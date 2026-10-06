# Review R62 of EXCEPTIONAL_LARGESIEVE4.md (hostile reviewer, branch side-agent/review-ls4)

Reviewed: EXCEPTIONAL_LARGESIEVE4.md at side-agent/hrough 1314818.
From-scratch scripts: scripts/review_ls4_*.py.

## Verdicts (in progress)

| claim | verdict |
|---|---|
| Lemma 1.1 (damped-collision reduction) | SOUND (re-derived; brute-forced) |
| Cor 1.2 | SOUND |
| Lemma 2.1 (tilted pair law) | SOUND (re-derived; identity verified in exact arithmetic) |
| Lemma 3.1 (pivotal bound), Lemma 3.2 | SOUND (3.2 brute-forced for Q < 400) |
| Prop 4.1 ("(B) is free") | SOUND |
| Thm 4.2 (cap ⟸ (A*)) | SOUND as an implication; labelled honestly |
| Lemma 5.1 (pinned pivotal bound) | SOUND (re-derived; brute-forced on capped, conditioned prime-power toys) |
| Thm 5.2 (residue-sparse mixtures) | SOUND (inputs as LS3 Thm 3.1: K2 (Q1)–(Q4), ElT for Case A); MINOR D1 |
| Cor 5.3 (small-height classes) | SOUND (brute-forced counts and examples) |
| §3.2 (CC), structured example | Assessment/CONJECTURE correctly labelled; MINOR D5 in the example |

**Overall: no FATAL, no MAJOR.** Five MINOR defects (D1–D5), all wording /
bookkeeping. The new PROVED content (Lemma 5.1 ⇒ Thm 5.2 ⇒ Cor 5.3, with
Thm 4.2 + Prop 4.1 as the engine) survives a line-by-line check. In
particular it closes LS3 review D6(c) (`𝒜_c ≠ ∅`) for the families it
covers, because `Q'_c(G_{B_c}) ≥ 1/2` forces a non-empty fibre.

## Re-derivations

**Lemma 1.1.** Σ_{den θ | M_S}|σ̂|² = M_S Σσ_S² = E Π_{ℓ∈S}(1+h_ℓ); Möbius over
T ⊆ S gives P_S = E Π_{ℓ∈S}h_ℓ = Σ_{supp θ=S}|σ̂|² ≥ 0. Then
Σ_θ|σ̂|^{2+2β} ≤ Σ_S w_S P_S = E Π(1+w_ℓh_ℓ), and
1+wh = (1−w)+w·ℓ^E 1[x_ℓ=y_ℓ] expands to E_T 𝓡_2(σ_T). Correct; note
𝓡_p(σ)=Σ_θ|σ̂(θ)|^p incl. θ=0 (term 1), consistent with LS3.

