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


if __name__ == "__main__":
    unittest.main()
