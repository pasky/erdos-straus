# Is the sign point `x̂_9` sterile? (task O72)

Status: in progress (side agent O72, branch `side-agent/sign-point-sterility`).
Builds on POINTWISE_TYPEI2.md (Theorem A, (2.2), Lemma 2.4, Lemma 3.1, Computation 3.2, Conjecture 3.4).

Notation. `x̂=x̂_w`: `w` at 2 (`w≡9 (16)`), `−1` at 7, `1` elsewhere. A certificate
at `x̂` is `(c,k,F)`, `v_7(c)` odd, `F | N=1+4ck²`, and `F≡−x̂ (mod 4ck)`, i.e.
(2.2). Write `4ck=2^t n` (`n` odd), `n=7^v m'` (`7∤m'`), `c=2^α7^a c'`,
`k=2^γ7^b k'`, so `t=2+α+γ`, `v=a+b`, `m'=c'k'`, `k_o=7^b k'` (odd part of k).
Note `4ck²=2^{t+γ} n k_o`.

## 1. Small-divisor reduction (PROVED)

**Lemma 1.1.** Let `(c,k,F)` be a certificate at `x̂_w` and `e=N/F`. For
`f∈{F,e}`:
(i) `m' | f+1` and `7^v | f−1`; in particular `n | (f+1)(f−1)`;
(ii) `f≡−w (mod 2^t)` if `f=F`, and `wf≡−1 (mod 2^t)` if `f=e`;
(iii) `2^{t+γ}·n·k_o ≡ −1 (mod f)`.
Conversely, given odd `f≥1`, a role (F or e), integers `t≥2`, `0≤γ≤t−2`, `a` odd,
`b≥0`, and `c',k'` odd, prime to 7, with (i)–(iii) for `m'=c'k'`, `v=a+b`,
then `(c,k,F)` with `c=2^{t−2−γ}7^a c'`, `k=2^γ7^b k'` and `F=f` (resp.
`F=N/f`) is a certificate at `x̂_w`.

*Proof.* `F≡−x̂ (mod 4ck)` means `F≡−1 (m')`, `F≡1 (7^v)`, `F≡−w (2^t)`. Since
`N≡1 (mod 4ck)`, `e≡F^{−1}≡−x̂^{−1}` (mod 4ck), and `x̂^{−1}` has components
`1, −1, w^{−1}`; this gives (i), (ii). (iii) is `f | N` rewritten. Conversely,
(iii) gives `f|N`, so `f` (resp. `N/f`) is coprime to `4ck` (N≡1 mod 4ck) and lies
in the class `−x̂` (resp. `−x̂^{−1}`) mod `4ck` by (i), (ii); the cofactor of
a divisor in class `−x̂^{−1}` is in class `−x̂`. `v_7(c)=a` is odd, so
`7 | sf(c)` and `s∉{1,2,3,6}`. ∎

**Consequence.** For a fixed `f`, there are finitely many certificates having
`f` as one of their two complementary divisors: `t ≤ v_2(f+w)` resp.
`t≤v_2(wf+1)`, `n` divides the explicit number `(f+1)_{odd}·7^{v_7(f−1)}`,
and `k_o | n`. So the certificates at `x̂_w` are graded by
`f_min=min(F,e)≤√N`, with a finite, fully explicit check per value of
`f_min`. Note `f_min` can be tiny while `ck` is huge (`ck=2^{t−2}n` with `n` up
to `≈f²/16`); this is how all near misses in the §5 data of POINTWISE_TYPEI2
look (`f_min` = 15, 71, 239, 407, …, with `ck` up to `4·10⁸`).
