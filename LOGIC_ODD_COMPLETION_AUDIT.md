# Odd congruence landing: what actually lifts?

**§0 (z74 Opus xreview fix).**
```
Result: for a countable Bezout domain D with −1 a sum of two squares in every R_m=D/mD, (2,m)=1, the odd inverse limit
        S has every unit a sum of four squares and every element a sum of five; four squares for all of S follow
        under (L) (e.g. Pic(R_m)[2]=0, or D an EDR), and a coherent norm −1 pair follows under semilocality.
Label:  PROVED (internal) for §1; PROVED assuming (L) for §2; PROVED assuming cofinal semilocality for §3
Scope:  algebra of the odd part of the interface in LOGIC_LAGRANGE_END_TEST.md §4 only; does not derive (L) or
        semilocality from Bezout + IOpen, and gives no second end extension.
Review: cross-model data/z74/xreview/REVIEW_ENDEXT_OPUS.md (rows OCA1–OCA7; ACCEPT-WITH-FIXES, fixes applied)
Triage: BARRIER-SCOPED / supporting lemma (no separate row)
STATUS delta: none
```
**Hypotheses, stated explicitly (z74 Opus xreview fix).** `D` is any countable Bézout **domain**. In the application it is discretely ordered with IOpen, but §§1–3 use neither. A modulus `m` is *odd* if `(2,m)=D`, so that 2 is invertible in `R_m`. Unit moduli are discarded. This note supersedes `LOGIC_ODD_QUATERNION_LIFT.md`.

**Verdict.** Let `D` be the countable discretely ordered Bézout domain in the question, `R_m=D/mD` for positive odd `m`, and `S=lim R_m`. Assume `−1` is a sum of two squares in **each** `R_m`. From these hypotheses I get every **unit** of S as a sum of four squares and **every element** as a sum of five. A cofinal local Picard condition gives a primitive hyperbolic plane for four squares; a cofinal semilocal condition gives the exact coherent pair for `−1`. I do **not** derive either additional condition merely from Bézout + IOpen, or exhibit a counterexample to four squares under the stated hypotheses. This concerns only the odd part of `LOGIC_LAGRANGE_END_TEST.md` §4.

### 1. Unconditional unit lifting and an additive consequence (PROVED)

Discard the trivial modulus 1. Countability gives a cofinal increasing divisibility sequence (successive products of enumerated moduli); no finite branching is assumed. On all levels 2 is invertible. Write `H=(-1,-1)` for the quaternion algebra with basis `1,i,j,ij`; its reduced norm is `Q=Σx_i²`. If `C=R_m[i]` and `b∈C` has `b b̄=−1`, represent `i` by multiplication by i on C and `j` by `w↦b w̄`. This is a splitting `H_m≅End(C)≅M₂(R_m)` carrying norm to determinant: every endomorphism has the unique form `w↦c w+d w̄` (solve from the images of 1,i using 2 invertible), whose determinant is `N(c)−N(d)`. No compatibility of the chosen b's is implicit.

For `m|n`, `SL₂(R_n)→SL₂(R_m)` is onto. In fact lift to D: for lifts `a,b` of the first column, `(a,b,m)=1`. A unimodular change of two coordinates over the Bézout **domain** takes `(a,b)` to `(g,0)`, `g=gcd(a,b)`. `(g,m)=1`, so `(g,m)` as a column is a primitive lift of `(g,0) mod m`; undo the basis change. Complete that column to determinant one over D. Modulo m the discrepancy with the requested second column is a multiple of the first (use the determinant-one basis); lift that multiple and correct. Reduction mod n proves the assertion. If both initial lifts are zero, the claimed first column was not unimodular. This needs neither stable range one nor a terminating Euclidean algorithm.

Now fix **any** `s∈Sˣ` and any old quaternion `q_m` of norm `s_m`. Choose a splitting at n, reduce **that same splitting** to m, and call the old matrix in its coordinates M. Then `M diag(s_m⁻¹,1)` has determinant 1. Lift it to `L∈SL₂(R_n)` and take `L diag(s_n,1)` in the chosen splitting at n. This lifts the actual old quaternion and has precisely the prescribed norm. Induct along the cofinal sequence. In particular choose `Σh_i²=−1` in S. For every `a∈S`,

```
a = ((a+1)/2)² + Σ_{i=1}^4 (h_i (a−1)/2)².
```

Thus **five** squares suffice, even for arbitrary nonunits. The displayed unit-target lift cannot plug in `s=0`: it used `s_m⁻¹`. This additive identity is not a four-square argument.

### 2. Four squares from a weaker local condition than PID

**PROVED assuming (L):** on a cofinal divisibility sequence, over each `R_m` every line module `L` such that `L⊕L≅R_m²` is free. In particular it suffices that `Pic(R_m)[2]=0` there: take exterior squares. Only two-generated lines of that special kind matter. EDR for D also suffices, since its quotients are EDRs and a rank-one idempotent of constant rank over such a ring has free image (diagonal reduction, first invariant factor unit, second zero).

