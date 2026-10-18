# EXP_15 — exponential-family forced budgets: two-base Pierpont boundary (F2) and 15·2^s + 1 (F1) (task O270)

Status: O270 in progress. **ES is not solved here.** Every theorem below is about a thin family. Labels as in DISCOVERIES.md.
Scripts `scripts/z40_*`, memos `BRAINSTORM/z40_*.md`. Source: board memo /home/pasky/.pi/boards/20261018-es-routes/memo.md (F1, F2).

## 0. Iteration log
(I1) F2 as posed ("do the (J)74/(J)75 windows for 3·2^s + 1 survive X ↦ 2^t3^{t′} on n = 8X^D + 1") conflates two
boundary points of the Pierpont family P = {2^a3^b + 1}. The {2,3}-unit-square points of P (limit value a unit square
at every place ≠ 2, 3, limit 1 at 2 and 3) are (a, b) → (0, 1) (limit 4) and (a, b) → (3, 0) (limit 9) (board: argon,
astra, fable; elementary). The (J)74 window lives at (0, 1), not (3, 0): n = 48X⁴ + 1 is the b ≡ 1 (mod 4) slice.
At (3, 0) the polynomial is 8X^D + 1, which is *reducible* for 3 | D ((2X)³ + 1). So the two boundary points behave
differently, and both answers are elementary (§1). The substantive question becomes: is there a finite certificate
for **all** 2^a3^b + 1 (a genuinely two-base family theorem)? (§1.3, computation.)

## 1. F2: the Pierpont family 2^a3^b + 1

**Lemma 1.1 ((0,1): the (J)74 window is base-free; PROVED, = MENU_STERILITY Theorem B/C read literally).** Theorem B
and the eight window rules of Theorem C(a) are polynomial identities in X with n = 48X⁴ + 1, valid (integral, positive)
for **every integer** X > 0 in the stated class X mod 11; no 2-adic condition is used (the forced budget is the
Aurifeuillean factorisation 4X⁴ + 1 = (2X² + 2X + 1)(2X² − 2X + 1), which is identical in X). Hence for X = 2^t3^{t′}
(t, t′ ≥ 0), i.e. n = 2^{4t+4}3^{4t′+1} + 1, ES holds whenever X ≢ 0, ±1 (mod 11), with the same budget. The window
classes X ≡ 2, 3, …, 9 (mod 11) are exactly the eight classes of Theorem C(a) (for X = 2^j these are j ≡ 1,…,9 except
j ≡ 0, 5 (mod 10)). So the answer to F2 at (0, 1) is "yes, trivially": the window is a statement about X, not about
how X is generated. *Proof.* Theorem B/C(a) as cited; re-verified in `scripts/z40_pierpont_check.py` (§1.3).

**Lemma 1.2 ((3,0): cyclotomic descent; PROVED, elementary).** If an odd prime p divides gcd(a, b) (a, b ≥ 0, not both
0), then Z := 2^{a/p}3^{b/p} gives 2^a3^b + 1 = Z^p + 1 = (Z + 1)(Z^{p−1} − … + 1) with 3 ≤ Z + 1 < n, and
4/(Z + 1) = 1/x + 1/y + 1/z implies 4/n = 1/(xr) + 1/(yr) + 1/(zr), r = n/(Z + 1). The neighbourhoods
{a ≡ 3, b ≡ 0 (mod L)} of (3, 0) with 3 | L lie in {3 | a, 3 | b}. So **the (3, 0) point is dissolved by an algebraic
factor of n itself** (8X³ + 1 = (2X + 1)(4X² − 2X + 1)), reducing to the smaller Pierpont number 2^{a/3}3^{b/3} + 1.
No window and no forced budget is needed; the 1D analogue of this is impossible for 15·2^s + 1 because 15Y^D + 1 is
irreducible for every D (Capelli). *Proof.* As stated. ∎

*Reading.* F2's either/or does not occur: there is neither a two-base obstruction nor a new identity; both boundary
points are handled by things that already ignore the base (a window polynomial in X at (0,1), reducibility of n at (3,0)).
The remaining question is a covering one (§1.3).

