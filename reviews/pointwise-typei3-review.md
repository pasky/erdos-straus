# R72 — hostile review of POINTWISE_TYPEI3.md (task O72)

Reviewer: side agent R72 (branch `side-agent/review-typei3`), merged author branch
`side-agent/sign-point-sterility` (incl. Prop 5.5 / Remark 5.6). From-scratch code:
`scripts/review_typei3_fs.c` (f-graded engine), `scripts/review_typei3_naive.c` (definition-only brute
force, no Lemma 1.1), `scripts/review_typei3_check.py` (exact verifier/converter).

Status: in progress (verdicts below are filled in claim by claim).

## Verdicts

### Lemma 1.1 (small-divisor reduction) — SOUND
Re-derived. With `c=2^α7^a c'`, `k=2^γ7^b k'`: `4ck²=2^{2+α+2γ}7^{a+2b}c'k'²=2^{t+γ}·7^{v+b}m'k'`, so (iii)
is exactly `f|N`. `N≡1 (mod 4ck)` makes `e≡F^{-1}`, and `(−x̂)^{-1}` has components `−1, 1, −w^{-1}`
at `m'`, `7^v`, `2^t`, giving (i), (ii). Converse: `f|N` ⇒ `(f,4ck)=1`; in the e-role `N/f≡f^{-1}` lands
in the `−x̂` class. `a≥1` odd ⇒ `7|sf(c)`. Both roles force `f≡1 (7)` and `f≡−w (4)` (odd `w` is its own
inverse mod 4), so the engines' progression filter `f≡f₀ (mod 4r)` loses nothing.
Search criterion: `γ≥0 ⇔ t≤s`, `γ≤t−2 ⇔ t≥⌈(s+2)/2⌉`; correct. Finiteness only for finite role depth
(the author's restriction after the self-review is correct; my engine reproduces the abort at
`(r,w,f)=(7,−15,15)`).

Lemma 2.1 of TYPEI2 (only `v_7(c)` odd can occur at `x̂`) is used implicitly to restrict the search.
Independent check: the naive search with **no** parity filter (`… all`, any `c` with `sf(c)∉{1,2,3,6}`,
`ck≤10⁵`, divisor ≤1000) finds no certificate with `v_r(c)` even at `(7,9),(7,25),(23,9),(7,1)`.

### Lemma 1.2 (height constant) — SOUND
`7|c ⇒ 4ck²=4(ck)²/c≤4X²/7`, `√(1+A²)<A+1`. So a certificate with `min(F,e)≥Y` has
`ck>(Y−1)√7/2=1.32288(Y−1)`. For r: `√r/2` = 2.3979 (23), 2.7839 (31), 3.4278 (47); the stated
`2.39/2.78/3.42·10¹¹` are correct, conservative roundings. Note the constant uses only `r|c` (c≥r), which
holds for every certificate at `x̂` by Lemma 2.1 of TYPEI2.

### Computation 2.1 / Cor 2.3 (f-graded searches) — see "Independent computations" below.

### Lemma 5.1 (Vieta descent) — SOUND
Re-derived: `F²+4ckδF=1+4ck²` ⇒ `F²−1=4ckρ`, `ρ=k−δF∈[1,k)` when `F>1`; `F'F=1+4cρ²`; induction on k.
The proof never uses that the coefficient is `4c`: it holds verbatim for any integer `B≥1` in place of `4c`
(this generalisation is what P5.3–P5.5 actually use, with `B=4c̃` odd at level 6). Brute force
(`review_typei3_vieta.py` (1), general `B≤60`, `K≤150`): 9102 pairs, 0 failures.

### Cor 5.2 (`t≥5`, `α+2γ≥5`) — SOUND
Rescaling `c̃=c/4^{t−4}`, `k̃=2^{t−4}k` is integral iff `α≥2(t−4)` ⇔ `α+2γ≤4`; `4c̃k̃=16n` and `e≡F (16n)`
since `w≡w^{-1} (16)`. `F≠e` by TYPEI2 L3.1. Brute force (vieta.py (2)): all `(c,k)`, `ck≤2·10⁴`, `v_7(c)` odd,
`t≤4` or `α+2γ≤4`, all divisors F, conditions for *some* `w∈9+16ℤ_2` (`F≡7 mod 2^{min(t,4)}`): 0 certificates.

### Prop 5.3 (levels 5,6 ⇒ `c'=1`; δ odd) — SOUND
At levels 5/6 `B=4c̃=2^{6−α−2γ}c_o∈ℤ`, and `e−F=16nδ=B·Kδ` with `K=2^{t−4}k` (checked: `B·K=c_o k_o 2^{α+2γ−2}·2^{6−α−2γ}=16n`).
Lemma 5.1 (general B) ⇒ `F≡1 (mod Bδ)` ⊇ `c_o`. With `F≡−1 (c')`: `c'|2` ⇒ `c'=1`. `v_2(e−F)=v_2(w−w^{-1})=v_2(w²−1)=4`
for `w≡9 (16)`, and `t≥5` makes this the valuation of `e−F`; so δ odd. Brute force (vieta.py (3), odd parts <60,
no certificate conditions): 6360 pairs with `16n|e−F`, all `F≡1 (mod c_o)`.

