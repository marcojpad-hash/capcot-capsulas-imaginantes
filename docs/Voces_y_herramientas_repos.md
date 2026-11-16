# Voces y herramientas en los repos de marcojpad-hash

Revisión **solo lectura**, sin modificar ni subir nada a GitHub. Fecha de revisión: 2026-11-16. **Corrección 2026-11-16 (§3.0):** sección de herramientas de búsqueda rehecha llamada por llamada tras el reclamo de Marco; nada subido a GitHub en esta pasada, informe listo para subir.
Repos: los 11 de `marcojpad-hash` (main). Método: conector GitHub, `search_code` / `get_file_contents` / `list_commits` / `list_issues`.

> **Límite de la revisión:** a mitad del trabajo el conector GitHub devolvió **HTTP 429 (too many requests)**. Por regla de rate-limit no se reintentó en caliente. Lo marcado "no verificado" abajo quedó pendiente por ese límite, no porque no exista.

## 1. Voces vigentes

### 1.1 CAPCOT ES — voz oficial

| Dato | Valor vigente |
|---|---|
| Voz | `es-MX-JorgeNeural` |
| Motor | edge-tts, vía Imaginantes (Grok Bot) |
| Rate | `+7%` |
| Pitch | `-2Hz` |
| Pad | `0.3 s` en la guía; `0.35 s` por defecto en el montador |
| Cierre | "Esto fue Datos y ociosidades." |

Evidencia:

- `capcot-capsulas-imaginantes/tools/tts/narrate.py`: `DEFAULT_VOICE = "es-MX-JorgeNeural"`, `DEFAULT_RATE = "+7%"`, `DEFAULT_PITCH = "-2Hz"`. Último commit `eb50a155`, 2026-11-08.
- `capcot-capsulas-imaginantes/docs/GUIA_MODELO_EXTERNO.md` §3: `"voice": {"engine": "edge-tts", "voice_id": "es-MX-JorgeNeural", "rate": "+7%", "pitch": "-2Hz", "pad_seconds": 0.3, "modo_pausas": "continuo"}`.
- `capcot-capsulas-imaginantes/docs/VOCES_POR_TEMA.md`: "JorgeNeural (es-MX) | edge-tts, vía Imaginantes | Voz oficial CAPCOT (+7%, −2 Hz)".
- `capcot-capsulas-imaginantes/docs/LINEA_EDITORIAL_VISUAL.json` v1.2.1 (fecha interna 2026-11-10): `"voz_oficial": "es-MX-JorgeNeural", "voz_rate": "+7%", "voz_pitch": "-2Hz"`.
- `capcot-capsulas-imaginantes/scripts/montar_capsula.py`: lee la voz del `storyboard.json`; defaults `rate +7%`, `pitch -2Hz`, `pad = 0.35` si modo continuo (aquí el pad difiere de la guía: 0.35 vs 0.3).
- `capcot-capsulas-imaginantes/scripts/dividir_lote.py` y `scripts/generar_guion_llm.py`: mismo bloque (`+7%`, `-2Hz`, `pad_seconds: 0.35`).

**Regla sin fallback (para modelos externos):** `docs/GUIA_MODELO_EXTERNO.md` §3: "Si en tu entorno no puedes usar edge-tts con JorgeNeural, **no montes el video**. Entrega SOLO storyboard + frames + fuentes y Grok Bot pone la voz. Prohibido sustituirla por eSpeak, gTTS, la voz del sistema u otra."

### 1.2 CAPCOT EN — Kokoro am_adam

- Voz: **Kokoro `am_adam`**. Cierre: **"That was Datos y ociosidades."**
- Evidencia: `capcot-capsulas-imaginantes/docs/CANAL_INGLES.md` (commit `68a74a80`, 2026-11-11): "Canal: **@datosyociosidadesEN**. Voz: Kokoro `am_adam`. Cierre: 'That was Datos y ociosidades.' Meta: 5 cápsulas/día (Marco 2026-11-10)".
- Flujo (mismo archivo, 2026-11-11): 1) Imaginantes manda ZIP semanal (frames limpios + storyboard + guion + `.srt` ES); 2) Pecas traduce guion y `.srt`; 3) Pecas genera la voz EN con Kokoro `am_adam`; 4) montaje MP4 EN (Pecas con capcot-montaje, o Imaginantes con el audio de Pecas); 5) subida a @datosyociosidadesEN. "No usar el MP4 en español como base: ya tiene voz y subtítulos quemados." / "La voz EN es Kokoro `am_adam`; no se usa otra voz sin decisión de Marco."
- Cierre confirmado en la práctica: `cola/entrada/2026-11-05_sinergia-algas/guion_en.txt` y `RELEVO_EN.md` de corales (2026-10-25), Juno (2026-10-29) y ADN sintético (2026-11-06).
- Speeds EN por cápsula, sin speed fija (fórmula en los relevos: necesaria = target − cortinilla − lead 0.3): corales 0.851, Juno 0.951, sinergia-algas 0.949, oxoboranos 1.05.

### 1.3 VoxCPM2 por tema (decisión Marco 2026-11-11)

`capcot-capsulas-imaginantes/docs/VOCES_POR_TEMA.md` (commit `4e422781`, 2026-11-12), "las cuatro voces":

| Voz | Origen | Descripción |
|---|---|---|
| JorgeNeural (es-MX) | edge-tts, vía Imaginantes | Voz oficial CAPCOT (+7%, −2 Hz) |
| narrador_es | VoxCPM2 Voice Design | Hombre es-MX cálido, curioso y pausado. **Seed 51**. F0 med 128 Hz (≈ em_santa, −1.0 sem) |
| narradora_es | VoxCPM2 Voice Design | Mujer es-MX cálida, curiosa, brillante. **Seed 52**. F0 med 291 Hz (mucho más aguda que ef_dora, +9.2 sem) |
| narrador_en | VoxCPM2 Voice Design | Hombre inglés americano estándar. **Seed 53**. F0 med 122 Hz (≈ am_adam, −0.6 sem) |

