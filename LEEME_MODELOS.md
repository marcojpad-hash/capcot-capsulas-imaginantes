# Reglas para los modelos (Claude, ChatGPT, Grok Bot)

> **Grok (producción de variedad): lee `ajustes_entre_modelos/HANDOFF_GROK_PRODUCCION.md`.**
- `investigacion/` contiene los análisis de estilo, la estrategia viral y el pipeline. Si quieres complementarlos, añade un archivo propio con tu nombre de modelo y la fecha; no sobrescribas los de otros.
- `referencias/` contiene los clips de muestra de Mj.
- Concepto: cápsulas de 60 a 90 s en periodismo narrativo, que arrancan in media res, donde la imagen narra y la voz es mínima. Cierran con una reflexión ontológica o una pregunta abierta, y al final va una cortinilla con las fuentes.
- No inventes datos ni fuentes.


## Protocolo obligatorio de entrada para todas las instancias

**Antes de trabajar en este repositorio, en cada nueva sesión y cada vez que se retome después de una pausa, lee en este orden:**

1. `ajustes_entre_modelos/README.md` — índice e instrucciones compartidas.
2. `ajustes_entre_modelos/COORDINACION_CHATGPT_IMAGINANTES.md` — responsabilidades y coordinación vigentes.
3. `docs/CONTRATO_OPERATIVO_UNIFICADO.md` — autoridad común, cupos y handoff.
4. `ajustes_entre_modelos/BITACORA_COORDINACION.md` — comentarios, decisiones, bloqueos y cambios recientes de las instancias.
5. El documento específico de tu tarea y el Plan Maestro.

No empieces producción, investigación asignada ni cambios de archivos antes de revisar esos cinco puntos. Si encuentras una instrucción contradictoria, detente en esa decisión concreta, registra la discrepancia en la bitácora y sigue la jerarquía documental; no inventes una resolución.

### Obligación de dejar comentarios
- Al terminar una intervención que afecte coordinación, alcance, prioridades, pipeline o archivos compartidos, añade una entrada a `ajustes_entre_modelos/BITACORA_COORDINACION.md`.
- Usa fecha y hora CDMX, instancia, archivos consultados, qué cambiaste, evidencia/commit, pendientes y a quién le corresponde la siguiente acción.
- No borres ni reescribas comentarios de otra instancia. La bitácora es append-only: cada entrada nueva se agrega al final.
- Si no hubo cambios ni hallazgos, no agregues ruido; basta con no registrar una entrada.
- Los comentarios son comunicación entre instancias, no sustituyen el contrato ni autorizan acciones prohibidas.

**Este protocolo aplica a ChatGPT, Grok app, Imaginantes/Grok Bot y cualquier modelo externo que trabaje en el repositorio.**

**Optimización de carga de Grok Bot:** aplicar `docs/PROTOCOLO_DESCARGA_CARGA_GROK.md`. ChatGPT entrega investigación y preproducción completas; Bot concentra tokens en producción audiovisual, QA y publicación autorizada. No duplicar research ni reescribir guiones por rutina.
