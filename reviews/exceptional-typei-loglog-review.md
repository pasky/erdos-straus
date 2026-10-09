# Hostile review R111 of EXCEPTIONAL_TYPEI_LOGLOG.md (O111, branch side-agent/heegner-typei)

Reviewer: side-agent/review-ttl. Scope: all claims of AGENT_REPORT_O111.md, with emphasis on the R1
repairs (not re-reviewed by the author). From-scratch scripts: `scripts/review_ttl_*.py`.
Status: IN PROGRESS (written claim by claim).

## Verdicts per claim

**V1. Lemma 2.1 (distance formula) — SOUND.** Re-derived; `scripts/review_ttl_sep.py` checks
`cosh−1 = disc(Q−Q')/(8d)` in exact rationals for every pair in 𝓕_d, d ≤ 30, A ≤ 40.

**V2. Lemma 2.2 (uniform separation) — SOUND.** `4d | disc(Q−Q')` re-derived (B ≡ B' (2d) ⇒ 4d² | (B−B')²;
d | C−C' ⇒ 4d | 4(A−A')(C−C')) and checked by brute force. The constant 3/2 is **sharp** on 𝓕_d
(attained for d = 1, 5, 11, 19, 29 in the window), and the Type I subset has min cosh = 3 as the author
observed. Injectivity of Q ↦ z_Q (A fixed by disc) correct.

**V3. Parity/invariance group (§6 'Parity') — SOUND.** On the z-side the Type I set is stable under
`Γ⁰(2d)∩Γ₀(2)` (0 failures in random tests, d ≤ 30), i.e. `Γ₀(2d)∩Γ⁰(2)` on the w-side; R1's
counterexample reproduced (`[1,8,18] ↦ [27,44,18]`, B = 44 ≢ 0 mod 8). Conjugating
`Γ₀(2d)∩Γ(2q)` by `u = w/(2q)` gives `{γ ∈ Γ₀(4dq²): p ≡ s ≡ 1 (2q)}` ⊇ Γ₁(4dq²), cusp width 1, so the
character decomposition over even χ mod q (= mod 2q) with `M = 4dq²` is right (see D-list for the
normalisation factor).

**V4. Lemma 6.1 (main-term factorisation) and the §6 densities — SOUND.** `scripts/review_ttl_local.py`:
for all odd primes ℓ ≤ 23, ℓ ∤ d, the quadric `B²−4AC = −4d` has `ℓ²+χℓ` points and SL₂(𝔽_ℓ) is
transitive on it (orbit size = quadric size; directly: the stabiliser of Q̄ is SO(Q̄), a torus of order
`ℓ−χ`, and `ℓ(ℓ²−1)/(ℓ−χ) = ℓ(ℓ+χ)`). The 'Witt' justification is imprecise (SL₂ maps onto the
spinor-kernel Ω ⊂ SO, not SO), but the conclusion is true. Both g_{c,d}(ℓ) formulas verified. The
orbit-stabiliser/strong-approximation bookkeeping is correct as a *ratio*; `[Γ'_1:Γ'_q]` as Möbius
groups is `|SL₂(ℤ/q)|/2` (−I ∈ Γ(2), −I ∉ Γ(2q)), which only affects the constant in Thm 6.2's last line
(minor D10).

**V5. Lemma 6.3 (r(d), incl. 2-adic) — SOUND (with room to spare).** Brute force over every primitive
reduced form of disc −4d, d ≤ 150: `#{(t:s) ∈ ℙ¹(ℤ/d): Q₀(t,s) ≡ 0 (d)} ≤ ∏ p^{⌊k/2⌋}` with **no**
extra factor 4 at p = 2 (max ratio 1.0). Re-derivation of the 2-adic case: Q₀ primitive ⇒ WLOG A odd;
B = 2B'; `4A·Q₀(t,1) = 4((At+B')² + d)` so `2^k | Q₀(t,1)` ⇔ `At+B' ≡ 0 (2^{⌈k/2⌉})`, and points
`(1:s)`, 2 | s, give `Q₀ ≡ A` odd. The factor 6 = [Γ₀(d):Γ₀(2d)∩Γ(2)] is correct for odd d and is 4 for
even d. `Σ_{d≤D} r(d) ≪ D log D`, so the final bound even holds with `(log D)²`. Note that the per-d
relative error is **not** uniform in d (Siegel: `#Λ(1)` can be ≈ d^{1/2−ε}); the proof correctly avoids
this by summing absolute errors via Cauchy–Schwarz — the paper should say so explicitly (D11).

