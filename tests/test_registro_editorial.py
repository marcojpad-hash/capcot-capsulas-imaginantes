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


    def test_slot_occupancy_reports_timestamp_mismatch_and_ignores_date_only(self):
        self.write_json(
            registro_editorial.ROOT / "data" / "publicaciones.json",
            [
                {
                    "fecha": "2026-11-21",
                    "project_id": "2026-11-21_mismatch",
                    "hora_local": "2026-11-21 13:30 (America/Mexico_City)",
                    "publishAt_utc": "2026-11-21T20:00:00Z",
                    "yt_id": "video123",
                },
                {
                    "fecha": "2026-11-21",
                    "project_id": "2026-11-21_date_only",
                    "publish_at": "2026-11-21",
                },
            ],
        )
        result = registro_editorial.ocupacion_slots("2026-11-21")
        self.assertEqual(len(result["ocupaciones"]), 1)
        self.assertEqual(result["ocupaciones"][0]["slot_local"], "13:30")
        self.assertTrue(result["ocupaciones"][0]["timestamp_mismatch"])
        self.assertEqual(len(result["inconsistencias_timestamp"]), 1)

    def test_slot_occupancy_reads_nested_youtube_schedule(self):
        self.write_json(
            registro_editorial.ROOT / "proyectos" / "2026-11-17_nuevo" / "programacion.json",
            {
                "project_id": "2026-11-17_nuevo",
                "slot": "dato del día 2026-11-17 23:30 CDMX",
                "youtube": {
                    "video_id": "abc123",
                    "privacyStatus": "private",
                    "publishAt": "2026-11-18T05:30:00Z",
                },
            },
        )
        result = registro_editorial.ocupacion_slots("2026-11-17")
        row = result["ocupaciones"][0]
        self.assertEqual(row["video_id"], "abc123")
        self.assertEqual(row["slot_local"], "23:30")
        self.assertEqual(row["estado_evidencia"], "PROGRAMADO_CON_VIDEO_ID")

    def test_slot_occupancy_reads_nested_published_video_record(self):
        self.write_json(
            registro_editorial.ROOT / "salidas" / "2026-11-16_publicado" / "publicacion.json",
            {
                "project_id": "2026-11-16_publicado",
                "resultado": {
                    "youtube": {
                        "kind": "youtube#video",
                        "id": "video456",
                        "snippet": {"publishedAt": "2026-11-16T13:00:23Z"},
                    }
                },
            },
        )
        result = registro_editorial.ocupacion_slots("2026-11-16")
        row = result["ocupaciones"][0]
        self.assertEqual(row["video_id"], "video456")
        self.assertEqual(row["slot_local"], "07:00")
        self.assertEqual(row["estado_evidencia"], "PUBLICACION_REGISTRADA")

    def test_slot_occupancy_checks_referenced_media_in_repository_tree(self):
        project_dir = registro_editorial.ROOT / "proyectos" / "2026-11-22_media"
        self.write_json(
            project_dir / "storyboard.json",
            {
                "project_id": "2026-11-22_media",
                "fecha_objetivo": "2026-11-22",
                "slot_local": "13:30",
                "asset_filename": "capsula.mp4",
                "export": {"filename": "capsula.mp4"},
            },
        )
        missing = registro_editorial.ocupacion_slots("2026-11-22")["ocupaciones"][0]
        self.assertEqual(missing["media_status"], "MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO")
        (project_dir / "capsula.mp4").write_bytes(b"test")
        verified = registro_editorial.ocupacion_slots("2026-11-22")["ocupaciones"][0]
        self.assertEqual(verified["media_status"], "VERIFICADOS_EN_REPOSITORIO")
        self.assertEqual(verified["missing_media_references"], [])


    def test_slot_occupancy_checks_scene_level_media_reference(self):
        self.write_json(
            registro_editorial.ROOT / "proyectos" / "2026-11-22_scene-media" / "storyboard.json",
            {
                "project_id": "2026-11-22_scene-media",
                "fecha_objetivo": "2026-11-22",
                "slot_local": "19:00",
                "scenes": [{"asset_filename": "scene_001.png"}],
            },
        )
        result = registro_editorial.ocupacion_slots("2026-11-22")
        row = result["ocupaciones"][0]
        self.assertEqual(row["missing_media_references"], ["scene_001.png"])
        self.assertEqual(row["media_status"], "MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO")


    def test_slot_occupancy_reads_daily_schedule_snapshots_and_skips_empty_slots(self):
        self.write_json(
            registro_editorial.ROOT / "data" / "horario_2026-11-11.json",
            {
                "fecha": "2026-11-11",
                "slots": [
                    {
                        "hora": "07:00",
                        "id": "2026-11-06_kids-ballena-azul-corazon",
                        "estado": "publicado_yt_tt",
                        "yt_id": "wbFrlM2e_YE",
                        "yt_published_at": "2026-11-11T13:00:03Z",
                        "mp4": "/workspace/capcot/ballena/capsula.mp4",
                    },
                    {"hora": "23:30", "id": None, "estado": "sin_paquete"},
                ],
                "atrasados_revisados": [
                    {
                        "hora_original": "2026-11-10 17:00",
                        "id": "capsaicina-resub",
                        "estado": "publicado_yt_tt",
                        "yt_id": "K2I_jgugiOU",
                        "yt_published_at": "2026-11-10T23:00:38Z",
                    }
                ],
            },
        )

        rows = registro_editorial.ocupacion_slots()["ocupaciones"]
        by_id = {row["project_id"]: row for row in rows}
        self.assertEqual(
            set(by_id),
            {"2026-11-06_kids-ballena-azul-corazon", "capsaicina-resub"},
        )
        current = by_id["2026-11-06_kids-ballena-azul-corazon"]
        self.assertEqual((current["fecha"], current["slot_local"]), ("2026-11-11", "07:00"))
        self.assertEqual(current["estado_evidencia"], "PUBLICACION_REGISTRADA")
        self.assertEqual(current["video_id"], "wbFrlM2e_YE")
        self.assertEqual(current["media_status"], "MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO")
        late = by_id["capsaicina-resub"]
        self.assertEqual((late["fecha"], late["slot_local"]), ("2026-11-10", "17:00"))
        self.assertEqual(late["video_id"], "K2I_jgugiOU")

    def test_slot_occupancy_classifies_fixed_regular_test_and_outside_windows(self):
        self.write_json(
            registro_editorial.ROOT / "data" / "horarios.json",
            {
                "actualizado": "2026-11-09",
                "zona_horaria": "America/Mexico_City",
                "politica_desde_2026-11-09": {
                    "ventanas": ["06:30-07:30", "16:30-18:00"],
                    "slot_fijo": "23:30 dato del día",
                },
                "ventanas_en_prueba": [
                    {"id": "noche", "inicio": "19:00", "fin": "21:00"}
                ],
            },
        )
        for project_id, slot in (
            ("2026-11-09_fijo", "23:30"),
            ("2026-11-09_regular", "07:00"),
            ("2026-11-09_prueba", "19:30"),
            ("2026-11-09_fuera", "13:30"),
        ):
            self.write_json(
                registro_editorial.ROOT / "proyectos" / project_id / "storyboard.json",
                {"project_id": project_id, "fecha_objetivo": "2026-11-09", "slot_local": slot},
            )

        result = registro_editorial.ocupacion_slots("2026-11-09")
        self.assertEqual(result["politica_horaria"]["fecha_politica"], "2026-11-09")
        rows = {row["project_id"]: row for row in result["ocupaciones"]}
        self.assertEqual(rows["2026-11-09_fijo"]["coincidencia_horaria"], "SLOT_FIJO")
        self.assertEqual(rows["2026-11-09_regular"]["coincidencia_horaria"], "VENTANA_REGULAR")
        self.assertEqual(rows["2026-11-09_prueba"]["coincidencia_horaria"], "VENTANA_EN_PRUEBA")
        self.assertEqual(rows["2026-11-09_fuera"]["coincidencia_horaria"], "FUERA_DE_VENTANA")

    def test_slot_occupancy_exposes_policy_cut_older_than_target_date(self):
        self.write_json(
            registro_editorial.ROOT / "data" / "horarios.json",
            {
                "actualizado": "2026-11-09",
                "politica_desde_2026-11-09": {
                    "ventanas": ["06:30-07:30", "16:30-18:00"],
                    "slot_fijo": "23:30",
                },
            },
        )
        self.write_json(
            registro_editorial.ROOT / "proyectos" / "2026-11-21_tarde" / "storyboard.json",
            {
                "project_id": "2026-11-21_tarde",
                "fecha_objetivo": "2026-11-21",
                "slot_local": "17:00",
            },
        )
        result = registro_editorial.ocupacion_slots("2026-11-21")
        row = result["ocupaciones"][0]
        self.assertEqual(
            result["politica_horaria"]["estado_frescura"],
            "CORTE_ANTERIOR_A_FECHA_OBJETIVO",
        )
        self.assertEqual(row["coincidencia_horaria"], "VENTANA_REGULAR")
        self.assertEqual(
            row["estado_frescura_horaria"],
            "CORTE_ANTERIOR_A_FECHA_OBJETIVO",
        )


if __name__ == "__main__":
    unittest.main()
