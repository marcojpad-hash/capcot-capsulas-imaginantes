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
