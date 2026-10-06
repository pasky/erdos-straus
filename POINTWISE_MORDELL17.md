# POINTWISE_MORDELL17 — sterility at r = 17 (task O83)

Status: work in progress (side agent O83, branch `side-agent/sterility-r17`). Builds on
POINTWISE_MORDELL.md (§2.1, §5; unreviewed author branch `side-agent/mordell-13`).
Labels as in DISCOVERIES.md.

Notation. T = {17}. A point `x∈Ẑ^×` is *17-generic* if `x_q = 1` for all q ≠ 17; write
`x = x(u)`, `u = x_17 ∈ ℤ_17^×`. Cell `C_v = {u ≡ v (mod 17)}`, v ∈ {5, 7} (non-residues,
5·7 ≡ 1). A class of modulus `M = 17^k·N` (17 ∤ N) contains `x(u)` iff its residue `r` satisfies
`r ≡ 1 (mod N)` and `u ≡ r (mod 17^k)`; then it contributes the *box* `r + 17^k ℤ_17` of
*level* `k`, `F = 17^k`. Haar measure on ℤ_17, `μ(C_v) = 1/17`.

## 1. The seven families collapse to four box types (PROVED, elementary)

From the T-generic conditions of POINTWISE_MORDELL §2.1 (which are just the ET coordinate
integrality conditions at `n=1` away from 17 and at `n=u` at 17). Throughout, all parameters are
positive integers, `F=17^k`, `'` = 17-free part, `g = f'`.

**Lemma 1.1.** At level `F = 17^k`, the boxes of the seven ET families are exactly the boxes of:

* **(P)** `(a,d,f)`, `17∤f`, `f | 4a²d+1`, `4(ad)' | f+1`, `(ad)_17 = F`; box `−f (mod F)`.
  [= I1; = I3 with `17 | cd`; = II3 with `17 | ad`.]
* **(Q)** `(a,d,f)`, `f = Fg`, `17∤g`, `4ad | f+1`, `g | 4a²d+1`; box `−4a²d (mod F)`.
  [= II2; = II3 with `17 | e`.]
* **(Q⁻¹)** box `−1/(4a²d)` for each (Q)-datum. [= I2 with `17 | f`.]
* **(√Q)** boxes `±√(−4a²d) (mod F)` for each (Q)-datum. [= I3 with `17 | f`.] *(Empty: Lemma 1.3.)*
* **(U)** `(a,b,e)`, `e | a+b`, `gcd(e,4ab)=1`, `4(ab)' | e+1`, `(ab)_17 = F`; box `−e (mod F)`.
  [= II1; = I2 with `17 | ac`.]
* **(U⁻¹)** box `−1/e` for each (U)-datum. [= I4.]

Moreover (P) is closed under `r ↦ 1/r` (so (P)∪(Q)∪(Q⁻¹)∪(U)∪(U⁻¹) is inversion-symmetric,
and `u ↦ 1/u` maps `C_5 ↔ C_7`).

**Lemma 1.3 (√Q is empty; Q only at odd levels in non-residue cells; PROVED — observation of the
reviewer R83, `reviews/pointwise-mordell17-review.md` Claim A) (R83 repair).** For a (Q)-datum,
`f = 4adm−1 = 17^k g` with `m=(f+1)/(4ad)`. Since `f ≡ −1 (mod 4d)`, Jacobi reciprocity gives
`(d/f) = 1` (odd part `d_o`: `(d_o/f) = (f/d_o)(−1)^{(d_o−1)/2} = (−1/d_o)(−1)^{(d_o−1)/2} = 1`; 2-part:
`f ≡ 7 (mod 8)` when d is even), and `(−1/f) = −1`, so `(−d/f) = −1`. As `g | 4a²d+1`,
`−d·(2a)² ≡ 1 (mod g)`, so `(−d/g) = 1`. Hence `(−d/17)^k = −1`: **k is odd and `−4a²d` is a
non-residue mod 17**. So `n² ≡ −4a²d (mod 17^k)` has no root, the (√Q) type (I3 with `17|f`) never
meets the 17-generic line, and the symmetry `C_5 ↔ C_7` is exact. The same argument applied to a
(P)-datum (`f = 4ni−1 | 4·17^K a'²d'+1`, `f ≡ −1 (mod 4d')`) gives `(17^K/f) = −1`, i.e. **K is odd**.
Numerically: 0 √Q boxes at all levels ≤ 7 (both engines).

