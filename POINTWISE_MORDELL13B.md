# POINTWISE_MORDELL13B — the candidate sterile point x* (r = 13) as a Diophantine problem (task O95)

Status: work in progress (side agent O95, branch `side-agent/r13-diophantine`). Not reviewed.
Builds on POINTWISE_MORDELL.md (§2.1 table, Comp. 4.1, Conj. 4.2), POINTWISE_MORDELL17.md
(Lemmas 1.1–1.3, 2.1–2.3, 5.1), POINTWISE_TYPEI4.md. Labels as in DISCOVERIES.md.

Notation. `T={11,13}`. For an integer `u` prime to 143, `x(u)∈Ẑ^×` has `x(u)_q=u` for `q∈T` and
`x(u)_q=1` otherwise; **`x* = x(2)`**. For an integer m, `m_T` = its {11,13}-part, `m'=m/m_T`.
A class `n≡r (mod M)` contains `x(u)` iff `r≡1 (mod M')` and `r≡u (mod M_T)` (CRT; `M'` may be even).
*Key simplification:* since `x*_11=x*_13=2` is the same integer, every box condition at x* is a
single congruence modulo `F=M_T` (no CRT between 11 and 13 is needed).

## 1. The seven families at x(u): explicit Diophantine conditions (PROVED, elementary)

**Lemma 1.1.** With the ET Prop 1.9 parametrisations of `scripts/mordell_lib.py`
(`cls_modulus_residues`), the class of the family with parameters P contains `x(u)` iff
(family constraints in brackets):

| family | P | condition for x(u) ∈ class |
|---|---|---|
| I1 | (a,d,f) [f∣4a²d+1] | `f≡−1 (4(ad)')`, `f≡−u ((ad)_T)` |
| I2 | (a,c,f) [(4ac,f)=1] | `f≡−1 (4(ac)')`, `f≡−u ((ac)_T)`, `f'∣a+c`, `c≡−ua (f_T)` |
| I3 | (c,d,f) [(4cd,f)=1] | `f≡−1 (4(cd)')`, `f≡−u ((cd)_T)`, `f'∣4c²d+1`, `f_T∣u²+4c²d` |
| I4 | (a,b,e) [e∣a+b, (e,4ab)=1] | `e≡−1 (4(ab)')`, `ue≡−1 ((ab)_T)` |
| II1 | (a,b,e) [same] | `e≡−1 (4(ab)')`, `e≡−u ((ab)_T)` |
| II2 | (a,d,f) [4ad∣f+1] | `f'∣4a²d+1`, `f_T∣u+4a²d` |
| II3 | (a,d,e) [(4ad,e)=1] | `e≡−1 (4(ad)')`, `e≡−u ((ad)_T)`, `e'∣4a²d+1`, `e_T∣u+4a²d` |

At x* (u=2): II2 reads `f_T∣2a²d+1`; II3 `e_T∣2a²d+1`; I3 `f_T∣c²d+1`; I2 `c≡−2a (f_T)`;
I4 `2e≡−1 ((ab)_T)`.
*Proof.* Moduli/residues of `cls_modulus_residues`: I1 `−f mod 4ad`; II1 `−e mod 4ab`; I4 `−1/e mod 4ab`;
II2 `−4a²d mod f`; II3 `−4a²d−e mod 4ade`; I2 `≡−f (4ac)`, `≡−c/a (f)`; I3 `≡−f (4cd)`, `n²≡−4c²d (f)`
(all roots). Split each modulus into T-free and T-part and impose `r≡1` resp. `r≡u`; for II3 use
`(ad)_T∣a²d`, for I3 that a root `≡1 (f')`, `≡u (f_T)` exists iff `1≡−4c²d (f')` and `u²≡−4c²d (f_T)`. ∎
*Check:* `scripts/m13b_table_check.py` compares the table, generalised to an arbitrary off-T value w
(replace the T-free "1" by w), with literal class membership for 14000 random (family, P, u, w):
0 mismatches, 3605 memberships (seed 2).

This is the §2.1 table of POINTWISE_MORDELL evaluated at `u=2`; the point of the lemma is that at x*
every condition is a polynomial congruence with integer right-hand sides `−1`/`−2`.

**Lemma 1.2 (reciprocity at x*; PROVED).** Write `v_T(m)=v_11(m)+v_13(m)`. If x* lies in the class, then
* II1, I4 (P=(a,b,e)): `v_T(ab)` is odd; II2: `v_T(f)` odd; I2: `v_T(ac)+v_T(f)` odd
  (i.e. **the T-level `F=M_T` has odd total valuation** for these four families);
