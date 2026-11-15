# RELEVO — Cápsula del mosquito (viral animado de la semana)

- **Paquete:** `cola/entrada/2026-10-28_mosquito-fruitless-audicion/`
- **Título:** El mosquito que escucha (El gen que afina el oído del mosquito macho)
- **Slot:** miércoles 2026-11-18, 13:30 CST (español)
- **Montado por:** Pecas (relevo / viral animado de la semana). Imaginantes NO lo toca.
- **Fecha de montaje:** 2026-11-15 (madrugada, para el slot del 18-nov)
- **Estado:** MONTADO — paquete cerrado (anti-duplicado: no volver a montar)

## Video

- **Archivo:** `capsula.mp4` — 1080x1920, 9:16, 30 fps, h264 + AAC
- **Duración real:** 87.30 s (target del storyboard: 85 s; diferencia +2.30 s, dentro de ±5 s)
- **Estructura:** 8 escenas (81.35 s) + cortinilla de fuentes (6 s)
- **Tamaño:** 23,645,149 bytes (23.6 MB)
- **Ubicación:** el MP4 no cabe en el repo por push_files (binario, 23.6 MB;
  el límite MCP ya falló con un JSON de 8.4 MB). Queda en la VM de Pecas en
  `~/workspace/capcot-entregas/2026-11-18_mosquito/capsula.mp4`.
  La programación en YouTube/TikTok/Facebook la hace el agente principal
  por navegador desde ese archivo.

## Voz y audio

- **Voz:** Kokoro em_santa, speed 0.9, español es-MX. Una sola voz, sin empalmes.
- **Desviación declarada:** la voz asignada por `docs/VOCES_POR_TEMA.md` era
  narradora_es (VoxCPM2, seed 52). VoxCPM2 NO está disponible para narrar:
  el workflow `VoxCPM2 CPU — Muestras de voz` solo genera las líneas de
  muestra del manifiesto (no acepta texto arbitrario) y el modelo (~9.5 GB)
  no cabe en la VM (8 GB RAM, ~685 MB libres). Respaldo autorizado aplicado:
  Kokoro em_santa (voz de relevo de Pecas, aprobada por Marco en Mpemba v2).
- **Velocidad:** 0.9 en vez de 0.85 — con 0.85 el total quedaba en 91.3 s y la
  puerta dura de duración es 85 ± 5 s; con 0.9 queda en 87.3 s.
- **Narración:** texto exacto del `storyboard.json`, 8 escenas, 76.95 s.
  Cierre hablado: "Esto fue Datos y ociosidades."
- **Cama sonora:** viento + pizzicato sintetizados con `scripts/cama_sonora.py`
  (nota: la función oficial `pista_sfx` falla con "viento" porque no está en
  SINTETICOS; se sintetizó directo con `cs.ambiente`/`cs.musica`).
- **Volumen medido:** -14.79 LUFS integrados, pico real -1.38 dBTP
  (objetivo -14 LUFS; desviación -0.79 LU, limitada por el techo de pico;
  el pipeline oficial de una pasada tiene la misma conducta).

## QA (puertas duras) — PASA

- Formato 1080x1920 9:16, 30 fps. Duración 87.30 s vs 85 s target (+2.30 s).
- Voz em_santa: no es voz rechazada (Piper). Sin huecos de silencio ≥ 1 s
  (silencedetect -50 dB: ninguno).
- Estilo `claymation`: en catálogo; distinto al de la cápsula anterior
  (Baffin 17-nov, `art_deco_poster`). Rotación OK.
- Sin texto quemado en los 8 frames (verificados visualmente uno por uno).
  Observación: el `image_prompt` de la escena 6 termina en
  "no numbers or text" en vez de "no text" — misma intención, frame limpio.
- DOI 10.1371/journal.pbio.3004041 resuelve (HTTP 200, PLOS Biology).
  Fuentes reales SRC-001/002/003, sin inventos.
- Subtítulos estilo oficial exacto (DejaVu Sans 72, negrita, Outline 6,
  Shadow 2, MarginL 90, MarginR 170, MarginV 620, blancos, sin recuadro);
  sincronía verificada en 3 muestras (t=2, 14 y 40 s).
- Cortinilla de fuentes 6 s con firma `Datos y ociosidades · @datosyociosidades`
  y aviso "Imágenes generadas con IA. Voz sintética. Música sintetizada."
- Capas informativas: mapa Nagoya (escena 2), gráfico 450/750 Hz (escena 3),
  dato "1/6" (escena 6). Título-gancho con caja amarilla, mayúsculas negras
  y subrayado rojo (línea publicada).

## Archivos de trabajo (VM de Pecas)

- `~/workspace/capcot-entregas/2026-11-18_mosquito/` — capsula.mp4,
  capsula.srt, capsula.ass, storyboard.json, frames/, audio09/ (narración),
  build_mosquito.py (script de montaje, reutiliza `scripts/montar_capsula.py`).
