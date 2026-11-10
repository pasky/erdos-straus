# z70 LOOSE #10, exploratory (after the kill): EXACT (Lemma S) failure counts of the bounded menus
# NP_k = {first k prime quadratic non-residues of p} for primes p = 1 (mod 24), p <= N.  Uses the compiled exact decider.
import sys, subprocess
from sympy import primerange, legendre_symbol
N = int(sys.argv[1]); KMAX = 3; exe = sys.argv[2]
ps = [p for p in primerange(25, N + 1) if p % 24 == 1]
nr = {p: [q for q in primerange(3, 2000) if legendre_symbol(p % q, q) == -1][:KMAX] for p in ps}
def decide(pairs):
    inp = '\n'.join(f'{p} {d}' for p, d in pairs) + '\n'
    out = subprocess.run([exe, '/dev/stdin'], input=inp, capture_output=True, text=True, timeout=1700).stdout
    return {(int(l.split()[0]), int(l.split()[1])): l.split()[2] == 'NONEMPTY' for l in out.splitlines()}
alive = ps
for k in range(KMAX):
    res = decide([(p, nr[p][k]) for p in alive])
    alive = [p for p in alive if not res[(p, nr[p][k])]]
    print(f"N={N}: primes p = 1 (24): {len(ps)}; menu NP_{k+1} exact failures: {len(alive)}; "
          f"largest: {alive[-5:]}", flush=True)
