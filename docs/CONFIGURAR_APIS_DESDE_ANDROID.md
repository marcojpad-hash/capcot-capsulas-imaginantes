# Activar las APIs de Krea y Runway desde Android

No compartas claves API en el chat ni las pegues en archivos del repositorio. Las claves deben quedar como secretos de GitHub.

## 1. Krea API

1. Abre https://www.krea.ai/app/api/pricing en Chrome.
2. Inicia sesión y entra en **API Tokens**.
3. Crea un token API y añade saldo solo cuando decidas hacer la primera prueba.
4. Copia el token en un gestor seguro; no lo envíes por mensaje.

## 2. Runway Dev API

1. Abre https://dev.runway.com/ e inicia sesión.
2. Entra al área de desarrolladores y crea una API key.
3. Añade créditos de Runway Dev cuando decidas probar una edición.
4. Conserva la clave en un gestor seguro. El saldo de Runway Dev es independiente de los créditos de la aplicación Runway.

## 3. Guardar las claves en GitHub

1. Abre https://github.com/marcojpad-hash/capcot-capsulas-imaginantes en Chrome.
2. Entra en **Settings → Secrets and variables → Actions**.
3. Pulsa **New repository secret** y crea:
   - Nombre: `KREA_API_KEY`; valor: token de Krea.
   - Nombre: `RUNWAYML_API_SECRET`; valor: API key de Runway Dev.
4. Guarda cada secreto. GitHub no vuelve a mostrar el valor después de guardarlo.

Si la interfaz móvil no muestra Settings, abre el menú de Chrome (⋮) y activa **Sitio para computadora**.

## 4. Qué se habilita al guardarlas

- Krea 3: edición de imágenes existentes con referencias y regiones.
- Krea Seedance 2.5: generación de clips de 4–30 segundos y edición guiada con video de referencia.
- Runway Bria FIBO Edit 1.5: edición de 1–4 imágenes de referencia.
- Runway Aleph 2.0: edición de clips existentes de 2–30 segundos.

## 5. Control de gasto

Los scripts no generan nada automáticamente al encontrar las claves. Cada llamada de edición/generación debe solicitarse explícitamente y puede cobrar saldo. Primero haremos una prueba de una sola imagen, revisaremos el resultado y luego una prueba de video de pocos segundos. El pipeline no debe enviar una cápsula completa a un modelo antes de aprobar esas dos pruebas.

No guardes tokens en el storyboard, JSON, ZIP, commits, variables públicas ni capturas de pantalla.
