# Project: explicit-k correlation bounds → Erdős–Straus exceptional set

Successor session to the campaign logged in `notes.md` (read it first, §3, §6,
§8.3, §11 are the load-bearing sections; `verify.py` re-checks every
computational companion claim in about 55 s). Goal: execute the one actionable
lever found there.

## The target

Prove an exceptional-set bound for the Erdős–Straus conjecture of the form

    #{p ≤ N prime : 4/p has no representation} ≪ N·exp(−c(log N)^θ)

by the criterion route (notes.md Thm 3.1), with the explicit ambition θ > 2/3
(beating Vaughan 1970) and the realistic fallback of any exp-type saving
derived independently of Vaughan's method.

## The plan (phases; each is standalone publishable-progress if it works)

**Phase 1 — explicit-k mean-value bounds for indicator slices (rigorous
target).** The stackable conditions: for each modulus w ≡ 3 (mod 4) and each
of the two criterion halves, a counterexample p forces the shifted value
((p+w)/4 resp. (pw+1)/4) to have NO prime factor in specified residue classes
mod w (the −1 and −x classes, when distinct; for w = 3 and some Case-B
classes they coincide; see notes §8.3, §11.3). These necessary slices are
multiplicative 0/1-indicator conditions on k
coprime linear forms in p. Needed: a k-fold Shiu/Nair–Tenenbaum-type upper
bound with constant C(k) explicit and subexponential in k. Key simplification
vs the general machinery (sources/henriot-1102.1643.pdf, which states
Nair–Tenenbaum Thm 1 and Holowinsky Thm 2): our functions are 0/1 indicators,
f(p^ℓ) ≤ 1, product structure across forms — the full M_k(A,B,ε) generality
is not needed and a direct sieve/Halász-style argument may give good
k-dependence cheaply. Warning from notes §11.3: prime moduli alone contribute
∑ 2/(w−1) ≈ log log W. Section 12's completed direct sieve also admits all
composite w≡3 (mod 4), raising the cumulative density to ≫log W and proving
the unconditional bound N·exp(−c(log log N)²). This remains superlogarithmic,
not a positive power of log N, so it cannot reach θ = 2/3.

**Phase 2 — capture the full per-modulus condition (the prize).** Full failure
at modulus w is subset-product avoidance: no product of prime factors of x
(exponents ≤ 2eᵢ) lands in the coset −x (mod w). Empirically this fails with
probability ≈ 0.3–0.7 per modulus, roughly independently across moduli and
halves (measured: notes §11.1), for w up to the divisor-richness threshold
≈ (log p)^{1.1}. Task: prove per-modulus failure probability ≤ ρ < 1 *on
average over p* for w ≤ (log N)^{1−ε}, e.g. via large-deviation/moment
control of the vector of class-counts of prime factors of the shifted values
(multidimensional Selberg–Delange / Halász), then stack with Phase-1-style
explicit-k control. Success here gives θ near 1 — beating Vaughan.

**Phase 3 — write-up.** Compare against Vaughan 1970's actual argument
(obtain the paper); be scrupulous about what is genuinely new. House rules:
no overclaiming — "verified numerically" ≠ "proved"; every analytic step
either proved or cited to a checked source; extend `verify.py` with numerical
sanity checks for each new lemma (e.g. simulate Phase-2 class-count
large-deviations against actual data for hard-class primes).

## Assets

* `notes.md` — full campaign: criterion (Thm 3.1, proved), obstruction
  theorems (5.1, 9.3), reciprocity collapse (8.1/9.1), one-bit completeness
  (§10.2), independence data + joint record (§11.1), calibration (§11.3).
* `verify.py` — about-55-second re-verification of all computational
  companion claims.
* `sources/henriot-1102.1643.pdf` — Henriot, NT bounds uniform in
  discriminant (quotes NT Thm 1, Holowinsky Thm 2 — the pair-case tools).
* `sources/bright-loughran-1908.02526.pdf` — geometry side (context only).
* `sources/nair-tenenbaum-1998.pdf`, `sources/shiu-1980.pdf` — originals.
* `sources/pomerance-weingartner-2025.pdf` — a modern proof explicitly following
  Vaughan's inaccessible 1970 paper; §4 gives the large-sieve argument.
* Still wanted: Vaughan 1970 itself (publisher page found; PDF access blocked).

## Known traps (paid for already, don't re-pay)

* The full failure condition is NOT a multiplicative indicator. Conditioning
  on p mod 4w fixes the target coset but does **not** make subset-product
  avoidance multiplicative (e.g. modulo 7, target −1: 8 and 15 each avoid it,
  while 120 does not). Only the necessary prime-class slices are multiplicative.
* Prime and near-prime x are provably useless (notes §8.3) — smoothness/many-
  factor x carry everything; don't waste effort on sparse-divisor slices.
* Identity/covering/form shortcuts are dead by theorem (notes §5, §9.3);
  don't rediscover them.
* GRH and Schinzel H do not shortcut Phase 2 (notes §10.5).

## Outcome 16 (2026-08-29, wave 12 — see notes.md §36–§38; all three hostile-reviewed: repairable → repaired)

* **§36 (mass-formula route): the exact ray-character mass for Type I —
  proved — and why it is not a positive class-number mass.**  Theorem 36.1:
  \(T_I(p)\) is exactly a finite Dirichlet-character projection of the
  divisor masses of \(p^2+4ck^2\) over the complete finite \((c,k)\) box,
  equivalently the integral-point count on the split quadrics
  \(r^2=ck(cks^2-ps-k)\); the primitive count carries an explicit Möbius
  weight and **equals Elsholtz–Tao's \(f_I(p)\)** (exact dictionary
  (36.17)–(36.21) to their \(\Sigma^I_p\) variety; their
  \(f=3f_I+3f_{II}\) and square-vanishing sanity checks pass).  Theorem
  36.2: the \(c=1\) Gaussian slice (discriminant \(-16\), class number
  one) **vanishes identically on every \(p\equiv1\ (4)\)** — unique
  factorisation exposes a wrong-grade obstruction (every divisor is
  \(1\bmod4\), the required grade is \(3\bmod4\)), not a positive mass.
  Theorem 36.3: exact \(k=1\) character formula; its unique zero among the
  143 hard primes \(<10^4\) is 2521.  Hurwitz–Kronecker restorations fail
  at explicit finite tests (the classical mass is weighted and unprojected;
  the moving ray projector mod \(4ck\) is precisely what it forgets;
  \(1534\ne830\) at \((73,10,1)\)).  Positivity of the exact formula for
  all hard \(p\) would BE Type-I Erdős–Straus; no cancellation estimate
  capable of that is obtained — the deliverable is the exact structure
  theorem plus a precise account of the missing projector.  New sources
  mined: Elsholtz–Tao 1107.1010 (full), Yamamoto 1965 (OCR), Salez
  1406.6307, Elsholtz–Planitzer 1805.02945.
