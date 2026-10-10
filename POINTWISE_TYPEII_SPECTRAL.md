# POINTWISE_TYPEII_SPECTRAL — automorphic structure of Type II solutions for fixed p (task O128)

Status labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010 (`sources/elsholtz-tao-1107.1010.pdf`),
§2 eqs. (2.13)–(2.21), Prop 2.6/2.7, Lemma 2.8. TTL = `EXCEPTIONAL_TYPEI_LOGLOG.md` (Type I Heegner method).
`f_II(p)` = number of Type II solutions (x,y,z) of 4/p = 1/x+1/y+1/z (p | y, z; p ∤ x), ordered in (y,z).

## 0. Summary

Type II solutions of a fixed prime p carry an exact SL₂ structure: `ff' − 4c²(dp) = 1`, `f ≡ f' ≡ −1 (mod 4cd)`
(Lemma 1.1.3). This is the Type I Heegner structure of TTL with **p moved from the congruence (`f ≡ −p mod 4ad`)
into the level/discriminant (−4dp)** — ET's dilation Σᴵ → Σᴵᴵ on the SL₂ side (§1, PROVED). Consequences:
* Prop 2.1/Lemma 2.2 (PROVED): for fixed (p,d), Type II points are Heegner points of discriminant −4dp at level
  dp, uniformly separated (`cosh ≥ 3/2`). Remark 2.3: the det-p matrix `[[e,2a],[2ad,f]]` is a `T_p`-Hecke element.
* Prop 2.4/2.5 (PROVED): the Type II condition is an **exact incidence**: the point lies at hyperbolic distance
  exactly `arsinh(1/(c√|D|))` from the cuspidal geodesic `(∞, −1/(2c))` (`⟨u,v⟩_Q = −1`). The shells have width
  `|D|^{−1/2}`, below the point spacing `|D|^{−1/4}`.
* §3: averaging over p collapses the incidence to one progression mod f — the averaged sum `≍ N log³N` is a
  BV/BT problem, no spectral input (PROVED reduction; constant ≈ 0.05 Assessment).
* §4 (Assessment): the sufficient statement (TS) is a shell-incidence statement; Young's method reaches shells
  of width `|D|^{−1/18}` (`|D|^{−1/6}` under GLH); Type II needs `|D|^{−1/2}`. Gap `D^{4/9}` (`D^{1/3}` under GLH),
  not closed by averaging over c or d. Precise negative conclusion: no existing or GLH-conditional
  equidistribution theorem implies `f_II(p) > 0`.
* §6 Lemma 6.1 (PROVED): Type II points lie in the genus `χ_{−4d} = −1`, i.e. `(p/f) = −1`; this recovers ET
  Prop 1.6 (`f_II(s²) = 0`), and shows the shell main term is false at squares — any correct method must carry
  the genus character. At reachable scales the automorphic input cannot see square-mimicking primes.
* §5 (EVIDENCE, p ≤ 10⁷): `f_II(p) ≥ 1` throughout; `min f_II/log³p ≈ 0.012–0.017`; hard primes are the
  square classes mod 840; normalised lower tail `R ≈ 0.28` and slowly widening; the fixed-p random-root Heegner
  predictor does not track hard primes (actual/predicted 0.27–0.38 vs 0.9–3.5).
**Net:** Type II has the hoped-for SL₂/Heegner structure, but for fixed p it is an exact-incidence problem at
scale `|D|^{−1/2}`, out of reach of spectral equidistribution by a power `D^{1/3}` even under GLH. No step
toward ES is claimed.

## 1. Type II parametrisations (PROVED, elementary)

**Lemma 1.1.** For a prime p ≥ 5 the following sets are in bijection (Type II solutions ↔ each line):
1. (ET Prop 2.6) quadruples `(a,b,c,d) ∈ ℕ⁴` with `4abcd = a + b + pc`, `gcd(a,c) = 1`; the solution is
   `(x,y,z) = (abd, acdp, bcdp)`. [ET require gcd(a,b,c) = 1; since `b = ce − a`, `gcd(a,c) | b`, so this is
   gcd(a,c) = 1.]
2. (det-p form) `(a,c,d,e)` with `e f − 4a²d = p`, `f := 4acd − 1`, `gcd(a,c)=1` (`b = ce − a`). Equivalently
   `M = [[e, 2a],[2ad, f]]` has **det M = p** and `f ≡ −1 (mod 4ad)`.
3. (SL₂ form) `(c,d,f,f')` with **`f f' − 4c²·(dp) = 1`**, `f ≡ f' ≡ −1 (mod 4cd)`, `gcd((f+1)/4cd, c) = 1`
   (`f = 4acd − 1`, `f' = 4bcd − 1`). I.e. `γ = [[f, 2c],[2c·dp, f']] ∈ SL₂(ℤ)`, and
   `γ = −I + 2c·[[2ad, 1],[dp, 2bd]]`.
4. (divisibility) `(a,c,d)` with `(4acd − 1) | (a + pc)`, gcd(a,c) = 1 (then `b = (a+pc)/(4acd−1)`).
5. (residue form) `(a,b)` with `e := (−p mod 4ab)` (least positive residue) dividing `a + b` and
   `gcd(a, (a+b)/e) = 1` (then `c = (a+b)/e`, `d = (p+e)/4ab`).

