# R218 — independent hostile review #2 of FF_STERILE_PUSH.md (O216)

Reviewer: R218 (side agent, branch side-agent/review-ff-push-2). Round 1. Written without reading R217.
Scripts: `scripts/review_fs2_*` (from scratch; none of the author's `fs_*` code reused).

Status: IN PROGRESS.

## Summary verdicts

(filled in at the end)

## Defects

(numbered as found)

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
the certification uses only explicit (m, k) pairs. Brute force: 0 violations of the m + k bound (ratio 1.0 attained).

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
