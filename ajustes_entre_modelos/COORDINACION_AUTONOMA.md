# Coordinación autónoma de modelos — el arreglo

Fecha: 2026-11-15. Autora: Amor, por orden directa de Marco ("solúcioname esa madre").
Problema: ChatGPT y Grok no hacen el trabajo cuando se les asigna por el bus (repo)
o por chat; solo se mueven cuando un humano (Marco) va y les dice que trabajen.
Mientras tanto todo el trabajo cae sobre los créditos de Muse, y Marco ya gastó
sus tokens de Muse como inversión para una operación GRATUITA. Esto lo arregla.

## 1. Por qué no se movían (causa raíz, verificada)

ChatGPT (chat) y Grok (web) son puntos conversacionales: solo actúan cuando alguien
les habla. El bus (archivos en el repo) es un buzón que ningún modelo abre por su
cuenta. No hay un "ellos revisan el repo solos" gratis. Lo verificado:

- **ChatGPT Tasks (tareas programadas).** En Plan Go: 3 tareas activas, como mucho
  1 vez al día. Una tarea corre un prompt guardado en horario fijo, puede buscar
  en la web y leer apps conectadas (GitHub), y avisa con el resultado. Pero NO es
  un trabajador: corre un prompt y notifica; los cambios de datos por apps
  conectadas pueden pausar pidiendo aprobación. Sirve de despertador, no de motor.
  Fuentes: ayuda de OpenAI vía lilachbullock.com/chatgpt-tasks,
  consultevo.com/how-to-use-chatgpt-tasks, zapier.com/blog/chatgpt-scheduled-tasks.
