# Integración oficial CAPCOT × CapCut × ChatGPT

**Estado:** integración preparada en documentación; autorización del plugin pendiente en la aplicación de escritorio del usuario.  
**Fecha de verificación:** 2026-10-28.  
**Fuente oficial:** https://www.capcut.com/tools/capcut-x-codex

## Decisión técnica

Usar el flujo oficial **CapCut × ChatGPT / Codex** para convertir los paquetes CAPCOT en borradores editables. No tratar `CAPCUT_IMPORT.json`, el CSV ni el SRT como un proyecto nativo: el exportador actual solo crea archivos auxiliares.

La página oficial indica que la conexión se configura desde la aplicación de escritorio de ChatGPT en PC, que el usuario debe instalar y autorizar el plugin mediante el procedimiento oficial, y que el flujo admite material propio y refinamiento conversacional de la línea de tiempo. La disponibilidad depende de la versión, cuenta y región.

## Instalación y autorización (una vez por equipo/cuenta)

1. En una PC, abre la aplicación de escritorio de ChatGPT y crea una tarea nueva.
2. Abre https://www.capcut.com/tools/capcut-x-codex y copia el prompt de instalación mostrado al inicio de la página.
3. En esa tarea, pega el prompt oficial. Este instruye a descargar y leer el archivo de habilidades oficial:
   `https://sf16-sg.tiktokcdn.com/obj/eden-sg/962370eh7nupenuhbo/capcut_codex_plugin/SKILL.md`
4. Sigue ese archivo literalmente para instalar y autorizar la conexión oficial de CapCut. No sustituirlo por un servidor MCP de terceros ni por instrucciones que escriban directamente en el formato interno de borradores.
5. Confirma que la tarea puede crear/abrir un borrador editable de CapCut. Si falla la autorización, registra el error exacto y detente; no simules una conexión activa.

## Procedimiento por cápsula

1. Usa como fuente de verdad el paquete del proyecto: storyboard/manifiesto, imágenes, guion/narración, fuentes y licencias.
2. Adjunta a la tarea los medios reales que falten en el repositorio (por ejemplo, las imágenes que están únicamente en el ZIP). No pedirle al agente que invente o sustituya medios existentes sin autorización.
3. Adjunta `CAPCUT_IMPORT.json`, `CAPCUT_PLAN_MONTAJE.csv` y `CAPCUT_SUBTITULOS.srt` como especificación de apoyo. El manifiesto actual declara explícitamente que no es formato nativo de CapCut.
4. Pide un proyecto **editable** 9:16, 1080×1920, 30 fps; escena por escena según el manifiesto, subtítulos legibles, narración alineada, música por debajo de la voz y cortinilla de fuentes de 6 s.
5. Haz que el agente indique qué acciones realizó y qué archivos generó. No declarar audio, MP4, render, sincronía exacta ni QA como hechos si no existen.
6. Abre el borrador en CapCut y revisa el audio completo, la sincronía de subtítulos, los créditos/fuentes, las licencias y el encuadre. Exporta solo después de esta revisión.
7. Registra en `ESTADO_EJECUCION.md` los resultados ejecutados y las pendientes. No publicar desde este flujo.

## Prompt operativo

Usa el archivo específico de tarea que acompaña a esta guía:

`cola/entrada/2026-10-28_mosquito-fruitless-audicion/CAPCUT_CODEX_PROMPT.md`

## Límites y seguridad

- El kit de exportación existente genera SRT/CSV; no genera un proyecto nativo.
- Los tiempos SRT existentes se estimaron por distribución de palabras. Deben verificarse con la narración real.
- No alterar `data/cola.json`, rotación, publicaciones ni estados editoriales durante una prueba de montaje.
- No publicar, programar ni sobrescribir un proyecto aprobado sin autorización explícita.
- No instalar herramientas no oficiales que modifiquen el formato privado del proyecto como sustituto de la conexión oficial.
- Si el equipo actual solo dispone de Android, la instalación oficial descrita en la página no puede completarse desde esta conversación móvil; debe hacerse desde la app de escritorio de ChatGPT en PC.
