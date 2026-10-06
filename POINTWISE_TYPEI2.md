# Type-I depth on `{n_p = r}`: compactness and the profinite question (task O69)

Status: checkpoint 1 (side agent O69, branch `side-agent/typei-sterile`). Review R69 (`reviews/pointwise-typei2-review.md`) found no FATAL or MAJOR defects; MINOR D1–D5 applied.

| # | statement | label |
|---|---|---|
| Thm A | `X_r` = least height of a finite Type-I covering of `Σ_r`. Then `C*(r)≤X_r` (PROVED). If no covering of height ≤X exists, then under H (finite family `𝓟_X`) there are infinitely many p with `n_p=r` and `ck_min>X`. Hence under H `C*(r)=X_r`, and `X_r=∞` ⟺ a sterile point exists (statements for `C*`, R69-D4). This closes R31-D6 / Remark 6.2(ii) | PROVED / CONDITIONAL (H) |
| L2.1–2.2, P2.3 | at points that are squares off 7: unforced ⟺ `v_7(c)` odd; certificates = 7-adic balls; the residue-one point is covered at level 1 by exactly 3 certificates | PROVED |
| L2.4, C2.5 | {2,7}-generic points: rigid parametrisation `c'JJ'−u=Λ`, `u∣J+J'`; finitely many certificates per level | PROVED |
| §2.2 | union of all certificate boxes with `Λ≤3·10⁸` leaves measure ≈0.0103 of `Σ'` uncovered (slowly decreasing); integral survivors all have `x_7=−1` | EVIDENCE |
| L3.1 | sign point `x̂_w=(w;−1;1)`, `w≡9 (16)`: no square-family certificate | PROVED |
| C3.2–3.3 | no certificate at `x̂_9` with `ck≤3·10⁹` (checker to `3·10⁹`; cross-checked to `10⁶` and `ck≤8660`; reproduced in review R69). Hence every Type-I covering of `{n_p=7}` has height `>3·10⁹`, and under H `C(7)>3·10⁹` (was ≥539). For r=23, 31, 47: `>10⁹` | CERTIFIED / CONDITIONAL (H) |
| P4.1 | sign points exist iff `r≡3 (4)`; for `r≡3 (8)` they are killed by `(r(r+1)/4,2,2r+1)`; for `r≡7 (8)` Lemma 3.1 holds | PROVED |
| §5 | near-miss mass at random `w` decays per dyadic height bin (≈0.01 at 2³⁰). Mechanism partly proved | EVIDENCE / Assessment |
| Conj 3.4 | `x̂_9` is sterile, so `C(7)=∞` under H | CONJECTURE (open) |

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
`Σ_r` is compact. A prime p is not a unit in `ℤ_p`, so for a prime p we
write `p∈Σ_r` to mean that the components of p at the primes `q≤r` (i.e.
`p mod 24∏_{ℓ≤r}ℓ`) satisfy the conditions defining `Σ_r` (R69-D1). With this
convention, by quadratic reciprocity a prime `p>r` is hard with `n_p=r` iff
`p∈Σ_r`. Moreover `p∈Cl(κ)` is the congruence condition modulo `4ckF`; it
is meaningful for every prime p.

**Lemma 0.1 (PROVED).** Let p be an odd prime and `(c,k)∈𝓑_p`. Then
`M_{c,k}(p)≥1` iff `p∈Cl(c,k,F)` for some F; the F's are exactly the target
divisors. *Proof.* A target divisor D satisfies `D|N`, `D≡−p (4ck)`, and
`(D,4ck)=1` because `(p,2ck)=1`; so `p∈Cl(c,k,D)`. Conversely
`p∈Cl(c,k,F)` means `F|p²+4ck²=N` and `F≡−p (4ck)`. ∎

So `ck_min(p)=min{ck : (c,k)∈𝓑_p, s∉{1,2,3,6}, p∈⋃_F Cl(c,k,F)}`.

A *Type-I covering of `Σ_r` of height ≤X* is a finite set of certificates
of height ≤X whose classes cover `Σ_r`. Let `X_r∈ℕ∪{∞}` be the least such
height. Put `C*(r)=limsup ck_min(p)` over hard p with `n_p=r`. Then
`C*(r)≤C(r)=sup`, and `C(r)<∞` iff `C*(r)<∞` and `ck_min(p)<∞` for the
finitely many p below any threshold beyond which `ck_min(p)≤C*(r)`. The
latter is a finite check once such a threshold is known (R69-D4). All
"iff" statements below are therefore stated for `C*`.

