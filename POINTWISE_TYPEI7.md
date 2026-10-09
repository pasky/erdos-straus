# The 2-adic closeness of fibre certificates to `w = 9` (task O109)

Status: work in progress (side agent O109, branch `side-agent/sign-point-2adic`). Not reviewed.
Builds on POINTWISE_TYPEI2.md ((2.2), §3), POINTWISE_TYPEI4.md (Lemma 1.1, Prop 1.2, Cor 1.4, Comp 3.4,
Cor 3.5, Assessment 4.2(d)), POINTWISE_TYPEI5.md (Lemma 1.1), POINTWISE_TYPEI6.md.

Notation as in TYPEI4: a fibre certificate of level `L = α+2γ ≥ 7` has `c = 2^α c_o`, `k = 2^γ k_o`,
`c_o = 7^a c'`, `k_o = 7^b X`, `n = c_o k_o`, `N = Fe = 1 + 2^{L+2} c_o k_o²`, `F ≡ 7 (mod 16)`,
`e − F = 16nδ` with `δ` odd (TYPEI4 Lemma 1.1(ii); here `δ` is **signed**: no orientation is chosen, so
`F` is the divisor under consideration and `e = N/F` its cofactor). `t = 2+α+γ`.

**Criterion (TYPEI4 Cor 3.5 proof).** A fibre certificate is a certificate at `x̂_9` for the split `(α,γ)`
iff `v_2(F+9) ≥ t`. Since `t ≥ 2+⌈L/2⌉` with equality for `γ = ⌊L/2⌋`, the level-`L` data
`(c_o,k_o,F)` give a certificate at `x̂_9` (for some split) iff `v_2(F+9) ≥ 2+⌈L/2⌉`.
(The split `α ∈ {0,1}` keeps `sf(c)` divisible by 7, so `s ∉ {1,2,3,6}`.)

## 1. An exact formula for the 2-adic closeness (PROVED)

**Lemma 1.1 (PROVED).** For every fibre certificate (any `L ≥ 1` with `F ≡ 7 (mod 16)`, `nδ` odd),

```
v_2(F + 9) = 3 + v_2(E),     E := 5 − 9nδ − 2^{L−2} c_o k_o².                                  (1.1)
```

In particular, for the minimal split, `F` is a certificate at `x̂_9` iff
`9nδ + 2^{L−2}c_ok_o² ≡ 5 (mod 2^{⌈L/2⌉−1})`, and for `L ≥ 5` (where `⌈L/2⌉−1 ≤ L−2`) iff

```
nδ ≡ 5·9^{−1} ≡ 5·57 ≡ 285 (mod 2^{⌈L/2⌉−1})     [9^{−1} ≡ 57 (mod 512)].                      (1.2)
```

The cofactor `e` (the other orientation, `δ ↦ −δ`) is a certificate at `x̂_9` iff `−nδ ≡ 5/9 (mod 2^{⌈L/2⌉−1})`.
*Proof.* `e = F + 16nδ` and `Fe = N` give the exact identity `F² + 16nδF − 1 = 2^{L+2}c_ok_o²`.
With `G := F + 9`: `(G−9)² + 16nδ(G−9) − 1 = G(G − 18 + 16nδ) + 80 − 144nδ`, so

```
G·(G − 18 + 16nδ) = 16·E.
```

`F ≡ 7 (16)` gives `16 | G`, so `v_2(G − 18 + 16nδ) = 1`, and `v_2(G) + 1 = 4 + v_2(E)`. ∎

*Consequence (scope).* The closeness to `w = 9` is a congruence on the single odd integer
`nδ = c'·X·7^{a+b}δ` modulo `2^{⌈L/2⌉−1}` (`nδ = c'XD` in Cor 1.4 coordinates). Whether some fibre
certificate satisfies (1.2) is therefore the question whether the Pell/archimedean structure
(TYPEI4 Lemma 3.1) correlates with `nδ mod 2^j`.

## 2. The closeness is unbounded: `x̂_9` is a limit of covered fibre points (PROVED)

**Theorem 2.1 (PROVED).** For every `m ≥ 4` there is a fibre certificate `(c,k,F)` (Type I, `v_7(c)` odd) with
`v_2(F+9) ≥ m`. Hence, for every `m`, the class `Cl(c,k,F)` contains the point `x̂_w` with `w := −F ∈ ℤ_2`,
`v_2(w−9) ≥ m`: the sign point `x̂_9` lies in the closure of the union of all certificate classes
(already inside the fibre `Φ = {x̂_w : w ≡ 9 (16)}`). In particular `max(v_2(F+9), v_2(e+9))` over fibre certificates
is unbounded (this answers the open question of TYPEI4 §5 / Assessment 4.2(d)), and **no 2-adic neighbourhood of 9
in `Φ` is sterile**: sterility of `x̂_9`, if true, cannot be proved by any test that sees `w` only modulo a fixed `2^j`.

