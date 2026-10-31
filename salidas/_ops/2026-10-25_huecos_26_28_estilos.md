# Huecos 26–28 oct + estilos (pedido Mj pt160u, 25-oct ~21:50 CDMX)

## Huecos
| Fecha | Ya cubierto | Faltan |
|---|---|---|
| 26-oct | P1 papel picado 14:30 · Catrina 17:00 · P2 19:00 · ave 21:00 | **+1** |
| 27-oct | P3 Pomuch 19:00 | **+2** |
| 28-oct | P4 Templo Mayor 19:00 | **+2** |

## Visual
- **Animación tipo Flash: DESCARTADA** (Mj: sin animación real queda "pegote").
- **Grafiti** → ya existe `grafiti_colorido` (mural spray saturado). También `stencil_banksy` (más sobrio). No hace falta id nuevo; opcional variante `grafiti_ddm` (calaveras wildstyle, paleta magenta/cempasúchil).
- **Mosaico literal** → NO existe. Lo más cercano: `vitral` (vidrio+plomo, no teselas). **Proponer `mosaico`.**
- **Litografía azul-dorado** → NO existe con ese nombre. Cercanos: `linograbado` (índigo+ocre, tallado), `risografia`. **Proponer `litografia_azul_dorado`** (o formalizarlo como alias si Mj ya lo usa como variante de linograbado).

### Estilos nuevos propuestos (NO añadidos aún a scripts/estilos.json; esperan OK)
```json
"mosaico": {
  "nombre": "Mosaico literal (propio)",
  "descripcion": "Teselas de piedra/vidrio/cerámica con juntas visibles, tipo mural mosaico mexicano.",
  "prompt_base": "literal tile mosaic mural, small irregular ceramic and stone tesserae with visible grout lines, rich mineral colors, slightly uneven surface catching light, vertical 9:16, no text",
  "temas": "murales, arqueología, ciudad, historia"
},
"litografia_azul_dorado": {
  "nombre": "Litografía azul-dorado",
  "descripcion": "Litografía bitono azul cobalto/prusia con acentos dorados metálicos sobre papel crema.",
  "prompt_base": "vintage stone lithograph print, two-tone deep prussian blue ink with metallic gold accents on cream paper, fine crayon grain texture, elegant crosshatching, vertical 9:16, no text",
  "paleta": "azul prusia, dorado, crema",
  "temas": "historia, ciencia, retratos, DdM"
}
```

## 5 ángulos propuestos (TBD; datos a VERIFICAR con fuente antes de guion)
| # | Slot | Estilo | Ángulo |
|---|---|---|---|
| A | 26-oct 12:00 | `grafiti_colorido` | **Calaveras en la calle**: del desfile de CDMX (nació tras la película *Spectre*, 2015) a murales de calaveras — cómo una ficción creó tradición. Cifra a verificar: asistencia desfile 2025. |
| B | 27-oct 14:30 | `mosaico` | **Muertos en mosaico**: murales-mosaico de Ciudad Universitaria (Biblioteca Central, O'Gorman: piedras naturales de colores de todo México) — memoria y muerte en piedra. |
| C | 27-oct 17:00 | `litografia_azul_dorado` | **Ciencia del cempasúchil**: por qué es naranja (carotenoides/luteína, uso industrial en alimento de aves) y por qué "guía" a los muertos. Dato fresco: producción 2026 (SIAP/SADER) a verificar. |
| D | 28-oct 14:30 | `grafiti_colorido` (o `stencil_banksy`) | **Mariposa monarca = almas que regresan**: llegan ~1-2 nov; dato fresco: superficie hibernación temporada 2025-26 (WWF/CONANP) a verificar. |
| E | 28-oct 17:00 | `litografia_azul_dorado` | **Pan de muerto: los "huesos" y la lágrima** — simbolismo + química del azahar/horneado; cifra consumo/precio 2026 (Profeco) a verificar. Alternativa: `mosaico` para Mictlán y sus 9 niveles. |

Rotación: evita repetir estilo el mismo día y evita chocar con P3 (`bordado`) / P4 (`codex_mexica`).

## Pendiente
- OK de Mj a ángulos/horas (horas tentativas) y a añadir 2 estilos en `scripts/estilos.json`.
- Sin video generado.
