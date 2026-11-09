# CAPCOT — revisión de pendientes y disponibilidad
**Fecha de corte:** 2026-11-09, 01:26 America/Mexico_City  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**HEAD revisado:** `7fa0b0097d9d95c8a5ca0f69b382126a1ed94887`  
**Alcance:** revisión de pendientes operativos, staging, handoff, Actions, PR y documentación. Sin producción de medios, dispatch, publicación, gasto de créditos ni cambios a datos/workflows/estados de Grok.

## 1. Dictamen

**NO ESTÁ TODO LISTO.** Hay avances verificables en TTS y en el diseño del buzón gratuito de Grok, pero el handoff aún no está demostrado, el workflow no acepta el formato de paquete que actualmente existe en cola, los storyboards 5–7 nov siguen bloqueados y el PR #3 no está listo para integrar.

El último commit de la rama es el control de cola del 8-nov. No hay commits posteriores ni entregables del 9-nov en el árbol revisado.

## 2. Inventario actual

- `proyectos/`: conserva los doce storyboards canónicos del lote 5–7 nov y numerosos artefactos históricos. No existe proyecto con prefijo `2026-11-08` ni `2026-11-09`.
- `docs/briefs/`: existen RADAR y CONTROL_COLA hasta el 8-nov. No existe RADAR ni CONTROL_COLA del 9-nov.
- `cola/entrada/`: una carpeta anidada, `2026-11-07_dato-clavo-te-cocina/`, con storyboard, fuentes y estado documental. Es el slot 23:30 del 7-nov, ya cubierto/programado según los documentos del 8-nov. **Esta carpeta no cumple el formato canónico de handoff** (`cola/entrada/<project_id>.json`) y no debe redispatcharse.
- `cola/estado/`: no contiene estados de Grok.
- `handoffs/grok_inbox/`: solo contiene README; no hay marcadores `<project_id>.json`.
- `handoffs/grok_done/`: solo contiene `.gitkeep`; no hay confirmaciones de finalización.

La existencia de la carpeta del dato de clavo no confirma recepción por Grok ni autoriza una segunda producción.

## 3. Lote obligatorio 5–7 nov

El último control, del 8-nov, registró estos valores de narrative_qa. No se encontraron commits posteriores que cambien los storyboards del lote:

| Proyecto | QA narrativo registrado |
|---|---:|
| 2026-11-05_kids-dia-en-venus | PASS 88 |
| 2026-11-05_comida-palomitas | FAIL 82 |
| 2026-11-05_inter-arboles-se-comunican | FAIL 78 |
| 2026-11-05_inter-rayo-globular | FAIL 81 |
| 2026-11-06_kids-ballena-azul-corazon | FAIL 80 |
| 2026-11-06_comida-aguacate-negro | FAIL 79 |
| 2026-11-06_inter-ranas-congeladas | FAIL 83 |
| 2026-11-06_inter-arena-cantante | PASS 94 |
| 2026-11-07_kids-huesos-bebe | FAIL 82 |
| 2026-11-07_comida-hielo-caliente | FAIL 81 |
| 2026-11-07_inter-pulpo-suenos | FAIL 80 |
| 2026-11-07_inter-nubes-pesan | FAIL 78 |

Estos son los valores del último reporte releído, no una nueva lectura narrativa ejecutada a las 01:26 del 9-nov.

Bloqueo estructural reportado: 0/12 aptos; faltan seis campos narrativos obligatorios en las 85 escenas (510 campos). Árboles tiene 169 palabras y carece de mapa y dato/gráfico. Los dos PASS narrativos tampoco pueden promocionarse por estructura. No se reescribieron narraciones ni claims.

## 4. Handoff Grok: diseño implementado, ejecución no demostrada

El documento `ajustes_entre_modelos/2026-11-02_GROK_HANDOFF_SIN_WEBHOOK.md` describe el flujo gratuito: Actions escribe un marcador en `handoffs/grok_inbox/<id>.json`; Grok/Imaginantes lo lee y, al terminar, lo mueve a `handoffs/grok_done/` y actualiza su estado.

**Corrección tras releer el contrato operativo y el QA narrativo obligatorios:** el workflow no presenta un defecto de rutas respecto del formato canónico vigente. El contrato exige que el auditor independiente promueva únicamente un JSON aprobado a `cola/entrada/<project_id>.json`; el workflow escucha y procesa precisamente esos archivos de primer nivel. La carpeta `cola/entrada/2026-11-07_dato-clavo-te-cocina/` es un formato heredado/no conforme, no una razón para ampliar el workflow y saltarse el contrato.

El paquete de clavo está marcado `PREPARADO_PENDIENTE_REVISION_GROK`, pero no contiene evidencia de `narrative_qa.status=PASS` ni de la revisión independiente requerida. El validador exige además `narrative_contract`, `narrative_qa` y otros campos estructurales. Por tanto, no se debe convertir ni enviar automáticamente ese paquete. La acción correcta es mantenerlo sin dispatch hasta que un auditor independiente haga la lectura en frío y el validador estructural dé PASS; si falla, debe preservarse y trasladarse a bloqueados conforme al contrato.

**Evidencia de ejecución:**
- No hay marcadores en inbox ni done.
- No hay estados individuales en `cola/estado/`.
- Último run del workflow de dispatch: run 41306776689, 1-nov, fallo en el paso «Verificar configuración del receptor»; el paso de entrega fue omitido.
- Ese run es anterior a la versión actual del workflow, que ya escribe el marcador gratuito antes del webhook opcional. No existe un run posterior del dispatch que pruebe la nueva ruta.
- Último run global visible: TTS smoke run 42447536352, 8-nov 04:37 UTC, SUCCESS.

