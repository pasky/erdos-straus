# z39_serre_stark_support — T1 is metaplectic, 105 is not: supports of weight-½ forms (O269)

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
2. The T1 part of the failure set *is* metaplectic: {m² : m odd} = supp(θ(z) − θ(4z)), weight ½, level 16.
3. **105 is not metaplectic** (CONDITIONAL on SQ₅ for the full statement; PROVED for period M ≤ 96): if the
   five-slice failure set Z = {n ≡ 1 (4) : λ(n) > 3} (DEDEKIND §9.1, boundary certificates included; the interior-only
   set {N₋ = 0} differs: its non-square zeros ≤ 10⁶ are 5 and 105) were exactly the support (over all n) of a
   weight-½ form g, then 105 ∈ supp g;
   the coefficient m ↦ a_g(105m²) = Σ_{k | m, k∈K} f_k(m/k) (contributions of the classes 105k²·□) is periodic in
   m, say with period M, and non-zero at m = 1, so 105m² ∈ supp g for all m ≡ 1 (mod M). M odd: 105(1+M)² is even,
   not in Z. M even ≤ 96: m = 1 + M ≤ 97 odd, 105m² ≤ 987945 < 10⁶, and the census says 105m² ∉ Z. Under SQ₅ every M
   is excluded. The same holds after adding to Z finitely many further non-square points, provided 105 stays.
   This is an exact-support obstruction only; weight-½ forms whose support merely contains 105 exist.
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
PROVED (classical input) + CONDITIONAL (SQ₅) for item 3. Sharpest available answer to "is the ES failure set
metaplectic": the square part is (θ), anything else is not, unless it comes in full periodic square classes. Promise as a route: 0; as steering: "no weight-½ object can certify non-square
failures".
