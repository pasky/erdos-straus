# Z53_HCSHIFTS: the one-coordinate polylog target HC(p) ≪ (log p)^A, growing-window kills, and the anatomy of shifted families

**ES is open. Nothing here proves or disproves ES, ES₅, (★), or HC(p) ≪ (log p)^A.** Each claim carries one label:
PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Everything is internal and unrefereed. This
is lane z53 HCSHIFTS (FRONTIER §7.2). Scripts are in `scripts/z53_hcshifts_*` and data in `data/z53/hcshifts/` (168 KB);
exact commands are in §7.

## 0. Verdict first: **narrowed**, plus a re-calibration of the target scale

**Target T (FRONTIER §7.2; OPEN).** There is an A such that HC(p) ≤ (log p)^A for all large primes p ≡ 1 (mod 8).

1. **The Hypothesis-H/Dickson kill has a wall at X ≍ log p (Theorem W; PROVED, elementary).** Take any Hypothesis-H-certified
   family of primes (Theorem-M formal run, POINTWISE_SIZE) on which no line x ≤ X fires. For every odd prime
   ℓ ≤ ⌊X/4⌋ + 1, p mod ℓ must be constant along the family. So every member except possibly one has
   log p > θ(⌊X/4⌋+1) − log 2 = (1/4 + o(1))X. **No H-type construction can refute T for any A ≥ 1, nor refute
   HC(p) ≤ (4+ε) log p.**
   * Under a uniform Bateman–Horn lower bound (UBH, non-standard), the Prop 3.3 family of LOWERTAIL_ROUND2_FABLE gives
     HC(p) > c·log p/log log p infinitely often (Prop W2; CONDITIONAL on UBH).
   * In the Bateman–Horn heuristic, no Dickson family gets past (4/3 + o(1)) log p/log log p (Assessment).
   * So the kill extends to growing X, but only to X ≍ log p/log log p, and it needs ≍ X simultaneously prime
     cofactors, as the kickoff suspected.
2. **Certificates built from smooth parts die at X ≍ log p, unconditionally (Prop W3; PROVED relative to Linnik's
   theorem).** There are infinitely many primes p at which every certificate with a coordinate x ≤ X ≥ (1/(2L) − o(1))·log p
   splits the (X+1)-rough part of its window integer nontrivially. Here L ≤ 5.2 is Linnik's constant; under GRH the bound
   becomes X ≥ (1/4 − o(1)) log p. CERTIFIED instances: X = 16, 20, 24, 32. **Every one of those primes has HC = 4**, with
   14–104 private certificates, so congruence-sterility costs the lottery nothing.
   * Together with H4_NOT_POLYLOG: a proof of T must use, at infinitely many primes, certificates whose divisor and
     cofactor both exceed exp((log p)^κ). At other infinitely many primes (Prop W3; possibly a different set) it must use
     certificates that split a window integer's rough part. Either way that means the actual factorisation of large
     primes private to one shift.
3. **Anatomy at one p (§3).**
   * PROVED: the forced structure of the window is congruence data only (Remark 3.1).
   * PROVED: T1's confinement mechanism is blocked at a prime exactly on the *unconfinable* endpoint lines (Lemma C),
     for example x = q ≡ 7 (8) prime with (p/q) = −1. Blocking forces firing only for q = 7 (the Mordell class).
   * EVIDENCE: for q = 23…127 unconfinable lines still miss 13–70 % of the time.
   * EVIDENCE, at 10⁹–10¹³: **line x fires with probability 1 − exp(−c·τ(N)/φ(x))** (c = 1 endpoint, 1/2 level), stable
     across scales.
   * EVIDENCE: **lines are independent once p mod 15015 is fixed.** The raw excess of P(HC > X) over the product of
     marginals, up to ×83, falls to ≈ 1 for X ≤ 16.
4. **Model consequence (Assessment): the extremal scale of HC is (log p)^{2 log 2 + o(1)} ≈ (log p)^{1.386}, not O(log p).**
   Assume the independent-private-anatomy model 𝔐 that the EVIDENCE supports, with ω of window integers Poisson(log log p).
   * Then P(HC(p) > (log p)^{κ log 2}) = exp(−(log p)^{g(κ)+o(1)}) with g(κ) = κ(1 + log 2 − log κ) − 1 < 1 for κ < 2.
   * So HC(p) > (log p)^{2 log 2 − ε} on a set of primes of counting function P^{1−o(1)}.
   * **Conjecture 3.4 of LOWERTAIL_ROUND2_FABLE (HC ≤ C log p) is false in 𝔐**: at X = log p, g = 0.914 < 1.
   * T itself is consistent with 𝔐 exactly for A > 2 log 2.
   * The range between log p/log log p and (log p)^{2 log 2} is a **dark range**. There 𝔐 predicts infinitely many
     exceedances, but no H-type family can certify one (Theorem W).
   * At the extremes the window lines are "lightly hit": a line fires only if its integer has τ ≳ φ(x), i.e.
     ω ≳ 2 log log p.
