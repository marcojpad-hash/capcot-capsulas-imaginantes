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
