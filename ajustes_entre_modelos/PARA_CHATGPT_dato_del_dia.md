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

## (Cubierto) Dato 8 nov 2026, slot 23:30 CDMX — NO entregar paquete nuevo

> Recheck Imaginantes 8-nov ~10:05 CDMX (corrida ≈10:00 de la rutina «dato del día»).
> **NO hay** `cola/entrada/2026-11-08_dato-*`. El único paquete «dato» en `cola/entrada/` es `2026-11-07_dato-clavo-te-cocina/` (fecha 7-nov).
> El slot **23:30 de HOY ya está ocupado** por ese dato del 7-nov, que llegó tarde y se programó para el 8-nov 23:30 CDMX:
> - project_id: `2026-11-07_dato-clavo-te-cocina`
> - Título: «¿Qué queda en tu cocina después de limpiar?»
> - YT [EwZ3dHalUn0](https://youtube.com/shorts/EwZ3dHalUn0) programado (oEmbed 403 coherente con privado/programado)
> - TT Scheduled Nov 9, 12:30 AM GMT-5 New York (= 23:30 CDMX), Everyone
> - FB Scheduled Sunday Nov 8 at 11:30 PM, Público
> Fuente de verdad: `data/horario_2026-11-08.json` (actualizado 07:53 CDMX) y `docs/briefs/2026-11-08_RADAR_CAPCOT.md` (NO_DUPLICAR).
> El 07:00 de hoy también está cubierto: palomitas `2026-11-05_comida-palomitas`, YT [zTP5akrGA9M](https://youtube.com/shorts/zTP5akrGA9M), publicado YT+TT+FB.
>
> **ChatGPT: NO generar ni entregar** un `cola/entrada/2026-11-08_dato-*`. No hay slot 23:30 libre el 8-nov. No preparar el dato del 9-nov hoy (regla: mismo día, sin anticipación).
> **Grok app: NO montar, no regenerar frames ni reprogramar** el clavo; ya está en parrilla. El paquete textual en `cola/entrada/2026-11-07_dato-clavo-te-cocina/` es archivo, no pedido de producción.


## (Cubierto con reserva) Dato 7 nov 2026, slot 23:30 CDMX — reserva evergreen pan YT PTk2QNMkOn4; el clavo se programó al 8-nov 23:30
> Actualización 8-nov ~10:05: el paquete SÍ está en `cola/entrada/2026-11-07_dato-clavo-te-cocina/` y quedó programado para el **8-nov 23:30** (YT EwZ3dHalUn0, TT+FB). El 7-nov 23:30 se cubrió con la reserva pan (PTk2QNMkOn4). El brief de abajo sigue como registro, no como pedido vigente.
> Guardia nocturna 7-nov ~22:20 CDMX: no hubo `cola/entrada/2026-11-07_dato-clavo-te-cocina/`. Se programó la reserva pan (capsula_v2) en YT+TT+FB a las 23:30 CDMX. El brief de abajo queda como registro, no como pedido vigente.
> Brief dejado por Imaginantes 7-nov ~16:10 CDMX (la corrida de ~10:00 falló; este es el primer brief del día). **NO hay paquete «dato» del 7-nov** en `cola/entrada/` (hay `barreleye-4k`, `comida-hielo-caliente`/Mpemba y `arboles-comunicacion-bosque`; ninguno es `*_dato-*` ni está asignado a 23:30). El slot en `data/horario_semana_2026-11-01_07.json` sigue como `2026-11-07_dato-TBD-news` / `pendiente_dato_dia`.
> Entregar HOY antes de las **21:00 CDMX** en `cola/entrada/2026-11-07_dato-clavo-te-cocina/` (`storyboard.json` + `fuentes.md` + `ESTADO_EJECUCION.md` = `PREPARADO_PENDIENTE_REVISION_GROK`) para que Grok app haga QA→frames→montaje→YT+TT+FB a **23:30 CDMX** (TT AI ON, FB sin AI; UI Nueva York = CDMX+1 h).
> DOI **verificado en Crossref por Imaginantes 7-nov 16:10** (publicado 30-oct-2026, *BMC Microbiology*, open access CC BY 4.0). Tip cocina / superficie — hueco editorial del canal. No repite Mpemba, Venus, arena, huesos, nubes ni pulpo de la parrilla de hoy.

- **project_id:** `2026-11-07_dato-clavo-te-cocina`
- **Fuente primaria:** Sezer et al. (2026) «Antimicrobial and antibiofilm effects of clove tea on bacteria isolated from kitchen food-contact surfaces». *BMC Microbiology*. DOI `10.1186/s12866-026-05875-y` — https://doi.org/10.1186/s12866-026-05875-y · https://bmcmicrobiol.biomedcentral.com/articles/10.1186/s12866-026-05875-y
- **Título sugerido (no técnico):** «El clavo que sobrevive a tu trapeador» o «¿Sabías que tras limpiar la cocina aún quedan bacterias?». Prohibido «MIC», «MBC», «biofilm» o «Staphylococcus» en el título.
- **Balazo (in medias res, sin «según un estudio»):** «Acabas de limpiar la cocina… y bajo el trapo todavía hay un ejército invisible haciendo casa.»
- **¿Y a mí qué? (obligatorio en escenas 1–2):** ancla cotidiana — la tarja, la tabla o la cubierta donde cortas verdura / dejas el plato. El tip es sobre lo que puede quedar **después** de la limpieza de siempre, no para asustar: para sumar un refuerzo barato.
- **Hecho usable / wow (solo lo que dice el abstract; léelo entero antes de escribir):**
  - Tomaron hisopos **después de la limpieza rutinaria** en superficies de contacto con comida de una cocina de comida preparada (50 puntos).
  - Sacaron **22 aislados**: *Escherichia coli* y *Staphylococcus aureus*; **15 de 22** formaban biofilm (capa pegajosa).
  - El **té de clavo** (clavo de olor infusionado) afectó esas bacterias de forma **dependiente de la concentración**.
  - Concentración inhibitoria mínima media (**MIC**) ≈ **15 %**; bactericida media (**MBC**) ≈ **19,33 %**. Explica «MIC/MBC» en una frase llana una sola vez («la dosis con la que deja de crecer» / «la dosis con la que muere»).
  - Más tiempo de contacto ayudó, pero **la concentración importó más**.
- **Límite / matiz (penúltima escena, obligatorio):** el propio paper lo dice: es un refuerzo **además** de la limpieza de siempre, **no un reemplazo**. Estudio de laboratorio sobre aislados de una cocina; no promete desinfección hospitalaria ni que «el clavo mate todo».
- **Giro final (última escena):** «La sorpresa no es que la cocina se ensucie: es que un té de clavo barato puede ayudar donde el trapeador ya pasó.» + pregunta abierta («¿Tú qué dejas «limpio» sin mirar dos veces?») + **«Esto fue Datos y ociosidades.»**
- **Formato trend:** tip cocina usable + «¿sabías que…?» contradictorio (limpiaste y aún hay biofilm). Público general, no kids.
- **Storyboard 8 escenas (texto, SIN frames):**
  1. Balazo: trapeador / esponja; zoom a capa invisible que se pega.
  2. ¿Y a mí qué?: tu tarja o tabla de picar; plato que «ya lavaste».
  3. El problema: biofilm = bacterias haciendo «casita» pegajosa que el trapo no siempre arranca.
  4. La escena del estudio: 50 puntos hisopados tras limpiar; aparecen E. coli y S. aureus (nómbralos una vez, luego «esas bacterias»).
  5. El tip: infusionar clavo de olor (té de clavo) y probarlo contra esas bacterias / biofilms maduros.
  6. Dato numérico: ~15 % para frenar el crecimiento, ~19 % para matar (medias del paper); más fuerte = más efecto.
  7. Matiz: refuerzo post-limpieza, no sustituye jabón/cloro ni convierte tu cocina en quirófano.
  8. Giro + pregunta + sello.
- **Personajes Imaginantes:** usar los propios del canal (ver `PARA_CHATGPT_LINEA_EDITORIAL.md` §8); estilo CapCut con imágenes fijas o animación narrada, subtítulos abajo. **NO HyperFrames.**
- **Hashtags (solo alto volumen):** `#curiosidades #ciencia #cocina #datosinteresantes #sabiasque #shorts`. Nada de `#biofilm` ni tags técnicos.
- **No inventar:** ni «mata el 99,9 %», ni que sustituye desinfectante, ni cifras de casas mexicanas, ni que el clavo cura infecciones.
- **Portada obligatoria (Mj 7-nov):** primera escena = portada con título grande en caja amarilla/crema y subrayado rojo; sin subtítulo encima (para la cuadrícula de Shorts/TT).
- **Plan B (si el clavo no cierra el enganche):** Grove et al. (2026) «The neural basis of flavour–nutrient learning». *Nature*, publicado 4-nov-2026. DOI `10.1038/s41586-026-11229-5` — https://doi.org/10.1038/s41586-026-11229-5. Ángulo: la boca estima el nutriente por el sabor y el intestino lo confirma; un circuito de dopamina en la amígdala aprende el vínculo. Tip usable débil → prioriza paradoja «tu lengua adivina, tu panza califica». PROHIBIDO medicalizar o prometer control de antojos. Lee el artículo; no inventes regiones ni neurotransmisores que no estén ahí.

---

## (Vencido) Dato 4 nov 2026, slot 23:30 CDMX (= 2026-11-05T05:30Z) — cubierto en producción (polvo/oro Rv998OZDUYc)
> Brief dejado por Imaginantes 4-nov ~10:10 CDMX. NO hay paquete «dato» del 4-nov en `cola/entrada/` (solo kids-hipo, miel e bioluminiscencia, ya programados en otros slots). Entregar HOY antes de las 21:00 CDMX en `cola/entrada/2026-11-04_dato-polvo-atrapa-oro/` (storyboard.json + fuentes.md + ESTADO_EJECUCION.md = `PREPARADO_PENDIENTE_REVISION_GROK`) para que Grok app haga QA→frames→montaje antes de las 22:30.
> Tema tomado del radar `docs/briefs/2026-11-04_RADAR_CAPCOT.md` (C03). DOI **verificado en Crossref por Imaginantes 4-nov 10:08** (publicado 30-oct-2026, Nature Communications, open access). No repite miel/hipo/bioluminiscencia/cielo azul de hoy.

> ⏰ **Recheck Imaginantes 4-nov ~16:07 CDMX:** sigue SIN paquete en `cola/entrada/2026-11-04_dato-polvo-atrapa-oro/`. Brief vigente sin cambios. Límite de entrega 21:00 CDMX; si no llega, la producción fin de día (~22:00) cubre el slot 23:30.

- **project_id:** `2026-11-04_dato-polvo-atrapa-oro`
- **Fuente primaria:** Zhu Z. et al. (2026) «Hydrogen-bond-mediated quasi-two-dimensional covalent organic frameworks for ultrahigh gold extraction». *Nature Communications*. DOI `10.1038/s41467-026-78532-7` — https://www.nature.com/articles/s41467-026-78532-7 (Nanjing University of Science and Technology + Shanghai Advanced Research Institute, CAS).
- **Título sugerido (no técnico):** «Este polvo atrapa 5 veces su peso en oro» o «¿Sabías que hay oro en tu cajón?». Prohibido «COF», «estructura orgánica covalente» o «quasi-2D» en título.
- **Balazo (in medias res, sin «según un estudio»):** «Un gramo de este polvo amarillo se tragó cinco gramos de oro… y lo dejó convertido en pepitas.»
- **¿Y a mí qué? (obligatorio en escenas 1–2):** el oro no solo está en anillos: hay oro en las placas de los celulares y aparatos viejos que guardas en un cajón. Para decirlo hay que **citar fuente oficial** en `fuentes.md` (p. ej. el *Global E-waste Monitor* de la ONU/UNITAR-ITU, o la EPA de EE. UU.). El paper NO habla de celulares: si no encuentras y verificas la fuente, usa solo el ancla «el oro de tus aretes o de un anillo» sin cifras.
- **Hecho usable / wow (lo que sí dice el paper):**
  - Es un material poroso de laboratorio (red orgánica tipo esponja/panal) diseñado para **atrapar oro disuelto** en agua (iones de oro).
  - Truco del diseño: grupos que apuntan «hacia afuera» y puentes de hidrógeno entre cadenas lo vuelven **plano y ordenado**, así los «ganchos» quedan expuestos en vez de escondidos dentro de los poros.
  - No solo lo atrapa: lo **reduce** a oro metálico; con calor suave y vibración se forman **nanopartículas de oro** que se juntan.
  - Capacidad reportada: **5 082,32 mg de oro por gramo** de material ≈ **5 veces su propio peso**. (Esta conversión es aritmética de la cifra del abstract; dila así, sin redondear a «5 kilos» ni similares.)
- **Límite / matiz (penúltima escena):** es un resultado de laboratorio en condiciones controladas; todavía no es una planta de reciclaje ni significa que puedas sacar oro de tu celular en casa.
- **Giro final (última escena):** «La sorpresa no es encontrar oro, es diseñar una esponja que lo atrape solo a él.» + pregunta abierta («¿Cuántos celulares viejos tienes guardados?») + **«Esto fue Datos y ociosidades.»**
- **Formato trend:** «¿sabías que…?» contradictorio + «qué pasa dentro de…» (zoom al material). Público general, no kids.
- **Storyboard 8 escenas (texto, SIN frames):**
  1. Balazo: polvo amarillo en una balanza que «se traga» oro; contador 1 g → 5 g.
  2. ¿Y a mí qué?: cajón con celulares y cargadores viejos / anillo (según lo que verifiques).
  3. El problema: oro disuelto en agua = invisible y difícil de recuperar.
  4. Qué pasa dentro: esponja/panal molecular con ganchos escondidos en los poros (la versión vieja que se tapa).
  5. El truco: puentes de hidrógeno «aplanan» las cadenas; ganchos al descubierto.
  6. Atrapar y transformar: iones → nanopartículas de oro que se juntan con calor suave y vibración.
  7. Matiz: laboratorio en Nanjing/Shanghái; aún no es industria ni truco casero.
  8. Giro + pregunta + sello.
- **Personajes Imaginantes:** usar los propios del canal (ver `PARA_CHATGPT_LINEA_EDITORIAL.md` §8); estilo CapCut con imágenes fijas o animación narrada, subtítulos abajo.
- **Hashtags (solo alto volumen):** `#curiosidades #ciencia #datosinteresantes #sabiasque #shorts #oro`. Nada de `#COF` ni tags técnicos.
- **No inventar:** ni cifras de cuánto oro tiene un celular sin fuente oficial citada, ni costos, ni fechas de aplicación industrial.
- **Plan B (si el oro no cierra el enganche):** radar C02 murciélagos y sus virus (Nature Communications, DOI `10.1038/s41467-026-79059-7`, también verificado en Crossref): «no es lo que comen, es dónde viven». Murciélagos fue el Short ganador del 3-nov. Prohibido el tono de alarma de contagio.

---

## (Vencido) Dato 3 nov 2026, slot 23:30 CDMX (= 2026-11-04T05:30Z) — cubierto y programado (R76ivFX9nXo)
> **Re-chequeo 3-nov ~16:05 CDMX (Imaginantes): SIGUE SIN paquete** `cola/entrada/2026-11-03_dato-polvo-africano-microbios/`. El brief de abajo sigue vigente; entregar antes de las 22:30 CDMX para que Grok app haga QA→frames→montaje a 23:30. El control de cola 16:23 (`docs/briefs/2026-11-03_CONTROL_COLA.md`) excluyó expresamente el dato del día: no cuenta como entrega.

> Brief dejado por Imaginantes 3-nov ~10:15 CDMX. NO hay paquete «dato» del 3-nov en `cola/entrada/` (horario: `2026-11-03_dato-TBD-news` = `pendiente_dato_dia`). `2026-11-03_enzimas-incrustadas-oceano` NO cuenta: no está asignado a 23:30 y su guion quedó FAIL de enganche. Entregar hoy antes de las 22:30 CDMX.
> Tema tomado del radar `docs/briefs/2026-11-03_RADAR_CAPCOT.md` (candidato 1, «mayor fuerza visual»), publicado hace 7 días y con DOI verificado en Crossref. Trends MX del corte 08:01 no traen este tema; no fuerces relación con «vórtice polar».

- **project_id:** `2026-11-03_dato-polvo-africano-microbios`
- **Balazo (in medias res, sin «según un estudio»):** «El aire que respiraba la selva del Amazonas cambió de dueño en cinco días… y venía de África.»
- **¿Y a mí qué? (obligatorio en escenas 1–2):** el aire que respiras no es solo de tu ciudad: el polvo viaja miles de kilómetros y trae vida microscópica. Ancla cotidiana: el polvo que se te pega en el carro o la ventana. Si quieres decir que el polvo del Sahara también llega a México/Caribe, VERIFÍCALO con fuente oficial (SMN/CONAGUA o NOAA) y cítalo en `fuentes.md`; si no la encuentras, di solo «cruza el Atlántico hasta América».
- **Hecho usable / wow:** en la Torre Alta del Amazonas (ATTO) midieron el aire a 42 y 323 m del suelo antes y durante una llegada de polvo del norte de África de 5 días. Durante el polvo, las **bacterias** del aire cambiaron fuerte hacia microbios de suelos secos, costras del desierto y del mar; los **hongos** casi no cambiaron. Las **endotoxinas** en el aire se triplicaron, pero NO aumentaron los patógenos obligados.
- **Ancla científica (verificada, DOI en Crossref):** Weber J. et al. (2026). *Amazonian rainforest bioaerosol influenced by African dust intrusion.* Communications Earth & Environment, publicado 27-oct-2026. DOI [10.1038/s43247-026-04119-1](https://doi.org/10.1038/s43247-026-04119-1) · https://www.nature.com/articles/s43247-026-04119-1 — Lee el artículo antes de escribir; NO agregues cifras que no estén ahí.
- **Límite obligatorio (penúltima):** fue un solo episodio de 5 días en un sitio; endotoxinas ≠ infección; no se encontraron más patógenos. PROHIBIDO titular «el polvo africano trae enfermedades».
- **Términos a explicar en 1 frase llana:** «bioaerosol» (vida microscópica flotando en el aire), «endotoxina» (pedacitos de la pared de ciertas bacterias que pueden irritar, aunque la bacteria ya no esté viva).

### Storyboard sugerido (8 escenas, sin frames — Grok los genera; estilo CapCut: stills/animación narrada con personajes Imaginantes, NO HyperFrames)
1. **Balazo:** nube naranja cruzando el océano hacia la selva; torre metálica entre la niebla.
2. **¿Y a mí qué?:** el polvo de tu ventana también viene de lejos; el aire es una carretera con pasajeros invisibles.
3. **Contexto:** la torre de 325 m en el Amazonas que «olfatea» el aire a dos alturas.
4. **Dato 1:** llega el polvo y en 5 días las bacterias del aire ya son otras: del desierto y del mar.
5. **Dato 2 / antítesis:** los hongos casi no se movieron. No todo viaja igual.
6. **Giro:** las endotoxinas se triplicaron… pero los patógenos no aumentaron. Más irritante no es lo mismo que más enfermedad.
7. **Límite (penúltima, 120–170 car.):** un episodio, un sitio, cinco días; falta ver si pasa igual siempre.
8. **Giro + pregunta + sello (110–170 car. antes del sello):** eco circular con el balazo, p. ej. «La próxima vez que limpies el polvo, piensa que quizá cruzó un océano con pasajeros. ¿Tú qué crees que viaja en tu aire? Esto fue Datos y ociosidades.»

QA de enganche (Mj, estricto): si las escenas 1–2 no dicen por qué le importa a alguien que no buscó el video, es FAIL aunque el técnico pase. Formato: 205–235 palabras, 1100–1300 caracteres, voz es-MX-JorgeNeural +7 % continuo, `PARA_CHATGPT_LINEA_EDITORIAL.md` §8–9. Hashtags solo de alto volumen: `#ciencia #datoscuriosos #curiosidades #naturaleza #shorts`.
Entrega: `cola/entrada/2026-11-03_dato-polvo-africano-microbios/` con `storyboard.json` (con `fecha_objetivo: 2026-11-03` y `slot_local: 23:30`), `fuentes.md`, `ESTADO_EJECUCION.md` = `PREPARADO_PENDIENTE_REVISION_GROK`.

---

## (Vencido) Dato 2 nov 2026 (Día de Muertos), slot 23:30 CDMX (= 2026-11-03T05:30Z)
> ⏰ Re-chequeo 2-nov ~16:07 CDMX: sigue SIN paquete en `cola/entrada/`. Límite de entrega 22:30 CDMX.
> Brief dejado por Imaginantes 2-nov ~10:05 CDMX. NO hay paquete «dato» con fecha de hoy en `cola/entrada/`. Entregar hoy antes de las 22:30 CDMX. El brief del 1-nov (cambio de horario) quedó vencido abajo; no lo entregues.

- **project_id:** `2026-11-02_dato-cempasuchil-raices`
- **Gancho del día (tendencia real):** hoy, 2 de noviembre, millones de ofrendas en México llevan cempasúchil. Después del Día de Muertos, mucha gente tira las flores o las macetas.
- **Hecho usable / wow:** la raíz del cempasúchil (género *Tagetes*) suelta una sustancia, el **alfa-tertienilo**, que es tóxica para los **nematodos agalladores**: gusanitos microscópicos del suelo que hinchan y pudren las raíces de jitomate, pepino y chile. Con luz se vuelve más potente, pero incluso a oscuras (bajo tierra) mata larvas de nematodo, porque atraviesa su piel y les causa estrés oxidativo.
- **Tip usable (con fuente):** la flor solo protege mientras está **viva y creciendo**. En invernadero, el cempasúchil francés (*Tagetes patula*) redujo los nematodos en el suelo húmedo y activo, pero no en el suelo seco, donde los nematodos están dormidos. Por eso conviene sembrarlo justo después de la cosecha y en suelo regado, no echar flores secas de la ofrenda como si fueran veneno.
- **Ancla científica (verificada):**
  - Hamaguchi T. et al. (2019). *Nematicidal actions of the marigold exudate α-terthienyl: oxidative stress-inducing compound penetrates nematode hypodermis.* Biology Open 8(4): bio038646. DOI [10.1242/bio.038646](https://doi.org/10.1242/bio.038646) · PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6504006/
  - Marahatta S. P., Wang K.-H., Sipes B. S., Hooks C. R. R. (2012). *Effects of Tagetes patula on Active and Inactive Stages of Root-Knot Nematodes.* J Nematol 44(1):26–30. PMID 23482862 · PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC3593261/
  - NO inventes porcentajes. El «≈50 %» que aparece en Marahatta 2012 viene de un estudio previo (Marahatta et al. 2010) citado ahí; úsalo solo si lo verificas en esa fuente primaria, si no, di «menos nematodos» sin cifra.
- **Límite obligatorio (penúltima):** son ensayos de laboratorio e invernadero; en campo el efecto es inconsistente, el lixiviado de raíz no frenó la eclosión de huevos y las flores cortadas o secas no sirven.
- **Términos a explicar en 1 frase llana:** «nematodo» (gusano tan pequeño que no se ve a simple vista), «estrés oxidativo» (la sustancia «oxida» las células del gusano como el óxido al metal), «alfa-tertienilo» (puedes decir «una molécula de la raíz» y nombrarla una sola vez).
- **Evitar:** no prometer que el cempasúchil cura plagas de todo tipo ni que repele mosquitos (no está en estas fuentes). Tono de Día de Muertos respetuoso, sin calaveras de terror.

### Storyboard sugerido (8 escenas, sin frames — Grok los genera)
1. **In medias res / paradoja:** «La flor que hoy guía a los muertos… bajo tierra se dedica a matar.» Ofrenda con cempasúchil; la cámara baja al suelo y se ven las raíces.
2. **Contexto llano:** qué es un nematodo; zoom a un gusanito transparente entrando a la raíz de un jitomate.
3. **Conflicto:** las agallas, raíces hinchadas como nudos, y la planta que se marchita aunque la riegues.
4. **Dato 1:** la raíz del cempasúchil suelta una molécula que es veneno para esos gusanos. Metáfora visible: la raíz como guardiana con farol naranja.
5. **Dato 2 / antítesis:** con luz es más potente, pero a oscuras también mata: atraviesa la piel del gusano y lo «oxida» por dentro.
6. **Giro técnico / tip:** solo funciona si la planta está viva y el suelo húmedo, cuando los gusanos están despiertos; en suelo seco no hizo efecto. Sembrarla tras la cosecha.
7. **Límite (penúltima, 120–170 caracteres):** laboratorio e invernadero, en campo falla a veces, y la flor seca de la ofrenda no sirve.
8. **Giro + pregunta + sello (110–170 car. antes del sello):** ej. «Hoy la usamos para recordar a los que se fueron; en el huerto, para que la planta no se vaya. ¿Qué harás con tu cempasúchil mañana? Esto fue Datos y ociosidades.» (reescribe con eco circular al arranque).

Formato: 205–235 palabras, narración 1100–1300 caracteres, voz es-MX-JorgeNeural +7 % continuo, línea editorial `PARA_CHATGPT_LINEA_EDITORIAL.md` §8–9. Hashtags simples: `#cempasuchil #diademuertos #ciencia #huerto #datoscuriosos`.
Entrega: `cola/entrada/2026-11-02_dato-cempasuchil-raices/` con `storyboard.json`, `fuentes.md`, `ESTADO_EJECUCION.md` = `PREPARADO_PENDIENTE_REVISION_GROK`.

---

## (Vencido) Dato 1 nov 2026, slot 23:30 CDMX (= 2026-11-02T05:30Z)
> Brief dejado por Imaginantes 1-nov ~10:10 CDMX. Aún NO hay paquete «dato» con fecha de hoy en `cola/entrada/`. Entregar hoy antes de las 22:30 CDMX.
> Revisión Imaginantes 1-nov ~16:10 CDMX: sigue SIN paquete en `cola/entrada/2026-11-01_dato-cambio-horario-corazon/`. Brief abajo sigue vigente; entregar antes de 22:30 CDMX.

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

## Brief del día 2026-11-10 (slot 23:30 CDMX) — sin paquete en cola a las 10:00
- Pendiente: `cola/entrada/2026-11-10_dato-<slug>/` (storyboard.json, fuentes.md, ESTADO_EJECUCION.md).
- Formato: tip práctico de cocina/hogar con ancla científica verificable (URL/DOI); 8 escenas, 85–90 s, cierre de 2 escenas (≥10 s) con «Esto fue Datos y ociosidades.».
- Variedad: base distinta de las 50 plantillas, paleta y encuadres distintos a los de 7–9 nov (no gouache verde azulado/dorado, no la científica recurrente); 9–10 frames con plano_seconds=5 si aplica.
- Sin frames, sin audio, sin publicar. Montaje/QA/publicación: Grok app.

## Brief del día 2026-11-11 (slot 23:30 CDMX) — sin paquete en cola a las 10:00
- Pendiente: `cola/entrada/2026-11-11_dato-<slug>/` (storyboard.json, fuentes.md, ESTADO_EJECUCION.md).
- Formato: tip práctico de cocina/hogar con ancla científica verificable (URL/DOI); 8 escenas, 85–90 s, cierre de 2 escenas (≥10 s) con «Esto fue Datos y ociosidades.». No repetir Mpemba (ya programado 13:30), ballena, aguacate ni clavo.
- Variedad: base distinta de las 50 plantillas, otra paleta y encuadres (general, cenital, macro, contrapicado, detalle); 9–10 frames con plano_seconds=5.
- Sin frames, sin audio, sin publicar. Montaje/QA/publicación: Grok app.
