# Revisión Semgrep y preservación de SARIF — 2026-11-21

## Resultado observado

- Repositorio: `marcojpad-hash/capcot-capsulas-imaginantes`.
- Ejecución de origen: [Actions 44974165982](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44974165982), rama `main`, commit `6ef8b749522b527502723d47cf904340c55a5ebc`.
- Job: `semgrep`, ID `137060204790`.
- El escaneo terminó: 361 reglas, 1,028 archivos, 32 findings (32 blocking); el comando salió con código 1 por `--error`.
- El paso `Upload SARIF` quedó `skipped` porque el paso de escaneo terminó en error. La consulta de artifacts devolvió una lista vacía; no hay SARIF descargable para esta ejecución.
- La consulta de Code Scanning mediante el conector devolvió HTTP 400 (endpoint no permitido por el conector). No se atribuye el bloqueo a la red ni se inventa el contenido de los 32 findings.

## Corrección preparada en la rama de trabajo

Se añadió `.github/workflows/semgrep.yml` a `feature/capcot-video-discovery-continuity`:

1. Permisos explícitos mínimos: `contents: read` y `security-events: write`.
2. El upload a GitHub Code Scanning usa `if: always() && hashFiles('semgrep.sarif') != ''`, para ejecutarse aunque Semgrep devuelva código 1, siempre que el SARIF exista.
3. Se conserva además `semgrep.sarif` como artifact descargable durante siete días.
4. El workflow mantiene el disparador `push` limitado a `main`, además de PR y schedule. La escritura en la rama feature no lo dispara.

**Commit de la corrección:** `cccb3536d88b3e2dddd8665b7a1c2d1182efecce`.  
**Lectura de vuelta:** blob `6a8797b11e56fb17527ce1dd319604e10f4ddd33`; permisos, condiciones de upload, artifact y ausencia de valores secretos comprobados.

## Límite de verificación

La corrección está **EJECUTADA y VERIFICADA por lectura de vuelta**, pero no se ejecutó el workflow ni se modificó `main`. Por tanto, todavía no está comprobado el upload real de SARIF. La corrección solo tendrá efecto en `main) después de una integración autorizada; no se abrió PR ni se hizo merge.

## Otras comprobaciones de esta pasada

- El trabajador de cola en `main`, run `44973903856`, terminó SUCCESS y registró literalmente `[trabajador] sin trabajo en cola.`.
- El smoke de Kuroshio, run `44951621909`, terminó SUCCESS y ejecutó `python scripts/validar_storyboard.py ...` **sin** `--check-doi`; no acredita verificación DOI.
- Los siete sidecars de estado consultados para proyectos 21–23 nov devolvieron 404: `RECEPCION_GROK_NO_CONFIRMADA`. No se crearon ni modificaron estados Grok.
- No se promovió ningún storyboard, no se envió webhook, no se generaron medios y no se modificaron `data/*.json`.
