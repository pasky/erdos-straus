# Technique-transfer audit for Erdős–Straus (O155)

Status: brainstorm memo, internal, not refereed. ES is not solved; nothing here proves any infinite case of it.

**Common frame.** Fix a prime p ≡ 1 (mod 24). Every encoding reduces to a family Θ(p) of events
"N_θ(p) has a divisor in a class modulo q_θ" (B2). The cleanest binary sub-family is the (A)3 slice

  R(p) = #{(A,B) ≥ 1 : 4AB | p + A + B}  (⇔ B | p+A, 4A | p+B, 4 | p+A+B; ES(p) ⇐ R(p) ≥ 1),

whose θ = A event is "p + A has a divisor B ≡ −p (mod 4A)". The common quantitative fact is the
**1/|θ| law** (EVIDENCE + heuristic, quantified in `tech_maynard_theta.md` §4): per θ in a dyadic block
θ ~ H the success probability is ≍ τ-type(p)/H. So every dyadic block of θ holds O(polylog p) expected
winners, whatever H is. A technique "transfers" only if it can produce a lower bound for a sum whose total
main term is polylog(p), at one p. Each paragraph below states the mechanism, the exact analogue, and the
first failing step (B1–B6, T1–T8 as in the brief).

1. **Maynard–Tao sieve weights (bounded gaps).** *Mechanism:* weights w(n) = (Σ λ_d)² over n ~ N.
   Bombieri–Vinogradov level of distribution gives asymptotics for Σ w and Σ w·1_P(n+h_i). The ratio
   exceeds m because primes have density 1/log N and the weights boost it by log k. *Analogue:* n := θ,
   with p fixed. This is a legitimate averaging variable, not a T7 leak. "Some of k forms is prime"
   becomes "some N_θ(p) has a divisor in its class". *Breaks:* at the density hypothesis. Maynard's sieve
   (also the "dense clusters in subsets" form, Maynard 2015/16, from memory) needs the target set to have
   density ≥ (log X)^{−O(1)} in the θ-range plus a power-saving level of distribution. Here the density is
   ≍ polylog(p)/X, so main term ≤ polylog(p) while the error is X^{1−δ}. This is **B3** (scale) at the step
   "error ≤ main term". Weights that force N_θ to be divisible by small primes are congruence conditions
   on θ at fixed p. They pay a measure factor 1/M for a multiplicity gain ≤ 3^{ω(M)}, so there is no net
   gain (**B4**; LONGSHOT_PIGEONHOLE Thm 2.2). Full memo: `tech_maynard_theta.md`.

2. **Zhang / Polymath level of distribution beyond 1/2 for smooth moduli; BFI well-factorable weights.**
   *Mechanism:* Σ_{q ≤ x^{1/2+ϖ}, q smooth} |π(x;q,a) − π(x)/φ(q)| ≪ x/log^A x. It averages over the primes
   up to x in each progression. *Analogue:* choose the Type II witness moduli 4cd (or 4A) smooth. Then the
   forced classes have well-factorable moduli. *Breaks:* pointwise it is a **T7/B6** leak: it averages
   over p. For the exceptional set it changes only the admissible modulus range of a CRT majorant. The
   campaign proved those majorants capped at (log N)^{3/4} at any level and with any modulus shape
   ((D)18, (D)24, (D)19 large sieve). So it gives no improvement of (B)11. Full memo: `tech_smooth_level.md`.

3. **Tao entropy decrement (Erdős discrepancy, log-averaged Chowla).** *Mechanism:* the entropy of
   blocks (g(n+1),…,g(n+H)) at a random n is bounded and decreases across scales. So at some scale the
   block is nearly independent of n mod q, and multiplicativity g(qn) = g(q)g(n) transports the
   statement. *Analogue:* a block of slice events {N_θ(p): θ ∈ [H,2H]}, with ES multiplicativity
   ES(m) ⇒ ES(mk). *Breaks:* the argument needs a *random location* n averaged over [1,X]. At fixed p there
   is one location, so it is **B6/T7**. Multiplicativity runs the wrong way for primes: p has no proper
   factors to transport from. Collapses at "choose n at random".

4. **Matomäki–Radziwiłł (multiplicative functions in short intervals).** *Analogue:* the slice integers
   p + A, A ≤ H, form a short interval at p. *Breaks:* MR controls almost all intervals [x, x+H], which is
   **B6** with x = p. The relevant statistic, "divisor in a class mod A", is not a bounded multiplicative
   function of p + A because the modulus moves with A. Pre-screened as W4 (B4); same conclusion.

5. **Green–Tao transference / dense models.** *Mechanism:* a set A of positive relative density in a
   pseudorandom majorant contains the expected patterns. *Analogue:* the set of winning θ. *Breaks:* wrong
   quantifier. GT *assumes* |A| is large (a lower bound) and produces structure inside A. ES asks
   |A| ≥ 1, and |A| ≍ polylog(p) inside a θ-range of size X, so there is no positive-density model.
   Collapses to **B3** at "relative density > 0".

6. **Helfgott-type explicit analytic tail + finite check.** *Mechanism:* an analytic count with explicit
   error, positive for N > N₀, plus a computer check below N₀. *Analogue:* "f(p) ≥ 1 for p > P₀" plus
   the EVIDENCE check to 10⁸. *Breaks:* there is no pointwise analytic statement for any P₀. The
   circle-method analogue for 4ABC − A − B = p is a cubic in 3 variables (far below Birch/Heath-Brown
   variable counts). Its main term is polylog(p) and no error term is known below p^{ε}, so **B3**.
   By-product remark: Theorem F (B1) means even a hypothetical P₀ would have to come from non-congruence
   input. The finite check cannot close any gap that bounded search leaves open.

