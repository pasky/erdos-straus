# Z58_WILDCARD — HOT TARGET, NO MECHANISM: the full Type II family passes all four falsifiers (statement level only)

**ES is OPEN; nothing here proves or disproves it.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Lane WILDCARD of wave z58 (`z52bbriefs/z58_lanes.md`; common rules `z53_depth.md` with z53 → z58).
Scripts `scripts/z58_wildcard_*`, data `data/z58/wildcard/` (≈ 9 MB). Status: **final draft, hostile review applied (§7)**.

**One-line verdict.** The full Elsholtz–Tao Type II family is the right *target*: as a statement it survives F1–F4
far better than (MS) does. It has no prime zero up to 10¹⁰. Its only odd non-square zero up to 10¹⁰ is 4545. Both
d-parity halves are eventually positive, so the numerator-8 trap does not carry over. All of this is statement-level,
computed evidence. **No mechanism was found**: the single-residue pointwise wall (B2) is unchanged. Verdict:
**strengthened (target) / inconclusive (mechanism).** The target is prior (Z57_BFII, notes §§60–61); what is new is how
it does on the falsifier screens, the numerator ladder with its twisted T1, a scaling bijection, an explicit necessary
condition, and a calibrated zero model.

## 0. Mandatory falsifier table (committed at checkpoint 1; final form)

Object: N_II(n) := #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = a + b + nc} (ET (2.15); (★) is the c = 1 line (u,B,C) = (a,b,d)).
For prime p, N_II(p) ≥ 1 ⟹ 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp) ⟹ ES(p). Numerator-K version:
N^{(K)}(n) := #{K·abcd = a + b + nc}, K ≡ 0 (mod 4).

| screen | behaviour of the target CONV-II / (MS-II) | label |
|---|---|---|
| **F1 odd squares** | N_II(m²) = 0 for every m (Z57_BFII Prop 2.2/Cor 2.3: every witness f = 4acd − 1 has (n/f) = −1). CONV-II says T1 is the *only* obstruction, so non-squareness is the hypothesis itself. Any proof must, at some step, produce a witness modulus f with (n/f) = −1. At the genus level this is Theorem G's step "ψ*χ_u is never principal, because the conductor of χ_u contains the squarefree kernel of n". Numerator K: the obstruction grows to n = s·m² for every odd s ∣ K/4 (Lemma 4.3, PROVED; CERTIFIED for K = 12: 2 887 of the 3 802 zeros ≤ 10⁸ have the form 3m²). | PROVED + CERTIFIED |
| **F2 numerator 8 / C-even** | The C-even half of (★) (= the c = 1 line of numerator 8) has 12 prime zeros in [10¹⁰, 1.1·10¹⁰]. The *full* numerator-8 family N^{(8)} is exactly the d-even half of N_II (Lemma 4.1). Among odd non-squares ≤ 10⁹ it has **22 prime zeros (last 35 569; three of them in 𝔐: 1129, 3361, 35 569) and 107 composite zeros (last 1 239 315)**, and none in (1 239 315, 10⁹]. The complementary d-odd half has 8 non-square zeros ≤ 10⁹: 13 (prime), 301, 445, 685, 1981, 3105, 4545, 9121. At the 12 R₈-zeros N^{(8)} has witnesses f ≤ 1311. So **the F2 trap does not carry over to the full family**: both parity halves are positive (empirically, eventually), and an argument that works verbatim for numerator 8 is not refuted at any threshold ≥ 1 239 315. What the full family *needs* is the c ≥ 2 lines: at 10¹⁰ the c = 1 line of numerator 8 is false. | CERTIFIED (≤ 10⁹) |
| **F3 composites** | (★) has 285 non-square composite zeros ≤ 8·10⁶. **N_II has exactly one odd non-square zero ≤ 10¹⁰: 4545 = 3²·5·101.** This extends Z57_BFII (10⁷) and notes §61 (10⁶). 284 of the 285 (★)-composite zeros have N_II ≥ 1. One part of the reason is PROVED: composites inherit solutions from their divisors (scaling bijection, Lemma 4.2). Removing inheritance (ET coprimality gcd(abd, n) = 1) leaves 142 zeros ≤ 10⁸. **Every one of them is divisible by 3 or 5** (137 by 3, 5 more with least prime factor 5); all are ≡ 1 (mod 4), and the last is 21 754 425. So, beyond non-squareness, primality is used only through gcd(n, 15) = 1 (coprime form) or not at all (N_II form, apart from the sporadic 4545). | CERTIFIED + PROVED |
| **F4 known zeros** | N_II ≥ 1 at all 14 (★)-zeros and all 38 𝔊*-zeros (least witness ≤ 239) and at the 12 R₈-zeros (≤ 295). No odd prime ≤ 10¹⁰ has N_II = 0. The statement has **no known prime zero**, so it needs no threshold above them. Those primes are zeros of the c = 1 line, so any proof that runs through that line fails there: the argument must genuinely use c ≥ 2. | CERTIFIED |

