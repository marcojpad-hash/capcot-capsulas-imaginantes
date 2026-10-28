# HANDOFF TOTAL CAPCOT → Grok principal (28-oct-2026 CDMX) — DOCUMENTO MAESTRO

## Prioridad Mj 28-oct ~01:50 CDMX

1. **Primero hoy:** producir los slots faltantes: **07:00, 13:30, 14:30, 17:00 y ~23:30**.
2. **Después**, solo con la parrilla cubierta: métricas / `vistas_historico`.
3. **19:00 DdM P4 ya está programado — no tocar.**

**Orden de Mj:** se entrega a **Grok principal (la app Grok, no un Grok Bot)** **TODA** la dinámica de CAPCOT durante ~4 días (mientras se recuperan créditos): **videos (cómo se hacen y armarlos) + criterio editorial + métricas + TODAS las rutinas + programados + publicación YT/TT/FB con la misma parrilla.** Este archivo manda sobre `2026-10-28_handoff_grok_principal.md` (que queda como antecedente).

## ★ Orden Mj 28-oct ~02:00 CDMX — tres cosas resueltas (sin atorarse)

### A. Plantillas y estilos — si Mj no los da, Grok los resuelve
- **Fuentes de estilo (leer en este orden):** `scripts/estilos.json`, `docs/ESTILOS_VISUALES.md`, `docs/PROPUESTAS_PLANTILLAS_VISUALES.md`, `docs/ESTRUCTURA_VISUAL_TRENDS.md`, `salidas/_ops/2026-10-27_plantilla_acuarela_japonesa.md`, `data/tendencias_estilos.json`.
- **No repetir:** consultar `data/estilos_usados.json` y `data/rotacion.json`; no usar el mismo estilo 2 días seguidos ni en dos slots del mismo día. Registrar cada estilo usado al programar.
- **Si Mj no entrega plantilla/estilo:** Grok **no espera ni pregunta**. Investiga (tendencias Shorts/TikTok del día, `docs/` arriba, cápsulas que más rindieron en `data/vistas_historico.json`), elige uno, lo anota en `data/estilos_usados.json` con 1 línea de por qué, y produce. Si falta una herramienta o crédito, usa la alternativa de §3.3 (frames manuales / Canva / otro modelo) — nunca se queda atorado.
- Mj solo se entera si algo es irrecuperable; lo demás se decide y se reporta en el cierre del día.

### B. Entrega diaria: volumen y slots los DECIDE Grok con datos (no cuota fija)
- **Aclaración Mj 28-oct:** «4 o 6 al día» fue un **ejemplo**, NO una cuota. Grok mira qué está pasando y decide cuántas cápsulas y en qué slots.
- Insumos para decidir: `data/vistas_historico.json` (picos, velocidad de vistas por slot/cesta), reporte horario §5.3, balance 6h §5.4, comentarios §5.8, qué estilos/temas funcionaron (`data/estilos_usados.json`).
- Regla práctica: reforzar slots/cestas que suben, recortar o cambiar los que se estancan; no publicar por publicar (mejor menos y buenas que relleno). La parrilla §4 (A 07:00 kids · B 13:30 familia · C 14:30/17:00/19:00 general · D ~23:30 dato del día) es la **base**, ajustable con evidencia.
- Cada cápsula pasa **QA (§3 paso 6) + revisión editorial (§2: fuentes, dato verificable, título legible en miniatura)** antes de programarse.
- **Programadas** en YT (private + publishAt UTC = CDMX + 6 h) y la misma parrilla en TT/FB. Nada sale sin revisión.
- Producir con antelación (rutina madrugada §5.1): al amanecer el día ya debe estar cubierto según el plan que Grok decidió.

### B2. Análisis real del canal — no un autómata
- Grok **analiza** cómo está funcionando el canal, no ejecuta un horario a ciegas. Mínimo en cada balance 6h y cierre del día:
  - Qué videos están en pico y por qué (tema, gancho, estilo, hora).
  - Qué está flojo y qué se cambia (título, miniatura, slot, estilo, tema).
  - Señales de comentarios (§5.8): preguntas, temas pedidos, quejas → nuevas cápsulas.
  - Decisión explícita para el siguiente bloque: volumen, slots, estilos, temas, end screens. Anotar en el cierre (1–3 líneas de «qué aprendimos / qué cambiamos»).