* **§37 (Lemma 33.3 minorant assault): the prime half transfers; the
  composite half is ONE precisely-stated moment bound away.**  Lemma 37.1
  (residue-set transfer, proved): the finite-window transfer works for
  class-SET terms with the corrected ledger \(\sum|c_\alpha|\rho(U_\alpha)\)
  (the \(\rho\)-factor is essential).  Theorem 37.2 (proved): the two-level
  tensor-plus-odd-Bonferroni minorant realizes the complete prime-modulus
  subsystem at degree \(O(L^2)\) — an accounting formulation of Theorem
  24.4's bound after quarantine, not an improvement.  Proposition 37.3
  (proved): a single conditional factorial-moment bound
  \(\mathbb E(H)_m\le(C\Lambda)^m\) at \(m\asymp\Lambda=L^3/\log L\) would
  give the full pointwise minorant and prove (33.16), i.e. refute
  \(H_{\rm PF}'\).  The proposed \(D=1\) common-prime star cliques are
  proved harmless (37.22); the exact missing input is isolated as a
  **residue-dispersion bound** (37.27):
  \(\sum_pp\sum_au_{p,a}^2=O(\Lambda^2)\) — the §31 charges control only
  \(\ell^1\) incidence and lose a factor \(\log L\) at the pair audit.
  Scott–Sokal cluster expansions proved non-pointwise (path-\(P_5\)
  counterexample).  \(H_{\rm PF}'\) remains OPEN.
* **§38 (fixed-value action hunt): a complete value-fixing law, and the
  door stays shut.**  Theorem 38.1 (proved): necessary-and-sufficient
  Diophantine conditions for the three §30 additive maps to fix either
  input's value; copied-coordinate maps can never fix their first input;
  behind the 2137 example lies a common law.  Every value-fixing edge
  preserves \(R=CK\), so fixed-value fibre graphs split into
  \(R\)-sheets: **none of the 76 hard-prime fibres through 5000 is
  connected** (complete 188,374-tuple census).  Sparse-rational fixed-value
  self-maps: only identity and swap survive an exact 2,996,352-ratio box
  (both types); Type-I scaling (38.17) is a nonprimitive reparametrization.
  No bounded \(k=2\to k=1\) coordinate law exists through \(P<10^5\)
  (universal conversion already refuted by 409).  All structures are
  conditional on fibre nonemptiness; the P4 descent slot is unchanged; no
  proof of Erdős–Straus results.

## Outcome 15 (2026-08-25, wave 11 — see notes.md §33–§35; §34 extra-severity-reviewed (pruned theorem confirmed) → all repaired)

* **§33 (critical-window transfer): H_PF′ still OPEN; the transfer routes
  are now walled with theorems.**  Any all-avoider congruence-class-union
  certificate needs \(\log Q\ge(\tfrac12+o(1))X\) (every prime
  \(\ell\equiv3\ (4)\), \(\ell\le X\) must divide \(Q\); strengthened in
  review: every residual atom is implied by a prime-modulus atom); the
  avoider indicator is provably NOT a tensor product over prime-power
  coordinates (exact \(X=15\) counterexample); charges-as-densities
  beta-sieve dies at an \(\exp(-\Theta(L^3))\) Euler product.  The one
  viable route is isolated (Lemma 33.3): a pointwise low-degree hypergraph
  minorant with controlled coefficient sum would transfer the §31 LLL
  density into the window; constructing it is open.
* **§34 (H_kBV assault): a pruned prime-slice theorem, proved
  unconditionally.**  For every fixed \(\kappa<1/240\), \(K=X^\kappa\):
  after removing triples with more than \((\log X)^4\) compatible
  multipliers (negligible mass by a new second-incidence-moment bound),
  ordinary Bombieri–Vinogradov applies and the full \((\log X)^3\)
  prime-slice class mass is realized — the first movement on this wall
  since §16; extra-severity review confirmed both author-flagged steps.
  Literal H_kBV stays open but is no longer needed: the dependency graph
  simplifies to ONE hypothesis — a restricted critical-window assembly
  (now formally stated in §34) — for the \(3/4\) exponent.  No
  unconditional \(E(N)\) gain (the lcm partition still forces
  \(K\ll\log N\); sharp \(\log L_K\sim2K/3\)).  Kloosterman completion
  loses \(2K^9\): documented dead end.
* **§35 (blind independent-method attack; anti-anchoring protocol).**
  Three-plus fresh angles (bounded-residue factor criteria, Type-II
  shifted factors at \(a=1\), conic/Pell, Type-I \(a=1\) slice) — all
  reconciled against the ten waves: no new mechanism escapes the wall
  (method-independence evidence).  New data: every hard prime below
  \(10^7\) has an \(a=1\) Type-I witness (82,887 primes; independently
  re-verified in review); exactly 193, 2521, 66529 fail the Type-II
  \(a=1\) slice below \(10^6\).

## Outcome 14 (2026-08-24, wave 10 — see notes.md §31–§32; §31 maximum-severity-reviewed (refutation confirmed) → repaired; §32 reviewed → repaired)

* **§31 (rough shifted-divisor assembly): H_PF as stated is REFUTED; the
  critical-window variant H_PF′ remains OPEN.**  Theorems 31.2–31.3 prove
  the weighted rough mean and softened pointwise charges; the finite-CRT
  Lovász-local-lemma argument gives
  \(\delta_X\geq\exp\{-O(L^3\log\log L/\log L)\}=\exp\{-o(L^3)\}\).  Exact
  complete-period multiples then contradict H_PF's claimed
  \(\exp(-cL^3)\) majorant mean.  This refutes H_PF's literal
  all-eligible-\(N\) quantifiers, not the restriction to
  \(\log N\asymp L^4\): H_PF′ is not refuted, would still imply Theorem
  18.6's conclusion, and the corresponding finite-window lower bound
  remains open.  (The maximum-severity review verified the borderline
  Henriot coefficient condition at the split point, the LLL
  factorization/independence structure, and the quarantine arithmetic.)
  Supersession pointers added at every stale H_PF status line in
  §§18/21/24/27.  Route audit: Hall moments, Nair–Tenenbaum on the void
  indicator, Suen, and smooth-restricted families each fail at a named
  step; the wall now lives entirely in the finite-window transfer.
* **§32 (k=1 certification audit): the intrinsic system does NOT certify
  k=1.**  The intrinsic-class witness's canonical multiplier is
  \(k=H/(H,D)\), \(H=(M+1)/4\); a same-class k=1 witness exists exactly
  when \(4D\mid H\) (class-level statement; scoped after review).  The
  k=1-certifying affine system within the fixed-divisor dictionary is
  \(\{-t\bmod M:t\mid H\}\), with all-modulus mass
  \(\tfrac18(\log X)^2+O(\log X)\) but prime-modulus mass only
  \(\asymp\log X\).  **New unconditional theorem:**
  \(\#\{P\le N\text{ prime}:P\ne4ABC-A-B\}\ll N\exp(-c\sqrt{\log N})\)
  (also for integer targets) — the honest exponent is \(1/2\), and
  \(2/3\) is blocked by a precisely-stated non-pairwise-coprime modulus
  assembly obstruction.  Anatomy of the nine k=1-less primes \(<10^6\):
  minimal Type-II \(k=2\) for eight, \(k=3\) for 102001; every one has
  Type-I tuples; **no Type-I-less odd prime exists through \(10^5\)**
  (Computational).

## Outcome 13 (2026-08-24, wave 9 — see notes.md §28–§30; all three hostile-reviewed → repaired)

* **§28 (census reconciliation): the combined blocked set is EMPTY through
  \(10^6\) — as witness decomposition.**  §25's additive maps and §26's
  census had run in parallel; under §23.4's uniform standard (descending
  inverse, self-certifying smaller sources) the additive branches close the
  five §26 holdouts, so every hard prime \(\le10^6\) that has a Type-II
  tuple decomposes through smaller sources (143/143, 1181/1181,
  9732/9732).  Existence remains the conjecture; the register is kept
  strict throughout.  Tuple-level atoms (34 of 940 rows at \(P\le3000\),
  coordinate-1 boundary) are law-family-relative and all fall to §30's
  moves.  Complete k=1-less census to \(10^6\): exactly nine primes
  409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321 (decade
  counts 0/2, 2/12, 2/129, 2/1038, 3/8551 — thinning, Measured).
  Residual conjecture H_W9 (forward-image totality of the four fixed
  predicates) stated verbatim and honestly assessed: stronger than raw
  witness existence, not a hardness reduction.
* **§29 (supply audit): the transfer laws do NOT enlarge the sieve supply
  beyond cubic.**  Theorem-level subsumption: the fixed-\((c,k)\) Case-B
  prime-divisor classes are exactly the §16 multiplier classes (verified
  symbolically and on all \(q\le3000\)).  The Type-I prime-divisor layer
  has a genuinely new class SHAPE (CRT of quadratic roots mod \(q\) with
  the coupling \(q\equiv-P\) mod \(4ck\); no coverage gain demonstrated)
  and total mass \(O((\log X)^2\log\log X)\) — subcubic.  The audited
  combined supply stays \(\asymp(\log X)^3\); Theorem 16.4 and the
  conditional 3/4 ceiling are unchanged.  Composite Type-I divisors and
  joint image counting remain open scope notes.
* **§30 (structure theorem): the full positive Type-II tuple lattice is
  one decorated additive orbit.**  Seven move schemas (unary generation
  form after review) generate every tuple from the single seed
  \((1,1,1,1)\); independent re-enumeration through 5000 reproduces the
  audit (zero non-seed atoms).  Exact reformulation: [ES\(_{II}\) for
  hard primes] \(\Leftrightarrow\) every hard prime's value fibre meets
  the orbit.  Technology audit: Markoff/Apollonian machinery lacks its
  prerequisite here (no fixed-value non-elementary action; moves change
  value; the canonical excursion through value \(KP\) is nonminimal and
  unbounded in \(K\)).  Honest verdict: a reformulation and a complete
  decomposition structure, not a solution; Type-I side not covered.

## Outcome 12 (2026-08-24, wave 8 — see notes.md §25–§27; all three hostile-reviewed: repairable → repaired)

* **§25 (sub-maximal maps): the eleven pure-tensor resisters all fall to
  fixed additive maps — as witness decomposition, not witness existence.**
  Shifted degree-two maps at modulus \(h_1\) (finite \(\pm1..\pm3\)
  coefficient box, exact inverse) reach 1153, 2473, 3361, 5281.  Theorem
  25.6: three fixed degree-ONE additive maps at modulus \(g\) decompose
  EVERY \(k=1\) Type-II tuple \((A,B,C,1)\ne(1,1,C,1)\) into two explicit
  smaller-value source tuples — all eleven resisters are decomposition
  images (Corollary 25.6.1, finite audit).  This is how non-pure maps shed
  the tensor's 2-adic weight: addition at modulus \(g\) instead of
  multiplication at \(v_2\ge4\).  Assessment 25.7 (honest ceiling): the
  proposed finite-family non-cofiniteness theorem is NOT established — the
  three fixed maps' image already contains every hard prime with a
  \(k=1\) tuple, and inverting any tuple presupposes the witness; **the
  entire transfer axis so far is witness decomposition; witness existence
  (forward totality from scratch) remains the conjecture.**  Census
  (exact, ES_FULL_SCAN-replayable): all 9,732 hard primes \(<10^6\) —
  pure-tensor descending inverses for 9,721; the pure-tensor resister set
  stays exactly the eleven of (23.14); no new resisters in
  \([10^5,10^6]\).
* **§26 (Type-I transfer theory — first of its kind).**  Foundations: the
  Type-I divisor form \((4ack-p)(4bck-p)=p^2+4ck^2\) with exact
  gcd bookkeeping and a PROVED finite enumeration of all Type-I tuples per
  \(p\) (no experimental cutoffs; stress-tested against brute force).
  Brahmagupta composition of the norms exists but lands in the wrong
  divisor grade (\(+P\) vs \(-P\) mod \(4c\) — the §20.2 sign obstruction's
  mirror; degenerate \(K_\sigma=0\) handled after review).  Theorem 26.4
  (corrected binary Type-I tensor, same \(m\)): \(A=a_1a_2\),
  \(B=(a_1+b_1)(a_2+b_2)-A\), \(C=mt-4c_1c_2\), \(K=k_1k_2m\),
  \(P=(4ABC-1)/m\) — with exact finite inverse test; reaches 2473, 3169,
  5281 with prime sources.  Theorem 26.5 (same-tuple cross-type bridge):
  \(Q=m(p-1)+1\), strict descent for \(m>1\); reaches 673, 1153, 3361,
  5281.  **Combined two-type reachability \(\le10^4\): 138/143; exact
  blocked set \(\{73,193,241,1129,2521\}\)** — all five have explicit
  tuples of both types; blocked = not an image of the present laws;
  forward-image totality is false for the present laws (later: see Outcome 13).
* **§27 (large-\(R\) conditioning): near-cubic fiber cutoff.**  Theorem 24.8's
  certificate hybridized with the prime-modulus slice extends joint
  avoidance to every fiber \(R\le Y\) with
  \(Y=L^3/(\log\log X)^{2+\eta}\), at cost
  \(\exp[-O(H_Y\log\log X+L^2)]\), \(H_Y=\sum_{R\le Y}2^{\omega(R)}\)
  (proved; probability spaces separated after review).  The remaining wall
  is named exactly: the weighted rough-modulus broad-cofactor clustering
  estimate (27.17) + a finite-interval cluster-expansion transfer;
  the elementary LLL charge diverges.  H_DC (falsifiable divisor-clustering
  hypothesis) formulated; H_DC \(\Rightarrow\) H_PF false.  New exact
  X=6400 sample (2.4e9 draws, reproducible C++ sampler + raw chunks
  checked in): survivor rate 1.14e-7, Wilson [1.01,1.29]e-7; the
  \(L^2\log L\) fit still dominates the subset benchmark.  **H_PF: still
  false-looking, open.**

## Outcome 11 (2026-08-24, wave 7 — see notes.md §23–§24; both hostile-reviewed: repairable → repaired)

* **§23 (flexible tensor reinterpretation): all six §22 blockers fall; the
  family is still not total.**  Theorem 23.1: moving factors between the
  output coordinates — any \(K'\mid A+B\) with \(K'\mid4c_1c_2k_1k_2\),
  \(C'=4c_1c_2k_1k_2/K'\) — gives \(P'=(k_1k_2/K')(16c_1c_2AB-s_1s_2)\), a
  valid Type-II tuple (descent no longer automatic: Warning 23.2's 71<75
  example; every inverse branch checks \(2\le p_i<P\) directly).  Lemma 23.3:
  exact finite inverse test (necessity \(4\mid CK\), replacing §22's
  \(4\mid C\)).  Census (23.9)/(23.12), independently reproduced in review:
  577, 5569, 83449 all have \(4\mid CK\) tuples and descending inverses
  (mostly from fixed source 2); 1170 of the 1181 hard primes \(<10^5\) are
  images with descending inverses; **eleven resisters**
  (73, 193, 241, 673, 1129, 1153, 2473, 2521, 3169, 3361, 5281) have **no
  tuple with \(4\mid CK\)** (parity criterion Lemma 23.6:
  \(v_2(C)+v_2(A+B)\le1\) on every tuple row).  Closure theorems: Lemma 23.7
  (product modulus, any tensor order), Lemma 23.8 (lcm/\(h_1h_2/g^2\)
  quotient readings, odd outputs), and Lemma 23.9 (review round:
  \(H\gcd(A,B)=4C''K''\gcd(A'',B'')\) for **arbitrary**-modulus readings of
  pure tensor factor pairs + finite odd-gcd audit) — **no pure tensor of any
  order at any modulus reaches any resister tuple**.  The circularity trap
  (inverting a known tuple presupposes \(P\in S\)) is documented; the
  theorem to hunt is forward-image totality.  Unclassified: non-pure
  (additive modulus-dependent) corrections (later: see Outcome 12 for a fixed
  additive family), rational maps.
* **§24 (H_PF lower-bound routes): prime slice pinned, truncated fibers
  proved, refutation reduced.**  Lemma 24.3: full prime-modulus intrinsic
  mass \(\asymp(\log X)^2\).  Theorem 24.4: two-sided
  \(|{\rm Av}^{\rm prime}_X(N)|=N\exp[-\Theta((\log X)^2)]\) for
  \(\log N\ge C(\log X)^3\) (CRT density + odd-Bonferroni transfer) — any
  cubic H_PF majorant must lean entirely on composite moduli.  Lemma 24.5:
  the \(D=1\) cluster exactly \(\asymp L^{-1/2}\).  Theorem 24.8
  (multi-shift prime-class certificate): joint avoidance of ALL intrinsic
  fibers \(R\le Y\) at cost \(\exp[-C_\epsilon Y\log(2Y)\log L]\), valid to
  \(Y=L^{3-\epsilon}\) — subcubic joint clustering for a genuinely
  composite-modulus subsystem.  Theorem 24.7 (scoped no-go):
  initial-cutoff Jacobi certificates + unconditioned first moment cannot
  refute H_PF (smooth moduli carry negligible mass, Lemma 24.6 — proof
  repaired in review: correctly-ranged CEP smooth bound via monotone
  enlargement).  Assessment 24.1: the uniform subset-product model outputs
  benchmark \(L^{2+\log2}\) but overpredicts sampled hits ~3x even after
  eligibility filters.  **H_PF: still false-looking, open**; refutation now
  = a large-\(R\) multi-shift divisor-clustering lower bound.

## Outcome 10 (2026-08-24, wave 6 — see notes.md §21–§22; reviewed: §21 sound, §22 repaired)

* **§21 (the truth of H_PF): false-looking, open.**  Exact reorganization of
  the complete-system avoidance into shifted-divisor events (n + 4D free of
  divisors ≡ −1 mod 4R₀(D) up to X); proved: every intrinsic class has
  Jacobi symbol −1 (mirror of Prop 8.1), hence **every perfect square
  avoids the complete intrinsic system** — the square-class phenomenon
  reappearing at the sieve-hypothesis level; unconditional upper bound
  |Av| ≪ N exp(−c(log X)²) for log N ≫ (log X)³; measured avoidance
  through X = 3200 fits (log X)² loglog X far better than (log X)³ (RMS
  0.046 vs 0.169).  If the refutation completes, Theorem 18.6's conditional 3/4
  route dies and Theorem 16.4 is near the intrinsic supply's true ceiling.
* **§22 (degree-two transfer-map classification): new maps found.**
  Complete classification of universal factor-congruence polynomial maps at
  degree ≤ 2 (and univariate degree ≤ 3); discovery of the
  **tensor-partition family** (C = 4c₁c₂, K = k₁k₂, P = 4ABC − (A+B)/K
  over partitions of {a₁a₂, a₁b₂, b₁a₂, b₁b₂}) — genuinely outside §20's
  explicit formulas, with strictly-lowering inverses on their image;
  reaches 409, 9601, 23929 from smaller solved primes; 577, 5569, 83449
  proved unreachable under the natural K' | k₁k₂ interpretations (no
  witness with 4 | C — exhaustive via AB ≤ p/2 bound); no total inverse,
  no induction, no proof.  Scope disclaimers: rational maps, quotient/lcm
  moduli, modulus-dependent coefficients unclassified (later partial
  classifications: see Outcomes 11–12).

