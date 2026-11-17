# Muertos (≤2 vistas, >20 h) y auditoría de portadas — 17-nov-2026 15:00 CDMX

- de: imaginantes · orden de Mj (17-nov 15:00): todo video con ≤2 vistas se resube; la portada con título va como frame 0 y como miniatura.
- Fuentes: YT Data API (token.json, vistas a las ~15:05 CDMX); TT = último registro del repo (`data/vistas_historico.json`, 17-nov 13:58); FB sin vistas por Reel en el repo.
- Excluidos: jeUrM5zzkdA y Z-nt8t7qPx8 (espera de Mj) y lo de menos de 20 h (KnP1j4y72ug y TT 7708178575924497716, hielo/Baffin 17-nov 13:30).

## Muertos
| Plataforma | id | Título | Vistas | Horas | Acción |
|---|---|---|---|---|---|
| YT | Rg-iTgMExWw | ¿Por qué tenemos hipo? | 1 | 320 | resubida preparada `hipo` (ojo: 4lOWeMn2RCo, mismo archivo, 8 vistas) |
| YT | wxnhEdlJYwU | La corneja decide en 235 milisegundos (resub. idéntica) | 0 | 142 | resubida preparada `corneja` (original ZHdJXFrURk4 tiene 22) |
| YT | JV8SB2EpPyI | El rosa del flamenco viene de su comida | 2 | 80 | resubida preparada `flamenco` |
| TT | 7708761702111759634 | El sarampión volvió a México | 2 | 30 | `sarampion` (fuente 720p reescalada) |
| TT | 7708616723385142580 | El pulpo reparte el trabajo entre tres corazones | 1 | 38 | `pulpo-tres-corazones` (casi duplicado del 3-nov) |
| TT | 7704164766893296902 | El polvo de África no viaja solo | 2 | 326 | `polvo-africa` |
| TT | 7703010495036460308 | La frontera invisible | 1 | 333 | `frontera-jupiter` |
| TT | 7703837369589304597 / 7703837508785818901 / 7701629331411324180 / 7700708931718450450 | cebolla / hielo 3 mantos / lince / ave jurásica | 0–2 | >300 | NO se preparan: ya tienen resubida viva (485 / 515 / 562 / 522) |

## Portadas YT (86 Shorts públicos)
- MP4 localizado por tamaño exacto de archivo (`fileDetails.fileSize`) en 77; 2 más por el MP4 de su resubida (misma portada). Todos los MP4 localizados tienen la portada con título en el frame 0.
- Antes: 46 solo con miniatura 16:9 (sin vertical de Shorts → en el feed móvil sale un frame automático), 13 con un frame posterior con subtítulo, 6 con tarjeta amarilla, 17 OK, 2 excluidos.
- Hecho: `thumbnails.set` con el frame 0 del MP4 en **62** Shorts; todos devolvieron `shortsAspectRatio` y la `sardefault.jpg` coincide con la portada (log: `yt_thumbnails_set_log.json`).
- Sin cambiar: cci90_HP6R4, knAElNo4raI (ya vertical con título), t8nH76NOOH8, N7a9o4xKTas, V4h28RA8bq0 (tarjeta amarilla vertical; su MP4 final no está en la caja), jeUrM5zzkdA y Z-nt8t7qPx8 (excluidos; no tienen portada).
- dz2C-Y8klXA (ornitorrinco): la portada del MP4 corta la palabra («ORNITORRINC/O»); se puso igual porque es el frame 0.

## TT/FB
Portada registrada solo en las cápsulas del 7-nov en adelante (`tt_fb_portadas_registradas.txt`); las de 24–29-oct no tienen registro.

## Resubidas (no subidas)
`/workspace/entregas/resubidas_2026-11-17/<slug>/` con capsula.mp4 (recodificado, frame 0 = portada), portada.jpg y caption.txt; tabla `resubidas.json` (copia aquí). Esperan OK de Mj.
