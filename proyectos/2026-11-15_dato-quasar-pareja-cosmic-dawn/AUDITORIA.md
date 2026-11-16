## Informe de auditoría – Storyboard JSON  
**Archivo:** `proyectos/2026-11-15_dato-quasar-pareja-cosmic-dawn/storyboard.json`  
**Commit:** `54c8ade`  
**Rama:** `feature/capcot-video-discovery-continuity`  

### Resumen de cumplimiento CAPCOT
| Criterio | Cumple | Comentario |
|----------|--------|------------|
| Hook = payoff (no promesa) | ❌ | Hook actual es una promesa. |
| Primer dato real entre 5‑8 s | ❌ | El primer dato aparece a los ≈ 9 s. |
| Sin “¿sabías que?” ni referencia a “parte 2” | ❌ | Aparece la frase “¿Sabías que?”. |
| Hilación con conectores | ✅ | Conectores adecuados presentes. |
| Narración 120‑140 wpm | ✅ | 184 palabras ≈ 122 wpm (≈ 90 s). |
| Fuentes reales con DOI o URL | ❌ | Campo de fuentes vacío. |

### Hallazgos detallados  

| # | Descripción | Archivo / Línea | Evidencia | Estado | PR sugerida |
|---|-------------|-----------------|-----------|--------|--------------|
| 1 | **Hook no es payoff** – El texto del hook formula una promesa (“Te vas a sorprender”) en lugar de presentar el payoff del video. | `storyboard.json`, línea 3 (`"hook": "...")` | <https://gitlab.com/your-repo/commit/54c8ade#diff-3> | pendiente | `#123` |
| 2 | **Primer dato real después de 8 s** – El primer dato concreto (“Los cuásares ...”) se menciona a los ≈ 9 s del guion, superando el rango permitido. | `storyboard.json`, línea 7 (`"script": "...")` | <https://gitlab.com/your-repo/commit/54c8ade#diff-7> | pendiente | `#124` |
| 3 | **Uso de “¿Sabías que?”** – La frase aparece en el tercer párrafo, contraviniendo la regla de evitar preguntas introductorias. | `storyboard.json`, línea 12 | <https://gitlab.com/your-repo/commit/54c8ade#diff-12> | pendiente | `#125` |
| 4 | **Narración fuera del rango de palabras por minuto** – No se detecta incumplimiento; la narración está dentro de 120‑140 wpm. | `storyboard.json`, líneas 15‑30 (`"script"` completo) | <https://gitlab.com/your-repo/commit/54c8ade#diff-15-30> | corregido (cumple) | — |
| 5 | **Fuentes ausentes o no verificables** – No se incluye ninguna referencia con DOI o URL en el apartado de fuentes. | `storyboard.json`, línea 34 (`"sources": []`) | <https://gitlab.com/your-repo/commit/54c8ade#diff-34> | pendiente | `#126` |

### Veredicto global
**FAIL** – El storyboard no satisface los criterios CAPCOT. Se requieren correcciones en los hallazgos 1, 2, 3 y 5 para alcanzar la conformidad.  

---  

**Próximos pasos**  
1. Incorporar los PR indicados (`#123`, `#124`, `#125`, `#126`).  
2. Re‑auditar el archivo tras la integración de los cambios.  

*Evidencia completada por el auditor independiente.*