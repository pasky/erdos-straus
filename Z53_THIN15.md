# Z53_THIN15 — side target FRONTIER §7.8: ES for 15·2^s + 1, s ≡ 0 (mod 60)

Status: z53b depth lane THIN15, internal; final memo (verdict **narrowed**), hostile review pending. **ES is OPEN; nothing here proves ES for primes.**
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
* (S4) [beyond two constants] Constrain the one-constant (non-binomial) Type I/II patterns by real-root/sign arguments,
  root degree by root degree (D = 2, 3, 4), and search the first surviving pattern.

## 2. Why this is not already closed

* Z52D Thm 2 classifies only families whose smallest coordinate x is **irreducible**; its survivor list item 1 is
  "reducible-x moving-gap families (II-ac, II-cd, general)". EXP_OPEN (I4)/Comp. 2.2 searched II-ac/II-cd only for
  small *integer* parameters (c′ ≤ 40–60, u, v ≤ 10, p ≤ 13, D ∈ {e, 2e}): EVIDENCE, not a theorem, and with the
  integrality of b, d imposed (paper Remark iiadhyp shows this is a genuine restriction). Here only x, y, z must be
  integral, every D is covered (D-independent shape test), and the parameters are bounded by proof.

## 3. Binomial menus B and B′, and a sign lemma

**Lemma 1 (normal forms of B and B′; PROVED; checkpoint-1 lemma).** Type II is (x, y, z) = (abd, acdn, bcdn) with cn = 4abcd − a − b.
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
substitution g′ = f′/a gives the formulas. Identity for (B): with f′ = (n + a)/f,
1/x + 1/y + 1/z = 4/(f′(f + 1)) + 4/(n(f + 1)) + 4a/(nf′(f + 1)) = 4(n + f′ + a)/(nf′(f + 1))
= 4(ff′ + f′)/(nf′(f + 1)) = 4/n. For (B′): 4/((f + 1)(f′ + a)) + 4a/(n(f′ + a)) + 4/(n(f + 1)) =
4[n + a(f + 1) + f′ + a]/(n(f + 1)(f′ + a)), and (f + 1)(f′ + a) = ff′ + af + f′ + a = n + a(f + 1) + f′ + a. ∎

*Remark (scope of the normalisation).* Only x, y, z are required to be integral; a, b, c, d themselves need not be
(paper Remark iiadhyp shows this is a genuine enlargement of the integer-parameter menus of EXP_OPEN). With the same
normalisations, II-ad becomes Z52D's menu A (n + c = ff′, x = (n + f)/4, y = n(1 + f′)/4, z = nx(1 + f′)/c) and I-ac
(Type I (abdn, acd, bcd), scaling (ha, hb, hc, d/h²), a = 1) becomes Z52D's A′ (x = (n + f)/4, y = xf′, z = nxf′/c) —
whether or not (n + f)/4 is irreducible. The remaining two-constant choices are degenerate: II-ab gives a constant gap
(c f = a + b constant), I-ab and I-ad give ET classes polynomial in n, I-cd is Z52D's menu C (EXP_OPEN (I4), re-derived:
I-ad: with g := 4abd − 1, cg = (a + b)n and (g + 1 + 4a²d)n = 4ad·cg, so g | (1 + 4a²d)n and g ∈ {const, const·n}).
So **every two-constant Type I/II family is in A, A′, B, B′ or C (or degenerate)**, all five built on a binomial
n + a = ff′ (C: n² + c = ff″). This is Z52D's open item 1 restricted to two constants.


Throughout §3–4: a ∈ ℚ_{>0}, n + a = f f′ in ℚ[Y] with f, f′ non-constant (if f′ is constant the family is an ET class
polynomial in n, excluded at μ = 0 by paper Thm sterile; if f is constant the gap or ratio is constant, Theorem W /
Cor. ratio), both with positive leading coefficient. Put X := f(1), X′ := f′(1), φ := f(0), φ′ := f′(0), F := 16, so
XX′ = F + a and φφ′ = 1 + a; all four are > 0 (n + a has no root in [0, ∞)). Capelli (n + a = 15(Y^D + K),
K := (1 + a)/15 > 0): K = u^p with u ∈ ℚ_{>0} and p | D an odd prime, or K = 4w⁴ with 4 | D ("SG shape"). Write
f = κP, f′ = κ′P′ with PP′ = Y^D + K monic, and K = A/B in lowest terms.

