# AGENT REPORT O93 — explicit tail for the r = 17 P-family

Branch `side-agent/r17-explicit-tail`. Deliverable: `POINTWISE_MORDELL17B.md`, `scripts/m17b_{penum,brute,union,tail}.py`.

**Outcome: CONDITIONAL. There is no unconditional sterile point.** The hypothesis needed is now explicit and weak.

1. **New enumerator (§2).** It is complete by an exact form of ET's four-regime cover (Lemma 2.1), with factorisations by
   coreutils `factor`. It agrees with the naive scan *as sets* at K = 5, 7, and with M17's counts at K ≤ 9. It is about 50× faster
   (K = 9: 9 s). **New: D_P(11) = 836, D_P(13) = 1463** (sequence 2, 32, 121, 258, 604, 836, 1463).
2. **Exact union through P-level 6 (§3).** It reproduces M17 exactly (56561/83521; Q/U level 7). Level 6 adds 100 new P-boxes
   (7.0·10⁻⁵ of the cell). Uncovered: **ρ₁ = 16344335/24137569 = 0.6771326**. Adding level 7 (P K = 13: 178 new) gives ρ₂ = 961421/1419857 = 0.6771252.
3. **Theorem 4.1 (PROVED reduction).** A sterile point exists in C_5, C_7 (hence M17 Cor. 4.2 applies) if
   `D_P(K) ≤ C·17^{θK}` for all odd K ≥ 13 and `D_Q(k) ≤ 17^{3k/5}` for all odd k ≥ 9, with
   (θ, C_max rounded down) = (0.25, 619.2), (0.3, 87.88), (0.35, 11.76), **(0.4, 1.409)**, (0.45, 0.1275) (R93 repair M1/m2:
   previously rounded up; C = 1.41 is NOT admissible, exact threshold 1.409796…).
   So ET's own exponent 2/5, with constant 1.40 and no o(1), suffices (R93 repair M1). Data: `D_P/17^{0.4K}` ≤ 1.07 for all K ≤ 11, and 0.0032 at K = 11.
   Conjecture 4.2 (`D_P ≤ 2K³`, `D_Q ≤ 3k³`; consistent with all data) gives tail < 4.1·10⁻⁴.
4. **Averaging over K (§5)** is only a reorganisation (Lemma 5.1). The first admissible K in each discrete-log class is
   unconstrained unconditionally, and small-order moduli are finitely many and live at low levels. Precise obstruction:
   an explicit average divisors-in-class bound over the ≍ n^{2/5} ET pairs. Pointwise Nicolas–Robin would need K ≳ 4·10⁷.
5. **What more computation adds.** K = 13 is done (1.5 h, 2 cores). It moves the hypothesis to K ≥ 15 and raises C_max at
   θ = 0.4 from 1.409 to 2.484 (R93 repair M1/m2: rounded down). K = 15 would take roughly 15× longer and gain a similar factor. No finite computation closes the tail,
   because the hypothesis is needed for every K.

Not reviewed. Points for the reviewer: the completeness of Lemma 2.1 (`acde ≤ n` for all N-points with a ≤ b), and the
use of M17 Lemmas 1.3/5.1/5.2 in Lemma 1.1 (U ⊂ P, Q⁻¹ = Q, odd levels only).
