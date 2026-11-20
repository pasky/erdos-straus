"""Run the author's z78_proth_primary.solve beyond h=199 (bigger PARI stack), output to a given json; check separately
with z78_r2opus_replay.py checkfile. Usage: python scripts/z78_r2opus_beyond_pari.py LO HI OUT.json"""
import importlib.util, json, sys, signal
spec = importlib.util.spec_from_file_location('prim', 'scripts/z78_proth_primary.py')
prim = importlib.util.module_from_spec(spec); spec.loader.exec_module(prim)
prim.pa.allocatemem(400 * 10 ** 6)
lo, hi, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
rows = []
class TO(Exception): pass
def alarm(*a): raise TO()
signal.signal(signal.SIGALRM, alarm)
for h in range(lo, hi + 1, 2):
    signal.alarm(120)
    try:
        d = prim.solve(h)
    except TO:
        d = dict(h=h, timeout=True)
    signal.alarm(0)
    rows.append(d); print(h, d.get('c', d), d.get('T0'), flush=True)
    json.dump(rows, open(out, 'w'))
