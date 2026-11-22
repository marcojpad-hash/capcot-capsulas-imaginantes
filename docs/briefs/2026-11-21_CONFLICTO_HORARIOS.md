# Conflicto entre política de horarios y plan semanal — 2026-11-21

## Fuentes leídas (solo lectura)

- `main/data/horarios.json`, blob `7baae556de18e0ddfadfd750568e4247a136d8fa`, actualizado 2026-11-16: define dos ventanas vigentes, 06:30–07:30 y 13:00–14:30. No declara una ventana de 16:30–18:00 ni una de 17:00.
- `feature/capcot-video-discovery-continuity/data/horarios.json`, blob `550599906c26e747de71b6b962080b6bd469f23f`, actualizado 2026-11-09: conserva la ventana 16:30–18:00; está desactualizado frente a main.
- `main/docs/briefs/produccion_2026-11-23_28/plan_semana.json`, blob `ed4467d1dc91a176de8da0c681ed3cf3467ae0bd`: programa 17:00 el 24, 26 y 28-nov; el plan semanal también anota 22-nov 17:00 (Ada).
- `main/docs/briefs/2026-11-21_PRODUCCION_SEMANA_23-28nov.md`: resume el mismo plan y el estado de programación.

## Conflicto

El plan de producción de main utiliza 17:00, pero el JSON de política vigente de main no contiene una ventana que autorice esa hora. La rama feature sí conserva 16:30–18:00, pero su snapshot es del 09-nov y no puede prevalecer sobre main.

No se puede resolver copiando el horario antiguo de feature ni editando los JSON protegidos. La autoridad documental está dividida entre la política de main y un plan semanal más reciente.

## Impacto en borradores 21–23 nov

- 21-nov 07:00, Homo erectus: narrative QA FAIL 83.
- 21-nov 17:00, púlsar gamma: narrative QA FAIL 83 y ventana ausente en la política JSON de main.
- 21-nov 23:30, Fentale: narrative QA PASS 90; la fuente primaria corresponde al 19-nov, no a una noticia del mismo día. No se considera apto para el slot de dato del día.
- 22-nov 07:00, Voyager 1: QA FAIL 83; main tiene Salem en ese slot.
- 22-nov 13:30, fusión estelar: QA FAIL 84; main tiene Gutenberg en ese slot.
- 22-nov 17:00, Yubarta: QA PASS 90, pero main tiene Ada en ese slot y la política JSON no declara la ventana.
- 23-nov 13:30, biodiversidad tropical: QA FAIL 82, una fuente suplementaria continúa `PENDING_SOURCE`, el lunes no es día preferente para mediodía y no hay autorización de slot que venza esos bloqueos.

Los siete archivos `cola/estado/<project_id>.json` consultados para estos proyectos devolvieron 404: `RECEPCION_GROK_NO_CONFIRMADA`. No hay evidencia de recepción Grok. No se promovió ni se redispatchó ningún borrador.

## Acción segura

- Mantener `data/*.json` intactos.
- Mantener los borradores en `proyectos/`; ningún FAIL entra a `cola/entrada/`.
- No modificar el plan de producción, la política de horarios ni las publicaciones.
- La decisión mínima pendiente es que el responsable editorial reconcilie si 17:00 es una ventana vigente y, de ser así, actualice la política en la fuente autorizada. Hasta entonces, no usar 17:00 para abrir nuevos slots.

## Verificación

El inventario de storyboards y los archivos de estado se releen desde GitHub. Este documento no declara recepción, producción, QA audiovisual ni publicación. No se dispararon workflows, no se enviaron webhooks y no se generaron medios.
