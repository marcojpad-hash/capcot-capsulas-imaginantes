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
