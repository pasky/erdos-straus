"""O257 goal (3): sources q = p - delta (|delta| <= W) sharing p's quadratic profile ((q/l) = (p/l) for odd l <= B,
q ≡ p mod 8).  For every source witness w' (all ET representations) record:
  vis  : p is NOT a square mod H'  (Thm 3.2: necessary for a determined lift)
  det  : p has a witness with H | H'  (Thm 3.1: the determined lift exists)
  share: exact-share lift (Prop 1.4, alpha = 1): (II,e'-delta) / (I,1) / (II,1-delta) in Spec(p)
Usage: z28_matched.py k B W p1 p2 ...   (or 'mordell N' for all Mordell-class primes <= N)"""
import sys
from sympy import isprime, primerange, legendre_symbol
from z28_witness import reps, is_square_mod

def profile_match(p, q, B):
    if (p - q) % 8: return False
    return all(legendre_symbol(p % l, l) == legendre_symbol(q % l, l) for l in primerange(3, B + 1) if p % l and q % l)

def analyse(p, k, B, W, verbose=True):
    Rp = reps(p, k); Hp = [r[6] for r in Rp]; spec = {(r[0], r[5]) for r in Rp}
    tot = dict(src=0, w=0, vis=0, det=0, visdet=0, share=0, srcdet=0, srctot=0, srcvissuff=0)
    lines = []
    for q in range(max(3, p - W), p + W + 1):
        if q == p or not isprime(q) or k % q == 0 or not profile_match(p, q, B): continue
        d = p - q; R = reps(q, k)
        if not R: continue
        nv = nd = nvd = ns = 0
        for (th, a, b, c, dd, e, H) in R:
            vis = not is_square_mod(p, H)
            det = any(H % h == 0 for h in Hp)
            sh = (th == 'II' and (('II', e - d) in spec or (e - d == 1 and ('I', 1) in spec))) or \
                 (th == 'I' and e == 1 and ('II', 1 - d) in spec)
            nv += vis; nd += det; nvd += vis and det; ns += sh
            assert not det or vis       # Thm 3.2 consistency
        tot['src'] += 1; tot['w'] += len(R); tot['vis'] += nv; tot['det'] += nd; tot['visdet'] += nvd; tot['share'] += ns
        tot['srcdet'] += nd > 0; tot['srctot'] += nd == len(R); tot['srcvissuff'] += nv == nd
        lines.append(f"{q}({d:+d}):{nd}/{nv}/{len(R)}")
    if verbose:
        print(f"p={p} k={k} B={B} W={W} |W(p)|={len(Rp)} sources={tot['src']} witnesses={tot['w']} visible={tot['vis']} "
              f"det={tot['det']} share={tot['share']} | sources with >=1 det={tot['srcdet']} total={tot['srctot']} "
              f"vis-sufficient={tot['srcvissuff']}")
        print('   ' + ' '.join(lines[:14]) + (' ...' if len(lines) > 14 else ''))
    return tot

if __name__ == '__main__':
    k, B, W = map(int, sys.argv[1:4])
    if sys.argv[4] == 'mordell':
        N = int(sys.argv[5]); M = {1, 121, 169, 289, 361, 529}
        ps = [p for p in primerange(5, N + 1) if p % 840 in M]
        agg = {}
        for p in ps:
            t = analyse(p, k, B, W, verbose=False)
            for kk, v in t.items(): agg[kk] = agg.get(kk, 0) + v
            agg['p_all_src_det'] = agg.get('p_all_src_det', 0) + (t['src'] > 0 and t['srcdet'] == t['src'])
            agg['p_some_total'] = agg.get('p_some_total', 0) + (t['srctot'] > 0)
            agg['p_nosrc'] = agg.get('p_nosrc', 0) + (t['src'] == 0)
        print(f"Mordell primes <= {N}: {len(ps)}; k={k} B={B} W={W}; aggregate {agg}")
    else:
        for p in map(int, sys.argv[4:]): analyse(p, k, B, W)
