# Control de cola CAPCOT — 6 de noviembre de 2026

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Corte:** 2026-11-06 15:10:29 CDMX  
**Rol:** auditoría; no producción de cápsulas ni medios.

## 1. Resultado ejecutivo

- **12/12** storyboards canónicos del lote 5–7 nov existen en `proyectos/<project_id>/storyboard.json`.
- **4/4** proyectos del día actual (6-nov) están inventariados; no hay otros borradores del 6-nov en `proyectos/`.
- **0** JSON en `cola/entrada/`; solo existe `.gitkeep`.
- **2 PASS narrativos / 10 FAIL narrativos**. Los scores y checks siguientes fueron releídos desde los JSON de GitHub.
- **0/12** pasan la compuerta estructural. Los dos PASS narrativos tampoco pueden promoverse.
- **0 promociones**, **0 dispatches** y **0 recepciones Grok confirmadas**.
- Los doce estados `cola/estado/<project_id>.json` devolvieron 404: **RECEPCION_GROK_NO_CONFIRMADA**.
- No existe `salidas/<project_id>/` para ninguno de los doce; no hay IDs ni programación de plataforma asociados a estos proyectos.

## 2. Inventario de borradores

Los doce archivos se incorporaron al árbol en el commit de staging `7a415426f5907c2ab03687a47f3d160a595cb669`, fechado 2026-11-02 22:11:24 UTC (16:11:24 CDMX). El JSON no contiene `created_at`; la fecha de creación se obtiene del historial Git. El commit no basta para atribuir la autoría al investigador CAPCOT, por lo que no se hace esa atribución. Las últimas modificaciones de QA previas a este run fueron commits del 5-nov.

| project_id | Fecha objetivo | Slot CDMX | Cesta | Palabras | Escenas | narrative_qa |
|---|---|---:|---|---:|---:|---:|
| `2026-11-05_kids-dia-en-venus` | 2026-11-05 | 07:00 | kids | 170 | 7 | PASS 88 |
| `2026-11-05_comida-palomitas` | 2026-11-05 | 13:30 | comida_familia | 173 | 7 | FAIL 82 |
| `2026-11-05_inter-arboles-se-comunican` | 2026-11-05 | 17:00 | intermedio_1 | 169 | 8 | FAIL 78 |
| `2026-11-05_inter-rayo-globular` | 2026-11-05 | 17:45 | intermedio_2 | 197 | 7 | FAIL 81 |
| `2026-11-06_kids-ballena-azul-corazon` | 2026-11-06 | 07:00 | kids | 174 | 7 | FAIL 80 |
| `2026-11-06_comida-aguacate-negro` | 2026-11-06 | 13:30 | comida_familia | 170 | 7 | FAIL 79 |
| `2026-11-06_inter-ranas-congeladas` | 2026-11-06 | 17:00 | intermedio_1 | 177 | 7 | FAIL 83 |
| `2026-11-06_inter-arena-cantante` | 2026-11-06 | 17:45 | intermedio_2 | 206 | 7 | PASS 94 |
| `2026-11-07_kids-huesos-bebe` | 2026-11-07 | 07:00 | kids | 172 | 7 | FAIL 82 |
| `2026-11-07_comida-hielo-caliente` | 2026-11-07 | 13:30 | comida_familia | 172 | 7 | FAIL 81 |
| `2026-11-07_inter-pulpo-suenos` | 2026-11-07 | 17:00 | intermedio_1 | 170 | 7 | FAIL 80 |
| `2026-11-07_inter-nubes-pesan` | 2026-11-07 | 17:45 | intermedio_2 | 221 | 7 | FAIL 78 |

Los 12 pares `project_id / fecha_objetivo / slot_local / slot_cesta` coinciden con `data/horario_semana_2026-11-01_07.json`. La identidad de árboles es la correcta: el storyboard canónico trata redes micorrícicas comunes y Karst et al. 2023; no se marca desajuste temático. La variante de respiración nocturna está en bloqueados y es otro artefacto. El slot de nubes es exactamente `2026-11-07_inter-nubes-pesan` a las 17:45; `extra-nubes-pesan` es material de origen, no un segundo proyecto.

