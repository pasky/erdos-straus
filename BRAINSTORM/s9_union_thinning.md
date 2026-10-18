# s9_union_thinning — (★) ∪ b = 1 is a 2-adic thinning of one numerator-free set; the lines are positively correlated, beyond its size (O271, mandatory (iv); title R282 repair)

## Idea
The brief asked whether the X-parts of (★) and b = 1 are negatively correlated (a structural reason for the union's robustness:
if (★) fails, b = 1 is forced up) and for an identity linking the two counts. Put both on the word set
W(p) = {(t, u, v) : tuv − u − v = p} and test.

## Literature
SPARKS8 Prop 1.3 (López Type A duality, arXiv:2404.01508 Thm 7); DEDEKIND_ES Thm 4.5 (five-slice sign = 2-adic conditions on
(t, u, v)); O268 §4 (residual correlation 0.21–0.30, merged as (J)100).

## Statement (SYNTHESIS_SPARKS9 §1)
* Lemma 1.1 / Cor 1.2 (PROVED): (c, g, s) ∈ W(n) ↔ (cs, cg − 1, 1) ∈ W(cn); hence for k/n, c = 1 line ⟺ a word with k | t, b = 1 line
  ⟺ a word with k | v; the k-union ⟺ a word with a coordinate ≡ 0 (mod k). The only "identity" linking the two lines is that they
  are two 2-adic conditions on the same set.
* Prop 1.3 (EVIDENCE, ≤ 10⁷): corr = +0.37/+0.39 (positive); A = 0 ⇒ B at 0.59× its mean; partial correlation given log |W|:
  0.03/0.01 — (R282 repair) a collider effect since W ⊇ A ∪ B; given log(W − U) (size of the rest of W) it stays 0.346/0.353.
  Given W, the union count is a mirror-pair thinning with dispersion 2.4–3.8 (2 = exact mirror-binomial).

## Barrier screen
B2: W(p) is itself a divisor-in-moving-class count (each word is a divisor e ≡ −1 (mod u) of p + u). T1: σ ≡ +1 at squares kills
every union word (DEDEKIND Thm 4.5); W(m²)/L² ≈ 0.45 vs W(p)/L² ≈ 0.92. Numerator models: k = 8 union = coordinate ≡ 0 (mod 8),
fails at 131, 241 by the same thinning with smaller π — no 4-specific forcing.

## Cheap numerics
`scripts/s9_words.py`, `scripts/s9_words.c`, `scripts/s9_union_stats.py`, `scripts/s9_thinning.py`, `scripts/s9_sign.py`;
logs `logs/s9_union_1e6.txt`, `logs/s9_union_1e7.txt`.

## Assessment
Negative answer to (iv): no anticorrelation, no forcing; robustness = additive main terms on one common set; the two lines co-vary positively BEYOND the size of the rest of W(p) (R282 repair: partial corr ≈ 0.35 given log(W − U); the 0.01–0.03 given log W is mechanical).
Labels: Lemma 1.1 / Cor 1.2 PROVED (reformulation; Prop 1.3 of SPARKS8 extended to all odd n and all k); correlations EVIDENCE.
