# Estado de ejecución — 2026-11-18_dato-kuroshio-puente-atmosferico

- Fecha de actualización: 2026-11-18
- Rama: `feature/capcot-video-discovery-continuity`
- Etapa: PREPRODUCCIÓN TEXTUAL
- Estado: `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`
- Medios: `NO_GENERADOS`
- Render: `NOT_GENERATED`
- Assets aprobados: ninguno
- Publicación/programación: no autorizada; pendiente de decisión de Grok.

## Archivos presentes
- `storyboard.json`
- `fuentes.md`

## Comprobaciones registradas
- Lectura en frío de narración: PASS, 90/100; siete checks verdaderos y sin banderas críticas.
- Estructura narrativa: 8 escenas, 222 palabras de narración, 84 segundos incluyendo cortinilla.
- Comprobación estructural equivalente en JavaScript contra el contrato visible del validador: 0 errores y 0 avisos.
- Fuente primaria: artículo de Nature Geoscience publicado el 17-11-2026. DOI visible tanto en la página editorial como en el PDF oficial: `10.1038/s41561-026-02139-2`.
- El resolvedor independiente Crossref/doi.org no se confirmó en esta ejecución; no se declara verificado por ese mecanismo.
- Regiones del mapa tomadas de las cajas de análisis publicadas en la figura 1; representadas como regiones delimitadas, no como pines ni trayectorias.

## Pendiente bloqueante
- CI posterior ya ejecutó la validación estructural: workflow run `44417215473` (`CAPCOT — validar preproducción Kuroshio`), commit `f78ab7bc9d312e4b4b87903099707b6e2b0685d1`, 2026-11-18 17:02:47–17:03:06 UTC. Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`. Resultado: `OK`, salida 0.
- El comando no incluyó `--check-doi`; Crossref no fue verificado en esa ejecución. El DOI `10.1038/s41561-026-02139-2` permanece `PENDIENTE_RESOLVEDOR`.
- No existe `cola/estado/2026-11-18_dato-kuroshio-puente-atmosferico.json`: `RECEPCION_GROK_NO_CONFIRMADA`.
- No copiar a `cola/entrada` ni emitir handoff mientras el DOI siga pendiente.

## Alcance
Este expediente es solo preproducción textual. No se han generado imágenes, audio, video ni publicaciones.


## Actualización de auditoría — 19-nov-2026

La ejecución CI indicada arriba corrige la anotación anterior de validación pendiente. El validador acepta la capa de mapa con regiones delimitadas válidas; no exige puntos si hay regiones válidas. La conclusión anterior de FAIL por `puntos=[]` no coincide con el código vigente ni con el run exitoso. La compuerta que permanece abierta es la resolución independiente del DOI y la ausencia de recepción formal de Grok.

## Actualización de auditoría — 20-nov-2026

Se releyeron las ejecuciones posteriores que no estaban reflejadas en la nota anterior:

- **Run #3:** `44617395667`; commit `369d0da1007f6b2eafd3502bd369c4284d3acee1`; creado `2026-11-19T21:18:16Z`; comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`; paso **Validar storyboard textual**: `OK`, salida 0.
- **Run #4 (más reciente):** `44617431497`; commit `b399dda95661b2e134a24c99d9ede803f597f1bb`; creado `2026-11-19T21:18:28Z`; mismo comando exacto; paso **Validar storyboard textual**: `OK`, salida 0. El paso de expediente también terminó con `Expediente textual íntegro; medios no generados; publicación no autorizada.`.

Ninguno de los dos comandos incluyó `--check-doi`. Estos runs confirman la validación estructural del storyboard en esos commits; no confirman Crossref/resolvedor ni levantan el bloqueo DOI. El DOI `10.1038/s41561-026-02139-2` permanece `PENDIENTE_RESOLVEDOR`. El estado permanece `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; no se copia a cola ni se emite handoff.


## Actualización de auditoría — 20-nov-2026 (run #5)

- Workflow: `CAPCOT — validar preproducción Kuroshio`.
- Run: `44824370570`; creado `2026-11-20T21:54:11Z`; resultado `success`.
- Commit ejecutado: `6b764c5328f1b2ac9641e8959c487b41927eb180`.
- Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Log del paso **Validar storyboard textual**: `OK`, salida 0.
- Log del paso de expediente: `Expediente textual íntegro; medios no generados; publicación no autorizada.`
- El comando no incluyó `--check-doi`. El DOI `10.1038/s41561-026-02139-2` permanece `PENDIENTE_RESOLVEDOR`.
- Comparación de blobs entre el commit ejecutado y la rama actual: storyboard `2046152ade90fffaf9527d180e13cc5f6009fb60`, validador `28e3d600431b92d7bd0eca94f34d4ff5867c9cbf`, workflow `e8151c8eb1ee5a0893f3f800f4c625887427ecde`; los tres permanecen idénticos, por lo que el resultado estructural sigue aplicando al contenido vigente.
- No existe `cola/estado/2026-11-18_dato-kuroshio-puente-atmosferico.json`: `RECEPCION_GROK_NO_CONFIRMADA`.
- Estado sin cambio: `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. No se copia a cola ni se emite handoff.


