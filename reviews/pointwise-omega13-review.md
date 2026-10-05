# Hostile review R48a of POINTWISE_OMEGA13.md (reviewer 1 of 2: quarantine machinery)

Reviewer branch: side-agent/review-omega13a (merged side-agent/beyond-fifth @ 4539218).
Scope: Lemma 1.1, Lemma 3.1, Lemma 3.2, the random-vs-deterministic logic of Thm 3.4.
Lemma 3.3 (NT inputs, Ξ) is reviewer 2's scope; only touched where it interfaces.
Scripts: `scripts/review_o13a_*.py` (from scratch; author's scripts not reused).

## Summary verdicts

(filled in claim by claim below)

## Claim-by-claim

### Lemma 1.1 (β-weighted LLL) — SOUND

*Re-derivation.* Dependency graph = "supports meet" (valid on a product space: E is
mutually independent of the σ-algebra of the coordinates outside supp E). For E'∼E
(including E'=E) we have `Σ_{E'∼E}x_{E'} ≤ Σ_{ℓ∈supp E}w̃_ℓ ≤ s(E)η`; each
`x_{E'} ≤ η ≤ 1/4` (needs `logβ≤1/3`, which is assumed), and
`−log(1−x)≤(4/3)x` on `[0,1/4]`. So `∏_{E'∼E}(1−x_{E'}) ≥ β^{−s(E)}` and
`P(E)=x_Eβ^{−s(E)}` gives the asymmetric-LLL hypothesis (even with E itself in the
product, which is stronger than needed). Both conclusions are the standard
Erdős–Lovász/Spencer ones. Checked the inequalities line by line; no hidden
hypothesis other than finiteness of the family (true: M≤T) and `supp E≠∅` (events
with empty support must be dead — this is exactly what Lemma 3.1 supplies in §3).

*Brute force* (`scripts/review_o13a_lll.py`, seeds 1,2): random product spaces with
3–6 coordinates, non-uniform marginals, events with 1–3-coordinate supports and 1–3
accepted tuples, β∈(e^{0.02},e^{1/3}); plus adversarial hill-climbing that adds or
replaces events while keeping (1.1), maximising the violation ratio. 4 844 valid
systems, exact enumeration:
`max exp(−(4/3)Σx)/P(∩Ē) = 0.99889` and `max P(E|∩_𝒮F̄)/x_E = 0.942` (claims ≤1).
No violation. (Ratios near 1 come from near-empty systems, where both sides →1.)

