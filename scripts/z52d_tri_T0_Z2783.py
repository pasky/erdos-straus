# z52d triage T0, Z2783: out-of-sample test of the phase(MGO q-rational at e^{i pi/4}) -> Legendre sign majority rule.
import sys, cmath, math
from collections import Counter, defaultdict
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
from z52d_tri_T0_mgo_core import mgo, regcf, mgo_zeta8_exact
P = int(sys.argv[1]); q = cmath.exp(1j*math.pi/4)
rows = []; poles = 0
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    for (t, u, v) in L.words(p):
        A = t*u - 1
        try: val = mgo_zeta8_exact(regcf(p, A))
        except ZeroDivisionError: poles += 1; continue
        rows.append((p, round(cmath.phase(val)/math.pi, 6), L.legendre(A, p)))
half = P//2
tr = [r for r in rows if r[0] <= half]; te = [r for r in rows if r[0] > half]
cls = defaultdict(Counter)
for _, ph, s in tr: cls[ph][s] += 1
base = Counter(s for _, _, s in tr).most_common(1)[0][0]
seen = [r for r in te if r[1] in cls]
acc_in = sum(max(c.values()) for c in cls.values())/len(tr)
acc_seen = sum(1 for _, ph, s in seen if cls[ph].most_common(1)[0][0] == s)/max(1, len(seen))
acc_all = sum(1 for _, ph, s in te if (cls[ph].most_common(1)[0][0] if ph in cls else base) == s)/len(te)
basel = sum(1 for r in te if r[2] == base)/len(te)
print(dict(exact_poles=poles, words=len(rows), train=len(tr), test=len(te), distinct_phases_train=len(cls), in_sample_acc=round(acc_in, 4),
           test_seen_phase=len(seen), acc_on_seen=round(acc_seen, 4), test_acc=round(acc_all, 4), test_baseline=round(basel, 4)))
