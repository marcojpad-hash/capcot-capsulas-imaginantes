# CONTROL DE COLA CAPCOT — 2026-10-31

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama auditada:** `feature/capcot-video-discovery-continuity`  
**Corte:** 2026-10-31  
**Tipo de trabajo:** auditoría de cola y rotación. No se produjeron cápsulas ni medios.

## 1. Resultado ejecutivo

- Hay **un único storyboard fechado 2026-10-31** en `cola/entrada/`: `2026-10-31_pardelas-jetlag-solar.json`.
- Existe el brief `docs/briefs/2026-10-31_RADAR_CAPCOT.md`; recomienda ese candidato.
- La propuesta cumple los parámetros narrativos y visuales principales: 8 escenas, 218 palabras, 84 segundos con cortinilla, gancho de 6 palabras, arco completo, voz declarada correcta, estilo de catálogo, fuentes por escena, mapa y capas de dato.
- Se corrigió un defecto mecánico del JSON: `approved_assets` contenía ocho rutas futuras de frames pese a que el contrato de preproducción exige `[]`. Se dejó vacío. También se normalizaron los estados de verificación bibliográfica sin cambiar afirmaciones ni decisión editorial.
- **La música no está declarada**: `music_asset=null`, `music_license=null` y no hay `music_plan`. Por tanto, no se puede auditar la rotación musical ni certificar la unicidad completa.
- **No hay recepción confirmada por Grok.** No existe `cola/estado/` en la rama ni archivo de estado para este `project_id`.
- No hay carpeta de proyecto ni salida de producción fechada 2026-10-31. No hay evidencia de selección, producción, QA oficial o publicación para esta propuesta.

## 2. Brief y unicidad del storyboard

### Evidencia del día

| Recurso | Estado |
|---|---|
| `docs/briefs/2026-10-31_RADAR_CAPCOT.md` | Existe; presenta 4 candidatos y recomienda pardelas |
| `cola/entrada/2026-10-31_pardelas-jetlag-solar.json` | Único storyboard de entrada con fecha 2026-10-31 |
| `cola/estado/2026-10-31_pardelas-jetlag-solar.json` | No existe |
| `proyectos/2026-10-31_*/` | No hay directorio de proyecto del día |
| `salidas/2026-10-31_*/` | No hay salida del día |
| `data/cola.json` | Lista vacía |

Los paquetes en `cola/entrada/` con prefijos 25, 26, 27, 28, 29 y 30 de octubre son históricos. No son storyboards adicionales del 31.

## 3. Validación estática del candidato

Proyecto: `2026-10-31_pardelas-jetlag-solar`  
Tema: desfase del reloj interno y brújula solar en pardelas pichonetas.

| Comprobación | Resultado |
|---|---|
| Serie e idioma | `Datos y ociosidades` / `es-MX` |
| Formato | 9:16; exportación declarada 1080×1920, 30 fps |
| Escenas | 8 |
| Narración | 218 palabras |
| Duración | 78 s de escenas + 6 s de cortinilla = 84 s |
| Gancho | «Las aves también tienen jet lag» — 6 palabras |
| Arco | `hook_medias_res` → desarrollo → `cierre_historia` → `reflexion_o_pregunta` |
| Cierre | Contiene exactamente «Esto fue Datos y ociosidades.» |
| Voz | edge-tts / `es-MX-JorgeNeural` / +7% / −2Hz / pad 0.3 s |
| Estilo | `papel_rasgado_capas`, único en el storyboard |
| Prompt base | Los 8 `image_prompt` comienzan con el `prompt_base` literal del catálogo |
| Biblia visual/tipográfica | Presente; incluye paleta, luz, textura, composición, exclusiones, semilla y tipografía |
| Fuentes | 4; los `source_ids` de todas las escenas resuelven a fuentes declaradas |
| DOI | `10.1126/science.adz2542`; la ficha consigna Crossref REST `status=ok` |
| Mapa | Skomer Island, 51.7375 N / −5.2967 W; pin contextual, no ruta GPS individual |
| Capas de dato | Dos capas `dato`: desfase de ≈1 hora y muestra de 1,045 aves / 3,688 viajes / 20 años |
| Ambiente/SFX | Cada escena declara ambos campos |
| Cortinilla | 6 s, fuentes SRC-001/SRC-002 y divulgación de imágenes IA, voz sintética y audio sintetizado |
| Rutas de assets | Ninguna en escenas/export; `approved_assets=[]` tras la corrección |
| Render/publicación | `NOT_GENERATED` / `PENDIENTE_DECISION_GROK` |

