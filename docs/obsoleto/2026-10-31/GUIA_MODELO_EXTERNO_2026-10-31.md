# Guía para modelo externo (ChatGPT u otro) — cómo producir una cápsula de «Datos y ociosidades»

Esta guía es obligatoria para cualquier modelo que no sea Grok Bot. Tú **produces un paquete**; Grok Bot lo revisa, lo monta con el pipeline oficial, corre el QA oficial y decide si se publica. **Tú nunca publicas.**

Canal y serie: **Datos y ociosidades** (@datosyociosidades). No existe otra serie: nunca escribas «Imaginantes de la ciencia» ni otro nombre en `serie`, títulos, cortinilla o cierre. El cierre hablado es siempre «Esto fue Datos y ociosidades.».

## 1. Qué lees antes de producir (en este orden)
1. `docs/RECETA_CAPSULA.md`: reglas editoriales, arco, duración, formato JSON `storyboard_vertical`.
2. `docs/ESTILOS_VISUALES.md` y `scripts/estilos.json`: catálogo de estilos con su `prompt_base` y sus temas.
3. `data/temas_del_dia.json`: temas ya usados hoy. El tuyo no puede repetirse.
4. `data/rotacion.json`: estructura, estilo, cama musical y duración de las cápsulas recientes.
5. `data/publicaciones.json`: lo publicado (títulos y temas), para no repetir.

## 2. Estética: el estilo se elige POR TEMA
- Elige el estilo cuyo campo «Temas» encaje con tu tema (p. ej. bacterias o laboratorio → `claymation`; mar o historia → `linograbado`; mitos → `teatro_sombras`).
- **Nunca uses el estilo de la cápsula anterior** (último registro de `data/rotacion.json`) ni uno usado hoy.
- Un solo estilo para todas las escenas. Cada `image_prompt` = `prompt_base` del estilo, tal cual, + « + » + la escena concreta en inglés. Frames verticales 9:16, sin texto dentro de la imagen.
- Las referencias visuales de Mj están en `referencias_estilo/`, pero esa carpeta no se sube al repo (está en .gitignore) y quizá no puedas verla. En ese caso usa **solo** las descripciones y `prompt_base` del catálogo (ESTILOS_VISUALES.md / estilos.json). **No inventes estilos** ni mezcles uno nuevo.

## 3. Voz (obligatoria)
- `"voice": {"engine": "edge-tts", "voice_id": "es-MX-JorgeNeural", "rate": "+7%", "pitch": "-2Hz", "pad_seconds": 0.3, "modo_pausas": "continuo"}`, con pausas de unos 0.3 s entre frases.
- Si en tu entorno no puedes usar edge-tts con JorgeNeural, **no montes el video**. Entrega SOLO storyboard + frames + fuentes y Grok Bot pone la voz. Prohibido sustituirla por eSpeak, gTTS, la voz del sistema u otra.

## 4. Contenido y formato
- **Subtítulos:** cubren el 100 % del guion (lo genera el pipeline a partir de `narration`). Escribe la narración completa en cada escena, sin texto suelto fuera de `narration`.
- **Título-gancho:** campo `titulo` (≤6 palabras), distinto del `title` de YouTube. Sale en pantalla desde el frame 0 de la escena 1, subrayado.
- **Capas:** al menos una `capa` de tipo `mapa` (lugar real con `region` [lon0, lon1, lat0, lat1] y `puntos` con lon/lat; base Natural Earth) y una de tipo `dato` (`valor`, `etiqueta`, `fuente`) o `grafico`.
- **Fuentes:** cada afirmación lleva `source_ids`. Cada fuente con **DOI real** que resuelva en doi.org/Crossref, o comunicado oficial. Lee el estudio y afirma solo lo que dice. No inventes DOIs ni cifras.
- **Duración:** 60–95 s (ideal 75–90), 170–235 palabras, 7–9 escenas.
- **Estructura:** `estructura` ∈ mito_vs_dato | pregunta | historia | comparacion | sabias_que, y **distinta a las ya usadas hoy** (ver rotacion.json).
- **Sonido:** en cada escena pon `ambiente` y `sfx` acordes al plano. Deja que el pipeline elija la música (`audio.music_asset` vacío o `sintetico:*`). No repitas la cama de otra cápsula del día.

