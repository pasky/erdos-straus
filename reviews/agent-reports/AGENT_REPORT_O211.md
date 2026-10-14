# AGENT_REPORT_O211 — BRIDGE_WORLDS (spark relay Y3): bridging the (h+1)- and (h−1)-worlds

Branch `side-agent/bridge-worlds` (merged side-agent/torsion-firing first); deep file `BRIDGE_WORLDS.md`; 8 memos
`BRAINSTORM/y3_*.md` (indexed in BRAINSTORM/README.md); scripts `scripts/y3_*`. **ES is not proved, nor any infinite
case.** Outcome: a precise negative classification of bridges, one clean sub-conjecture (PM-II), and a refutation.

## SHARP:
1. **Three-tier bridge classification (BRIDGE_WORLDS Thm 2.1, PROVED, elementary).** For m | h + 1 (semi-primitive),
   anything that carries μ_m ⊂ T(F_h) into F_h (where −p lives) is one of: (a) a homomorphism → image ±1 (O207 Thm 3.1);
   (b) a symmetric algebraic function of a subgroup (cardinalities, ∏(1 − ζ) = c, Gauss-sum moduli and signs,
   uniform cyclotomic numbers, Gross–Koblitz Γ_h(1/m) ≡ j, Dickson/Chebyshev/cosecant identities) → the residue of a
   FIXED RATIONAL s(m): this is exactly the box −p ≡ c/j; (c) Frobenius-invariant functions of one ζ → ring maps
   O_{ℚ(ζ_m)⁺} → F_h (h splits completely in ℚ(ζ_m)⁺). ES Type II is the ℚ-rational section of (c).
2. **Tier (c) has a mute mechanism (Prop 6.1).** The units of ℚ(ζ_{4cd})⁺ reduce homomorphically into F_h^* — the
   same group as p (FF_MUTE-style), with large image (m = 8: index ≤ 2 for 75% of h < 10⁵). The unit-twisted Type II
   "𝔥 | p + 4c²d·ε" has large-coset firing sets; its gap to ES is ε ≡ 1 (mod 𝔥), i.e. the exponent-cap wall of (J)34.
   A spark agent could test whether this is a genuinely new provable cousin of ES (and whether anything transports).
3. **Semi-primitivity = "h imitates ∞"** (memo y3_frob_infinity): h ≡ −1 (mod m) ⟺ Frob_h = c_∞ in ℚ(ζ_m); O207's gcd = 2
   is |D_∞|. Type II on (c, d) ⟺ a sub-product of the prime factors of p + 4c²d has Artin symbol c_∞. For cd | 6 this is
   pure genus theory: the slice fails ⟺ some odd quadratic character mod 4cd is 1 on every prime factor (0 mismatches
   in 72 905 slice instances). Explains why every non-homomorphic bridge is archimedean.
4. **CONJECTURE PM-II (EVIDENCE):** every prime p ≥ 5 except 3361 has a prime-modulus Type II certificate. Exhaustive
   to 10⁷ (O207), [10⁸: see below]; full census of all certificates to 10⁶ (min N_II^pr = 5 on [10⁵, 10⁶]); only
   13, 193, 76441 have N_II^pr = 1; mean N_II^pr ≈ 0.3·log²p; stacked-QR adversaries to 1.3·10¹¹ still fire.

## Other results
* Uniform cyclotomy residue law (EVIDENCE): m²·(a,b)_m over F_{h²} ≡ 1, 1 − m or 1 − 3m (mod h) for m ∈
  {4,6,8,10,12,16,20,24}, h ≤ 199. Stickelberger: g(χ_{4cd}) = (−1)^j h.
* Scaling collapse (Prop 1.2, PROVED): weighted-homogeneous cyclotomic counts see p only via p mod F_h^{*e}.
* O207 spark 1 REFUTED/COLLAPSED (PROVED + EVIDENCE): the Type I dual Hasse window is exactly the g ∈ {1,3,5} family
  (g = 3, the greedy x = (p+3)/4 family, for p ≡ 1 mod 4); the trace-(1−p) curve never has CM by ℚ(√−d) (0/10 737).
  Type I overlap |Hom(μ_{f+p}, F_f^*)| = gcd(p+1, f−1); full overlap at level 4cd ⟺ p ≡ 3 (4) trivial case.
* Euclid–Schur: ES firing classes are exactly Schur–Murty "Euclidean" classes (a² ≡ 1); residue-only forcing of a
  prime factor ≡ −1 exists only for |(ℤ/m)^*| = 2 (trivial slice).
* Salié angle dictionary: Type II at prime h ⟺ a root ν of ν² ≡ −pd (mod h) sits exactly at (h+1)/(2j) (Planck scale).
* Mixed Gauss sums (χ∘N)·ψ decompose into torus character sums (checked); Weil-bounded (B3).

## Barrier screen summary
All eight memos COLLAPSE (B1/B2/B3/B4 as tabulated in BRIDGE_WORLDS §7); T1 control (odd squares) gave 0 throughout.

## Sparks (not pursued)
1. Tier (c) unit-twisted ES (Prop 6.1): find the Diophantine equation it is equivalent to (norm form
   p² + t·pX + N(ε)X², X = 4c²d) and whether it is provable (Chebotarev over ℚ(ζ_m)⁺ with large unit image).
2. Closed form for the residue law m²(a,b) ≡ {1, 1 − m, 1 − 3m} from Baumert–Mills–Ward (should be a two-line check).
3. FF analogue of "h imitates ∞": in Carlitz cyclotomy D_∞ = F_q^*; does the FF ES firing condition become
   "h ≡ unit (mod m)", and does this explain the small-q accidents of FUNCTIONFIELD_ES?
4. Composite-modulus Type II as a zero-sum problem with target c_∞ in (ℤ/4cd)^* beyond 2-groups (cf. W15).
