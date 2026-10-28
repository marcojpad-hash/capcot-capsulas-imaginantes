# Estado de ejecución — 2026-10-28_mosquito-fruitless-audicion

## Resultado
Paquete candidato preparado con storyboard, ocho frames, fuentes, registro preliminar de licencias y bloques de subtítulos de máximo tres palabras. **No hay MP4, audio final, SRT/ASS temporizado, QA oficial ni publicación.**

## Entorno comprobado
- `test -d /workspace/capcot`: falso; no está disponible el runtime oficial en esta sesión.
- `python3 -c 'import edge_tts'`: `ModuleNotFoundError`; no está instalada la voz obligatoria `edge-tts` para `es-MX-JorgeNeural`.
- `ffmpeg`: presente, pero no basta para producir el audio oficial.
- Ocho imágenes se generaron manualmente con OpenAI ImageGen y se normalizaron a 1080×1920. Esto no cuenta como ejecución del proveedor ni del pipeline oficial.
- La cama elegida es `pizzicato`, 84 BPM, distinta de las camas de los otros proyectos programados hoy (`pulso`, `marimba`, `tambor`, `arpegio`, `circuito_neural`). El archivo musical no se generó; debe producirse mediante `scripts/cama_sonora.py`.
- No se ejecutaron `procesar_cola.py`, `capsula_diaria.py`, `validar_storyboard.py --check-doi` ni `qa_capsula.py`, porque el repositorio no está clonado en el runtime de esta sesión. No se afirma QA oficial.

## Diferencias editoriales del 28-oct
- Tema: el gen `fruitless` y la audición de machos de `Aedes aegypti`; no aparece en `data/temas_del_dia.json` ni en los temas de los slots del `data/horario_2026-10-28.json`.
- Estilo: `claymation`, adecuado para biología/animales; no aparece en los estilos de hoy. El último uso registrado fue 2026-10-24, por lo que no repite los estilos de hoy ni el del día anterior.
- Música: `pizzicato`, permitida por `scripts/rotacion.py`, no registrada entre las camas de hoy.
- **Estructura: UNICIDAD NO RESUELTA.** El esquema oficial solo admite cinco estructuras (`mito_vs_dato`, `pregunta`, `historia`, `comparacion`, `sabias_que`) y todas aparecen en cápsulas del 28-oct, incluida `sabias_que` en `2026-10-28_ddm-parte4-templo-mayor`. Se conserva `sabias_que` para no inventar un sexto valor ni modificar el validador; por tanto, esta candidata no puede cumplir la unicidad formal sin cambiar el esquema o la programación del día.
- **Cupo/estado inconsistente:** `data/rotacion.json` registra cinco proyectos del día y `data/horario_2026-10-28.json` lista seis slots; el procedimiento de `scripts/rotacion.py` fija máximo tres por día (dos propias y una externa). `data/publicaciones.json` no refleja todos los slots de hoy y `data/cola.json` está vacío. El pipeline oficial puede rechazar el paquete. No se forzó el cupo.

## Integridad y alcance
- 8 escenas; 194 palabras narradas; 79 s de escenas + 6 s de cortinilla = 85 s previstos.
- Formato objetivo 9:16, 1080×1920, 30 fps.
- Hay capa `mapa`, capa `grafico` y capa `dato`, todas con fuente.
- `subtitulos_bloques.json` contiene bloques de 1–3 palabras sin timecodes; los timecodes deben salir de WordBoundary del TTS oficial.
- No se añadieron registros a `data/cola.json`, `data/rotacion.json`, `data/publicaciones.json`, `data/temas_del_dia.json` ni `data/estilos_usados.json`. No se tocó motor U6.