*Proof.* 1 is ET Prop 2.6. (1⇒3) `(4acd−1)(4bcd−1) = 16abc²d² − 4cd(a+b) + 1 = 4cd(4abcd − a − b) + 1 =
4c²dp + 1`. (3⇒1) reverse the computation. (1⇔2) is ET (2.19) with `e = (a+b)/c` (an integer: (2.15)
mod c). (1⇔4): `b(4acd−1) = a + pc`. (1⇔5): `4abd = p + e` (ET (2.13)), `e | a + b`; and `e ≤ a+b < 4ab`
unless a = b = 1 (then e ∈ {1,2} < 4), so e is the least positive residue of −p mod 4ab. ∎
Checked against brute force for all primes 5 ≤ p < 400 (1243 solutions; `scripts/t2s_param.py`).

**Duality with Type I (PROVED, same computation).** Type I (TTL §1): `(4acd − p) | (pa + c)`; Type II:
`(4acd − 1) | (a + pc)`. In SL₂ language:

| | discriminant of Heegner form | SL₂ identity | congruence carrying p |
|---|---|---|---|
| Type I | −4d | `ef − 4a²·d = 1` | `f ≡ −p (mod 4ad)` |
| Type II | −4dp | `ff' − 4c²·(dp) = 1` | `f ≡ −1 (mod 4cd)` |

This is ET's non-isotropic dilation `(a,b,c,d,e,f) ↦ (a,b,c/n²,dn,n²e,f/n)` between Σᴵ and Σᴵᴵ read on
the SL₂ side: **p moves from the congruence into the level.**

## 2. Heegner / SL₂ structure

Notation of TTL §2: `𝓕_D = {[A,B,C] : B² − 4AC = −4D, A > 0, B ≡ 0 (2D), C ≡ 0 (D)}`, root `z_Q`,
`w_Q = z_Q/D`; `Γ⁰(D)` acts on 𝓕_D, `Λ_D` = the finite set of classes.

**Prop 2.1 (Type II solutions are level-dp Heegner points; PROVED).** For fixed p, d the map
`(c, f) ↦ Q = [f, 4c·dp, dp·f']` sends the Type II solutions with this d injectively into 𝓕_{dp}
(discriminant `−4dp`), with `w_Q = (−2c + i/√(dp))/f`. Its image is the set of `Q = [A, B, C] ∈ 𝓕_{dp}`
with `B ≡ 0 (mod 4dp)`, `B > 0`, `A ≡ −1 (mod B/p)` and the coprimality of Lemma 1.1.3.
*Proof.* `16c²d²p² − 4dp·ff' = −4dp(ff' − 4c²dp) = −4dp`; B, C divisibilities are visible; injectivity: c = B/4dp, f = A. ∎
Every class of discriminant −4dp occurs in 𝓕_{dp} (choose A coprime to dp and B ≡ 0 mod 2dp by CRT),
so `#Λ_{dp} ≍ h(−4dp)·2^{O(ω(dp))} = (dp)^{1/2+o(1)}`, on a curve of volume `≍ dp`.

**Lemma 2.2 (uniform separation; PROVED).** For fixed (p,d), the Type II points `z_Q`, Q as in Prop 2.1,
are pairwise at hyperbolic distance with `cosh ≥ 3/2`.
*Proof.* TTL Lemma 2.2 applied to 𝓕_{dp}: `4dp | disc(Q − Q')` and `cosh − 1 = disc(Q−Q')/(8dp)`. ∎
(Checked numerically for p < 400 in `t2s_param.py`.) *Contrast:* in the det-p coordinates (Lemma 1.1.2;
forms `[f, 4ad, de]` of the same discriminant −4dp, but only `B ≡ 0 (2d)`, `C ≡ 0 (d)`) the same lemma
gives only `cosh − 1 ≥ 1/(2p)`: separation needs the dilated (level-dp) coordinates.

**Remark 2.3 (det-p / Hecke view).** `M = [[e,2a],[2ad,f]]` of Lemma 1.1.2 lies in the Hecke set
`Δ_p = {det = p}`; the Type I matrix of TTL has det 1. So Type II = Type I with SL₂(ℤ) replaced by the
`T_p`-correspondence; on the level of points this is the passage from discriminant −4d to −4dp (Prop 2.1).

**Prop 2.4 (the Type II condition is an exact hypercycle incidence; PROVED).** Let `w = X + iY = w_Q` for
`Q = [f, 4cdp, dpf']` as in Prop 2.1. Then `f ≡ −1 (mod 4cd)` with `(f+1)/(4cd) = a` iff
`X = −(1 + Y√(dp))/(2ad)`, i.e. `w` lies on the Euclidean ray `H_{a,d}` from the cusp `−1/(2ad)` through
the point `−i/√(dp)`; such a ray is a **hypercycle** (equidistant curve) of the geodesic `{−1/(2ad) + it}`.
*Proof.* `f = 1/(Y√dp)`, `c = −Xf/2`; substitute in `f + 1 = 4acd`. ∎ (Checked in `t2s_param.py`.)
In det-p coordinates `w₁ = (−2a + i√(p/d))/f` the same statement holds with `a ↔ c`:
`X₁ = −(1 + Y₁√(d/p))/(2cd)`.
*Consequence (Assessment).* For fixed p the Type II condition is not a box condition on Heegner points
(as in TTL, where n was summed and the congruence `f ≡ −n (4ad)` was absorbed by the free c), but an
exact incidence with a measure-zero set (a countable union of hypercycles). Any spectral counting must
first thicken `H_{a,d}`; the natural thickening is the discreteness of Λ_{dp} itself (Lemma 2.2).