## 1. Closing the compactness gap of Remark 6.2(ii)

**Theorem A (PROVED (i); CONDITIONAL on H (ii)).**
(i) If `X_r<∞`, fix a covering 𝒦 of height `X_r` and let `F_max` be the
largest F occurring in 𝒦. Then `ck_min(p)≤X_r` for every hard p with
`n_p=r` and `p>max(2X_r, F_max)`. Hence `C*(r)≤X_r`.
(ii) Let X be such that no covering of height ≤X exists. Then, under
Schinzel H for an explicit finite family `𝓟_X` (§1, step 4), there are
infinitely many hard p with `n_p=r` and `ck_min(p)>X`.
(iii) Hence, under H, `C*(r)=X_r`. Moreover `X_r=∞` iff some point
`x*∈Σ_r` lies in no `Cl(κ)` at all (a *sterile point*).

*Proof of (i).* Let `M=lcm{4ckF : (c,k,F)∈𝒦}`. For a prime `p>F_max`
with `p>2X_r` and `p>r`, p is prime to every `4ck` and every F of 𝒦, hence
to M. (A prime dividing some F would never lie in that `Cl(c,k,F)`.) So
`p mod M` is the residue of a unit point of `Σ_r`, i.e. of some
`x∈Σ_r⊂Ẑ^×` with `x≡p (mod M)`. The class of `p mod M` lies in some
`Cl(κ)`, `κ∈𝒦`, because 𝒦 covers `Σ_r` and every `Cl(κ)` is defined
modulo M. Finally, for `ck≤X_r<p/2`: `p∤ck`, `k<2p/3`,
`c≤(2p+k)/4k` (as `4ck<2p`), so `(c,k)∈𝓑_p`, and Lemma 0.1 applies. ∎

*Proof of (iii) from (i), (ii).* `C*(r)≤X_r` is (i). If `X<X_r`, then no
covering of height ≤X exists, and (ii) gives `C*(r)>X`. Hence
`C*(r)≥X_r` under H. For the sterile point (R69-D5): put
`U_X=Σ_r∖⋃_{κ∈K_X}Cl(κ)`, with `K_X` the set of certificates of height
≤X. Each `U_X` is closed in the compact set `Σ_r` (the `Cl(κ)` are open),
and `U_X⊇U_{X'}` for `X≤X'`. If `X_r=∞`, then each `U_X` is nonempty.
Otherwise compactness would extract a finite subcover of height ≤X from
`{Cl(κ):κ∈K_X}`. By the finite intersection property,
`⋂_X U_X≠∅`, and any point of the intersection is sterile. Conversely, a
sterile point lies in every `U_X`, so no covering exists. ∎

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
  values `V'` and larger than `v_q(4X!)`, and put `y_q=x*_q+q^T`. Then
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
* `y_q≡x*_q (mod q^T)` with `T>v_q(4X!)≥v_q(4ck)` at perturbed q, and
  `y_q=x*_q` elsewhere; so `x*≡y≡−d (mod 4ck)`.
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
  certificate κ. Under H, `C*(7)=∞` iff `Σ_7` has a sterile point; a
sterile point gives `C(7)≥C*(7)=∞` (R69-D4). Then
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

## 3. The sign point `x̂=(w; −1; 1)` and `C(7)>3·10⁹` under H

**Definition.** For `w∈ℤ_2`, `w≡9 (16)`, let `x̂_w∈Ẑ^×` have components
`x̂_2=w`, `x̂_7=−1`, `x̂_q=1` for every prime `q∉{2,7}`. Then `x̂_w∈Σ_7`
(`w≡1 (8)`, `1` is a square mod 3, 5, and `−1` is a non-square mod 7), and
`x̂_w` satisfies Lemma 2.1. The odd components satisfy `x̂_q²=1`, so
`N_{c,k}(x̂)=1+4ck²` exactly at every odd prime. A certificate at `x̂_w` is
exactly an integer solution of (2.2) with `7∥sf(c)` (i.e. `v_7(c)` odd).

