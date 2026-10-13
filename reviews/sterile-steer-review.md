# R188 — hostile review of O188 STERILE_STEER.md (+ BRAINSTORM/bsM_*.md)

Reviewer: side agent R188 (branch side-agent/review-sterile-steer). Reviewed: STERILE_STEER.md as merged from
side-agent/sterile-steer (checkpoint 1), memos bsM_*.md, AGENT_REPORT_O188.md. From-scratch scripts:
`scripts/review_ss_*.py` (none of the author's code is reused; `mordell_lib` is used only as an *a posteriori*
cross-check of my own class tables).
Sources checked: Elsholtz–Tao arXiv:1107.1010 (sources/elsholtz-tao-1107.1010.pdf, text read directly).

**ES is not solved; nothing in O188 claims otherwise, and nothing in this review changes that.**

## Summary verdicts

| Claim | Verdict |
|---|---|
| §1 Lemma 1.1 (escape) | SOUND (minor wording, D6) |
| §2 EVIDENCE (r = 17, u = 5, 180 cases) | SOUND (independently reproduced; D7 duplicates, D8 "2.5B") |
| Prop 3.1 (S closed; ES(p) ⟺ p ∉ S; SQ ⟺ S ∩ ℕ_odd = odd squares) | SOUND-AFTER-REPAIRS (wrong citation, D1; Type I/II vs N-point wording, D2) |
| Prop 3.2 (divergent side, second Borel–Cantelli) | SOUND (BC II not even needed, D4) |
| Cor 3.3 (density 1/4) | SOUND; the "Reading" overstates what it says about integers (D3) |
| §4 Lemma 4.1 | SOUND for odd r; false for r = 2 (D5) |
| §4 Lemma 4.2 | SOUND (D15 wording) |
| §5 Prop 5.1(a) | SOUND relative to the stated inputs (D11 normalisation) |
| §5 Prop 5.1(b) | SOUND |
| §5 Reading ("unique bounded-modulus shot", "every infinite pattern divergent", "exactly the signature") | GAP as worded (D9, D10) |
| §6 r₀ table (Assessment) | numbers SOUND; one wrong scaling law (D12), one inconsistent input at r = 17 (D13), one overclaim (D14) |
| §3 13-line remark (A_13 = ∅ via moduli 39, 143) | SOUND (reproduced) |
| Labels overall | appropriate except D3, D9, D14 (framing) |

## Claim-by-claim

### Prop 3.1

Re-derived from ET's text. (i) *Class ⇒ N-point at every n ≥ 1.* I re-checked the seven ET §10 tuples
(ET p. 37–38) for positivity at every n ≥ 1 in the class, not just n large: I1 c = (n+f)/4ad ≥ 1 and
b = ce − a > 0 because ce = (n+f)(4a²d+1)/(4adf) > a; I2, I3, II3 all coordinates are quotients of positive
integers; I4 f = na/b + (a+b)/(be) > 0; II1 f = 4acd − 1 ≥ 3; II2 ce = (f+1)(n+4a²d)/(4adf) > a. So every n ≥ 1 in
a class has an N-point of Σ^I_n or Σ^II_n, i.e. an element of V_I(n) ∪ V_II(n), and hence an ES solution via π^I / π^II.
Numerically confirmed by `scripts/review_ss_classes.py` (below). (ii) *N-point ⇒ class.* V_I: 4abd = ne+1,
a+b = ce gives e(4acd − n) = 4a²d + 1, so f := 4acd − n ≥ 1, f | 4a²d+1, n ≡ −f (mod 4ad): I1 class (a, d, f).
V_II: 4abd = n+e gives e(4acd − 1) = n + 4a²d, so with f := 4acd − 1, 4ad | f+1 and n ≡ −4a²d (mod f): II2 class.
Both hold with **no coprimality hypothesis**, which is what (b) needs for composite n. (iii) For an odd prime p
every solution of 4/p has p dividing one or two denominators (none: p | 4xyz impossible; three: RHS ≤ 3/p), and
ET Props 2.2 / 2.6 put Type I / II solutions on Σ^I_p / Σ^II_p. p = 2 lies in II2(1,1,3) = {n ≡ 2 (3)}.
(iv) S is the complement of a union of clopen sets, hence closed. (v) SQ as recorded in DISCOVERIES (J)-list is
literally "V_I(n) ∪ V_II(n) = ∅ ⟺ n square, n odd", so by (i)–(ii) it is S ∩ ℕ_odd = odd squares. SOUND, with D1, D2.

