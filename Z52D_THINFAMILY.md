# Z52D_THINFAMILY — depth lane THINFAMILY (cluster C6 of RANKING_O = A09 of RANKING_A)

Status: z52d depth lane, internal. **ES is OPEN; nothing here proves ES for primes or for any new infinite family.**
Labels: PROVED / CONDITIONAL / CERTIFIED (computer) / EVIDENCE / CONJECTURE / Assessment. Internally reviewed only.
Scripts `scripts/z52d_thinfamily_*.py`, data and logs `data/z52d/thinfamily/` (< 1 MB). Run with
`ulimit -v 8000000; PYTHONPATH=scripts uv run --with sympy --with cypari2 --with gmpy2 python scripts/…`.

Cluster members: Z2969 (subspace / Corvaja–Zannier), Z3189 (recurrences for minimal certificates), Z0417, Z2995
(Niederreiter-type recursive constructions), Z2031, Z1557 (primitive / cyclotomic divisors), Z2776 (I3 exponent
coverings), Z1797 (Lean / AI prover). Cited: FRONTIER §7.8, §7.17; EXP_15; DISCOVERIES (J)84, (J)110;
paper/es-exponential-families.tex (below "the paper"); EXP_OPEN; MENU_LADDER.

## 0. Bottom line

* **Calibration (CERTIFIED).** Every actual proof certificate for 3·2^s + 1 and 63·2^s + 1 is a C-finite sequence on each
  valid residue class. Berlekamp–Massey recovers the characteristic polynomial ∏_e (X − 2^{ωTe}), with e running over the
  monomials Y^e of the coordinate, and predicts the next 10 terms exactly.
  *(EVIDENCE.)* **Minimal** certificates show no recurrence: on even s the middle coordinate y has linear complexity
  len/2. So Z3189's literal proposal (BM on minimal certificates) is void. The object to study is the *family*
  certificate.
* **The ansatz is the root-family menu (PROVED, Thm 1).** A certificate that is C-finite on a progression, with
  characteristic roots of the form 2^{rational}·(root of unity), gives a root family x, y, z ∈ ℚ[Y], Y = 2^{s/D}. Coefficients
  depending on s are allowed in the hypothesis. So the recurrence ansatz inherits every existing obstruction (the paper's
  Thm W, Cor ratio, Thm iiad3). Roots with other bases (3^s, …) are not covered.
* **New structure theorem (PROVED, Thm 2).** Consider a root family through μ = 0 of c₀·2^s + 1 (c₀ + 1 = 4^J, n irreducible)
  with moving gap and no constant ratio. If its smallest coordinate x is **irreducible** in ℚ[Y], the family lies in one of
  three explicit menus A, A′, C, each with one rational constant c. **Menu C is empty at μ = 0 (PROVED, Prop 3)**, by a
  Jacobi argument. This makes rigorous, and extends to rational constants, the one-line "Type I with (c, d) constant is
  dead" remark of EXP_OPEN (I4), which had no written proof (gcd bookkeeping, the case 2 | d).
* **Menu A (contains II-ad = (BI)) is reduced to a 2-adic approximation problem with an explicit bound (PROVED,
  Thms 4–5).** Here c = 15u^p − 1 = 2^E c_o with u ∈ ℤ odd, E ≥ 2, and **c_o ≤ 32(1 + 2^E) + (1024(1 + 2^E)² + 1)/2**.
  Hence |15u^p − 1|₂ ≪ u^{−p/3}.
  * Consequences: the u ≡ 3 (mod 8) branch (E = 2) is empty for the **whole** menu A, not only for (BI) (the paper's
    Thm iiad3 is extended).
  * For p ≥ 5 there are finitely many solutions for each p (Ridout, ineffective).
  * The large-a₁ sub-branch of EXP_15 §2.4, which EXP_15 called superelliptic, is also of this 2-adic type.
* **Menu A′ (contains I-ac), sub-case c ∈ ℤ[1/2] (PROVED reduction, Thm 7).** Here c_o ≤ 2^E + 17, or in the dyadic case
  c_num ≤ 2^e + 17 together with jj′c_num − 2^e j − 16j′ = 1.
* **CERTIFIED for 15·2^s + 1.**
  * No family in menu A, and no family in menu A′ with c ∈ ℤ (integer u), exists for any root degree D, any prime p and
    any E = v₂(c) ≤ E_max = 3000 (log summary line, §4).
  * Even u in A′ is empty by hand (Thm 7).
  * No dyadic A′ family (u or w ∈ ℤ[1/2] \ ℤ) exists for e = −v₂(c) ≤ 66, the Sophie-Germain shape included.
  * The only limit-level survivors (u = 1 and u = 1/2) are killed **for every D** by a D-independent 2-adic shape test
    (Lemma 6).
  * Positive controls: c₀ = 63 recovers exactly the data of EXP_OPEN Thm 2.3 (= paper Lemma 63class), and c₀ = 3
    recovers the c = 80 families.
* **Verdict: narrowed.** The recurrence ansatz is identified with root families. In the irreducible-x half of the
  moving-gap space, C is dead, A loses its u ≡ 3 (8) branch outright, and A and A′ (c ∈ ℤ[1/2]) are reduced to explicit
  2-adic approximation inequalities that are certified empty up to large heights. The rest survives (Ridout finiteness
  is ineffective, so "finite" does not mean "empty"):
  * reducible-x moving-gap families (II-ac, II-cd, general);
  * menu A, p = 3, beyond E_max (exponent exactly 1, no Ridout);
  * menu A, p ≥ 5, beyond E_max (finitely many for each p, ineffective, not uniform in p);
  * menu A′ with integer u beyond E_max (finitely many for each p, ineffective);
  * dyadic A′ with e > 66;
  * the A′ sub-case with odd(λ₂) > 1 (EVIDENCE only);
  * exponential certificates in other bases.
  No new all-exponent identity was found.
