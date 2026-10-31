# CAPCOT — Datos y ociosidades

Este repositorio mantiene la investigación, preproducción textual, producción audiovisual y evidencias del canal **Datos y ociosidades**.

## Flujo vigente

- **ChatGPT:** radar científico, verificación, brief y storyboard JSON textual.
- **Grok:** selección editorial, generación/edición audiovisual, QA oficial y publicación.
- **GitHub:** registro y canal de handoff.

ChatGPT no genera frames, imágenes, audio, voz, video o renders; no publica; no modifica \`data/*.json\`; no toca Motor U6 ni motores canónicos.

## Fuente operativa

Rama de trabajo: \`feature/capcot-video-discovery-continuity\`.

Lee primero:
1. [Plan maestro](docs/PLAN_MAESTRO_AUTOMATICO.md)
2. [Receta](docs/RECETA_CAPSULA.md)
3. [Guía externa](docs/GUIA_MODELO_EXTERNO.md)
4. [Flujo externo](docs/FLUJO_EXTERNO.md)
5. [Catálogo visual](docs/ESTILOS_VISUALES.md) y [JSON canónico de estilos](scripts/estilos.json)

## Entregables de ChatGPT

- \`docs/briefs/YYYY-MM-DD_RADAR_CAPCOT.md\`
- \`cola/entrada/YYYY-MM-DD_slug.json\`

El storyboard incluye las fuentes; no se crea un archivo \`_fuentes.md\` separado. El JSON no contiene rutas de assets ni declara archivos multimedia inexistentes.

## Rotación reconciliada

\`scripts/registro_editorial.py\` combina en modo de solo lectura los registros de \`data/\` con storyboards de \`cola/entrada/\`, \`proyectos/\` y \`salidas/\`. No modifica archivos de datos.

Uso:
\`\`\`bash
python3 scripts/registro_editorial.py --fecha 2026-10-31
\`\`\`

Los proyectos/colas cuentan como evidencia de tema y estilo propuestos; no prueban publicación. Para estados de publicación, usar \`data/publicaciones.json\` y evidencia de plataforma.

## Automatizaciones y workflows

Hay automatizaciones de ChatGPT para investigación y control de cola. La automatización antigua de “tercera cápsula” fue reconvertida a auditoría de integridad para evitar producción duplicada y generación de medios por ChatGPT.

El workflow de GitHub Actions está en esta rama de trabajo. Los eventos \`schedule\` y \`workflow_dispatch\` no se consideran operativos hasta que el workflow exista en la rama por defecto. No afirmar que su cron está ejecutándose mientras permanezca solo en esta rama.

## Estado de ramas

Al corte de auditoría 2026-10-31, la rama de trabajo estaba divergida respecto de \`main\` (61 commits exclusivos de la rama y 9 commits exclusivos de \`main\`). No se hizo merge ni se modificó \`main\`. El paquete textual del 30-oct se copió como evidencia histórica; los assets de ese paquete permanecen fuera del repositorio y no forman parte de la cola actual.

## Documentación histórica

Las versiones previas de plan, receta, guía y flujo están en \`docs/obsoleto/2026-10-31/\`. No usarlas como instrucciones activas.

## Confirmación de Grok
Grok debe registrar recepción y estados en cola/estado/YYYY-MM-DD_slug.json. Sin ese archivo, la recepción no está confirmada. Ver docs/GROK_STATUS_CONTRACT.md.
