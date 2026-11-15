# Flujo externo — cápsula de actualidad científica de ChatGPT (3.ª del día)

**Reparto (2026-10-24, Mj):** ChatGPT **propone y produce** la cápsula de actualidad científica del día y la deja en cola; **nunca publica** (ni YouTube ni TikTok). Grok Bot **revisa, hace QA y publica**.

> **Antes de producir, lee [docs/GUIA_MODELO_EXTERNO.md](GUIA_MODELO_EXTERNO.md)**: qué leer, el estilo por tema, la voz obligatoria (JorgeNeural +7 %; si no la tienes, entrega sin montar), el formato del paquete en `cola/entrada/<project_id>/`, el checklist de autocrítica y el anti-ejemplo Ideonella.

## 0. Cómo elige ChatGPT el tema
- Noticia científica o de investigación de los **últimos ~7 días** (estudio publicado, descubrimiento, misión espacial, salud, clima), buscada en fuentes reales: Nature/Science news, EurekAlert, ScienceDaily, Phys.org, NASA/ESA/JAXA, SINC, Agencia Informativa Conacyt, UNAM Global. Puede partir de `python3 scripts/tendencias.py` (feeds de ciencia primero).
- Abre el **estudio original** (DOI) o comunicado oficial y solo afirma lo que este respalda. `trend_source.tipo = "noticia_cientifica"` con `url`, `estudio_doi` y `fecha_publicacion`.
- Sin deportes, crimen ni tragedias; tema distinto a los de `data/temas_del_dia.json`.

Límite: **3 cápsulas por día = 2 propias (capsula_diaria) + 1 externa (cola)**, cada una en una ventana distinta (9–11, 13–15, 18–21 h America/Mexico_City). Lo exige `rotacion.exigir_cupo(fecha, origen)`.

## 1. Qué entrega ChatGPT (paquete en cola, sin publicar)
Siguiendo **docs/RECETA_CAPSULA.md** (JSON `storyboard_vertical`, §3), deja **una** de estas dos formas en `cola/entrada/`:
- `cola/entrada/<project_id>.json`: solo el storyboard. Los frames se generan con `--proveedor-img`.
- `cola/entrada/<project_id>/storyboard.json` + `frames/escena_XX.png`: storyboard con imágenes propias.
- Opcional: `cola/entrada/<project_id>/capsula.mp4` ya montado + `fuentes.md`. Grok Bot igual lo revisa y, si no cumple la receta, lo vuelve a montar desde el storyboard.

Requisitos: `project_id` único, `trend_source.termino` (tema), `estructura` (mito_vs_dato | pregunta | historia | comparacion | sabias_que), escenas con `capa` (mapa y dato/gráfico), `sources` verificables (DOI/URL), 60–95 s (límite que impone scripts/validar_storyboard.py). Opcional: `resumen` (va al caption de TikTok).

**Antes de escribir**, el modelo (o quien lo opere) consulta `data/temas_del_dia.json`: el tema no puede coincidir con otro del día. Tampoco debe repetir la estructura, el estilo ni la música de las otras cápsulas del día (ver data/publicaciones.json y data/rotacion.json).

## 2. Revisión y publicación (solo Grok Bot; mismo pipeline y misma cola)
Grok Bot verifica la noticia y el DOI antes de procesar; si la fuente no respalda el guion, marca `rechazado` con motivo en `data/cola.json`.
```
cd /workspace/capcot && python3 scripts/procesar_cola.py --publicar --programar   # --dry-run para probar
```
1. Toma la primera entrada y la registra en `data/cola.json` (estado `recibido`).
2. Si el tema ya aparece en `data/temas_del_dia.json`: estado `rechazado`.
3. Copia la entrada a `cola/<fecha>_<id>/` y corre `validar_storyboard.py --check-doi`. Si falla: estado `invalido`.
4. Llama `capsula_diaria.py --storyboard ... --origen externa`. Esto renderiza, pasa QA (duración, estructura, capas, licencias, metadata YouTube) y genera metadata.json y tiktok.json. Si QA pasa, publica en YouTube (programado) y registra en data/publicaciones.json, data/rotacion.json y data/temas_del_dia.json.
5. Estado final en `data/cola.json`: `publicado_yt+pendiente_tiktok`, `renderizado+pendiente_tiktok` o `fallo`.

Si QA falla, no se publica; el detalle queda en `resumen.json` → `fallas`.

## 3. TikTok
Cada paquete trae `tiktok.json`: `caption`, `mp4`, `estado: pendiente_tiktok` y una hora sugerida. El agente principal publica por navegador con un agente de escritorio y luego marca `publicado_tiktok` y la `url`.

## 4. Git
`cola/**` con medios queda fuera de git (*.mp4, *.png, *.jpg). Solo se versiona data/cola.json y data/temas_del_dia.json.
