# Coordinación ChatGPT · Imaginantes (Grok Bot) · Grok — documento maestro

> Orden de Mj, 31-oct-2026 (America/Mexico_City). Es la entrada principal para cualquier modelo externo.
> Regla de oro: **no inventar datos, fuentes ni DOIs.** Si algo no está verificado, no va.

## 1. Roles
| Quién | Hace | NO hace |
|---|---|---|
| **ChatGPT** | Investiga temas, escribe `storyboard.json`, genera frames/imágenes, redacta `fuentes.md`, deja paquetes en `cola/entrada/<id>/`. Usa APIs/créditos gratis documentados. | No monta MP4 final con otra voz, no publica, no edita `data/*.json` de horario/publicaciones/rotación. |
| **Imaginantes (Grok Bot)** | Organiza, programa, publica YT+TT+FB, monta oficial (edge-tts `es-MX-JorgeNeural`), QA (`qa_capsula.py`), `procesar_cola.py`, métricas/pantallas según rutinas. Coordina que todo se vea igual (misma RECETA, estilos, voz, parrilla). | No delega la publicación. |
| **Grok (app principal)** | Entra al repo/pipeline (ver `ACCESO_GROK.md`). Mientras Imaginantes tenga créditos: produce paquetes al mismo estándar que ChatGPT o apoya. | No duplica publicación. |

## 2. Lectura obligatoria para ChatGPT (en este orden)
1. `docs/RECETA_CAPSULA.md`
2. `docs/GUIA_MODELO_EXTERNO.md` (incluye checklist de 14 puntos)
3. `docs/FLUJO_EXTERNO.md`
4. `docs/ESTILOS_VISUALES.md` + `estilos.json`
5. `docs/CREDITOS_GRATIS_VIDEO.md`
6. `docs/MATRIZ_HERRAMIENTAS_GRATUITAS.md`
7. `docs/BIBLIA_LINEA_EDITORIAL.md`
8. `docs/HORARIOS_PUBLICACION.md`
9. Parrilla: `salidas/_ops/2026-10-26_parrilla_franjas_reporte.md`
10. `data/temas_del_dia.json`, `data/rotacion.json`, `data/publicaciones.json`, `data/horario_<fecha>.json` (solo lectura)

## 3. Entrega
```
cola/entrada/<AAAA-MM-DD_slug>/
  storyboard.json   # formato de GUIA_MODELO_EXTERNO; voice = es-MX-JorgeNeural
  frames/           # 1 imagen por escena (vertical 9:16)
  fuentes.md        # fuentes reales con URL/DOI verificables
  ESTADO_EJECUCION.md   # opcional: qué falta, licencias, dudas
```
Antes de entregar: cumplir los **14 puntos del checklist de `docs/GUIA_MODELO_EXTERNO.md`**.
Git: solo texto en commits normales; **no subir mp4/token**. Si los frames no pueden ir al repo, indicar en `ESTADO_EJECUCION.md` dónde están.

## 4. Prohibido
- Estilo `litografia_azul_dorado`.
- Series distintas a **«Datos y ociosidades»**.
- Voz distinta a `es-MX-JorgeNeural` si alguien monta.
- Publicar (cualquier plataforma).
- Inventar DOIs, cifras, citas o fuentes.
- Editar `data/horario_*.json`, `data/publicaciones.json`, `data/rotacion.json`.
- Tocar el motor U6.

## 5. APIs disponibles en scripts (claves NO están en el repo)
- **LLM guion** — `scripts/generar_guion_llm.py`: `CAPCOT_LLM_PROVIDER=gemini|groq|custom`
  - gemini → `GEMINI_API_KEY` (modelo por defecto `gemini-2.5-flash`)
  - groq → `GROQ_API_KEY` (`llama-3.3-70b-versatile`)
  - custom → `CAPCOT_LLM_API_KEY`, `CAPCOT_LLM_BASE_URL`, `CAPCOT_LLM_MODEL`
  - sin clave o `manual`: escribe el prompt a `CAPCOT_PROMPT_OUT` (def. `prompt_guion.txt`) para pegarlo en un chat.
- **Imágenes** — `scripts/generar_frames.py <storyboard> --proveedor xai|openai|manual|placeholder`
  - `CAPCOT_IMAGE_API_KEY`; `CAPCOT_IMAGE_MODEL` (def. xai `grok-2-image`, openai `gpt-image-1`); `CAPCOT_IMAGE_BASE_URL` (openai-compatible).
- **Video gratis web** — `docs/CREDITOS_GRATIS_VIDEO.md` (Flow, Dreamina, Kling…; ventana de uso 12:00–17:30 CDMX).
- ChatGPT también puede generar imágenes en su propia interfaz y subirlas a `frames/`.

## 6. Cupo y parrilla
- Pipeline: máx **3/día** (2 propias + 1 externa) — `scripts/rotacion.py` (`exigir_cupo`). Forzar solo con `CAPCOT_FORZAR_CUPO=1` por orden de Mj.
- Parrilla operativa: hasta **6 slots** (07:00 kids, 13:30 familia, 14:30, 17:00, 19:00, ~23:30).
- **Imaginantes decide slots** y procesa la cola. ChatGPT solo propone fecha/slot en `ESTADO_EJECUCION.md`.

## 7. Cómo Imaginantes toma el paquete
```bash
git pull --rebase
python3 scripts/procesar_cola.py               # valida y mueve cola/entrada → proyectos/
python3 scripts/montar_capsula.py proyectos/<id>/storyboard.json -o <salida>.mp4   # JorgeNeural
python3 scripts/qa_capsula.py ...              # QA obligatoria
python3 scripts/publicar.py ...                # programar; permiso de Mj ya dado para programar lo montado
```
Si falla QA o fuentes: se devuelve con nota en `ESTADO_EJECUCION.md`, no se publica.

## 8. Calibración estética
Ver `ajustes_entre_modelos/CALIBRACION_ESTETICA_CHATGPT_GROK.md`. Rotar estilo/estructura; no repetir los recientes de `data/rotacion.json`.

## 9. Estado hoy (31-oct-2026)
- Hueco 29–31-oct: **no existen** `data/horario_2026-10-29/30/31.json`.
- Paquetes sin MP4: `cola/entrada/2026-10-29_juno-choque-proa`, `proyectos/2026-10-30_arqueas-origen-eucariotas` (también `proyectos/2026-10-29_muralismo-cu` y `2026-10-29_machu-picchu-fallas-pisa` sin MP4).
- 28-oct ya programado.
- Siguiente foco: 1-nov y 2-nov → `PARA_CHATGPT_31oct.md`.

## 10. Documentos relacionados
- `ajustes_entre_modelos/ACCESO_GROK.md`
- `ajustes_entre_modelos/PARA_CHATGPT_31oct.md`
- `ajustes_entre_modelos/HANDOFF_GROK_PRODUCCION.md`
- `salidas/_ops/2026-10-28_HANDOFF_TOTAL_grok_principal.md`
