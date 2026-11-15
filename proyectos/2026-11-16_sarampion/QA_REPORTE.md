# QA — Dato del día: El sarampión volvió a México después de 30 años

- **Fecha de producción:** 2026-11-15 (para programar lun 16-nov-2026 07:00 CST)
- **Entregable:** `capsula.mp4` — 1080x1920, 9:16, 30 fps, h264 + aac, **94.27 s**, 45.6 MB
- **Voz:** Kokoro ef_dora (narradora_es), speed 0.73 — **133.4 palabras/min** (rango 120–140 para público 65+)
- **Narración medida:** 85.01 s (189 palabras: guion 184 + cierre 5)
- **Estilo:** vitral (del pool de 25 nunca usados; cálido y claro; rompe la familia azul/dorado)
- **Estado:** RELEVO_AMOR

## Puertas duras — resultado: PASA

| Puerta | Esperado | Real | Veredicto |
|---|---|---|---|
| Duración total 60–95 s, ±5 s del target | target 94 s | 94.27 s (Δ 0.27 s) | PASA |
| Resolución / fps | 1080x1920, 30 fps | 1080x1920, 30 fps (ffprobe) | PASA |
| Audio presente, voz no rechazada | Kokoro (no Piper) | Kokoro ef_dora, voz presente en mezcla (media −17.0 dB en escena vs −19.6 dB solo cama en cortinilla) | PASA |
| Sin huecos de silencio | ninguno >1 s | silencedetect −40 dB d=1.0: ninguno; la cama (viento+arpegio) cubre todo el video incl. cortinilla | PASA |
| Sonoridad | −14 LUFS | medido −14.23 LUFS (entrada −14.61) | PASA |
| Estilo distinto al anterior | ≠ ukiyo_e (último registrado) | vitral, nunca usado | PASA |
| Sin texto quemado en los frames | ninguno | 6/6 frames revisados visualmente; la escena 2 se regeneró porque la v1 traía "1996" en numerales de vitral | PASA |
| Dato con fuente | El Economista + INSP | 20,701 casos / 50 muertes (SSA, datos al 12-nov-2026); 1996; 95%→88%; 69%; 2,829 casos 1–4 años; Jalisco 8,272; 89,163 en 1989–1990 | PASA |
| Subtítulos oficiales | DejaVu Sans 72 negrita, blancos, contorno | ASS generado por el pipeline oficial; verificado en 9 cuadros QA (título, rótulos y subtítulos legibles, en sync con la narración) | PASA |
| Cortinilla de fuentes 6 s | presente | presente (q_92s): El Economista + INSP + disclaimer IA | PASA |
| Gancho 9 palabras en 2.5 s | "El sarampión volvió a México después de treinta años" | título en pantalla desde 0 s; subtítulo desde 0.25 s | PASA |
| Sin "¿sabías que?" ni "parte 2" | — | no aparecen | PASA |
| Sin consejo de salud | — | el guion solo da datos, no recomienda nada | PASA |
| Hilación | conectores | así que, pero, y, por eso, porque (en el guion aprobado) | PASA |

## Notas de producción

- **Velocidad de la voz:** a speed 0.9 Kokoro ef_dora daba 177 ppm (demasiado rápido para este público); se bajó a 0.73 → 133.4 ppm. A 0.69 daba 128 ppm pero el video total quedaba en 97.6 s (fuera del rango 60–95); a 0.73 el total es 94.3 s.
- **Escenas:** 6, duraciones de video 15.36 / 21.37 / 11.79 / 13.16 / 17.77 / 8.87 s (voz + 0.25 lead + 0.3 pad cada una) + cortinilla 6 s.
- **Rótulos en pantalla:** cada escena muestra su rótulo solo en el primer plano (~4 s) y luego la imagen sigue con zoompan; es el comportamiento del pipeline oficial (`escena_video`/`_plano`), no un fallo.
- **Subtítulos:** tiempos uniformes por palabra (aproximación del build relevo, igual que mosquito y apagón); verificados en sync en los cuadros QA (17 s, 20 s, 40 s, 50 s, 60 s, 65 s, 80 s).
- **Frames:** 1152x2048, 9:16, generados por escena con el prompt del storyboard; escena 2 regenerada sin numerales.
- **MP4:** 45.6 MB, no cabe por la API de GitHub (límite 413, igual que Mozart/Napoleón); vive solo en la VM. El paquete del repo lleva guion, storyboard, fuentes, scripts de build, srt/ass y este reporte.

## Cuadros QA

`qa_frames/q_01s.jpg` (título + subtítulo), `q_17s.jpg`, `q_20s.jpg`, `q_30s.jpg`, `q_40s.jpg`, `q_50s.jpg`, `q_55s.jpg`, `q_60s.jpg`, `q_65s.jpg`, `q_80s.jpg`, `q_85s.jpg`, `q_92s.jpg` (cortinilla).

## Para subir (YouTube, lun 16-nov 07:00 CST)

- **Título:** El sarampión volvió a México después de 30 años
- **Descripción sugerida:** El sarampión volvió a México después de treinta años. Desde febrero de 2025 se han confirmado más de veinte mil casos y cincuenta muertes, según la Secretaría de Salud. Esto es Datos y ociosidades.
- **Hashtags sugeridos:** #sarampion #mexico #salud #datosyociosidades
- **Archivo:** `~/workspace/capcot-entregas/2026-11-16_sarampion/capsula.mp4`
- **Aviso:** hoy 15-nov YouTube tocó el límite diario de subida con Leidenfrost; verificar que el slot de las 07:00 no choque con ese límite ni con el reintento de Leidenfrost (cron 16-nov 12:35).
