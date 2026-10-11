# Long shot A: a deterministic pigeonhole ("highly composite slices") mechanism for pointwise ES (task O135)

Status labels as in DISCOVERIES.md. **ES is not proved here, nor any new case of it.** Work in progress;
§0 is filled in at the checkpoint.

## 0. Summary (checkpoint)

(to be written)

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
