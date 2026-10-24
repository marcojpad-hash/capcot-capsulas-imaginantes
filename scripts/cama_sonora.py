#!/usr/bin/env python3
"""Cama sonora 100% sintetizada (numpy): ambiente por escena + música con pulso suave.
Obra propia generada por el pipeline -> sin derechos de terceros (equivale a CC0; ver docs/AUDIO_LICENCIAS.md).
Ambientes: oceano, puerto (oleaje + motor de lancha + crujidos), viento, viento_fuerte, lluvia,
tormenta (lluvia + truenos graves), mercado (murmullo de voces filtrado), silencio. Combinables con '+'."""
import wave
import numpy as np

SR = 48000
rng = np.random.default_rng(7)

def _ruido(n, color="white"):
    w = rng.standard_normal(n)
    if color == "white": return w
    f = np.fft.rfft(w); k = np.arange(len(f)); k[0] = 1
    f /= np.sqrt(k) if color == "pink" else k
    x = np.fft.irfft(f, n); return x / (np.abs(x).max() + 1e-9)

def _lp(x, fc):  # paso-bajo de 1 polo, aplicado 2 veces
    a = np.exp(-2 * np.pi * fc / SR)
    from scipy.signal import lfilter
    for _ in range(2): x = lfilter([1 - a], [1, -a], x)
    return x

def _bp(x, lo, hi):
    from scipy.signal import butter, sosfilt
    return sosfilt(butter(2, [lo, hi], btype="band", fs=SR, output="sos"), x)

def _norm(x, rms=0.1):
    return x * rms / (np.sqrt(np.mean(x ** 2)) + 1e-9)

def ambiente(tipo, seg):
    n = int(seg * SR); t = np.arange(n) / SR; out = np.zeros(n)
    for a in tipo.split("+"):
        if a == "oceano":
            ola = 0.25 + 0.75 * np.sin(np.pi * t / 8.5 + rng.uniform(0, 3)) ** 4
            x = _lp(_ruido(n, "brown"), 700) * ola + 0.3 * _bp(_ruido(n), 1500, 5000) * ola ** 2
        elif a == "puerto":
            x = 0.6 * ambiente("oceano", seg)
            motor = np.sin(2 * np.pi * 38 * t) * (0.6 + 0.4 * np.sin(2 * np.pi * 9 * t)) + 0.5 * np.sin(2 * np.pi * 76 * t)
            x = x + 0.25 * _norm(_lp(motor + 0.3 * _ruido(n), 300))
            for c in rng.uniform(0, seg, int(seg / 3)):  # crujidos de madera
                i = int(c * SR); m = min(n - i, int(0.25 * SR))
                x[i:i + m] += 0.4 * _bp(_ruido(m), 300, 900) * np.exp(-np.arange(m) / (0.05 * SR))
        elif a in ("viento", "viento_fuerte"):
            g = 0.4 + 0.6 * (0.5 + 0.5 * np.sin(2 * np.pi * 0.09 * t) * np.sin(2 * np.pi * 0.031 * t + 1))
            x = _bp(_ruido(n, "pink"), 250, 1400 if a == "viento" else 2500) * g ** (1 if a == "viento" else 2)
            if a == "viento_fuerte": x *= 1.6
        elif a in ("lluvia", "tormenta"):
            x = _bp(_ruido(n), 2000, 9000) * 0.6
            for c in rng.uniform(0, seg, int(seg * 25)):  # gotas
                i = int(c * SR); m = min(n - i, 300)
                x[i:i + m] += rng.uniform(.3, 1) * np.sin(2 * np.pi * rng.uniform(2e3, 5e3) * np.arange(m) / SR) * np.exp(-np.arange(m) / 40)
            if a == "tormenta":
                for c in rng.uniform(0, seg, max(1, int(seg / 6))):
                    i = int(c * SR); m = min(n - i, int(2.5 * SR))
                    x[i:i + m] += 4 * _lp(_ruido(m, "brown"), 120) * np.exp(-np.arange(m) / (0.7 * SR))
        elif a == "mercado":
            voces = sum(_bp(_ruido(n), f, f * 1.6) * (0.5 + 0.5 * np.sin(2 * np.pi * rng.uniform(2, 5) * t + k)) ** 2
                        for k, f in enumerate([300, 450, 700, 1100]))
            x = voces
        elif a in ("", "silencio"): continue
        else: raise SystemExit(f"ambiente desconocido: {a}")
        out += _norm(x)
    return out

