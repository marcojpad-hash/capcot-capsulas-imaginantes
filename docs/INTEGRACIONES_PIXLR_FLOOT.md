# Integraciones visuales: Pixlr y Floot

**Verificación:** 2026-11-06  
**Repositorio:** CAPCOT / Datos y ociosidades  
**Rama:** `feature/capcot-video-discovery-continuity`

Este documento registra dos herramientas complementarias. No afirma que exista una integración API entre ellas ni que se haya creado un proyecto de producción.

## Dictamen operativo

| Herramienta | Uso útil en CAPCOT | Gratis: dictamen | Conexión disponible |
|---|---|---|---|
| Pixlr | Edición de imágenes, recorte, eliminación de fondo/objetos, capas, composición y generación puntual de imágenes o clips | Editor básico: sí, con anuncios y límites. IA: cuota gratuita pequeña/no garantizada; no contar con video gratis recurrente | Uso web/Android manual. No se encontró conector MCP ni API de Pixlr habilitada en esta sesión |
| Floot | Construir utilidades web internas: tablero de producción, registro de activos, revisión de paquetes, formularios y pequeñas herramientas de operación | Construcción: 100 acciones/día en Free. No incluye créditos de IA ni asignación de hosting mensual en la tabla de precios. La documentación sí describe subdominio Floot gratuito; confirmar condiciones de publicación antes de depender de ello | Conector Floot MCP disponible en ChatGPT. Cuenta consultada: todavía sin proyectos |

## 1. Pixlr