## Outcome 9 (2026-08-23, frontal assault — see notes.md §20; hostile-reviewed: repairable → repaired)

* **A direct proof attempt at the full conjecture, transfer slot first.  No
  proof resulted; genuinely new algebra did.**  Proved: the fixed-(c,k)
  composition monoid u∘v = u+v+Luv with witness absorption (N(u∘v) =
  N(u)N(v)); the divisor-set product law Δ_h(n₁n₂) = Δ_h(n₁)Δ_h(n₂) (even
  non-coprime) making the witnessed set an ideal of {n ≡ 1 (mod L)}; the
  sign-grading obstruction (exact binary Gauss-style composition lands in
  +1, the wrong class; ternary works); the minimal corrected binary law and
  its collapse into affine grids; exact and corrected cross-slice
  composition with real hard-prime transfers — witnesses of 3 and 59
  compose to one for the hard prime 2617, and 3, 41 → 7873; Theorem 20.4:
  the complete fixed-slice solution set is exactly k bilinear grids
  (reduced-seed classification); the Euclidean divisor-reduction identity;
  the off-diagonal supply lemma with its synchronization proved equivalent
  to the residual problem (not a weaker lemma).  Theorem 20.3: finite
  transfer seeds can never cover cofinitely (residue-1 escape).  Explicit
  monoid atoms (p = 313) block reverse composition.  All algorithmic
  descents (reverse composition, affine reduction, Euclid/LLL,
  least-counterexample) documented with exact failure points.  §20.5: the
  transfer door is colder — the one unclosed subslot is a non-monomial
  cross-modulus correspondence outside all classified maps, with no warm
  candidate and a stated (not yet well-posed) classification direction
  (later: see Outcomes 10–12).

