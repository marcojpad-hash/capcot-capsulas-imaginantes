# Envoltura de scripts/montar_capsula.py: reintenta edge-tts cuando devuelve NoAudioReceived (fallo intermitente del servicio).
import sys, asyncio, runpy
sys.path.insert(0, '/workspace/capcot_main/scripts')
import montar_capsula as mc
_orig = mc._tts_one
async def _tts_one(*a, **k):
    for t in range(6):
        try: return await _orig(*a, **k)
        except Exception as e:
            if t == 5: raise
            print('reintento TTS', t + 1, repr(a[0])[:60], type(e).__name__, file=sys.stderr); await asyncio.sleep(3 + 3 * t)
mc._tts_one = _tts_one
mc.main()
