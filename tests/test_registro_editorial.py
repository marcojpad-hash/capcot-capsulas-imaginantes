import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import registro_editorial


class RegistroEditorialTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old_root = registro_editorial.ROOT
        registro_editorial.ROOT = Path(self.tmp.name)
        (registro_editorial.ROOT / "data").mkdir()
        (registro_editorial.ROOT / "proyectos").mkdir()
        (registro_editorial.ROOT / "cola" / "entrada").mkdir(parents=True)

    def tearDown(self):
        registro_editorial.ROOT = self.old_root
        self.tmp.cleanup()

    def write_json(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def test_reconciles_queue_and_project_when_data_is_stale(self):
        rotacion = [{"fecha": "2026-10-28", "project_id": "2026-10-28_old", "tema": "tema viejo", "estilo": "ukiyo_e"}]
        topics = {"2026-10-28": [{"tema": "tema viejo", "project_id": "2026-10-28_old"}]}
        rot_path = registro_editorial.ROOT / "data" / "rotacion.json"
        topics_path = registro_editorial.ROOT / "data" / "temas_del_dia.json"
        self.write_json(rot_path, rotacion)
        self.write_json(topics_path, topics)
        self.write_json(
            registro_editorial.ROOT / "proyectos" / "2026-10-30_arqueas" / "storyboard.json",
            {"project_id": "2026-10-30_arqueas", "title": "Arqueas", "estilo_id": "microscopio_psicodelico",
             "estructura": "pregunta", "scenes": [{"duration_seconds": 80}], "cortinilla_fuentes": {"duration_seconds": 6}}
        )
        self.write_json(
            registro_editorial.ROOT / "cola" / "entrada" / "2026-10-31_aves.json",
            {"project_id": "2026-10-31_aves", "title": "Pardelas", "trend_source": {"termino": "reloj solar de pardelas"},
             "estilo_id": "papel_rasgado_capas", "estructura": "historia", "audio": {"music_asset": "sintetico:pizzicato"},
             "scenes": [{"duration_seconds": 78}], "cortinilla_fuentes": {"duration_seconds": 6}}
        )

        day = registro_editorial.registros_dia("2026-10-31")
        self.assertEqual(len(day), 1)
        self.assertEqual(day[0]["project_id"], "2026-10-31_aves")
        self.assertEqual(day[0]["estilo"], "papel_rasgado_capas")
        self.assertEqual(day[0]["cama"], "pizzicato")
        self.assertEqual(registro_editorial.temas_dia("2026-10-31")[0]["tema"], "reloj solar de pardelas")
        self.assertEqual(json.loads(rot_path.read_text(encoding="utf-8")), rotacion)
        self.assertEqual(json.loads(topics_path.read_text(encoding="utf-8")), topics)

    def test_external_origin_survives_project_and_output_copies(self):
        sb = {
            "project_id": "2026-10-31_external",
            "title": "External package",
            "trend_source": {"termino": "external topic"},
            "estilo_id": "papel_rasgado_capas",
            "estructura": "historia",
            "scenes": [{"duration_seconds": 78}],
            "cortinilla_fuentes": {"duration_seconds": 6},
        }
        self.write_json(
            registro_editorial.ROOT / "cola" / "entrada" / "2026-10-31_external.json",
            sb,
        )
        self.write_json(
            registro_editorial.ROOT / "proyectos" / "2026-10-31_external" / "storyboard.json",
            sb,
        )
        self.write_json(
            registro_editorial.ROOT / "salidas" / "2026-10-31_external" / "storyboard.json",
            sb,
        )
        day = registro_editorial.registros_dia("2026-10-31")
        self.assertEqual(len(day), 1)
        self.assertEqual(day[0]["origen"], "externa")

    def test_deduplicates_same_project_across_queue_and_rotation(self):
        self.write_json(
            registro_editorial.ROOT / "data" / "rotacion.json",
            [{"fecha": "2026-10-31", "project_id": "2026-10-31_aves", "tema": "Pardelas", "estructura": "historia"}]
        )
        self.write_json(
            registro_editorial.ROOT / "cola" / "entrada" / "2026-10-31_aves.json",
            {"project_id": "2026-10-31_aves", "title": "Pardelas", "estilo_id": "papel_rasgado_capas",
             "scenes": [{"duration_seconds": 78}], "cortinilla_fuentes": {"duration_seconds": 6}}
        )
        day = registro_editorial.registros_dia("2026-10-31")
        self.assertEqual(len(day), 1)
        self.assertEqual(day[0]["estructura"], "historia")
        self.assertEqual(day[0]["estilo"], "papel_rasgado_capas")


    def test_includes_blocked_storyboards_in_rotation(self):
        self.write_json(
            registro_editorial.ROOT / "cola" / "bloqueados" / "2026-11-07_clavo" / "storyboard.json",
            {
                "project_id": "2026-11-07_clavo",
                "title": "Clavo de cocina",
                "estilo_id": "linograbado",
                "estructura": "historia",
                "audio": {"cama_musical": "sintetico:pizzicato"},
                "scenes": [{"duration_seconds": 78}],
                "cortinilla_fuentes": {"duration_seconds": 6},
            },
        )
        day = registro_editorial.registros_dia("2026-11-07")
        self.assertEqual(len(day), 1)
        self.assertEqual(day[0]["project_id"], "2026-11-07_clavo")
        self.assertEqual(day[0]["_source"], "bloqueado")
        self.assertEqual(day[0]["origen"], "externa")
        self.assertEqual(day[0]["estilo"], "linograbado")
        self.assertEqual(day[0]["cama"], "pizzicato")
        self.assertEqual(
            registro_editorial.temas_dia("2026-11-07")[0]["tema"],
            "clavo de cocina",
        )



    def test_includes_flat_blocked_storyboards_in_rotation(self):
        self.write_json(
            registro_editorial.ROOT / "cola" / "bloqueados" / "2026-11-07_clavo.json",
            {
                "project_id": "2026-11-07_clavo",
                "title": "Clavo de cocina",
                "estilo_id": "linograbado",
                "estructura": "historia",
                "audio": {"cama_musical": "sintetico:pizzicato"},
                "scenes": [{"duration_seconds": 78}],
                "cortinilla_fuentes": {"duration_seconds": 6},
            },
        )
        day = registro_editorial.registros_dia("2026-11-07")
        self.assertEqual(len(day), 1)
        self.assertEqual(day[0]["project_id"], "2026-11-07_clavo")
        self.assertEqual(day[0]["_source"], "bloqueado")
        self.assertEqual(day[0]["origen"], "externa")
        self.assertEqual(day[0]["estilo"], "linograbado")
        self.assertEqual(day[0]["cama"], "pizzicato")
        self.assertEqual(
            registro_editorial.temas_dia("2026-11-07")[0]["tema"],
            "clavo de cocina",
        )



    def test_finds_storyboards_more_than_one_directory_level_deep(self):
        self.write_json(
            registro_editorial.ROOT / "proyectos" / "2026-11-20_nested" / "archive" / "review" / "storyboard.json",
            {
                "project_id": "2026-11-20_nested",
                "title": "Nested storyboard",
                "estilo_id": "linograbado",
                "scenes": [{"duration_seconds": 78}],
                "cortinilla_fuentes": {"duration_seconds": 6},
            },
        )
        rows = registro_editorial.registros_dia("2026-11-20")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["project_id"], "2026-11-20_nested")
        self.assertEqual(rows[0]["_source"], "proyecto")
        self.assertEqual(
            rows[0]["_path"],
            "proyectos/2026-11-20_nested/archive/review/storyboard.json",
        )

    def test_handoff_markers_are_listed_separately_and_never_confirm_receipt(self):
        self.write_json(
            registro_editorial.ROOT / "handoffs" / "grok_inbox" / "2026-11-20_robot.json",
            {
                "event": "capcot.package.ready",
                "status": "pending",
                "project_id": "2026-11-20_robot",
                "branch": "main",
                "commit_sha": "abc123",
                "package_path": "cola/entrada/2026-11-20_robot/",
            },
        )
        self.assertEqual(registro_editorial.registros_dia("2026-11-20"), [])
        markers = registro_editorial.handoffs_grok_inbox()
        self.assertEqual(len(markers), 1)
        self.assertEqual(markers[0]["status"], "pending")
        self.assertFalse(markers[0]["receipt_confirmed"])
        self.assertEqual(markers[0]["project_id"], "2026-11-20_robot")
        self.assertEqual(
            markers[0]["receipt_rule"],
            "Solo cola/estado/<project_id>.json confirma recepción Grok.",
        )



    def test_slot_occupancy_reports_project_target_slot(self):
        self.write_json(
            registro_editorial.ROOT / "proyectos" / "2026-11-21_nuevo" / "storyboard.json",
            {
                "project_id": "2026-11-21_nuevo",
                "fecha_objetivo": "2026-11-21",
                "slot_local": "17:00",
                "title": "Tema nuevo",
                "publicacion": {"status": "PENDIENTE_DECISION_GROK"},
            },
        )
        result = registro_editorial.ocupacion_slots("2026-11-21")
        self.assertEqual(len(result["ocupaciones"]), 1)
        row = result["ocupaciones"][0]
        self.assertEqual((row["fecha"], row["slot_local"]), ("2026-11-21", "17:00"))
        self.assertEqual(row["estado_evidencia"], "PROPUESTA_EN_PROYECTOS")
        self.assertEqual(result["conflictos"], [])

    def test_slot_occupancy_converts_utc_publication_to_local_slot(self):
        self.write_json(
            registro_editorial.ROOT / "data" / "publicaciones.json",
            [{
                "fecha": "2026-11-21",
                "project_id": "2026-11-21_publicado",
                "publishAt_utc": "2026-11-21T19:30:00Z",
                "hora_local": "2026-11-21 13:30 (America/Mexico_City)",
                "yt_id": "video123",
            }],
        )
        result = registro_editorial.ocupacion_slots("2026-11-21")
        row = result["ocupaciones"][0]
        self.assertEqual(row["slot_local"], "13:30")
        self.assertEqual(row["estado_evidencia"], "PUBLICADO_O_ID_REGISTRADO")
        self.assertEqual(row["video_id"], "video123")

    def test_slot_occupancy_detects_cross_project_conflict(self):
        self.write_json(
            registro_editorial.ROOT / "data" / "publicaciones.json",
            [{
                "fecha": "2026-11-21",
                "project_id": "2026-11-21_publicado",
                "hora_local": "2026-11-21 13:30 (America/Mexico_City)",
                "yt_id": "video123",
            }],
        )
        self.write_json(
            registro_editorial.ROOT / "proyectos" / "2026-11-21_borrador" / "storyboard.json",
            {
                "project_id": "2026-11-21_borrador",
                "fecha_objetivo": "2026-11-21",
                "slot_local": "13:30",
            },
        )
        result = registro_editorial.ocupacion_slots("2026-11-21")
        self.assertEqual(len(result["conflictos"]), 1)
        self.assertEqual(
            result["conflictos"][0]["project_ids"],
            ["2026-11-21_borrador", "2026-11-21_publicado"],
        )

    def test_slot_occupancy_flags_inconsistent_slots_for_same_project(self):
        self.write_json(
            registro_editorial.ROOT / "data" / "publicaciones.json",
            [{
                "fecha": "2026-11-21",
                "project_id": "2026-11-21_mismo",
                "hora_local": "2026-11-21 13:30 (America/Mexico_City)",
                "yt_id": "video123",
            }],
        )
        self.write_json(
            registro_editorial.ROOT / "proyectos" / "2026-11-21_mismo" / "programacion.json",
            {
                "project_id": "2026-11-21_mismo",
                "publish_at": "2026-11-22T01:00:00Z",
                "hora_cdmx": "19:00",
                "estado": "programado_para_publicar",
            },
        )
        result = registro_editorial.ocupacion_slots("2026-11-21")
        self.assertEqual(len(result["discrepancias_por_project_id"]), 1)
        self.assertEqual(
            result["discrepancias_por_project_id"][0]["slots"],
            [
                {"fecha": "2026-11-21", "slot_local": "13:30"},
                {"fecha": "2026-11-21", "slot_local": "19:00"},
            ],
        )

    def test_slot_occupancy_keeps_blocked_evidence_without_counting_it_as_publication(self):
        self.write_json(
            registro_editorial.ROOT / "cola" / "bloqueados" / "2026-11-21_bloqueado" / "storyboard.json",
            {
                "project_id": "2026-11-21_bloqueado",
                "fecha_objetivo": "2026-11-21",
                "slot_local": "23:30",
            },
        )
        result = registro_editorial.ocupacion_slots("2026-11-21")
        self.assertEqual(result["ocupaciones"][0]["estado_evidencia"], "BLOQUEADO")
        self.assertIsNone(result["ocupaciones"][0]["video_id"])

if __name__ == "__main__":
    unittest.main()