## Actualización de auditoría — 20-nov-2026 (run #6)

- Workflow: `CAPCOT — validar preproducción Kuroshio`; run `44828326509`, job `136606531020`, resultado `success`, creado `2026-11-20T22:21:50Z`.
- Commit ejecutado: `4afd38844d615aeb18f68a9c7d61c21182ac9a91`.
- Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Log del paso **Validar storyboard textual**: `OK`, salida 0. El paso de expediente terminó con `Expediente textual íntegro; medios no generados; publicación no autorizada.`.
- El comando no incluyó `--check-doi`. El DOI `10.1038/s41561-026-02139-2` sigue `PENDIENTE_RESOLVEDOR`; el run confirma estructura, no Crossref.
- En el corte del run #6, los blobs del storyboard y del validador coincidían con la rama entonces vigente. El run posterior se documenta abajo; el validador actual cambió respecto del ejecutado en ese run, por lo que no se afirma validación con el hash actual. No se promueve ni se copia a cola.


## Actualización de auditoría — 21-nov-2026 (run posterior, revisión de obsolescencia)

- Workflow: `CAPCOT — validar preproducción Kuroshio`; run `44832382024`, job `136620265585`, resultado `success`.
- Commit ejecutado: `30d0d5840a21388d8b45978c9ea4bab4fbda7bb9`; log de checkout: `HEAD is now at 30d0d58 Record latest Kuroshio structural CI run without DOI validation`.
- Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Paso **Validar storyboard textual**: `OK`, salida 0. Paso de expediente: `Expediente textual íntegro; medios no generados; publicación no autorizada.`
- El comando no incluyó `--check-doi`; el DOI `10.1038/s41561-026-02139-2` permanece `PENDIENTE_RESOLVEDOR`.
- Comparación de blobs: storyboard del commit y actual = `2046152ade90fffaf9527d180e13cc5f6009fb60`; workflow = `e8151c8eb1ee5a0893f3f800f4c625887427ecde`; validador del run = `28e3d600431b92d7bd0eca94f34d4ff5867c9cbf`; validador actual = `50335bb620ea5b0fad395af71c0f0c764cf9b067`.
- El validador actual cambió: encapsula la validación de puntos y añade coordenadas ecuatoriales RA/Dec. El mapa de este storyboard usa regiones terrestres delimitadas (35–45°N; 140–170°E y 35–45°N; 50–80°W), no puntos celestes; el cambio observado no parece afectar este caso, pero no existe una ejecución CI con el hash actual del validador.
- Estado conservado: `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. La validación del run posterior acredita la versión anterior del validador; no acredita Crossref ni elimina el bloqueo DOI. No se copia a cola ni se emite handoff.


## Actualización de auditoría — 22-nov-2026 (run #11; supersede la nota de obsolescencia del 21-nov)

- Workflow: `CAPCOT — validar preproducción Kuroshio`; run `44951621909`, job `136990599397`, resultado `success`, creado `2026-11-21T21:27:24Z`.
- Commit ejecutado: `ed8659ec7184d51cdd84d3575a5ac57c1595ce2c`.
- Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Paso **Validar storyboard textual**: `OK`, salida 0. Paso de expediente: `Expediente textual íntegro; medios no generados; publicación no autorizada.`.
- Comparación de blobs entre el commit del run y la rama actual al corte de esta actualización: storyboard `2046152ade90fffaf9527d180e13cc5f6009fb60`, validador `50335bb620ea5b0fad395af71c0f0c764cf9b067`, workflow `e8151c8eb1ee5a0893f3f800f4c625887427ecde`; los tres coinciden. Por tanto, el run sí acredita la validación estructural del storyboard con el validador vigente.
- El comando **no** incluyó `--check-doi`; no acredita Crossref. El DOI `10.1038/s41561-026-02139-2` permanece `PENDIENTE_RESOLVEDOR` y bloquea la promoción.
- `cola/estado/2026-11-18_dato-kuroshio-puente-atmosferico.json` sigue sin existir: `RECEPCION_GROK_NO_CONFIRMADA`.
- Estado conservado: `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. No copiar a cola ni emitir handoff.


## Reejecución CI posterior observada — run #45075532329

