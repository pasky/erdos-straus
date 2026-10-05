# AGENT REPORT O42 — Haar avoidance ⇒ prime avoidance (branch `side-agent/avoid-transfer`)

Deliverable: `POINTWISE_TRANSFER.md` (new), `scripts/transfer_mn.py`,
`scripts/transfer_toy.py`. Not merged into main.

## Goal 1: abstract theorem (POINTWISE_TRANSFER §§0–3)

**Theorem 1.1 (proved modulo Gallagher [MV3 Thm 28.19] + Landau–Page, and
Håstad).** Free primes `𝒫` (coprime to `Q`), `N = |𝒫|`, prime powers
`ℓ^{e_ℓ} ≤ T`; events = *arbitrary* sets of unit classes on `≤ k` free primes;
`S` = total Haar mass; LLL weights `x_i` with `δ_L = ∏(1−x_i)`; `m_a` = number
of distinct atoms (`≤ 2(NT)^k`); twist hypothesis (Tw):
`|𝔼[Fψ]| ≤ δ/5` for real primitive `ψ` on the free primes. Then there is a
prime `p ≡ a (Q)`, `p > T`, avoiding every event, with
```
log p ≤ C₇(log Q + (3k+2t)log T + 1),  t = 10·k·⌈log₂(4NT)⌉·⌈log₂(400 m_a²(S+1)/δ_L)⌉.
```
`C₇ = 2C₂(1+log1.03)+1`, `C₂` the absolute (effective, not computed)
constant of the [SN] transfer theorem.
**Corollary 1.3:** if `w_ℓ ≤ 1/(64k)` for all `ℓ`, then (LLL),(Tw) hold and
`log p ≪ log Q + k·log T·log(4NT)·(S + k log(4NT))`.

Hypotheses clarified: no single-value hypothesis on events (splitting into
atoms is used only inside the sandwich, cost `log m_a ≤ k log(NT)+1`); no
codegree hypothesis; non-unit classes can be deleted (contain no prime `> T`);
moduli must be supported on free primes; `δ_L` may be replaced by *any* lower
bound `δ_* ≤ δ` (Remark 3.1); (Tw) holds under the Haar criterion
`δ^{(ℓ₀)} ≤ (6/5)δ` (Lemma 3.2) or the LLL-local criterion (Lemma 1.2).
Exceptional zero (§3.3): no Siegel hypothesis; enters only via (Tw) for real
characters on free primes (Case B), and via the Page bound to absorb `R₁` in
Case A. I explain why Case B cannot be handled Case-A-style by this argument.

## Comparisons (§4)
* Linnik single class: `log p ≪ log Q + Σ e_ℓ log ℓ ≍ N log T`; Theorem 1.1
  replaces `N log T` by poly(`k, log T, S`) × `log N`.
* Per-cell Thorner–Zaman (OMEGA8 v1) pays the ℓ¹ mass; Gallagher transfer pays
  only `𝔼|B|/𝔼B`.
* §4.6 (Assessment, revised after R42 MAJOR-1): the right benchmark is
  quarantine (Q) + coarsening/union bound (C) + Bonferroni (B), all with the
  same Gallagher transfer. (B) alone beats Thm 1.1 by `≈ log(NT)` on
  codegree-spread systems. Hub examples are beaten by (Q) (single/multi-hub)
  or (C) (pair-hubs on a matching). **No system is known on which Thm 1.1
  provably beats (Q)+(C)+(B)**; whether the ES witness system is one is
  unchecked (the OMEGA2 experience is only evidence). The earlier claim
  that the hub example shows the sandwich's advantage was wrong.
* Jacobsthal/covering literature (Iwaniec, FKMPT, FFKPY, Hough, BBMST): all
  Haar-side or integer statements; only Costello–Watts/FGKMT/FKMPT are in
  `sources/`; the others are *[memory]* and unchecked. No priority claim.

