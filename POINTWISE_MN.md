# POINTWISE_MN — the m/n witness modulus at exponent 1/4 (task O63)

Status: work in progress (branch `side-agent/mn-quarter`). Labels as in DISCOVERIES.md.

## 0. Setting

Fix `m ≥ 4`. As in POINTWISE_TRANSFER §5.1: an *atom* is `(M,D)` with `M ≡ −1 (mod m)`,
`M ≥ 3`, `A = A_M = (M+1)/m`, `D | A²`; its event is `n ≡ −mD (mod M)`;
`R_m(M) = {−mD mod M : D | A²}`; `W_m(n)` is the least M with `n mod M ∈ R_m(M)`.
By TRANSFER Lemma 5.0 these are exactly the Type II solutions of `m/n` (5.1)
`m/n = 1/(suw) + 1/(nsvw) + 1/(nuvw)`, `M = m·uvw − 1`, class `−u v^{−1} ≡ −m u² w (mod M)`.
Note `gcd(M, mA) = 1`; every prime of `m` and of `A` is `≡`-congruent: `M ≡ −1 (mod q)` for all `q | mA`.

For `m = 4` POINTWISE_OMEGA13 Lemma 3.1 says the class `−4D` is a Jacobi non-residue mod M.
This is what lets the square-class process (OMEGA13 §3) never fire an event.

## 1. The Jacobi symbol of the event classes for general m

Let `e = e(m,D)` be the squarefree part of `mD` (equivalently of `m·w` in (5.1), since
`−mD = −m u² w`). Write `e = 2^{t} e_o` with `t ∈ {0,1}`, `e_o` odd.

**Lemma 1.1 (PROVED; brute-forced).** Let `(M,D)` be an atom with M odd.

* (a) Every prime `ℓ | M` has `(−mD | ℓ) = (−e | ℓ)`.
* (b) If `M ≡ 3 (mod 4)`: `(−mD | M) = −(2|M)^t`. In particular `= −1` if `M ≡ 7 (8)`,
  and for `M ≡ 3 (8)` it is `−1` iff `t = 0`.
* (c) If `M ≡ 1 (mod 4)`: `(−mD | M) = (2|M)^t · (−1)^{(e_o−1)/2}`.
* (d) **If `m ≡ 0 (mod 4)`, then `(−mD | M) = −1` for every atom** (OMEGA13 Lemma 3.1 verbatim).

*Proof.* (a) `gcd(M, mA) = 1` and every prime of D divides A, so `ℓ ∤ mD`, and `−mD = −e·□` with the square prime to ℓ. (Also ℓ odd as M is odd.)
For (b),(c): every prime `q | e` divides `mA = M + 1`, so `M ≡ −1 (mod q)`. For odd q,
reciprocity gives `(q|M) = (M|q)(−1)^{((q−1)/2)((M−1)/2)} = (−1)^{((q−1)/2)((M+1)/2)}`,
i.e. `(q|M) = 1` if `M ≡ 3 (4)` and `(q|M) = (−1|q)` if `M ≡ 1 (4)`. Multiply with
`(−1|M)` and `(2|M)^t`: for `M ≡ 3 (4)`, `(−1|M) = −1` and all odd q give 1; for `M ≡ 1 (4)`,
`(−1|M) = 1` and `∏_{q|e_o}(−1|q) = (−1|e_o) = (−1)^{(e_o−1)/2}`.
(d) `m ≡ 0 (4)` gives `M ≡ 3 (4)`. If `t = 1` then `v_2(mD)` is odd; if `8 | m` then
`8 | mA`; if `m ≡ 4 (8)` then `v_2(D)` is odd, so `2 | A` and `8 | mA`. Either way
`M ≡ 7 (8)`, `(2|M) = 1`, and (b) gives `−1`. ∎

*Check.* `scripts/mn_jacobi.py 50000 4 5 6 7 8 9 10 11 12 14 18`: the formula (b)/(c) and (a)
hold on every odd-M atom (e.g. 473 842 atoms for m=4, 284 878 for m=5), 0 failures; for
`m ∈ {4,8,12}` every symbol is −1.

