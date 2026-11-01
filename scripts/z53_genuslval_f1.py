"""Falsifier F1 for Theorem U (Z53_GENUSLVAL.md): windowed family sums vs predicted main term.
Runs the C engine z53_genuslval_family.c, computes A_u = (6/pi^2) prod_{l|2up} l/(l+1) * L(1,chi_{-4up}) from exact
class numbers (pari qfbclassno; L(1,chi_D) = pi h(D)/sqrt|D| for D < -4) and compares, per u and in total:
  S1_u (eta=1 windowed sum)  vs  A_u log(X/Y)
  F_u  (genus family slice)   vs  A_u log(X/Y)/phi(u)
Usage: uv run --with cypari2 python scripts/z53_genuslval_f1.py p U0 U1 Y X [M]
"""
import sys, subprocess, math, os
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9, silent=True) if False else None

def main():
    p, U0, U1, Y, X = map(int, sys.argv[1:6]); doM = len(sys.argv) > 6
    exe = '/tmp/z53fam'
    src = os.path.join(os.path.dirname(__file__), 'z53_genuslval_family.c')
    if not os.path.exists(exe):
        subprocess.check_call(['gcc', '-O2', '-o', exe, src, '-lm'])
    out = subprocess.run([exe, str(p), str(U0), str(U1), str(Y), str(X)] + (['M'] if doM else []),
                         capture_output=True, text=True, check=True).stdout.strip().split('\n')
    tot = out[-1]; rows = [l.split() for l in out[:-1]]
    lg = math.log(X / Y)
    sumF = sumPred = 0.0; worst = 0.0; s1err = []
    for r in rows:
        u = int(r[0]); F = float(r[1]); S1 = float(r[2])
        D = -4 * u * p
        h = int(pari.qfbclassno(D))
        L1 = math.pi * h / math.sqrt(-D)
        fac = 1.0
        for l in [int(x) for x in pari.factor(2 * u * p)[0]]:
            fac *= l / (l + 1)
        A = 6 / math.pi ** 2 * fac * L1
        phiu = int(pari.eulerphi(u))
        sumF += F; sumPred += A * lg / phiu
        s1err.append(S1 - A * lg)
        worst = max(worst, abs(S1 - A * lg) / (A * lg))
    print(f"p={p} U=({U0},{U1}] W=({Y},{X}] nu={len(rows)} log(X/Y)={lg:.3f}")
    print(f"  family F = {sumF:.4f}  predicted main = {sumPred:.4f}  ratio = {sumF/sumPred:.4f}")
    print(f"  eta=1 slices: max rel err |S1-A log|/(A log) = {worst:.4f}; mean abs err = "
          f"{sum(abs(e) for e in s1err)/len(s1err):.4f}; mean err = {sum(s1err)/len(s1err):+.4f}")
    print("  " + tot)
    print(f"  log^2 p = {math.log(p)**2:.2f};  F/log^2 p = {sumF/math.log(p)**2:.5f}")

if __name__ == '__main__':
    main()
