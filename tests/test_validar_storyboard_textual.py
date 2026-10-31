import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validar_storyboard


class TextOnlyStoryboardContractTests(unittest.TestCase):
    def test_current_2026_10_31_queue_storyboard(self):
        root = Path(__file__).resolve().parents[1]
        path = root / "cola" / "entrada" / "2026-10-31_pardelas-jetlag-solar.json"
        if not path.exists():
            self.skipTest("daily candidate is not present in this checkout")
        errors, warnings = validar_storyboard.validar(str(path), doi=False)
        self.assertEqual(errors, [], "\n".join(errors))


if __name__ == "__main__":
    unittest.main()
