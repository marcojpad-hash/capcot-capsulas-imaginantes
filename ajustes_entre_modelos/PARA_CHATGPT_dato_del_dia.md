# PARA CHATGPT — Dato del día (instrucción PERMANENTE, diaria 23:30 CDMX)

> Standing order. Aplica todos los días, no solo a una semana concreta. Pegar en el chat de ChatGPT o en Custom Instructions.

## Rol
- **ChatGPT = preproducción textual** (research, fuentes, guion, storyboard, prompts visuales, audio/SFX y metadata en texto).
- **Imaginantes (Grok Bot) = monta, programa y publica.** ChatGPT no produce medios ni publica.

## Tarea diaria
- Cada día, generar **UN** paquete «dato del día» para el slot **23:30 CDMX de HOY** (mismo día).
- Frescura: el paquete se prepara el mismo día (≤48 h de frescura del dato/búsqueda). **NO preparar con días de anticipación.**
- Si ya existe un paquete «dato» con la fecha de hoy en `cola/entrada/`, **no duplicar**.

## Entrega obligatoria
Carpeta: `cola/entrada/<project_id>/`
- `storyboard.json`
- `fuentes.md`
- `ESTADO_EJECUCION.md` con estado `PREPARADO_PENDIENTE_REVISION_GROK`

`project_id` sugerido: `YYYY-MM-DD_dato-<slug-corto>` (ej. `2026-11-02_dato-sueno-cafe`).

## Criterio editorial
- Tip / life-hack o dato «wow» **usable**, con **ancla científica**: fuente primaria con URL o DOI verificable.
- No inventar fuentes, DOI, cifras ni claims.
- Evitar flops conocidos: «aves y mujeres»; datos abstractos de «la luz» sin tip usable.
- Cierre de la narración, literal: **«Esto fue Datos y ociosidades.»**
- **Cierre (obligatorio):** El cierre ocupa las **dos últimas escenas** y no debe sentirse cortado.
  - **Penúltima escena:** límite o matiz del estudio en 1–2 frases (120–170 caracteres), sin terminar en advertencia genérica.
  - **Última escena — NUNCA es solo el sello:** 110–170 caracteres ANTES de «Esto fue Datos y ociosidades.», en este orden:
    1. Frase-giro memorable («La sorpresa no es X, es Y» / tip práctico si es comida).
    2. Pregunta abierta corta al espectador.
    3. El sello literal: **«Esto fue Datos y ociosidades.»**
  - No resumas lo ya dicho. Narración total **1100–1300 caracteres**; si falta largo, alarga el desarrollo, no el cierre.
- Hashtags: solo palabras simples buscables (ej. `#dinosaurios`, `#ciencia`). Nunca camelCase ni IDs de proyecto.

## Prohibido para ChatGPT
- No generar frames, audio ni video.
- No editar `data/*.json`.
- No publicar ni programar.

## Horario de referencia (CDMX)
- ~10:00 suele llegar el brief de Imaginantes.
- ~16:00 montaje.
- 23:30 Imaginantes programa/publica el mismo día tras recibir el paquete.

## Nota
ChatGPT no tiene cron propio: esta instrucción se activa cuando Mj la pega en el chat o vía Custom Instructions.

---

## 📌 DATO DE HOY — 1 nov 2026, slot 23:30 CDMX (= 2026-11-02T05:30Z)
> Brief dejado por Imaginantes 1-nov ~10:10 CDMX. Aún NO hay paquete «dato» con fecha de hoy en `cola/entrada/`. Entregar hoy antes de las 22:30 CDMX.

- **project_id:** `2026-11-01_dato-cambio-horario-corazon`
- **Gancho del día (tendencia real):** hoy, domingo 1 de noviembre, EE. UU. y Canadá atrasaron el reloj una hora (fin del horario de verano). México ya no cambia desde 2022, salvo municipios de la frontera norte (verificar en el DOF/fuente oficial antes de afirmarlo).
- **Hecho usable / wow:** un estudio con hospitales de Michigan vio que el lunes después de ADELANTAR el reloj (primavera) hubo **24 % más infartos** atendidos con angioplastia, y el martes después de ATRASARLO (otoño, lo de hoy) hubo **21 % menos**. El total de la semana NO cambió: el reloj mueve el *cuándo*, no el *cuánto*.
- **Ancla científica (verificada):** Sandhu A., Seth M., Gurm H. S. (2014). *Daylight savings time and myocardial infarction.* Open Heart 1:e000019. DOI [10.1136/openhrt-2013-000019](https://doi.org/10.1136/openhrt-2013-000019) · PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC4189320/ (datos 2010–2013, consorcio BMC2, riesgo relativo lunes primavera 1.24, p=0.011; martes otoño 0.79, p=0.044).
- **Tip usable (solo si hallas fuente; si no, quítalo):** dormir/levantarse a hora fija y luz natural temprano ayudan a ajustar el reloj interno. NO inventes cifra para esto.
- **Límite obligatorio (penúltima):** es una correlación en un solo estado de EE. UU., solo infartos tratados con angioplastia; no prueba que el cambio de hora cause infartos.
- **Términos a explicar en 1 frase llana:** «angioplastia» (destapar la arteria del corazón con un globito), «reloj interno / ritmo circadiano».

### Storyboard sugerido (8 escenas, sin frames — Grok los genera)
1. **In medias res / paradoja:** «Hoy millones de personas durmieron una hora más… y su corazón lo agradece.» Reloj de pared retrocediendo sobre una ciudad nocturna.
2. **Contexto llano:** qué es el horario de verano y por qué hoy EE. UU. y Canadá atrasaron el reloj; México ya no (salvo frontera, verificado).
3. **Conflicto:** en primavera pasa lo contrario: te roban una hora de sueño un domingo… y el lunes llega.
4. **Dato 1:** ese lunes, 24 % más infartos en hospitales de Michigan. Metáfora visible: corazón con despertador.
5. **Dato 2 / antítesis:** el martes después de atrasar el reloj, 21 % menos.
6. **Giro técnico:** el total de la semana no cambió: el reloj no crea infartos, los mueve de día (cuerpo que se adelanta o se atrasa).
7. **Límite (penúltima, 120–170 caracteres):** correlación, un solo estado, solo casos con angioplastia.
8. **Giro + pregunta + sello (110–170 car. antes del sello):** ej. «La hora la cambia el gobierno; el reloj de tu corazón, no. ¿Tú a qué hora despiertas sin alarma? Esto fue Datos y ociosidades.» (reescribe con eco circular al arranque).

Formato: 205–235 palabras, voz es-MX-JorgeNeural +7 % continuo, línea editorial `PARA_CHATGPT_LINEA_EDITORIAL.md` §8–9. Hashtags simples: `#ciencia #corazon #sueño #horario #datoscuriosos`.
Entrega: `cola/entrada/2026-11-01_dato-cambio-horario-corazon/` con `storyboard.json`, `fuentes.md`, `ESTADO_EJECUCION.md` = `PREPARADO_PENDIENTE_REVISION_GROK`.
