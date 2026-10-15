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
