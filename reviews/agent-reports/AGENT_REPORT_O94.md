# AGENT_REPORT_O94 — the 3/4 exceptional-set bound for m/n (Sierpiński/Schinzel)

Branch `side-agent/mn-threequarter`. Deliverable: `EXCEPTIONAL_MN.md`, plus `scripts/emn_hm.py`, `scripts/emn_identity.py`,
`scripts/emn_mass.py` (+ `scripts/emn_mass.out.txt`). ES is not solved. Nothing was merged into main.

## Results (all PROVED *relative to the note* `paper/es-threequarter-note.tex` + EXCEPTIONAL_SHORT; same internal-only status)

1. **Theorem A.** There are absolute c, C such that for every m ≥ 4, every interval I of length H ≥ 2:
   `E_m(I) ≤ C H exp(−c (log H)^{3/4} m^{−1/4})`. In particular `E_m(N) ≤ C N exp(−c (log N)^{3/4}/m^{1/4})`.
   * Goal (1): the note's argument goes through for **every** m ≥ 4. Nothing in the density proof is m-specific.
     The POINTWISE_MN Jacobi dichotomy (m ≡ 0 (4) or not) concerns the pointwise square-class process and never enters (§1.4).
   * Changes: identity `kℓ+1 = m·uvw` (Lemma 1.1); multipliers `k ≤ X^κ` with `(k,m) = 1` instead of `k ≡ 1 (4)`;
     modulus `q = muv`; `φ(muv) ≥ φ(m)φ(u)φ(v)` and `φ(muv) ≤ φ(m)uv`; `h_m(K) ≍ (φ(m)/m) log K` (Lemma 2.1).
   * Fibre mass `≍ t³/m` on reduced fibres, and `≪ t³/m` on every fibre (Cor. 3.2). The void lemma works with absolute η = 1/4 and
     `y = max(2, B t³/m)`. Bonferroni depth is `r ≍ t³/m`, the ledger is `e^{O(t⁴/m)}` and `t⁴ ≍ m log H`.
     The whole m-dependence is the substitution `t³ → t³/m`.
2. **Uniformity (goal 3).** `c_m = c·m^{−1/4}` exactly, with absolute c: no φ(m) or log m loss. The BV range `m ≤ t³` is automatic
   whenever the saving is ≥ 1. This beats Pomerance–Weingartner Thm 1.3 (`exp(−C (log N)^{2/3}/φ(m)^{1/3})`, m ≤ log² N)
   asymptotically: the exponent ratio is ≫ `(Lm)^{1/12}/(log log 3m)^{1/3}`, so Theorem A's bound wins once that exceeds an absolute
   ineffective Λ_0 (e.g. for fixed m and N large). The saving → ∞ iff `m = o((log N)³)` (R94A repair D1, D2; R94B repair D2).
3. **Theorem B / Cor. C (goal 2).** SHORT's progression and prime-short-interval statements carry over with saving
   `(log(H/q))^{3/4} m^{−1/4}` and the same q₁ (smooth-part) loss. Caveat: SHORT's "every prime q" remark does **not**
   transfer automatically (`log X_q`/saving ≍ `(m/log(H/q))^{1/2}`).