**Lemma 3.1 (square families excluded; PROVED).** At `x̂_w` there is no
certificate with `F² = 1+4ck²`.
*Proof.* Let `F²=1+4ck²`. By (2.2) `m'|F+1` and `7^{v}|F−1`. Here
`gcd(F−1,F+1)=2`, and `m'=c'k'` divides `F+1`, so `k'` is prime to `F−1`
and `k'²|F+1`. Comparing odd parts of `(F−1)(F+1)=4ck²` gives
`F+1=2^i c'k'²`, `F−1=2^j 7^{s}`, with `s=a+2b` odd, `i+j=2+α+2γ` and
`min(i,j)=1`.
* `j=1`: `2^{i−1}c'k'²=1+7^s`. For odd s, `v_2(1+7^s)=3`, so `i=4`,
  `α+2γ=3` and `α+γ≥2`. Hence the 2-adic modulus is `2^{2+α+γ}≥16`, and
  `−F=−1−2·7^s≡1 (16)` (as `7^s≡7 (16)`). But `w≡9 (16)`.
* `i=j=1`: then `α=γ=0` and `c'k'²=1+7^s` is even, but `c'k'` is odd.
* `i=1`, `j≥2`: `F=1+2^j7^s`, with `j=1+α+2γ`. If `γ≥1`, then
  `j≥2+α+γ`, so `−F≡−1 (mod 2^{2+α+γ})`, and `w≡−1 (8)` is impossible. If
  `γ=0`, then `c'k'²−1=2^{α}7^s` with `c'k'` odd. This forces `α≥1`; then
  modulo `2^{2+α}` we get `−F≡−1+2^{1+α}`, which is not `≡1 (8)` for
  `α≥1`.

So no square certificate exists. ∎

**Computation 3.2 (CERTIFIED: one engine to `3·10⁹`, cross-checked by two
others on smaller ranges, and independently re-run to the full ranges in
review R69, `reviews/pointwise-typei2-review.md`, with identical slice
counts; R69-D3).**
* *Factorisation-free checker* `typei2_signcheck.c` (`r w X`). For each
  slice with `ck≤X` and `v_7(c)` odd it builds the target class ξ mod `4ck`
  by CRT. Since `N=1+4ck²≡1 (mod 4ck)`, the cofactor of a certificate lies
  in the class `ξ^{−1}`. So it suffices to test the `D≤√N` in the classes
  `ξ` and `ξ^{−1}`; there are about `√N/4ck<1` such D per class. This is
  complete and exact (128-bit arithmetic).
  * `signcheck 7 9 10^8`: 210 905 636 unforced slices, **0 certificates**
    (18 s). The same holds for `w=−7, 25, 41`.
  * `signcheck 7 9 3·10^9`: 7 602 614 538 unforced slices, **0
    certificates** (≈10 min).
  * `signcheck r 9 10^9` for `r=23, 31, 47` (all `≡7 (8)`): **0
    certificates** (744 701 974 / 548 469 498 / 356 411 660 slices).
  * The checker finds the expected certificates where they exist:
    `(14,2,15)` for `w=1`, `(33,2,23)` for r=11, `(95,2,39)` for r=19.
* *Factoring engine* `typei2_formal.py` (sympy; `1+4ck²<2^{64}`, where
  sympy's primality test is deterministic): `X=10⁶`, 1 533 438 slices (the
  same count), no certificate at `x̂_9` or `x̂_{−7}`.
* *Λ-enumeration* `typei2_s27 3·10⁸` (Lemma 2.4; every slice with
  `ck≤8660` has `Λ≤4(ck)²≤3·10⁸`): no box contains `x̂_9`.

**Corollary 3.3.** (i) *(CERTIFIED, by Computation 3.2)* Every finite
Type-I covering of `{n_p=7}` has height `>3·10⁹`. For `r=23, 31, 47`,
every covering of `{n_p=r}` has height `>10⁹`. (ii) *(CONDITIONAL on H
for the finite family `𝓟_X` of Theorem A, built from `x̂_9`)* there are
infinitely many hard primes with `n_p=7` and `ck_min(p)>3·10⁹`. So
`C(7)>3·10⁹`, up from `≥539` (Cor 6.4 of POINTWISE_TYPEI). Likewise,
under H, `C(r)>10⁹` for `r=23, 31, 47`.
*Proof.* (i) A covering of height `≤3·10⁹` would contain `x̂_9`, but no
certificate holds there. (ii) Apply Theorem A(ii), Steps 2–5, with
`x*=x̂_9`. Step 1 holds for all of `K_X`: forced slices carry no
certificate at `x̂_9` (Lemma 2.1), and Computation 3.2 covers the slices with
`v_7(c)` odd. We apply Theorem A verbatim, with `𝓟_X` built from all of `𝓢`
(R69-D2). An optional reduction drops the forced slices. On the class `𝒞`,
`p≡x̂ (mod 8∏_{q≤B}q)`, and every prime of s is `≤X≤B`. So
`χ_s(p)=χ_s(x̂)=1` for `v_7(c)` even, and `M_{c,k}(p)=0` by notes
Thm 48.1. Hence the ≈7.6·10⁹ polynomials for the slices with `v_7(c)` odd
(together with `f_0`) already suffice. ∎