def pista_ambiente(escenas, total):
    """escenas: [(tipo, dur_s)]; crossfade 0.4 s entre escenas; relleno silencioso hasta total."""
    n = int(total * SR); out = np.zeros(n); pos = 0; xf = int(0.4 * SR)
    for tipo, d in escenas:
        seg = ambiente(tipo, d + 0.4); m = len(seg)
        env = np.ones(m); env[:xf] = np.linspace(0, 1, xf); env[-xf:] = np.linspace(1, 0, xf)
        e = min(n, pos + m); out[pos:e] += (seg * env)[:e - pos]; pos += int(d * SR)
    return out

NOTAS = {"A1": 55.0, "F1": 43.65, "C2": 65.41, "G1": 49.0, "A3": 220.0, "C4": 261.63, "E4": 329.63,
         "F3": 174.61, "G3": 196.0, "B3": 246.94, "D4": 293.66, "E3": 164.81}
PROG = [("A1", ["A3", "C4", "E4"]), ("F1", ["F3", "A3", "C4"]), ("C2", ["G3", "C4", "E4"]), ("G1", ["G3", "B3", "D4"])]

NOTAS.update({"D2": 73.42, "E2": 82.41, "D3": 146.83, "A4": 440.0, "G4": 392.0, "B4": 493.88, "D5": 587.33, "E5": 659.25})
# Camas musicales (regla anti 'contenido en serie', YouTube 2801973): varias, rotadas, todas síntesis propia (licencia: obra propia).
CAMAS = {
    "pulso":    {"bpm": 92,  "prog": PROG, "timbre": "pad",     "bateria": "lofi"},
    "marimba":  {"bpm": 104, "prog": [("C2", ["C4", "E4", "G4"]), ("A1", ["A3", "C4", "E4"]), ("F1", ["F3", "A3", "C4"]), ("G1", ["G3", "B3", "D4"])], "timbre": "marimba", "bateria": "shaker"},
    "pizzicato":{"bpm": 84,  "prog": [("D2", ["D4", "F3", "A3"]), ("A1", ["A3", "C4", "E4"]), ("G1", ["G3", "B3", "D4"]), ("A1", ["A3", "C4", "E4"])], "timbre": "pluck", "bateria": "suave"},
    "arpegio":  {"bpm": 112, "prog": [("E2", ["E4", "G4", "B4"]), ("C2", ["C4", "E4", "G4"]), ("G1", ["G4", "B4", "D5"]), ("D2", ["D4", "A4", "D5"])], "timbre": "arp", "bateria": "lofi"},
    "tambor":   {"bpm": 96,  "prog": [("A1", ["A3", "E4", "A4"]), ("G1", ["G3", "D4", "G4"]), ("F1", ["F3", "C4", "A4"]), ("E2", ["E4", "B3", "E4"])], "timbre": "pad", "bateria": "mano"},
}

