# Coordinación ChatGPT · Imaginantes (Grok Bot) · Grok
**Vigente desde 2026-10-31 · America/Mexico_City**

> **Lectura obligatoria al entrar:** antes de cualquier tarea, lee `ajustes_entre_modelos/README.md`, `docs/CONTRATO_OPERATIVO_UNIFICADO.md` y `ajustes_entre_modelos/BITACORA_COORDINACION.md`. Registra al final de la bitácora cualquier cambio de coordinación o archivo compartido. La bitácora es append-only.


Este archivo es el punto de entrada para los modelos externos. La autoridad completa es `docs/CONTRATO_OPERATIVO_UNIFICADO.md`; no mantiene reglas paralelas.

## Reglas de ejecución
1. **ChatGPT:** investigación, fuentes, radar, rotación y storyboard textual. No genera medios, no monta, no ejecuta QA audiovisual oficial, no programa ni publica. No edita `data/*.json`.
2. **Imaginantes (Grok Bot):** recibe paquetes, registra estados, produce medios, monta, ejecuta QA oficial y administra programación/publicación autorizada. Es el único operador de publicación.
3. **Grok app:** apoyo bajo coordinación de Imaginantes; no crea una ruta paralela ni publica duplicados.
4. **Mj:** define prioridades y autoriza cambios de alcance o cupo.

## Cupo
La capacidad configurada en esta rama es de hasta cinco cápsulas por fecha (máximo dos propias y cinco externas, con tope global de cinco). El procesador recorre múltiples entradas de la fecha y conserva la entrada original si falla producción. La programación cuenta con cinco ventanas asociadas a la parrilla (07:00, 13:30, 17:00, 19:00 y 23:30 CDMX). Esto no demuestra cinco publicaciones efectivas: cada una requiere QA y evidencia registrada. Ver secciones 3 y 8 del contrato unificado.

## Handoff
ChatGPT deja radar y storyboard textual en las rutas definidas por el Plan Maestro. Imaginantes registra recepción solo después de leer el paquete en `cola/estado/<project_id>.json`, decide, produce, hace QA y registra publicación con URL/ID. Sin estado no hay recepción confirmada.

## Reglas no negociables
- No inventar fuentes, DOI, cifras, claims, recepción, QA o publicación.
- No subir secretos ni tokens.
- No tocar `main`, Motor U6 ni motores canónicos.
- No modificar `data/*.json` desde ChatGPT.
- No publicar desde ChatGPT.
- Los paquetes históricos solo se reutilizan tras revisar su estado real; carpeta existente no equivale a publicación.

## Descarga de carga para Grok Bot

Aplicar `docs/PROTOCOLO_DESCARGA_CARGA_GROK.md`. ChatGPT debe entregar preproducción textual completa y validada (research, fuentes, guion, storyboard, prompts visuales, audio/SFX y metadata). Imaginantes/Grok Bot debe dedicar su trabajo a producir los medios, montar/renderizar, ejecutar QA audiovisual y publicar cuando esté autorizado. No duplicar research ni reescribir guiones por rutina. Las correcciones se limitan al campo/escena defectuoso; los faltantes factuales vuelven a ChatGPT como solicitud puntual. Las correcciones consumen tokens: evitar reescrituras y regeneraciones completas innecesarias.

## 31-oct — tips ciencia+hack
ChatGPT busca y empaqueta tips/life-hack con ancla científica (ver PARA_CHATGPT_tips_ciencia_hack_31oct.md). Imaginantes solo monta/publica. Hashtags simples. Evitar flops: aves-mujeres, dato abstracto de luz.

## Standing diario — dato del día 23:30 CDMX
Instrucción permanente: ver `PARA_CHATGPT_dato_del_dia.md`.
ChatGPT entrega cada día UN paquete en `cola/entrada/YYYY-MM-DD_dato-<slug>/` (storyboard.json, fuentes.md, ESTADO_EJECUCION.md = PREPARADO_PENDIENTE_REVISION_GROK) para el slot 23:30 del mismo día; sin anticipación de días ni duplicados.
Imaginantes monta y programa. ChatGPT no tiene cron: se activa por pegado de Mj o Custom Instructions.

> **Regla de cierre (obligatoria):** ver bloque «Cierre (obligatorio)» en `PARA_CHATGPT_dato_del_dia.md` — las 2 últimas escenas cierran; la última nunca es solo el sello.

## Regla de portada YouTube Shorts (Mj 31-oct, obligatoria)
- La portada / custom thumbnail de YT es SIEMPRE el frame de la escena gancho (la pregunta inicial, `scene_001`). Nunca una escena intermedia.
- **ChatGPT:** cada storyboard.json lleva `"thumbnail_source": "scene_001"` (o el id de la escena gancho si fuera otro). La escena gancho debe tener la pregunta en `narration`/`on_screen_text`.
- **Imaginantes/Grok:** al publicar, `scripts/publicar.py` sube `frames/<thumbnail_source>.jpg|png` con `thumbnails.set` (reescalado a 1280px máx, <2 MB). Si la subida falla, el paquete no se marca listo hasta corregirlo a mano en YT Studio con ese mismo frame.
- TikTok/Facebook: elegir como portada el primer segundo/frame del gancho.
