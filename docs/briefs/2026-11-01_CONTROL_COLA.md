# Control de cola CAPCOT — 2026-11-01

**Corte:** 2026-11-01, 18:00 CDMX  
**Rama:** feature/capcot-video-discovery-continuity  
**Base revisada:** commit 277a12b4253f3bbbad37f0b9a58812a58053677e  
**Alcance:** auditoría de briefs, borradores, salidas, rotación, cola, dispatch, estados y Actions. Solo lectura salvo QA narrativo y correcciones mecánicas documentadas abajo.

## Resultado ejecutivo

- Se encontraron **4 borradores** en proyectos para la fecha 2026-11-01 y **0 entradas de cola** del día.
- QA narrativo en frío: dato cambio-horario **PASS 87**; red eléctrica **PASS 89**; cebolla **FAIL 79**; pulpo **FAIL 72**.
- Los cuatro borradores están en proyectos/, no en cola/entrada/. Por ruta, los cuatro son **NOT_DISPATCHABLE**.
- El slot 23:30 sigue como TBD en el calendario canónico. Hay dos candidatos distintos: cambio de horario/corazón, pedido en el brief diario, y red eléctrica, recomendado en el radar. No existe selección de Grok registrada.
- No existe cola/estado para ninguno de los cuatro borradores ni para los cinco paquetes programados del 1-nov. En todos los casos corresponde **RECEPCION_GROK_NO_CONFIRMADA**.
- Las ejecuciones recientes del workflow de dispatch fallaron. El último error observado es literal: `Falta configurar GROK_WEBHOOK_URL.`; también falta configurar `GROK_WEBHOOK_TOKEN`.
- No se ejecutó el validador Python ni helpers: no había checkout/runtime local accesible. La revisión estructural fue estática y se identifica como tal.
- No se generaron medios, no se publicaron ni programaron piezas, no se consumieron créditos, no se modificaron data/*.json, main, workflows, secretos ni estados Grok.

## 1. Briefs y autoridad documental

Se relevaron el Contrato Operativo Unificado, Plan Maestro, Receta, Guía, Flujo Externo, contrato de estado Grok, QA narrativo en frío, plantillas, catálogo visual, línea editorial, continuidad audiovisual, protocolo de handoff y briefs del día.

### Briefs que afectan al 1-nov

1. **ajustes_entre_modelos/PARA_CHATGPT_dato_del_dia.md** pide el dato del día para el slot 23:30 y define el candidato cambio de horario/corazón, basado en Sandhu et al. (2014), con ID `2026-11-01_dato-cambio-horario-corazon`.
2. **docs/briefs/2026-11-01_RADAR_CAPCOT.md**, corte 14:20, recomienda como candidato principal el estudio de las oscilaciones de un minuto en redes eléctricas. Su storyboard está en proyectos/ como `2026-11-01_red-electrica-pulso-minuto`.
3. **ajustes_entre_modelos/PARA_CHATGPT_hasta_08nov.md** mantiene el slot diario de 23:30 como noticia del mismo día o de las últimas 48 horas y marca como no tocar los cinco paquetes ya programados.
4. **data/horario_semana_2026-11-01_07.json** conserva el slot 23:30 como `2026-11-01_dato-TBD-news`, estado `pendiente_dato_dia`. No incorpora ninguno de los dos candidatos.
5. **salidas/_ops/2026-11-01_cobertura_hasta_fin_semana.md** todavía describe el 23:30 como hueco ChatGPT→Grok. Hay un borrador nuevo en proyectos/, pero no una entrada de cola ni selección.
6. **salidas/_ops/2026-11-01_swap_arqueas_tiburon.md** registra el cambio de arqueas por tiburón en el slot 19:00. Ese cambio no quedó reconciliado en todos los registros machine-readable.

### Contradicciones de instrucciones

- El brief diario conserva una instrucción heredada de entregar en `cola/entrada/<project_id>/` con archivos separados. El Contrato Operativo Unificado y el Plan Maestro vigentes establecen primero proyectos/<project_id>/storyboard.json, QA independiente y después una copia JSON en cola/entrada/<project_id>.json. Prevalece el contrato vigente.
- El brief diario pide que el cierre previo al sello tenga 110–170 caracteres. El storyboard de cambio de horario tiene 101 caracteres antes de «Esto fue Datos y ociosidades.»; incumple ese requisito por 9 caracteres. El penúltimo tramo sí cumple, con 156 caracteres.
- El radar recomienda red eléctrica; el brief específico de 23:30 pide cambio de horario/corazón. La agenda conserva TBD. No hay decisión de selección de Grok que resuelva la discrepancia.
- La instrucción «YA NO TOCAR» para pulpo y cebolla choca con el QA narrativo FAIL registrado en sus borradores. Ya hay registros de producción/programación en salidas; esta auditoría no desprograma ni reemplaza publicaciones.

## 2. Inventario de borradores en proyectos/

Fechas de creación tomadas del historial Git del archivo; la fecha del ID no equivale necesariamente a la fecha de creación ni al slot.

| project_id | Creación CDMX | Slot/objetivo | Narrativa | Estructura estática | Estilo | Dispatch |
|---|---|---|---|---|---|---|
| 2026-11-01_pulpo-tres-corazones | 31-oct 14:25 | 1-nov 07:00 | FAIL 72 | FAIL | carton_recortado | NOT_DISPATCHABLE |
| 2026-11-01_llorar-cebolla-quimica | 31-oct 14:25 | 1-nov 13:30 | FAIL 79 | FAIL | papel_recortado_popup | NOT_DISPATCHABLE |
| 2026-11-01_red-electrica-pulso-minuto | 1-nov 14:33 | Sin slot asignado | PASS 89 | Sin errores estáticos; DOI pendiente | risografia | NOT_DISPATCHABLE |
| 2026-11-01_dato-cambio-horario-corazon | 1-nov 17:54 | Propuesto para 1-nov 23:30 | PASS 87 | Sin errores estructurales estáticos; pendiente de ajuste del brief | art_deco_poster | NOT_DISPATCHABLE |

### Detalle de validación

**Pulpo**
- 8 escenas; 228 palabras; 78 s de escenas + 12 s de cortinilla = 90 s. La receta exige cortinilla de 6 s.
- Gancho de 4 palabras; 3 fuentes y source_ids resolubles.
- Sin capa de mapa ni capa de dato/gráfico; falta narrative_contract y faltan los seis campos de progresión narrativa por escena.
- SFX vacío en las ocho escenas. Hay asset_filename en las escenas, aunque approved_assets=[] y render_status=NOT_GENERATED. Las rutas de frames no existen en el árbol Git.
- QA en frío: FAIL 72. Flags: apertura hipotética, analogía imprecisa sobre branquias y afirmación no respaldada sobre corazones no sustituibles.
- Copia heredada en cola/bloqueados/; no existe copia activa en cola/entrada/.

**Cebolla**
- 8 escenas; 231 palabras; 78 s + cortinilla de 12 s = 90 s. La receta exige 6 s.
- Gancho de 6 palabras; 3 fuentes y source_ids resolubles.
- Sin mapa ni dato/gráfico; falta narrative_contract y faltan los seis campos de progresión por escena.
- SFX vacío en las ocho escenas. Hay asset_filename en las escenas, aunque approved_assets=[] y render_status=NOT_GENERATED. Las rutas de frames no existen en el árbol Git.
- QA en frío: FAIL 79. Flags: cierre que atribuye intención evolutiva no demostrada y límite de evidencia ausente.
- Copia heredada en cola/bloqueados/; no existe copia activa en cola/entrada/.

**Red eléctrica**
- 8 escenas; 196 palabras; 78 s + cortinilla de 6 s = 84 s. Gancho de 5 palabras.
- Tiene mapa, tres capas de dato/gráfico, 3 fuentes, source_ids resolubles, voz correcta, prompt_base literal y los seis campos narrativos por escena. Ambiente y SFX están presentes; no hay rutas de assets; approved_assets=[] y render_status=NOT_GENERATED.
- QA en frío registrado: PASS 89, siete checks true, critical_flags vacío.
- El DOI principal 10.1038/s41560-026-02144-0 sigue marcado PENDIENTE en el storyboard. No se ejecutó el check Crossref del validador. No tiene slot ni selección registrada.

**Cambio de horario/corazón**
- 8 escenas; 219 palabras; 78 s + cortinilla de 6 s = 84 s. Gancho de 4 palabras.
- 5 fuentes; source_ids resolubles; el archivo marca el DOI principal 10.1136/openhrt-2013-000019 como VERIFICADO_RESOLVEDOR. No se ejecutó Crossref en esta auditoría.
- Tiene mapa, tres capas de dato/gráfico, voz correcta, prompt_base literal, ambiente y SFX en las ocho escenas. No hay asset_filename, asset_type ni rutas de medios; approved_assets=[] y render_status=NOT_GENERATED.
- QA independiente registrado en esta auditoría: **PASS 87**, siete checks true, critical_flags vacío. La narración permite reconstruir una sola pregunta, abre con el reloj retrocediendo, explica el cambio de distribución por día y acota Michigan, 2010–2013, pacientes tratados con angioplastia y el carácter observacional.
- Se corrigieron mecánicamente cuatro rótulos de pantalla para dejarlos en tres palabras o menos. La narración y los claims no se reescribieron.
- Sigue pendiente el ajuste del cierre: 101 caracteres antes del sello frente a 110–170 del brief. Además, art_deco_poster repite el estilo del paquete Baffin asignado a las 17:00 del mismo día. No se promovió.

## 3. Paquetes ya presentes en salidas para slots del 1-nov

La agenda tiene cinco slots regulares y un paquete extra de madrugada a las 03:00. Se encontraron cinco paquetes con registros de producción/programación; no equivalen a cinco publicaciones públicas confirmadas.

| Paquete | Slot CDMX | Storyboard en salidas | QA local disponible | Evidencia de publicación |
|---|---:|---|---|---|
| 2026-11-01_dato-xolo-mictlan | 03:00 extra | 7 escenas; 214 palabras; 77+12=89 s; sin mapa/dato | No hay qa.json | YouTube uploaded/private con publishAt; TT/FB figuran programados |
| 2026-11-01_pulpo-tres-corazones | 07:00 | 8; 228 palabras; 78+12=90 s; sin mapa/dato | 19/21; fallan mapa y dato | YouTube uploaded/private; TT/FB v4 registrados como programados |
| 2026-11-01_llorar-cebolla-quimica | 13:30 | 8; 231 palabras; 78+12=90 s; sin mapa/dato | 19/21; fallan mapa y dato | YouTube uploaded/private; TT/FB v4 registrados como programados |
| 2026-10-26_baffin-bay-ice-shelf | 17:00 | 9; 215 palabras; 81+6=87 s | 20/21; falla subs_max_3_palabras (83 bloques) | YouTube uploaded/private; TT/FB v4 registrados como programados |
| 2026-11-03_kids-tiburon-groenlandia | 19:00 | 8; 244 palabras; 78+6=84 s | No hay qa.json | YouTube uploaded/private; TT/FB en conflicto entre registros |

Hallazgos de salida:
- Xolo: estilo declarado teatro_sombras, pero visual_identity.style_id declara carton_recortado; los prompts usan teatro_sombras. Además tiene cortinilla de 12 s y carece de mapa/dato.
- Pulpo y cebolla: sus ESTADO_EJECUCION dicen 78+6=84 s, pero el JSON suma 78+12=90 s. Los QA locales no son QA narrativo ni QA oficial de Grok.
- Baffin: usa art_deco_poster, igual que el candidato cambio-horario de las 23:30; hay repetición de estilo el mismo día.
- Tiburón: storyboard tiene 244 palabras, pero ESTADO_EJECUCION declara 211. El ID conserva fecha 3-nov aunque el slot se adelantó al 1-nov.
- Para tiburón, salidas/_ops registra que TT/FB se programaron el 1-nov 20:00 hora de Nueva York. Sin embargo, publicacion.json mantiene estado pendiente_ui para el 1-nov y conserva otros bloques TT/FB con el slot antiguo del 3-nov. data/reprogramacion_tt_fb_v4_2026-11-01_03.json todavía asigna el slot 1-nov 19:00 a arqueas. La programación TT/FB del tiburón no está reconciliada en los registros.
- Los storyboard de salidas contienen asset_filename o referencias a MP4, pero el árbol Git no contiene esos frames, audio ni MP4. Algunos mantienen approved_assets=[] y render_status=NOT_GENERATED pese a los registros de carga/programación. No se puede verificar el almacenamiento local desde GitHub.
- YouTube aparece como uploaded/private con publishAt futuro; eso prueba carga privada/programación registrada, no publicación pública. Los qa.json locales tampoco prueban recepción ni QA oficial de Grok.

## 4. Cola, estados y dispatchabilidad

### Inventario de cola del día

- cola/entrada/ contiene únicamente .gitkeep.
- No hay archivos cola/entrada/*.json ni carpetas cola/entrada/<project_id>/storyboard.json del 1-nov.
- No hay entradas activas del día. Las copias de pulpo y cebolla están en cola/bloqueados/, no en cola/entrada/.
- Existe una carpeta histórica de pardelas bajo cola/ y data/cola.json conserva un registro con estado fallo, rc=1 y una ruta de entrada que ya no existe. No corresponde al 1-nov.

### Compuerta de workflow

Archivo inspeccionado: .github/workflows/capcot-grok-dispatch.yml.

- Push escucha únicamente cola/entrada/*.json y el script interno exige una sola ruta de primer nivel con forma cola/entrada/<archivo>.json.
- workflow_dispatch con all busca solo archivos de primer nivel mediante find -maxdepth 1; con project_id construye exactamente cola/entrada/<project_id>.json.
- El workflow no busca proyectos/, salidas/, cola/bloqueados/ ni cola/entrada/<project_id>/storyboard.json.
- procesar_cola.py sí admite JSON de primer nivel y una carpeta inmediata con storyboard.json. Por tanto, el procesador admite una forma de entrada que el workflow no puede despachar.
- Si un commit modifica más de un JSON de entrada, el workflow de push falla porque espera exactamente uno.

**Resultado por ubicación:** los cuatro proyectos, los cinco storyboards en salidas y las copias bloqueadas son NOT_DISPATCHABLE en sus rutas actuales. No existe ningún paquete DISPATCHABLE en cola/entrada/.

### Estados Grok

No se encontró cola/estado/<project_id>.json para ninguno de estos IDs. Resultado exacto en cada caso:

| project_id | Resultado |
|---|---|
| 2026-11-01_dato-cambio-horario-corazon | RECEPCION_GROK_NO_CONFIRMADA |
| 2026-11-01_llorar-cebolla-quimica | RECEPCION_GROK_NO_CONFIRMADA |
| 2026-11-01_pulpo-tres-corazones | RECEPCION_GROK_NO_CONFIRMADA |
| 2026-11-01_red-electrica-pulso-minuto | RECEPCION_GROK_NO_CONFIRMADA |
| 2026-11-01_dato-xolo-mictlan | RECEPCION_GROK_NO_CONFIRMADA |
| 2026-10-26_baffin-bay-ice-shelf | RECEPCION_GROK_NO_CONFIRMADA |
| 2026-11-03_kids-tiburon-groenlandia | RECEPCION_GROK_NO_CONFIRMADA |

No se creó ni modificó ningún archivo de estado.

## 5. Actions y configuración de dispatch

Se revisaron las ejecuciones recientes de capcot-grok-dispatch.yml:
- Runs 131–147: 17 ejecuciones consecutivas con conclusión failure.
- La más reciente es la run 147, ID 41306776689, iniciada 2026-11-01 12:29:58Z.
- Los logs de las runs 147, 146 y 145 muestran el error literal: `Falta configurar GROK_WEBHOOK_URL.`
- La configuración también carece de `GROK_WEBHOOK_TOKEN`; el paso se detiene primero al comprobar la URL.
- No hay acuse HTTP 2xx ni receipt_id verificable en esas ejecuciones.

La nueva actualización del storyboard de cambio-horario está en proyectos/, fuera del filtro de paths, por lo que no disparó el workflow. Esta auditoría tampoco disparó Actions ni envió payloads.

## 6. Procesador, registro editorial y rotación

### scripts/procesar_cola.py

- La fecha por defecto se calcula con America/Mexico_City.
- Solo considera entradas en cola/entrada/ y filtra por los primeros diez caracteres del nombre de archivo o de la carpeta que contiene storyboard.json. No consume automáticamente colas históricas.
- El filtro usa la fecha del ID/ruta, no un campo fecha_objetivo o el slot editorial.
- Si Baffin (ID 2026-10-26) o tiburón (ID 2026-11-03) se volvieran a poner en cola para el 1-nov, el filtro los excluiría por su prefijo, aunque el calendario los asigne a slots del 1-nov.

### scripts/registro_editorial.py

- Es de solo lectura y combina data, proyectos, cola y salidas; no escribe data/*.json.
- Busca storyboards con profundidad de un nivel bajo proyectos/, cola/entrada/, cola/ y salidas/. No incorpora cola/bloqueados/.
- La fecha reconciliada se obtiene del project_id o nombre de carpeta, no del slot real. Por eso Baffin y tiburón quedan asociados a las fechas de sus IDs, no al 1-nov.
- La vista puede recuperar temas y estilos ausentes de data, pero no certifica por sí sola la fecha de publicación ni la selección de Grok.

### data/*.json — 16 archivos inspeccionados

| Archivo | Cobertura/último dato relevante |
|---|---|
| balances_6h.json | 24–28 oct |
| cola.json | 31 oct; conserva pardelas con fallo rc=1 y ruta de entrada ausente |
| endsscreens_rotacion.json | última revisión 1-nov 15:55 CDMX |
| estilos_usados.json | 24–28 oct |
| horario_2026-10-26.json | snapshot 26-oct |
| horario_2026-10-27.json | snapshot 27-oct |
| horario_2026-10-28.json | snapshot 28-oct |
| horario_2026-10-31.json | snapshot 31-oct |
| horario_semana_2026-11-01_07.json | parrilla 1–7 nov |
| horarios.json | actualizado 26-oct |
| publicaciones.json | registros hasta 31-oct; algunos publishAt llegan al 1-nov |
| reprogramacion_tt_fb_v4_2026-11-01_03.json | 1–3 nov; 10/10 TT y 10/10 FB, pero el slot 1-nov 19:00 aún apunta a arqueas |
| rotacion.json | registros hasta 31-oct |
| temas_del_dia.json | 24–28 oct; no contiene 1-nov |
| tendencias_estilos.json | actualizado 31-oct |
| vistas_historico.json | 24–28 oct |

La parrilla semanal contiene 36 filas: 35 slots regulares más el xolo extra de 03:00 del 1-nov. El slot 23:30 permanece TBD. La rotación y temas canónicos están desactualizados para 1-nov; registro_editorial.py aporta los storyboards, pero asigna fecha por ID y no por slot. No se modificó ningún JSON de data.

## 7. SFX, medios y APIs

- El storyboard de cambio-horario declara ambiente y SFX en las ocho escenas. Los SFX están escritos como descripciones, no como IDs del manifiesto. El manifiesto contiene 13 claves; solo reloj tiene correspondencia directa clara con el tic-tac. Los demás efectos requieren mapeo/decisión de producción. No hay audio generado.
- El catálogo canónico scripts/estilos.json contiene 50 estilos. Los prompt_base de los cuatro proyectos coinciden literalmente con sus estilos.
- No se reabrió la investigación de APIs: el radar del 1-nov no encontró evidencia oficial nueva suficiente para cambiar la documentación Meta/Google Trends. No se actualizó el informe técnico.

## 8. Cambios ejecutados en esta auditoría

1. En proyectos/2026-11-01_dato-cambio-horario-corazon/storyboard.json se registró QA narrativo independiente: PASS 87, siete checks true y flags vacíos.
2. Se acortaron cuatro rótulos de pantalla a tres palabras o menos. No se alteró narración, cifras, claims, fuentes ni decisión editorial.
3. Se volvió a leer el JSON desde GitHub. Verificación: 8 escenas, 219 palabras, 78+6=84 s, gancho de 4 palabras, source_ids válidos, mapa y tres capas de dato, prompts exactos, ambiente/SFX presentes, approved_assets=[] y render_status=NOT_GENERATED. Sin rutas de assets.
4. Se actualiza este informe y se volverá a leer desde GitHub.

## 9. No ejecutado deliberadamente

- No se promovió ningún storyboard a cola/entrada/: el slot 23:30 sigue sin selección, el candidato cambio-horario aún incumple la longitud final del brief y su estilo repite Baffin; además, una promoción al path observado por push dispararía el workflow, prohibido en esta ejecución.
- No se creó ni modificó cola/estado/.
- No se modificó data/*.json, main, workflows, permisos ni secretos.
- No se ejecutó el validador Python, tests ni helpers. La validación reportada es estática; no se declara PASS del validador ejecutable.
- No se generaron frames, imágenes, voz, audio, video, renders ni publicaciones; no se consumieron créditos.

**Estado final:** 4 borradores en proyectos; 0 entradas de cola del 1-nov; 0 paquetes dispatchables; 0 recepciones Grok confirmadas. El dato cambio-horario superó la lectura narrativa en frío, pero todavía no está en cola ni seleccionado. Red eléctrica también tiene QA narrativo PASS, pero carece de slot y mantiene DOI PENDIENTE.