4. **Corollary D (new consequence).** Most primes in (N/2, N] are m-representable once `log N ≥ C m^{1/3}(log m)^{4/3}`.
   The proof of PW Thm 3.1 shows most primes there are m-exceptional for `m^{1/4} ≪ log N ≤ (φ(m)/(C log² m))^{1/3}`.
   So the **density** transition is at `log n = m^{1/3+o(1)}`. Monotonicity in between is unknown (R94A D3, R94B D3), with a gap factor `(log m)²(m/φ(m))^{1/3}`; PW's rigorous bounds had left it between m^{1/3} and m^{1/2}.
   This says nothing about the largest exception (PW's heuristic puts that near exp(m^{1/2})).
5. **Literature (goal 4).** I found no 3/4-type, short-interval or progression result for m/n. Searches were 2026-10-07, plus
   LITERATURE_2026 and the PW text; Dartmouth "ESS-ExceptionsV8" has the same Thm 1.3. The known results are Vaughan 1970
   (exponent 2/3; quoted for m = 4 only, general-m content unverified, R94B D4) and PW (explicit in m). Assessment: the results are new for m ≠ 4; the method is the note with 4 → m.

## Checks
* `emn_hm.py 100000` (Lemma 2.1): 0 failures. `emn_identity.py`: Lemma 1.1 on 4 821 random instances (exact rationals), and
  Lemma 1.3 distinctness on 19 446 atoms: 0 failures. Both scripts now exit non-zero on failure.
* `emn_mass2.py 1e6 170 7 60 2` (EVIDENCE, toy; deduplicated; m-independent floor; K ≥ m²; R94A D5):
  `m·μ_c ∈ [0.98, 1.13]` vs `φ(m)·μ_c ∈ [0.33, 1.04]` for m = 4..13, with 0 collisions.
  The older incidence toy `emn_mass.py` (`m·μ ∈ [3.85, 4.58]`) is superseded. The parity-pattern remark is an observation only (R94B D6).
* Self-review: a `review` subagent (deep) ran a hostile pass. It found the core transfer sound and listed 6 repairs, all applied (commit "repairs after self-review"):
  1. PW threshold has φ(m), not m;
  2. "sharp" was restricted to the density transition, not Schinzel's eventual threshold;
  3. the two-sided fibre mass holds only on reduced fibres;
  4. Theorem B prime-q caveat;
  5. Λ² vs (log z)² constant 1/32, and the N ≥ 16 detail in Cor. D;
  6. toy script counts incidences.

## For the parent
* Proposed ledger entry: "(D)31 EXCEPTIONAL_MN: m-uniform 3/4 bound `E_m(I) ≪ H exp(−c(log H)^{3/4}m^{−1/4})`, m ≥ 4,
  plus progressions/primes and the density-transition corollary — PROVED rel. note".
* What most needs an independent re-check: Prop. 3.1, the BV step uniform in m ≤ t³ with modulus muv and its multiplicity.
  Also Lemma 4.1, where the union bound with absolute η = 1/4 is measured against h_m ≥ 0.54 S_m.
* Open: close the `(log m)²(m/φ(m))^{1/3}` gap in Cor. D. SHORT's smooth-q progression gap is inherited.

## Repairs after independent reviews (R94A = exceptional-mn-review-A.md D1–D7, R94B = exceptional-mn-review-B.md D1–D6)
Neither review found a FATAL or MAJOR defect, and all repairs below are applied, each tagged "(R94A/R94B repair Dk)" in EXCEPTIONAL_MN.md. Commits are grouped:
1. **PW comparison and range** (A D1, D2; B D2). The comparison is now explicitly asymptotic, with an absolute ineffective Λ_0. The saving → ∞ iff m = o((log N)³).
2. **Cor. D** (A D3, D4; B D3). It now cites the range from PW's *proof*, `m^{1/4} ≪ log N ≤ (φ(m)/(C log² m))^{1/3}`, and notes that monotonicity in between is unknown. The heuristic match now reads "up to bounded and log log factors".
3. **Vaughan attribution** (B D4). Vaughan is quoted for m = 4 only, and his general-m content is unverified.
4. **Scope and bookkeeping** (A D6, D7; B D1, D5):
   * only the pruned ω-route is re-derived; the no-ω family and the §6 Cauchy–Schwarz route are sketched as transferring;
   * Lemma 1.3 now assumes m ≤ t³;
   * the Theorem A side conditions are made explicit via t³ = ms ≥ 4s;
   * the Thm 4.3 ledger is spelled out.
5. **Toy evidence** (A D5; B D6). There is a new deduplicated `emn_mass2.py` with an m-independent floor. The Euler-factor/parity explanation is demoted to an observation.

No PROVED statement changed.
