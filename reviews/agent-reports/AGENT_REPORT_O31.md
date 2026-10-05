# AGENT REPORT O31 — Type-I `ck_min` beyond the Graham–Ringrose barrier

Branch `side-agent/typei-ckmin`. Deliverable: `POINTWISE_TYPEI.md` (§0 has
the results table). Scripts: `scripts/typei_*.py`. Data:
`data/pointwise_typei/ckmin_np_1e7.txt.gz`. Checkpoint 1; not yet reviewed.

## Outcome by goal

1. **Goal (1), `ck_min ≥ g(p)·n_p` with g→∞, unconditionally: NOT
   obtained.** What I did prove instead is a precise map of the obstruction:
   * Lemma 1.1 (PROVED; checked on 5994 triples): `M_{c,k}(p)` is the
     number of j with `(4ckj−p) | 4cj²+1`. So vanishing is a congruence sieve
     on p with moduli `4ck·D` up to `4ck·p`, which is larger than the sifted
     variable.
   * Prop 4.1 (PROVED): the exact list of events. For `G<n_p` the unforced
     slices up to `G·n_p` are `(qc',k)`, with exactly one non-residue prime
     q.
   * Prop 4.2 (PROVED, sharpens POINTWISE_OMEGA Prop 8.3): every reduced
     hard class contains infinitely many p with `ck_min=n_p`. So congruence
     input gives exactly `g=1`.
   * Lemma 4.3 (PROVED): subgroup-type sieve criteria have dimension ≥1/2
     per unforced slice, and the dimensions add across slices.
   * Assessment 4.4: these criteria need sifting range `√N≈x`. The
     semi-linear sieve is at its limit (`f(1)=0`) even under EH. For two or
     more slices, the sieve limit is ≥2 against an available level ≤x.
   * Lemma 4.5 / Assessment 4.6: the first-moment (union bound) approach
     needs moduli larger than x. It fails beyond O(1) extra slices, because
     the mass is `≈(log G)³ log p/log₂p`. A Poisson model suggests a true
     i.o. gain of `g=exp(c(log₂p)^{1/3})` on GR-type primes. Data show the
     Poisson form is conservative.
2. **Goal (2).** Thm 3.1 (CONDITIONAL on GRH): there are infinitely many
   hard p with `ck_min > (1/(2log2)−ε)·log p·log log p`. This is
   Montgomery's result, written out via Lagarias–Odlyzko so that the
   `p≡1 (24)` constraint is visible. Under GRH, Ankeny's bound caps what
   congruence methods can certify at `O((log p)²)`. Neither GRH nor EH
   reaches the combined event (§3 remarks, §4).
3. **Goal (3), the upper-bound direction.**
   * Thm 2.1 (CONDITIONAL on H for an explicit finite family): for all g,
     and every prime `r≥100D(g)²g³`, there are infinitely many p with
     `n_p=r` and `ck_min>g·n_p`. Also `ck_min≥n_p^{2−ε}` i.o. So no bound
     `ck_min≤f(n_p)` with `f(r)≤r^{2−ε}` can be proved without refuting H.
     The construction uses fixed part `A=1+4ck²` times one H-prime, and
     chooses the non-residue class b mod r to avoid the target divisors of
     A.
   * Thm 6.1 (PROVED, elementary): `n_p=5 ⟹ ck_min≤10`, and this is sharp
     (p=193). It follows from a Type-I covering with D=3 or D=7: the values
     −20, −40, −80 are all the non-zero squares mod 7.
   * Remark 6.2: under H, `C(r)=sup_{n_p=r} ck_min` is exactly the least
     height of a finite Type-I covering of `{n_p=r}` (the proved direction
     plus an H-sketch).
   * Open: is `C(7)<∞`? Evidence: every `n_p=7` prime up to `3·10^6` is
     witnessed by a target divisor `D≤2000` at `ck≤194`. The restricted
     covering search fails on 1684 of 7560 nodes. The real witnesses use
     further non-residue primes (11, 17, 19, …), so a proof must branch on
     p mod ℓ.

## Census (EVIDENCE)
I computed `ck_min` and `n_p` for all 82887 hard primes below `10^7`.
There are no violations of Lemma 8.1. The engine reproduces the notes
§48 records. Two new records:
* `ck_min(414241)=218`;
* `ck_min(9033649)=883`, with `n_p=43`, ratio 20.5 and
  `ck_min/(log p)²=3.44`. An independent dual engine confirmed it.

