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
P ≡ π, X ≡ π/A, so the four types are ≡ a₀, a₀π, π/(A a₀), π²/(A a₀): **π-weight w = 0, 1, 1, 2**.
**Lemma 3.1 (π-free families; PROVED).** If w(t_a) = w(t_b) — types {0,0}, {1,1}, {2,2}, {3,3} (E | a₀ + b₀ or
E | L/a₀ + L/b₀) and {1,2} (E | 1 + A a₀ b₀) — the condition E | s does not involve x mod E. In particular at
**every** x ∈ R̂^* the families (E; 1, a₀; 2, b₀) with E monic, E | D = 1 + A a₀ b₀, E ≡ −x (mod A·L) are valid:
the Case B system of the slice, with "E ≡ −1 mod L'" replaced by "E ≡ −x mod L'". If w(t_a) ≠ w(t_b) the
condition is a polynomial congruence in x mod E: linear for weight difference 1 (e.g. types (0,2):
x ≡ −A a₀ b₀ mod E), quadratic for (0,3) (x² ≡ −A a₀ b₀ mod E: 0, 1 or several roots).
*Proof.* Direct from the residues listed (for (1,2): π a₀ + π/(A b₀) = π(1 + A a₀ b₀)/(A b₀); for (0,2):
a₀ + π/(A b₀)). lc(s) = 1 for distinct types, so E is monic. ∎
On the slice (π = 1 at all ℓ) every family is π-free; this is why the slice makes validity deterministic.

**Theorem 3.2 (O(q, A) is Haar-null; PROVED).** For every q and monic A of positive degree, the
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
(b) A sterile point must avoid **every** event x ≡ −A (mod ℓ), ℓ ≡ −x (mod A) prime, and the conditions of every
π-dependent family; Haar-generic points fail this (Thm 3.2 says nothing about which null sets hold sterile points). Global points x ≡ θ (θ ∈ F_q(T)^*) at all
ℓ outside a finite set make every family π-free (conditions become E | a fixed polynomial); θ = 1 (the slice)
collapses the most type pairs (θ ≠ 1 adds E | a₀ + θb₀, E | Aa₀b₀ + θ, E | Aa₀b₀ + θ², …). Assessment: the slice
is a natural home for sterile-point candidates, and on it the problem is the deterministic divisor lottery of §1;
other null sets are not excluded by anything proved here.

## 4. The point x*_c: what is proved, the exact residual problem, and a large-K cyclotomic search

**What is proved at x*_c (all PROVED; the first two are O173/O175 results re-derived, the third is new).**
(i) Case A is impossible (FUNCTIONFIELD_ES2 §0.2, R166 D1). (ii) Every Case B family covering x*_c is lopsided
(O175 Lemma 3.2) and has (N + 1)/4 ≤ l ≤ 2N − k − 1 (O173 Lemma 2.3). (iii) With Lemma 2.1:
deg E ≥ N + 1 and deg E' ≥ N + 1 — *Proof.* deg E ≤ N forces E = −(1 + cT) (degree 1, odd: Lemma 2.1). deg E' ≤ N
forces (1 + cT)E' + 1 = cT^{N+1}, i.e. E' = (cT^{N+1} − 1)/(1 + cT), which needs c(−c)^{N+1} = 1, i.e. c = 1 and
N odd, and then deg E' = N is odd (Lemma 2.1). ∎ (Weaker than O173's l ≥ (N+1)/4 in most ranges; recorded
because it is the genus lemma doing the work that the leading-coefficient sign does in Case A.)

**The residual problem (exact; PROVED reformulation).** By Lemma 1.1 and the identities above, x*_c is sterile iff
for no K ≥ 2 and no r with deg r < K is there an ordered factorisation T^K + r = H·H'·L'' into monic factors
with H + H' = T g' r (g' monic, g'(0) ≠ 0) and **H·g'L'' ≡ −c (mod T^{N₀})**, N₀ = ⌈K/2⌉ + 1 (the covering condition
v ≡ −HL' mod T^N at the weakest admissible N; it implies, but is not implied by, H + (1 + cT)H' ≡ 0 mod T^{N₀} — e.g.
K = 2, H = T + 2, H' = T + 1 satisfies the latter and covers 1 + T + 2T², not x*_1) — i.e. "T^K + r has a divisor
triple whose product HL' lies in a prescribed T-adic class of precision about half the degree": exactly the integer divisor-class problem B2 (a divisor of N_θ(p) in a residue
class whose modulus is part of the solution), with r playing the role of the moving modulus. The data of
§1–§2 and Lemma 2.1 cut the parameters but leave this lottery intact; I found no step that is false for all K.

