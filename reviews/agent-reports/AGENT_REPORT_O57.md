# AGENT REPORT O57 — beyond the 1/4 ceiling? (branch side-agent/beyond-ceiling)

Deliverable: `POINTWISE_OMEGA15.md`, `scripts/omega15_pseudorandom.py`,
`data/omega15/pseudorandom.txt`. Outcome: **precise obstruction, no conditional improvement.**

## Main results
* **Lemma 1.1 (PROVED).** O14's deterministic planted law ν is exponentially pseudorandom: for
  every *reduced product* h (bounded, local factors of mean ≤1/4 at big primes: residue classes,
  Dirichlet characters, additive characters of any modulus) `|E_νh−E_Ph|≤(4r*)^{k+1}`, and 0 if h
  touches ≤k big primes. Exact checks: closed form vs brute force (40), bound (900 cases).
* **Thm 1.2 (Wiener-norm barrier; PROVED mod O14 Thm 4.5 inputs).** Every minorant B≤F (any
  level) on any fibre: `E_HB≤e^{−c𝓛^4/log𝓛}·‖B‖_×`. Contains O14 Thm 4.5.
* **Thm 2.2 + Lemma 2.3 + Cor 2.4 + Prop 2.5.** Linear certificates (Def 2.1: only positivity,
  mass and accuracy bounds; no atomicity/integrality/support) with full-orbit uniform accuracy
  (classes, characters, additive characters; one-sided and Hölder-averaged accounting too) need
  `log x≥c𝓛^4/log𝓛`. Positivity must come from moduli `>x`, where every true orbit-uniform bound
  is trivial (Lemma 2.3, now proved relative to H via the coset K), so prime input (GRH etc.) is
  irrelevant *within this class by construction*; the content is Thm 1.2. `‖ν−P‖_TV≤e^{−0.6μ*}`.
* **Thm 3.1 (Siegel; atom norm).** The Siegel-model law `(1−εχ_1)P` has the fake `(1−εχ_1)ν`; for low
  level, `E_{P_1}B≤0` exactly — closes O14 Cor 4.6's "Siegel positivity" item for linear
  transfers.
* **Prop 4.1 (integers).** Haar bound for integer Type I sums `Σ_{n≤x,d|n}F(n)` (Haar on Ẑ, an
  exceptional set of measure `e^{−c𝓛^6}`); the certificate consequence holds only for accounting
  that charges error 1 to every deep class — not the natural accounting for integers, whose
  support is known. Integer Type I sums and Type II input are therefore **open** (N2).
* **Prop 5.2.** Finite-range prime-only minorants of a single modulus `≤x^{1/5}/(QT)` have
  `E B≤0` (Linnik–Xylouris; uses the single-prime event `n≡−4 (ℓ_0)`).
* Reading (Assessment 4.3, heuristic): the 1/4 ceiling is a sieve-*dimension* barrier (κ≍𝓛³/log𝓛,
  needed level superpolynomial `x^{𝓛^{1−o(1)}}`), a property of F; Type II / parity / Siegel
  input address the prime half. Maynard's restricted digits: complexity `≤X` (period = range)
  vs ES `x^{𝓛/polylog}`.

## Not covered (precise residual, §6)
(N1) non-periodic structure (integer analogue: squares avoid everything, Remark 4.2);
(N2) **atomicity / integrality / support of the prime or integer measure**, in particular
support-aware / finite-range accounting (e.g. classes mod q>x with least rep >x are empty) — the
main gap, including the integer Type I sums; Prop 5.2 handles single moderate moduli only;
(N3) non-linear certificates (pair statistics, density increment); (N4) non-class-ℓ¹ evaluation
of integer Type I sums.

## Self-review
`review` (deep) over `main..`: no FATAL; MAJOR items (Siegel norm closure; "oblivious" overclaim;
Type I/II overreach; integer error-accounting rule) repaired by rescoping to "full-orbit uniform",
atom norm in Thm 3.1, Cor 4.3 → Assessment, and Prop 5.2 + (N2). Minors applied.

## Parent review R57 (`reviews/pointwise-omega15-review.md`)
No FATAL. Repaired: M1 (§0/Cor 2.4/§6/Answer: "full-orbit uniform, Def 2.1" everywhere; "GRH
included" replaced by the statement that prime input is irrelevant within the class by
construction), M2 (Lemma 2.3 proved relative to H via `K={u≡r (gcd(q,Q))}`; Cor 2.4 / Prop 2.5 no
longer use the false Q-reduction), M3 (integer Type I sums moved to "covered only under full-orbit
accounting"; Type II "moot" removed; Answer (1b) labelled Assessment). Minors m1–m8 and
suggestions s1 (one-sided accounting remark), s2 (Siegel mass exact for s≤k) applied; the
self-review is renamed R57-self.

## Suggested ledger entry (H)28 (for the parent)
"Wiener-norm barrier (POINTWISE_OMEGA15): every minorant of F (any level) has
`E B≤e^{−c𝓛^4/log𝓛}‖B‖_×` (ℓ¹ over residue classes / characters / additive characters), via
pseudorandomness of O14's planted law (Lemma 1.1). Consequence: linear certificates with
full-orbit uniform accuracy (standard sieve-remainder accounting; one-sided and Hölder-averaged
too) cannot beat exponent 1/4 — within this class prime input (GRH etc.) is irrelevant by
construction, since on moduli >x every true orbit-uniform bound is trivial; the same holds for the
Siegel-model law `(1−εχ_1)P` (closes O14 Cor 4.6's Siegel item for such transfers). PROVED mod
(G), effective Page, fundamental lemma (O14 Thm 4.5 inputs); Prop 5.2 mod Linnik–Xylouris.
Open: certificates using atomicity/integrality/support of the prime or integer measure
(support-aware accounting; this includes integer Type I sums, so the role of Type II input is
open — heuristic Assessment only), non-periodic structure, non-linear methods. Reviews: R57-self,
R57 (SOUND after M1–M3 repairs)."

Replay: `PYTHONPATH=scripts uv run python scripts/omega15_pseudorandom.py 1` (~1 min).
