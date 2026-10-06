# Type-I depth on `{n_p = r}`: compactness and the profinite question (task O69)

Status: work in progress (side agent O69, branch `side-agent/typei-sterile`).
Builds on POINTWISE_TYPEI.md (notation, Lemma 1.1, Thm 2.1, Remark 6.2, Cor 6.4).

## 0. Setup

`Ẑ=∏_q ℤ_q`. A *certificate* is `κ=(c,k,F)` of positive integers with
`(F,4ck)=1` and `s=sf(c)∉{1,2,3,6}`; its *height* is `ck` and its class is
the clopen set

```
Cl(κ) = {x ∈ Ẑ : x ≡ −F (mod 4ck),  x² ≡ −4ck² (mod F)}.
```

`Σ_r ⊂ Ẑ^×` (r ≥ 5 prime) is the clopen set of unit points with `x≡1 (24)`,
`x mod ℓ` a non-zero square for primes `5≤ℓ<r`, `x mod r` a non-square.
`Σ_r` is compact. By quadratic reciprocity a prime `p>r` is hard with
`n_p=r` iff `p∈Σ_r`.

**Lemma 0.1 (PROVED).** Let p be an odd prime and `(c,k)∈𝓑_p`. Then
`M_{c,k}(p)≥1` iff `p∈Cl(c,k,F)` for some F; the F's are exactly the target
divisors. *Proof.* A target divisor D satisfies `D|N`, `D≡−p (4ck)`, and
`(D,4ck)=1` because `(p,2ck)=1`; so `p∈Cl(c,k,D)`. Conversely
`p∈Cl(c,k,F)` means `F|p²+4ck²=N` and `F≡−p (4ck)`. ∎

So `ck_min(p)=min{ck : (c,k)∈𝓑_p, s∉{1,2,3,6}, p∈⋃_F Cl(c,k,F)}`.

A *Type-I covering of `Σ_r` of height ≤X* is a finite set of certificates
of height ≤X whose classes cover `Σ_r`. Let `X_r∈ℕ∪{∞}` be the least such
height. Put `C*(r)=limsup ck_min(p)` over hard p with `n_p=r` (this differs
from `C(r)=sup` only by finitely many p, each with its own value).

## 1. Closing the compactness gap of Remark 6.2(ii)

**Theorem A (PROVED (i); CONDITIONAL on H (ii)).**
(i) `ck_min(p)≤X_r` for every hard p with `n_p=r` and `p>2X_r`. Hence
`C*(r)≤X_r`.
(ii) Let X be such that no covering of height ≤X exists. Then, under
Schinzel H for an explicit finite family `𝓟_X` (§1, step 4), there are
infinitely many hard p with `n_p=r` and `ck_min(p)>X`.
(iii) Hence, under H, `C*(r)=X_r`. Moreover `X_r=∞` iff some point
`x*∈Σ_r` lies in no `Cl(κ)` at all (a *sterile point*).

*Proof of (i).* For `p>2X` and `ck≤X`: `p∤ck`, `k≤X<2p/3`,
`c≤X≤(2p+k)/4k` (as `4ck≤4X<2p`), so `(c,k)∈𝓑_p`. Apply Lemma 0.1. ∎

*Proof of (iii) from (i), (ii).* The first claim is immediate. For the
second: the `Cl(κ)` are open and `Σ_r` is compact. ∎

*Proof of (ii).*

*Step 1 (compactness).* Let `K_X` be the (infinite) set of all
certificates of height ≤X. If `⋃_{K_X}Cl(κ)⊇Σ_r`, a finite subcover is a
covering of height ≤X. So some `x*∈Σ_r` lies in no `Cl(κ)`, `κ∈K_X`.

*Step 2 (move off the roots).* Let `𝓢` be the set of slices with `ck≤X`,
`s∉{1,2,3,6}`, and `m=#𝓢`. Fix a prime `B≥max(X,r,2m+2)`. Write
`N_V(x)=x²+4V`, so `N_{c,k}=N_{ck²}`. Fix a prime `q≤B`.
* At most one value `V∈{ck² : (c,k)∈𝓢}` has `N_V(x*_q)=0` in `ℤ_q`,
  since `x*_q` determines `−4V=x*_q²`. Such a root needs `q` odd and
  `q∤V` (for `q|V` or `q=2`, `N_V(x*_q)` is a unit; recall `x*_q` is a
  unit).