- Ajuste semanal (§5.7) con la misma lógica: mover horarios según dónde rinde.

### B3. Iniciativa — mismo rigor que Imaginantes / Puta 3 bots
- Misma estructura: RECETA, parrilla, pantallas fuerte→flojo, comentarios 5.8, QA, programación.
- **Si se atora** (falta plantilla, estilo, crédito, herramienta, dato, fuente): **investiga y resuelve** (docs/, `scripts/estilos.json`/`data/tendencias_estilos.json`, web, alternativa §3.3). **No espera a Mj indefinidamente.** Decide, documenta el porqué y sigue; a Mj solo lo irrecuperable.

### C. Pantallas finales / promoción: rotar de pico fuerte → flojos
- Como se ha practicado: los videos **en pico** (más vistas recientes según `data/vistas_historico.json`) empujan con end screen / tarjeta a los **flojos**; repartir entre varios flojos, no todos al mismo.
- Rotación horaria (`30 7-23 * * *`, §5.6); estado en `data/endscreens_rotacion.json`. Reevaluar quién es fuerte/flojo con cada reporte de vistas. No tocar Shorts fijados por Mj. Avisar a Mj **solo si cambió**.

## ⚠️ Cesión temporal (orden Mj 28-oct)

- Este traspaso **solo aplica mientras los Grok Bots (Imaginantes + CAPCOT Métricas/Pantallas) no tengan créditos**. Grok principal es dueño de CAPCOT **únicamente hasta que vuelvan los créditos**.
- **Cuando regresen los créditos, los bots retoman el mando** con **el mismo rigor y la misma forma de trabajo**: RECETA, parrilla, métricas (`vistas_historico.json`), comentarios 5.8, rutinas 5.1–5.7, QA y programación igual que hoy.
- **Al devolver el mando, Grok principal deja un estado del día breve** en `data/` (p. ej. `data/estado_devolucion_AAAA-MM-DD.md`): qué se publicó/programó, slots pendientes, último timestamp de `vistas_historico`, pendientes abiertos.

## Roles (vigentes desde hoy — temporales, ver Cesión temporal)

| Quién | Qué hace |
|---|---|
| **Grok principal** | **Dueño de CAPCOT completo**: temas, guiones, frames, montaje, QA, programar/publicar YT+TT+FB, horario diario, métricas (`vistas_historico.json`, balances, cierre), end screens, ajuste semanal. Monta las rutinas 5.1–5.7. |
| **Puta 3 (Grok Bot)** | **Solo motor U6.** No toca CAPCOT. (Grok principal tampoco toca el motor ni Engine/244.) |
| **Imaginantes (Grok Bot)** | Soporte/transición. **Pausa generación y métricas en cuanto Grok principal confirme que ya escribe `data/vistas_historico.json`.** |
| **CAPCOT Métricas / Pantallas** | Sin rutinas duplicadas; se pausan/coordinan igual que Imaginantes. |

> **Cuando confirmes que ya escribes el historial (`vistas_historico.json`), avísale a Imaginantes (vía Mj) para que pause sus rutinas 5.3–5.5 y la generación.** Mensaje sugerido: «Grok principal ya escribe vistas_historico desde <timestamp CDMX>; pausen métricas y generación CAPCOT.»

---

**Repo (privado, compartido con ChatGPT/Claude):**  
https://github.com/marcojpad-hash/capcot-capsulas-imaginantes  

Clone: `git clone https://github.com/marcojpad-hash/capcot-capsulas-imaginantes.git` → trabajar en `main`, siempre `git pull --rebase` antes de commit. **No subas mp4/png/jpg pesados** (están en `.gitignore`); sí versiona storyboards, guiones, json de data/, docs, scripts.

Canal: **Datos y ociosidades** · @datosyociosidades  
- YouTube: `UCU2ZI-6pBJEr9aSFsF6bxLw`  
- TikTok: https://www.tiktok.com/@datosyociosidades  
- Facebook: https://www.facebook.com/datosyociosidades  
**Misma parrilla en las 3** (no sets distintos). Publicar/programar solo con confirmación de Mj salvo permiso explícito ya dado (hoy: programar lo montado; Mj revisa después).