* I1: `v_T(d)` odd; I3: `v_T(d)` odd; II3: `v_T(d)+v_T(e)` odd.
*Proof.* Facts: `(2/11)=(2/13)=−1`, `(−1/11)=−1`, `(−1/13)=1`, so `(−2/11)=1`, `(−2/13)=−1`.
(i) If `g≡−1 (mod 4m')` for an integer m', then `(m'/g)=1` (Jacobi; odd p∣m': `(p/g)=(g/p)(−1)^{(p−1)/2}=1`;
if `2∣m'`, `g≡7 (8)`). (ii) If moreover `q∤g` and `g≡−2` or `g≡−1/2 (mod q)`, q∈T (R95 repair, applied by reviewer: the hypothesis `q∤g` moved here from (i)), then
`(q/g)=(g/q)(−1)^{(q−1)/2}=(−2/q)(−1)^{(q−1)/2}=−1` for both q=11, 13. Also `(−1/g)=−1`.
II1/I4: `e∣a+b`, `(e,ab)=1` give `(−ab/e)=(b²/e)=1`; by (i),(ii) `(−ab/e)=−(−1)^{v_T(ab)}`.
I1: `f∣4a²d+1` gives `(−d/f)=1`; by (i),(ii) (q∣d ⇒ q∣(ad)_T ⇒ `f≡−2 (q)`) `(−d/f)=−(−1)^{v_T(d)}`.
I3: `(−d/f')=1` from `f'∣4c²d+1`, and `(−d/q)=1` for q∣f_T from `f_T∣c²d+1`; so `(−d/f)=1`; the
right side is as for I1. II3: `(−d/e')=1`; for q∣e_T, `2a²d≡−1` gives `(−d/q)=(2/q)=−1`; so
`(−d/e)=(−1)^{v_T(e)}`, against `−(−1)^{v_T(d)}` from (i),(ii). II2: `f≡−1 (mod 4ad)` with full d, so
`(−d/f)=−1` (MORDELL17 Lemma 1.3), while `(−d/f')=1`, `(−d/q)=−1` for q∣f_T: `(−1)^{v_T(f)}=−1`.
I2: `f'∣a+c` gives `(−ac/f')=1`; for q∣f_T, `c≡−2a` gives `(−ac/q)=(2/q)=−1`; so `(−ac/f)=(−1)^{v_T(f)}`,
against `−(−1)^{v_T(ac)}` from (i),(ii) (`(4ac)`-coprimality makes q∣ac and q∣f exclusive). ∎
*Scope.* Reciprocity only gives these parities, all satisfiable; it kills e.g. every II1/II2/I4 class
of T-level 143, 11², 13², 11·13³ …, but no family entirely (no uniform quadratic obstruction).

## 2. Data at x* are ES solutions of 4/N, N a T-unit (in progress)

**Lemma 2.1 (II3, all placements of 11, 13; PROVED).** Let `(a,d,e)` be T-generic II3 data, i.e. `(4ad,e)=1` and the T-free conditions
`e≡−1 (4(ad)')`, `e'∣4a²d+1` of Lemma 1.1 hold (R95 repair, applied by reviewer: the proof uses only these, so
x(u) need not lie in the class).
Write `a=a_Ta'`, `d=d_Td'`, `λ=a_T²d_T`, `B=e_T`, `e=Bg`, `m=(e+1)/(4a'd')`. Then `j:=(λa'+m)/g` is a
positive integer, `4a'd'mj = Bλa'+Bm+j`, and
`4/(Bλ) = 1/(d'mj) + 1/(λa'd'j) + 1/(Bλa'd'm)` — an ES solution of `4/N`, `N=e_T·a_T²·d_T`.
*Proof.* `Bg=4a'd'm−1` gives `4a'd'm≡1 (g)`; `a²d=λa'²d'`, so `m(4a²d+1)≡λa'+m (g)`, and `g∣4a²d+1`
(Lemma 1.1) gives `g∣λa'+m`. Then `jBg=j(4a'd'm−1)=B(λa'+m)`; multiply the ES identity by `Bλa'd'mj`. ∎
Special cases: `B=1` is MORDELL17 Lemma 2.3 (P, "half level": `N=a_T²d_T` vs box level `(ad)_T`),
`λ=1` is Lemma 2.1 there (Q). In the mixed case (11 in ad, 13 in e) the ES level is `13^β·11^{2α_a+α_d}`.
Consequently, at each fixed T-level the II3 data containing x* are finitely many and are recovered from
the finitely many ES solutions of `4/N`, `N | F²`.
Remark: Lemma 2.1 uses only `e=4a'd'm−1=Bg` and `g∣4a²d+1`; hence it applies verbatim to **I3**
`(c,d,f)` (same shape, `B=f_T`) and to **I1** `(a,d,f)` (`f∣4a²d+1`, so one may take `B=1`, `g=f`; then `N=a_T²d_T`), giving
`4/N` with `N=f_T·a_T²·d_T` resp. `a_T²d_T` (I1) (MORDELL17 Lemma 2.3 is the case `B=1`).

