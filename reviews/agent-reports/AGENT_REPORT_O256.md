# AGENT_REPORT_O256 — balanced relation lattices: from Hypothesis W to GRH (checkpoint 1)

Branch side-agent/balanced-lattice (merged O252 and main incl. R264 repairs). Main file BALANCED_LATTICE.md; memos
BRAINSTORM/z27_*.md (6); scripts scripts/z27_dual.py, scripts/z27_eqcheck.py; data data/z27/ (tiny).
**ES is not solved; no infinite case of ES is claimed. Bounded / (log₂p)^{O(1)} cap is NOT ES — cap 0 is the B2 divisor event.**

## SHARP:
1. **Exact dual dictionary (PROVED, §1):** Λ_q(S)*/ℤ^S ≅ Û_q; cube covering radius ≍ 1/𝔻_min within k^{3/2} (Banaszczyk),
   𝔻_min = min_{ψ≠1} Σ_{s∈S} ‖arg ψ(s²)/2π‖. *q is balanced ⟺ no nontrivial character of U_q is ℓ¹-pretentious to 1 on the k
   forced primes at the Minkowski scale N^{−1/k}.*
2. **The balance-deciding character has large order, divisible by P⁺(q−1) (EVIDENCE, §6; R269 repair: = N in ≈ 75 %, "≍ N" only in this sense):** P⁺(q−1) | ord in > 99 % of q (k = 3, 4, 5; q ≤ 10⁷),
   identical to the uniform-discrete-log model; orders ≤ N^{3/(2k+4)} (nominal small-order range): ≤ 0.07 %. Combined with the
   **indistinguishability Prop 2.2 (PROVED, abstract-vector form)**: Frobenius data in ℚ(ζ_m, S^{1/m}), m ≤ M, is a function of the discrete logs mod
   the M-smooth part of q − 1, and is compatible, among abstract generating vectors with the same projections, with L_min ≥ (M-rough part) − 1. ⇒ The brief's
   Hooley/Kummer route, as an accounting of Frobenius classes in the class −p mod 8P, certifies essentially only the index
   condition (Assessment 2.3).
3. **GRH + a p-free, class-free sparsity hypothesis S ⇒ e*(p) ≤ (log₂p)^{9/2+o(1)} (Thm 4.2, CONDITIONAL);** GRH + EQ
   (no over-concentration of large-order pretentious primes in classes mod 8P) ⇒ (log₂p)^{13/2+o(1)} (Thm 4.1). S = #{q ≤ x :
   some character of order > x^{3/(2k)} has 𝔻_S < x^{−3/(2k)}} ≤ x^{1/2}(log x)^A (uniformly in y with P(y) ≤ √x) — the
   random-model prediction (rare-event heuristic up to constants); a rank-k
   "small multiplicative order" sparsity statement (Erdős–Murty/Kurlberg–Pomerance analogue). They are alternative sufficient
   hypotheses (no logical comparison with W is proved); neither is standard.

## Results (labels)
* Lemma 1.1, Prop 1.3, Cor 1.4 (dictionary, transference, scales) — PROVED.
* Prop 2.1 (Frobenius visibility), Prop 2.2 (indistinguishability, abstract-vector scope), Prop 2.4 (below 1/ε only the index
  condition is visible) — PROVED. Lemma 2.5 (GRH count of the index obstruction in the class; |C| ≤ 1, Serre's form of
  Lagarias–Odlyzko, Schinzel for Kummer degrees) — CONDITIONAL. Assessment 2.3 (GRH accounting of the general small-angle
  event; the former "Thm 2.3/Cor 2.4" cutoff x^{3/(2k+4)} is withdrawn as a theorem).