---

## 0. Urgencia (léelo primero)

Hoy **28-oct** en `data/horario_2026-10-28.json` solo está **listo/programado**:

| Hora CDMX | Slot | Estado |
|-----------|------|--------|
| **19:00** | DdM P4 Templo Mayor (`RhiKtLt2UNQ`) | **programado_yt** (publishAt 29-oct 01:00Z = 19:00 CDMX 28) · mp4 en `salidas/2026-10-28_ddm-parte4-templo-mayor/` · falta alinear TT/FB si no están |

**Faltan (hay que producir YA):**

| Hora | Propuesta | Estado |
|------|-----------|--------|
| 07:00 | Kids Titanoboa | borrador_propuesta |
| 13:30 | Familia Voyager disco de oro | borrador_propuesta |
| 14:30 | TBD (ej. monarca/almas) | TBD — **no usar litografía azul-dorado** |
| 17:00 | TBD (ej. pan de muerto) | TBD — estilo litografía **descartada** |
| ~23:30 | Noctámbulos «dato del día» | **no está en el json 28** — hay que **añadir** (descubrimiento reciente ciencia/naturaleza, no evergreen) |

Regla Mj: **cada día todas las cestas + noctámbulos 23:30 programados en YT+TT+FB**. Prioridad producción: cubrir 28, luego 29–31.

Guion listo pendiente OK Mj (no producir sin OK): Machu Picchu fallas/Pisa (`peru-machu-pisa`).

---

## 1. Lectura obligatoria (en este orden)

1. `docs/RECETA_CAPSULA.md` — reglas + JSON storyboard + estilos  
2. `docs/GUIA_MODELO_EXTERNO.md` — si produces sin montar (paquete cola)  
3. `docs/SKILL_DRAFT_capsula_diaria.md` — comandos del pipeline  
4. `docs/BIBLIA_LINEA_EDITORIAL.md` + `docs/PLAN_MAESTRO_AUTOMATICO.md`  
5. `docs/ESTILOS_VISUALES.md` + `scripts/estilos.json`  
6. `docs/HORARIOS_PUBLICACION.md` + `data/horarios.json`  
7. `salidas/_ops/2026-10-26_parrilla_franjas_reporte.md` — cestas A/B/C/D  
8. `data/horario_AAAA-MM-DD.json` del día · `data/temas_del_dia.json` · `data/rotacion.json` · `data/publicaciones.json`  
9. Créditos video gratis: `docs/CREDITOS_GRATIS_VIDEO.md`

---

## 2. Línea editorial (no negociable)

- Temas: **datos sin sociedades** — meteoritos, océanos, animales, inventos, misterios, ciencia/naturaleza («y más»). **No** temas de sociedad.  
- Prioridad: noticia científica ≤7 días con estudio/DOI; Trends secundario; backlog atemporal solo si no hay noticia.  
- Formato: vertical 9:16, 1080×1920, 30 fps, **60–95 s** (ideal 75–90), ~170–235 palabras.  
- Voz: **edge-tts `es-MX-JorgeNeural` rate +7 % (o +8), pitch −2 Hz**, pausas continuas. Sin eSpeak/gTTS.  
- Arco: hook in medias res → desarrollo → cierre historia → reflexión/pregunta + «Esto fue Datos y ociosidades.»  
- Estructuras: rotar `pregunta | historia | mito_vs_dato | comparacion | sabias_que` — **no todos «¿Sabías qué?» seguidos**.  
- Guion: ~80 % voz/ritmo Mj + ~20 % giro humano; títulos que **nombren el objeto**.  
- Estilo visual: **uno por cápsula**, por tema; **no repetir** el de la cápsula anterior. Prohibido: `litografia_azul_dorado`. Plantillas anotadas (aún no en estilos.json hasta frame de prueba): acuarela japonesa, lápiz sucio/sketchbook lo-fi.  
- Fuentes reales; nada inventado. Cortinilla 6 s con fuentes + aviso IA.  
- Cupo duro pipeline: **máx. 3/día** (2 propias + 1 externa cola) vía `rotacion.exigir_cupo` — la parrilla operativa de Mj pide **~5–6 slots/día**; eso se cubre produciendo fuera del cupo automático o forzando con cuidado (`CAPCOT_FORZAR_CUPO=1` solo tema/estilo) y programando a mano. En la práctica Imaginantes produce las cestas del `horario_*.json` aunque sean >3.

