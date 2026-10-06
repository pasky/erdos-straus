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
