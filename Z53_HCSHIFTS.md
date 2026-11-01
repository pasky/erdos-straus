# Z53_HCSHIFTS: the one-coordinate polylog target HC(p) ≪ (log p)^A, growing-window kills, and the anatomy of shifted families

**ES is open. Nothing here proves or disproves ES, ES₅, (★), or HC(p) ≪ (log p)^A.** Each claim carries one label:
PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Everything is internal and unrefereed.
This is lane z53 HCSHIFTS (FRONTIER §7.2). Scripts are in `scripts/z53_hcshifts_*`; data are in `data/z53/hcshifts/`
(< 1 MB); the commands are in §7.

**Review record.** A hostile internal review (deep mode; `data/z53/hcshifts/REVIEW_internal_deep.md`) returned
UNSOUND-as-written. This version applies all of its repairs (§8):
* Theorem W is scoped to fixed families and their non-least members.
* The model's boundary scale is corrected: A = 2 log 2 is *allowed*.
* Cross-prime independence is made explicit.
* The fire law is restated with its systematic deviations.
* L2 is rerun held-out and with separate endpoint/level events.
* "Private" is split into rough-splitting and shift-private.
* The engine's existential type flags are labelled as such.
* The BH limit is restricted to the displayed family.
* Remark 3.1's universal reading is downgraded to Assessment.

A cross-model review (`data/z53/xreview/REVIEW_HCSHIFTS.md`) returned ACCEPT-WITH-FIXES; its fixes are applied (§8).

## 0. Verdict first: **narrowed**, plus a model-based re-calibration of the target scale

**Target T (FRONTIER §7.2; OPEN).** There is an A such that HC(p) ≤ (log p)^A for all large primes p ≡ 1 (mod 8).

**1. The Dickson/Hypothesis-H kill has a wall at X ≍ log p (Theorem W; PROVED, elementary).**
* *Families covered.* p = P(q) along an admissible set (a Theorem-M formal run, POINTWISE_SIZE). Every window integer
  N_x^∗(P(q)), x ∈ 𝒞 ∩ [4, X], formally factors as a fixed integer times irreducible polynomials whose values are (fixed
  constant)×prime. This is the shape of LOWERTAIL_ROUND2_FABLE Prop 3.3.
* *Statement.* Such a family has p mod ℓ constant for every odd prime ℓ ≤ ⌊X/4⌋ + 1. So **every member except the least
  satisfies log p > (1/4 + o(1))X**.
* *Consequence for kills.* Through its fixed-window factorisation, one such family can *certify* HC(p) > X only for
  X < (4 + o(1)) log p (except possibly at its least member). So no single family of this shape can certify a growing
  threshold HC(p) > (4+ε) log p, or HC(p) > (log p)^A for A > 1, at infinitely many members. W bounds the certified
  window, **not the actual HC** of the members: they may well miss further lines beyond X.
* *What this leaves open.* An infinite sequence of families each contributing only its least member is not excluded;
  that is no longer a Hypothesis-H mechanism. Nor does W exclude a kill of HC ≤ C log p for C < 4.

**2. The kill does extend to growing X, but only to X ≍ log p/log log p.**
* Under a uniform Bateman–Horn lower bound (UBH, non-standard), the Prop 3.3 family gives HC(p) > c·log p/log log p
  infinitely often (Prop W2; CONDITIONAL on UBH).
* For that family the Bateman–Horn first-hit scale is (4/3 + o(1)) log p/log log p (Assessment).
* It needs ≍ X simultaneously prime cofactors, as the kickoff expected.

