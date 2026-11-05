# Z57_COMPLEMENT — are the failure sets of different certificate families complementary at one prime?

Status: z57 lane COMPLEMENT (brief `z52bbriefs/z57_lanes.md` §COMPLEMENT, rules `z53_depth.md`). Internal, internally
reviewed only (§9). **ES is OPEN; nothing here proves or disproves ES, (★), or any family's positivity at any infinite set
of primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts
`scripts/z57_complement_*`, data `data/z57/complement/` (13 MB).

## 0. Summary

**Verdict: narrowed (scoped negative).** No pair of certificate families in the menu is statistically complementary
beyond local data; the negative dependence that exists is CRT exclusion — between cheap congruence events (local, top
levels) and, at lower order, between divisors of different integers (the privacy link). The question (2) of the brief
(prove a union inequality for an anti-correlated pair) has no candidate pair; (3) is delivered as a scoped theorem plus
certified falsifiers. Pointwise complementarity at primes is *not* excluded for the pairs with no joint prime zero
((★)&b = 1, (★)&Type I, b = 1&Type I, Type I&c2, Type I&c3).

* **Unification (Lemma W, PROVED; §3.1).** Every family of the menu is a set of words of W(p) = {tuv − u − v = p} or of
  W(cp): (★) = {4 | t}, b = 1 = {4 | u or v}, Type I a = 1 = {4 | tu − 1 or tv − 1}, c-lines = {4c | t} in W(cp). On
  interior words of W(p) the three certificate slices are exactly the Jacobi-(−1) words (DEDEKIND_ES Thm 4.5), the rest
  (QR) the Jacobi-(+1) words. A word from shift u is a divisor m of p + u, and (apart from the single boundary word t = 1)
  its slice-membership vector is a function of (m mod 4u, p mod 4u) (m odd); a word with fixed (u, v) exists iff
  p ≡ −(u + v) (mod uv), and (apart from t = 1) its slices are a function of p mod 4uv. (★) ∩ (Type I a = 1) = ∅.
* **Theorem C (same-integer positive covariance; PROVED, Bombieri–Vinogradov; §3.2).** Fix U, 0 < θ < 1/4 and local data
  p ≡ a (mod M) with 4·lcm(1..U) | M. The low-level (m ≤ x^θ), M-coprime parts of any two slices (STAR, B1, I1, QR) at a
  common shift u ≤ U (both non-empty there) are positively correlated over primes p ≤ x, p ≡ a (M): covariance
  ≥ κ(log x)³ − O((log x)²), correlation ≥ c₀ > 0. Parts on *different* integers (shifts u ≠ u′, or a c-line integer
  cp + b with b ≠ cu) have covariance −Θ((log x)²) — a negative coupling from CRT exclusion at primes ∤ M, of lower order
  (correlation ≍ −1/log x). *Sharing an integer couples families positively (τ-richness: divisor pairs with a large
  common part); different integers are coupled only weakly and negatively.* (c-line words at shifts b = cw live on the
  same integers p + w as STAR/B1/I1 at shift w.)
* **Prop F (falsifiers of implications; CERTIFIED; §3.3).** For every pair of certificate families in {(★), b = 1,
  Type I a = 1, c = 2, c = 3} there are non-square composites n ≡ 1 (4) with R_A(n) = R_B(n) = 0 (e.g. 105, 4545 for
  (★) & b = 1), and odd squares kill all of them (T1). At primes: R_(★)(102001) = R_{c2}(102001) = 0;
  R_{b=1} = R_{c2} = 0 at 193, 2521; R_{b=1} = R_{c3} = 0 at 193; R_(★) = R_{c3} = 0 at 577, 5569, 83449, 1134241, 1726201.
  So "R_A(p) = 0 ⟹ R_B(p) ≥ 1" is *false* for (★)⇒c2, (★)⇒c3, b=1⇒c2, b=1⇒c3 (and the reverses).
* **Measurement (EVIDENCE; §4).** 108 397 + 48 139 + 25 226 primes p ≡ 1 (4) (all, at 10⁸, 10⁹, 10¹⁰ windows), 2 305 / 960 /
  550 sampled primes in [10¹¹, 1.6·10¹¹], [10¹², 1.7·10¹²], [10¹³, 1.8·10¹³], and 42 000 rough semiprime controls. For
  all 21 pairs of certificate families among {STAR, B1, I1, c2, c3, 𝔊*, K}, residual correlations after local controls
  are **positive at every scale** except c2–c3 at 10¹³ (−0.004, within one s.e.) (STAR–B1 +0.48…+0.55, B1–I1 +0.61…+0.64,
  STAR–I1 +0.39…+0.46, STAR–c2 +0.34…+0.41, 𝔊*–K +0.04…+0.18, c2–c3 −0.004…+0.10). Joint low tails (each family ≤ its
  within-stratum 5 % quantile), ratio to within-stratum independence: 0.88–4.71 over all certificate pairs and scales
  (excluding the nested pair STAR–𝔊*), > 1 in all but three entries (c2–c3 0.88, 𝔊*–K 0.99 at 10¹¹; c3–K 0.99 at
  10¹²; all within noise). Truncated-Euler-product proxies for L(1, χ_p), L(1, χ_{−4p}) load with the **same sign on every
  certificate family** (10⁹, 10¹⁰) and the opposite sign (χ_p) on the placebo; they change any pair correlation by ≤ 0.03.
  **Rough semiprimes reproduce the prime joint structure** (family means/L² to ±0.001, total-count means to ±0.003, pair
  correlations to ±0.025): nothing in the joint law is prime-specific at this resolution.
* **Registered falsifier (checkpoint 1).** Leads were triggered (12 cross-family level-band pairs, §4.5). Follow-up:
  6 leads involve a congruence band (t ≥ p^{0.6}); for the three of them tested against the exact CRT (local) model
  (STAR z7 vs c2/c3/b = 1 cheap pairs) the model reproduces sign and most of the size (empirical −0.079/−0.070/−0.055 vs
  model −0.067/−0.064/−0.043, s.e. 0.010); the other three are attributed to the same mechanism by Lemma W(e)
  (Assessment). The 6 bottom-band leads have |r| ≤ 0.04 and mostly shrink under finer residue controls; they match the
  sign and order of the cross-integer CRT exclusion of Thm C(ii) (Assessment). No full certificate pair is negative.
* **Zero census ≤ 4·10⁶ (CERTIFIED counts; §4.6).** At primes: Type I a = 1 never vanishes; (★) 12 zeros, b = 1 3, none
  shared; joint zeros of other pairs occur at or above per-decade independence (c2&c3 53 vs 33, 𝔊*&K 12 vs 2.8). At
  non-square composites joint zeros exceed independence by 1.4–25× (positive tail dependence); the five-slice union
  vanishes only at n = 105.

