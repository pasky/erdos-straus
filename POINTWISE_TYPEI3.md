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

**Lemma 1.2 (f-bound ⇒ height bound; PROVED).** If `ck≤X` (and `7|c`), then
`min(F,e)≤√N<2X/√7+1`. Hence: no certificate at `x̂_w` with
`min(F,e)<Y` ⟹ no certificate with `ck≤(Y−1)√7/2≈1.3229(Y−1)`.
*Proof.* `4ck²=4(ck)²/c≤4X²/7`, and one of two complementary divisors is `≤√N`. ∎

**Search criterion (from Lemma 1.1).** Given `f`, put `R=7^{v+b}k'm' mod f`. A
certificate with divisor `f` exists iff for some admissible `(m',k',v,a)` and
`s=t+γ` we have `2^s R≡−1 (mod f)` with `⌈(s+2)/2⌉≤t≤min(s, T_role)`, where
`T_F=v_2(f+w)`, `T_e=v_2(wf+1)`. As `γ≤t−2`, `s≤2T−2≤2log₂(f+|w|)`: only
**small** powers of 2 are relevant (no discrete logarithm needed).

## 2. Computation: the f-graded search (CERTIFIED once run; see Replay)

`scripts/typei3_fsearch.c` (`r w Ylo Yhi`) runs over `f≡1 (7)`, `f≡−w (4)` in
`[Ylo,Yhi)`, factors `(f+1)_odd` by a segmented sieve, and tests Lemma 1.1
for every `m'|(f+1)_odd`, `k'|m'`, `1≤v≤v_7(f−1)`, `a` odd, both roles,
`2≤t≤T_role`, `0≤γ≤t−2`. It is complete for all certificates having a
divisor `f` in range, at any height. Hits are re-verified by the stand-alone
exact checker `scripts/typei3_verify.py`.

*Cross-check (agreement of certificate sets).* `scripts/typei3_cmp.sh r w X` compares,
for all certificates with `ck≤X`, the output of the independent ck-graded
checker `typei2_signcheck.c` with `typei3_fsearch` on `f<2X/√7+2`. At
`X=2·10⁵` the sets coincide exactly for
`(r,w)=(7,1),(7,−7),(7,25),(7,41),(7,17),(7,−15),(11,9),(19,9),(23,1),(7,9)`
(3, 0, 0, 0, 13, 35, 7, 4, 2, 0 certificates).

## 3. Scope of any sterility proof: sterile points are nowhere dense (PROVED)

**Proposition 3.1.** The set `St_7` of sterile points of `Σ_7` is closed and has
empty interior. In particular every clopen neighbourhood of `x̂_9` contains
non-sterile points (covered by certificates with `k=1`, `t=2`, height `7p`).
*Proof.* Closed: `St_7=⋂_X U_X` (proof of Thm A(iii)). Let `x∈Σ_7` and
`U={y: y≡x (mod Q)}`, `Q=2^j7^i∏_{q∈P}q^{e_q}` (P a finite set of odd primes
`≠7`); such U form a neighbourhood basis. Pick a prime `p∉P∪{2,7}` and put
`c=7p`, `k=1`, so `4ck=28p`, `t=2`, `v=1`, `m'=p`, `s=7p∉{1,2,3,6}`. Pick a prime
`F∉P∪{2,7,p}` with `F≡3 (4)`, `F≡−x_7 (7)` and `(−7p/F)=1`. This is a
condition on `F mod 28p`: `(−7/F)=(F/7)=(−x_7/7)=(−1/7)(x_7/7)=1` as `x_7` is a
non-square mod 7, and `(p/F)=(F/p)(−1)^{(p−1)/2}` (F≡3 mod 4) fixes the class
of F mod p as squares or non-squares. So Dirichlet gives such F. Then
`Cl(7p,1,F)={y≡−F (28p), y²≡−28p (F)}` meets U: at 2 the conditions are
`y≡−F≡1 (4)`, compatible with `y≡x_2≡1 (8)`; at 7, `y≡−F≡x_7 (7)`; at p and at F
(outside P) they are free congruences with a solution (`−28p` is a square mod
F); at `q∈P`, `y≡x (q^{e_q})`. By CRT, `U∩Cl≠∅`; points of `Cl` are not
sterile. ∎

