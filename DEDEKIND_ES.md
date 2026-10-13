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
itself**; "r = 3" is the condition that the *odd-indexed* regular partial quotients of n/A are all 1 except in
the pattern `[v−1; 1, t−2, 1, u−1]` (entries 2 in [[·]] merge into the 1-strings).

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
p ≡ 3 (4), and equidistributed (≈ 50:50) on the other residue classes of (A, t) mod 4.

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
`−1 ∈ Σ_e(N)` with `e = v`, `(a,b) = (f,1)`; `4 | v` is its reversal.
*Proof.* By Cor 4.1, `(A/n)` depends only on `(t,u,v) mod 8`. `scripts/dk_cells.py` enumerates all 512 cells: of
those with `n ≡ 1 (4)`, the 120 cells with value −1 are exactly the cells satisfying one of the five conditions,
and the 40 cells with value +1 satisfy none. ∎ (Direct check on data, `scripts/dk_qnr.py`: all
non-square n ≡ 1 (4) ≤ 5000, 0 failures.)

**Corollary 4.6 (a "least non-residue in the Farey metric" form of ES; PROVED).** For a prime p ≡ 1 (mod 8) let
`λ(p) := min{ r(p/A) : (A/p) = −1 }` (the HJ length is the number of left turns of the positive Farey path from ∞
to p/A). Then `λ(p) ≥ 2` (L₁ = {1}), and
* `λ(p) = 2` ⟺ some divisor b of p+1 is a QNR ⟺ (p+1)/2 has a prime factor ≡ 3 (4) (since `(b/p) = (−1/b)` for
  odd b | p+1, and (2/p) = 1). This is exactly the boundary certificate of 4.2.
* `λ(p) = 3` ⟹ an interior X/e-slice certificate (Thm 4.5).
So **the five X/e-slices of ES(p) together hold ⟺ λ(p) ≤ 3**: *some quadratic non-residue mod p is reached
from ∞ by at most three left turns in the Farey graph.* At n = m² there are no non-residues (Jacobi), which is
the T1 obstruction in its barest form. EVIDENCE: λ(p) ∈ {2, 3} for all 556 primes p ≡ 1 (8), p ≤ 2·10⁴
(395 with λ = 2, 161 with λ = 3; `dk_qnr.py 20000`).

*Reading.* The classical least quadratic non-residue `n_p` measures non-residues in the archimedean order. The
Burgess bound is `n_p ≪ p^{0.152}`, and n_p ≪ log²p under GRH. λ(p) measures them in the Farey/HJ word metric
centred at ∞. In that metric the ball of radius 3 is the sparse set `L_{≤3}(p)`, of expected size ≍ log²p, and the
conjecture λ(p) ≤ 3 is ES on five slices. Every Jacobi value on the ball is a mod-8 polynomial in the letters
(Cor 4.1), so "the ball contains a non-residue" is literally "the cubic `tuv − u − v = p` has a solution in one of
120 residue cells mod 8". This dictionary is exact but is not by itself a route (B1/B2).
