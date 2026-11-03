# Z55_HCO — Problem HC: HC(p) ≤ (log p)^A for all large primes p ≡ 1 (mod 4)? (wave z55, tryhard lane HCO)

Brief: `/home/pasky/projects/math/z52bbriefs/z55_tryhard.md` (Problem HC). Scripts `scripts/z55_hco_*`, data
`data/z55/hco/`. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / Assessment.

Notation (from the brief and `Z53_UPPER.md` §1). p ≡ 1 (mod 4) prime; 𝒞_p := {x ∈ ℕ : x ≡ 0 (mod 4) or x ≡ −p (mod 8)};
HC(p) := least c ∈ 𝒞_p such that p + c or cp + 1 has a positive divisor d ≡ −1 (mod c) (the *U-line* and *T-line* at c;
by `Z53_UPPER.md` Lemma 1.1 this is the least 𝒞_p-coordinate of a word (t,u,v), tuv − u − v = p). For p ≡ 5 (mod 8),
HC(p) = 3 (`Z53_UPPER.md` P2.1(i)), so everything below concerns p ≡ 1 (mod 8), where 𝒞_p ∩ [1, ∞) = {4, 7, 8, 12, 15,
16, 20, 23, …}. A *certificate* for p is a pair (c, d) as in the definition.

---------------------------------------------------------------------------------------------------------------------

## 0. Verdict

**The target is NOT proved.** HC(p) < ∞ already gives a solution of 4/p = 1/x + 1/y + 1/z (brief; Theorem 1 of
`LOWERTAIL_ROUND2_FABLE.md` §1.1), so "HC(p) ≤ (log p)^A for every large p ≡ 1 (mod 4)" contains the Erdős–Straus
conjecture for all large primes p ≡ 1 (mod 8), which is open. I attacked it directly (§2). Each route stops at
the same point. A pointwise proof must show that, for the given p, one of the polylog-many fixed integers
p + c, cp + 1 has a divisor in a prescribed residue class whose modulus c varies with the integer. In the hard cases
(§4), the least usable congruence modulus is usually of mid size: median p^{0.35}, up to p^{0.64}. No available
pointwise technique reaches such divisors.

What this lane delivers:

| # | statement | status |
|---|-----------|--------|
| C3.1 | **HC(p) ≤ 64 for every prime p ≡ 1 (mod 4), p < 10¹²** (previous range: 10⁸). The maximum 64 is attained only at p = 21 841; the maximum over [10⁸, 10¹²) is 60, at p = 818 789 590 249 | CERTIFIED (`z55_hco_census.c`; histogram and verification in §3) |
| L2.1 | for k with (k/p) = −1, p + 4k has an odd number (with multiplicity) of prime factors ℓ with (ℓ/p) = −1, and (ℓ/p) = (−k/ℓ) for each prime ℓ ∣ p + 4k (this is where primality enters; false-premise at squares) | PROVED (+ checked: 234 541 cases, 0 violations) |
| P2.2 | every certificate is a single congruence p ≡ a (mod μ), with μ = min(d, c·e), e = N/d; a certificate with μ ≤ Y is "Y-local" | PROVED (elementary) |
| E4.1 | among the 126 primes p < 10¹² with HC(p) ≥ 44, the least certificate modulus μ at c = HC(p) lies in [p^{0.138}, p^{0.636}], median p^{0.345}. 101 of the 126 have μ > (log p)². So mid-size divisors carry most worst cases | EVIDENCE |
| E4.2 | "locally square" primes p ≡ 1 (mod 8∏_{3≤q≤y} q), y = 13, 23, 29, 31, 37, up to 2·10¹⁵: tails P(HC > 4), P(HC > 8) are 3–10× the global ones, but max HC is 47, 32, 23, 15, 7 respectively (samples of 3.8·10⁶, 4·10⁵, 1.5·10⁴, 525, 13 primes) | EVIDENCE |
| E4.3 | tail fractions decrease with height: P(HC > 4) 0.087 → ≈0.06, P(HC > 16) 2.2·10⁻⁴ → ≈3·10⁻⁵ from [0, 10⁸) to [10¹¹, 10¹²) | EVIDENCE |

