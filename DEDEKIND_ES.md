# DEDEKIND_ES — exact lattice-point formulas, Dedekind sums and reciprocity for ES certificates (O169)

Status: internal research note, SPARK phase. **ES is not solved here, nor any infinite case of it.**
Labels as in DISCOVERIES.md. Scripts `scripts/dk_*`.

Notation. For 0 < A < n, gcd(A,n) = 1: `n/A = [[b₁,…,b_r]] = b₁ − 1/(b₂ − 1/(⋯ − 1/b_r))`, b_i ≥ 2, the
Hirzebruch–Jung (negative, "HJ") continued fraction; `r(n/A) := r` its length; `A* ∈ (0,n)` with `AA* ≡ 1 (n)`;
`s(a,c)` the Dedekind sum. `K(b₁,…,b_r)` = negative continuant (numerator of `[[b₁,…,b_r]]`):
`K(b) = b`, `K(b₁,b₂) = b₁b₂ − 1`, `K(b₁,b₂,b₃) = b₁b₂b₃ − b₁ − b₃`.

## 1. Dictionary: X-slice certificates are HJ fractions of length 3 (PROVED, elementary)

**Lemma 1.1.** Let n ≥ 2. The map `(t,u,v) ↦ A = tu − 1` is a bijection
`{(t,u,v) ∈ ℤ³_{≥2} : tuv − u − v = n}  →  L₃(n) := {A ∈ (0,n) : gcd(A,n) = 1, r(n/A) = 3}`,
with `n/A = [[v,t,u]]`, `A* = tv − 1`, `AA* = tn + 1`.
*Proof.* `[[v,t,u]] = v − u/(tu−1) = (v(tu−1) − u)/(tu−1) = (tuv−u−v)/(tu−1)`, and numerator/denominator are
coprime (consecutive convergents of an HJ CF are coprime: the convergent matrices have determinant 1). HJ
expansions with all b_i ≥ 2 are unique (the first entry is `⌈n/A⌉`, A ↦ ⌈n/A⌉A − n is the HJ step), so every
A with r(n/A) = 3 arises exactly once. Finally `(tu−1)(tv−1) = t(tuv − u − v) + 1 = tn + 1`, and `tv−1 < n`. ∎

So `E(n) := {(t,u,v) : tuv − u − v = n}` (WINDMILL_REDUCTION §6, PARITY_FIXED_P (★)) is, up to the boundary
cases u = 1 or v = 1 (which are HJ length 2: `n/(t−1) = [[v,t−1]]`-type data, i.e. divisors of n+1), the set
of **length-3 HJ fractions with numerator n**, and `(t,u,v)` are their partial quotients (middle one = t).

**Corollary 1.2 (ES slices in HJ language).**
* (Type I, slice a = 1; CONDITIONAL_ES Lemma 1.1) If some `A ∈ L₃(p)` has `A ≡ 0 (mod 4)`, then ES(p):
  with `n/A = [[v,t,u]]`, `m = A = tu − 1`, `m'' = A* = tv − 1`, `4/p = 1/(bdp) + 1/(cd) + 1/(bcd)` with
  `(c,f,g) = (v,u,t)`, `d = A/4`, `b = (p+v)/u`.
* (Type II, (A)3: `4abc − a − b = p`) If some `A ∈ L₃(p)` has middle entry `t ≡ 0 (mod 4)`, then ES(p)
  (`4/p = 1/(abc) + 1/(acp) + 1/(bcp)` with `(a,b,c) = (u,v,t/4)`).
So, in the cleanest form: **ES(p) ⇐ some reduced fraction A/p with A ≡ 0 (4) has HJ length exactly 3.**
In toric language: the cyclic quotient singularity `1/p(1,A)` has a minimal resolution
with exactly three exceptional curves.

EVIDENCE/CERTIFIED (`scripts/dk_dict.py 3000`, exact rationals): Lemma 1.1 as a set identity, and (D2), (D3)
of §2, for all primes and odd squares ≤ 3000 (0 failures); at every odd square n ≤ 3000, no `A ∈ L₃(n)` has
`A ≡ 0 (4)` (T1 control, as it must by ET Prop 1.6).

## 2. Dedekind sums see exactly the alternating half of the CF (PROVED, classical + one-line consequence)

**(D2) Hirzebruch–Zagier / Myerson formula** (classical; Hirzebruch–Zagier, *The Atiyah–Singer theorem and
elementary number theory*, 1974 — cited from memory, verified numerically, `dk_dict.py`):
`12 s(A,n) = Σ_{i=1}^r (b_i − 3) + (A + A*)/n`.

