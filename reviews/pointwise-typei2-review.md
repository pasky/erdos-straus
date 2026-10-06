# Review R69 of POINTWISE_TYPEI2.md (task O69, branch side-agent/typei-sterile)

Reviewer: hostile side agent R69 (branch side-agent/review-typei2). Reviewed
author commit `5c66f67`. Status: in progress.

## Summary verdicts

| claim | verdict |
|---|---|
| Thm A (i) | SOUND-AFTER-REPAIRS (D1: the "every p>2X_r" form is overstated; limsup statement fine) |
| Thm A (ii), (iii) | SOUND (re-derived Steps 1–5 line by line, incl. the `v_q(4X!)` perturbation fix) |

## Re-derivation notes

### Theorem A

Definitions checked against notes (36.1) (`𝓑_p`: `k≤⌊2p/3⌋`, `c≤⌊(2p+k)/4k⌋`,
`(p,ck)=1`), POINTWISE_TYPEI §0 (`M_{c,k}`, `ck_min`, hard = `p≡1 (24)`).

* (i) `p>2X`, `ck≤X` ⇒ `(c,k)∈𝓑_p`: `4ck≤4X<2p≤2p+k` ✓, `k≤X<p/2≤2p/3` ✓,
  `p∤ck` as `p>X≥c,k` ✓. See D1 for the membership `p∈⋃Cl` itself.
* Step 1: `Cl(κ)` is clopen (defined mod `4ckF`); `Σ_r` compact ✓.
* Step 2: root uniqueness ✓ (`−4V=x_q²` fixes V); q=2 or `q|V` gives unit
  `N_V(x_q)` ✓. Perturbation: `N_V(x+q^T)=q^T(2x+q^T)`, q odd, x unit ⇒
  `v_q=T` exactly ✓; other `V'` keep valuation since `T>v_q(N_{V'}(x))` ✓.
  `𝒞⊂Σ_r` needs `B≥r`, `E_2≥3`, `E_3≥1` ✓ (but see D1 about units at q>B).
* Step 3: the repair is correct and needed: `x*≡y (mod 4ck)` at a perturbed q
  needs `T>v_q(4ck)`, and `ck≤X` ⇒ `4ck | 4·X!` ⇒ `v_q(4ck)≤v_q(4X!)<T` ✓.
  Valuation comparison in all three cases ✓; `(d,4ck)=1` from `d≡−y` ✓.
* Step 4: integrality (`E_q>n_{c,k,q}` ⇒ `f|Q`; `f | a²+4ck²` since
  `a∈𝒞`) ✓; values at q≤B are q-units: `N(Qt+a)≡N(a) (mod q^{E_q})` and
  `v_q(N(a))=n<E_q` ✓; q>B: degree `1+2m'<q` where m' = #distinct V ≤ m ✓,
  leading coefficient `Q·∏Q²/f_V` prime to q ✓. Distinctness: same V ⇒ same
  polynomial; different V ⇒ different leading coeff or constant ✓.
* Step 5: `N=f·R`, R prime > B ≥ X, so R coprime to f and to 4ck; also
  `R≠p` since `p∤4ck²`. Target divisors are `d`, `dR` ✓. The cofactor
  computation `dR≡−p ⟺ e≡−p (mod 4ck)` (using `N≡p² (mod 4ck)`) ✓.
* (iii): `X_r` finite ⇒ apply (ii) with `X=X_r−1` ⇒ limsup ≥ X_r ✓.
  Sterile point from `X_r=∞`: nested nonempty closed sets
  `Σ_r∖⋃_{K_X}Cl` in compact `Σ_r`, finite intersection property ✓ (the
  one-line proof "Cl open, Σ_r compact" is terse but correct).

## Defects

**D1 (MINOR) — Thm A(i), §0 definition of Σ_r.** `Σ_r⊂Ẑ^×` is defined as a
set of *unit* points, but a prime p is not a unit in `ℤ_p`, so "p∈Σ_r" (§0,
Step 5) is literally false. Harmless for (ii) (only q≤B matter), but it
matters for (i): a finite covering of `Σ_r` (units) is a covering mod
`M=lcm(4ckF)`; a prime p with `p|M` (i.e. `p|F` for some F in the covering)
reduces to a non-unit residue and is not guaranteed to be covered — and
indeed `p∉Cl(c,k,F)` whenever `p|F` (would need `p|4ck²`). So "for every
hard p with `n_p=r` and `p>2X_r`" is not proved; it holds for
`p>max(2X_r, max F over the covering)`. *Repair:* state (i) with that
threshold (or "for all but finitely many p"); `C*(r)≤X_r` (a limsup) is
unaffected. Also say "p∈Σ_r" means `p mod M ∈ Σ_r mod M` for the relevant
moduli / define membership via the components at q≤r.

### (2.2) derivation, Lemma 2.1, Lemma 3.1, Prop 4.1

* (2.2) from `Cl`: at odd `q∉{7}` with `x_q=1`: `F≡−1 (q^{v_q(4ck)})`; at 7,
  `x_7=−1`: `F≡+1 (7^{v_7(ck)})`; at 2: `F≡−w`; `x²≡−4ck² (F)` with `x_q²=1`
  at all `q|F` (F odd, prime to 7) ⟺ `F|1+4ck²` ✓.
