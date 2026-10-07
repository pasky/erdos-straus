# Higher reciprocity / Pell structure at the sign point `x̂_9` (task O89)

Status: work in progress (side agent O89, branch `side-agent/redei-sign-point`). Not reviewed.
Builds on POINTWISE_TYPEI2.md (Theorem A, (2.2), Lemma 3.1, Conj 3.4) and POINTWISE_TYPEI3.md
(Lemma 1.1, Cor 5.2, Props 5.3–5.5: certificates at `x̂_w`, `w≡9 (16)`, need level `L:=α+2γ≥7`).

Notation as in TYPEI3: certificate `(c,k,F)` at `x̂_w`, `e=N/F`, `N=1+4ck²`,
`c=2^α7^a c'`, `k=2^γ7^b k'` (`a` odd, `c'k'` odd and prime to 7), `c_o=7^a c'`, `k_o=7^b k'`,
`n=c_ok_o`, `t=2+α+γ`, `L=α+2γ`. The **fibre** is `Φ={x̂_w : w≡9 (16)}`.

## 1. Fibre certificates are norm-one units of a Pell order (PROVED)

**Lemma 1.1 (fibre certificates; PROVED).** Let `(c,k,F)` have `v_7(c)` odd and level `L=α+2γ≥7` (so
`t=2+α+γ≥2+⌈L/2⌉≥6`), and let it be a near miss (TYPEI2 §5: `F|N`, `F≡−1 (mod c'k')`, `F≡1 (mod 7^{a+b})`).
Call it a **fibre certificate** if `F≡7 (mod 16)`. Then:
(i) it is a fibre certificate iff it is a certificate at `x̂_w` for some `w≡9 (16)` (namely every `w≡−F (mod 2^t)`);
(ii) if it is a fibre certificate, then `e=N/F` satisfies `e≡F (mod n)`, `v_2(e−F)=4`, so
`δ:=(e−F)/16n` is an odd integer (possibly negative). Conversely `δ` odd forces `F≡7` or `9 (mod 16)`.
*Proof.* (i) A certificate at `x̂_w` has `F≡−w (mod 2^t)` with `t≥6`; for `w≡9 (16)` that is `F≡7 (16)`.
Conversely, if `F≡7 (16)` put `w:=−F` (or any `w≡−F (mod 2^t)`); then `w≡9 (16)` and the converse part of
TYPEI3 Lemma 1.1 applies. (ii) TYPEI3 Lemma 1.1 gives `e≡F (mod n)` (both `≡−1` mod `c'k'`, `≡1` mod `7^{a+b}`),
and `e≡F^{−1} (mod 2^{L+2})`. For odd `F`, `F^{−1}≡F+16 (mod 32)` iff `F²≡17 (mod 32)` iff `F≡7,9 (mod 16)`;
otherwise `F²≡1 (32)`. ∎
(The case `F≡9 (16)` belongs to the fibre `w≡7 (16)` and is not considered further.)

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

**Computation 3.4 (CERTIFIED once replayed; complete per `(L,b)`, all `a`, all heights).**
`scripts/typei4_lb.c L b` implements Cor 3.2 (each solution re-verified by the identity `Fe=1+2^{L+2}c'7^{a+2b}X²`
in 128-bit arithmetic). It reproduces exactly the solutions of `typei4_level` / `typei4_pqsearch` for
`L=11,13,14,16`, `b≤1`.
* `L∈{7,8,9,10}`, `b≤7`: **0 solutions** (40 s for `b=6,7`).
* `L=11…22`, `b≤3`: fibre certificates exist exactly for
  `(L,b)=(11,0),(13,1),(14,0)×2,(14,3),(16,0)×3,(18,0),(18,1),(19,0)×2,(20,0)×4,(21,0),(22,1)×2`;
  none at `L=12,15,17` (b≤3).
* `L=23…26`, `b≤1`, and `L=23,24`, `b=2`: 6+0, 2+1, 3+2, 3+0, 0, 0 solutions; `max(v_2(F+9),v_2(e+9))≤10`
  throughout (`≤8` for `L≤25`).

