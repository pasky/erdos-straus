# Type-I `ck_min` beyond the least non-residue (task O31)

Status: IN PROGRESS (side agent O31, branch `side-agent/typei-ckmin`).

Notation as in POINTWISE_OMEGA §8 and notes §§36, 44, 48, 50, 52. A slice
is `(c,k)∈𝓑_p` (notes (36.1)); `h=4ck`, `N=N_{c,k}(p)=p²+4ck²`,
`s=sf(c)`, `χ_s=(Δ_s/·)`;
`M_{c,k}(p)=#{D>0 : D|N, D≡−p (mod h)}`;
`ck_min(p)=min{ck : (c,k)∈𝓑_p, s∉{1,2,3,6}, M_{c,k}(p)>0}`;
`n_p` = least quadratic non-residue mod p. A slice is **forced** at p if
`χ_s(p)=1` (then `M=0`, notes Thm 48.1) and **unforced** if `χ_s(p)=−1`.
"Hard" means `p≡1 (mod 24)`.

## 1. The dual (divisor) form of slice vanishing

**Lemma 1.1 (dual parametrisation; PROVED).** Let p be an odd prime and
`(c,k)` positive integers with `(p,ck)=1`. Then

```
M_{c,k}(p) = #{ j ≥ 1 : hj > p,  (hj − p) | 4cj² + 1 }.
```

Equivalently, `M_{c,k}(p)>0` iff `p = 4ck·j − D` for some `j≥1` and some
divisor `D` of `4cj²+1` with `D<4ckj`.

*Proof.* Every target divisor D is a positive integer `≡−p (mod h)`, so
`D=hj−p` with a unique integer `j`, and `D>0` forces `hj>p`, `j≥1`. Since
`hj≡p (mod D)`,

```
N = p²+4ck² ≡ h²j²+4ck² = 4ck²(4cj²+1)   (mod D).
```

`(D,2ck)=1` because `D≡−p (mod 4ck)` and `(p,2ck)=1`. Hence
`D|N ⟺ D | 4ck²(4cj²+1) ⟺ D | 4cj²+1`. ∎

So the slice-positivity set
`S_{c,k}={4ckj−D : j≥1, D|4cj²+1, 0<D<4ckj}` is the classical Type-I
parametrisation (`a=j`, notes (50.5)) and `M_{c,k}(p)=0 ⟺ p∉S_{c,k}`
(counting multiplicity). Since `N≡p² (mod h)`, the involution `D↔N/D`
preserves the target class, so `M_{c,k}(p)>0` iff some target divisor
`D≤√N` exists; `√N ≤ p+2ck²/p`, so these D are `≤ p(1+o(1))` for
`ck²=o(p²)`. In sieve language:

* for a fixed divisor value D, `D|N, D≡−p (h)` is a union of `ρ(D)`
  classes of p modulo `hD` (ρ = number of roots of `x²≡−4ck² (D)`);
* vanishing is "p avoids all these classes for all D up to `√N≍p`", a
  congruence sieve whose moduli `hD` run up to `h·p`, i.e. **beyond the size
  of the sifted variable** (see §4).

## 2. Conditionally, `ck_min` is not bounded by any function of `n_p`

Task goal (3) asked whether `ck_min(p) ≪ f(n_p)` might hold (for all p or
on average). The pointwise form is impossible to prove without disproving
Schinzel's Hypothesis H.

**Theorem 2.1 (H-conditional unboundedness of `ck_min/n_p`; CONDITIONAL on
H for an explicit finite family).** Let `g≥1` be an integer and `r>g`,
`r≥5` a prime with

```
Σ_{c'k≤g} τ(1+4rc'k²)  <  (r−1)/2.                                  (2.1)
```

Assume Schinzel's Hypothesis H for the `1+D(g)` polynomials (2.3) below,
`D(g)=Σ_{m≤g}τ(m)`. Then there are infinitely many primes `p≡1 (24)` with

```
n_p = r      and      ck_min(p) > g·r = g·n_p.
```

(2.1) holds for all `r ≥ 100·D(g)²·g³` (use `τ(n)≤2√n`), and also for
`g = r^{1−ε}`, `r≥r_0(ε)` (use `τ(n)=n^{o(1)}`). Hence, under H (for a
finite family depending on ε), `ck_min(p) ≥ n_p^{2−ε}` for infinitely many
hard p, and `limsup ck_min(p)/n_p = ∞`.

*Proof.* Put `𝓕={(rc',k): c'k≤g}` and `A_{c,k}=1+4ck²` for `(c,k)∈𝓕`.
Choose `B ≥ max(g·r, 2|𝓕|+2, max_𝓕 A_{c,k})` and for each prime
`ℓ≤B`, `ℓ≠r`, an exponent `E_ℓ` with `ℓ^{E_ℓ} > max_𝓕 A_{c,k}`. Let
`P=∏_{ℓ≤B,ℓ≠r} ℓ^{E_ℓ}`, `Q=Pr`, and let `a mod Q` be the class with

```
a ≡ 1 (mod P),     a ≡ b (mod r),                                    (2.2)
```

where b is a quadratic non-residue mod r chosen in step 5.