* Lemma 2.1 at `x̂_w`: for `x≡1 (8)`, `χ_s(x)=∏_{q|s odd}(x/q)` by
  reciprocity ⇒ `χ_s(x̂)=(−1)^{[7|s]}` ✓; Dirichlet + Thm 48.1 argument needs
  p large so that `(c,k)∈𝓑_p` (Dirichlet gives infinitely many) ✓. So Step 1
  of Thm A at `x̂_9` only needs slices with `v_7(c)` odd ✓, and these
  automatically have `s∉{1,2,3,6}` ✓.
* Lemma 3.1, re-derived: all primes of `c'k'` divide `F+1` (as `m'|F+1`),
  `7^{a+2b}|F−1` (7∤F+1) ⇒ `F+1=2^i c'k'²`, `F−1=2^j7^s`, `i+j=2+α+2γ`,
  `min(i,j)=1` ✓. `j=1`: `v_2(1+7^s)=3` (s odd) ⇒ `α+2γ=3` ⇒
  `(α,γ)∈{(3,0),(1,1)}`, modulus ≥16, `−F≡1 (16)` ✓. `i=j=1` ⇒ `α=γ=0`,
  parity contradiction ✓. `i=1,j≥2`: `γ≥1` ⇒ `F≡1 (2^{2+α+γ})` ⇒ `w≡−1 (8)` ✗ ✓;
  `γ=0`: `−F≡−1+2^{1+α} (2^{2+α})`, ≡3 or 7 (8) ✓. Modulus is ≥8 in every
  branch ✓. **SOUND.**
* Prop 4.1(ii) for `r≡15 (16)`: `v_2(1+r^s)≥4` (not =3), so the `j=1`
  branch gives `α+2γ=v_2(1+r^s)≥3`, still `α+γ≥2`, modulus ≥16, and
  `−1−2r^s≡1 (16)` ✓. The author's "used only `v_2≥3`" is accurate. **SOUND.**
* Prop 4.1(i): `1+4ck²=1+4r(r+1)=(2r+1)²`, `v_2(4ck)=3`, `(F,4ck)=1`
  (`gcd(2r+1,r)=gcd(2r+1,r+1)=1`), `F≡−1 ((r+1)/4)`, `F≡1 (r)`,
  `−F≡1 (8)` ✓; checked numerically below. **SOUND.**

### Computation 3.2: completeness of the checker and independent re-run

*Completeness, re-derived.* At `x̂_w` a certificate on slice (c,k) is a
divisor `F|N=1+4ck²` with `F≡ξ:=−x̂ (mod h)`, `h=4ck` (this already forces
`(F,h)=1`). Since `N≡1 (mod h)` the cofactor `e=N/F≡ξ^{−1}`. One of `F,e` is
`≤√N`, and `√N=√(1+4ck²)<4ck=h` for all `c,k≥1`, so the smaller divisor is
*the least positive residue* of `ξ` resp. `ξ^{−1}` mod h. Hence exactly two
candidates per slice; the test is exact and complete ✓. (The author's "about
`√N/4ck<1` per class" is the same fact.) Slices with `v_7(c)` even are
excluded by Lemma 2.1 ✓ (my definition engine confirms numerically: no
forced-slice certificate at `x̂_w` up to ck≤2·10⁴, even including
`s∈{1,2,3,6}`).

*From-scratch engines.*
* `scripts/review_ti2_check.c` — same two-candidate principle (it is the only
  sensible complete method), but independent code: `x̂ mod h` built by
  explicit CRT with extended Euclid, `w^{−1} mod 2^t` by egcd, 128-bit.
* `scripts/review_ti2_defn.py` — independent algorithm, straight from the
  definition: factor N (sympy), every divisor F with `(F,4ck)=1`, `x̂ mod 4ckF`
  by CRT, test `x≡−F (4ck)` and `x²≡−4ck² (F)`, over **all** slices.

*Cross-validation.* For r=7 and `w∈{57,−23,197529,1,17,33,−7}`, X=2·10⁴,
the two engines output identical certificate lists (0,0,0,2,10,2,0
certificates). r=11, 19 at X=3000: identical lists, `(33,2,23)`,
`(132,1,23)`, `(22,12,23)` resp. `(95,2,39)`, `(380,1,39)`, `(38,20,1559)` —
the minimal ones match the author's sanity values; `w=1`: `(14,2,15)` ✓.

*Results (my C engine, ≤1 core, ulimit -v 8 GB).*

| r | w | X | slices (mine) | slices (author) | certs |
|---|---|---|---|---|---|
| 7 | 9 | 10⁶ | 1 533 438 | 1 533 438 | 0 |
| 7 | 9, −7, 25, 41 | 10⁷ | 18 212 347 | — | 0 |
| 7 | 9 | 10⁸ | 210 905 636 | 210 905 636 | 0 (30 s) |
| 23 | 9 | 10⁹ | 744 701 974 | 744 701 974 | 0 |
| 31 | 9 | 10⁹ | 548 469 498 | 548 469 498 | 0 |
| 47 | 9 | 10⁹ | 356 411 660 | 356 411 660 | 0 |
| 7 | 9 | 3·10⁹ | (running) | 7 602 614 538 | |
| 7 | 9 (defn engine) | 2·10⁴ | 201 177 (all slices) | — | 0 |
