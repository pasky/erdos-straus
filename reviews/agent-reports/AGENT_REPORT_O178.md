# AGENT_REPORT_O178 — spark relay E: the depth aspect (prime-power moduli), checkpoint 1

Branch side-agent/spark-depth-aspect (merged side-agent/ff-sterile-point first). Deep file `DEPTH_ASPECT.md`. Memos
`BRAINSTORM/bsE_*.md` (9, indexed in BRAINSTORM/README.md). Scripts `scripts/bsE_qpow.c`, `bsE_qpow_check.py`, `bsE_famcount.c`,
`bsE_crosscheck.py`, `bsE_caseA.py`, `bsE_largeq.py`. Data `data/bsE/` (40 KB). **ES is not solved; no case of ES is claimed.**

## SHARP:
1. **O173's "square-root barrier" at depth T^s is not a barrier.** Two extra identities, E | g'T^s + w and E | T^s + m'w²
   (DEPTH_ASPECT Lemma 2.1), give Elsholtz–Tao-style divisor casework. With them the Case B slice families of parameter s
   number ≤ C^s·q^{2(s−3)/5} (Lemma 2.2, PROVED), against the cylinder weight q^{−s/2}. Case A at generic slice points
   (Lemmas 2.3–2.4, PROVED) gives ≤ C^α q^{(α−1)/2} against q^{−α}. So the covered mass decays exponentially per level. The only
   obstruction to O(3, T²) ≠ ∅ by the measure route is the explicit divisor constants, not exponents. This answers O173's
   and O179's "need 3^{(1/2−δ)K}" in exponent form: δ = 1/10, elementary. Constants are not explicit at q = 3.
2. **Theorem 2.5 (PROVED, function field): for q = 3^r with r ≥ 27 (and every odd q ≥ 1.3·10^16), and every k ≥ 2,
   ES_q(T^k, ·) has no finite linear covering.** A positive-measure part (≥ 97 %) of each c-slice is obstructed. This is the
   large-q theorem requested in the brief. It is new in char 3, where the class-1 obstruction is absent. It is at fixed q and
   all degrees, unlike O140 Thm 2.1. Proof: union bound with q-independent divisor constants; numbers from `scripts/bsE_largeq.py`.
3. **Theorem 3.1 (transfer to ℤ; PROVED relative to ET Prop 1.7's proof for N-points and MORDELL17 Lemmas 1.1, 2.1–2.3,
   Cor 4.2 for general r): for every sufficiently large prime r (effective r₀, astronomical), the r-generic line has a
   sterile point.** Hence no finite set of ET classes covers the primes p ≡ 1 (24) with least quadratic non-residue r.
   This is MORDELL17's measure criterion with ET's exponents 3/5 and 2/5 (margins 2/5 and 1/10), averaged over the (r − 1)/2
   non-residue cells. Large r absorbs the n^{C/log log n} divisor loss that kills r = 17. If it survives review, it is the first
   proved sterile Mordell point other than the square points. **Caveat:** written in one pass at the end of the session.
   DEPTH_ASPECT §3 Remark (5) lists the three steps to recheck.

## Results (labels)
* §1 (ℤ, prime-power moduli). Exact table of which ET moduli can be q^s (PROVED, elementary). Parity kill: q = 2 is impossible,
  and q ≡ 1 (4) never helps p ≡ 1 (4). Mass ≍ log²p/q^s per slice (Assessment), measured decay ≈ 1/3 per s at q = 3.
  **EVIDENCE: the q = 3 family misses 1233 of the 78496 primes ≤ 10⁶** (q = 7: 3518). Two engines agree to 7400, all solutions
  rebuilt exactly, odd squares all empty (T1 control). Lemma 1.3 (PROVED): exponential-polynomial / q-adically analytic
  witnesses serve only bounded depth. Verdict: over ℤ, prime-power moduli give a thin H-A family dominated by bounded moduli,
  i.e. B2. Depth-aspect character sums have no entry point at fixed p, since there is no interval (Assessment).
* §2 Lemmas 2.1–2.4 (PROVED), Thm 2.5 (PROVED, relative to O173 Lemmas 1.1/2.1/3.1, R166 Case A steps (1)–(2) and the ES2
  compactness criterion).
* §3 Thm 3.1 (PROVED relative to cited inputs; review needed).
* §4 EVIDENCE: exhaustive Case B counts (q = 3 to s = 15; q = 5, 7, 11), cross-validated against O173's ff3_caseB in both directions
  (0 mismatches). Case A by two independent routes (identical). The union bound at q = 3 is 1.74 (B) + 0.09 (A) > 1, so q = 3
  stays open.
* Over ℤ, a by-product: #{(c,f,g): cfg − c − f = n} ≪ n^{1/3+o(1)} (PROVED, elementary, likely folklore).

## What I did not do
* Exact union census for q = 3 (overlaps), or averaged divisor bounds that might close q = 3 (memo bsE_q3_explicit_constants).
* F_9 / F_27 enumeration (prime fields only).
* Explicit r₀ for Thm 3.1; a check of whether MORDELL17 R83 already noted large-r convergence (I found no such remark in §4).

## Sparks
* Make Thm 3.1 explicit: Nicolas–Robin divisor bounds + ET's casework with explicit constants gives a concrete r₀. Then ask
  how far down averaging (instead of max divisor bounds) brings it.
* q = 3 closure programme: exact census to s ≈ 20 plus averaged divisor sums in APs mod T^s (exact in F_q[T] for long APs).
* The Case A(α) ↔ Case B(α + 1) count coincidence (memo bsE_caseAB_shift): find the bijection (type swap a ↔ X/a?).
* O179's x*_c reduction plus Lemma 2.2's identities: a point-specific (not measure) argument at x*_c might use (R3)/(R4) with
  the forced T-adic digits of u = 1 + cT.
* Large-r sterile points for the main (non-np) Mordell variant, and for the r = 13 two-prime cells (T = {11, 13}: T-generic
  boxes with two depths). Is there a "large T" analogue?
