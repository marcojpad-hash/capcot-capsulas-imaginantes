import datetime
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import rotacion


class RotacionCapacityTests(unittest.TestCase):
    def test_daily_capacity_is_five_and_origin_caps_are_respected(self):
        with patch.object(rotacion, "hecha_hoy", return_value=[]):
            self.assertEqual(len(rotacion.exigir_cupo("2026-11-01", "externa")), 0)
        five = [
            {"project_id": f"p{i}", "origen": "externa" if i < 3 else "propia"}
            for i in range(5)
        ]
        with patch.object(rotacion, "hecha_hoy", return_value=five):
            with self.assertRaises(SystemExit):
                rotacion.exigir_cupo("2026-11-01", "externa")

        two_own = [{"project_id": f"o{i}", "origen": "propia"} for i in range(2)]
        with patch.object(rotacion, "hecha_hoy", return_value=two_own):
            with self.assertRaises(SystemExit):
                rotacion.exigir_cupo("2026-11-01", "propia")

    def test_five_distinct_publication_windows_can_be_assigned(self):
        now = datetime.datetime(2026, 11, 1, 6, 0, tzinfo=rotacion.datetime.timezone(
            datetime.timedelta(hours=-6)
        ))
        used = []
        for expected in range(5):
            with patch.object(rotacion, "publicaciones", return_value=used):
                local, utc, window = rotacion.hora_publicacion(
                    "2026-11-01", ahora=now, semilla=expected
                )
            self.assertIsNotNone(local)
            self.assertIsNotNone(utc)
            self.assertEqual(window, expected)
            used.append({"fecha": "2026-11-01", "ventana": window})
        self.assertEqual(len({x["ventana"] for x in used}), 5)


if __name__ == "__main__":
    unittest.main()
