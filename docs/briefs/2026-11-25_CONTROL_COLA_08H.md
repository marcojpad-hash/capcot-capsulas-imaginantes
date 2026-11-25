# Control de cola CAPCOT — 2026-11-25 (corte 08H CDMX)

**Rama auditada:** `feature/capcot-video-discovery-continuity`  
**HEAD de la rama:** `21067c07b0bb06ae5fc46d5df9611bf2197a1743`  
**HEAD de `main` consultado en solo lectura:** `020f5ae3fa7ca8131671ac94bf9b29c22ffff425`  
**Alcance:** inventario, backlog interdiario, lote 5–7 nov, cola/handoff, programación, producción preexistente y Actions. No se dispararon workflows.

## 1. Radar, fuentes y slots

- `docs/briefs/2026-11-25_RADAR_CAPCOT.md` ya existe y contiene cinco candidatos del corte anterior. No se creó otro radar ni se promovió un candidato nuevo.
- Se reintentaron los RSS definidos en `scripts/tendencias.py` y Google Trends RSS México. Persisten estos errores de lectura XML: ScienceDaily (ciencia/salud/espacio) `400 Unsupported content-type: application/xml`; Phys.org `400 Unsupported content-type: text/xml`; NASA y UNAM Global `400 Unsupported content-type: application/rss+xml`; ESA Space Science `404 Not Found`; Nature `500 Redirected to idp.nature.com/authorize`; EurekAlert y SINC `URL is not accessible via this tool`. Google Trends RSS México también devolvió `URL is not accessible via this tool`.
- **Respaldo oficial:** la página HTML de Google Trends México abrió con 198 tendencias totales y 25 visibles en la vista consultada. Ninguna de las primeras 25 aportó un tema científico, de naturaleza, cocina, cuerpo o espacio utilizable sin una fuente primaria adicional.
- Se cribaron cuatro investigaciones recientes como alternativas, pero ninguna superó la verificación Crossref/resolvedor; quedan `PENDING_SOURCE`, no seleccionadas:
  - EuSi y textura magnética p-wave — Nature, DOI declarado `10.1038/s41586-026-11295-9`; página editorial no verificable en este corte.
  - Inspiral de envoltura común en AT 2025abao — Nature, DOI declarado `10.1038/s41586-026-11221-z`; página editorial accesible, resolvedor pendiente.
  - Transporte de glucosa independiente de insulina en músculo esquelético de ratón — Communications Biology, DOI declarado `10.1038/s42003-026-10848-y`; página editorial no verificable en este corte.
  - Sistema triple Welopō’ai — Astronomy & Astrophysics, DOI declarado `10.1051/0004-6361/202661214`; página editorial devolvió 403.
- Crossref REST y los resolvedores DOI no entregaron una respuesta verificable. Ninguno de esos cuatro candidatos se marca `VERIFICADO_CROSSREF`.
- No hay slot libre: la programación observada mantiene siete publicaciones diarias del 25 al 28, por encima del tope de cinco. Las ventanas vigentes son 06:30–07:30 y 16:30–18:00; el dato de 23:30 es fijo. No se creó storyboard.

## 2. Cola, dispatch y recepción