**Conjecture 3.4.** `x̂_9` is sterile. Then, under H, `C*(7)=∞` (hence
`C(7)=∞`; Theorem A(iii)).

## 4. Other r: the sign point exists iff r≡3 (4), survives only if r≡7 (8)

For a prime `r≥7` define `x̂^{(r)}_w` by `x̂_2=w` (`w≡9 (16)`), `x̂_r=−1`,
`x̂_q=1` otherwise. It lies in `Σ_r` iff `−1` is a non-square mod r, i.e.
`r≡3 (4)`. Lemma 2.1 holds verbatim (unforced ⟺ `v_r(c)` odd), and the odd
components square to 1, so certificates are the integer solutions of (2.2)
with 7 replaced by r.

**Proposition 4.1 (PROVED).**
(i) If `r≡3 (8)`, then `(c,k,F)=(r(r+1)/4, 2, 2r+1)` is a certificate at
every `x̂^{(r)}_w`, for every `w`, and indeed at every `x∈Σ_r` with
`x_r≡−1 (r)`, `x_q≡1` (to sufficient q-adic precision) at the primes q of `(r+1)/4` and of `2r+1`. So the
sign point fails, with height `r(r+1)/2` (r=11: 66; r=19: 190, matching
`typei2_formal.py`).
(ii) If `r≡7 (8)`, Lemma 3.1 holds for `x̂^{(r)}_w` (no square
certificates).
*Proof.* (i) `c=r·(r+1)/4` with `(r+1)/4` odd and prime to r, `k=2`; so
`v_r(c)=1` and the slice is unforced. `1+4ck²=1+4r(r+1)=(2r+1)²`.
Target: `4ck=2r(r+1)`, whose 2-part is 8 (as `r+1≡4 (8)`).
`F=2r+1≡1 (r)`, `≡−1 (mod (r+1)/4)`, and `−F=−2r−1≡−7≡1 (8)` since
`r≡3 (8)`. These match `x_r=−1`, `x=1`, `x_2≡1 (8)`.
(ii) The proof of Lemma 3.1 used only `v_2(1+r^s)≥3` for odd s (true iff
`r≡7 (8)`), and `−1−2r^s≡1 (16)`. The latter holds since `r^s≡r (16)`
(as `r²≡1 (16)`) and `−1−2r≡1 (16)` for `r≡7,15 (16)`. ∎

**Remarks.**
* For `r≡1 (4)` (e.g. `r=5`, where `C(5)=10`), no sign point exists: the
  only units whose square is 1 are `±1`, and both are squares mod r. This
  is suggestive. The sign mechanism is unavailable exactly when a finite
  covering is known (r=5). Whether `C(13)<∞` is open (task suggestion: a
  covering search for r=13).
* For `r≡3 (8)`, other (non-sign) deep points exist, e.g. the r=11 point
  of POINTWISE_TYPEI Cor 6.4 (`ck_min>3000`).

## 5. Why the sign point survives: near-miss statistics (EVIDENCE / Assessment)

A *near miss* at the sign point is `(c,k,F)` with `v_7(c)` odd,
`F|1+4ck²`, `F≡−1 (mod m')` and `F≡1 (mod 7^{v})`. It satisfies every
condition of (2.2) except the 2-adic one. It is a certificate at `x̂_w`
iff `w≡−F (mod 2^t)`, `t=v_2(4ck)`. So for Haar-random `w∈9+16ℤ_2`, the
expected number of certificates in a height range is the sum of `2^{4−t}`
over the near misses there with `−F≡9 (16)` and `t≥4`
(`typei2_nearmiss.c`, factorisation-free like the checker; X=2·10⁹, 4 min):

