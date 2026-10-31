# Radar CAPCOT — 30 de octubre de 2026

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Estado:** investigación y preproducción textual; sin imágenes, video, render ni publicación.

## 1. Google Trends México

### Observado
- Google Trends «Trending Now», México, ventana de 24 horas: **216 tendencias**, primera página de 25 resultados.
- La primera página está dominada por fútbol, celebridades, noticias y conversación de actualidad: Puebla–Pumas, San Luis–Atlas, Juárez–Querétaro, Le Havre–PSG, Warriors–Lakers, entre otros.
- **«catrina gigante zocalo»** aparece con **2K+ búsquedas y +300 %**. Es una señal cultural/estacional, no un hallazgo científico.
- No aparece una consulta científica inequívoca entre los primeros 25 resultados.

Fuente: https://trends.google.com/trending?geo=MX

### Límite de captura
Se solicitó el RSS oficial `https://trends.google.com/trending/rss?geo=MX`. El endpoint respondió como XML; el lector web no puede interpretar directamente ese tipo de contenido. Los endpoints RSS de Nature y ScienceDaily también devolvieron XML/RSS no procesable por esta interfaz. Por tanto, **este informe no presenta el RSS como si hubiera sido parseado**: usa la página oficial de Trending Now como respaldo y páginas primarias de los editores para la búsqueda científica. El script del repositorio `scripts/tendencias.py` sigue siendo la vía normal de ingesta RSS cuando se ejecute en el entorno del proyecto.

### Inferencia editorial
No conviene forzar una relación entre la Catrina del Zócalo y una noticia científica sin una pregunta de ingeniería verificable. Se puede guardar como señal cultural; no desplaza a los estudios científicos de esta semana.

## 2. Candidatos científicos (publicados en los últimos siete días)

La clasificación usa la **taxonomía provisional** de la matriz operativa. No sustituye la auditoría de las seis líneas históricas que debe validar Grok.

