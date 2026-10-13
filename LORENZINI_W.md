# LORENZINI_W — attacking Lorenzini's A₃ question (W) (O180, spark relay G)

Status: internal research note, SPARK phase. **(W) is NOT proved here; ES is not solved.** Labels as in DISCOVERIES.md.
Scripts `scripts/bsG_*`. Builds on HJ_DEEP.md (O174, reviewed R174) and DEDEKIND_ES.md.

**(W)** (Lorenzini, *The critical polynomial of a graph*, J. Number Theory 257 (2024) 215–248, arXiv:2311.06367, Example 6.2(a);
still open: T. Wang and L. Lu, *The critical polynomials of simple connected graphs*, Electron. J. Combin. 33(3) (2026), #P3.80,
doi:10.37236/13899, prove density 1 for every connected simple G and call finiteness of the complement, for general G, "an open problem" — R184 repair, D3): every n ≥ 2 outside
E_W = {2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510} is n = xyz − x − z with x, y, z ≥ 2. EVIDENCE to 10⁹ (O174/R174).
Scope reminder (R174 D1): ES needs only (W) at primes p ≡ 1 (4) (plus (S)); global (W) is stronger.

## 0. Summary (updated as the work proceeds)
0. **New partial answer to Lorenzini's question (§9, PROVED): every even n ≥ 16 except 510 is a value.** Lorenzini left n = 2^m − 2 (m odd)
   open. A Sierpiński-type covering of odd m mod 36 by six fixed-pair families settles it. (W) is now *exactly* the statement for odd n ≡ 3, 9, 11 (mod 12)
   with n + 2 prime. (R184 repair, D8: novelty = not found in Lorenzini 2024, Wang–Lu 2026, the 7 Semantic-Scholar citers of Lorenzini's paper, or
   Lorenzini's later preprints; a web search cannot exclude unindexed work — see reviews/lorenzini-w-review-2.md §2.)
1. Four further elementary equivalent forms of (W) (§1, PROVED, checked against brute force for n < 700).
2. **(W) is not T1-free: odd/even squares carry a partial genus obstruction ("square shadow", §3, PROVED).** At n = m² the
   middle letter y satisfies y ≢ 0 (mod 4), y ≢ 7 (mod 8), and y ≢ 3 (mod 4) if m is even. The record-low
   values of R(n) = #solutions are squares of smooth numbers (5336100 = 2310², R = 4, against a mean ≈ 104 there).
   Yet squares are not exceptions: **every square except 1 and 9 is a value (Prop 3.3, PROVED; two families).**
3. Profinite "sterile set" (§4): the closed set S ⊂ Ẑ of points that no fixed-pair family covers. It contains −1 (HJ_DEEP Lemma
   3.2) and more (single-prime deviations ν(ℓ, c), Thm 4.2 PROVED). So compactness-type arguments cannot prove (W).
4. **SHARP/deflationary (§8, PROVED): (W) at primes p ≡ 1 (4) is trivial**, by two fixed-pair families, (2,2,·) and (3,·,4). So for ES
   the whole content of SQ₅ at primes is the sign half (S).
5. Short-block law (§5, EVIDENCE): x*(n) ≤ 12 for every n < 10⁸ outside E_W. CONJECTURE: x*(n) ≪ log n / log log n.
6. Unconditional rate #E ∩ [1,N] ≪ N exp(−c√log N) (§6, PROVED; input: the Titchmarsh divisor theorem of Linnik / Halberstam–Rodriquez — R180 repair, D3). Stern coding
   V_{A_k}(2) = s(popcount k+1) (§7, PROVED).

## 1. Elementary equivalent forms (PROVED; `scripts/bsG_forms.py 700`: 0 mismatches against brute force)
For n ≥ 2 the following are equivalent to (W)(n) ("n = xyz − x − z, x, y, z ≥ 2"):
* (F0) [HJ_DEEP] ∃ t ≥ 2: tn + 1 = (tx − 1)(tz − 1), x, z ≥ 2. ∃ x ≥ 2: n + x has a divisor d ≡ −1 (mod x), d ≥ 2x − 1, (n+x)/d ≥ 2.
* (F1) **∃ x, z ≥ 2 with xz | n + x + z** and (n + x + z)/(xz) ≥ 2. (Then y = (n+x+z)/(xz).) For coprime x, z this is
  "x | n + z and z | n + x": a pair of mutually n-shifted divisors.
* (F2) **∃ z ≥ 2: with q = ⌈n/z⌉ and r = qz − n, r ≥ 2 and r | q + 1** (and (q+1)/r ≥ 2); or a diagonal solution x = z
  (x | n, x | n/x + 2 and n/x + 2 ≥ 2x, i.e. y ≥ 2; without the last condition n = x(x−2) such as 3, 15, 35 would be wrongly accepted — (R180 repair, D1)). *Proof.* n = qz − r with x = r, y = (q+1)/r gives xyz − x − z = (q+1)z − r − z = n. Conversely any
  solution with x < z has r = x, q = xy − 1. ∎ (A ceiling-function form: one division of n by each z.)
* (F3) ∃ d ≥ 3: ρ := (−n mod d) is a divisor of d + 1 with 2 ≤ ρ ≤ (d+1)/2, and n + ρ ≥ 2d. (d = xy − 1, ρ = x.)
* (F4) ∃ a ∈ [1, n−1] coprime to n, with ā = a⁻¹ mod n, b := (aā − 1)/n ≥ 2, b | a + 1, b | ā + 1, a, ā ≥ 2b − 1.
  This is the SL₂ form [[a, b],[n, ā]] ≡ −[[1, 0],[−n, 1]] (mod b) (a = bx − 1, ā = bz − 1): points of the modular hyperbola
  aā ≡ 1 (mod n) whose quotient b divides a + 1 and ā + 1.

## 2. The count landscape (EVIDENCE; `scripts/bsG_minR.c 10⁸`, `scripts/bsG_count.c`)
R(n) := #{(x,y,z) ∈ Z³_{≥2} : xyz − x − z = n} (ordered). The mean over dyadic blocks is ≈ 0.45 log² n (0.35 at n ~ 30, 0.453 at
n ~ 5·10⁷; heuristic Σ_{d ≤ n} (τ(d+1) − 2)/d ≈ ½ log² n). Record lows per dyadic block [2^k, 2^{k+1}) for 2^k ≥ 2048:
2079 (R=4), 5580 (4), 9090 (3), **30276 = 174² (4), 34596 = 186² (5), 69696 = 264² (5), 207936 = 456², 324900 = 570² (6),
853776 = 924² (7), 1920996 = 1386² (5), 5336100 = 2310² (4), 16160400 = 4020² (9), 25401600 = 5040² (9), 51840000 = 7200² (11),
79388100 = 8910² (13)**. From 2^14 on, almost every block minimum is a square of a smooth number. The square-of-primorial
values grow again: R(30030²) = 37, R(510510²) = 39, R(9699690²) = 81 (`bsG_count`, n ≈ 9.4·10¹³ in 1.7 s).
Lorenzini's family n = 2^{2k+1} − 2: R = 0 (6, 510), 1 (30), 2 (126), 3 (2046), 7, 14, 25 (131070): growing.