7. **Guth–Maynard large values / zero density.** *Breaks:* it improves primes in almost all short
   intervals and zero-density exponents, so it is **B6** pointwise. For exceptional sets, zero-density
   enters the (A)/(B) chain only through prime counts in progressions of moduli ≤ exp(c√log N). There the
   3/4 cap is structural ((D)17–(D)24), not analytic. No gain.

8. **Maynard, primes with restricted digits.** *Mechanism:* a thin set (density x^{−c}) whose Fourier
   transform factorises and has small L¹ norm. *Analogue:* the winning-θ set or the ES-good primes in a
   thin set. *Breaks:* the product structure of the digit set is what is used. ES-good θ at fixed p have
   no known Fourier structure; their structure *is* the lottery (**B2**). ES-good primes are density 1,
   so "infinitely many ES-good primes in any thin set with a Maynard-type theorem" follows trivially
   only when the thin set's ES-failure density is controlled, which is again (A)-type averaging. No new
   content.

9. **Hooley / Duke–Friedlander–Iwaniec divisor sums and root equidistribution for quadratics.**
   *Analogue:* Type I, f | p² + 4c²d with f ≡ −p (mod 4cd). *Breaks:* DFI equidistributes ν/f for roots of a
   *fixed* polynomial on average over f. Hooley-type sums Σ_c τ(p² + 4c²d) are not known uniformly in the
   constant term p² in the needed range (redteam-2 H-A). Most decisively, the condition f ≡ −p is a class
   modulo a modulus tied to the variable c (moving modulus). Collapses to **H-A/B2**.

10. **Heath-Brown square sieve.** *Tempting:* T1 says ES Type I/II fails at squares, and sterile primes
    "mimic squares". If avoidance of all forced classes forced (p/q) = +1 for all q ≤ Q, Burgess-type
    least-non-residue bounds would give ES. *Breaks:* the avoider set is not a square-class condition. Its
    residue density decays like exp(−c(log)^{3/4}) ((D) chain), far more slowly than square classes
    (2^{−ω}), and it is pure congruence data (**B1**, Thm M/Prop A). The square sieve is an upper-bound
    tool besides. Collapses at "avoidance ⇒ quadratic residuosity".

11. **Friedlander–Iwaniec / Heath-Brown asymptotic sieve with bilinear (Type II) input.** This is the
    closest in spirit (redteam-2 **H-B**). *Breaks (Assessment):* bilinear forms need long sums with a
    smooth main term. Here every dyadic block carries O(1) expected mass (1/|θ| law), so a bilinear
    decomposition has nothing to dominate. The target event is also "divisor in a moving class", not a
    parity-sensitive prime indicator. **Open, no technology** (H-B as already recorded).

12. **Kahn–Kalai / Park–Pham thresholds.** At fixed p, "ES(p)" is a disjunction of explicit,
    non-random events. There is no product measure, so no threshold statement applies. The randomised
    model gives first moment ≍ log³p, but that is the lottery heuristic (`prob_lottery_model.md`).
    Collapses to **B2/B6** at "introduce randomness".

13. **Granville–Harper–Soundararajan pretentious methods.** The slice event at one N is
    (1/φ(e)) Σ_χ χ(−1)|Σ_{d|N} χ(d)|²-type, i.e. a finite product over the prime factors of N. Its failure
    is exactly "the primes of N generate a subgroup avoiding −1" ((C)21–(C)25). Pretentious mean values
    average over N (**B6**). At a single N it is the finite combinatorics already in (C). **B2.**

14. **Bourgain–Gamburd expansion / affine sieve; Lindenstrauss measure rigidity/AQUE; Pila–Zannier;
    Dimitrov–Gao–Habegger.** Already screened: `thin_group_orbits.md` (B3),
    `nonab_homogeneous_dynamics.md` (B3), `logic_ominimal.md` (upper bounds only). DGH bounds rational
    points on curves *from above* uniformly, which is the wrong direction for existence.

15. **Polynomial method / slice rank / Huang sensitivity / Kelley–Meka.** Slice rank and Kelley–Meka are
    upper bounds for dense sets avoiding patterns. ES success sets are sparse, and ES asks for existence,
    not avoidance. See `polynomial_method.md` (B4/B3). Huang's sensitivity theorem has no ES structure
    (cosmetic analogy).

16. **Bhargava / geometry-of-numbers counting in families; Kedlaya-style averaging.** Average over the
    family parameter (discriminant ↔ p): **B6/T7**. The analogue over θ at fixed p reduces to counting
    lattice points with moving congruence (`gon_*` memos, B2).

17. **Motivic positivity (Brown, Kontsevich).** `nonab_motivic_pointcounts.md`: the motive of U_n is mixed
    Tate, so there is no non-trivial Galois input. Collapses.

18. **Iwaniec P₂ values of n² + 1 (lower-bound sieve beyond level 1 via bilinear forms).** It produces
    numbers with *few* prime factors. ES wants N_θ(p) with *many* or well-placed factors (a prime N_θ
    kills the slice), so the direction is opposite. The upper-bound sieve form only bounds how many θ are
    bad. **H-B.**

**Strongest transfers chosen for full memos:** (1) Maynard–Tao with θ as the averaging variable,
(2) smooth-moduli level of distribution. Both collapse; see the memos.
