# Z53_WILDCARD — from-scratch attack on the tied divisor event

**ES is OPEN; nothing here claims it proved or disproved.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Status: **final (hostile review applied, §6)**. Lane rule: ideas generated before reading
FRONTIER §§3–4, §6; the barrier check comes in §4 below.

## 0. The statement attacked

(★) For a prime p ≡ 1 (mod 24) find positive integers u, B, C with p = 4uBC − u − B; equivalently (PROVED, trivial)
any one of
* ∃ C and d | 4Cp+1 with d ≡ −1 (mod 4C);
* ∃ u and d | p+u with d ≡ −1 (mod 4u) (then B = (p+u)/d, C = (d+1)/(4u));
* ∃ coprime u,B with u | p+B, B | p+u and 2^{2+v₂(uB)} | p+u+B;
* ∃ d ≡ 3 (4) such that ρ_p(d) := (−p mod d) ∈ [1,d−1] divides (d+1)/4.

Necessary condition (PROVED, 5 lines, §2.1): any such d has (d/p) = −1. For n = q² an odd square every candidate
fails because (−u/d) = −1 for every d ≡ −1 (4u) while every divisor of q²+u has (−u/d)=+1 (this is the T1 wall
restated; proof in §2.1).

## 1. Idea list (generated from scratch, before reading FRONTIER §§3–4/§6)

Each with a first concrete test. (Status filled in later sections.)

1. **Full Type II family, not only (★).** Deriving Mordell/Elsholtz–Tao Type II from scratch gives
   hp = 4ahkC − a − k (h,a,k,C ≥ 1); (★) is h = 1. Equivalent forms (PROVED §2.2): ∃ a,h: hp+a has a divisor
   ≡ −1 (mod 4ah); ∃ a,C: p+4a²C has a divisor ≡ −1 (mod 4aC); ∃ g, h|g: 4ghp+1 has a divisor ≡ −1 (mod 4g);
   ∃ t ≡ 3 (4), a,b with ab | (p+t)/4 and t | a+b. Expected count ≍ log³p (heuristic; vs log²p for (★)); the modulus of the
   divisor condition is relaxed from 4u to u/a when a² | u/4 (e.g. p+4a² needs only a divisor ≡ −1 mod 4a).
   Test: which p ≡ 1 (24) (and which non-squares n) have Type II but no (★); compare minimal parameters.
2. **Type I family** tp+1 = 4abC with t | a+b (derived §2.3); a=1 slice: (tp+1)/4 has a divisor ≡ −1 (mod t).
   Dual to Type II a=1 slice ((p+t)/4 has a divisor ≡ −1 mod t). Test: same census.
3. **Characterise the (★)/Type-II exceptional set among non-squares.** If the only n ≡ 1 (24) without Type II are
   squares, primality is used only through non-squareness; otherwise the extra exceptions show exactly what a proof
   must use. Test: census (done to 2·10⁵, §3.1).
4. **r-spectrum R(n) = {r : rn+1 has a divisor ≡ −1 (mod r)}** (r=1,2,3 always for odd n; (★) ⟺ R(p) ∩ 4ℤ ≠ ∅; for squares
   R(q²) ∩ 4ℤ = ∅, PROVED §2.1 — but odd r ≡ 3 (4) can occur at squares via even divisors, e.g. 3 ∈ R(25)). Test for a composition law / multiplicative structure on R(n) numerically.
5. **Covering-system view**: the APs {n ≡ −(u+B) mod 4uB} must cover all primes ≡ 1 (24); large sieve with
   non-CRT targets on composite moduli — compare with Vaughan/Elsholtz exceptional-set bounds (density only;
   expected dead for individual p, but check whether the half-dimensional structure (d/p) = −1 adds anything).
6. **Genus/ray-class reformulation**: d | 4Cp+1 ↔ ideal divisors of (1+2√(−Cp)); condition d ≡ −1 (4C) is a ray
   class condition, (d/p) = −1 a genus condition. Test whether anything beyond genus theory is captured.
7. **Polynomial identities in a quadratic-form parametrisation of p** (forms outside the principal genus never take
   square values, so T1 does not forbid them a priori). PROVED dead by degree count for ℚ-irreducible Q on full-rank cosets (Prop 2.4): only congruence menus; rank-1 cosets are the thin families.
8. **Mutual-divisibility graph / Vieta-type moves**: u | p+B, B | p+u. Checked: no Vieta jump (equation linear in
   each variable); the ratio r = (p+u+B)/(uB) classifies edges; a (★) certificate is an edge with 4 | r.
9. **Sierpiński/Proth slice** C = 2^j: p·2^{j+2}+1 needs a divisor ≡ −1 (mod 2^{j+2}). Test numerically whether
   this slice alone always succeeds for small p (expected not).
