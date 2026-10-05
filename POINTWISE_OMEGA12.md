# H_ω(2): the charge moment is `≪𝓛^4(log𝓛)^2` (task O45)

Status: IN PROGRESS. Labels as in DISCOVERIES.md.

Notation as in POINTWISE_OMEGA11.md (O11): `𝓛=log T`, atoms `(M,D)`,
`M≤T`, `M≡3 (4)`, `A_M=(M+1)/4`, `D|A_M²`, `g=g(M,D):=gcd(M,4D+1)`,
`s(M,D)=C log log T·g/M` (O11 Lemma 2.1), `h(M)=Σ_{ℓ|M}H_{v_ℓ(M)}`,
`Ω♯=Σ s·h` (O11 §4). ET = Elsholtz–Tao arXiv:1107.1010
(`sources/elsholtz-tao-1107.1010.pdf`): Prop 1.4, Thm 7.1, Cor 7.4, (7.10).
`q` always denotes a prime power `ℓ^i` (`i≥1`), and `Σ_q` sums over them.

Target (O11 §4): **H_ω(B)** `Ω♯≪𝓛^4(log𝓛)^B`. We prove it with `B=2`
(Theorem 4), modulo ET Prop 1.4, Thm 7.1, Cor 7.4 and (7.10) (all proved in ET).

## 1. Elementary facts about h

**Lemma 1.1 (PROVED).** (a) `h(M)=Σ_{q|M}1/i` (`q=ℓ^i`).
(b) `h(xy)≤h(x)+h(y)`.
(c) For `Y≥2`: `Σ_{q|N, q>Y} 1/i ≤ log N/log Y`.

*Proof.* (a) `H_v=Σ_{i≤v}1/i` and `ℓ^i|M ⇔ i≤v_ℓ(M)`.
(b) `H_{x+y}−H_x=Σ_{x<i≤x+y}1/i≤H_y`.
(c) Fix `ℓ|N`, `v=v_ℓ(N)`. Each term with `ℓ^i>Y` has `i>log Y/logℓ`, so
`1/i<logℓ/log Y`, and there are at most v such i. Summing `v·logℓ/log Y`
over ℓ gives `log N/log Y`. ∎

## 2. Type I coordinates and the reduction

Put `Ω_0:=Σ_{atoms} (g/M)·h(M)`, so `Ω♯=C log log T·Ω_0`, and
`S_0:=Σ_{atoms} g/M`.

**Lemma 2.1 (parametrisation; PROVED; O2 Lemma 4.1 / O2 Lemma 8.1).**
Every atom with `D≤A_M` is `D=da²`, `A_M=dab` (`d` squarefree, `b≥a`), and
with `P:=4a²d+1`, `e:=g`, `f:=P/e`, `c:=(a+b)/e`, `N:=M/e` one has: c is a
positive integer, `f|P`, and

```
N = 4acd − f,     acd ≤ N ≤ T,     a²d ≤ T,     M = eN.
```

The map atom ↦ `(a,c,d,f)` is injective, and `g/M=1/N`. The involution
`D↦A_M²/D` preserves M and g. Hence

```
Ω_0 ≤ 2 Σ_{(a,c,d,f)} h(eN)/N ≤ 2(Σ_I + Σ_II),
Σ_I := Σ_{(a,c,d,f)} h(e)/N,   Σ_II := Σ_{(a,c,d,f)} h(N)/N,
```

both sums over quadruples coming from atoms (`e=P/f`, `N=4acd−f`).

*Proof.* `gcd(M,4dab)=1` as `M=4dab−1`. Since `M+4D+1=4da(a+b)`, `g|a+b`,
so c is an integer, and `g|P=4D+1`. The identity `4acd=f+N` is ET's (2.6),
checked in O2 Lemma 8.1: `e·4acd=4ad(a+b)=(ef−1)+(eN+1)`. From `b≥a`,
`eN=4abd−1≥4a²d−1=ef−2`, so `N≥f−2/e`. Then `2N≥N+f−2/e=4acd−2/e`, so
`N≥2acd−1≥acd`. `a²d=D≤A_M≤T`. `(a,c,d,f)` determines `e=P/f`, `b=ce−a`,
hence the atom. `g/M=e/(eN)=1/N`. For the involution: `gcd(A_M,M)=1` and
`4A_M≡1 (M)`, so `4A_M²/D+1≡(4D)^{−1}(1+4D) (mod M)`, and `g` is unchanged.
Finally `h(eN)≤h(e)+h(N)` (Lemma 1.1(b)). ∎

*Dyadic blocks.* For `A,B,C∈{2^j: j≥0}` the block `(A,C,B)` is
`a∈[A,2A)`, `c∈[C,2C)`, `d∈[B,2B)`. Only blocks with `A²B≤T` and `ACB≤T`
occur; there are `O(𝓛²)` pairs `(A,B)` (`A≤√T`, `B≤T`) and `≤𝓛/log2+1` values of C.

