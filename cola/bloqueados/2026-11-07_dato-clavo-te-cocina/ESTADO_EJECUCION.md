# Estado de ejecución — Dato del día 7 nov 2026

- **project_id:** `2026-11-07_dato-clavo-te-cocina`
- **Serie:** Datos y ociosidades
- **Fecha objetivo:** 2026-11-07
- **Slot:** 23:30 America/Mexico_City
- **Estado:** `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`
- **QA narrativo independiente (2026-11-20):** FAIL, 82/100; `limite_evidencia_explicito=false`; flag `CIFRAS_SIN_UNIDAD_Y_CONDICIONES_DE_ENSAYO_INSUFICIENTES`.
- **Ubicación archivada:** `cola/bloqueados/2026-11-07_dato-clavo-te-cocina/`.
- **Recepción Grok:** `RECEPCION_GROK_NO_CONFIRMADA`.
- **Preproducción textual:** COMPLETADA
- **Fuente primaria:** VERIFICADA
- **Medios:** `NO_GENERADOS`
- **Medios:** `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` — no se encontró `salidas/2026-11-07_dato-clavo-te-cocina/` en los árboles `feature` ni `main`; el registro de plataforma sí contiene IDs de publicación.
- **Publicación/programación:** `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` — YouTube y TikTok figuran publicados en los registros del 9-nov; Facebook figura programado, sin confirmación posterior.

## Archivos del paquete

- `storyboard.json`: storyboard textual de 8 escenas, formato 9:16.
- `fuentes.md`: fuente primaria, DOI, afirmaciones respaldadas y límites.

## Notas para revisión Grok

1. Revisar el guion y el cumplimiento del arco narrativo antes de generar medios.
2. La primera escena es la portada: caja amarilla/crema, subrayado rojo y sin subtítulo superior.
3. Mantener el matiz: té de clavo experimental como posible complemento; nunca presentarlo como desinfectante doméstico probado ni reemplazo de la limpieza rutinaria.
4. Voz prevista: `es-MX-JorgeNeural`, rate `+7%`, pausas continuas, pad 0.3 s.
5. No publicar ni programar sin QA y decisión de Grok.

## Ejecución

Paquete textual preparado por ChatGPT en la rama de trabajo CAPCOT. La recepción por Grok y el montaje/publicación quedan pendientes de confirmación externa.

## Auditoría operativa 2026-11-20

- **QA narrativo independiente:** FAIL 82/100; siete checks: seis true, `limite_evidencia_explicito=false`; flag `CIFRAS_SIN_UNIDAD_Y_CONDICIONES_DE_ENSAYO_INSUFICIENTES`. La narración no contextualiza la base/unidad de los porcentajes MIC/MBC ni las condiciones asociadas a esas medias.
- **Handoff:** `RECEPCION_GROK_NO_CONFIRMADA`; `cola/estado/2026-11-07_dato-clavo-te-cocina.json` devuelve 404. La publicación histórica no sustituye el acuse de recepción.
- **Evidencia de procesamiento previo:** `data/horario_2026-11-08.json` registra el slot 23:30, YouTube ID `EwZ3dHalUn0` y TikTok post ID `7705655549571894529`; `data/horario_2026-11-09.json` los clasifica publicados y registra YouTube a `2026-11-09T05:30:22Z` (23:30 CDMX del 8-nov). Facebook figura programado para el 8-nov 23:30, sin URL ni confirmación final en el registro consultado.
- `data/publicaciones.json` no contiene entrada para este project_id ni para el YouTube ID. No se modificó ningún `data/*.json`.
- Clasificación final: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. No reprogramar ni redispatchar. El campo `publicacion.status=PENDIENTE_DECISION_GROK` del storyboard queda como valor histórico de preproducción; esta bitácora registra la evidencia posterior sin reescribir el storyboard editorial.