## Outcome 8 (2026-08-23, the pointwise campaign — see notes.md §17–§19)

* **The full-conjecture ("all p") frontier is now mapped to closure.**  Three
  parallel swings, all merged and verified:
* **§17 (pointwise frontier; hostile-reviewed, rewritten once).**
  Theorem 17.1: complete four-parameter parametrization of both solution
  types (kp = 4abck−a−b for Type II, p(a+b) = k(4abc−1) for Type I,
  valuation-argument bijections), with the divisor dictionary — Case B ⟺
  some 4pck²+1 has a divisor ≡ −1 (mod 4ck) (coprimality subtlety at fixed
  (c,k) documented with the p = 29 regression).  Lemma 17.2: the quadratic
  layer is **pointwise inert** — λ_p = +1 identically on both witness
  families, so no global parity contradiction can ever bite an exceptional
  p.  Theorem 17.3 (**square-class escape**): the residue 1 (mod M) lies in
  no forced class of any formalized shape (a)–(e) — with self-contained
  proofs for the three moving-parameter shapes: the Lemma-16.1 class set
  𝓡(M) never contains 1 (a 4-line size argument), and the Case-A and
  Case-B moving-c families ((a,b,m) and (a,b,k)) avoid 1; corollary:
  bounded-modulus identity systems are escapable by actual primes forever.
  §17.4 (**entropy wall**, honest split): Lemma 17.4.1 (box-coverage mass
  ≥ s−1, worst case), Lemma 17.4.2 (the all-ones configuration forces
  pinned-target certificates into q | p+4 congruence families — dead by
  17.3), Assessment 17.4.3 (sub-exponential-window oblivious certificates
  are confined to congruence reach or unproved strong forcing onto sparse
  λ-special moduli — the earlier "no certificate system" theorem-claim is
  withdrawn), Lemma 17.4.4 (Mahler measure of the exponent box = 0 exactly;
  corrected reading: average-case equidistribution holds in the model, the
  pointwise problem is carried entirely by worst-case configurations).
  §17.5: technology audit (Duke positivity, Linnik repulsion, GRH-Chebotarev
  — compositum-limited to exp(−(loglog p)²) density, matching Thm 12.2;
  Chen-type sieves vs polylog mass; EGZ coverage) — each an assessment with
  the missing structural prerequisite identified.  §17.6: exact residual
  problem (unbounded Thm 3.1) vs the natural polylog sufficient target,
  and the P1–P4 feature list for proofs within the divisor-coset frame
  (explicitly not a classification of all conceivable proofs).  §17.7
  (descent audit): the three audited minimal-counterexample routes yield no known purchase —
  Lemma 17.7.1 completely classifies the valuation shapes at p² (descending
  shape; (2,0,0) with p²|4X−1; (2,1,0) with p|4X−1, realized by
  4/9 = 1/9 + 1/12 + 1/4; the (a,a,0) family, a ≥ 2, with v_p(X+Y) = a−2;
  all else impossible — mixed shapes carry wrong-window data), the induction
  hypothesis is window-irrelevant, and lattice transfers stay inside
  harvested classes; the three obvious routes yield no known transfer
  (cleverer transfers remain unexcluded — the open P4 slot; later: see Outcomes 9–13).
