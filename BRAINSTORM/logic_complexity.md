# Brainstorm O141(c): computational complexity of finding ES solutions

Status: no theorem here proves any case of ES. Verdict: **PARTIAL**. We get a sharp computational reading of
barrier B1: congruence-table search is provably superpolylogarithmic infinitely often, while search with one
factorisation per slice looks polylogarithmic in the data. We also get one EVIDENCE-level observation on
factor leakage that is new to the campaign. The angle does not escape B1/B2.

## 1. Idea

**The search problem.** ES-SEARCH takes n (log n bits) and outputs (x,y,z) with 4xyz = n(xy+yz+zx). The
witness has O(log n) bits, since x ≤ 3n/4, y ≤ 2nx and z ≤ 2n⁴. If ES is true, ES-SEARCH is a TFNP problem.
Questions:
* (Q1) Is ES-SEARCH in FP, i.e. time poly(log n)?
* (Q2) What does a factoring oracle buy?
* (Q3) Does ES-SEARCH help factoring?
* (Q4) What would a proof in bounded arithmetic give?

**Bounded arithmetic (standard).** ES is ∀n ∃w ≤ t(n) φ with φ atomic. By Buss's witnessing theorem,
S¹₂ ⊢ ES would give a polynomial-time ES solver, and T¹₂ ⊢ ES would put ES-SEARCH in PLS. IΔ₀ gives
nothing: the least witness is Δ₀-definable, and it lies in the linear-time hierarchy whether or not ES is
provable.
* Consequently, a proof of ES of "feasible" shape (formalisable in S¹₂/PV) *is* a classical poly-time
  algorithm. An analytic proof (positive counts, sieve lower bounds) need not be.
* So "is there an FP algorithm?" is a sharp necessary condition for the most constructive kind of proof.

## 2. Literature anchor

* Buss, *Bounded Arithmetic* (1986): witnessing for S¹₂ (FP) and T¹₂ (PLS, Buss–Krajíček 1994). From
  memory; standard.
* Jeřábek, "Integer factoring and modular square roots" (JCSS 2016): FACTOR reduces to PPA ∩ PPP under
  randomised reductions. From memory, unverified.
* Shor (1994): FACTOR ∈ BQP.
* ES computations: Salez (2014, arXiv 1406.6307) verified ES to 10¹⁷ via modular filters. From memory;
  the campaign's own verification to 10⁸ is in STATUS.md.
* Campaign inputs:
  * POINTWISE_OMEGA13 / POINTWISE_MN: W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4}) infinitely often
    (PROVED modulo cited sources). Here W(p) = min{M ≡ 3 (4) : p mod M ∈ 𝓡(M)} is a p-independent
    table search.
  * POINTWISE_SIZE §4 and OMEGA Thm 8.5: Type-I slice minimum ck_min ≫ log p·log₃p infinitely often
    (modulo Lau–Wu).
  * CONDITIONAL_ES Lemma 1.1: slice form t·p + 1 = m·m'', 4 | m, m ≡ m'' ≡ −1 (mod t), with an explicit
    solution.

## 3. Results and screens

