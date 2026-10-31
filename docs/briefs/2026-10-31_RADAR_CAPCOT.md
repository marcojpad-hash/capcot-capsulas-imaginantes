# Radar CAPCOT — 31 de octubre de 2026

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Entrega:** investigación y preproducción textual; sin imágenes, voz, video, render ni publicación.

## 1. Google Trends México

### Observado
- Google Trends Trending Now, México, ventana de 24 horas, consultado el 31-oct-2026.
- La página muestra **220 tendencias** en total y 25 resultados en la primera página.
- Entre las señales visibles dominan fútbol (Puebla–Pumas, San Luis–Atlas, Juárez–Querétaro, Warriors–Lakers), celebridades y actualidad general.
- No aparece una tendencia científica inequívoca entre los primeros 25 resultados consultados.
- No se fuerza relación entre esas tendencias y el candidato científico.

Fuente: https://trends.google.com/trending?geo=MX

### Captura RSS
Se intentó consultar el RSS oficial `https://trends.google.com/trending/rss?geo=MX`. El endpoint no fue accesible mediante el lector web en esta ejecución. **No se afirma que el XML haya sido parseado.** Se usa Trending Now oficial como respaldo y se deja constancia de la limitación. La ruta de ingesta automática prevista por el repositorio sigue siendo `scripts/tendencias.py`.

## 2. Candidatos científicos recientes

| Prioridad | Estudio / fecha | Línea temática CAPCOT | Novedad observada | Público / ocasión | Riesgo |
|---|---|---|---|---|---|
| **1 — principal** | **Rapid longitudinal flights cause time shifts and Sun compass error**, Science, 29-oct. DOI: [10.1126/science.adz2542](https://doi.org/10.1126/science.adz2542) | Naturaleza / bichos; actualidad científica; comportamiento animal | 20 años de GPS, 1,045 pardelas y 3,688 viajes. El desfase del reloj interno durante vuelos rápidos hacia el este predice errores de brújula solar. | Público general interesado en animales; buen gancho narrativo por analogía prudente con jet lag. | No equiparar por completo fisiología de aves y humanos; no decir que se pierden ni atribuir efectos de salud no demostrados. |
| 2 | **Host diet may shape bat RNA viromes within geographic and phylogenetic constraints at a global-scale**, Nature Communications, 30-oct. DOI: [10.1038/s41467-026-79059-7](https://doi.org/10.1038/s41467-026-79059-7) | Naturaleza / bichos; ecología; actualidad | 1,627 bibliotecas de viroma, 78 especies y 13 países; geografía y parentesco explican más variación que dieta. | Público interesado en biodiversidad y ecología. | No convertir detección de secuencias en riesgo inmediato de contagio humano. |
| 3 | **First U-Pb dating of Kromdraai cave...**, npj Heritage Science, 30-oct. DOI: [10.1038/s40494-026-03075-5](https://doi.org/10.1038/s40494-026-03075-5) | Historia / paleontología / dato científico | Primera datación absoluta de un bloque clave de brecha: 1.94 ± 0.08 a 2.67 ± 0.17 Ma. | Público curioso por evolución humana y arqueología. | La edad es del bloque estudiado, no de toda la cueva ni de todos sus fósiles. |
| 4 | **Global warming intensifies compound renewable energy droughts**, Communications Earth & Environment, 29-oct. DOI: [10.1038/s43247-026-04183-7](https://doi.org/10.1038/s43247-026-04183-7) | Actualidad / clima y ambiente / energía | Simulaciones CMIP6 a 1.5, 2 y 3 °C; los episodios simultáneos de baja generación eólica y solar se intensifican con el calentamiento. | Público interesado en clima, energía y futuro. | Son simulaciones globales, no pronóstico de apagones en México. |
| 5 | **SmartPE enables efficient prime editing in dicot crops**, Nature Plants, 28-oct. DOI: [10.1038/s41477-026-02447-w](https://doi.org/10.1038/s41477-026-02447-w) | Tecnología / agricultura / biología | Sistema de edición de precisión mejora eficiencias experimentales en varias plantas dicotiledóneas. | Público interesado en alimentos y biotecnología. | No presentarlo como cultivo comercial listo ni generalizar resultados de laboratorio al campo. |

## 3. Candidato principal: pardelas y jet lag solar

### Observado
- El estudio de Patrick Lewin y colaboradores apareció en *Science* el 29-oct-2026.
- El comunicado de Oxford describe 20 años de datos GPS de 1,045 pardelas pichonetas y 3,688 viajes de alimentación.
- En vuelos de regreso hacia el este, el reloj interno puede quedar retrasado hasta alrededor de una hora frente al tiempo solar local.
- Las direcciones observadas muestran desviaciones sistemáticas compatibles con el error predicho de la brújula solar; se reportan desviaciones de hasta unos 15°.
- Las aves continuaron mostrando influencia de la brújula solar incluso cuando había referencias costeras.

### Cálculo / cartografía
- Pin cartográfico de Skomer Island: 51.7375 N, -5.2967 W, tomado del registro geográfico Getty TGN.
- El pin representa una colonia conocida y un punto de contexto, no una ruta GPS individual ni la trayectoria exacta de todos los sujetos.

### Inferencia narrativa
La comparación con el jet lag humano permite explicar un desfase entre reloj interno y hora solar. Es una analogía funcional para orientar la comprensión, no una afirmación de que las aves experimenten todos los síntomas humanos.

### Recomendación
Abrir con la contradicción: el ave usa el Sol para orientarse, pero su reloj interno puede quedarse atrás. Revelar el mecanismo antes del segundo 35–40. Cerrar con la pregunta sobre cuántos animales dependen de la sincronía entre reloj y ambiente.

## 4. Paquete creado para Grok

Archivo: `cola/entrada/2026-10-31_pardelas-jetlag-solar.json`

- Estructura: `historia`.
- Estilo: `papel_rasgado_capas`, elegido por naturaleza y paisaje, con prompt base literal del catálogo.
- Duración planificada: 84 s, incluida cortinilla de fuentes.
- 8 escenas; narración estimada dentro del rango operativo de 170–235 palabras.
- Incluye mapa de contexto de Skomer, dato de desfase horario, dato de muestra GPS, fuentes y `source_ids` por escena, identidad visual, tipográfica y voz.
- Modalidad: storyboard-only. No se generaron frames, audio ni video.

### Compuertas y límites
- DOI identificado en el registro bibliográfico de Science/AAAS y comunicado institucional; la página de Science bloqueó acceso automatizado (403). Grok debe correr `scripts/validar_storyboard.py --check-doi` en su entorno antes de aceptar el paquete.
- `data/rotacion.json` y `data/temas_del_dia.json` disponibles en esta rama llegan hasta el 28-oct. No se modificaron por prohibición expresa sobre `data/*.json`. Por ello, la rotación de estructura/estilo de los días 29–31 queda parcialmente sin cotejar.
- No se declara QA oficial, validación de Crossref ni aceptación editorial por Grok.

## 5. Handoff
- **ChatGPT:** investigación, brief, guion y storyboard textual; deja el paquete en cola.
- **Grok Bot:** verifica DOI con su validador, coteja rotación completa, decide si acepta, genera/edita medios, corre QA oficial y publica según su pipeline.
- No se publicó ni programó contenido. No se tocaron `main`, motor U6, archivos canónicos ni `data/*.json`.
