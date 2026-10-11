# Long shot A: a deterministic pigeonhole ("highly composite slices") mechanism for pointwise ES (task O135)

Status labels as in DISCOVERIES.md. **ES is not proved here, nor any new case of it.** Work in progress;
§0 is filled in at the checkpoint.

## 0. Summary (checkpoint 1)

**ES is not proved, nor any new case of it.** Outcome: a PROVED negative result with exact scope, a precise
reduction of the "highly composite slice" idea, and EVIDENCE.
* **Exact covering problem (§1; PROVED).** The single coordinate e parametrises all solutions: ES(p) ⟺ for some
  e, −1 lies in the *signed* divisor-ratio set `Σ_e(N) = {ab⁻¹ mod e : ab | N}`, `N = (p+e)/4` (Type II, consecutive
  integers above p/4) or `(pe+1)/4` (Type I) (Lemma 1.1). The target lies in the non-trivial coset of the genus
  subgroup `K_e = ker χ_{−e}`, and each prime factor ℓ of N sits in K_e or −K_e according to `(ℓ/p)` (Lemma 1.2;
  this is the odd-square step T1 and the n_p phenomenon T4).
* **Pigeonhole proper gives the wrong sign** (Lemma 1.3): collisions/zero-sums produce *signed* solutions
  `4/p = 1/x − 1/y + 1/z`. Positivity is a covering-of-a-translate statement.
* **Covering thresholds (§1.4–1.5).** Counting: `τ(N²) ≥ |target|`. Structure-only (Kneser) criteria: linear in the
  index, and sharp (Prop 1.4). The brief's `≈ log₃ q` needs the actual residues of the prime factors.
* **Supply (§2).** CRT forcing costs `e^{(1+o(1))k log k}` against `3^{k+1}` (Lemma 2.1 — the brief's estimate,
  confirmed); every certificate has `e ≤ p^{o(1)}` (Lemma 2.3); large Ω comes from prime powers, which count
  linearly. **Theorem 2.2 (PROVED, rel. PNT in APs, Brun–Titchmarsh, Shiu, Nicolas–Robin):** covering certificates
  built from the prime factors *below the modulus* plus one opaque cofactor, covering a coset of size
  `≥ φ(e)e^{−θ}/2` with θ < 1/2 (R135 repair: the size restriction was missing here; R135 remark after Thm 2.2
  extends it to every θ < 1), have bounded mass and **fail for a
  positive proportion of primes, in every e-slice of both types**. The remaining (non-transparent) part is the
  residue distribution of large prime factors of specific integers — the lottery (H-A/H-B), untouched here.
* **Numerics (§3; EVIDENCE).** Validated engine. Full-coset covers exist at every sampled prime ≥ 10⁶ (largest
  covered |−K_e| up to 2339), the deep covers are almost always transparent, covers are a ≈ 5 % minority of
  solution slices at e ≥ 500 (10⁸), and the transparent counts are still pre-asymptotic at 10⁸ (Theorem 2.2's
  failure set is not observable numerically).
* **Conjecture PH (§5)** (full-coset cover in some e-slice for all large p) is consistent with the data but, by
  Theorem 2.2, needs the lottery input on a positive-density set.
* **T1–T8 (§4):** passes T1/T4/T8 by construction; the deterministic part dies by Thm 2.2, the rest is T2/T7 lottery.

## 1. The covering problem, made exact

### 1.1 The e-slices: one coordinate, signed products

Recall (red team 2 §2.0) `V_I(p) = {4abd = pe+1, a+b = ce}`, `V_II(p) = {4abd = p+e, a+b = ce}`, and
ES(p) ⟺ `V_I(p) ∪ V_II(p) ≠ ∅`. For a fixed value of the single coordinate e put

```
N_e^II(p) := (p+e)/4,   N_e^I(p) := (pe+1)/4      (integers iff e ≡ −p (mod 4)).
```

For an integer N and a modulus e with gcd(N,e) = 1 define the **signed divisor-ratio set**

```
Σ_e(N) := { a·b⁻¹ mod e : a, b ≥ 1, ab | N }  ⊂  G_e := (ℤ/e)*.
```

**Lemma 1.1 (e-slice; PROVED, elementary).** Let p be an odd prime, e ≥ 1, e ≡ −p (mod 4), p ∤ e.
(i) gcd(N_e^I, e) = gcd(N_e^II, e) = 1.
(ii) The Type T fibre `{(a,b,c,d) : (a,b,c,d,e) ∈ V_T(p)}` (T ∈ {I, II}) is in bijection with
`{(a,b) : a,b ≥ 1, ab | N_e^T, e | a+b}` via `d = N/(ab)`, `c = (a+b)/e`.
(iii) Hence the fibre is non-empty iff `−1 ∈ Σ_e(N_e^T)`.
(iv) `Σ_e(N) = ∏_{ℓ^v ∥ N} {ℓ^t : |t| ≤ v}` (product set in G_e). In particular `|Σ_e(N)| ≤ τ(N²)`.

*Proof.* (i) `4N^I = pe+1 ≡ 1 (e)`; `4N^II = p+e ≡ p (e)` and p ∤ e, p prime. As e is odd, gcd(N,e) = 1.
(ii) `4abd = 4N` and `a+b = ce` are the defining equations. (iii) By (i) every a, b | N is a unit mod e, and
`e | a+b ⟺ ab⁻¹ ≡ −1 (e)`. (iv) Write `a = ∏ℓ^{α_ℓ}`, `b = ∏ℓ^{β_ℓ}`; `ab | N` iff `α_ℓ+β_ℓ ≤ v_ℓ`; the ratio is
`∏ℓ^{α_ℓ−β_ℓ}` and every `t = α−β ∈ [−v,v]` occurs (α = max(t,0), β = max(−t,0)). ∎