**Reading (Assessment).** CONV-II passes all four screens, so it is a **HOT TARGET**. It is *not* a hot lead in the
mechanism sense. Passing the screens is a property of a *statement plus data*; §5 explains why no mechanism found here
moves B2.

## 1. Precise statements

* **CONV-II (CONJECTURE).** Every odd non-square n ≥ 3 other than n = 4545 has N_II(n) ≥ 1.
  * CERTIFIED for n ≤ 10¹⁰ (§3).
  * PROVED for n ≡ 3 (mod 4): (a,b,c,d) = (1, 1, 2, (n+1)/4) gives 8d = 2n + 2 = a + b + 2n (Lemma 4.4(a)). So
    CONV-II is a statement about n ≡ 1 (mod 4).
* **CONV-II-15 (CONJECTURE).** Every odd non-square n with gcd(n, 15) = 1 has a solution with gcd(abd, n) = 1 (a genuine
  ET Type II solution). CERTIFIED for n ≤ 10⁸.
* **(MS-II) (CONJECTURE).** Every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 has N_II(p) ≥ 1.
  * (MS-II) is implied by (MS), since c = 1 is a sub-family.
  * Together with Mordell's reduction and Salez (10¹⁷), (MS-II) implies ES (PROVED relative to those, exactly as for
    (MS)).
  * CERTIFIED for all odd primes ≤ 10¹⁰. The internal-census variant at threshold 10¹⁰ therefore holds with no
    exceptional primes at all.
* **CONV-II(K) (CONJECTURE, K ≡ 0 mod 4).** The zero set of N^{(K)} on odd n is
  {s·m² : s odd, s ∣ K/4} ∪ (a finite set).
  * K = 8: finite part ≤ 10⁹ = 129 integers.
  * K = 12: finite part ≤ 10⁸ = 915 integers, the last prime 1 998 793 and the last composite 19 156 825.
  * K = 16: zeros continue to 10⁸ (last prime 12 895 921, last composite 94 165 635).
  * EVIDENCE only for K ≥ 16. "Finite" for each K is the conjecture.

## 2. Quick pass on the four leads

* **(i)+(ii) full Type II / converse of T1: adopted** (best falsifier outcome by far: table above).
* **(iii) r-spectrum.** The natural closure law, multiplicativity, is false in one line. 2 ∈ R(n) for every odd n
  (2n + 1 is its own divisor ≡ −1 mod 2), yet 4 ∉ R(409) since R(409) = 0. No other selection law gave a quick falsifier
  outcome. Not pursued.
* **(iv) varying fields Q(√(−Cp)) / joint divisor constraints.** No quick computation.
  * The slice forms of Type II already *are* these joint constraints: f | cn + a with f ≡ −1 (mod 4ac); f | n + 4a²d;
    f | 4c²dn + 1.
  * Lemma 4.4(b) extracts their rigid part. Pushing further means a sieve/norm-form route, i.e. B6 or
    CLASS_FORCING Thm 2.1 territory (§5).