- **Codex en GitHub (@codex / Agent HQ).** Asignar un Issue a Codex y que abra un
  PR solo funciona en los planes de pago de Copilot (Agent HQ, preview feb-2026).
  La integración de Codex en GitHub (revisión automática, @codex en PRs) está
  listada bajo el plan Plus. En Plan Go el acceso a Codex cloud NO está
  confirmado en la documentación (unas fuentes dicen que Codex viene incluido
  en Free/Go, otras que la nube empieza en Plus). NO se asume: se prueba en la
  cuenta (paso de verificación abajo).
  Fuentes: docs.github.com (Kick off a task with Copilot agents: "enabled by
  default for all paid Copilot plans", "Third-party coding agents are available
  for all paid Copilot plans"), developertoolkit.ai (Codex GitHub integration),
  agentbuildershq.com (Codex Cloud).
- **Copilot coding agent.** Solo planes de pago. El plan Free lo marca "Not
  included" para el agente en la nube (asignar un Issue y que abra un PR).
  Pro cuesta $10/mes. Queda FUERA por la regla de nada con dinero.
  Fuentes: docs.github.com (misma página), sharkly.ai, kipt.me, agentkoji.com.
- **Grok.** La API NO tiene nivel gratuito permanente: es pago por uso
  (grok-4.7 $2/$6 por millón de tokens). El programa de $150/mes por compartir
  datos ya no está documentado (terminó ~may-2025). El crédito promocional de
  $25 no aparece en la documentación actual. Grok gratis solo existe en
  grok.com / X web (~10 preguntas cada 2 h), no programático. Los "Grok API
  gratis" de GitHub manejan la web con una sesión logueada: frágiles, se rompen
  cuando cambia la web, y la sesión pasa por código de terceros.
  Fuentes: docs.x.ai vía toolfreebie.com/grok-api-free-credits,
  intelsi.si/guides/is-xai-api-free, layer3labs.io. Además, en este proyecto
  ya está verificado: la API de Grok devuelve HTTP 400 (clave rechazada) y
  grok.com bloquea el navegador en la nube con Cloudflare.
- **Lo que SÍ es gratis y funciona solo:**
  - GitHub Actions: gratis e ilimitado en repositorios públicos con runners
    estándar (documentación de facturación de GitHub: "GitHub Actions usage is
    free for self-hosted runners and for public repositories that use standard
    GitHub-hosted runners"). CAPCOT y motor-u6-storage son públicos. El
    orquestador ya corre ahí con Groq y en verde desde 2026-11-10.
  - Groq (nivel gratuito): gpt-oss-120b, 30 peticiones/min, 1,000/día,
    8,000 tokens/min, 200,000 tokens/día. Ya conectado y funcionando en la VM
    y en Actions (secreto GROQ_API_KEY del repo).
  - Gemini (nivel gratuito): modelos Flash con entrada y salida gratis, sin
    tarjeta; límites exactos por proyecto en AI Studio. Ya conectado y
    funcionando en la VM.
- **Patrón open source que se copia (no las herramientas):** WoterClip
  (Issues como plano de control + heartbeat), OS-APOW (Issues como máquina de
  estados con etiquetas + centinela que sondea), Overdeck (plano de control
  de Issues a PR). El patrón es: **Issues + etiquetas como cola con estados,
  y un trabajador que sondea**. Lo implementamos con lo que ya existe y es
  gratis (Actions + Groq/Gemini + el repo), no con Claude ni con claves de pago.

## 2. El mecanismo — Trabajador de cola

### 2.1 La cola son los Issues

Un Issue = una unidad de trabajo, con contrato. Etiquetas (máquina de estados):

- `cola` — esperando trabajador.
- `en-progreso` — el trabajador lo tomó.
- `hecho` — entregado, con enlace al PR/commit de evidencia.
- `bloqueado` — no se pudo, con el motivo exacto y qué lo desbloquea.

Plantillas en `.github/ISSUE_TEMPLATE/` (trabajo-capsula, trabajo-motor,
trabajo-auditoria). Cada Issue lleva: `tipo:` (validar | texto | motor),
`ruta:` (dónde va el artefacto), `tarea:` (qué hay que hacer, con fuentes
reales), criterio de aceptación y evidencia. Sin Issue no hay trabajo: lo que
no está en un Issue es invisible y no se hace.

### 2.2 El trabajador corre solo en GitHub Actions

Workflow `trabajador-cola.yml` (copia de staging en
`ajustes_entre_modelos/workflow-trabajador-cola.yml`; instalar en
`.github/workflows/` — no se puede subir por API, ver §4):

- Disparadores: cada 2 horas (`0 */2 * * *`), al etiquetar un Issue con
  `cola`, y manual (`workflow_dispatch`).
- Corre `scripts/trabajador_cola.py`, que:
  1. Crea las etiquetas si faltan.
  2. Toma el Issue con `cola` más viejo (máximo 5 por corrida).
  3. Lo marca `en-progreso` y comenta que lo tomó.
  4. Ejecuta según `tipo:`:
     - `validar`: corre los validadores del repo sobre `ruta:`
       (`validar_storyboard.py --check-doi`, `qa_capsula.py`, verificador del
       motor). Sin LLM.
     - `texto`: llama a Groq (gpt-oss-120b; Gemini si existe el secreto
       `GEMINI_API_KEY`) con la tarea del Issue, escribe el artefacto en
       `ruta:`, lo valida con el validador que corresponda ANTES de abrir el
       PR, y abre el PR desde la rama `trabajador/<n>`.
     - `motor`: corre `correr_estandar.py` sobre la entrada de `ruta:` y
       verifica con el verificador que corresponda.
  5. Abre el PR con la evidencia y marca el Issue `hecho` (con enlace al PR)
     o `bloqueado` (con el motivo exacto y qué lo desbloquea).
  6. Nunca toca `main` directo, nunca fusiona, nunca borra nada.
- Verificación por PR/commit, nunca por acuse. El PR no se abre si el
  validador no pasa.

### 2.3 Roles nuevos (a quién le toca qué)

- **Trabajador de cola (Actions + Groq/Gemini):** el que hace el trabajo
  diario. No gasta créditos de Muse, no necesita que nadie le hable.
- **ChatGPT / Codex:** especialista, solo para lo que necesita a ChatGPT
  (sus propias auditorías y revisiones narrativas). Vía: Issue + mención
  @codex SI la prueba de Go lo permite (ver §4.1); si no, vía una Task diaria
  de ChatGPT que revise el bus (despertador) + asignación por navegador de
  Amor como respaldo. ChatGPT NUNCA está en el camino crítico del pipeline
  diario.
- **Grok:** estación manual, degradado. No hay vía programática gratuita
  (ver §1). Su trabajo (generar paquetes) pasa al trabajador de cola. Grok
  queda como fuente opcional cuando se le alcanza por navegador; nada puede
  depender de que responda en horario. Los pendientes que lo necesitan van a
  `bloqueado: sin vía programática gratuita` con el motivo escrito.
- **Amor:** supervisora y excepciones. El cron `coordinacion-modelos` (cada
  4 h) sigue: revisa lo que entregó el trabajador, corrige lo que el
  trabajador no puede, y solo sube a Marco lo que necesita solo a él. Amor
  deja de ser la que hace el trabajo.
- **Marco:** nunca es el mensajero entre modelos. Solo decide lo que solo él
  puede juzgar (una voz, una cara, un tema, un conflicto real).

### 2.4 Reglas duras del mecanismo

- Nada con dinero. Solo niveles gratuitos (Actions en repo público, Groq,
  Gemini, Codex si el plan Go lo permite).
- Verificar por ejecución/commit/PR, nunca por acuse. Un acuse no es entrega.
- Todo lo producido va al repo. El RESULT grande del motor no se versiona
  por límite de la API (413); van recibo + nota.
- No inventar datos, fuentes ni DOIs. Si algo no está verificado, no va.
- Un Issue bloqueado lleva escrito QUÉ lo desbloquea. Sin eso, no es un
  bloqueo, es un abandono.

## 3. Qué quedó implementado en este cambio

- Este documento.
- `.github/ISSUE_TEMPLATE/trabajo-capsula.md`, `trabajo-motor.md`,
  `trabajo-auditoria.md`.
- `ajustes_entre_modelos/LEDGER_ASIGNACIONES.md` (tablero vivo de
  asignaciones con estado y evidencia; se actualiza en cada corrida).
- `scripts/trabajador_cola.py` (v1: validar + texto + motor; `--dry-run` y
  `--self-test` para probarlo sin tocar nada).
- `ajustes_entre_modelos/workflow-trabajador-cola.yml` (copia de staging del
  workflow; instalar en `.github/workflows/`, ver §4.2).

## 4. Pasos que necesitan navegador (para Amor, NO para Marco)

### 4.1 Probar si Codex funciona con el plan Go (una vez)

1. Abrir chatgpt.com/codex con la sesión de marcosabines@gmail.com.
2. Intentar iniciar una tarea en la nube sobre el repo CAPCOT (o comentar
   `@codex` en un Issue de prueba).
3. Anotar el resultado en `LEDGER_ASIGNACIONES.md`:
   - Si arranca: Codex queda como vía para Issues `tipo: auditoria` y
     `tipo: texto` que pidan Codex. Anotar qué plan/límite muestra.
   - Si pide Plus o no arranca: Codex queda DESCARTADO como vía autónoma;
     ChatGPT solo entra por Task diaria (despertador) y por navegador.

### 4.2 Instalar el workflow `trabajador-cola.yml` (una vez)

La app de Muse no puede subir `.github/workflows/` por API (403). Vías, en
este orden:
1. Delegar por el bus a Copilot/Codex con escritura nativa: Issue con el
   archivo de staging (`ajustes_entre_modelos/workflow-trabajador-cola.yml`)
   y la instrucción de copiarlo a `.github/workflows/trabajador-cola.yml`.
2. Si eso no cierra, subirlo por navegador con la sesión de GitHub.

### 4.3 Task diaria de ChatGPT (despertador, una vez)

En chatgpt.com, crear una tarea programada (Plan Go: 3 tareas, 1 vez/día):
"Todos los días, revisa el bus en marcojpad-hash/capcot-capsulas-imaginantes
(ajustes_entre_modelos/DELEGACIONES.md y LEDGER_ASIGNACIONES.md) y en
marcojpad-hash/ChatGPT-migracion, y dime qué Issues con etiqueta `cola` o
`bloqueado` necesitan a ChatGPT. No escribas en el repo desde la tarea;
solo avisa." Anotar que quedó creada.

### 4.4 Primera corrida de verificación

Tras instalar el workflow: crear un Issue de prueba con la plantilla
`trabajo-capsula` y `tipo: validar` sobre un storyboard que ya existe, y
correr el workflow manual (`workflow_dispatch`). El Issue debe quedar
`hecho` con el comentario del resultado, o `bloqueado` con el motivo.
Anotar el resultado en el ledger.