def musica(total, bpm=92, cama="pulso"):
    """Cama musical sintetizada. `cama` elige variante de CAMAS (tempo, progresión, timbre, batería)."""
    cfg = CAMAS.get(cama, CAMAS["pulso"]); bpm = cfg["bpm"] if cama in CAMAS else bpm
    if cfg["timbre"] != "pad" or cfg["bateria"] != "lofi" or cama != "pulso": return _musica_var(total, cfg)
    n = int(total * SR); out = np.zeros(n); beat = 60 / bpm; t = np.arange(n) / SR
    def put(x, s):
        i = int(s * SR); m = min(len(x), n - i)
        if m > 0: out[i:i + m] += x[:m]
    kt = np.arange(int(0.35 * SR)) / SR
    kick = np.sin(2 * np.pi * (45 * kt + 60 * (1 - np.exp(-kt * 30)) / 30)) * np.exp(-kt * 9) * 0.9
    ht = int(0.05 * SR); hat = _bp(_ruido(ht), 6000, 12000) * np.exp(-np.arange(ht) / (0.012 * SR)) * 0.25
    b = 0
    while b * beat < total:
        s = b * beat
        if b % 4 in (0, 2): put(kick, s)
        if b % 8 == 7: put(kick * 0.4, s + beat / 2)
        put(hat * (1 if b % 2 else 0.7), s); put(hat * 0.5, s + beat / 2)
        b += 1
    bar = 4 * beat; k = 0
    while k * bar < total:
        raiz, acorde = PROG[k % 4]; m = int(bar * SR); tt = np.arange(m) / SR
        env = np.minimum(1, tt / 0.3) * np.minimum(1, (bar - tt) / 0.4)
        bajo = np.sin(2 * np.pi * NOTAS[raiz] * 2 * tt) * np.exp(-((tt % (2 * beat)) * 2.5)) * 0.5
        pad = sum(np.sin(2 * np.pi * NOTAS[x] * tt + j) * (1 + 0.2 * np.sin(2 * np.pi * 0.3 * tt)) for j, x in enumerate(acorde)) * 0.12
        put((bajo + _lp(pad, 1500)) * env, k * bar); k += 1
    fade = np.minimum(1, t / 1.0) * np.minimum(1, (total - t) / 2.5)
    return out * fade

def _musica_var(total, cfg):
    n = int(total * SR); out = np.zeros(n); beat = 60 / cfg["bpm"]; t = np.arange(n) / SR
    def put(x, s):
        i = int(s * SR); m = min(len(x), n - i)
        if m > 0: out[i:i + m] += x[:m]
    kt = np.arange(int(0.3 * SR)) / SR
    kick = np.sin(2 * np.pi * (48 * kt + 50 * (1 - np.exp(-kt * 30)) / 30)) * np.exp(-kt * 10) * 0.8
    st = int(0.06 * SR); shk = _bp(_ruido(st), 5000, 10000) * np.exp(-np.arange(st) / (0.02 * SR)) * 0.18
    tom = np.sin(2 * np.pi * 140 * kt * np.exp(-kt * 3)) * np.exp(-kt * 14) * 0.6
    b = 0
    while b * beat < total:
        s0 = b * beat; bt = cfg["bateria"]
        if bt == "lofi":
            if b % 4 in (0, 2): put(kick, s0)
            put(shk, s0 + beat / 2)
        elif bt == "shaker":
            if b % 4 == 0: put(kick * 0.8, s0)
            for q in range(4): put(shk * (1 if q % 2 else 0.5), s0 + q * beat / 4)
        elif bt == "suave":
            if b % 4 == 0: put(kick * 0.6, s0)
            if b % 2: put(shk * 0.6, s0)
        elif bt == "mano":
            put(tom * (1 if b % 2 == 0 else 0.6), s0)
            if b % 4 == 3: put(tom * 0.5, s0 + beat / 2)
            put(shk * 0.5, s0 + beat / 2)
        b += 1
    bar = 4 * beat; k = 0
    while k * bar < total:
        raiz, acorde = cfg["prog"][k % len(cfg["prog"])]; m = int(bar * SR); tt = np.arange(m) / SR
        env = np.minimum(1, tt / 0.05) * np.minimum(1, (bar - tt) / 0.3)
        seg = np.sin(2 * np.pi * NOTAS[raiz] * 2 * tt) * np.exp(-((tt % (2 * beat)) * 2.0)) * 0.45
        tim = cfg["timbre"]
        if tim == "pad":
            seg += _lp(sum(np.sin(2 * np.pi * NOTAS[x] * tt + j) for j, x in enumerate(acorde)) * 0.12, 1500)
        else:
            sub = {"marimba": beat / 2, "pluck": beat, "arp": beat / 4}[tim]; dec = {"marimba": 9, "pluck": 6, "arp": 12}[tim]
            q = 0
            while q * sub < bar - 1e-6:
                f0 = NOTAS[acorde[q % len(acorde)]] * (2 if tim == "marimba" else 1)
                L = int(min(sub * 2, bar - q * sub) * SR); u = np.arange(L) / SR
                w = np.sin(2 * np.pi * f0 * u) + (0.3 * np.sin(2 * np.pi * f0 * 4 * u) if tim == "marimba" else 0.4 * np.sin(2 * np.pi * f0 * 2 * u))
                i0 = int(q * sub * SR); seg[i0:i0 + L] += (w * np.exp(-u * dec) * 0.22)[:m - i0]; q += 1
        put(seg * env, k * bar); k += 1
    return out * np.minimum(1, t / 1.0) * np.minimum(1, (total - t) / 2.5)

