# Estado de ejecución — 2026-11-15_dato-dia-diapausa-lestes-sponsa

- **Fecha:** 15-nov-2026
- **Slot local propuesto:** 23:30, America/Mexico_City
- **Estado:** BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION
- **Medios:** NO_GENERADOS

## Comprobaciones

- Storyboard: 8 escenas, 183 palabras, 78 s de escenas + 6 s de cortinilla = 84 s.
- QA narrativo independiente: PASS/90; siete checks verdaderos y `critical_flags=[]` (15-nov-2026, 15:51 CDMX).
- Validador Python real: Amor ejecutó localmente `scripts/validar_storyboard.py cola/entrada/2026-11-15_dato-dia-diapausa-lestes-sponsa/storyboard.json --check-doi` el 15-nov-2026; resultado reportado: exit 0 y DOI resuelto.
- Los ocho `asset_filename` son rutas previstas; los archivos de frames no existen. La ejecución local reportada el 15-nov indicó exit 0, pero el validador vigente de esta rama rechaza `asset_filename` cuando `production_mode=storyboard_only` (regla en `scripts/validar_storyboard.py`). Por tanto, ese resultado histórico no demuestra conformidad con el contrato actual.
- No se generaron imágenes, frames, voz, audio, subtítulos temporizados, vídeo ni render.
- No se ejecutó `procesar_cola.py`, no se realizó QA audiovisual y no se publicó ni programó.

## Recepción

No existe `cola/estado/2026-11-15_dato-dia-diapausa-lestes-sponsa.json`, `handoffs/grok_inbox/2026-11-15_dato-dia-diapausa-lestes-sponsa.json` ni acuse individual de Grok. La carpeta preparada no demuestra recepción. El workflow automático `capcot-grok-dispatch.yml` solo escucha JSON de primer nivel en `cola/entrada/*.json`; esta entrega está en formato de carpeta anidada. El procesador `scripts/procesar_cola.py` sí contempla `cola/entrada/<id>/storyboard.json`, pero no se ejecutó en esta sesión.


## Auditoría CAPCOT — 2026-11-17

- QA narrativo persistido: PASS/90, siete checks verdaderos y `critical_flags=[]`.
- La validación estructural vigente falla: las ocho escenas declaran `asset_filename` en modo `storyboard_only`; no hay archivos de frames referenciados.
- Paquete conservado íntegro en `cola/bloqueados/2026-11-15_dato-dia-diapausa-lestes-sponsa/`. No existe estado Grok ni recepción confirmada. No se ejecutó validador ni workflow en esta auditoría.


## Corrección mecánica verificada — 2026-11-20

- Se retiraron los ocho campos `asset_filename` que apuntaban a `frames/scene_001.jpg`–`scene_008.jpg`, inexistentes en el repositorio.
- La corrección se aplicó y releyó tanto en `proyectos/2026-11-15_dato-dia-diapausa-lestes-sponsa/storyboard.json` como en esta copia bloqueada. Ambos blobs resultantes coinciden: `8a1d9fad63790bb4ba66504a14717c544f432a2c`.
- No se generaron ni subieron medios. `approved_assets=[]` y `export.render_status=NOT_GENERATED` permanecen sin cambios.
- La narración y el QA narrativo PASS/90 permanecen idénticos; no se repitió la lectura en frío.
- No se ejecutó el validador oficial en este run. El proyecto sigue bloqueado y no se promueve: la fecha objetivo 15-nov ya pasó y no hay autorización para publicación retroactiva.
