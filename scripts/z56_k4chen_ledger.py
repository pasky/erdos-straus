#!/usr/bin/env python3
"""z56 K4CHEN ledger: best model margin (direct + switching scheme, z56_k4chen_direct.py) per level theta.
Usage: python z56_k4chen_ledger.py r mode(bv|same) theta1,theta2,...   (pen = 1)"""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z56_k4chen_direct import evaluate
r = int(sys.argv[1]); mode = sys.argv[2]; thetas = [float(a) for a in sys.argv[3].split(',')]
ZG = {4: [0.01, 0.015, 0.02, 0.03, 0.04, 0.06], 2: [0.02, 0.04, 0.06, 0.08, 0.1, 0.13, 0.16, 0.2],
      0: [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45]}[r]
TG = [0.30, 0.33, 0.36, 0.39, 0.42, 0.45, 0.47, 0.49]
for theta in thetas:
    lamsw = 0.5 if mode == 'bv' else theta
    best = (-1e9, None)
    for zeta in ZG:
        for th1 in TG:
            if theta - zeta <= th1: continue
            v = evaluate(r, th1, zeta, theta, lamsw, 1.0, taus=list(np.linspace(0, min(theta - 0.02, 1.0), 41)))
            if v[0] > best[0]: best = v
    print(f"r={r} mode={mode} theta={theta}: margin={best[0]:.4f} {best[1]}", flush=True)
