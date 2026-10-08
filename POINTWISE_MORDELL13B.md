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
(i) If `g≡−1 (mod 4m')` for an integer m' and q∤g, then `(m'/g)=1` (Jacobi; odd p∣m': `(p/g)=(g/p)(−1)^{(p−1)/2}=1`;
if `2∣m'`, `g≡7 (8)`). (ii) If moreover `g≡−2` or `g≡−1/2 (mod q)`, q∈T, then
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