---

## 3. Cómo generar un video (pipeline)

### 3.1 Ruta rápida (recomendada)

```bash
cd /workspace/capcot   # o tu clone
git pull --rebase

# 1) Tema
python3 scripts/tendencias.py

# 2) Storyboard (agente escribe JSON a mano siguiendo RECETA, o LLM)
#    CAPCOT_LLM_API_KEY=... python3 scripts/generar_guion_llm.py "<tema>" -o proyectos/<id>/storyboard.json
#    Sin key: escribe proyectos/<fecha>_<slug>/storyboard.json

# 3) Validar fuentes
python3 scripts/validar_storyboard.py proyectos/<id>/storyboard.json --check-doi

# 4) Frames (elige uno)
#    a) API: CAPCOT_IMAGE_API_KEY=... python3 scripts/generar_frames.py <sb> --proveedor xai|openai
#    b) Manual: GenerateImage / Canva / otro → guardar frames/scene_001.jpg … (9:16)
#    c) Placeholder solo para probar montaje: --proveedor placeholder

# 5) Orquestar (montaje + QA + paquete en salidas/)
python3 scripts/capsula_diaria.py --storyboard proyectos/<id>/storyboard.json --proveedor-img manual --fecha AAAA-MM-DD

# Montaje solo:
python3 scripts/montar_capsula.py proyectos/<id>/storyboard.json -o salidas/.../capsula.mp4

# 6) QA (debe pasar)
python3 scripts/qa_capsula.py salidas/.../capsula.mp4 salidas/.../storyboard.json

# 7) Metadatos
python3 scripts/metadata.py salidas/<dir>/

# 8) Publicar YouTube (SOLO con OK / --ejecutar)
python3 scripts/publicar.py salidas/<dir>/ --ejecutar
# Programar: privacy private + publishAt ISO UTC (= hora CDMX + 6 h en invierno fijo CDMX UTC-6)
```

**Dependencias:** python3, ffmpeg/ffprobe, `pip install edge-tts pillow requests` (+ google-api-python-client / oauth para YT).

**Token YouTube:** `~/.capcot/token.json` (OAuth canal Datos y ociosidades). Verificar: `python3 scripts/publicar.py --verificar-yt`.

### 3.2 Paquete desde otro modelo (ChatGPT/Claude)

Dejar en `cola/entrada/<project_id>/`:
- `storyboard.json` + `frames/` + `fuentes.md`  
Luego: `python3 scripts/procesar_cola.py --publicar --programar`  
El modelo externo **nunca publica**. Ver `docs/FLUJO_EXTERNO.md`.

### 3.3 Frames sin créditos del bot

Si se acaban créditos de imagen del asistente:
- Canva / Flow (Veo) / Dreamina / Kling según `docs/CREDITOS_GRATIS_VIDEO.md` (ventana práctica **12:00–17:30 CDMX**).  
- Preferencia CAPCOT actual: **stills 9:16 + Ken Burns** en `montar_capsula.py` (no hace falta video IA por plano).  
- Guardar como `frames/scene_NNN.jpg` con el mismo nombre que `asset_filename` del storyboard.

### 3.4 Salida esperada por cápsula

```
salidas/AAAA-MM-DD_slug/
  storyboard.json, guion.md, fuentes.md, frames/
  capsula.mp4, capsula.srt/.ass, qa.json, metadata.json
  publicacion.json, tiktok.json, facebook.json, LEEME.md
```

Actualizar `data/horario_AAAA-MM-DD.json` (estado, yt_id, publishAt, tiktok/facebook).

---

## 4. Parrilla / cestas (todos los días)

