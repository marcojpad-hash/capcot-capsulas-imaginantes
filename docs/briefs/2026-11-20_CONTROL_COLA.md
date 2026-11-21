# CONTROL DE COLA — 2026-11-20

Repositorio: `marcojpad-hash/capcot-capsulas-imaginantes`  
Rama: `feature/capcot-video-discovery-continuity`  
Corte: 2026-11-20, 00:35 CDMX  
Tipo: auditoría de solo lectura + registro documental. No se generaron cápsulas ni medios.

## 1. Fuentes efectivamente leídas

- `docs/CONTRATO_OPERATIVO_UNIFICADO.md`
- `docs/PLAN_MAESTRO_AUTOMATICO.md`
- `docs/RECETA_CAPSULA.md`
- `docs/GUIA_MODELO_EXTERNO.md`
- `docs/FLUJO_EXTERNO.md`
- `docs/QA_NARRATIVO_EN_FRIO.md`
- `docs/GROK_STATUS_CONTRACT.md`
- `templates/storyboard_vertical.template.json`
- `scripts/estilos.json`
- `scripts/registro_editorial.py`
- `scripts/procesar_cola.py`
- `.github/workflows/capcot-grok-dispatch.yml`
- Inventarios actuales de `proyectos/`, `cola/entrada/`, `cola/bloqueados/`, `salidas/`, `handoffs/grok_inbox/` y `data/`.
- `docs/briefs/2026-11-19_CONTROL_COLA.md` y los dos storyboards del 19-nov.

No se modificó `data/*.json`, workflow, secretos, permisos, estados Grok ni `main`.

## 2. Inventario del día actual

No existe carpeta `proyectos/2026-11-20_*` en el inventario leído. Tampoco existe `docs/briefs/2026-11-20_RADAR_CAPCOT.md` al corte. No se atribuye un paquete a la fecha actual ni se inventa una entrega.

El último lote de borradores visible corresponde al 19-nov y contiene dos proyectos. Ambos conservan QA narrativo PASS en sus JSON, pero tienen bloqueos independientes de estructura/DOI/rotación. Permanecen en `proyectos/`; no hay autorización para promoción.

## 3. Revisión de los dos borradores más recientes

| project_id | SHA del storyboard releído | Fecha/slot | QA narrativo | Estructura / DOI | Decisión |
|---|---|---|---|---|---|
| `2026-11-19_dato-dia-luz-dos-manos-oro-poroso` | `a211420b3a8850a1866e9311b5930c4360b0703c` | 19-nov · 23:30 · dato_del_dia | PASS 91/100; siete checks true; flags vacías; lectura en frío registrada | 8 escenas; 188 palabras; 84 s totales; cortinilla 6 s; voz es-MX-JorgeNeural +7%/-2Hz; `approved_assets=[]`; `NOT_GENERATED`; DOI 10.1038/s41467-026-78158-9 permanece `PENDIENTE_RESOLVEDOR` | NO PROMOVER: DOI sin resolver/Crossref confirmado |
| `2026-11-19_dato-estrella-dentro-de-estrella` | `b55ae1d811cd70fd8953efb1f443851478b611dd` | 19-nov · 17:00 · intermedio_1 | PASS 90/100; siete checks true; flags vacías; lectura en frío registrada | 8 escenas; 197 palabras; 84 s totales; cortinilla 6 s; voz correcta; `approved_assets=[]`; `NOT_GENERATED`; DOI 10.1038/s41586-026-11221-z pendiente; mapa usa coordenadas celestes RA/Dec donde el validador espera geometría terrestre lat/lon o bounds; `art_deco_poster` repite el estilo de Juno registrado para el mismo día | NO PROMOVER: DOI, geometría y rotación sin resolver |

Las narraciones se releen concatenadas sin usar título, resumen, arco ni `narrative_contract`. Los resultados JSON existentes se conservaron; no se reescribió narración ni claims. El QA narrativo PASS no subsana los bloqueos estructurales ni DOI.

Para ambos IDs, `cola/estado/<project_id>.json` devuelve 404 y no existe `salidas/<project_id>/` en la rama auditada. Registrar exactamente: `RECEPCION_GROK_NO_CONFIRMADA`. No se creó ni editó estado Grok.

## 4. Cola: rutas reales contra selector de dispatch

Inventario actual de `cola/entrada/`:

| Ruta real | Contenido observado | Workflow push | workflow_dispatch | Estado |
|---|---|---|---|---|
| `cola/entrada/2026-11-07_dato-clavo-te-cocina/` | `storyboard.json`, `fuentes.md`, `ESTADO_EJECUCION.md` | No coincide con `cola/entrada/*.json` | No la encuentra: `find -maxdepth 1 -type f -name '*.json'` | NOT_DISPATCHABLE |
| `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/` | `storyboard.json`, `PARA_GROK.md`, `fuentes.md`, carpeta `frames/` | No coincide con `cola/entrada/*.json` | No la encuentra por profundidad | NOT_DISPATCHABLE; además hay procesamiento/publicación preexistente en main: no redispatch |
| `cola/entrada/2026-11-11_dato-ratas-topo-damaraland/` | Solo carpeta `frames/`; no se encontró `storyboard.json` en el nivel inspeccionado | No coincide | No hay JSON raíz | NOT_DISPATCHABLE |

El selector de `.github/workflows/capcot-grok-dispatch.yml`:
- Push: `paths: 'cola/entrada/*.json'`; el diff exige archivos `^cola/entrada/[^/]+\.json$`.
- Manual `all`: `find cola/entrada -maxdepth 1 -type f -name '*.json'`.
- Manual por ID: construye `cola/entrada/<ID>.json`.

Por tanto, **ninguna de las tres carpetas actuales es dispatchable por ese workflow**. No se infiere recepción por su presencia en GitHub.

Hay una diferencia entre componentes: `scripts/procesar_cola.py` sí enumera `cola/entrada/*.json` y `cola/entrada/*/storyboard.json`; el workflow de dispatch no. Esto es una incompatibilidad de rutas/profundidad entre el procesador y el dispatch. No se modificó el workflow ni se disparó.

## 5. Buzón y recepción Grok

`handoffs/grok_inbox/` contiene solo:
- `2026-11-09_dato-robot-ensambla-orbita.json` (status pendiente).
- `README.md`.

Ese marcador no acredita que Grok haya leído el paquete. Para los dos storyboards del 19-nov no existe marcador de handoff ni estado de Grok. El directorio `cola/estado/` no existe en la rama consultada; los dos accesos por project_id devolvieron 404.

## 6. Ejecución real de Actions observada

Se consultó la ejecución más reciente disponible del workflow `Trabajador de cola`:
- Run: [44688912590](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44688912590)
- Run #18; evento `schedule`; estado `completed`; conclusión `success`.
- Rama: `main`; commit: `05e842dc55577461e63d8f5de13fba96c46ff5f1`.
- Job: `trabajar`; ID `136129750966`; pasos terminados en success.
- Comando observado: `python3 scripts/trabajador_cola.py`.
- Salida literal: `[trabajador] sin trabajo en cola.`

Este resultado solo acredita que el trabajador programado consultó la cola de `main` y no encontró trabajo allí. No acredita que haya procesado la rama feature ni sus tres carpetas anidadas. La ejecución fue preexistente; no se disparó desde esta auditoría.

La consulta de la colección de Actions por endpoint de workflow específico no estuvo disponible desde el conector; no se inventan runs ni logs de `capcot-grok-dispatch.yml`.

## 7. Riesgo de producción preexistente

`2026-11-09_dato-robot-ensambla-orbita` tiene evidencia de salida/programación en `main` descrita en el control anterior y contiene un paquete de producción en la rama principal. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. No se crea otra entrada ni se reenvía.

No se declara que los medios referenciados estén disponibles fuera de sus ubicaciones comprobadas. No se borró, canceló ni reprogamó publicación alguna.

## 8. Estado final y acciones realizadas

- Inventario del día y backlog inmediato: EJECUTADO por lectura GitHub.
- QA de los dos storyboards recientes: conservado y contrastado con JSON actual; no se repitió una evaluación PASS ya válida.
- Dispatchabilidad: verificada contra rutas reales y workflow.
- Recepción Grok: `RECEPCION_GROK_NO_CONFIRMADA` para ambos proyectos del 19-nov.
- Producción preexistente: robot de órbita protegido contra redispatch.
- Validador local: NO EJECUTADO; se realizó inspección estática de contrato, JSON y código del selector. No se declara prueba de runtime.
- Cambios: solo este documento de control. No se modificaron narraciones, claims, `data/*.json`, workflow, main, estados Grok ni decisiones editoriales.
- Medios: NO_GENERADOS. Créditos: NO_CONSUMIDOS.

## 9. Siguiente trabajo concreto que no debe quedar perdido

1. Resolver DOI/Crossref del storyboard de oro; solo después reevaluar su compuerta estructural.
2. Resolver el mapa del storyboard de la estrella usando geometría válida respaldada por fuente, y resolver la repetición de estilo; no inventar coordenadas.
3. Reconciliar el dispatch con el formato real de cola en una tarea autorizada posterior. La corrección requeriría cambiar workflow y/o normalizar entradas; esta auditoría no lo hace.
4. Continuar el inventario interdiario y el backlog pendiente; no tratar el run `sin trabajo en cola` de main como procesamiento de feature.


## Addendum — 2026-11-20, verificación de rutas heredadas y producción preexistente

Este addendum amplía el control anterior; no sustituye el corte inicial ni modifica `data/*.json`, `main`, workflows, IDs de plataforma o estados Grok.

### 1. Clavo de cocina — QA y salida de cola

- Se hizo lectura en frío independiente solo de la narración concatenada. Resultado: `FAIL 82/100`; seis checks true y `limite_evidencia_explicito=false`; flag `CIFRAS_SIN_UNIDAD_Y_CONDICIONES_DE_ENSAYO_INSUFICIENTES`. Los porcentajes de concentración MIC/MBC no indican con precisión la base/unidad ni las condiciones asociadas a las medias.
- La carpeta heredada `cola/entrada/2026-11-07_dato-clavo-te-cocina/` se trasladó a `cola/bloqueados/2026-11-07_dato-clavo-te-cocina/`: storyboard con QA, fuentes y estado se copiaron; las tres copias se leyeron de vuelta; después se retiraron los tres archivos de la ruta de entrada. La ruta de entrada ya no contiene el paquete.
- Commits: `0d41041f7f4e14c39bf4969b561383b9cf7bbed1` (QA/storyboard), `86984b19400cc2d5193967821e2841525b071300` (fuentes), `fe92ee585c4e362927e09db7f338a71188c594d8` (estado), `8a4aa0298587ba56f840f557ab6f755aca335ff0`, `4fb106c8e8d6ec9c520ce45ac0c3c2c5a4d8c3f7` y `238e0b7469c07c454172b1222994c6a1cbd9b1c8` (retiro de origen tras verificación).
- La revisión de `data/horario_2026-11-08.json` y `data/horario_2026-11-09.json` reveló procesamiento/publicación previa: YouTube `EwZ3dHalUn0` y TikTok `7705655549571894529` aparecen publicados; Facebook aparece programado sin confirmación final. `data/publicaciones.json` no contiene una entrada correspondiente. No hay `salidas/<id>/` ni MP4 en los árboles GitHub consultados: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- `cola/estado/2026-11-07_dato-clavo-te-cocina.json` devuelve 404: `RECEPCION_GROK_NO_CONFIRMADA`. La publicación histórica no es acuse Grok. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no reprogramar ni redispatchar.
- `ESTADO_EJECUCION.md` en bloqueados fue reconciliado con esta evidencia (commit `4f3439cf43ed0919a86575172a642aa9d90cf4ca`).

