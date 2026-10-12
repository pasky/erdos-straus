# AGENT REPORT O142 — brainstorm: probabilistic / physics / additive-combinatorics angles

Branch `side-agent/bs-probabilistic`. Three memos under `BRAINSTORM/`, scripts `scripts/bs_prob_*`,
logs `logs/bs_prob_*.txt`. **No memo is LIVE.** ES is not solved; nothing here proves any case of it.

**(a) `BRAINSTORM/prob_lll_fixed_p.md`: LLL/Janson/Suen/Shearer at a fixed p. Verdict: COLLAPSES.**
Strongest reason: the atom lemma (Lemma 3.1 / Prop 3.2, PROVED, elementary). A probabilistic
bound certifies a single configuration only through an atom heavier than the bound, and there
are only three places to put the randomness:
* over θ at fixed p: the events are deterministic and disjoint, so all that is left is the first
  moment f(p) > 0, the B2 lottery;
* Haar over p: the atoms of (ℤ/Q)^× force a full covering, which is B1. Worse, the LLL proves
  the truncated avoider set is non-empty (OMEGA2), so the local lemma is a tool *against* ES;
* uniform over primes in (x, 2x]: this needs an exceptional set < 1, which is B6/T7, beyond
  GRH-quality error terms and capped at saving (log N)^{3/4} by the sieve-limit theorem (D)9.

Combinatorial Nullstellensatz, Chevalley–Warning and absorption have the same direction or
locality problem. Novelty: folklore-level logic, made explicit.

**(b) `BRAINSTORM/prob_lottery_model.md`: a statistical-mechanics model of the lottery. Verdict:
COLLAPSES as a proof route; useful EVIDENCE.** Strongest reason: the one proof-relevant
phenomenon, rigidity, is absent. Per unordered solution the bulk has number variance/mean
≈ 1.5 > 1, i.e. mildly positively clustered and Poisson-class, not determinantal. Exact f_II
counts to 10⁸ (new counter `bs_prob_fII.c`, matches R128b) give a two-level picture:
* a heavy-tailed part: e ≤ 16, only four shifted integers (p+e)/4, carries 40% of the mass and
  nearly all the variance;
* a compound-Poisson bulk (κ ≈ 3.06 in weight-2 units), calibrated within a factor 2 down to the
  10⁻⁵ lower-tail quantile. Model min bulk/L³ is 0.0021 against 0.00196 observed.

Predictions (Assessment): ≈ 0.02 sterile primes in [2²⁰, 3·10⁷], and ≲ 10⁻⁸ beyond 10⁸.

Further EVIDENCE:
* the square-class depression of the mean saturates near 0.5 (Q up to 2042040);
* the hardest primes have near-prime shifts (p+3)/4;
* f_I and f_II are **strongly positively** correlated (0.85 within cells mod 120120), so there
  is no conservation law;
* a common quenched driver is the divisor structure of p − 1 (corr ≈ −0.4 with log τ(p−1);
  every M | p−1 is a dead witness modulus).

**(c) `BRAINSTORM/addcomb_unit_fraction_density.md`: Croot/Bloom density methods. Verdict:
COLLAPSES to B3.** Strongest reason: Bloom's engine (Prop 1 of arXiv:2112.03726, checked against
the PDF) has every element ≥ N^{1−1/log log N}. So |S| ≥ N^{1−o(1)} terms, against 3. Its
circle method needs many multiples of each prime power of the lcm.
* At k = 3 the method's local-cancellation principle reproduces exactly ET's Type I/II
  parametrisation (known).
* The additive-looking e-slice condition a + b ≡ 0 (mod e) is purely multiplicative
  (a/b ≡ −1), so sum-product has nothing to act on (→ LONGSHOT_PIGEONHOLE Prop 1.4).
* Representation counts are p^{o(1)}, so no power-saving method applies.

**Caveats for the parent's review.**
* The (b) numbers are EVIDENCE and Assessment only.
* κ per dyadic range is biased downward at 2²⁰ (cells with ~3 primes).
* `bs_prob_model.py` / `bs_prob_euler.py` / `bs_prob_shifts.py` read a 3-field 10⁸ dump made by
  the first version of `bs_prob_fII.c`; the current 5-field build needs `reshape(-1,5)`.
* The large binary dumps were kept in /tmp, not committed.
* ET Thm 1.7 is cited from memory.
