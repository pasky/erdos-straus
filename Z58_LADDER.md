# Z58_LADDER — mechanism III (size-controlled covering), a primality-free rung, and the exponent-cap ladder

Status: z58 lane LADDER (brief `z52bbriefs/z58_lanes.md` §LADDER, rules `z52bbriefs/z53_depth.md` with z53 → z58).
Internal; one hostile internal review (§7). **ES is OPEN; nothing here proves or disproves ES or (MS).** Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_ladder_*`, data `data/z58/ladder/`
(≈ 10 kB). Notation as in `Z57_SYNTH.md`: R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}; 𝔐 = {1, 121, 169, 289, 361, 529}
⊂ (ℤ/840)^× (= the subgroup of squares; n ∈ 𝔐 ⇒ gcd(n, 210) = 1 and n ≡ 1 (mod 24)); n_p = least quadratic non-residue
mod p.

## 0. Summary and falsifier table

**Verdict: narrowed** (no HOT LEAD). Three results.
1. **Size-controlled covering (mechanism III) has a precise size scale and a precise cost** (§1). The symmetric least
   hit modulus μ(n) (least of the three congruence moduli 4uC − 1, 4BC − 1, 4uB over all solutions) satisfies
   n_p ≤ μ(p) ≤ 1.9231 (p+1)^{2/3} at primes p ≡ 1 (4) with R(p) ≥ 1 (PROVED). Hence (MS) is *exactly* a covering statement with moduli
   ≤ 1.93 p^{2/3}, and every size-controlled strengthening SC(D) with D(p) ≤ p^θ, θ < 1/(4√e), would prove a
   least-non-residue bound n_p ≤ p^θ for all large p ∈ 𝔐 — beyond Burgess (Prop 1.2, PROVED). Data to 10¹¹
   (CERTIFIED counts): P(μ(p) > D) over primes in 𝔐 is p-independent (0.2103, 0.01293, 1.77·10⁻⁴ at D = 10², 10³, 10⁴),
   and the record μ at 10¹⁰–10¹¹ is ≈ p^{0.5}. Model (Assessment): at the Salez threshold 10¹⁷ the hardest 𝔐 primes need
   symmetric moduli ≈ p^{0.42}; a Burgess-beating size control is reached only near p ≈ 10^{130}.
2. **A primality-free sufficient rung L2^𝔐** (§2): *R(n) ≥ 1 for every non-square n > P with n mod 840 ∈ 𝔐*. It
   implies (MS) at threshold P. CERTIFIED (two engines to 2·10⁷, one engine beyond): its zero set up to 10¹¹ is exactly
   9 primes and 18 composites, the last 17 401 609; **no zero among the 128 491 751 primes and 585 009 682 non-square
   composites in 𝔐 ∩ (10⁸, 10¹¹]**. This also extends the (★) prime census on 𝔐 from 10¹⁰ to 10¹¹ (one engine).
   Inside 𝔐, composites have the same μ-statistics as primes to two digits. So F3 does not force primality on 𝔐:
   on the domain of (MS), primality is used (empirically) only through n mod 840 ∈ 𝔐 and non-squareness.
3. **Exponent-cap ladder below (MS)** (§3): L2^{(k)}: some d ≡ 3 (4) has r = (−p mod d) | ((d+1)/4)^k. Every rung
   keeps T1 exactly (PROVED, all k ≤ ∞), and at all 14 known prime zeros of (★) and the three new 𝔐-composite zeros
   already R^{(2)} ≥ 3. The whole difficulty sits in the single step k = 2 → k = 1 (the exponent cap of FRONTIER (J)34).
4. Ladder logic (§4): a provable rung S with L3 ⟹ S ⟹ L2 would prove (MS); the meaningful targets are rungs *above* L2
   that are structurally easier (none found: SC(D) is beyond-Burgess for small D; L2^𝔐 is a lottery of the same size)
   and rungs below (§3). No arrow L6 ⟹ L5 or L5 ⟹ L4 was found.

**MANDATORY FALSIFIER TABLE** (for the lane's objects: size-controlled covering SC(D), the rung L2^𝔐, the cap ladder).

| screen | behaviour | identifiable step |
|---|---|---|
| **F1** odd squares | μ(m²) = ∞ (T1); L2^𝔐 excludes squares by hypothesis; R^{(k)}(m²) = 0 for every k ≤ ∞ (Lemma 3.1) | non-squareness enters only through χ_n = (·/n) being non-principal: a hit modulus needs a prime ℓ with χ_n(ℓ) = −1 (Lemma 1.1(c)); at squares no such ℓ exists |
| **F2** C-even sub-line | SC(D), L2^𝔐 and the cap ladder are *statements*; restricted to C even (moduli d ≡ 7 (8) and pair moduli 8uB) they become R₈-statements, false above 10¹⁰ (4 Mordell zeros) | **no step found** that fails on the C-even sub-line. Only d ≡ 3 (mod 8) hits are exclusively C-odd (d ≡ 3 (8) ⇒ uC odd). An argument for (MS) at 10¹⁰ must use them or a threshold > 1.09·10¹⁰ |
| **F3** composites | 270 of the 285 F3 composites are outside 𝔐 (265 have a factor 3, 5 or 7). In 𝔐: 18 composite zeros ≤ 10¹¹, last 17 401 609; none in (1.75·10⁷, 10¹¹]; μ-laws of composites and primes agree (§2) | primality is not needed on 𝔐 beyond 𝔐-membership + non-squareness + a threshold > 1.75·10⁷ (EVIDENCE). A proof of (MS) via L2^𝔐 would be primality-blind; F3 then only demands that it fail outside 𝔐 (e.g. at multiples of 3, 5, 7) |
| **F4** known zeros | SC(1.93p^{2/3}) ⟺ (MS) (Lemma 1.1(b)); fails at all 14 + (for L2^𝔐) 18 composite zeros | threshold: > 8 813 281 for (MS), > 17 401 609 for L2^𝔐; 𝔊*-zeros are irrelevant here (full family) |

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
satisfies χ_{−4uB}(−(u + B)) = −1 identically (FRONTIER §2.2, BL Thm 1.1); p ≡ −(u + B) (mod 4uB) gives
χ_{−4uB}(p) = (−uB/p) = (uB/p) = −1 (p ≡ 1 (4), p ∤ uB as uB < p), so uB has a prime factor ℓ with (ℓ/p) = −1 and
4uB > n_p. The role-swapped d-form 4BC − 1 is the d-form for the solution (B, u, C). ∎

**SC(D) (size-controlled covering).** *Every prime p > P in 𝔐 has μ(p) ≤ D(p).* By Lemma 1.1(b), SC(1.9231(p+1)^{2/3})
is (MS); smaller D gives rungs *above* (MS).

**Proposition 1.2 (PROVED, immediate from 1.1(c)).** SC(D) at threshold P implies n_p ≤ D(p) for every prime p > P in 𝔐.
In particular SC(p^θ) with θ < 1/(4√e) ≈ 0.1516 would give n_p ≤ p^θ for all large p ∈ 𝔐. The best unconditional bound
for every large prime is Burgess's n_p ≪_ε p^{1/(4√e)+ε} (classical; no improvement for all primes of a fixed residue
class mod 840 is known to us — Assessment). SC(exp(C√log p)) would imply n_p ≤ exp(C√log p), weaker than GRH's
n_p ≤ 2 log² p (Bach, used only as orientation) but far beyond Burgess.
Lower side, for comparison: Prop A.3 of Z57_SYNTH kills every bounded D; `POINTWISE_OMEGA13.md` Thm 5.1 (PROVED
modulo the cited inputs) gives Type II witness moduli ≥ exp(c(log p)^{1/4}(log log p)^{−1/4}) infinitely often.

**Data (CERTIFIED counts; one engine per range, cross-checked).**
* `scripts/z58_ladder_mu.c` (sieve over all solutions with a modulus ≤ CAP; `mu_1e8.txt` with Y = 100,
  `mu_1e8_Y11.txt` with Y = 11): all n ≡ 1 (4) ≤ 10⁸, CAP = 420 000 ≥ 1.9231(10⁸+1)^{2/3}, so "μ > CAP" ⟺ R(n) = 0.
  Reproduces exactly the 14 known prime zeros and the 20 F3 composites with least prime factor ≥ 11.
* `scripts/z58_ladder_mdec.c` (per-n exact decider: scan m = 3, 4, … ≤ 1.9231(n+1)^{2/3}, first hit wins; deterministic
  Miller–Rabin): all non-square n ∈ 𝔐 in [10³, 2·10⁷] (identical zero list to the sieve) and in (10⁸, 10¹¹]
  (`mdec_*.txt`). Its prime part reproduces the known absence of (★)-zeros at primes in 𝔐 ∩ (10⁸, 10¹⁰] (FRONTIER §2.1).
* μ over primes in 𝔐, by range (fraction with μ > 10², > 10³, > 10⁴):

| range | primes in 𝔐 | > 10² | > 10³ | > 10⁴ | max μ (at p) | log μ / log p |
|---|---|---|---|---|---|---|
| 10⁶–10⁷ | 18 143 | 0.2023 | 0.01240 | 1.1·10⁻⁴ | 14 559 (9 477 889) | 0.60 |
| 10⁷–10⁸ | 158 955 | 0.2086 | 0.01249 | 2.1·10⁻⁴ | 44 771 (98 943 049) | 0.58 |
| 10⁸–5·10⁹ | 7 159 582 | 0.2102 | 0.01288 | 1.9·10⁻⁴ | 193 763 (413 490 001) | 0.61 |
| 10¹⁰–3·10¹⁰ | 26 401 647 | 0.2103 | 0.01293 | 1.8·10⁻⁴ | 250 735 (13 205 460 241) | 0.53 |
| 5·10¹⁰–7.5·10¹⁰ | 31 434 779 | 0.2104 | 0.01293 | 1.7·10⁻⁴ | 579 007 (51 914 346 409) | 0.54 |
| 7.5·10¹⁰–10¹¹ | 31 005 959 | 0.2104 | 0.01294 | 1.8·10⁻⁴ | 237 467 (82 871 232 889) | 0.49 |

  Outside 𝔐 the hits are much cheaper (P(μ > 10²) ≈ 0.011 for primes p ≡ 1 (4) not in 𝔐, 10⁵–10⁸).
* *Reading (EVIDENCE + Assessment).* For D ≪ p^{2/3}, {μ(p) > D} is a congruence event of p modulo moduli ≤ D, so its
  density among primes in 𝔐 is a fixed number F(D) (Dirichlet); the table shows F(D) is already stable at 10⁶. A quadratic
  fit in log D through the three pooled points gives log F(D) ≈ −0.142 log²D + 0.42 log D − 0.49 (three points; Assessment).
  Setting F(D*) = 1/#{primes in 𝔐 ∩ [x, 2x]} reproduces the observed records (predicted ≈ 4·10⁵ at 10¹¹, observed
  2.4·10⁵–5.8·10⁵), and predicts D* ≈ 1.4·10⁷ ≈ p^{0.42} at x = 10¹⁷. The model's D* ≈ exp(2.66√log p) drops below
  p^{1/(4√e)} only for log p ≳ 306, i.e. p ≳ 10^{133}.
* *Consequence (Assessment).* Mechanism III in size-controlled form has no compression at practical thresholds: at
  10¹⁷ the hardest 𝔐 primes need symmetric moduli ≈ p^{0.4}, where "covering by small moduli" is not the regime; and
  any SC(D) proof in the regime where it *is* a small-moduli covering (D ≤ p^{0.15}) proves a beyond-Burgess least
  non-residue bound for 𝔐 primes (Prop 1.2). This is the III-analogue of Z57_SYNTH's calibration of mechanism I.

## 2. A primality-free rung: L2^𝔐

**L2^𝔐(P).** *R(n) ≥ 1 for every non-square n > P with n mod 840 ∈ 𝔐.* Since primes in 𝔐 are non-squares,
L2^𝔐(P) ⟹ (MS) at threshold P (PROVED, trivial). It is a rung *above* L2 that does not mention primality.

**Zero set (CERTIFIED: the sieve ≤ 10⁸ and the decider on [10³, 2·10⁷] agree; the decider alone on (10⁸, 10¹¹]).**
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

**μ-statistics, composites vs primes in 𝔐 (EVIDENCE).** Fractions with μ > 10², 10³, 10⁴ on (10⁸, 10¹¹]: composites
0.2315 / 0.01578 / 2.5·10⁻⁴, primes 0.2104 / 0.01293 / 1.8·10⁻⁴. For 100-rough composites in 𝔐, [10⁷, 10⁸]:
0.2091 / 0.0129 / 2.13·10⁻⁴ against primes 0.2086 / 0.0125 / 2.08·10⁻⁴ (`mu_1e8.txt`). The slight composite excess is
carried by small factors (11, 13, …), which delete the moduli they divide.

*Reading (Assessment).*
* F3 ("(MS) over all n ≡ 1 (4) is false") is a statement about the classes *outside* 𝔐 and about small factors:
  265 of the 285 composites have a factor 3, 5 or 7, which excludes every modulus divisible by it.
* On 𝔐, the composite analogue is consistent with all data above 1.75·10⁷ and certified empty on (1.75·10⁷, 10¹¹].
* So a proof of (MS) is allowed (by all known data) to be primality-blind on 𝔐: what it must use is non-squareness
  (F1), 𝔐-membership or a substitute (F3: it must fail at multiples of 3, 5, 7 or outside 𝔐), and a threshold
  > 1.75·10⁷ (F4).
* This removes one candidate source of a mechanism. A mechanism that needs p prime in a strong sense — e.g.
  irreducibility of a polynomial at p, a field ℚ(√p) with specific class-group behaviour, or (ℓ/p) for *all* ℓ as a
  multiplicative character modulo a prime — is not *required* by the data. Nothing here shows it is useless.
* It does not make (MS) easier. L2^𝔐 is the same lottery (same μ-law), on 4.5× as many integers.

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

*Reading.* Every rung keeps T1; the k = 2 rung is already a comfortable lottery at every known (★)-zero. The cap step
k = 2 → 1 (r | m² → r | m) is where all known failures live. This is the d-form instance of the exponent cap of
FRONTIER (J)34 and of the flat power ladder (J)108 — prior in substance. New here only as data at the zeros.

## 4. Ladder logic (PROVED, elementary) and arrows

* If S is a statement about primes in 𝔐 with L3 ⟹ S ⟹ L2 and S is proved, then L2 = (MS) is proved. So "a provable
  rung strictly between L2 and L3" is a proof of (MS). The useful questions are (i) rungs above L2 that are structurally
  easier, and (ii) provable rungs below L2.
* (i) The two rungs above L2 examined here are not easier. SC(D) for small D is beyond Burgess (Prop 1.2). L2^𝔐 is
  the same lottery. Restricting families (L3, L4, F_μ) shrinks the lottery (Z57_SYNTH §3.I).
* (ii) The cap ladder L2^{(k)} keeps T1. Its k = 2 rung shows no failures in this data (the zeros above all have
  R^{(2)} ≥ 3). This was not searched systematically.
* L6 ⟹ L5, L5 ⟹ L4: no arrow. L5 and L6 bound different remainders (X_𝔊* versus X), and L4 needs positivity inside H3 ⊂ 𝔊*. Neither
  remainder controls the other. No implication was found and none is claimed (Assessment; as in Z57_SYNTH Prop 1.1).

## 5. What would be a genuine fourth mechanism (Assessment)

Screened and discarded during the lane, with reasons:
* *Exact (threshold-free) mechanisms* — count congruences/parity (M5), involutions, identities, inverse theorems
  "R(n) = 0 ⟹ n square". All are refuted by F4 on 𝔐 itself: 9 prime and 18 composite non-square zeros in 𝔐. Any valid
  mechanism must contain a size condition that is false below 1.75·10⁷ on L2^𝔐 (8.8·10⁶ for primes).
* *Inverse/pretentious form of III* ("avoiders of all H_d, d ≤ D, are QR-like"): false in the finite form (A.3). At
  the zeros, n_p and the genus mass are ordinary (Z57_SYNTH §2.2; FAMDESIGN §4.5). The μ-law shows avoidance is a
  p-independent congruence lottery up to D ≈ p^{0.4} at 10¹⁷.
* *Multiplicative transfer* (from factors of n to n, or n ↦ kn). The only exact relation found is
  R(kn) ≥ #{solutions of n with k | C} (C ↦ C/k fixes 4Cn + 1 and keeps d ≡ −1 (mod 4C/k)). It does not propagate
  positivity to primes.
What survives: a counting mechanism with an explicit threshold (mechanism I, calibrated in Z57_SYNTH). A
primality-blind version on 𝔐 is not excluded by any known data (§2).

## 6. Proposed FRONTIER text (do not apply here) and bottom line

* §2.4, append: *(z58, `Z58_LADDER.md`.)*
  * Symmetric least hit modulus μ(n) = min over solutions of min(4uC − 1, 4BC − 1, 4uB). At primes p ≡ 1 (4) with
    R(p) ≥ 1, n_p ≤ μ(p) ≤ 1.9231(p+1)^{2/3} (PROVED). Hence a size-controlled covering SC(D) implies n_p ≤ D(p), which
    is beyond Burgess for D ≤ p^{0.15}.
  * Data to 10¹¹ (CERTIFIED counts): P(μ > 10², 10³, 10⁴) = 0.210, 0.0129, 1.8·10⁻⁴ for primes in 𝔐, stable from 10⁶.
    Records ≈ p^{0.5} at 10¹⁰–10¹¹. Model (Assessment): ≈ p^{0.42} at 10¹⁷.
  * **Primality-free rung L2^𝔐**: R(n) ≥ 1 for all non-square n > P in 𝔐 implies (MS). Its zeros ≤ 10¹¹ are 9 primes
    and 18 composites, the last 17 401 609. None among the 7.1·10⁸ non-square n ∈ 𝔐 ∩ (10⁸, 10¹¹] (CERTIFIED, one
    engine). This extends the (★) prime census on 𝔐 to 10¹¹.
* §4 item on composites (F3): *on 𝔐 the composite analogue of (MS) is consistent with all data above 1.75·10⁷;
  F3 is a statement about classes outside 𝔐 and small factors (265 of 285 have a factor 3, 5 or 7). An argument may
  be primality-blind on 𝔐 but must fail outside it or at multiples of 3, 5, 7.*
* §6, add: *(z58) Size-controlled covering (mechanism III): no compression at practical thresholds (μ ≈ p^{0.4–0.5}
  for the hardest 𝔐 primes); with moduli ≤ p^{0.15} it is at least as strong as a beyond-Burgess n_p bound on 𝔐 (PROVED
  implication). Exponent-cap ladder r | m^k: T1 for all k; all known failures at the k = 1 step.*

**Bottom line.** Mechanism III, made size-controlled and symmetric, is an exact reformulation of (MS) with moduli up to
1.93p^{2/3}. Shrinking the moduli is the only way it could become a "covering" argument. That costs a beyond-Burgess
least non-residue bound below p^{0.15}, while the data and model put the needed size near p^{0.4} at 10¹⁷. The census
side yields a primality-free sufficient rung: on Mordell's classes, non-square composites behave exactly like primes and
have no zero in (1.75·10⁷, 10¹¹]. So the F3 screen reduces to "uses 𝔐 and non-squareness, with a threshold". The
C-even screen F2 remains the one no idea here passes. B2 did not move. **ES is OPEN.**

## 7. Commands, files, review

* `gcc -O2 -o /tmp/z58mu scripts/z58_ladder_mu.c -lm`; `/tmp/z58mu 100000000 420000 100 > data/z58/ladder/mu_1e8.txt`
  and `… 11 > mu_1e8_Y11.txt` (≈ 1 min each, ≈ 1.2 GB).
* `gcc -O2 -o /tmp/z58mdec scripts/z58_ladder_mdec.c -lm`; `/tmp/z58mdec A B` for [10³, 2·10⁷], (10⁸, 5·10⁹],
  (5·10⁹, 10¹⁰], (10¹⁰, 3·10¹⁰], (3·10¹⁰, 5·10¹⁰], (5·10¹⁰, 7.5·10¹⁰], (7.5·10¹⁰, 10¹¹] → `mdec_*.txt` (≈ 30 min total
  CPU). All runs under `ulimit -v 4000000` and `timeout ≤ 1800`.
* `gcc -O2 -o /tmp/capk scripts/z58_ladder_capk.c`; `/tmp/capk <n…>` (§3 table).
* Review: see §8.

## 8. Review log
(pending)
