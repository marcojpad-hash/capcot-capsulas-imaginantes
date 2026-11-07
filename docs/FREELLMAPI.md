# FreeLLMAPI en CAPCOT — router local de modelos gratis

> Estado 2026-11-07: instalado y verificado en la VM de Pecas.
> Sin claves de proveedor todavía: el router responde, pero no puede
> generar nada hasta que Marco cree las claves gratuitas (ver lista abajo).

## Qué es

[FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi) (MIT) es un
router local que junta los planes gratis de 34 proveedores de IA detrás
de un solo endpoint compatible con OpenAI. Cuando un modelo llega a su
límite, salta solo al siguiente (failover automático). No es un servicio
en la nube: corre en la VM y las peticiones van de la VM directo a cada
proveedor. Las claves de proveedor quedan cifradas (AES-256-GCM) en la
base local y nunca salen de la máquina, salvo hacia el proveedor que
corresponda. El único contacto con los servidores del proyecto es el
catálogo de modelos (feed firmado, verificado con Ed25519, 2 veces/día);
ese feed no ve prompts, respuestas ni claves.

## Dónde corre

- Máquina: VM de Pecas (Marco no tiene computadora; esta es la única).
- Servidor: `http://127.0.0.1:3001` (solo localhost, no expuesto a la red).
- Código: `~/workspace/freellmapi` (clon de `tashfeenahmed/freellmapi`).
- Base de datos: `~/workspace/freellmapi/server/data/freeapi.db`.
- Clave unificada: se consulta en el dashboard, página Keys
  (`http://127.0.0.1:3001`). **Nunca se escribe en este repo.**
- Arrancar: `bash ~/workspace/freellmapi/start-freellmapi.sh`
- Parar: `pkill -f "node dist/index.js"`
- Verificado 2026-11-07: `GET /v1/models` con la clave unificada lista
  289 modelos; `POST /v1/chat/completions` sin claves de proveedor
  responde `no_providers_configured` (esperado: el router funciona,
  faltan las claves).

## Cómo se usa en CAPCOT

`scripts/generar_guion_llm.py` ya trae un proveedor `custom` que acepta
cualquier API compatible con OpenAI. No hizo falta cambiar código: solo
variables de entorno.

```bash
export CAPCOT_LLM_PROVIDER=custom
export CAPCOT_LLM_BASE_URL=http://127.0.0.1:3001/v1
export CAPCOT_LLM_API_KEY="<clave unificada de FreeLLMAPI>"
export CAPCOT_LLM_MODEL=auto
python3 scripts/generar_guion_llm.py --tema "..." -o proyectos/x/storyboard.json
```

Con `model=auto` el router elige el mejor modelo disponible y cambia
solo si se agota la cuota. El script pide `response_format: json_object`;
el router lo pasa al proveedor.

Nada cambia en el resto del flujo: las fuentes que proponga el LLM se
siguen verificando con `validar_storyboard.py --check-doi`; nunca se
aceptan sin verificar. El montaje, QA y publicación siguen siendo de
Imaginantes.

## Claves gratuitas que faltan (las crea Marco, una por proveedor)

Ninguna clave está guardada: no se pueden "generar" desde aquí. Cada
una se crea con su cuenta en la web del proveedor y luego se carga en
el dashboard de FreeLLMAPI (página Keys) o con
`npx freellmapi keys add <proveedor>`. Prioridad para CAPCOT:

1. **Google AI Studio (Gemini)** — https://aistudio.google.com/apikey
   (la que ya usa el proveedor `gemini` por defecto; modelos Flash gratis).
2. **Groq** — https://console.groq.com/keys
   (la que ya usa el proveedor `groq`; llama-3.3-70b gratis, muy rápido).
3. **Mistral** — https://console.mistral.ai/api-keys
   (plan gratis con modelos pequeños; el pool gratis más grande del
   catálogo, ~1B tokens/mes según FreeLLMAPI).
4. **OpenRouter** — https://openrouter.ai/keys
   (da acceso a varios modelos con sufijo `:free`).
5. **Cohere, HuggingFace, NVIDIA NIM, Z.ai, Cloudflare** — opcionales,
   mismo mecanismo; añaden modelos y margen de failover.

Con solo Gemini + Groq ya hay failover real. El resto es margen.

## Advertencias (del propio proyecto y del reel)

- **Uso personal, no producción.** El proyecto lo dice así: los planes
  gratis no son una base estable; si algo se vuelve real, se usa una API
  de pago. Para CAPCOT (borradores de guion) es suficiente.
- **Revisar los términos de cada proveedor.** Una cuenta por proveedor,
  no revender, no compartir el endpoint con terceros. Cada proveedor
  puede cambiar o retirar su plan gratis sin aviso.
- **No pasar datos sensibles por planes gratis.** Los guiones de CAPCOT
  son contenido público en preparación (temas, noticias, fuentes); no
  llevan datos personales, contraseñas ni nada sensible. Si algún día
  llevaran, no irían por este router.
- **Los modelos gratis no son los de frontera.** La calidad varía y
  baja al final del día (UTC) cuando los mejores modelos agotan su cuota
  diaria; se resetea a medianoche UTC. Para guiones, con revisión humana
  y verificación de fuentes después, alcanza.
- **Catálogo gratis con 30 días de retraso.** La versión gratis recibe
  el catálogo mensual; los modelos nuevos tardan ~30 días en aparecer.
  El router en sí es gratis y MIT; lo de pago ($19/año) es solo el
  catálogo en vivo, y no hace falta.

## Si algo falla

- Servidor caído: correr `start-freellmapi.sh`; si el puerto 3001 no
  responde, ver `~/workspace/freellmapi/server.log`.
- `no_providers_configured`: faltan claves de proveedor (ver lista).
- `401 Invalid API key`: la clave unificada cambió o no se exportó;
  tomarla de nuevo del dashboard (página Keys).
- Si un proveedor cambia su plan gratis, el router lo refleja en el
  catálogo y salta al siguiente; no hay que tocar el script.