Inductively keep a quaternion **idempotent** `e_m` that is `E₁₁` under *some* splitting. Start with any level splitting. At the next stage use a fresh splitting and reduce it to m. The matrix representing `e_m` there need not have a visibly free image. Nevertheless its image and kernel are isomorphic line modules: transport the **whole old matrix-unit system** into these new coordinates. The two off-diagonal units give inverse isomorphisms on the two images, which are complementary, locally of rank one. By (L) both are free. Taking basis columns of the two images gives `g∈GL₂(R_m)` conjugating `E₁₁` to this idempotent. Scale one column by `det(g)⁻¹`; this does not change the idempotent and makes `g∈SL₂`. Lift g and conjugate `E₁₁` at n. The result is again part of a full system of matrix units; **only the idempotent** must agree downwards. There is no unsupported claim that arbitrary `GL₂`, `PGL₂` or full algebra splittings lift.

The coherent idempotent e gives `u=e, v=1−e`, with `Q(u)=Q(v)=0` and `u·v=1/2` (since `Q(1)=1`). Thus the plane is split primitive: its dot-product Gram matrix is invertible and it is a direct summand. Explicitly `Q(e+a(1−e))=a` for every a in S. Equivalently `2e−1` has reduced trace zero and squares to 1, so its three pure quaternion coefficients have sum of squares `−1`. This is enough for the odd four-square target without straightening e into the special two-coordinate norm equation. In contrast, the quaternion lift for a unit target in §1 has no line-module issue whatsoever.

**Picard audit.** `Pic(D)=0` since an invertible fractional ideal of a Bézout domain is principal. That argument does **not** identify abstract rank-one projectives over its zero-divisor quotients with principal regular ideals, nor imply base change on Picard groups is onto. Călugăreanu–Pop–Vasiu, [*Matrix invertible extensions*, III, Thm 1.2(4)](https://arxiv.org/abs/2405.01234), identify freeness of all **two-generated** projective lines over **all principal quotients** of a Hermite ring with the elementary divisor ring condition. A Bézout domain is Hermite. Thus dismissing *all* these lines as automatically free amounts to invoking an EDR theorem, not the elementary Bézout identity. The restricted odd, doubled-line condition (L) is weaker. A nonfree line in an unrelated quotient is **not** a counterexample to (L), still less to coherence. In the matrix approach left/right determinant-one moves preserve the isomorphism class of a rank-one image, so mere surjectivity on `SL₂` does not remove it. Nor need a nonfree image rule out another successful chain or a lift of that line itself.

### 3. When the two coordinates themselves lift

**PROVED assuming the quotients on a cofinal chain are semilocal** (e.g. each odd modulus lies in only finitely many maximal ideals). Put `T_m={c∈R_m[i]ˣ:c c̄=1}`. If `m|n` lie on the chain, take any norm `−1` element at n, reduce it and divide the desired old solution by this reduction. The discrepancy `c∈T_m` can be written `w/w̄` with w a unit: take `w=h+c h̄`. At a residue field of `R_m`, choose `h=1` unless `c=−1`, and `h=i` in that case. In the split residue algebra the two components of c are mutual inverses, so either **both** components of `1+c` are nonzero or both are zero; in the field case the same test works. CRT on the finitely many maximal ideals chooses h simultaneously. Then w is a unit and `c w̄=w`. The finite algebra `R_n[i]` is also semilocal; its units lift through the quotient onto `R_m[i]ˣ` (take a lift and impose value 1 at the finitely many other maximal ideals by CRT). Lift w to a unit W, multiply the new solution by `W/W̄`, and proceed along the sequence. This proves the exact pair in S, not just universal four squares. More generally the norm `−1` sets are torsors for `T_m`, so a Mittag–Leffler condition on the images of the `T_n` at each level suffices: the nonempty coset images then stabilize, and their stable images lift along the countable chain.

Without semilocality, choices of `h` at each residue field do not establish a single h, and lifting a Gaussian unit is not lifting an `SL₂` matrix. Smooth lifting does suffice along *standard powers of one fixed odd m*: if a lifted Gaussian element has norm `−1+δ`, `δ∈(m^j)`, multiply by `1+δ/2` to repair through `m^(2j)`. Those towers need not be cofinal. No compactness of the individual quotients or extraction of a dyadic component is used. An odd completion alone inverts 2, so it cannot supply the full integral intersection in §4 by itself.

**Scope checks:** square classes, numerator 8, composites and standard ES zero screens are unaffected: the moduli here are ideals, not prime ES inputs. No assertion of a second end extension retaining Bézout, or of the assumed modular hypothesis from IOpen + Lagrange.