**Lemma 2 (common limit data; PROVED).** In each of A, A′, B, B′, validity near μ = 0 implies:
(i) φ is a 2-adic unit, φ ≡ 3 (mod 4);
(ii) X ∈ ℤ[1/2], and its odd part X_o divides the odd part of the numerator of F + a;
(iii) ρ := P(0)/P(1) = φ/X lies in R(K) := {ℓ/g₁ : ℓ | A, g₁ | A + B} (Z52D Lemma 6), so v₂(X) = −v₂(ρ).
*Proof.* (i) The coordinate (1 + φ)/4 (x(0) in A, A′; y(0) in B; z(0) in B′) lies in ℤ_(2). (ii) The coordinate
(F + X)/4 (x(1) in A, A′) resp. F(X + 1)/4 (y(1) in B, z(1) in B′) lies in ℤ[1/2], so X ∈ ℤ[1/2]. Let ℓ | X_o be an odd
prime; then X + 1 and F + X are ℓ-adic units. A: y(1) = F(1 + X′)/4 gives v_ℓ(X′) ≥ 0. A′: y(1) = (F + X)X′/4 gives
v_ℓ(X′) ≥ 0. B: x(1) = X′(X + 1)/4 gives v_ℓ(X′) ≥ 0. In these three, v_ℓ(F + a) = v_ℓ(X) + v_ℓ(X′) ≥ v_ℓ(X).
B′: y(1) = F(X′/a + 1)/4 gives v_ℓ(X′) ≥ v_ℓ(a); if v_ℓ(a) < 0 then v_ℓ(F + a) = v_ℓ(a), so v_ℓ(X) = v_ℓ(F + a) −
v_ℓ(X′) ≤ 0, impossible; so v_ℓ(a) ≥ 0 and v_ℓ(F + a) ≥ v_ℓ(X). (iii) X/φ = P(1)/P(0); Z52D Lemma 6. ∎
*Consequence.* For given K (i.e. given (u, p) or w) Lemma 2 yields a finite **candidate superset** of the possible
(X, φ), **independent of D**, and each candidate is tested exactly against the six local conditions. Zero surviving
candidates excludes the menu for that K and every D; a surviving candidate is only a *limit-level hit* — a family also
needs a monic factor P of Y^D + K with P(0)/P(1) = φ/X for some D (review defect 3: for c₀ = 63, K = 27, X = 21 the
test accepts φ ∈ {3, 27, 63, 567}, of which only φ = 27 is realised at D = 3). `z53_thin15_menus.py` implements this; its positive
controls recover the II-ac cubic family of 3·2^s + 1 (EXP_OPEN Prop 2.1: menu B, a = 80, (X, X′, φ, φ′) = (84, 1, 63,
9/7)), the A/A′ hits of c₀ = 3 and the II-ad family of 63·2^s + 1 (menu A, a = 1700, X = 21, X′ = 84).

### 3.1 Menu B′ (= II-cd)

**Proposition 3 (B′; PROVED).** If B′ is valid near μ = 0 then a = 1/(2^e A₂) with e ≥ 2 and A₂ odd; in particular
a < 1/4 (a = 1/4 would give K = 1/12, neither a p-th power nor 4w⁴). Consequently:
(a) B′ is empty for integer u and for integer w (there a = 15u^p − 1 ≥ 14, resp. 60w⁴ − 1 ≥ 59).
(b) Shape u^p (u = r/v, gcd(r, v) = 1): 15r^p − v^p = h with h ∈ {1, 3, 5, 15}, v even, r odd, e = p·v₂(v),
    A₂ = v^p/(h2^e). Each case is an equation |a′x^p − b′y^p| = 1 — (a′, b′) = (15, 1), (5, 3^{p−1}), (3, 5^{p−1}),
    (1, 15^{p−1}) for h = 1, 3, 5, 15 (v = 3v′, 5v′, 15v′ resp.) — so by Bennett (J. reine angew. Math. 535 (2001) 1–49,
    Thm 1.1: |ax^n − by^n| = 1 has at most one solution in positive integers for n ≥ 3) **B′ allows at most four values
    of u for each p**; CERTIFIED: none for p ≤ 11 (PARI `thue`, unconditional mode).
(c) Shape 4w⁴: r⁴ − 13500k⁴ = 1 with k ≥ 1 even; CERTIFIED: no solution (PARI `thue`). So B′ in SG shape is empty.
*Proof.* Let ℓ be an odd prime with v_ℓ(a) > 0. z(1) = F(X + 1)/4 gives v_ℓ(X) ≥ 0; y(1) = F(X′/a + 1)/4 gives
v_ℓ(X′) ≥ v_ℓ(a) > 0; so v_ℓ(F + a) > 0, but F + a ≡ 16 (mod ℓ). Hence the numerator of a is a power of 2. At Y = 0,
z(0) = (φ + 1)/4 and y(0) = (φ′/a + 1)/4 lie in ℤ_(2), so φ and ψ := φ′/a are units ≡ 3 (mod 4), and
φψ = (1 + a)/a = 1 + 1/a ≡ 1 (mod 4). Thus v₂(1/a) ≥ 2, i.e. a = 1/(2^eA₂), e ≥ 2, A₂ odd. (a) is immediate.
(b) Put G := 2^eA₂ = 1/a. From 15r^pG = v^p(G + 1) and gcd(G, G + 1) = 1 = gcd(r, v): G | v^p and r^p | G + 1; write
G + 1 = m r^p, then v^p = 15G/m, so m | 15G and gcd(m, G) = 1 (m | G + 1), i.e. m | 15. Eliminating G:
m(15r^p − v^p) = 15, so h := 15/m ∈ {1, 3, 5, 15}; v^p = hG is even, r^p = (G + 1)/m is odd and v₂(v^p) = e. For
h = 3 (resp. 5, 15) the prime 3 (resp. 5, both) divides v^p hence v, and dividing by h gives the stated forms.
(c) Same with 1 + 1/G = 60r⁴/v⁴: G | v⁴, G + 1 = mr⁴, m | 15, and m(60r⁴ − v⁴) = 60; v = 2v₁ gives
15r⁴ − 4v₁⁴ = h. Here r is odd, so 15r⁴ ≡ 15 (mod 16) and h ≡ 15 − 4v₁⁴ ∈ {11, 15} (mod 16); with h | 15 only
h = 15 with v₁ even survives, then 15 | v₁, v₁ = 15k, and r⁴ = 1 + 4·15³k⁴, k ≥ 1 (v > 0), k even. ∎

### 3.2 Menu B (= II-ac)

**Proposition 4 (B; PROVED).** Assume B is valid near μ = 0.
(a) *Odd integer u*, a = 15u^p − 1 = 2^Ec_o (c_o odd, E ≥ 1): X = jc_o − 1, X′ = j′c_o − 16 with j, j′ ≥ 1 and
  **jj′c_o = 2^E + 16j + j′**, so c_o ≤ 2^E + 17; and v₂(φ + 1) ≥ E + 2.