### Prop 5.4 (level 5 empty) — SOUND
Mod-16 chain `(F,H)↦(F+14H,F+15H)` re-derived; from-scratch run over `a∈{1,3,5,7}`, odd δ<32, 64 steps:
divisor residues mod 16 are exactly `{1,15}`, never 7 (`review_typei3_level6.py` (a)).

### Prop 5.5 (level 6 empty) — SOUND
Re-derived every step:
* Chain: `F_{i+1}=F_i+BK_iδ`, `K_{i+1}=F_{i+1}δ+K_i` preserves `F_iF_{i+1}=1+BK_i²`, `F_{i+1}−F_i=BK_iδ` (checked by
  `F_{i+1}²=F_{i+1}(F_i+BK_iδ)=1+BK_i²+BK_iδF_{i+1}`); the descent of L5.1 (general B) lands every oriented pair on
  the chain from `(δ,1)` with the *same* δ. `H=K/δ`, `D=Bδ²`, `v_2(H)=v_2(K)=α+2γ−2=4`.
* Norm: `(F+e)²−dH²=(e−F)²+4Fe−D(D+4)H²=D²H²+4+4DH²−D²H²−4DH²=4`. The step equals multiplication by
  `ε=(D+2+√d)/2` (checked both coordinates: `X'=((D+2)X+dH)/2`, `H'=((D+2)H+X)/2`). ε is integral
  (root of `x²−(D+2)x+1`), `η²=ε`, `η−η^{-1}=√D`, `η+η^{-1}=√(D+4)`, so for odd m `X−2=DU_m²`, `H=U_mW_m`
  with `U_m,W_m∈ℤ`; `U_3=D+3`, and `U_3|U_{3j}` for odd j.
* Mod-32 claim: `D=7^aδ²` mod 32 ∈ {7,15,23,31} (a odd); from-scratch run mod 2¹⁰ over all 128 residues
  `7^aδ² mod 2¹⁰`: every index with `H≡16 (32)` has `m≡3 (mod 6)`; 0 violations.
* Clash: `D≡7 (8)` ⇒ `(D+3)/2` odd, ≥5, prime to 7; `q|(D+3)|H` ⇒ `q|k'` ⇒ `F≡e≡−1 (q)`; but
  `F,e=(X∓DH)/2≡1 (q)`. Correct.
* Exact check (level6.py (b)): `a∈{1,3,5}`, odd δ<400, 60 chain steps: 3000 positions with `v_2(H)=4`, all
  satisfy `(D+3)|H`, `D(D+3)²|X−2`, and the clash at the least prime of `(D+3)/2`; Pell identity holds everywhere.
* Definition-level brute force without any chain/Pell input (level6.py (c), `c=2^α7^a c'`, `k=2^γ7^b k'`, odd
  7-free `c',k'≤25`, `a∈{1,3}`, `b∈{0,1}`, all divisors F, `F≡7 (16)` + odd-prime conditions): 0 hits at levels
  5, 6 (and 7). Controls: dropping `F≡−1 (m')` gives 66/40/32 hits, so the test has power.
Remark (not a defect): P5.5 does not use `w` beyond `δ` odd and `F≢1`; it is a statement about odd-part
conditions. Remark 5.6 (level 7 open) is correctly labelled.

### Prop 3.1 (sterile set closed, nowhere dense) — SOUND; scope correctly weakened
Re-checked: `U⊂Σ_7` once `2^3·3·5·7 | Q`. For `F≡3 (4)`: `(−7/F)=(−1/F)(7/F)=(−1)(−(F/7))=(F/7)=(−x_7/7)=1`;
`(p/F)=(F/p)(−1)^{(p−1)/2}`, so all conditions on F are classes mod `28p` (coprime pieces) and Dirichlet applies.
`Cl(7p,1,F)∩U≠∅` by CRT (2: `1 mod 4` vs `x_2≡1 (8)`; 7: `−F≡x_7`; p, F free; root of `y²≡−28p (F)` is a unit).
`sf(7p)=7p∉{1,2,3,6}`. Closedness from `St_7=⋂U_X`.
What it does **not** say (the current text is accurate on this after the self-review): nothing about
non-emptiness of `St_7`; nothing about thin sets (the fibre Φ is itself nowhere dense in `Σ_7`, so a sterile
positive-Φ-measure set is not excluded; a closed positive-measure nowhere-dense set — fat Cantor type — is
perfectly possible inside Φ); nothing about arguments using infinitely many coordinates of `x̂_9`. Note also
that the heights `7p` of the killing certificates are unbounded as `U` shrinks, as they must be.
Minor wording: "no ambient cylinder around `x̂_9` is sterile" is true for *every* point of `Σ_7`, so it carries
no information specific to `x̂_9` (MINOR, see D-list).