*Proof.* Read off the table of POINTWISE_MORDELL §2.1 with T={17}, splitting each family by which
of its moduli carries the 17 (the gcd conditions of I2, I3, II3 forbid both):
I3 with `17∤f`: conditions `f | 4c²d+1`, `4(cd)'|f+1`, box `−f` mod `(cd)_17` — literally (P).
II3 with `17∤e`: `e | 4a²d+1`, `4(ad)'|e+1`, box `−4a²d−e ≡ −e` mod `(ad)_17` (as
`v_17(a²d) ≥ v_17(ad)`) — (P). II3 with `17 | e`: then `17∤ad`, `4ad | e+1`, `e' | 4a²d+1`, box
`−4a²d−e ≡ −4a²d` mod `e_17` — (Q). I2 with `17∤f`: `f | a+c`, `4(ac)'|f+1`, box `−f` mod
`(ac)_17`, `gcd(f,4ac)=1` — (U). I2 with `17 | f = Fg`: `4ac | Fg+1`, `g | a+c`, box `−c/a` mod F.
Put `t = (Fg+1)/(4ac)`; then `4at | Fg+1` and, as `g | a+c` and `g | 4ac·t−1 = 4at(a+c) − 4a²t − 1`,
`g | 4a²t+1`; so `(a,t,Fg)` is a (Q)-datum, and `c ≡ 1/(4at)` gives box `−c/a ≡ −1/(4a²t)`. Conversely
a (Q)-datum `(a,d,Fg)` gives the I2 class `(a, c=(Fg+1)/(4ad), Fg)` (`g | a+c` since
`m(4a²d+1) ≡ a+m (mod g)` for `m=c`, `4adc ≡ 1`). I3 with `17 | f`: `4cd | f+1`, `f' | 4c²d+1`
(the (Q) conditions with `a=c`), boxes the roots of `n² ≡ −4c²d` mod `f_17`.
(P) closed under inversion: `f* = (4a²d+1)/f` satisfies `f f* ≡ 1 (mod F)` and `f* ≡ −1 (mod 4(ad)')`,
so `(a,d,f*)` is a (P)-datum with box `−f* ≡ −f^{−1} = (−f)^{−1} (mod F)`. ∎

**Lemma 1.2 (no level-0 boxes).** No class of any family contains all 17-generic points
(i.e. there is no box with `F=1`). *Proof:* see §2 (rigid forms with F=1 have no solutions).

## 2. Box types = Erdős–Straus solutions of 4/17^K (PROVED, elementary)

ET notation (arXiv:1107.1010 §2): `Σ^I_n`: `4abcd = n(a+b)+c`, `e=(a+b)/c`, `f=4acd−n`,
`ef=4a²d+1`; `Σ^II_n`: `4abcd = a+b+nc`, `e=(a+b)/c`, `f=4acd−1`, `ef=n+4a²d`,
`4c²dn+1=f(4bcd−1)`. `π^I=(abdn,acd,bcd)`, `π^II=(abd,acdn,bcdn)` map N-points to ordered
solutions of `4/n=1/x+1/y+1/z`, injectively modulo the dilation `(λa,λb,λc,λ^{−2}d)`.

**Lemma 2.1 (Q ↔ Type I points of 4/17^k).** `(a,d,f=Fg)` is a (Q)-datum of level `F=17^k` iff
`(a,b,c,d) = (a, (f+1)/(4ad), (a+b)/g, d)` is an N-point of `Σ^I_F` with `e=g` prime to 17. The box
`−4a²d (mod F)` is dilation invariant, so **#(Q)-boxes of level k ≤ #ordered solutions of
4/17^k** (and the same for Q⁻¹; √Q is empty by Lemma 1.3).
*Proof.* Put `m=(f+1)/(4ad)`. `gcd(m,g)=1` and `m(4a²d+1) ≡ a+m (mod g)` give `g | a+m`; with
`j=(a+m)/g`: `jf = F(a+m)`, i.e. `4amjd = Fa+Fm+j`, which is (2.3) for `(a,m,j,d)`, `n=F`; then
`e=(a+m)/j=g` and `f_ET = 4ajd−F = (Fa+j)/m > 0`. Conversely (2.3) gives `j(4amd−1)=F(a+m)=Fje`,
so `4amd−1 = Fe`, and `e | 4a²d+1` is (2.7). ∎