5. **Numerics (CERTIFIED/EVIDENCE).**
   * HC was computed for 3·10⁶ primes p ≡ 1 (8) (600 000 consecutive ones from each of 10⁹, …, 10¹³), all lines to 256.
   * Also computed: 166 hard primes (the 14 (★)-zeros, z49's HC ≥ 32 list, Dickson instances, HC ≥ 20 sample primes),
     12 000 near-squares and 5 000 odd squares.
   * Odd squares: no line fires (T1).
   * At HC ∈ [12,16] the HC-certificate is private-type relative to the privacy threshold 64² in 5.5 % → 16.7 % of cases
     from 10⁹ to 10¹³, rising with p.

**What the lane buys.** Two scoped kill theorems (W, W3) answer Q1: the B1 kill stops at ≍ log p. One model computation,
backed by three scale-stable empirical laws, moves the target scale from log p to (log p)^{2 log 2}. One structural lemma
(C) locates T1 in the coordinate lines. **No positive step toward T** (Assessment): every forced structure found is
congruence data, and the open step is a single-p anatomy statement about private primes, i.e. B2.

## 1. Objects and precise statements

For a prime p ≡ 1 (mod 8) let 𝒞 = 𝒞_p = {x ≥ 4 : 4 | x or x ≡ 7 (mod 8)}. For x ∈ 𝒞 the two **lines** are the integers
  N_x^e := p + x (endpoint line),  N_x^l := xp + 1 (level line).
Both are prime to x: N_x^e ≡ p and N_x^l ≡ 1 (mod x), and p > x. Line x **fires** if N_x^e or N_x^l has a divisor
d ≡ −1 (mod x).
* A divisor d ≡ −1 of N_x^e is the numerator A = tx − 1 of the word (t, x, N/d).
* A divisor d ≡ −1 of N_x^l is the numerator A = xu − 1 of the word (x, u, ·).

By LOWERTAIL_ROUND2_FABLE Thm 1 / Cor 1.1 (PROVED there), firing lines are exactly the five-slice certificate words with a
𝒞-coordinate equal to x, and
  **HC(p) = min{x ∈ 𝒞 : line x fires}**, with ES₅(p) ⟺ HC(p) < ∞.
For p ≡ 5 (8), HC = 3. The engine `z53_hcshifts_hc.c` reproduces z49's values at every listed hard prime (HC = 4, 4, 15,
7, 7, 7, 8, 8, 64, 39, 47, 56, … at 409, 577, 2521, 3361, 5569, 9601, 66529, 8 813 281, 21 841, 83 449, 92 401, 691 681).

**Certificate types.** Take a firing line with integer N, divisor d ≡ −1 (mod x) and threshold y. Write N = s·r, where s is
the y-smooth part and r the y-rough part.
* The certificate is **congruence-type (w.r.t. y)** if gcd(d, r) ∈ {1, r}. Then d mod x is determined by p modulo a y-smooth
  modulus (by s, and by r ≡ N/s mod x).
* Otherwise it is **private-type**: d splits r, so r has ≥ 2 prime factors > y, spread over d and N/d.

Privacy (SYNTHESIS_SPARKS8 Lemma 2.3 and its mixed form):
* gcd(p+x, p+x′) | x − x′;
* gcd(xp+1, x′p+1) | x − x′;
* gcd(p+x, x′p+1) | xx′ − 1.

So a prime ℓ > X² divides at most one window integer.

**Questions attacked.**
* (Q1) How far does the Dickson/H kill of Prop 3.3 extend in X = X(p)?
* (Q2) What is forced or provable about the joint factorisation of the window, and can it force a firing line?
* (Q3) At hard primes, do the HC-certificates come from smooth parts or from private primes?

**Why not already closed.** The closed items are fixed X (Prop 3.3, Dickson) and two-endpoint polylog windows
(H4_NOT_POLYLOG, unconditional). T is one-coordinate, so the divisor side is free. Neither result addresses growing X with a
free divisor side.

## 2. Q1: growing-window kills

### 2.1 Theorem W (the Dickson / Theorem-M wall; PROVED)

**Theorem W.** Let X ≥ 8 and let 𝒜 be an infinite set of primes p ≡ 1 (8) of the following form, as produced by a
Theorem-M formal run (POINTWISE_SIZE Thm M):
* p = P(q), where P is a non-constant integer polynomial and q ranges over an infinite "admissible" set;
* for every x ∈ 𝒞 ∩ [4, X] and ∗ ∈ {e, l}, the formal factorisation N_x^∗(P(q)) = c_{x,∗}·∏_i f_{x,∗,i}(q)^{e_i} holds with a
  fixed integer c_{x,∗} and non-constant irreducible f's;
* at every admissible q, every f_{x,∗,i}(q) equals a fixed constant C_{x,∗,i} times a prime.

Linear Dickson families (P linear, one form per line) are the special case used in LOWERTAIL_ROUND2_FABLE Prop 3.3.
Then for every odd prime ℓ ≤ ⌊X/4⌋ + 1, p mod ℓ is the same for all but finitely many p ∈ 𝒜. Consequently all but finitely
many p ∈ 𝒜 lie in one residue class modulo Π_X := ∏_{3≤ℓ≤⌊X/4⌋+1} ℓ. Hence all but finitely many satisfy
  log p > θ(⌊X/4⌋ + 1) − log 2 = (1/4 + o(1)) X.
For the linear form, all members except possibly the least satisfy this.

*Proof.*
1. Fix an odd prime ℓ ≤ ⌊X/4⌋ + 1. Discard the finitely many admissible q at which some non-constant f_{x,∗,i}(q) has
   absolute value ≤ ℓ·max|C|, or p = P(q) ≤ ℓ. Each non-constant polynomial takes any given value at most deg times, so
   this removes finitely many q.
2. For a remaining q, put a = p mod ℓ ∈ {1, …, ℓ−1}. The window contains the ⌊X/4⌋ ≥ ℓ − 1 multiples 4k, 1 ≤ k ≤ ⌊X/4⌋,
   of 4, and 4 is invertible mod ℓ. So some x = 4k ∈ 𝒞 ∩ [4, X] has 4k ≡ −a (mod ℓ); take the least such k ≤ ℓ − 1.
