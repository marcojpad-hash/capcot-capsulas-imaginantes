# Estado de ejecución — CAPCOT externa 2026-10-26

**Estado:** `PAQUETE_PREPARADO_NO_RENDERIZADO_NO_PUBLICADO`. No hay MP4, voz, subtítulos temporizados ni QA oficial.

## Procedimiento leído

Se leyeron `docs/PLAN_MAESTRO_AUTOMATICO.md`, `docs/FLUJO_EXTERNO.md`, `docs/RECETA_CAPSULA.md`, `docs/GUIA_MODELO_EXTERNO.md`, `docs/SKILL_DRAFT_capsula_diaria.md`, `docs/ESTILOS_VISUALES.md`, `scripts/estilos.json`, `scripts/rotacion.py`, `scripts/cama_sonora.py`, `scripts/sfx_manifest.json`, `templates/storyboard_vertical.template.json`, `data/temas_del_dia.json`, `data/rotacion.json`, `data/publicaciones.json` y `data/cola.json`. El catálogo de skills instaladas de esta sesión devolvió una lista vacía; se usó la guía operativa versionada en el repositorio.

## Tema y fuentes

Tema: plataforma de hielo de la bahía de Baffin durante la última glaciación. El estudio original de *Nature Geoscience* se publicó el 21 de octubre de 2026 y el Research Briefing editorial relacionado se publicó el 26 de octubre de 2026. Los DOI son `10.1038/s41561-026-02126-7` y `10.1038/s41561-026-02127-6`. No coincide con los dos temas de `data/temas_del_dia.json` (hongo *Lanmaoa asiatica* y maduración del pimiento).

## Diferencias y conflicto de rotación

- Estilo seleccionado: `art_deco_poster`, según `scripts/estilos.json`; no aparece en las cápsulas de hoy consultadas.
- Música prevista: `circuito_neural`, cama válida en `scripts/cama_sonora.py` y `scripts/rotacion.py`, distinta de las camas registradas hoy (`arpegio`, `pizzicato`, `tambor`, `marimba`).
- La estructura permitida `pregunta` ya aparece en el storyboard del proyecto de ave jurásica programado como remake para hoy. Las otras cuatro estructuras permitidas también aparecen en storyboards fechados hoy. Por tanto, con el catálogo actual no existe una estructura permitida que pueda certificarse como única frente a todas las cápsulas actuales. Se conserva `pregunta` porque difiere de las dos cápsulas principales registradas en `data/rotacion.json`, pero esta coincidencia con el remake queda explícitamente pendiente de resolución por Grok Bot.
- `data/publicaciones.json` contiene seis `project_id` distintos con `fecha=2026-10-26`: `2026-10-26_pimiento-verde-rojo`, `2026-10-26_hongo-gente-diminuta`, `2026-10-26_papel-picado-dia-muertos`, `2026-10-26_catrina-posada-monerismo`, `2026-10-26_papel-picado-dia-muertos_parte2` y `2026-10-25_ave-jurasica-REMAKE`. `scripts/rotacion.py` establece `MAX_POR_DIA=3`. El pipeline oficial probablemente rechazará la cola por cupo excedido; no se modificaron manualmente los registros para ocultar este conflicto.

## Bloqueos técnicos

- `/workspace/capcot` no existe en este entorno; no se pudo ejecutar `scripts/procesar_cola.py`, `scripts/capsula_diaria.py`, `scripts/validar_storyboard.py --check-doi` ni `scripts/qa_capsula.py`.
- `edge_tts` no está instalado. Según `docs/GUIA_MODELO_EXTERNO.md`, no se debe sustituir `es-MX-JorgeNeural` por otra voz ni montar el video si esa voz no está disponible.
- Las nueve imágenes se generaron con ChatGPT ImageGen y se guardan únicamente en el paquete local. El proveedor oficial de imagen y sus credenciales no se pudieron comprobar.
- No se generaron música, efectos, voz, SRT temporizado ni MP4. `subtitulos_bloques.txt` es una segmentación textual de referencia, no una pista temporizada.
- El repositorio cita un documento de licencia de audio, pero `docs/AUDIO_LICENCIAS.md` no está presente en la rama consultada; la licencia formal de la cama sintetizada requiere revisión.

## Integridad y publicación

No se publicaron videos. No se modificaron `data/temas_del_dia.json`, `data/rotacion.json`, `data/publicaciones.json` ni `data/cola.json`. No se tocó motor U6. Solo se preparan evidencias textuales para GitHub; las imágenes permanecen fuera del repositorio. El QA oficial sigue **PENDIENTE**, no aprobado.
