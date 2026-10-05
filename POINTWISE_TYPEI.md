# Type-I `ck_min` beyond the least non-residue (task O31)

Status: checkpoint 1 (side agent O31, branch `side-agent/typei-ckmin`); not yet reviewed.

## 0. Results at a glance

| # | statement | label |
|---|---|---|
| L1.1 | `M_{c,k}(p)=#{j: hj>p, (hj−p) ∣ 4cj²+1}` (dual/Type-I form); vanishing is a congruence sieve on p with moduli `hD` up to `h·p` | PROVED |
| T2.1 | under Schinzel H: for every g and prime `r≥100D(g)²g³`, infinitely many hard p with `n_p=r`, `ck_min>g·n_p`; also `ck_min≥n_p^{2−ε}` i.o. So no bound `ck_min≤f(n_p)` with `f(r)≤r^{2−ε}` is provable without refuting H | CONDITIONAL (H, explicit finite family) |
| T3.1 | under GRH: `ck_min(p)>(1/(2log2)−ε)log p·log log p` i.o. (Montgomery's `n_p` Ω-result via Lagarias–Odlyzko, with `p≡1 (24)`) | CONDITIONAL (GRH) |
| P4.1 | exact event list for `ck_min>G·n_p` (one non-residue prime per unforced slice for `G<n_p`) | PROVED |
| P4.2 | every reduced hard class mod L contains infinitely many p with `ck_min(p)=n_p`; congruence input gives exactly `g=1` | PROVED |
| L4.3 | subgroup-type sieve criteria for an unforced slice have dimension `≥1/2`, additive over slices | PROVED |
| A4.4–4.6 | sieve/level/first-moment barriers: EH insufficient even for one slice by pure sieve; union bound gives only `O(1)` extra slices; Poisson model suggests `g=exp(c(log₂p)^{1/3})` on GR-type primes | Assessment |
| L4.5 | target divisors near `√N` correspond to classes mod `hD>hx/2` | PROVED (CRT description); the "needs moduli >x" consequence is Assessment |
| §5 | census of all 82887 hard `p<10^7`: new records `ck_min(414241)=218`, `ck_min(9033649)=883` (`n_p=43`, ratio 20.5) | EVIDENCE |
| T6.1 | `n_p=5 ⟹ ck_min(p)≤10` (sharp), by a mod-7 Type-I covering | PROVED |
| C6.4 | under H: `C(7)≥539`, `C(11)>3000` via explicit formal escape points; unconditionally any Type-I covering of `{n_p=7}` (resp. 11) has height ≥539 (>3000) | CONDITIONAL / PROVED |
| R6.2 | finite covering ⇒ `C(r)≤X` (PROVED); uncovered fixing class ⇒ `C(r)>X` under H; the exact equivalence needs a compactness step (sketched); `C(7)<∞`? open (EVIDENCE: covered by small-D certificates to `3·10^6`) | PROVED direction + H sketch; open |

**Answer to the task.** (1) An unconditional `ck_min ≥ g(p)·n_p`, g→∞,
was **not** obtained; §4 identifies the needed events exactly (P4.1) and
shows why available tools stop: congruences give exactly `g=1` (P4.2);
sieve criteria cost dimension `≥1/2` per slice and need sifting range
`√N≈x` at level `≤x` (L4.3, A4.4); first-moment needs `>x` moduli and
fails beyond `O(1)` slices (L4.5, A4.6). (2) GRH: T3.1; GRH/EH do not
reach the combined event. (3) The upper-bound direction is false in the
strong form under H (T2.1: `ck_min≥n_p^{2−ε}` i.o.), but **true for
`n_p=5`** (T6.1, `C(5)=10`), and in general reduces under H to a finite
covering problem per value of `n_p` (R6.2).

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
`2^{π(y)} ≤ x^{1/2}/(C(log x)²·log log x)`. In the range below,
`θ(y)≪log x·log log x`, so the main term `≍C x^{1/2} log x·log log x`
dominates `c₁x^{1/2}(θ(y)+3+log x)`, and `n_Lθ(y) ≪ x^{1/2}/log x`.
(R31-D2: the earlier condition omitted the `log log x` factor and did not
close.) Take y maximal with
`π(y) ≤ (log x − 4 log log x − 2 log log log x − 2 log C)/(2 log 2)`. By the prime number
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

*Scope (R31-D5).* `𝓤_p(G)` is understood intersected with `𝓑_p`
(`(p,ck)=1` and the size bounds of (36.1)). This intersection is
automatic when `G n_p<n_p²≤p/2`, which holds for every hard p (no hard
`p<10^6` has `n_p²>p/2`; beyond that, Burgess's bound `n_p≪p^{1/(4√e)+ε}` gives it for
large p, and explicit versions (e.g. Treviño) for all p; only large p
matter here). Since `ck<n²`, every prime of `c'` (not only of `sf(c')`)
is a residue.

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
`(h x^θ, h√N]`, and `h√N>hx/2`. *Proof.* Lemma 1.1 and CRT (`(D,h)=1`). ∎

*Consequence (Assessment, a meta-statement, not a theorem; R31-D4).* An
argument that controls these events through the distribution of primes in
progressions would need moduli `>x`, beyond EH and GEH, unless the
divisors `D∈(x^{1−ε},√N]` are handled otherwise.

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

(The cube is the large-G asymptotic of the continuous `(c',k)`-count. For
`G=1+η` with `η<1` the only slices are `(q,1)`, `q∈[n,Gn]`, and the mass is
linear: `≈(c_0/2)·η·log p/log n`.) A union bound needs the mass `<1`. In
the linear regime this gives `η ≪ log₂p/log p`: only the first `O(1)`
non-residue slices beyond `n_p`, i.e. `ck_min ≥ n_p(1+O(log₂p/log p))`,
and no multiplicative gain. (R31-D3: applying the cube formula at small
η would instead give `η≪(log₂p/log p)^{1/3}`; that formula does not
apply there. Either way, no fixed G>1 is reached.) Joint vanishing at multiplicative scale G needs an
independence input of strength `exp(−c(log G)³log p/log₂p)` for
`≍G(log G)²·log p` factorisation events, i.e. a uniform (in the number of
polynomials) Hypothesis-H/Bateman–Horn statement. Under the Poisson model
it holds while `(log G)³ ≲ log₂p` (the GR primes number `x^{1−o(1)}`, the
model cost is `p^{−(c_0/12)(log G)³/log₂ p}`), suggesting the true i.o.
gain is `g(p)=exp(c(log₂p)^{1/3})` on GR-type primes (Assessment).

## 5. Census (EVIDENCE)

`typei_ratio.py` (forced slices skipped by Thm 48.1; the `--noskip` run to
6000 gives identical output) over all 82887 hard primes `p<10^7`, data
`data/pointwise_typei/ckmin_np_1e7.txt.gz` (lines `p n_p ck_min`).
Reproduces notes (48.12)/(48.13) and the §48 records to `10^5`.

| range | #p | `ck_min=n_p` | ratio ≥2 | ratio ≥5 | max ratio (p, n_p, ck_min) | max ck_min |
|---|---|---|---|---|---|---|
| `[25,10^5)` | 1181 | 0.638 | 0.231 | 11 | (12289, 11, 77) | 103 (p=92401) |
| `[10^5,10^6)` | 8551 | 0.645 | 0.220 | 41 | (414241, 19, 218) | 218 |
| `[10^6,10^7)` | 73155 | 0.663 | 0.198 | 251 | (9033649, 43, 883) | 883 |

* New records beyond notes §48: `ck_min(414241)=218`, `ck_min(9033649)=883`
  (`n_p=43`, ratio 20.5, `ck_min/(log p)²=3.44`). The latter was
  re-verified by the independent dual engine of Lemma 1.1 (all slices,
  forced included, `ck≤900`): first positive slice `(883,1)`.
* `typei_records.py`: at `p=9033649` all 583 unforced slices with
  `ck<883` vanish (83 non-residue primes in `[43,883)`), model mass
  `Σ log p/ck=22.8`.
* Per-slice statistics near `p≈9.2·10^6` (unforced p only): `P(M=0)` is
  far above `exp(−𝔼M)` (e.g. slice (5,1): 0.127 vs 0.005; (43,1): 0.90 vs
  0.80) — M is even (pairs `D,N/D`) and heavy-tailed, so Assessment 4.6's
  Poisson form is conservative.
* By `n_p`: `n_p=5` (41568 primes): max `ck_min=10` (explained by Thm 6.1);
  `n_p=7`: max 76; 11: 111; 13: 143; 17: 166; 19: 218; 23: 222; 29: 202;
  31: 158; 37: 148; 41: 123; 43: 883.

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

**Remark 6.2 (what decides `C(r)`; PROVED direction + H-conditional
direction, sketch).** Call `(c,k,D)` with `(D,4ck)=1` a *Type-I
certificate*; its class is `{p : p≡−D (mod 4ck), p²≡−4ck² (mod D)}`, on
which `M_{c,k}(p)≥1` (Lemma 1.1). (i) If the certificates with `ck≤X`
cover `S_r={p hard : n_p=r}` (a union of classes mod `24∏_{ℓ≤r}ℓ`) up to
finitely many p, then `C(r)≤X` up to those p (PROVED; Thm 6.1 is the case
r=5, X=10, D∈{3,7}). (ii) Conversely, if some class of `S_r` (mod a
modulus fixing `v_ℓ(N_{c,k})` for all `ℓ≤B`, `ck≤X`) is not covered by the
certificates with B-smooth D, then the construction of Thm 2.1 steps 3–5
(fixed part times one H-prime) gives, under H, infinitely many p with
`n_p=r` and `ck_min(p)>X` (CONDITIONAL on H; this is the form used in
Thm 2.1 and Cor 6.4). *Equivalence (sketch, R31-D6).* The claim "under H,
`C(r)` is exactly the least height of a finite Type-I covering" needs one
more step: if every fixing class is covered by B-smooth certificates, then
a **finite** covering exists. Fixing classes have unbounded depth near the
ℓ-adic roots of the `N_{c,k}`, and the certificates there could use
unbounded powers `ℓ^e`. The step is a compactness argument in
`∏_{ℓ≤B}ℤ_ℓ`, which we only sketch:
* take an ℓ-adic root point p* of one slice;
* off finitely many ℓ, p* is not a root of any other slice;
* if p* were uncovered, then, since `ℓ^i mod 4ck` is periodic and the
  other slices are locally constant near p*, nearby fixing classes would
  be uncovered too, contrary to the hypothesis;
* so every point is covered, and compactness gives a finite subcover.

Until this is written out, only "finite covering ⇒ `C(r)≤X`" (PROVED) and
"uncovered fixing class ⇒ `C(r)>X` under H" are claimed. Thm 2.1 says the
latter happens at height `≥r^{2−ε}` for large r.


### 6.1 Literature: which coverings are known (task check)

* **Our certificates are a known family.** In Elsholtz–Tao
  (arXiv:1107.1010, Prop 1.9), the third Type-I family is
  `{n≡−f (mod 4cd)} ∩ {n²≡−4c²d (mod f)}`, `(4cd,f)=1`. This is exactly
  the certificate `(c_ours,k_ours,D)=(d,c,f)` of Remark 6.2. It is also
  Salez's modular equation (15d) (arXiv:1406.6307, Prop 3: `C,D,F`
  constant, `p+F≡0 (4CD)`, `p²+4C²D≡0 (F)`, with `(A,B,C,D)=(a,b,k,c)` in
  our Type-I equation `4abck=p(a+b)+k`).
