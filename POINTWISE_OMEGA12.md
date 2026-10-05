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
occur; there are at most `(𝓛+1)²` pairs `(A,B)` and `𝓛/log2+1` values of C.

**Lemma 2.2 (block mass; PROVED modulo ET Prop 1.4).** For every block,
`Σ_{(a,c,d,f)∈(A,C,B)} 1/N ≤ Σ_{a,d} 2τ(P)/(ad) ≪ log(A+B+2)`.
Consequently `S_0≪𝓛^4`.

*Proof.* `1/N≤1/(acd)`, `Σ_{c∈[C,2C)}1/c≤2`, and for fixed `(a,d)` there
are `τ(P)` choices of f. ET Prop 1.4 (with ET's `(k,a,b)=(4,d,a)`) gives
`Σ_{a<2A,d<2B}τ(4a²d+1)≪AB log(A+B+2)`, and `1/(ad)≤1/(AB)` in the block.
Summing over `≤(𝓛+1)²(𝓛/log 2+1)` blocks, with `log(A+B+2)≪𝓛`, gives `S_0`. ∎