**Where it stops (§5).** A complementarity theorem would have to come from (i) local data — the CRT exclusion that
exists is a covering-congruence statement (B1, dead for fixed menus), or (ii) the medium regime, where Thm C proves the
same-integer coupling positive for bounded shifts and the cross-integer coupling of lower order, and the data show the
total positive. Within one word set the certificates and QR are the two Jacobi halves, so (conditionally on the word
count) QR is the only complementary partner; R_STAR∪B1∪I1 ≥ 1 ⟺ some interior word is a Jacobi non-residue or a
boundary certificate exists — for p ≡ 1 (8) this is ES₅, λ(p) ≤ 3 (DEDEKIND_ES Cor 4.6), already on FRONTIER. No
sidestep of B2 is available through unions of the menu.

## 1. Statements attacked

p ≡ 1 (mod 4) prime, L = log p. **The word set** W(n) := {(t, u, v) ∈ ℕ³_{≥1} : tuv − u − v = n} (ordered; (t,u,v) and
(t,v,u) are distinct unless u = v); "interior" = t, u, v ≥ 2, then n/A = [[v,t,u]] with A = tu − 1 (`DEDEKIND_ES.md`
Lemma 1.1). **The menu 𝓜** (counts are ordered word counts):

| family | words | meaning (source) |
|---|---|---|
| STAR | 4 \| t | (★) = ET Type II c = 1; (u, B, C) = (u, v, t/4); R_STAR = R(p) (FRONTIER §2.1) |
| G = 𝔊*, K | STAR with Q⁴ > P·p, resp. not (P, Q = min, max of u, v) | `Z56_FAMDESIGN` Thm V family and its Burgess corner |
| H3, HC | STAR with 64C³ ≤ p, resp. C ≤ ⌊L²⌋ | complete levels; HC words (Z56_FAMDESIGN §6) |
| B1 | 4 \| u or 4 \| v | López Type A / the b = 1 line, 4xy \| p + 4x + y (`B1_LINE.md`); R_B1 = 2·N₁ |
| I1 | 4 \| tu − 1 or 4 \| tv − 1 | ET Type I, slice a = 1 (`CONDITIONAL_ES` Lemma 1.1), incl. boundary words |
| QR | interior, none of the above | Jacobi (A/p) = +1 words — **not certificates; placebo family** |
| c2, c3 | words of W(cp) with 4c \| t | ET Type II c-lines (4abcd − a − b = cp; `CONDITIONAL_ES` Lemma 1.2) |
| X z k | family X restricted to z = log t / log(cp) ∈ [k/10, (k+1)/10) | level-band sub-families (non-trivial zero rates) |
| INT, W | all interior words; all words | totals (collider controls) |

(Q1) **Measurement (EVIDENCE).** For pairs (A, B): residual correlation after removing local data (p mod 840 strata; OLS on
one-hot residues of p mod 8, 3, 9, 5, 25, 7, 49, 11, …, 47), and joint zero / joint low-tail rates against the
within-stratum independence prediction (ratio and Mantel–Haenszel odds ratio). Complementary beyond local data :=
robustly negative.
(Q2) **Complementarity theorem** (target if (Q1) finds a pair): R_A(p) + R_B(p) ≥ c·(main) or R_A(p) = 0 ⟹ R_B(p) ≥ 1.
(Q3) **Scoped negative** (target otherwise): what all menu pairs share and what a complementarity argument would need.

## 2. Why this is not closed

