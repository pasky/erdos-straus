# Hostile review R88 of EXCEPTIONAL_SHORT.md (task O88)

Reviewer: side-agent/review-short. Source reviewed: `EXCEPTIONAL_SHORT.md` and
`reviews/agent-reports/AGENT_REPORT_O88.md` as merged from `side-agent/short-intervals`.
Note = `paper/es-threequarter-note.tex` (internally proved, unrefereed). All verdicts
below are **relative to the note's thm:assembly / lem:identity / lem:CRT**; I did not
re-audit the note's void/moment machinery (outside R88's scope).

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (local mean, shift-uniform) | SOUND (statement slightly weaker than its proof; see D3) |
| Lemma 1.2 (smooth-part decomposition, chain, Rankin) | SOUND |
| Theorem 1 | SOUND (rel. note) |

## Claim-by-claim re-derivation

### Lemma 1.1
Re-derived. thm:assembly expands ν_X = S_y·Q_r(H_X) into ≤ T_abs signed plain
congruence classes a (mod q), every nonempty modulus dividing 𝓜 (eq:termq; atoms at
the same ℓ have distinct projections mod ℓ, lem:CRT, so intersections are empty or one
class). Intersecting with β (mod Q) gives empty or one class mod lcm(q,Q). For *any*
real half-open interval of length H, #{n ∈ (z,z+H] : n ≡ a' (m)} = H/m + θ, |θ| < 1
(checked: floor((z+H−a')/m) − floor((z−a')/m) differs from H/m by < 1). Summation gives
Σ_{n∈I, n≡β(Q)} ν_X(n) = H·E_{Z/lcm(𝓜,Q)}[ν_X 1_{β(Q)}] + O_{≤1}(T_abs). Nothing in
eq:transfer uses the left endpoint; the period 𝓜 (= e^{≍X}, astronomically larger than H)
never needs to be ≤ H, because the count is done class-by-class with O(1) error each, not
period-by-period. The selector period P_y is inside the same expansion. **SOUND.**
Positivity ν_X ≥ 0 (lem:Bonferroni) gives E[ν 1_β] ≤ E ν ≤ e^{−c_a t^3}.

### Lemma 1.2
(a) ES representability is inherited by multiples (4/(dm) = Σ 1/(d x_i)); 1 is
exceptional (4 > 3·1). Correct; n ↦ (d,m) is a bijection, so no double counting.
(b) Chain d = d_0 > d_1 > … > 1 removing one prime ≤ y each step: the last element
> D_0 has successor ≤ D_0 and ratio ≤ y, so lies in (D_0, yD_0]. Correct.
(c) Rankin with exponent 1/2: Σ_{d'>D_0, y-smooth} 1/d' ≤ D_0^{−1/2} Π_{p≤y}(1−p^{−1/2})^{−1};
−log(1−u) ≤ 2u on [0, 2^{−1/2}] (worst at u = 2^{−1/2}: 1.228 ≤ 1.414) and
Σ_{p≤y} p^{−1/2} ≤ Σ_{n≤y} n^{−1/2} ≤ 2√y. Correct (numerically checked, script below).
**SOUND.**

### Theorem 1
(F2) re-derived: lem:identity is stated for every n ≥ 1, so every exceptional m ≥ 1
has H_X(m) = 0 (no restriction m > K or m > ℓ is needed — e.g. m = 1 lies in no atom
class since kℓ ∤ u+v as u+v ≤ 2z_j < ℓ); with (m,P_y)=1 and Q_r(0)=1, ν_X(m) = 1.
The note's own restriction "exceptional prime n > max(K,y)" is merely conservative.

Case (ii), the worry "m ranges over an interval of length H/d, short for large d":
harmless, because Lemma 1.1 has *additive* error T_abs per d irrespective of length,
and there are ≤ D_0 = e^{2c_a t^3} values of d, so the total additive error is
D_0·e^{C_L t^4} = e^{O(t^4)}; H/d may even be < 1 without harm. The main terms sum to
H e^{−c_a t^3} Σ_{d≤D_0} 1/d ≤ H(1+2c_a t^3)e^{−c_a t^3}.

Case (i), the worry "smooth numbers are not equidistributed in short intervals": the
proof never uses distribution of smooth numbers in I. It only uses the trivial
#{n ∈ I : d' | n} ≤ H/d' + 1 for each y-smooth d' ∈ (D_0, yD_0], summed by a union
bound; the +1's total ≤ yD_0 = e^{O(t^3)}. Correct.

Balance: E(I) ≤ C_1 H e^{−c_a t^3/2} + e^{C_2 t^4}, t = (log H/(2C_2))^{1/4} needs
t ≥ log X_a, i.e. H ≥ exp(2C_2 (log X_a)^4) — a fixed threshold; below it trivial.
Since thm:assembly is asserted for *every* X ≥ X_a (not a sequence of X), a
continuous choice of t is legitimate. Uniform in z, no H ≤ z or z ≥ 0 hypothesis.
Corollary ranges (H ≥ x^θ ⇒ saving θ^{3/4}(log x)^{3/4}) are immediate. **SOUND.**
