# FF_INVERSION_CHECK — is the function-field family classification complete? The Case A inversion asymmetry (O244)

Status: checkpoint 1 (O244, integrity check); self-reviewed, no hostile review yet. **ES is not solved here, nor any infinite case of ES or ES_q.** Labels as in
DISCOVERIES.md. Builds on FUNCTIONFIELD_ES.md (= FE; Lemma 1.3, §6.2 linear families, Lemma 6.2), FUNCTIONFIELD_ES2.md (= FE2;
§0.1 compactness, §0.2 Case A), FUNCTIONFIELD_ES3.md (= FE3; Lemma 1.1, the A/B dichotomy), FF_STERILE_PUSH.md (= SP),
FF_STERILE_SMALL.md (= SS), FF_ODD_ABSENCE.md (= OA), SIBLING.md (branch side-agent/sibling-conj; Prop 1.3), POINTWISE_MORDELL17.md
(= M17; Lemma 1.1, the ℤ box types). Scripts `scripts/zi_*`, data `data/zi/`.

## 0. Iteration log

* (I1) The O242 asymmetry is real at the level of *families*: the F_q[T] model of FE §6.2 ("linear family": E = AX − P a fixed
  polynomial) does **not** contain the analogue of the Elsholtz–Tao type I4, whose ℤ boxes are M17's (U⁻¹) = −1/e. Its F_q[T]
  analogue (§1, Prop 1.4) is a genuine congruence family with balls u ≡ −1/E — exactly the missing "Case A⁻¹". Explicit
  solutions over F₃[T] (`scripts/zi_example.py`) have E_FF = AX − P of degree n − 2 or n − 1, so these solution triples are
  produced by no fixed linear family.
* (I2) The missing type changes nothing on the slices where sterility is proved (for k ≥ 3: relative to the level-2 covered set
  that the proofs bound): for k ≤ 2 every Case A ball with monic E there lies inside a Case B ball with the *same* E (§2, Lemma 2.3; seen first in the depth-9 data, `scripts/zi_AinB.py`), Case B is inversion-closed,
  so the I4 balls lie inside Case B balls too. The second missing ET type (II2) is never valid on a slice (Lemma 2.1).
