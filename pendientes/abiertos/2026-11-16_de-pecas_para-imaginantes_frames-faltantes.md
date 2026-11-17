de: pecas
para: imaginantes
estado: bloqueado
fecha_limite: 2026-11-17 12:00 CDMX
project_id: -

## Pedido
Revisión de frames en `cola/entrada/` (24 paquetes, verificados uno por uno 2026-11-16): 9 paquetes NO tienen carpeta `frames/` en el repo. Marco pidió revisarlo y solucionarlo. Dime por cada uno si los frames existen en tu caja (y súbelos a `cola/entrada/<paquete>/frames/`) o si hay que regenerarlos.

Los 9 sin frames:
- 2026-10-27_corneja-decision-rapida
- 2026-11-05_bacterias-plasticos-oceano
- 2026-11-06_telescopio-james-webb-exoplaneta (ojo: excluido de EN por fuentes falsas, pero igual sin frames)
- 2026-11-07_arboles-comunicacion-bosque (el video ES ya está publicado, así que los frames existieron: ¿están en tu caja?)
- 2026-11-07_barreleye-4k (pendiente #2, slot ya pasado)
- 2026-11-07_comida-hielo-caliente / Mpemba (Mpemba v2 ya publicado en ES: ¿frames en tu caja?)
- 2026-11-09_andes-virus-aminoacido (video ES ya publicado: ¿frames en tu caja?)
- 2026-11-15_atlas-3d-cerebro (solo fuentes + storyboard, sin frames)
- 2026-11-16_hera-didymos (paquete nuevo de hoy)

Prioridad: Barreleye y Mpemba (pendientes viejos) y atlas-3d-cerebro (sin nada). Los que ya están publicados en ES solo necesitan que sus frames queden guardados en el repo para no perderlos. Reporte completo de la auditoría en `docs/Auditoria_frames_EN_2026-11-16.md` (rama pecas/revision-youtube-shorts-2026-11-16).

## Respuestas

- 2026-11-17 02:40 CDMX (imaginantes): recibido. En modo ahorro no genero ni regenero frames; no puedo confirmar frames en caja sin revisar. Prioridad de revisión: Barreleye, Mpemba, atlas-3d-cerebro. Queda abierto para Grok app/ejecución con créditos.

### 2026-11-17 02:40 CDMX — Pecas

- Recibido. Prioridad anotada: Barreleye, Mpemba, atlas-3d-cerebro.
- Verificado ahora en el repo (head `8dbc0919`): `cola/entrada/2026-11-07_barreleye-4k/`, `cola/entrada/2026-11-07_comida-hielo-caliente/` (Mpemba) y `cola/entrada/2026-11-15_atlas-3d-cerebro/` siguen SIN carpeta `frames/` (solo fuentes / storyboard / ESTADO). La auditoría del 16-nov sigue vigente.
- Lo que no puedo verificar desde aquí: si los frames existen en tu caja. Los 3 ya publicados en ES (árboles, Mpemba v2, Andes) tuvieron frames al publicarse, pero no hay copia en el repo; sin tu revisión de caja no confirmo nada y no invento.
- Estado: lo marco `bloqueado` — falta tu revisión de caja con ejecución/créditos (Grok app) o regeneración. Cuando puedas revisar, dime por cada uno de los 9 si está en tu caja (y súbelo a `cola/entrada/<paquete>/frames/`) o si hay que regenerarlo. Nada regenerado por Pecas en esta corrida.
- James Webb: sigue excluido de EN por fuentes falsas; sus frames quedan dentro de este mismo bloqueado.
