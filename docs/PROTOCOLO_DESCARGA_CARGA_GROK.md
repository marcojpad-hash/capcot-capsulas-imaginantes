# Protocolo de descarga de carga de Grok Bot

**Vigente desde 2026-10-31 · America/Mexico_City**

## Objetivo
Reducir el consumo de tokens y el tiempo operativo de Imaginantes (Grok Bot) evitando que repita investigación, selección de fuentes, redacción de guiones y documentación que puede entregar ChatGPT. Bot conserva el control de la producción audiovisual y la publicación autorizada.

## Reparto de trabajo

### ChatGPT — preproducción completa
Entrega un paquete listo para producir, no una lluvia de ideas:
1. Radar y selección recomendada del tema conforme a prioridades y rotación.
2. Investigación con fuentes primarias, verificación de claims, fechas, DOI/URL y límites de evidencia.
3. Guion final, narración, título, arco y duración.
4. Storyboard completo por escena: visual, movimiento, encuadre, texto en pantalla, mapa/dato, ambiente y SFX.
5. Prompts visuales por escena compatibles con el estilo del catálogo.
6. Metadata/copy sugeridos y fuentes incorporadas al paquete.
7. Validación textual y técnica del paquete antes del handoff.

ChatGPT deja explícitos los campos pendientes; no inventa datos para aparentar que el paquete está completo. El entregable sigue siendo textual: no genera frames, voz, audio ni video.

### Imaginantes / Grok Bot — producción audiovisual
Bot no vuelve a ejecutar la investigación ni reescribe el guion por rutina. Su flujo normal:
1. Leer el paquete y comprobar que contiene los elementos mínimos.
2. Registrar recepción y decisión según el contrato de estados.
3. Producir/generar los recursos visuales y audiovisuales, voz, audio, montaje y render.
4. Ejecutar QA audiovisual oficial.
5. Corregir defectos de producción y hacer ajustes puntuales al paquete cuando sean indispensables para producir correctamente.
6. Administrar programación/publicación autorizada y registrar URL/ID, estado y métricas.

## Política de correcciones de bajo consumo
Las correcciones sí consumen tokens; no son gratuitas. Para reducir ese gasto:
- Corregir solo el campo, escena, prompt o segmento afectado.
- No repetir investigación, lectura extensa de fuentes ni reescritura integral si el defecto es local.
- No pedir a Bot que vuelva a generar el guion completo por preferencias menores.
- Si falta un dato verificable o hay contradicción factual, devolver a ChatGPT una solicitud concreta con el claim y la evidencia faltante. ChatGPT resuelve la investigación y entrega un parche.
- Si el paquete está completo y validado, Bot pasa directamente a producción.
- Rehacer una escena o un recurso audiovisual solo cuando QA detecte un defecto real; conservar los elementos aprobados.

## Contrato mínimo del paquete
Cada handoff debe incluir:
- project_id, fecha objetivo, prioridad y estado.
- Tema, enfoque y razón editorial breve.
- Guion final y duración objetivo.
- Storyboard escena por escena con prompts visuales listos.
- Fuentes y relación claim → source_id; DOI/URL y estado de verificación.
- Voz, música/ambiente, SFX, estilo y restricciones de continuidad.
- Metadata/copy sugeridos.
- Checklist de prevalidación y lista explícita de pendientes/bloqueos.

No se debe enviar un paquete como listo para producción si faltan elementos esenciales. La ausencia de un dato se marca como pendiente y genera devolución puntual, no una investigación paralela de Bot.

## Flujo operativo
ChatGPT investiga y prepara → paquete completo validado → Bot recibe y produce → QA audiovisual → correcciones puntuales si hacen falta → publicación autorizada.

## Medición
Registrar por paquete:
- Si Bot tuvo que investigar o reescribir (objetivo: no).
- Número y causa de devoluciones.
- Correcciones locales frente a reescrituras completas.
- Escenas/recursos rehechos por QA.
- Tiempo desde recepción hasta primer render y QA aprobado.

La primera revisión de resultados debe comparar al menos cinco paquetes o una semana de operación, lo que ocurra después. No afirmar ahorro de tokens sin datos de uso; medir primero retrabajo, devoluciones y tareas duplicadas como indicadores observables.

## Límites
Este protocolo no transfiere a ChatGPT la generación audiovisual, el render, QA oficial, programación ni publicación. No cambia cupos, contratos de estados, rama autorizada ni reglas de seguridad. No modifica main, data/*.json ni Motor U6.