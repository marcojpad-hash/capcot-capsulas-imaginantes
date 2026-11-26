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

    def test_candidate_is_not_counted_against_daily_capacity(self):
        five = [
            {"project_id": f"p{i}", "origen": "externa" if i < 3 else "propia"}
            for i in range(5)
        ]
        with patch.object(rotacion, "hecha_hoy", return_value=five):
            remaining = rotacion.exigir_cupo(
                "2026-11-01", "externa", project_id="p4"
            )
        self.assertEqual(len(remaining), 4)

    def test_three_current_windows_respect_minute_bounds_and_exclude_fixed_2330(self):
        now = datetime.datetime(2026, 11, 26, 6, 0, tzinfo=rotacion.datetime.timezone(
            datetime.timedelta(hours=-6)
        ))
        used = []
        expected = [
            ("manana", 6 * 60 + 30, 7 * 60 + 30),
            ("mediodia", 13 * 60, 14 * 60 + 30),
            ("tarde", 16 * 60 + 30, 18 * 60),
        ]
        for index, (window_id, start, end) in enumerate(expected):
            with patch.object(rotacion, "publicaciones", return_value=used):
                local, utc, window = rotacion.hora_publicacion(
                    "2026-11-26", ahora=now, semilla=index
                )
            self.assertIsNotNone(local)
            self.assertIsNotNone(utc)
            self.assertEqual(window, window_id)
            local_dt = datetime.datetime.fromisoformat(local)
            minute_of_day = local_dt.hour * 60 + local_dt.minute
            self.assertGreaterEqual(minute_of_day, start)
            self.assertLess(minute_of_day, end)
            used.append({"fecha": "2026-11-26", "ventana": window})

        with patch.object(rotacion, "publicaciones", return_value=used):
            self.assertEqual(
                rotacion.hora_publicacion("2026-11-26", ahora=now),
                (None, None, None),
            )

    def test_legacy_window_indices_and_slot_times_prevent_duplicates(self):
        used = [
            {"fecha": "2026-11-26", "ventana": 0},
            {"fecha": "2026-11-26", "ventana": 1},
            {"fecha": "2026-11-26", "ventana": None, "slot": "17:00"},
        ]
        now = datetime.datetime(2026, 11, 26, 6, 0, tzinfo=rotacion.datetime.timezone(
            datetime.timedelta(hours=-6)
        ))
        with patch.object(rotacion, "publicaciones", return_value=used):
            self.assertEqual(
                rotacion.hora_publicacion("2026-11-26", ahora=now),
                (None, None, None),
            )

    def test_legacy_utc_publish_at_is_converted_to_cdmx_window(self):
        used = [{
            "fecha": "2026-11-26",
            "ventana": None,
            "publishAt_utc": "2026-11-26T23:00:00Z",
        }]
        now = datetime.datetime(2026, 11, 26, 16, 0, tzinfo=rotacion.datetime.timezone(
            datetime.timedelta(hours=-6)
        ))
        with patch.object(rotacion, "publicaciones", return_value=used):
            self.assertEqual(
                rotacion.hora_publicacion("2026-11-26", ahora=now),
                (None, None, None),
            )

    def test_fixed_2330_is_not_a_variable_window(self):
        now = datetime.datetime(2026, 11, 26, 22, 0, tzinfo=rotacion.datetime.timezone(
            datetime.timedelta(hours=-6)
        ))
        with patch.object(rotacion, "publicaciones", return_value=[]):
            self.assertEqual(
                rotacion.hora_publicacion("2026-11-26", ahora=now),
                (None, None, None),
            )


    def test_blocked_storyboards_do_not_consume_capacity_but_remain_rotation_evidence(self):
        blocked = [
            {
                "project_id": f"blocked{i}",
                "origen": "externa",
                "tema": "tema bloqueado",
                "estructura": "historia",
                "estilo": "linograbado",
                "cama": "pizzicato",
                "_source": "bloqueado",
            }
            for i in range(5)
        ]
        with patch.object(rotacion, "hecha_hoy", return_value=blocked):
            remaining = rotacion.exigir_cupo("2026-11-20", "externa")
            with patch.object(rotacion, "temas_del_dia", return_value=[]):
                evitar = rotacion.evitar_hoy("2026-11-20")
        self.assertEqual(remaining, [])
        self.assertIn("linograbado", evitar["estilo"])
        self.assertIn("pizzicato", evitar["cama"])
        self.assertIn("tema bloqueado", evitar["tema"])



if __name__ == "__main__":
    unittest.main()