Mapa tema → voz (mismo archivo; confirmado en `docs/HORARIO_TEMAS_VOCES.md`): Historia/biografías → narrador_es; Ciencia/física/química/astronomía → JorgeNeural; Biología/cocina/hacks/cultura/literatura → narradora_es; canal EN (todos los temas) → narrador_en, alternando con Kokoro am_adam. Slot principal EN 18:00 CST.

Manifiesto en `microserie-heredera-voces/muestras_narradores.json`, workflow "VoxCPM2 CPU — Muestras de voz".

**Importante — VoxCPM2 asignado pero en la práctica no narra cápsulas completas:** ver §1.5 (mosquito) y §1.6 (ratas topo). El workflow solo genera líneas de muestra del manifiesto (no acepta texto arbitrario) y el modelo (~9.5 GB) no cabe en la VM (8 GB RAM, ~685 MB libres).

### 1.4 Microserie La heredera que vendieron — locks Kokoro

Locks **cerrados, no se regeneran ni se tocan** (regla de Marco 2026-11-10, citada en `microserie-heredera-sadtalker/assets/LEEME_ASSETS.md`).

| Personaje | Lock vigente |
|---|---|
| Elena | `ef_dora` speed **1.0** |
| Adrián | `em_santa` speed **1.0** |
| Camila | `ef_dora` speed **1.05** |
| Carmen | `ef_dora` speed **0.9** |
| Don Emilio | `em_alex` speed **0.95** (solo en `microserie-heredera-voces/muestras.json`; no tiene clip en el episodio 1) |

Evidencia: `microserie-heredera-sadtalker/manifiesto_clips.json` (`"voces_lock"`), `microserie-heredera-sadtalker/README.md`, `microserie-heredera-sadtalker/assets/LEEME_ASSETS.md`, `microserie-heredera-voces/muestras.json` (HEAD voces `60812753750456a5e67ce76b6400ea716be8b60c`; HEAD sadtalker `49f06ee3f26463d1b8407e62b2ebccf824bc4670`). Sin contradicciones entre esas fuentes.

- Episodio 1 "La boda que no fue", 90 s, 25 clips SadTalker solo CPU en Actions: `manifiesto_clips.json`, parámetros `cpu:true, preprocess:"full", size:256, still:true, expression_scale:0.8, batch_size:1, enhancer:null`; 18 clips `sync` y 7 `vo`; audio total 45.46 s; 25 wavs ~2.1 MB; fotos lock 1600×1600.
- Prueba prevista `max_clips: 2` (escenas 02 Camila sync y 03 Elena vo, ~10–20 min); completa `max_clips: 0` (25 clips, ~2.5–4.5 h, límite 360 min; artifacts caducan a 7 días).
- **Estado real no verificado:** no hay reporte/log/artifact leído que confirme la prueba de 2 clips ni la "corrida #3" que el README de voces pone como compuerta. El conector no lista runs de Actions; la lectura de `storyboard.json` e issues cayó en el 429. No se puede afirmar que el episodio 1 esté generado.

#### Muestras VoxCPM2 (microserie)

`microserie-heredera-voces/muestras.json` — propósito: "SOLO muestras para que Marco las escuche y apruebe; NO cambian ningun lock de voz". Modelo `openbmb/VoxCPM2`, `cfg_value: 2.0`, `device: cpu`, `inference_timesteps: 10`, `load_denoiser: false`, `optimize: false`, `sample_rate_hz: 48000`, licencia Apache-2.0.

| Personaje | Edad | Seed | Línea |
|---|---|---|---|
| Camila Mendoza | 26 | 42 | "La novia soy yo, por si se te olvida." |
| Carmen Mendoza | 55 | 43 | "Elena, no hagas escandalo." |
| Don Emilio | 65 | 44 | "Es autentico. Es el testamento de tu abuelo." |

Estado (README de voces, a 2026-11-10): script y workflow en GitHub (`.github/workflows/voxcp2-cpu.yml`, `scripts/generar_muestras.py`, `muestras.json`); **no hay evidencia de corrida VoxCPM2 ni de WAV generado/escuchado**. "No se debe disparar el workflow hasta confirmar que la corrida #3 de SadTalker quedó resuelta." Veredicto del README: VoxCPM-0.5B y 1.5 **NO sirven** (sin Voice Design, solo zh/en); **solo VoxCPM2 (2B)** sirve; CPU en principio sí, pero **NO_VERIFICADO en ejecución**; estimado 15–30 min (hasta ~60), timeout 120 min.

Además, `microserie-heredera-voces/muestras_narradores.json` (serie Datos y ociosidades, NO heredera): Narrador ES seed 51, Narradora ES seed 52, Narrador EN seed 53; "alternativa gratis a JorgeNeural y a las 3 voces Kokoro en español" / "alternativa gratis a ef_dora" / "alternativa gratis a Kokoro am_adam". "NO cambian ningun lock de voz ni la voz oficial JorgeNeural".

### 1.5 Viral animado — "El mosquito que escucha" (18-nov)

**Discrepancia asignado vs montado:**

