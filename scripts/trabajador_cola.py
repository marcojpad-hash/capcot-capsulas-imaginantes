#!/usr/bin/env python3
"""Trabajador de cola — CAPCOT / motor U6.

Lee Issues con etiqueta `cola`, toma el más viejo, ejecuta según `tipo:`
(validar | texto | auditoria | motor), abre un PR con la evidencia y
actualiza la etiqueta a `hecho` o `bloqueado`. Corre solo en GitHub Actions
(gratis en repo público) o a mano con --dry-run / --self-test.

Uso:
  python3 scripts/trabajador_cola.py [--repo owner/repo] [--once]
  python3 scripts/trabajador_cola.py --dry-run
  python3 scripts/trabajador_cola.py --self-test

Reglas:
- Nunca toca main directo: todo cambio va por PR desde trabajador/<n>.
- Nunca fusiona, nunca borra nada.
- Verificar antes de entregar: un artefacto que no pasa su validador no abre PR.
- Sin Issue no hay trabajo. Verificar por PR/commit, nunca por acuse.
- Solo stdlib + CLI `gh` (preinstalado en los runners de Actions).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "openai/gpt-oss-120b"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent"

LABELS = {
    "cola": ("Cola de trabajo, esperando trabajador", "fbca04"),
    "en-progreso": ("Trabajo en curso", "1d76db"),
    "hecho": ("Entregado con evidencia", "0e8a16"),
    "bloqueado": ("No se pudo, ver motivo en el Issue", "d93f0b"),
}

REGLAS_TEXTO = (
    "REGLAS QUE NO SE PUEDEN OLVIDAR:\n"
    "- No inventes datos, fuentes ni DOIs. Si algo no está verificado, no va.\n"
    "- Devuelve SOLO el artefacto pedido, sin explicaciones ni saludos.\n"
    "- Si la tarea pide un JSON, devuelve solo JSON válido.\n"
)

REGLAS_AUDITORIA = (
    "REGLAS DE AUDITORÍA:\n"
    "- Eres un auditor independiente. NO escribiste el artefacto que auditas.\n"
    "- No fabriques ejecuciones: si no corriste el código, escribe "
    "\"no ejecutado\", nunca inventes un resultado.\n"
    "- Cada hallazgo lleva archivo, línea y evidencia.\n"
    "- Devuelve el informe completo, sin explicaciones fuera de él.\n"
)

FAKE_ISSUE = {
    "number": 999,
    "title": "[capsula] Prueba en seco",
    "createdAt": "2026-11-15T00:00:00Z",
    "body": (
        "tipo: validar\n"
        "ruta: storyboard.json\n"
        "\n"
        "## Qué\n"
        "Validar el storyboard de prueba.\n"
    ),
}


def log(msg):
    print(f"[trabajador] {msg}", flush=True)


def sh(cmd, cwd=None, timeout=600, input_text=None):
    return subprocess.run(
        cmd, cwd=cwd, capture_output=True, text=True,
        timeout=timeout, input=input_text,
    )


class GitHub:
    """Mutaciones en GitHub vía CLI `gh` (autenticada en Actions por GH_TOKEN)."""

    def __init__(self, repo, dry_run=False):
        self.repo = repo
        self.dry_run = dry_run

    def gh(self, *args, input_text=None):
        cmd = ["gh"] + list(args) + ["--repo", self.repo]
        if self.dry_run:
            log("DRY-RUN gh " + " ".join(args))
            return ""
        r = sh(cmd, timeout=120, input_text=input_text)
        if r.returncode != 0:
            raise RuntimeError(
                "gh " + " ".join(args) + " falló: " + r.stderr.strip()[:500]
            )
        return r.stdout

    def ensure_labels(self):
        for name, (desc, color) in LABELS.items():
            if self.dry_run:
                log(f"DRY-RUN: etiqueta {name} ok")
                continue
            r = sh(["gh", "label", "create", name, "--color", color,
                    "--description", desc, "--repo", self.repo], timeout=60)
            if r.returncode != 0 and "already exists" not in r.stderr:
                log(f"aviso: no se pudo crear la etiqueta {name}: "
                    f"{r.stderr.strip()[:200]}")

    def list_queue(self):
        if self.dry_run:
            return [dict(FAKE_ISSUE)]
        out = self.gh("issue", "list", "--label", "cola", "--state", "open",
                      "--limit", "20", "--json", "number,title,body,createdAt")
        issues = json.loads(out or "[]")
        issues.sort(key=lambda i: i.get("createdAt", ""))
        return issues

    def comment(self, number, text):
        if self.dry_run:
            log(f"DRY-RUN comentario #{number}:\n{text}")
            return
        self.gh("issue", "comment", str(number), "--body", text)

    def set_labels(self, number, add=(), remove=()):
        for a in add:
            self.gh("issue", "edit", str(number), "--add-label", a)
        for x in remove:
            self.gh("issue", "edit", str(number), "--remove-label", x)

    def open_pr(self, branch, title, body):
        if self.dry_run:
            log(f"DRY-RUN PR desde {branch}: {title}")
            return "https://example.invalid/pr/0"
        out = self.gh("pr", "create", "--head", branch,
                      "--title", title, "--body", body)
        return out.strip()


def section(body, heading):
    """Devuelve el texto bajo un encabezado ## <heading> (hasta el próximo ##)."""
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s|\Z)",
                  body or "", re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else ""


