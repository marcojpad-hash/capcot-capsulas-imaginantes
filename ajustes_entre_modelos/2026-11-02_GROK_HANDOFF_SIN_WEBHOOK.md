# Handoff a Grok SIN webhook (2026-11-02)

## Por qué
El workflow `capcot-grok-dispatch.yml` hacía POST a `GROK_WEBHOOK_URL` (Bearer `GROK_WEBHOOK_TOKEN`) con el evento `capcot.package.ready` y exigía `{accepted:true, receipt_id}`. Ese receptor requería un servidor (Firebase Blaze = tarjeta/pago). **Se abandona Firebase.** El aviso ahora vive dentro del repo: gratis, sin cuentas externas.

## Flujo nuevo
1. **ChatGPT** redacta paquete → `proyectos/` / borrador.
2. **Auditor** hace QA narrativo + validador estructural; solo con PASS promueve el JSON a `cola/entrada/<id>.json` y hace push a `feature/capcot-video-discovery-continuity`.
3. **GitHub Actions** (`capcot-grok-dispatch.yml`) valida el JSON y escribe/commitea `handoffs/grok_inbox/<id>.json` (commit `[skip ci]`) con: `event, status:"pending", receipt_id (repo-<id>-<sha12>), created_at, project_id, branch, commit_sha, package_path, package_url`. El `receipt_id` es el acuse.
4. **Grok app / Imaginantes** revisa `handoffs/grok_inbox/` al iniciar sesión (o cuando Mj le diga "revisa el buzón"): toma cada marcador `pending`, lee el paquete, genera frames/montaje.
5. Al terminar, Grok mueve el marcador a `handoffs/grok_done/<id>.json` con `status:"done"` y su archivo de estado habitual.

## Webhook
Queda **opcional**: si algún día existen los secretos `GROK_WEBHOOK_URL`/`GROK_WEBHOOK_TOKEN` (p. ej. Cloudflare Worker gratis), el workflow además hace el POST con acuse. Sin secretos, no falla.

## Probar
- Actions → "CAPCOT — entrega automática a Imaginantes" → Run workflow (rama feature, `project_id` = un ID existente en `cola/entrada/` o `all`). Debe aparecer un commit `handoff: paquete listo para Grok` con el marcador.
- No toca frames, publicación ni contenido de cápsulas.

## Firebase
Proyecto `capcot-webhook-261102` y código `/workspace/capcot-grok-webhook` quedan sin usar (plan Spark, sin costo). Borrarlo es opcional y solo con confirmación de Mj.
