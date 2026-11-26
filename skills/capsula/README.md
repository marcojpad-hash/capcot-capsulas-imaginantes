# Skill: cápsula — producción de cápsulas Datos y ociosidades

Los archivos canónicos de esta skill viven fuera de esta carpeta y NO se
duplican aquí. Esta carpeta es el apuntador.

## Archivos canónicos

- **Skill JSON (máquina):** `templates/skill_capsula.json` — estaciones,
  formato, montaje, QA (puertas duras), hashtags, semana de producción,
  voces, imágenes públicas. Versión 1.0.0; creada 2026-11-11, última regla
  (hashtags por idioma) 2026-11-25.
- **Checklist de revisión final:** `checklists/revision_final.md` — puerta
  de QA antes de montar/subir.
- **Plantillas de storyboard:** `templates/storyboard.template.json`,
  `templates/storyboard_generico.template.json`,
  `templates/storyboard_vertical.template.json`.
- **Cocina / flujo:** `docs/COCINA_CAPCOT.md`, `docs/FLUJO_DE_PRODUCCION.md`.
- **Línea editorial:** `docs/BIBLIA_LINEA_EDITORIAL.md`.
- **Ganchos y retención:** `docs/ESTRATEGIA_GANCHOS_Y_RETENCION.md`.
- **Borradores viejos de skill (no vigentes):** `docs/SKILL_DRAFT_capsula_diaria.md`.

## Resumen de la skill

Cápsulas de 60–90 s (objetivo 75–90 s, QA 60–95 s), 9:16, 1080×1920,
30 fps. Guion adulto 190–210 palabras de narración (menos de 190 NO PASA
a montaje; excepción Bruno el Búho ~150 palabras). Cierre máx 6 s. Voz
-16 LUFS, música -27 LUFS, ambiente -26 LUFS; mezcla final -14 LUFS.
Hashtags en el idioma del video, 7–8 verificados en YouTube (máx 5 en
TikTok), del campo semántico del video. Cada imagen PD/CC citada por su
biblioteca en licencias.json y en la descripción.

Estaciones: Grok investiga y escribe el guion; Grok Bot (Imaginantes)
monta el MP4 oficial; Pecas coordina, verifica y monta relevos; ChatGPT
audita y escribe guiones; Gemini verifica y genera imagen/video.
Ningún modelo tiene callback: Pecas entra a hablarles directo en su chat.
