# z39_serre_stark_support — supports of holomorphic weight-½ forms: T1's squares are one, the five-slice failure set is not (O269)

**ES is not solved here.** Labels as in DISCOVERIES.md. (Self-review repairs applied: failure-set definition,
period parity, support vs zero set.)

## Idea
The brief asks for a half-integral weight object "whose support is the ES set and whose vanishing at squares IS
T1". Weight ½ is rigid: Serre–Stark classify all holomorphic weight-½ forms. Use that to decide exactly which
ES-type sets can be supports (or zero sets) of weight-½ objects.

## Statement
**Prop S (PROVED, from Serre–Stark).** Every holomorphic modular form of weight ½ on Γ₁(4N) is a finite linear
combination of θ_{ψ,t}(z) = Σ_{m∈ℤ} ψ(m)q^{tm²} (ψ even, t ≥ 1). Hence its coefficient support S satisfies:
S ⊆ ⋃_{t∈F} t·□ (F finite) and S ∩ t·□ = {tm² : m ∈ 𝒞_t} with 𝒞_t periodic in m (a union of classes mod some M).
Consequences:
1. No weight-½ holomorphic form has support equal to the ES-five success set {n ≡ 1 (4) : N₋(n) > 0}, nor to any
   set of positive lower density (|S ∩ [1, X]| ≪ X^{1/2}).
2. The T1 part of the failure set is a holomorphic weight-½ support: {m² : m odd} = supp(θ(z) − θ(4z)), weight ½, level 16.
3. **Z is not the exact support of any holomorphic weight-½ form — PROVED unconditionally (R280 repair, D6).**
   Z = {n ≡ 1 (4) : λ(n) > 3} (DEDEKIND §9.1, boundary certificates included; R280 census: Z \ □ = {105} to 10⁸; the
   interior-only set {N₋ = 0} has non-square zeros 5 and 105). If supp g = Z, then m ↦ a_g(105m²) is periodic (period
   M) and non-zero at m = 1. M odd: 105(1+M)² is even, not in Z. M even: pick a prime ℓ ≡ 3 (4), (ℓ/105) = −1, ℓ ∤ M
   (11, 19, 31, 43, …); then (−105/ℓ) = 1, and by CRT some odd m ≡ 1 (M) has ℓ | 105m² + 1 with (ℓ/105m²) = −1, a
   length-2 certificate, so 105m² ∉ Z: contradiction. Same for Z ∪ F (F finite, 105 ∈ Z ∪ F). The obstruction is
   elementary (Z misses whole residue classes of m on 105·□) and exact-support only (θ_{1,105} contains 105).
   (Compare bsB_theta_multiplier: Shimura zero-propagation fails for W at 105k² — a statement about eigenforms;
   Prop S is about *all* weight-½ forms and about supports.)
4. Weight ≥ 3/2: no support restriction from this argument; coefficients of non-unary forms have power size; (J)39
   Thm 2.2 already excludes N₋ itself. (Zagier's ℋ is mock — modular only after completion — and H(n) = 0 for
   n ≡ 1, 2 (4), so it is not a full-support example.)

## Literature
J.-P. Serre, H. Stark, "Modular forms of weight 1/2", LNM 627 (1977) 27–67; Shimura, Ann. Math. 97 (1973);
D. Zagier, C. R. Acad. Sci. 281 (1975) (ℋ, shadow θ).

## Barrier screen
T1/B5: exactly reproduced (item 2). B3: item 1 is a density form of B3 (weight-½ supports are √X-thin, ES sets are
X-fat). B2: not engaged — the statement is about zero sets, not mechanisms. B1/B4/B6/Thm 9.1/Prop 10.3: n/a.

## Cheap numerics
None needed beyond DEDEKIND §9.1 (`scripts/dk_vanish5.py 1000000`, existing).

## Assessment
PROVED (classical input), item 3 unconditional (R280). Scope: holomorphic weight-½ forms only (R280 D7) — mock,
weakly holomorphic and harmonic weight-½ objects have positive-density supports and are not covered. Answer to "is the ES failure set a holomorphic weight-½ support": its
square part is (θ); the whole set Z is not. Promise as a route: 0; as steering: "no holomorphic weight-½ form has Z
as exact support".