*Consequence (scope).* A proof that `x̂_9` is sterile cannot be a congruence
argument modulo a fixed modulus, as in Lemma 2.1 or Lemma 3.1 of POINTWISE_TYPEI2 (those
prove sterility of a whole clopen set of slices or families, never of a point
neighbourhood). It must use that `x̂_q=1` exactly at infinitely many q. Inside the
sign family `{x̂_w}` this means that `w=9` is exact 2-adic data: by Lemma 1.1 the
2-adic depth available to a divisor `f` is `v_2(f+9)` (resp. `v_2(9f+1)`), a
quantity with no uniform bound.

**Computation 2.1 (CERTIFIED by one engine; cross-checked as above).**
`typei3_fsearch 7 9 1 10^11` (run as `[1,10⁸)`, `[10⁸,5·10¹⁰)`, `[5·10¹⁰,10¹¹)`;
3 571 429 + 1 782 142 857 + 1 785 714 285 values of f; ≈55 min per half on one core
before the speed-ups): **0 certificates.**

**Corollary 2.2.** (i) *(CERTIFIED)* No certificate at `x̂_9` has a divisor
`f=min(F,e)<10¹¹`, at any height. Hence (Lemma 1.2) none has `ck≤1.32·10¹¹`,
and every finite Type-I covering of `{n_p=7}` has height `>1.32·10¹¹`
(was `>3·10⁹`, POINTWISE_TYPEI2 Cor 3.3). (ii) *(CONDITIONAL on H for the finite family `𝓟_X` of
Theorem A built from `x̂_9`, X=1.32·10¹¹)* infinitely many hard primes have
`n_p=7` and `ck_min(p)>1.32·10¹¹`; so `C(7)>1.32·10¹¹` under H.
*Proof.* As POINTWISE_TYPEI2 Cor 3.3, with Computation 2.1 + Lemma 1.2 in place of Computation 3.2. ∎

## 4. The sign fibre: f-graded near-miss mass (EVIDENCE / Assessment)

Fibre `Φ={x̂_w : w∈9+16ℤ_2}`, Haar measure on `w` normalised to 1. By Lemma 1.1,
for each `f≡7 (16)` (both roles force this when `t≥4`) the certificates having
divisor `f` kill the union of two nested-ball families, i.e. at most the two balls
`−f+2^{t_min}ℤ_2` and `−f^{−1}+2^{t_min}ℤ_2`, where `t_min(f)` is the least
admissible `t≥4` over all `(m',k',v,a,s)` with `2^sR≡−1 (f)` (`t=⌈(s+2)/2⌉`).
(`t≤3` certificates would kill all of Φ; Computation 2.1 shows none has
`f<10¹¹`.) `typei3_fsearch 7 9 lo hi mass` prints `t_min(f)` and the per-bin
union-bound mass `Σ 2·2^{4−t_min}` (t capped at 40); `typei3_union.py` computes the
exact measure of the union of the balls.

| f-range | f with t_min≤40 | mass in bin | uncovered measure of Φ (exact union) |
|---|---|---|---|
| < 2¹⁰ | 5 | 0.125 | — |
| [2¹⁰,2²⁰) | 81 | 0.59 | 0.6636 (f<2²⁰) |
| [2²⁰,2²⁸) | 142 | 0.16 | 0.6412 (f<2²⁸) |
| [2²⁸,2²⁹) | 30 | 0.063 | 0.6103 |
| [2²⁹,2³⁰) | 27 | 0.0011 | 0.6103 |
| [2³⁰,2³¹) | 35 | 0.0012 | 0.6103 |
| [2³¹,2³²) | 42 | 0.0016 | 0.6100 |
| [2³²,10¹⁰) | 39 | 0.0003 | 0.6099 |

