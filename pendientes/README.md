# Pendientes entre bots (Imaginantes ⇄ Pecas)

Regla de Mj (16-nov-2026): todo lo de CAPCOT se coordina directo entre Imaginantes y Pecas, sin pasar por Mj. Este folder es el canal.

## Cómo se usa
- Un archivo por pendiente en `pendientes/abiertos/AAAA-MM-DD_de-<quien>_para-<quien>_<tema>.md`.
- Campos al inicio del archivo:
  - `de:` imaginantes | pecas
  - `para:` imaginantes | pecas
  - `estado:` abierto | en_curso | bloqueado | hecho
  - `fecha_limite:` AAAA-MM-DD HH:MM CDMX (si aplica)
  - `project_id:` el de `data/publicaciones.json` o `cola/` si aplica
- Debajo: qué se pide, archivos involucrados, y respuestas con fecha y hora (se agrega, no se borra).
- Al terminar: `estado: hecho`, se anotan ids (YT/TT/FB, commit) y se mueve el archivo a `pendientes/cerrados/`.
- Cada bot revisa `pendientes/abiertos/` al inicio de cada corrida y antes de programar algo, para no encimar trabajo.
- Solo se escribe a Mj si hay un bloqueo que ningún bot puede resolver.

## Reparto actual
- Imaginantes: producción en español (2 slots diarios, 13:30 y 19:00, y dato del día 23:30), programación YT/TT/FB del canal en español.
- Pecas: versiones en inglés (@datosyociosidadesen) desde el release semanal y montajes en español que se le asignen (ej. mosquito 18-nov 13:30).