| L | b | (c',g,δ,P₁,X) | F | e | v₂(F+9) | v₂(e+9) | t_min=2+⌈L/2⌉ |
|---|---|---|---|---|---|---|---|
| 11 | 0 | (3,3,7,13,1) | 71 | 2423 | 4 | 7 | 8 |
| 13 | 1 | (79,19,1,1,17) | 204135 | 1257047 | 4 | 5 | 9 |
| 14 | 0 | (101,1,5,3,3) / (3,1,173,101,3) | 2423 / 71 | 172103 / 174455 | 7 / 4 | 4 / 7 | 9 |
| 14 | 3 | — | 281104279 | 49335587512359 | 5 | 4 | 9 |
| 16 | 0 | three | 5335, 9479, 11159 | 7911, 14519, 66599 | ≤5 | ≤6 | 10 |
| 18–22 | | eleven | | | ≤8 | ≤6 | 11–13 |

**Corollary 3.5 (CERTIFIED; new type of bound — unbounded height).** No certificate at `x̂_9` has
(`α+2γ≤10` and `v_7(k)≤7`) or (`α+2γ≤22` and `v_7(k)≤3`) or (`α+2γ≤24`, `v_7(k)≤2`) or
(`α+2γ≤26`, `v_7(k)≤1`), **at any height** `c,k` and for any `v_7(c)`.
*Proof.* A certificate at `x̂_9` is a fibre certificate (Lemma 1.1) with, for the divisor in the F-role,
`v_2(F+9)≥t≥2+⌈L/2⌉` (as `γ≤L/2`). Levels `≤6` are empty by TYPEI3 §5. In the complete lists of Comp 3.4,
`max(v_2(F+9),v_2(e+9))<2+⌈L/2⌉` in every case (the role of `e` is covered by `v_2(e+9)`, since `F`/`e` is
symmetric in (1.2) up to orientation). ∎
For `b=0` (i.e. `7∤k`) at `L≤10` this is a finite hand-checkable statement (Lemma 3.1(iv): `a=1` only, as
`7^a<T²/4≤2^{12}` gives `a≤3`, and `a=3` needs `7³<T²/4`, i.e. `L=10` only).

**Example (level 11 is genuinely inhabited in the fibre).** `(c,k,F)=(42,32,71)`: `N=172033=71·2423`, `t=8`,
`c'=3`, `71≡−1 (3)`, `71≡1 (7)`; it is a certificate at `x̂_w` for every `w≡185 (mod 256)`
(`typei3_verify.py 7 185 42 32 71`: CERTIFICATE), but not at `w=9` (`v_2(71+9)=4`).

### 3.6 The 7-adic tower at `L=7`: bounded `b` for each fixed gap `j` (PROVED)

At `L=7` (`T=8`) case A of Lemma 3.1(iv) is impossible (`7^a<4`), so `2y<8·7^b`. Put `u:=7^b`,
`j:=4u−y` (odd, `1≤j<4u`), `m:=c'δ²` (odd), `ρ:=z/P_1=(4u+j)/P_1`. Since `c'g²=y²/m`, Lemma 3.1(iii) reads
`mP_1=y²−2mj7^au`, hence

```
ρ·[(4u−j)² − 2mj·7^a·u] = m(4u+j),        m·j·7^a < 8u.                                  (3.1)
```

**Lemma 3.6 (PROVED).** Let `L=7` and `7∤j`. Then `λ:=(ρj−m)/u` is an even integer, `2≤λ≤4j+j²/u`, and
`u(16ρ+4λ)=j(12ρ+2·7^aρm−λ)` (3.2). Moreover `7^{b−a}<2λj³+10j²+37j`, `m<8·7^{b−a}/j`, and `u` is a root
of the non-zero quadratic
`(2jm−16·7^{e})λu² + (2jm²−16·7^e m+8·7^eλj)u + 7^e(12jm−λj²) = 0`, `e:=b−a`. Hence **for each fixed `j`
(prime to 7) only finitely many `b` occur, with an explicit bound.**
*Proof.* (3.1) mod `u` gives `ρj²≡mj`, so `ρj≡m (mod u)` and `λ∈ℤ`. Substituting `m=ρj−λu` into (3.1) and
dividing by `u` gives (3.2). LHS of (3.2) is even and `j` odd, so `λ` is even. `λ>−m/u>−1` (by (3.1),
`m<8u/7`), so `λ≥0`. `λ=0`: (3.2) gives `8u=j(6+7^am)`; for `b≥1` this needs `7|6`; for `b=0`, `j≤3` and
`8=j(6+7^am)` fails. `λ≤ρj/u≤(4u+j)j/u` as `P_1≥1`. Write (3.2) as `Dd | Nn` with `Dd=A_1ρ+4λ`,
`A_1=2·7^aλj+16`, `Nn=2·7^aj²ρ²+12jρ−λj`. Then `A_1²Nn ≡ C (mod Dd)` with
`C=−λj(4·49^aλ²j²+128·7^aλj+1024)≠0`, so `A_1ρ<|C|`, i.e. `ρ<2·7^aλ²j²+64λj+512/7^a`, and
`u<ρj/λ` gives the bound on `7^{b−a}`. `m<8·7^{b−a}/j` is (3.1). Multiplying (3.2) by `j7^e` and using
`jρ=m+λu`, `7^a7^e=u` gives the quadratic. Its leading coefficient vanishes only if `jm=8·7^e`, which is
impossible as `jm` is odd. ∎

*Examples.* For `j=1` the cases `λ∈{2,4}` reduce to `7^am=8u−5` resp. `8u=7^a+4`, both impossible mod 7. So
`j=1` is excluded for all `b` (direct check of Lemma 3.6).
*What remains at `L=7`.* By (3.1) `m·7^a<8u/j`. So large `j` forces small `m=c'δ²`, and the open regime
is `j→∞` together with `b→∞`. For fixed `(m,a,ρ)`, (3.1) is a conic in `(u,j)` of non-square discriminant
`4ρ²(μ²−16)`, `μ=m7^a+4`. Its points with `u=7^b` are finite (a non-degenerate binary recurrence meets the powers
of 7 finitely often; Baker/S-unit theory, not made explicit here). But `ρ` is not bounded in terms of `(m,a)`.
So for `L=7` the tower is reduced to the regime `j, b → ∞` with `m` bounded by `8u/(7j)`. This is not closed.
The same method applies verbatim to `L=8,9,10` (`T=16,32,64`; for `L≥8` case A of Lemma 3.1 adds `a=1` with
`P_1>7^{1+b}`), but it was not carried out.

## 4. What this says about higher reciprocity obstructions (Assessment, with one PROVED scope statement)

**Proposition 4.1 (scope; PROVED).** Any argument excluding certificates at `x̂_9` of level `L` that uses the
2-adic component only through `w mod 16` (as TYPEI3 Props 5.4, 5.5 do) fails for
`L∈{11,13,14,16,18,19,20,21,22}`. *Proof.* Comp 3.4 lists, for each such `L`, a certificate at some `x̂_{w'}`,
`w'≡9 (16)`, of level `L`; such an argument would exclude it too. ∎
So at `L≥11` the exact value `w=9` (at depth `≥t`) must enter, and for `L≤10` a fibre-uniform proof is
**not** excluded (no fibre certificate known). In the Pell picture (Prop 1.2) the `w`-dependence is the
position of the unit `ε=A+8k_o√d` at a split prime `𝔭|2` of `ℚ(√d)`: `ε_𝔭≡−w` resp. `−w^{−1} (mod 2^t)`.

**Assessment 4.2 (why residue symbols do not obviously help).**
(a) *Quadratic data are already exhausted and pass.* In (1.2) the Jacobi conditions mod `P_1`, `c'`, 7 combine (by
reciprocity, using `P=c'P_1≡7 (8)`, forced by (1.2) mod 16 for `L≥7`) to `(2/P)^L=(−1)^{(c'−1)(P_1−1)/4}`, which
holds identically. This is the Lemma 2.1 / genus test of TYPEI2 in the present coordinates.
(b) *At fixed `(L,a,b)` the problem is finite for archimedean reasons* (Lemma 3.1, Cor 3.2), so a reciprocity
obstruction has nothing to add there: the finite lists are simply computed (Comp 3.4).
(c) *Across levels the problem is exponential-Diophantine.* For fixed `(L,a,c',X,δ)`, (1.2) in the unknowns
`(P_1,b)` says `(32c'X²P_1−1)² − E·(7^b)² = 1`, `E=64c'X²7^a(c'7^aδ²+T)`: a Pell equation whose `y`-coordinate
must be a pure power of 7. By primitive divisors of the associated Lucas sequence this has `O(1)` solutions, i.e.
`b` is bounded for fixed `(L,a,c',X,δ)`. But `c'`, `δ`, `X` are not bounded uniformly in `b` (Lemma 3.1 only gives
`c'gδ<T7^b`). The natural tools for the whole tower are linear forms in logarithms (7-adic and archimedean),
not residue symbols. The same holds 2-adically for the original tower in `L`.
(d) *The 2-adic position at `x̂_9` looks random.* In the Pell picture the certificate unit is (in all 87 examples)
the **fundamental** unit `ε_d`, and the condition at `x̂_9` is `ε_d≡−9^{±1} (mod 𝔭^t)` at a split `𝔭|2`. Over the
fibre certificates with a divisor `f<10⁹` (`typei3_fsearch 7 9 1 10⁹ mass`), the 2-adic closeness
`max(v_2(f+9),v_2(9f+1))` reaches 14 (`f=212983`, ball radius `2^{−35}`), 12, 10, 10, …; no bound is visible.
If it is unbounded, no test that sees `w` only modulo a fixed `2^j` can prove sterility of `x̂_9` (TYPEI3 Prop 3.1
is the analogous statement for the odd components).
(e) Concretely tested and found uninformative: quartic symbols `(·/F)_4` are undefined/trivial since all
certificate divisors are `≡7 (16)`, i.e. `≡3 (4)`; the residue class of `−F` in `9^{ℤ_2}` modulo `2^7`
(`z≡1,3,5,7 (8)`) is hit in every class by fibre certificates (Comp 3.4 table: `v_2(F+9)=7,8` occur).

## 5. Status and open problems

* PROVED: Pell form (Prop 1.2); reduced equation (Cor 1.4, Remark 1.6); finiteness per `(L,b)` with explicit
  bounds (Lemma 3.1, Cor 3.2); `L=7`, `7∤k` by hand (Prop 3.3); scope Prop 4.1.
* CERTIFIED (once replayed): no fibre certificate at `L∈{7,8,9,10}` with `v_7(k)≤7`, nor at `L∈{12,15,17}` with
  `v_7(k)≤3`; no certificate at `x̂_9` with `L≤22`, `v_7(k)≤3` (or `L≤26`, `v_7(k)≤1`) (Cor 3.5), at any height.
* OPEN (the precise blocking point): the **7-adic tower** `b→∞` at fixed `L∈{7,…,10}`. Each `b` is a finite
  check, but for `L=7,8` already the window condition `1≤P_1≤z` of Lemma 3.1 is met by only 0–2 candidates per
  `b≤3` (`typei4_lb` instrumented), against 10–44 at `L=11`. A proof for all `b` would need a uniform bound on `b`
  (e.g. via (c) above with a bound on `c'δ` in terms of `L` alone), which we do not have.
* OPEN: whether `max v_2(f+9)` over fibre certificates is bounded (if yes, a ball around 9 in the fibre is sterile
  and `x̂_9` is sterile by a finite 2-adic test; if no, any proof must use the exact 2-adic number 9).

## Replay

```
gcc -O2 -o /tmp/nmdump scripts/typei3_nmdump.c -lm && /tmp/nmdump 7 9 100000000 > /tmp/nm8.txt   # 8 s
uv run --with sympy python scripts/typei4_pell.py /tmp/nm8.txt 5 | tail -1    # Prop 1.2 check: 461 rows, 0 failures
gcc -O2 -o /tmp/pq scripts/typei4_pqsearch.c -lm && /tmp/pq 300000 10001 > /tmp/pq3.txt      # 87 solutions, 3 min
python3 scripts/typei4_dgraded.py 5 24 3000 6                                     # 8 hits, all m=1, L>=11
gcc -O2 -o /tmp/lev scripts/typei4_level.c && for L in 7 8 9 10 12 15; do for s in 1 3 5 7 9; do /tmp/lev $L $s; done; done
gcc -O2 -o /tmp/lb scripts/typei4_lb.c && for L in 7 8 9 10; do for b in 0 1 2 3 4 5 6 7; do /tmp/lb $L $b; done; done
for L in $(seq 11 22); do for b in 0 1 2 3; do /tmp/lb $L $b; done; done        # Comp 3.4 table (minutes)
PYTHONPATH=scripts uv run python scripts/typei3_verify.py 7 185 42 32 71            # level-11 fibre example
```