| Franja | Hora típica CDMX | Línea | Notas |
|--------|------------------|-------|-------|
| A | ~07:00 | kids | Dato claro, biología OK |
| B | ~13:30 | familia | |
| C | 14:30 / 17:00 / 19:00 | general | DdM serie si aplica |
| D | **~23:30** | noctámbulos | **dato del día** reciente (ciencia/naturaleza), no evergreen |

Ventanas base (`data/horarios.json`): mediodía 13:30–15, tarde 16:30–18, noche 19–21. Rotar minuto exacto.

**Serie DdM 2026:** P1 papel / Catrina / P2 / P3 Pomuch (27) / **P4 Templo (28 19:00)** — ya en YT programado.

Miniatura YT: usar frame donde se lee el título (no el primer frame confuso).

---

## 5. Rutinas a recrear en Grok principal

Copia el **intent** (no hace falta el texto literal). Zona: `America/Mexico_City`.

### 5.1 CAPCOT generación madrugada
- **Cron:** `30 2 * * *` (flexible ±15)  
- Pull repo → leer `data/horario_HOY.json` + RECETA → cubrir **todas las cestas + 23:30** → producir faltantes (guion→frames→montaje→QA) → dejar listos / programar YT+FB si Mj lo pidió → commit json/docs.  
- Aviso a Mj solo si falla auth o quedan cestas sin cubrir.

### 5.2 CAPCOT publicar TikTok (misma parrilla)
- **Cron:** `0 14,17,19 * * *` (puede ir hasta ~59 min tarde)  
- Subir a TT los **mismos** de la parrilla YT (mp4 + caption + etiqueta IA). Alinear FB si falta.  
- Si bloqueo/captcha: mandar a Mj mp4 + caption. Actualizar `tiktok.json` / horario.  
- Studio TT a veces en GMT-4: convertir horas CDMX.

### 5.3 CAPCOT reporte vistas horario
- **Cron:** `0 7-23 * * *` (±15)  
- YT Data API: Shorts **públicos** (vistas/likes/comentarios) + suscriptores; delta vs última fila.  
- TT si se puede; si no → `tiktok: null` (no inventar).  
- Append `data/vistas_historico.json` → commit+push solo ese json.  
- Mensaje corto a Mj cada hora.

**Formato fila:**
```json
{
  "timestamp_cdmx": "2026-10-27T22:57-06:00",
  "youtube": { "<yt_id>": {"view":0,"like":0,"comment":0} },
  "youtube_totales": {"view":0,"like":0,"comment":0},
  "suscriptores": 0,
  "delta_vs_anterior": {"view":0,"like":0,"comment":0,"suscriptores":0},
  "tiktok": null,
  "nota": "..."
}
```
Último snapshot Imaginantes: **2026-10-27T22:57** → 14,465 vistas · 495 likes · 19 com · 41 subs · TT null. Script apoyo: `scripts/metricas.py vistas` + `publicar.yt_cliente()`.

### 5.4 CAPCOT balance 6h
- **Cron:** `0 8,14,20 * * *`  
- Totales YT/TT, Δ ~6 h, top crecimiento, estancados, lectura de flujo → `data/balances_6h.json` (+ append histórico) → mensaje a Mj siempre (aunque plano).

### 5.5 CAPCOT cierre del día
- **Cron:** `0 23 * * *`  
- Escribe `data/cierre_diario/YYYY-MM-DD.md` + mensaje breve a Mj (ganador del día, qué repetir mañana, empujones).

### 5.6 CAPCOT pantallas finales
- **Cron:** `30 7-23 * * *`  
- Rotar end screens fuerte→flojo (varios flojos, no todos al mismo). Solo avisar a Mj **si cambió**. Estado: `data/endscreens_rotacion.json`. No tocar Shorts fijados por Mj.

### 5.7 CAPCOT ajuste semanal de horarios
- **Cron:** lunes `0 10 * * 1`  
- Revisar Analytics «cuándo conectada la audiencia» y ajustar ventanas.

**Coordinación métricas:** Imaginantes tiene 5.3–5.5 activas. Cuando **tú** confirmes que ya escribes `vistas_historico.json`, Imaginantes las **pausa** (y avisa a CAPCOT Métricas) para no pisar el repo. CAPCOT Métricas no tiene rutina duplicada.

---

