# AGENT REPORT O246 — EXP_OPEN (checkpoint 1)

Branch side-agent/exp-open. Main file EXP_OPEN.md; scripts scripts/z19_*; data data/z19/ (2 small files).

## SHARP
1. **ES holds for every 63·2^s + 1 (EXP_OPEN Theorem 3.1, PROVED, computer-assisted; certificate data/z19/cert63_et.json,
   independent checker scripts/z19_cert63_check.py: identities, integrality, positivity, period, coverage mod 2520,
   T1 control, exact solutions s ≤ 1000).** 63·2^s + 1 has a profinite unit-square point (no ET/divisor covering,
   EXPONENT_COVERING Cor 1.5) AND no window / constant-gap class reaches it (Theorem W below; O239 Cor 2.8). It is closed
   by a NEW kind of class: a moving-gap Type II family of root degree 3 (Theorem 2.3):
   s ≡ 0 (mod 24), Y = 2^{s/3}, a = 5, d = 17, b = (63Y³ + 3Y² − 9Y + 28)/340, c = (21Y + 64)/340, (x, y, z) = (abd, acdn, bcdn);
   mechanism: n + 4a²d = 63(Y³ + 3³) = 63(Y + 3)(Y² − 3Y + 9), the gap 4x − n = 3(Y² − 3Y + 9) is the cyclotomic factor.
   Plus 18 ET/divisor classes for all s ≢ 0 (mod 24) mod 2520.
2. **Theorem W (PROVED + finite check): no constant-gap (4x − n constant) or constant-ratio (x/n constant) family of ANY root
   degree, with ANY polynomial divisors (all Aurifeuillean/cyclotomic factorisations, fixed-prime splits of SG numerators,
   mixed sub-products, composite m, the n-atom, Type-I shapes) reaches μ = 0 of 15·2^s + 1, 31·4^s + 33, 7·4^s + 57,
   63·4^s + 1, 47·4^s + 17, 55·4^s + 9.** New tool: the limits ρᵢ = dᵢ(1) of the divisors have 2-adic valuations fixed by
   the Newton polygon of the binomial (x-factors contribute −2·deg/D, n-factors ≥ 0), which makes the magnitude argument
   of Cor 2.8 work for every divisor; Capelli at the 2-adic place leaves only m = 4c₀w⁴ − k. Positive controls recover
   exactly the known escapes of (3,1), (7,9), (23,41), (39,25). This closes every reviewer gap of EXP_105 Cor 2.8 at once.
3. **Binomial menus are the right next menu:** fixing two of (a, b, c, d) gives (besides ET / constant gap / constant ratio)
   four menus II-ac, II-ad, I-ac, II-cd where a witness is a factor of a binomial and congruences are modulo a FIXED
   modulus (EXP_OPEN §2 table). They reach unit-square points of (3,1) (new cubic family, Prop 2.1), (15,49), (39,25),
   (63,1), (55,201) — but none found for **15·2^s + 1** (nor (7,9), (23,41), (31,33), (7,57), (47,17), (55,9)).

## Results by goal
* Goal (1) 15·2^s + 1: NOT decided. Odd half 30·4^t + 1 is ET-covered at L = 60 (EVIDENCE, z15_tree; certificate not
  written). Even half: Theorem W (constant-gap/ratio: PROVED sterile); binomial menus II-ac, I-ac, II-ad, II-cd: EVIDENCE
  empty (II-ac/I-ac: c′ ≤ 40, u, v ≤ 10, p ≤ 13, SG; II-ad: u ≤ 3000, a ≤ 1000, p ≤ 7 and the limit filter of Reduction 2.5
  E ≤ 40, a₁ ≤ 2001, j, j′ ≤ 60 finds no candidate at all; II-cd: 4c²dn + 1 never reducible for c²d ≤ 3·10⁶). A larger
  II-ac/I-ac/II-ad/II-cd run (c′ ≤ 150, u, v ≤ 25, p ≤ 19, D ∈ {e, 2e, 3e}) was still running at checkpoint time
  (/tmp/z19/big15.txt). CONJECTURE 6.4 is now reduced to families with no constant gap/ratio and not in a two-constant
  binomial menu.
* Goal (2) 297 / 33 / 273: NOT decided. Prop 4.1 (PROVED): every constant-gap/ratio class through the square point μ = 3
  must split 19 off n (so lies in D₁₉'s region); no such class with period prime to 3 meets the 3-line. O239's
  "r < 0 windows" die by Jacobi. Computation 4.2 (EVIDENCE): {2,3}-supported ET coverings do not exist at supply q ≤ 10⁹
  (1.2·10⁻² uncovered). Assessment: the window question is decided negatively; 297 needs supply-efficient coverings.
* Goal (3) certificates: 63·2^s + 1 as above. Not in review_r253 tree format (flat format, own checker written from
  scratch with sympy only; the ET part was produced by the O240 machinery z19_cert_make.py = adapted z15_cert_proth_make.py).

## Honest caveats
* Theorem W's finite check enumerates a superset of limit relations (necessary conditions), so "0 relations" is a proof;
  its hypotheses: c₀ odd 4th-power-free, k ≡ 1 (8), c₀ + k = 4^J, n irreducible (true for the listed pairs).
* Map 2.4 / Computation 2.2 are small-range searches (EVIDENCE).
* Theorem 3.1 literature check not done for 63·2^s + 1 specifically.

## Suggested DISCOVERIES entry
(J)78 O246: ES for every 63·2^s + 1 (PROVED, computer-assisted) via a moving-gap cubic Type II class through a unit-square
point that every window provably misses; Theorem W (PROVED): constant-gap/ratio classes of any root degree never reach μ = 0
of 15·2^s + 1, 31·4^s + 33, 7·4^s + 57, 63·4^s + 1, 47·4^s + 17, 55·4^s + 9; binomial menus II-ac/II-ad/I-ac/II-cd
(new cubic family for 3·2^s + 1); 15·2^s + 1 and 4^s + 297 still open (Prop 4.1: windows cannot attack 297's 3-line).

## Sparks (not pursued)
* S1. Prove binomial-menu sterility for (15,1): Reduction 2.5 turns II-ad into exponential-Diophantine equations
  (k + T(E))/c₀ = u^p; similar reductions for II-ac / I-ac; a mod-3/5 argument kills j = j′ = 1 for (15,1) by hand.
* S2. One-constant menus (e.g. a constant, d linear): the specialisation trick decouples d(1) (odd places) from d(0) (2-adic) —
  the natural next search for 15·2^s + 1.
* S3. Close (15,49), (39,25), (55,201), (3,1)-variants fully with binomial-menu classes + ET (as for 63); test which
  unit-square families become coverable; 255·2^s + 1 (J = 4) with larger ranges.
* S4. Binomial menus at non-unit square points (297's μ = 3 with D₁₉ excluded) — Capelli at Y* = 1 with n(1) = 19².
* S5. Why (63,1) and not (15,1)? For j = j′ = 1 the II-ad condition is c₀(u^p − z) = (1 + z)², z = 2^E a₁ — a family of
  superelliptic curves; (63,1) sits at z = 20. For c₀ = 15 the analogous curves 15t² + 15t − 1 = u^p have no small points.
