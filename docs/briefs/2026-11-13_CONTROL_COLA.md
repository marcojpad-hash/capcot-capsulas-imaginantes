# CONTROL DE COLA CAPCOT — 2026-11-13

Rama auditada: `feature/capcot-video-discovery-continuity`.
Rol: auditor independiente. No se produjeron cápsulas ni medios, no se publicaron contenidos, no se dispararon workflows ni se enviaron payloads externos.

## 1. Briefs y alcance

- Leídos: `docs/briefs/2026-11-13_RADAR_CAPCOT.md`, `docs/briefs/2026-11-12_CONTROL_COLA.md`, Plan Maestro, contrato operativo, Receta, Guía del modelo externo, Flujo Externo, contrato de estado Grok, QA narrativo en frío, plantillas genérica y vertical, catálogo de estilos, `scripts/validar_storyboard.py`, `scripts/procesar_cola.py`, `scripts/registro_editorial.py` y los JSON operativos disponibles bajo `data/`.
- El radar 13-nov es una instantánea anterior a esta auditoría: registraba el storyboard del día sin `narrative_qa`. Esta auditoría añadió y releyó ese campo; no se reescribió el radar.
- No se ejecutaron cambios en APIs: el documento técnico registra Graph API v27.0 (anuncio 4-nov) pero la referencia oficial de Meta no pudo confirmarse por HTTP 429. No apareció un cambio oficial nuevo verificable que justifique otra revisión.

## 2. Inventario del 13 de noviembre

| Ruta | Fecha de creación | Fecha objetivo | Slot | Estado |
|---|---|---|---|---|
| `proyectos/2026-11-13_dato-caracol-16-embriones/storyboard.json` | 13-nov (incorporación registrada en el radar, commit `e10ecc27`) | 2026-11-13 | 17:00, staging; `slot_cesta` ausente | PROPUESTA_PENDIENTE_DE_GROK |

- Es el único storyboard de fecha objetivo 13-nov encontrado en `proyectos/`.
- No hay JSON plano `cola/entrada/2026-11-13_*.json` ni carpeta `cola/entrada/2026-11-13_*/storyboard.json`.
- No hay `salidas/2026-11-13_dato-caracol-16-embriones/`, `cola/bloqueados/2026-11-13_dato-caracol-16-embriones/`, `handoffs/grok_inbox/2026-11-13_dato-caracol-16-embriones.json` ni `ESTADO_EJECUCION.md`.
- `cola/estado/2026-11-13_dato-caracol-16-embriones.json` devuelve 404: **RECEPCION_GROK_NO_CONFIRMADA**.
- `data/horario_2026-11-13.json` no existe. `data/horarios.json` solo define ventanas; 17:00 cae en la ventana vespertina 16:30–18:00, pero viernes no es día preferente de tarde. El radar lo define como slot de staging, no hora de publicación. Sin `slot_cesta` ni asignación diaria no se declara seleccionado.

### 2.1 QA narrativo en frío — caracol fósil

Se leyó únicamente la narración concatenada, sin título, resumen, arco, notas ni `narrative_contract`.

- `narrative_qa.status`: **PASS**.
- `score`: **91**.
- `review_basis`: `lectura_en_frio_solo_narracion`.
- `reviewer_role`: `auditor_capcot_independiente`.
- `reviewed_at`: `2026-11-13T15:42:39-06:00`.
- Siete checks: todos `true` (`pregunta_central_reconstruible`, `apertura_in_medias_res`, `progresion_por_escena`, `transiciones_causales`, `giro_cientifico_explicado`, `limite_evidencia_explicito`, `payoff_cierre_apertura`).
- `critical_flags`: `[]`.
- Lectura: la tomografía abre con una anomalía ya en curso; la distribución de embriones plantea la pregunta, la muestra y el gradiente de tamaños desarrollan el giro hacia ovoviviparidad, los residuos digestivos amplían la evidencia de dieta, y la hipótesis de ceniza alcalina explica la preservación sin presentarse como hecho observado. El cierre vuelve a la concha.

### 2.2 Preflight estructural estático — caracol fósil

