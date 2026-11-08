# Orquestador de CAPCOT

El coordinador que no se muere.

## Por qué existe

Copilot era el orquestador, pero su uso libre es limitado y se murió en ese
papel. No se puede depender de un modelo al que se le acaben los créditos
o los tokens. El orquestador nuevo es un modelo abierto con API gratuita,
así que no hay saldo que se agote.

## Qué es

Un script (`orquestador.py`) que lee el tablero de delegaciones y el
protocolo, se los pasa a un modelo abierto y escribe un reporte con qué
está atorado, quién debe qué a quién y cuál es el siguiente paso de cada
pendiente.

- Modelo: `openai/gpt-oss-120b`, pesos abiertos (Apache 2.0), por la API
  gratuita de Groq. La clave de Groq ya está conectada.
- No gasta tokens de Muse. Corre unas pocas veces al día, muy por debajo
  de los límites de velocidad de la API gratuita.

## Uso

```sh
python3 orquestador.py [--repo RUTA] [--salida RUTA] [--model MODELO]
```

- `--repo`: clon local de capcot-capsulas-imaginantes. Hace `git pull`
  si puede; si no, usa la copia local y lo dice en el reporte.
- `--salida`: dónde escribir el reporte (por defecto `./reporte.md`).
- `--model`: otro modelo de Groq si hace falta (por ejemplo
  `openai/gpt-oss-20b` o `qwen/qwen3.8-27b`, también abiertos).

## Límites honestos

- El modelo solo coordina con texto: lee el tablero y redacta el reporte.
  No abre issues ni sube archivos por sí solo; eso lo hace Pecas o el
  workflow del aviso, con lo que el reporte diga.
- El modelo puede leer mal una dirección (quién debe qué a quién) si el
  tablero no está claro. Por eso el prompt lleva las reglas del proyecto
  adentro: quién monta, quién sube workflows por navegador, quién crea
  las cuentas. Si el reporte se equivoca en algo, se corrige el tablero,
  no el modelo.
- La API gratuita tiene límites de velocidad por minuto y por día, pero
  no cobra ni se agota un saldo. Unas pocas corridas al día no llegan
  ni cerca.
