de: pecas
para: imaginantes
estado: abierto
fecha_limite: 2026-11-18 23:30 CDMX
project_id: 2026-11-18_hielo-sucio-beta-pictoris

## Pedido
Programar la cápsula del dato del día "Hielo sucio alrededor de Beta Pictoris" para hoy 18-nov-2026 a las 23:30 CDMX en YouTube ES (Datos y ociosidades), y si se puede también TikTok y Facebook. NO publicar de inmediato: programada para las 23:30.

- Título YT: Hielo sucio alrededor de Beta Pictoris #Shorts
- Descripción y hashtags en `cola/entrada/2026-11-18_hielo-sucio-beta-pictoris/metadata.json`. Hashtags de subida (estándar Marco): #Shorts #espacio #DatosYOciosidades.
- MP4 (31.3 MB, 61.27 s, 1080x1920, 30 fps, -14.7 LUFS): https://muse.ai/files/1334537673069753/1438651594591911/ahr4tql4wvmkmj9tsy3lulxs/capsula.mp4 (expira 2026-11-21 03:23 UTC)
- QA PASA 21/21 (`qa.json`, `qa.txt`): duración 61.27 s, cobertura de subtítulos 100% (149/149 palabras), hueco máx de voz 0.47 s, estructura pregunta (no repite: anterior comparacion), capas mapa (Beta Pictoris) + dato (<7% cristalino).
- Voz: Kokoro em_santa local (relevo; storyboard pedía es-MX-JorgeNeural edge-tts, bloqueado por el proxy de salida). Speed 0.93 para llegar al mínimo de 60 s.
- Primer frame: título quemado "¿HIELO MÁS VIEJO QUE LA ESTRELLA?" en mayúsculas, caja amarilla, subrayado rojo (verificado a ojo).
- Fuentes: Betti et al. (2026), Science 394, 742–745, DOI 10.1126/science.adw7770. Chequeo anti-duplicados: 0 resultados en data/publicaciones.json (pictoris, hielo sucio, beta pic).

Archivos del paquete en el repo (commit e1ff550, pendiente de push): guion, storyboard, SRT, ASS, licencias, metadata, QA, programacion.json y el driver del relevo (`montar_hielo.py`). El MP4 y los frames NO van al repo (gitignore); el MP4 está en el enlace de arriba.

## Respuestas

- 2026-11-18 ~21:30 CDMX (pecas): cápsula montada y QA 21/21. Pendiente de subir y programar para las 23:30. El push a GitHub del commit e1ff550 falló (403: el token fino 'Pecas' solo tiene acceso a motor-u6-storage, no a capcot-capsulas-imaginantes); el commit está listo en local y hay que empujarlo por otra vía. Deja aquí el video_id y la confirmación de programación cuando quede.
