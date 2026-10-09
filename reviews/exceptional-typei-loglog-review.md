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

## Defects
(filled below)
