# bsC_eichler_orientation — the ES congruence as a level structure on supersingular curves (O176; O172 spark 2)

**ES is not solved here.** Labels as in DISCOVERIES.md. Notation of KUDLA_ES §1 / QUATERNION_ES §1.

## Idea
bsC_supersingular_transfer: the curve side is genus-vacuous because Kudla data are class functions of T. The
representative (ray-class) condition can only enter the geometry through **level structure**. Make it explicit:
Type I via the orientation of an Eichler order of level e; Type II via an involution structure on E[4cd].

## Literature
Voight GTM 288: Ch. 23 (Eichler orders = intersections of two maximal orders; level-N characters), Ch. 30 (optimal
embeddings with orientation; Eichler's embedding numbers ∏_{ℓ|N}(1 + (D/ℓ)) for squarefree N); Ribet, *On modular
representations…* Invent. 100 (1990) §2–3 (supersingular points of X₀(N) ↔ Eichler orders / pairs (E, C));
Gross, *Heights and special values of L-series* (1987) (oriented optimal embeddings in Eichler orders);
Kudla–Rapoport–Yang 2006 and Sankaran (*Unitary/level-structure Kudla* papers) for Eichler-level special cycles.

## Statements (PROVED, elementary)
**Prop 1 (Type I = oriented Eichler order with a liftable eigenvalue).** Let (a,b,c,d,e) be Type I for p, m = ab,
Λ = Λ_{d,m} ⊂ B_{p,∞}. (i) Λ is an Eichler order of level e (bsC_supersingular_transfer Prop 3); so Λ = End(E, C) for
a supersingular E with cyclic C ⊂ E of order e (Ribet). (ii) Its level characters `χ: Λ → ℤ/e` (2^{ω(e)} of them:
one choice of end at each ℓ | e) satisfy `χ(u)² = −d`, `2χ(u)χ(v) = 1`, `χ(v)² = −m`, and
`{χ(v)} = all square roots of −m mod e` (gcd(m,e) = 1; e odd). (iii) Hence for an **arbitrary** pair (d, m) with
4dm − 1 = pe and Λ_{d,m} ⊂ B_{p,∞} Eichler of level e:
**Type I at (d,e) ⟺ m has a divisor a equal (mod e) to the eigenvalue χ(v) of v on some level-e line**, and then
`(v − a)(v + a) = −ace` with `C ⊆ ker(v − a)`: v − a = ψ∘φ_C factors through the level isogeny, deg ψ = ac.
*Proof.* (ii) χ is a ring map, apply to u² = −d, uv + vu = 1, v² = −m; flipping the end at ℓ negates χ(v) at ℓ, and an
odd e with −m a unit has exactly 2^{ω(e)} roots. (iii) e | a + b ⟺ a² ≡ −m (mod e) (Lemma 1.1 of QUATERNION_ES);
then (v − a) kills the χ = a line, and nrd(v − a) = m + a² = a(a+b). ∎
**Prop 2 (Type II = an "involution level structure"; PROVED).** For a Type II tuple and x, y ∈ End E with Gram T'
(bsC_supersingular_transfer Thm 1), `M := 4cd`: `x² = −f ≡ 1`, `y² ≡ 1 (mod M)`, `(x + y)² = −Mce ≡ 0`, and
`k := xy + 1` has `k² = −4c²dp = −cMp`. So on E[M] (p ∤ M) x and y act as involutions whose sum is nilpotent, and E
carries the "spine" endomorphism k (E^{(p)} is d-isogenous-type to E). Conversely, given an involution pair (x₀, y₀)
mod M, every maximal order O contains x ≡ x₀ (mod M·O) with trd x = 0 (O⁰ → sl₂(ℤ/M) is onto: lift, then correct the
trace by M·z with trd z = −trd(x)/M), so `nrd x ≡ −1 (mod M)` **for every curve and every M, deterministically**.
What is *not* free is the exact equation `ff' − 1 = cMp` with d = M/4c (a single binary representation; DIFF_DEEP §2).

## Barrier screen
* **B2 (decisive).** Prop 1(ii): the Eichler structure realises *every* root of −m; the geometric orientation carries
  no constraint, and the remaining condition "m has a divisor ≡ that root" is QUATERNION_ES Prop 2.2 verbatim.
  Level-e special cycles with "moving level datum" = the moving modulus e (H-A). *Assessment:* Gross–Keating multiplicities at
  Eichler level are local densities at ℓ | e: functions of (T, level) that are the same for all orientations (the
  local normaliser of Λ_ℓ — Atkin–Lehner — permutes the 2^{ω(e)} characters, Atkin–Lehner), so they cannot separate "a | m" from "a ∤ m".
* **Prop 2** is the first place a ray condition (`nrd x ≡ −1 mod M`) is achieved deterministically on a supersingular
  curve; the cost is moved into an exactness condition (size layer). This is the "sign/genus easy, size hard" pattern of
  PARITY_FIXED_P in geometric form (B3).
* **T1**: the level structure exists equally at n = m² (no supersingular curve; at the composite level Diff decides).
* B1/B4/B6/Thm 9.1: not engaged (no covering, pointwise).

## Cheap numerics
None beyond identities (Props 1–2 are algebra; QUATERNION_ES §3.4 already shows admissible (d,e) with opposite ES
status). The deterministic lift of Prop 2 is sanity-checked in `scripts/review_dd_lift.py` (R176; the previously cited
`scripts/bsC_involution_lift.py` does not exist — R176 repair D8).

## Assessment
**Exact dictionary (PROVED), COLLAPSES to B2 for Type I; Type II is the live thread** — the ray condition is free on
one endomorphism, the obstruction becomes an exact binary representation problem. Promise 2 (as a test bed for
"congruence ↔ exactness" trade-off), taken to depth in DIFF_DEEP.md.