**Lemma 2.1.** E[ℓ^E1[x=x']|past] = U(F^c∩F'^c)/((1−p)(1−p')),
η = (U(F∩F')−pp')/((1−p)(1−p')): checked. Z_ℓ=(1+wh)/(1+wη) is a
martingale-ratio density, Π(1+wη) predictable ⇒ identity. Inflation:
Σ_{a'}k'(a')(1+wh(a,a')) = 1−w+wℓ^E k'(a) ≤ 1/(1−p'): checked.

**Lemma 3.1.** Standard Efron–Stein/Walsh expansion; the B ≠ S terms die
because χ has a mean-zero factor e(c_ℓθ_ℓ) independent of the rest.
Pairing A ↔ A∪{ℓ} when ℓ not pivotal: correct (pivotality is per
realization of (c,c',π), which is what the bound uses).

**Prop 4.1.** E_T𝓡_2((σ_B)_T) = E_{Q'⊗Q'}[1_G(x)1_G(x')Π(1+wh)]/Q'(G)² (Lemma 1.1
identity applied to σ_B). Inserting the path functional Φ = 1_G⊗1_G in the
tilting is legitimate (dQ/d(Q'⊗Q') = ΠZ_ℓ, and Π(1+wη) is a path
functional). For the capped rule `1+η = ℓ^E Σ_a k k' ≤ ℓ^E max k = (1−p̃)^{-1}`
(heavy: k = U, p̃ = 0, η = 0 exactly), so η ≤ 2p̃(x) as p̃ ≤ δ ≤ 1/2; on
G_B(x), Π(1+wη) ≤ e^{2B}; Q is a probability, Φ ≤ 1. Correct. (Remark: with
w ≡ 1 one even has the pointwise `M σ_B(x) ≤ e^{2B}/Q'(G)`, so the result is
elementary; that is a feature, not a defect.)

**Thm 4.2.** Checked against LS3 Thm 1.1 (needs π_s(c) ≤ ρ/M_s and π_c a
probability on 𝒜_c — satisfied: σ_c lives on G_{B_c} ⊆ 𝒜_c, non-empty) and
LS3 Lemma 2.1 (any z-smooth event E with Q'(E) ≤ 1/8; here E is
c-measurable: E₀, {leak_c > 1/4}, {m_c > 32J}). Leak above z: on light
steps the plain rule never enters F_ℓ, so E_c leak_c ≤ Σ_{ℓ>z}E[p_ℓ1{heavy}]
≤ Σ ℓ^{1/2}E p_ℓ² ≤ C z^{−1/4}(log z)^c by (Q2) — fine. Off E:
Q'_c(G_{B_c}) ≥ 1 − 1/4 − 1/8; (A*) ⇒ (A_w) with w_ℓ = (Kℓ^{−γ})^{2β} ≤ ℓ^{−γβ} < 1;
Lemma 1.1 + Prop 4.1 ⇒ log𝓡 ≤ 16m_c + log 4 ≤ 512J + log 4. J: K^{2β} ≤ z^{γβ}
= e^γ, α = 2βγ, α^{−3} = (log N)^{3/4}/(8γ³); partial summation as LS3 Thm 3.1
(reviewed SOUND). The 16𝔐(z) term has no γ^{−3} but γ ≤ 1 so it is absorbed.
The statement is an implication from (A*) in the header, the summary row
and the report; (A*) is nowhere claimed. Honest.

**Lemma 5.1.** Pinned representation: given coins for q ∉ S, the outside
path is a deterministic function of v and Q'(x_S = v, G) = E_coins[1_G
Π_{ℓ∈S}k_ℓ(v_ℓ|past)] — correct (coins realise the outside step laws
independently of v). 0 ≤ Φ ≤ Π(1−δ_ℓ)^{−1}. The Efron–Stein pairing step
is the same as Lemma 3.1 with Φ real and bounded. Pivotal ⇒ residue: if
v_ℓ, v'_ℓ ∉ R_ℓ then for EVERY A ∌ ℓ the two pinned paths agree before ℓ;
at ℓ, F̃_ℓ (⊆ R_ℓ, and = ∅ if heavy) and hence the factor agree; after ℓ no
class through ℓ is ever matched in either path (its ℓ-component lies in
R_ℓ), so all activated sets, light/heavy flags, coin outcomes, later
S-factors, avoider membership and Σwp̃ agree. I checked the "every A"
quantifier and that R_ℓ must be independent of (v, v', outside coins) —
it is (deterministic, or c-measurable in Thm 5.2). Bound
`Q'(G)^{−1}·2^{|S|}·Π(1−δ)^{−1}·Π2U(R_ℓ)` = stated. Correct.

**Thm 5.2.** In the fibre at c the classes through a rough ℓ are those of
𝔊₂ (⊆ Res_ℓ(𝔊₂)) and those of 𝔊₁ with rough prime ℓ and smooth part
matched by c, which are exactly F^r_ℓ(c) (top prime ℓ, cofactor z-smooth).
U(F^r_ℓ(c)) ≤ p_ℓ(x) pointwise for x with smooth part c, so
Q'(E₁) ≤ Σ_{ℓ>z}ℓ^{1/2}E p_ℓ² as stated. Constants: 2Π16ℓ^{−γ'} ≤ Π32ℓ^{−γ'},
K = 32 ≤ z^{γ'/2} for N ≥ N₀(γ) (see D1). Correct.

**Cor 5.3.** ℓ > z > H, so −r/s mod ℓ is defined; ≤ (H+1)H ≤ z^{1/2}
projections mod ℓ; a class mod ℓ^v lies in its class mod ℓ, so
U(Res_ℓ) ≤ z^{1/2}/ℓ ≤ ℓ^{−1/2}; then γ' = min(1/2, 1/4) = 1/4. The listed
examples are H-small: (a,D) is −(4D+a)/1 (K2 Def 2.0), Case A is −1/m with
m | 4d+1 coprime to G = 4rh, ℛ(M)-classes −4, −1 (D = A), −1/4 (D = A²),
−4d, −1/(4d) (D = A²/d), −d (D = dA, d | A). All brute-forced.

## Numerical checks (from scratch; EVIDENCE)

* `scripts/review_ls4_toy.py` (40 random toy families, coordinates
  ℤ/9×ℤ/5×ℤ/7×ℤ/11 or ℤ/5×ℤ/7×ℤ/11×ℤ/13, classes with prime-power
  components, random caps δ_ℓ ∈ {1/6,1/3,1/2}, half of them residue-sparse;
  σ = Q'(·|G_B) with B the median damped mass, and σ = Q'(·|avoider)):
  - Lemma 1.1: identity Σ_S w_S P_S = E_T𝓡_2(σ_T) (rel. err < 1e−9) and the
    inequality 𝓡_{2+2β} ≤ E_T𝓡_2(σ_T) for w the smallest (uniform or random
    direction) weights satisfying (A_w); max ratio 0.9986 (nearly tight, never
    violated);
  - Prop 4.1: E_T𝓡_2(σ_B) ≤ e^{2B}/Q'(G_B)² in all cases;
  - Lemma 5.1: |σ̂(θ)| ≤ Q'(G)^{−1}Π4U(Res_ℓ)/(1−δ_ℓ) for every θ ≠ 0 (both G);
    max ratio over non-trivial bounds 0.243;
  - Lemma 2.1: E_{σ⊗σ}Π(1+wh) = E_QΠ(1+wη) **exactly** (Fractions, recursion
    over prefix pairs, always-forbid law on 3 coordinates), and the
    inflation bound P_Q(x_ℓ=a|past) ≤ U(a)/((1−p)(1−p')(1+wη)) at every node.
* `scripts/review_ls4_res.py`: Lemma 3.2's divisor criterion for all units
  v mod Q, Q ≡ 3 (4), Q < 400 (16226 pairs); Cor 5.3 counts for
  z ∈ {16,…,4096}, 200 primes above each z, including ℤ/ℓ² classes; the
  H-small examples in ℛ(M) for all M < 4000; Rem 5(c): projections mod ℓ of
  ℛ(ℓq), q < 3000, cover all ℓ−1 nonzero residues for ℓ = 11, 19, 23
  (so (RS_γ) genuinely fails for generic ℛ — the author's "open" part is
  real).

## Defects

**D1 (MINOR, hidden quantifier; Thm 5.2 statement and Thm 4.2 statement).**
Both theorems quantify over `γ ∈ (0,1]` but the proofs need N ≥ N₀(γ):
Thm 5.2 needs `K = 32 ≤ z^{γ'/2}`, i.e. `(log N)^{1/4} ≥ 2 log 32/γ'`, and
Thm 4.2 needs `1 ≤ K ≤ z^{γ/2}` to be non-empty for the K one has (plus
"Q'(E) ≤ 1/8 for N large"). For γ ≲ (log N)^{−1/4} the conclusion is
vacuous anyway (γ^{−3}(log N)^{3/4} ≥ log N), so nothing is lost, but say
so. *Repair:* add "for N ≥ N₀(γ) (N₀(γ) = exp(Cγ^{−4}) suffices)" to both
statements, or note that the bound is trivial below that range.

**D2 (MINOR, statement wording; Lemma 5.1).** "any sets `R_ℓ ⊇
F̃_ℓ`-candidates as below" is garbled, and the one hypothesis that really
matters is only implicit: R_ℓ must not depend on the pinned values
(v, v') nor on the outside coins (otherwise the product over ℓ ∈ S of
P({v_ℓ,v'_ℓ} ∩ R_ℓ ≠ ∅) is not justified). *Repair:* "Let R_ℓ ⊆ ℤ/ℓ^{E_ℓ}
(ℓ ∈ S) be fixed sets (in Thm 5.2: c-measurable) containing, for every
class of the (fibre) family with ℓ in its modulus, its class mod
ℓ^{v_ℓ(G_C)}. Then …" (this also gives F̃_ℓ ⊆ R_ℓ automatically).

**D3 (MINOR, stale text; header, §0 title, "Plan (not yet results)").**
"Status: in progress", "Summary (so far)" and the Plan section are stale.
The Plan's §4 bullet ("the class −4 mod pM' contributes one residue per ℓ,
and the damping w_ℓ cuts the Σ1/ℓ sum to O(1)") describes a mechanism that
is *not* the one used (Cor 5.3 goes through Lemma 5.1's deterministic
residue sets, not damping), and the section numbers in the Plan do not
match the document. *Repair:* delete the Plan section or mark it
historical; update status.

**D4 (MINOR, label provisos; §0 rows for Thm 4.2 and Cor 5.3).** Thm 5.2's
row carries "(K2 inputs; Case A via ElT)", but Thm 4.2 (uses (Q1)–(Q4),
i.e. the same inputs) and Cor 5.3 (a corollary of 5.2) are labelled bare
"PROVED (implication)" / "PROVED". *Repair:* append the same proviso
"(LS3 Lemma 2.1 inputs: K2 (Q1)–(Q4); Case A via ElT Prop 1.4)" to both rows
and to the Cor 5.3 heading.

**D5 (MINOR, Assessment text; §3.2 structured example).** The claim
"`|E_S|` stays `≤ τ(F²)^{O(1)}·|S|^{|S|}`" is wrong as written: with the
singleton moduli present every coordinate may independently be any of the
values −4d mod ℓ (d | F²/16), so `|E_S| = Π_ℓ #{−4d mod ℓ}` which is
`τ(F²/16)^{|S|}`, larger than `τ^{O(1)}|S|^{|S|}` when τ ≫ |S|. The
conclusion drawn (product constraints, per-prime probability `≤ τ/ℓ`) is
right with the corrected count. The "2^{Θ(|S|²)} minimal covers" count is
asserted without proof. *Repair:* replace by "`P(E_S) ≤ Π_{ℓ∈S}τ(F²/16)/ℓ`
(each coordinate must be some −4d mod ℓ)"; mark the cover count as
heuristic or give the construction.

**D6 (MINOR, inconsistency left by the self-review repair M1; Thm 4.2
Remark (c)).** Remark (c) still says "for supports of size
`≤ (1−2γ)log₂ z` the count is trivially within the slack (§3.2)", but the
repaired §3.2 says this holds only when *also* `2^{|S|}T_S ≤ z^{1−2γ}`, and
`T_S` (classes per modulus, ≤ τ(A_Q²) for ℛ) can exceed any power of z.
*Repair:* "…within the slack when `2^{|S|}T_S ≤ z^{1−2γ}` (§3.2)…". In the
same Remark (a), "far weaker than LS2's (H_LS∞)(b)" is a comparison, not a
theorem — tag it Assessment.

## Points checked and found fine (for the record)

* Thm 4.2 / 5.2 do not secretly rely on (CC) or (A*) for the families
  claimed: Thm 5.2 verifies (A*) completely via Lemma 5.1.
* No circularity: σ_c depends on (w, K, γ) through B_c, but (A*) is a
  hypothesis on these explicitly defined measures; in Thm 5.2 it is
  verified for exactly those measures (G_{B_c} is admissible in Lemma 5.1
  since Σwp̃ is a function of activated sets and light/heavy flags).
* LS3 review D1/D2 (overclaims about equivalence / mixed frequencies) do
  not propagate: LS4 claims only sufficiency and handles mixed
  frequencies through fibre measures σ_c with an explicit (A*).
* Lemma 3.1's "Moreover" clause and Lemma 3.2 (incl. the converse
  direction: D = A²/s̃ gives −4D ≡ 16A²v ≡ v) — fine.

## Verdict

SOUND-AFTER-REPAIRS only in the cosmetic sense: D1–D6 are all MINOR. The
document's PROVED labels are earned (modulo the inherited K2/ElT inputs,
D4). Ledger entry can proceed after D1, D2, D4, D6 (one-line fixes).