**(R1) Table search is provably not polynomial (PROVED modulo the campaign's cited inputs).**
* Consider any algorithm that certifies ES(p) only by testing p mod M ∈ 𝓡(M) for M ≤ T(p), in any order.
  If T(p) ≤ exp(c(log p)^{1/4−ε}), it fails for infinitely many p. This is just W's Ω-result restated.
* Brute force over ET pairs (a,b) with (−p mod 4ab) | a+b (no factoring) is a table search of the same
  kind (𝓡 is replaced by ET's tables). Its Haar-model failure probability up to size T is ≈ exp(−c(log T)³)
  (Haar exponent 3). So the worst case over p ≤ X is heuristically T ≈ exp(C(log X)^{1/3}).
  * This is an L[1/3]-type running time.
  * The campaign's 1/4 is the proved part and 1/3 the heuristic ceiling (OMEGA13 §3 remark).
  * Assessment.

**(R2) Factoring per slice: the data look polylogarithmic (EVIDENCE).**
* Let Tf(p) := min t in Lemma 1.1, where each t costs one factorisation of tp+1. Given the factorisation, a
  divisor m ≡ −1 (mod t) with 4 | m is found by dynamic programming over the residues mod 4t of partial divisors, in
  time O(Σ(e_i+1)·t). So the cost is Tf(p)·(poly(log p) + FACTOR).
* `scripts/bs_logic_mimic.py`: 60 primes per row, p ≡ 1 (mod L_y), L_y = 8∏_{3≤ℓ≤y} ℓ. These primes are
  squares modulo every ℓ ≤ y, i.e. they are deep into the square-mimicking regime of Theorem C.

| y | p ≈ | W mean / max | Tf mean / max |
|---|---|---|---|
| 7 | 1.3e5 | 28 / 143 | 10 / 79 |
| 13 | 1.0e8 | 41 / 119 | 8 / 47 |
| 19 | 3.1e10 | 56 / 279 | 8 / 63 |
| 23 | 6.8e10 | 82 / 559 | 9 / 35 |
| 29 | 7.1e12 | 94 / 383 | 9 / 47 |

  * W was searched up to M ≤ 6·10⁴ and Tf up to t ≤ 3000; no value was censored.
  * As square-mimicry deepens, the table witness W grows. The factoring witness Tf stays flat: the factors
    of tp+1 are not controlled by p mod L.
  * Sequential records over all 4519 hard primes < 2·10⁶ (`scripts/bs_logic_search.py`) are
    W = 383 (p = 1853329) and Tf = 367 (p = 830041); the latter matches CONDITIONAL_ES's EVIDENCE.
    Records come from small p, where tp+1 has few divisors.
* **CONJECTURE FQ.** Tf(p) ≤ (log p)^{A} for all primes p ≥ 5. Under FQ, ES-SEARCH ∈ FP^{FACTOR} ⊂ FBQP, and
  classically it runs in time L_p[1/3] via NFS.
  * Known lower bound: Tf is unbounded under Hypothesis H (Theorem M: any fixed finite slice set fails
    infinitely often), and ck_min ≫ log p·log₃p i.o. for the Type I slice family.
  * So FQ is the computational form of escape hatch E1 (a p-dependent, unbounded family of consulted
    integers) with a polylog budget.

**(R3) Factor leakage (EVIDENCE, `scripts/bs_logic_factorleak.py 4000`).**
* Over all 82 semiprimes n = pq ≤ 4000 with n ≡ 1 (24), p, q ≥ 5, we enumerated *all* solutions. A solution
  is "non-revealing" if every denominator has gcd ∈ {1, n} with n.
* **Every n with p ≠ q has a non-revealing solution. Every square n = p² has none.** The square case is
  ET Prop 1.6 (f_I(m²) = f_II(m²) = 0): every solution at an odd square descends through m, so it reveals m.
  That leak is useless, since √n is easy.
* So an adversarial ES oracle can avoid leaking factors of pq, and no factoring reduction comes from naive
  gcds. Random solutions leak with probability ≈ 90%, which proves nothing about worst-case hardness.
* Q3 (ES-SEARCH ≥ FACTOR?): no evidence for it. Q2 (ES-SEARCH ≤ FACTOR): heuristically yes (R2).

**Barrier screen.**
* *B1.* R1 *is* B1 in complexity language. R2 is outside B1 only because it consults p-dependent integers
  (E1). It proves nothing pointwise.
* *B2.* Each factoring slice is a divisor-class lottery, and FQ asserts that the first polylog many slices
  contain a winner. That is exactly the per-slice lottery H-A/H-B, now with a polylog *number* of slices
  rather than a fixed finite set. Proving FQ is at least as hard as proving ES (FQ ⇒ ES). Collapse:
  **FQ = (B2 lottery with a polylog moving set of slices)**.
* *B3.* No main term is involved; not applicable.
* *B5.* At n = m² every route through Type I/II is empty, so any ES-SEARCH algorithm must factor or
  root-extract at squares. Lemma 1.1 applied to n = m² fails for all t, since it produces Type I solutions.
  The algorithm survives only by first testing whether n is a perfect power, which costs O(log n). The
  failing step is "slice t succeeds", which is false for every t at odd squares.
* *B6.* The data are averages and sampled maxima; FQ is pointwise and unproved.
* *Positivity/Skolem analogy.* Signed solutions are free, both in Z and in Shepherdson's model (see
  `logic_weak_arithmetic.md` C3); positivity is the whole problem. In Skolem/Positivity, hardness results
  show that *deciding* positivity encodes Diophantine approximation. Here the answer is believed always
  YES, so the analogy transfers no technique. **Collapses** (cosmetic analogy).
* *Verifying ES(n) for all n ≤ N.* Sieve-factor tn+1 over the arithmetic progression n ≤ N, for t ≤ T(N).
  This costs O(N·T(N)·log log N), so N·polylog under FQ. That is no better than what the campaign and
  Salez already do; sublinear verification would need a compressed description of the uncovered set,
  which by R1 has no bounded-modulus form.

## 4. Experiments

`scripts/bs_logic_search.py`, `scripts/bs_logic_mimic.py` and `scripts/bs_logic_factorleak.py`, all
described above. Their outputs are small and reproduced in the tables.

## 5. Viability Assessment: **PARTIAL**

* The by-products are a clean dichotomy, labelled as follows:
  * congruence-table search is not FP (PROVED modulo campaign Ω-results);
  * factoring-assisted slice search is polylog in the data and on square-mimicking primes (EVIDENCE);
  * Conj FQ ⇒ ES-SEARCH ∈ FP^{FACTOR} ⊂ FBQP (PROVED implication; FQ is a CONJECTURE that implies ES).
* The factor-leak dichotomy (EVIDENCE) also stands. One could conjecture that every pq with p ≠ q has a
  non-revealing solution; nothing here depends on it.
* As a route to ES, this collapses to B2 (H-A with a polylog moving slice set).
* Next step, if anyone wants it: does S¹₂ + "FACTOR is total" prove ES under any natural extra axiom?
  That axiom would be FQ itself, so it is circular. No further work is recommended.
