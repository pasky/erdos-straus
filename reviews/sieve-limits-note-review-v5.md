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
* **Lemma 14.15 (residue concentration) — SOUND.** D=1 in Lemma \ref{lem:RM}'s description of 𝓡(M)
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

## Defects
(in progress)
