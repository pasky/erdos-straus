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

**Corollary 2.3 (the covered part of the fibre is open and dense; PROVED).** Identify `Φ` with `9 + 16ℤ_2` via `x̂_w ↦ w`.
The set `C_Φ` of points of `Φ` lying in some certificate class is open and dense in `Φ`; so the sterile part
`Φ ∖ C_Φ` is closed and **nowhere dense**.
*Proof.* Open: a union of clopen classes. Dense: given `w_0 ≡ 9 (16)` and `m ≥ 4`, run the construction of Theorem 2.1
with `s` odd chosen so that `7^s ≡ −w_0 (mod 2^m)` (possible since `−w_0 ≡ 7 (16)`). The resulting certificate covers
`x̂_w` for `w = −F ≡ w_0 (mod 2^m)`. ∎
*Consequence (Assessment).* This is compatible with TYPEI3 §4 (EVIDENCE that the sterile part of `Φ` has Haar measure
≈ 0.6): the sterile part, if non-empty, is a "fat Cantor set". No sterile point of `Φ` has a sterile neighbourhood, so any
proof that a given point (e.g. `w = 9`) is sterile must use its exact 2-adic coordinate (not `w mod 2^j` for any fixed
`j`), and the measure route of TYPEI3 Remark 4.1 must control infinitely many scales. This upgrades TYPEI4 Prop 4.1
(levels 11–22, `w` only mod 16) to all depths.

## 3. Data: closeness vs. level on complete `(L,b)` lists (CERTIFIED once replayed)

**Computation 3.1.** `typei4_lb L b` (TYPEI4 Comp 3.4; complete per `(L,b)`, all `a`, all heights) was run on the grid
`2^{L−4}·7^b ≤ 2^{28}`, i.e. `b=0: L≤32; b=1: L≤29; b=2: L≤26; b=3: L≤23; b=4: L≤20; b=5: L≤17; b=6: L≤15; b=7: L≤12;
b=8: L≤9` (129 runs, ≈ 1 h on one core). `scripts/typei7_tab.py` re-verifies every row (`Fe = N`, `F ≡ e ≡ 7 (16)`,
Lemma 1.1 in both orientations: 134 checks) and tabulates `max(v_2(F+9), v_2(e+9))` against `t_min = 2+⌈L/2⌉`.
It reproduces Comp 3.4 of TYPEI4 exactly on its range. All 67 certificates (59 distinct divisor pairs):

| L | b | # | closeness (both roles, max) | t_min | margin |
|---|---|---|---|---|---|
| 11 | 0 | 1 | 7 | 8 | 1 |
| 13 | 1 | 1 | 5 | 9 | 4 |
| 14 | 0 / 3 | 2 / 1 | 7,7 / 5 | 9 | 2 |
| 16 | 0 | 3 | 6,5,5 | 10 | 4 |
| 18 | 0 / 1 | 1 / 1 | 5 / 5 | 11 | 6 |
| 19 | 0 | 2 | 5,5 | 12 | 7 |
| 20 | 0 | 4 | 8,6,6,5 | 12 | 4 |
| 21 | 0 | 1 | 5 | 13 | 8 |
| 22 | 1 | 2 | 7,5 | 13 | 6 |
| 23 | 0 | 6 | 8,8,8,8,6,6 | 14 | 6 |
| 24 | 0 / 1 | 2 / 1 | 6,6 / 5 | 14 | 8 |
| 25 | 0 / 1 | 3 / 2 | 8,6,5 / 7,6 | 15 | 7 |
| 26 | 0 | 3 | 10,7,5 | 15 | 5 |
| 27 | 0 / 1 | 5 / 3 | 7,6,6,5,5 / 7,5,5 | 16 | 9 |
| 28 | 1 | 2 | 6,6 | 16 | 10 |
| 29 | 0 | 3 | 6,6,5 | 17 | 11 |
| 30 | 0 | 9 | 7,7,7,7,7,5,5,5,5 | 17 | 10 |
| 31 | 0 | 5 | 7,6,5,5,5 | 18 | 11 |
| 32 | 0 | 4 | 6,6,5,5 | 18 | 12 |

(All other grid cells, in particular every `L ≤ 10` and `L ∈ {12,15,17}`, are empty.) Equal closeness values within a cell
are mostly one divisor pair `(F,e)` reached by two factorisations `c'X² = c''X'²` (e.g. `L=30`: `F=71`, `c'X² = 9·1² = 1·3²`; the
first is the `m=4` certificate of Comp 2.2. It is not a recurrence of the `L=11` triple `(42,32,71)`, which has `c'X²=3`).
By Remark 2.1(b) the `L=11` triple recurs at `L=46, 81, …`, outside the grid.