### Prop 3.2

ν_T makes the x_q (q ∈ T) independent, each uniform on the non-squares of ℤ_q^×; reduction mod q maps this
uniformly onto the (q−1)/2 non-residues, so P(x_q ≡ −4 mod q) = 2/(q − 1) when q ≡ 3 (4) (−4 is then a non-residue)
and 0 when q ≡ 1 (4). II2(1,1,q) needs 4·1·1 | q+1, residue −4 mod q: correct (checked against ET's family
"−4a²d mod f, 4ad | f+1"). The off-T coordinates (x = 1) play no role because the modulus of II2(1,1,q) is q.
Σ 2/(q−1) = ∞ along T ∩ {q ≡ 3 (4)} gives P(no event) = ∏(1 − 2/(q−1)) = 0. SOUND (D4: only *one* event is needed).
Measure: ν_T is a product of probability measures, well defined for infinite T. No hidden uniformity issue.

### Cor 3.3

For n > 0 not a square, the Kronecker character χ_D of ℚ(√n) is non-trivial and ≠ χ_{−4} (ℚ(√n) is real), so
χ_{−4} and χ_D are independent quadratic characters and {q : q ≡ 3 (4), (n/q) = −1} has Dirichlet density 1/4
(no Chebotarev needed beyond Dirichlet for the biquadratic field). Primes q | n are excluded because n_q is not a
unit. SOUND. But see D3 on the "Reading".

### §1 Lemma 1.1