def parse_body(body):
    body = body or ""

    def field(name):
        m = re.search(rf"^{name}:\s*(.+)$", body, re.MULTILINE | re.IGNORECASE)
        return m.group(1).strip() if m else ""

    que = section(body, "Qué") or section(body, "Que")
    fuentes = section(body, "Fuentes reales")
    tarea = "\n\n".join(x for x in [que, fuentes] if x) or body
    return {
        "tipo": field("tipo").lower(),
        "ruta": field("ruta"),
        "tarea": tarea,
        "body": body,
    }


def llamar_groq(prompt, api_key, model=GROQ_MODEL):
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4000,
    }).encode("utf-8")
    req = urllib.request.Request(
        GROQ_URL, data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "capcot-trabajador-cola/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = json.load(resp)
    return data["choices"][0]["message"]["content"]


def llamar_gemini(prompt, api_key):
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 4000},
    }).encode("utf-8")
    req = urllib.request.Request(
        GEMINI_URL + "?key=" + api_key, data=body,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = json.load(resp)
    return data["candidates"][0]["content"]["parts"][0]["text"]


def job_validar(ruta, repo_root):
    """Corre el validador que corresponde al artefacto. Sin LLM."""
    p = Path(repo_root) / ruta
    if not p.exists():
        return False, f"ruta no existe: {ruta}", []
    if p.suffix == ".json" and "storyboard" in p.name:
        cmd = [sys.executable, "scripts/validar_storyboard.py",
               str(p), "--check-doi"]
        r = sh(cmd, cwd=repo_root, timeout=300)
        ok = r.returncode == 0
        out = (r.stdout + r.stderr).strip()[-2000:]
        return ok, f"validar_storyboard.py --check-doi: exit {r.returncode}\n{out}", []
    if p.suffix == ".mp4":
        sb = p.parent / "storyboard.json"
        if not sb.exists():
            return False, "qa_capsula necesita storyboard.json junto al mp4", []
        r = sh([sys.executable, "scripts/qa_capsula.py", str(p), str(sb)],
               cwd=repo_root, timeout=600)
        ok = r.returncode == 0
        out = (r.stdout + r.stderr).strip()[-2000:]
        return ok, f"qa_capsula.py: exit {r.returncode}\n{out}", []
    return False, f"sin validador conocido para: {ruta}", []


def job_texto(parsed, ruta, repo_root, dry_run=False):
    """Genera el artefacto con Groq (Gemini como segunda opinión si hay clave).

    tipo=texto: el artefacto ES el storyboard, se escribe en `ruta` y se
    valida como storyboard antes del PR.
    tipo=auditoria: el artefacto es un INFORME en prosa sobre el archivo de
    `ruta`. NUNCA se escribe sobre `ruta` (eso destruía el storyboard y
    luego el validador fallaba al leer prosa como JSON). El informe va a
    AUDITORIA.md junto al archivo auditado y no se valida como storyboard.
    """
    groq_key = os.environ.get("GROQ_API_KEY", "")
    if not groq_key:
        return (False,
                "falta el secreto GROQ_API_KEY en el repo "
                "(Settings > Secrets and variables > Actions).", [])
    es_auditoria = parsed["tipo"] == "auditoria"
    reglas = REGLAS_AUDITORIA if es_auditoria else REGLAS_TEXTO
    prompt = reglas + "\nTAREA:\n" + parsed["tarea"]
    if dry_run:
        log("DRY-RUN: llamaría a Groq con un prompt de "
            f"{len(prompt)} caracteres para escribir {ruta}")
        return True, "dry-run: texto no generado", []
    if es_auditoria:
        # El archivo a auditar debe existir y leerse; si no, no hay
        # auditoría que hacer. No se exige que pase el validador
        # estructural: la auditoría narrativa puede (y debe) señalar
        # esos problemas como hallazgos.
        # El modelo audita el CONTENIDO REAL del archivo, no la
        # descripción del Issue: si no ve el archivo, inventa líneas,
        # enlaces y números de PR (pasó con cuásares, 2026-11-15).
        origen = Path(repo_root) / ruta
        if not origen.exists():
            return False, f"el archivo a auditar no existe: {ruta}", []
        try:
            contenido = origen.read_text(encoding="utf-8")
            if origen.suffix == ".json":
                json.loads(contenido)
        except Exception as e:
            return False, f"el archivo a auditar no es JSON válido: {e}", []
        prompt += ("\nARCHIVO A AUDITAR (contenido real; cita solo lo que "
                   "aparece aquí, no inventes líneas, enlaces ni números "
                   "de PR):\n" + contenido[:30000])
    try:
        texto = llamar_groq(prompt, groq_key)
    except Exception as e:
        return False, f"Groq no respondió: {e}", []
    if es_auditoria:
        destino = Path(repo_root) / Path(ruta).parent / "AUDITORIA.md"
    else:
        destino = Path(repo_root) / ruta
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto, encoding="utf-8")
    if not es_auditoria:
        # Verificar el artefacto antes de abrir el PR (solo cuando el
        # artefacto es el storyboard generado, no un informe en prosa).
        ok, salida, _ = job_validar(ruta, repo_root)
        if not ok:
            destino.unlink(missing_ok=True)
            return False, ("el artefacto generado NO pasa su validador, "
                           "no se abre PR:\n" + salida), []
    gemini_key = os.environ.get("GEMINI_API_KEY", "")
    nota = "Generado con Groq gpt-oss-120b"
    if gemini_key:
        try:
            segunda = llamar_gemini(
                "Revisa este artefacto y dime solo si tiene errores graves, "
                "en una línea. Artefacto:\n" + texto, gemini_key)
            nota += f". Segunda opinión (Gemini): {segunda.strip()[:300]}"
        except Exception as e:
            nota += f". Gemini no respondió ({e}), se entrega solo con Groq."
    rel = str(destino.relative_to(repo_root))
    return True, nota + f". Artefacto escrito en {rel}.", [rel]


