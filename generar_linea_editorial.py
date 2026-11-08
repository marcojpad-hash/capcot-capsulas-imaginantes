#!/usr/bin/env python3
"""Genera docs/LINEA_EDITORIAL_VISUAL.json para CAPCOT.

Junta en UN solo JSON la línea editorial (BIBLIA_LINEA_EDITORIAL.md),
el catálogo de estilos (scripts/estilos.json, leído tal cual, sin
transcribir a mano) y la serie de skills de generación
(~/workspace/custom-skills/capcot-*), para que cualquier modelo que lo
lea use la misma plantilla, la misma voz y el mismo rango de duración,
sin inventar versiones.

Uso:
    python3 generar_linea_editorial.py
Salida:
    docs/LINEA_EDITORIAL_VISUAL.json
"""
import json
import os

REPO = os.path.dirname(os.path.abspath(__file__))
# El script vive en la raíz del repo CAPCOT (junto a scripts/ y docs/).
# Si se corre desde otro lado, REPO es el cwd del script.
if not os.path.exists(os.path.join(REPO, "scripts", "estilos.json")):
    REPO = os.path.expanduser(
        "~/workspace/cbm-repos/capcot-capsulas-imaginantes"
    )

with open(os.path.join(REPO, "scripts", "estilos.json"), encoding="utf-8") as f:
    catalogo = json.load(f)

