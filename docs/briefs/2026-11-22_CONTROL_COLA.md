# Control de cola y auditoría CAPCOT — 2026-11-22

**Corte:** 2026-11-22 01:58 CDMX  
**Rama:** `feature/capcot-video-discovery-continuity` · HEAD observado `8e3df802`  
**Main:** HEAD observado `22cc55e0`

## Resultado

- **0 proyectos promovibles; 0 dispatches; 0 medios generados.**
- No se modificaron `data/*.json`, main, estados Grok, secretos, permisos ni programación.
- No se disparó Actions ni se envió payload a Grok.
- Se relevaron 7 proyectos recientes, los 12 IDs del lote 5–7 nov, cola en ambas profundidades, bloqueados, salidas, main, inventario de publicación, workflow y Actions.

## Proyectos recientes: 21–23 nov

| Proyecto | Slot | QA existente | Defecto estructural / decisión |
|---|---|---:|---|
| `2026-11-21_fentale-metano-sin-erupcion` | 21 nov 23:30 | PASS 90 | Falta `prompt_base` y `map`; main ya contiene `Eldk0fVWqpo`: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` |
| `2026-11-21_homo-erectus-selva-tropical` | 21 nov 07:00 | FAIL 83 | Falta `prompt_base` y `map`; slot pasado |
| `2026-11-21_pulsar-gamma-reticulo` | 21 nov 17:00 | FAIL 83 | Falta `prompt_base` y `map`; 17:00 sigue en prueba |
| `2026-11-22_voyager-1-un-dia-luz` | 22 nov 07:00 | FAIL 83 | Falta `prompt_base` y `map`; main ocupa Salem |
| `2026-11-22_bao-estrella-fusion-andromeda` | 22 nov 13:30 | FAIL 84 | Falta `prompt_base` y `map`; main ocupa Gutenberg |
| `2026-11-22_yubarta-genoma-soplo` | 22 nov 17:00 | PASS 90 | Falta `prompt_base` y `map`; main ocupa Ada y 17:00 sigue en prueba |
| `2026-11-23_tropical-biodiversity-turnover` | 23 nov 13:30 | FAIL 82 | Falta `prompt_base` y `map`; `SRC-002=PENDING_SOURCE`; main ocupa Rosetta |

Los siete tienen 8 escenas y 171–208 palabras. Los seis campos narrativos por escena están presentes. No se repitió QA ni se reescribieron narraciones. Los PASS existentes no compensan la falta de mapa y `prompt_base`.

## Lote 5–7 nov: 12 IDs canónicos

`2026-11-05_comida-palomitas`, `2026-11-05_inter-arboles-se-comunican`, `2026-11-05_inter-rayo-globular`, `2026-11-05_kids-dia-en-venus`, `2026-11-06_comida-aguacate-negro`, `2026-11-06_inter-arena-cantante`, `2026-11-06_inter-ranas-congeladas`, `2026-11-06_kids-ballena-azul-corazon`, `2026-11-07_comida-hielo-caliente`, `2026-11-07_inter-nubes-pesan`, `2026-11-07_inter-pulpo-suenos`, `2026-11-07_kids-huesos-bebe`.

- QA existente: **2 PASS** (Venus 88, arena 94), **10 FAIL**.
- Estructura: 85 escenas; **510 campos narrativos estructurales ausentes** (seis por escena).
- Nueve coincidencias de video/publicación preexistente en main; no redispatchar:
  - palomitas `zTP5akrGA9M`
  - árboles `EX0W3q-yKRw`
  - Venus `phVfyHp3CnY`
  - arena `m4RqQRaz55k`
  - ranas `UBFuKBU3cx0`
  - corazón de ballena azul `wbFrlM2e_YE`
  - hielo caliente `HSgrnejAcaI`
  - peso de nubes `4Qpl17Ts_vI`
  - huesos de bebé `uEsoscBrfgU`
- Rayo globular, aguacate negro y sueños del pulpo no tienen coincidencia inequívoca de publicación. Siguen sin ser promovibles por QA/estructura.
- Las salidas de árboles e hielo contienen metadatos/publicación, pero no `capsula.mp4` en el árbol Git. Para los nueve casos con video ID: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; donde el MP4 no aparece: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- Las copias heredadas de nombres anteriores ya están en `cola/bloqueados/`. Los 12 IDs canónicos siguen en `proyectos/`; no hay copia de esos IDs en cola activa. No se movió ni borró nada.

## Cola, Grok y medios

- En feature, `cola/entrada/` contiene solo `.gitkeep` y `2026-11-09_dato-robot-ensambla-orbita/` anidado; no hay JSON plano.
- `cola/estado/<id>.json` devolvió 404 para los 7 proyectos recientes, los 12 IDs y el robot: **20 comprobaciones**, todas `RECEPCION_GROK_NO_CONFIRMADA`.
- El marcador en `handoffs/grok_inbox/` no es un estado Grok ni prueba de recepción.
- El robot tiene `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` en `ESTADO_EJECUCION.md`; main registra `ZG4iQgmWrLI`. Sus medios aparecen en la carpeta de cola, pero no hay salida local equivalente. No redispatchar.
- Main contiene entradas anidadas de árboles e hielo con procesamiento previo; sus `cola/estado` también devolvieron 404. No se modificaron.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` selecciona JSON planos de primer nivel (`find -maxdepth 1`); `scripts/procesar_cola.py` admite carpetas anidadas. No hay ejecución reciente de dispatch en las Actions consultadas.
- No se comprobó la existencia de secretos del webhook; no se leyeron ni modificaron valores.

