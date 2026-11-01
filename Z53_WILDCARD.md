# Z53_WILDCARD — from-scratch attack on the tied divisor event

**ES is OPEN; nothing here claims it proved or disproved.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Status: **Checkpoint 1 (idea list, pre-FRONTIER)**. Lane rule: ideas generated before reading
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
   ∃ t ≡ 3 (4), a,b with ab | (p+t)/4 and t | a+b. Expected count ≍ log³p (vs log²p for (★)); the modulus of the
   divisor condition is relaxed from 4u to u/a when a² | u/4 (e.g. p+4a² needs only a divisor ≡ −1 mod 4a).
   Test: which p ≡ 1 (24) (and which non-squares n) have Type II but no (★); compare minimal parameters.
2. **Type I family** tp+1 = 4abC with t | a+b (derived §2.3); a=1 slice: (tp+1)/4 has a divisor ≡ −1 (mod t).
   Dual to Type II a=1 slice ((p+t)/4 has a divisor ≡ −1 mod t). Test: same census.
3. **Characterise the (★)/Type-II exceptional set among non-squares.** If the only n ≡ 1 (24) without Type II are
   squares, primality is used only through non-squareness; otherwise the extra exceptions show exactly what a proof
   must use. Test: census n ≤ 10⁶–10⁷.
4. **r-spectrum R(n) = {r : rn+1 has a divisor ≡ −1 (mod r)}** (r=1,2 always; ES ⟺ R(p) ∩ 4ℤ ≠ ∅; for squares
   R(q²) ⊆ {r ≡ 1,2 (4)}, PROVED §2.1). Test for a composition law / multiplicative structure on R(n) numerically.
5. **Covering-system view**: the APs {n ≡ −(u+B) mod 4uB} must cover all primes ≡ 1 (24); large sieve with
   non-CRT targets on composite moduli — compare with Vaughan/Elsholtz exceptional-set bounds (density only;
   expected dead for individual p, but check whether the half-dimensional structure (d/p) = −1 adds anything).
6. **Genus/ray-class reformulation**: d | 4Cp+1 ↔ ideal divisors of (1+2√(−Cp)); condition d ≡ −1 (4C) is a ray
   class condition, (d/p) = −1 a genus condition. Test whether anything beyond genus theory is captured.
7. **Polynomial identities in a quadratic-form parametrisation of p** (forms outside the principal genus never take
   square values, so T1 does not forbid them a priori). PROVED dead by degree count (§2.4): only congruence menus.
8. **Mutual-divisibility graph / Vieta-type moves**: u | p+B, B | p+u. Checked: no Vieta jump (equation linear in
   each variable); the ratio r = (p+u+B)/(uB) classifies edges, ES needs 4 | r.
9. **Sierpiński/Proth slice** C = 2^j: p·2^{j+2}+1 needs a divisor ≡ −1 (mod 2^{j+2}). Test numerically whether
   this slice alone always succeeds for small p (expected not).
10. **Davenport-constant / zero-sum argument** on the multiset of prime residues of p+u in (ℤ/4u)*: only bites when
    ω(p+u) ≳ |G|; fails for typical u. Noted, not pursued.
11. **Probabilistic/LLL, Chevalley–Warning, circle method, modular forms**: all reduce to counting with error ≫ log²p
    or give mod-p information without size control. Dead on first inspection (reasons in §2.5).

## 2. Derivations (all elementary; PROVED unless marked)

### 2.1 The Jacobi obstruction and the forced non-residue

**Lemma 2.1.** Let u ≥ 1 and d odd with d ≡ −1 (mod 4u). Then the Kronecker–Jacobi symbol (−u/d) = −1.
*Proof.* d ≡ 3 (4) gives (−1/d) = −1. Write u = 2^a u′, u′ odd. Quadratic reciprocity for the odd coprime pair
(u′, d) with d ≡ 3 (4): (u′/d) = (d/u′)(−1)^{(u′−1)/2} = (−1/u′)(−1)^{(u′−1)/2} = 1. If a ≥ 1 then 4u ≡ 0 (8) so
d ≡ 7 (8) and (2/d) = 1. Hence (−u/d) = (−1/d)(2/d)^a(u′/d) = −1. ∎

