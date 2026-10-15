# EXP_OPEN — the hardest open exponential families: 15·2^s + 1 and 4^s + 297 / 33 / 273 (task O246)

Status: O246 checkpoint in progress. **ES is not solved here, nor any infinite case of it unless stated with a complete
proof and a replayed certificate.** Labels as in DISCOVERIES.md. Scripts `scripts/z19_*`, data `data/z19/`.
Builds on EXP_105 (O239: Prop 2.4–Cor 2.8), MENU_STERILITY (O240: Prop 4.1, 4.3), MENU_LADDER (O245: Lemma 2.1, CONJ 6.4).

## 0. Iteration log
(I1) 15·2^s + 1 = (15·4^t + 1) ∪ (30·4^t + 1). The odd half 30·4^t + 1 has no unit-square point (EXP_NEAR_SQUARE Lemma 3.1,
c₀ ≡ 2 mod 4) and is covered by ET/divisor classes at L = 60 (`z15_tree.py 30 1 2 60 60 100000 2 1 3`: residual ∅;
EVIDENCE until a certificate is written, §5). So everything sits at μ = 0 of 15·4^t + 1.
(I2) Construction-first attempt on the reviewers' gaps of Cor 2.8 (split SG numerators, mixed sub-products, other
Aurifeuillean / higher-root factorisations, composite m, Type I windows). Instead of enumerating shapes, I looked at the
*limit* of an arbitrary constant-gap family at μ = 0. All these gaps are instances of one menu ("some denominator x has
4x − n constant, y and z arbitrary polynomials in a root of 2^s"), and a 2-adic Newton-polygon bound on the limit values
makes the magnitude argument of Cor 2.8 work for *every* divisor in that menu. Outcome: Theorem W (§1) — the whole
constant-gap menu is PROVED sterile at μ = 0 for (15,1), (31,33), (7,57), (63,1), (47,17), (55,9), while the same
finite check recovers exactly the known escapes of (3,1), (7,9), (23,41), (39,25) (positive controls). This is a
negative result for the menu; it steers constructions to *moving-gap* families (§2).

## 1. Theorem W: constant-gap families never reach μ = 0

Setting. c₀ odd, k ≡ 1 (mod 8), c₀ + k = 4^J (J ≥ 1), n_s = c₀2^s + k, μ = 0 the profinite unit-square point. A *root
family through μ = 0* is: D ≥ 1, a clopen neighbourhood C = {s ≡ 0 (mod L), s ≥ s₀} (D | L), and x, y, z ∈ ℚ[Y] with
4/n = 1/x + 1/y + 1/z identically, n = c₀Y^D + k, all three positive integers at Y = 2^{s/D} for every s ∈ C. (Every
exponential-polynomial identity near μ = 0 has this form after reparametrisation; a shift Y ↦ 2^{−r/D}Y with D | r is
absorbed.) It has *constant gap m* if 4x − n = m ∈ ℤ (constant), and *constant ratio t* if x = t·n, t ∈ ℕ.
Recall MENU_LADDER Lemma 2.1: R ∈ ℚ[Y] is integer-valued on (a smaller) C iff R(1) ∈ ℤ[1/2] and R(0) ∈ ℤ_(2).

**Lemma 1.1 (reduction to polynomial divisors; PROVED).** Given a constant-gap family, put N = n·x ∈ ℚ[Y]. After
shrinking C there are d₁, d₂ ∈ ℚ[Y], integer-valued and positive on C, with d₁d₂ | N in ℚ[Y] and m | d₁ + d₂ on C.
*Proof.* m/N = 1/y + 1/z. For s ∈ C let g = gcd(y, z), y = gy′, z = gz′: mgy′z′ = N(y′ + z′) and gcd(y′z′, y′ + z′) = 1
give y′z′ | N and m | (N/y′z′)(y′ + z′). Near μ = 0, Y ≡ 1 (mod m) so N ≡ N(1) = 4^{J−1}(4^J + m) (mod m), coprime to
m; hence m | y′ + z′. Write y/z = U/V with U, V ∈ ℤ[Y] coprime in ℚ[Y]; then y′ = κU(Y)/h(s) with κ ∈ ℚ fixed and
h(s) | Res(U, V)·(content), and h(s) depends only on Y modulo a fixed integer; on a smaller neighbourhood (Y ≡ 1 at the odd
part, Y ≡ 0 at the 2-part) h is constant. So d₁ := y′, d₂ := z′ are polynomials in Y. Finally d₁d₂ | N(Y) for infinitely
many Y = 2^t forces d₁d₂ | N in ℚ[Y]: N = Q·d₁d₂ + R with deg R < deg d₁d₂, R/(d₁d₂) ∈ (1/den)ℤ tends to 0, so R(2^t) = 0
infinitely often. ∎ (This is Rav's criterion for m/N = 1/y + 1/z made uniform; it contains every z14 window, every
fixed-prime split of any piece, every sub-product mixing pieces, the n-atom, and every algebraic factorisation.)

**Lemma 1.2 (Jacobi at the limit; PROVED; generalises EXP_105 Prop 2.4 and MENU_STERILITY Prop 4.1).** Write
ρᵢ := dᵢ(1) = 2^{eᵢ}aᵢ (i = 1, 2) and ρ₃ := d₃(1) with d₃ := N/(d₁d₂). Then ρᵢ > 0, aᵢ odd, a₁a₂a₃ = M := 4^J + m,
m | ρ₁ + ρ₂ in ℤ[1/2], and necessarily **m ≡ 3 (mod 8) and e₁ − e₂ odd.**
*Proof.* Positivity: n and n + m = c₀Y^D + k + m have no root in (0, ∞), so every factor of N with positive leading
coefficient is positive at Y = 1; d₁, d₂, d₃ have positive leading coefficient (positive on C). ρ₁ρ₂ρ₃ = N(1) =
4^{J−1}M, all ρᵢ ∈ ℤ[1/2] (Lemma 2.1) give the factorisation of the odd part. Y ≡ 1 (mod m) on a neighbourhood gives
m | ρ₁ + ρ₂. n ≡ k ≡ 1 (mod 4) forces m = 4x − n ≡ 3 (mod 4). Every prime q | M has −m ≡ 4^J (mod q), so
(m/q) = (−1/q) and (q/m) = (m/q)(−1)^{(q−1)/2} = 1; hence (aᵢ/m) = 1, and ρ₁ ≡ −ρ₂ gives (2/m)^{e₁−e₂} = (−1/m) = −1. ∎

**Lemma 1.3 (2-adic size of the limits; PROVED).** Assume m ≡ 3 (mod 8). Then each dᵢ(0) is a 2-adic unit and
  eᵢ = −2δᵢ + νᵢ, δᵢ := deg(dᵢ, x-part)/D ∈ [0, 1], νᵢ ≥ 0, ν₁ + ν₂ + ν₃ = 2J,
where dᵢ = λᵢ·(product of irreducible factors of x)·(product of irreducible factors of n), δᵢ is the degree fraction of its
x-part and νᵢ := v₂(n-part(1)/n-part(0)). If n is irreducible in ℚ[Y], νᵢ ∈ {0, 2J}.
*Proof.* N(0) = k(k + m)/4 and k + m ≡ 4 (mod 8), so N(0) is a 2-adic unit; the dᵢ(0) ∈ ℤ_(2) multiply to it, so each is a
unit and eᵢ = v₂(dᵢ(1)/dᵢ(0)), independent of λᵢ. For a monic factor P: P(1)/P(0) = ∏_α (1 − α)/(−α) over its roots in
ℚ̄₂. Roots of n + m: α^D = −(k + m)/c₀, v₂(α) = 2/D > 0, so each contributes v₂(1 − α) − v₂(α) = −2/D. Roots of n:
α^D = −k/c₀, v₂(α) = 0, contribution v₂(1 − α) ≥ 0, total v₂(n(1)/n(0)) = v₂(4^J/k) = 2J. ∎

**Lemma 1.4 (Capelli at the 2-adic place; PROVED).** If x = (c₀Y^D + k + m)/4 has a monic factor product of degree
exactly D/2 over ℚ (needed below), then 4 | D and m = 4c₀β⁴ − k with β ∈ ℚ, v₂(β) = 0; if c₀ is 4th-power-free,
β = w ∈ ℤ odd, i.e. **m = 4c₀w⁴ − k** (O239's 'sg1' windows).
*Proof.* x is then reducible, so by Capelli −K := −(k + m)/c₀ is a p-th power (p | D prime) or lies in −4ℚ⁴ (4 | D).
K > 0 rules out p = 2; v₂(K) = 2 (m ≡ 3 mod 8) rules out odd p (p ∤ 2). So K = 4β⁴, v₂(β) = 0; β = w/u in lowest terms
gives u⁴ | c₀. ∎

**Lemma 1.5 (magnitude; PROVED).** Let e := |e₁ − e₂| ≤ E and r := M/m. Then
  m ≤ B := max(2^E·4^J + 2^{2E+2}r², 2^E·4r² + 4^J).
*Proof.* WLOG e₁ ≥ e₂; u := 2^e a₁, v := a₂ satisfy u + v = jm (j ≥ 1, positivity). If u ≥ v then a₁ ≥ m/2^{e+1},
a₂a₃ = M/a₁ ≤ 2^{e+1}r, and multiplying u ≡ −v by a₂a₃ gives m | 2^eM + a₂²a₃ ≡ 2^e4^J + a₂²a₃ (M ≡ 4^J), a positive
integer ≤ 2^E4^J + 2^{2E+2}r². If v > u then a₂ > m/2, a₁a₃ ≤ 2r, and multiplying by a₁a₃ gives m | 2^e a₁²a₃ + 4^J ≤
2^E·4r² + 4^J. ∎

**Theorem W (constant-gap sterility at μ = 0; PROVED, finite check `scripts/z19_thmW.py`).** Let c₀ be odd and
4th-power-free, k ≡ 1 (mod 8), c₀ + k = 4^J, and c₀Y^D + k irreducible in ℚ[Y] for all D (Capelli: k/c₀ is not ± a
p-th power for odd p, and not 4β⁴ — true for all pairs below). A constant-gap root family through μ = 0 exists only if
for some odd w with m = 4c₀w⁴ − k ∈ (0, B] there are a₁a₂ | M and (δ₁, δ₂, n-placement) with δᵢ ∈ {0, ½, 1},
δ₁ + δ₂ ≤ 1, n in at most one of d₁, d₂, such that m | 2^{e₁}a₁ + 2^{e₂}a₂ in ℤ[1/2] (eᵢ as in Lemma 1.3, E = 2J + 2).
*Proof.* Lemma 1.1–1.3: νᵢ ∈ {0, 2J} are even, so eᵢ ∈ ℤ forces 2δᵢ ∈ ℤ (δᵢ ∈ {0, ½, 1}), and e₁ − e₂ odd forces some 2δᵢ odd, i.e. a sub-product of the factors of
x of degree exactly D/2; Lemma 1.4 gives m = 4c₀w⁴ − k; Lemma 1.5 bounds m. ∎
**Computation 1.6 (CERTIFIED by exhaustive enumeration, `z19_thmW.py c₀ k`).**
* **(15, 1), (31, 33), (7, 57), (63, 1), (47, 17), (55, 9): no limit-level relation** (w ≤ 3, 5, 9, 5, 5, 5 resp. up to the
  bound; (7, 57) has only m = −29 < 0 at w = 1). Hence **no constant-gap root family of any degree D reaches μ = 0.**
* Positive controls: (3, 1) → m = 11 only; (7, 9) → m = 19 only; (23, 41) → m = 51 only; (39, 25) → m = 131 only — exactly
  the known Sophie-Germain escapes (MENU_STERILITY Thm B/C, EXP_105 Thm 2.6, Obs 2.1), e.g. (7, 9): ρ₁ = 7, ρ₂ = 5/2.

**Corollary 1.7 (constant ratio; PROVED).** Under the hypotheses of Theorem W no root family with x = t·n (t ∈ ℕ fixed)
reaches μ = 0. *Proof.* As in Lemma 1.1 with ε := 4t − 1 ≡ 3 (mod 4) and N = tn: d₁d₂ | tn, ε | d₁ + d₂. Limits:
ρᵢ = λᵢ·4^{J·[n | dᵢ]} with λᵢ | t (n irreducible). Odd q | t: ε ≡ −1 (mod q) gives (q/ε) = 1; if 2 | t then ε ≡ 7 (mod 8)
and (2/ε) = 1; if t is odd no odd power of 2 occurs. So (ρ₁ρ₂/ε) = 1 ≠ (−1/ε). ∎

**Scope (exact).** Theorem W + Cor 1.7 close every reviewers' gap of EXP_105 Cor 2.8 *at once*: split SG numerators,
sub-products mixing primes of both SG factors, Aurifeuillean splittings of Φ_n-pieces, quintic/sextic/any root windows,
composite windows m, the n-atom, and Type-I-shaped windows (x/n constant), for every root degree D. Hence:
**15·2^s + 1 (and 31·4^s + 33, 7·4^s + 57, 63·4^s + 1, 47·4^s + 17, 55·4^s + 9) has no finite covering by ET classes,
divisor classes and constant-gap / constant-ratio exponential classes of any degree** (compactness as in EXP_105 Cor 2.8;
the 30·4^t + 1 half is irrelevant there since μ = 0 lies in the even half). NOT covered: families in which no denominator
has constant gap or ratio (all of 4x − n, 4y − n, 4z − n non-constant and none of x, y, z a constant multiple of n), i.e.
MENU_LADDER's general T, T′ normal form with T′ non-constant. CONJECTURE 6.4 is reduced to these *moving-gap* families.

## 2. Moving-gap families: the binomial menu (II-ac) — a new cubic escape for 3·2^s + 1, none for 15·2^s + 1

(I3) Theorem W leaves the moving-gap families. The cheapest ones are again *binomial*: in Type II
(x, y, z) = (abd, acdn, bcdn), cn = 4abcd − a − b, the identity cn + a = b·(4acd − 1) shows that **with a, c constant**
the witness f = 4acd − 1 is a polynomial factor of the binomial c·c₀Y^D + (ck + a); the gap m = (a + b)/c moves (b is a
polynomial). Call this menu (II-ac) (its mirror (II-bc) is the same with a ↔ b). Capelli: the binomial is reducible iff
K := (ck + a)/(cc₀) ∈ ℚ^p (p | D odd prime) or K ∈ 4ℚ⁴ (4 | D), i.e. a = c′(c₀u^p − kv^p), c = c′v^p (resp.
a = c′(4c₀u⁴ − kv⁴), c = c′v⁴). By Lemma 2.1 of MENU_LADDER the family f = κP (P a monic factor product) is valid near
μ = 0 iff d = (f + 1)/(4ac) and b = (cn + a)/f are integral at Y = 1 (ℤ[1/2]) and Y = 0 (ℤ_(2)); positivity is automatic
(P has no positive root). Test (exact, `scripts/z19_iiac.py`): v₂(κ) is forced by f(0) ∈ ℤ_(2)^×, so v₂(f(1)) = e is forced,
and the odd part w of f(1) must satisfy w ≡ −2^{−e} (mod q), q = odd(a)·odd(c), w | odd(c·4^J + a) — a short arithmetic
progression, no factoring needed.

**Proposition 2.1 (a cubic-root family through the unit-square point of 3·2^s + 1; PROVED, verified exactly).**
For s ≡ 0 (mod 36), s ≥ 18, put Y = 2^{s/3}, n = 3Y³ + 1 = 3·2^s + 1, a = 80, c = 1,
  d = (21Y + 64)/320, b = (Y² − 3Y + 9)/7, x = abd, y = acdn, z = bcdn.
Then 4/n = 1/x + 1/y + 1/z. *Proof.* cn + a = 3(Y³ + 27) = 3(Y + 3)(Y² − 3Y + 9) and 4acd − 1 = 21(Y + 3), so
cn + a = b(4acd − 1), which is the Type II identity. Integrality: 320 | 21Y + 64 iff 64 | Y and Y ≡ 1 (mod 5), i.e.
s/3 ≥ 6 and 4 | s/3; 7 | Y² − 3Y + 9 iff Y ≡ 1 (mod 7), i.e. 3 | s/3. Positivity is clear. (Checked numerically for
s = 36, 72, …, 180.) ∎
*Significance.* The class s ≡ 0 (mod 36) contains μ = 0, the profinite unit-square point of 3·2^s + 1, and the family has
moving gap 4x − n = a + b = 80 + (Y² − 3Y + 9)/7 and root degree D = 3. So (i) the cubic rung of MENU_LADDER's ladder is
NOT sterile at a unit-square point (for (3, 1)); (ii) the escape uses a *cyclotomic* factor Y + 3 of Y³ + 3³ — the shape
that EXP_105 Prop 2.7 / Theorem W prove useless for constant-gap windows — because the fixed modulus is now 4ac = 320 and
the 2-adic condition reads f(0) = 63 ≡ −1 (mod 64) while f(1) = 84 ≡ −1 (mod 5). It is a second, independent mechanism
beside the Sophie-Germain window m = 11 (MENU_STERILITY Theorem B).

**Computation 2.2 (EVIDENCE, `z19_iiac.py c₀ k 10⁸ 60 13 1,2 10`: c′ ≤ 60, u, v ≤ 10, p ≤ 13 and SG, D ∈ {e, 2e}).**
(3, 1): exactly the family of Prop 2.1 (and its D = 6 reparametrisation). (7, 9): none. **(15, 1): none.**

(I4) All two-constant *binomial menus* (`scripts/z19_binom.py`, replay `scripts/z19_binom_verify.py`). Fixing two of
(a, b, c, d) in cn = 4abcd − a − b (Type II) or (a + b)n = c(4abd − 1) (Type I, x = abdn, y = acd, z = bcd) leaves
either an ET class / constant gap (Thm W) / constant ratio (Cor 1.7) / Type I with (c, d) constant (dead at μ = 0: the
witness character (−d/·) is evaluated at −n → −(unit square)), or one of four menus in which a witness f is a polynomial
factor of a binomial B and two parameters are fixed by congruences modulo a FIXED modulus:
| menu | constants | binomial B | congruences (mod Mod) |
|---|---|---|---|
| II-ac | a, c | cn + a | f = 4acd − 1 ≡ −1 (4ac) |
| II-ad | a, d | n + 4a²d | f = 4abd − n (the gap) ≡ −n, B/f = 4acd − 1 ≡ −1 (4ad) |
| I-ac | a, c | an + c | f = 4acd − n ≡ −n (4ac) |
| II-cd | c, d | 4c²dn + 1 | f, B/f ≡ −1 (4cd) |
In every menu f(0) is a 2-adic unit, so the same progression test applies. Positive controls and results (c′/a ≤ 40,
u, v ≤ 10, p ≤ 13 and SG, D ∈ {e, 2e}; every hit replayed by `z19_binom_verify.py` on s = Dj, j ≤ 240–400):
* (3, 1): hits in II-ac, II-ad, I-ac (cyclotomic Y³ + 27 and SG pieces), e.g. Prop 2.1.
* (39, 25): I-ac hits (SG, (a, c) = (1, 131)). (7, 9), (23, 41), (31, 33), (7, 57): none.
* **(63, 1): II-ad hit (a, d) = (5, 17), D = 3** — see Theorem 2.3. **(15, 1): none.**

**Theorem 2.3 (a moving-gap family through the unit-square point of 63·2^s + 1; PROVED, elementary; replayed).**
For s ≡ 0 (mod 24), s ≥ 6, put Y = 2^{s/3}, n = 63Y³ + 1 = 63·2^s + 1, a = 5, d = 17 and
  b = (63Y³ + 3Y² − 9Y + 28)/340,  c = (21Y + 64)/340,  x = abd, y = acdn, z = bcdn.
Then 4/n = 1/x + 1/y + 1/z with x, y, z positive integers.
*Proof.* n + 4a²d = 63Y³ + 1701 = 63(Y + 3)(Y² − 3Y + 9). Put f = 3(Y² − 3Y + 9), f′ = 21(Y + 3), so ff′ = n + 1700.
Then 4abd − n = 340b − n = f and 4acd − 1 = 340c − 1 = 21Y + 63 = f′, so (4abd − n)(4acd − 1) = n + 4a²d; since
(4abd − n)(4acd − 1) = 4ad(4abcd − b − cn) + n, this is c·n = 4abcd − a − b (Type II identity). Integrality: 340 = 4·5·17;
Y ≡ 0 (4), and Y ≡ 1 (mod 5) and (mod 17) iff 4 | s/3 and 8 | s/3; then 21Y + 64 ≡ 85 ≡ 0 and
63Y³ + 3Y² − 9Y + 28 ≡ 85 ≡ 0 (mod 5·17), both ≡ 0 (mod 4). Positivity is clear. ∎ (`z19_binom_verify.py 63 1 II-ad 5 17 3
"Y**2-3*Y+9" 3 400`: identity and integrality verified at all j = s/3 ≡ 0 (mod 8), j ≤ 400.)
*Significance (SHARP).* 63·2^s + 1 is one of the families PROVED (EXPONENT_COVERING Cor 1.5) to have no ET/divisor
covering, and Theorem W (and O239 Cor 2.8) prove that no constant-gap / window class reaches its unit-square point
μ = 0. The class s ≡ 0 (mod 24) above contains μ = 0. So **a moving-gap, cubic-root, cyclotomic (Y³ + 3³) Type II
class dissolves a unit-square point that every window provably misses.** The gap 4x − n = 3(Y² − 3Y + 9) is itself the
cyclotomic factor. Whether 63·2^s + 1 is fully coverable (ET + windows + this class) is the next step (§3).

## 3. ES for every 63·2^s + 1

**Theorem 3.1 (PROVED, computer-assisted; certificate `data/z19/cert63_et.json`, independent checker
`scripts/z19_cert63_check.py`).** For every s ≥ 0, 4/(63·2^s + 1) is a sum of three unit fractions.
*Proof.* (a) s ≡ 0 (mod 24), s ≥ 24: Theorem 2.3. (b) Every other residue s mod 2520 (s ≥ 10) lies in one of 18
ET/divisor classes (moduli 5, 11, 15, 19, 29, 39, 87, 119, 127, 344, 584, 1016, 5620, 51944), each a polynomial
identity in n on a residue class n ≡ r (mod M) whose odd part has ord(2) | 2520 (built by `z19_cert_make.py 63 2520
300000 … 24 0`, the O240 machinery; ET/divisor classes alone leave exactly s ≡ 0 mod 2520, `z15_tree.py 63 1 1 2520 …`).
(c) s ≤ 9: brute force. The checker verifies every identity symbolically, integer-valuedness on each class (forward
differences), positivity (Cauchy bound below 63·2^10), the period, integrality of Theorem 2.3's b, c on s ≡ 0 (mod 24)
over a full period of 2^{s/3} mod 340, coverage of all residues mod 2520, that no non-divisor ET class contains an odd
square (T1 control), and an explicit verified solution for every s ≤ 1000 (950 ET, 41 moving class, 10 brute). ∎
*Scope / honesty.* A thin family. It is the first family with a profinite unit-square point **that no window / constant-gap
class can reach (Theorem W) and that is nevertheless closed** — the closing class is a moving-gap Type II family from the
binomial menu II-ad. T1 respected: the integer square 63·2^8 + 1 = 127² lies in the divisor class D₁₂₇ (s ≡ 1 mod 7) and
is solved by brute force anyway (s < 10). Literature: not searched yet for this specific family (the campaign's prior web
searches found no ES result for any k·2^m + 1 family; non-exhaustive).

**Map 2.4 (EVIDENCE; `z19_binom.py c₀ k MENU 30 8 7 1,2` for every c₀ ≡ 7 (mod 8), k = 4^J − c₀ ≡ 1 (mod 8), J ≤ 4).**
Families with a profinite unit-square point and a binomial-menu class through it: (3, 1) [II-ac, II-ad, I-ac],
(15, 49) [II-ac SG (a, c) = (11, 1); I-ac cubic (a, c) = (8, 13)], (39, 25) [I-ac SG], (63, 1) [II-ad cubic],
(55, 201) [II-ac SG]. None found (at this small range) for (7, 9), **(15, 1)**, (7, 57), (23, 41), (31, 33), (47, 17),
(55, 9) and all other J = 4 pairs. (Hits are necessary-and-sufficient for validity near μ = 0; each was spot-replayed.)

**Reduction 2.5 (II-ad at the limit; PROVED algebra, used as a fast EVIDENCE filter `scripts/z19_iiad_limit.py`).** In
II-ad, B = n + T, T = 4a²d, the roots of B are 2-adic units, so v₂(f(1)/f(0)) ≥ 0 and X := f(1), X′ := f′(1) are
positive integers with X ≡ −4^J, X′ ≡ −1 (mod q), q = odd(a)·odd(d), XX′ = 4^J + T. Writing X = jq − 4^J,
X′ = j′q − 1, a = 2^α a₁, d = 2^δ d₁, E = 2 + 2α + δ: **jj′a₁d₁ = 2^E a₁ + j + 4^J j′**, and Capelli needs
(k + T)/c₀ ∈ ℚ^p ∪ 4ℚ⁴. For j = j′ = 1, k = 1, c₀ = 4^J − 1 this reads c₀(u^p − z) = (1 + z)², z = 2^E a₁: the (63, 1)
class is z = 20 (u³ = 20 + 21²/63 = 27). Enumeration E ≤ 40, a₁ ≤ 2001, j, j′ ≤ 60: (63, 1) → only Theorem 2.3's data;
(3, 1) → T = 80 (Prop-2.1-type); (7, 9) → one limit candidate T = 180 that fails the factor-shape test; **(15, 1) → no
limit candidate at all.** (A proof for all (E, a₁, j, j′) would need the exponential-Diophantine equations
(k + T(E))/c₀ = u^p; not attempted.)
