---
name: "Trabajo — motor U6"
about: "Correr, verificar o corregir el motor U6. Lo toma el trabajador de cola (o un modelo asignado)."
title: "[motor] "
labels: ["cola"]
---

## Tipo y ruta (lo lee el trabajador, no borrar)

tipo: motor
ruta: motor/corridas_ciegas_20261113/entrada_<CASO>.json

## Qué

<!-- Caso, corrida o corrección. Incluir el random_seed si es reproducción. -->

## Comando (si aplica)

<!-- p. ej. correr_estandar.py <entrada> <NOMBRE> ; verificar_correccion_mozart.py <RESULT> -->

## Criterio de aceptación

- Recibo de ejecución con status COMPLETED.
- Verificador que corresponda en verde (o con los fallos documentados como esperados).
- H1/H2 comparados con el original cuando es reproducción.

## Evidencia

<!-- La llena el trabajador: recibo + nota en el repo (el RESULT grande no se versiona, API 413). Sin evidencia no está hecho. -->