### Proyectos del día actual (6-nov)

Son exactamente cuatro: ballena azul, aguacate negro, ranas congeladas y arena cantante. Sus estados de proyecto son borradores en espera de auditoría; la parrilla conserva `pedir_chatgpt`. Ninguno está seleccionado, recibido por Grok, en producción, con QA audiovisual oficial ni publicado.

## 3. QA narrativo en frío

Se releyó únicamente la narración concatenada de cada storyboard, sin usar título, resumen, arco, notas ni `narrative_contract` para decidir el resultado. Los doce JSON fueron actualizados con `reviewed_at="2026-11-06T15:10:29-06:00"` y releídos desde GitHub. Todos conservan `review_basis="lectura_en_frio_solo_narracion"` y `reviewer_role="auditor_capcot_independiente"`.

| project_id (abreviado) | Score/status | Checks false | critical_flags |
|---|---:|---|---|
| 05 Venus | 88 PASS | ninguno; 7/7 true | `[]` |
| 05 palomitas | 82 FAIL | `apertura_in_medias_res`, `progresion_por_escena` | `APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`; `ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA` |
| 05 árboles | 78 FAIL | `apertura_in_medias_res` | `APERTURA_GENERICA_NO_IN_MEDIAS_RES` |
| 05 rayo globular | 81 FAIL | `apertura_in_medias_res` | `APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES` |
| 06 ballena | 80 FAIL | `payoff_cierre_apertura` | `PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE` |
| 06 aguacate | 79 FAIL | `progresion_por_escena`, `transiciones_causales` | `REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL` |
| 06 ranas | 83 FAIL | `progresion_por_escena`, `transiciones_causales` | `REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES` |
| 06 arena | 94 PASS | ninguno; 7/7 true | `[]` |
| 07 huesos | 82 FAIL | `progresion_por_escena`, `transiciones_causales` | `ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION` |
| 07 hielo caliente | 81 FAIL | `apertura_in_medias_res` | `APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES` |
| 07 pulpo | 80 FAIL | `progresion_por_escena`, `transiciones_causales`, `payoff_cierre_apertura` | `REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO` |
| 07 nubes | 78 FAIL | `progresion_por_escena`, `transiciones_causales`, `payoff_cierre_apertura` | `ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION` |

Los siete checks explícitos están presentes en los doce JSON: `pregunta_central_reconstruible`, `apertura_in_medias_res`, `progresion_por_escena`, `transiciones_causales`, `giro_cientifico_explicado`, `limite_evidencia_explicito` y `payoff_cierre_apertura`. PASS solo aparece en Venus y arena, ambos con score ≥85, siete checks true y flags vacíos. Los diez FAIL conservan sus flags y checks falsos.

## 4. Validación estructural estática

No se ejecutó `scripts/validar_storyboard.py` ni helpers: no había runtime local del repositorio. Se leyó el validador y se contrastaron estáticamente los doce JSON. Resultado: **0/12 estructuralmente aptos**.

| Criterio | Resultado |
|---|---|
| Escenas | 12/12 cumplen 7–9; árboles tiene 8 y los demás 7 |
| Palabras | 11/12 cumplen 170–235; árboles tiene 169 |
| Duración | 12/12: 78 s de escenas + cortinilla de 6 s = 84 s |
| Gancho | 12/12: 3–5 palabras, máximo permitido 6 |
| Arco y cierre hablado | 12/12 tienen los cuatro arcos en orden y contienen «Esto fue Datos y ociosidades.» |
| Voz | 12/12 declaran edge-tts, es-MX-JorgeNeural, es-MX, +7% y -2Hz |
| narrative_contract | 12/12 contienen pregunta central, promesa, stakes, giro científico, límite de evidencia y payoff |
| Campos narrativos por escena | 0/12 cumplen: faltan `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information` en todas las escenas (42 ausencias por storyboard de 7 escenas; 48 en árboles) |
| Mapa y dato/gráfico | 11/12 tienen ambas capas con fuente; árboles no tiene ninguna |
| Coordenadas | Las coordenadas numéricas presentes están dentro de rango; no se certificó la precisión geográfica real |
| Assets | Los doce tienen `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type`, `export.filename` ni rutas de medios |
| Publicación | Los doce mantienen `publicacion.status=PENDIENTE_DECISION_GROK` |

