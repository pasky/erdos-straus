# AGENT REPORT O68 — support-aware certificates (branch side-agent/support-aware)

Deliverable: `POINTWISE_OMEGA17.md`; scripts `scripts/omega17_{shallow,charlier,toylp}.py`;
data `data/omega17/`. Checkpoint 1, for parent review.

## Result in one paragraph
No certificate beyond exponent 1/4 was found, and no support-aware planting lemma for ES was
proved. The question is reduced to a precise **integer-only** statement (Conjecture SAP, §6):
with Haar-type prime information, support and atomicity enter only through the integer
capacities of the information atoms. If those capacities are Haar-like, the planted fake
survives up to constants. The planted law is flat once R ≥ kr* + (k+1)/(s−1) (Lemma 5.2), so the
box costs only constants. Toy LPs agree (EVIDENCE): support awareness helps only when
|S|/N_x < ≈2, and then by one junta level. Proving SAP for ES is blocked by a specific mechanism:
the small coordinates (§4). It is not blocked by the big ones, for which a shallow Charlier
fake exists in exchangeable models (§3).

## Items and labels
* Def 1.1 SALC; Lemma 1.2 (moduli > x give only the box or primality tests): PROVED.
* Lemma 1.3 / Rem 1.4 (duality; with Haar-type bounds, validity is an integer statement): PROVED.
* Lemma 2.1 (no monotone fake; Harris): PROVED.
* Prop 3.1 (Charlier fake): identities PROVED. Positivity is EVIDENCE: exact rationals, R_min(n)
  for odd n ≤ 81, with R_min/n ≈ 2.9 at n = 81, growing slowly.
* Cor 3.2 (exchangeable model): PROVED given the positivity of the multivariate ψ, which has
  been checked only in the Poisson limit.
* Lemma 4.1 (no fixed-polynomial exchangeable fake that is uniform in R): PROVED.
  Assessment 4.2 (small-coordinate tilt; untilting costs level e^{Θ(𝓛⁴)}): Assessment.
* Lemma 5.1 (aggregation: only capacities matter): PROVED.
  Lemma 5.2 (capped/flat planting): PROVED.
* Toy LP table (§5): EVIDENCE.
* Conjecture SAP: CONJECTURE.

## Scope warnings for the reviewer
* SAP's scope is information with unconditional-type accuracy. Even in the exchangeable model,
  GRH-quality (√x) information is not handled, because T-rough integers are not known to
  equidistribute to √x accuracy (finite Euler product).
* Cor 3.2 is stated with a hypothesis that the multivariate shallow ψ is nonnegative. This is
  checked only in the symmetric Poisson limit.
* Assessment 4.2 uses the order of magnitude of HAAR Lemma 2.3's loads w_q. It is not a theorem.

## Replay
See the Replay section of `POINTWISE_OMEGA17.md`. The runs total about 30 min, on 2 cores and
under 8 GB.
