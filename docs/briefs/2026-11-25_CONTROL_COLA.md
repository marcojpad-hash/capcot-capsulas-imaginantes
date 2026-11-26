# CONTROL DE COLA CAPCOT — 2026-11-25

**Corte:** 2026-11-25 15:19, America/Mexico_City  
**Rama auditada:** `feature/capcot-video-discovery-continuity`  
**HEAD de feature al iniciar:** `0bac784d0d7faab9a1a7e31e10ea8db381e3cb61`  
**HEAD de main consultado:** `f4af1797e02fa3113f89385c3146ae0c4b49034e`  
**Alcance:** auditoría de solo lectura de storyboards, cola, producción, estados Grok, datos, workflows, Actions y PRs. Se escribieron únicamente este informe y una corrección documental de Kuroshio en feature.

## 1. Resultado ejecutivo

- **Feature:** 90 storyboards en `proyectos/`; ninguno tiene prefijo/fecha objetivo 25-nov. No hubo cambios de storyboard, cola ni datos editoriales desde el corte de las 14:00; el delta de feature previo a esta auditoría solo contenía los briefs `2026-11-25_CONTROL_COLA_14H.md` y `2026-11-25_RADAR_CAPCOT.md`.
- **Main:** 10 storyboards con prefijo 25-nov: nueve reworks con producción/programación preexistente y un paquete React. Los diez están fuera de feature.
- **Cola del 25-nov:** cero entradas planas. Existe una sola copia de cola del día, anidada: `cola/entrada/2026-11-25_react-bacterias-anticancer/storyboard.json` en main. Es **NOT_DISPATCHABLE**.
- **Cola histórica:** el robot orbital del 9-nov está anidado en ambas ramas. En main contiene MP4, nueve frames, subtítulos, QA audiovisual y programación; no se debe redispatchar.
- **Estados Grok:** no hay archivos JSON bajo `cola/estado/` en feature ni main. Para los expedientes consultados aplica literalmente **RECEPCION_GROK_NO_CONFIRMADA**.
- **Promociones:** cero. No se creó ninguna entrada de cola, no se movió ningún archivo y no se disparó ningún workflow.
- **Lote 5–7 nov:** los 12 QA narrativos actuales en JSON son 2 PASS y 10 FAIL; la estructura sigue 0/12 apta.
- **Kuroshio:** apareció un CI posterior al documentado. Se actualizó y releyó `ESTADO_EJECUCION.md`; la estructura sigue OK, pero DOI/Crossref permanece pendiente porque el comando no incluyó `--check-doi`.

## 2. Inventario por rama y fecha

### 2.1 Feature

- 90 archivos `proyectos/<project_id>/storyboard.json`.
- Cero proyectos con fecha/prefijo 25-nov.
- Cero JSON planos de entrada del 25-nov.
- Una entrada histórica anidada: `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/storyboard.json`.
- Cero archivos `cola/estado/*.json`.
- Un marker de handoff en `handoffs/grok_inbox/`: robot orbital, pendiente.
- 56 directorios de salida; 28 storyboard JSON en bloqueados y 61 rutas bajo `cola/bloqueados/`. No se encontró salida del 25-nov.
- El árbol de feature no contiene medios de los nueve reworks del 25-nov ni del paquete React de main.

### 2.2 Main: todos los proyectos con prefijo 25-nov

| project_id | Fecha/slot objetivo comprobado | Evidencia y clasificación |
|---|---|---|
| `2026-11-25_react-bacterias-anticancer` | 25-nov, 17:00 CDMX según `programacion.json` | Proyecto y copia anidada de cola con el mismo blob SHA `c630de2cb085bab908fed431df8085c95c63ac9b`. Sin video_id ni evidencia de render. NOT_DISPATCHABLE. |
| `2026-11-25_rehecho-barreleye-no-son-sus-ojos` | 25-nov, 15:00 | Registro `data/rehechos_2026-11-22.json`: YT `3rwo_sK1e18`. Render.log declara 87.53 s. PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. |
| `2026-11-25_rehecho-dunas-que-cantan-no-es-viento` | 28-nov, 10:00 | YT `6VUxaJtqbF0`. Render.log declara 86.70 s. PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. |
| `2026-11-25_rehecho-dunkelflaute-sin-sol-ni-viento` | 29-nov, 10:00 | YT `m1FeS0mhfZ4`. Render.log declara 88.77 s. PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. |
| `2026-11-25_rehecho-escudo-jupiter-no-es-pared` | 28-nov, 15:00 | YT `Dx3lqkAb8Sc`. Render.log declara 87.40 s. PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. |
| `2026-11-25_rehecho-miel-su-unico-enemigo` | 27-nov, 10:00 | YT `p06UCGu0-Og`. Render.log declara 86.47 s. PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. |
| `2026-11-25_rehecho-nube-500-toneladas` | 25-nov, 10:00 | YT `9RxTSifAcpo`. Render.log declara 86.80 s. PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. |
| `2026-11-25_rehecho-ola-azul-alarma-antirrobo` | 27-nov, 15:00 | YT `HKpani8TTeY`. Render.log declara 87.17 s. PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. |
| `2026-11-25_rehecho-pan-refri-endurece` | 26-nov, 10:00 | YT `7pzPfqRSagU`. Render.log declara 88.47 s. PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. |
| `2026-11-25_rehecho-ratas-topo-ayudar-no-es-cuidar` | 26-nov, 15:00 | YT `MgHVHbeIVS0`. Render.log declara 88.80 s. PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. |

