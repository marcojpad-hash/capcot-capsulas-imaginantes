# Reels muertos vs vivos: causa en la subida (TT + YT)

- de: imaginantes · para: pecas, muse, Mj · estado: abierto (falta verificación en TikTok Studio) · fecha: 2026-11-16 23:50 CDMX
- Solo lectura. No se subió, resubió, borró ni cambió nada.
- Fuentes:
  - TikTok: listado público con yt-dlp, 16-nov 23:40 CDMX, 84 posts. Trae vistas, duración, caption completo y nombre de la pista. La hora de creación sale del id (`id >> 32`) y la de salida de `timestamp`; la diferencia da programado o inmediato y la anticipación.
  - YouTube: Data API v3 con `~/.capcot/token.json` (videos.list con status, processingDetails y fileDetails) y YouTube Analytics v2 (`insightTrafficSourceType` y retención por video, 20-oct a 16-nov).
  - Repo: `data/vistas_historico.json`, `data/publicaciones.json`, `salidas/*/tiktok.json`, `salidas/_ops/*`.
  - Tablas completas en `pendientes/analisis/datos_2026-11-17/` (`tt_rows.md` y `yt_rows.md`, más el JSON crudo).
- Definición: un post está **muerto** si tiene 15 vistas o menos y más de 20 h al aire. Analytics de YT va unos 2 días atrasado: lo del 15-nov en adelante todavía sale en 0.

## 1. TikTok: resubidas (misma cápsula, primera muerta y segunda viva)

| Cápsula | 1.ª subida (vistas) | caption 1.ª | 2.ª subida (vistas) | caption 2.ª | pista 2.ª |
|---|---|---|---|---|---|
| Ave jurásica | 7700708931718450450 (**1**), prog. 29 h | «Fuentes en YouTube @…» + #AveJurasica… | 7702208975848099090 (**522**), inmediato | sin YouTube | «sonido original» |
| Tardígrado | 7700708627706907912 (**3**), prog. 5 h | «Fuentes en YouTube» | 7702330005044432134 (**491**), inmediato | sin YouTube | «sonido original» |
| Ofrenda pt. 4 | 7701630032619408661 (**4**), prog. 17 h | «Fuentes en YouTube» + #Ofrendas186187189TemploMayor | 7702542108728610055 (**542**), inmediato | sin YouTube (lleva link a tiktok.com) | «sonido original» |
| Lince | 7701629331411324180 (**2**), prog. 21 h | «Fuentes en YouTube» | 7702692254871244084 (**562**), inmediato | sin YouTube | «sonido original» |
| Cebolla | 7703837369589304597 (**0**), inmediato 01:03 | #Shorts | 7703996737895124231 (**485**), inmediato | sin #Shorts | «sonido original» |
| Hielo 3 mantos | 7703837508785818901 (**0**), inmediato 01:04 | #Shorts | 7704024509996633352 (**515**), inmediato | sin #Shorts | «sonido original» |
| Hipo | 7702976051953257748 (**4**), prog. 86 h | «Fuentes en YouTube» | 7706268341152894215 (**113**), prog. 4 h | sin YouTube | caja |
| Leche → capsaicina | 7703799090567580949 (**6**), prog. 8 h | «Fuentes en YouTube» | 7706268748067409170 (**188**), prog. 27 h | sin YouTube | caja |
| Voyager | 7701628592215592212 (**8**), prog. 11 h | «Fuentes en YouTube» | 7702925930045443336 (**165**), prog. 2 h | **con** YouTube | caja |

Resubidas de posts que **ya estaban vivos**:

- Aves: de 504 a **3** (7706269323030973714).
- Corneja: de 232 a 142.

Las 9 resubidas de posts muertos revivieron, todas. En 8 de las 9 se quitó «YouTube» o «#Shorts» del caption; la excepción es Voyager, que revivió a medias (165). El tema no cambió. Esto descarta que el problema sea el contenido: la marca se pone por post al momento de subir.

## 2. TikTok: qué separa muertos de vivos (80 posts con más de 20 h)

| Variable | Muertos / total | Mediana de vistas |
|---|---|---|
| Caption con «YouTube» o «#shorts» (referencia a otra plataforma) | **18/53 (34 %)** | 144 |
| Caption sin esas referencias | **2/27 (7 %)** | 262 |
| Pista «sonido original» a secas (subidas de Mj desde el teléfono; en 10-24/26 consta en `tiktok.json`) | 1/18 (6 %) | 518 |
| Pista «sonido original - Datosyociosidades» (subidas desde la caja, Studio web) | 19/62 (31 %) | 151 |
| Caja con referencia a otra plataforma | 17/48 (35 %) | 118 |
| Caja sin referencia a otra plataforma | 2/14 (14 %) | 172 |
| Inmediato (todas las vías) | 4/30 (13 %) | 504 |
| Programado de 0.1 a 24 h | 10/29 (34 %) | 156 |
| Programado 24 h o más | 6/21 (29 %) | 117 |
| 7 o más posts el mismo día | 9/19 (47 %) | 144 |
| 2 a 6 posts el mismo día | 11/59 (19 %) | — |

