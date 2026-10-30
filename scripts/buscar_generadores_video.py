#!/usr/bin/env python3
"""Discover public video-generation APIs, open models and integration projects.

Uses GitHub's public repository search API. No provider account is created,
no API keys are requested, and no generation credits are consumed.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "investigacion" / "generadores_video"
QUERIES = [
    '"text to video" generation API',
    'video generation model inference API',
    'ComfyUI video generation workflow',
    'open source image to video text to video',
    'video generation API client SDK',
]
PROVIDER_DOCS = [
    {
        "provider": "Runway",
        "category": "API comercial",
        "documentation": "https://docs.dev.runwayml.com/",
        "verification": "Revisar endpoints, modelos, duración, precio y disponibilidad regional."
    },
    {
        "provider": "xAI",
        "category": "API comercial",
        "documentation": "https://docs.x.ai/docs/guides/video",
        "verification": "Revisar modelos, duración, precio, límites y acceso."
    },
    {
        "provider": "Google Vertex AI / Veo",
        "category": "API comercial",
        "documentation": "https://cloud.google.com/vertex-ai/generative-ai/docs/video/overview",
        "verification": "Revisar disponibilidad, cuotas, duración, precio y requisitos de proyecto."
    },
    {
        "provider": "ComfyUI",
        "category": "Interfaz y API autoalojable",
        "documentation": "https://github.com/comfyanonymous/ComfyUI",
        "verification": "Revisar workflows de video, modelos, VRAM y despliegue."
    },
    {
        "provider": "Hugging Face Diffusers",
        "category": "Biblioteca / modelos abiertos",
        "documentation": "https://huggingface.co/docs/diffusers",
        "verification": "Buscar pipelines de text-to-video e image-to-video y sus licencias."
    },
    {
        "provider": "fal",
        "category": "API agregadora comercial",
        "documentation": "https://fal.ai/docs",
        "verification": "Revisar modelo concreto, precio por segundo, límites y licencia del modelo."
    },
]

def github_search(query: str) -> list[dict]:
    params = urllib.parse.urlencode({"q": query + " fork:false", "sort": "updated", "order": "desc", "per_page": 30})
    url = "https://api.github.com/search/repositories?" + params
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "CAPCOT-video-discovery/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            payload = json.loads(response.read().decode("utf-8"))
        return payload.get("items", [])
    except Exception as exc:
        print(f"AVISO: búsqueda GitHub falló para {query!r}: {exc}", file=sys.stderr)
        return []

def classify(repo: dict) -> list[str]:
    text = " ".join([
        repo.get("name") or "",
        repo.get("description") or "",
        " ".join(repo.get("topics") or []),
    ]).lower()
    tags = []
    if any(x in text for x in ("api", "sdk", "endpoint", "client")):
        tags.append("integración/API probable")
    if any(x in text for x in ("text-to-video", "text to video", "t2v")):
        tags.append("texto a video")
    if any(x in text for x in ("image-to-video", "image to video", "i2v")):
        tags.append("imagen a video")
    if any(x in text for x in ("comfyui", "workflow", "node")):
        tags.append("workflow/interfaz")
    if any(x in text for x in ("open source", "opensource", "weights", "diffusers")):
        tags.append("modelo/código abierto probable")
    if not tags:
        tags.append("candidato por revisar")
    return tags

def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    found: dict[str, dict] = {}
    for query in QUERIES:
        for item in github_search(query):
            full_name = item.get("full_name")
            if not full_name:
                continue
            found[full_name] = {
                "repository": full_name,
                "url": item.get("html_url"),
                "description": item.get("description"),
                "stars": item.get("stargazers_count", 0),
                "forks": item.get("forks_count", 0),
                "language": item.get("language"),
                "license": (item.get("license") or {}).get("spdx_id"),
                "created_at": item.get("created_at"),
                "updated_at": item.get("updated_at"),
                "pushed_at": item.get("pushed_at"),
                "archived": item.get("archived", False),
                "topics": item.get("topics", []),
                "candidate_tags": classify(item),
                "verification_status": "PENDIENTE: revisar README, licencia, código, demos y requisitos",
            }
        time.sleep(1)

    repos = sorted(found.values(), key=lambda x: (x["archived"], x["pushed_at"] or "", x["stars"]), reverse=False)
    repos.sort(key=lambda x: (x["archived"], -(x["stars"] or 0)))
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "GitHub public repository search API",
        "queries": QUERIES,
        "method_limitations": [
            "Los resultados son candidatos, no certificaciones de que una API funcione.",
            "La búsqueda de repositorios no sustituye la lectura de documentación ni una prueba real.",
            "Precio, cuotas, licencia comercial, duración, resolución y disponibilidad regional deben verificarse en fuente oficial.",
            "No se ejecuta código de terceros ni se consumen créditos.",
        ],
        "provider_documentation_candidates": PROVIDER_DOCS,
        "repositories": repos[:100],
    }
    json_path = OUT / "catalogo_actual.json"
    md_path = OUT / "catalogo_actual.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Catálogo de generadores de video — CAPCOT",
        "",
        f"Actualizado (UTC): {report['generated_at_utc']}",
        "",
        "> Los elementos son candidatos. Ninguno se considera integrado, gratuito o apto para uso comercial sin verificación.",
        "",
        "## Documentación de proveedores y proyectos",
        "",
        "| Proveedor/proyecto | Tipo | Documentación | Verificación pendiente |",
        "|---|---|---|---|",
    ]
    for p in PROVIDER_DOCS:
        lines.append(f"| {p['provider']} | {p['category']} | {p['documentation']} | {p['verification']} |")
    lines += ["", "## Repositorios públicos candidatos", ""]
    if not repos:
        lines.append("No se obtuvieron resultados. Revisar cuota o disponibilidad de GitHub Search API.")
    else:
        lines += [
            "| Repositorio | Estrellas | Última actualización | Licencia declarada | Clasificación |",
            "|---|---:|---|---|---|",
        ]
        for r in repos[:100]:
            license_name = r["license"] or "No declarada"
            tags = ", ".join(r["candidate_tags"])
            lines.append(
                f"| [{r['repository']}]({r['url']}) | {r['stars']} | {r['pushed_at'] or 'N/D'} | {license_name} | {tags} |"
            )
    lines += [
        "",
        "## Criterios obligatorios antes de elegir",
        "",
        "- Entrada: texto, imagen, video de referencia; soporte de imagen-a-video y extensión.",
        "- Duración por clip, resolución, fps, relación 9:16 y control de cámara.",
        "- Consistencia entre clips: referencias, seed, personaje/objeto, último frame y extensión.",
        "- Acceso: API oficial, API comunitaria, interfaz autoalojable o notebook; autenticación y límites.",
        "- Economía: costo por segundo/clip, créditos gratuitos, concurrencia y reintentos.",
        "- Legal: licencia del código y del modelo por separado; uso comercial y restricciones de salida.",
        "- Operación: disponibilidad, mantenimiento, cola asíncrona, almacenamiento y descarga.",
        "- Integración CAPCOT: montaje con FFmpeg, subtítulos, voz y control editorial.",
        "",
        "## Estrategia de ensamblaje",
        "",
        "No descartar servicios por generar clips cortos. Calcular escenas y duración acumulada; usar clips consecutivos, extensión desde el último frame, frames estáticos animados, generación por lotes o combinación de proveedores. El render final debe cumplir el rango de duración de la receta vigente y pasar QA.",
        "",
        "## Límites de esta ejecución",
        "",
        "- Este proceso solo descubre y cataloga; no instala, ejecuta ni contrata servicios.",
        "- La presencia de una URL o repositorio no demuestra que el servicio siga operativo.",
        "- Los campos no verificados permanecen explícitamente pendientes.",
    ]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Repositorios candidatos: {len(repos)}")
    print(f"JSON: {json_path.relative_to(ROOT)}")
    print(f"Markdown: {md_path.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
