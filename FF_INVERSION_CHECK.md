# FF_INVERSION_CHECK — is the function-field family classification complete? The Case A inversion asymmetry (O244)

Status: in progress (O244, integrity check). **ES is not solved here, nor any infinite case of ES or ES_q.** Labels as in
DISCOVERIES.md. Builds on FUNCTIONFIELD_ES.md (= FE; Lemma 1.3, §6.2 linear families, Lemma 6.2), FUNCTIONFIELD_ES2.md (= FE2;
§0.1 compactness, §0.2 Case A), FUNCTIONFIELD_ES3.md (= FE3; Lemma 1.1, the A/B dichotomy), FF_STERILE_PUSH.md (= SP),
FF_STERILE_SMALL.md (= SS), FF_ODD_ABSENCE.md (= OA), SIBLING.md (branch side-agent/sibling-conj; Prop 1.3), POINTWISE_MORDELL17.md
(= M17; Lemma 1.1, the ℤ box types). Scripts `scripts/zi_*`, data `data/zi/`.

## 0. Iteration log

* (I1) The O242 asymmetry is real at the level of *families*: the F_q[T] model of FE §6.2 ("linear family": E = AX − P a fixed
  polynomial) does **not** contain the analogue of the Elsholtz–Tao type I4, whose ℤ boxes are M17's (U⁻¹) = −1/e. Its F_q[T]
  analogue (§1, Prop 1.4) is a genuine congruence family with balls u ≡ −1/E — exactly the missing "Case A⁻¹". Explicit
  solutions over F₃[T] (`scripts/zi_example.py`) have E_FF = AX − P of degree n − 2 or n − 1, so they lie in no linear family.
* (I2) The missing type changes nothing on the slices where sterility is proved: every Case A ball there lies inside a Case B
  ball with the *same* E (§2, Lemma 2.3; seen first in the depth-9 data, `scripts/zi_AinB.py`), Case B is inversion-closed,
  so the I4 balls lie inside Case B balls too. The second missing ET type (II2) is never valid on a slice (Lemma 2.1).

## 1. The classification, re-derived from scratch

Setting of FE §1: q odd, R = F_q[T], A monic of degree k ≥ 1, P monic prime of degree n, P ∤ A, monic denominators (NC is then
automatic, FE Lemma 1.2).

**Lemma 1.1 (ET parametrisation over F_q[T]; PROVED).** Let A/P = 1/X₁ + 1/X₂ + 1/X₃ with X_i monic. Then P divides one or two
of the X_i, and after renumbering there are monic a, b, c, d ∈ R with c | a + b, e := (a + b)/c, and
 (Type I, P | X₁ only)        X₁ = abdP, X₂ = acd, X₃ = bcd,  A·abd = eP + 1   (equivalently A·abcd = (a + b)P + c);
 (Type II, P | X₂, X₃ only)   X₁ = abd, X₂ = acdP, X₃ = bcdP, A·abd = P + e    (equivalently A·abcd = cP + a + b).