**Corollary 2.2 (T1 at the level of one event).** For an odd square n = q² and any u ≥ 1, q²+u has no divisor
d ≡ −1 (mod 4u): every prime ℓ | q²+u has (−u/ℓ) = +1 (ℓ ∤ q since ℓ | q ⇒ ℓ | u ⇒ ℓ | gcd(d,u) = 1), so (−u/d) = +1
for every divisor d, contradicting Lemma 2.1. For a prime p ≡ 1 (4) and d | p+u, d ≡ −1 (4u): (p/d) = (−u/d) = −1, and
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
Expected count: Σ_{a,h} τ(hp+a)/φ(4ah) ≍ log³p against log²p for h = 1 (consistent with Elsholtz–Tao's f_II average).
In the repository this family is ET Type II; the a = 1 slice of (II-ii) is López's b = 1 line (`B1_LINE.md`). Nothing
in 2.2 is new to the campaign; it is recorded because the lane required an independent derivation.

### 2.3 Type I, from scratch

4/p = 1/(px′) + 1/y + 1/z with p ∤ yz: yz(4x′ − 1) = px′(y + z). With g = gcd(y,z), y = gy₁, z = gz₁: y₁z₁ | x′,
x′ = y₁z₁x₂, and x₂ | g, g = x₂g₁, leaving g₁(4y₁z₁x₂ − 1) = p(y₁ + z₁). p ∤ g₁ (else 4y₁z₁x₂ − 1 ≤ y₁ + z₁, impossible),
so **(I)  tp = 4abC − 1 with t | a + b** (t := (4y₁z₁x₂ − 1)/p, a = y₁, b = z₁, C = x₂). Divisor form: ∃ a, C: 4Ca² + 1 has a
divisor t ≡ −p^{−1} (mod 4aC). The a = 1 slices of (I) and (II-iv) are dual: (tp+1)/4 resp. (p+t)/4 has a divisor ≡ −1
(mod t), t ≡ 3 (4). Both are obstructed at squares by the same Lemma 2.1 (applied to u = t with the even-divisor caveat
irrelevant since (p+t)/4, (tp+1)/4 are tested only for odd divisors ≡ −1 (mod t) here). *(Not pursued further; it is ET
Type I.)*

### 2.4 No polynomial identity in a quadratic-form parametrisation (degree count)

Suppose p = Q(x,y) (Q a binary form, possibly restricted to a coset of a sublattice) and p = 4CuB − u − B with
C, u, B ∈ ℚ[x,y] positive and integral on the coset. Degrees: deg C + deg u + deg B = 2. If two of them are constant the
third is (Q + const)/const, i.e. a congruence condition on Q(x,y) mod a fixed modulus — a fixed menu (B1). If C is constant
and u, B linear, the quadratic part of Q is 4C·(linear)(linear), reducible over ℚ; a definite or ℚ-irreducible indefinite
Q is excluded, and reducible Q represents a prime only trivially. If u is constant and B, C are linear, Q + u = B(4uC − 1)
factors, same conclusion. Hence **no identity beyond (★) itself and congruence menus exists in this shape** — and this
holds regardless of whether Q lies in a non-principal genus (where Q never takes square values, so T1 alone would not
have excluded it). Noted because the "non-principal genus escapes T1" thought is tempting and wrong for a different
reason.

### 2.5 One-line kills (no computation needed)
* Chevalley–Warning / polynomial method mod p: gives solutions of 4uBC ≡ u + B (mod p) with no size control; the size
  condition uBC < p/2 is the whole problem.
* Probabilistic method / LLL: there is no randomness; it is the count R(p) with its ≍ log²p mean and unbounded variance.
* Circle method on 4uBC − u − B = p: three variables, cubic, main term log²p ≪ any minor-arc error.
* Modular forms: Σ_n R_t(n)qⁿ is a Lambert/Appell-type series, not holomorphic modular (FRONTIER §2.3 already has the
  exact theta-quotient form); no exact formula with a positive main term.
* Vieta jumping on 4uBC − u − B = p: linear in each variable, no involution (FRONTIER (J)89 Cor 4.2 says the same for
  Type I).
* Davenport/zero-sum on the residues of the prime factors of p + u in (ℤ/4u)*: needs ω(p+u) ≳ |(ℤ/4u)*| ≍ u, false for
  typical u.

## 3. Computations (CERTIFIED in the stated ranges; scripts `scripts/z53_wildcard_*`, data `data/z53/wildcard/`)

### 3.1 Census of the three families, n ≡ 1 (mod 24), n ≤ 2·10⁵ (`z53_wildcard_census.c`, 8 s)
`gcc -O2 scripts/z53_wildcard_census.c -lm; ./a.out 200000 300 > data/z53/wildcard/census_2e5.txt`.
(★) and full Type II are enumerated exactly (bounded loops: ak ≤ (N+a+k)/4, h | a+k); Type I is enumerated with the
WLOG a ≤ b and the restriction a ≤ 300 (so "no Type I" below means none with min(a,b) ≤ 300 — a partial census).
* Of 8 333 values n ≡ 1 (24): 189 have no (★); 148 have no full Type II; 148 have no Type I (a ≤ 300); 148 have neither.
* The 148 are **exactly the odd squares ≡ 1 (24) in range** (checked list equality). So in this range the full Type II
  and Type I exceptional sets among n ≡ 1 (24) are precisely the squares (T1 is sharp), while (★) has 41 further
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
| 5569 | 0 | 10 | 7 | 3 | 11, 16, 26, 27, 12, 20 |
| 9601 | 0 | 7 | 2 | 4 | 15, 21, 36, 21, 34, 38 |
| 23929 | 0 | 39 | 15 | 6 | 37, 39, 13, 38, 36, 33 |
| 83449 | 0 | 15 | 4 | 2 | 71, 29, 37, 30, 45, 51 |
| 102001 | 0 | 21 | 9 | 0 | 63, 70, 42, 36, 53, 42 |
| 329617 | 0 | 30 | 11 | 5 | 61, 75, 48, 83, 64, 60 |
| 712321 | 0 | 32 | 5 | 8 | 83, 74, 58, 64, 61, 72 |

EVIDENCE: at 7 of the 8 hard primes the *full* Type II count is at or below the minimum of its six neighbours (23929 is the
exception); the deficit is global across the h-layers, not confined to h = 1. This matches `BM_CORRECTED_COUNT.md` §4
(positively correlated residuals of (★) and the b = 1 line; 83449 and 329617 are the union minima). Reading: a (★)
failure is a lower-tail event of one depressed integer, so widening the family (idea 1) buys a larger mean (log³p) but
no complementarity — exactly the "doubled main term, nothing forced" conclusion already recorded there.

## 4. Barrier check against FRONTIER §§3–4, §6 (read only after §§1–3 were fixed)

For each idea: which barrier, whether its scope really covers the idea, and what (if anything) is left.

| # | idea | barrier / existing item | scope really covers it? | residue |
|---|---|---|---|---|
| 1 | full Type II (II), log³p mean, modulus u/a on shifts 4a²C | It *is* ET Type II; the a = 1 slice is López's b = 1 line (`B1_LINE.md`, `BM_CORRECTED_COUNT.md` §4, Prop 4.1(a): Brauer character χ_{−4ab} on the whole family). B2 (tied modulus 4ah with the integer hp + a), T1 for every h (§2.2(b)), B6 for the log³ average (ET). | Yes. Every layer is a tied divisor event of one integer in one moving class; §3.2 shows the layers are positively correlated at the hard primes (no complementarity). | None as a route. Useful only as bookkeeping: the hardest primes are hard on *all* layers. |
| 2 | Type I | ET Type I; same barriers; (J)89 Lemma 4.1 (positive Type I slices have (d/p) = −1). | Yes. | None. |
| 3 | exceptional set = squares? | T1 (B5) is exact: f_I(m²) = f_II(m²) = 0 (ET Prop 1.6); the converse to 2·10⁵ (§3.1) is implied by the prime census to 10⁸ (FRONTIER §1) plus scaling. | Yes. | Confirms that primality enters only through non-squareness *at the level of the obstruction*; the proof must still produce a class, not a parity (checklist 9). |
| 4 | r-spectrum R(n) = labels of the forest F_n | The forest (J)106/(J)83, bichromatic ⟺ certificate, composition "adds reachability, never existence" ((J)82), fixed roots/bounded windows dead under Dickson. | Yes: an r-closure law would be a composition rule between slices, exactly what (J)82 found adds nothing. A numerical look (p = 409, 577: R ∋ 2, 3, 6, 11, 14, 15, … with no multiple of 4) showed no closure pattern. | None. |
| 5 | covering-system / large sieve with non-CRT targets | B6 (Vaughan 1970, Elsholtz–Tao exceptional sets ≪ N exp(−c(log N)^{2/3})); §7.12 (exponent θ > 3/4) is the live averaged target, already audited (`BREADTH_Z45.md` §§15–16: CRT architectures capped at 3/4). | Yes; and the targets {−(u+B) mod 4uB} are genuinely non-CRT, which is the audited "non-CRT" gap. | Nothing beyond §7.12, which has its own lanes. |
| 6 | genus / ray-class reformulation | §2.2 (BM = one Kronecker character per pair), §7.3 (class inside the coset), CLASS_FORCING Thm 2.1 (no reciprocity law adds information about [N] ∈ (ℤ/t)*). | Yes: the condition d ≡ −1 (mod 4C) is a ray-class condition mod 4C whose only p-dependent part is the parity (d/p) = −1. | None. |
| 7 | identities over a non-principal-genus form | B1 (Mordell–Schinzel) *plus* the degree count of §2.4, which kills it even where T1 would not. | Yes (own proof). | Dead, PROVED. |
| 8 | mutual-divisibility pairs / Vieta | Forest F_p; no involution ((J)89 Cor 4.2); equation linear in each variable. | Yes. | None. |
| 9 | Proth slice C = 2^j | "2-group levels alone do not suffice (1 298 primes ≤ 10⁶ have no word at any such level)" (§3, Stickelberger item). | Yes. | None. |
| 10 | Davenport / zero-sum on prime residues | needs ω(p+u) ≳ |(ℤ/4u)*|; §7.6 (full-factor-multiset realisation) is the open form. | Yes. | Only §7.6, already listed. |
| 11 | probabilistic / polynomial / circle / modular | §2.5; B3 scale, §2.3 (theta quotient is Eisenstein-only). | Yes. | None. |

**Screens for the best survivor (idea 1, full Type II as the target statement).** T1: passes (vanishes at squares for
every h, §2.2(b)); 8/131: the same family for numerator 8 fails at 131 and 241 (`BM_CORRECTED_COUNT.md` §4), so any argument
must use 4 — not supplied; tied modulus: fails (modulus 4ah tied to the integer hp + a; relaxing to u/a on square-multiple
shifts changes the constant, not the tie); fixed p: fails (only averaged inputs known). So idea 1 is **not a route**; it is
the same wall with a log³p mean.

**False-kill audit.** I looked for an idea whose kill depends on a scope assumption that the idea violates. The only
candidates were idea 7 (non-principal genus forms escape *T1*) — killed instead by §2.4, unconditionally — and idea 5's
non-CRT targets, which are precisely the gap §7.12/z50 already names. No false kill found.

## 5. Verdict / proposed §7 text

(pending)
