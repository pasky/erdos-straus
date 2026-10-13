# bsD_genus_vacuity_LDp — (LD_p) as reduction theory on the genus of Gross lattices: the genus is vacuous, a fixed lattice is decided by ternary representation theory (O177)

**ES is not solved here.** Labels as in DISCOVERIES.md. Deep version: LDP_DEEP.md §B.

## Idea
Direction (b): O176's (LD_p) — "some maximal order O ⊂ B_{p,∞} has trace-zero x, y, ⟨x,y⟩ = 1, with
4h | gcd(h, G)², h = (nrd x·nrd y − 1)/p, G = gcd(nrd x + 1, nrd y + 1)" — as a successive-minima / Minkowski /
mass-formula statement over the ≈ p/12 orders that must use |Diff| = 1.

## Literature
DIFF_DEEP Thm 1.1, 2.1 (O176); Siegel mass formula for representations of binary by ternary lattices (Siegel 1935;
Kitaoka, *Arithmetic of Quadratic Forms* (1993), §6.8); Gross, *Heights and special values of L-series* (1987)
(Gross lattices O⁰, Brandt matrices); Duke–Schulze-Pillot, *Representation of integers by positive ternary quadratic
forms and equidistribution of lattice points on ellipsoids*, Invent. Math. 99 (1990) (large n, spinor exceptions);
Schulze-Pillot, *Representation by integral quadratic forms — a survey* (2004); Ellenberg–Venkatesh, *Local-global
principles for representations of quadratic forms*, Invent. Math. 171 (2008) (codimension conditions).

## Statement
**Prop 1 (genus vacuity; PROVED from DIFF_DEEP Thm 1.1).** (LD_p) holds ⟺ there is an integral binary
T = [[f,1],[1,f′]] > 0 with p | ff′ − 1 and 4h | gcd(h, G)² (the arithmetic Type II statement of DIFF_DEEP Thm 2.1).
*Proof.* Every such T has Diff(T) = {p} (KUDLA_ES Thm 1.4), hence by Thm 1.1 is the Gram matrix of a pair in some
O⁰. ∎ So no reduction-theoretic or mass-formula statement about the genus can add information: the Siegel mass
Σ_O r(O⁰, T)/|O^×| is a positive local-density product for **every** certificate-shaped T (Diff = {p} ⇔ all local
densities positive), and the genus-level problem is *exactly* the existence of the integer matrix T — the slice lottery.
**Remark 2 (a fixed order is a lottery at every determinant; Assessment, with a corrected first draft).** A primitive
binary T ↪ O⁰ corresponds to a primitive v ∈ (O⁰)^# (orthogonal complement) with Q(v) determined by det T, *and*
the isometry class of v^⊥ must be T. Duke–Schulze-Pillot controls only the first (representation of the number);
the second is a "mixed" equidistribution problem (Aka–Einsiedler–Wieser, *Joint equidistribution of CM points*, Ann.
Math. 195 (2022), and its sublattice versions): the ≍ h(−4 det T)·(local factors) vectors v spread their complements
over ≍ h(−4 det T) binary classes, so a *given* T is represented O(1) times on average over the genus (R177 repair: the genus total is a divisor-type
ρ(T) = p^{o(1)} spread over ≈ p/12 orders, so ≈ 12ρ(T)/p per fixed O⁰ — heuristic). [First draft
claimed "every T is represented by every O⁰ for det T ≥ p^C" via Duke–Schulze-Pillot — **false**: DSP represents the
number, not the binary form.] So "∀ O" and "a fixed O" are lotteries at all determinants (consistent with O176 §2.5).
**Prop 3 (Minkowski/Siegel-lemma constructions miss by f^{3/2}; = DIFF_DEEP Prop 2.3–2.4).** Successive minima of
the 6-dimensional lattice of pairs (x, y) ≡ (x₀, y₀) (mod M O⁰) give pairs with level M and nrd ≪ M²p, but the
*exact* condition ⟨x, y⟩ = 1 plus det T ≤ pM²/4 is a codimension-2 exactness condition on a 6-dim lattice — the scale
barrier B3 in lattice form (gap ≍ f^{3/2}).

## Barrier screen
* **Hypotheses of Prop 1 → escapes.** (i) *Gram-matrix data*: add non-Gram data (orientations, level structures) —
  O176 §2–3: free (Prop 2.3) or a divisor condition (Type I). (ii) *∃ O*: replace by a *p-dependent canonical O* with an
  explicit basis (Ibukiyama O(q, r)) and look for explicit pairs: this is a polynomial-identity recipe (B1, Thm M/C) or
  a lottery (§2.5 EVIDENCE). (iii) *quadratic forms only*: higher-degree forms (cubic norm forms of degree-3 algebras)
  have trivial class sets over ℚ (bsD_eichler_degree_k Prop 2) — no genus to reduce.
* T1: Prop 1 holds for odd n in the form "∃ T with Diff(T) = {ℓ | n …}"; at squares Diff = ∅ and the genus of
  B_{∅} = M₂(ℚ) has no definite lattices — T1 enters exactly through Diff, as required, but adds no existence.
* B2/B3: Props 1–3.

## Assessment
PROVED reduction: **(LD_p) has no geometric content at the level of the genus** (Prop 1); at a fixed order it is
a lottery at every determinant (Remark 2, joint-equidistribution heuristics). Direction (b) collapses to the H-A core. Promise 1.