**Consequence (square-consistency).** Call an atom *square-consistent* if `−mD` is a
square unit modulo every prime power `ℓ^v ‖ M` (for `ℓ = 2`: `v=1` any; `v=2`: `≡1 (4)`;
`v≥3`: `≡1 (8)`). These are exactly the atoms that the OMEGA13 square-class process can fire.
By (d) there are none for `m ≡ 0 (4)`. For `m ≢ 0 (4)` they are a positive proportion
(`M ≤ 5·10⁴`: m=5: 68 642 of 363 982; m=6: 56 964/293 117; m=7: 38 355/244 129;
m=10: 29 704/159 390). Smallest examples: `m=5: (M,D)=(9,1)` (class 4 ≡ 2² mod 9),
`(29,1)` (class 24 ≡ 13² mod 29); `m=6: (5,1)` (class 4); `m=7: (13,2)` (class 12 ≡ 5²).

## 2. For m ≢ 0 (mod 4) the square-class process fires: a precise obstruction

**Proposition 2.1 (PROVED).** Let `m ≢ 0 (mod 4)`. There are infinitely many primes
`ℓ ≡ −1 (mod m)` such that the prime atom `M = ℓ` has event classes in *both* cosets of the
squares mod ℓ. Hence for any rule that reveals `r mod ℓ` uniformly inside a coset of the squares
(either coset, chosen by any rule), the prime atom `M = ℓ` fires with probability `≥ 2/(ℓ−1) > 0`.

*Proof.* It suffices to find ℓ prime, `ℓ ≡ −1 (m)`, `ℓ ≡ 1 (4)`, and a prime `q | A = (ℓ+1)/m`
with `(q|ℓ) = −1`: then `D = 1` and `D = q` (both divide `A²`) give classes `−m`, `−mq` with
Legendre symbols of ratio `(q|ℓ) = −1`.
* `m` odd: take `q = 2` and `ℓ ≡ −1 (mod m)`, `ℓ ≡ 5 (mod 8)` (compatible). Then `ℓ+1 ≡ 6 (8)`,
  so `2 | A`, and `(2|ℓ) = −1`.
* `m ≡ 2 (mod 4)`: take an odd prime `q ≡ 3 (4)`, `q ∤ m`, and `ℓ ≡ −1 (mod mq)`, `ℓ ≡ 1 (mod 4)`
  (compatible, as `v_2(mq) = 1`). Then `q | A` and, by Lemma 1.1's reciprocity step,
  `(q|ℓ) = (−1|q) = −1`.
Dirichlet's theorem gives infinitely many such ℓ. ∎

Examples: `m=5`, `ℓ=29` (`A=6`, classes `−5D`, `D|36`, contain both residues and
non-residues); `m=6`, `ℓ=5` (`A=1`, class `4 = 2²`, so the squares coset itself is hit).

*Scope.* In the OMEGA13 process every prime `ℓ ≤ Y` whose fibre mass exceeds `η ≍ 1/log 𝓛` is
stepped; the Haar mass through a fixed small prime is `≫ 𝓛³/ℓ`, so fixed small ℓ
(e.g. 29 for m=5) are always stepped. So the square-class process of OMEGA13 §3 does not run for
`m ≢ 0 (4)`, and no "random square class of a fixed quadratic character pattern" replaces it.
More generally, Lemma 1.1(b),(c) show that the Jacobi symbol `(−mD|M)` is a function of
`(M mod 8, e mod 8)`, and for a fixed M it takes both values as D varies whenever A has a prime
`q ≡ 3 (4)` (M ≡ 1 (4)) or `t` varies (M ≡ 3 (8)); a coset `k·□` of the squares has
`(k|M)` depending on M only, so it cannot separate the event classes for those M. What survives
for every m: atoms with `M ≡ 7 (mod 8)` are never square-consistent (Lemma 1.1(b)).
