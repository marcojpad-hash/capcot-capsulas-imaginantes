# Contrato operativo unificado CAPCOT
**Vigente desde 2026-10-31 · America/Mexico_City**

Este documento reconcilia el Plan Maestro, la Receta, la Guía para modelos externos, el Flujo Externo y las instrucciones de coordinación que aparecieron en una línea divergente. Es la referencia común para ChatGPT, Imaginantes (Grok Bot) y Grok app. No reemplaza los contratos técnicos de storyboard ni el contrato de estados.

## 1. Jerarquía documental
1. `docs/CONTRATO_OPERATIVO_UNIFICADO.md`: reparto de responsabilidades, autoridad, capacidad y handoff.
2. `docs/PLAN_MAESTRO_AUTOMATICO.md`: investigación, rotación, calidad editorial, restricciones y entregables de ChatGPT.
3. `docs/RECETA_CAPSULA.md` + `docs/GUIA_MODELO_EXTERNO.md`: esquema y requisitos del storyboard.
4. `docs/FLUJO_EXTERNO.md` + `docs/GROK_STATUS_CONTRACT.md`: transferencia, estados y evidencia.
5. `scripts/estilos.json`, plantillas y validadores: contratos ejecutables; el JSON canónico prevalece sobre vistas Markdown.
6. Brief semanal/parrilla: prioridades y slots solicitados; nunca pueden anular límites de seguridad, validación o capacidad del pipeline.

Un documento de coordinación, un prompt dirigido a un modelo o una parrilla no modifica por sí solo el código ni concede permisos de publicación.

## 2. Responsabilidades sin duplicación
| Actor | Responsable de | No debe hacer |
|---|---|---|
| **ChatGPT** | Radar e investigación; verificación y trazabilidad de fuentes; selección de candidatos recomendados; storyboard textual conforme a Receta/Guía; auditoría de rotación; documentación, validadores y reportes de evidencia. | No generar frames, imágenes, voz, audio o video; no renderizar, ejecutar QA audiovisual oficial, programar ni publicar; no editar `data/*.json`; no crear estados de Grok. |
| **Imaginantes (Grok Bot)** | Operación de producción: leer paquetes, decidir qué entra a producción dentro de las prioridades aprobadas, generar/organizar medios, montar, ejecutar QA oficial, administrar la programación/publicación autorizada y registrar estados y métricas. | No reescribir la investigación como si fuera evidencia; no publicar sin QA aprobado; no duplicar una publicación ejecutada por otro actor; no editar el contrato editorial unilateralmente. |
| **Grok app** | Apoyo de investigación, revisión, producción o resolución técnica cuando Imaginantes lo solicite; documentar qué realizó. | No mantener una segunda cola de publicación ni publicar en paralelo con Imaginantes. |
| **Mj** | Define objetivos, prioridades, autorizaciones personales y cambios de política/cupo. | Una parrilla no equivale a autorización para saltar validadores o forzar cupos. |
| **GitHub** | Fuente verificable de archivos, versiones, estados y commits. | La presencia de un archivo no prueba que un paso posterior haya ocurrido. |

La división se mantiene hasta que Mj cambie explícitamente el alcance de ChatGPT. Ningún agente debe asumir que “ayudar” autoriza a duplicar trabajo de otro.

## 3. Capacidad: cinco slots autorizados
La parrilla del 1–7 de noviembre plantea **5 slots diarios** (35 en la semana). **Mj autorizó explícitamente 5 publicaciones por día el 31-oct-2026** (orden de la parrilla de 7 días × 5 slots, "no dejar de publicar").

En consecuencia, en la rama `feature/capcot-video-discovery-continuity`:
- `scripts/rotacion.py`: `MAX_POR_DIA = 5`, `MAX_ORIGEN = {propia: 2, externa: 5}` (los paquetes de ChatGPT son externos y pueden llenar el día desde la cola).
- `scripts/procesar_cola.py`: procesa en orden todas las entradas de `--fecha` hasta llenar el cupo (consulta `rotacion.exigir_cupo` antes de cada una); sigue sin consumir colas de otras fechas, sigue validando DOI y solo saca de `entrada/` en corrida real.

Se mantienen separadas:
- **Slots editoriales:** 5 al día.
- **Capacidad implementada:** hasta 5 por día (máx. 2 propias; externas hasta 5).
- **Publicaciones efectivas:** solo las que Imaginantes registre con QA y evidencia de publicación. Habilitar el cupo **no** significa que los 5 slots estén publicados; cada slot requiere su evidencia.

`CAPCOT_FORZAR_CUPO=1` sigue prohibido como solución rutinaria. Pendiente de revisar: ventanas horarias (`VENTANAS` tiene 3 franjas) frente a 5 slots, y límites de plataformas.