**Lemma 2.2 (block mass; PROVED modulo ET Prop 1.4).** For every block,
`Σ_{(a,c,d,f)∈(A,C,B)} 1/N ≤ Σ_{a,d} 2τ(P)/(ad) ≪ log(A+B+2)`.
Consequently `S_0≪𝓛^4`.

*Proof.* `1/N≤1/(acd)`, `Σ_{c∈[C,2C)}1/c≤2`, and for fixed `(a,d)` there
are `τ(P)` choices of f. ET Prop 1.4 (with ET's `(k,a,b)=(4,d,a)`) gives
`Σ_{a<2A,d<2B}τ(4a²d+1)≪AB log(A+B+2)`, and `1/(ad)≤1/(AB)` in the block.
Summing over `O(𝓛³)` blocks, with `log(A+B+2)≪𝓛`, gives `S_0`. ∎

## 3. The rough part: `Σ_II≪𝓛^4 log𝓛` (cut the primes at the c-scale)

**Lemma 3.1 (PROVED modulo ET Prop 1.4).** For every block `(A,C,B)`, with
`Y:=max(C,2)`,

```
Σ_{(a,c,d,f)∈(A,C,B)} h(N)/N ≪ log(A+B+2)·( log log(C+2) + 𝓛/log Y ).
```

Hence `Σ_II ≪ 𝓛^4 log𝓛`.

*Proof.* Split `h(N)=Σ_{q|N}1/i` (Lemma 1.1(a)) at `q≤C` / `q>Y`
(for `C=1` the first part is empty).

*Small q (`q≤C`).* Fix `(a,d,f)` and `q=ℓ^i≤C`. If `ℓ|4ad` then `ℓ∤N`:
`N≡−f (ℓ)` and `f|P≡1 (ℓ)` (P is odd, so `ℓ=2` is also excluded). Otherwise
`q|N=4ad·c−f` puts c in one class mod q, which has `≤C/q+1≤2C/q` elements in
`[C,2C)`. Each term has `1/N≤1/(adC)`. So the contribution is
`≤(2/(ad))Σ_{q≤C}1/(iq) ≤ (2/(ad))(log log(C+2)+O(1))` (Mertens for prime
powers). Summing over the `τ(P)` choices of f and over `(a,d)` with ET
Prop 1.4 as in Lemma 2.2 gives `≪log(A+B+2)·log log(C+2)`.

*Large q (`q>Y`).* By Lemma 1.1(c) and `N≤T`, `Σ_{q|N,q>Y}1/i≤𝓛/log Y`
pointwise. Lemma 2.2 gives `≪log(A+B+2)·𝓛/log Y`.

*Sum.* With `C=2^j`, `Σ_{0≤j≤𝓛/log2}(log log(2^j+2)+𝓛/log max(2^j,2)) ≪ 𝓛 log𝓛`,
and `Σ_{(A,B)}log(A+B+2)≪𝓛³`. ∎

*Why this avoids O11's obstruction.* O11 §4 summed `q|N` along the whole
c-progression for every q, and the first term of each progression (c below
q) has no usable bound. Here progressions are used only for `q≤C`, where a
block contains a full period. The primes `q>C` are paid pointwise by Lemma
1.1(c), at a cost `𝓛/log C`. This is large only when c is small, and Lemma
2.2 gives every dyadic c-scale the same mass, so the cost averages to
`(1/𝓛)Σ_j𝓛/j≍log𝓛`.

## 4. The smooth part: `Σ_I≪𝓛^4 log𝓛` (ET Thm 7.1 in progressions)

By Lemma 1.1(a), `Σ_{e|P}h(e)=Σ_{q|P}(1/i)·τ(P/q)` (write `e=qe'`, `e'|P/q`).
For a pair `(A,B)` put `Z:=max(A,B)` and

```
R(A,B) := Σ_{a∈[A,2A), d∈[B,2B)} (1/(ad)) Σ_{q|P} (1/i)·τ(P/q),     P=4a²d+1.
```

**Lemma 4.1 (PROVED modulo ET Prop 1.4, Thm 7.1, Cor 7.4, (7.10)).**
`R(A,B) ≪ log(Z+2)·log log(Z+16)`, uniformly in `A,B≥1`.

*Proof.* Every `q|P` is odd and has `ℓ∤ad`, since `P` is odd and `P≡1 (ℓ)` if `ℓ|ad`.

*Large q (`q>Z^{1/2}`), and all q if `Z<16`.* Use `τ(P/q)≤τ(P)`. As
`P<32Z³`, Lemma 1.1(c) gives `Σ_{q|P,q>Z^{1/2}}1/i≤2log(32Z³)/log Z≪1` for
`Z≥16`; for `Z<16` simply `h(P)≤log₂P≪1`. So this part is
`≪Σ τ(P)/(ad)≪log(Z+2)` (ET Prop 1.4, as in Lemma 2.2).

*Small q, case `A≥B` (`Z=A≥16`, `q=ℓ^i≤A^{1/2}`), quadratic.* Fix `d<2B`
with `ℓ∤d`. `P(x)=4dx²+1` has at most two roots `x_0 mod q` (ℓ odd,
`ℓ∤4d`, Hensel). For each, write `a=qa'+x_0`. Then `a'≥1` (as
`a≥A≥q>x_0`) and `a'≤N':=⌊2A/q⌋`. Put

```
Q(a') := P(qa'+x_0)/q = 4dq·a'² + 8dx_0·a' + (4dx_0²+1)/q .
```

The coefficients are nonnegative integers `≤8dq≤16A^{3/2}≤N'^5` (`N'≥A^{1/2}`,
`A≥16`). Root counts: Q is odd-valued, so `ρ_Q(2^j)=0`. For an odd prime
`p≠ℓ`, `a'↦qa'+x_0` is a bijection mod `p^j`, so `ρ_Q(p^j)=ρ_{4d}(p^j)≤2`,
where `ρ_{4d}(m):=#{x mod m: 4dx²+1≡0}` (ET's `ρ_{ka}` with `k=4`, `a=d`). For
`p=ℓ`, each of the `≤2` roots of P mod `ℓ^{i+j}` fixes `a' mod ℓ^j`, so
`ρ_Q(ℓ^j)≤2`. ET Thm 7.1 (degree 2, `l=5`, `C=2`) gives

```
Σ_{a'≤N'} τ(Q(a')) ≪ N' Σ_{m≤N'} ρ_Q(m)/m ≤ (2A/q)·(1+2/(ℓ−1))·Σ_{m≤2A} ρ_{4d}(m)/m,
```

using multiplicativity of `ρ_Q` and `ρ_Q(m')=ρ_{4d}(m')` for `ℓ∤m'`. With
`1/(ad)≤1/(AB)` and two roots,

```
Σ_{a,d: q|P} τ(P/q)/(ad) ≪ (1/(qB)) Σ_{d<2B} Σ_{m≤2A} ρ_{4d}(m)/m ≪ log A / q,
```

by ET (7.10) with ET's `(A,B,k)=(2B,2A,4)`. ET prove (7.10) for ET's `A≤B`,
which is `B≤A` here.

*Small q, case `B>A` (`Z=B≥16`, `q≤B^{1/2}`), linear.* Fix `a<2A` with
`ℓ∤a`. `q|P` means `d≡d_0:=−(4a²)^{−1} (mod q)`, `0<d_0<q`. Write
`d=qd'+d_0` with `1≤d'≤N:=⌊2B/q⌋` (`d≥B≥q`). Then
`P/q=4a²d'+b_a`, `b_a:=(4a²d_0+1)/q≤4a²+1`. Here `gcd(4a²,b_a)=1`: `b_a` is
odd, and `gcd(a,b_a)|gcd(a,4a²d_0+1)=1`. Both coefficients are
`≤16B²≤N^6` (`N≥B^{1/2}`, `B≥16`). ET Cor 7.4 gives
`Σ_{d'≤N}τ(4a²d'+b_a)≪N log N≤(2B/q)log(2B)`. With `1/(ad)≤1/(aB)`:
`Σ_{a,d: q|P}τ(P/q)/(ad)≪(log B/q)Σ_{a<2A}1/a`. The last sum is over
`a∈[A,2A)`, so it is `≤2`.

*Sum over small q.* `Σ_{q≤Z^{1/2}}(1/i)·log Z/q ≪ log Z·log log Z`. ∎

**Corollary 4.2 (PROVED modulo ET).** `Σ_I ≪ 𝓛^4 log𝓛`.

*Proof.* `1/N≤1/(acd)`, `Σ_{c∈[C,2C)}1/c≤2`, and each `(a,d,e)` with `e|P`
occurs once per c. So `Σ_I≤Σ_C Σ_{(A,B)} 2R(A,B)`. Lemma 4.1 with
`log(Z+2)≪𝓛` (as `Z≤T`) and the block counts of §2 gives
`≪𝓛·𝓛²·𝓛 log𝓛`. ∎

## 5. The theorem

**Theorem 5.1 (H_ω(2); PROVED modulo ET Prop 1.4, Thm 7.1, Cor 7.4, (7.10)).**

```
Ω_0 = Σ_{atoms} (g/M)·h(M) ≪ 𝓛^4 log𝓛,      Ω♯ = C log log T·Ω_0 ≪ 𝓛^4 (log𝓛)^2.
```

*Proof.* Lemma 2.1, Lemma 3.1 and Corollary 4.2. ∎

So the s-weighted mean of the charge h is `≪log𝓛` (against `S_0≪𝓛^4`), as
the O11 EVIDENCE suggested (`2.32, 2.57, 2.79` at `T=10^{4,5,6}`).

## 6. Exponent 1/5

**Theorem 6.1 (PROVED modulo (G), ET Prop 1.4/Thm 7.1/Cor 7.4/(7.10), and
OMEGA10 Thm 3.4).** For infinitely many Mordell-hard primes p,

```
W(p) ≥ exp( c·(log p)^{1/5}·(log log p)^{−2/5} ),     uniformly  log L_h(T) ≪ 𝓛^5 (log𝓛)^2.
```

*Proof.* O11 Corollary 4.1 with `B=2` (Theorem 5.1). In detail: O11
Lemma 2.2 with `c=1/64` gives `log Q≤9+64𝓛Ω♯≪𝓛^5(log𝓛)^2`. O11 Cor 1.2
gives the junta term `O(𝓛(S+𝓛))` with `S≤S♯≪𝓛^4log𝓛` (O2 Lemma 9.2 under ET; also Lemma 2.2
here). The rest is O11 Thm 3.2's proof verbatim, with Cor 1.2's
modulus-weighted truncation in place of OMEGA10 Thm 4.2's coordinate count.
So `log Z≪𝓛^5(log𝓛)^2`, and some hard `p>T` with `W(p)>T` has
`log p≪𝓛^5(log𝓛)^2`, i.e. `𝓛≫(log p)^{1/5}(log log p)^{−2/5}`. ∎

Thus the "1/5 natural limit of the present ES-modulus route" (O11 §4,
Assessment) is reached, up to `(log log p)^{2/5}`. Unconditionally (without
ET) nothing changes: O9 Thm 2.3 stands.

## 7. Checks (EVIDENCE; exact identities asserted)

`scripts/omega12_blocks.py T` enumerates all atoms with `D≤A_M` and asserts
Lemma 2.1's identities (`c∈ℤ`, `N=4acd−f`, `N≥acd`, `a²d≤T`), Lemma 1.1(b)
for `M=eN`, and Lemma 3.1's pointwise large-q bound. All pass at
`T=10^4,10^5,10^6` (35 803 / 547 733 / 7 777 872 atoms).
(`data/omega12/blocks_1e{4,5,6}.txt`)

| T | `S_0'` | `Ω_0'` | mean h | `Σ_I` | `Σ_II` | `(Σ_I+Σ_II)/Ω_0'` | max `R/(log(Z+2)loglog(Z+16))` |
|---|---|---|---|---|---|---|---|
| 10⁴ | 28.75 | 62.18 | 2.163 | 18.37 | 45.30 | 1.024 | 1.290 |
| 10⁵ | 58.04 | 139.42 | 2.402 | 42.86 | 99.91 | 1.024 | 1.290 |
| 10⁶ | 105.03 | 274.81 | 2.617 | 87.05 | 194.16 | 1.023 | 1.290 |

(primes: restricted to `D≤A_M`, i.e. half of O11's pure-`g/M` sums; the mean
h matches O11's `2.18, 2.42, 2.63`.) The splitting `h(eN)≤h(e)+h(N)` loses
only 2%. The Lemma 4.1 ratio is the same small-block maximum at all T. The
Lemma 3.1 profile (mass and mean `h(N)` per c-scale `C=2^j`) shows the
crude bound `𝓛/log max(C,2)` far above the actual large-q part
(at `10^6`: `1.65` vs `19.9` at `j=0`; `0.26` vs `1.17` at `j=17`), and the mass
per scale *decreasing* in j (14.2 at j=0, 0.13 at j=17). Evaluated on these
actual masses, Lemma 3.1's two bounds (`log log` small part plus `𝓛/log Y`)
give a mean `≈8.6` for `h(N)` at `10^6`, against the true `1.85`: at finite T the
proof is crude, and almost all of the slack is the `j≤1` scales. The asymptotic
statement only uses Lemma 2.2's uniform bound per scale.

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; timeout 600  uv run python scripts/omega12_blocks.py 10000)    # seconds  -> data/omega12/blocks_1e4.txt
(ulimit -v 8000000; timeout 1800 uv run python scripts/omega12_blocks.py 100000)   # ~10 s    -> data/omega12/blocks_1e5.txt
(ulimit -v 8000000; timeout 7200 uv run python scripts/omega12_blocks.py 1000000)  # ~3 min   -> data/omega12/blocks_1e6.txt
```
