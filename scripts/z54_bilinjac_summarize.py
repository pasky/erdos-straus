"""Summarise strip_*.txt (z54_bilinjac_multi.py output) per file, type and P-choice.
Each n is run twice by z54_bilinjac_multi.py, first with P = max(3, round(sqrt V)) ('Psmall'), then P = max(3, V//4)
('Pbig'); the choice is identified by line order (when both coincide, as for tiny V, the two rows are identical)."""
import sys, re, statistics as st
for fn in sys.argv[1:]:
    rows, seen = {}, {}
    for line in open(fn):
        tag = line.split()[0]
        d = dict(re.findall(r"(\w+)=([-\d.e+]+)", line))
        k = (tag, d["n"]); seen[k] = seen.get(k, 0) + 1
        key = (tag, "Psmall" if seen[k] == 1 else "Pbig")
        rows.setdefault(key, []).append(d)
    print(f"== {fn}")
    print("type         P      #n  V-range     W-range        |A|range     sq  cnterr_rms SQrms_mean SQmax_max boxmax_max Erms_mean Tmax_max Trms_mean g1range       addbd_mean Sq0_rms")
    for key, R in sorted(rows.items()):
        f = lambda k: [float(r[k]) for r in R]
        rg = lambda k, fmt="{:.0f}": (fmt + "-" + fmt).format(min(f(k)), max(f(k)))
        print(f"{key[0]:12s} {key[1]:6s} {len(R):3d} {rg('V'):11s} {rg('W'):14s} {rg('A'):12s} {int(sum(f('sq'))):3d} "
              f"{(st.mean([x*x for x in f('cnterr')]))**.5:9.2f} {st.mean(f('SQrms')):9.2f} {max(f('SQmax')):9.2f} {max(f('boxmax')):9.2f} "
              f"{st.mean(f('Erms')):8.2f} {max(f('Tmax')):8.2f} {st.mean(f('Trms')):8.2f} {rg('g1','{:.2f}'):12s} {st.mean(f('addbd')):8.2f} "
              f"{(st.mean([x*x for x in f('Sq0')]))**.5:7.2f}")
