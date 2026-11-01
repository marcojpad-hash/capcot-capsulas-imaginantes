#!/usr/bin/env python3
"""Genera storyboard vertical (JSON) con un LLM compatible con la API de chat de OpenAI.
Proveedor GRATUITO por defecto, elegido con CAPCOT_LLM_PROVIDER:
  gemini (def.)  -> GEMINI_API_KEY, endpoint OpenAI-compatible de Google AI Studio, modelo gemini-2.5-flash (free tier)
  groq           -> GROQ_API_KEY, https://api.groq.com/openai/v1, modelo llama-3.3-70b-versatile (free tier)
  custom         -> CAPCOT_LLM_API_KEY + CAPCOT_LLM_BASE_URL + CAPCOT_LLM_MODEL (cualquier API OpenAI-compatible)
  manual         -> no llama a nada.
Nunca usa un modelo de pago por defecto. Si falta la clave o el proveedor es manual, escribe prompt_guion.txt y sale con
código 3: el agente (o Mj) escribe el storyboard a mano siguiendo docs/RECETA_CAPSULA.md.
Uso: python3 scripts/generar_guion_llm.py --tema "el niño fenomeno" --noticias tendencias.json -o proyectos/x/storyboard.json
Las fuentes que proponga el LLM se VERIFICAN después (validar_storyboard.py --check-doi); nunca se aceptan sin verificar."""
import argparse, json, os, sys, urllib.request
PROMPT = """Eres guionista de Datos y ociosidades: divulgación científica narrativa, español de México.
Duración total {duracion} s incluyendo 6 s de fuentes; produce 7-9 escenas y 170-235 palabras narradas. Usa el arco hook_medias_res → desarrollo → cierre_historia → reflexion_o_pregunta.
Antes de redactar, diseña una sola pregunta central, promesa, stakes, giro científico, límite de evidencia y payoff. Abre in medias res: acción, anomalía o consecuencia ya en curso; una definición o pregunta genérica NO cuenta. Cada escena debe avanzar la pregunta central y declarar dramatic_beat, scene_function, causal_bridge_from_previous, question_state, reason_to_continue y new_information. La narración concatenada debe leerse como una sola pieza oral: cada escena deriva de la anterior. Cifras: explica qué se midió, bajo qué condiciones y qué significa. No añadas datos para rellenar tiempo; profundiza mecanismo, consecuencia, límite o transición. No inventes protagonistas ni episodios.
Incluye capa mapa con coordenadas verificables cuando el fenómeno tenga localización y capa dato/grafico con fuente primaria. Ninguna cifra sin source_ids. Usa fuentes reales; si no puedes verificar, decláralo pendiente. Estilo visual: {estilo}. Devuelve SOLO JSON con title, titulo (máximo 6 palabras), sources[{id,cita_corta,doi,url,supports[]}], narrative_contract{premise,central_question,promise,stakes,scientific_turn,evidence_limit,payoff}, scenes[{id,arc,duration_seconds,narration,on_screen_text,sfx[],visual_description,image_prompt,source_ids[],dramatic_beat,scene_function,causal_bridge_from_previous,question_state,reason_to_continue,new_information}]. Tema: {tema}. Noticias: {noticias}"""

def llamar(prompt):
    prov = os.environ.get("CAPCOT_LLM_PROVIDER", "gemini").lower()
    P = {"gemini": ("GEMINI_API_KEY", "https://generativelanguage.googleapis.com/v1beta/openai", "gemini-2.5-flash"),
         "groq": ("GROQ_API_KEY", "https://api.groq.com/openai/v1", "llama-3.3-70b-versatile"),
         "custom": ("CAPCOT_LLM_API_KEY", os.environ.get("CAPCOT_LLM_BASE_URL", ""), os.environ.get("CAPCOT_LLM_MODEL", ""))}
    if prov == "manual" or prov not in P or not os.environ.get(P[prov][0]):
        open(os.environ.get("CAPCOT_PROMPT_OUT", "prompt_guion.txt"), "w", encoding="utf-8").write(prompt)
        print(f"MODO MANUAL (proveedor={prov}): prompt guardado; el agente escribe el storyboard", file=sys.stderr); sys.exit(3)
    key = os.environ[P[prov][0]]; base = P[prov][1]; model = os.environ.get("CAPCOT_LLM_MODEL", P[prov][2]) if prov != "custom" else P[prov][2]
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}],
                       "response_format": {"type": "json_object"}}).encode()
    req = urllib.request.Request(base + "/chat/completions", body, {"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    return json.loads(json.load(urllib.request.urlopen(req, timeout=180))["choices"][0]["message"]["content"])

if __name__ == "__main__":
    import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    ap = argparse.ArgumentParser(); ap.add_argument("--tema", required=True); ap.add_argument("--noticias", default="")
    ap.add_argument("--estilo", default="elige uno distinto de papel recortado (p.ej. linograbado, acuarela, miniatura, risografía)")
    ap.add_argument("--id", default="capsula"); ap.add_argument("--estructura", default="pregunta"); ap.add_argument("--duracion", type=int, default=75); ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    g = llamar(PROMPT.format(tema=a.tema, noticias=a.noticias[:1500], estilo=a.estilo, duracion=a.duracion, estructura=a.estructura, estructura_desc=__import__("rotacion").ESTRUCTURAS[a.estructura]))
    for s in g["scenes"]:
        s.pop("asset_filename", None); s.pop("asset_type", None)
    sb = {"project_id": a.id, "serie": "Datos y ociosidades", "language": "es-MX", "aspect_ratio": "9:16",
          "target_duration_seconds": a.duracion, "estructura": a.estructura, "trend_source": {"tipo": "google_trends_rss", "rss_geo": "MX", "termino": a.tema},
          "voice": {"engine": "edge-tts", "voice_id": "es-MX-JorgeNeural", "rate": "+7%", "pitch": "-2Hz", "pad_seconds": 0.3},
          "cortinilla_fuentes": {"duration_seconds": 6, "titulo": "Fuentes", "aviso": "Fuentes consultadas", "bg_rgb": [18, 16, 14]},
          "audio": {"music_asset": None, "music_plan": "Pendiente de producción por Grok"},
          "export": {"resolution": "1080x1920", "fps": 30, "render_status": "NOT_GENERATED"},
          "narrative_qa": {"status": "FAIL", "score": 0, "review_basis": "lectura_en_frio_solo_narracion", "central_question_reconstructable": False, "opening_is_in_medias_res": False, "every_scene_advances": False, "transitions_are_causal": False, "data_is_interpreted": False, "scientific_turn_present": False, "payoff_resolves_opening": False, "critical_flags": ["PENDIENTE_REVISION_INDEPENDIENTE"]},
          "publicacion": {"status": "PENDIENTE_DECISION_GROK"}, "approved_assets": [], **g}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(sb, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(a.out)
