# AGENT_REPORT_O211 — BRIDGE_WORLDS (spark relay Y3): bridging the (h+1)- and (h−1)-worlds

Branch `side-agent/bridge-worlds` (merged side-agent/torsion-firing first); deep file `BRIDGE_WORLDS.md`; 8 memos
`BRAINSTORM/y3_*.md` (indexed in BRAINSTORM/README.md); scripts `scripts/y3_*`. **ES is not proved, nor any infinite
case.** Outcome: a precise negative classification of bridges, one clean sub-conjecture (PM-II), and a refutation.

## SHARP:
1. **Three tiers of bridges (BRIDGE_WORLDS Thm 2.1, PROVED, elementary; scope = these tiers only).** For m | h + 1
   (semi-primitive), a rule carrying μ_m ⊂ T(F_h) into F_h (where −p lives) that is (a) a homomorphism has image ±1
   (O207 Thm 3.1); (b) a fixed symmetric rational expression in a subgroup (cardinalities, ∏(1 − ζ) = c, cosecant
   sums) gives the residue of a FIXED RATIONAL (for Type II: the box −p ≡ c/j); (c) a Frobenius-invariant expression in
   one ζ gives ρ_𝔥(α), α ∈ ℚ(ζ_m)⁺ (h splits completely there). Separately checked: pure Gauss sums (sign (−1)^j),
   uniform cyclotomic numbers (EVIDENCE: m²(a,b) ≡ 1, 1 − m, 1 − 3m mod h), Γ_h (argument 1/m ≡ j), Salié angles —
   all end at the box, a Planck-scale hit, or a Weil-bounded sum. "Every useful bridge is archimedean" is Assessment.
2. **Semi-primitivity = "h imitates ∞"** (memo y3_frob_infinity, PROVED dictionary): h ≡ −1 (mod m) ⟺ Frob_h = c_∞ in
   ℚ(ζ_m); O207's gcd = 2 is |D_∞|. Type II on (c, d) ⟺ a sub-product of the prime factors of p + 4c²d has Artin
   symbol c_∞. For cd | 6 this is genus theory: the slice fails ⟺ some odd quadratic character mod 4cd is 1 on every
   prime factor (0 mismatches in 86 310 prime slice instances p < 10⁵). Folklore-level, but a clean dictionary.
3. **CONJECTURE PM-II (EVIDENCE):** every prime p ≥ 5 except 3361 has a prime-modulus Type II certificate. Exhaustive
   to 10⁷ (O207) [10⁸ run: see "10⁸ status" below]; full census of all certificates to 10⁶ (min N_II^pr = 5 on
   [10⁵, 10⁶]); only 13, 193, 76441 have N_II^pr = 1; mean N_II^pr ≈ 0.3·log²p; stacked-QR adversaries up to 1.3·10¹¹
   still have ≥ 14 prime-firing slices with cd ≤ 200.
4. **Tier-(c) unit twists erase the box, leaving exactly the genus layer (Prop 6.1/6.2, PROVED + EVIDENCE).** Units of
   ℚ(ζ_{4cd})⁺ reduce into F_h^* (p's group). With ALL units the twist is trivial (ε = −1 is signed ES: 3 | p ± 4).
   With totally positive units of ℚ(√2) (E⁺ = ⟨(1+√2)²⟩): odd squares NEVER fire (PROVED: (−d/h) = −1 whenever
   h ≡ −1 mod 4d), and a prime p fires at every "good" h ≡ 7 (8) with (p/h) = −1 (good = 1 + √2 has index ≤ 2 mod h;
   75% of h). Every prime < 10⁵ fires at some h < 2000 (half at h = 7). So the E⁺-twisted Type II is a T1-keeping,
   Artin-type (V_φ-like) cousin of ES, and the gap to ES is exactly the box (ρ(ε) = 1). Spark: unconditional proof via
   higher-rank units of ℚ(ζ_m)⁺ (Gupta–Murty/Heath-Brown), and whether anything transports back.

## Other results
* Uniform cyclotomy residue law (EVIDENCE): m²·(a,b)_m over F_{h²} ≡ 1, 1 − m or 1 − 3m (mod h) for m ∈
  {4,6,8,10,12,16,20,24}, h ≤ 199. Stickelberger: g(χ_{4cd}) = (−1)^j h.
* Scaling collapse (Prop 1.2, PROVED): weighted-homogeneous cyclotomic counts see p only via p mod F_h^{*e}.
* O207 spark 1 COLLAPSES (PROVED + EVIDENCE): the Type I dual Hasse window consists of the g ∈ {1,3,5} certificates
  (p ≥ 17); for p ≡ 1 mod 4 that is g = 3 with f prime, a sub-family of the greedy x = (p+3)/4 family; the CM-by-ℚ(√−d)
  suggestion holds in none of 10 737 window certificates. Type I overlap |Hom(μ_{f+p}, F_f^*)| = gcd(p+1, f−1); full
  overlap at level 4cd ⟹ p ≡ 3 (4) (trivial case); partial overlaps exist for p ≡ 1 (4) on finitely many slices.
* Euclid–Schur: the ES class −1 is one of the Schur–Murty "Euclidean" classes (a² ≡ 1); forcing a prime factor ≡ −1
  of a single integer from its residue exists only for |(ℤ/m)^*| = 2 (trivial slice); forcing via auxiliary primes is B1.
* Salié angle dictionary: Type II at prime h ⟺ a root ν of ν² ≡ −pd (mod h) sits exactly at (h+1)/(2j) (Planck scale).
* Mixed Gauss sums (χ∘N)·ψ decompose into torus character sums (checked); Weil-bounded (B3).

## Self-review (deep reviewer, R-O211)
1 FATAL (universal "no algebraic bridge" verdict overreached: rescoped to the three tiers, Assessment otherwise),
6 MAJOR (Euclid–Schur E3 false → withdrawn as remark; unit-twist variant trivial via ε = −1 → caveat; Gross–Koblitz
sign and value/argument confusion → fixed; Box(k) can be a subgroup (h = 7) → withdrawn; Type I overlap overstated →
fixed; Prop G integrality → "regular at 𝔥"), minors (Type I window proof completed via c ≤ 2p/3 ⇒ g < 13, f-prime
condition kept; genus criterion hypothesis and counts fixed; label wording). All repaired in place ("R-O211 repair").

## Barrier screen summary
All eight memos COLLAPSE (B1/B2/B3/B4 as tabulated in BRIDGE_WORLDS §7); T1 control (odd squares) gave 0 throughout.

## Sparks (not pursued)
1. Tier (c) unit-twisted ES (Prop 6.1): find the Diophantine equation it is equivalent to (norm form
   p² + t·pX + N(ε)X², X = 4c²d) and whether it is provable (Chebotarev over ℚ(ζ_m)⁺ with large unit image).
2. Closed form for the residue law m²(a,b) ≡ {1, 1 − m, 1 − 3m} from Baumert–Mills–Ward (should be a two-line check).
3. FF analogue of "h imitates ∞": in Carlitz cyclotomy D_∞ = F_q^*; does the FF ES firing condition become
   "h ≡ unit (mod m)", and does this explain the small-q accidents of FUNCTIONFIELD_ES?
4. Composite-modulus Type II as a zero-sum problem with target c_∞ in (ℤ/4cd)^* beyond 2-groups (cf. W15).
