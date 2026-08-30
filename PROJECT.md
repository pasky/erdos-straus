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

## Outcome 33 (2026-08-30, wave 29 — see notes.md §69 + paper v15; max-severity refutation-class review → repaired / FAITHFUL)

* **§69: the ALL-RAYS polynomial obstruction — the §66 forward-ray gap is
  CLOSED (SOUND-AFTER-REPAIRS; refutation-class protocol).**  Theorem
  69.4: NO polynomial witness family (M(t), D(t)) exists on any anchored
  class m(t) = m₀ + Kt of the three sporadic families — for every
  degree, every period K, every eventual-validity start t₀, both
  divisibility regimes (polynomial cofactor AND pointwise integer-wise).
  Mechanism: Lemma 69.1 (integer-wise polynomial divisibility forces an
  integer-VALUED polynomial quotient — Newton/binomial basis — with
  constant resultant residual; the t(t+1)/2-type subtlety handled),
  Lemma 69.3 (backward propagation via real-zero analysis: at every real
  zero of M the eligibility chain forces D < 0 there, and at every zero
  of D it forces M = −1 — so the constraints CANNOT die between t = 1
  and t = 0; review added the explicit t₀ > 1 tail induction on shifted
  parameterizations, anchor fixed), then the congruence at t = 0 hits
  W(288/336/4545) = +∞.  Hunt exhaustions independently replayed
  (bound-5000: 5,792,112 candidates, zero hits; 65-class projection:
  1,709 divisor rows, zero).  Consequence, honestly scoped: combined
  with §66's certificate ceiling, the anchored cylinders are
  undecidable by finite harvested laws AND by polynomial witness
  families of every shape — any resolution of C_SQ′ on the twisted
  families requires non-polynomial structure.  Scope strict: polynomial
  families only; NOT evidence for C_SQ′.  Verify (bp) 0.6s/2.1s deep.
* **paper v15 (145pp, FAITHFUL-AFTER-REPAIRS):** §66–§68 absorbed as
  Sections 28–30 (verbatim PW Theorem 1.1–1.4 quotes restored in
  review; Layer-1 range made explicit); v16 queue = §69.

## Outcome 32 (2026-08-30, wave 28 — see notes.md §66–§68 + paper v14; all max-severity-reviewed → repaired / FAITHFUL)

* **§66: twisted-family escape cylinders (SOUND-AFTER-MINOR-REPAIRS;
  censuses + hunt independently replayed).**  Proved: {m : W(sm²) ≤ T}
  is a union of residue classes mod L(T) = lcm{M ≡ 3 (4), M ≤ T}, with
  **log L(T) = (2/3 + o(1))T** (review re-derived: 1/2 from 3-mod-4
  primes + 1/6 from 1-mod-4 primes through T/3); since W(2·12²) = ∞,
  the whole class m ≡ 12 (mod L(T)) escapes depth T — so
  **limsup_m W(2m²) = +∞** (density ≥ 1/L(T)); same for 21m² (anchor
  4) and 505m² (anchor 3).  Corollary: family-level certificate ceiling
  — no finite set of harvested congruence laws decides C_SQ′ even on
  {2m²}; any classification proof must be non-covering.  **Anchored
  polynomial-identity obstruction (proved):** no polynomial witness
  family (any degree) covers a class through the anchor — the congruence
  transfers to t = 0 against W(288) = ∞; forward rays honestly scoped as
  NOT obstructed (positivity/eligibility need not extend backward —
  review repair).  54,990-candidate hunt: zero identities.  Censuses to
  m ≤ 2000 (caps stated): only the three anchors unresolved; maxima
  W(2·1530²) = 4019, W(21·851²) = 695, W(505·1239²) = 479.  Verify
  (bm).
* **§67: record-stall anatomy (SOUND-AFTER-REPAIRS).**  All top-10
  census primes pass the D=1 purity gate (p+4 free of 3-mod-4 primes);
  exhaustive purity depth does NOT rank W (2031121 has depth 28, others
  1–14; τ repaired to an integer supremum allowing +∞; τ(193) = ∞).
  Residue-one empirics (T, p, W, W−T): (15, 4324321, 23, 8),
  (19, 232792561, 183, 164), (23, 10708457761, 47, 24),
  (27, 401567166001, 71, 44) — the §54.1 guarantee W > T is loose at
  T = 19.  Heuristic record-spacing (toy, all inputs displayed,
  explicitly no-evidence): expected #{W > 2495} ≈ 0.017 in (10⁷, 10⁸)
  — observed 0 is unremarkable — and ≈ 0.15 in (10⁸, 10⁹).
  A_emp(2031121) = 2.9232; the honest frontier restated: **A < 1
  refuted, every A ≥ 1 open** (PROJECT.md's old '[1, ~2] window'
  wording repaired — review — to finite-normalization gloss only).
  Verify (bn).
* **§68: external — the 2025 Pomerance–Weingartner exceptions paper
  (arXiv:2511.16817v2; confirmed-after-repairs, source-bounded).**
  Discovery: our sources/pomerance-weingartner-2025.pdf IS v1 of this
  paper (arXiv regenerated; numbering unchanged).  v2 archived with
  SHA-256 + provenance; full reading audit in reviews/.  Their results:
  Schinzel exceptions n_m ≥ exp(m^{1/3+o(1)}); explicit prime
  exceptions p ∈ (m², 2m²) for m ≥ 6.52×10⁹ (conjecturally m ≥ 20);
  explicit-in-m Vaughan bound at exactly the 2/3 exponent for
  4 ≤ m ≤ log²N.  **Priority verdicts: no threat to Theorems 39.7,
  43.12, 51.2/51.6** (no m = 4 bound beyond 2/3, no effectivity, no
  witness-modulus statistic, no Dahan citation); crossover algebra
  (68.6) re-derived; consistency: their exception regimes lie outside
  §43/§55's stated ranges (review repaired one overbroad '§55' blanket
  — the asymptotic regime can enter §55 at fixed B > 3 but both tail
  masses vanish; no contradiction).  Two adjacent refs newly registered
  (Gottschlich, Nakayama) — no priority impact.  Vaughan 1970: five
  accurate secondary descriptions extracted (method + statement);
  access log updated (HathiTrust/zbMATH checked — no full text).
  Verify (bo).
* **paper v14 (133pp, FAITHFUL-AFTER-REPAIRS):** §63–§65 absorbed as
  Sections 25–27 (sporadic ledger triples restored, box-scope caveat
  added in review); v15 queue = §66–§68.

## Outcome 31 (2026-08-30, wave 27 — see notes.md §63–§65 + paper v13; all max-severity-reviewed → repaired / FAITHFUL)

* **§63: the algebraic-witness taxonomy in the dual frame
  (SOUND-AFTER-REPAIRS; census independently replicated).**  Proved: the
  DIV family (any divisor \(e\mid h\), \(e\equiv-1\pmod a\) ⇒ witness
  \(D=h/e\)); the D1 family (\(a\mid p+4\iff h\equiv-1\pmod a\); both
  \(D=1\) and \(D=h^2\) fire, \(M=(p+4)/a\)); the **square-root law**:
  if \(p+4\) has ANY prime factor \(\equiv3\pmod4\) then
  \(W(p)\leq\sqrt{p+4}\) (both parts of the factorization pair are
  \(\equiv3\pmod4\); take \(a\) = the larger); the fixed-\(D\) dual laws
  \(D=1..4\) (exact classes incl. 2-adic branches); the **universal
  \(a\)-law** (success at any odd \(a\iff\) a bounded-coefficient
  CRT-coupled integer feasibility — the same \(f_q\) feeds every
  component; the six §62 laws are instances); effective
  \(\ll N/(\log N)^{3/2}\) bound for the exceptional set (half-dimensional
  sieve, no prime level-of-distribution input — review expanded the proof
  with exact CRT remainders).  Honest register: change of coordinates on
  Lemma-16.1 supply, weaker than §51's tails on both axes; its value is
  elementarity + effectivity + EXPLICIT exceptional characterization
  (\(p+4\) purely \(1\bmod4\)) — exactly the four §62.22 record primes'
  signature.  New statistic \(a_1(p)\) (first witnessing \(a\)): census
  9,732 hard primes \(\leq10^6\) (max \(a_1=63\) at 87,481), research
  \(10^7\) (82,887 primes, max \(a_1=107\) at 8,803,369 — whose
  \(W=139\) sits at \(a_W=63{,}335\): first-witness and minimal-\(W\)
  coordinates separate at scale; \(a_W>a_1\) on every census row).
  Verify (bj) ~2.4s; reviewer reimplemented the full \(10^6\) census +
  200-prime research sample from scratch, zero disagreements.