10. **Davenport-constant / zero-sum argument** on the multiset of prime residues of p+u in (ℤ/4u)*: only bites when
    ω(p+u) ≳ |G|; fails for typical u. Noted, not pursued.
11. **Probabilistic/LLL, Chevalley–Warning, circle method, modular forms**: all reduce to counting with error ≫ log²p
    or give mod-p information without size control. Dead on first inspection (reasons in §2.5).

## 2. Derivations (elementary; §§2.1–2.4 PROVED with the stated scopes, §2.5 Assessment)

### 2.1 The Jacobi obstruction and the forced non-residue

**Lemma 2.1.** Let u ≥ 1 and d odd with d ≡ −1 (mod 4u). Then the Kronecker–Jacobi symbol (−u/d) = −1.
*Proof.* d ≡ 3 (4) gives (−1/d) = −1. Write u = 2^a u′, u′ odd. Quadratic reciprocity for the odd coprime pair
(u′, d) with d ≡ 3 (4): (u′/d) = (d/u′)(−1)^{(u′−1)/2} = (−1/u′)(−1)^{(u′−1)/2} = 1. If a ≥ 1 then 4u ≡ 0 (8) so
d ≡ 7 (8) and (2/d) = 1. Hence (−u/d) = (−1/d)(2/d)^a(u′/d) = −1. ∎

**Corollary 2.2 (T1 at the level of one event).** For an odd square n = q² and any u ≥ 1, q²+u has no divisor
d ≡ −1 (mod 4u): every prime ℓ | d has (−u/ℓ) = +1 (ℓ | q²+u, and ℓ ∤ q since ℓ | q ⇒ ℓ | u, while gcd(d,u) = 1; so −u ≡ q² is a
nonzero square mod ℓ), hence (−u/d) = +1 for every divisor d of q²+u coprime to 2u, contradicting Lemma 2.1. For a prime p ≡ 1 (4) and d | p+u, d ≡ −1 (4u): (p/d) = (−u/d) = −1, and
by reciprocity (d/p) = (p/d), so **(d/p) = −1**: every certifying divisor is a quadratic non-residue mod p. (This is
FRONTIER Lemma CT / `PARITY_AUDIT` Lemma 3.2, re-derived.)

### 2.2 The full Type II family, from scratch

Let p be prime, p ∤ x, and 4/p = 1/x + 1/(py′) + 1/(pz′). Clearing denominators: x(4y′z′ − y′ − z′) = p y′z′. Put
g = gcd(y′, z′), y′ = ga, z′ = gb, gcd(a,b) = 1: x(4gab − a − b) = p g ab. Since gcd(ab, 4gab − a − b) = gcd(ab, a+b) = 1,
ab | x; x = ab x″ gives x″(4gab − a − b) = pg. The case p | x″ is impossible (then 4gab − a − b ≤ g, false for
a, b, g ≥ 1). So 4gab − a − b = p·h with x″h = g, i.e. **h | g**. Writing g = hC:

  **(II)  hp = 4ahbC − a − b,   a, b, h, C ≥ 1**,   solution 4/p = 1/(abC) + 1/(p·hbC) + 1/(p·haC).

(Check: (hp + a + b)/(p·habC) = 4ahbC/(p·habC) = 4/p.) (★) is h = 1. Equivalent divisor forms, each a two-line
substitution using 4ahC ≡ 1 (mod d) for d = 4ahC − 1:
* (II-i)  ∃ a, h: hp + a has a divisor d ≡ −1 (mod 4ah)          [d = 4ahC − 1, b = (hp+a)/d];
* (II-ii) ∃ a, C: p + 4a²C has a divisor d ≡ −1 (mod 4aC)        [since h^{−1} ≡ 4aC, hp + a ≡ h(p + 4a²C)];
* (II-iii) ∃ g, h | g: 4ghp + 1 has a divisor d ≡ −1 (mod 4g)      [(4ga − 1)(4gb − 1) = 4ghp + 1];
* (II-iv) ∃ t ≡ 3 (4), a, b: ab | (p+t)/4 and t | a + b           [t := (a+b)/h, C := (p+t)/(4ab)];
* (II-v)  ∃ d ≡ 3 (4), h | (d+1)/4 with h·ρ_{h}(d) | (d+1)/4, where ρ_h(d) := (−hp mod d) ∈ [1, d−1]
          [a = ρ_h(d) is forced because a ≤ (d+1)/(4h) < d].

