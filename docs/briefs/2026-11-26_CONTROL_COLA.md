# Control de cola CAPCOT — 2026-11-26

**Corte:** 2026-11-26, 02:14 America/Mexico_City  
**Rama de trabajo:** feature/capcot-video-discovery-continuity  
**HEAD de proyecto tras la auditoría de Quasar y antes de registrar los briefs:** cd9ffa5e0fa4f498242b586347c2584923089d04  
**Regla:** solo lectura en main; sin dispatch, payload, publicación, programación, generación de medios ni consumo de créditos.

## 1. Ramas, CI y contratos

- En la comparación main → feature, la rama feature tiene 1,431 commits exclusivos y main tiene 594 commits exclusivos. PR #3 sigue abierto y GitHub lo reporta mergeable=false. No fusionar ni sincronizar por fuerza.
- main está en 5667579d040c89907c5784b643a758be4aed5674. Ese commit añade skills/, templates/skill_capsula.json y LEEME_MODELOS.md. La nueva ficha propone 190–210 palabras para cápsulas adultas y asigna investigación/redacción a Grok, auditoría a ChatGPT y generación a Gemini. Esto difiere de la ficha maestra vigente, que asigna investigación a ChatGPT, auditoría a Grok y prohíbe generar medios en esta etapa. Se siguió la ficha maestra. Para trabajos futuros, 190–210 palabras satisface la intersección con el rango maestro 170–235; no se reescribieron expedientes existentes.
- La última ejecución de Actions de feature es #45705919466, exitosa, sobre un SHA anterior (331cd6...). Su log valida únicamente Kuroshio y comprueba production_mode, approved_assets y render_status; no ejecuta --check-doi ni auditoría narrativa completa. No equivale a validar el backlog.
- En main, Semgrep #45766124954 terminó con 37 hallazgos bloqueantes. El paso de subida SARIF quedó omitido; no hay evidencia descargable de los hallazgos individuales en ese run. No se modificó main.
- No se disparó ningún workflow. Los cambios de este run afectan únicamente proyectos/ y docs/briefs/; no coinciden con los filtros de capcot-grok-dispatch.yml, validar-kuroshio.yml, tts-tooling-smoke.yml ni capcot-descubrimiento.yml.

### Corrección del control anterior

templates/grok_status.template.json sí existe en feature (blob SHA 8962cc751e5023f071e1e7b439501efa52ab5a35). El reporte del 25-nov que lo marcó como ausente no coincide con el árbol actual. El archivo es una plantilla; no prueba recepción individual ni crea un estado Grok.

## 2. Proyectos y QA narrativo

El árbol de la rama contiene 90 storyboards. Este corte interdiario cubrió los 37 proyectos fechados del 5 al 23-nov: los 12 IDs expresamente señalados del 5–7-nov, el expediente del 9-nov, 15 expedientes del 10–20-nov y 9 expedientes del 21–23-nov. Los 53 storyboards anteriores al 5-nov se dejaron como archivo histórico y no se reauditaron narrativamente en este corte.

| Grupo | Proyectos | Narrative QA |
|---|---:|---:|
| 5–7 nov (lote explícito) | 12 | 2 PASS / 10 FAIL |
| 9 nov (robot/orbita) | 1 | 1 PASS |
| 10–20 nov | 15 | 12 PASS / 3 FAIL |
| 21–23 nov | 9 | 2 PASS / 7 FAIL |
| **Total** | **37** | **17 PASS / 20 FAIL** |

- Los PASS existentes se conservaron; no se repitió PASS cuando el historial del archivo mostró cambios solo de fuentes/notas y no de narración.
- En los 12 IDs del 5–7-nov, todos los storyboards carecen de los seis campos narrativos por escena que exige el validador vigente: dramatic_beat, scene_function, causal_bridge_from_previous, question_state, reason_to_continue y new_information. Se observaron 42–48 omisiones por expediente. Uno de los 12, 2026-11-05_inter-arboles-se-comunican, también carece de capa de mapa y de dato/gráfico con coordenadas/fuente. Varios tienen arreglos SFX vacíos. Los dos PASS narrativos de este lote no superan por ello la compuerta estructural.
- En los expedientes del 10–20-nov, la estructura manual revisada contiene capas de mapa/dato, prompt_base coincidente, 8 escenas y 84 s; 2026-11-10_dato-adn-sincroniza-flujo tiene seis escenas con SFX vacío. Quedan tres FAIL narrativos: Quasar, Catorce campos hidrotermales y Marea cerebral.
- En los expedientes del 21–23-nov, la estructura manual revisada contiene 8 escenas y 84 s; 2026-11-23_supersequias-722-eventos tiene metadatos incompletos en una fuente. Los dos PASS narrativos son Fentale y Yubarta; las modificaciones posteriores revisadas afectaron fuentes/notas, no la narración.
- La inspección estructural fue manual contra los requisitos de scripts/validar_storyboard.py; no se ejecutó el validador completo sobre los 37. No se afirma un PASS estructural global. El último CI disponible solo cubre Kuroshio.
- Los DOI/URL de los 37 expedientes no se volvieron a resolver uno por uno en este corte. CI sin --check-doi no acredita esa compuerta.

### Acción ejecutada: Quasar

Se leyó en frío únicamente la narración concatenada de 2026-11-15_dato-quasar-pareja-cosmic-dawn, sin título, resumen, arco, notas ni narrative_contract. Se actualizó y leyó de vuelta narrative_qa:

- status=FAIL, score=82.
- review_basis=lectura_en_frio_solo_narracion.
- reviewer_role=auditor_capcot_independiente.
- Checks: pregunta central, apertura, progresión, transiciones, límite y payoff = true; giro_cientifico_explicado=false.
- Flag: GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO.
- Evidencia: la narración menciona las alas azules de [O III] como pista para distinguir dos fuentes, pero no explica por qué esa diferencia favorece dos cuásares frente a una lente gravitacional.

Commit de QA: cd9ffa5e0fa4f498242b586347c2584923089d04. Lectura de vuelta confirmada. La narración y los claims permanecen intactos. No existe ESTADO_EJECUCION.md en el expediente Quasar; no se inventó ni se creó uno.

## 3. Cola, Grok y procesamiento preexistente

