# AGENT_REPORT_O258 — Synthesis VIII over wave AA (checkpoint 1)

Branch side-agent/synthesis-eight. Deep file SYNTHESIS_SPARKS8.md; memos BRAINSTORM/s8_*.md (9, indexed in README);
scripts scripts/s8_lines.c (census engine), s8_check_b1.py (independent brute force), s8_mp_check.py, s8_genus_checks.py,
s8_proximity.py; logs logs/s8_* (tiny). **ES is not solved; no infinite case claimed.**

**R268 review (reviews/synthesis-eight-review.md): no FATAL; MAJOR M1–M4; repairs applied by the reviewer.** The census is
independently reproduced to 10⁸ (different algorithm). SHARP re-scoped (R268 repair M4): López, arXiv:2404.01508, already has
the divisor form of Prop 1.3 (his Thm 7, Type A = b = 1 line), the Type-A exceptions 193, 2521 (and 66529), and the union
conjecture (his Conjecture 1, checked to 104 729); new here is the 10⁸ census with exact failure sets, and Conjecture 2.5 as a
sharpening. R268 repair M2: DFI is NOT uniform in the numerator (explicit (a + MN)^{3/8} etc.; nontrivial only for a ≪ MN).
R268 repair M3: the (vi) "one step, two readings" holds for fixed-slice classes only (R267 D-M1). k = 8 counts are over all
primes 5 ≤ p < 8000 (39/22 over p ≡ 1 (4)) (m1).

SHARP: **The b = 1 line of Type II — equivalently, "∃ d ≥ 1: p + 4d has a divisor ≡ −1 (mod 4d)" (Prop 1.3 duality) — fails at
exactly three primes p ≡ 1 (4) ≤ 10⁸: 193, 2521, 66529 (all with p − 1 11-smooth). The union of the b = 1 and c = 1 (= (★)) lines
never fails ≤ 10⁸** (complete window decisions in C, failures confirmed by an independent brute force; T1 squares and 105
fail as they must; the k = 8 analogue fails at 34 primes < 8000 incl. 131, 241, so it is 4-specific). CONJECTURE 2.5 only —
it implies ES at those primes, so it is at least as hard. Relay suggestion: explain why the shift-4d family is far more robust
than (★) (forced levels of b = 1 are exactly the non-residues d of p — Lemma 2.2(b)); a variance comparison may say something
about the lottery margin. It will not yield a proof.

## Results by mandatory item
* (i) Least residue × height-dependent target: the single-p problem is written in four equivalent coordinates (window; twisted
  hyperbola H_u with height-dependent class, Prop 1.5; Kloosterman fraction; mutual shift pairs MP(p), Props 1.2–1.4). What
  fails, exactly (§1.7 table): Thue/Minkowski need a lattice and a fixed target. DFI 1997 IS uniform in the numerator a = p, so
  fixed p is not the obstruction. The obstruction is O(1) expected points per dyadic box, where completion leaves error
  ≥ (XY)^{1/2} even with square-root cancellation (Lemma 1.6). Continued fractions linearise −p mod y and return ET's window
  form (Prop 1.4). No route.
* (ii) Support-1 lottery: the brief's form is the b = 1 line with a prime (odd-prime support forces j even). Lemma 2.2 (PROVED):
  every b = 1 divisor is T1-visible, (w/p) = −1, and the forced levels are the non-residues d. Lemma 2.3 (PROVED):
  gcd(jp + 1, j′p + 1) | j − j′, so large primes are private to one j and any pigeonhole across j sees only congruences (B1).
  Per-j events are near-independent (mean joint/product 1.004; all-24 failure 10 vs 6.6). No deterministic mechanism; see SHARP.
* (iii) Lemma 3.1 (PROVED): (K_q/p) = (q/p), and every cap-0 certificate has (uv/p) = −1. The forced-window channel and the
  T1-adversary visibility are the same parity; routing through forced windows adds no totality (O257 still needs favourable
  witnesses). Closed.
* (iv) Lemma 4.1 (PROVED; classical in substance, the Type I form of (J)52's three-bit law): d > 0 ⟹ (d/p) = −1, d < 0 ⟹
  (|d|/p) = +1. No |d|-preserving signed→positive move; no Vieta structure (linear in each variable). Closed.
* (vi) (parent's extra item; memo s8_numerator_size_screen, §8): for 4 | k, k/n is ES restricted to solutions with
  (k/4) | gcd(x, y, z) (k-witnesses = 4-witnesses with (k/4) | d). O257's size inequality at x_{ℓ,2} = local condition at the
  primes of k + the k-free bound e ≤ a + b; 2-adically, the surviving Mordell witness has d a 2-adic unit. So it is the same
  step as (J)57's bit law: "d may be odd". Threshold-form k-uniform proofs are stronger than ES. A proof must spend the step on
  v₂(d); at 131, 241 every solution of 4/p has an odd denominator. Not sharp.
* (v) Profinite proximity to 1 (smooth p − 1): weak EVIDENCE of a few per cent beyond squareness.

## Labels / caveats for the reviewer
* Census figures rely on s8_lines.c (window form, complete to m ≤ (p + 4)/3). Cross-checks: window vs divisor form
  equal ≤ 10⁶; MP brute force ≤ 1500; brute force at the failures. The 10⁸ run takes ≈ 15 s; please re-run independently.
* Lemma 1.6's "completion error" is an Assessment about the method, not a theorem about all methods.
* The b = 1 failures being 11-smooth-(p − 1) is EVIDENCE with a selection caveat (all are small).

## Sparks (not pursued)
1. Variance/structure comparison b = 1 vs (★) (why shift 4d beats shift j).
2. 2-adic model on MP(p): do the "v₂(N) = 1" near-misses carry other-type solutions (a third line)?
3. b = 1 census beyond 10⁸ (segmented sieve), plus direct bounded-window tests on smooth-(p − 1) primes to 10¹⁵.
