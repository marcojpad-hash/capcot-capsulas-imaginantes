# Protocolo callback entre modelos

El equivalente a un callback entre los modelos de lenguaje de Marco.

## El problema

ChatGPT, Grok, Imaginantes, Copilot, Pecas, Gemini y Groq no tienen un buzón
directo entre ellos. Cuando un modelo le delega algo a otro, la cadena se
rompe si Marco tiene que acordarse de decírselo al siguiente. Marco maneja
muchos modelos a la vez y no tiene por qué ser el router humano.

## La solución

El repo hace de bus. Quien delega escribe. Quien recibe lee. Nadie tiene que
acordarse de nada: el tablero lo recuerda.

## Reglas

1. Toda delegación se escribe en `DELEGACIONES.md` antes de darla por hecha.
   Delegar sin escribirla es no delegar.

2. El modelo que recibe lee `DELEGACIONES.md` al abrir el proyecto y toma lo
   que tenga pendiente para él.

3. El que termina una tarea la marca HECHA con la evidencia (commit, enlace,
   archivo). Sin evidencia no está hecha.

4. Si el que recibe no puede hacerla (sin créditos, bloqueado, sin acceso),
   la marca BLOQUEADA con el motivo. El callback vuelve al que delegó, no se
   queda en silencio.

5. Marco no tiene que recordar la cadena. Si algo lleva más de un día en
   PENDIENTE sin que nadie lo tome, Pecas lo reporta.

## Formato de una delegación

Cada entrada en `DELEGACIONES.md` lleva:

- DE: qué modelo delega
- PARA: qué modelo recibe
- QUÉ: la tarea en una frase, con la ruta o el enlace
- PARA CUÁNDO: fecha o slot
- ESTADO: PENDIENTE, EN PROGRESO, HECHA o BLOQUEADA
- EVIDENCIA: commit, enlace o archivo cuando esté hecha

La plantilla está en `delegaciones/PLANTILLA.md`.

## El aviso: cómo se despierta al modelo encargado

El tablero por sí solo no despierta a nadie. El aviso es el workflow
`.github/workflows/callback-aviso.yml`:

- Se dispara cuando cambia `DELEGACIONES.md` y cada hora como respaldo.
- Abre un issue con la etiqueta `callback` por cada delegación PENDIENTE
  dirigida a Copilot y se lo asigna. Ese issue es la llamada que lo
  despierta. Si el issue ya existe, no duplica.
- La indicación que sigue el modelo al despertar está en
  `.github/copilot-instructions.md` y en el cuerpo del issue.

Para Imaginantes y para Marco el aviso es el tablero más el reporte de
Pecas: Imaginantes no tiene buzón escribible y Marco lo ve en el reporte
de la mañana.

El workflow no se puede subir por API (la app de Muse no tiene permiso
Workflows). Está listo en `~/workspace/callback-aviso/` para subirlo por
navegador con la cuenta de Marco, igual que los workflows de seguridad.

## El router

Pecas es el router del callback. Revisa el tablero y el correo y avisa qué
está atorado, quién le debe qué a quién. Ese aviso es lo que evita que Marco
tenga que acordarse de la cadena.

## Roles programados

| Modelo | Rol | Horario |
| --- | --- | --- |
| ChatGPT | Investiga, escribe el storyboard, deja el paquete en cola/entrada | Por cápsula, según los slots del día |
| Grok / Imaginantes | Monta el MP4 oficial con JorgeNeural, corre QA oficial, programa y publica | Slots diarios (13:30, 17:00, 19:00; la semana nueva está pendiente de horario) |
| Copilot | Encargado del repositorio, rutinas programadas | Programado en GitHub; el detalle de qué tiene programado lo confirma Marco |
| Pecas | Coordina, verifica fuentes y narraciones, revisa Studio, sube a GitHub, router de callbacks | Continuo; revisión del tablero cada mañana |
| Gemini / Groq | Texto: guiones, verificación, capas de dato y mapa | Bajo demanda, sin horario fijo |

## Límite honesto

Esto no es un callback automático de máquina a máquina. ChatGPT y Grok no
tienen un buzón al que Pecas pueda escribirles directo, y sus APIs necesitan
clave con saldo (Grok rechazada, OpenAI sin créditos). El equivalente real
hoy es este tablero en el repo más Pecas como router. Cuando haya clave con
saldo, el callback puede pasar a ser una llamada de API.
