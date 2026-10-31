# Contrato de estado Grok — cola CAPCOT

## Propósito
El JSON de storyboard prueba que ChatGPT dejó una propuesta en GitHub. No prueba que Grok la haya recibido. Para eliminar esa ambigüedad, Grok registra un archivo de estado independiente.

## Ruta
Para el storyboard con project_id YYYY-MM-DD_slug, Grok crea y actualiza:

cola/estado/YYYY-MM-DD_slug.json

Plantilla: templates/grok_status.template.json.

## Estados permitidos
1. RECIBIDO_POR_GROK: Grok leyó brief y storyboard.
2. SELECCIONADO, DEVUELTO o RECHAZADO: decisión editorial explícita.
3. EN_PRODUCCION: assets en generación/edición.
4. QA_APROBADO o QA_RECHAZADO: resultado oficial con evidencia.
5. PUBLICADO: URL/ID y fecha/hora de publicación registradas.

No saltar estados sin explicar la razón. Una decisión editorial no equivale a QA; QA no equivale a publicación.

## Reglas de evidencia
- updated_at debe incluir zona horaria.
- checks solo cambia a true después de verificar cada punto.
- production.assets solo enumera archivos que realmente existen en el repositorio o en un destino verificable.
- qa.evidence contiene enlaces, logs o resultados observados; no frases como “todo bien”.
- publication.urls y published_at solo se llenan tras publicación confirmada.
- Si Grok aún no recibió la entrada, no crear un estado falso; la ausencia del archivo significa “recepción no confirmada”.

## Responsabilidades
- Grok crea y actualiza el estado.
- ChatGPT solo lo lee y lo audita; no puede declarar que Grok recibió o aceptó el paquete.
- El auditor CAPCOT crea el reporte CONTROL_COLA, pero no modifica el estado de Grok ni toma la decisión editorial.