## 3. The square shadow: T1 acts partially on (W) (PROVED)
**Lemma 3.1 (square shadow).** Let n = m², t ≥ 2, and tn + 1 = XZ with X ≡ Z ≡ −1 (mod t) (a word with middle letter t). Then
t ≢ 0 (mod 4) and t ≢ 7 (mod 8). If m is even, also t ≢ 3 (mod 4). If t ≡ 3 (mod 8) (m odd), then X ≡ Z ≡ 2 (mod 4).
*Proof.* For an odd prime q | tn + 1 we have q ∤ m and −t ≡ (m⁻¹)² (mod q), so (−t/q) = 1. Write X = 2^a X₁ with X₁ odd; by
multiplicativity (−t/X₁) = 1.
(i) 4 | t: X ≡ −1 (mod 4), so a = 0. Write t = 2^s t₁ (s ≥ 2, t₁ odd). Then (−1/X) = −1. Also (t₁/X) = (X/t₁)(−1)^{(t₁−1)/2} =
(−1/t₁)(−1)^{(t₁−1)/2} = 1, using X ≡ −1 (mod t₁) and X ≡ 3 (mod 4). Finally (2/X)^s = 1 (s even, or s ≥ 3 and X ≡ −1 mod 8).
So (−t/X) = −1, a contradiction. (This is the HJ form of ES's T1.)
(ii) t ≡ 3 (mod 4): −t ≡ 1 (mod 4), so (−t/X₁) = (X₁/t) for odd positive X₁. From 2^a X₁ ≡ −1 (mod t) we get
(X₁/t) = (−1/t)(2/t)^a = −(2/t)^a. For this to equal +1 we need a odd and (2/t) = −1, i.e. t ≡ 3 (mod 8). If m is even, tn + 1
is odd, so a = 0 and t ≡ 3 (mod 4) is impossible. If t ≡ 3 (mod 8) and m is odd, then n ≡ 1 (mod 8), so v₂(tn+1) = v₂(t+1) = 2. Both
X and Z need an odd 2-adic valuation, so a_X = a_Z = 1. ∎
**Remark 3.2 (n = k m²).** The same argument gives: if n = k m², no word has middle t ≡ 0 (mod 4k). Indeed, for t = 4ks, q | tn + 1 gives −s·(2km)² ≡ 1 (mod q), i.e.
(−s/q) = 1, while X ≡ −1 (mod 4s) gives (−s/X) = −1 as in (i). EVIDENCE (`scripts/bsG_kshadow.py`):
35 372 words at n = k m² (k ∈ {1,2,3,5,6,7}, m < 160), 0 violations of Lemma 3.1 / Remark 3.2.
`scripts/bsG_sqslices.py 300`: middle letters mod 8 at odd squares {1,2,3,5,6}, at even squares {1,2,5,6}, and at the control
n = m² + 2 all eight classes occur.
*Reading.* HJ_DEEP called (W) "T1-free". That is true only for the existence statement, not for the mechanism. At squares, exactly the
genus character that kills ES (the t ≡ 0 (mod 4) slices) also kills the slices t ≡ 3 (mod 4) (mostly). Squares of smooth
numbers additionally lose all small prime factors of tn + 1 (tn + 1 ≡ 1 mod every prime dividing m). This explains the record lows of §2.
**Barrier consequence (B5 for (W), PROVED by Lemma 3.1).** Any argument for (W) that uses only middle letters t ≡ 0 (mod 4), or only
t ≡ 3 (mod 4) for even n, gives nothing at squares. The shadow constrains only the middle letter: outer-letter slices such as Lorenzini's z = 2, 4 are
not directly affected. A route must use middle letters t ≡ 1, 2 (mod 4) (or t ≡ 3 (mod 8) at odd squares).

**Prop 3.3 (squares; PROVED).** Every square n = m² ∉ {1, 9} is a value of xyz − x − z with x, y, z ≥ 2.
*Proof.* m even: n ≡ 0 (mod 4) and (2, n/4 + 1, 2) works. 3 ∤ m: n ≡ 1 (mod 3) and (2, 2, (n+2)/3) works, with (n+2)/3 ≥ 2 for n ≥ 4.
m = 3k with k odd ≥ 3: (3, (k²+1)/2, 6) gives 18(k²+1)/2 − 9 = 9k² = n. ∎
(Certificate `scripts/bsG_sqproof.py`: a greedy covering of odd m mod 180 picks exactly these two families; explicit solutions are checked for all
odd m < 20001.) So the shadow lowers R(m²) but never empties it. This contrasts sharply with ES, where T1 empties every slice.
**Assessment.** The shadow is the precise sense in which T1 "acts" on (W). It shows that (W) is not a cleaner test bed than ES as far as
genus characters go. However the shadow is partial (two of four middle classes mod 4 survive), and the surviving slices
(t = 2, (x,z) = (3,6)) already cover squares by congruences, because −1 is not a square mod 3 or 4. The class n ≡ −1 (mod M) that defeats every
finite covering (HJ_DEEP Lemma 3.2) contains no squares.

## 4. The profinite sterile set of (W) (PROVED parts + EVIDENCE)
A *fixed-pair family* is a class c + dZ of one of two kinds: (x,y) fixed, d = xy − 1, c = −x (then z = (n+x)/d); or (x,z) fixed,
d = xz, c = −(x+z) (then y = (n+x+z)/(xz)). The (y,z) kind is the (x,y) kind mirrored. Each family certifies (W)(n) for every
n ≡ c (mod d) above a size threshold (≤ 2d). Let C ⊂ Ẑ be the union of the open sets c + dẐ, and let the **sterile set** be S := Ẑ \ C (closed).
By compactness, a finite fixed-pair covering of all n outside a clopen set V exists iff S ⊂ V.
**Prop 4.1.** S ∩ Z = {−1}.
*Proof.* −1 ∈ S is HJ_DEEP Lemma 3.2. If ν ≤ −2, take x = −ν (any y): d | ν + x = 0. If ν = 0, take (x,z) = (2,2): 4 | 0 + 4.
If ν ≥ 1, take (x,y) = (ν+1, 2): d = 2ν + 1 = ν + x. ∎ (Integers fail (W) only through the size thresholds.)
**Theorem 4.2 (S is infinite and accumulates at −1; PROVED).** For a prime ℓ let ν(ℓ, c) ∈ Ẑ be the point with ν ≡ −1 in Z_q for every
q ≠ ℓ and ν = c in Z_ℓ. For every prime ℓ ≥ 3, ν(ℓ, ℓ−1) ∈ S. Since ν(ℓ, ℓ−1) → −1 as ℓ → ∞, −1 is not isolated in S.
*Proof.* Write m_ℓ for the ℓ-part and m_{ℓ'} for the prime-to-ℓ part. Then d | ν + x ⟺ d_{ℓ'} | x − 1 and d_ℓ | x + ℓ − 1.
(x,y) kind: d = ℓ^j e (e prime to ℓ), with e | x − 1, ℓ^j | x + ℓ − 1, x | d + 1, d ≥ 2x − 1. Since e < 2x − 1 we have j ≥ 1. Then ℓ | x − 1, so x ≥ ℓ + 1. Put
x − 1 = ef. From ef ≡ −1 ≡ ℓ^j e (mod x) and gcd(e,x) = 1 we get ℓ^j ≡ f (mod x). Since 1 ≤ f < x and ℓ^j ≤ x + ℓ − 1 < f + 2x, we get ℓ^j ∈ {f, f + x}.
If ℓ^j = f, then ℓ^j divides both x − 1 and x + ℓ − 1, so j = 1, f = ℓ and d = x − 1 < 2x − 1. ✗. If ℓ^j = f + x > x, then ℓ^j | x + ℓ − 1 < 2ℓ^j
forces x + ℓ − 1 = ℓ^j, so f = ℓ − 1 and e = (ℓ^j − ℓ)/(ℓ − 1). This is divisible by ℓ if j ≥ 2, and gives x = 1 if j = 1. ✗.
(x,z) kind: x = ℓ^a u, z = ℓ^b v (u, v prime to ℓ). The conditions are uv | x + z − 1 and ℓ^{a+b} | x + z + ℓ − 1. If a = b = 0 then xz | x + z − 1 < xz. ✗.
If a, b ≥ 1, then x + z + ℓ − 1 ≡ ℓ − 1 ≢ 0 (mod ℓ). ✗. So w.l.o.g. a ≥ 1 and b = 0. Then u | v − 1, v | ℓ^a u − 1, and ℓ^a | v + ℓ − 1. Put v + ℓ − 1 = ℓ^a m
and ℓ^a u − 1 = vk. Then v(km − u) = (ℓ − 1)u − m =: vs, with 0 ≤ s ≤ ℓ − 2 (use u ≤ v − 1 and m < v).
* s = 0 gives k(ℓ − 1) = 1, impossible for ℓ ≥ 3.
* s ≥ 1: substituting u = km − s gives sℓ^a = (ℓ − 1)k − 1. Then s(v − 1) = s(ℓ^a m − ℓ) = (ℓ − 1)u − m − s, so u | v − 1 forces u | m + s, hence (k − 1)m ≤ 2s.
  * If a ≥ 2, this forces m = 1, and then u = k − s ≤ s + 1 needs s(ℓ^a − 2ℓ + 2) ≤ ℓ − 2, which is false. ✗.
  * If a = 1, integrality of k forces s = ℓ − 2, k = ℓ − 1, m ≤ 2. Then m = 1 gives v = 1, and m = 2 gives u = ℓ. ✗. ∎

**EVIDENCE 4.3 (`scripts/bsG_dev.c`, `scripts/bsG_devT.c`, `scripts/bsG_sterile.py`).**
* Single-prime deviations ν(ℓ, c) with integer 0 ≤ c ≤ 60 that no family of modulus ≤ 2·10⁵ covers. For ℓ = 2: c = 3, 7, 15, 19, 23, 31, 35, 39, 47. For ℓ = 3: c = 2, 8, 11, 17,
  26, …. For ℓ = 5: c = 4, 9, 14, 24, …. For ℓ = 7: c = 6, 13, 20, …. For ℓ = 11: c = 10, 21, 25, 32, 33, …. Mostly c ≡ −1 (mod ℓ), but not only.
* Multi-prime deviations: ν = c at every prime ≤ P and −1 elsewhere, integer c ≤ 2000, moduli ≤ 10⁵. Uncovered: 287 values for P = 2,
  34 for P = 3, and 3 for P = 5 (c = 899, 1439, 1799, all ≡ −1 (mod 30)). For P = 7, 11, …, 31 there are **none**.
  So in this probe every sterile point found is ≡ −1 at all but a few small primes.
* Finite levels: |U_M| (classes mod M missed by all families with modulus | M) is 0.161 % (M = 720720), 0.0852 % (12252240),
  0.0225 % (73513440), 0.00763 % (151351200 = 2⁵3³5²7²·11·13). The projections to mod 12 stay {3, 6, 9, 11} at every level tested.
* Integers *near* sterile points are not hard. n = 3·L′ − 1 and 5·L″ − 1, with L′, L″ the 3-free and 5-free parts of lcm(1..30), have
  R = 264 and 288 (block mean ≈ 300). Large-modulus families do the work.
**Consequences (Assessment).** (a) Compactness cannot prove (W). Exceptions to every finite fixed-pair covering are integers near S, and S is
infinite with −1 as an accumulation point. (b) A *finite-level computer-assisted* strengthening of Lorenzini's Prop 6.3 is available.
**Cor 4.4 (CERTIFIED, self-contained — R180 repair, D2).** Every n ∉ E_W whose class mod M = 151351200 lies outside U_M (11 550 classes,
density 7.6·10⁻⁵) satisfies (W). *Proof.* All size thresholds (2d − x, resp. 2xz − x − z) are < 2M, so every n ≥ 2M outside U_M is certified by a
family. For n < 2M: `scripts/review_lw_cor44.c` (R180, 16 s, one core) marks every n < 3M lying in a family class above that family's threshold
(68 683 families with modulus | M), recovers |U_M| = 11 550 from [2M, 3M), and checks every unmarked n < 2M outside U_M by direct search. The only
non-values are 2, 3, 5, 6, 9, 11, 14, 15, 35 ∈ E_W (105 and 510 lie in U_M classes). ∎ (The earlier version leaned on R174's 10⁹ enumeration; that is
no longer needed.) This is a density statement only. Lorenzini/Wang already have density 1, so the novelty is the explicit
level and the explicit residual classes.

## 5. Short blocks: the least outer letter (EVIDENCE + heuristic CONJECTURE)
Let x*(n) := min{min(x,z) : xyz − x − z = n}. In the language of (F0), x*(n) is the first x ≥ 2 for which n + x has a divisor ≡ −1 (mod x) in
range. So the brief's "consecutive block" n + 2, n + 3, … is exactly the search for x*(n).
**EVIDENCE 5.1 (`scripts/bsG_xstar.c 10⁸`).** For every n < 10⁸, n ∉ E_W: **x*(n) ≤ 12**. Records: x* = 3 (n = 17), 4 (51), 6 (126), 12 (1379).
The decade maxima from 10³ on are 12, 8, 7, 9, 11. The counts #{n in decade : x*(n) > X} for X = 2…10 at [10⁷, 10⁸) are
5 096 879, 198 815, 17 577, 1 405, 169, 17, 8, 3, 1. The unique n in [10⁷, 10⁸) with x* = 11 is n = 64 858 079 (its immediate neighbours have x* = 2); two further n there have x* = 10 (R180 repair, D6b).
**Heuristic.** For fixed x, the integers m with no divisor ≡ −1 (mod x) have density ≍ (log m)^{−δ_x}. Here δ_x = 1 − |H_x|/φ(x), and H_x is a
largest subgroup of (Z/x)^× not containing −1. Hence δ₂ = 1 (m prime or 2^k), δ_x = 1/2 for x = 3, 4, 6, 7, 8, 9, 11, 12, …, δ₅ = δ₁₀ = 3/4,
and δ_x = 1 − 2^{−v₂(φ(x))} for cyclic (Z/x)^×. In general δ_x = 1 − 1/r_x, where r_x is the least order of an odd Dirichlet character mod x. So
δ_x = ½ whenever some prime p ≡ 3 (4) divides x, which is true for almost all x. Treating the x-events as independent,
#{n ≤ N : x*(n) > X} ≈ N (log N)^{−Σ_{x≤X} δ_x}. Here **Σ_{x ≤ X} δ_x = (½ + o(1))X** (numerically 0.557·X at X = 1000, `scripts/review_lw_delta.py`).
(R180 repair, D5: an earlier version claimed (1 + o(1))X via v₂(φ(x)) → ∞, which is valid only for cyclic groups.) This predicts
**CONJECTURE 5.2 (short-block (W)).** x*(n) ≪ log n / log log n for n ∉ E_W. (The naive independence model gives x*(n) ≤ (2 + o(1)) log n / log log n — R180 repair, D5.)
The observed decay of the X = 4 column (8.8, 4.9, 3.0, 1.95 ·10⁻⁴ per decade) gives an effective exponent ≈ 2.9 against the naive Σ_{x≤4} δ_x = 2.
So the joint events are positively correlated, but in the predicted direction.
**Why no deterministic block argument (PROVED, via §4).** Fix X and a divisor bound D. Every n in the clopen neighbourhood
n ≡ −1 (mod lcm{d ≤ D}) has no divisor d ≤ D of n + x with d ≡ −1 (mod x) and d ≥ 2x − 1, for every x ≤ X. Indeed d | n + x forces d | x − 1 < d.
So any block argument must use divisors larger than every fixed bound, i.e. the large prime factors of the n + x. Those are
prime-constellation events ("n + 2 prime, n + 4 a sum of two squares, n + 3 of the form a² + 3b², …" all at once). The norm-form parts can be met
simultaneously by polynomial families (consecutive sums of two squares exist infinitely often). The x = 2 part is a primality
condition, so it is a parity-type sieve problem. **Assessment:** the consecutive-integer route is a prime-k-tuple-type lower-bound problem
(in the opposite direction from a sieve upper bound), with no known technology. It is attractive mainly as a sharp, testable numerical law.

## 6. An unconditional quantitative density bound (PROVED, using the Titchmarsh divisor theorem — a theorem: Linnik 1963; Rodriquez 1965 / Halberstam 1967 via Bombieri–Vinogradov. R180 repair, D3)
**Prop 6.1.** #{n ≤ N : n ∉ V_{A₃}(2)} ≪ N·exp(−c √(log N)) for an absolute c > 0.
*Proof.* Let S = E ∩ (N, 2N] be the set of exceptions there, and Q = √N. For a prime p ≤ Q and x | p + 1 with 2 ≤ x ≤ (p+1)/2, every n ≡ −x (mod p) with n > N
is a value: take (x, (p+1)/x, (n+x)/p), where z = (n+x)/p ≥ 2 because n > Q² ≥ 2p. So S avoids ω(p) = τ(p+1) − 2 distinct classes mod p. By
Montgomery's large sieve, |S| ≤ (N + Q²)/L with L = Σ_{m ≤ Q} μ²(m) Π_{p|m} ω(p)/(p − ω(p)) ≥ e_k(g; I), where e_k is the
k-th elementary symmetric sum of g(p) = ω(p)/p over p ∈ I = (Q^{1/(2k)}, Q^{1/k}]. By the Titchmarsh divisor problem (Linnik; via Bombieri–Vinogradov),
Σ_{p ≤ y} τ(p+1) = C y + o(y) with C = ζ(2)ζ(3)/ζ(6). Partial summation gives G := Σ_{p∈I} g(p) = (C/2 + o(1)) (log Q)/k − 2 log 2 + o(1).
By inclusion–exclusion, k!·e_k ≥ G^k − C(k,2)·T·G^{k−2} with T := Σ_{p∈I} g(p)² (R180 repair, D3). Take k = ⌊ε √(log Q)⌋. Then
k/G → 2ε²/C is a constant (not o(1)), but T ≤ Σ_{p > min I} p^{−2+o(1)} → 0 because min I = Q^{1/2k} → ∞; so e_k ≥ ½ G^k/k! ≥ (eG/k)^k/(2e√k) for large Q,
and eG/k ≈ eC/(2ε²) > e for ε small. Then L ≥ exp(c′ √(log Q)), and dyadic summation finishes. ∎ (Only the lower bound Σ_{p∈I} τ(p+1)/p ≫ log Q/k is
needed, which Bombieri–Vinogradov gives directly.)
*Remarks.* This is the (W)-analogue of the classical ES density bounds. Vaughan (1970) has N exp(−c log^{2/3} N) for ES. Using composite moduli
(non-CRT avoided classes) is what would improve it, and is a spark. Lorenzini/Wang state density 1. But the correct baseline is stronger. Lorenzini's
Prop 6.3(b) already gives #E ∩ [1,N] ≤ π(N+2) + O(log N) ≪ N/log N, and his z = 4 condition gives ≪ N(log N)^{−3/2}. Prop 6.1 beats every power of log
(R180 repair, D4). The bound is
far from finiteness, as it must be (B6).

## 7. Stern / Minkowski coding (PROVED identity)
**Prop 7.1.** For letters a₁, …, a_k ≥ 2, Stern's diatomic sequence satisfies
s(1 0^{a₁−2} 1 0^{a₂−2} 1 ⋯ 1 0^{a_k−2} 1 (binary)) = K⁻(a₁, …, a_k) = d_{A_k}(a₁, …, a_k).
Hence **V_{A_k}(2) = {s(N) : popcount(N) = k + 1}**, and (W) says that every n ∉ E_W is a Stern value at a position with exactly four 1-bits.
*Proof.* Put u = s(N), w = s(N+1). Appending a bit 0 maps (u, w) ↦ (u, u + w), and appending 1 maps (u, w) ↦ (u + w, w). So the block 0^{a−2}1 maps
(u, w) ↦ ((a−1)u + w, (a−2)u + w). In p := u, q := u − w this reads (p, q) ↦ (ap − q, p), the negative-continuant recursion. The
start N = 1 gives (p, q) = (1, 0). Trailing zeros do not change s. ∎ Checked exhaustively for a_i ≤ 26, k = 3 (/tmp check; `scripts/bsG_stern.py`).
`scripts/bsG_Ak.c` reproduces Lorenzini's lists L_{A₃} (to 10⁸), L_{A₄} (to 10⁸), L_{A₅} and L_{A₆} (to 10⁷) exactly.
*Reading.* s is 2-regular (Allouche–Shallit), and positions of popcount k + 1 form a sparse regular language: ≍ (log X)^k positions N < X (R180 repair, D6c; s is not monotone, so this counts positions, not values). So (W)
asks that the image of a 2-regular sequence on the popcount-4 slice covers a cofinite set. I found no theorem about images of 2-regular sequences on fixed-popcount
slices (Defant 2016 bounds max s on fixed popcount; Stanley–Wilf refine by number of parts). Assessment: a clean dictionary, no tool.

## 8. (W) restricted to what ES needs is trivial: all the ES content of SQ₅ is the sign (S) (PROVED; SHARP)
**Prop 8.1.** Every n ≡ 1 (mod 4) with 3 ∤ n and n ≥ 13 is a value of xyz − x − z (x, y, z ≥ 2). Explicitly:
* n ≡ 1 (mod 3): (x, y, z) = (2, 2, (n+2)/3);
* n ≡ 2 (mod 3), i.e. n ≡ 5 (mod 12): (x, y, z) = (3, (n+7)/12, 4). Check: 12(n+7)/12 − 7 = n.
In particular **(W) holds at every prime p ≡ 1 (mod 4), p ≥ 13.** (The ES-relevant scope noted by R174 D1.) ∎
(R180 repair, D6a.) The first family alone shows more: **every n ≡ 1 (mod 3), n ≥ 4, is a value** ((2, 2, (n+2)/3)). That is not stated in Lorenzini's Prop 6.3,
whose (c) is weaker, and it is used in the residue computations below.
(R184 repair, D5: attribution.) Both families are slices Lorenzini already uses. (2,2,·) is his z = 2 slice (3 | n + 2, so n + 2 is neither prime nor a
2-power; this is the z = 2 claim (i) in his proof of 6.3). (3,·,4) is his z = 4 slice with the divisor (n+4)/3 ≡ 3 (mod 4). So Prop 8.1 is a two-line
strengthening of Lorenzini 6.3(c) (it drops his mod-9 condition), not a new idea.
**Cor 8.2.** For primes p ≡ 1 (4), p ≥ 13: interior-SQ₅(p) ⟺ (S)(p), i.e. *L₃(p) (which is non-empty) contains a Jacobi −1 word*.
(R184 repair, D4.) For p ≡ 5 (mod 12) the word (3, (p+7)/12, 4) is itself a −1 word (see below), so (S)(p) and interior-SQ₅(p) are PROVED there.
Cor 8.2 has content only for p ≡ 1 (mod 12).
The (W) half of HJ_DEEP's split carries no ES content at primes.
**Signs of the two families.** For p ≡ 5 (mod 12) the word (3, (p+7)/12, 4) has A = 3t − 1 = (p+3)/4 and (A/p) = (3/p) = (p/3) = −1. This
is the classical p ≡ 2 (mod 3) ES identity in HJ form. For p ≡ 1 (mod 12) the word (2, 2, (p+2)/3) has both A-values 3 and (2p+1)/3 ≡ 3⁻¹,
with sign (3/p) = +1. So it is useless for ES, and (S) must find another word. That is the hard residue (Mordell's classes) again.
(`scripts/bsG_primes_W.py`: all 74 415 primes p ≡ 1 (4), 13 ≤ p < 2·10⁶, 0 failures. `scripts/bsG_primes.c 10⁸`: x*(p) ≤ 3 for all
primes p ≡ 1 (4) below 10⁸, as Prop 8.1 forces; min R(p)/mean R(p) ≈ 0.26 at 10⁸.)
**Where (W) is still open after Prop 8.1, Prop 3.3 and Lorenzini 6.3.** n ≡ 0 (4) is trivial ((2, n/4+1, 2)), n ≡ 1 (3) is trivial ((2,2,·)), and
n ≡ 5 (12) is trivial ((3,·,4)). Lorenzini (b) handles n odd with n + 2 composite. The residue is therefore
**n ≡ 3, 9, 11 (mod 12) with n + 2 prime, and n ≡ 2, 6 (mod 12) with n + 2 = 2^m** (Lorenzini (a): m odd). On these (W) is a genuine
divisor-in-moving-class problem. It is ES-irrelevant except for n ≡ 9 (12) composites through SQ₅ (for which see HJ_DEEP's (S)).
**Assessment.** This deflates the "(W) as an ES test bed" motivation: what ES needs from (W) is trivial. The interest of (W) is now as Lorenzini's
problem in its own right. For ES, the spark relay should redirect to (S) at primes p ≡ 1 (mod 12) (ultimately Mordell's residual classes mod 840),
which is the familiar sign/genus layer: Prop 4.1 of HJ_DEEP.

## 9. The even half of Lorenzini's question is settled (PROVED; not found in the literature — R184 repair, D8: not in Lorenzini 2024, Wang–Lu 2026, the citing papers on Semantic Scholar, or Lorenzini's later preprints; Google Scholar lists 9 citers, of which 2 were not seen)
**Theorem 9.1.** Every even n ≥ 16 with n ≠ 510 is a value of xyz − x − z with x, y, z ≥ 2. Equivalently, the even part of the complement of
V_{A₃}(2) is exactly {0, 2, 6, 14, 510}.
*Proof.* By Lorenzini Prop 6.3(a) it suffices to treat n = 2^m − 2 with m odd. (For other even n: z = 2 if n + 2 is not a 2-power, and
(4, (2^{m−3}+1)/3, 6) if m ≥ 6 is even.) For odd m the following six fixed-pair families cover every odd class of m mod 36:
| family | condition on n | in terms of m | covers odd m (mod 36) |
|---|---|---|---|
| (x,z) = (3,3) | 9 \| n + 6 | 2^m ≡ 5 (9) ⟺ m ≡ 5 (6) | 5, 11, 17, 23, 29, 35 |
| (x,z) = (6,12) | 72 \| n + 18 | m ≥ 3 and 2^m ≡ 2 (9) ⟺ m ≡ 1 (6) | 1, 7, 13, 19, 25, 31 |
| (x,y) = (7,2) | 13 \| n + 7 | 2^m ≡ 8 (13) ⟺ m ≡ 3 (12) | 3, 15, 27 |
| (x,z) = (3,9) | 27 \| n + 12 | 2^m ≡ 17 (27) ⟺ m ≡ 15 (18) | 15, 33 |
| (x,y) = (10,11) | 109 \| n + 10 | 2^m ≡ −8 (109) ⟺ m ≡ 21 (36) | 21 |
| (x,z) = (8,74) | 592 = 16·37 \| n + 82 | m ≥ 4 and 2^m ≡ 31 (37) ⟺ m ≡ 9 (36) | 9 |
The third letter is z = (n+x)/d for the (x,y) families and y = (n+x+z)/(xz) for the (x,z) families. It is ≥ 2 for n ≥ 2·592 − 82 = 1102 (the worst family is (8,74)), in particular for all odd m ≥ 11 (R184 repair, D1).
For m ∈ {1, 3, 5, 7, 9}: 0, 6 and 510 are exceptions, 30 = (3,4,3) and 126 = (6,2,12). (These two are caught by the (3,3) and (6,12) families, so only
m = 1, 3, 9 are genuine exceptions to the covering.) ∎
Certificate: `scripts/bsG_pow2_cert.py` (greedy cover found automatically; explicit solutions checked with exact integers for all odd 11 ≤ m ≤ 4001).
`scripts/bsG_pow2.py 20000 L` shows that L = 36 is the least period among {12, 36, 60, …} that works; L = 12 misses m ≡ 9.
(R184 repair, D2: more precisely, with all fixed-pair families of modulus ≤ 3000, no even period L < 36 works — 12 misses 9; 18 misses 3, 9; 24 misses 9, 21;
30 misses 3, 9, 21 — and 36 is the least even period that works; `scripts/review_lw2_period.py 3000 72`.)
The orders used are ord₉(2) = 6, ord₁₃(2) = 12, ord₂₇(2) = 18, ord₁₀₉(2) = ord₃₇(2) = 36. This is a Sierpiński-type covering, possible here because the
family 2^m − 2 is a *one-parameter exponential* family: it is not dense in Ẑ, so the sterile set (§4) does not obstruct it.
**What remains of (W) (exact).** By Lorenzini 6.3(b), Prop 8.1 and Thm 9.1, (W) is equivalent to: **every odd n ≡ 3, 9, 11 (mod 12) with n + 2 prime,
n ∉ {3, 9, 11, 15, 35, 105}, is a value.** Here the residue is a prime-shift set, dense in every congruence class compatible with it (n ≡ −1 (mod M) is
compatible). So no finite covering can finish it (HJ_DEEP Lemma 3.2 restricted to n + 2 prime: each class n ≡ −1 (mod M) contains
infinitely many n with n + 2 prime, by Dirichlet applied to primes ≡ 1 (mod M)).
