# demo-001 v2 — cambios (2026-10-24)

## Voz
Elegida: **edge-tts es-MX-DaliaNeural**, rate +4 %, pitch -1 Hz, síntesis frase por frase con
pausas por puntuación (`PAUSAS` en `scripts/montar_capsula.py`; edge-tts no acepta SSML `<break>`).
- es-MX-JorgeNeural (v1): la que sonaba robótica; descartada.
- es-ES-AlvaroNeural: natural, pero acento de España (público es-MX).
- es-US-AlonsoNeural / es-ES-Ximena: correctas, menos cálidas.
- No existen voces `es-MX-*Multilingual` en edge-tts. Las multilingües (en-US-AndrewMultilingualNeural,
  Ava, Emma) hablan español con prosodia más conversacional pero acento neutro/no mexicano y fallos
  intermitentes en frases cortas: alternativa 2.
- Piper `es_MX-claude-high` (local, offline, libre): buena alternativa sin red, pero no da marcas de
  palabra (subtítulos) y es menos expresiva: alternativa 3 / fallback.
- Coqui XTTS v2: no evaluado a fondo; licencia CPML no comercial, ~2 GB y lento en CPU.
Muestras: /workspace/imaginantes/voz_muestras/muestra_{1,2,3}_*.wav (no versionadas).

## Imágenes
11 frames de papel recortado generados con el generador de imágenes del agente (no hay API key de
imágenes en el entorno). Los prompts por escena están en `image_prompt` del storyboard.
Frames y placeholders v1 (frames_v1_placeholder/) no se versionan.

## Datos verificados
- 10-20 Mt a ~10 km de altura: NASA Ames Tunguska Workshop (2019), NTRS 20190002302 (SRC-004).
  El rango 10-15 Mt no aparece como consenso; se usa 10-20 Mt.
- ~2000 km²: Jenniskens et al. 2019 (SRC-002). La cifra 2150 km² es antigua y fue cuestionada
  (Sci. Rep. 2025, doi:10.1038/s41598-025-98362-9), por eso se dice "unos dos mil".