Remarks. (1) For p ≡ 1 (mod 4) the admissible e are e ≡ 3 (mod 4), e ≥ 3; every element of V(p) lies in exactly
one e-slice, so **the e-slices are a complete one-parameter parametrisation** of ES(p). (The case p | e is empty
for Type II (red team 2 Lemma 2.1 proof) and impossible for Type I since `p | 4abd = pe+1` is false.)
(2) The {a,e} and {d,e} rows of the slice table are sub-slices of Lemma 1.1. The two-coordinate rows {c,d}, {a,c},
{a,d} have plain (unsigned) divisor conditions: e.g. Type I {c,d}: `−p ∈ D_{4cd}(p²+4c²d)` where
`D_q(N) := {f mod q : f | N}` (red team 2 Lemma 2.1).
(3) Type II e-slice in words: N runs over the **consecutive integers** just above p/4 (`e = 4N − p`), and one asks
for a, b with `ab | N`, `a ≡ −b (mod 4N − p)`. Type I: N runs over the progression `(pe+1)/4`.

### 1.2 The genus subgroup and the sign

For e ≡ 3 (mod 4), `−e ≡ 1 (mod 4)` is a (possibly non-fundamental) discriminant; its Kronecker character
`χ_{−e} = (−e/·)` is a character of `G_e` with `χ_{−e}(−1) = −1`. Put `K_e := ker χ_{−e}` (index 2, `−1 ∉ K_e`).

**Lemma 1.2 (genus; PROVED).** Let p ≡ 1 (mod 4) be prime, e ≡ 3 (mod 4), p ∤ e, T ∈ {I, II}, N = N_e^T(p).
(i) Every prime ℓ | N satisfies `χ_{−e}(ℓ) = (ℓ/p)`.
(ii) `χ_{−e}(N^I) = 1` and `χ_{−e}(N^II) = (e/p)`.
(iii) Consequently `a b⁻¹ ≡ −1 (e)` with `ab | N` forces `ab` to have a prime factor ℓ with `(ℓ/p) = −1`; the
odd-square case: if p is replaced by an odd square n = m² with gcd(m, e) = 1, then `Σ_e(N) ⊂ K_e ∌ −1`
(ET Prop 1.6 for these slices).

*Proof.* (i) ℓ odd: Type II gives `−e ≡ p (ℓ)`, Type I gives `−e ≡ p⁻¹ (ℓ)`; in both cases `(−e/ℓ) = (p/ℓ) = (ℓ/p)`
(reciprocity, p ≡ 1 (4)). ℓ = 2: `2 | N` means `8 | p+e` (resp. `8 | pe+1`), so `−e ≡ p` (resp. `p⁻¹ ≡ p`) mod 8,
and the Kronecker symbol at 2 depends only on the residue mod 8: `(−e/2) = (p/2) = (2/p)`.
(ii) Multiply (i) over ℓ^v ∥ N: `χ_{−e}(N) = (N/p)` (Jacobi). `4N^I ≡ 1`, `4N^II ≡ e (mod p)`.
(iii) `χ_{−e}(ab⁻¹) = −1` and (i). At n = m² every `(ℓ/n) = 1` for ℓ ∤ m, and ℓ | m, ℓ | N would give ℓ | e. ∎

*Reading.* The target −1 lies in the **non-trivial coset** `−K_e`; prime factors of N with `(ℓ/p) = 1` stay in K_e.
So a solution needs a "p-non-residue" prime factor of N — this is POINTWISE red team 1 Prop 2.5 (every solution
sees a non-residue `ℓ ≥ n_p`) seen inside one slice, and it is the step that fails at odd squares (T1).
For Type II with `(e/p) = −1` the product of all prime factors lies in `−K_e`, so non-residue factors exist
automatically; for Type I and for `(e/p) = +1` their number is even and may be 0.

### 1.3 Pure pigeonhole gives the wrong sign

**Lemma 1.3 (zero-sums are signed solutions; PROVED).** In the setting of Lemma 1.1, if `2^{ω(N)} > φ(e)`
there are a ≠ b with `ab | N`, `gcd(a,b) = 1`, `a ≡ b (mod e)`, and then with `c = |a−b|/e`, `d = N/(ab)`:
Type II: `4/p = 1/(abd) − 1/(acdp) + 1/(bcdp)` (a > b); Type I: `4/p = 1/(abdp) − 1/(acd) + 1/(bcd)` (a > b).

*Proof.* The `2^{ω(N)}` unitary divisors u of N have products `u` mod e in G_e; two coincide, `u ≡ u'`. Put
`g = gcd(u,u')`, `a = u/g`, `b = u'/g`: coprime, `ab | N`, `a ≡ b`. The identities: Type II
`(cp − b + a)/(abcdp) = c(p+e)/(abcdp) = 4/p` (using `a − b = ce`, `4abd = p+e`); Type I
`(c + p(a−b))/(abcdp) = c(1+pe)/(abcdp) = 4/p`. ∎

So the classical pigeonhole (collision ⇒ zero-sum, Davenport-constant type) always lands on target **1 ∈ K_e**,
i.e. on *signed* ES solutions, which exist trivially. Positivity is exactly the requirement to hit the
non-trivial coset `−K_e` (Lemma 1.2), i.e. a **covering/translate** statement, not a collision statement.
Zero-sum theory (Davenport, Olson, Erdős–Ginzburg–Ziv) is therefore not directly applicable; one needs
covering theorems for a prescribed target.

### 1.4 A deterministic covering criterion (Kneser) and its sharpness

Let G be a finite abelian group (written multiplicatively), `g_1,…,g_k ∈ G`, `v_i ≥ 1`,
`A_i := {g_i^t : |t| ≤ v_i}`, `Σ := A_1⋯A_k`, and a target `t_0 ∈ G`. For a subgroup H write `o_H(g)` for the order
of gH in G/H. (For the e-slice: G = G_e, g_i the prime factors ℓ of N, v_i = v_ℓ(N), Σ = Σ_e(N), t_0 = −1.)

