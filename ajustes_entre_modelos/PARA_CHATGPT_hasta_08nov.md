# PARA CHATGPT — Plan hasta el 8-nov-2026 (CDMX)

> Orden de Mj (1-nov): **no gastar créditos del bot Imaginantes**. Tú (ChatGPT) escribes guiones/storyboards; Grok (app principal) hace frames, montaje y programación. El bot solo actualiza docs y commits.
> Fuente de verdad de estados: `data/horario_semana_2026-11-01_07.json` (solo lectura para ti).
> Lee antes: `PARA_CHATGPT_LINEA_EDITORIAL.md` (§1–9, en especial §8 figuras humanas / anti-LLM plano y §9 remontajes), `docs/RECETA_CAPSULA.md`, `docs/FLUJO_EXTERNO.md`.

## 0. HUECOS HOY 4-nov (madrugada 02:30 CDMX) — PRIORIDAD
1. **4-nov 23:30 dato_del_dia** `2026-11-04_dato-polvo-atrapa-oro` — brief completo (DOI verificado) en `PARA_CHATGPT_dato_del_dia.md` § «DATO DE HOY 4 nov» (10:10 CDMX). Entregar en `cola/entrada/2026-11-04_dato-polvo-atrapa-oro/` antes de 16:00 CDMX (límite duro 21:00) con balazo + «¿y a mí qué?» temprano.
2. **4-nov 19:00 intermedio_2** — sin OK de Mj para Machu Picchu y el respaldo NO se entregó (vencía 3-nov 12:00). Entregar YA el respaldo `2026-11-04_inter-cielo-azul-atardecer` ("Por qué el cielo es azul y el atardecer rojo", NASA SpacePlace / NOAA), formato «¿sabías que…?» contradictorio. Límite: 4-nov 12:00 CDMX para que Grok monte y se programe a las 19:00.
(kids 07:00, comida 13:30 e intermedio_1 17:00 ya están programados YT+TT+FB.)

## 1. YA NO TOCAR (programado YT+TT+FB, 1–4 nov)
| Fecha | Hora | project_id |
|---|---|---|
| 1-nov | 03:00 | 2026-11-01_dato-xolo-mictlan |
| 1-nov | 07:00 | 2026-11-01_pulpo-tres-corazones |
| 1-nov | 13:30 | 2026-11-01_llorar-cebolla-quimica |
| 1-nov | 17:00 | 2026-10-26_baffin-bay-ice-shelf |
| 1-nov | 19:00 | 2026-11-03_kids-tiburon-groenlandia (adelantado, sustituyó arqueas) |
| 2-nov | 07:00 | 2026-11-02_camaron-mantis |
| 2-nov | 13:30 | 2026-11-02_comida-pan-duro |
| 2-nov | 17:00 | 2026-10-31_murcielagos-viroma-global |
| 2-nov | 19:00 | 2026-10-31_sequias-energia-renovable |
| 3-nov | 13:30 | 2026-11-03_comida-maillard |
| 3-nov | 17:00 | 2026-10-29_juno-choque-proa |
| 3-nov | 19:00 | 2026-10-31_smartpe-edicion-plantas |
| 4-nov | 07:00 | 2026-11-04_kids-hipo-por-que |
| 4-nov | 13:30 | 2026-11-04_comida-miel-no-caduca |
| 4-nov | 17:00 | 2026-11-04_inter-bioluminiscencia-mar |

Tampoco: arqueas, corales, corneja, mosquito (ya publicados o retirados), Chicxulub y tardígrado sin OK de Mj.

## 2. Prioridad ESTRICTA (en este orden)
**(a) Kids 3-nov 07:00 — NUEVO (urgente, antes del 2-nov 20:00 CDMX)**
- Slot `2026-11-03_kids-TBD`. Tema: animal wow o cuerpo/tip concreto, de temporada otoño si se puede. Que no repita pulpo, tiburón, camarón mantis, hipo, ballena, huesos.
- Elige un slug real `2026-11-03_kids-<tema>` y una fuente primaria verificable (NASA/NOAA/Smithsonian/paper). Si dudas de una cifra, pon `PENDING_SOURCE`.

**(b) Dato del día 23:30 CDMX, 1–7 nov (mismo día)**
- Slots `2026-11-0X_dato-TBD-news`. Una noticia científica del mismo día o de ≤48 h, con fuente primaria (paper DOI, NASA, ESA, agencia). Entrégalo antes de las 18:00 CDMX del día para que Grok alcance a montar.
- Si un día no hay noticia sólida: avisa "SIN DATO <fecha>" en `BITACORA_COORDINACION.md`; no rellenes con algo flojo.

**(c) Rewrite 5–7 nov (kids + comida + inter)**
Los storyboards ya están en cola, pero **sin frames**. Pásalos por la línea editorial §8–9 (arranque con paradoja, metáfora visible, antítesis, cierre con eco) y vuelve a entregarlos en la misma carpeta, como `storyboard.json` v2. Conserva el arranque si ya engancha (§9).
| Fecha | Hora | Carpeta en cola |
|---|---|---|
| 5-nov | 07:00 kids | 2026-11-05_inter-venus-dia-largo |
| 5-nov | 13:30 comida | 2026-11-05_comida-palomitas-explotan |
| 5-nov | 17:00 inter | 2026-11-05_inter-arboles-mito-respiran |
| 5-nov | 19:00 inter | 2026-11-05_inter-rayo-globular (**solo .json** → crear carpeta con storyboard) |
| 6-nov | 07:00 kids | 2026-11-06_inter-corazon-ballena-azul |
| 6-nov | 13:30 comida | 2026-11-06_comida-aguacate-negro |
| 6-nov | 17:00 inter | 2026-11-06_inter-ranas-congeladas |
| 6-nov | 19:00 inter | 2026-11-06_inter-arena-cantante (**solo .json** → crear carpeta) |
| 7-nov | 07:00 kids | 2026-11-07_kids-huesos-bebe |
| 7-nov | 13:30 comida | 2026-11-07_inter-mpemba-mito |
| 7-nov | 17:00 inter | 2026-11-07_inter-suenos-pulpo |
| 7-nov | 19:00 inter | 2026-11-07_extra-nubes-pesan |
Orden si no alcanza: kids → comida → inter_1 → inter_2, primero el 5, luego el 6 y al final el 7.

**(d) 4-nov 19:00 — Machu Picchu (fallas/Pisa)**
- Solo si Mj da OK explícito. Si no hay OK al 3-nov 12:00 CDMX → entrega el respaldo textual **"Por qué el cielo es azul y el atardecer rojo"** (NASA SpacePlace / NOAA) como `2026-11-04_inter-cielo-azul-atardecer`.

## 3. Formato de entrega
- `cola/entrada/<pid>/storyboard.json` + `fuentes.md` (+ `ESTADO_EJECUCION.md` con "PREPARADO_PENDIENTE_REVISION_GROK").
- 8 escenas, 205–235 palabras, voz es-MX-JorgeNeural +7%, en continuo. Cada escena se cablea con la siguiente y el cierre es memorable (firma).
- Por escena: `texto_narracion`, `prompt_visual` (estilo de las plantillas permitidas; nada de litografía azul/dorado, y evita grafiti_colorido, bordado y ukiyo_e), `transicion`.
- Ciencia/naturaleza; sin sociedades. No inventes cifras.

## 4. PROHIBIDO
- Generar frames o imágenes, audio o mp4.
- Publicar o programar en YT/TT/FB.
- Editar `data/*.json` (eso lo actualiza Grok/bot).
- Pedir trabajo al bot Imaginantes.