Conversely each such (a, b, c, d) gives a solution (lc conditions aside).
*Proof.* If P divides no X_i, the right side has a P-free denominator but A/P has not. If P divides all three, A = Σ 1/(X_i/P)
with monic X_i/P: deg A = k ≥ 1, while the right side has degree ≤ 0. Type II: X₂ = PY', X₃ = PZ' give
(AX₁ − P)/X₁ = 1/Y' + 1/Z'. The left side is in lowest terms (gcd(AX₁ − P, X₁) = gcd(P, X₁) = 1). Put g = gcd(Y', Z') (monic),
Y' = gy, Z' = gz; then 1/Y' + 1/Z' = (y + z)/(gyz) with gcd(y + z, yz) = 1, so its reduced form has numerator (y + z)/c and
denominator dyz, where c := gcd(y + z, g), d := g/c. Comparing reduced forms (all monic): X₁ = dyz, AX₁ − P = (y + z)/c. Take
a = y, b = z (then Y' = acd, Z' = bcd). Type I: X₁ = PX₁', P ∤ X₂X₃ give (AX₁' − 1)/(PX₁') = (y + z)/(c·dyz) with the same notation. The right side's
reduced denominator is prime to P, so P | AX₁' − 1, and then X₁' = dyz, (AX₁' − 1)/P = (y + z)/c. ∎
(This is ET 2013 Prop 1.3 transcribed; nothing in it uses ℤ beyond unique factorisation, and "monic" replaces "positive".)

**Lemma 1.2 (which parametrised solutions are linear families; PROVED).** The NC-minimal denominator X (deg X = n − k, FE
Lemma 1.2) and E_FF := AX − P (the "E" of FE Lemma 1.3 and of every linear family) are:
 Type II: X = X₁ = abd and **E_FF = e**;
 Type I (deg a < deg b, say): X = X₂ = acd and **E_FF = (aP + c)/b**, of degree n − (deg b − deg a).
A linear family (FE §6.2) is by definition a family with E_FF a fixed polynomial. So, over a family of P (some parameters fixed,
the others functions of P), it is linear iff e stays bounded (Type II) or b/a grows like P (Type I).
*Proof.* Type II: deg X₂, X₃ ≥ n > n − k. Type I: A·acd = c(eP + 1)/b and ce = a + b give AX₂ − P = (aP + c)/b. Monicity of all
three denominators forces lc(a + b) = 1 in Type I (see Prop 1.4), so deg a ≠ deg b and the smaller of X₂, X₃ is the one with the
smaller of a, b. ∎

**Corollary 1.3 (the ET dictionary).** The seven ET families (fix three of the parameters, solve for the rest; ET 2013 §2, M17
Lemma 1.1, `scripts/mordell_lib.py`) translate as follows. Linear (E_FF fixed): II1 (a, b, e fixed; d = (P + e)/(Aab); E_FF = e),
II3 (a, d, e fixed; E_FF = e), I1 (a, d, f fixed; c, b ~ P; E_FF = f), I2 (a, c, f fixed; d, b ~ P; E_FF = f), I3 (c, d, f fixed;
a ~ P, b ~ P²; E_FF = f). **Not linear:** I4 (a, b, e fixed; E_FF = (aP + c)/b grows) and II2 (a, c, d fixed, f := Aacd − 1,
b = (cP + a)/f; E_FF = e = (a + b)/c = (P + Aa²d)/f grows).
*Proof.* Lemma 1.2 applied to each parametrisation (for I1–I3 the fixed f equals AX − P for X = acd: AX = P + f is the defining
divisibility of each). ∎

**Proposition 1.4 (the I4 analogue is a congruence family outside the linear model; PROVED).** Let a, b, e ∈ R be monic with
deg a ≠ deg b, e | a + b, gcd(e, Aab) = 1, and put c := (a + b)/e. For every monic prime P with **Aab | eP + 1** and
n = deg P ≥ k + deg a + deg b − deg e, the polynomial d := (eP + 1)/(Aab) is monic and
  A/P = 1/(abdP) + 1/(acd) + 1/(bcd)
with three monic denominators (NC automatic). So the family **I4(a, b, e)** is valid on the unit class P ≡ −e^{−1} (mod Aab):
its validity set V_{I4} ⊂ R̂^* is clopen, defined by one congruence. At a slice point x_u (x ≡ 1 at every prime ≠ T, x ≡ u mod
T^∞; A = T^k) it is valid iff
  T^{k+v_T(ab)} | ue + 1  and  (ab)' | e + 1     ((ab)' = prime-to-T part),
i.e. on the **ball u ≡ −1/e (mod T^{k+v_T(ab)})** — the mirror image of the Case A ball u ≡ −E (mod T^{k+j}) of FE3 Lemma 1.1.
Its solutions have E_FF = (aP + c)/b (deg a < deg b), of degree n − deg b + deg a → ∞: I4(a, b, e) is not a linear family, and no
finite set of linear families has the same validity set restricted to large n. (For a single P the solution does lie in a
linear family, namely (E_FF(P); 1, a; 0, c), but that family changes with P.)
*Proof.* d is a polynomial by hypothesis; lc(d) = lc(e)/lc(Aab) = 1, lc(c) = lc(a + b) = 1 as deg a ≠ deg b, so all three
denominators are monic. The identity is A·abcd = c(eP + 1) = (a + b)P + c, which is the Type I equation of Lemma 1.1. NC: FE
Lemma 1.2 (odd q). The slice form: x ≡ u at T and x ≡ 1 at the primes of (ab)'. The single-P statement: with κ = b,
a_FF = Pa, b_FF = c in FE Lemma 1.3 one gets Y = κPX/a_FF = bcd and Z = κPX/b_FF = abdP, κ = (a_FF + b_FF)/E_FF. ∎

*Example (`scripts/zi_example.py`, q = 3, A = T²).* a = 1, b = T, e = T + 1 (c = 1): P = T⁶ + T⁴ + 2T² + T + 2 is irreducible,
T³ | eP + 1, and the three denominators have degrees 11, 4, 5, all monic; E_FF = T⁵ + T³ + 2T + 1 (degree n − 1). Twelve such
examples, all verified by the identity A·X₁X₂X₃ = P(X₁X₂ + X₂X₃ + X₃X₁).

**Remark 1.5 (II2).** The other non-linear ET type, II2(a, c, d): f := Aacd − 1, b := (cP + a)/f, solution (abd, acdP, bcdP), is
valid on the class f | cP + a, i.e. P ≡ −a/c (mod f). Since f ≡ −1 (mod T) when T | A, it has no T-adic condition at all.

**What FE3 Lemma 1.1 classifies, and what it does not.** FE3 Lemma 1.1 (the A/B dichotomy) is correct and complete *for linear
families*: re-derived here from scratch for all 16 type pairs (t_a, t_b) ∈ {0,1,2,3}²: at a slice point P ≡ 1 and
X ≡ T^{−k} (mod E), so a ≡ a0 (types 0, 1) or (T^k a0)^{−1} (types 2, 3); same side gives E | a0 + b0 (after multiplying by the
unit T^k a0 b0 in the 2/3 case), opposite sides give E | 1 + T^k a0 b0. The normalisations used afterwards (a0 = T^γ g'·a1 etc.,
γ ≤ j, gcd removal, WLOG deg a1 ≥ deg b1 by the symmetry a ↔ b of the family) lose nothing for linear families. The gap is
one level up: the *definition* of a linear family (FE §6.2, fixed E) is narrower than the ET family notion, and
Cor 1.3 shows that it omits exactly I4 and II2.

## 2. On the slices the missing types are dominated by Case B

Setting: A = T^k, q odd, slice points x_u. "Family valid at x_u" for linear families is FE3 Lemma 1.1 (stated for general k);
for I4 it is Prop 1.4. Notation of FE3/FE2 §0.2 for a Case A family: a0 = g·a1, b0 = g·b1, gcd(a1, b1) = 1, E | a1 + b1,
E ≡ −1 (mod g'·(a1b1)'), E ≡ −u (mod T^{k+j}), j = v_T(lcm(a0, b0)) = γ + v_T(a1b1).

**Lemma 2.1 (II2 is never valid on a slice; PROVED).** For every k ≥ 1 and every slice point x_u, no II2(a, c, d) is valid at x_u.
*Proof.* f = Aacd − 1 ≡ −1 (mod T), so all primes of f are ≠ T and x_u ≡ 1 at them: validity f | cP + a becomes f | a + c. As
deg f = k + deg a + deg c + deg d > deg(a + c) (k ≥ 1), this forces a + c = 0, impossible for monic a, c (Lemma 1.1 makes all
four parameters monic; q odd). ∎

**Lemma 2.2 (I4 is the mirror of Case A; PROVED).** If I4(a, b, e) is valid at x_u, then the linear family
F^A := (e; 0, a; 0, b) is a Case A family valid at x_{1/u}, with E = e monic and deg a ≠ deg b. Its ball u' ≡ −e
(mod T^{k+j}) at 1/u has j = v_T(lcm(a, b)) ≤ v_T(ab), so 1/(I4 ball) ⊆ (ball of F^A). For gcd(a, b) = 1 the two balls are exact
mirror images, and the I4 data with gcd(a, b) = 1 are exactly the Case A data (a1, b1, E) with E monic, deg a1 ≠ deg b1.
*Proof.* Validity of F^A at x_{1/u} (FE §6.2): A·lcm(a, b) | P + e at x_{1/u} means T^{k+j} | u^{−1} + e, i.e. T^{k+j} | ue + 1,
implied by T^{k+v_T(ab)} | ue + 1; and lcm(a, b)' | 1 + e, implied by (ab)' | e + 1. s = a + b ≠ 0, e | s, lc(s) = 1 = lc(e)
since deg a ≠ deg b. Conversely, a Case A datum with gcd(a1, b1) = 1, E monic, deg a1 ≠ deg b1 satisfies the hypotheses of
Prop 1.4 with (a, b, e) = (a1, b1, E) (gcd(E, Aa1b1) = 1 since T ∤ E and E ≡ −1 mod (a1b1)'). ∎

**Lemma 2.3 (a Case A ball lies in a Case B ball with the same E; PROVED).** Let F be a Case A family valid at x_u with E monic,
T^α ∥ a1, T ∤ b1 (after renaming), α ≥ 1, and put v := v_T(E + 1), H := (E + 1)/T^v. Suppose **α + v ≥ k** and v ≤ k + α. Put
  s := α + v, L' := H/b1, g' := (a1)' = a1/T^α, j := ⌈(s − k)/2⌉, γ := ⌊(s − k)/2⌋.
Then (E; 0, T^γ g'; 2, T^j L') is a Case B family (D = 1 + T^s L'g', E | D, D/E monic) valid at x_u, and at every point of the
Case A ball of F; its ball u ≡ −E (mod T^{k+j}) contains the Case A ball.
*Proof.* H is T-free; E ≡ −1 (mod (a1b1)') gives (a1)'·b1 | H, so L' is a T-free polynomial with E ≡ −1 (mod L') and
g' | L' (gcd(a1', b1) = 1). Modulo E: T^v H = E + 1 ≡ 1 and b1 ≡ −a1 = −T^α g' (E | a1 + b1; b1 is a unit mod E because
b1 | E + 1). Hence T^s L' g' = T^v H · T^α g'/b1 ≡ −1, i.e. E | D. D is monic (H, b1, g' monic), so D/E is monic. 0 ≤ γ ≤ j and
s = k + j + γ. The Case A ball has depth k + j_A with j_A ≥ α, and j ≤ α because s − k ≤ 2α (v ≤ k + α); so E ≡ −u
(mod T^{k+j}) on it. FE3 Lemma 1.1, converse (re-derived: A·T^jL' | P + E is the congruence pair E ≡ −u mod T^{k+j},
E ≡ −1 mod L'; mod E, P ≡ 1, X ≡ T^{−k}, so s_F = T^γg' + X/(T^jL') ≡ (T^sL'g' + 1)/(T^{k+j}L') ≡ 0; lc(s_F) = 1 = lc(E) for
n large) gives validity. ∎

**Lemma 2.4 (Case B is inversion-closed; PROVED, any k ≥ 1, q odd).** If the Case B family with data (E, L', g', s, j, γ) is valid
at x_w, then the one with (E' := D/E, L', g', s, j, γ) is valid at x_{1/w}.
*Proof.* EE' = D ≡ 1 (mod T^s) and s ≥ k + j give E' ≡ −1/w (mod T^{k+j}); D ≡ 1 (mod L') and E ≡ −1 give E' ≡ −1 (mod L');
E' monic, E' | D. Lemma 2.3's converse argument. (This is the swap τ^∨ of SIBLING Prop 1.3, stated there for k = 2.) ∎