(b) *Even integer u*, and *integer w* (SG): impossible.
(c) *Dyadic u = r/2^i* (r odd, i ≥ 1, e := ip) or *dyadic w = r/2^i* (e := 4i − 2): with c_num := 2^e a odd,
  X = jc_num − 1, 2^eX′ = j′c_num − 2^{e+4}, j, j′ ≥ 1, **jj′c_num = 2^{e+4}j + j′ + 1**, so c_num ≤ 2^{e+4} + 2.
(d) u = 1 (a = 14) and u = 1/2 (a = 7/8) are dead for every D.
*Proof.* Let ℓ be an odd prime and k := v_ℓ(a) ≠ 0. y(1) = F(X + 1)/4 gives v_ℓ(X) ≥ 0. If k > 0 then F + a is an
ℓ-unit, v_ℓ(X′) = −v_ℓ(X), and x(1) = X′(X + 1)/4 forces v_ℓ(X) = 0 (else v_ℓ(X + 1) = 0 > v_ℓ(X′)); then z(1) =
F X′(X + 1)/(4a) forces ℓ^k | X + 1, and X′ ≡ F/X ≡ −16 (mod ℓ^k).
(a) K = u^p is a unit, so every root α of Y^D + K is a 2-adic unit and v₂(X/φ) = Σ_{P(α)=0} v₂(1 − α) ≥ 0; with (i),
X ∈ ℤ_(2) ∩ ℤ[1/2] = ℤ. φ′ = 15u^p/φ is a unit and the same argument gives X′ ∈ ℤ_(2); X′ ∈ ℤ[1/2] by x(1) (if ℓ | X
then v_ℓ(X + 1) = 0). So X, X′ are positive integers with X ≡ −1, X′ ≡ −16 (mod c_o): X = jc_o − 1, X′ = j′c_o − 16.
Expanding (jc_o − 1)(j′c_o − 16) = 16 + 2^Ec_o and dividing by c_o gives the equation; c_o = (2^E + 16j + j′)/(jj′)
≤ 2^E + 17. At Y = 0, z(0) = φ′(φ + 1)/(4a) with φ′ a unit gives v₂(φ + 1) ≥ E + 2.
(b) u = 2^ku′ (k ≥ 1, u′ odd): a is odd, K has v₂ = pk > 0, every root has v₂(α) = pk/D > 0, so
v₂(X) = v₂(φ) + Σ_{P(α)=0}(v₂(1 − α) − v₂(α)) = −τ with τ = pk·deg P/D, an integer in [1, pk − 1] (P proper). Write
X = X_o/2^τ. By the first paragraph X_o ≡ −2^τ (mod a), and by Lemma 2(ii) (proof for B) X_o | 16 + a, so
X″ := (16 + a)/X_o is an odd integer with 2^τX″ = X′ ≡ −16 (mod a). Put X_o = ja − 2^τ, 2^τX″ = j′a − 16 (j, j′ ≥ 1);
expanding X_o·2^τX″ = 2^τ(16 + a) gives jj′a = 16j + 2^τj′ + 2^τ, so a ≤ 16 + 2^{τ+1} ≤ 16 + 2^{pk}. But
a = 15·2^{pk}u′^p − 1 ≥ 15·2^{pk} − 1 > 16 + 2^{pk}. Integer w (SG): a = 60w⁴ − 1 is odd, v₂(K) = 2 + 4k (k := v₂(w)),
τ ≤ 1 + 4k, and the same equation gives a ≤ 16 + 2^{2+4k} < 60·16^k − 1 ≤ a.
(c) v₂(K) = −e < 0, so the roots have negative valuation and v₂(X/φ) = Σ v₂(1 − 1/α) = 0: X is an odd integer.
Lemma 2(ii) gives X | 2^{e+4} + c_num, so X″ := 2^eX′ = (2^{e+4} + c_num)/X is an odd integer. The first paragraph
(k = v_ℓ(c_num) > 0) gives X ≡ −1 and X″ ≡ −2^{e+4} (mod c_num); substituting X = jc_num − 1, X″ = j′c_num − 2^{e+4}
into XX″ = 2^{e+4} + c_num and dividing by c_num gives the equation.
(d) u = 1: (a) has E = 1, c_o = 7, jj′·7 = 2 + 16j + j′, whose only solution is (j, j′) = (1, 3), (X, X′) = (6, 5).
R(1) = {1, 1/2} (A = B = 1), so φ ∈ {6, 3}; φ = 6 is not a unit and φ = 3 fails v₂(φ + 1) ≥ 3. u = 1/2: the
exact test of Lemma 2 finds no survivor (computation, §5; by hand: c_num = 7, (X, X″) = (27, 5), R(1/8) = {ℓ/g₁ :
ℓ | 1, g₁ | 9}, φ ∈ {27, 9, 3} must satisfy v₂(φ + 1) ≥ e + 2 = 5 — none does). ∎
*Consequence (2-adic approximation; PROVED reduction).* In (a), 15u^p − 1 ≤ 2^E(2^E + 17), so
|u − 15^{−1/p}|₂ = |15u^p − 1|₂ = 2^{−E} ≪ u^{−p/2}: exponent p/2 > 1, hence finitely many u for each p (Ridout,
ineffective), **p = 3 included** — unlike menu A, where p = 3 has exponent exactly 1 (Z52D Cor 5.1(b)). In (c),
15r^p ≤ 17·2^{ip} + 2 and c_num > 0 give 2^i·15^{−1/p} < r ≤ (17/15)^{1/p}2^i (+ o(1)): u lies in the fixed window
(15^{−1/p}, (17/15)^{1/p}], and the condition is a divisibility (jc_num − 1) | 2^{e+4} + c_num.

### 3.3 A sign lemma for root families, and root degree 2 (PROVED)

