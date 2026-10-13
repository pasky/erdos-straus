# AGENT REPORT O172 — Kudla program / incoherent Eisenstein series vs ES (checkpoint 1)

Branch `side-agent/kudla-incoherent`. Main file `KUDLA_ES.md` (§1–§3). Scripts `scripts/kud_typeI_diff.py`,
`scripts/kud_typeII_diff.py`, `scripts/kud_genus_majorant.py` (each < 1 min). **ES is not solved; no infinite case.**

## SHARP:
* **T1 = oddness of Kudla's Diff(T) (exact dictionary, PROVED, elementary, for all odd n).** Type I tuples
  (4abd = ne + 1, a + b = ce) give the genus-2 Fourier index `T(d,ab) = [[d,−1/2],[−1/2,ab]]` (det 2T = ne); Type II
  tuples give the Heegner Gram matrix `T' = [[f,1],[1,f']]` (ff' − 1 = 4c²dn, f ≡ f' ≡ −1 (4cd)). For Kudla's
  incoherent ternary collection of the modular curve, Diff(T) = Ram_fin(B_T) is odd, and the ES congruences
  (`e | a+b`, resp. `f ≡ −1 (4cd)`) are *exactly* what clear every place except the primes of n:
  `Diff = {ℓ | n : v_ℓ(n) odd, ℓ ∤ e, (−d/ℓ) = −1}` (I), `Diff = {ℓ | n : v_ℓ(n) odd, (−f/ℓ) = −1}` (II).
  Hence T1 (no tuples at odd squares) and, at n = p, Diff = {p}: certificates are supersingular points mod p of Z(T),
  i.e. lie in the support of E'(τ,0)'s T-th coefficient. Checked on all 882749 Type I and 336357 Type II tuples of all
  odd n ≤ 20000. Caveat: mathematically this is Hilbert reciprocity (same content as ET Prop 1.6 / GI Lemma 1.3); new
  is the dictionary, not new arithmetic. Note the Type II index is T', not the Gram e·T' of QUATERNION_ES's pair
  (2ai+j, 2bi−j) — the two algebras differ in ~half the cases.

## Results (KUDLA_ES.md)
* §1 Thm 1.2 / 1.4 (above). Lemma 1.1: det(2T) odd ⇒ 2 ∉ Diff for Type I.
* §2 Prop 2.1: positivity of the derivative coefficient is **automatic** at certificate indices — the open question
  is the *existence of an index*, which Kudla's identities (values at given indices) do not address.
* §2 Prop 2.2: the Kudla-support count `G_{c,d}(n) = #{f | 1+4c²dn : Diff(T'_f) ⊆ Odd(n)}` is a T1-respecting
  majorant of the Type II slice count (G = 0 at all odd squares by Diff-parity); it depends only on genus characters
  of f (and not on c at all). Numerics: primes < 3000, 35 slices: ES 5791 vs G 51591, 0 violations.
* §2 Prop 2.3 (PROVED rel. Dirichlet): Kudla-supported indices with Diff = {p} exist at every prime, deterministically
  (one Dirichlet prime q ≡ 3 (4) non-residue mod p, CRT choice of c). The incoherence layer is easy; ES is its
  ray-class upgrade `4c | q + 1` = the Type II divisor problem (B2).
* §2 Prop 2.4: Kudla coefficients are GL₂(ℤ)-class functions of T; the certificate property is a representative
  property ⇒ any identity ES = Σ w(T)E'_T has w = the certificate indicator (B2 in Kudla language).
* §3 Lemma 3.1: split discriminants admit no incoherent binary collection (binary form of T1). Construction log:
  (1) genus-2 Kudla → B2; (2) level structure/coset Schwartz functions → back to the split-plane divisor sum, which has
  no incoherent partner; (3) exact decomposition `ES = Q + R` with Q = quadratic-character (orthogonal Siegel–Weil /
  Kudla-visible) part = genus count/|(ℤ/M)^{×2}|, zero at squares, ≪ 1 per slice (B3), R = characters of order ≥ 3
  (no orthogonal Siegel–Weil incarnation); (4) base change to F = ℚ(ζ_M)⁺ makes the ray character the quadratic
  η_{E/F} (big-CM / Bruinier–Kudla–Yang setting) but only on divisors with all prime factors ≡ ±1 (M), and turns the
  moving modulus into a moving base field (H-A).

## Verdict (Assessment)
Outcome (a)+(c): a precise dictionary (T1 = incoherence parity) and a precise reason the Kudla program cannot by itself
certify ES: its arithmetic degrees are genus/class-level values at given indices (automatically positive at
certificate indices, deterministically realisable at the genus level), while ES is the existence of an index in a
ray class — the same core (H-A / B2). No existence mechanism found.

## Sparks (not pursued)
1. Big-CM / unitary Kudla over the moving base F = ℚ(ζ_{4cd})⁺ (item 4): is there a *uniform-in-M* arithmetic
   Siegel–Weil whose aggregate over M is natural (an H-A aggregate with geometric positivity)?
2. Type I: ES ⇔ the scalar χ₁(v) by which v acts on the Eichler level-e line equals ±a for a divisor a | m
   (equivalently nrd(v + a) = ace). A level-e special cycle with a *moving* level-structure datum — test whether
   Gross–Keating multiplicities at Eichler level separate it.
3. Fourier–Jacobi view: certificate indices T' = [[f,1],[1,f']] with f' fixed are coefficients c(f, r = 2) of an index-f'
   Jacobi form; summing E' over f ≡ −1 (4cd) is a twisted Jacobi coefficient sum — any positivity there?
4. The R-part (order ≥ 3 characters) at fixed slice is the whole lottery; a unitary (U(1,1) over ℚ(ζ_k)) Siegel–Weil
   for cubic/quartic characters might give it a geometric home.
