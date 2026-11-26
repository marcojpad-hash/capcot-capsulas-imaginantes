# Control de cola CAPCOT — 2026-11-26

**Corte:** 2026-11-26, 02:14 America/Mexico_City  
**Rama de trabajo:** feature/capcot-video-discovery-continuity  
**HEAD al cierre:** cd9ffa5e0fa4f498242b586347c2584923089d04  
**Regla:** solo lectura en main; sin dispatch, payload, publicación, programación, generación de medios ni consumo de créditos.

## 1. Ramas, CI y contratos

- La rama feature está divergida de main: 594 commits exclusivos de feature y 1,428 commits exclusivos de main. PR #3 sigue abierto y GitHub lo reporta mergeable=false. No fusionar ni sincronizar por fuerza.
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

## 6. Resultado del corte

- **EJECUTADO Y VERIFICADO:** QA narrativo frío de Quasar, registrado y leído de vuelta; radar del 26-nov creado en docs/briefs/2026-11-26_RADAR_CAPCOT.md; este control creado en docs/briefs/2026-11-26_CONTROL_COLA.md.
- **NOT_DISPATCHABLE:** todos los proyectos sin JSON plano de entrada y sin estado Grok individual.
- **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR:** paquete Robot/órbita, por MP4, QA y programación en main.
- **PENDIENTE:** resolver la ocupación real del slot 23:30 con historial/Studio vigente; ejecutar el validador estructural real y DOI/Crossref en los expedientes que superen QA; corregir los campos estructurales de los 12 expedientes antiguos solo cuando se pueda hacer sin reescribir claims ni decisiones narrativas.
