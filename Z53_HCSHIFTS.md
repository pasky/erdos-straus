# Z53_HCSHIFTS — the one-coordinate polylog target HC(p) ≪ (log p)^A: growing-window kills, anatomy of shifted families

**ES is open. Nothing here proves or disproves ES, ES₅, (★), or HC(p) ≪ (log p)^A.** Labels: PROVED / CONDITIONAL
(on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Lane z53 HCSHIFTS (FRONTIER §7.2).
Scripts `scripts/z53_hcshifts_*`, data `data/z53/hcshifts/`.

*Status: CHECKPOINT 1 (skeleton; statements and first results; proofs and numerics being completed).*

## 0. Objects and the precise statements attacked

For a prime p ≡ 1 (mod 8) let 𝒞 = 𝒞_p = {x ≥ 4 : 4 | x or x ≡ 7 (mod 8)} and, for x ∈ 𝒞, the two **lines**
  N_x^e := p + x (endpoint line),  N_x^l := xp + 1 (level line).
Line x **fires** if N_x^e or N_x^l has a divisor d ≡ −1 (mod x). By LOWERTAIL_ROUND2_FABLE Thm 1 / Cor 1.1 (PROVED there),
a firing line is exactly a five-slice certificate word with a coordinate equal to x, and
  **HC(p) = min{x ∈ 𝒞 : line x fires}**, ES₅(p) ⟺ HC(p) < ∞.
(For p ≡ 5 (8), HC(p) = 3 always; only p ≡ 1 (8) is at issue.) Census: HC ≤ 64 for p ≤ 10⁸ (z49, CERTIFIED there).

**Target T (FRONTIER §7.2; OPEN).** ∃ A: HC(p) ≤ (log p)^A for all large primes p ≡ 1 (mod 8).

Sub-statements attacked in this lane:
* **(Q1) How far does the Dickson/H kill (LOWERTAIL_ROUND2_FABLE Prop 3.3) extend in X = X(p)?** Formalised as: for which
  functions X(p) can a Hypothesis-H / Theorem-M certified family of primes have HC(p) > X(p)?
* **(Q2) Anatomy of the shifted family {N_x^e, N_x^l : x ∈ 𝒞 ∩ [4, X]} at one p:** what is forced, what is congruence data,
  what is private; can the forced structure produce a firing line?
* **(Q3) Numerics:** HC(p) and the congruence-type vs private-type certificate rates at hard primes and samples to 10¹³.

**Why this is not already closed.** The closed items are: fixed root sets / bounded windows (Dickson, fixed X), the
least-non-residue root, the principal Pell-cycle menu, two-endpoint polylog windows (H4_NOT_POLYLOG, unconditional), and
everything in FRONTIER §6. T is one-coordinate: the other coordinate (the divisor d and its cofactor) is free, so
H4_NOT_POLYLOG does not apply, and the Dickson kill of Prop 3.3 is for fixed X only. Q1 asks exactly whether the fixed-X
kill extends to growing X; Q2/Q3 ask what a proof of T would have to use.

## 1. First results (checkpoint)

**Certificate types.** For a firing line with integer N, divisor d ≡ −1 (mod x) and threshold y, write N = s·r with s the
y-smooth and r the y-rough part. The certificate is **congruence-type (w.r.t. y)** if gcd(d, r) ∈ {1, r} (the rough part is
not split, so d mod x is a function of p modulo a y-smooth modulus), and **private-type** otherwise (d splits r: at least
two prime factors > y, on both sides). Privacy (SYNTHESIS_SPARKS8 Lemma 2.3): gcd(p+x, p+x′) | x − x′,
gcd(xp+1, x′p+1) | x − x′, gcd(p+x, x′p+1) | xx′ − 1, so a prime ℓ > X² divides at most one of the window integers.

**Theorem W (Dickson/Theorem-M wall; PROVED, elementary — proof in §2).** In any Dickson-certified (more generally
Theorem-M-certified) family of primes p ≡ 1 (8) on which every line x ∈ 𝒞 ∩ [4, X] is certified not to fire, p mod ℓ is
constant along the family for every odd prime ℓ ≤ ⌊X/4⌋ + 1. Hence all but one member satisfy
p > ∏_{3 ≤ ℓ ≤ X/4+1} ℓ = e^{(1/4+o(1))X}, i.e. **X < (4 + o(1)) log p: no H/Dickson-type kill reaches X(p) ≥ (4+ε) log p.**

**Proposition W3 (congruence-type certificates die at X ≍ log p; PROVED rel. Linnik's theorem).** There are infinitely
many primes p ≡ 1 (8) such that, with X ≥ (1/10 − o(1)) log p (≥ (1/4 − o(1)) log p under GRH), every certificate with a
coordinate x ≤ X (both lines) is private-type w.r.t. y = X + 1: it divides the (X+1)-rough part r_x ≥ 2 primes nontrivially.

**First falsifier (Q3; CERTIFIED computation, `scripts/z53_hcshifts_hc.c`).** Could the HC-certificates at hard primes come
from smooth parts only? Samples of 300 000–600 000 consecutive primes p ≡ 1 (8) from 10⁹, 10¹⁰, …, 10¹³ (all lines to 256):
at HC ≥ 12 the HC-certificate is private-type w.r.t. the privacy threshold y = 4096 = 64² in 5.4 %, 9.0 %, 15.4 %, 14.5 %,
18.0 % of cases (rising with p), and private-type w.r.t. y = x in ≥ 85 %. Status: the smooth-part-only route does not
survive at hard primes as p grows (EVIDENCE), consistent with Prop W3.

**Assessment (to be developed, §4): in the independent-anatomy (Kubilius) model the extremal HC is (log p)^{2 log 2 + o(1)},
not O(log p).** The kill mechanisms that can be certified stop at ≍ log p / log log p; the model's extra range comes from
"lightly hit" lines x ≍ (log p)^{κ log 2}, 1 < κ ≤ 2, which miss simply because N_x has fewer than φ(x) divisors.
