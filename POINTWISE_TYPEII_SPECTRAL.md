# POINTWISE_TYPEII_SPECTRAL — automorphic structure of Type II solutions for fixed p (task O128)

Status labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010 (`sources/elsholtz-tao-1107.1010.pdf`),
§2 eqs. (2.13)–(2.21), Prop 2.6/2.7, Lemma 2.8. TTL = `EXCEPTIONAL_TYPEI_LOGLOG.md` (Type I Heegner method).
`f_II(p)` = number of Type II solutions (x,y,z) of 4/p = 1/x+1/y+1/z (p | y, z; p ∤ x), ordered in (y,z).

## 0. Summary

(written at the end)

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
