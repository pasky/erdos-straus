# bsB_redei_oddpart — what 2-power class field theory (Rédei, governing fields, spins) can see of the ES class (O175)

**ES is not solved here.** Labels as in DISCOVERIES.md. (Complements `nonab_frobenius_redei.md`, which tested
Frob_p in fixed non-abelian fields; here the question is which part of the *class condition* is 2-primary.)

## Idea
The sign layer is quadratic (genus). Rédei symbols, governing fields, 4-/8-/16-rank theorems (Rédei, Stevenhagen,
Smith, Koymans–Pagano) and FIMR spins are the 2-power refinements of genus theory. Could the ES class condition
`m'' ≡ −1 (mod t)` be a Rédei-type triple symbol, so that its distribution or existence follows from 2^∞ theory?

## Decomposition (PROVED, elementary)
Write (ℤ/t)^* = A₂ × A_odd (2-Sylow × odd part). Then `m'' ≡ −1 (t)` ⟺ (a) the A₂-component is that of −1 and
(b) every odd-order Dirichlet character mod t is 1 on m''. 2-power objects (Rédei/spins/2^k-ranks/governing
fields) only see characters of 2-power order, i.e. (a).
1. **For prime t = ℓ ≡ 3 (mod 4), A₂ = {±1}: the 2-primary part of the condition IS the genus sign** (the
   Legendre symbol (m''/ℓ)), which GI Prop 4.1 / `bsB_rayclass_norm_pullback` item 3 already transfers to
   (m''/p). Everything beyond the sign is the odd-order condition (b): **Rédei-level (quartic and higher 2-power)
   information is vacuous for every prime t.**
2. Genus at all t (not only certificates): for every divisor d of tn + 1 with the 2-adic condition,
   `(d/n) = (d/t)` (genus product formula; so at n = k² *all* divisors are residues mod t — the classical
   "prime divisors of 1 + tk² are residues mod t"). The ES class −1 is one of the (φ(t)/2) non-residue classes;
   the others are separated from it only by odd-order characters.
3. **Slices fully visible to 2-power theory**: (ℤ/t)^* is a 2-group and t ≡ 3 (4) ⟺ t = 3·F, F a product of
   distinct Fermat primes. With the known Fermat primes this is a finite set of 16 slices (t = 3, 15, 51, 255,
   771, …); finite slice menus fail i.o. under H (redteam-automorphic-2 Thm 2.2(iii)). So **every Rédei/
   governing-field mechanism is, on Type I slices, a finite-slice mechanism plus genus data** (Assessment for
   "every mechanism"; items 1–3 PROVED).
4. *Odd part via higher reciprocity (Assessment).* For ℓ ≡ 1 (3), the cubic character of m'' mod ℓ is
   ∏_{q|m''} (q/π_ℓ)_3 = ∏ (π_ℓ/𝔮)_3 (Eisenstein reciprocity, primary normalisations), where 𝔮 | q is the prime of
   ℤ[ω] — a cubic **spin**: it depends on π_ℓ mod 𝔮, not on ℓ mod q, so unlike the quadratic case it is not a
   function of p. Item (b) is a product of r-th power spins over the factorisation of tp + 1, r | (ℓ − 1)/2 odd.

## Numerics (`scripts/bsB_oddpart.py 100000 130000`)
Primes n ≡ 1 (4) in [10⁵, 1.3·10⁵], t = 7, 11, 19, 23, 31: 0 violations of (d/n) = (d/t) (item 2). Shares of
the non-residue classes among sign-odd divisors: t = 7: {3: .40, 5: .30, **6: .30**}; t = 19: class 18 = **.079**
vs max .146; t = 31: class 30 = **.049** vs max .117. The ES class −1 is the *least* populated non-residue class
(size bias: both m'' and m must be ≥ t − 1), so the odd-order condition costs more than its naive 1/(φ(t)/2).

## Barrier screen
* B2: the odd part is precisely the class layer (DE Prop 6.3/Thm 7.3 in another guise); item 3 is B2's finite
  menu. H-D: item 4 converts (b) into r-th power spins — non-abelian (Kummer) data with nonzero coefficient, the
  only H-D-shaped residue; at fixed p, spin equidistribution (FIMR; Koymans–Milovic) needs averaging over the
  prime (B6).
* T1 consistent (item 2).

## Literature
Rédei, J. reine angew. Math. 171 (1934), 180 (1939); Stevenhagen, arXiv:1806.06250; A. Smith, arXiv:1702.02325;
Friedlander–Iwaniec–Mazur–Rubin, Invent. Math. 193 (2013); Koymans–Milovic, "On the 16-rank of class groups of
ℚ(√−2p) for primes p ≡ 1 mod 4", IMRN 2019; Ireland–Rosen Ch. 9, 14 (cubic/Eisenstein reciprocity). From memory.

## Assessment
Items 1–3 PROVED (elementary). The brief's "Rédei-symbol form of the ray-class condition" does not exist beyond
genus for prime t, and for composite t it is a finite slice menu. Promise 0/5 for 2-power theory; the odd part
becomes odd-order spins (H-D residue, no fixed-p technology): promise 1/5.