- Asignado: `capcot-capsulas-imaginantes/docs/COCINA_CAPCOT.md` (commit `08acdf9d`, 2026-11-14): "mié 18-nov | El mosquito que escucha (`2026-10-28_mosquito-fruitless-audicion`) | **Pecas — viral animado de la semana** | narradora_es (VoxCPM2 seed 52) | Pendiente".
- Realidad: `cola/entrada/2026-10-28_mosquito-fruitless-audicion/RELEVO.md` (commit `e888b931`, 2026-11-15) dice **MONTADO** el 2026-11-15, 87.30 s, QA PASA; COCINA sigue diciendo "Pendiente" (desactualizado).
- **Voz real usada: Kokoro `em_santa`, speed 0.9, español es-MX** — no narradora_es. Desviación declarada en el RELEVO: "la voz asignada por `docs/VOCES_POR_TEMA.md` era narradora_es (VoxCPM2, seed 52). VoxCPM2 NO está disponible para narrar: el workflow `VoxCPM2 CPU — Muestras de voz` solo genera las líneas de muestra del manifiesto (no acepta texto arbitrario) y el modelo (~9.5 GB) no cabe en la VM (8 GB RAM, ~685 MB libres). Respaldo autorizado aplicado: Kokoro em_santa (voz de relevo de Pecas, aprobada por Marco en Mpemba v2)." Speed 0.9 en vez de 0.85 porque con 0.85 quedaba en 91.3 s y la puerta dura es 85 ± 5 s. Cierre: "Esto fue Datos y ociosidades."
- **Hora:** el repo dice **13:30 CST** en todas partes (RELEVO slot; `programacion.json`: "programado 18-nov 13:30 CST, yt_id -fDL2pBjH30"; `data/publicaciones.json` igual). **No se encontró ningún "10:00" para el mosquito en el repo.**

### 1.6 Otras voces Kokoro en uso real (relevos de Pecas)

- **Kokoro `em_santa`** — voz de relevo de Pecas. `docs/LINEA_EDITORIAL_VISUAL.json`: `"voz_fallback": "Kokoro em_santa speed 0.85 (local, relevo; Piper PROHIBIDA)"`. Usada en mosquito (speed 0.9) y en `cola/entrada/2026-11-07_comida-hielo-caliente/RELEVO_V2_APROBADO.md` (speed 0.85, aprobada por Marco 2026-11-09 ~14:12 "Me agrada"; la versión oficial Imaginantes/JorgeNeural es la que publica).
- **Kokoro `ef_dora` = narradora_es (mapeo local):** `capcot-capsulas-imaginantes/proyectos/2026-11-16_sarampion/QA_REPORTE.md`: "Voz: Kokoro ef_dora (narradora_es), speed 0.73 — 133.4 palabras/min (rango 120–140 para público 65+)", 94.27 s. Inconsistencia interna en ese proyecto: el `storyboard.json` trae `"speed": 0.9` en el bloque de voz, mientras build/QA usan 0.73.
- **Ojo, mismo `em_santa` con speed distinta según contexto:** `agente-cero-costo/guardian/guardian.py`: "Voz local actual: em_santa speed 0.85 (Marco aprobó en Mpemba v2 2026-11-09; em_alex rechazada)" — CAPCOT/Mpemba 0.85 vs Adrián en heredera 1.0. Son contextos distintos, no es un error, pero no se deben mezclar.
- Caso análogo al mosquito: `cola/entrada/2026-11-11_dato-ratas-topo-damaraland/RELEVO.md` dice voz "VoxCPM2 narradora_es (seed 52)", pero su `programacion.json` aclara: "Voz es-MX-JorgeNeural (sustituye VoxCPM2/narradora_es del paquete por regla fija de Mj)".
- `capcot-capsulas-imaginantes/docs/VOCES_POR_TEMA.md` también registra F0 medidas de los narradores VoxCPM2 (ver §1.3).

## 2. Contradicciones / versiones viejas que ya no valen

1. **Plantilla con +4% y fallback Chirp3 — VIEJA.** `capcot-capsulas-imaginantes/templates/storyboard_vertical.template.json`: `"voice": {"engine": "edge-tts", "voice_id": "es-MX-JorgeNeural", "rate": "+4%", "pitch": "-2Hz", "pad_seconds": 0.5, "fallback": {"engine": "google-chirp3-hd", "voice_id": "es-US-Chirp3-HD-Charon"}}`. Rate +4% (no +7%), pad 0.5 (no 0.3/0.35) y fallback Chirp3-Charon — único sitio donde aparece Chirp3 en todo el repo (1 resultado). Su comentario dice ser "fuente de verdad: docs/PLAN_MAESTRO_AUTOMATICO.md". La guía vigente y `narrate.py` dicen +7% y prohíben sustituir la voz.
2. **Piper: prohibida en lo vigente, fallback en lo viejo.** Vigente — `docs/LINEA_EDITORIAL_VISUAL.json` (2026-11-10): "La voz es la oficial (es-MX-JorgeNeural) o el fallback Kokoro em_santa speed 0.85 (relevo). Piper está prohibida (puerta dura de QA). No se usa otra voz." Viejo — `tools/tts/README.md` y `tools/tts/narrate.py` (commit `eb50a155`, 2026-11-08): "Si edge-tts falla… usa el fallback offline: `python tools/tts/narrate_piper.py …`", modelo `es_MX-ald-medium`; `generar_linea_editorial.py` (2026-11-08, `dae34217`) también fija `"voz_fallback": "es_MX-ald-medium (Piper, offline)"`. Los QA recientes lo confirman como rechazada: mosquito y sarampión dicen "no es voz rechazada (Piper)".
3. **Validadores con rangos de duración distintos (y ninguno valida la voz).**
   - `scripts/validar_storyboard.py`: duración planificada **60–95 s**; no valida voz (ni `voice_id`, rate ni pitch).
   - `scripts/qa_capsula.py`: `ok("duracion_>=60_<=120", 60 <= d <= 120, ...)` — **permite hasta 120 s**; tampoco valida la voz (solo `voz_<=240_palabras` y huecos de voz ≤0.9 s).
   - Documento viejo `avances/2026-10-24_GrokBot_plan_maestro.md`: validador descrito como "60–90 s". Docs vigentes dicen 60–95 s, objetivo 75–90.
