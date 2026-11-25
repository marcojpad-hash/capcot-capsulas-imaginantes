# Control de cola CAPCOT — 2026-11-25 00:03 CDMX

## Corte y ramas

- Rama de trabajo: feature/capcot-video-discovery-continuity, HEAD 1bce9a7a200073d0a4286d0d69f027b7ea45ea93.
- main, solo lectura: HEAD 7b50235a1a46b4d759796253e0d036fb147c4401.
- La rama de trabajo conserva 90 storyboards en 103 directorios de proyecto. No apareció storyboard del 25-nov desde el corte anterior. Hay una entrada heredada anidada, 2026-11-09_dato-robot-ensambla-orbita; no hay JSON plano en cola/entrada.
- main contiene 33 IDs de entrada anidada y cero JSON planos en cola/entrada. data/cola.json está vacío, aunque el árbol de cola no lo está. No hay elementos en cola/bloqueados en main.

## Profundidad y despacho

- scripts/registro_editorial.py recorre recursivamente storyboard.json, incluidos paquetes anidados.
- .github/workflows/capcot-grok-dispatch.yml solo observa cola/entrada/*.json. En workflow_dispatch usa find cola/entrada -maxdepth 1 y el selector acepta JSON planos. Las carpetas anidadas son auditables, pero NOT_DISPATCHABLE por esta ruta.
- No se disparó el workflow ni se envió payload. La entrada robot de feature y las 33 entradas anidadas de main no se promovieron.
- El trabajador scripts/trabajador_cola.py es un operador de Issues con etiquetas queue/blocked, no un escáner de carpetas. Su ejecución 45530346824 terminó SUCCESS y registró “sin trabajo en cola”; eso significa que no encontró Issues accionables, no que las 33 carpetas anidadas estén vacías.

## Paquete magnetismo en main

Proyecto y copia anidada: 2026-11-24_magnetismo-p-wave-eusi. El storyboard de proyecto y el de cola comparten el mismo contenido.

- Seis escenas y duración objetivo de 85 s; no cumple el mínimo de siete escenas.
- narrative_qa ausente; no existe revisión independiente registrada. Resultado de compuerta: FAIL/0, REVISION_INDEPENDIENTE_AUSENTE.
- approved_assets ausente y export.filename referencia capsula.mp4, pero el archivo no está en el árbol.
- ESTADO_EJECUCION.md no existe y cola/estado/2026-11-24_magnetismo-p-wave-eusi.json devuelve 404.
- Clasificación: NOT_DISPATCHABLE, RECEPCION_GROK_NO_CONFIRMADA, MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO. No se modificó porque está en main y no es un borrador apto.

## Publicación preexistente: Yo soy Sam

2026-11-24_yo-soy-sam ya tiene YouTube ID hY7UQAfRu-o, publicación TikTok 7711731601956146484 y publicación Facebook 122112456891518983. No hay storyboard en su carpeta de proyecto; sí hay registros de programación y publicación. Clasificación: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR.

## Nueve reworks ya programados en main

Los nueve tienen render.log y registro de programación; los nueve tienen YouTube ID y TikTok/Facebook en estado PROGRAMADO. Duraciones medidas registradas: 86.47–88.80 s. Sus metadatos indican 215–229 palabras, siete escenas y objetivo de 88 s. Los storyboards no tienen narrative_qa ni approved_assets; contienen asset_filename por escena y export.filename. Los MP4 referenciados no aparecen en el árbol Git. Para los nueve, cola/estado/<project_id>.json devuelve 404.

| Fecha | Hora CDMX | Clave | YouTube ID | Duración medida |
|---|---:|---|---|---:|
| 25-nov | 10:00 | nube | 9RxTSifAcpo | 86.80 s |
| 25-nov | 15:00 | barreleye | 3rwo_sK1e18 | 87.53 s |
| 26-nov | 10:00 | pan | 7pzPfqRSagU | 88.47 s |
| 26-nov | 15:00 | ratas | MgHVHbeIVS0 | 88.80 s |
| 27-nov | 10:00 | miel | p06UCGu0-Og | 86.47 s |
| 27-nov | 15:00 | mar | HKpani8TTeY | 87.17 s |
| 28-nov | 10:00 | arena | 6VUxaJtqbF0 | 86.70 s |
| 28-nov | 15:00 | juno | Dx3lqkAb8Sc | 87.40 s |
| 29-nov | 10:00 | viento | m1FeS0mhfZ4 | 88.77 s |

Clasificación para los nueve: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR, RECEPCION_GROK_NO_CONFIRMADA y MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO. No se intentó cancelar, duplicar ni redispatchar. La falta de narrative_qa impide tratarlos como PASS; bajo la regla vigente quedan FAIL/0 con REVISION_INDEPENDIENTE_AUSENTE.

## Horarios y colisiones

data/horarios.json fija ventanas 06:30–07:30 y 16:30–18:00, con 23:30 como slot fijo. La prueba de 13:00–14:30 ya no figura como ventana activa. Los nueve reworks de 10:00 y 15:00 están fuera de las ventanas vigentes; se conserva la programación existente sin cancelarla.

data/miniaturas_auditoria_2026-11-21.json registra colisiones de publishAt:
- 25-nov 07:00: cPNiOFeY5_k y W9g2tPZTpD4.
- 26-nov 17:00: JqlKsJOVmdE y -1DRh_qj7Bg.
- 27-nov 07:00: jiX6RdwJ1gg y nd0rs6iVy8E.
- 28-nov 17:00: gN6svdqe62Q y fcSNbU809ao.

historial_youtube.json devuelve 404. Por eso no se puede cerrar la revisión de riesgo de IDs antiguos fuera de los registros visibles. data/publicaciones.json contiene 62 registros, data/rotacion.json 39 y data/cola.json cero.

## CI y PR

- Semgrep run 45553710984: FAILURE, 37 findings, pero el log identifica los 37 como archivos mayores de 1 MB omitidos por el escáner; no aparecen coincidencias de reglas de código en ese run. El árbol Git muestra 36 blobs mayores de 1 MB; queda una diferencia de conteo por resolver.
- Gitleaks run 45553711043: SUCCESS.
- PR #15 sigue abierto, mergeable=false y sin CI verificable sobre su HEAD. No se fusionó.
- El worker de Issues no equivale al despacho Grok; no hay despacho manual registrado en este corte.

## Resultado del run

EJECUTADO: lectura de árboles de ambas ramas, revisión de los nueve reworks, magnetismo, publicación Yo soy Sam, horarios, colisiones, estados Grok individuales, workflow y logs de CI; revalidación de feeds y respaldo de Trends.

VERIFICADO: cero JSON planos de cola en ambas ramas; 33 paquetes anidados en main; nueve reworks ya programados; estados Grok 404 para magnetismo y los nueve reworks; ningún storyboard nuevo del 25-nov en feature.

NO EJECUTADO: no se crearon medios, storyboards, entradas de cola ni estados; no se modificaron data/*.json, main, permisos, secretos o workflows; no se enviaron payloads ni se cancelaron publicaciones.