* 4^s + 297: the ansatz has no structural role (§5); its μ = 3 lies in the divisor class D₁₉. I3 coverings for 3^k ± 2
  were **not attempted** (time).

## 1. Statements attacked

(S1) [Z3189/Z2995] Do proof certificates of the proved families satisfy linear recurrences per class of s, and does the
template transfer to 15·2^s + 1 at s ≡ 0 (mod 60)?
(S2) [A09] Prove a new all-exponent identity for an open family (15·2^s + 1 with 60 | s; 4^s + 297), or a rigorous
obstruction to the recurrence ansatz.
Throughout: n = c₀Y^D + 1, c₀ = 4^J − 1 odd, Y = 2^{s/D}, μ = 0 the profinite unit-square point. A *root family through
μ = 0* is as in the paper (Def. 5.1): x, y, z ∈ ℚ[Y], 4xyz = n(xy + yz + zx), positive integers at Y = 2^{s/D} for all s in
C = {s ≡ 0 (mod L), s ≥ s₁}. Lemma (special) of the paper / MENU_LADDER Lemma 2.1: R ∈ ℚ[Y] is integer-valued on a
smaller such C iff R(1) ∈ ℤ[1/2] and R(0) ∈ ℤ_(2). For c₀ ∈ {3, 15, 63}, n is irreducible in ℚ[Y] for every D
(Capelli: −1/c₀ is not a p-th power for odd p, and 1/c₀ ∉ 4ℚ⁴; paper Comp. W for 15, 63).

## 2. Calibration: Berlekamp–Massey on the actual certificates (CERTIFIED) and on minimal ones (EVIDENCE)

`scripts/z52d_thinfamily_bm.py 60` (log `data/z52d/thinfamily/bm_calibration.log`). The script imports the certificates
from the paper's verifier `scripts/c1_expfam_verify.py` and adds the cubic family of EXP_OPEN Prop 2.1. The actual
certificates are: 3·2^s + 1, 4 Sophie-Germain window rules and 6 ET/divisor rules; 63·2^s + 1, the II-ad family plus 18
ET/divisor rules.
* For every rule, every valid residue class t ≡ v (mod T) of its parameter, and every coordinate, exact BM over ℚ on
  24 terms returns linear complexity L = (number of monomials of the coordinate in Y). The connection polynomial equals
  ∏_e (X − 2^{ωTe}), and the recurrence predicts 10 further terms exactly. All 3 × 39 = 117 sequences pass (14 rule-classes for 3·2^s + 1, 2 for the cubic family, 23 for 63·2^s + 1).
  Examples:
  * SG rules (Y = 2^{(s−4)/4}): L = 2, 9, 7 or 9.
  * 63-family (Y = 2^{s/3}, t ≡ 0 (mod 8)): L = (4, 4, 8).
  * ET classes polynomial in n: L ≤ 4.
  This is what the brief asked for. It is a tautology once one notes that every certificate is polynomial in a root
  Y = 2^{s/D} (Thm 1 is the converse).
* Minimal certificates of 3·2^s + 1 (least x, then least y; exhaustive window-lemma divisor search via PARI; s ≤ 60) show
  a clean dichotomy:
  * the gap is 3 for every odd s ≥ 3 and 7 for every even s ≥ 14 (for odd s the whole certificate is polynomial in n; for
    even s it is a constant-gap window m = 7 whose budget varies), so x is C-finite;
  * on even s ≥ 14 (24 terms) the coordinate y has **L = 12 = len/2**, i.e. no recurrence is detected — the budget uses
    "lottery" divisors of the factorisation;
  * on odd s, y has L = 3 (an ET class).
  (EVIDENCE.) In this range, minimal certificates are recurrent exactly where they come from an ET class.

## 3. Theorems

**Theorem 1 (recurrence ansatz = root family; PROVED).** Let s = s₀ + Lt (t ≥ t₀) with s₀ ≡ 0 (mod L). Let x_t, y_t, z_t be
positive integers solving 4/n_{s} = 1/x + 1/y + 1/z. Suppose each is an exponential polynomial Σ_j P_j(t)·ζ_j^t·2^{λ_j t}
with P_j ∈ ℚ̄[t], λ_j ∈ ℚ and roots of unity ζ_j (this is exactly "C-finite with characteristic roots in
2^ℚ·μ_∞"). Then there are D ≥ 1, L′ ∈ Lℤ, and a root family through μ = 0 (no t in
its coefficients) whose values agree with an ES solution on {s ≡ 0 (mod L′), s ≥ s₁}.
*Proof.*
0. Since s₀ ≡ 0 (mod L), reindexing t ↦ t − s₀/L makes s₀ = 0.
1. Let M be the lcm of the orders of the ζ_j and restrict to t ≡ 0 (mod M); then ζ_j^t = 1, so after grouping equal
   bases each coordinate is Σ_j P_j(t)2^{λ_j t} with distinct λ_j. Its values are rational, and the representation of a
   sequence as such a sum is unique, so applying Galois automorphisms shows P_j ∈ ℚ[t]. (The class t ≡ 0 keeps μ = 0 in
   the closure.) Choose λ > 0 such
   that every λ_j and L are integer multiples of λ, and further restrict t so that λt ∈ ℤ. With Y := 2^{λt}, each
   coordinate is Σ_{j∈ℤ} P_j(t)Y^j, and n = c₀Y^{L/λ} + 1.
2. *Negative powers vanish.* Let e clear the denominators of all P_j. Then R(t) := Σ_{j<0}P_j(t)Y^j = x_t − Σ_{j≥0}P_j(t)Y^j
   lies in (1/e)ℤ and tends to 0, so R(t) = 0 for all large t. The functions t^k2^{λjt} are linearly independent, so P_j = 0
   for j < 0.
3. *The identity.* The exponential polynomial 4xyz − n(xy + yz + zx) vanishes for all large t, so it vanishes identically.
   Since t and 2^{λt} are algebraically independent as functions, it vanishes as a polynomial in ℚ[t, Y].
