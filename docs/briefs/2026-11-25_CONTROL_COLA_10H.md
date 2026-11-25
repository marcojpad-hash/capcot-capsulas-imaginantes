# Control de cola CAPCOT — 25 de noviembre de 2026, 10:02 CDMX

**Rama de auditoría:** `feature/capcot-video-discovery-continuity`  
**HEAD antes de este registro:** `d41690333f18f71586b0aca2bd607c502ba34d7d`  
**HEAD de main consultado:** `020f5ae3fa7ca8131671ac94bf9b29c22ffff425`  
**Resultado:** sin slot libre; sin nueva entrada Grok; no redispatchar producción preexistente.

## 1. Delta desde el control de las 08:00

Compare `21067c07...` → `d416903...`: cinco commits de avance, pero los únicos archivos tocados fueron `data/endscreens_rotacion.json`, los controles de cola 08H/08:30 y el radar. No cambió ningún storyboard ni narración desde el baseline de las 08:00. No se repitió ningún PASS narrativo.

Compare `main` `7b50235...` → `020f5ae...`: dos commits; el único archivo cambiado fue `data/endscreens_rotacion.json` (+173/-5), registro de pantallas del 25-nov 08 aplicado 9/9. `main` se mantuvo en solo lectura.

El inventario reportado a las 08:00 contiene 90 storyboards en la rama feature. En este corte se releyeron 11 storyboards recientes del backlog 20–23 nov para comprobar que sus QA y estructura no habían cambiado.

## 2. Backlog interdiario 20–23 nov — lectura de vuelta

| Proyecto | QA ya registrado | Resultado observado |
|---|---:|---|
| 20-nov Atlántico / humedad / sapropeles | PASS 90, 7/7 | Conserva QA; no se repitió. |
| 20-nov marea cerebral durante el sueño | FAIL 82 | Stakes no suficientemente explicados. |
| 21-nov metano sin erupción | PASS 90, 7/7 | Conserva QA; no se repitió. |
| 21-nov Homo erectus / selva tropical | FAIL 83 | El giro está nombrado, pero no explicado. |
| 21-nov púlsar gamma / Retículo | FAIL 83 | El giro está nombrado, pero no explicado. |
| 22-nov Bao / fusión estelar / Andrómeda | FAIL 84 | Stakes no suficientemente explicados. |
| 22-nov genes y estatura por etapas | FAIL 72, 3/7 | Tres checks verdaderos y tres flags críticos; sigue en borrador. |
| 22-nov Voyager 1 / un día luz | FAIL 83 | Confunde el hito de distancia con su confirmación/registro. |
| 22-nov yubarta / genoma / soplo | PASS 90, 7/7 | Conserva QA; no se repitió. |
| 23-nov supersequías / 722 eventos | FAIL 82 | Stakes no suficientemente explicados. |
| 23-nov tropical biodiversity turnover | FAIL 82 | Stakes no suficientemente explicados. |

Los 11 mantienen ocho escenas, 84 s declarados y entre 172 y 231 palabras. No se crearon medios: `approved_assets=[]` y `export.render_status=NOT_GENERATED` en los borradores de preproducción. Los tres PASS existentes se conservaron sin volver a emitir la evaluación.

## 3. Lote de auditoría 5–7 nov

El lote canónico de 12 IDs conserva **2 PASS y 10 FAIL**; no hubo cambios de narración desde el control anterior. El agregado sigue mostrando 85 escenas, 510 campos dramáticos requeridos ausentes (seis por escena), 75 escenas con SFX vacío y carencias de mapa/dato gráfico en la mayor parte del lote. Los dos PASS previos no se repitieron. Las copias heredadas en bloqueados y las entradas antiguas se dejaron intactas.

## 4. Producción preexistente y programación

`main/data/rehechos_2026-11-22.json` contiene nueve reworks ya programados:

| Fecha CDMX | Tema | ID YouTube | Duración del render.log |
|---|---|---|---:|
| 25-nov 10:00 | Nube de 500 toneladas | `9RxTSifAcpo` | 86.80 s |
| 25-nov 15:00 | Barreleye | `3rwo_sK1e18` | 87.53 s |
| 26-nov 10:00 | Pan en refrigerador | `7pzPfqRSagU` | 88.47 s |
| 26-nov 15:00 | Ratas topo | `MgHVHbeIVS0` | 88.80 s |
| 27-nov 10:00 | Miel | `p06UCGu0-Og` | 86.47 s |
| 27-nov 15:00 | Mar / alarma antirrobo | `HKpani8TTeY` | 87.17 s |
| 28-nov 10:00 | Arena que canta | `6VUxaJtqbF0` | 86.70 s |
| 28-nov 15:00 | Juno / escudo de Júpiter | `Dx3lqkAb8Sc` | 87.40 s |
| 29-nov 10:00 | Dunkelflaute / viento | `m1FeS0mhfZ4` | 88.77 s |

