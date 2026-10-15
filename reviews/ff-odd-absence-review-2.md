# Hostile review #2 of FF_ODD_ABSENCE.md (O226) — R241, round 1

Reviewer: R241 (independent; no edits to the author's files in round 1). Scope: Lemma 1.1, Thm 1.2, Cor 1.3, Thm 1.4,
Cor 1.5, Prop 1.6, Cor 1.7, Lemma 2.1, Thm 2.2 (certificate), consistency with (J)56 Thm 8.1.
From-scratch scripts: `scripts/review_r241_*.py`.

## Summary verdicts
| Claim | Verdict |
|---|---|
| Lemma 1.1 (root-product identity) | SOUND (re-derived line by line, §1) |
| Thm 1.2 (Case B law) + Cor 1.3 | SOUND (§1; brute-force EVIDENCE reproduced from scratch) |
| Thm 1.4 (Case A law) | SOUND, modulo the inherited input lc K = lc E ∈ F₃^* ((J)56 Lemma 7.2) (§2) |
| Cor 1.5 (vanishing law) | SOUND (§2) |
| Prop 1.6 (sharpness) | SOUND (§3); its 'Exact scope' paragraph partially reproduced (q = 9, s ≤ 12) |
| Cor 1.7 (k ≥ 2 parity law) | SOUND (§3); the bound-sum reductions 41.87 → 11.24, 1466.7 → 389.2 not re-run (not load-bearing) |
| (further claims) | (in progress) |

## §1. Lemma 1.1, Theorem 1.2, Corollary 1.3

**Re-derivation of Lemma 1.1 (independent).** Over an algebraic closure write V = λ∏(T − β_i), W = μ_W∏(T − γ_j). At a root β of V:
C(β) = −W(β) (from W + C = GV; G is never used otherwise, so G = 0 is harmless) and M(β)W(β)C(β) = β^s, so
−M(β)W(β)² = β^s; multiplying, (−1)^t P_M P_W² = (∏β_i)^s = (−1)^{ts}V(0)^s λ^{−s}, with P_X := ∏_i X(β_i). At a root γ of W,
V(γ) = −γ^s, so ∏_{i}(γ_j − β_i) = V(γ_j)/λ gives P_W = μ_W^t(−1)^{ta}λ^{−a}∏_j V(γ_j) = μ_W^{t−s}(−1)^{ta+a+as}λ^{−a}W(0)^s,
and likewise P_M = μ_M^{t−s}(−1)^{tz+z+zs}λ^{−z}M(0)^s (the identity at roots of M is the same, MWC = 0 there). Substituting,
using V(0) = M(0)W(0)C(0) and M(0) ≠ 0:
  (W(0)/C(0))^s = (−1)^{t+tz+z+zs+ts} λ^{z+2a−s} μ_M^{s−t} μ_W^{2(s−t)}  —  exactly the stated formula.
No hypothesis on lc C, on deg(MWC) or on G is used; repeated roots are fine (products with multiplicity); t = 0 / z = 0 / a = 0
give empty products and the formula still holds. **SOUND.**

**Theorem 1.2.** Lemma 1.1 with M = m', W = w, V = v, μ = 1; λ = lc v = lc(w + C)/lc g' = lc(w + C) ∈ {1 (a ≠ b), 2 (a = b)}
(q odd, no cancellation). The λ-exponent z + 2a − s equals a − b because z + a + b = s ((J)56 Lemma 7.1(i); re-checked by
brute force below: no tuple with deg(m'wC) ∈ {s + 1} at the tested sizes, and the enumerator below never finds a tuple outside
z + a + b = s). Hence ε = (−1)^{t+tz+z(1+s)+ts} for every odd q (the R-O226 repair is correct). E(0) = w(0)/C(0) follows from
Ev = T^s + m'w² at 0 (v(0) = m'(0)w(0)C(0)); E(0) ≠ −1 because w(0) + C(0) = g'(0)v(0) ≠ 0. **SOUND.**

**Cor 1.3.** gcd(2s, q − 1) = 2 ⟺ gcd(s, (q−1)/2) = 1; instances q = 9, 27, 81, 243 re-checked arithmetically. For q = 9:
odd s: E(0)^s = ±1 with E(0) ∈ μ_8 forces E(0) = ±1; s ≡ 2 (4): E(0)² ∈ μ_4 to an odd power, so E(0) = ±i (and E(0) = 1 is
on u₀ = −1 ∈ F₃^*), sign (±i)^s = −1 = ε; s ≡ 0 (8): E(0)^s = 1 = ε. **SOUND.**

**From-scratch verification (EVIDENCE; R241 code, no author code).**
* `scripts/review_r241_enum.py` (python-flint factorisation over F_q; five complete routes V[t], (m',w), (m',C), (w,g'), (C,g'),
  each candidate re-verified against the full definition (B^{k=1}); ORDERED tuples, both orientations).
* `scripts/review_r241_brute.py` (naive: all monic T-free (m', w, C) with deg sum ≤ s + 1, v := m'wC − T^s). Agreement of the full
  (pattern, E(0)) histograms: q = 9 (s ≤ 4), 5 (s ≤ 6), 7 (s ≤ 5), 27 (s ≤ 3): **exact match**, and 0 tuples with deg(m'wC) = s + 1.
  (A first version of my brute force forgot T ∤ g' and found E(0) = −1 tuples — confirming that the T ∤ g' condition is what
  excludes E(0) = −1.)
* Law check (both the unsimplified Lemma 1.1 form and the simplified ε form) on every tuple: q = 9, s ≤ 12 (15 701 ordered
  tuples), q = 5, s ≤ 14 (4 224), q = 7, s ≤ 12 (2 835), q = 25, s ≤ 6 (1 644), q = 27, s ≤ 9 (625): **0 failures**.
* The author's counts are reproduced exactly: oriented (a ≤ b), 2 ≤ s: q = 9, s ≤ 12: 8 915; q = 27, s ≤ 9: 340
  (the author's 305/645 for q = 5/7 also match my 307/647 minus the two s = 1 tuples with a ≤ b).
* q = 9 E(0)-distribution (my run): odd s only E(0) = 1; s ≡ 2 (4) only {1, ±i}; s ≡ 0 (4) all classes except −1;
  q = 27, s ≤ 9: only E(0) = 1. As claimed.

## §2. Theorem 1.4 and Corollary 1.5

**Re-derivation.** From E + 1 = a1'b1K and EF = T^αa1' + b1: mod a1', E ≡ −1 so −F ≡ b1, i.e. a1' ∣ F + b1 (z polynomial);
b1KF = (E+1)F/a1' = (T^αa1' + b1 + F)/a1' = T^α + z (A3, checked symbolically and on every enumerated datum by assertion). So
(M, W, C, G, V, s) = (K, b1, F, a1', z, α) satisfies (R), V(0) = z(0) = b1(0)K(0)F(0) ≠ 0 since E(0)F(0) = b1(0) ≠ 0. Lemma 1.1
gives the stated formula with μ_M = lc K, μ_W = 1. lc F = lc(T^αa1' + b1)/lc E ∈ F₃^* when lc E ∈ F₃^*; λ = lc(F + b1) is in
F₃^* unless deg F = β and lc F = −1, in which case κ + 2β − α = β − f = 0. Correct. **Dependency:** lc K = lc E ∈ {1, 2} is an input
from (J)56 Lemma 7.2 / DEPTH_ASPECT Lemma 2.4 (not re-proved here; for general q the right side need not be in F₃^*). In addition
β + κ ≤ α always (deg E ≤ deg(T^αa1' + b1), and β > α + deg a1' forces a1' = 1, K const and −1/c = T^α: impossible) — this
justifies my enumeration route below. **SOUND.**

**From-scratch check** (`scripts/review_r241_caseA.py`: all (b1, K), β + κ ≤ α, lc K ∈ {1, 2}; E | T^α + b1²K, which I derived:
E(Fb1K − T^α) = T^α + b1²K; a1' = (E+1)/(b1K)): q = 9, α ≤ 5 (505 data): unsimplified formula and E(0)^{2α} = 1 hold for every
datum, 0 failures. The off-F₃ counts per pattern at α ≤ 4 equal `data/zc/caseA9_4.txt` exactly (α = 2: 18, α = 4: 268); the
P₈ part at α = 4 is only 174 (the author's use of 268 is a valid over-count).

**Cor 1.5.** ord(−u₀) ∣ 2n is a restatement; q = 27: −u₀ ∉ {±1} has order 13 or 26 ⇒ 13 ∣ n; q = 9: ord 4 (±i) ⇒ 2 ∣ n, ord 8
(P₈) ⇒ 4 ∣ n. **SOUND.**

## §3. Proposition 1.6 and Corollary 1.7

**Prop 1.6** re-checked by hand: (D+1)C = T^s + 1 + C = T^s + v, w + C = v = g'v; m'(0) = D(0) + 1 ≠ 0, C(0) = 1/D(0),
v(0) = (D(0)+1)/D(0) ≠ 0, v nonconstant (deg C = s − deg D ≥ 1); E(0) = D(0); for D = T − ρ, ρ^s = −1 gives ρ ≠ 1 (q odd).
Consistency with the law: z = 1, t = s − 1 gives ε = (−1)^{s²+2s−1} = (−1)^{s+1} = (−ρ)^s. **SOUND.** The "Exact scope" EVIDENCE
(all allowed classes populated) is reproduced by my q = 9, s ≤ 12 run (§1) and by q = 7 (s ≤ 12: s ≡ 0 (3) all classes ≠ −1, else
only E(0) = 1); the q = 27, s = 13 statement (118 443 tuples, all 24 classes) was **not** re-run (cost; it is EVIDENCE and not used).

**Cor 1.7** re-derived: with (M, W, C, G, V, s) = (m', w₁, C₁, Tg', v₁, s − 2), W(0)/C(0) = −1 since w₁(0) + C₁(0) = 0. I also checked
that deg(m'w₁C₁) = s − 2 is forced (if larger, deg v₁ = z + a' + b' > max(a', b') ≥ deg(w₁ + C₁) = 1 + y + deg v₁; if smaller,
t' = s − 2 and deg(Tg'v₁) ≥ s − 1 > max(a', b')), so the λ-exponent is a' − b' and λ = 2 only when it is 0. Parity reduction
(z even ⇒ s ≡ t(1+s) ⇒ s, t even; z odd ⇒ ts odd) verified. From-scratch brute force (`scripts/review_r241_k2parity.py`, all monic
T-free (m', w₁, C₁) of total degree ≤ s' + 1, g' any monic — a superset of (B)): q = 3 (s' ≤ 9), 5 (≤ 7), 7 (≤ 6), 9 (≤ 5):
0 parity failures, 0 tuples with deg ≠ s'. (Small samples; the proof is what matters.) **SOUND.**

## §4. Lemma 2.1 and the logic/filters of Theorem 2.2

**Lemma 2.1 (normalisation).** The criterion of (J)56 §7 / (J)51 Lemma 2.1 is stated in *relative* slice units: each slice
u₀ has relative measure 1, a Case B tuple's maximal cylinder u ≡ −E (mod T^{N+1}), N ≥ ⌈(s−1)/2⌉ (s = N + 1 + γ, γ ≤ N), has
relative mass ≤ q^{−⌈(s−1)/2⌉} inside the single slice u₀ = −E(0), and a Case A datum's maximal cylinder (mod T^{1+α}) has
relative mass q^{−α}. Hence Σ_{u₀∈P} covered(u₀) ≤ (left side) < |P| ⇒ min_{u₀∈P} covered(u₀) < 1 (countable subadditivity) ⇒ a
positive-measure set of u in that slice lies in no validity set ⇒ O(9, T) ≠ ∅. The restriction to a subset P is legitimate:
nothing in the argument needs the slices outside P, and the depth-1 families (Prop 6.1: u₀ ∈ F₃^*) never meet P ⊂ F₉^* ∖ F₃^*.
"< |P|" is the right threshold (it is "< q − 3" of (J)56 with P = all off-F₃ slices). **SOUND** (inherits the (J)51/(J)56
framework: every linear family is a Case A datum or a (B^{k=1}) tuple with the stated maximal cylinder).

**Filters.** (a) *Slice filter*: −P₈ = P₈ ((−ζ)⁴ = ζ⁴), so −E(0) ∈ P₈ ⟺ E(0)⁴ = −1 ⟺ (E(0) ∉ F₃ and E(0)⁴ ≠ 1);
zc_enum's SLICEF = 2 test (E(0) ∉ {0, 1, 2}, E(0)⁴ ≠ 1, with E(0) = m'(0)g'(0)w(0) − 1, the T0 form of E) is equivalent. (b) *Level
filter*: E(0) ∈ P₈ has order 8 and E(0)^{2s} = 1 ⇒ 4 ∣ s; Case A: E(0)^{2α} = 1 ⇒ 4 ∣ α. (c) *Pattern filter*: for 4 ∣ s,
E(0)^s = (E(0)⁴)^{s/4} = (−1)^{s/4} must equal ε(s; z, t). The char-3 form used in the C code (extra λ^{z+s} with λ = −1 iff
a = b) is identical because a = b ⇒ z + s = 2(z + a) is even. (d) *Orientation*: the files store a ≤ b with the a = b count
containing both orders; mult 2 for a < b. Under w ↔ C, E(0) ↦ 1/E(0) (P₈ is inversion-closed), the pattern's (s, z, t) and
hence ε are unchanged — so the (b, a) orientation is in P₈ and compatible exactly when (a, b) is. My ordered-tuple enumeration
confirms this directly: per-pattern P₈ counts of (a, b) and (b, a) agree in every pattern (s ≤ 12), and the author's mass
equals my ordered-tuple mass (§5). **All filters SOUND.**

**Frobenius remark** in the statement of Thm 2.2 (covered measure constant on {ζ, ζ³}, {ζ⁵, ζ⁷}): correct (the (B^{k=1}) and Case A
conditions are F₃-rational, σ(E) is the E of the conjugate datum, and coefficientwise Frobenius preserves Haar measure on
F₉[[T]]), but unproved in the text; harmless (m-2).

## Defects

No FATAL, no MAJOR defect found. Minor:

* **m-1 (FF_ODD_ABSENCE §1, Thm 1.2 *Check*, and AGENT_REPORT_O226 Results 1).** "q = 9, s ≤ 12: 8 915 tuples; q = 5, 7, 27, s ≤ 9:
  305, 645, 340" are counts of tuples with a ≤ b (a = b both orders) and 2 ≤ s; the number of ordered tuples is 15 701 (q = 9).
  *Repair:* say "oriented tuples (deg w ≤ deg C), 2 ≤ s ≤ 12".
* **m-2 (Thm 2.2 statement, parenthetical Frobenius sentence).** Correct but unproved inside a PROVED statement. *Repair:* move
  to a Remark with the one-line proof (the data conditions are F₃-rational; σ maps the datum of E to that of σ(E) and the cylinder
  u ≡ −E to u ≡ −σ(E); coefficientwise σ preserves Haar measure), or label it.
* **m-3 (Thm 1.4 statement).** "lc K = lc E ∈ {1, 2}" is an input from (J)56 Lemma 7.2 / DEPTH_ASPECT Lemma 2.4, and the conclusion
  E(0)^α ∈ F₃^* uses it. *Repair:* cite it explicitly as the source of that hypothesis (the proof as written reads as if it were
  part of the definition).
* **m-4 (Thm 2.2 proof, tail bullet).** This is the first use of `fz1_tail` at r = 2, and at q = 9 the tail bound exists only
  because of the linearised Lemma 4.1 (FF_STERILE_SMALL Lemma 5.1, RANK = 1): R226's reviewer tail without Rankin gives
  3.08·10⁶ at r = 2 (my run), with my port of R221's own Lemma 4.1 it gives 0.0228. *Repair:* state that the tail rests on
  Lemma 5.1 (as in Thm 5.2), and cite the independent value.
* **m-5 (Thm 2.2 *Validation*, AGENT_REPORT trust points).** The s = 16 and s = 20 exact counts are load-bearing (route bounds
  there: ≈ 2.1 and 2.4–2.9, either alone would break < 4), and s = 20 was "not cross-checked independently". *Repair:* add
  this review's cross-check (§5: 725 of the 933 exact s = 20 patterns re-enumerated from scratch, 0 mismatches; s = 16 see §5).
* **m-6 (Lemma 2.1 proof).** "the stated relative mass" should be "the relative mass of the tuple's maximal cylinder, which
  contains the validity sets of all families with that datum" ((J)51 Lemma 2.1 wording). Cosmetic.
* **m-7 (cross-file status; for the parent).** FF_STERILE_SMALL §7 (end) and §8 ("Status … Open: … q = 9 with k = 1") still list
  q = 9, k = 1 as open; STATUS/DISCOVERIES need the update "ES_q(T): no finite linear covering for every q = 3^r, r ≥ 2
  ((J)56 Thm 8.1 + O226 Thm 2.2)" when O226 is merged.
