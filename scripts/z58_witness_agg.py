"""z58 WITNESS aggregator: stream z58_witness_scan output (all primes p ≡ 1 (4) in a range) and summarise
least-witness statistics by half-decade, with the Mordell split (inM = p mod 840 ∈ 𝔐).
Usage: cat s_*.txt | python3 scripts/z58_witness_agg.py OUTPREFIX
Writes OUTPREFIX_summary.txt, OUTPREFIX_records.txt (running records of d_min, u_min, C_min, q_min, m3 = min(d_min, q_min)),
OUTPREFIX_hard.txt (p with u_min >= 7 or C_min >= 40 or d_min > 30*sqrt(p) or R=0)."""
import sys, math
from collections import defaultdict, Counter

out = sys.argv[1]
B = lambda p: math.floor(2 * math.log10(p)) / 2  # half-decade bucket
stats = defaultdict(lambda: dict(n=0, z=0, maxd=(0, 0), maxu=(0, 0), maxC=(0, 0), maxq=(0, 0), maxm3=(0, 0),
                                 uh=Counter(), Ch=Counter(), sld=0.0, slq=0.0, maxdnp=(0, 0), dnp1=0, np=Counter(),
                                 dlog=Counter()))
rec = {k: 0 for k in ('d', 'u', 'C', 'q', 'm3')}
recs = []
hard = []
for line in sys.stdin:
    if line[0] == '#':
        continue
    f = line.split()
    p = int(f[0]); M = int(f[2])
    dmin, ud, Cd, Bd, umin, du, Cmin, dC, qmin, uq, Bq, npp = map(int, f[3:15])
    s = stats[(B(p), M)]
    s['n'] += 1
    s['np'][npp] += 1
    if dmin < 0:
        s['z'] += 1; hard.append(('ZERO', p, M, line.strip())); continue
    m3 = min(dmin, qmin) if qmin > 0 else dmin
    for k, v in (('maxd', dmin), ('maxu', umin), ('maxC', Cmin), ('maxq', qmin), ('maxm3', m3)):
        if v > s[k][0]:
            s[k] = (v, p)
    s['uh'][umin] += 1; s['Ch'][min(Cmin, 99)] += 1
    s['sld'] += math.log(dmin); s['slq'] += math.log(qmin) if qmin > 0 else 0
    s['dlog'][int(math.log10(dmin))] += 1
    r = dmin / npp
    if r > s['maxdnp'][0]:
        s['maxdnp'] = (r, p)
    # does d_min equal n_p (the least non-residue prime itself fires)?
    if dmin == npp:
        s['dnp1'] += 1
    for k, v in (('d', dmin), ('u', umin), ('C', Cmin), ('q', qmin), ('m3', m3)):
        if v > rec[k]:
            rec[k] = v; recs.append((k, p, M, v, line.strip()))
    if umin >= 7 or Cmin >= 40 or dmin > 30 * math.sqrt(p):
        hard.append(('HARD', p, M, line.strip()))

with open(out + '_summary.txt', 'w') as fo:
    fo.write('# bucket=floor(2log10 p)/2, M=inM. n primes p≡1(4); z=#R=0; max (value,argmax) for d_min,u_min,C_min,q_min,m3=min(d_min,q_min);\n')
    fo.write('# mean log d_min, mean log q_min; max d_min/n_p; #(d_min==n_p); u_min histogram; C_min histogram (99=≥99); log10 d_min histogram; n_p histogram\n')
    for key in sorted(stats):
        s = stats[key]; h = s['n'] - s['z']
        fo.write(f"{key[0]:4.1f} M={key[1]} n={s['n']} z={s['z']} maxd={s['maxd']} maxu={s['maxu']} maxC={s['maxC']} maxq={s['maxq']} "
                 f"maxm3={s['maxm3']} meanlogd={s['sld']/max(h,1):.3f} meanlogq={s['slq']/max(h,1):.3f} maxd/np={s['maxdnp'][0]:.1f}@{s['maxdnp'][1]} "
                 f"d==np:{s['dnp1']}\n   uh={sorted(s['uh'].items())}\n   Ch={sorted(s['Ch'].items())}\n   dlog={sorted(s['dlog'].items())}\n"
                 f"   np={sorted(s['np'].items())}\n")
with open(out + '_records.txt', 'w') as fo:
    fo.write('# running records over primes p≡1(4) in increasing order: kind p inM value | full scan line\n')
    for r in recs:
        fo.write(f"{r[0]} {r[1]} {r[2]} {r[3]} | {r[4]}\n")
with open(out + '_hard.txt', 'w') as fo:
    fo.write('# p with R=0, or u_min>=7, or C_min>=40, or d_min>30 sqrt(p): tag p inM | full scan line\n')
    for r in hard:
        fo.write(f"{r[0]} {r[1]} {r[2]} | {r[3]}\n")
