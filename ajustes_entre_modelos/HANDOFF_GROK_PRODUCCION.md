# HANDOFF — Grok (app con GitHub) produce cápsulas de variedad
Actualizado: 2026-10-24 18:30 CDMX. Pedido de Mj (24-oct).

## Roles
- **Grok (app):** produce cápsulas EXTRA con variedad temática. Entrega paquetes; no publica salvo OK explícito de Mj.
- **Imaginantes / Grok Bot (box):** rutina diaria, reportes, métricas, montaje oficial, QA oficial y envío del TikTok a Mj (lo sube él desde el teléfono).

## Lee antes de producir (obligatorio, en este orden)
1. `docs/RECETA_CAPSULA.md` (reglas, arco, formato `storyboard_vertical`).
2. `docs/GUIA_MODELO_EXTERNO.md` (voz, capas, fuentes, checklist de 14 puntos, anti-ejemplo Ideonella).
3. `docs/FLUJO_EXTERNO.md` (cola/entrada → montaje).
4. `docs/ESTILOS_VISUALES.md` + `scripts/estilos.json` (prompt_base por estilo).
5. `data/temas_del_dia.json`, `data/rotacion.json`, `data/publicaciones.json` (no repetir tema/estilo/estructura).
Ejemplo de formato correcto: `proyectos/2026-10-24_ideonella-pet/storyboard.json` y `proyectos/2026-10-24_serpientes-que-ruedan/storyboard.json`.

## Temas a rotar (cápsula cultural; uno distinto por cápsula)
1. Naturaleza  2. Datos médicos/salud  3. Datos curiosos (tipo serpientes que ruedan)
4. Noticias IA/tecnología  5. Investigación (estudio recién publicado)  6. Docencia/ciencias sociales.
**Prioridad: ciencia reciente (≤7 días) con fuentes reales y DOI que resuelva.** No inventes datos ni fuentes.

## Cupo
- Máx ~2 propias + 1 externa por día.
- **Hoy 24-oct ya hay 4 publicadas → NO se publica nada más hoy.** Grok arma el lote para **mañana 25-oct** (y siguientes) como paquetes en `cola/entrada/` o `proyectos/`.

## Publicados hoy 24-oct (no duplicar temas)
| Tema | Estilo | YouTube id |
|---|---|---|
| Fenómeno El Niño | linograbado | 5D96DmjvioU |
| Serpientes que ruedan | disney_clasico | ZrUtKs7Ty7U |
| Ideonella sakaiensis come PET | claymation | r1AhsPOAS_o |
| Aves temen más a mujeres | garabato_cuaderno | ZmejLrdEslU |
También en lote previo (sin publicar aún / ver salidas/): tardígrado, Chicxulub.

## Estilos
Elige por temática desde el catálogo. **No uses** linograbado, disney_clasico, claymation ni garabato_cuaderno (usados hoy), ni el estilo de la última entrada de `data/rotacion.json`. Un estilo por cápsula; cada `image_prompt` = `prompt_base` exacto + " + " + escena en inglés; 9:16, sin texto.

## Cómo generar (paso a paso, comandos reales; repo en `/workspace/capcot` o tu clon)
0. `git clone git@github.com:marcojpad-hash/capcot-capsulas-imaginantes.git capcot && cd capcot ` ; instala `ffmpeg` y `pip install edge-tts` (no hay requirements.txt).
1. **Tema + fuentes:** `python3 scripts/tendencias.py --dias 7 --json` (feeds de ciencia primero; `--geo MX`; `--sin-ciencia` solo para comparar). Elige uno de la rotación de arriba, abre el estudio y anota DOI/URL.
2. **Storyboard:** escribe `proyectos/AAAA-MM-DD_slug/storyboard.json` según RECETA (7–9 escenas, 170–235 palabras, 60–95 s, `titulo` ≤6 palabras, capa `mapa` + capa `dato`/`grafico`, `source_ids` en cada afirmación, `estructura` distinta a las de hoy, `ambiente`/`sfx` por escena, serie «Datos y ociosidades», cierre «Esto fue Datos y ociosidades.»). Voz:
   `"voice": {"engine":"edge-tts","voice_id":"es-MX-JorgeNeural","rate":"+7%","pitch":"-2Hz","pad_seconds":0.3,"modo_pausas":"continuo"}`
   Valida: `python3 scripts/validar_storyboard.py proyectos/<id>/storyboard.json --check-doi`