4. *Specialisation.* Let P_top be the top coefficient of a coordinate. P_top(t) > 0 for large t, because the coordinate
   is positive. Choose t₁ ≡ 0 (mod e) large with all three P_top(t₁) > 0, and put G(Y) := Σ_j P_j(t₁)Y^j.
   For t ≡ t₁ (mod e): eP_j ∈ ℤ[t] gives eP_j(t) − eP_j(t₁) ∈ (t − t₁)ℤ ⊆ eℤ, so G(2^{λt}) ≡ x_t (mod 1), i.e.
   G(2^{λt}) ∈ ℤ.
5. G(2^{λt}) is positive for large t, and the identity of step 3 specialises at t = t₁. So (G_x, G_y, G_z) is a root family
   with D = L/λ on {t ≡ t₁ (mod e), t ≡ 0 (mod M·M′)} (M′ making λt integral), i.e. on s ≡ 0 (mod L·lcm(e, M, M′)),
   whose closure contains μ = 0 (t₁ ≡ 0 mod e, and s₀ = 0 by step 0).
6. On that set it is a valid ES certificate: positive integers satisfying the identity. ∎

*Scope.* Roots with other prime bases (3^t, …) or irrational algebraic roots are **not** covered. Reducing them would
need a Corvaja–Zannier-type theorem on integral values of ratios of power sums: if F(n)/G(n) ∈ ℤ infinitely often, then
P(n)F(n)/G(n) is a power sum for some polynomial P (Corvaja–Zannier, Invent. Math. 149 (2002) 431–451, verified
bibliographically). This is not done here (Assessment: the natural next step if a non-2-power certificate is ever
proposed). *Reading.* BM per class therefore detects exactly the root families. It cannot find anything that the
root-family menus of the paper/EXP_OPEN/EXP_15 miss, and every obstruction to root families (Theorem W, Cor. ratio,
Thm iiad3, and Thm 5 below) is an obstruction to the ansatz.

**Theorem 2 (structure of irreducible-x moving-gap families; PROVED).** Let (x, y, z) be a root family through μ = 0 of
n = c₀Y^D + 1 with n irreducible. Let x be its smallest coordinate (for large Y), and assume x ≠ t·n (t constant) and
f := 4x − n non-constant. If x is irreducible in ℚ[Y], then, after swapping y and z, one of the following holds with a
constant c ∈ ℚ_{>0}:
* (A) n + c = f·f′ in ℚ[Y], x = (n + f)/4, y = n(1 + f′)/4, z = nx(1 + f′)/c;
* (A′) n + c = f·f′, x = (n + f)/4, y = x f′, z = n x f′/c;
* (C) n² + c = f·f″, x = (n + f)/4, z = (n + f″)/4, y = 4nxz/c.
Conversely each shape satisfies 4/n = 1/x + 1/y + 1/z identically (direct check: e.g. in (A),
1/y + 1/z = (n + c + f)/(nx(1 + f′)) = f/(nx)).
*Proof.*
1. *Degree of x.* For large Y, n/4 < x ≤ 3n/4, so deg x = D. Since n ∤ x (else x = tn), gcd(x, n) = 1 in ℚ[Y]. Hence
   gcd(f, x) = gcd(n, x) = 1 and gcd(f, n) = gcd(4x, n) = 1, i.e. f is coprime to N := nx.
2. *Polynomial divisors.* As in the paper's Lemma reduce: write y/z = U/V with U, V coprime in ℤ[Y]; on a shrunk C the
   integer h = gcd(U(Y), V(Y)) is constant. Then d₁ := U/h and d₂ := V/h are integer-valued polynomials equal to the
   coprime parts y′, z′ of y, z. From f g y′z′ = N(y′ + z′) (g = gcd(y, z) on C) we get y′z′ | N(Y). The remainder
   argument gives d₁d₂ | N in ℚ[Y]; put d₃ := N/(d₁d₂).
3. *f divides d₁ + d₂.* g = y/d₁ ∈ ℚ(Y) takes integer values at infinitely many Y = 2^{s/D}, so g ∈ ℚ[Y] (remainder
   argument). The identity f·g = d₃(d₁ + d₂) holds at infinitely many points, hence in ℚ[Y]. By step 1, f | d₁ + d₂.
4. *Case analysis.* Since x = λ′P with P irreducible, each dᵢ = λᵢn^{εᵢ}P^{δᵢ} with Σεᵢ = Σδᵢ = 1; every dᵢ has positive
   leading coefficient. Up to d₁ ↔ d₂:
   * {λ₁, λ₂}: f | constant, excluded.
   * {λ₁ P, λ₂ n}: here d₁ + d₂ = (μ/4)(n + f) + λ₂n with μ := λ₁/λ′ > 0. Hence f | (μ/4 + λ₂)n, a positive multiple of n
     coprime to f, so f is constant, excluded.
   * {λ₁, λ₂P}: with μ = λ₂/λ′, d₁ + d₂ = (μ/4)(n + f + c) with c := 4λ₁/μ > 0. So f | n + c, and writing n + c = ff′
     gives d₁ + d₂ = (μ/4)f(1 + f′), g = λ₃n(μ/4)(1 + f′), y = gd₁ = n(1 + f′)/4 (as λ₁λ₂λ₃ = λ′), and
     z = gd₂ = nx(1 + f′)/c. This is (A).
   * {λ₁, λ₂n}: f | n + c with c := λ₁/λ₂; d₃ = (λ₃/λ′)x gives y = xf′, z = nxf′/c. This is (A′).
   * {λ₁nP, λ₂}: modulo f, 4x ≡ n, so 4(d₁ + d₂) ≡ μn² + 4λ₂ (μ := λ₁/λ′). Hence f | n² + c with c := 4λ₂/μ, and the same
     computation gives (C). ∎