* Prop 3.1 (Fejér pair count, class-blind: #Bad₁(ε) ∩ (x/2, x] ≤ 48(6xε)^{(k+1)/(k−1)} log P/log(x/2), no 2^k loss) — PROVED.
  Cor 3.3: the P-loss in exact form; reproduces CAP_INTERPOLATION Thm 4.2(b). Not a GRH barrier (R264 D8).
* Thm 4.1 (GRH + EQ ⇒ (log₂p)^{13/2+o(1)}), Thm 4.2 (GRH + S ⇒ (log₂p)^{9/2+o(1)}) — CONDITIONAL, PROVED relative to hypotheses.
  Remark 4.3: GRH alone gives (log₂p)^{13/2+o(1)} for almost all p — not new (weaker than CAP_INTERPOLATION §2).
* Prop 5.1 (the guaranteed forced sub-box {0,1}^S cannot cover the §4 windows at cap 0; balance at positive cap says nothing
  about cap 0) — PROVED (narrowed after self-review: small windows CAN be covered at cap 0, e.g. p = 409, q = 11). T1: the route needs χ_n(q) = −1, impossible at n = m² (no forced windows).
* Numerics (EVIDENCE, §6): ν = 𝔻_min N^{1/k} matches the random model; ord ψ_min ≍ N; every class mod 840 has ν ≥ 1.48;
  EQ-type uniformity of existential Bad₁ over classes mod 840 (permutation p = 0.33/0.97/0.86) and mod 9240
  (p = 0.033/0.44/0.93; the 0.033 cell has 72 events in 480 classes); the full pretentious set incl. index-degenerate q is
  class-correlated (p = 0.003 at k = 3, 4) — the Chebotarev-visible part.

## Answers to the brief
GRH alone → (log₂p)^C: **no, by this route** (exact reason: SHARP 2 + Prop 3.1/Cor 3.3). GRH + named standard hypothesis: none
found; GRH + EQ or S (isolated, p-free) suffice. (i) almost all p: nothing new. (ii) cap 0: nothing (Prop 5.1, B2). (iii) numerics §6.

## Self-review / caveats
* A deep self-review (codex, R-O256) found 9 MAJOR issues (no FATAL); all repaired in BALANCED_LATTICE.md, marked
  "R-O256 repair n": Ĥ vs Û_q scope (1), Thm 2.3 demoted + new Lemma 2.5 for Bad₂ with correct error/main-term accounting (2, 3),
  visibility cutoff withdrawn (4), Prop 2.2 scoped to abstract vectors (5), Prop 5.1 narrowed (6), existential Bad₁ in
  z27_eqcheck + permutation null + order stats conditioned on generation (7), small-exponent memo bound corrected to cap ≳ log p
  i.o. (8), report wording (9). Exponents 13/2 and 9/2 survive (reviewer re-derived).
* Thm 2.3 and Bad₂ handling are citation-level (Kummer degrees, linear disjointness with ℚ(ζ_{8P}, √p) as in CAP_INTERPOLATION
  Thm 4.2); discriminant bound in Serre form n(Σ log p_ram + log n) (cf. R264 D9).
* Prop 2.2 is scoped to the Kummer–cyclotomic fields K_m with m | (q−1)/2, m ≤ M — not "all number fields".
* Exponents 13/2, 9/2 are not optimised (transference k^{3/2}, log P, square-root loss in Prop 3.1).

## Sparks (not pursued)
* Rank-k Erdős–Murty: prove S's index-degenerate part (index ≥ x^{θ}) with exceptional set x^{1−δ_k} better than the blind
  1 − 1/(2k); any power saving beyond Prop 3.1 in the *flat* (large-order pretentious) count lowers the P-loss.
* Use several disjoint generator blocks S₁, S₂, … with separate class conditions: needs independence of the Bad₁ sets across
  blocks — a "joint EQ" that may be easier to motivate.
* Pretentious-distance large sieve restricted to S-units with Fejér weights (z27_large_sieve_sunits fails only by sparsity;
  a sieve over q in a class weighted by Λ(q) and Kummer characters?).
* Is 𝔻_min's distribution (ν) exactly the random-lattice law? A precise conjecture (Siegel/Rogers measure for ℓ¹ minima of
  sublattices of index N) + test at larger k.
