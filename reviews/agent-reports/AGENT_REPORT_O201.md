# AGENT_REPORT_O201 — growing mute set, bounded exponent cap (spark relay V), checkpoint 1

Main file: GROWING_MUTE.md. Scripts: scripts/gm_dict.py, gm_least.py, gm_orbits.py. Data: data/gm/least_1e6.txt.
**ES is not solved; no infinite case of ES is claimed. ES^{(y,1)} for all non-squares remains OPEN.**

## SHARP:
1. **Symmetric divisor form of capped overflow (Prop 1.1(c), PROVED, checked on 816 + 497 cases).** In the shot
   family, the variant ES^{[2]} ("den(z) | y²", i.e. Q | K², K = (g+1)/4) is exactly
   **nA² + B² has a divisor g ≡ −1 (mod 2AB)** (A = 2k even, B = overflow odd, gcd(A,B) = gcd(B,n) = 1);
   ES^{(y,1)} = same with B squarefree; ES's shot family = B = 1 (the Type II line nA² + 1). T1 = sum of two
   coprime squares has no divisor ≡ 3 mod 4. Hierarchy ES ⇒ ES^{(y,1)} ⇒ ES^{[2]} ⇒ ES^{(y)} via q = 1 / q | y sqfree /
   q | y / rad q | y (den z = q²).
2. **Markoff-type surfaces (Prop 1.2, 2.2).** Equivalently: integral points on V_n : nA² + B² + D = 2λD·AB, i.e. on the
   affine cubic surfaces S_{n,D} : nA² + B² + D = ABC with 2D | C (D ≡ 3 mod 4 forced). Each (λ, D) with one point
   carries an infinite Pell orbit (so no archimedean wall once B is free — R200 M1 confirmed), but for n ≡ 1 (mod 4)
   **only one Vieta involution is integral** (reciprocity forbids n | λ, Prop 1.2(c)): no Markoff tree/descent.
   A possible new door: integral-point / Brauer–Manin theory on Markoff-type surfaces (Ghosh–Sarnak; Colliot-Thélène–
   Wei–Xu; Loughran–Mitankin — citations from memory, not checked). Is the T1 at n = m² an integral Brauer–Manin
   obstruction on V_{m²} (quaternion algebra (−1, g))? Does V_n satisfy integral strong approximation off BM for
   non-square n? Nobody in the campaign has looked at this.
3. **The growing-mute sieve has no Chebotarev content (Prop 2.1).** For each fixed P the firing primes in the
   progression g ≡ −1 (4P) are an explicit finite divisor set (g ≤ 2nP²(n + P²)); BV/BDH level is irrelevant; at every
   bounded e the per-modulus box is g^{o(1)}, so only hitting (never covering) is possible.
4. **e = 0 vs e = 1 differ only archimedeanly (Prop 3.1).** Same per-modulus box size g^{o(1)}; B = 1 caps A ≤ 3(n+1)/2,
   B free does not. GHS/smooth-number results are irrelevant at bounded e (the representatives are divisors of
   (g+1)/4, a g^{o(1)}-set).

## Results with labels
* PROVED: Prop 1.1 (cap hierarchy, (A,B) form, T1), Prop 1.2 (Markoff-type equation, Pell automorph orbits preserving
  all side conditions, no second involution for n ≡ 1 mod 4), Prop 2.1, Prop 2.2 (equivalences), Prop 3.1 (e-ladder).
* EVIDENCE (§4): all 39 175 primes p ≡ 1 (4) below 10⁶ have ES^{(y,1)} shot solutions; 116 need B > 1 within k ≤ 300
  (B ∈ {3,5,7,11,23}); p = 13, 37, 97 have provably no shot-family ES solution (complete, k ≤ 3(p+1)/4) but have
  ES^{(y,1)} ones, e.g. 4/13 = 1/6 + 1/390 + 9/65. Orbits: points per (λ, D) ≤ 3 in A, B ≤ 300; n | λ never;
  squares 9, 25, 49: none (proved).
* Assessment: ES^{(y,1)} at fixed n is an infinite (log³) lottery, immune to B3/B6, but it is a thin integral-point
  count with no equidistribution handle; not an opening for ES.

## What I did not do / caveats
* Literature claims about Ghosh–Sarnak, GHS, Harman are from memory/brief, not re-checked (labelled in text).
* §4.1 least-B values > 1 are upper bounds for p > 400 (B = 1 may occur at k > 300).
* No attempt yet at the Brauer–Manin computation on V_n (spark 1).

## Sparks (not pursued)
1. Compute the integral Brauer group of S_{n,D} / V_n and test whether the T1 at squares is exactly a BM obstruction
   and whether, for non-square n, some S_{n,D} has no BM obstruction to integral points; then compare with the
   known failure of integral Hasse beyond BM on Markoff surfaces.
2. Ghosh–Sarnak-style counting: #{D ≤ T : S_{n,D} has an admissible integral point} — a positive proportion of D
   would prove ES^{[2]}(n); this is a count over D (the "level"), not over n, so B6 does not apply.
3. Composition: representations of −D_i (i = 1,2,3) by the same principal form f_μ compose to −D₁D₂D₃; with
   D₁D₂D₃ | μ this generates new (λ, D) from old — a possible "Markoff-tree substitute" across surfaces.
4. ES (B = 1) inside V_n: is there a Vieta/automorph move from a B > 1 point back to B = 1 at the same n? (The data
   for n = 13, 37, 97 say no in general — the shot-family ES fails there.)
