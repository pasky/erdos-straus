# bsB_sterile_pretentious — sterile points are maximally pretentious, not Siegel-exceptional (O175)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
Brief: read the F_q[T] sterile point x*_c (FUNCTIONFIELD_ES2 §0.2: x* ≡ 1 at every prime ≠ T, ≡ 1 + cT mod T^∞,
q = 3, A = T²) as a function-field "Siegel zero / exceptional character". Make the analogy precise and test it.

## Dictionary
1. **x*_c is a profinite square** (PROVED): 1 + cT is a square in F_q[[T]] for q odd (Hensel, constant term 1),
   and x* ≡ 1 elsewhere. Over ℤ the profinite squares are exactly the points where every quadratic character
   "pretends to be 1"; the archetype is the point 1, and its integer approximants are the primes p ≡ 1 (mod M_E),
   M_E = ∏_{ℓ≤E} ℓ (SYNTHESIS X5, DE Thm 7.3).
2. **Inversion of the brief's analogy** (Assessment, with EVIDENCE below). A Siegel-exceptional real character has
   χ(ℓ) = −1 for most small ℓ (L(1, χ) tiny). Such p have many small non-residues and are *easy* for ES (the
   certificate sign is a non-residue condition, GI Prop 4.1). Hard p are those where χ_p pretends to be the
   trivial character: L(1, χ_p) large (Granville–Soundararajan extreme values). So sterile points ↔ the
   **opposite** extreme: "maximally pretentious to 1". The FF x* is the profinite limit of that extreme with one
   deformed place.
3. **Mordell transfer in F_q[T] (PROVED relative to FF Lemma 6.2 and FF Prop 4.1, modulo one unwritten step; R175
   repair, D16: the map from a family valid at the reducible P = Q² to a coprime Prop 4.1 datum (a, b, c, d) is not
   written. Lemma 6.2 does not use irreducibility, and f ⊥ P holds because f is coprime to Aa²d. On the slice the parity
   also follows, for Case B, from FF2's QR parity (deg E, deg D even).)** Let x be a profinite square
   point and F a linear family valid at x. Every class mod W_F containing x contains squares Q² (Q monic, any large
   degree), and validity is a congruence condition on monic P of large degree, reducible or not (Lemma 6.2), so
   F yields Type II data for P = Q². There (P/f) = 1 (f ⊥ P: f ≡ −1 mod Ad and mod a), so FF Prop 4.1 forces the
   exponent to be even: **for q ≡ 3 (mod 4), deg(Ad) and deg f(Q²) are even for all large Q; for q ≡ 1 (mod 4),
   no constraint.** Over ℤ the same transfer gives a contradiction (the sign is forced to −1 by f > 0,
   f ≡ −1 (4)): every profinite square is obstructed — the archimedean place does the work. In F_q[T] the
   "archimedean" data are degrees and leading coefficients: FF2's Case A exclusion of x* is exactly an lc
   (place-at-∞) argument, and the parity constraint above is the ∞-place shadow of T1. FF2 §0.2 records that
   quadratic symbols alone do not kill Case B, consistent with item 3 being only a parity constraint.

## Cheap numerics (`scripts/bsB_pretend.py /tmp/bsB/W2e6.bin 1000000 2000000 50`)
Primes p ≡ 1 (4) in [10⁶, 2·10⁶] (35241 primes), W(p) = Type I slice a = 1 count (`scripts/bsB_wcount.c`), and
log L_y(1, χ_p) with y = 50: **corr = −0.49**; mean W/log²p is 0.18 in the bottom decile of L_y and 0.10 in
the top decile (EVIDENCE). Consistent with the hardness law of the square classes mod 840 (BRAINSTORM
adv_stacked_primes, hardness_law); the new point is the orientation of the analogy, not the correlation.

## Barrier screen
* B5/T1: item 3 is T1 itself in profinite form; over ℤ it obstructs, over F_q[T] it leaves a parity constraint.
* B1: "pretentiousness" is congruence data (χ_p(ℓ) for ℓ ≤ y), so it can only modulate the main term (B3), never
  certify. The Granville–Soundararajan maximum (R175 repair, D17: under GRH L(1, χ) ≤ (2e^γ + o(1)) log log p, i.e.
  log L(1, χ) ≤ log log log p + O(1), essentially attained) bounds how pretentious a prime can be
  (under GRH) — this is the one place where a pretentious-character theorem says something at a single p. Under
  GRH the least QNR is ≤ 2 log²p (Bach), so p cannot be a square modulo all ℓ ≤ 2 log²p; unconditionally only
  ℓ ≤ p^{1/(4√e)+o(1)} (Burgess). That bounds the "squareness" of p at a polylog modulus — exactly the scale where
  B4 (pigeonhole on small primes) already fails.
* H-A: unchanged.

## Literature
Granville–Soundararajan, "The distribution of values of L(1, χ_d)", GAFA 13 (2003); Granville–Soundararajan,
"Large character sums: pretentious characters and the Pólya–Vinogradov theorem", JAMS 20 (2007); Ankeny/Bach
(least QNR under GRH); Rosen, *Number theory in function fields*, Ch. 3 (reciprocity in F_q[T]).

## Assessment
Items 1, 3 PROVED (elementary/relative to FF lemmas); item 2 Assessment + EVIDENCE. The FF sterile point is the
maximally-pretentious (anti-Siegel) extreme; in FF its only sign-layer constraint is a degree-parity condition
(q ≡ 3 mod 4), so Conjecture 0.2, if true, needs a class-layer (Case B divisor) reason. Promise 1/5.
