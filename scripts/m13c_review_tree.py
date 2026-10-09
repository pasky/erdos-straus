"""Second, independent check of O100 tree certificates, built on the R80 engine scripts/review_mordell_check.py
(sol / family_ok / identity_ok / covers: ET coordinates re-derived from the paper, exact Fractions,
integer-valuedness at s = 0..4, positivity).  Re-derives the partition from scratch: the leaves and open
leaves of every root must form a partition of the root's unit residues into classes mod their own L
(checked by measure: sum over leaves of phi-weights == 1, with each node's children = all units x+Lt mod Lp).
usage: m13c_review_tree.py tree.json"""
import sys, json
from fractions import Fraction as Fr
from review_mordell_check import family_ok, identity_ok, covers

def main():
    T = json.load(open(sys.argv[1]))
    assert sorted(r['x'] for r in T['roots']) == [112561, 352801, 380881, 418321, 473761, 483841]
    seen = {}; nleaf = nopen = 0; openm = Fr(0); total = Fr(0)
    def visit(nd, m):
        nonlocal nleaf, nopen, openm, total
        x, L = nd['x'], nd['L']
        ch = nd.get('children')
        if ch:
            p = nd['split']
            assert L * p == ch[0]['L']
            units = {(x + L * t) % (L * p) for t in range(p) if (x + L * t) % p != 0}
            xs = [c['x'] % (L * p) for c in ch]
            assert len(xs) == len(set(xs)) and set(xs) == units and all(c['L'] == L * p for c in ch)
            for c in ch:
                visit(c, m / len(units))
            return
        total += m
        if 'leaf' in nd:
            fam, P = nd['leaf'][2], tuple(nd['leaf'][3])
            k = (fam, P)
            if k not in seen:
                seen[k] = family_ok(fam, P) and identity_ok(fam, P)
            assert seen[k], k
            assert covers(fam, P, x, L), (x, L, k)
            nleaf += 1
        else:
            assert nd.get('open')
            nopen += 1; openm += m
    sys.setrecursionlimit(100000)
    for r in T['roots']:
        assert r['L'] == 720720
        visit(r, Fr(1, 6))
    assert total == 1
    print(f"review: {nleaf} leaves OK ({len(seen)} classes), {nopen} open, open density {float(openm):.4e}; partition mass {total}")
    print("REVIEW OK")

main()
