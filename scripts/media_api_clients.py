#!/usr/bin/env python3
"""CAPCOT adapters for Krea and Runway Dev.

No requests are sent at import time. Each generation/edit call is billable.
Use environment variables KREA_API_KEY and RUNWAYML_API_SECRET.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any

KREA_BASE = "https://api.krea.ai"
RUNWAY_BASE = "https://api.dev.runwayml.com/v1"
RUNWAY_API_VERSION = "2024-11-06"


class MediaAPIError(RuntimeError):
    pass


def _request_json(url: str, method: str, headers: dict[str, str],
                  payload: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise MediaAPIError(f"{method} {url} -> HTTP {exc.code}: {detail[:1200]}") from exc
    except urllib.error.URLError as exc:
        raise MediaAPIError(f"No se pudo conectar con {url}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise MediaAPIError(f"Respuesta no JSON desde {url}") from exc


class KreaAPI:
    """Krea image editing (Krea 3) and video generation/editing (Seedance 2.5)."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("KREA_API_KEY")
        if not self.api_key:
            raise MediaAPIError("Falta KREA_API_KEY. No se ha enviado ninguna solicitud.")

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def edit_image(self, prompt: str, image_urls: list[str],
                   resolution: str = "2K",
                   regions: list[dict[str, Any]] | None = None) -> dict[str, Any]:
        """Edit an existing image with Krea 3 using image references/regions."""
        if not image_urls:
            raise ValueError("Krea 3 image editing requires at least one image URL.")
        if resolution not in {"1K", "2K", "4K"}:
            raise ValueError("resolution must be 1K, 2K or 4K")
        body: dict[str, Any] = {
            "prompt": prompt,
            "resolution": resolution,
            "image_urls": image_urls[:8],
        }
        if regions:
            body["regions"] = regions[:24]
            body["regional_edit"] = True
        return _request_json(
            f"{KREA_BASE}/generate/image/krea/krea-3",
            "POST", self.headers, body
        )

    def generate_video(self, prompt: str, duration: int = 5,
                       aspect_ratio: str = "9:16", resolution: str = "720p",
                       start_image: str | None = None,
                       end_image: str | None = None,
                       reference_images: list[str] | None = None,
                       reference_videos: list[str] | None = None,
                       draft: bool = False) -> dict[str, Any]:
        """Generate a Seedance 2.5 clip; references can guide an edit of source video."""
        if not 4 <= duration <= 30:
            raise ValueError("Seedance 2.5 duration must be between 4 and 30 seconds")
        if resolution not in {"480p", "720p", "1080p"}:
            raise ValueError("resolution must be 480p, 720p or 1080p")
        body: dict[str, Any] = {
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
            "draft": bool(draft),
        }
        if start_image:
            body["start_image"] = start_image
        if end_image:
            body["end_image"] = end_image
        if reference_images:
            body["reference_images"] = reference_images[:30]
        if reference_videos:
            body["reference_videos"] = reference_videos[:10]
        return _request_json(
            f"{KREA_BASE}/generate/video/bytedance/seedance-2-5",
            "POST", self.headers, body
        )

    def get_job(self, job_id: str) -> dict[str, Any]:
        return _request_json(
            f"{KREA_BASE}/jobs/{job_id}", "GET",
            {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}
        )


class RunwayDevAPI:
    """Runway Dev video editing with Aleph 2.0."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("RUNWAYML_API_SECRET")
        if not self.api_key:
            raise MediaAPIError("Falta RUNWAYML_API_SECRET. No se ha enviado ninguna solicitud.")

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "X-Runway-Version": RUNWAY_API_VERSION,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def edit_image(self, prompt_text: str, reference_images: list[str],
                   seed: int | None = None) -> dict[str, Any]:
        """Edit 1–4 reference images with Bria FIBO Edit 1.5 on Runway Dev."""
        if not 1 <= len(reference_images) <= 4:
            raise ValueError("Bria FIBO Edit 1.5 requires 1–4 reference images")
        if not prompt_text or len(prompt_text) > 10000:
            raise ValueError("prompt_text must contain 1–10000 characters")
        body: dict[str, Any] = {
            "model": "bria_fibo_edit_1_5",
            "promptText": prompt_text,
            "referenceImages": [{"uri": uri} for uri in reference_images],
        }
        if seed is not None:
            body["seed"] = seed
        return _request_json(
            f"{RUNWAY_BASE}/text_to_image", "POST", self.headers, body
        )

    def edit_video(self, video_uri: str, prompt_text: str,
                   keyframes: list[dict[str, Any]] | None = None,
                   target_aspect_ratio: str | None = None) -> dict[str, Any]:
        """Edit a 2–30 second source clip with Aleph 2.0; the call is billable."""
        if not video_uri.startswith(("https://", "runway://", "data:video/")):
            raise ValueError("video_uri must be HTTPS, a Runway upload URI or a video data URI")
        if not prompt_text or len(prompt_text) > 1000:
            raise ValueError("prompt_text must contain 1–1000 characters")
        body: dict[str, Any] = {
            "model": "aleph2",
            "videoUri": video_uri,
            "promptText": prompt_text,
        }
        if keyframes:
            body["keyframes"] = keyframes[:5]
        if target_aspect_ratio:
            body["targetAspectRatio"] = target_aspect_ratio
        return _request_json(
            f"{RUNWAY_BASE}/video_to_video", "POST", self.headers, body
        )

    def get_task(self, task_id: str) -> dict[str, Any]:
        return _request_json(
            f"{RUNWAY_BASE}/tasks/{task_id}", "GET",
            {
                "Authorization": f"Bearer {self.api_key}",
                "X-Runway-Version": RUNWAY_API_VERSION,
                "Accept": "application/json",
            }
        )


def configured_providers() -> dict[str, bool]:
    """Safe preflight: reports presence only, never prints or transmits secrets."""
    return {
        "krea_api_key_present": bool(os.getenv("KREA_API_KEY")),
        "runway_dev_api_key_present": bool(os.getenv("RUNWAYML_API_SECRET")),
    }


if __name__ == "__main__":
    print(json.dumps(configured_providers(), indent=2))