### Estilo, fuentes y audio

- Los doce `estilo_id` existen en el catálogo de 50 estilos y no se repite estilo dentro de cada día.
- Se corrigió mecánicamente el `visual_identity.prompt_base` de árboles y se antepuso el prompt base literal del catálogo a sus ocho `image_prompt`; tras releer, los doce storyboards cumplen la coincidencia de prefijo.
- Todos los `source_ids` usados por escenas están declarados. Ocho paquetes incluyen DOI y cuatro no consignan DOI en el JSON (Venus/NASA, aguacate/PMC, huesos/OpenStax y nubes/USGS). No se ejecutó resolución Crossref.
- Se corrigió `trend_source.url` de palomitas para que apunte a SRC-001 (Virot y Ponomarenko, DOI 10.1098/rsif.2014.1247) y de pulpos para que apunte a SRC-001 (Nature 2023, DOI 10.1038/s41586-023-06203-4). No se modificaron claims.
- Discrepancias de fuente con la asignación: aguacate usa un artículo alojado en PMC donde el horario decía USDA/revisión; ranas cita Costanzo et al. 1993 mientras el horario pedía Storey & Storey. El tema coincide en ambos casos, pero la sustitución de fuente debe ser validada editorialmente. En huesos, el horario dejó las cifras 300/206 como PENDING_SOURCE; el borrador usa OpenStax, pero la fuente citada debe respaldar expresamente ambas cifras antes de promover.
- Árboles declara dos source_ids que resuelven al mismo DOI de Karst et al.; son referencias duplicadas del mismo trabajo.
- Diez storyboards usan ambiente genérico y tienen `sfx=[]` en todas sus escenas. Rayo globular y arena cantante tienen ambientes/SFX más específicos, pero cada uno conserva dos escenas con SFX vacío. El silencio no queda declarado expresamente en las escenas vacías.

## 5. Cola, handoff y dispatchabilidad

`cola/entrada/` contiene solo `.gitkeep`: no hay JSON de primer nivel, subdirectorios de paquetes ni entradas del día. Por tanto, **los doce proyectos son NOT_DISPATCHABLE** desde su ubicación actual en `proyectos/`.

El workflow `.github/workflows/capcot-grok-dispatch.yml`:
- En push escucha únicamente `cola/entrada/*.json`.
- En dispatch manual busca con `find cola/entrada -maxdepth 1 -type f -name '*.json'`; un ID concreto también resuelve a `cola/entrada/<id>.json`.
- No busca `proyectos/<id>/storyboard.json` ni `cola/entrada/<id>/storyboard.json`.
- Su paso de validación solo parsea JSON; no aplica el validador estructural ni comprueba `narrative_qa`. El handoff podría dispararse con un JSON sintácticamente válido pero editorialmente no apto si se escribiera en la ruta vigilada.
- El workflow manual no filtra por fecha; `project_id=all` selecciona todos los JSON de primer nivel que existan.

`scripts/procesar_cola.py` sí compara la fecha del nombre del paquete con `--fecha`, cuyo valor por defecto es la fecha local de CDMX. También acepta `--fecha` explícita, por lo que no es una barrera absoluta contra fechas históricas. El procesador admite JSON de primer nivel y `cola/entrada/<id>/storyboard.json`; el workflow no admite esa segunda profundidad. No se ejecutó el procesador.

Los doce `cola/estado/<project_id>.json` devolvieron 404. Resultado individual para cada uno: **RECEPCION_GROK_NO_CONFIRMADA**. `handoffs/grok_inbox/` contiene solo README; no hay marcadores individuales ni archivos en `handoffs/grok_done/`.

### GitHub Actions

Las diez últimas ejecuciones disponibles son runs #138–147, todas fallidas el 1-nov-2026. En los logs de las diez, el paso de validación JSON termina correctamente y el fallo ocurre en la verificación del receptor. Error literal del run #147 (y repetido en los demás): `Falta configurar GROK_WEBHOOK_URL.` El paso termina con exit code 1 y se omite la entrega. El chequeo de `GROK_WEBHOOK_TOKEN` no llega a ejecutarse en esos runs.