- Fecha de ejecución: `2026-11-22T22:03:34Z`.
- Commit validado: `25e1ecfc96faf9a40f86a9feb0e30af90d9d608b`.
- Job: `137371796752`.
- Comando estructural exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Resultado literal: `OK`.
- Comprobación adicional del mismo job: `approved_assets=[]`, `export.render_status=NOT_GENERATED`; salida literal: `Expediente textual íntegro; medios no generados; publicación no autorizada.`
- El run **no ejecutó `--check-doi`**. Por tanto, no acredita Crossref ni resolución DOI; el bloqueo DOI permanece.
- Es una reejecución del mismo commit/archivos ya validados en el run #44951621909; no cambia el estado editorial ni autoriza promoción.



## Revalidación CI — 24-nov-2026 (run #45477532530)

- Workflow: `CAPCOT — validar preproducción Kuroshio`; run `45477532530`, job `138741609287`, resultado `success`.
- Inicio: `2026-11-24T20:07:58Z`; finalización: `2026-11-24T20:08:16Z` (14:07:58–14:08:16 CDMX).
- Rama: `feature/capcot-video-discovery-continuity`.
- Commit ejecutado: `08d5cc016d69c59b5ad1f0aae0b2e3dbb50e14c3`.
- Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Resultado literal del validador: `OK`, salida 0. El paso adicional comprobó `production_mode=storyboard_only`, `approved_assets=[]` y `export.render_status=NOT_GENERATED`; salida literal: `Expediente textual íntegro; medios no generados; publicación no autorizada.`.
- El comando no incluyó `--check-doi`; no acredita Crossref. El DOI `10.1038/s41561-026-02139-2` permanece `PENDIENTE_RESOLVEDOR`.
- Comparación de blobs entre el commit ejecutado y la rama vigente: storyboard y `scripts/validar_storyboard.py` idénticos; `.github/workflows/validar-kuroshio.yml` idéntico. La validación aplica al contenido actual de este expediente.
- El log no ejecutó `tests/test_validar_storyboard_textual.py`; no se declara suite de pruebas ejecutada.
- `cola/estado/2026-11-18_dato-kuroshio-puente-atmosferico.json` sigue ausente: `RECEPCION_GROK_NO_CONFIRMADA`.
- Estado conservado: `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. No copiar a cola ni emitir handoff mientras el DOI siga pendiente.


## Revalidación CI posterior — 24-nov-2026 (run #45500710272)

- Workflow: `CAPCOT — validar preproducción Kuroshio`.
- Run: `45500710272`; job: `138822927244`; resultado: `success`.
- Inicio: `2026-11-24T22:24:55Z`; finalización: `2026-11-24T22:25:06Z` (16:24:55–16:25:06 CDMX).
- Rama y commit ejecutados: `feature/capcot-video-discovery-continuity`, `ba92e02ac0076041a32ca809f91cc3e2d4cb89bf` (HEAD vigente al corte).
- Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Resultado literal del validador: `OK`, salida 0. No se usó `--structural-only`.
- El paso adicional comprobó `production_mode=storyboard_only`, `approved_assets=[]` y `export.render_status=NOT_GENERATED`; resultado literal: `Expediente textual íntegro; medios no generados; publicación no autorizada.`
- El comando **no** incluyó `--check-doi`. El DOI `10.1038/s41561-026-02139-2` permanece `PENDIENTE_RESOLVEDOR`; Crossref no está acreditado y continúa bloqueando la promoción.
- El run no ejecutó la suite `tests/test_validar_storyboard.py`.
- `cola/estado/2026-11-18_dato-kuroshio-puente-atmosferico.json` sigue ausente: `RECEPCION_GROK_NO_CONFIRMADA`.
- Estado conservado: `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. No copiar a cola ni emitir handoff.

## Revalidación CI posterior — 2026-11-24

- Run más reciente localizado para este storyboard: [45502897065](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45502897065).
- Commit ejecutado: `82db8f2aa2d6c58bb80a93b82a804fcc4df453c9` (`docs: registrar CI Kuroshio #45500710272 y bloqueo DOI`).
- Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Resultado del validador: `OK`; el chequeo posterior confirmó `approved_assets=[]` y `export.render_status=NOT_GENERATED`.
- Comparación de blobs entre el commit del run y el HEAD actual de feature: storyboard `2046152d4cf918f6a3a3908c9a050a92f47c77a0` y validador `50335d4b0d4d7b85f36d0ad2d1c13ed11a87c0df` sin cambios. La validación estructural sigue aplicando al contenido actual.
- El comando **no** incluyó `--check-doi`; no acredita consulta Crossref ni verificación DOI. DOI permanece `PENDIENTE_RESOLVEDOR`.
- Este run sustituye a `45500710272` como última ejecución CI documentada. No cambia narrativa, claims ni decisión editorial. Kuroshio permanece fuera de cola y no apto para promoción hasta completar DOI.
