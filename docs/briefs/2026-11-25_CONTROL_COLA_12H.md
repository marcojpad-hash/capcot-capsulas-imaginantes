# Control de cola CAPCOT — 25 de noviembre de 2026, 12:03 CDMX

## Alcance y fuentes

Corte de solo lectura sobre `feature/capcot-video-discovery-continuity`, `main`, briefs, inventario, storyboards, `data/*.json`, scripts, plantillas, flujo Grok, Issues, PR y Actions. No se modificaron `main`, `data/*.json`, cola, estados Grok, programación, workflows, secretos, permisos ni medios.

- HEAD feature: `cd29e0e294ce6b174bdcf3716fde1962c906e6ed`.
- HEAD main observado: `7e363e4eb5b56d39a71052da3257e345d510d3c0`.
- El commit más reciente de feature solo actualiza el radar; no cambia storyboards. Se conserva el resultado narrativo del corte 10H: 2 PASS y 10 FAIL en el lote de 12 IDs del 5–7 nov; no se repite ningún PASS porque las narraciones no cambiaron.
- El inventario `ajustes_entre_modelos/PARA_CHATGPT_5-7nov_PASS_auditor.md` fue releído.

## Radar y tendencias

- La shortlist vigente del radar 10:02 es: Varroa/hipoxia, brazo de Norma, complejidad del plancton, Pantoea asociada a quinoa y Europa Clipper. Europa Clipper sustituyó al saltamontes acuático; permanece como candidato, no seleccionado.
- El addendum de 08:30 registra respuestas `status=ok` de Crossref/resolvedor para los cuatro primeros DOI. La revalidación 10:02 no pudo repetir el acceso, pero conserva esa verificación previa; la tabla inicial del radar aún muestra estados pendientes y debe leerse como supersedida por los addenda posteriores.
- En este corte, Crossref REST y `doi.org` no entregaron una respuesta verificable desde el lector disponible. No se invalida la evidencia positiva de 08:30 ni se crea una verificación nueva.
- Reintento de RSS/Google Trends: no se obtuvo XML utilizable. El respaldo HTML oficial de Google Trends México mostró 232 tendencias totales y 25 visibles; las señales visibles no identificaron un hallazgo científico con fuente primaria suficiente. No se seleccionó tema por tendencia sola.
- No se creó storyboard: la ocupación ya era 7/5 para el 25–28 nov y 5/5 para el 29 nov; el paquete nuevo de main eleva el 25 nov a, al menos, 8/5.

## Proyecto nuevo detectado solo en main

ID: `2026-11-25_react-bacterias-anticancer`.

### Estado de ruta y despacho

