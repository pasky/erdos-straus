"""Print the markdown class-factor tables of RESIDUE_HARDNESS §1.3 from data/z52c/rh/model_tables.json (window '1e6')."""
import json, sys
MT = json.load(open('data/z52c/rh/model_tables.json')); w = sys.argv[1] if len(sys.argv) > 1 else '1e6'
def sq(Q, r):
    if Q in (8, 16): return ''
    if Q == 840: return ''
    return '■' if pow(r, (Q - 1)//2, Q) == 1 else ''
print('| Q | r | U model (data) | (★) model (data) | Type I model | Type II model |\n|---|---|---|---|---|---|')
for Q in [3, 5, 7, 8, 11, 13, 16]:
    d = MT[w][str(Q)]
    for i, r in enumerate(d['classes']):
        print(f"| {Q} | {r}{sq(Q, r)} | {d['U']['model'][i]:.3f} ({d['U']['data'][i]:.3f}) | {d['S']['model'][i]:.3f} ({d['S']['data'][i]:.3f}) |"
              f" {d['I']['model'][i]:.3f} | {d['II']['model'][i]:.3f} |")
d = MT[w]['840']; cl = d['classes']
sq840 = [r for r in cl if r % 8 == 1 and all(pow(r % m, (m-1)//2, m) == 1 for m in (3, 5, 7))]
for r in sq840:
    i = cl.index(r)
    print(f"| 840 | {r} (Mordell sq.) | {d['U']['model'][i]:.3f} ({d['U']['data'][i]:.3f}) | {d['S']['model'][i]:.3f} ({d['S']['data'][i]:.3f}) | {d['I']['model'][i]:.3f} | {d['II']['model'][i]:.3f} |")
u = d['U']['model']; i0, i1 = u.index(min(u)), u.index(max(u))
print(f"\nmod 840 (96 classes p ≡ 1 (4)): U-model range {min(u):.3f} (r = {cl[i0]}) … {max(u):.3f} (r = {cl[i1]}); "
      f"mean over the 6 Mordell squares {sum(u[cl.index(r)] for r in sq840)/6:.3f}.")
