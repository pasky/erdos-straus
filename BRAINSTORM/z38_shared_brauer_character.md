# z38_shared_brauer_character — (★) and the b = 1 line are two shifts of one pair lattice with one Brauer character (O268)

**Idea.** O260 spark 5: genus split of the b = 1 line and of the union (★) ∪ b = 1 (never fails ≤ 10⁸, López/B1_LINE).

**Result (PROVED, BM_CORRECTED_COUNT Prop 4.1).** With (S, T) = (4x, y) (B1_LINE Lemma 1.1), b = 1 is 4xy | p + 4x + y and (★)
is 4xy | p + x + y: the same moduli, shifts −(4x + y) and −(x + y), and BL's class is χ_{−4xy}(p) for both
((4x + y) | (4x)² + 4xy, resp. (x + y) | (x − y)² + 4xy). On the full Type II family the Brauer character is χ_{−4ab},
independent of (c, d). The bare M_BM of the b = 1 line diverges (y = 1 pairs); with the mod-4 character added (M4) it is finite.

**Literature.** López 2022/2024 (b = 1 = Type A/B lines), BL Thm 1.2, B1_LINE Lemma 1.2.

**Barrier screen.** No forcing: the residuals of the two lines are positively correlated (0.21–0.30), so no
complementarity theorem can come from the BM layer (both lines see the same Legendre sum Σ(−xy/p)/φ(4xy)). T1: both M4 vanish
at squares. B3: the union only doubles the main term.

**Cheap numerics.** `scripts/z38_b1.c`, `z38_b1_stats.py` (p ≡ 1 (24) in [10⁵, 4·10⁵]: var/2M = 1.53 (★), 0.85 (b = 1), 1.42
(union); min union ratio 0.167). Reproduces the b = 1 exceptions 193, 2521, 66529 and (★)'s 409, 577, ….

**Assessment.** PROVED (identity) + EVIDENCE (negative: no anti-correlation). The union's robustness is a main-term effect.