Known: (★) vs b = 1 residuals positively correlated (+0.21…0.30; `BM_CORRECTED_COUNT.md` §4, `BRAINSTORM/z38_*`),
co-varying beyond |W| (`BRAINSTORM/s9_union_thinning.md`); Type I vs Type II residual log counts +0.70 at p ≤ 2·10⁵
(`BRAINSTORM/z52b_fingerprint.md` #246); windows inside (★) net positively dependent with two congruence-level negative
leads (`Z56_FAMATTACK.md` §3.2). Not done before: local controls beyond p mod 840 for *different* families; the joint
zero/low-tail structure; Type I a = 1, the c-lines, 𝔊* vs its corner, a placebo family; 10¹⁰–10¹³; composite controls;
and any theorem explaining the sign. Nothing in FRONTIER §6 or the z53 closed list concerns the joint law of two
families at one p.

## 3. Proved / certified

### 3.1 Lemma W (unification; PROVED)

Let p ≡ 1 (mod 4) be prime.
(a) Each family of 𝓜 is a set of words of W(p) (STAR, G, K, H3, HC, B1, I1, QR) or of W(cp) (c-lines), with the
    membership conditions of the table; each word is an explicit ES certificate for STAR, B1, I1, c-lines.
(b) For interior words of W(p): (A/p) = −1 ⟺ the word lies in STAR ∪ B1 ∪ I1. Hence INT = #{QNR interior words} + QR,
    disjointly.
(c) STAR ∩ I1 = ∅.
(d) (shift form) The words (t, u, v) of W(p) with given u and u ≤ v are in bijection with the divisors m of p + u with
    m ≡ −1 (mod u), m ≤ (p + u)/u, via t = (m + 1)/u, v = (p + u)/m. If m is odd and m ≠ u − 1 (i.e. t ≠ 1), the
    membership vector of the word in (STAR, B1, I1, QR, boundary) is a function of (m mod 4u, p mod 4u). (Slices overlap:
    STAR ∩ B1 ∋ (4, 4, 3) at p = 41, and B1 ∩ I1 ≠ ∅.)
(e) (pair form) For fixed u, v ≥ 1 there is at most one word (t, u, v); it exists iff p ≡ −(u + v) (mod uv), and then,
    unless t = 1, its membership vector is a function of p mod 4uv (t = 1 and t = 5 have the same residues).

*Proof.* (a) Certificates: (★) FRONTIER §2.1; B1 and I1 DEDEKIND_ES Thm 4.5 (explicit triples
4/n = 1/(wf) + 1/(tnw) + 1/(tnwf) for u = 4w, f = tv − 1, and CONDITIONAL_ES Lemma 1.1 for 4 | tv − 1, which allows
t, u, v ≥ 1); Thm 4.5 is stated for interior words, but the B1 identity is the algebraic identity
4w(tv − 1) = n + v rewritten and holds verbatim for boundary words (t = 1; v = 1 is impossible with 4 | u at
n ≡ 1 (4)), and the brute-force check below verifies it for every boundary word with n ≤ 1393; c-lines: a word
(4cd, a, b) of W(cp) is 4abcd − a − b = cp, giving 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp) (BM_CORRECTED_COUNT Prop 4.1(a)).
(b) DEDEKIND_ES Thm 4.5 (proved there by Rademacher's congruence and a 512-cell check). (c) 4 | t ⟹ tu ≡ tv ≡ 0 (mod 4).
(d) v(tu − 1) = p + u; put m = tu − 1. Then t ≡ (m + 1)/u (mod 4) depends on m mod 4u; v ≡ (p + u)·m⁻¹ (mod 4) depends on
p mod 4 and m mod 4; the slice conditions involve only t, u, v mod 4 and the boundary conditions t = 1, u = 1, v = 1, i.e.
m = u − 1 (excluded by hypothesis), u = 1 (fixed), m = p + u (excluded by m ≤ (p+u)/u for u ≥ 2; for u = 1 every word
is a boundary word). (e) t = (p + u + v)/(uv) must be a positive integer; t mod 4 is determined by p + u + v mod 4uv,
and t = 1 is the only boundary value not determined by it. ∎

Checks (CERTIFIED): the engine (§4.1) recomputes (A/p) for every interior word of every prime in [1000, 20000] and finds
the cell law of (b) without exception; `z57_complement_brute.py` turns every STAR, B1, I1, c2, c3 word for n ≤ 1393 into
a 4/n identity checked in exact rationals.

*Reading.* (d)–(e) are the two regimes. Low level t (small m): slices are divisor counts of the *same* integers p + u in
different residue classes mod 4u. Top level (uv ≤ p^{1−z}): slices are congruence events modulo 4uv, and the different
lifts of one pair are mutually exclusive — exact local anti-correlation.

### 3.2 Theorem C (same-integer positive covariance; PROVED)

**Setting.** U ≥ 1, 0 < θ < 1/4, M with 4·lcm(1, …, U) | M, a with gcd(a, M) = 1; 𝒫_x := {p ≤ x prime : p ≡ a (M)};
y := x^θ. For a modulus q | M and a non-empty set 𝒞 of unit classes mod q put
  D_𝒞(N) := #{m | N : m ≤ y, gcd(m, M) = 1, m mod q ∈ 𝒞}
(for the slices q = 4u; for c-line words from shift b, q = 4cb; two counts with different moduli are compared after
lifting both class sets to the lcm, which still divides M).
E, Cov, Var denote mean, covariance, variance over p ∈ 𝒫_x.

**Theorem C.** (i) For u ≤ U, q | M and non-empty 𝒞, 𝒞′ mod q (disjoint or not) there are κ = κ(θ, M, q) > 0 and
C = C(θ, M) with
  Cov(D_𝒞(p + u), D_𝒞′(p + u)) ≥ κ(log x)³ − C(log x)²,  Var(D_𝒞(p + u)) ≤ C(log x)³,
so corr(D_𝒞(p + u), D_𝒞′(p + u)) ≥ κ/(2C) for x ≥ x₀(θ, M, U).
(ii) (different integers) Let u ≤ U, c, b ≥ 1 with cu ≠ b (c = 1, b = u′ ≠ u is the case of two shifts), and suppose
every prime dividing c(cu − b) divides M. Then for non-empty class sets 𝒞 (mod q) and 𝒞′ (mod q′), q, q′ | M,
  Cov(D_𝒞(p + u), D_𝒞′(cp + b)) = −Σ_{m∈𝒞, m′∈𝒞′, m, m′ ≤ y, (mm′, M) = 1, (m, m′) > 1} 1/(φ(m)φ(m′)) + O_A((log x)^{−A}),
and −C(log x)² ≤ Cov ≤ −κ₂(log x)² + O(log x) with κ₂ = κ₂(θ, M, q, q′) > 0: a negative coupling of lower order
(correlation ≍ −1/log x), from CRT exclusion (a prime ℓ ∤ M cannot divide both integers — the privacy link of
`Z56_FAMATTACK` Lemma L(c)).

**Corollary C1 (the slices).** For S ∈ {STAR, B1, I1, QR} and u ≤ U let S_u^♭(p) := #{words (t, u, v) ∈ S with
m = tu − 1 ≤ x^θ and gcd(m, M) = 1}. By Lemma W(d) (m is odd since 2 | M) S_u^♭(p) = D_{𝒞_S(u, a)}(p + u) − δ_S(u, a)
for a set of classes 𝒞_S(u, a) mod 4u depending only on u and a mod 4u, where the constant δ_S(u, a) ∈ {0, 1} removes the
single boundary divisor m = u − 1 (t = 1; coprime to M only for u = 2, m = 1, and then its divisibility is fixed by a);
constants do not affect covariances. Hence for F_S := Σ_{u ≤ U} S_u^♭:
  Cov(F_S, F_{S′}) ≥ Σ_{u ≤ U : 𝒞_S, 𝒞_{S′} ≠ ∅} κ_u (log x)³ − O_U((log x)²)  (> 0 if some u has both non-empty),
while the cross-shift terms contribute only −O_U((log x)²) by (ii). c-lines: if b = cw (w ≤ U), then cp + b = c(p + w)
and (c | M) the M-coprime divisors of cp + b are those of p + w, so the c-line part at shift b is a class count on the
*same* integer as the slices at shift w, and (i) applies (positive, order (log x)³); if b ∉ cℕ, (ii) applies (negative,
order (log x)², when every prime dividing c(cu − b) divides M). (Example of emptiness: B1 at odd u ≡ 1 (4) is empty,
since then p + u ≡ 2 (mod 4) and 4 ∤ v; QR is empty at u = 1, where every word is a boundary word.)

*Proof of (i).* For m coprime to M (hence to u, since every prime ≤ U divides M, and to 2), the conditions m | p + u and
p ≡ a (M) define one unit class modulo Mm (m < p). For a pair (m, m′) the joint condition m, m′ | p + u is one class
modulo M·[m, m′]. By Bombieri–Vinogradov, for every A there is B with
Σ_{r ≤ x^{1/2}(log x)^{−B}} max_{(b,r)=1} |π(x; r, b) − π(x)/φ(r)| ≪ x(log x)^{−A}. All moduli here are ≤ M y² = M x^{2θ},
inside the BV range for x ≥ x₀ since 2θ < 1/2. Each modulus r = M l arises from at most τ(l)² pairs (m, m′) with
[m, m′] = l (at most τ(l²) ≤ τ(l)² pairs); with the trivial bound |E(x; r)| ≪ x/φ(r) and Cauchy–Schwarz,
Σ_l τ(l)²|E(x; Ml)| ≤ (Σ_{l ≤ x} τ(l)⁴ x/φ(l))^{1/2}(x(log x)^{−A})^{1/2} ≪ x(log x)^{8 − A/2}. Dividing by |𝒫_x| ≍ x/log x:
  E[D_𝒞] = S₁(𝒞) + O((log x)^{−A′}),  E[D_𝒞 D_𝒞′] = S₂ + O((log x)^{−A′}),
  S₁(𝒞) := Σ_{m ≤ y, (m,M)=1, m∈𝒞} 1/φ(m),  S₂ := Σ_{m, m′ ≤ y, (mm′,M)=1, m∈𝒞, m′∈𝒞′} 1/φ([m, m′]).
