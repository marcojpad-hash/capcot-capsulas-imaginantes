# Ajustes entre modelos — centro compartido de coordinación

Esta carpeta es el espacio común de indicaciones, comentarios y handoffs entre ChatGPT, Grok app e Imaginantes (Grok Bot).

## Lectura obligatoria al entrar
En cada sesión nueva y cada reanudación, antes de trabajar:
1. Leer este README.
2. Leer `COORDINACION_CHATGPT_IMAGINANTES.md`.
3. Leer `../docs/CONTRATO_OPERATIVO_UNIFICADO.md`.
4. Leer `BITACORA_COORDINACION.md` completa, especialmente las entradas más recientes.
5. Leer el documento de tarea asignada.

El mismo requisito está publicado en `../LEEME_MODELOS.md`. No asumir que otra instancia ya leyó los cambios.

## Documentos vigentes
| Archivo | Uso |
|---|---|
| `COORDINACION_CHATGPT_IMAGINANTES.md` | Punto de entrada de responsabilidades, reglas y capacidad actual |
| `BITACORA_COORDINACION.md` | Comentarios cronológicos entre instancias; append-only |
| `ACCESO_GROK.md` | Accesos y límites de conexión |
| `PARA_CHATGPT_semana_01-07nov.md` | Encargo semanal; subordinado al contrato común |
| `HANDOFF_GROK_PRODUCCION.md` | Handoff de producción; subordinado al contrato común |
| `CALIBRACION_ESTETICA_CHATGPT_GROK.md` | Criterios de continuidad visual, sin autoridad para cambiar roles |

## Cómo comentar
Al completar una tarea que cambie coordinación, prioridades, pipeline, alcance o archivos compartidos, agrega una entrada al final de `BITACORA_COORDINACION.md` con:
- Fecha y hora CDMX.
- Instancia/modelo.
- Objetivo y documentos consultados.
- Hallazgo o decisión.
- Archivos modificados y commit.
- Pendientes, responsable y siguiente acción.

No editar ni borrar entradas previas. Si hay desacuerdo, cada instancia registra su evidencia y propone resolución; no modifica silenciosamente la instrucción de la otra.

## Precedencia
La bitácora comunica; no legisla. En caso de contradicción manda `../docs/CONTRATO_OPERATIVO_UNIFICADO.md`, después el Plan Maestro y los contratos técnicos específicos. La parrilla semanal no cambia límites del código. No tocar `main`, Motor U6 ni `data/*.json` desde ChatGPT; no publicar desde ChatGPT.

## Estado de capacidad conocido
El contrato y el código de la rama feature establecen hasta cinco cápsulas por fecha (máximo dos propias y cinco externas, con tope global de cinco). `procesar_cola.py` recorre las entradas de la fecha hasta llenar el cupo. La programación dispone de cinco ventanas horarias; esto acredita capacidad de asignación, no cinco publicaciones efectivas. Las publicaciones solo se cuentan con QA y evidencia de plataforma. La suite de regresión de cupo/procesador debe pasar antes de declarar el flujo plenamente validado.

## Prioridad operativa: descargar trabajo de Grok Bot
El documento `../docs/PROTOCOLO_DESCARGA_CARGA_GROK.md` define el reparto de preproducción y producción. ChatGPT entrega investigación, fuentes, guion, storyboard, prompts y metadata listos; Bot se concentra en generación audiovisual, montaje, render, QA y publicación autorizada. Bot no repite investigación ni reescribe por rutina. Las correcciones son puntuales y también consumen tokens; los faltantes de evidencia regresan a ChatGPT.