* **Which families bound `ck_min`.** The other three Type-I families
  (Salez 15a–c / ET families 4, 2, 1) are also Type-I identities. But in
  each of them c or k grows linearly in p:
  * (15a): `D=c=(pE+1)/4AB`;
  * (15b): `D=c=(p+F)/4BC`;
  * (15c): `C=k=(p+F)/4BD`.

  Salez's equations (14a–c) are the other ET type, where p divides two
  denominators, so they are not Type-I.
  Hence: **`C(r)≤X` is witnessed by a finite covering of `S_r` by ET
  family-3 / Salez-(15d) classes with `ck≤X`** (Remark 6.2), and only
  those classes count.
* **Known coverings.** The classical "Mordell" covering of all non-square
  classes mod 840 (Rosati; Mordell 1967, pp. 287–290; ET p. 8) and Salez's
  filters (`S_5={0,2,3}`, `S_7={0,3,5,6}`, so all non-residues mod 5 and
  mod 7 are covered for `p≡1 (24)`) use all seven equation types. For
  primes 11–37 Salez's single-prime filters do **not** contain all
  non-residues; e.g. `S_11={0,7,8,10}` misses the non-residues 2 and 6. So
  for `p≡1 (24)` the literature has full single-prime coverings exactly for
  `r=5,7`.