### Fuentes y mapa

- SRC-001: Lewin et al., *Science* (2026), DOI [10.1126/science.adz2542](https://doi.org/10.1126/science.adz2542). La ficha ya consignaba el resultado Crossref `status=ok`; el título y los resultados se contrastan con el comunicado oficial de Oxford.
- SRC-002: [University of Oxford](https://www.ox.ac.uk/news/2026-10-26-study-finds-that-long-distance-flights-can-throw-seabirds-internal-clocks-out-of), página visible con fecha 30-oct-2026. Confirma 20 años de GPS, 1,045 aves, 3,688 viajes, desfase de hasta alrededor de una hora y desviaciones de hasta unos 15°.
- SRC-003: [Pembrokeshire Coast National Park — Skomer](https://www.pembrokeshirecoast.wales/things-to-do/pembrokeshires-islands/skomer/). Confirma la colonia de pardelas pichonetas.
- SRC-004: [Getty TGN 1009194](https://www.getty.edu/vow/TGNFullDisplay?english=Y&find=midway&nation=&place=atoll&subjectid=1009194). Sus coordenadas publicadas coinciden exactamente con el pin del storyboard.

Las afirmaciones narradas no convierten la analogía «jet lag» en síntomas humanos: el texto limita la conclusión a la navegación y dice que las aves adultas pueden corregir el rumbo.

### Correcciones mecánicas aplicadas

1. `approved_assets`: de ocho entradas con nombres de frames inexistentes a lista vacía, conforme al Plan Maestro.
2. `verification_status`: normalizado para las cuatro fuentes (`VERIFICADO_CROSSREF` o `VERIFICADO_RESOLVEDOR`), con notas de verificación. No se alteraron claims, guion, tema, estructura ni estilo.

### Pendientes que no se corrigieron

- `audio.music_asset` y `audio.music_license` siguen en `null`; falta `music_plan`. No se eligió música porque sería una decisión editorial y además no hay rotación del 29–31 completa.
- La escena 5 solicita SFX `latido`, que no aparece en `scripts/sfx_manifest.json`. Los demás SFX declarados sí tienen clave en el manifiesto. No se sustituyó el efecto porque cambiaría el diseño sonoro.
- La cortinilla cita las dos fuentes científicas principales; las fuentes cartográficas SRC-003/SRC-004 quedan en el storyboard y en la capa de mapa. No es un error estructural.

## 4. Reconciliación de temas, estructura, estilo y música

### Secuencia conocida

| Fecha / recurso | Estado real según archivos | Tema | Estructura | Estilo | Música |
|---|---|---|---|---|---|
| 2026-10-29, `salidas/2026-10-29_muralismo-cu` | Salida con QA JSON; publicación privada/programada en metadatos, no prueba de publicación pública | Muralismo CU | `sabias_que` | `mosaico_piedra` | `menor_calma` |
| 2026-10-30, `cola/entrada/2026-10-30_kromdraai-primera-fecha.json` | Propuesta histórica en cola; no hay estado Grok | Datación de Kromdraai | No declarado | `dibujo_cientifico_scratchboard` | No declarada |
| 2026-10-30, `proyectos/2026-10-30_arqueas-origen-eucariotas` | Proyecto histórico migrado; README dice que no es cola vigente y que no tiene MP4/QA/publicación | Heimdallarchaeia | `pregunta` | `microscopio_psicodelico` | `pizzicato` |
| 2026-10-31, candidato actual | Propuesta textual; recepción no confirmada | Pardelas / brújula solar | `historia` | `papel_rasgado_capas` | **No declarada** |

### Conclusiones de rotación

- El tema de pardelas no coincide con los dos candidatos conocidos del 30-oct ni con la salida conocida del 29-oct.
- El estilo `papel_rasgado_capas` difiere de los estilos de los dos candidatos conocidos del 30-oct y de la salida del 29-oct. Sí aparece en `data/rotacion.json` el 24-oct (Abejas bullying), por lo que no es un estilo históricamente inédito.
- La estructura `historia` no se repite dentro del 31-oct porque solo existe un storyboard del día. Difiere de la estructura `pregunta` del proyecto de arqueas del 30-oct, pero coincide con el último registro de `data/rotacion.json` (28-oct). La entrada Kromdraai del 30-oct no declara estructura.
- La música no se puede comparar: el candidato del 31-oct no la declara. No certificar rotación musical ni unicidad total.
- No puede certificarse la regla de «no repetir la estructura inmediatamente anterior» porque faltan registros completos y orden temporal fiable del 29–31-oct.

### Desfase entre registros

| Archivo | Última fecha disponible |
|---|---|
| `data/temas_del_dia.json` | 2026-10-28 |
| `data/rotacion.json` | 2026-10-28 |
| `data/estilos_usados.json` | Registros hasta 2026-10-28 |
| `data/publicaciones.json` | 2026-10-26 |
| `data/balances_6h.json` | 2026-10-28 08:08 CDMX |
| `data/vistas_historico.json` | 2026-10-28 08:08 CDMX |
| `data/endscreens_rotacion.json` | 2026-10-28 |
| `data/tendencias_estilos.json` | 2026-10-26 |
| `data/horario_2026-10-*.json` | Solo 26, 27 y 28 |
| `data/cierre_diario/` | Último cierre: 2026-10-27 |
| `data/cola.json` | Vacía |

Además, `data/rotacion.json` registra `papel_rasgado_capas` el 24-oct, pero `data/estilos_usados.json` no contiene ese uso. La vista combinada de `scripts/registro_editorial.py` no lee `estilos_usados.json`; combina rotación, publicaciones, cola y storyboards de cola/proyectos/salidas. Por ello, la rotación y los storyboards son evidencia más completa que ese registro de estilos aislado.

## 5. Estados: propuesta, recepción, selección, producción, QA y publicación

| Estado | 2026-10-31 | Evidencia |
|---|---|---|
| Propuesta | **Sí** | Radar del día + JSON en `cola/entrada/` |
| Recibido por Grok | **No confirmado** | No existe `cola/estado/` ni archivo del proyecto |
| Seleccionado | **Sin evidencia** | No hay decisión de Grok |
| En producción | **Sin evidencia** | No existe proyecto/salida del 31 |
| QA aprobado/rechazado | **Sin evidencia** | No existe QA del 31 |
| Publicado | **Sin evidencia** | No existe URL/ID/fecha del 31 |

### Hallazgo histórico: salida Muralismo CU

`salidas/2026-10-29_muralismo-cu/qa.json` contiene 21 comprobaciones con resultado `ok=true`. Es evidencia de un archivo QA; no atribuye por sí sola esa ejecución a Grok.

Hay una contradicción de estado que debe reconciliar el responsable:
- `LEEME.md` dice «PENDIENTE REVISIÓN DE MJ — no programar ni publicar hasta su OK».
- `data/horario_2026-10-27.json` marca el proyecto `programado_yt` con `publishAt=2026-10-27T20:30:00Z`.
- `publicacion.json` registra `uploadStatus=uploaded`, `privacyStatus=private` y el mismo `publishAt`.
- `data/publicaciones.json` no contiene ese registro porque su corte termina el 26-oct.

Esto prueba carga privada/programación registrada, no publicación pública. No se debe etiquetar como `PUBLICADO` sin URL/ID y evidencia pública correspondiente.

## 6. Procesador de cola y archivos históricos

Lectura estática de `scripts/procesar_cola.py`:
1. Recoge JSON directos y `*/storyboard.json` de `cola/entrada/`.
2. Obtiene la fecha de los primeros 10 caracteres del nombre de archivo o directorio.
3. Filtra estrictamente por igualdad con `--fecha`.
4. Si no hay entrada de esa fecha, se detiene y enumera entradas antiguas.
5. Si hay varias candidatas de la fecha, toma la primera; para 2026-10-31 hay exactamente una.

Por tanto, las entradas 25–30 no se seleccionan al procesar 2026-10-31. No se ejecutó el procesador.

Archivos históricos relevantes:
- Las carpetas de cola 25–29 conservan storyboards y documentación de paquetes anteriores; no son recepción confirmada.
- `2026-10-30_kromdraai-primera-fecha.json` conserva un contrato anterior: declara `asset_filename` en escenas y `approved_assets` con rutas futuras; no declara `estructura` y deja la música vacía. El filtro de fecha lo excluye el 31-oct.
- El proyecto de arqueas del 30-oct está en `proyectos/`, no en la cola vigente; su README lo identifica como registro histórico migrado desde `main`.
- No existe `cola/estado/` en esta rama: no hay estados machine-readable de Grok para las entradas auditadas.

## 7. Documentos y plantillas contradictorios

El Plan Maestro vigente (2026-10-31) prevalece y declara obsoletas las instrucciones anteriores archivadas en `docs/obsoleto/2026-10-31/`. Sin embargo, permanecen dos recursos sin marcar claramente como legado:

1. `docs/SKILL_DRAFT_capsula_diaria.md` sigue en la raíz de `docs/`. Permite generación de frames por el agente, ejecución integral, `--publicar --programar` y describe una voz/longitud de 75–95 s. Contradice el Plan/Guía/Receta actuales, que limitan ChatGPT a investigación y preproducción textual.
2. `templates/storyboard.template.json` es una plantilla antigua 16:9 / 120 s que declara assets, voz y exportación. La plantilla vigente para CAPCOT es `templates/storyboard_vertical.template.json` (9:16, 75–90 s, storyboard textual, sin rutas de medios).

No se modificaron esos documentos porque archivarlos o cambiar su autoridad es una decisión de mantenimiento del repositorio, no una corrección mecánica del candidato. `docs/obsoleto/2026-10-31/` sí contiene las versiones antiguas del Plan, Guía, Receta y Flujo Externo.

## 8. Runtime, validadores y APIs

- `/workspace/capcot`: ausente.
- El intento de clonar la rama en el entorno de auditoría falló por resolución DNS de `github.com`.
- No se ejecutaron `validar_storyboard.py`, `validar_continuidad_audiovisual.py`, `registro_editorial.py`, `rotacion.py` ni `procesar_cola.py`.
- Se hizo parseo JSON y comprobación estática de conteos, campos, arcos, fuentes, prompt base, capas y rutas a partir de los archivos leídos de GitHub.
- El código de `validar_storyboard.py` habría rechazado el `approved_assets` no vacío; ese defecto se corrigió. No se afirma un resultado de ejecución.
- `validar_continuidad_audiovisual.py` pertenece a la etapa audiovisual de Grok y exige assets reales; no se aplica a esta preproducción textual.
- El Radar 2026-10-31 ya documenta que no encontró un cambio oficial nuevo de Meta/Google Trends que justificara reescribir la investigación técnica. No se actualizó ese informe ni se abrieron cambios de API sin evidencia nueva.

## 9. Límites de esta auditoría

No se generaron cápsulas, frames, imágenes, voz, audio, video ni renders. No se publicó ni programó. No se creó ni modificó ningún archivo de `cola/estado/`. No se atribuyó recepción, selección, producción ni QA a Grok para el 31-oct. No se modificaron `data/*.json`, `main`, ni Motor U6; no hubo merge ni consumo de créditos.

**Conclusión:** el candidato del 31-oct está estructuralmente bien encaminado y su único incumplimiento mecánico directo del contrato de preproducción (`approved_assets` no vacío) quedó corregido. La recepción por Grok no está confirmada. La música, el SFX `latido`, la secuencia completa de rotación y los estados históricos contradictorios siguen pendientes de decisión o conciliación por sus responsables.
