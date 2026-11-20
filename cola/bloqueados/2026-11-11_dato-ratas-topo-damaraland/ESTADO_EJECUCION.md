# Estado de ejecución — 2026-11-11_dato-ratas-topo-damaraland

- **Estado:** `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- **Rama de este borrador:** `feature/capcot-video-discovery-continuity`.
- **Ubicación del borrador:** `cola/bloqueados/2026-11-11_dato-ratas-topo-damaraland/`.
- **QA narrativo independiente de este borrador:** PASS 91/100; siete checks verdaderos; `review_basis=lectura_en_frio_solo_narracion`; `critical_flags=[]`.
- **Importante:** el QA anterior corresponde solo al storyboard bloqueado de `feature`. La narración del storyboard de producción en `main` es distinta; no se transfiere este PASS a esa versión.
- **Handoff:** `RECEPCION_GROK_NO_CONFIRMADA`; `cola/estado/2026-11-11_dato-ratas-topo-damaraland.json` devuelve 404. La producción registrada en `main` no sustituye un acuse Grok.

## Producción preexistente en main

- `cola/entrada/2026-11-11_dato-ratas-topo-damaraland/programacion.json` registra YouTube ID `WcTviUWqbes`, URL de Shorts y programación para `2026-11-12T13:00:00Z` (07:00 CDMX del 12-nov).
- `salidas/2026-11-11_dato-ratas-topo-damaraland/programacion.json` marca `publicado_yt_tt_fb`, registra TikTok `7707137000121404680`, Facebook `122109293493518983` y actualización 12-nov 07:28 CDMX.
- `salidas/.../publicacion.json` registra YouTube `publishedAt=2026-11-12T04:22:18Z` (22:22 CDMX del 11-nov), discrepante con el horario programado de 07:00 CDMX del 12-nov. No se infiere cuál fue la hora efectiva sin reconciliar el historial de plataforma.
- QA audiovisual: 21/21 checks; duración 87.90 s. Esto no sustituye QA narrativo.
- El árbol GitHub contiene frames, subtítulos, portada y JSON de publicación; `capsula.mp4` está referenciado pero no aparece en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- En `feature/cola/entrada/` solo hay frames; el storyboard permanece en `cola/bloqueados/`. No hay paquete JSON seleccionable.
- No redispatchar, no reprogramar y no cancelar publicaciones.

## Límites

No se modificó `main`, `data/*.json`, el paquete publicado, los IDs de plataforma ni los estados Grok.
