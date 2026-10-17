# R269 — hostile review of O256 (BALANCED_LATTICE.md, checkpoint 1 incl. R-O256 repairs 1–9)

Reviewer: R269 side agent (branch side-agent/review-balanced-lattice, merged side-agent/balanced-lattice at a5cf0e51).
Scope: BALANCED_LATTICE.md §§1–7, memos BRAINSTORM/z27_*.md, scripts/z27_{dual,eqcheck}.py, data/z27/, AGENT_REPORT_O256.md.
From-scratch scripts: scripts/review_r269_*.py (none reuse the author's code). Sources/ contains none of Banaszczyk 1993,
Serre 1981, Schinzel 1977: citation checks below are from the reviewer's knowledge of the statements and are flagged as such.

**Repairs applied (author quiet ≥ 2 h at review end):** BALANCED_LATTICE.md, marked "(R269 repair)", for D1, D3, D6, D7, D8(i,iii), D10,
D11, D13, D14, D16, D18, D19; BRAINSTORM/README.md z27 row (D17); AGENT_REPORT_O256.md SHARP 2 wording (D14). Not applied
(optional): D2, D4, D5, D8(ii) (constants), D9, D12, D15, D20.

## Overall verdict

**No FATAL and no MAJOR defect.** Every PROVED/CONDITIONAL claim survived a from-scratch re-derivation; the exponents 13/2
(GRH + EQ) and 9/2 (GRH + S) are correct as stated (with an o(1) of size O(log₄p/log₃p), D9); EQ and S are precise, p-free
(S also class-free), and not false for any trivial reason I could find (Brun–Titchmarsh regime, Chebotarev families of
Prop 5.2 type, extreme class a ≡ 1 (mod P)). All §6 EVIDENCE that I re-ran reproduces — the EQ tables at y = 7 and y = 11
exactly. Labels are honest ("bounded cap is not ES" is stated four times; no ES claim). 20 MINOR defects, mostly wording,
statement hygiene and citation precision (D1, D3, D7, D10, D11, D13, D14, D16, D17, D18 should be repaired; the rest optional).

## Summary verdicts (claim by claim)

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
| Prop 5.1 (narrowed) | SOUND | trivial size statement (2^k = P^{o(1)} ≪ \|U_q\| ≍ x ≥ P²) correctly labelled; the counterexample to the unnarrowed version re-verified from scratch: (11/409) = −1, K = (409 + 11)/4 = 105, t = −105 ≡ 5 (11), W₀ = {3^{2j₁}5^{2j₂}7^{2j₃}} = {1, 3, 4, 5, 9} = U₁₁ |
| Barrier screen §5 | SOUND | B5/T1: (q/m²) = 1 for q ∤ m, so no forced windows at squares — correct and algebraic; B2 handled by Prop 5.1 |
| §6 ν statistics | SOUND-AFTER-REPAIRS (EVIDENCE) | reproduced from scratch (600 q, k = 3; 400 q, k = 4); the 1 % quantiles quoted must be conditioned on 𝔻_min > 0 (D13) |
| §6 order statistics | SOUND (EVIDENCE); wording (D14) | reproduced: k = 3: ord = N 0.78 (random 0.75), ≥ N^{0.9} 0.89 (0.88), P⁺(N) \| ord 0.995 (0.997); k = 4: 0.76 (0.80), 0.86 (0.88), 0.995 (0.995); ≤ N^{1/2}: 0 resp. 0.25 % |
| §6 per-class ν (mod 840) | SOUND (EVIDENCE) | reproduced: q ≤ 3·10⁵ (6493 q from q = 11; the author's 6450 start at ≈ 10³): min over classes of the best ν = 1.481, median 1.572 (author 1.481 / 1.575); 29 classes have a degenerate q |
| §6 EQ at y = 7 (mod 840) | SOUND (EVIDENCE), reproduced exactly | from-scratch run over all 19 609 q ≡ 3 (8) in [10³, 10⁶]: Bad₁ counts 250 / 1272 / 3463 and χ² 49.5 / 28.0 / 29.8, full set 653 / 1670 / 3848, χ² 213.9 / 96.1 / 64.7 — identical to data/z27/eqcheck_y7.txt; my permutation p (1000 perms) 0.34 / 0.97 / 0.87 and 0.001 / 0.001 / 0.006 (D15) |
| §6 EQ at y = 11 (mod 9240) | SOUND (EVIDENCE), reproduced exactly; one follow-up (D19) | from scratch, all q ≡ 3 (8) ≤ 2·10⁶ (37 259 incl. 42 q < 10³ that carry no events): Bad₁ 72 / 653 / 2513, full 310 / 889 / 2747, χ² 543.6 / 474.2 / 405.6 — identical to the author's; permutation p 0.034 / 0.455 / 0.937 |

**D19 (MINOR, evidence follow-up) — the marginal y = 11 cell is the extreme class q ≡ 1 (mod 1155).** The p = 0.033 at
t = 0.3 comes entirely from class 6931 mod 9240, the unique class with q ≡ 1 (mod 3·5·7·11): 3 of its 66 primes are in Bad₁
(4.5 %) against 69/37 193 (0.19 %) elsewhere (q = 1 448 371, 1 623 931, 1 753 291; two minimisers of order N, one of order
1045 = 5·11·19 with ψ(g₅) = ψ(g₁₁) = 1). This class matters conceptually: in Thm 4.1 the class is −p mod 8P, and for
p ≡ −1 (mod P) every candidate window has P | N, i.e. the Frobenius-visible smooth part of N is ≥ P ≍ √x/log²p — the regime
farthest from Prop 2.2's "large rough part". Stratifying by w := #{ℓ ∈ S : ℓ | N}: at y = 7 there is no trend in Bad₁ (rates
0.0137 / 0.0126 / 0.0119 / 0.0096 for w = 0..3 at t = 0.3); a pre-specified re-test of class 6931 vs a w = 0 control class
(3467 mod 9240) on fresh primes q ∈ (2·10⁶, 8·10⁶] gives Bad₁ 0/202 vs 1/198 (t = 0.3), 1/202 vs 7/198 (t = 0.5),
9/202 vs 19/198 (t = 0.7): no enrichment — the cluster is a fluke (look-elsewhere probability that some class of 480 gets ≥ 3
at mean 0.15 is ≈ 0.25). *Repair:* add this to §6 and name the class a ≡ 1 (mod P) as the natural worst case for EQ in any
future test.

**D20 (MINOR, informative) — Hypothesis S is stated at a threshold with a factor ≈ k^k of unused random-model room.** Under
the uniform model the expected #Bad₁(ε) ∩ [1, x] is ≈ x²(2ε)^k/(4ζ(k)k! log x) (± pairs, primitive vectors). At
ε′ := (k/2e)·x^{−3/(2k)} this is ≈ x^{1/2}/(√k log x) — still inside S's allowance — and gives 1/ε′ = y^{2+o(1)}, hence
L = k^{3/2}/ε′ = y^{7/2+o(1)}; with an ℓ^∞ transference of constant O(1) (numerically μ_∞·𝔻_min ≤ 1.11, D2) it would be
y^{2+o(1)}, exactly Cor 4.4's random-lattice (log₂p)^{2+o(1)}. So "S is the random-model prediction, with room" is right, and
the exponent 9/2 reflects the chosen ε and the k^{3/2} transference, not the random model. *Repair (optional):* add this
remark after Thm 4.2 (no change to the theorem).
