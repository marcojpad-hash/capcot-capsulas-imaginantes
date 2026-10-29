# Kit de montaje CapCut para CAPCOT

Este kit convierte el manifiesto `CAPCUT_IMPORT.json` en dos archivos que CapCut Web/Desktop puede usar como apoyo de montaje:

- `CAPCUT_SUBTITULOS.srt`: subtítulos importables con marcas de tiempo estimadas.
- `CAPCUT_PLAN_MONTAJE.csv`: orden, tiempos, recurso, texto en pantalla, movimiento, narración y capas por escena.

## Alcance

No fabrica un borrador nativo de CapCut ni accede a APIs privadas. Las marcas de tiempo se distribuyen por número de palabras dentro de la duración declarada de cada escena; sirven como primer montaje y requieren revisión auditiva. Si el TTS produce marcas WordBoundary, deben reemplazar estas estimaciones.

## Uso

Desde la raíz del repositorio:

```bash
python3 scripts/exportar_capcut.py
```

Para otro manifiesto:

```bash
python3 scripts/exportar_capcut.py --input ruta/CAPCUT_IMPORT.json --out-dir ruta/salida
```

## Importación

1. Abre el editor web de CapCut y crea un proyecto vertical 9:16.
2. Importa los ocho archivos de imagen referidos por el manifiesto y colócalos en el orden del CSV con las duraciones indicadas.
3. Importa el audio de narración disponible y alinéalo desde el inicio. El manifiesto actual no contiene el archivo de audio.
4. En Subtítulos/Captions, importa `CAPCUT_SUBTITULOS.srt`; revisa cada bloque contra la narración y corrige los tiempos.
5. Añade la cortinilla de fuentes de seis segundos al final, incorpora música solo cuando exista el archivo con licencia registrada y revisa el audio completo.
6. Exporta 1080×1920, 30 fps. Reproduce el archivo exportado y verifica sincronía, fuentes, legibilidad y licencias antes de publicarlo.

**Estado de la cápsula del 28-oct:** el repositorio indica que las imágenes están en el ZIP de trabajo, no versionadas aquí; el MP4 y el audio final todavía no forman parte del paquete. Este kit prepara los archivos auxiliares de montaje, no sustituye esos medios.
