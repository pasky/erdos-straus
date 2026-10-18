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