3. Then ℓ | p + x = N_x^e(P(q)) = c·∏ f_i(q)^{e_i}.
4. If ℓ ∤ c, then ℓ | f_i(q) = C_i·(prime) for some i, so ℓ | C_i or ℓ is that prime. In the second case
   |f_i(q)| ≤ ℓ|C_i|, which was excluded. In the first case, and in the case ℓ | c, ℓ divides N_x^e(P(q′)) for **every**
   admissible q′: c and C_i are fixed, and C_i divides f_i(q′) at every admissible q′.
5. Hence P(q′) ≡ −x ≡ a (mod ℓ) for all admissible q′, apart from the finitely many discarded. This proves the first claim.
6. Distinct members of one class modulo Π_X differ by ≥ Π_X. So all but the least of the (cofinitely many) members exceed
   Π_X, and θ(⌊X/4⌋+1) = (1/4 + o(1))X by the prime number theorem. ∎

*Remarks.*
* Only the endpoint lines with 4 | x were used. With all of 𝒞 and the level classes −x⁻¹, the forced product grows the
  same way: `scripts/z53_hcshifts_wall.py` gives log(∏ forced ℓ)/X = 0.24–0.28 for X = 64…4096, and the forced primes
  are contiguous up to ≈ X/4, e.g. up to 1033 at X = 4096.
* The proof never uses that the family is a *kill*. Requiring ≍ X window integers to be "fixed constant × primes" already
  forces p mod every ℓ ≤ X/4. This is the precise form of the kickoff observation "∏_{ℓ≤X} ℓ = e^X ≫ p".
* Read as a statement about T: a Theorem-M family certifying HC(p) > X(p) needs (by Theorem W) X(p) < (4 + o(1)) log p.
  **H-type kills cannot refute T for any A ≥ 1, nor refute HC(p) ≤ (4+ε) log p.**

### 2.2 Prop W2: how far the kill actually reaches (CONDITIONAL on UBH)

**Hypothesis UBH** (uniform Bateman–Horn lower bound, linear case). This is *not* a standard conjecture: standard
Hardy–Littlewood/Bateman–Horn statements fix the number k of forms. There are constants c₁ ∈ (0,1] and C₁ ≥ 1 with the
following property:
* for every k ≥ 1, every admissible family of k linear forms a_i s + b_i with 1 ≤ a_i, b_i ≤ A, and every S with
  log S ≥ C₁ k log log(AS),
* #{s ≤ S : all forms prime} ≥ c₁^k 𝔖·S/(log(AS))^k,
* where 𝔖 = ∏_ℓ (1 − ν(ℓ)/ℓ)(1 − 1/ℓ)^{−k}.

**Prop W2.** Under UBH there are infinitely many primes p ≡ 1 (mod 24) with HC(p) > c·log p/log log p, with c > 0 depending
only on c₁ and C₁.

*Proof.* Use LOWERTAIL_ROUND2_FABLE Prop 3.3(a), PROVED there:
* the forms are p = 1 + Qs, F_x = 1 + Qs/(x+1), G_x = 1 + xQs/(x+1) for x ∈ 𝒞_X = 𝒞 ∩ [4, X];
* Q = lcm(24, x(x+1) : x ∈ 𝒞_X);
* for every s with all forms prime, HC(p) > X.

Steps:
1. *Size of the family.* k = 1 + 2|𝒞_X| ≤ (3/4)X + 3. Since x and x+1 are coprime and both divide lcm(1, …, X+1),
   Q | 24·lcm(1…X+1), so log Q ≤ (1+o(1))X. The coefficients are ≤ A := XQ.
2. *Admissibility.* All forms equal 1 at s = 0, so ν(ℓ) ≤ min(k, ℓ−1).
3. *Lower bound on 𝔖.*
   * For ℓ ≤ 2k the factor is ≥ (1 − (ℓ−1)/ℓ) = 1/ℓ, so these contribute ≥ e^{−θ(2k)}.
   * For ℓ > 2k the factor is ≥ (1 − k/ℓ)(1 + k/ℓ) = 1 − k²/ℓ² ≥ 3/4, and Σ_{ℓ>2k} k²/ℓ² ≪ k/log k.
   * Hence 𝔖 ≥ e^{−C₃X}.
4. *Choice of S.* Take log S = C₂ X log X with C₂ ≥ 2C₁ large. Then log(AS) ≤ 2C₂ X log X, so UBH applies, and
   #{s ≤ S} ≥ exp(C₂X log X − k log(2C₂X log X) − C₃X − k log(1/c₁)) ≥ exp(C₂X log X − (3/4 + o(1))X log X − O(X)) ≥ 1.
5. *Conclusion.* The resulting p satisfies log p ≤ log Q + log S ≤ (C₂ + o(1)) X log X, so X ≥ (1/C₂ − o(1)) log p/log log p.
   Members are ≥ Q → ∞, so letting X → ∞ gives infinitely many distinct p. ∎

*Assessment (the BH limit).* Any Dickson family for the window X needs one prime form per line and per type, i.e.
k ≈ (3/4)X forms. In BH its expected number of members ≤ P is ≈ 𝔖P/(Q(log P)^k), with 𝔖 ≤ (C log X)^k and Q ≥ Π_X
(Theorem W). Members exist only if X/4 + (3/4)X(log log P − O(log log log P)) ≤ log P, i.e.
X ≤ (4/3 + o(1)) log P/log log P. So, heuristically, **Dickson kills reach exactly the scale log p/log log p**. Theorem W's
(4 + o(1)) log p is the unconditional wall.