*Remarks.*
(i) **Lemma 2.1 (f′ is non-constant; PROVED).** In a family of shape (A) or (A′) valid near μ = 0, f′ is not constant.
Hence n + c is reducible, and Capelli gives (1 + c)/c₀ = u^p (u ∈ ℚ_{>0}, p | D odd prime) or 4 | D and
(1 + c)/c₀ = 4w⁴.
*Proof.* Suppose f′ = κ′ is constant. Then f = (n + c)/κ′, and x, y, z ∈ ℚ[n].
1. *A residue class of n.* With m a common denominator, integrality of R ∈ ℚ[n] at n_s depends only on n_s mod m, and
   for s ≡ 0 (mod L·ord_{odd(m)}(2)), s large, n_s ≡ ρ (mod m) with ρ ≡ 4^J (mod odd(m)) and ρ ≡ 1 (mod 2^{v₂(m)}).
2. *An odd square in it.* By CRT choose an odd t with t ≡ 2^J (mod odd(m)), t² ≡ 1 (mod 2^{v₂(m)}), and t ≡ 1 modulo
   every prime of the numerators and denominators of c, κ′ not dividing m. Put n := t². Then x, y, z are positive
   integers solving 4/n = 1/x + 1/y + 1/z (positivity: n large), and gcd(n, c·κ′) = 1 for the numerators and
   denominators involved. Also gcd(x, n) = 1: from 4κ′x = (κ′ + 1)n + c, a common prime would divide c.
3. *(A).* y/n = (1 + κ′)/4 and z/n = x(1 + κ′)/c are rationals whose denominators are prime to n, and y, z ∈ ℤ, so
   y/n, z/n ∈ ℤ. Write y = nY′, z = nZ′, g = gcd(Y′, Z′), Y′ = ga, Z′ = gb. Then (4x − n)gab = x(a + b) gives
   ab | x =: abd, and (4abd − n)g = d(a + b). Since gcd(d, 4abd − n) = gcd(d, n) = 1, c_ET := g/d is an integer with
   4abc_ET d = nc_ET + a + b and gcd(abd, n) = gcd(x, n) = 1. This contradicts the paper's Lemma T1(ii).
4. *(A′).* z/n = xκ′/c ∈ ℤ as in step 3, and gcd(y, n) = gcd(κ′x, n) = 1. With g := gcd(x, y), x = ga, y = gb,
   z = nZ′, one gets nZ′(a + b) = gab(4Z′ − 1). Then ab | Z′ (as gcd(ab, n(a + b)) = 1), d := Z′/ab,
   g(4abd − 1) = nd(a + b), so d | g, and c_ET := g/d gives 4abc_ET d = n(a + b) + c_ET with gcd(c_ET, n) | gcd(x, n) = 1.
   This contradicts the paper's Lemma T1(i). ∎
(ii) In Type I/II language, (A) is II-ad = (BI) with the constants allowed rational (c = 4a²d), (A′) is I-ac, and (C) is
Type I with (c, d) constant. The menus are strictly larger than the integer-parameter menus searched before. Example:
(BI) needs odd(ad) | X + 16 and | X′ + 1 separately, while (A) needs only odd(c) | (16 + X)(1 + X′) (Lemma 4).
(iii) Reducible x is **not** covered. It contains II-ac (the cubic 3·2^s + 1 family) and the Sophie-Germain windows.

**Proposition 3 (menu C is empty at μ = 0; PROVED).** For c₀ + 1 = 4^J and s₁ ≥ 3, no family of shape (C) is valid on a
class whose closure contains μ = 0.
*Proof.* Fix a member s ∈ C (large, s ≡ 0 mod a high multiple of ord_{odd(c)}(2)) and write x, y, z, f, f″ for the
values. x, z, f, f″ = 4z − n are integers, so c = ff″ − n² ∈ ℤ_{>0}. For an odd prime q | c, n ≡ 4^J (mod q) near μ = 0,
so q ∤ n. Then q ∤ f, since q | f would give q | n². Let g := gcd(x, z), x = gx₁, z = gz₁, and w := 4gx₁z₁ − n(x₁ + z₁).
Since y = 4nxz/c, the identity reads 4/n = 1/x + 1/z + c/(4nxz). Multiplying by 4nxz gives 16xz − 4n(x + z) = c,
i.e. c = 4gw, so w > 0. Then y = 4nxz/c = ngx₁z₁/w.
1. gcd(x₁z₁, w) = gcd(x₁z₁, n): w ≡ −nz₁ (mod x₁) and gcd(x₁, z₁) = 1, and likewise for z₁.
2. gcd(x, n) = gcd(z, n) = 1: a common prime of x and n divides f = 4x − n and n, hence c = ff″ − n², contradicting
   the first paragraph; likewise for z (via f″ = 4z − n). So gcd(x₁z₁, w) = 1.
3. gcd(w, n) = 1: an (odd) prime q | w, q | n would give q | w + n(x₁ + z₁) = 4gx₁z₁, i.e. q | x or q | z, contradicting 2.
4. Hence w | g. Put d := g/w ∈ ℕ, so c = 4w²d.
For every odd prime q | f we have q ∤ c and n² ≡ −4w²d (mod q), so (−d/q) = 1 and the Jacobi symbol (−d/f) = 1. Write
d = 2^a d′ with d′ odd. Now f = 4x − n ≡ 3 (mod 4), so (−1/f) = −1.
* If a ≥ 1, then 2 | d | g | x, so 8 | 4x and f ≡ −n ≡ −1 (mod 8) (as n ≡ 1 mod 8); hence (2/f) = 1.
* Reciprocity, with (f − 1)/2 odd, gives (d′/f) = (f/d′)(−1/d′). Since d′ | d | g | x, f ≡ −n (mod d′), so
  (f/d′)(−1/d′) = (n/d′).
So (−d/f) = −(n/d′). But d′ | c is one of finitely many fixed odd numbers, and near μ = 0 we have n ≡ 4^J (mod d′), so
(n/d′) = 1 and (−d/f) = −1, a contradiction. ∎