**Fechas:** el registro de lote `data/rehechos_2026-11-22.json` declara creación el 22-nov. El prefijo `2026-11-25` de los project_id no demuestra por sí solo fecha de creación. Los slots 25–29 nov provienen del campo `programado_CDMX` del registro. Los storyboards de los nueve reworks no declaran `fecha_objetivo`, `slot_local` ni `slot_cesta` de forma canónica.

### 2.3 Reconciliación de la programación del 25-nov

El snapshot `data/miniaturas_auditoria_2026-11-21.json` registra para el 25-nov:

| Hora CDMX | Registro |
|---|---|
| 07:00 | `cPNiOFeY5_k` |
| 07:00 | `W9g2tPZTpD4` |
| 10:00 | Rework `9RxTSifAcpo` |
| 13:30 | `G1ByWhjfxls` |
| 15:00 | Rework `3rwo_sK1e18` |
| 17:00 | `L6ggmPAwBOA` |
| 19:00 | `A3JK0gYuqG8` |

Son siete registros programados para una capacidad diaria de cinco; 07:00 ya presenta colisión. El proyecto React añade una reserva local `programado_paquete` para 17:00, con privacidad privada y sin video_id. Esa reserva **no** demuestra programación externa, pero colisiona con `L6ggmPAwBOA`. No se debe contar como publicación ni como recepción de Grok.

A las 15:19 CDMX, los publishAt de 10:00 y 15:00 ya habían vencido. No se verificó el estado externo y `data/publicaciones.json` no contiene los dos IDs de rework; por tanto, no se afirma que se hayan publicado.

## 3. Validación de los diez storyboards de main

### 3.1 Nueve reworks

Comprobación conjunta de los nueve archivos:

- Siete escenas y 215–229 palabras por storyboard.
- `target_duration_seconds` = 88; la suma declarada de escenas más cortinilla es 76 s (70 s + 6 s). Los render.log declaran 86.47–88.80 s: **discrepancia entre storyboard y duración medida**.
- No hay campos explícitos `gancho`, `arco` ni `cierre`; `hook_type` es solo una etiqueta, no sustituye la apertura ni el payoff.
- No hay `narrative_contract` ni `narrative_qa` en los JSON.
- `estilo_id` = `foto_commons` en los nueve; ese ID no existe en el catálogo canónico de 50 estilos de `scripts/estilos.json`.
- Falta `visual_identity.prompt_base` y no hay `image_prompt` por escena.
- No hay capas mapa/gráfico/dato ni ambiente por escena. SFX sí está declarado.
- Voz declarada: `es-MX-JorgeNeural`, rate `+7%`, pitch `-2Hz`.
- Las escenas contienen `asset_filename` y el objeto export contiene `filename`; ambos contradicen el contrato de preproducción.
- `approved_assets` y `export.render_status` no están presentes.
- Los source_ids están presentes, pero no se ejecutó verificación DOI/Crossref.

Los render.log dicen que se produjo un MP4 y una portada y declaran duraciones dentro de 75–90 s. Sin embargo, los MP4, portadas y frames referenciados **no están en el árbol GitHub**. Se registra **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**; los logs no se cuentan como archivos multimedia.

No se repitió la lectura narrativa: los storyboards no cambiaron desde el corte anterior. Los JSON siguen sin `narrative_qa`. Los informes históricos discrepan: el control 24-nov 14H registró 6 PASS/3 FAIL (scores 89, 92, 82, 82, 88, 91, 82, 90, 91); el control 24-nov 22H registró 8 PASS/1 FAIL; el control 25-nov 14H volvió a resumir 6 PASS/3 FAIL. Ninguno de esos scores está persistido en los nueve JSON. Se registra la contradicción, no se elige un score como si proviniera del storyboard. Los nueve ya tienen producción/programación preexistente y no se redispatchan.

### 3.2 React — lectura en frío independiente de este run

La lectura se hizo únicamente sobre la narración concatenada, sin consultar título, resumen, arco ni notas.

- `pregunta_central_reconstruible`: true.
- `apertura_in_medias_res`: false.
- `progresion_por_escena`: false.
- `transiciones_causales`: false.
- `giro_cientifico_explicado`: false.
- `limite_evidencia_explicito`: false.
- `payoff_cierre_apertura`: false.
- **Resultado de auditoría en este informe: FAIL / 42.**
- `critical_flags`: `APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`; `PROGRESION_Y_TRANSICIONES_INSUFICIENTES`; `GIRO_CIENTIFICO_NO_EXPLICADO`; `LIMITE_EVIDENCIA_AUSENTE`; `PAYOFF_NO_CIERRA_APERTURA`; `CLAIM_4X_PENDIENTE_DE_FUENTE`.

Este resultado está registrado en este informe, no en el storyboard: el archivo pertenece a main y no se escribió en esa rama. El JSON sigue sin `narrative_contract` ni `narrative_qa`.

