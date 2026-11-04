# Z56_K4TRY — tryhard (unprimed twin) on P(4,15): primes p ≡ 1 (8) with p + 4 ∈ S and 4p + 1 ∈ S

**ES is OPEN.** Nothing here proves or disproves it. Lane K4TRY (wave z56). Scripts `scripts/z56_k4try_*`, data
`data/z56/k4try/`. Internally reviewed only (review log §8).

Notation (as `Z55_P415.md`): 𝒬 = {primes ≡ 3 (mod 4)}, 𝒬(z) = ∏_{q∈𝒬, q<z} q; S = {n ≥ 1 : every prime factor
≡ 1 (mod 4)}; N₁ = p + 4, N₂ = 4p + 1; χ = χ₋₄; r(n) = #{(a,b) ∈ ℤ² : a² + b² = n} = 4Σ_{d|n}χ(d);
r*(n) = #{(a,b) : a² + b² = n, gcd(a,b) = 1}; for odd n, r*(n) = 4·2^{ω(n)}·1_S(n). W(z) = ∏_{q∈𝒬,q<z}(1 − 1/q)
≍ (log z)^{−1/2}; F, f the semi-linear (κ = 1/2, β = 1) beta-sieve functions as in P415; f_lin the linear (κ = 1,
β = 2) lower function. P(4,15) := "infinitely many primes p ≡ 1 (8) with N₁, N₂ ∈ S" (= K(4) by HCKILL Lemma 1.1).
Only `Z55_P415.md`, `Z54_HCKILL.md` (Theorems U, E, Q, Remark 1.3) were read, per the lane brief.

## 0. Verdict: **not proved**; one unconditional theorem for generic shifts, one new conditional route (model only)

1. **The target contains an open problem of Friedlander–Iwaniec (first-hand check, §1).** By HCKILL Remark 1.3,
   #{p : N₁, N₂ ∈ S} is the primitive-point count of the determinant-15 shell at height 16p + 34, the analogue of
   Friedlander–Iwaniec's *Hyperbolic prime number theorem* (Acta Math. 202 (2009)): primes p = ‖γ‖², γ ∈ SL₂(ℤ), i.e.
   p ± 2 both sums of two squares. I verified from the published abstracts of Bourgain–Kontorovich (C. R. Acad. Sci.
   Paris 348 (2010) 947–950) and Sedunova (arXiv:2609.28200, Sept 2026) that FI's *upper* bound is unconditional while
   the *lower* bound (infinitude) rests on Elliott–Halberstam; the current unconditional state of the det-1 problem is
   "square-free distances" (asymptotic) and "distances with ≤ 7 prime factors" (Sedunova). So P(4,15) is at least as
   hard as an open FI problem; every route below either assumes a level of distribution or changes the problem.
2. **Theorem AA (PROVED, unconditional; generic shifts).** For every ε > 0 there are η, c > 0 such that, with
   H = x^{1−η}, all but at most εH² *admissible* pairs (a, b) ∈ [1, H]² (a ≡ 0 (4), b ≡ 1 (4), 3 | ab(a − b)) have
   #{p ≤ x : p ≡ 1 (8), p + a ∈ S, 4p + b ∈ S} ≥ c·x/(log x)² (§3). It is Theorem E's proof with Barban–Davenport–
   Halberstam in place of EH: the *only* obstruction to P(4,15) is the level of distribution of primes in the
   CRT-coherent residue classes of the one pair (a, b) = (4, 1); for a generic pair the same sieve closes. Not a step
   toward (4, 1) itself.
3. **Hybrid route (Assessment; model numbers, not a theorem).** Weight one shift exactly by r*(4p + 1) (cost: level
   1/2 by the hyperbola trick, no sieve loss) and sift the other, p + 4, by the semi-linear sieve beyond x^{1/4} with
   Iwaniec switching. In P415's model this needs total level **0.908** (pen 1) / **0.958** (pen 2.35) — versus
   0.976–0.996 for the product sieve (P415 §2(b)) and ≈ 1.22 for the vector sieve (§2(a)) — provided the hypothesis
   also covers the switched sums (§2). With the switched sums bounded without any primes-in-progressions input
   (Poisson in ℤ[i] + Weil; route only) the loss factor is too large and the model level returns to 0.989–0.995.
   The rigorous version with unspecified constants has exactly Theorem E's strength (EH(1 − η₁)); the *missing
   lemma* is an r*-weighted switched bound uniform for q ≈ √x (Lemma S, §2.3, **not proved**).
4. **Direct-attack notes (§4, PROVED identities; negative).** Polynomial two-parameter confinement family on the
   det-15 quadric: p(m, n) = (n² − m² + 4)² + m² − 4 has p + 4 = (n² − m² + 4)² + m², 4p + 1 = (2n² − 2m² + 7)² + 4n²,
   and p ≡ 1 (8) on m ≡ 2 (4), n odd — but it is thinner than Friedlander–Iwaniec's a² + b⁴ (≍ √x·log x points
   below x), so no prime-value theorem applies; every polynomial family on the quadric is a union of lines
   (Bunyakovsky slices, Theorem Q being the line (u, s) = (−1, 2)). A tempting "automatic confinement" for
   SL₂(ℤ)-norms is false (counterexample recorded) — a warning for future lanes.