Enlaces oficiales:
- [Editor Pixlr](https://pixlr.com/es/)
- [Generador de vídeo](https://pixlr.com/es/video-generator/)
- [Precios](https://pixlr.com/es/pricing/)
- [Google Play / Android](https://play.google.com/store/apps/details?id=com.pixlr.express)

Capacidades anunciadas:
- Editor de imágenes y diseño en navegador, móvil y escritorio.
- Generación de imágenes y edición asistida por IA.
- Texto a vídeo e imagen a vídeo; exportación MP4 y formato vertical 9:16.
- Herramientas de eliminación de fondo/objetos, relleno y expansión generativa.

Límites y cautelas:
- La página de vídeo anuncia uso gratuito, pero el precio de cada modelo se expresa en créditos. El sitio no publica en su tabla de planes una asignación mensual Free comparable a Plus/Premium.
- La tabla oficial consultada muestra Plus a USD 2.49/mes con 80 créditos mensuales (estimación oficial: ~4 vídeos Fast) y Premium a USD 9.99/mes con 1,000 créditos (estimación: ~50 vídeos Fast). Precios sujetos a cambio y región.
- La investigación externa de cuentas gratuitas encontró una asignación inicial de 10 créditos; sirve para unas pocas imágenes económicas, no para los modelos de vídeo revisados. Es evidencia externa, no garantía contractual de Pixlr.
- La respuesta del desarrollador en Google Play indica tres guardados diarios en la versión Android gratuita. No extrapolar ese límite a la web.
- No asumir que “generador gratuito” equivale a vídeo ilimitado ni iniciar una generación que muestre costo en créditos sin autorización.

Uso recomendado:
1. Preparar y corregir imágenes de referencia, mapas, recortes y elementos gráficos.
2. Usar generación de imagen solo cuando la cuota visible de la cuenta sea suficiente.
3. Considerar imagen-a-vídeo/texto-a-vídeo como prueba excepcional, no como capacidad gratuita recurrente.
4. Antes de generar, registrar modelo, duración, resolución, relación de aspecto, créditos mostrados y saldo posterior.
5. Descargar el archivo y conservarlo en la carpeta de assets del proyecto solo después de comprobar calidad, licencia/condiciones de uso y procedencia.

Pixlr no se conecta automáticamente con GitHub ni con Floot en la configuración verificada. El paso de archivos es manual.

## 2. Floot

Enlaces:
- [Precios oficiales](https://floot.com/es/pricing)
- [Cómo funciona Floot](https://floot.com/docs/getting-started/how-floot-works)

Capacidades útiles:
- Crear aplicaciones web full-stack con frontend, endpoints, Postgres, autenticación y almacenamiento.
- Construir y modificar proyectos desde ChatGPT mediante el conector Floot.
- Leer/escribir archivos del proyecto, ejecutar pruebas y revisar errores.
- Crear herramientas internas que apoyen CAPCOT sin tocar el motor U6.

Plan Free verificado en la página oficial:
- 100 acciones de construcción por día.
- Sin créditos de IA mensuales.
- La tabla de precios no asigna presupuesto mensual de hosting al plan Free.
- La documentación explica que existe publicación en subdominio `.floot.app`; sin embargo, la tabla de precios muestra hosting como no incluido en Free. Por esa discrepancia, no depender de publicación/hosting gratuito sin comprobarlo en la cuenta y en el momento de publicar.
- Las tareas programadas de una app publicada requieren que el propietario tenga plan de pago.
- Generación de imágenes dentro de Floot, funciones de IA de la app y chat con modelos de Floot consumen créditos. No usarlos bajo la suposición de que son gratuitos.

Estado de cuenta consultado por el conector el 2026-11-06: **no hay proyectos Floot todavía**. El conector está disponible; eso no significa que exista ya una app CAPCOT.

Uso recomendado:
- Free para prototipos y utilidades internas de bajo consumo de acciones.
- No activar servicios de IA, generación de imágenes, pagos, hosting de producción ni tareas programadas de pago sin autorización explícita.
- Si se decide crear una app CAPCOT, primero definir un alcance pequeño y aislado (por ejemplo, un tablero de activos y enlaces), construir con datos de prueba y verificar antes de cargar datos reales.
- No copiar secretos, tokens ni credenciales a GitHub. Usar el gestor de credenciales de Floot cuando corresponda.

## 3. Flujo de trabajo propuesto

1. CAPCOT conserva en GitHub el storyboard textual, fuentes, IDs y estado editorial.
2. Pixlr se usa manualmente para editar/generar recursos visuales cuando la cuota visible lo permita.
3. El activo exportado se revisa y se entrega a la etapa de producción correspondiente; no se inventan rutas ni se declara un medio como generado antes de tener el archivo.
4. Floot puede alojar una herramienta auxiliar para catalogar activos, enlazar storyboards y registrar revisiones. No sustituye GitHub como fuente de verdad ni sustituye el pipeline de producción.
5. Cualquier paso con costo, crédito, publicación, exposición pública o cambio irreversible requiere autorización específica.

## 4. Límites de integración comprobados

- **Pixlr ↔ GitHub:** no hay integración directa verificada; transferencia manual.
- **Pixlr ↔ Floot:** no hay integración directa verificada; transferencia manual.
- **ChatGPT ↔ Floot:** conector MCP disponible y operativo; cuenta sin proyectos al momento de la consulta.
- **ChatGPT ↔ Pixlr:** no hay conector/API de Pixlr habilitado en esta sesión. Se puede preparar el prompt y el procedimiento, pero la generación/edición se realiza en la interfaz de Pixlr.

## 5. Registro de pruebas

| Fecha | Prueba | Resultado |
|---|---|---|
| 2026-11-06 | Consultar precios y límites oficiales Pixlr | Hecho; cuota Free de IA no especificada en la tabla oficial |
| 2026-11-06 | Contrastar generador de vídeo Pixlr | Anuncia acceso gratuito, pero los modelos consumen créditos; no se verificó un saldo Free suficiente para vídeo |
| 2026-11-06 | Consultar plan Floot Free | Hecho; 100 acciones/día, 0 créditos IA/mes y hosting mensual no incluido en tabla |
| 2026-11-06 | Consultar proyectos Floot de la cuenta | Hecho; no hay proyectos |
| 2026-11-06 | Generar medios o crear app | No ejecutado; no se consumieron créditos ni se creó proyecto |

## 6. Regla de actualización

Antes de recomendar pago o prometer capacidad gratuita, volver a comprobar precios, cuota visible de la cuenta y condiciones de publicación. La documentación pública puede cambiar. Mantener este archivo como registro de capacidades, no como autorización automática de gasto o publicación.
