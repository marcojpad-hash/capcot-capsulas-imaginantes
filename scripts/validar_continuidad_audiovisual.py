#!/usr/bin/env python3
"""Strict CAPCOT audiovisual continuity checks for storyboard JSON.

This validator is intentionally separate from validar_storyboard.py until the
schema migration is approved. It does not claim to perform semantic image/audio
review; it checks declared identity, language, prompt consistency and assets.
"""
import json
import sys
from pathlib import Path

REQUIRED_VISUAL = (
    "style_id", "style_name", "prompt_base", "palette",
    "lighting", "texture", "composition", "negative_prompt",
)
REQUIRED_TYPE = (
    "font_family", "font_weight", "title_style",
    "subtitle_style", "hierarchy", "animation",
)

def nonempty(obj, key):
    return isinstance(obj, dict) and bool(str(obj.get(key, "")).strip())

def validar(path):
    errors, warnings = [], []
    path = Path(path)
    try:
        sb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"No se pudo leer JSON: {exc}"], []

    visual = sb.get("visual_identity")
    typography = sb.get("typography_identity")
    voice = sb.get("voice")
    if not isinstance(visual, dict):
        errors.append("falta visual_identity (biblia visual maestra)")
        visual = {}
    if not isinstance(typography, dict):
        errors.append("falta typography_identity")
        typography = {}
    if not isinstance(voice, dict):
        errors.append("falta voice")
        voice = {}

    for key in REQUIRED_VISUAL:
        if not nonempty(visual, key):
            errors.append(f"visual_identity.{key} vacío o ausente")
    for key in REQUIRED_TYPE:
        if not nonempty(typography, key):
            errors.append(f"typography_identity.{key} vacío o ausente")

    if sb.get("language") != "es-MX":
        errors.append("language debe ser exactamente es-MX")
    expected_voice = {
        "engine": "edge-tts",
        "voice_id": "es-MX-JorgeNeural",
        "rate": "+7%",
        "pitch": "-2Hz",
    }
    for key, expected in expected_voice.items():
        if voice.get(key) != expected:
            errors.append(f"voice.{key} debe ser {expected!r}; recibido {voice.get(key)!r}")
    if voice.get("language", "es-MX") != "es-MX":
        errors.append("voice.language debe ser es-MX")

    scenes = sb.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        errors.append("scenes debe ser una lista no vacía")
        scenes = []

    style_id = visual.get("style_id")
    prompt_base = visual.get("prompt_base")
    seen_assets = set()
    approved_assets = sb.get("approved_assets")
    approved_names = None
    if not isinstance(approved_assets, list) or not approved_assets:
        errors.append("approved_assets debe declarar explícitamente todos los recursos visuales autorizados")
    else:
        approved_names = {
            item.get("filename") for item in approved_assets
            if isinstance(item, dict) and item.get("filename")
        }
        if len(approved_names) != len(approved_assets):
            errors.append("approved_assets contiene elementos inválidos o filenames duplicados")
    if not isinstance(typography.get("font_family"), str):
        errors.append("font_family debe ser una cadena única para toda la cápsula")

    for index, scene in enumerate(scenes, 1):
        sid = scene.get("id", f"scene_{index:03d}") if isinstance(scene, dict) else f"scene_{index:03d}"
        if not isinstance(scene, dict):
            errors.append(f"{sid}: escena no es objeto")
            continue
        scene_style = scene.get("style_id", style_id)
        if style_id and scene_style != style_id:
            errors.append(f"{sid}: style_id distinto de la biblia visual")
        prompt = scene.get("image_prompt", "")
        if prompt_base and (not isinstance(prompt, str) or not prompt.startswith(prompt_base)):
            errors.append(f"{sid}: image_prompt no comienza con prompt_base exacto")
        filename = scene.get("asset_filename")
        if not filename:
            errors.append(f"{sid}: falta asset_filename")
        elif filename in seen_assets:
            errors.append(f"{sid}: asset_filename duplicado: {filename}")
        else:
            seen_assets.add(filename)
        if approved_names is not None and filename not in approved_names:
            errors.append(f"{sid}: recurso no declarado en approved_assets: {filename}")
        for field in ("narration", "on_screen_text"):
            value = scene.get(field, "")
            if value and not isinstance(value, str):
                errors.append(f"{sid}: {field} debe ser texto")
        if scene.get("text_language", "es-MX") != "es-MX":
            errors.append(f"{sid}: text_language debe ser es-MX")
        if scene.get("voice_id", "es-MX-JorgeNeural") != "es-MX-JorgeNeural":
            errors.append(f"{sid}: voz distinta de la voz maestra")
        scene_typography = scene.get("typography_identity")
        if scene_typography is not None and scene_typography != typography:
            errors.append(f"{sid}: identidad tipográfica sobrescribe la biblia maestra")
        extra_assets = scene.get("additional_images", []) or scene.get("extra_assets", [])
        if extra_assets:
            extra_names = {
                item.get("filename") if isinstance(item, dict) else item
                for item in extra_assets
            }
            if approved_names is None or not extra_names.issubset(approved_names):
                errors.append(f"{sid}: contiene imágenes adicionales no autorizadas")

    if approved_names is not None:
        unused = approved_names - seen_assets
        if unused:
            warnings.append("Recursos aprobados no usados: " + ", ".join(sorted(unused)))

    if not isinstance(visual.get("reference_assets", []), list):
        errors.append("visual_identity.reference_assets debe ser una lista")
    if not visual.get("seed_policy"):
        errors.append("visual_identity.seed_policy ausente")

    return errors, warnings

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 scripts/validar_continuidad_audiovisual.py <storyboard.json>")
        return 2
    errors, warnings = validar(sys.argv[1])
    for item in warnings:
        print("AVISO:", item)
    for item in errors:
        print("ERROR:", item)
    print("PASS ESTRUCTURAL" if not errors else f"FAIL ({len(errors)} errores)")
    if not errors:
        print("NOTA: la continuidad estética real, OCR y voz requieren revisión audiovisual.")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
