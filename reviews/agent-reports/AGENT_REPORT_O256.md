# AGENT_REPORT_O256 — balanced relation lattices: from Hypothesis W to GRH (checkpoint 1)

Branch side-agent/balanced-lattice (merged O252 and main incl. R264 repairs). Main file BALANCED_LATTICE.md; memos
BRAINSTORM/z27_*.md (6); scripts scripts/z27_dual.py, scripts/z27_eqcheck.py; data data/z27/ (tiny).
**ES is not solved; no infinite case of ES is claimed. Bounded / (log₂p)^{O(1)} cap is NOT ES — cap 0 is the B2 divisor event.**

## SHARP:
1. **Exact dual dictionary (PROVED, §1):** Λ_q(S)*/ℤ^S ≅ Û_q; cube covering radius ≍ 1/𝔻_min within k^{3/2} (Banaszczyk),
   𝔻_min = min_{ψ≠1} Σ_{s∈S} ‖arg ψ(s²)/2π‖. *q is balanced ⟺ no nontrivial character of U_q is ℓ¹-pretentious to 1 on the k
   forced primes at the Minkowski scale N^{−1/k}.*
2. **The balance-deciding character has order ≍ N, divisible by P⁺(q−1) (EVIDENCE, §6):** in > 99 % of q (k = 3, 4, 5; q ≤ 10⁷),
   identical to the uniform-discrete-log model; orders in the GRH-visible range ≤ N^{3/(2k+4)}: ≤ 0.07 %. Combined with the
   **indistinguishability Prop 2.2 (PROVED)**: Frobenius data in ℚ(ζ_m, S^{1/m}), m ≤ M, is a function of the discrete logs mod
   the M-smooth part of q − 1, and is compatible with L_min ≥ (M-rough part) − 1. ⇒ The brief's Hooley/Kummer route certifies only
   the index condition (+ a negligible fraction of characters).
3. **GRH + a p-free, class-free sparsity hypothesis S ⇒ e*(p) ≤ (log₂p)^{9/2+o(1)} (Thm 4.2, CONDITIONAL);** GRH + EQ
   (no over-concentration of large-order pretentious primes in classes mod 8P) ⇒ (log₂p)^{13/2+o(1)} (Thm 4.1). S = #{q ≤ x :
   some character of order > x^{3/(2k)} has 𝔻_S < x^{−3/(2k)}} ≤ x^{1/2+o(1)} — the random-model prediction; a rank-k
   "small multiplicative order" sparsity statement (Erdős–Murty/Kurlberg–Pomerance analogue). Both strictly weaker in form than
   W; neither is standard.

## Results (labels)
* Lemma 1.1, Prop 1.3, Cor 1.4 (dictionary, transference, scales) — PROVED.
* Prop 2.1 (Frobenius visibility), Prop 2.2 (indistinguishability) — PROVED. Thm 2.3 (what GRH certifies: no ε-pretentious
  character of order ≤ M for ≫ x/(φ(8P) log x) q in the class) — CONDITIONAL (GRH, Lagarias–Odlyzko; citation-level proof).
  Cor 2.4: below N^{1/k} the visible part is exactly the index condition; GRH reaches M ≤ x^{3/(2k+4)}.
* Prop 3.1 (Fejér pair count, class-blind: #Bad₁(ε) ∩ (x/2, x] ≤ 48(6xε)^{(k+1)/(k−1)} log P/log(x/2), no 2^k loss) — PROVED.
  Cor 3.3: the P-loss in exact form; reproduces CAP_INTERPOLATION Thm 4.2(b). Not a GRH barrier (R264 D8).
* Thm 4.1 (GRH + EQ ⇒ (log₂p)^{13/2+o(1)}), Thm 4.2 (GRH + S ⇒ (log₂p)^{9/2+o(1)}) — CONDITIONAL, PROVED relative to hypotheses.
  Remark 4.3: GRH alone gives (log₂p)^{13/2+o(1)} for almost all p — not new (weaker than CAP_INTERPOLATION §2).
* Prop 5.1 (balance says nothing at cap 0) — PROVED. T1: the route needs χ_n(q) = −1, impossible at n = m² (no forced windows).
* Numerics (EVIDENCE, §6): ν = 𝔻_min N^{1/k} matches the random model; ord ψ_min ≍ N; every class mod 840 has ν ≥ 1.48;
  EQ-type uniformity of Bad₁ over classes mod 840 (χ² 29–49, df 47) and mod 9240 (χ² 404–475, df 479); the full pretentious
  set incl. index-degenerate q is non-uniform (χ² 214, df 47) — the Chebotarev-visible part.

## Answers to the brief
GRH alone → (log₂p)^C: **no, by this route** (exact reason: SHARP 2 + Prop 3.1/Cor 3.3). GRH + named standard hypothesis: none
found; GRH + EQ or S (isolated, p-free) suffice. (i) almost all p: nothing new. (ii) cap 0: nothing (Prop 5.1, B2). (iii) numerics §6.

## Self-review / caveats
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