x(p) ∈ C ⟺ (p ≡ ρ mod M_r and 1 ≡ ρ mod M'); with p ≡ ρ (mod M) this is M' | p − 1. (b): if v_r(M) ≤ L and
M' | p − 1 then x(u)_r = u ≡ p ≡ ρ (mod M_r) and x(u)_q = 1 ≡ p ≡ ρ (mod q^v), so x(u) ∈ C, a box of level v_r(M) ≤ L.
"E = 1 impossible": E = 1 means M | p − 1, so 1 ∈ C; but 4/1 = 1/x+1/y+1/z has no solution (RHS ≤ 3) while
every n ≥ 1 in a class has one (Prop 3.1(i)). SOUND. D6 is wording only.

### §4 Lemma 4.1

Limit set: for μ ∈ Ẑ, m_i → ∞ with m_i → μ in Ẑ gives 2-component k·2^{m_i} + c → c and q-components → k·2^μ + c
(m ↦ 2^m mod q^j is periodic, so extends continuously to Ẑ). For **odd** r the proof is right. For r = 2 the
r-generic line imposes nothing at 2, and c = −1, k = 2^j gives ν(1 − j) = (−1 at 2, 1 at every odd q), a point of the
2-generic line (e.g. Mersenne numbers 2^m − 1, μ = 1). See D5.

### §4 Lemma 4.2

On Λ_k the 2-component is the constant c, so the 2-part of the class condition is all-or-nothing. For M' odd with
gcd(k, M') = 1, k·2^μ + c ≡ ρ (mod M') ⟺ 2^μ ≡ k⁻¹(ρ − c), one target value g; μ ↦ 2^μ mod M' factors through the
surjection Ẑ → ℤ/ord_{M'}(2), so Haar measure pushes to the uniform measure on ⟨2⟩. Measure = 1/ord or 0. SOUND.
Brute-force check (`scripts/review_ss_misc.py`): for k ∈ {9, 27, 105}, c = ±1, all classes of modulus ≤ 400 with
gcd(k, M') = 1: the measure computed by enumerating μ mod ord is always 0 or 1/ord (never > 1 solution).
The consequence "Sierpiński-type finite coverings become possible, as O185 found for k = 9 and 27" matches
EXPONENT_COVERING.md on side-agent/exponent-covering (k = 9 covered at M = 464 844; k = 27 example §2); O185 takes
k odd, consistent with gcd(k, M') = 1 being the generic case.

### §5 Prop 5.1

(a) The level-1 boxes on the q-line are: Q/Q⁻¹/U/U⁻¹ boxes at k = 1 (≤ 6f(q) by DEPTH_ASPECT §3 / MORDELL17 Lemma 1.1,
2.1–2.2 transferred to general r) and P-boxes with ⌈K/2⌉ = 1, i.e. K ∈ {1, 2}. The author's "K = 2 contributes
nothing" is right: the Jacobi argument of MORDELL17 Lemma 1.3 (for a P-datum, −r^K d'(2a')² ≡ 1 (mod f) and
(−d'/f) = −1 since f ≡ −1 (mod 4d')) gives (r^K/f) = −1, so K is odd, for every odd prime r (I re-did it; nothing
uses r = 17). Each box has Haar measure 1/q, so the union has measure ≤ (6f(q) + 2f_II(q))/q, and ET Prop 1.7
(f_I(n) ≪ n^{3/5+O(1/log log n)}, f_II(n) ≪ n^{2/5+…}, f(p) = 3f_I(p) + 3f_II(p) for odd primes — checked in the PDF)
gives ≪ q^{−2/5+o(1)}. SOUND relative to the DEPTH_ASPECT transfer (still under R178/R187), as labelled. D11 is cosmetic.
(b) −φ a non-square mod 𝔮 and 4φ^{2k} a square, so −4φ^{2k+1} runs over the coset −4φ⟨φ²⟩ inside the non-squares,
of relative size |⟨φ²⟩| / |squares| = 1/i_𝔮. Brute-force (`review_ss_misc.py`): exact for all split 𝔮 with ℓ < 3000.
That a hit is a genuine solved class: n ≡ −4φ^{2k+1} (mod 𝔮) gives 𝔮 | a_k with χ(𝔮) = −1, and O183 Thm 1.3(b)
(R183-reviewed) then gives V_φ(n). SOUND.
*Reading.* "i_𝔮 = 1 for a positive proportion under GRH": this is O183 Thm 3.1's Lenstra input (ℓ ≡ 1 (4), φ a
primitive root ⇒ χ(𝔮) = −1 and ⟨φ²⟩ = squares); numerically 6 461 of the 9 015 split 𝔮 (ℓ < 2·10⁵) with
χ_{−φ}(𝔮) = −1 have i_𝔮 = 1. "Σ 1/i_𝔮 = ∞ unconditionally": correct by the elementary argument
#{𝔮 : ord_𝔮 φ ≤ y} ≤ #{prime ideals dividing ∏_{m≤y}(φ^m − 1)} ≪ y², so ord_𝔮 φ ≥ N𝔮^{1/2}/log N𝔮 for almost all
𝔮 and 1/i_𝔮 ≫ N𝔮^{−1/2}/log N𝔮 ("Erdős–Murty type" is the right attribution, but the weak elementary bound
suffices; only 72 of 17 924 split 𝔮 below 2·10⁵ have ord φ < √ℓ). The overreach is in the conclusions drawn (D9, D10).

### §6 (Assessment)

Recomputed C_adm(r, K₁) = 0.45 / Σ_{K ≥ K₁ odd} 2r^{2K/5 − (K+1)/2}: all twelve table entries reproduced to the
printed precision (`review_ss_misc.py`). The closed form is C_adm = 0.225·(1 − r^{−1/5})·r^{0.1K₁ + 0.5}, not
"≈ r^{0.1K₁+0.1}" (D12). Nicolas–Robin: log τ(n) ≤ 1.5379·log 2·log n/log log n, i.e. τ(n) ≤ n^{1.0660/log log n}
(n ≥ 3): the constant is right. The double-exponential r₀: the loss exponent K·1.07m/log(K log r) beats the margin
K/10 + 1/2 for all K ≥ 1 only if log log r ≳ 10.7m (m = number of τ-factors), since the terms with
K log r < e^{10.7m} grow; so r₀ ≈ exp(exp(10.7m)) — the author's reasoning is right in shape, and m is unverified
("number of τ factors in ET's casework" was not counted), which is fine for an Assessment. D13, D14.

### Numerical cross-checks (from scratch)

`scripts/review_ss_lib.py`: the seven families and the ET §10 sextuples typed in from ET pp. 8, 37–38; ES solution
checked with exact fractions; V_I/V_II membership checked. `scripts/review_ss_classes.py 600 2000`:
* my residue sets equal `mordell_lib.residue_set(M)` for every M ≤ 600 (13 903 classes);
* all 138 967 pairs (class of modulus ≤ 600, 1 ≤ n ≤ 2000 in it) give a V_I/V_II point and an exact ES solution:
  0 failures (Prop 3.1(i) **at every n ≥ 1**, including composite and small n);
* all 5 686 V-points with a, b, d < 60 of all n ≤ 300 lie in the I1 resp. II2 class named in the proof: 0 failures;
* no integer square ≤ 10⁴ lies in a class of modulus ≤ 600;
* 13-line, level 1: non-residues 5, 6, 8, 11 are covered by modulus 39 and 2, 7 by modulus 143 (plus 52, 104, 312, 364),
  confirming the parenthetical remark of §3.

### §2 EVIDENCE (independent recomputation)

`scripts/review_ss_escape.py 100000 30 188 23 47 97` (log `logs/review_ss_escape_1e5.txt`). Different method from
the author: no residue table; for each prime p the ET *class conditions* are tested directly against p mod m for
all 5.1·10⁶ parameter tuples with modulus ≤ 10⁵; both witnesses (least-h class, least-E class) re-solved at p with my
own ET-tuple solver (exact fractions). Own random primes (seed 188), same four population definitions.

| B | A (near x(5)): h, E | B (near 1): h, E | C: h, E; E = 17 | D: h, E |
|---|---|---|---|---|
| 23 | 71, 31 | 71, 37 | 68, 17; 21/30 | 11, 7 |
| 47 | 131, 59 | 79, 59 | 68, 17; 23/30 | 7, 5 |
| 97 | 167, 107 | 223, 107 | 119, 17; 19/30 | 15, 5 |

Author: A (47,37), (151,67), (239,127); B (79,37), (159,61), (239,107); C E = 17 in 70–80 %; D (7–11, 5).
Qualitative claims **reproduced**: every prime has a class of modulus ≤ 10⁵; in A and B the least escape modulus is
a single prime q > B in 180/180 of my cases (q ∈ {101, …, 239} at B = 97), never a 17-power; in C 63–77 % escape at
17; D is easy. The medians fluctuate by up to a factor 2 between runs (h ∈ [1.7B, 3.1B]), which is expected with
few distinct primes (D7). Consistent with Lemma 1.1: no A-prime's least-E witness is a 17-power (I did not test
all classes of each prime for this). Scope remark (not a defect): the populations are "near x(5)" only to depth L = 4 (p ≡ 5 mod 17⁴), although x(5)
is certified to level 10, and with M ≤ 10⁵ no class of 17-level ≥ 4 is visible at all (4·17⁴ > 10⁵). So §2 shows
that at agreement depth 4 and B ≤ 97 the sterile point is invisible; "the r-adic part of Thm 3.1 is not where the
difficulty sits" is an extrapolation and is correctly labelled Assessment.

## Defects

**D1 (MINOR; Prop 3.1 header and proof, "relative to ET Props 1.3/1.4 and §10").** ET has no Prop 1.3, and Prop 1.4
is the average of τ(kab²+1). The parametrisation results are ET **Props 2.2 and 2.6** (with the equivalent
characterisations Props 2.3, 2.7). *Repair:* cite ET Props 2.2/2.6 (for (a)) and §10 (for (i)); state that (b)
uses only the bare identities above, no ET proposition.

**D2 (MINOR; Prop 3.1(b) "an ET N-point (a Type I or Type II parametrised solution)").** In ET, "Type I/II
solution" carries coprimality conditions (abcd or abd prime to n), and for composite n an N-point of Σ_n need not
give a Type I/II solution. The statement is true for V_I(n) ∪ V_II(n) (N-points, no coprimality), which is also how
SQ is defined. *Repair:* replace the parenthesis by "(an element of V_I(n) ∪ V_II(n), no coprimality conditions;
for composite n this is weaker than an ET Type I/II solution)". Also add the missing case "p divides no
denominator" to the proof of (a) and treat p = 2.

