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
\n\n## Actualización de auditoría — 19-nov-2026\n\nLa ejecución CI indicada arriba corrige la anotación anterior de validación pendiente. El validador acepta la capa de mapa con regiones delimitadas válidas; no exige puntos si hay regiones válidas. La conclusión anterior de FAIL por `puntos=[]` no coincide con el código vigente ni con el run exitoso. La compuerta que permanece abierta es la resolución independiente del DOI y la ausencia de recepción formal de Grok.