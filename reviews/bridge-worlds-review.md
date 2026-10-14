# R216 — hostile review of O211 (BRIDGE_WORLDS.md + BRAINSTORM/y3_*.md)

Reviewer: R216 (side agent). Branch `side-agent/review-bridge-worlds`, merged `side-agent/bridge-worlds` at 7714153a.
**ES is not solved; nothing in O211 claims otherwise, and nothing here changes that.**
From-scratch scripts: `scripts/review_r216_*.{c,py}` (none of the author's `scripts/y3_*` were reused).

## Summary verdicts
(filled in progressively; see sections below)

## Checks, claim by claim

### C1. §1 Lemma 1.1 / Prop 1.2 / Prop 1.3 (scaling collapse, additive bridge) — SOUND (one label understated)
Re-derived. Lemma 1.1: F_h^* = ⟨g^{h+1}⟩ ⊂ ⟨g^m⟩ since m | h + 1. Prop 1.2: x ↦ (λ^{w_i}x_i) preserves each C_{a_i}
(λ^{w_i} ∈ F_h^* ⊂ C_0) and maps F = u to F = λ^e u. Prop 1.3: Φ-free identity (X^c − 1)/(X − 1) at X = 1; then
4cd·c = 4c²d. Stickelberger (BEW Thm 11.6.3 — book not accessible here; statement as recalled: h^t ≡ −1 (mod m),
t minimal, q = h^{2tγ}, g(χ) = (−1)^{γ−1+γ(h^t+1)/m}√q) gives (−1)^j h with t = γ = 1, m = 4cd.
From scratch (`scripts/review_r216_gauss.py 60`, F_{h²} = F_h[i], all h ≡ 3 (4) in [7, 59], all m | h + 1, m ≥ 3):
g(χ) = (−1)^{(h+1)/m} h, ∏_{μ_c∖1}(1 − ζ) = c, and the u-independence of #{x ∈ C_a : x + u ∈ C_b} (u ∈ F_h^*):
0 failures.
**The uniform-cyclotomy residue law is PROVED, not EVIDENCE (two lines; this also settles the report's spark 2).**
With (a,b) = #{x ∈ C_a : 1 + x ∈ C_b} and J'(χ^s, χ^t) = Σ_{x ≠ 0, −1} χ^s(x)χ^t(1 + x),
m²(a,b) = Σ_{s,t mod m} ζ_m^{−as−bt} J'(χ^s, χ^t). Here J'(1,1) = q − 2, J'(χ^s,1) = J'(1,χ^s) = J'(χ^s,χ^{−s}) = −1
(s ≢ 0; uses χ(−1) = 1, true as −1 ∈ F_h^* ⊂ C_0), and for s, t, s + t ≢ 0 the Jacobi sum is g(χ^s)g(χ^t)/g(χ^{s+t})
up to a sign χ^s(−1) = 1, i.e. ±h, since every nontrivial character of order | h + 1 has a pure Gauss sum ±h. With
q = h² ≡ 0: **m²(a,b) ≡ 1 − m(δ_{a,0} + δ_{b,0} + δ_{a,b}) (mod h)**, i.e. 1 − 3m at (0,0), 1 − m when exactly one of
a = 0, b = 0, a = b holds, and 1 otherwise. My script confirms this exact *pattern* (not just the value set) for every
(a,b), m | h + 1, m ≥ 3, h ≤ 59: (0,0)/(0,i)/(i,0)/(i,i)/other = 1 − 3m / 1 − m / 1, 0 exceptions.

### C2. Thm 2.1 (three tiers) and Cor 2.2 — SOUND-AFTER-REPAIRS (minor; the statements are correct but near-tautological)
(a) Hom(ℤ/m, ℤ/(h − 1)) has order gcd(m, h − 1) | gcd(h + 1, h − 1) = 2. Correct.
(b) Correct over ℂ: a symmetric S regular at the point μ_m (some ordering) is regular on the whole S_m-orbit, hence
(invariants of the semilocal ring of a finite quotient) S = A(e)/B(e) with A, B ∈ ℚ[e_1..e_m], B(e(μ_m)) ≠ 0. At μ_m the
e_i are the coefficients of X^m − 1 in ℂ and in F_{h²}, so S(μ_m mod h) ≡ A(ē)/B(ē) = s(m) mod h provided B(ē) ≢ 0
(mod h) and A, B have h-integral coefficients. The author's proof ("S is a rational function of the e_i") skips the
regularity step, and the "good reduction" hypothesis is stated for "the fixed formula" — it must refer to an
A(e)/B(e) representation (a representation P(x)/Q(x) with Q(μ̄_m) ≠ 0 but B(ē) ≡ 0 gives a value that need not be
the residue of s(m), which then has h in its denominator).
Two of the listed examples are not instances of (b) as defined: |μ_c| = c is not a rational function of the
coordinates at all, and ∏_{ζ≠1}(1 − ζ) and Σ csc²(πk/c) are symmetric in μ_c ∖ {1}, not in μ_m (the factor ζ = 1
would vanish). Both are covered by the obvious generalisation "symmetric functions of the roots of a fixed monic
F ∈ ℤ[X] (here (X^c − 1)/(X − 1)) with unit leading coefficient", whose proof is identical. → m1.
(c) Correct: Frob_𝔓|ℚ(ζ_m) = (ζ ↦ ζ^h) = c_∞ (h ≡ −1 mod m), trivial on K = ℚ(ζ_m)⁺; h splits completely in K; a
fixed f ∈ ℚ(X) with f(ζ) = f(ζ^{−1}) in characteristic 0 has f(ζ) ∈ K and its reduction at the place 𝔓 picked out by
ζ ↦ ζ̄ is ρ_𝔥(f(ζ)) if f(ζ) is 𝔥-integral. The quantifier that carries all the content is that **f is fixed
independently of h** (and of p). Without it tier (c) is vacuous: the prime field of F_{h²} is F_h, so every element of
F_h is "built from μ_m by field operations" (e.g. 1 + … + 1). The memo y3_lucas_dickson_trace (Prop G) states this
("independent of h once the characteristic-zero formula is fixed"), but Thm 2.1(c) as written in BRIDGE_WORLDS does
not. → m2. Note also that "a single ζ" is no restriction (μ_m = ⟨ζ⟩).
Cor 2.2: Type II at (c,d,h) ⟺ h | p + 4c²d ⟺ −p ≡ 4c²d ≡ c/j (j·4cd = h + 1). Correct; the author correctly notes
rationality ≠ box membership (3 ∉ {1,2,4} at h = 7: Box(2) = {c/j : cj | 2} = {1, 2, 1/2 = 4} ✓).
Scope/labels: "every useful bridge is archimedean" is labelled Assessment in §2, §7 and the report — correct. But the
§2 heading "Classification of bridges between the two worlds (PROVED)" still reads as a classification; what is proved
is three elementary facts about three hand-picked classes. → m3 (relabel heading).
