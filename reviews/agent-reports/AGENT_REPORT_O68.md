# AGENT REPORT O68 — support-aware certificates (branch side-agent/support-aware)

Deliverable: `POINTWISE_OMEGA17.md`; scripts `scripts/omega17_{shallow,charlier,toylp}.py`;
data `data/omega17/`. Checkpoint 1, for parent review.

## Result in one paragraph
No certificate beyond exponent 1/4 was found, and no support-aware planting lemma for ES was
proved. The question is reduced to a precise **integer-only** statement (Conjecture SAP, §6):
with Haar-type prime information, support and atomicity enter only through the integer
capacities of the information atoms. If those capacities are Haar-like, the planted fake
should survive up to constants (heuristic). The planted law is flat once R ≥ kr* + (k+1)/(s−1) (Lemma 5.2), so the
box costs only constants. Toy LPs agree (EVIDENCE): support awareness helps only when
|S|/N_x < ≈2, and then by one junta level. The natural route to SAP is to make the planted law
*shallow*. For the big coordinates this looks feasible: a Charlier density is positive on a
finite grid in an exchangeable model (§3, EVIDENCE; the integer fake built from it is only an
outline). For the small coordinates the natural shallow constructions tilt the small-coordinate
law (§4, heuristic).

## Items and labels
* Def 1.1 SALC; Lemma 1.2 (moduli > x give only the box or primality tests): PROVED.
* Lemma 1.3 / Rem 1.4 (duality; with Haar-type bounds, validity is an integer statement): PROVED.
* Lemma 2.1 (no monotone fake; Harris): PROVED.
* Prop 3.1 (Charlier fake): identities PROVED. Positivity is EVIDENCE: exact rationals, R_min(n)
  for odd n ≤ 81, with R_min/n ≈ 2.9 at n = 81, growing slowly.
* Construction 3.2 (exchangeable-model integer fake): an Assessment-level outline with three
  named gaps (box/normalisation, local densities at primes > T, BT constraints). The
  self-review showed the earlier "PROVED given positivity" label was wrong.
* Lemma 4.1 (in a Poisson model with R ranging over an interval): PROVED. Its application to ES
  is heuristic, since actual conditional means take finitely many values.
  Assessment 4.2 (tilt of the natural shallow constructions): heuristic, and specific to those
  constructions.
* Lemma 5.1 (aggregation: only capacities matter): PROVED.
  Lemma 5.2 (capped/flat planting): PROVED.
* Toy LP table (§5): EVIDENCE.
* Conjecture SAP: CONJECTURE, restated after the self-review. It now has admissible
  (LQ-smooth) moduli, reduced classes, Q ≤ x^δ and the range C𝓛³ ≤ log x ≤ c𝓛⁴/log𝓛. Its
  consequence is limited to LP-relaxed SALCs on S_T whose information profile is 𝒥(δ).

## Scope warnings for the reviewer
* SAP's scope is information with unconditional-type accuracy. Even in the exchangeable model,
  GRH-quality (√x) information is not handled, because T-rough integers are not known to
  equidistribute to √x accuracy (finite Euler product).
* Whether 𝒥(δ) covers all known unconditional prime information is an Assessment, because
  Gallagher's estimate carries extra terms.
* Self-review: a deep reviewer subagent (R68-self) checked Lemmas 1.3, 2.1, 5.1 and 5.2 as
  correct; Lemma 5.2 was checked in exact rationals for k ≤ 3. It also checked the toy-LP
  aggregation against an unaggregated LP. Its FATAL and MAJOR items were repaired by
  downgrading or restating; see the Status line of the document.
* Assessment 4.2 uses the order of magnitude of HAAR Lemma 2.3's loads w_q. It is not a theorem.

## Replay
See the Replay section of `POINTWISE_OMEGA17.md`. The runs total about 30 min, on 2 cores and
under 8 GB.