### 2. Robot ensambla órbita — producción en main

- El storyboard de `feature` está en una carpeta anidada de cola, no en el JSON de primer nivel que selecciona Actions. Se verificó en `main` una producción posterior del mismo project_id: `capsula.mp4`, portada, nueve frames, subtítulos y QA audiovisual.
- `main/cola/entrada/2026-11-09_dato-robot-ensambla-orbita/qa.json`: 21/21 checks true; duración 87.57 s, dentro del contrato 75–90 s.
- `main/.../programacion.json`: YouTube ID `ZG4iQgmWrLI`, programado para 2026-11-21 19:00 CDMX; TikTok y Facebook figuran programados sin IDs de publicación.
- `cola/estado/2026-11-09_dato-robot-ensambla-orbita.json` devuelve 404: `RECEPCION_GROK_NO_CONFIRMADA`. La producción en main no sustituye el acuse.
- Se corrigió el estado documental de la copia `feature` para marcar `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, sin tocar `main` ni el paquete publicado (commit `a78333cb8c7ee6124dab968fb04eeaf5f14a5894`).

### 3. Ratas topo — producción publicada y versión distinta

- En `main` existe paquete de producción y `salidas/2026-11-11_dato-ratas-topo-damaraland/`. La programación registra YouTube `WcTviUWqbes`, TikTok `7707137000121404680` y Facebook `122109293493518983`; el estado de salida indica `publicado_yt_tt_fb`.
- Hay discrepancia temporal: `programacion.json` fija 12-nov 07:00 CDMX, mientras `publicacion.json` registra YouTube `publishedAt=2026-11-12T04:22:18Z` (11-nov 22:22 CDMX). No se infiere la hora efectiva sin reconciliar el historial de plataforma.
- QA audiovisual: 21/21; 87.90 s. El MP4 está referenciado pero no aparece en el árbol GitHub: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- El storyboard de `feature/cola/bloqueados/` tiene una narración distinta a la versión de producción en `main`. Se registró PASS 91/100 únicamente para el borrador bloqueado de `feature` (commit `ae75fcddb72cae0cb12630f02fe1d4318728d819`); ese QA no se transfiere a la versión de main.
- `cola/estado/2026-11-11_dato-ratas-topo-damaraland.json` devuelve 404: `RECEPCION_GROK_NO_CONFIRMADA`. La carpeta de entrada en `feature` contiene frames, no un storyboard seleccionable. Se añadió `ESTADO_EJECUCION.md` a bloqueados con la clasificación `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` (commit `a160f67a90df799c916065b3b4e9633847119c6e`).

### 4. Beta Pictoris — conflicto exacto de slot con hidrotermales

- `main/cola/entrada/2026-11-18_hielo-sucio-beta-pictoris/programacion.json` contiene video_id `2a36r5QOvi4`, `publishAt=2026-11-19T05:30:00Z` (18-nov 23:30 CDMX) y privacidad `private`. Ocupa el mismo fecha_objetivo + slot que el borrador hidrotermal del 18-nov.
- El QA audiovisual reporta 21/21 checks, pero mide 61.27 s; la comprobación del paquete solo exige 60–120 s y no satisface el contrato editorial 75–90 s.
- El MP4 se referencia en almacenamiento remoto `/workspace/guardia_1118/hielo.mp4`; no aparece en el árbol GitHub: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- `cola/estado/2026-11-18_hielo-sucio-beta-pictoris.json` devuelve 404. Clasificación: `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. No cancelar, reprogramar ni duplicar.

### 5. Lote 5–7 nov y backlog de 18 nov

- Se releyeron los doce storyboard JSON actuales: dos conservan narrative QA PASS (88 y 94), diez FAIL (72–83). Ninguno tiene copia en `cola/entrada/`; todos permanecen en `proyectos/`. Los dos PASS siguen fallando la estructura por campos narrativos ausentes; siete proyectos tienen sidecars de plataforma y no deben redispatcharse. No se repitió ningún PASS válido ni se modificó `data/*.json`.
- Kuroshio sigue PASS 90 y CI estructural exitoso, pero DOI resolver/Crossref pendiente; su estado ya dice no apto para promoción.
- Catorce campos hidrotermales sigue FAIL 68 y fuera de cola; su estado ya dice no apto para promoción y el slot 23:30 está ocupado por Beta Pictoris en main.

### 6. Dispatch y automatizaciones

- El workflow actual `capcot-grok-dispatch.yml` selecciona exclusivamente `cola/entrada/*.json` a profundidad 1. El procesador `procesar_cola.py` también acepta carpetas anidadas y `--fecha` histórico. Esa diferencia sigue siendo un riesgo de selección manual, no una razón para ampliar el dispatch a carpetas heredadas.
- El último run de dispatch encontrado es #147, 1-nov-2026, failure. Sus logs muestran la versión anterior del workflow, que exigía `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`; el error literal fue `Falta configurar GROK_WEBHOOK_URL.` El workflow actual hace webhook opcional y escribe un marker `handoffs/grok_inbox/` con estado pending, pero no hay run posterior que verifique ese nuevo camino. Un marker pending no es recepción Grok.
- Se reactivaron las automatizaciones existentes del investigador (08:00) y auditor (15:00), sin cambiar sus prompts ni horarios. La lectura de vuelta confirmó ambas habilitadas; el operador general sigue habilitado.

## Addendum — PR #14 cuásares y ledger (20-nov, revisión del operador)