Cited input (Kn): **Kneser's theorem** (M. Kneser, Math. Z. 58 (1953) 459–484; finite form as in Tao–Vu,
*Additive Combinatorics*, CUP 2006, Thm 5.5): for finite non-empty A, B ⊂ G with `H = Stab(AB)`,
`|AB| ≥ |AH| + |BH| − |H|`.

**Proposition 1.4 (covering criterion; PROVED from (Kn)).** If `t_0 ∉ Σ`, there is a subgroup `H ≤ G` with
`t_0 ∉ H` and
```
1 + Σ_i ( min(2v_i+1, o_H(g_i)) − 1 )  ≤  |G:H| − 1 .
```
Equivalently: if for every subgroup H with `t_0 ∉ H` one has `Σ_i (min(2v_i+1, o_H(g_i)) − 1) ≥ |G:H| − 1`, then
`t_0 ∈ Σ`.

*Proof.* Let `H = Stab(Σ)`. Since 1 ∈ A_i, 1 ∈ Σ and H ⊂ Σ; so t_0 ∉ Σ gives t_0 ∉ H and `t_0H ∩ Σ = ∅`, whence
`|Σ/H| ≤ |G:H| − 1`. In G/H let X_i be the image of A_i; `Σ/H = X_1⋯X_k` has trivial stabiliser, and so does every
partial product `X_1⋯X_j` (a stabiliser of a partial product stabilises the full product). Kneser with trivial
stabiliser gives `|X_1⋯X_j| ≥ |X_1⋯X_{j−1}| + |X_j| − 1`, so `|Σ/H| ≥ 1 + Σ_i(|X_i| − 1)`, and
`|X_i| = #{g_i^t H : |t| ≤ v_i} = min(2v_i+1, o_H(g_i))`. ∎

*Checks.* (a) H = K_e (index 2, −1 ∉ K_e) in the e-slice: the condition reads "some prime factor ℓ ∉ K_e", i.e. the
genus condition of Lemma 1.2 — necessary and, for G = G_3 = {±1}, also sufficient. (b) H = {1} is always admissible
(e ≥ 3): one needs `Σ_i (min(2v_i+1, ord g_i) − 1) ≥ φ(e) − 1`, so in particular `Ω(N) ≥ (φ(e) − 1)/2`.
(c) *Sharpness.* G = ℤ/2m (additive), all g_i = 1, v_i = 1, t_0 = m: Σ = [−k, k] ∋ m iff k ≥ m, and the criterion
at H = 0 reads `2k ≥ 2m − 1`, i.e. k ≥ m. So no criterion that uses only the multiset of images of the g_i in the
quotients G/H (orders and counts) can do better than linear in |G:H|: the example has all images "in general
position" in this sense (each g_i generates G) yet needs k ≍ |G|.

### 1.5 How many prime factors? The three regimes (exact statements and their status)

Fix the e-slice, G = G_e, |G| = φ(e), target −1 ∈ −K_e, `k := ω(N)`, `Ω := Ω(N)`.
* **Counting (PROVED, trivial).** `|Σ_e(N)| ≤ τ(N²) ≤ 3^Ω`. A *pigeonhole* (p-blind) certificate — one proving
  `Σ_e(N) ⊇ −K_e` from structural data rather than locating −1 — needs `τ(N²) ≥ φ(e)/2`, so `Ω ≥ log₃(φ(e)/2)`.
* **Deterministic, structure-only (PROVED, Prop 1.4; sharp by 1.4(c)).** Hypotheses on the residues of the prime
  factors that are invariant under "re-labelling within each subgroup quotient" (orders, counts outside
  subgroups) guarantee −1 ∈ Σ only when `Σ_i(min(2v_i+1, o_H(g_i)) − 1) ≥ |G:H| − 1` for all H ∌ −1, in
  particular `Ω ≳ φ(e)/2`: **linear** in the modulus.
* **Generic/random residues (heuristic; not cited as a theorem).** If the g_i were independent uniform in −K_e ∪ K_e
  (with at least one in −K_e), the signed sums cover G once `3^k ≳ φ(e) log φ(e)` (coupon-collector heuristic; the
  classical random-subset-product results go back to Erdős–Rényi, J. Analyse Math. 14 (1965) 127–138 — exact
  threshold statement there UNVERIFIED by our citation check). This is the brief's "≈ log₃ q".
Between log and linear there is no structure-only guarantee: the gap is bridged only by a *dissociativity /
general-position* property of the actual residues `ℓ mod e`, i.e. by knowing where specific large primes fall
mod e. For distinct residues in groups of prime order there is an intermediate quadratic regime (Balandraud,
Israel J. Math. 188 (2012) 405–429, Thm 5: `A ⊂ ℤ/p`, `A ∩ (−A) = ∅` ⇒ `|Σ(A)| ≥ min(p, 1 + |A|(|A|+1)/2)`), but
`G_e` has even order φ(e), so it does not apply verbatim.
For the two-coordinate rows the same three regimes hold with plain divisor sets (`|D_q(N)| ≤ τ(N)`, 2^k instead
of 3^k, Kneser with `A_i = {1, g_i, …, g_i^{v_i}}`).

## 2. Supply: where could the many prime factors come from?

### 2.1 Forcing by congruences costs the modulus (the brief's estimate, made exact)

In the e-slice, `ℓ | N_e^II(p)` iff `e ≡ −p (mod 4ℓ)` and `ℓ | N_e^I(p)` iff `e ≡ −p⁻¹ (mod 4ℓ)` (ℓ odd, ℓ ≠ p).
Forcing a set S of k odd primes, `L = ∏S`, therefore puts e in one class mod 4L, whose least positive member
`e_0(p) = (−p mod 4L)` (resp. `−p⁻¹`) is equidistributed in [1, 4L) as p varies.
In each two-coordinate D row the same holds with e replaced by one of the coordinates (c, d or a), each of which
divides `q_θ/4`, so `q_θ ≥ 4·(forced coordinate)`.

