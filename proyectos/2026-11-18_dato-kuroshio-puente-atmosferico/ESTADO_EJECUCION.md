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
- En el corte del run #6, los blobs del storyboard y del validador coincidían con la rama entonces vigente. El run posterior posterior se documenta abajo; el validador actual cambió respecto del ejecutado en ese run, por lo que no se afirma validación con el hash actual. No se promueve ni se copia a cola.


## Actualización de auditoría — 21-nov-2026 (run posterior, revisión de obsolescencia)

- Workflow: `CAPCOT — validar preproducción Kuroshio`; run `44832382024`, job `136620265585`, resultado `success`.
- Commit ejecutado: `30d0d5840a21388d8b45978c9ea4bab4fbda7bb9`; log de checkout: `HEAD is now at 30d0d58 Record latest Kuroshio structural CI run without DOI validation`.
- Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Paso **Validar storyboard textual**: `OK`, salida 0. Paso de expediente: `Expediente textual íntegro; medios no generados; publicación no autorizada.`
- El comando no incluyó `--check-doi`; el DOI `10.1038/s41561-026-02139-2` permanece `PENDIENTE_RESOLVEDOR`.
- Comparación de blobs: storyboard del commit y actual = `2046152ade90fffaf9527d180e13cc5f6009fb60`; workflow = `e8151c8eb1ee5a0893f3f800f4c625887427ecde`; validador del run = `28e3d600431b92d7bd0eca94f34d4ff5867c9cbf`; validador actual = `50335bb620ea5b0fad395af71c0f0c764cf9b067`.
- El validador actual cambió: encapsula la validación de puntos y añade coordenadas ecuatoriales RA/Dec. El mapa de este storyboard usa regiones terrestres delimitadas (35–45°N; 140–170°E y 35–45°N; 50–80°W), no puntos celestes; el cambio observado no parece afectar este caso, pero no existe una ejecución CI con el hash actual del validador.
- Estado conservado: `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. La validación del run posterior acredita la versión anterior del validador; no acredita Crossref ni elimina el bloqueo DOI. No se copia a cola ni se emite handoff.
