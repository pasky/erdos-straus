# z32 memo 3: how much can a conspiracy prime kill? (O262; DISPROOF_AVENUES §3.2)

Labels as in DISCOVERIES.md. ES is not solved. Budget statements are Assessment (Bateman–Horn heuristics); the
killing statement itself is memo 2 (PROVED, existence CONDITIONAL).

**Idea.** Construct p that kills as many solution families as possible at once: windows ≤ M, b = 1 shifts ≤ σ,
c = 1 shifts ≤ σ, Type I levels ≤ L — and count what survives.

**Budget.** At size X (L = log X) a Prop-3.1 prime needs Q ≤ X and k prime cofactors; Bateman–Horn gives
≈ 𝔖X/(Q L^{k+1}) such p, 𝔖 ≲ (e^γ log y)^{k+1}. Hence **k ≲ L/log L** prime-forced slices, plus every congruence
row with modulus dividing Q.

**What survives.** e-slices carry ≍ L²/e each (share of e ≤ 31 in f_II: 0.22 at 10⁸, 0.10 at 10¹⁶; O154), pair
slices ≍ L/q. The best k slices carry a share ≈ log k/L ≈ (log L)/L. Congruence conditions multiply the mean by
a saturating ≈ 0.73 (O154, y = 13…37, 10⁸…10¹⁶). So **≍ L³ = (log p)³ solutions remain untouchable**, not ≍ √p:
the √p-sized unions (full b = 1 line, all e-slices) need moduli > p ((J)90 Thm 4.2 Reading).

**Data (EVIDENCE, memo 5).** At 10¹⁸–10²⁵ the best designs depress the cheap-family count to 0.26–0.36 of
controls (saturating), and at 10¹² the exact f_II only to 0.80–0.82.

**Barrier screen.** This is B1 + B2 seen from the disproof side: congruence data saturate; finite slice sets fall
but carry a vanishing share; growing families cannot be forced. B3: the surviving main term is p^{o(1)} but → ∞.

**Viability (Assessment).** COLLAPSES as a disproof route at "kill a positive share of the bulk". Promise 0/5.
