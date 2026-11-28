import sys
import unittest
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validar_storyboard


class TextOnlyStoryboardContractTests(unittest.TestCase):
    def test_valid_narrative_contract_passes(self):
        contract = {key: "contenido verificable" for key in validar_storyboard.NARRATIVE_CONTRACT_FIELDS}
        self.assertEqual(validar_storyboard.validar_narrative_contract(contract), [])

    def test_missing_narrative_contract_fields_are_rejected(self):
        self.assertTrue(validar_storyboard.validar_narrative_contract({"central_question": "¿Por qué?"}))

    def test_valid_independent_narrative_qa_passes(self):
        qa = {
            "status": "PASS",
            "score": 90,
            "review_basis": "lectura_en_frio_solo_narracion",
            "checks": {key: True for key in validar_storyboard.NARRATIVE_QA_CHECKS},
            "critical_flags": [],
            "reviewer_role": "auditor_capcot_independiente",
        }
        self.assertEqual(validar_storyboard.validar_narrative_qa(qa), [])

    def test_valid_terrestrial_map_point_passes(self):
        self.assertTrue(validar_storyboard.validar_punto_mapa({"lat": 53.5, "lon": -129.3}))

    def test_valid_celestial_ra_dec_point_passes(self):
        point = {
            "ra_deg": 9.7025,
            "dec_deg": 40.7689528,
            "sistema_coordenadas": "Ecuatoriales J2000 (RA/Dec)",
        }
        self.assertTrue(validar_storyboard.validar_punto_mapa(point))

    def test_invalid_celestial_ra_dec_point_is_rejected(self):
        point = {
            "ra_deg": 360,
            "dec_deg": 91,
            "sistema_coordenadas": "Ecuatoriales J2000 (RA/Dec)",
        }
        self.assertFalse(validar_storyboard.validar_punto_mapa(point))

    def test_check_doi_requires_crossref_identity(self):
        class Response:
            status = 200

            def getheader(self, name):
                return None

            def read(self):
                return b'{"message":{"DOI":"10.1234/another-record"}}'

        class Connection:
            def __init__(self, host, timeout, context):
                self.host = host

            def request(self, method, path, headers):
                pass

            def getresponse(self):
                return Response()

            def close(self):
                pass

        with patch.object(validar_storyboard.http.client, "HTTPSConnection", side_effect=Connection) as factory:
            self.assertFalse(validar_storyboard.check_doi("10.1234/requested-record"))
            self.assertEqual(factory.call_count, 1)
            self.assertEqual(factory.call_args.args[0], "api.crossref.org")

    def test_check_doi_accepts_exact_crossref_identity_case_insensitively(self):
        class Response:
            status = 200

            def getheader(self, name):
                return None

            def read(self):
                return b'{"message":{"DOI":"10.5194/BG-15-5131-2018"}}'

        class Connection:
            def __init__(self, host, timeout, context):
                self.host = host

            def request(self, method, path, headers):
                pass

            def getresponse(self):
                return Response()

            def close(self):
                pass

        with patch.object(validar_storyboard.http.client, "HTTPSConnection", side_effect=Connection):
            self.assertTrue(validar_storyboard.check_doi("10.5194/bg-15-5131-2018"))

    def test_check_doi_rejects_malformed_crossref_json(self):
        class Response:
            status = 200

            def getheader(self, name):
                return None

            def read(self):
                return b"not-json"

        class Connection:
            def __init__(self, host, timeout, context):
                self.host = host

            def request(self, method, path, headers):
                pass

            def getresponse(self):
                return Response()

            def close(self):
                pass

        with patch.object(validar_storyboard.http.client, "HTTPSConnection", side_effect=Connection):
            self.assertFalse(validar_storyboard.check_doi("10.1234/requested-record"))

    def test_missing_narrative_qa_is_rejected(self):
        self.assertTrue(validar_storyboard.validar_narrative_qa(None))

    def test_fail_or_flags_are_rejected(self):
        qa = {
            "status": "FAIL",
            "score": 84,
            "review_basis": "lectura_en_frio_solo_narracion",
            "checks": {key: True for key in validar_storyboard.NARRATIVE_QA_CHECKS},
            "critical_flags": ["CIERRE_SIN_PAYOFF"],
            "reviewer_role": "auditor_capcot_independiente",
        }
        self.assertTrue(validar_storyboard.validar_narrative_qa(qa))


if __name__ == "__main__":
    unittest.main()
