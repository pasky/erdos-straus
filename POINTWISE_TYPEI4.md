# Higher reciprocity / Pell structure at the sign point `x̂_9` (task O89)

Status: work in progress (side agent O89, branch `side-agent/redei-sign-point`). Not reviewed.
Builds on POINTWISE_TYPEI2.md (Theorem A, (2.2), Lemma 3.1, Conj 3.4) and POINTWISE_TYPEI3.md
(Lemma 1.1, Cor 5.2, Props 5.3–5.5: certificates at `x̂_w`, `w≡9 (16)`, need level `L:=α+2γ≥7`).

Notation as in TYPEI3: certificate `(c,k,F)` at `x̂_w`, `e=N/F`, `N=1+4ck²`,
`c=2^α7^a c'`, `k=2^γ7^b k'` (`a` odd, `c'k'` odd and prime to 7), `c_o=7^a c'`, `k_o=7^b k'`,
`n=c_ok_o`, `t=2+α+γ`, `L=α+2γ`. The **fibre** is `Φ={x̂_w : w≡9 (16)}`.

## 1. Fibre certificates are norm-one units of a Pell order (PROVED)

**Lemma 1.1 (fibre certificates).** Fix `L≥5`. The following are equivalent for `(c,k,F)` with
`v_7(c)` odd and `α+2γ=L`:
(i) `(c,k,F)` is a near miss (TYPEI2 §5: `F|N`, `F≡−1 (mod c'k')`, `F≡1 (mod 7^{a+b})`) with
`F≡7 (mod 16)` and `t≥5`; equivalently, `(c,k,F)` is a certificate at `x̂_w` for some `w≡9 (16)`
(namely every `w≡−F (mod 2^t)`).
(ii) Writing `e=N/F`, `δ:=(e−F)/16n` is an odd integer (possibly negative).
(Under (i) the cofactor `e` automatically satisfies `e≡−w^{−1} (mod 2^t)`.)

*Proof.* (i)⇒(ii): Lemma 1.1 of TYPEI3 gives `e≡F (mod n)` (both `≡−1` mod `c'k'`, `≡1` mod `7^{a+b}`), and
`e≡F^{−1} (mod 2^{t+γ})` with `t+γ≥5`; `F≡7 (16)` gives `F^{−1}≡F+16 (mod 32)` (`7·23≡1`, `23·7≡1` mod 32).
So `v_2(e−F)=4`, `16n | e−F`, quotient odd. (ii)⇒(i): if δ is odd then `e≢F (mod 32)`; since `F≡7 (8)`
(near misses in the dump have `−F≡1 (8)`) this forces `F≡7 (16)`. For `L≥7`, `t=2+α+γ≥2+⌈L/2⌉≥6`.
The converse direction of TYPEI3 Lemma 1.1 then gives a certificate at every `w≡−F (mod 2^t)`. ∎

**Proposition 1.2 (Pell form; PROVED).** Let `(c,k,F)` be a fibre certificate of level `L≥5`, oriented
so that `δ>0` (swap `F,e` otherwise). Put
`M:=c_oδ²+2^{L−4}`, `d:=c_oM`, `A:=(F+e)/2`. Then
`A²−d·(8k_o)²=1`, `A≡−1 (mod 32)`, and
`A+1=32·P·X²`, `A−1=2·Q·Y²` with `P=c'P_1`, `Q=7^aQ_1`, `P_1Q_1=M`, `X=k'`, `Y=7^b`. Equivalently:

```
16·P·X² − Q·Y² = 1,     P·Q = c_o(c_oδ²+2^{L−4}),     c'|P, 7^a‖Q, Y=7^b, X=k'.     (1.1)
```