Observations. (a) The number of f per dyadic bin that carry any near miss grows
slowly (≈10 → ≈40). (b) But `t_min(f)` grows like `½log₂f` (least `t_min` in bin
`2^j`: 8–15 for j≤27, 15–19 for j=29–33), so the 2-adic weight `2^{4−t_min}` decays
like `f^{−1/2}`, and the mass per bin decays (spikes such as j=28, `t_min=9`, are
isolated). (c) Hence ≈61% of the fibre survives all certificates with
`f<10¹⁰` (in particular with `ck≤1.3·10¹⁰`), and the decrement over the last five bins is
`3·10⁻⁴`.

*Assessment.* If `t_min(f)≥½log₂f−C` persists and the number of near-miss f per bin
grows only polylogarithmically, the expected number of certificates at a
Haar-random `w` with `f≥10¹¹` is `≈Σ_{j≥37} 40·2^{5−j/2}≈2·10⁻³`. This supports
Conjecture 3.4 for `x̂_9`, and suggests the stronger statement: **the sterile
points of Φ have positive measure (≈0.61)**. Note this differs from the ck-graded
§5 of POINTWISE_TYPEI2: a small `f` produces near misses at all heights
`ck=2^{t−2}n` with `t` in an arithmetic progression, so the ck-grading spreads one
f over many bins.

**Remark 4.1 (measure route; PROVED reduction).** Theorem A(iii) needs *some*
sterile point, not `x̂_9`. If `μ(U_Y)>Σ_{f≥Y}mass(f)`, where `U_Y⊂Φ` is the
(computed) set surviving all `f<Y`, then Φ contains a sterile point, so
`C*(7)=∞` under H. With `Y=10¹⁰`, `μ(U_Y)≈0.61`. So an explicit tail bound
`Σ_{f≥10¹⁰} 2^{5−t_min(f)}<0.6` would suffice. This is a counting problem: bound
the near misses with `t≤T` by `o(2^{T})` explicitly. It is open. (Heuristic sketch, not
a proof: in (2.1) with `J≤J'` one has `u | c'J²+Λ` and `c'J | Λ+u`; a Lenstra-type
bound on divisors in a residue class (Lenstra 1984: at most 11 divisors of n in a
class mod `s≥n^{1/3}`) then suggests only `#certificates(level)≪Λ^{1/2+ε}`. Against the box measure
`2^{−(2+α+γ)}7^{−(a+b)}`, the exponent ½ is exactly borderline in the `γ`, `b`
directions.)

## 5. Vieta descent: the low 2-levels are empty (PROVED)

**Lemma 5.1 (Vieta descent).** Let `c,k,δ≥1` and `F,e≥1` be integers with
`Fe=1+4ck²` and `e−F=4ckδ`. Then `F≡e≡1 (mod 4cδ)`.
*Proof.* Induction on k. If `F=1`, then `4ckδ=e−1=4ck²`, so `k=δ`, `e=1+4cδ²`, and
the claim holds. If `F>1`, put `ρ=k−δF`. From `F²+4ckδF=1+4ck²` we get
`F²−1=4ckρ`, so `1≤ρ<k`. Put `F'=F−4cρδ`. Then
`F'F=F²−4cρδF=1+4ckρ−4cρδF=1+4cρ²>0`, so `F'≥1`, and `F−F'=4cρδ`. By induction
(applied to `(c,ρ,δ,F',F)`), `F≡F'≡1 (mod 4cδ)`, and `e=F+4ckδ≡F`. ∎

(Equivalently, `((F+e)/2,k)` runs over the solutions of
`A²−4c(1+cδ²)k²=1`, and the descent shows that `(1+2cδ², δ)` is the fundamental one.
Brute-force check: all 39 660 pairs with `c,k<200` satisfy the conclusion `F≡e≡1 (mod 4)`.)

