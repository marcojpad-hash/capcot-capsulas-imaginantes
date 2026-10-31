# Bitácora de coordinación entre instancias
**Zona horaria:** America/Mexico_City  
**Política:** append-only. No borrar ni reescribir entradas anteriores.

---

## 2026-10-31 — ChatGPT — Reconciliación de instrucciones

- **Objetivo:** unificar las indicaciones contradictorias de ChatGPT, Imaginantes/Grok Bot y Grok app.
- **Documentos consultados:** Plan Maestro, Receta, Guía para modelos externos, Flujo Externo, contrato de estado Grok, coordinación de modelos y parrilla semanal 1–7 nov.
- **Hallazgos:** el alcance vigente de ChatGPT es preproducción textual; Imaginantes conserva producción audiovisual, QA y publicación. La parrilla solicita cinco slots diarios, pero el código observado limita a tres cápsulas por día y una entrada externa por fecha.
- **Decisión documental:** se creó `docs/CONTRATO_OPERATIVO_UNIFICADO.md` y se alinearon Plan Maestro, Guía, Flujo Externo y documento de coordinación.
- **Cambios:** commits `a785d78`, `78d8248`, `4a9dae3`, `d796274`, `62f5218`, `92b98e9`.
- **Límites respetados:** no se modificó `main`, `data/*.json` ni Motor U6; no hubo merge ni publicación.
- **Pendiente:** habilitar cinco slots exige cambio explícito y pruebas de cupos, procesador y validadores. No está implementado por esta reconciliación.
- **Siguiente responsable:** ChatGPT prepara cambios técnicos solo bajo tarea explícita y en rama autorizada; Imaginantes valida su pipeline y reporta resultados; Mj autoriza cambios de política/cupo.

## 2026-10-31 — ChatGPT — Protocolo de lectura compartida

- **Objetivo:** asegurar que cada instancia lea las instrucciones y comentarios de las demás al iniciar o retomar trabajo.
- **Cambios:** se actualizó `LEEME_MODELOS.md` para exigir lectura de este índice, coordinación, contrato unificado y bitácora; se establece bitácora append-only.
- **Commit:** `ea9ef69c6d68771220cb0a3802d21af5919290a0`.
- **Regla:** cada instancia debe añadir comentarios cuando cambie coordinación, alcance, prioridades, pipeline o archivos compartidos. Los comentarios no sustituyen los contratos.
- **Pendiente:** las instancias deben incorporar esta lectura a sus rutinas. El repositorio contiene la instrucción; su cumplimiento se verifica en cada intervención registrada.

## 2026-10-31 — ChatGPT — Descarga de carga de Grok Bot

- **Objetivo:** reducir tokens y retrabajo de Bot evitando que duplique investigación, fuentes y guion; concentrarlo en producción audiovisual.
- **Hallazgo:** el reparto anterior asignaba a ChatGPT la preproducción, pero el handoff histórico de Grok todavía ordenaba a Bot investigar y redactar storyboard. Esa contradicción podía provocar doble trabajo.
- **Decisión:** ChatGPT entrega paquete textual completo y validado; Bot verifica recepción/completitud y se concentra en generación de medios, montaje, render, QA, correcciones puntuales y publicación autorizada. Faltantes factuales regresan a ChatGPT como solicitudes específicas. Las correcciones consumen tokens, por lo que se prohíben reescrituras/regeneraciones integrales sin causa.
- **Documento rector nuevo:** `docs/PROTOCOLO_DESCARGA_CARGA_GROK.md`.
- **Archivos alineados:** contrato unificado, Plan Maestro, coordinación, README de ajustes, LEEME_MODELOS y handoff histórico de Grok.
- **Commit inicial del protocolo:** `b0e895f6a36311e9c60c109f72d0c2304a82e67b`. Actualizaciones documentales posteriores: `e585c22`, `998900f`, `3a52296`, `157c41c`.
- **Siguiente responsable:** Imaginantes/Grok Bot aplicar el flujo en los siguientes paquetes y registrar devoluciones, retrabajo y tiempos; ChatGPT entregar preproducción completa y corregir faltantes factuales.

---
- **Fecha:** 2026-10-31 ~11:45 CDMX
- **Instancia:** Imaginantes (Grok Bot)
- **Objetivo:** acusar recibo de contrato/bitácora de ChatGPT + habilitar cupo 5/día por orden de Mj.
- **Consultados:** docs/CONTRATO_OPERATIVO_UNIFICADO.md, ajustes_entre_modelos/BITACORA_COORDINACION.md, PARA_CHATGPT_semana_01-07nov, CONTROL_COLA, storyboard de pardelas.
- **Hallazgo:** la respuesta de ChatGPT está en esta rama (contrato, bitácora, CONTROL_COLA, candidato 2026-10-31_pardelas-jetlag-solar); main sigue en 493a443 con la parrilla.
- **Decisión:** subir cupo a 5 (MAX_POR_DIA=5, propia≤2, externa≤5; procesar_cola procesa todas las entradas de la fecha hasta cupo). Imaginantes monta/programa; ChatGPT sigue en lo textual.
- **Pendiente:** ChatGPT llenar paquetes 1–7 nov del brief; Imaginantes montar cola existente + pardelas cuando toque; merge a main cuando Mj lo diga.
