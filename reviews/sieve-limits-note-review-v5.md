# Referee report R65 — paper/sieve-limits-note.tex, version 5

Branch reviewed: `side-agent/sieve-paper-v5-2` @ bdb61bc (merged ff into `side-agent/referee-sieve-v5`).
Referee: R65 (hostile). Scope: everything new/changed v4 → v5 (diff 66191c6..bdb61bc).

## Compilation
pdflatex ×3 in a clean dir: 71 pp., no undefined refs/citations, no multiply-defined labels;
one pre-existing overfull hbox 1.29pt (lines 3818–3825). OK.

## Verdicts per claim

### §14.5 Smooth–rough splitting
* **Thm 14.12 (smooth–rough splitting) — SOUND.** Re-derived: HY on Z/M_s with
  f = M_sπ_s(c)π̂_c(θ_r) gives Σ_{θ_s}|π̂|^{p'} ≤ (Σ_cπ_s(c)(M_sπ_s(c))^{p−1}|π̂_c|^p)^{p'/p}
  ≤ ρ^{(p−1)p'/p}(E|π̂_c|^p)^{p'/p} ≤ ρE|π̂_c|^{p'} (Jensen, p'/p ≥ 1; (p−1)p'/p = 1).
  Hölder with exponents p'/2, q=(1+β)/β and Σw^q ≤ N^{1−q} gives F_w ≤ (R/N)^{1/(1+β)}; then
  log(N/B) ≤ (β log N + log R)/(1+β) ≤ β log N + log R. From-scratch random check
  `scripts/review_r65_smoothrough.py` (3000 instances, (a) HY+Jensen, (b) Hölder, (c) per-prime
  bound Σ_{a≠0}|φ|^{p'} ≤ g^{1+2β}): worst ratios 1.000000 / 0.976 / 1.000000 (equality cases
  attained, never exceeded).
* **Lemma 2.1 of LS3 in prose (density of π_s) — SOUND** as a transcription (inputs (Q1)–(Q4) of
  KA2; R59 D6(a) about Q₀ ∤ M_s is not mentioned in the paper but is harmless by marginalisation —
  see minor point).
* **Thm 14.13 (rough-slice mixtures) — SOUND (given KA2 §§2–4).** Author's check point 1
  confirmed: 𝔐(y) in KA2 §3 is a sum over the *universe* 𝔘 of all classes of the four types with
  W < P(G) ≤ y, no size bound on G (only y-smoothness), and (Q1) holds for every family ⊆ 𝔘; the
  J-integral α∫_z^∞𝔐(y)y^{−1−α}dy ≪ α^{−3}(log 1/α)^3 (t = log y) is therefore uniform in moduli
  size. Chebyshev for E₁ (ℓ^{2−2κ}Ep_ℓ² = ℓ^{1/2}·ℓ^{−7/4+o(1)}, summable from z) and Markov for E₂
  are correct; the constant 64 = 4·16 matches the per-prime bound 4pℓ^{−α} (checked in (c)).
* **Hyp 14.14 (H_rough) — labels SOUND** (conjecture; sufficiency only, R59 D1 respected). See
  minor point on the added "primes ≤ N^{O(1)}".
* **Lemma 14.15 (residue concentration) — SOUND.** D=1 in Lemma 2.2's description of 𝓡(M)
  gives −4; Σ_{M'≤X, P⁻(M')>z, one class mod 4}1/M' ≍ log X/log z by Mertens/Buchstab
  (needs X ≥ z^{1+ε}, true for X = N^A).

### §14.6 Damped collisions
* **Lemma 14.16 (damped-collision reduction) — SOUND.** Re-derived: group θ by S = supp θ;
  Σ_{supp θ=S}|σ̂|² = E∏_{ℓ∈S}h_ℓ ≥ 0 (CRT + Σ_{a≢0 (q)}e(at/q) = q1[q|t]−1), so
  R_{2+2β} ≤ Σ_S∏_{S}w_ℓ·P_S = E∏(1+w_ℓh_ℓ) = E_T R_2(σ_T). From-scratch exhaustive check
  (`scripts/review_r65_damped.py`, 400 random σ on Z/M, M ≤ 90 with 2–3 prime-power factors, w
  chosen to satisfy the hypothesis): two-copy identity error ≤ 7e−15, max ratio LHS/RHS = 1.000000
  (equality only in degenerate cases).
* **Collision bound e^{2B}/Q'(G_B)² (LS4 Lemma 2.1/Prop 4.1), in prose — transcription SOUND;**
  not re-derived from scratch beyond reading LS4 §§2,4 (needs the KA2 sequential law).
* **Thm 14.17 ((H_rough) from sup decay) — SOUND as an implication; label correct** ("proved
  implication", (A*) open; not an unconditional all-level cap — the abstract/intro must keep this,
  see below). Checked: w_ℓ = (Kℓ^{−γ})^{2β} ∈ [0,1] since K ≤ z^{γ/2} < ℓ^γ; K^{2β} ≤ e^γ; α = 2βγ
  gives J ≪ γ^{−3}β^{−3}(log(1/(βγ)))³, and under N ≥ exp(Cγ^{−4}) one has
  log(1/(βγ)) ≤ ½ log log N + O(1), so the stated uniform-in-γ form is correct (LS4's caveat
  "γ fixed or γ ≥ (log N)^{−o(1)}" is unnecessary under N₀(γ)). Constant 512 = 2·8·32 ✓.
  N₀(γ) = exp(Cγ^{−4}) is what K = 32 ≤ z^{γ'/2} needs in Thm 14.18 ✓.
* **Lemma 5.1 of LS4 (pinned pivotal bound), in prose — transcription SOUND** (read LS4 §5; the
  argument "both pinned values avoid R_ℓ ⇒ ℓ not pivotal" is correct given F̃_ℓ ⊆ R_ℓ on every path).
* **Thm 14.18 (residue-sparse mixtures; H-small corollary) — SOUND.** U(R_ℓ) ≤ 2ℓ^{−γ'} ⇒ per-prime
  factor 4·2/(1−½) = 16, global Q'(G)^{−1} ≤ 2 absorbed at one prime ⇒ K = 32 ✓. H-small:
  (H+1)H ≤ z^{1/2} for H ≤ z^{1/4}/2 ✓ (in fact gives γ = 1/2; γ = 1/4 stated is weaker, fine).
  From scratch: for all M ≡ 3 (4), M < 400, the listed classes −4, −1 (D=A), −1/4 (D=A²),
  −4d, −1/(4d) (d | A², d ≤ 5) lie in 𝓡(M) = {−4D : D | A²}, and all 9752 n < 1200 in 𝓡(M)-classes
  have a 4/n decomposition (forcedness sanity check).

### §14.9 Hybrid methods
* **Def 14.28 (SPW, ex-hypothesis) — SOUND** (now correctly a definition; no remaining
  "Hypothesis~\ref{hyp:SPW}" text; label name `hyp:SPW` is cosmetic only).
* **Thm 14.30 (fixed-σ SPW fails) — SOUND.** Re-derived completely: k ∈ [m₀,M] divides L_M | e so
  e/k ≤ ⌊N/2⌋ and ρ̂(k) is pinned; T = (ρ−1_W)∗F_M has degree < m₀ and |T| ≤ 1 on Z/e;
  sampling+Bernstein gives ‖T‖_∞ ≤ (1−πm₀/e)^{−1}; normalised Fejér tail beyond r is
  ≤ e/(2(M+1)r) (sin πx ≥ 2x), and both tails enter, giving σ − e/((M+1)r); the wrap-around
  condition e > N+2r is exactly r < ((C−1)N−1)/2. Optimisation gives 4√(πm₀/(M+1)). (P3) unused ⇒
  "whatever Δ₀" ✓.
* **Exact certificates σ ≤ 72/185 (N=300, e=630) and σ ≤ 0.381133 (N=1150, e=2310) — REPRODUCED
  from scratch** (`scripts/review_r65_spw_cert.py`: LP on Z/e, dual rounded to rationals,
  weak-duality bound σ ≤ 1 − Σ_W g/Σ g⁺ evaluated in exact arithmetic): 72/185 exactly and
  0.3811324…; LP optima 0.389189 / 0.381132. (For these e the only divisor e' > CN is e itself.)
* **Lemma 14.31 (weak SPW suffices) — SOUND, with one presentational defect (D-H1 below).**
  Re-derived: R₁ satisfies (P1) (both parts have the window profile), (P2) (a class of modulus
  > CN > N meets W in ≤ 1 point: ≤ 1 − 1/(2K) + (1−η)/(2K) on full, ≤ ½ ≤ 1 − η/(2K) on missing),
  (P3) with Δ'/(2K); then t, s₀ ≍ η/K, log(1+Δ(1+c)) ≤ log(1+c) + log(1+Δ'/K) + O(1) ✓;
  s₀ ≥ N^{−A₁} ⇔ η/K ≥ 4N^{−A₁} ✓. The removal of Thm 14.27's hypotheses t,1/Δ ≥ e^{−S_A} is
  plausible (if log(1/t) or log(1+Δ) exceeds log N the bound is trivial) but see D-H1.
* **Hyp 14.32 (weak SPW) — label open ✓;** "Thm 14.30 forces only η/K ≪ (log N)^{−1/2}" ✓ (apply
  Thm 14.30 to R₁ with σ = η/(2K)).
* **Thm 14.33 (K-free edge bound) — SOUND.** Re-derived: |ρ̂(k)| ≤ total mass N (P1 with d=1),
  so |T'| ≤ (4πN/e²)·m₀(m₀−1) (paper's m₀(m₀+1) is a harmless over-estimate); the unbounded
  off-W mass enters only via F(j) ≤ e/(4(M+1)j²) at distance > r, giving eN/(4(M+1)r²) ✓;
  r = ⌈NM^{−1/3}⌉ balances to M^{−1/3} ✓, uniform in K ✓.

### §18 One sieve limit behind both ceilings
* **Thm 18.1 (two-sided order-k limit) — SOUND as a transcription of CU Thm 4.1** (constants
  0.6P−1, e²P, 2e^{−P} match; p_b ≤ 1/4 gives r* ≤ 1/3 for the planting condition). From-scratch
  LP check, symmetric case (`scripts/review_r65_twosided.py`; symmetrisation over hit-indicators
  and permutations preserves 𝒱_k and the constraints): (L−) never violated (n,p) ∈ {(60,¼),
  (100,0.15), (200,0.05), (400,0.05)}; Bonferroni signs (Q_k ≥ F even, ≤ F odd) and the (U+)/(L+)
  bounds checked exactly in rationals for n = 40, 120. The float-LP first positive-minorant order
  (7 at n=40,P=4 — equal to CU §4.4; 17 vs CU's exact 15 at n=40,P=8, i.e. my float tolerance
  1e−9 overestimates the threshold) is consistent with k ≍ P; no contradiction with the
  "≈2P" EVIDENCE.
* **CU Prop 4.2 in prose — SOUND transcription** (level log D ≤ c𝓛⁴; ineffective; given TQ and
  O14 Thm 1.3; "removes a factor log 𝓛 from O14 Thm 4.5" ✓ — CU also notes it *replaces* O14's
  inputs (G)/effective Page/fundamental lemma by BV/BT/Shiu; the paper says "given \cite{TQ}", OK).
* **Thm 18.2 (ES sieve limit) — SOUND as a conjunction; labels honest.** (1) upper bound =
  Thm 10.12 (noBcap = KA3 Thm 4.1, as CU's KARY3 Thm 4.1) ✓; (2) ✓; (3) proved within the stated
  scopes, Assessment outside ✓; the a/(a+1), 1/(a+1) extrapolation CONDITIONAL ✓; the reviewer's
  caution "(U−) for the subfamily does not bound majorants of the full avoider" is stated ✓;
  Remark 4.4 of CU reproduced accurately.
* **π(N) form (CU Thm 2.1/Prop 3.1), Cor 3.3 — transcription SOUND**, "a reproof, not an
  improvement" ✓.
* **Pointwise background + OMEGA16 pointer — SOUND-AFTER-REPAIRS** (minor scope/label points
  D-U1, D-U2 below).

### Abstract, intro, §§16–17, numbering
* Numbering after renumbering: all v5 labels resolve (aux: 14.12–14.18, 14.27–14.33, 18.1–18.2,
  §§14.5, 14.6, 14.9, 16, 17, 18); no hard-coded theorem numbers in new text; the O65 change list
  numbers match the PDF. "Twenty-five documents" now matches the list (25) ✓.
* Abstract/intro/§16/§17 propagation of LS3/LS4/SPW/SPW2/CU: consistent with the theorems, with the
  wording points D2, D3, D7 below. Thm 14.17 is presented everywhere as an implication from (A*)
  (abstract: "reduced to a sup-decay hypothesis"; intro: "\lab{proved} implication") ✓; weak SPW
  is open everywhere ✓; Thm 18.2 is "proved within the stated scopes" in the intro ✓.

## Defects

No FATAL and no MAJOR defect found. All numbered points are MINOR.

**D1 (MINOR, presentation; author's check point 2). Lemma 14.31 uses a stronger Thm 14.27 than the
one stated.** Lemma 14.31 allows η/K down to 4N^{−A₁}, so t ≍ η/K can be far below e^{−S_A},
violating Thm 14.27's stated hypothesis "t, 1/Δ ≥ e^{−S_A}"; the proof of Lemma 14.31 removes this
hypothesis in passing. I checked that the removal is correct: in the non-trivial case
(1+Δ(1+c))B < tN ≤ N one gets s₀W⁺_{>CN} < N, so the level bound does not involve t or Δ, and t, Δ
enter only the final line. *Repair:* drop "t,1/Δ ≥ e^{−S_A}" from Thm 14.27 (lines ≈3558–3560) and add
one sentence to its proof sketch ("in the non-trivial case W⁺_{>CN} ≤ N/s₀, independent of t, Δ"),
citing \cite[Rem. after Lemma 1.1]{SPW2}; then Lemma 14.31's proof can just cite Thm 14.27.

**D2 (MINOR, overclaim echo of R53 M1). "Exact requirement" without "for this route".** The abstract
(l. ≈75: "with an exact requirement on its margins") and §16 "New in version 5" (l. ≈4329: "the exact
weak requirement that replaces it") drop the qualifier that the body (l. ≈3697–3700) and intro item 6
carry. Lemma 14.31 is sufficiency only. *Repair:* "with a requirement on its margins that is exact
for this route" / "…that replaces it as the target of this route".

**D3 (MINOR, hidden parameter). The residue-sparse cap depends on γ.** Abstract l. ≈79–84 states
"saves at most O((log N)^{3/4}(log log N)^3) … and more generally whenever the classes with several
such primes are residue-sparse"; Thm 14.18 gives C γ^{−3}(log N)^{3/4}(log log N)^3 only for
N ≥ exp(Cγ^{−4}). *Repair:* "O_γ(…)" or "(RS_γ) with γ > 0 fixed" in the abstract and intro item 6
(the §16 item already has the factor γ^{−3}).

**D4 (MINOR, statement drift). Hyp 14.14 (H_rough) adds "primes ≤ N^{O(1)}".** LS3 §4's (H_rough)
has no such restriction, and Thms 14.13/14.18 (its proved cases) have none either. The added
restriction makes the hypothesis weaker, so it is not wrong, but the conclusion drawn ("a cap … over
every such mixture") is then only for such mixtures, and the reader may think 14.13/14.18 need it.
*Repair:* drop "with primes ≤ N^{O(1)}" (matching the source), or say explicitly it is this note's
restriction. Also add that the implication uses the density lemma (KA2 inputs), not Thm 14.12 alone.

**D5 (MINOR, undefined quantity). Lemma 14.15's "conditional mass at the residue −4 mod p".**
Not defined in the paper; in LS3 it is the deterministic sum m*(p,b) = Σ_{C∋p, b_C≡b (p^v)}p^v/G_r(C).
As written it reads like a probability under some law, for which "≍" would need an argument.
*Repair:* define m*(p,b) in one line before the lemma.

**D6 (MINOR, scope/label). OMEGA16 sentence in §18 (l. ≈4628–4635).** (a) "the heuristic truth is
1/3" carries no label — mark *Assessment*. (b) "EH-, GEH- and BV-type input … stays capped at 1/4":
O16 Prop 3.1 covers only Haar-centred error bounds for primes in progressions/characters of
moduli ≤ x — for GEH only its specialisation to primes in progressions, and not full GRH (O16
review R61 M1). *Repair:* "Haar-centred progression input (BV, EH(θ), the progression part of GEH;
not full GRH or GEH)". (c) O16 Thm 1.2 is conditional on LS *and* modulo Nair–Tenenbaum; say so.

**D7 (MINOR, wording). "Only residue-dense classes remain" (§17 (iii), §16 item 1, intro item 7).**
(RS_γ) is a property of the *union* Res_ℓ(𝔊₂) over all multi-rough classes, not of single classes:
many individually H-small classes with different (r,s) can make the union dense. *Repair:* "only
mixtures whose multi-rough part violates (RS_γ) for every fixed γ > 0".

**D8 (MINOR, citations; author's check point 3). Published inputs of §18 not in the bibliography.**
"Gallagher's 1970 theorem on primes in progressions" (Invent. Math. 11 (1970), 329–339) is not in
the bibliography and is easily confused with \cite{Gallagher} (larger sieve, 1971); Nair–Tenenbaum
(Acta Math. 180 (1998)) and the effective Page bound / fundamental lemma have no entries.
POINTWISE_OMEGA15 is cited as \texttt{} only, although Thm 18.2(3)'s scope rests on it; give it a
bib entry with its review (`reviews/pointwise-omega15-review.md`). O13 Thm 5.1 is also modulo the
internal OMEGA10 Thm 3.4 — "published inputs listed there" should say "published and internal
inputs". *Repair:* add the entries; one clause.

**D9 (MINOR, cosmetic).** (a) Def 14.28 keeps label `hyp:SPW` (harmless; rename to `def:SPW` if
convenient). (b) Thm 14.33's Lipschitz term has m₀(m₀+1); the derivation gives m₀(m₀−1) — the
stated bound is weaker and correct, no change needed. (c) Thm 14.18 with H ≤ z^{1/4}/2 actually
yields U(Res_ℓ) ≤ ℓ^{−1/2}, i.e. γ = 1/2; γ = 1/4 as stated is fine because γ' = min(γ,1/4)
anyway — a footnote would preempt the question. (d) LS3 review D6(a) (Q₀ ∤ M_s; take the
marginal) is not mentioned in the prose density lemma; one parenthesis would do.

## Points the author asked to be checked
1. Thm 14.13 "no bound on modulus size" — **confirmed** (𝔐(y) sums over the whole universe 𝔘 of
   y-smooth-topped classes, KA2 §3; (Q1) holds for every 𝔊 ⊆ 𝔘; the J-integral to ∞ is fine).
2. Lemma 14.31 vs Thm 14.27 hypotheses — the removal is **correct** but should be stated at
   Thm 14.27 (D1).
3. §18 published inputs not individually cited — **yes, should be fixed** (D8).

## Recommendation
**Accept after minor revision** (D1–D8; D9 optional). Every new v5 theorem was re-derived
(Thms 14.12, 14.13, 14.17, 14.18, 14.30, 14.33; Lemmas 14.15, 14.16, 14.31) and the cited-only
results were checked against their sources (LS3, LS4, SPW, SPW2, CU, O13/O14/O16 statements).
From-scratch scripts: `scripts/review_r65_smoothrough.py`, `review_r65_damped.py`,
`review_r65_spw_cert.py` (both SPW certificates reproduced exactly), `review_r65_twosided.py`.
Labels are honest: Thm 14.17 is an implication from the open (A*); weak SPW is open; Thm 18.2 is a
conjunction within scopes, Assessment outside; ES is nowhere claimed. The cap of Thm 10.12/main
theorem is unchanged, as stated.