| ck in | near misses | in 9+16ℤ₂ | Σ2^{4−t} |
|---|---|---|---|
| [2¹⁰,2¹¹) | 62 | 2 | 0.125 |
| [2¹⁴,2¹⁵) | 154 | 8 | 0.070 |
| [2¹⁸,2¹⁹) | 329 | 20 | 0.083 |
| [2²²,2²³) | 597 | 42 | 0.024 |
| [2²⁶,2²⁷) | 1003 | 82 | 0.021 |
| [2²⁸,2²⁹) | 1232 | 106 | 0.009 |
| [2²⁹,2³⁰) | 1373 | 124 | 0.009 |

Cumulative ≈1.01 up to `2³¹`; below `2¹⁰` there is nothing. The
near-miss count grows (≈ `ck^{0.37}`), but the 2-adic weight decays faster.
**Observed mechanism:** near misses with `−F≡1 (8)` occur only with a deep
2-part. Apart from the square family `(α,γ)=(1,1)`, which gives `−F≡1 (16)`
(Lemma 3.1), they need `t=v_2(4ck)≥6`. Those with `−F≡9 (16)` need
`t≥8` in the data (`ck≤3·10⁷`). Partial explanation (PROVED): if
`t≥3` and `F≡7 (8)`, then `e=N/F≡7 (8)` too, since `Fe≡1 (2^T)`. So `F≡e (mod 8n)`,
n the odd part of ck. Then either `F=e` (square family, excluded by
Lemma 3.1), or `|F−e|≥8n`, which forces `min(F,e)≤N/(8n)≈2^{α+2γ−1}k_o`
(`k_o` the odd part of k). Hence a non-square near miss in `7+8ℤ` needs a
divisor of N in the class `ε (mod n)` below `2^{α+2γ−1}k_o`. That is rare
unless the 2-part `2^{α+2γ}` is large, and then the 2-adic weight
`2^{4−t}` is small.

*Assessment.* If the per-bin mass keeps decaying geometrically (ratio ≈
0.85 per doubling over the last 8 bins), the expected number of
certificates at a random `w∈9+16ℤ_2` above `2³¹` is `≈0.1`. Then a set of
`w` of positive measure, and plausibly `w=9`, is sterile. If instead the
mass decays only like `1/log`, a.e. `w` is eventually covered. The data
cannot exclude this. Even then, exceptional sterile `w` might exist, and
by compactness this is exactly the question `C(7)=∞` vs `<∞` under H.
**Neither is proved.** Proving the decay would need an upper bound for
divisors of `1+4ck²` in a fixed class `ε (mod n)` below
`≈2^{α+2γ}k_o`, uniform in the slice. That is a divisor-in-short-ranges
problem of the type in POINTWISE_TYPEI §4.2.

## Replay

```
gcc -O2 -o /tmp/signcheck scripts/typei2_signcheck.c -lm
/tmp/signcheck 7 9 100000000            # C3.2: 0 certificates, 18 s
/tmp/signcheck 7 9 3000000000           # C3.2: 0 certificates, ~10 min
/tmp/signcheck 7 1 1000; /tmp/signcheck 11 9 1000; /tmp/signcheck 19 9 1000   # sanity: (14,2,15), (33,2,23), (95,2,39)
for r in 23 31 47; do /tmp/signcheck $r 9 1000000000; done                    # §4: 0 certificates each
cd scripts
PYTHONPATH=. uv run python typei2_formal.py 600 1 2:25:14 3:7:9 7:6:6          # reproduces 539 (POINTWISE_TYPEI Cor 6.4)
PYTHONPATH=. uv run python typei2_formal.py 1000000 1 2:9:80 7:$(python3 -c 'print(7**60-1)'):60   # C3.2 second engine (~10 min)
PYTHONPATH=. uv run python typei2_balls.py 20000 3 1 2:25:14 3:7:9           # §2: (21,351,155) kills x_7=6
PYTHONPATH=. uv run python typei2_balls.py 3000 4 1                           # P2.3: 3 level-1 balls
gcc -O2 -o /tmp/typei2_s27 typei2_s27.c && /tmp/typei2_s27 300000000 > /tmp/s27_3e8.txt   # ~8 min
PYTHONPATH=. uv run python typei2_union.py /tmp/s27_3e8.txt 300000000         # §2.2 table
PYTHONPATH=. uv run python typei2_points.py /tmp/s27_3e8.txt                  # §2.2 integral points
gcc -O2 -o /tmp/nearmiss typei2_nearmiss.c -lm && /tmp/nearmiss 7 2000000000  # §5 table (~4 min)
```