def guardar(x, path, rms=0.1):
    x = _norm(x, rms); x = np.clip(x, -0.98, 0.98)
    st = np.repeat((x * 32767).astype(np.int16)[:, None], 2, axis=1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())

# ---- SFX por plano con grabaciones reales CC0/dominio público (scripts/sfx_manifest.json) ----
UNA_VEZ = {"gaviotas", "gaviotas2", "madera"}  # efectos puntuales: se colocan una vez, no en bucle
SINTETICOS = {"oceano", "puerto", "viento_fuerte", "mercado", "silencio", "motor", "redes"}
_cache = {}

def _cargar(path):
    if path not in _cache:
        import subprocess
        raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"])
        x = np.frombuffer(raw, np.int16).astype(float) / 32768; _cache[path] = _norm(x[np.abs(x) > 0][:] if False else x)
    return _cache[path]

def _sfx(nombre, seg, carpeta):
    n = int(seg * SR)
    if nombre == "motor":
        t = np.arange(n) / SR; m = np.sin(2*np.pi*42*t)*(0.6+0.4*np.sin(2*np.pi*11*t)) + 0.5*np.sign(np.sin(2*np.pi*21*t))
        return _norm(_lp(m + 0.2*_ruido(n), 400))
    if nombre == "redes":  # cuerda/red: crujidos de madera reales + roce
        return _sfx("madera", seg, carpeta) + 0.3 * _norm(_bp(_ruido(n), 2000, 6000)) * (np.random.default_rng(1).random(n) > 0.6)
    if nombre in SINTETICOS: return ambiente(nombre, seg)
    import glob
    f = glob.glob(os.path.join(carpeta, nombre + ".*"))
    if not f: raise SystemExit(f"sfx desconocido: {nombre} (ver scripts/sfx_manifest.json)")
    x = _cargar(f[0])
    if nombre in UNA_VEZ:
        out = np.zeros(n); i = int(0.3 * SR); m = min(len(x), n - i)
        if m > 0: out[i:i + m] = x[:m]
        return out
    o = int(rng.uniform(0, max(len(x) - n, 1))) if len(x) > n else 0
    return np.resize(x[o:], n) if len(x) - o < n else x[o:o + n]

import os
def pista_sfx(planos, total, carpeta):
    """planos: [(sfx 'a+b', dur_s)] en orden; crossfade 0.3 s entre planos."""
    n = int(total * SR); out = np.zeros(n); pos = 0; xf = int(0.3 * SR)
    for tipo, d in planos:
        seg = sum(_sfx(a, d + 0.3, carpeta) for a in tipo.split("+") if a) if tipo else np.zeros(int((d + .3) * SR))
        if np.isscalar(seg): seg = np.zeros(int((d + .3) * SR))
        m = len(seg); env = np.ones(m); env[:xf] = np.linspace(0, 1, xf); env[-xf:] = np.linspace(1, 0, xf)
        e = min(n, pos + m); out[pos:e] += (seg * env)[:e - pos]; pos += int(d * SR)
    return out
