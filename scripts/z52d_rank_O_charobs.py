"""C9 falsifier (rank_O): at (★)-hard primes vs controls, classify obstructed Type II e-slices
(e ≡ −p mod 4, N=(p+e)/4, success iff −1 ∈ {a·b⁻¹ mod e : ab | N, gcd(a,b)=1, gcd(ab,e)=1})
as SUBGROUP-type (−1 ∉ ⟨prime factors of N⟩ mod e, i.e. some odd character kills all factors)
or POVERTY-type (−1 in the subgroup but not in the ratio set). Subgroup-type windows are split into
  sub_chi_e   : killed by χ_{−e} itself (= Jacobi (·/e) for e ≡ 3 mod 4; the BM character of the slice),
  sub_real    : killed by SOME odd real (genus) character mod e (includes sub_chi_e),
  sub_nonreal : killed by no odd real character, only by characters of order ≥ 3.
Limited diagnostic (EVIDENCE): it does not measure the Z3003 Fourier products or common characters across windows."""
import sys, random
from itertools import combinations
from math import gcd, prod
def isprime(n):
    if n < 2: return False
    for d in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % d == 0: return n == d
    d, s = n-1, 0
    while d % 2 == 0: d//=2; s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True
def factor(n):
    f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d,0)+1; n//=d
        d += 1
    if n > 1: f[n] = f.get(n,0)+1
    return f
def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a//=2
            if n % 8 in (3,5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
def kron_minus_e(l, e):  # χ_{-e}(l) for odd prime l, e ≡ 3 mod 4 so -e ≡ 1 mod 4: = (l / e) Jacobi by reciprocity
    return jacobi(l, e)
def odd_real_killers(e, primes):
    qs = sorted(factor(e))
    for r in range(1, len(qs)+1):
        for S in combinations(qs, r):
            if sum(1 for q in S if q % 4 == 3) % 2 == 0: continue  # even character
            if all(prod(jacobi(l, q) for q in S) == 1 for l in primes):
                return True
    return False
def classify(p, E):
    out = {'ok':0, 'sub':0, 'sub_chi_e':0, 'sub_real':0, 'sub_nonreal':0, 'pov':0}
    e = (-p) % 4 or 4
    while e <= E:
        N = (p + e)//4; f = factor(N)
        primes = [l for l in f if gcd(l, e) == 1]
        divs = [1]
        for l, k in f.items():
            if gcd(l, e) != 1: continue
            divs = [d*l**i for d in divs for i in range(k+1)]
        rat = set()
        for a in divs:
            for b in divs:
                if gcd(a,b)==1 and N % (a*b) == 0: rat.add(a*pow(b,-1,e) % e)
        if e == 1 or (e-1) % e in rat: out['ok'] += 1
        else:
            H = {1 % e}; fr = [1 % e]
            while fr:
                x = fr.pop()
                for l in primes:
                    y = x*l % e
                    if y not in H: H.add(y); fr.append(y)
            if (e-1) in H: out['pov'] += 1
            else:
                out['sub'] += 1
                if all(kron_minus_e(l, e) == 1 for l in primes) and e % 4 == 3: out['sub_chi_e'] += 1
                if odd_real_killers(e, primes): out['sub_real'] += 1
                else: out['sub_nonreal'] += 1
        e += 4
    return out
hard = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321]
random.seed(7); E = int(sys.argv[1]) if len(sys.argv) > 1 else 400
print('E =', E)
for p in hard:
    ctrl = []
    while len(ctrl) < 3:
        q = random.randrange(int(p*0.5), int(p*1.5)) | 1
        if q % 24 == 1 and isprime(q) and q not in hard and q not in ctrl: ctrl.append(q)
    h = classify(p, E); cs = [classify(q, E) for q in ctrl]
    agg = {k: sum(c[k] for c in cs)/3 for k in h}
    print(p, ctrl, 'HARD', h, '| ctrl avg', {k: round(v,1) for k,v in agg.items()})
