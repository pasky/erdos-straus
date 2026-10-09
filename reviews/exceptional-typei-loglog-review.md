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

## Defects
(filled below)