---------------------------------------------------------------------------------------------------------------------

## 1. Reformulation used throughout

For p ≡ 1 (mod 8) and c ∈ 𝒞_p (c ≥ 4), put N_U := p + c, N_T := cp + 1. The line at c succeeds iff N_U or N_T has a
divisor d ≡ −1 (mod c). Every such d is coprime to c, so only the residues mod c of the prime factors of N matter.
The line succeeds iff some sub-multiset of these residues (taken with multiplicity) has product −1 in G_c := (ℤ/cℤ)^×.
Thus HC(p) ≤ X is a statement about the joint multiplicative structure of the ≍ X integers p + c, cp + 1 (c ≤ X).

---------------------------------------------------------------------------------------------------------------------

## 2. Direct attack: the routes and where each one stops

### 2.1 Using primality: the quadratic character (PROVED lemma, route stops)

The brief requires the key step to fail at odd squares n = m². Pointwise, the only feature separating a prime p ≡ 1 (8)
from a square is that (·/p) is a non-trivial character, i.e. some k has (k/p) = −1. The following lemma is the strongest
consequence of this for the lines that I found.

**Lemma 2.1 (PROVED).** Let p ≡ 1 (mod 4) be prime and k ∈ ℕ with p ∤ k. For every prime ℓ ∣ p + 4k we have ℓ odd,
ℓ ≠ p, and (ℓ/p) = (−k/ℓ) (Jacobi symbol). If (k/p) = −1, then Σ_{ℓ ∣ p+4k, (ℓ/p) = −1} v_ℓ(p + 4k) is odd. In
particular p + 4k has a prime factor ℓ with (ℓ/p) = −1.

*Proof.* p + 4k is odd. If p ∣ p + 4k then p ∣ 4k, so p ∣ k, excluded. For an odd prime ℓ ∣ p + 4k: if ℓ ∣ k then ℓ ∣ p,
so ℓ = p, excluded; thus ℓ ∤ 4k. Quadratic reciprocity with p ≡ 1 (mod 4) gives (ℓ/p) = (p/ℓ), and p ≡ −4k (mod ℓ)
gives (p/ℓ) = (−4k/ℓ) = (−k/ℓ). The Legendre symbol mod p is completely multiplicative, so
((p+4k)/p) = ∏_ℓ (ℓ/p)^{v_ℓ(p+4k)} = (−1)^{Σ_{(ℓ/p)=−1} v_ℓ}. Also ((p+4k)/p) = (4k/p) = (k/p). If (k/p) = −1 the
exponent sum is odd, hence ≥ 1. ∎

*Use of primality / squares.* The lemma needs a k with (k/p) = −1. For n = m² every Jacobi symbol (k/n) with gcd(k, m) = 1
equals 1, so the hypothesis never holds. CERTIFIED check (`scripts/z55_hco_parity_check.py`): all primes 5 ≤ p < 2·10⁵,
p ≡ 1 (4), and all 1 ≤ k < 60. There were 234 541 pairs with (k/p) = −1, with 0 parity violations and 0 violations of
(ℓ/p) = (−k/ℓ).

*Where the route stops.* A certificate at c = 4k needs a divisor d ≡ −1 in G_{4k}. Lemma 2.1 gives a divisor d (a single
prime) with χ(d) = −1 for one quadratic character χ = (−k/·) of G_{4k}, and χ(−1) = −1. Hitting the element −1 needs
the values of *all* characters of G_{4k}. When |G_c| = 2 one character is enough, and that happens only for c ∈ {3, 4, 6}.
In 𝒞_p (p ≡ 1 (8)) this leaves c = 4. There (4/p) = 1, so the lemma's hypothesis fails. For c = 4k, k ≥ 2, the
information is a single bit. The other characters of the prime factors of p + 4k are pointwise uncontrolled: no theorem
fixes the residue of a prime factor of a given integer modulo 4k. A second use of primality would be the exact residue
p mod q for a non-residue prime q. This is no stronger: a certificate that depends only on p mod q is a congruence
p ≡ −c or −c^{−1} (mod q) with c ∣ q + 1, plus similar cofactor shapes. There are O(τ(q + 1)) such classes, against
(q − 1)/2 non-residue classes (Assessment; standard Mordell–Yamamoto reasoning, not formalised here).

