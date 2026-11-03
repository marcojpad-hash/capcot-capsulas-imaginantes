# Estrategia de ganchos y retención — CAPCOT (basada en evidencia)

Fecha: 2026-11-02. Fuentes pesadas: análisis de 550+ ads ganadores, estudios de atención (TikTok/Meta), neurociencia de short-form (fMRI Communications Psychology 2026), storytelling científico (ABT/Pixar, Frontiers 2020), frameworks AIDA/PAS validados en práctica publicitaria.

## Reglas duras (evidencia)

1. **Primeros 3 s deciden.** 50% del impacto de un anuncio cae en los primeros 2 s; 90% en los primeros 6 s (TikTok). 65% de quienes ven los 3 s se quedan ≥10 s (Meta).
2. **Ganchos negativos/declarativos ganan.** En 550+ ads ganadores: 91% abren con algo negativo (problema, error, advertencia); 82% con afirmación, no pregunta.
3. **Pattern interrupt + open loop.** Interrupt visual/verbal en 0–0.8 s + señal de identidad + loop abierto (no cerrar hasta el final). Escenas cortas y simples retienen mejor (eye-tracking + computer vision, Journal of the Academy of Marketing Science).
4. **Short-form fragmenta memoria.** fMRI muestra que el formato short-form impide consolidar memoria a largo plazo aunque el espectador quiera aprender. Por eso: un solo dato fuerte, repetido, con cierre claro. No listas.
5. **Storytelling científico.** Videos de ciencia populares usan dramatic question, insight, moments of change y arousal emocional (Frontiers 2020). Estructura ABT (And-But-Therefore) o Pixar Spine funciona mejor que lista de hechos.
6. **Personas en frame.** Mostrar persona en los primeros 2 s sube hooking power ~50% y reconocimiento de ad 32% (TikTok). En CAPCOT: o figura humana en el estilo, o zoom fuerte a objeto clave.

## Estrategia operativa para cápsulas CAPCOT

### 1. Hook (0–3 s) — obligatorio
- Afirmación fuerte o problema (no pregunta de apertura).
- Pattern interrupt visual (objeto inesperado, movimiento, contraste).
- Open loop explícito: “esto no es lo que parece” / “se equivocan en X” / número concreto.
- On-screen text desde el frame 0 (≤6 palabras).
- Ejemplo: “El plástico que tiramos se rompe solo en el fondo del mar. No es bacteria japonesa.”

### 2. Retain (3–60 s) — beats de curiosidad
- ABT interno: contexto (And) → conflicto/dato raro (But) → consecuencia (Therefore).
- Cortes secos cada 2.5–4 s. Un movimiento distinto por plano.
- Un solo número o dato por escena, con source_id.
- Micro-loops: “y aquí viene lo raro…” sin cerrar hasta el final.
- Evitar densidad visual alta (escenas simples ganan en atención sincronizada).

### 3. Reward (cierre)
- Cierra el loop con el dato exacto + fuente.
- Pregunta abierta o reflexión ontológica + firma “Esto fue Datos y ociosidades.”
- Cortinilla de fuentes 6 s.

### 4. Frameworks aplicables (rotar)
- **PAS** (problema-agitación-solución): cuando el tema tiene mito o error común.
- **ABT**: para casi todas. Más rápido y memorable.
- **Hook-Retain-Reward**: estructura de retención obligatoria.
- AIDA solo como checklist interno (Atención en 0-3 s, Interés con el dato raro, Deseo con la consecuencia, Acción = suscripción/firma).

### 5. Checklist de producción (cada cápsula)
- [ ] Hook es afirmación/negativo, no pregunta.
- [ ] On-screen text frame 0.
- [ ] Pattern interrupt visual en primeros 0.8 s.
- [ ] Open loop no se cierra antes del final.
- [ ] Escenas ≤15 s, cortes secos.
- [ ] Un dato fuerte + source_id por afirmación.
- [ ] Estilo visual coherente (no repetir el de la cápsula anterior).
- [ ] Voz JorgeNeural +7% −2 Hz.
- [ ] Cierre con pregunta + firma.

### 6. Métricas a vigilar
- Retención a 3 s (objetivo >65%).
- Retención media (objetivo >40-50% en Shorts/TT).
- Comentarios que citen el dato (señal de que el loop cerró).

## Integración con el repo
- Añadir campo `hook_type` y `open_loop` en storyboard.json.
- QA automático (si existe) debe rechazar hooks que empiecen con pregunta o que no tengan on_screen_text en scene_001.
- Rotación: no repetir estilo ni estructura de las últimas 5.

Fuentes principales: Adside (550+ ads), TikTok/Meta internal, Communications Psychology fMRI 2026, Frontiers in Communication 2020, Journal of the Academy of Marketing Science (attentional synchrony), AnimateYour.Science (ABT/Pixar).
