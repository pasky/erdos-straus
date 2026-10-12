# AGENT REPORT O158 — Zagier-windmill / involution route (depth)

Branch `side-agent/involution-depth`. Deliverable: `INVOLUTION_ES.md`; scripts `scripts/inv_*.py`.
**ES is not solved. Outcome: (B) obstruction theorems with explicit scope; no construction.**

## Results (labels as in the file)
1. **Lemma 2.2 (PROVED)**: the ES part `{4 | tu−1}` of the O152 set X(m²) is empty for odd m (a Jacobi-symbol
   argument; the parametric form of ET Prop 1.6, without coprimality). **Prop 2.3 (PROVED)**: `|X(q²)|` is odd for
   every odd prime q. So no involution of X(q²) has ES-only fixed points (a pointwise statement), and a windmill
   on X cannot be required to work on a unit square class. Windmills on X defined on primes only are not
   affected (R158 repair). O152's odd set is odd at primes only through the periodic point `(n+2,1,1)`. The T1
   principle itself is the remark after ET Prop 1.6.
2. **Prop 3.1 (PROVED)**: for windmill families defined on the whole class, squares included (R158 repair), with
   divisor-type σ-fixed counts (residues mod M; fixed cones; square and periodic terms), T1 forces the
   coefficient of the factorisation `1·p` to vanish, for every M and unit a. This uses a 4-pattern certificate
   in a free model, checked by hand and on actual integers. A T1-compatible count must be "periodic point +
   square detector". T1 alone is not a barrier (`1+[n=□]` passes), which the file states.
3. **Finite-menu rigidity (Lemma 4.1, Prop 4.2, Thm 4.4; PROVED)**: an involution family that uses a fixed finite
   list of affine maps (pieces arbitrary, even prime-specific) acts on generic points (outside a fixed proper
   algebraic set Z) only by symmetries of the level function. The coordinate systems treated:
   * ES coordinates: S₃;
   * O152 (t,u,v), with n-dependent coefficients allowed: {id, swap};
   * O152 SL₂ (A,B,t), ET Type II (a,b,c,k) and Type II SL₂ (f,f',c,d), n-independent menus: swap,
     reparametrisations and divisor-moving scalings, which act on finitely many slices.

   None of these symmetries changes the slice integer, so no cross-slice coupling of *generic* points exists in
   this class. (R158 repair) The windmill may act only on Z, so this **reduces** the WINDMILL Prop 2 gap to a
   bounded-slice statement; it does not close it. Precursor: Elsholtz 2010 §2.1, which derives Zagier's matrix
   uniquely assuming identical invariance; Lemma 4.1 derives that invariance. Remark 4.5: O152's SL₂ unipotents
   u_k act only on the planes t=1, u=1. The full n-dependent SL₂ group is not classified.
4. **Thm 5.1 (PROVED)**: a finite-menu involution on X(p), p ≡ 1 (4) prime, with ES-only fixed points must
   certify ES(p) through an element on a fixed proper surface Z. Such windmills are therefore equivalent to
   the bounded-slice statement `E(p) ∩ Z ≠ ∅` ∀p. **Cor 5.3 (CONDITIONAL on Dickson; sketch completed by the R158
   repair)**: if Z is a union of coordinate planes, such windmills fail infinitely often.
   **Unconditionally, no primes-only windmill is excluded; the route is narrowed, not barred** (R158 repair).
   For all p ≡ 1 (24) ≤ 40000, E(p) meets the planes `{t,u,v = c}` with c ≤ 11. **Lemma 5.2 (PROVED)**: every
   ES element of X(p), p ≡ 1 (8), has a non-residue prime factor in A.

## Open, not excluded (§6)
* infinite or p-growing menus, and non-affine maps;
* n-dependent menus in the Type II / SL₂ coordinates beyond the analysed families;
* auxiliary sets other than X;
* exceptional surfaces Z that are not unions of coordinate planes (Remark 5.4 is a heuristic only);
* (R158 repair) unconditionally, every primes-only finite-menu windmill supported on a fixed surface Z,
  coordinate planes included (Cor 5.3 is conditional on Dickson).

(R158 repair) Hostile review: `reviews/involution-es-review.md`. No FATAL defects; D1–D7 (scope and framing, the
Cor 5.3 residue step, citations) have been applied in INVOLUTION_ES.md, each marked "(R158 repair)".

## Checks
* `inv_x_squares.py 1500 90000` (Lemma 2.1 for odd n ≤ 1500; E(m²)=∅ and the parity of |X(m²)| for odd m ≤ 300);
* `inv_t1_free.py 3 3 -1 2` (finds the certificate) and `inv_t1_cert_check.py` for (840,11), (24,5), (120,7),
  (1,1), (7,3);
* `inv_stab_check.py 13|97` (sympy reproduces Prop 4.2(a)–(c));
* `inv_lemma52_check.py 1500` (275 elements, 0 violations).

## Self-review (reviewer subagent, deep)
It found and I repaired the following:
* Lemma 4.1 lacked the involution hypothesis, and Z₁ properness needed a non-planar level-set hypothesis plus
  exceptional levels;
* the cone extension of Prop 3.1 is now scoped to the pattern m's;
* Lemma 4.3(ii) wording;
* a wrong congruence in Remark 5.4 (p=433, t=15), now a heuristic;
* scope and assessment overclaims.

The same reviewer also flagged issues in *other agents'* commits that were already on main. I did not touch them,
but list them for the parent:
* `scripts/bs_adv_count.c:68–74`: wrong emin/Xsmall metadata in part B;
* `scripts/bs_adv_drivers.py:60`: the "log τ(p−1)" feature actually computes the log of the smooth part;
* triage-A Prop A.2 repair: insufficient;
* overclaimed conclusions in `adv_stacked_primes.md` and `corr_typeI_typeII_joint.md`.

## Suggested ledger entry
(I)-series or WINDMILL follow-up: "Finite-menu rigidity for involution routes" — items 1–4 above, with the stated
labels.
