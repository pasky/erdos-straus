"""Shared helpers for z52b Pass-1 batch U01 (reads existing raw data; no new heavy compute)."""
import json, os, math
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(REPO, "data/z52b/raw")
OUT = os.path.join(REPO, "data/z52b/pass1/outcome_U01.jsonl")

def load_counts(path):
    """Rows: n U D O minz minz_x minz_y maxx minx nx k1 k2 k3 minlcm (U = #unordered sols of m/n)."""
    d = {}
    with open(path) as f:
        for line in f:
            t = line.split()
            if len(t) < 4: continue
            d[int(t[0])] = [int(x) for x in t[1:]]
    return d

def load_m(m):
    """Prime-n counts for numerator m (m/p, p<=1e5) from raw m{m}_pr1e5.txt; returns {p: U}."""
    p = os.path.join(RAW, f"m{m}_pr1e5.txt")
    return {n: v[0] for n, v in load_counts(p).items()}

def primes_upto(N):
    s = bytearray([1])*(N+1); s[0]=s[1]=0
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(N+1) if s[i]]

def rec(mid, outcome, summary, evidence, nxt=""):
    assert outcome in ("nothing","covered","interesting","needs-compute","skipped")
    row = {"mid": mid, "outcome": outcome, "summary": summary, "evidence": evidence, "next": nxt}
    with open(OUT, "a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
