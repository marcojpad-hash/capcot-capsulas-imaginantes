import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validar_storyboard


class TextOnlyStoryboardContractTests(unittest.TestCase):
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