**Lemma 2.2 (II1, I4; PROVED — MORDELL17 Lemma 2.2 verbatim).** For `(a,b,e)` with `e∣a+b`, `(e,4ab)=1`,
`e≡−1 (4(ab)')`, put `F=(ab)_T`, `c=(a+b)/e`, `i=(e+1)F/(4ab)`. Then `4/F=1/(iab)+1/(iac)+1/(ibc)`.

**Lemma 2.3 (II2; PROVED — MORDELL17 Lemma 2.1, any placement).** For `(a,d,f)` with `4ad∣f+1`, `f'∣4a²d+1`,
put `F=f_T`, `m=(f+1)/(4ad)`, `j=(a+m)/f'` (an integer). Then `4amjd=F(a+m)+j`, i.e.
`4/F=1/(amdF)+1/(ajd)+1/(mjd)`. (T-primes in `ad` are allowed; they impose no box condition.)

**Lemma 2.4 (I2, all placements; PROVED).** For `(a,c,f)`, `(4ac,f)=1`, `f≡−1 (4(ac)')`, `f'∣a+c`, put
`A=(ac)_T`, `B=f_T`, `t=(f+1)/(4(ac)')`, `h=(a+c)/f'`. Then `4/(AB)=1/(cth)+1/(ath)+1/(Bact)`.
*Proof.* `fh=Bf'h=B(a+c)` and `f=4(ac)'t−1` give `4(ac)'th=B(a+c)+h`; multiply by A (`A(ac)'=ac`) and
divide by `AB·acth`. ∎

**Corollary 2.5 (finiteness per ES level; PROVED).** Every T-generic datum of any family (only the T-free
conditions of Lemma 1.1 are used) yields an ordered ES solution of `4/N` for an explicit T-unit `N`
(its *ES level*: `(ab)_T`, `f_T`, `(ac)_T f_T`, or `B·a_T²d_T`), and the datum is recovered from the
solution by the inverse maps `XY/Z=t·A²`, … (`scripts/m13b_invert.py`). As `N ≥ F=M_T` and `N ≤ F²`,
each box level carries finitely many data, all found among the ES solutions of `4/N`, `F ≤ N ≤ F²`.
## 3. x* is NOT sterile: Conjecture 4.2 of POINTWISE_MORDELL is false (PROVED by explicit check)

**Theorem 3.1.** x* lies in the ET class
* II3 `(a,d,e)=(8,33,11999)`: modulus `M=4ade=12670944=2⁵·3·11·13²·71`, residue `r=12650497`
  (`= −4a²d−e mod M`), with `r≡1 (mod 6816=M')` and `r≡2 (mod 1859=11·13²)`;
* and also I2 `(a,c,f)=(125,88,11999)`: `M=527956000`, `M_T=1859`, residue `426568001`.
Hence every `n≡12650497 (mod 12670944)` satisfies ES with the II3 polynomial solution (positive for all n ≥ 1,
POINTWISE_MORDELL §0), e.g. the prime `p=12650497` (`p≡2 mod 11, mod 13`):
`4/p = 1/3165624 + 1/3339731208 + 1/5005839614391`.
*Proof.* Lemma 1.1 conditions for II3: `(4ad,e)=(1056,11999)=1`; `e+1=12000≡0 (mod 4(ad)'=4·8·3=96)`;
`(ad)_T=11` and `e+2=12001=11·1091`; `e'=71 | 4a²d+1=8449=71·119`; `e_T=169 | 2a²d+1=4225=25·169`. ∎
Checked: `mordell_lib.solve` gives exact positive integer solutions at 200 members of each class
(`/tmp/o95/verify_hit.py` and inline check, see Replay).
Data: ES level `N=e_T·a_T²·d_T=169·11=1859` (Lemma 2.1, mixed type: P at 11, Q at 13). Both classes
have modulus `>10⁶` and are outside the families of the rigid search (II1/II2/I4), so Comp. 4.1 is correct
as stated; only Conjecture 4.2 (and the evidence read into it) fails. Note both data share `f=e=11999`
(the I2/II3 coincidence is the Q⁻¹/Q pairing at 13 of MORDELL17 Lemma 1.1).
*Consequence.* A neighbourhood of x* is covered. The question "is Theorem 3.1(b) improvable to a finite
covering of `Σ_13` (main)?" is reopened; x* is no longer evidence against it.
*Independent check:* `scripts/m13b_check_hit.py` uses the stand-alone sympy engine of `mordell_check.py`
(ET coordinates rebuilt from the paper, not mordell_lib): polynomial identity holds, `x,y,z>0` for `n>1`,
and `x,y,z` are integer-valued on `t+Mℤ`, `t` = CRT lift of x* (`t≡1 (M')`, `t≡2 (M_T)`), for both classes. OK.