3. **Frames:** genera una imagen 9:16 por escena con tu generador de imágenes (Grok Imagine) usando el `image_prompt`, guárdala con el nombre `asset_filename` en `proyectos/<id>/frames/`. Alternativa en box: `python3 scripts/generar_frames.py proyectos/<id>/storyboard.json --proveedor manual` (lista lo que falta).
4. **Montar:** `python3 scripts/capsula_diaria.py --storyboard proyectos/<id>/storyboard.json --fecha AAAA-MM-DD --dry-run` (prueba) y luego sin `--dry-run` (sin `--publicar`). Secuencia manual equivalente: `python3 scripts/montar_capsula.py proyectos/<id>/storyboard.json -o salidas/<id>/salida.mp4` (edge-tts + cama `scripts/cama_sonora.py` incluidas en el pipeline) → QA oficial: `python3 scripts/qa_capsula.py salidas/<id>/salida.mp4 proyectos/<id>/storyboard.json` (código 0 = pasa).
   **Si no puedes correr edge-tts JorgeNeural, NO montes:** deja `cola/entrada/<id>/{storyboard.json,frames/,fuentes.md}` y Grok Bot corre `python3 scripts/procesar_cola.py` → `capsula_diaria.py --origen externa` → `qa_capsula.py`.
5. **Metadata:** `python3 scripts/metadata.py salidas/<id>/ proyectos/<id>/storyboard.json` (título, descripción, tags, caption).
6. **YouTube — SOLO con OK explícito de Mj:** primero `python3 scripts/publicar.py salidas/<id>/ --plataforma yt` (simulación), luego `python3 scripts/publicar.py salidas/<id>/ --plataforma yt --ejecutar [--privacidad public|private] [--publish-at ISO]`. Requiere token en `~/.capcot/` del box (nunca en el repo). Sin OK → no publicar.
7. **TikTok:** NO por navegador ni API. Entrega `salida.mp4` + caption (de metadata) para que Mj lo suba desde su teléfono.

## Entrega
- Mínimo: storyboard + frames + fuentes.md en `cola/entrada/<id>/` (o `proyectos/<id>/`). Ideal: paquete montado en `salidas/<id>/` con QA oficial.
- Commit sin mp4/png/tokens (ya en .gitignore). Mensaje: `Paquete <id> (<estilo>, <estructura>) para <fecha>`.
- Pasa el checklist de 14 puntos de GUIA_MODELO_EXTERNO antes de entregar.

## Actualización obligatoria — Bot no duplica preproducción

Este handoff histórico queda subordinado a `docs/PROTOCOLO_DESCARGA_CARGA_GROK.md`. En el flujo actual, ChatGPT entrega tema seleccionado, investigación verificada, fuentes, guion final, storyboard, prompts por escena y metadata. **Grok Bot no debe volver a ejecutar los pasos 1 y 2 de investigación/storyboard por rutina**: debe revisar que el paquete esté completo, registrar recepción y pasar a generar frames/medios, voz/audio, montaje, render y QA. Si falta evidencia o hay un error factual, devuelve a ChatGPT el claim y el campo exactos; ChatGPT investiga y entrega el parche. Bot corrige únicamente defectos de producción y cambios locales. No rehacer todo el guion ni regenerar escenas aprobadas sin motivo de QA. Las correcciones también consumen tokens: mantenerlas acotadas. Los pasos históricos de research y storyboard solo aplican cuando Mj asigne expresamente a Bot un trabajo extraordinario de preproducción.