**Lemma 4 (menu A: integrality data; PROVED).** In (A), put X := f(1), X′ := f′(1), φ₀ := f(0), φ₀′ := f′(0), F := 4^J.
Then:
1. φ₀, φ₀′ ≡ 3 (mod 4) are 2-adic units;
2. c ∈ ℤ, and c ≡ 0 (mod 4), so E := v₂(c) ≥ 2;
3. 1 + c = c₀u^p with u ∈ ℤ odd, provided c₀ is p-th-power-free (true for c₀ = 3, 15, 63); the 4w⁴ case is impossible;
4. X, X′ are positive integers with XX′ = F + c, and with c = 2^E c_o (c_o odd),
   **c_o | (F + X)(1 + X′) ⇔ c_o | X + F X′ + 2F**;
5. 2-adically v₂(1 + φ₀) + v₂(1 + φ₀′) ≥ 2 + E.
Conversely, these conditions together with the factor shape f = κP (P a monic product of a proper non-empty set of
irreducible factors of Y^D + u^p, κ > 0) are equivalent to validity near μ = 0.
*Proof.*
* x(0) = (1 + φ₀)/4 and y(0) = (1 + φ₀′)/4 lie in ℤ_(2), so φ₀, φ₀′ ≡ 3 (mod 4) are units. Their product
  B(0) = 1 + c ≡ 1 (mod 4) gives c ∈ ℤ_(2) and 4 | c.
* x(1) = (F + X)/4 and y(1) = F(1 + X′)/4 give X, X′ ∈ ℤ[1/2], so c = XX′ − F ∈ ℤ[1/2] ∩ ℤ_(2) = ℤ.
* If 1 + c = 4c₀w⁴ then v₂(1 + c) = 2 + 4v₂(w) ≠ 0, a contradiction. So u^p = (1 + c)/c₀ with u = r/v in lowest terms and
  v^p | c₀. For c₀ = 15, 63, 3 (p-th-power-free) this gives v = 1. u is odd because 1 + c is odd.
* The roots α of B = c₀(Y^D + u^p) are 2-adic units, so v₂(P(1)/P(0)) = Σ v₂(1 − α) ≥ 0. Hence v₂(X) ≥ v₂(φ₀) = 0 and
  X ∈ ℤ; likewise X′. Both are positive, since B has no root in [0, ∞).
* z(1) = F x(1)(1 + X′)/c = 4^{J−1}(F + X)(1 + X′)/c ∈ ℤ[1/2] ⇔ c_o | (F + X)(1 + X′). Also
  (F + X)(1 + X′) = 2F + FX′ + X + c. This gives item 4.
* z(0) = (1 + φ₀)(1 + φ₀′)/(4c) ∈ ℤ_(2) is item 5.
* The converse is Lemma special (positivity: κ > 0 and B has no root in [0, ∞)). ∎

**Theorem 5 (magnitude bound for menu A; PROVED).** In Lemma 4, write X + FX′ + 2F = k c_o (k ≥ 1). Then
  k²c_o ≤ Q + (Q² + 1)/2,  Q := 2F(k + 2^E);  in particular **c_o ≤ 2F(1 + 2^E) + (4F²(1 + 2^E)² + 1)/2.**
*Proof.*
1. With W := |X − FX′| we have W² = (kc_o − 2F)² − 4F·XX′ = (kc_o − 2F)² − 4F(F + 2^E c_o) = c_o(k²c_o − 4F(k + 2^E)).
2. Multiplying by k²: (kW)² = (k²c_o − 2F(k + 2^E))² − Q². Put A := k²c_o − 2F(k + 2^E); then (|A| − kW)(|A| + kW) = Q²
   with both factors positive integers.
3. Hence |A| ≤ (Q² + 1)/2, i.e. k²c_o ≤ Q + (Q² + 1)/2.
4. The right-hand side divided by k² decreases in k, so k = 1 gives the global bound. ∎

**Corollary 5.1 (PROVED, with a finite check).** For c₀ = 15 (F = 16):
(a) *The branch u ≡ 3 (mod 8) of menu A is empty for every D and every factorisation.* Here 15u^p − 1 ≡ −u − 1 ≡ 4 (mod 8),
so E = 2 and c_o ≤ 160 + (1024·25 + 1)/2 = 12960, i.e. u^p ≤ (1 + 4·12960)/15 < 3457: u ≤ 15 (p = 3), u ≤ 5 (p = 5),
u ≤ 3 (p = 7), no u ≥ 3 for p ≥ 11. With u ≡ 3 (mod 8) the candidates are (u, p) = (3, 3), (11, 3), (3, 5), (3, 7),
with c_o = 101, 4991, 911, 8201. The finite check (`z52d_thinfamily_menuA.py 15 …`, E = 2 rows; independently re-done
by the reviewer) finds no divisor pair passing item 4. (`z52d_thinfamily_binom.py` covers only D = pt, t ≤ 4, and the
paper's boxed equation only integer (a, d); neither is the proof.) This extends the
paper's Thm iiad3 from the integer-parameter menu (BI) to all of menu A (Remark iiadhyp's gap is closed for E = 2).
(b) For each E only finitely many (p, u) are possible: 15u^p ≤ 1 + 2^E·C_A(E) with C_A(E) the bound above. For E ≥ 2,
C_A(E) ≤ 811·4^E < 2^{2E+10}, so 15u^p − 1 < 2^{3E+10}, 15·3^p < 2^{3E+10} + 1, and u < (2^{3E+10}/15)^{1/p}.
Moreover u ≡ 15^{−1/p} (mod 2^E): x ↦ x^p is a bijection of (ℤ/2^E)^× for odd p. So the menu reduces to the 2-adic
approximation inequality
  |u − 15^{−1/p}|₂ = |15u^p − 1|₂ = 2^{−E} < (2^{10}/(15u^p − 1))^{1/3}   (|u − ζβ|₂ = 1 for ζ ≠ 1, EXP_15 §2.4).