* **What these coverings give for `C(r)`.**
  * For `r=7` the classical covering does not bound `C(7)`. No
    (15d)-certificate is decided modulo `168=[7,24]` on a non-residue class
    mod 7. With F built from `{3,7}`, the condition `F≡−p (mod 4ck)` and
    `p≡1 (24)` force `ck|2` (core in `{1,2}`) or a residue class mod 7.
    The mod-7 identities are therefore of the growing types (15a–c) or of
    the non-Type-I type (14).
  * For `r=5`, Salez's Example 1 [15d] is a (15d) identity for
    `p≡2 (5)`, with `C=1, D=5`, i.e. slice `(5,1)` with target divisor 3
    (our Thm 6.1, first case). The second case of Thm 6.1 (`p≡3 (5)`,
    mod-7 split over three slices) is not listed there.

  I found no published statement on Type-I coverings with bounded ck
  for any r.

**EVIDENCE 6.3 (r=7).** `typei_smallD.py 7 3000000 2000 400`: all 6495
hard primes in `(10^5,3·10^6)` with `n_p=7` have a positive unforced slice
with `ck≤194` witnessed by a target divisor `D≤2000` (most frequent D: 11,
3, 23, 15, 71, 7, 39, …); with `D≤200, ck≤120`, 27 are not witnessed. This
is consistent with a finite covering for r=7 but uses many D's.
`typei_cover.py` (sound covering search: c,k smooth over `{2,…,r}`, D with at
most one new prime) re-proves Thm 6.1 (`typei_cover.py 5 10 7 3 1 1`: 2/2
nodes covered) but for r=7 leaves 1684 of 7560 nodes mod `32·27·25·49`
uncovered (`X=1500, Dmax=3000`). The actual witnesses on the uncovered
class `p≡601 (5040)` use slices whose core contains a *further*
non-residue prime (`(11,1,D=3)`, `(17,1,3)`, `(19,1,7)`, `(26,1,15)`, …),
so a covering for r=7 must branch on `p mod ℓ` for `ℓ=11,13,17,…`; the
worst branches are the residue-one-like points, where the analysis is
that of Thm 2.1 step 5. Not done. **Open:** is
`C(7)<∞`? Is `C(r)<∞` for every r? A positive answer for all r would prove
Type-I ES for all hard primes (by a family of coverings, one per value of
`n_p` — an E2 escape in the sense of POINTWISE_SIZE Prop A, since `n_p` is
not a bounded formal quantity).