Todos figuran como `private→public programado`; TikTok y Facebook también constan como programados en el registro de reworks. Los MP4 están referenciados en rutas `/workspace/capcot_main/...`, pero no aparecen en los árboles Git. Los dos directorios inspeccionados (nube y barreleye) contienen `storyboard.json`, `metadata.json`, `render.log`, guion, licencias y créditos, no el MP4. Estado: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` y `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.

Hallazgo adicional: el `render.log` del barreleye contiene `AVISO: la cortinilla invade la zona segura inferior`. Es una advertencia de producción pendiente de revisión visual; no se declara QA audiovisual aprobado.

El registro de nube ya pasó su `publishAt` local de 10:00 cuando se hizo este corte. El JSON conserva `private→public programado`, pero `data/publicaciones.json` y `data/rotacion.json` no tienen registro del 25-nov. El intento de abrir el ID de YouTube no fue accesible (`DisabledError`); `data/historial_youtube.json` devolvió 404. Resultado: `PUBLICACION_NO_CONFIRMADA`; no se declara publicado ni se reprograma.

## 5. Cupo, colisiones y compuertas de cola

- Ocupación registrada: **7/5** para 25–28 nov y **5/5** para 29 nov. No hay slot libre.
- Colisiones de `publishAt` identificadas: 23-nov 07:00 y 24-nov 17:00 (pasadas); 25-nov 07:00 (pasada); 26-nov 17:00, 27-nov 07:00 y 28-nov 17:00 (futuras). No se movió ni canceló ninguna.
- `main/cola/entrada`: 33 directorios anidados, sin JSON plano nuevo. `feature/cola/entrada`: un directorio anidado heredado. No existe `cola/estado/` en el árbol feature consultado.
- La ausencia de `cola/estado/<id>.json` significa `RECEPCION_GROK_NO_CONFIRMADA`; no se infiere recepción por la existencia de una carpeta en cola.
- `main/salidas/` no contiene salidas de los nueve reworks del 25–29 nov; la evidencia está en sus carpetas de proyecto y en el registro de reworks.

## 6. CI, Actions y PRs

- Queue worker run `45629608920`: job `trabajar` SUCCESS; log literal `[trabajador] sin trabajo en cola.` No es un dispatch de Grok.
- Semgrep run `45630730232`: FAILURE por **37 hallazgos bloqueantes**, 361 reglas, 1,254 archivos objetivo, ~100% de líneas parseadas; 37 archivos grandes (>1 MB) quedaron omitidos. SARIF no se subió tras el fallo.
- Gitleaks run `45630730137`: SUCCESS.
- Las consultas de runs asociadas a los HEAD actuales de main y feature no devolvieron ejecuciones adicionales. No se disparó ningún workflow.
- PR #3 continúa OPEN/DRAFT. PR #15 continúa OPEN y `mergeable=false`; no se fusionó. Sus pruebas locales/CI pendientes no se sustituyen por lectura estática.

## 7. Datos y reconciliación entre ramas

Se leyeron los JSON raíz de `data/` en feature sin modificarlos. La base de feature sigue antigua en varios registros: `publicaciones.json` llega al 1-nov, `rotacion.json` al 31-oct, `cola.json` al 31-oct, `temas_del_dia.json` al 28-oct, `horarios.json` al 9-nov y `vistas_historico.json` al 28-oct; `endscreens_rotacion.json` sí llega al 25-nov.

`scripts/registro_editorial.py` une `rotacion.json`, `publicaciones.json`, `cola.json` y storyboards encontrados en el árbol. No lee directamente `data/rehechos_2026-11-22.json`; los storyboards de rework tampoco llevan `fecha_objetivo`/`slot_local` en su raíz. Por tanto, la reconciliación automática de feature no incorpora por sí sola esa programación de main: el cruce manual con main sigue siendo obligatorio para evitar slots duplicados. No se alteró `data/*.json`.

## 8. Resultado de este corte

**EJECUTADO:** relectura de HEADs, diff entre ramas, 11 storyboards recientes, cola, dos carpetas de rework, render logs, datos de programación, workflow y logs de Actions, PRs, inventario de datos y radar de fuentes.

**VERIFICADO:** no hay cambios de storyboard desde el baseline 08H; el slot sigue saturado; hay nueve reworks preexistentes; el video de nube no tiene publicación confirmada; el render del barreleye tiene advertencia de zona segura; no hay recibos Grok nuevos.

**PENDIENTE:** revisión visual de medios fuera del repo; confirmación de publicación del ID de nube; resolver colisiones futuras sin cancelar ni mover; reparar el acceso a RSS/Crossref o ejecutar el validador desde un runner autorizado; resolver 37 hallazgos Semgrep.

No se modificaron `main`, `data/*.json`, entradas o bloqueados de cola, estados Grok, programación, workflows, secretos, permisos, ni medios. Este registro y la revalidación del radar son los únicos cambios de este corte.