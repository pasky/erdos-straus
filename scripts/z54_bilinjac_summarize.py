"""Summarise strip_*.txt (z54_bilinjac_multi.py output) per file, type and P-choice."""
import sys, re, statistics as st
for fn in sys.argv[1:]:
    rows = {}
    for line in open(fn):
        tag = line.split()[0]
        d = dict(re.findall(r"(\w+)=([-\d.e+]+)", line))
        key = (tag, "Psmall" if int(d["P"]) < int(d["V"]) ** 0.75 else "Pbig")
        rows.setdefault(key, []).append(d)
    print(f"== {fn}")
    print("type         P      #n  V     W        |A|mean  sq  cnterr_rms SQrms_mean SQmax_max boxmax_max Erms_mean Tmax_max Trms_mean g1   addbd_mean Sq0_rms")
    for key, R in sorted(rows.items()):
        f = lambda k: [float(r[k]) for r in R]
        print(f"{key[0]:12s} {key[1]:6s} {len(R):3d} {R[0]['V']:5s} {R[0]['W']:8s} {st.mean(f('A')):8.1f} {int(sum(f('sq'))):3d} "
              f"{(st.mean([x*x for x in f('cnterr')]))**.5:9.2f} {st.mean(f('SQrms')):9.2f} {max(f('SQmax')):9.2f} {max(f('boxmax')):9.2f} "
              f"{st.mean(f('Erms')):8.2f} {max(f('Tmax')):8.2f} {st.mean(f('Trms')):8.2f} {st.mean(f('g1')):6.2f} {st.mean(f('addbd')):8.2f} "
              f"{(st.mean([x*x for x in f('Sq0')]))**.5:7.2f}")
