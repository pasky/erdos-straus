# Z53_THIN15 — side target FRONTIER §7.8: ES for 15·2^s + 1, s ≡ 0 (mod 60)

Status: z53b depth lane THIN15, internal, **in progress (checkpoint 1)**. **ES is OPEN; nothing here proves ES for primes.**
Labels: PROVED / CONDITIONAL / CERTIFIED (computer) / EVIDENCE / CONJECTURE / Assessment. Internally reviewed only.
Scripts `scripts/z53_thin15_*`, data `data/z53/thin15/`.

## 1. Statements attacked

Notation (as in Z52D_THINFAMILY, EXP_OPEN): n = 15Y^D + 1, Y = 2^{s/D}; μ = 0 is the profinite unit-square point
(n → 16 at every odd place, n → 1 at 2); a *root family through μ = 0* is x, y, z ∈ ℚ[Y] with
4xyz = n(xy + yz + zx), all positive integers at Y = 2^{s/D} for all s ≡ 0 (mod L), s ≥ s₁. By the specialisation lemma
(paper Lemma special) validity ⇔ positive leading coefficients, values at Y = 1 in ℤ[1/2] and at Y = 0 in ℤ_(2).

* (S0) [target] ES(15·2^s + 1) for every s ≡ 0 (mod 60). (60 ∤ s is PROVED: paper Prop 5.12.) OPEN.
* (S1) [finite range] ES(15·2^s + 1) for every s ≤ S_max: explicit certificates for s = 60t (t ≤ T). Goal CERTIFIED.
* (S2) [binomial menus] Every *two-constant* Type I/II family through μ = 0 (two of ET's a, b, c, d constant) is, after
  the scaling normalisation, one of five menus built on a binomial identity n + a = f·f′ (or n² + c = f·f″):
  A (= II-ad), A′ (= I-ac), **B (= II-ac)**, **B′ (= II-cd)**, C (Type I, (c, d) const) — or degenerate (ET class,
  constant gap, constant ratio). Z52D treated A, A′, C; **B and B′ (the reducible-x menus) are attacked here**:
  reduce them to explicit limit equations, kill what can be killed by hand, certify the rest to large 2-adic height.
* (S3) [covering] The kickoff's "covering congruence families" strategy: decide exactly what a finite covering can and
  cannot do on s ≡ 0 (mod 60).

## 2. Why this is not already closed

* Z52D Thm 2 classifies only families whose smallest coordinate x is **irreducible**; its survivor list item 1 is
  "reducible-x moving-gap families (II-ac, II-cd, general)". EXP_OPEN (I4)/Comp. 2.2 searched II-ac/II-cd only for
  small *integer* parameters (c′ ≤ 40–60, u, v ≤ 10, p ≤ 13, D ∈ {e, 2e}): EVIDENCE, not a theorem, and with the
  integrality of b, d imposed (paper Remark iiadhyp shows this is a genuine restriction). Here only x, y, z must be
  integral, every D is covered (D-independent shape test), and the parameters are bounded by proof.

## 3. First lemma (checkpoint 1)

**Lemma 1 (normal forms of B and B′; PROVED).** Type II is (x, y, z) = (abd, acdn, bcdn) with cn = 4abcd − a − b.
The rescaling (a, b, c, d) ↦ (a/h, b/h, c/h, h²d) preserves x, y, z.
(B) If a, c are constants, rescale to c = 1 and put f := 4ad − 1, f′ := b. Then n + a = f f′ and
  x = f′(f + 1)/4,  y = n(f + 1)/4,  z = n f′(f + 1)/(4a).
(B′) If c, d are constants, put λ := 4c²d (scale-invariant), g := 4bcd − 1, g′ := 4acd − 1. Then g g′ = λn + 1, and
  with a := 1/λ, f := g, f′ := a·g′: n + a = f f′ and
  x = (f + 1)(f′ + a)/4,  y = n(f′ + a)/(4a),  z = n(f + 1)/4.
Conversely each shape satisfies 4/n = 1/x + 1/y + 1/z identically whenever n + a = f f′.
*Proof.* (B): b = (cn + a)/(4acd − 1) is the II-ac identity; after scaling, f f′ = (4ad − 1)b = n + a, d = (f + 1)/(4a),
and x = a b d, y = a d n, z = b d n give the formulas. (B′): (4bcd − 1)(4acd − 1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1;
a = (g′ + 1)/(4cd), b = (g + 1)/(4cd) give x = (g + 1)(g′ + 1)/(4λ), y = n(g′ + 1)/4, z = n(g + 1)/4, and the
substitution g′ = f′/a gives the formulas. Identity for (B): 4f n + 4(n + a) + 4af = 4(ff′ + a)(f + 1)/… — direct:
1/x + 1/y + 1/z = 4[fn + (n + a) + af]/(n(n + a)(f + 1)) = 4(n + a)(f + 1)/(n(n + a)(f + 1)). For (B′):
4[n + a(f + 1) + (f′ + a)]/(n(f + 1)(f′ + a)) and (f + 1)(f′ + a) = n + a + af + f′ + a. ∎

**Proposition 2 (B′ with integer u is empty; PROVED).** By Capelli (n + a = 15(Y^D + (1 + a)/15) reducible),
1 + a = 15u^p (u ∈ ℚ_{>0}, p | D odd prime) or 1 + a = 60w⁴ (4 | D). If u ∈ ℤ, no family of shape B′ is valid near μ = 0.
*Proof sketch (full proof in §4).* At Y = 1: X X′ = 16 + a with X := f(1), X′ := f′(1); y(1) = 4(X′ + a)/a ∈ ℤ[1/2]
forces odd(a) | X′, z(1) = 4(X + 1) and the Y = 0 conditions force X, X′ ∈ ℤ, so odd(a) | 16, odd(a) = 1, i.e.
15u^p = 1 + 2^E. But 2^E mod 15 ∈ {1, 2, 4, 8} ≠ −1. ∎

**Observation 3 (B with odd integer u ≡ A′ at the limit; PROVED).** For a = 15u^p − 1 = 2^E c_o (u odd), validity of B at
Y = 1 forces X = j c_o − 1, X′ = j′ c_o − 16 with **j j′ c_o = 2^E + 16 j + j′** — the A′ equation of Z52D Thm 7 with
(j, X) ↔ (j′, X′) swapped. So the Z52D certification of A′ (E ≤ 3000: only u = 1 at the limit level) transfers; u = 1
(X, X′) = (6, 5) is killed for every D by the shape test (φ₀ ∈ {6, 3}, but B needs φ₀ ≡ −1 (mod 8)). To be re-run
independently (§5).

First falsifier queued: §5 finite-range solver (any s = 60t without a certificate would be a counterexample candidate).

## 4. Proofs (in progress)
## 5. Computations (in progress)
## 6. Verdict, screens, proposed FRONTIER text (pending)