### 5.8 CAPCOT revisión de comentarios (YouTube / TikTok / Facebook)

Cada vez que entres a YouTube Studio, TikTok Studio o las herramientas de la Página/creador de Facebook de **Datos y ociosidades**, revisa los comentarios nuevos:

- **Preguntas buenas:** responde breve, en la voz de la marca (curiosa, clara, con humor ligero). Si no sabes el dato con fuente, no respondas con suposiciones: di que lo revisas o déjalo para Mj.
- **Nunca inventes datos** en una respuesta.
- **Spam, odio, acoso o estafas:** no respondas; márcalos para Mj (enlace + captura + plataforma) en el reporte.
- **Cadencia:** aprovecha las mismas ventanas de métricas (7–23 h CDMX) y cada vez que publiques. Fuera de ese horario, no hace falta.
- Anota en el reporte: cuántos comentarios nuevos, cuántos respondidos, cuántos marcados.

## 6. Credenciales / secretos (dónde viven)

| Qué | Dónde |
|-----|--------|
| YouTube OAuth | `~/.capcot/token.json` en el box de Imaginantes |
| Imagen API | `CAPCOT_IMAGE_API_KEY` (+ opcional `CAPCOT_IMAGE_MODEL`) |
| LLM guion | `CAPCOT_LLM_API_KEY` / GEMINI / GROQ |
| TikTok API | `CAPCOT_TIKTOK_ACCESS_TOKEN` (recolectar aún TODO; hoy TT se lee por Studio browser o queda null) |

Sin esas keys en tu entorno: produce storyboard + frames a mano y monta con edge-tts local; publica YT con OAuth del canal.

---

## 7. Standing orders de Mj (resumen operativo)

- Programar lo montado **ya**; revisión después.  
- YT = TT = FB misma parrilla.  
- Cierre noctámbulos 23:30 = dato del día reciente.  
- Reportes vistas cada hora en chat; balance 6 h; cierre nocturno.  
- Pantallas: solo notificar si cambian.  
- Acerca de YT: honesto (meteoritos/océanos/…/y más + links TT/FB); IA en imagen/voz OK si se dice que guion/corte los revisan humanos.  
- Entregas como **adjuntos en chat**, no Drive.  
- Repo privado compartido con otros modelos; no inventar datos; no borrar archivos ajenos.

---

## 8. Checklist día 1 (Grok principal)

1. Acceso git al repo + `git pull --rebase`. Leer la sección 1 en orden.
2. Instalar ffmpeg, `pip install edge-tts pillow requests google-api-python-client google-auth-oauthlib`; probar `montar_capsula.py` con un storyboard existente.
3. Token YT: `~/.capcot/token.json` (OAuth canal Datos y ociosidades) — si no lo tienes, pedirlo a Mj. Verificar `python3 scripts/publicar.py --verificar-yt`.
4. **Hoy 28-oct:** completar cestas 07:00 / 13:30 / 14:30 / 17:00 + **23:30 noctámbulos**; confirmar DdM P4 19:00 también en TT y FB.
5. Crear `data/horario_2026-10-29.json` … `-31.json` con 5–6 cestas + 23:30.
6. Montar rutinas **5.1–5.7** (cron CDMX arriba).
7. Primera fila propia en `data/vistas_historico.json` → **avisar «ya escribo historial» → Imaginantes pausa**.
8. Commits solo data/docs/json (sin mp4/png/jpg).
9. **No tocar** motor U6 / Engine/244 (es de Puta 3).

## 9. Contactos bots (referencia)

- **Puta 3** — motor U6 únicamente.
- **Imaginantes** — ex-productor CAPCOT; pausa al confirmar historial.
- **CAPCOT Métricas** / **CAPCOT Pantallas** — sin duplicar rutinas.

Métricas de apoyo: `scripts/metricas.py` (`vistas [yt_id…]` vía YouTube Data `videos.list`, `reporte`, `metas` hacia YPP 5-dic-2026, `recolectar` con `CAPCOT_YT_TOKEN`/`CAPCOT_TIKTOK_ACCESS_TOKEN`). Horarios: `docs/HORARIOS_PUBLICACION.md` (CDMX UTC-6; ajuste semanal con Analytics).