**Corollary 3.2 (CERTIFIED once replayed; extends TYPEI4 Cor 3.5).** No certificate at `x̂_9` has level `L` and
`v_7(k) = b` with `2^{L−4}7^b ≤ 2^{28}` (grid above), at any height. New relative to TYPEI4 Cor 3.5 / TYPEI6 Cor 4.2:
`b=0, L=27–32`; `b=1, L=27–29`; `b=2, L=25,26`; `b=3, L=23`; `b=4, L=11–20`; `b=5, L=11–17`; `b=6, L=11–15`;
`b=7, L=11,12`. *(Engines: `typei4_lb` alone so far; cross-check with `review_typei4_jsearch.c` in progress, §3.3.)*

**Observation 3.3 (EVIDENCE).** The maximal closeness grows very slowly (≤ 10 for `L ≤ 32`) while `t_min` grows like
`L/2`; the margin `t_min − max` is ≥ 4 for all `L ≥ 16` in the grid and ≥ 10 for `L ≥ 28`. The cell counts do not grow
visibly (≤ 9 per `(L,b)`).

## 4. Level-graded heuristic (Assessment)

Model: the divisor `F` of a fibre certificate is a random class `≡ 7 (mod 16)` modulo `2^{t_min}`; then each of the two roles
hits `x̂_9` with probability `2^{4−t_min}`. Over the 67 certificates of the grid the expected number of hits is
`Σ 2^{5−t_min} ≈ 0.59` (observed: 0); the 31 certificates with `L ≥ 27` contribute only `0.009`. With ≤ 10 certificates per
`(L,b)` cell and `t_min = 2+⌈L/2⌉`, each further `b`-row contributes `≲ 10·Σ_{L≥L_0} 2^{3−⌈L/2⌉}`, e.g. `≈ 2·10^{−3}` for
`L_0 = 33`. This agrees in order of magnitude with the f-graded estimate of TYPEI3 §4 (`≈ 0.012` for `f ≥ 10¹¹`).
The model is **not** a proof: Theorem 2.1 shows that the classes do accumulate at `w = 9`, and nothing excludes a
structured family whose `F mod 2^{t}` drifts towards `−9` with the level. What the exact formula (1.1) shows is that such a
family would need `nδ ≡ 5/9 (mod 2^{⌈L/2⌉−1})`, a condition on which the Pell structure (TYPEI4 Cor 1.4) imposes no
local constraint: for given odd `c', X, D` the equation `16c'X²P_1² − P_1 − c'D² ≡ 0 (mod 2^{L−4})` has a unique
2-adic root `P_1` (Hensel; the derivative `32c'X²P_1 − 1` is odd), so every class of `nδ = c'XD` is locally realised.

**Theorem 2.4 (density with `7 ∤ k` and `k` a power of 2; PROVED).** For every `w_0 ≡ 9 (mod 16)` and `m ≥ 4` there is a
certificate of the shape

```
F = 71^e (e odd),   c = 2^α·7·c',  c' = (71^e+1)/8,   k = 2^γ,   α+2γ = L,   7·2^{L−1} ≡ −1 (mod 71^e),
```

with `−F ≡ w_0 (mod 2^m)`. So Corollary 2.3 holds already for the sub-union of classes with `a=1, b=0, k'=1`: neither the
7-adic tower nor odd parts of `k` are needed to approximate any fibre point, in particular `x̂_9`.
*Proof.* (i) `71 ≡ 7 (16)` and `v_2(71²−1) = v_2(5040) = 4`, so `71²` topologically generates `1+16ℤ_2` and `{71^e : e odd}` is
dense in `7+16ℤ_2`; pick `e` odd with `71^e ≡ −w_0 (mod 2^m)`. (ii) `ord_71(2) = 35 = (71−1)/2` and `2^{70} ≢ 1 (mod 71²)`
(`2^{70} ≡ 143`), so `ord_{71^e}(2) = 35·71^{e−1}` and `⟨2⟩` is the subgroup of squares of `(ℤ/71^e)^×`. `−7^{−1}` is a square
mod 71 (`2^{29} ≡ −7^{−1} (mod 71)`), hence mod `71^e` (Hensel). So an `L ≥ 7` with `2^{L−1} ≡ −7^{−1} (mod 71^e)` exists
(namely `L ≡ 1 + log_2(−7^{−1}) (mod 35·71^{e−1})`). (iii) Certificate conditions: `F ≡ 7 (16)` so `c'` is odd;
`F ≡ 1 (mod 7)` so `7 ∤ c'` and `F ≡ 1 (mod 7^{v_7(ck)} = 7)`; `c' | F+1`; `F` is prime to `4ck = 2^{L+2}·7c'`;
`N = 1+2^{L+2}·7c' ≡ 1 + 7·2^{L−1} ≡ 0 (mod F)` since `8c' ≡ 1 (mod F)`; `v_7(c) = 1` is odd. ∎
*Check.* `e = 1` gives `L ≡ 30 (mod 35)`; the `L = 30` certificate `(c',X) = (9,1)`, `F = 71` of Comp 3.1 is this one.

**Computation 2.5 (CERTIFIED once replayed; `scripts/typei7_dense71.py 14`, 1 min).** Least odd `e` with `71^e ≡ −9 (mod 2^m)`
and least level `L` (discrete log mod `35·71^{e−1}`, Pohlig–Hellman), each certificate checked by modular arithmetic
(`F | N`, (2.2)):

