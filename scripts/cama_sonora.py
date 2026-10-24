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

def musica(total, bpm=92):
    """Lo-fi sutil: kick suave en 1 y 3 (+ fantasma), hat cerrado en corcheas, bajo y pad por compás."""
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

def guardar(x, path, rms=0.1):
    x = _norm(x, rms); x = np.clip(x, -0.98, 0.98)
    st = np.repeat((x * 32767).astype(np.int16)[:, None], 2, axis=1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
