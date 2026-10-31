# Plan de integración de métricas CAPCOT

Fecha: 2026-10-31  
Rama: feature/capcot-video-discovery-continuity  
Estado: especificación ejecutable pendiente de implementación y autorización OAuth.

## Diagnóstico confirmado

La recopilación privada aún no está implementada. `scripts/metricas.py recolectar` solo comprueba la presencia de `CAPCOT_YT_TOKEN` y `CAPCOT_TIKTOK_ACCESS_TOKEN`, y después imprime un TODO. No consulta YouTube Analytics ni TikTok. Tampoco existen adaptadores Meta en el flujo inspeccionado. El esquema SQLite actual almacena vistas, retención, likes, comentarios, compartidos, guardados y suscriptores, pero no conserva endpoint, versión API, periodo, timestamp de captura ni respuesta original.

Esto significa que el diseño descrito en el documento de investigación no debe confundirse con una integración operativa.

## Arquitectura objetivo

Separar conectores por plataforma y conservar los datos crudos:

- `scripts/metricas.py`: CLI, orquestación y reportes.
- `scripts/adapters/youtube_analytics.py`: informes privados del canal autorizado.
- `scripts/adapters/tiktok_insights.py`: métricas de cuenta propia cuando el producto/permisos habiliten el endpoint.
- `scripts/adapters/meta_instagram.py`: Instagram profesional propio.
- `scripts/adapters/meta_facebook.py`: Facebook Page propia.
- `scripts/normalizar_metricas.py`: mapeo conservador a esquema común.

No crear una integración monolítica ni compartir tokens entre plataformas.

## Esquema mínimo de captura

Cada fila debe conservar:
`project_id, platform, account_id, media_id, published_at, captured_at, window, metric_name_raw, metric_value, source_endpoint, api_version, status, error_code`.

Reglas:
1. Una captura nueva agrega una fila; no sobrescribe una captura anterior.
2. Métrica no devuelta = NULL/ausente, nunca cero.
3. No convertir reach en views ni views en reach.
4. No sumar orgánico, pagado, reposts o placements que puedan solaparse.
5. Toda cifra debe poder rastrearse al endpoint, versión y hora de captura.
6. No guardar access tokens ni respuestas que contengan datos personales innecesarios.

## Implementación por etapas

### Etapa A — lista sin credenciales
- Migrar SQLite con columnas de trazabilidad y tabla `metricas_raw`.
- Añadir fixtures JSON por plataforma.
- Añadir pruebas para normalización, valores ausentes, duplicados y errores de API.
- Generar reporte por publicación y ventanas de edad equivalentes (24 h contra 24 h, 72 h contra 72 h).
- Mostrar claramente qué plataformas están conectadas y cuáles no.

### Etapa B — YouTube
- Sustituir el TODO actual por llamadas reales de YouTube Analytics API para el canal autenticado.
- Consultar vistas, averageViewPercentage/averageViewDuration, likes, comments, shares y subscribersGained cuando el informe y dimensión sean compatibles.
- Separar YouTube Data API (estadísticas públicas) de YouTube Analytics (datos privados del titular).
- Probar primero una publicación conocida; comparar con YouTube Studio y documentar diferencias de ventana/atribución.

### Etapa C — Meta
- Configurar Meta App y OAuth con autorización del titular.
- Seleccionar un solo flujo de login por adaptador y documentar permisos exactos.
- Descubrir activos accesibles y guardar solo IDs no secretos.
- Consultar una publicación propia de Instagram y una de Facebook Page.
- Obtener las métricas que el endpoint real devuelva en la versión fijada; no codificar nombres retirados como obligatorios.
- Hacer prueba de expiración/renovación y manejo de permisos insuficientes.

### Etapa D — TikTok
- Verificar el producto API y el acceso concedido al proyecto antes de escribir el conector. No asumir que un token por sí solo da acceso a analíticas de rendimiento.
- Implementar solo endpoints documentados y habilitados para la aplicación.

### Etapa E — decisión editorial
- Cruzar tema, línea, sublínea, estilo, gancho, duración, slot y rendimiento.
- Comparar cohortes de edad equivalente y tamaño de muestra visible.
- No recomendar cambios editoriales con una sola publicación o métricas incompletas.
- Entregar a Imaginantes un reporte de rendimiento; no pedirle recopilar manualmente datos ya capturados.

## Pruebas de aceptación

- [ ] El CLI funciona sin credenciales y reporta conectores desconectados sin fallar.
- [ ] Fixtures prueban datos completos, parciales, métricas ausentes y errores.
- [ ] Dos capturas de la misma publicación quedan preservadas con timestamps distintos.
- [ ] No se convierten métricas ni se rellenan ceros falsos.
- [ ] Los reportes comparan ventanas equivalentes.
- [ ] Los tokens no aparecen en logs, archivos, commits ni reportes.
- [ ] YouTube se valida contra Studio.
- [ ] Instagram y Facebook se validan con activos propios autorizados.
- [ ] TikTok se habilita solo tras confirmar endpoint y permisos.
- [ ] Grok recibe resultados agregados y deja de hacer captura manual duplicada.

## Bloqueos externos

La integración Meta requiere OAuth de activos propios y secretos configurados por el titular. La alfa de Trends depende de aprobación de Google; no bloquea la detección por RSS. La cobertura de BigQuery Trends para México debe verificarse antes de incorporarla. No se deben pedir tokens por chat ni incluirlos en GitHub.

## Fuente de estado

La investigación de APIs y sus fuentes se mantiene en `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`. Este plan describe el trabajo de ingeniería que falta; no certifica conectores implementados.
