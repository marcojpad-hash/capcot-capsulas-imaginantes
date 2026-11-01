# Cola bloqueada — CAPCOT

Esta carpeta conserva paquetes retirados de `cola/entrada/` porque no acreditaban la compuerta narrativa independiente.

## Regla de reingreso

Un storyboard solo puede regresar a `cola/entrada/YYYY-MM-DD_slug.json` cuando:
- contiene `narrative_contract` completo: `central_question`, `promise`, `stakes`, `scientific_turn`, `evidence_limit`, `payoff`;
- un revisor distinto del redactor hizo lectura en frío solo de la narración concatenada;
- contiene `narrative_qa.status=PASS`, score >=85, siete checks true, `review_basis=lectura_en_frio_solo_narracion` y `critical_flags=[]`;
- supera el validador estructural.

Contrato: `docs/QA_NARRATIVO_EN_FRIO.md`.

## Movimientos verificados — 2026-11-01

- Commit `057474c747202e164c28d3cf2f54c3196d55ca9f`: cuatro paquetes asignados a slots del 1-nov; 15 archivos movidos, SHA de blob conservado.
- Commit `3795f40cd035a8293efed759a2af1b5d58ef1ef0`: 29 project_id adicionales de cola histórica/futura; 101 archivos movidos, SHA de blob conservado.
- Total: 33 project_id y 116 archivos conservados. No se reescribieron narraciones ni fuentes.
- La comprobación posterior encontró cero storyboards en `cola/entrada/`. Los estados `cola/estado/` no se tocaron; recepción de Grok sigue sin confirmación donde no existe acuse.

Los movimientos son reversibles: el contenido se conserva bajo `cola/bloqueados/`; no se descartaron archivos.