*Upper bounds.* Σ_{m≤y}1/φ(m) ≪ log y, so S₁ ≪ log x. Writing g = (m, m′), m = ga, m′ = gb, (a, b) = 1:
φ(gab) ≥ φ(g)φ(a)φ(b), so S₂ ≤ Σ_{g≤y}φ(g)⁻¹(Σ_{a≤y}φ(a)⁻¹)² ≪ (log x)³; the same bound holds for E[D_𝒞²], giving the
variance bound.
*Lower bound.* Let 𝒮 = {n ≥ 1 : (n, M) = 1}, c ∈ 𝒞, c′ ∈ 𝒞′ fixed. Every pair (m, m′) ∈ 𝒮² is uniquely (ga, gb) with
g = (m, m′) and (a, b) = 1, and then [m, m′] = gab and φ(gab) ≤ gab. Keeping only m ≡ c, m′ ≡ c′:
  S₂ ≥ Σ_{g ∈ 𝒮, g ≤ y} g⁻¹ T(y/g; c ḡ, c′ ḡ),  T(z; r, r′) := Σ_{a, b ≤ z; a, b ∈ 𝒮; (a,b)=1; a ≡ r, b ≡ r′ (q)} 1/(ab).
Since q | M, the classes r, r′ are units and the integers of 𝒮 in the class r mod q are φ(M)/φ(q) classes mod M, so
A(w; r) := Σ_{a ≤ w, a ∈ 𝒮, a ≡ r} 1/a = α log w + O_M(1) (w ≥ 1), α := φ(M)/(Mφ(q)), and A(w; r) = 0 for w < 1.
Möbius inversion of (a, b) = 1 (the common divisor e lies in 𝒮):
  T(z) = Σ_{e ∈ 𝒮, e ≤ z} μ(e)e⁻² A(z/e; r ē) A(z/e; r′ ē) = α²(log z)² Σ_{e∈𝒮} μ(e)e⁻² + O_M(log z + 1),
because Σ_e e⁻²(log e)^j converges for j ≤ 2 and the tail e > z contributes ≪ (log z)²/z. So
T(z) ≥ κ₁(log z)² − C₁(log z + 1) with κ₁ = α²∏_{ℓ ∤ M}(1 − ℓ⁻²) > 0, uniformly in the classes. With
Σ_{g ≤ w, g ∈ 𝒮} 1/g = β log w + O(1), β = φ(M)/M, partial summation gives Σ_{g≤y, g∈𝒮} g⁻¹ log²(y/g) =
(β/3)(log y)³ + O((log y)²), and Σ_{g ≤ y} g⁻¹(log(y/g) + 1) ≪ (log y)². Hence S₂ ≥ (κ₁β/3)(θ log x)³ − O((log x)²),
while S₁(𝒞)S₁(𝒞′) ≪ (log x)². So Cov = S₂ − S₁S₁′ + o(1) ≥ κ(log x)³ − C(log x)² with κ = κ₁β θ³/3. ∎
*Proof of (ii).* If a prime ℓ divides m | p + u and m′ | cp + b then ℓ | c(p + u) − (cp + b) = cu − b; by hypothesis ℓ | M,
contradicting (mm′, M) = 1. So pairs with (m, m′) > 1 never occur together: P(m | p + u, m′ | cp + b) = 0. For
(m, m′) = 1: since (m′, c) = 1, m′ | cp + b is the class p ≡ −b c⁻¹ (mod m′), a unit class (a prime ℓ | (m′, b) would
divide cp, impossible as ℓ ∤ c and m′ < p), and the three congruences are one unit class modulo M m m′ ≤ M x^{2θ}; BV as
above gives P = 1/(φ(m)φ(m′)) + error, with total error O((log x)^{−A′}) after normalisation. Since
E[D]E[D′] = Σ_{all m, m′} 1/(φ(m)φ(m′)) + O((log x)^{−A′}), the covariance is minus the sum over (m, m′) > 1, as stated.
Upper bound for that sum: (m, m′) > 1 means some prime ℓ ∤ M divides both; with φ(ℓa) ≥ φ(ℓ)φ(a) it is
≤ Σ_{ℓ ∤ M} φ(ℓ)⁻²(Σ_{a ≤ y} φ(a)⁻¹)² ≪ (log x)². Lower bound: fix one prime ℓ₀ ∤ M and keep m = ℓ₀a, m′ = ℓ₀a′ with
a ≡ c ℓ̄₀ (q), a′ ≡ c′ ℓ̄₀ (q′), a, a′ ∈ 𝒮: the sum is ≥ ℓ₀⁻² A(y/ℓ₀; ·)A′(y/ℓ₀; ·) ≥ κ₂(log x)² − O(log x).
(For c = 1, b = u′ the hypothesis is automatic since 0 < |u − u′| < U.) ∎

*Scope (read this).* Theorem C is about the distribution over primes in a fixed class, not about a single p (B6); it
covers bounded shifts, divisors ≤ x^θ with θ < 1/4, and divisors coprime to M — sub-families of the slices, not the full
counts. It is a theorem about the *sign* of the coupling: in the regime it covers, slices sharing an integer are
positively coupled (the τ-richness/gcd mechanism: pairs (ga, gb) with a large common part g give the (log x)³ term),
and slices on different integers are negatively coupled at the lower order (log x)² by CRT exclusion (correlation → 0
like 1/log x). So the only negative dependence it finds beyond the fixed local datum is this privacy effect, which is
dominated wherever an integer is shared. It does not exclude a pointwise implication; Prop F does that for the four
prime pairs listed there.

### 3.3 Proposition F (falsifiers of implications; CERTIFIED)

