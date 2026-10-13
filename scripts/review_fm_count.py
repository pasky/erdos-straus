"""R195: from-scratch count of G(d) = #{f monic irreducible, deg d, f not | A P s, f = -1 mod A,
-P/A square mod f (q odd), s primitive root mod f}  (FF_MUTE Lemma 3.1 (i)-(iii)) by direct exponentiation,
compared with the main term delta q^d / d.  Usage: review_fm_count.py q Acoeffs scoeffs d nP"""
import sys
import random
import sympy
from review_fm_ff import GF


def parse(s):
    return tuple(int(c) for c in s.split(','))


def G(F, A, s, P, d, irr_d):
    q = F.q
    e = q ** d - 1
    primes = list(sympy.factorint(e))
    cnt = 0
    for f in irr_d:
        if f in (s, P) or F.pmod(A, f) == ():
            continue
        if F.pmod(F.padd(f, (1,)), A) != ():
            continue
        if q % 2:
            invA = F.ppowmod(A, e - 1, f)
            w = F.pmod(F.pscale(F.minus_one, F.pmul(P, invA)), f)
            if F.ppowmod(w, e // 2, f) != (1,):
                continue
        if any(F.ppowmod(s, e // l, f) == (1,) for l in primes):
            continue
        cnt += 1
    return cnt


if __name__ == "__main__":
    q = int(sys.argv[1]); A = parse(sys.argv[2]); s = parse(sys.argv[3]); d = int(sys.argv[4]); nP = int(sys.argv[5])
    F = GF(q)
    random.seed(1)
    PhiA = 1
    for g, ex in F.factor(A).items():
        PhiA *= (q ** (len(g) - 1) - 1) * q ** ((len(g) - 1) * (ex - 1))
    delta = sympy.totient(q - 1) / ((2 if q % 2 else 1) * (q - 1) * PhiA)
    irr = F.irreds(d)
    Ps = []
    for n in range(1, 6):
        Ps += [P for P in F.irreds(n) if F.pmod(A, P) != () and P != s]
    random.shuffle(Ps)
    out = [G(F, A, s, P, d, irr) for P in Ps[:nP]]
    print(f"q={q} A={A} s={s} d={d}: G(d) over {len(out)} random irreducible P: {out}; "
          f"min {min(out)} mean {sum(out)/len(out):.1f}; main term delta q^d/d = {delta * q ** d / d:.1f}")
