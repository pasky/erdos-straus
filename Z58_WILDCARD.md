# Z58_WILDCARD — HOT TARGET, NO MECHANISM: the full Type II family passes all four falsifiers (statement level, bounded ranges)

**ES is OPEN; nothing here proves or disproves it.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Lane WILDCARD of wave z58 (`z52bbriefs/z58_lanes.md`; common rules `z53_depth.md` with z53 → z58).
Scripts `scripts/z58_wildcard_*`, data `data/z58/wildcard/` (≈ 14 MB). Status: **final; hostile review applied (§7)**.

**One-line verdict.** Among targets carried by the campaign, the full Elsholtz–Tao Type II family is the one whose
*statement* survives F1–F4. In the tested ranges:
* no odd prime ≤ 10¹⁰ is a zero;
* the only odd non-square zero ≤ 10¹⁰ is 4545;
* the d-even half (= numerator 8) has no odd non-square zero in (1 239 315, 10⁹], and the d-odd half has none in
  (9121, 10⁹].

So the numerator-8 trap of (MS) is not reproduced in the tested ranges. All of this is bounded computation plus
elementary lemmas. **No mechanism was found**: the single-residue pointwise wall (B2) is unchanged.

Verdict: **strengthened (choice of target) / inconclusive (mechanism).** The target itself is prior (Z57_BFII; notes
§§60–61, `C_SQ′`). New here:
* the falsifier-screen profile;
* the numerator ladder with its twisted T1 (Lemma 4.3);
* a scaling bijection;
* an explicit necessary condition for zeros;
* a calibrated zero-rate model.

"HOT TARGET" is an Assessment about the statement. It is not the brief's mechanism-level HOT LEAD.

## 0. Mandatory falsifier table (committed at checkpoint 1 in `40c1af69`; final form after review)

Object: N_II(n) := #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = a + b + nc} (ET (2.15)). (★) is its c = 1 line, (u,B,C) = (a,b,d). For a
prime p, N_II(p) ≥ 1 ⟹ 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp) ⟹ ES(p). Numerator-K version:
N^{(K)}(n) := #{K·abcd = a + b + nc}, K ≡ 0 (mod 4).

