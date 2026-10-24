# Flujo de producción CAPCOT

## Estructura de cada proyecto
    proyectos/
      ejemplo-001/
        brief.md
        fuentes.md
        guion.md
        storyboard.json
        prompts/
        medios/          (local; no subir clips pesados por defecto)
        voz/
        subtitulos/
        exportaciones/   (local)
        registro.md

## Estados
BORRADOR → FUENTES_VERIFICADAS → GUION_APROBADO → STORYBOARD_VALIDADO → MEDIOS_GENERADOS → MONTAJE → REVISION → FINAL

Un estado solo cambia cuando se cumple su criterio. Un prompt no equivale a un clip generado; un montaje no es final hasta reproducirlo y revisarlo.

## Procedimiento
1. Crear brief con audiencia, objetivo y duración de 60–180 s.
2. Registrar fuentes, URL, fecha de consulta y afirmación respaldada.
3. Escribir narración y asignar tiempos por escena.
4. Completar la plantilla de storyboard JSON.
5. Validar campos obligatorios y duración total.
6. Generar medios en la interfaz oficial, manualmente; descargar y nombrar scene_001.mp4 o scene_001.png.
7. Preparar narración y subtítulos; comprobar exactitud académica.
8. Ejecutar montaje local con FFmpeg cuando exista el script de ensamblaje.
9. Reproducir el video completo y revisar audio, texto, cortes, licencias y marcas de agua.
10. Registrar herramientas, fecha, créditos consumidos si se muestran, fuentes, archivos y hashes SHA-256.
11. Versionar documentos y código pequeños en GitHub; mantener medios pesados fuera salvo decisión explícita.

## Automatización sin API
Automatizar archivos y operaciones locales. No automatizar clicks, sesiones ni mecanismos de acceso para eludir límites de proveedores. Las funciones oficiales de agente o lote pueden usarse solo conforme a sus condiciones.

## Criterio de publicación
No publicar hasta verificar fuentes, narración/subtítulos, reproducción completa, derechos, condiciones de herramientas y registro de limitaciones.