- En feature, cola/entrada/ contiene un único paquete anidado del 9-nov; no hay JSON plano en la raíz de entrada. En main hay 33 paquetes anidados y cero JSON planos. El workflow de Grok escucha cola/entrada/*.json; un directorio anidado no coincide con ese patrón. Clasificación: NOT_DISPATCHABLE.
- No existen archivos individuales en cola/estado/ en las ramas inspeccionadas. Para los storyboards sin estado: RECEPCION_GROK_NO_CONFIRMADA. No se crearon ni editaron estados.
- Existe un marcador handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json con estado pending; no acredita recepción de Grok.
- main contiene para ese expediente capsula.mp4, nueve frames, miniatura, programacion.json y qa.json. El registro de programación muestra yt_id=ZG4iQgmWrLI, programación para 21-nov-2026 19:00 CDMX (publish_at=2026-11-22T01:00:00Z). El QA registrado es 21/21. El ESTADO_EJECUCION heredado dice que no se programó, en contradicción con programacion.json; se toma la programación y el ID como evidencia de procesamiento preexistente. Clasificación: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. Los medios están en main, no en la copia de feature.
- templates/grok_status.template.json está presente, pero no hay estados individuales. La presencia de la plantilla no prueba recepción.
- El workflow referencia secretos de webhook, pero el conector usado no permite comprobar la lista de nombres de secretos. No se afirma que falten ni se consultaron valores.

## 4. Rotación y ocupación del 26-nov

La conciliación entre ramas sigue incompleta:

| Fuente | Rama feature | main |
|---|---|---|
| data/publicaciones.json | 22 registros, último 31-oct | 62 registros, último 23-nov |
| data/rotacion.json | 27 registros, último 31-oct | sin conciliación equivalente con los nuevos reworks |
| data/temas_del_dia.json | última fecha 28-oct | sin registro vigente del 26-nov |
| data/horarios.json | actualizado 9-nov; fija 23:30 | mismo contrato histórico |

scripts/registro_editorial.py lee rotación, publicaciones, cola, proyectos y salidas de su propia rama; no incorpora data/rehechos_2026-11-22.json ni data/miniaturas_auditoria_2026-11-21.json de main. Por tanto, el cálculo automático de cupos/rotación en feature no representa el inventario actual de main. El último registro publicado de main es 2026-11-23_oso-wojtek, slot 23:30; ese registro tampoco existe en el archivo de publicaciones de feature.

En main, el 26-nov aparecen:
- Rework a las 10:00: “El refri NO salva tu pan”.
- Rework a las 15:00: “Ayudar con las crías NO era quedarse en el nido”.
- Dos IDs programados en colisión a las 17:00: JqlKsJOVmdE y -1DRh_qj7Bg.
- No aparece registro de 23:30 en los snapshots consultados.

No existe un archivo historial_youtube vigente en el árbol inspeccionado ni una lectura actual de YouTube Studio. Aunque el snapshot del repositorio no muestra un video a las 23:30, no se puede certificar que un ID antiguo siga o no programado fuera del repositorio. Resultado: OCUPACION_23_30_NO_CONCILIADA. No se creó storyboard para el 26-nov.

## 5. Issues y decisiones externas

- Issue #11 sigue abierto; PR #13 y PR #14 siguen abiertos y sin merge. No se fusionaron ni cerraron.
- Issue #16 sigue abierto y sin comentarios nuevos. Sus solicitudes de producción/resubida/publicación externa no se ejecutaron.
- No se enviaron mensajes externos, no se subieron archivos a plataformas, no se programó ni publicó, no se generaron medios ni placeholders y no se consumieron créditos.
- No se modificó data/*.json, cola/entrada, cola/estado, cola/bloqueados, main, secretos ni permisos.

## 6. Commits materiales de este run

- Quasar: 0caa26af40f1d6d1252f11867e1b2c85150820da (lectura fría) y cd9ffa5e0fa4f498242b586347c2584923089d04 (alineación del rol auditor).
- Radar: 7737d2f5cfd3d4f0bea7214d2efe3302247dd180.
- Primera escritura de este control: 8b19990be54551b43d3772a66d66614dd5199ba3; esta actualización corrige el registro de HEAD.

## 7. Resultado del corte

- **EJECUTADO Y VERIFICADO:** QA narrativo frío de Quasar, registrado y leído de vuelta; radar del 26-nov creado en docs/briefs/2026-11-26_RADAR_CAPCOT.md; este control creado en docs/briefs/2026-11-26_CONTROL_COLA.md.
- **NOT_DISPATCHABLE:** todos los proyectos sin JSON plano de entrada y sin estado Grok individual.
- **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR:** paquete Robot/órbita, por MP4, QA y programación en main.
- **PENDIENTE:** resolver la ocupación real del slot 23:30 con historial/Studio vigente; ejecutar el validador estructural real y DOI/Crossref en los expedientes que superen QA; corregir los campos estructurales de los 12 expedientes antiguos solo cuando se pueda hacer sin reescribir claims ni decisiones narrativas.


## Addendum de verificación — 2026-11-26 02:24 CDMX

### Quasar: alcance real de la revisión independiente

- El registro actual de `narrative_qa` permanece **FAIL/82**, con seis checks verdaderos, `giro_cientifico_explicado=false` y `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`. No se modificó la narración ni el score.
- La pasada fría del 26-nov fue separada y leyó solo la narración concatenada, pero la ejecutó ChatGPT. El requisito específico del Issue #11 pide auditor de otro modelo (Grok/Gemini); ese requisito de diversidad de modelo sigue sin evidencia.
- PR #12 (cerrado sin merge) y PR #13 (abierto, sin merge) contienen auditorías Groq gpt-oss-120b sobre el commit histórico `54c8ade`, pero usan el checklist anterior (hook/payoff, primer dato 5–8 s, fuentes) y referencias al storyboard completo. No acreditan la lectura ciega de solo narración ni los siete checks del contrato vigente.
- **Estado del Issue #11: ABIERTO.** No se declara completada la auditoría externa de otro modelo y no se promueve Quasar.

### PR #15: implementación ya presente; pruebas aún no incorporadas

- PR #15 sigue abierto, `mergeable=false`, `mergeable_state=dirty`; su head es `947df50e` y su base es `feature/capcot-video-discovery-continuity`.
- La implementación que propone ya está en la rama base: commits `b6d7fbb` (rechazo de coordenadas booleanas y endurecimiento Crossref) y `08d5cc0` (corrección del patrón DOI). La lectura actual de `scripts/validar_storyboard.py` confirma rechazo de booleanos en lat/lon, RA/Dec y bounds, además de HTTPS fijo con TLS verificado para Crossref.
- La cobertura nueva del PR (seis pruebas de booleanos y DOI/TLS) **no** está en `tests/test_validar_storyboard_textual.py` de la rama base; el archivo base conserva ocho métodos y ninguno cubre esos casos. Por tanto, el código está presente, pero la regresión específica sigue pendiente de incorporar/ejecutar.
- No se fusionó ni cerró PR #15. No se disparó CI ni se afirmó que las pruebas nuevas hayan pasado.



## Addendum de revalidación — 2026-11-26 04:00 CDMX

### Rama, CI y handoff

- HEAD revalidado de `feature/capcot-video-discovery-continuity`: `7cfdc3a085f230f732830a67248b91d1753bc8d7`. HEAD de `main`: `5667579d040c89907c5784b643a758be4aed5674`.
- PR #3 continúa abierto y `mergeable=false`, `mergeable_state=dirty`: 1,435 commits, 718 archivos modificados. CodeQL del PR, run #45784089913, terminó `success` el 26-nov 08:32 UTC. No hubo run de dispatch Grok en las Actions consultadas.
- PR #15 continúa abierto y dirty. La implementación de validación de booleanos/TLS ya está en la rama base, pero las pruebas nuevas siguen fuera de `tests/test_validar_storyboard_textual.py`; no se afirmó que esa regresión haya sido ejecutada.
- Se verificaron los filtros de `capcot-grok-dispatch.yml`, `validar-kuroshio.yml`, `tts-tooling-smoke.yml` y `capcot-descubrimiento.yml`: `docs/briefs/**` no activa sus filtros de push. Este addendum no requiere disparar Actions.

### Lote explícito 5–7 nov

- Revisión de integridad: los 12 `storyboard.json` conservan como último commit el 18-nov-2026 21:58–21:59 UTC, y sus registros `narrative_qa` siguen fechados el 18-nov. No se detectó cambio de narración; se conservaron los 2 PASS y 10 FAIL sin repetir ni sobrescribir PASS.
- No existe `ESTADO_EJECUCION.md` para ninguno de los 12 proyectos. Los 12 intentos de lectura de `cola/estado/<project_id>.json` devolvieron 404: `RECEPCION_GROK_NO_CONFIRMADA`. No hay JSON plano de entrada para esos IDs y no se promovió ninguno.
- Persisten las seis omisiones estructurales por escena documentadas en el corte anterior (`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`), además de las carencias de mapa/dato/SFX ya registradas. Los dos PASS narrativos continúan sin superar la compuerta estructural.

### Expediente main-only del 25-nov: React/doxorrubicina

- `proyectos/2026-11-25_react-bacterias-anticancer/storyboard.json` existe también como copia anidada en `cola/entrada/2026-11-25_react-bacterias-anticancer/storyboard.json`. No hay `ESTADO_EJECUCION.md`, `cola/estado/<id>.json` ni archivo de salida `capsula.mp4`.
- `programacion.json` conserva `status=programado_paquete` y `publish_at=2026-11-25T23:00:00Z` (17:00 CDMX). Se clasifica `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; el hecho de que la hora ya haya pasado no prueba publicación, porque no hay historial de YouTube ni lectura actual de Studio.
- La copia de cola está anidada. El workflow solo consume `cola/entrada/*.json` y, en dispatch manual, busca con `find ... -maxdepth 1`; por tanto la ruta observada es `NOT_DISPATCHABLE`.
- Lectura fría de la narración concatenada, sin título ni metadatos: FAIL/57. Checks: pregunta central true; apertura in medias res false; progresión por escena true; transiciones causales false; giro científico explicado true; límite de evidencia explícito true; payoff cierre-apertura false. No se escribió `narrative_qa` porque el expediente está en `main`, que permanece solo consulta.
- Estructura observada: 6 escenas, 102 palabras y 66 s frente al contrato de 7–9 escenas, 170–235 palabras y 75–90 s. DOI `10.1126/science.aee2641` coincide con el artículo primario de *Science* publicado el 19-nov-2026 (registro PubMed); el endpoint Crossref no fue accesible en esta pasada. El abstract consultado no acredita por sí solo la cifra exacta de 40,000 proteínas: esa afirmación requiere texto completo/suplemento o queda `PENDING_SOURCE`. No hay medios binarios en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.

### Reworks programados del 26-nov y slot 23:30

- `data/rehechos_2026-11-22.json` conserva dos paquetes para el 26-nov: 10:00 CDMX, video ID `7pzPfqRSagU`; y 15:00 CDMX, video ID `MgHVHbeIVS0`, ambos con `publishAt` y estado programado. Clasificación de ambos: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- Los directorios de proyecto revisados contienen storyboard/metadata/registro de render, pero no `capsula.mp4` ni `portada`; tampoco hay salida correspondiente en `salidas/`. Se marca `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`; no se reenvía ni cancela.
- No hay proyecto ni entrada para el 26-nov 23:30 en `main` o feature, ni registro 23:30 en los snapshots de publicaciones/rotación consultados. `historial_youtube` no existe en el árbol y no hay lectura actual de Studio. Se conserva `OCUPACION_23_30_NO_CONCILIADA`; no se creó storyboard.

### Fuentes de tendencia: limitación de transporte

- No se ejecutó `scripts/tendencias.py` en un runner. El visor web rechazó varios RSS por MIME XML (`400 Unsupported content-type`); el intento de descarga directa devolvió `ERROR: download failed`. Esto no demuestra que los feeds estén caídos.
- Se usó búsqueda de respaldo en fuentes oficiales: ESA confirmó la actualización Hera del 25-nov ya incluida en el radar; la nota NASA sobre cultivos espaciales remite a estudios primarios de agosto/septiembre, por lo que no desplaza a los cinco candidatos actuales. Google Trends RSS México no quedó verificado en esta pasada. Se conservan los cinco candidatos del radar sin añadir un sexto ni crear storyboard.


## Addendum de auditoría ampliada — 2026-11-26 05:55 CDMX

### Corrección de ocupación del slot 23:30

La conclusión del corte de las 04:00 queda corregida: la búsqueda anterior no detectó un expediente main-only.

- En main existe proyectos/2026-11-23_dato-thanksgiving-washington/storyboard.json; no existe copia equivalente en feature.
- metadata.json fija publishAt_utc=2026-11-27T05:30:00Z, equivalente a 2026-11-26 23:30 CDMX. El proyecto está en proyectos/, no en una entrada plana de cola/entrada.
- El storyboard tiene 6 escenas y 207 palabras. render.log informa duración medida de 89.56 s; qa_es.json y qa_en.json son QA audiovisual, no narrativa.
- No existe cola/estado/2026-11-23_dato-thanksgiving-washington.json (404), ni carpeta correspondiente en salidas/, ni programacion.json. capsula.mp4 y capsula_en.mp4 no están en el árbol Git, aunque metadata y render logs los referencian.
- No hay narrative_qa ni registro de revisión fría independiente. Estado de auditoría: FAIL, score 0, critical_flags=["REVISION_INDEPENDIENTE_AUSENTE"]. No se escribió el campo en main.
- El tema es histórico/Thanksgiving y queda fuera de las categorías editoriales vigentes (ciencia, naturaleza, cocina, cuerpo y espacio).

Clasificación: CONFLICTO_DE_SLOT_ENTRE_RAMAS; PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR; MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO; RECEPCION_GROK_NO_CONFIRMADA; NOT_DISPATCHABLE. No se duplicó, movió ni canceló nada.

### Otros paquetes main-only del 25–26 nov

- 2026-11-25_react-bacterias-anticancer: el storyboard aparece en cola/entrada/<id>/storyboard.json (ruta anidada), con programacion.json en status=programado_paquete y publish_at=2026-11-25T23:00:00Z. El estado Grok individual devuelve 404 y no hay carpeta salidas/<id>/. La ruta no coincide con cola/entrada/*.json ni con find -maxdepth 1. Se conserva la auditoría anterior FAIL/57; no cambió la narración y no se repitió la revisión.
- 2026-11-25_rehecho-pan-refri-endurece: data/rehechos_2026-11-22.json mantiene programación 10:00 CDMX y video ID 7pzPfqRSagU.
- 2026-11-25_rehecho-ratas-topo-ayudar-no-es-cuidar: el mismo registro mantiene programación 15:00 CDMX y video ID MgHVHbeIVS0.
- Los dos reworks tienen render.log y duración medida de 88.47 s y 88.80 s. Sus MP4 no están en el árbol Git; no hay carpetas salidas/<id>/ ni estados Grok individuales (404). Ambos son PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR, MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO, RECEPCION_GROK_NO_CONFIRMADA y NOT_DISPATCHABLE.

### QA narrativo frío separado de los dos reworks

La lectura se hizo solo sobre la narración concatenada, sin título, resumen, arco, notas ni narrative_contract. No se modificaron claims ni storyboards.

**Pan / refrigeración**

- status=FAIL, score=82, review_basis=lectura_en_frio_solo_narracion.
- Checks: pregunta_central_reconstruible=true; apertura_in_medias_res=true; progresion_por_escena=true; transiciones_causales=true; giro_cientifico_explicado=true; limite_evidencia_explicito=false; payoff_cierre_apertura=true.
- critical_flags=["AFIRMACION_SEQUEDAD_ABSOLUTA_NO_SOSTENIDA"].
- La frase “no es porque se seque” es demasiado absoluta: el estudio primario citado describe retrogradación del almidón y redistribución de humedad/deshidratación de la miga. No se reescribió.
- Estructura observada: 7 escenas, 219 palabras, objetivo 88 s y render 88.47 s. La primera línea tiene 15 palabras y no hay campo gancho separado de máximo 6 palabras. Faltan prompt_base, mapa con coordenadas, dato/gráfico y ambiente por escena; no existe fuentes.md. Hay referencias de asset y export de producción preexistente.

**Ratas topo de Damaraland**

- status=PASS, score=90, review_basis=lectura_en_frio_solo_narracion.
- Los siete checks son true: pregunta central, apertura, progresión, transiciones causales, giro científico, límite de evidencia y payoff. critical_flags=[].
- La narración mantiene como propuesta de los autores la explicación de que el trabajo fuera del nido apoya a la madre; no lo presenta como prueba de cuidado directo.
- Estructura observada: 7 escenas, 218 palabras, objetivo 88 s y render 88.80 s. El primer fragmento de gancho es “Nacen las crías” (3 palabras), pero no hay campo gancho independiente. Faltan prompt_base, mapa con coordenadas, dato/gráfico y ambiente por escena; no existe fuentes.md. Hay referencias de asset y export de producción preexistente.

Los dos registros de QA se documentan aquí porque los expedientes están en main, que permanece SOLO_CONSULTA; no se escribió narrative_qa en esos storyboards.

### Conciliación de horarios y riesgo de IDs antiguos

La versión vigente de main/data/horarios.json (23-nov) define 06:30–07:30, una ventana de prueba 13:00–14:30, 16:30–18:00 y el slot fijo 23:30. El slot 19:00 fue retirado. Los reworks de 10:00 y 15:00 son producción preexistente, no nuevos slots autorizados.

- 07:00: snapshot data/miniaturas_auditoria_2026-11-21.json conserva ID ZkrzVP6V5k8.
- 13:30: el mismo snapshot conserva ID 966qJDbIJp4.
- 17:00: docs/briefs/produccion_2026-11-23_28/plan_semana.json conserva -1DRh_qj7Bg; el snapshot de miniaturas conserva JqlKsJOVmdE, ambos con publishAt=2026-11-26T23:00:00Z. Colisión de dos IDs confirmada en los snapshots, no en YouTube Studio.
- 23:30: expediente Thanksgiving main-only descrito arriba.

data/publicaciones.json tiene 62 registros y el último es del 23-nov; no contiene estos registros del 26-nov. historial_youtube.json no existe en el árbol. No hay acceso a una lectura vigente de Studio, por lo que los IDs de los snapshots quedan como riesgo de programación antigua; no se cancelan ni se reprograman.

### Rutas de Grok y dispatch

- cola/entrada/ de main contiene 34 elementos, todos directorios; feature contiene .gitkeep y un directorio anidado. No hay JSON plano en la raíz de ninguna rama.
- cola/estado/ no existe en las ramas inspeccionadas. Para los IDs examinados se confirma RECEPCION_GROK_NO_CONFIRMADA (404).
- El único marcador handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json sigue en pending; no es acuse de Grok.
- capcot-grok-dispatch.yml solo selecciona cola/entrada/*.json y, en despacho manual, usa profundidad máxima 1. La entrada anidada del robot y la del expediente React son NOT_DISPATCHABLE.
- La última Action visible de feature, #45705919466, corresponde a Kuroshio, no al dispatch. No se inspeccionaron valores de secretos; no se afirma que GROK_WEBHOOK_URL o GROK_WEBHOOK_TOKEN falten.

### Estado de rotación, ramas e Issues

- HEAD de feature revalidado: b162a123e48bb4742a4d8596f8ff6337f76c5717; el commit de revalidación anterior solo modificó este control, no storyboards. Los 12 IDs del lote 5–7 nov permanecen sin cambios desde su auditoría del 18-nov.
- HEAD de main: 5667579d040c89907c5784b643a758be4aed5674. main/data/horarios.json es del 23-nov y main/data/rotacion.json tiene 39 entradas hasta el 23-nov; feature conserva horarios del 9-nov y rotación de 27 entradas hasta el 31-oct. Los data/*.json permanecen solo lectura.
- PR #3 sigue abierto/dirty; PR #13 abierto con estado inestable; PR #15 abierto/dirty. El comentario de Semgrep sobre HTTPSConnection sigue sin resolución verificada. Issue #11 sigue abierto. Issue #16 solicita envíos de medios y acciones de publicación/resubida; no se ejecutó nada externo.
- No se promovió ningún paquete, no se disparó workflow, no se envió payload, no se publicó ni programó, no se generaron medios y no se consumieron créditos.

### Resultado del corte

- EJECUTADO Y VERIFICADO: inventario de ambas ramas y de proyectos/, cola/entrada/, cola/bloqueados/, salidas/, data/ y programación; lectura de vuelta de los proyectos main-only y estados Grok (404); QA narrativo frío de los dos reworks, documentado en este control.
- NOT_DISPATCHABLE: entradas anidadas o ausencia de JSON plano y estado Grok.
- PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR: Thanksgiving 23:30, React 25-nov y los dos reworks 10:00/15:00.
- CONFLICTO_DE_SLOT_ENTRE_RAMAS: 23:30 main-only; colisión de IDs a las 17:00 en snapshots.
- PENDIENTE: verificación de programación en YouTube Studio/historial vigente; incorporación del QA de reworks al expediente solo cuando la autoridad de rama/privacidad permita escritura; resolver la alerta de seguridad y las pruebas de PR #15. No hay slot autorizado libre para un storyboard nuevo el 26-nov.


## Addendum de auditoría posterior — 2026-11-26 06:23 CDMX

### Backlog interdiario adicional detectado en `main` (solo lectura)

La revisión anterior no había incorporado los registros del 24-nov. Se inspeccionaron las carpetas de proyecto, programación, copias de cola y registros de publicación. No se modificó `main`.

- **`2026-11-24_magnetismo-p-wave-eusi`**
  - `proyectos/<id>/storyboard.json` y `cola/entrada/<id>/storyboard.json` tienen el mismo contenido; la copia está dentro de una carpeta anidada, no como `cola/entrada/<id>.json`.
  - `programacion.json` declara `publish_at=2026-11-24T23:15:00Z` (17:15 CDMX), estado `programado_para_publicar` y nota de que falta montar el MP4. Por tanto: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** y **CONFLICTO_DE_SLOT_ENTRE_RAMAS** para 24-nov 17:15.
  - La ruta del workflow solo observa JSON planos de primer nivel en `cola/entrada/*.json`; esta copia anidada no satisface ese selector. Clasificación: **NOT_DISPATCHABLE** por ruta, sin disparar workflow.
  - `cola/estado/2026-11-24_magnetismo-p-wave-eusi.json`: 404; registrar exactamente **RECEPCION_GROK_NO_CONFIRMADA**. `salidas/2026-11-24_magnetismo-p-wave-eusi/`: 404.
  - El storyboard declara 6 escenas, 121 palabras y duración objetivo de 85 s; las duraciones de escena suman 65 s y la cortinilla declara 6 s: total declarado 71 s, inferior al contrato 75–90 s. No es duración audiovisual medida.
  - Faltan `prompt_base`, `approved_assets=[]`, `export.render_status=NOT_GENERATED` y `publicacion.status=PENDIENTE_DECISION_GROK`; existen referencias `asset_filename` y `export.filename`, pero los medios no aparecen en el árbol del proyecto. Clasificación: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No se verificó `fuentes.md`; el storyboard sí contiene un DOI, no revalidado con Crossref en esta pasada.
  - Auditoría narrativa posterior y en frío, leyendo únicamente la narración concatenada (sin título, resumen, arco, notas ni contrato): `status=FAIL`, `score=43`, `review_basis=lectura_en_frio_solo_narracion`. Checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=false`, `progresion_por_escena=true`, `transiciones_causales=false`, `giro_cientifico_explicado=false`, `limite_evidencia_explicito=false`, `payoff_cierre_apertura=true`. Flags: `APERTURA_DESCRIPTIVA`, `TRANSICIONES_CAUSALES_INSUFICIENTES`, `GIRO_CIENTIFICO_NO_EXPLICADO`, `LIMITE_EVIDENCIA_AUSENTE`. No se reescribió la narración. Este resultado queda registrado aquí; no se escribió `narrative_qa` en el storyboard porque pertenece a `main`, que es solo consulta.

- **`2026-11-24_yo-soy-sam`**
  - La carpeta contiene programación y sidecars de plataformas, pero no `storyboard.json`. La programación y `data/publicaciones.json` confirman publicación previa en YouTube, TikTok y Facebook. Clasificación: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. Sin storyboard no procede QA narrativo ni consulta de estado Grok por storyboard.

- **`2026-11-24_purpura-no-piedras`** y **`2026-11-24_pollo-lavar`**
  - No se encontraron carpetas de proyecto para esos IDs en `proyectos/`; sí existen registros previos en `data/publicaciones.json` (uno público y otro con transición privado→público programada). Clasificación: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**; no crear storyboards sustitutos ni reencolar.

### Deriva de horario entre ramas

- La rama de trabajo conserva `data/horarios.json` con política fechada 2026-11-09; `scripts/rotacion.py` mantiene ventanas codificadas para 07:00, 13:30, 17:00, 19:00 y 23:30.
- El `main` consultado contiene una política posterior, fechada 2026-11-23: ventanas activas 06:30–07:30 y 16:30–18:00, más el slot fijo 23:30; 13:30 y 19:00 ya no figuran como ventanas activas.
- La rama de trabajo puede seguir proponiendo 13:30/19:00 desde su configuración antigua. No se asignó slot nuevo ni se cambió `data/*.json` o el script; queda **DERIVA_DE_HORARIO_ENTRE_RAMA_Y_MAIN** hasta reconciliación autorizada.

### Cierre de este corte

No hay storyboard nuevo del 26-nov en la rama de trabajo. El slot 23:30 del 26-nov continúa ocupado por el proyecto Thanksgiving ya registrado en `main`; el snapshot también conserva una colisión de 17:00. No se creó cola, no se tocó estado Grok, no se disparó workflow y no se produjo ningún medio.


### Estado Grok de la rama — 2026-11-26 06:42 CDMX

La consulta de `cola/estado/` en la rama de trabajo devuelve 404 (`NOT_FOUND`). No existe un árbol de estados Grok en esta rama; para los storyboards de proyecto, la recepción queda **RECEPCION_GROK_NO_CONFIRMADA** hasta que exista el JSON individual en la fuente autorizada. No se creó ni editó ningún estado.


### Reconciliación adicional de main, rotación y Actions — 2026-11-26 08:27 CDMX

- La rama de trabajo no recibió storyboards ni proyectos nuevos desde la última auditoría; el único cambio previo fue documental. `main` sigue siendo solo lectura para esta revisión.
- `main/data/endscreens_rotacion.json` se actualizó en el commit `1202ff151f04ce14127ed4f21bf03b0e067b3b1d`. El snapshot conserva `pendiente_studio=true`; no acredita que los cambios se hayan aplicado en YouTube Studio.
- `main/data/rehechos_2026-11-22.json` contiene dos reworks preexistentes para el 26-nov: 10:00, video_id `7pzPfqRSagU`, publishAt `2026-11-26T16:00:00Z`; y 15:00, video_id `MgHVHbeIVS0`, publishAt `2026-11-26T21:00:00Z`. No son slots nuevos.
- Los snapshots de `main/data/miniaturas_auditoria_2026-11-21.json` y `docs/briefs/produccion_2026-11-23_28/plan_semana.json` conservan ocupación el 26-nov: 07:00 `ZkrzVP6V5k8`; 13:30 `966qJDbIJp4`; 17:00 colisión entre `JqlKsJOVmdE` y `-1DRh_qj7Bg`, ambos con publishAt `2026-11-26T23:00:00Z`. No cancelar ni duplicar esos IDs.
- El slot fijo 23:30 está ocupado por `proyectos/2026-11-23_dato-thanksgiving-washington`: metadata publishAt `2026-11-27T05:30:00Z` y `render.log` declara 89.56 s. La ruta MP4 declarada apunta fuera del árbol GitHub y no se encontró en `salidas/`: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- La política vigente de `main/data/horarios.json` mantiene 06:30–07:30 y 16:30–18:00, prueba reversible 13:00–14:30 y 23:30 fijo; 19:00 no está autorizado. 07:00 está ocupado, 13:30 pertenece a la prueba y está ocupado, 17:00 tiene colisión y 23:30 está ocupado. No existe slot nuevo autorizable para hoy; no crear storyboard.
- Corrección de inventario: `main/data/rotacion.json` contiene 39 registros y su último `fecha` es 2026-11-21, no 2026-11-23 como se indicó en el corte anterior. `main/data/publicaciones.json` conserva 62 registros, último 2026-11-23.
- `cola/estado/` no existe en el árbol de la rama de trabajo; la recepción individual sigue como `RECEPCION_GROK_NO_CONFIRMADA`. No hay evidencia de `historial_youtube.json` ni confirmación de Studio.
- Actions observadas: CodeQL `45784089913` SUCCESS; Gitleaks `45836080613` SUCCESS; Semgrep `45836080617` FAILURE con 37 hallazgos bloqueantes. El paso de carga SARIF fue omitido y el run no publicó artefacto SARIF, por lo que no hay lista verificable de hallazgos individuales. Se intentó reproducción local, pero no se pudo instalar Semgrep en el entorno; no se declara una segunda ejecución.
- PR #15 sigue abierto/no mergeable: la corrección del validador ya está en la rama base de trabajo, pero la cobertura de regresión adicional sigue en el PR. No se fusionó ni se abrió/cerró ningún PR.


## Addendum de verificación — 26-nov-2026, 09:39 CDMX

### Ocupación y autoridad horaria

Se contrastó la rama de trabajo contra `main/data/horarios.json` (actualizado 2026-11-23; lectura de solo consulta). La política vigente tiene ventanas activas 06:30–07:30 y 16:30–18:00; 13:00–14:30 es una ventana reversible de prueba; 23:30 es el slot fijo del dato del día; 19:00 está retirado.

El snapshot `main/data/miniaturas_auditoria_2026-11-21.json` y `main/data/rehechos_2026-11-22.json` muestran para el 26-nov:

- 07:00 — `ZkrzVP6V5k8`, ya programado.
- 10:00 — el ID `2fQp5v9mQ6A` citado en el primer corte quedó NO_VERIFICADO; la fuente vigente main/data/rehechos_2026-11-22.json registra `7pzPfqRSagU`.
- 13:30 — `966qJDbIJp4`, ventana de prueba ocupada.
- 15:00 — el ID `4vQ2M2t8m3A` citado en el primer corte quedó NO_VERIFICADO; la fuente vigente main/data/rehechos_2026-11-22.json registra `MgHVHbeIVS0`.
- 17:00 — colisión de dos IDs: `JqlKsJOVmdE` y `-1DRh_qj7Bg`.
- 19:00 — `q5ZHy9oH6VM` sigue programado pese a que la franja fue retirada; no cancelar ni duplicar desde esta auditoría.
- 23:30 — `2026-11-23_dato-thanksgiving-washington`, `publishAt_utc=2026-11-27T05:30:00Z` (26-nov 23:30 CDMX).

Para Thanksgiving, `render.log` mide 89.56 s y 207 palabras; `qa_es.json` contiene 21/21 checks audiovisuales positivos, pero el storyboard tiene 6 escenas y no contiene `narrative_qa`. El log conserva una advertencia de safe area. El MP4 se referencia bajo `/workspace` y no está en el árbol GitHub; clasificar `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. Hay procesamiento y programación preexistentes: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.

La función de rotación marca una ventana completa como usada al encontrar un slot dentro de ella; por tanto, 17:00 consume la ventana 16:30–18:00 y no queda un 17:45 alternativo. 13:30 no es una franja histórica retirada: pertenece a la ventana de prueba 13:00–14:30 y está ocupada. Esta precisión supersede la frase anterior de este informe que la calificaba como histórica/legada.

Resultado: no existe slot libre verificable para crear storyboard el 26-nov. No se creó cola ni storyboard; no se canceló ni reenvió ningún paquete. `cola/estado/` continúa sin árbol/estado verificable: `RECEPCION_GROK_NO_CONFIRMADA`.

### Actions, issues y cambios posteriores

- El último commit de `main`, `1202ff151f04ce14127ed4f21bf03b0e067b3b1d`, solo añade la propuesta de end screens `propuesta_2026-11-26_08` con estado `pending_studio`; no demuestra aplicación en YouTube Studio.
- Semgrep en `main`, run `45836080617`: falló con 37 hallazgos bloqueantes; la carga SARIF se omitió por el fallo previo, así que no hay desglose verificable en ese run. Gitleaks y CodeQL finalizaron correctamente.
- `callback-aviso-delegaciones`, run `45845778090`: terminó correctamente. La búsqueda posterior conserva las dos issues abiertas existentes; no se observó issue nueva creada por ese run.
- La issue de reenvío/publicación externa sigue fuera de autorización. La auditoría narrativa de Cuásares sigue delegada a otra revisión; esta conversación no la sustituye.
- PR #3 continúa draft/no mergeable y su diff incluye `data/*.json`; no se fusionó.
- Los últimos commits de esta rama modifican documentación, no los 12 storyboards del lote 5–7-nov. Se conserva el resultado anterior de 2 PASS / 10 FAIL y 0/12 con estructura completa; no se repitió PASS ni se reescribió narración.



## Addendum de conciliación de reworks — 2026-11-26 09:58 CDMX

### Fuente de verdad y corrección de IDs

Se releyó main/data/rehechos_2026-11-22.json (blob 902a92411a516df4a3bf1046d8fec3ce1ee888c9) y se cruzó contra los nueve directorios de proyecto, sus metadata.json y render.log. La fuente contiene nueve reworks con ID de YouTube y programación privada→pública; TikTok y Facebook también figuran como programados. Esto acredita procesamiento/programación preexistente, no que cada publicación ya se haya hecho pública.

La línea del corte de las 09:39 que asignaba 2fQp5v9mQ6A a las 10:00 y 4vQ2M2t8m3A a las 15:00 no está respaldada por los archivos consultados ni por búsqueda de código en el repositorio. Se conserva como dato anterior NO_VERIFICADO. Los IDs respaldados por data/rehechos_2026-11-22.json son 7pzPfqRSagU y MgHVHbeIVS0.

| Fecha / slot CDMX | Proyecto main | YouTube ID | Estado registrado |
|---|---|---|---|
| 25-nov 10:00 | 2026-11-25_rehecho-nube-500-toneladas | 9RxTSifAcpo | private→public programado |
| 25-nov 15:00 | 2026-11-25_rehecho-barreleye-no-son-sus-ojos | 3rwo_sK1e18 | private→public programado |
| 26-nov 10:00 | 2026-11-25_rehecho-pan-refri-endurece | 7pzPfqRSagU | private→public programado |
| 26-nov 15:00 | 2026-11-25_rehecho-ratas-topo-ayudar-no-es-cuidar | MgHVHbeIVS0 | private→public programado |
| 27-nov 10:00 | 2026-11-25_rehecho-miel-su-unico-enemigo | p06UCGu0-Og | private→public programado |
| 27-nov 15:00 | 2026-11-25_rehecho-ola-azul-alarma-antirrobo | HKpani8TTeY | private→public programado |
| 28-nov 10:00 | 2026-11-25_rehecho-dunas-que-cantan-no-es-viento | 6VUxaJtqbF0 | private→public programado |
| 28-nov 15:00 | 2026-11-25_rehecho-escudo-jupiter-no-es-pared | Dx3lqkAb8Sc | private→public programado |
| 29-nov 10:00 | 2026-11-25_rehecho-dunkelflaute-sin-sol-ni-viento | m1FeS0mhfZ4 | private→public programado |

### Auditoría de los nueve expedientes

- Los nueve storyboards tienen 7 escenas, 215–229 palabras, 9:16, voz es-MX-JorgeNeural a +7% / -2Hz y cortinilla de 6 s. Los render.log miden entre 86.47 y 88.80 s, dentro del rango audiovisual 75–90 s; la suma nominal de los tiempos de escena más cortinilla en el JSON es 76 s.
- Los nueve contienen siete entradas SFX, pero no tienen prompt_base, mapa con coordenadas, dato/gráfico ni campo de ambiente por escena. Tampoco contienen narrative_qa; no hay evidencia de una revisión narrativa independiente registrada. Por contrato no se consideran PASS ni aptos para handoff.
- Los JSON incluyen referencias asset_filename / export.filename=capsula.mp4, pero las carpetas GitHub no contienen capsula.mp4 ni portada; los logs apuntan a rutas de /workspace. Clasificación para los nueve: MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO.
- Los nueve tienen ID, publishAt y programación de plataformas en el registro de reworks. Clasificación: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. No se intentó abrir Studio, publicar, cancelar ni reenviar.
- Ninguno tiene JSON plano en cola/entrada; están en proyectos/, no en una ruta que active el workflow. Clasificación: NOT_DISPATCHABLE. El árbol cola/estado devuelve 404; recepción Grok: RECEPCION_GROK_NO_CONFIRMADA.

### Conciliación del registro de publicaciones

main/data/publicaciones.json (blob a822459849571a443196e6a5b5d4ee73d109b1cd) contiene 62 registros y termina el 23-nov; no contiene los nueve IDs del archivo de reworks ni registros del 25–26 nov. La programación está registrada en data/rehechos_2026-11-22.json, pero no reconciliada en data/publicaciones.json. Se registra como discrepancia documental; ambos JSON permanecen intactos.

### Resultado

- Los slots 26-nov 10:00 y 15:00 están ocupados por los reworks Pan y Ratas; no se asigna un storyboard nuevo.
- Los demás reworks ocupan 25-nov 10:00/15:00, 27-nov 10:00/15:00, 28-nov 10:00/15:00 y 29-nov 10:00. No se duplican ni se cancelan.
- No se creó storyboard, cola, estado Grok ni medio. No se disparó workflow ni se envió payload.


### Estado procedimental de QA narrativo — nueve reworks main-only

La relectura de los nueve metadata.json y storyboard.json no encontró autor/modelo verificable, narrative_qa ni artefacto de auditoría independiente. No se realizó una pasada fría independiente de sus narraciones y no se inventan checks. Conforme al contrato, el estado efectivo de QA para cada uno es FAIL, score 0, critical_flags=["REVISION_INDEPENDIENTE_AUSENTE"]; review_basis y los siete checks quedan sin evaluación porque no existe una revisión separada acreditada. Esto es una clasificación procedimental, no una valoración del contenido narrativo. No se escribió narrative_qa en main ni se modificaron los storyboards.


---

## Addendum de auditoría · 2026-11-26 11:58 CDMX

### Cambios desde la última revisión

- La rama de trabajo sigue en `feature/capcot-video-discovery-continuity`; el último commit previo fue documental. No hubo cambios nuevos de storyboards en esa rama antes de esta ejecución.
- `main` recibió el paquete `2026-11-26_nbp-nanocables` mediante el commit `04ea20a18c130a76047c4aeacc8421163c69a7bb` (Grok CAPCOT, 10:37 CDMX). El mismo ID aparece en `proyectos/`, `cola/entrada/` y `salidas/`.

### NBP nanocables — auditoría de artefacto preexistente en main

- Programación de paquete: 26-nov, 17:15 CDMX. `salidas/<id>/` y `programacion.json` existen: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**.
- La cola es anidada (`cola/entrada/<id>/storyboard.json`); el workflow de la rama de trabajo selecciona únicamente `cola/entrada/*.json` plano. **NOT_DISPATCHABLE** con la ruta actual.
- `cola/estado/<id>.json` devuelve 404: **RECEPCION_GROK_NO_CONFIRMADA**. No existe marcador de recepción para NBP.
- No hay MP4, imágenes ni frames en `proyectos/`, `cola/entrada/` o `salidas/`: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. El storyboard declara `asset_filename` y `export.filename` sin archivos correspondientes.
- Revisión estructural estática: 124 palabras, 7 escenas, 67 s de escenas + 6 s de cortinilla = 73 s frente a 82 declarados; faltan `fecha_objetivo` y `slot_local`; no hay `narrative_qa`, `approved_assets` ni `export.render_status=NOT_GENERATED`. No apto.
- Lectura en frío de narración concatenada, separada de título/resumen/arco: **FAIL / 57**. Checks: pregunta central true; apertura in medias res false; progresión por escena true; transiciones causales true; giro científico explicado true; límite de evidencia explícito false; payoff cierre-apertura false. Flags: `APERTURA_NO_IN_MEDIAS_RES`, `LIMITE_DE_EVIDENCIA_AUSENTE`, `PAYOFF_CIERRE_APERTURA_DEBIL`. La revisión no se escribió en `main` porque esa rama es de solo lectura.
- NBP cae en la ventana de tarde 16:30–18:00 y se programa a 17:15; el registro de miniaturas ya muestra dos publicaciones a las 17:00. Es una **SOBREASIGNACION_DE_VENTANA_TARDE_EN_MAIN**, no un conflicto entre ramas: no hay paquete del 27-nov en `main` para el mismo slot 23:30.

### Handoffs y publicación preexistente

- El slot 26-nov 23:30 sigue ocupado por `2026-11-23_dato-thanksgiving-washington` en `main`; no crear otro paquete para ese slot.
- `cola/estado/` no existe en las dos ramas revisadas. Los marcadores de `handoffs/grok_inbox/` son solicitudes pendientes, no recibos; clasificar esos IDs como **RECEPCION_GROK_NO_CONFIRMADA**.
- El paquete robot del 09-nov ya tiene `capsula.mp4` y programación en `main`: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. Las dos series del 24-nov tienen marcadores pendientes, pero no estado de recepción; no se reenvían.
- No se encontró archivo `historial_youtube` en el árbol del repositorio. La auditoría de miniaturas sí muestra IDs antiguos aún programados para 26-nov (17:00 y 19:00); no se cancelan. El estado real en YouTube Studio no se pudo verificar desde los conectores disponibles.

### CI, Issues y PRs

- Run `45705919466` (`validar-kuroshio`) terminó SUCCESS, pero ejecutó solo `--structural-only`; no ejecutó `--check-doi`. DOI de Kuroshio sigue pendiente.
- En `main`, Semgrep `45864192131` falló con 37 hallazgos; el paso de subida SARIF quedó skipped y no se generó artefacto. Gitleaks `45864192057` terminó SUCCESS. CodeQL `45864191628` seguía queued al corte.
- Issue #11 continúa OPEN aunque conserva etiqueta `hecho`. PR #13 (auditoría externa de cuásares) y PR #14 (corrección narrativa) siguen abiertos; no se acepta ni se fusiona. PR #15 (rechazo de booleanos en coordenadas) sigue abierto y no mergeable. PR #3 continúa draft.
- Issue #16 sigue abierto: 17 MP4 no entregados y 10 resubidas TikTok solicitadas. No se enviaron archivos ni mensajes externos.

### Lote 5–7 nov y cola heredada

- Los 12 storyboards siguen sin cambios: 2 PASS narrativos (Venus 88; arena cantante 94) y 10 FAIL; estructura 0/12 apta. No hay entradas planas en `cola/entrada/` para ese lote. Las copias heredadas identificadas están en `cola/bloqueados/`; no se promovieron.
- En ambas ramas no hay `cola/estado/<id>.json` para confirmar recepción. No se crearon estados ni se asumió recepción por la presencia de marcadores.
- No se modificó ningún `data/*.json`, no se dispararon workflows, no se enviaron webhooks, no se crearon medios ni se publicó/programó nada desde esta ejecución.


### Corrección editorial de radar y storyboard · 2026-11-26 12:06 CDMX

- Se retiró del radar el candidato provisional de control de unidades motoras: el DOI citado no resolvió a la publicación y no se localizó una página primaria coincidente. El radar queda con cuatro candidatos primarios verificables.
- Se corrigió el storyboard `2026-11-27_dato-registros-intermareales-1950s`: las cuatro publicaciones en francés salieron entre 1956 y 1963 y describen observaciones de 1949–1957; el método se expresa como digitalización/OCR, corrección, traducción y cotejo con los originales. El guion queda en 174 palabras, 8 escenas y 84 s totales.
- La fuente primaria y el DOI aparecen en Nature Scientific Data; la verificación Crossref/doi.org sigue pendiente. El storyboard permanece en BORRADOR, sin QA, sin cola y sin medios; no es promovible.


---

## Registro de ejecución — 2026-11-26, 13:56 CDMX

### Storyboard del 27-nov

- Proyecto: `2026-11-27_dato-registros-intermareales-1950s`.
- Commit de actualización: `01f0815756ddbd8d2a7d408199b5e5925a28d6bb`; lectura de vuelta confirmada.
- Se corrigieron las fechas de creación de los tres datasets GBIF y se registró la verificación manual de DOI: SRC-001 Crossref `status=ok`; SRC-002/003/004 resueltos a GBIF.
- El storyboard permanece `BORRADOR`, `PROPUESTA_PENDIENTE_DE_GROK`; 8 escenas, 173 palabras, 84 s totales. Mapa con dos bounding boxes; tarjeta de datos 6,925 / 272. Sin medios ni placeholders.
- `narrative_qa=FAIL`, score 0, `REVISION_INDEPENDIENTE_AUSENTE`. No hubo lectura ciega separada; no es una evaluación narrativa sustantiva ni habilita promoción.
- No se ejecutaron el validador estructural Python ni `--check-doi`; la inspección estructural fue manual y la comprobación DOI fue manual por Crossref/resolvedor.
- `cola/estado/2026-11-27_dato-registros-intermareales-1950s.json` devuelve 404: registrar `RECEPCION_GROK_NO_CONFIRMADA`. No existe entrada plana en `cola/entrada`, copia anidada, carpeta de salida ni copia en bloqueados para este ID. Clasificación: `NOT_DISPATCHABLE`. No se creó ni modificó estado Grok.
- `main` no muestra proyecto, salida, publicación ni programación para 2026-11-27 23:30; por tanto no hay conflicto de slot entre ramas. El 2026-11-26 23:30 sí está ocupado por Thanksgiving. La ventana fija 23:30 está documentada en Plan Maestro/rotación, pero `data/horarios.json` no enumera esa ventana en su lista actual: discrepancia pendiente.
- No se obtuvo lectura de YouTube Studio ni de `historial_youtube`; no se puede descartar por completo un ID antiguo aún programado fuera del repositorio.
- `data/rotacion.json` y `data/temas_del_dia.json` de la rama de trabajo siguen con datos de octubre; no se modificaron.

### Lote canónico 5–7 nov: 12 IDs

Relectura de los 12 storyboards canónicos en `proyectos/`; no se repitió la auditoría narrativa porque sus narraciones no cambiaron desde la revisión registrada.

| ID | QA vigente | Score |
|---|---:|---:|
| `2026-11-05_kids-dia-en-venus` | PASS | 88 |
| `2026-11-05_comida-palomitas` | FAIL | 82 |
| `2026-11-05_inter-arboles-se-comunican` | FAIL | 78 |
| `2026-11-05_inter-rayo-globular` | FAIL | 81 |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL | 80 |
| `2026-11-06_comida-aguacate-negro` | FAIL | 79 |
| `2026-11-06_inter-ranas-congeladas` | FAIL | 83 |
| `2026-11-06_inter-arena-cantante` | PASS | 94 |
| `2026-11-07_kids-huesos-bebe` | FAIL | 82 |
| `2026-11-07_comida-hielo-caliente` | FAIL | 81 |
| `2026-11-07_inter-pulpo-suenos` | FAIL | 72 |
| `2026-11-07_inter-nubes-pesan` | FAIL | 78 |

Resultado: 2 PASS y 10 FAIL. Los 12 siguen estructuralmente incompletos: cada escena carece de los seis campos narrativos `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information` (42 o 48 campos ausentes por storyboard). Resultado estructural: 0/12 completos. Las copias de `cola/bloqueados` conservan nombres heredados distintos; no se renombraron ni movieron porque no son entradas planas activas y los 12 IDs canónicos están presentes en `proyectos/`.

### Cola, Grok, producción y CI

- `cola/entrada` de la rama de trabajo contiene una entrada anidada antigua del 09-nov; no hay JSON plano para el proyecto 27-nov.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` solo selecciona JSON planos en `cola/entrada/*.json`; el proyecto 27-nov no entra en su selector actual.
- No hay estado Grok individual para el proyecto; `RECEPCION_GROK_NO_CONFIRMADA`. No se envió payload ni se disparó el workflow de Grok.
- Issue #11 (auditoría independiente de cuásares) sigue OPEN; Issue #16 (17 MP4, 10 resubidas TikTok y Pancho EN) sigue OPEN, sin comentarios nuevos. No se enviaron medios ni enlaces externos.
- PR #3 sigue OPEN, draft y `mergeable=false`; el commit de esta ejecución dejó el run dinámico #45888959774 en cola. No se fusionó.
- En main: run dinámico #45888521806 SUCCESS; Gitleaks #45888521884 SUCCESS; Semgrep #45888521848 FAILURE. El fallo Semgrep mantiene 37 hallazgos reportados previamente; no se generó SARIF útil.

### Límites de ejecución de esta sesión

- No se modificó ningún `data/*.json`, `main`, secretos, permisos ni estados Grok.
- No se crearon medios, no se publicaron cápsulas, no se consumieron créditos y no se enviaron mensajes externos.


---

## Corte de auditoría — 2026-11-26, 15:14 CDMX

### Confirmación de briefs y referencias

- Este archivo ya existía; se actualiza con el corte posterior y se vuelve a leer desde GitHub.
- Referencias reconsultadas en `feature/capcot-video-discovery-continuity`: Plan Maestro, Receta, Guía de modelo externo, Flujo Externo, `docs/GROK_STATUS_CONTRACT.md`, plantilla storyboard, catálogo de generadores, `scripts/registro_editorial.py`, `scripts/procesar_cola.py`, `scripts/rotacion.py`, `scripts/estilos.json`, `.github/workflows/capcot-grok-dispatch.yml` y los JSON de `data/`.
- HEAD de feature antes de este commit de informe: `67cfc0e374ca2432d5b3fe8b2ebad56d3bf67738`. No se modificó `main`.

### Inventario completo de proyectos en feature

- Storyboards actuales: **91**.
- Proyectos con prefijo/fecha objetivo 2026-11-26 en feature: **0**.
- Borrador nuevo/futuro en feature: `2026-11-27_dato-registros-intermareales-1950s`, fuera de cola.
- El inventario completo de los 91 directorios con `proyectos/<id>/storyboard.json` se lista al final de este corte.

### Cola y dispatchabilidad

| Rama / paquete | Fecha objetivo y slot | Ruta comprobada | Dispatch |
|---|---|---|---|
| feature — robot orbital, 09-nov | 09-nov, slot histórico | `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/storyboard.json` | **NOT_DISPATCHABLE**: anidado; el workflow solo selecciona JSON planos |
| main — NBP nanocables | 26-nov, 17:15 CDMX | `cola/entrada/2026-11-26_nbp-nanocables/storyboard.json` | **NOT_DISPATCHABLE**: anidado y además en `main`, mientras el trigger push del workflow está limitado a feature |
| feature — 26-nov | 26-nov | No hay JSON en `cola/entrada/` | No hay paquete que despachar |

- En feature hay una entrada histórica anidada (robot orbital); en main hay una entrada anidada del día (NBP). No hay JSON plano de la fecha en ninguna rama.
- `.github/workflows/capcot-grok-dispatch.yml` usa el patrón `cola/entrada/*.json`; el selector manual usa `find cola/entrada -maxdepth 1 -type f -name '*.json'` y, para ID explícito, `cola/entrada/${id}.json`. Ninguna de las dos rutas encuentra los paquetes anidados.
- `scripts/procesar_cola.py` sí contempla entradas anidadas, pero su fecha por defecto es hoy y permite sobrescribirla con `--fecha`; no existe una prohibición absoluta contra seleccionar histórico manualmente.
- No se encontró ejecución de `capcot-grok-dispatch` entre los últimos 400 runs de Actions consultados. No hay log de dispatch que permita afirmar presencia o ausencia de `GROK_WEBHOOK_URL` o `GROK_WEBHOOK_TOKEN`.
- No existe ningún archivo en `cola/estado/` en feature ni en main. Para los storyboards de feature y el paquete NBP: **RECEPCION_GROK_NO_CONFIRMADA**.
- Main contiene tres markers en `handoffs/grok_inbox/` (robot 09-nov, serie cuántica y serie Thomas Harris 24-nov), todos con `status=pending`. No hay marker para NBP. Un marker pendiente no es recepción individual.
- Corrección del addendum 20-nov: el `scripts/registro_editorial.py` actual **sí** define `handoffs_grok_inbox()` y recorre `handoffs/grok_inbox/`; la afirmación anterior de que no lo recorría quedó obsoleta. El marker sigue sin sustituir `cola/estado/<project_id>.json`.

### Paquete NBP nanocables — main, fecha 26-nov

- Creación registrada por commit del 26-nov; paquete presente en `proyectos/`, `cola/entrada/` y `salidas/` (esta última solo con `metadata.json` y `programacion.json`). No hay `qa.json`, `publicacion.json`, `licencias.json`, MP4 ni frames.
- `programacion.json`: `publish_at=2026-11-26T23:15:00Z` = 17:15 CDMX; `privacy=private`; `estado=programado_paquete`; la nota indica que falta montar el MP4. No hay `video_id` ni evidencia de programación efectiva en plataforma.
- JSON del storyboard: 7 escenas; 124 palabras; duración declarada 82 s, pero las escenas suman 67 s y la cortinilla 6 s: **73 s efectivos**, por debajo de 75–90. `title` tiene 5 palabras; no existe `narrative_contract` ni `narrative_qa`.
- La apertura es una pregunta hipotética genérica, no una anomalía/acción ya en curso. No se realizó lectura narrativa independiente; no se asigna PASS.
- `source_ids` están presentes y el DOI está escrito, pero no hay estado de verificación DOI en el paquete. Voz, ambiente y SFX están presentes. No hay capa de mapa/gráfico ni `visual_identity.prompt_base` explícito (el identificador `risografia` coincide con el catálogo y su texto aparece embebido en los prompts de escena).
- Incumplimientos de preproducción: `asset_filename` en las siete escenas, `export.filename=capsula.mp4`, `approved_assets` ausente (no `[]`) y `export.render_status` ausente (no `NOT_GENERATED`). Los siete nombres de frame y el MP4 no existen en el árbol GitHub: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- `data/publicaciones.json`, `data/rotacion.json`, `data/temas_del_dia.json`, `data/estilos_usados.json` y `data/cola.json` de main no registran NBP. El paquete ya existe en main; no se creó una segunda copia en feature ni se intentó dispatch.

### Inventario de programación documentada para el 26-nov en main

Los siguientes son registros de programación/planificación, no nueve entradas de `cola/entrada/`. Se distinguen de la única entrada de cola (NBP).

| Slot CDMX | Paquete / tema | ID YouTube | Evidencia en repo | Estado de medios |
|---|---|---|---|---|
| 07:00 | Cyrus cylinder | `ZkrzVP6V5k8` | snapshot de miniaturas: `programado`; privacidad no consta | **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO** |
| 10:00 | Rehecho: pan de refrigerador | `7pzPfqRSagU` | `data/rehechos_2026-11-22.json`: private→public programado; TT/FB programados | ruta local en metadata/log, sin MP4 en GitHub |
| 13:30 | Museums public | `966qJDbIJp4` | snapshot de miniaturas: `programado`; privacidad no consta | **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO** |
| 15:00 | Rehecho: ratas topo | `MgHVHbeIVS0` | `data/rehechos_2026-11-22.json`: private→public programado; TT/FB programados | ruta local en metadata/log, sin MP4 en GitHub |
| 17:00 | Magallanes | `JqlKsJOVmdE` | snapshot de miniaturas: `programado`; privacidad no consta | **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO** |
| 17:00 | Plátano | `-1DRh_qj7Bg` | plan semanal y snapshot; privacidad private; QA declarado 77.3 s | ruta local, sin MP4 en GitHub |
| 17:15 | NBP nanocables | sin ID | `programacion.json`: private, `programado_paquete` | MP4 no montado / no verificado |
| 19:00 | Babylonian maps | `q5ZHy9oH6VM` | snapshot de miniaturas: `programado`; privacidad no consta | **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO** |
| 23:30 | Thanksgiving — `2026-11-23_dato-thanksgiving-washington` | sin ID | metadata y render.log; publishAt 05:30Z; QA audiovisual ES/EN 21/21 | rutas `/workspace`, sin MP4 en GitHub |

- Hay **9 registros para una capacidad declarada de 5**: cuatro por encima del límite. Los dos IDs de las 17:00 comparten `publishAt=2026-11-26T23:00:00Z`; el propio snapshot registra la colisión. NBP añade 17:15 dentro de la misma ventana de tarde.
- Los registros de Cyrus, Museums, Magallanes y Babylonian no tienen miniatura vertical ni MP4 en la caja auditada; tampoco se encontró blob de GitHub con los tamaños declarados. No se afirma que estén disponibles en plataforma: solo que el snapshot los etiqueta `programado`.
- Pan y Ratas tienen IDs, `publishAt` y estado de programación en el archivo de rehechos; los MP4 se referencian por rutas locales `/workspace`, no por archivos del repositorio.
- Thanksgiving tiene `publishAt_utc=2026-11-27T05:30:00Z`, 89.56 s ES / 87.03 s EN, 207 / 200 palabras y 21/21 checks audiovisuales por idioma. El render.log y QA no sustituyen el MP4; el archivo no está en GitHub. El pigeon que aparecía antes en el hueco del 26 fue movido al 30-nov; no es un segundo paquete del 26.
- La colisión de 17:00 y el exceso de capacidad no se corrigieron ni cancelaron.

### Reconciliación de horarios, temas, rotación y estilos

- `data/horarios.json` de main (actualizado 23-nov) solo contiene ventanas 06:30–07:30 y 16:30–18:00. Así, 07:00, 17:00 y 17:15 quedan dentro; 10:00, 13:30, 15:00, 19:00 y 23:30 no están autorizados por ese archivo.
- Feature conserva `data/horarios.json` de 09-nov con dos ventanas y un fijo 23:30; `scripts/rotacion.py` añade además una ventana experimental 13:00–14:30. Código, política de datos y main no son equivalentes. El contrato/Plan Maestro conserva referencias a cinco slots fijos, mientras el horario vigente de main muestra dos ventanas.
- Main: `publicaciones.json` 62 registros, último 24-nov; `rotacion.json` 39, último 21-nov; `temas_del_dia.json` 19, último 28-oct; `estilos_usados.json` 32, último proyecto 09-nov. Ninguno registra los nueve paquetes del 26-nov.
- Feature: publicaciones y rotación siguen cortadas al 31-oct; temas y estilos al 28-oct. `data/cola.json` de main está vacío; feature conserva solo un fallo histórico de 31-oct.
- `data/endscreens_rotacion.json` se actualizó 26-nov 14:05 y mantiene `pendiente_studio=true`; es rotación de pantallas finales, no registro de publicaciones. No se trató como prueba de programación de los nueve paquetes.

### Lote obligatorio 5–7 nov — revalidación estructural sin repetir QA narrativo

Los 12 IDs canónicos siguen coincidiendo con `data/horario_semana_2026-11-01_07.json` en fecha, slot y cesta. Título, tema y fuentes corresponden al horario; el storyboard canónico de árboles sigue siendo redes micorrícicas comunes y Karst et al. 2023, sin desajuste temático. Se conservaron los scores/statuses leídos de los JSON actuales; no se repitió lectura en frío donde ya existe QA.

| ID | narrative_qa del JSON |
|---|---:|
| 05-kids Venus | PASS 88 |
| 05-comida palomitas | FAIL 82 |
| 05-inter árboles | FAIL 78 |
| 05-inter rayo globular | FAIL 81 |
| 06-kids ballena azul | FAIL 80 |
| 06-comida aguacate negro | FAIL 79 |
| 06-inter ranas congeladas | FAIL 83 |
| 06-inter arena cantante | PASS 94 |
| 07-kids huesos bebé | FAIL 82 |
| 07-comida hielo caliente | FAIL 81 |
| 07-inter pulpo sueños | FAIL 72 |
| 07-inter nubes pesan | FAIL 78 |

- Estructura de los 12: 7–8 escenas; 169–221 palabras; 78 s de escenas + 6 s de cortinilla = 84 s; gancho/título 3–5 palabras; voz, source_ids y prompt_base presentes; ambiente presente en todas; 11/12 tienen capas mapa+dato (árboles no tiene capa mapa/gráfico).
- En 85 escenas faltan los seis campos `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information`: **510 ausencias**. SFX está vacío en **75/85** escenas. Resultado estructural: **0/12 aptos**.
- Los 12 conservan `approved_assets=[]`, `export.render_status=NOT_GENERATED` y no tienen `asset_filename` ni rutas de medios.
- Producción preexistente: `2026-11-07_comida-hielo-caliente` tiene QA audiovisual 89.83 s (21/21), YT `HSgrnejAcaI` privado con `publishAt=2026-11-11T19:30Z` (13:30 CDMX), TT `7706905447424347393` y FB `122109123507518983` registrados como publicados. La nota de publicaciones dice que el ID de YouTube ya no aparecía en el canal el 12-nov; discrepancia conservada.
- `2026-11-07_inter-nubes-pesan` tiene YT `4Qpl17Ts_vI` public con `publishAt=2026-11-12T13:00Z` (07:00 CDMX), TT `7705597569203768597` y FB `122109293529518983`. No existe carpeta `salidas/` ni MP4/QA en el árbol: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- No hay entrada activa de esos 12 IDs en `cola/entrada/`; las variantes históricas en `cola/bloqueados/` se conservaron. No se movió ni creó ninguna copia.

### Backlog interdiario — inventario completo de 91 storyboards

Distribución leída de los JSON actuales: **20 PASS, 28 FAIL, 42 sin narrative_qa y 1 PENDIENTE**. Los 42 sin QA no se promueven; los 28 FAIL y el PENDIENTE permanecen en proyectos.

**PASS (score del JSON):**
- 2026-11-01_red-electrica-pulso-minuto 89
- 2026-11-02_camaron-mantis 90
- 2026-11-04_cielo-azul-atardecer-rojo 94
- 2026-11-05_kids-dia-en-venus 88
- 2026-11-06_inter-arena-cantante 94
- 2026-11-09_dato-robot-ensambla-orbita 90
- 2026-11-10_comida-aprendizaje-sabor-nutriente 92
- 2026-11-10_dato-adn-sincroniza-flujo 91
- 2026-11-12_dato-pedorreta-chimpances 91
- 2026-11-13_dato-caracol-16-embriones 91
- 2026-11-14_dato-microplasticos-pantanal 88
- 2026-11-15_dato-dia-diapausa-lestes-sponsa 90
- 2026-11-16_dato-polen-desenreda-nanotubos 91
- 2026-11-17_dato-suelo-dos-relojes 89
- 2026-11-18_dato-kuroshio-puente-atmosferico 90
- 2026-11-19_dato-dia-luz-dos-manos-oro-poroso 91
- 2026-11-19_dato-estrella-dentro-de-estrella 90
- 2026-11-20_dato-dia-atlantico-humedad-sapropeles 91
- 2026-11-21_fentale-metano-sin-erupcion 90
- 2026-11-22_yubarta-genoma-soplo 90

**FAIL (score del JSON):**
- 2026-10-31_murcielagos-viroma-global 72
- 2026-10-31_sequias-energia-renovable 56
- 2026-10-31_smartpe-edicion-plantas 80
- 2026-11-01_dato-cambio-horario-corazon 84
- 2026-11-01_llorar-cebolla-quimica 79
- 2026-11-01_pulpo-tres-corazones 72
- 2026-11-02_comida-pan-duro 84
- 2026-11-05_comida-palomitas 82
- 2026-11-05_inter-arboles-se-comunican 78
- 2026-11-05_inter-rayo-globular 81
- 2026-11-06_kids-ballena-azul-corazon 80
- 2026-11-06_comida-aguacate-negro 79
- 2026-11-06_inter-ranas-congeladas 83
- 2026-11-07_kids-huesos-bebe 82
- 2026-11-07_comida-hielo-caliente 81
- 2026-11-07_inter-pulpo-suenos 72
- 2026-11-07_inter-nubes-pesan 78
- 2026-11-15_dato-quasar-pareja-cosmic-dawn 82
- 2026-11-18_dato-catorce-campos-hidrotermales 68
- 2026-11-20_dato-marea-cerebral-en-sueno 82
- 2026-11-21_homo-erectus-selva-tropical 83
- 2026-11-21_pulsar-gamma-reticulo 83
- 2026-11-22_bao-estrella-fusion-andromeda 84
- 2026-11-22_genes-estatura-etapas 72
- 2026-11-22_voyager-1-un-dia-luz 83
- 2026-11-23_supersequias-722-eventos 82
- 2026-11-23_tropical-biodiversity-turnover 82
- 2026-11-27_dato-registros-intermareales-1950s 0

**Sin `narrative_qa` (42):**
- 2026-10-24_abejas-bullying
- 2026-10-24_ideonella-pet
- 2026-10-24_osedax-comehuesos
- 2026-10-24_serpientes-que-ruedan
- 2026-10-25_ave-jurasica-sin-vuelo
- 2026-10-25_corales-contacto
- 2026-10-25_reina-olor
- 2026-10-25_sueno-electricidad-qom
- 2026-10-26_baffin-bay-ice-shelf
- 2026-10-26_catrina-posada-monerismo
- 2026-10-26_hongo-gente-diminuta
- 2026-10-26_papel-picado-dia-muertos
- 2026-10-26_papel-picado-dia-muertos_parte2
- 2026-10-26_pimiento-verde-rojo
- 2026-10-27_cempasuchil-ciencia
- 2026-10-27_corneja-decision-rapida
- 2026-10-27_ddm-parte3-pomuch
- 2026-10-27_familia-ajolote
- 2026-10-27_kids-serpiente-voladora
- 2026-10-27_noct-anfibio-marino
- 2026-10-28_ddm-parte4-templo-mayor
- 2026-10-28_familia-voyager-disco-oro
- 2026-10-28_kids-titanoboa
- 2026-10-28_monarca-almas
- 2026-10-28_mosquito-fruitless-audicion
- 2026-10-28_noct-lince-milanos
- 2026-10-28_pan-de-muerto-huesos
- 2026-10-29_juno-choque-proa
- 2026-10-29_muralismo-cu
- 2026-10-30_arqueas-origen-eucariotas
- 2026-10-30_kromdraai-primera-fecha
- 2026-10-31_pardelas-jetlag-solar
- 2026-11-03_dato-polvo-africano-microbios
- 2026-11-03_kids-leche-enchilado
- 2026-11-xx_kids-flamencos-rosas_RESPALDO
- demo-001
- guiones_lote_01
- lote01-01-el-nino
- lote01-02-petroleo
- lote01-03-balon-curva
- lote01-04-tardigrado
- lote01-05-chicxulub

**PENDIENTE (sin score PASS):**
- `2026-11-04_dato-polvo-atrapa-oro`

- Caso hidrotermales: `2026-11-18_dato-catorce-campos-hidrotermales` permanece FAIL 68; su `ESTADO_EJECUCION.md` ya dice `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`.
- Kuroshio: narrative_qa PASS 90; CI estructural posterior #45705919466 success, pero sin `--check-doi`; DOI pendiente. Su estado documental se actualizó para registrar ese run y conservar el bloqueo.
- Se revisaron los ocho `ESTADO_EJECUCION.md` presentes en proyectos. No se encontró otro estado `PREPARADO` que contradiga la compuerta. No se modificaron los storyboards ni los estados Grok.
- El nuevo proyecto 27-nov tiene `narrative_qa.status=FAIL`, score 0, `review_basis=lectura_en_frio_solo_narracion`, flag `REVISION_INDEPENDIENTE_AUSENTE`; no se repitió lectura narrativa. Estructura: 8 escenas, duración declarada 84 s con cortinilla de 6 s, sin assets, `approved_assets=[]`, `render_status=NOT_GENERATED`. No hay paquete en cola ni slot homólogo en main para 27-nov 23:30.

**Inventario completo de rutas `proyectos/<id>/storyboard.json` (91):**
```text
- 2026-10-24_abejas-bullying
- 2026-10-24_ideonella-pet
- 2026-10-24_osedax-comehuesos
- 2026-10-24_serpientes-que-ruedan
- 2026-10-25_ave-jurasica-sin-vuelo
- 2026-10-25_corales-contacto
- 2026-10-25_reina-olor
- 2026-10-25_sueno-electricidad-qom
- 2026-10-26_baffin-bay-ice-shelf
- 2026-10-26_catrina-posada-monerismo
- 2026-10-26_hongo-gente-diminuta
- 2026-10-26_papel-picado-dia-muertos
- 2026-10-26_papel-picado-dia-muertos_parte2
- 2026-10-26_pimiento-verde-rojo
- 2026-10-27_cempasuchil-ciencia
- 2026-10-27_corneja-decision-rapida
- 2026-10-27_ddm-parte3-pomuch
- 2026-10-27_familia-ajolote
- 2026-10-27_kids-serpiente-voladora
- 2026-10-27_noct-anfibio-marino
- 2026-10-28_ddm-parte4-templo-mayor
- 2026-10-28_familia-voyager-disco-oro
- 2026-10-28_kids-titanoboa
- 2026-10-28_monarca-almas
- 2026-10-28_mosquito-fruitless-audicion
- 2026-10-28_noct-lince-milanos
- 2026-10-28_pan-de-muerto-huesos
- 2026-10-29_juno-choque-proa
- 2026-10-29_muralismo-cu
- 2026-10-30_arqueas-origen-eucariotas
- 2026-10-30_kromdraai-primera-fecha
- 2026-10-31_murcielagos-viroma-global
- 2026-10-31_pardelas-jetlag-solar
- 2026-10-31_sequias-energia-renovable
- 2026-10-31_smartpe-edicion-plantas
- 2026-11-01_dato-cambio-horario-corazon
- 2026-11-01_llorar-cebolla-quimica
- 2026-11-01_pulpo-tres-corazones
- 2026-11-01_red-electrica-pulso-minuto
- 2026-11-02_camaron-mantis
- 2026-11-02_comida-pan-duro
- 2026-11-03_dato-polvo-africano-microbios
- 2026-11-03_kids-leche-enchilado
- 2026-11-04_cielo-azul-atardecer-rojo
- 2026-11-04_dato-polvo-atrapa-oro
- 2026-11-05_comida-palomitas
- 2026-11-05_inter-arboles-se-comunican
- 2026-11-05_inter-rayo-globular
- 2026-11-05_kids-dia-en-venus
- 2026-11-06_comida-aguacate-negro
- 2026-11-06_inter-arena-cantante
- 2026-11-06_inter-ranas-congeladas
- 2026-11-06_kids-ballena-azul-corazon
- 2026-11-07_comida-hielo-caliente
- 2026-11-07_inter-nubes-pesan
- 2026-11-07_inter-pulpo-suenos
- 2026-11-07_kids-huesos-bebe
- 2026-11-09_dato-robot-ensambla-orbita
- 2026-11-10_comida-aprendizaje-sabor-nutriente
- 2026-11-10_dato-adn-sincroniza-flujo
- 2026-11-12_dato-pedorreta-chimpances
- 2026-11-13_dato-caracol-16-embriones
- 2026-11-14_dato-microplasticos-pantanal
- 2026-11-15_dato-dia-diapausa-lestes-sponsa
- 2026-11-15_dato-quasar-pareja-cosmic-dawn
- 2026-11-16_dato-polen-desenreda-nanotubos
- 2026-11-17_dato-suelo-dos-relojes
- 2026-11-18_dato-catorce-campos-hidrotermales
- 2026-11-18_dato-kuroshio-puente-atmosferico
- 2026-11-19_dato-dia-luz-dos-manos-oro-poroso
- 2026-11-19_dato-estrella-dentro-de-estrella
- 2026-11-20_dato-dia-atlantico-humedad-sapropeles
- 2026-11-20_dato-marea-cerebral-en-sueno
- 2026-11-21_fentale-metano-sin-erupcion
- 2026-11-21_homo-erectus-selva-tropical
- 2026-11-21_pulsar-gamma-reticulo
- 2026-11-22_bao-estrella-fusion-andromeda
- 2026-11-22_genes-estatura-etapas
- 2026-11-22_voyager-1-un-dia-luz
- 2026-11-22_yubarta-genoma-soplo
- 2026-11-23_supersequias-722-eventos
- 2026-11-23_tropical-biodiversity-turnover
- 2026-11-27_dato-registros-intermareales-1950s
- 2026-11-xx_kids-flamencos-rosas_RESPALDO
- demo-001
- guiones_lote_01
- lote01-01-el-nino
- lote01-02-petroleo
- lote01-03-balon-curva
- lote01-04-tardigrado
- lote01-05-chicxulub
```

### Pull requests y Actions

- PR #3: OPEN/DRAFT, base main, head feature, `mergeable=false`, 719 archivos cambiados; incluye 5 workflows, 4 scripts, 13 JSON de data, 62 storyboards de proyectos, 5 entradas de cola y 28 storyboards bloqueados. No se integró.
- PR #4: OPEN, base feature; modifica estado del robot y afirma frames generados en chat Grok, pero no están subidos al repositorio. No se integró.
- PR #6: OPEN, base feature; añade supervisor con `secrets: inherit` y disparador amplio. No se integró.
- PR #13: OPEN, base main; auditoría documental de cuásares, no aprobación.
- PR #14: OPEN, base main; añade `asset_filename` a las ocho escenas de Quasar, conserva narrative_qa FAIL/82 y no acredita `--check-doi`. Rechazado para preproducción.
- PR #15: OPEN, base feature; cambios de validador/coordenadas y tests, no integrados ni usados como validación de los storyboards actuales.
- El QA audiovisual de main todavía acepta 60–120 s; feature propone 75–90 s en `scripts/qa_capsula.py`. La versión estricta no está integrada en main. Hielo 89.83 s y Thanksgiving ES 89.56 s sí quedan dentro de 75–90.
- Actions: `45896512901` (Trabajador de cola, main, 26-nov 15:12:30 CDMX) SUCCESS; no es el dispatch de Grok. El endpoint de logs no devolvió stdout legible.
- Semgrep `45888521848` FAILURE en el paso `Run semgrep scan --config p/default --config p/python --sarif --output semgrep.sarif --error`; el endpoint de logs no devolvió stderr legible, por lo que no se inventa mensaje literal.
- Kuroshio: run más reciente `45705919466`, commit `331cd68451a77894004866151bfa0474b32da97c`, comando `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`, conclusión success. No incluyó `--check-doi`; DOI sigue pendiente.
- No se encontró run de `capcot-grok-dispatch` entre los últimos 400 runs consultados.

### Límites y acciones de este corte

- Sin runtime del repositorio; revisión estática y conteos reproducidos desde los JSON de GitHub. No se ejecutó el validador local.
- No se revisaron APIs: no apareció un cambio oficial nuevo que justificara esa revisión.
- Únicas escrituras de esta auditoría: este brief y la corrección documental de `ESTADO_EJECUCION.md` de Kuroshio. No se modificaron `data/*.json`, storyboards, cola, `cola/estado/`, workflows, secretos, permisos ni `main`.
- No se dispararon workflows, no se enviaron payloads, no se generaron medios, no se publicó y no se consumieron créditos.


### Trazabilidad de creación, objetivo y slot — paquetes del 26-nov

- `2026-11-26_nbp-nanocables`: creado el 26-nov a las 10:37:18 CDMX por commit `04ea20a18c130a76047c4aeacc8421163c69a7bb`; fecha objetivo 26-nov; slot 17:15.
- `2026-11-23_dato-thanksgiving-washington`: proyecto registrado el 23-nov; fecha objetivo 26-nov; slot 23:30. El render.log/QA pertenecen a ese paquete preexistente, no a una entrada nueva de cola.
- Rehechos Pan y Ratas: registros en `data/rehechos_2026-11-22.json` (22-nov); proyectos con prefijo 25-nov; fecha objetivo 26-nov; slots 10:00 y 15:00 respectivamente.
- Plátano: planificación registrada en `docs/briefs/produccion_2026-11-23_28/plan_semana.json` (23-nov); fecha objetivo 26-nov; slot 17:00.
- Cyrus cylinder, Museums public, Magallanes y Babylonian maps: snapshot de miniaturas `data/miniaturas_auditoria_2026-11-21.json` (21-nov); fecha objetivo 26-nov; slots 07:00, 13:30, 17:00 y 19:00 respectivamente.
- Thanksgiving es el paquete que ocupa el 26-nov 23:30 en `tools/animales_2026-11-23/specs_animales.py`; la paloma originalmente prevista para ese hueco fue movida al 30-nov, no es un segundo paquete del 26.
- `2026-11-27_dato-registros-intermareales-1950s`: creado el 26-nov a las 14:12:10 CDMX por commit `a801612f239004d71f56d27cac1864c0b138f656`; fecha objetivo 27-nov; slot 23:30. No se confunde la fecha de creación con la fecha objetivo.
- Para los 12 IDs del lote 5–7-nov se cotejaron `fecha_objetivo`, `slot_local` y `slot_cesta` con el horario. El prefijo del ID coincide con la fecha objetivo, pero no se usa como sustituto de un timestamp de creación por commit.
- No hay archivo independiente `historial_youtube` en el árbol actual; los IDs históricos se cotejaron en `data/publicaciones.json`, `data/miniaturas_auditoria_2026-11-21.json` y los paquetes de `salidas/`.


---

## Actualización del operador — 2026-11-26, 16:04 CDMX

### Trabajo ejecutado y verificado

- Se corrigió el mapa de `2026-11-27_dato-registros-intermareales-1950s`: se añadió la extensión GBIF IPT del dataset de cirrípedos `10.15468/jnzaw3` (35.472, -9.466, 43.723, -1.785). La escena 3 ahora cita los tres datasets y distingue bounding boxes publicados de estaciones puntuales.
- Lectura de vuelta: commit `d57f1b9cf4c70e7539e3b6ca50aaaa3c118d37b8`, blob `8ad79510f5b037b6455187dae97ac357394a6291`.
- La narración no cambió: 174 palabras, 8 escenas, 78 s + 6 s de cortinilla = 84 s. Voz, prompt base y estilo siguen coincidiendo con el catálogo. `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin nombres ni rutas de medios.
- `narrative_qa` permanece `FAIL/0`, `REVISION_INDEPENDIENTE_AUSENTE`. No se repitió ni se presentó como evaluación sustantiva. No existe `ESTADO_EJECUCION.md` independiente para este proyecto.

### Dispatch, slot y producción previa

- Proyecto 27-nov: no hay copia en `cola/entrada/`, no hay marker en `handoffs/grok_inbox/`, y `cola/estado/2026-11-27_dato-registros-intermareales-1950s.json` devuelve 404. Registrar `RECEPCION_GROK_NO_CONFIRMADA`; clasificación `NOT_DISPATCHABLE`.
- `.github/workflows/capcot-grok-dispatch.yml` filtra únicamente `cola/entrada/*.json` (profundidad plana). El proyecto sigue en `proyectos/`; no se envió payload ni se disparó workflow.
- En main no hay proyecto, publicación ni rotación para 27-nov 23:30. `data/rehechos_2026-11-22.json` contiene 27-nov 10:00 y 15:00, no 23:30. El historial independiente de YouTube no existe en el árbol; no se afirma que el slot esté libre en Studio.
- El paquete Thanksgiving 26-nov 23:30 permanece preexistente en main; no es el slot del 27-nov. NBP 26-nov 17:15 conserva programación preexistente y no se redispatcha.
- La auditoría del 26-nov 15:14 ya registró 9 programaciones del día, la colisión 17:00 y la sobreasignación de la tarde. No se alteró programación ni se canceló ningún ID.

### Actions y PR

- Worker main `45896512901`: SUCCESS, sin trabajo en cola; no equivale a dispatch de Grok.
- Kuroshio `45898334232`: SUCCESS, pero valida solo `2026-11-18_dato-kuroshio-puente-atmosferico`; no valida el proyecto 27-nov ni ejecuta `--check-doi`.
- No se encontró ejecución de `capcot-grok-dispatch`.
- PR #3: OPEN/DRAFT, `mergeable=false`, 719 archivos; no integrar.
- PR #15: OPEN, `mergeable=false`; `Semgrep OSS` success, `semgrep` failure con 37 hallazgos bloqueantes en 1,277 archivos; no integrar ni atribuir pruebas a la rama activa.
- Issues #11 y #16 continúan abiertos. El lote obligatorio 5–7 nov mantiene 2 PASS (Venus 88, Arena 94), 10 FAIL y 0/12 estructuralmente aptos. No se modificaron sus storyboards.

### Investigación y límites de lectura

Se intentaron los endpoints de RSS definidos en `scripts/tendencias.py` y Google Trends RSS México. La interfaz devolvió `400 Unsupported content-type` para feeds XML/RSS, `404 Not Found` para ESA Space Science RSS y `URL ... is not accessible via this tool` para EurekAlert, SINC y Google Trends. Google Trends HTML tampoco fue accesible en esta relectura. Estos errores describen la herramienta de lectura; no prueban que todos los feeds estén caídos. No se simuló una ejecución local de `scripts/tendencias.py`.

Crossref REST y `doi.org` devolvieron `URL ... is not accessible via this tool`. Se conserva la verificación Crossref histórica `status=ok` del corte de 13:56; no se afirma una revalidación nueva. El validador estructural real no se ejecutó para el storyboard del 27-nov.

### Integridad

No se modificaron `data/*.json`, main, secretos, permisos, estados Grok, workflows, PRs ni publicaciones. No hubo dispatch, payload externo, generación de medios ni consumo de créditos.


---

## Corrección de conflicto entre ramas — 2026-11-26, 16:18 CDMX

**Corrección del apartado de slots de las 16:04:** la consulta de `proyectos/`, `data/publicaciones.json` y `data/rotacion.json` no bastó para declarar libre el 27-nov 23:30. Una inspección adicional de `main:tools/animales_2026-11-23/specs_animales.py` encontró `SPECS["stubbs"]` con `hueco="2026-11-27 23:30 (America/Mexico_City)"`. Es una asignación explícita de preproducción en main; no demuestra publicación efectiva, pero sí reserva editorial para evitar duplicación.

- Clasificación del storyboard intermareal en feature: `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `NOT_DISPATCHABLE`.
- El borrador permanece en `proyectos/`; no se crea entrada de cola ni se altera main.
- `validation_notes` del storyboard se actualizó y leyó de vuelta en commit `f52be5584de9018e6d5439c3835ee9afdb3dc4fa`, blob `a486715cefbaf06252bb1956234dde245d33c8ea`.
- La narración, `narrative_qa=FAIL/0`, fecha y slot no se modificaron.
- La misma especificación de main reserva también 28, 29 y 30-nov a las 23:30; no se reasigna el borrador a otra fecha sin nueva conciliación.
- La nota de las 16:04 que describía el slot como libre en main queda supersedida por esta corrección.
