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
La parrilla de cinco slots diarios es el objetivo editorial, no la capacidad actual del pipeline. El código vigente limita a tres por día (dos propias y una externa), y el procesador acepta una entrada externa por fecha. No forzar cupos ni anunciar cinco publicaciones ejecutables hasta que código, pruebas y validadores hayan sido actualizados y verificados. Ver sección 3 y 8 del contrato unificado.

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