**Lemma 2.1 (CRT forcing; PROVED).** Let S be k distinct odd primes, L = ∏S, and suppose the only factorisation
data used at (p, e) are: the primes of S (with exponent 1) and the opaque cofactor M = N/L. If the resulting
residue set `R = Σ_e(L)·{M⁻¹, 1, M}` contains a coset `gH` of a subgroup of index ≤ I, then
`3^{k+1} ≥ φ(e)/I`. If moreover `e ≥ εL` ("honest forcing"), then `3^{k+1} ≥ c ε L/(I log log L)`, which fails
for `k ≥ k_0(ε, I)`, since `L ≥ ∏_{i≤k} p_{i+1} = e^{(1+o(1))k log k}`.

*Proof.* `|R| ≤ 3·3^k`, `|gH| ≥ φ(e)/I`, `φ(e) ≫ e/log log e`. ∎

So the brief's estimate is right in this exact sense: `e^{k log k}` (forcing cost) against `3^k` (signed covering;
`2^k` in the plain two-coordinate rows) — the loss is the factor log k in the exponent. Honest forcing is a
bounded procedure for each k ≤ k_0, so it lands in POINTWISE_SIZE Thm C (finitely many slices, refuted i.o. under H;
red team 2 Thm 2.2(iii)). The remaining freedom is **adaptive** choice of S and e ("luck": e small *and*
`N_e` divisible by many small primes). Theorem 2.2 shows that this freedom is also insufficient, for a positive
proportion of primes, as long as the covering primes are below the modulus.

### 2.2 Transparent pigeonhole fails for a positive proportion of primes

**Definition.** Let p ≡ 1 (4), e ≡ 3 (4), T ∈ {I, II}, N = N_e^T(p). The *transparent part* of N is
`L := ∏_{ℓ^v ∥ N, ℓ < e} ℓ^v` (the prime factors below the modulus, whose residues mod e are just themselves),
`M := N/L`, and the transparent residue set is `R := Σ_e(L)·{M⁻¹, 1, M}` (all prime powers below the modulus
used with their full exponent range, and the rest of N as one opaque block). For `0 ≤ θ < 1/2`, a
*transparent covering certificate of strength θ* (TCC_θ) at (p, e, T) is a subgroup `H ≤ G_e` with
`|G_e : H| ≤ 2e^θ` (R135 repair: was `≤ e^θ`, which at θ = 0 excludes H = K_e) and `−H ⊂ R`. (θ = 0 with H = K_e is "R covers the whole target coset −K_e"; −H ⊂ R with
−1 ∈ −H gives an ES solution. TCC_θ is the most a p-blind covering argument can extract from the primes below the
modulus.)

**Theorem 2.2 (PROVED, relative to PNT in progressions to a fixed modulus, Brun–Titchmarsh (Montgomery–Vaughan,
Mathematika 20 (1973) 119–134), Shiu's theorem (J. reine angew. Math. 313 (1980) 161–170, Thm 1) and the
Nicolas–Robin bound `log τ(n) ≤ 1.5379 log 2 · log n/log log n`).** Fix `0 ≤ θ < 1/2` and ε > 0. There is
`C = C(θ, ε)` such that for every `Y ≥ 3`, with `q_0 := 8∏_{3≤ℓ≤Y} ℓ`,
```
#{p ≤ x prime : p ≡ 1 (mod q_0), TCC_θ exists at some (e, T)}  ≤  (C·Y^{−1+2θ+ε} + o_{x→∞}(1)) · π(x; q_0, 1).
```
Here e ranges over **all** e ≡ 3 (mod 4) and T over {I, II}. Consequently, for Y large, a set of primes of lower
relative density `≥ (1 − 2C·Y^{−1+2θ+ε})/φ(q_0) > 0` has no transparent covering certificate in any e-slice.

*Proof.* Fix p ≡ 1 (q_0), p ≤ x. A TCC_θ forces `|R| ≥ |H| ≥ φ(e)e^{−θ}/2` (R135 repair), hence (Lemma 1.1(iv))
`τ(L²) ≥ φ(e)e^{−θ}/6 =: B_e` (R135 repair: /6 instead of /3 after the index bound 2e^θ; all constants below
change by bounded factors only). Split the e-range.

*(a) e ≤ Y: no certificate at all.* Every prime ℓ < e ≤ Y satisfies `(ℓ/p) = 1` (p ≡ 1 mod 8ℓ), so by
Lemma 1.2(i) `L ∈ K_e`. By Lemma 1.2(ii) `χ_{−e}(N) ∈ {1, (e/p)}` and `(e/p) = 1` because every prime factor of
e is ≤ Y. So `χ_{−e}(M) = 1` and `R ⊂ K_e`, which misses `−K_e ∋ −1`: not even a transparent *witness* exists.