## 3. Computations (CERTIFIED unless labelled otherwise)

**Engine** `scripts/z58_wildcard_census.c`. For each odd n it looks for the least f ≡ −1 (mod K), f ≤ FMAX, with
−n mod f ∈ T_f := {a·c⁻¹ : ac | (f+1)/K}. This is Z57_BFII Lemma 1.1(d); its proof works verbatim for any K, and b ≥ 1 is
automatic because f | cn + a > 0. The search uses bitmaps. A non-square with no witness ≤ FMAX is decided *exactly* by
the (a,b)-loop
  K·a·b·d = n + e, e | a + b, 1 ≤ e ≤ a + b
(e = (a+b)/c). Since K·ab > a + b, each (a,b) has at most one candidate e.

Options: coprime mode (gcd(a, n) = gcd(d, n) = 1, which forces gcd(b, n) = 1); d-odd mode (env `Z58DODD=1`).

Validation:
* (V1) FMAX = 3, so 6 596 non-squares ≤ 2·10⁴ take the exact path. The zero set is identical ({4545}), and likewise in
  d-odd mode on n ≤ 3·10⁴.
* (V2) It reproduces Z57_BFII's 10⁷ zero set (an independent enumerator).
* (V3) `scripts/z58_wildcard_screens.py` recomputes T_f by independent Python code at every falsifier integer. It
  builds explicit (a,b,c,d), checks K·abcd = a + b + nc, and for K = 4 checks 4/n = 1/x + 1/y + 1/z in exact
  rationals.
* (V4) Odd-square counts match exactly (4 999 below 10⁸; 34 189 in [10⁹, 10¹⁰)).

| run (odd n) | non-square zeros | notes |
|---|---|---|
| K = 4, [1, 10⁸), FMAX 2·10⁴ | **4545** | max least witness 14 111 (n = 92 455 209); primes 2 495 (p = 2 031 121) |
| K = 4, [10⁸, 10⁹) | none | one n (302 812 197) has no witness ≤ 2·10⁴; the exact loop gives f = 151 406 099; primes: max least witness 3 359 |
| K = 4, [10⁹, 10¹⁰) | none | every non-square has a witness ≤ 2·10⁴ (max 19 711); primes: max 3 799 at p = 6 736 278 481 |
| K = 4 coprime, [1, 10⁸) | 142, all divisible by 3 or 5 | last 21 754 425; none coprime to 15 |
| K = 4 d-odd, [1, 10⁹), FMAX 4·10⁴ | 13, 301, 445, 685, 1981, 3105, 4545, 9121 | |
| K = 8, [1, 10⁹) | 129 (22 primes) | last prime 35 569, last composite 1 239 315 |
| K = 12, [1, 10⁸) | 3 802 (2 887 of the form 3m²) | non-twisted: last prime 1 998 793, last composite 19 156 825 |
| K = 16, [1, 10⁸) | 5 269 (447 primes) | still present near 10⁸ |
| K = 20 / 24, primes ≤ 10⁸ | 1 164 / 3 740 prime zeros | last 94 965 203 / 96 577 729 |

