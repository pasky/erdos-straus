# Compare joint failure J(V) with the product of marginal failure rates, class n ≡ 1 (mod 8).
import sys, math
fn = sys.argv[1]; nsq = int(sys.argv[2]) if len(sys.argv) > 2 else 0
rows = []; cnt = None; cls = None
for line in open(fn):
    if line.startswith('# class'):
        cls = int(line.split('≡')[1].split()[0]); cnt = int(line.split('count=')[1].split(',')[0])
        continue
    if line.startswith('#') or cls != 1: continue
    v, inC, mf, J = line.split(); rows.append((int(v), int(inC), float(mf), float(J)))
sq = nsq / cnt
logprod = 0.0
print("v  fail_v  cost_v=-ln(fail)  J(V)  Jns(V)=J-sq  -ln Jns  sum cost  ratio ln(Jns/prod)")
for v, inC, mf, J in rows:
    if not inC: continue
    logprod += -math.log(mf)
    Jns = J - sq
    lj = -math.log(Jns) if Jns > 0 else float('inf')
    print(f"{v:4d} {mf:.4f} {-math.log(mf):.4f} {J:.3e} {Jns:.3e} {lj:7.3f} {logprod:7.3f} {(-lj + logprod) if Jns>0 else float('nan'):7.3f}")