- En `feature/capcot-video-discovery-continuity` hay un paquete anidado en `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/`; no hay JSON plano en la raíz de `cola/entrada/`.
- Su marcador `handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json` conserva `status=pending`, rama `main` y ruta anidada. Es un marcador del repositorio, no un acuse de Grok.
- Clasificación: **NOT_DISPATCHABLE** por profundidad/ruta; **RECEPCION_GROK_NO_CONFIRMADA** porque no existe `cola/estado/<project_id>.json`.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` existe en la rama de trabajo, pero no en `main` (404). Su trigger de push exige `cola/entrada/*.json` plano y su selector usa `find -maxdepth 1`; el paquete anidado no satisface esa ruta. No se encontró una ejecución de ese workflow en las Actions consultadas.
- El webhook es opcional: el workflow puede dejar el marcador en el buzón sin webhook. No se leyeron valores de secretos y no se infirió recepción a partir del marcador.
- Inventario de rutas: `main` tiene 33 directorios anidados de entrada y cero JSON planos; la rama de trabajo tiene un directorio anidado y cero JSON planos. No hay archivos `cola/estado/` en ninguno de los dos árboles.

## 3. Proyectos, QA y backlog 5–7 nov

- La rama de trabajo conserva 90 storyboards en `proyectos/`; no hay storyboard nuevo del 25 nov. El diff desde el control 04H no contiene cambios de storyboards, por lo que no se repitió ningún PASS narrativo válido.
- Lote de 12 IDs del 5–7 nov: **2 PASS** (Venus, 88; arena cantante, 94) y **10 FAIL**. Los dos PASS conservan `review_basis=lectura_en_frio_solo_narracion`, siete checks verdaderos y `critical_flags=[]`.
- Revisión estructural de esos 12 archivos: 85 escenas; 510 ausencias en los seis campos explícitos de progresión por escena; 11/12 tienen puntos con coordenadas en una capa de mapa (pines de instituciones, no ubicación demostrada del fenómeno); 1/12 carece de esa capa; no se encontró un objeto/campo de gráfico de datos en ninguno; 75/85 escenas no tienen SFX no vacío y 10/85 sí; ambiente presente en 85/85.
- Los 12 conservan 9:16, voz es-MX-JorgeNeural con rate +7% y pitch -2Hz, 170–221 palabras, 7–8 escenas y objetivo de 84 s. No tienen campo dedicado `hook`; la primera oración de apertura mide 9–20 palabras, por encima del límite de seis. `approved_assets=[]`, `export.render_status=NOT_GENERATED` y sin `export.filename`.
- No hay `ESTADO_EJECUCION.md` para esos 12, no hay copias en `cola/entrada/` y no se encontró estado PREPARADO que corregir. Hay nueve copias heredadas en `cola/bloqueados/`; permanecen intactas.
- El proyecto `2026-11-24_magnetismo-p-wave-eusi` existe solo en `main`. Su `programacion.json` registra `programado_para_publicar` para el 24 nov a las 17:15 CDMX, hora ya vencida; el storyboard tiene seis escenas y 121 palabras, carece de `narrative_qa` y de fecha/slot propios, y referencia `capsula.mp4`, archivo que no aparece en el árbol. El cold read independiente previo quedó en FAIL 40/100; no se repitió.
  - Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `PROGRAMACION_VENCIDA_POR_VERIFICAR`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` y `RECEPCION_GROK_NO_CONFIRMADA`. No se identificó un storyboard de la rama de trabajo con el mismo slot; no se declara conflicto entre ramas.

## 4. Producción preexistente, programación e historial

- `main` conserva nueve reworks del 25–29 nov con storyboard y `render.log`. Los logs miden entre **86.47 y 88.80 s**, dentro del intervalo 75–90 s. No aparecen los MP4 referenciados en el árbol Git; por tanto, duración medida no equivale a medios verificables en el repositorio.
- Esos nueve reworks ya tienen procesamiento/render y programación de TikTok/Facebook a las 10:00 y 15:00, fuera de las ventanas registradas. Sus storyboards no contienen `narrative_qa` ni `approved_assets` y sí referencias de exportación. Se clasifican `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No se canceló ni movió ninguna publicación.
- La auditoría de horarios conserva cuatro colisiones futuras:
  - 25 nov 07:00 — `cPNiOFeY5_k` / `W9g2tPZTpD4`.
  - 26 nov 17:00 — `JqlKsJOVmdE` / `-1DRh_qj7Bg`.
  - 27 nov 07:00 — `jiX6RdwJ1gg` / `nd0rs6iVy8E`.
  - 28 nov 17:00 — `gN6svdqe62Q` / `fcSNbU809ao`.
  Las dos colisiones del 23 y 24 nov ya son pasadas. No se alteró programación.
- `historial_youtube.json` no existe en el árbol. `data/publicaciones.json` contiene 62 registros y no incluye los nueve IDs de rework; esto no se toma como prueba de que no sigan programados en Studio.
- La rotación de pantallas finales sí tiene una actualización nueva en `main`: `data/endscreens_rotacion.json`, 25 nov 08:07. El registro de Studio indica **9/9 verificadas al recargar, 3 aplicadas, 6 ya estaban correctas, 0 fallidas**, `pendiente_studio=false`. El HEAD de `main` cambió solo ese JSON respecto del commit anterior; no cambió storyboards.
- Los inventarios auxiliares siguen desfasados: `data/rotacion.json` llega al 31 oct; `data/temas_del_dia.json`, al 28 oct; `data/cola.json`, al 31 oct; `data/publicaciones.json`, al 1 nov; `data/horarios.json` conserva la política del 9 nov. Se dejan intactos por la regla de solo lectura de `data/*.json`.

## 5. Actions, PRs e Issues

- Worker de cola run **45629608920**: success, pero el log dice que no había paquetes válidos que procesar; no produjo handoff nuevo.
- Semgrep en `main`, run **45630730232**: failure con **37 hallazgos bloqueantes**. El paso de carga SARIF se omitió al fallar el escaneo. La rama de trabajo ya contiene `if: always()` en su workflow Semgrep para conservar el SARIF en futuros fallos; ese cambio no está en `main`.
- Gitleaks run **45630730137**: success.
- PR #3 sigue draft y de gran tamaño (1,400 commits / 710 archivos); CodeQL pasó, pero no hay evidencia de pruebas unitarias, validador estructural ni compuerta DOI en ese run.
- PR #15 sigue abierto; el HEAD no tiene status checks. Sus seis pruebas añadidas no se han ejecutado en ese HEAD. El último Semgrep visible de ese PR registró 27 hallazgos.
- Issue #11 sigue abierto con etiqueta `hecho`, aunque el backlog conserva 10 FAIL narrativos. No se cambió Issue ni PR.

## 6. Resultado del corte

**EJECUTADO/VERIFICADO:** lectura de ambas ramas, inventario de cola y proyectos, lectura de programación y logs, revisión de 12 storyboards, verificación de 9 render logs, lectura de Actions/PRs/Issue y verificación de 9/9 pantallas finales en el registro de Studio.

**PENDIENTE:** recepción Grok individual; liberación de un slot; DOI/resolvedor para candidatos nuevos; resolución de colisiones y verificación de estado real de IDs en YouTube Studio; medios MP4 dentro del árbol; QA estructural/narrativo de los borradores FAIL.

No se generaron medios, no se redactaron storyboards nuevos, no se promovió cola, no se modificó `data/*.json`, `main`, secretos, permisos, programación ni estados Grok.
