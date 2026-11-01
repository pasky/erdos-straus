# ZF1 shard S2 — interesting items

## Z2418 — the 3/4 exceptional-set theorem can be made effective (Assessment)
**What.** Line audit of `paper/es-threequarter-note.tex`: Siegel–Walfisz enters only via Bombieri–Vinogradov
(eq. BV, saving (log x)^{−26}) in the lower bound of Thm `supply`; moduli are q = 4uv ∈ (4X^{1/24}, 4x^{1/3}].
BMOR's explicit PNT-in-AP (arXiv:1802.00085) is unusable there (needs x ≥ exp(0.03√q log³q) for q > 10⁵).
An effective BV that excludes multiples of one Landau–Page modulus r1 (Akbary–Hambrook arXiv:1309.2730 Thm 1.2,
explicit c0 = 48.83, + effective zero-free region) suffices: if r1 ≤ (log x)^{1.9} BMOR Prop 1.11
(β ≤ 1 − 40/(√q log² q)) makes the exceptional term x^{β1} ≤ x·exp(−(log x)^{0.04}); otherwise drop the triples
with r1 | 4uv from the (nonnegative) lower-bound sum, losing a fraction ≪ (log x)^{−1.9+ε} of the main term.
**Numbers / reproduce.** No computation; read `data/z52b/pass2/ZF1/Z2418/effectivity.md` §§1–4 against the note,
l. 297–307 and 497–541.
**Why it might matter.** The flagship internal theorem is stated as "ineffective because of BV"; the sketch removes
that caveat cheaply (same for the log log and m/n notes, which use BV the same way — not re-derived). It does NOT give
any calibration: N·exp(−c(log N)^{3/4}) → ∞, so no version can certify "no counterexample below X" (§5).
**Next.** Write the lemma into the note and get it reviewed; optionally make Shiu's constant explicit.
