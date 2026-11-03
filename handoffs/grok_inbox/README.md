# Buzón Grok (handoff sin webhook)
Cada `<project_id>.json` aquí = paquete de `cola/entrada/` listo para que Grok/Imaginantes genere frames y montaje.
Grok: lee `package_path` en el `commit_sha` indicado, genera, y al terminar mueve el marcador a `handoffs/grok_done/` (con `status: "done"`).
Ver `ajustes_entre_modelos/2026-11-02_GROK_HANDOFF_SIN_WEBHOOK.md`.