**Lemma 2.2 (U ↔ solutions of 4/17^k).** For a (U)-datum `(a,b,e)` of level `F` put `c=(a+b)/e`,
`i=(e+1)/(4ab/F)`. Then `4/F = 1/(iab) + 1/(iac) + 1/(ibc)`, and the box is
`−e = −(x/y + x/z)` for `(x,y,z) = (iab,iac,ibc)`. Hence **#(U)-boxes of level k ≤ #ordered
solutions of 4/17^k** (same for U⁻¹).
*Proof.* `e+1 = 4i·ab/F` and `a+b = ce` give `4iabc = F(a+b+c)`; divide by `F·iabc`. And
`x/y + x/z = b/c + a/c = e`. ∎

**Lemma 2.3 (P ↔ Type II points of 4/17^K, at half level).** Let `(a,d,f)` be a (P)-datum of level
`k`, `a=17^α a'`, `d=17^δ d'` (`α+δ=k`), `n=a'd'`, `f=4ni−1`, `f*=(4a²d+1)/f=4nj−1`. Then
`(i, j, a', d')` is an N-point of `Σ^II_N`, `N=17^K`, `K=k+α ∈ [k,2k]`, with `17∤a'd'`, and the box is
`−f = −f_ET (mod 17^k)`. Conversely every N-point of `Σ^II_{17^K}` with `17∤cd` and every
`0≤α≤K/2` gives a (P)-datum of level `K−α` with box `−f_ET mod 17^{K−α}`. These boxes are nested;
**the union of all (P)-boxes is the union over K≥1 and over N-points of Σ^II_{17^K} (17∤cd) of the
boxes `−f_ET (mod 17^{⌈K/2⌉})`.**
*Proof.* `(4ni−1)(4nj−1)=4aFn+1` expands to `4nij−i−j=aF=17^K a'`, i.e. `4·i·j·a'·d' = i+j+17^K a'`
— (2.15). Conversely (2.21) `4c²dN+1 = f(4bcd−1)` with `a=17^α c`, `d_P=17^{K−2α}d` gives
`f | 4a²d_P+1`, and `f+1 = 4acd ≡ 0 (mod 4cd)`. ∎

**Corollary 2.4 (no level-0 boxes; Lemma 1.2).** `F=1` would give ES solutions of `4/1` in
positive integers, impossible (`1/x+1/y+1/z ≤ 3`). For (P), `K≥1` as `k≥1`... and `k=0` forces `K=0`. ∎

**Consequence (measure).** With `f(N)` = #ordered positive solutions of `4/N=1/x+1/y+1/z` and
`f_II(N)` = #N-points of `Σ^II_N` modulo dilation,
`μ(⋃ boxes) ≤ Σ_{k≥1} 6 f(17^k) 17^{−k} + Σ_{K≥1} f_II(17^K) 17^{−⌈K/2⌉}`.
Both series CONVERGE (PROVED, but with non-explicit constants) (R83 repair m1): ET Prop 1.7 *as
stated* bounds Type I/II solutions (coprimality included), not all N-points nor `f(17^k)`. However, the
*proof* of Prop 1.7 (ET §3) counts N-points of `Σ^I_n` resp. `Σ^II_n` obeying Lemma 2.8, whose proof uses
only the defining equations; this gives `D_Q(k) ≪ 17^{(3/5+o(1))k}` and `D_P(K) ≪ 17^{(2/5+o(1))K}`. For
(U), whose data are general ordered solutions of `4/17^k` (Lemma 2.2), use Browning–Elsholtz (ET ref. [8]):
`f(n) ≪_ε n^{2/3+ε}` for all n (alternatively Lemma 5.2 below: U adds nothing new). The bounds are
effective in principle but the constants are not explicit, and any explicit version (via Nicolas–Robin)
is far too weak at computable levels (§4). The (P) series is the critical
one: exponent `2/5` against measure `N^{−1/2}`.

