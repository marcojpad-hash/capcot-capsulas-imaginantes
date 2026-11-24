import json
import ssl
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validar_storyboard as validator


PROMPT_BASE = "atlas test prompt"
NARRATION = [
    "La cámara del robot recorre una ladera submarina. A 6,148 metros, aparecen bordes lobulados de roca volcánica.",
    "No está en el fondo de Challenger Deep: Jason/Medea trabaja en su antearco, donde el equipo buscaba rocas y señales geológicas.",
    "En cinco inmersiones recorrió unos 300 kilómetros del segmento central y occidental, un entorno donde el volcanismo de antearco es inusual; tres de ellas recuperaron depósitos piroclásticos.",
    "Una fotografía muestra láminas fracturadas a 6,334 metros; otra registra frentes de flujo de uno a dos metros de ancho.",
    "Los autores los identifican como productos de volcanismo explosivo submarino, los más profundos conocidos hasta ahora.",
    "Pero a seis kilómetros la presión dificulta la expansión de gases. El equipo propone fluidos supercríticos para explicar una fragmentación distinta.",
    "Eso sigue siendo una hipótesis: no localizaron los conductos eruptivos ni observaron una erupción en marcha; reconstruyen el proceso desde las rocas.",
    "El robot no llegó al fondo de la fosa, pero encontró una huella extraordinaria: la geología también deja archivos en el abismo. Esto fue Datos y ociosidades.",
]


def fixture_storyboard():
    arcs = [
        "hook_medias_res", "desarrollo", "desarrollo", "desarrollo",
        "desarrollo", "desarrollo", "cierre_historia", "reflexion_o_pregunta",
    ]
    durations = [10, 10, 10, 10, 10, 10, 9, 9]
    scenes = []
    for i, text in enumerate(NARRATION):
        scene = {
            "id": f"scene_{i+1:03d}",
            "arc": arcs[i],
            "duration_seconds": durations[i],
            "narration": text,
            "visual_description": f"Scientific engraved illustration for scene {i+1}.",
            "image_prompt": PROMPT_BASE + f" scene {i+1}",
            "source_ids": ["SRC-001"],
            "ambiente": "Submarine low ambience.",
            "sfx": ["soft sonar pulse"],
            "dramatic_beat": f"Beat {i+1}",
            "scene_function": f"Function {i+1}",
            "causal_bridge_from_previous": f"Bridge {i+1}",
            "question_state": f"Question state {i+1}",
            "reason_to_continue": f"Reason {i+1}",
            "new_information": f"New information {i+1}",
            "style_id": "atlas_antiguo",
        }
        if i == 0:
            scene["capa"] = {
                "tipo": "mapa",
                "fuente": "SRC-001, Table 1",
                "puntos": [{"nombre": "Dive start", "lat": 11.486, "lon": 141.565}],
            }
        if i == 3:
            scene["capa"] = {
                "tipo": "dato",
                "fuente": "SRC-001, Figure 8",
                "valores": [{"etiqueta": "Flow front", "valor": 6148, "unidad": "m"}],
            }
        scenes.append(scene)
    return {
        "_schema": "CAPCOT_STORYBOARD_TEXT_V2",
        "project_id": "2026-11-30_test",
        "serie": "Datos y ociosidades",
        "title": "Test storyboard",
        "titulo": "Hook test",
        "language": "es-MX",
        "aspect_ratio": "9:16",
        "target_duration_seconds": 84,
        "fecha_objetivo": "2026-11-30",
        "slot_local": "07:00",
        "estructura": "historia",
        "trend_source": {
            "termino": "deep-sea pyroclastic deposits",
            "fecha_publicacion": "2026-11-23",
            "url": "https://example.org/primary-source",
        },
        "estilo_id": "atlas_antiguo",
        "visual_identity": {
            "style_id": "atlas_antiguo",
            "prompt_base": PROMPT_BASE,
        },
        "typography_identity": {
            "font_family": "DejaVu Sans",
            "title_style": "Maximum six words",
            "subtitle_style": "Short blocks",
        },
        "voice": {
            "engine": "edge-tts",
            "voice_id": "es-MX-JorgeNeural",
            "language": "es-MX",
            "rate": "+7%",
            "pitch": "-2Hz",
        },
        "sources": [{
            "id": "SRC-001",
            "cita_corta": "Primary research article.",
            "url": "https://example.org/primary-source",
            "doi": None,
            "verification_status": "VERIFICADO_RESOLVEDOR",
        }],
        "scenes": scenes,
        "cortinilla_fuentes": {
            "duration_seconds": 6,
            "source_ids": ["SRC-001"],
        },
        "audio": {
            "music_asset": None,
            "cama_musical": "arpegio",
            "music_plan": "Text-only plan; no asset.",
        },
        "export": {
            "resolution": "1080x1920",
            "fps": 30,
            "render_status": "NOT_GENERATED",
        },
        "publicacion": {
            "status": "PENDIENTE_DECISION_GROK",
            "platforms": ["YouTube Shorts"],
        },
        "narrative_contract": {
            "central_question": "What formed the deposits?",
            "promise": "Explain the observed evidence.",
            "stakes": "Avoid overstating the evidence.",
            "scientific_turn": "A pressure-related mechanism is proposed.",
            "evidence_limit": "The vents are not located.",
            "payoff": "The rocks preserve the evidence.",
        },
        "approved_assets": [],
        "production_mode": "storyboard_only",
    }


class StoryboardValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.old_root = validator.ROOT
        validator.ROOT = str(self.root)
        (self.root / "scripts").mkdir()
        (self.root / "scripts" / "estilos.json").write_text(
            json.dumps({"atlas_antiguo": {"prompt_base": PROMPT_BASE}}),
            encoding="utf-8",
        )
        self.storyboard_path = self.root / "storyboard.json"
        self.write_storyboard(fixture_storyboard())

    def tearDown(self):
        validator.ROOT = self.old_root
        self.tmp.cleanup()

    def write_storyboard(self, value):
        self.storyboard_path.write_text(
            json.dumps(value, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def test_structural_only_accepts_draft_without_narrative_qa(self):
        errors, warnings = validator.validar(
            str(self.storyboard_path),
            structural_only=True,
        )
        self.assertEqual(errors, [])
        self.assertNotIn("narrative_qa", fixture_storyboard())
        self.assertEqual(warnings, [])

    def test_full_mode_still_requires_independent_narrative_qa(self):
        errors, _ = validator.validar(str(self.storyboard_path))
        self.assertIn("falta campo raíz: narrative_qa", errors)

    def test_structural_only_still_enforces_not_generated(self):
        value = fixture_storyboard()
        value["export"]["render_status"] = "RENDERED"
        self.write_storyboard(value)
        errors, _ = validator.validar(
            str(self.storyboard_path),
            structural_only=True,
        )
        self.assertIn(
            "export.render_status debe ser NOT_GENERATED en preproducción textual",
            errors,
        )

    def test_boolean_terrestrial_coordinates_are_rejected(self):
        self.assertFalse(validator.validar_punto_mapa({"lat": True, "lon": -70}))
        self.assertFalse(validator.validar_punto_mapa({"lat": 10, "lon": False}))

    def test_boolean_celestial_coordinates_are_rejected(self):
        point = {
            "ra_deg": True,
            "dec_deg": 12.5,
            "sistema_coordenadas": "Ecuatoriales J2000 (RA/Dec)",
        }
        self.assertFalse(validator.validar_punto_mapa(point))

    def test_boolean_map_bounds_are_rejected(self):
        self.assertFalse(validator.validar_bounds_mapa([True, -70, 12, -60]))
        self.assertFalse(validator.validar_bounds_mapa([-10, -70, 12, False]))

    def test_valid_map_bounds_pass(self):
        self.assertTrue(validator.validar_bounds_mapa([-10, -70, 12, -60]))

    def test_check_doi_rejects_untrusted_input_before_network(self):
        with mock.patch.object(validator.http.client, "HTTPSConnection") as connection:
            self.assertFalse(validator.check_doi("file:///etc/passwd"))
            self.assertFalse(validator.check_doi("10.1234/example?next=https://evil.test"))
            connection.assert_not_called()

    def test_check_doi_uses_fixed_https_host_and_verified_tls(self):
        class Response:
            status = 200
            def getheader(self, name):
                return None

        class Connection:
            def __init__(self, host, timeout, context):
                self.host = host
                self.timeout = timeout
                self.context = context
            def request(self, method, path, headers):
                self.request_args = (method, path, headers)
            def getresponse(self):
                return Response()
            def close(self):
                pass

        with mock.patch.object(
            validator.http.client, "HTTPSConnection", side_effect=Connection
        ) as factory:
            self.assertTrue(validator.check_doi("10.5194/bg-15-5131-2018"))
            self.assertEqual(factory.call_args.args[0], "api.crossref.org")
            self.assertEqual(factory.call_args.kwargs["timeout"], 20)
            context = factory.call_args.kwargs["context"]
            self.assertTrue(context.check_hostname)
            self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)

    def test_check_doi_uses_fixed_doi_resolver_without_following_redirect(self):
        class Response:
            def __init__(self, status, location=None):
                self.status = status
                self.location = location
            def getheader(self, name):
                return self.location if name.lower() == "location" else None

        class Connection:
            def __init__(self, host, timeout, context):
                self.host = host
                self.timeout = timeout
            def request(self, method, path, headers):
                self.request_args = (method, path, headers)
            def getresponse(self):
                if self.host == "api.crossref.org":
                    raise OSError("Crossref unavailable")
                return Response(302, "https://journals.example.org/article")
            def close(self):
                pass

        with mock.patch.object(
            validator.http.client, "HTTPSConnection", side_effect=Connection
        ) as factory:
            self.assertTrue(validator.check_doi("10.5194/bg-15-5131-2018"))
            self.assertEqual(
                [call.args[0] for call in factory.call_args_list],
                ["api.crossref.org", "doi.org"],
            )

    def test_doi_check_falls_back_from_crossref_to_resolver(self):
        with mock.patch.object(
            validator, "_https_status",
            side_effect=[(None, None), (302, "https://publisher.example/article")],
        ) as request:
            self.assertTrue(validator.check_doi("10.1234/example"))
        self.assertEqual(
            request.call_args_list[0].args,
            ("api.crossref.org", "/works/10.1234/example"),
        )
        self.assertEqual(
            request.call_args_list[1].args,
            ("doi.org", "/10.1234/example"),
        )

    def test_doi_check_fails_if_both_endpoints_fail(self):
        with mock.patch.object(validator, "_https_status", return_value=(None, None)):
            self.assertFalse(validator.check_doi("10.1234/example"))

    def test_url_check_accepts_primary_http_response(self):
        with mock.patch.object(validator.urllib.request, "urlopen", return_value=FakeResponse()):
            self.assertTrue(validator.check_url("https://example.org/primary-source"))

    def test_url_check_rejects_non_http_scheme(self):
        self.assertFalse(validator.check_url("file:///etc/passwd"))

    def test_check_doi_flag_checks_url_when_source_has_no_doi(self):
        with mock.patch.object(validator, "check_url", return_value=False):
            errors, _ = validator.validar(
                str(self.storyboard_path),
                doi=True,
                structural_only=True,
            )
        self.assertTrue(any("URL de fuente no confirmada por HTTP" in error for error in errors))


class FakeResponse:
    status = 200

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False


if __name__ == "__main__":
    unittest.main()
