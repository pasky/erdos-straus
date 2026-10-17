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
| Hypothesis EQ | precise; not trivially false | p-free; uniform in y (P ≤ √x), ε, class. Not false for trivial reasons: (i) at ε where Bad₁ has positive density it is a Brun–Titchmarsh-type statement; (ii) its Chebotarev-visible part (index-ℓ degeneracy with ℓ > 1/ε) has ℓ > 1/ε > y, so ℓ ∤ 8P and the splitting fields are linearly disjoint from ℚ(ζ_{8P}) (D7's abelianisation argument) — equidistributed mod 8P, consistent with EQ; the class-correlated index part (ℓ ≤ y) lies in Bad₂, as the author's numerics show; (iii) it is trivially true when P ≥ x^{1/2}(log x)^{−A+1} (each class has ≲ √x log y/log x primes), but non-trivial where used (P ≍ √x/log²p). Domain of q unstated (D11) |
| Hypothesis S | precise; not trivially false | p-free and class-free as claimed. Toy test (from scratch, all q ≤ 2·10⁵): y = 5: 1 prime, y = 7: 1 prime in Bad₁(x^{−3/(2k)}), vs x^{1/2} = 447; the uniform-random model with the 1/ζ(k)-primitive and ± corrections predicts O(5). Prop 5.2-type families: the index-degenerate part needs ℓ > x^{3/(2k)}, where GRH-Chebotarev least-prime bounds give q ≲ ℓ^{2k} > x³, so they produce no counterexample. Uniformity over all y is more than needed (D12) |
| Thm 4.1 | SOUND (relative to GRH + EQ) | every inequality re-derived: Bad₂ main ≤ G·Σ_{ℓ≥3}ℓ^{−k}, error/G ≍ z log x/log p → 0; Bad₁ main = 48c₃x/(φ(8P) log(x/2)) by the choice of ε; EQ error/G ≍ (log x)^{A+1}/log²p → 0; 1/ε = 6x^{2/(k+1)}(C log P/c₃)^{(k−1)/(k+1)} = y^{5+o(1)}; L = y^{13/2+o(1)}; FORCED_WINDOW Thm 4.3 applicable (y ≤ log p, L = L(p) not q-dependent per R264 D7, q ≤ X(p)). Exponent evaluated numerically (D9) |
| Thm 4.2 | SOUND (relative to GRH + S) | ε = x^{−3/(2k)}: 1/ε = y^{3+o(1)}, L = y^{9/2+o(1)}; S's total ≤ x^{1/2}(log x)^A ≤ G/8. Hypotheses should be spelled out (D10) |
| Reading after 4.2 ("S ⇒ EQ at the parameters used") | SOUND | only at ε = x^{−3/(2k)} (Bad₁(ε) is not monotone in ε) |
| Remark 4.3 | SOUND (Assessment-level, not new) | Markov over classes + equidistribution of −p mod 8P (needs GRH for primes in progressions to modulus 8P = (log p)^{(1+o(1))log₃p}, beyond Siegel–Walfisz — available since GRH is assumed) and x frozen per dyadic p-block; correctly declared weaker than CAP_INTERPOLATION §2 |

**D9 (MINOR, informative) — size of the o(1) in Thms 4.1/4.2.** From-scratch evaluation of the paper's own parameter choices
(scripts/review_r269_exponents.py, data/review_r269/exponents.txt; C₀ = C = 10³, c₃ = 10⁻³): log L/log log₂p equals
12.3, 10.8, 9.9, 9.3, 8.9 (Thm 4.1) and 6.2, 5.8, 5.6, 5.4, 5.3 (Thm 4.2) at log₂p = 10², …, 10⁶; measured against log y the
values are 7.5 and 4.46 at log₂p = 10⁶. The limits 13/2 and 9/2 are right, but the o(1) is O(log₄p/log₃p) (from
log x/y = 2 + O(1/log₃p), y/k = log y − 1 + o(1), and log y = log₃p + log₄p + …). *Repair (optional):* write
(log₂p)^{13/2 + O(log₄p/log₃p)}, or state the bound as y^{13/2+o(1)} with y = log₂p·log₃p.

**D10 (MINOR) — Thm 4.2 statement.** "CONDITIONAL on GRH + S" without saying which GRH. *Repair:* "Assume GRH for Dirichlet
L-functions and for the Dedekind zeta functions of ℚ(ζ_{lcm(8P,ℓ)}, √p, S^{1/ℓ}) (ℓ odd prime ≤ y^{3+o(1)}), and
Hypothesis S."

**D11 (MINOR) — domain of Bad₁ in EQ and S.** The notation section takes q ≡ 3 (mod 4), Prop 3.1 says "q prime", S says
"#{q ≤ x : q ∈ Bad₁}". For q ≡ 1 (mod 4), U_q has even order and the definitions still make sense, but the application needs
only q ≡ 3 (mod 8), q ∤ P. *Repair:* state EQ and S for primes q ≡ 3 (mod 8), q ∤ P (weakest form); this also removes the
doubt whether the 2-part of q − 1 could carry pretentious characters of order > 1/ε.

**D12 (MINOR, optional) — S is stated more uniformly than used.** S quantifies over all y with P(y) ≤ x^{1/2}, but Thm 4.2
uses one y = y(x) (inverse of x = C₀φ(8P(y))² log⁴p, i.e. log x = (2 + o(1))y) and only q ∈ (x/2, x]. *Repair:* record the
minimal form "for y = y(x) with x ≍ P(y)²·exp(O(y/log y)) and q ∈ (x/2, x]" next to the uniform one; the weaker statement is
the one whose plausibility matters.