**1.3 Is there a finite certificate for all 2^a3^b + 1? (EVIDENCE; `scripts/z40_pierpont_cover.py`, `scripts/z40_tree2d.py`).**
Setting: cells (a mod L, b mod L), a, b ≥ A0; tools: Lemma 1.2 descent (odd p | gcd), Lemma 1.1 windows (X ≢ 0, ±1 mod 11),
divisor classes q | n and ET classes mod M = 2^u3^vM′ (ord_q 2, ord_q 3 | L for q | M′, M ≤ Mmax), and optionally (`--win`)
the general 2D window rules m = 2^i3^j w^e − 1 (e ∈ {1, 3, 5, 7} cyclotomic, or Sophie-Germain 2^a3^b = 4·2^i3^jZ⁴), Lemma-1.1
splitting with atoms 2, 3 and the algebraic factors of Z^e + w^e (resp. 2Z² ± 2Zw + w²).
* L = 120, M ≤ 3000: 21 of 14400 cells open (density 1.5·10⁻³). Tree 120 → 360 → 2520 → 5040 → 10080 → 20160 (M ≤ 3·10⁴,
  windows on): open density 5.4·10⁻⁵, 3.2·10⁻⁶, 1.3·10⁻⁶, 1.3·10⁻⁶, 1.2·10⁻⁶ (496 open cells at L = 20160). Lifting by 11 and 13
  instead (no windows): 1.9·10⁻⁷, 1.7·10⁻⁸, but the open *count* grows (51 → 596 → 8800), i.e. the tree is not closing at
  this supply.
* No sterile point is detected: at L = 5040 and at L = 20160 **every** open cell is a quadratic non-residue modulo some
  admissible prime q (97, 113, 127, 193, 211, …), so the limit of each open cell is not a profinite unit square at that
  level. The open cells are a *supply* problem (no ET class of modulus ≤ Mmax realises that non-residue jointly with the
  2-, 3-adic data), not an obstruction. Only 7 of the 47 open cells at L = 5040 still mimic 289 = 2⁵3² + 1 at level 360
  (the EXPONENT_COVERING §4.3 near-square phenomenon); none at level 5040.
* So: a finite certificate for all Pierpont numbers is NOT FOUND at this supply (non-discovery, not non-existence). By
  EXPONENT_COVERING Thm 1.4 / §5.1 (S-unit version) together with Lemmas 1.1–1.2 it exists iff the closure of
  {(a, b)} minus the neighbourhoods of (0, 1) and (3, 0) avoids the sterile set S′ — an exponential local–global question
  of (EH) type in two exponents; no 2D obstruction is known.

## 2. F1 gate: the binomial menus at μ = 0 of 15·2^s + 1

Notation as in EXP_OPEN §1–2: n = 15Y^D + 1, Y = 2^{s/D}, μ = 0 the profinite unit-square point (n → 16 at odd places,
n → 1 at 2); a *family* is a choice of the ET parameters as ℚ-polynomials in Y, integer-valued and positive on a
neighbourhood C = {s ≡ 0 (mod L), s ≥ s₀} of μ = 0. MENU_LADDER Lemma 2.1: R ∈ ℚ[Y] is integer-valued on a (smaller)
such C iff R(1) ∈ ℤ[1/2] and R(0) ∈ ℤ_(2).

### 2.1 Menu II-ad (a, d constant)

Type II: (x, y, z) = (abd, acdn, bcdn), cn = 4abcd − a − b. With f := 4abd − n (the gap 4x − n) and f′ := 4acd − 1,
(4abd − n)(4acd − 1) = 4ad(4abcd − b − cn) + n, so the identity is **f·f′ = B := n + 4a²d = 15Y^D + K, K = 1 + 4a²d**.

**Lemma 2.1 (limit conditions for II-ad; PROVED).** A II-ad family through μ = 0 with f, f′ non-constant exists only if
(C1) K = 15u^p for an integer u ≥ 3 and an odd prime p | D; then u ≡ 3 (mod 4);
(C2) X := f(1), X′ := f′(1) are positive integers with XX′ = B(1) = 16 + 4a²d = 15(1 + u^p) and
     X ≡ −16, X′ ≡ −1 (mod q), q := odd part of a·d (prime powers included);