**Cyclotomic sub-family (r constant) — structure (PROVED) and large-K search (EVIDENCE).** By Lemma 2.1,
deg r ≡ K (mod 2) (if a ≥ b, deg r = K − deg E'; if a < b, deg(T^K + H'²L'') = 2b + λ ≡ K), so r is constant
only for even K. Then H H' L'' = T^K + r₀ and every ordered 3-factor split of T^K + r₀ with H + H' = r₀ T g'
(g' monic, g'(0) ≠ 0) is a solution. These explain the count spikes (K = 12: 72 of 104 solutions, K = 16, …;
T^K − 1 highly factorable) and the dominant K = 2 cylinder (H = T ± c, HH' = T² − 1; it recurs for every even K
with L'' = (T^K − 1)/(T² − 1), inside the same cylinder). `scripts/fsp_cyclo.py` (sympy factorisation; checked
against `fsp_enum.py`: identical cyclotomic counts 2, 6, 8, 12, 4, 72, 4 for K = 2, …, 14) enumerates **all**
cyclotomic solutions for 15 ≤ K ≤ 149 except 47 pairs (K, r₀) (at 34 levels) with > 3·10⁵ splits, marked SKIP in
the log `data/fsp_cyclo_K15_150.txt`: **no enumerated cyclotomic solution covers x*_{±1}** (the test is exactly
v_T(HL' + c) ≥ N₀) (first time levels
K > 19 are touched at x*). Closest approach: v_T(HL' + c) = 12 against the needed 14 at K = 26 (a = b = 13, T^26 − 1);
elsewhere ≤ 13 against needed ≥ 72. Observed: T^K + 1 has cyclotomic solutions at K = 4, 12, 20, 28, 36, 40, 44, 52, …, 136, 148 (mostly K ≡ 4 mod 8,
not only).

## 5. The "covered measure → 1/2": what it is and what it is not

Exact covered slice measure (union of maximal cylinders v ≡ −HL' mod T^{N₀}, N₀ = max(2, ⌈K/2⌉ + 1), Haar on
v ∈ F₃[[T]]^*; recomputed from a fresh `bsB_caseB 19` run, agreeing with O175 and R175):
| K ≤ | 4 | 5 | 8 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| measure | 0.3333 | 0.4074 | 0.4568 | 0.4650 | 0.4705 | 0.4787 | 0.4806 | 0.4833 | 0.4851 | 0.4885 | 0.4890 | 0.4904 | 0.4906 |
* **Decomposition (exact).** 1/3 is the single K = 2 cyclotomic family (prefix v ≡ (c, 2)); K = 5 adds 2/27 (four
  depth-4 cylinders), K = 8 adds 4/81; everything after K = 8 adds 0.034 so far. Two-level increments
  0.0137, 0.0101, 0.0046, 0.0039, 0.0016 (K = 10–11, …, 18–19) decay with ratio ≈ 0.6 per two levels; geometric
  extrapolation gives a limit ≈ 0.493 (range 0.492–0.495 for ratios 0.5–0.7). Assessment (finite data +
  extrapolation, not a proof): **no sign of an exact 1/2**; "≈ 1/2" is 1/3 + 2/27 + 4/81 + (apparently small tail).
  C is the Case-B-covered set; its complement is sterile only where Case A is also excluded.
* **No quadratic group character produces it (PROVED).** 1 + T F₃[[T]] is pro-3, so it has no nontrivial ±1-valued
  group character (arbitrary continuous ±1-valued functions of higher digits are not excluded); the only such
  character of the slice is v(0) = c, and C is invariant under
  c ↦ −c (T ↦ −T; O175 Lemma 3.1(ii), whose sign bookkeeping is exactly Lemma 2.1 — this closes R175 D7).
  Cubic (Artin–Schreier) characters would give thirds, not halves.
* **A homeomorphism swapping covered/uncovered forces C clopen (PROVED, topology).** C is open, U closed, so
  τ(C) = U makes both clopen (C a finite union of cylinders). C has not stabilised through K = 19 (every increment for
  10 ≤ K ≤ 19 is > 0); whether it does later is open, so this only says what such a τ would require.
* Near x*_c coverage is zero up to the depth at which x*_c is known uncovered: a level-N family meeting
  {u ≡ 1 + cT mod T^{N+1}} covers x*_c itself (ultrametric triviality). This is all R175's "far below 49 %" says.

## 6. Why goal (1) is not reached: the square-root barrier for the slice (PROVED bounds; Assessment of scope)

A *sufficient* condition for a sterile point on the slice: for some finite K₀ the uncovered measure U(K₀) exceeds
the tail Σ_{K > K₀} #cyl(K)/(2·3^{N₀(K)−1}) (union bound; a sterile set could also be nonempty and null; Case A must also be excluded on the region used — proved only at x*_c, EVIDENCE elsewhere). U(19) = 0.5094, so a bound #sol(K) ≤ C·3^{(1/2−δ)K}
with explicit C, δ making the tail beyond a computed K₀ smaller than U(K₀) would finish the existence proof (data:
#sol(K) ≈ 3^{0.2K}, R175). The elementary parametrisations I found do not beat the square root: with ρ = deg r, a
solution is fixed by r and a divisor triple of T^K + r (≤ 3^{ρ + o(K)}), or by (H', g', L'') via Lemma 1.1
(≤ 3^{K − 1 − ρ}); at ρ ≈ K/2 both give 3^{K/2 + o(K)}, no decay against the cylinder mass ≈ 3^{−K/2}. Beating it needs an
equidistribution input for "T^K mod E' is a short polynomial" over the moving moduli E' = T H' L' − 1 — the
function-field face of B3, matching O173 §3. The off-slice escape (choose x at the primes of L' to gain 1/Φ(L')
rigorously) meets Theorem 3.2: at points that are random at the primes of L' the π-dependent families (whose E is unconstrained) make the first moment diverge (Assessment for partially random points; PROVED for Haar-random x).