**V6. Lemma 1.1 — SOUND.** `#{(j,k) ∈ [1,L]²: max(j,k) = m} = 2m−1`, so the identity and `≤ 2L` hold;
the application (m_{jk} ≪ NL per (c-block, a-block), from ET (8.2)-type mass) is consistent. j = 0
(c ≍ 1, no BT saving) costs only `Σ_k NL·C/k ≪ NL log L` — harmless, but not mentioned (minor).

**V7. Prop 4.3 / Lemmas 4.1–4.2 (Sobolev duality, uniform in Γ') — SOUND (modulo ±I bookkeeping).**
`h(t) = (5/4+t²)^{−2}` is holomorphic in `|Im t| < √5/2 > 1/2` with `t^{−4}` decay, so the pre-trace
kernel is legitimate; `1−Δ = −Δ − s(1−s)` at `s = φ`, so the decay rate `e^{−φr}` (times `r` for the
square) is right; packing only uses the separation radius, hence uniform in Γ', d, q. The pairing
`ν(P₀) = ⟨(1−Δ)P₀,(1−Δ)^{−1}ν⟩` is fine (resolvent kernel has a log singularity, in L²). If −I ∈ Γ' the
kernel sum double-counts (factor ≤ 2). P_ψ ∈ L² since ψ has compact y-support (vanishes high in every cusp).

**V8. Thm 6.2 (per-d count) — SOUND at outline level, given Prop 5.1.** Re-derived the bookkeeping:
`#Λ(q)^{1/2} ≈ q #Λ(1)^{1/2}`, main `≈ 𝔐_d/q`, relative error per q `≈ q²[(d/A)^{1/2} + F'^{1/2}/A]`,
summed absolutely over d via Lemma 6.3 + Cauchy–Schwarz. Main-term density checked numerically from
scratch (`scripts/review_ttl_perd.py`: d = 101, 1009, A = 2·10⁴, F' ≈ A√d/2, c ∈ {1,2,3,5}, q ≤ 23 —
all counts within ~±2σ of `g_{c,d}(q)·N_d(1)`, including the `ℓ | c` cases, e.g. g = 0 for c = q = 3,
d = 1009). Weak evidence (sharp cut-offs, small sizes) but it confirms the orbital density is the
arithmetic one. Defects: D5 (cusp-width/period inconsistency F ≥ 8A vs f' ≥ A/8), D10.

**V9. Prop 7.1 ((K_a), fixed a) — SOUND at outline level (the restriction min(E,F) ≥ N^{c₀} is
necessary and sufficient for its use).** Re-derived: (0,0) term = `g'(q)·S_a(1)` main term (density
`φ(m)/m²` × `(ℓ−1)/ℓ²` resp. `1/ℓ`, verified in `review_ttl_local.py`); h = 0 ≠ k: the k-sum is the error
of replacing `Σ_{(f,m)=1}` by `(φ(m)/m)∫`, giving relative `O(τ(m)·q/F)` (and symmetrically `q/E`); hk ≠ 0:
Weil for prime-power moduli `|S(h,k;p^β)| ≤ 2p^{β/2}(h,k,p^β)^{1/2}`, `≪ (mq)²/(EF)` effective pairs,
the gcd sum is `≪ HK` (multiples of δ > H don't occur), total `≪ τ³ 3^{ω(q)} q m^{1/2} = O(qa)`. E or F > m
is harmless (then only h = 0 resp. k = 0 survive and the bound only improves). From-scratch numerics
(`scripts/review_ttl_ka.py`, smooth weights): for `E,F ≥ 131`, `|S_a(q) − g'(q)S_a(1)| ≤ 0.1·qa` for all
q ≤ 41, a ∈ {3,7,10}, c ∈ {1,5}; for `E = 3` (tiny e, a = c = 1) the deviation is `37·qa` at q = 5 (R1's
failure reproduced; consistent with the `qD/E` term). Inside R_bad(η₁) one indeed has
`e, f ≥ N^{1/2−3η₁/2}` (re-derived from MN3 Prop 3.3: β ≥ (1−η)/2 from α+β ≥ 1−η, α ≤ β; and
`1+α−β ≥ max(1−α−γ−η, α−η)`), so Prop 7.1 applies throughout the fixed-a part of R_bad. Defect D6
(stale reference to the retired Prop 7.2 inside the proof).

## Defects
(filled below)