(C3) f(0), f′(0) ∈ ℤ_(2) with f(0) ≡ f′(0) ≡ −1 (mod 2^{2+v₂(a)+v₂(d)}).
(If f is constant the family has constant gap and dies by EXP_OPEN Theorem W; if f′ is constant, c is constant and
b = (cn + a)/f′ is an ET class polynomial in n, which cannot contain a neighbourhood of the unit-square point μ = 0
(EXPONENT_COVERING Thm 1.4/Cor 1.5).)
*Proof.* B = f·f′ with both factors non-constant, so B is reducible over ℚ. Capelli: 15(Y^D − c), c = −K/15 < 0, is
reducible iff c ∈ ℚ^p for a prime p | D (p = 2 impossible, c < 0) or 4 | D and c ∈ −4ℚ⁴ (impossible: K is odd). So
K/15 = u^p, u ∈ ℚ_{>0}; writing u = r/s in lowest terms, Ks^p = 15r^p forces s^p | 15, s = 1 (p ≥ 3). K ≡ 1 (mod 4)
gives −u^p ≡ 1, u ≡ 3 (mod 4). (C2): positivity gives f, f′ > 0 for large Y, so both have positive leading
coefficient; B has no root in [0, ∞), hence neither factor has, so X, X′ > 0. X ∈ ℤ[1/2] (Lemma 2.1 for b = (f + n)/4ad);
f(0) ∈ ℤ_(2), and f = κP with P monic, whose roots are roots of B, i.e. 2-adic units (K, 15 odd), so
v₂(P(1)/P(0)) = Σ v₂(1 − α) ≥ 0 and X ∈ ℤ_(2); so X ∈ ℤ, likewise X′. For an odd prime ℓ | ad, ℓ-adic continuity of
b = (f + n)/(4ad) and c = (f′ + 1)/(4ad) at Y → 1 (along s → 0 in Ẑ; ℓ^v ℤ_ℓ is closed) gives
ℓ^{v_ℓ(ad)} | X + 16 and | X′ + 1. (C3) is the same at the 2-adic limit Y → 0 (n → 1). ∎
(C1)–(C3) are also sufficient for validity on a smaller neighbourhood (Lemma 2.1 of MENU_LADDER), given the factor shape.

**Theorem 2.2 (the u ≡ 3 (mod 8) branch is sterile for every root degree and every factorisation; PROVED).**
Every II-ad family through μ = 0 of 15·2^s + 1 has **u ≡ 7 (mod 8)**, equivalently a or d even.
*Proof.* u^p ≡ u (mod 8) (u odd, p odd), so 4a²d = 15u^p − 1 ≡ −u − 1 (mod 8). If u ≡ 3 (mod 8) this is ≡ 4, so a and d
are odd and q = ad. By (C2), X = m₁ad − 16 and X′ = m₂ad − 1 with integers m₁, m₂ ≥ 1, and expanding
(m₁ad − 16)(m₂ad − 1) = 16 + 4a²d gives the boxed equation
  **a(m₁m₂d − 4) = m₁ + 16m₂.**
Lemma 2.2′ below: it has exactly 39 solutions, all with d ≤ 21, a ≤ 81, m₁ ≤ 36; for none is 4a²d + 1 = 15u^p (only
(a, d) = (1, 11) has 15 | 4a²d + 1, quotient 3, not a p-th power). So (C1) fails. ∎
This uses neither D nor the shape of the factorisation of Y^D + u^p — only the values X, X′ at Y = 1. So **argon's
round-4 argument via P₀(Y^{2^r}) is not needed**, and it is in fact false:

