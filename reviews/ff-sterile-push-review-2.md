# R218 — independent hostile review #2 of FF_STERILE_PUSH.md (O216)

Reviewer: R218 (side agent, branch side-agent/review-ff-push-2). Round 1. Written without reading R217.
Scripts: `scripts/review_fs2_*` (from scratch; none of the author's `fs_*` code reused).

Status: round 1 complete. **No FATAL, no MAJOR.** 8 MINOR.

**Repairs applied (round 2):** m-1..m-8 applied to FF_STERILE_PUSH.md (marked "(R218 repair m-…)"), m-8 in `scripts/fs_caseA.py`, report line in `reviews/agent-reports/AGENT_REPORT_O216.md`; consolidated with R217: m-3 with R217 m5 (constants at r = 5, 6), m-4 with R217 m1/m2 (certified finite-level failure at r = 3; added the s = 36 crossing and the exact critical point (1/3, 1/3, 1/6, 1/6)), m-5 into the status line together with both reviews.

## Summary verdicts

| claim | verdict |
|---|---|
| **Theorem 3.1** (q = 3^r, r ≥ 4, k ≥ 2: O(q, T^k) ≠ ∅; (a) r = 4 sum ≤ 2.18; (b) r ≥ 5 per-c bounds) | **SOUND** (independently re-certified with own code: r = 4 ≤ 1.831; r = 5 ≤ 0.251; r = 6 ≤ 0.039 with S = 100; r = 7 ≤ 0.0117; r = 8 ≤ 0.0032; r = 9 ≤ 0.00103; 10 ≤ r ≤ 30 ≤ 3.5·10⁻⁴) |
| reduction to (Σ) / inherited inputs (O173 1.1, 2.1 via R187; R166 Case A; compactness) | SOUND (no input beyond Thm 2.5's) |
| Lemma 1.1 (E·v = T^s + m'w², y + t = max(a, b)) | SOUND (m-1: simpler proof available) |
| Lemma 1.2 (loss-free routes) | SOUND |
| Lemma 1.3 | SOUND |
| **Lemma 1.4** (FF Lenstra, ≤ 2 if 3ρ > n) | **SOUND** (proof re-derived; adversarial brute force F₃, F₅, F₇: 0 violations, bound attained) |
| **Lemma 1.5** (FF Coppersmith, (C) ⇒ ≤ m + k; threshold ρ > d(n − d)/n) | **SOUND** (m-2: asymptotic sentence garbled; unused) |
| Lemma 1.6 (19 routes, R10 with Σ2^ω) | SOUND (every row re-derived; Σ2^ω closed form brute-forced; per-pattern brute force 0 violations) |
| Lemma 2.1 (averaging over c) | SOUND |
| Lemma 2.2 (Case A routes, α ≥ 3) | SOUND (small-depth part unused, m-6) |
| certification fs_certify.sh / fs_sum.c / fs_tail.c / fs_caseA.py | SOUND (audited line by line; fails closed; rounding margin ample; values reproduced or beaten by an independent implementation, exact-rational cross-check to 16 digits) |
| §3 r = 3 barrier | SOUND as EVIDENCE/Assessment; understated (m-4: a CERTIFIED negative statement is available) |
| §4 char 2 Frobenius family covers each u(0) = 1 c-slice (k = 2) | SOUND |
| §5 (S1)–(S3) equivalence at q = 3 | SOUND (PROVED; numerical check vacuous, algebra re-derived) |
| §5 census 94/27, M2 count | SOUND (94/27 reproduced exactly; v₁ = −1 count 5.6·10²¹ at s = 244 ≥ claimed 7.8·10¹⁰) |
| labels (Conjecture 0.2 not proved; r = 3 barrier EVIDENCE/Assessment) | SOUND (m-5 hygiene) |

## Defects (all MINOR)

**m-1 (MINOR, Lemma 1.1(ii) proof).** The identity y + t = max(a, b) is immediate from g'v = w + C (w, C monic, q odd ⇒
deg(w + C) = max(a, b)); the route via E·v and deg(T^s + m'w²) is correct but roundabout, and DEPTH_ASPECT §2.1 only had
"≤". *Repair:* add the one-line proof; keep (i) since E·v = T^s + m'w² is used by R4/R4'.

**m-2 (MINOR, Lemma 1.5 last sentence of proof).** "minimising over 1 + τ = X^{−1/2}·… gives the condition √(nX) < d" is
garbled. *Repair:* "f(τ) = (1 + τ)d − (n + X)/2 − τX − τ²X/2 is maximised at τ = ρ/X (1 + τ = d/X), where
f = d²/(2X) − n/2; so (C) holds for large m iff X < d²/n." (I verified this algebra.) Add that only explicit (m, k) are
used by the certificate.

**m-3 (MINOR, Thm 3.1(b) constants, optional).** The r = 5, 6 constants are artefacts of the small cutoff S: with S = 160
(r = 5) and S = 100 (r = 6) my certified totals are ≤ 0.1746 and ≤ 0.0386 (uncovered ≥ 0.82 and ≥ 0.96 per slice) instead
of 0.26 and 0.38; similarly the non-monotone tails at r = 17, 19, 20 in data/fs/certify.txt are box overhead. Not an error;
*repair (optional):* raise S for r = 5, 6 or add a sentence that the constants are not optimised.

**m-4 (MINOR, §3 "Where the method stops", and §5(b)).** The text says fs_tail "fails to certify 835 boxes (a failure to
certify, not a negative result)" and the r = 3 finite sums are "not a proof of divergence". But the *finite* part of (Σ)
computed with the Lemma 1.6 bounds already exceeds q − 1 = 26 at s = 36 (27.68; 195.06 at s ≤ 150; fs_sum gives
195.60). So "the union bound (Σ) with the Lemma 1.6 route bounds fails at r = 3" is CERTIFIED (finite exact computation),
independent of any tail. *Repair:* state this (with the s = 36 crossing), keeping "no proof that every union bound
fails" as Assessment. Also note the exact critical point: at (a, z, y, t)/s = (1/3, 1/3, 1/6, 1/6), R1 = 1/6 + log 3/log 27
= 1/2 and the R10 Coppersmith threshold ab/(a + b) = 1/6 = t, both exactly — cleaner than the grid point quoted.

**m-5 (MINOR, label hygiene).** Header says "Theorem 3.1 (r ≥ 4) certified", the theorem says "PROVED, computer-assisted".
The computation is floating point with a ×1.01 safety factor and an informal error estimate, not interval arithmetic.
I find the margin ample (my exact-rational evaluation agrees with long-double sums to 16 digits for r = 4, s ≤ 60), so
"PROVED (computer-assisted)" is acceptable, but use one label consistently and cite an exact cross-check (e.g. this
review's `review_fs2_exact.py`) in the proof text.

**m-6 (MINOR, Lemma 2.2).** The small-depth statement (Case A has α ≥ 3) is not used by the certificate (fs_caseA sums
from α = 1). *Repair:* say so, or start the sum at α = 3 and cite the lemma. Its proof also silently assumes b1, F monic
(true by DEPTH_ASPECT Lemma 2.4's "E, F, K monic" since α > β); cite that.

**m-7 (MINOR, accuracy of the description of cls).** Lemma 1.6 says cls uses "the least ... m + k over (m, k) satisfying
(C)"; fs_sum.c / fs_sum_check.py search only m ≤ 60, k ≤ 200 (with a correct early break). Any valid (m, k) gives a valid
bound, so this is conservative (my unrestricted search over m + k ≤ 200 finds smaller values for 22 344 of 10.7M triples
(n ≤ 400) and never a larger one; e.g. at r = 4 the total drops from 1.67692 to 1.67548). *Repair:* say "least over
m ≤ 60, k ≤ 200". Note also that fs_sum_check.py copies this search, so its agreement with fs_sum is not fully
independent on this point (it is independent on the arithmetic).

**m-8 (MINOR, fs_caseA.py tail).** The α > 40 majorant is computed in floats and uses q^{−a0/2} where q^{−(a0+1)/2} is
available (conservative); the unused variable `first` is computed in exact arithmetic and discarded. Harmless; tidy up.

## Per-claim notes

### Lemma 1.1 (degree identity) — SOUND
Re-derived. (i) is DEPTH_ASPECT Lemma 2.1 (R4) rewritten with m'wC = T^s + v; correct. (ii) is correct, but the E·v detour is
unnecessary: g'v = w + C with w, C monic and q odd gives deg(w + C) = max(a, b) directly (lc 1 or 2), hence y + t = max(a, b)
(m-1 below). (iii) correct (v₁(0) = m'(0)w₁(0)C₁(0) ≠ 0 since s ≥ 3).
*From-scratch check* (`scripts/review_fs2_brute.py`: enumerates all monic (m', w, C) with the T-conditions for every
degree split, solves for v, g' directly from (B), no use of bsE_famcount): asserts y + t = max(a, b), E v = T^s + m'w²,
E'v = T^s + m'C², T² ∥ v (v₁(0) ≠ 0) and gcd(w₁, Tv₁) = 1 for **all** tuples with p = 3, s ≤ 15; p = 5, s ≤ 9;
p = 7, s ≤ 8 — 0 failures. Tuple totals 122 (p = 3, s ≤ 13) + 32 + 28 = 182, matching the document's "182 tuples".

### Lemma 1.2 (loss-free routes) — SOUND
All four reconstructions re-derived; the counts N*(·) are right (v₁ has fixed lc = lc(w + C) and v₁(0) ≠ 0).

### Lemma 1.3 — SOUND (standard).

### Lemma 1.4 (FF Lenstra) — SOUND
Proof re-derived line by line: (L) is exact; Λ-determinant argument: σ₀(u_x u'_y − u_y u'_x) ≡ 0 (mod Q), degree ≤ X + Y =
n − 2ρ < ρ, so all differences are F_q(T)-collinear; b primitive ⇒ α ∈ F_q[T]; b_x = 0 excluded since Y < ρ; the
α-polynomial is non-zero of degree ≤ 2 (α²-coefficient b_x b_y Q, or α-coefficient b_x e₀ when b_y = 0). The trivial cases
(d < ρ; n − d < ρ) need only that σ is a unit mod Q (τ₀ ≡ Fσ₀⁻¹ is then unique), which is a hypothesis.
*Brute force* (`scripts/review_fs2_lemmas.py`, own code): moduli chosen **adversarially** (Q = monic gcd of differences
of 2–3 divisors of F of equal degree, and its divisors, plus random Q), all scalar multiples of divisors included, only
unit classes. See the Lemma 1.5 paragraph for the counts. 0 violations; the bound 2 is attained (ratio 1.0), so the
search does reach the extremal configurations.

### Lemma 1.5 (FF Coppersmith–Howgrave-Graham) — SOUND (statement and finite form); asymptotic remark sketchy
Re-derived: E | F₁ since E is prime to Q; Q f(x₀) ≡ E (mod E) and Q is a unit mod E, so E | f(x₀); E^m | g_i(x₀), h_j(x₀);
the coefficient embedding P ↦ (p_l T^{lX}) is triangular with diagonal degrees (m − i)deg F₁ + iX and (m + j)X, so
deg det ≤ Δ(m, k); exact Siegel pigeonhole gives deg p_l + lX ≤ ⌊Δ/N⌋ < md, so P(x₀) = 0, ≤ m + k roots. Correct.
The asymptotic sentence ("minimising over 1 + τ = X^{−1/2}·… gives √(nX) < d") is garbled (m-2) but is **not used**:
the certification uses only explicit (m, k) pairs. Brute force (`scripts/review_fs2_lemmas.py`): p = 3: 400 random highly factorable F (deg 6–13), 323 468 (Q, d)-groups;
p = 5: 200 F, 368 129 groups; p = 7: 120 F, 347 056 groups — **0 violations** of the trivial bound, of Lemma 1.4's 2 and of
Lemma 1.5's m + k; each bound is attained (max count/bound = 1.0), so the adversarial moduli reach the extremal cases.

### Lemma 1.6 (route table) — SOUND
Every row re-derived from Lemmas 1.1–1.5 and DEPTH_ASPECT Lemma 2.1: polynomial degrees (s + 2y + z; s − 1 + y; s − 2
(= deg(T^{s−2} + m'w₁²), lc 2 when z + 2a = s); z + 2b − 2; s − 1 − a; a + b − 2), divisor degrees, modulus degrees
(TL': y + z + 1; Tw₁g': a + y; Tm'w₁: a + z; Tv₁: t − 1), the unit property of every class and the coprimality used
for the cofactor versions (R2: F ≡ 1 mod TL'; R4/R4C: common prime would divide T^{s−2}; R5/R10: prime to Tv₁ by
Lemma 1.1(iii)); R3/R3C correctly E-version only. R10: ≤ 2 square roots of a unit modulo each prime power (q odd,
(1 + P)/(1 + P^e) is a 3-group), so ≤ 2^{ω(Tv₁)} = 2·2^{ω(v₁)} classes. The closed form
Σ_{deg v = e, monic} 2^{ω(v)} = q^e(2 + (e − 1)(1 − 1/q)) was verified by brute force for q = 3, 5, 7, e ≤ 5 (14 cases, exact).
*Brute force*: for every pattern hit by a real tuple (p = 3, s ≤ 15; p = 5, s ≤ 9; p = 7, s ≤ 8) the exact count is
≤ the minimum of my own implementation of the 19 rows (`scripts/review_fs2_bounds.py`); 0 violations, max ratio 1.000.
(Caveat: at these tiny p, s most rows are not binding; this is a sanity check, the proof is the derivation above.)

### Lemma 2.1 (averaging over c) and Lemma 2.2 (Case A) — SOUND
Lemma 2.1: a Case B cylinder u ≡ −E (mod T^{N+1}), N ≥ 1, and a Case A cylinder (mod T^{k+α}) both fix u mod T², i.e. c;
summing covered masses over the q − 1 slices is ≤ LHS(Σ); then #{c : covered ≥ θ} ≤ LHS/θ. Correct; no new hypothesis.
(a) of Thm 3.1: #{c : covered ≥ 1/2} ≤ 2.176/0.5 < 5, so ≥ 76 (claimed ≥ 75) slices have > 1/2 uncovered. Correct.
Lemma 2.2: all six routes re-derived from DEPTH_ASPECT (A0)–(A4): (A1) EF = T^α a1' + b1, E ≡ −1 (Ta1'b1) [gcd(a1', b1) = 1,
T | K], deg = α + λ; (A2) zE = T^α + b1²K, E ≡ −1 (b1K), deg = max(α, 2β + κ) (no cancellation: both monic); (A3) multinomial
for the monic degree-α polynomial T^α + z, z ∈ T·F_q[T] of degree ≤ ζ: q^ζ choices; (A4) and the quadratic. The trivial
"n − d < ρ ⇒ 1" class bound used in fs_caseA for route (iii) is legitimate although T^α + b1²K need not be prime to b1K
(both are divisible by T): Lemma 1.4's trivial case needs only σ = −1 a unit. Dropping g' from the count is right
(cylinder depends on (E, α) only). The small-depth claim (α ≥ 3) is correct but **unused**: fs_caseA sums from α = 1.
Independent recomputation (`scripts/review_fs2_caseA.py`, exact rationals, own code; tail α > 40 from DEPTH_ASPECT Lemma 2.4
as an exact rational geometric majorant): exact part 8.4882704620e-4 (r = 4), 8.7646411455e-5 (r = 5), 9.5155829299e-6
(r = 6) — identical to fs_caseA to 11 digits; my α > 40 tail is smaller (fs_caseA uses q^{−α/2} where q^{−(α+1)/2} is
available — conservative, fine). Without any class bound the totals change by < 3 %: Case A is negligible everywhere.

### Certification of (Σ) (fs_certify.sh / fs_sum.c / fs_tail.c) — SOUND (independently re-certified)
**Code audit of fs_tail.c (the rigour-critical part).** Checked every route against Lemma 1.6: the per-unit-s exponents
use N*(d) ≤ q^d at the box's upper corner; every binomial is first enlarged to an unshifted one (C(s−1+y, a+y+z) ≤
C(s+y, a+y+z); C(s−2, t−2) ≤ C(s, t); C(z+2b−2, t−2) ≤ C(z+2b, t); C(s−1−a, b−1) ≤ C(s−a, b); C(a+b−2, a−1) ≤ C(a+b, a);
multinomial with (z, a−1, b−1) ≤ G(z, a, b)) — all correct; B and G are increasing and 1-homogeneous, so the upper corner
bounds them. R10: Σ2^ω ≤ (t − 1)q^{t−2} ≤ (s + 1)q^t, factor 2 for 2^{ω(T)}, polys = 1 — correct. Class conditions are
checked as linear inequalities with integer shifts, for all s ≥ S, in exact dyadic arithmetic (all box corners are
dyadic with ≤ 10 bits, coefficients small integers, so no rounding occurs in these tests). Pattern count per box
(sw + 1)³ ≥ #integer points; boundary double counting only overcounts; pruning (a0 + z0 + y0 > 1, 2a0 + z0 > 1) is correct.
Geometric tail: P(s+1)/P(s) ≤ ((s+2)/(s+1))³ holds for w ≤ 1 (cross-multiplication gives w ≤ 1), and the bound is
decreasing in s, so term·ρ/(1 − ρ) dominates the remainder. q^{1−⌈s/2⌉} ≤ q^{1−s/2}. Fails closed (failed box or non-finite
total ⇒ exit 1; set -euo pipefail in fs_certify.sh; Python exits 1 if total ≥ q − 1). Floating point: the only
non-exact operations are log/exp/pow in double on moderate arguments; with the 1.01 factor the margin is ≫ the rounding.
No defect found in the tail logic.
**Independent recomputation (own code, different implementation choices).**
* Finite part: `scripts/review_fs2_sum.c` (long double, minimal Coppersmith m + k over all m + k ≤ 200 found by exact
  integer search, Kahan summation, ×(1 + 10⁻⁸)), cross-checked by `scripts/review_fs2_exact.py` (exact rationals,
  Python big integers) — **agreement to 16 digits** for r = 4, s ≤ 30 (1.435880509176952) and s ≤ 60 (1.656037212202324).
  Values: r = 4, s ≤ 200: **1.675485** (fs_sum: 1.676921; mine is smaller because fs_sum's Coppersmith search is
  restricted to m ≤ 60 and stops early — conservative, harmless); r = 5, s ≤ 100: 0.1744531 (fs_sum 0.1745084);
  r = 6, s ≤ 60: 0.0385984 (fs_sum 0.0386052); r = 7: 0.0103174 (0.0103182). Per-s terms agree with fs_sum to 10 digits
  for s ≤ 12 and differ by < 0.2 % later, always in the conservative direction for fs_sum.
* Tail: `scripts/review_fs2_tail.c` — own adaptive octree, a different summation (closed-form unimodal sum + integral
  bound of Σ (s+1)^{3+p}e^{gs}, using sh + 1 ≤ (s+1)(h + 1/(S+1))), class conditions combined into a single linear form
  before taking the sup, a node's bound = min(own, sum of children). r = 4 (S = 200): ≤ 0.148; r = 5 (S = 100): ≤ 0.0763;
  r = 6 (S = 60): ≤ 0.399; r = 7: ≤ 1.35·10⁻³.
* Case A: as above.
* Totals (`scripts/review_fs2_certify.sh`, log `data/review_fs2/certify.txt`): **r = 4: ≤ 1.831 < 80; r = 5: ≤ 0.2509;
  r = 6: ≤ 0.4373; r = 7: ≤ 0.01167; r = 8: ≤ 0.003176; r = 9: ≤ 0.001029; 10 ≤ r ≤ 30: ≤ 3.42·10⁻⁴.** Every claimed
  constant of Thm 3.1(a)/(b) is confirmed except that my S = 60 bound at r = 6 (0.437) is weaker than the claimed 0.38;
  with S = 100 at r = 6 my bound is **0.0386 + 4.7·10⁻⁶ + 10⁻⁵ ≤ 0.039**, so the claim "≤ 0.38" holds (and is
  very loose: m-3). Likewise r = 5 with S = 160: ≤ 0.1746 (claimed 0.26). The tail at S = 60 is pure box overhead.

### Theorem 3.1 as a whole — SOUND (PROVED, computer-assisted, relative to the stated Thm 2.5 inputs)
Reduction re-derived: (Σ) ⇒ (Lemma 2.1) some c-slice has positive uncovered measure ⇒ O(q, T^k) ≠ ∅ ⇒ no finite linear
covering (FUNCTIONFIELD_ES2 §0.1). The inherited inputs are used within their hypotheses and **no input beyond those of
Thm 2.5 is used**: the Case A/B split and cylinder form (O173 Lemma 1.1, re-derived in R187 §2.1 item 8); (B) with T² | v,
T ∥ w, T ∥ C (O173 Lemma 2.1(a),(b), R187); nested cylinders N ≥ N(s) (γ ≤ j); R166 Case A steps (1)–(2) (only
E ≡ −u (mod T^{k+α}) with u ≡ 1 + cT (mod T²) is used, as in DEPTH_ASPECT §2.2); k-monotonicity (N(s) and the Case A
exponent increase with k, the tuple sets do not depend on k). Uniformity: the route bounds are uniform in c and the
counts are over all tuples; no constant depends on s beyond what is summed. w ↔ C symmetry is a bijection of (B)
preserving s and swapping (a, b), so the multiplicities 2/1 are right. r ≥ 31 rests on Thm 2.5 (r ≥ 27), so the two
ranges overlap. All stated constants (a), (b) are confirmed by my independent certificate (section above).

### §3 "Where the method stops: r = 3" — SOUND as EVIDENCE/Assessment, but understated (m-4)
My continuum computation (`scripts/review_fs2_rate.py`, own code, grid + local search) confirms the critical point: at
(a, z, y, t)/s = (1/3, 1/3, 1/6, 1/6) the R1 exponent is t + G(1/3, 1/3, 1/3)/log q = 1/6 + log 3/log 27 = **1/2 exactly**
at q = 27, and the R10 Coppersmith threshold ab/(a + b) = 1/6 = t is met with equality there; nearby the sup of min-route
is −8·10⁻⁵ → 0⁻. So r = 3 is exactly critical for these route bounds (author: "0.000", "R1 and R10 meet exactly" — confirmed;
the author's quoted location (0.31, 0.325, 0.20, 0.168) is a grid point near this exact point). At r = 4 my grid gives
−0.024 (author −0.027): both negative; EVIDENCE only, and the certificate does not depend on it.
**But:** the finite part of (Σ) with the Lemma 1.6 bounds at r = 3 already exceeds q − 1 = 26 at **s = 36 (27.68)** and is
195.06 at s ≤ 150 (my code; fs_sum gives 195.60). So this union bound *provably* cannot give (Σ) at r = 3 — independent
of any tail — which is a CERTIFIED negative statement the document misses; it currently says only that fs_tail "fails to
certify" and that per-s terms are ≈ 2 "not a proof of divergence".

### §4 characteristic 2 (Frobenius family) — SOUND
Re-derived with the linear-family definition of FUNCTIONFIELD_ES §6.2: family (E; 0, g'; 2, g'), A = T², a = g',
b = X/g', X = (P + E)/T². At a c-slice point: T² | P + E (u ≡ 1 + cT ≡ E, char 2); P + E ≡ 1 + 1 = 0 (mod g') and
gcd(g', T) = 1, so g' | X; gcd(g', E) = gcd(T + c, 1) = 1, X ≡ T⁻² (mod E), so s ≡ (T²g'² + 1)/(T²g') = E²/(T²g') ≡ 0;
s, E monic. The NC identity A/P = 1/X + 1/Y + 1/Z with κ = s/E then holds formally. The k = 2m generalisation is also
right (E = 1 + T^m g', g' ≡ h (mod T^m)). Scope correctly limited to u(0) = 1 (repair m7).
*Check* (`scripts/review_fs2_char2.py`, own code, F₂ and F₄ via python-flint): 180 random instances per field (m = 1, 2, 3;
random g', random large-degree monic P in the slice with P ≡ 1 mod g'E), all valid, identity verified.

### §5 reformulation (S1)–(S3) at q = 3 — SOUND (PROVED)
Both directions re-derived: forward: from C₁E = g'T^{2n−1} + w₁ and E ≡ −u (mod T^{n+1}), w₁ ≡ −uC₁ (mod T^{n+1}) (needs
2n − 1 ≥ n + 1, i.e. n ≥ 2), then with w₁ + C₁ = Tg'v₁: w₁(1 − u) ≡ −uTg'v₁, i.e. w₁ ≡ c u g'v₁ (mod T^n); the expansion
m'w₁C₁ = −m'g'²v₁²u − cm'g'v₁T^nω(cT − 1) − m'T^{2n}ω² (uses u + 1 = cT − 1 in F₃, c² = 1) is right, and (S1)–(S3)
follow as stated. Converse: (E + u)C₁ = g'T^{2n−1} − cT^{n+1}ω, as stated. (S1) ⇒ z + 2y + t ≥ n + 1 since P ≠ 0.
*Brute force* (`scripts/review_fs2_s5.py`): all tuples with s = 2n ≤ 14, c ∈ {1, 2}: LHS ⟺ RHS on every tuple —
**but the test is vacuous** (no tuple covers x*_c in that range, consistent with FF_STERILE_PROOF), so the equivalence rests
on the algebra above (which I checked). The doc does not claim a numerical check; fine.
§5(a) census 94/27: **reproduced exactly** by my enumerator (q = 3, s ≤ 15; tuple counts per s 2, 4, 10, 8, 8, 4, 24, 12,
14, 36, 104, 48 for s = 4..15, identical through s = 13 to R187's list).
§5(b) M2 repair (count at v₁ = −1, s = 3^h + 1, not polynomial): checked by exact DP over the factorisation of T^{3^h−1} − 1
(`scripts/review_fs2_m2.py`, cross-checked by direct enumeration at h = 2, 3: 12 and 1116 tuples). Exact counts of tuples
with v₁ = −1: 9.63·10⁸ (s = 82), **5.60·10²¹ (s = 244)** ≥ the claimed 7.8·10¹⁰ (which is a sub-count at the thirds
corner). Growth ≈ 3^{#factors} = exp(Θ(s/log s)) as claimed.

### Labels — mostly SOUND
Conjecture 0.2 is nowhere claimed proved; "ES not solved" is stated; the r = 3 barrier is labelled EVIDENCE + Assessment;
§4 ℤ-paragraph is Assessment. Minor inconsistencies: m-5, m-6.

## Replay (reviewer scripts)
```
uv run --with python-flint python scripts/review_fs2_brute.py 3 15     # also 5 9, 7 8: Lemma 1.1 + route bounds + census 94/27
uv run --with python-flint python scripts/review_fs2_lemmas.py 3 400 7 # also 5 200 8, 7 120 9: Lemmas 1.4/1.5
gcc -O2 -o /tmp/rfs2_sum scripts/review_fs2_sum.c -lm && /tmp/rfs2_sum 4 200 20
uv run python scripts/review_fs2_exact.py 4 60                         # exact rationals, cross-check of review_fs2_sum
gcc -O2 -o /tmp/rfs2_tail scripts/review_fs2_tail.c -lm && /tmp/rfs2_tail 4 200 9 0.001
uv run python scripts/review_fs2_caseA.py 4,5,6 40
./scripts/review_fs2_certify.sh                                        # r = 4..30 -> data/review_fs2/certify.txt
uv run python scripts/review_fs2_rate.py 150 1,2,3,4,5,6               # continuum exponents (EVIDENCE)
uv run --with python-flint python scripts/review_fs2_char2.py
uv run --with python-flint python scripts/review_fs2_s5.py 14
uv run --with python-flint python scripts/review_fs2_m2.py
```
