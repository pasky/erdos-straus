# BRAINSTORM — greedy-type algorithm dynamics for 4/p (O150, angle b)

Labels as in DISCOVERIES.md. Script: `scripts/bs_graph_greedy.py`.

## 1. Idea

Egyptian-fraction algorithms are dynamical systems on ℚ ∩ (0,1). Examples are greedy (Fibonacci–Sylvester)
`r ↦ r − 1/⌈1/r⌉`, Engel `r ↦ r⌈1/r⌉ − 1`, and Golomb/Farey-predecessor `a/b ↦ a′/b′` with `ab′ − a′b = 1`.
The odd-greedy variant is irrelevant here: 4/n with n odd has no representation with three odd denominators,
since `n(xy+yz+zx) = 4xyz` has odd left side and even right side.

The question: is there a deterministic algorithm, or a family A_J indexed by a parameter J growing with p (escape
route E1), whose 3-term success set provably contains every large prime? A weaker target from the brief: an A_J
whose failure set is provably not a whole residue class.

## 2. Literature anchor

* Fibonacci–Sylvester greedy and Engel expansions are classical. Golomb's algorithm (1962) uses the Farey predecessor
  and gives at most a terms for a/b. From memory, unverified: Bleicher, Erdős–Straus problem surveys; Mordell's
  identities give all p ≢ 1 (24) and the classes 1, 121, 169, 289, 361, 529 (mod 840) remain.
* Campaign: POINTWISE_SIZE Thm M/C, Prop A (fixed procedures); POINTWISE_SIZE §8 window frame (Thm 8.1,
  Prop 8.4, Lemma 11.3); POINTWISE_XWIN (fixed-set stacking); notes Lemma 77.1.

## 3. Results

**Prop B.1 (PROVED, elementary).** For every prime p ≡ 1 (mod 24), the greedy, Engel and Golomb algorithms all
need ≥ 4 terms for 4/p.

*Proof.*
* *Greedy.* x = (p+3)/4 is odd (p ≡ 1 (8)) and ≡ 1 (mod 3). The remainder is 3/(px) with px ≡ 1 (3), so
  y = (px+2)/3 is odd and the remainder 2/(pxy) has odd denominator, so it is not a unit fraction.
* *Engel.* q₁ = (p+3)/4, r = 3/p. Then q₂ = (p+2)/3, r = 2/p, q₃ = (p+1)/2, r = 1/p ≠ 0.
* *Golomb.* 4/p = 3/b′ + 1/(pb′) with b′ = (3p+1)/4, which is odd and ≡ 1 (3). Then 3/b′ = 2/b″ + 1/(b′b″) with
  b″ = (2b′+1)/3 odd, and 2/b″ is not a unit fraction. ∎

These are Theorem M instances: the run is congruence-determined. Theorem C says that every fixed correct procedure
fails infinitely often on p ≡ 1 (24) (CONDITIONAL on H); here the failure is total and unconditional.

**Prop B.2 (PROVED; a dictionary).** Let G_J be the "offset greedy" algorithm. It tries x = ⌈p/4⌉ + j for
0 ≤ j < J, then any 2-term completion of `4/p − 1/x`. For p ≡ 1 (4) put
`J(p) := min{j : G_{j+1} succeeds}`. Then `J(p) = (a_min(p) − 3)/4`, where a_min is the window statistic of
POINTWISE_SIZE §8.

*Proof.* Put q = 4x − p = 3 + 4j. The candidate x < p is p-free. By notes Lemma 77.1, 4/p has a solution with
p-free denominator x iff `Rat_q(x) ∩ {−1,−p} ≠ ∅`, which is the window condition at q. ∎

So every statement about the window frame transfers verbatim to the most natural growing-parameter algorithm
family:
* ES ⟺ J(p) < ∞ (Thm 8.1).
* For every K, J(p) > K for infinitely many p (Prop 8.4, CONDITIONAL on Dickson). So no fixed J suffices; this is
  the B1 statement for this family.
* Failure of G_J is never congruence-forced (Lemma 11.3, PROVED). The brief's weaker target, "a family whose failure
  set is provably not all of a residue class", is therefore already met. It is worthless for ES: it is a statement
  about *some* primes in each class, not all.
* Two-sided density of failures: `#{p ≤ N : J(p) ≥ K} ≪_K π(N)(log N)^{−J′(K)/2}` (XWIN Thm 1.2), and orders
  are known for K ≤ 2 (W1/W2, Cor 1.4).
* The sufficient conjecture is X_win(C): J(p) ≤ (C/4) log p. Data: J/log p < 2.5 to 10⁸ (EVIDENCE, POINTWISE_SIZE
  §8). The random model gives J ≍ log p/log log p.

**Remark B.3 (nondeterministic dynamics).** The full nondeterministic greedy tree (any x in the admissible range at
each step) is the complete solution enumeration, which is ET's parametrisation. Any pruning by a fixed rule is a
Theorem-M procedure (B1); pruning by a rule with growing width is the e-slice lottery (B2/H-A). No algorithm class
was found between these two.

## 4. Experiment (`bs_graph_greedy.py 300000`)

* The 3 202 primes p ≡ 1 (24) below 3·10⁵: greedy, Engel and Golomb succeed in 3 terms for 0 of them (Prop B.1).
* Distribution of J(p): 0: 1627, 1: 1235, 2: 211, 3: 38, 4: 43, 5: 32, 6: 3, 7: 11, 9: 1, 14: 1. The maximum
  is J(118801) = 14, i.e. a_min = 59, consistent with the window census.

## 5. Barrier screen

* **B1.** Fixed algorithms are covered by Theorem M/C, and greedy/Engel/Golomb fail on all of p ≡ 1 (24) outright.
* **B2.** G_J at fixed j asks whether Rat_q((p+q)/4) contains −1 or −p: whether one integer has a divisor pair in
  a residue class mod q. This is the divisor-class lottery with q in the solution.
* **B3.** Each window succeeds with probability bounded away from 1, so J must grow (random model
  log p/log log p). There is no main term to certify.
* **B5.** At n = m², G_J (with the p-free reading) fails for every J, since Type I/II are empty. The step that fails
  is "Rat_q(x_q) ∋ −1 or −n for some q". ES(m²) holds only through denominators divisible by m.
* **B6.** The density statements (XWIN) are averages over p; at a single p they say nothing.

## 6. Viability Assessment

**COLLAPSES** to B1 (fixed algorithms: Prop B.1, Theorem M/C) and, for growing-parameter families, exactly to the
window frame (Prop B.2) and hence to B2. The parameter J(p) of the natural algorithm family *is* `(a_min − 3)/4`.
By-products: Prop B.1 (folklore-level, PROVED) and the dictionary B.2 (PROVED, elementary). Neither is new in
substance.