- 8 escenas; 78 s de escenas + cortinilla de 6 s = 84 s.
- 210 palabras de narración; gancho de 5 palabras.
- Arcos completos; cierre oral con el sello del canal.
- Voz `es-MX-JorgeNeural`, `+7%`, `-2Hz`; `source_ids` de escenas y cortinilla resuelven a fuentes declaradas.
- `dibujo_cientifico_scratchboard` existe en el catálogo; `visual_identity.prompt_base` coincide literalmente y los 8 prompts comienzan con ese texto.
- Hay escena de mapa y escena de dato/gráfico; ambiente y SFX no vacíos en las 8 escenas.
- `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type`, `export.filename` ni rutas de medios.
- La fuente primaria `SRC-001`, DOI `10.1038/s42003-026-11188-7`, conserva `verification_status=PENDIENTE_RESOLVEDOR`. No se presenta como DOI verificado. El validador `--check-doi` intenta confirmar por Crossref; no se ejecutó.
- Revisión estática: sin errores de esquema detectados; queda pendiente la comprobación real del resolvedor y la ejecución del validador.

### 2.3 Handoff y decisión de promoción

- El storyboard permanece en `proyectos/`; por ruta es **NOT_DISPATCHABLE**.
- No se creó copia en `cola/entrada/`. El workflow se activa al hacer push de `cola/entrada/*.json`; promoverlo habría disparado el workflow, en contradicción con la instrucción explícita de no dispararlo ni enviar payloads.
- Tampoco se ejecutó el validador real porque no se obtuvo runtime local. Por tanto, PASS narrativo no equivale a validación ejecutable, selección editorial, recepción Grok ni autorización de producción.
- El archivo sigue con `editorial_status=PROPUESTA_PENDIENTE_DE_GROK` y `publicacion.status=PENDIENTE_DECISION_GROK`.

## 3. Cola y dispatchabilidad

### Entradas de fecha 13-nov

- **0** entradas planas.
- **0** entradas anidadas.
- No existe estado Grok ni marcador de handoff para el proyecto del día.

### Entradas históricas visibles en la rama feature

| Ruta | Fecha del ID | Dispatch | Estado Grok |
|---|---|---|---|
| `cola/entrada/2026-11-07_dato-clavo-te-cocina/storyboard.json` | 7-nov | **NOT_DISPATCHABLE**: carpeta anidada | `RECEPCION_GROK_NO_CONFIRMADA` (404) |
| `cola/entrada/2026-11-11_dato-ratas-topo-damaraland/storyboard.json` | 11-nov | **NOT_DISPATCHABLE**: carpeta anidada | `RECEPCION_GROK_NO_CONFIRMADA` (404) |

Estas dos rutas se registran solo para inventario de cola y dispatchabilidad. Los slots 23:30 de dato del día están excluidos de la revisión narrativa del lote 5–7; no se emitió QA editorial ni se movieron.

El paquete de ratas topo conserva además un `fuentes.md` separado y el formato legado de plantilla genérica. No se toma como evidencia de medios generados ni de recepción. No se modificó.

### Workflow y procesador

- `.github/workflows/capcot-grok-dispatch.yml` escucha `cola/entrada/*.json`; el selector usa profundidad máxima 1 y regex `^cola/entrada/[^/]+\.json$`. No encuentra carpetas `cola/entrada/<id>/storyboard.json`.
- `workflow_dispatch` también enumera solo JSON de primer nivel.
- El workflow escribe un marcador `handoffs/grok_inbox/<id>.json` con `status=pending`; ese marcador no es acuse de recibo. Solo `cola/estado/<id>.json` constituye la evidencia exigida por el contrato.
- `scripts/procesar_cola.py` usa por defecto la fecha CDMX actual, pero admite `--fecha` para seleccionar otra fecha. Acepta tanto JSON plano como carpetas anidadas y filtra por prefijo de ruta; no contrasta la fecha del nombre con `fecha_objetivo` dentro del JSON. Por tanto, el comportamiento por defecto es diario, pero el código no impide seleccionar históricos mediante override.
- `scripts/registro_editorial.py` recorre `proyectos`, `cola/entrada`, `cola` y `salidas` a una profundidad limitada. No integra `cola/bloqueados`, `handoffs/grok_inbox`, cierres diarios externos ni el horario semanal; tampoco mantiene un ledger completo de estilos. Puede omitir evidencia de publicación que sí aparece en los cierres diarios de `main`.

### Actions