## Goal 2: applications (§5)
* **Cor 5.2 (`m/n`, Sierpiński `m=5`):** for each fixed `m ≥ 4`, with the
  Type II family `m/n = 1/(suw)+1/(nsvw)+1/(nuvw)`, `M = m·uvw − 1`, classes
  `R_m(M) = {−mD : D | A²}`: `W_m(p) ≥ exp(c_m(log p)^{1/7})` i.o. (mod G+H+ET
  Prop 1.4 with `κ=m`), and `(1/log2−o(1))log₂p·log₃p` without ET.
  Lemma 5.1 (atoms, class of one, gcd symmetry) proved + machine-checked.
  After R42: Lemma 5.0 (reviewer's proof, credited) — every Type II
  solution of `m/p` (prime `p > m`) has the form (5.1), so Cor 5.2 bounds
  *all* Type II solutions. ET Prop 1.4 is stated for general `k`; nothing
  beyond ET is assumed.
* **Cor 5.3 (generic witness families):** any `R(M)` of unit classes with
  `1 ∉ R(M)` and mass `S^♮(T) = Σ_{M≤T}Σ_{r∈R(M)} gcd(M,r−1)/φ(M) ≤ ℒ^α` has
  `W_R(p) ≥ exp(c(log p)^{1/β})` i.o., `β = max(α+3, 5)` (the floor 5 comes
  from the `log m_a` term in `k₀`; fixed after self-review). ES is
  `α = 4`(+log) → `1/7`.
* **Cor 5.4 (prime Jacobsthal-type, composite moduli)** with an honest scope
  paragraph: for `k = 1` / monotone ("`d | p+h`") events, sieves are far
  better; for small mass the union bound suffices; §5.3(c) is now an
  unverified Assessment (no separating example known, see §4.6).

## Checks
`scripts/transfer_mn.py` (Lemma 5.1, identity, `m ≤ 11`, `M ≤ 3000`) and
`scripts/transfer_toy.py` (exact Haar: sandwich identity, `B ≤ F`, energy bound,
ℓ¹-tightness, Lemma 3.2 chain, on 6 random general-event systems) pass.
Toy shows (Tw) failing exactly when one prime carries half the constraint.

## For the reviewer
Most delicate points: Step 1 (atoms vs. LLL on original events), Step 6
(target class `a ≠ 1` in the transfer proof, Case A with `χ₁(a') = −1`),
Lemma 1.2's use of the conditional LLL on the subfamily, and the claim in §2
Step 3 that [SN] `lem:tail` holds for arbitrary (non-cell) events.

## Self-review (deep reviewer subagent) — applied
Fixed: Cor 5.3 exponent (`β = max(α+3,5)`); hub example (single hub was
refuted by `B₁ = 1 − N`; now multi-hub); empty events excluded; (Tw)
criteria stated as sufficient only; Chebotarev comparison (discriminant vs
conductor); small-`Q` qualifier for sieve claims; non-unit-class wording;
toy-output misreport; script cutoff handling. Confirmed sound by the
reviewer: Steps 1/3 (arbitrary events, atom count, DNF width), Step 6
(general target class, `χ₁(a') = −1`, aux prime, `log Z`), Lemmas 1.2/3.2,
Cor 1.3 arithmetic, Cor 5.2.

## Round 2: R42 repairs (all applied, one commit each)
* MAJOR-1: §4.6 rewritten with the (Q)+(C)+(B) benchmark; plain statement
  that no separating example is known; pair-hub attempt shown beaten by
  coarsening; §5.3(c) softened to unverified Assessment.
* MINOR-1/2: Lemma 5.0 (completeness, reviewer's proof with credit); Cor 5.2
  phrased for all Type II solutions; ET Prop 1.4 label wording.
* MINOR-3..6: exponent `1/max(α+3,5)` in Remark (i); `log log p` step and
  `log(S^♮+1)` clause in Cor 5.3; Remark 3.1 says (LLL) is unused with
  `δ_*`; Cor 5.4 instance (2) needs `q ∤ h`, `y ≥ 64`.