## Main, horarios e historial

- Ventanas autorizadas: 06:30–07:30 y 13:00–14:30. 16:30–18:00 continúa en prueba; 19:00 fue retirado; 23:30 es el slot fijo de dato del día.
- Main ocupa 07:00/13:30 del 22–29 nov en el snapshot disponible. El 22 nov aparecen Salem (07:00), Gutenberg (13:30), Ada (17:00) y Webb (19:00); el 23 nov, Nudillos (07:00), Rosetta (13:30), Pirámides (17:00) y Gutenberg (19:00).
- 22 nov 23:30 no aparece ocupado, pero el APOD de Juno del día duplica la línea Juno ya publicada el 29 oct; no se seleccionó.
- No se infiere disponibilidad para 1 dic: main no contiene un plan que confirme ese horizonte.
- `data/miniaturas_auditoria_2026-11-21.json`: 36 elementos sin MP4 local y 6 colisiones de `publishAt`.
- `data/publicaciones.json` tiene solo dos registros; no es inventario completo. No existe `historial_youtube` en `data/`; `vistas_historico.json` tiene 107 entradas y no incluye el ID del robot. No se afirmó que videos antiguos sigan programados.
- `data/temas_del_dia.json` está vacío; `data/rotacion.json` y `data/estilos_usados.json` no reflejan rotación reciente (últimos registros visibles: 31 oct y 28 oct). Se dejaron intactos.

## RSS y radar científico

Las ocho fuentes de `scripts/tendencias.py` y Google Trends México se consultaron por HTTP directo. Los nueve endpoints devolvieron el error literal:

`URLError: <urlopen error [Errno -3] Temporary failure in name resolution>`

El script no se ejecutó dentro del repositorio; el error corresponde a las consultas HTTP de esta sesión. Se usaron fuentes oficiales como respaldo.

| Candidato | Fuente / fecha | Hecho respaldado | Estado |
|---|---|---|---|
| Nubes crepusculares de Curiosity | NASA Photojournal, 20 nov 2026 | Imagen tomada 31 oct 2026, sol 5061; aparecen por poco tiempo cada otoño sobre Gale Crater. Coordenada de referencia del aterrizaje: 4.6°S, 137.4°E; no es la posición exacta de la nube. | Candidato para slot regular futuro |
| Floración del desierto de Atacama | NASA Earth Observatory, 19 nov 2026 | Landsat 8/9, imágenes del 14 sep y 24 oct; NASA compara el episodio con 13 floraciones de 1981–2015 y lo describe como posiblemente el más extenso de la era satelital. | Candidato; no apto para dato del día 22 nov |
| Agua antigua más allá de Neptuno | NASA Science, 18 nov; Science Advances, 11 nov | 12 partículas de polvo estratosférico; el origen en el cinturón de Kuiper se infiere por huellas de partículas energéticas, no por muestreo directo. DOI visible: `10.1126/sciadv.aeg1602`. | PENDING_CROSSREF |
| Dos especies de tardígrados marinos | Senckenberg / ZooKeys, 20 nov | Dos especies descritas en el monte submarino Senghor. DOI: `10.3897/zookeys.1295.205902`. | NO_DUPLICAR: ya existe cápsula de tardígrados en salidas del 24 oct |
| Colores de Júpiter en APOD | NASA APOD, 22 nov | Publicación del día sobre una imagen Juno del paso 14 de 2018. | NO_DUPLICAR: ya existe proyecto/salida Juno del 29 oct |

Crossref API y resolvedor no pudieron consultarse. Error de red: `Temporary failure in name resolution`. Los DOI visibles en páginas editoriales no se declararon verificados por Crossref.

**Decisión:** no se creó storyboard. El slot 22 nov 23:30 carece de candidato del día que supere actualidad y no duplicación; los slots regulares 22–29 nov están ocupados; 1 dic no está confirmado por main. No se generaron medios, placeholders ni QA narrativo.

## CI y cierre

- PR #3 sigue OPEN y `mergeable_state=dirty`; no se fusionó.
- CodeQL del PR: run `44999261966`, éxito.
- Semgrep en main: run `44988989131`, 32 findings bloqueantes; la carga SARIF se omitió al fallar el análisis.
- `semgrep.yml` en feature usa `if: always()` y conserva el artifact 7 días; todavía no hay ejecución de Semgrep en feature que pruebe esa corrección.
- No se disparó Actions.

**EJECUTADO:** lectura y auditoría de 19 storyboards, 20 estados Grok, cola, bloqueados, salidas, main, inventario, workflow, Actions y fuentes oficiales.  
**VERIFICADO:** 0 proyectos promovibles; nueve publicaciones/videos preexistentes en el lote; ausencia de MP4 Git en las dos salidas inspeccionadas; 20 estados Grok no confirmados; PR #3 abierto/dirty.  
**PENDIENTE:** revisión narrativa independiente para borradores nuevos; corrección estructural por sus autores; vínculo inequívoco del video `4Qpl17Ts_vI`; acceso a RSS/Crossref; agenda confirmada a partir del 1 dic.

No se reescribieron narraciones, no se alteraron estados Grok, no se promovió ni redispatchó ningún paquete.
