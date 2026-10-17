# R269 — hostile review of O256 (BALANCED_LATTICE.md, checkpoint 1 incl. R-O256 repairs 1–9)

Reviewer: R269 side agent (branch side-agent/review-balanced-lattice, merged side-agent/balanced-lattice at a5cf0e51).
Scope: BALANCED_LATTICE.md §§1–7, memos BRAINSTORM/z27_*.md, scripts/z27_{dual,eqcheck}.py, data/z27/, AGENT_REPORT_O256.md.
From-scratch scripts: scripts/review_r269_*.py (none reuse the author's code). Sources/ contains none of Banaszczyk 1993,
Serre 1981, Schinzel 1977: citation checks below are from the reviewer's knowledge of the statements and are flagged as such.

## Summary verdicts (filled in claim by claim)

| claim | verdict | notes |
|---|---|---|
| Lemma 1.1 (Λ*/ℤ^S ≅ Ĥ) | SOUND | re-derived; also checked numerically with an LLL dual basis built from an independent kernel computation (no characters used): λ₁^{(1)}(Λ*) = min(1, 𝔻_min) in 70/70 non-degenerate samples |
| Prop 1.3 (transference) | SOUND | constants re-derived: lower bound exact; upper uses μ_∞ ≤ μ₂, Banaszczyk μ₂λ₁^{(2)}(Λ*) ≤ k/2 (his formal bound, valid for every k, no o(1)), λ₁^{(2)} ≥ λ₁^{(1)}/√k. Discrete consequences via FORCED_WINDOW Prop 4.1(i)/(ii) correct. Numerics: μ_∞·min(1,𝔻) ∈ [0.51, 0.96] (k = 3) and [0.62, 1.11] (k = 4) against the proved window [0.5, k^{3/2}/2]; D1, D2 |
| Cor 1.4 | SOUND-AFTER-REPAIRS | (a), (c) correct; (b) is an "⟺ up to k^{O(1)}" whose two directions carry different constants (D3) |
| Prop 2.1 | SOUND | (a) re-derived (Frob_𝔔 ∈ Gal(K_m/ℚ(ζ_m)) ↪ Hom(⟨S⟩, μ_m); conjugation by σ_u gives b ↦ ub; ψ^m = 1 ⟺ ψ = χ_m^j\|_{U_q}, θ_s = 2jb_s/m since m odd). (b) b = a mod m checked numerically (40 q, all m \| N, m < 200: 0 mismatches). Scope can be widened (D4) |
| Prop 2.2 | SOUND (honestly scoped) | proof complete; the fake has L′_min = N₂ − 1 exactly in 12/12 real-q tests (data/review_r269/prop22_fake.txt; L_true ≈ 20). It is an information statement about abstract vectors and is labelled as such; it is not a barrier for statistical arguments (the text says so). D4, D5 |
| Assessment 2.3 | SOUND as Assessment | the \|C\|-linear GRH error is not the only available form; the conclusion survives the refined forms, but for a different reason (D6) |
| Prop 2.4 | SOUND | trivial; (b) duplicates 2.1(c) |
| Lemma 2.5 | SOUND | degree 2φ(lcm(8P,ℓ))ℓ^k re-derived; \|C\| ≤ 1 and C is a (central) conjugacy class; Serre's Thm 4 form (\|C\|/\|G\|)(log d + n log x)√x = \|C\|√x(log d/n + log x) and Prop 6 (log d/n ≤ Σ_ram log r + log n) quoted correctly (from memory; PDFs not in sources/). Densities match numerically (D7) |
| Prop 3.1 | SOUND | every step re-derived (fibre bound N(2Bε + 1/d), Cauchy–Schwarz, Π ≥ 4(B+1)^k, Fejér identity Σ_h w(h)[q \| N_h], \|N_h\| < P^{2B}); the constants are slack: the proof gives (4/3)B(2B+1)xε log P/log(x/2) and 8(6xε)^{(k+1)/(k−1)}…, stated 4B(2B+1)… and 48(…). Each proof step checked numerically for every Bad₁ prime (D8) |
| Prop 3.2 | SOUND | (wording: "1/d > ε" should be "1/d ≥ ε > 𝔻"; D8) |
| Cor 3.3 | SOUND (as bookkeeping; "PROVED + arithmetic" is fair for the displayed L, the "no class-blind bound can recover" sentence is Assessment) | exponent arithmetic and the y-optimisation to exp(O(√(log₂p log₃p))) re-derived (y ≈ 2√(log₂p log₃p) when log x ≈ 4 log₂p) |

**D8 (MINOR) — Prop 3.1 / Prop 3.2 statement hygiene.** (i) Bad₁(ε) is defined for "q prime" but g_s = s² mod q needs
q ∤ 2P (and the notation section restricts to q ≡ 3 (mod 4)); for x/2 < y the set (x/2, x] meets S. *Repair:* define Bad₁ for
odd primes q ∤ P, and say whether q ≡ 1 (mod 4) is included (it matters for Hypothesis S, see D11). (ii) The constants 4 and 48
can be 4/3 and 8; harmless. (iii) Prop 3.2 proof: "1/d > ε" → "1/d ≥ ε > 𝔻_S(ψ)". From-scratch numerics
(scripts/review_r269_fejer.py P): y = 7, x = 2·10⁴, ε = 0.014, B = 33: 8 Bad₁ primes, every proof inequality holds;
Σ_q(Π − (B+1)^k) = 2.3·10⁸ vs the bound 5.2·10¹⁰; y = 5, ε = 0.004, B = 319: 70 Bad₁ primes, 0 failures, 2.1·10⁹ vs 2.0·10¹²
(the per-relation charge 2B log P/log x is the main slack, as the author's Reading says).
