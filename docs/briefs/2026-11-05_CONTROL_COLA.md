# CONTROL DE COLA CAPCOT — 2026-11-05

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Corte:** 2026-11-05 15:18 CDMX  
**Rol:** auditoría; no producción ni publicación.

## Resultado ejecutivo

- Se localizaron **12 storyboards canónicos** del lote 5–7 nov: cuatro del día 5, cuatro del 6 y cuatro del 7.
- QA narrativo en frío releído y actualizado en GitHub: **2 PASS** (Venus 88, dunas 94) y **10 FAIL**.
- **0/12 superan la estructura de preproducción**. Los doce carecen de los seis campos narrativos obligatorios en cada escena. Por eso, incluso los dos PASS narrativos permanecen fuera de cola.
- `cola/entrada/` no contiene JSON activos. No se promovió ningún borrador.
- Para los doce IDs, `cola/estado/<project_id>.json` devuelve 404: **RECEPCION_GROK_NO_CONFIRMADA**.
- Los doce paquetes son **NOT_DISPATCHABLE** desde sus ubicaciones actuales en `proyectos/`.
- No hay salidas, IDs de plataforma ni evidencia de producción para ninguno de los doce.
- No se generaron medios, no se publicó, no se disparó ningún workflow, no se enviaron payloads y no se consumieron créditos.

## 1. Briefs y alcance

Briefs encontrados y leídos:

- [Radar 5 nov](2026-11-05_RADAR_CAPCOT.md)
- [Radar 6 nov](2026-11-06_RADAR_CAPCOT.md)
- [Radar 7 nov](2026-11-07_RADAR_CAPCOT.md)

El radar del 5 nov contiene una sección inicial obsoleta que dice que los cuatro paquetes están en cola y asigna 19:00 al rayo globular. Una corrección posterior del mismo documento aclara que los cuatro canónicos están en `proyectos/`, que ninguno está en `cola/entrada/` y que el segundo intermedio pasó a 17:45. Los radares del 6 y 7 nov todavía conservan en sus secciones iniciales 19:00 y la frase “cuatro paquetes en cola”; sus secciones posteriores aclaran que los borradores están bloqueados y fuera de `cola/entrada/`, pero no incorporan la corrección horaria. La fuente vigente es [data/horario_semana_2026-11-01_07.json](../../data/horario_semana_2026-11-01_07.json), que fija los slots intermedios en 17:00 y 17:45. [docs/HORARIOS_PUBLICACION.md](../HORARIOS_PUBLICACION.md) también dice que desde el 5 nov no se programa 19:00.

No se revisaron los slots excluidos: dato del día 23:30, kids 3-nov 07:00 ni Machu Picchu 4-nov 19:00.

### Fechas de creación y actualización

Los doce directorios de `proyectos/` contienen únicamente `storyboard.json`; no contienen `ESTADO_EJECUCION.md`. El historial de Git sitúa la creación común del lote en **2026-11-02 16:11 CDMX**. Las últimas modificaciones previas a esta auditoría fueron el **4 nov, entre 16:08 y 16:15 CDMX**. La fecha de creación no se confunde con la fecha objetivo del proyecto. No atribuyo la redacción a una ejecución del investigador CAPCOT: el commit de origen registra el staging del lote y no acredita por sí solo quién redactó cada narración.

## 2. Inventario de los doce proyectos

La comparación de `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` con el horario semanal dio **12/12 coincidencias**. Los doce slots tienen estado de horario `pedir_chatgpt`: asignación/propuesta, no selección de Grok.

