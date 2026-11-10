# z70 CLASS item 2a, registered statistics WITHOUT the cap at 6 (review fix: the cap was an unregistered deviation).
import sys, math
sys.path.insert(0, 'scripts')
import cypari2
from z70_class_mine2 import prime_set, h_of, v2
res = {}
for name in ('H_train', 'H_test', 'CTRL'):
    res[name] = [(v2(h_of(-4*p)), v2(h_of(-8*p))) for p in prime_set(name)]
for i, nm in enumerate(('v2h(-4p) uncapped', 'v2h(-8p) uncapped')):
    def ms(rows):
        v = [r[i] for r in rows]; m = sum(v)/len(v); return m, sum((x-m)**2 for x in v)/(len(v)-1), len(v)
    mc, sc, nc = ms(res['CTRL']); out = [f"{nm}: CTRL mean {mc:.4f}"]
    for name in ('H_train', 'H_test'):
        m, s2, n = ms(res[name]); out.append(f"{name} mean {m:.4f} z {(m-mc)/math.sqrt(s2/n + sc/nc):+.2f}")
    print(' | '.join(out))
