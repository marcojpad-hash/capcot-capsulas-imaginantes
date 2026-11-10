# Hook de pedidos a Grok (cápsulas) — causa y arreglo

Fecha: 2026-11-09 ~22:40 America/Mexico_City  
De: Imaginantes (investigación + registro, sin programar el workflow a fondo)

## Cuál es el hook

Grok (grok.com, conector GitHub) no se entera por webhook ni por `handoffs/grok_inbox/`. El hook vigente está documentado en `docs/LINEA_EDITORIAL_VISUAL.json` (`cableado_grok`):

- Lee el **bus** de `marcojpad-hash/agente-cero-costo`: `conector/ESTADO.md`, `conector/estado.json` y `conector/bus/*.json`.
- Un pedido entra al bus creando un Issue `[BUS] indicacion - <emisor>` con `para: grok` en el cuerpo. El workflow `github-native-agent-bus.yml` lo convierte en `conector/bus/gh-issue-N.json`.
- El webhook Firebase (`capcot.package.ready`) y los secretos `GROK_WEBHOOK_URL` / `GROK_WEBHOOK_TOKEN` están abandonados (`gh secret list` vacío).

## Qué fallaba (evidencia)

El paquete ASTRA (`cola/entrada/2026-11-09_dato-robot-ensambla-orbita/`, commit `7ea62b5`, 18:40 hora CDMX) y el marcador `handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json` nunca se registraron en el bus: no había Issue previo de este pedido. Una corrida de Grok que solo lea el bus no lo toma.

Además, el workflow viejo `capcot-grok-dispatch.yml`:

- no está en `main` (solo en `feature/capcot-video-discovery-continuity`);
- dispara solo con `cola/entrada/*.json`, y los paquetes reales son carpetas;
- todas las corridas del 1-nov fallaron con `Falta configurar GROK_WEBHOOK_URL`.

Por eso también quedaron sin aviso briefs como `ajustes_entre_modelos/PARA_GROK_variar_plantillas_08nov.md` o entregas `revariar-*` si nadie abrió un Issue `[BUS]`.

Los frames de ASTRA se generaron después en un chat (commits `9f6984d` y `da50278`, 22:29–22:30 hora CDMX), pero `frames/` sigue sin PNG: la subida binaria falló por el conector.

No encontré en los repos un horario documentado a las 10:23. Las Automations CAPCOT documentadas (si siguen activas en grok.com; no se verificó la app) son C1 ~11:00, C3 ~18:00 y C2 ~20:00 hora CDMX (`docs/SCRIPT_AUTOMATIONS_GROK_CAPCOT.md`).

## Qué se arregló ahora

- Pedido ASTRA + orden de arreglo del hook registrados en el bus: https://github.com/marcojpad-hash/agente-cero-costo/issues/18 (evento `conector/bus/gh-issue-18.json`).
- Este archivo. El marcador de `handoffs/grok_inbox/` apunta al Issue.

## Pendiente de Grok

1. Subir `frame_01` … `frame_09` (1080×1920) al paquete ASTRA; mover el marcador a `handoffs/grok_done/`; no tocar JorgeNeural ni publicar.
2. En una rama + PR a `main` de este repo, **sin merge**: workflow en `main` que, al entrar un paquete a `cola/entrada/`, abra un Issue `[BUS] indicacion - CAPCOT` en `agente-cero-costo`.

Grok debería tomarlo en la próxima sesión o Automation que lea el bus (Issue #18). El slot 23:30 de hoy ya no está garantizado.
