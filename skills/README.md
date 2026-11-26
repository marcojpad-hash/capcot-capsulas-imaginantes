# Skills CAPCOT — índice

Punto de entrada para los modelos (ChatGPT, Grok/Imaginantes, Pecas, Gemini).
Cada skill vive en su propia subcarpeta, con su README.md.

Los archivos canónicos que ya existían en `templates/`, `checklists/` y `docs/`
NO se duplican aquí: cada subcarpeta apunta a su archivo canónico. Dos copias
de lo mismo se desincronizan; aquí solo hay apuntadores.

## Skills

- `capsula/` — Producción de cápsulas (skill JSON + checklist de revisión final).
- `ganchos-virales/` — Desarmar videos virales y reproducir su estructura
  (ganchos, retención, fórmulas). Incluye herramientas, prompts y flujo.
- `miniaturas/` — Portadas/miniaturas de YouTube.
- `herramientas/` — Matriz de herramientas gratuitas y comparativas.

## Reglas

- Una skill = una subcarpeta, con su README.md.
- No duplicar archivos canónicos: apuntar a su ruta.
- Al añadir una skill, registrarla en este índice con fecha y origen.
- Las skills se leen antes de producir. La orden de usarlas se da en
  `ajustes_entre_modelos/COORDINACION_CHATGPT_IMAGINANTES.md`.
- Nada de lo que dice una skill se da por hecho sin verificarlo en el repo
  o en la fuente que cita.