**Prop 2.5 (level-1 form; PROVED).** The det-p forms `Q = [f, 4ad, de]` (Lemma 1.1.2) are level-1
Heegner forms of discriminant `−4dp`, and the Type II condition is `A ≡ −1 (mod B)`, `B ≡ 0 (4d)`,
`d | C`. With `u = (1,0)`, `v = (1,−2c)` and the bilinear form `⟨·,·⟩_Q` (Gram `[[A, B/2],[B/2, C]]`):
`A − cB = ⟨u, v⟩_Q`, so the Type II condition with this c is **`⟨u,v⟩_Q = −1`**. Writing
`Q(x,y) = √|D|·|x − z y|²/(2 Im z)` (z the root, `|D| = 4dp`) gives
`⟨u,v⟩_Q = √|D|(1 + 2c·Re z)/(2 Im z)`, hence (since `sinh dist(z, {Re = x₀}) = |Re z − x₀|/Im z`):
**a Type II point is a Heegner point of discriminant −4dp at hyperbolic distance exactly
`arsinh(1/(c√|D|))` from the cuspidal geodesic `γ_c = (∞, −1/(2c))`, on its left.** Integrality of
⟨u,v⟩ makes the shell `T_c = {z left of γ_c : sinh dist(z,γ_c) ∈ [½, 3/2]/(c√|D|)}` an honest region whose
Heegner points (of disc −4dp with the B, C congruences) are exactly the Type II points with this c (and d).
*Proof.* Direct substitution; `⟨u,v⟩_Q = A − cB` since `⟨e₁,e₂⟩ = B/2`. ∎ (Same as Prop 2.4, written
intrinsically.)

## 3. Averaged-over-p sanity check

**Prop 3.1 (PROVED, elementary).** For fixed `(c, d, f)` with `f ≡ −1 (mod 4cd)`, the Type II condition
`f | 4c²dp + 1` (Lemma 1.1.3; `f'` is then automatically `≡ −1 (4cd)`, since `ff' ≡ 1 (4cd)`) is the single
residue class `p ≡ −(4c²d)^{−1} (mod f)` (note `gcd(f, 2cd) = 1`). Hence
`Σ_{p≤N} f_II(p) = Σ_{c,d,a; gcd(a,c)=1} w·π(N; 4acd−1, r_{c,d}) ` (range/weights as in Lemma 2.8 of ET).
So **averaging over p collapses the Heegner incidence of Prop 2.4 to one arithmetic progression mod f**:
the averaged Type II sum is a Bombieri–Vinogradov/Brun–Titchmarsh problem, and no spectral input is
needed (consistent with ET, who get `≍ N log³N` for Type II with no log log loss; the spectral input in TTL
was needed only for Type I). The Heegner picture "reproduces" ET only in this trivial sense.

*Heuristic constant (Assessment).* With `π(N;f,r) ≈ π(N)/φ(f)`, the region `a ≤ b` (`2α+δ ≤ 1`) and
`e ≥ 1` (`γ ≤ 1−α−δ`) in log-coordinates (`a = p^α, d = p^δ, c = p^γ`) has volume 1/8, so
`f_II(p) ≈ 2·(1/4)·(1/8)·κ·log³p`, `κ = E[f/φ(f)]·P(gcd(a,c)=1) ≈ 1.30·0.61`, i.e. `≈ 0.05 log³p`.
Empirically the mean of `f_II(p)/log³p` is 0.0998 (p≈2¹⁰), 0.0779 (2¹⁶), 0.0679 (2²³), slowly decreasing
(positive lower-order `log²` terms) — consistent with a limit near 0.05 (EVIDENCE, weak).

## 4. Fixed p: the automorphic family, the target, and the gap

**4.1 The family.** For fixed p: `{Λ_{dp}}_{d ≥ 1}` — Heegner points of discriminants `−4dp` (fields
`ℚ(√−dp)`, varying with d), with the B ≡ 0 (4d), d | C level data (Prop 2.5) — or, uniformly separated, the
level-dp sets of Prop 2.1/Lemma 2.2. **The single discriminant −4p (d = 1) already carries the d = 1 family**,
which has expected size `≍ log²p` (§5: actual d=1 counts 0–98 for p ≈ 10⁶).

**4.2 The target (Prop 2.5).** `T(p,d) = ⋃_{c} T_c ∩ {height range}`, a union of shells of width
`w_c = 1/(c√|D|)` (`|D| = 4dp`) along cuspidal geodesics γ_c, of hyperbolic length `ℓ ≈ log(a_max) ≈ ½log(p/d)`.
Area `≈ Σ_c ℓ/(c√|D|) ≈ log²(p/d)/√(dp)`; with `#Λ ≈ |D|^{1/2}` points on a curve of volume `≍ 1` (level 1),
the expected count is `≈ log²(p/d)` per d … weighted by the level data, `≈ log²(p/d)/d` (§3), total `log³p`.
**Typical spacing of Heegner points is `|D|^{−1/4}`; the shells have width `|D|^{−1/2}`** — the target is below
the point spacing by `|D|^{1/4}`: an exact-incidence problem disguised as a region (integrality of ⟨u,v⟩).

