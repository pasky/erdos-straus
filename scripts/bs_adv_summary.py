"""O154: summary table of all logs/bs_adv_*.jsonl (exact f_II at single adversarial / control primes)."""
import json, glob, statistics as S, math
print("design | n | log10 p | mean f/L^3 | CV | min f/L^3 | min f | median Wmin | median emin | share e<=31 | all verified")
for fn in sorted(glob.glob('logs/bs_adv_*.jsonl')):
    R = [json.loads(l) for l in open(fn)]
    x = [r['fL3'] for r in R]
    print(f"{fn[12:-6]} | {len(R)} | {S.mean(math.log10(r['p']) for r in R):.1f} | {S.mean(x):.4f} | {S.pstdev(x)/S.mean(x):.3f} | "
          f"{min(x):.4f} | {min(r['f'] for r in R)} | {S.median(r['Wmin'] for r in R)} | {S.median(r['emin'] for r in R)} | "
          f"{S.mean(sum(r['Xs'])/r['f'] for r in R):.3f} | {all(r['verified'] for r in R)}")
