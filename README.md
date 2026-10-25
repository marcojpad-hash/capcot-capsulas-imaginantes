# CAPCOT — Cápsulas de imaginantes

Proyecto para producir micro-cápsulas científicas verticales (9:16, 60–90 s) de forma automática.

> **Fuente de verdad vigente: [docs/PLAN_MAESTRO_AUTOMATICO.md](docs/PLAN_MAESTRO_AUTOMATICO.md)** (sustituye lo que contradiga a los documentos iniciales). Plantilla: [templates/storyboard_vertical.template.json](templates/storyboard_vertical.template.json). Prototipo probado: `scripts/`.

## Arquitectura inicial
- [Arquitectura y límites](docs/ARQUITECTURA_INICIAL.md)
- [Matriz de herramientas gratuitas y condiciones](docs/MATRIZ_HERRAMIENTAS_GRATUITAS.md)
- [Flujo de producción](docs/FLUJO_DE_PRODUCCION.md)
- [Plantilla de storyboard JSON](templates/storyboard.template.json)
- [Lista de revisión final](checklists/revision_final.md)
- [Registro de cambios](avances/2026-10-24_ChatGPT_arquitectura_inicial.md)

## Principios
1. Priorizar interfaces web gratuitas sin API de pago, verificando el acceso real de cada cuenta.
2. Automatizar localmente guion estructurado, validación, subtítulos y montaje con herramientas libres cuando sea posible.
3. No asumir generación ilimitada, ausencia de marcas de agua ni derechos comerciales en planes gratuitos.
4. No guardar medios pesados en GitHub por defecto.
5. No modificar el motor U6 desde este repositorio.

Los scripts de validación y montaje existen. El plan maestro documenta un prototipo probado; las corridas concretas deben distinguirse de los paquetes locales y verificarse por separado.
**Para Grok / modelos externos:** ver `ajustes_entre_modelos/HANDOFF_GROK_PRODUCCION.md`.
