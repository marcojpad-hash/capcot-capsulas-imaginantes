# Horarios de publicación (TikTok y YouTube Shorts)

Actualizado: 2026-11-26. Todas las horas finales están en **CDMX (UTC-6, sin horario de verano)**.

## Política operativa vigente (corte 2026-11-23)

Fuente de verdad consultada: `main:data/horarios.json`, actualización 2026-11-23. La copia `feature/data/horarios.json` es anterior y permanece sin modificar por la regla de solo lectura; el programador de la rama refleja explícitamente esta política vigente.

| Ventana | CDMX | Estado | Uso |
|---|---|---|---|
| Mañana | 06:30–07:30 | Activa | YouTube Shorts + TikTok espejo |
| Mediodía | 13:00–14:30 | **Prueba reversible desde 23-nov** | Solo si fecha, rotación y conflictos de ambas ramas dejan el slot libre |
| Tarde | 16:30–18:00 | Activa | YouTube Shorts + TikTok espejo |
| Dato del día | 23:30 fijo | Slot separado | No lo asigna `hora_publicacion()`; requiere proyecto y evidencia propios |

La ventana de prueba de mediodía sustituye el registro legado 13:30–15:00; 13:30 sigue siendo una hora posible dentro de 13:00–14:30, no una ventana independiente. La franja 19:00–21:00 está retirada desde 5-nov. El slot fijo 23:30 nunca se ofrece como ventana variable.

Antes de asignar: comprobar `fecha_objetivo + slot_local`, rotación, publicaciones, programaciones y `main` de solo lectura. Si no queda una ventana autorizada, el resultado es `NO_SLOT_DISPONIBLE`: bloquear publicación y TikTok, nunca convertir la falta de slot en publicación inmediata.

Conversión: con horario de verano en EE.UU. (mar–nov) sumar +1 h más a ET/CT/PT; España en verano (CEST) = CDMX+8.

## Fuentes

