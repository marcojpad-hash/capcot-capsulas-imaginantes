---
name: "Trabajo — cápsula"
about: "Generar o corregir un paquete CAPCOT (storyboard + fuentes). Lo toma el trabajador de cola."
title: "[capsula] "
labels: ["cola"]
---

## Tipo y ruta (lo lee el trabajador, no borrar)

tipo: texto
ruta: cola/entrada/<id>/storyboard.json

## Qué

<!-- Tema, gancho y estructura. Sin "¿sabías que?" ni parte 2. Gancho = payoff, primer dato en 5-8 s. -->

## Fuentes reales (obligatorio, con URL o DOI)

<!-- Sin fuentes verificadas no se escribe el guion. No inventar datos, fuentes ni DOIs. -->

- Fuente 1:
- Fuente 2:

## Voz y estilo

voz:
estilo:

## Criterio de aceptación

- `scripts/validar_storyboard.py <ruta> --check-doi` sale con código 0.
- Narración 120-140 palabras por minuto, hilación con conectores.
- El artefacto queda en `ruta:` y el PR lo enlaza.

## Evidencia

<!-- La llena el trabajador: enlace al PR/commit. Sin evidencia no está hecho. -->
