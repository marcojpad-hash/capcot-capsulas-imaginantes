import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import capas_datos


class CelestialMapBoundsTests(unittest.TestCase):
    def test_nasa_ra_dec_coordinates_produce_a_valid_celestial_viewport(self):
        capa = {
            "tipo": "mapa",
            "puntos": [
                {
                    "id": "AT2025abao",
                    "ra_deg": 9.7025,
                    "dec_deg": 40.7689528,
                    "sistema_coordenadas": "RA/Dec ecuatorial",
                }
            ],
        }
        ra0, ra1, dec0, dec1 = capas_datos._celestial_bounds(capa)
        self.assertLess(ra0, 9.7025)
        self.assertGreater(ra1, 9.7025)
        self.assertLess(dec0, 40.7689528)
        self.assertGreater(dec1, 40.7689528)
        self.assertLess(ra1 - ra0, 10)
        self.assertLess(dec1 - dec0, 10)

    def test_explicit_ra_dec_region_is_preserved(self):
        capa = {
            "puntos": [{"ra_deg": 9.7025, "dec_deg": 40.7689528}],
            "region_ra_dec": [8.0, 12.0, 39.0, 43.0],
        }
        self.assertEqual(
            capas_datos._celestial_bounds(capa),
            (8.0, 12.0, 39.0, 43.0),
        )

    def test_terrestrial_map_does_not_enter_celestial_branch(self):
        capa = {"puntos": [{"nombre": "Gemini North", "lon": -155.469, "lat": 19.8238}]}
        self.assertIsNone(capas_datos._celestial_bounds(capa))

    def test_mixed_terrestrial_and_celestial_points_are_rejected(self):
        capa = {
            "puntos": [
                {"ra_deg": 9.7025, "dec_deg": 40.7689528},
                {"nombre": "Gemini North", "lon": -155.469, "lat": 19.8238},
            ]
        }
        with self.assertRaises(ValueError):
            capas_datos._celestial_bounds(capa)

    def test_out_of_range_celestial_coordinates_are_rejected(self):
        capa = {"puntos": [{"ra_deg": 361.0, "dec_deg": 40.0}]}
        with self.assertRaises(ValueError):
            capas_datos._celestial_bounds(capa)


if __name__ == "__main__":
    unittest.main()
