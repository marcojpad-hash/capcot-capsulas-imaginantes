# La cocina CAPCOT — organización

Chef ejecutiva: Pecas. Decisión de Marco, 2026-11-11.

La cocina es el área de creación audiovisual de CAPCOT (Datos y
ociosidades), donde esperamos monetizar algún día. Pecas coordina todo
con los demás modelos. No son solo suyos: también se vinculan con la
otra parte (el motor U6). La gestión operativa es la misma para las dos
áreas: bus (repo) + skills + verificación en repo + callback por
navegador.

## Los chefs (modelos) y su estación

| Chef | Estación |
|---|---|
| Grok | Investiga, escribe el guion (storyboard.json), genera frames y clips. Deja el paquete en cola/entrada. Responde callbacks por navegador. |
| Grok Bot (Imaginantes) | Montaje oficial con JorgeNeural + QA + programa/publica. |
| ChatGPT (marcosabines) | Auditor y montador de respaldo (workflow de montaje pendiente de cablear). Escribe scripts, audita, guiones. |
| ChatGPT (marco.jp@live.com.mx) | Segunda cuenta, por sumarse a la ronda de callback. |
| Gemini | Verificación y contexto; imagen/video por la app (Nano Banana, Flow/Veo). |
| Groq | Orquestador (gpt-oss-120b) y agregador. |
| Pecas (chef ejecutiva) | Coordina, verifica todo en el repo, monta relevos con ffmpeg + Kokoro/VoxCPM2, hace los callbacks por navegador, lleva el ledger, reporta solo lo verificado. |

## Skills, no sistema multiagente

Cada estación trabaja con una skill (la receta): capcot-guion,
capcot-frames, capcot-manim, capcot-montaje, capcot-narracion, capcot-qa.
No hay agentes autónomos hablando entre sí: el trabajo pasa por el repo
(bus), cada modelo ejecuta su skill, y Pecas lo verifica y lo mueve a la
siguiente estación. Más funcional que un sistema multiagente: cada skill
es un paso con entrada, salida y puertas de QA.

## Flujo (workflow)

1. Tema → Grok: investigación + storyboard.json + frames → cola/entrada/<id>/.
2. Voz según tema (docs/VOCES_POR_TEMA.md).
3. Montaje: Imaginantes (oficial) / Pecas relevo (ffmpeg) / ChatGPT respaldo (pendiente workflow).
4. QA (capcot-qa, puertas duras) → programa/publica.
5. Pecas verifica en repo; nada se da por entregado sin evidencia en repo. Revisión diaria 08:10.

## Reglas de la cocina

- Nada se da por entregado en chat; solo vale lo verificado en el repo.
- Ningún modelo tiene callback: Pecas entra a hablarles directo en su chat.
- Los locks no se tocan (voces Grok de la microserie; voz oficial JorgeNeural).
- Stock: Grok crea en 3 semanas; Pecas monta 1 viral animado/semana.
- La voz la decide el tema (docs/VOCES_POR_TEMA.md).
