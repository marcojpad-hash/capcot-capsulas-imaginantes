# CAPCOT — Arquitectura inicial

Fecha: 2026-10-24  
Estado: diseño inicial; no es todavía una cadena de producción probada.

## Objetivo
Crear videos académicos e infografías animadas de 1–3 minutos, priorizando interfaces web gratuitas, sin API de pago, y automatizando localmente todo lo posible desde guion hasta MP4.

## Etapas
1. **Brief:** audiencia, propósito pedagógico, idioma, duración, tono y accesibilidad.
2. **Investigación:** fuentes rastreables para afirmaciones académicas; separar hechos, interpretación e hipótesis.
3. **Guion:** narración por escena y duración aproximada; total de 60–180 segundos.
4. **Storyboard JSON:** ID estable, duración, voz, texto en pantalla, descripción visual, prompt, fuentes, nombre de archivo y estado.
5. **Generación web:** usar Flow o Kling solo si la cuenta permite crear y descargar contenido gratis. Este paso sigue siendo manual desde la interfaz oficial; GitHub no dispara por sí solo una generación.
6. **Voz y subtítulos:** voz grabada o TTS local gratuito; preparar SRT/VTT y revisar pronunciación.
7. **Montaje local:** FFmpeg para unir clips, ajustar formato, mezclar voz/música con licencia compatible, subtitular y exportar MP4.
8. **Control de calidad:** reproducir el video completo, comprobar sincronía, legibilidad, audio, fuentes, licencias y marcas de agua.
9. **Registro:** anotar herramientas, fecha, límites, fuentes y hashes de los archivos finales.

## Componentes
- Markdown y JSON para brief, guion, storyboard y registro.
- Python estándar para validar manifiestos y automatizar tareas locales.
- FFmpeg local para ensamblar y exportar video.
- Generadores web gratuitos como adaptadores sustituibles, sujetos a cuenta, región, créditos y condiciones.
- GitHub privado para código, prompts, plantillas y registros.

## Límites
- Sin API de pago, claves secretas ni automatización que eluda colas, controles o límites de proveedores.
- No asumir acceso gratuito permanente, uso comercial permitido o exportación sin marca de agua.
- Los videos finales y medios pesados se guardan localmente o en almacenamiento apropiado; no se suben automáticamente a GitHub.
- GitHub Actions se reserva para validaciones ligeras, no para renderizado pesado.
- Este repositorio es independiente del motor U6; no modificarlo desde CAPCOT.

## Criterio del primer prototipo
Dado un storyboard de 60–180 segundos y medios descargados manualmente, validar escenas y preparar el montaje local. El render automatizado solo se considera probado cuando exista un script, se ejecute y se revise un MP4 real.