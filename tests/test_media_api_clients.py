import unittest
from unittest.mock import patch

from scripts.media_api_clients import KreaAPI, RunwayDevAPI


class MediaAPIClientTests(unittest.TestCase):
    @patch("scripts.media_api_clients._request_json")
    def test_krea_image_edit_uses_references_and_regional_edit(self, request):
        request.return_value = {"job_id": "job-1"}
        api = KreaAPI("fake-krea-token")
        result = api.edit_image(
            "Keep the mosaic style; replace only the sky",
            ["https://assets.example/frame.png"],
            resolution="2K",
            regions=[{"label": "sky", "x": 0, "y": 0, "width": 100, "height": 80}],
        )
        self.assertEqual(result["job_id"], "job-1")
        args = request.call_args.args
        self.assertEqual(args[0], "https://api.krea.ai/generate/image/krea/krea-3")
        self.assertEqual(args[1], "POST")
        payload = args[3]
        self.assertTrue(payload["regional_edit"])
        self.assertEqual(len(payload["image_urls"]), 1)
        self.assertNotIn("thinking_mode", payload)

    @patch("scripts.media_api_clients._request_json")
    def test_krea_seedance_clip_is_bounded_and_uses_start_frame(self, request):
        request.return_value = {"job_id": "job-2"}
        api = KreaAPI("fake-krea-token")
        api.generate_video(
            "Slow camera push-in, preserve the frame's visual identity",
            duration=12,
            aspect_ratio="9:16",
            resolution="720p",
            start_image="https://assets.example/scene.png",
        )
        payload = request.call_args.args[3]
        self.assertEqual(payload["duration"], 12)
        self.assertEqual(payload["aspect_ratio"], "9:16")
        self.assertEqual(payload["start_image"], "https://assets.example/scene.png")
        with self.assertRaises(ValueError):
            api.generate_video("Too long", duration=31)

    @patch("scripts.media_api_clients._request_json")
    def test_runway_bria_image_edit_uses_one_to_four_references(self, request):
        request.return_value = {"id": "task-1"}
        api = RunwayDevAPI("fake-runway-token")
        api.edit_image(
            "Remove the sign while preserving the stone mosaic texture",
            ["https://assets.example/frame.png"],
            seed=42,
        )
        args = request.call_args.args
        self.assertEqual(args[0], "https://api.dev.runwayml.com/v1/text_to_image")
        payload = args[3]
        self.assertEqual(payload["model"], "bria_fibo_edit_1_5")
        self.assertEqual(payload["referenceImages"][0]["uri"], "https://assets.example/frame.png")
        self.assertNotIn("ratio", payload)
        with self.assertRaises(ValueError):
            api.edit_image("Invalid", [])

    @patch("scripts.media_api_clients._request_json")
    def test_runway_aleph_video_edit_uses_video_to_video(self, request):
        request.return_value = {"id": "task-2"}
        api = RunwayDevAPI("fake-runway-token")
        api.edit_video(
            "https://assets.example/clip.mp4",
            "Remove the background sign; preserve camera movement",
            keyframes=[{"uri": "https://assets.example/keyframe.png", "seconds": 5}],
        )
        args = request.call_args.args
        self.assertEqual(args[0], "https://api.dev.runwayml.com/v1/video_to_video")
        self.assertEqual(args[3]["model"], "aleph2")
        self.assertEqual(args[3]["videoUri"], "https://assets.example/clip.mp4")

    @patch("scripts.media_api_clients._request_json")
    def test_runway_task_polling_uses_version_header(self, request):
        request.return_value = {"status": "SUCCEEDED"}
        api = RunwayDevAPI("fake-runway-token")
        api.get_task("task-3")
        self.assertEqual(request.call_args.args[0], "https://api.dev.runwayml.com/v1/tasks/task-3")
        self.assertEqual(request.call_args.args[2]["X-Runway-Version"], "2024-11-06")


if __name__ == "__main__":
    unittest.main()