## Caveats and items for review
* Thm 2.1 depends on Hypothesis H (Schinzel) for `1+D(g)` polynomials.
  The fixed-prime-divisor check is in step 4. Please check step 5
  (`M=2·#{D|A: D≡−p}`) and the reduction to b mod r.
* Thm 3.1 cites Lagarias–Odlyzko 1977 Thm 1.1 and Serre 1981 Thm 4 from
  memory. They are not in `sources/`. The extra `+log d_L` term is
  included.
* Lemma 4.3 and Assessment 4.4 make method-level claims. The β-sieve
  sifting limits are standard facts (`β_{1/2}=1`, `β_1=2`). I make no
  optimality claim beyond Selberg's κ=1 parity example.
* Remark 6.2 (ii) is a sketch. It needs the Thm 2.1 machinery with general
  fixed parts in place of `p≡1 (ℓ^E)`.
* Novelty: Thm 3.1 is known (Montgomery). Thm 6.1 is classical ES
  territory (Mordell mod 5); only the Type-I depth 10 is new. Thm 2.1 is
  an instance of the formal-genericity mechanism. As far as I can tell the
  new content is P4.2, L4.3, T2.1's exponent `2−ε`, T6.1/R6.2 and the
  census.

## Suggested next step
Write a branching covering search for `C(7)`: depth-first search over p mod ℓ
for `ℓ=11,13,17,…`, with certificates whose cores include the branch's
non-residue primes. If it terminates, the result is an unconditional
`n_p=7 ⟹ ck_min≤C`. If it does not, it should produce an explicit
H-generic escape class.

## Round 2 (parent request: C(r) coverings)

1. **Literature (§6.1).** Our certificates `(c,k,D)` are exactly
   Elsholtz–Tao Prop 1.9 Type-I family 3, which is Salez's (15d). The other
   Type-I families (Salez 15a–c) have c or k growing with p, so (15d) is
   the only family that bounds `ck_min`. So `C(r)≤X` iff a (15d)-covering
   of `{n_p=r}` of height X exists (unconditional direction; under H also
   the converse, Remark 6.2). The literature has full single-prime
   coverings for `p≡1 (24)` exactly for non-residues mod 5 and mod 7
   (Rosati/Mordell; Salez `S_5`, `S_7`). Salez's `S_11`, …, `S_37` miss
   some non-residues. Those coverings use all equation types. For r=7, no
   (15d)-certificate is decided mod 168 on a non-residue class, so they
   say nothing about `C(7)`. The r=5 first case is Salez's Example 1
   [15d]. I found no statement about bounded-ck Type-I coverings.
2. **Branching covering search (§6.2, `typei_branch_cover.py`).** It
   re-derives Thm 6.1. For r=7 it found no covering
   (`X=600, F≤5000, q≤47`). Uncovered leaves are residue-one-like classes.
3. **Explicit escape classes (`typei_formal.py`, the Thm 2.1 machinery
   with an arbitrary residue pattern).** It computes the formal `ck_min` at
   an H-generic point and asserts that every fixed part and target class
   is determined by the class.
   * r=7: the point `p≡25 (2^14)`, `7 (3^9)`, `6 (7^6)`, `1 (ℓ^E)`
     elsewhere has formal `ck_min=539`.
   * r=11: the point `p≡2 (11^5)`, `1` elsewhere has formal
     `ck_min>3000`.

   **Cor 6.4:** under H, `C(7)≥539` and `C(11)>3000`. **PROVED
   unconditionally:** every finite Type-I covering of `{n_p=7}` has height
   ≥539, and every covering of `{n_p=11}` has height >3000. The proof
   refines the class at the primes >B occurring in the covering.
   Mechanism for r=11: at the residue-one point, a target `D|1+4ck²` has
   `D≡e≡−1 (mod 4m)`, which forces `jj'≈11^{a1+2a2}/(4c')`. This leaves
   only finitely many tiny cases until `ck≥11·121`.
   No stand-alone checker for a *covering* was needed, since none was
   found. The escape claims are checked by the assertions inside
   `typei_formal.py`.
4. **Conjecture (weak evidence):** under H, `C(r)=∞` for every `r≥7`, so
   r=5 is the only value of `n_p` with a finite Type-I covering.

Items for review: the soundness of `typei_formal.py`'s determinacy asserts
(an earlier run without the `4ck`-exponent assert gave a spurious
`>2000`; that assert was then added), and the refinement argument in the
proof of Cor 6.4.
