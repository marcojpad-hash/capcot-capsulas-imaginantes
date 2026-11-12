# Voces por tema — Shorts de Datos y ociosidades

Decisión de Marco, 2026-11-11: las tres voces VoxCPM2 probadas NO son para
la novela/drama (la microserie keeps sus locks Grok), son para los Shorts.
Los Shorts se organizan por tema y cada tema lleva su voz. La voz de Grok
es JorgeNeural, la oficial de CAPCOT (confirmado por Marco 2026-11-11).

## Las cuatro voces

| Voz | Origen | Descripción / lock |
|---|---|---|
| JorgeNeural (es-MX) | edge-tts, vía Imaginantes | Voz oficial CAPCOT (+7%, −2 Hz). La que ya suena al canal. |
| narrador_es | VoxCPM2 Voice Design | Hombre, español mexicano cálido, tono curioso y pausado, estilo documental. Seed 51. F0 med 128 Hz (≈ em_santa, −1.0 sem). |
| narradora_es | VoxCPM2 Voice Design | Mujer, español mexicano cálido, tono curioso, voz brillante. Seed 52. F0 med 291 Hz (mucho más aguda que ef_dora, +9.2 sem; como voz propia, no como clon). |
| narrador_en | VoxCPM2 Voice Design | Hombre, inglés americano estándar, tono curioso y pausado, estilo documental. Seed 53. F0 med 122 Hz (≈ am_adam, −0.6 sem). |

Las voces VoxCPM2 se definen por descripción en inglés + seed (descripción +
seed = lock de voz). Manifiesto: `muestras_narradores.json` en el repo
marcojpad-hash/microserie-heredera-voces; se generan con el workflow
`VoxCPM2 CPU — Muestras de voz` (input manifiesto = muestras_narradores.json).
Licencia del modelo: Apache-2.0 (se puede publicar). Muestras medidas en
`voces-voxcp2-narradores/MEDICION.md` (corrida #3, 2026-11-11).

## Mapa voz → tema

| Tema | Voz |
|---|---|
| Historia, historias, biografías | narrador_es |
| Ciencia, física, química, astronomía | JorgeNeural |
| Biología, cocina / datos de cocina, hacks / life hacks, cultura, literatura | narradora_es |
| Canal en inglés (todos los temas) | narrador_en, alternando con Kokoro am_adam |

## Reglas

- La voz la decide el tema de la cápsula, no la fecha ni el orden.
- Si un tema cambia de voz, se cambia aquí y queda registrado; no se
  cambia de voz en el paquete de una cápsula sin actualizar esta tabla.
- La microserie NO usa estas voces: sus locks son las voces Grok
  (ara, luna, ursa, leo, orion) y no se tocan.
- La F0 medida es guía; el oído de Marco decide si una voz sirve.
