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