5. **EVIDENCE (§5).** Census to 2·10⁸: the empirical switched mass T(θ)/A(θ) (share of survivors of 𝒬-sifting to
   x^θ that have exactly two 𝒬-factors) agrees with the model's B(θ)/F(1/θ) to within 5 % for θ ∈ [0.25, 0.45],
   supporting the model ledgers of P415 and §2. The r*-mean on the target set is ≈ 2.13 (in units of 8).

**Bottom line (Assessment).** No unconditional progress on (4, 1) is possible with the tools used here (confirmed
state of the art for the det-1 twin). The one new rigorous statement is that generic shift pairs are fine (Theorem
AA). The hybrid route lowers the *model* level requirement from ≈ 0.98 to ≈ 0.91 but not the rigorous one.

## 1. Setting; the det-1 twin and what is known about it (first-hand)

HCKILL Remark 1.3: (x, y, u, v) ↦ M = (2x − u, −(2y + v); 2y − v, 2x + u) is a bijection from {x² + y² = p + 4,
u² + v² = 4p + 1} onto the integral points of det M = 15 with ‖M‖² = 16p + 34 and the parity P + Q ≡ R + T ≡ 0 (4).
Hence Σ_p r(p + 4)r(4p + 1) is a det-15 "hyperbolic prime number theorem" and P(4,15) its primitive-point version.

**What FI 2009 proves (CHECKED from secondary sources, not from the paper).** Bourgain–Kontorovich (2010), abstract:
"Under the Elliott–Halberstam conjecture, they [FI] proved the existence of such [primes p = ‖γ‖², γ ∈ SL₂(ℤ)], as well
as a formula for their count, off by a constant from the conjectured asymptotic." Sedunova (arXiv:2609.28200):
"the upper bound is unconditional, while the lower one rests on a strong hypothesis concerning the distribution of
primes in arithmetic progressions"; unconditionally she proves an asymptotic for square-free distances and ≫ x/log x
distances with ≤ 7 prime factors, and ≤ N prime factors under level θ for r(n − 2)r(n + 2) in progressions (7 ↔ θ =
1/6). This matches P415/HCKILL's reading ("lower bound only under A(θ)"). Consequence: the r-weighted det-15 lower
bound Σ_{p≤x} r(p + 4)r(4p + 1) ≫ x is a sibling of an open problem; the S-refinement is harder still (parity on both
shifts). Almost-prime versions are already maximal for our problem (P415 §4: 720k² + 1 = P₂ with both shifts in S), so
Sedunova's P₇-type route adds nothing here.

## 2. The hybrid route: r* on one shift, semi-linear sieve + switching on the other (Assessment)

### 2.1 Identity and main term (PROVED, elementary)

For odd n ≡ 1 (mod 4): χ(n/d) = χ(n)χ(d) = χ(d), so pairing d with n/d,
  r(n) = 8 Σ_{d | n, d < √n} χ(d) + 4·[n = □]·χ(√n).   (2.1)
r*(n) = Σ_{g² | n, g odd} μ(g) r(n/g²) (Möbius over the content of (a, b)); for n ∈ S, r*(n) = 4·2^{ω(n)} ≥ 8, and
r*(n) = 0 for n ∉ S. So for p ≡ 1 (8),
  𝒮(x; z) := Σ_{p ≤ x, p ≡ 1 (8), (p + 4, 𝒬(z)) = 1} r*(4p + 1)/8 ≤ #{p ≤ x : p ≡ 1 (8), (p + 4, 𝒬(z)) = 1, 4p + 1 ∈ S}·2^{ω(4p+1)−1},
and (parity reduction, P415 Step 1, z = x^{θ_z} with θ_z > 1/4): every p counted has p + 4 ∈ S or p + 4 = mqq′ with
m ∈ S, q ≤ q′ in 𝒬, q ≥ z. Hence
  #{p ≤ x : p ≡ 1 (8), p + 4 ∈ S, 4p + 1 ∈ S} ≥ 𝒮(x; z)/max 2^{ω−1} … — more usefully, with the weight kept:
  Σ_{p: N₁, N₂ ∈ S} r*(N₂)/8 ≥ 𝒮(x; z) − T₁,  T₁ := Σ_{p ≤ x, p ≡ 1 (8), p+4 = mqq′ as above} r*(4p + 1)/8.   (2.2)
Every term of the left side is ≥ 1, so a positive lower bound for 𝒮 − T₁ gives P(4,15) (with ≫ x/(log x)^{3/2}
weighted mass; the unweighted count is ≫ x/(log x)^{3/2}/max 2^{ω} ≥ x^{1−ε}, or ≫ x/(log x)² after the standard
removal of p with 2^{ω(4p+1)} > (log x)^{1/2}·C, which has weighted mass o(𝒮) by Cauchy–Schwarz against Σ r*² ≪ x log x
— this last step is routine but not written out).