4. **Demo-001 — voces descartadas, no usar.** `capcot-capsulas-imaginantes/proyectos/demo-001/NOTAS_v2.md` (2026-10-24): "Elegida: edge-tts es-MX-DaliaNeural, rate +4%, pitch -1 Hz"; "es-MX-JorgeNeural (v1): la que sonaba robótica; descartada" (previo al cambio a JorgeNeural oficial). Su `storyboard.json` trae DaliaNeural +4% / −1 Hz y fallback Piper `es_MX-claude-high`. También menciona `es-ES-AlvaroNeural`, `en-US-AndrewMultilingualNeural`, eSpeak (usado por error en Ideonella 2026-10-24, anti-ejemplo en la guía) y Coqui XTTS v2 (no evaluado, licencia CPML no comercial).
5. **`tools/tts/README.md` sugiere `es-MX-DaliaNeural` como ejemplo** de cambio de voz — solo ejemplo de argumento, pero es la voz descartada de demo-001.
6. **Imprecisión menor en `microserie-heredera-voces/muestras.json`:** `"proposito"` dice "para los 3 personajes que hoy comparten voz Kokoro", pero Don Emilio usa `em_alex` 0.95 "compartida con nadie mas"; solo Camila y Carmen comparten `ef_dora` con Elena.
7. **Discrepancia sin resolver (por el 429):** `search_repositories` reporta `open_issues_count: 1` en cada repo de la microserie, pero `list_issues` en voces devolvió `{"issues":[],"totalCount":0}`; el de sadtalker no respondió. No se pudo confirmar qué issue es ni su contenido.
8. **Pad 0.3 vs 0.35:** guía dice 0.3; `montar_capsula.py`, `dividir_lote.py` y `generar_guion_llm.py` usan 0.35 por defecto.
9. **Sarampión speed 0.9 vs 0.73:** ver §1.6.

## 3. Herramientas / skills / scripts de búsqueda y coordinación

### 3.0 Herramientas de búsqueda — corrección 2026-11-16

> **Corrección a la revisión anterior:** la primera versión de esta sección decía que no había evidencia de ninguna herramienta de búsqueda difusa/fonética en los repos. Eso estaba mal: no se había leído `docs/CODEBASE_MEMORY_MCP.md` ni `docs/MAPA_HERRAMIENTAS_POR_PROYECTO.md`, y las búsquedas de `difflib` / `fuzzy` habían caído en el 429. Esta corrección se hizo solo lectura, llamada por llamada (pausas de ~8 s entre llamadas, sin reintentos en caliente), y **sin subir nada a GitHub en esta pasada** — el informe queda listo para subir.

#### 3.0.1 Tabla — qué herramienta de búsqueda existe, dónde y para qué

| Herramienta | Dónde está | Qué busca / cómo se usa | Estado real |
|---|---|---|---|
| **codebase-memory-mcp** (servidor MCP local, grafo de conocimiento en SQLite) | `capcot-capsulas-imaginantes/docs/CODEBASE_MEMORY_MCP.md` y `motor-u6-storage/docs/CODEBASE_MEMORY_MCP.md`; `.mcp.json` en la raíz de ambos | Buscar símbolos (`search_graph`), seguir llamadas (`trace_path`), buscar texto literal (`search_code`), leer fragmento de un símbolo (`get_code_snippet`), esquema de archivo (`get_file_outline`), vista general (`get_architecture`), Cypher solo lectura (`query_graph`), listar proyectos (`list_projects`); indexar con `index_repository`, ver estado con `index_status` | **Documentado, pero NO instalado ni vivo en esta máquina** (ver 3.0.2) |
| **GitHub `search_code` del conector** | Conector GitHub de Muse (no es un archivo del repo) | Búsqueda por texto exacto / símbolos en los 11 repos (`user:marcojpad-hash`), con `repo:`, `path:`, `filename:`, `language:` | **Es la herramienta que sí se usó en esta revisión**; es literal, no difusa: no entiende sonido ni typos |
| **`difflib.SequenceMatcher` en `qa_capsula.py`** | `capcot-capsulas-imaginantes/scripts/qa_capsula.py` | Compara guion vs subtítulos (SRT) palabra por palabra normalizada (`_norm_w`, minúsculas, sin acentos/puntuación) y exige cobertura ≥99% (`subs_cobertura_>=99%`, `SequenceMatcher(None, _guion, _subs, autojunk=False).get_matching_blocks()`) | **Existe y es la única coincidencia difusa real en código** (1 hit en toda la org). Pero es QA de subtítulos, no una herramienta general de búsqueda |
| **Regla "glob / fuzzy simple" del Motor U6** | `motor-u6-storage/motor/motor/protocolo_kernel_motor.py` y `motor/motor/control_flujo_soluciones.py` | Ante ruta con typo o letra de menos: "Listar el directorio padre y tomar el match más cercano (glob / fuzzy simple)", "Probar alias conocidos (sidecar_* ↔ control_*, catalogo ↔ catálogo)", "Si hay 1 candidato claro: usarlo y anotar la corrección". Y prohibido: "Detenerse por typo/letra en ruta sin glob/fuzzy" | **Regla documentada, no librería ni script**: no hay código que la ejecute, es una instrucción para el modelo |
| **`memoria-compartida/INDICE.md`** | `memoria-compartida/INDICE.md` | Índice manual de lectura: protocolo obligatorio, política de privacidad, y una línea por tema (`hechos/proyectos.md`, `decisiones.md`, `correcciones.md`, `tokens.md`, `estado.md`, `personas.md`); "Lee solo los archivos que tu tarea necesita" | **Es un índice de lectura, no una herramienta de búsqueda**: no busca, solo dice qué leer primero |
| **Búsqueda de tendencias / fuentes** | `capcot-capsulas-imaginantes/scripts/tendencias.py`, `tendencias_estilos.py`, `metricas.py` (listado de `scripts/`) | Tendencias y métricas de cápsulas (por nombre de archivo; no se leyó su contenido en esta corrección) | No es búsqueda por patrones en el repo; se anota por listado, sin afirmar su contenido |
| **Bus / `recibir.py`** | `agente-cero-costo/conector/recibir.py` (confirmado en listado de `conector/`, junto a `bus_core.py`, `emitir.py`, `publicar.py`, `aplicar.py`, `puente_mcp.py`) | Recibir órdenes del bus (par de `emitir.py`); no es búsqueda | **Existencia confirmada en esta corrección** (antes quedaba sin verificar) |