* If there is no root, put `y_q=x*_q`.
* If `V` is a root, take `T` larger than `v_q(N_{V'}(x*_q))` for all other
  values `V'`, and put `y_q=x*_q+q^T`. Then
  `N_V(y_q)=(y_q−x*_q)(y_q+x*_q)`, so `v_q(N_V(y_q))=T`. For `V'≠V`,
  `N_{V'}(y_q)≡N_{V'}(x*_q) (mod q^T)`, so `v_q(N_{V'}(y_q))=v_q(N_{V'}(x*_q))`.

Now take `E_q` larger than every `v_q(N_{c,k}(y_q))`, `(c,k)∈𝓢`, and
than `v_q(4X!)`, with `E_2≥3`. Let `𝒞` be the class `x≡y_q (mod q^{E_q})`,
`q≤B`. On `𝒞`:
* `v_q(N_{c,k}(x))=n_{c,k,q}:=v_q(N_{c,k}(y_q))` is constant for every
  `(c,k)∈𝓢`, `q≤B`;
* `x≡y (mod 4ck)`;
* `𝒞⊂Σ_r` (since `y_q≡x*_q (mod q)` and `y_2=x*_2`).

Put `f_{c,k}=∏_{q≤B}q^{n_{c,k,q}}`, the fixed B-part.

*Step 3 (transfer to x\*).* Let `(c,k)∈𝓢` and `d|f_{c,k}`. Claim:
`d≢−y (mod 4ck)`. Suppose otherwise; we show `x*∈Cl(c,k,d)`.
* For `q|4ck` there is no perturbation at q (no root), so
  `x*≡y≡−d (mod 4ck)`.
* For `q|d`, either `y_q=x*_q`, or the value `ck²` is the root at q (then
  `v_q(N_{c,k}(x*_q))=∞`), or it is not (then
  `v_q(N_{c,k}(x*_q))=n_{c,k,q}`). In every case
  `v_q(N_{c,k}(x*_q))≥n_{c,k,q}≥v_q(d)`.
* `(d,4ck)=1` follows from `d≡−y` with `y` a unit.

So `(c,k,d)∈K_X` and `x*∈Cl(c,k,d)`, contrary to Step 1.

*Step 4 (the H family).* Let `Q=∏_{q≤B}q^{E_q}` and `a≡y (mod Q)`,
`0<a<Q`. The family `𝓟_X` consists of `f_0(t)=Qt+a` and the distinct
polynomials

```
g_{c,k}(t) = ((Qt+a)² + 4ck²) / f_{c,k},      (c,k) ∈ 𝓢.
```

(Slices with the same `ck²` give the same polynomial.)
* Integer coefficients: `f_{c,k}|Q` (since `E_q>n_{c,k,q}`) and
  `f_{c,k}|a²+4ck²`.
* Irreducible: quadratics with negative discriminant.
* No fixed prime divisor. For `q≤B`, every value is a q-unit, by the
  exact valuations of Step 2. For `q>B`, the product has degree
  `≤1+2m<q` and leading coefficient prime to q, so it is a nonzero
  polynomial mod q with a non-root.

Under H, infinitely many t make all members prime simultaneously. For
large such t, `p=f_0(t)` is prime and `N_{c,k}(p)=f_{c,k}R_{c,k}` with
`R_{c,k}` a prime `>B`.

*Step 5 (vanishing).* For such large p: `p∈Σ_r`, so p is hard with
`n_p=r`. Let `(c,k)∈𝓢`; then `(c,k)∈𝓑_p` (proof of (i)). Every target
divisor is `d` or `dR` with `d|f=f_{c,k}`, `R=R_{c,k}`.
* `d≡−p≡−y (mod 4ck)` is excluded by Step 3.
* `N≡p² (mod 4ck)`, and `f` is a unit mod `4ck`. So with `e=f/d`,
  `dR=dN/f≡dp²/f`, and `dR≡−p ⟺ dp≡−de ⟺ e≡−p (mod 4ck)`. This is
  excluded by Step 3 applied to `e|f`.

So `M_{c,k}(p)=0` for every `(c,k)∈𝓢`: `ck_min(p)>X`. ∎

**Remarks.**
* Forcedness (notes Thm 48.1) is not used. Forced slices simply never
  contain a certificate class point of `Σ_r`.
* The family `𝓟_X` must depend on X. A single finite family controls
  `N_{c,k}` for finitely many slices only.
* This closes R31-D6 / the gap of Remark 6.2(ii). The decisive object is
  thus a **sterile point**: `x*∈Σ_r` with `x*∉Cl(κ)` for *every*
  certificate κ. Under H, `C(7)=∞` iff `Σ_7` has a sterile point. Then
  `𝓟_X` is explicit from `x*` and X.

