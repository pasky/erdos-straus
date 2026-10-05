# AGENT REPORT O30 (branch side-agent/haar-primes-2): Haar → primes

Deliverable: `POINTWISE_OMEGA8.md`, scripts `scripts/omega8_brw_check.py`,
`scripts/omega8_levels.py`, data `data/omega8/`.

## Result (checkpoint 1; needs hostile review)

* **Thm 4.3 (PROVED mod Thorner–Zaman + Elsholtz–Tao Prop 1.4):**
  `W(p) ≥ exp(c(log p)^{1/14})` for infinitely many Mordell-hard p;
  `log L_h(T) ≪ (log T)^{14}`. This replaces O4 Cor 3.1
  (`log₂p·log₃p/log₄p`) and reaches O4 §4.4's "third target".
* **Thm 4.4 (PROVED mod Thorner–Zaman only):**
  `log W ≥ (1/(2log2)−o(1))·log₂p·log₃p` (was `log₂p·log₄p/log₅p`).

## How

1. **Diagnosis (goal 1, §2; Assessment).** The Haar local lemma uses suppression:
   good configurations rarely contain partial clusters with large
   completion mass. Alternating expansions (PO Brun, O2 support
   truncation, O3/O4 levels) amplify on such clusters. That produces the
   codegree thresholds `(kL)^{−(i−1)}`, an unsolvable single-family Markov
   recursion, the levels, and the `(k−1)!`. Lemma 2.1 (locally minimal
   events) shows that the outer inclusion–exclusion needs no codegree
   input; all the trouble is in the neighbourhood factors.
2. **Construction (§3).** Bazzi's one-sided ℓ² sandwich in
   Razborov–Wigderson form:
   `B = 1 − Σ_i A_i(1−Σ_{j<i}A_ju_j)²` satisfies `B ≤ F` pointwise for
   any `u_j`, with `F−B = Σ_iA_i(Σ_{j<i}A_j(F_{<j}−u_j))²` (Lemma 3.1,
   brute-force checked). Take `u_j` = Efron–Stein truncation of
   `F_{<j}|_{E_j}`. Then the error is an Efron–Stein tail, and ℓ¹ mass
   and moduli are `e^{O(t𝓛)}` (Lemma 3.2). The twist follows as in O2
   (Lemma 3.3). Thm 3.4 feeds this into PO Thm 4.1.
3. **The tail (§4).** Encode each residue coordinate in
   `b≈2log₂T` bits (`π(u)=g_{⌊q·int(u)/2^b⌋}`; fibres are intervals, so
   unions of `≤2b` subcubes). The bad-indicator becomes a DNF of width
   `≤kb`. Håstad's switching lemma with the LMN argument then gives a
   Fourier tail `≤2·2^{−k_0}` beyond degree `2C_H·kb·k_0`, independent
   of the number of terms. Pulling back by conditional expectation keeps
   the junta size; the Haar/encoding density ratio is `≤e^{1/2}`
   (Lemma 4.1). So `t ≍ k𝓛(S+𝓛)`, polynomial, with no hypothesis.

## Self-review (deep reviewer subagent, round 1): no fatal; repairs applied

* MAJOR 1 (applied): Setting 3.0 needs single-value events; surviving
  atoms with vertex sets mod `ℓ^a`, `a<e_ℓ`, are split into full values.
  This preserves masses and F but gives `m≤T^{k+2}`; then
  `t=O(k𝓛(S+k𝓛))`, and Thm 4.3's `t≪𝓛^6`, `K,log Z≪𝓛^7` are unchanged.
* MAJOR 2 (applied): §2.3/2.4 "facts" were overstated (Markov gives
  upper bounds; completion mass alone does not give `e^{−M}`
  suppression). They are relabelled as Assessment/heuristic, and the
  counterexample is recorded.
* MAJOR 3 (applied): Lemma 1.1's "converse" was a statement about the
  certificate, not about p. It is reworded; constant fixed to 9/16.
