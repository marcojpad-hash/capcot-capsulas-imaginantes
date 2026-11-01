# CONTROL DE COLA CAPCOT — 2026-11-01

**Corte:** 1-nov-2026, tarde CDMX. **Rama:** `feature/capcot-video-discovery-continuity`. **HEAD de auditoría:** `2abc31925449c0cd53656f6f3dbadc4db5fadb84`.  
**Método:** lectura de GitHub y revisión estática; no hubo checkout/runtime local.

## Dictamen

**HANDOFF BLOQUEADO.** Hay 3 borradores en `proyectos/`, 0 entradas activas en `cola/entrada/`, 2 snapshots bloqueados (pulpo y cebolla), 5 paquetes de salida asignados a slots y un slot de dato de las 23:30 aún pendiente. No hay acuses en `cola/estado/`; recepción de Grok no confirmada para ninguno.

QA narrativo independiente: pulpo **FAIL 72**, cebolla **FAIL 79**, red eléctrica **PASS 89**. Red eléctrica no se promovió: el validador Python no pudo ejecutarse, el DOI primario sigue `PENDIENTE` y crear una entrada en la ruta observada por Actions dispararía el workflow, expresamente prohibido en esta auditoría.

Las 12 ejecuciones más recientes de Actions (#136–147) fallaron. Error literal de los tres logs más recientes: `Falta configurar GROK_WEBHOOK_URL.`.

## 1. Briefs y borradores vigentes

Existe `docs/briefs/2026-11-01_RADAR_CAPCOT.md`; la versión anterior de este control decía erróneamente que no existía y queda sustituida por este informe.

| Proyecto | Creación del borrador | Slot/fecha objetivo | QA narrativo | Dispatch |
|---|---|---|---|---|
| `2026-11-01_pulpo-tres-corazones` | 31-oct, 14:25 CDMX | 1-nov 07:00 | FAIL 72/100 | NOT_DISPATCHABLE |
| `2026-11-01_llorar-cebolla-quimica` | 31-oct, 14:25 CDMX | 1-nov 13:30 | FAIL 79/100 | NOT_DISPATCHABLE |
| `2026-11-01_red-electrica-pulso-minuto` | 1-nov, 14:33 CDMX | 1-nov, sin slot | PASS 89/100 | NOT_DISPATCHABLE |

Pulpo y cebolla tienen copias en `cola/bloqueados/<project_id>/storyboard.json`; los blobs coinciden con los originales previos al QA. Se conservaron sin modificar. No había una copia activa en entrada que mover.

`cola/entrada/` contiene solo `.gitkeep`: 0 JSON de primer nivel y 0 carpetas con `storyboard.json`. El paquete histórico de pardelas bajo `cola/2026-10-31_2026-10-31_pardelas-jetlag-solar/` no es entrada vigente.

## 2. Paquetes de salida asociados a la parrilla del 1-nov

| Pieza | ID de salida | Slot | Evidencia y fallos |
|---|---|---:|---|
| Xolo | `2026-11-01_dato-xolo-mictlan` | 03:00 extra | 7 escenas, 214 palabras, 77+12=89 s; sin `qa.json`; faltan mapa y dato/gráfico; rutas de assets; YouTube cargado privado y programado |
| Pulpo | `2026-11-01_pulpo-tres-corazones` | 07:00 | QA local 19/21; render 61.80 s; faltan mapa y dato/gráfico; YouTube privado programado |
| Cebolla | `2026-11-01_llorar-cebolla-quimica` | 13:30 | QA local 19/21; render 66.70 s; faltan mapa y dato/gráfico; YouTube privado programado |
| Baffin | `2026-10-26_baffin-bay-ice-shelf` | 17:00 | QA local 20/21; render 91.93 s; 83 bloques de subtítulos superan tres palabras; YouTube privado programado |
| Tiburón de Groenlandia | `2026-11-03_kids-tiburon-groenlandia` | 19:00 | 8 escenas, 244 palabras (>235), 78+6=84 s; sin `qa.json`; YouTube privado programado |

El slot 23:30 sigue pendiente y no tiene storyboard. Los cinco storyboards de salida conservan `approved_assets=[]` y `export.render_status=NOT_GENERATED`, pero hay QA o registros de carga/programación y rutas de assets. No hay MP4, frames, imágenes ni audio rastreables en el árbol de GitHub. Los placeholders no cuentan como medios y el estado del JSON contradice los artefactos de salida.

### Acuses

Los seis archivos consultados devolvieron 404. Resultado exacto para cada ID:

- `2026-11-01_pulpo-tres-corazones` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-11-01_llorar-cebolla-quimica` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-11-01_red-electrica-pulso-minuto` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-11-01_dato-xolo-mictlan` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-10-26_baffin-bay-ice-shelf` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-11-03_kids-tiburon-groenlandia` — **RECEPCION_GROK_NO_CONFIRMADA**

Los `qa.json` existentes son QA local; no prueban recepción ni QA de Grok.

## 3. QA en frío y estructura

La lectura se hizo solo sobre la narración concatenada, ocultando título, resumen, arco, notas y contrato.

- **Cebolla — FAIL 79.** Pregunta, apertura, progresión, transiciones y giro pasan. Fallan límite de evidencia y payoff. Flags: `CIERRE_ATRIBUYE_INTENCION_EVOLUTIVA_NO_DEMOSTRADA`, `LIMITE_DE_EVIDENCIA_NO_EXPLICITO`. El cierre atribuye a la cebolla una intención de evitar ser comida que las fuentes no demuestran.
- **Pulpo — FAIL 72.** Pregunta, progresión, transiciones, giro y payoff pasan. Fallan apertura y límite de evidencia. Flags: `APERTURA_HIPOTETICA_NO_IN_MEDIAS_RES`, `ANALOGIA_BRANQUIAS_SACAR_AIRE_DEL_AGUA_IMPRECISA`, `AFIRMACION_CORAZONES_NO_SUSTITUIBLES_SIN_RESPALDO`.
- **Red eléctrica — PASS 89.** Los siete checks son verdaderos y `critical_flags=[]`. La narración pasa del patrón global a la medición local, identifica la autoprueba de la UPS, limita la conclusión a una UPS concreta y paga la apertura con el efecto de rutinas sincronizadas.

Se registró `narrative_qa` en los tres borradores. En red eléctrica también se añadieron los seis campos narrativos por escena, sin cambiar narración ni claims.

Pulpo y cebolla: 8 escenas, 78 s de escenas + cortinilla declarada de 12 s = 90 s, frente a objetivo 84 s. Sus `ESTADO_EJECUCION.md` dicen 78+6=84, contradicción con el JSON. Además, no tienen `narrative_contract`, faltan los seis campos narrativos por escena, faltan capas mapa y dato/gráfico, tienen rutas `asset_filename`/`asset_type` no existentes en el árbol y SFX vacíos.

Red eléctrica: 8 escenas, 196 palabras, título de 5 palabras, 78+6=84 s, voz `edge-tts / es-MX-JorgeNeural`, `source_ids` válidos, `prompt_base` coincidente con `risografia`, mapa, dato, ambiente y SFX presentes, `approved_assets=[]`, `render_status=NOT_GENERATED` y sin rutas de medios. El DOI `10.1038/s41560-026-02144-0` conserva estado `PENDIENTE`; la página editorial existe, pero no se ejecutó Crossref.

La revisión estática de las condiciones estructurales del validador no encontró errores en red eléctrica tras añadir los campos por escena. No equivale a ejecutar Python. No se promovió a cola.

## 4. Dispatch, Actions y procesador

El workflow `.github/workflows/capcot-grok-dispatch.yml` observa JSON de primer nivel en `cola/entrada/` y usa búsqueda con profundidad máxima 1. No detecta `proyectos/<id>/storyboard.json`, `cola/entrada/<id>/storyboard.json`, bloqueados ni salidas. Por ruta, los tres borradores, las dos copias bloqueadas y los cinco storyboards de salida son **NOT_DISPATCHABLE**.

Las ejecuciones #136–147 terminaron en failure. Los tres logs más recientes contienen literalmente `Falta configurar GROK_WEBHOOK_URL.`. Los nombres `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` aparecen vacíos en el entorno; el paso se detiene primero por URL y no llega a comprobar token. No se muestran valores.

`scripts/procesar_cola.py` sí acepta JSON raíz y carpeta anidada de un nivel, pero filtra por los primeros diez caracteres del nombre de archivo/directorio, no por una fecha objetivo del storyboard. Baffin (ID 26-oct) y tiburón (ID 3-nov) no serían seleccionados para 1-nov aunque el horario los asigne a ese día.

`scripts/registro_editorial.py` toma fecha del prefijo de `project_id`, escanea un nivel en proyectos/entrada/cola/salidas y no incluye `cola/bloqueados/`. Por ello omite bloqueados, clasifica Baffin y tiburón por fecha de ID y cuenta red eléctrica como elemento del 1-nov aunque no tenga slot.

## 5. Datos y contradicciones

- El horario semanal declara `slots_por_dia=5`, pero contiene 6 filas para 1-nov: Xolo extra 03:00, pulpo 07:00, cebolla 13:30, Baffin 17:00, tiburón 19:00 y dato 23:30 pendiente. Si se llena 23:30, serán seis piezas contando el extra.
- `project_id_plan` no coincide con el ID real de pulpo ni cebolla.
- Baffin y tiburón tienen prefijos 26-oct y 3-nov aunque el slot objetivo es 1-nov.
- `data/reprogramacion_tt_fb_v4_2026-11-01_03.json` declara el lote completo, pero su slot 1-nov 19:00 aún referencia arqueas. El horario y `salidas/_ops/2026-11-01_swap_arqueas_tiburon.md` dicen que fue sustituida por tiburón. El `publicacion.json` del tiburón conserva TT/FB pendientes en su resultado, mientras el registro operativo dice que ya se programó en UI.
- `data/temas_del_dia.json` llega a 28-oct; `rotacion.json` y `publicaciones.json` a 31-oct; `estilos_usados.json`, `balances_6h.json` y `vistas_historico.json` a 28-oct. No reflejan el 1-nov.
- `data/cola.json` conserva el fallo de pardelas de 31-oct (`rc=1`) con una ruta de entrada que no existe en el árbol actual.
- `data/endscreens_rotacion.json` sí tiene actualización del 1-nov a las 13:48 CDMX.
- Los radares 5–7 nov afirman que sus cuatro paquetes están en `cola/entrada/`; el árbol actual los muestra en `cola/bloqueados/`, no en entrada.

Los tres borradores actuales usan estilos de catálogo distintos: `carton_recortado`, `papel_recortado_popup` y `risografia`. Los cinco storyboards de salida también tienen estilos distintos, pero la rotación no puede certificarse con el registro histórico desactualizado y el cálculo por prefijo de ID.

Los registros de YouTube muestran `privacyStatus=private` y `publishAt` programado. Aunque algunos horarios ya transcurrieron, no se consultó el estado público en vivo; no se marca ninguna pieza como publicada. Los registros de TT/FB son evidencia de programación en algunos casos, no de publicación pública.

## 6. Correcciones mecánicas realizadas

Sin tocar claims, narración, decisiones editoriales, datos ni workflows:

1. `scripts/validar_storyboard.py` — eliminada la validación duplicada que exigía booleanos ingleses fuera de `checks` y un campo `premise` ajeno al contrato documentado. Commit `22f2718041975b21fdfd64aa74afb82669c667f0`.
2. `scripts/generar_guion_llm.py` — deja de autoañadir `narrative_qa`; el QA corresponde al auditor independiente. Contrato de seis campos y voz con idioma `es-MX`. Commit `bfbfaaa72e819d4a3720eb36b5661684de8acab4`.
3. `templates/storyboard_vertical.template.json` — añadidos los seis campos narrativos por escena. Commit `8d74e3f23c4b52794566f918e3159cd4e5ef93ac`.
4. `docs/RECETA_CAPSULA.md` — documentados los campos por escena y la responsabilidad del auditor. Commit `bb7f995e451778f823a3aebc68e6432da96fb645`.
5. `scripts/qa_capsula.py` — umbral de duración renderizada corregido de 60–120 s a **75–90 s**. Commit `2abc31925449c0cd53656f6f3dbadc4db5fadb84`.

Los `qa.json` históricos no se reescribieron. Con el nuevo umbral, los renders de pulpo (61.80 s), cebolla (66.70 s) y Baffin (91.93 s) también fallarían duración si se repitiera QA; no se volvió a renderizar.

Commits de QA: cebolla `794c3a18b3e7e6f417eda12b2bdfa43f9ac2fd3a`; pulpo `b50a4337128310b70e80fc52e5072e87b7b1bafc`; red eléctrica QA `1359d0bb3994f607ed88d7441253bb53b8c562ae` y metadatos causales `94eb9252e3358a20fc20d6f4290dcf1974281810`.

## 7. Límites y estado final

No había runtime/checkout local: no se ejecutaron validador Python, helpers ni tests. Se hizo revisión estática y comprobación estática de los campos del validador. No se revisaron APIs porque no se identificó un cambio oficial nuevo.

No se modificaron `data/*.json`, `main`, estados de Grok, workflow, secretos, permisos ni decisiones editoriales. No hubo merge. No se generaron medios, no se publicó, no se dispararon Actions ni se enviaron payloads externos.

- Pulpo: **FAIL narrativo; no promover**.
- Cebolla: **FAIL narrativo; no promover**.
- Red eléctrica: **PASS narrativo; estructura sin errores detectados en revisión estática; no promover en esta ejecución**.
- Cola activa: **vacía**.
- Recepción Grok: **no confirmada para todos los IDs enumerados**.
- Publicación pública: **no confirmada**.