*(b) Y < e ≤ E_1 := exp((log x)^{1/3}).* (b1) If `L > x^{1/2}`: all prime factors of L are `< e < x^{1/4}`, so
multiplying them one at a time yields `u | N` with `x^{1/4} < u ≤ x^{1/2}`, `P⁺(u) < E_1`. The condition `u | N` puts
p in one class mod 4u (`4u | p+e`, resp. `4u | pe+1`, gcd(u, e) = 1), so by Brun–Titchmarsh the number of such
p is `≤ 2x/(φ(4u) log(x^{1/2}/4)) ≤ 5x/(φ(u) log x)`. By Rankin with `σ = 1/log E_1`,
`Σ_{u > x^{1/4}, P⁺(u) < E_1} 1/φ(u) ≤ x^{−σ/4} ∏_{ℓ<E_1}(1 + Σ_v ℓ^{vσ}/φ(ℓ^v)) ≪ e^{−(log x)^{2/3}/4}(log x)^{O(1)}`.
Summing over the ≤ 2E_1 pairs (e, T) gives `o(x/(φ(q_0) log x))`.
(b2) If `L ≤ x^{1/2}`: let `f(n) = τ(n²)²` and `h = f * μ`, so `h ≥ 0` multiplicative, `h(ℓ^v) = 8v`. Then
`1 ≤ B_e^{−2} τ(L²)² = B_e^{−2} Σ_{m | L} h(m)` with every such m `≤ x^{1/2}`, `P⁺(m) < e`, `m | N`. The condition
`m | N` puts p in one class b mod 4m; with p ≡ 1 (q_0) it is consistent only if `b ≡ 1 (mod g)`,
`g := gcd(4m, q_0)`, which (both types) forces every odd prime ℓ ≤ Y dividing m to divide `e+1`; then p lies in
one class mod `lcm(4m, q_0) ≤ x^{2/3}`, and Brun–Titchmarsh gives `≤ 6x φ(g)/(φ(q_0)φ(4m) log x)`. Writing m = m_1 m_2
(m_1 supported on primes ≤ Y, m_2 on (Y, e)),
```
Σ_m h(m) φ(g)/φ(4m) ≤ [Σ_{j≥0} 8j·2^{−max(j−1,0)} + 1] · ∏_{ℓ | e+1, 3≤ℓ≤Y} (1 + 8/(1−1/ℓ)²) · ∏_{Y<ℓ<e}(1 + 8ℓ²/(ℓ−1)³)
                    ≤ 33 · 19^{ω(e+1)} · C_0 (log e)^8 .
```
Hence the (b2) count is `≤ (C_1 x/(φ(q_0) log x)) Σ_{e>Y} 19^{ω(e+1)}(log e)^8 B_e^{−2}`, and
`B_e^{−2} ≪ e^{2θ−2}(log log e)²`, `19^{ω(n)} ≪_ε n^{ε/2}`; the sum is `≪ Y^{−1+2θ+ε}`. The constant does not
depend on Y. PNT in progressions gives `π(x; q_0, 1) ≥ x/(2φ(q_0) log x)` for x ≥ x_0(Y).

*(c) E_1 < e ≤ x.* Markov with `τ(L²) ≤ τ(N²)`: the count is `≤ B_e^{−2} Σ_{p ≤ x} f(N_e^T(p))`. p ↦ N is
injective. Type II: N ≤ x/2, so `≤ B_e^{−2} Σ_{n ≤ x/2} f(n) ≪ B_e^{−2} x(log x)^8` (`f = 1*h`,
`Σ_{n≤X} f ≤ X Σ_{d≤X} h(d)/d`). Type I: N lies in the progression `n ≡ 4⁻¹ (mod e)`, `n ≤ xe/4`; Shiu's theorem
(f(ℓ^v) = (2v+1)² ≤ 9^v; Shiu needs modulus `k < y^{1−α}`, here y = X = (xe+1)/4, α = 1/4, and `e < X^{3/4}` holds
for all e ≤ x — R135 repair: the earlier check `e ≤ (xe/4)^{1/2}` fails for e > x/4) gives `≪ (xe/φ(e))(log x)^8`. Summing,
`Σ_{e > E_1} B_e^{−2}·e/φ(e) ≪ E_1^{−1+2θ+ε}`, which beats every power of log x: `o(x/(φ(q_0) log x))`.

*(d) e > x.* Then N ≤ e²/4 (both types), and by Nicolas–Robin `τ(N²) ≤ τ(N)² ≤ exp(4.3 log e/log log e) < B_e`
for e ≥ e_0(θ); take x_0 ≥ e_0. No certificate. ∎

*Remark (R135 repair/extension; reviewer derivation, see reviews/longshot-pigeonhole-review.md D6).* The restriction
θ < 1/2 comes only from using the second moment. With `f_r = τ(·²)^r`, r > 1/(1−θ): `h_r = f_r * μ ≥ 0`,
`h_r(ℓ^v) = (2v+1)^r − (2v−1)^r ≪_r v^{r−1}`, so the 2-part and small-prime factors in (b2) are constants c_r
(`c_r^{ω(e+1)} ≪ e^ε`), the product over Y < ℓ < e is `≪ (log e)^{3^r−1}`, Markov gives `B_e^{−r} ≪ e^{−r(1−θ)+ε}` (tail
`≪ Y^{1−r(1−θ)+ε}`); (b1) is unchanged; (c) uses Shiu with `f_r(ℓ^v) ≤ (3^r)^v`; (d) holds for every θ < 1. So Theorem 2.2
holds for every fixed θ < 1 (with `C·Y^{1−r(1−θ)+ε}` in place of `C·Y^{−1+2θ+ε}`): for every δ > 0, transparent
certificates covering a coset of size ≥ e^δ fail on a positive-density set. Single witnesses (H = {1}) remain outside.

*Reading.* Every ES solution lies in some e-slice (Lemma 1.1). Theorem 2.2 says that **a covering argument that only
uses prime factors smaller than the modulus (plus one opaque cofactor) to cover a coset of size `≥ e^{1−θ}`, θ < 1/2
(R135 repair: size restriction added; arguments that only hit −1 or cover smaller cosets are not excluded),
cannot prove ES, not even for almost all
primes**: it fails on a set of positive density, uniformly over all e and both types. The mechanism is exactly the
brief's: the transparent prime factors of N_e behave like the small prime factors of a random integer, whose
`τ(·²)`-moment is `(log e)^{8}`, while a coset-covering needs `τ(L²) ≥ e^{1−θ−o(1)}`; the expected number of
certificates over all e is majorised by a convergent series `Σ_e (log e)^8 e^{2θ−2}`, **independent of p**. So transparent
covering is a *bounded-mass* mechanism, whereas ES solutions have mass `≍ (log p)³`. This is a stronger form of the
"log log loss" in the brief: it is not a near miss, the mass is O(1).