| screen | behaviour of the target CONV-II / (MS-II) | label |
|---|---|---|
| **F1 odd squares** | N_II(m²) = 0 for every m (Z57_BFII Prop 2.2 / Cor 2.3: every witness f = 4acd − 1 has (n/f) = −1). CONV-II says that, apart from the excluded 4545, T1 is the only obstruction on odd n, so non-squareness is the hypothesis itself. Any proof must produce a witness f with (n/f) = −1. At primes the genus-level form of this step is PROVED (Theorem G, Z57_BFII App. A): the twisted character ψ*χ_u is never principal because p, with p ∤ u, divides the conductor of χ_u. For composite n the analogous step needs an odd prime of the squarefree kernel s(n) that does *not* divide u. Shared factors can cancel: at n = 4545 = 505·3² and u = 505, −nu = −1515² has conductor 4. The composite genus analysis is only heuristic here. Numerator K: the obstruction is n = s·m² for every odd s ∣ K/4 (Lemma 4.3, PROVED). CERTIFIED for K = 12: 2 887 of the 3 802 zeros ≤ 10⁸ have the form 3m². | PROVED (squares, primes' genus step) + CERTIFIED |
| **F2 numerator 8 / C-even** | The C-even half of (★) (= c = 1 line of numerator 8) has 12 prime zeros in [10¹⁰, 1.1·10¹⁰]. The full numerator-8 family N^{(8)} is exactly the d-even half of N_II (Lemma 4.1). Among odd non-squares ≤ 10⁹ it has **22 prime zeros (last 35 569; in 𝔐: 1129, 3361, 35 569) and 107 composite zeros (last 1 239 315)**. The complementary d-odd half has exactly 8 odd non-square zeros ≤ 10⁹: 13, 301, 445, 685, 1981, 3105, 4545, 9121. At the 12 R₈-zeros N^{(8)} has witnesses f ≤ 1311. **In the tested range the F2 trap does not reproduce for the full family.** An argument that also proves the numerator-8 statement must have threshold P ≥ 35 569 (primes) or ≥ 1 239 315 (all odd non-squares). That is harmless at 10¹⁰, unlike the C-even sub-line. Eventual positivity of N^{(8)} is a CONJECTURE. | CERTIFIED (≤ 10⁹) |
| **F3 composites** | (★) has 285 non-square composite zeros ≤ 8·10⁶. **N_II has exactly one odd non-square zero ≤ 10¹⁰: 4545 = 3²·5·101.** This extends Z57_BFII (10⁷) and notes §61 (10⁶). 284 of the 285 (★)-composite zeros have N_II ≥ 1. Partial explanation (PROVED, Lemma 4.2): N_II(nk) ≥ 1 whenever n has a solution with k ∣ c (or, via (b), with k ∣ d). This is *conditional* inheritance. Positivity does not pass to multiples in general: N_II(5) > 0 but N_II(4545) = 0. Removing every non-coprime solution (ET coprimality gcd(abd, n) = 1) leaves 142 zeros ≤ 10⁸. **Every one of them is divisible by 3 or 5** (137 by 3, 5 more with least prime factor 5); all are ≡ 1 (mod 4), and the last is 21 754 425. Empirical reading (CONJECTURE CONV-II-15): beyond non-squareness, the coprime form needs only gcd(n, 15) = 1. The N_II form needs nothing beyond excluding 4545. | CERTIFIED + PROVED |
| **F4 known zeros** | N_II ≥ 1 at all 14 (★)-zeros and all 38 𝔊*-zeros (least witness ≤ 239), and at the 12 R₈-zeros (≤ 295). No odd prime ≤ 10¹⁰ has N_II = 0. The 14 (★)-zero primes (not the 𝔊*- or R₈-zeros, which have c = 1 solutions) are zeros of the c = 1 line. So an argument for a statement that covers them, e.g. CONV-II at a threshold below 8 813 281, cannot run through the c = 1 line alone. (MS-II) at threshold 10¹⁷ is not logically forced to use c ≥ 2. Using c ≥ 2 is this lane's *proposed strategy*, suggested by the robustness data. | CERTIFIED |

**Reading (Assessment).** CONV-II passes all four screens in the tested ranges, so it is a **HOT TARGET**. It is not a
hot lead in the mechanism sense. Passing the screens is a property of a *statement plus bounded data*; §5 explains why no
mechanism found here moves B2.

## 1. Precise statements

* **CONV-II (CONJECTURE).** Every odd non-square n ≥ 3 other than n = 4545 has N_II(n) ≥ 1.
  * The predicate is CERTIFIED for n ≤ 10¹⁰ (§3).
  * PROVED for n ≡ 3 (mod 4) by Lemma 4.4(a). So CONV-II is a statement about n ≡ 1 (mod 4).
  * Prior form: notes §60.2 `C_SQ′` over all n, including even n and the sporadics 288 and 336.
* **CONV-II-15 (CONJECTURE).** Every odd non-square n with gcd(n, 15) = 1 has a solution with gcd(abd, n) = 1 (a genuine
  ET Type II solution). The predicate is CERTIFIED for n ≤ 10⁸.
* **(MS-II) (CONJECTURE).** Every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 has N_II(p) ≥ 1.
  * (MS) ⟹ (MS-II), since c = 1 is a sub-family.
  * (MS-II) + Mordell's reduction + Salez (10¹⁷) ⟹ ES (PROVED relative to those, exactly as for (MS)).
  * The predicate N_II(p) ≥ 1 is CERTIFIED for every odd prime p ≤ 10¹⁰. So the internal-census variant at threshold
    10¹⁰ has no exceptional prime below its threshold.
* **CONV-II(K) (CONJECTURE, K ≡ 0 mod 4).** The zero set of N^{(K)} on odd n is
  {s·m² : s odd, s ∣ K/4} ∪ (a finite set).
  * The first part is PROVED to consist of zeros (Lemma 4.3). Finiteness is conjectural for every K.
  * Data on the finite part:
    * K = 8: 129 integers ≤ 10⁹, none in (1 239 315, 10⁹].
    * K = 12: 915 integers ≤ 10⁸ outside 3m², last prime 1 998 793, last composite 19 156 825.
    * K = 16: zeros still present near 10⁸ (last prime 12 895 921, last composite 94 165 635).
  * For K ≥ 8 the tests stop at 10⁸–10⁹, so the data cannot confirm finiteness for any K.
  * Trivially N^{(K)}(n) = 0 when K > n + 2, so finite-part thresholds are unbounded over K.

## 2. Quick pass on the four leads

* **(i)+(ii) full Type II / converse of T1: adopted.** It had the best falsifier outcome by far (table above).
* **(iii) r-spectrum.** Write ℛ(n) for the set {r : rn + 1 has a divisor ≡ −1 (mod r)}, as distinct from the count R(n).
  The natural closure law, multiplicativity, is false in one line:
  * 2 ∈ ℛ(n) for every odd n;
  * 4 ∉ ℛ(409), since R(409) = 0.

  No other selection law gave a quick falsifier outcome. Not pursued.
* **(iv) varying fields Q(√(−Cp)) / joint divisor constraints.** No quick computation.
  * The slice forms of Type II already *are* such joint constraints: f | cn + a with f ≡ −1 (mod 4ac); f | n + 4a²d;
    f | 4c²dn + 1.
  * Lemma 4.4(b) extracts their rigid part. Pushing further means a sieve/norm-form route (§5).

## 3. Computations

**Engine** `scripts/z58_wildcard_census.c`. For each odd n it looks for the least f ≡ −1 (mod K), f ≤ FMAX, with
−n mod f ∈ T_f := {a·c⁻¹ : ac | (f+1)/K}. This is Z57_BFII Lemma 1.1(d); its proof works verbatim for any K, and
b = (cn + a)/f ≥ 1 is automatic.

A non-square with no witness ≤ FMAX (a "LATE" record) is decided *exactly* by the (a,b)-loop
  K·a·b·d = n + e, e | a + b, 1 ≤ e ≤ a + b
(e = (a+b)/c). Since K·ab > a + b, each (a,b) has at most one candidate e; the loop takes a ≤ b, with the necessary
bound K·a² ≤ n + 2a. The fallback returns *some* witness, not necessarily the least. The engine's "max least witness" is
over bitmap hits only.

Modes:
* coprime mode: gcd(a,n) = gcd(d,n) = 1; gcd(b,n) = 1 then follows from bf = cn + a;
* d-odd mode: env `Z58DODD=1`.

The program checks its arguments (K ≡ 0 mod 4, LP64).

Validation:
* (V1) FMAX = 3 sends 6 596 non-squares ≤ 2·10⁴ to the exact path. The zero set is identical ({4545}), and likewise in
  d-odd mode on n ≤ 3·10⁴.
* (V2) It reproduces Z57_BFII's 10⁷ zero set.
* (V3) `scripts/z58_wildcard_screens.py` recomputes T_f by independent code at every falsifier integer. It builds
  explicit (a,b,c,d), checks K·abcd = a + b + nc, and for K = 4 checks 4/n = 1/x + 1/y + 1/z exactly.
* (V4) Odd-square counts match exactly (4 999 below 10⁸; 34 189 in [10⁹, 10¹⁰)).
* (V5) The hostile reviewer (§7) ran an independent (a,b,d,e) enumerator to 10⁵. It matched every zero list there:
  K4 {4545}; K8 123; K12 797; K16 2 359; coprime 86; d-odd 8; K20 primes 634; K24 primes 1 230. It also re-checked all
  267 527 stored LATE witnesses and all P/C flags.

| run (odd n) | non-square zeros | notes |
|---|---|---|
| K = 4, [1, 10⁸), FMAX 2·10⁴ | **4545** | max least witness (hits) 14 111 (n = 92 455 209); primes 2 495 (p = 2 031 121) |
| K = 4, [10⁸, 10⁹) | none | one LATE n (302 812 197), exact loop gives f = 151 406 099; primes: max least witness 3 359 (p = 281 850 319 ≡ 3 mod 4) |
| K = 4, [10⁹, 10¹⁰) | none | every non-square has a witness ≤ 2·10⁴ (max 19 711); primes: max 3 799 (p = 6 736 278 481) |
| K = 4 coprime, [1, 10⁸) | 142, all divisible by 3 or 5 | last 21 754 425 |
| K = 4 d-odd, [1, 10⁹), FMAX 4·10⁴ | 13, 301, 445, 685, 1981, 3105, 4545, 9121 | |
| K = 8, [1, 10⁹) | 129 (22 primes) | last prime 35 569, last composite 1 239 315 |
| K = 12, [1, 10⁸) | 3 802 (2 887 of the form 3m²) | non-twisted: last prime 1 998 793, last composite 19 156 825 |
| K = 16, [1, 10⁸) | 5 269 (447 primes) | still present near 10⁸ |
| K = 20 / 24, primes ≤ 10⁸ | 1 164 / 3 740 prime zeros (raw, incl. obstructed 5, resp. 3) | last 94 965 203 / 96 577 729 |

Runtime (not archived): the K = 4 run on [10⁹, 10¹⁰) took about 34 s on this host, because most n hit f = 3, 7 or 15.

**Squarefree-kernel profile** (`z58_wildcard_kernels.py` → `kernels.txt`; EVIDENCE). Apart from the PROVED 3m² family
at K = 12, the composite zeros are not twisted squares with small kernel:
* (★): 0 of 285 have kernel ≤ 15;
* K = 16: 55 of 4 822.

Most of them are squarefree with small prime factors (3, 5, 7).

**Count samples** (`z58_wildcard_count.c`, exact ordered counts):
* `counts_K4to24_1e6.txt`: every second prime p ≡ 1 (4) in [10⁶, 1.1·10⁶), 1 821 primes;
* `counts_K4to24_mordell_1e6_3e6.txt`: all 4 258 primes in 𝔐 in [10⁶, 3·10⁶).

Means (mean N^{(K)}/L³) and zeros on the first sample:

| K | 4 | 8 | 12 | 16 | 20 | 24 |
|---|---|---|---|---|---|---|
| p ≡ 1 (4) | 0.0762 | 0.0329 | 0.0159 | 0.0141 | 0.0107 | 0.0067 |
| 𝔐 | 0.0507 | 0.0209 | 0.0120 | 0.0084 | 0.0071 | 0.0049 |
| zeros of the c = 1 line (first sample) | 0 | 7 | 53 | 118 | 198 | 363 |
| zeros of the full family (first sample) | 0 | 0 | 0 | 2 | 1 | 25 |

**Zero-rate model** (`z58_wildcard_ladder2.py` → `ladder2.txt`). The fit is EVIDENCE; every use for K = 4 is
Assessment, conditional on an unvalidated model.
* *Setup.* For each population the mean count λ_K comes from the matching count sample. Zero counts per decade come
  from the census files, all primes ≤ 10⁸, excluding primes with an odd prime factor of K/4.
* *Model.* z_{K,k} ~ Poisson(π_k·exp(A − B·λ_K L_k³)). It is fitted by maximum likelihood on *all* (K, decade) bins
  with K = 8…24 and decades 10¹–10⁷, zero bins included. (`z58_wildcard_ladder.py` / `ladder.txt` keep the first
  least-squares version, which used only bins with ≥ 3 zeros and mismatched populations; they are superseded.)
* *P1, p ≡ 1 (4).* rate = exp(−0.18 − 0.250·λL³), but the deviance is 409 on 33 df, a poor fit. For K = 4 it predicts
  5.4 prime zeros in 10¹–10⁷ (3.8 in [10, 100), 1.5 in [100, 1000)), and 0 are observed. So on all p ≡ 1 (4) the law
  does not describe K = 4.
  * A plausible structural reason (PROVED ingredient, Z57_BFII Prop 3.1): the moduli 3, 7, 15 are complete for
    numerator 4. They solve every p that is a non-residue mod 3, 5 or 7, i.e. 7/8 of primes. For numerator 8 the same
    moduli 7 and 15 are not complete (T_7 = {1}, T_15 = {1, 2, 8}).
  * No classification of complete moduli for other K is claimed.
* *P2, 𝔐 classes, where Mordell's identities give nothing.* rate = exp(0.42 − 0.315·λL³), with deviance 65.5 on 23 df:
  over-dispersed by about 3×; a poor fit. Most bins with positive counts are within a few-fold of the fit; the worst
  observed/fit ratio is ≈ 4.8 (K = 12, decade 5), and zero bins enter only through the deviance. Neither fitted model
  is validated for pointwise use.
* *K = 4 under the P2 law.* It predicts 0.0096 prime zeros in 𝔐 below 10⁸, and 0 are observed. This is consistent,
  but only extremely weakly so: the Poisson probability of seeing 0 is ≈ 0.99. Nested numerators share primes and
  events, so no independent-Poisson significance is claimed. The fitted x-range ends at 107.7: the K = 4 decade-5 value
  (x ≈ 103) lies inside it, and the decade-6 and decade-7 predictions lie outside it.
* *Reading.* On the domain of (MS-II) the data are consistent with K = 4 behaving like the ladder at its larger mean
  count (λ₄/λ₈ ≈ 2.4 on 𝔐). This is compatibility only. It shows neither that numerators 4 and 8 differ *only* through
  the mean, nor anything about individual primes (B6). Example of another arithmetic difference: f = 11 is a K = 4
  modulus forbidden for K = 8, and it solves p = 4201 ≡ 1 (mod 840) via (1, 382, 1, 3).
* *Scale at 10¹⁷.* Arithmetic extrapolation, not a certified mean: ≈ (0.05–0.076)·39.1³ ≈ 3·10³–4.5·10³ solutions for
  the full family, against ≈ 200–250 for (★).

## 4. Lemmas (PROVED, elementary)

**Lemma 4.1 (numerator nesting).** For k ≥ 1 the map (a,b,c,d) ↦ (a,b,c,kd) is a bijection from the solutions of
kK·abcd = a + b + nc onto the solutions of K·abcd = a + b + nc that have k | d. In particular:
* N^{(8)} is the d-even half of N_II;
* the C-even half of (★) is the c = 1 line of N^{(8)} (= Z57_SYNTH Lemma 2.1).

*Proof.* kK·abcd = K·abc(kd). ∎

**Lemma 4.2 (scaling bijection).** Let N = nk with n, k ≥ 1.
* (a) (a,b,c,d) ↦ (a, b, kc, d/k) is a bijection {solutions for N with k | d} → {solutions for n with k | c}.
* (b) (a,b,c,d) ↦ (a/k, b/k, c, kd) is a bijection {solutions for N with k | a and k | b} → {solutions for n with k | d}.

*Proof.*
* (a) 4ab(kc)(d/k) = 4abcd = a + b + Nc = a + b + n(kc). The inverse is (a,b,c,d) ↦ (a, b, c/k, kd).
* (b) Dividing by k: 4(a/k)(b/k)c(kd) = 4abcd/k = (a + b + Nc)/k = a/k + b/k + nc. The inverse is
  (a,b,c,d) ↦ (ka, kb, c, d/k): 4k²ab·c·d/k = k(a + b + nc).
* Checked as set equalities on 7 composites for all k ≤ 11, also independently by the reviewer. ∎

*Consequence.* Inheritance is conditional on the divisibility hypothesis:
* a solution of n with k | c gives one of nk via (a);
* a solution of n with k | d gives one of nk via (b)⁻¹.

Positivity alone does not pass to multiples (N_II(5) > 0, N_II(4545) = 0). The lemma is empty at primes and does not
explain why primes have no zeros.

A solution of N is non-coprime (gcd(abd, N) > 1) iff it is lifted from N/ℓ for some prime ℓ | N:
* if ℓ | d, use (a);
* if ℓ | a, then ℓ | b (because bf = cN + a and gcd(f, N) = 1), so use (b).

That is why the coprime census is the honest F3 test; it leaves zeros only at multiples of 3 or 5.

**Lemma 4.3 (T1 for numerator K).** Let K ≡ 0 (mod 4), let n be odd, and let f = K·acd − 1 be a witness. Then
(n/f) = −1 (Jacobi). Hence N^{(K)}(s·m²) = 0 for every odd s | K/4 and every odd m.

*Proof.*
* f ≡ −1 (mod K·ac). Z57_BFII Lemma 2.1 with k = (K/4)·ac and with k = K/4 gives ((K/4)·ac / f) = ((K/4)/f) = 1, so
  (ac/f) = 1.
* As in Prop 2.2 there, −n ≡ a·c⁻¹ (mod f), a unit. So (−n/f) = 1 and (n/f) = (−1/f) = −1.
* For n = s·m² with odd s | K/4 and gcd(m, f) = 1: f ≡ −1 (mod 4s), so (s/f) = 1 by Lemma 2.1 with k = s, and
  (n/f) = 1. This is a contradiction.
* If a prime ℓ divides both m and f, then f | cn + a forces ℓ | a, contradicting gcd(a, f) = 1 (f ≡ −1 mod a). ∎

*Use.* This is the exact K-dependence of the *proved* square obstruction. It does not prove that these are the only
infinite zero families. For K = 4 and K = 8 the obstruction is the odd squares alone (for K = 8, 2m² is even).

**Lemma 4.4.**
* (a) For odd n ≡ 3 (mod 4), (1, 1, 2, (n+1)/4) solves 4abcd = a + b + nc, coprimally.
* (b) Suppose n ≡ 1 (mod 4) and N_II(n) = 0. Then every prime factor of (n+1)/2, of n + 4 and of 4n + 1 is ≡ 1 (mod 4).
  In particular n is a non-zero quadratic residue modulo each of these primes.

*Proof.*
* (a) 4·1·1·2·(n+1)/4 = 2n + 2 = 1 + 1 + 2n.
* (b) Let ℓ ≡ 3 (mod 4) be a prime. It gives a solution with f = ℓ in each case:
  * ℓ | n + 1 (equivalently ℓ | (n+1)/2): (a, c) = (1, 1), d = (ℓ+1)/4, b = (n+1)/ℓ.
  * ℓ | n + 4: (a, d) = (1, 1), c = (ℓ+1)/4, b = (cn+1)/ℓ. This is integral because 4(cn+1) = n(ℓ+1) + 4 and
    gcd(4, ℓ) = 1.
  * ℓ | 4n + 1: (c, d) = (1, 1), a = (ℓ+1)/4, b = (n+a)/ℓ. This is integral because 4(n+a) = 4n + 1 + ℓ.
* For a prime ℓ ≡ 1 (mod 4) dividing these integers, n ≡ −1, −4 or −1/4 (mod ℓ), so (n/ℓ) = (−1/ℓ) = 1. ∎

*Use.* The odd zeros of N_II lie in the explicit set
  S₃ := {n ≡ 1 (4) : (n+1)/2, n + 4, 4n + 1 have only prime factors ≡ 1 (mod 4)}.
* Odd squares lie in S₃: (m²+1)/2 = ((m−1)/2)² + ((m+1)/2)², m² + 2² and (2m)² + 1 are all sums of two coprime squares.
* 4545 lies in S₃: 2273, 4549 and 18181 are primes ≡ 1 (mod 4).
* The (★)-zeros in general do not. For example 409 + 4 = 7·59, and (1, 117, 2, 1) solves Type II for 409.
* Size of S₃ (Assessment; standard Selberg upper-bound sieve): for each prime ℓ ≡ 3 (mod 4), ℓ ≠ 3, the three forms
  exclude three residue classes, so the sieve dimension is 3/2 and #S₃ ∩ [1, X] ≪ X/(log X)^{3/2}. No matching lower
  bound is claimed; the true order is a heuristic.

So the "explicit sparse set" asked about in lead (ii) is PROVED only in the weak form Z(N_II) ∩ odd ⊂ S₃ (squares
included). Heuristically S₃ contains infinitely many primes, so rigid slices cannot finish the job.

## 5. Mechanism attempts and why each stops (Assessment unless labelled)

1. **Genus main term.** Theorem G (Z57_BFII, PROVED) gives genus mass ≥ 10⁻¹⁰ (log p)³ at primes. Its non-squareness step
   uses p ∤ u and p | conductor.
   * For composite n the conductor can lose shared factors (F1 row). The genus term of a composite is not analysed
     here.
   * At primes the genus term is not the obstruction: the order-≥ 3 remainder is (Z57_BFII §5.2). **B2 unchanged.**
2. **Inheritance (Lemma 4.2).** Conditional on divisibility, and empty at primes. It gives no prime statement.
3. **Rigid slices (Lemma 4.4(b)).**
   * The three modulus-4 slices force a dimension-3/2 sieve condition.
   * Already at modulus 8, failure allows two index-2 subgroups ({1,3} or {1,5} mod 8), only one of which is the kernel
     of the relevant character. So a prime ℓ ≡ 5 (mod 8) with (n/ℓ) = −1 can divide n + 2 or 2n + 1 without producing
     a witness.
   * Joint emptiness of all slices is a pointwise sieve event; for a single n only upper-bound sieves are available
     (B6).
   * Reciprocity constrains only the total product, e.g. (n/(n+4)) = 1 automatically (CLASS_FORCING Thm 2.1).
4. **Numerator ladder.** It gives a calibration (§3), not a proof.
   * An argument that also proves numerator-K statements must have thresholds at or above the observed zeros of each
     such K. Observed last prime zeros: 35 569, 1 998 793, ≥ 12 895 921 and ≥ 94 965 203 for K = 8–20.
   * On 𝔐 the data are compatible with K = 4 behaving like the ladder at its larger mean count. No mechanism
     distinguishing the numerators was found.
5. **Witness growth.** The maximal least witness at primes is 2 495 (≤ 10⁸), 3 359 (≤ 10⁹) and 3 799 (≤ 10¹⁰), i.e.
   ≈ 0.3·L³ at the observed records. A polylog bound would imply one for n_p, since W ≥ n_p (Z57_BFII Cor 2.4). That
   is the WITNESS lane's territory.

**What would count as a mechanism (Assessment).** A fixed-p argument that uses non-squareness at a named step (F1). It
must not lean on small prime factors of n: in the coprime form, zeros ≤ 10⁸ occur only at 3 | n or 5 | n. If it also
covers the (★)-zero primes, it must use c ≥ 2. None was found. The best available sufficient condition remains
Z57_BFII §5.5 (SB ⟹ f_II ≥ 1), a single-prime equidistribution statement at characters of all orders.

## 6. Verdict, proposed FRONTIER text, bottom line

**Verdict.** **Strengthened (choice of target)** and **inconclusive (mechanism)**: no new pointwise step, and B2 did not
move.

New this lane:
* (a) CERTIFIED: the N_II predicate for odd n ≤ 10¹⁰ (zeros: squares and 4545); the coprime form for n ≤ 10⁸; N^{(8)}
  and the d-odd half for n ≤ 10⁹; the ladder K ≤ 24 for n ≤ 10⁸.
* (b) PROVED: Lemmas 4.1–4.4 (nesting; scaling bijection; T1 for numerator K with the s | K/4 twist; n ≡ 3 (4)
  trivial; the rigid-slice necessary condition S₃).
* (c) EVIDENCE: a Poisson zero-rate law across numerators 8–24. On 𝔐 it is compatible with K = 4; on all p ≡ 1 (4) it
  fits poorly, and K = 4 beats it.

**Proposed FRONTIER text (do not edit FRONTIER; for the integrator).**
* §2.4 / ladder: add the rung **(MS-II)**: N_II(p) ≥ 1 for p > 10¹⁷ in 𝔐. It is implied by (MS) and sufficient for ES.
  No odd prime ≤ 10¹⁰ is a zero; the only odd non-square zero ≤ 10¹⁰ is 4545 (`Z58_WILDCARD.md`, CERTIFIED). The
  numerator-8 analogue (= d-even half) has no prime zero in (35 569, 10⁹].
* §4 screens: "for numerator K the square obstruction is n = s·m² with s | K/4 odd (Lemma 4.3)".
* §6: "conditional composite inheritance (Lemma 4.2) explains part of F3 for N_II but is empty at primes; rigid
  modulus-4 slices give Z(N_II) ∩ odd ⊂ S₃ (Lemma 4.4), a dimension-3/2 sieve set — no pointwise content".
* Keep the model and the eventual-positivity statements out of FRONTIER, except as labelled CONJECTURE / EVIDENCE.

**Bottom line.** Measured by the four falsifiers in the tested ranges, the full Type II family is a much better target
than (★):
* (★) has 14 prime zeros, 285 composite zeros ≤ 8·10⁶, and a C-even half that is false at 10¹⁰;
* N_II has no odd prime zero ≤ 10¹⁰ and one odd non-square zero (4545);
* both its parity halves are clean in the tested ranges above 1.24·10⁶;
* on Mordell-class primes a Poisson law fitted across numerators 8–24 is compatible with K = 4.

That supports (MS-II) and points to the c-variable as the source of robustness. It is *not* a proof idea. Every
mechanism tried reduces to one of three things: conditional inheritance, which is empty at primes; single-integer
sieve/norm events; or the order-≥ 3 remainder of Z57_BFII. The wall is the same B2, now with a log³ instead of a log²
main term.

## 7. Review record

**Hostile review** (deep-mode subagent; `data/z58/wildcard/review_hostile.md`). It found 8 SERIOUS and 6 MINOR issues.
Lemmas 4.1–4.4 and the census engine passed. It independently reproduced all zero lists to 10⁵, all 267 527 stored LATE
witnesses, and all four Python outputs byte for byte. Fixes applied:

| # | finding | fix |
|---|---|---|
| 1 | F4 called all screen primes c = 1 zeros | restricted to the 14 (★)-zeros; "must use c ≥ 2" made conditional and relabelled as strategy |
| 2 | composite conductor claim false (shared factors cancel; 4545/u = 505 example) | F1 and §5.1 now quote the prime-only theorem; composite analysis marked heuristic |
| 3 | S₃ density ≍ unsupported | now only the upper bound ≪ X/(log X)^{3/2}, labelled Assessment |
| 4 | model populations mismatched; bins selected by outcome | refit by Poisson MLE incl. zero bins, matched populations P1/P2, new 𝔐 count sample (4 258 primes); old fit marked superseded |
| 5 | "differ only through mean count" overclaim | replaced by compatibility statement plus the f = 11 counter-illustration |
| 6 | "only K = 4 has complete moduli" not proved | restricted to the specific moduli 3, 7, 15 |
| 7 | bounded data written as eventual positivity | ranges and "odd non-square" added everywhere; eventual statements labelled CONJECTURE |
| 8 | inheritance stated unconditionally | divisibility hypotheses restored; N_II(5) > 0 = N_II(4545) noted |
| 9–14 | x-range number, K24 twist filter, LATE/max-witness labels, scope wording, provenance, CLI checks | fixed (the new ladder2 excludes all odd prime factors of K/4; census labels and argument checks added; data size and sample descriptions corrected) |

**Cross-model review** (`data/z58/xreview/REVIEW_WILDCARD.md`, ACCEPT-WITH-FIXES). It confirmed:
* every census by full reruns, plus an independent progression sieve to 10⁸ (zero lists identical);
* Lemmas 4.1–4.4;
* the F2/F3/F4 witnesses;
* the `ladder2.txt` refit, byte for byte.

Required fixes, both applied in §3:
1. "bin-by-bin within a factor 2–3" is replaced by "most positive bins within a few-fold; worst ratio ≈ 4.8; zero bins
   enter through the deviance".
2. "K = 4 values beyond 10⁵ outside the x-range" is corrected: decade 5 is inside, decades 6–7 are outside.

The desirable clarification is added too: 0 observed against 0.0096 expected is very weak compatibility (P ≈ 0.99), and
no significance is claimed.

## 8. Reproduction
```
gcc -O2 -o /tmp/z58wc scripts/z58_wildcard_census.c -lm          # ulimit -v 4000000; timeout <= 1800 on every run
/tmp/z58wc 4 1 100000000 20000 > data/z58/wildcard/census_K4_1e8.txt
/tmp/z58wc 4 100000000 1000000000 20000 > data/z58/wildcard/census_K4_1e8_1e9.txt
/tmp/z58wc 4 1000000000 10000000000 20000 > data/z58/wildcard/census_K4_1e9_1e10.txt
/tmp/z58wc 4 1 100000000 20000 0 0 1 > data/z58/wildcard/census_K4cop_1e8.txt              # coprime
Z58DODD=1 /tmp/z58wc 4 1 1000000000 40000 > data/z58/wildcard/census_K4dodd_1e9.txt
/tmp/z58wc 8 1 10000000 20000 > data/z58/wildcard/census_K8_1e7.txt   # + [1e7,1e8), [1e8,1e9) files likewise
/tmp/z58wc 12 1 100000000 40000 > data/z58/wildcard/census_K12_1e8.txt ; same for 16
/tmp/z58wc 20 1 100000000 40000 1 > data/z58/wildcard/census_K20_primes_1e8.txt ; same for 24
gcc -O2 -o /tmp/z58cnt scripts/z58_wildcard_count.c
/tmp/z58cnt 1000000 1100000 6 2 > data/z58/wildcard/counts_K4to24_1e6.txt
/tmp/z58cnt 1000000 3000000 6 1 1 > data/z58/wildcard/counts_K4to24_mordell_1e6_3e6.txt
python3 scripts/z58_wildcard_ladder.py > data/z58/wildcard/ladder.txt        # superseded first fit (kept for the record)
python3 scripts/z58_wildcard_ladder2.py > data/z58/wildcard/ladder2.txt      # Poisson MLE, matched populations
uv run python scripts/z58_wildcard_screens.py > data/z58/wildcard/screens.txt
uv run --with sympy python scripts/z58_wildcard_kernels.py > data/z58/wildcard/kernels.txt
```