**Main term (CONDITIONAL on 𝒟 below).** Expanding r* by Möbius (g ≤ x^δ; the tail Σ_{g > x^δ} #{p : g² | 4p + 1}·
2^{ω} ≪ x^{1−δ+ε} is negligible), r by (2.1), and 1_{(p+4, 𝒬(z))=1} by the semi-linear lower sieve of level x^{θ_e},
𝒮(x; z) is a sum of primes in progressions to moduli 8g²·d·e with g ≤ x^δ, d ≤ 2√x (χ-weighted, from (2.1)) and e | 𝒬(z),
e ≤ x^{θ_e} (sieve weights), in the residue class c ≡ 1 (8), c ≡ −4 (e), 4c + 1 ≡ 0 (g²d). Define

**Hypothesis 𝒟(θ_e).** For every A > 0: Σ_{g ≤ x^δ} Σ_{e ≤ x^{θ_e}, e | 𝒬(z)} 3^{ω(e)} |Σ_{d ≤ 2√x, (d, 2ge) = 1} χ(d)·
(π(x; 8g²de, c) − li(x)/φ(8g²de))| ≪_A x(log x)^{−A}, c = c(g, d, e) as above.

𝒟(θ_e) follows from EH(1/2 + θ_e + 2δ + ε) (all residues) by the triangle inequality and Cauchy–Schwarz; its extra
structure is that the long variable d carries only the periodic weight χ(d) (residue classes mod 4) — the shape in
which unconditional "level 1 − ε" results exist for a *fixed* residue (Fouvry; BFI I), but **not** with the present
CRT two-shift residue (−4 mod e, −4⁻¹ mod d); the literature check (MathOverflow 513733, BFI I Thm 10 as quoted there)
confirms that even uniformity in a single large residue is not available as a black box. So 𝒟 is a weakening of EH
in form, not a known theorem in any range θ_e > 0.

Under 𝒟(θ_e), the semi-linear lower sieve (Nath–Xie Prop. 3.10 with one component, i.e. the standard κ = 1/2 beta
sieve) gives, with s = θ_e/θ_z > 1 and 𝔐 := lim (1/X) Σ_{p ≡ 1 (8)} r*(4p + 1)/8 (a convergent Euler product, positive),
  𝒮(x; z) ≥ (𝔐′ + o(1)) X W(z) f(s),  X = li(x)/4, 𝔐′ = 𝔐·(local correction at ℓ = 3: 3 | p + 4 ⟹ 3 | 4p + 1 ⟹ r* = 0,
so sifting by 3 is free; and at ℓ ∈ 𝒬, ℓ ≥ 7, the conditional mean of r*(4p+1) given ℓ | p + 4 is 𝔐(1 + O(1/ℓ)), which
keeps the κ = 1/2 product condition).   (2.3)
I did not write out the evaluation of the local densities g(ℓ) for the weighted sequence; it is the same computation
as Theorem U Step 2 with the weight's Euler factor inserted, and is **not** needed for the model numbers below.

### 2.2 Switched term and the model ledger

