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

### Lemma 3.1 (event classes are Jacobi non-residues) — SOUND

*Re-derivation.* (a) `gcd(M,4A)=1` since `M=4A−1`; D|A² so ℓ∤2D; `−4D=−d·(2·□)²`.
(b) `(−d|M)=(−1|M)(d|M)=−(d|M)`; each p|d has `v_p(D)` odd ⇒ p|A ⇒ `M≡−1 (p)`;
odd p: reciprocity with `(M−1)/2` odd gives `(p|M)=(−1|p)(−1)^{(p−1)/2}=1`;
p=2: 2|A ⇒ M≡7 (8) ⇒ `(2|M)=1`. Correct, incl. prime powers (Jacobi is
multiplicative in M, `(r|ℓ^v)=(r|ℓ)^v=1` for r a square mod ℓ) and ℓ=3 (squares
mod 3 = {1}; 3|M forces 3∤A, nothing special). The "more generally" clause is also
right: if `a_ℓ≥1` at every ℓ|M (even with `v_ℓ(M)>a_ℓ`), consistency would need
`−4D≡r` to be a square mod every ℓ|M, giving `(−4D|M)=+1`. ℓ=2 is irrelevant (M odd).

*Brute force* (`scripts/review_o13a_jacobi.py 3000 100000`), three independent checks:
1. Direct enumeration of `x² mod M` (no symbols): for all 15 754 atoms with
   M≤3000, `−4D` is never a square mod M; (a) via Euler's criterion: 0 failures.
2. Own Jacobi implementation: `(−4D|M)=−1` on all 1 070 466 atoms with M≤10⁵.
3. Square-class states: 3 000 random `Q=∏ℓ^{a_ℓ}` over ℓ≤23 with `a_ℓ≤4`, r a random
   CRT of unit squares mod `ℓ^{a_ℓ}`; 462 418 (atom with M|Q, state) pairs; fired: 0.

*Consequence check (the logic "random square classes never fire").* Under the
process, at every ℓ with `a_ℓ≥1` the fibre is a class mod `ℓ^{a_ℓ}` that is a square
(a=0 step picks a square mod ℓ; later lifts of a unit square mod ℓ are squares mod
ℓ^{a}, ℓ odd). So the realised r is a unit square mod every odd prime of Q, and every
atom with `rad(M)|Q` is dead. An event with `supp_end E=∅` is exactly such an atom
(`a_ℓ≥v_ℓ(M)≥1` at all ℓ|M). Hence no surviving event has empty support, which is
the only use made in Thm 3.4 / Lemma 1.1. SOUND.

