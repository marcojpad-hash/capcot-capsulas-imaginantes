# Flujo externo CAPCOT — ChatGPT → GitHub → Grok

## Roles
- ChatGPT: investigación, verificación, brief y storyboard textual.
- Grok: selección editorial final, producción audiovisual, QA oficial y publicación.
- GitHub: contrato de handoff y registro verificable.

No suponer que Grok consulta la cola en segundo plano. La recepción solo se confirma con lectura/estado registrado.

## Entrada
ChatGPT trabaja exclusivamente en \`feature/capcot-video-discovery-continuity\` y crea:
- \`docs/briefs/YYYY-MM-DD_RADAR_CAPCOT.md\`
- \`cola/entrada/YYYY-MM-DD_slug.json\`

El storyboard incorpora fuentes, identificadores por escena, mapa, dato/gráfico, biblia visual/tipográfica, voz prevista, ambiente y SFX. No genera medios ni directorios de frames; no altera \`data/*.json\`.

## Recepción y producción de Grok
1. Lee brief y JSON.
2. Verifica fuentes, DOI, claims, coordenadas y rotación.
3. Decide seleccionar, devolver o rechazar.
4. Si selecciona, genera assets y asigna rutas en la etapa de producción.
5. Ejecuta render y QA oficial.
6. Decide y ejecuta publicación conforme a permisos.
7. Registra estados y evidencia.

El validador acepta storyboards textuales sin rutas de assets. El pipeline de producción asigna rutas después. \`procesar_cola.py\` solo selecciona entradas cuya fecha coincide con \`--fecha\`; no consume automáticamente la cola histórica más antigua.

## Estados
- \`PROPUESTA_EN_COLA\`
- \`RECIBIDO_POR_GROK\`
- \`SELECCIONADO\` / \`DEVUELTO\` / \`RECHAZADO\`
- \`EN_PRODUCCION\`
- \`QA_APROBADO\` / \`QA_RECHAZADO\`
- \`PUBLICADO\`

Un estado no implica el siguiente. Un storyboard no prueba recepción; un paquete de medios no prueba QA; QA no prueba publicación.

## Límites
ChatGPT no usa \`--publicar\`, no programa, no modifica \`main\`, no hace merge, no modifica \`data/*.json\`, no toca Motor U6 ni motores canónicos, no consume créditos y no declara QA oficial. La continuidad audiovisual aplica a la etapa de Grok, no autoriza a ChatGPT a generar medios.
