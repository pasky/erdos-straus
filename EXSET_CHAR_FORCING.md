# EXSET_CHAR_FORCING — pointwise character forcing "(q/p) = −1 ⟹ ES(p)" with a growing reach

*Wave z51, lane 2c, slug `forcing`. Brief: `/home/pasky/projects/math/z51briefs/2c_opus_forcing.md`. ES is OPEN; nothing
here claims it proved or disproved. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z51_forcing_*`, data `data/z51_forcing/`, reviews `reviews/z51-forcing-*`.*

## 0. Summary table

| # | claim | label | review |
|---|---|---|---|
| 1 | audit: what the Linnik route needs, which gate (G2–G4) each item attacks | Assessment | (pending) |
| 2 | window criterion and deterministic covering lemma | (pending) | (pending) |
| 3 | per-window failure rates; G4 checked | (pending) | (pending) |
| 4 | joint failure across windows; G2 loss | (pending) | (pending) |
| 5 | robust Linnik confinement | (pending) | (pending) |
| 6 | full Type I/II forcing reach, numerics to 10¹⁰, fits | (pending) | (pending) |
| 7 | least-QNR lines, n₂(p) = 17 | (pending) | (pending) |
| 8 | remaining gap | Assessment | — |

**Bottom line.** (pending)

## 1. Audit

### 1.1 The route and the input it needs

Notation. p ≡ 1 (mod 8) prime (p ≡ 5 (8) and p ≡ 3 (4) are classical). For a prime q ∤ 2p, (q/p) = (p/q) by
reciprocity. n₂(p) is the least quadratic non-residue (odd prime here). ES(p) means 4/p = 1/x + 1/y + 1/z.

**Forcing hypothesis F(R).** For every large prime p and every prime q ≤ R(p): (q/p) = −1 ⟹ ES(p).

**Observation 1.1 (PROVED, standard inputs; this is G3 made exact).**
(a) ES ⟹ F(R) for every R (trivially).
(b) F(R) with R(p) ≥ (log p)^A, A > 2, ⟹ #{p ≤ X : ES(p) fails} ≤ X^{2/A+o(1)}.
(c) Under GRH, F(R) with R(p) ≥ 2 log²p ⟹ ES(p) for all large p.
*Proof.* (b) If ES(p) fails then (q/p) = +1 for all q ≤ (log p)^A; for p ∈ (X^{1/2}, X] this includes all
q ≤ (½ log X)^A. Linnik's large sieve in the form of CAP_BOUNDED Thm 3.2 (with 𝒜 = products of primes
q ≤ y = (½ log X)^A, no congruence restriction on q; |𝒜 ∩ [1, X²]| = X^{2(1−1/A)+o(1)}) gives
≤ (X² + X²)/X^{2−2/A+o(1)} = X^{2/A+o(1)} such p; p ≤ X^{1/2} are trivially few. (c) Under GRH n₂(p) < 2 log²p
(Bach 1990, recalled). ∎

So F at reach ≍ log²p is, modulo GRH, *equivalent* to ES for large p; unconditionally it is equivalent to ES outside
the Linnik set {n₂(p) > (log p)^A}. Any proof of F at that reach is a pointwise ES theorem on the generic part of the
primes. This is why the brief asks also for (i) a reach for "all p outside a power-small set", (ii) weaker pointwise
inputs that still feed Linnik (§5 below gives one: a *majority* of q suffices), and (iii) quantitative versions of the
gates.

### 1.2 Which gate each item attacks, and the door

* Item 1 (windows): G4 directly (per-window failure), then G2 (joint loss). Door: none new — the window mechanism is
  CAP_POINTWISE Thm 1.1; what is new is the exact failure law (§§2–3) and its interaction with G2 (§4).
* Item 2 (reach): G3. The reach is a *counterfactual* (profinite) statement: "every non-residue class of p mod q, with
  p's residues at all moduli prime to q kept, carries a certificate". It implies F at q, is not implied by ES, and its
  failure set is a congruence-avoidance set with supply ≍ (log p)³/q per class (§6). Door used by Linnik: primality of
  the exceptional moduli (z50 B §4.2; outside the CRT caps).
* Item 3 (lines): G3 at fixed q = 17; finite coverings are dead there in the (J)70/MORDELL17 sense, so only
  p-dependent (non-congruence) data can help (§7).

Controls run on every mechanism below: odd squares (no windows exist at squares, CAP_POINTWISE Cor 1.2), numerator 8
at n = 17, 241, and the hard primes 193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281.

## 2. The window and a sharp deterministic covering lemma (gate G4)

(pending)

## 3. Per-window failure: the exact exponent for fixed q, and G4

(pending)

## 4. Many windows: what joint bounds can and cannot give (gate G2)

(pending)

## 5. Robust Linnik confinement

(pending)

## 6. Full Type I/II forcing reach (work item 2)

(pending)

## 7. Least-QNR lines (work item 3)

(pending)

## 8. Hostile reviews

(pending)

## 9. Remaining gap

(pending)