Las variables que **no** separan: duración (68–99 s en ambos grupos), hora de salida, número de hashtags (de 3 a 6 en ambos grupos), largo del caption y la etiqueta IA. La etiqueta IA va ON en muertos y en vivos desde la caja; el texto «Contenido ilustrado con IA» aparece en 4 vivos de 11-14/15.

**Muertos que el patrón no explica:**

- Luz eléctrica/qom (7700697251659762952, 5 vistas): subida por Mj, pero llevaba «Fuentes en YouTube».
- Polvo de África (7704164766893296902, 2 vistas): caja, sin YouTube ni #shorts.
- Sarampión (7708761702111759634, 2 vistas): caja, sin referencias, apenas 16 h al aire. Es tema de salud y puede estar en revisión.

**Vivos con referencia a otra plataforma:** 35 de 53, por ejemplo el lote de 11-02 (146–678 vistas). La referencia sube el riesgo, pero no condena siempre al post.

**Pulpo 15-nov** (7708616723385142580, 1 vista):

- Caja, programado 1.3 h antes y con «#shorts» en el caption.
- El mismo tema ya estaba en la cuenta: «Un pulpo tiene tres corazones», 7703837126491753748, 164 vistas el 3-nov.
- Encaja con dos factores: la referencia a otra plataforma y que sea casi un duplicado de un post propio.

**Contradicción en los registros:** Serpiente voladora (7701412000789794055) y UNAM (7701457680061172999) tienen pista «sonido original» a secas, pero `tiktok.json` dice que se subieron desde la caja con Studio web. La pista no prueba al 100 % el método de subida.

## 3. YouTube

YouTube Analytics separa limpio a muertos de vivos por fuente de tráfico:

- **Vivos:** 85–97 % de las vistas vienen del feed de Shorts (`SHORTS`).
- **Muertos:** el feed de Shorts nunca los sirvió. Las pocas vistas que tienen llegan por búsqueda o desde el canal.
- Todos los videos están en `processingStatus=succeeded` y `madeForKids=false`. El procesamiento no explica nada.

| YT id | Cápsula | Vistas | Feed de Shorts / total | Nota de subida |
|---|---|---|---|---|
| O7TdKvuBjyg | Aves (orig.) | 25 | 5/25 (20 %) | sin #Shorts en el título, 0 tags |
| YVfUrd2NQJw | Aves (resub. 12-nov, API, programado) | **528** | 518/527 (98 %) | **mp4 recodificado** (otro tamaño de archivo) |
| ZHdJXFrURk4 | Corneja (orig.) | 22 | 12/22 | — |
| wxnhEdlJYwU | Corneja (resub.) | **0** | 0 | **mismo archivo exacto** (46 751 396 bytes) |
| Rg-iTgMExWw | Hipo (orig.) | 1 | 1/1 | — |
| 4lOWeMn2RCo | Hipo (resub.) | 8 | 0/8 | **mismo archivo exacto** (33 860 080 bytes) |
| 7ay4KLS8h8I | Capsaicina (orig.) | 20 | 3/20 | sin #Shorts, 0 tags, 1:43 |
| K2I_jgugiOU | Capsaicina (resub.) | 23 | 6/21 | otro archivo, pero sigue muerto |
| jeUrM5zzkdA / Z-nt8t7qPx8 / hrUwoLgADBI | Apagón (3 subidas 15-nov) | 0 / 8 / 13 | sin datos aún | jeUrM y Z-nt son **el mismo archivo exacto**; hrUwo se bajó del TikTok que ya estaba publicado (3062 vistas en TT) |
| 4Qpl17Ts_vI + WcTviUWqbes | Nubes + ratas topo | 11 / 15 | 10/10 y 1/15 | **salieron en el mismo minuto** (12-nov 07:00) |
| YV_3JgGv1kg | Pez barreleye | 24 | 4/22 | — |
| JV8SB2EpPyI | Flamenco | 2 | 0/1 | — |
| OFpAg4XA3AM, OwfxfQ4RPSo | Voyager, viento y sol | 30, 27 | 13/30, 21/27 | — |

En YouTube:

- **Resubir el archivo idéntico no revive nada.** Las 2 resubidas idénticas (wxnh, 4lOW) quedaron en 0 y 8, y el apagón triple también quedó muerto.
- **Recodificado:** 1 de 2 revivió (aves sí, capsaicina no).
- **Arranque tardío:** varios Shorts que parecían muertos arrancaron solos días después, sin resubir:
  - Reina gIjJ0YKYQ8M: 4 vistas a las 8 h y 1213 a las 48 h.
  - Titanoboa oGFKLUgBdhA: 4 vistas a las 48 h y 1353 a las 96 h.
  - Virus Andes 8EcFyXTcSdM: 0 a las 24 h y 117 a las 48 h.