def job_motor(parsed, ruta, repo_root, dry_run=False):
    """Corre el motor sobre la entrada de `ruta:` y deja recibo + nota."""
    runner = Path(repo_root) / "motor" / "correr_estandar.py"
    if not runner.exists():
        return (False,
                "este repo no tiene motor/correr_estandar.py; el trabajo "
                "motor va en motor-u6-storage.", [])
    entrada = Path(repo_root) / ruta
    if not entrada.exists():
        return False, f"entrada no existe: {ruta}", []
    nombre = entrada.stem.replace("entrada_", "")
    if dry_run:
        log(f"DRY-RUN: correría el motor sobre {ruta} como {nombre}")
        return True, "dry-run: motor no corrido", []
    r = sh([sys.executable, "motor/correr_estandar.py", str(entrada), nombre],
           cwd=repo_root, timeout=900)
    recibo = Path(repo_root) / "motor" / f"RESULT_{nombre}_RECIBO_EJECUCION.json"
    if r.returncode != 0 or not recibo.exists():
        return False, (f"correr_estandar.py exit {r.returncode}\n"
                       + (r.stdout + r.stderr).strip()[-2000:]), []
    nota_path = Path(repo_root) / "motor" / f"NOTA_REPRO_{nombre}.md"
    nota_path.write_text(
        f"# Reproducción {nombre} — trabajador de cola\n\n"
        f"- Entrada: {ruta}\n"
        f"- Exit: {r.returncode}\n"
        f"- Recibo: motor/{recibo.name}\n"
        f"- Salida (últimas líneas):\n```\n"
        f"{(r.stdout + r.stderr).strip()[-1500:]}\n```\n",
        encoding="utf-8")
    return True, (f"motor corrido, exit {r.returncode}, "
                   f"recibo {recibo.name}."), [str(recibo.relative_to(repo_root)),
                                              str(nota_path.relative_to(repo_root))]


