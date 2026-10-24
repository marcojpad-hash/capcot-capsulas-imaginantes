# Matriz inicial de herramientas gratuitas

Consulta: 2026-10-24. Las condiciones cambian; comprobar la cuenta y el panel antes de cada producción. Gratis no significa ilimitado.

| Herramienta | Uso propuesto | Límites observados en fuentes oficiales | Fuente |
|---|---|---|---|
| Google Flow | Generar imágenes y clips cortos | La ayuda describe 50 créditos diarios para usuarios sin suscripción, no acumulables, con costos por generación. Puede bloquear video en horas pico sin suscripción. Otra página de ayuda describe requisitos de suscripción para la experiencia completa. Por eso, el acceso gratuito real depende de cuenta, región y disponibilidad; comprobarlo antes de diseñar el flujo. Puede haber marca de agua visible. | https://support.google.com/flow/answer/16526234 ; https://support.google.com/flow/answer/16353333 |
| Kling AI | Alternativa para clips e imágenes | Créditos promocionales sujetos a interfaz y campañas; no asumir cuota fija. Algunas funciones, como 1080p o quitar marcas de agua, pueden ser exclusivas de pago. | https://kling.ai/ ; https://kling.ai/docs/point-policy |
| CapCut Free | Editor de respaldo | El plan gratuito ofrece herramientas básicas y plantillas; herramientas avanzadas y créditos de IA se asocian a planes de pago. No asumir API gratuita. | https://www.capcut.com/pricing |
| FFmpeg | Montaje y exportación local | Software libre para combinar clips, audio y subtítulos; no genera escenas por IA. Requiere instalación local. | https://ffmpeg.org/ |
| Python | Validación y automatización local | Python estándar sirve para procesar JSON y archivos sin API de pago. | https://www.python.org/ |
| GitHub Actions | Validaciones ligeras | Repositorios privados tienen cuotas de minutos y almacenamiento según el plan. No renderizar video pesado en CI. | https://docs.github.com/en/actions/concepts/billing-and-usage ; https://docs.github.com/en/billing/reference/product-usage-included |

## Orden de prueba
1. Abrir Flow y comprobar saldo, acceso a video, duración y descarga con un clip corto. Si el video está bloqueado, registrar el mensaje; no intentar eludir el límite.
2. Probar Kling y registrar saldo, duración, marca de agua y descarga.
3. Si no hay generación de video gratuita, producir una primera cápsula con imágenes fijas y movimiento local mediante FFmpeg.
4. Usar CapCut Free solo para retoques que sean más sencillos allí que con herramientas locales.

Antes de publicar, revisar términos, derechos de los medios subidos, música, voces, marcas de agua y restricciones comerciales.