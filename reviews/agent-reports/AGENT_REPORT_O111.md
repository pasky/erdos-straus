# AGENT REPORT O111 — the Type I log log N via Heegner points (branch side-agent/heegner-typei)

Deliverable: `EXCEPTIONAL_TYPEI_LOGLOG.md` (§0 summary), scripts `scripts/ttl_separation.py`,
`scripts/ttl_perd.py` (+ `.out.txt`). DI 1982 scan added: `sources/o111/deshouillers-iwaniec-1982.pdf`.

## Result
* **Theorem 8.1 (CONDITIONAL on Selberg's eigenvalue conjecture for Γ₀(M) with even nebentypus mod 2q):**
  `Σ_{p≤N} f_I(p) ≪ N log² N`, i.e. ET's open (OPEN-I). It is **not** unconditional. Parts of the proof are
  careful outlines: Prop 5.1 (the Bessel/Mellin bookkeeping in the large-sieve step), Prop 7.1 (the
  Ramanujan-sum terms) and the cell bookkeeping of Thm 8.1.
* **Unconditional status:** the argument covers every cell except a strip `0 < 2α−1+γ ≲ 0.1`, where
  exceptional eigenvalues (Kim–Sarnak 7/64) beat the saving. The strip still costs `log log N`, so there is
  no unconditional improvement of ET. DI Thm 5, DI Thm 6 (level average) and Humphries' density theorem
  were checked; none closes the strip (§3.2, §9).

## Key new ingredients (PROVED unless stated)
1. Lemma 2.2: level-d Heegner forms `[f,4ad,de]` have **uniformly separated** roots: `cosh dist ≥ 3/2` for
   all d, since `disc(Q−Q') = 8d(cosh−1)` and `4d | disc(Q−Q')`. Numerically the minimum is `cosh ≥ 3`.
2. Prop 4.3: Sobolev duality. For a separated Γ'-invariant set,
   `|Σ_z P(z) − #Λ⟨P⟩| ≪ (#Λ)^{1/2}‖(1−Δ)P₀‖₂`, uniformly in Γ'. The proof uses the kernel of `(1−Δ)^{−2}`
   and a packing argument.
3. Prop 5.1 (conditional on SEL; uses the DI Thm 2 / Drappeau 2017 Prop 1 large sieve): the box Poincaré
   series has variance `≪ polylog·(area + 1/(Y·level))`.
4. Thm 6.2: the per-d count with the sieve congruence has relative error `≈ q²(d/a)^{1/2}`. The main term
   factorises (Lemma 6.1, via strong approximation and Witt), and parity is handled by `Γ₀(d)∩Γ(2q)`.
5. Complementarity: MN3's per-a Weil count (K_a, Prop 7.1) has relative error `≈ q² a/d`. The two
   methods meet exactly at `d = a`. Lemma 1.1 shows that a linearly degenerating saving costs only
   `O(N log² N)`, since `Σ_{j,k≤L} min(1/j,1/k) ≤ 2L`. So no third method is needed. MN3's
   W_e/W_f/BT are unnecessary for c ≤ N^η.
6. MN3's (H**), Heegner equidistribution on X₀(d), cannot hold: there are `≈ √d` points against a volume
   of `d`. It is also not needed, because only the second moment of the lift count enters.

## Literature (search-limited, two research subagents + own checks)
No removal of ET's log log was found. Jia 2012 (Sci. China Math.) is cited by ET v6, which still says the
log log is open; Jia's text was not accessed. No joint level–discriminant result with level ≍ |D| exists
(LMY 2013: `q ≤ |D|^{1/20}`). No result on `Σ_a S(h,k;a²)` or on τ in APs to square moduli was found.
The DI Thm 5 statement was read from the scan; Drappeau's nebentypus large sieve is cited from the subagent
(not re-read by me).

## Points the reviewer should attack
* Prop 5.1: whether the large sieve really controls `Σ_j (1+|t_j|)^4 |⟨P,u_j⟩|²` with only polylog loss
  (the `t`-dependent `|n|^{−it}`; small `t`; the Eisenstein and `n = 0` parts; the index normalisation over
  characters).
* Lemma 6.3's `r(d)` bound (the 2-adic case is hand-waved), and that only polylog losses occur near
  `α = (1−γ)/2` (Thm 8.1 step (4) puts `O(log L)` layers on BT).
* Prop 7.1's error terms when `E` or `F` exceeds `m = 4a²`, or is tiny.
* Thm 8.1 step (3): the weighted masses with `s/φ(s)` (via MN3 Prop 2.3 with `4k`, `4k²`).