| m | e | bits of F | v_2(F+9) | L | t_min |
|---|---|---|---|---|---|
| 4 | 1 | 7 | 4 | 30 | 17 |
| 5 | 3 | 19 | 5 | 109 685 | 54 845 |
| 6 | 7 | 44 | 6 | 419 119 864 270 | ≈ 2.1·10¹¹ |
| 7–10 | 15 | 93 | 10 | ≈ 2^91 | ≈ 2^90 |
| 11 | 143 | 880 | 11 | ≈ 2^879 | ≈ 2^878 |
| 12–14 | 399 | 2454 | 14 | ≈ 2^2452 | ≈ 2^2451 |

So the approximating certificates exist explicitly, but their level is of the size of `F` itself (the discrete log is
"random" in `[0, ord_F(2))`), while `e` (hence `log_2 F`) grows like `2^m`; so `v_2(F+9) ≈ log_2 log_2 L` in this family,
whereas `x̂_9` needs `v_2(F+9) ≥ 2+⌈L/2⌉`.

## 5. Status and what remains open

* PROVED: the exact closeness formula (Lemma 1.1: `v_2(F+9) = 3 + v_2(5 − 9nδ − 2^{L−2}c_ok_o²)`; a certificate at
  `x̂_9` ⟺ `nδ ≡ 5/9 (mod 2^{⌈L/2⌉−1})`); unboundedness of the closeness (Thm 2.1 — answers the open question of TYPEI4
  §5 / Assessment 4.2(d) negatively: **no** ball around 9 in the fibre is sterile); recurrence of every fibre triple at all
  levels `≡ L_0 (mod ord_F(2))` with constant closeness (Remark 2.1(b)); the covered part of `Φ` is open and dense and
  the sterile part nowhere dense (Cor 2.3), already with `F = 71^e`, `k = 2^γ`, `7 ∤ k` (Thm 2.4).
* CERTIFIED once replayed: Comp 2.2, 2.5 (explicit approximants up to closeness 14); Comp 3.1 / Cor 3.2 (complete
  `(L,b)` grid `2^{L−4}7^b ≤ 2^{28}`: no certificate at `x̂_9`; max closeness ≤ 10, margin ≥ 1, ≥ 10 for `L ≥ 28`).
* Assessment / EVIDENCE: §4 level-graded heuristic (expected hits in the grid 0.59, observed 0; tail ≲ 10^{−2}).
* NOT achieved (precise negative statement): an inequality `v_2(F+9) < 2+⌈L/2⌉` for all fibre certificates is exactly
  sterility of `x̂_9` (by Lemma 1.1 and the Criterion), and by Cor 2.3 / Thm 2.4 it cannot follow from any statement
  about `F mod 2^j` for a fixed `j`, nor from any argument that is uniform on a neighbourhood of `w = 9`, nor from
  bounded 7-depth or `k'=1` restrictions alone (Thm 2.4 lives at `b=0, k'=1`). A proof must couple the 2-adic size of
  `F+9` with the level, e.g. a bound of the form "`F ≡ −9 (mod 2^t)` forces `ord`/discrete-log information on `2 mod F`
  incompatible with `2^{L−1}7^sX ≡ −g (mod F)`" (Remark 1.6 / §2 form: `F | 2^{L−1}7^sX + g`, `(F+1)/8 = c'gX`). We have
  no such tool; sterility of `x̂_9` remains open (Conjecture TYPEI2 3.4), and so does `C(7) = ∞` under H.

## Replay

```
gcc -O2 -o /tmp/lb scripts/typei4_lb.c -lm
# Comp 3.1 grid (≈1 h, one core): all (L,b) with L>=7, 2^(L-4)*7^b <= 2^28
for b in 0 1 2 3 4 5 6 7 8; do for L in $(seq 7 32); do
  python3 -c "import math,sys;sys.exit(0 if $L-4+$b*math.log2(7)<=28.01 else 1)" && /tmp/lb $L $b > /tmp/t7/lb_${L}_${b}.txt
done; done
uv run python scripts/typei7_tab.py /tmp/t7/lb_*.txt          # table of §3; 67 certs, 134 Lemma-1.1 checks, no HIT
gcc -O2 -o /tmp/t7/js scripts/review_typei4_jsearch.c -lm     # second engine (R89), per cell: /tmp/t7/js L b > /tmp/t7/js_L_b.txt
uv run python scripts/typei7_xcheck.py /tmp/t7                # compares lb vs js cell by cell
PYTHONPATH=scripts uv run --with sympy python scripts/typei7_unbounded.py 5    # Comp 2.2 (m = 4, 5)
uv run --with sympy python scripts/typei7_dense71.py 14                         # Comp 2.5 (1 min)
uv run --with sympy python scripts/typei7_family.py 30 11 14 3                  # fixed-(c',g) family engine, sanity (2 rows)
```