### 2.2 Every certificate is a congruence (PROVED) and the worst ones are mid-size (EVIDENCE)

**Proposition 2.2 (PROVED).** Let c ≥ 3, N ∈ {p + c, cp + 1}, and d ∣ N with d ≡ −1 (mod c); put e := N/d. The pair
(c, d) is an instance of two congruence-type certificates. The *d-fixed* one says that line c of p′ succeeds with the same
divisor d; it holds exactly for p′ in one residue class modulo d. The *e-fixed* one says that line c of p′ succeeds with the
cofactor e; it holds exactly for p′ in one residue class modulo c·e. Precisely, for p′ ∈ ℕ (with the same c):
U-line: d ∣ p′ + c ⟺ p′ ≡ −c (mod d); and [e ∣ p′ + c and (p′ + c)/e ≡ −1 (mod c)] ⟺ p′ ≡ −c − e (mod ce).
T-line: d ∣ cp′ + 1 ⟺ p′ ≡ −c̄ (mod d), where c c̄ ≡ 1 (mod d); and [e ∣ cp′ + 1, (cp′ + 1)/e ≡ −1 (mod c)] ⟺
cp′ + 1 ≡ −e (mod ce).
We call μ := min(d, ce) the *modulus* of the certificate.

*Proof.* gcd(c, d) = 1 because d ≡ −1 (mod c), so c̄ exists. The first equivalence on each line is immediate. For the
second: if e ∣ M and M/e = m, then m ≡ −1 (mod c) ⟺ c ∣ m + 1 ⟺ ce ∣ e(m + 1) = M + e. Conversely, if ce ∣ M + e then
e ∣ M and c ∣ M/e + 1. Apply this with M = p′ + c or M = cp′ + 1. ∎

Since d·(ce) = cN, μ ≤ √(cN) ≤ X√p + 1 for c ≤ X, N ≤ Xp + 1. So HC(p) ≤ X holds exactly when p lies in a union of
residue classes, over c ≤ X, with moduli μ ≤ X√p + 1. This union can never be confined to moduli μ ≤ c₀ log p.
Let m := ∏_{3≤q≤Y} q and let p ≡ 1 (mod 8m) (Linnik gives such p with log p ≪ Y, `Z53_UPPER.md` P3.3). Then (ℓ/p) = 1
for every prime ℓ ≤ Y. By `Z53_UPPER.md` L3.1, (d/p) = −1, so d has a prime factor > Y, i.e. d > Y. If ce ≤ Y, then
c and e are products of primes ≤ Y. On the T-line e itself is ≡ −1 (mod c) and divides cp + 1, so L3.1 gives
(e/p) = −1, a contradiction. On the U-line (d/p)(e/p) = (c/p) = 1 gives (d/p) = 1, again a contradiction. So such p
have no certificate with μ ≤ Y. Even well beyond log p,
local covering looks hopeless (the Z53 heuristics give an uncovered density far above 1/p). **EVIDENCE (E4.1, §4):** there are 126
primes p < 10¹² with HC(p) ≥ 44. For these, the least-modulus certificate at c = HC(p) has log μ / log p ∈
[0.138, 0.636], median 0.345, and μ > (log p)² for 101 of them. A pointwise proof therefore has to produce, in typical
hard cases, a divisor of size p^{θ} (0 < θ < 1) in a prescribed class modulo c. It must do so for one of the specific
integers p + c, cp + 1.

### 2.3 Other routes tried (Assessment, short)

* **Pointwise short-interval sieves.** Upper-bound sieves are uniform in the shift, so they do give pointwise facts about
  {p + c : c ≤ H}: for example, many of these integers have a prime factor ≡ 3 (mod 4) below H^ε. The required class,
  though, is −1 modulo the *shift c itself*. A small prime ℓ helps line c only when c ∣ ℓ + 1 and ℓ ∣ p + c. That is a
  local certificate again (P2.2 with μ = ℓ), and C3.2-type primes kill it.