**Remark 2.3 (argon's P₀(Y^{2^r}) claim; REFUTED).** Claim: for D = e·2^r every factor of Y^D + u^e is P₀(Y^{2^r}) with
P₀ | Z^e + u^e, so the pairs (P(0), P(1)) are those of degree e. Counterexample: Y⁶ + 27 = (Y² + 3)(Y² + 3Y + 3)(Y² − 3Y + 3)
(sympy factor_list; by hand Y⁴ − 3Y² + 9 = (Y² + 3)² − (3Y)²). The pairs (P(0), P(1)) = (3, 7), (3, 1) are new.
(This is astra's (a, d) = (1, 101), D = 6 example, u = 3 ≡ 3 (mod 8), so Theorem 2.2 kills it anyway.) The splitting
happens because −3 is a square in ℚ(ζ₃); in general Y^{2^r e} + u^e can split further than Z^e + u^e.

**Lemma 2.2′ (the boxed equation; PROVED, by hand + exhaustive check `scripts/z40_boxed.py`).** All solutions in positive
integers of a(m₁m₂d − 4) = m₁ + 16m₂ satisfy d ≤ 21, a ≤ 81, m₁ ≤ 36; there are exactly 39.
*Proof.* a ≥ 1 gives m₁m₂d ≤ m₁ + 16m₂ + 4, so d ≤ 1/m₂ + 16/m₁ + 4/(m₁m₂) ≤ 21, and (m₁ − 16)(m₂ − 1) ≤ 20. Hence
m₂ = 1, or m₁ ≤ 16, or (m₂ ≥ 2 and m₁ ≤ 36). If m₂ = 1: m₁(ad − 1) = 16 + 4a, ad = 1 is impossible, and ad ≥ 2 gives
m₁ ≤ (16 + 4a)/(2a − 1) ≤ 20 for a ≥ 1, d ≥ 2, resp. m₁ = 4 + 20/(a − 1) ≤ 24 for d = 1; then a(m₁d − 4) = m₁ + 16 ≤ 40
forces m₁d ≥ 5 and a ≤ 40. Otherwise m₁ ≤ 36 and m₂(am₁d − 16) = m₁ + 4a: if m₁d ≥ 5,
a ≤ (m₁ + 16)/(m₁d − 4) ≤ 52; if m₁d = 4, 4(a − 4)(m₂ − 1) = m₁ + 16 gives a ≤ 9; m₁d = 3: (3a − 16)(3m₂ − 4) = 3m₁ + 64
gives a ≤ 29; m₁d = 2: (a − 8)(2m₂ − 4) = m₁ + 32 gives a ≤ 42; m₁d = 1: (a − 16)(m₂ − 4) = 65 gives a ≤ 81. The script
enumerates a ≤ 500, d ≤ 100, m₁ ≤ 2000 (m₂ determined), asserts the bounds, finds 39 solutions (astra's count, reproduced
independently) and checks (C1) on each. ∎

**2.4 The u ≡ 7 (mod 8) branch (OPEN; reduction + EVIDENCE).** Here 4a²d = 2^E a₁²d₁ with E = 2 + 2v₂(a) + v₂(d) ≥ 3,
q = a₁d₁, and XX′ = N := 15(1 + u^p) = 16 + 2^E a₁²d₁ with X ≡ −16, X′ ≡ −1 (mod q).
* (2-adic bookkeeping, PROVED.) v₂(N) = v₂(1 + u) =: V ≥ 3, and comparing with 16 + 2^E a₁²d₁: E = 3 ⇔ V = 3; E = 4 ⇒ V ≥ 5;
  E ≥ 5 ⇒ V = 4 (u ≡ 15 mod 32). So E is unbounded only on u ≡ 15 (mod 32) with 15u^p ≡ 1 (mod 2^E).
* (Magnitude, PROVED.) If q ≥ 17 then (q − 16)(q − 1) ≤ N, i.e. a₁d₁ ≤ √(15(1 + u^p)) + 17, while a₁²d₁ = (15u^p − 1)/2^E.
  So a solution needs 15u^p − 1 to have a large "2^E·a₁²" part: 2^E a₁ ≳ √(15u^p) (or q ≤ 16). For a = 1 this is the
  2-adic approximation |15u^p − 1|₂ ≲ (15u^p)^{−1/2}, i.e. u is a very good 2-adic approximation of 15^{−1/p};
  Ridout's theorem makes this finite (ineffectively) for p ≥ 5, and nothing elementary bounds it for p = 3. For q ≤ 16
  the limit system (jq − 16)(j′q − 1) = N has solutions for every E (e.g. q = 1, j′ = 2), and (C1) becomes the
  S-unit-type equation 15u^p − 2^E c = 1, c = a₁²d₁ ≤ 256 — finite for each p (Thue), but not settled for all p here.
* (Factor shape for D = p, PROVED.) For D = p the factors of Y^p + u^p are Y + u and Φ = (Y^p + u^p)/(Y + u) (when Φ is
  irreducible), the roots −uζ (ζ ≠ 1) have v₂(1 + uζ) = 0, so v₂(X) ∈ {0, V}. Splittings for D = p·2^r (Remark 2.3) can
  produce other valuations.
* So **the u ≡ 7 (mod 8) branch is not closed**: closing it is an exponential-Diophantine problem (2-adic approximation
  of 15^{−1/p} by integers u, or S-unit equations 15u^p − c2^E = 1 for all p), which is exactly where the board's
  "CONDITIONAL" label stands. Argon's "u ≡ 7 is similarly bounded via EXP_OPEN Lemma 1.5" is unsupported: Lemma 1.5
  bounds a constant window m, here there is no constant window and E is unbounded at the limit level.
* EVIDENCE (`scripts/z40_iiad7.py 15 23 20000`, (C1)+(C2) only, all branches, all D): p = 3, u ≤ 2·10⁴; p = 5, u ≤ 380;
  p = 7, u ≤ 70; p ≤ 23 correspondingly (7414 tuples (u, p, a, d)): **no solution of (C1)+(C2)**. Positive control:
  `z40_iiad7.py 63 13 60` finds exactly (u, p, a, d, X, X′) = (3, 3, 5, 17, 21, 84) = EXP_OPEN Theorem 2.3.

### 2.5 Menus II-ac, I-ac, II-cd (status)
Not closed in this session. The same limit analysis applies (values at Y = 1, Y = 0; EXP_OPEN §2 table); e.g. for II-ac
with Capelli data a = c′(15u^p − v^p), c = c′v^p one gets 16c + a = 15c′(u^p + v^p) and the witness value X = f(1) must
satisfy 2^e·x ≡ −1 (mod odd(c′²v^p(15u^p − v^p))) with x | 15(u^p + v^p), e = v₂(X) ≤ v₂(u + v) (u, v odd): again
solvable only if 15u^p − v^p is abnormally 2-divisible, i.e. (v/u)^p is an exceptionally good 2-adic approximation of 15
(Assessment, same Ridout-type obstacle as §2.4). EVIDENCE for small parameters: EXP_OPEN Map 2.4 / Computation 2.2
(c′ ≤ 40, u, v ≤ 10, p ≤ 13): none. **W_binom remains CONDITIONAL** (board's label stands); the PROVED part is Theorem 2.2.

## 3. F1 construction: one-constant moving-gap families (menu II-d: d constant, a = a(Y))

The identity f·f′ = n + 4a²d of §2.1 holds verbatim with a ∈ ℚ[Y]; now c = (f′ + 1)/(4ad) ∈ ℚ[Y] forces a | f′ + 1, so
**f′(y₀) = −1 at every root y₀ of a** (and then f(y₀) = −n(y₀) automatically). At Y = 1 the conditions (C2) hold with
A := a(1) ∈ ℤ[1/2] in place of a, so for A, d odd the Y = 1 data are exactly the 39 boxed solutions (argon's "targets").

**Lemma 3.1 (even D; PROVED).** If D is even and d > 0 is constant, a has no real root. *Proof.* n > 0 on ℝ, so
B = n + 4a²d > 0 on ℝ. If a(y₀) = 0 (y₀ ∈ ℝ) then f′(y₀) = −1 < 0 while f′ has positive leading coefficient, so f′, hence
B, has a real root > y₀. ∎ So for even D the menu needs deg a ≥ 2 (no real roots); a linear is impossible. (This explains
the 0 algebraic configurations at D = 4, 6, 8 below.)

**Computation 3.2 (EVIDENCE; negative).**
* `scripts/z40_trinom.py c0 D 40 8 40` (a linear, a quadratic factor g of B with g = f′ or g = f, p, q ∈ ℚ of height
  ≤ 40 with denominators | 8, d = sqfree(δ)·t², t ≤ 40; exact Lemma-2.1 test): (15, 1), D = 3…8: 52/0/10/0/9/0 algebraic
  configurations, **0 valid families**; same for (3, 1) and (63, 1) (controls — no II-d family known there either).
* `scripts/z40_seeded.py c0 D boxed` (seeded by the 39 boxed solutions (A, d, X, X′); quadratic g interpolating
  (0, φ), (1, X′ or X), (y₀, −1 or −n(y₀)); g | B solved exactly by resultants): (15, 1), D = 3: 2 rational solutions
  (a = (Y + 1)/2, d = 3 and a = 3(Y + 1)/2, d = 5), both fail 2-adic integrality (a(0) = 1/2, 3/2). Larger D: see log
  `data/z40/seeded.log`.