def commit_and_pr(gh, repo_root, number, files, title, body, dry_run=False):
    branch = f"trabajador/{number}"
    if dry_run:
        log(f"DRY-RUN: commit de {files} en {branch} y PR: {title}")
        return "https://example.invalid/pr/0"
    sh(["git", "config", "user.name", "trabajador-cola"], cwd=repo_root)
    sh(["git", "config", "user.email", "trabajador-cola@capcot.local"],
       cwd=repo_root)
    sh(["git", "checkout", "-b", branch], cwd=repo_root)
    for f in files:
        sh(["git", "add", f], cwd=repo_root)
    r = sh(["git", "commit", "-m", title], cwd=repo_root)
    if r.returncode != 0:
        raise RuntimeError("git commit falló: " + r.stderr.strip()[:500])
    sh(["git", "push", "-u", "origin", branch], cwd=repo_root)
    return gh.open_pr(branch, title, body)


def procesar_issue(gh, repo_root, issue, dry_run=False):
    number = issue["number"]
    parsed = parse_body(issue.get("body", ""))
    tipo, ruta = parsed["tipo"], parsed["ruta"]
    log(f"#{number}: tipo={tipo} ruta={ruta}")
    if not tipo or not ruta:
        gh.comment(number, "Bloqueado: el Issue no trae `tipo:` ni `ruta:` "
                            "legibles. Ver la plantilla que corresponde.")
        gh.set_labels(number, add=["bloqueado"], remove=["cola"])
        return False
    gh.set_labels(number, add=["en-progreso"], remove=["cola"])
    gh.comment(number, f"Trabajador de cola: tomado. Tipo `{tipo}`, "
                       f"ruta `{ruta}`. Empiezo.")
    try:
        if tipo == "validar":
            ok, summary, files = job_validar(ruta, repo_root)
        elif tipo in ("texto", "auditoria"):
            ok, summary, files = job_texto(parsed, ruta, repo_root, dry_run)
        elif tipo == "motor":
            ok, summary, files = job_motor(parsed, ruta, repo_root, dry_run)
        else:
            ok, summary, files = (
                False, f"tipo desconocido: `{tipo}` (usa validar | texto | "
                       "auditoria | motor).", [])
    except Exception as e:
        ok, summary, files = False, f"error del trabajador: {e}", []
    if ok and files:
        title = f"[trabajador] {issue.get('title', '')} (#{number})"
        try:
            url = commit_and_pr(gh, repo_root, number, files, title,
                                f"Cierra #{number}.\n\n{summary}", dry_run)
        except Exception as e:
            gh.comment(number, f"Bloqueado al abrir el PR: {e}")
            gh.set_labels(number, add=["bloqueado"], remove=["en-progreso"])
            return False
        gh.comment(number, f"Hecho. PR: {url}\n\n{summary}")
        gh.set_labels(number, add=["hecho"], remove=["en-progreso"])
        return True
    if ok:
        gh.comment(number, f"Hecho (sin cambios en archivos).\n\n{summary}")
        gh.set_labels(number, add=["hecho"], remove=["en-progreso"])
        return True
    gh.comment(number, "Bloqueado.\n\n" + summary +
               "\n\nQué lo desbloquea: corregir lo que dice el mensaje y "
               "volver a etiquetar el Issue con `cola`.")
    gh.set_labels(number, add=["bloqueado"], remove=["en-progreso"])
    return False


