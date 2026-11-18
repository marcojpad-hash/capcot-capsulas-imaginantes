# CONTROL DE COLA CAPCOT — 18 de noviembre de 2026

**Corte:** 18-nov-2026, 15:00 CDMX  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**HEAD revisado antes de la auditoría:** `ce93f6c57b9dd25816b28860f4f50cff4cdf1cf6`  
**Árbol base:** `37f2abde1f56a4235cdfbd99a9b708c74eec6ecb`

## 1. Briefs e inventario del día

- Existe `docs/briefs/2026-11-18_RADAR_CAPCOT.md` (blob `047f1ba9eac411b393e4218bc3726087bd52a1e6`).
- No existía `docs/briefs/2026-11-18_CONTROL_COLA.md`; este archivo registra el control.
- En `proyectos/` hay **un solo storyboard del 18-nov**: `proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
  - Creación por historial Git: 18-nov 08:19:39 CDMX; ajuste posterior de capas: 08:20:52 CDMX.
  - Fecha objetivo: 18-nov-2026; slot 17:00; cesta `intermedio_1`.
  - La carpeta contiene solo `storyboard.json`; no hay `ESTADO_EJECUCION.md`.
- `cola/entrada/*.json`: **0** archivos de primer nivel.
- No existe carpeta anidada `cola/entrada/2026-11-18_*`; tampoco hay salida ni copia bloqueada del proyecto actual.
- No existe `data/horario_2026-11-18.json`. El slot 17:00 cae dentro de la ventana vigente 16:30–18:00 de `data/horarios.json`; hoy miércoles es un día preferente de esa ventana. Eso no demuestra programación en una plataforma.
- El inventario del día no muestra un segundo storyboard, una entrada de cola adicional ni una salida.

## 2. Lectura narrativa independiente del proyecto del día

Se ocultaron título, resumen, arco, notas y `narrative_contract`; la evaluación se hizo únicamente con la narración concatenada.

**`2026-11-18_dato-kuroshio-puente-atmosferico`: `PASS / 90`.**

- `review_basis=lectura_en_frio_solo_narracion`.
- Siete checks verdaderos; `critical_flags=[]`.
- La narración abre con el desplazamiento al norte de la extensión de Kuroshio en las simulaciones y plantea cómo puede influir una corriente sobre otra sin mezclar aguas. Desarrolla el puente atmosférico, cuantifica la contribución modelada, acota el resultado y cierra regresando a la conexión entre océanos.
- El registro independiente quedó añadido al storyboard con `reviewed_at=2026-11-18T15:00:00-06:00` y `reviewer_role=auditor_capcot_independiente`.

## 3. Validación estructural estática del proyecto del día

| Control | Resultado |
|---|---|
| Escenas | 8 |
| Palabras de narración | 222 |
| Duración de escenas | 78 s |
| Cortinilla | 6 s |
| Duración total | 84 s |
| Gancho | 5 palabras |
| Arco | Los cuatro tipos requeridos están presentes |
| `narrative_contract` | Seis campos completos |
| `source_ids` | SRC-001 válido en las escenas |
| Voz | `es-MX-JorgeNeural`, coherente con ciencia/clima/oceanografía |
| Estilo | `atlas_antiguo` existe en el catálogo y el prompt base coincide literalmente |
| Ambiente/SFX | Declarados en las ocho escenas |
| Mapa/gráfico | Ambas capas presentes y con fuente |
| Assets | `approved_assets=[]`; `export.render_status=NOT_GENERATED`; sin `asset_filename`, `asset_type` ni rutas de medios |

**Bloqueo estructural:** la capa de mapa tiene dos regiones con límites geográficos y fuente (figura 1a–b), pero `puntos=[]`. El validador vigente exige una lista de puntos no vacía para reconocer la capa y la rechaza como “mapa sin puntos o fuente”. La plantilla vertical, en cambio, muestra `puntos=[]` como ejemplo. Es una contradicción entre plantilla y validador. No añadí un pin o centroide artificial: la nota del storyboard aclara que los rectángulos son regiones de análisis, no estaciones puntuales.

La fuente primaria es la página editorial de Nature Geoscience. El DOI `10.1038/s41561-026-02139-2` figura como cadena mostrada por la editorial, pero `doi_verification_status=PENDIENTE_RESOLVEDOR`; no se marca como DOI resuelto.

**Resultado estructural:** FAIL por la regla actual del mapa. El PASS narrativo no basta para promover. El proyecto permanece en `proyectos/`; no se creó `cola/entrada/<project_id>.json`.

## 4. Compuerta de handoff y dispatchabilidad

El workflow `.github/workflows/capcot-grok-dispatch.yml` (blob `47bbd228cfce5a1d402dc952e283e8d0f8e37030`) tiene:

- Filtro push: `cola/entrada/*.json`.
- Selector en push: regex `^cola/entrada/[^/]+\.json$`.
- `workflow_dispatch`: `find cola/entrada -maxdepth 1 -type f -name '*.json'`; para un ID busca `cola/entrada/<project_id>.json`.

Por tanto, el workflow no descubre paquetes en `cola/entrada/<project_id>/storyboard.json` ni directorios anidados.

| Elemento observado | Ruta real | Estado para este workflow |
|---|---|---|
| Storyboard Kuroshio 18-nov | `proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json` | **NOT_DISPATCHABLE**: no está en cola |
| JSON de primer nivel en `cola/entrada/` | Ninguno | **NOT_DISPATCHABLE**: cero archivos seleccionables |
| Carpeta histórica 9-nov robot | `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/storyboard.json` | **NOT_DISPATCHABLE**: carpeta anidada |
| Carpeta 11-nov ratas topo | `cola/entrada/2026-11-11_dato-ratas-topo-damaraland/frames/` | **NOT_DISPATCHABLE**: contiene frames, no un storyboard seleccionable |

La carpeta 9-nov robot contiene un storyboard de 9 escenas, 210 palabras y `narrative_qa=PASS/90`; `frames/` contiene solo `.gitkeep`. Su marcador en `handoffs/grok_inbox/` conserva `status=pending`, `branch=main` y el commit que declara ese JSON. Ese marcador no es un acuse de lectura de Grok ni prueba que no haya existido una entrega por otra vía.

La carpeta 11-nov ratas topo conserva ocho PNG reales en `frames/` (no placeholders); el storyboard correspondiente está en `cola/bloqueados/`, no en la carpeta de entrada. No es un paquete despachable.

La carpeta histórica correspondiente a un slot 23:30 queda expresamente excluida por la instrucción y no se incorpora a la auditoría narrativa ni a una promoción.

## 5. Recepción Grok y ejecuciones de Actions

- `cola/estado/` no existe en esta rama. La consulta directa de `cola/estado/<project_id>.json` devolvió 404 para el storyboard del 18-nov y para los doce IDs del lote 5–7.
- Para esos trece proyectos se registra exactamente **`RECEPCION_GROK_NO_CONFIRMADA`**. Es el estado de la evidencia disponible en este repositorio; **no demuestra que no haya ocurrido entrega manual o por otro canal**.
- `handoffs/grok_done/` contiene solo `.gitkeep`. `handoffs/grok_inbox/` contiene el marcador pending del robot 9-nov y su README; no hay marcador de finalización.
- La ejecución más reciente del workflow de dispatch sigue siendo la #147 del 1-nov-2026 (run ID `41306776689`). Validó un paquete y falló en “Verificar configuración del receptor” con el error literal `Falta configurar GROK_WEBHOOK_URL.`; el paso “Entregar paquetes y exigir acuse individual” quedó skipped. En ese log también aparecen vacíos los nombres `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`; no se registra ningún valor.
- Esa ejecución pertenece a una versión anterior del workflow. El YAML vigente hace el webhook opcional y, si no está configurado, escribe un marcador en `handoffs/grok_inbox/`; el marcador sigue sin equivaler a recepción. No se encontró una ejecución posterior de `capcot-grok-dispatch`; el smoke test TTS del 8-nov no es un dispatch.

No se envió webhook, payload ni dispatch en esta auditoría.

## 6. Procesador y registro editorial

- `scripts/procesar_cola.py` usa por defecto la fecha local actual de CDMX y filtra por la fecha extraída del nombre/ruta. Acepta `--fecha` explícita, por lo que puede procesar una fecha histórica si se le pide; no está bloqueado técnicamente a “hoy”. La selección por ruta tampoco sustituye la comprobación de `fecha_objetivo` dentro del JSON.
- El procesador contempla tanto JSON de primer nivel como storyboards en carpetas anidadas. Esto no coincide con el selector del workflow, que solo admite JSON de primer nivel.
- `scripts/registro_editorial.py` combina rotación/publicaciones y storyboards de proyectos, cola y salidas, pero no incorpora los sidecars sociales, `cola/bloqueados/`, `handoffs/` ni los horarios diarios posteriores. No basta por sí solo para certificar el estado real de publicación.

No se ejecutaron Python helpers: el repositorio no quedó disponible como checkout/runtime en este entorno. La validación fue estática, leyendo los scripts y los JSON directamente desde GitHub.

## 7. Lote obligatorio 5–7 de noviembre: identidad y metadatos

Se releyeron los doce storyboards canónicos y se compararon `project_id`, fecha objetivo, hora local y cesta con `data/horario_semana_2026-11-01_07.json`. **Los doce coinciden exactamente** con sus slots asignados. Los slots 23:30, kids 3-nov 07:00 y Machu Picchu 4-nov 19:00 quedan fuera del lote.

El storyboard canónico `2026-11-05_inter-arboles-se-comunican` sí trata redes micorrícicas comunes y cita Karst et al. 2023; no hay desajuste de tema. La variante de árboles en `cola/bloqueados/` es otro artefacto. El slot 2026-11-07 17:45 corresponde exactamente a `2026-11-07_inter-nubes-pesan`; `extra-nubes-pesan` no se cuenta como segundo proyecto.

| Project ID | Slot/cesta | narrative_qa | Checks true | Checks false |
|---|---|---:|---:|---|
| `2026-11-05_kids-dia-en-venus` | 05-nov 07:00 / kids | **PASS 88** | 7/7 | — |
| `2026-11-05_comida-palomitas` | 05-nov 13:30 / comida_familia | **FAIL 82** | 5/7 | apertura; progresión |
| `2026-11-05_inter-arboles-se-comunican` | 05-nov 17:00 / intermedio_1 | **FAIL 78** | 6/7 | apertura |
| `2026-11-05_inter-rayo-globular` | 05-nov 17:45 / intermedio_2 | **FAIL 81** | 6/7 | apertura |
| `2026-11-06_kids-ballena-azul-corazon` | 06-nov 07:00 / kids | **FAIL 80** | 6/7 | payoff |
| `2026-11-06_comida-aguacate-negro` | 06-nov 13:30 / comida_familia | **FAIL 79** | 5/7 | progresión; transiciones |
| `2026-11-06_inter-ranas-congeladas` | 06-nov 17:00 / intermedio_1 | **FAIL 83** | 5/7 | progresión; transiciones |
| `2026-11-06_inter-arena-cantante` | 06-nov 17:45 / intermedio_2 | **PASS 94** | 7/7 | — |
| `2026-11-07_kids-huesos-bebe` | 07-nov 07:00 / kids | **FAIL 82** | 5/7 | progresión; transiciones |
| `2026-11-07_comida-hielo-caliente` | 07-nov 13:30 / comida_familia | **FAIL 81** | 6/7 | apertura |
| `2026-11-07_inter-pulpo-suenos` | 07-nov 17:00 / intermedio_1 | **FAIL 72** | 2/7 | progresión; transiciones; giro; límite; payoff |
| `2026-11-07_inter-nubes-pesan` | 07-nov 17:45 / intermedio_2 | **FAIL 78** | 4/7 | progresión; transiciones; payoff |

Los siete checks se conservan explícitos en cada JSON: `pregunta_central_reconstruible`, `apertura_in_medias_res`, `progresion_por_escena`, `transiciones_causales`, `giro_cientifico_explicado`, `limite_evidencia_explicito` y `payoff_cierre_apertura`. Todos mantienen `review_basis=lectura_en_frio_solo_narracion` y sus `critical_flags`. En esta corrida se refrescó `reviewed_at` a 2026-11-18T15:00:00-06:00; no se reescribió ninguna narración, afirmación ni fuente. Los dos PASS narrativos no son aptos para promoción porque el validador estructural falla.

### Estructura y contrato de los doce

- 85 escenas en total; las doce piezas tienen 7–8 escenas y 78 s de escenas + 6 s de cortinilla = 84 s.
- Gancho de 3–5 palabras y arco completo en los doce.
- Palabras: 170–221, excepto `2026-11-05_inter-arboles-se-comunican`, que tiene **169**.
- Faltan los seis campos obligatorios por escena (`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`) en las **85 escenas: 510 campos ausentes**. Esta compuerta bloquea los doce, incluidos Venus y Arena aunque su QA narrativo sea PASS.
- Hay **75 arrays `sfx` vacíos**; el ambiente sí está declarado. La receta pide que el silencio se exprese explícitamente, por lo que un array vacío no documenta por sí mismo si hubo decisión de silencio.
- Once storyboards tienen capas de mapa y dato con fuente; Árboles no tiene ninguna de las dos.
- `source_ids` son válidos; los estilos existen y todos los prompts comienzan con el `prompt_base` exacto.
- En los doce: `approved_assets=[]`, `export.render_status=NOT_GENERATED`; no aparecen `asset_filename`, `asset_type` ni rutas de medios.
- Los doce usan `estructura=pregunta`: se repite cuatro veces en cada día, contra la regla de no repetir estructura el mismo día. Los `style_id` sí son distintos dentro de cada día.
- `2026-11-07_inter-pulpo-suenos` atribuye la observación a `Octopus insularis`, pero el DOI citado corresponde a `Octopus laqueus`; se conserva la bandera de discrepancia de fuente. No se altera el claim.
- La matriz `docs/VOCES_POR_TEMA.md` asigna `narradora_es` a biología y cocina. Siete storyboards de esas líneas mantienen `es-MX-JorgeNeural`: Palomitas, Árboles, Ballena, Aguacate, Ranas, Huesos y Pulpo. Plan/Receta/validador aún fijan JorgeNeural globalmente, así que existe conflicto documental y el validador no detecta el mapa temático más reciente. No se cambiaron voces.

### Copias heredadas bloqueadas

Hay snapshots ya ubicados en `cola/bloqueados/` para seis IDs canónicos: Rayo globular, Aguacate, Ranas, Arena, Huesos y Nubes. Sus SHA difieren de los storyboards actuales de `proyectos/`; no se reemplazaron ni se movieron. No existe copia activa de ninguno de los doce en `cola/entrada/`. Las variantes de Palomitas, Árboles, Ballena, Hielo, Pulpo y Venus no se confundieron con los IDs canónicos.

## 8. Guardia de producción preexistente y no redispatch

Siete de los doce proyectos tienen evidencia de salida, programación o publicación en sidecars de `proyectos/` y/o en los horarios diarios. Se clasifican **`PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`**. Esto no atribuye QA oficial a Grok.

| Proyecto | Evidencia registrada | IDs/privacidad/estado |
|---|---|---|
| Venus | TikTok y Facebook publicados el 07-nov | TikTok `7705488176793652481` (Everyone); Facebook `2544385142727016` (Public). No aparece ID de YouTube en estos sidecars. Los horarios reales difieren del slot semanal 05-nov 07:00. |
| Palomitas | YT, TikTok y Facebook publicados 08-nov 07:00 | YT `zTP5akrGA9M` (public); TikTok `7705593452003691794` (Everyone); Facebook `1167496802382795` (Public). |
| Ranas | YT y TikTok publicados 09-nov 07:00; Facebook marcado programado | YT `UBFuKBU3cx0` (public); TikTok `7705596671807245586` (Everyone); Facebook sin ID de publicación confirmado. |
| Aguacate | YT y TikTok publicados 10-nov 07:00; Facebook marcado programado | YT `nSS_q2tj2P0` (public); TikTok `7705594217136966920` (Everyone); Facebook sin ID de publicación confirmado. |
| Ballena azul | YT y TikTok publicados 11-nov 07:00; Facebook marcado programado | YT `wbFrlM2e_YE` (public); TikTok `7705594333574991122` (Everyone); Facebook sin ID de publicación confirmado. |
| Arena cantante | YT, TikTok y Facebook con evidencia de publicación 07-nov | YT `m4RqQRaz55k` (public); TikTok `7705502155427368212` (Everyone); Facebook `2224920108452190` (Public). Un segundo ID, `ztIkYcXB91U`, sigue descrito como programado para 19:00; privacidad no registrada. **Riesgo de duplicado** frente al ID público; no se canceló ni borró. |
| Hielo caliente | YT/TikTok/Facebook programados 11-nov 13:30 | YT `HSgrnejAcaI` (private, programado); TikTok `7706905447424347393` (Everyone, programado); Facebook asset `1460158683840154` (Public, UI “En proceso…”). No se marca como publicado. |

Los slots reales de varios sidecars/daily records no coinciden con los slots del horario semanal original; el horario semanal conserva `estado=pedir_chatgpt`, mientras los registros posteriores documentan publicaciones o programación. Para estado de plataforma prevalecen esos registros posteriores, sin borrar la discrepancia.

En los siete proyectos los sidecars apuntan a MP4 bajo rutas locales `/workspace/...`; la rama no contiene `salidas/<project_id>/` ni esos archivos. Se marca **`MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`**. No se afirma que los MP4 no existan fuera de GitHub.

Los otros cinco IDs (Árboles, Rayo, Huesos, Pulpo y Nubes) no muestran en esta rama sidecars sociales, IDs ni programación diaria de salida. Eso significa “sin evidencia de salida en este árbol”, no prueba de que no haya ocurrido trabajo externo.

No existe archivo `historial_youtube` en esta rama. El riesgo `ztIkYcXB91U` aparece en el sidecar de Arena y se conserva como discrepancia pendiente.

## 9. Rotación y registros de datos

- `data/horario_semana_2026-11-01_07.json` contiene los doce slots canónicos y sus metadatos coinciden.
- `data/horario_2026-11-08.json` a `data/horario_2026-11-11.json` registran estados posteriores para Palomitas, Ranas, Aguacate, Ballena y Hielo.
- `data/horarios.json` está actualizado al 09-nov; no existe archivo de horario diario del 18-nov.
- `data/estilos_usados.json` llega a 28-oct; `data/rotacion.json`, `data/publicaciones.json` y `data/cola.json` llegan a 31-oct; `data/temas_del_dia.json` llega a 28-oct. Son registros incompletos para certificar la rotación de 5–7 o la del día 18.
- El catálogo `scripts/estilos.json` tiene 50 estilos. Los doce IDs históricos están presentes y sus prompts base coinciden; dentro de cada día no se repite estilo. La estructura `pregunta`, en cambio, sí se repite cuatro veces por día.
- Para el 18-nov, `atlas_antiguo` coincide con el tema océano/clima y no repite el estilo `papel_stop_motion` del borrador del 17-nov.

## 10. APIs y documentación oficial

La revisión del 18-nov ya quedó registrada en `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`, sección 9.9: la tabla oficial de Meta incluye Graph API v27.0, introducida el 04-nov-2026; Page Insights muestra v27.0. Instagram Insights no presenta una métrica nueva en esa revisión y Google Trends API continúa en alfa limitada. No apareció en los briefs una actualización oficial posterior que justificara repetir la consulta o modificar integraciones. No se tocaron conectores, permisos ni credenciales.

## 11. Cambios realizados y límites

En esta auditoría:

1. Se añadió `narrative_qa=PASS/90` al storyboard Kuroshio del 18-nov.
2. Se refrescó `reviewed_at` de los doce QA históricos, conservando exactamente sus scores, statuses, checks y `critical_flags`.
3. Se creó este control.

No se modificaron narraciones, claims, fuentes, decisiones editoriales, `data/*.json`, `cola/estado/`, workflows, secretos, permisos, `main`, medios ni publicaciones. No se creó ninguna entrada de cola, no se movió ninguna copia, no se generaron medios, no se publicó, no se enviaron payloads y no se consumieron créditos.

**Resultado:** Kuroshio tiene QA narrativo PASS, pero sigue fuera de cola por la incompatibilidad mapa/validador. En el lote 5–7 hay 2 PASS narrativos, 10 FAIL y **0/12 estructuralmente aptos**. Siete proyectos ya tienen procesamiento/publicación/programación preexistente y no deben redispatcharse.


## Addendum técnico — corrección del contrato de mapas, 18-nov-2026

Después del corte de las 15:00 se revisó la causa del bloqueo estructural de Kuroshio contra el storyboard, la plantilla vertical, la Receta y el validador. Se confirmó una contradicción real: la receta exigía coordenadas reales y precisión; el storyboard describía dos regiones de análisis con límites publicados y advertía que no eran estaciones puntuales; pero el validador solo aceptaba pines individuales. La plantilla, además, mostraba `puntos=[]` sin ofrecer una estructura para regiones.

### Corrección mecánica aplicada

1. `scripts/validar_storyboard.py` ahora acepta dos geometrías cartográficas válidas: puntos con latitud/longitud, o regiones con `bounds=[lat_min, lon_min, lat_max, lon_max]`. Valida límites numéricos y rangos geográficos; sigue exigiendo fuente y al menos una geometría válida. No convierte regiones en pines.
   - Commit: `c164c1b2dc4ea293af50154bd0ead3768fc2c356`.
2. `templates/storyboard_vertical.template.json` ahora incluye el esquema de `areas` con bounds y nota de precisión, además de `puntos`.
   - Commit: `82fa4f9df9bb627d8213dad325df08945cb15e53`.
3. `docs/RECETA_CAPSULA.md` ahora define ambas geometrías y prohíbe inventar pines, centroides o trayectorias cuando la fuente solo publica regiones.
   - Commit: `1fe58b94e6180a059e1bf1e33afbdf5fd585887d`.

### Relectura estática del storyboard Kuroshio desde GitHub

Blob actual: `3f2dae68e9e32257b1bff2f485e532c466467113`.

- QA narrativo: `PASS`, score 90, siete checks true, `critical_flags=[]`, `review_basis=lectura_en_frio_solo_narracion`.
- Estructura comprobada estáticamente: 8 escenas; 222 palabras; 78 s de escenas + 6 s de cortinilla = 84 s; gancho de 5 palabras.
- Las dos regiones del mapa pasan el nuevo contrato de bounds: Kuroshio [35, 140, 45, 170] y Gulf Stream [35, -80, 45, -50]. Ambas proceden de las cajas regionales citadas en SRC-001. No se inventaron coordenadas puntuales.
- Capa de gráfico, fuente, voice contract, prompt base, source_ids, `approved_assets=[]`, `export.render_status=NOT_GENERATED` y ausencia de rutas de medios: comprobados estáticamente.
- DOI: permanece `PENDIENTE_RESOLVEDOR`; la verificación independiente no está resuelta. El validador no se ejecutó en runtime en esta sesión, y no se ejecutó `--check-doi`.

**Estado operativo:** la causa específica “mapa sin puntos” quedó corregida en el validador y alineada con plantilla/receta. No declaro todavía “validador ejecutado PASS” ni promuevo a cola: falta ejecución real del helper y resolver la verificación DOI que el procesador exige con `--check-doi`. El proyecto permanece en `proyectos/`; no se creó handoff ni se disparó workflow.

### Precisión adicional sobre el procesador

`scripts/procesar_cola.py` usa por defecto la fecha CDMX actual y filtra por el prefijo de fecha de la ruta. Permite una fecha histórica explícita mediante `--fecha`; por tanto, no está limitado técnicamente a hoy cuando se proporciona ese argumento. Tampoco compara la fecha del nombre con un campo interno `fecha_objetivo` del JSON. La regla operativa correcta es: ejecución normal sin override = fecha actual; ejecución con `--fecha` = fecha solicitada explícitamente. No se modificó el procesador.