### 2.3 Prop W3: congruence-type certificates die at X ≍ log p (PROVED rel. Linnik; GRH variant)

Let Q_X := ∏_{ℓ ≤ X+1} ℓ^{a_ℓ} with a_ℓ = ⌊log_ℓ(X+1)⌋ + 1. Then ℓ^{a_ℓ} > X + 1 and
log Q_X = θ(X+1) + ψ(X+1) = (2 + o(1))X; the values for X = 16…32 are 1.77X–1.84X.

**Prop W3.** Let X ≥ 7 and let p be a prime with p ≡ 1 (mod Q_X); then 16 | Q_X, so p ≡ 1 (8). For every x ∈ [1, X] and
both lines:
* (i) the (X+1)-smooth part of N_x^e and of N_x^l equals x + 1;
* (ii) every certificate d ≡ −1 (mod x) of a line x ∈ 𝒞 ∩ [4, X] is private-type w.r.t. y = X + 1. Writing N = (x+1)r,
  we have d = d₁d₂ with d₁ | x + 1 and 1 < d₂ < r, d₂ ≡ −d₁⁻¹ (mod x). In particular r has ≥ 2 prime factors (with
  multiplicity), all > X + 1, and a line whose rough part is prime does not fire.

By Linnik's theorem (least prime ≡ 1 (mod Q) is ≪ Q^L), such p exist with log p ≤ (L + o(1)) log Q_X = (2L + o(1))X.
Letting X → ∞ gives infinitely many p with **X ≥ (1/(2L) − o(1)) log p**.
* Linnik's constant: L = 5.2 is admissible (Xylouris, as cited in Lamzouri–Li–Soundararajan, arXiv:1309.3595, §1.2); L ≤ 5
  per Xylouris's thesis (Tao's constants page). So X ≥ (1/10.4 − o(1)) log p.
