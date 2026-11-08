# PARA GROK (grok.com) / ChatGPT — variar plantillas y personajes (Mj, 8-nov)

**Quién:** el armado y el código lo hace Grok en grok.com o ChatGPT trabajando en este repo, para no gastar créditos del bot Imaginantes. Imaginantes solo monta con `scripts/montar_capsula.py` (ffmpeg local, sin costo) y reprograma.

## Problema (Mj)
Las escenas de los montajes salen todas con la **misma plantilla visual** y casi siempre con un **personaje femenino**. Ya existen **50 estilos** en `scripts/estilos.json`, además de `docs/ESTILOS_VISUALES.md` y `docs/PROPUESTAS_PLANTILLAS_VISUALES.md`. La rotación (`scripts/rotar_estilo.py` y `scripts/rotacion.py`) no se está reflejando en las escenas generadas.

## Tareas
1. Encontrar por qué todas las escenas salen con el mismo estilo y personaje. Revisar `estilo_id` en cada `storyboard.json` y los prompts de imagen: si hay un personaje o referencia fija, si `rotar_estilo.py` no se usa, o si el prompt base está fijo en un JSON o template (`templates/storyboard_vertical.template.json`). Documentar la causa exacta.
2. Arreglar la rotación:
   - Cada cápsula de la semana usa un `estilo_id` distinto de `scripts/estilos.json`, sin repetir en 7 días. Registrarlo en `data/rotacion_estilos.json`.
   - Los personajes Imaginantes varían de género y tipo: hombre, mujer, niño o niña, persona mayor y personaje no humano o animal. No más de 2 cápsulas seguidas con personaje del mismo género.
   - Dentro de una cápsula, las escenas o nodos se intercalan: no van dos escenas seguidas con el mismo encuadre o personaje, ni repeticiones pegadas.
3. Reescribir los storyboards de la semana 9–14 nov: ranas `UBFuKBU3cx0`, aguacate `nSS_q2tj2P0`, ballena `wbFrlM2e_YE`, nubes `4Qpl17Ts_vI`, huesos `uEsoscBrfgU` y flamencos `JV8SB2EpPyI`. Cambiar solo el estilo, los personajes y los prompts de imagen, intercalados. El guion y la voz no cambian.

   Dejarlos en `cola/entrada/2026-11-08_revariar-<tema>/` con `storyboard.json`, prompts e imágenes si Grok las genera gratis en grok.com.

## Reglas fijas (no cambiar)
- La voz es **JorgeNeural**.
- Estilo CapCut: imágenes fijas o animación narrada, subtítulos abajo.
- La primera escena es la portada: título grande en caja crema o amarilla con subrayado rojo, sin subtítulo encima.
- Duración de 60 a 90 s. No usar HyperFrames.

## Entrega
Hacer commit en `main` con el mensaje `revariar: <tema>`. Imaginantes revisa `cola/entrada/` todos los días. Monta y reemplaza en YT, TT y FB **solo** las cápsulas que aún no se publican, a la misma hora. No toca videos ya publicados.
