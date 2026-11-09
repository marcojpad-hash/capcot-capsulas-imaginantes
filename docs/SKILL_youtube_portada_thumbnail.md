# Skill — YouTube miniatura = portada con título

Fuente: Mj 9-nov (y reafirmado desde 26-oct / 31-oct / 7-nov). Skill bot: `entrega-de-cápsula-con-portada`.

## Regla
Tras cada `videos.insert` (o resubida), fijar miniatura custom con el frame de portada (~0.5 s del mp4): título en caja crema/amarilla + subrayado rojo. Sin esto el feed no muestra el título.

## Pipeline
`scripts/publicar.py` con `--ejecutar`:
1. `videos.insert`
2. `extraer_portada(mp4)` → `portada_thumb.jpg` (1080×1920)
3. `thumbnails().set(videoId, jpg)`

Canal: `UCU2ZI-6pBJEr9aSFsF6bxLw`. Token: `~/.capcot/token.json`.