* **§64: the gcd mechanism structurally mapped; the sporadic hunt
  enlarged 2.7× (SOUND-AFTER-REPAIRS; hunt independently fully
  replayed).**  Proved: the cancellation-cover theorem (eligibility
  fails exactly at primes in the window
  \(2v_q(A)<v_q(D)\leq2v_q(a)+2v_q(A)\), all dividing \((a,D)\mid n\) —
  so for prime \(p\) the mechanism is void, re-deriving Corollary 61.5
  structurally); the cancellation-immune \(D=1,2\) shifted laws for ALL
  \(n\) (any admissible factorization \(n+4=aM\) witnesses regardless of
  gcd — \(W(n)=+\infty\) forces \(n+4\) divisor-purity); dyadic and
  twisted-square family exclusions; the composite unit-branch ratio law
  (odd \((a,n)=1\) branches behave exactly like primes).  Complete
  failure-prime ledgers for 288/336/4545 (all quotient rows die at primes
  dividing \(n\)).  **Enlarged hunt: 242,837 NEW pairs (squarefree
  \(s\leq2000\), \(m\leq600\), \(n=sm^2\in(10^6,10^8]\); 388,853 total
  with the old box), ZERO survivors at \(M\leq10^4\); max
  \(W(3{,}201{,}660)=5303\) at \(15\cdot462^2\); thin \(10^8<n\leq10^9\)
  slice (4,992 pts) zero survivors** — reviewer re-ran the ENTIRE
  new-region scan independently (6.09s), exact match.  \(C_{\rm SQ}'\)
  survives a 2.7×-wider stress; still only \(\supseteq\) proved;
  finiteness of the sporadic set remains open (honest Assessment of
  obstacles recorded).  Verify (bk) ~1s.
* **§65: the two-decade census — \(W\)-records STOP at \(10^{6.3}\)
  (SOUND-AFTER-REPAIRS; independent from-scratch full replay
  committed).**  Complete exact census of all **719,781 hard primes
  \(p<10^8\)**: the record list is 15 pairs ending at
  \((2{,}031{,}121,\ 2495)\) — **no new record in \((10^7,10^8)\)**; the
  suprema \(W/\log p=171.78\) and \(W/(\log p\log\log p)=64.20\) both
  still sit at \(p=2031121\) and DECLINE for two decades after it
  (INFO-only; no growth law claimed; \(H_{\rm MOD}\) untouched).
  Even-\(D\) minimal-witness prevalence persists (60.293% at \(10^7\) vs
  60.618% at \(3\cdot10^5\)); the §63 square-root prediction has zero
  violations (all three applicable records have \(p+4\) purely
  \(1\bmod4\)).  Review found the research scanner had not been
  committed (HIGH) and committed its own full-replay
  `scripts/review65_independent.py` (1.39s, Python-int divisor paths) —
  the headline now rests on the committed independent implementation.
  Verify (bl) ~0.03s default.
* **paper v13 (118pp, FAITHFUL, zero defects):** §62 absorbed as Section
  24 (all six laws, tables digit-checked, mechanism register with its
  honesty clause, staged-hunt box scope); v14 queue = §63–§65.
* **Ops lesson (norm update):** a truncated merge-output pipe hid a
  notes.md conflict line and three merge-conflict sentinels got
  committed; all three section reviewers caught them independently.  New
  mandatory step: `grep -c '<<<<<<<\|>>>>>>>'` on notes.md AND verify.py
  AND espaper.tex after EVERY merge, before commit.

## Outcome 30 (2026-08-30, wave 26 — see notes.md §62 + paper v12; max-severity-reviewed → repaired / FAITHFUL)

* **§62: the divisor-ratio spectrum — the terminal distillation of the
  Type-II pointwise problem (SOUND-AFTER-REPAIRS; every law
  independently re-derived).**  Theorem (spectrum law): for prime \(p\),
  admissible \(a\): \(\{Dh^{-1}\bmod a:D\mid h^2\}=\{\prod_{q\mid
  h}q^{f_q}:|f_q|\leq v_q(h)\}\), so \(p\) is witnessed at \(a\iff-1\
  ({\rm mod}\ a)\) is a bounded-exponent product of \(h\)'s primes,
  \(h=(p+a)/4\).  **Explicit per-\(a\) laws proved for a =
  3,7,11,15,19,23** (subgroup/coset + CRT; reviewer re-derived all six
  and checked every unit \(h\leq10^5\) — zero disagreements; failure
  counts recorded).  **Multiplicity-budget phenomenon (new, verified):**
  \(a=7,h=17\): \(\langle3\rangle=(\mathbb Z/7)^*\ni-1\), yet \(-1=3^3\)
  needs exponent 3 \(>\) budget 1 — subgroup membership ≠ spectrum
  membership; the budget is real.  Late-record anatomy (recomputed
  independently): first-witness vs minimal-\(W\) data separate — e.g.
  \(p=2031121\) first succeeds at \(a=11\) (\(M=185279\)) while
  \(W=2495\) comes from \(a=815\).  Finite-conspiracy display: a prime
  failure needs EVERY admissible \(a\leq2B\) to fail its law — the
  trichotomy (squares: character; sporadics: gcd; primes: neither
  available) + Heuristic joint-failure mass with dependence caveat.
  **Fourth-sporadic hunt: all 146{,}016 nonsquare twisted squares
  \(sm^2\in(10^6,10^8]\) in the box \(s\leq1000\), \(m\leq300\) resolve
  by \(M\leq10^4\)** (max \(W(9028800)=3359\); box-subset framing
  repaired in review; 2{,}000 seeded independent replays) — C_SQ\'
  strengthened, still only \(\supseteq\) proved.  Verify (bi) ~7s.
* **paper v12 (112pp, FAITHFUL-AFTER-MINOR-REPAIR):** §61 absorbed
  (Section 23; census pedigree, residue laws, prime criterion,
  trichotomy; 3630-entry codebook condensed to histogram + displayed
  SHA-256 digest); v13 queue = §62.

## Outcome 29 (2026-08-30, wave 25 — see notes.md §61 + paper v11; max-severity-reviewed → repaired / FAITHFUL)

* **§61: the decidable census, the twisted-square laws, and the prime
  criterion (SOUND-AFTER-REPAIRS; independently replicated).**
  **Complete census: through \(10^6\), the \(W=+\infty\) set is EXACTLY
  1{,}000 squares + \{288, 336, 4545\}** (default-committed 200{,}000;
  reviewer's independent original-harvest replay: all \(n\leq5000\),
  2{,}500 seeded random samples, and the full optional million — zero
  disagreements) — C_SQ\' (squares ∪ the three sporadics) SURVIVES its
  millionfold stress test; only \(\supseteq\) is proved.  Twisted-square
  box (squarefree \(s\leq200\), \(m\leq30\); 3{,}630 entries replayed):
  only \((2,12)\) and \((21,4)\) vanish ((505,3) outside the box);
  proved exact residue laws for \(2m^2\) subfamilies (\(W=3\iff3\nmid
  m\); \(W=11\)/\(W=19\) classes with explicit root sets and
  smaller-\(M\) exclusions — all re-derived in review).  **The prime
  criterion (proved equivalence, replayed on all 3{,}202 hard primes
  \(\leq3\cdot10^5\) including even-\(D\) minima):** for
  \(p\equiv1\ (24)\), \(W(p)<\infty\iff\exists a\equiv3\ (4)\),
  \(a\leq2\lfloor(p+1)/3\rfloor\), with some \(D\mid h^2\),
  \(D\equiv-h\ ({\rm mod}\ a)\), \(h=(p+a)/4\) — gcd-eligibility
  automatic for primes; the sporadics' failure mechanism (gcd) and the
  squares' (character) are BOTH structurally unavailable to primes; a
  prime failure would need a third, unstructured mechanism (every
  divisor of every \(h^2\) in wrong classes mod \(a\) simultaneously) —
  the cleanest finite form of the hard core the campaign has reached.
  No claim that primes cannot fail; register kept.  Verify (bh) ~12s +
  reviewer's all-prime cross-check.
* **paper v11 (106pp, FAITHFUL-AFTER-REPAIRS):** §60 absorbed (Section
  22; C_SQ-supersession sweep complete — no stale live-C_SQ wording;
  Theorem 60.3 kept explicitly computer-assisted with the
  independent-reimplementation pedigree); v12 queue = §61.

## Outcome 28 (2026-08-30, wave 24 — see notes.md §60; hostile-reviewed → SOUND-AFTER-REPAIRS)

* **§60: finite witness duality closes the survivor frontier.**  Every
  harvested datum has the canonical form
  \(A=gu,h=gv,D=gd\), \((u,v)=1\), \(d\mid g\),
  \(a=4gv-n\geq1\), \(au=d+v\).  With
  \(B=\lfloor(n+1)/3\rfloor\), this proves the unconditional bounds
  \(a,u\leq2B\) and \(M\leq8B^2-1\), without any invalid \(a\leftrightarrow
  M\) swap.  Exact Python-integer exhaustion, independently replayed from
  the original \(D\mid((M+1)/4)^2\) harvest at ceilings 73,727, 100,351,
  and 18,361,799, proves
  **\(W(288)=W(336)=W(4545)=+\infty\)**.  Thus historical `C_SQ` is
  **REFUTED** and superseded by the open, falsifiable `C_SQ'` asserting
  squares plus exactly these three sporadics.  This concerns only the
  Lemma-16.1 witness statistic: all three composites have ordinary explicit
  Egyptian-fraction representations and are not Erdős--Straus
  counterexamples.  The repaired conjecture would still imply
  Erdős--Straus because its entire exceptional set is composite (or 1).
  Verify block `(bg)` is green; the wave-24 attestation records the independent
  409,000,770-incidence largest-ceiling replay and all cancellation/symmetry
  checks.
* **Paper status:** paper v10 predates §60 and still presents the wave-23
  `C_SQ`/survivor state historically.  `paper/README.md` now flags those
  passages as superseded pending source §60 absorption; no paper theorem has
  silently been updated.
* **Wave-25 lead (from §60's near-miss diagnosis):** the three sporadics
  fail eligibility through shared-factor structure (\(\gcd(a,D)>1\),
  possible only because \(\gcd(a,D)\mid n\)); for an odd PRIME \(p\) the
  normal form forces \(a<p\), hence \(\gcd(a,D)=1\) always — the sporadic
  failure mechanism is structurally unavailable to primes, and the
  per-prime witness question is a clean finite divisor condition
  (\(O(p(\log p)^2)\)-average scan).  Open: full \(W=\infty\) census
  via decidability (more sporadics? all twisted squares?), the
  twisted-square vanishing law, and what the prime/composite asymmetry
  yields for the pointwise frontier.

## Outcome 27 (2026-08-30, wave 23 — historical state superseded by Outcome 28; see notes.md §59 + paper v9; hostile-reviewed → repaired / FAITHFUL)

* **§59: the polynomial escape classification (SOUND-AFTER-REPAIRS).**
  Exact local criterion (uniform escape ⟺ every harvested congruence
  \(f(x)\equiv-4D\ ({\rm mod}\ M)\) unsolvable); **degrees 1–2 complete:
  no linear uniform escape exists, and quadratic uniform escapes are
  EXACTLY the squares \(g(x)^2\)** (D=1-layer character/discriminant
  arithmetic + higher-\(D\) pinning); general degree: a cyclotomic
  root-field obstruction (Chebotarev, ineffective, labeled) — full
  classification open as named conjecture C_POLY.  Prime-value corollary:
  classified escapes are square-valued, hence contain no primes — the
  polynomial-family route cannot produce \(W=\infty\) primes (scope:
  polynomial families only).  Proposition: the ALL-INTEGER supercritical
  tail fails beyond \(\theta=1/3\) exactly (\(\sqrt N\) squares vs a
  below-one prediction) — the wave-18 prime-restriction of Theorem 51.2
  was necessary, not cosmetic.  **C_SQ named (falsifiable): the
  \(W=+\infty\) set is exactly the squares; C_SQ ⇒ E-S for all primes
  (strictly stronger).**  Census stress test: three nonsquare survivors
  **288 = 2·12², 336 = 21·4², 4545 = 505·3² remain unwitnessed past
  \(M=1.5\cdot10^8\)** (review deep scan, 2.9G divisor values; an
  int32-overflow artifact that briefly 'resolved' them was caught and
  quarantined — the false values are explicitly rejected in the text);
  review derived the exact twisted-square reduction (hits require
  \((s/M)=-1\), \(s\nmid D\); per-survivor: 288 → odd \(D\),
  \(M\equiv3\ (8)\); 336 → \(21\nmid D\), \((M/3)(M/7)=-1\); 4545 →
  \(505\nmid D\), \((M/5)(M/101)=-1\)); family controls: 177/180 members
  of \(2m^2/21m^2/505m^2\) resolve by \(M\leq131\) — the three are
  sporadic individuals, not family escapes (consistent with the
  classification).  No \(W=\infty\) proof landed; C_SQ live with three
  explicit stress candidates.  Verify (bf): criterion replays, family
  tables, committed Python-int survivor scan (int32 overflow lesson
  baked into the block).
* **paper v9 (91pp, FAITHFUL-AFTER-REPAIRS):** §57–§58 absorbed as
  paper §§19–20 (conditional-reduction thresholds, mass-invariant gap
  with antecedent citations restored in review, square-escape full
  repaired proof, censuses digit-checked, liminf duality); §59 = v10
  queue.
* **Next-wave lead (derived in-session, unformalized):** writing a
  witness as \(aM=4D+n\) gives \(16a^2A^2=(a(M+1))^2\equiv(n+a)^2\ ({\rm
  mod}\ D)\), so for odd \(D\): \(D\mid A^2\iff D\mid(n+a)^2\) — an
  exact \(a\)-parameterized duality turning the survivor question into
  divisor-class structure of \((n+a)^2\); wave-24 target.

## Outcome 26 (2026-08-30, wave 22 — see notes.md §57–§58 + paper v8; all hostile-reviewed → repaired / FAITHFUL)

* **§57: the supercritical window — the count-below-one reduction, the
  mass-invariant gap, and the crossing localization (SOUND-AFTER-REPAIRS).**
  Theorem 57.1 (proved conditional): the named falsifiable window
  hypotheses — \(H_{\rm WIN}(\theta)\) (cubic tail
  \(N\exp\{-c(\log T)^3\}\) valid to \(T=\exp\{(\log N)^\theta\}\)) and
  \(H'_{\rm WIN}(\theta)\) (square-log mirror) — imply E-S for all
  sufficiently large primes at \(\theta>1/3\) resp. \(\theta\geq1/2\)
  (endpoint \(1/2\) suffices exactly; effective if the constants are);
  mechanism: counterexamples have \(W=\infty\), one valid supercritical
  \(T\) forces the count below one, dyadic sweep.  Proved validity today is
  \(\theta=1/4\) (Theorem 51.2; cubic variant CLAIMED/PROVISIONAL via
  34.8) and \(\theta=1/3^-\) for square-log — each variant sits exactly
  ONE factor \(t=\log T\) short of its own crossing.  Proposition 57.2
  (mass-invariant gap; proved in the formalized absolute-remainder
  architecture; antecedents §18.2/(18.15)/Assessment 18.4 + Lemma 33.3 +
  (51.11) cited, not re-derived): supply mass \(\mu=t^a\) at
  condition-entropy \(t\) caps the exceptional-set exponent at
  \(\theta=a/(a+1)<1\) for EVERY \(a\) — no supply-mass improvement can
  ever cross to pointwise within Bonferroni-CRT / fundamental-lemma /
  large-sieve devices (each checked; the \(\mu t\leq\log N\) budget is
  the CRT information cost).  §57.3 localizes the crossing: hypotheses
  \(H_{\rm XW}\) (supercritical remainder cancellation across
  \(e^{\Theta(\mu)}\) classes at joint moduli \(>N\); the upper-transfer
  mirror of Lemma 33.3) and \(H_{\rm EQ}\) (fair-share conspiracy
  non-concentration for primes) — either implies large-\(p\) E-S
  (Proposition 57.4); §54's residue-one escapes verified subcritical
  (consistency).  Verify (bd): threshold arithmetic + exact harvested-mass
  calibration (integer survivors at \(T{=}3000\) below \(3\cdot10^5\):
  550, of which 547 are squares — see §58; prime tails empty there).
* **§58: the inverse census — Theorem 58.1 (square escape; proved,
  max-severity replayed): \(W(m^2)=+\infty\) for EVERY positive integer
  \(m\)** — every harvested Lemma-16.1 class misses every perfect square
  (quadratic-character eligibility conspiracy; the naive per-factor
  shortcut is FALSE — \(M{=}15,D{=}2\) counterexample — the repaired
  proof handles composite/prime-power/2-adic/\(\ell\mid D\) cases; 750k
  square-residue incidences replayed exact).  Consequently, under the
  moving convention (58.2) (\(L_{\rm int}(T)=\min\{n>T:W(n)>T\}\), the
  raw inverse being corrupted by \(W(1)=W(4)=\infty\)):
  \(T<L_{\rm int}(T)\leq T+2\sqrt T+1\) — the all-integer inverse is
  NEAR-LINEAR, so the **integer/prime dichotomy is PROVED**: all-integer
  supercritical fair-share is false (squares over-concentrate,
  \(\sim\sqrt N\) permanent conspirators \(\leq N\)), and any
  count-below-one route to E-S (§57) is prime-essential.
  \(L_p(T)\leq\exp\{(5.2+o(1))T\}\) (§54).  Exact censuses to
  \(T=2000\) (\(L_p\) vs hard-only \(L_h\) kept distinct:
  \(L_p(335)=22621\) vs \(L_h(335)=1853329\)); Lemma 58.2
  (shifted-sieve necessary conditions: \(W(n)>T\Rightarrow n+4\) free of
  primes \(\equiv3\ (4)\leq T\), \(n+8\) free of \(\equiv7\ (8)\));
  Theorem 58.3 Iwaniec's Jacobsthal bound \(g(n)\ll(\omega\log\omega)^2\)
  secondary-source-verified (Costello–Watts 2013 + FGKMT PDFs archived in
  sources/jacobsthal-literature/ with honest provenance — primary 1978
  paper inaccessible); Lemma 58.5 duality: superlog prime \(W\)-records
  \(\iff\liminf\log L_p(T)/T=0\) (§56 caps congruence routes;
  technology audit finds no sifted-set least-prime tool).  Review:
  SOUND-AFTER-REPAIRS.
* **paper v8 (79pp, FAITHFUL-AFTER-REPAIRS):** §56 absorbed (certificate
  ceilings with every wave-21 caveat, censuses digit-checked, (56.16)
  three-label window display); §57–§58 queued for v9.  Vaughan 1970:
  wave-22 retry failed again (new routes logged; DOI corrected to
  …2886 in the access log).

## Outcome 25 (2026-08-30, wave 21 — see notes.md §56 + paper v7; hostile-reviewed → repaired / FAITHFUL)

* **§56: the congruence-certificate ceiling — §54's lower bound is optimal
  among ALL congruence certificates (proved, effective).**  Theorem 56.1
  (Type-II): ANY class \(a\ ({\rm mod}\ Q)\) — adaptive, not just the
  §54 lcm construction — whose (primes/integers) all satisfy \(W>T\) must
  have \(P_3(T)\mid Q\), so \(\log Q\geq(1/2+o(1))T\): the \(D=1\)
  intrinsic datum (class \(-4\bmod\ell\), Lemma 18.1/16.1) is hit via
  CRT+Dirichlet unless \(\ell\mid Q\), for every prime
  \(\ell\equiv3\ (4)\), \(\ell\leq T\).  Honest limitation recorded: only
  \(1/2\), not the full-lcm constant 1.  Theorem 56.2 (Type-I): a class
  certifying \(ck_{\min}>T\) must be genus-forced on every slice
  \(ck\leq T\) (Corollary 52.2 forbids identically-vanishing unforced
  progressions!) ⇒ \(\chi_s\) constant on the class ⇒ (primitive
  characters are nonconstant on proper-divisor classes) conductor
  \(f_s\mid Q\) for every forced core ⇒ \(\log Q\gg T\).  Corollary:
  §54 is Linnik-capped-optimal among congruence certificates (GRH remark
  labeled); beyond-log extremal lower bounds need non-congruence
  certificates (Assessment wall).  Computational 56.3/56.4 + verify (bc):
  W-statistic records to \(10^6\) (full-scan \(10^7\)), \(ck_{\rm pr}\)
  records to \(3\cdot10^5\) (full-scan \(10^6\)), conspiracy depth
  \(D(p)\) extension — streamed/chunked, cross-checked exactly against
  (ax)/(aw) overlaps; normalized maxima INFO-only, no growth-law claims.
  Review: SOUND-AFTER-REPAIRS (eventual-certificate quantifiers, memory
  wording, pointer fix).
* **paper v7 (74pp, FAITHFUL, zero defects):** §54–§55 absorbed (two-sided
  frontier display, A∈[1,~2] window, general-m effectivity perimeter with
  review-tightened scope), Dyachenko/auro-zera external context absorbed
  with the honest conditional characterization; §56 queued for v8.

## Outcome 24 (2026-08-29/30, wave 20 — see notes.md §54–§55 + paper v6 + reviews/external-auro-zera-lean-wave20.md; all hostile-reviewed → repaired)

* **§54: the LOWER tail — logarithmic witness moduli are NECESSARY;
  H_MOD(A) and H_SPF(A) are REFUTED for every A < 1 (proved, effective;
  review CONFIRMED with no mathematical repairs).**  Theorem 54.1: every
  prime \(p\equiv1\ ({\rm mod}\ M(T))\) has \(W(p)>T\) (the §17.3
  residue-one size argument covers every Lemma-16.1 datum); effective
  Linnik (Xylouris 5.18) then gives infinitely many \(p\) with
  \(W(p)\geq c\log p\).  Theorem 54.3 (Type-I mirror): \(p\equiv1\ ({\rm
  mod}\ R(T))\) forces \(\chi_s(p)=1\) for all \(s\leq T\) (Theorem 50.5's
  construction) ⇒ every slice \(ck\leq T\) genus-forced ⇒ even
  \(ck_{\min}(p)>T\); same Linnik quantification.  Corollaries: the
  pointwise hypothesis space collapses to **A ≥ 1 exactly, in both
  frames** — the two-sided W picture is now: typical size polylog^\(\epsilon\)
  (a.a. tails, §51/§53) and extremal size \(\geq c\log p\) i.o. (§54,
  effective).  Every eventual exponent \(A\geq1\) remains open.  The old
  \(\log p,\log p\log\log p,(\log p)^2\) panel from the census and
  Dahan/auro-zera data is only a finite normalization window, not a
  conjectural upper frontier; §67 records the finite value
  \(A_{\rm emp}(2031121)=2.923244\).  The full-lcm escape cannot by itself
  beat log-scale because its lcm cost is forced.
* **§55: the general-m truncated tails and the m-uniform effectivity
  perimeter (SOUND-AFTER-REPAIRS).**  \(W_m(p)\) tails in both supply
  variants (Layer-1 \(\eta_1(m)/\varphi(m)\)-thinned square-log; thinned
  cubic \(\theta_m(\log T)^3\), inherits Provisional 43.7) with
  top-of-window consistency vs Theorem 43.12.  The E19-flagged
  exceptional-conductor-divides-m subtlety RESOLVED: for \(r_1\nmid m\)
  the §51.5 deletion transfers; for \(r_1\mid m\) every BV modulus is
  divisible by \(r_1\) (deletion impossible) and the repair retains the
  residue classes where the exceptional term has favorable sign — review
  tightened the quantifiers (holds for the FULL Layer-1 family and
  structured c-free fibres, NOT arbitrary sparse subfamilies; worst-case
  fibre-retention inequality added; unfavorable k=1 case fixed).
  Effectivity-perimeter table per row (Layer-1 / thinned-cubic / 43.12).
* **paper v6 (66pp): §51–§53 absorbed** — the effectivity headline, the
  witness-modulus tail, the empty third layer, almost-all H_SPF with the
  genus-permission asymmetry, Dahan/Lenstra–Pomerance references,
  blind-adjudication pedigree; §54–§55 queued for v7.
* **External review (pasky request): the "auro-zera" Lean formalization
  (github Suro-One) is NOT a proof** — sound algebraic identity layer
  (witnesses replayed exact), complete mod-840 split, but ONE axiom
  (`good_divisor_exists`) = exactly the open hard core, and its cited
  support (Dyachenko arXiv:2511.07465) disclaims the infinite case in its
  own Conclusion ("certainly not proven … conditional in nature" —
  verbatim, PDF archived).  Reconciliation: their rigid primes = our
  conspiracy set; their cascade = our escape walls; their axiom = the
  unbounded cousin of H_MOD/H_SPF; our §51–§54 strictly quantify what
  they assume.  No campaign statement needs revision.  Artifacts in
  sources/auro-zera/ + sources/dyachenko-2511.07465.pdf; review in
  reviews/external-auro-zera-lean-wave20.md.

## Outcome 23 (2026-08-29, wave 19 — see notes.md §53 + §51.9–§51.10 + blind51.md; all hostile-reviewed/adjudicated → repaired)

* **§53: almost-all \(H_{\rm SPF}\) — proved, EFFECTIVE — and the
  genus-permission asymmetry derived.**  Theorem 53.1 (fixed box \(T\),
  effective): per reduced hard class \(C\) mod \(Q_T\), the stacked
  no-good-slice-prime sieve exponent is \(1+m_\#(C)\), \(m_\#\) the exact
  root-union density (the naive mass \(\sum2/\varphi(4ck)\) is WRONG:
  equal radicands \(c_1k_1^2=c_2k_2^2\) — e.g. (5,2) vs (20,1) — are
  permanent root-class duplicates; Lemma 53.1a gives the sharp
  \(4T^2\) disjointness threshold).  Single-slice case = Theorem 52.1.
  **Theorem 53.3 (headline, max-severity reviewed):** for every fixed
  \(A<1\), \(\#\{\)hard \(p\leq X\): no active slice \(ck\leq(\log X)^A\)
  has a good prime factor\(\}\ll_A(X/\log X)\exp\{-c_A(\log\log
  X)^{3/2}/\sqrt{\log\log\log X}\}\) — EFFECTIVE (uniform-in-dimension
  beta-sieve fundamental lemma + Landau–Page-repaired Siegel–Walfisz;
  no BV).  Corollary 53.4: the \(H_{\rm SPF}(A)\) event fails on at most
  that many hard \(p\) — the pointwise frontier now holds almost-all in
  BOTH frames.  The exponent is \((\log\log)^{3/2}\), not \((\log\log)^3\):
  the genus-permission layer (escape classes of Theorem 50.5, smallest
  active core \(q_0\) with mass \(\gg(\log(T/q_0))^2/q_0\) vs
  \(\Pr(q_0>y)=2^{-\pi(y)}\)) costs exactly a square root vs the
  permission-free Type-II stack (§51) — an honest structural asymmetry,
  not a technical loss.  Review repairs: corollary cutoff direction, the
  Page no-exception branch, exact growing-dimension sieve error, overlap
  threshold, Dahan cross-reference.  Verify (az): overlap geometry for
  all 111 slice labels \(ck\leq30\), \(Q_{30}=9{,}316{,}358{,}251{,}200\),
  256-class \(m_\#\) census + explicit escape class, mass regressions,
  \(ck_{\rm pr}\) consistency.
* **§51.9–§51.10 + blind51.md: priority search, exact citations, and the
  blind-construction adjudication of the effectivity headline.**
  Priority (§51.9, honest register): PW's printed §4 chain is
  Siegel-sensitive exactly at its BV lower bound — no effectivity claim
  in the literature found for Vaughan-strength E-S bounds;
  **Lenstra–Pomerance JEMS 2019 Lemma 11.2** verified as the precise
  citable effective excluded-conductor BV form (repairs the review's
  citation caveat); **Dahan arXiv:2608.24035 (2026)** found and archived:
  his Theorem 4.17 reaches the SAME \((\log\log N)^3\) exponent shape at
  polylog depth for a DIFFERENT statistic (two-parameter \(u,a\) search
  depth, no genus gate, explicitly ineffective) — now cited prominently
  at the cubic-variant statement *(wave-19 priority repair)*: the shape
  antecedent is his; the minimal-congruence-modulus statistic and the
  effective constants are ours.  Vaughan 1970 still inaccessible (new
  routes tried, logged).  Blind adjudication (§51.10, protocol as
  §41/§43.11; blind clone at the pre-wave-18 commit): CONVERGED-WITH-
  DIVERGENCES — tails, windows, repair architecture and PW comparison
  all reproduced; the one material divergence was a BLIND-side overclaim
  (it asserted effectivity of Theorem 34.8's ancillary all-triples
  \(o(1)\), which the deletion repair does not give; §51's narrower
  perimeter is correct).  Labels unchanged: independent-construction
  datum, not a status upgrade.

## Outcome 22 (2026-08-29, wave 18 — see notes.md §51–§52 + paper v5; all hostile-reviewed → repaired)

* **§51: the record and the pointwise frontier are now one object — the
  witness-modulus tail — and the repaired supply chain is EFFECTIVE
  (CLAIMED/PROVISIONAL).**  \(W(p)\) = minimal Lemma-16.1 witness modulus
  \(k\ell\).  Master tail theorem (Theorem 51.2, proved by parameterizing
  the whole §39 machinery at general truncation \(t=\log X\),
  \(\mu=t^2\log K\), with \(X=T^{1/2}\)): for primes,
  \(\#\{p\leq N:W(p)>T\}\ll N\exp\{-c(\log T)^2\log\log T\}\) using only
  Lemma 16.3 supply (no Theorem 34.8), and
  \(\ll N\exp\{-c(\log T)^3\}\) with Theorem 34.8 (inherits its
  provisional status), uniformly to the window top
  \(T=\exp\{\alpha(\log N)^{1/4}\}\) where the cubic tail reproduces
  Theorem 39.7 exactly.  Polylog corollary: \(W(p)\leq(\log p)^A\) outside
  \(N\exp\{-c_A(\log\log N)^3\}\) (cubic variant).  New hypothesis frame
  \(H_{\rm MOD}(A)\) (Type-II mirror of §50's \(H_{\rm SPF}(A)\); neither
  implies the other; either gives E-S for all large p) — the residual
  pointwise problem is exactly the triple-log-sparse conspiracy set.
  **Effectivity audit (Theorem 51.6, record-adjacent):** the belief
  "§16 is SW-ineffective" was WRONG in an unexpected direction — Lemma
  16.3's lower bound uses Bombieri–Vinogradov (so not elementary), but the
  chain is REPAIRABLE to fully effective: Lemma 51.4 (effective
  excluded-conductor BV at polynomially-large moduli: Landau–Page gives at
  most one exceptional real conductor per dyadic block; the review round
  added the missing induced-small-conductor bookkeeping
  \(\sum_{q\leq Q,r\mid q}1/\varphi(q)\ll\log(2Q)/\varphi(r)\) and
  per-block conductor selection) + Lemma 51.5 (deletion tolerance: erasing
  all moduli \(4uv\) divisible by any fixed \(r_1\geq3\) keeps a positive
  fraction of every Lemma-16.2 box mass, pointwise in k — replayed in
  review).  Perimeter honest: Theorem 34.8's ancillary all-triples
  \(o(1)\) sentence is NOT effectivized, only its class-mass consequence
  (34.18)–(34.19) — which is all that Lemma 39.5 uses; the §39 N-side is
  exact integer class-counting; Theorem 16.4's larger sieve and 16.5's
  Rankin transfer are effective.  So Theorems 16.4/39.7/51.2 all become
  effective after the repair.  PW §4 comparison honest (their truncation
  gives the square-log tail; our multiplier family adds the
  \(\log\log T\)/\(\log T\) factor).  Review found + repaired a literal
  integer-vs-prime scope overclaim in the displayed sets.  Verify (ax):
  exact class harvest for all moduli \(\leq3000\), 3,202 primes
  \(<3\cdot10^5\): tails (226, 19, 0, 0) at T=(25,100,400,1600), max
  \(W=279\); exact 6-atom inclusion–exclusion regression; deletion toys.
* **§52: the third slice-obstruction layer is EMPTY at the congruence
  level — per-slice vanishing is a quantified density-zero event (proved,
  elementary sieve).**  Theorem 52.1: for every fixed unforced admissible
  slice \((c,k)\) (core \(\notin\{1,2,3,6\}\)) and compatible unforced
  hard class \(a\): \(\#\{p\leq X:p\equiv a,\ M_{c,k}(p)=0\}\ll
  X(\log X)^{-1-2/\varphi(4ck)}\) — via Theorem 50.1's contrapositive
  (vanishing ⊆ no good prime factor), a dimension-\(1+2/\varphi(h)\)
  upper sieve on integers (2 root classes at each good prime
  \(q\equiv-a\ (4ck)\), whose solvability is automatic from the genus
  identity, + the 0 class), ELEMENTARY remainder — no BV, no SW; constants
  effective for fixed slice.  Corollary 52.2 (the prize): NO arithmetic
  progression inside any unforced slice-class is identically vanishing —
  §44's core law + §48.1's genus law are the COMPLETE list of
  congruence-level vanishing laws per slice; everything deeper is
  factorization noise with decaying frequency.  Proposition 52.3: uniform
  version to \(4ck\leq(\log X)^\theta\) (SW-based, ineffective, labeled).
  Census (ay, exact to \(3\cdot10^4\), full-scan \(10^5\)): 31 unforced-slice
  residual frequencies; the 74 \(ck_{\rm pr}>ck_{\min}\) gap events
  dissected (canonical composite witnesses: 68/98 semiprime, 24 with ≥3
  prime factors, 6 prime powers — refuting the all-semiprime guess);
  same-core pair correlations near independence with stable exceptions
  ((5,1)×(5,2) ratio ≈0.53) — no independence claim.  Honest walls: no
  \(D(p)\) pointwise bound, no \(H_{\rm SPF}\) case, per-slice vanishing
  infinitude OPEN (parity-adjacent), multi-slice union deferred (wave-19
  target: the growing-dimension stacked sieve toward almost-all
  \(H_{\rm SPF}\); note the genus-permission layer will degrade the
  stacked exponent — the escape-prime classes of Theorem 50.5 have zero
  small-slice supply).
* **paper v5 (54pp, FAITHFUL-AFTER-REPAIRS):** §49 grid refutation + §50
  conditional frontier absorbed; the antichain-repair storyline now ends
  at the §49 refutation everywhere; three §50 caveat/label omissions
  repaired in fidelity review; records + provisional labels intact;
  §51–§52 flagged as the v6 queue.

## Outcome 21 (2026-08-29, wave 17 — see notes.md §49–§50 + paper v4; all hostile-reviewed → repaired)

* **§49: the ANTICHAIN repair is also refuted — the factorial-moment /
  codegree route to the complete system is now structurally closed
  (maximum-severity refutation review CONFIRMED).**  Theorem 49.1: exact
  implication criterion between intrinsic atoms; §49.2: what first-moment
  mass the implication reduction preserves; Theorem 49.4: the uniform
  \(1/\varphi(g)\) residue profile FAILS even on the antichain (the
  \(D=2\) slice stays residue-concentrated — the §39.3 cancellation has
  no analog here).  Theorem 49.5 (collective-closure obstruction):
  maximal \(D=2\) semiprime atoms \(n\equiv-8\ (q_ip_j)\),
  \(q_i\equiv3\,(8)\), \(p_j\equiv5\,(8)\), form complete bipartite grids
  in the antichain; the diagonal matching's INTERSECTION implies every
  off-diagonal edge (extension ratio exactly 1), so
  \(\mathcal L^\dagger(S)\geq t(t-1)\gg\Lambda\) for pairwise-coprime
  squarefree \(S\), and one CRT class \(C_R\) (cost \((2z)^{-2t}\)) fires
  all \(t^2\) atoms, exploding \(\mathbb E((H^\dagger)_m\mid T_0)\) past
  \((C\Lambda)^m\) at \(m\asymp\Lambda\).  Lesson: no void-preserving
  single-atom reduction can stop INTERSECTIONS from having rich divisor
  shadows; the hierarchy/moment FORMULATIONS (40.27–28, 47.16,
  37.19-for-any-reduced-count) are dead — the cube killed nesting, the
  grid kills antichains.  Scope: H_PF′, (33.16), (40.19), (37.27)
  untouched; Lemma 33.3's minorant now needs a non-moment construction;
  Proposition 47.3's prime-only rung survives.  Strategic consequence
  (Assessment): the H_PF′-refutation arc's stakes were already collapsed
  by the unconditional §39 record; with the moment door closed this axis
  is DORMANT unless a genuinely new mechanism appears.
* **§50: the pointwise problem reduced to a named bespoke hypothesis, and
  the conditional frontier mapped.**  Proved reduction: a prime
  \(q\mid p^2+4ck^2\) with \(q\bmod4ck\) in the explicit good-class set
  \(G(c,k)\) (\(\chi_s\)-compatible slices only) forces slice positivity,
  hence a Type-I witness.  \(H_{\rm SPF}(A)\) (formalized, falsifiable):
  every large hard \(p\) has such \((c,k)\), \(ck\leq(\log p)^A\) —
  implies Type-I E-S for all large hard \(p\).  Audits (Assessment, each
  with the exact failing step): Bateman–Horn is asymptotic-in-family, not
  per-\(p\); GRH/Chebotarev stays compositum-limited even with the
  polylog \((c,k)\) freedom (recomputed in the slice frame); EH is
  exceptional-set-only.  Census (aw): minimal-\(ck\) distribution across
  hard \(p<3\cdot10^4\) (+\(10^5\) scan), implication instances
  machine-checked.  Register kept: \(H_{\rm SPF}\) is unproved; no
  unconditional pointwise progress claimed.
* **paper v4 (45pp, FAITHFUL-AFTER-REPAIRS): Theorem 43.12 promoted to
  the general-m headline** (fourth-root thinning, range
  \(m\leq(\log N)^{3-\epsilon}\), full proof incl. the finite
  relative-mass inequality), §47 refutation + §46 endpoint widening +
  §48 moving-genus material absorbed, PW comparison redone, pedigree
  section updated; wave-17 fidelity pass fixed four stale (47.16)-open
  claims (the §49 grid refutation postdates v4's drafting and is noted
  as the v5 queue item together with §50).

## Outcome 20 (2026-08-29, wave 16 — see notes.md §46–§48, §43.11–§43.12, §47's refutation, paper v3; all hostile-reviewed → repaired)

* **§47: the literal codegree hierarchy (40.28) and the raw-\(H\) moment
  bound (37.19) are REFUTED — maximum-severity review CONFIRMED.**
  Theorem 47.2 (nested retained-atom obstruction): primes
  \(q\equiv3\,(8)\), \(p_i\equiv5\,(8)\) in \((Y,2Y)\) build
  \(M=q\prod_1^kp_i\), \(k\asymp L/\log L\); every odd subset \(I\) gives
  the SAME residue \(-8\) atom mod \(M_I\mid M\) (Lemma 18.1 supply,
  \((-8/q)=+1\) so not prime-implied, \(D=2\) canonical) — a Boolean
  implication lattice: conditioning on the finest atom fires all
  \(2^{k-1}\) coarser ones free, so \(\mathcal L(\{A\})\geq e^{cL/\log L}\)
  and \(\mathbb E((H)_m\mid T_0)\gg(K)_m/M\gg(C\Lambda)^m\) for every
  \(C\).  The flaw is LOGICAL REDUNDANCY in the §37/§40 formulations, not
  in the sieve: the repair (§47.4) implication-reduces the family to the
  inclusion-maximal antichain — void preserved exactly — and the
  residue-resolved hierarchy for THAT reduced family (47.16) is the new
  open wall.  Proposition 47.3: prime-only selected sets still satisfy
  \(\mathcal L(S)=O(\Lambda)\).  Scope crisp: refutes a proposed
  sufficient mechanism; H_PF′, (33.16), (40.19), (37.27) untouched.
  Supersession pointers planted at every stale §37/§40/§42/§45/§46 status
  line.  Verify (at): exact toy \(\mathcal L\)-computations + the (47.15)
  prime-power corner examples.
* **§43.12 (wave-16 blind construction → adjudicated strengthening):
  fourth-root thinning — CLAIMED/PROVISIONAL.**  The §35/§41-style blind
  parallel construction of the general-m chain (frozen in blind43.md,
  attested §43.11) converged on S1–S5 and found the ledger scales with the
  THINNED mass: \(y,r\) shrink to \(\Theta(\theta_mt^3)\),
  \(\theta_m=\eta_2(m)/\varphi(m)\), ledger \(e^{O(\theta_mt^4)}\), so the
  window releases \(t=(\log N/\theta_m)^{1/4}\)-scale and
  **Theorem 43.12**: \(E_m(N)\ll N\exp\{-c(\eta_2(m)(\log
  N)^3/\varphi(m))^{1/4}\}\) uniformly for \(3\leq m\leq(\log
  N)^{3-\epsilon}\) (vs Layer 2's linear thinning and \((\log
  N)^{3/4-\epsilon}\) range; at \(m=4\) same shape as Theorem 39.7).
  Maximum-severity adjudication CONFIRMED (load-bearing new step: a
  finite relative-mass inequality for the thinned multiplier family;
  PW crossover recomputed; Layer-1 all-denominator range repaired).
  Theorem 43.8 retained as the conservative replay; inherits Theorem
  34.8 + §39.7 qualifications; external status unchanged.
* **§46 (endpoint bulk): closed prefix widened
  \(W_0\asymp L^3/(\log L)^2\to W_1\asymp L^5\log\log L/(\log L)^2\), plus
  the large-c wedge \(c\geq z\), \(m\leq zW_1\); exact remainder =
  distinct-cell collision sum (46.13).**  Mechanisms: per-block
  injectivity (blockwise \(p>2W\)), supported-cell progression occupancy,
  a global cell-diagonal estimate.  The dyadic method provably loses
  \(W/(CW_1)\) on the remainder; (40.19)/(37.27) remain OPEN.  Verify
  (as): exact 5-corner resum of \(\mathcal V_X^{\rm end}\) at
  \(X=80..800\).
* **§48 (conspiracy depth): the vanishing law is a MOVING genus
  character.**  Theorem 48.1: for hard \(p\) and slice \((c,k)\),
  \(\chi_s(p)=1\Rightarrow M_{c,k}(p)=0\) (\(s\) = squarefree core of
  \(c\)); \(\chi_s\equiv1\) on the hard progression iff
  \(s\in\{1,2,3,6\}\) — so §44's identical-vanishing law is the
  fixed-character slice of a per-p obstruction that kills ~half the
  unforced slices at each p.  Theorem 48.4: complete fixed-divisor
  progression law (the guaranteed-positivity classification); Theorem
  48.5: residue-one escape — every bounded fixed-divisor guarantee system
  is escaped forever (the §17.3 mirror in slice language); Proposition
  48.6: Type-I depth-equivalence bookkeeping.  Review fixed a false §35
  same-row identification.  Census D(p) to \(3\cdot10^4\) (ES_FULL_SCAN
  \(10^5\)).  Register: pointwise existence remains the conjecture.
* **paper v3 (41pp, FAITHFUL-AFTER-REPAIRS): general-m second headline +
  verification-pedigree section + §42/§44/§45 absorbed; §46–§48 and
  Theorem 43.12 are the flagged v4 queue** (README erratum notes).  Two
  dropped hypotheses and a census datum restored in fidelity review;
  DFI/Bettin–Chandee provenance corrected; zero pdflatex errors.

## Outcome 19 (2026-08-29, wave 15 — see notes.md §43–§45 + §34.5 + reviews/; all hostile-reviewed → repaired)

* **§43 (general numerators): the whole multiplier machine is m-uniform —
  CLAIMED/PROVISIONAL two-layer record for every fixed m.**  Lemma 43.1:
  the Lemma-16.1 identity holds verbatim for every numerator \(m\ge3\)
  (\(k\ell\equiv-1\ (m)\), \(A=(k\ell+1)/m=uvw\), class
  \(n\equiv-uv^{-1}\ (k\ell)\) ⇒ \(m/n\) is a sum of three unit
  fractions).  Exact thinning factors \(\eta_1(m),\eta_2(m)\) computed;
  Layer 1 (complete §16 replay, internally proved): \(E_m(N)\ll
  N\exp\{-c(\eta_1(m)/\varphi(m))^{1/3}(\log N)^{2/3}(\log\log
  N)^{1/3}\}\), primes to \(m\le(\log N)^{2-\epsilon}\), all denominators
  to \(m\le(\log N)^{1-\epsilon}\) (semigroup transfer is m-uniform).
  Layer 2 (inherits provisional Theorem 34.8 through the muv-threaded
  Theorem 43.7): \(E_m(N)\ll N\exp\{-c\,\eta_1(m)(\log
  N)^{3/4}/\varphi(m)\}\) for \(m\le(\log N)^{3/4-\epsilon}\).  Honest
  benchmark: PW 2025's exponent \((\log^2N/\varphi(m))^{1/3}\) transcribed
  exactly; two-regime comparison — ours wins iff (roughly)
  \(\varphi(m)\le(\log N)^{1/8}\), i.e. for every fixed m; PW's uniformity
  is better for large m.  NO uniform-beating claim.  Maximum-severity
  review: SOUND-AFTER-REPAIRS (semigroup cutoff \(\epsilon/4\); conditioned
  local factor; reduced-fibre quantifier; no Siegel-uniform or short-class
  equidistribution used — only the aggregate \((k,m)=1\) family).
* **§44 (slice conspiracies): the exact vanishing law of the §36 ray-mass
  slices, a strictly larger wrong-grade obstruction, and a census of deep
  conspiracies.**  Theorem: slice \((c,k)\) vanishes at \(p\) iff the
  exponent box of \(p^2+4ck^2\) misses the grade \(-p\bmod4ck\) (raw form;
  raw-vs-primitive Möbius boundary repaired in review with the exact
  counterexample \(M_{7,3}(241)=2\), \(M^*_{7,3}(241)=0\)).  New proved
  obstruction: squarefree core of \(c\) in \(\{1,2,3,6\}\) ⇒ the slice
  vanishes identically on hard primes — 80 of the 111 slices with
  \(ck\le30\) are forced to zero (strictly extends Theorem 36.2).  The
  \((5,1)\) slice is positive on \(p\equiv97\ (120)\) — identified in
  review as the known §35/§16 supply re-read in ray language.  Two-slice
  joint vanishing is NOT determined mod the natural modulus (193 vs 1033
  mod 840).  Census (aq): 15 of the 385 hard primes \(<3\cdot10^4\) have
  ALL 111 small slices vanishing (2521 among them) — depth-111
  conspiracies exist; every such p still has Type-I witnesses at larger
  ck.  GRH audit sharpened: even idealized square-root cancellation across
  the \(O(p)\) fibres leaves \(p^{1/2+o(1)}\) against a \(p^{o(1)}\)
  principal term — the moving-divisor wall, now with the exact formula.
  Pointwise existence remains the conjecture; register kept.
* **§45 (endpoint vs Kloosterman fractions): DFI/BC audited against the
  actual papers — insufficient for (40.19) — but the review round found
  and we formalized Theorem 45.9, the widest proved (40.19) subfamily.**
  Lemma 45.1: \(\mathcal V_X^{\rm end}\) IS an exact Kloosterman-fraction
  matrix form (phase \(e_p(-h\bar m)\), \(m=4c^2s\)); both reciprocity
  orientations audited (q can never carry the phase modulus).  DFI 1997
  (PDF finally obtained — Duke's UCLA archive) and Bettin–Chandee
  transcribed with true quantifiers; failure is structural: the
  coefficients are a joint \((m,p)\) matrix, not separated sequences, and
  the complete h-sum needs an operator/large-sieve bound, not a scalar
  bilinear one (exact failure logs 45.4–45.6).  Theorem 45.9 (from the
  hostile review, independently verified, no cancellation used): cells
  with \(m=4c^2s\le W_0\asymp L^3/(\log L)^2\) are pairwise
  non-colliding mod every endpoint prime (\(W_0=o(z)\) + inversion
  injectivity), so their energy is \(\ll W_0L^3\ll\Lambda^2\) — closes
  \(\asymp L^3/(\log L)^2\) moving-s fibres over the ENTIRE prime range
  (vs \(O(L^{3/2}/\log L)\) fixed fibres before).  Open core of (40.19)
  is now exactly the bulk \(m>W_0\).  (40.19), (40.28), (37.19), (33.16),
  H_PF′: all still OPEN.
* **§34.5 (attestation): third independent re-derivation of Theorem 34.8
  — CONFIRMED-AFTER-REPAIRS.**  Fresh blind unit re-derived the
  power-sized Lemma-16.2 extension, the second-incidence-moment pruning,
  and the BV-multiplicity assembly; Shiu's 1980 hypotheses instantiated
  from the actual PDF (\(\alpha=\beta=1/4\)); the \(1\in\mathcal J\) use,
  same-prime distinctness, and §39's data-dependent subfamily inheritance
  (\(\mathcal J_c\), canonical boxes, \(h(\mathcal J_c)\gg\log K\)) all
  audited.  The record chain's single provisional input now has three
  independent internal checks; external expert review remains the gate.
* **Sources:** DFI 1997 and Bettin–Chandee 2015 PDFs archived with
  provenance; Vaughan 1970 still inaccessible after a systematic chase
  (access log in sources/vaughan-1970-access-log.md — don't re-pay).
  Latent §31 eaten-\(\backslash\)r artifact found and fixed by two units
  independently; new corruption species (eaten backslash before
  \(\backslash\)n-commands) caught in review and swept: zero remaining.

## Outcome 18 (2026-08-29, wave 14 — see notes.md §41–§42 + paper v2; all reviewed → repaired)

* **§41 (blind parallel construction of the §39 record chain): CONVERGED,
  no error found.**  Under a §35-style attested blind protocol (derivation
  frozen in `unit_r_blind.md` at commit 347a570 before §39 was opened), a
  fresh unit re-derived S1–S7 (the full c-free assembly chain) from §16+§34
  inputs alone; all seven verdicts CONFIRMED-SAME-METHOD (route divergences
  non-substantive: Shiu mod k, pointwise 1/k moment bound, direct weighted
  fibre averaging — review re-checked each variant closes).  Numerical
  stress: exact rational CRT moments to j=6 at dyadic-cutoff toys to
  X=10⁴ (14,210 atoms, 1.13M compatible pairs — coupling/distinct-ℓ/dedup
  all hold; no scale-growing residue-profile excess).  This adds an
  independent-construction datum; it does NOT upgrade §39's
  CLAIMED/PROVISIONAL status (Theorem 34.8 remains the shared provisional
  input).
* **§42 (endpoint attack): (40.19) still OPEN, now sparse-structured.**
  Proved: exact unique-cofactor form (\(q_p(R)\) unique in \([1,4R)\)),
  complement-divisor \(c^2s\) reindexing, no-equal-shift collision lemma,
  every fixed squarefree-\(s\) fibre \(o(\Lambda^2)\) uniformly in
  \(s\), and the full target on every fixed polylog prime range
  \(z<p\leq L^B\) (per-\(B\) constants).  The unresolved core: moving
  \(s\mid{\rm rad}(R)\) superposition at \(L^B<p\leq X/z\) — Gauss/completion
  bounds do not couple to the moving nonnegative coefficients (42.26).
  (37.27), (37.19), (33.16), H_PF′: all remain OPEN; no status line
  superseded.
* **paper v2: the provisional 3/4 is now the paper's headline** — ~30pp,
  complete §39 chain with every wave-13 repair and caveat transcribed
  (fidelity-reviewed; five real eaten-\(\backslash\)r artifacts found and
  fixed), §40 frontier subsection, priority framing search-limited and
  conditional.  External expert review of the 3/4 chain is TODO #1.

## Outcome 17 (2026-08-29, wave 13 — see notes.md §39–§40 + paper/; §39 maximum-severity-reviewed (record chain SURVIVES) → repaired; §40 + paper reviewed → repaired)

* **§39 (c-free critical-window assembly): E_all(N) ≪ N exp{−c(log N)^{3/4}}
  — unconditional, CLAIMED/PROVISIONAL.**  The record-class chain: (i)
  Lemma 39.1 — the §34.4 M₀-partition wall dissolves because the H_kBV
  coupling \(k\mid u+cv\) is IMPLIED by each atom's own congruence, so one
  fixed c-free unpruned family majorizes every exceptional prime; compatible
  atom sets have pairwise-distinct large primes \(\ell\) (size argument
  \(z^2<\ell\) + unique-multiplier argument \(4uv>4H^2\gg K\)); (ii) Lemma
  39.2 — residue-resolved mass profiles \(W_{k,a}(g)\ll
  t^2\varphi(k)^2/(\varphi(g)k^3)\) (Shiu in reduced classes; rewritten in
  review), total mass \(\mu\asymp t^3\); (iii) Theorem 39.4 — ALL factorial
  moments \(\mathbb E(H)_m\le(Ct^3)^m\): lcm-collapse and residue-consistency
  cancel exactly at every prime power under \((n,P_y)=1\) conditioning,
  \(y=Bt^3\) (the direct Janson route fails: \(\Delta=\Theta(\mu^2)\));
  (iv) Lemma 39.5 — conditioned void \(\le e^{-ct^3}\) via Chernoff on the
  multiplier fibre + Theorem 34.8 applied to every surviving subfamily
  \(\mathcal J_c\); (v) Theorem 39.6 — even-Bonferroni majorant at degree
  \(r\asymp t^3\) with honest ledger \(e^{O(rt)}=e^{O(t^4)}\), absorbed by
  the window \(\log N\ge C_0t^4\) (the literal \(e^{O(J)}\) clause of
  H_PF′(kℓ;good) remains open — deliberately bypassed, not proved).  Fresh
  maximum-severity review re-derived (39.10)–(39.11) and the unequal-prime-power
  moment induction, confirmed Theorem 34.8's subfamily uniformity, found two
  MAJOR writing gaps (both repaired: full Shiu derivation inserted; \(y<X^{1/2}\)
  restriction) and no mathematical break.  Status: inherits Theorem 34.8's
  provisional status; needs external expert check + priority search before
  citation.  θ=3/4 is the absolute ceiling of this axis (§18.2).
* **§40 (complete-system residue dispersion): the regular tail closes;
  (37.27) ≡ an explicit short-cofactor endpoint.**  Proved: exact
  deduplicated character reformulation of the dispersion quantity; atom
  diagonal \(O(\Lambda)\); regular progression tail \(o(\Lambda^2)\).  The
  full pair bound (37.27) is equivalent to the falsifiable endpoint estimate
  (40.19) (moving short-cofactor range analogous to Theorem 31.3's
  \(u_p\) term); generic large sieve and divisor-BDH provably do not supply
  it; the higher-codegree hierarchy (40.28) is a separate open wall.  Also
  corrected a parent-session inference; H_PF′ remains OPEN, no status line
  superseded.
* **paper/ (consolidation): the H_PF arc as a compilable standalone paper.**
  ~20pp, complete proofs (criterion, intrinsic system, cubic supply, prime
  slices, square-class phenomenon, the §31 refutation with exact scope, the
  §33/§37 transfer walls), full provisional-status and Vaughan-access
  honesty; fidelity-reviewed against notes.md (nine transcription defects
  found → repaired); pdflatex zero errors.  §39 not yet absorbed.

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
