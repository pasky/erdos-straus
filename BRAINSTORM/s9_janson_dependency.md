# s9_janson_dependency — a Janson/Harris inequality over p: what it would need, and the measured dependency term (O271, mandatory (iii))

## Idea
The data say per-level events are near-independent ((J)89) and failures follow an e^{−cμ^{0.91}}-type zero law ((J)97). The
probabilistic tool that turns "many weakly dependent events" into "P(none) ≤ e^{−(something)}" deterministically is Janson's
inequality, P(∩Ā_i) ≤ exp(−μ + Δ/2), resp. exp(−μ²/(2Δ)) when Δ ≥ μ. Ask: with the TRUE dependency structure of (★)-words,
what exponent would an (ideal) Janson inequality over primes give, and is it > log p (needed, Lemma 3.2)?

## Literature
Janson, Łuczak, Ruciński, *Random Graphs* (2000), Thm 2.14/2.18 (Janson inequalities; need a product space and increasing
events — Harris/FKG); EXCEPTIONAL_INTERFREQ (D)20: CRT-accurate correlations of order ≍ log N are false (squares avoid every class)
and TC_θ ⟹ E(N) ≤ (e+2)N exp(−(2/e²)(log N)^θ); (D)9–(D)24 caps at (log N)^{3/4} for CRT/large-sieve methods.

## Statement (SYNTHESIS_SPARKS9 Prop 3.3; EVIDENCE)
Words dependent ⟺ share one of tp + 1, p + u, p + v. Over 108 283 primes p ≡ 1 (4) ≤ 3·10⁶ binned by M_BM8:
Δ/μ = 3.6 → 9.4 (≈ linear in μ), so exp(−μ + Δ/2) > 1 and μ²/(2Δ) = 0.85 → 1.82 (vs log p ≈ 6 → 14): word-level Janson is
useless. At level granularity, E[#hit levels] = 2.65 → 13.8 = (0.44 → 0.97)·log p: a level-Poisson model is exactly critical
for Lemma 3.2 at accessible heights.

## Barrier screen
B6 (averages over p): an exponent > log p turns an over-p statement into a pointwise one (Lemma 3.2), so the hatch is legitimate
in shape; but (a) no product structure exists beyond CRT depth ≍ log N/log q, (b) over ℤ the Harris-type inequality is false by
T1 (squares have density N^{−1/2} ≫ e^{−μ}), (c) a BM-corrected Harris inequality over primes is T1-consistent but would give a
power-saving exceptional set for (★), beyond (D)9–(D)24. Numerator models: such an inequality is asymptotic, so 8/131, 8/241
(μ small) do not refute it — and also do not test it.

## Cheap numerics
`scripts/s9_janson.c`, `scripts/s9_janson_stats.py`, `logs/s9_janson.txt` (R cross-checked against O268's `z38_mbm.c`).

## Assessment
EVIDENCE + Assessment. Precise answer to "why near-independence cannot be turned into a proof": the near-independent units are
levels, their expected number is only ≈ log p at 10⁶, and no inequality with a product structure is available; within a level
the hits cluster (divisors of one integer), which is what makes the lower tail Landau-type rather than Poisson. CONJECTURE-shape
only (BM-Harris over primes), no evidence of a technique. No route.
