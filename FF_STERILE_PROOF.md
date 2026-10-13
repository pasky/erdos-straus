# FF_STERILE_PROOF — towards an explicit sterile point of ES₃(T²) (O179, spark relay F)

Status: in progress (O179). Labels as in DISCOVERIES.md. **ES over Z is not touched; this is the F₃[T] model.**
Inputs (treated as CLAIMED, re-derived where used): FUNCTIONFIELD_ES3.md (O173), SIGNLAYER_DEEP.md (O175),
FUNCTIONFIELD_ES2.md (compactness criterion §0.1, Case A at x*_c §0.2). Scripts `scripts/fsp_*`.

## 0. Setting and notation

q = 3, A = T². Slice point x_u: x ≡ 1 at every prime ≠ T, x ≡ u (mod T^∞), u = 1 + Tv, v(0) = c ∈ {1, 2}
(u ≡ 1 mod T² is covered by the constant family E = −1, so these are the only interesting slice points).
x*_c: u = 1 + cT. By O175 Lemma 1.1 (re-derived in §1) the Case B families valid on the slice are the tuples
(H, H', g', L'', r, K) — H = h₁, H' = h₁' — with H, H', g', L'' monic, nonzero constant terms,
* (I) H + H' = T g' r, (II) H H' L'' = T^K + r, L' := g'L'', l := deg L', a := deg H, b := deg H', λ := deg L'',
and the family of level N (N − 1 ≤ K ≤ 2N − 2) covers the cylinder u ≡ 1 − T H L' (mod T^{N+1}).
E := T H L' − 1, E' := T H' L' − 1 (the two monic cofactors, E E' = D := 1 + T^{K+2} L' g').

Independent re-enumeration: `scripts/fsp_enum.py` (own arithmetic, checks (I), (II) explicitly, prints full
tuples) reproduces the O175 solution list (K, a, b, w) of `bsB_caseB.c` **exactly for K ≤ 14** (312 solutions).

## 1. Reformulations (PROVED, elementary)

**Lemma 1.1 (one-sided form).** (H, H', g', L'', r, K) is a solution iff E' := T H' g' L'' − 1 divides
T^K + H'² L'', with quotient r, and H := T g' r − H' is monic with H(0) ≠ 0. Symmetrically with H ↔ H'; so
E' r = T^K + H'² L'' and E r = T^K + H² L'' (same r).
*Proof.* If (I), (II) hold, E' r = T H' L' r − r = H' L''(H + H') − r = H H' L'' + H'² L'' − r = T^K + H'² L''.
Conversely if E' r = T^K + H'²L'' and H := Tg'r − H', then H H' L'' = H'L''(T g' r − H') = r(E' + 1) − H'²L''
= T^K + r, which is (II), and (I) holds by definition. ∎
**Lemma 1.2 (the covered cylinder is a rational approximation).** For a solution of level N,
u ≡ 1 − T H L' (mod T^{N+1}) ⟺ u ≡ −H/H' − [K + 1 = N]·T^N g'(0)/H'(0) (mod T^{N+1}); in particular the family
covers u only if **u ≡ −H/H' (mod T^N)**, and u^{−1} ≡ 1 − T H' L' (mod T^{N+1}).
*Proof.* H'·(1 − THL') = H' − T g'(T^K + r) = H' − (H + H') − T^{K+1} g' = −H − T^{K+1}g' by (I), (II); K + 1 ≥ N.
The last claim: (1 − THL')(1 − TH'L') = E E' = D ≡ 1 (mod T^{K+2}). ∎
So a covering family is a rational approximation −H/H' of u to T-adic order N whose numerator and denominator
almost divide T^K (∞-adic condition (II)), with a + b ≤ K ≤ 2N − 2: a *two-place* approximation problem.

## 2. The genus (sign-layer) constraint: degree parities (PROVED; checked on all 312 solutions K ≤ 14)

**Lemma 2.1.** On the slice (u(0) = 1), every Case B solution has **deg E and deg E' even and λ ≡ K (mod 2)**;
equivalently a ≡ b (mod 2), a + b ≡ 0, l ≡ a + 1 (mod 2).
*Proof.* D = 1 + T^{K+2} g'² L'' = 1 + M Y² with (M, Y) = (L'', T^{(K+2)/2} g') for K even, (T L'', T^{(K+1)/2} g')
for K odd. E | D and E ≡ −1 (mod T L'), so every prime π | E is prime to T M Y and −M ≡ Y^{−2} is a square mod π:
the Jacobi symbol (−M/E) = 1. In F₃[T], for monic coprime A, B: (A/B)(B/A) = (−1)^{deg A·deg B},
(−1/B) = (−1)^{deg B}, (B/T) = (B(0)/3). Since E ≡ −1 (mod L''), (E/L'') = (−1/L'') = (−1)^λ; and
(T/E) = (−1)^{deg E}(E(0)/3) = (−1)^{deg E + 1} as E(0) = −u(0) = −1.
K even: 1 = (−1/E)(L''/E) = (−1)^{deg E + λ deg E + λ}, i.e. (deg E + 1)(λ + 1) odd: deg E, λ even.
K odd: 1 = (−1/E)(T/E)(L''/E) = (−1)^{deg E + deg E + 1 + λ deg E + λ}, i.e. λ(deg E + 1) odd: λ odd, deg E even.
Same for E' (also E' ≡ −1 mod TL', E'(0) = −1). With deg E = 1 + a + l, deg E' = 1 + b + l, K = a + b + λ. ∎
Check (`fsp_enum.py 14`): parity classes (a, b, λ, K mod 2) of the 312 solutions: (0,0,0,0) 112, (1,1,0,0) 88,
(0,0,1,1) 84, (1,1,1,1) 28; no violation.
*Remark.* This is the full genus information: the local symbol at T of F₃(T)(√−M) only sees E(0) (1-units of
F₃[[T]] are squares, the group 1 + TF₃[[T]] being pro-3), so quadratic characters see **no** T-adic digit of u
beyond u(0). In particular no quadratic character (Legendre/genus) can split the slice into covered/uncovered
halves; a "hidden character" explaining the 1/2 would have to be cubic (Artin–Schreier) or non-abelian.

## 3. Where sterile points can live: π-weights, and O(q, A) is Haar-null (PROVED)

Families F = (E; t_a, a₀; t_b, b₀) as in FUNCTIONFIELD_ES §6.2 (a = a₀, P a₀, X/a₀, P X/a₀ for t = 0, 1, 2, 3;
X = (P + E)/A; valid iff A a₀, A b₀ | P + E, E | s := a + b, lc(s) = lc(E), s ≠ 0). For x ∈ R̂^* and a prime
ℓ | E (ℓ ∤ AL automatically, since E ≡ −x mod AL is a unit there) put π := x mod ℓ^{v_ℓ(E)}. Mod E,
P ≡ π, X ≡ π/A, so the four types are ≡ a₀·π^w / (A a₀)^{−1}·π^w with **π-weight w = 0, 1, 1, 2**.
**Lemma 3.1 (π-free families; PROVED).** If w(t_a) = w(t_b) — types {0,0}, {1,1}, {2,2}, {3,3} (E | a₀ + b₀ or
E | L/a₀ + L/b₀) and {1,2} (E | 1 + A a₀ b₀) — the condition E | s does not involve x mod E. In particular at
**every** x ∈ R̂^* the families (E; 1, a₀; 2, b₀) with E monic, E | D = 1 + A a₀ b₀, E ≡ −x (mod A·L) are valid:
the Case B system of the slice, with "E ≡ −1 mod L'" replaced by "E ≡ −x mod L'". If w(t_a) ≠ w(t_b) the
condition is x ≡ ρ_F (mod E) for an explicit ρ_F (e.g. types (0,2): x ≡ −A a₀ b₀ mod E).
*Proof.* Direct from the residues listed (for (1,2): π a₀ + π/(A b₀) = π(1 + A a₀ b₀)/(A b₀); for (0,2):
a₀ + π/(A b₀)). lc(s) = 1 for distinct types, so E is monic. ∎
On the slice (π = 1 at all ℓ) every family is π-free; this is why the slice makes validity deterministic.

**Theorem 3.2 (O(q, A) is Haar-null; PROVED).** For every odd or even q and monic A of positive degree, the
obstructed set O(q, A) = {x ∈ R̂^* : no linear family is valid at x} has Haar measure 0. In fact Haar-a.e. x is
covered by infinitely many families of the single shape F_ℓ = (ℓ; 0, 1; 2, 1), ℓ irreducible.
*Proof.* F_ℓ: a = 1, b = X, s = 1 + X. It is valid at x iff ℓ ≡ −x (mod A) and x ≡ −A (mod ℓ) (since
ℓ | 1 + X ⟺ P ≡ −A mod ℓ; lc(s) = lc(X) = 1 = lc ℓ; s ≠ 0). Fix the class κ = x mod A. Under Haar measure the
components of x at distinct primes are independent, so the events B_ℓ = {x ≡ −A mod ℓ}, ℓ ≡ −κ (mod A), ℓ ∤ A,
are independent given κ, with μ(B_ℓ) = 1/(|ℓ| − 1). By the prime number theorem in arithmetic progressions of
F_q[T], Σ_{deg ℓ = e, ℓ ≡ −κ (A)} 1/|ℓ| ~ 1/(Φ(A)·e), whose sum over e diverges. Borel–Cantelli II: a.s. infinitely
many B_ℓ hold, and each gives a valid F_ℓ. ∎
*Consequences.* (a) Settles the open alternative of FUNCTIONFIELD_ES2 §0.2 (R166 D11): O(3, T²) is null in R̂^*,
so the ≈ 1 % plateau of the `ffl_tree` covering tree is a truncation artefact, not a positive-measure obstruction.
(b) A sterile point must be **non-generic at almost all primes**: it must avoid x ≡ −A (mod ℓ) for all but
finitely many ℓ ≡ −x (mod A) — and likewise for every π-dependent family. Global points x ≡ θ (θ ∈ F_q(T)^*) at all
ℓ outside a finite set make every family π-free (conditions become E | a fixed polynomial); θ = 1 (the slice)
collapses the most type pairs (θ ≠ 1 adds E | a₀ + θb₀, E | Aa₀b₀ + θ, E | Aa₀b₀ + θ², …). So the slice is
the natural (not merely convenient) home of sterile points, and on it the problem is the deterministic
divisor lottery of §1. This is the function-field shadow of the integer picture: a prime p is "generic" in this
sense, ES holds for it by a small-E family, and the hard cases are the non-generic residue patterns.
