# y1_gamma8_trace — words as hyperbolic classes: the sign is a Γ(8)-class function, the ES content is the length-3 extraction (O209)

## Idea (brief item (a))
Each word gives M_w = S_v S_t S_u = [[n, −A*], [A, −t]] ∈ SL₂(ℤ) (S_x = [[x, −1], [1, 0]]), trace T = tuv − t − u − v
(cyclically symmetric), fixed-point form f_w = [A, −(n + t), A*] of discriminant T² − 4 (GROWING_IDENTITIES Lemma 1.1,
bsA_fricke_vieta F3: the cyclic word is the Zagier minus-CF cycle of [M_w]). Question: is N₋(n) a *twisted count of
hyperbolic classes*, so that a twisted Selberg/Eichler–Selberg trace formula (Sarnak's Σ h(t² − 4) family) gives an
exact formula with T1 = "a genus character becoming principal at squares"?

**Fact G1 (PROVED; finite cell check).** χ(w) is a function of M_w mod 8: there is f: SL₂(ℤ/8) → {±1} with
χ(w) = f(M_w mod 8) for every word of odd n (gcd(A, n) = 1 always). Hence χ is a **Γ(8)-class function** (conjugation by
Γ(8) does not change M mod 8). *Proof.* χ is a cell function of (t, u, v) mod 8 (CHI_FLIP Cor 1.2); the map cell ↦ M mod 8 is
finite, and `scripts/y1_matrix_mod.py` checks that cells with equal M mod 8 have equal χ (all cells occur for letters < 48;
236 keys, 0 clashes). Mod 4 is not enough (6 480 clashes).
**Fact G2 (PROVED, explicit).** χ is **not** an SL₂(ℤ)-class function: M_{(1,3,3)} (n = 3, χ = +1) and M_{(3,3,1)} (n = 5,
χ = −1) are conjugate (rotation of the cyclic word); 88 such pairs with non-square n among letters ≤ 11 (CHI_FLIP's rotation
law). So no character/representation of SL₂(ℤ) and no function of the SL₂(ℤ)-class (trace, length, genus of f_w, linking
number with the trefoil) can be the sign. Γ(8) is the coarsest natural level.
**Fact G3 (the sign is the genus character at n of the *definite* partner; PROVED).** With T_w = [[A*, 1], [1, A]] (disc
−4tn), for each odd prime ℓ | n the assigned character χ_ℓ(T_w) = (A/ℓ) (T_w represents A, ℓ ∤ A) is a genus character of
T_w, and χ(w) = (−1/n)·Π_{ℓ | n} χ_ℓ(T_w)^{v_ℓ(n)} (for n squarefree this is the genus character χ_{n*}, n* = (−1)^{(n−1)/2}n).
At n = m² every exponent is even and (−1/n) = 1: the product is principal — T1 is exactly "the genus character becomes
principal at squares" (cf. GROWING_IDENTITIES (J)10 for the Type I version).

## Literature
Sarnak, *Class numbers of indefinite binary quadratic forms*, J. Number Theory 15 (1982) (Σ_{t ≤ x} h(t² − 4) log ε ~ x²/2
via prime geodesics); Zagier, *Zetafunktionen und quadratische Körper* (1981) (minus-CF reduction); Hejhal, Selberg trace
formula Vol. 2 (twisted by finite-image representations of Γ); Ghys, *Knots and dynamics* (ICM 2006) (Rademacher function
= linking number); Kohnen–Zagier / Zagier, *Nombres de classes et formes modulaires de poids 3/2* (1975) (genus-twisted
class number sums); Kronecker's genus-character formula (Σ_Q χ_{d₁}(Q) ↔ L(χ_{d₁})L(χ_{d₂})).

## Barrier screen
* A Γ(8)-twisted trace formula evaluates Σ_{[γ]_{Γ(8)}, tr γ = T} f(γ mod 8)·(weights) — a twisted Hurwitz/Sarnak
  class-number sum of size T^{1+o(1)} — over **all** classes of trace T. The words are only the classes whose Zagier cycle
  has **three letters** with a **marked letter** t (n = T + t): #(length-3 classes of trace T) ≤ #{(a, b, c) : abc − a − b − c = T}
  = T^{o(1)}. So the ES count is a fraction T^{−1+o(1)} of the trace-formula count, extracted by a non-spectral
  condition (cycle length = number of cusp excursions; Zagier's cycle length is not a spectral invariant). **B3** in
  trace-formula form: the sign layer is visible (Γ(8)), the size layer is the extraction.
* Twisted *full* sums are positive and exact (Kronecker: Σ over all classes of disc −4tn of χ_{n*} is an L-value product),
  but the family F_t(n) = {T_w} is a divisor-in-class subset (T_w ≡ −(x − y)² mod t): **B2**.
* T1: respected by G3 (principal at squares). Thm 2.2 (O205): any generating function in n is non-holomorphic; a sum over
  t of twisted trace formulas is "growing level" (H-A).

## Cheap numerics
`scripts/y1_matrix_mod.py`: keys/clashes for N = 4, 8, 16, 32 (30/6480, 236/0, 1880/0, 15024/0); 88 conjugate pairs with
opposite χ.

## Assessment
PROVED small facts (G1–G3); negative for (a) as posed: the sign *is* a Γ(8)-class function and a genus character, so a
twisted trace formula can carry it, but it cannot select three-letter cycles. Promise 1/5.