### 2.3 The modulus ceiling, and why large-deviation supply is degenerate

**Lemma 2.3 (modulus ceiling; PROVED).** If a coset `gH` with `|G_e:H| ≤ e^θ` (θ < 1/2) is contained in
`Σ_e(N_e^T(p))` (any covering certificate, transparent or not), then `e ≤ exp((C_θ + o(1)) log p/log log p)`.
*Proof.* `τ(N²) ≥ φ(e)e^{−θ}`; `N ≤ max(p, e)²`; `log τ(N²) ≤ 2 log τ(N) ≤ 2.14 log N/log log N` (Nicolas–Robin). If
e ≥ p then `e^{1−θ−o(1)} ≤ exp(4.3 log e/log log e)`, false for large e; so e < p and
`(1−θ−o(1)) log e ≤ 4.3 log p/log log p`. ∎

So every pigeonhole certificate lives in a family of length `p^{o(1)}`: Type II e-slices are integers
`N ∈ [p/4, p/4 + p^{o(1)}]` — a *specific* very short interval. (Sieve lower bounds need intervals of length `≥ N^δ`;
Matomäki–Radziwiłł-type results hold for almost all short intervals, not a prescribed one. Assessment: no known
technology supplies "an integer with prescribed rich factorisation in [x, x + x^{o(1)}]" pointwise.)

Large deviations do not help either ((i) PROVED, elementary; (ii) Assessment resting on Prop 1.4): (i) many *distinct* primes are capped:
`3^{ω(N)} ≤ N^{(log 3+o(1))/log log N} = p^{o(1)}`; (ii) large `Ω(N)` is achieved mainly through prime *powers*,
and a prime power ℓ^v contributes the progression `{ℓ^t : |t| ≤ v}` inside the cyclic group ⟨ℓ⟩: by Prop 1.4
(H = {1}) such contributions need `Σ_i min(2v_i+1, ord ℓ_i) ≥ φ(e)`, i.e. they count linearly, not
exponentially. The covering-efficient resource is ω (distinct, independent-looking residues), and its supply in a
window of length `p^{o(1)}` is the lottery of §2.4.

### 2.4 Non-transparent primes: the "free generators" are the lottery

The prime factors of N_e above the modulus have residues mod e that are not determined by any bounded data. Their
genus is (Lemma 1.2) `χ_{−e}(ℓ) = (ℓ/p)`, and for Type II with `(e/p) = −1` at least one of them is a p-non-residue
automatically (Lemma 1.2(ii)) — the only "free" structural fact. Beyond that:
* their number is `ω_{>e}(N) ≈ Poisson(log(log N/log e))` for N random (Kubilius model), so they multiply the
  residue-set size by `E[3^{ω_{>e}}] ≈ (log N/log e)²` on average: they turn the bounded transparent mass of
  Theorem 2.2 into a mass growing like a power of log p (Assessment; numerics §3);
* a certificate using them must know `ℓ mod e` for specific large primes ℓ | N_e(p); for p ranging over a class
  mod `∏_{ℓ≤Y}ℓ` these are unconstrained, and Theorem C (POINTWISE_SIZE, under H) already shows that for any
  bounded family of e the large factors can be prime-patterned to fail;
* "general position" of these residues is an equidistribution statement for the prime factors of one specific
  integer in classes mod e — exactly the per-slice divisor-in-class event of red team 2 Thm 2.2, i.e. the lottery
  whose total expectation is polylogarithmic (CONDITIONAL_ES Prop 2.3 scale constraint applies to any lower bound
  for it proportional to a main term).

*Verdict (Assessment).* The covering mechanism splits cleanly: the part that is deterministic (transparent primes,
Kneser/structure criteria) has bounded mass and fails on a positive-density set (Theorem 2.2); the part that has
growing mass is a statement about residues of large prime factors of specific integers, i.e. H-A/H-B again.

## 3. Numerics (EVIDENCE)

Engine `scripts/lsa_census.c` (e-slices e ≤ E, both types; factorisation by trial division + Miller–Rabin/Pollard;
fibre count, full-coset flag P = `Σ_e(N) ⊇ −K_e`, transparent flag TP = `R ⊇ −K_e` with θ = 0). Validation:
total fibre counts equal the brute-force `|V_I(p)|, |V_II(p)|` of `scripts/rt2_slices.py` for all 21 primes
p ≡ 1 (4), p < 200 (E = 2400; Type I needs e up to ≈ 8.5p); P/TP/fibre flags re-derived independently
(`scripts/lsa_check_cover.py`: Σ built from divisor pairs, −K_e from Jacobi symbols) on 13000 + 2000 slices,
0 mismatches. Runs: `scripts/lsa_run.sh` (≈ 70 s), tables `scripts/lsa_tables.sh` → `logs/lsa_tables.txt`.
Primes: all 2370 Mordell-hard primes (p mod 840 ∈ {1,121,169,289,361,529}) below 10⁶ (E = 2000); 300 consecutive
Mordell-hard primes after 10^k, k = 4..8 (E = 5000; the 10⁴ and 10⁵ samples overlap); 15 hard primes (minimal f_I
in their dyadic range ≤ 2²⁶ from `data/spec/t1e8_stats.txt`, 5101441, and the S(p) = 1 primes of
`data/cond/scan_hard_1e7.txt`) with E = 20000.

**Table 3.1 (per prime, means; P20/TP20 = number of P/TP slices with `|−K_e| = φ(e)/2 ≥ 20`).**

