# Estructura visual de Shorts/TikTok (nicho datos/curiosidades narradas), hallazgos y cambios

Fecha: 2026-10-24. Encargo de Mj: revisar la **estructura** del video, no el estilo de ilustración.

## Fuentes consultadas (web, 2026)
- Grow Creator, "First 3 Seconds Rule: Education Shorts": https://growcreator.pro/blog/education-shorts-first-3-seconds
- Virvid, "The First 3 Seconds: Hook Structures (faceless Shorts 2026)": https://virvid.ai/blog/first-3-seconds-hook-faceless-shorts-2026
- Shino, "How to Make Educational Short Videos (2026 Guide)": https://shino.app/blog/educational-short-videos-guide
- Fluxnote, "Voiceover + B-Roll Shorts 2026": https://fluxnote.io/guides/youtube-shorts-voiceover-broll-format-2026
- Faceless Lab, "How to Make Faceless Educational Videos": https://facelesslab.video/blog/en/faceless-educational-videos

Ojo: son blogs de herramientas y creadores, no estudios con datos abiertos. Hay que tomarlos como consenso del oficio y validarlos con la retención real del canal.

## Hallazgos y cómo estaba CAPCOT (v4)
| Aspecto | Lo que hoy funciona | CAPCOT v4 | Veredicto |
|---|---|---|---|
| Gancho de 0 a 3 s | La primera palabra antes de 0.5 s, texto en pantalla desde el frame 1 y el plano más llamativo al inicio. Nada de logo ni saludo. YouTube mide la caída en los tramos 0–3 s y 3–7 s | La voz arranca en 0.25 s, pero no había texto de gancho en pantalla | Se ajusta |
| Ritmo de cortes | Un plano nuevo cada 2–3 s. Un plano fijo de 5 s o más se siente viejo | Una imagen por escena, de 6 a 18 s, con un solo Ken Burns lento | **Era el problema principal** |
| Texto en pantalla | Subtítulos grandes, de pocas palabras y alto contraste, dentro de la zona segura. La idea clave se fija en pantalla unos segundos | Subtítulos de 3 palabras, pero a 70 px del borde inferior, bajo la interfaz de TikTok. El `on_screen_text` no se mostraba | Se ajusta |
| Movimiento | Un punch-in donde uno señalaría, usado con moderación | Zoom uniforme de 12 % | Se ajusta |
| Transiciones | Corte seco. Los fundidos se sienten viejos y los giros distraen | Corte seco | Se queda igual |
| Cortinilla | Cierre sin despedida larga | Fuentes durante 6 s | Baja a 5 s. Se queda porque las fuentes son obligatorias en el canal |
| Música | Instrumental bajo la voz que sube en las pausas, con ducking | Pad casi inaudible (-40 LUFS), sin pulso | Se ajusta (ver Audio) |

## Cambios en la plantilla base (`scripts/montar_capsula.py`)
1. **Planos de unos 2.5 s** (`export.plano_seconds`). Cada escena se divide en planos con cortes secos. Cada plano usa un movimiento distinto sobre el frame, en este orden: zoom in, paneo a la derecha, punch-in alto, zoom out, paneo a la izquierda, punch-in bajo.
2. **Gancho**: el `on_screen_text` de la escena 1 sale en una tarjeta grande (92 px, fondo ocre) desde el frame 0 y dura los 2 primeros planos. Debe ser la afirmación sorprendente, no el título.
3. **Texto clave por escena**: el `on_screen_text` se muestra en el primer plano de cada escena, en la parte superior (12 % de alto, dentro de la zona segura).
4. **Subtítulos** subidos a `MarginV=560`, fuera del 20 % inferior que tapa la interfaz.
5. **Cortinilla** de 5 s por defecto.

## Audio
- Ambiente **por escena**: campo `scenes[].ambiente` con los valores oceano, puerto, viento, viento_fuerte, lluvia, tormenta, mercado y silencio, combinables con `+`. Las escenas se encadenan con un crossfade de 0.4 s.
- Música con **pulso suave** a 92 BPM: kick suave, hat en corcheas, bajo y pad (progresión Am–F–C–G).
- Niveles: voz a -16 LUFS, música a -27 y ambiente a -30, con ducking por sidechain (ratio 8, release 350 ms). En las pausas y en la cortinilla la música vuelve a subir.
- **Licencia**: todo el audio se sintetiza con numpy en `scripts/cama_sonora.py` y no usa ninguna muestra ni grabación de terceros. Es obra propia del pipeline, así que no hay derechos que verificar; equivale a CC0. No se usó Pixabay, porque su licencia no es CC0. Si algún día se usan archivos externos (`music_asset` o un ambiente en archivo), solo se admite Freesound con CC0 verificado, guardando la URL y la licencia en `audio.music_license`.

## Correcciones v6 (feedback Mj 2026-10-24 11:06)
- **Bug de subtítulos en v5.** El SRT tenía las 215 palabras completas, pero se quemaba con `subtitles=...:force_style=MarginV=560`. Con SRT, libass usa PlayResY=288, así que ese margen sacaba casi todo el texto de cuadro. Ahora se genera un **.ass con PlayRes 1080×1920**: fuente de 72 px, borde 6, base del subtítulo en y=1300 px. Así queda debajo del título y del texto clave (12–35 % del alto) y arriba del 20 % inferior que tapa la interfaz. Siguen siendo bloques de máximo 3 palabras, sincronizados palabra por palabra.
- **QA nuevo** (`qa_capsula.py`): `subs_cobertura_>=99%` compara las palabras del SRT contra el guion completo; `subs_sin_solapes` revisa que no se encimen tiempos; `subs_en_cuadro_zona_segura` revisa PlayResY=1920 y MarginV entre el 20 % y el 55 % del alto.
- **Título-gancho por cápsula**: campo `titulo` del storyboard (máximo unas 6 palabras, una afirmación sorprendente). Se muestra como tarjeta ocre en mayúsculas desde el frame 0, durante los 2 primeros planos. `generar_guion_llm.py` ya lo pide.
- **SFX por plano**: campo `scenes[].sfx`, una lista con un efecto por plano de unos 2.5 s; si hay menos efectos que planos, el último se repite. Usa grabaciones reales de Wikimedia Commons, **solo CC0 o dominio público**, verificadas por API: olas, gaviotas, lluvia, tormenta, truenos, viento, viento_costa, campanas, reloj, pluma y madera. Hay sintéticos para motor, redes, viento_fuerte, oceano y mercado. La lista con autor y licencia está en `scripts/sfx_manifest.json`. `scripts/descargar_sfx.py` baja los audios a `assets/sfx/` (que no se commitea), re-verifica la licencia y escribe las URL en `assets/sfx/LICENCIAS.json`. No se usó Freesound, porque su descarga exige cuenta; Commons tiene CC0/PD descargable sin login.