| Fecha objetivo | Project ID | Slot / cesta | Palabras / escenas | QA narrativo releído | Dispatch |
|---|---|---|---:|---|---|
| 05 nov | `2026-11-05_kids-dia-en-venus` | 07:00 / kids | 170 / 7 | PASS 88 | NOT_DISPATCHABLE |
| 05 nov | `2026-11-05_comida-palomitas` | 13:30 / comida_familia | 173 / 7 | FAIL 82 | NOT_DISPATCHABLE |
| 05 nov | `2026-11-05_inter-arboles-se-comunican` | 17:00 / intermedio_1 | 169 / 8 | FAIL 78 | NOT_DISPATCHABLE |
| 05 nov | `2026-11-05_inter-rayo-globular` | 17:45 / intermedio_2 | 197 / 7 | FAIL 81 | NOT_DISPATCHABLE |
| 06 nov | `2026-11-06_kids-ballena-azul-corazon` | 07:00 / kids | 174 / 7 | FAIL 80 | NOT_DISPATCHABLE |
| 06 nov | `2026-11-06_comida-aguacate-negro` | 13:30 / comida_familia | 170 / 7 | FAIL 79 | NOT_DISPATCHABLE |
| 06 nov | `2026-11-06_inter-ranas-congeladas` | 17:00 / intermedio_1 | 177 / 7 | FAIL 83 | NOT_DISPATCHABLE |
| 06 nov | `2026-11-06_inter-arena-cantante` | 17:45 / intermedio_2 | 206 / 7 | PASS 94 | NOT_DISPATCHABLE |
| 07 nov | `2026-11-07_kids-huesos-bebe` | 07:00 / kids | 172 / 7 | FAIL 82 | NOT_DISPATCHABLE |
| 07 nov | `2026-11-07_comida-hielo-caliente` | 13:30 / comida_familia | 172 / 7 | FAIL 81 | NOT_DISPATCHABLE |
| 07 nov | `2026-11-07_inter-pulpo-suenos` | 17:00 / intermedio_1 | 170 / 7 | FAIL 80 | NOT_DISPATCHABLE |
| 07 nov | `2026-11-07_inter-nubes-pesan` | 17:45 / intermedio_2 | 221 / 7 | FAIL 78 | NOT_DISPATCHABLE |

Los doce JSON fueron releídos después de escribir el QA. En todos consta `review_basis="lectura_en_frio_solo_narracion"`, los siete checks explícitos y `reviewed_at="2026-11-05T15:18:57-06:00"`. Los scores y statuses de la tabla son los valores exactos releídos desde GitHub.

### Flags de QA narrativo

- **Venus — PASS 88:** siete checks true; `critical_flags=[]`.
- **Palomitas — FAIL 82:** `APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`; `ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA`.
- **Árboles — FAIL 78:** `APERTURA_GENERICA_NO_IN_MEDIAS_RES`.
- **Rayo globular — FAIL 81:** `APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES`.
- **Ballena — FAIL 80:** `PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE`.
- **Aguacate — FAIL 79:** `REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL`.
- **Ranas — FAIL 83:** `REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES`.
- **Dunas — PASS 94:** siete checks true; `critical_flags=[]`.
- **Huesos — FAIL 82:** `ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION`.
- **Efecto Mpemba — FAIL 81:** `APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES`.
- **Pulpos — FAIL 80:** `REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO`.
- **Nubes — FAIL 78:** `ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION`.

La lectura de árboles respeta la identidad corregida: el canónico `2026-11-05_inter-arboles-se-comunican`, blob previo `854c12ed9b77f82f66ec736797dea4d700983d78`, trata la red micorrícica común y Karst et al. 2023. **No tiene desajuste temático.** Falla por apertura genérica y estructura, no por tema. La variante sobre respiración nocturna es otro artefacto bloqueado con otro `project_id`.

La identidad del slot de nubes también se conserva: **17:45 corresponde exactamente a `2026-11-07_inter-nubes-pesan`**. `2026-11-07_extra-nubes-pesan` es material de origen, no un segundo proyecto.

## 3. Validación estructural y de preproducción

Comprobaciones comunes a los doce:

- Esquema `CAPCOT_STORYBOARD_TEXT_V2`, serie, idioma `es-MX`, formato 9:16 y exportación 1080×1920 presentes.
- 7–8 escenas; duración de escenas 78 s + cortinilla de 6 s = **84 s**; objetivo 84 s.
- Gancho de 3–5 palabras; arcos declarados; cierre oral “Esto fue Datos y ociosidades.”
- Voz `edge-tts / es-MX-JorgeNeural`, tasa +7%, pitch −2 Hz: coincide en los doce.
- `narrative_contract` completo en los doce.
- `source_ids` de escenas y cortinilla referencian IDs existentes; no hay IDs huérfanos.
- `approved_assets=[]`, `export.render_status=NOT_GENERATED`, `audio.music_asset=null`; no aparecen `asset_filename`, `asset_type`, rutas de medios ni nombres de archivos de render.
- Once proyectos tienen mapa con puntos, coordenadas dentro de rango y fuente, además de capa de dato/gráfico con fuente. Árboles carece de ambas capas.
- No se detectaron errores de duración de escena ni referencias de asset que haya que verificar.

**Bloqueo estructural decisivo:** las seis propiedades exigidas por la plantilla vertical —`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information`— faltan en todas las escenas de los doce proyectos: 42 propiedades ausentes por cada storyboard de 7 escenas y 48 en árboles, de 8 escenas. El JSON y las etiquetas de arco no sustituyen esas funciones narrativas. Por este motivo el validador estructural no pasa en ninguno, incluidos Venus y dunas.

Hallazgos adicionales:

- Árboles: 169 palabras, por debajo del mínimo 170; no tiene mapa ni capa de dato/gráfico; los ocho `image_prompt` no comienzan con el `prompt_base` literal del estilo.
- SFX: diez proyectos tienen arrays `sfx` vacíos en todas las escenas y ambiente genérico (“ambiente/cama discreta; voz al frente”), sin declarar explícitamente silencio. Rayo y dunas tienen cues SFX en cinco de siete escenas cada uno. El manifiesto SFX documenta fuentes de audio, pero dice que los archivos no se commitean; los cues no se contaron como medios.
- Los doce `estilo_id` existen en el catálogo y no hay repetición de estilo dentro de un mismo día. La secuencia no repite el estilo de los tres outputs conocidos del 4 nov. El registro `data/estilos_usados.json` está atrasado, por lo que no sirve por sí solo como historial actualizado.
- El catálogo asocia débilmente los temas de Venus con `constructivista_ruso`, palomitas con `papel_recortado_popup`, rayo con `pixel_art`, Mpemba con `satira_periodico` y pulpos con `amigurumi`. Es una alerta de coherencia de estilo, no un error estructural automático.
- Metadatos de fuente por revisar: en palomitas, `trend_source.url` apunta al DOI 10.1093/chemse/bjr071, mientras `SRC-001` y el horario citan Virot & Ponomarenko 2015, DOI 10.1098/rsif.2014.1247. En pulpos, `trend_source.url` apunta a 10.1016/j.isci.2021.102223, mientras `SRC-001` y el horario citan Pophale et al. 2023, DOI 10.1038/s41586-023-06203-4. Árboles registra dos IDs de fuente para el mismo DOI de Karst et al.; es duplicación de referencia, no cambio de tema.
- La revisión de DOI fue estática: no se ejecutó comprobación en vivo de Crossref/resolvedor.

## 4. Cola, dispatch y recepción Grok

### Cola y rutas

- `cola/entrada/`: sin JSON; solo archivo de mantenimiento.
- `cola/estado/`: no hay estados para ninguno de los doce; las doce lecturas individuales de `cola/estado/<project_id>.json` devolvieron 404. Para cada uno aplica literalmente **RECEPCION_GROK_NO_CONFIRMADA**.
- `handoffs/grok_inbox/`: solo README; sin marcadores pendientes.
- `handoffs/grok_done/`: solo `.gitkeep`; sin acuses.
- Los doce storyboard vigentes están en `proyectos/<project_id>/storyboard.json`. Todos son **NOT_DISPATCHABLE** desde esa ruta.
- No había copia activa en `cola/entrada/` que debiera moverse a bloqueados. Las copias antiguas ya ubicadas en `cola/bloqueados/` permanecen allí; no se descartó ni movió contenido.

### Workflow y procesador

[Workflow actual](../../.github/workflows/capcot-grok-dispatch.yml):