## 3. Exact low levels (CERTIFIED by one engine; independent re-check pending)

`scripts/m17_enum.c` enumerates, using the bounds of ET Lemma 2.8 (valid for every N-point, not
only Type I/II solutions, as its proof uses only the defining equations):
* `Q k`: N-points of `Σ^I_{17^k}` with `a≤b` (`n/4<acd≤3n/4`, `f=4acd−n | 4a²d+1`), `17∤e`;
  boxes `−4a²d`, `−4b²d` (the reflection `a↔b`);
* `U k`: `4i·uvw = F(u+v+w)`, `u≤v≤w` (`4iuv ≤ 3F`), every choice of `c∈{u,v,w}`, conditions of (U);
* `P K`: N-points of `Σ^II_{17^K}` with `a≤b` (`a²d ≤ abd ≤ N/2`), `f·e = N+4a²d`, `f≡−1`,
  `e≡−N (mod 4ad)`, `17∤cd`; boxes `−f`, `−f* = −(4bcd−1)` mod `17^{⌈K/2⌉}` (reflection).
`scripts/m17_union.py` adds Q⁻¹, √Q, U⁻¹ (Lemma 1.1) and computes the union in `C_5`, `C_7`
exactly (ultrametric: two boxes are nested or disjoint, so the union measure is the sum over
maximal boxes).

Validation (soundness): `scripts/m17_validate.py` rebuilds, from independent Python enumerations of
the same data (Q, U: k=1,3; P: K=1,3,5), the genuine ET classes (II2 for Q, I1 for P at every
`α≤K/2`, II1/I4 for U), and checks with `mordell_lib` that each contains the 17-generic points of
the claimed box and that `solve()` returns a valid ES solution at a prime >10⁶ in it: 1152 classes OK.
Validation (completeness): every box of the brute-force run `mordell_tgen.py 100000 17 3 17` (all seven
families, all moduli `M≤10⁵`, 106 boxes) meeting `C_5∪C_7` is in the complete list; the 13 rigid
II-boxes of POINTWISE_MORDELL §5 (cell 5, level 3) are in it. (Brute force leaves 76.1% of each cell
uncovered at level ≤3; the complete enumeration 68.5%: the extra boxes have T-free part >10⁵/17³.)