*Construction.* Since `−9 ≡ 7 (mod 16)` and `7^s` (`s` odd) runs through all classes `≡ 7 (mod 16)` modulo `2^m`
(`7·⟨49⟩`, `⟨49⟩ = 1 + 16ℤ_2`), choose an odd `s` with `7^s ≡ −9 (mod 2^m)`. Put `b := (s−1)/2`, `a := 1`, choose
`i ≥ m` with `3·7^b | i` (so `2^i ≡ 1 (mod 7^{b+1})`, as `ord_{7^{b+1}}(2) = 3·7^b`), and set

```
F := 7^s + 2^i,    c' := (F+1)/8,    X := 1,    c_o := 7c',    k_o := 7^b,
L ≥ 7 with L ≡ 1 − i (mod ord_F(2)),    c := 2^α c_o, k := 2^γ k_o  (any split α + 2γ = L).
```

*Proof.* (1) `F ≡ 7^s ≡ −9 (mod 2^m)`, so `v_2(F+9) ≥ m` and `F ≡ 7 (mod 16)`. (2) `F+1 ≡ 8 (mod 16)`, so `c'` is an
odd integer; `F ≡ 2^i ≡ 1 (mod 7)` gives `F+1 ≡ 2 (mod 7)`, so `7 ∤ c'`; and `v_7(c) = 1` is odd, so `7 | sf(c)`.
(3) `F | N`: `N = 1 + 2^{L+2}c_ok_o² = 1 + 2^{L+2}7^s c'`, and `8c' ≡ 1 (mod F)` gives
`N ≡ 1 + 2^{L−1}7^s ≡ 1 − 2^{L−1+i} ≡ 0 (mod F)` by the choice of `L`. (4) The congruences of TYPEI2 (2.2):
`F ≡ −1 (mod c'k')` since `c'k' = c' | F+1`; `F ≡ 1 (mod 7^{v_7(ck)})`, `v_7(ck) = b+1`, since `7^{b+1} | 7^s` and
`2^i ≡ 1 (mod 7^{b+1})`; and `F ≡ −w (mod 2^{2+α+γ})` for `w = −F`. (5) `(F, 4ck) = 1`: `F` is odd, `7 ∤ F`, and
`gcd(F, c') | gcd(F, F+1) = 1`. So `(c,k,F)` is a certificate at `x̂_w` (TYPEI2 §3), and it is a fibre certificate
(TYPEI4 Lemma 1.1, `F ≡ 7 (16)`). ∎

*Remarks.* (a) The certificate is **not** at `x̂_9`: its level satisfies `L ≡ 1−i (mod ord_F(2))` with `L−1+i ≥ log_2 F`,
so `L` is of size `ord_F(2)` (typically ≈ `F ≥ 2^i ≥ 2^m`), far above `2·v_2(F+9)`. (b) The same argument shows that
every fixed triple `(c_o, k_o, F)` that is a fibre certificate at one level `L_0` is one at every level
`L ≡ L_0 (mod ord_F(2))`, `L ≥ 7` (only `F | N` depends on `L`, and only through `2^L mod F`); for those `L` the
closeness `v_2(F+9)` is constant and `v_2(e+9) = v_2(9F+1)` once `L+2 > v_2(9F+1)` (as `e ≡ F^{−1} (mod 2^{L+2})`).
So **every fibre certificate recurs at infinitely many levels, and each triple `(c_o,k_o,F)` is at `x̂_9` for at most
the finitely many levels with `2+⌈L/2⌉ ≤ max(v_2(F+9), v_2(9F+1))`** (PROVED). E.g. `(42,32,71)` (TYPEI4) recurs at
`L = 11 + 35j` (`ord_71(2) = 35`).

**Computation 2.2 (CERTIFIED once replayed).** `scripts/typei7_unbounded.py 5` builds the Theorem 2.1 certificates
for `m = 4, 5` and checks them (two splits each) with the stand-alone checker `typei3_verify.check`:
`m=4`: `s=1, i=6, F=71, c'=9, L=30` (`ord_71(2)=35`); `m=5`: `s=3, b=1, i=21, F=7³+2²¹=2097495,
c'=262187, L=93184` (`ord_F(2)=93204`), `v_2(F+9)=5`. For `m ≥ 6` the construction needs `s ≥ 7`, `i ≥ 3·7³`, and
`ord_F(2)` for `F > 2^{1029}` is not computed; the proof does not need it (`L` exists since `F` is odd).