* (I3) Checkpoint: verdict "classification incomplete as a *definition*, complete in effect on the sterility slices"
  (Thm 2.5, Cor 2.6); no PROVED theorem needs repair; report `reviews/agent-reports/AGENT_REPORT_O244.md`.

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
denominator dyz, where c := gcd(y + z, g), d := g/c. Comparing reduced forms (denominators monic; the numerator (y + z)/c need not be,
e.g. lc 2 if deg y = deg z): X₁ = dyz, AX₁ − P = (y + z)/c. Take
a = y, b = z (then Y' = acd, Z' = bcd). Type I: X₁ = PX₁', P ∤ X₂X₃ give (AX₁' − 1)/(PX₁') = (y + z)/(c·dyz) with the same notation; gcd(AX₁' − 1, X₁') = 1. The right side's
reduced denominator is prime to P, so P | AX₁' − 1, and then X₁' = dyz, (AX₁' − 1)/P = (y + z)/c. ∎
(This is ET 2013 Prop 1.3 transcribed; nothing in it uses ℤ beyond unique factorisation, and "monic" replaces "positive".)

**Lemma 1.2 (which parametrised solutions are linear families; PROVED).** The NC-minimal denominator X (deg X = n − k, FE
Lemma 1.2) and E_FF := AX − P (the "E" of FE Lemma 1.3 and of every linear family) are:
 Type II: X = X₁ = abd and **E_FF = e**;
 Type I (deg a < deg b, say): X = X₂ = acd and **E_FF = (aP + c)/b**, of degree n − (deg b − deg a).
A linear family (FE §6.2) fixes E (= E_FF), a0, b0 and the types. So a family of solutions (some parameters fixed, the others
functions of P) can be a linear family only if E_FF is the same polynomial for all its P; in Type I this needs deg b − deg a to
grow like n. (The converse — that the five ET types listed in Cor 1.3 as linear really are linear families with fixed a0, b0 and
types — is checked type by type there; review fix R-O244.)
*Proof.* Type II: deg X₂, X₃ ≥ n > n − k. Type I: A·acd = c(eP + 1)/b and ce = a + b give AX₂ − P = (aP + c)/b. Monicity of all
three denominators forces lc(a + b) = 1 in Type I (see Prop 1.4), so deg a ≠ deg b and the smaller of X₂, X₃ is the one with the
smaller of a, b. ∎

**Corollary 1.3 (the ET dictionary).** The seven ET families (fix three of the parameters, solve for the rest; ET 2013 §2, M17
Lemma 1.1, `scripts/mordell_lib.py`) translate as follows. Linear (E_FF fixed): II1 (a, b, e fixed; d = (P + e)/(Aab); E_FF = e),
II3 (a, d, e fixed; E_FF = e), I1 (a, d, f fixed; c, b ~ P; E_FF = f), I2 (a, c, f fixed; d, b ~ P; E_FF = f), I3 (c, d, f fixed;
a ~ P, b ~ P²; E_FF = f). **Not linear:** I4 (a, b, e fixed; E_FF = (aP + c)/b grows) and II2 (a, c, d fixed, f := Aacd − 1,
b = (cP + a)/f; E_FF = e = (a + b)/c = (P + Aa²d)/f grows).
*Proof.* Lemma 1.2 applied to each parametrisation (for I1–I3 the fixed f equals AX − P for X = acd: AX = P + f is the defining
divisibility of each). The linear ones are linear families with fixed (a0, b0, types) (review fix): in FE Lemma 1.3 form, Type II
with κ = c has (a_FF, b_FF) = (b, a), Type I with κ = b has (a_FF, b_FF) = (Pa, c) (using bE_FF = aP + c). Hence II1 =
(e; 0, b; 0, a); II3 = (e; 2, ad; 0, a) (b = X/(ad)); I1 = (f; 1, a; 2, ad) (c = X/(ad)); I2 = (f; 1, a; 0, c); I3 = (f; 3, cd; 0, c)
(Pa = PX/(cd)). For I4 the same (Pa, c) are fixed-shape but E_FF is not fixed. ∎

**Proposition 1.4 (the I4 analogue is a congruence family outside the linear model; PROVED).** Let a, b, e ∈ R be monic with
deg a ≠ deg b, e | a + b, gcd(e, Aab) = 1, and put c := (a + b)/e. For every monic prime P with **Aab | eP + 1** and
n = deg P ≥ k + deg a + deg b − deg e, the polynomial d := (eP + 1)/(Aab) is monic and
  A/P = 1/(abdP) + 1/(acd) + 1/(bcd)
with three monic denominators (NC automatic). So the family **I4(a, b, e)** is valid on the unit class P ≡ −e^{−1} (mod Aab):
its validity set V_{I4} ⊂ R̂^* is clopen, defined by one congruence. At a slice point x_u (x ≡ 1 at every prime ≠ T, x ≡ u mod
T^∞; A = T^k) it is valid iff
  T^{k+v_T(ab)} | ue + 1  and  (ab)' | e + 1     ((ab)' = prime-to-T part),
i.e. on the **ball u ≡ −1/e (mod T^{k+v_T(ab)})** — the mirror image of the Case A ball u ≡ −E (mod T^{k+j}) of FE3 Lemma 1.1.
Its solutions have E_FF = (aP + c)/b (deg a < deg b), of degree n − deg b + deg a → ∞: I4(a, b, e) is not a linear family, and
its *solution triples* are produced by no finite set of linear families. (For a single P the solution does lie in a linear
family, namely (E_FF(P); 1, a; 0, c), but that family changes with P.) This says nothing about whether the *validity set* of
I4(a, b, e) is covered by linear validity sets — it can be: for a = 1, b = T, e = 1 (A = T²) the class P ≡ −1 (mod T³) is also
the validity set of the linear family (1; 0, T; 1, 1) (review counterexample). Coverage questions are settled in §2 on the
slices only.
*Proof.* d is a polynomial by hypothesis; lc(d) = lc(e)/lc(Aab) = 1, lc(c) = lc(a + b) = 1 as deg a ≠ deg b, so all three
denominators are monic. The identity is A·abcd = c(eP + 1) = (a + b)P + c, which is the Type I equation of Lemma 1.1. NC: FE
Lemma 1.2 (odd q). The slice form: x ≡ u at T and x ≡ 1 at the primes of (ab)'. The single-P statement: with κ = b,
a_FF = Pa, b_FF = c in FE Lemma 1.3 one gets Y = κPX/a_FF = bcd and Z = κPX/b_FF = abdP, κ = (a_FF + b_FF)/E_FF. ∎

*Example (`scripts/zi_example.py`, q = 3, A = T²).* a = 1, b = T, e = T + 1 (c = 1): P = T⁶ + T⁴ + 2T² + T + 2 is irreducible,
T³ | eP + 1, and the three denominators have degrees 11, 4, 5, all monic; E_FF = T⁵ + T³ + 2T + 1 (degree n − 1). Twelve such
examples, all verified by the identity A·X₁X₂X₃ = P(X₁X₂ + X₂X₃ + X₃X₁).

**Remark 1.5 (II2).** The other non-linear ET type, II2(a, c, d): f := Aacd − 1, b := (cP + a)/f, solution (abd, acdP, bcdP), is
valid on the class f | cP + a, i.e. P ≡ −a/c (mod f). Since f ≡ −1 (mod T) when T | A, it has no T-adic condition at all.

**Lemma 1.6 (three bounded parameters; PROVED).** Call a family *3-bounded* if three of a, b, c, d are fixed and the fourth is a
function of P (n → ∞). The 3-bounded families are exactly II1 (a, b, c fixed; linear), II2 ((a, c, d) or (b, c, d) fixed) and I4
(a, b, c fixed, Type I). *Proof.* Type I, A·abcd = (a + b)P + c: (a, b, c) fixed gives I4. (a, b, d) fixed: c(Aabd − 1) = (a + b)P
forces deg c ≥ n − O(1) for large n (P ∤ Aabd − 1), contradicting c | a + b. (a, c, d) fixed: b(Aacd − P) = aP + c makes b bounded
too, so only finitely many P. (b, c, d): symmetric. Type II, A·abcd = cP + a + b: (a, b, c) gives II1; (a, c, d) gives
b(Aacd − 1) = cP + a, II2; (a, b, d): c(Aabd − P) = a + b is impossible by degrees for large n. ∎
*Scope.* ET's other four types fix two of a, b, c, d plus E_FF (Cor 1.3) and are linear. Families fixing other auxiliary
combinations (two of a, b, c, d and some quantity other than E_FF, or fewer) are **not classified here**; the claim of this
document is completeness relative to the seven ET types, which is also the scope of the ℤ box classification M17 Lemma 1.1.

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

**Lemma 2.3 (a Case A ball lies in a Case B ball with the same E; PROVED).** Let F be a Case A family valid at x_u with E monic of positive
degree, T^α ∥ a1, T ∤ b1 (after renaming), α ≥ 1, and put v := v_T(E + 1), H := (E + 1)/T^v. Suppose **α + v ≥ k** and v ≤ k + α. Put
  s := α + v, L' := H/b1, g' := (a1)' = a1/T^α, j := ⌈(s − k)/2⌉, γ := ⌊(s − k)/2⌋.
Then (E; 0, T^γ g'; 2, T^j L') is a Case B family (D = 1 + T^s L'g', E | D, D/E monic) valid at x_u, and at every point of the
Case A ball of F; its ball u ≡ −E (mod T^{k+j}) contains the Case A ball.
*Proof.* H is T-free and monic (deg E ≥ 1); E ≡ −1 (mod (a1b1)') gives (a1)'·b1 | H, so L' is a T-free polynomial with E ≡ −1 (mod L') and
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

**Theorem 2.5 (the missing types add nothing on the sterility slices; PROVED).** Let q be odd and let Σ be either
 (i) k ≥ 2 and the c-slices u ≡ 1 + cT (mod T²), c ≠ 0 (SP, SS §§3–5, SIBLING), or
 (ii) k = 1, q = 3^r, and the slices u(0) ∉ F₃^* (SS §§6–8, OA §2).
For x_u ∈ Σ with k ≤ 2: if some family of the seven ET types (linear, I4 or II2) is valid at x_u, then some linear family is
valid at x_u; if an I4 family is valid at x_u, then a Case B family is valid at x_u. For k ≥ 3 (case (i)): every x_u ∈ Σ at which
some level-k ET-type family is valid lies in the covered set of the *level-2* linear families (the set whose measure SP/SS
bound). For k ≤ 2 moreover every Case A family with E monic valid
at x_u is dominated by a Case B family with the same E (Lemma 2.3). Hence O_ET(q, T^k) ∩ Σ = O(q, T^k) ∩ Σ for k ≤ 2, and O_ET(q, T^k) ∩ Σ ⊇ O(q, T²) ∩ Σ for k ≥ 3, where O_ET is the
set of points at which no ET-type family is valid.
*Proof.* II2: Lemma 2.1. I4, k = 2 (case (i)): by Lemma 2.2, F^A is a Case A family valid at x_{1/u}, and 1/u lies in the
(−c)-slice. FE2 §0.2 step (1) uses only u ≡ 1 + cT (mod T²); applied at 1/u it gives T^α ∥ a1 with α ≥ 1 and T ∤ b1 for the
labelling with deg a1 ≥ deg b1, and E + 1 ≡ cT (mod T²) gives v = 1. So α + v ≥ 2 = k and v ≤ k + α: Lemma 2.3 gives a Case B
family valid at x_{1/u}, and Lemma 2.4 one valid at x_u. Case (ii): at 1/u, u(0)^{−1} ∉ F₃^*, so SS Lemma 7.2(a) gives α ≥ 1,
and e(0) = −u(0)^{−1} ≠ −1 gives v = 0; α + v ≥ 1 = k, and conclude as before. k ≥ 3 in case (i) — the data of linear families,
of I4 and of Case B tuples do not depend on k except through the ball depth:
 a Case A or I4 datum has ball depth k + (fixed), so its level-k ball lies in its level-2 ball (same centre);
 a level-k Case B datum (E, L', g', s, j, γ), s = k + j + γ, is a level-2 datum with j₂ = j + k − 2, γ₂ = γ (γ₂ ≤ j₂), with the
 same ball (depth 2 + j₂ = k + j).
So covered_k(A ∪ B ∪ I4) ⊆ covered_2(A ∪ B ∪ I4) = covered_2(A ∪ B) (the k = 2 case), and the k ≥ 3 statements of SP/SS (which
are proved by bounding the k = 2 covered measure — "N(s) and the Case A exponent only grow with k", SP Thm 3.1 proof) hold with
I4 and II2 included. ∎

**Corollary 2.6 (the PROVED no-covering theorems survive; PROVED).** (J)51 (SP Thm 3.1), (J)56 (SS Thms 3.1, 5.2, 7.3, 8.1) and
(J)67 (OA Thm 2.2) each exhibit a positive-measure subset of Σ outside every linear validity set. By Thm 2.5 these points are
outside the validity sets of all seven ET-type families. So each theorem holds verbatim with "linear covering" replaced by
"covering by families of the seven ET types", with the same certified constants: **no repair is needed, the union bounds do not
undercount** (on Σ the I4 balls lie in Case B balls — for k ≥ 3 in level-2 Case B balls, which is what the proofs bound — and
for k ≤ 2 even the Case A terms of (Σ) with monic E are redundant; for k = 1, Case A data with lc(E) = 2 (SS Lemma 7.2) are not
covered by Lemma 2.3 and stay in the bound). The same holds for Conjecture 0.2 (x*_c ∈ O ⟺ x*_c ∈ O_ET) and for
O140 Prop 4.1 (the point x ≡ 1: I4 would need Aab | e + 1 with deg e ≤ max(deg a, deg b), forcing e = −1, not monic; II2 needs
f | a + c, impossible as in Lemma 2.1).
*What is affected.* (1) The definition of O(q, A) (FE2 §0.1) and every *global* statement about it away from the slices: at a
general point of R̂^* (P ≢ 1 off T) Thm 2.5 does not apply, and whether I4/II2 cover points outside all linear validity sets is
**not established here**; EVIDENCE such as the ffl_tree "uncovered density" (FE2 §0.1, FE §6.3) is an upper bound for the
ET-uncovered density (equality not known). (2) Wording: statements
"ES_q(T^k) has no finite covering" must keep the word "linear" or cite Cor 2.6. (3) Positive results (FE Thm 6.3, (J)4) are
unaffected (they exhibit coverings).

## 3. Computations (EVIDENCE; logs in `data/zi/`)

**3.1 Every solution is ET-parametrised (Lemma 1.1, FE Lemma 1.2), exhaustive.** `scripts/zi_solutions.py q k n CYL` enumerates
*all* monic solutions for every monic prime P of degree n in the T-adic cylinder CYL, without using FE Lemma 1.3: for each monic X
of degree n − k, (EY − M)(EZ − M) = M² (M = PX, E = AX − P) over all divisors of M² times all units; then every solution is
re-parametrised by the construction in the proof of Lemma 1.1 and the identities are asserted (own GF(q) tables, `scripts/zi_gf.py`;
q = 9 as F₃[i]/(i² + 1), axioms checked). No violation of Lemma 1.1 or of FE Lemma 1.2 (no second denominator of degree ≤ n − k):
| q, k, n, cylinder | primes | solutions Type I / Type II | Type I with deg E_FF ≥ n/2 | P with no solution |
|---|---|---|---|---|
| 3, 2, 6, P ≡ 1 + T (T²) | 18 | 127 / 35 | 85 | 0 |
| 3, 2, 7, P ≡ 1 + T (T²) | 50 | 570 / 155 | 307 | 0 |
| 3, 2, 7, P ≡ 1 + 2T (T²) | 54 | 725 / 328 | 209 | 0 |
| 5, 2, 4, P ≡ 1 + T (T²) | 7 | 4 / 0 | 4 | 4 |
| 9, 2, 3, P(0) = 1 | 30 | 2 / 4 | 1 | 25 |
| 9, 1, 3, P(0) = 3 (= i) | 30 | 55 / 11 | 25 | 3 |
Type I solutions with large E_FF are I4-shaped (Prop 1.4); some primes have *only* such solutions (e.g. 2 of 18 at q = 3, n = 6).
At finite n this is only illustrative (every single solution lies in *some* linear family, Prop 1.4), but it shows that the
I4 shape is common, not exotic.

**3.2 The q = 3 depth-9 tree with I4 (`scripts/zi_tree.py data/z16/balls_d9.txt 9 data/zi/census_s16.txt`, log
`data/zi/tree_d9.txt`).** Ball sets on the two c-slices, depth ≤ 9: Case A 26 balls (route_A4, complete), Case B 148 (census
`bsE_famcount 3 2 16 print`, complete; read directly — review fix: A ∩ B = 2 balls, A ∪ B = the 172 balls of O241), I4 26 (mirrors
of Case A). Missing inverses: Case B alone 0 (Lemma 2.4), A + B: 24
(the O242 observation), **A + B + I4: 0**. Of the 26 I4 balls, 24 are new as balls, but survivor counts at depths 3–9 are
identical with and without I4 (2, 6, 16, 44, 130, 380, 1130 per slice) and x*_c stays alive: **every Case A ball and every I4
ball lies inside a Case B ball** (26/26 and 26/26; `scripts/zi_AinB.py` lists, for each Case A datum, containing Case B tuples and
flags those with the *same* E: all 26 Case A data have a same-E container — this is how Lemma 2.3 was found; `data/zi/AinB_d9.txt`).
Solution-enumeration logs of §3.1: `data/zi/solutions.txt`.

**3.3 Lemmas 2.2–2.4 by brute force (`scripts/zi_slicecheck.py`, `data/zi/slicecheck.txt`).** All Case A data with g = 1 in a
degree box (a1, b1 monic coprime of degree ≤ D, E every divisor of a1 + b1 with admissible lc), ball depth ≤ DMAX. For each: the
I4 mirror re-checked against Prop 1.4; the Lemma 2.3 Case B datum built and E | D, D monic, E ≡ −1 (mod L'), g' | L', depth checked;
the Lemma 2.4 swap E' = D/E checked to give a ball containing the I4 ball.
| q, k, slices, D, DMAX | Case A data (monic E, deg ≥ 1) | Lemma 2.3 holds | outside hypotheses (α + v < k) | I4 balls in census B balls |
|---|---|---|---|---|
| 3, 2, c-slices, 6, 9 | 32 | 32 | 0 | 16 / 16 (independent census s ≤ 16) |
| 9, 1, u(0) ∉ F₃^*, 2, 12 | 12 | 12 | 0 | — |
| 5, 2, c-slices, 4, 12 | 0 | — | — | — |
| 3, 2, *all units u*, 4, 9 | 60 | 52 | 8 | — |
| 5, 2, all units, 3, 8 | 56 | 48 | 8 | — |
| 9, 2, all units, 2, 8 | 24 | 16 | 8 | — |
| 3, 3, all units, 4, 10 | 60 | 44 | 16 | — |
0 failures of Lemma 2.3 whenever its hypotheses hold. The "all units" rows show where the domination argument stops: off the
sterility slices (u(0) ≠ 1, v = 0, α = 1 < k) Case A data — and hence I4 data — exist to which Lemma 2.3 does not apply. Whether
those I4 balls are covered by other linear families is not examined (it concerns only global EVIDENCE such as ffl_tree densities,
Cor 2.6 (1)).

**3.4 Robustness without Thm 2.5 (Assessment on the certified totals).** Even if one simply added the I4 mass (= the Case A mass;
inversion preserves Haar measure and maps the slice families Σ of each theorem to themselves: c ↦ −c, resp. u₀ ↦ 1/u₀, and
P₈ = {u₀⁴ = −1} is inversion-closed) to each union bound, every certificate would still close: OA Thm 2.2: 3.195 + 1.01·0.1705
≈ 3.37 < 4; SS Thm 5.2 (q = 9, k ≥ 2): 3.577 + 1.01·0.1750 ≈ 3.75 < 8; SS Thm 3.1 (q = 27): Case A ≤ 0.0097, total far below 26;
SP Thm 3.1 (`data/fs/certify.txt`): Case A terms 0.064 (r = 4), 8.8·10⁻⁵ (r = 5), ≤ 10⁻⁵ beyond, against totals 2.18 / 0.25 /
0.37 and budgets 80 / 1 (per c) / 1; SS Thm 7.3 (k = 1, `data/fz/certify_k1.txt`): Case A 0.068 (r = 3), 2.55 (r = 4), → 2.00,
totals 9.47 / 27.6 / ≤ 15.5 against q − 3 = 24 / 78 / ≥ 240. This is a second, independent reason why no theorem breaks; Thm 2.5 is the exact one.

## 4. Answers (O244 goals)

**(1) Classification.** FE3 Lemma 1.1 (A/B dichotomy) is correct and complete for linear families; its normalisations (γ ≤ j,
removal of g, the labelling a ↔ b, monic E on the c-slices) lose no generality (§1, re-derived). The *definition* of a linear
family (fixed E = AX − P) is narrower than the ET family notion: Lemma 1.1 (ET parametrisation over F_q[T]), Cor 1.3 and Lemma 1.6
show that the F_q[T] model omits exactly two of the seven ET types, **I4** (the "Case A⁻¹" of the brief, balls u ≡ −1/E) and
**II2** (no T-adic condition). So the asymmetry of the O242 *ball list* is an artefact of the missing type I4.
**(2) Exhaustive computations.** Every solution found (q = 3, 5, 9; k = 1, 2; all primes of the tested degrees in the tested
cylinders) is Type I or II as in Lemma 1.1 (§3.1). On the slices, every ball of every ET-type family lies in a Case B ball
(q = 3 to depth 9, complete; brute-force degree boxes at q = 3, 5, 9, §§3.2–3.3). No solution and no ball outside the counted
families was found that is not dominated by a counted Case B ball.
**(3) Consequences.** On the slices where the no-covering theorems live, II2 = ∅ and I4 ⊆ Case B (Thm 2.5; for k ≥ 3: inside the
level-2 Case B covered set, which is the set the proofs bound): (J)51, (J)56, (J)67
and Conjecture 0.2 stand verbatim and extend to "no finite covering by ET-type families" (Cor 2.6); their union bounds do not
undercount (and even naive double counting of the Case A mass keeps every certificate closed, §3.4). What needs a remark:
the definition of O(q, A) and any *global* EVIDENCE about it (FE2 §0.1, ffl_tree densities): these are for linear families only.

**Why the asymmetry, in one paragraph.** By Lemma 1.1 every solution is Type II, A·abd = P + e, or Type I, A·abd = eP + 1, with
e = (a + b)/c. For fixed (a, b, e) these are the classes P ≡ −e and P ≡ −1/e (mod Aab): ET's II1 and I4, swapped by P ↦ P^{−1}.
Over ℤ both are counted, and at a prime r ∤ 4 they give M17's boxes (U) and (U⁻¹). In F_q[T] the monic condition forces lc(AX) =
lc(P) for the smallest denominator X, so II1 keeps a *bounded* E = AX − P = e and is a linear family (it is Case A), while in I4
E = AX − P = (aP + c)/b has degree n − (deg b − deg a): the ℤ ratio 4x/n = 1 + a/b ≠ 1 becomes a degree drop, and the fixed-E model
drops I4. Case B (ℤ's (P) boxes, EE' = D) is closed under inversion by itself (swap E ↔ E'), so the only mirror pair split by the
model is Case A / I4. On the sterility slices (k ≤ 2; for k ≥ 3 via level 2) the split is invisible in the covered set, because
every Case A ball with monic E sits inside a Case B ball with the same E (Lemma 2.3: E | 1 + T^{α+v}(H/b1)a1'), hence every I4 ball inside the mirror Case B ball.