No se pudo obtener un listado actualizado de ejecuciones ni logs: el conector disponible no expone una acción de listado de workflow runs y el acceso web al endpoint de GitHub no respondió en esta sesión. No se atribuye un error nuevo ni se afirma que falten `GROK_WEBHOOK_URL` o `GROK_WEBHOOK_TOKEN`. El error antiguo `Falta configurar GROK_WEBHOOK_URL.` del run #147 (1-nov) no se presenta como último run; el workflow actual trata el webhook como opcional y usa el buzón del repositorio.

## 4. Lote obligatorio 5–7 noviembre

Los 12 proyectos fueron releídos en frío. Se compararon `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` contra `data/horario_semana_2026-11-01_07.json`: **12/12 coincidencias**. El slot 7-nov 17:45 corresponde exactamente a `2026-11-07_inter-nubes-pesan`. El storyboard canónico de árboles trata redes micorrícicas comunes y Karst et al. 2023; no se marcó desajuste temático. La variante de respiración nocturna no se confundió con ese canónico.

| ID | Slot | QA frío releído | Fallo/flag principal |
|---|---:|---|---|
| `2026-11-05_kids-dia-en-venus` | 07:00 kids | **PASS 88** | — |
| `2026-11-05_comida-palomitas` | 13:30 comida_familia | **FAIL 82** | `apertura_in_medias_res=false`; apertura definicional y escena 6 repetitiva |
| `2026-11-05_inter-arboles-se-comunican` | 17:00 intermedio_1 | **FAIL 78** | `apertura_in_medias_res=false`; apertura genérica |
| `2026-11-05_inter-rayo-globular` | 17:45 intermedio_2 | **FAIL 81** | `apertura_in_medias_res=false`; apertura histórica descriptiva |
| `2026-11-06_kids-ballena-azul-corazon` | 07:00 kids | **FAIL 80** | `payoff_cierre_apertura=false`; sobreafirma «casi se detiene» |
| `2026-11-06_comida-aguacate-negro` | 13:30 comida_familia | **FAIL 79** | progresión y transiciones causales falsas; escenas 5–6 repetidas |
| `2026-11-06_inter-ranas-congeladas` | 17:00 intermedio_1 | **FAIL 83** | progresión y transiciones causales falsas; repetición de límites/condiciones |
| `2026-11-06_inter-arena-cantante` | 17:45 intermedio_2 | **PASS 94** | — |
| `2026-11-07_kids-huesos-bebe` | 07:00 kids | **FAIL 82** | progresión y transiciones causales falsas; escena 6 repite conteo/fusión |
| `2026-11-07_comida-hielo-caliente` | 13:30 comida_familia | **FAIL 81** | `apertura_in_medias_res=false`; apertura desde creencia general |
| `2026-11-07_inter-pulpo-suenos` | 17:00 intermedio_1 | **FAIL 80** | progresión, transiciones y payoff falsos; repetición escenas 5–6 |
| `2026-11-07_inter-nubes-pesan` | 17:45 intermedio_2 | **FAIL 78** | progresión, transiciones y payoff falsos; escena 7 reitera cifra/límite |

Los 12 JSON conservan `review_basis=lectura_en_frio_solo_narracion`, siete checks explícitos y `critical_flags`; se actualizó únicamente `reviewed_at` a `2026-11-13T15:42:39-06:00` y se releyeron los 12 archivos. Scores y statuses permanecen exactamente como se muestran.

### Validación estructural del lote

- 85 escenas en total; 7–8 escenas por proyecto.
- 11/12 cumplen 170–235 palabras; árboles tiene 169.
- Los 12 declaran 78 s de escenas + cortinilla de 6 s = 84 s; gancho de hasta 6 palabras.
- Voz, `source_ids` y `prompt_base` son consistentes con sus fuentes/catálogo. Hay mapa y dato/gráfico en 11/12; árboles carece de ambos.
- Ambiente está presente en las 85 escenas, pero **75/85 arrays SFX están vacíos**.
- Las seis propiedades narrativas obligatorias (`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`) faltan en las 85 escenas: **510 campos ausentes**. Resultado: **0/12 aptos estructuralmente**, aunque Venus y Arena tengan PASS narrativo.
- En los 12: `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename` ni `asset_type`. Los placeholders no se cuentan como medios.
- El DOI de Pulpo `10.1038/s41586-023-06203-4` corresponde a Pophale et al. (2023), cuyo artículo estudia `Octopus laqueus`; el storyboard afirma `Octopus insularis`. Es un desajuste de especie y fuente que el redactor debe corregir. Fuente primaria bibliográfica: https://pubmed.ncbi.nlm.nih.gov/37380770/ .

