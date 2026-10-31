# Investigación operativa: Meta Graph API y Google Trends para CAPCOT

Fecha de corte: 2026-10-31  
Rama: `feature/capcot-video-discovery-continuity`  
Estado: investigación inicial documentada; integración técnica sujeta a credenciales y prueba con la cuenta del canal.

## 1. Resultado ejecutivo

**Meta sí ofrece APIs oficiales que pueden descargar métricas propias de Instagram profesional y Facebook Pages/Reels.** Es una ruta útil para que CAPCOT centralice datos de publicaciones y reduzca el trabajo manual de Grok Bot. No es una API abierta para leer analíticas privadas de cualquier cuenta: requiere app, autorización del titular, tokens y permisos. Las métricas disponibles dependen del tipo de cuenta, endpoint, versión y permisos concedidos.

**Google Trends tiene una API oficial, pero continúa en alfa limitada.** No debemos diseñar CAPCOT suponiendo que tendremos acceso. Mientras tanto, el RSS público de tendencias por país ya se utiliza en `scripts/tendencias.py`; sirve para detectar consultas emergentes y sus noticias relacionadas, pero no equivale a la API de interés histórico ni entrega todos los temas científicos relevantes.

**Distribución de trabajo propuesta:**
- ChatGPT: investigación de fuentes, exploración de tendencias, clasificación editorial, brief, guion/storyboard textual, referencias y análisis de métricas.
- Grok Bot: mantener la línea editorial, validar/ajustar la propuesta, generar y editar medios audiovisuales usando sus recursos y las APIs habilitadas, ejecutar QA y gestionar el flujo de publicación conforme a las reglas del repositorio.
- GitHub: memoria operativa compartida, evidencias, matrices, scripts, estado, asignación y decisiones.
- No enviar claves ni tokens por chat ni guardarlos en el repositorio.

## 2. Meta: Instagram Graph API / Instagram Platform

### Qué puede aportar

Para una cuenta profesional (Business o Creator) autorizada por el titular, la API de Instagram permite consultar el perfil, los medios publicados y métricas de rendimiento. La documentación y el workspace oficial de Meta describen lectura de medios, publicación y métricas.

Para Reels, las métricas que deben investigarse y probarse en la versión vigente incluyen, según elegibilidad del endpoint y versión:
- views y reach;
- likes y comments;
- shares y saved/saves;
- total_interactions;
- tiempo medio de reproducción y tiempo total de reproducción de Reels;
- reposts y métricas agregadas de contenido cruzado, cuando la versión y el tipo de cuenta las expongan.

Meta anunció ampliaciones de métricas de Instagram en 2026, incluidas métricas adicionales de reposts, saves, shares y vistas agregadas en distintos placements. Antes de implementar cada campo hay que comprobar el nombre exacto, endpoint y versión de Graph API. No codificar nombres de métricas a partir de documentación de terceros sin contrastarlas en la referencia vigente.

### Requisitos y límites

1. Cuenta Instagram profesional (Business o Creator); una cuenta personal de consumidor no basta para Insights.
2. Crear una Meta App en Meta for Developers y configurar el producto/login correspondiente.
3. Autorizar la cuenta del canal mediante OAuth; obtener token adecuado y guardar el token como GitHub Actions Secret o en el gestor de secretos del entorno.
4. Seleccionar la ruta de autenticación vigente:
   - Instagram Login, con permisos de Instagram correspondientes; o
   - Facebook Login, que normalmente requiere una Facebook Page vinculada a la cuenta profesional y permisos de Pages/Instagram.
5. Para uso propio, empezar con Standard Access sobre activos que administra el titular. Advanced Access, App Review y verificación empresarial pueden ser necesarios si se pretende que usuarios externos conecten sus cuentas o se excede el acceso estándar.
6. Consultar límites de uso, expiración/renovación de tokens y restricciones de métricas en la documentación vigente. No automatizar interacciones sociales (likes/comentarios) porque no aportan a este proyecto y amplían innecesariamente permisos.

### Facebook Pages y Facebook Reels

La integración de Facebook debe tratarse como una ruta separada, no asumir que el token de Instagram concede automáticamente acceso a métricas de una Page. Para una Page administrada por el titular, revisar Pages API y Page Insights, permisos de lectura de engagement y los endpoints específicos de videos/Reels. Confirmar en la cuenta qué identificadores de publicación y métricas de Reels están disponibles.

### Arquitectura recomendada

Crear adaptadores separados:
- `meta_instagram_insights.py`: medios Instagram/Reels y métricas de cuenta.
- `meta_facebook_insights.py`: Page/video/Reels Insights.
- `normalizar_metricas.py`: convierte las respuestas a un esquema común, conservando el campo original, plataforma, endpoint, versión, timestamp y ventana.
- `metricas.py`: persiste snapshots sin sobrescribir mediciones previas.

Esquema común mínimo:
`platform, account_id, media_id, published_at, captured_at, media_type, views, reach, likes, comments, shares, saves, reposts, avg_watch_time, total_watch_time, follows, source_endpoint, api_version`.

No rellenar métricas no devueltas por la API. Mantener `null` y documentar la causa. Separar orgánico, promocionado y crossposted cuando Meta lo permita; no sumar valores que se solapen.

### Valor para CAPCOT

Con la integración correcta, el trabajo manual de Grok para recopilar métricas de Instagram/Facebook puede reducirse a revisar anomalías y evaluar resultados. Se podrán cruzar por publicación: línea editorial, tema, horario, gancho, plantilla, duración, retención/tiempo de reproducción, compartidos, guardados y seguidores obtenidos.

**Pendiente para activar:** confirmar si @datosyociosidades ya tiene Instagram profesional y una Facebook Page vinculada, y completar el consentimiento OAuth desde Meta. No pedir al usuario que comparta el token en el chat.

