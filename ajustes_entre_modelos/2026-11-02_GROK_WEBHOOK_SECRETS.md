# Brief: secretos GROK_WEBHOOK_* (2-nov-2026, 18:30 CDMX)

Estado: el repo NO tiene ningún secret de Actions (`gh secret list` vacío). No hay URL de receptor documentada en el repo, docs ni entorno. No se inventó ningún valor.

## Qué exige `.github/workflows/capcot-grok-dispatch.yml`
- `GROK_WEBHOOK_URL`: obligatorio, debe empezar con `https://`.
- `GROK_WEBHOOK_TOKEN`: obligatorio; se envía como `Authorization: Bearer <token>`.
- POST `Content-Type: application/json` con `{event:"capcot.package.ready", project_id, repository, branch, commit_sha, package_path, package_url, storyboard}`.
- Respuesta 2xx con JSON `{"accepted": true, "receipt_id": "..."}`; si no, falla.

## Bloqueo
Ni Grok (app de xAI) ni Grok Bot exponen hoy un endpoint HTTPS público con ese contrato. Hace falta un receptor (p. ej. Cloud Function/Firebase, Cloudflare Worker) que valide el Bearer, guarde el paquete y responda el acuse.

## Paso para Mj
1. Elegir/crear el receptor y obtener su URL HTTPS; generar token: `openssl rand -hex 32`.
2. `gh secret set GROK_WEBHOOK_URL -R marcojpad-hash/capcot-capsulas-imaginantes`
3. `gh secret set GROK_WEBHOOK_TOKEN -R marcojpad-hash/capcot-capsulas-imaginantes`
4. Probar: `gh workflow run capcot-grok-dispatch.yml -R marcojpad-hash/capcot-capsulas-imaginantes --ref feature/capcot-video-discovery-continuity -f project_id=all` y revisar `gh run watch` → `ACK receipt_id=...`.
