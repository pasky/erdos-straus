# R215 — recount SEVEN_SIBLING §3.3 with the reviewer's own menu (review_r215_menu.uncovered):
# residues s mod ell (1 <= s < ell) such that EVERY unit lift n ≡ 1 (mod core_mod), n ≡ s (mod ell) at level base*ell is covered.
import sys
from review_r215_menu import uncovered
M, base, core_mod = map(int, sys.argv[1:4])
for ell in map(int, sys.argv[4:]):
    U, unc = uncovered(M, base*ell, check=False); unc = set(unc)
    core = [r for r in U if r % core_mod == 1]
    full = [s for s in range(1, ell) if all(r not in unc for r in core if r % ell == s)]
    print(f"M={M} ell={ell}: fully covered residues {len(full)}/{ell-1} {full}", flush=True)
