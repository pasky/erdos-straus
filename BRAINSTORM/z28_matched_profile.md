# z28_matched_profile — sources sharing p's non-residue primes (O257; NONCONG_LIFTS §3, §4.1)

**Idea.** O253 spark: sources q with (q/ℓ) = (p/ℓ) for ℓ ≤ B make q's own T1 constraint visible to p. Is visibility
then sufficient in some family?
**Results.** Lemma 3.1 (PROVED): with q ≡ p (8) and matched profile up to B, every source witness with B-smooth
modulus is visible to p (q ≢ □ mod H′ by T1 at q, and the witnessing local non-square transfers). CERTIFIED: at the
fixtures (B = 7, |p − q| ≤ 600) and all 273 Mordell-class primes ≤ 10⁵ (|p − q| ≤ 1000): 1347 sources, 65% of witnesses
visible, 30% of visible ones transport by determined lifts, 0 sources total, 0 sources where visibility suffices.
Model screen: at exceptions of k = 8, 12, 16 (131, 241, 1129…12241, 3361…83449) matched soluble sources have many
visible witnesses (8/131 ← 251: 10/10), none transports — the matched-source law is false in models sharing T1.
**Literature.** O253 AMPLIFY_EXCEPTION Thm 3.1–Cor 3.3; CAP_POINTWISE (J)64 (non-residue windows force information).
**Barrier screen.** B2: transport of a visible witness is "p has a witness with H | H′", a divisor event; §2.4 explains
the 30%: visible levels involve primes ≥ 11 and are incomplete. B6: n/a. (J)41/models: screened out.
**Cheap numerics.** `scripts/z28_matched.py`; logs `logs/z28_matched_{fixtures,mordell,models}.txt`.
**Assessment.** PROVED (lemma) + CERTIFIED (negative). Profile matching removes the adversary's small-prime inputs
but not the incompleteness of the levels that remain.
