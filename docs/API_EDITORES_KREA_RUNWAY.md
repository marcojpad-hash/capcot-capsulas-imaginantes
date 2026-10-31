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
- El precio visible para Seedance 2.5 no aparece desglosado en la tabla pública consultada; debe verificarse en el panel antes de enviar trabajos. La tabla sí publica Seedance 2.0 desde USD $0.0809/s, pero no se debe asumir que esa tarifa aplica a 2.5.
- El saldo de API es independiente del cómputo de la aplicación Krea.

### Runway Dev — editor de video

**Edición: Aleph 2.0**
- Endpoint: \`POST https://api.dev.runwayml.com/v1/video_to_video\`.
- Modelo: \`aleph2\`.
- Recibe un clip de 2–30 segundos y una instrucción de texto; admite hasta 5 keyframes y cambio/expansión de relación de aspecto.
- Casos documentados: quitar objetos o texto, cambiar fondos, ropa, clima, iluminación o estilo; mantener el resto del plano y su movimiento.
- Conserva el audio original en la edición estándar.
- Precio: 28 créditos por segundo, mínimo 56 créditos por solicitud. Runway Dev publica el crédito a USD $0.01: referencia de USD $0.28 por segundo, sujeto a mínimos y cargos de formato.
- Alternativa de edición: Seedance 2.5 dentro de Runway Dev admite video-to-video `mode: "edit"`; en 720p cuesta 30 créditos/s de salida + 15 créditos/s de video de entrada/referencia (USD $0.45 por segundo combinado), mínimo 80 créditos. Aleph 2.0 es la opción más barata para edición directa con prompt y keyframes.
- Gen-4.5 es generación de video (texto/imagen a video), no el modelo de edición de un video existente.

**Imagen: Bria FIBO Edit 1.5 dentro de Runway Dev**
- Endpoint: `POST https://api.dev.runwayml.com/v1/text_to_image`.
- Modelo: `bria_fibo_edit_1_5`.
- Edita de 1 a 4 imágenes de referencia con una instrucción de hasta 10,000 caracteres; mantiene el encuadre de la primera imagen si no se envía `ratio`.
- Entrenado únicamente con datos licenciados, según el changelog oficial de Runway.
- Precio: 5 créditos por imagen (USD $0.05 por imagen al precio API publicado).
- Es un modelo de Bria accesible desde Runway Dev, no un modelo propio de Runway.
- Runway Dev también ofrece otros modelos de imagen de terceros; para CAPCOT las rutas directas son Krea 3 o Bria FIBO Edit 1.5.

## Comparación de costo por edición

- Krea 3 a 2K: USD $0.06 por imagen; una referencia añade USD $0.02 si mide hasta 1024×1024 o USD $0.07 si es mayor. Una edición 2K con un frame vertical de referencia de más de 1MP queda alrededor de USD $0.13.
- Bria FIBO Edit 1.5 en Runway Dev: USD $0.05 por imagen (5 créditos); salida de 1MP.
- Runway Aleph 2.0: USD $0.28 por segundo, mínimo 56 créditos por solicitud. Un clip de 10 s ronda USD $2.80; uno de 30 s, USD $8.40. Editar 75–90 s en tres segmentos ronda USD $21–$25.20, antes de posibles mínimos/ajustes.
- Krea Seedance 2.5: la tabla pública consultada no muestra su precio individual. No usar el precio de Seedance 2.0 como sustituto.
- Runway Dev Seedance 2.5 para edición de video: en 720p cobra 30 créditos/s de salida más 15 créditos/s de video de entrada, con mínimo 80 créditos. Para edición con prompt y keyframes, Aleph 2.0 cuesta menos: 28 créditos/s.

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


## Referencias oficiales consultadas
- Krea API reference: https://www.krea.ai/docs/api-reference/introduction
- Krea 3 image edit: https://www.krea.ai/docs/api-reference/krea/krea-3
- Krea Seedance 2.5: https://www.krea.ai/docs/api-reference/video/seedance-25
- Krea API pricing: https://www.krea.ai/app/api/pricing
- Runway Dev API reference: https://docs.dev.runwayml.com/api/
- Runway Dev video editing guide (Aleph 2.0): https://dev.runwayml.com/learn/edit-and-finish-video-api
- Runway Dev model catalog: https://docs.dev.runwayml.com/guides/models/
- Runway Dev pricing: https://docs.dev.runwayml.com/guides/pricing/
- Runway Dev changelog (Bria FIBO Edit 1.5): https://docs.dev.runwayml.com/api-details/api_changelog/
