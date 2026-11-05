# Z58_LADDER — mechanism III (size-controlled covering), a primality-free rung, and the exponent-cap ladder

Status: z58 lane LADDER (brief `/home/pasky/projects/math/z52bbriefs/z58_lanes.md` §LADDER, rules
`/home/pasky/projects/math/z52bbriefs/z53_depth.md` with z53 → z58; both outside the repo). Internal; one hostile
internal review applied (§8). **ES is OPEN; nothing here proves or disproves ES or (MS).** Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_ladder_*`, data `data/z58/ladder/`
(≈ 10 kB). Notation as in `Z57_SYNTH.md`: R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}; 𝔐 = {1, 121, 169, 289, 361, 529}
⊂ (ℤ/840)^× (= the subgroup of squares; n ∈ 𝔐 ⇒ gcd(n, 210) = 1 and n ≡ 1 (mod 24)); n_p = least quadratic non-residue
mod p.

## 0. Summary and falsifier table

**Verdict: narrowed** (no HOT LEAD). Four results.
1. **Size-controlled covering (mechanism III) has a precise size scale and a precise cost** (§1). The symmetric least
   hit modulus μ(n) (least of the three congruence moduli 4uC − 1, 4BC − 1, 4uB over all solutions) satisfies
   n_p ≤ μ(p) ≤ 1.9231 (p+1)^{2/3} at primes p ≡ 1 (4) with R(p) ≥ 1 (PROVED). Hence (MS) is *exactly* a covering statement with moduli
   ≤ 1.93 p^{2/3}. Every size-controlled strengthening SC(D) implies n_p ≤ D(p) for all large p ∈ 𝔐; for
   D(p) ≤ p^θ, θ < 1/(4√e), that is a least-non-residue bound beyond Burgess (Prop 1.2, PROVED). Data to 10¹¹
   (CERTIFIED counts): the proportion of primes in 𝔐 with μ(p) > D is stable across ranges (pooled over (10⁸, 10¹¹]:
   0.2103, 0.01292, 1.77·10⁻⁴ at D = 10², 10³, 10⁴). The interval maxima of μ at 10¹⁰–10¹¹ are ≈ p^{0.5}. A three-point
   model (Assessment, extrapolation) predicts maxima ≈ p^{0.42} at 10¹⁷, and reaches the Burgess exponent only near
   p ≈ 10^{134}–10^{138}.
2. **A primality-free sufficient rung L2^𝔐** (§2): *R(n) ≥ 1 for every non-square n > P with n mod 840 ∈ 𝔐*. It
   implies (MS) at threshold P. CERTIFIED (two engines on [10³, 2·10⁷], the sieve alone on (2·10⁷, 10⁸], the decider
   alone on (10⁸, 10¹¹]): its zero set up to 10¹¹ is exactly 9 primes and 18 composites, the last 17 401 609; **no zero
   among the 128 491 751 primes and 585 009 682 non-square composites in 𝔐 ∩ (10⁸, 10¹¹]**. This also extends the (★)
   prime census on 𝔐 from 10¹⁰ to 10¹¹ (one engine). Inside 𝔐, composites have similar μ-tails to primes, with a
   measurable excess (§2); 100-rough composites match primes closely. So the known composite zeros do not exclude a
   proof that is primality-blind on 𝔐 above a threshold (Assessment).
3. **Exponent-cap ladder below (MS)** (§3): L2^{(k)}: some d ≡ 3 (4) has r = (−p mod d) | ((d+1)/4)^k. Every rung
   keeps T1 exactly (PROVED, all k ≤ ∞). At all 14 known prime zeros of (★) and the three new 𝔐-composite zeros,
   R^{(2)} ≥ 3; at all 18 𝔐-composite zeros R^{(2)} ≥ 1. All tested failures are removed at k = 2; proving any rung
   k ≥ 2 eventually remains open (this is the exponent cap of FRONTIER (J)34).
4. Ladder logic (§4): a provable rung S with L3 ⟹ S ⟹ L2 would prove (MS); the meaningful targets are rungs *above* L2
   that are structurally easier (none identified: SC(D) is beyond-Burgess for D ≤ p^{0.15}; L2^𝔐 is a lottery of the
   same kind) and rungs below (§3). No arrow L6 ⟹ L5 or L5 ⟹ L4 was found.

**MANDATORY FALSIFIER TABLE** (for the lane's objects: size-controlled covering SC(D), the rung L2^𝔐, the cap ladder).

| screen | behaviour | identifiable step |
|---|---|---|
| **F1** odd squares | μ(m²) = ∞ (T1); L2^𝔐 excludes squares by hypothesis; R^{(k)}(m²) = 0 for every k ≤ ∞ (Lemma 3.1) | for every n ≥ 1 a hit gives a d-form modulus d (coprime to n) with Jacobi (n/d) = −1, hence a prime ℓ | d with (n/ℓ) = −1; at a square no such d exists. (For composite n the *pair* modulus 4uB need not contain such a prime, e.g. (u, B, C) = (17, 918, 1), n = 61 489 ∈ 𝔐; at primes it does, Lemma 1.1(c).) |
| **F2** C-even sub-line | SC(D) and L2^𝔐 are *statements*. Restricted to C even — d-form: d ≡ 7 (8) **and** r | (d+1)/8; pair form: 8uB | n + u + B with n + u + B ≥ 8uB — they become R₈-statements, false above 10¹⁰ (4 Mordell zeros). For the relaxed cap rungs (k ≥ 2) the screen is *not* established: the four Mordell R₈-zeros, and 409, have numerator-8 k = 2 witnesses (r | ((d+1)/8)², e.g. 10 532 106 649: d = 79, r = 25) | **no step found** that fails on the C-even sub-line. Only d ≡ 3 (mod 8) hits are exclusively C-odd (d ≡ 3 (8) ⇒ uC odd). An argument for (MS) at threshold 10¹⁰ cannot stay valid for exact R₈-positivity; it must use C-odd hits or a threshold ≥ 10 868 474 401 for the sub-line |
| **F3** composites | 270 of the 285 F3 composites are outside 𝔐 (265 have a factor 3, 5 or 7); 15 are inside. In 𝔐: 18 composite zeros ≤ 10¹¹, last 17 401 609; none in (1.75·10⁷, 10¹¹]; μ-tails similar to primes with a measurable excess (§2) | the known composite zeros are finite lists; they refute threshold-free statements only. They do not exclude a primality-blind proof on 𝔐 with threshold ≥ 17 401 609, nor a still broader eventual theorem for non-squares (EVIDENCE + Assessment). The idea's use of primality is therefore: none beyond the domain (𝔐) and non-squareness |
| **F4** known zeros | On primes in 𝔐, SC(1.9231(p+1)^{2/3}) at threshold P is MS(P) (Lemma 1.1(b)); it fails at the nine in-domain prime zeros (14 in the p ≡ 1 (4) census); L2^𝔐 also at 18 composite zeros | thresholds: P ≥ 8 813 281 for MS(P), P ≥ 17 401 609 for L2^𝔐(P) (convention n > P). The fixed-threshold (MS) (P = 10¹⁷) is not touched; 𝔊*-zeros concern a sub-family and are irrelevant here |

## 1. Mechanism III, size-controlled and symmetric

**Definition.** μ(n) := min over (★)-solutions (u, B, C) of min(4uC − 1, 4BC − 1, 4uB); μ(n) = ∞ if R(n) = 0.

**Lemma 1.1 (PROVED).** Let (u, B, C) ∈ ℕ³ solve 4uBC − u − B = n.
* (a) n ≡ −u (mod 4uC − 1), n ≡ −B (mod 4BC − 1), n ≡ −(u + B) (mod 4uB). Conversely: if d ≡ 3 (4), d ≥ 3,
  r := (−n mod d) ≥ 1 and r | (d+1)/4, then (u, C, B) = (r, (d+1)/(4r), (n+r)/d) is a solution; if 4uB | n + u + B
  and n + u + B ≥ 4uB, then C := (n + u + B)/(4uB) gives a solution.
* (b) min(4uC − 1, 4BC − 1, 4uB) ≤ (64/9)^{1/3}(n + 1)^{2/3} < 1.9231 (n + 1)^{2/3}. Hence R(n) ≥ 1 ⟺ some modulus
  m < 1.9231(n+1)^{2/3} carries a hit of one of the two shapes in (a).
* (c) If p ≡ 1 (mod 4) is prime and R(p) ≥ 1, then μ(p) ≥ n_p.

*Proof.* (a) n + u = B(4uC − 1), n + B = u(4BC − 1), n + u + B = 4uBC. The d-form converse is Lemma A.1(a) of
`Z57_SYNTH.md`; the pair-form converse is immediate. (b) (4uC)(4BC)(4uB) = 4(4uBC)² = 4(n + u + B)². From
(u − 1)(B − 1) ≥ 0, uB ≥ u + B − 1, so n = 4uBC − u − B ≥ 3(u + B) − 4 and n + u + B ≤ (4n + 4)/3. The least of three
positive numbers is at most the cube root of their product: min ≤ (4·(16/9)(n+1)²)^{1/3}. (This is FAMTRY §4.5's bound.)
(c) d-form: p ≡ −u (mod d) and (−u/d) = −1 (Lemma A.1(b)), so the Jacobi symbol (p/d) = −1 and some prime ℓ | d has
(p/ℓ) = −1; ℓ is odd and (ℓ/p) = (p/ℓ) since p ≡ 1 (4); so d ≥ ℓ ≥ n_p. Pair form: the Kronecker character χ_{−4uB}
satisfies χ_{−4uB}(−(u + B)) = −1 whenever gcd(u, B) = 1 and u + B is odd (FRONTIER §2.2; `BM_CORRECTED_COUNT.md`
Thm 1.1). At a prime p these hold automatically: gcd(u, B) divides 4uBC − u − B = p and u, B < p (from u + B ≤ uB + 1,
p ≥ 3uB − 1, so uB ≤ (p+1)/3), so gcd(u, B) = 1; and p odd forces u + B odd. Then p ≡ −(u + B) (mod 4uB) gives
χ_{−4uB}(p) = (−uB/p) = (uB/p) = −1 (p ≡ 1 (4), p ∤ uB), so uB has a prime factor ℓ (possibly 2) with (ℓ/p) = −1, and
4uB > n_p. The role-swapped d-form 4BC − 1 is the d-form for the solution (B, u, C). (n_p need not be odd; the proof
does not use it.) For composite n the pair-form part fails: (u, B, C) = (17, 918, 1) gives n = 61 489 ∈ 𝔐 with
4uB = 2³·3³·17² and no prime ℓ | 4uB with (n/ℓ) = −1. The d-form part holds for every n (with χ_n in place of (·/p)). ∎

**SC(D) (size-controlled covering).** *Every prime p > P in 𝔐 has μ(p) ≤ D(p).* By Lemma 1.1(b), SC(1.9231(p+1)^{2/3})
is (MS); smaller D gives rungs *above* (MS).

**Proposition 1.2 (PROVED, immediate from 1.1(c)).** SC(D) at threshold P implies n_p ≤ D(p) for every prime p > P in 𝔐.
This is a necessary consequence, not an impossibility result for SC(D). In particular SC(p^θ) with
θ < 1/(4√e) ≈ 0.1516 would give n_p ≤ p^θ for all large p ∈ 𝔐. The best unconditional bound
for every large prime is Burgess's n_p ≪_ε p^{1/(4√e)+ε} (classical; no improvement for all primes of a fixed residue
class mod 840 is known to us — Assessment). SC(exp(C√log p)) would imply n_p ≤ exp(C√log p), weaker than GRH's
n_p ≤ 2 log² p (Bach, used only as orientation) but far beyond Burgess.
Lower side, for comparison. **Corollary 1.3 (PROVED).** SC(D) fails for every bounded D. *Proof.* By Dirichlet there are
infinitely many primes p ≡ 1 (mod 840·∏_{ℓ ≤ D} ℓ); such p lie in 𝔐 (class 1), have (2/p) = 1 (p ≡ 1 (8)) and
(ℓ/p) = (p/ℓ) = 1 for odd ℓ ≤ D, so n_p > D and μ(p) > D by Lemma 1.1(c) (or μ = ∞). ∎ (Z57_SYNTH Prop A.3 is the
d-form-only analogue.) `POINTWISE_OMEGA13.md` Thm 5.1 (PROVED modulo the cited inputs) gives Type II witness moduli
≥ exp(c(log p)^{1/4}(log log p)^{−1/4}) infinitely often.

**Data (CERTIFIED counts; one engine per range; the two engines agree on their overlap [10³, 2·10⁷]).**
* `scripts/z58_ladder_mu.c` (sieve over all solutions with a modulus ≤ CAP; `mu_1e8.txt` with Y = 100,
  `mu_1e8_Y11.txt` with Y = 11): all n ≡ 1 (4) ≤ 10⁸, CAP = 420 000 ≥ 1.9231(10⁸+1)^{2/3}, so "μ > CAP" ⟺ R(n) = 0.
  Reproduces exactly the 14 known prime zeros and the 20 F3 composites with least prime factor ≥ 11.
* `scripts/z58_ladder_mdec.c` (per-n exact decider: scan m = 3, 4, … up to the largest m with 9m³ ≤ 64(n+1)², checked
  in 128-bit integers; first hit wins; no coprimality imposed on pair forms, so exact for composites; deterministic
  Miller–Rabin): all non-square n ∈ 𝔐 in [10³, 2·10⁷] (identical zero list to the sieve) and in (10⁸, 10¹¹]
  (`mdec_*.txt`). Its prime part reproduces the known absence of (★)-zeros at primes in 𝔐 ∩ (10⁸, 10¹⁰] (FRONTIER §2.1).
* μ over primes in 𝔐, by range: unconditional fractions with μ > 10², > 10³, > 10⁴ (zeros, μ = ∞, counted in every
  tail; the two lowest rows contain 4 and 0 zeros), and the maximum *finite* μ in the interval:

| range | primes in 𝔐 | > 10² | > 10³ | > 10⁴ | interval max finite μ (at p) | log μ / log p |
|---|---|---|---|---|---|---|
| 10⁶–10⁷ | 18 143 | 0.2025 | 0.01262 | 3.3·10⁻⁴ | 14 559 (9 477 889) | 0.60 |
| 10⁷–10⁸ | 158 955 | 0.2086 | 0.01249 | 2.1·10⁻⁴ | 44 771 (98 943 049) | 0.58 |
| 10⁸–5·10⁹ | 7 159 582 | 0.2102 | 0.01288 | 1.9·10⁻⁴ | 193 763 (413 490 001) | 0.61 |
| 5·10⁹–10¹⁰ | 6 876 657 | 0.2101 | 0.01292 | 1.8·10⁻⁴ | 96 360 (9 526 341 889) | 0.50 |
| 10¹⁰–3·10¹⁰ | 26 401 647 | 0.2103 | 0.01293 | 1.8·10⁻⁴ | 250 735 (13 205 460 241) | 0.53 |
| 3·10¹⁰–5·10¹⁰ | 25 613 127 | 0.2103 | 0.01291 | 1.8·10⁻⁴ | 298 171 (36 503 286 481) | 0.52 |
| 5·10¹⁰–7.5·10¹⁰ | 31 434 779 | 0.2104 | 0.01293 | 1.7·10⁻⁴ | 579 007 (51 914 346 409) | 0.54 |
| 7.5·10¹⁰–10¹¹ | 31 005 959 | 0.2104 | 0.01294 | 1.8·10⁻⁴ | 237 467 (82 871 232 889) | 0.49 |

  Pooled over (10⁸, 10¹¹]: 128 491 751 primes, tail numerators 27 024 568 / 1 660 737 / 22 757 (`fit.txt`).
  Outside 𝔐 the hits are much cheaper (P(μ > 10²) ≈ 0.011 for primes p ≡ 1 (4) not in 𝔐, 10⁵–10⁸).
* *Reading.* (PROVED) For fixed D and p > max moduli, {μ(p) > D} depends only on p modulo the lcm of the moduli ≤ D, so
  the prime number theorem in arithmetic progressions gives a limiting proportion F(D) among primes in 𝔐 (a limit with D
  fixed; no uniformity in growing D). (EVIDENCE) The observed proportions are stable from 10⁶ to 10¹¹ at D ≤ 10⁴.
  (Assessment, extrapolation; `scripts/z58_ladder_fit.py` → `fit.txt`) An exact three-point quadratic fit (no residual
  degrees of freedom) gives log F(D) ≈ −0.1415 log²D + 0.418 log D − 0.482. The expected-exceedance size D* with
  F(D*) = 1/#{primes in 𝔐 ∩ [x, 2x]} is ≈ 4.0·10⁵ at x = 10¹¹ (observed interval maxima 2.4·10⁵–5.8·10⁵) and
  ≈ 1.4·10⁷ ≈ x^{0.42} at x = 10¹⁷. To leading order D* ≈ exp(2.66√log x). That drops below x^{1/(4√e)} at
  log₁₀ x ≈ 133.5; with the full fitted equation the crossover is at log₁₀ x ≈ 137.8. These are heuristic
  extrapolations of a fixed-D law to a growing-D extreme tail. They do not bound any maximum.
* *Consequence (Assessment).* In this model, size-controlled covering shows no compression at practical thresholds:
  at 10¹⁷ the model predicts that the hardest 𝔐 primes need symmetric moduli ≈ p^{0.4}, far above "small moduli".
  Separately and rigorously, any SC(D) with D ≤ p^{0.15} implies a beyond-Burgess least non-residue bound for 𝔐 primes
  (Prop 1.2). This is the III-analogue of Z57_SYNTH's calibration of mechanism I. It is not a no-go for covering
  arguments with moduli between p^{0.15} and p^{2/3}.

## 2. A primality-free rung: L2^𝔐

**L2^𝔐(P).** *R(n) ≥ 1 for every non-square n > P with n mod 840 ∈ 𝔐.* Since primes in 𝔐 are non-squares,
L2^𝔐(P) ⟹ (MS) at threshold P (PROVED, trivial). It is a rung *above* L2 that does not mention primality.

**Zero set (CERTIFIED: the sieve ≤ 10⁸ and the decider on [10³, 2·10⁷] agree; the sieve alone on (2·10⁷, 10⁸]; the
decider alone on (10⁸, 10¹¹], all six runs exited 0, `mdec_*.txt.status`).**
Non-square n ≤ 10¹¹ in 𝔐 with R(n) = 0:
* 9 primes: 5569, 9601, 83449, 102001, 712321, 1 724 209, 1 726 201, 5 212 561, 8 813 281 (the known ones);
* 18 composites: 1969 = 11·179, 2641 = 19·139, 5161 = 13·397, 18001 = 47·383, 23881 = 11·13·167, 90889 = 97·937,
  112849 = 11·10259, 199369 = 193·1033, 345361 = 29·11909, 349609 = 13·26893, 510169 = 11·19·2441,
  539281 = 23·23447, 897961 = 443·2027, 2 956 321 = 211·14011, 3 210 601 = 19·37·4567, **8 725 201 = 29·300869,
  12 538 801 = 11·47·79·307, 17 401 609 = 47·370247** (the last three are above the F3 range 8·10⁶; the first fifteen
  are exactly the 𝔐-members of the F3 list).
* None in (17 401 609, 10¹¹]: 128 491 751 primes and 585 009 682 non-square composites in 𝔐 ∩ (10⁸, 10¹¹] were decided
  positive, plus the sieve range (2·10⁷, 10⁸].

All 18 composite zeros are squarefree; 7 of 18 have a factor 11 or 13 (the smallest primes allowed in 𝔐). Outside 𝔐, the
11-rough (gcd(n, 210) = 1) non-square composites ≤ 10⁸ with R = 0 are 2929, 12001, 25441, 752257, 810001 and
29 210 401 = 11·31·85661 (from `mu_1e8_Y11.txt`).

**μ-statistics, composites vs primes in 𝔐 (EVIDENCE).** Fractions with μ > 10², 10³, 10⁴ pooled over (10⁸, 10¹¹]:
composites 0.2315 / 0.01578 / 2.48·10⁻⁴ (numerators 135 443 883 / 9 232 800 / 145 119 of 585 009 682), primes
0.2103 / 0.01292 / 1.77·10⁻⁴. The composite excess is ≈ 10 %, 22 %, 40 % — similar tails, not equal ones. For
100-rough composites in 𝔐 on [10⁷, 10⁸] the match is close: 0.2091 / 0.01292 / 2.13·10⁻⁴ against primes
0.2086 / 0.01249 / 2.08·10⁻⁴ (`mu_1e8.txt`). Hypothesis (not measured): the excess comes from small factors 11, 13, …,
which delete every d-form modulus they divide (gcd(n, d) = 1 is forced for d-forms; pair forms need not be coprime to n,
see Lemma 1.1 proof).

*Reading (Assessment).*
* F3 ("(MS) over all n ≡ 1 (4) is false") refutes the threshold-free statement over all n ≡ 1 (4). 265 of its 285
  composites have a factor 3, 5 or 7, 15 lie in 𝔐. As finite lists, neither F3 nor the lists here refute an eventual
  statement, inside or outside 𝔐.
* On 𝔐, the composite analogue is consistent with all data above 1.75·10⁷ and certified empty on (1.75·10⁷, 10¹¹].
* So the known data allow a proof of (MS) that is primality-blind on 𝔐, using non-squareness (F1) and a threshold
  ≥ 17 401 609 (F4). 𝔐 is a convenient sufficient domain; the data do not show it is a necessary ingredient.
* This removes one candidate source of a mechanism. A mechanism that needs p prime in a strong sense — e.g.
  irreducibility of a polynomial at p, a field ℚ(√p) with specific class-group behaviour, or (ℓ/p) for *all* ℓ as a
  multiplicative character modulo a prime — is not *required* by the data. Nothing here shows it is useless.
* It does not make (MS) easier. L2^𝔐 is a lottery of the same kind (similar μ-tails) on 5.55× as many integers
  (non-square composites outnumber primes in 𝔐 ∩ (10⁸, 10¹¹] by 4.55 : 1).

## 3. The exponent-cap ladder below (MS)

For k ∈ ℕ ∪ {∞} let R^{(k)}(n) := #{d ≡ 3 (4), 3 ≤ d ≤ (4n+1)/3 : r := (−n mod d) ≥ 1 and r | m^k}, m := (d+1)/4
(for k = ∞: rad(r) | m). R^{(1)} = R (Lemma A.1(a)), and R^{(k)} increases with k.

**Lemma 3.1 (PROVED).** For every odd m₀ and every k ≤ ∞, R^{(k)}(m₀²) = 0.
*Proof.* Let d ≡ 3 (4) and r | m^k (rad(r) | m), m = (d+1)/4; then gcd(r, d) = 1 since gcd(m, d) = 1. For an odd prime
ℓ | r, ℓ | m gives d ≡ −1 (mod ℓ), so (ℓ/d) = (d/ℓ)(−1)^{((ℓ−1)/2)((d−1)/2)} = (−1/ℓ)(−1)^{(ℓ−1)/2} = 1, as (d−1)/2 is
odd. If 2 | r then 2 | m, d ≡ 7 (8) and (2/d) = 1. So (r/d) = 1 and (−r/d) = −1. If n = m₀² ≡ −r (mod d), then
gcd(m₀, d) = 1 and (−r/d) = (m₀/d)² = 1, a contradiction. ∎

**Data (CERTIFIED, `scripts/z58_ladder_capk.c`, exhaustive over d).** At the 14 prime zeros, the three new 𝔐-composite zeros, and square controls:

| n | R^{(2)} | R^{(3)} | R^{(4)} | R^{(∞)} |
|---|---|---|---|---|
| 409 / 577 / 5569 / 9601 | 4 / 6 / 6 / 3 | 4 / 7 / 9 / 4 | 4 / 7 / 9 / 5 | 4 / 8 / 9 / 8 |
| 23929 … 712321 (5 primes) | 12–17 | 17–31 | 18–41 | 19–52 |
| 1 134 241 … 8 813 281 (5 primes) | 18–30 | 28–51 | 35–66 | 51–89 |
| 8 725 201, 12 538 801, 17 401 609 | 21, 23, 33 | 39, 42, 41 | 51, 51, 53 | 71, 77, 77 |
| 9, 225, 1225, 9801 (controls) | 0 | 0 | 0 | 0 |

*Reading.* Every rung keeps T1. The k = 2 rung already has hits at every tested (★)-zero (R^{(2)} ≥ 3 at the 14 prime
zeros and the three new composites; ≥ 1 at all 18 𝔐-composite zeros, the minimum 1 at 2641; `capk_zeros.txt`). All
tested failures live at the cap step k = 2 → 1 (r | m² → r | m). No eventual theorem for any rung k ≥ 2 is proved
here. This is the d-form instance of the exponent cap of FRONTIER (J)34 and of the flat power ladder (J)108 — prior in
substance; new here only as data at the zeros.

## 4. Ladder logic (PROVED, elementary) and arrows

* If S is a statement about primes in 𝔐 with L3 ⟹ S ⟹ L2 and S is proved, then L2 = (MS) is proved. So "a provable
  rung strictly between L2 and L3" is a proof of (MS). The useful questions are (i) rungs above L2 that are structurally
  easier, and (ii) provable rungs below L2.
* (i) For the two rungs above L2 examined here, no easier route was identified. SC(D) with D ≤ p^{0.15} implies a
  beyond-Burgess bound (Prop 1.2). L2^𝔐 is a lottery of the same kind. Restricting families (L3, L4, F_μ) shrinks the
  lottery (Z57_SYNTH §3.I).
* (ii) The cap ladder L2^{(k)} keeps T1. Its k = 2 rung has hits at every tested zero (§3); it was not searched
  systematically, and no rung is proved.
* L6 ⟹ L5, L5 ⟹ L4: no arrow. L5 and L6 bound different remainders (X_𝔊* versus X), and L4 needs positivity inside
  H3 ⊂ 𝔊*. Neither remainder controls the other. No implication was found and none is claimed (Assessment; as in
  Z57_SYNTH Prop 1.1).

## 5. Candidate fourth mechanisms screened (Assessment)

Screened and set aside during the lane, with reasons (not exhaustive):
* *Exact (threshold-free) mechanisms* — count congruences/parity (M5), involutions, identities, inverse theorems
  "R(n) = 0 ⟹ n square". Any such statement asserted on 𝔐 without a threshold is refuted by the 9 prime and 18 composite
  non-square zeros in 𝔐 (on primes alone: by the 9 prime zeros). A valid mechanism needs a size condition that fails
  below 8 813 281 (primes) or 17 401 609 (L2^𝔐).
* *Inverse/pretentious form of III* ("avoiders of all H_d, d ≤ D, are QR-like"): false in the finite form (A.3,
  Cor 1.3). At the zeros, n_p and the genus mass are ordinary (Z57_SYNTH §2.2; FAMDESIGN §4.5). For fixed D, avoidance is a
  congruence event with a limiting density (§1). The model extends this to D ≈ p^{0.4} at 10¹⁷; that extension is
  extrapolation.
* *Multiplicative transfer* (n ↦ kn). The only exact relation found: if (u, B, C) solves n and k | C, then
  (ku, kB, C/k) solves kn (4·ku·kB·C/k − ku − kB = k(4uBC − u − B)). So R(kn) ≥ #{solutions of n with k | C}. It
  does not propagate positivity to primes.
Not excluded: a counting mechanism with an explicit threshold (mechanism I, calibrated in Z57_SYNTH), possibly
primality-blind on 𝔐 (§2); covering arguments with moduli in [p^{0.15}, p^{2/3}]; anything not listed here.

## 6. Proposed FRONTIER text (do not apply here) and bottom line

* §2.4, append: *(z58, `Z58_LADDER.md`.)*
  * Symmetric least hit modulus μ(n) = min over solutions of min(4uC − 1, 4BC − 1, 4uB). At primes p ≡ 1 (4) with
    R(p) ≥ 1, n_p ≤ μ(p) ≤ 1.9231(p+1)^{2/3} (PROVED). Hence a size-controlled covering SC(D) implies n_p ≤ D(p) on 𝔐,
    which is beyond Burgess for D ≤ p^{0.15}. SC(D) is false for every bounded D (n_p argument).
  * Data to 10¹¹ (CERTIFIED counts): for primes in 𝔐, P(μ > 10², 10³, 10⁴) ≈ 0.210, 0.0129, 1.8·10⁻⁴, stable from 10⁶.
    Interval maxima ≈ p^{0.5} at 10¹⁰–10¹¹. Three-point model (Assessment, extrapolation): ≈ p^{0.42} at 10¹⁷.
  * **Primality-free rung L2^𝔐**: R(n) ≥ 1 for all non-square n > P in 𝔐 implies (MS). Its zeros ≤ 10¹¹ are 9 primes
    and 18 composites, the last 17 401 609. None among the 7.1·10⁸ non-square n ∈ 𝔐 ∩ (10⁸, 10¹¹] (CERTIFIED, one
    engine). This extends the (★) prime census on 𝔐 to 10¹¹ (one engine).
* §4 item on composites (F3): *on 𝔐 the composite analogue of (MS) is consistent with all data above 1.75·10⁷. The
  finite composite lists (F3 and these) refute only threshold-free statements, so they do not exclude a proof that is
  primality-blind on 𝔐 with an adequate threshold, or a broader eventual theorem. 265 of the 285 F3 composites have a
  factor 3, 5 or 7.*
* §6, add: *(z58) Size-controlled covering (mechanism III): with moduli ≤ p^{0.15} it implies a beyond-Burgess n_p bound
  on 𝔐 (PROVED implication); in the model, the hardest 𝔐 primes need μ ≈ p^{0.4–0.5} at practical sizes (Assessment).
  Exponent-cap ladder r | m^k: T1 for all k; all tested failures are removed at k = 2.*

**Bottom line.** Mechanism III, made size-controlled and symmetric, is an exact reformulation of (MS) with moduli up to
1.93p^{2/3}. Below p^{0.15} it would yield a beyond-Burgess least non-residue bound. The data and an extrapolated model
put the moduli the hardest 𝔐 primes need near p^{0.4–0.5} at practical sizes. The census side yields a primality-free
sufficient rung. On Mordell's classes, non-square composites have similar μ-tails to primes, with a measurable excess.
They have no zero in (1.75·10⁷, 10¹¹]. So known data do not force primality on 𝔐 beyond non-squareness plus a
threshold. The C-even screen F2 remains the one no idea here passes. B2 did not move. **ES is OPEN.**

## 7. Commands, files, review

* `gcc -O2 -o /tmp/z58mu scripts/z58_ladder_mu.c -lm`; `/tmp/z58mu 100000000 420000 100 > data/z58/ladder/mu_1e8.txt`
  and `… 11 > mu_1e8_Y11.txt` (≈ 1 min each, ≈ 1.2 GB).
* `gcc -O2 -o /tmp/z58mdec scripts/z58_ladder_mdec.c -lm`; `/tmp/z58mdec A B` for [10³, 2·10⁷], (10⁸, 5·10⁹],
  (5·10⁹, 10¹⁰], (10¹⁰, 3·10¹⁰], (3·10¹⁰, 5·10¹⁰], (5·10¹⁰, 7.5·10¹⁰], (7.5·10¹⁰, 10¹¹] → `mdec_*.txt` (≈ 30 min total
  CPU; the ranges were run twice, before and after the review fixes, with identical results). All runs under `ulimit -v 4000000` and `timeout ≤ 1800`.
* `gcc -O2 -o /tmp/capk scripts/z58_ladder_capk.c`; `/tmp/capk <n…>` → `capk_zeros.txt` (§3 table).
* `python3 scripts/z58_ladder_fit.py data/z58/ladder/mdec_*.txt > data/z58/ladder/fit.txt` (§1 model).
* Each large decider run appends its exit status and arguments to `mdec_*.txt.status` (all 0).

## 8. Review log

* **Hostile internal review** (`data/z58/ladder/internal_review.md`): REQUEST CHANGES, 7 MAJOR + 6 MINOR, no FATAL. The
  reviewer re-verified Lemmas 1.1, 3.1 and Prop 1.2, and reran the decider on [10³, 2·10⁷] (byte-identical). It also
  cross-checked μ(n) against brute-force enumeration for all n ≤ 20 000, the interval maxima, the capk table, the counts
  285/270/265/15/20, and the fit. Fixes:
  1. The (5·10¹⁰, 10¹¹] outputs are committed. All large ranges were rerun with exit-status files.
  2. Tail fractions now count zeros (μ = ∞) in every tail; maxima are "maximum finite μ". The ≤ 10⁸ rows were regenerated
     (10⁶–10⁷: 3.3·10⁻⁴, not 1.1·10⁻⁴); raw tail numerators are printed.
  3. F2: the exact C-even condition is r | (d+1)/8 (d-form), and the R₈ screen is not established for the relaxed cap rungs.
     The reviewer's numerator-8 k = 2 witnesses are quoted.
  4. F1 and the small-factor explanation are restricted to d-forms; the composite pair-form example 61 489 was added; the
     excess explanation is labelled a hypothesis.
  5. F3 conclusions are rescoped: finite lists refute only threshold-free statements, and 𝔐 is sufficient, not shown
     necessary.
  6. The fixed-D density (PNT in APs) is separated from the extrapolated growing-D model; "predicts", not "need".
  7. Necessity and exhaustiveness rhetoric was removed (§§0, 4–6).
  8. The prime hypotheses of the pair-form identity are made explicit. Cor 1.3 (bounded D via n_p) replaces the A.3
     attribution.
  9. Crossovers: leading order 10^{133.5}, full model 10^{137.8} (`fit.py`).
  10. Input/range validation, allocation checks, a divisor-capacity guard, the exact integer cap 9m³ ≤ 64(n+1)², and the
      capk range guard were added.
  11. F4: nine in-domain prime zeros; P ≥ z.
  12. "Similar tails with a measurable excess" (10/22/40 %); population ratio 5.55×; interval maxima.
  13. Counts, links and brief paths were fixed; the capk output is stored; the C code is reformatted.

* **Cross-model review** (`data/z58/xreview/REVIEW_LADDER.md`): ACCEPT-WITH-FIXES. Every claim was rated CORRECT, or
  CORRECT as a one-engine certificate or Assessment. The reviewer independently checked μ(n) for n ≤ 25 000, reproduced
  the stored runs byte-identically, decided 42 832 high-range 𝔐 inputs pointwise, recounted the census population, and
  recertified the 12 R₈ zeros. One required fix (MINOR, documentation only) was applied: the Miller–Rabin comment in
  `scripts/z58_ladder_mdec.c` now reads "deterministic for all uint64". The old claim, that 12 bases are deterministic
  below 3.3·10²⁴, was false (counterexample 318665857834031151167461). No results change. The review's scope
  qualifications are kept in §6: one engine; fixed D versus growing D; a beyond-Burgess bound on 𝔐 only; the model is
  not a bound.