def self_test():
    """Prueba el trabajador sin tocar GitHub ni gastar llamadas de modelo."""
    checks = []

    def check(name, cond, detail=""):
        checks.append((name, bool(cond), detail))
        print(("PASS " if cond else "FAIL ") + name +
              ((" :: " + str(detail)) if detail else ""))

    # 1. parse_body lee tipo/ruta y las secciones Qué/Fuentes.
    p = parse_body(FAKE_ISSUE["body"])
    check("parse tipo", p["tipo"] == "validar", p["tipo"])
    check("parse ruta", p["ruta"] == "storyboard.json", p["ruta"])
    check("parse tarea", "Validar el storyboard" in p["tarea"])
    # 2. El payload de Groq se construye (sin enviar).
    payload = json.dumps({
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": REGLAS_TEXTO + "hola"}],
        "max_tokens": 4000,
    })
    check("payload groq válido", json.loads(payload)["model"] == GROQ_MODEL)
    # 3. job_validar corre el validador real sobre un storyboard real que pasa.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "scripts").mkdir()
        val = root / "scripts" / "validar_storyboard.py"
        try:
            req = urllib.request.Request(
                "https://raw.githubusercontent.com/marcojpad-hash/"
                "capcot-capsulas-imaginantes/feature/"
                "capcot-video-discovery-continuity/cola/entrada/"
                "2026-11-15_dato-dia-diapausa-lestes-sponsa/storyboard.json",
                headers={"User-Agent": "capcot-trabajador-cola/1.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                sb = resp.read()
            (root / "storyboard.json").write_bytes(sb)
            req2 = urllib.request.Request(
                "https://raw.githubusercontent.com/marcojpad-hash/"
                "capcot-capsulas-imaginantes/main/scripts/validar_storyboard.py",
                headers={"User-Agent": "capcot-trabajador-cola/1.0"})
            with urllib.request.urlopen(req2, timeout=60) as resp:
                val.write_bytes(resp.read())
            ok, salida, _ = job_validar("storyboard.json", str(root))
            check("validar storyboard real (Lestes) pasa", ok, salida[-300:])
        except Exception as e:
            check("validar storyboard real (Lestes) pasa", False, str(e)[:300])
    # 4. tipo=auditoria: el informe va a AUDITORIA.md y NO toca el storyboard.
    # (Bug 2026-11-15: job_texto escribía el informe sobre `ruta` y luego
    # job_validar lo leía como JSON; siempre fallaba en el carácter 0.)
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "proyectos" / "prueba").mkdir(parents=True)
        sb = root / "proyectos" / "prueba" / "storyboard.json"
        sb.write_text('{"title": "prueba", "scenes": []}', encoding="utf-8")
        antes = sb.read_text(encoding="utf-8")
        real_groq = globals()["llamar_groq"]
        prompts = []
        def _fake_groq(prompt, key):
            prompts.append(prompt)
            return "# Auditoría\n\nVeredicto: pasa."
        globals()["llamar_groq"] = _fake_groq
        os.environ["GROQ_API_KEY"] = "test-sin-llamada"
        os.environ.pop("GEMINI_API_KEY", None)
        try:
            ok_a, nota_a, files_a = job_texto(
                {"tipo": "auditoria", "tarea": "Auditar el storyboard."},
                "proyectos/prueba/storyboard.json", str(root))
        finally:
            globals()["llamar_groq"] = real_groq
            os.environ.pop("GROQ_API_KEY", None)
        informe = root / "proyectos" / "prueba" / "AUDITORIA.md"
        check("auditoria no toca el storyboard",
              sb.read_text(encoding="utf-8") == antes)
        check("auditoria escribe AUDITORIA.md",
              ok_a and informe.exists() and
              "Auditoría" in informe.read_text(encoding="utf-8"),
              nota_a[-200:])
        check("auditoria devuelve el informe para el PR",
              files_a == ["proyectos/prueba/AUDITORIA.md"], files_a)
        check("auditoria manda el contenido real al modelo",
              bool(prompts) and '"title": "prueba"' in prompts[0] and
              "no inventes" in prompts[0])
    bad = [c for c in checks if not c[1]]
    print(f"SELF-TEST: {len(checks) - len(bad)}/{len(checks)} PASS")
    return 0 if not bad else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.environ.get(
        "GITHUB_REPOSITORY", "marcojpad-hash/capcot-capsulas-imaginantes"))
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--label", default="cola")
    ap.add_argument("--max-issues", type=int, default=5)
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    gh = GitHub(args.repo, dry_run=args.dry_run)
    gh.ensure_labels()
    issues = gh.list_queue()
    if not issues:
        log("sin trabajo en cola.")
        return 0
    log(f"{len(issues)} Issue(s) en cola; proceso hasta {args.max_issues}.")
    hechas = 0
    for issue in issues[:args.max_issues]:
        try:
            procesar_issue(gh, args.repo_root, issue, args.dry_run)
            hechas += 1
        except Exception as e:
            log(f"#{issue.get('number')}: error no controlado: {e}")
        if args.once:
            break
    log(f"listo: {hechas} Issue(s) procesados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