### 6.2 Branching covering search and formal escape points (r=7, r=11)

**Covering search** (`typei_branch_cover.py`). This is a sound DFS. It
fixes `p mod ∏_{ℓ≤r}ℓ^{E_ℓ}` and then branches on `p mod q` for new primes
`q≤Qmax`. Only residues that are not already covered are branched on.
The certificates are `(c,k,F)` with `ck≤X`, `F≤Fmax`, and at most one
undecided prime in F.
* It re-derives Thm 6.1 (`5 10 7 7 3,1,1`: COVERED).
* For r=7 (`7 600 5000 47 5,3,1,1`) it is NOT covered. The first
  uncovered leaves are residue-one-like classes: `p≡25 (32)`,
  `p≡7 (27)`, `p≡1 (5)`, `p≡6 (7)`, and `p≡1` or close to it modulo
  every prime in `11,…,47`.
* No finite covering was found for r=7 or r=11. The formal points below
  explain why.

**Formal ck_min at H-generic points** (`typei_formal.py`; this is the
Thm 2.1 machinery with an arbitrary prescribed residue pattern). Take p
with prescribed residues `a_ℓ mod ℓ^{e_ℓ}` and `p≡1 (mod ℓ^E)` at every
other prime `ℓ≤B`. The script computes the fixed B-part `f_{c,k}` of
every `N_{c,k}` with `ck≤X`. It asserts that this part, and every target
class `−p mod 4ck`, is determined by the class. It then evaluates
`M=2·#{D|f: D≡−p (4ck)}`. Under H, with `B≥2·#slices+2`, infinitely many
primes in the class have exactly this `ck_min` and this `n_p`.
(CONDITIONAL on H for the explicit family; the proof is Thm 2.1 steps 3–5
verbatim.)

| r | prescribed residues (all other ℓ≤B: `p≡1 mod ℓ^E`) | X, B | formal `ck_min` | witness |
|---|---|---|---|---|
| 7 | `p≡3` or `5 (7)` | 2000, 30000 | 21 | (7,3), D=11 / 23 |
| 7 | `p≡6 (7)` | 2000, 30000 | 28 | (14,2), D=15 |
| 7 | `p≡25 (2^{14}), 7 (3^9), 6 (7^6)` | 2000, 30000 | **539** | (77,7), D=43 |
| 7 | `p≡25 (2^{14}), 7 (3^9), 13 (7^6)` | 1500, 12000 | 98 | (14,7), D=183 |
| 11 | `p≡25 (2^{14}), 7 (3^9), 2 (11^4)` | 1500, 12000 | 990 | (55,18), D=119 |
| 11 | `p≡2 (11^5)` | 3000, 30000 | **>3000** | none |
| 11 | `p≡2` or `6 (11^4)` | 1500, 14000 | >1500 | none |