## 2. Sterile points for r=7: reductions

**Lemma 2.1 (forced slices at "square" points; PROVED).** Let `x*∈Σ_7` with
`x*_q` a square in `ℤ_q^×` for every prime `q≠7` (for q=2: `x*_2≡1 (8)`).
Then a certificate `(c,k,F)` can hold at x* only if `v_7(c)` is odd.
*Proof.* `χ_s(x*)` depends on `x* mod 4s` and equals `∏_{q|s}(x*_q/q)`
times the 2-adic factor, which is 1; so `χ_s(x*)=−1` iff `7|s`. If
`χ_s(x*)=1` and `x*∈Cl(c,k,F)`, the open set `Cl(c,k,F)∩{χ_s=1}∩Σ_7`
contains a unit class, hence (Dirichlet) primes p with `(c,k)∈𝓑_p`,
`χ_s(p)=1` and `M_{c,k}(p)≥1`, contradicting notes Thm 48.1. ∎

**Lemma 2.2 (7-adic balls; PROVED).** Fix all components of such an x*
except `x*_7`. For a slice with `v_7(c)` odd, `v=v_7(ck)`, we have
`7∤N_{c,k}(x*)`, so `(c,k,F)` holds at x* iff (a) `F` divides the
7-free fixed part and `F≡−x* (mod 4ck/7^v)` (conditions not involving
`x*_7`), and (b) `x*_7≡−F (mod 7^v)`. So every certificate forbids one ball
of radius `7^{−v}` for `x*_7`, and a sterile `x*_7` exists iff these balls
miss some non-square unit of `ℤ_7`. (`scripts/typei2_balls.py`.)

**Proposition 2.3 (the residue-one point is not sterile; PROVED).** Let
`x*_q=1` for all `q≠7`. Then every non-square `x*_7` is covered already at
level `v=1`: by `(7,3,11)`, `(7,3,23)`, `(14,2,15)` for `x*_7≡3,5,6 (7)`.
In fact these are **all** level-1 certificates there. *Proof.* Here
`N=1+4ck²` is an integer and `F≡−1 (mod 4m)`, m the 7-free part of
`ck`; the cofactor `e=N/F` also satisfies `e≡−1 (mod 4m)`. Write
`c=7^a c'`, `k=7^b k'`, `F=4mj−1`, `e=4mj'−1` (`j,j'≥1`). Expanding
`Fe=1+4ck²` gives `4c'k'jj'−j−j'=7^{a+2b}k'`. So `k'|j+j'`; put
`j+j'=k'u`. Then `4c'jj'=7^{a+2b}+u` and `u≤j+j'≤jj'+1`. For `a=1,b=0`:
`u≤(7+u)/(4c')+1`. If `c'=1` this gives `u≤3`, with `4|7+u`, so `u=1`,
`jj'=2`, `k'=3`: `F=11,23`. If `c'≥2`, `u≤2` and `4c'|7+u`, so `u=1`,
`c'=2`, `j=j'=1`, `k'=2`: `F=15`. The three certificates are checked
directly (`253=11·23`, `225=15²`). ∎

Numerically (`typei2_balls.py 20000 3 1 2:25:14 3:7:9`): at the point
`x*_2=25, x*_3=7`, `x*_q=1` (q≠2,3,7) of Cor 6.4, `x*_7≡3,5` are again
killed by `(7,3,11)`, `(7,3,23)`, and `x*_7≡6` is killed at level 1 by
`(21,351,155)` (height 7371). So that point has formal `ck_min≤7371` for
every `x*_7`. The certificates `(7,3,11)`, `(7,3,23)` hold at **every**
point with `11|N`, `23|N` there, i.e. `x*_{11}≡±1 (11)` resp. `x*_{23}≡±1 (23)` (as `252≡−1` mod 11 and 23) — they
can only be avoided by moving `x*_{11}`, `x*_{23}`.

### 2.1 The {2,7}-generic points (x*_q = 1 for q ≠ 2,7)

At such points `N=1+4ck²` is an honest integer at every `q≠2,7`, and
`2∤N`, `7∤N` (for `7|c`). So a certificate is an honest divisor
`F|1+4ck²` with `F≡−1 (mod m')`, where `m'` is the part of `ck` prime to
14, together with the **box** condition

```
x*_2 ≡ −F (mod 2^{v_2(4ck)}),     x*_7 ≡ −F (mod 7^{v_7(ck)}).
```

