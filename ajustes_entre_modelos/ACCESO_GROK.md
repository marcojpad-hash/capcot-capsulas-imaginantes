# Acceso de Grok (app principal) al repo y al pipeline

> 31-oct-2026. Lee primero `COORDINACION_CHATGPT_IMAGINANTES.md`. Contexto completo: `salidas/_ops/2026-10-28_HANDOFF_TOTAL_grok_principal.md`.

## Pasos para Mj
1. **Repo (privado):** https://github.com/marcojpad-hash/capcot-capsulas-imaginantes
   - En la app Grok, conectar GitHub (cuenta `marcojpad-hash`) y autorizar este repo; o
   - si no hay conector, pegar en Grok este archivo + `COORDINACION_CHATGPT_IMAGINANTES.md` + el HANDOFF_TOTAL.
   - Alternativa: invitar como colaborador a la cuenta GitHub que use Grok (Settings → Collaborators).
2. **Máquina con terminal** (la app Grok sola no tiene shell persistente):
```bash
git clone https://github.com/marcojpad-hash/capcot-capsulas-imaginantes.git && cd capcot-capsulas-imaginantes
sudo apt install ffmpeg fonts-dejavu-core   # macOS: brew install ffmpeg + DejaVu; ajustar FONT/FONT_R en scripts/montar_capsula.py
pip install edge-tts pillow numpy matplotlib requests google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
edge-tts --voice es-MX-JorgeNeural --text "prueba" --write-media /tmp/t.mp3
python3 scripts/montar_capsula.py proyectos/2026-10-24_abejas-bullying/storyboard.json -o /tmp/prueba.mp4
```
3. **Token YouTube:** existe en el box de Imaginantes en `~/.capcot/token.json`. **NUNCA en el repo.**
   - Mj lo pasa por canal privado, o reautoriza OAuth con su `client_secret.json` (`~/.capcot/auth.py` tiene rutas `/home/box/...` fijas: cambiarlas a tu home).
   - Ruta alterna: `CAPCOT_YT_TOKEN=/ruta/token.json`.
   - Verificar: `python3 scripts/publicar.py --verificar-yt` → `OK`, canal `UCU2ZI-6pBJEr9aSFsF6bxLw`.
4. **Variables si Grok produce guion/frames** (ver COORDINACION §5):
   `CAPCOT_LLM_PROVIDER` + `GEMINI_API_KEY`/`GROQ_API_KEY`/`CAPCOT_LLM_*`; `CAPCOT_IMAGE_API_KEY`, `CAPCOT_IMAGE_MODEL`, `CAPCOT_IMAGE_BASE_URL` (`--proveedor xai` usa `https://api.x.ai/v1`).

## Qué hace Grok
| Situación | SÍ | Deja a Imaginantes |
|---|---|---|
| Sin máquina (solo app + GitHub) | Paquetes en `cola/entrada/<id>/` igual que ChatGPT | Montaje, QA, programación, publicación, `data/*.json` |
| Con máquina + token | Montar (JorgeNeural) + QA + programar | Avisar antes en `salidas/_ops/` qué slot toma; `git pull --rebase` antes de cada cambio; nunca publicar algo que ya está en `data/publicaciones.json` |

Mientras Imaginantes tenga créditos, **la publicación la hace Imaginantes**; Grok produce o apoya.