**Two consequences worth stating.** (a) On shifts u = 4a²C the required modulus drops from 4u ((★)) to u/a:
"p + 4a² has a divisor ≡ −1 (mod 4a)" already certifies ES (C = 1, (II-ii)); e.g. p = 73: 77 = 7·11, 7 ≡ −1 (4),
h = 2, b = 21, 4/73 = 1/21 + 1/146 + 1/3066. (b) The square obstruction persists for every h: with n = q², d | hq² + a and
d ≡ −1 (4ah) give (−ah/d) = +1 for every divisor, while Lemma 2.1 (applied to u = ah) gives (−ah/d) = −1. So no
h-layer escapes T1, and for prime p every certifying d again has (d/p) = −1.
Expected size (heuristic, Assessment): Elsholtz–Tao prove Σ_{p≤N} f_II(p) ≍ N log²N, i.e. the full family has ≍ log³p
solutions *on average* over primes, against ≍ log²p for the h = 1 line (FRONTIER §2.2). No fixed-p statement follows
(B6). (An earlier attempt here to derive log³p from a "one of each divisor pair" cut-off was wrong — at p = 73 the
certificate (a,b,C,h) = (2,5,2,1) has both certifying divisors above √(hp+a) — and has been removed.)
In the repository this family is ET Type II; the a = 1 slice of (II-ii) is López's b = 1 line (`B1_LINE.md`). Nothing
in 2.2 is new to the campaign; it is recorded because the lane required an independent derivation.

### 2.3 Type I, from scratch

4/p = 1/(px′) + 1/y + 1/z with p ∤ yz: yz(4x′ − 1) = px′(y + z). With g = gcd(y,z), y = gy₁, z = gz₁: y₁z₁ | x′,
x′ = y₁z₁x₂, and x₂ | g, g = x₂g₁, leaving g₁(4y₁z₁x₂ − 1) = p(y₁ + z₁). p ∤ g₁ (else 4y₁z₁x₂ − 1 ≤ y₁ + z₁, impossible),
so **(I)  tp = 4abC − 1 with t | a + b** (t := (4y₁z₁x₂ − 1)/p, a = y₁, b = z₁, C = x₂). Divisor form: ∃ a, C: 4Ca² + 1 has a
divisor t ≡ −p^{−1} (mod 4aC). The a = 1 slices of (I) and (II-iv) are dual: (tp+1)/4 resp. (p+t)/4 has a divisor ≡ −1
(mod t), t ≡ 3 (4); the divisor may be even (p = 73, t = 7: 20 | 20; p = 97, t = 7: 34 | 170). Type I is obstructed at
odd squares by ET Prop 1.6 (FRONTIER B5); the Lemma 2.1 argument covers (II) for every h via (II-i) (§2.2(b)) but is
*not* claimed for Type I here. *(Not pursued further; it is ET Type I.)*

### 2.4 No polynomial identity in a quadratic-form parametrisation (degree count)

