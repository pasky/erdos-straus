# Review R67b — EXCEPTIONAL_LARGESIEVE5.md (task O67, branch side-agent/astar-dense)

Reviewer: hostile side agent, branch `side-agent/review-ls5`. Independent of
the author's self-review R67. From-scratch scripts: `scripts/review_ls5_*.py`.

## Verdict per claim

| item | verdict |
|---|---|
| Lemma 1.1 (monotonicity in the family) | SOUND (the lemma); the appended sentence on fibres is wrong → D1 |
| Lemma 1.2 (rational labels, compatibility) | SOUND (constant improvable: `H₁H₂ ≥ g`, D2) |

| Setting 2.0 (truncated forbidding) | SOUND after a constant repair (leak bound misses `1/(1−p̃)`, D3) |
| Prop 2.1 ((B) for the tilted law) | SOUND |
| "LS4 Thm 4.2 holds with (A*_tilt)" | SOUND-AFTER-REPAIRS (the base law Q' changed; (Q1)–(Q4) must be re-asserted, D4) |
| Caution (LS4 Lemma 5.1 does not transfer) / Rem 2.2 | correct retraction; Rem 2.2 correctly labelled Assessment |
| Lemma 3.1 (label partition, product model) | SOUND (CS_j needs a convention when `q | den λ_j`, D5) |
| §4 caveat (undamped product model fails uniformly in X) | correct retraction (verified); quantitative aside slightly off, D7 |
| (LCH) withdrawal | correct |
| Cor 4.2 | correctly labelled SKETCH; sketch arithmetic checks out given its stated gap |
| §4 (C1)–(C3), (S) | Assessment; minor wording, D8–D9 |
| §5 numerics | reproduced independently (EVIDENCE) |
| Overall labels | nothing claims (CC)/(A*); no overclaim beyond D1 |

## Claim-by-claim

### Lemma 1.1

Re-derived from LS §1: a bound is CRT-admissible for 𝔊 iff `L ≤ F_w(π)` for
all `π ∈ P(𝒜(𝔊))`; since `𝒜(𝔊') ⊆ 𝒜(𝔊)`, `P(𝒜(𝔊')) ⊆ P(𝒜(𝔊))`, so
`L ≤ F*_w(𝔊')` and the cap for 𝔊' applies. For the Hölder route the
measure π on `𝒜(𝔊')` is a legitimate measure on `𝒜(𝔊)`. Correct and
trivial, as labelled.

The follow-up paragraph, however, says "no adversarial sub-selection of
moduli has to be handled: every sum over classes through a prime is a
complete sum over cofactors … Fibres at a smooth part c are still full in
the rough direction (all rough cofactors occur)". This is false for the
objects (A*) is actually about (LS4 Thm 4.2 needs (A*) for the **fibre**
laws `σ_c`, whose family is `𝔊_{X,c}`): see D1.

### Lemma 1.2

Checked by hand: ℛ(M): `gcd(A,M)=1` (4A−M=1), `16DD' = (4A)² ≡ 1 (M)`, so
`−1/(4D') ≡ −4D`; heights `4D ≤ M+1` resp. `4D' < M+1`. (a,D): `D ≤ g(D)²`
so `4D+a ≤ 4g²+a ≤ 16a²g² = G²`. Case A: `4rh² = h·G ≡ 0 (G)`, so
`mm' ≡ 1 (G)`; `min(m,m') ≤ √(4rh²+1) ≤ 4rh`. Compatibility: since all
labels have `r ≥ 0`, `|r₁s₂ − r₂s₁| ≤ max(r₁s₂, r₂s₁) ≤ H₁H₂`, so in fact
`H₁H₂ ≥ g` (the stated `g/2` is correct but loses 2).

From scratch: `scripts/review_ls5_labels.py 300` enumerates all 2746
classes of the four types with modulus ≤ 300, verifies label ≡ class,
`gcd(s,G)=1`, `r ≥ 0` and the height bounds; over all 265259 pairs of
distinct labels congruent mod some `g > 1` dividing both moduli,
`min H₁H₂/g = 1.0034` (attained by `−297` vs `−1`, g = 296), confirming
`H₁H₂ ≥ g`; and "at most one label of height `< √(g/2)` per class mod g"
holds for every g ≤ 300. SOUND.

### Setting 2.0 and Proposition 2.1

Re-derived. (i) Truncation: if `p ≤ δ` then `|F| ≤ ⌊δ|Ω|⌋`, so `F̃ = F`;
adding one residue changes `F̃` by ≤ 2 elements; an activation of a class
mod `q^v` changes `p̃_q` by `≤ q^{−v} ≤ 1/q`. (ii) Leak: given the past,
`P(x_ℓ ∈ F∖F̃) = (p−p̃)/(1−p̃)`, **not** `≤ p − p̃` (D3; factor ≤ 2).
(iii) Prop 2.1: `E_T𝓡_2(σ_T) = E_{σ⊗σ}Π(1+w_ℓh_ℓ)` (LS4 Lemma 1.1) and
`σ = Q'Φ/Z` give `Z^{−2}E_{Q'⊗Q'}[Φ(x)Φ(x')Π(1+wh)]`; the change of measure
`dQ/d(Q'⊗Q') = ΠZ_ℓ`, `Π(1+wh) = Π(1+wη)·ΠZ_ℓ` is an identity of
integrands, so any Φ (indeed any function of the pair path) may be
inserted. `1+η = ℓ^EΣ_a k k' ≤ ℓ^E max k = (1−p̃(x))^{−1}`, so
`Π(1+wη) ≤ e^{2Y(x)}` with `p̃ ≤ δ ≤ 1/2`; `Φ(x)e^{2Y(x)} ≤ 1`, `Φ(x') ≤ 1`,
and `E_Q 1 = 1`. Lower bound for Z by Jensen on `𝒜` and `Y ≥ 0`.
Arithmetic: `(16/3)m + 2log(4/3) ≤ 6m + 1`. All correct.

From scratch: `scripts/review_ls5_tilt.py 8` builds random rough families
on primes {3,5,7}, {2,3,5,7} (up to 30 classes, moduli with ≤ 3 primes,
δ = 1/2 so truncation really occurs), enumerates the truncated sequential
law exactly, and checks (exactly in ℚ for the rational tilt
`Φ = 1_𝒜/Π(1+2w p̃)`, which the same proof covers, and in 60-digit
mpmath for `Φ = 1_𝒜e^{−2Y}`): the pair-sum = T-decomposition identity,
`E_T𝓡_2 ≤ Z^{−2}`, Jensen's lower bound for Z, `log E_T𝓡_2 ≤ 6EY + 1`
when `Q'(𝒜) ≥ 3/4`, and `η ≤ p̃/(1−p̃)` on 2000 random steps. All pass
(max `E_T𝓡_2/Z^{−2}` = 0.70). The leak exceeded `EΣ(p−p̃)` in 44 of the
runs and was always `≤ 2EΣ(p−p̃)` — confirming D3.

*Transfer to LS4 Thm 4.2.* The document changes the base law itself
(truncated instead of K2's light/heavy forbidding), not only σ_c. Thm 4.2
uses (Q1)–(Q4) of LS3 §2 for Q'. I checked that all four follow from the
chain rule (Q4) `Q'(n ≡ b (m)) ≤ Γ(m)/m`, `γ'(ℓ) = (1−ℓ^{−1/2})^{−1}`
(K2 §2, Lemma 4.1, Lemma 4.3), whose only input is that each step forbids
mass `≤ δ_ℓ`; the truncated rule forbids `p̃ ≤ δ_ℓ`, so (Q4) and hence
(Q1)–(Q2) hold verbatim, and (Q3) (leak) holds up to the factor 2 of D3.
The smooth marginal is unchanged (smooth coordinates come first). So the
transfer is correct, but it is not stated in the document (D4).

The *Caution* paragraph (LS4 Lemma 5.1/Thm 5.2 do not transfer: prefactor
`Z^{−1}` instead of `Q'(G_B)^{−1} ≤ 2`) is correct: Lemma 5.1 bounds
`|σ̂|` by `‖Φ‖_∞/Z` × pivotal probability, and `Z^{−1}` can be
`e^{2m_c}`-large. So the price of Prop 2.1 is that (A*) is open for a
*new* law; this is honestly stated. Remark 2.2: the example class
`(−4D, ℓq)`, `q ≡ −ℓ^{−1} (4D)` is valid (`ℓq ≡ −1 (4D)` gives
`4D | M+1`, `D | A`, `D ≤ A`); the rest is heuristic and labelled
Assessment. Typo "only yields only" (applied by reviewer, see below).

### Lemma 3.1

Re-derived: the witness at ℓ gives `v_ℓ ≡ λ(ℓ)`; for `q ∈ G_j ∩ S`
matching gives `v_q ≡ λ_j`, and `v_q ≡ λ_{j(q)}`, so `q ∈ U_j` or
`λ_j ≡ λ_{j(q)} (q)`; on `Q_j ⊆ U_j ∪ CS_j` the class condition is then
automatic, so only `y ≡ λ_j` on `m_j` remains, and v, y are independent.
The `Π ℓ^{−1}` is exact for squarefree coordinates. Correct.

From scratch: `scripts/review_ls5_partition.py 3,7,11,19 3` (full ℛ(M)
family + selectors over the pool, 78 classes, 51 labels) computes
`P(E_S)` and the full right-hand side of Lemma 3.1 exactly in ℚ for all
`|S| ≤ 3` (all partitions, all distinct label tuples, y enumerated), and
checks the proof's pointwise construction at every point of `E_S`.
Inequality holds in all 14 cases (LHS/RHS between 0.37 and 0.97). The
first run crashed exactly at the ambiguity D5 (a label `−1/(4D')` with
`q | 4D'`, q ∈ S).

### §4: retractions and Assessment

*Caveat (undamped model fails uniformly in X).* Verified: for `a ≢ 0 (ℓ)`
take `D ≡ −a/4 (ℓ)`, `1 ≤ D < ℓ`; for every prime `q ≡ −ℓ^{−1} (4D)`,
`M = ℓq ≡ −1 (4D)` so `D | A` and `(−4D, ℓq)` is an ℛ(M) class with
residue a at ℓ, matched with probability `1/q` independently; `Σ1/q = ∞`
over such q, so `P(E_{{ℓ}}) → (ℓ−1)/ℓ`, and `→ 1` with the selector
`0 mod ℓ`. The retraction is correct and necessary, and it also
correctly downgrades everything else in §4 to the regime
`log X ≤ z^c`. The aside "`P(E_{{ℓ}}) ≤ (log X)³/ℓ`" is slightly off (D7).

*(LCH) withdrawal.* The counterexample (one block, `2^t` labels `−4d`,
`d | P | A_M`) is valid; withdrawing is right.

*Cor 4.2.* Labelled SKETCH with the gap stated (moments of `τ(A²)` over
shared primes). Given that gap, the bookkeeping is consistent: with
`|S| ≤ c₀ log log N`, `(C log X)^{2^{|S|}}` costs
`exp(A (log N)^{c₀ log 2} log log N) = z^{o(1)}` for `c₀ log 2 < 1/4`, so
`c₀ < 1/5` suffices. Fine as a calibration.

*(S).* `−4D ∈ Λ(Q'm) ⟺ 4D^♮ | Q'm + 1` (and `D ≤ A`) is right
(`D | A² ⟺ D^♮ | A`); at most one short m per label is right. The
Lenstra/CHN threshold `A^{1/2+ε}` (divisors of `A²` in a class mod
`g > (A²)^{1/4+ε}`) matches the statements I know (Lenstra 1984: modulus
`> n^{1/3}`, ≤ 11 divisors; Coppersmith–Howgrave-Graham–Nagaraj 2008:
`> n^{1/4+ε}`, `O_ε(1)`); sources not available in `sources/`, checked
from memory only. Correctly Assessment.

### §5 numerics

Independent numpy re-implementation `scripts/review_ls5_cover.py`
(same pool {7,11,19,23,31,43}, 4.485·10⁷ points): coverage
probabilities 0.121–0.467, max ratios 1.558 / 2.443 / 4.092 for
|S| = 2/3/4 — identical to the document. (I count 1504 classes by
divisor D, the document 1428, presumably after merging coincident
residues; coverage is unaffected.) For |S| = 5, 6 the per-prime ratio is
1.427 / 1.405, so "≈ 1.42 at most" is accurate only for |S| ≤ 4, as
stated. EVIDENCE, correctly labelled.

## Defects

**D1 (MAJOR; §1, paragraph after Lemma 1.1, last two sentences).** The
fibre family at a smooth part c is *not* full: a class `(λ, G_sG_r)` with
smooth part `G_s > 1` belongs to `𝔊_{X,c}` iff `c ≡ λ (mod G_s)`. So in
the fibre the classes through a rough prime are a **c-dependent
filtration of labels** (by congruence at the smooth primes), and (A*) is
required for every c off an event of probability 1/32, not on average
over c. "Every sum over classes through a prime is a complete sum over
cofactors" holds only for the sub-family of z-rough moduli, or after
averaging over c (K2 chain rule). Since §4 invokes exactly this
completeness to justify divisor-in-progression averages, the plan of §4
inherits the gap. *Repair:* replace by "Fibres at c contain every class of
z-rough modulus; a class with smooth part `G_s > 1` is present iff
`c ≡ λ (mod G_s)` — a c-dependent filter on labels. Complete cofactor
sums are available only for the rough-modulus subfamily or after
averaging over c; for (A*) at a fixed typical c the filter must be
handled (e.g. by putting c with atypical filtered mass into the
exceptional event)."

**D2 (MINOR; Lemma 1.2, compatibility).** Since every label has `r ≥ 0`,
the bound is `H₁H₂ ≥ g` (and "at most one label of height `< √g`").
Not an error.

**D3 (MINOR; Setting 2.0, "The leak is `≤ EΣ_ℓ(p_ℓ − p̃_ℓ)`").** Under the
truncated rule `x_ℓ ~ U(·|Ω∖F̃_ℓ)`, so the leak at ℓ has conditional
probability `(p−p̃)/(1−p̃) ≤ 2(p−p̃)`. Counterexample to the stated bound:
a single step ℓ = 5, δ = 1/2, three always-activated residues: `p = 3/5`,
`p̃ = 2/5`, leak `= 1/3 > 1/5`. *Repair (applied by reviewer):* "`≤
EΣ_ℓ(p_ℓ−p̃_ℓ)/(1−p̃_ℓ) ≤ 2EΣ_ℓ p_ℓ1[p_ℓ > δ_ℓ]`". Only K2 Lemma 4.3's
constant changes.

**D4 (MINOR; §2, "So in Theorem 4.2 of LS4 one may use σ_c := σ_tilt").**
The base law Q' is changed (truncated forbidding), so Thm 4.2's inputs
(Q1)–(Q4) must be re-asserted for it. They hold (all follow from the
chain rule, which only needs per-step forbidden mass `≤ δ_ℓ`). *Repair
(applied by reviewer):* one sentence saying so.

**D5 (MINOR; Lemma 3.1, definition of CS_j).** `λ_j ≡ λ_{j(q)} (mod q)` is
undefined when q divides the denominator of `λ_j` or `λ_{j(q)}` (e.g.
`λ = −1/(4D')`, `q | D'`). Such q cannot divide the modulus of a class
with that label, so the convention "not congruent" is the right one.
*Repair (applied by reviewer):* add "(q ∉ CS_j if q divides the
denominator of λ_j or of λ_{j(q)})".

**D6 (MINOR; §3 first paragraph, "the path law dominates this up to
Π(1+2p^{−1/2})").** Direction reversed: the inflation bound says the
product model dominates the path law (`P_path(match) ≤ Γ(G)/G`). *Repair
(applied by reviewer):* "the path law is dominated by this up to …".

**D7 (MINOR; §4 Caveat, "then `P(E_{{ℓ}}) ≤ (log X)³/ℓ`").** The union
bound gives `P(E_{{ℓ}}) ≤ Mass(ℓ)/ℓ` (+`1/ℓ` for the selector), and by
the document's own bound `Mass(ℓ) ≤ C(log X)³ + ℓ^{O(1/log log ℓ)}`; the
`ℓ^{o(1)}` term is not dominated by `(log X)³` for large ℓ. *Repair
(applied by reviewer):* "`≤ (C(log X)³ + ℓ^{o(1)})/ℓ`".

**D8 (MINOR; §4, bound on `Mass(Q')`).** Stated as "standard" without a
label or proof; it is a K2-Lemma-4.2-type Shiu estimate (needs Shiu's
range `Q' < x^{1−ε}`, short range by the pointwise divisor bound; Case-A
labels need the ElT input as in K2 Lemma 3.6). *Repair (applied by
reviewer):* tag it "(Assessment: standard, as in K2 Lemmas 3.3–3.6 and
4.2; not re-proved here)".

**D9 (MINOR; §4 (C2)).** "harmless iff `|S| ≤ (1/2 − γ)log₂ z`" — the
trivial count gives total `≤ 2^{|S|+k|S|}`, i.e. `≤ 2^{1+|S|}` per
S-prime, so the condition is sufficient but not necessary (and not
sharp). *Repair (applied by reviewer):* "iff" → "if". Same for "harmless
iff" in (C3).

**D10 (MINOR; Rem 2.2).** Typo "only yields only one prime of decay".
*Repair (applied by reviewer).*

## Summary

No FATAL defect in what is claimed. The four PROVED items (Lemmas 1.1,
1.2, Prop 2.1, Lemma 3.1) are correct; independent exact computations
confirm them. The retractions (undamped product model, (LCH), LS4 Lemma
5.1 for σ_tilt) are correct and needed. One MAJOR item: D1, the claim
that fibres are "full" — the fibre family at a smooth c filters labels
by `c ≡ λ (mod G_s)`, so the "complete cofactor sum" mechanism promised
for §4 is only available for rough moduli or on average over c. Nothing
in the document claims (CC) or (A*); the open problem is correctly
located in (C2)/(C3) for damped witness weights, now additionally with
the c-filter of D1.

## Repairs applied by reviewer to EXCEPTIONAL_LARGESIEVE5.md

D1 (fibre sentence replaced by the corrected statement), D3 (leak factor
`1/(1−p̃)`), D4 ((Q1)–(Q4) re-asserted for the truncated law), D5 (CS_j
convention), D6 ("is dominated by"), D7 (`ℓ^{o(1)}` term), D8 (Mass bound
tagged Assessment), D9 ("iff" → "if", twice), D10 (typo); status header
notes R67b. No mathematics changed beyond these repairs. D2 not applied
(the `g/2` constant is correct).

## Replay

    ulimit -v 8000000
    timeout 600  env PYTHONPATH=scripts uv run python scripts/review_ls5_labels.py 300
    timeout 1800 env PYTHONPATH=scripts uv run --with mpmath python scripts/review_ls5_tilt.py 8
    timeout 1500 env PYTHONPATH=scripts uv run python scripts/review_ls5_partition.py 3,7,11,19 3
    timeout 1500 env PYTHONPATH=scripts uv run --with numpy python scripts/review_ls5_cover.py
