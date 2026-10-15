# z10_exact_family — ES^{(y,e)} certificates are the classes −4D, D ∈ 𝒟_e(M) (O234; CAP_INTERPOLATION.md §5)

**ES is not solved here.**

## Idea
In the overflow cube (c, d, j) the solution only depends on D = c²d: x = (p+E)/4, y = pA, z = pxA/D with
E = (p+4D)/M, any modulus M ≡ 3 (4), A = (M+1)/4. So ask directly which D give ES^{(y,e)}.

## Result
* Prop 5.1 (PROVED; exhaustive check M < 1200, 36 458 cases per e): ES^{(y,e)} ⟺ rad D | A and, per prime s | D,
  v_s(D) ≤ 2v_s(A) or (s odd, v_s(D) even ≤ 2v_s(A) + 2e). e = 0: D | A², the 3/4 note's ℛ(M).
* Cor 5.2: supply dimension exactly e + 3 at composite moduli (e + 2 at primes) — no tower of overflow dimensions at
  fixed e; composite multipliers should give (e+3)/(e+4) (Assessment); KARY3 does not literally apply for e ≥ 1.
* Prop 5.3: the extra local values are exactly those with v_s(z) < 0 — at e = 0 nothing is hidden.
* T1 (PROVED): (−D/M) = −1 for all D ∈ 𝒟_e(M), any e, any M.

## Assessment
A clean exact dictionary; it answers goals 2–3 negatively (no free dimension at e = 0 or fixed e) and makes the
KARY3-analogue for ES^{(y,e)} a concrete target.