From the census of all n ≡ 1 (mod 4), 5 ≤ n ≤ 4·10⁶ (§4.6; `census_summary.txt`):
(a) every odd square n ≤ 4·10⁶ has all menu families zero (T1);
(b) for every pair {A, B} ⊂ {STAR, B1, I1, c2, c3} there is a non-square composite n ≡ 1 (4) with R_A(n) = R_B(n) = 0
    (STAR&B1: 105, 4545; STAR&I1: 105, 465, 801, 2641, 2929, 3705, 13041; B1&I1: 105, 2961, 25305, 111969; I1&c2: 2961,
    14841, 1 243 089; STAR&c2: 18 values; STAR&c3: 48; B1&c2: 12; B1&c3: 17; I1&c3: 13; c2&c3: 503);
(c) at primes p ≡ 1 (4) ≤ 4·10⁶: R_STAR = R_c2 = 0 at 102001; R_STAR = R_c3 = 0 at 577, 5569, 83449, 1 134 241, 1 726 201;
    R_B1 = R_c2 = 0 at 193, 2521; R_B1 = R_c3 = 0 at 193; no prime has R_STAR = R_B1 = 0, R_STAR = R_I1 = 0,
    R_B1 = R_I1 = 0, R_I1 = R_c2 = 0 or R_I1 = R_c3 = 0 (R_I1 never vanishes at these primes).
Consequences (CERTIFIED): an implication R_A(n) = 0 ⟹ R_B(n) ≥ 1 asserted for all non-square n ≡ 1 (4) is false for
every pair; at primes it is false for STAR ⇒ c2, STAR ⇒ c3, B1 ⇒ c2, B1 ⇒ c3 (and the reverses). So a complementarity
proof must use more than non-squareness and n ≡ 1 (4). Caveat: for STAR&B1, B1&I1 and I1&c2 every composite falsifier
found is divisible by 3 (105, 4545, 2961, 25305, 111969, 14841, 1 243 089), so an argument using also 3 ∤ n is not
refuted by this census for those pairs; for STAR&I1 there are falsifiers coprime to 105 (2641 = 19·139,
2929 = 29·101). For the five pairs with no joint prime zero ≤ 4·10⁶ (STAR&B1, STAR&I1, B1&I1, I1&c2, I1&c3) nothing here
excludes a pointwise implication at primes (for STAR&B1 this is the open union question of FRONTIER §2.1).

## 4. Computed

### 4.1 Engine and validation (CERTIFIED for the stated ranges)

`scripts/z57_complement_words.c` (`gcc -O2 -o z57w scripts/z57_complement_words.c -lm`): for each n, factors n + u
(segmented sieve) for u ≤ 2 + √(n + 1) and enumerates all words with u ≤ v (Lemma W(d)); repeats for cn, c = 2, 3, keeping
4c | t. Output: W, STAR, B1, I1, QR, BND, G, K, H3, HC, c2, c3 and ten level bands for STAR, B1, I1, QR, c2, c3.
Validation: (a) `scripts/z57_complement_brute.py` (direct enumeration of all (t, u, v); exact-rational certificate check
for every STAR, B1, I1, c2, c3 word) agrees column by column at all 349 n ≡ 1 (4), 5 ≤ n ≤ 1393; (b) STAR = R and
B1 = 2·N₁ against `scripts/z38_b1.c` at all 1045 primes p ≡ 1 (4) in [1000, 20000]; (c) JAC=1 mode: the Thm 4.5 cell
law at every interior word in that range; (d) the census ≤ 4·10⁶ reproduces the (★) zeros 409 … 1 726 201 (FRONTIER §2.1)
and the b = 1 zeros 193, 2521, 66529 exactly.

### 4.2 Datasets (`data/z57/complement/`)

| label | n | primes ≡ 1 (4) | command |
|---|---|---|---|
| 1e8 | all in [10⁸, 1.04·10⁸] | 108 397 | `z57w range LO HI 3`, 4 chunks (`w_1e8_*`) |
| 1e9 | all in [10⁹, 1.002·10⁹] | 48 139 | 4 chunks (`w_1e9_*`) |
| 1e10 | all primes in the initial segments of six chunks [10¹⁰ + k·333 334, +333 333] (each processed until the 1790 s timeout on a heavily loaded machine; e.g. chunk 0 = [10¹⁰, 10 000 177 813]; reached ends = last line of each file) | 25 226 | `w_1e10_*_partial` |
| 1e11 / 1e12 / 1e13 | next prime ≡ 1 (4) after 10^k + j·step (`z57_complement_samples.py`) | 2 305 / 960 / 550 | `z57w list 3 < list_1e*`, partial (timeout), `w_l1*_partial` |
| rough8 / rough9 | composite non-square n ≡ 1 (4), least prime factor > n^0.4 (`z57_complement_controls.py rough`) | 30 000 / 12 000 | `w_rough_*` |
| census | all n ≡ 1 (4), 5 ≤ n ≤ 4·10⁶ | 1 000 000 n | `z57w list 3`; stored: rows with some zero (`census_le4e6_anyzero.txt.gz`); full file regenerable (9 min) |

Statistics: `scripts/z57_complement_stats.py` (`stats_*.txt`), `_lproxy.py` (`lproxy_*.txt`), `_leads.py` (`leads.txt`),
`_leadfollow.py` (`leadfollow_*.txt`), `_toplocal.py` (`toplocal_*.txt`), `_census.py` (`census_summary.txt`). All run with
`OMP_NUM_THREADS=1`, `ulimit -v ≤ 7.5·10⁶`, `timeout ≤ 1790`. z-values are nominal (r√N).

Means/L² (1e10; stable across scales): W 0.86, INT 0.68, STAR 0.161, B1 0.294, I1 0.269, QR 0.177, 𝔊* 0.131, K 0.030,
c2 0.080, c3 0.047; all overdispersed (var/mean of the families 1.9–10; W 29, BND 133 at 10¹⁰). QNR share of interior words 0.740 (all scales).

### 4.3 Pair correlations and joint low tails (EVIDENCE)

Entry = residual correlation after OLS on residues of p mod 8, 3, 9, 5, 25, 7, 49, 11, …, 47 / joint-low-tail ratio
(observed number of p with both families ≤ their within-p-mod-840 5 % quantile, over the within-stratum independence
prediction). Rough = semiprime controls.