* **Norm-form structure of p.** p = a² + b² (and p = x² − 2y² when p ≡ 1 (8)) factors p + c only for shifts
  c = −b² + (square), c = 2y², …. These are of size ≍ √p or p. Composition of forms moves the factorisation to cp with
  c of size p. None of these gives a small c. Quartic data (a, b mod q) carries information beyond p mod q. Certificates,
  however, depend only on p (P2.2), so that information cannot be used directly.
* **Lattice/word counting.** Σ_{c ≤ X} #{d ∣ p + c : d ≡ −1 (c)} counts representations of p by tuv − u − v with
  u ≤ X. A pointwise lower bound for it is a divisor problem in a short family. It is not reachable by the circle method
  (three variables, one of them tiny) or by any dispersion argument (these average over p).

**Weaker versions actually obtained.** (i) A *range* version: C3.1 (CERTIFIED to 10¹²). (ii) Positive-proportion and
exceptional-set versions are already PROVED in the repo: `Z53_UPPER.md` T4.2/T4.3 give #{p ≤ x : HC(p) > (log x)^A}
≪ x·exp(−(1−ε)A(log log x)²). `Z53_HCHYP.md` Thm U, PROVED modulo Henriot, gives ≪_X x(log x)^{−1−ℓ(X)/2}. I did not
improve these. (iii) No conditional form under a standard hypothesis was found. GRH controls only character values,
i.e. the single bit of §2.1 per modulus, and certificates are congruences (P2.2).

---------------------------------------------------------------------------------------------------------------------

## 3. CERTIFIED census to 10¹²

`scripts/z55_hco_census.c` (OpenMP; segmented sieve for p; full factorisation of p + c and cp + 1 by trial division
below 1000, deterministic 64-bit Miller–Rabin (12 prime bases, valid below 3.3·10²⁴) and Brent–Pollard ρ; all divisors
enumerated and tested against −1 mod c). For each prime p ≡ 1 (mod 8) it scans c ∈ 𝒞_p ∩ [4, 4000) upward and stops at
the first success; all products fit in 64 bits (cp + 1 < 4·10¹⁵). Run: `scripts/z55_hco_runcensus.sh` in chunks of
5·10¹⁰; outputs `data/z55/hco/census_*.txt`; aggregation `scripts/z55_hco_aggregate.py` (checks that chunks tile [0, 10¹²)
and that every histogram sums to the prime count).

Cross-checks. (a) Below 10⁸ the histogram matches `Z53_UPPER.md` §6 (independent program `z53_upper_hc.c`) entry by
entry, including #{p ≡ 5 (8)} = 1 440 534 and #{p ≡ 1 (8)} = 1 439 970. (b) Every p < 10¹² with HC(p) ≥ 44 (126 primes; `data/z55/hco/verify.txt`) was
re-verified independently in Python/sympy (`scripts/z55_hco_verify.py`). The check confirms p is prime and ≡ 1 (8), the
printed certificate is valid, and *minimality*: no c < HC(p) in 𝒞_p has a divisor ≡ −1 (mod c) of p + c or cp + 1.
0 failures. (c) `z55_hco_adv.c` (same kernel, different p-enumeration) with L = 8 reproduces the < 10⁸ histogram.

**Result (CERTIFIED).** Primes p ≡ 1 (mod 4) below 10¹²: 18 803 924 340, of which 9 401 972 490 are ≡ 5 (8) (HC = 3) and
9 401 951 850 are ≡ 1 (8). For the latter, HC(p) < 4000 always (no FAIL line), with the following histogram:

| HC | 4 | 7 | 8 | 12 | 15 | 16 | 20 | 23 | 24 | 28 | 31 | 32 |
|----|---|---|---|----|----|----|----|----|----|----|----|----|
| # | 8 851 945 528 | 511 181 865 | 31 048 619 | 5 448 736 | 1 687 276 | 400 730 | 169 702 | 49 652 | 11 842 | 3 024 | 3 086 | 924 |