Number of data (`m17_enum` stderr): Q: 2, 0, 73, 0, 245, 0, 707 (k=1..7); U: 4, 0, 68, 0, 310, 0,
826; P: 2, 0, 32, 0, 121, 0, 258, ·, 604 (K=1..9; P 9 took ≈8 min). Even K are empty: for Q and P this is PROVED by Lemma 1.3 (direct reciprocity) (R83 repair m2:
ET Prop 1.6's *statement* concerns Type I/II solutions, while our N-points may have `17|c` (Q) or `17|ij`
(P); ET's proof in §4 uses only (2.1), (2.2), (2.13), (2.14) and would also apply). For U, even levels are
only computed empty (k=2,4,6; reproduced by R83). That is harmless, since `B_k` keeps `D_U(k)` for all k
(see also Lemma 5.2: in-cell U-data need `α−β` odd, hence k odd).

**Computation 3.1.** Covered fraction of `C_5` (identical numbers for `C_7`):

| level k | boxes meeting C_5 (by type) | maximal | covered fraction after level k |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 2 | 4 (P, K=3) | 4 | 0.235294 |
| 3 | 32 (Q 12, Q⁻¹ 12, U 4, U⁻¹ 4, P 20) | 23 | 0.314879 |
| 4 | 50 (P, K=7) | 34 | **0.321799** (complete through level 4) |
| 5 | 158 (Q 39, Q⁻¹ 39, U 25, U⁻¹ 25, P 93 from K=9) | 83 | **0.322793** (complete through level 5) |
| 7 (Q,U only) | 240 | 94 | 0.322797 |

So the boxes of level ≤5 leave **67.72%** of each cell uncovered (CERTIFIED; level 6 has only P-boxes
from K=11, not computed), and the measure
added per level falls by roughly a factor 17–20 per level (EVIDENCE). The points `u=5`, `u=7`
(the `x̃` of POINTWISE_MORDELL Comp. 5.1) lie in no box of level ≤5, nor in any Q/U box of level 7.

## 4. The tail: reduction to explicit counts, and where it breaks

Write `D_Q(k)`, `D_U(k)`, `D_P(K)` for the numbers of data enumerated by `m17_enum` (Q: N-points of
`Σ^I_{17^k}` with `a≤b`, `17∤e`; U: (U)-data; P: N-points of `Σ^II_{17^K}`, `a≤b`, `17∤cd`). By
Lemma 1.1 and §2 the boxes of level k number at most `B_k = 4D_Q(k) + 2D_U(k) + 2D_P(2k−1) + 2D_P(2k)`
(Q: two orientations × {Q, Q⁻¹}, √Q being empty by Lemma 1.3; P: two orientations), and `D_P(2k) = 0`
(Lemma 1.3) (R83 repair: previously `8D_Q`, an over-count).

**Theorem 4.1 (measure criterion; PROVED).** If
`Σ_{k≥6} 17^{1−k}·B_k < 0.677207` (the uncovered fraction of `C_5` after level 5, Comp. 3.1),
then `C_5` contains a sterile point `u`: `x(u)` lies in no class of any of the seven ET families.
The same holds for `C_7`.
*Proof.* Boxes of level ≥6 have total measure `≤ Σ_{k≥6} B_k 17^{−k}`, which is less than the measure
`0.677207/17` of the part of `C_5` missed by levels ≤5. ∎

**Corollary 4.2 (what sterility gives; PROVED from a sterile point).** If `u∈C_5` is sterile, then
no finite set of ET Prop 1.9 classes (equivalently, by ET Prop 1.9, no finite set of the polynomial
ES identities of these seven families) covers all sufficiently large primes `p` with `(p/17)=−1`
and `(p/q)=+1` for every prime `5≤q<17` (Mordell-hard primes with `n_p=17`): the finite union misses
a neighbourhood of `x(u)`, i.e. a class `x ≡ u (mod 17^L)`, `x ≡ 1 (mod Q)` with `17∤Q`, which
contains infinitely many primes (Dirichlet), all with `x_17 ≡ 5`, i.e. `(p/17)=−1`, and squares at
every other prime ≤ 13 (as `x_q=1`).

**Conjecture 4.3.** `C_5` (equivalently `C_7`, by inversion) contains a sterile point. EVIDENCE:
67.72% of each cell lies in no box of level ≤5 (Comp. 3.1), and the measure added per level decays
geometrically. By Theorem 4.1 (a PROVED reduction) and Corollary 4.2, the conjecture follows from an
explicit tail bound (§6). It would imply that no finite set of polynomial ES identities covers the
Mordell-hard primes with `n_p=17`.

**Status of the hypothesis of Theorem 4.1.**
* *Non-explicit convergence (PROVED; R83 repair m1).* By §2 (proof of ET Prop 1.7 for N-points;
  Browning–Elsholtz for U), `D_Q ≪ 17^{(3/5+o(1))k}`, `D_U ≪ 17^{(2/3+ε)k}` and
  `D_P(K) ≪ 17^{(2/5+o(1))K}`, so `Σ_k 17^{−k}B_k < ∞`; the tail beyond level `k₀` tends to 0.
  The ET constants (`n^{O(1/log log n)}` from the divisor bound) are not explicit, so this does
  not give a `k₀` that the computation reaches.
* *The critical family is (P)* (= I1, I3 with `17|cd`, II3 with `17|ad`, i.e. the 17 sits in the
  quadratic-form modulus `4ad`). Its boxes have half level `⌈K/2⌉` relative to the ES level `K`,
  so the measure weight is `N^{−1/2}` against ET's `f_II(N) ≪ N^{2/5+o(1)}`: margin only `1/10`.
  Even granting `D_P(K) ≤ 17^{2K/5}` with constant 1, `Σ_{K≥11 odd} 2·17^{2K/5}·17^{1−(K+1)/2} ≈ 0.84`
  exceeds 0.677; one would need exact enumeration through K=11 *and* an explicit ET-quality bound.
  Q and U have margin `2/5` (exponent 3/5 against `N^{−1}`) and are harmless given any explicit
  bound `D ≤ C·N^{0.9}` with moderate C.
* *Why elementary effective bounds fail.* Counting `D_P(K)` amounts to counting `(a,b)` with
  `r=(−17^K mod 4ab) | a+b` (ET Prop 2.7, second form; `d` is then unique since
  `0 < 4abd−N ≤ a+b`), or divisors of `4c²dN+1` in the class `−1 mod 4cd`. Lenstra's bound
  (≤11 divisors in a class mod `s ≥ m^{1/3}`) applies only when `16cd² ≳ N`, and the number of
  pairs is `≍ N log N`; pointwise divisor bounds are `m^{0.2+}` at the relevant sizes. Any route
  needs a genuinely new explicit count of ES solutions at prime powers.
* *Empirics (EVIDENCE).* `D_P = 2, 32, 121, 258, 604` (K=1,…,9 odd), `D_Q = 2,73,245,707`, `D_U = 4,68,310,826`
  (k=1,3,5,7): polylogarithmic-looking growth, far below what Theorem 4.1 needs (it suffices, e.g.,
  that `D_Q+D_U ≤ 17^{k/2}` for `k≥8` and `D_P(K) ≤ 17^{K/4}` for `K≥11`: then the tail is `< 0.01`).

**Assessment.** A sterile point in `C_5` is extremely likely (67.7% of the cell survives all
boxes of level ≤ 5 and the measure added per level decays geometrically in the data), but a
proof needs an explicit bound on the number of ES solutions of `4/17^K` of exactly the strength
that is open in general. Theorem 4.1 is the precise reduction.

## Replay

```
gcc -O2 -o /tmp/o83/m17_enum scripts/m17_enum.c
for a in "Q 5" "U 5" "P 7" "Q 7" "U 7" "P 9"; do /tmp/o83/m17_enum $a | sort -u > /tmp/o83/out_${a/ /}.txt; done  # P 9 ≈ 8 min, rest < 2 min
PYTHONPATH=scripts uv run python scripts/m17_union.py 7 9        # Comp. 3.1 (small k computed on the fly)
PYTHONPATH=scripts uv run python scripts/mordell_tgen.py 100000 17 3 17   # brute-force cross-check (§3)
PYTHONPATH=scripts uv run python scripts/m17_validate.py         # soundness, ~1 min
PYTHONPATH=scripts uv run python scripts/m17_union.py 3 6 --cmp /tmp/o80_boxes_100000_17_3.pkl
```

## 5. Tail attempts I: nesting and centres (task O83, round 2)

**Lemma 5.1 (rational centres; PROVED).** (i) For an N-point `(a,b,c,d)` of `Σ^I_n`, `n=17^k`, with
`17∤bc`, the (Q)-box is `−4a²d ≡ −a/b (mod 17^k)`. (ii) For an N-point of `Σ^II_N`, `N=17^K`, with
`17∤b`, the (P)-box is `−f ≡ −a/b (mod 17^K)`, a fortiori mod `17^{⌈K/2⌉}`.
*Proof.* (i) (2.3) `c(4abd−1) = n(a+b) ≡ 0`, so `4abd ≡ 1`, `4a²d ≡ a/b`. (ii) (2.20) `bf = Nc+a ≡ a`. ∎
For in-cell boxes the hypotheses hold: for Q, `17|c` forces box `≡1` (§2), and `17|b` gives
`17|c` by (2.3); for P, `17|b` with `17∤cd` forces `17|a` by (2.15), and then `f ≡ −1` and box `≡ 1`.
*Consequences.* The Q-boxes are closed under inversion (the reflection `a↔b` sends `−a/b` to
`−b/a`), so the types Q and Q⁻¹ give the **same** set of boxes (confirmed by the data). Both Q and P
boxes are balls around the rationals `−a/b` built from an ES point.

**Lemma 5.2 (U is never new; PROVED).** Every (U)-box meeting `C_5∪C_7` lies inside a (P)-box of
strictly lower level with the same centre. In particular (U)-boxes add no measure, and (U) is empty at
even levels.
*Proof.* Take a (U)-datum `(a,b,e)` with `a=17^α a'`, `b=17^β b'`, `α+β=k`, and WLOG `α≥β`. Put
`c=(a+b)/e` and `e+1=4i a'b'`. Then `4ia'b'c = a+b+c`.
If `17|i`, then `e≡−1` and the box is `≡1`, which is not in a cell; so `17∤i`.
*Case α>β.* `v_17(a+b)=β` and `17∤e`, so `c=17^β c'` with `17∤c'`. Dividing by `17^β` gives
`4ia'b'c' = 17^{α−β}a' + b' + c'`. This is (2.15) for `(A,B,C,D)=(b',c',a',i)` with `N'=17^{α−β}`, and
`17∤CD`, so it is a (P)-datum (Lemma 2.3). By Lemma 5.1(ii) its box is `−b'/c' (mod 17^{⌈(α−β)/2⌉})`.
On the other side, `e = (17^{α−β}a'+b')/c' ≡ b'/c' (mod 17^{α−β})`. So the U-box `−e (mod 17^k)` lies in
that P-box, whose level is `⌈(α−β)/2⌉ < k`. Moreover `α−β` must be odd (ET Prop 1.6: `f_II(17^{2j})=0`).
*Case α=β.* Then `ce = 17^α(a'+b')`. If `17^α ∤ c`, then `17 | e`, which is impossible. So `c=17^α c''` and
`4ia'b'c'' = a'+b'+c''`, i.e. `4i = Σ 1/(pairwise products) ≤ 3`, which is impossible. ∎

**Data (new = not inside a box of lower level).** New boxes meeting C_5, by level:
2: P 4; 3: Q 8 (=Q⁻¹), P 16; 4: P 34; 5: Q 29, P 54; 7: Q 94 (P not computed).
U: never new (Lemma 5.2). So new boxes are about half of all boxes. This is a constant factor,
not an exponent: nesting does not change the critical comparison (P: count `N^{2/5+o(1)}` vs weight
`N^{−1/2}`), because a centre is new at its *first* K, and first occurrences are not provably
rarer than occurrences.

## 6. Tail attempts II: prime-power structure, digit sets (EVIDENCE / precise obstruction)

*Reformulation of (P) (PROVED).* An N-point of `Σ^II_N` with `a≤b` is determined by `(a,b)`.
Indeed `ce=a+b` gives `0<e≤a+b<4ab`, and `N+e=4abd`, so `e` is the least positive residue of
`−N (mod 4ab)` and `d=(N+e)/(4ab)`. Hence
`D_P(K) ≤ #{(a,b): a≤b, 2ab ≤ 17^K, (−17^K mod 4ab) divides a+b}`, with box centre `−a/b` (Lemma 5.1).
For fixed `(a,b)` the admissible `K` are periodic mod `ord_{4ab}(17)`, and the boxes are nested
(Lemma 5.2's mechanism). So the (P)-union is `⋃_{(a,b)} B(−a/b, 17^{−⌈K₀(a,b)/2⌉})` together with its
reflection, where `K₀` is the first admissible K. Since `17^{K₀} ≥ 2ab`, the radius is `≤ (2ab)^{−1/2}`.

*Scaled vs primitive (PROVED, partial).* For a P-datum, `17|a ⟺ 17|b` (2.15). If `17|a,b`, then
`(a/17, b/17, c, 17d)` is an N-point for `17^{K−1}` with the same centre `−a/b`. That point is **not** a
P-datum (`17|d`), so scaling does not give nesting inside P. These boxes have centre `≡1 (17)`
anyway (`f≡−1`), so in-cell P-data are all primitive (`17∤ab`). For Q (Lemma 5.1) the in-cell data
satisfy `17∤abcd`. So **the prime-power structure enters only through the residues `17^K mod 4ab`.**

*What an explicit bound requires.* The weight of a level-K P-box is `≍ N^{−1/2}`, so one needs
`D_P(K) ≤ C·17^{θK}` with `θ<1/2` and explicit C. Here is what the available tools give:
* The elementary scan over `(a,d)` with `f|N+4a²d`, `f≡−1`, `e≡−N (mod 4ad)` gives `O(N)`: for
  `4ad>√(3N)` each pair still has one candidate `e=(−N mod 4ad)`, and nothing bounds how often it
  divides `N+4a²d`.
* Lenstra's bound (≤11 divisors in a class mod `s ≥ m^{1/3}`, valid for `ad ≥ N^{1/3}`) and
  Coppersmith–Howgrave-Graham–Nagaraj (for `ad ≥ N^{1/4+δ}`) bound the count *per pair* `(a,d)`
  by O(1). But there are `≍N` pairs with `a²d ≤ N/2`, so the result is again `O(N)`. What is
  missing is a bound on how many pairs have any admissible divisor at all.
* ET's `N^{2/5+o(1)}` uses the pointwise divisor bound. With Nicolas–Robin constants the exponent
  is `≥ 0.6` for every `K ≤ 40`.
So the P-tail is equivalent in difficulty to an explicit "small residues of `17^K` modulo `4ab`"
statement: `#{(a,b): ab≤17^K, (−17^K mod 4ab) | a+b} ≤ C·17^{(1/2−δ)K}`. Heuristically it is
`≈ Σ τ(a+b)/(4a·b)·b ≍ log³`. I see no unconditional route.

*Digit-set (Cantor) construction — tested, fails as stated (EVIDENCE).* If every box `r` of level k
had `r` or `1/r ≡ −z (mod 17^k)` with `0<z<θ·17^k`, a 17-adic `u` whose digits and those of `1/u`
avoid the top digits would be sterile. The digit-wise choice is possible because the new digit of
`1/u` is an affine function with slope `−u₀^{−2} ≡ 2` of the new digit of `u`. The integer centres
`−f` of P-boxes with `cd` small do satisfy this (`min(f,f*) ≤ √(4c²dN+1)`). But over all new
in-cell boxes the ratio `t = min(z_r, z_{1/r})/17^k` has median ≈0.15–0.2 and maximum 0.87–0.99
(levels 3–7). So no fixed θ works, and the boxes are only mildly biased toward small integer centres.

*Equivalent parametrisation and the discrete-log heuristic (Assessment).* Put `(s,t)=(c,d)`.
Then (2.20) says the P-data at level K are exactly the `(a,s,t)` with `f=4ast−1 | s·17^K+a` and
`b=(s17^K+a)/f ≥ a`. In that case `s | a+b` is automatic (`f≡−1 (mod s)`), and so is (2.15):
`4abst = bf+b = s17^K+a+b`. As `gcd(s,f)=1`, the condition is `17^K ≡ −a/s (mod f)`. So `(a,s,t)` is
ever admissible iff `−a/s ∈ ⟨17⟩ ⊂ (ℤ/f)^×`, and then exactly for `K ≡ log_17(−a/s) (mod ord_f 17)`
with `17^K ≳ 4a²t` (from `b≥a`). Under a random model for this discrete logarithm (17^K equidistributed
modulo f, for fixed K and f varying), `E[D_P(K)] ≈ Σ_{a,s,t} 1/(4ast) ≍ K³`. The weighted tail
`Σ_K 17^{−K/2} D_P(K)` is then tiny. The quantity to control is **how often `−a/s` lies in `⟨17⟩`
modulo `4ast−1`, and where its logarithm falls**. That is an Artin / discrete-log equidistribution
question for one fixed base, many moduli, and a fixed exponent K. Divisor-bound methods (ET,
Lenstra, CHN, Nicolas–Robin) treat `N` as an arbitrary integer and never see the special form
`N=17^K`. That is why they stop at `N^{2/5+o(1)}` ineffectively and at `O(N)` effectively, and why
no method of that kind can reach the `N^{1/2−δ}` that is needed.

**Assessment after round 2.** (a) Nesting: U contributes nothing (PROVED); Q⁻¹ = Q; the new-box
counts are about ½ of all boxes; the exponents are unchanged. (b) Prime-power structure:
in-cell data are primitive, and the P-count is a small-residue problem for `17^K mod 4ab`. No
explicit θ<1/2 bound is in reach. (c) Raising the exact cutoff would not close the tail by itself.
Theorem 4.1's hypothesis needs a per-K bound for all K, so more computation alone does not help.
P at K=11 would need an `N^{2/5}` factoring-based enumerator. Recommendation: record Theorem 4.1 as
the reduction, together with the CONJECTURE that `C_5` contains sterile points (EVIDENCE: 67.7%
uncovered through level 5, with rapidly decaying increments).
