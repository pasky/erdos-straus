# BRIDGE_WORLDS — bridging the (h+1)- and (h−1)-worlds (task O211, spark relay Y3)

Status: in progress (O211). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on TORSION_FIRING.md (O207, Thm 3.1 torsion–residue orthogonality), FIXED_MODULUS_SHOTS (Thm 3.1 box),
FF_MUTE ((J)30), FROBENIUS_FIRING ((J)34). Memos `BRAINSTORM/y3_*.md`, scripts `scripts/y3_*`.

Notation. p odd prime; h prime ≡ 3 (mod 4), h ∤ p; k = (h + 1)/4. Type II fires at h iff ∃ c, d, j ≥ 1 with
h = 4cdj − 1 and h | p + 4c²d (⟺ h | pj + c ⟺ −p ≡ c/j mod h, cj | k: the box). Write m = 4cd (so m | h + 1:
h is *semi-primitive* mod m, h ≡ −1). N_II(p) := #{(c, d, h) : 4cd | h + 1, h | p + 4c²d} (all h, prime or not),
N_II^pr(p) the same with h prime.

## 0. Iteration log
(I1) Task (a): semi-primitive (uniform) cyclotomy over F_{h²}. Result: a scaling-collapse proposition (§1) — every
cyclotomic statistic at level m | h + 1 sees p only through F_h^*/F_h^{*e}; the only non-homomorphic bridge is
the additive shift ζ ↦ 1 − ζ, which transports exactly the INTEGER m (cardinality), i.e. the box. Memo
`y3_semiprimitive_collapse`.

## 1. Semi-primitive cyclotomy is p-blind except through the integer m (PROVED)

**Lemma 1.1.** Let h be an odd prime, g a generator of F_{h²}^*, m | h + 1, C_a = g^a⟨g^m⟩. Then F_h^* ⊂ C_0.
*Proof.* F_h^* = ⟨g^{h+1}⟩ and m | h + 1. ∎

**Proposition 1.2 (scaling collapse).** Let F ∈ F_h[x_1..x_n] be weighted-homogeneous: F(λ^{w_1}x_1, …) = λ^e F(x)
for λ ∈ F_h^*. For a ∈ (ℤ/m)^n and u ∈ F_h^* put N_a(u) = #{x ∈ (F_{h²}^*)^n : F(x) = u, x_i ∈ C_{a_i}}. Then
N_a(λ^e u) = N_a(u) for all λ ∈ F_h^*. Hence N_a(p) depends on p only via p mod F_h^{*e}.
*Proof.* x ↦ (λ^{w_i}x_i) is a bijection of the solution sets that preserves each C_{a_i} by Lemma 1.1. ∎
Consequences: (i) shifted cyclotomic numbers #{x ∈ C_a : x + u ∈ C_b} (F = x_2 − x_1, e = 1) are independent of
u ∈ F_h^*; (ii) with e = 2 the only p-information is the Legendre symbol (p/h): the genus layer of Thm 3.1.

**Proposition 1.3 (the additive bridge).** In F_{h²}, ∏_{ζ ∈ μ_c ∖ {1}} (1 − ζ) = c for every c | h + 1. Hence Type
II fires at (c, d, h) iff −p ≡ P(μ_{4cd}) · P(μ_c) (mod h), P(μ) := ∏_{ζ∈μ∖1}(1 − ζ). Pure Gauss sums of order m
equal (−1)^{(h+1)/m} h (Stickelberger; BEW Thm 11.6.3), so g(χ_{4cd}) = (−1)^j h: they carry only the parity of j.
Uniform cyclotomic numbers reduce mod h to integer polynomials in m (EVIDENCE: m²(a,b) ≡ 1, 1 − m, 1 − 3m).
*Proof.* (X^c − 1)/(X − 1) = ∏(X − ζ) at X = 1. ∎ **Assessment:** the non-homomorphic bridge between the two
worlds that semi-primitivity supplies is cardinality (the integer m read in F_h); it is the box, not new input.
