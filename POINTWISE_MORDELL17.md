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
* **(√Q)** boxes `±√(−4a²d) (mod F)` for each (Q)-datum. [= I3 with `17 | f`.]
* **(U)** `(a,b,e)`, `e | a+b`, `gcd(e,4ab)=1`, `4(ab)' | e+1`, `(ab)_17 = F`; box `−e (mod F)`.
  [= II1; = I2 with `17 | ac`.]
* **(U⁻¹)** box `−1/e` for each (U)-datum. [= I4.]

Moreover (P) is closed under `r ↦ 1/r` (so (P)∪(Q)∪(Q⁻¹)∪(U)∪(U⁻¹) is inversion-symmetric,
and `u ↦ 1/u` maps `C_5 ↔ C_7`; only (√Q) may break the symmetry).

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
so `(a,d,f*)` is a (P)-datum with box `−f* ≡ −1/f = (−f)^{−1}`·... i.e. `(−f)^{−1}·1`? —
precisely `−f* ≡ −f^{−1} = (−f)^{−1}` (as `(−1)^{−1}=−1`). ∎

**Lemma 1.2 (no level-0 boxes).** No class of any family contains all 17-generic points
(i.e. there is no box with `F=1`). *Proof:* see §2 (rigid forms with F=1 have no solutions).
