# APIs de edición audiovisual — Krea y Runway

Estado: integración preparada en código; credenciales y pruebas de generación pendientes. Ninguna llamada de generación se ejecuta al importar los clientes o al correr los validadores.

## Resultado de la investigación

### Krea — editor de imágenes y generador/editor de clips

**Imagen: Krea 3**
- Endpoint: \`POST https://api.krea.ai/generate/image/krea/krea-3\`.
- Acepta prompt, resolución 1K/2K/4K, hasta 8 referencias de imagen y regiones delimitadas para dirigir ediciones localizadas.
- Uso previsto: corregir un frame de storyboard, sustituir objetos, retocar composición y crear un keyframe maestro que conserve el estilo.
- Precio publicado: USD $0.03 por imagen 1K y $0.06 por imagen 2K. Cada referencia de hasta 1024×1024 añade USD $0.02; referencias mayores tienen otra tarifa publicada.
- La API se factura por separado de Krea Pro/Max y requiere token y saldo API.

**Video: Seedance 2.5 servido por Krea**
- Endpoint: \`POST https://api.krea.ai/generate/video/bytedance/seedance-2-5\`.
- Clips de 4–30 segundos, 480p/720p/1080p.
- Texto a video, animación de imagen inicial/final y referencias de imagen, video y audio. La documentación admite edición guiada por video de referencia.
- Precio publicado en la página de API: desde USD $0.0809 por segundo; el costo exacto depende del modelo y la configuración.
- El saldo de API es independiente del cómputo de la aplicación Krea.

### Runway Dev — editor de video

**Edición: Aleph 2.0**
- Endpoint: \`POST https://api.dev.runwayml.com/v1/video_to_video\`.
- Modelo: \`aleph2\`.
- Recibe un clip de 2–30 segundos y una instrucción de texto; admite hasta 5 keyframes y cambio/expansión de relación de aspecto.
- Casos documentados: quitar objetos o texto, cambiar fondos, ropa, clima, iluminación o estilo; mantener el resto del plano y su movimiento.
- Conserva el audio original en la edición estándar.
- Precio: 28 créditos por segundo, mínimo 56 créditos por solicitud. Runway Dev publica el crédito a USD $0.01: referencia de USD $0.28 por segundo, sujeto a mínimos y cargos de formato.
- Gen-4.5 es generación de video (texto/imagen a video), no el modelo de edición de un video existente.

**Imagen en Runway Dev**
- La API de Runway Dev reúne modelos de imagen de Runway y terceros. El catálogo incluye generación de imágenes Runway Gen-4 y modelos de edición de otros proveedores (por ejemplo, GPT Image, Seedream e Ideogram Precise).
- Para edición de imagen con referencias/regiones y estilo consistente, la ruta más directa para CAPCOT es Krea 3; Runway Aleph queda como editor de video.

## Decisión recomendada para CAPCOT

| Trabajo | Servicio | Modelo | Uso |
|---|---|---|---|
| Corregir/editar frame maestro | Krea | Krea 3 | Imagen de referencia + instrucción + regiones |
| Mantener el estilo en frames | Krea | Krea 3 | Reutilizar referencias y biblia visual |
| Animar un frame en clip | Krea | Seedance 2.5 | Imagen inicial y prompt de movimiento |
| Editar un clip existente | Runway Dev | Aleph 2.0 | Cambios locales/globales guiados por texto |
| Crear clip desde imagen | Runway Dev o Krea | Gen-4.5 / Seedance 2.5 | Generación por escenas de 4–30 s |

Para una cápsula de 75–90 segundos, no se debe pedir un único clip largo. Se divide por escenas o segmentos de hasta 30 segundos, se mantiene la misma biblia visual y se ensambla con el pipeline CAPCOT. Las generaciones se guardan como recursos intermedios; voz, subtítulos, capas, música, QA y montaje final siguen bajo el pipeline editorial.

## Credenciales y seguridad

Variables de entorno reconocidas por \`scripts/media_api_clients.py\`:
- \`KREA_API_KEY\`
- \`RUNWAYML_API_SECRET\`

No poner claves en el código, storyboard, ZIP, logs, commits ni mensajes. Para GitHub Actions se deben guardar como Repository Secrets con esos nombres. El cliente solo comprueba presencia de credenciales sin imprimirlas.

**Separación de planes:** una suscripción Krea Pro/Max no paga el API. Una suscripción Runway de la aplicación tampoco debe confundirse con el saldo de Runway Dev API. Los créditos del workspace Runway conectado a ChatGPT se consultan por separado y no habilitan automáticamente Runway Dev API.

## Pruebas

- Pruebas estáticas y de estructura: no consumen saldo.
- Pruebas reales de edición/generación: sí son facturables. No se ejecutan automáticamente en CI.
- Cada llamada devuelve un ID de trabajo/tarea; el cliente permite consultar el estado con \`get_job\` o \`get_task\`.
- Antes de habilitar generación automática, hacer una prueba individual de imagen y una de video con límites de costo, revisar los resultados y guardar las versiones de modelo y parámetros.