**(D3) Corollary (PROVED).** Let `r = r(n/A)`, `r' = r(n/(n−A))`. Then
`r − r' = −12 s(A,n) − 1 + (A + A*)/n`.
*Proof.* Riemenschneider duality: `Σ_i (b_i − 2) = r' − 1`. Apply (D2) to A and to n − A (whose inverse is
n − A*, and s(n−A,n) = −s(A,n)), eliminate Σb'_j = (r − 1) + 2r'. ∎

On a certificate `n/A = [[v,t,u]]`: `12 s(A,n) = t + u + v − 9 + (A+A*)/n` and `r' = t + u + v − 5`.
So **the Dedekind sum s(A,n) determines r − r' (the alternating sum of regular partial quotients) but not r
itself**. (R169 repair of a garbled sentence:) for the regular CF `n/A = [a₀; a₁, a₂, …]` one has
`r(n/A) = 1 + Σ_{i odd} a_i`, so "r = 3" is the condition that the odd-indexed regular partial quotients sum to 2.
That is the pattern `[v−1; 1, t−2, 1, u−1]`, or `[v−1; 2, u−1]` when t = 2 (entries 2 in [[·]] merge into the 1-strings).

## 3. T1 in Dedekind clothing: the X-slices force a quadratic non-residue (PROVED)

**(R) Rademacher's congruence** (classical; Rademacher–Grosswald, *Dedekind Sums*, Ch. 3, from memory;
checked for all odd c < 400 in `scripts/dk_t1mod8.py`): for odd c ≥ 3 and gcd(a,c) = 1,
`12 c s(a,c) ≡ c + 1 − 2·(a/c)  (mod 8)` (Jacobi symbol).

**Proposition 3.1 (PROVED).** Let n ≡ 1 (mod 4) be odd and `n/A = [[v,t,u]]` with `4 | A` (Type I slice) or
`4 | t` (Type II (A)3 slice). Then the Jacobi symbol `(A/n) = −1`. In particular **no such A exists when n is
an odd square** (then `(A/n) = 1` for every A coprime to n): this is ET Prop 1.6 / T1 for these slices.
*Proof.* By (D2), `12 n s(A,n) = n(t+u+v−9) + A + A*` with `A = tu−1`, `A* = tv−1`. Insert into (R):
`2(A/n) ≡ n + 1 − n(t+u+v−9) − (tu−1) − (tv−1) (mod 8)`, a polynomial in (t,u,v), so its residue depends
only on (t,u,v) mod 8. The finite check over all 512 triples (`dk_t1mod8.py`: 32 admissible triples per slice)
shows the right side ≡ −2 (mod 8) whenever `tuv − u − v ≡ 1 (4)` and `4 | tu−1` (resp. `4 | t`). ∎
Numerically (all primes < 2·10⁴): on L₃(p) the symbol `(A/p)` is −1 on both slices when p ≡ 1 (4), +1 when
p ≡ 3 (4). *(R169 repair: the earlier "equidistributed (≈ 50:50) on the other classes of (A,t) mod 4" was false.
Several other classes are deterministic, e.g. (A,t) ≡ (1,1) is always +1 and (1,3), (3,1), (3,3) are always −1 for
p ≡ 1 (4); the exact law is the mod-4 table of §8.1.)*

*Credit.* For the 4|A slice this is the same fact as reviews/redteam-automorphic.md Lemma 5.2 (`(d/p) = −1`,
d = A/4, via notes Lemma 77.6); what is new here is the derivation from Dedekind sums and its extension in Thm 4.5.

