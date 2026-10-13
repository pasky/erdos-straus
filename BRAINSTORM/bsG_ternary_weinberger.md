# bsG_ternary_weinberger — is there a Borwein–Choi/Weinberger (class-group exponent) structure behind (W)? (O180)

## Idea
Borwein–Choi: n ≠ xy + yz + zx ⟺ the class group of discriminant −4n has exponent ≤ 2 (idoneal-type). Then Weinberger gives
"finitely many, and at most one more without GRH". Look for the analogous quadratic structure in (W).

## Findings
1. Ternary lattice form (PROVED, tautological): n = det [[x,1,0],[1,y,1],[0,1,z]]. So (W)(n) ⟺ some positive ternary lattice of determinant n has a
   "path basis". Because the Gram determinant equals n, any path triple is automatically a basis. Summing over classes just recounts R(n).
   Siegel–Weil gives nothing new (no fixed lower-rank form is being represented).
2. Binary sublattice / ideal form (PROVED): the (x,y)-family with d = xy − 1 corresponds to the form (x, 1, y) of determinant d, i.e. the ideal
   𝔞 = (x, 1 + √−d) | (1 + √−d) in Z[√−d]. So (W)(n) ⟺ ∃ d ≤ n and an ideal 𝔞 | (1 + √−d) with N𝔞 ≡ −n (mod d), 2 ≤ N𝔞 ≤ (d+1)/2
   (and n + N𝔞 ≥ 2d). The quadratic field moves with d. There is no single class group.
3. At squares n = m², the words with middle t are factorisations of the norm t m² + 1 = N(1 + m√−t). Hence the shadow (bsG_square_shadow)
   is genus theory of Q(√−t), with t again moving.
4. Slices t ∈ {3, 4, 6} are quadratic: slice t fails ⟺ tn + 1 is (essentially) composed of primes split in Q(√−3) resp. Q(i). This
   is a norm-form condition and can hold for several t at once infinitely often (it is a quadric condition, e.g. 4(3n+1) − 3(4n+1) = 1).
5. Comparison: E_W = {2,3,5,6,9,11,14,15,35,105,510}. 105 and 2, 3, 5, 6, 9, 15 are idoneal, but 11, 14, 35, 510 are not. 2n + 1 is prime for every
   element of E_W (forced by slice t = 2).

## Literature
Borwein–Choi, *On the representations of xy + yz + zx* (Exp. Math. 2000). Weinberger (1973), exponent-2 class groups. Euler's idoneal numbers.
Lorenzini JNT 2024 §6.

## Barrier screen
B2 (divisor-class reduction): the moving discriminant (−4d or −4t) is exactly the moving modulus. A Weinberger argument needs exceptions
⟹ a *fixed* field's class group is small. In (W) each failing slice constrains a different field, so there is no exponent law.

## Assessment
Negative (Assessment, with the PROVED dictionaries 1–2). No Weinberger-type route. Promise 0.