* **§18 (full-harvest ceiling).**  Lemma 18.1: the Lemma-16.1 classes mod M
  are exactly {−4D : D | A²}, A = (M+1)/4.  Theorem 18.2: total identity
  supply is **exactly cubic** — Σ F(M)/M ≍ (log Q)³ — so B = 3 and θ = 3/4
  is the absolute ceiling of the identity-sieve axis; **that axis can never
  prove ES outright**.  The realized §16 mass is capped by two named walls:
  summed-BV multiplicity (H_kBV) and composite-modulus Selberg assembly
  (H_PF); Theorem 18.6: under H_PF, E_all(N) ≤ N exp(−c(log N)^{3/4})
  (CONDITIONAL, nonstandard hypothesis, stated falsifiably — after review,
  H_PF is quantified over the COMPLETE intrinsic system only: the reviewer's
  sparse-subfamily counterexample (D=1 classes with 3|M leave density-2/3
  avoiders) is recorded in the hypothesis's scope warning).  Ordinary EH
  does not substitute.  No unconditional improvement of Theorem 16.4.
* **§19 (computational frontier to 10¹⁰).**  All 719,781 primes ≡ 1 (mod 24)
  below 10⁸: interleaved witness records only (73,3),(241,7),(2521,15),
  (21169,31),(118801,59); extension §19.4 scanned the further 56,156,819
  primes to 10¹⁰: exactly one new record, w*(2,927,257,369) = 71, then flat
  — w* ≤ 71 through 10¹⁰ (vs log 10¹⁰ ≈ 23); growth data cannot yet
  discriminate c·log p from log-powers.  F3 microscopy (§19.4): box-failures
  are deficit-1-dominated with no largest-factor rule, strongly
  squarefree-enriched and lower-ω than successes (ω alone does not separate
  F3 from F1).  Failure
  taxonomy: 99.23% Jacobi (F1), the rest exponent-box (F3), non-Jacobi
  subgroup misses essentially absent (one case) — record primes enrich F3 to
  22%.  Type-II dictionary verified on all 36,384 stored witnesses (zero
  decomposition failures); six primes < 10⁵ (409, 577, 5569, 9601, 23929,
  83449) need k ≥ 2 (later: see Outcome 13 for the extended census).
* **Honest verdict:** the conjecture is true-with-room on all evidence, the
  exceptional set is provisionally below Vaughan, and a full proof requires
  technology (pointwise-uniform divisor equidistribution in moving cosets, or
  a prime-to-prime transfer structure) that currently does not exist
  (later: see Outcomes 9–13) — with
  the reasons now theorem-level precise rather than folklore.

## Outcome 7 (2026-08-23, multiplier classes — see notes.md §16)

* **CLAIMED/PROVISIONAL Vaughan-beating bounds.**  This record claim is
  subject to external verification and priority search; Vaughan's primary
  paper (1970) remains access-blocked and was checked only through the
  Pomerance-Weingartner 2025 reconstruction.  The generalized identity for
  \(A_k=(k\ell+1)/4=uvw\) forces the class
  \(n\equiv-uv^{-1}\pmod{k\ell}\).  Lemma 16.3 proves, by a
  Bombieri--Vinogradov divisor-sum argument with honest cross-\(k\)
  deduplication, class mass \(\asymp(\log X)^2h(\mathcal J)\) pointwise in
  every compatible subsequence.  The full multiplier family has
  \(h\asymp\log K\), giving for prime exceptions
  \(E(N)\ll N\exp[-c(\log N)^{2/3}(\log\log N)^{1/3}]\) (Theorem 16.4).
* **All-denominator scope.**  Every prime factor of an exceptional integer is
  exceptional.  Rankin's inequality for that multiplicative semigroup lifts
  Theorem 16.4 at full strength: Theorem 16.5 gives
  \(E_{\rm all}(N)\ll N\exp[-c(\log N)^{2/3}
  (\log\log N)^{1/3}]\).  The prime and all-integer statements have the same
  scale, but remain separate statements.  `verify.py (o)` checks 7,684 exact
  identities (including composite/even inputs), an informational toy average
  with the actual floor and \(\omega\)-cutoff over primes and reduced classes,
  and within/across-multiplier distinctness.

## Outcome 6 (2026-08-22, declustering door — see notes.md §15)

* **An independent reconstruction matches the Vaughan/PW class count.**  For
  ℓ ≡ 3 (mod 4), a=(ℓ+1)/4, each squarefree T|a and split d₁d₂=a/T,
  d₁<d₂, gives D=Td₁² and r=ℓ−4D.  With g=(d₁,d₂), u=d₁/g,
  v=d₂/g, w=Tg², every n=r+jℓ has s=v−u+jv and q=j+1, with the
  exact identity 4/n=1/(suw)+1/(nsvw)+1/(nuvw).  It needs no mod-4
  condition and covers composite/even n.  The count f(ℓ)=(τ(a²)−1)/2
  matches PW (4.1) and locates the B=2 supply in the divisors of a².  PW
  state the count but do not print this identity; Vaughan's paper was
  inaccessible, so this is not claimed as verification of his parametrization.
* **The measured fixed-multiple route adds nothing in its tested scope; the
  full door remains unclear.**  Testing all 27,452 nonzero residues for the
  eight primes ℓ=103,…,13799, 40 values of n≡1 (mod 4) each, and exactly
  k≤20 leaves one candidate per ℓ for q=kℓ or m=kℓ: r=−4.  No k-shift
  gain was measured.  The corrected scan now requires both reconstructed
  denominators to be integral for composite n; the earlier relaxed check was
  conservative and the full rerun was unchanged.  This is evidence only for
  those eight primes, that k-range, and the all-n hard-slice notion—not a
  theorem for arbitrary ℓ or k.  The varying q in the reconstructed family
  shows only that its explicit witnesses are not fixed-q; alternative fixed-q
  witnesses can cover the same class (as r=−4 does).  Thus the scan is not
  guaranteed to upper-envelope all ℓ-local families.  No B>2 family was found
  (later: see Outcome 7).  `phase0_full.py` records the experiment; `verify.py (n)` replays it and
  checks the ℓ=103,199 closed forms.
## Outcome 5 (2026-08-19, phase nine — see notes.md §14.6)

* **New campaign record: E(N) ≪ N exp(−(log N)^{θ_*−o(1)}),
  θ_* = log 3/(1+log 3) = 0.5234946419… (Theorem 14.9), unconditional
  and Siegel–Walfisz-ineffective.**  For every fixed σ > 0 the proved
  bound is N exp(−c(σ)(log N)^{θ_*−σ}log log N).  The
  restricted-support problem has an exact Boolean solution: Möbius
  inversion makes the unrestricted quadratic minimum equal the true
  witness-miss probability, despite the support not being divisor-closed.
  After a cardinality cap L = O(log h), Rankin tails are polynomially
  small; Boolean differences give the marked bound
  C^|M|h^O(1)∏_{q∈M}q^−1; the floor u absorbs that fixed h-power in the
  §14.3 exclusion assembly.  Taking window mass λ = ρ log h for any
  fixed ρ > 1/log 3 costs h^ρ times logarithms; the rounding budget gives
  every exponent below 1/(1+ρ), and ρ ↓ 1/log 3 gives θ_*.
* **The proposed subset lemma at λ = (1+ε)log h is false for small ε.**
  With K ∼ Poisson(λ), a typical subset alphabet has only 2^K products;
  if ε < 1/log 2−1, a union bound plus Poisson concentration gives miss
  probability 1−h^−c, and the exact-minimum identity means no weights can
  repair it.  The **signed** alphabet closes the application: Lemma 12.5
  plus Poisson concentration gives miss O(h^−c) whenever
  λ ≥ ρ log h with fixed ρ > 1/log 3 for unit groups; a direct
  Bernoulli–Poisson coupling and Siegel–Walfisz transfer
  this to arithmetic windows.  `verify.py (m1)` labels its exact Möbius
  check subset-only; `(m2)` adds signed reachability (including inverse
  transitions) and informational iid-Poisson tables centered at 1/log 3,
  contrasted with the subset threshold 1/log 2.
* **Corrected framework ceiling:** signed entropy requires
  K ≥ (log h)/log 3, so this window-and-rounding architecture has supremum
  θ_*, not 1/2.  Every fixed exponent below θ_* is proved; the endpoint
  is not.  Vaughan's 2/3 remains stronger than the stacking family
  (but see Outcome 7 for the claimed/provisional improvement by the
  multiplier-class route), and all constants remain
  ineffective because of Siegel–Walfisz.  The §14.5 declustering door
  remains the named route past Vaughan.

## Outcome 4 (2026-08-18, phase eight — see notes.md §14)

* **New campaign record: E(N) ≪ N exp(−(log N)^{2/5−o(1)}) (Theorem
  14.4), unconditional (SW-ineffective).**  θ = 2/5 vs the previous 1/8;
  Vaughan's 2/3 still stands.  Mechanism — the H3 stacking problem
  dissolved by two structural moves: (1) count exceptional primes inside
  ∑_{m≡1 (24), m≤N} Λ(m)² over the *integers* (Λ = ∏_w(1−θ_wU_w) = 1 on
  every criterion failure; the tilt is truncated *in the definition*,
  so the expansion is finite and congruence counts are exact to O(1) —
  no BV error floor); (2) all witness primes sit above a floor u > W,
  so no prime can serve two shifted forms (m+w)/4, (m+w′)/4: shared-
  prime terms are *incompatible* (count zero), compatible terms factor
  by CRT, and the exclusion corrections are second-order with
  identically vanishing principal parts (marked-sum bound), total
  O(W²/u) = o(1).  Per-modulus factors: signed (n²-divisor, c = 3)
  witnesses tilted at 3^{−ω}, telescoping Euler factors, δ_w ≤ h^{−ϑ};
  ∏ over w ≤ W = (log N)^{2/5−ϑ} gives the exponent (windows sized
  K_w ≈ h^{3(1+ϑ)/2}, total level (log N)^{1−ϑ/4}).  `verify.py (l)`:
  signed local-factor identities exact; exclusivity of shared primes
  confirmed on data (joint count 0 vs model N/q²);
  joint/marginal-product = 0.9992 (second-order-only correlations);
  exact solutions from signed witnesses.
* **Framework ceiling corrected (§14.4–14.5, assessments with named
  model assumptions):** phase eight's restricted-weight forecast of 1/2
  was false.  Signed witness entropy only forces window level
  h_w^{1/log 3+o(1)} per modulus, so Outcome 5 reaches every fixed
  θ < log 3/(1+log 3); within these assumptions **it still does not reach
  2/3**.  Prime-side stacking by
  progression evaluations is impossible (BV polylog floor vs
  exponential main terms).  Vaughan's 2/3
  = B/(B+1), B = 2 class-mass (log X)², verified tight in PW's own
  proof; total solution mass is (log p)³ but clusters log p per class.
  **The one visible door past 2/3: declustering — (log ℓ)^{2+δ}
  distinct forced classes per prime ℓ.**  Hybrids pay CS-halving and do
  not add exponents (later: see Outcome 7).

## Outcome 3 (2026-08-18, phase seven — see notes.md §13.5)

* **H1′/H2′ PROVED (window form): the single-modulus transfer is
  complete.**  With the prime window W = (z₀, z], z₀ = exp((log N)^{ε/2}),
  z = exp((log N)^{1−ε/2}), and witnesses restricted to squarefree
  W-smooth divisors d ≡ −1 (mod w) of n = (p+w)/4, the tilted moments
  hold with (1 + O((log N)^{−ε/2})) precision uniformly for w ≡ 3 (4),
  w ≤ (log N)^{1/2−ε} (Lemmas 13.9–13.10).  No Selberg–Delange machinery
  survives in the proof: the θ = 1/2 tilt telescopes every principal
  Euler factor to exactly 1; the inputs are Siegel–Walfisz for window
  character sums (the floor z₀ deletes the L(1,χ)-biased small primes
  that otherwise wall the method at w ≈ (log N)^{3/8} even with the
  enlarged window top, and at ≈ (log N)^{3/16} for the literal H1′
  window — an honest proof-level obstruction, documented), Bombieri–Vinogradov at level N^{3/8} with
  τ-bounded multiplicities, and Rankin tails.  **Theorem 13.11:**
  per-modulus criterion failure probability O((log N)^{−ε/2}), uniformly
  to w ≤ (log N)^{1/2−ε} — the successor-unit deliverable, past every
  §13.3 ceiling at single-modulus level.  Constants ineffective (SW).
  `verify.py (k)`: factorization spot-checks (toy window, defect
  < 1e-12), uncapped-moment model tracking + PZ inequality on real data
  (informational — the cap is untestable at toy scale), and exact
  solution reconstruction from window witnesses (machine-checked
  sufficiency chain).
* **Honest ledger:** a single modulus improves no E(N) bound (one w gives
  only N(log N)^{−1−ε/2}).  Open inputs now: (H3) the w-joint version
  for stacking (later: see Outcome 4) — with it this window route yields every θ < 1/2, not
  θ < 1 (the 2^{−ω} tilt's range cap h ≤ e^{(1/2−ε)λ} is structural);
  and the signed/n²-divisor variant (3^{−ω} tilt, Lemma 12.5's pair
  combinatorics as Euler factors), model range w ≤ (log N)^{2/3−ε},
  plausibly window-transferable — θ = 2/3, Vaughan-equal, still not
  beating 2/3.  Beating 2/3 still needs conditioning beyond fixed-order
  tilts.

## Outcome 2 (2026-08-18, phase six — see notes.md §13)

* **Positive power achieved unconditionally (fallback prize):**
  E(N) ≤ N exp(−(log N)^{1/8}) for large N (Theorem 13.2).  Method:
  Lemma 12.4's Fourier bound discretized into hard level-set factor-count
  thresholds (Lemma 13.1), conditioned on exceptional factor patterns, and
  fed to the many-root sieve with an explicit Poisson–Chernoff/character
  union cost; a finite rate certificate (verify.py (h)) closes the
  arithmetic.  Criterion-native, keeps primality, independent of Vaughan’s
  construction — but still **weaker than Vaughan’s 2/3**; not a record.
* **Ceilings computed (§13.3):** the fully optimized version of this route
  caps at θ < γ* ≈ 0.207 (numerical estimate); any route through the first-moment pigeonhole
  (12.11) caps at θ < log 3/2 ≈ 0.549; Vaughan’s outer argument caps at
  θ = A/(A+1) with A = 2 the divisor-density of identity classes, i.e. 2/3.
  Beating 2/3 therefore needs the second-moment transfer, not more of this.
* **Unconditioned halves of the gap now proved (§13.4, Lemmas 13.3–13.5,
  Cor 13.6):** Pólya–Vinogradov character-average lemma; first-moment
  asymptotic li(N)·c_w·(log N)/h for divisor witnesses along the actual
  shifted primes (Bombieri–Vinogradov, level N^{1/4}); second-moment upper
  bound N(log N)²/h² (Brun–Titchmarsh); hence success ≫ li(N)/log N per
  modulus, uniformly for w ≤ (log N)^{1−ε}.  The lost 1/log N is exactly
  divisor over-dispersion — the ω-conditioning is the sole remaining
  analytic input.
* **Gap sharpened twice (§13.4):** first from growing-order marked
  Sathe–Selberg to ω-conditioned fixed-order hypotheses H1/H2/H3; then —
  via **Lemma 13.7 (proved)**, the θ = 1/2 tilted subset-product second
  moment — the conditioning itself is removed in the model: P(T = 0) =
  o(1) for h ≤ e^{(1/2−ε)λ} with only first/second tilted moments.  The
  remaining open inputs are H1'/H2' (tilted divisor moments along the
  shifted primes: Selberg–Delange × BV hybrids, fixed-order, Rankin-
  controlled tails, τ-bounded BV multiplicities — no k! wall, no
  over-dispersion wall) uniformly for w ≤ (log N)^{1/2−ε}, plus the
  w-joint H3 for stacking (later: see Outcome 4).  Proving H1'/H2' is the
  successor unit (later: see Outcome 3); the naive-route obstructions (k!-vs-BV; unconditioned over-dispersion,
  now quantified by Cor 13.6) are documented.

## Outcome (2026-08-17)

* **Phase 1 completed:** Lemma 12.1 is a direct many-root large sieve with
  absolute constant 4 and no hidden k-dependence. Applied to both criterion
  halves, all moduli w≡3 (mod 4) up to δ log N (prime and composite), and the
  prime affine form itself, it independently proves
  E(N)≪N exp(−c(log log N)²) (Theorem 12.2). The method is criterion-native;
  the bound is weaker than Vaughan's known theorem and is not a literature
  record.
* **Phase 2 reduced but not solved:** Lemmas 12.3–12.4 give the exact signed
  subset-product and Fourier large-deviation formulations; Lemma 12.5 proves
  success with probability 1−o(1) in the independent uniform-residue model
  throughout w≤(log N)^{1−ε}. The missing input is a growing-order,
  residue-marked factor-count theorem along a prime affine form. No uniform
  contraction ρ<1 for the actual shifted values, and hence no positive θ, was
  proved (later: see Outcomes 2–3).
* **Phase 3 corrected:** Vaughan uses many sufficient residue classes per
  auxiliary prime plus the large sieve and a Rankin tail, not growing-k shifted
  correlations. Pomerance–Weingartner §4 is the checked modern reconstruction;
  Vaughan's primary PDF remained access-blocked.
