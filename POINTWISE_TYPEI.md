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

## 3. Under GRH: `ck_min ≫ log p·log log p` infinitely often

**Theorem 3.1 (CONDITIONAL on GRH for real Dirichlet characters).** For
every `ε>0` there are infinitely many primes `p≡1 (24)` with

```
n_p > (1/(2 log 2) − ε)·log p·log log p   and hence   ck_min(p) > (1/(2 log 2) − ε)·log p·log log p.
```

This is Montgomery's GRH Ω-result for `n_p` (Topics in multiplicative
number theory, LNM 227; quoted in Lau–Wu §1, archived
`sources/lit2026/lau-wu-least-quadratic-nonresidue.txt` l. 72), in the form
needed for Lemma 8.1 (the extra condition `p≡1 (mod 4)`); we give the
standard proof so that the congruence condition and the constant are
visible.

*Proof.* Let `y≥5`, and let `L=ℚ(√−1, √ℓ : ℓ≤y prime)`, a multiquadratic
field of degree `n_L=2^{π(y)+1}`. Its quadratic subfields have conductors
dividing `F=8∏_{3≤ℓ≤y}ℓ`, so by the conductor–discriminant formula
`log d_L ≤ n_L log F ≤ n_L(θ(y)+log 8)`. A prime `p>y` splits completely in
L iff `p≡1 (4)` and `(ℓ/p)=1` for all primes `ℓ≤y`. ζ_L is a product of
Dirichlet L-functions of real characters, so GRH for these gives the
Lagarias–Odlyzko effective Chebotarev theorem (Lagarias–Odlyzko 1977,
Thm 1.1; in Serre's form, Serre 1981, Thm 4): for the identity class,

```
| π_split(x) − Li(x)/n_L | ≤ c₁ x^{1/2} (log d_L / n_L + log x) + log d_L
                          ≤ c₁ x^{1/2}(θ(y)+3+log x) + n_L(θ(y)+3),
```

with c₁ absolute (the last term accounts for ramified primes; Serre's
form omits it at the cost of the constant). Hence the number of split primes in `(x/2,x]` is

```
≥ x/(3 n_L log x) − 2c₁ x^{1/2}(θ(y)+3+log x)   (x large),
```

which, after subtracting also `n_L(θ(y)+3)`, is positive as soon as
`2^{π(y)} ≤ x^{1/2}/(C(log x)²)` (using `θ(y)≪log x·log log x` in the range
below; then `n_Lθ(y) ≪ x^{1/2}/log x`). Take y maximal with
`π(y) ≤ (log x − 4 log log x − 2 log C)/(2 log 2)`. By the prime number
theorem `y ∼ π(y) log π(y) ∼ (1/(2 log 2)) log x·log log x`. Every split
`p∈(x/2,x]` has `p≡1 (4)`, `(2/p)=(3/p)=1` (so `p≡1 (24)`) and
`(ℓ/p)=1` for all `ℓ≤y`, so `n_p>y` and Lemma 8.1 (POINTWISE_OMEGA) gives
`ck_min(p)>y`. Since `log p = log x+O(1)`, the claim follows. ∎

**Remarks.**
* *Ceiling for congruence methods under GRH.* Ankeny (GRH):
  `n_p ≪ (log p)²`. By Cor 8.4 every congruence certificate for
  `ck_min(p)>T` forces `n_p>T`, so under GRH congruence methods can never
  certify `ck_min > C(log p)²`. Theorem 3.1 is within a factor
  `log p/log log p` of that ceiling, and matches the random model
  `max_{p≤x} n_p ≍ log x·log log x`.
* *GRH does not reach the combined event.* GRH controls Chebotarev
  conditions in fixed (or controlled-discriminant) fields, i.e. congruence
  conditions on p. On an unforced slice, `M_{c,k}(p)=0` is not a congruence
  event (notes Cor 52.2), and it involves target divisors D up to `√N≍p`,
  i.e. congruences on p modulo `hD` up to `h·p` (Lemma 1.1). GRH gives
  equidistribution of primes ≤x only to moduli `≤x^{1/2−o(1)}`. Section 4
  quantifies why this (and even Elliott–Halberstam) is insufficient.

## 4. Goal (1): what a proof of `ck_min ≥ g(p)·n_p` (g→∞) must do

Throughout, p is hard with `n_p=n`, and `1<G<n`.

**Proposition 4.1 (the exact event list; PROVED).** `ck_min(p)>G·n` iff
for every slice in

```
𝓤_p(G) = { (qc', k) : q a non-residue prime mod p, q∤c', every prime of sf(c') a residue mod p, qc'k ≤ G n }
```

and every j with `p < 4qc'k·j ≤ p+√N`, `(4qc'k·j − p) ∤ 4qc'j²+1`.

*Proof.* Lemma 8.1's computation gives `χ_s(p)=(−1/p)∏_{ℓ|s}(ℓ/p)`, so the
unforced slices are those whose core has an odd number of non-residue
primes; all non-residues are `≥n`, and `ck≤Gn<n²` allows exactly one, to
the first power. Forced slices vanish (notes Thm 48.1). For unforced ones
apply Lemma 1.1 and the `D↔N/D` pairing (only `D≤√N` is needed). ∎

So beyond `n_p` the event is a conjunction, over
`|𝓤_p(G)| ≍ Σ_{q nonres, n≤q≤Gn} (Gn/q)log(Gn/q)` slices, of
"`p²+4ck²` has no divisor `≤√N≈p` in the class `−p mod 4ck`".

**Proposition 4.2 (every hard class has primes with `ck_min=n_p`; PROVED,
a sharpening of POINTWISE_OMEGA Prop 8.3).** Let `24|L` and let `a mod L` be
reduced with `a≡1 (24)`. Then infinitely many primes `p≡a (L)` satisfy
`ck_min(p)=n_p`. Consequently no finite congruence combination B (as in
POINTWISE_OMEGA Cor 8.4) with `0≤B(p)≤1[ck_min(p)>G·n_p]` for all large
primes `p≡1 (24)` can be positive anywhere, for any `G≥1`: congruence input
gives exactly the factor `g=1`, and every gain `g>1` needs factorisation
input on the unforced slices.

*Proof.* Let ℓ be the least prime `≥5` with `ℓ∤L` or `(a/ℓ)=−1` (it exists
since L is finite). Run the proof of POINTWISE_OMEGA Prop 8.3 with this ℓ:
it produces infinitely many primes `p≡a (L)`, `p≡c_0 (4ℓ)` with
`(c_0/ℓ)=−1`, and `M_{ℓ,1}(p)≥1`, so `ck_min(p)≤ℓ`. For such p:
`(ℓ/p)=(p/ℓ)=(c_0/ℓ)=−1`; for primes `5≤ℓ'<ℓ` we have `ℓ'|L`, `(a/ℓ')=1`,
so `(ℓ'/p)=1`; and `(2/p)=(3/p)=1`. Hence `n_p=ℓ`, and
Lemma 8.1 gives `ck_min(p)≥n_p=ℓ`. So `ck_min(p)=n_p`. For the consequence:
B is L'-periodic; if `B(a)>0` on a reduced class `a mod L'` (necessarily
`a≡1 (24)` if it contains large hard primes), the first part gives primes
in it with `ck_min=n_p≤G·n_p`, contradicting `B≤1[ck_min>G n_p]`. (Read "positive anywhere" as "positive at some large hard prime"; B may be positive on non-hard classes, where it is unconstrained.) ∎

### 4.1 Sieve criteria: dimension ≥ 1/2 per unforced slice

The natural sieve-type sufficient condition for `M_{c,k}(p)=0` is "all prime
factors of N lie in a subgroup avoiding the target".

**Lemma 4.3 (subgroup criteria; PROVED).** Let `(c,k)` be unforced at p,
`K_s=ker χ_s ⊂ G_h=(ℤ/h)^×`, and `H≤G_h` a subgroup with `−p∉H`.
(a) If every prime factor of N lies in H, then `M_{c,k}(p)=0`.
(b) `−p∈K_s`, so `H∩K_s` is a proper subgroup of `K_s`, of index `≥2`.
The primes `ℓ∤2h` that can divide some `N_{c,k}(p')` and are excluded by
(a) are those in `K_s∖H`; they have relative density `≥1/4` among all
primes, and each has `ρ(ℓ)=2` roots of `p'²≡−4ck² (mod ℓ)`. So the
sifting problem "(a) holds" has dimension `κ ≥ 1/2`.
(c) If `H∩K_s=ker ψ ∩ K_s` for a real character ψ mod h with `ψ(−p)=−1`,
it suffices to sift primes `ℓ≤√N`: the product of all prime factors is
`N≡p² (mod h)`, which lies in `ker ψ ∩ K_s`, so a single prime factor
`>√N` is then automatically in H.
(d) For K unforced slices with pairwise distinct values `c_ik_i²`, the
excluded root classes `p'≡±2k_i√(−c_i) (mod ℓ)` are distinct for
`ℓ∤∏_{i<j}(c_ik_i²−c_jk_j²)`, so the dimensions add: `κ ≥ K/2`.

*Proof.* (a) All divisors lie in H. (b) `χ_s(−p)=−χ_s(p)=1` (`χ_s` is odd,
the slice unforced); every prime `ℓ|N`, `ℓ∤h`, has `χ_s(ℓ)=1`
(notes Thm 48.1 proof); `K_s` has density 1/2 and `H∩K_s` at most 1/4 of
the classes by Dirichlet. (c) `χ_s(N)=ψ(N)=1`, `N≡p²`. (d) Distinct
`c_ik_i²` give distinct polynomials `x²+4c_ik_i²`, whose roots mod ℓ differ
off the displayed resultant primes. ∎

**Assessment 4.4 (sieve limits; Assessment, not a theorem).** In p≤x the
criterion of Lemma 4.3 must sift `N≈x²` up to `z=√N≈x`, with moduli `d|N`
⇔ `p` in `ρ(d)` classes mod d. Level of distribution for primes in
progressions: `x^{1/2}` (Bombieri–Vinogradov, also GRH), `x^{1−ε}` (EH).
* One slice (`κ=1/2`): the semi-linear sieve has sifting limit `β=1`, and
  its lower function vanishes for `s=log D/log z≤1`. Even under EH we have
  `s<1`. A positive lower bound needs an extra large-prime (parity) input
  to exclude configurations with two prime factors `≡ψ-bad` in
  `(x^{1−ε},x]` — this is the same shape as POINTWISE_WINDOW Thm W2
  (EH-conditional), but for a quadratic polynomial at primes. Plausible
  under EH with a switching/parity argument; not carried out here.
* `K≥2` slices (`κ≥1`): the sifting limit of the known (β/DHR) sieves is
  `≥2` (`=2` for the linear sieve, where Selberg's parity example shows it
  optimal), so the level needed is `≥x²` against an available `≤x`; no
  bounded number of large-prime corrections closes a gap of this size.
* The GR/Thm 3.1 configuration needs `K=|𝓤_p(G)|≍G(log G)²·n_p/log n_p`
  simultaneous slices, i.e. dimension `≍log p`.

So subgroup-type sieve criteria cannot give even `g=1+η` beyond the
single-slice range. They are also far from the exact event: by Thm 52.1
the exact per-slice vanishing has "dimension" `2/φ(h)`, not `1/2`; the
gap is the composite-divisor structure (divisors of N, not primes, must
avoid one class), which is not a sieve condition.

### 4.2 The first moment and the level barrier

**Lemma 4.5 (level needed by the exact event; PROVED).** For a slice with
`h=4ck` and primes `p∈(x/2,x]`, the condition "`p²+4ck²` has a divisor
`D≡−p (mod h)`" restricted to divisors `D∈(Z,√N]` is the union, over those
D, of `ρ(D)` classes of p modulo `hD`. For `Z=x^{θ}` the moduli range over
`(h x^θ, h√N]`, and `h√N>hx/2`. Hence any argument that controls these
events through the distribution of primes in progressions needs moduli
`>x`, beyond EH and GEH, unless the divisors `D∈(x^{1−ε},√N]` are
handled otherwise. *Proof.* Lemma 1.1 and CRT (`(D,h)=1`). ∎

**Assessment 4.6 (union bound gives only O(1) further slices).** In the
divisor model (`D|N` with probability `ρ(D)/D`, target class probability
`2/φ(h)` inside `K_s`), the expected number of target divisors of an
unforced slice is `𝔼M_{c,k} ≈ c_0·L(1,χ_{−s})·log p/ck` (up to `φ` vs
identity factors), and the portion from `D∈(x^{1−ε},√N]` is a fraction
`≈ε` of it. Summing over `𝓤_p(G)` with `n≍log p·log₃p` (GR primes) or
`n≍log p·log₂p` (Thm 3.1):

```
Σ_{𝓤_p(G)} 𝔼M ≈ (c_0/2)·log p·Σ_{q nonres∈[n,Gn]} (1/q)·(log(Gn/q))²/2 ≈ (c_0/12)·(log G)³·log p/log n.
```

A union bound needs this `<1`, i.e. `(log G)³ ≪ log₂p/log p`: only the
first `O(1)` non-residue slices beyond `n_p`, i.e. `ck_min ≥ n_p+O(n_p·log₂p/log p)`,
no multiplicative gain. Joint vanishing at multiplicative scale G needs an
independence input of strength `exp(−c(log G)³log p/log₂p)` for
`≍G(log G)²·log p` factorisation events, i.e. a uniform (in the number of
polynomials) Hypothesis-H/Bateman–Horn statement. Under the Poisson model
it holds while `(log G)³ ≲ log₂p` (the GR primes number `x^{1−o(1)}`, the
model cost is `p^{−(c_0/12)(log G)³/log₂ p}`), suggesting the true i.o.
gain is `g(p)=exp(c(log₂p)^{1/3})` on GR-type primes (Assessment).

## 6. Goal (3), the upper-bound side: `C(r)=sup{ck_min(p) : p hard, n_p=r}`

Theorem 2.1 shows (under H) that no bound `ck_min ≤ f(n_p)` with
`f(r)≤r^{2−ε}` holds. But for each *fixed* r the set `{p hard : n_p=r}` is
a union of congruence classes mod `24∏_{ℓ≤r}ℓ` that is **not** a square
class (p is a non-residue mod r), so the Mordell–Schinzel square-class
obstruction does not apply, and `C(r)<∞` may be provable by a finite
covering by Type-I positivity classes (fixed target divisors). The census
(§5) gives `C(5)≥10`, `C(7)≥76`, `C(11)≥111`, `C(13)≥143`, `C(17)≥166`,
`C(19)≥218`, `C(23)≥222`, `C(43)≥883`.

**Theorem 6.1 (`C(5)=10`; PROVED, elementary).** Every hard prime p with
`(5/p)=−1` has `ck_min(p)≤10`; if moreover `p≡2 (mod 5)` then
`ck_min(p)=5`. The bound 10 is attained (`p=193`).

*Proof.* `n_p=5` (2, 3 are residues), and `p≡1 (8)`, `p≡1 (3)`,
`p≡2,3 (5)`, so `p≡17` or `33 (mod 40)`. All slices used below are in
`𝓑_p` for `p>40`, and have cores 5 or 10.
* `p≡17 (40)`: `h=20`, `−p≡3 (mod 20)`, and `p²+20≡1+2≡0 (mod 3)`. So
  `D=3` is a target divisor, `M_{5,1}(p)≥1`, `ck_min≤5=n_p≤ck_min`.
* `p≡33 (40)`: `−p≡7 (mod 40)`, hence also mod 20. As p ranges over units
  mod 7, `p²∈{1,2,4}`, and `−20≡1`, `−40≡2`, `−80≡4 (mod 7)`. So 7
  divides exactly one of `p²+20`, `p²+40`, `p²+80`, and `D=7` is a target
  divisor of the slice `(5,1)`, `(10,1)` or `(5,2)` respectively
  (`h=20,40,40`). Thus `ck_min≤10`.
(Every hard prime is `≥73>40`.) `ck_min(193)=10` (§5; `193≡33 (40)`). ∎

*Mechanism.* One fixed prime D (here 7) lies in the target class of several
slices at once (all `h|40`), and the values `−4ck² (mod D)` of those slices
cover all non-zero squares mod D. This is a finite covering by Type-I
positivity progressions in the sense of notes Thm 48.4, i.e. a Mordell-type
identity system restricted to Type I. (ES for `p≡2,3 (5)` is classical via
Mordell's identities; the content here is only the Type-I depth `≤10`.)
