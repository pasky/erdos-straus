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
   Conjecture 4.2 (R93 repair m7: CONJECTURE, robust form `D_P(K) ≤ K⁵` for K ≥ 15, `D_Q(k) ≤ k⁵` for k ≥ 9) gives tail ≤ 4.2·10⁻³;
   the tighter 2K³/3k³ fit is kept as an observation.
4. **Averaging over K (§5; R93 repairs m4–m6).** Lemma 5.1 now assumes `17 ∤ ab` (other pairs miss the cells) and
   takes the pair form: all boxes of `(a,b)` are concentric at `−a/b`, so `T_P ≤ 2Σ_{(a,b)} 17^{(1−K_min)/2}`. This is an upper
   bound, not a reorganisation of the same sum. Assessment: there is no visible unconditional gain from averaging over K.
   Small-order pairs sit at level `≲ L`. Revised obstruction: Lenstra/CHN handle most `ad`/`ac` pairs. The bottleneck is the
   `e`-regime (short-interval τ₃ sums), the `cd` regime, and explicit constants; at best these give `n^{2/5}(log n)^{O(1)}`.
   The pointwise Nicolas–Robin terms are not small before K ≳ 4·10⁷ (assuming M ≈ n^{1.8}).
5. **What more computation adds.** K = 13 is done (1.5 h, 2 cores). It moves the hypothesis to K ≥ 15 and raises C_max at
   θ = 0.4 from 1.409 to 2.484 (R93 repair M1/m2: rounded down). K = 15 would take roughly 15× longer and gain a similar factor. No finite computation closes the tail,
   because the hypothesis is needed for every K.

Reviewed by R93 (`reviews/pointwise-mordell17b-review.md`): no FATAL. M1 and m1–m8 are applied and marked
"(R93 repair)". D_P(11) and D_P(13) are now two-engine CERTIFIED, with set hashes equal (`data/m17b/`). Original points for the reviewer: the completeness of Lemma 2.1 (`acde ≤ n` for all N-points with a ≤ b), and the
use of M17 Lemmas 1.3/5.1/5.2 in Lemma 1.1 (U ⊂ P, Q⁻¹ = Q, odd levels only).