| sample | solution slices | P | TP | P20 | TP20 | #p with P20 = 0 | largest covered `φ(e)/2`: mean / min | max ω(N_e) |
|---|---|---|---|---|---|---|---|---|
| MH ≤ 10⁶ (E=2000) | 43.5 | 14.0 | 10.1 | 7.3 | 6.8 | 2 (3529, 110881) | 238 / 12 | 6.5 |
| 10⁴ | 36.1 | 10.8 | 8.0 | 4.9 | 4.7 | 1 (110881) | 159 / 12 | 6.6 |
| 10⁶ | 61.3 | 16.0 | 11.4 | 8.8 | 8.1 | 0 | 319 / 36 | 7.1 |
| 10⁷ | 80.2 | 20.1 | 13.5 | 12.0 | 10.3 | 0 | 500 / 60 | 7.3 |
| 10⁸ | 100.6 | 25.2 | 16.0 | 16.1 | 12.7 | 0 | 697 / 95 | 7.6 |
| 15 hard primes (E=20000) | 51.3 | 9.6 | 7.4 | 6.4 | 5.7 | 0 | 242 / 20 | 7.6 |

**Table 3.2 (per prime, first 100 of each sample: solution slices / P / TP by e-range).**

| sample | e < 20 | 20 ≤ e < 100 | 100 ≤ e < 500 | 500 ≤ e < 2000 | 2000 ≤ e < 5000 |
|---|---|---|---|---|---|
| 10⁴ | 3.27/3.10/1.06 | 8.02/4.79/4.33 | 10.12/1.89/1.88 | 6.07/0.13/0.13 | 2.76/0/0 |
| 10⁶ | 4.02/3.82/0.98 | 10.53/6.92/5.38 | 18.24/4.46/4.36 | 17.50/0.60/0.60 | 10.92/0.02/0.02 |
| 10⁸ | 4.61/4.41/0.84 | 13.05/9.43/5.60 | 26.89/8.57/6.91 | 33.13/2.36/2.31 | 23.22/0.27/0.27 |

Readings (EVIDENCE, finite ranges):
1. **Covering vs luck.** For e < 20 almost every solution slice is a full cover (|−K_e| ≤ 9, so "cover" and "hit"
   nearly coincide). For e ≥ 500 covers are rare (≈ 5 % of solution slices at 10⁸, ≈ 1.5–2 % at 10⁴–10⁶): the bulk of
   the growing solution mass at moderate e is *luck* (−1 is hit without the coset being covered).
2. **The deep covers are transparent.** The largest covered coset per prime is attained by a transparent
   certificate for 2358/2370 primes ≤ 10⁶ and ≥ 297/300 in every sample; for e ≥ 100, P ≈ TP in every bin. Large
   prime factors ("free generators") add covers almost only at e < 100. This is the regime of Theorem 2.2.
3. **Transparent counts still grow at p ≤ 10⁸** (TP 8 → 16 per prime), although Theorem 2.2 says the limit is
   bounded: truncation (`L ≤ N_e`, and a cover at modulus e needs `L ≳ e^{log₃ e}`) has not saturated. The limiting
   model (`scripts/lsa_model_limit.py`: exact p → ∞ law of the transparent part, CRT-independent divisibility)
   gives, for the *necessary* size condition `3τ(L²) ≥ φ(e)/2`, per type: 2.0 (e < 10), 12.6, 41.1, 85.1, 116.6,
   112.5 for the decades up to 10⁶ — a convergent but large series (the Markov bound in Thm 2.2 is far from sharp).
   So Theorem 2.2's positive-density failure set has density far too small to observe below 10⁸. Assessment: the
   theorem is qualitative.
4. **Largest k.** max_e ω(N_e) over e ≤ 5000 is 7–8 at 10⁸ (the largest covered `φ(e)/2` is 2339, `log₃ 2339 ≈ 7.1`): the brief's
   "≈ log₃ q" is what is attained, and it is attained with mostly *small* (transparent) primes.
5. All sampled primes have covers with |−K_e| ≥ 20 except 3529 and 110881; every
   sampled prime ≥ 10⁶ has ≥ 2. This is EVIDENCE for Conjecture 5.1 below, not for a mechanism.

## 4. Collapse tests T1–T8 (red team 1 §4) for the pigeonhole mechanism

* **T1 (odd squares).** The step that fails at n = m² is named: a cover of the target coset `−K_e` needs a prime
  factor outside K_e, i.e. with `(ℓ/n) = −1` (Lemma 1.2(i),(iii)); at odd squares every prime factor of N_e is in
  K_e. Every covering criterion must carry this genus condition (Prop 1.4 at H = K_e). PASS (it is built in).
* **T2 (integrality).** Not a counting route; certificates are witness-producing. But the *mass* of certificates
  matters: transparent covers have bounded mass (Thm 2.2), so they cannot be "always present".
* **T3 (range).** Lemma 2.3: all certificates have `e ≤ p^{o(1)}`. At e ≤ Y every transparent route fails at
  primes p ≡ 1 (mod 8∏_{ℓ≤Y}ℓ) (Thm 2.2(a)) — the n_p phenomenon. No claim below n_p is made.
* **T4 (non-residue).** χ_p enters exactly through `χ_{−e}(ℓ) = (ℓ/p)` (Lemma 1.2(i)); for Type II with
  `(e/p) = −1` a non-residue factor is automatic. PASS.
* **T5 (X5 fibre).** The Type II multiplier of an e-slice solution is `f = 4acd − 1 ≥ 4N/e > p/e`, so W(p) > T
  constrains only e ≳ p/T: X5 does not bind the small-e slices where covers live. (No contradiction, no help.)
* **T6 (covering / sterile points).** Bounded families of e: Thm C under H (red team 2 Thm 2.2(iii)). Transparent
  covers over *all* e: Thm 2.2, unconditional, positive density. At sterile candidates (x**, x̂₉) only the
  non-transparent part can act.
* **T7 (average leak).** Theorem 2.2 averages over p, legitimately (it is a negative statement). A positive use of
  "general position of the residues of large prime factors" proved on average over p would be a T7 leak.
