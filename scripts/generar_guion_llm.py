#!/usr/bin/env python3
"""Genera storyboard vertical (JSON) con un LLM compatible con la API de chat de OpenAI.
Variables: CAPCOT_LLM_API_KEY (obligatoria), CAPCOT_LLM_BASE_URL (def. https://api.x.ai/v1),
CAPCOT_LLM_MODEL (def. grok-4). Sin clave sale con código 3 (el orquestador usa entonces un guion manual).
Uso: python3 scripts/generar_guion_llm.py --tema "el niño fenomeno" --noticias tendencias.json -o proyectos/x/storyboard.json
Las fuentes que proponga el LLM se VERIFICAN después (validar_storyboard.py --check-doi); nunca se aceptan sin verificar."""
import argparse, json, os, sys, urllib.request
PROMPT = """Eres guionista de micro-cápsulas científicas verticales estilo Imaginantes (periodismo informativo-narrativo).
Reglas: 60-90 s totales, 120-190 palabras, 7-9 escenas de 6-12 s; primera escena arc=hook_medias_res (in medias res, frase <=12 palabras);
luego desarrollo, cierre_historia y una última reflexion_o_pregunta (reflexión ontológica o pregunta abierta). La imagen narra: 2-3 escenas sin voz.
La voz eleva a idea, no describe. Metáfora y personificación. Ninguna cifra sin source_ids. Fuentes REALES con DOI o URL institucional que
existan; si no estás seguro de una fuente, NO la incluyas. Estilo visual único para esta cápsula: {estilo}.
Devuelve SOLO JSON con claves: title, estilo_visual, sources[{{id,cita_corta,doi?,url,supports[]}}],
scenes[{{id,arc,duration_seconds,narration,on_screen_text,visual_description,image_prompt,source_ids[]}}].
Tema del día: {tema}. Noticias relacionadas: {noticias}"""

def llamar(prompt):
    key = os.environ.get("CAPCOT_LLM_API_KEY")
    if not key: print("FALTA CAPCOT_LLM_API_KEY", file=sys.stderr); sys.exit(3)
    base = os.environ.get("CAPCOT_LLM_BASE_URL", "https://api.x.ai/v1"); model = os.environ.get("CAPCOT_LLM_MODEL", "grok-4")
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}],
                       "response_format": {"type": "json_object"}}).encode()
    req = urllib.request.Request(base + "/chat/completions", body, {"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    return json.loads(json.load(urllib.request.urlopen(req, timeout=180))["choices"][0]["message"]["content"])

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--tema", required=True); ap.add_argument("--noticias", default="")
    ap.add_argument("--estilo", default="elige uno distinto de papel recortado (p.ej. linograbado, acuarela, miniatura, risografía)")
    ap.add_argument("--id", default="capsula"); ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    g = llamar(PROMPT.format(tema=a.tema, noticias=a.noticias[:1500], estilo=a.estilo))
    for i, s in enumerate(g["scenes"]): s.setdefault("asset_filename", f"frames/scene_{i+1:03}.png")
    sb = {"project_id": a.id, "serie": "Imaginantes de la ciencia", "language": "es-MX", "aspect_ratio": "9:16",
          "target_duration_seconds": 80, "trend_source": {"tipo": "google_trends_rss", "rss_geo": "MX", "termino": a.tema},
          "voice": {"engine": "edge-tts", "voice_id": "es-MX-JorgeNeural", "rate": "-8%", "pitch": "-2Hz", "pad_seconds": 0.8},
          "cortinilla_fuentes": {"duration_seconds": 6, "titulo": "Fuentes", "aviso": "Imágenes generadas con IA. Voz sintética.", "bg_rgb": [18, 16, 14]},
          "audio": {"music_asset": "", "music_volume": 0.25},
          "export": {"filename": a.id + ".mp4", "resolution": "1080x1920", "fps": 30, "subtitle_max_words": 3}, **g}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(sb, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(a.out)