Comprobación estructural: seis escenas, 102 palabras, 66 s con cortinilla frente a objetivo 85 s; no hay campos `gancho`, `arco` o `cierre`. `estilo_id=linea_fina` es válido, y las seis image_prompt empiezan con el prefijo visual correspondiente, pero falta `visual_identity.prompt_base` explícito. No hay mapa ni dato/gráfico. Ambiente y SFX están presentes; voz JorgeNeural +7%/-2Hz y source_ids están presentes. DOI 10.1126/science.aee2641 aparece en sources, pero el claim “cuatro veces más rápido” permanece PENDING_SOURCE en el control anterior y no se ejecutó `--check-doi`. Seis `asset_filename` y `export.filename` están presentes; `approved_assets` y `export.render_status` faltan. Los seis archivos de frame referenciados no existen en el árbol.

La copia de cola es idéntica al proyecto (mismo blob SHA) y está en ruta anidada. `programacion.json` indica una reserva local para 25-nov 17:00, privacidad privada y ningún video_id. Se clasifica **NOT_DISPATCHABLE** y **RECEPCION_GROK_NO_CONFIRMADA**. No se promueve.

## 4. Compuerta de handoff, workflow y recepción

### 4.1 Rutas y selector

El workflow `.github/workflows/capcot-grok-dispatch.yml` existe en feature, no en main (404; PR #3 sigue abierto). En feature:

- Trigger de push: `cola/entrada/*.json`.
- Selector manual: `find ... -maxdepth 1 -name '*.json'`.
- Ruta manual construida como `cola/entrada/\${project_id}.json`.

Por tanto, carpetas anidadas como `cola/entrada/<project_id>/storyboard.json` no coinciden con los paths ni con el selector. El paquete React y el robot son **NOT_DISPATCHABLE**. No hay JSON plano actual que sí sea dispatchable.

### 4.2 Procesador y registro editorial

- `scripts/procesar_cola.py` usa la fecha CDMX actual por defecto y filtra por fecha del archivo/ruta; contempla JSON planos y storyboard anidado a un nivel. El argumento explícito `--fecha` permite seleccionar otra fecha: el comportamiento automático por defecto es del día actual, pero no es un bloqueo absoluto contra una selección histórica manual.
- `scripts/registro_editorial.py` ahora incluye `handoffs_grok_inbox()` y recorre recursivamente handoffs, proyectos, entradas, bloqueados y salidas. Esto **supersede** la nota anterior del 20-nov que decía que no recorría handoffs ni profundidades. El registro combinado sigue sin demostrar recepción individual.
- `docs/GROK_STATUS_CONTRACT.md` exige el archivo individual `cola/estado/<project_id>.json` como evidencia de recepción.

### 4.3 Handoffs y estados

- Feature: marker del robot orbital en `handoffs/grok_inbox/`, estado pending.
- Main: marker del robot y dos markers de serie del 24-nov (`serie_cuantica_evolucion` y `serie_thomas_harris`), ambos pending. Son markers, no acuses de lectura por Grok.
- `cola/estado/` no contiene JSON en ninguna de las dos ramas. Las consultas de estado para los diez proyectos del día, los doce del lote 5–7 y el robot devolvieron 404. Para cada uno aplica **RECEPCION_GROK_NO_CONFIRMADA**.
- No se creó ni modificó ningún estado Grok.

## 5. Producción preexistente: robot orbital

`2026-11-09_dato-robot-ensambla-orbita` permanece **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**.

En main, su carpeta anidada de cola contiene MP4, portada, nueve frames, SRT/ASS, metadata, programación y `qa.json`. El QA audiovisual registra 21/21 y duración medida 87.57 s; 87.57 está dentro del requisito estricto 75–90, aunque el check interno solo acepta 60–120. Ese QA no es narrative_qa.

La programación registra YouTube `ZG4iQgmWrLI`, publishAt `2026-11-22T01:00:00Z` (21-nov 19:00 CDMX), privacidad `private→public (publishAt)` y TikTok/Facebook programados sin IDs públicos. `data/publicaciones.json` incluye ese video_id. No se verificó el estado público actual.

Contradicción documental: el `ESTADO_EJECUCION.md` de main dice frames pendientes de subir y que audio/video no se generaron, pero el árbol main sí contiene MP4, portada, nueve frames, subtítulos y QA. La copia de feature no contiene esos medios y su estado ya clasifica el caso como procesamiento preexistente en main. PR #4 propone un cambio de estado para feature; sigue abierto y no se integró. No se modificó main.

## 6. Lote obligatorio 5–7 nov

Los doce project_id, fecha_objetivo, slot_local y slot_cesta coinciden con `data/horario_semana_2026-11-01_07.json`. La lectura narrativa no se repitió: los blobs no cambiaron desde el corte anterior y los QA ya están persistidos en los JSON con `review_basis=lectura_en_frio_solo_narracion` y siete checks explícitos.

| project_id | narrative_qa JSON | Score | critical_flags |
|---|---:|---:|---|
| `2026-11-05_kids-dia-en-venus` | PASS | 88 | [] |
| `2026-11-05_comida-palomitas` | FAIL | 82 | APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES; ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA |
| `2026-11-05_inter-arboles-se-comunican` | FAIL | 78 | APERTURA_GENERICA_NO_IN_MEDIAS_RES |
| `2026-11-05_inter-rayo-globular` | FAIL | 81 | APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL | 80 | PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE |
| `2026-11-06_comida-aguacate-negro` | FAIL | 79 | REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL |
| `2026-11-06_inter-ranas-congeladas` | FAIL | 83 | REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES |
| `2026-11-06_inter-arena-cantante` | PASS | 94 | [] |
| `2026-11-07_kids-huesos-bebe` | FAIL | 82 | ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION |
| `2026-11-07_comida-hielo-caliente` | FAIL | 81 | APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES |
| `2026-11-07_inter-pulpo-suenos` | FAIL | 72 | FUENTE_PRIMARIA_CORRESPONDE_A_OCTOPUS_LAQUEUS_NO_INSULARIS; REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO |
| `2026-11-07_inter-nubes-pesan` | FAIL | 78 | ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION |

**Estructura:** 85 escenas; 510 campos obligatorios ausentes (seis por escena: dramatic_beat, scene_function, causal_bridge_from_previous, question_state, reason_to_continue y new_information); 75 arrays SFX vacíos. Ambiente está presente en las 85 escenas. Once proyectos contienen mapa y dato/gráfico; Árboles no tiene ninguna de esas dos capas. Árboles tiene 169 palabras, una por debajo del mínimo. Los doce conservan cortinilla de 6 s, duración total declarada de 84 s, voice, source_ids y prompt_base. No hay asset_filename ni asset_type; approved_assets=[] y export.render_status=NOT_GENERATED.

Los dos PASS narrativos (Venus y Arena) no pasan estructura; no se promueve ninguno. No hay entrada exacta de estos doce en cola/entrada.

**Identidad:** el storyboard canónico de árboles sigue tratando redes micorrícicas comunes y Karst et al. 2023; no se marca desajuste temático. Su blob actual es distinto del histórico de 5-nov, pero el tema y la fuente primaria siguen correspondiendo. El slot 7-nov 17:45 es exactamente `2026-11-07_inter-nubes-pesan`; la variante extra en bloqueados es material de origen, no un segundo proyecto.

## 7. Backlog interdiario

No hubo storyboards nuevos ni cambios de storyboard desde el corte anterior. Se conserva el inventario heredado de 40 rutas sin compuerta narrativa, sin repetir lecturas de narraciones que no cambiaron:

**31 storyboards de 24–30 oct:**
- `2026-10-24_abejas-bullying`
- `2026-10-24_ideonella-pet`
- `2026-10-24_osedax-comehuesos`
- `2026-10-24_serpientes-que-ruedan`
- `2026-10-25_ave-jurasica-sin-vuelo`
- `2026-10-25_corales-contacto`
- `2026-10-25_reina-olor`
- `2026-10-25_sueno-electricidad-qom`
- `2026-10-26_baffin`
- `2026-10-26_catrina`
- `2026-10-26_hongo`
- `2026-10-26_papel-picado`
- `2026-10-26_papel-picado-parte2`
- `2026-10-26_pimiento`
- `2026-10-27_cempasuchil`
- `2026-10-27_corneja`
- `2026-10-27_ddm-parte3-pomuch`
- `2026-10-27_familia-ajolote`
- `2026-10-27_kids-serpiente-voladora`
- `2026-10-27_noct-anfibio-marino`
- `2026-10-28_ddm-parte4`
- `2026-10-28_familia-voyager`
- `2026-10-28_kids-titanoboa`
- `2026-10-28_monarca`
- `2026-10-28_mosquito`
- `2026-10-28_noct-lince`
- `2026-10-28_pan-de-muerto`
- `2026-10-29_juno`
- `2026-10-29_muralismo-mexicano`
- `2026-10-30_arqueas-origen-eucariotas`
- `2026-10-30_kromdraai`

**Además:** `2026-10-31_pardelas-jetlag-solar` y ocho artefactos de prueba/respaldo: `2026-11-xx_kids-flamencos-rosas_RESPALDO`, `demo-001`, `guiones_lote_01` y `lote01-01` a `lote01-05`. Permanecen sin narrativa_qa/contrato apto y fuera de cola. No se atribuyen a un investigador sin evidencia.

**Casos recientes con QA persistido:**
- `2026-11-23_supersequias-722-eventos`: FAIL/82, flag `STAKES_NO_EXPLICADOS`.
- `2026-11-23_tropical-biodiversity-turnover`: FAIL/82, flag `STAKES_NO_EXPLICADOS`.
- `2026-11-18_dato-catorce-campos-hidrotermales`: FAIL/68; sigue en proyectos, sin promoción.
- `2026-11-18_dato-kuroshio-puente-atmosferico`: PASS/90; DOI pendiente, sin promoción.

**Exclusiones absolutas respetadas:** no se leyó narración ni se creó copia para slots 23:30 de dato del día, kids 3-nov 07:00 ni Machu Picchu 4-nov 19:00. `2026-11-04_dato-polvo-atrapa-oro` se identificó solo por metadata como 4-nov 23:30, cesta dato_del_dia, y quedó excluido sin leer su narración.

## 8. Datos, temas y estilos

### Feature (rama auditada)

- `data/temas_del_dia.json`: último dato 28-oct.
- `data/rotacion.json`: último dato 31-oct.
- `data/estilos_usados.json`: último dato 28-oct.
- `data/horarios.json`: actualización 9-nov.
- `data/publicaciones.json`: 22 registros, máximo 31-oct.
- `data/cola.json`: registro del 31-oct, estado fallido.
- `data/endscreens_rotacion.json`: actualización 25-nov 08:30.

### Main (solo lectura)

- `data/temas_del_dia.json`: sigue en 28-oct.
- `data/rotacion.json`: 39 registros, máximo 21-nov.
- `data/estilos_usados.json`: 32 registros, máximo 11-nov.
- `data/horarios.json`: actualización 23-nov; no contiene slot específico del 25-nov.
- `data/publicaciones.json`: 62 registros, máximo fecha 24-nov; incluye robot orbital, no los nueve nuevos IDs de rework.
- `data/miniaturas_auditoria_2026-11-21.json`: snapshot del 21-nov; 36 programados sin MP4 local en ese corte, cuatro por rework, nueve miniaturas corregidas, 41 coincidentes con frame 0 y seis colisiones de horario. No se toma como inventario vivo posterior al 21-nov.
- `data/rehechos_2026-11-22.json`: lote de nueve reworks, con nuevos IDs y publishAt; sus IDs no aparecen en `data/publicaciones.json`.
- `data/endscreens_rotacion.json`: actualización 25-nov 14:08 CDMX, `pendiente_studio=true`.

La rama feature está atrasada frente a main en los datos editoriales. PR #3 incluye 13 archivos `data/*.json` y podría sustituir versiones más recientes de main por las antiguas de feature. No se modifica ningún JSON de datos.

## 9. Pull requests abiertos

Se consultaron los PR abiertos y sus diffs; ninguno se fusionó.

| PR | Rama origen → destino | Hallazgo |
|---|---|---|
| #3 | feature → main | Draft, mergeable=false; feature 1,414 commits ahead y 589 behind. 715 archivos cambiados, 64 storyboards y 13 data JSON. Incluye workflow, procesador y registro; no es integrable sin reconciliar el enorme desfase y los datos más nuevos de main. |
| #4 | fix/robot-frame-location → feature | Solo cambia ESTADO_EJECUCION del robot. Abierto; no se integra. |
| #6 | guardia/supervisor → main | Añade supervisor workflow y guardia config; usa secrets: inherit. No es el dispatcher CAPCOT. Abierto. |
| #7 | dependabot → main | Cambia actions/checkout a v7 en callback-aviso, gitleaks, orquestador y semgrep. No altera selector CAPCOT. |
| #8 | dependabot → main | Cambia actions/setup-python a v7 en orquestador. |
| #9 | dependabot → main | Cambia upload-sarif a v4 en semgrep. |
| #13 | worker/11 → main | Solo agrega AUDITORIA.md de Quasar; no modifica storyboard ni narrative_qa. El documento no sustituye el campo JSON. |
| #14 | chatgpt/quasar-audit-fixes-20261115 → main | OPEN/NOT MERGED; añade asset_filename a ocho escenas, no ejecuta --check-doi y conserva QA histórico FAIL/82. Incompatible con preproducción. |
| #15 | fix/capcot-map-coordinate-types-20261122 → feature (base antigua) | OPEN; modifica validador y pruebas, no hay prueba unitaria ejecutada en esta auditoría. No se integra. |

## 10. Actions y validación

- **Dispatch:** último run específico localizado `41306776689`, 1-nov, versión anterior del workflow. Error literal: `Falta configurar GROK_WEBHOOK_URL.` El log muestra ausentes las variables `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`; no se registran valores. No se encontró ejecución posterior de dispatch entre los últimos 100 runs consultados.
- **Workflow actual en feature:** webhook opcional; si no está configurado, puede dejar marker pendiente. Un marker no es acuse Grok.
- **Main:** `capcot-grok-dispatch.yml` devuelve 404; el workflow de feature no está integrado.
- **Worker:** run `45629608920`, success, 25-nov 08:01 CDMX; log literal `[trabajador] sin trabajo en cola.` Ocurrió antes del commit del paquete React (10:37 CDMX), por lo que no demuestra que el paquete posterior fuera procesado.
- **Semgrep:** run `45692100140`, failure, 25-nov 14:08 CDMX; 37 hallazgos bloqueantes; error final `Process completed with exit code 1.`
- **CodeQL:** run `45674625888`, success en PR #3; análisis de seguridad, no validación estructural ni narrativa.
- **Kuroshio:** run más reciente `45502897065`, commit `82db8f2aa2d6c58bb80a93b82a804fcc4df453c9`. Comando exacto: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`. Resultado literal `OK`; chequeo adicional confirmó `approved_assets=[]` y `export.render_status=NOT_GENERATED`. No incluyó `--check-doi` ni ejecutó tests. Los blobs de storyboard y validador coinciden con el HEAD actual de feature; DOI sigue `PENDIENTE_RESOLVEDOR`.
- No hubo runtime local del repositorio para ejecutar el validador/helpers de todos los paquetes. Esta auditoría es revisión estática de JSON/árbol GitHub más contraste de CI existentes. No se ejecutó Crossref en esta corrida.

## 11. Cambios efectuados y límites

1. Se actualizó `proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/ESTADO_EJECUCION.md` con el run posterior `45502897065`, commit, comando, resultado y bloqueo DOI. Commit de esa corrección: `331cd68451a77894004866151bfa0474b32da97c`. El archivo se releyó desde GitHub.
2. Se creó este control de cola en feature.
3. No se modificaron storyboards, narrativa, claims, decisiones editoriales, `data/*.json`, estados Grok, workflow, secretos, permisos ni main.
4. No se promovió ningún proyecto, no se movió ninguna entrada, no se disparó Actions, no se envió payload externo, no se generaron imágenes/frames/voz/audio/video/render, no se publicó y no se consumieron créditos.
5. No se revisaron cambios de API porque no apareció una actualización oficial nueva sustentada.

## 12. Precisión adicional: procedencia, privacidad e historial

- El storyboard React y su copia de cola tienen el mismo blob. El commit de esos archivos está fechado 25-nov 10:37 CDMX y el autor registrado es `marcojpad-hash`; no hay evidencia para atribuirlos al investigador CAPCOT ni a Grok.
- El registro del lote de nueve reworks declara creación 22-nov y fue committeado por Grok Bot. Eso prueba la autoría del registro, no la recepción formal por Grok ni la ejecución de QA narrativo. El prefijo 25-nov de los project_id no se toma como fecha de creación.
- Para los nueve reworks, `data/rehechos_2026-11-22.json` registra privacidad `private→public` por publishAt y estados TikTok/Facebook como programados; no aporta IDs públicos de esas plataformas. No se verificó su estado externo. Los dos publishAt del 25-nov (10:00 y 15:00) ya vencieron al corte, pero el ledger de publicaciones no confirma esos dos IDs.
- No hay `qa.json` audiovisual ni directorio `salidas/<project_id>/` para los nueve reworks. Render.log no sustituye un QA audiovisual ni verifica la existencia del MP4/portada/frame en GitHub.
- Se buscó un archivo/ruta `historial_youtube` o equivalente y no se encontró en el árbol main. No es posible reconciliar IDs desde ese historial ausente. El ID del robot sí aparece en `data/publicaciones.json` y en `programacion.json`; su publishAt ya pasó, pero no se verificó el estado público actual. Se conserva el riesgo de programación histórica obsoleta; no se elimina ni cancela nada.
- El paquete React mantiene privacidad local privada, sin video_id y sin prueba de montaje. Su reserva de 17:00 es local y colisiona con el ID existente `L6ggmPAwBOA`; no se interpreta como una segunda publicación ya programada en plataforma.


## Revalidación de continuidad — 25-nov-2026 16:01 CDMX

- HEAD de `main` al corte: `f4af1797e02fa3113f89385c3146ae0c4b49034e`. HEAD de feature antes de esta revalidación: `5412d56e52a7f1e3b994968cee6eafd78eeb35a7`. No se observó un cambio nuevo de storyboard, cola, programación o publicación en main después del control de 14H; el cambio de main sigue limitado al snapshot de pantallas de las 14:00.
- El radar se revalidó y actualizó en el commit `b2ee813b28883be7e668da3d664edf3741649f97`; lectura de vuelta confirmada. Conserva cuatro candidatos sin selección, DOI/resolvedor pendiente y ningún slot autorizado. La página HTML oficial de Google Trends México mostró 221 tendencias, 25 visibles; ninguna aportó un hallazgo científico concreto.
- El último CodeQL observado en PR #3 es run `45706674458`, SUCCESS sobre el HEAD de feature. Es análisis de seguridad; no valida estructura, DOI, narrativa, cola ni producción. Semgrep de main conserva el fallo `45692100140` con 37 hallazgos bloqueantes. PR #15 continúa abierto; no se ejecutó workflow ni se disparó CI manualmente.
- Issue #16 continúa abierto con solicitudes de enlaces, reenvío de MP4 y resubidas a TikTok/Facebook. No se ejecutaron cargas, resubidas, publicaciones ni mensajes externos.
- No se creó storyboard, no se promovió cola, no se creó/alteró estado Grok, no se generaron medios y no se modificó ningún `data/*.json`, proyecto o programación.


## Revalidación de continuidad — 25-nov-2026 18:04 CDMX

### Ramas y cambios posteriores al control de 16:01
- HEAD de feature antes de este registro: `647961d73f34b1d964526dba4bbab422d70a5eed`. El compare desde el control de auditoría `5412d56e52a7f1e3b994968cee6eafd78eeb35a7` hasta ese HEAD muestra solo cambios en `docs/briefs/2026-11-25_CONTROL_COLA.md` y `docs/briefs/2026-11-25_RADAR_CAPCOT.md`; no cambió ningún storyboard, entrada de cola ni proyecto de feature.
- HEAD de main: `8287da5dd25fa8304d9cb7b9a3b411a6ec16fe12`. El commit `pantallas 2026-11-25_17 pendiente_studio` modifica únicamente `data/endscreens_rotacion.json`: añade `snapshot_2026-11-25_17` y `propuesta_2026-11-25_17`, con `pendiente_studio=true`. No modifica storyboard, cola, horario ni publicación. La propuesta de pantallas no es una publicación ni una reserva de slot.
- Discrepancia interna del snapshot: el campo textual `motivo` conserva la referencia a `5XQfUHpyTWs (46 vistas)`, mientras `vistas_ref` registra 989 para ese ID y el snapshot nuevo enumera otros IDs. Se conserva como texto posiblemente obsoleto; no se usa para decidir ni se modifica `data/*.json`.
- La propuesta 17:00 mapea `9RBB5dFsWyA → 3rwo_sK1e18`, `qBLbjs8GiDM → L6ggmPAwBOA` y `9W9nn72rmfE → b0e7RHWudl8`; sigue pendiente de Studio. No se aplicó.

### Actions, PRs e Issues
- Worker de cola, run [45726069741](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45726069741): `completed/success`, 25-nov 18:04 CDMX. Log exacto: `[trabajador] sin trabajo en cola.` No procesó ni modificó paquetes.
- Semgrep de main, run [45718781669](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45718781669): `failure`; 37 hallazgos bloqueantes, 361 reglas, 1.260 archivos escaneados y 37 archivos mayores de 1 MB omitidos; SARIF no se subió y el proceso terminó con `exit code 1`.
- Gitleaks de main, run [45718781922](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45718781922): `success`.
- PR #3 sigue draft y sin merge; conserva 1.420 commits ahead, 589 behind y 716 archivos cambiados. CodeQL de PR #3 terminó en éxito en los runs [45706674458](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45706674458) y [45710459092](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45710459092). CodeQL es análisis de seguridad, no QA narrativo, estructural, DOI ni prueba de dispatch.
- PR #15 sigue abierto. Su HEAD `947df50e1ee895e7744e54cc43f3865c78eedf13` no tiene estados de commit; el único workflow asociado localizado es Semgrep run [45310165026](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45310165026), `failure`. No se encontró ejecución de pruebas unitarias/DOI para ese HEAD.
- Issue #16 sigue abierto con solicitudes externas de MP4, enlaces y resubidas. No se cargó material, no se publicó, no se programó y no se enviaron mensajes externos.

### Revalidación editorial
- Los nueve reworks 25–29-nov y el paquete React permanecen sin cambios desde la auditoría de 15:42. Los reworks conservan procesamiento/programación preexistentes y medios no verificados en el árbol; no se redispatchan. React conserva FAIL/42, seis escenas, 102 palabras, 66 s efectivos, entrada anidada y conflicto de 17:00; sigue `NOT_DISPATCHABLE`, `CONFLICTO_DE_SLOT_EN_MAIN` y `RECEPCION_GROK_NO_CONFIRMADA`.
- El lote 5–7-nov no cambió: 2 PASS narrativos y 10 FAIL; estructura 0/12 apta. No se repitieron PASS ni se modificaron narraciones.
- El backlog de 40 rutas sin compuerta narrativa sigue igual. No hubo nuevos storyboards.
- La ocupación 25–28-nov permanece 7/5 y 29-nov 5/5. No hay slot libre autorizado.

### Estado de ejecución
- **EJECUTADO:** relectura de ramas, compare de archivos, lectura de snapshot 17:00, inspección de Actions/logs, PRs, Issue #16, feeds RSS y Trends HTML; revalidación de candidatos por fecha primaria.
- **VERIFICADO:** no cambió ningún storyboard desde el control de 16:01; el worker terminó sin trabajo; main solo añadió snapshot/propuesta de pantallas; no hubo nueva cola ni publicación.
- **PENDIENTE:** resolver DOI/Crossref de los cuatro candidatos; resolver ocupación editorial; atender solicitudes externas solo con autorización; resolver PR #15/37 hallazgos Semgrep. No se ejecutó validador local porque no hubo checkout/runtime local disponible; la revisión fue estática y contrastada con Actions.
- Sin cambios en `data/*.json`, storyboards, cola, estados Grok, workflow, secretos, permisos, main o publicación. No se disparó ningún workflow ni se generaron medios.


## Revalidación 21:58 CDMX — correcciones y evidencia nueva

### Estado de ramas y ejecución

- CAPCOT feature: HEAD observado 813a89bf9eca09a8d9377f4b5f5f7987447f4e9b. No hay storyboard con fecha objetivo 25-nov en esta rama. El árbol contiene 90 storyboards de proyecto, una entrada antigua, 56 storyboards bajo salidas y 28 bloqueados.
- CAPCOT main: HEAD observado bb5806f65a6e927ca7e03ce5157acef361785f34. Tiene 73 storyboards de proyecto, 33 en cola/entrada y 34 bajo salidas. No existe ruta cola/estado/ ni archivo historial_youtube en el árbol de main o feature.
- La ejecución del trabajador 45726069741 terminó SUCCESS con “sin trabajo en cola”. Gitleaks terminó SUCCESS; Semgrep sigue FAILURE con 37 hallazgos bloqueantes. El último run de validar-kuroshio en feature terminó SUCCESS. No se disparó ningún workflow ni se envió payload.
- El issue #16 sigue abierto con solicitudes de MP4, resubidas de TikTok y Pancho EN. No hubo carga, publicación ni mensaje externo.

### React: conflicto confirmado y clasificación

Se confirma que el paquete React de main y el video L6ggmPAwBOA reservan exactamente 2026-11-25 17:00 CDMX / 2026-11-25T23:00:00Z:

- React: proyectos/2026-11-25_react-bacterias-anticancer/programacion.json declara fecha_objetivo 2026-11-25, slot_local 17:00 y publish_at 2026-11-25T23:00:00Z.
- L6ggmPAwBOA: data/miniaturas_auditoria_2026-11-21.json lo identifica como “Francia NO pagó toda la Estatua de la Libertad #Shorts”, estado programado, publishAt 2026-11-25T23:00:00Z y hora CDMX 17:00.
- La misma auditoría de miniaturas ya registraba otra colisión para el 25-nov a las 07:00: cPNiOFeY5_k y W9g2tPZTpD4. El archivo registra seis pares de colisión entre el 23 y el 28-nov.
- La colisión de las 17:00 es interna a main. Feature no contiene un storyboard para ese mismo slot; por tanto, no se etiqueta como CONFLICTO_DE_SLOT_ENTRE_RAMAS.

El paquete React permanece NOT_DISPATCHABLE y PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR: el storyboard tiene seis escenas, 102 palabras narradas y 66 segundos totales incluyendo cortinilla; contiene asset_filename y export.filename, carece de narrative_qa y narrative_contract, y la copia de cola es idéntica pero está anidada en cola/entrada/<project_id>/storyboard.json. El workflow solo recoge cola/entrada/*.json en profundidad plana. No existe cola/estado/<project_id>.json: RECEPCION_GROK_NO_CONFIRMADA. El estado externo del video L6ggm no pudo verificarse; el fetch de la página de YouTube devolvió DisabledError. No se presume que se haya publicado por haber pasado publishAt.

### Nueve reworks: procesamiento previo, política horaria y medios

Los nueve registros de data/rehechos_2026-11-22.json contienen video_id y publishAt; los nueve render.log del árbol terminan OK, con duraciones reportadas entre 86.47 y 88.80 s. Barreleye conserva un aviso de cortinilla fuera de zona segura. Los MP4 se referencian con rutas absolutas de /workspace, pero no aparecen en el árbol GitHub ni en salidas/<id>/: MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO. Los nueve se clasifican PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR.

Sus horas programadas son 10:00 y 15:00 CDMX entre el 25 y el 29-nov. La política vigente en data/horarios.json, con corte 2026-11-23, solo declara ventanas 06:30–07:30 y 16:30–18:00, más el slot fijo 23:30. Las horas 10:00 y 15:00 quedan FUERA_DE_VENTANA. No se modifican ni cancelan programaciones preexistentes.

### Defecto del inventario automático de ocupación

scripts/registro_editorial.py no incorpora data/rehechos_2026-11-22.json ni data/miniaturas_auditoria_2026-11-21.json. registros() solo carga publicaciones.json, rotacion.json, cola.json y storyboards del árbol; ocupacion_slots() añade horario_*.json y JSON de proyectos/cola/salidas, pero no lee los dos inventarios que contienen los nueve publishAt y las seis colisiones.

Consecuencia: el cálculo automático de ocupación no ve toda la programación real. Los valores 7/5 y 5/5 de controles anteriores no quedan reproducidos de manera independiente con el inventario actual; se reclasifican OCUPACION_NO_CONCILIADA, no como dato verificado. Para el 25-nov sí están comprobados el par de las 07:00, L6ggm a las 17:00 y la reserva duplicada de React a las 17:00. No se crea un storyboard porque no hay un slot libre demostrado. La corrección del lector de inventario requiere prueba unitaria antes de cablearse; no se modifica código en este run.

### Reconciliación de anfibio marino y pantallas finales

Se corrige la conclusión previa de que 5XQfUHpyTWs no tenía mapeo:

- salidas/2026-10-27_noct-anfibio-marino/publicacion.json lo vincula con “Anfibio marino: hallan el primero que vivió en el mar”.
- data/horario_2026-10-27.json registra el slot 23:30 y el video_id 5XQfUHpyTWs.
- El snapshot de API de YouTube guardado en pendientes/analisis/datos_2026-11-17/yt_videos_api.json lo muestra público con 987 vistas; vistas_historico del 24-nov registra 989.
- El publicacion.json de salidas sigue mostrando privacyStatus private y publishedAt 2026-10-27T05:31:36Z, en contradicción con el snapshot posterior y el horario de 2026-10-28T05:30:00Z. Se marca PUBLICACION_JSON_DESACTUALIZADO / TIMESTAMP_DISCREPANTE.
- rotacion.json mantiene dos filas para noct-anfibio-marino con camas distintas y sin yt_id; publicaciones.json no contiene la entrada. El mapeo correcto está en salidas y horario, no en esas dos tablas.

La propuesta de pantallas 20:00 sigue pendiente de Studio; el último registro aplicado continúa en 08:07. El snapshot 20:00 muestra 5XQfUHpyTWs=989, N21TIYdONZo=124, 5D96DmjvioU=641 y L6ggmPAwBOA=1. N21TIYdONZo corresponde a Salem. El motivo de la propuesta que atribuye 46 vistas a 5XQ está desactualizado; 46 pertenece a un valor antiguo de referencia y no coincide con el snapshot actual. No se modifica data/endscreens_rotacion.json ni se opera Studio.

### Compuertas y secretos

- Los estados individuales de Grok no existen en el árbol revisado; cualquier proyecto sin archivo individual conserva RECEPCION_GROK_NO_CONFIRMADA. Los handoff markers no sustituyen el acuse.
- Se intentó consultar solo los nombres de secrets de Actions para comprobar GROK_WEBHOOK_URL y GROK_WEBHOOK_TOKEN. El endpoint de GitHub fue rechazado por el conector con INVALID_ARGUMENT: “GitHub Fetch URL is not an allowed public GitHub repository or search endpoint.” No se consultaron ni expusieron valores; la presencia de ambos nombres queda NO_VERIFICADA.
- No se modificaron data/*.json, cola/entrada, cola/estado, salidas, main, secretos, permisos, programación, ni publicaciones.
