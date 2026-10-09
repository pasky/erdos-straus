# EXCEPTIONAL_TYPEI_LOGLOG — attacking ET's open Type I bound Σ_{p≤N} f_I(p) ≪ N log² N (task O111)

Status labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010v6 (`sources/elsholtz-tao-1107.1010.pdf`);
MN3 = `EXCEPTIONAL_MN3.md` (§3 there: the obstruction region R_bad / R**, Lemma 3.1, Thm 3.8);
DI = Deshouillers–Iwaniec, Invent. Math. 70 (1982) 219–288. `L = log N`.

## 0. Summary (work in progress; updated as lemmas are added)

* Literature (2026-10, search-limited, research subagent + own check): no removal of ET's `log log N` found.
  ET v6 cites Jia, Sci. China Math. 55 (2012) 465–474 ("mean values … 4/p"), yet still states the Type I
  `log log N` as open (ET p. 5); Jia's text was not accessible (abstract only).
* Lemma 2.2 (PROVED, elementary): the level-d Heegner points of MN3 Lemma 3.1 are **uniformly separated**
  in the hyperbolic plane: distinct points satisfy `cosh dist ≥ 3/2`, independently of d.
  (Numerically the minimum is ≥ 3: `scripts/ttl_separation.py`.)
* Plan (§3): per-d count = (#classes)·(mean of an automorphic Poincaré-type function) + error, with the
  error bounded by Cauchy–Schwarz in a Sobolev norm: `‖Σδ_z‖_{H^{-2}}² ≪ #classes` (by separation) times
  the variance of the counting function (by the DI large sieve). Heuristic outcome: relative error
  `(d/a)^{1/2}`, complementary to MN3's (K_a) (relative error `a/d`).

## 1. Set-up

For `c ≥ 1`, the Type I weight (MN3 §3.7) is
`w_c(n) = #{(a,d,f) ∈ ℕ³ : f | 4a²d+1, n = 4acd − f, n/4 < acd ≤ 3n/4}`, `f_I(p) ≤ 2Σ_c w_c(p)`.
Write `e = (4a²d+1)/f`, so `ef − 4a²d = 1`; MN3 Lemma 3.1: `M = [[e,2a],[2ad,f]] ∈ SL₂(ℤ)`.
Exponents for `n ≍ N`: `a = N^α`, `c = N^γ`, `d ≍ N^{1−α−γ}`, `e ≍ N^{β−γ}`, `f ≍ N^{1+α−β}`.
MN3 Thm 3.8 reduces (OPEN-I) to a level of distribution for `w_c`, `c ≤ N^{η₀}`; MN3 §3.4 locates the
difficulty at `α ≥ (1−γ)/2` (the (K_a) count — modular hyperbola `ef ≡ 1 (mod 4a²)` — has per-a error
`≍ a` against main term `≍ d`).

**Key accounting remark (Lemma 1.1 below).** A power saving that *degenerates linearly* at a boundary
(e.g. relative error `N^{−κ|α−1/2|}`) does **not** reintroduce `log log N`: only a positive-measure set of
cells with no power saving at all does.

**Lemma 1.1 (degenerate savings are harmless; PROVED, elementary).** Let `L ≥ 2`. For integers
`1 ≤ j, k ≤ L` let `m_{jk} ≥ 0` with `Σ_k m_{jk} ≤ M` for each j. Then
`Σ_{j,k≤L} m_{jk} min(1/j, 1/k) ≤ M·(1 + log L)` trivially, but if also `m_{jk} ≤ M/L` for all j, k, then
`Σ_{j,k} m_{jk} min(1/j,1/k) ≤ (M/L)·Σ_{j,k≤L} min(1/j,1/k) ≤ 2M`.
*Proof.* `Σ_{j,k≤L} min(1/j,1/k) = Σ_{m≤L} (2m−1)/m ≤ 2L`. ∎
*Use.* j indexes the dyadic c-block (`c ≍ 2^j`; BT gives saving `1/j`), k a dyadic distance from the bad
boundary (e.g. `a ≍ N^{1/2}2^{k}`, saving `≍ 1/k` once a level of distribution `N^{κ k/L}` is available);
`m_{jk} ≪ N log N` is the Type I mass of one (c-block, a-block) pair (ET (8.2) per dyadic box). So a
saving `min(1/j, 1/k)` costs `O(N log² N)` in total.

## 2. Separation of the level-d Heegner points

Fix `d ≥ 1`. Let `𝓕_d` be the set of integral binary forms `Q = [A, B, C] = AX² + BXY + CY²` with
`B² − 4AC = −4d`, `A > 0`, `B ≡ 0 (mod 2d)`, `C ≡ 0 (mod d)`. Each Type I quadruple gives
`Q = [f, 4ad, de] ∈ 𝓕_d` (disc `16a²d² − 4def = −4d`). Root map `z_Q = (−B + i√(4d))/(2A) ∈ ℍ`.

**Lemma 2.1 (distance formula; standard).** For positive definite forms Q, Q' of the same discriminant
`D < 0`: `cosh dist_ℍ(z_Q, z_{Q'}) = 1 + disc(Q − Q')/(2|D|)`.
*Proof.* `cosh dist(z,w) = 1 + |z−w|²/(2 Im z Im w)`. With `z = (−B+i√|D|)/2A`, `w = (−B'+i√|D|)/2A'`:
`|z−w|²·4AA' = (BA' − B'A)²/(AA') + |D|(A'−A)²/(AA')`, and `2 Im z Im w·4AA' = 2|D|`. So
`cosh − 1 = [(BA'−B'A)² + |D|(A−A')²]/(2|D|AA')`. Expanding `disc(Q−Q') = (B−B')² − 4(A−A')(C−C')`
with `4AC = B² + |D|`, `4A'C' = B'² + |D|`, `4AC' = A(B'²+|D|)/A'`, `4A'C = A'(B²+|D|)/A`, one gets
`AA'·disc(Q−Q') = (BA' − B'A)² + |D|(A − A')²`. ∎ (Checked numerically in `scripts/ttl_separation.py`.)

**Lemma 2.2 (uniform separation; PROVED).** For distinct `Q, Q' ∈ 𝓕_d`: `cosh dist(z_Q, z_{Q'}) ≥ 3/2`.
*Proof.* `B ≡ B' (mod 2d)` gives `4d² | (B−B')²`, and `C ≡ C' ≡ 0 (mod d)` gives `4d | 4(A−A')(C−C')`,
so `4d | disc(Q−Q')`. By Lemma 2.1 (|D| = 4d), `disc(Q−Q') = 8d(cosh − 1) ≥ 0`, so
`cosh − 1 ∈ ½ℤ_{≥0}`. If `cosh = 1` then `z_Q = z_{Q'}`; a positive definite form of discriminant D is
determined by its root (`Q = A(X − zY)(X − z̄Y)` and `B² − 4AC = D` fixes A), so `Q = Q'`. ∎
*Remark.* Only `B ≡ B' (2d)` and `d | C, C'` were used, so the lemma holds for any subset of 𝓕_d, e.g.
the forms with prescribed residues mod q (sieve conditions). Numerically (`ttl_separation.out.txt`)
the minimum over the enumerated pairs is `cosh ≥ 3`.
