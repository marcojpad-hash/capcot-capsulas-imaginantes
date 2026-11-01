# QA narrativo en frío — CAPCOT

**Estado:** compuerta obligatoria previa al handoff a Grok.  
**Rama:** feature/capcot-video-discovery-continuity.

## Propósito

Evitar que un storyboard llegue a la cola por tener JSON válido, etiquetas de arco o una sucesión de datos. Se evalúa una historia oral completa: pregunta central, promesa, stakes, giro científico, límite de evidencia y payoff.

Este QA es independiente del validador estructural y del QA audiovisual oficial de Grok. No selecciona el tema ni autoriza producción o publicación.

## Separación de funciones

- **Investigador/redactor (08:00):** redacta y guarda el borrador en proyectos/<project_id>/storyboard.json. No crea la entrada de cola, no añade narrative_qa y no se autoevalúa.
- **Auditor/revisor (15:00):** es una ejecución/conversación distinta. Oculta título, resumen, arco y notas; extrae y lee únicamente las narraciones de todas las escenas, concatenadas en orden.
- **Grok:** recibe solo paquetes que ya superaron esta compuerta. Mantiene selección editorial, producción audiovisual, QA oficial y publicación.

## Contrato narrativo del autor

El borrador incluye un objeto `narrative_contract` con seis campos no vacíos: `central_question`, `promise`, `stakes`, `scientific_turn`, `evidence_limit` y `payoff`. Este contrato guía la escritura, pero no es evidencia ni puede sustituir la narración.

Durante la lectura en frío, el revisor también oculta `narrative_contract`; no debe usarlo para reconstruir la historia. La pregunta, progresión, giro, límite y payoff tienen que ser recuperables solo desde la narración.

## Siete checks obligatorios

El revisor marca cada campo booleano, con evidencia breve:

1. pregunta_central_reconstruible: la narración permite reconstruir una sola pregunta central y la promesa.
2. apertura_in_medias_res: la primera escena comienza con acción, anomalía o consecuencia ya en curso; no con una definición ni pregunta genérica.
3. progresion_por_escena: cada escena agrega información necesaria y cumple una función dramática distinta.
4. transiciones_causales: cada tramo responde o complica el anterior y deja una razón concreta para continuar.
5. giro_cientifico_explicado: el hallazgo o mecanismo cambia la comprensión inicial y está explicado, no solo nombrado.
6. limite_evidencia_explicito: distingue qué se midió/demostró, bajo qué condiciones y qué no permite concluir.
7. payoff_cierre_apertura: el final resuelve o resignifica la apertura; no introduce un tema nuevo.

## Umbral de decisión

PASS requiere simultáneamente:
- score >= 85/100;
- los siete checks en true;
- critical_flags vacío.

Cualquier check false, sobreafirmación científica, dato decorativo, transición genérica, cierre sin payoff o ausencia de revisor independiente produce FAIL. Si no se realizó la lectura independiente, usar score 0, los siete checks false y critical_flags: ["REVISION_INDEPENDIENTE_AUSENTE"]; no simular una puntuación.

## Registro machine-readable

El auditor escribe en el storyboard:

```json
{
  "narrative_qa": {
    "status": "FAIL",
    "score": 0,
    "review_basis": "lectura_en_frio_solo_narracion",
    "checks": {
      "pregunta_central_reconstruible": false,
      "apertura_in_medias_res": false,
      "progresion_por_escena": false,
      "transiciones_causales": false,
      "giro_cientifico_explicado": false,
      "limite_evidencia_explicito": false,
      "payoff_cierre_apertura": false
    },
    "critical_flags": ["REVISION_INDEPENDIENTE_AUSENTE"],
    "reviewer_role": "auditor_capcot_independiente"
  }
}
```

El ejemplo es solo el esquema; no es un resultado. El auditor debe reemplazar cada valor según la revisión real. No puede marcar PASS por cumplir el esquema.

## Flujo de archivos

1. El investigador crea brief y borrador en docs/briefs/ y proyectos/.
2. El auditor relee el borrador desde GitHub y hace QA en frío sin consultar título, resumen, arco ni notas durante la evaluación.
3. Escribe narrative_qa en el borrador y vuelve a leer/verificar el JSON.
4. Si PASS, crea/promueve una copia de handoff en cola/entrada/YYYY-MM-DD_slug.json y compara el contenido después de escribir.
5. Si FAIL, el borrador permanece en proyectos/ y no se crea entrada de cola.
6. Para entradas heredadas ya presentes en cola/entrada/ que fallen, mueve el archivo a cola/bloqueados/<project_id>/storyboard.json después de verificar la copia; conserva el contenido íntegro. No borra ni reescribe la narración.
7. Si la promoción o el movimiento no se pueden verificar, informa el bloqueo y no declara dispatchabilidad.

## Reglas editoriales y científicas

- La narración concatenada debe leerse como una sola pieza oral.
- Cada cifra debe indicar qué se midió, condiciones e interpretación; no se agregan cifras para rellenar duración.
- No inventar protagonistas, episodios, intenciones biológicas ni causalidad.
- Profundizar mecanismo, consecuencia, transición o límite en lugar de añadir datos inconexos.
- El cierre hablado conserva exactamente: Esto fue Datos y ociosidades.
- No cambiar claims durante el QA. Si el guion requiere reescritura, el auditor devuelve observaciones al investigador; el nuevo texto vuelve a pasar por QA independiente.

## Reglas de handoff

- Sin narrative_qa.status=PASS, el storyboard no está preparado, no se promueve y no debe permanecer en cola/entrada/.
- approved_assets=[]; export.render_status=NOT_GENERATED; sin asset_filename ni rutas de medios en preproducción.
- Cortinilla de fuentes: 6 segundos conforme a plantilla y receta; duración total de escenas más cortinilla: 75–90 segundos.
- No crear ni modificar cola/estado/<project_id>.json; solo Grok registra recepción/decisión/producción/QA/publicación.
- No publicar, programar, generar medios ni consumir créditos desde esta compuerta.