T₁ is Theorem U's Step 3 sum with the weight r*(4mqq′ − 15)/8 on the switched variable q′ ∈ [q, Y], Y = (x + 4)/(mq).
In P415's model (units X𝔐W(z)): main = f(s); T₁ = pen·(2/a)·B(θ_z), B(θ) = F(1/θ) − F(1)√θ (Buchstab mass of the
two-𝒬-factor configurations, checked numerically in P415 and again here, §5), 2/a = loss for detecting p = mqq′ − 4
prime by an upper linear sieve at level x^a, pen ∈ {1, 2.35} as in P415. The r*-weight is evaluated exactly (hyperbola,
cost 1/2), so a = λ_sw − 1/2 where λ_sw is the level available for the switched sums; with the hypothesis covering
them, λ_sw = 1/2 + θ_e, a = θ_e. Total level L = 1/2 + θ_e. `scripts/z56_k4try_hybrid.py` (reusing P415's F, f, B)
minimises L subject to f(s) > T₁ over θ_z ∈ (1/4, 1/2) (`data/z56/k4try/hybrid_model.txt`):

| switched input | pen | minimal sufficient L | at θ_z, s |
|---|---|---|---|
| same level as main (λ_sw = L) | 1 | **0.908** | 0.365, 1.119 |
| same level as main | 2.35 | **0.958** | 0.438, 1.047 |
| no progression input ("gauss": both k and p sieved at relative level 1/3, loss 36) | 1 | 0.989 | 0.483, 1.012 |
| idem | 2.35 | 0.995 | 0.493, 1.005 |

For comparison (P415 §2, same model and pen): product linear sieve 0.996 (BV switching) / 0.976 (same-level
switching); vector sieve ≈ 1.22. **Reading (Assessment):** replacing one sieve by the exact r*-weight saves
≈ 0.07–0.09 in the model level when the switched sums get the same level, and nothing when they do not. These are
sufficient levels of one implementation in a model, not barriers and not audited constants.

### 2.3 Why the rigorous version is no stronger than Theorem E; the missing lemma

Rigorously (unspecified sieve constants, as in Theorems U/E) the only mechanism is "loss → 0 faster than main":
main ≍ √(s − 1), T₁ ≤ K₂(1 − 2θ_z)^{3/2}. With 1 − 2θ_z = η and s − 1 = t this needs t ≫ η³ and gives
L = 1/2 + (1 + t)(1 − η)/2 = 1 − η/2 + O(η³) < 1: i.e. 𝒟(1/2 − η/2 + O(η³)) ⟹ P(4,15) — the same shape as Theorem E
(EH(1 − η₀)), since 𝒟(1/2 − η′) ⟸ EH(1 − η′ + ε). No rigorous gain.

**Lemma S (NOT PROVED; the obstacle).** Uniformly for m ∈ S, m ≤ x^{2η}, q ∈ 𝒬, z ≤ q ≤ √x, with Y = (x+4)/(mq):
  Σ_{k ≤ Y, k prime, mqk − 4 prime ≡ 1 (8)} r*(4mqk − 15) ≪ Y·h(m)/(log x)²   (h(m) = ∏_{ℓ|m}(1 + O(1/ℓ))).
Theorem E's Step 4 (sift the *integers* k by ℓ < w = x^{1/100}; no progression input) handles the unweighted count.
With the weight, r*(n) ≤ 8Σ_{d | n, d ≤ √n} μ²(d)1_S(d) and the hyperbola divisor d runs up to 2√x, while the interval
of k has length Y, which is as small as ≈ √x when mq ≈ √x — exactly the range z ≤ q ≤ √x that carries the whole
switched mass when θ_z → 1/2. For d > Y/w² the progression k ≡ c_d (d) has O(1) elements and the sieve on k cannot be
applied; the trivial bound is Σ_{d ∈ [Y/w², 2√x]} O(1) ≍ √x, which loses (log x)^{5/2} against the target. Route to a
proof (sketch only): count α ∈ ℤ[i] with N(α) = 4mqk − 15 directly — Gaussian integers in a disk of radius ≈ 2√x on the
conic N(α) ≡ −15 (mod 4mq) with the sieve conditions on k = (N(α) + 15)/(4mq) imposed as further conic conditions mod
ℓ < w; Poisson summation in ℤ[i] plus the Weil/Kloosterman bound |Σ_{N(c) ≡ a (ℓ)} e(Tr(ξc̄)/ℓ)| ≤ 2√ℓ + 1 (split ℓ:
hyperbola, Kloosterman sum; inert ℓ: norm-one torus, Hasse–Davenport reduces it to a Kloosterman sum) gives main +
O(M^{1/2+ε}) per modulus M = 4mq·e, hence an upper-bound sieve of level e ≤ x^{1/6} relative to Y ≈ √x — enough for an
absolute constant K₂, but not written out here (prime-power moduli from m, gcd terms, and uniformity in m, q all need
care). If Lemma S holds, Theorem H (𝒟(1/2 − η₁) ⟹ P(4,15)) follows by Theorem E's Step 5 verbatim.

## 3. Theorem AA: generic shift pairs (PROVED, unconditional)

**Theorem AA (PROVED relative to: Barban–Davenport–Halberstam (Davenport, *Multiplicative Number Theory*, Ch. 29,
ψ-version Σ_{q≤Q}Σ_{a (q)*}|ψ(x; q, a) − x/φ(q)|² ≪ x²(log x)^{−A} for Q ≤ x(log x)^{−A−1}); the linear beta sieve lower
bound and Ford's upper-bound sieve exactly as cited in HCKILL Theorem E Steps 2 and 4).** Call (a, b) *admissible* if
a ≡ 0 (mod 4), b ≡ 1 (mod 4) and 3 | ab(a − b). For every ε ∈ (0, 1) there exist η = η(ε) ∈ (0, 1/10], c = c(ε) > 0 and
x₀(ε) such that for x ≥ x₀ and H := x^{1−η}, all but at most εH² admissible pairs (a, b) ∈ [1, H]² satisfy
  #{p ≤ x : p ≡ 1 (mod 8), p + a ∈ S, 4p + b ∈ S} ≥ c·x/(log x)².
(The pair (4, 1) is admissible. Non-admissible pairs with 3 ∤ ab(a − b) have no such p > 3 at all: p ≡ 1 (3) forces
3 | 4p + b or p ≡ 2 (3) forces 3 | p + a.)

*Proof.* Fix η ∈ (0, 1/10] (chosen in Step 5), z = x^{1/2−η}, D = x^{1−η}/8, w = x^{1/100}, X = li(x)/4,
E(x; q, c) := π(x; q, c) − li(x)/φ(q).

*Step 1 (sieve setup, one pair).* 𝒜 = {(p + a)(4p + b) : p ≤ x, p ≡ 1 (8)}, sifted by ℓ ∈ 𝒬, ℓ < z. For squarefree
d | 𝒬(z) let R(d) = {β mod d : (β + a)(4β + b) ≡ 0 (d), (β, d) = 1}, ν(d) = |R(d)|, multiplicative with ν(ℓ) ≤ 2 and
ν(3) ≤ 1 by admissibility (the roots −a, −b·4⁻¹ ≡ −b mod 3 coincide or one is 0). Then
  |𝒜_d| = Σ_{β ∈ R(d)} π(x; 8d, c_β) + O(ω(d)) = g(d)X + r_d,  g(d) = ν(d)/φ(d),  |r_d| ≤ Σ_{β∈R(d)}|E(x; 8d, c_β)| + O(ω(d)),
where c_β ≡ 1 (8), ≡ β (d) (φ(8d) = 4φ(d), d odd; the O(ω(d)) counts primes p | d). Since 0 ≤ g(ℓ) ≤ 2/(ℓ − 1) ≤ 1/2
for ℓ ≥ 5 and g(3) ≤ 1/2, the one-sided linear-sieve axiom ∏_{w′≤ℓ<z}(1 − g(ℓ))⁻¹ ≤ ∏_{w′≤ℓ<z, ℓ∈𝒬}(1 − 2/(ℓ−1))⁻¹ =
(log z/log w′)(1 + K/log w′) holds with K absolute (Mertens in the progression 3 mod 4), uniformly in (a, b).

*Step 2 (lower bound).* The linear beta sieve (as in Theorem E Step 2; its o(1) depends only on κ, K, hence is uniform
in (a, b)) gives, with s = log D/log z = (1 − η)/(1/2 − η) + o(1) ≥ 2 + 2η,
  S(𝒜, 𝒬, z) ≥ X V(z)(f_lin(s) − o(1)) − R_{a,b},  R_{a,b} := Σ_{d<D, d|𝒬(z)} 3^{ω(d)}|r_d|,
V(z) = ∏_{ℓ∈𝒬,ℓ<z}(1 − g(ℓ)) ≥ (1/2)∏_{ℓ∈𝒬, 7≤ℓ<z}(1 − 2/(ℓ−1)) ≍ 1/log x, f_lin(s) ≥ (2e^γ/3)η. So
  S(𝒜, 𝒬, z) ≥ c₁η·x/(log x)² − R_{a,b}  (x ≥ x₀(η)), c₁ absolute.   (3.1)

*Step 2′ (the remainder on average over (a, b); the only place BDH enters).* Claim: for every B > 0,
  Σ_{(a,b) ∈ [1,H]²} R_{a,b} ≪_B H² x (log x)^{−B}  (x ≥ x₀(B, η)).   (3.2)
The O(ω(d)) terms contribute ≪ H² Σ_{d<D} 3^{ω(d)}ω(d) ≪ H² x^{1−η}(log x)³. For the main terms: each β ∈ R(d)
corresponds to a factorisation d = d₁d₂ with β ≡ −a (d₁), β ≡ −b·4⁻¹ (d₂) (take d₁ = ∏{ℓ | d : ℓ | β + a}; primes
dividing both β + a and 4β + b divide 4a − b and give the same root either way), so Σ_{β∈R(d)}|E(x; 8d, c_β)| ≤
Σ_{d₁d₂=d}|E(x; 8d, c(d₁, d₂; a, b))| with c ≡ 1 (8), ≡ −a (d₁), ≡ −b·4⁻¹ (d₂) (terms with (c, 8d) > 1 absent). As a runs
over [1, H] ∩ 4ℤ and b over [1, H] ∩ (1 + 4ℤ), the pair (a mod d₁, b mod d₂) takes each value at most
(H/(4d₁) + 1)(H/(4d₂) + 1) ≤ H²/(16d) + H times (d odd, H ≥ 2), and by CRT the class c mod 8d runs over the classes
≡ 1 (8), each once. Hence
  Σ_{a,b} Σ_{β∈R(d)} |E(x; 8d, c_β)| ≤ τ(d)(H²/(16d) + H)·𝔈(8d),  𝔈(q) := Σ_{c (q)*}|E(x; q, c)| ≤ φ(q)^{1/2}𝔈₂(q)^{1/2},
𝔈₂(q) := Σ_{c (q)*}|E(x; q, c)|². By Cauchy–Schwarz over d,
  Σ_{d<D} 3^{ω(d)}τ(d)(H²/(16d) + H)𝔈(8d) ≤ [H²(Σ_d 9^{ω(d)}τ(d)²·8/d)^{1/2} + H(Σ_{d<D} 9^{ω(d)}τ(d)²·8d)^{1/2}]·(Σ_{q≤8D}𝔈₂(q))^{1/2}
  ≪ (H² + HD)(log x)^{C}·(Σ_{q≤8D}𝔈₂(q))^{1/2} ≪ H²(log x)^{C}(Σ_{q≤8D}𝔈₂(q))^{1/2}  (D ≤ H).
BDH for ψ at height t and the partial summation E_π(x; q, c) = E_ψ(x; q, c)/log x + ∫₂^x E_ψ(t; q, c)dt/(t log²t), with
Cauchy–Schwarz on the integral and the trivial bound Σ_{q≤Q}Σ_c|E_ψ(t; q, c)|² ≪ t²(log t)^{C′} for t ≤ Q(log x)^{A+1},
give Σ_{q ≤ 8D} 𝔈₂(q) ≪ x²(log x)^{−A} + x^{2−2η}(log x)^{C′} (8D = x^{1−η} ≤ x(log x)^{−A−1}). Taking A = 2B + 2C + 2
proves (3.2). Consequently, for x ≥ x₀, all but at most H²(log x)^{−B/2} pairs have R_{a,b} ≤ x(log x)^{−B/2} ≤
(c₁η/2)x/(log x)² (B ≥ 6, x large).   (3.3)

*Step 3 (survivors).* For p counted in S(𝒜, 𝒬, z) and N ∈ {p + a, 4p + b}: N ≡ 1 (4) (a ≡ 0, b ≡ 1 mod 4, p ≡ 1 mod 8),
so N has an even number of 𝒬-prime factors, all ≥ z, and N ≤ 5x < z³ (η ≤ 1/10, x large). So N ∈ S or N = q₁q₂m with
q₁ ≤ q₂ in 𝒬, q₁ ≥ z, m ∈ S, m ≤ 5x/z² = 5x^{2η}. Hence #target ≥ S(𝒜, 𝒬, z) − |Bᵉ| − |Bˡ| as in Theorem E.

*Step 4 (bad configurations; unconditional, uniform up to a local factor).* Bᵉ: p + a = mq₁k, m ∈ S, m ≤ 5x^{2η},
q₁ ∈ 𝒬, z ≤ q₁ ≤ k ≤ Y := (x + a)/(mq₁) ≤ 2x/(mq₁) (so Y ≥ q₁ ≥ z ≥ x^{0.4}), k prime, p = mq₁k − a prime ≡ 1 (8),
4p + b = 4mq₁k − 4a + b free of 𝒬-primes below z. Discard the ≤ w primes p ≤ w. For fixed (m, q₁) sift the integers
k ∈ [1, Y] by ℓ < w at the classes k ≡ 0 (k prime > w); k ≡ a(mq₁)⁻¹ (ℓ ∤ mq₁; p prime > w); and, for ℓ ∈ 𝒬, ℓ ∤ mq₁,
k ≡ (4a − b)(4mq₁)⁻¹ (ℓ ∤ 4p + b). Every k counted survives. The number of classes ω(ℓ) is ≤ 3 for all ℓ, ≤ 1 at ℓ = 2
(a even), ≤ 2 at ℓ = 3 by admissibility (3 | a: second class is 0; 3 | b: third = second; a ≡ b: third is 0), ≤ 2 at
split ℓ ∉ 𝒬 (no third class), and ≤ 1 at ℓ | m (second and third classes undefined; if ℓ | a too, no p at all). So
ω(ℓ) < ℓ always and the product-condition axiom holds with dimension 5/2 and absolute K. Ford's upper-bound sieve
(as in Theorem E Step 4; remainder O(w log²w), negligible against Y(log x)^{−5/2} since Y ≥ x^{0.4}) gives
  #k ≪ Y ∏_{ℓ<w}(1 − ω(ℓ)/ℓ) ≪ Y (log x)^{−5/2}·h(m)·K_{a,b},
where the generic ω(ℓ) (2 at split ℓ, 3 at inert ℓ ≥ 7, 2 at ℓ = 3, 1 at ℓ = 2) gives ∏_{ℓ<w}(1 − ω_gen(ℓ)/ℓ) ≍
(log x)^{−5/2}, and each ℓ | m·ab(4a − b) at which ω(ℓ) < ω_gen(ℓ) changes the factor by at most
(1 − ω/ℓ)/(1 − ω_gen/ℓ) ≤ (1 − 3/ℓ)⁻¹ ≤ 1 + 6/ℓ (ℓ ≥ 6; at ℓ = 2, 3, 5 the ratio is ≤ 2, 3, 4/3 ≤ 1 + 6/ℓ). Thus
h(m) := ∏_{ℓ|m}(1 + 6/ℓ), K_{a,b} := ∏_{ℓ | ab(4a−b)}(1 + 6/ℓ). Summing over (m, q₁), Σ_{q₁∈𝒬, z≤q₁≤√(2x)} 1/q₁ =
(1/2)log((1/2)/(1/2 − η)) + o(1) ≤ 2η and Σ_{m∈S, m≤5x^{2η}} h(m)/m ≤ ∏_{ℓ≡1(4), ℓ≤5x^{2η}}(1 + (1 + 6/ℓ)/(ℓ − 1)) ≪
(η log x)^{1/2} (Mertens in the progression 1 mod 4), so
  |Bᵉ| ≤ C₂ K_{a,b} η^{3/2} x/(log x)²,  C₂ absolute;   (3.4)
Bˡ (4p + b = mq₁k, k in the class with mq₁k ≡ b (4), p = (mq₁k − b)/4, p + a = (mq₁k − b + 4a)/4 sifted) is identical.

*Step 4′ (the local factor is bounded on average).* Σ_{(a,b)∈[1,H]²} K_{a,b} ≤ C₃H², C₃ absolute. Indeed, with
n = ab(4a − b) ≠ 0, |n| ≤ 5H³, and L := 100 log H: ∏_{ℓ|n, ℓ>L}(1 + 6/ℓ) ≤ exp(6ω(n)/L) ≤ exp(6·log(5H³)/(L log 2)) ≤ 2
(ω(n) ≤ log|n|/log 2), and ∏_{ℓ|n, ℓ≤L}(1 + 6/ℓ) = Σ_{d | n, d | P(L)} μ²(d)6^{ω(d)}/d. For squarefree d, the number of
(a, b) mod d with d | ab(4a − b) is ≤ ∏_{ℓ|d}(3ℓ) (three lines mod ℓ), so #{(a, b) ∈ [1,H]² : d | n(a,b)} ≤
3^{ω(d)} d (H/d + 1)². Hence Σ_{a,b} K_{a,b} ≤ 2 Σ_{d | P(L)} 18^{ω(d)}(H/d + 1)² ≤ 2[4H² Σ_d 18^{ω(d)}/d² + 4·19^{π(L)}]
≤ C₃H², since 19^{π(L)} = exp(O(log H/log log H)) = H^{o(1)}.

*Step 5 (choice).* Given ε: K := 4C₃/ε, η := min(1/10, (c₁/(8C₂K))²), B := 6, c := c₁η/4. By Markov and Step 4′ at
most C₃H²/K = εH²/4 pairs have K_{a,b} > K; by (3.3) at most H²(log x)^{−3} ≤ εH²/4 pairs (x large) have R_{a,b} >
(c₁η/2)x/(log x)². For every other admissible pair, (3.1), (3.3), (3.4):
  #target ≥ (c₁η/2 − 2C₂Kη^{3/2})x/(log x)² − 2w ≥ (c₁η/4)x/(log x)²  (x ≥ x₀(ε)). ∎

*Remarks.* (i) EH enters Theorem E only through Step 1's remainder; averaging over the residue pair (a mod d₁,
b mod d₂) converts it into a mean square over *all* classes, which BDH controls to level x^{1−η} — this is the whole
content. (ii) The theorem says nothing about any specific pair; the exceptional set is "≤ ε" in density, not
explicit, and (4, 1) may well lie in it for every x as far as this argument knows. (iii) The same averaging over the
single shift a (b fixed) fails: the modulus d₂ part keeps a fixed residue −b·4⁻¹ and BDH does not apply; one needs
both shifts free. (iv) Sanity: at odd squares n = m² in place of p the statement is irrelevant (no ES content); the
argument uses primality only through π(x; q, c) and the parity reduction, as it should for a statement that does not
imply ES.

## 4. Direct-attack notes (PROVED identities; nothing usable)

**4.1 Polynomial family on the det-15 quadric.** With u = 2A − C, v = 2A + C, s = 2B − D, t = 2B + D, the quadric
4A² + 4B² − C² − D² = 15 is uv + st = 15 (= det of (u, −s; t, v)); its integer points are the union over (u, s) of the
lattice lines in (v, t). The line u = 1 with s = 2(m + n), t = 2(m − n) gives A = 4 − m² + n², B = m, C = 7 − 2m² + 2n²,
D = −2n, i.e.
  p(m, n) := A² + B² − 4 = (n² − m² + 4)² + m² − 4,  p + 4 = (n² − m² + 4)² + m²,  4p + 1 = (2n² − 2m² + 7)² + 4n²
(checked symbolically and for |m|, |n| ≤ 50 in `scripts/z56_k4try_family.py`). Both shifts are automatically sums of
two squares; they are in S when gcd(4 + n², m) and gcd(7 − 2m², n) have no 𝒬-factor; p ≡ 1 (8) iff m ≡ 2 (4), n odd.
Theorem Q's p = 5m² + 1 is the line (u, s) = (−1, 2) (A = 2m − 1, B = m + 2, C = 4m − 1, D = 2m + 2). The family has
≍ √x·log x members below x (for m ≤ √x, n ranges over an interval of length ≍ √x/m), thinner than a² + b⁴ (x^{3/4}),
and is not a norm form in the sense of Maynard; no prime-value theorem applies (Assessment). More generally every
polynomial family on the quadric is contained in finitely many lines over each (u, s), i.e. in Bunyakovsky slices, and
the full point set (≍ x log x points, multiplicity r(p+4)r(4p+1)) is the whole problem.

**4.2 A false shortcut (recorded as a warning).** For M = (w, x; y, z) ∈ SL₂(ℤ), ‖M‖² ± 2 = (w ± z)² + (x ∓ y)², so
p ≡ 1 (4) prime has p + 4 a sum of two squares iff p + 2 = ‖M‖² for some M ∈ SL₂(ℤ). One is tempted to conclude that
(w + z)² + (x − y)² is automatically in S ("a common 𝒬-factor q of w + z and x − y forces w² + x² ≡ −1 (q)"), but
w² + x² ≡ −1 (mod q) is solvable for every odd q; M = (2, 1; 1, 1) has ‖M‖² + 2 = 9 ∉ S. So the SL₂ reformulation is
exactly r(p+4) > 0 (HCKILL Remark 1.3) and nothing more.

**4.3 Where the direct count breaks (Assessment, two lines).** Σ_p r(p+4)r(4p+1) = 16Σ_{d₁≤√x, d₂≤2√x} χ(d₁d₂)·
π(x; [8d₁d₂], c) + lower order: moduli up to 2x with the residue determined by the split (d₁, d₂) — the balanced
bilinear range √x × √x where neither BFI-type dispersion (fixed residue) nor the multiplicative large sieve saves
anything. This is the det-15 copy of the FI obstruction (§1).

## 5. Numerics (CERTIFIED counts by `scripts/z56_k4try_census.c`; EVIDENCE for the model)

`z56_k4try_census X` builds a least-prime-factor table to 4X + 2 and, for primes p ≤ X, p ≡ 1 (8), reports
A₁(θ) = #{p : N₂ ∈ S, N₁ has no 𝒬-factor < X^θ}, T₁(θ) = A₁(θ) − #{N₁, N₂ ∈ S} (by parity: N₁ = mqq′ with q, q′ ≥ X^θ),
and the mirror A₂, T₂. Model: T/A ≈ B(θ)/F(1/θ) (`data/z56/k4try/model_masses.txt`).

X = 10⁷ (`census_1e7.txt`): 165 976 primes; N₁ ∈ S: 38 696; N₂ ∈ S: 37 142; both: 16 125; Σ_{both} r*(N₂)/8 = 34 400
(mean 2.133).

| θ | T₁/A₁ (N₁ ≤ x) | model B/F | T₂/A₂ (N₂ ≤ 4x) |
|---|---|---|---|
| 0.25 | 0.254 | 0.247 | 0.284 |
| 0.30 | 0.183 | 0.176 | 0.214 |
| 0.35 | 0.109 | 0.114 | 0.141 |
| 0.40 | 0.058 | 0.062 | 0.087 |
| 0.45 | 0.019 | 0.022 | 0.043 |

X = 2·10⁸ (`census_2e8.txt`): 2 769 023 primes; N₁ ∈ S: 595 516; N₂ ∈ S: 574 770; both: 232 258; r*-mean 2.323.

| θ | T₁/A₁ | model B/F | T₂/A₂ |
|---|---|---|---|
| 0.25 | 0.244 | 0.247 | 0.271 |
| 0.30 | 0.170 | 0.176 | 0.199 |
| 0.35 | 0.109 | 0.114 | 0.138 |
| 0.40 | 0.056 | 0.062 | 0.083 |
| 0.45 | 0.017 | 0.022 | 0.040 |

Reading: the Buchstab masses used in P415's and §2's ledgers are the right order at these heights (N₂ ≤ 4x has
effectively smaller θ, hence larger masses; the model's F, B are x → ∞ limits, so a few per cent drift is expected).
Family §4.1: `family_check.txt` — symbolic identities, the mod-8 criterion, 9 740 members with |m|, |n| ≤ 50 and clean
gcds all have both shifts 𝒬-free, and 55 624 members below 10⁸ (≈ 0.3·√x·log x).
Odd-square control: not applicable (no statement here implies ES).

## 6. What would close P(4,15) (Assessment, inherited and sharpened)

* A level-of-distribution input for primes in the CRT classes of (p + 4)(4p + 1): EH(1 − η₀) (Theorem E), or the
  structured 𝒟(1/2 − η₁) plus Lemma S (§2.3); in the model, 𝒟 at total level ≈ 0.91 with the switched sums covered.
* Or a genuinely new idea for the balanced bilinear range — the same thing FI's det-1 problem needs (Sedunova's
  2026 progress is on almost-primes and square-free distances only).
* Not: algebraic families (Lemmas A1/A2 of P415 plus §4.1 here), averaging over shifts (Theorem AA shows the generic
  case is easy, which is why it says nothing about (4, 1)).

## 7. Reproduction (every command under `timeout` and `ulimit -v 6000000`)

```
uv run --with numpy python scripts/z56_k4try_hybrid.py          > data/z56/k4try/hybrid_model.txt   (≈ 1 min)
uv run --with numpy python scripts/z56_k4try_family.py           (identity checks, §4.1)
gcc -O2 -o z56_census scripts/z56_k4try_census.c -lm; ./z56_census 10000000  > data/z56/k4try/census_1e7.txt
./z56_census 200000000 > data/z56/k4try/census_2e8.txt            (≈ 3.2 GB, ≈ 10 min)
```
`scripts/z56_k4try_hybrid.py` imports F, f, B from `scripts/z55_p415_sieve.py` (unchanged).

## 8. Review log

(filled after the hostile line-by-line review)