### §4 near-miss mass ≈61% — EVIDENCE label correct; numbers independently reproduced to 10⁸ (more below)
From-scratch `tmin` mode of `review_typei3_fs.c` vs author `mass` mode on `f<10⁸`: the 198 `B f t_min` lines are
**identical**. From-scratch exact union (`review_typei3_union.py`, exact rationals, nested/disjoint balls):
uncovered 0.641806 at the last f below 10⁸, identical to `typei3_union.py`.
Ball measure: `w∈−f+2^tℤ_2` has measure `2^{−t}/2^{−4}=2^{4−t}` in Φ, two roles ⇒ `2^{5−t}`; truncation error
`(Y/112+1)·2^{−36}≈0.0013` at `Y=10¹⁰` re-derived. Heuristic tail `Σ_{j≥37}40·2^{5−j/2}=0.01179` re-derived.

### Remark 4.1 (measure route) — SOUND (as a reduction)
Φ compact, balls clopen; every certificate at `x̂_w` is recorded at both of its divisors, in particular at
`f=min(F,e)`, so the killed set is `⊆ ⋃_{f<Y}B_f ∪ ⋃_{f≥Y}B_f`; `μ(U_Y)>Σ_{f≥Y}mass(f)` gives `w∈Φ` killed by no
certificate with `v_7(c)` odd, and TYPEI2 L2.1 (x̂_w is a "square point": `w≡1 (8)` is a 2-adic square) removes
`v_7(c)` even; so `x̂_w` is sterile in `Σ_7` and Theorem A(iii) applies (CONDITIONAL on H). f's with `f≢7 (16)`
carry no certificates at any `w∈Φ` by Cor 5.2 (`t≥5`), so restricting the mass to `f≡7 (16)` is justified —
the text should cite Cor 5.2 for this (currently it says "`t≤3` certificates would kill all of Φ; Computation 2.1
shows none has f<10¹¹", which is weaker than needed for a tail over *all* f≥Y; see D-list).
"not necessarily `x̂_9`": correct and important — positive measure gives no information about `w=9`.

## Independent computations (priority 1: completeness of the f-graded search)

All with my own engine `review_typei3_fs.c` (written from the definition; own sieve with Fermat inverses,
own `(c',k')` enumeration as exponent pairs `i+j≤E`, `R=7^{a+2b}c'k'²`, explicit `(α,γ)` loop), its output
re-verified line by line with exact integers by `review_typei3_check.py`.

1. *Engine vs naive definition-level brute force* (`review_typei3_naive.c`: all `(c,k)` with `ck≤3·10⁵`,
   `v_r(c)` odd, every odd divisor ≤3000 of N in **both** roles, conditions (2.2) tested directly — no use of
   Lemma 1.1, no progression filter) — identical certificate sets for
   `(r,w)=(7,1),(7,9),(7,17),(7,25),(7,41),(7,−7),(7,5),(7,−3),(11,9),(19,9),(23,9),(23,1),(31,9)`
   (3,0,14,0,0,0,0,0,8,3,0,1,0 certificates) and `(7,−15)` on `f≥16` (12=12).
2. *Engine vs author's `typei3_fsearch`, full output at all heights, `f<10⁷`*: identical certificate sets for
   `(7,1)` 10, `(7,17)` 47, `(7,−15)` (f≥16) 101, `(11,9)` 28, `(19,9)` 31, `(23,1)` 9, `(7,−7)` 0, and the
   deep test point `w=2⁴³−743` (2 certificates, incl. `(14,2⁴⁰,743)` with `t=43`): both engines find
   the `t=43` certificate. All of my reported certificates verify exactly (0 invalid).
3. *No-parity control*: naive search over all c with `sf(c)∉{1,2,3,6}` (`ck≤10⁵`, divisor ≤1000) at
   `(7,9),(7,25),(23,9),(7,1)` finds no certificate with `v_r(c)` even (TYPEI2 L2.1 consistent).
4. *`w=9`, `f<10⁸`*: both engines test 3 571 429 values of f, 0 certificates.
5. *Near-miss (`t_min`) data, `f<10⁸`*: identical 198 `B` lines (see §4 above).
6. Overflow/array audit of `typei3_fsearch.c`: modular products are `u128`; `xs<f<2⁴⁰` doubling cannot
   overflow; the `(m',k')` table (400 000) exceeds the maximum `∏(E+1)(E+2)/2=91 854` over odd 7-free
   `A≤2.5·10¹¹` (my DP over non-increasing exponent vectors); `MAXF=16` distinct primes suffices. Hit
   detection precedes the `u128` reconstruction, so overflow there could only garble *printed* hits.