- El trigger push escucha `cola/entrada/*.json`, es decir, JSON de primer nivel.
- El dispatch manual busca con `find cola/entrada -maxdepth 1 -type f -name '*.json'`; tampoco descubre carpetas por proyecto.
- La ruta `cola/entrada/<id>/storyboard.json` que acepta el procesador no coincide con el selector del workflow.
- La ruta contractual compatible con el workflow es `cola/entrada/<project_id>.json`, pero no se promocionó ningún paquete porque los doce fallan estructura.

[scripts/procesar_cola.py](../../scripts/procesar_cola.py) toma por defecto `fecha_actual_cdmx()` y filtra entradas por la fecha derivada del nombre del archivo/directorio. Por defecto selecciona solo la fecha actual. Tiene un override explícito `--fecha AAAA-MM-DD`, por lo que un operador puede solicitar deliberadamente una fecha histórica. El procesador busca JSON de primer nivel y `*/storyboard.json`. `rotacion.py` usa `registro_editorial.py` para reconciliar proyectos, cola y salidas al contar temas/cupos; no depende únicamente del `data/temas_del_dia.json` atrasado. El comentario de ventanas de `rotacion.py` aún enumera 19:00, aunque la programación semanal vigente usa 17:45.

### Actions

Las diez ejecuciones más recientes disponibles del workflow son las runs **138–147**, todas del 1 nov y todas fallidas en “Verificar configuración del receptor”. Los logs repiten el error literal:

`Falta configurar GROK_WEBHOOK_URL.`

La etapa “Entregar paquetes y exigir acuse individual” quedó omitida. La run #147 (ID 41306776689) correspondió al commit `c2791e806fbf44940f4dd87b64753ba48e04da6f`, que modificó `cola/entrada/2026-11-07_inter-nubes-pesan.json`; el paso de validación dijo que había un paquete, pero el paso de configuración falló antes de la entrega. El blob de esa copia está ahora en bloqueados. El log incluye la comprobación de `GROK_WEBHOOK_TOKEN`, pero no llegó a ejecutarla porque falló primero la URL. No se muestran valores de secretos.

La versión actual del workflow en la rama ya usa webhook opcional y crea un marcador `pending` en `handoffs/grok_inbox/` cuando no hay credenciales; no hay ejecución posterior que demuestre ese comportamiento. Un marcador de inbox tampoco equivale a recepción Grok ni crea `cola/estado/<id>.json`. No se atribuye recepción por el mero hecho de que un JSON haya existido en GitHub.

## 5. Reconciliación editorial, estilos y archivos históricos

### Estados por etapa

- **Propuesta/asignación:** los doce aparecen en el horario semanal con `estado="pedir_chatgpt"`.
- **Recibido por Grok:** ninguno acreditado.
- **Seleccionado:** ninguno acreditado.
- **Producción:** ninguno; los doce dicen `production_mode="storyboard_only"`, `approved_assets=[]` y `NOT_GENERATED`.
- **QA:** solo QA narrativo; dos PASS y diez FAIL. No hay QA audiovisual para estos doce.
- **Publicado/programado:** ninguno de estos doce tiene carpeta en `salidas/`, ID de YouTube ni evidencia de programación en YouTube/TikTok/Facebook. `publicacion.status` sigue en `PENDIENTE_DECISION_GROK`.

### Datos maestros atrasados

- El horario semanal 1–7 nov es la asignación vigente y coincide con los doce IDs.
- `data/temas_del_dia.json` y `data/estilos_usados.json` llegan hasta el 28 oct.
- `data/rotacion.json`, `data/publicaciones.json` y `data/cola.json` contienen registros hasta el 31 oct, no el lote 5–7.
- `data/vistas_historico.json` y `data/balances_6h.json` llegan hasta el 28 oct.
- `data/endscreens_rotacion.json` sí incluye la actividad del 4 nov.
- `registro_editorial.py` une los registros canónicos con storyboards de proyectos, cola y salidas; no se ejecutó por falta de runtime local.

### Copias bloqueadas y variantes