*Reading.* The exact Dedekind formula (D2) plus the mod-8 law (R) is precisely the genus obstruction: on
the X-slices, a certificate lives in the quadratic-non-residue half of (ℤ/p)^*. That half exists at primes
and is empty at squares. Everything that Dedekind sums know *mod a fixed modulus* is of this kind (by (R) and
`12 c s(a,c) ≡ a + a* (mod c)`, the residue of `12 c s(a,c)` mod `8c` is fixed by `c mod 8`, `(a/c)`, and
`a + a* mod c`). By Prop S of BRAINSTORM/invol_sign_identities, such data cannot certify the square classes.
A Dedekind route has to use the **real size** of s(A,p) (equivalently r − r', by (D3)), not its residues.

## 4. The genus character on HJ words; boundary certificates; the vanishing set

**Corollary 4.1 (PROVED, from (R) and (D2)).** For odd n and `n/A = [[b₁,…,b_r]]`, with `n = K(b₁..b_r)`,
`A = K(b₂..b_r)`, `A* = K(b₁..b_{r−1})` (continuants):
`2·(A/n) ≡ n + 1 − n·Σ(b_i − 3) − A − A*  (mod 8)`.
So the Jacobi symbol `(A/n)` is a polynomial function of `(b₁,…,b_r) mod 8`: a **genus character on HJ words**
(for each fixed length r). Prop 3.1 is the statement that on the length-3 cylinder with `4 | A` (or `4 | t`)
this character is constant −1 when n ≡ 1 (4). (Jacobi symbols via the Euclidean algorithm are classical; this
is the HJ/Dedekind packaging of that fact.)

**4.2 Boundary certificates (PROVED, elementary).** The X-slice of WINDMILL_REDUCTION §6 / CONDITIONAL_ES
Lemma 1.1 also allows t, u or v = 1, which fall outside `(0, n)`:
* t = 1: `n + 1 = AA*`, `4 | A` — needs n ≡ 3 (4).
* u = 1: `A = t − 1 | n + 1`, `4 | A` — needs n ≡ 3 (4).
* v = 1: `A = n + u > n`, `A* = t − 1`, `u(t−1) = n + 1`, `tu ≡ 1 (4)`. For n ≡ 1 (4) this forces
  `t ≡ u ≡ 3 (4)`, so it holds **iff (n+1)/2 has a prime factor ≡ 3 (mod 4)** (take u = that factor). At
  `n = m²` (m odd), `(m²+1)/2 = ((m+1)/2)² + ((m−1)/2)²` is a sum of two coprime squares, so it has no such factor (T1
  again).
So for p ≡ 1 (4): **X-slice ES(p) ⟺ [some `A ≡ 0 (4)` has `r(p/A) = 3`] or [(p+1)/2 has a prime factor ≡ 3 (4)].**

**4.3 Minimal HJ length in the class A ≡ 0 (4) (EVIDENCE, `/tmp` probe recorded here).** For n ≡ 1 (4) and
`C₀ = {A ≡ 0 (4)}`: A = 4 gives `n/4 = [[(n+3)/4, 2, 2, 2]]` (length 4, `(4/n) = +1`), so min r over `C₀ ∩ QR`
is ≤ 4, and lengths 1, 2 are impossible in C₀. All primes p ≡ 1 (4), 5 < p ≤ 6000: min r over `C₀ ∩ QR` = 4,
min r over `C₀ ∩ QNR` = 3 except at p = 17, 241, 769, 1409, … (min 4; these primes are then solved by the
boundary case 4.2). At all 38 odd squares ≤ 6000, min r over C₀ = 4 and C₀ ⊂ QR.

**4.4 Vanishing set over all odd n (EVIDENCE, `scripts/dk_vanish.py 200000`).** Let `a₀(n)` resp. `a_T(n)` count
`n/A = [[v,t,u]]` with `4 | A`, resp. `4 | t`. Among the **non-square** n ≡ 1 (4), n ≤ 2·10⁵ (primes and
composites), `a₀(n) = 0` for 52 values (largest 156961), and `a₀(n) = a_T(n) = 0` for only 22 values, the largest
being 28225 = 5²·1129. The full list is 5, 17, 65, 105, 241, 265, 321, 465, 545, 681, 769, 801, 1161, 1409, 2265, 2641,
2929, 3705, 5105, 8865, 13041, 28225. At every odd square both vanish (Prop 3.1). **CONJECTURE (from this
EVIDENCE):** for non-square n ≡ 1 (4), n > 28225, `a₀(n) + a_T(n) > 0`. Thus, empirically, the Jacobi
obstruction of Prop 3.1 is the *only* obstruction to the two interior HJ-length-3 slices, for composite n as
well as for primes. An exact formula for `a₀ + a_T` would have to vanish exactly on the squares (and on a
finite set). The simplest objects with that property are counts of Jacobi −1 classes, such as
`#{A ∈ (ℤ/n)^* : (A/n) = −1} = φ(n)/2·[n ≠ □]`.

**Theorem 4.5 (ES certificates of length 3 = quadratic non-residues; PROVED).** Let n ≡ 1 (mod 4) and
`A ∈ L₃(n)`, `n/A = [[v,t,u]]`. Then
`(A/n) = −1  ⟺  4 | tu−1 (Type I, a = 1)  or  4 | tv−1 (its reversal)  or  4 | t ((A)3)  or  4 | u  or  4 | v`.
Each of the five conditions gives an ES solution of 4/n: the first three by Cor 1.2. For `4 | u = 4w`:
`n + v = 4w(tv − 1)`, so `f = tv − 1 ≡ −1 (mod v)` divides `N = (n+v)/4`. This is the Type II e-slice
`−1 ∈ Σ_e(N)` with `e = v`, `(a,b) = (f,1)`; `4 | v` is its reversal. Explicit ES triples (R169 repair). For `4 | u = 4w`, `f = tv − 1`:
`4/n = 1/(wf) + 1/(tnw) + 1/(tnwf)`. This comes from `4/n − 1/N = v/(nN)` with `N = wf`, and
`v/(nN) = (f+1)/(tnN) = 1/(tnw) + 1/(tnwf)`. It is a Type II solution, since two denominators are divisible by n.
For `4 | v = 4w'`, `f' = tu − 1`: `4/n = 1/(w'f') + 1/(tnw') + 1/(tnw'f')`.
Both are verified in exact rationals for all n ≤ 5000 (`scripts/review_dk_core.py`).
*Proof.* By Cor 4.1, `(A/n)` depends only on `(t,u,v) mod 8`. `scripts/dk_cells.py` enumerates all 512 cells: of
those with `n ≡ 1 (4)`, the 120 cells with value −1 are exactly the cells satisfying one of the five conditions,
and the 40 cells with value +1 satisfy none. ∎ (Brute-force check, `scripts/dk_thm45_check.py 1000000`: all
21 430 357 length-3 words with n ≡ 1 (4), n ≤ 10⁶, 0 failures; 0 slice words at odd squares.)

**Corollary 4.6 (a "least non-residue in the Farey metric" form of ES; PROVED).** For a prime p ≡ 1 (mod 8) let
`λ(p) := min{ r(p/A) : (A/p) = −1 }` (the HJ length is 1 + the number of L-steps of the Stern–Brocot path, i.e. 1 + Σ_{i odd} a_i for the regular CF
— R169 repair of "number of left turns"; path from ∞
to p/A). Then `λ(p) ≥ 2` (L₁ = {1}), and
* `λ(p) = 2` ⟺ some divisor b of p+1 is a QNR ⟺ (p+1)/2 has a prime factor ≡ 3 (4) (since `(b/p) = (−1/b)` for
  odd b | p+1, and (2/p) = 1). This is exactly the boundary certificate of 4.2.
* `λ(p) = 3` ⟹ an interior X/e-slice certificate (Thm 4.5).
So **the five X/e-slices of ES(p) together hold ⟺ λ(p) ≤ 3** (R169 repair: slice parameters t,u,v ≥ 1 allowed;
every degenerate case at p ≡ 1 (4) is either impossible or gives λ = 2): *some quadratic non-residue mod p is reached
from ∞ by at most three left turns in the Farey graph.* At n = m² there are no non-residues (Jacobi), which is
the T1 obstruction in its barest form. EVIDENCE: λ(p) ∈ {2, 3} for all 556 primes p ≡ 1 (8), p ≤ 2·10⁴
(395 with λ = 2, 161 with λ = 3; `dk_qnr.py 20000`). Moreover all 19 552 primes p ≡ 1 (8), p ≤ 10⁶, have an
*interior* five-slice hit (λ ≤ 3 already with r = 3), and no odd square ≤ 10⁶ has any hit, interior or boundary
(`scripts/dk_lambda_big.py 1000000`).

*Reading.* The classical least quadratic non-residue `n_p` measures non-residues in the archimedean order. The
Burgess bound is `n_p ≪ p^{0.152}`, and n_p ≪ log²p under GRH. λ(p) measures them in the Farey/HJ word metric
centred at ∞. In that metric the ball of radius 3 is the sparse set `L_{≤3}(p)`, of expected size ≍ log²p, and the
conjecture λ(p) ≤ 3 is ES on five slices. Every Jacobi value on the ball is a mod-8 polynomial in the letters
(Cor 4.1), so "the ball contains a non-residue" is literally "the cubic `tuv − u − v = p` has a solution in one of
120 residue cells mod 8". This dictionary is exact but is not by itself a route (B1/B2).

## 5. Further dictionary items (each PROVED as stated, or labelled)

**5.1 Lattice geometry (PROVED, standard toric geometry).** For the cone `σ_A = cone((0,1),(p,−A))`, the compact boundary of
`conv(σ_A ∩ ℤ² ∖ 0)` has lattice points `w₀ = (0,1), w₁, …, w_r, w_{r+1} = (p,−A)` with `w_{i−1} + w_{i+1} = b_i w_i`.
The region between the apex and this boundary is the fan of the r+1 unimodular triangles `(0, w_i, w_{i+1})`. Hence
`r(p/A) = 2·Area(σ_A ∖ conv(σ_A ∩ ℤ²∖0)) − 1`. **ES X/e-slice(p) ⟺ some cone of determinant p whose second ray has
non-residue slope (A/p) = −1 has a lattice-free apex region of area exactly 2** (area 3/2 is the boundary case 4.2).
Dedekind sums are exact lattice counts in the *triangle* `conv(0, (p,0), (p,A))`. By (D3) they measure
`r − r'`, the difference between the apex areas of σ_A and of the dual cone. They do not measure r itself.

**5.2 Topology (PROVED dictionary; literature from memory).** `p/A = [[b₁..b_r]]` ⟺ the lens space L(p,A) bounds the
negative-definite linear plumbing of r spheres with Euler numbers `−b_i`. (D2) is the signature-defect /
Casson–Walker form of the Dedekind sum, and Cor 4.1 is van der Blij–Milgram–type for the linking form `A/p`.
So: **X/e-slice ES(p) ⟺ some L(p,A) with non-residue linking form bounds a linear plumbing of ≤ 3 spheres.**
By the Fintushel–Stern/Greene linking-form constraint (integral p-surgery on a knot in S³ gives L(p,q) only with
±q a square mod p), these are *among* (R169 repair: not "exactly"; the QR condition is only necessary) the short-plumbing lens spaces that are **not** integral surgeries on knots
in S³. At n = m², T1 corresponds to the fact that the linking-form invariant that matters, the Jacobi symbol,
is trivial. (Rational-homology-ball lens spaces, Lisca's classification, live at squares as well, e.g. the Wahl
fraction 25/14 = [[2,5,3]], but with A ≢ 0 (4) and Jacobi +1.) Assessment: gauge/Floer theory gives
*obstructions* to plumbings and surgeries, never existence of short plumbings, so I see no transferable theorem.

**5.3 Thin-group / Zaremba view (Assessment).** `L₃(p) = {γ = T^vST^tST^uS : v,t,u ≥ 2, γ₁₁ = p}`. Bourgain–Kontorovich
local–global theorems (Zaremba) need an orbit with growth exponent `2δ > 1` with room to spare, which gives about
`n^{2δ−1}` representations per n. The length-3 set has `#{γ : ‖γ‖ ≤ X} ≍ X log²X`, i.e. `2δ = 1` exactly, with
log² representations per n. This is B3 (scale constraint) in thin-group language: ES lies at the critical exponent,
where circle-method/expander methods give only density-type averages (B6).

**5.4 Euclid recursion (PROVED).** `A ∈ L_r(n) ⟺ (−n mod A) ∈ L_{r−1}(A)` and `⌈n/A⌉ ≥ 2`. So
`a_r(n) = Σ_{A<n} 1_{L_{r−1}(A)}(−n mod A)`, with `L₁(A) = {1}` and `L₂(A) = {b | A+1, 2 ≤ b ≤ (A+1)/2}`. For r = 3 this is
PARITY_FIXED_P (★). Dedekind reciprocity is the r-independent part of this recursion (it evaluates the
alternating sum). The r-dependent part is the backward-CF (Rényi) transfer operator, which has an indifferent fixed
point. Pointwise-in-n counts for it are fixed-denominator counts, so again B6 for averages and B2 for slices.

## 6. Construction log (which barrier hypothesis each attempt violated, and the outcome)

* **C1. Dedekind sums modulo a fixed modulus.** (Escapes "congruence data on n" by using p's CF.) Outcome: by (R)
  and `12cs ≡ a + a* (mod c)`, these data are (A/p), A + A* mod p and p mod 8. On the certificate locus they are
  exactly the genus character (Prop 3.1, Thm 4.5). Prop S (invol_sign_identities) then kills every parity law of
  this kind on square classes. **Dead (PROVED reduction).**
* **C2. The real value of s(A,p).** (Violates "congruence-only data".) Outcome: (D3) shows that s(A,p) determines
  `r − r'` exactly, while ES needs r = 3. The second invariant needed is `r + r'` (Stern–Brocot depth, equal to the
  total of regular partial quotients up to a constant). It satisfies no reciprocity law. Its sum over A is the
  Yao–Knuth count of `xy' − x'y = p`, a shifted divisor convolution (B6/H-A). **Reduces to H-A.**
* **C3. Smith-type palindrome mechanism.** (Smith's CF proof of p = a² + b² uses the fixed point of
  `A ↦ −A*` and reads the archimedean conclusion off the CF symmetry; this violates "𝔽_p-algebraic data only
  see square roots", because the CF converts a square root into sizes.) The CF-compatible symmetries of
  `{A : 0 < A < p}` that I know are the Klein group {id, A*, p−A, p−A*} (reversal, Riemenschneider duality).
  On L₃(p), reversal is free (u = v forces p = u(tu−2), not prime), and duality sends length 3 to length
  t+u+v−5. So no fixed-point mechanism lands in L₃. The fixed points of `−A*` give s(A,p) = 0 (two squares), which is
  information about L_r with r = r', not about short words. **No mechanism found** (no classification of
  CF-compatible maps attempted).
* **C4. Hecke–Knopp exact family.** (Violates "finite fixed-level identity" by an unbounded family of levels t.)
  By Thm 4.5 the certificate count is Σ over the 120 cells of the counts `#{(t,u,v) ∈ cell : (tu−1)(tv−1) = tp+1}`.
  For fixed t this is a twisted divisor sum at `N = tp+1` modulo 8t: a fixed-level Eisenstein coefficient,
  expressible through Knopp-type Hecke identities for generalized Dedekind sums. Each such identity sums over all
  `ad = N, b mod d`, so it carries exactly σ(N)-type information (SA Thm 9.1 per level). The t-family is
  PARITY_FIXED_P (★). I found no telescoping and no sign in the family. **Reduces to H-A (Assessment).**
* **C5. Size-literal parity laws** (the brief's Gauss-lemma spark, with weights that use sizes of lifts).
  `scripts/dk_parity_size.py 30000`: 820 sub-counts of `E_X(p)` (≤ 2 literals among orderings of t,u,v,A,A*,
  p^{1/2}, p^{1/3} thresholds, floor parities of 12s(A,p), (A+A*)/p, A/√p, 4A/p) — **none** is odd for all
  385 primes p ≡ 1 (24) ≤ 3·10⁴ (EVIDENCE, negative; extends WINDMILL_REDUCTION §6 from congruence literals to size
  literals).
* **C6. Archimedean least non-residues → Farey least non-residues.** (Burgess and Vinogradov give QNRs q ≪ p^{0.152}.)
  For small q, `r(p/q) = 1 + r(q/(−p mod q))`, so λ(p) ≤ 3 via A = q needs `(−p mod q) | q + 1`. That is one
  (★)-event per q, and a QNR prime q is no likelier to satisfy it than any other q. **Lottery (B3).**

## 7. Verdict (Assessment) and exact scope

* **PROVED:** Lemma 1.1, Cor 1.2 (X-certificates = HJ fractions of length 3); (D3); Prop 3.1 (T1 via Rademacher's
  mod-8 law, relative to the classical (R) and (D2)); Cor 4.1; 4.2; **Theorem 4.5** (for n ≡ 1 (4), a length-3
  HJ fraction is an ES certificate of one of five slices ⟺ its Jacobi symbol is −1); Cor 4.6 (the five slices ⟺
  λ(p) ≤ 3); 5.1, 5.4.
* **EVIDENCE:** λ(p) ≤ 3 for all primes p ≡ 1 (8) ≤ 10⁶ (interior r = 3 hit in every case); Thm 4.5 re-checked by brute force to 10⁶. The two interior slices 4|A, 4|t vanish at only 22
  non-square n ≡ 1 (4) ≤ 2·10⁵ (largest 28225). No size-literal parity law (C5).
* **CONJECTURE:** for non-square n ≡ 1 (4), n > 28225, `a₀(n) + a_T(n) > 0`. Equivalently, the Jacobi symbol is
  the only obstruction to the interior length-3 slices for all n, composite included.
* **Answer to the brief's question.** Can the moving-modulus ES conditions be encoded by finitely many
  Dedekind-type sums? **Yes, and the moving modulus disappears.** In HJ coordinates the ES conditions on the
  length-3 locus are one fixed character: the Jacobi symbol, i.e. Dedekind sums mod 8. The whole difficulty
  moves into the archimedean condition "HJ length = 3". Dedekind sums see only the antisymmetric part `r − r'`
  of that condition. The symmetric part `r + r'` obeys no reciprocity law, and its exact sums are shifted
  convolutions. T1 is fully explained: at m² the Jacobi symbol is +1 on every class, so no length-3 fraction is a
  certificate. Any reciprocity-forced positivity would therefore have to produce a *non-residue at Farey
  distance ≤ 3*. I found no mechanism that does this. The nearest classical analogue, Smith's palindrome proof,
  produces fixed points only for r = r'.

# Part II (parent follow-up: sign transfer, composites, complexity, statistics)

## 8. Structure of the sign; which maps can transfer it

**8.1 The sign is a mod-4 function (PROVED, `scripts/dk_sign.py`, finite check).** For n ≡ 1 (4) the Jacobi
symbol of a length-3 word `[[v,t,u]]` depends only on `(t,u,v) mod 4`. It is **+1 exactly on the five classes
`(t,u,v) ≡ (1,2,3), (1,3,2), (2,1,2), (2,2,1), (3,1,1) (mod 4)`** and −1 on the other 15 admissible classes. So
"non-certificate" means one of these five patterns. At squares, every length-3 word lies in them.

**8.2 Sign-preserving symmetries (PROVED).**
* Klein group: `(A*/n) = (A/n)` because `AA* ≡ 1`, and `((n−A)/n) = (A/n)` because `(−1/n) = 1`. Reversal, duality
  and their product preserve the sign.
* Rotation `(v,t,u) ↦ (t,u,v)`, `n ↦ n' = n + u − t`, is conjugation of `γ = T^vST^tST^uS` (cyclic word). The
  cell table (`dk_sign.py` (ii)) shows that **whenever n, n' ≡ 1 (4) the sign is preserved** (40 −1 cells → −1,
  8 +1 cells → +1). So on n ≡ 1 (4) the sign behaves as a conjugacy-class (genus-type) invariant of γ, and rotations
  cannot transfer it.
* Within a fixed n, the only CF-compatible bijections I know are the Klein group. Every other bijection of
  (ℤ/n)^* that preserves the Jacobi symbol (`A ↦ c²A`, inversion, negation) and moves A into L₃ is the problem itself.

**8.3 A genuine sign-FLIPPING transfer: scaling (PROVED).** For integers a ≥ 2 and u', v' ≥ 1:
`K(a v', t, a u') = a·K(v', a t, u')`, and both words have the same `A = a t u' − 1`. Hence, for odd a and odd
`m = K(v', at, u')`, `n = am`:
`(A/n) = (A/a)(A/m) = (−1/a)·(A/m)` (as A ≡ −1 mod a).
So **a word of m whose middle entry is divisible by a ≡ 3 (mod 4) and whose sign is +1 becomes a certificate
for n = am.** Degenerate m-words (u' = 1 or v' = 1) are allowed, because the scaled entries are ≥ a ≥ 3.
(Brute-force check of the sign law: 191 520 cases with a < 40 odd, 0 failures, `scripts/dk_scale.py`.)
This is consistent with T1. At n = m'² it forces every such inherited word to have sign +1 on the m-side,
which is a constraint on m and not a contradiction. The transfer needs a *composite* n. It cannot help at
primes, which have no factor a.

**8.4 The signed sum.** `S(n) := Σ_{A∈L₃(n)} (A/n) = N₊ − N₋`. By 8.1 it is a weighted count of the cubic's
solutions with weights ±1 given by the class mod 4. For fixed t this is a twisted divisor sum at `tn + 1` with
a mod-8 weight, and the sum over t is the (★)-type family again. No closed form was found (Assessment; cf.
STRONG_APPROX §9.1 for the analogous negative test on cubic counts). The only exact facts are that N₋ is even *at primes* (R169 repair: at composite n a self-reversed word u = v can
be −1, e.g. N₋(21) = 1 from [[3,3,3]])
(reversal pairs) and N₋(m²) = 0.

## 9. Composites, and the five-slice square conjecture

**9.1 EVIDENCE (`scripts/dk_vanish5.py 1000000`).** Among all non-square n ≡ 1 (4) up to 10⁶ (primes and
composites), the five slices together with the boundary case 4.2 vanish **only at n = 105** (direct check: λ(105) = 4). They vanish at every
odd square (Prop 3.1, 4.2).

**Conjecture SQ₅ (CONJECTURE).** For n ≡ 1 (mod 4), n ≠ 105: `λ(n) ≤ 3 ⟺ n is not a square`, where
`λ(n) = min{ r(n/A) : (A/n) = −1 }`. The boundary case is length 2. For n ≡ 5 (8), A = 2 gives λ ≤ 2, and
(n+1)/2 ≡ 3 (4) always has a prime factor ≡ 3 (4). For n ≡ 1 (8), the QNR-in-L₂ criterion of Cor 4.6 holds verbatim
for composite n, because `(b/n) = (−1/b)` for odd b | n+1. SQ₅ is a strengthening, on n ≡ 1 (4) with
n ≠ 105, of O146's CONJECTURE SQ (Type I/II empty ⟺ square): it uses only five explicit slices of Type I/II.
(R169 repair: SQ₅ says nothing at n = 105, where SQ must be checked separately.) It implies ES for all
primes p ≡ 1 (4).

**9.2 Composite case with a factor ≡ 3 (4): reduction, not proof (PROVED lemma).** Let `n = am ≡ 1 (4)` with
a ≡ 3 (4), so m ≡ 3 (4). If `m + 1` has a divisor `A ≡ −1 (mod a)`, `A ≥ 2a − 1`, with `(2/m)^{v₂(A)} = 1`, then
`[[a(m+1)/A, (A+1)/a, a]]` is a certificate for n. (Use 8.3 with u' = 1. For A | m+1, A = 2^k A', reciprocity
gives `(A'/m) = 1`, so `(A/m) = (2/m)^k`.) Special family: `a | m + 2` gives the word `[[a, (m+2)/a, a]]`,
`n = a(at − 2)`; this was checked for q < 200, t < 200 (`dk_scale.py` (b)).
Coverage (`dk_scale.py 200000` (c)): of the 31 143 composite non-square n ≡ 1 (4) ≤ 2·10⁵ that have a divisor ≡ 3 (4),
24 645 (79 %) have a certificate inherited this way (a | u, a | v for some a ≡ 3 (4), a | n).
**Why this is not a proof.** The inherited certificate still needs a divisor of `m + 1` in the class −1 mod a. That
is a B2 divisor event, with the extra freedom of choosing a among the divisors ≡ 3 (4) of n. The bare
existence of the factor gives only the *sign* (8.3), never the *length-3 word*. I see no explicit construction
covering all such n. Polynomial identities in (a, m) of the shapes "t constant, u and v linear in the two
factors" and "u, v constant" are impossible (elementary coefficient comparison, done by hand; general shapes not
excluded).

## 10. Complexity reading and statistics

**10.1 What λ(p) ≤ 3 says (Assessment).** Cor 4.6 is an exact *converse* to the T4 theme
(redteam-automorphic Prop 2.5, Lemma 5.2: every solution exposes a non-residue). On the five slices,
**certificate ⟺ a quadratic non-residue inside the explicit set `L_{≤3}(p)`**, and `|L_{≤3}(p)| ≍ log²p` on average.
* Full ES on the slices only says that this set contains a QNR. Computing `L_{≤3}(p)` needs up to ≍ p factorisations,
  so there is no algorithmic consequence. One can find a QNR in time p^{0.152+o(1)} anyway (Burgess search).
* The **bounded-height** version `t_min(p) ≤ (log p)^C`, where t_min is the least middle entry of a −1 word, would
  give a deterministic algorithm that finds a QNR mod p with `(log p)^C` calls to a factoring oracle (factor
  tp+1 for t ≤ T, and test its O(log p) *prime* factors: a −1 word A | tp+1 has a QNR prime factor — R169 repair,
  since enumerating all divisor words is not polylog). Deterministic polynomial-time QNR finding is a well-known open problem.
  Unconditionally nothing better than `p^{1/(4√e)+o(1)}` search is known; under GRH the least QNR is ≤ 2 log²p
  (Ankeny/Bach; from memory). I know of no result that makes it easier with a factoring oracle (from memory; not
  checked). So a proof of the polylog-height version would be an unconditional derandomisation result of a
  kind not currently available. That is a precise sense in which it is hard. Full ES (unbounded t) carries no
  such complexity implication. Under H, POINTWISE_SIZE Thm C / Cor C1 (R169 repair of the citation "CONDITIONAL_ES Thm C") shows that for
  every fixed T the bound t ≤ T fails i.o. (t_min unbounded) for the
  4|A slice. EVIDENCE: for all primes p ≡ 1 (8) ≤ 10⁶, `t_min(p) ≤ 64` (records 2, 4, 6, 7, 15, 64 at p = 17, 41,
  769, 1049, 2521, 21841; `scripts/dk_tmin.py`).

**10.2 Coin heuristic (EVIDENCE, `dk_sign.py 300000`).** On the 6457 primes p ≡ 1 (8) ≤ 3·10⁵, a fraction
q = 0.695 of all length-3 words are −1. That is well above 1/2, because 15 of the 20 admissible mod-4 classes are
−1. Per prime, `N₋/|L₃|` has mean 0.697, sd 0.107 and minimum 0.19 (|L₃| ≥ 40). The independent-pair model
`P(N₋ = 0) = (1−q)^{|L₃|/2}` predicts 0.67 failures in total, almost all at |L₃| < 8 (3 primes). Observed: 0.
At odd squares N₋ = 0 always, with mean |L₃| = 34. So at primes the signs look like biased coins (≈ 70 % −1),
while at squares they are all forced to +1. The model is consistent with SQ₅ holding beyond a small range,
and with the single exception 105.