* Minor (applied): Thm 4.4 asymptotics redone by monotone inversion;
  Thm 3.4 range `7≤z≤T^{1/3}` and `m=0`; the script now exits nonzero on
  failure.
* The reviewer independently confirmed Lemmas 3.1–3.3, 4.1 (width `≤kb`,
  restriction identity, pullback junta, density `≤e^{1/2}`), the
  precision chain, the extension to all integers, the auxiliary prime,
  and the final `log p=O(𝓛^{14})`.

## Things a reviewer should attack

* Lemma 4.1(b): constants of the switching lemma and LMN step (median
  argument), and whether the DNF width really is `≤kb` after the interval
  encoding (vertex sets that are unions of classes mod `ℓ^{e}` give many
  subcubes but the same width).
* Lemma 4.1(c): the measure change (`π_*` vs Haar) and Jensen.
* Lemma 3.2: the ℓ¹ bookkeeping of products of cells on overlapping
  coordinates (the `T^{|I∩J|}` inflation).
* Thm 3.4: is PO Thm 4.1 applicable verbatim (finite combination of unit
  cells, `gcd(d_i,Q)=1`, the auxiliary prime `ℓ_0` as in O4 Thm 2.1)?
  Is O2 Lemma 4.3 (I) valid for the iterated-quarantine Π (O2 Thm 11.3
  asserts it)?
* The twist (Lemma 3.3) for hypergraph events.

## Not done / scope

* The exponent 1/14 is not optimised. ES is not touched.
* §1 (budget lemma) and §2 are now mostly diagnostic. The old route's
  requirement `log K ≤ k^{O(1)}` is moot.
