# z70 LOOSE item 4: analysis of pell_*.jsonl (real letters vs exact local null vs exact decoys).
import sys, json, math, gzip
def load(fn):
    op = gzip.open if fn.endswith('.gz') else open
    return [json.loads(l) for l in op(fn, 'rt')]
def zc(ds):
    num = sum(ds); den = math.sqrt(sum(d * d for d in ds))
    return num / den if den else 0.0
def analyse(name, recs, roles=None):
    O = E = V = 0.0; n = 0; nd = 0; clus_null = []; clus_dnull = []; clus_con = []; drop = 0; none = 0
    Od = Ed = 0.0
    for r in recs:
        a = b = c = 0.0
        for row in r['rows']:
            if roles and not (set(row['roles']) & set(roles)): continue
            if row['P0'] is None: none += 1; continue
            n += 1; O += row['D']; E += row['P0']; V += row['P0'] * (1 - row['P0']); a += row['D'] - row['P0']
            if row.get('dec'):
                dd = [x for x in row['dec'] if x[2] is not None]
                if len(dd) == 2:
                    nd += 1
                    md = sum(x[1] for x in dd) / 2; mp = sum(x[2] for x in dd) / 2
                    Od += md; Ed += mp
                    b += md - mp
                    c += (row['D'] - row['P0']) - (md - mp)
            else: drop += 1
        clus_null.append(a); clus_dnull.append(b); clus_con.append(c)
    print(f"{name}{' roles='+roles if roles else ''}: letters={n} (P0 undefined {none}; no decoy {drop}) | real D rate {O/max(n,1):.4f} vs exact null {E/max(n,1):.4f} "
          f"(O-E={O-E:+.1f}, binomial z={(O-E)/math.sqrt(V) if V else 0:+.2f}, cluster z={zc(clus_null):+.2f}) | decoys ({nd} letters): "
          f"D {Od/max(nd,1):.4f} vs null {Ed/max(nd,1):.4f} (cluster z={zc(clus_dnull):+.2f}) | real-vs-decoy (null-adjusted) cluster z={zc(clus_con):+.2f}")
if __name__ == '__main__':
    for fn in sys.argv[1:]:
        recs = load(fn); nm = fn.split('/')[-1]
        analyse(nm, recs)
        for ro in ('x', 'y', 'z'): analyse(nm, recs, ro)

def by_v2(fn):
    recs = load(fn); nm = fn.split('/')[-1]
    for lo, hi in ((0, 0), (1, 1), (2, 2), (3, 99)):
        O = E = V = 0.0; n = 0; cl = []; Od = Ed = 0.0; cld = []
        for r in recs:
            a = 0.0; b = 0.0
            for row in r['rows']:
                l = row['l']; v = (l & -l).bit_length() - 1
                if not (lo <= v <= hi) or row['P0'] is None: continue
                n += 1; O += row['D']; E += row['P0']; V += row['P0'] * (1 - row['P0']); a += row['D'] - row['P0']
                dd = [x for x in row.get('dec') or [] if x[2] is not None]
                for x in dd: b += (x[1] - x[2]) / len(dd)
            cl.append(a); cld.append(b)
        print(f"  {nm} v2(l) in [{lo},{hi}]: letters={n} real {O/max(n,1):.4f} vs null {E/max(n,1):.4f} cluster z={zc(cl):+.2f}; decoys-vs-null cluster z={zc(cld):+.2f}")
if __name__ == '__main__' and len(sys.argv) > 1:
    for fn in sys.argv[1:]: by_v2(fn)