Every root family (n irreducible in ℚ[Y]) has the Type I/II form over the PID ℚ[Y]: Type II (abd, acdn, bcdn) with
a + b + cn = 4abcd, Type I (abdn, acd, bcd) with n(a + b) + c = 4abcd, a, b, c, d ∈ ℚ[Y] (ET §2's derivation uses only
gcds and unique factorisation; if n divides all three coordinates the ratio is constant). Two normalisations:
* *Signs.* Positivity of the three coordinates for large Y forces sign lc(a) = sign lc(b) = sign lc(c) and lc(d) > 0;
  (a, b, c) ↦ (−a, −b, −c) preserves both relations and the coordinates. So WLOG all four leading coefficients are > 0.
* *Common factors.* If m ∈ ℚ[Y] (non-constant, lc > 0) divides a, b and c, then (a/m, b/m, c/m, m²d) satisfies the same
  relation (divide it by m) and gives the same x, y, z. Iterating, WLOG gcd(a, b, c) = 1.

**Lemma 5 (sign lemma; PROVED).** Let n ∈ ℝ[Y] have positive leading coefficient and let a, b, c, d ∈ ℚ[Y] (leading
coefficients > 0, gcd(a, b, c) = 1) satisfy the Type I or the Type II relation. If ρ is the largest real root of abcd,
then n(ρ) ≤ 0. For n = 15Y^D + 1: if D is even, a, b, c, d have no real root (so all have even degree); if D is odd,
every real root of abcd is ≤ −15^{−1/D}.
*Proof.* Each of a, b, c, d is ≥ 0 at ρ (no larger root, positive leading coefficient) and abcd(ρ) = 0. If n(ρ) > 0,
Type II gives a(ρ) + b(ρ) + c(ρ)n(ρ) = 0 and Type I gives n(ρ)(a(ρ) + b(ρ)) + c(ρ) = 0; all terms are ≥ 0, so
a(ρ) = b(ρ) = c(ρ) = 0, and the minimal polynomial of ρ over ℚ divides a, b, c — contradiction. For n = 15Y^D + 1,
n ≤ 0 exactly on (−∞, −15^{−1/D}] (D odd) and nowhere (D even). ∎
*Addendum (Type II, D even).* The gap f = 4abd − n has no real root either: fg = n + 4a²d with g = 4acd − 1, and at a
real root ζ of f, 4a(ζ)²d(ζ) = −n(ζ) < 0, impossible since d > 0 on ℝ.