| Fuente | Segmento | Zona original | Qué dice |
|---|---|---|---|
| [VISUAL Review 2024 – Divulgadores científicos en TikTok](https://doi.org/10.62161/revvisual.v16.5247) | Ciencia (hispano) | local | Encuesta a 36 divulgadores: 52.8% publica tarde (12–19), 47.2% noche (20–24). Sin métricas de rendimiento. |
| [Hootsuite – Educación 2025](https://blog.hootsuite.com/social-media-education-benchmarks/) | Educación | local (118 países) | TikTok: miércoles 4–6 p.m. |
| [Hashmeta](https://hashmeta.com/insights/best-time-post-tiktok) | Educativo | EST | mar–mié 2–4 p.m. y 8–10 p.m.; dom 7–9 p.m. (metodología no publicada). |
| [Kapwing vía Small Biz Trends](https://smallbiztrends.com/kapwing-study-best-times-to-post-on-tiktok/) | General | ET | 15k videos: mié 12 p.m. ET; mañanas fuertes. |
| [TokPortal 2025](https://www.tokportal.com/post/the-best-time-to-post-on-tiktok-for-us-reach-in-2025-data-by-time-zone) | EE.UU. | local por zona | CT 12–14 y 20–21:30; ET 11:30–13:30 y 19–21; PT 12:30–14 y 20:30–22. |
| [Hootsuite TikTok 2025](https://blog.hootsuite.com/best-time-to-post-on-tiktok/) | General | local | Por día: lun 17, mar 10–13, mié 16–18, jue 7–9, vie 16–18, sáb 10–19, dom 8–12. |
| [Later](https://later.com/blog/best-time-to-post-on-tiktok/) | General | PST | lun–vie 10 a.m. PST (= 12 CDMX invierno). |
| [Adobe vía MarketingProfs](https://www.marketingprofs.com/charts/2025/52561/the-best-days-and-times-to-post-on-tiktok) | General | UTC | 5, 8 y 19 UTC (= 23, 2 y 13 h CDMX); domingo más vistas. |
| [Sprout Social vía Marketing4eCommerce MX](https://marketing4ecommerce.mx/mejor-hora-para-publicar-en-tiktok/) | General/educación | local | Mié–jue muy alto 15–18 h; educación mar–mié 16–17 h. |
| [Tiendanube](https://www.tiendanube.com/blog/cuales-son-las-mejores-horas-para-publicar-en-tiktok/) | México | hora MX | Horas por día (p.ej. jue 9, 12, 19; sáb 11, 19, 20); sin metodología. |
| [Allmarket](https://allmarket.ai/blog/mejor-hora-para-publicar-tik-tok/) | Latam | local | MX 6–8, 13–15, 19–23; Argentina 20–00. Orientativo. |
| [Shopify ES](https://www.shopify.com/es/blog/mejor-hora-para-publicar-en-tiktok) | España | CET | Horas por día (p.ej. mié 13–14, vie 19 y 21). |
| [Adobe – YouTube Shorts](https://www.adobe.com/express/learn/blog/best-times-to-post-youtube-shorts) | General Shorts | local | 24k Shorts: martes y 4 p.m. mejores; sáb 4 p.m. mejor combo; fuera de pico rinde más. |
| [Adobe – encuesta Shorts](https://www.adobe.com/express/learn/blog/youtube-shorts-length-study) | General Shorts | local | Sábados; 6–8 p.m. entre semana. |
| [Buffer YouTube](https://buffer.com/resources/best-time-to-post-on-youtube/) | General (incl. Shorts) | local | vie 3–4 p.m., jue 6 p.m., mar 2 p.m. |
| [Lenostube](https://www.lenostube.com/en/best-time-to-post-on-youtube-shorts/) | General Shorts | local | 12–2 p.m. (opinión). |

## Hallazgos

- Ciencia/divulgación: solo hay una encuesta (preferencias, no rendimiento) que apunta a tarde y noche; educación (Hootsuite, Sprout, Hashmeta) converge en **16–18 h** y noche 20–22 h.
- Hispano: fuentes MX/Latam son orientativas (sin metodología) pero coinciden en comida (13–15) y noche (19–23).
- General: mediodía local (TokPortal, Kapwing, Later) y tarde 15–18 h (Sprout, Adobe Shorts, Buffer).

## Segmentos sin datos públicos verificables

- Divulgación científica con datos de rendimiento por hora (ni TikTok ni Shorts).
- Divulgación en español específicamente.
- YouTube Shorts por país hispano (MX, Latam, España).
- EE.UU. hispano separado de la audiencia general de EE.UU.

## Ajuste continuo

Estas ventanas son hipótesis iniciales. Se ajustarán **semanalmente** con YouTube Analytics (gráfico "Cuándo está conectada tu audiencia") y con las analíticas de TikTok (actividad de seguidores por hora) cuando se activen, registrando resultados en `data/metricas.db`.

## Historial de decisiones — 2-nov-2026 (superado por la política 23-nov)
Ventanas: 06:30–07:30 / 13:30–15:00 / 16:30–18:00 (CDMX). Lo programado a las 19:00 hasta el 4-nov inclusive se queda; desde el 5-nov no se programa 19:00 (los slots vacíos pasan a reserva). Noche solo a prueba con OK de Mj. TikTok espejo 07:00 / 14:00 / 17:00.


## Reconciliación operativa — 2026-11-26

- `main:data/horarios.json` incluye tres ventanas variables (mañana, mediodía de prueba y tarde) y el dato del día fijo 23:30.
- `scripts/rotacion.py` usa IDs estables `manana`, `mediodia` y `tarde`, acepta índices históricos 0–2 y recupera la ventana desde `slot`/`hora_local`/`publishAt_utc` cuando falta el campo.
- El slot 23:30 no forma parte del selector variable.
- `scripts/capsula_diaria.py` bloquea el flujo de YouTube/TikTok cuando `--programar` no encuentra ventana; ya no publica inmediatamente como fallback.
- Esta automatización no ejecuta publicaciones ni programa contenido.