La versión actual del workflow en la rama cambió: ahora escribe un marcador en `handoffs/grok_inbox/` sin webhook y trata el webhook como opcional si están disponibles ambos secretos. No hay ejecuciones posteriores que demuestren que esa versión haya corrido. Se mencionan solo los nombres `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`; no se leen ni exponen valores.

## 6. Producción preexistente y copias bloqueadas

No existe `salidas/<project_id>/` para los doce proyectos. No hay `storyboard.json`, `qa.json`, `publicacion.json`, `metadata.json` ni `licencias.json` de salida asociados; tampoco IDs de YouTube ni programación de estos proyectos en YouTube/TikTok/Facebook. No aplica `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` a los doce canónicos.

Sí existen copias heredadas en `cola/bloqueados/`:
- Aguacate: JSON directo de 198 palabras y copia de carpeta de 170 palabras.
- Ranas: JSON directo de 208 palabras y copia de carpeta de 177 palabras.
- Huesos: JSON directo de 207 palabras y copia de carpeta de 172 palabras.
- Arena: JSON directo de 206 palabras.
- Rayo globular: JSON directo de 197 palabras.
- Nubes: JSON directo de 227 palabras.

Varias copias conservan `estado=PENDIENTE_REVISION_GROK`, pero están en `cola/bloqueados/` y no tienen estado individual de Grok; esa etiqueta no demuestra recepción. Se conservaron íntegras y no se movieron ni eliminaron. También hay variantes bloqueadas con otros IDs: `inter-arboles-mito-respiran`, `comida-palomitas-explotan`, `inter-venus-dia-largo`, `inter-corazon-ballena-azul`, `inter-mpemba-mito`, `inter-suenos-pulpo` y `extra-nubes-pesan`. No se confundieron con los doce canónicos.

## 7. Reconciliación editorial, datos y documentos contradictorios

- El horario semanal es la fuente vigente para el lote: 07:00, 13:30, 17:00 y 17:45. El slot de 23:30 queda excluido. No se revisaron los slots 23:30, kids 3-nov 07:00 ni Machu Picchu 4-nov 19:00.
- `docs/briefs/2026-11-06_RADAR_CAPCOT.md` todavía conserva arriba la frase «cuatro paquetes en cola» y 19:00, pero su anotación del 6-nov 07:55 corrige a proyectos/ y 17:45. La nota final prevalece.
- `docs/briefs/2026-11-07_RADAR_CAPCOT.md` todavía afirma cuatro paquetes en cola y asigna nubes a 19:00; no contiene la corrección equivalente. El horario vigente asigna nubes a 17:45 y el borrador canónico está en proyectos/.
- `docs/PLAN_MAESTRO_AUTOMATICO.md` y `docs/CONTRATO_OPERATIVO_UNIFICADO.md` siguen describiendo una ventana de 19:00. `scripts/rotacion.py` conserva `VENTANAS=[(7,9),(13,15),(16,18),(18,21),(23,24)]` y su comentario sigue nombrando 19:00 y 23:30. Contrasta con la decisión de `docs/HORARIOS_PUBLICACION.md` del 2-nov (no programar 19:00 desde el 5-nov) y el slot 17:45 del horario semanal. No se cambió código ni la decisión horaria sin runtime y pruebas.
- `templates/storyboard.template.json` es una plantilla genérica antigua de 16:9/120 s que incluye `asset_filename`, `asset_type`, rutas de audio y `export.filename`; la plantilla vigente indicada por la receta es `templates/storyboard_vertical.template.json` (9:16, 75–90 s y preproducción sin assets). La plantilla antigua no se usó.
- Los datos operativos no están sincronizados con la semana: `temas_del_dia.json` llega a 28-oct; `rotacion.json`, `publicaciones.json` y `cola.json` a 31-oct; `estilos_usados.json` a 28-oct; `balances_6h.json` y `vistas_historico.json` a 28-oct. `endscreens_rotacion.json` llega a 4-nov y `horario_semana_2026-11-01_07.json` contiene la asignación vigente. No se modificó ningún `data/*.json`.
- Los doce storyboards no declaran `origen`. Según el código de `registro_editorial.py`, los archivos en `proyectos/` reciben por defecto `origen=propia`; el contrato describe los paquetes externos de ChatGPT como `externa`. Sin evidencia suficiente sobre quién creó el lote, no se estampó `origen` ni se atribuyó al investigador. Esta omisión puede distorsionar el conteo `MAX_ORIGEN` de rotación.
- La documentación de APIs tiene corte 31-oct. No se abrió revisión de APIs: no se presentó ni verificó un cambio oficial nuevo en esta ejecución.