### Producción preexistente y no redispatch

El cruce con los horarios diarios `data/horario_2026-11-08.json` a `data/horario_2026-11-11.json` permite enlazar por `project_id` exacto **5/12** proyectos. Los IDs de Venus (`phVfyHp3CnY`) y Arena (`m4RqQRaz55k`) aparecen en un cierre global, pero no están vinculados a `project_id` ni a los slots de esos horarios diarios; no se atribuyen a esos dos proyectos. No se atribuye la producción a Grok.

| Proyecto del horario | ID de YouTube | Evidencia |
|---|---|---|
| Venus, 5-nov 07:00 | — | Sin vínculo exacto en los horarios diarios; ID global `phVfyHp3CnY` no atribuible |
| Palomitas, 5-nov 13:30 | `zTP5akrGA9M` | `data/horario_2026-11-08.json`, vínculo exacto por `project_id` |
| Arena cantante, 6-nov 17:45 | — | Sin vínculo exacto en los horarios diarios; ID global `m4RqQRaz55k` no atribuible |
| Ranas congeladas, 6-nov 17:00 | `UBFuKBU3cx0` | `data/horario_2026-11-09.json`, vínculo exacto por `project_id` |
| Aguacate negro, 6-nov 13:30 | `nSS_q2tj2P0` | `data/horario_2026-11-10.json`, vínculo exacto por `project_id` |
| Ballena azul, 6-nov 07:00 | `wbFrlM2e_YE` | `data/horario_2026-11-11.json`, vínculo exacto por `project_id` |
| Hielo caliente, 7-nov 13:30 | `HSgrnejAcaI` | vínculo exacto por `project_id` en `data/publicaciones.json` y `salidas/` de `main` |

Los cinco con vínculo exacto quedan como **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. Los otros siete sin evidencia de publicación enlazada por `project_id` son Venus, Arena, Rayo globular, Árboles, Huesos bebé, Pulpo sueños y Nubes pesan. Para Venus y Arena solo existen IDs globales no atribuibles. Los 12 estados `cola/estado/<project_id>.json` devuelven 404: **RECEPCION_GROK_NO_CONFIRMADA** en todos; una publicación no demuestra recepción de Grok.

### Caso Hielo caliente — discrepancias de salida

- `salidas/2026-11-07_comida-hielo-caliente/` existe en `main`, no en la rama feature. `qa.json` mide **89.83 s**, dentro de 75–90 s; es QA audiovisual, no `narrative_qa`.
- `publicacion.json` registra YouTube `HSgrnejAcaI`, `privacyStatus=private`, `publishedAt=2026-11-10T21:01:55Z` y `publishAt=2026-11-11T19:30:00Z`. El registro de publicaciones dice que el ID ya no aparecía en el canal el 12-nov 07:20 CDMX.
- `facebook.json` dice publicado; `tiktok.json` dice programado, mientras `data/publicaciones.json` dice TikTok publicado. Registrar la discrepancia; no reprogramar.
- La metadata/caption afirma «el agua caliente se congela antes que la fría», mientras la narración del proyecto presenta el efecto como no universal y con evidencia en disputa. Es una discrepancia de metadata que no se corrigió.
- `capsula.mp4` y `portada.jpg` referenciados no existen en el árbol consultado: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.

### Estilos y rotación

- Los 12 estilos están en el catálogo. `papel_rasgado_capas` se usa en Árboles y Ranas; `dibujo_cientifico_scratchboard` aparece en Ballena y en el caracol del 13-nov. No es una infracción automática de «estilo de la cápsula anterior», pero la rotación debe mirar todos los proyectos, no solo los dos días previos.
- `data/estilos_usados.json` termina el 31-oct y no representa el lote 5–7 ni el proyecto actual; no sirve para certificar rotación reciente.

## 5. Reconciliación de `data/` y registro editorial

En la rama feature, los archivos operativos no cubren las publicaciones recientes:

