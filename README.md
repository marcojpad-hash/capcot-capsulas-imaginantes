# CAPCOT — Cápsulas de imaginantes

Proyecto para producir micro-cápsulas científicas verticales (9:16, 60–90 s) de forma automática.

> **Fuente de verdad vigente: [docs/PLAN_MAESTRO_AUTOMATICO.md](docs/PLAN_MAESTRO_AUTOMATICO.md)** (sustituye lo que contradiga a los documentos iniciales). Plantilla: [templates/storyboard_vertical.template.json](templates/storyboard_vertical.template.json). Prototipo probado: `scripts/`.
>
> **Biblia editorial y plantilla visual: [docs/BIBLIA_LINEA_EDITORIAL.md](docs/BIBLIA_LINEA_EDITORIAL.md)**.

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

## Nuevos módulos — descubrimiento y continuidad
- [Buscador de generadores de video](scripts/buscar_generadores_video.py): cataloga APIs, repositorios públicos, modelos abiertos y alternativas de ensamblaje; no contrata servicios ni consume créditos.
- [Continuidad audiovisual](docs/CONTINUIDAD_AUDIOVISUAL.md): biblia visual, tipográfica y de voz, con reglas de consistencia de inicio a fin.
- Validador: `python scripts/validar_continuidad_audiovisual.py <storyboard.json>`.
- Workflow semanal: `.github/workflows/capcot-descubrimiento.yml` (requiere integrar esta rama a `main` para activar el calendario).


## APIs de edición: Krea y Runway
- [Investigación y decisión de integración](docs/API_EDITORES_KREA_RUNWAY.md).
- Cliente API opcional: `scripts/media_api_clients.py` (Krea 3 y Runway/Bria FIBO Edit 1.5 para edición de imagen; Krea Seedance 2.5 para clips; Runway Aleph 2.0 para edición de video).
- Credenciales solo como variables de entorno/Repository Secrets: `KREA_API_KEY` y `RUNWAYML_API_SECRET`. No se guardan en Git.
- Las llamadas de generación son facturables y no se ejecutan en CI.
- Migración y auditoría de continuidad: `scripts/migrar_storyboard_continuidad.py`, `scripts/validar_continuidad_audiovisual.py`, `scripts/auditar_assets_storyboard.py`.