**4.3 The statement that would suffice.** (TS) *For every large prime p there are d, c ≤ p^{o(1)} such that
the Heegner points of discriminant −4dp (with the level data of Prop 2.5) meet the shell `T_c` in the
genus `𝔊⁻ = {χ_{−4d}(Q) = −1}`* (Lemma 6.1 below: Type II points automatically lie there). (TS) ⇒ f_II(p) > 0.
A counting version: `#(Λ_{4dp} ∩ T_c) = h·area/vol·(1 + o(1))` on average over c ≤ C.

**4.4 Gap to known results (Assessment, using `LITERATURE_AUTOMORPHIC.md`).** Young 2017 Thm 2.1 error
`‖φ‖₂ D^{5/12+ε} V^{1+ε}` (Lindelöf: `D^{1/4+ε}`) against main `D^{1/2}‖φ‖₁`. For a shell of width w and length
`ℓ ≈ log D`: `‖φ‖₁ ≈ wℓ`, `‖φ‖₂ ≈ (wℓ)^{1/2}`, `V ≈ w^{−1}`. Main beats error iff
`w^{3/2} ≫ D^{−1/12+ε}`, i.e. **`w ≫ D^{−1/18}` (unconditional — exactly Young's cusp-strip range)**, and
`w ≫ D^{−1/6}` under Lindelöf. Type II needs **`w ≍ D^{−1/2}/c`**: gap `D^{4/9}` unconditionally, `D^{1/3}`
under GLH. Summing over c ≤ C does not change V (the c = 1 shell is the thinnest) and adds at most a factor
`log C` to the main term. Summing over d ≤ D₀ does not help either: at `w = |D|^{−1/2}` the GLH error per d is `≈ (wℓ)^{1/2}|D|^{1/4}w^{−1} ≈ |D|^{1/2}` (polylog factors dropped) against a per-d main term `≈ log²p/d`; even square-root cancellation across d leaves error `≫ D₀·p^{1/2}` against total main `≪ log³p`. Even optimal pointwise square-root cancellation
over the class group (error `≈ (h·area)^{1/2}`) would be ≈ `log p` against main `log²p` — fine — but no
spectral method gives that at Sobolev scale `V = D^{1/2}`: smoothing at the point-spacing scale `D^{−1/4}` is
the natural limit of any equidistribution statement, and the target is `D^{1/4}` finer. Compare Young
Prop 1.2 (existence of roots of `b² ≡ −D (mod 4a)` with `a ≍ √D`, `|b| ≍ √D/V`, `V ≪ D^{1/18}`): the Type II
root condition is `ν = 2ad` with `ν² ≡ −dp (mod f)` **and `f ≡ −1 (mod 2ν)`**, i.e. ν is pinned to one residue
(`ν ≡ (2c)^{−1} mod f`), not to an interval of length `f/V`. **Conclusion (Assessment): no existing or
GLH-conditional equidistribution theorem reaches (TS); the obstruction is the exact-incidence nature of the
Type II condition (Prop 2.4/2.5), not the strength of subconvexity.**

## 5. Numerics (EVIDENCE; `scripts/t2s_count.c`, `t2s_numerics.py` → `t2s_numerics.out.txt`; `t2s_predict.c` → `t2s_predict.out.txt`)

Engine: all ET quadruples with `a ≤ b` via `(a,c,d,e)`, weight 2 (1 if a = b); validated against an
independent Python enumeration for all primes < 700 (which is validated against brute force < 400).
`n ≤ 10⁷`: 9.2·10⁸ tuples, 8 s.
* `f_II(p) > 0` for every prime `5 ≤ p ≤ 10⁷` (known: ES has been verified far beyond). Dyadic minima of
  `f_II` grow: 4 (2¹¹), 18 (2¹⁶), 36 (2²⁰), 60 (2²²), 72 (2²³, p = 9744001). `min f_II/log³p` is flat:
  0.0117–0.017 for p ≥ 10⁵ (smallest: p = 2031121, f_II = 36), against mean ≈ 0.068.
* Subfamilies: `d = 1` is empty for some p in every block ≥ 2⁶ (e.g. 135 primes in 2²² have no d = 1
  solution); `c = 1` is empty for 0–3 primes per block: no single Heegner discriminant (d = 1) suffices numerically; the full d-family is needed.
* Every one of the 20 smallest normalised values (p ≥ 10⁵) has `p ≡ 1 (mod 24)` except one (`p ≡ 13`); the six
  smallest class means mod 840 are exactly the six square classes `{1,121,169,289,361,529}` (≈ 0.037–0.042
  vs 0.32 for `p ≡ 839`): **square-mimicking primes are the hard ones for Type II.**
* `R(p) = f_II(p)/mean(f_II over q ≡ p mod 840, same dyadic block)`: min R = 0.43 (2¹⁶), 0.31 (2²⁰), 0.28 (2²³);
  sd of R grows slowly 0.257 → 0.301. Relative fluctuations do **not** shrink with p (divisor-type
  fluctuation of the integers `4c²dp + 1`), so a pointwise lower bound must survive an `R ≈ 1/4` lower tail
  even after the mod-840 singular series.
* Per-family predictions (30 primes in [0.67, 2.1]·10⁶: the 10 hardest + 20 random). The fixed-p
  "random root" Heegner prediction `E_heeg = Σ w·ρ_{−dp}(f)/f` (chance that ν = 2ad is a root of
  `ν² ≡ −dp (mod f)`) and the averaged `E_avg = Σ w/φ(f)` are both ≈ 110–180 for **all** 30 primes; actual
  `f_II` is 36–48 for the hard ten (actual/E_heeg 0.27–0.38) and 122–619 for the random twenty
  (0.9–3.5). By families (d = 1 | 2–7 | 8–63 | ≥ 64) the hard primes are depleted in every family, worst at
  d = 1 (0–8 vs predicted 12–21). **Assessment:** the Heegner/random-root model averages out exactly the
  information (p mod small moduli, through the factorisation of `4c²dp+1` at small c, d) that decides the
  hard primes; the singular series it produces is p-blind to leading order.

## 6. Square-mimicking primes and the genus obstruction

**Lemma 6.1 (genus lemma; PROVED).** For every Type II solution of a prime p, with `f = 4acd − 1`,
`f' = 4bcd − 1` coprime to p: `(p/f) = (p/f') = −1` (Jacobi). Equivalently the Type II Heegner forms of
discriminant −4dp lie in the genus `𝔊⁻_d = {χ_{−4d}(Q) = −1}`.
*Proof.* `ef = p + 4a²d` gives `(2ad)² ≡ −dp (mod f)` with `gcd(dp, f) = 1` (`f ≡ −1 mod 4ad`), so
`(−dp/f) = 1`. `(−d/f) = (−4d/f)` and the Kronecker symbol `(−4d/·)` is a character mod 4d with value
`sign(−4d) = −1` at `−1`; `f ≡ −1 (mod 4d)` gives `(−d/f) = −1`, so `(p/f) = −1`. Same for f'
(Lemma 1.1.3 symmetry). ∎ Checked for all 2486 moduli with p < 400 (`t2s_param.py`).
**Cor 6.2 (ET Prop 1.6, Type II half, recovered).** For `n = s²` odd, `(s²/f) = 1` (gcd(s,f) = 1 since a common
prime would divide `4a²d`, coprime to f), so `f_II(s²) = 0`. **Our route fails at n = p², as it must:** the
genus `𝔊⁻_d` is empty for discriminant `−4ds²` (every represented A coprime to 2ds has `χ_{−4d}(A) = +1`),
although the shells `T_c` have the same area `≈ log²/(c√|D|)`, and the CM points of `ℤ[s√−d]` equidistribute
(Hecke orbits). So the shell main term `h·area/vol ≈ log²` is **false** at squares: a second proof that the
shells are below every equidistribution scale, and that any correct count must carry the genus projector
`(1 − ψ_d)/2`, `ψ_d(Q) = χ_{−4d}(A)`.
**Cor 6.3 (PROVED).** If `(p/q) = 1` for all primes `q ≤ y`, every Type II f (and f') has a prime factor
`q > y` with `(p/q) = −1`. (Type II solvability is a non-residue phenomenon; cf. the Mordell-hard primes,
`n_p`, of the pointwise line.)

**What the automorphic input sees (Assessment).** (i) Measures: genus-restricted equidistribution
(Duke; Humphries Thm 1.24-type for genera) holds for every prime p; at any scale where it is a theorem it
is blind to square-mimicking (the genus `𝔊⁻_d` has the full share h/#genera of points). (ii) The ψ_d-twisted
Weyl sums factor (genus characters) into `L(·, χ_{−4d})·L(·, χ_p)` (constant/Eisenstein part) and
`L(½, u_j×χ_{−4d})L(½, u_j×χ_p)` (cusp part); for square-mimicking p, `L(s, χ_p)` agrees with ζ at all small
primes, so these terms grow toward the size of the main term — the analytic shadow of Cor 6.2 — but at the
shell scale `|D|^{−1/2}` they are not controlled anyway (§4.4). (iii) Relation to POINTWISE_SIZE Thms M, C,
Prop A: a spectral existence theorem is analytic (E2-type) input and is not itself a congruence procedure,
so Theorem C does not forbid it; but §4.4 shows the only available spectral statements live at scales
`≥ |D|^{−1/18}` (`|D|^{−1/6}` under GLH), while the Type II target is at `|D|^{−1/2}`; at the reachable scales the
input is genus-equidistribution, which is identical for square-mimicking and generic primes. So the automorphic
input **cannot distinguish** square-mimicking primes at any reachable scale, and the numerically decisive
information (§5) sits exactly in the unreachable `|D|^{−1/2}` regime.

---
# Round 2 (O128b): the algebraic angle

## 7. Exact lattice data

**Set-up.** `L = {[A,B,C]} ≅ ℤ³` (integral binary quadratic forms), `q([A,B,C]) = B² − 4AC` (signature (2,1);
q < 0 ⇔ definite form ⇔ point of ℍ, q > 0 ⇔ indefinite form ⇔ geodesic), bilinear form
`b(x,y) = q(x+y) − q(x) − q(y) = 2BB' − 4AC' − 4A'C`. `SL₂(ℤ)` acts by `x ↦ x∘γ`, isometrically; this is the
standard isomorphism `PSL₂(ℤ) ≅ SO⁺(L)` up to finite index (L ≅ the trace-zero matrices `[[B/2·, ·],[·, ·]]`
up to scaling: `[A,B,C] ↔ [[B, 2C],[−2A, −B]]` has `−det = B² − 4AC`).

**Prop 7.1 (Gram data; PROVED).** For a Type II quadruple (a,b,c,d) of p (Lemma 1.1.2) let
`Q = [f, 4ad, de]`, `S_c = [0, 2c, 1]`. Then `q(Q) = −4dp`, `q(S_c) = 4c²`, `b(Q, S_c) = 4(cB − A) = 4`. So
`ℤQ + ℤS_c ⊂ L` has Gram matrix (w.r.t. `q`) `T = 4·T₀`, **`T₀ = [−dp, 1, c²]`** (the binary form
`−dp x² + xy + c² y²`), `disc T₀ = 1 + 4c²dp =: N_{c,d}`. Conversely a vector `Q = [A,B,C] ∈ L` with
`q(Q) = −4dp`, `A > 0`, `b(Q, S_c) = 4`, `B ≡ 0 (4d)`, `d | C`, `gcd(B/4d, c) = 1` is a Type II solution
(`a = B/4d`, `f = A = cB − 1`, `e = C/d`). (Checked, `t2s_ternary.py`.)
`S_c` is the split form `Y(2cX + Y)`; its geodesic is `(∞, −1/2c)` (§2.5).

**Prop 7.2 (Pell form; PROVED).** With `m = a − b`, `D' = d²m² + dp`, `T = 2cd(a+b) − 1`:
`T² − D'(2c)² = 1`. Conversely every solution `(T, 2c)` of `x² − D'y² = 1` with `D' = d²m² + dp` and
`T ≡ −1 (mod 2cd)`, `(T+1)/2cd ≡ m (mod 2)`, `|m| < (T+1)/2cd` gives a Type II quadruple (up to gcd(a,c)).
*Proof.* `T² − 4c²d²m² = (T − 2cdm)(T + 2cdm) = (4bcd − 1)(4acd − 1) = 1 + 4c²dp` (Lemma 1.1.3). ∎
So Type II solutions are **unusually small units** `T + 2c√D'` (`T ≍ c√D'`) of the orders `ℤ[√(d²m² + dp)]` —
the Type II analogue of TYPEI4's "fibre certificates are norm-1 units". Since `h(D')·log ε_{D'} ≍ √D'·L(1,χ)`,
a small unit forces `log ε ≪ log(c√D')`, i.e. near-maximal class number of `ℚ(√D')`: one more way to see that
Type II lives in a thin, arithmetically special set.

## 8. Reduction theory, invariance, and the collapse to the divisor condition

**Prop 8.1 (exact reduction; PROVED).** For fixed `(c,d)` put `M = 4cd`, `N = N_{c,d} = 4c²dp + 1`. Then
`f_II(p) = Σ_{c,d ≥ 1} #{f | N : f ≡ −1 (mod M), gcd((f+1)/M, c) = 1}` (both orientations a ≶ b counted), and
`F(p) := Σ_{c,d} #{f | N : f ≡ −1 (mod M)} = Σ_{(a,b,c,d) primitive} #{g : g² | d} ≥ f_II(p)`, with
`F(p) > 0 ⇔ f_II(p) > 0`.
*Proof.* Lemma 1.1.3: (a,b) ↔ f = 4acd − 1, with `f' = N/f ≡ −1` automatic (`ff' ≡ 1 mod M`); `f, f' > 0` gives
`a, b ≥ 1`, and `c | a+b` is automatic from `4abcd = a + b + pc`; so the sum over (c,d) is finite. A
non-primitive solution `(ga', gb', gc', d)` satisfies `4g²a'b'c'd = a' + b' + pc'`, i.e. it is the primitive
`(a', b', c', g²d)`. ∎ (Checked for p < 160 against the quadruple enumeration.)

**Prop 8.2 (the group acting, and what is invariant; PROVED).** (i) The stabiliser of `S_c` in `SL₂(ℤ)` is
`{±I}` (a split form of square discriminant has no non-trivial automorphs: `t² − 4c²u² = 4` forces u = 0).
Hence, once S is normalised to `S_c` inside its `SL₂(ℤ)`-orbit, **Q is determined: there is no residual
group action and no reduction-theory freedom.** (ii) The `SL₂(ℤ)`-classes of primitive vectors with `q = 4c²`
are `S_{c,k} = [0, 2c, k]`, `k ∈ (ℤ/2c)^×` (translation `X ↦ X + jY` shifts k by 2cj). The pair-invariants
are the Gram matrix `T`, the class k of S, and (with the level structure) the classes of `Q` mod `Γ⁰(d)`-type
data. For class `k`, `b(Q, S_{c,k}) = 4(cB − kA)`, so the general condition `b = 4` reads `kA = cB − 1`;
**Type II is the single class `k ≡ 1 (mod 2c)` together with the congruences `B ≡ 0 (4d)`, `d | C`** — these
are not invariants of the Gram matrix. (iii) Positivity: `(−Q, −S_c)` has the same Gram matrix, and
`−S_c ~ S_{c,−1}`; so "A > 0" is the choice `k = +1` vs `k = −1`, i.e. achieved inside the orbit exactly when
the k-class is ±1; it is not an extra restriction beyond the class condition.

**Prop 8.3 (everything except one sign is automatic; PROVED).** For every `n ≥ 1` (prime or not, including odd
squares) and every `(c,d)`, the vector `Q₀ = [−1, 0, −dn] ∈ L` satisfies `q(Q₀) = −4dn`, `b(Q₀, S_c) = 4`,
`B ≡ 0 (4d)`, `d | C`: a **global integral** solution of the whole embedding problem of Prop 7.1 except
positivity `A > 0` (it is the trivial factorisation `N = (−1)(−N)`, i.e. `a = 0`). Equivalently `(−Q₀, −S_c)` =
`([1,0,dn], S_{c,−1})` solves it with `A > 0` but in the class `k = −1`. So all local conditions (all ℓ-adic
ones, and the archimedean one up to sign) and hence genus and spinor-genus data are satisfied **for every n**,
in particular for `n = s²`, where `f_II(s²) = 0` (Cor 6.2). The entire content of Type II is: **N has a
positive divisor in the class `−1 (mod M)`, while it always has the positive divisor `1` in the class `+1`** —
the two differ exactly by the sign at ∞, i.e. by the ray class group mod `M·∞` (`(ℤ/M)^×`) versus mod M
(`(ℤ/M)^×/±1`). Odd characters (`η(−1) = −1`) are what detect it (§9).
*Consequence (PROVED, from 8.3 + Cor 6.2).* No statement of the form "locally represented + spinor
condition ⇒ represented" can hold for the Type II embedding problem with its congruence data: the odd
squares are a counterexample at every (c,d). The obstruction at squares is the quadratic-reciprocity
(genus-character) obstruction of Lemma 6.1 — in the language of the ES surface, the integral Brauer–Manin
obstruction (Bright–Loughran 2020, already cited in STATUS) — and it lives in the **split torus**: the
orthogonal complement of `S_c` in `L ⊗ ℚ` is split binary (q(S_c) is a square), and with S fixed the problem is
`N = (T − U)(T + U)`, `(T, U) ≡ (−1, 0) (mod 2cd)`: representations of a number by the isotropic form
`x² − y²` in a coset. For a split torus `𝔾_m` strong approximation fails; the obstruction group is
`(ℤ/M)^×` and the question is exactly whether the divisors of N hit the class −1. **Answer to (iii): the
ternary/spinor formulation collapses exactly to the divisor condition** (Prop 8.1), adds no information,
and is not weaker; Gauss/three-squares-type local–global arguments do not apply because the relevant
stabiliser is a split torus, not a semisimple group with strong approximation.

*Remark 8.4 (why three squares works and this does not).* In the three-squares theorem the stabiliser of the
represented vector is `SO(w^⊥)` for a positive definite binary `w^⊥`, i.e. an anisotropic torus whose class
group is controlled by genus theory + Siegel. Here the class of `S` is the binding constraint and its
stabiliser is the split torus: the counting is not by class numbers but by divisors in residue classes.
Choosing instead to fix `Q` and vary `S` (§9.2) brings back an anisotropic torus (the CM torus of ℚ(√−dp)),
but the Type II sum then runs over the whole genus 𝔊⁻ of Q, which averages the class-group information away.

## 9. Generating series: everything is Eisenstein

**Prop 9.1 (character expansion; PROVED).** With `M = 4cd`, `N = 4c²dn + 1` (so gcd(N, M) = 1),
`#{f | N : f ≡ −1 (M)} = (1/φ(M)) Σ_{η mod M} η(−1) σ_η(N)`, `σ_η(N) = Σ_{f|N} η(f)`.
(Orthogonality.) For odd η, `Σ_N σ_η(N) qᴺ` is the holomorphic weight-1 Eisenstein series `E₁(1, η)` of level
M; for even η, `σ_η(N)` is (up to the factor `N^{0}K₀`) the N-th coefficient of the weight-0 Eisenstein series
`E(z, ½; 1, η)`. So by Prop 8.1 `F(n) = Σ_{c,d} (1/φ(4cd)) Σ_η η(−1) σ_η(4c²dn + 1)`: **a finite sum, over
≍ n log n levels `4cd`, of Eisenstein coefficients evaluated along the progressions `N ≡ 1 (4c²d)`. There is no
cuspidal term at all.**

**Prop 9.2 (genus pairing; PROVED).** Let `ψ = χ_{−4d}` (odd real character mod 4d | M). For n = p prime and
f | N: `ψ(f) = (p/f)` (from `(−dp/f) = 1`, Lemma 6.1). Pairing η ↔ ηψ (opposite parities):
`#{f | N : f ≡ −1 (M)} = (1/φ(M)) Σ_{η even} Σ_{f|N} η(f)(1 − (p/f))`.
For `n = s²` (odd) every factor `1 − (s²/f)` vanishes: Cor 6.2 is **the exact cancellation of each even
Eisenstein coefficient against its odd genus-twin**. The η = 1 part, `MT_{c,d}(p) = (2/φ(M))#{f | N : (p/f) = −1}`,
is the "genus main term"; for `(c,d) = (1,1)` (M = 4) it is the whole count.

**EVIDENCE (`scripts/t2s_eis.py` → `t2s_eis.out.txt`; c ≤ 3, d ≤ 300, the 30 sample primes of §5).**
act/naive (η = 1 only): hard primes 0.17–0.76, random 0.71–1.83; act/MT (genus main term): hard 0.27–0.79,
random 0.70–1.72. The genus term corrects only a small part of the hard-prime deficit; the rest is carried by
non-genus characters η (distribution of the divisors of the specific integers `4c²dp + 1` in residue classes
mod 4cd). Assessment: square-mimicking acts through *many* small-conductor characters at once, not through
one genus character.

**9.3 Fixing Q instead (CM theta series; Assessment with PROVED skeleton).** For fixed Q of discriminant −4dp,
`Q^⊥ ⊂ L` is a positive definite binary lattice (q(Q) < 0, signature (2,1)) of discriminant `≍ dp`, and
`{S : b(Q,S) = 4}` is a coset of it. Hence `Σ_S e(q(S)τ)` over this coset is a weight-1 **CM theta series** of
`ℚ(√−dp)`, which does have cuspidal (Hecke-character) components. Type II asks for coefficients at `4c²`
(squares) in the class `S ~ S_{c,1}`. But Type II sums over **all** Q in the genus 𝔊⁻_d (Lemma 6.1; nothing in
the ES conditions selects a class within the genus — the conditions `B ≡ 0 (4d)`, `d | C` are level data, the
k-class is a condition on S). By Siegel–Weil, the genus sum of these theta series is an Eisenstein series, and
the class-group (non-genus) characters, which carry the cuspidal part, cancel identically. This is consistent
with Prop 9.1: both orders of summation end up Eisenstein.

**9.4 Kudla / Gross–Kohnen–Zagier (Assessment).** In Kudla's theory the generating series of special cycles
`Z(T)` for the rank-2 lattice data `T = 4T₀ = 4[−dp, 1, c²]` is a genus-2 Siegel-type (here indefinite, weight
3/2) theta/Eisenstein object, and intersection numbers of CM cycles with geodesic cycles are its Fourier
coefficients (GKZ-type). Prop 7.1 says `f_II(p)` is a sum of such coefficients `a(T)` over
`T ∈ {4[−dp, 1, c²] : c, d ≥ 1}` with the extra class/level conditions. Three facts make this a dead end for a
pointwise route:
1. **No fixed form.** p enters only through the entry `T₁₁ = −4dp`, and the sum runs over `T₂₂ = 4c²`,
   `T₁₁ ∈ −4pℤ` with unbounded levels `4cd`. There is no single modular form whose p-th coefficient is
   `f_II(p)`. Restricting to bounded levels (c, d ≤ K) gives a fixed form (Prop 9.1 with finitely many levels),
   but then the count is `≈ log²K`-sized and vanishes for many p (§5: even the full d = 1 family is empty for
   ≈ 135 primes per dyadic block near 4·10⁶).
2. **No cusp part.** The `S_c` with `q(S_c) = 4c²` (a square) are isotropic-type: `S_c^⊥` is split, and the Siegel–Weil
   genus average kills the class-group characters (9.3). What remains is Eisenstein (Prop 9.1): divisor sums in
   residue classes.
3. **Eisenstein coefficients do not have "pointwise" main terms.** `σ_η(N)` are multiplicative functions of
   `N = 4c²dp + 1`. Nonvanishing of `Σ_η η(−1)σ_η(N)` for *some* (c,d) is precisely the original
   question (a divisor of some N in the class −1 mod M). It is a problem about the anatomy of the values of the
   polynomials `4c²d·X + 1` at X = p, i.e. the factorisation-shape territory of POINTWISE_SIZE Thms M/C. Any
   argument there must survive the square-mimicking points (Prop 9.2: exact cancellation at squares).

**Conclusion of round 2 (Assessment, with the PROVED reductions 7.1–9.2).** The algebraic/ternary route is
exact but **not new information**. Type II(p) for a pair (c,d) is an embedding `4[−dp,1,c²] ↪ L` with a class
condition on the isotropic-type vector `S_c`. This collapses to "N_{c,d} = 4c²dp+1 has a positive divisor ≡ −1
(mod 4cd)" (Prop 8.1). All local, genus and spinor data hold for every n (Prop 8.3; even globally up to the sign
at ∞). The obstruction group is the ray class group mod `4cd·∞` of a split torus, where strong approximation
fails. The generating series are Eisenstein (Props 9.1–9.2), with no cuspidal component whose size could be
bounded. There is therefore no "real automorphic pointwise route" here. What survives is the reformulation
"some `4c²dp + 1` has a divisor in a given class", together with its exact Eisenstein/genus bookkeeping.

## 10. Numerics to 10⁸ (EVIDENCE; `t2s_count 10⁸`, 1.35·10¹⁰ tuples; `scripts/t2s_numerics_1e8.out.txt`)
* `f_II(p) ≥ 1` for all 5 761 453 primes `5 ≤ p ≤ 10⁸`. Dyadic minima: 62 (2²³, p = 12257281), 74 (2²⁴),
  88 (2²⁵), 94 (2²⁶, p = 84525841). `min f_II/log³p` stays in 0.0143–0.0158 for blocks 2²³–2²⁶; overall minimum
  over p ≥ 10⁵ is still 0.0117 (p = 2031121). All 20 smallest normalised values are `≡ 1 (mod 24)`, except
  p = 1190701 (`≡ 13`). The six smallest mod-840 class means are again the six square classes.
* `R(p)` (class-mean ratio mod 840): min 0.268 / 0.248 / 0.253 / 0.239 (2²³…2²⁶), slowly decreasing. The 0.1%
  quantile is stable at ≈ 0.37, the 1% quantile ≈ 0.505, and the sd grows slowly (0.307 → 0.323). The lower tail
  thickens very slowly, consistent with divisor-function-type fluctuation of `Σ_{c,d}` over small (c,d) (Assessment).
* The d = 1 family (single discriminant −4p) is empty for 148–198 primes per block at 2²⁴–2²⁶.