| HC | 36 | 39 | 40 | 44 | 47 | 48 | 52 | 55 | 56 | 60 | 64 |
|----|----|----|----|----|----|----|----|----|----|----|----|
| # | 336 | 348 | 56 | 80 | 31 | 3 | 3 | 5 | 2 | 1 | 1 |

**Hence HC(p) ≤ 64 for every prime p ≡ 1 (mod 4) below 10¹².** Equality holds only at p = 21 841. Records above 10⁸:
HC = 60 at p = 818 789 590 249 (U-line, d = 1 667 219), HC = 56 at 844 772 955 601, and HC = 55 at five primes
(3 014 346 241; 33 257 638 801; 511 526 736 361; 712 917 322 849; 915 805 615 201). Every p ≡ 1 (8) below 10¹² thus
yields a solution of 4/p = 1/x + 1/y + 1/z with a word coordinate ≤ 64.

Further checks. (d) The prime enumeration was checked with the same segmented sieve counting all residues mod 4
(`scripts/z55_hco_picount.c`, `data/z55/hco/picount_1e12.txt`). It gives π(10¹²) = 37 607 912 018, the known value, and
π(10¹²; 4, 1) = 18 803 924 340, equal to the census total. (e) Divisor-array bound. The divisor buffer holds 2¹⁵
entries; a guard aborting on τ(N) > 2¹⁵ was added after the chunks below 2.52·10¹¹ (and the chunk running at that
moment) had already run. Those chunks only factor N ≤ 64·3.02·10¹¹ + 1 < 2·10¹³ (every scan stopped at c = HC(p) ≤ 64).
Every N < 10¹⁴ has τ(N) ≤ 17 280 < 2¹⁵, so the guard could not have fired there.

Per-chunk tail fractions (p ≡ 1 (8); full list in `data/z55/hco/aggregate_1e12.txt`):

| range | #p | max HC | P(HC>4) | P(HC>8) | P(HC>16) |
|-------|----|--------|---------|---------|----------|
| [0, 10⁸) | 1 439 970 | 64 | 0.0868 | 2.78·10⁻³ | 2.22·10⁻⁴ |
| [10⁸, 2·10⁹) | 23 113 408 | 52 | 0.0744 | 1.73·10⁻³ | 9.9·10⁻⁵ |
| [2·10⁹, 5.2·10¹⁰) | 525 630 219 | 55 | 0.0649 | 1.14·10⁻³ | 4.5·10⁻⁵ |
| [5.02·10¹¹, 5.52·10¹¹) | 463 130 225 | 55 | 0.0576 | 7.8·10⁻⁴ | 2.29·10⁻⁵ |
| [8.02·10¹¹, 8.52·10¹¹) | 455 529 296 | 60 | 0.0567 | 7.5·10⁻⁴ | 2.06·10⁻⁵ |
| [9.52·10¹¹, 10¹²) | 434 674 092 | 47 | 0.0564 | 7.3·10⁻⁴ | 2.02·10⁻⁵ |


---------------------------------------------------------------------------------------------------------------------

## 4. EVIDENCE

**E4.1 (certificate size at the worst primes).** `scripts/z55_hco_certsize.py` over all HIGH records (HC ≥ 44):
there are 126 primes p < 10¹² with HC(p) ≥ 44. For each, μ is the least modulus over all
certificates at c = HC(p). Then log μ/log p ranges over [0.138, 0.636] with median 0.345. 86 of the 126 have μ > 1000,
101 have μ > (log p)², and 118 have μ ≥ p^{0.2}. The 25 with μ ≤ (log p)² are prime-level certificates such as
d = 43 at c = 44 or d = 47 at c = 48 (q ∣ p + c, c ∣ q + 1). So most, but not all, of the worst cases are carried by
mid-size divisors. Examples: p = 21 841 (HC 64): μ = 575 = p^{0.64}; p = 691 681 (HC 56):
μ = 4872 = p^{0.63}; p = 33 257 638 801 (HC 55): μ = 274 = p^{0.23}. The high-HC primes are "locally square". For
example p − 1 = 2⁴·3·5·7·13 at 21 841 (least non-residue 11), 2⁵·3·5·11·131 at 691 681 (least non-residue 29), and
2⁴·3³·5²·3 079 411 at 33 257 638 801.

