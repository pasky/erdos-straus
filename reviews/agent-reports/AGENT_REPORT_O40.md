# AGENT_REPORT_O40 — SPW (branch side-agent/spw-proof), checkpoint 1

Deliverable: `EXCEPTIONAL_SPW.md`; scripts `scripts/spw_*.py`; data `data/spw/`.

## Headline
**The O40 target is refuted.** SPW(2, 2/5 − ε, O(1)) for all large N is false, and so is
SPW(C, σ, Δ₀) for every fixed C and every fixed σ > 0 at all large N:

* **Theorem 3.2 (PROVED):** any R with (P1)–(P2) at N has σ ≤ 4√(πm₀/(M+1))(1+o(1)),
  m₀ ≤ 2C+3, M ≍ log N, so σ ≲_C (log N)^{−1/2}. Proof: project to ℤ/e with e the least
  multiple of lcm(1..M) above CN. Then every frequency m₀ ≤ |k| ≤ M of ρ − 1_W is pinned
  by the profile constraints, so the degree-M Fejér smoothing of ρ − 1_W is a trig
  polynomial of degree < m₀. That polynomial would have to jump by ≈ σ across the window
  edge within distance ≈ e/√(m₀M), which Bernstein's inequality forbids.
* **Exact finite certificates (PROVED, rational arithmetic):** σ ≤ 72/185 = 0.3892 at
  N = 300 (single modulus e = 630) and σ ≤ 0.381133 at N = 1150 (e = 2310). So the R25
  observation "LP optimum = σ_C(N) = 2/5 at every N" breaks beyond the tested N ≤ 60.
  LP values (EVIDENCE) keep falling: 0.3737 at N = 4400 (e = 9240).
* **Corollary 3.3:** the same bound holds for the Flat margin s₀ (for any t). So the decay
  of the IF2 §5 Flat margins is not only a truncation effect.

## What survives (important for the parent)
IF2 Thm 5.2 does **not** need fixed σ. By its Remarks (i)–(ii) and Prop 9.1 it needs only
**weak SPW**: σ_N ≥ c₀e^{−S_A} and Δ_N ≤ e^{S_A} (Lemma 1.4). Lemma 1.4 also shows that only
classes *through [1,N]* need mass < 1; sparse classes may carry quasi-polynomial mass.
Theorem 3.2 forces only σ_N ≲ (log N)^{−1/2}, far above e^{−S_A}. So the hybrid 3/4-cap
route is not refuted. Its hypothesis must be restated as weak SPW, which is **open**.

## Other results
* Lemma 1.1: SPW on ℤ is equivalent (up to ε) to a periodic SPW on ℤ/lcm(1..T).
* Lemma 1.3 (two-edge split): c(b,d) = N/d + {−b/d} − {(N−b)/d}. SPW follows from one
  N-free "half-line" problem HL (left edge only); the right edge is its reflection.
* §2 BDW (pointwise density ≤ A·uniform on ℤ/L₀; this would imply SPW for C > A):
  - The LP optimum equals the trivial bound A*(N) = 3/2 − 3/N exactly for N ≤ 24, with a
    bang-bang optimal solution.
  - But A(N) ≥ c√N is PROVED, and A(150) ≥ 1.551 holds by exact computation. So the
    small-N LP evidence for BDW was completely misleading.
  - Lesson: small-N LP pinning (as in R25 C10) is weak evidence here.

## Not done / open
* No construction for weak SPW at large N. True decay rate of σ*(N) unknown: between the
  (log N)^{−1/2} upper bound and nothing.
* Multi-modulus (global) obstructions might decay faster than the single-modulus bound. I
  found no mechanism for that; the Fejér argument is intrinsically single-modulus
  (e ≈ CN forces M ≲ log N).
* The background run on e = 18480 and 30030 (data/spw/local_primorial2.txt) may still be
  going.

## Suggested review focus
Theorem 3.2's proof, in particular:
1. the Fourier characterisation "free ⟺ gcd(k,e) < e/D";
2. the tail bounds;
3. the sampling ⇒ continuous sup step.

Also re-run `spw_local_cert.py 300 2 630` and check the certificate logic: g is a
combination of classes mod d ≤ D, and Σ z_s 1_s ≥ g is checked exactly.

## Self-review (deep reviewer subagent) — applied
Confirmed: Thm 3.2 (Fourier criterion, Fejér tails, sampling, Bernstein, choice of r) sound
for fixed C > 1; Lemma 1.3 reflection identity; Lemma 1.4; both C = 2 certificates.
Fixed: exact (Fraction) C in `spw_local_cert.py`; outward rounding of all "rigorous" decimals
(A(400) ≥ 2.496, σ ≤ 0.381133); half-line script now prints the Lemma 1.3 margin
(0.3472, not 1 − 2h); Lemma 1.3 note direction corrected; Lemma 2.1 proved directly (no
clipping at 1/2); Prop 2.3 odd-N range k < (D−1)/3; Cor 3.3 notation (M vs M_F, t ≥ 0);
Thm 3.2 scope "M → ∞ for fixed C > 1"; two overstatements removed.

## Checkpoint 2 — review R40 (SOUND-AFTER-MINOR-REPAIRS) applied
* D1: Lemma 1.3 note — with Thm 3.2, the HL optimum satisfies h ≥ 1/2 − 1/(4C) − o(1)
  (3/8 at C = 2); HL can only serve weak SPW; h = 0.1889 at D = 10 is a small-D artefact.
* D2: Remark (ii) threshold now log N ≳ 16πm₀/σ² ≈ 200/σ² at C = 2.
* D3: Thm 3.2 states the explicit inequality (3.1) for every admissible r, then the asymptotic.
* D4: "quasi-polynomial" → sub-polynomial N^{o(1)} (precisely c₀e^{±S_A}); cap is S′ + O(S_A).
* D5: √N density consequence relabelled PROVED (by Prop 2.3).
* D6: Lemma 2.1 uses AN/(KQ′) ≤ N/K since A ≤ Q′.
* EXCEPTIONAL_INTERFREQ2.md §9: dated notes at the top of §9, after the Prop 9.1 bold
  implication, and after the 2/5 Assessment. They say that fixed-σ SPW is refuted (Thm 3.2) and
  that Thm 5.2 needs only weak SPW, which is open. Ledger (D)26 is left to the parent.
* Background LP: N = 9100, e = 18480 gave 0.3733 (committed). The e = 30030 run did not
  finish and was killed.
