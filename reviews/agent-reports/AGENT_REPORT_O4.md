# AGENT_REPORT_O4: pair-codegree gap G_pair (checkpoint 1)

Branch: `side-agent/omega-gpair` (worktree `erdos-straus-claude-agent-worktree-0001`).
Deliverable: `POINTWISE_OMEGA3.md`; scripts `scripts/omega3_codeg.py` and
`scripts/omega3_compose_check.py`; data in `data/omega3/`.

## Outcome

**G_pair is not a genuine barrier.** It came from using one truncation
level for all events. Claimed results (labels as in the document; not yet
reviewed by the parent):

1. **Thm 4.3** (PROVED modulo Thorner–Zaman via PO Thm 4.1; effective):
   `W(p) ≥ (log p)^4·exp(−C log log p/log log log p)` for infinitely many
   Mordell-hard p. H_MIN(θ) holds for θ>1/4, and `H_MOD(A)` is refuted
   for `A<4`. Cor 4.4 adds `ck_min(p)≥(log p)^{1−o(1)}` jointly.
2. **Thm 5.2** (same status): for every fixed k, there are infinitely many
   p with `W(p) ≥ (log p)^k·exp(−C_k log log p/log log log p)`. In uniform
   form, `log L_h(T) ≤ T^{o(1)}`, and H_MIN(θ) holds for all θ>0. The
   prime side now matches the Haar side (O2 Thm 11.3). No explicit rate
   is claimed for k→∞.

## The idea

* **Thm 3.2 (two-level minorant).** Events of support ≤2 (singles and
  edges) form an *outer* graph-level sieve. O2's Lemma 2.1 needs no
  codegree condition, so the truncation `L_2` of this level is free. The
  hyperedge level is composed *inside* it, coefficient by coefficient:
  a lower approximant for positive coefficients, an upper approximant for
  negative ones, with the level-2 system conditioned on each cell.
* **The key estimate is the tilted moment.** The conditional local lemma
  (HSS) gives `E[F_2·1[C]] ≤ P(𝒜_2)P(C)e^{|π(C)|/2}`. So the level-3
  truncation `L_3`, and hence the codegree threshold `t≍1/L_3`, depend
  only on the level-3 mass.
* **Lemma 3.3 (push-down).** Heavy pairs (codegree `>t`) become level-2
  edges, and high-degree vertices become singles. Both are Markov
  (first-moment) steps. The cost lands in the level-2 mass, `O(Ŝ²)`, and
  never feeds back into t. The `−4d²` clusters (O2 §11.4, reviewer r3)
  thus become level-2 vertex quarantines.
* **Thm 5.1 (k levels).** The same scheme iterates: masses flow
  downwards, and thresholds depend only on higher levels.
* **No arithmetic input.** No upper bound on pair codegrees is used. §2
  (atoms as triples `(s,a,b)`; three hub families `−4sa²`, `−1/(4sb²)`,
  `−a/b`, the third new; heavy pairs = small-height rationals,
  numerically) is explanation and EVIDENCE only.
* §1 (Thm 1.1, Brun-pure-sieve decoupling of prime-local quarantines)
  is a self-contained special case. §§3–5 do not depend on it.
* The brief's QR idea: `−4d²` is QNR exactly at `ℓ≡3 (4)`. Forcing
  residuosity globally costs `π(T)log 2`, so the idea is unusable and,
  after §3, not needed.

## Checks done

* Self-review (`review` tool, deep, hostile): no fatal or structural
  obstruction found. Two false estimates were found and repaired:
  * the tilted weight `w'`: now `1+w'=17e^{1/2}` consistently;
  * the induced-event mass in Thm 5.1: now bounded via higher codegrees,
    since the degree sum alone is false when several vertices of one
    event are fixed.

  Presentation repairs: the numeric `F_r` was renamed `H_r`; the mass
  budgets `Ŝ_{≥r}` are frozen; Thm 5.2 is stated in uniform form instead
  of "equivalently"; the unsupported `k≍logloglog T` rate was removed.

  The reviewer also found that the codegree script's shortest-vector
  "height" classification was wrong. It was removed; hub membership is
  now by explicit enumeration of `𝓗_X`.
* `omega3_compose_check.py`: brute-force check of Thm 3.2's pointwise
  algebra on random small systems. 0 violations in 3×3000 trials. The
  negative control has 1283 violations. The script exits nonzero on a
  violation.
