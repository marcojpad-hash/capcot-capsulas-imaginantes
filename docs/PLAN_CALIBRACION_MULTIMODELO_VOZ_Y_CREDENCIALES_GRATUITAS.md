# Plan CAPCOT: calibración multimodelo, continuidad audiovisual y voz propia

**Estado:** propuesta operativa para revisión externa.  
**Alcance:** complementa la biblia audiovisual y el flujo de descubrimiento. No modifica U6, no publica contenido y no autoriza consumo de créditos.

## Objetivo

Producir cápsulas con distintos proveedores de generación/edición sin que el canal cambie de identidad cada día. El proveedor puede variar; la identidad editorial, visual y sonora debe permanecer estable.

La unidad de control será un paquete canónico de producción que todos los modelos reciben y que toda salida debe respetar.

## 1. Paquete canónico por cápsula

Cada cápsula debe tener un manifiesto versionado con:
- Identificador, fecha de corte de la información y fuente factual aprobada.
- Guion maestro bloqueado, duración objetivo y pausas.
- Storyboard por plano: propósito narrativo, encuadre, sujeto, movimiento, duración y transición.
- Biblia visual: paleta, contraste, textura, iluminación, composición y reglas de continuidad.
- Tipografía, jerarquía, márgenes seguros y reglas para subtítulos.
- Identidad sonora: voz elegida, velocidad, tono, pronunciación, música/ambiente y mezcla.
- Relación 9:16, resolución de entrega y especificación de exportación.
- Elementos prohibidos: cambios de logotipo, textos inventados, marcas de agua, voces distintas y alteraciones del dato.
- Proveedor, modelo, versión, parámetros, prompt, seed (si existe), referencias y hash de assets.

Los modelos no deben reescribir el dato ni improvisar texto en pantalla. Reciben guion y storyboard como restricciones.

## 2. Arquitectura multimodelo

Separar el flujo en etapas intercambiables:
1. **Dato y guion:** una fuente editorial valida el dato del día y congela el guion.
2. **Desglose:** se produce storyboard canónico y lista de planos.
3. **Generación visual:** uno o varios proveedores generan alternativas para los mismos planos.
4. **Edición/continuidad:** el editor adapta los planos al storyboard y a la biblia visual.
5. **Voz:** se incorpora una pista de voz maestra; los proveedores no deben sustituirla por voces sintéticas.
6. **Montaje y control:** composición, subtítulos, mezcla y validación.
7. **Aprobación humana:** ninguna salida se publica automáticamente.

Cada proveedor se conecta mediante un adaptador que traduce el manifiesto canónico a su API. La salida se normaliza a un esquema común; no acoplar el proyecto a un único proveedor.

## 3. Calibración comparativa de proveedores

Antes de asignar producción diaria, ejecutar un benchmark pequeño con el mismo material:
- Seleccionar 3 planos representativos: apertura, plano explicativo y cierre.
- Enviar el mismo guion, referencias, storyboard y restricciones a cada proveedor.
- Hacer 2–3 variantes por plano solo si el coste está autorizado.
- Conservar prompts, parámetros, modelo/versión, archivos originales y coste real.
- Comparar resultados con una rúbrica común.

### Rúbrica (0–5)

| Dimensión | Qué se evalúa |
|---|---|
| Identidad visual | Paleta, iluminación, textura y composición |
| Continuidad | Los planos parecen pertenecer a la misma cápsula |
| Fidelidad factual | No altera el dato ni inventa elementos |
| Tipografía | Texto correcto, legible y dentro de márgenes |
| Movimiento | Movimiento útil, estable y sin deformaciones |
| Voz | Conserva voz maestra, pronunciación y ritmo |
| Audio | Niveles, limpieza, sincronía y artefactos |
| Repetibilidad | Parámetros documentados y reproducibles |
| Coste/tiempo | Coste por plano aprobado y tiempo de entrega |

Registrar puntuaciones por proveedor y modelo, no solo una calificación global. Un modelo puede ser bueno generando imágenes y malo editando video. No forzar un único ganador para todas las etapas.

**Aceptación inicial:** ningún defecto crítico de factualidad, texto, identidad de marca o audio; puntuación mínima acordada en continuidad e identidad. Las salidas que fallen se descartan o corrigen, no se compensan con un promedio alto.

## 4. Dato del día y consistencia entre modelos

El dato del día tendrá una sola ficha editorial con afirmación exacta, fuente primaria y fecha, contexto, límites de interpretación, guion aprobado, texto exacto en pantalla e identificador/hash de versión.

Si dos modelos proponen datos distintos, no se promedian ni se elige por mayoría. Se vuelve a la fuente primaria y la revisión editorial decide. Los modelos pueden proponer candidatos, pero solo una ficha aprobada alimenta todas las versiones audiovisuales.

Se pueden comparar en paralelo guiones o tratamientos de distintos modelos, pero se conserva un único guion final bloqueado para producción.

## 5. Voz propia como pista maestra

Probar la voz del creador como narración principal:
1. Grabar el guion con el teléfono en un espacio silencioso.
2. Mantener distancia al micrófono, orientación y nivel consistentes.
3. Grabar una toma completa o tomas por párrafo.
4. Conservar el original sin procesar, preferentemente WAV/PCM.
5. Limpiar ruido, ajustar pausas y nivelar volumen sin cambiar la identidad.
6. Entregar a cada editor exactamente la misma pista maestra.
7. Bloquear la pista de voz durante la edición visual; el modelo solo crea imágenes y montaje.

