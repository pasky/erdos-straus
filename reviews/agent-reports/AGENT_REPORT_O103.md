# AGENT REPORT O103 — r = 13, hybrid DFS with a complete C witness engine (checkpoint 1)

Branch `side-agent/r13-hybrid-close` (merged `side-agent/r13-cover-all` first). Document: POINTWISE_MORDELL13D.md.

**Outcome: no root closed.** No certificate produced; POINTWISE_MORDELL Thm 3.1(b) and 13C Thm 6.1 unchanged.
Nothing is claimed beyond EVIDENCE for the DFS behaviour.

Deliverables
1. `scripts/m13d_wit.c` (+ `m13d_wit.py` driver): complete witness set at a node — all seven ET families, `M | L`,
   no size cap, optional `req` (only classes with `p^{v_p(L)} | M`, used for children of open nodes). 128-bit,
   ≈ 45 ms per full set at `L ≈ 10¹⁹` (Python 13C engine: minutes). Reorganised enumeration (13D §1: loop over odd
   `f | L` + `gcd(L_f, x+f)`; I1/II1/I4 by residues mod `m`; II2 via cached Pollard-rho factorisation of `(f+1)/4`).
2. Validation vs `m13c_witness.witness_all(first=False)`: all 156288 units at L = 9240, 10920, 65520, 720720;
   240 random open leaves of the 13C §8.2 tree (200 truncated to 10¹⁰–10¹⁵, 40 at k ≤ 4 dropped prime powers,
   incl. untruncated `L ≈ 10²⁰`), 790 children in `req` mode — **0 mismatches** (logs/o103_val_*.log).
3. `scripts/m13d_dfs.py`: hybrid DFS (tables M ≤ 10⁶ + complete engine at each node; optional C-scored split
   choice, per-prime exponent caps), output in 13C tree format → 13C checkers apply unchanged.
4. Negative EVIDENCE (13D §2–3): for root 418321 the best split leaves ≈ 1.3–3 open children per open node at
   all depths sampled (bits 40–90); open-leaf count grows ≈ ×2.5 per expansion; 1 h runs end with 15–17k open
   leaves (open mass down to `5·10⁻⁹`). p-adic refinement at primes already in L stalls (25 levels of `2^k`, both
   children open). Open leaves are QRs at nearly all primes ∉ {11,13}.

Not done: other roots (418321 is the easiest; same behaviour expected), certificates/checkers (nothing closed).
Dives v2 (logs/o103_dive12.log) still running at report time (first dive closed at once; second: min open
1, 4, 2, 2, 5 at bits 65–82).

Suggestions: closure needs a structural idea, not more compute — e.g. understand the uncovered set of the root
in `∏_{p≤P} ℤ_p` (is it empty for some P?), or a reciprocity obstruction for nodes that are QRs at all primes
∉ {11,13}; the engine is ready for any such targeted experiment.

## Addendum (parent's follow-ups)
* Dives v2 finished by timeout (13D §3): dive 0 closed at once. In dive 1 the minimum number of open children was
  1, 4, 2, 2, 5, 5, 3 at bits 65–94 (mean ≈ 3.1). Step cost grew to 10⁴ s at L ≈ 2⁹⁴. The run is consistent
  with supercritical branching (one branch, weak evidence).
* 13D §4 (EVIDENCE + Assessment): 6224 of the 16857 open leaves of run 2.2 are QRs at all primes ∉ {11,13}.
  Of 400 sampled, **none** lies on the T-generic line, and **all 400** T-projections are covered at the same
  level. Root 418321 sits in T-cell (2,7), not (2,2). So its failure to close is **not** the T-generic
  (2,2)/x** phenomenon; it comes from square-mimicking, off-line points. The (2,2) cell concerns root 473761
  only, which was not run.