Conversely every solution of (1.1) in positive integers with `δ` odd, `a` odd, `7∤c'X`, gives a
fibre certificate `c=2^α c_o, k=2^γ k_o` for each split `α+2γ=L` (with `F=A−8nδ`, `e=A+8nδ`,
`A=2QY²+1`, `k_o=XY`).
*Proof.* `A²−(e−F)²/4=Fe=1+4ck²` and `(e−F)/2=8nδ`; `4ck²=2^{L+2}c_ok_o²`, so
`A²=1+64k_o²(c_o2^{L−4}+c_o²δ²)=1+64dk_o²`. Mod 32: `F≡7, e≡23` or vice versa, so `F+e≡30 (32)`
and `A≡15 (16)`; so `v_2(A−1)=1` and `v_2(A+1)=5` because `(A+1)(A−1)=64dk_o²` with `d,k_o` odd
(`d≡c_o²δ²` mod 2). The odd parts: `gcd(A+1,A−1)=2`; `c'k'|F+1` and `F≡A (mod n)` (as `F=A−8nδ`)
give `c'k'|A+1`, hence `k'²|A+1` (k' is prime to `A−1`); `7^{a+b}|A−1` similarly gives `7^{a+2b}|A−1`.
`M` is prime to `c_o` and split between the two factors arbitrarily; `M` is prime to 7 (`M≡2^{L−4}` mod 7).
Comparing odd parts gives the stated shapes; (1.1) is `(A+1)/2−(A−1)/2=1`, divided appropriately.
Converse: `ε:=(4X√P+Y√Q)²=A+8XY√d` with `A=16PX²+QY²=2QY²+1`, and `A²−64dX²Y²=N(ε)=1`.
Then `F,e=A∓8nδ` satisfy `Fe=A²−64n²δ²=1+64k_o²(d−c_o²δ²)=1+2^{L+2}c_ok_o²`. The congruences:
`F≡A≡−1 (mod c'k')` since `c'k'²|P X²|A+1`, `F≡A≡1 (mod 7^{a+b})` since `7^{a+2b}|A−1`, and
`F≡A−8≡7 (mod 16)` as `A≡−1 (32)` and `nδ` odd. ∎

*Remarks.* (a) The sign conditions of (2.2) (`−1` at `c'k'`, `+1` at 7) are **built into** the
factorisation `(A+1)(A−1)`: (1.1) is the classical "Legendre/Dirichlet square root" `ε=ζ²`,
`ζ=4X√P+Y√Q` of the unit `ε`. (b) For `L≥7`: `d≡c_o²δ²≡1 (mod 8)`, so 2 **splits** in `Q(√d)`; for
`L=5,6` it ramifies resp. stays inert. And `d=(c_oδ)²+2^{L−4}c_o` is of Richaud–Degert type
(`r|4c_oδ`) exactly when `L≤6` — which is why the descent of TYPEI3 §5 stays in ℤ for `L≤6` only.
Checked: `scripts/typei4_pell.py` on all 461 oriented non-square near misses of `typei3_nmdump 7 9 10⁸`
(`A²−d(8k_o)²=1` in all cases).

**Observation 1.3 (EVIDENCE).** In the dump `ck≤10⁸`, the fibre certificates (δ odd) occur only at
levels `L ∈ {11,13,14,16,18,19,…}` — none at `L=7,8,9,10,12`. The 34 "level-7 near misses" of TYPEI3
Remark 5.6 all have δ even (`F≡15 (16)`); they are not fibre certificates at all.

**Corollary 1.4 (the reduced equation; PROVED).** With `P=c'P_1`, `X=k'`, `D:=7^{a+b}δ`, (1.1) is
equivalent to

```
c'·g·h − P_1 = K:=2^{L−4}·7^{a+2b},    g:=4P_1X−D,  h:=4P_1X+D,                     (1.2)
```

with `a` odd, `b≥0`, and `c',P_1,X,δ` odd positive, `7∤c'P_1X`.
*Proof.* (1.2) reads `16c'P_1²X²−c'D²−P_1=K`, i.e. `P_1(16c'X²P_1−1)=7^{a+2b}(c_oδ²+2^{L−4})=7^{a+2b}M`.
As `7∤P_1`, `Q_1:=(16c'X²P_1−1)/7^{a+2b}` is an integer, `P_1Q_1=M`, which is (1.1). Conversely (1.1)⇒(1.2)
by the same computation. ∎
Note `g>0` (as `c'gh=P_1+K>0`, `h>0`), so `h≥8P_1X−g`… and `4c'gP_1<c'gh=P_1+K`; hence for fixed
`(L,a,b)` the solutions are finitely many and enumerable: `(4c'g−1)P_1<K` and `h(8c'g−1)≤8K+g`
(from `g+h=8P_1X≥8P_1=8(c'gh−K)`). This is TYPEI2 Cor 2.5 in the present coordinates.

**Observation 1.5 (EVIDENCE).** All fibre certificates found so far (`typei4_pqsearch 3·10⁵ 10⁴`, 87 solutions;
`typei4_dgraded.py 5 24 3000`) use the **fundamental** unit (`m=1`), have `a=1`, `b≤1`, and level `L≥11`.
Levels 12, 15, 17 are also absent so far.

**Remark 1.6 (dictionary).** (1.2) is TYPEI2 Lemma 2.4 / (2.1) in disguise: `F=8c'Xg−1`, `e=8c'Xh−1`
(so `J=8g`, `J'=8h`, `u=64P_1`), and `(8c'Xg−1)(8c'Xh−1)=1+2^{L+2}c'7^sX²` with `s=a+2b`. Hence the fibre
problem at level `L` is simply: **does `N=1+2^{L+2}c'7^sX²` (`s` odd; `c',X` odd, prime to 7) have a divisor
`F≡7 (mod 16)` with `F≡−1 (mod c'X)` and `F≡1 (mod 7^{(s+1)/2})`?** (`a=1`, `b=(s−1)/2` is the weakest split;
`F≡7 (16)` already forces `e≡F^{−1}≢F (mod 32)`, i.e. δ odd.)

## 2. Computation: the low levels are empty for small `s` (CERTIFIED once replayed)

**Computation 2.1.** `scripts/typei4_level.c L s` enumerates **all** solutions of (1.2) with given `(L,s)`,
at all heights (all `c'`, `X`), using the bounds of Cor 1.4. Cross-check: it reproduces exactly the
`L=11,13,14,16` solutions found by the independent engines `typei4_pqsearch.c` and `typei4_dgraded.py`
(`(L,s)=(11,1)`: `(c',P_1,X,δ)=(3,13,1,7)`; `(13,3)`: `(79,1,17,1)`; `(14,1)`: 2; `(16,1)`: 3).
Result: **no fibre certificate** for `L∈{7,8,9,10,12,15}` and `s∈{1,3,5,7,9}`, nor for `L=17`, `s≤7`
(each run < 1 min except `L=15,s=9`). So: *no certificate at any `x̂_w`, `w≡9 (16)`, with
`α+2γ∈{7,8,9,10,12,15}` and `v_7(ck²)≤9`, of any height.*

## 3. Fixed 7-depth `b`: a finite problem per `(L,b)`; `b=0` closes levels 7–10 (PROVED)

Put `T:=2^{L−4}`, `y:=c'gδ`, `z:=T7^b−y`, `D=7^{a+b}δ`.

**Lemma 3.1 (PROVED).** Every solution of (1.2) satisfies
(i) `y<T·7^b`; (ii) `P_1(4c'gX−1)=7^{a+b}z`, hence `P_1 | z`; (iii) `P_1=c'g²+7^{a+b}(2y−T7^b)`;
(iv) `7^a<T/2` if `2y>T7^b`, and `7^a<T²7^b/4` if `2y<T7^b` (`2y≠T7^b` as y is odd and `L≥5`).
*Proof.* `h=4P_1X+D=g+2D`. (1.2) gives `4c'gP_1X+c'gD=P_1+K`, i.e. `K−c'gD=P_1(4c'gX−1)≥3P_1>0`; with
`K−c'gD=7^{a+b}(T7^b−y)` this is (i), (ii), and `7∤P_1` gives `P_1|z`. (iii) is `P_1=c'g(g+2D)−K`.
(iv) If `2y>T7^b`, (iii) gives `P_1>7^{a+b}`, while `P_1≤z<T7^b/2`. If `2y<T7^b`, `P_1≥1` gives
`7^{a+b}≤7^{a+b}(T7^b−2y)<c'g²≤(c'g)²≤y²<T²7^{2b}/4`. ∎

**Corollary 3.2 (PROVED).** For fixed `(L,b)` the fibre certificates of level `L` with `v_7(k)=b` are finitely
many and are found by the finite search: `y<T7^b` odd, `y=c'gδ`, `a` odd with (iv), `P_1` from (iii) with
`1≤P_1`, `P_1|z`, `7∤P_1`, and `X=(1+7^{a+b}z/P_1)/(4c'g)` an odd integer prime to 7.

**Proposition 3.3 (`b=0`, `L=7`, by hand; PROVED).** `T=8`, so `7^a<16` (both cases), `a=1`, `y∈{1,3,5,7}`.
`y=5,7`: `2y>8` and `P_1=c'g²+7(2y−8)≥15>z=8−y`. `y=1,3`: `P_1=c'g²−7(8−2y)≤y²−14(4−y)<0`. No solution.
So no certificate at any `x̂_w` (`w≡9 (16)`) has `α+2γ=7` and `7∤k`. ∎