#### 3.0.2 codebase-memory-mcp — lo que dice el repo y lo que hay de verdad en esta máquina

Es la herramienta de búsqueda que faltaba en la primera revisión, y la más importante:

- **Qué es:** servidor MCP local en un solo binario en C (DeusData/codebase-memory-mcp, MIT). Indexa un repo en un grafo persistente (SQLite) y responde consultas estructurales sin releer todos los archivos: buscar símbolos, seguir llamadas, leer fragmentos, ver arquitectura.
- **Versión documentada:** **0.12.1** (release 16-oct-2026), binario verificado con SHA-256.
- **Índices documentados (7-nov-2026):** CAPCOT **12 129 nodos / 13 879 aristas** (556 archivos, 13 s, solo `.git` fuera); Motor U6 **13 531 nodos / 27 173 aristas** (según `MAPA_HERRAMIENTAS_POR_PROYECTO.md`).
- **Dónde está configurado:** `.mcp.json` en la raíz de CAPCOT/main y de U6 (también en `alterno/cameo-pesos` según el mapa del 15-nov). **NO está en la rama activa de CAPCOT** (`feature/capcot-video-discovery-continuity`): ahí `docs/CODEBASE_MEMORY_MCP.md` y `.mcp.json` devuelven 404. Los índices son foto del 7-nov y hay que reindexar cuando el repo cambia.
- **Cómo se usa (según el doc):** binario en `~/workspace/codebase-memory-mcp/bin/codebase-memory-mcp`; cliente en `~/workspace/custom-connectors/custom.codebase-memory-mcp/bin/client.py`; índice en `~/.cache/codebase-memory-mcp/` (un `.db` por proyecto). Ejemplo verificado en el doc: `search_graph` con `{"project": "capcot-capsulas-imaginantes", "query": "procesar_cola", "limit": 5}` devuelve `scripts.procesar_cola.cola`, `.guardar`, `.upd`.
- **Caveat del propio doc:** pre-1.0, 560 issues abiertos a 7-nov; su paper reporta 83% de calidad frente a 92% de exploración manual, a cambio de ~10× menos tokens. "Verifica siempre en el archivo fuente lo que el grafo afirme, sobre todo antes de cambiar código."
- **Estado real en esta máquina (verificado 2026-11-16 con `find`/`ls`):** **NO está instalado aquí.** `~/workspace/codebase-memory-mcp/bin/` no existe, `~/workspace/custom-connectors/custom.codebase-memory-mcp/bin/client.py` no existe, `~/.cache/codebase-memory-mcp/` no existe y `~/workspace/cbm-repos/` no existe. El mapa del 15-nov ya lo advertía: "Esta sesión no expone herramientas MCP de codebase-memory ni acceso al índice local" y "la configuración local no equivale a conexión viva". **Conclusión: la herramienta existe en los repos como documentación/configuración, pero Pecas no la tiene disponible en este workspace; hay que instalarla/reindexarla antes de usarla, no darla por usada.**

#### 3.0.3 Lo que NO existe — verificado con 0 hits (una llamada por término)

- `fuzzywuzzy` / `rapidfuzz` / `Levenshtein`: **0 resultados** en los 11 repos.
- `soundex` / `fonética` / `fonetica`: **0 resultados**.
- `"patrones similares"`: **0 resultados**. `"palabra exacta"`: **0 resultados**. `"búsqueda difusa"` / `"busqueda difusa"`: **0 resultados**.
- `ripgrep` / `rg`: **0 resultados**. Archivo `filename:buscar`: **0 resultados**.
- `grep`: 14 hits, pero son menciones en docs (`tools/tts/README.md`, `CONTRATO_TRABAJO_MULTI_MODELO.md`, `conector/ESTADO.md`, `DELEGACIONES.md`, etc.), no un script de búsqueda con grep.
- `filename:search`: 1 hit, `motor-u6-storage/motor/tests/test_mc_required_search_provenance.py` — es un test de procedencia de búsqueda del motor, no una herramienta de búsqueda para Pecas (no se leyó su contenido en esta corrección).
- No hay ningún script de búsqueda en `capcot-capsulas-imaginantes/scripts/` (listado completo: 25 archivos; ninguno se llama buscar/search; los más cercanos son `tendencias.py` y `metricas.py`) ni en `capcot-capsulas-imaginantes/tools/` (solo `orquestador/` y `tts/`).
- **La regla "buscar por patrones similares (sonido, sentido, función), no fiarse de la palabra exacta" sigue sin aparecer en los repos con ninguna de esas frases.** Lo más cercano que sí existe es la regla U6 de glob/fuzzy simple ante typos en rutas (§3.0.1) y el `SequenceMatcher` de QA de subtítulos. Si esa regla vive en algún lado, no está en GitHub con ese texto: vive en la conversación con Marco / en las skills locales (que tampoco están, ver 3.0.4).

#### 3.0.4 Skills locales — tampoco están en este workspace

