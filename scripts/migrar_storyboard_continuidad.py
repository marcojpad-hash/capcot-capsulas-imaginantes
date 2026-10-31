#!/usr/bin/env python3
"""Create a temporary continuity-ready copy of a legacy CAPCOT storyboard."""
import argparse
import hashlib
import json
from pathlib import Path

def migrate(source: Path, output: Path, styles_path: Path):
    sb = json.loads(source.read_text(encoding="utf-8"))
    styles = json.loads(styles_path.read_text(encoding="utf-8"))
    style_id = sb.get("estilo_id") or sb.get("style_id")
    style = styles.get(style_id)
    if not style:
        raise ValueError(f"El estilo {style_id!r} no existe en scripts/estilos.json")
    prompt_base = style.get("prompt_base")
    if not prompt_base:
        raise ValueError(f"El estilo {style_id!r} no tiene prompt_base")

    project_id = sb.get("project_id", source.stem)
    seed = int(hashlib.sha256(project_id.encode("utf-8")).hexdigest()[:8], 16)
    approved = []
    seen = set()
    for scene in sb.get("scenes", []):
        filename = scene.get("asset_filename")
        if filename and filename not in seen:
            approved.append({"filename": filename, "type": "scene_frame", "scene_id": scene.get("id")})
            seen.add(filename)
        layer = scene.get("capa")
        if isinstance(layer, dict):
            layer_name = layer.get("asset_filename")
            if layer_name and layer_name not in seen:
                approved.append({"filename": layer_name, "type": "scene_layer", "scene_id": scene.get("id")})
                seen.add(layer_name)
        scene["style_id"] = style_id
        scene["text_language"] = "es-MX"
        scene["voice_id"] = (sb.get("voice") or {}).get("voice_id", "")

    title_style = sb.get("titulo_estilo") or {}
    title_font = Path(title_style.get("font", "Alfa Slab One")).name
    sb["visual_identity"] = {
        "style_id": style_id,
        "style_name": style.get("nombre", sb.get("estilo_visual", style_id)),
        "prompt_base": prompt_base,
        "palette": style.get("paleta") or "Paleta por fijar en la biblia de estilo",
        "lighting": "Luz difusa neutra y consistente entre escenas; cualquier variación debe justificarse en el storyboard.",
        "texture": style.get("descripcion") or style.get("nombre", style_id),
        "composition": "Vertical 9:16; conservar la composición y escala del estilo; un sujeto focal por plano; sin texto incrustado.",
        "negative_prompt": "photorealism, unrelated art styles, mixed media, collage, lettering, text, watermark, logos, inconsistent material texture",
        "reference_assets": [],
        "seed_policy": "Semilla maestra fija derivada del project_id; reutilizar en todas las escenas y registrar proveedor, modelo y parámetros por recurso.",
        "seed": seed,
    }
    sb["typography_identity"] = {
        "font_family": f"{title_font} (título) + DejaVu Sans (subtítulos)",
        "font_weight": "Alfa Slab One Regular para el gancho; DejaVu Sans Bold para subtítulos.",
        "title_style": json.dumps(title_style, ensure_ascii=False, sort_keys=True),
        "subtitle_style": "ASS: DejaVu Sans, 72 px, blanco, contorno negro 6 px, sombra 2 px, centrado abajo; línea base 1300 px en lienzo 1080x1920.",
        "hierarchy": "Título-gancho desde el frame 0; subtítulos palabra a palabra debajo del foco visual; cortinilla de fuentes al cierre.",
        "animation": "Gancho con caja y subrayado del storyboard; subtítulos sincronizados con WordBoundary; cortes y movimientos definidos por escena.",
    }
    sb["approved_assets"] = approved
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(sb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "project_id": project_id,
        "style_id": style_id,
        "scene_count": len(sb.get("scenes", [])),
        "approved_asset_count": len(approved),
        "seed": seed,
        "output": str(output),
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--styles", default="scripts/estilos.json")
    args = p.parse_args()
    result = migrate(Path(args.input), Path(args.output), Path(args.styles))
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