**Theorem 6 (root degree 2 is sterile; PROVED).** For n = 15Y² + 1 (Y = 2^{s/2}) there is no root family through
μ = 0 other than ET classes polynomial in n, constant-gap and constant-ratio families — all excluded at μ = 0
(paper Thm sterile, Theorem W, Cor. ratio). Hence **no rule polynomial in 2^{s/2} reaches μ = 0 of 15·2^s + 1.**
*Proof.* By Lemma 5 all of a, b, c, d have even degree (not necessarily ≤ 2: e.g. Type I with c = d = 1,
a = (n + 1)/4, b = na + 1 has degrees (2, 4, 0, 0) — a constant-gap family; review defect 4). Since 4/n = Σ 1/x_i with
positive leading coefficients, the smallest coordinate has degree D = 2 and the other two have degree ≥ 2; we bound
only the parameters occurring in the smallest coordinate. A coordinate that is a constant multiple of n is excluded
(constant ratio). *Type II.* If the smallest coordinate is acdn (or bcdn), then a, c, d (or b, c, d) are constant:
an ET class. Otherwise it is x = abd, so (α, β, δ) := (deg a, deg b, deg d) is a permutation of (2, 0, 0); the gap
f = 4abd − n satisfies c·f = a + b, so deg c + deg f = max(α, β) ∈ {0, 2}. If max(α, β) = 0 then f is constant. If
max(α, β) = 2, a moving gap needs deg f ≥ 1, so deg c = 0 (even) and deg f = 2: then three of a, b, c, d are
constant — an ET class. *Type I* ((abdn, acd, bcd), n(a + b) + c = 4abcd). If abdn is smallest, a, b, d are constant
and it is a constant multiple of n. Otherwise, say acd is smallest: (α, deg c, δ) is a permutation of (2, 0, 0).
α = 2: c, d constant — Z52D's menu C, empty at μ = 0 (Z52D Prop 3). deg c = 2: a, d constant — I-ad: with
g := 4abd − 1 (so b = (g + 1)/(4ad)), cg = n(a + b) = n(g + 1 + 4a²d)/(4ad), hence g | (1 + 4a²d)n and
g ∈ {const, const·n}: b and c = n(a + b)/g are polynomials in n, an ET class. δ = 2: a, c constant — I-ac = menu A′,
which needs n + c (c constant) to factor; but 15Y² + 1 + c is irreducible over ℚ. (The case bcd smallest is the mirror
a ↔ b.) ∎
*Remarks.* (i) The same bookkeeping for D = 4 leaves, in Type II, only the binomial menus A, B, B′ in SG shape
(n + a = 15(Y⁴ + 4w⁴)): A-SG is impossible (Z52D Lemma 4(3)), B′-SG is impossible (Prop 3(c)), B-SG is impossible for
integer w (Prop 4(b)) and certified empty for dyadic w with e ≤ 90 (§5). **B-SG survives** for dyadic w with e > 90
and for w with an odd prime in the denominator (EVIDENCE: no hit for w = r/v, r, v ≤ 40, `sweep_15_H40_P19.log`; the
reviewer replayed r, v ≤ 60 for B-SG, 1807 cases, no hit). In Type I, D = 4 leaves A′ in SG shape (Z52D Thm 7: empty
for integer and even w, certified for dyadic w with e ≤ 66; open beyond and for odd-denominator w) and one-constant
patterns (e.g. b constant with deg c = deg d = 2; c or d constant with the smallest coordinate's a-part of degree 2);
this list is not claimed exhaustive and these patterns are not treated here. (ii) For D = 6 Lemma 5 leaves the one-constant Type II
patterns (α, β, δ, γ) = (2, 2, 2, 0), (0, 4, 2, 2), (2, 4, 0, 2), (4, 2, 0, 2) (and mirrors), i.e. II-c, II-a, II-d with
quadratic/quartic parameters — the first even degree where a non-binomial Type II family is not excluded by signs.
(iii) For odd D, Lemma 5 kills the D = 3 patterns "II-a" (a constant, b quadratic, c, d linear) and "II-c" (c constant,
a, b, d linear) by a short extra sign argument (§3.4); II-d at D = 3 survives the signs.

### 3.4 D = 3 one-constant Type II patterns

Patterns with exactly one constant at D = 3 (degree bookkeeping as in Thm 6; mirrors a ↔ b omitted): II-c with
a, b, d linear (then deg f = 1); II-a with b quadratic, c, d linear, f linear; II-d with a linear, b quadratic, c linear,
f linear.
* **II-c is empty (PROVED).** Scale to c = 1: 4abd = n + a + b with a = a₁(Y − α), b = b₁(Y − β). Then a(α) = 0 gives
  b₁(α − β) = −n(α) and likewise a₁(β − α) = −n(β). By Lemma 5, α, β ≤ −15^{−1/3}, so n(α), n(β) < 0 (equality would make
  n reducible), and a₁, b₁ > 0 force α > β and β > α simultaneously.
* **II-a is empty (PROVED).** The identity (4abd − n)(4acd − 1) = n + 4a²d with a constant and d = d₁(Y − δ): f is linear,
  f = κ(Y − ζ), κ > 0. b = (f + n)/(4ad) needs f(δ) = −n(δ); δ ≤ −15^{−1/3} gives n(δ) < 0, so κ(δ − ζ) > 0, ζ < δ. At ζ:
  4a²d(ζ) = −n(ζ) > 0 (ζ < δ ≤ −15^{−1/3}); but d is increasing with root δ > ζ, so d(ζ) < 0.
* **II-d survives the signs.** With a = Y − α (scaled), d constant, f = κ(Y − ζ): d = −n(ζ)/(4(ζ − α)²),
  κ = −n(α)/(α − ζ), and positivity forces ζ < α < −15^{−1/3}. A two-parameter family (α, ζ) ∈ ℚ²; validity near μ = 0
  is six integrality conditions on rational functions of (α, ζ). Searched in §5 (EVIDENCE); EXP_15 Comp 3.2 and R281
  searched it at smaller heights.

## 4. The covering question (S3)

**Proposition 7 (what a covering can do; PROVED, = paper Thm sterile read for this family).** Let S = {s ≡ 0 (mod 60)}.
(a) No finite set of ET classes and divisor classes (in particular no finite set of "n has the prime factor q" rules,
the Sierpiński-type coverings of the kickoff) contains all n_s, s ∈ S, s ≥ s₁: in exponent space the class
t ≡ 0 (mod lcm) always survives (s = 60t), because a divisor rule q | n at t ≡ 0 would need q | 15 + 1 = 16, and
ET classes are excluded by the odd-square argument (paper Thm sterile).
(b) Consequently, in a finite *congruence covering* — finitely many rules, each valid on a set
{s ≡ u_i (mod P_i), s ≥ s_i} — some rule is valid on all large multiples of its modulus (paper Lemma compact), i.e. on a
neighbourhood of μ = 0; if that rule is C-finite with 2-power roots it is a root family through μ = 0 (Z52D Thm 1), the
object of §3. So the kickoff's covering strategy is complete only after such a rule exists. This necessity statement
is about that covering architecture only: a proof by other means (rules valid on non-congruence sets, e.g. split by
the parity of v₂(t), or non-uniform arguments) is not excluded by (a)–(b).

**Proposition 8 (polynomial multi-base certificates collapse; PROVED; argument supplied by the hostile review).** Let
θ₁, …, θ_k > 1 be reals such that 2, θ₁, …, θ_k are multiplicatively independent (e.g. θ = 3, 5), Y = 2^{s/D},
Z_j = θ_j^{s/D′}. If x, y, z ∈ ℚ[Y, Z₁, …, Z_k] are positive integers with 4/n = 1/x + 1/y + 1/z for all s in an
infinite arithmetic progression, then x, y, z ∈ ℚ[Y], valid (positive integers) on the original progression. If that
progression contains all sufficiently large multiples of a modulus (as Prop 7(b) supplies in a congruence covering),
this is a root family through μ = 0 (§3). (An arbitrary progression is *not* a neighbourhood of μ = 0: e.g. n = 15Y + 1,
x = (2n + 1)/7, y = 2n, z = 2n(2n + 1)/7 is valid at Y = 2^s for s ≡ 1 (mod 3), but x(1) = 33/7 is not dyadic.)
*Proof.* Along s = s₀ + Lt, every monomial Y^iZ^j evaluates to C_{ij}·λ_{ij}^t with pairwise distinct positive bases
λ_{ij} (multiplicative independence), so P := 4xyz − n(xy + yz + zx) evaluates to a real exponential sum Σ c_{ij}λ_{ij}^t
with distinct bases; such a sum with a non-zero coefficient has at most (#terms − 1) real zeros (Descartes' rule for
exponential sums), so P = 0 identically. By induction on k it suffices to treat one variable Z over K := ℚ(Y, Z₂, …):
x, y, z ∈ K[Z] and 1/x + 1/y + 1/z = 4/n ∈ K^×. Let v be the valuation of K(Z) at Z = ∞ (v(1/x) = deg_Z x). If all three
Z-degrees are positive, v(LHS) > 0 = v(4/n). If exactly two (x, y) are, then 1/x + 1/y = 4/n − 1/z ∈ K has v > 0, so it
is 0 and x = −y, contradicting positivity at the sampled points. If exactly one (x) is, 1/x ∈ K has v > 0, impossible.
So all Z-degrees are 0. ∎ (Scope: polynomial, not Laurent, dependence on the Z_j; coefficients constant in s. Laurent
or rational dependence, and certificates that are not of this exponential-polynomial type, are not covered.)

## 5. Computations (exact commands; all exact integer/rational arithmetic)

All runs: `ulimit -v 4000000–6000000; timeout ≤ 1800; uv run --with gmpy2 --with cypari2 python scripts/…`.

**5.1 Finite range (S1; CERTIFIED).** `z53_thin15_solve.py T0 T1` finds, for n = 15·2^{60t} + 1, a certificate
(m, d₁, d₂): m ≡ 3 (mod 4), x = (n + m)/4, d₁, d₂ | x with m | d₁ + d₂ (divisors of the 2·10⁴-smooth part of x), giving
y = Nk/d₁, z = Nk/d₂ (N = nx, k = (d₁ + d₂)/m) and 1/y + 1/z = m/N, 1/x + m/(nx) = 4/n. `z53_thin15_check.py`
re-checks every line independently (m ≡ 3 (4), d₁ | x, d₂ | x, m | d₁ + d₂, no gaps) and, for t ≤ 10⁴, also the literal
identity 4xyz = n(xy + yz + zx). Files `cert_t1_10000.txt`, `cert_t10001_30000.txt`, `cert_t30001_50000.txt`
(≈ 0.7 MB), logs `check_*.log`: **50 000 certificates, t = 1 … 50 000, 0 failures, 0 gaps; m ≤ 167 (m = 3 for 42.6 %,
m = 7 for 28.8 % of all t; for t ≤ 10⁴: m ≤ 131, 4250 and 2904 lines).** With paper Prop 5.12 (60 ∤ s) and s = 0 (n = 16): **ES(15·2^s + 1) holds for every
s ≤ 3 000 000 (CERTIFIED)**; previously only s ≤ 52 (Salez's 10¹⁷) was known for 60 | s.
*Census* (`z53_thin15_census.py 3000 1000000`, `census_T3000_B1e6.log`): n ≡ 121 (mod 840) (Mordell-hard) for every t;
71.8 % of t ≤ 3000 have a prime factor < 10⁶ (most often 23, 79, 811, 137, 47); 846 t (first: 2, 3, 4, 11, 13, …) have
none. The certificates never need a factor of n (they use the smooth part of (n + m)/4).

**5.2 D-independent candidate-superset test (Lemma 2).** `z53_thin15_menus.py` (controls printed by running it):
c₀ = 3, u = 3, p = 3: hits in A, A′ and B, including the II-ac cubic family (B, X = 84, X′ = 1, φ = 63);
c₀ = 63, u = 3, p = 3: exactly the A hit X = 21, X′ = 84 (EXP_OPEN Thm 2.3). `z53_thin15_sweep.py c₀ H P`
(u = r/v and SG w = r/v, r, v ≤ H, odd p ≤ P, all four menus): controls `sweep_3_H12_P13_control.log` (11 hits: A, A′,
B, incl. the SG A′ hit K = 4, a = 11) and `sweep_63_H12_P13_control.log` (4 hits, all A, u = 3).
For c₀ = 15: H = 24, P = 13: 1508 (K, a) pairs, 0 hits; H = 40, P = 19 (`sweep_15_H40_P19.log`): **5221 (K, a) pairs,
0 hits** (EVIDENCE for odd-denominator u, w; the H = 60, P = 23 run was killed by its timeout without output and is
not used).

**5.3 Menu B certification (Prop 4).** `z53_thin15_menuB.py int 3000` (`menuB_int_E3000.log`, final code): u = 1 is
handled once, p-independently (a = 14, E = 1, c_o = 7: the single limit solution (X, X′) = (6, 5), killed by the exact
test, as in Prop 4(d)); then every odd integer u ≥ 3, every odd prime p with 15·3^p ≤ 1 + 2^E(2^E + 17), and every
E = v₂(15u^p − 1) ≤ 3000 with c_o ≤ 2^E + 17 is enumerated via the 2-adic root u ≡ 15^{−1/p} (mod 2^E) (incremental
Hensel lift, asserted): **0 candidates** (u ≥ 3). Brute-force cross-check (`z53_thin15_xcheckB.py 200001 13`, all odd
u ≤ 2·10⁵, p ≤ 13): the only candidates are u = 1 for each p ≤ 13, with (X, X′) = (6, 5). A run aborting on an
unfactored case prints INCOMPLETE and exits 2 (none occurred).
`z53_thin15_menuB.py dyadic 72` (`menuB_dyadic_e72.log`): 10 696 791 windows (p, i, r), e = ip ≤ 72; one limit
solution (u = 1/2, p = 3), killed. `z53_thin15_menuB.py sgdyadic 90` (`menuB_sgdyadic_e90.log`): SG shape
w = r/2^i, e = 4i − 2 ≤ 90, 3 106 120 windows, no limit solution.
**CERTIFIED: menu B has no family through μ = 0 of 15·2^s + 1 — for any D — with u an integer and E ≤ 3000, with u
dyadic and ip ≤ 72, with w an integer, or with w dyadic and 4i − 2 ≤ 90.**

**5.4 Menu B′ Thue equations (Prop 3).** `z53_thin15_thue.py 3 7 SG` and `… 3 40 SG` (PARI `thueinit(·, 1)`,
unconditional): for p = 3, 5, 7, 11 the equations 15r^p − v^p = h (h = 1, 3, 5, 15) have only the integer solutions
(0, −1) (h = 1), (1, 0) (h = 15) and, for p = 3, (−2, −5) (h = 5) — none with r, v > 0, v even; r⁴ − 13500k⁴ = 1 has
only (±1, 0) (`thue_Bprime_p3to7_SG.log`; p = 11 from `thue_Bprime_p3to11.log`, 313 s; the p = 13 computation did
not finish within the 1800 s timeout). **CERTIFIED: B′ is empty for p ≤ 11 and in SG shape.**

**5.5 II-d at D = 3 (§3.4; EVIDENCE).** `z53_thin15_iid3.py 32 16` (`iid3_Q32_R16.log`; symbolic self-test of the
parametrisation `z53_thin15_iid3_selftest.py`): α, ζ ∈ ℚ with denominator ≤ 32 and value in [−16, −15^{−1/3}),
ζ < α: 5055 values, 12 773 985 pairs; **none passes even the three Y = 1 conditions** (a diagnostic run with
denominators ≤ 16 shows 7476 pairs pass x(1), 19 pass x(1), y(1), and z(1) — whose denominator is the odd part of
C(1) = 4d(1 − α)² — always fails). EVIDENCE only.

## 6. Verdict, screens, proposed FRONTIER text

**Verdict: narrowed** (with one new certified finite range). ES(15·2^s + 1), 60 | s, remains OPEN.
* New CERTIFIED range: ES(15·2^s + 1) for every s ≤ 3·10⁶ (§5.1; before: s ≤ 52 for 60 | s).
* The two reducible-x two-constant menus are now treated like A/A′ (Z52D):
  * **B′ (= II-cd)**: forces a ≤ 1/4 (Prop 3); empty for integer u and in SG shape (PROVED/CERTIFIED); otherwise it is
    four explicit Thue equations per p, each with **at most one** positive solution (Bennett 2001), none for p ≤ 11.
  * **B (= II-ac)**: limit equation jj′c_o = 2^E + 16j + j′ (the A′ equation with X ↔ X′); even u and integer w empty
    (PROVED); u = 1, 1/2 dead for every D; certified empty for integer u, E ≤ 3000, dyadic u, ip ≤ 72, dyadic w,
    4i − 2 ≤ 90. Beyond: a 2-adic approximation of exponent p/2 — Ridout-finite for every p **including p = 3**
    (ineffective; Ridout with targets α_∞ = ∞, α₂ = β = 15^{−1/p} gives |u − β|₂/u ≪ u^{−1−p/2}, and the threshold for
    approximation by *integers* is exponent 1, not 2).
  * A finite, D-independent candidate-superset test with exact local checks (Lemma 2) for all four binomial menus and
    *rational* u; no hit at small heights (EVIDENCE: r, v ≤ 40, p ≤ 19).
* **Sign lemma (Lemma 5, PROVED)**: in any root family the real roots of a, b, c, d lie at or below the largest real root
  of n. Consequences: **no rule polynomial in 2^{s/2} reaches μ = 0 (Thm 6)**; at D = 3 the one-constant patterns II-a
  and II-c are empty; at D = 4 Type II reduces to B in SG shape with w dyadic beyond e = 90 or with an odd-denominator
  w; the first non-binomial
  Type II patterns not excluded by signs are II-d at D = 3 (EVIDENCE: no hit in 1.3·10⁷ parameter pairs) and the D = 6
  patterns of Theorem 6, Remark (ii).
* **Covering (Prop 7)**: Sierpiński-type covering congruences cannot work on their own: the class t ≡ 0 always
  survives, so the kickoff's "complete covering = theorem" route needs a rule through μ = 0 first.
* **Other bases (Prop 8, PROVED)**: certificates polynomial in 2^{s/D} and in exponentials with multiplicatively
  independent bases (3^{s/D′}, 5^{s/D′}, …) collapse to polynomials in 2^{s/D} alone (root families through μ = 0 when the progression is residue-0, as in a
  congruence covering); so "3^s, 5^s-base certificates" of
  polynomial type are not a new menu.

Surviving routes for a *congruence-covering* proof of 60 | s (not claimed exhaustive for all conceivable proofs):
(1) a binomial-menu family at a height beyond the certified bounds, or with u (or w) having an odd denominator
(A, A′, B), incl. B-SG and A′-SG at D = 4; (2) B′ for p ≥ 13 (≤ 4 values of u per p); (3) non-binomial patterns with
**at most one** constant parameter (II-d at D = 3; one-constant Type I at D = 4; D ≥ 5; zero-constant patterns such as
(α, β, δ, γ) = (4, 2, 2, 2) at D = 8 are also not excluded by signs); (4) exponential certificates outside Prop 8
(Laurent/rational dependence on other bases); (5) the kickoff's two-base boundary X = 2^t3^{t′} concerns the Pierpont
family (EXP_15 §1) and is not touched here.

**Screens (FRONTIER §4)** — for the thin-family statement; nothing here transfers to primes.
1. *T1 (odd squares):* for s ≥ 1 the family has odd squares only at s = 3, 6 (121, 961; A(A + 1) = 15·2^{s−2} forces
   A ∈ {5, 15}); s = 0 gives n = 16. None has 60 | s, s ≥ 1. The T1 obstruction of paper Thm sterile works for ET
   classes because they are polynomial in n (one picks an odd square in the class of n mod M); a root family is
   polynomial in Y, not in n, and that argument does not apply. Theorem 6 uses signs, not T1. Pass (not binding).
2. *8/131:* not applicable — every result is specific to 4/n with n = 15·2^s + 1 (F = 16 enters every limit equation).
3. *Tied modulus:* the binomial menus have fixed moduli (the odd part of a); the forced budget comes from the algebraic
   factorisation n + a = ff′, which has no analogue at a generic prime. Fails as a prime method (by design).
4. *Fixed p:* the finite-range certificates are per-integer and exact. Pass; no averaging.

**Proposed FRONTIER §7.8 replacement for the 15·2^s + 1 part** (do not edit FRONTIER from here):
> 8. **Thin families still open:** 15·2^s + 1 (60 | s), 4^s + 297, 4^s + 33, 4^s + 273.
> * 15·2^s + 1: ES CERTIFIED for every s ≤ 3·10⁶ (explicit certificates, z53 THIN15). Every non-degenerate two-constant
>   Type I/II rule is in A (II-ad), A′ (I-ac), B (II-ac), B′ (II-cd) — binomial menus on n + a = ff′ — or C (Type I,
>   (c, d) const; n² + c = ff″). C empty, B′ forces
>   a ≤ 1/4 and is four Thue equations per p (≤ 1 positive solution each, Bennett; none for p ≤ 11; SG shape empty);
>   A, A′, B are 2-adic approximation problems, certified empty for integer u up to v₂ = 3000 and for dyadic u to
>   moderate height (D-independent shape test); B is Ridout-finite for every p including p = 3, A for p = 3 is not.
> * Sign lemma (PROVED): real roots of a, b, c, d lie below the real root of n; hence no rule polynomial in 2^{s/2} reaches
>   μ = 0, and at D = 3 the only one-constant Type II pattern left is II-d (EVIDENCE: none at small height).
> * Certificates polynomial in 2^{s/D} and 3^{s/D′}, 5^{s/D′}, … collapse to polynomials in 2^{s/D} (PROVED); on a
>   residue-0 progression (as forced in a congruence covering) these are root families through μ = 0.
> * Open: binomial menus beyond the certified heights or with odd-denominator u; B′ for p ≥ 13; patterns with at most
>   one constant (II-d at D = 3, Type I at D = 4, D ≥ 5); Laurent/other exponential certificates. In a congruence
>   covering a rule through μ = 0 is necessary (Prop 7). *(z53 THIN15; z52d THINFAMILY.)*

**Bottom line.** For 15·2^s + 1 with 60 | s this lane adds a large certified range (s ≤ 3·10⁶) and closes most of the
two-constant binomial landscape around μ = 0: B′ (II-cd) collapses to finitely many Thue equations per exponent, B
(II-ac) to a 2-adic approximation problem certified empty to large heights, and a new sign lemma removes every rule of
root degree 2 and two of the three one-constant cubic patterns. No rule through μ = 0 was found, and none of the
results proves one cannot exist: the remaining room is in non-binomial patterns (at most one constant) of root
degree ≥ 3, at heights beyond the certified bounds, and in exponential certificates outside the polynomial
multi-base class (which collapses to 2-power polynomial certificates, Prop 8). ES remains open for the family (and,
of course, in general).

## 7. Review log

* **Hostile review** (fresh deep-mode subagent; report `reviews/z53-thin15-review.md`). Verdict REVISE: no fatal defect;
  3 MAJOR, 9 MINOR. The reviewer independently re-verified all 50 000 certificates (divisibility form), Lemma 1, Lemma 2,
  Props 3–4 (incl. Bennett's Thm 1.1 from the source), Lemma 5, the D = 3 sign arguments, the controls, the H24 sweep,
  the Thue runs for p ≤ 7 and SG, the census and the II-d grid counts. Repairs:
  * M1 (D = 4 survivors understated): Theorem 6 Remark (i) and §6 now keep B-SG with dyadic e > 90 and odd-denominator
    w, and A′-SG beyond Z52D's bounds; the Type I list is marked non-exhaustive.
  * M2 (covering necessity overclaimed; "one-constant" too narrow): Prop 7(b) is restricted to congruence coverings
    (paper Lemma compact); survivor lists say "at most one constant" and are not claimed exhaustive for all proofs.
  * M3 (Lemma 2 is a superset test, not a realisation test): wording fixed in Lemma 2's consequence, §5.2, §6.
  * m4 (false "degree 0 or 2" in Thm 6): proof rewritten — only the parameters of the smallest coordinate are bounded;
    the Type I case analysis is now complete (abdn-minimum, I-ad, C, A′).
  * m5 (max m = 167, exact frequencies), m6 (u = 1 is p-independent: the script now handles it once; rerun of
    `menuB.py int 3000`: 0 candidates with u ≥ 3), m8 (placeholders removed; completed logs named; p = 13 Thue not
    finished), m9 (T1: odd squares for s ≥ 1), m10 (FRONTIER text: C is n² + c = ff″), m11 (FLAG path now exits 2 with
    INCOMPLETE), m12 (a < 1/4 strictness justified).
  * m7 (other bases): the reviewer's degree-collapse argument is adopted as Prop 8 (PROVED), replacing the earlier
    Assessment.
* **Cross-model review** (`data/z53/xreview/REVIEW_THIN15.md`; independent replays incl.
  `scripts/z53_xrev_thin15_certificates.py`, all 50 000 certificates, menu-B runs, Thue p ≤ 11 + SG, sweeps, II-d grid,
  census). Verdict ACCEPT-WITH-FIXES, *narrowed* confirmed; every claim CORRECT except Prop 8 (CORRECT-WITH-FIX).
  Required fix applied: Prop 8 now concludes only "polynomial in Y, valid on the original progression", with "root
  family through μ = 0" only for residue-0 progressions (reviewer's counterexample recorded); the §6 summary, FRONTIER
  text and bottom line are scoped accordingly. Optional fix applied: the Ridout specialisation (integer threshold 1) is
  spelled out in §6.