## 5. Dónde dejas el paquete
```
cola/entrada/<project_id>/
  storyboard.json      # storyboard_vertical completo
  frames/scene_001.jpg …  # mismo nombre que asset_filename de cada escena
  fuentes.md           # cita, DOI/URL y qué respalda cada fuente
```
`project_id` = `AAAA-MM-DD_slug`. **NUNCA publiques** en YouTube ni en TikTok, no edites `data/*.json` y no hagas tu propio render «final». Grok Bot corre `procesar_cola.py` → `capsula_diaria.py --origen externa` → `qa_capsula.py`.

## 6. Checklist de autocrítica (todas deben ser «sí» antes de dejar el paquete)
| # | Pregunta | Sí/No |
|---|---|---|
| 1 | ¿Leí RECETA_CAPSULA, ESTILOS_VISUALES, temas_del_dia, rotacion y publicaciones? | |
| 2 | ¿El tema no aparece en temas_del_dia.json de hoy? | |
| 3 | ¿El estilo sale del catálogo, encaja con el tema y no es el de la cápsula anterior ni uno de hoy? | |
| 4 | ¿Cada image_prompt empieza con el prompt_base exacto y los frames son 9:16 sin texto? | |
| 5 | ¿La voz es edge-tts es-MX-JorgeNeural +7 %, pitch −2 Hz, pausas de ~0.3 s? (Si no la tengo: ¿entregué sin montar?) | |
| 6 | ¿`serie` es «Datos y ociosidades» y el cierre dice «Esto fue Datos y ociosidades.»? | |
| 7 | ¿Hay `titulo` gancho de ≤6 palabras? | |
| 8 | ¿Hay una capa mapa con coordenadas reales y una capa dato o gráfico con fuente? | |
| 9 | ¿Cada afirmación tiene source_ids, y cada fuente un DOI que resuelve y respalda lo dicho? | |
| 10 | ¿170–235 palabras y 60–95 s? | |
| 11 | ¿La estructura es distinta a las de hoy? | |
| 12 | ¿Cada escena tiene ambiente/sfx y no fijé una música ya usada hoy? | |
| 13 | ¿El paquete está en cola/entrada/<project_id>/ con storyboard.json, frames/ y fuentes.md? | |
| 14 | ¿NO publiqué nada, NO toqué data/ y NO presento un QA propio como si fuera el oficial? | |

## 7. Anti-ejemplo: Ideonella (2026-10-24)
El paquete `salidas/2026-10-24_ideonella-pet/` tenía buen tema y buenas fuentes con DOI, pero lo rehízo Grok Bot por estos errores:
- **Voz eSpeak** en lugar de JorgeNeural. Debió entregar sin montar.
- **Serie mal nombrada** («Imaginantes de la ciencia»).
- **Fuera del pipeline:** no se dejó en `cola/entrada/` ni se montó con capsula_diaria/montar_capsula, así que faltaban título-gancho subrayado, mapa Natural Earth y ambiente por plano.
- **QA propio no oficial** («16/16») presentado como aprobado. Solo cuenta `scripts/qa_capsula.py` corrido por Grok Bot.
- Prompts sin el `prompt_base` del catálogo.

Versión corregida: `salidas/2026-10-24_2026-10-24-ideonella-pet/` (storyboard en `proyectos/2026-10-24_ideonella-pet/storyboard.json`). Úsala como ejemplo de formato.


## 8. Continuidad audiovisual obligatoria
Antes de generar frames o clips, lee `docs/CONTINUIDAD_AUDIOVISUAL.md`. Cada cápsula debe declarar una biblia audiovisual única (`visual_identity`), identidad tipográfica (`typography_identity`) y voz maestra. No mezcles estilos ni cambies idioma, voz, tipografía, paleta, iluminación o acabado entre escenas. Cada prompt debe comenzar con el `prompt_base` exacto del catálogo. No agregues imágenes o planos que no estén declarados expresamente en `approved_assets`/storyboard. Para clips cortos se permite generación por segmentos y ensamblaje, siempre heredando la misma biblia audiovisual. Ejecuta `python scripts/validar_continuidad_audiovisual.py <storyboard.json>`; el resultado estructural no sustituye la revisión visual y auditiva integral. Si la voz oficial falla, no la sustituyas silenciosamente.
