# Producción semana 23–28 nov 2026 (Grok Bot, 21-nov CDMX)

Carpeta de trabajo en el box: `/workspace/capcot_prod_20261121/` (mp4 finales con portada en `final/`).
Plan completo: `docs/briefs/produccion_2026-11-23_28/plan_semana.json` (captions TT/FB, fuentes, QA).

| Fecha | Hora CDMX | Tema | Título | QA | YT |
|---|---|---|---|---|---|
| lun 23-nov | 07:00 | nudillos | ¿Qué pasa dentro cuando truenas los dedos? | PASS 77.5 s | pendiente subir |
| mar 24-nov | 17:00 | pollo | ¿Lavas el pollo crudo? Mejor no | PASS 76.5 s | pendiente subir |
| mié 25-nov | 07:00 | medusa | Esta medusa vuelve a ser joven | PASS 76.1 s | pendiente subir |
| jue 26-nov | 17:00 | plátano | ¿Sabías que el plátano es una baya y la fresa no? | PASS 77.3 s | pendiente subir |
| vie 27-nov | 07:00 | microondas | ¿El microondas calienta de adentro hacia afuera? | PASS 77.0 s | pendiente subir |
| sáb 28-nov | 17:00 | mareo | ¿Por qué te mareas en el coche? | PASS 79.8 s | pendiente subir |

Reservas evergreen (no se suben): `RESERVA_huevo.mp4` (yema verde, PASS 76.0 s), `RESERVA_tardigrado.mp4` (revivió tras 30 años congelado, PASS 81.2 s).

- Origen: guiones del lote 14-nov que nunca se publicaron (el render falló por TTS edge-tts `NoAudioReceived`). Se revisaron contra el canal (107 videos): ninguno publicado.
- Cambios editoriales: se reescribieron los cierres con tono de encuesta (nudillos, pollo, mareo, huevo) para que abran curiosidad; portadas reconstruidas con título grande (caja crema, negras en mayúsculas, subrayado rojo) = primer frame (2 s).
- Tardígrado: guion nuevo con Tsujimoto 2016 (Cryobiology), Boothby 2017 (Mol Cell), Hashimoto 2016 (Nat Commun); verificados contra los abstracts de PubMed.
- Ventanas: `politica_desde_2026-11-09` (06:30–07:30, 16:30–18:00); se rota 07:00/17:00.
- Radar YT MX 21-nov: cuerpo humano, animales y cocina son las búsquedas «qué pasa dentro»/«sabías que» con más vistas; los más vistos propios de la semana fueron «Hera/DART», «agua que baila en el sartén» y «coral».
- QA automático (`qa21.py`): duración 60–90 s, 1080x1920, audio, primer frame = portada, subtítulos completos (palabras SRT = narración), no abre con «¿Sabías que?», cierre con pregunta, fuentes ≥1.


## Estado final programación (21-nov ~19:21 CDMX)
YT (API, canal UCU2ZI-6pBJEr9aSFsF6bxLw): dom22 Salem 07:00 / Gutenberg 13:30 / Ada 17:00 (previos); lun23 nudillos tmOji99zGPE 07:00; mar24 pollo _YzBY4OfUeo 17:00; mié25 medusa W9g2tPZTpD4 07:00; jue26 plátano -1DRh_qj7Bg 17:00; vie27 microondas nd0rs6iVy8E 07:00; sáb28 mareo fcSNbU809ao 17:00. containsSyntheticMedia=true enviado; la API no lo devuelve al releer; Studio bloqueado por verificación Google → sin verificar.
TikTok @datosyociosidades (selector en CDMX GMT-6 esta sesión, no NY): dom22 RESERVA huevo 13:00 (7710703730752015668); lun–sáb mismos 6 a las mismas horas CDMX; Everyone + etiqueta IA.
Facebook página Datos y ociosidades: mismos 7 Reels mismas horas CDMX, público.
Reserva restante: RESERVA_tardigrado.mp4 (no subida).