## 4. Complete enumeration by ES level (CERTIFIED, one engine + brute-force cross-check)

`scripts/m13b_es.c N` lists all `x≤y≤z` with `4/N=1/x+1/y+1/z` (divisor method; equal to an exact-fraction
brute force for N<90 and N=121,143,169,1331). `scripts/m13b_invert.py` applies the inverse maps of
Lemmas 2.1–2.4 to every permutation and unitary split, and tests each candidate exactly (T-free class
condition via `mordell_lib`, then `r≡2 (mod M_T)`). `scripts/m13b_run.sh 40000000` covers all 32
T-units `1<N≤4·10⁷`.
* *Completeness cross-check:* `scripts/m13b_validate.py`: of the 1306 brute-force T-generic boxes of
  POINTWISE_MORDELL §2 (`mordell_tgen.py 1000000 13 3 11,13`, all families, `M≤10⁶`), the 1157 whose
  witness has ES level `≤3·10⁶` all appear in the engine output (0 missing). (A first run had 374 missing
  P-type boxes due to an `a_T` loop bug; found by this check and fixed.)
* *x\*:* among all T-generic data of ES level `N≤4·10⁷` exactly two contain x\*: the II3 and I2 data of
  Theorem 3.1 (level 1859; the same parameter triples are re-found at `N=24167, 314171` because the inversion of
`m13b_invert.py` is non-canonical (its candidates are a superset of the canonical inverse images; no new
datum) — R95 repair, applied by reviewer). **No other datum through
  `4·10⁷`.**
* *Coverage of the cell `(x_11,x_13)≡(2,2) (mod 11,13)`* (`scripts/m13b_cell.py k`, boxes with
  `M_T∣11^k13^k` and ES level ≤ 4·10⁷; all other non-residue cells of `x_13` are fully covered at k=3,
  `scripts/m13b_cover.py`):

| k | uncovered subcells of the (2,2) cell | fraction | distinct `x_11 mod 11^k` × `x_13 mod 13^k` |
|---|---|---|---|
| 2 | 15 / 143 | 10.5% | 3 × 5 (exact product) |
| 3 | 970 / 20449 | 4.74% | 20 × 51 = 1020 |
| 4 | 135639 / 2924207 | 4.64% (incomplete: needs `N` up to `F²`) | 216 × 661 = 142776 |

  Before this work: 24.8% at k=4 (POINTWISE_MORDELL §4.1). So the (2,2) cell is still **not** covered.
  Sterile candidates, if any, are now off x*; at k=2 the survivors are
  `x_11 mod 121 ∈ {2,57,79}`, `x_13 mod 169 ∈ {15,28,54,132,145}` (EVIDENCE).

## Replay

```
gcc -O2 -o /tmp/o95/target scripts/m13b_target.c; gcc -O2 -o /tmp/o95/target2 scripts/m13b_target2.c
/tmp/o95/target $(python3 scripts/m13b_pt.py 2 15) 100000000 20      # Comp 5.1, ~25 min
/tmp/o95/target2 $(python3 scripts/m13b_pt.py 2 15) 20000000 12     # Comp 5.1, ~20 min
PYTHONPATH=scripts uv run python scripts/m13b_target_validate.py /tmp/o95/run /tmp/o95/target 2000000 20 60   # FAMS=II2 for II2
PYTHONPATH=scripts uv run python scripts/m13b_target2_validate.py /tmp/o95/run /tmp/o95/target2 300000 8 60
gcc -O2 -o /tmp/o95/es scripts/m13b_es.c
PYTHONPATH=scripts uv run python scripts/m13b_table_check.py 14000 2          # Lemma 1.1, ~10 min
PYTHONPATH=scripts uv run python scripts/m13b_check_hit.py                    # Thm 3.1 (independent sympy engine)
PYTHONPATH=scripts uv run python scripts/m13b_verify_hit.py                   # Thm 3.1 (mordell_lib, prime member)
scripts/m13b_run.sh 40000000 /tmp/o95/run                                     # §4, ~25 min, one core
PYTHONPATH=scripts uv run python scripts/m13b_validate.py /tmp/o80_boxes_1000000_11,13_3.pkl /tmp/o95/run 3000000
PYTHONPATH=scripts uv run python scripts/m13b_cover.py 3 /tmp/o95/run
for k in 2 3 4; do PYTHONPATH=scripts uv run python scripts/m13b_cell.py $k /tmp/o95/run; done
```

