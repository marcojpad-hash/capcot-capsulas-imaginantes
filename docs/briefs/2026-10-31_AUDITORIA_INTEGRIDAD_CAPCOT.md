# Auditoría integral CAPCOT — 2026-10-31

## Resumen de estado

La rama de trabajo sigue siendo feature/capcot-video-discovery-continuity. No se tocó main ni se hizo merge. La auditoría encontró inconsistencias reales entre el contrato textual nuevo y el pipeline heredado; se corrigieron documentos, plantilla, validador, rotación, selección de cola y separación entre preproducción y producción.

## Problemas encontrados y correcciones

| Problema | Evidencia | Corrección |
|---|---|---|
| El catálogo Markdown tenía menos estilos que el JSON canónico. | scripts/estilos.json contiene 50 estilos; docs/ESTILOS_VISUALES.md tenía 37. | Regenerado el Markdown desde el JSON: 50 estilos, prompt_base literal por estilo. |
| La plantilla seguía un contrato anterior. | Nombre de serie, voz, duración y campos de assets no coincidían con el brief vigente. | Reemplazada templates/storyboard_vertical.template.json por el esquema textual V2. |
| El validador aceptaba 60–95 s y esperaba asset_filename. | scripts/validar_storyboard.py no comprobaba 170–235 palabras, 7–9 escenas, mapa/dato y voz exacta. | Reescrito para el contrato vigente y para separar storyboard textual de producción. |
| El storyboard diario declaraba archivos inexistentes y privacidad pública. | El JSON de pardelas incluía asset_filename/asset_type y export.filename; publicacion declaraba privacy=public. | Eliminados campos de assets; render_status=NOT_GENERATED; publicación pendiente de Grok. |
| Fuentes duplicadas fuera del JSON. | Existía un archivo _fuentes.md adicional. | Eliminado; todas las fuentes quedan dentro del storyboard autocontenido. |
| La rotación dependía solo de data/*.json, que llega a 28-oct/26-oct. | data/temas_del_dia.json y data/rotacion.json llegaban al 28-oct; data/publicaciones.json al 26-oct. | Nuevo scripts/registro_editorial.py combina data, cola, proyectos y salidas en modo solo lectura; rotacion.py y rotar_estilo.py usan esa vista. No se modificó data/*.json. |
| La cola podía seleccionar el JSON histórico más antiguo. | scripts/procesar_cola.py elegía ent[0] sin filtrar fecha. | Ahora solo selecciona la entrada cuya fecha coincide con --fecha; si no hay entrada del día, se detiene y lista las antiguas. |
| La producción asumía nombres de assets en el storyboard de ChatGPT. | capsula_diaria.py copiaba assets a partir de asset_filename. | Los nombres se asignan en memoria solo al entrar en la etapa de producción de Grok; el JSON de preproducción permanece sin rutas inexistentes. |
| No existía confirmación verificable de recepción por Grok. | La presencia del JSON en cola no prueba lectura ni aceptación. | Nuevo contrato docs/GROK_STATUS_CONTRACT.md y templates/grok_status.template.json. Grok debe escribir cola/estado/; ChatGPT solo lee. |
| README y documentos de operación describían funciones antiguas. | Plan/receta/guía/flujo previos permitían producción integral y generaban expectativas contradictorias. | Versiones anteriores archivadas en docs/obsoleto/2026-10-31/; documentos activos reemplazados y README actualizado. |
| El paquete de arqueas del 30-oct no estaba en la rama de trabajo. | El paquete existía en main, pero no en feature. | Copiados nueve archivos textuales/JSON como evidencia histórica. README del paquete advierte que no es cola actual, no tiene MP4/QA y los assets no están en GitHub. |

## Datos que siguen incompletos

- Los snapshots de data/ siguen desactualizados. La lectura combinada resuelve la detección de repetidos sin alterar los JSON canónicos, pero no reconstruye métricas de publicación que no estén registradas.
- La integración privada de Meta/Instagram/Facebook Insights no está conectada: requiere OAuth y permisos de la cuenta. No se copiaron tokens ni se guardaron secretos.
- YouTube Analytics y TikTok Insights siguen siendo incompletos en scripts/metricas.py; no se afirmó que las métricas privadas estén disponibles.
- Google Trends API alfa sigue siendo una ruta documentada, no una integración autenticada. El flujo RSS/Trending Now se mantiene como ruta de investigación.
- Se sugirió conectar Windsor.ai como conector de analítica orgánica multi-plataforma (Instagram, Facebook, YouTube y TikTok). La sugerencia fue enviada; no está instalado/conectado y no se han importado datos privados.
- La rama feature está divergida de main: 61 commits exclusivos de feature y 9 exclusivos de main al corte. No se sincronizó porque el contrato vigente prohíbe merge y modificación de main.
- Los workflows GitHub Actions que solo existen en feature no tienen cron operativo hasta que el archivo esté en la rama por defecto. La investigación y auditoría diarias se sostienen con las automatizaciones de ChatGPT, no con ese cron.

## Estado de las automatizaciones

- Agente de investigación CAPCOT: activo, 08:00 CDMX; prompt actualizado para entregar exactamente brief + storyboard, sin medios ni archivo de fuentes separado.
- Auditor CAPCOT — cola y rotación: activo, 15:00 CDMX; sustituye la antigua “Tercera cápsula”, que podía duplicar producción y generar medios. Ahora solo audita y corrige defectos mecánicos.
- Operador autónomo general: activo, 07:00 CDMX; prompt actualizado para coordinar repositorios y comprobar estados. La ejecución del 31-oct permanecía en progreso al momento de la auditoría; no se declaró completada.

## Verificación del candidato del 31-oct

El JSON de pardelas fue vuelto a parsear y comprobar estáticamente después de corregirlo:

- 8 escenas.
- 218 palabras de narración.
- 78 s de escenas + 6 s de cortinilla = 84 s.
- Gancho: 6 palabras.
- Los cuatro arcos están presentes y ordenados.
- Cierre hablado exacto.
- 4 fuentes; source_ids enlazan a fuentes existentes.
- Voz declarada edge-tts / es-MX-JorgeNeural / +7% / -2Hz.
- Prompt base coincide con el estilo del catálogo en todas las escenas.
- Capa mapa y capa dato están presentes.
- No quedan asset_filename, asset_type ni export.filename.
- Publicación queda pendiente de decisión de Grok.

No se ejecutó el validador Python ni QA audiovisual oficial en esta auditoría; se añadieron pruebas unitarias para el siguiente entorno de ejecución. La revisión anterior fue estática/estructural, no aceptación de Grok.

## Entregables y límites

- Brief diario: docs/briefs/2026-10-31_RADAR_CAPCOT.md.
- Storyboard: cola/entrada/2026-10-31_pardelas-jetlag-solar.json.
- Registro de esta auditoría: este archivo.
- Fuentes dentro del storyboard; el archivo _fuentes.md se eliminó.
- No se generaron imágenes, frames, audio, voz, video ni renders.
- No se publicó ni programó nada.
- No se modificó data/*.json, main, Motor U6 ni motores canónicos.
- El informe técnico Meta/Trends no se reescribió porque no se verificó un cambio oficial nuevo que justificara actualizarlo.