**E4.2 (adversarial families).** `scripts/z55_hco_adv.c`, primes p = 1 + kL with L = 8∏_{3≤q≤y} q. For such p,
(q/p) = 1 for all q ≤ y, so every certificate needs a prime factor > y with (ℓ/p) = −1 (`Z53_UPPER.md` C3.2):

| y | L | p range | #primes | P(HC>4) | P(HC>8) | max HC |
|---|---|---------|---------|---------|---------|--------|
| 13 | 120 120 | ≤ 2.4·10¹² | 3 797 371 | 0.222 | 0.0112 | 47 |
| 23 | 892 371 480 | ≤ 2.0·10¹⁵ | 400 359 | 0.220 | 0.0102 | 32 |
| 29 | 2.59·10¹⁰ | ≤ 2.1·10¹⁵ | 14 673 | 0.219 | 0.0103 | 23 |
| 31 | 8.02·10¹¹ | ≤ 2.2·10¹⁵ | 525 | 0.234 | 0.0114 | 15 |
| 37 | 2.97·10¹³ | ≤ 2.1·10¹⁵ | 13 | 0.31 | 0 | 7 |

The local obstruction raises the tails compared with §3: P(HC > 4) about 3.5×, P(HC > 8) about 10×, but HC stays small. This fits the conclusion of §2.2: the
mechanism is not local.

**E4.3 (tails decrease with height).** Per-chunk tail fractions are in the §3 table. P(HC > 4) falls from 0.087 (below
10⁸) to 0.0564 (last chunk). This is consistent with the Kubilius-model picture of `Z53_HCHYP.md` (more prime
factors per line as p grows). That model predicts eventual growth of max HC like (log p)^{2 log 2 + o(1)}. The census
maximum is flat at 64 (≤ 60 above 10⁸), still below (log p)^{2 log 2}, which grows from ≈ 57 to ≈ 100 across the
range. The model's own Poisson scale X* (`Z53_HCHYP.md` §6) is ≈ 3.4 log p ≈ 63–95 here, also above the observed
maximum.

---------------------------------------------------------------------------------------------------------------------

## 5. What a proof would need (one paragraph)

By P2.2 and E4.1, any proof of the target must contain a pointwise statement of this type: for every large prime p there
are c ≤ (log p)^A in 𝒞_p and N ∈ {p + c, cp + 1} with a divisor ≡ −1 (mod c) of size p^{θ} for some θ bounded away from 0
and 1. It must also fail for p = m² (Lemma 2.1 is the only primality input found). No current method gives pointwise
control of medium-size divisors of a specific integer in a residue class, even averaged over a polylog family of
shifts. Under this lane's analysis the target is equivalent in difficulty to ES for p ≡ 1 (mod 8) with a polylog
coordinate. That is an Assessment, not a theorem.

---------------------------------------------------------------------------------------------------------------------

## 6. Files

* `scripts/z55_hco_census.c` — HC census (segmented, OpenMP); `scripts/z55_hco_runcensus.sh` — chunk driver.
* `scripts/z55_hco_verify.py` — independent sympy verification (certificate + minimality) of all HC ≥ 44 records.
* `scripts/z55_hco_aggregate.py` — tiling/consistency check and totals.
* `scripts/z55_hco_adv.c` — adversarial families p = 1 + kL.
* `scripts/z55_hco_certsize.py` — least certificate modulus μ at c = HC(p).
* `scripts/z55_hco_parity_check.py` — numerical check of Lemma 2.1.
* `data/z55/hco/census_*.txt`, `data/z55/hco/adv_L*.txt`, `data/z55/hco/verify.txt`, `data/z55/hco/aggregate.txt`,
  `data/z55/hco/certsize.txt`.