## 5. Targeted search at a given T-generic point, without a T-level cap (CERTIFIED within stated ranges)

For a point `x(u)` with `x_11=u_11`, `x_13=u_13` (any 11-, 13-adic units, given mod `q^16`), the classes
containing it are searched directly. The T-free part is enumerated and the T-part is solved as a
discrete logarithm in the T-units.
* `scripts/m13b_target.c` (P/Q types: II3, I3, I1, II2). Loop over `e=4a'd'm−1≤X`, with `a',d'` prime to 143
  and `B=e_T`, `g=e/B`. The T-free condition `g∣4λa'²d'+1` is equivalent to `λ≡−1/(4a'²d') (mod g)`, solved over
  `λ=a_T²d_T=11^i13^j`, `i,j≤E`. Every split `λ=a_T²d_T` is then tested against the box conditions of
  Lemma 1.1. II2 with T-primes in `ad` additionally needs `a_Td_T∣(e+1)/(4a'd')`. II2 with T-free `ad` is
  literally II3 with `(ad)_T=1`, so it is reported as II3.
* `scripts/m13b_target2.c` (U types II1, I4, and I2). Loop over `h=4xyt−1≤X`, with `x,y` prime to 143.
  `(first,second)=(R_n x,R_d y)` with `R_n/R_d=ρ=11^i13^j`, `|i|,|j|≤E`, `ρ≡−y/x` modulo `h` (U) resp. `h/h_T` (I2).
  A common T-factor s of the two parameters can be dropped: `gcd(s,h)=1`, so s does not affect the T-free
  conditions, and it only refines the box.
* *Validation against the complete engine of §4.* At box centres of random engine data:
  - II3/I3/I1: 60/60 recovered;
  - II2: 60/60, and the T-in-`ad` datum `(26,1,6655)` is recovered;
  - I2/II1/I4: 60/60.
  At x* both programs recover Theorem 3.1's II3 and I2 data (`e=f=11999`).

**Computation 5.1 (CERTIFIED, one engine per family group; validated as above).** Each of the four
small-height survivors of §4, `(u_11,u_13) = (2,15), (2,1/7), (2,−7/3), (−5/3,15)`, lies in no ET class
within the following ranges:
* II3/I3/I1 with `e≤10⁸` for the first two, `≤3·10⁷` for the last two;
* II2 with `f≤3·10⁷`;
* I2/II1/I4 with `f, e≤2·10⁷` for the first two, `≤10⁷` for the last two.

In all cases the T-exponents are `≤20` (P/Q) resp. `|i|,|j|≤12` (U/I2), and the height is otherwise
unrestricted. For comparison, x* is caught at `e=11999`.
*Consequence (PROVED from 5.1, as POINTWISE_MORDELL §4).* Every finite ET covering of the Mordell-hard primes
with `(p/11)=(p/13)=−1` contains a class outside these ranges. Indeed the point `x**=x(2,15)` lies in
`Σ_13` (main) (`x**_q=1` for q∉T), and Dirichlet applies near it.

**Conjecture 5.2.** `x**` (`x_11=2`, `x_13=15`, `x_q=1` otherwise) is sterile.
*Assessment.* The status of x* shows that such conjectures can fail at moderate height (`e≈1.2·10⁴`,
modulus `1.3·10⁷`). Here, however, the search goes 4 orders of magnitude further in `e` with no T-level
cap. The (2,2)-cell survivors also form a near-product set (§4). Both facts favour a genuinely uncovered
region, but this is EVIDENCE, not proof. A proof would need a tail bound of MORDELL17 Theorem 4.1 type,
and that is out of reach (MORDELL17 §6). The finite-exception theorem 3.1(b) is therefore **not** improved
here: its exceptions contain survivor points of the targeted searches.
