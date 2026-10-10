# AGENT REPORT O131b — Type I CM torus (round 2), branch side-agent/exact-formula

Deliverable: `EXACT_FORMULA.md` §5. Scripts: `scripts/exf_cm_check.py` (PARI via `uv run --with cypari2`),
`scripts/exf_cm_classes.py`, `scripts/exf_cm_bias.py`; outputs `data/exf/cm_classes_out.txt`, `data/exf/cm_bias_out.txt`.

## Results
* **Lemma 5.1 (PROVED; PARI-checked on 9908 triples):** for p inert, p ∤ 2cd, α = p + 2c√−d is primitive and every
  prime of N(α) splits with exactly one prime above it dividing α. So ideal divisors of (α) ↔ integer divisors of
  N(α) = p² + 4c²d, bijectively via the norm.
* **Theorem 5.2 (PROVED):** T1_{c,d}(p) = #{𝔞 | α : N𝔞 ≡ −p mod 4cd}. This is a ray-class condition mod 4cd, but
  one that factors through the norm. In the Hecke-character expansion only χ∘N occurs, so among class-group
  characters only the genus characters occur; all non-genus Hecke/class-group characters have coefficient 0. The
  count equals (1/φ(4cd)) Σ_χ χ̄(−p) σ_χ(p² + 4c²d) = ((1 + χ_{−4d}(−p))/φ(4cd)) Σ_{χ mod ⟨χ_{−4d}⟩} …. That is O123's
  genus factor as an exact identity, and the same Dirichlet/Eisenstein divisor-count object as Type II (O128 9.1).
  **Answer: it is genuinely a ray-class divisor count of a single element, not a class-group-theoretic quantity.**
* **EVIDENCE (p ≤ 2·10⁴):** all Type I ideals of (p,d) lie in one genus. Inside it the class distribution is biased
  towards the principal class (≈ 2× the other classes; share 0.23–0.37 vs 1/h = 0.125–0.25 for d = 14, 26, 29,
  41). The bias does not decay over this range and comes from the small complementary norm e. It is a
  small-norm/L(1,ψ) effect in the mean, never pointwise; no class is always hit.
* **Weight 3/2 / Brandt:** only the round-1 H-coefficient tests were done (rank intersection 0); Brandt matrices at
  level n were not computed. Assessment in §5.4: no mechanism, plus a √p vs log³p size mismatch.

## Verdict
Negative, exact scope. Both the split (Type II) and the anisotropic CM (Type I) tori reduce to norm conditions mod
4cd. ES at fixed (c,d) is a divisor-in-residue-class condition on one integer, with genus theory as the only
class-group content. No class-number positivity is available along this route.

Suggested ledger addition to (I)x O131: "+ round 2: Type I CM torus collapses (Thm 5.2: only genus characters occur;
the count is σ_χ(p² + 4c²d) twisted by Dirichlet characters); class bias only in means (EVIDENCE)."
