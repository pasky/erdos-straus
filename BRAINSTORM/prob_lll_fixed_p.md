# Brainstorm memo: Local-Lemma / Janson-type existence at a FIXED prime (O142(a))

Status labels as in DISCOVERIES.md. ES is not solved; nothing here proves any case of it.
Verdict up front: **COLLAPSES** (to B2 at fixed p, to B1 in Haar space, to B6/T7 in prime space).
The by-product is a three-way "placement-of-randomness" lemma that makes the collapse exact.

## 1. Idea

The events `A_θ(p) = "slice θ has no Type I/II solution at p"` are dependent: they share small
primes (θ's moduli `f_θ` share factors) and genus characters (`(p/f) = −1` for every Type II
witness). The hope: a dependency-sensitive inequality (Lovász Local Lemma (LLL), lopsided LLL,
Shearer, Moser–Tardos, Janson, Suen) yields a *deterministic* conclusion
`¬∧_θ A_θ(p)`, i.e. ES(p), at every large p, with the randomness over θ, not over p (T7).

For this to prove ES one needs a probability space (Ω,P), a point ω₀ that encodes "the actual
arithmetic at p", and a bound on the measure of the "all slices fail" set Z that excludes ω₀.

## 2. Literature anchor (from memory; standard; statements not re-checked against the PDFs)

* LLL (Erdős–Lovász 1975), lopsided LLL (Erdős–Spencer 1991), Shearer 1985 (the optimal
  dependency-graph bound), Moser–Tardos 2010 (algorithmic), Haeupler–Saha–Srinivasan 2011
  (conditional LLL; used in the campaign, DISCOVERIES (H)11).
  These are all **lower bounds** `P(∧ Ā_i) ≥ ∏(1 − x_i) > 0`, i.e. existence of an *avoider*.
* Janson 1990 / Boppana–Spencer, Suen 1990 (Alon–Spencer, *The Probabilistic Method*, Ch. 8).
  These are **upper bounds** `P(∧ Ā_i) ≤ exp(−μ + Δ/2)` (Janson) for events that are monotone in
  independent bits. They are never 0. The campaign has a one-hot Janson variant (OMEGA13 Thm 1.4,
  (H)-ledger; novelty "known method, new statement").
* The campaign already uses the LLL in the **anti-ES direction**: Haar avoiders and
  `W(p) ≥ (log p)^k` infinitely often (POINTWISE_OMEGA2/3, DISCOVERIES (H)11–(H)13). The Haar
  avoider density satisfies `δ*(T) > 0` (OMEGA2 Thm 11.3 gives `log(1/δ*(T)) ≤ T^{o(1)}`).

## 3. The exact collapse (PROVED, elementary)

**Lemma 3.1 (atom lemma; PROVED, trivial).** Let Z ⊆ Ω be measurable and let ω₀ ∈ Ω.
(i) If `P({ω₀}) > β` and `P(Z) ≤ β`, then ω₀ ∉ Z.
(ii) If `P({ω₀}) ≤ β`, the bound `P(Z) ≤ β` does not decide whether ω₀ ∈ Z, because the
set Z' = {ω₀} also satisfies `P(Z') ≤ β`.
So a probabilistic upper bound proves a pointwise statement **only through an atom heavier than
the bound**. LLL-type lower bounds can only prove that Z ≠ ∅, which is the anti-ES direction.

**Proposition 3.2 (placement of the randomness; PROVED).** There are three places for the
randomness, and each one collapses.

(a) *Randomness over solver choices θ at fixed p.* Take Ω = Θ(p), the (finite, p-dependent)
set of candidate parameters, with any measure of full support. Then each θ either works or it
does not. ES(p) ⟺ `P(S_p) > 0`, where S_p is the set of working θ. That is a first-moment
statement `Σ_θ w_θ 1[θ works] > 0`. If the slices partition Θ, the events are disjoint and
`P(no slice works) = 1 − Σ_i P(slice i works)` holds exactly. Dependency inequalities (LLL,
Janson, Suen) are non-trivial only for events that are monotone functions of a common
**product** randomness. Here there is none: the point θ is the whole randomness. So the
argument is the count `f(p) > 0`, which is the lottery of B2 (O132 Thm 2.2).

(b) *Haar randomness over p ∈ Ẑ (or the classes mod Q).* Ẑ has no atoms, so by Lemma 3.1(ii)
no measure bound decides a single p. The finite version, Ω = (ℤ/Q)^× with atoms `1/φ(Q)`,
needs `P(Z_Q) < 1/φ(Q)`, i.e. `Z_Q = ∅`. That says the witness classes mod Q **cover** every
unit class, which is B1 (POINTWISE_SIZE Thm M/C; covering certificates fail at the square point).
Worse, the LLL proves `P(Z_T) ≥ δ*(T) > 0` for the truncation to witnesses ≤ T (OMEGA2), so
Haar Z is never empty at any finite truncation. In this space the local lemma is a tool
*against* ES.

(c) *Randomness over primes p ∈ (x, 2x], uniform.* Atoms have mass `1/π(x)`. Lemma 3.1(i) needs
`#{p ∈ (x,2x] : ES(p) fails} < 1`, an exceptional-set bound **below 1**. Any Janson/Suen run
in this space must input the joint distribution of primes in the classes `−4a²d (mod f)` for
pairs of moduli. The best available error bounds are BV's `x/(log x)^A` and GRH's
`x^{1/2}(log x)²` per modulus. Summed over the moduli used, neither is ever < 1. On the majorant side, CRT/Haar majorants save
at most `C(log N)^{3/4}` against the `log N` needed to go below 1 (sieve-limit theorem,
EXCEPTIONAL_THETA Thm 2.5 / Cor 3.4, DISCOVERIES (D)9). This is B6/T7: an average over p says
nothing at a single p unless the total is < 1, and that is out of reach by a power of x.

