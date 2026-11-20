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