* Under GRH, Lamzouri–Li–Soundararajan Corollary 1.2 (checked in the arXiv PDF: "Assume GRH. Let q > 3 … P(a, q) ≤
  (φ(q) log q)²") gives log p ≤ (2 + o(1)) log Q_X, hence X ≥ (1/4 − o(1)) log p.

*Proof.*
1. *Smooth part.* p ≡ 1 (mod ℓ^{a_ℓ}) gives p + x ≡ x + 1 and xp + 1 ≡ x + 1 (mod ℓ^{a_ℓ}). Since 1 ≤ x + 1 ≤ X + 1 < ℓ^{a_ℓ},
   v_ℓ(N) = v_ℓ(x + 1) for every ℓ ≤ X + 1. This is (i).
2. *Residues mod x.* Every prime power exactly dividing x ≤ X divides Q_X, so p ≡ 1 (mod x). Hence N ≡ 1 + x ≡ 1 (mod x),
   and r = N/(x+1) ≡ 1 (mod x).
3. *Factorising d.* Write d = d₁d₂ with d₁ = gcd(d, x+1) and d₂ | r; this is possible because gcd(x+1, r) = 1.
4. *d₂ is proper.* If d₂ ∈ {1, r}, then d ≡ d₁ (mod x). With 1 ≤ d₁ ≤ x + 1, d₁ ≡ −1 forces d₁ = x − 1, and then
   x − 1 | x + 1 gives x ≤ 3. This is impossible for x ≥ 4. ∎

**CERTIFIED** (`scripts/z53_hcshifts_linnik.py`, PARI, exit 0; `data/z53/hcshifts/linnik_W3_check.txt`). For
X = 16, 20, 24, 32 the first 3, 3, 2, 2 primes p ≡ 1 (mod Q_X) were checked:
* p = 87 568 474 593 601, …, 434 424 710 172 806 936 102 520 001, with X/log p ≈ 0.49–0.54;
* (i) and (ii) hold;
* **HC(p) = 4 at every one of them**, with 14–104 certificates of coordinate ≤ X, all private.

*Reading (Assessment).* Prop W3 is the growing-window, pointwise analogue of the transparent-certificate barrier B4:
smooth parts plus one opaque rough cofactor certify nothing up to X ≍ log p. The certified instances show that the
private part restores the certificate at once. Together with H4_NOT_POLYLOG (both coordinates ≤ exp((log p)^κ) empty
i.o.), a proof of T must, at infinitely many primes, find a firing line through a divisor that
(a) is "middle" (d, N/d > exp((log p)^κ); H4 primes) and
(b) splits a rough part (Prop W3 primes).
These are two scoped statements about possibly different sets of primes; their joint version (one set) is not claimed.

## 3. Q2: anatomy of the shifted family at one p

**Remark 3.1 (forced structure is congruence data; PROVED, elementary).**
* For every p and X ≥ 1:
  Σ_{x≤X} #{d ≤ X : d | p+x} = Σ_{d≤X} #{x ≤ X : x ≡ −p (mod d)} ≥ Σ_{d≤X} ⌊X/d⌋ = X log X + O(X).
  The same holds for levels with d ∤ p, using x ≡ −p⁻¹ (mod d).
* So the window carries a deterministic mass ≍ X log X of small divisors. Each one is the congruence event
  p ≡ −x (mod d) (resp. p ≡ −x⁻¹).
* Such a divisor certifies line x only if d ≡ −1 (mod x), i.e. d = tx − 1 with t ≤ (X+1)/x. So the certificate has two
  bounded coordinates (x and t, resp. x and u).
* Certificates with both the divisor and the coordinate below exp((log p)^κ) are empty infinitely often
  (H4_NOT_POLYLOG, A_min). Prop W3 extends this to smooth (not necessarily small) divisors at X ≍ log p.
* Sylvester–Schur-type facts constrain only sizes, never the classes of the private primes. Examples: Sylvester's
  theorem for the block p+1, …, p+X; the X-smooth part of ∏_{x≤X}(p+x) is ≤ X!·(p+X)^{π(X)}.
* So **every forced divisibility in the window is congruence data, and congruence data cannot force a firing line at
  sub-power windows infinitely often.**

**Lemma C (confinement; PROVED, elementary).** Let p ≡ 1 (8) be prime, x ∈ 𝒞, G = (ℤ/xℤ)^×, and N ∈ {N_x^e, N_x^l}.
* (a) If all prime factors of N lie in a subgroup H ≤ G with −1 ∉ H, the line does not fire on N.
* (b) Such an H exists only if −1 ∉ ⟨N mod x⟩, because the prime factors multiply to N.
* (c) Level lines (N ≡ 1) and endpoint lines with 4 | x always satisfy −1 ∉ ⟨N⟩: every power of p is ≡ 1 (mod 4), while
  −1 ≡ 3 (mod 4).
* (c′) For an endpoint line with x = q prime ≡ 7 (8): −1 ∈ ⟨p mod q⟩ ⟺ (p/q) = −1. Call such a line **unconfinable**.
  *Proof.* G is cyclic of order q − 1 = 2m with m odd, and −1 is its unique involution. ⟨p⟩ ∋ −1 iff ord(p) is even, iff p
  lies outside the index-2 subgroup of squares (which has odd order m). ∎
* (d) At p = m² (m odd, gcd(m, x) = 1) every line is confined by the odd real character χ_{−x} = (−x/·) (an odd character mod x). For a
  prime ℓ | N: m² ≡ −x (resp. x m² ≡ −1) mod ℓ makes −x a square mod ℓ. This is the T1 argument of ET Prop 1.6 /
  LOWERTAIL_ROUND2_FABLE Cor 1.2 in line form.
* (e) (Mordell class q = 7.) If (p/7) = −1, line 7 fires.
  *Proof.* N = p + 7 = 2^a m with a ≥ 3, because p ≡ 1 (8). Mod 7, ⟨2⟩ = {1, 2, 4} is the group of squares, and m ≡ N·2^{−a}
  is a non-square. So the divisors 2^j m, j = 0, 1, 2, run through the non-squares {3, 5, 6} ∋ −1. ∎

*Reading (Assessment).* At a prime, the non-square-ness of p acts on a single line only through unconfinable lines (c′).
Blocking confinement forces firing only when a small smooth part sweeps the relevant coset, which is a congruence event
(e). EVIDENCE (`data/z53/hcshifts/confinable_vs_unconfinable.txt`, 10⁹ and 10¹³ samples): for q ≡ 7 (8),
P(miss | unconfinable) vs P(miss | confinable) is

| q | at 10⁹ | at 10¹³ |
|---:|---|---|
| 7 | 0 vs 0.19 | 0 vs 0.16 |
| 23 | 0.16 vs 0.40 | 0.13 vs 0.33 |
| 47 | 0.37 vs 0.56 | 0.31 vs 0.47 |
| 127 | 0.70 vs 0.73 | 0.62 vs 0.65 |

Unconfinable lines miss by *anatomy deficit*: the subset products of the prime factors avoid −1 although they generate a
subgroup containing it. This is cheap once φ(q) ≳ τ(N). It is the line-level form of "reciprocity forces parity, not class"
(FRONTIER §3).

**Three empirical laws (EVIDENCE; `scripts/z53_hcshifts_hc.c` modes range/lines, `_indep.py`, `_strat.py`,
`_summary.py`).**
* **(L1) Fire law.** P(line x fires | τ(N) = 2^b) ≈ 1 − exp(−c·2^b/φ(x)), with c = 1 for endpoint lines and c = 1/2 for
  level lines (whose certificate divisors pair as d ↔ N/d).
  * The fit is within a few % for 2^b ≥ φ(x)/4, for every x ∈ {23, …, 256} tested, at 10⁹, 10¹¹ and 10¹³ alike
    (`fire_law.txt`).
  * The mean number of certificate divisors is ≈ τ/φ(x) (ratio 0.9–1.2 for τ ≳ φ).
  * So **a line's chance depends on the anatomy of its integer only through τ, and the classes of divisors mod x behave as
    uniform**.
* **(L2) Conditional independence.**
  * Raw: empirical P(HC > X) exceeds the product of the per-line miss rates by ×3.0 (X = 7), ×4.6 (12), ×22 (16) and
    ×83 (24) at 10⁹, with similar values at 10¹¹ and 10¹³ (`indep_product_of_marginals.txt`).
  * After conditioning on p mod 15015 and averaging the per-class products, the ratio is 0.98–1.08 for X ≤ 12,
    1.16–1.19 at X = 15 and 0.68–1.05 at X = 16. Mod 105 and mod 1155 already remove most of the excess.
  * At X ≥ 20 the cells at 15015 are thin. The residual is ≤ 1.4 at X = 20 and ≤ 3.4 at X = 23, 24, from 26, 7 and 5
    events (`indep_stratified.txt`).
  * So **the line correlations are small-prime congruence data (B1) and the private parts act independently**, as
    privacy suggests.
* **(L3) Landau-type decay with p.**
  * At fixed X, P(HC > X) decreases with p: P(HC > 4) = 0.073, 0.067, 0.061, 0.057, 0.052 and P(HC > 8) = 1.65, 1.19,
    0.92, 0.75, 0.60 ·10⁻³ at 10⁹, …, 10¹³ (`samples_summary.txt`).
  * Max HC in each 600 000-prime sample: 31, 32, 32, 23, 23.

### 3.2 The model 𝔐 and the scale (log p)^{2 log 2} (Assessment; model computation)

**Model 𝔐.** Fix p, put λ = log log p, and treat the lines x ∈ 𝒞 ∩ [4, X] (both types) as independent. Each line misses
with probability E[exp(−c·2^ω/φ(x))], where ω ~ Poisson(λ) (a Kubilius / Sathe–Selberg proxy for ω of a shifted prime)
and c ∈ {1, 1/2} as in (L1).
* (L1) and (L2) are the empirical support. (L2) says congruence correlations must be added, and §3.3 argues they change
  rates only by bounded factors.
* The Titchmarsh divisor theorem (Σ_{p≤P} τ(p+a) ~ C(a)P, for example Fouvry 1985 / Bombieri–Friedlander–Iwaniec 1986;
  not re-verified here, used only for the size of E τ) fixes E τ(N_x) ≍ log p = e^λ, consistent with E 2^ω = e^λ.

**Model computation.** Let X = (log p)^{κ log 2}, Q(κ) := κ log κ − κ + 1 and g(κ) := κ log 2 − Q(κ) = κ(1 + log 2 − log κ) − 1.
1. For a line with φ(x) ≈ x = (log p)^{a}, ln 2 < a < 2 ln 2 (φ(x)/x ≥ c/log log x does not affect exponents), put κ_a = a/ln 2. The Poisson tail gives
   −log P(miss) ≈ E[1 − e^{−2^ω/x}] = (log p)^{−Q(κ_a)+o(1)}. This is dominated by ω ≈ κ_a λ (2^ω ≈ x); both
   P(ω ≥ κλ) and E[2^ω/x; ω < κλ] are (log p)^{−Q(κ)+o(1)} for 1 < κ < 2.
2. A dyadic block of such x contains ≍ x lines, so it costs (log p)^{a − Q(κ_a)+o(1)} = (log p)^{g(κ_a)+o(1)}.
3. g increases on [1, 2], with g(1) = log 2 and g(2) = 1. Lines with x < (log p)^{log 2} cost O(λ) each, i.e.
   O((log p)^{log 2} λ) in total.
4. Hence, in 𝔐,
   **−log P(HC(p) > (log p)^{κ log 2}) = (log p)^{g(κ)+o(1)} for 1 ≤ κ < 2.**
   For X = M(log p)^{2 log 2} with M large it is ≍ (log M)·log p: each further dyadic block costs ≍ E τ ≍ log p.
5. Numerical evaluation of the model sum for λ = 20, 40, 80, 160 converges to g. At κ = 1.2, 1.5, 1.8 the values
   log(cost)/λ = 0.804, 0.924, 0.990 at λ = 160 match g = 0.813, 0.932, 0.990 (script in §7).

**Consequences in 𝔐.**
* (i) For κ < 2, g(κ) < 1, so the primes p ≤ P with HC(p) > (log p)^{κ log 2} number P^{1−o(1)}. In particular, at
  κ = 1/log 2 (X = log p) g = 0.914, so **HC(p) > C log p for a set of primes of counting function P^{1−o(1)}, for every
  C**. LOWERTAIL_ROUND2_FABLE Conjecture 3.4 (HC ≤ C log p) is false in 𝔐.
* (ii) Borel–Cantelli at X = M(log p)^{2 log 2} with M large gives HC(p) ≤ M(log p)^{2 log 2} eventually. So
  limsup log HC(p)/log log p = 2 log 2 ≈ 1.386 in 𝔐.
* (iii) T is consistent with 𝔐 iff A > 2 log 2.
* (iv) **Dark range.** For log p/log log p ≪ X < (log p)^{2 log 2}, 𝔐 predicts HC > X infinitely often, but by
  Theorem W no Hypothesis-H family can exhibit it: the exceedances come from lightly-hit lines missing at random, not from
  congruence or primality structure.

**What 𝔐 says a proof of T must do (Assessment).**
* At the extremal primes, the window up to (log p)^{2 log 2} is lightly hit: typical window integers have
  τ ≈ (log p)^{log 2} ≪ φ(x).
* A firing line there comes from a window integer with τ ≳ φ(x), i.e. ω ≳ (2 − o(1)) log log p prime factors, mostly
  private, together with a divisor in the class −1 (mod x).
* So T at the extremes is a *single-p* statement that among (log p)^A shifted integers some has unusually many prime
  factors *and* a divisor in a tied class.
* Nothing in Remark 3.1 or Lemma C forces it. This is B2 (tied class at one integer) composed with a single-p
  large-deviation event, the kind of event that no sieve gives at a prescribed p (B6).

### 3.3 Robustness of the exponent (Assessment)

* Positive correlations (L2) only enlarge P(HC > X), so consequence (i) survives them.
* For (ii) one needs that no choice of p modulo small primes cuts the hit rate on *all* lines up to (log p)^{2 log 2+ε}
  by an unbounded factor. Two observations support this:
  * whatever p mod ℓ is (p ≢ 0), ℓ divides the same proportion 1/ℓ of the endpoint integers and of the level integers,
    so the window-averaged E τ is invariant;
  * the cheapest structured conspiracies change rates by bounded factors: p ≡ 1 (mod x) pairs the classes like a level
    line (factor 2), and square-mimicking p confines only the small-prime part of each N_x.
* Neither argument is a proof. 𝔐 is a heuristic for primes only: it ignores the character layer, so it would wrongly
  predict firing at odd squares, where Lemma C(d) confines every line.

## 4. Q3: numerics

**Samples** (`data/z53/hcshifts/samples_summary.txt`; 600 000 consecutive primes p ≡ 1 (8) from each 10^k, all lines in
𝒞 ∩ [4, 256], 45 s – 4 min each).

| start | P(HC>4) | P(HC>8) | P(HC>16) | max HC | private share of HC-cert. at HC ∈ [12,16] (y = 64²) | at HC = 8 (y = 64²) |
|---:|---:|---:|---:|---:|---:|---:|
| 10⁹ | 0.0734 | 1.65e-3 | 9.3e-5 | 31 | 5.5 % | 6.0 % |
| 10¹⁰ | 0.0666 | 1.19e-3 | 5.7e-5 | 32 | 9.0 % | 7.2 % |
| 10¹¹ | 0.0611 | 9.2e-4 | 3.8e-5 | 32 | 14.1 % | 10.2 % |
| 10¹² | 0.0565 | 7.5e-4 | 2.7e-5 | 23 | 15.9 % | 11.3 % |
| 10¹³ | 0.0523 | 6.0e-4 | 8.3e-6 | 23 | 16.7 % | 14.5 % |

* With the threshold y = x (the coordinate) instead of 64², the HC-certificate is private in ≈ 46 % of cases at HC = 4
  and in 100 % at HC = 8. The reason is that a divisor ≡ 7 (mod 8) of an integer whose 8-smooth part is a power of 2 must
  split the 8-rough part.
* The congruence-type share relative to the privacy threshold falls steadily with p at every HC ≥ 8. This is
  EVIDENCE for the kickoff hypothesis that **as p grows the HC-certificates come from private primes**, consistent with
  Prop W3 and 𝔐.

**Hard primes** (`hard_primes_hc.txt`, 166 primes):
* All 14 (★)-zeros have HC ∈ {4, 7, 8, 12, 31, 39}, with no failure; the maximum is 39 at 83 449 and 31 at 1 726 201.
* z49's HC ≥ 32 primes reproduce exactly.
* Prop 3.3(a) instances have HC = 15, 12, 15 (> 8 as designed). Prop 3.3(b) instances (X = 4) have HC = 12, 7, 7.
* The HC ≥ 20 primes from the samples have HC-certificates of both types.

**Why hard primes are hard** (`hard_primes_anatomy.txt`, `scripts/z53_hcshifts_hardanat.py`). The sample primes with
HC ≥ 20 (56, 23 and 5 primes at 10⁹, 10¹¹, 10¹³) were compared with 3 000 random primes of the same scale, over the lines
x ∈ 𝒞 ∩ [4, 20):

| quantity | HC ≥ 20 (10⁹ / 10¹¹ / 10¹³) | random (10⁹ / 10¹¹ / 10¹³) |
|---|---|---|
| mean log₂ τ(N) | 3.15 / 3.11 / 3.21 | 3.80 / 3.99 / 4.14 |
| model hit sum H = Σ (τ(N^e) + τ(N^l)/2)/φ(x) | 22 / 23 / 31 | 43 / 52 / 61 |
| #{ℓ ∈ {3,…,13} : p ≡ 1 (mod ℓ)} | 2.2–2.6 | 1.1 |
| #{ℓ ≤ 23 : (p/ℓ) = +1} | 6.8 of 8 | 4.0 |

So at accessible scales hardness is a mixture of two things:
* congruence structure: square-mimicking, the T1 deformation, and p ≡ 1 modulo small primes, which makes the smooth parts
  useless as in Prop W3;
* an anatomy deficit: about 0.7–0.9 fewer bits of τ per window integer, and half the expected hits (EVIDENCE).

§3.3 argues that only the anatomy part can grow with p.

**Controls** (`controls_squares_nearsquares.txt`):
* Odd squares m², m odd in [100 001, 110 000] (5 000 values): **no line in 𝒞 ∩ [4, 256] fires** (T1, CERTIFIED for this
  range).
* Near-squares p = m² + k (2 000 primes each, m ≥ 10⁵), P(HC > 4):
  * k = 9: 0.106, and k = 24: 0.063, against 0.067 for generic primes at 10¹⁰. The k = 9 deficit is the T1 deformation
    of (J)53/(J)55.
  * k = 1: 0.035, and k = 16: 0.048.
  * k = 8, 17: 0, because primality forces 3 | m, so p ≡ 2 (mod 3) and 3 | p + 4 (HC = 4). This is a congruence
    artifact.
  * The maximum is HC = 23 (k = 24).
* Prop W3 primes: HC = 4.

## 5. FRONTIER §4 hard screens for the lane's best statements

| statement | T1 squares | 8/131 | tied modulus | fixed p |
|---|---|---|---|---|
| Theorem W, Prop W2, W3 (kills/walls) | n/a: they are limits on kills; they hold at squares trivially | n/a; the argument is numerator-agnostic, which is harmless for a kill | they *are* statements that the tie cannot be broken by congruence/primality data below ≍ log p | yes (W3: specific primes) |
| Model 𝔐 / scale 2 log 2 | **fails** (ignores the character layer; it is a heuristic for primes, not a mechanism) | 4-specific through 𝒞 | **fails**: the class −1 mod x is tied to the coordinate; 𝔐 only prices it | heuristic at one p, calibrated on averages |
| Target T, A > 2 log 2 (CONJECTURE) | passes (false at squares, Lemma C(d)) | 4-specific | **fails**: B2 | yes |

Nothing passes line 4, as in every previous round.

## 6. Proposed FRONTIER §7.2 text (do not edit FRONTIER here)

> *(z53 HCSHIFTS, `Z53_HCSHIFTS.md`.)*
> * **Dickson/H kills of the one-coordinate target stop at X ≍ log p.**
>   * Any Hypothesis-H/Theorem-M family certifying "no line x ≤ X fires" fixes p mod every ℓ ≤ X/4, so log p > (1/4 + o(1))X
>     (Theorem W, PROVED).
>   * Under a non-standard uniform Bateman–Horn bound the Prop 3.3 family reaches HC > c log p/log log p (CONDITIONAL).
>   * H-type kills can never refute HC ≪ (log p)^A.
> * **Smooth-part (congruence-type) certificates die at X ≍ log p, unconditionally.** At infinitely many primes (Linnik;
>   X ≥ log p/10.4, GRH: log p/4), every certificate with coordinate ≤ X splits the X-rough part of its integer
>   (Prop W3). The certified instances all have HC = 4 via private certificates.
> * **Empirical laws (EVIDENCE, 10⁹–10¹³, 3·10⁶ primes).**
>   * Line x fires with probability 1 − exp(−c·τ(N)/φ(x)) (c = 1 endpoint, 1/2 level).
>   * Lines are independent given p mod 15015.
> * **Re-calibration (Assessment).** In the resulting independent-anatomy model the extremal HC is (log p)^{2 log 2+o(1)}:
>   P(HC > (log p)^{κ log 2}) = exp(−(log p)^{g(κ)}), g(κ) = κ(1 + log 2 − log κ) − 1 < 1 for κ < 2.
>   * Conjecture 3.4 (HC ≤ C log p) is predicted false; the model-consistent target is HC ≤ (log p)^A with A > 2 log 2.
>   * Between log p/log log p and (log p)^{2 log 2} lies a "dark range": exceedances are predicted there, but no H-type
>     family can certify them.
> * **What a proof needs (Assessment).** A single-p statement that some window integer has ≳ 2 log log p prime factors
>   *and* a divisor in the tied class. All forced window structure is congruence data (PROVED remarks), and T1's
>   confinement is blocked only on unconfinable lines, which still miss by anatomy deficit.

**Bottom line.**
* The kickoff's key observation is correct, and it is now a theorem. Hypothesis-H/Dickson kills need p fixed modulo every
  prime up to X/4, so they cannot reach X ≥ (4 + ε) log p, and under the Bateman–Horn heuristic they reach only
  log p/log log p.
* The observation is *not* a source of hope for the polylog target. The anatomy model (fire law, conditional
  independence, Poisson ω) predicts that HC exceeds (log p)^{1.38} infinitely often anyway, through lines that are merely
  lightly hit.
* So the right target is HC ≤ (log p)^A with A > 2 log 2, and the old C log p conjecture should be retired.
* Smooth-part certificates are provably insufficient at X ≍ log p (Linnik). Every forced structure of the shifted family
  is congruence data.
* What remains is a large-deviation-plus-tied-class event among the private primes of one shifted integer: B2 at a single
  p, with no new handle. **Verdict: narrowed.**

## 7. Reproduction

```sh
ulimit -v 2000000
gcc -O2 -o /tmp/z53hc scripts/z53_hcshifts_hc.c
for e in 9 10 11 12 13; do timeout 1700 /tmp/z53hc range 1$(printf '0%.0s' $(seq 1 $e)) 600000 256 4096 > samp_1e$e.txt; done   # 1-4 min each
for e in 9 11 13; do timeout 1700 /tmp/z53hc lines 1$(printf '0%.0s' $(seq 1 $e)) 200000 256 > data/z53/hcshifts/lines_1e$e.txt; done
python3 scripts/z53_hcshifts_summary.py samp samp_1e*.txt  > data/z53/hcshifts/samples_summary.txt
python3 scripts/z53_hcshifts_summary.py lines data/z53/hcshifts/lines_1e*.txt > data/z53/hcshifts/fire_law.txt
uv run python scripts/z53_hcshifts_indep.py samp_1e9.txt samp_1e11.txt samp_1e13.txt   # (L2) raw
uv run python scripts/z53_hcshifts_strat.py samp_1e9.txt samp_1e13.txt                 # (L2) stratified, ~15 min
python3 scripts/z53_hcshifts_confine.py samp_1e9.txt samp_1e13.txt                     # Lemma C data
timeout 600 /tmp/z53hc list 256 4096 < data/z53/hcshifts/hard_primes_list.txt > data/z53/hcshifts/hard_primes_hc.txt
uv run --with sympy python scripts/z53_hcshifts_wall.py                                # Theorem W forced-prime table
uv run --with cypari2 python scripts/z53_hcshifts_linnik.py                            # Prop W3 instances (exit 0)
python3 scripts/z53_hcshifts_model.py                                                  # model exponent g(kappa)
uv run --with cypari2 python scripts/z53_hcshifts_hardanat.py samp_1e9.txt samp_1e11.txt samp_1e13.txt  # hard-prime anatomy
```
Squares/near-squares controls: `scripts/z53_hcshifts_controls.sh`. The raw samples (≈ 240 MB) are not committed; they are
regenerated by the first loop (deterministic).