Resultado: **RECEPCION_GROK_NO_CONFIRMADA** para cualquier paquete sin estado individual. No se crearon ni modificaron estados de Grok y no se disparó Actions.

## 5. TTS y pruebas

El workflow `.github/workflows/tts-tooling-smoke.yml` terminó SUCCESS el 8-nov. Pasaron checkout, instalación de Edge TTS, compilación de `tools/tts/narrate.py`, CLI `--help` y comprobación de manifiestos de dependencias.

Esto verifica que el cliente TTS compila y que su interfaz responde; **no** demuestra generación de voz, audio final ni integración audiovisual. No se generó audio.

No hubo runtime local para ejecutar `validar_storyboard.py`, `procesar_cola.py` ni la suite completa en esta revisión. La validación de esos componentes es estática; el smoke TTS sí fue ejecutado en GitHub Actions.

## 6. PR #3: no listo para merge

PR [#3](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/pull/3):
- Abierto y en estado Draft.
- Head = HEAD de esta rama; base = `main`.
- En el corte inicial del informe: 586 archivos cambiados; 57,587 adiciones y 1,683 eliminaciones. Tras los commits documentales de esta revisión, GitHub informa 587 archivos, 57,705 adiciones y 1,683 eliminaciones.
- GitHub reporta `mergeable=false`.
- El diff incluye diez archivos `data/*.json`, además de numerosos `_tmp/` logs/scripts y artefactos históricos.

Los cambios a `data/*.json` contradicen el contrato operativo vigente, que prohíbe a ChatGPT modificarlos. El propio cuerpo del PR ya identifica este bloqueo y pide restaurar esos registros desde la fuente operativa o separarlos antes del merge. No se modificó ni se aprobó el PR.

## 7. Pendientes heredados y clasificación

| Pendiente | Estado |
|---|---|
| QA estructural/narrativo de los doce proyectos 5–7 nov | ABIERTO |
| Handoff gratuito: primera ejecución que cree marcadores | NO DEMOSTRADO |
| Consumo/acuse por Grok y movimiento a grok_done | NO CONFIRMADO |
| Compatibilidad workflow con paquetes anidados | BLOQUEO DE CÓDIGO |
| Estados individuales de Grok | AUSENTES |
| Radar/brief y horario específico del 9-nov | AUSENTES en HEAD revisado |
| PR #3 limpio y listo para merge | BLOQUEADO; incluye data/*.json y artefactos temporales |
| Revisión de APIs comerciales Krea/Runway y credenciales | OPCIONAL/PENDIENTE; no bloquea el flujo textual ni el handoff gratuito |
| Muse: permiso Contents: Read and write en CAPCOT | PENDIENTE DE VERIFICACIÓN; no se cambió ningún permiso |
| Prototipo integral storyboard→MP4 y QA audiovisual automatizado | NO DEMOSTRADO por el smoke TTS |

## 8. Qué significa «listo»

Para declarar CAPCOT operativo de extremo a extremo aún hacen falta, como mínimo:
1. Aplicar el formato canónico ya definido: solo promover a `cola/entrada/<project_id>.json` después de QA narrativo independiente PASS y validación estructural PASS; no ampliar el workflow para admitir carpetas heredadas.
2. Ejecutar una prueba controlada de handoff que produzca un marcador verificable en inbox; después Grok debe leerlo y registrar su estado conforme al contrato.
3. Corregir los doce storyboards y volver a pasar las compuertas narrativa y estructural; no promover los dos PASS narrativos hasta que también pasen estructura.
4. Separar/restaurar los cambios prohibidos a `data/*.json` y limpiar artefactos no destinados al PR antes de considerar el merge.
5. Confirmar el permiso de escritura de Muse por separado; no confundir el permiso del usuario conectado con el de la app Muse.

## 9. Integridad y límites de esta revisión

No se generaron cápsulas, frames, imágenes, voz, audio, video ni renders. No se publicó, programó, disparó workflow, envió payload externo ni consumió créditos. No se modificaron `data/*.json`, `main`, workflows, secretos, permisos, estados de Grok, storyboards del lote ni decisiones editoriales.

No se revisaron APIs por no haber identificado en esta pasada un cambio oficial nuevo que justificara esa comprobación. No se ejecutó la suite local por ausencia de runtime. El inventario corresponde al HEAD indicado y puede cambiar si otro actor hace commits después del corte.

## 10. Corrección de diagnóstico — revisión de contratos

La primera lectura describió la diferencia entre la carpeta anidada y el selector del workflow como un defecto del workflow. Esa conclusión queda **reemplazada**: al leer `docs/CONTRATO_OPERATIVO_UNIFICADO.md`, `docs/QA_NARRATIVO_EN_FRIO.md` y `scripts/validar_storyboard.py`, se confirma que el formato autorizado es un archivo JSON plano en `cola/entrada/<project_id>.json`, y que la promoción depende de QA independiente PASS. El workflow actual se alinea con ese contrato. La carpeta anidada de clavo no está habilitada para dispatch y carece de evidencia de aprobación narrativa; no se debe modificar el workflow para aceptarla.

No se cambió el workflow, la cola, el storyboard ni los estados Grok. Esta corrección es documental y evita un cambio técnico que habría relajado indebidamente la compuerta editorial.