## 4. Una sola ruta de trabajo
1. ChatGPT consulta el Plan Maestro y la memoria editorial disponible; distingue tema propuesto, paquete preparado, producción, QA y publicación.
2. ChatGPT entrega brief y storyboard textual en la rama de trabajo autorizada. Cada claim tiene fuente; lo pendiente se marca como pendiente, nunca se rellena por conjetura.
3. Imaginantes lee el paquete y registra `RECIBIDO_POR_GROK` solo después de leerlo. Después registra una decisión: `SELECCIONADO`, `DEVUELTO` o `RECHAZADO`.
4. Solo los seleccionados pasan a producción. Imaginantes genera medios, renderiza y ejecuta QA oficial.
5. Solo con `QA_APROBADO` y autorización de publicación correspondiente, Imaginantes programa/publica y registra URL/ID y fecha.
6. ChatGPT audita el estado y reporta discrepancias; no simula ni escribe estados que pertenecen a Imaginantes.

El contrato machine-readable es `docs/GROK_STATUS_CONTRACT.md`. La ausencia de `cola/estado/<project_id>.json` significa recepción no confirmada. Un storyboard o una carpeta en `proyectos/` no prueban publicación.

## 5. Paquetes y medios
Para el alcance vigente de ChatGPT, el paquete es textual: radar Markdown + storyboard JSON en la ruta definida por el Plan Maestro. Fuentes, DOI, estado de verificación y `source_ids` viajan dentro del storyboard. No se crean carpetas de frames ni `fuentes.md` separado por defecto. `approved_assets=[]`, `render_status=NOT_GENERATED` y sin rutas de medios antes de producción.

Los frames, audio, voz, video, render y archivos de producción pertenecen a Imaginantes. Si Mj cambia el alcance de ChatGPT, primero se actualizan Plan, Guía, Receta, Flujo, permisos y validación; un mensaje de coordinación no basta.

## 6. Reutilización de paquetes y prioridades
Los paquetes existentes pueden proponerse para reutilización, pero cada uno conserva su estado real. Reutilizar no significa recibido, seleccionado, renderizado, aprobado ni publicado. Antes de asignar un slot, Imaginantes verifica duplicados y estado; ChatGPT puede auditar la evidencia disponible y señalar conflictos. Un tema marcado `TBD` requiere investigación del día y no puede convertirse anticipadamente en un claim.

La parrilla semanal ordena prioridades, no cambia automáticamente el estado de los paquetes previos ni crea evidencia que no existe.

## 7. Restricciones y seguridad operativa
- No tocar `main`, no hacer merge ni cambiar de rama sin autorización explícita.
- No modificar `data/*.json` desde ChatGPT.
- No tocar Motor U6 ni motores canónicos.
- No publicar ni programar desde ChatGPT.
- No inventar recepción, QA, publicación, fuentes, DOI, cifras ni resultados.
- No subir secretos, tokens, claves ni archivos privados de credenciales.
- No declarar validación ejecutada si solo se hizo lectura estática.
- Los documentos heredados que contradigan este contrato se consideran legado hasta que se archiven o actualicen expresamente; no se usan como instrucciones activas.

## 8. Cambios necesarios para habilitar cinco publicaciones diarias
Antes de declarar operativa la parrilla completa, Imaginantes/ChatGPT deben preparar y probar, en rama de trabajo:
1. Política de cupos por día y por origen que soporte cinco sin duplicados.
2. Procesador que pueda recibir y procesar la cantidad aprobada, sin saltarse fechas ni consumir históricos por accidente.
3. Validadores y pruebas de regresión para los cinco slots y el reparto por origen.
4. Revisión de ventanas horarias, colisiones, rotación de tema/estructura/estilo/música y límites de plataformas.
5. Evidencia de QA y publicación por cada slot.

Actualización 31-oct-2026: puntos 1 y 2 implementados en rama (cupo 5, procesador multi-entrada); 3–5 siguen pendientes. Estado: **objetivo de cinco / capacidad de código cinco / publicación efectiva según evidencia**. Esta etiqueta debe acompañar cualquier reporte de operación.

## 2A. Descarga de carga de Grok Bot

El protocolo operativo detallado está en `docs/PROTOCOLO_DESCARGA_CARGA_GROK.md` y complementa este contrato. La división obligatoria es: ChatGPT entrega investigación verificada, guion final, storyboard completo, prompts por escena y metadata; Imaginantes/Grok Bot se concentra en recepción, generación audiovisual, montaje, render, QA, correcciones de producción y publicación autorizada. Bot no repite research ni reescribe guiones por rutina. Las devoluciones deben señalar el campo o escena exactos; ChatGPT resuelve faltantes de investigación y entrega parches. Las correcciones también consumen tokens, por lo que se limita el cambio al fragmento afectado. No rehacer escenas aprobadas ni paquetes completos salvo defecto demostrado.