- El repo cita `~/workspace/custom-skills/capcot-guion/SKILL.md` ("Escribe storyboard.json con fuentes, escenas y narración") y `~/workspace/custom-skills/capcot-frames/SKILL.md` ("Genera las imágenes de cada escena") en `capcot-capsulas-imaginantes/generar_linea_editorial.py`.
- **Verificado 2026-11-16:** `~/workspace/custom-skills/` está **vacío** y `~/workspace/custom-connectors/` está **vacío**. No existe `capcot-guion/SKILL.md` ni `capcot-frames/SKILL.md` en esta máquina, así que no se pudo revisar qué herramientas de búsqueda usan. Eso también explica por qué la primera revisión no encontró skills: no es solo que no estén en GitHub, es que tampoco están en el workspace local.
- `SKILL.md` en GitHub: 7 hits en la primera revisión, ninguno es un archivo de skill propio (se mantiene).

#### 3.0.5 Veredicto para Marco

1. **Sí hay herramientas de búsqueda, y la principal es codebase-memory-mcp** — pero está documentada, no instalada ni viva aquí, y no está en la rama activa de CAPCOT. Hay que instalar el binario, reindexar CAPCOT y U6, y decidir si se integra en la rama feature.
2. **La única coincidencia difusa real en código es `difflib` en `qa_capsula.py`** (cobertura guion vs subtítulos ≥99%), más la regla U6 de glob/fuzzy ante typos. No hay librería fuzzy, ni fonética, ni soundex, ni script `buscar`.
3. **La regla de "patrones similares" no está escrita en los repos.** Si hay que mantenerla, hay que escribirla (en `memoria-compartida` o en una skill) en vez de suponer que ya está.
4. **Las skills `capcot-guion` / `capcot-frames` citadas en el repo no existen en este workspace.** Hay que recuperarlas o reescribirlas antes de contar con ellas.

### 3.1 Skills — no hay skills dentro de los repos; las referencias apuntan fuera

Búsqueda `SKILL.md user:marcojpad-hash`: **7 hits, ninguno es un archivo `SKILL.md` dentro de un repo**.

- `capcot-capsulas-imaginantes/generar_linea_editorial.py` — referencia skills **locales, fuera de GitHub**, en `~/workspace/custom-skills/`:
  - `"id": "capcot-guion", "archivo": "~/workspace/custom-skills/capcot-guion/SKILL.md", "hace": "Escribe storyboard.json con fuentes, escenas y narración."`
  - `"id": "capcot-frames", "archivo": "~/workspace/custom-skills/capcot-frames/SKILL.md", "hace": "Genera las imágenes de cada escena con el prompt_base del estilo elegido."`
- `capcot-capsulas-imaginantes/docs/CAPCUT_CODEX_INTEGRACION.md` — `SKILL.md` **oficial externo de CapCut** (`https://sf16-sg.tiktokcdn.com/.../capcut_codex_plugin/SKILL.md`), con instrucción de seguirlo literalmente y no sustituirlo por un MCP de terceros.
- `agente-cero-costo/guardian/README.md` — menciona `capcot-frames/SKILL.md` solo como documento corregido (G4): decía de explainroo "NO instalado, NO probado"; se probó 2026-11-09 y no se adopta; candidato actual Nano Banana por la app de Gemini (probado 2026-11-10).

**Conclusión:** en los repos no se encontró ningún `SKILL.md` propio ni directorio de skills; las skills citadas viven en el workspace local (`~/workspace/custom-skills/`), no versionadas en estos 11 repos según lo buscado.

### 3.2 Búsqueda por patrones similares — corregido en §3.0

- `"patrones similares" user:marcojpad-hash`: **0 resultados**.
- `"palabra exacta" user:marcojpad-hash`: **0 resultados**.

**Corrección 2026-11-16 (ver §3.0, que sustituye lo que seguía en este apartado):** la regla literal de "buscar por patrones similares (sonido, sentido, función)" sigue sin aparecer con esas frases, pero **sí hay herramientas de búsqueda que la primera revisión no vio**: `codebase-memory-mcp` (grafo de búsqueda, documentado en CAPCOT y U6, no instalado en esta máquina), `difflib.SequenceMatcher` en `scripts/qa_capsula.py` (cobertura guion vs subtítulos ≥99%, único hit difuso en código) y la regla U6 de "glob / fuzzy simple" ante typos en rutas. Lo que antes decía "no hay evidencia de una herramienta de búsqueda difusa/fonética" queda corregido por §3.0.1–3.0.3: hay herramienta estructural (codebase-memory) y coincidencia difusa en QA, pero **no hay** librería fuzzy/fonética ni script general de búsqueda por patrones, y la regla como frase no está en los repos.

### 3.3 Bus / conector — vigente en agente-cero-costo

- `bus_core`: 3 hits, todos en `agente-cero-costo`:
  - `conector/puente_mcp.py` — `from bus_core import Bus` y `bus=Bus()` (puente MCP sobre el bus).
  - `tests/test_unified_bus.py` — carga `conector/bus_core.py` como módulo y lo prueba (`UnifiedBusTests`).
  - `.github/workflows/unified-agent-bus.yml` — se dispara con cambios en `conector/bus_core.py` y `conector/puente_mcp.py`.
- `emitir`: 39 hits, en `agente-cero-costo/conector/`:
  - `conector/emitir.py` — "Emitir: el enchufe (macho) del conector… El par es reversible: cualquier modelo puede emitir y cualquier modelo puede recibir. El que emite hoy puede recibir mañana, y viceversa."
  - `conector/emitir-bloque.md` — alternativa por Issue: título `[BUS] tipo - nombre-del-modelo`, mensaje en el cuerpo; "Si tu aplicación solo tiene lectura, usa el bloque [EMITIR] como alternativa y solicita que el propietario lo aplique."