linea = {
    "formato": 1,
    "nombre": "Línea editorial visual — Datos y ociosidades (CAPCOT)",
    "version": "1.0.0",
    "fecha": "2026-11-08",
    "fuentes": [
        "docs/BIBLIA_LINEA_EDITORIAL.md",
        "docs/ESTILOS_VISUALES.md",
        "docs/PLAN_MAESTRO_AUTOMATICO.md",
        "docs/RECETA_CAPSULA.md",
        "scripts/estilos.json",
        "templates/storyboard_vertical.template.json",
    ],
    "nota": (
        "JSON canónico y único de la línea editorial visual. Si algo choca "
        "con docs/PLAN_MAESTRO_AUTOMATICO.md, manda el plan maestro. "
        "Los valores en valores_fijos NO se cambian: son los que los modelos "
        "venían alterando (otra voz, otra plantilla visual, otra duración)."
    ),
    "serie": "Datos y ociosidades",
    "language": "es-MX",
    "valores_fijos": {
        "aspect_ratio": "9:16",
        "resolution": "1080x1920",
        "fps": 30,
        "duracion_segundos": {"min": 60, "max": 95, "objetivo": [75, 90]},
        "escenas": 6,
        "duracion_escena_segundos": 10,
        "loudness_lufs": -14,
        "voz_oficial": "es-MX-JorgeNeural",
        "voz_rate": "+7%",
        "voz_pitch": "-2Hz",
        "voz_fallback": "es_MX-ald-medium (Piper, offline)",
        "cierre_hablado": "Esto fue Datos y ociosidades.",
        "cortinilla_fuentes": {
            "titulo": "Fuentes",
            "firma": "Datos y ociosidades · @datosyociosidades",
            "aviso": "Imágenes generadas con IA. Voz sintética.",
            "duration_seconds": 6,
        },
        "export_filename": "capsula.mp4",
    },
    "reglas_editoriales": [
        "Un estilo por cápsula, elegido del catálogo según la temática; nunca se repite el estilo de la cápsula anterior.",
        "9:16 con sujeto grande y sin texto dentro de la imagen (el image_prompt siempre termina en 'vertical 9:16, no text').",
        "Rigor con fuentes: cada afirmación es DATO (sale de la fuente con URL) o INFERENCIA (criterio de diseño). No se inventan datos, fuentes ni DOIs.",
        "Máximo 2-3 cápsulas al día.",
        "La narración es exactamente el texto de 'narration' de cada escena del storyboard.json; no se reescribe ni se improvisa.",
        "La voz es la oficial (es-MX-JorgeNeural) o el fallback Piper (es_MX-ald-medium). No se usa otra voz.",
        "La duración es 60-95 s (objetivo 75-90). No se cambia el rango.",
        "La plantilla visual sale del catálogo (prompt_base). No se inventa un estilo nuevo fuera del catálogo.",
        "La capa de tratamiento Nostalgia 85-95 se aplica en el montaje (rótulos, transiciones, apertura y cierre), nunca cambia el prompt_base.",
        "Límites de la nostalgia: inspiración de época sí; logos, personajes, sprites, fotogramas o música con IP no. Nada grotesco ni ultra-estético.",
        "Tono de dibujo SÍ: línea limpia estilo HB/MGM, formas simples, fondos pintados, humor seco. NO: grotesco tipo Ren & Stimpy, hiper-estilización geométrica, CalArts / nueva ola de CN, 3D brillante.",
    ],
    "catalogo_estilos": {
        "fuente": "scripts/estilos.json",
        "regla_seleccion": (
            "El estilo se elige según la temática de cada cápsula "
            "(scripts/rotar_estilo.py) y nunca es el de la cápsula anterior. "
            "El prompt_base de cada estilo se usa tal cual; solo se le suma "
            "la descripción de la escena."
        ),
        "estilos": catalogo,
    },
    "pipeline_skills": {
        "nota": (
            "Serie de skills que genera la cápsula con código, sin el "
            "generador de video de Muse (que quemaba los tokens: los 7 "
            "videos de Mpemba empujaron el límite semanal del 0% al 62%). "
            "Se ejecutan en orden; cada una recibe lo que dejó la anterior."
        ),
        "orden": [
            "capcot-guion",
            "capcot-frames",
            "capcot-narracion",
            "capcot-montaje",
            "capcot-qa",
        ],
        "skills": [
            {
                "id": "capcot-guion",
                "archivo": "~/workspace/custom-skills/capcot-guion/SKILL.md",
                "hace": "Escribe storyboard.json con fuentes, escenas y narración.",
                "entrada": "Investigación con fuentes reales.",
                "salida": "cola/entrada/<project_id>/storyboard.json y fuentes.md",
            },
            {
                "id": "capcot-frames",
                "archivo": "~/workspace/custom-skills/capcot-frames/SKILL.md",
                "hace": "Genera las imágenes de cada escena con el prompt_base del estilo elegido.",
                "entrada": "storyboard.json (image_prompt por escena).",
                "salida": "frames/scene_001.jpg ... scene_006.jpg",
                "estado": "explainroo es el candidato; NO instalado ni probado. Falta la prueba con Barreleye.",
            },
            {
                "id": "capcot-narracion",
                "archivo": "~/workspace/custom-skills/capcot-narracion/SKILL.md",
                "hace": "Narra el guion en es-MX, gratis y local (Piper es_MX-ald-medium; JorgeNeural donde edge-tts responde).",
                "entrada": "Narración de cada escena del storyboard.json.",
                "salida": "audio/narracion.mp3 (volumen a -6 dB).",
            },
            {
                "id": "capcot-montaje",
                "archivo": "~/workspace/custom-skills/capcot-montaje/SKILL.md",
                "hace": "Arma el MP4 9:16 con ffmpeg/OpenMontage: imágenes + narración + subtítulos + cortinilla.",
                "entrada": "frames/, audio/narracion.mp3, storyboard.json.",
                "salida": "capsula.mp4 (1080x1920, 30 fps, -14 LUFS).",
            },
            {
                "id": "capcot-qa",
                "archivo": "~/workspace/custom-skills/capcot-qa/SKILL.md",
                "hace": "Revisa formato, audio, fuentes y cierre antes de entregar. Da PASA o NO PASA con fallos concretos.",
                "entrada": "capsula.mp4 y storyboard.json.",
                "salida": "Veredicto PASA / NO PASA.",
            },
        ],
    },
    "storyboard": {
        "plantilla": "templates/storyboard_vertical.template.json",
        "campos_clave": [
            "project_id",
            "serie",
            "language",
            "aspect_ratio",
            "estructura",
            "estilo_id",
            "estilo_visual",
            "target_duration_seconds",
            "voice",
            "export {filename, fps, resolution, loudness_lufs}",
            "cortinilla_fuentes",
            "sources",
            "scenes[] {id, arc, duration_seconds, image_prompt, narration, on_screen_text, source_ids, asset_filename}",
        ],
    },
    "reparto": {
        "nota": "Quién hace qué. No se cambia por fuera de este JSON.",
        "ChatGPT": "Investiga y escribe el storyboard; deja el paquete en cola/entrada.",
        "Grok_e_Imaginantes": "Montan el MP4 oficial con voz es-MX-JorgeNeural, corren el QA oficial y programan/publican.",
        "Pecas": "Prepara borradores, verifica fuentes y narraciones, coordina entre modelos y revisa YouTube Studio. No monta el MP4 final ni publica.",
        "Copilot": "Modelo nativo de GitHub con el encargo del repositorio.",
    },
    "revision_diaria": {
        "nota": (
            "Para que el canal no se quede sin publicar si Imaginantes se "
            "detiene. La revisión la hacen los modelos constructores "
            "(Pecas, ChatGPT y el bot) por lo menos una vez al día."
        ),
        "frecuencia": "Por lo menos una vez al día.",
        "que_revisar": [
            "¿Hubo publicaciones hoy? (data/publicaciones.json, data/cierre_diario/, YouTube Studio.)",
            "¿La cola tiene paquetes sin procesar? (cola/entrada/.)",
            "¿Imaginantes publicó o está detenido?",
        ],
        "si_imaginantes_se_detiene": (
            "Si Imaginantes deja de publicar, los modelos constructores "
            "(Pecas y ChatGPT) generan la cápsula con la serie de skills "
            "de este JSON (guion, frames, narración, montaje, QA) y la "
            "publican, para que el contenido no se detenga. El relevo no "
            "espera a que alguien lo pida: es automático al detectar que "
            "no hubo publicación."
        ),
        "quien_revisa": ["Pecas", "ChatGPT", "Imaginantes (Grok Bot)"],
    },
    "creditos_imaginantes": {
        "nota": (
            "Imaginantes ya se pausó antes por créditos y la cola se atascó "
            "sin publicaciones desde el 26-oct. Hay que estar al pendiente "
            "para no quedarse sin publicar."
        ),
        "que_saber": "Cuántos créditos le quedan a Imaginantes.",
        "como_saberlo": (
            "En la revisión diaria, el orquestador (tools/orquestador) "
            "reporta el estado del tablero, incluida la cola atascada y si "
            "Imaginantes está pausado. Si el estado de créditos no se puede "
            "ver desde el tablero, se pregunta directo y se anota en el "
            "cierre diario (data/cierre_diario/)."
        ),
        "alerta": (
            "Si los créditos están agotados o no se pueden verificar, se "
            "activa el relevo de revision_diaria (los constructores generan "
            "y publican) y se avisa a Marco en una línea."
        ),
        "fecha_limite_conocida": "2026-12-05: se acaban créditos de una versión de prueba (servicio por confirmar).",
    },
    "tendencias": {
        "nota": (
            "Análisis de los trends que están pegando últimamente, marcado "
            "dentro de la línea editorial, para que los temas vayan con lo "
            "que la audiencia está viendo y no se pierda tracción."
        ),
        "herramientas": [
            "scripts/tendencias_estilos.py (frecuencia semanal; Google News RSS sobre estéticas en TikTok y Shorts, mezcla 50/50 con el peso previo).",
            "scripts/tendencias.py",
            "data/tendencias_estilos.json",
        ],
        "regla": (
            "El análisis de tendencias se hace de forma regular y se marca "
            "en la línea editorial (qué trend, en qué franja pega, qué "
            "estilo del catálogo le corresponde). Los temas nuevos se eligen "
            "con el trend en mente, sin romper las reglas editoriales "
            "(fuentes reales, un estilo por cápsula, 9:16, sin texto en la "
            "imagen)."
        ),
    },
    "formato_imaginantes": {
        "nota": (
            "El formato oficial de Imaginantes, para que no se olvide. Es el "
            "montaje oficial: no se cambia por fuera de este JSON."
        ),
        "scripts": ["scripts/montar_capsula.py", "scripts/qa_capsula.py"],
        "montaje": "MP4 oficial con voz es-MX-JorgeNeural (+7%, -2Hz), subtítulos, cortinilla de fuentes y capas de dato/mapa.",
        "formato": "1080x1920, 9:16, 30 fps, -14 LUFS, 60-95 s (objetivo 75-90), 6 escenas de ~10 s.",
        "cierre": "Esto fue Datos y ociosidades.",
        "programacion": "Lote programado a las 07:00 en YouTube, TikTok y Facebook.",
        "qa": "El QA oficial lo corre Imaginantes (scripts/qa_capsula.py). La skill capcot-qa es la revisión previa, no el QA oficial.",
    },
}

salida = os.path.join(REPO, "docs", "LINEA_EDITORIAL_VISUAL.json")
with open(salida, "w", encoding="utf-8") as f:
    json.dump(linea, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("Escrito:", salida)
print("Estilos en catálogo:", len(catalogo))
print("Tamaño:", os.path.getsize(salida), "bytes")
