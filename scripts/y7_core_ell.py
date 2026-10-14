# y7 (O215): how much of 7's class-of-one core (n ≡ 1 mod 105, level 840) is covered at level 840*ell, per prime ell.
# Reports, for each ell, the fraction of core lifts (mod 840*ell, n ≢ 0 mod ell) that are covered, and the residues
# mod ell that are covered for EVERY lift mod 840 (i.e. whole classes mod ell inside the core).
import sys
from math import gcd
from y7_mordell_cover import cover
M=int(sys.argv[1]); base=int(sys.argv[2]); core_mod=int(sys.argv[3])
for ell in map(int,sys.argv[4:]):
    L=base*ell
    U,unc=cover(M,L)
    unc=set(unc)
    core=[r for r in U if r%core_mod==1]
    covered=[r for r in core if r not in unc]
    full=[s for s in range(1,ell) if all((r not in unc) for r in core if r%ell==s)]
    print(f"M={M} ell={ell}: core lifts {len(core)}, covered {len(covered)} ({len(covered)/len(core):.3f}); residues mod ell fully covered: {len(full)}/{ell-1} {full}",flush=True)