- `publicar.py`: 40 hits. **Dos `publicar.py` distintos, no confundir:**
  - `agente-cero-costo/conector/publicar.py` — del bus: toma el bloque `[EMITIR]` que el modelo produce y el usuario pega; "aplicar.py lo escribe en el bus… Se corre solo cada vez que hay una actualización (avisar.py y emitir.py ya lo llaman)."
  - `capcot-capsulas-imaginantes/scripts/publicar.py` — publicación de video: YT con `CAPCOT_YT_CLIENT_SECRETS / CAPCOT_YT_TOKEN` ("NUNCA commitear ni imprimir esos archivos"), verificación solo lectura `--verificar-yt`; TikTok "DESACTIVADO por defecto (no hay cuenta nueva…)", solo con `--habilitar-tiktok`.
- `recibir.py` — **existencia confirmada en la corrección 2026-11-16**: `agente-cero-costo/conector/recibir.py` aparece en el listado del directorio `conector/` (junto a `bus_core.py`, `emitir.py`, `publicar.py`, `aplicar.py`, `puente_mcp.py`). Es el par receptor de `emitir.py`; no es una herramienta de búsqueda.

### 3.4 Coordinación entre modelos — CAPCOT

- `PROTOCOLO_CALLBACK`: 9 hits. Archivo canónico: `capcot-capsulas-imaginantes/ajustes_entre_modelos/PROTOCOLO_CALLBACK.md`, resumido en `agente-cero-costo/guardian/README.md`: "Regla 1: delegar sin escribirla en DELEGACIONES.md es no delegar. Regla 3: HECHA con evidencia (commit, enlace, archivo); sin evidencia no está hecha. Regla 4: si el receptor no puede, marca BLOQUEADA con el motivo. Regla 5: más de un día en PENDIENTE → Pecas lo reporta (de aquí sale el umbral de 24 h). El aviso es el workflow `callback-aviso.yml` (Issue con etiqueta `callback`); el tablero por sí solo no despierta a nadie. Pecas es el router."
- `capcot-capsulas-imaginantes/ajustes_entre_modelos/COORDINACION_CHATGPT_IMAGINANTES.md` — "Regla de oro: no inventar datos, fuentes ni DOIs"; entrega en `cola/entrada/<id>/` (storyboard, frames 9:16, `fuentes.md`, `ESTADO_EJECUCION.md`); "solo texto en commits; no subir mp4/token"; prohibido otra serie, otra voz, publicar, inventar DOIs, editar `data/*.json`, tocar el motor U6; máx 3/día, 6 slots, Imaginantes decide; cadena: `procesar_cola.py` → `montar_capsula.py` (JorgeNeural) → `qa_capsula.py` (obligatoria) → `publicar.py`.
- `qa_capsula`: 30 hits. `capcot-capsulas-imaginantes/scripts/qa_capsula.py` — "Compuertas automáticas (PLAN_MAESTRO §5) sobre un MP4 renderizado + su storyboard. Uso: `python3 scripts/qa_capsula.py salida.mp4 storyboard.json` -> escribe `qa.json` junto al mp4; código 0 si pasa." Usa `ffprobe` (`-show_streams`, `-show_format`).
- `capcot-capsulas-imaginantes/docs/GUIA_MODELO_EXTERNO.md` — "Grok Bot corre `procesar_cola.py` → `capsula_diaria.py --origen externa` → `qa_capsula.py`" y advierte que un "QA propio no oficial («16/16»)" no cuenta: "Solo cuenta `scripts/qa_capsula.py` corrido por Grok Bot."
- `orquestador-central/docs/PROMPT_MUSE_VIDEO.md` — también cita `qa_capsula.py` como parte del pipeline CAPCOT.

### 3.5 Contradicciones viejas vs vigentes en coordinación

- Webhook de Grok **abandonado**, bus por Issues vigente. `capcot-capsulas-imaginantes/salidas/_ops/2026-11-09_hook_pedidos_grok.md`: "Un pedido entra al bus creando un Issue `[BUS] indicacion - <emisor>` con `para: grok` en el cuerpo. El workflow `github-native-agent-bus.yml` lo convierte en `conector/bus/gh-issue-N.json`." / "El webhook Firebase (`capcot.package.ready`) y los secretos `GROK_WEBHOOK_URL` / `GROK_WEBHOOK_TOKEN` están abandonados (`gh secret list` vacío)." / "[el workflow viejo] dispara solo con `cola/entrada/*.json`, y los paquetes reales son carpetas; todas las corridas del 1-nov fallaron con `Falta configurar GROK_WEBHOOK_URL`."
- `agente-cero-costo/guardian/README.md` (G5): "`PROTOCOLO_CALLBACK.md` dice que `callback-aviso.yml` está 'listo para subirlo por navegador con la cuenta de Marco' (regla vieja). La vía es delegar la subida a Copilot/Codex por el bus."
- `PLAN_MAESTRO_AUTOMATICO.md` de CAPCOT (citado en el mismo `guardian/README.md`): "Mj no necesita estar presente, la revisión humana es opcional"; "fallo en una compuerta → reintento máx. 2 → FALLIDO y cápsula de reserva del backlog"; compuertas: "fuentes con DOI que resuelve, duración 60–90 s, 1080×1920 30 fps, −14 LUFS ±1".

### 3.6 Los 11 repos confirmados

| Repo | Privado | Descripción registrada |
|---|---|---|
| `microserie-heredera-sadtalker` | No | Pipeline de video episodio 1 con SadTalker en CPU |
| `baterias-memoria` | No | Batería de memoria para el stack agente costo cero |
| `ChatGPT-migracion` | No | Migración y continuidad de ChatGPT, independiente del motor y de CAPCOT |
| `orquestador-central` | No | Orquestador central: núcleo, memoria compartida, registro de órdenes, enrutador de agentes |
| `capcot-capsulas-imaginantes` | No | CAPCOT — cápsulas de imaginantes |
| `microserie-heredera-voces` | No | Voces VoxCPM2 para La heredera |
| `baterias-tokens` | No | Batería de tokens / proveedores gratuitos |
| `motor-u6-storage` | No | (sin descripción) |
| `memoria-compartida` | No | Memoria compartida: hechos verificados, decisiones y correcciones |
| `agente-cero-costo` | No | Stack agente costo cero: DeepSeek Harness + gpt-oss por Groq, TwIL-8B local + puente local |
| `red-teaming-safety-u6` | **Sí** | Red-teaming white-hat / homeostasis U6 |

