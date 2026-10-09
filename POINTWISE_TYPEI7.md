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