**Corollary 5.2 (PROVED).** Let `w≡9 (16)`. A certificate `(c,k,F)` at `x̂_w` has
`t=v_2(4ck)≥5` and `α+2γ≥5`. (Recall `c=2^α…`, `k=2^γ…`, `t=2+α+γ`.)
*Proof.* Put `e=N/F`. By Lemma 1.1, `F≡−x̂`, `e≡−x̂^{−1} (mod 4ck)`. The odd components
of `x̂` are `±1`, and `w≡w^{−1} (mod 16)` (as `81≡1`). So `e≡F (mod 2^{min(t,4)}n)`, where `n`
is the odd part of `ck`. Also `F≡−w≡7 (mod 8)` if `t≥3`, and `F≡3 (mod 4)` if `t=2`; in all cases
`F≢1 (mod 4)`. `F≠e` by Lemma 3.1 of POINTWISE_TYPEI2 (no square-family certificate at `x̂_w`, `w≡9 (16)`).
* `t≤4`: then `e≡F (mod 4ck)`, and Lemma 5.1 gives `F≡1 (mod 4)`, a contradiction.
* `t≥5` and `α≥2(t−4)` (equivalently `α+2γ≤4`): put `c̃=c/4^{t−4}`, `k̃=2^{t−4}k` (integers). Then
  `4c̃k̃²=4ck²` and `4c̃k̃=16n`. Since `e≡F (mod 16n)`, Lemma 5.1 applies to `(c̃,k̃)`
  and again gives `F≡1 (mod 4)`, a contradiction. ∎

The near-miss data agree. In the dump `typei3_nmdump 7 9 10⁸` (932 near misses with `−F≡1 (8)`,
`t≥4`), every one with `t≤4` or `α+2γ≤4` is a square (`F=e`).

*Scope (what the descent gives for `α+2γ≥5`).* Put `λ=2^{t−4}`, `c̃=c/λ²∈ℤ[1/2]`, `K=λk`,
`δ=(e−F)/16n`. Then `Fe=1+4c̃K²` and `e−F=4c̃Kδ`, and the step
`(K,F)↦(ρ,F')=(K−δF, F−4c̃ρδ)` still preserves the equation. It is multiplication by a
fixed real quadratic unit, so it ends after finitely many steps at a reduced pair with
`F_end∈ℤ[1/2]`, `0<F_end≤1`. (If `ρ_end≤0`, then `F_end²≤1`. On all 932 near misses of the dump, `scripts/typei3_descent.py`
terminates within ≤156 steps. Long chains occur when `δ` is small and `c̃` tiny. The intermediate F have
2-adic valuation decreasing by a fixed amount per step.)
The steps move F by `4c̃ρδ`, which is divisible by `c_o` (the odd part of c) at every odd prime.
So `F≡F_end (mod c_o)`, `F_end=a/2^m≤1`. Lemma 5.1 is the case `F_end=1`. When
`c̃∉ℤ`, `F_end<1` occurs, and the congruence `F≡a/2^m (mod c_o)` does not contradict
`F≡−1 (c')`, `F≡1 (7^a)`. So the obstruction in Cor 5.2 is special to
`α+2γ≤4`. It does not extend unless the 2-adic part of the orbit is controlled exactly.
That is possible only with the exact value `w=9`, never modulo a fixed `2^j` (compare Prop 3.1).

## Replay

```
gcc -O2 -o /tmp/fsearch scripts/typei3_fsearch.c -lm
gcc -O2 -o /tmp/signcheck scripts/typei2_signcheck.c -lm
/tmp/fsearch 7 1 1 2000                      # sanity: finds (14,2,15), (602,14,687), (29498,2,687)
# cross-check vs the ck-graded checker (edit binary paths in the script first):
for a in "7 1" "7 -7" "7 25" "7 41" "7 17" "7 -15" "11 9" "19 9" "23 1" "7 9"; do scripts/typei3_cmp.sh $a 200000; done
# Computation 2.1 (2 cores, ulimit -v 8000000):
/tmp/fsearch 7 9 1 100000000; /tmp/fsearch 7 9 100000000 50000000000; /tmp/fsearch 7 9 50000000000 100000000000
# §4 mass and exact union (≈15 min per 5·10⁹ on one core):
/tmp/fsearch 7 9 1 100000000 mass > m1.txt; /tmp/fsearch 7 9 100000000 5000000000 mass > m2.txt
/tmp/fsearch 7 9 5000000000 10000000000 mass > m3.txt
PYTHONPATH=scripts uv run python scripts/typei3_union.py m1.txt m2.txt m3.txt
# verify any hit:
PYTHONPATH=scripts uv run python scripts/typei3_verify.py 7 9 c k F
```
