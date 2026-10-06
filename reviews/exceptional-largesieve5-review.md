# Review R67b — EXCEPTIONAL_LARGESIEVE5.md (task O67, branch side-agent/astar-dense)

Reviewer: hostile side agent, branch `side-agent/review-ls5`. Independent of
the author's self-review R67. From-scratch scripts: `scripts/review_ls5_*.py`.

## Verdict per claim

| item | verdict |
|---|---|
| Lemma 1.1 (monotonicity in the family) | SOUND (the lemma); the appended sentence on fibres is wrong → D1 |
| Lemma 1.2 (rational labels, compatibility) | SOUND (constant improvable: `H₁H₂ ≥ g`, D2) |

(further rows added below as the review proceeds)

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
