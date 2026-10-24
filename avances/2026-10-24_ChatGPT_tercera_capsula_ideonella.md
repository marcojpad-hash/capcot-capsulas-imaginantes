# 2026-10-24 — ChatGPT — tercera cápsula: Ideonella y PET

## Revisión del skill
Se revisó docs/SKILL_DRAFT_capsula_diaria.md y sus documentos operativos. Se corrigieron tres contradicciones documentales:
- README.md afirmaba que el validador y el montador aún no existían.
- docs/FLUJO_EXTERNO.md indicaba 60–120 s, mientras scripts/validar_storyboard.py impone 60–95 s.
- docs/RECETA_CAPSULA.md decía una cápsula diaria, mientras scripts/rotacion.py define 3/día (2 propias + 1 externa). docs/ESTILOS_VISUALES.md ahora remite el cupo a rotacion.py.

## Cápsula producida
- ID: 2026-10-24_ideonella-pet
- Título: La bacteria que come plástico… pero no hace magia
- Tema: Ideonella sakaiensis y degradación enzimática del PET.
- Duración verificada: 87.506 s.
- Formato: 1080×1920, 30 fps, H.264/AAC.
- Audio: -14.5 LUFS.
- Subtítulos: 56 bloques, máximo 3 palabras; cobertura medida 100% (160/160), hueco máximo 0.35 s.
- QA local: 16/16 comprobaciones propias aprobadas.
- Fuentes: 4 referencias científicas con DOI; incluye advertencia sobre límites de los resultados experimentales.
- Estilo: claymation; estructura mito_vs_dato; cama musical sintética pizzicato.

## Límites y estado
- Render creado fuera de /workspace/capcot; no se ejecutó scripts/capsula_diaria.py ni scripts/qa_capsula.py del repositorio.
- TTS: eSpeak es-MX, fallback offline; no es la voz edge-tts es-MX-JorgeNeural exigida por la receta.
- No publicado en YouTube ni TikTok.
- No se modificaron data/publicaciones.json, data/rotacion.json ni data/temas_del_dia.json porque esta no fue una corrida del pipeline oficial.
- Motor U6: no consultado ni modificado.