| Prioridad | Estudio y fecha | Línea / encaje provisional | Novedad verificable | Público y ocasión | Riesgo editorial |
|---|---|---|---|---|---|
| **1 — principal** | **Kromdraai: primera datación U-Pb de un bloque de brecha**, 30-oct. DOI: [10.1038/s40494-026-03075-5](https://doi.org/10.1038/s40494-026-03075-5) | Historia de la ciencia y del mundo · paleontología | Primeras fechas absolutas para un bloque clave: intervalo de 1.94 ± 0.08 a 2.67 ± 0.17 Ma. | Público general curioso; cápsula de historia natural para fin de semana. | No trasladar la edad del bloque a toda la cueva ni a todos los fósiles; no afirmar que se fechó directamente el espécimen tipo. |
| 2 | **Host diet may shape bat RNA viromes…**, 30-oct. DOI: [10.1038/s41467-026-79059-7](https://doi.org/10.1038/s41467-026-79059-7) | Naturaleza y vida animal | Integra 1,627 bibliotecas de viroma de ARN, 78 especies y 13 países; geografía y parentesco del hospedador explican más variación que la dieta. | Público interesado en fauna, ecología y biodiversidad. | No convertir secuencias virales detectadas en «virus peligrosos» ni insinuar brote o transmisión humana; el viroma no equivale a infección humana. |
| 3 | **Global warming intensifies compound renewable energy droughts**, 29-oct. DOI: [10.1038/s43247-026-04183-7](https://doi.org/10.1038/s43247-026-04183-7) | Actualidad científica · clima y ambiente | Simulaciones CMIP6 a 1.5, 2 y 3 °C; a 3 °C se reportan cambios significativos en duración, frecuencia e intensidad en 69.4 %, 74.0 % y 50.2 % del área terrestre global, respectivamente. | Público general interesado en clima y energía. | Son proyecciones/modelos globales, no apagones observados ni un pronóstico específico para México. |
| 4 | **SmartPE enables efficient prime editing in dicot crops**, 28-oct. DOI: [10.1038/s41477-026-02447-w](https://doi.org/10.1038/s41477-026-02447-w) | Ciencia y tecnología · agricultura/alimentos | En protoplastos, la eficiencia mejoró 6.3–23.0 veces en Arabidopsis y 8.2–38.2 veces en tomate frente a sistemas de edición de referencia; también se probaron tejidos y transformaciones estables. | Estudiantes y público interesado en biotecnología agrícola. | No presentarlo como cultivo comercial disponible ni como resultado uniforme en campo; las cifras dependen de especie, tejido y locus. |

Fuentes primarias:
- Kromdraai: https://www.nature.com/articles/s40494-026-03075-5
- Murciélagos: https://www.nature.com/articles/s41467-026-79059-7
- Energía renovable: https://www.nature.com/articles/s43247-026-04183-7
- SmartPE: https://www.nature.com/articles/s41477-026-02447-w

## 3. Selección principal: Kromdraai

**Razón de selección:** publicación del día, DOI y metadatos visibles en la página del editor, ubicación concreta, un método explicable y una advertencia narrativa clara que evita el sensacionalismo.

### Observado en el estudio
- Kromdraai forma parte del conjunto patrimonial de la Cuna de la Humanidad, en Gauteng, Sudáfrica.
- El equipo obtuvo las primeras fechas absolutas para un bloque clave de brecha mediante geocronología uranio-plomo.
- El intervalo comunicado para ese bloque va de **1.94 ± 0.08 a 2.67 ± 0.17 millones de años**.
- El artículo explica que comparar varios enfoques matemáticos permite evaluar mejor los modelos cuando el ajuste isotópico es débil.

### Cálculo cartográfico
La página de mapas de UNESCO da para el componente 915bis-001 las coordenadas 25°55′45″ S, 27°47′20″ E. Convertidas a decimal: **lat −25.92917, lon 27.78889**. El pin representa el componente patrimonial que incluye Kromdraai y alrededores; **no** pretende marcar la entrada exacta de la cueva.

### Inferencia
Una mejor cronología permite ordenar y comparar los depósitos fósiles. La datación de un bloque no resuelve por sí sola la edad de todos los restos encontrados en el sitio.

### Recomendación
Conservar el gancho «La cueva ya tiene fecha», pero explicar antes del cierre que la fecha corresponde a un bloque concreto. No utilizar «los fósiles tienen 2.6 millones de años» ni «la cueva tiene exactamente 2 millones de años».

## 4. Paquete textual preparado para Grok

Archivo: `cola/entrada/2026-10-30_kromdraai-primera-fecha.json`

- Estructura: `sabias_que` (no aparece entre las cinco entradas más recientes visibles en `data/rotacion.json`).
- Estilo: `dibujo_cientifico_scratchboard`, elegido por la etiqueta temática de paleontología del catálogo; no aparece entre las cinco entradas más recientes de rotación.
- Duración planificada: **84 s**, incluida la cortinilla de fuentes de 6 s.
- Narración: **185 palabras**, ocho escenas.
- Incluye capas `mapa` y `dato`, tres fuentes, `source_ids` por escena, `visual_identity`, `typography_identity`, voz obligatoria y ocho nombres de assets previstos.
- No hay frames: el paquete es storyboard-only, modalidad admitida por `docs/FLUJO_EXTERNO.md`. Grok decide si lo acepta, genera los medios y corre el QA oficial.

### Compuerta pendiente
- La página de Nature publica el DOI; la comprobación automatizada `python3 scripts/validar_storyboard.py ... --check-doi` contra Crossref queda para el entorno del repositorio.
- No se generaron archivos de imagen, no se montó audio/video y no se ejecutó QA audiovisual.
- `data/rotacion.json` y `data/temas_del_dia.json` llegan hasta el 28-oct en esta rama; `data/publicaciones.json` llega hasta el 26-oct. No se modificaron porque la guía prohíbe editar `data/*.json`. Por eso no se afirma que el registro de publicaciones de los días 29 y 30 esté completo.

## 5. Seguimiento técnico: Meta y Google Trends

### Meta — detalles nuevos para el diseño del adaptador
1. **Etiqueta de contenido generado con IA:** la documentación de Instagram Platform lista `is_ai_generated` en la creación de medios y como campo de IG Media, disponible con Facebook Login e Instagram Login. Es una autodeclaración al publicar, no un detector automático. Para CAPCOT conviene conservar este campo en metadata y coordinarlo con Grok, que controla publicación.
2. **Story Insights:** `link_clicks` cuenta taps en enlaces de Stories; la nota de Meta indica que solo está disponible con Instagram API usando Facebook Login. No pedirlo para Reels.
3. **`media_url` no garantizado:** desde el cambio del 30-jul-2026 puede omitirse para medios con audio protegido o Reels con descargas desactivadas, incluso si la respuesta HTTP es 200. Si una futura rutina necesita localizar un medio, tratar `media_url` como opcional y conservar `permalink`/`thumbnail_url`.
4. **Facebook Page Insights:** las referencias de integradores que reproducen el anuncio de Meta sitúan desde el 15-jun-2026 la retirada de métricas antiguas de impresiones/alcance único, entre ellas `page_impressions_unique` y `post_impressions_unique`. Se citan como reemplazos `page_total_media_view_unique` y `post_total_media_view_unique` cuando corresponda; varias desagregaciones paid/viral/non-viral no tienen reemplazo equivalente. No mezclar las series antiguas de reach con las nuevas de media views ni codificar nombres sin una prueba contra la versión/activo real.
5. Las notas del 20 y 28-oct-2026 se refieren principalmente a comentarios ordenados, captions de Stories y handoffs de mensajería/webhooks; no añaden una métrica orgánica de Reels que cambie el MVP de analítica.

**Acceso a fuentes Meta:** el changelog oficial enlazado desde las notas de Meta respondió HTTP 429 en esta consulta. Los puntos anteriores se contrastaron con el feed de notas de Instagram Platform que enlaza al changelog oficial; los campos de Page Insights deben confirmarse en la prueba autorizada antes de implementar.

### Google Trends API
La documentación oficial sigue describiendo una **alfa de acceso limitado**, con ventana móvil de cinco años, agregación diaria/semanal/mensual/anual, regiones/subregiones y datos escalados consistentemente. No se observó una nueva apertura general ni una modificación de esas capacidades en esta revisión. El RSS MX sigue siendo la ruta gratuita de señal diaria del repositorio; no sustituirlo por endpoints internos o por una API alfa sin aprobación.

Fuentes técnicas:
- Meta Instagram Platform changelog: https://developers.facebook.com/docs/instagram-platform/changelog/
- Meta Instagram Insights: https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-media/insights/
- Meta Page Insights: https://developers.facebook.com/docs/platform/insights/reference/page-insights/
- Meta Graph API v25 changelog: https://developers.facebook.com/docs/graph-api/changelog/version25.0/
- Google Trends API alpha: https://developers.google.com/search/apis/trends
- Google Trends MX: https://trends.google.com/trending?geo=MX

## 6. Handoff y límites

- **ChatGPT:** fuentes, clasificación, brief, guion/storyboard y documentación.
- **Grok:** decisión editorial final, generación/edición audiovisual, QA oficial y publicación conforme al flujo vigente.
- No se publicará desde este paquete. No se tocaron `main`, motor U6 ni archivos canónicos. No se solicitaron ni expusieron tokens.
