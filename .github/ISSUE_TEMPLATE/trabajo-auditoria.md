---
name: "Trabajo — auditoría"
about: "Auditoría o revisión independiente de algo que ya está en el repo. La hace un modelo distinto al que lo escribió."
title: "[auditoria] "
labels: ["cola"]
---

## Tipo y ruta (lo lee el trabajador, no borrar)

tipo: auditoria
ruta: <ruta del archivo a auditar>
commit: <sha del archivo auditado>

## Qué se audita

<!-- Archivo + commit exactos. Contra qué checklist o contrato. -->

## Reglas

- El auditor NO es el autor. Si lo escribió ChatGPT, lo audita otro modelo (trabajador de cola, Codex si el plan lo permite, o Grok por navegador).
- No fabricar ejecuciones: si no se corrió el código, se escribe "no ejecutado", no se inventa un resultado.
- Los hallazgos van con archivo, línea y evidencia.

## Criterio de aceptación

- Informe de auditoría en el repo, con veredicto por hallazgo (corregido / pendiente / por diseño).
- Los hallazgos que se corrigen llevan su PR.

## Evidencia

<!-- La llena el trabajador: enlace al informe y a los PRs. Sin evidencia no está hecho. -->