- PR [#14](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/pull/14) sigue **OPEN / NOT MERGED**. Su rama `chatgpt/quasar-audit-fixes-20261115` apunta a `main`, no a `feature/capcot-video-discovery-continuity`; no se integró ni se alteró `main`.
- El PR modifica `proyectos/2026-11-15_dato-quasar-pareja-cosmic-dawn/storyboard.json` y `ajustes_entre_modelos/LEDGER_ASIGNACIONES.md`. El diff añade `asset_filename` a las ocho escenas. Esto contradice el contrato de preproducción vigente, que exige ausencia de `asset_filename`, `asset_type`, rutas de assets y nombres de exportación. El hecho de que el validador legado lo pida no autoriza a reintroducir esos campos.
- El cuerpo del PR confirma que **no ejecutó** `validar_storyboard.py --check-doi` en esa rama y conserva el `narrative_qa` histórico `FAIL/82`; por tanto no hay validador DOI ni QA narrativo nuevo que habilite promoción.
- PR #13 continúa abierto y no fusionado; PR #12 está cerrado sin merge. Issue #11 sigue abierta aunque conserva etiqueta `hecho`; esa etiqueta no convierte el storyboard en apto ni cierra la reauditoría pendiente.
- Clasificación: **NO_MERGE / NOT_DISPATCHABLE** bajo el contrato actual. Siguiente transición válida: revisar la propuesta en la rama autorizada `feature`, resolver la incompatibilidad del validador sin añadir campos de assets prohibidos, ejecutar validación estructural y DOI en esa rama y solicitar una auditoría narrativa independiente nueva sobre la narración corregida. No se ejecutó ni se solicitó ninguna de esas acciones en este corte.

### Lectura narrativa independiente de la versión propuesta en PR #14

- Se ocultaron título, resumen, arco, notas y narrative_contract y se leyó solo la narración concatenada del blob `4ce762eb64b99523d731a613cb71be80ccdda388` en `chatgpt/quasar-audit-fixes-20261115`.
- Resultado de esta lectura en frío de la **versión del PR**: `PASS 90/100`; review_basis=`lectura_en_frio_solo_narracion`; siete checks true: pregunta_central_reconstruible, apertura_in_medias_res, progresion_por_escena, transiciones_causales, giro_cientifico_explicado, limite_evidencia_explicito y payoff_cierre_apertura; critical_flags=[].
- La narración abre con la separación observada por Gemini North, progresa desde los cubos NIRSpec y el seguimiento de la compañera débil hasta la evidencia espectral [O III], y conserva como límite la lente gravitacional no descartada y la ausencia de prueba de fusión.
- Este PASS se aplica exclusivamente al blob del PR #14. **No se transfiere** al storyboard de `feature`, cuyo `narrative_qa` vigente sigue FAIL/82; tampoco habilita promoción porque el PR apunta a `main`, añade `asset_filename`, no tiene validación estructural + DOI y requiere revisión de integración en la rama autorizada.
## Addendum — vigencia de rotación y alcance del registro editorial

- Los datos de rotación no están actualizados a la fecha de este corte: `data/temas_del_dia.json` llega a 2026-10-28; `data/rotacion.json` llega a 2026-10-31; `data/estilos_usados.json` conserva 21 entradas y la última es 2026-10-28. `data/horarios.json` fue actualizado 2026-11-09. Se respetó la regla de solo lectura: ningún `data/*.json` fue modificado.
- `scripts/rotacion.py` usa `registro_editorial.registros()` y `temas_dia()` en lugar de depender exclusivamente de esos archivos históricos. `registro_editorial.py` combina rotación, publicaciones, cola y storyboards de `proyectos/`, `cola/entrada/`, `cola/` y `salidas/`; `temas_dia()` combina el JSON con los registros encontrados.
- Errata de alcance: el texto anterior quedó desactualizado tras la ampliación de `_storyboard_paths()`. El registro ya recorre `cola/bloqueados/<id>/storyboard.json` a un nivel; hasta este corte omitía los JSON planos `cola/bloqueados/*.json` y `handoffs/grok_inbox/`. El commit `e678b4ca7982e2f9c0b024d960694f4ef54d416d` añade los JSON planos de bloqueados y `6d40c5567fc8aa7c028567ceaaca906aa7d2bd87` agrega su prueba. Sigue sin recorrer `handoffs/grok_inbox/` ni profundidades mayores a un nivel; inspección directa de handoffs permanece obligatoria.
- La rama conserva la instrucción de contrastar `fecha_objetivo` + `slot_local` en `feature` y `main` y de no modificar `data/*.json`.

## Addendum — registro editorial y capacidad de bloqueados (20-nov, operador)

Se corrigió una omisión descubierta al comparar el inventario de cola/bloqueados/ con el registro editorial:

- scripts/registro_editorial.py ahora recorre cola/bloqueados/<project_id>/storyboard.json, conserva _source="bloqueado" y clasifica su origen por defecto como externa. Los bloqueados aportan tema, estructura, estilo y cama a la rotación para evitar duplicaciones.
- scripts/rotacion.py::exigir_cupo() excluye _source="bloqueado" del conteo de slots/cupo diario. Un borrador bloqueado no consume una plaza de publicación, pero sigue siendo evidencia para evitar_hoy() y la comprobación de duplicados.
- Se añadieron pruebas de regresión en tests/test_registro_editorial.py y tests/test_rotacion_capacity.py.
- Pruebas locales sobre las copias de los módulos: test_registro_editorial.py 4/4 PASS; comprobación aislada de capacidad 5 bloqueados → 0 plazas consumidas y tema/estilo conservados en rotación PASS. No equivale a la suite completa del repositorio.
- Commits: a23708bb34bb865b3ca55d93a66f61a340d957cd (registro), da191306d4f5fa4ad6222e6de413bae4509d178e (test registro), bd26a2850fc6cdba047b20349338b5b5b11af088 (capacidad), 4102ff6abba32d2721931f983bad1755f96fa686 (test capacidad).
- CI del commit 4102ff6abba32d2721931f983bad1755f96fa686: CodeQL, Analyze (python) y Analyze (actions) terminaron success (run #44733338122). Estas comprobaciones no ejecutan la suite de tests del repositorio; los ocho tests locales de los dos módulos sí pasaron sobre copias de código.
- No se modificaron data/*.json, main, workflows, cola, estados Grok ni medios. Los markers de handoffs/grok_inbox/ siguen revisándose directamente por el auditor; no se incorporaron como storyboards de rotación.

- El commit documental cf3de6efd69a314d44540fa69bc4ba05744c1646 terminó run #44733428873 en success (CodeQL neutral; Analyze Python y Actions success). El commit de conciliación de CI `9c08be6dec250e3598af7b6bab8c6ad4955ce5c8` terminó run #44733560788 en success (CodeQL, Analyze Python y Actions). Son checks de análisis, no la suite de tests del repositorio.

## Reconsulta operativa — 20-nov-2026, 06:27–06:42 CDMX

### Registro editorial: omisión corregida

- Se comprobó que había archivos `cola/bloqueados/<project_id>.json` planos además de carpetas `<project_id>/storyboard.json`. El registro anterior solo incluía los segundos.
- Se modificó únicamente `scripts/registro_editorial.py`: ahora `_storyboard_paths()` incluye JSON planos tanto de `cola/entrada/` como de `cola/bloqueados/`. No se tocaron `data/*.json`, rotación ni decisiones editoriales.
- Se añadió `test_includes_flat_blocked_storyboards_in_rotation` a `tests/test_registro_editorial.py`.
- Commits verificados: script `e678b4ca7982e2f9c0b024d960694f4ef54d416d`; prueba `6d40c5567fc8aa7c028567ceaaca906aa7d2bd87`.
- Verificación de lectura: blob del script `a1419d0e5214d770cb4a0cb7e89c792313e794ca`; blob del test `2351b2c082c5e08a3f7376cabbe6e5a2c57ec50a`.
- Prueba local aislada con el módulo y fixtures copiados: **5/5 PASS** (reconciliación con data histórica, origen externo, deduplicación, bloqueado anidado y JSON plano bloqueado). No es la suite completa ni un run de CI.

### Lote de doce proyectos, relectura estática (sin repetir QA narrativo)

Los doce IDs indicados por la auditoría siguen en `proyectos/`; sus QA existentes no se repitieron. Resultado leído de los storyboards actuales: **2 PASS** (Venus 88; arena cantante 94) y **10 FAIL** (palomitas 82, árboles 78, rayo globular 81, ballena 80, aguacate 79, ranas 83, huesos de bebé 82, hielo caliente 81, pulpo 72, nubes 78). Los doce archivos individuales `cola/estado/<project_id>.json` devolvieron 404: **RECEPCION_GROK_NO_CONFIRMADA** en los doce casos.

- Revisión estructural estática: 170–221 palabras, 7–8 escenas, 84 s con cortinilla, voz JorgeNeural +7%/−2Hz, assets vacíos y `NOT_GENERATED` en los doce. El proyecto de árboles carece de mapa con coordenadas y de capa dato/gráfico; los otros once sí contienen ambos. No se ejecutó el validador estructural real ni se hizo una nueva lectura narrativa.
- Siete proyectos conservan sidecars de plataforma y por eso se clasifican **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**: Venus, palomitas, ballena, aguacate, ranas, arena cantante e hielo caliente. Hay publicaciones verificadas en TikTok/Facebook y programaciones antiguas de Facebook/TikTok; los detalles y fechas siguen en los sidecars.
- Los siete sidecars apuntan a MP4 en rutas de workspace, no a archivos presentes en el árbol GitHub: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No se encontró `historial_youtube` en ninguna de las dos ramas. El sidecar de arena cantante menciona el ID YouTube `m4RqQRaz55k` como público y `ztIkYcXB91U` como programado; la disponibilidad actual no se pudo verificar con una conexión de YouTube, por lo que no se declara publicado ni cancelado.
- No hay proyectos/entradas de 20 o 21-nov en `feature` ni en `main` al corte. El investigador de las 08:00 sigue habilitado y es responsable del dato del día; no se duplicó su trabajo.

### PRs y CI

- PR [#3](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/pull/3): OPEN, DRAFT, NOT MERGEABLE; base `main`, head `feature/capcot-video-discovery-continuity`; 1,041 commits, 676 archivos, 72,326 adiciones y 1,693 eliminaciones. El diff incluye 13 `data/*.json`; esos datos permanecen fuera de este cambio y no se fusionó nada. Sus runs recientes de CodeQL/Analyze en verde no ejecutan la suite de pruebas CAPCOT. El run #44737931310 sobre el commit `8f5a520e66e78f82e3526e994ed6d02461c2956c` terminó success en Analyze (Python) y Analyze (Actions); no ejecutó pruebas unitarias.
- PR [#14](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/pull/14) sigue OPEN/NOT MERGED, apunta a `main` y conserva la incompatibilidad `asset_filename`/DOI ya documentada. PR #13 también sigue abierto y sin merge.
- Gitleaks run [#44735449493](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44735449493) falló al escanear 1,727 commits y encontró un `generic-api-key` en el commit histórico `a4ccf1974a8966d5801a991ac25609ef4d7cdca7`, archivo `docs/SKILL_DRAFT_capsula_diaria.md`, línea 17. Se inspeccionó el texto histórico con el valor omitido: es el placeholder literal `CAPCOT_LLM_API_KEY=...`, no una credencial; el archivo actual tampoco contiene una cadena larga en esa línea. Clasificación: **FALSO_POSITIVO_CONFIRMADO_POR_CONTENIDO**. No se rotó ni cambió ningún secreto.
- La diferencia entre los dos escaneos explica el resultado: el run anterior #44645952263, aunque verde, solo escaneó 1 commit; el nuevo recorrió la historia completa. No se modificó la configuración de Gitleaks ni se reescribió historia.

### Automatizaciones y recepción

- Investigador CAPCOT: habilitado; último run completado 19-nov 08:13 CDMX; próximo 20-nov 08:00.
- Auditor CAPCOT: habilitado; último run completado 19-nov 15:27 CDMX; próximo 20-nov 15:00.
- Operador único: este run permanece `in_progress` sin `completed_at`; no se registra como completado.
- No se disparó dispatch. El workflow sigue seleccionando JSON planos de `cola/entrada/`; no se encontró un run de dispatch posterior al #147 (1-nov). Un marker de handoff no acredita recepción Grok.


## Addendum de registro editorial recursivo — 20-nov-2026

- Se amplió `scripts/registro_editorial.py`: ahora busca `storyboard.json` recursivamente bajo proyectos, cola y salidas, sin limitarse a `*/storyboard.json`. Conserva además la lectura de JSON planos de entrada/bloqueados.
- Se añadió `handoffs_grok_inbox` como inventario separado en la salida CLI. Cada marker se expone con ruta, project_id, status, commit y package_path, pero siempre `receipt_confirmed=false`; el propio registro recuerda que solo `cola/estado/<project_id>.json` confirma recepción. Los markers no se incorporan a la rotación temática ni se confunden con storyboards.
- Pruebas añadidas en `tests/test_registro_editorial.py`: profundidad superior a un nivel y separación de marker sin recepción.
- Commits: script `d8f40e54ce9460d92b82b5a41ca7acad5e869f1d`; tests `83dc330ff05b99d386190195b42fb408947f1346`.
- Lectura de vuelta: blob script `bbbb188ef03dd834266be985ff95bda994c9f30c`; blob tests `c27a68f983cf084d30176ac81cac5aec875c6208`.
- Prueba local aislada de la lógica nueva: 2/2 checks PASS (storyboard anidado y marker separado con recepción false). **No** equivale a ejecutar la suite completa del repositorio. Los runs automáticos de análisis asociados a ambos commits seguían `queued` al corte; no se dispararon workflows manuales.


## Addendum — auditoría independiente del 20-nov, 10:03 CDMX

### 1. QA narrativo en frío registrado

Se releyó cada narración concatenada ocultando título, resumen, arco, notas y `narrative_contract`. El revisor fue distinto del investigador de las 08:00. Se registraron los siete checks obligatorios, `review_basis=lectura_en_frio_solo_narracion`, reviewer_role `auditor_capcot_independiente` y flags vacías.

| project_id | Resultado | Palabras | Escenas | Duración total |
|---|---:|---:|---:|---:|
| `2026-11-20_dato-marea-cerebral-en-sueno` | PASS 92/100 | 218 | 8 | 84 s |
| `2026-11-20_dato-dia-atlantico-humedad-sapropeles` | PASS 91/100 | 215 | 8 | 84 s |

Ambos JSON se releyeron después de la escritura y conservan siete checks true y `critical_flags=[]`.

Commits de QA y estado de fuentes:
- Marea cerebral: `a0ed3cd30bd001dea4a0c19056dd0e8b9642d226`; blob releído `813379e455ccab4304e3bf7a154b1f476b6f40d6`.
- Sapropeles: `745b548e4d281f9f0d240cca324c60de4e40e88e`; blob releído `5adae8aa07cf13e2fce954b2daa9feea4adf85eb`.

### 2. DOI y fidelidad de afirmaciones

- **Marea cerebral:** DOI `10.1038/s43587-026-01270-4` aparece en la página y PDF editorial de Nature Aging. La consulta directa Crossref/doi.org no se completó; `doi_verification_status` permanece `PENDIENTE_RESOLVEDOR`. El abstract resume el grupo mayor como 60–84; Methods, después de excluir participantes por movimiento, especifica que los 41 participantes mayores restantes tenían 60–83 años. El storyboard usa 60–83 y coincide con la muestra analítica final; queda retirada la discrepancia factual señalada en el primer corte.
- **Sapropeles:** la página editorial indexada de Nature Geoscience muestra el título, DOI `10.1038/s41561-026-02141-8`, fecha de publicación y versión de registro del 20-nov-2026. La consulta directa Crossref/doi.org no se completó; `verification_status` permanece `PENDIENTE` y `doi_verification_status` `PENDIENTE_RESOLVEDOR`. La página oficial de IODP para Site U1385 sí se consultó y respalda las coordenadas usadas.

Fuentes de verificación:
- https://api.crossref.org/works/10.1038/s43587-026-01270-4
- https://www.nature.com/articles/s43587-026-01270-4
- https://news.mit.edu/2026/waste-clearing-waves-in-brain-during-sleep-are-impaired-in-older-adults-1113
- https://api.crossref.org/works/10.1038/s41561-026-02141-8
- https://www.nature.com/articles/s41561-026-02141-8
- https://www.iodp.tamu.edu/scienceops/sitesumm/339/339_ss1385.html

### 3. Revisión estructural y staging

Se compararon ambos JSON con las reglas visibles de `scripts/validar_storyboard.py`: campos raíz, voz, estilo/prompt_base, 7–9 escenas, 170–235 palabras, arco, puentes por escena, source_ids, mapa con coordenadas, capa de dato, cortinilla de 6 s, 75–90 s, cierre hablado, assets vacíos, export NOT_GENERATED y estado de publicación pendiente. La reimplementación estática de esas reglas no encontró errores en los campos inspeccionados.

**Límite:** no se ejecutó el archivo oficial `scripts/validar_storyboard.py` ni se disparó GitHub Actions. La revisión estructural fue estática. Tampoco se completó una consulta directa Crossref/doi.org para ninguno de los dos DOI; se consultaron las páginas editoriales disponibles y el sitio oficial de IODP. No se declara validación Crossref.

### 4. Slots, cola y recepción

- 07:00: `main/data/publicaciones.json` registra flamenco, YouTube `msWV2AXr6Uk`, `publishAt=2026-11-20T13:00:00Z`.
- 13:30: `main/data/publicaciones.json` registra mxenes, YouTube `WTlFSZV9HYg`, `publishAt=2026-11-20T19:30:00Z`, con TikTok y Facebook también programados.
- 13:45: en `main`, `2026-11-20_react-proteinas-microbios` tiene storyboard en `proyectos/` y `cola/entrada/` y `programacion.json` con `publish_at=2026-11-20T19:45:00Z` (13:45 CDMX), estado `programado_para_private_hasta_hora`. Es un procesamiento/programación preexistente: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. El storyboard declara `export.filename=capsula.mp4`, pero `capsula.mp4` no existe en `cola/entrada/<id>/`, `proyectos/<id>/` ni `salidas/<id>/`: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No hay `cola/estado/<id>.json`; la programación no se eleva a recepción ni publicación confirmada.
- 17:00 y 23:30: los dos storyboards de feature ya ocupan esos slots; no se crea una segunda propuesta.

Para los dos project_id actuales, las rutas exactas de `cola/estado/`, `cola/entrada/`, `cola/bloqueados/` y `salidas/` devolvieron 404 tanto en feature como en main. Sus markers individuales en `handoffs/grok_inbox/` también devuelven 404. No se atribuye recepción Grok.

Resultado para ambos: `RECEPCION_GROK_NO_CONFIRMADA`; `NOT_DISPATCHABLE` porque siguen en `proyectos/` y el workflow solo selecciona JSON planos de primer nivel en `cola/entrada/*.json`. No se promovieron. El QA narrativo PASS no basta para promoción sin validador estructural oficial y DOI verificado. La edad 60–83 de Marea sí coincide con la muestra analítica final del paper.

### 5. Automatizaciones observadas

- Investigador CAPCOT: run `c691932a-cb50-8321-bf4e-977532ef080f`, COMPLETED el 20-nov 08:40 CDMX; entregó el radar y los dos storyboards ya auditados.
- Auditor CAPCOT: último run COMPLETED el 19-nov; siguiente 20-nov 15:00 CDMX. Esta auditoría es una pasada independiente del investigador; el auditor programado debe conservar los PASS si la narración no cambió y revisar solo los bloqueos restantes.
- Operador único: run actual `936c994c-16f4-8327-a308-93d6cedc66be` sigue `in_progress`, sin `completed_at`.

No se generaron medios, no se consumieron créditos, no se publicaron ni programaron piezas y no se modificaron `data/*.json`, `main`, workflow, secretos, permisos ni estados Grok.


## Corrección de inventario — lote 5–7 nov revalidado (20-nov, 10:03 CDMX)

Esta reconsulta corrige el conteo previo de siete sidecars. Se releyeron los 12 storyboards y el horario congelado; no se repitió la lectura narrativa.

### Identidad, horario y QA vigente

Los doce `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` coinciden con `data/horario_semana_2026-11-01_07.json`. Los doce registros del horario siguen con estado `pedir_chatgpt`, sin yt_id ni publishAt. QA leído directamente de los JSON actuales:

| project_id | QA vigente | Checks true | Palabras | Escenas | Total |
|---|---:|---:|---:|---:|---:|
| `2026-11-05_kids-dia-en-venus` | PASS 88 | 7/7 | 170 | 7 | 84 s |
| `2026-11-05_comida-palomitas` | FAIL 82 | 5/7 | 173 | 7 | 84 s |
| `2026-11-05_inter-arboles-se-comunican` | FAIL 78 | 6/7 | 170 | 8 | 84 s |
| `2026-11-05_inter-rayo-globular` | FAIL 81 | 6/7 | 197 | 7 | 84 s |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL 80 | 6/7 | 174 | 7 | 84 s |
| `2026-11-06_comida-aguacate-negro` | FAIL 79 | 5/7 | 170 | 7 | 84 s |
| `2026-11-06_inter-ranas-congeladas` | FAIL 83 | 5/7 | 177 | 7 | 84 s |
| `2026-11-06_inter-arena-cantante` | PASS 94 | 7/7 | 206 | 7 | 84 s |
| `2026-11-07_kids-huesos-bebe` | FAIL 82 | 5/7 | 172 | 7 | 84 s |
| `2026-11-07_comida-hielo-caliente` | FAIL 81 | 6/7 | 172 | 7 | 84 s |
| `2026-11-07_inter-pulpo-suenos` | FAIL 72 | 2/7 | 170 | 7 | 84 s |
| `2026-11-07_inter-nubes-pesan` | FAIL 78 | 4/7 | 221 | 7 | 84 s |

Los doce archivos `cola/estado/<project_id>.json` volvieron a devolver 404: `RECEPCION_GROK_NO_CONFIRMADA`. No se repitió el QA narrativo de ningún PASS existente. La validación estructural oficial no se ejecutó en esta pasada; ningún proyecto se promueve.

### Cola, bloqueados y salidas

- `proyectos/` conserva los doce storyboard actuales.
- `cola/entrada/` en feature solo tiene las carpetas anidadas de 09-nov robot orbital y 11-nov ratas topo; no hay entradas de estos doce IDs.
- `salidas/` en feature no tiene ninguno de estos doce IDs.
- `cola/bloqueados/` contiene borradores anteriores. Se verificaron seis variantes con nombres distintos —palomitas-explotan, árboles-mito-respiran, Venus-día-largo, corazón-ballena-azul, Mpemba-mito y sueños-pulpo—; sus `ESTADO_EJECUCION.md` dicen `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`, `NO_GENERADOS` y `PENDIENTE_DECISION_GROK`. No son los mismos project_id y no acreditan producción.
- También existen copias bloqueadas de aguacate, ranas y huesos de bebé. Sus estados dicen NO_GENERADOS y no aptos. Las copias planas de arena cantante y nubes pesan conservan `approved_assets=[]`, `NOT_GENERATED` y `PENDIENTE_DECISION_GROK`.

### Corrección de producción preexistente y conteo

El conteo previo de **siete proyectos con sidecars** no se sostiene al cruzar los IDs exactos. La consulta actual de `main/data/publicaciones.json`, `main/cola/entrada/` y `main/salidas/` encontró evidencia de procesamiento para **dos** project_id exactos:

1. **`2026-11-07_comida-hielo-caliente`**: en main existen `cola/entrada/<id>/` y `salidas/<id>/`. QA audiovisual 21/21, 89.83 s. YouTube `HSgrnejAcaI`, privado con `publishAt=2026-11-11T19:30:00Z`; TikTok `7706905447424347393` y Facebook `122109123507518983` figuran publicados. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. El QA audiovisual no reemplaza el FAIL/81 del storyboard de feature.
2. **`2026-11-07_inter-nubes-pesan`**: `main/data/publicaciones.json` registra YouTube `4Qpl17Ts_vI`, TikTok `7705597569203768597` y Facebook `122109293529518983` como publicados el 12-nov. No existe `salidas/<id>/` ni carpeta de cola en main; por tanto: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. El storyboard de feature conserva FAIL/78.

No se encontraron registros de publicación, salidas ni entradas en main para los otros diez IDs exactos. Los nombres de variantes bloqueadas no se deben convertir en evidencia de publicación del proyecto actual.

**Decisión:** los doce siguen fuera de una nueva promoción en esta auditoría. Los dos PASS narrativos no tienen ejecución del validador estructural oficial demostrada; los dos project_id con producción/publicación previa quedan además protegidos contra redispatch. El snapshot `data/horario_semana_2026-11-01_07.json` conserva `pedir_chatgpt` para todos, por lo que no refleja los dos procesamientos posteriores observados en main. No se modificó ese JSON ni ningún otro `data/*.json`.


## Run 8 — auditoría de backlog, cruces de main y correcciones de fuente (20-nov-2026, corte 12:14 CDMX)

Esta sección **corrige y amplía** el corte anterior. No se repitieron PASS narrativos cuando la narración permanecía igual. No se promovió ningún proyecto ni se disparó workflow.

### Cambios ejecutados y releídos en feature

1. **Marea cerebral** — commit `2795358cb3c22f8a92caa16772162e2673340a28`.
   - `SRC-001.verification_status` ahora es `VERIFICADO_FUENTE_PRIMARIA`; `doi_verification_status` permanece `PENDIENTE_RESOLVEDOR`.
   - **Corrección de la auditoría anterior:** no existe discrepancia factual entre la narración y la muestra analizada. El resumen del artículo informa 60–84 años; la sección Methods, después de exclusiones por movimiento, describe 41 participantes mayores de 60–83. La narración usa 60–83 y coincide con la muestra final analizada. El DOI sigue sin resolución independiente Crossref/doi.org; no se declara verificado.
2. **Sapropeles** — commit `f52e57dddf3354eeb00e715ab3779ffc3d52a326`.
   - `SRC-001.verification_status` cambió de `VERIFICADO_CROSSREF` a `PENDIENTE`, porque la nota de fuente registraba que Crossref y el resolvedor no completaron. La ficha editorial indexada muestra título, fecha y DOI, pero el HTML devolvió HTTP 500 y la resolución independiente continúa pendiente.
3. **Microplásticos del Pantanal** — commit `dcc9873dddf10d91d1187078a6f1650029cb777c`.
   - `SRC-001.verification_status` cambió de `VERIFICADO_RESOLVEDOR` a `VERIFICADO_FUENTE_PRIMARIA`. La página editorial de Nature se consultó; Crossref/doi.org no completaron. El DOI sigue pendiente. No se altera la narración.
4. **Pareja de cuásares** — commit `f69fd05dca6fbd13973b3aecfe2663b8f75b4f3a`.
   - El storyboard había cambiado después del QA FAIL anterior (commit de revisión de transiciones posterior a la lectura). Se hizo una nueva lectura en frío usando solo la narración concatenada.
   - Resultado actualizado: `FAIL 82`; checks: pregunta central true, apertura true, progresión true, transiciones causales false, giro true, límite true, payoff true. Flags: `TRANSICION_002_003_NO_CAUSAL` y `TRANSICION_003_004_NO_CAUSAL`. Estado: `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. No se reescribió narración ni claims.

### Inventario de proyectos y backlog 14–20 nov

| Proyecto | Slot local | QA narrativo vigente | Bloqueo/disposición |
|---|---:|---:|---|
| `2026-11-14_dato-microplasticos-pantanal` | 17:00 | PASS 88 | Fuente primaria identificada; DOI pendiente. Fecha pasada y sin validador oficial demostrado. NOT_DISPATCHABLE. |
| `2026-11-15_dato-dia-diapausa-lestes-sponsa` | 23:30 | PASS 90 | Consta validación local previa con `--check-doi` exit 0. Fecha pasada; no promover retroactivamente. |
| `2026-11-15_dato-quasar-pareja-cosmic-dawn` | 17:00 | FAIL 82 | Nueva lectura en frío tras cambio de narración; dos transiciones no causales. NOT_DISPATCHABLE. |
| `2026-11-16_dato-polen-desenreda-nanotubos` | 17:00 | PASS 91 | DOI pendiente y validación estructural oficial pendiente. Fecha pasada. NOT_DISPATCHABLE. |
| `2026-11-17_dato-suelo-dos-relojes` | 17:00 | PASS 89 | Colisión exacta con programación de Vikingos en main para 17-nov 17:00. NOT_DISPATCHABLE. |
| `2026-11-18_dato-catorce-campos-hidrotermales` | 23:30 | FAIL 68 | Colisión exacta con Beta Pictoris programado en main para 18-nov 23:30. NOT_DISPATCHABLE. |
| `2026-11-18_dato-kuroshio-puente-atmosferico` | 17:00 | PASS 90 | DOI/resolvedor pendiente. El CI verde del 19-nov fue solo smoke check, no ejecutó `validar_storyboard.py` ni `--check-doi`. NOT_DISPATCHABLE. |
| `2026-11-19_dato-dia-luz-dos-manos-oro-poroso` | 23:30 | PASS 91 | Sin conflicto exacto en main; no consta verificación DOI completa ni validador estructural oficial. NOT_DISPATCHABLE. |
| `2026-11-19_dato-estrella-dentro-de-estrella` | 17:00 | PASS 90 | La capa mapa usa coordenadas no válidas como latitud/longitud; DOI pendiente. NOT_DISPATCHABLE. |
| `2026-11-20_dato-marea-cerebral-en-sueno` | 17:00 | PASS 92 | La edad 60–83 sí coincide con la muestra analítica final. DOI pendiente; 17:00 pertenece a ventana de prueba. NOT_DISPATCHABLE. |
| `2026-11-20_dato-dia-atlantico-humedad-sapropeles` | 23:30 | PASS 91 | Fuente editorial indexada, HTML 500, DOI pendiente. 23:30 es slot fijo, pero falta validación DOI oficial. NOT_DISPATCHABLE. |

Se ejecutó una **comprobación estática equivalente** de campos/escenas/voz/arco/duración/mapa/dato/assets para los storyboards 14–20: 14, 15 Lestes, 15 Quasar, 16, 17, 18 hidrotermales, 18 Kuroshio, 19 oro, 19 estrella, 20 Marea y 20 Sapropeles. La única anomalía estructural detectada en esa comprobación fue el mapa de estrella dentro de estrella. Esta comprobación no ejecutó el script oficial; no se presenta como sustituto de `scripts/validar_storyboard.py`. El smoke check de Kuroshio tampoco equivale al validador estructural ni verifica DOI.

Los 12 IDs del lote 5–7 nov conservan los mismos SHA/contenidos desde la pasada independiente del 18-nov: dos PASS (88 y 94), diez FAIL. Sus `narrative_qa.reviewed_at` sigue en 18-nov; no se repitió lectura narrativa. Los dos IDs exactos con procesamiento en main continúan siendo hielo caliente y nubes pesan; no se amplía el conteo a variantes bloqueadas.

### Cruces de main y producción preexistente

- **17-nov, 17:00 — Vikingos cuernos:** `main/cola/entrada/2026-11-16_vikingos-cuernos/programacion.json` registra video_id `ThbHry-YC-w`, publishAt `2026-11-17T23:00:00Z` (17:00 CDMX), 81.2 s y QA audiovisual 21/21. Coincide exactamente con `2026-11-17_dato-suelo-dos-relojes`. Clasificación del storyboard feature: `CONFLICTO_DE_SLOT_ENTRE_RAMAS`; Vikingos: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. El MP4 no aparece en el árbol de main: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- **18-nov, 23:30 — Beta Pictoris:** la programación de cola en main registra video_id `2a36r5QOvi4`, publishAt `2026-11-19T05:30:00Z`, 61.27 s y QA 21/21. Coincide exactamente con hidrotermales. La duración medida queda fuera del contrato 75–90 s. Además, el `programacion.json` de proyecto dice 13:30, mientras el de cola dice 23:30: inconsistencia interna en main. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` y `CONFLICTO_DE_SLOT_ENTRE_RAMAS` para hidrotermales.
- **20-nov, 13:45 — React proteínas/microbios:** main contiene programación a 13:45, sin video_id ni MP4 en el árbol; el storyboard tiene 106 palabras, 7 escenas, `export.filename`, no tiene narrative_qa y `fuentes.md` enlaza Phys.org como nota secundaria. El MP4 se declara pendiente de montaje. No es dispatchable; `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. Main ya tiene otro registro a 13:30 dentro de la misma ventana activa 13:00–14:30: posible sobrecarga de ventana, no conflicto de hora exacta. No se canceló ni alteró.
- **16-nov — HERA/Didymos:** main programa 23:30 con video_id y duración 85.93 s; los assets sí aparecen en el árbol. No colisiona con polen 17:00.
- **21-nov, 19:00 — Robot orbital:** main programa video_id `ZG4iQgmWrLI`, publishAt `2026-11-22T01:00:00Z`, 87.57 s, QA audiovisual 21/21 y assets visibles en el árbol. Es procesamiento preexistente: no redispatchar. En feature existe un marker `pending` en `handoffs/grok_inbox`, pero `cola/estado/2026-11-09_dato-robot-ensambla-orbita.json` devuelve 404: la recepción Grok no está confirmada.

### Cola, handoff y datos

- En feature, `cola/entrada/` solo contiene dos carpetas anidadas: robot orbital (con storyboard y paquete) y una carpeta de ocho PNG atribuida por nombre a ratas topo. Esta última no tiene storyboard ni carpeta de proyecto; es `ORPHAN_ASSETS_NO_STORYBOARD`, no una entrada dispatchable. No se movió porque no existe storyboard que preservar y no se pudo vincular con certeza a una publicación.
- El ID `knAElNo4raI` aparece en `data/endscreens_rotacion.json` con 285 vistas y mapeo a `wxnhEdlJYwU`; el archivo no vincula ese ID con ratas topo. Se retira la atribución anterior no sustentada: no hay evidencia suficiente para asignarlo a ese tema.
- No hay archivos `cola/estado/*.json` en el árbol feature; por tanto, para los proyectos revisados aplica `RECEPCION_GROK_NO_CONFIRMADA`. `salidas/` está vacío en feature y no existe `historial_youtube`.
- `capcot-grok-dispatch.yml` selecciona JSON planos de primer nivel (`cola/entrada/*.json` / `find -maxdepth 1`); las carpetas anidadas observadas no son dispatchables. El marker de inbox no equivale a recepción. No se disparó workflow ni se envió payload.
- Divergencia de horario: `feature/data/horarios.json` conserva versión del 09-nov; `main/data/horarios.json` está actualizado al 16-nov. En main la tarde 16:30–18:00 es ventana de prueba, el mediodía 13:00–14:30 es activo y 23:30 es slot fijo. No se modificó ningún `data/*.json`.
- `data/rotacion.json`, `temas_del_dia.json`, `estilos_usados.json`, `vistas_historico.json` y `publicaciones.json` de feature conservan cortes de octubre; la rotación necesita contrastarse con main y el registro editorial. `registro_editorial.py` sí recorre storyboards recursivamente y separa los markers de handoff. No se ejecutó su suite en este run.
- Actions: el smoke check de Kuroshio del 19-nov terminó verde, pero no ejecutó el validador real. En main, Semgrep terminó FAIL con 32 findings y no dejó artefacto SARIF descargable; Gitleaks terminó SUCCESS. No se modificó main.

**Resultado:** ningún storyboard 14–20 es promovido. Los bloqueos restantes son verificables: dos colisiones exactas de slot, varios DOI/resolvedores pendientes, un QA FAIL actualizado, una capa de mapa inválida, ausencia de ejecución del validador oficial y recepción Grok no confirmada. No se generaron medios, no se consumieron créditos y no se alteraron publicaciones, programación ni estados Grok.


### Comprobación adicional de slots y capacidad — run operador 8

- `feature/data/horarios.json` (actualizado 09-nov) habilita 06:30–07:30 y 16:30–18:00, más 23:30 fijo. `main/data/horarios.json` (16-nov) habilita 06:30–07:30 y 13:00–14:30, más 23:30 fijo. `scripts/rotacion.py` aún conserva cinco ventanas (07:00, 13:30, 17:00, 19:00, 23:30). La discrepancia entre políticas por rama y ventanas de código permanece; no se modificaron `data/*.json` ni el código de rotación. 17:00 es válido dentro de la ventana activa de feature; 19:00 no se reutiliza.
- La reserva main de REACT a las 13:45 está dentro de la ventana mediodía de main, pero no coincide exactamente con los slots 17:00 o 23:30 de feature. Considerando 07:00, 13:30, 13:45, 17:00 y 23:30, el inventario visible ya alcanza cinco piezas/reservas para la fecha; no se crea un sexto paquete.

## RUN 9 — 20-nov-2026, 16:11 CDMX

### Proyectos recientes y QA

- El inventario de la rama no cambió en los proyectos anteriores a este run: la comparación desde `6b764c5` solo muestra la nueva pieza de Fentale y las actualizaciones de briefs/QA. Por ello no se repitieron los PASS vigentes de Marea cerebral (92), Sapropeles (91), Luz de dos manos (91) y Estrella dentro de estrella (90).
- `2026-11-21_pulsar-gamma-reticulo`, slot 17:00: conserva `FAIL 83`, flag `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`. No se reescribió la narración.
- `2026-11-21_fentale-metano-sin-erupcion`, slot fijo 23:30: creado en `proyectos/` y QA independiente posterior, lectura en frío solo de narración: `PASS 90/100`, siete checks true, `critical_flags=[]`. 8 escenas, 170 palabras, 78 s de escenas + 6 s de cortinilla = 84 s. Estilo `pulp_comic_1940s`; mapa GVP 8.985°N, 39.906°E; datos 38.2 ± 3.9 kt CH₄ y pico 157 ± 41 t/h.
- La fuente primaria Nature Geoscience (DOI `10.1038/s41561-026-02137-4`) está identificada y la página editorial está indexada. Crossref/doi.org no completaron; `doi_verification_status=PENDIENTE_RESOLVEDOR`. El validador estructural oficial no se ejecutó para esta pieza. No promover.
- Fentale permanece en `proyectos/`, sin `cola/estado`, sin entrada en cola, sin handoff, sin medios y sin programación. `approved_assets=[]`, `render_status=NOT_GENERATED`, publicación `PENDIENTE_DECISION_GROK`.
- El slot 21-nov 23:30 estaba libre al crear: en `main` se observaron publicaciones a 13:30 y 19:00, pero no `publishAt=2026-11-22T05:30:00Z`. No se detectó conflicto exacto de fecha+slot.

### Recepción, cola y producción preexistente

- Los 12 IDs del lote 5–7 nov siguen sin cambios desde la auditoría previa: 2 PASS y 10 FAIL; no se repitió QA de PASS. Ninguno tiene `cola/estado/<id>.json`; registrar `RECEPCION_GROK_NO_CONFIRMADA`. Los duplicados heredados permanecen en bloqueados; no promover por fechas vencidas ni alterar `data/*.json`.
- `2026-11-09_dato-robot-ensambla-orbita`: entrada anidada, no seleccionada por el workflow actual; marcador en `handoffs/grok_inbox` en estado pendiente, pero sin `cola/estado` (no confirma recepción). Main conserva video_id `ZG4iQgmWrLI` y programación 21-nov 19:00; el MP4 y la portada sí están en el árbol. Clasificación: `NOT_DISPATCHABLE` y `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- `2026-11-11_dato-ratas-topo-damaraland`: entrada anidada, no seleccionada por el workflow; estado ausente y sin handoff. Main conserva publicación con video_id `WcTviUWqbes`, TikTok `7707137000121404680` y Facebook `122109293493518983` (12-nov 07:00). La referencia a `capsula.mp4` no tiene archivo correspondiente en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. Clasificación: `NOT_DISPATCHABLE` y `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- REACT, 20-nov 13:45: la programación privada preexistente permanece; `capsula.mp4` no aparece en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No redispatchar ni cancelar.
- No existe archivo `historial_youtube` en el árbol revisado; el cruce se hizo con `data/publicaciones.json` y los registros de programación disponibles.

### Workflow, CI y PR

- `.github/workflows/capcot-grok-dispatch.yml` selecciona solo `cola/entrada/*.json` en raíz y el modo manual usa profundidad máxima 1. No procesa las entradas anidadas actuales. Los storyboards que siguen únicamente en `proyectos/` son `NOT_DISPATCHABLE`.
- No se encontraron ejecuciones de `capcot-grok-dispatch` entre las últimas 100 Actions consultadas. No se enviaron payloads ni se dispararon workflows; por tanto no se afirma presencia ni ausencia de los secretos `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`.
- `validar-kuroshio.yml` valida el proyecto Kuroshio, no Fentale, y ejecuta el validador sin `--check-doi`. CodeQL pasó para el commit de creación de Fentale; eso no es validación estructural ni DOI.
- PR #3 sigue OPEN, draft y no mergeable; PR #6 OPEN/no mergeable con riesgo por `secrets: inherit` y permisos de escritura; PR #14 OPEN/no mergeable y conserva referencias `asset_filename` incompatibles. Issue #11 sigue OPEN con etiqueta `hecho`. No se fusionó ni cerró nada.

### Resultado de promoción

Ninguna pieza se promovió. Fentale tiene QA narrativo PASS, pero mantiene dos compuertas independientes pendientes: resolución DOI/Crossref y ejecución del validador estructural oficial. Los demás bloqueos de recepción, producción previa, fechas vencidas y selección por profundidad permanecen sin eludir.

**Commits run 9:** storyboard Fentale `096612f3809fb16b47b66489fae497f669c9c688`; QA Fentale `18492e0d9f0db615f5af81cb420d48efaf07606a`; radar sincronizado `a6aeef2fe4eaee7cb44b398909cc527aa16091ca`; control de cola `9e4cd84783d2e8784ba6c0a746012bea9b16a11e`.


---

# Auditoría ampliada — 2026-11-20

**Corte de rama:** `feature/capcot-video-discovery-continuity`, PR #3 abierto/draft, HEAD del PR `837892244f6b04976a2c23e968d0b7490c1eb8fe` (no integrado en `main`). No se escribió en `main`.

## 1. Inventario de briefs y proyectos

Leídos de nuevo: Plan Maestro, Receta, Guía del modelo externo, Flujo Externo, contrato de estado Grok, contrato operativo, QA narrativo en frío, plantilla vertical vigente, catálogo de estilos, datos operativos, `scripts/registro_editorial.py`, `scripts/procesar_cola.py`, validador, workflow de dispatch y briefs del 20-nov.

Proyectos con fecha objetivo **2026-11-20** encontrados en `proyectos/`:

| project_id | slot_local | narrative_qa del JSON | Estructura estática | Bloqueo |
|---|---:|---:|---|---|
| `2026-11-20_dato-marea-cerebral-en-sueno` | 17:00 | PASS 92 | 8 escenas, 218 palabras, 78 s de escenas + 6 s de cortinilla = 84 s; voz, prompt_base, source_ids, mapa/dato, ambiente y SFX correctos; sin assets | DOI `10.1038/s43587-026-01270-4`: `PENDIENTE_RESOLVEDOR` |
| `2026-11-20_dato-dia-atlantico-humedad-sapropeles` | 23:30 | PASS 91 | 8 escenas, 215 palabras, 84 s; voz, prompt_base, source_ids, mapa/dato, ambiente y SFX correctos; sin assets | Fuente `SRC-001` y DOI `10.1038/s41561-026-02141-8` siguen pendientes de verificación/resolución |

Los dos QA ya incluyen `reviewer_role=auditor_capcot_independiente`, siete checks verdaderos y `critical_flags=[]`; se conservaron sin reescribir la narración ni repetir un PASS válido. En ambos: `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type`, `export.filename` ni rutas de medios. No hay entrada de cola para ninguno. Sus dos lecturas de `cola/estado/<project_id>.json` devolvieron 404: **RECEPCION_GROK_NO_CONFIRMADA**. No se promueven mientras el requisito DOI siga abierto.

Consulta de solo lectura a `main`: el 20-nov hay publicación a las 07:00 y 13:30, además de `2026-11-20_react-proteinas-microbios` programado a las 13:45; ninguno comparte los slots exactos 17:00 o 23:30. No se detectó conflicto de slot para estos dos borradores.

### Backlog reciente

| project_id | narrative_qa | Bloqueo/estado |
|---|---:|---|
| `2026-11-17_dato-suelo-dos-relojes` | PASS 89 | QA válido; no requiere repetición |
| `2026-11-18_dato-catorce-campos-hidrotermales` | FAIL 68 | Estado ya corregido a `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; permanece fuera de cola |
| `2026-11-18_dato-kuroshio-puente-atmosferico` | PASS 90 | CI estructural PASS; DOI pendiente; estado actualizado con run #5 |
| `2026-11-19_dato-dia-luz-dos-manos-oro-poroso` | PASS 91 | JSON dice `VERIFICADO_URL`; no hay ejecución `--check-doi` que confirme Crossref/resolvedor |
| `2026-11-19_dato-estrella-dentro-de-estrella` | PASS 90 | FAIL estructural: coordenadas celestes usadas como latitud/longitud geográfica; fuente/DOI pendiente |

No se promovió ninguno del backlog. Los PASS válidos se conservaron.

## 2. Lote obligatorio 5–7 nov: identidad, QA y estructura

Los doce `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` coinciden con `data/horario_semana_2026-11-01_07.json`. No se encontró desajuste de tema-slot en el lote.

| project_id | slot | narrative_qa del JSON | Observación determinante |
|---|---:|---:|---|
| `2026-11-05_kids-dia-en-venus` | 07:00 | PASS 88 | Producción/publicación preexistente; no redispatch |
| `2026-11-05_comida-palomitas` | 13:30 | FAIL 82 | Gancho definicional y progresión repetitiva |
| `2026-11-05_inter-arboles-se-comunican` | 17:00 | FAIL 78 | 169 palabras (mínimo 170) y ausencia de capa mapa/dato; el tema canónico sí corresponde a redes micorrícicas comunes y Karst et al. 2023 |
| `2026-11-05_inter-rayo-globular` | 23:30 | FAIL 81 | Apertura histórica/descriptiva, no in medias res |
| `2026-11-06_kids-ballena-azul-corazon` | 07:00 | FAIL 80 | El cierre exagera: el mínimo medido es 2 latidos/min, no que el corazón casi se detenga |
| `2026-11-06_comida-aguacate-negro` | 13:30 | FAIL 79 | Repetición de información entre escenas 5 y 6 |
| `2026-11-06_inter-ranas-congeladas` | 17:00 | FAIL 83 | Repetición de escenas y pareja DOI/URL que requiere resolver antes de aceptar la fuente |
| `2026-11-06_inter-arena-cantante` | 17:45 | PASS 94 | Producción/publicación preexistente y riesgo de ID de YouTube duplicado |
| `2026-11-07_kids-huesos-bebe` | 07:00 | FAIL 82 | El rango 270–300 huesos al nacer no queda respaldado por la fuente citada |
| `2026-11-07_comida-hielo-caliente` | 13:30 | FAIL 81 | Gancho definicional; además existe producción previa del mismo ID |
| `2026-11-07_inter-pulpo-suenos` | 17:00 | FAIL 72 | La narración atribuye el resultado a `Octopus insularis`, mientras la fuente enlazada corresponde a otra especie |
| `2026-11-07_inter-nubes-pesan` | 17:45 | FAIL 78 | Repite estimación/límite y no paga la apertura; publicación previa en otro slot |

Comprobaciones comunes del lote: 7–8 escenas; 78 s de escenas + cortinilla de 6 s = 84 s; títulos cortos de 3–5 palabras; voz `edge-tts / es-MX-JorgeNeural` con parámetros de catálogo; `source_ids` válidos; `prompt_base` coincide con el catálogo; ambiente y SFX presentes en todas las escenas; `approved_assets=[]`; `export.render_status=NOT_GENERATED`; sin `asset_filename`, `asset_type`, `export.filename` ni rutas de medios. Los DOI declarados están presentes donde corresponde. La excepción estructural clara es el storyboard canónico de árboles: 169 palabras y sin capa mapa/dato. Los FAIL narrativos no se promovieron.

Identidad y variantes:
- `2026-11-05_inter-arboles-se-comunican` es el storyboard canónico; no se marcó desajuste temático. `2026-11-05_inter-arboles-mito-respiran` en bloqueados es otro artefacto.
- El slot 2026-11-07 17:45 pertenece exactamente a `2026-11-07_inter-nubes-pesan`. `2026-11-07_extra-nubes-pesan` es material de origen, no un segundo proyecto.
- Las copias planas heredadas de rayo, aguacate, arena, ranas, nubes y huesos en `cola/bloqueados/` son snapshots antiguos; no son entradas activas de `cola/entrada/`.

## 3. Producción preexistente y no redispatch

Se contrastaron sidecars, `salidas/`, publicaciones y ambas ramas. Ocho de los doce IDs tienen evidencia de programación/publicación preexistente:

| Proyecto | Evidencia registrada | Estado/horario y discrepancia |
|---|---|---|
| Venus | YT `phVfyHp3CnY`; TT/FB publicados | 7-nov 17:00/17:58, fuera del slot objetivo 5-nov 07:00 |
| Palomitas | YT `zTP5akrGA9M`; TT/FB publicados | 8-nov 07:00, fuera del slot objetivo |
| Ballena | YT `wbFrlM2e_YE`; TT publicado, FB programado | 11-nov 07:00 |
| Aguacate | YT `nSS_q2tj2P0`; TT publicado, FB programado | 10-nov 07:00 |
| Ranas | YT `UBFuKBU3cx0`; TT publicado, FB programado | 9-nov 07:00 |
| Arena | YT `m4RqQRaz55k` público; TT/FB publicados | El sidecar aún describe `ztIkYcXB91U` como programado a las 19:00: riesgo de duplicado; no cancelar ni borrar |
| Hielo caliente | YT `HSgrnejAcaI`; TT/FB publicados | YT aparece privado con publishAt 11-nov 13:30 y el registro diario dice que dejó de aparecer el 12-nov |
| Nubes | YT `4Qpl17Ts_vI`; TT/FB publicados | Publicado 12-nov 07:00, no en el slot 7-nov 17:45; coincide en hora con ratas topo |

Los sidecars de estos siete proyectos con `tiktok.json`/`facebook.json` apuntan a rutas locales `/workspace/...`; esos medios no están en el árbol GitHub. Para ellos: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. La búsqueda no encontró un archivo `historial_youtube`; `data/vistas_historico.json` está vacío. El ID `ztIkYcXB91U` solo aparece como programado en la nota del sidecar; se conserva como riesgo, no como estado actual confirmado.

Además:
- `main` contiene `salidas/2026-11-07_arboles-comunicacion-bosque/`, otro project_id con el mismo tema general de redes arbóreas. Su QA audiovisual marca 21/21 y 87.50 s, pero su YouTube `EX0W3q-yKRw` figura privado con publishAt 13-nov 13:30; TT/FB aparecen publicados. Es duplicación temática con el canónico del 5-nov, no desajuste de tema.
- `main` contiene `salidas/2026-11-07_comida-hielo-caliente/`: QA audiovisual 21/21, 89.83 s; YouTube `HSgrnejAcaI` privado con publishAt 11-nov 13:30; TT/FB publicados. No aparece `capsula.mp4` en el árbol.
- `main` contiene `salidas/2026-11-11_dato-ratas-topo-damaraland/`: QA audiovisual 21/21, 87.90 s; YouTube `WcTviUWqbes` privado con publishAt 12-nov 07:00; `programacion.json` dice `publicado_yt_tt_fb`, mientras `publicacion.json` conserva `privacyStatus=private`. El MP4 no aparece en el árbol y la miniatura referencia una ruta local: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- La cola de main contiene `2026-11-07_comida-hielo-caliente` y `2026-11-07_arboles-comunicacion-bosque`; no se crea una segunda entrada desde feature.

El QA audiovisual de `salidas/` no se usó como `narrative_qa`. Los cuatro QA audiovisuales revisados (robot 9-nov, árboles 7-nov, hielo 7-nov y ratas 11-nov) miden 87.57, 87.50, 89.83 y 87.90 s, respectivamente, todos dentro de 75–90 s.

## 4. Cola, handoff y dispatchabilidad

En feature, `cola/entrada/` contiene solo dos carpetas históricas:
- `2026-11-09_dato-robot-ensambla-orbita/`
- `2026-11-11_dato-ratas-topo-damaraland/`

No hay JSON plano de entrada ni paquete de 2026-11-20. Los dos storyboards del día siguen en `proyectos/`, por tanto **NOT_DISPATCHABLE**. Las dos carpetas históricas también son **NOT_DISPATCHABLE** para el workflow actual: `.github/workflows/capcot-grok-dispatch.yml` escucha `cola/entrada/*.json` y el dispatch manual busca solo profundidad 1 (`-maxdepth 1)); no descubre `cola/entrada/<project_id>/storyboard.json`.

Las 16 lecturas de `cola/estado/<project_id>.json` para los dos proyectos del día y los doce del lote 5–7 devolvieron 404: registrar literalmente **RECEPCION_GROK_NO_CONFIRMADA**. El marcador de `handoffs/grok_inbox/` para robot 9-nov tiene estado pending y solo prueba que se escribió un marker; no prueba lectura por Grok. `handoffs/grok_done/` contiene únicamente `.gitkeep`.

Última ejecución del workflow de dispatch encontrada: run `41306776689`, 2026-11-01T12:29:58Z, falló con el texto literal `::error::Falta GROK_WEBHOOK_URL en Actions Secrets.`. No hay ejecuciones posteriores de ese workflow. El workflow vigente tiene webhook opcional y marker; el log no permite afirmar el estado de `GROK_WEBHOOK_TOKEN`, y no se expone ningún valor de secreto.

`scripts/procesar_cola.py` usa hoy como fecha por defecto, pero acepta `--fecha` explícita: no está blindado para procesar únicamente la fecha real actual. Puede seleccionar carpetas históricas si se invoca con fecha antigua.

El código vigente de `scripts/registro_editorial.py` usa `rglob` para storyboards en proyectos/cola/salidas y tiene un recorrido recursivo separado de `handoffs/grok_inbox/`. Esto contradice la nota anterior que decía que no recorría handoffs ni profundidades mayores. Aun así no es inventario exhaustivo: no incorpora los sidecars TikTok/Facebook ni confirma estados externos.

## 5. Backlog anterior sin narrative_qa

Se encontraron 32 borradores antiguos sin `narrative_qa` antes de esta actualización. Treinta y uno tienen ya una carpeta `salidas/<id>/` y quedan clasificados **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**; no se repitió su QA ni se dedujeron medios por placeholders:

`2026-10-24_abejas-bullying`, `2026-10-24_ideonella-pet`, `2026-10-24_osedax-comehuesos`, `2026-10-24_serpientes-que-ruedan`, `2026-10-25_ave-jurasica-sin-vuelo`, `2026-10-25_corales-contacto`, `2026-10-25_reina-olor`, `2026-10-25_sueno-electricidad-qom`, `2026-10-26_baffin-bay-ice-shelf`, `2026-10-26_catrina-posada-monerismo`, `2026-10-26_hongo-gente-diminuta`, `2026-10-26_papel-picado-dia-muertos`, `2026-10-26_papel-picado-dia-muertos_parte2`, `2026-10-26_pimiento-verde-rojo`, `2026-10-27_cempasuchil-ciencia`, `2026-10-27_corneja-decision-rapida`, `2026-10-27_ddm-parte3-pomuch`, `2026-10-27_familia-ajolote`, `2026-10-27_kids-serpiente-voladora`, `2026-10-27_noct-anfibio-marino`, `2026-10-28_ddm-parte4-templo-mayor`, `2026-10-28_familia-voyager-disco-oro`, `2026-10-28_kids-titanoboa`, `2026-10-28_monarca-almas`, `2026-10-28_mosquito-fruitless-audicion`, `2026-10-28_noct-lince-milanos`, `2026-10-28_pan-de-muerto-huesos`, `2026-10-29_juno-choque-proa`, `2026-10-29_muralismo-cu`, `2026-10-30_arqueas-origen-eucariotas`, `2026-10-30_kromdraai-primera-fecha`.

El único borrador anterior sin QA y sin salida/publicación es `2026-10-31_smartpe-edicion-plantas`. Se realizó lectura en frío independiente y se registró **FAIL 80** en su storyboard. Checks: pregunta central true; apertura in medias res false; progresión true; transiciones causales true; giro científico explicado false; límite de evidencia true; payoff true. Flags: `APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES` y `GIRO_CIENTIFICO_NOMBRADO_SIN_EXPLICAR_MECANISMO`. Se retiraron mecánicamente sus `asset_filename`, `asset_type` y `export.filename`; se añadieron `approved_assets=[]` y `export.render_status=NOT_GENERATED`. No se modificó narración ni claims. Sigue estructuralmente no apto: 166 palabras, falta `narrative_contract`, faltan campos causales por escena, no hay capa mapa/dato y la configuración de voz no coincide con el contrato. No se creó entrada de cola.

Contradicciones documentales detectadas, sin reescribir claims: `2026-10-28_mosquito-fruitless-audicion` dice `BORRADOR_SIN_RENDER` pese a salida/publicación; `2026-10-27_corneja-decision-rapida` dice candidato no publicado pese a salida/publicación; `2026-10-30_kromdraai-primera-fecha` conserva estado de propuesta pese a salida/publicación; `2026-10-30_arqueas-origen-eucariotas` dice borrador sin render pese a carpeta de salida. No se halló un `ESTADO_EJECUCION.md` activo en esos cuatro proyectos para una corrección permitida. Se excluyeron de esta revisión las exclusiones expresas: kids 3-nov 07:00, Machu Picchu 4-nov 19:00 y slots 23:30 de dato del día.

## 6. Datos, estilos y rotación

- Catálogo `scripts/estilos.json`: 50 estilos; todos los IDs usados por los doce del lote y los dos del día existen.
- Reutilización observada: `papel_rasgado_capas` en árboles/rana y `art_deco_poster` en arena/estrella. No se inventa una regla de prohibición; la rotación no puede validarse con el ledger obsoleto.
- `data/temas_del_dia.json`: última fecha 28-oct; `data/rotacion.json`: 31-oct; `data/estilos_usados.json`: 28-oct. Son insuficientes para validar rotación actual.
- `data/horarios.json`: feature actualizado 9-nov; main 16-nov. Ambos contienen solo dos ventanas, mientras `scripts/rotacion.py` define cinco (07:00, 13:30, 17:00, 19:00, 23:30). La configuración de ventanas es contradictoria/incompleta.
- `data/publicaciones.json`: feature 22 registros; main 48. El registro de feature no refleja los sidecars ni varias publicaciones de noviembre. `data/cola.json` tampoco es inventario exhaustivo.
- No se modificó ningún `data/*.json`.

## 7. Actions y Pull Requests

### Actions
- Run `44824370570`, workflow `CAPCOT — validar preproducción Kuroshio`, commit `6b764c5328f1b2ac9641e8959c487b41927eb180`, 2026-11-20T21:54:11Z, success.
- Comando: `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`; salida `OK`, exit 0. No incluyó `--check-doi`.
- Los blobs de storyboard, validador y workflow son idénticos entre ese commit y el HEAD del PR; el PASS estructural aplica al contenido actual, no al DOI.
- No se ejecutó el validador localmente; el resto de las comprobaciones de esta auditoría son estáticas.

### PRs abiertos, no integrados
- **#3** `feature/capcot-video-discovery-continuity → main`: OPEN/DRAFT, 681 archivos. Cambia workflow, scripts, contratos y múltiples `data/*.json`; no hacer merge. El diff contiene referencias `asset_filename` en snapshots históricos de `cola/bloqueados` y `salidas`, además de asignación en etapa de producción; no deben trasladarse a preproducción.
- **#4** rama de reconciliación robot → feature: OPEN, solo propone cambiar el estado de robot a frames generados en chat pendientes de subida; no integrado y ya queda superado por la evidencia de producción en main. No merge.
- **#6** supervisor IA → feature: OPEN; workflow/configuración de supervisor, sin cambios relevantes en storyboards, cola, ledger o contrato Grok. No merge.
- **#14** `chatgpt/quasar-audit-fixes-20261115 → main`: OPEN/NOT MERGED. Añade `asset_filename` a las ocho escenas del storyboard de Quasar, cambia ledger, mantiene `narrative_qa` FAIL/82 y no ejecuta `validar_storyboard.py --check-doi`. **No apto para integración** por contrato de preproducción.

No se revisaron APIs: no apareció un cambio oficial nuevo sustentado en este corte.

## 8. Acciones ejecutadas y límites

1. Se añadió `narrative_qa` independiente FAIL/80 a SmartPE y se retiraron únicamente placeholders de assets/nombre de exportación; narración y claims intactos.
2. Se añadió el run #5 a `proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/ESTADO_EJECUCION.md`; el bloqueo DOI permanece.
3. El estado de robot 9-nov ya estaba reconciliado como `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no se modificó.
4. No se promovió ningún storyboard, no se movió ni borró ninguna entrada, no se escribió en `main`, `data/*.json`, workflow, secretos ni `cola/estado/`.
5. No se generaron cápsulas, frames, imágenes, voz, audio, video ni renders; no se publicó ni se consumieron créditos.

**Resultado:** cero entradas nuevas de cola y cero dispatches. Los dos borradores del 20-nov quedan en proyectos hasta resolver DOI; los FAIL siguen fuera de cola; los proyectos con producción previa quedan bloqueados contra redispatch.


## Revalidación del operador único — run 10 — 2026-11-20 18:05 CDMX

### Ejecuciones y corte

- Agente de investigación CAPCOT: última ejecución registrada **COMPLETED**, 20-nov 08:40 CDMX.
- Auditor CAPCOT: última ejecución registrada terminó **FAILED** el 20-nov 17:07 CDMX. Este run realizó la relectura manual de inventario, storyboards, colas, publicaciones, workflows, CI y PRs; no disparó Actions.
- Operador único: la ejecución anterior terminó 16:18 CDMX; el run actual inició 18:03 y este apéndice no le atribuye un `completed_at` que todavía no consta.

### Storyboards recientes y slots del 21-nov

La rama feature se releyó completa. Main conserva para el 21-nov dos asignaciones: `oxoboranos-estables` a las 13:30 y `robot-ensambla-orbita` a las 19:00. No hay una asignación de main a las 17:00 ni a las 23:30; por tanto, no se encontró colisión exacta para los dos borradores nuevos.

| Proyecto | QA narrativo | Revisión estructural estática | Decisión |
|---|---:|---|---|
| `2026-11-21_fentale-metano-sin-erupcion` | PASS 90 | 8 escenas, 170 palabras, 78 s de escenas + 6 s de cortinilla = 84 s; voz, catálogo, prompt_base, mapa, capa de datos, fuentes y campos de escena presentes; sin medios ni rutas | Permanece en `proyectos/`. DOI primario identificado, pero `--check-doi`/Crossref no ejecutado. La página editorial fecha el artículo el 19-nov sin hora de publicación; no se puede certificar la ventana de actualidad de 48 h para el slot 21-nov 23:30. No promover |
| `2026-11-21_pulsar-gamma-reticulo` | FAIL 83 | 8 escenas, 209 palabras, 84 s; estructura, mapa, datos y prompt_base presentes | Permanece en `proyectos/`; falla narrativa. No promover |

En ambos casos: no existe `cola/estado/<project_id>.json`, no hay copia en `cola/entrada/`, no hay salida ni marker individual de Grok. Estado: **RECEPCION_GROK_NO_CONFIRMADA** y **NOT_DISPATCHABLE**. El preflight de estructura de esta relectura fue estático y no sustituye al validador Python oficial. No se generaron medios, frames, voz, audio ni vídeo.

Los storyboards recientes restantes se releyeron sin repetir PASS válido cuando la narración no cambió: Lestes 90, Quasar 82 FAIL, polen 91, suelo 89, hidrotermales 68 FAIL, Kuroshio 90, oro poroso 91, estrella dentro de estrella 90, marea cerebral 92 y sapropeles 91. Kuroshio tiene CI estructural SUCCESS en run `44832382024`, pero el log ejecuta `scripts/validar_storyboard.py` sin `--check-doi`; no acredita DOI/Crossref.

### Revalidación de los 12 IDs del lote 5–7 nov

Los 12 storyboards siguen fuera de promoción. El preflight estático basado en las reglas del validador encontró **85 escenas, 510 campos narrativos ausentes** (seis por escena) y **75 SFX vacíos**. El proyecto de árboles además carece de capa de mapa y de datos. Dos QA PASS previos (Venus 88 y arena 94) se conservaron sin repetir; los otros diez siguen FAIL:

| ID | QA vigente | Procesamiento previo / decisión |
|---|---:|---|
| `2026-11-05_kids-dia-en-venus` | PASS 88 | TikTok y Facebook publicados; YouTube ID `phVfyHp3CnY` en evidencia de analítica. No redispatch |
| `2026-11-05_comida-palomitas` | FAIL 82 | YouTube, TikTok y Facebook publicados; sidecar refiere MP4 bajo `/workspace`, no verificable en el árbol. No redispatch |
| `2026-11-05_inter-arboles-se-comunican` | FAIL 78 | Sin salida exacta; existe tema relacionado publicado el 7-nov bajo `arboles-comunicacion-bosque`. No duplicar tema |
| `2026-11-05_inter-rayo-globular` | FAIL 81 | Sin evidencia de publicación o programación; fecha vencida y estructura inválida |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL 80 | YouTube y TikTok publicados; Facebook aparece programado, no confirmado. MP4 local no verificable en el árbol. No redispatch |
| `2026-11-06_comida-aguacate-negro` | FAIL 79 | YouTube y TikTok publicados; Facebook aparece programado, no confirmado. MP4 local no verificable en el árbol. No redispatch |
| `2026-11-06_inter-ranas-congeladas` | FAIL 83 | YouTube y TikTok publicados; Facebook aparece programado, no confirmado. MP4 local no verificable en el árbol. No redispatch |
| `2026-11-06_inter-arena-cantante` | PASS 94 | YouTube, TikTok y Facebook publicados; además existe otro ID de YouTube `ztIkYcXB91U` programado a las 19:00: riesgo de duplicado pendiente, no cancelar |
| `2026-11-07_kids-huesos-bebe` | FAIL 82 | Sin evidencia de publicación o programación; fecha vencida y estructura inválida |
| `2026-11-07_comida-hielo-caliente` | FAIL 81 | YouTube privado con `publishAt`, TikTok programado y Facebook publicado. MP4 referenciado no está en el árbol. No redispatch |
| `2026-11-07_inter-pulpo-suenos` | FAIL 72 | Sin evidencia de publicación o programación; fecha vencida y estructura inválida |
| `2026-11-07_inter-nubes-pesan` | FAIL 78 | YouTube, TikTok y Facebook publicados el 12-nov; MP4 referenciado no está en el árbol. No redispatch |

Los siete proyectos con sidecars (Venus, palomitas, ballena, aguacate, ranas, arena e hielo) y Nubes tienen evidencia de procesamiento/publicación o programación previa. Los estados de plataforma no son equivalentes: en ballena, aguacate y ranas Facebook sigue solo como programado; en hielo YouTube permanece privado/programado. No se afirma publicación donde el registro no la confirma. Los archivos `cola/estado/` siguen ausentes; no se infiere recepción Grok a partir de sidecars o IDs públicos.

### Cola, producción preexistente y Grok

- `cola/entrada/` en feature conserva únicamente dos carpetas anidadas: robot y ratas topo; **no hay JSON plano en la raíz**. El selector de `capcot-grok-dispatch.yml` usa `find -maxdepth 1` y `cola/entrada/*.json`; esas carpetas no son seleccionadas.
- Robot: el estado de feature ya dice `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. Main tiene el mismo proyecto y slot 21-nov 19:00, YouTube ID `ZG4iQgmWrLI`, programación privada y `capsula.mp4` presente. Clasificación: **CONFLICTO_DE_SLOT_ENTRE_RAMAS**; no redispatchar.
- Ratas topo: la carpeta de entrada de feature contiene ocho PNG pero no storyboard; el storyboard PASS 91 está en bloqueados. Main conserva programación/publicación YT/TT/FB; el MP4 referenciado no existe en el árbol. Clasificación: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** y **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- REACT: main mantiene programación privada a las 13:45 del 20-nov; no se encontró `capsula.mp4` en el árbol. No redispatchar; medios no verificados.
- `handoffs/grok_inbox/` solo contiene el marker del robot. No es recibo de Grok. No hay archivos de estado individual.
- El workflow actual admite fallback de inbox sin webhook; el último intento histórico disponible (1-nov, run `41306776689`) registró `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` vacíos. No existe ejecución posterior del dispatcher en la rama feature. No se disparó workflow ni se envió payload.
- No existe un archivo `historial_youtube.json` en los árboles main/feature; esta revalidación usó `data/publicaciones.json`, `data/horario_2026-11-12.json`, sidecars y registros `programacion/publicacion` disponibles.

### CI, Issues y PRs

- Run Kuroshio `44832382024`: SUCCESS estructural; el comando no incluyó `--check-doi`.
- PR #3 sigue draft y abierto, con 681 archivos; contiene cambios amplios de datos/workflows. No fusionar.
- PR #6 (supervisor/workflow), #13 (auditoría independiente) y #14 (correcciones Quasar) siguen abiertos. PR #14 añade `asset_filename` a escenas y contradice el contrato de preproducción; no fusionar.
- PR #4 documental y Dependabot #7–#9 siguen abiertos; no se fusionó ninguno.
- Issue #11 sigue abierto pese a conservar etiqueta `hecho`; no se cerró ni se modificó.

No se modificaron `data/*.json`, main, secretos, permisos, decisiones editoriales ni estados Grok. No se publicaron ni programaron piezas, no se generaron medios y no se consumieron créditos.


---

## Revalidación del operador único — run 11 — 20-nov-2026 20:08 CDMX

### 1. Cambios ejecutados y lectura de vuelta

- **Nuevo borrador** `proyectos/2026-11-21_homo-erectus-selva-tropical/storyboard.json`, commit `bdec12ec9c81fab42cb9d5543532a3f929f24713`. Lectura de vuelta confirmada: 8 escenas, 196 palabras de narración, 78 s de escenas + 6 s de cortinilla = 84 s, gancho de 5 palabras, cierre hablado exacto, voz `es-MX-JorgeNeural` (+7%, −2 Hz), `papel_rasgado_capas`, mapa con localizador urbano real de Chongzuo y capa de cronología de los dos depósitos. La coordenada ubica la ciudad, no las cuevas. `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin nombres ni rutas de assets, `publicacion.status=PENDIENTE_DECISION_GROK`. No se creó `narrative_qa` ni `ESTADO_EJECUCION.md`; sigue en proyectos y no está preparado.
- **Normalización mecánica de rotación**: Fentale `audio.cama_musical` `sintetico:pulso` → `pulso`, commit `9522502cf28361ef5ea47aca154fc413986c6d91`; Púlsar `sintetico:arpegio` → `arpegio`, commit `db4f09480971d4ea68d953980c8fffc9eb07c173`. La cama prevista no cambió; solo se normalizó la etiqueta que consume `scripts/rotacion.py`.
- Fentale conserva QA independiente PASS 90; no se repitió. Su `estructura=paradoja_mecanica` no pertenece a `ESTRUCTURAS` en `scripts/rotacion.py`. No se cambió porque elegir otra estructura sería una decisión editorial. DOI/resolvedor y validador oficial siguen pendientes.
- Púlsar conserva FAIL 83; no se reescribió la narración. Marea cerebral PASS 92 y Sapropeles PASS 91 permanecen sin cambios; no se repitieron.

### 2. Slots, producción previa y recepción

- Para 21-nov se verificaron cuatro ocupaciones existentes: Oxoboranos main 13:30 (YT `K4qNkx2f4RI`, publishAt `2026-11-21T19:30:00Z`, TT/FB programados); Púlsar feature 17:00; robot orbital main 19:00 (YT `ZG4iQgmWrLI`, publishAt `2026-11-22T01:00:00Z`, TT/FB programados); Fentale feature 23:30. El slot 07:00 está dentro de la ventana matutina 06:30–07:30 y no tiene conflicto exacto en main ni feature. Con el borrador nuevo se llega al máximo de cinco piezas/reservas del día (dos propias, tres externas); no crear más para 21-nov.
- Para los cinco storyboards del 20–21 nov, las 5 lecturas de `cola/estado/<project_id>.json` devolvieron HTTP 404; registrar `RECEPCION_GROK_NO_CONFIRMADA`. También devolvieron 404 las rutas planas/anidadas de `cola/entrada`, `cola/bloqueados` y `salidas` para esos cinco IDs. No hay copia de cola ni salida; todos siguen `NOT_DISPATCHABLE`.
- Los 12 IDs obligatorios del lote 5–7 nov conservan 2 PASS y 10 FAIL del run 10. Ninguno de los tres commits de este run tocó esos doce storyboards; las doce lecturas de estado devolvieron 404. No se repitió QA PASS ni se promovió ningún ID.
- `main/data/publicaciones.json` no muestra otros `publishAt` futuros para 21-nov aparte de Oxoboranos 13:30 y robot 19:00. El ID `ztIkYcXB91U` continúa siendo solo un riesgo mencionado en un sidecar anterior; no aparece en el inventario actual de publicaciones y no se declara programado.
- **Corrección de registro anterior:** `data/vistas_historico.json` no está vacío. En main contiene 106 snapshots, último `2026-11-18T13:56-06:00`; en feature contiene 74, último `2026-10-28T08:08-06:00`. La nota del run 10 que lo describió como vacío era incorrecta. No existe un archivo separado `historial_youtube.json`; el histórico de vistas está desactualizado y no permite confirmar publicaciones posteriores al 18-nov.

### 3. Actions, workflow y CI

- Worker main run `44839666536`: log literal `[trabajador] sin trabajo en cola.`; no procesó los borradores feature.
- Callback main run `44850289947`: leyó `ajustes_entre_modelos/DELEGACIONES.md` y filtró entradas pendientes dirigidas a Copilot; no encontró ninguna, no creó Issues `[callback]` y no asignó trabajo. El workflow conserva `Issues: write`; si aparecen entradas `PARA: Copilot`, sí puede crear Issues automáticamente.
- `.github/workflows/capcot-grok-dispatch.yml` no se disparó y no se enviaron webhooks. Su selector sigue limitado a JSON planos de primer nivel; las carpetas anidadas históricas no son dispatchables.
- Los commits nuevos `bdec12e`, `db4f094` y `9522502` no tienen status checks publicados al momento de esta lectura; no se declara CI verde. PR #3 sigue OPEN/DRAFT con HEAD `bdec12e`; PR #14 sigue abierto y conserva `asset_filename` en preproducción; no se fusionó ni se disparó workflow.
- La auditoría programada CAPCOT terminó FAILED a las 17:07 CDMX; este run hizo la relectura manual. No se generaron medios, no se consumieron créditos, no se alteraron `data/*.json`, publicaciones ni estados Grok.
