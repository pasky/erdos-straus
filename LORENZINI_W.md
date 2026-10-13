# LORENZINI_W — attacking Lorenzini's A₃ question (W) (O180, spark relay G)

Status: internal research note, SPARK phase. **(W) is NOT proved here; ES is not solved.** Labels as in DISCOVERIES.md.
Scripts `scripts/bsG_*`. Builds on HJ_DEEP.md (O174, reviewed R174) and DEDEKIND_ES.md.

**(W)** (Lorenzini, *The critical polynomial of a graph*, J. Number Theory 257 (2024) 215–248, arXiv:2311.06367, Example 6.2(a);
still open: T. Wang, EJC 33(3) #P80 (2026) calls finiteness "an open problem"): every n ≥ 2 outside
E_W = {2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510} is n = xyz − x − z with x, y, z ≥ 2. EVIDENCE to 10⁹ (O174/R174).
Scope reminder (R174 D1): ES needs only (W) at primes p ≡ 1 (4) (plus (S)); global (W) is stronger.

## 0. Summary (updated as the work proceeds)
1. Four further elementary equivalent forms of (W) (§1, PROVED, checked against brute force for n < 700).
2. **(W) is not T1-free: odd/even squares carry a partial genus obstruction ("square shadow", §3, PROVED).** At n = m² the
   middle letter y satisfies y ≢ 0 (mod 4), y ≢ 7 (mod 8), and y ≢ 3 (mod 4) if m is even. The record-low
   values of R(n) = #solutions are squares of smooth numbers (5336100 = 2310², R = 4, against a mean ≈ 104 there).
   Yet squares are not exceptions: **every square except 1 and 9 is a value (Prop 3.3, PROVED; two families).**
3. Profinite "sterile set" (§4): the closed set S ⊂ Ẑ of points that no fixed-pair family covers. It contains −1 (HJ_DEEP Lemma
   3.2) and more (single-prime deviations ν(ℓ, c)). So compactness-type arguments cannot prove (W).

## 1. Elementary equivalent forms (PROVED; `scripts/bsG_forms.py 700`: 0 mismatches against brute force)
For n ≥ 2 the following are equivalent to (W)(n) ("n = xyz − x − z, x, y, z ≥ 2"):
* (F0) [HJ_DEEP] ∃ t ≥ 2: tn + 1 = (tx − 1)(tz − 1), x, z ≥ 2. ∃ x ≥ 2: n + x has a divisor d ≡ −1 (mod x), d ≥ 2x − 1, (n+x)/d ≥ 2.
* (F1) **∃ x, z ≥ 2 with xz | n + x + z** and (n + x + z)/(xz) ≥ 2. (Then y = (n+x+z)/(xz).) For coprime x, z this is
  "x | n + z and z | n + x": a pair of mutually n-shifted divisors.
* (F2) **∃ z ≥ 2: with q = ⌈n/z⌉ and r = qz − n, r ≥ 2 and r | q + 1** (and (q+1)/r ≥ 2); or a diagonal solution x = z
  (x | n, x | n/x + 2). *Proof.* n = qz − r with x = r, y = (q+1)/r gives xyz − x − z = (q+1)z − r − z = n. Conversely any
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
**Remark 3.2 (n = k m²).** The same argument gives: if n = k m², no word has middle t ≡ 0 (mod 4k). Here q | tn + 1 forces
(−t/(4k)… ) i.e. (−s/q) = 1 for t = 4ks, and X ≡ −1 (mod 4s) gives (−s/X) = −1. EVIDENCE (`scripts/bsG_kshadow.py`):
35 372 words at n = k m² (k ∈ {1,2,3,5,6,7}, m < 160), 0 violations of Lemma 3.1 / Remark 3.2.
`scripts/bsG_sqslices.py 300`: middle letters mod 8 at odd squares {1,2,3,5,6}, at even squares {1,2,5,6}, and at the control
n = m² + 2 all eight classes occur.
*Reading.* HJ_DEEP called (W) "T1-free". That is true only for the existence statement, not for the mechanism. At squares, exactly the
genus character that kills ES (the t ≡ 0 (mod 4) slices) also kills the slices t ≡ 3 (mod 4) (mostly). Squares of smooth
numbers additionally lose all small prime factors of tn + 1 (tn + 1 ≡ 1 mod every prime dividing m). This explains the record lows of §2.
**Barrier consequence (B5 for (W), PROVED by Lemma 3.1).** Any argument for (W) that uses only middle letters t ≡ 0 (mod 4), or only
t ≡ 3 (mod 4) for even n, gives nothing at squares. This applies to Lorenzini's z = 4 slice read as a middle letter… (no: z is an outer
letter; the shadow constrains only the middle letter). A route must use t ≡ 1, 2 (mod 4) at squares.

**Prop 3.3 (squares; PROVED).** Every square n = m² ∉ {1, 9} is a value of xyz − x − z with x, y, z ≥ 2.
*Proof.* m even: n ≡ 0 (mod 4) and (2, n/4 + 1, 2) works. 3 ∤ m: n ≡ 1 (mod 3) and (2, 2, (n+2)/3) works, with (n+2)/3 ≥ 2 for n ≥ 4.
m = 3k with k odd ≥ 3: (3, (k²+1)/2, 6) gives 18(k²+1)/2 − 9 = 9k² = n. ∎
(Certificate `scripts/bsG_sqproof.py`: a greedy covering of odd m mod 180 picks exactly these two families; explicit solutions are checked for all
odd m < 20001.) So the shadow lowers R(m²) but never empties it. This contrasts sharply with ES, where T1 empties every slice.
**Assessment.** The shadow is the precise sense in which T1 "acts" on (W). It shows that (W) is not a cleaner test bed than ES as far as
genus characters go. However the shadow is partial (two of four middle classes mod 4 survive), and the surviving slices
(t = 2, (x,z) = (3,6)) already cover squares by congruences, because −1 is not a square mod 3 or 4. The class n ≡ −1 (mod M) that defeats every
finite covering (HJ_DEEP Lemma 3.2) contains no squares.