Esto evita pagar TTS por cada proveedor, reduce la variación de voz y conserva identidad. No elimina el coste de generación de video ni garantiza que el editor respete la pista: comprobar exportación y comparar audio antes/después. No entrenar ni clonar la voz en servicios externos sin revisar condiciones y consentimiento.

## 6. Niveles gratuitos y Codex

Investigar vías legítimas:
- Planes gratuitos oficiales y límites publicados.
- Créditos promocionales otorgados por proveedores.
- Modelos open-source con demo o alojamiento gratuito permitido.
- Cuotas gratuitas de APIs, verificando uso comercial y restricciones.
- Herramientas móviles/locales que no requieran API de pago.
- Codex/GitHub para automatizar código, validadores, manifiestos y pruebas; no asumir que Codex incluye créditos de generación audiovisual.

No crear cuentas múltiples para evadir límites, promociones, controles antifraude o términos del proveedor. Se pueden usar cuentas de miembros reales de un equipo cuando cada persona las administra y el proveedor lo permite expresamente. No automatizar altas, rotación de identidades, teléfonos o métodos de pago para multiplicar cuotas.

Por servicio registrar proveedor, plan, elegibilidad comercial, límites, caducidad, política de datos, retención, atribución, restricciones de cuenta y coste al superar el nivel gratuito. Priorizar coste total y continuidad, no solo cantidad de créditos.

## 7. Papel de Codex/GitHub

Codex puede ayudar a mantener y ejecutar software del pipeline sobre el repositorio: adaptadores, validadores, pruebas, manifiestos y comparadores. No es por sí mismo un puente universal a créditos de Krea, Runway u otros generadores. Cada servicio requiere integración oficial y credenciales propias.

Diseño recomendado:
- GitHub Actions para validación sin coste externo y tareas dentro de límites gratuitos.
- Secrets de GitHub para claves; nunca escribirlas en archivos, commits, issues o conversaciones.
- Adaptadores por proveedor con interfaz común.
- Modo de simulación por defecto.
- Límite de gasto y confirmación manual antes de generación de pago.
- Registro de consumo por trabajo y proveedor.
- Ninguna clave en logs o artefactos.
- No activar generación real hasta que el usuario autorice el coste y estén configuradas las credenciales.

## 8. Puertas de control

| Puerta | Requisito |
|---|---|
| G0 — Fuente | Dato verificado y guion aprobado |
| G1 — Manifiesto | Storyboard y biblia visual completos |
| G2 — Calibración | Benchmark comparable y coste registrado |
| G3 — Voz | Pista maestra aprobada y nivelada |
| G4 — Montaje | Continuidad visual, tipográfica y sonora validada |
| G5 — Publicación | Aprobación humana explícita |

Si falta un asset o una pista de audio, el estado debe ser BLOCKED_MISSING_ASSET, no aprobado.

## 9. Entregables propuestos

- manifests/capsula.schema.json: esquema común del manifiesto.
- calibration/providers.yaml: matriz de proveedores, modelos, capacidades, límites y coste.
- calibration/scorecard.csv: resultados por plano.
- assets/voice/README.md: procedimiento para incorporar voz maestra sin subir grabaciones privadas.
- scripts/validate_manifest.py: validación del manifiesto.
- scripts/compare_provider_outputs.py: comparación y reporte.
- Adaptadores desacoplados para generación de imagen, video, edición y audio.

Son objetivos de implementación; no deben marcarse como creados hasta que existan y pasen pruebas.

## 10. Solicitud de revisión externa (Grok u otro revisor)

Revisar este plan y el PR completo con foco en:
1. Errores técnicos o supuestos falsos sobre Codex, GitHub Actions, Krea, Runway y APIs.
2. Servicios gratuitos reales que permitan el uso previsto, límites y términos; citar documentación oficial y distinguir demo, plan gratuito y API gratuita.
3. Riesgos de depender de varios proveedores y propuesta de adaptadores/formatos interoperables.
4. Mejoras para preservar identidad visual, voz, tipografía y continuidad.
5. Viabilidad de la voz propia como pista maestra y cómo impedir que editores la sustituyan.
6. Coste de un piloto mínimo y estrategia para minimizar consumo.
7. Seguridad, secretos, licencias, privacidad y derechos de uso.
8. Qué implementar primero y qué no conviene construir todavía.

**Formato solicitado:** hallazgos priorizados (bloqueante/alto/medio/bajo), evidencia/enlaces oficiales, archivos y líneas afectados, corrección concreta y pruebas necesarias. No aprobar por cortesía: señalar contradicciones y rechazar mecanismos que violen términos de servicio.

## Restricciones permanentes

- No modificar U6 ni sus archivos canónicos.
- No hacer commits en main para esta propuesta.
- No publicar cápsulas.
- No ejecutar generaciones de pago ni consumir créditos sin autorización expresa.
- No subir grabaciones de voz privadas al repositorio.
- Mantener storyboard y assets originales; cualquier transformación produce una copia versionada.