For p ≥ 5 this has exponent p/3 > 1, so by Ridout's theorem (integers approximating the 2-adic algebraic number
15^{−1/p}) there are finitely many u **for each p ≥ 5**. This is ineffective and not uniform in p. **For p = 3 the
exponent is exactly 1 and the inequality has ≈ 2 solutions u per E** (u ≡ β (mod 2^E), u < 4.1·2^E, about half with
v₂ exactly E). The p = 3 part of
menu A is therefore not reduced to finiteness. It is certified only for E ≤ E_max (§4) and needs the divisibility of
item 4 beyond that. (EXP_15 §2.4's "large-a₁ sub-branch, of superelliptic type" is inside this bound: it is again a
2-adic approximation, with exponent p/3.)

**Lemma 6 (D-independent shape test; PROVED).** Let K = A/B > 0 in lowest terms and let P be a monic factor in ℚ[Y] of
Y^D + K, for any D. Then P(1)/P(0) = g(1)/ℓ_g, where g is a primitive integer factor of AZ^D + B with positive leading
coefficient ℓ_g | A and 0 < g(1) | A + B.
*Proof.*
1. If α runs over the roots of P, then P(1)/P(0) = ∏(1 − α)/(−α) = ∏(1 − β) with β = 1/α. The β are roots of
   AZ^D + B, which is primitive.
2. The monic Q := ∏(Z − β) divides it in ℚ[Z]. By Gauss, AZ^D + B = g·g′ with primitive integer g = ℓ_gQ. So
   ℓ_gℓ_{g′} = A and g(1)g′(1) = A + B, and ∏(1 − β) = Q(1) = g(1)/ℓ_g.
3. Q(1) > 0, because the real roots of Z^D + B/A are negative or absent. ∎
In all menus φ₀ = f(0) = X·P(0)/P(1), so φ₀ ranges over the finite set {X ℓ/g₁ : ℓ | A, g₁ | A + B} for **every** D. A
limit-level solution (X, X′) for which no element of this set satisfies the Y = 0 conditions is dead for all root degrees
at once. (For integer u: A = u^p, B = 1.)

**Theorem 7 (menu A′ with c ∈ ℤ[1/2]; PROVED reduction).**
(Here c = λ₁/λ₂ in lowest terms, with d₁ = λ₁ and d₂ = λ₂n; c ∈ ℤ[1/2] ⇔ odd(λ₂) = 1. Since x(0) ∈ ℤ_(2), φ₀ ≡ 3 (mod 4)
is a unit, as in Lemma 4. If c ∈ ℤ[1/2] then u (resp. w) has no odd denominator: writing u = r/v, odd(v)^p | 15 forces
odd(v) = 1, and likewise odd(v)⁴ | 15.)
* *Odd integer u (c ∈ ℤ, so λ₂ = 1).* Write c = 15u^p − 1 = 2^E c_o (c₀ = 15, F = 16).
  1. y(1) = (16 + X)X′/4 with X′ = (16 + c)/X, and gcd(odd(X), 16 + X) = 1, give odd(X) | 16 + c, so X′ ∈ ℤ[1/2]. φ₀′ =
     15u^p/φ₀ is a 2-adic unit (u odd), and the roots of B are 2-adic units, so as in Lemma 4, X, X′ ∈ ℤ_{>0}.
  2. Integrality of z(1) = 4(16 + X)X′/c gives c_o | (16 + X)X′ ≡ 16(X′ + 1) (mod c_o), so c_o | X′ + 1. Then XX′ ≡ 16
     forces X ≡ −16, so X = jc_o − 16 and X′ = j′c_o − 1 with j, j′ ≥ 1.
  3. Expanding gives **jj′c_o = 2^E + j + 16j′, so c_o ≤ 2^E + 17**, i.e. 15u^p − 1 ≤ 2^E(2^E + 17), and
     |15u^p − 1|₂ = 2^{−E} ≪ u^{−p/2}. This is a 2-adic approximation with exponent p/2 > 1, so for each p there are
     finitely many solutions (Ridout, ineffective), **p = 3 included**.