- La prueba de la resubida tiene ruido: puede que el original hubiera revivido solo.

## 4. Hipótesis, ordenadas por evidencia

1. **TT: la referencia a otra plataforma en el caption (sobre todo «Fuentes en YouTube @…» y «#shorts») deja el post fuera de Para ti al subirlo.**
   - Muertos: 34 % con referencia contra 7 % sin ella.
   - 8 de las 9 resubidas que revivieron quitaron la referencia.
   - Es coherente con la política de TikTok de no recomendar contenido que manda a otra plataforma. No está confirmado: falta ver el aviso en Studio.
2. **TT: subir desde la caja (Studio web, programado) muere más que subir desde la app del teléfono** (31 % contra 6 %).
   - Se mezcla con la hipótesis 1: las subidas desde el teléfono casi nunca llevaban «YouTube».
   - Sin referencia, la caja queda en 14 % de muertos.
3. **TT: un duplicado o casi duplicado en la misma cuenta muere.**
   - Aves resubido sobre un original vivo: 3 vistas.
   - El pulpo de 15-nov repite el tema del 3-nov: 1 vista.
   - Pocos casos.
4. **YT: el archivo idéntico ya subido (en YT o bajado de TT) no entra al feed de Shorts.**
   - 3 de 3 muertos: corneja, hipo y el apagón.
   - YouTube anunció desde ene/oct-2026 que baja el alcance del contenido repetido (`docs/TENDENCIAS_2026.md`).
5. **Muchos posts el mismo día o dos en el mismo minuto** (47 % de muertos con 7 o más al día en TT; nubes + ratas topo en YT). La evidencia es débil y se cruza con lo anterior.
6. **Descartados con datos:**
   - Hecho para niños: todo va en false.
   - Procesamiento: todo está en succeeded.
   - Duración, hora de salida, número de hashtags y etiqueta IA no separan muertos de vivos.

## 5. Datos que faltan

- **El estado de cada post en TikTok Studio.** Hay que abrir Analíticas del post y revisar:
  - Si sale el aviso «Este video no es apto para el feed Para ti» o «Contenido no apto para recomendación».
  - El origen del tráfico (Para ti, perfil, búsqueda).
  - Posts a revisar:
    - Muertos: 7708616723385142580 (pulpo), 7708761702111759634 (sarampión), 7707280073446952213 (pez), 7703010495036460308 (frontera), 7704164766893296902 (polvo) y 7701628198106221845 (titanoboa).
    - Vivos de control: 7708177280417221894 (coral) y 7703009295595556116 (murciélagos).
  - Esto no está en el repo y se hace en el navegador.
- **Quién y cómo subió cada post de TT.** El método no se registró de forma sistemática antes del 27-oct, y las resubidas de 10-29/10-30 y 11-03 no tienen registro. Desde ahora habría que guardar en `tiktok.json`: método (teléfono o Studio web), programado o inmediato, y caption exacto.
- **Ediciones después de publicar** (caption o portada), **música y sonido**, y **borradores o posts borrados cerca de cada subida**: no hay registro de nada de esto.
- **Facebook:** no hay vistas por Reel en el repo. No se puede analizar.
- **YT:**
  - La hora real de subida contra el publishAt de los videos ya públicos: la API solo la da mientras están privados.
  - «Uso de IA = Sí»: la API no lo devuelve; hay que verlo en Studio.
  - Analytics de 15-nov en adelante: hay que repetir la consulta el 19-nov.

## 6. Prueba propuesta

- **TT:**
  - En las próximas 6 cápsulas, alternar dos versiones de caption:
    - A: el caption actual.
    - B: **sin «YouTube», sin «#shorts», sin hashtag compuesto largo**. Fuentes como «fuentes en el perfil» y 4–5 hashtags.
  - Todo lo demás igual: caja, programado de 1 a 6 h, una por slot, etiqueta IA ON.
  - Medir vistas y el % de Para ti a las 2 h y a las 24 h en Studio.
  - Si B queda en 0 de 3 muertos y A en 1 o más de 3, se confirma.
  - Además, cuando Mj quiera, subir **una** cápsula desde el teléfono y otra igual de limpia desde la caja el mismo día, en slots distintos.
- **YT:** no resubir nunca el mismo archivo. Si se resube, recodificar y cambiar al menos la portada y los primeros 2 s. Esperar 96 h antes de declarar muerto un Short (reina, titanoboa y virus Andes arrancaron tarde). Revisar la fuente `SHORTS` en Analytics a las 72 h.
- **Regla inmediata, sin costo:** quitar «Fuentes en YouTube @datosyociosidades» y «#Shorts» de todos los captions de TikTok y Facebook. Las fuentes van en el perfil o en el comentario fijado.