### IDs antiguos en `yt_id_historial`

No existe un archivo separado llamado `historial_youtube`; los IDs antiguos están en `yt_id_historial` dentro de `data/horario_semana_2026-11-01_07.json`. Diez slots siguen descritos como `programado_yt_tt_fb` y mantienen veinte IDs históricos:

| Slot / proyecto | ID vigente | IDs históricos que permanecen en el registro |
|---|---|---|
| 1-nov 07:00 pulpo tres corazones | `PQzLUQnHbcA` | `3B1ckNUahS8`, `pxX0eGK3r98` |
| 1-nov 13:30 cebolla | `ZWF6ke9Zec0` | `Fh4KkcZr3e8`, `0WAcVgODwd8` |
| 1-nov 17:00 Baffin | `HDQr9OGpFJM` | `krh0Ll3kVjM`, `MYWsfLm_Brw` |
| 1-nov 19:00 tiburón de Groenlandia | `0x1B9_rMm-I` | `i2l4BkMvHp0`, `9XflXdWDM0A`, `bICGA3kIBcU` |
| 2-nov 07:00 camarón mantis | `5sxxx0vuXFE` | `tmxMkxA6nOw`, `d-tYvAM8hGE` |
| 2-nov 13:30 pan duro | `V9bO9EUN0JA` | `TbZRvpiDjdk`, `sHjf4QF9QiM` |
| 2-nov 17:00 murciélagos | `c-7pMF3-B-g` | `dFwKjIb8tFI`, `6ts8TvhgKa8` |
| 2-nov 19:00 sequías/energía | `OwfxfQ4RPSo` | `SQ7_g-vz8Ow`, `pMkzlwB-7bo`, `-HfaDUCg4OE` |
| 3-nov 17:00 Juno | `bpeRL5XtYLI` | `73cZz8Pi9TE`, `3IiUmsRb30Y` |
| 3-nov 19:00 SmartPE | `-WBW0X9KpLM` | `MXsNOywNzcg`, `aOcqxbBhQ0E` |

Esto es un **riesgo de duplicado pendiente de comprobación externa**: los IDs históricos siguen junto a slots descritos como programados. No se afirma que estén efectivamente activos ni se borró/canceló nada.

## 8. Cambios efectuados y límites

Cambios únicamente mecánicos y de registro:
1. Actualizado `narrative_qa.reviewed_at` en los doce JSON tras la nueva lectura en frío.
2. Corregido el prompt base de árboles y el prefijo de sus ocho prompts para coincidir literalmente con el catálogo.
3. Alineado `trend_source.url` de palomitas y pulpos con sus respectivas fuentes SRC-001.

No se reescribieron narraciones ni claims. No se modificaron `data/*.json`, `main`, workflows, secretos, permisos, estados de Grok, cola de entrada, copias bloqueadas, salidas ni decisiones editoriales. No se promovió ningún paquete. No se generaron cápsulas, frames, imágenes, voz, audio, video o renders; no se publicó ni se consumieron créditos.

## 9. Estado final

**Lote abierto.** Venus y arena pasan QA narrativo, pero no estructura. Los otros diez fallan QA narrativo. Los doce permanecen fuera de cola en `proyectos/`; no hay recepción Grok confirmada y no existe autorización para redispatch.

La auditoría fue estática: no había runtime local para ejecutar validador/helpers ni resolver DOI con Crossref. No se hizo investigación nueva de Trends ni revisión de APIs oficiales.