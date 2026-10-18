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
