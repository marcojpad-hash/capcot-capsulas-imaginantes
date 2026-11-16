# Auditoría de frames en cola/entrada — ¿qué se puede subir con solo cambiar audio y subtítulos? (2026-11-16)

**Revisión: listado de `cola/entrada/` (24 paquetes) vía API pública de GitHub, 16-nov-2026 ~13:36 CST. Verificado archivo por archivo: carpeta `frames/`, `RELEVO_EN.md`, `storyboard_en.json`, `guion_en.txt`, `capsula_en.srt`, `capsula_en.mp4`.**

## Veredicto

**Lo que Marco suponía es cierto para los paquetes EN: los 13 paquetes EN tienen frames generados (8–11 por paquete), subtítulos en inglés y storyboard en inglés. Solo falta cambiar el audio (voz am_adam) y quemar los subtítulos.** Ninguno tiene `capsula_en.mp4` en el repo (los MP4 viven en la VM/box, no en el repo, por tamaño).

**Pero el ritmo de 6 al día no se sostiene con este backlog: de los 13, 10 ya están publicados o programados en el canal EN.** Quedan solo 3 listos para montar + 2 que necesitan traducción primero.

## Los 13 paquetes EN con frames (listos, solo audio + subtítulos)

| Paquete | Frames | guion_en | srt_en | Estado en canal EN |
|---|---|---|---|---|
| 2026-10-25_corales-contacto | 9 | no | sí | Programado 16-nov 18:00 |
| 2026-10-26_baffin-bay-ice-shelf | 9 | no | sí | Programado 17-nov 18:00 |
| 2026-10-28_mosquito-fruitless-audicion | 8 | no | sí | Programado 18-nov 18:00 (montado por Pecas) |
| 2026-10-29_juno-choque-proa | 8 | no | sí | Programado 19-nov 18:00 |
| 2026-11-01_mxenes-ia-descubrimiento | 8 | no | sí | Programado 20-nov 18:00 |
| 2026-11-02_oxoboranos-estables | 8 | no | sí | Programado 21-nov 18:00 |
| 2026-11-03_autismo-microbioma-cerebro | 9 | sí | sí | Publicado 15-nov |
| 2026-11-03_enzimas-incrustadas-oceano | 9 | sí | sí | Programado 16-nov 19:00 |
| 2026-11-05_sinergia-algas | 9 | sí | sí | **NO está en el canal — listo para montar** |
| 2026-11-06_adn-sintetico-myc | 9 | sí | sí | **NO está en el canal — listo para montar** |
| 2026-11-09_dato-robot-ensambla-orbita | 11 | sí | sí | **NO está en el canal — listo para montar** |
| 2026-11-10_residual-riesgo-ldl | 9 | sí | sí | Programado 17-nov 19:00 |
| 2026-11-11_agua-magnetismo-hidrogeno | 9 | no | sí | Publicado 15-nov |

Nota: 5 de los 13 no tienen `guion_en.txt` (corales, Baffin, mosquito, Juno, agua-magnetismo), pero sí `storyboard_en.json` + `capsula_en.srt`, que es de donde salió la narración del mosquito EN. No es bloqueador.

## Cola para montar ya (3 + 2)

**Montar directo (frames + EN completo):** sinergia-algas, adn-sintetico-myc, robot-ensambla-orbita.
**Con traducción primero (tienen frames, les faltan los archivos EN):** ratas-topo-damaraland (9 frames), comida-arroz-olvidado (9 frames).

## Paquetes SIN frames en cola/entrada (revisar y solucionar)

9 paquetes sin carpeta `frames/`:

- 2026-10-27_corneja-decision-rapida (tampoco tiene archivos EN)
- 2026-11-05_bacterias-plasticos-oceano (tampoco EN)
- 2026-11-06_telescopio-james-webb-exoplaneta (tampoco EN; excluido del EN por fuentes falsas según DELEGACIONES #8)
- 2026-11-07_arboles-comunicacion-bosque (tampoco EN; el video ES ya está publicado, 749 vistas)
- 2026-11-07_barreleye-4k (tampoco EN; pendiente #2 >24 h)
- 2026-11-07_comida-hielo-caliente / Mpemba (tampoco EN; Mpemba v2 ya está publicado en ES)
- 2026-11-09_andes-virus-aminoacido (tampoco EN; el video ES ya está publicado)
- 2026-11-15_atlas-3d-cerebro (tampoco EN; solo fuentes + storyboard, sin frames)
- 2026-11-16_hera-didymos (tampoco EN; paquete nuevo de hoy)

**Matiz importante:** "sin frames en el repo" no significa "sin frames en ningún lado". Árboles, Mpemba v2 y Andes ya están publicados en ES, así que sus frames existieron en la caja de Imaginantes; solo no quedaron en `cola/entrada/`. Lo que hay que resolver con Imaginantes: confirmar cuáles frames viven en su caja (que los suba a `cola/entrada/`) y cuáles hay que regenerar (atlas-3d-cerebro, corneja, hera-didymos, Barreleye).