*Proof.* (a) If each θ ∈ Ω is deterministic in p, then `P(∧_i Ā_i)` is computed from one
indicator per point; disjointness gives the exact formula. (b) Lemma 3.1 with atom
`1/φ(Q)`; positivity of `δ*(T)` is OMEGA2 Thm 11.3 (at each finite T, Z_T is a non-empty union
of classes). (c) Lemma 3.1 with atom `1/π(x)`, together with the cited sieve-limit theorem;
the GRH error size is the standard `x^{1/2}(log x)²` per modulus. ∎

**Remark 3.3 (hidden product structure?).** The only way to get product randomness at fixed p
is to treat the *unknown factorisations* of the integers `N_θ(p)` as random. That is a
heuristic model (memo `prob_lottery_model.md`), not a probability space containing the true p as
an atom. Making it rigorous at one p means proving that this deterministic factorisation
behaves like its model, i.e. H-A/H-B again.

**Remark 3.4 (other deterministic-existence tools; Assessment).** The other combinatorial
existence principles have the same direction problem.
* Combinatorial Nullstellensatz (Alon 1999) proves **non-vanishing** somewhere in a grid
  (avoidance). ES needs vanishing of `4xyz − p(xy+yz+zx)`.
* Chevalley–Warning / Ax–Katz give zeros **mod q** only. For ES the local zeros always exist
  (the Brauer set is non-empty, BL Thm 1.8), and they exist at odd squares too (B5).
* Rödl nibble and absorption build global coverings, which is B1.
* Ramsey/density-type hitting theorems need many variables or positive density (memo
  `addcomb_unit_fraction_density.md`).

## 4. Barrier screen

* **B1:** (b) is literally a covering statement mod Q; Thm M/C applies.
* **B2:** (a) is the per-p count; no dependency structure exists to exploit.
* **B3:** (c) needs main term `M = μ(p) ≍ log³p` (fine) but an error below the atom `1/π(x)`.
  The scale-constraint obstruction appears in the form "equidistribution at granularity 1/x".
* **B4:** not used.
* **B5 (odd squares):** in (b) and (c) the false step is the measure bound itself: Z contains the
  Ẑ-closure of the odd squares, a closed null set. In Haar language that is the "square point"
  of Thm C, which lies in Z at every finite truncation. In (a) the step that would fail at
  `n = m²` is `f(m²) > 0`, and that is the whole content.
* **B6/T7:** (c) is the average leak by construction. The atom lemma makes it exact: averages
  help only if they are < one atom.
* **T2:** Janson's `exp(−μ+Δ/2)` is a group bound (kind (b) of redteam Prop 2.1), but it is
  valid only in a product space. At fixed p there is none.

## 5. Small experiment

None was needed: the collapse is logical. The quantitative inputs (`δ*(T) > 0`, the sieve-limit
cap) are already PROVED in the campaign.

## 6. Viability

**COLLAPSES**: to B2 at step "randomness over θ" (Prop 3.2(a)), to B1 at step "Haar atoms"
(3.2(b)), and to B6/T7 plus the sieve limit at step "prime atoms" (3.2(c)).

By-product: Lemma 3.1 / Prop 3.2 (PROVED, elementary). This is a clean statement of why
LLL-type existence methods point **away** from ES. The campaign's successful uses of the local
lemma (OMEGA2/3, Ω-results for W(p)) are exactly the avoider direction. Novelty: folklore-level
logic, made explicit; not worth a paper on its own, but a useful line for the barrier note.

## Errata (triage O156/O157)

Appended by O160; the memo body above is unchanged. Source: reviews/triage-brainstorm-B.md (§0.3 and the per-memo
paragraph). Counterexamples re-verified by `scripts/errata_check.py` (tag in brackets).

* **Prop 3.2(a) / Remark 3.3 are false as general claims** (fixed-p choices cannot carry product randomness;
  dependency inequalities need monotone events). Counterexample [LLL]: Θ = {0,1}⁶ uniform, B_i = {θ_{2i−1} = θ_{2i}},
  i = 1,2,3: the B_i are independent and non-monotone, and LLL (here exactly) gives P(avoid all) = 1/8 > 0.
  Determinism of each candidate's arithmetic outcome is no obstruction: the probability space is over solver
  choices θ. The Janson/Suen monotonicity requirement applies to those inequalities, not to the symmetric/asymmetric LLL.
* Lemma 3.1 (atoms) correctly limits what a measure bound alone says; it does not exclude probabilistic existence.
* Redteam-automorphic-2 Thm 2.2(iii) excludes only Θ₀ fixed independently of p (CONDITIONAL on H).
* **Corrected verdict:** PARTIAL → H-A (displayed instantiations collapse). Open: independent solver coordinates at
  fixed p with arithmetic bounds P(B_i) ≤ x_i ∏_{j∼i}(1−x_j), uniformly in large p — none constructed.