| pair | 1e8 | 1e9 | 1e10 | 1e11 | 1e12 | 1e13 | rough8 | rough9 |
|---|---|---|---|---|---|---|---|---|
| STAR–B1 | +0.483 / 3.74 | +0.495 / 3.74 | +0.501 / 3.97 | +0.532 / 2.44 | +0.541 / 2.01 | +0.548 / 1.41 | +0.486 / 3.75 | +0.480 / 3.74 |
| STAR–I1 | +0.388 / 3.11 | +0.403 / 3.29 | +0.409 / 2.98 | +0.452 / 2.21 | +0.464 / 1.53 | +0.408 / 1.10 | +0.393 / 3.01 | +0.395 / 3.11 |
| B1–I1 | +0.608 / 4.71 | +0.624 / 4.65 | +0.640 / 4.32 | +0.612 / 3.13 | +0.621 / 1.86 | +0.621 / 1.83 | +0.605 / 4.75 | +0.615 / 4.32 |
| STAR–c2 | +0.342 / 2.57 | +0.349 / 2.58 | +0.351 / 2.54 | +0.347 / 1.67 | +0.405 / 1.51 | +0.381 / 1.20 | +0.344 / 2.37 | +0.345 / 2.49 |
| STAR–c3 | +0.152 / 1.49 | +0.157 / 1.43 | +0.158 / 1.68 | +0.182 / 1.28 | +0.210 / 1.22 | +0.087 / 1.27 | +0.155 / 1.58 | +0.143 / 1.78 |
| c2–c3 | +0.074 / 1.21 | +0.067 / 1.19 | +0.065 / 1.11 | +0.094 / 0.88 | +0.102 / 1.13 | −0.004 / 1.01 | +0.066 / 1.28 | +0.079 / 1.15 |
| 𝔊*–K | +0.035 / 1.32 | +0.077 / 1.40 | +0.108 / 1.47 | +0.147 / 0.99 | +0.182 / 1.48 | +0.083 / 1.21 | +0.036 / 1.25 | +0.060 / 1.32 |
| B1–K | +0.159 / 1.78 | +0.165 / 1.81 | +0.170 / 1.93 | +0.226 / 1.10 | +0.253 / 1.56 | +0.180 / 1.29 | +0.158 / 1.94 | +0.158 / 1.71 |
| I1–K | +0.134 / 1.90 | +0.147 / 1.96 | +0.144 / 1.96 | +0.180 / 1.41 | +0.162 / 1.50 | +0.225 / 1.23 | +0.139 / 1.91 | +0.138 / 1.67 |
| STAR–QR | +0.158 / 1.40 | +0.184 / 1.34 | +0.202 / 1.47 | +0.189 / 1.48 | +0.261 / 1.47 | +0.254 / 1.52 | +0.155 / 1.43 | +0.196 / 1.32 |
| B1–QR | −0.013 / 1.09 | +0.015 / 0.89 | +0.027 / 1.12 | +0.058 / 1.22 | +0.049 / 0.82 | +0.079 / 1.20 | −0.011 / 1.03 | +0.011 / 0.69 |
| I1–QR | +0.049 / 1.42 | +0.078 / 1.34 | +0.099 / 1.48 | +0.159 / 2.06 | +0.217 / 1.40 | +0.169 / 1.29 | +0.047 / 1.32 | +0.081 / 1.21 |

(N = 108 397, 48 139, 25 226, 2 305, 960, 550, 30 000, 12 000. Nominal s.e. of r: 0.003 … 0.043. At 10¹¹–10¹³ the
96 classes mod 840 hold on average ≈ 24, 10, 6 primes, so the 5 % quantile events are coarse and the tail ratios are shrunk towards 1.) The other
16 pairs (`stats_*.txt`) are also positive for every certificate pair; the only non-positive entries involve QR or are
within one s.e. of 0 (c2–c3 at 10¹³). With partial correlations given INT (a collider for the interior W(p)-families; not
for the c-lines, which live on W(cp), nor for boundary words) the W(p)-certificate pairs stay positive (STAR–B1
+0.28…+0.46, B1–I1 +0.31…+0.46), I1–c2 and c2–c3 become slightly negative (−0.01…−0.07), and the W(p)-certificate–QR pairs
turn negative (B1–QR −0.52…−0.59, I1–QR −0.42…−0.47, STAR–QR −0.07…−0.15; QR–c2 stays positive): conditionally on the
size of the word set, the Jacobi split is the one clear complementarity, and it is between certificates and
non-certificates. (Unconditionally certificate–QR correlations are ≥ 0: STAR–QR +0.16…+0.26.)

### 4.4 Global (non-local) drivers (EVIDENCE; `lproxy_*.txt`)

Proxies: log of ∏_{ℓ < 20000}(1 − χ(ℓ)/ℓ)⁻¹ for χ_p and χ_{−4p}, residualised on the local design. Correlation of each
family/L² residual with them (10⁹, N = 48 139; 10¹⁰ agrees):

| | STAR | B1 | I1 | c2 | c3 | 𝔊* | K | QR | INT |
|---|---|---|---|---|---|---|---|---|---|
| log L(1, χ_p) | −0.019 | −0.025 | −0.018 | −0.020 | −0.021 | −0.017 | −0.010 | **+0.020** | −0.017 |
| log L(1, χ_{−4p}) | +0.064 | +0.051 | +0.016 | +0.029 | +0.030 | +0.066 | +0.007 | −0.009 | +0.018 |

Same sign on every certificate family; opposite (χ_p) on the placebo. (Pooled over p mod 8; BM_LVALUE Thm A's T(p)
changes sign with p mod 8, so no sign prediction is claimed. At 10¹², N = 960, the signs are mixed — noise.) Adding the proxies (quadratically) to the local controls changes pair
correlations by ≤ 0.03. So the class-number layer is a *common* factor, not a complementary one.

### 4.5 Registered falsifier: outcome (EVIDENCE)

Rule (checkpoint 1, commit 144b7268): a cross-family pair of certificate level bands is a **lead** if its residual
correlation is < −4 s.e. within p mod 840 at two scales and < −2 s.e. under the residue OLS (here extended to mod 16, 32,
27). `scripts/z57_complement_leads.py` (`leads.txt`): 921 pairs at 10⁸/10⁹/10¹⁰; 84 below −4 s.e. somewhere; **12 leads**:

