# Z54_HCWIN — the growing-window target HC(p) ≤ (log p)^A, A > 2 log 2: anatomy layer vs class layer (wave z54, lane HCWIN)

**ES is OPEN. Nothing here proves or disproves ES.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only. Scripts `scripts/z54_hcwin_*`, data `data/z54/hcwin/`.
Kickoff: `z52bbriefs/z54_lanes.md` §HCWIN (FRONTIER §7.2).

*Status: CHECKPOINT 1 skeleton (statements, why-open, first lemma + first falsifier). Proofs and numbers to be completed.*

## 1. Statements attacked

Notation as in `Z53_HCHYP.md` §1. p ≡ 1 (8) prime; 𝒞 = {x ≥ 4 : 4 | x or x ≡ 7 (8)}; for x ∈ 𝒞 the two *lines*
ι = (x, E), (x, L) have window integers N_ι = p + x, xp + 1 (coprime to x); G_x = (ℤ/x)^×; line ι *succeeds* iff N_ι has
a divisor d ≡ −1 (mod x); HC(p) = min{x : a line at x succeeds}.

**Target S_A (FRONTIER §7.2).** ∃ p₀ ∀ p > p₀ prime, p ≡ 1 (8): HC(p) ≤ (log p)^A, with A > 2 log 2.

Three per-line quantities (all computable from the factorisation of N_ι and x alone):
* τ(N_ι) (anatomy);
* the genus count g_ι := #{d | N_ι : d ∈ −G_x²} (quadratic layer; g_ι = 0 iff an odd real character mod x is trivial
  on every prime factor of N_ι — the T1/alignment confinement);
* the class count c_ι := #{d | N_ι : d ≡ −1 (mod x)} (success iff c_ι ≥ 1).

Window masses: **Λ(p, X) := Σ_{ι : x ≤ X} min(1, τ(N_ι)/φ(x))** (anatomy mass) and
**Γ(p, X) := Σ_{ι : x ≤ X} min(1, g_ι/|G_x²|)** (genus mass). In the uniform-residue model these are, up to a factor ≤ 2,
the expected number of successful lines given the anatomy (Lemma M1 of HCHYP).

Statements attacked:
* **(Q1) Origin of 2 log 2.** Identify the arithmetic statement behind the model exponent and prove what is provable.
  Target form: Anat(A, C): Λ(p, (log p)^A) ≥ C log p for all large p.
* **(Q2) Single-p anatomy.** Prove the part of Anat provable at one p (Turán–Kubilius over the window variable x).
* **(Q3) Class hypothesis.** Find the weakest clean hypothesis on the class layer and prove S_A conditional on it
  plus anatomy, with explicit A; decide whether a *per-line* class hypothesis can work.
* **(Q4) Numerics** at hard primes to 10¹³, with odd squares, near-squares and the §4 item-14 primes as controls.

## 2. Why this is not already closed

HCSHIFTS §3.2 and HCHYP Thm M derive 2 log 2 inside a model; neither identifies an *arithmetic* statement with that
threshold, nor separates the anatomy layer (τ of the window integers) from the class layer at one p. HCHYP's LT is a
joint lower-tail hypothesis on the *model* mass 𝓜 (a function of x only), i.e. anatomy and class are fused into one
far-tail assumption. HCHYP Cor M3/M4 block hypotheses that the model satisfies with positive probability (θ < 2 log 2)
or that are block-robust; they do not address (i) the decomposition "anatomy + per-line class", (ii) which part of the
anatomy is provable at a single p, (iii) a class hypothesis conditioned on the *actual* anatomy, which is pointwise and
numerically falsifiable.

## 3. First lemma and first falsifier (checkpoint)

**First lemma (Theorem C below; PROVED in the model 𝔐 of HCHYP §3.1).** The natural two-layer decomposition
"(ii) every large p has a line with τ(N_ι) ≥ K φ(x); (i) every such 'big' line succeeds" has 𝔐-probability 0, for every
fixed K and for every K = K(p) → ∞ with K ≤ (log p)^{1/2}, and at every window size (even X = ∞). So the class
hypothesis cannot be per-line; it must be a joint lottery over lines with individually small success probabilities.

**First falsifier (running).** For a conditioned class hypothesis Lot(C) ("Γ(p, X) ≥ C log p ⟹ HC(p) ≤ X"), measure the
largest Γ(p, X)/log p among primes with HC(p) > X, and the curve P(HC > X | Γ) against exp(−cΓ), at 10⁹, 10¹¹, 10¹³,
hard primes, near-squares, odd squares. Lot is dead at accessible scales if failures occur at Γ ≫ log p.