**Lemma 2.4 (rigid parametrisation; PROVED).** Write `c=2^α7^a c'`,
`k=2^γ7^b k'` (`c'k'` prime to 14, a odd), `m'=c'k'`,
`Λ=2^{2+α+2γ}7^{a+2b}`. The certificates at a {2,7}-generic point with
these exponents correspond bijectively to integer tuples
`(c',J,J',u)`, `J,J',u≥1`, with

```
c'·J·J' − u = Λ,      u | J + J',      k' := (J+J')/u,       (2.1)
```

and `c'k'` prime to 14, `F=m'J−1` with `(F,14)=1`. The cofactor is
`e=m'J'−1`. *Proof.* `F≡−1 (m')` and `Fe=1+4ck²≡1 (m')` give
`e≡−1 (m')`. Write `F=m'J−1`, `e=m'J'−1`, `J,J'≥1` (`F,e>0`). Then
`Fe=1+4ck²` ⟺ `m'JJ'−J−J'=4ck²/m'=Λk'`. Reducing mod `k'` gives
`k'|J+J'`; with `J+J'=k'u` we get (2.1). Conversely (2.1) gives back
`Fe=1+4ck²`. ∎

**Corollary 2.5 (finiteness per level; PROVED).** For fixed `(α,γ,a,b)`
there are finitely many certificates, all with `u≤Λ+4`. *Proof.* If
`c'≥2`: `u≤J+J'≤JJ'+1≤(Λ+u)/2+1`, so `u≤Λ+2`. If `c'=1` and
`min(J,J')=1`, say `J=1`: `u|1+J'=1+Λ+u`, so `u|Λ+1`. If `c'=1`,
`J,J'≥2`: `J+J'≤JJ'/2+2`, so `u≤Λ+4`. Then `c'JJ'=Λ+u` is bounded. ∎

So for {2,7}-generic points every certificate is a box of measure
`2^{−(2+α+γ)}7^{−(a+b)}` in `ℤ_2×ℤ_7`, with finitely many boxes per
level. Whether a sterile point exists is a question about the union of
these boxes (§2.2).

### 2.2 Numerics: the {2,7}-generic sterile set (EVIDENCE)

`typei2_s27 Λmax` enumerates via (2.1) **all** certificates with
`Λ≤Λmax` (complete by Cor. 2.5). `typei2_union.py` computes the exact
Haar measure of the union of their boxes inside
`Σ'={x_2≡1 (8)}×{x_7 non-square}` (normalised to 1):

| Λmax | boxes in Σ' | covered | uncovered |
|---|---|---|---|
| 10³ | 10 | 0.833333 | 0.166667 (one cell: `x_2≡9 (16)`, `x_7≡6 (7)`) |
| 10⁴ | 66 | 0.976190 | 0.023810 (one cell: `x_2≡9 (16)`, `x_7≡48 (49)`) |
| 10⁵ | 262 | 0.979167 | 0.020833 |
| 10⁶ | 678 | 0.985119 | 0.014881 |
| 3·10⁶ | 1296 | 0.986713 | 0.013287 |
| 3·10⁷ | 3710 | 0.989226 | 0.010774 |
| 3·10⁸ | 8176 | 0.989749 | 0.010251 |

The uncovered measure decreases ever more slowly (decrements per
decade ≈ 0.0025, 0.0005). This suggests (EVIDENCE only) that a set of
positive measure ≈0.01 of `Σ'` consists of sterile points. But the sum of
**all** box measures per decade of Λ stays large (≈0.4 at Λ≈10⁶). So the
union bound alone cannot prove this; the overlaps matter.

**Integral points.** Among the 1976 points `(x_2,x_7)=(w,z)`, `w≡9 (16)`,
`|w|≤200`, `|z|≤60` non-square mod 7, exactly 26 are uncovered by all
certificates with `Λ≤3·10⁸`. **All 26 have `z=−1`** (e.g. `w=9, −7, 25, 41`).
(`typei2_points.py`.) So `x*_7=−1` is distinguished. There the odd
components of x* are all `±1`, and every certificate is an integral object:

```
F | 1+4ck²,   F≡−1 (mod m'),   F≡+1 (mod 7^{v_7(ck)}),   F≡−w (mod 2^{v_2(4ck)}).   (2.2)
```

Candidate sterile point: **`x*=(w at 2; −1 at 7; 1 at all other q)`**, e.g.
`w=9`. A proof would need to exclude (2.2) for all slices with `7∥sf(c)`.
