# AGENT_REPORT_O9 — verify.py blocks for the 2026-10 documents

Branch: this worktree. Commits: one per block, then docstring + STATUS.

## What was added

There are nine new `verify.py` blocks, (bz)–(ch). They sit before the final "all checks passed". Each block is a deterministic, seeded, small instance of the key machine check, and fails with an `AssertionError` that names the lemma. All blocks except (ch) are re-implemented inline; they do not import `scripts/`.

| block | document | what is checked | s |
|---|---|---|---|
| (bz) | POINTWISE_SIZE | Lemma CT (a/b/c) on all 3498 solutions, p≡1 (4) ≤ 1500, enumeration completeness by naive loop for p < 300 (same counts as `pointwise_size_ct_check.py 1500 300`). Lemma 8.2 and the identity (−p/q) = −(x/q) of Cor 8.3(a) on all 47076 windows, p≡1 (8) < 2000, q≡3 (4) < 3p | 5.7 |
| (ca) | POINTWISE_OMEGA | Lemma 2.3 algebra (involution; (s,r,k), k ≥ r, m \| r+k), M ≤ 6000. Lemma 2.1 and its converse at T = 255, 1023, 4095: random n≡1 (Q_y) plus CRT-forced survivors, W(n) > T compared directly | 0.6 |
| (cb) | POINTWISE_OMEGA2 | Lemmas 1.1 (closed form R_L, vanishing), 1.2, 10.1(1) by brute force on 400 random systems (262862 cases) | 3.4 |
| (cc) | POINTWISE_OMEGA3 | Thm 3.2 item 1 composition B ≤ F2·F3, plus cell bounds β ≤ F2^{(i)} ≤ α; 3×1500 systems. A negative control (β for c_i < 0) must produce violations (275) | 2.3 |
| (cd) | EXCEPTIONAL_THETA | Prop 2.4 Step 3 symmetrisation identity, exact. The reduction LP W ≥ E_w W_ex ≥ void runs on 40 instances only if scipy imports; otherwise it prints SKIPPED | 0.1 / 1.9 |
| (ce) | EXCEPTIONAL_BALANCED | Lemma 4.1 exhaustive for M ≤ 6000: D\|A² ⇔ A = srk; part (1) coprimality; part (2) for all n mod q; part (3). Lemma 2.1 (gapped ⇒ (U)) on all M ≤ 2·10⁵ for 1+η ∈ {5/4, 3/2, 2}, with the gapped test in exact integers | 1.8 |
| (cf) | EXCEPTIONAL_TWIN | Jacobi Lemma 1.1 on 159390 classes (M ≤ 20000), together with gcd(D,M) = 1. Lemma 3.1 u-form and Lemma 3.2 sign constraint for M ≤ 3000 | 3.6 |
| (cg) | EXCEPTIONAL_TWIN2 | Thm 1.4 by exact tensor computation. Seeds 1–3 × 400 reproduce the Replay numbers (215/211/191 in-hypothesis systems, max 0.9892); seeds 4–6 × 1000 are added, giving 2178 in-hypothesis systems with max lhs/bound = 0.9984. Also checks Z₂(0) = Z₁², and that the q-term is needed on some instances | 1.8 |
| (ch) | 3/4 blind audit | imports `scripts/es34_blind_audit_checks.py`, runs its 11 functions, and requires exactly 16 PASS and no FAIL | 2.5 |

The new blocks add about 22 s. A full `uv run python verify.py` passes in 172 s, peak RSS 313 MB. A full `uv run --with scipy python verify.py` passes in 181 s with the LP included. Both runs used `ulimit -v 12 GB` and 2 BLAS threads.

## Mutation tests (ad hoc, not committed)

These mutations were each caught:
* (ca): dropping the condition m \| 4D+1 when building F_ℓ;
* (bz): using p≡3 (4) primes;
* (cb): the wrong sign in R_L, and a +1 in Lemma 10.1(1);
* (cc): using β for negative coefficients;
* (ce): the sign in part (3);
* (cf): the sign in Lemma 3.2;
* (cg): dropping the q-term.

## Remarks for the parent

* **Lemma 8.2 holds for every p≡1 (4).** It holds for p≡5 (8) as well. A mutation to p≡1 (4) was *not* caught, and this is correct: at r = 2, q≡3 (8) and (2/q) = (2/p) = −1. Only the context of the lemma uses p≡1 (8). This is not an error in the document, just a weaker hypothesis than needed.
* **The O2 Lemma 1.2 constant is loose on small systems.** |B_L − 1[A=∅]| ≤ G_{L+1}, without the factor 4^{L+1}, also held on all 262862 small cases. A mutation removing the factor was therefore not caught. The lemma's constant is simply loose here.
* **The TWIN2 Thm 1.4 constant is nearly tight on random instances.** On the larger sample the maximum of lhs/((1+25δ)·rhs) is 0.9984.
* **"Thm 2.4" in the brief is Proposition 2.4** of EXCEPTIONAL_THETA.
* **scipy is not a project dependency.** So (cd)'s LP is skipped by default, and the skip is printed.
* **Labels.** All of these are finite checks (EVIDENCE/sanity). No label in DISCOVERIES.md was changed.