| Archivo | Corte observado |
|---|---|
| `data/temas_del_dia.json` | 28-oct |
| `data/vistas_historico.json` | 28-oct, 74 snapshots |
| `data/rotacion.json` | 31-oct |
| `data/estilos_usados.json` | 31-oct |
| `data/publicaciones.json` | 31-oct en feature; `main` añade Hielo el 11-nov |
| `data/cola.json` | una entrada fallida del 31-oct |
| `data/balances_6h.json` | 31-oct |
| `data/horarios.json` | ventanas generales; no slot del 13-nov |
| `data/horario_semana_2026-11-01_07.json` | horario de los 12 proyectos del lote |
| `data/horario_2026-11-13.json` | 404 |

Los cierres diarios del 8–11 nov están en `main`, no en la rama feature. Esta divergencia explica por qué la rama feature no refleja por sí sola los siete IDs publicados.

`registro_editorial.py` no lee cierres diarios ni `horario_semana`, no recorre `cola/bloqueados` ni `handoffs`, y limita la búsqueda a una profundidad. `procesar_cola.py` acepta `--fecha` histórica y rutas anidadas; el workflow no. El registro editorial puede perder publicaciones y bloqueos que no estén duplicados en `data/publicaciones.json` o `data/rotacion.json`.

## 6. IDs históricos de YouTube

`data/horario_semana_2026-11-01_07.json` conserva 22 IDs en `yt_id_historial` en diez slots. Se marcan como riesgo de duplicado pendiente de comprobación manual en Studio; el archivo no demuestra que sigan activos ni autoriza borrarlos.

| Proyecto | IDs históricos |
|---|---|
| 1-nov pulpo tres corazones | `3B1ckNUahS8`, `pxX0eGK3r98` |
| 1-nov llorar cebolla | `Fh4KkcZr3e8`, `0WAcVgODwd8` |
| 1-nov Baffin Bay | `krh0Ll3kVjM`, `MYWsfLm_Brw` |
| 1-nov tiburón de Groenlandia | `i2l4BkMvHp0`, `9XflXdWDM0A`, `bICGA3kIBcU` |
| 2-nov camarón mantis | `tmxMkxA6nOw`, `d-tYvAM8hGE` |
| 2-nov pan duro | `TbZRvpiDjdk`, `sHjf4QF9QiM` |
| 2-nov murciélagos viroma | `dFwKjIb8tFI`, `6ts8TvhgKa8` |
| 2-nov sequías y energía renovable | `SQ7_g-vz8Ow`, `pMkzlwB-7bo`, `-HfaDUCg4OE` |
| 3-nov Juno | `73cZz8Pi9TE`, `3IiUmsRb30Y` |
| 3-nov SmartPE plantas | `MXsNOywNzcg`, `aOcqxbBhQ0E` |

## 7. Ejecución y límites

- Se intentó obtener el repositorio local con `git clone`; la red del runtime no resolvió GitHub. No hubo runtime local.
- `scripts/validar_storyboard.py`, `scripts/procesar_cola.py` y `scripts/registro_editorial.py` no se ejecutaron. La validación fue estática y la lectura de código confirmó sus selectores.
- No hay acceso disponible al listado actualizado de Actions ni a sus logs. No se declara un error reciente ni ausencia de secretos.
- No se modificaron `data/*.json`, `main`, workflows, permisos, secretos, estados Grok, horarios ni decisiones editoriales. No se hizo merge.
- No se crearon frames, imágenes, voz, audio, video, renders ni publicaciones. No se consumieron créditos.

## 8. Cambios efectuados y verificación

1. Se añadió `narrative_qa` al storyboard del caracol del 13-nov: PASS 91, siete checks true, flags vacíos. El JSON se releyó; blob SHA `251a8941a0955c8ed28cfd673f1c5730daafd95b`.
2. En los doce storyboards del lote 5–7 se actualizó únicamente `narrative_qa.reviewed_at` a `2026-11-13T15:42:39-06:00`. Se releyeron los doce JSON; no se alteraron scores, statuses, checks, flags, narración ni claims.
3. Se creó este informe en `docs/briefs/2026-11-13_CONTROL_COLA.md`; debe releerse después de la creación.

**Conclusión:** el único borrador del 13-nov supera la lectura narrativa en frío, pero sigue siendo propuesta, con DOI pendiente y sin validación ejecutable; no se promovió para respetar la prohibición de disparar workflows. El lote 5–7 mantiene 2 PASS narrativos, 10 FAIL y 0/12 aptos estructuralmente. Cinco proyectos tienen evidencia de procesamiento/publicación preexistente y quedan protegidos contra redispatch.