**D3 (MAJOR as framing; §3 "Reading (Assessment)" and AGENT_REPORT SHARP 1, "Every non-square integer sits in the
divergent regime … ES lives exactly on the divergent side … at a ν-null point").** An integer n is not merely
ν-null in G_{T(n)}: it is **not in G_T for any T** (its components off T(n) are n_q ≠ 1, or non-units). The
dichotomy is a statement about the slices G_T ("1 off T"); n lives on a different slice (n_q a non-trivial square
off T). Prop 3.2 does extend to the slice "x_q prescribed squares off T" (its proof only uses coordinates in T), but
the convergent side (O178) does **not**: O178 is specific to x_q = 1 off r, and on a slice with other square
coordinates the box dictionary changes (a class meets the slice iff ρ ≡ x_q at the other primes, not ρ ≡ 1).
So "ES lives on the divergent side of a Borel–Cantelli dichotomy" compares objects on different slices.
*Repair:* say "the non-square pattern of an integer is divergent; the dichotomy itself is proved only on the
slices G_T, which contain no integer", and drop "exactly".

**D4 (MINOR; Prop 3.2 proof).** "Second Borel–Cantelli: a.s. infinitely many occur" is true but more than needed;
one occurrence suffices, and P(none) = ∏(1 − 2/(q−1)) = 0 is the whole proof. *Repair:* optional.

**D5 (MINOR; §4 Lemma 4.1 "for any r").** False for r = 2 (counterexample above). *Repair:* "for every odd prime r".

**D7 (MINOR; §2 "30 random primes", "in all 180 cases").** For A and B the primes are drawn as k·Q_B·17⁴ + res
with k ∈ [lo/mod, 2lo/mod); at B = 97 this is k ∈ [1000, 2000), which contains only ≈ 75 primes of the progression,
and at B = 23 only ≈ 380 values of k. Sampling is with replacement: in my run with the same scheme only 24–26 of
each 30 A/B primes are distinct. The author's "180 cases" are therefore ≈ 150 distinct primes. The conclusion is
unaffected (my independent set agrees). *Repair:* sample without replacement, report distinct counts.

**D8 (MINOR; §2 Reading (i) "h ≈ 2.5B ≈ 2.5·log Q_B").** Reproduced medians range over 1.7B–3.1B and the A/B
medians differ by ×1.6 at B = 47 in my run (131 vs 79) while the author had 151 vs 159. "≈ 2.5B" is a single-run
figure. *Repair:* "h of order B (1.5B–3B in two independent runs)".

**D9 (MAJOR as framing; §5 Reading "So in V_φ every infinite non-square pattern is in the divergent regime of §3",
and "The O178 sterile points are exactly the profinite signature of 'finitely many shots'"; same in AGENT_REPORT
SHARP 2 and bsM_shot_coverage).** (i) False as stated: any infinite T can be thinned to T' ⊂ T with
Σ_{𝔮∈T'} 1/i_𝔮 < ∞ (take one 𝔮 per dyadic block of a sparse sequence). What is true: Σ 1/i_𝔮 = ∞ over any set of
𝔮 of positive (upper) density, in particular over the pattern of every non-square integer n (the 𝔮 with
(n/𝔮) = −1 and i_𝔮 = 1 have positive density under GRH; unconditionally Σ 1/i_𝔮 = ∞ over that set by the elementary
bound above together with Chebotarev in K(√n, √−φ)). (ii) "Exactly" asserts an equivalence; what is shown is one
direction on |T| = 1 lines (summable per-prime coverage ⇒ sterile points, O178) plus the observation that V_φ's
per-prime coverage is not summable. *Repair:* replace (i) by "every pattern of positive density, in particular that
of every non-square integer", and (ii) by "O178 sterile points are a profinite symptom of finitely many shots per
prime"; keep the Assessment label.

**D10 (MINOR; §5 Reading and AGENT_REPORT: "the unique ℤ-shot with bounded modulus 4 is Mordell's p + 4" /
"Mordell's p + 4 is the unique bounded-modulus shot").** Every fixed II2 shot (a, d) ("p + 4a²d has a prime factor
f ≡ −1 (mod 4ad)") has the bounded modulus 4ad; e.g. p + 8, p + 16 (modulus 8). The precise contrast is per prime:
at a given q only the shots with 4ad | q + 1 are usable (at most f_II(q) ≤ τ((q+1)/4)²-many, each one residue mod q),
whereas in V_φ all shots k ∈ ℤ are usable at every 𝔮 with χ(𝔮) = −1. Mordell's (a, d) = (1, 1) is the unique II2 shot
usable at **every** q ≡ 3 (mod 4) (the only one with 4ad = 4). *Repair:* state it this way.

**D11 (MINOR; Prop 5.1(a) "cover a fraction ≤ (6f(q) + 2f_II(q))/q of ℤ_q^×").** (6f + 2f_II)/q is the Haar
measure in ℤ_q; as a fraction of ℤ_q^× (measure (q−1)/q) it is (6f + 2f_II)/(q − 1). Also the P-box count is per
N-point of Σ^II_q modulo dilation (f_II^N), which equals f_II(q) for prime q (coprimality automatic) — worth saying.

**D12 (MINOR; §6 "(C_adm ≈ r^{0.1K₁+0.1})").** Wrong exponent: the table itself follows
C_adm = 0.225(1 − r^{−1/5})·r^{0.1K₁+0.5} (e.g. r = 10⁹+7, K₁ = 1: 5.6·10⁴ vs r^{0.2} = 63). *Repair:* replace.

**D13 (MINOR; §6 "≈ 0.45 of the non-residue mass is left for it").** (a) As used in the formula, 0.45 is an
*absolute* Haar mass, i.e. ≈ 96 % of the non-residue mass (r−1)/(2r) ≈ 0.47 at r = 17, not "0.45 of" it. (b) At r = 17
the certified census (MORDELL17B: ρ₁ ≈ 0.677 of each cell uncovered through P-level 6) leaves only
≈ 0.677·8/17 ≈ 0.32 of ℤ_17, so the r = 17 entries are ≈ 1.4× too generous; the per-cell target of MORDELL17B
(C ≤ 1.40 at θ = 2/5, K ≥ 13) is a different, stronger statement (a sterile point in a prescribed cell) and should
not be compared with the table without saying so. *Repair:* say "absolute mass 0.45" and footnote r = 17.

**D14 (MINOR; §6 "So **no computer-assisted proof at r = 101 or 10⁹ is possible without a new explicit count of
Type II solutions of 4/r^K with no divisor-function loss**").** This is an impossibility claim about all proofs;
what is shown is that *this union-bound route with τ-lossy explicit counts* fails at these r. *Repair:* "no
computer-assisted proof along the O178 union-bound route …" (Assessment).

**D15 (MINOR; Lemma 4.2 "s ≤ the 2-adic compatibility").** Undefined phrase. *Repair:* "(the 2-adic condition
c ≡ ρ (mod 2^s) either holds, and then the class has the stated measure, or fails, and the measure is 0)".

**D6 (MINOR; §1 Lemma 1.1(a)).** "The ET classes of p with M' | p − 1 are exactly the boxes on the r-generic line
containing u = p" is ambiguous: a box containing u = p can come from a class with ρ ≡ 1 (M'), ρ ≡ p (M_r) but
p ≢ 1 (M'), which does not contain p. Correct reading: "C ↦ C ∩ line is a bijection from the classes of p with
M' | p − 1 onto the boxes containing u = p whose class has M' | p − 1". *Repair:* reword as above, or simply
state (a) as "x(p) ∈ C".