## 3. Google Trends: qué existe realmente

### API oficial

La documentación oficial de Google mantiene la Google Trends API en **alfa con acceso limitado por solicitud**. Sus capacidades anunciadas incluyen:
- ventana móvil de aproximadamente cinco años;
- agregaciones diaria, semanal, mensual y anual;
- regiones y subregiones;
- escala consistente entre solicitudes, útil para comparar docenas de términos y series.

La API no devuelve volumen absoluto de búsquedas: el índice representa interés relativo. No hay que tratarlo como conteo de personas ni como prueba de interés por audiencia de YouTube.

Acción: presentar una solicitud de acceso alfa describiendo el caso de uso de CAPCOT (editorial científica mexicana, comparación de interés entre categorías y seguimiento temporal). La aprobación no está garantizada; no bloquear la producción mientras esperamos.

### RSS público actual

El script del repositorio ya consulta:
`https://trends.google.com/trending/rss?geo=MX`

El RSS permite obtener consultas emergentes, tráfico aproximado en rangos, fecha y noticias relacionadas. Es una señal diaria y gratuita; no proporciona una serie histórica de interés por término. Puede sufrir cambios o respuestas temporales 429.

Mejora propuesta:
- consultar MX como fuente principal;
- añadir, como señales secundarias, ES y US, sin confundir tendencias de esos países con demanda mexicana;
- almacenar snapshot diario y fecha/hora de consulta;
- deduplicar términos y noticias;
- conservar el tráfico como bucket aproximado, no como cifra exacta;
- clasificar cada tendencia en los géneros CAPCOT y puntuar relevancia científica, novedad, narrabilidad, fuentes primarias, adecuación de audiencia y riesgo editorial;
- unir las señales con RSS de ScienceDaily, Phys.org, NASA, ESA, Nature, EurekAlert, SINC y UNAM Global;
- verificar el estudio original/DOI antes de escribir una afirmación científica.

No usar endpoints internos no documentados de Trends, scrapers que eludan límites ni `pytrends` como dependencia de producción.

## 4. Hallazgo sobre el estado actual del repositorio

- `scripts/tendencias.py` ya ingiere feeds científicos y Google Trends RSS MX. Es una base útil y evita pagar por una API de tendencias para la detección inicial.
- El script no conserva por sí mismo una serie histórica consolidada de snapshots de Trends ni clasifica de forma robusta por las líneas editoriales finales.
- `scripts/metricas.py` tiene esquema para algunas métricas, pero la ruta actual `vistas` guarda vistas, likes y comentarios; la recolección avanzada de Analytics figura como TODO. Por tanto, el diseño de la base supera la recolección realmente implementada.
- La prioridad técnica inmediata es instrumentar Meta Insights y completar la captura de YouTube Analytics, no comprar herramientas de terceros antes de comprobar las APIs nativas.

## 5. Orden de implementación con mínimo coste

1. **Sin credenciales:** mejorar la ingesta RSS, snapshots, clasificación, deduplicación, scoring y reportes; todo con Python estándar y GitHub Actions ligero.
2. **Con autorización del canal:** integrar Instagram Insights para activos propios y probar con una publicación Reel.
3. **Después:** integrar Facebook Page Insights/Reels si la Page y permisos están disponibles.
4. **Paralelo:** solicitar acceso a la API alfa de Google Trends. Mantener RSS mientras tanto.
5. **Datos:** ampliar el recolector de YouTube Analytics para retención, duración media, shares y suscriptores ganados; preservar ventanas 1h/24h/72h/7d cuando la API lo permita.
6. **Informe:** generar ranking por línea, subtema, horario, gancho, plantilla, audiencia y coste. Comparar ventanas equivalentes y reportar n y datos faltantes.

## 6. Coordinación ChatGPT ↔ Grok Bot

Se solicita incorporar a ChatGPT como responsable formal de **investigación, datos y preproducción textual**, y a Grok Bot como responsable de **dirección editorial, producción audiovisual, integración/uso de APIs de generación de medios, QA y publicación**.

Grok debe:
- confirmar la división de responsabilidades y reflejarla en el handoff del repositorio;
- indicar los archivos y contratos JSON que necesita recibir para generar video;
- publicar instrucciones de integración de sus APIs de video en el pipeline compartido, con nombres de secrets y parámetros, nunca sus valores;
- devolver a ChatGPT requisitos de assets, formatos, referencias, duración y estado para que la preproducción entregue paquetes compatibles;
- dejar que ChatGPT mantenga briefs, guiones, fuentes, clasificación y análisis de rendimiento;
- comunicar bloqueos y cambios mediante un archivo de coordinación compacto en GitHub, evitando conversaciones extensas y duplicadas.

No asumir que ChatGPT puede invocar directamente las credenciales o herramientas de Grok. La integración debe realizarse mediante contratos de archivos, APIs autorizadas y GitHub Actions, con credenciales protegidas.

## 7. Fuentes consultadas

- Google Trends API (documentación oficial): https://developers.google.com/search/apis/trends
- Anuncio oficial de Google Trends API alpha (24-jul-2025): https://developers.google.com/search/blog/2025/07/trends-api
- Tendencias actuales México: https://trends.google.com/trending?geo=MX&hl=es
- Instagram API, workspace oficial de Meta en Postman: https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api
- Instagram Platform / documentación oficial: https://developers.facebook.com/docs/instagram-platform/
- Instagram Insights, referencia oficial: https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-media/insights/
- Facebook Pages API: https://developers.facebook.com/docs/pages-api/
- Page Insights: https://developers.facebook.com/docs/platform/insights/

Nota: las referencias de Meta deben comprobarse contra la versión Graph API configurada al implementar; la lista de métricas y permisos puede cambiar entre versiones.