**Corollary 6.4 (CONDITIONAL on H).**
* There are infinitely many primes with `n_p=7` and `ck_min(p)=539`, so
  `C(7)≥539` (census: 76).
* There are infinitely many primes with `n_p=11` and `ck_min(p)>3000`, so
  `C(11)>3000` (census: 111).
* Unconditionally, any finite Type-I covering of `{n_p=7}` must have height
  `≥539`, and any covering of `{n_p=11}` must have height `>3000` (PROVED).
  *Proof.* Let `X_0` be the formal `ck_min` of the escape point
  (`X_0=539` for r=7; for r=11 put `X_0=3001`). Suppose a finite covering
  by certificates of height `<X_0` is given, and let `ℓ_1,…,ℓ_t>B` be the
  primes `>B` that occur in its F's. Certificates on forced slices never
  hold (notes Thm 48.1). So it suffices to refine the formal class by
  `p≢0` and `p≢` any root of `N_{c,k}` mod each `ℓ_i`, for the **unforced**
  slices with `ck<X_0`. There are 319 such slices for r=7 and 1491 for
  r=11. This excludes at most `2·#+1` residues, and `ℓ_i>B>2·#+1`
  (B=30000), so the refinement is possible. The refined class is a
  reduced class mod `Q·∏ℓ_i`. By Dirichlet it contains infinitely many
  primes, all hard with `n_p=r`.
  * A certificate on an unforced slice whose F contains some `ℓ_i` never
    holds there (`ℓ_i∤N`).
  * A certificate on an unforced slice with B-smooth F holds on the class
    iff F divides the fixed part and `F≡−p (4ck)`. Both are determined by
    the class (checked for every unforced slice with `ck<X_0`), and the
    computation excludes them.

  So the class is not covered. ∎

*Why r=11 escapes so well.* At the residue-one point the unforced slices
are `(11c',k)` with odd `v_11(c)`. Write `m` for the 11-free part of `ck`,
and `a1=v_11(c)`, `a2=v_11(k)`. A target divisor D of
`f=1+4ck²` (exactly, because `p≡1` elsewhere) has `D≡−1 (mod 4m)`, and so
does its cofactor `e`. So `D=4mj−1`, `e=4mj'−1`, and
`4mjj'−j−j'=ck²/m`. Hence `jj'≈11^{a1+2a2}/(4c')`. For `11∥c` and
`11∤k` this leaves only `jj'≤3`, which is a finite set of checks mod 11.
Real freedom starts only at `ck≥11·121`. This is the mechanism of
Thm 2.1, and here it already works at r=11.

**Status of `C(7)`, `C(11)`.** Both are open. Unconditionally no covering
was found; under H the lower bounds above hold. I conjecture
(CONJECTURE, weak evidence) that `C(r)=∞` under H for every `r≥7`, i.e.
that `r=5` is the only value of `n_p` with a finite Type-I covering. Two
things support this: the DFS keeps meeting residue-one-like leaves, and the
best formal points reach far beyond the census maxima.

## Replay

```
PYTHONPATH=scripts uv run python scripts/typei_dual_check.py 300 10        # Lemma 1.1, 0 mismatches
PYTHONPATH=scripts uv run python scripts/typei_ratio.py 25 30000 200       # notes (48.12) records, Lemma 8.1
PYTHONPATH=scripts uv run python scripts/typei_ratio.py 25 6000 200 /tmp/a --noskip   # forced-skip check
PYTHONPATH=scripts uv run python scripts/typei_ratio.py 25 3000000 2000 /tmp/r1.txt     # §5 (~10 min)
PYTHONPATH=scripts uv run python scripts/typei_ratio.py 3000000 10000000 2000 /tmp/r2.txt  # §5 (~1 h)
PYTHONPATH=scripts uv run python scripts/typei_records.py 9033649 414241 12289
PYTHONPATH=scripts uv run python scripts/typei_smallD.py 7 3000000 2000 400  # EVIDENCE 6.3
uv run python scripts/typei_c5.py                                          # Thm 6.1 covering mod 840
uv run python scripts/typei_branch_cover.py 7 600 5000 47 5,3,1,1   # §6.2 DFS (not covered)
uv run python scripts/typei_formal.py 2000 30000 2:25:14 3:7:9 7:6:6     # formal ck_min=539
uv run python scripts/typei_formal.py 3000 30000 11:2:5                   # >3000 (~40 min)
uv run python scripts/typei_cover.py 5 10 7 3 1 1; uv run python scripts/typei_cover.py 7 1500 3000 5 3 2 2   # §6 covering search
```