**Proposition 2.4 (PROVED, scoped).** Let Q ∈ ℚ[x,y] be a binary quadratic form irreducible over ℚ (every positive
definite form; every indefinite form of non-square discriminant), Λ ⊂ ℤ² a coset of a *full-rank* sublattice, and
C, u, B ∈ ℚ[x,y] **nonzero** polynomials taking positive integer values on Λ with Q(x,y) = 4C·u·B − u − B for all
(x,y) ∈ Λ. Then two of C, u, B are constants (positive integers C₀, u₀, B₀), and the identity is the congruence
Q ≡ −(u₀+B₀) (mod 4u₀B₀) (resp. Q ≡ −u₀ (mod 4u₀C₀ − 1), Q ≡ −B₀ (mod 4B₀C₀ − 1)) on Λ — a fixed congruence menu (B1).
*Proof.* A full-rank coset is Zariski dense in 𝔸², so the identity holds in ℚ[x,y]. Since C, u, B ≠ 0, deg(4CuB) =
deg C + deg u + deg B. If at least two of the three are nonconstant, this exceeds both deg u and deg B, so deg Q =
deg C + deg u + deg B = 2: exactly two factors are linear and one is a nonzero constant, and the top-degree part of Q is
(constant)·(linear)·(linear), a factorisation of Q over ℚ — contradicting irreducibility. (Three nonconstant factors give
degree ≥ 3.) Hence at least two of C, u, B are constant; the third is then a quadratic polynomial determined by Q and the
two constants, and its taking integer values on Λ is exactly the displayed congruence (the constants are positive
integers as values on Λ). ∎
(The nonzero hypothesis is essential: with C = 0, u = x³, B = −x³ − x² − y² the identity holds for Q = x² + y² with only
C constant — reviewer's example; positivity on Λ excludes it.)
*Scope remarks.* (i) On a rank-1 coset (a line x = x₀ + kt, y = y₀ + kt′) identities do exist: e.g. on
(x,y) = (63 + 96k, 1), Q = x² − 8y², u = 8, B = x, C = (x+1)/32 gives Q = 4CuB − u − B (reviewer's example; at x = 735,
Q = 540217 is a prime ≡ 1 (24)). These are the thin families p = φ(k) of FRONTIER (J)84 / §3 B1 (polynomial budgets at a
general prime need a relation p = φ(u)), not identities over the form. (ii) Positivity and integrality are not used in the
degree count; they only shape the menu. (iii) The conclusion holds regardless of the genus of Q: a form outside the
principal genus never takes square values (primitively or not), so T1 alone would not have excluded such an identity —
the degree count does, unconditionally. Noted because the "non-principal genus escapes T1" thought is tempting.

### 2.5 One-line dismissals (Assessment, not theorems)
* Chevalley–Warning / polynomial method mod p: produce solutions of 4uBC ≡ u + B (mod p) with no size control; the size
  condition uBC < p/2 is the whole problem.
* Probabilistic method / LLL: no random object is available; the natural randomisation is the count R(p) itself, whose
  mean ≍ log²p is known and whose lower tail is the question.
* Circle method on 4uBC − u − B = p: three variables, cubic; the expected main term is ≍ log²p, below every known
  minor-arc saving (B3 regime).
* Modular forms: Σ_n R_t(n)qⁿ is a Lambert/Appell-type series, not holomorphic modular (FRONTIER §2.3 already has the
  exact theta-quotient form); no exact formula with a positive main term is known.
* Vieta jumping on 4uBC − u − B = p: linear in each variable, so no single-variable Vieta involution (FRONTIER (J)89
  Cor 4.2 for Type I).
* Davenport/zero-sum on the residues of the prime factors of p + u in (ℤ/4u)*: standard zero-sum results concern the
  identity, not the target −1, and need sequence length comparable to the group order, while ω(p+u) is typically
  log log p ≪ φ(4u).

## 3. Computations (CERTIFIED in the stated ranges; scripts `scripts/z53_wildcard_*`, data `data/z53/wildcard/`)

### 3.1 Census of the three families, n ≡ 1 (mod 24), n ≤ 2·10⁵ (`z53_wildcard_census.c`, 8 s)
`gcc -O2 scripts/z53_wildcard_census.c -lm; ./a.out 200000 300 > data/z53/wildcard/census_2e5.txt`.
Range 25 ≤ n ≤ 2·10⁵, n ≡ 1 (24) (8 333 values). (★) and the positive algebraic family (II) are enumerated exactly (bounded
loops: ak ≤ (N+a+k)/4, h | a+k); a seventh column flags (II) solutions with gcd(n, akC) = 1 (ET's Type II coprimality,
automatic at primes: p | akC with n = p forces (a+k)/h ≡ 0 (mod p) and akC ≥ p, hence a + k ≥ (a+k)/h = 4akC − p ≥ 3p,
while 4ak ≤ 4akC = p + (a+k)/h ≤ p + a + k gives 3(a+k) ≤ p + 4 — contradiction for p ≥ 5). Type I is enumerated with the WLOG a ≤ b and the
restriction a ≤ 300 (so "no Type I" below means none with min(a,b) ≤ 300 — a partial census).
* 189 have no (★); 148 have no (II); 153 have no coprime (II); 148 have no Type I (a ≤ 300); 148 have neither (II) nor Type I.
* The 148 are **exactly the odd squares ≡ 1 (24) in range** (checked list equality). The 5 extra coprime-(II) failures
  are the composites 1705, 3985, 4585, 6265, 12145 (all 5·(…); 3985 is FRONTIER §7.14's example), whose only (II)
  solutions share a factor with n — ES holds there by scaling, but strict ET Type II does not. So in this range the
  exceptional set of the family (II) among n ≡ 1 (24) is precisely the squares (T1 is sharp), while (★) has 41 further
  non-square failures: 7 primes — 409, 577, 5569, 9601, 23929, 83449, 102001 — and 34 composites (1345, 1465, 1969, …).
  The 7 primes are exactly FRONTIER §4 item 14's list in this range (independent reproduction, independent code).
* Brute-force cross-check in Python (all (u,B) with 4uB − u − B ≤ p): R(409) = R(577) = R(5569) = 0, while e.g.
  409 = 4·1·13·8 − (1+13)/2 (h = 2), 577 = 4·1·5·29 − (1+5)/2.

### 3.2 Type II counts at the (★)-hard primes versus neighbours (`z53_wildcard_counts.c`; 1.5 + 8 min)
For each p: R(p) = #{(u,B): u ≤ B, 4uB | p+u+B}; N_II = #{(a,k,h): a ≤ k, h | a+k, 4ak | p+(a+k)/h}; N_a1 = the a = 1 slice;
N_h2 = the h = 2 layer. Hard primes (`counts_hard.out`) and the six next primes ≡ 1 (24) after each (`counts_ctrl.out`):

| p (hard) | R | N_II | N_a1 | N_h2 | neighbours' N_II (six primes ≡ 1 (24) above p) |
|---|---|---|---|---|---|
| 409 | 0 | 7 | 4 | 4 | 10, 7, 7(=577), 7, 5, 9 |
| 577 | 0 | 7 | 7 | 4 | 7, 5, 9, 12, 8, 12 |
| 5569 | 0 | 10 | 7 | 3 | 11, 16, 26, 27, 12, 20 |
| 9601 | 0 | 7 | 2 | 4 | 15, 21, 36, 21, 34, 38 |
| 23929 | 0 | 39 | 15 | 6 | 37, 39, 13, 38, 36, 33 |
| 83449 | 0 | 15 | 4 | 2 | 71, 29, 37, 30, 45, 51 |
| 102001 | 0 | 21 | 9 | 0 | 63, 70, 42, 36, 53, 42 |
| 329617 | 0 | 30 | 11 | 5 | 61, 75, 48, 83, 64, 60 |
| 712321 | 0 | 32 | 5 | 8 | 83, 74, 58, 64, 61, 72 |

Near-square controls (p = m² + k ≡ 1 (24), k ≤ 64, m ≈ 300–335; `counts_nearsq.out`): (p, R, N_II) = (91873, 11, 45),
(94273, 6, 27), (99241, 10, 44), (99289, 9, 39), (105649, 12, 43), (106993, 9, 64), (112249, 12, 39) — ordinary values at
this scale (the near-square deficit of (J)53/(J)55 is a few σ on averages, not visible on seven primes).

EVIDENCE: at 6 of the 9 hard primes (5569, 9601, 83449, 102001, 329617, 712321) the *aggregate* count N_II is at or below
the minimum of its six neighbours; the exceptions are 409, 577 (N_II = 7 vs a neighbour with 5) and 23929 (39 vs 13).
This is an aggregate statement: individual layers need not be depressed (at 712321 the h = 2 layer has N_h2 = 8, tied
for the maximum among its neighbours' 8, 5, 6, 6, 6, 5), and nothing here excludes complementarity at the rare zeros.
It is consistent with `BM_CORRECTED_COUNT.md` §4 (residuals of (★) and the b = 1 line positively correlated overall;
union count/main-term minima at 83449 (p ≡ 1 (4) sample) and 317209 (p ≡ 1 (24) sample)). Reading (Assessment): the hard primes tend
to be poor in aggregate. This statistic does not test complementarity of *zero* events (all nine have N_II > 0) and
supports no claim about what widening the family does or does not buy.

## 4. Barrier check against FRONTIER §§3–4, §6 (read only after §§1–3 were fixed)

For each idea: which barrier, whether its scope really covers the idea, and what (if anything) is left.

| # | idea | barrier / existing item | scope really covers it? | residue |
|---|---|---|---|---|
| 1 | full Type II (II), log³p mean, modulus u/a on shifts 4a²C | It *is* ET Type II; the a = 1 slice is López's b = 1 line (`B1_LINE.md`, `BM_CORRECTED_COUNT.md` §4, Prop 4.1(a): Brauer character χ_{−4ab} on the whole family). B2 (tied modulus 4ah with the integer hp + a), T1 for every h (§2.2(b)), B6 for the log³ average (ET). | Only partly. B2's conditional impossibility is for a *fixed finite* menu and explicitly exempts growing p-dependent families; T1 kills square-blind steps only; B6 forbids inference from averages only. None excludes a prime-specific mechanism on the full family. | **Unexcluded, undeveloped.** No such mechanism was supplied here; the family is ET's, so the novelty is nil, but "not a route" is not a theorem. |
| 2 | Type I | ET Type I; same barriers; (J)89 Lemma 4.1 (positive Type I slices have (d/p) = −1). | Same as row 1: the cited items constrain, they do not exclude. | **Unexcluded, not advanced here.** |
| 3 | exceptional set = squares? | T1 (B5) is exact: f_I(m²) = f_II(m²) = 0 (ET Prop 1.6); the converse at primes to 10⁸ is FRONTIER §1 (f_II(p) ≥ 1); §3.1 adds the composite n ≡ 1 (24) ≤ 2·10⁵ for the family (II) (scaling a prime's solution gives a non-coprime (II) solution, so this needed computing). | No kill involved: T1 proves squares fail; it does not address a converse. | **Open reformulation**: CONJECTURE (consistent with §3.1): every non-square n ≡ 1 (24) is in the family (II); with ET coprimality the five composites of §3.1 are genuine exceptions. Primality enters only through non-squareness *at the level of the obstruction*; a proof must still produce a class, not a parity (checklist 9). |
| 4 | r-spectrum R(n) = labels of the forest F_n | The forest (J)106/(J)83, bichromatic ⟺ certificate, composition "adds reachability, never existence" ((J)82), fixed roots/bounded windows dead under Dickson. | **No.** (J)82 (`LATTICE_MEETING.md` §§1.3, 2.1–2.3) is about downward propagation with fixed (k,d) and controlled lifts in split-slice lattices, not about every closure/selection law on R(p); its Cor 1.5 explicitly does not exclude class data guiding produced norms. A numerical look (R(409) ∩ [1,40] = {1,2,3,6,11,14,15}, R(577) ∩ [1,40] = {1,2,3,5,7,9,10,18,21,35,39}, no multiple of 4) showed no obvious pattern, which is not a no-go. | **Unexcluded, undeveloped.** Note: since (★) is false at 409, any structural law on R(p) can only serve ES through a broader family or by handling the 14 known failures separately. |
| 5 | covering-system / large sieve with non-CRT targets | B6 (Vaughan 1970, Elsholtz–Tao exceptional sets ≪ N exp(−c(log N)^{2/3})); §7.12 (exponent θ > 3/4) is the live averaged target, already audited (`BREADTH_Z45.md` §§15–16: CRT architectures capped at 3/4). | Yes; and the targets {−(u+B) mod 4uB} are genuinely non-CRT, which is the audited "non-CRT" gap. | Nothing beyond §7.12, which has its own lanes. |
| 6 | genus / ray-class reformulation | §2.2 (BM = one Kronecker character per pair), §7.3 (class inside the coset), CLASS_FORCING Thm 2.1 (no reciprocity law adds information about [N] ∈ (ℤ/t)*). | **No.** CLASS_FORCING Thm 2.1 concerns characters of the *total product* [N] on a fixed line; it does not eliminate joint constraints on divisors, nor the varying fields Q(√(−Cp)) and their ray class groups. ("Only p-dependent part is parity" was an unproved claim, withdrawn.) Pure genus/parity repackaging is blocked (§2.2, §7.3); the full investigation is not. | **Unexcluded, undeveloped**; overlaps §7.3/§7.6 and the GENUS lanes. |
| 7 | polynomial identities over a non-principal-genus form | Prop 2.4 (nonzero polynomial C, u, B with positive integer values, ℚ-irreducible Q, full-rank coset) plus B1 for the resulting menus. | Yes, within that scope (own proof). | **Excluded in scope** (PROVED). Says nothing about rational functions, thin loci (rank-1 cosets = (J)84 thin families) or non-polynomial choices. |
| 8 | mutual-divisibility pairs / Vieta | Forest F_p (FRONTIER §7.2); equation linear in each variable, so no single-variable Vieta involution; (J)89 Cor 4.2 (square-class-preserving moves). | For the single-variable Vieta proposal, yes. Multivariable graph moves / global existence arguments on F_p are not excluded (they are §7.2's open item). | Single-variable Vieta: unavailable. Rest: **open, belongs to §7.2**. |
| 9 | Proth slice C = 2^j | Direct: p = 409 has no (★) certificate at all (§3.1), so no 2-power slice; "2-group levels alone do not suffice" (§3, Stickelberger item). | Yes (the universal slice is false). | **Dead as a universal slice** (CERTIFIED at 409). |
| 10 | Davenport / zero-sum on prime residues | Plain zero-sum results target the identity, not −1 (many identity residues still fail); the length needed is a Davenport-type constant of (ℤ/4u)*, not literally the group order. §7.6 (full-factor-multiset realisation) is the open form. | Plain cardinality forcing: yes. Arithmetic information on the full multiset: no. | **Reduces to §7.6 (open).** |
| 11 | probabilistic / polynomial / circle / modular | §2.5 (Assessment); B3 leaves polylog main terms with small errors open. | Only the naive applications sketched; no exclusion of the methods. | **Not developed**; nothing supplied here. |

**Screens for the best survivor (idea 1, full Type II as the target statement).** T1: passes (vanishes at squares for
every h, §2.2(b)); 8/131: the same family for numerator 8 fails at 131 and 241 (`BM_CORRECTED_COUNT.md` §4), so any argument
must use 4 — not supplied; tied modulus: fails (modulus 4ah tied to the integer hp + a; relaxing to u/a on square-multiple
shifts changes the constant, not the tie); fixed p: fails (only averaged inputs known). So idea 1 is **not a route**; it is
the same wall with a log³p mean.

**False-kill audit (after cross-model review).** The first version of this table declared every idea dead; the review
showed that was unsupported for ideas 1–4, 6, 8, 11 (barriers cited out of scope). Corrected status: *excluded in scope*
— 7 (Prop 2.4), 9 (409); *reduces to an existing open item* — 5 (§7.12), 8-graph (§7.2), 10 (§7.6); *unexcluded and
undeveloped* — 1, 2, 3 (as a conjecture), 4, 6, 11. None of the unexcluded ideas comes with an argument here; the
honest statement is that this lane did not find a kill for them, not that they lead anywhere.

### 4.1 One small PROVED addition: privacy extends to the whole Type II family

**Lemma 4.1.** For primitive pairs (h, a) ≠ (h′, a′) (gcd(h,a) = gcd(h′,a′) = 1) with h, h′ ≤ H, a, a′ ≤ A,
gcd(hp + a, h′p + a′) divides h′a − ha′, which is nonzero (distinct primitive pairs are not proportional) and < 2AH in
absolute value. *Proof.* h′(hp + a) − h(h′p + a′) = h′a − ha′. ∎ Hence a prime ℓ > 2AH divides at most one of the
integers hp + a over primitive pairs with h ≤ H, a ≤ A (non-primitive pairs reduce to primitive ones by §2.2 with a
stronger modulus, so nothing is lost; without the primitivity restriction the statement is false: p = 433, (1,1) and
(2,2) give 434 and 868, both divisible by 31): SS8 Lemma 2.3 (privacy of large primes, stated there for jp + 1 and p + 4d) holds verbatim for the
full Type II family in (II-i) coordinates. *What this does and does not say (Assessment):* a prime ℓ > 2AH is a factor
of at most one layer integer, so a mechanism that pools *large prime factors* across layers reduces to congruence data
(B1), as in FRONTIER's privacy item. It does **not** say the layer events are independent, nor exclude joint residue
constraints or a deterministic mechanism that never pools factors — FRONTIER explicitly exempts those.

## 5. Verdict / proposed §7 text

**Verdict: inconclusive.** Sound reformulations and finite data, one scoped polynomial no-go, no new pointwise
theorem. The first draft's claims "no idea survived", "no false kill", "none as a route" were overclaims (cross-model
review, §6) and are withdrawn. What the lane adds:
1. PROVED (scoped: nonzero polynomial C, u, B with positive integer values, Q irreducible over ℚ, full-rank coset): no
   polynomial identity Q(x,y) = 4CuB − u − B beyond congruence menus, by degree count (Prop 2.4); rank-1 cosets are the
   thin families of (J)84. Closes the "non-principal genus escapes T1" thought independently of T1 — within that scope.
2. PROVED: privacy of large primes extends to the full Type II family over primitive (h,a) (Lemma 4.1); it constrains
   factor-pooling mechanisms only.
3. CERTIFIED (25 ≤ n ≤ 2·10⁵, n ≡ 1 (24)): the family (II) and Type I (min(a,b) ≤ 300) fail exactly at the odd squares;
   with ET's coprimality (II) fails additionally at 1705, 3985, 4585, 6265, 12145; (★) fails at 41 further n, 7 of them
   primes — an independent reproduction of the item-14 list by independent code (and reproduced again by the
   cross-model reviewer's independent verifier `scripts/z53_xrev_wildcard_counts.cpp`).
4. EVIDENCE: at 6 of 9 hard primes the aggregate Type II count is ≤ the minimum of six neighbours (all nine have
   N_II > 0, so this says nothing about complementarity of zero events).
5. A unified residue form of the full family, (II-v): ∃ d ≡ 3 (4), h | (d+1)/4 with h·(−hp mod d) | (d+1)/4 — the
   (★) form ρ_p(d) | (d+1)/4 is h = 1. Bookkeeping.

**Which ideas survive (unexcluded), and why.** Because (★) itself is false at 409 (and 13 further primes ≤ 10¹⁰), any
route must work on a broader family or treat those primes separately; with that caveat:
* Idea 1/2 (full Type II, Type I as the target family): B2's no-go is conditional on a *fixed finite* menu and exempts
  growing p-dependent families; T1 passes on every layer (§2.2(b)); B6 only forbids inference from averages. Unexcluded;
  no mechanism supplied here. Screens: T1 pass; 8/131 fail unless a 4-specific input is added (the numerator-8 family
  fails at 131, 241); tied modulus fail (4ah tied to hp + a); fixed p fail (no single-integer input).
* Idea 3 (converse of T1 for the family (II) at non-squares): a CONJECTURE consistent with §3.1; not addressed by any
  barrier; with ET coprimality it has the five listed composite exceptions.
* Idea 4 (r-spectrum / all-r forest edges): (J)82 is about specific downward propagation, not every selection law on
  R(p); unexcluded and undeveloped; overlaps §7.2.
* Idea 6 (ray-class / varying fields Q(√(−Cp)) and joint divisor constraints): CLASS_FORCING Thm 2.1 concerns the total
  product on a fixed line and does not cover joint constraints or varying fields; unexcluded and undeveloped; overlaps
  §7.3, §7.6.
* Ideas 8 (graph moves beyond single-variable Vieta), 11 (methods, not their naive applications): not developed, not
  excluded.
Excluded in scope: 7 (Prop 2.4), 9 (universal 2-power slice, dead at 409). Reducing to listed open items: 5 (§7.12),
10 (§7.6).

**Proposed FRONTIER §7 text (do not edit FRONTIER; for the integrator):** under §6 *Algebraic / forcing* add one line:
"Polynomial identities Q(x,y) = 4CuB − u − B with C, u, B ∈ ℚ[x,y] on a full-rank coset, Q a ℚ-irreducible binary
form of any genus → only congruence menus, by degree count (`Z53_WILDCARD.md` Prop 2.4, PROVED; rank-1 cosets are the
thin families of (J)84); privacy of large primes holds on the full Type II family over primitive (h,a) (hp + a, Lemma 4.1)." Under §3 *Privacy* add the pointer, with the caveat that it constrains factor-pooling only. No new §7 target is
proposed; the unexcluded ideas above overlap existing items §7.2, §7.3, §7.6 and were not developed here.

**Bottom line.** A fresh number theorist, told only the statement, rediscovers in order: the Jacobi obstruction and the
forced non-residue (d/p) = −1, the full Elsholtz–Tao Type II/Type I families with their log³p means, the covering/large-
sieve density view, the genus/ray-class reading, the forest of mutual-divisibility pairs, and the degree-count death of
identities — and finds each already mapped as a *parametrisation*. That is a novelty verdict, not a no-go: several of the broader
structural inquiries (ideas 1–4, 6) are not excluded by any scoped theorem in the map, and this lane did not develop them.
What is established here is modest: a scoped degree-count no-go for polynomial identities, primitive-pair privacy on the
full family, and finite data. The wall remains: a divisor of one integer in one moving class at one prime, below a
(log p)² main term.

## 6. Review record

Hostile reviewer (deep-mode subagent, independent recomputation of all 70 count rows, the census, and the nine neighbour
lists) found 12 defects, all fixed above: the false "ES ⟺ R(p) ∩ 4ℤ ≠ ∅" (now (★) ⟺); the false "R(q²) ⊆ {r ≡ 1,2 (4)}"
(even divisors at odd r); a mis-attributed r-list for 577; Lemma 4.1 needing primitive pairs (counterexample p = 433);
Prop 2.4 needing ℚ-irreducibility and a full-rank coset (counterexample on a line); an invalid Type I square-obstruction
sentence (removed; ET Prop 1.6 cited); the composite census not being ET's coprime Type II (coprime column added: +5
failures 1705, 3985, 4585, 6265, 12145, independently reproduced); "7 of 8" → "6 of 9" with 409, 577, 23929 as exceptions;
"all layers depressed" → aggregate only (712321's h = 2 layer is not depressed); the union-minimum attribution (83449,
317209); the "scaling" justification (replaced by computation); the divergent expected-count sum (now scoped and labelled
heuristic); §2.5 relabelled Assessment. Reviewer's verdict on the sound parts: Lemma 2.1 incl. its 2-adic part, Cor 2.2
(repaired), the Type II derivation and all five forms, the p = 73 example, the all-h square obstruction, the Type I
algebra, the b = 1 and SS8 attributions, the enumeration bounds — all check. Nothing in this memo establishes or refutes
ES.

**Cross-model review** (`data/z53/xreview/REVIEW_WILDCARD.md`, independent verifier `scripts/z53_xrev_wildcard_counts.cpp`):
REJECTED the first final draft for overclaimed kills ("no idea survived", "no false kill", "None as a route", "dead"),
retaining the algebra and computations (all 70 count rows and the census reproduced independently; Lemma 2.1, Cor 2.2,
(II), (II-i)–(II-v), §2.2(b), §2.3, Lemma 4.1 confirmed). Required fixes, all applied: (1) the §4 table and §5 verdict
rewritten with honest per-idea status (excluded in scope / reduces to an open item / unexcluded and undeveloped) and a
list of surviving ideas; (2) Prop 2.4 repaired (nonzero factors, positive integer values; counterexample C = 0,
u = x³, B = −x³ − x² − y² recorded); (3) the invalid "one of each divisor pair" cut-off removed, the log³p statement now
cites ET's average only; (4) Lemma 4.1's consequence restricted to factor-pooling mechanisms; (5) the §3.2 statistic no
longer used against complementarity; verdict recast as inconclusive. ES remains OPEN.
