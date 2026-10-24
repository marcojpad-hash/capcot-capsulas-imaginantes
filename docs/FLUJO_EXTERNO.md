# Flujo externo — 3.ª cápsula del día (ChatGPT u otro modelo)

Límite: **3 cápsulas por día = 2 propias (capsula_diaria) + 1 externa (cola)**, cada una en una ventana distinta (9–11, 13–15, 18–21 h America/Mexico_City). Lo exige `rotacion.exigir_cupo(fecha, origen)`.

## 1. Qué entrega el modelo externo
Siguiendo **docs/RECETA_CAPSULA.md** (JSON `storyboard_vertical`, §3), deja **una** de estas dos formas en `cola/entrada/`:
- `cola/entrada/<project_id>.json`: solo el storyboard. Los frames se generan con `--proveedor-img`.
- `cola/entrada/<project_id>/storyboard.json` + `frames/escena_XX.png`: storyboard con imágenes propias.

Requisitos: `project_id` único, `trend_source.termino` (tema), `estructura` (mito_vs_dato | pregunta | historia | comparacion | sabias_que), escenas con `capa` (mapa y dato/gráfico), `sources` verificables (DOI/URL), 60–120 s. Opcional: `resumen` (va al caption de TikTok).

**Antes de escribir**, el modelo (o quien lo opere) consulta `data/temas_del_dia.json`: el tema no puede coincidir con otro del día. Tampoco debe repetir la estructura, el estilo ni la música de las otras cápsulas del día (ver data/publicaciones.json y data/rotacion.json).

## 2. Proceso (mismo pipeline y misma cola)
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
