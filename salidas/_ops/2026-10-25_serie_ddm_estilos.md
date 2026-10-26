# Serie Día de Muertos 2026 — biblia (corrección MJ pt144u)

| Parte | Fecha/hora CDMX | Título | Estilo |
|---|---|---|---|
| 1 | 26-oct 14:30 | Día de Muertos · Parte 1: El papel picado nació de una DEUDA | papel_picado (sin id en estilos.json; usar papel_recortado_popup como base) |
| 2 | 26-oct 19:00 | Día de Muertos · Parte 2: La ofrenda | claymation → variante papel maché / cartonería (alebrijes de Linares) |
| 3 | 27-oct 19:00 | Día de Muertos · Parte 3: (TBD) Los pueblos que sí limpian a sus muertos | bordado (alterno linograbado) |

Catrina 17:00 es pieza suelta (sugerido linograbado/satira_periodico, guiño Posada), no lleva "Parte".

## Estilos de estilos.json que encajan con DdM
- **linograbado** — grabado tipo Posada; cambiar paleta a negro/cempasúchil.
- **papel_recortado_popup** — base para papel picado/recortado.
- **claymation** — más cercano a papel maché/alebrije; pedir textura de papel engomado y pintura vibrante.
- **bordado** — textil de pueblo, ideal para tradiciones regionales.
- **satira_periodico** — calaveras literarias / prensa de Posada.
No hay ids `papel_mache` ni `alebrije`: proponer alta en estilos.json + prueba en salidas/estilos_test.

## Hooks que encadenan
- Cierre P1 → "El papel picado decora... pero ¿para quién se pone la ofrenda? Parte 2 hoy 19:00."
- Apertura P2 → "En la Parte 1 vimos el papel; ahora lo que va debajo."
- Cierre P2 → "Hay pueblos que no solo ponen ofrenda: sacan los huesos y los limpian. Parte 3 mañana."
- Apertura P3 → "Parte 3: en Pomuch los muertos salen de la tumba cada año."

## Consistencia visual
Mismo marco/título "Día de Muertos · Parte N", paleta fija cempasúchil + magenta + negro, cempasúchil como elemento recurrente de transición; cambia solo la técnica.