**3. Smooth-part certificates die at X ≍ log p, unconditionally (Prop W3; PROVED relative to Linnik's theorem).**
* *Statement.* There are infinitely many primes p at which every certificate with a coordinate x ≤ X, where
  X ≥ (1/(2L) − o(1)) log p, **splits the (X+1)-rough part** of its window integer nontrivially. Here L ≤ 5.2 (Xylouris);
  under GRH X ≥ (1/4 − o(1)) log p.
* *Instances (CERTIFIED).* X = 16, 20, 24, 32. **Every instance has HC = 4**, through 14–104 rough-splitting
  certificates.
* *Scope.* Since p ≥ Q_X + 1, these windows satisfy X ≤ (1/2 + o(1)) log p. So W3 constrains only certificates with
  coordinates in a logarithmic window: a proof of T that certifies within that window must split rough parts at
  infinitely many primes. Certificates at larger coordinates x ≤ (log p)^A (A > 1) are not excluded by W3.
* *Together with H4_NOT_POLYLOG.* Every coordinate x ≤ (log p)^A lies below H = exp((log p)^κ) (κ < 1/12; < 1/6 relative
  to Gallagher). So at infinitely many primes (H4's), any certificate for T has both divisor and cofactor above H.

**4. Anatomy at one p (§3).**
* *Small divisors (PROVED).* The deterministic small-divisor structure of the window is congruence data (Remark 3.1). That
  *all* forced structure is congruence data is Assessment.
* *Confinement (PROVED, Lemma C).* T1's confinement mechanism needs −1 ∉ ⟨N mod x⟩. At a prime p this fails exactly on
  endpoint lines with −1 ∈ ⟨p mod x⟩, for example x = q ≡ 7 (8) prime with (p/q) = −1. Blocked confinement forces firing
  at q = 7 (the Mordell class), but for q = 23…127 such lines still miss 13–70 % of the time (EVIDENCE).
* *EVIDENCE, 10⁹–10¹³.*
  * (L1) Line x fires with probability close to 1 − exp(−c·τ(N)/φ(x)) (c = 1 endpoint, 1/2 level). The model
    over-predicts by 3–24 % pooled, more at small τ, and the law is stable across scales.
  * (L2) After fixing p mod 15015, the held-out all-miss frequency (per coordinate) is 0.97–1.17 × the product of
    per-line rates for X ≤ 12, and 0.82–1.53 × at X = 15–16; the 1.53 rests on 16 events. In a separate, in-sample run
    with endpoint and level as separate events, the ratio is 0.95–1.12 for X ≤ 16. The unconditioned excess is up to ×624.

**5. Model consequence (Assessment): the extremal scale of HC is (log p)^{2 log 2 − o(1)} ≈ (log p)^{1.386}, not O(log p).**
* *The model 𝔐.* Lines are independent given p, with ω of window integers Poisson(log log p) and the fire law (L1); for
  item (b) below, the primes are also independent draws.
* *Tail.* P(HC(p) > (log p)^{κ log 2}) = exp(−(log p)^{g(κ)+o(1)}) for 1 < κ < 2, with g(κ) = κ(1 + log 2 − log κ) − 1 < 1.
* *(a) Upper scale.* P(HC(p) > M(log p)^{2 log 2}) ≤ exp(−c log p·√(log log p)). This is summable, so in 𝔐,
  HC(p) ≤ (log p)^{2 log 2} eventually. This needs no cross-prime independence.
* *(b) Lower scale.* With independent draws across primes, HC(p) > (log p)^{2 log 2 − ε} on a set of counting function
  P^{1−o(1)}. In particular HC(p) > C log p for every C (g = 0.914 at X = log p), so **LOWERTAIL_ROUND2_FABLE
  Conjecture 3.4 (HC ≤ C log p) is false in 𝔐**.
* *(c) T.* T is consistent with 𝔐 + 𝔐× exactly for A ≥ 2 log 2.
* *(d) Dark range.* For (4+ε) log p ≤ X ≤ (log p)^{2 log 2 − ε}, 𝔐 + 𝔐× predicts infinitely many exceedances. No single
  Theorem-W family can *certify* such a growing threshold at infinitely many members (PROVED part; W bounds the certified
  window, not actual HC). The BH heuristic extends this down to ≍ log p/log log p for the Prop 3.3 family.

**6. Numerics (CERTIFIED/EVIDENCE).**
* *Samples.* HC was computed for 3·10⁶ primes p ≡ 1 (8): 600 000 consecutive from each of 10⁹, …, 10¹³ (HC exact; lines
  scanned to ≥ 128 and further only when needed).
* *Special sets.* 166 hard primes, 12 000 near-squares and 5 000 odd squares. No line fires at the odd squares (T1).
* *Certificate types.* The fraction of primes with HC ∈ [12,16] for which *every* HC-certificate is rough-splitting
  w.r.t. 64² rises from 5.5 % to 16.7 % over 10⁹ → 10¹³.
* *Hard primes* (HC ≥ 20) show both a congruence signature (square-mimicking; p ≡ 1 modulo small primes) and an anatomy
  deficit: 0.7–0.9 fewer bits of τ per window integer, half the expected hits.

**What the lane buys.**
* Q1 is answered by two scoped kill-limit theorems (W for fixed families, W3).
* A model computation, backed by scale-stable empirical regularities, moves the target scale from log p to
  (log p)^{2 log 2}.
* A structural lemma (C) locates T1 in the coordinate lines.
* **No positive step toward T** (Assessment). Every forced structure found is congruence data, and the open step is a
  single-p anatomy statement about large primes, i.e. B2.

## 1. Objects and precise statements

For a prime p ≡ 1 (mod 8) let 𝒞 = 𝒞_p = {x ≥ 4 : 4 | x or x ≡ 7 (mod 8)}. Throughout, 4 ≤ x ≤ X < p, so gcd(x, p) = 1. For
x ∈ 𝒞 the two **lines** are the integers
  N_x^e := p + x (endpoint line),  N_x^l := xp + 1 (level line).
Both are prime to x: N_x^e ≡ p and N_x^l ≡ 1 (mod x). Line x **fires** if N_x^e or N_x^l has a divisor d ≡ −1 (mod x):
* a divisor d ≡ −1 of N_x^e is the numerator A = tx − 1 of the word (t, x, N/d);
* a divisor d ≡ −1 of N_x^l is the numerator A = xu − 1 of the word (x, u, ·).

By LOWERTAIL_ROUND2_FABLE Thm 1 / Cor 1.1 (PROVED there), firing lines are exactly the five-slice certificate words with a
𝒞-coordinate equal to x, and
  **HC(p) = min{x ∈ 𝒞 : line x fires}**, with ES₅(p) ⟺ HC(p) < ∞.
For p ≡ 5 (8), HC = 3. The engine `z53_hcshifts_hc.c` reproduces z49's values at every listed hard prime. The internal
reviewer re-checked it independently by PARI divisor enumeration on all 166 hard primes and 500 sample primes, with zero
discrepancies.

**Certificate types.** Take a firing line with integer N, divisor d ≡ −1 (mod x) and threshold y ≥ every prime factor of
x. Write N = s·r, where s is the y-smooth part and r the y-rough part.
* **Congruence-type (w.r.t. y):** gcd(d, r) ∈ {1, r}. Then d mod x is determined by p modulo a y-smooth modulus, through
  s and r ≡ N/s (mod x).
* **Rough-splitting (w.r.t. y):** otherwise. Then r has ≥ 2 prime factors > y, spread over d and N/d.

**Shift-privacy.** By SYNTHESIS_SPARKS8 Lemma 2.3 and its mixed form:
* gcd(p+x, p+x′) | x − x′;
* gcd(xp+1, x′p+1) | x − x′;
* gcd(p+x, x′p+1) | xx′ − 1.

So a prime ℓ > X² divides at most one window integer. Rough-splitting w.r.t. y ≥ X² is therefore *shift-private*. For
y = X + 1 it need not be: the reviewer's example is X = 8, p = 2 646 001 ≡ 1 (mod Q_8), where 31 divides both p + 4 and
8p + 1.

**Questions attacked.**
* (Q1) How far does the Dickson/H kill of Prop 3.3 extend in X = X(p)?
* (Q2) What is forced or provable about the joint factorisation of the window, and can it force a firing line?
* (Q3) At hard primes, do the HC-certificates come from smooth parts or from large primes?

**Why not already closed.** The closed items are fixed X (Prop 3.3, Dickson) and two-endpoint polylog windows
(H4_NOT_POLYLOG). T is one-coordinate, so the divisor side is free. Neither result addresses growing X with a free
divisor side.

## 2. Q1: growing-window kills

### 2.1 Theorem W (fixed-family wall; PROVED)

**Theorem W.** Let X ≥ 8 and let 𝒜 = {P(q) : q ∈ 𝒬} be an infinite set of primes p ≡ 1 (8) with p > X, where P ∈ ℤ[q] is
non-constant and 𝒬 ⊆ ℕ is infinite. Assume that for every x ∈ 𝒞 ∩ [4, X] and ∗ ∈ {e, l}:
* there is a polynomial identity N_x^∗(P(q)) = c_{x,∗}·∏_i f_{x,∗,i}(q)^{e_i}, with c_{x,∗} ∈ ℤ∖{0} and f_{x,∗,i} ∈ ℤ[q]
  non-constant;
* for every q ∈ 𝒬, f_{x,∗,i}(q) = C_{x,∗,i}·(a prime), with fixed nonzero integers C_{x,∗,i}.

This is the shape of a Theorem-M certified family (POINTWISE_SIZE Thm M) for the window-X procedure; the linear case is
LOWERTAIL_ROUND2_FABLE Prop 3.3. Then for every odd prime ℓ ≤ ⌊X/4⌋ + 1, P(q) mod ℓ is the same for **all** q ∈ 𝒬. Hence
𝒜 lies in one residue class modulo Π_X := ∏_{3≤ℓ≤⌊X/4⌋+1} ℓ, and every member of 𝒜 except the least satisfies
  log p > log Π_X = θ(⌊X/4⌋ + 1) − log 2 = (1/4 + o(1)) X.

*Proof.*
1. Fix an odd ℓ ≤ ⌊X/4⌋ + 1. Choose q ∈ 𝒬 so large that p = P(q) > ℓ and |f_{x,∗,i}(q)| > ℓ·|C_{x,∗,i}| for all
   x, ∗, i. Each non-constant polynomial takes each value at most deg times, so such q exist.
2. Let a = p mod ℓ ∈ {1, …, ℓ−1}. The multiples 4k, 1 ≤ k ≤ ℓ − 1 ≤ ⌊X/4⌋, lie in 𝒞 ∩ [4, X], and since 4 is invertible
   mod ℓ they cover all nonzero classes. Take x = 4k with 4k ≡ −a (mod ℓ).
3. Then ℓ | N_x^e(P(q)) = c·∏ f_i(q)^{e_i}. Either ℓ | c, or ℓ | f_i(q) = C_i·(prime) for some i. In the latter case
   ℓ | C_i, since otherwise ℓ would be that prime and |f_i(q)| = ℓ|C_i| ≤ ℓ|C_i|, contrary to the choice of q.
4. In both cases ℓ divides N_x^e(P(q′)) for **every** q′ ∈ 𝒬, because c divides it identically and C_i | f_i(q′) for
   q′ ∈ 𝒬. Hence P(q′) ≡ −x ≡ a (mod ℓ) for all q′ ∈ 𝒬.
5. Members of one class modulo Π_X differ by multiples of Π_X, so all but the least exceed Π_X. Finally
   θ(y) = (1 + o(1))y. ∎

*Remarks.*
* Only endpoint lines with 4 | x were used. With all of 𝒞 and the level classes −x⁻¹ (`scripts/z53_hcshifts_wall.py`),
  log(∏ forced ℓ)/X lies in [0.238, 0.285] for X = 64…4096, and the forced primes are contiguous up to ≈ X/4 (1033 at
  X = 4096).
* The proof does not use that the family is a *kill*. Requiring ≍ X window integers to be "constant × primes" already
  fixes p modulo every ℓ ≤ X/4. This is the precise form of the kickoff observation that ∏_{ℓ≤X} ℓ = e^X ≫ p.
* *Scope.* W concerns one family at a time, of the stated factorisation shape. It does not exclude:
  * a sequence of families, one per X, each of whose least member is an exceedance;
  * mechanisms that certify "no divisor ≡ −1 (mod x)" without factoring the window integers into prime-valued
    factors (for instance subgroup confinement of all prime factors, Lemma C(a)). Such mechanisms would need a
    joint-Landau hypothesis, not H.

### 2.2 Prop W2: how far the displayed kill reaches (CONDITIONAL on UBH)

**Hypothesis UBH** (uniform Bateman–Horn lower bound, linear case). This is *not* a standard conjecture: the standard
statements fix k. There are constants c₁ ∈ (0,1] and C₁ ≥ 1 with the following property.
* For every k ≥ 1 and every admissible family of k distinct, pairwise non-proportional, primitive linear forms a_i s + b_i
  with 1 ≤ a_i, b_i ≤ A;
* and for every S with log S ≥ C₁ k log log(AS);
* #{s ∈ [1, S] : all forms prime} ≥ c₁^k 𝔖·S/(log(AS))^k, where 𝔖 = ∏_ℓ (1 − ν(ℓ)/ℓ)(1 − 1/ℓ)^{−k}.

**Prop W2.** Under UBH there are infinitely many primes p ≡ 1 (mod 24) with HC(p) > c·log p/log log p, with c > 0 depending
only on c₁ and C₁.

*Proof.* Use LOWERTAIL_ROUND2_FABLE Prop 3.3(a) (PROVED there): the forms p = 1 + Qs, F_x = 1 + Qs/(x+1) and
G_x = 1 + xQs/(x+1) for x ∈ 𝒞_X, with Q = lcm(24, x(x+1)); at every s with all forms prime, HC(p) > X.
1. *Forms.* They have distinct slopes, so they are pairwise non-proportional, and they are primitive (constant term 1).
   k = 1 + 2|𝒞_X| ≤ (3/4)X + 3.
2. *Size of Q.* x and x + 1 are coprime and both divide lcm(1…X+1), so Q | 24·lcm(1…X+1) and log Q ≤ (1+o(1))X. The
   coefficients are ≤ A := XQ.
3. *Singular series.* All forms equal 1 at s = 0, so ν(ℓ) ≤ min(k, ℓ−1).
   * For ℓ ≤ 2k the factor is ≥ 1/ℓ.
   * For ℓ > 2k it is ≥ (1 − k/ℓ)(1 + k/ℓ) = 1 − k²/ℓ² ≥ 3/4, and Σ_{ℓ>2k} k²/ℓ² ≤ k/2.
   * Hence 𝔖 ≥ e^{−C₃X}.
4. *Choice of S.* Take log S = C₂X log X with C₂ ≥ 2C₁ large. UBH applies, and
   #{s ≤ S} ≥ exp(C₂X log X − (3/4 + o(1))X log X − O(X)) ≥ 1.
5. *Conclusion.* log p ≤ log Q + log S ≤ (C₂ + o(1))X log X, so X ≥ (1/C₂ − o(1)) log p/log log p. Members are > Q → ∞. ∎

*Assessment (BH first-hit scale for this family).* For the Prop 3.3(a) family, k ≈ (3/4)X, 𝔖 ≤ (C log X)^k and
log Q = (5/6 + o(1))X (cross-review: primes ≡ 3 (8) divide Q only up to (X+1)/3; direct lcm computation gives
log Q/X = 0.829, 0.836, 0.834 at X = 10³, 10⁴, 10⁵; only the lower-order O(X) term is affected). The BH expected number of members ≤ P is ≈ 𝔖P/(Q(log P)^k), which reaches 1 at
X ≈ (4/3 + o(1)) log P/log log P. This is a typical first-hit threshold for this family, not an exclusion. Other Dickson
families, for example with refined moduli, may have larger singular series. Theorem W's (1/4 + o(1))X is the only
family-independent bound proved here.

### 2.3 Prop W3: congruence-type certificates die at X ≍ log p (PROVED rel. Linnik; GRH variant)

Let Q_X := ∏_{ℓ ≤ X+1} ℓ^{a_ℓ} with a_ℓ = ⌊log_ℓ(X+1)⌋ + 1. Then ℓ^{a_ℓ} > X + 1 and
log Q_X = θ(X+1) + ψ(X+1) = (2 + o(1))X; the values for X = 16…32 are 1.77X–1.84X.

**Prop W3.** Let X ≥ 7 and let p > X be a prime with p ≡ 1 (mod Q_X); then 16 | Q_X, so p ≡ 1 (8).
* (i) For every 1 ≤ x ≤ X and both lines, the (X+1)-smooth part of N_x^∗ equals x + 1.
* (ii) Every certificate d ≡ −1 (mod x) of a line x ∈ 𝒞 ∩ [4, X] is rough-splitting w.r.t. y = X + 1. Writing
  N = (x+1)r, we have d = d₁d₂ with d₁ | x + 1 and 1 < d₂ < r, d₂ ≡ −d₁⁻¹ (mod x). In particular a line whose rough part is
  prime does not fire.

By Linnik's theorem such p exist with log p ≤ (L + o(1)) log Q_X = (2L + o(1))X. Letting X → ∞ gives infinitely many p
with **X ≥ (1/(2L) − o(1)) log p**.
* L = 5.2 is admissible (Xylouris, as cited in Lamzouri–Li–Soundararajan, arXiv:1309.3595, §1.2); L = 5 per Xylouris's
  thesis (Tao's constants page).
* Under GRH, LLS Corollary 1.2 (verified in the arXiv PDF: "Assume GRH. Let q > 3 … P(a, q) ≤ (φ(q) log q)²") gives
  X ≥ (1/4 − o(1)) log p.

*Proof.*
1. *Smooth part.* p + x ≡ xp + 1 ≡ x + 1 (mod ℓ^{a_ℓ}), and 1 ≤ x + 1 < ℓ^{a_ℓ}, so v_ℓ(N) = v_ℓ(x+1) for all ℓ ≤ X + 1.
   This is (i).
2. *Residues mod x.* Every prime power exactly dividing x divides Q_X, so p ≡ 1 (mod x), N ≡ 1 (mod x), and
   r = N/(x+1) ≡ 1 (mod x).
3. *Factorising d.* Write d = d₁d₂ with d₁ = gcd(d, x+1) and d₂ | r; this works because gcd(x+1, r) = 1.
4. *d₂ is proper.* If d₂ ∈ {1, r}, then d ≡ d₁ (mod x) with 1 ≤ d₁ ≤ x + 1. Then d₁ ≡ −1 forces d₁ = x − 1, and x − 1 | x + 1
   forces x ≤ 3. This is impossible. ∎

**CERTIFIED** (`scripts/z53_hcshifts_linnik.py`, PARI, exit 0, `linnik_W3_check.txt`; independently re-run by the
reviewer, who also checked (i) at all 440 line instances).
* For X = 16, 20, 24, 32 the first 3, 3, 2, 2 primes p ≡ 1 (mod Q_X) were checked: p = 87 568 474 593 601, …,
  434 424 710 172 806 936 102 520 001, with X/log p ≈ 0.49–0.54.
* (i) and (ii) hold.
* **HC(p) = 4 at every one of them**, with 42, 28, 14; 60, 28, 100; 92, 98; 104, 64 certificates of coordinate ≤ X.

*Reading (Assessment).* W3 is a growing-window, pointwise analogue of the transparent-certificate barrier B4: smooth parts
plus one opaque rough cofactor certify nothing up to X ≍ log p. The instances show the rough-splitting part restores
certificates at once.
* *Scope.* Since p ≥ Q_X + 1, these windows have X ≤ (1/2 + o(1)) log p. A proof of T whose certificates lie within the
  window X ≍ log p must, at the W3 primes, fire a line through a rough-splitting divisor. Certificates at coordinates
  between X and (log p)^A are not constrained by W3.
* *With H4.* Combined with H4_NOT_POLYLOG Thm 1 (fixed κ < 1/12 effective; κ < 1/6 relative to Gallagher's theorem (G);
  there is no certificate with a coordinate and its numerator both ≤ exp((log p)^κ), infinitely often): every coordinate
  x ≤ (log p)^A is below exp((log p)^κ). So a proof of T must, at H4's primes, fire a line through a divisor d with both d
  and N/d above exp((log p)^κ). This rests on the imported H4 energy lemma, which is not re-proved here.
* A joint version on one set of primes is not claimed.

## 3. Q2: anatomy of the shifted family at one p

**Remark 3.1 (small divisors are congruence data).** PROVED, with the universal reading as Assessment.
* *PROVED.* For every p and 1 ≤ X < p:
  Σ_{x≤X} #{d ≤ X : d | p+x} = Σ_{d≤X} #{x ≤ X : x ≡ −p (mod d)} ≥ Σ_{d≤X} ⌊X/d⌋ = X log X + O(X).
  For levels the same holds with gcd(d, p) = 1, which is automatic for d ≤ X < p.
  * Each such divisor is the congruence event p ≡ −x (resp. −x⁻¹) (mod d).
  * It certifies line x only if d = tx − 1, i.e. with a second coordinate t (resp. u) ≤ (X+1)/x.
  * Certificates with a coordinate and its numerator both ≤ exp((log p)^κ) are empty infinitely often (H4_NOT_POLYLOG,
    A_min; κ as above).
  * Prop W3 handles smooth, not necessarily small, divisors at X ≍ log p.
  * Sylvester–Schur-type facts constrain only sizes. Examples: Sylvester's theorem for the block p+1, …, p+X; the X-smooth
    part of ∏_{x≤X}(p+x) is ≤ X!(p+X)^{π(X)}.
* *Assessment.* Among the structures examined here, every forced divisibility in the window is congruence data, and
  congruence data does not force a firing line at the scoped windows (H4, W3). A general theorem that *no* deterministic
  joint-factorisation mechanism exists is not claimed.

**Lemma C (confinement; PROVED, elementary).** Let p ≡ 1 (8) be prime, x ∈ 𝒞 with x < p, G = (ℤ/xℤ)^× and
N ∈ {N_x^e, N_x^l}.
* (a) If all prime factors of N lie in a subgroup H ≤ G with −1 ∉ H, the line does not fire on N.
* (b) A *necessary* condition for (a) is −1 ∉ ⟨N mod x⟩, because the prime factors multiply to N. It is not sufficient:
  whether the actual factors lie in such an H is a Landau-type event.
* (c) Level lines (N ≡ 1) and endpoint lines with 4 | x always satisfy the necessary condition: every power of p is ≡ 1
  (mod 4), while −1 ≡ 3 (mod 4).
* (c′) For an endpoint line, call x **unconfinable** if −1 ∈ ⟨p mod x⟩. For x = q prime ≡ 7 (8) this holds iff
  (p/q) = −1.
  *Proof.* G is cyclic of order q − 1 = 2m with m odd, and −1 is its unique involution. So ⟨p⟩ ∋ −1 iff ord p is even, iff
  p lies outside the odd-order subgroup of squares. ∎
  For composite odd x ∈ 𝒞, the condition is p^k ≡ −1 modulo every prime power of x for a single k.
* (d) At p = m² (m odd, gcd(m, x) = 1) every line is confined by the Kronecker character χ_{−x} = (−x/·).
  * Since −x ≡ 1 (mod 4) for x ≡ 7 (8), and −x ≡ 0 (mod 4) for 4 | x, χ_{−x} is an odd (possibly imprimitive) Dirichlet
    character mod x.
  * For an odd prime ℓ | N: m² ≡ −x (resp. xm² ≡ −1) mod ℓ makes −x a square mod ℓ.
  * The prime 2 divides N only if x ≡ 7 (8), and then χ_{−x}(2) = +1 because −x ≡ 1 (mod 8).
  * This is the T1 argument (ET Prop 1.6; LOWERTAIL_ROUND2_FABLE Cor 1.2) in line form.
* (e) (Mordell class q = 7.) If (p/7) = −1, line 7 fires.
  *Proof.* N = p + 7 = 2^a m with a ≥ 3. Mod 7, ⟨2⟩ = {1, 2, 4} is the group of squares and m is a non-square, so the
  divisors 2^j m, j = 0, 1, 2, run through the non-squares {3, 5, 6} ∋ −1. ∎

*Reading (Assessment).* At a prime, the necessary condition for T1-type confinement fails exactly on the unconfinable
endpoint lines. On those lines the non-square-ness of p rules out confinement, but it forces firing only when a small
smooth part sweeps the relevant coset, which is a congruence event (e).

EVIDENCE (`confinable_vs_unconfinable.txt`): endpoint lines at primes q ≡ 7 (8), P(miss | unconfinable) vs
P(miss | confinable):

| q | at 10⁹ | at 10¹³ |
|---:|---|---|
| 7 | 0 vs 0.19 | 0 vs 0.16 |
| 23 | 0.16 vs 0.40 | 0.13 vs 0.33 |
| 47 | 0.37 vs 0.56 | 0.31 vs 0.47 |
| 127 | 0.70 vs 0.73 | 0.62 vs 0.65 |

Unconfinable lines miss by *anatomy deficit*: the subset products of the prime factors avoid −1 although they generate a
group containing it. This is the line-level form of "reciprocity forces parity, not class" (FRONTIER §3).

**Empirical regularities (EVIDENCE; `z53_hcshifts_hc.c` modes range/lines, `_indep.py`, `_strat.py`, `_summary.py`).**

**(L1) Occupancy law** (`fire_law.txt`; each (x, type) is binned by b = ⌊log₂ τ(N)⌋, and the model prediction
1 − exp(−c·τ(N)/φ(x)) is averaged over the actual τ in the bin, c = 1 endpoint, c = 1/2 level).
* The observed firing rates follow the prediction in shape at every x ∈ {23, …, 256} tested.
* The prediction is systematically *high*. The pooled ratio observed/predicted over bins with prediction ≥ 0.2 is
  0.76–0.97. The excess is largest at small τ: for example level lines with τ < 16 almost never fire at x = 23, 31, 47.
* Rates agree within ≈ 0.01–0.03 across 10⁹, 10¹¹ and 10¹³, so the law is stable across scales.
* Reading: a line's chance is governed, up to a bounded factor, by τ(N)/φ(x). That is all the model below uses, since
  bounded factors do not change its exponents. "Only through τ" and "fires only if τ ≳ φ" are *not* claimed.

**(L2) Conditional independence of misses given small-prime residues** (`indep_*.txt`).
* *Raw.* The all-miss frequency P(HC > X) exceeds the product of per-coordinate miss rates by ×3.0, ×4.6, ×22 and ×83 at
  X = 7, 12, 16, 24 (10⁹; similar at 10¹¹, 10¹³). With endpoint and level counted as separate events the excess is ×9.7
  to ×625.
* *Stratified by p mod 15015, in-sample.* Ratio 0.98–1.05 for X ≤ 12 and 1.05–1.16 at X = 15–16 (10⁹). At 10¹³:
  0.98–1.08 for X ≤ 12, 1.19 at X = 15, 0.68 at X = 16.
* *Held out* (marginals fitted on half the primes, evaluated on the other half): 0.97–1.17 for X ≤ 12 and 0.82–1.53 at
  X = 15–16.
* *Separate endpoint/level events:* 0.95–1.01 for X ≤ 12 and 1.01–1.12 at X = 15–16.
* At X ≥ 20 the residual ratios (0.5–3.6) rest on ≤ 26 events.
* Reading: conditioning on p modulo small primes removes nearly all of the all-miss excess at these coordinates. This is
  consistent with the large prime factors acting independently across the window integers. The full joint distribution
  was not tested, and private-factor independence remains a *model assumption* below.

**(L3) Landau-type decay with p** (`samples_summary.txt`).
* At fixed X, P(HC > X) decreases with p: P(HC > 4) = 0.073, 0.067, 0.061, 0.057, 0.052 and
  P(HC > 8) = 1.65, 1.19, 0.92, 0.75, 0.60 ·10⁻³ at 10⁹, …, 10¹³.
* Max HC per sample: 31, 32, 32, 23, 23.

### 3.2 The model 𝔐 and the scale (log p)^{2 log 2} (Assessment; model computation)

**Model 𝔐.** Fix p and put λ = log log p.
* The lines x ∈ 𝒞 ∩ [4, X], both types, miss independently.
* Each misses with probability E[exp(−c·2^ω/φ(x))], where ω ~ Poisson(λ) is a Kubilius / Sathe–Selberg proxy for ω of a
  shifted prime, and c ∈ {1, 1/2}.
* For statements about counting functions over primes, add **𝔐×**: different primes are independent draws.

Support for 𝔐:
* (L1) and (L2) are the empirical support, up to bounded factors.
* E 2^ω = e^λ = log p matches the Titchmarsh divisor theorem Σ_{p≤P} τ(p+a) ~ C(a)P. That theorem is used only for the size
  of E τ and was not re-verified from a source here.

**Model computation.** Write X = (log p)^{κ log 2}, Q(κ) := κ log κ − κ + 1 and g(κ) := κ log 2 − Q(κ) = κ(1 + log 2 − log κ) − 1.
1. *One line.* Take φ(x) ≈ x = (log p)^{a} with ln 2 < a < 2 ln 2, and put κ_a = a/ln 2. (Losing φ(x)/x ≥ c/log log x does not
   change exponents.) Poisson large deviations give −log P(miss) ≈ E[1 − e^{−2^ω/x}] = (log p)^{−Q(κ_a)+o(1)}.
2. *One dyadic block.* It has ≍ x lines, so it costs (log p)^{g(κ_a)+o(1)}.
3. *Small lines.* g increases on [1, 2], with g(1) = log 2 and g(2) = 1. Lines with x < (log p)^{log 2} cost O(λ) each.
4. *Sub-critical tail.* Hence, in 𝔐, **−log P(HC(p) > (log p)^{κ log 2}) = (log p)^{g(κ)+o(1)} for 1 < κ < 2.**
5. *Numerical check* (`scripts/z53_hcshifts_model.py`). log(cost)/λ at λ = 160 is 0.804, 0.924, 0.990 for
   κ = 1.2, 1.5, 1.8, against g = 0.813, 0.932, 0.990.
6. *Critical scale* (corrected after review). At X = M(log p)^{2 log 2}, with M > 0 fixed, summing the linear part over
   x ≥ 2^ω gives cost ≫ E[2^ω (log X − ω log 2)_+] = e^λ E[(log M + (2λ − V) log 2)_+] with V ~ Poisson(2λ). This is
   ~ (log 2)√(λ/π)·log p. So **P(HC(p) > M(log p)^{2 log 2}) ≤ exp(−c log p √(log log p))**, which is summable over p. At
   κ = 2 the script gives log(cost)/λ = 1.010 at λ = 160, consistent with log p·√λ growth.

**Consequences in 𝔐.**
* (a) By the first Borel–Cantelli lemma (no independence across primes needed), HC(p) ≤ M(log p)^{2 log 2} for all large p,
  for every fixed M > 0.
* (b) Under 𝔐×: for fixed κ < 2, g(κ) < 1, so the primes p ≤ P with HC(p) > (log p)^{κ log 2} number P^{1−o(1)} almost
  surely. In particular, with κ = 1/log 2 (X = log p, g = 0.914), **HC(p) > C log p for a set of primes of counting
  function P^{1−o(1)}, for every C**. LOWERTAIL_ROUND2_FABLE Conjecture 3.4 (HC ≤ C log p) is false in 𝔐 + 𝔐×.
* (c) Hence in 𝔐 + 𝔐×, limsup log HC(p)/log log p = 2 log 2 ≈ 1.386, and T is consistent with 𝔐 + 𝔐× iff A ≥ 2 log 2.
* (d) *Dark range.* For (4+ε) log p ≤ X ≤ (log p)^{2 log 2 − ε}, 𝔐 + 𝔐× predicts infinitely many primes with HC > X.
  * No single Theorem-W family can certify such a growing threshold at infinitely many members (PROVED; W bounds the
    certified window, not the actual HC of the members).
  * For the Prop 3.3 family the BH first-hit scale is already log p/log log p (Assessment).
  * In 𝔐 the exceedances come from lightly-hit lines missing at random, not from congruence or primality structure.

**What 𝔐 suggests about T at the extremes (Assessment; model interpretation only, no arithmetic necessity).**
* At the extremal primes the window up to ≈ (log p)^{2 log 2} is lightly hit: typical window integers have
  τ ≈ (log p)^{log 2} ≪ φ(x).
* In 𝔐 the hits at the critical scale are carried, on the logarithmic scale, by window integers with
  ω = (2 − o(1)) log log p. The tilted ω is 2λ − O(√λ), so many hits have τ/φ(x) exponentially small in √λ.
* Hits with τ ≳ φ(x) are *not* predominant: in the Poisson model their share at x = 2^{2λ} is 0.17, 0.092 and 0.067 for
  λ = 20, 80, 160 (cross-review computation), decaying like λ^{−1/2}.
* So in the model, T at the extremes looks like a single-p large-deviation event in the anatomy of the window integers,
  combined with a tied-class divisor event. Nothing in Remark 3.1 or Lemma C forces it. This is B2 at one integer, not a
  proved requirement on proofs of T.

### 3.3 Robustness of the exponent (Assessment)

* *Consequence (b).* The positive correlations seen in (L2) only enlarge P(HC > X) at the tested scales. Whether they do
  so throughout the extreme tail is not established.
* *Consequence (a).* This needs that no choice of p modulo small primes cuts the hit rate on *all* lines up to
  (log p)^{2 log 2} by an unbounded factor.
  * Whatever p mod ℓ is (p ≢ 0), ℓ divides a proportion 1/ℓ of the endpoint and of the level integers, so the
    window-averaged E τ is invariant.
  * The structured conspiracies seen change rates by bounded factors. p ≡ 1 (mod x) pairs classes like a level line
    (factor 2). Square-mimicking p (cost 2^{π(y)}, affordable to y ≍ log p log log p) confines only the small-prime part
    of each N_x, which roughly halves the useful divisors.
  * Neither point is a proof.
* *Scope of 𝔐.* 𝔐 is a heuristic for primes only. It ignores the character layer and would wrongly predict firing at odd
  squares, where Lemma C(d) confines every line.

## 4. Q3: numerics

**Samples** (`samples_summary.txt`; 600 000 consecutive primes p ≡ 1 (8) from each 10^k).
* HC is exact. The masks cover 𝒞 ∩ [4, 128]. The scan stops at the first x ≥ 128 where HC and the auxiliary minima
  (≤ 256) are known.
* The type columns use the engine's *existential* flags. "rough-splitting" means **every** HC-certificate at that prime is
  rough-splitting w.r.t. y = 64² = 4096; the column gives the fraction of primes.

| start | P(HC>4) | P(HC>8) | P(HC>16) | max HC | all-HC-certificates rough-splitting, HC ∈ [12,16] | same, HC = 8 |
|---:|---:|---:|---:|---:|---:|---:|
| 10⁹ | 0.0734 | 1.65e-3 | 9.3e-5 | 31 | 5.5 % | 6.0 % |
| 10¹⁰ | 0.0666 | 1.19e-3 | 5.7e-5 | 32 | 9.0 % | 7.2 % |
| 10¹¹ | 0.0611 | 9.2e-4 | 3.8e-5 | 32 | 14.1 % | 10.2 % |
| 10¹² | 0.0565 | 7.5e-4 | 2.7e-5 | 23 | 15.9 % | 11.3 % |
| 10¹³ | 0.0523 | 6.0e-4 | 8.3e-6 | 23 | 16.7 % | 14.5 % |

* Over this range the rough-splitting fraction rises monotonically with p in the HC = 8 and HC ∈ [12,16] bins. The
  sparse HC ≥ 20 bin (56 → 5 primes) is not monotone.
* With the threshold y = x (the coordinate itself) the flag reads "all rough-splitting" for ≈ 46 % of primes at HC = 4 and
  for all primes at HC = 8. No mechanism is claimed for the latter.
* EVIDENCE for the kickoff hypothesis that as p grows the HC-certificates increasingly need large primes. It is
  consistent with W3 and 𝔐.

**Why hard primes are hard** (`hard_primes_anatomy.txt`, `scripts/z53_hcshifts_hardanat.py`). The sample primes with
HC ≥ 20 (56, 23 and 5 primes at 10⁹, 10¹¹, 10¹³) were compared with 3 000 random primes of the same scale, over the lines
x ∈ 𝒞 ∩ [4, 20):

| quantity | HC ≥ 20 (10⁹ / 10¹¹ / 10¹³) | random (10⁹ / 10¹¹ / 10¹³) |
|---|---|---|
| mean log₂ τ(N) | 3.15 / 3.11 / 3.21 | 3.80 / 3.99 / 4.14 |
| hit sum H = Σ (τ(N^e) + τ(N^l)/2)/φ(x) | 22 / 23 / 31 | 43 / 52 / 61 |
| #{ℓ ∈ {3,…,13} : p ≡ 1 (mod ℓ)} | 2.2 / 2.35 / 2.6 | 1.1 |
| #{ℓ ≤ 23 odd : (p/ℓ) = +1} | 6.8 of 8 | 4.0 |

At accessible scales hardness mixes two things:
* congruence structure: square-mimicking, the T1 deformation, and p ≡ 1 modulo small primes, which makes the smooth parts
  useless as in W3;
* an anatomy deficit in the window integers.

**Hard primes** (`hard_primes_hc.txt`, 166 primes):
* All 14 (★)-zeros have HC ∈ {4, 7, 8, 12, 31, 39}; the maximum is 39 at 83 449.
* z49's HC ≥ 32 primes reproduce.
* Prop 3.3(a) instances have HC = 15, 12, 15; Prop 3.3(b) instances (X = 4) have HC = 12, 7, 7.

**Controls** (`controls_squares_nearsquares.txt`):
* Odd squares m², m odd in [100 001, 110 000] (5 000 values): **no line in 𝒞 ∩ [4, 256] fires** (T1, CERTIFIED for this
  range).
* Near-squares p = m² + k (2 000 primes each, m ≥ 10⁵), P(HC > 4):
  * k = 9: 0.106, against 0.067 generically at 10¹⁰. This is the T1 deformation of (J)53/(J)55.
  * k = 24: 0.063; k = 1: 0.035; k = 16: 0.048.
  * k = 8, 17: 0. Primality forces 3 | m, so p ≡ 2 (mod 3) and 3 | p + 4: a congruence artifact.
* W3 primes: HC = 4.

## 5. FRONTIER §4 hard screens

| statement | T1 squares | 8/131 | tied modulus | fixed p |
|---|---|---|---|---|
| Theorem W, Prop W2, Prop W3 | n/a: limits on kills; true at squares trivially | n/a (numerator-agnostic, harmless for a limit) | they *are* statements that congruence/primality data below ≍ log p cannot break the tie | yes (W3: specific primes) |
| Model 𝔐 / scale 2 log 2 | **fails**: ignores the character layer; a heuristic, not a mechanism | 4-specific through 𝒞 | **fails**: only prices the tie | heuristic at one p, calibrated on averages |
| T with A ≥ 2 log 2 (CONJECTURE) | passes (false at squares, Lemma C(d)) | 4-specific | **fails**: B2 | yes |

Nothing passes line 4, as in every previous round.

## 6. Proposed FRONTIER §7.2 text (not edited here)

> *(z53 HCSHIFTS, `Z53_HCSHIFTS.md`.)*
> * **Hypothesis-H kills of the one-coordinate target stop at X ≍ log p.**
>   * Every Theorem-M family that factors all window integers N_x = p + x, xp + 1 (x ∈ 𝒞 ∩ [4, X]) into prime-valued factors
>     has p fixed modulo every prime ℓ ≤ X/4. So all its members but the least have log p > (1/4 + o(1))X (Theorem W,
>     PROVED).
>   * Under a non-standard uniform Bateman–Horn bound, Prop 3.3's family reaches HC > c log p/log log p (CONDITIONAL).
> * **Smooth-part certificates die at X ≍ log p.** At infinitely many primes every certificate with coordinate
>   ≤ X ≥ log p/10.4 (GRH: log p/4) splits the X-rough part of its integer (Prop W3, PROVED rel. Linnik). The certified
>   instances all have HC = 4.
> * **Empirical regularities (EVIDENCE, 10⁹–10¹³).**
>   * Line x fires with probability ≈ 1 − exp(−c τ(N)/φ(x)); the model over-predicts by 3–24 %.
>   * Coordinate misses are close to independent once p mod 15015 is fixed (held-out ratios 0.97–1.17 for X ≤ 12,
>     0.82–1.53 at X = 15–16 on few events).
> * **Re-calibration (Assessment).** In the independent-anatomy model fitted to these regularities,
>   P(HC > (log p)^{κ log 2}) = exp(−(log p)^{g(κ)+o(1)}) with g(κ) = κ(1 + log 2 − log κ) − 1 < 1 for 1 < κ < 2, while
>   HC ≤ (log p)^{2 log 2} eventually.
>   * So Conjecture 3.4 (HC ≤ C log p) is predicted false (with independent draws across primes).
>   * The model-consistent target is HC ≤ (log p)^A with A ≥ 2 log 2 ≈ 1.386.
>   * The model's exceedances in (4+ε) log p ≤ X ≤ (log p)^{2 log 2 − ε} cannot be *certified* by any single H-family
>     at infinitely many members (W bounds the certified window, not actual HC).
> * **Structure (PROVED + Assessment).** Among the structures examined, the forced small-divisor structure of the window
>   is congruence data. T1's confinement fails at a prime only on "unconfinable" endpoint lines, which still miss by
>   anatomy deficit. In the model, T at the extremes looks like a single-p anatomy large deviation combined with a
>   tied-class divisor event (Assessment, not a proved requirement).

**Bottom line.**
* The kickoff's key observation is now a theorem, scoped to fixed families. A Hypothesis-H/Dickson kill must fix p modulo
  every prime up to X/4, so one family cannot certify a growing threshold beyond (4 + ε) log p at infinitely many
  members. This bounds the certified window, not the actual HC. The displayed
  family needs a non-standard uniform Bateman–Horn bound even to reach log p/log log p.
* This wall is not a source of hope for the polylog target. In the anatomy model built from three scale-stable regularities
  (occupancy law, conditional independence, Poisson ω), HC exceeds (log p)^{2 log 2 − ε} infinitely often anyway, through
  lightly-hit lines, and stays below (log p)^{2 log 2}.
* So the model-consistent target is HC ≤ (log p)^A with A ≥ 2 log 2, and the C log p conjecture is model-disfavoured.
* Smooth-part certificates are provably insufficient within windows X ≍ log p. Among the structures examined, all
  forced small-divisor structure is congruence data. What remains is a large-deviation-plus-tied-class event among the large primes of one shifted integer: B2 at a
  single p, with no new handle.
* **Verdict: narrowed.**

## 7. Reproduction

```sh
ulimit -v 2000000
gcc -O2 -o /tmp/z53hc scripts/z53_hcshifts_hc.c -lm
for e in 9 10 11 12 13; do timeout 1700 /tmp/z53hc range 1$(printf '0%.0s' $(seq 1 $e)) 600000 256 4096 > samp_1e$e.txt; done   # 1-4 min each
for e in 9 11 13; do timeout 1700 /tmp/z53hc lines 1$(printf '0%.0s' $(seq 1 $e)) 200000 256 > data/z53/hcshifts/lines_1e$e.txt; done
python3 scripts/z53_hcshifts_summary.py samp samp_1e*.txt  > data/z53/hcshifts/samples_summary.txt
python3 scripts/z53_hcshifts_summary.py lines data/z53/hcshifts/lines_1e*.txt > data/z53/hcshifts/fire_law.txt
uv run python scripts/z53_hcshifts_indep.py samp_1e9.txt samp_1e11.txt samp_1e13.txt    # (L2) raw
uv run python scripts/z53_hcshifts_strat.py samp_1e9.txt samp_1e13.txt                  # (L2) stratified, in-sample (~15 min)
uv run python scripts/z53_hcshifts_strat.py --holdout samp_1e9.txt samp_1e13.txt        # (L2) held-out
uv run python scripts/z53_hcshifts_strat.py --sep samp_1e9.txt                          # (L2) endpoint/level separate
python3 scripts/z53_hcshifts_confine.py samp_1e9.txt samp_1e13.txt                      # Lemma C data
timeout 600 /tmp/z53hc list 256 4096 < data/z53/hcshifts/hard_primes_list.txt > data/z53/hcshifts/hard_primes_hc.txt
uv run --with sympy python scripts/z53_hcshifts_wall.py                                 # Theorem W forced-prime table
uv run --with cypari2 python scripts/z53_hcshifts_linnik.py                             # Prop W3 instances (exit 0)
python3 scripts/z53_hcshifts_model.py                                                   # model exponent g(kappa)
uv run --with cypari2 python scripts/z53_hcshifts_hardanat.py samp_1e9.txt samp_1e11.txt samp_1e13.txt
scripts/z53_hcshifts_controls.sh                                                        # squares / near-squares
```
The raw samples (≈ 240 MB) are not committed; the first loop regenerates them deterministically. The engine aborts if a
divisor count exceeds its 2¹⁶ buffer; the reviewer bounded τ ≤ 64 512 over the ranges used.

## 8. Review log

Internal hostile review (deep mode, 2026-11-01), verdict UNSOUND-as-written. Full text:
`data/z53/hcshifts/REVIEW_internal_deep.md`. Issues and repairs:

1. **CRITICAL** — "universal growing-window wall". W is now stated for one fixed family (all members but the least;
   the reviewer confirmed this holds for polynomial families too), with explicit scope, and the dark range's PROVED part
   starts at (4+ε) log p.
2. **MAJOR** — The boundary-scale calculation was wrong. The cost at M(log p)^{2 log 2} is ≍ log p·√(log log p), so
   A = 2 log 2 is allowed; corrected in §3.2(6) and (a)–(c).
3. **MAJOR** — The cross-prime model was missing. 𝔐× is added for counting-function claims, and "retire" is softened to
   "model-disfavoured".
4. **MAJOR** — L1 accuracy was overstated. The law is now averaged over exact τ per bin (`lines` mode stores the sum of
   predictions) and restated with its 3–24 % over-prediction.
5. **MAJOR** — L2 was in-sample and OR'ed endpoint/level events. It is rerun held-out and with separate events, and
   independence of private factors is now a model assumption.
6. **MAJOR** — The BH limit is restricted to the displayed family and called a first-hit scale.
7. **MAJOR** — Remark 3.1's universal claim is downgraded to Assessment, and κ is specified.
8. **MAJOR** — "Private" is split into rough-splitting vs shift-private (threshold X²). The engine's flags are documented
   as existential and the tables relabelled; the wrong HC = 8 explanation is removed.
9. **MINOR** — The stale 10¹³ raw-independence block is regenerated (3.02, 3.65, 4.46, 18.43, 14.09). The
   "falls steadily" wording is fixed.
10. **MINOR** — Domain conditions (X < p, gcd(d, p) = 1) are added. UBH now requires distinct, non-proportional,
    primitive forms. Lemma C(b) is stated as necessary only.
11. **MINOR** — Engine coverage is documented. A divisor-buffer guard and an XCAP check are added. The W3 script now checks
    (i) at every 1 ≤ x ≤ X.

All other proofs (W fixed-family, W2, W3, Lemma C(a)–(e), the sub-critical g(κ)) and all numbers were confirmed by the
reviewer, including an independent re-run of the engine and of W3.

**Cross-model review** (`data/z53/xreview/REVIEW_HCSHIFTS.md`, verdict ACCEPT-WITH-FIXES). The reviewer independently
reran the engine on all 166 hard primes, the W3 instances, two 600 000-prime samples, the held-out L2, the confinement data,
the L1 reductions, the wall table and the model script, and found agreement. Required fixes, all applied:
1. **Major — W quantifiers.** W bounds the window that a fixed family *certifies*, not the actual HC of its members. The
   wording in §§0, 2.1, 3.2(d), 6 and the bottom line now says "cannot certify a growing threshold (except possibly the
   least member)".
2. **Major — W3 inference.** Since X ≤ (1/2 + o(1)) log p, W3 constrains only certificates within logarithmic windows. The
   claim that every proof of the polylog target must split rough parts is removed; the H4 consequence (valid for all
   x ≤ (log p)^A) is kept, scoped to the imported H4 lemma.
3. **Major — model interpretation.** The claim that hits at the critical scale come "predominantly from τ ≳ φ(x)" is
   wrong: their share is O(λ^{−1/2}) (0.17, 0.092, 0.067 at λ = 20, 80, 160). It is replaced by the logarithmic-scale
   statement ω = (2 − o(1)) log log p. All "a proof of T must …" statements derived from 𝔐 are removed, and 𝔐× is now
   explicit in the "iff A ≥ 2 log 2" claims.
4. **Moderate — L2 headline.** "±20 %" is replaced by the held-out ranges 0.97–1.17 (X ≤ 12) and 0.82–1.53 (X = 15–16;
   the 1.53 rests on 16 events). The separate-endpoint/level run is identified as in-sample.
5. **Minor.** log Q = (5/6 + o(1))X for the Prop 3.3 family (it was stated as X; only the lower-order term changes). The
   FRONTIER formula now carries +o(1) and 1 < κ < 2. "Among the structures examined" is added to the congruence claims.