Sobre `red-teaming-safety-u6`: aparece como privado, pero ninguna búsqueda completada devolvió hits en él; no se verificó por separado qué permite leer el conector dentro de ese repo.

## 4. No verificado / pendiente (por el 429)

- `list_commits` de los repos de la microserie (fechas/autores por archivo) y `list_issues` de sadtalker.
- Lectura de `microserie-heredera-sadtalker/storyboard.json`, `scripts/generar_muestras.py` y workflows completos.
- Búsqueda `"La heredera" org:marcojpad-hash`, `em_santa` / `VoxCPM2` en toda la org.
- Estado real de las corridas de Actions (prueba 2 clips SadTalker y corrida #3): no hay herramienta de lectura para ello en el conector; habría que verificarlo en la web de GitHub.
- `ChatGPT-migracion` — `ABRAZO_CHIQUITO`: 2 hits en `ChatGPT-migracion/README.md`, fragmento truncado, archivo no leído; contenido no citable. `HISTORIAL_DE_INTERACCION_Y_CALIBRACION`: búsqueda fuera del recorte entregado, no verificado.
- `memoria-compartida` — `INDICE.md` **verificado en la corrección 2026-11-16**: índice manual de lectura (protocolo, privacidad, hechos por tema), no herramienta de búsqueda (ver §3.0.1). Protocolo e índice ya no quedan pendientes por el 429.
- Reglas de búsqueda por voz a texto / patrones similares con otra redacción, `difflib`/fuzzy, scripts genéricos de búsqueda/grep, `orquestador-central` en detalle, `motor-u6-storage`, `baterias-*`, microseries y `red-teaming-safety-u6` por dentro: **difflib, fuzzy, grep, INDICE y `recibir.py` quedaron verificados en la corrección 2026-11-16 (§3.0)**. Siguen sin verificar: `orquestador-central` en detalle, `motor-u6-storage` y `baterias-*` por dentro, microseries por dentro y `red-teaming-safety-u6` por dentro. No se afirma que no existan; se afirma que esta revisión no los encontró.
- `docs/RECETA_CAPSULA.md` (CAPCOT): la búsqueda con filtro de ruta no devolvió resultados; no se afirma qué dice sobre voz.
- No se listaron directorios raíz ni se leyó ningún archivo completo; la evidencia es de fragmentos de `search_code` / `get_file_contents` puntuales.

## 5. Resumen ejecutivo

- **Vigente ES:** es-MX-JorgeNeural, edge-tts, **+7%, −2 Hz, pad 0.3 (0.35 en el montador)**, sin sustitución para externos; fallback de relevo **Kokoro em_santa speed 0.85** (Piper prohibida).
- **Vigente EN:** Kokoro **am_adam**, cierre "That was Datos y ociosidades.", flujo ZIP semanal → traducción → voz → montaje; speeds por cápsula (0.851–1.05).
- **VoxCPM2 (narrador_es 51 / narradora_es 52 / narrador_en 53):** asignado por tema en `VOCES_POR_TEMA.md` (2026-11-12), pero **en la práctica no narra cápsulas completas** (modelo no cabe / workflow solo hace muestras); los relevos reales usan em_santa / ef_dora / JorgeNeural. El mosquito del 18-nov está montado con **em_santa 0.9**, programado **13:30 CST** (yt `-fDL2pBjH30`), no 10:00.
- **Heredera:** locks Kokoro cerrados — Elena ef_dora 1.0, Adrián em_santa 1.0, Camila ef_dora 1.05, Carmen ef_dora 0.9, Don Emilio em_alex 0.95 (solo muestras). Muestras VoxCPM2 seeds 42/43/44, sin evidencia de corrida ni WAV escuchado; solo VoxCPM2 (2B) sirve, CPU no verificado.
- **Corregir:** plantilla con +4%/Chirp3, docs TTS con fallback Piper, QA que permite 120 s frente a 60–95 s del validador/docs, COCINA que dice "Pendiente" el mosquito ya montado.
- **Skills:** no hay `SKILL.md` propio en los 11 repos; las skills citadas (`capcot-guion`, `capcot-frames`) viven en `~/workspace/custom-skills/`, fuera de GitHub — **y en la corrección 2026-11-16 se verificó que ese directorio está vacío en esta máquina: las skills tampoco están en el workspace local**.
- **Búsqueda (corregido 2026-11-16, ver §3.0):** la herramienta principal es **codebase-memory-mcp** (grafo de búsqueda, docs en CAPCOT y U6, índices 7-nov: CAPCOT 12 129 nodos, U6 13 531 nodos), pero **no está instalada ni viva en esta máquina** y no está en la rama activa de CAPCOT (feature, 404). La única coincidencia difusa real en código es **`difflib.SequenceMatcher` en `qa_capsula.py`** (subtítulos ≥99%), más la regla U6 de glob/fuzzy ante typos. **No hay** fuzzywuzzy/rapidfuzz/Levenshtein, soundex/fonética, ripgrep ni script `buscar`; la regla literal "patrones similares / no fiarse de la palabra exacta" **no aparece** en los repos con esas frases.
- **Bus:** vigente en `agente-cero-costo/conector/` (`bus_core.py`, `emitir.py`, `publicar.py` del bus, Issues `[BUS]`); webhook Grok abandonado.
