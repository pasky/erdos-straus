# BRAINSTORM O153 — wildcard angles on Erdős–Straus (list + pre-screen)

Author: side agent O153 (branch `side-agent/bs-wildcard`). All verdicts below are pre-screens (Assessment) unless a
memo is cited. Literature recalled from memory is marked *(unverified)*. Angles already owned by other agents
(function fields, logic/complexity, LLL, cubic/Markoff/elliptic, Farey/thin groups, identities, H-A/H-B, Rédei/
dynamics/motivic, GoN, p-adic, graphs/greedy, Dirichlet series, involutions) are avoided or only cross-referenced.

Notation: 𝓛 = log p. "Slice" = O132 Lemma 2.1 (one integer N_θ(p), divisor in a class mod q_θ).

---

**W1. Canonical invariants of p as algebraic seeds (units ε_p, class groups, Cornacchia representations).**
Every prime p ≡ 1 (4) carries data not determined by congruences: the fundamental unit ε_p = (t+u√p)/2 of ℚ(√p)
(negative Pell always solvable), the class numbers h(p), h(−4p), and the representations p = u² + dv² for every
d with (−d/p) = 1. Idea: build an ES solution as an explicit algebraic function of these seeds ("algebraic
forcing", not counting). *Pre-screen:* every ES parameter is ≤ p^{O(1)} while log ε_p ≍ √p typically; reps
p = u² + dv² are polynomial seeds and meet the odd-square test through Pythagorean pairs; residues of ε_p mod q
are Frobenius data (→ nonab_frobenius_redei D1). **Deep memo: `canonical_invariants.md`.**

**W2. A "hardness law": f(p) versus the small-prime profile of χ_p (and the Siegel-zero dichotomy).**
Hard primes are square classes mod 840, i.e. χ_p(q) = +1 for q ≤ 7. Conjecture a quantitative law
f(p) ≈ C 𝓛³ · Φ(χ_p|_{q≤y}), linking ES-hardness to large values of L(1, χ_p) (Littlewood/Granville–
Soundararajan extremes), and ask whether the classical "illusory world" dichotomy (GRH-world / Siegel-zero world,
as in Heath-Brown's twin-prime theorem) can be run. *Pre-screen:* as a route this is counting (B2) and the Siegel
world makes the *easy* primes easier; as a law it is new EVIDENCE refining the mod-840 picture and predicting
how close to sterile a prime can get. **Deep memo: `hardness_law.md`.**

**W3. Non-counting argument shapes: compactness, descent, overspill, minimal counterexample.**
(a) Compactness in Ẑ: a compact-open set of residues is ET-covered by finitely many classes iff it contains no
sterile profinite point. (b) Descent on a defect (Fermat/Euclid/Lagrange template). (c) Nonstandard overspill
from a hypothetical infinite family of counterexamples. (d) Minimal counterexample: use ES(n) for n < p.
*Pre-screen:* (a) is Thm M / the MORDELL13 programme; (b) needs a composition law, and the only group structure on
the ES variety is the split torus G_m² (GEOMETRY_ES); (c) reduces to (a); (d) needs a transfer ES(n) ⇒ ES(p),
closed (H-G). **Deep memo: `noncounting_shapes.md`** (with a precise "where the integer enters" lemma).

**W4. Structured numbers in *every* short interval (Harman, Matomäki–Radziwiłł smooth numbers).**
Unlike almost-all results, "every interval [x, x + x^{1/2+ε}] contains an x^ε-smooth number" is a fixed-p
theorem *(unverified exponents)*. Apply to N_e = (p+e)/4, e ≤ E. *Pre-screen:* COLLAPSES to B4: certificates
need e ≤ p^{o(1)} (PIGEONHOLE Lemma 2.3) and forcing k small prime factors into one N_e costs
e ≥ e^{(1+o(1))k log k} against the 3^{k+1} products needed (PIGEONHOLE Lemma 2.1); every-interval results start
at length ≈ p^{1/2}, a power too long. No memo beyond this paragraph.

**W5. Many-term → three-term merging.** 4/p has p^{c}-many 4-term representations (power mass); ES(p) ⟺ some
4-term representation has two terms merging (1/z + 1/w = 1/v). *Pre-screen:* COLLAPSES to B3: each 3-term
solution has many 4-term splittings, so the merge event is the same polylog lottery seen through a large fibre;
LONGSHOT_FIBRED Thm 3.1 (fibre factor cancels).

**W6. Entropy / optimal transport.** Prove that a "no solution" configuration of the joint residues of the prime
factors of {N_θ(p)} has entropy deficit, contradicting an entropy lower bound. *Pre-screen:* COLLAPSES to B6/B2:
the only fixed-p randomness available (Hecke/Galois orbits) is Planck-scale ((I)3); an entropy lower bound for the
residues of prime factors of ≍𝓛³ specific integers is a parity-type statement (H-B).

**W7. Gowers norms / nilsequences on factorisation patterns.** Green–Tao–Ziegler count linear patterns
weighted by multiplicative functions. *Pre-screen:* COLLAPSES to B6: they average over the free variables of
the linear forms, at scale → ∞; at fixed p the event family has only ≍𝓛³ effective members of O(1) mass each
(redteam-2 §3.1), no long linear structure to average.

**W8. ES as a constraint-satisfaction problem with a phase transition.** *Pre-screen:* ES(p) is a single
*disjunction* of ≍𝓛³ events (a 1-DNF), not a random k-SAT formula; no phase transition exists; the random
model only reproduces ET's heuristic P(fail) ≈ exp(−c𝓛³) (B6). Collapses at the modelling step.

**W9. Vojta / Nevanlinna / Siegel-type integral-point theory.** *Pre-screen:* wrong direction. These theories give
finiteness or degeneracy of integral points (upper bounds); BL / GEOMETRY_ES Thm 3.1 (only lines carry infinitely
many integral points on U_n) is consistent with Vojta and proves nothing about existence. Collapses (B2/F-H).

**W10. Positivstellensatz / SOS / cutting-plane duality.** A sterile p would have an infeasibility certificate
for a bounded integer program (Chvátal–Gomory cuts). *Pre-screen:* real-algebraic certificates cannot see
integrality (the real fibre is a nonempty 2-dimensional region for every n); proving that no CG certificate of
bounded rank exists for a specific instance is a proof-complexity lower bound for a single instance—no
technology; overlaps logic_complexity. Collapses.

**W11. Proof mining of the density proofs (Kohlenbach).** *Pre-screen:* the ET / campaign density arguments are
already effective; proof mining extracts rates, i.e. exceptional-set bounds, never a pointwise statement (B6).

**W12. Half-integral weight / Shimura lifts of the Type I/II generating series.** *Pre-screen:* COLLAPSES to
B2/B5: the series are Eisenstein with no cusp part ((I)4 Props 9.1–9.2, (I)5); Shimura lifts of Eisenstein series
are Eisenstein, and the genus pairing cancels exactly at odd squares.

**W13. Heights / Mahler measure / Siegel's lemma for small solutions.** *Pre-screen:* Siegel's lemma produces
small solutions of *linear* systems; the ES equation linearises only after fixing two coordinates (a slice, B2), and
box-principle collisions give only signed solutions (PIGEONHOLE Lemma 1.3). Collapses.

**W14. Quantum algorithms.** Grover / period finding speed up search for witnesses. *Pre-screen:* algorithms
verify, they do not prove; overlaps logic_complexity. Collapses.

**W15. Weighted zero-sum theory (Davenport constant with target −1 and weights ±1 in (ℤ/e)^×).** *Pre-screen:*
COLLAPSES to B4: = PIGEONHOLE Prop 1.4 (Kneser) — covering needs ≳ log₃|G| generating primes per N_e, which
the integers N_e need not have (and, by Thm 2.2 there, fail to have for a positive proportion of p).

**W16. Tensor rank / algebraic complexity of the cubic 4xyz − nw(xy+yz+zx).** *Pre-screen:* rank, border rank and
the singularity type are invariants over a field, constant in n outside finitely many primes; they carry no
information distinguishing primes from odd squares (B1/B5). Collapses at once.

**W17. Euclidean descent in quaternion orders (Lagrange four-squares template).** Type II ⟺
(2ai + j)(2bi − j) = −e(1 + 2ck) in (−d, −p) ((I)6). Lagrange's proof finds an element of norm p by a Euclidean
algorithm in the Hurwitz order. *Pre-screen:* COLLAPSES: (i) the ES condition is a factorisation shape, not a norm
condition (QUATERNION_ES Props 2.2/3.2: residual split divisor problem); (ii) norm-Euclidean definite quaternion
orders are finitely many *(Fitzgerald-type classification, unverified)*, while the algebra here varies with p.

**W18. Dynamical zeta functions of e ↦ N_e = (p+e)/4.** *Pre-screen:* the map is affine, its "dynamics" is the
shift; any thermodynamic average over e is a legitimate fixed-p average but is exactly H-A. Collapses to B2.

---

Selected for full memos: W1 (`canonical_invariants.md`), W2 (`hardness_law.md`), W3 (`noncounting_shapes.md`).
