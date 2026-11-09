# z68_sign_graph_agg.py FILE [FILE...] — aggregate z68_sign_graph.c output by record (keyed by n and record type),
# from exact integer counts (COUNTS line) plus the component and minimax lines.  Prints per-band tables with explicit
# denominators and the prime-level success table for the registered kill threshold (>= 99 % of primes <= 1e5).
import re, sys, statistics as st
from collections import defaultdict

def parse(fn):
    R = defaultdict(dict)
    for line in open(fn):
        m = re.match(r'n=(\d+) (\S+)', line)
        if not m: continue
        n = int(m.group(1))
        if ' COUNTS ' in line:
            R[n]['C'] = {k: int(v) for k, v in re.findall(r'(\w+)=(-?\d+)', line.split(' COUNTS ', 1)[1])}
        elif ' giant=' in line:
            g = dict(re.findall(r'(\w[\w+]*)=([-\d./]+)', line))
            fl = dict(re.findall(r'(S[12]\w+\+?):(\d)', line))
            R[n]['G'] = {'giant': float(g['giant']), 'giantp': float(g['giant+']), 'giantpsign': int(g['giant+sign']),
                         'L3inG': tuple(map(int, g['L3inGiant'].split('/'))), 'goodL3inG': int(g['goodL3inGiant']),
                         'goodL3inGp': int(g['goodL3inGiant+']), **{k: int(v) for k, v in fl.items()}}
        elif 'minimax-height' in line:
            mm = re.search(r'S1\(len (-?\d+)\): E (-?\d+) E\+ (-?\d+) \| S2\(len (-?\d+)\): E (-?\d+) E\+ (-?\d+)', line)
            R[n]['H'] = dict(zip(['l1', 'h1', 'h1p', 'l2', 'h2', 'h2p'], map(int, mm.groups())))
    return R

def pct(a, b): return f"{a}/{b} = {100.0 * a / b:.3f} %" if b else f"{a}/0"

def report(R, bands):
    for lo, hi in bands:
        ns = sorted(n for n in R if lo < n <= hi and 'C' in R[n] and 'G' in R[n])
        if not ns: continue
        for n in ns: assert 'H' in R[n], n
        C = [R[n]['C'] for n in ns]; G = [R[n]['G'] for n in ns]; H = [R[n]['H'] for n in ns]; N = len(ns)
        print(f"== ({lo}, {hi}]: {N} records")
        print(f"  giant mean {st.mean(g['giant'] for g in G):.4f} (min {min(g['giant'] for g in G):.4f}); E+ giant band mean "
              f"{st.mean(g['giantp'] for g in G):.4f}, per-n range [{min(g['giantp'] for g in G):.4f}, {max(g['giantp'] for g in G):.4f}];"
              f" moves/V band mean {st.mean(c['moves'] / c['V'] for c in C):.3f}")
        print(f"  all L3 in giant: {pct(sum(g['L3inG'][0] == g['L3inG'][1] for g in G), N)}; good L3 in giant: {pct(sum(g['goodL3inG'] > 0 for g in G), N)};"
              f" E+ giant good-signed: {pct(sum(g['giantpsign'] == -1 for g in G), N)}")
        print(f"  D (strict descent to good L3) among good words of length >= 4: per-n mean {100 * st.mean(c['inD'] / c['goodlen4'] for c in C):.3f} %,"
              f" pooled {pct(sum(c['inD'] for c in C), sum(c['goodlen4'] for c in C))}; D+ per-n mean {100 * st.mean(c['inDp'] / c['goodlen4'] for c in C):.3f} %")
        CS = [c for c in C if c['S3n'] > 0]
        if CS:
            print(f"  S3 (bounded-digit good words, letters <= 4, length >= 6; {len(CS)} records with S3 non-empty): per-n mean Rmin {100 * st.mean(c['S3Rmin'] / c['S3n'] for c in CS):.4f} %,"
                  f" D {100 * st.mean(c['S3D'] / c['S3n'] for c in CS):.4f} %; pooled Rmin {pct(sum(c['S3Rmin'] for c in CS), sum(c['S3n'] for c in CS))},"
                  f" D {pct(sum(c['S3D'] for c in CS), sum(c['S3n'] for c in CS))}")
        print(f"  prime-level: S1 Rmin {pct(sum(c['S1Rmin'] for c in C), N)}, S1 Rmin+ {pct(sum(c['S1Rminp'] for c in C), N)}, S2 Rmin {pct(sum(c['S2Rmin'] for c in C), N)},"
              f" S2 Rmin+ {pct(sum(c['S2Rminp'] for c in C), N)}, S2 in D {pct(sum(c['S2D'] for c in C), N)}, some S3 Rmin-success {pct(sum(c['S3anyRmin'] for c in C), N)},"
              f" some S3 in D {pct(sum(c['S3anyD'] for c in C), N)}")
        long1 = [c for c in C if c['S1len'] >= 4]
        print(f"  S1: length 2 at {pct(sum(c['S1len'] == 2 for c in C), N)}; length 3 (already an L3 word) at {pct(sum(c['S1len'] == 3 for c in C), N)};"
              f" genuinely long (>= 4): {len(long1)}, Rmin success among them {sum(c['S1Rmin'] for c in long1)}")
        print(f"  component of start contains good L3 (E / E+): S1 {pct(sum(g['S1comp'] for g in G), N)} / {pct(sum(g['S1comp+'] for g in G), N)};"
              f" S2 {pct(sum(g['S2comp'] for g in G), N)} / {pct(sum(g['S2comp+'] for g in G), N)}")
        h2 = [h['h2'] for h in H]; h2p = [h['h2p'] for h in H]; h1 = [h['h1'] for h in H]
        print(f"  minimax height from S2 (E): =4 at {pct(sum(x == 4 for x in h2), N)}, undefined at {sum(x < 0 for x in h2)}, max {max(h2)};"
              f" (E+): undefined at {sum(x < 0 for x in h2p)}, max {max(h2p)}; from S1 (E): undefined at {pct(sum(x < 0 for x in h1), N)}")

if __name__ == '__main__':
    bands = [(0, 1000), (1000, 10000), (10000, 30000), (30000, 60000), (60000, 100000), (0, 100000), (1000, 100000),
             (100000, 900000), (900000, 1000000)]
    for fn in sys.argv[1:]:
        print("#", fn); report(parse(fn), bands)
