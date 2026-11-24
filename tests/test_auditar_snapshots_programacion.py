import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import auditar_snapshots_programacion as auditor


class SnapshotProgrammingAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write_json(self, name, value):
        path = self.root / name
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
        return path

    def test_miniaturas_detects_same_slot_collision_and_converts_utc(self):
        path = self.write_json("miniaturas_auditoria_2026-11-21.json", {
            "siguen_mal_sin_mp4_no_se_invento": [
                {"yt_id": "video-a", "titulo": "A", "estado": "programado",
                 "publishAt": "2026-11-23T13:00:00Z", "hora_cdmx": "2026-11-23 07:00 CST"},
                {"yt_id": "video-b", "titulo": "B", "estado": "programado",
                 "publishAt": "2026-11-23T13:00:00Z", "hora_cdmx": "2026-11-23 07:00 CST"},
            ]
        })
        before = path.read_bytes()
        result = auditor.load_snapshots(self.root, "2026-11-23")
        self.assertEqual(len(result["ocupaciones"]), 2)
        self.assertEqual(len(result["conflictos"]), 1)
        self.assertEqual(result["conflictos"][0]["slot_local"], "07:00")
        self.assertEqual(result["conflictos"][0]["video_ids"], ["video-a", "video-b"])
        self.assertEqual(result["inconsistencias_timestamp"], [])
        self.assertEqual(result["resumen_por_fecha"][0]["cantidad_slots"], 1)
        self.assertEqual(result["resumen_por_fecha"][0]["cantidad_videos"], 2)
        self.assertEqual(path.read_bytes(), before)

    def test_rehechos_uses_project_path_and_nested_youtube_timestamp(self):
        path = self.write_json("rehechos_2026-11-22.json", {
            "capsulas": [{
                "clave": "nube",
                "titulo": "Una nube NO es ligera",
                "mp4": "/workspace/capcot_main/proyectos/2026-11-25_rehecho-nube/capsula.mp4",
                "portada": "/workspace/capcot_main/proyectos/2026-11-25_rehecho-nube/portada.jpg",
                "programado_CDMX": "2026-11-25 10:00",
                "youtube": {"id": "video-cloud", "publishAt_utc": "2026-11-25T16:00:00Z",
                            "estado": "private→public programado"},
            }]
        })
        before = path.read_bytes()
        result = auditor.load_snapshots(self.root, "2026-11-25")
        self.assertEqual(len(result["ocupaciones"]), 1)
        row = result["ocupaciones"][0]
        self.assertEqual(row["project_id"], "2026-11-25_rehecho-nube")
        self.assertEqual(row["video_id"], "video-cloud")
        self.assertEqual((row["fecha"], row["slot_local"]), ("2026-11-25", "10:00"))
        self.assertFalse(row["timestamp_mismatch"])
        self.assertEqual(row["source_kind"], "rehechos")
        self.assertEqual(path.read_bytes(), before)

    def test_real_snapshot_collision_group_is_loaded(self):
        self.write_json("miniaturas_auditoria_2026-11-21.json", {
            "siguen_mal_sin_mp4_no_se_invento": [],
            "colisiones_horario_mismo_publishAt": [{
                "publishAt": "2026-11-23T13:00:00Z",
                "hora_cdmx": "2026-11-23 07:00 CST",
                "videos": [
                    {"yt_id": "IQEU2Bqy3v0", "titulo": "Video A"},
                    {"yt_id": "tmOji99zGPE", "titulo": "Video B"},
                ],
            }],
        })
        result = auditor.load_snapshots(self.root, "2026-11-23")
        self.assertEqual(len(result["ocupaciones"]), 2)
        self.assertEqual(len(result["conflictos"]), 1)
        self.assertEqual(result["conflictos"][0]["slot_local"], "07:00")
        self.assertEqual(
            result["conflictos"][0]["video_ids"], ["IQEU2Bqy3v0", "tmOji99zGPE"]
        )
        self.assertTrue(all(x["source_kind"] == "miniaturas_colision" for x in result["ocupaciones"]))

    def test_collision_group_and_missing_media_list_are_deduplicated(self):
        item = {"yt_id": "video-same", "titulo": "Same", "estado": "programado",
                "publishAt": "2026-11-23T13:00:00Z", "hora_cdmx": "2026-11-23 07:00 CST"}
        self.write_json("miniaturas_auditoria_2026-11-21.json", {
            "siguen_mal_sin_mp4_no_se_invento": [item],
            "colisiones_horario_mismo_publishAt": [{
                "publishAt": item["publishAt"], "hora_cdmx": item["hora_cdmx"],
                "videos": [{"yt_id": "video-same", "titulo": "Same"},
                           {"yt_id": "video-other", "titulo": "Other"}],
            }],
        })
        result = auditor.load_snapshots(self.root, "2026-11-23")
        same = [x for x in result["ocupaciones"] if x["video_id"] == "video-same"]
        self.assertEqual(len(same), 1)
        self.assertEqual(len(same[0]["source_files"]), 2)
        self.assertEqual(len(result["conflictos"]), 1)

    def test_declared_local_time_mismatch_is_exposed(self):
        self.write_json("miniaturas_auditoria_2026-11-21.json", {
            "siguen_mal_sin_mp4_no_se_invento": [{
                "yt_id": "video-mismatch", "titulo": "Mismatched",
                "publishAt": "2026-11-23T13:00:00Z",
                "hora_cdmx": "2026-11-23 08:00 CST",
            }]
        })
        result = auditor.load_snapshots(self.root)
        self.assertEqual(len(result["inconsistencias_timestamp"]), 1)
        self.assertEqual(result["inconsistencias_timestamp"][0]["slot_local"], "08:00")

    def test_duplicate_video_across_snapshots_is_not_double_counted(self):
        item = {"yt_id": "video-same", "titulo": "Same", "estado": "programado",
                "publishAt": "2026-11-23T13:00:00Z", "hora_cdmx": "2026-11-23 07:00 CST"}
        self.write_json("miniaturas_auditoria_2026-11-21.json", {
            "siguen_mal_sin_mp4_no_se_invento": [item]
        })
        self.write_json("miniaturas_auditoria_2026-11-22.json", {
            "siguen_mal_sin_mp4_no_se_invento": [item]
        })
        result = auditor.load_snapshots(self.root)
        self.assertEqual(len(result["ocupaciones"]), 1)
        self.assertEqual(len(result["ocupaciones"][0]["source_files"]), 2)
        self.assertEqual(result["conflictos"], [])

    def test_scheduled_item_without_parseable_time_is_not_silently_ignored(self):
        self.write_json("miniaturas_auditoria_2026-11-21.json", {
            "siguen_mal_sin_mp4_no_se_invento": [
                {"yt_id": "video-without-time", "titulo": "Missing schedule"}
            ]
        })
        result = auditor.load_snapshots(self.root)
        self.assertEqual(result["resumen"]["errores"], 1)
        self.assertIn("publishAt y hora_cdmx ausentes", result["errores"][0])

    def test_missing_snapshot_directory_is_not_reported_as_empty_success(self):
        missing = self.root / "missing"
        result = auditor.load_snapshots(missing)
        self.assertEqual(result["resumen"]["errores"], 1)
        self.assertIn("FileNotFoundError", result["errores"][0])

    def test_empty_snapshot_directory_is_not_reported_as_empty_success(self):
        result = auditor.load_snapshots(self.root)
        self.assertEqual(result["resumen"]["errores"], 1)
        self.assertIn("NoSnapshotFiles", result["errores"][0])

    def test_invalid_snapshot_error_is_preserved_exactly(self):
        bad = self.root / "miniaturas_auditoria_2026-11-21.json"
        bad.write_text("{bad", encoding="utf-8")
        result = auditor.load_snapshots(self.root)
        self.assertEqual(result["resumen"]["errores"], 1)
        self.assertIn("JSONDecodeError", result["errores"][0])
        self.assertIn(str(bad), result["errores"][0])


    def test_collision_groups_are_loaded_from_every_miniaturas_snapshot(self):
        self.write_json("miniaturas_auditoria_2026-11-21.json", {
            "siguen_mal_sin_mp4_no_se_invento": [],
            "colisiones_horario_mismo_publishAt": [{
                "publishAt": "2026-11-23T13:00:00Z",
                "hora_cdmx": "2026-11-23 07:00 CST",
                "videos": [{"yt_id": "first-a"}, {"yt_id": "first-b"}],
            }],
        })
        self.write_json("miniaturas_auditoria_2026-11-22.json", {
            "siguen_mal_sin_mp4_no_se_invento": [],
            "colisiones_horario_mismo_publishAt": [{
                "publishAt": "2026-11-23T23:00:00Z",
                "hora_cdmx": "2026-11-23 17:00 CST",
                "videos": [{"yt_id": "second-a"}, {"yt_id": "second-b"}],
            }],
        })
        result = auditor.load_snapshots(self.root, "2026-11-23")
        self.assertEqual(len(result["ocupaciones"]), 4)
        self.assertEqual(len(result["conflictos"]), 2)
        self.assertEqual([x["slot_local"] for x in result["conflictos"]], ["07:00", "17:00"])
        source_files = {
            source.split("#", 1)[0]
            for row in result["ocupaciones"]
            for source in row["source_files"]
        }
        self.assertEqual(source_files, {
            "miniaturas_auditoria_2026-11-21.json",
            "miniaturas_auditoria_2026-11-22.json",
        })

if ( __name__ == "__main__" ):
    unittest.main()