* **T8 (lifting).** Exact: Lemma 1.1 is a bijection between the e-fibres of V_T(p) and the (a,b)-pairs (validated
  numerically against brute force). (R135 repair: the map V_T(p) → solutions is surjective but not injective —
  dilation `(a,b,c,d) ↦ (λa,λb,λc,λ⁻²d)`, ET Prop 2.2; it is a bijection once gcd(a,b) = 1 is imposed, checked for
  p < 110 in `scripts/review_r135_slices.py`. No proof here is affected.)
Verdict: the mechanism survives T1/T4/T8 by construction; its deterministic part is killed by Thm 2.2, and its
remaining part is the lottery (T2/T7).

## 5. What is proved, what is conjectured, and the exact scope of the negative result

**Theorem 5.0 (the deterministic pigeonhole mechanism cannot prove ES; PROVED, assembled from §§1–2).**
(i) *Exact covering problem.* ES(p) (p ≡ 1 mod 4) holds iff for some e ≡ 3 (mod 4) the signed divisor-ratio set
`Σ_e(N_e^T(p))` contains −1 (Lemma 1.1); −1 lies in the non-trivial coset of the genus subgroup K_e = ker χ_{−e},
and prime factors fall into K_e or −K_e according to `(ℓ/p)` (Lemma 1.2).
(ii) *Pigeonhole proper* (collisions, zero-sum theory) produces only target 1, i.e. signed solutions (Lemma 1.3).
(iii) *Covering criteria.* Counting needs `τ(N²) ≥ |target set|`; structure-only criteria (Kneser; R135 repair: "structure-only" = depending only on orders/counts of the images in
the quotients G/H — Prop 1.4(c) does not cover criteria using e.g. distinctness of residues) need a number of
prime factors **linear** in |G:H| for every subgroup H ∌ −1, and this is sharp (Prop 1.4). Exponential efficiency
(`3^ω ≈ φ(e)`) requires knowing the actual residues of the prime factors.
(iv) *Forcing.* CRT-forcing of k primes costs `e ≥ e^{(1+o(1))k log k}` against `3^{k+1}` residues (Lemma 2.1);
every covering certificate has `e ≤ p^{o(1)}` (Lemma 2.3).
(v) *Transparent covering fails on a positive-density set.* For every θ < 1/2, a positive proportion of primes
admits no certificate covering a coset of index ≤ e^θ in any e-slice (any e, both types) from the prime factors
below the modulus plus one opaque cofactor (Theorem 2.2; inputs: PNT in APs to a fixed modulus, Brun–Titchmarsh,
Shiu, Nicolas–Robin).
*Scope.* (v) concerns certificates in the e-slices (which parametrise all solutions) whose residue information
comes from prime factors `< e` and one opaque block. It says nothing about certificates that use the residues of
specific prime factors `> e` of N_e(p); those are the per-slice divisor-in-class events of red team 2 §2, i.e.
the lottery (hatches H-A/H-B), and nothing here excludes them. The two-coordinate rows ({c,d}, {a,c}, {a,d}) have
the same structure with plain divisor sets and modulus `q_θ = 4·(coord)(coord)`; the analogue of Thm 2.2 should
follow by the same proof with a two-parameter sum `Σ_{c,d} (log)^C/(cd)^{2−2θ}` (not written out: Assessment).

**Conjecture 5.1 (PH, full-coset pigeonhole; CONJECTURE).** For every sufficiently large prime p there are
e ≡ −p (mod 4) and T ∈ {I, II} with `φ(e) ≥ 40` and `Σ_e(N_e^T(p)) ⊇ −K_e`.
PH implies ES(p) and is "probability-free" in its conclusion (the whole target coset is hit). EVIDENCE: every
sampled Mordell-hard prime ≥ 10⁶ and every hard prime of §3 satisfies it with e ≤ 5000 (resp. 20000); exceptions
below 10⁶: 3529, 110881. By Theorem 2.2, on a positive-density set any proof of PH must use prime factors above
the modulus, so PH is not easier than the lottery it was meant to replace (Assessment).

**Small explicit instances (PROVED by Prop 1.4; classical in flavour, recorded only as illustrations of "ES on a
non-congruence-defined set").** For p ≡ 1 (mod 4): ES(p) holds if `(p+3)/4` has a prime factor ≡ 2 (mod 3)
(e = 3); or if `(p+7)/4` has a prime factor ≡ 3, 5 or 6 (mod 7) and at least three distinct prime
factors ≢ ±1 (mod 7) (e = 7: subgroups ∌ −1 of G_7 ≅ C_6 are {1} and K_7 = {1,2,4}; Prop 1.4 gives the two
conditions). These are sub-cases of single e-slices; under Hypothesis H each fails for infinitely many p
(Thm C). They are not progress towards ES.

**Answer to the brief's question.** The quick estimate is a theorem in the precise form of Lemma 2.1 (honest
forcing) and, more strongly, Theorem 2.2 (adaptive "lucky" forcing included, as long as the covering primes lie
below the modulus): the loss is not a log log near-miss but a change of regime — the deterministic certificates have
**bounded mass** (a convergent series over e, independent of p), whereas solutions have mass ≍ (log p)³. No slice
decouples the modulus from the forcing cost: in every D row the forced coordinate divides `q_θ/4` (or is e), prime
powers count linearly (Prop 1.4), several slices do not combine (a certificate lives in one slice), and the large
prime factors are the lottery.

## Replay

`sh scripts/lsa_run.sh && sh scripts/lsa_tables.sh` (≈ 2 min, 1 core; data in `data/lsa/`, tables in
`logs/lsa_tables.txt`); `uv run python scripts/lsa_check_cover.py 400 < <primes>` (independent flag check);
`uv run python scripts/lsa_model_limit.py 1000000` (§3 item 3, ≈ 12 s).
