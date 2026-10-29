#!/usr/bin/env python3
"""z51 linnik: union-bound mass of certificate boxes on a Pi-plane (EXSET_LINNIK §2.4, EVIDENCE).

Pi = primes in (y/2, y] (option --mod4 3: only q == 3 mod 4).  Sign pattern eps: each x_q is drawn from the
residue cell (eps=+1) or the non-residue cell (eps=-1) mod q.  Single-coordinate certificate boxes (h = q) are
removed from the cells (G_q); h = q^2 boxes and pair boxes (h = q q') are charged by the union bound.
Usage: z51_linnik_planemass.py y family(es5|U) pattern(nr|res|rand) [--triples] [--search K] [--mod4 3]
"""
import sys, math, random, json, argparse
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import z51_linnik_plane as P

def primes_in(a, b):
    return [q for q in range(max(3, a), b + 1) if all(q % d for d in range(2, math.isqrt(q) + 1))]

def legendre(a, q):
    r = pow(a % q, (q - 1) // 2, q)
    return 0 if r == 0 else (1 if r == 1 else -1)

def cert_boxes(h, Pi, fam):
    return {d["c"] for d in P.labels(h, Pi) if d[fam]}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("y", type=int); ap.add_argument("fam"); ap.add_argument("pattern")
    ap.add_argument("--triples", action="store_true"); ap.add_argument("--search", type=int, default=0)
    ap.add_argument("--mod4", type=int, default=0); ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default="")
    A = ap.parse_args()
    y = A.y
    Pi = [q for q in primes_in(y // 2 + 1, y) if (A.mod4 == 0 or q % 4 == A.mod4)]
    rnd = random.Random(A.seed)
    hmax = (y ** 3 if A.triples else y * y) + 10
    P.set_spf(min(3 * hmax + 10, 60_000_000))
    eps = {}
    for q in Pi:
        eps[q] = -1 if A.pattern == "nr" else (1 if A.pattern == "res" else (0 if A.pattern == "haar" else rnd.choice((-1, 1))))
    G = {}
    single_nr = []
    m_sq = 0.0
    for q in Pi:
        b1 = {c % q for c in cert_boxes(q, Pi, A.fam)}
        assert all(legendre(c, q) == -1 for c in b1), "plane parity law fails (single)"
        cell = [a for a in range(1, q) if eps[q] == 0 or legendre(a, q) == eps[q]]
        G[q] = [a for a in cell if a not in b1]
        nb_nr = len([c for c in b1 if legendre(c, q) == -1]); nb_r = len(b1) - nb_nr
        single_nr.append((q, len(b1), nb_nr, nb_r))
        b2 = cert_boxes(q * q, Pi, A.fam)
        Gs = set(G[q])
        m_sq += sum(1 for c in b2 if c % q in Gs) / (q * len(G[q]))
    m_pair = 0.0
    npairs = 0; lab_stats = []
    pair_boxes = {}
    for i, q in enumerate(Pi):
        for q2 in Pi[i + 1:]:
            h = q * q2
            labs = P.labels(h, Pi)
            bx = {d["c"] for d in labs if d[A.fam]}
            assert all(legendre(c, q) * legendre(c, q2) == -1 for c in bx), "plane parity law fails"
            lab_stats.append((len(labs), len(bx), math.log(h)))
            Gq, Gq2 = set(G[q]), set(G[q2])
            hit = [(c % q, c % q2) for c in bx if c % q in Gq and c % q2 in Gq2]
            pair_boxes[(q, q2)] = hit
            m_pair += len(hit) / (len(G[q]) * len(G[q2]))
            npairs += 1
    trip_boxes = {}
    m_trip = 0.0
    if A.triples:
        for i, q in enumerate(Pi):
            for j in range(i + 1, len(Pi)):
                for k in range(j + 1, len(Pi)):
                    q2, q3 = Pi[j], Pi[k]
                    h = q * q2 * q3
                    bx = cert_boxes(h, Pi, A.fam)
                    hit = [(c % q, c % q2, c % q3) for c in bx
                           if c % q in set(G[q]) and c % q2 in set(G[q2]) and c % q3 in set(G[q3])]
                    trip_boxes[(q, q2, q3)] = hit
                    m_trip += len(hit) / (len(G[q]) * len(G[q2]) * len(G[q3]))
    avg_lab = sum(a for a, b, l in lab_stats) / max(1, len(lab_stats))
    avg_box = sum(b for a, b, l in lab_stats) / max(1, len(lab_stats))
    avg_l2 = sum(l * l for a, b, l in lab_stats) / max(1, len(lab_stats))
    res = dict(y=y, fam=A.fam, pattern=A.pattern, nPi=len(Pi), mass_sq=m_sq, mass_pair=m_pair, mass_trip=m_trip,
               avg_labels_pair=avg_lab, avg_certboxes_pair=avg_box, avg_log2h=avg_l2,
               min_G_frac=min(len(G[q]) / ((q - 1) / 2) for q in Pi),
               singles=single_nr[:8])
    # random search for a point avoiding all single / square / pair (/ triple) boxes
    if A.search:
        found = 0
        for trial in range(A.search):
            x = {q: rnd.choice(G[q]) for q in Pi}
            ok = all((x[a], x[b]) not in set(hb) for (a, b), hb in pair_boxes.items())
            if ok and A.triples:
                ok = all((x[a], x[b], x[c]) not in set(hb) for (a, b, c), hb in trip_boxes.items())
            if ok:
                found += 1
        res["search_trials"] = A.search; res["search_found"] = found
    print(json.dumps(res))
    if A.out:
        with open(A.out, "a") as f:
            f.write(json.dumps(res) + "\n")

if __name__ == "__main__":
    main()