- El storyboard aparece en `main/proyectos/<id>/storyboard.json` y también en `main/cola/entrada/<id>/storyboard.json`, dentro de un directorio anidado.
- No aparece en la rama activa feature.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` de feature filtra `cola/entrada/*.json` y busca archivos con `find ... -maxdepth 1 -type f -name '*.json'`. La ruta anidada no satisface ese selector ni activa el filtro de paths. `scripts/procesar_cola.py` admite rutas anidadas, pero el workflow de despacho no las selecciona.
- No existe `cola/estado/<id>.json`: **RECEPCION_GROK_NO_CONFIRMADA**.
- No hay salida, carpeta de bloqueados ni medios de escena en el árbol para este ID. Los nombres `asset_filename` y `export.filename` son referencias, no prueba de medios existentes: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- `programacion.json` registra el paquete para el 25 nov a las 17:00 CDMX (`publishAt=2026-11-25T23:00:00Z`). El mismo instante ya está ocupado en main por `L6ggmPAwBOA`: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** y **CONFLICTO_DE_SLOT_EN_MAIN**. No hay un candidato equivalente en feature; por eso no se etiqueta como conflicto entre ramas.
- Clasificación: **NOT_DISPATCHABLE**. No se promueve ni se redispatcha.

### Auditoría estructural estática

No se ejecutó `validar_storyboard.py --check-doi`; esta es inspección estática del JSON, no una ejecución del validador.

- Correcto: `language=es-MX`, `aspect_ratio=9:16`, objetivo declarado de 85 s, voz `es-MX-JorgeNeural` con +7% y -2 Hz, `prompt_base` de `linea_fina` incorporado, ambiente y SFX por escena, cortinilla de 6 s y cierre hablado exacto.
- Incumplimientos: 6 escenas (se exigen 7–9); 102 palabras (170–235); 60 s de escenas + 6 s de cortinilla = 66 s (75–90); gancho inicial de 11 palabras (máximo 6); no hay mapa con coordenadas ni dato/gráfico.
- El JSON contiene `asset_filename` en las seis escenas y `export.filename`; ambos están prohibidos en preproducción. Faltan `approved_assets=[]`, `export.render_status=NOT_GENERATED`, `publicacion.status=PENDIENTE_DECISION_GROK`, `narrative_contract`, `narrative_qa`, `fuentes.md` y `ESTADO_EJECUCION.md`.
- No existe una revisión independiente en frío registrada. Resultado de auditoría narrativa conforme al contrato: **FAIL, score 0, critical_flags=[REVISION_INDEPENDIENTE_AUSENTE]**. No se reescribió narración ni claims.

### Fuente y afirmaciones

- El DOI `10.1126/science.aee2641` y los metadatos del artículo de Science quedan corroborados por el registro PubMed y la nota institucional de University of Michigan (19-nov-2026). Crossref/resolvedor no se pudo completar desde este corte.
- La fuente accesible respalda que DnrV reduce especies reactivas de oxígeno y favorece la catálisis P450; la nota institucional respalda la familia REACT de más de 40,000 proteínas. La afirmación cuantitativa de aceleración de cuatro veces no quedó localizada en el abstract ni en la nota institucional consultada: **PENDING_SOURCE para esa cifra**.
- La fuente no se eleva a compuerta DOI PASS sin resolver Crossref/DOI y sin documentar la cifra específica.

## Rotación, CI y backlog

- `data/horarios.json` refleja ventanas activas distintas de las cinco ventanas codificadas en `scripts/rotacion.py`. El código conserva ventanas de 07–09, 13–15, 16–18, 18–21 y 23–24, mientras la programación vigente documentada concentra ventanas en 06:30–07:30 y 16:30–18:00, además del slot de dato-día 23:30. No se cambió la configuración: requiere decisión editorial, no corrección automática.
- Main: Gitleaks SUCCESS; Semgrep FAILURE con 37 hallazgos bloqueantes (361 reglas, 1,260 archivos objetivo; 37 archivos grandes omitidos). El SARIF no se subió tras el fallo.
- Feature: no hay ejecución nueva de CI posterior al commit de radar. No se dispararon workflows.
- PR #3 sigue OPEN/DRAFT; PR #13 y #14 siguen abiertos, sin merge; issue #11 continúa abierto aunque conserve etiqueta `hecho`. PR #15 sigue OPEN y `mergeable=false`; tiene Semgrep OSS SUCCESS y Semgrep FAILURE, sin prueba funcional verificada. No se fusionó ni cerró nada.
- Issue #16 mantiene tareas externas de MP4/TikTok/Pancho EN y bloqueo del chat Grok. No se enviaron mensajes, no se subieron archivos y no se publicó ni programó nada.

## Resultado del corte

**EJECUTADO:** relectura de inventario, radar, scripts, plantillas, datos de rotación, workflow, Issues/PR/Actions y cruce de main para el paquete nuevo; verificación bibliográfica del artículo por PubMed/University of Michigan y revisión de la afirmación de cuatro veces.

**VERIFICADO:** no hay slot autorizado; el paquete nuevo de main no es dispatchable, tiene conflicto de 17:00, no tiene recepción Grok confirmada ni medios verificables y falla estructura/narrativa. El backlog narrativo previo no cambió.

**PENDIENTE:** resolver la cifra de cuatro veces con fuente primaria; reconciliar las ventanas de rotación con la programación vigente; resolver los 37 hallazgos Semgrep; obtener revisión independiente y estructura válida para cualquier paquete nuevo; completar las tareas externas de issue #16 solo cuando exista autorización y acceso.

No se generaron medios, no se promovió ninguna entrada y no se modificó programación ni datos.