* `omega3_codeg.py`: exact pair codegrees for one pair per T, T from
  10⁹ to 10¹³, θ=0.26–0.28. Max Δ is ≈0.21–0.30 (class −4, −1, −1/4).
  Outside `𝓗_X` the maximum is ≈0.003–0.007 at X=1024, falling roughly
  like `X^{−0.7}`. All 30 heaviest classes in each run lie in `𝓗_16`.

## What the parent review should attack

1. **Thm 3.2 Step 1.** The claim is that O2 Lemma 10.2's proof goes
   through with the tilt. Its pointwise reduction to private families is
   positive, so the conditional bound applies term by term.
2. **Thm 3.2 Step 2 and the composition.** Check `B≤F_2B_3` with signed
   `B_3`, and the error budget `E[F_2F_3−B]≤P/100`.
3. **Lemma 3.1(2).** This is HSS Thm 2.1 for the product measure
   conditioned on avoidance; it is the same use as in O2 Thm 3.1 Step 4.
4. **Thm 5.1.** Check the conditioned codegrees and induced masses, the
   freezing order, and that `L_r, N_r, H_r, Λ_r` contain no circularity.
5. **Application.** O2 Lemma 11.2 is used with `c_0∝Ŝ^{−A}`, so the
   quarantine has `T^{o(1)}` extra primes. The rest is O2 Thm 5.1's
   transfer verbatim.

## Suggested ledger text (if the review confirms)

> **(H)13.** **Every exponent (POINTWISE_OMEGA3 Thms 4.3, 5.2):** for
> every A, `W(p)>(log p)^A` for infinitely many Mordell-hard p, and
> `log L_h(T)≤T^{o(1)}`; exponent 4 with the explicit
> `exp(−C log log p/log log log p)` loss. **PROVED modulo
> Thorner–Zaman.** Mechanism: multi-level support-truncated minorant.
> Lower levels (graph level: no codegree condition) have free
> truncation; upper levels are composed inside via the conditional
> local lemma; heavy vertex sets are pushed down by Markov. G_pair
> (O2 §11.4) was an artefact of a single truncation level.

STATUS.md: replace "any pointwise multiplier mechanism needs witness
moduli beyond `(log p)^3`" with "beyond every fixed power of log p".

## Review round 1 (parent hostile review, `reviews/pointwise-omega3-review.md`)

* **Verdict.** Every item is SOUND: Thm 3.2, Lemma 3.1, Lemma 3.3,
  Thm 5.1/5.2, and the ES instantiation modulo Thorner–Zaman.
* **End-to-end check.** A brute force at T=30000 confirms the
  certificates.
* **Repairs applied** (commit "review repairs D1–D6"):
  * **D1.** Setting 3.0 (D3) now refers to `t(Ŝ)` only; the stray O2
    `C_3` formula is removed.
  * **D2.** Lemma 3.3's mass display now uses `S_2^{(b)}`, the edge mass
    after (b) and before the (c) deletions. Thm 3.4's Σ bound was updated
    to match.
  * **D3.** Thm 5.2: `y^k>T` gives `Ω(r)≤k−1`. So Thm 5.1 is applied
    with `k'=max(k−1,3)` levels, and Lemma 11.2 uses `k−1` free primes
    per atom.
  * **D4.** The §1 twist claim now states `h_ℓ≤1/100` (Lemma 1.3's
    assumption).
  * **D5.** §6 now says that the O4 script uses `e_{L+1}(a)`, not
    `G^{cov}`. It cites the reviewer's `review_omega3_check.py compose`
    (true `G^{cov}`, 0 violations) and its `push` mode.
  * **D6.** Thm 5.1 Step B: identical induced events are merged, so the
    conditioned systems are simple.
## Review round 2 (`reviews/pointwise-omega3-review-2.md`)

* **Verdict.** Everything is SOUND, including from-scratch
  re-derivations of O2 Lemmas 10.1, 10.2 and 2.1 and an adversarial brute
  force.
* **D1** (the duplicate t) and **D3** (`Ω(r)≤k−1`) had already been
  repaired in round 1.
* **D2.** In Thm 5.1, `L_2` is now chosen with `200k𝔐_3`, so the
  level-2 error is `≤P(all)/(100k)` and the total is `≤P/100`. `Λ_2` is
  defined explicitly for the k-level case.
* **2a/2b** are fixed in POINTWISE_OMEGA2.md Lemma 10.2 by minimal
  edits:
  * fixed-slot breadth-first encoding (`N=kh` slots);
  * simplicity of the hypergraph is not needed.

## Status

Review repairs applied. Stopping for the parent's final check.