Runtimes: the K = 4 run to 10¹⁰ takes 34 s, because most n hit f = 3, 7 or 15 (Mordell's complete moduli). Each K ≥ 8
run takes 10 s to 15 min.

**Squarefree-kernel profile** (`z58_wildcard_kernels.py` → `kernels.txt`; EVIDENCE). Apart from the PROVED 3m²-family
at K = 12, the composite zeros are *not* twisted squares with small kernel:
* (★): 0 of 285 have kernel ≤ 15;
* K = 16: 55 of 4 822.

Most of them are squarefree, with small prime factors (3, 5, 7).

**Count sample and numerator ladder** (`z58_wildcard_count.c`, `z58_wildcard_ladder.py` → `ladder.txt`,
`counts_K4to24_1e6.txt`). Sample: 1 821 primes p ≡ 1 (4) in [10⁶, 1.1·10⁶). Mean N^{(K)}/L³ for K = 4, 8, …, 24:

| K | 4 | 8 | 12 | 16 | 20 | 24 |
|---|---|---|---|---|---|---|
| mean N^{(K)}/L³ | 0.0762 | 0.0329 | 0.0159 | 0.0141 | 0.0107 | 0.0067 |
| zeros of the c = 1 line | 0 | 7 | 53 | 118 | 198 | 363 |
| zeros of the full family | 0 | 0 | 0 | 2 | 1 | 25 |

**Zero-rate model (EVIDENCE for the fit; the extrapolation is Assessment).** Let rate(K, decade) be the number of
prime zeros of N^{(K)} divided by the number of primes in that decade, using 24 (K, decade) points with K = 8…24 and
decades 10²–10⁸. The single two-parameter law
  rate ≈ exp(−0.78 − 0.219·λ_K·L³)
fits all 24 points to within ≈ 1.4 in log, where λ_K·L³ is the mean count. It also captures the shift of the peak
decade with K (10³ for K = 12 up to 10⁵–10⁶ for K = 24).

At K = 4 the mean is λ₄ = 0.076. The law then predicts a zero rate of ≈ e^{−9.5} near 10³ (inside the fitted x-range)
and e^{−19} near 10⁴ (already an extrapolation). The expected number of K = 4 prime zeros is ≈ 0.01 in total, matching
the zero observed.
* At 10¹⁷ the mean count is ≈ 0.076·39.1³ ≈ 4.5·10³ for the full family, against ≈ 0.166·39.1² ≈ 250 for (★).
* For comparison, the R₈ fit of Z57_SYNTH is exp(−0.627 − 0.026 L²), i.e. B ≈ 0.35 per unit mean.

The model is a *statistical* calibration. It says nothing about any individual prime (B6).

## 4. Lemmas (PROVED, elementary)

**Lemma 4.1 (numerator nesting).** For k ≥ 1 the map (a,b,c,d) ↦ (a,b,c,kd) is a bijection from the solutions of
kK·abcd = a + b + nc onto the solutions of K·abcd = a + b + nc that have k | d. In particular:
* N^{(8)} is the d-even half of N_II;
* the C-even half of (★) is the c = 1 line of N^{(8)} (= Z57_SYNTH Lemma 2.1).

*Proof.* kK·abcd = K·abc(kd). ∎

**Lemma 4.2 (scaling bijection).** Let N = nk with n, k ≥ 1.
* (a) (a,b,c,d) ↦ (a, b, kc, d/k) is a bijection {solutions for N with k | d} → {solutions for n with k | c}.
* (b) (a,b,c,d) ↦ (a/k, b/k, c, kd) is a bijection {solutions for N with k | a, k | b} → {solutions for n with k | d}.

*Proof.*
* (a) 4ab(kc)(d/k) = 4abcd = a + b + Nc = a + b + n(kc). The inverse is (a,b,c,d) ↦ (a, b, c/k, kd).
* (b) 4(a/k)(b/k)c(kd) = 4abcd/k = (a + b + Nc)/k = a/k + b/k + nc. The inverse is (a,b,c,d) ↦ (ka, kb, c, d/k):
  4k²ab·c·d/k = k(a + b + nc).
* Checked numerically on 7 composites and all k ≤ 11 (0 mismatches). ∎

*Consequence.*
* If N_II(n) ≥ 1 has a solution with k | c, then N_II(nk) ≥ 1.
* Composites therefore inherit witnesses from their divisors; at primes the lemma is empty.
* This is the PROVED part of why F3 looks so much better for N_II than for (★). The coprime census of §3 shows how much
  is left once inheritance is removed: zeros only at multiples of 3 or 5.
* The lemma gives nothing at primes. In particular it does not explain why primes have no zeros.

**Lemma 4.3 (T1 for numerator K).** Let K ≡ 0 (mod 4), let n be odd, and let f = K·acd − 1 be a witness. Then
(n/f) = −1 (Jacobi). Hence N^{(K)}(s·m²) = 0 for every odd s | K/4 and every m with s·m² odd.

*Proof.*
* f ≡ −1 (mod K·ac). Z57_BFII Lemma 2.1 with k = (K/4)·ac gives ((K/4)·ac / f) = 1. With k = K/4 alone it gives
  ((K/4)/f) = 1, so (ac/f) = 1.
* As in Prop 2.2 there, −n ≡ a·c⁻¹ (mod f). So (−n/f) = (ac/f) = 1, and (n/f) = (−1/f) = −1.
* For n = s·m² with odd s | K/4 and gcd(m, f) = 1: f ≡ −1 (mod 4s) and Lemma 2.1 (k = s) give (s/f) = 1, so (n/f) = 1.
  This is a contradiction.
* If gcd(m, f) > 1, then f ∤ cn + a: a prime ℓ | gcd(m, f) would divide a, but gcd(a, f) = 1 because f ≡ −1 (mod a).
  ∎

*Use.* This is the exact K-dependence of the square obstruction. For K = 4 and K = 8 it is the squares alone (for
K = 8, 2m² is even), so 4 and 8 are structurally alike. A screen for uniform-in-K arguments follows: they must see the
twist at K/4.

**Lemma 4.4.**
* (a) For odd n ≡ 3 (mod 4), (1, 1, 2, (n+1)/4) solves 4abcd = a + b + nc.
* (b) Suppose n ≡ 1 (mod 4) and N_II(n) = 0. Then every prime factor of (n+1)/2, of n + 4 and of 4n + 1 is ≡ 1 (mod 4).
  In particular n is a quadratic residue modulo each of these primes.

*Proof.*
* (a) Direct: 4·1·1·2·(n+1)/4 = 2n + 2.
* (b) Three slices of Type II have modulus exactly 4: (a, c) = (1, 1) needs f | n + 1; (a, d) = (1, 1) needs
  f | n + 4 (Z57_BFII Lemma 1.1(e)); (c, d) = (1, 1) needs f | 4n + 1. In each case the condition is f ≡ 3 (mod 4).
  A prime ℓ ≡ 3 (mod 4) dividing one of these integers is such an f. These integers are odd apart from n + 1, which is
  ≡ 2 (mod 4), so its odd part is (n+1)/2.
* For a prime ℓ ≡ 1 (mod 4) dividing n + 1, n + 4 or 4n + 1: n ≡ −1, −4 or −1/4 (mod ℓ), so (n/ℓ) = (−1/ℓ) = 1. ∎

*Use.* The zero set of N_II lies inside the explicit set
  S₃ := {n : (n+1)/2, n + 4 and 4n + 1 are products of primes ≡ 1 (mod 4)},
a sieve-dimension-3/2 set of density ≍ (log X)^{−3/2} (Assessment: standard upper-bound sieve).
* Odd squares lie in S₃: (m²+1)/2, m² + 2² and (2m)² + 1 are sums of two coprime squares.
* So does 4545: 2273, 4549 and 18181 are primes ≡ 1 (mod 4).
* So does every (★)-zero that has a Type II solution only with c ≥ 2? *No*: e.g. 409 + 4 = 413 = 7·59, so 409 ∉ S₃, and
  indeed 409 has a modulus-4 Type II witness f = 7. The (★)-zeros fail (★) but not Type II's rigid slices.

The answer to lead (ii)'s "explicit sparse set" question is thus PROVED only in the weak form Z(N_II) ⊂ squares ∪ S₃.
S₃ contains infinitely many primes heuristically (Dickson-type), so rigid slices cannot finish the job.

## 5. Mechanism attempts and why each stops (Assessment unless labelled)

1. **Genus main term at non-squares.** Theorem G (Z57_BFII, PROVED) gives a genus mass ≥ 10⁻¹⁰ (log p)³ at primes.
   * Its non-squareness step is "the conductor of χ_u contains p". For a general non-square n, the conductor contains
     the squarefree kernel s(n).
   * When s(n) is small (twisted squares s·m²), the Burgess step is replaced by small-conductor characters. The genus
     mass then loses the u-classes with s | u (second poles, as at squares) but stays ≍ log³ (heuristic; not
     re-proved here).
   * So nothing at the genus level distinguishes 4545 or the 142 coprime zeros. The genus term is not the obstruction;
     the order-≥ 3 remainder is (Z57_BFII §5.2). **B2 unchanged.**
2. **Inheritance (Lemma 4.2).** It explains the composite profile (F3) but is empty at primes. It gives no prime
   statement.
3. **Rigid slices (Lemma 4.4(b)).**
   * The three modulus-4 slices force a 3/2-dimensional norm condition.
   * Slices with modulus 8 already allow two index-2 subgroups ({1,3} or {1,5} mod 8), only one of which is the
     kernel of the relevant character. So a non-residue prime ℓ ≡ 5 (mod 8) can sit in n + 2 or 2n + 1 without
     producing a witness.
   * Joint emptiness of all slices is a pointwise sieve event. For a single n only *upper*-bound sieves are available
     (B6).
   * Reciprocity constrains only the total product, e.g. (n/(n+4)) = 1 automatically (CLASS_FORCING Thm 2.1).
4. **Numerator ladder.** The ladder gives a calibration (§3), not a proof. Any mechanism that works for all K ≡ 0 (4)
   uniformly must have threshold ≥ the last zero of each K it covers. That last zero grows quickly with K (≈ 3.6·10⁴,
   2·10⁶, ≥ 1.3·10⁷, ≥ 9.5·10⁷ for K = 8–20). So **any K-uniform argument must carry an explicit K-dependent constant**.
   At K = 4 the observed sporadic is 4545 and nothing else; this is consistent with a threshold-free statement, but no
   argument delivers it.
5. **Witness growth.** The maximal least witness at primes is 2 495 (≤ 10⁸), 3 359 (≤ 10⁹) and 3 799 (≤ 10¹⁰), i.e.
   ≈ 0.3·L³. Bounding it by any polylog would prove a GRH-strength bound on n_p, because W ≥ n_p (Z57_BFII Cor 2.4).
   That is the WITNESS lane's territory; it is noted here only as a reason not to aim at small witnesses.

**What would count as a mechanism (Assessment).** A fixed-p argument that uses c ≥ 2 essentially (F2/F4) and
non-squareness at a named step (F1). It must not lean on small prime factors of n: the coprime zeros all have
3 | n or 5 | n, so an argument that works for every n coprime to 15 is not falsified by F3, and primes are the easiest
case of it. None was found. The best available sufficient condition remains Z57_BFII §5.5 (SB ⟹ f_II ≥ 1). It is a
single-prime equidistribution statement at characters of all orders.

## 6. Verdict, proposed FRONTIER text, bottom line

**Verdict.** **Strengthened (target)**: the screens single out the full Type II family, and (MS-II) is the target to
carry. **Inconclusive (mechanism)**: no new pointwise step; B2 did not move.

New this lane:
* (a) CERTIFIED: CONV-II to 10¹⁰ (only 4545), CONV-II-15 to 10⁸, N^{(8)} and the d-odd half to 10⁹, and the ladder
  K ≤ 24 to 10⁸.
* (b) PROVED: Lemmas 4.1–4.4 (nesting; scaling bijection; T1 for numerator K with the s | K/4 twist; n ≡ 3 (4)
  trivial; the rigid-slice necessary condition S₃).
* (c) EVIDENCE: a single two-parameter zero-rate law across the numerator ladder.

**Proposed FRONTIER text (do not edit FRONTIER; for the integrator).**
* §2.4 / ladder: add the rung **(MS-II)**: N_II(p) ≥ 1 for p > 10¹⁷ in 𝔐. It is implied by (MS) and sufficient for ES.
  It has no prime zero ≤ 10¹⁰, and its only odd non-square zero ≤ 10¹⁰ is 4545 (`Z58_WILDCARD.md`). The F2 trap does
  not transfer: N^{(8)} = d-even half, last prime zero 35 569 ≤ 10⁹.
* §4 screens: "for numerator K the square obstruction is n = s·m², s | K/4 odd (Lemma 4.3)".
* §6: "composite inheritance (Lemma 4.2) explains F3 for N_II but is empty at primes; rigid modulus-4 slices give
  Z(N_II) ⊂ □ ∪ S₃ (Lemma 4.4), a 3/2-dimensional norm set — no pointwise content".

**Bottom line.** Measured by the four falsifiers, the full Type II family is a much better target than (★):
* (★) has 14 prime zeros, 285 composite zeros, and a C-even half that is false at 10¹⁰;
* N_II has no prime zero, one odd non-square sporadic (4545), and both parity halves eventually positive;
* its numerator-8 analogue is clean beyond 1.24·10⁶;
* a single zero-rate law across numerators 8–24 fits the data and puts K = 4 far from any zero.

That is strong evidence that (MS-II) is true and that the c-variable is what makes it robust. It is *not* a proof
idea. Every mechanism tried reduces either to inheritance, which is empty at primes, or to single-integer sieve/norm
events, or to the order-≥ 3 remainder of Z57_BFII. The wall is the same B2 with a log³ instead of a log² main term.

## 7. Review record
(to be filled after the hostile review)

## 8. Reproduction
```
gcc -O2 -o /tmp/z58wc scripts/z58_wildcard_census.c -lm          # ulimit -v 4000000; timeout <= 1800 on every run
/tmp/z58wc 4 1 100000000 20000 > data/z58/wildcard/census_K4_1e8.txt
/tmp/z58wc 4 100000000 1000000000 20000 > data/z58/wildcard/census_K4_1e8_1e9.txt
/tmp/z58wc 4 1000000000 10000000000 20000 > data/z58/wildcard/census_K4_1e9_1e10.txt        # 34 s
/tmp/z58wc 4 1 100000000 20000 0 0 1 > data/z58/wildcard/census_K4cop_1e8.txt              # coprime
Z58DODD=1 /tmp/z58wc 4 1 1000000000 40000 > data/z58/wildcard/census_K4dodd_1e9.txt
/tmp/z58wc 8 1 10000000 20000 > data/z58/wildcard/census_K8_1e7.txt   # + [1e7,1e8), [1e8,1e9) files
/tmp/z58wc 12 1 100000000 40000 > data/z58/wildcard/census_K12_1e8.txt ; same for 16
/tmp/z58wc 20 1 100000000 40000 1 > data/z58/wildcard/census_K20_primes_1e8.txt ; same for 24
gcc -O2 -o /tmp/z58cnt scripts/z58_wildcard_count.c && /tmp/z58cnt 1000000 1100000 6 2 > data/z58/wildcard/counts_K4to24_1e6.txt
python3 scripts/z58_wildcard_ladder.py > data/z58/wildcard/ladder.txt; python3 scripts/z58_wildcard_ladder2.py > data/z58/wildcard/ladder2.txt
uv run python scripts/z58_wildcard_screens.py > data/z58/wildcard/screens.txt
uv run --with sympy python scripts/z58_wildcard_kernels.py > data/z58/wildcard/kernels.txt
```
