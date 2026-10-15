"""R232: validate review_r232_box.py route bounds against exact enumeration (per box and per row), for single N = F.
Usage: review_r232_box_validate.py N [l2]   (N odd, ideally prime so that the in-cell unit-class hypotheses hold)."""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import review_r232_box as B
from review_r232_level1 import P_data, Q_data

def dy(x): return 1 << (x.bit_length() - 1)
N = int(sys.argv[1]); B.L2 = len(sys.argv) > 2
for mode in ('Q', 'P'):
    cnt, rows = {}, {}
    data = Q_data(N) if mode == 'Q' else P_data(N)
    for (a, b, c, d) in data:
        if mode == 'Q':
            if (a + b) % c or ((a + b) // c) % N == 0: continue
            key = (dy(c), dy(d), dy(4 * a * c * d - N))
        else:
            if c % N == 0 or d % N == 0: continue
            key = (dy(a), dy(d), dy(c))
        cnt[key] = cnt.get(key, 0) + 1; rows[key[:2]] = rows.get(key[:2], 0) + 1
    dump = {}
    tot, _ = B.cell_bound(mode, N, N, dump)
    bad = [(k, n, dump.get(k)) for k, n in cnt.items() if dump.get(k) is None or dump[k] < n]
    badr = [(k, n, dump.get(('row',) + k)) for k, n in rows.items() if dump.get(('row',) + k) is None or dump[('row',) + k] < n]
    tight = sum(1 for k, n in cnt.items() if dump.get(k) == n)
    print(f"{mode} N={N}: data {sum(cnt.values())}, boxes hit {len(cnt)}, bound total {float(tot):.4e}, "
          f"box violations {len(bad)}, row violations {len(badr)}, tight boxes {tight}", bad[:3], badr[:3])
