# PARA GROK (grok.com) / ChatGPT — variar plantillas y personajes (Mj, 8-nov)

**Quién:** el armado y el código lo hace Grok en grok.com o ChatGPT trabajando en este repo, para no gastar créditos del bot Imaginantes. Imaginantes solo monta con `scripts/montar_capsula.py` (ffmpeg local, sin costo) y reprograma.

## Problema (Mj)
Las escenas de los montajes salen todas con la **misma plantilla visual** y casi siempre con un **personaje femenino**. Ya existen **53 estilos** en `scripts/estilos.json`, además de `docs/ESTILOS_VISUALES.md` y `docs/PROPUESTAS_PLANTILLAS_VISUALES.md`. La rotación (`scripts/rotar_estilo.py` y `scripts/rotacion.py`) no se está reflejando en las escenas generadas.

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

## Agregado 8-nov 23:30 (Mj): deriva visual confirmada + TIPS

- Confirmado con fotogramas: desde Venus (7-nov) TODAS las cápsulas (Venus, palomitas, pan, clavo, ranas) usan la misma ilustración cálida y la misma muchacha de lentes. Del 1 al 4-nov había estilos distintos (crayón/tiburón, collage de papel/pan duro, bordado/miel). Volver a esa variedad: un estilo de scripts/estilos.json distinto por cápsula, y no siempre con personaje humano.
- TIPS: Mj lleva tiempo pidiendo cápsulas de tips prácticos (solo salió la de capsaicina). Formato fijo: al menos 2 tips por semana (cocina/casa/salud cotidiana), mismo molde: portada, gancho, ¿y a mí qué?, tip accionable, cierre. Entregar en cola/entrada/2026-11-08_tip-<tema>/ para la semana 9–14 (slots que no estén publicados).
- Estrategia: el canal se estanca cuando no hay estreno diario; temas de cocina «qué pasa por dentro de…» son los que hoy jalan.

## Causa raíz encontrada (9-nov 01:15)
Todos los storyboard.json desde el 7-nov traen el MISMO prompt_base: "Warm gouache editorial illustration, teal gold cream palette, textured paper, original recurring scientist, full bleed no text". Eso fija paleta (teal/dorado/crema), técnica (gouache), el personaje (científica recurrente) y el encuadre. Al rehacer: prompt_base distinto por cápsula tomado de scripts/estilos.json, variar paleta, tipo de toma (plano general, cenital, macro, contrapicado, detalle) y quitar "recurring scientist" salvo cuando el estilo lo pida.

## Ritmo y número de frames (Mj 9-nov 01:18)
Las cápsulas nuevas tienen 7 frames con planos de 2.5 s y punch-ins: se sienten rápidas. Para los storyboards revariados:
- 9 a 10 escenas (frames) en vez de 7, ~8 s cada una.
- En el storyboard poner "export": {"plano_seconds": 5}. Con eso montar_capsula.py usa solo zoom/paneo lentos (sin punch-in): el mismo frame se recorre en 1-2 encuadres pausados.
- Variar el encuadre dentro de cada frame (pedir imágenes con varios puntos de interés) para que el movimiento lento tenga a dónde ir.
Costo: los frames extra salen de Grok/ChatGPT gratis; el montaje es ffmpeg local.

## Duración y cierre (Mj 9-nov 01:20)
Las nuevas duran 74–81 s (antes 84–93 s) y el cierre se siente apresurado. Objetivo: 85–90 s, y la última escena (cierre) de al menos 10 s con narración pausada, sin recortar el remate.


## Miniatura = portada (9-nov)
Mj: en toda subida/resubida YT la miniatura DEBE ser el primer frame (título en caja crema/amarilla + subrayado rojo). `scripts/publicar.py` ahora extrae ~0.5s y llama `thumbnails.set` tras el insert. Skill: entrega-de-cápsula-con-portada. Sin esto la entrega no está lista.