* *Even integer u = 2^k u′ (k ≥ 1; reviewer's argument, checked).* Then c = 15u^p − 1 is odd and the roots of B have
  v₂(α) = pk/D > 0.
  1. For a proper factor P, v₂(X) = −t with t = pk·deg P/D ∈ [1, pk − 1], and v₂(X′) = t; φ₀ is a unit.
  2. z(1) gives c | X′ + 1 and X ≡ −16 (mod c), so X′ = j′c − 1 and 2^tX = jc − 2^{4+t}.
  3. Expanding (2^tX)X′ = 2^t(16 + c) gives jj′c = j + 2^{4+t}j′ + 2^t, so c ≤ 1 + 17·2^t ≤ 1 + 8.5·2^{pk}.
  4. But c ≥ 15·2^{pk} − 1. Contradiction, so even u is empty.
  Even w in the Sophie-Germain shape is the same with t ≤ 1 + 4k: c ≤ 1 + 34·16^k < 60·16^k − 1.
* *Sophie-Germain shape with odd integer w* (1 + c = 60w⁴, c = 60w⁴ − 1 odd, 4 | D).
  1. The roots α of Y^D + 4w⁴ have v₂(α) = 2/D, so v₂(X) = −2·deg P/D. This is an integer, so for a proper factor P,
     deg P = D/2 and v₂(X) = −1. (The values a ∈ {0, −2} in the enumeration below correspond to f or f′ constant, which
     is excluded; they are kept only as a harmless superset.)
  2. With a := v₂(X): X′ = j′c − 1 and 2^{|a|}X = jc − 2^{4+|a|} (for a = 0: X = jc − 16).
  3. Expanding: jj′c = j + 2^{4+|a|}j′ + 2^{|a|}, so c ≤ 69 and w = 1, c = 59. Then (59j − 64)(59j′ − 1) = 300 (|a| = 2),
     (59j − 32)(59j′ − 1) = 150 (|a| = 1), resp. c ≤ 18 (a = 0) have no solutions with j, j′ ≥ 1.
  So this case is empty (by hand; the general-A′ search of Computation 8(d) also covers it).
* *Dyadic u = r/2^i (i ≥ 1), or the Sophie-Germain case 1 + c = 60w⁴, w = r/2^i.* Put e := v₂(c^{−1}) (= ip, resp.
  4i − 2) and c_num := 2^e c, odd.
  1. x(0) ∈ ℤ_(2) makes φ₀ a unit, so v₂(φ₀′) = −e.
  2. The roots of B have negative valuation, so v₂(X) = 0 and v₂(X′) = −e. Hence X″ := 2^eX′ is an odd integer and
     XX″ = 2^{e+4} + c_num.
  3. z(1) ∈ ℤ[1/2] gives c_num | X″ + 2^e and X ≡ −16, so X = jc_num − 16, X″ = j′c_num − 2^e and
     **jj′c_num − 2^e j − 16j′ = 1**. In particular c_num ≤ 2^e + 17, i.e. 2^e < 15r^p ≤ 2^{e+1} + 17.
  4. y(0) ∈ ℤ_(2) needs v₂(1 + φ₀) ≥ e + 2. ∎
(The sub-case odd(λ₂) > 1 of (A′), c = λ₁/λ₂ with an odd denominator, is not reduced here; §4, Computation 8(d).)

## 4. Computations (exact commands; all exact integer/rational arithmetic)

**Computation 8.**
(a) `z52d_thinfamily_menuA.py 15 3000` (log `menuA_15_E3000.log`, final summary line; CERTIFIED for E ≤ 3000). It enumerates every (E, p, u): u ≡ 15^{−1/p} (mod 2^E), 15u^p ≤ 1 + 2^E·C_A(E), v₂(15u^p − 1) = E. For
each it tests menu A by Theorem 5:
* small N: all divisors of N;
* otherwise: all k ≤ k_max(E, c_o), each tested by an exact perfect-square check.
Menu A′ (odd integer u) is tested by the j′-loop of Theorem 7. Even u is excluded by hand (Theorem 7). Every limit hit
then goes through the D-independent test of Lemma 6 (ℓ = ℓ_g > 0, g₁ = g(1) > 0). The k-loop was cross-checked against
direct divisor enumeration on 2400 (c₀, u, p) cases (c₀ ∈ {3, 15, 63, 255}, u < 400, p ≤ 7; `z52d_thinfamily_xcheck.py`,
log `xcheck.log`): 0 mismatches. The reviewer repeated this independently on 1200 cases (0 mismatches). **Result for c₀ = 15: the only limit-level hits are u = 1 (c = 14, X = 5, X′ = 6;
listed for p = 3, 5, but u = 1 is p-independent). Lemma 6 kills them for every D: (A) needs φ₀φ₀′ = 15 with both
≡ 3 (mod 4), impossible; (A′) fails the test as well.** Hence no menu-A family and no A′ family with integer u exists for
c₀ = 15, any D and any p, for E up to the logged bound.
Positive controls (`menuA_63_E400.log`, `menuA_3_E400.log`, E ≤ 400, run with the final shape test; the later
incremental-lift speed-up of the residue computation reproduces the same summary lines):
* c₀ = 63: exactly one hit, (E, p, u, c, X, X′) = (2, 3, 3, 1700, 21, 84) = the data of EXP_OPEN Thm 2.3, and it passes
  Lemma 6 (e.g. (g₁, ℓ) = (7, 9));
* c₀ = 3: c = 80 (u = 3, p = 3) survives Lemma 6 in A for X ∈ {1, 6, 21} and in A′ for X = 21 (EXP_OPEN Map 2.4: II-ad,
  I-ac hits for (3, 1)); the u = 1 hits are killed for both A and A′.
(b) `z52d_thinfamily_dyadic.py 66` (log `dyadic_E66.log`; CERTIFIED): menu A′ with u = r/2^i or w = r/2^i, all odd p
and the Sophie-Germain shape, e ≤ 66. 451 713 (p, i, r) windows were tested. There is one limit-level hit (p = 3,
u = 1/2, c = 7/8, X = 5, X′ = 27/8); Lemma 6 kills it for every D (by hand: P(1)/P(0) = g(1) ∈ {1, 3, 9}, while the
conditions need φ₀ = 5/g(1) ≡ −1 (mod 32)).
(c) `z52d_thinfamily_binom.py 15 7 200 1,2,3,4 2` (log `binom_15.log`; EVIDENCE cross-check with explicit factor
shapes, D = pt, t ≤ 4, p ≤ 7, u = r/2^i, i ≤ 2): 152 928 tests, 0 hits. Controls: `… 63 5 30 1,2 0`
(`binom_63_control.log`) gives the EXP_OPEN Thm 2.3 family at D = 3, 6, and `… 3 7 40 1,2 1` (`binom_3_control.log`)
gives the c = 80 family.
(d) `z52d_thinfamily_Ap.py 15 20 30 13` (log `Ap_general_15.log`; EVIDENCE): general (A′) with c = λ₁/λ₂ (any coprime
λ's), K = (r/v)^p or 4(r/v)⁴, r, v ≤ 20, λ₂ multiplier ≤ 30, p ≤ 13. 1064 pairs (λ₁, λ₂) gave 0 hits under the
D-independent test. Controls (`Ap_general_3_control.log`, `Ap_general_63_control.log`, r, v, t ≤ 12, p ≤ 7): c₀ = 3
gives the c = 80 cubic hit and an SG hit (K = 4, c = 11); c₀ = 63 gives none (as expected: its family is in menu A).

## 5. 4^s + 297 and 3^k ± 2

* 4^s + 297 (Assessment, with PROVED ingredients cited). Here μ = 3 is a non-unit square point, but μ = 3 itself lies in
  the divisor class D₁₉ (4³ + 297 = 19², ord₁₉ 4 = 9, so 19 | n for s ≡ 3 (mod 9)). By MENU_LADDER Thm 6.2 (compactness) a
  finite certificate exists iff every point of the exponent closure lies in some ET, divisor or root class. The uncovered
  region of all trees is near the 3-line X_{3,3} (EXP_NEAR_SQUARE §2 certifies ET coverage of the whole line). Root
  families add only supply there; they give no structural escape. So the recurrence ansatz has nothing specific to offer
  for 4^s + 297. Its status stays "supply problem" (EXP_OPEN §4). Not attempted further.
* I3 exponent coverings for 3^k ± 2 (Z2776): **not attempted** (time box spent on §3–4).

## 6. Verdict for the cluster: **narrowed**

* Sub-route killed:
  * "BM on minimal certificates" (Z3189 as posed): minimal certificates are lottery objects (§2).
  * Menu C (Prop 3), at every D.
  * The u ≡ 3 (8) branch of the whole menu A (Cor 5.1(a)).
* Sub-routes reduced to explicit inequalities, with certified emptiness up to large heights:
  * menu A (certified for E ≤ 3000; beyond: p ≥ 5 Ridout-finite per p, p = 3 open);
  * menu A′ with c ∈ ℤ[1/2] (integer u: certified for E ≤ 3000, beyond Ridout-finite per p, all p; even u empty;
    dyadic: certified for e ≤ 66).
* Surviving (where a positive theorem for 15·2^s + 1 must live, if anywhere; Ridout finiteness is ineffective, so the
  "finite" items are not excluded):
  1. moving-gap root families whose smallest coordinate is **reducible** in ℚ[Y] (II-ac, II-cd-type and general; the
     cubic II-ac escape of 3·2^s + 1 lives here);
  2. menu A, p = 3 (3 | D), with v₂(15u³ − 1) > 3000;
  3. menu A, p ≥ 5, with E > 3000 (finitely many per p, not effective);
  4. menu A′, odd integer u, E > 3000 (finitely many per p, not effective);
  5. dyadic A′, e > 66;
  6. A′ with odd(λ₂) > 1;
  7. certificates using other exponential bases.
* The "recursion escapes the finite-covering no-go" premise of the ranking is correct only in the trivial sense that
  every rule polynomial in a root is a recursion. The recursion ansatz is not a new menu.

## 7. Proposed FRONTIER §7.8 text (do not edit FRONTIER from here)

> 8. **Thin families still open:** 15·2^s + 1 (60 | s), 4^s + 297, 4^s + 33, 4^s + 273. *(z52d THINFAMILY.)*
> * A C-finite certificate in 2-power roots is a root family (PROVED), so recurrence fitting is not a new menu.
> * For 15·2^s + 1 at μ = 0, every moving-gap root family with irreducible smallest coordinate is in menu A (⊇ II-ad),
>   A′ (⊇ I-ac) or C (Type I, (c, d) const). C is empty (PROVED).
> * A satisfies c_o ≤ 32(1 + 2^E) + (1024(1 + 2^E)² + 1)/2 (PROVED). Hence the u ≡ 3 (8) branch is empty for all of A.
>   Beyond the certified range, every p ≥ 5 is Ridout-finite (ineffective) and p = 3 reduces to a 2-adic approximation
>   of exponent 1.
> * Certified empty, for all p and all D (D-independent shape lemma): A and A′ with integer u for v₂(c) ≤ 3000; A′ with
>   u ∈ ℤ[1/2] \ ℤ for −v₂(c) ≤ 66.
> * Open: reducible-x moving-gap families (II-ac/II-cd/general); A and A′ (integer u) beyond v₂(c) = 3000 (p = 3 in A
>   not even finite); dyadic A′ beyond 66; A′ with odd(λ₂) > 1 (EVIDENCE only); non-2-power exponential certificates.
> * 4^s + 297 is a covering-supply problem (μ = 3 ∈ D₁₉); roots add only supply.
> *Why:* concrete; the only setting where forced budgets beat every ET covering.

## 8. Review

Hostile review by a fresh subagent: `reviews/z52d-thinfamily-review.md`. Result: no FATAL defect; 4 MAJOR and 13 MINOR
defects. The reviewer re-verified Thm 1, Thm 2 (all 9 placements), Prop 3, Lemma 4, Thm 5, Cor 5.1 (all numbers), Lemma 6
and Thm 7 for odd u, and re-ran the scripts. Repairs:
* M1 (certified range not supported by the committed log): the E ≤ 3000 run was restarted with the final code and
  completed; the committed log ends with its summary line (§4).
* M2 (survivor lists treated Ridout-finite and bounded-certified items as dead): the lists in §0, §6 and §7 now include
  A for p ≥ 5 beyond E = 3000, A′ with integer u beyond 3000, and dyadic A′ beyond e = 66.
* M3 (even u and even w in A′ untreated): added to Thm 7, with the reviewer's argument (checked).
* M4 (Remark (i) used odd-square results outside their scope): replaced by Lemma 2.1 with a direct reduction to the
  paper's Lemma T1(i)/(ii).
* Minor repairs:
  * m1: 39 rule-classes, not 43.
  * m2: labels and wording of the minimal-certificate claims.
  * m3: Thm 1 precision (Galois step, class t ≡ 0, modulus).
  * m4: ≈ 2 solutions per E.
  * m5: the "also covered" claim in Cor 5.1(a) is qualified, and the candidates are listed.
  * m6: Sophie-Germain typo and the a ∈ {0, −2} remark.
  * m7: two implicit steps of Thm 7.
  * m8: the script's shape test is now exactly Lemma 6 (ℓ > 0), and the controls were re-run and committed.
  * m9: the cross-check script and the control logs are committed.
  * m10: references and numbering.
  * m11: the binom cache key.
  * m12: "repairs" became "makes rigorous".
  * m13: the hypothesis of Lemma 4 item 3.