* *Leads involving a congruence band (6):* STAR z7 vs c2 z8, c3 z8, B1 z8; STAR z6 vs c2 z8; c2 z6 vs c3 z8; STAR z0 vs
  c2 z6. Each involves at least one band with t ≥ p^{0.6}, i.e. pairs with uv ≤ p^{0.4}, which by Lemma W(e) is a
  congruence family modulo 4uv (both sides are, except STAR z0 in the last, whose size is ≤ 0.013). Sizes −0.01 to −0.06
  (−0.09 with L-proxies for STAR z7–B1 z8), not removed by residues to 199 — as expected, since the moduli 4uv reach
  p^{0.4} (`leadfollow_1e9.txt`, `leadfollow_1e10.txt`). **CRT test**
  (`scripts/z57_complement_toplocal.py`, 10 000 primes ≡ 1 (4) from 10¹⁰; STAR pairs 100 < uv ≤ 1000, others uv ≤ 100,
  i.e. the bands STAR z7, X z8): the exact local model (p uniform on units modulo the lcm) gives
  corr(STAR, c2/c3/B1) = −0.067/−0.064/−0.043 vs empirical −0.079/−0.070/−0.055 (s.e. 0.010), and reproduces c2–c3
  (+0.260 vs +0.277) and all means to 1–2 % (at 10¹² with uv ≤ 250 vs ab ≤ 16: STAR–c2 −0.110 vs −0.106). For these three
  the empirical value exceeds the model in the same direction by 0.6–1.2 s.e.; the leads STAR z6–c2 z8, c2 z6–c3 z8 and
  STAR z0–c2 z6 were not CRT-tested — their attribution to the same mutual exclusion of residue classes of cheap pairs
  (as FAMATTACK's C(3,4)) is Assessment, via Lemma W(e).
* *Bottom-band leads (6):* STAR z0 vs B1 z1, c2 z1; B1 z1 vs I1 z0; STAR z1 vs I1 z0, I1 z1; I1 z1 vs c2 z0 (t ≤ p^{0.2}).
  |r| ≤ 0.04 at 10⁸–10¹⁰, mostly shrinking under residues mod all primes ≤ 199 (e.g. STAR z0–B1 z1: −0.024 → −0.013 at
  10¹⁰, STAR z1–I1 z1: −0.033 → −0.020 at 10⁹; I1 z1–c2 z0 barely moves, −0.024 → −0.022). STAR z0–c2 z1 grows to −0.039 (−6.1 s.e.) at 10¹⁰ when the L-proxies are added. Not
  identified; Assessment: sign and size are those of the cross-integer CRT exclusion of Thm C(ii) (different integers
  p + u, cp + b: −Θ((log x)²) covariance, correlation ≍ −1/log x), plausibly the same effect as FAMATTACK's u(0,1);
  about one order of magnitude below the positive full-family couplings (0.15–0.64).
* **Kill condition for the full families met:** no pair of full *certificate* families is below −2 s.e. under local
  controls at any scale (QR–K −0.046 at 10⁸ and B1–QR −0.013 at 10⁸ are negative, but QR is not a certificate), and every
  full certificate pair has joint-low-tail ratio ≥ 1 at every scale except c2–c3 (0.88) and 𝔊*–K (0.99) at 10¹¹ and
  c3–K (0.99) at 10¹², within noise.

### 4.6 Joint zero census, all n ≡ 1 (4) ≤ 4·10⁶ (CERTIFIED counts; independence predictions EVIDENCE)

`census_summary.txt` (per-decade independence = Σ_decades N_dec·r_A·r_B):

| | primes (141 502) | non-square composites (857 499) |
|---|---|---|
| zeros STAR / B1 / I1 / c2 / c3 / 𝔊* / K | 12 / 3 / **0** / 493 / 3088 / 31 / 3778 | 257 / 41 / 26 / 5826 / 24605 / 1043 / 48065 |
| joint STAR&B1, STAR&I1, B1&I1 | 0, 0, 0 (pred. 0.0 each) | 2, 7, 4 (pred. 0.6, 0.3, 0.2) |
| joint STAR&c2, STAR&c3 | 1, 5 (pred. 0.6, 1.5) | 18, 48 (pred. 8.3, 21.8) |
| joint B1&c2, B1&c3, B1&K | 2, 1, 3 (pred. 0.3, 0.7, 0.5) | 12, 17, 32 (pred. 3.4, 7.4, 7.0) |
| joint c2&c3, 𝔊*&K | 53, 12 (pred. 33.1, 2.8) | 503, 257 (pred. 281, 94) |
| five-slice union zero | 0 | 1 (n = 105) |

Joint zeros never fall below the independence prediction by more than noise and are mostly 1.5–25× above it: positive
tail dependence, the opposite of complementarity. (I1, the Type I a = 1 slice with its boundary words, has no zero at
these primes, consistent with CONDITIONAL_ES §1/§8: it is the most robust single line, with S(5 101 441) = 1 recorded
there.) The 999 odd squares are zeros of every family.

### 4.7 Universality across rough composites (EVIDENCE)

On the 42 000 rough semiprimes (both factors ≥ n^0.4) every mean/L² agrees with the primes at the same height to
±0.001 (e.g. STAR 0.1630 vs 0.1630, B1 0.2924 vs 0.2922 at 10⁸) and every pair correlation of §4.3 to ±0.02 (e.g.
STAR–B1 +0.486 vs +0.483, B1–I1 +0.605 vs +0.608, 𝔊*–K +0.036 vs +0.035 at 10⁸; STAR–B1 +0.480 vs +0.495 at 10⁹);
joint-low-tail ratios agree within noise. So nothing in the *joint* law of the menu
distinguishes primes from rough semiprimes at this resolution — a complementarity mechanism would have to be invisible
in it (Assessment).

## 5. Where it stops; the escape hatch

1. **Local regime.** Top-level families are congruence families (Lemma W(e)); their negative couplings are CRT exclusion
   (§4.5). A union theorem built from them is a covering-congruence statement: fixed menus fail (B1, FRONTIER §3), and
   the moving menu is (★)/ES itself.
2. **Shared-integer regime.** Low-level parts of slices on one integer are positively coupled (Thm C, PROVED for bounded
   shifts, θ < 1/4, M-coprime divisors); on different integers negatively coupled only at lower order (CRT exclusion,
   correlation ≍ −1/log x). The regime Thm C leaves open — shifts up to √p and
   divisors beyond p^{1/4} — is exactly the tied-divisor regime of B2, and there the data (§4.3) are positive.
3. **The only complementary partner is the placebo.** Within the interior word set, certificates and QR are the two
   Jacobi halves (Lemma W(b)): R_STAR∪B1∪I1 ≥ 1 ⟺ (A/p) = −1 for some A ∈ L₃(p) or a boundary certificate exists; for
   p ≡ 1 (8) this is ES₅, λ(p) ≤ 3 (DEDEKIND_ES Cor 4.6; at p ≡ 5 (8) ES holds classically). A "complementarity theorem" against QR is therefore the statement that χ_p is not
   identically +1 on the sparse set L₃(p) of size ≍ log²p — a character sum over a p-dependent sparse set, B2 again
   (and false at squares, as it must be).
4. **Escape hatch (Assessment).** Theorem C's proof shows exactly where positivity comes from: the gcd-sharing pairs
   (ga, gb). A complementarity mechanism would need an *exact* relation between divisor classes of *different*
   integers (p + u vs p + u′, or p + u vs cp + b) that is not a congruence and not a size statement. FAMATTACK's Lemma L
   lists the known ones (switch, privacy, parity law); none forces a hit, and the measurements here (28 pairs, six
   scales, rough controls) show none at the resolution of counts.

## 6. Screens (FRONTIER §4) for the best idea (a complementarity/union argument over the menu)

1. **T1 squares:** passes trivially (every family is 0 at m², §4.6) — but Prop F shows the needed step must also fail at
   the non-square composite joint zeros (105, 4545, 2641, …), so it must use more than non-squareness and n ≡ 1 (4)
   (for three pairs all composite falsifiers found are divisible by 3; §3.3 caveat).
2. **8/131:** the menu families are numerator-4 objects; the numerator-8 c = 1 line fails at 835 primes ≤ 10⁶ including
   131, 241 (BM_CORRECTED_COUNT §4); a union argument insensitive to the numerator would be refuted there. Not tested
   further here.
3. **Tied modulus (B2):** fails — every family keeps the tied divisor event; unions only add main terms (Thm C regime) or
   are congruence coverings (local regime).
4. **Fixed p:** fails for Thm C (an average over p in a class; B6); the measurements are over primes, not at one p.

## 7. Verdict

**Narrowed (scoped negative).** Killed as a route (EVIDENCE, statistical): "two certificate families of the menu fail on
complementary sets beyond local data"; killed pointwise (CERTIFIED) for the four prime pairs of Prop F. Not killed:
a pointwise implication at primes for (★)&b = 1, (★)&Type I, b = 1&Type I, Type I&c2, Type I&c3 (no joint prime zero
≤ 4·10⁶). What is proved: Lemma W (unification; local exclusion of lifts), Theorem C (same-integer slices are
positively coupled at order (log x)³, different integers negatively coupled at order (log x)², over primes in any fixed
class), Prop F (implications R_A = 0 ⟹ R_B ≥ 1
are false at non-square composites for every pair and at primes for four pairs). What survives: complementarity through an
exact non-congruence relation between classes of divisors of different integers (none known), and the Jacobi statement
χ_p ≢ 1 on L₃(p) (= ES₅, already on FRONTIER).

## 8. Proposed FRONTIER text (do not edit FRONTIER here)

*§6 (dead ends), new line:* **Complementarity of certificate families** (`Z57_COMPLEMENT.md`). (★), b = 1, Type I a = 1
are the Jacobi-(−1) cells of one word set W(p); c-lines live on W(cp). Over primes in a fixed class, low-level parts of
slices on the same integer are positively correlated (Thm C, PROVED via BV; κ(log x)³ covariance from gcd-sharing divisor
pairs), parts on different integers negatively coupled only at lower order (CRT exclusion, correlation ≍ −1/log x);
top-level parts are congruence families whose negative couplings are CRT
exclusion (local). EVIDENCE 10⁸–10¹³ (+ rough semiprimes, same joint law): all 21 certificate pairs positive after
local and L-value controls (c2–c3 ≈ 0), joint low tails mostly 1.1–4.7× independence; given the word count, the only
anti-correlated partner of the certificates is the Jacobi-(+1) placebo. CERTIFIED: "R_A = 0 ⟹ R_B ≥ 1" is false at non-square composites for every pair and at primes for
(★)⇒c2 (102001), (★)⇒c3 (577, …), b=1⇒c2 (193, 2521), b=1⇒c3 (193). Do not retry without an exact non-congruence relation
between divisor classes of different integers.

*§2.1 census, addition:* Type I a = 1 (with boundary words) has no zero at primes p ≡ 1 (4) ≤ 4·10⁶; joint zeros of
(★), b = 1, Type I a = 1 at primes ≤ 4·10⁶: none (CERTIFIED, `Z57_COMPLEMENT.md` §4.6).

**Bottom line.** The failure sets of different certificate families are not complementary. All families of the menu
are cells of one or two word sets and their counts are divisor events of shared or unrelated integers; sharing couples
them positively (proved, for bounded shifts and small divisors, over primes in any residue class), not sharing leaves
only a lower-order negative CRT coupling, and the visible negative couplings are local congruence exclusions between
cheap pairs, which a covering argument
cannot turn into a theorem. Across 10⁸–10¹³ every certificate pair is positively dependent, joint low tails are more
frequent than independence, the class-number layer pushes every family the same way, and rough semiprimes show the same
joint law as primes. Unions help only by adding main terms. A union theorem over the menu would need an exact relation
between divisor classes of different integers that is neither a congruence nor a size statement; none is known. ES is
open.

## 9. Review log

* **Internal hostile review** (subagent, same model; read the memo, scripts, data and cited memos; light re-parsing of
  the data files). Verified: every number in §3.3, §4.3, §4.4, §4.5, §4.6 against the files; Lemma W (a)–(c); every step
  of Thm C(i) (BV range, multiplicity τ(l²) ≤ τ(l)², Cauchy–Schwarz error, the g = gcd lower bound, Möbius step, variance
  bound) and the boundary handling of Cor C1. Found 4 MAJOR issues, all fixed: (1) Thm C(ii) claimed zero cross-integer
  covariance; correct value is −Σ_{(m,m′)>1} 1/(φ(m)φ(m′)) = −Θ((log x)²) (CRT exclusion) — restated with proof, and the
  narrative ("uncoupled") corrected throughout; (2) c-line words at shifts b = cw live on the same integers p + w —
  added to Cor C1 (positive by (i)); (3) Prop F's consequence overclaimed "must use primality" — all composite falsifiers
  for three pairs are divisible by 3; narrowed, relabelled CERTIFIED; (4) only 3 of the 6 congruence-band leads were
  CRT-tested — said so, the rest Assessment. 17 MINOR fixes: boundary exception t = 1 in Lemma W(d)(e) and overlapping
  slices; sign exceptions and tail-ratio range (0.88–4.71, three entries < 1) in §0; partial-given-INT description;
  stratum sizes; 999 squares; composite excess 1.4–25×; rough-control tolerances (±0.003 / ±0.025); var/mean range;
  dropped an unjustified BM_LVALUE sign claim (T(p) changes sign with p mod 8); ES₅ equivalence restricted to p ≡ 1 (8)
  and to include boundary certificates; bottom-band lead size "one order" (not two) and the L-proxy growth of
  STAR z0–c2 z1; kill condition restricted to certificate pairs; "M-coprime" instead of "K-rough"; non-emptiness
  hypotheses; boundary B1 certificates justified; QR complementarity stated as conditional on the word count; verdict
  scoped (pointwise implications at primes for five pairs not excluded).
* Cross-model review: pending.