* No ledger or STATUS edits (parent's call). If the result survives
  review, these become obsolete as stated: DISCOVERIES (H)14 "proved rate
  remains Cor 3.1", STATUS's "for every fixed k, W ≥ (log p)^k", and O4
  §4.4.

## Round 2: parent's hostile reviews R30a, R30b (both SOUND, no FATAL/MAJOR)

Merged `side-agent/review-omega8a-2` and `side-agent/review-omega8b`
(reviews and scripts). All ten minor repairs are applied in OMEGA8:
* the `log Z` constant `2(3k+2t+1)𝓛` (D1/D2 of both reviews);
* "f|d_i" in Lemma 3.3, and `μ_ψ=E[Bψ]` justified (a-D2);
* LMN cited as O'Donnell Lemma 4.21 plus Kaas–Buhrman (a-D3);
* the Haar side quoted as `𝓛^7/log𝓛` (D4 of both);
* the Lemma 3.2 constant explained (a-D5);
* `B≤1[W>T]` needed only for n coprime to all `d_i` (b-D1);
* the auxiliary prime renamed `ℓ_aux` (b-D3);
* duplicates after splitting are kept (b-D5).
Phase 2 (exponent optimisation) follows in OMEGA8 §6.

## Phase 2: optimising the exponent (OMEGA8 §6; numbered §6 so that the reviewed §§1–5 keep their numbers)

* **§6.1 ledger.** Under ET, with `z=𝓛²`:
  * `S*≪𝓛^4log𝓛`, width `w=kb≍𝓛²/log𝓛`, degree `d≍w·S≍𝓛^6`;
  * `log M_1≍d𝓛` (Lemma 3.2), `log max d_i≍d𝓛`, `log Q_Π≍k²S*𝓛`;
  * so `log p≍K·log Z≍𝓛^{14}`.
* **Lemma 6.1 (PROVED).** Use the pulled-back Fourier truncation as
  `u_j`. Its spectral norm satisfies `Σ_{|S|<d}|ĝ(S)|≤2(4C_Hw)^d`, from
  `Σ_S p^{|S|}|f̂(S)| ≤ E 2^{DT(f_ρ)}` and Håstad. Products are expanded as
  bounded functions, so there is no `T^{junta}` overlap inflation. Hence
  `log M_1 ≤ 3log m+2d log(4C_Hw)+4`, and K loses a factor 𝓛.
* **Thm 6.3 (PROVED mod TZ+ET):** `W(p) ≥ exp(c(log p/loglog p)^{1/13})`;
  `log L_h(T)≪𝓛^{13}log𝓛`.
* **§6.4.** The bit width b≍𝓛 is the next loss. A q-ary decision-tree
  switching lemma would remove it, but is **false** even with per-prime
  masses `≤q^{−1/2}`. The proved counterexample is "two of `√q`
  coordinates coincide": `DT_q(f_ρ)≍√q` with constant probability. The
  correct open target is the energy form ESW,
  `E_ρW^{≥s}[f_ρ]≤(C(pk+max w_ℓ))^s`, which with LMN gives exponent 1/11.
* **§6.5 ceilings (Assessment).** PO Thm 4.1 needs `log p≫K·log Z`, with
  `K≳S` and junta `≳S`, so `log p≳S²` up to logs for *any* minorant.
  That is ≈1/9 under ET, ≈1/6 with the observed `S≈𝓛^{2.5}`. The
  heuristic 1/3 is beyond this transfer unless S is `≪𝓛`.
* Not pursued: log-weighted quarantine thresholds `c_ℓ=log ℓ/(16𝓛)`.
  They satisfy the local lemma but save only on bad primes `>√T`, and they
  are irrelevant while `log Z≍d𝓛` dominates.
* Review targets for phase 2: the restriction identity
  `E_z f̂_ρ(S)=f̂(S)` and the spectral-norm bound in Lemma 6.1; that the
  pulled-back characters are bounded functions of `<d` coordinates; and
  the counterexample in §6.4.

## Phase 3 (parent's tasks (a), (b)); stopping near the context limit

* **(b) is a dead end, proved (OMEGA8 §6.6, Prop 6.6; modulo a standard
  BV divisor lower bound for `Σ_p τ(((p+1)/4)²)`).** The `m=1` singles
  survive every class-of-one quarantine and carry mass `≍𝓛²`, so
  `S≪𝓛^{1+o(1)}` is impossible, also for the iterated quarantine
  (`|𝓑|=T^{o(1)}`). With §6.5, the route via PO Thm 4.1 cannot beat
  roughly `log p≈𝓛^{4…6}` (exponent ≤1/4) even ideally. The one opening:
  singles are prime-local, so sieve them by Brun and use BRW only for
  multi-prime events. Then `S_{≥2}` replaces S; its size is unexamined.
* **(a) ESW: not attempted beyond its formulation (§6.4).** I did no
  literature check of Tal 2017, p-biased or product-space switching, or
  O'Donnell ch. 8; there was no context left for it. §6.4's
  counterexample shows that any q-ary result must bound energy, not
  decision depth.
* Phase 2/3 status: Thm 6.3 (exponent 1/13) and Prop 6.6 are unreviewed.

## Round 3: review R30c of §6 (applied by successor O34)

R30c (`reviews/pointwise-omega8-review-3.md`): Thm 6.3 and Lemma 6.1 SOUND.
MAJOR M1 applied: "ESW ⇒ 1/11" needs in addition a q-ary ℓ¹ bound and a
quarantine with `|𝓑|≪kS*` (the cited "Lemma 6.2" never existed); without
them ESW gives no real gain. The phase-2 bullets above that say "ESW would
give 1/11" and "≈1/9 is the ceiling under ET" are superseded by OMEGA8
§6.4–6.5 as repaired (1/9 is bookkeeping, the supported ceiling of the
PO-Thm-4.1 route is 1/4). Minors m1–m8 applied (m7: `K ≥ log(1/δ) ≥ S1 ≫ 𝓛²`
rigorously; m8: splitting off singles cannot lower K).
