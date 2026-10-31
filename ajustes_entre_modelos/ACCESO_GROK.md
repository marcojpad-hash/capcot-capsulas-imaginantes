# Acceso de Grok al repo y al pipeline (misma cuenta)

> 31-oct-2026. Actualizado: **bot Imaginantes y Grok usan la misma cuenta de Mj** (SuperGrok / GitHub `marcojpad-hash`). Mj no configura Grok a mano: Imaginantes opera con sus cuentas.

Lee primero `COORDINACION_CHATGPT_IMAGINANTES.md`. Contexto: `salidas/_ops/2026-10-28_HANDOFF_TOTAL_grok_principal.md`.

## Quién opera qué
| Quién | Cuenta | Qué hace |
|---|---|---|
| **Imaginantes (Grok Bot)** | Misma cuenta Mj | Montaje, QA, programación, publicación YT+TT+FB, GitHub push, métricas. Ya tiene el box, `gh` como `marcojpad-hash`, y `~/.capcot/` para YouTube. |
| **Grok (app)** | Misma cuenta Mj | Puede leer/escribir el repo privado si GitHub está conectado en esa app. Si no hay shell, deja paquetes como ChatGPT en `cola/entrada/`. |
| **ChatGPT** | Cuenta aparte | Solo paquetes en `cola/entrada/` (storyboard+frames+fuentes). Nunca publica. |

## Repo
https://github.com/marcojpad-hash/capcot-capsulas-imaginantes — privado, dueño `marcojpad-hash`. **No hace falta invitar otra cuenta:** es la misma.

Si Grok (app) no «entra» al repo: en esa app, conectar GitHub con la cuenta `marcojpad-hash` (la de Mj). Imaginantes no puede completar el OAuth de la app Grok desde aquí; lo que sí hace es mantener el repo, los docs y el pipeline listos.

## YouTube (canal Datos y ociosidades)
- Token en el box: `~/.capcot/token.json` (+ `client_secret.json`). **Nunca en el repo.**
- Verificar: `python3 scripts/publicar.py --verificar-yt` → canal `UCU2ZI-6pBJEr9aSFsF6bxLw`.
- Si el token caduca (`invalid_grant`), Imaginantes reautoriza OAuth en el box con la cuenta Google del canal (Mj solo aprueba el consentimiento en pantalla si hace falta).

## Variables de imagen/LLM (opcionales)
Ver COORDINACION §5: `CAPCOT_LLM_PROVIDER` + claves Gemini/Groq; `CAPCOT_IMAGE_API_KEY` para `--proveedor xai|openai`.

## Regla
Mientras Imaginantes tenga créditos, **publica Imaginantes**. Grok/ChatGPT producen paquetes al mismo estándar (RECETA + JorgeNeural en montaje oficial).