Las copias bajo `cola/bloqueados/` no son entradas activas. Se encontraron variantes antiguas con IDs distintos: `2026-11-05_comida-palomitas-explotan`, `2026-11-05_inter-arboles-mito-respiran`, `2026-11-05_inter-venus-dia-largo`, `2026-11-06_inter-corazon-ballena-azul`, `2026-11-07_inter-mpemba-mito` y `2026-11-07_inter-suenos-pulpo`. La variante de respiración nocturna no reemplaza al canónico de red micorrícica. La carpeta `2026-11-07_extra-nubes-pesan` se etiqueta `MATERIAL_DE_ORIGEN_NO_ES_PROYECTO`.

Los `ESTADO_EJECUCION.md` de las carpetas bloqueadas inspeccionadas indican `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; la carpeta extra de nubes indica material de origen. En cambio, algunos JSON sueltos dentro de bloqueados conservan `estado="PENDIENTE_REVISION_GROK"`. Esa etiqueta contradice su ubicación bloqueada y no demuestra recepción; no se cambió.

### Guardia de producción y publicaciones previas

Ninguno de los doce IDs tiene `salidas/<project_id>/`, `qa.json`, `publicacion.json`, `metadata.json`, `licencias.json`, ID de YouTube ni programación conocida. No aplica `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` a estos doce porque no hay procesamiento previo.

Separadamente, existen tres outputs del 4 nov con IDs de YouTube y estados privados/programados: Hipo `Rg-iTgMExWw` (07:00), miel `jpDyCX6zSgQ` (13:30) y bioluminiscencia `4xylLT3vSIU` (17:00). Sus registros también muestran programación de TikTok/Facebook. No tienen `qa.json`; son procesamiento preexistente y no deben redispatcharse. La metadata de bioluminiscencia referencia estudios/DOI de miel, una discrepancia de fuentes que queda señalada sin modificar la salida.

No se encontró un archivo independiente llamado `historial_youtube` en `data/` ni en `salidas/_ops/`. Sí hay riesgo de duplicado en el historial disponible: `data/publicaciones.json` y los horarios históricos de 28 y 31 oct conservan IDs pasados con estados `private→public (publishAt)` o `programado_yt`. Ejemplos: `IzWU_1BXq3Q`, `GHxm9dDUMmM`, `bYGd7QuenSk`, `PBDMJxOkCRk`, `ivVo2H9NaEU`, `GYxjXDh1ahc`, `YKldyldCeiQ`, `Mz-IVFvFWH4`, `G5is50omLo4`, `ILDMoFhsH74` y `MSiwJnSu_Dk`. No se intentó cancelar ni borrar nada en plataformas externas.

## 6. Ejecución y cambios de esta auditoría

- Se actualizó únicamente `narrative_qa.reviewed_at` en los doce storyboards, conservando status, score, checks, flags, narración, claims y fuentes. Los doce archivos se releyeron desde GitHub y los valores de QA de este reporte coinciden con esa lectura.
- Se creó este reporte en `docs/briefs/2026-11-05_CONTROL_COLA.md`.
- No se modificó `data/*.json`, `main`, workflow, secretos, permisos, `cola/estado/`, decisiones editoriales, narraciones ni claims.
- No se promovieron paquetes ni se movieron copias bloqueadas: `cola/entrada/` estaba vacía y los doce fallan estructura.
- No se dispararon Actions ni webhooks. No se generaron imágenes, frames, voz, audio, video o renders. No se publicó ni se gastaron créditos.
- No hay runtime local del repositorio: **no se ejecutó** `validar_storyboard.py`, `registro_editorial.py` ni helpers. La validación fue estática, contrastando los JSON con las reglas del validador y la plantilla. La comprobación de DOI fue estática.
- No se abrió revisión de APIs: los archivos del día no señalan un cambio oficial nuevo que justifique esa revisión.

**Decisión de auditoría:** mantener los doce en `proyectos/`. Venus y dunas pasan narrativa, pero no estructura. Los otros diez fallan narrativa y estructura. No hay ningún paquete listo para promoción ni recepción Grok confirmada.
