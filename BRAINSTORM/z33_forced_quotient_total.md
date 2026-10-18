# z33_forced_quotient_total — the total product's forced quotient is all of G (O263; CLASS_FORCING §2)

**Idea.** Reciprocity "forces" χ(N) for quadratic χ (Lemma 2.2(b) of SYNTHESIS_SPARKS8). Push to higher characters / the
full class of N in G = (ℤ/t)^× and ask when E(N, t) ("a divisor ≡ −1 (mod t)") follows.
**Literature.** Elementary; z29_forced_level_characters (χ₋₄ never forced on the b = 1 line); JOINT_BUDGET §4.1.
**Result (PROVED, Thm 2.1(a), Table 2.2).** On every ES line (b = 1: p + 4d; dual: cp + 1; Type II/I e-slices) 4N mod t is
p, cp + 1, p, 1 resp.: the FULL class of N is congruence data, so H_forced = {1}; no reciprocity law adds anything to it.
Since a prime N is compatible, the forced subset-product set of the total is {1, [N]}; E is forced from total data iff
[N] = −1, which never happens on the b = 1 line (p ≡ 1 (4)). Table for d ≤ 30: exponent 2 only for d ∈ {1, 2, 3, 6}.
**Barrier screen.** B1: knowing [N] is congruence data. T1: at p = m² the same total data occur (m² ≡ 1 mod everything coprime
admits squares) and E fails. Prop 10.3: the χ-shadow is G/G²; here even the full G-class does not suffice.
**Cheap numerics.** `scripts/z33_forced_quotient_table.py` (−1 ∉ ⟨[p]⟩ for every possible [p], d ≤ 30).
**Assessment.** Closes "class of the total product" as a source of forcing; the gap is the factorisation, not the class.