1. *`n_p=r`.* For prime `p≡a (Q)`: `p≡1 (8)` and `p≡1 (ℓ)` for odd
   `ℓ<r`, so `(2/p)=1` and `(ℓ/p)=(p/ℓ)=1`; and `(r/p)=(p/r)=(b/r)=−1`.
   Also `p≡1 (24)`.
2. *The unforced slices with `ck≤gr` are exactly 𝓕.* Let `ck≤gr≤B`. If
   `v_r(c)` is even, every prime of `s=sf(c)` is `≤B`, `≠r`, hence a residue
   mod p, and `χ_s(p)=(−s/p)=1`: the slice is forced and `M_{c,k}(p)=0`
   (notes Thm 48.1). If `v_r(c)` is odd then `c=rc'`, `r∤c'` (as
   `r²>gr≥ck`), and `c'k≤g`, i.e. `(c,k)∈𝓕`.
3. *Factorisation shape.* Fix `(c,k)∈𝓕`. For `ℓ≤B`, `ℓ≠r`:
   `N≡1+4ck²=A (mod ℓ^{E_ℓ})` and `v_ℓ(A)<E_ℓ`, so `v_ℓ(N)=v_ℓ(A)`. For
   `ℓ=r`: `r|c`, so `N≡p²≢0` and `A≡1 (mod r)`. Since every prime factor
   of A is `≤A≤B`, we get `N=A·R` with R free of primes `≤B`.
4. *Hypothesis H.* With `p=Qt+a`, the polynomials

   ```
   f_0(t)=Qt+a,        f_{c,k}(t) = ((Qt+a)²+4ck²)/A_{c,k},  (c,k)∈𝓕,    (2.3)
   ```

   lie in `ℤ[t]` (`A|Q` and `A|a²+4ck²` by step 3), are irreducible (the
   quadratics have negative discriminant), and have positive leading
   coefficients. Their product has no fixed prime divisor: for `ℓ|Q` each
   factor is a unit mod ℓ at every t (step 3 and `a` reduced); for `ℓ∤Q`
   we have `ℓ>B≥2|𝓕|+2`, and the product is a nonzero polynomial mod ℓ of
   degree `1+2|𝓕|<ℓ` (its leading coefficient is prime to ℓ), so some t mod
   ℓ is not a root. H gives infinitely many t with all values prime; for
   large t, `p=f_0(t)` is prime and every `R_{c,k}=f_{c,k}(t)` is a prime
   `>A_{c,k}`.
5. *Counting target divisors; choice of b.* For such p and `(c,k)∈𝓕`, the
   divisors of `N=AR` are `D` and `DR` with `D|A`. Since `N≡p² (mod h)` and
   A is a unit mod h, `DR≡−p ⟺ Dp²A^{−1}≡−p ⟺ A/D≡−p (mod h)`. Hence

   ```
   M_{c,k}(p) = 2·#{D | A_{c,k} : D ≡ −p (mod 4ck)}.
   ```

   Write `m=c'k`. All primes of `4m` are `≤B`, `≠r`, and
   `ℓ^{E_ℓ}>A>4m`, so `p≡1 (mod 4m)`. Thus `D≡−p (mod h=4mr)` iff
   `D≡−1 (mod 4m)` and `D≡−b (mod r)`. The set
   `𝒟={D mod r : (c,k)∈𝓕, D|A_{c,k}, D≡−1 (4c'k)}` has at most the
   left side of (2.1) elements, which is `<(r−1)/2`, the number of
   non-residues. Choose a non-residue b with `−b∉𝒟`. Then `M_{c,k}(p)=0`
   for every `(c,k)∈𝓕`.

By steps 2 and 5, every slice with `ck≤gr` (with `s∉{1,2,3,6}` or not)
has `M=0`, so `ck_min(p)>gr`.

*The two sufficient ranges for (2.1).* (i) `τ(n)≤2√n` and
`A≤1+4rg³≤5rg³` give left side `≤2D(g)√5·g^{3/2}√r`, which is
`<(r−1)/2` once `√r ≥ 4√5·D(g)g^{3/2}+1`; `r≥100D(g)²g³` suffices.
(ii) `τ(A)≤exp(O(log r/log log r))=r^{o(1)}` uniformly for `A≤5r⁴`, and
`D(g)≤g(1+log g)`, so for `g=⌊r^{1−ε}⌋` the left side is `r^{1−ε+o(1)}`.
Then `ck_min(p)>gr ≥ r^{2−ε}/2` with `n_p=r`. ∎

**Remarks.**
* This is the formal-genericity mechanism (POINTWISE_SIZE Thm C) applied
  to `ck_min`: on the H-generic points the norm `N_{c,k}` factors as a
  fixed part times one large prime, and slice positivity reduces to the
  divisors of the fixed part `A_{c,k}=1+4ck²`.
* The construction stops at exponent 2: for `g≥r` the family 𝓕 has
  `≫r log r` slices and 𝒟 can exhaust the residue classes mod r.
* Corollary (goal 3, negative): any proof that `ck_min(p) ≤ f(n_p)` for
  all large hard p, for any function f, or even `ck_min(p) ≤ n_p^{2−ε}`,
  would disprove Hypothesis H for the explicit family (2.3). Averaged
  upper bounds are not affected (the H-primes have density zero).
