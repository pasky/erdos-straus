# Second independent hostile review: z83 Lane 1 `IE1_DECIDER` — `T_F ⊭ IE₁⁻` via Π

Reviewer: Claude Opus (smart mode), second independent hostile cross-lab reviewer for the z83 orchestrator.
Object: `git show 8ef750588:notes/z83/IE1_DECIDER.md` (branch `side-agent/z83-ie1-decider`) and
`git show 8ef750588:scripts/z83_ie1_digits.py`. The R1/R1V Opus reviews on that branch were **not** read before
this verdict was written (see the postscript).
Sources checked: `notes/z82/FAREY_IE1.md` §§4.1, 7–12 (identical on `main` and at the pin), `notes/z81/FAREY_PROOF.md`
§§2–5, 7–12, `notes/z79/IE1_BASE.md` §§4, 7, FRONTIER's IE₁⁻ barrier entries and `data/z66/ie1/lit_ie1.md` for the
definition of `IE₁⁻`.

**Bottom line.** I found no gap. The heart of the note holds: the §1 instance is a genuine parameter-free `E₁`
induction provable in `IE₁⁻`, and §2's miss at `(h,a)=(H,P)` is a correct algebraic argument in the vertical fibre.
Together they prove `T_F ⊭ IE₁⁻`. Below are the verdicts for each section and a few minor wording fixes. Nothing in the
note claims `IE₁⁻ ⊢ ES` or `IE₁⁻ ⊬ ES`. ES in ℕ remains OPEN.

| Section | Verdict |
|---|---|
| §1 `IE₁⁻ ⊢ Π` (and the degree-`d` scheme) | **ACCEPT WITH MINOR FIXES** (m1, m2: state the auxiliary theorems the step uses, and the base for the pigeonhole equivalence) |
| §2 `T_F ⊭ Π`, threshold `h∈C`, largest convex Π-subring | **ACCEPT WITH MINOR FIXES** (m3, m4: make the edge inventory explicit) |
| §3 henselian, regular/solvable obstruction, `S₅`, compatibility | **ACCEPT** (m5 optional) |
| §3.1, §4 (light pass) | **ACCEPT** at the level checked |
| §0 labels, scope, STATUS delta | **ACCEPT**. The delta wording is accurate |

---

## 1. §1: the induction instance

**Definition used.** In the repo `IE₁⁻` means `PA⁻` plus the parameter-free scheme
`φ(0) ∧ ∀y(φ(y)→φ(y+1)) → ∀y φ(y)` for `E₁` formulas `φ(y)` with `y` as the only free variable. Here `E₁` means
bounded-existential quantifiers with term bounds over an open matrix, in `{0,1,+,·,<}`. This is the
Kaye–Paris–Dimitracopoulos definition, quoted in `lit_ie1.md` (line 103) and used in z79 §4. The axiom is an
implication, so it suffices that `IE₁⁻` *proves* the base and the step. Other `IE₁⁻` theorems may be used inside those
proofs without circularity.

**The formula, written out.** Let `φ(y)` be:

```
∃m≤y ∃i≤y ∃s≤y ∃u≤y ∃v≤y ∃d≤y ∃e≤y ∃x≤y ∃q≤10(y+1)³ ∃b≤y ∃b'≤y ∃c≤y [
   m²≤y<(m+1)² ∧ y=m²+i ∧ s²≤m<(s+1)² ∧ m=s²+u ∧
   ( u>s                                     -- invalid pair: open
   ∨ (u+v=s ∧ ( h=0                          -- with h:=u, a:=v (or the nested variant)
       ∨ (b=2b'+1 ∧ b>1 ∧ bc=h)              -- escape
       ∨ (de=h ∧ d≥j ∧ x<d ∧ (x+2x²=a+dq ∨ a=x+2x²+dq)) )))   ]
```

Here `j=min(i,h)` is expanded into the two open cases `i≤h ∧ …[j:=i]` and `i>h ∧ …[j:=h]`. There is no bounded
universal quantifier anywhere, no `D₂` guard, and no "least" or "unique". Every bound is a term in `y`. The matrix is
open, with disjunctions. The note's description ("invalid decodes or `h=0` succeed openly… **no** universal guard `D₂`
inside the matrix") matches this exactly. For the fixed-degree `X+2G(X)` extension with packed signed coefficients,
the same shape works with a larger fixed exponent in the `q`-bound.

**Base.** At `y=0` we get `m=i=s=u=v=0`, so `h=0` and the formula succeeds openly. The base is TRUE.

**Step, checked case by case.** The proof is in `PA⁻` plus two auxiliary `IE₁⁻` theorems; see m1.

* *Same block* (`y+1<(m+1)²`). Keep `m,s,u,v`. Set `i↦i+1`.
  * If `i≥h`, then `j` is unchanged and the state is carried.
  * Otherwise `j↦j+1`. If `d≥j+1`, keep the state. Otherwise `d=j` by discreteness, and `d<h`, so `e≥2`.
  * If `e` is odd, `(b,c)=(e,d)` is the escape.
  * If `e` is even, the new state is `(2d,e/2)`, with `2d≥j+1` because `j=d≥1`.
  * The new `x` is chosen by the parity of `q`. In the `+` branch, `F(x+d)−a=d(q+1+4x+2d)`. In the `−` branch it is
    `d(−q+1+4x+2d)`; trichotomy of `q` against `1+4x+2d` gives a nonnegative quotient on the correct side. The odd
    factor `1+4x+2d` makes exactly one of `x, x+d` work mod `2d`. Both candidates lie below `2d≤h`.
  * The bounds are `|q|≤3h²+a≤3y²+y`, and the new quotient is at most half of `q+1+4x+2d`. Everything stays within
    `10(y+1)³`.
  * An escape, an invalid pair or `h=0` is carried unchanged.
* *Block boundary* (`y+1=(m+1)²`). Set `m'=m+1`, `i'=0`. The new root `s'` comes openly from `s`: either `m+1<(s+1)²`
  and `s'=s`, or `m+1=(s+1)²` and `s'=s+1`. So the single-pair decode needs **no** separate root axiom at the
  successor. Decode, then initialize with `d=1, e=h, x=0`, using `F(0)≡a (mod 1)`. This holds for every `a`, including
  `a≥h`.
* *Nested codes* (the packed-coefficient variant). Here one needs `∀w ∃r≤w+1 (r²≤w<(r+1)²)`. That is a separate
  parameter-free `E₁` induction with an open step (z79 §4 "Root decoding is total"). It is proved before and
  independently, so there is no circularity.
* *Parity* (`e` and `q` are even or odd). This needs `∀y ∃k≤y (y=2k ∨ y=2k+1)`. It is again an independent
  parameter-free `E₁` induction with an open step.

**Terminal state.** Given `h>0` and arbitrary `a≥0`, put `m=(h+a)²+h` and `y=m²+h`. Then `h≤m`, so `h≤2m`. The roots
`m` and `s=h+a` are forced by uniqueness of integer square roots, which holds in `PA⁻`. The pair is valid, `i=h` and
`j=h`. So `φ(y)` gives either the escape, or `de=h, d≥h`. Since `e≥1`, that forces `d=h` and hence `x<h` with
`F(x)≡a (mod h)`. So every pair `(h,a)` is reached at a block with `2m≥h`. **Π follows.**

**Independent simulation** (`/tmp/z83r/sim.py`, not committed). I ran exactly this state machine, with the invariant
`de=h, d≥j, x<d, d|F(x)−a`, signed-quotient parity and the odd-cofactor escape. The run covered every `h<400`, every
`a<2h+3` plus random large `a`, and four polynomials `G`: `X², X⁵, 3X³−7X+11, −5X⁴+X²−2`. The invariants held at every
step, and the terminal outcome was "hit" iff `h` is a power of 2 ("escape" otherwise). The author's
`z83_ie1_digits.py` also replays PASS (permutation iff pure dyadic for `h≤512`, collision recipe, Newton = bit lift
through 512 bits, 37 remainder controls).

**Pigeonhole equivalence.** I checked both directions. `F(v)−F(u)=(v−u)(1+2(u+v))`. For the converse, take `k=h/b`
and `4u≡−1−2k (b)`; then `1+4u+2k≡0 (b)`. The equivalence needs Bézout (for the coprimality step) and parity. `IE₁⁻`
proves both (z79 §4), and `T_F` has them. See m2.

**m1 (minor).** State explicitly that the step is proved in `PA⁻` plus two earlier parameter-free `IE₁⁻` theorems:
totality of parity, and (only for nested or packed codes) totality of integer square root. The single-pair successor
root is open. Currently the note mentions the square root but leaves parity implicit ("odd means `b=2s+1`", "use the
parity of the signed quotient").

**m2 (minor).** "Over the base" in the bounded-pigeonhole paragraph should name the base, e.g. "over
`PA⁻`+parity+Bézout (all `IE₁⁻`-provable, z79 §4)".

## 2. §2: failure in `T_F`

**`D₂(H)`.** Take `r e=H` in `T_F`. Divisibility of bounded elements is absolute between `T_F` and the uncut `R`. In
the finite-stage upper algebra `A` (a UFD with units `K*`; z81 §3 invariant, rows, spheres and polynomial blocks
preserve it per z80 §4, z81 §7 and z82 §§8–9), the factor `r` divides the nonzero scalar `H`, so `r` is a unit and
`r∈K*`. Integrality at every scalar place puts `r` in `B`. Oddness of a scalar inside `T_F` is PA oddness, because
`(b−1)/2` is in `K` and integral, hence in `B`. In PA, `2^L` has no odd divisor >1. So `D₂(H)` holds, and by Bézout in
`T_F`, `F` is injective mod `H`.

**`B'` and the residue field.** `C∖0` is multiplicatively closed and contains every ordinary integer, including 2.
`H=2^L` is still a nonunit of `B'`: `H|c` with `0<c∈C` is impossible because `c<H`. There is no conflict here. `L`
lies in `C`, but `2^L` does not, and `C∖0` is closed under finite products, not under powering to nonstandard
exponents. A maximal ideal `M∋H` exists, and `k=B'/M` has characteristic 0.

**Fibre.**
* Seed: `(C∖0)⁻¹R_seed=B'[P]` (z81 §4: descending degree with leading coefficient `L^{2n}∈C`, plus integrality of
  `P`). The fibre is `k[p]` with `p` transcendental.
* Free, floor and Dirichlet lines and the two `z82` two-free blocks: the localized algebra is `S_old[Y]`, respectively
  `S_old[Y,Z]`. The fibre is a polynomial ring over the old fibre domain, hence purely transcendental.
* Rows: `(S_old/M)[u,v]/(āu+b̄v−1)`. The pivots have coprime scalar contents, so not both contents lie in `M`. Their
  content-1 parts survive by the gcd-in-`B'` argument, which I rechecked: if `g|r` in `S_stage`, then `g` divides
  `c·content(r)` for some `c∈C`. So at least one pivot is nonzero. The ring is covered by the opens `D(ā)` and
  `D(b̄)`. These are polynomial over localizations of a domain, with nonempty overlap if both survive. So it is an
  integral scheme, its fraction field is `Frac(old)(v)`, and `old→new` is injective.
* Spheres: monic rank 4. The algebra is free over `old[x₁,x₂,x₃]`, so it injects into the generic fibre. A quadric of
  rank ≥3 is geometrically integral even when the target reduces to 0. So the fraction-field extension is regular.
* Directed union: `S/MS=colim(S_stage/MS_stage)` with injective transitions. Regularity is transitive, so `k(p)` is
  relatively algebraically closed in `Frac(S/MS)`.

**Edge inventory hunt.** I looked for any edge in the z82 `T_F` queue that adjoins an algebraic element in the fibre.
There is none.
* The edges are: the z81 seed, floors, rows, Lag spheres, Dirichlet lines (z81 §7: free `Y=H'η'` with `a+mY`
  primitive), the passing two-free blocks, and the failing-case prefixes. The prefixes consist of "the usual unchanged
  z81 edges to floors and Bézout" (z82 §10), cut to a finite prefix (z82 §11).
* The quadratic and Galois scalar base changes of z82 §§9–10 (`K(√−D)`, `L/K`) occur **only inside proofs**. They are
  never edges.
* Supplied-unit PW, the factorial strings, scalar four-square targets and Farey/Thue hold through the cut lemma or
  true arithmetic, not through adjunction. There are no Pell, norm or elliptic edges in `T_F`: z81 §12 "retained
  rungs" are proofs, not edges.
* z81 §11's square-tested prime births are not in `T_F` (z82 §11 schedules only floor, row, sphere, Dirichlet and
  pair tasks). They would be polynomial `S_old[q]` in the fibre anyway, as used in §4's `T_F^↓`.
* z81 §9's extra first-digit polynomial `1+(LP)²` is a valuation choice, not an edge.

**Reduction.** `x,v∈T_F⊂R⊂S`, and reduction modulo `MS` is a ring map. `F(x)=P+Hv` becomes
`(1+4x̄)²=1+8p`, which is impossible because `1+8p` has a simple zero in `k(p)` (characteristic ≠2). This holds even
for `x` and `v` in the uncut `R`, so no cut-bounding subtlety arises. The instance `y=m₀²+H` with
`m₀=(H+P)²+H∈T_F` therefore fails in `T_F`. `T_F` satisfies `IOpen`, so it has the parity and root theorems, and the
base and step of the §1 axiom hold there. **`T_F ⊭ IE₁⁻`.** The statement is correct, and it is independent of BCM.

**Threshold and `(P−1)/8`.** Assume `D₂(h)`. A positive primitive horizontal prime factor `π` cannot be even, because
`π/2` would have content `1/2`. By `IOpen` parity, `π` is then odd and >1, which violates `D₂`. So `h` is a scalar
times a unit in `K*`, and in PA it is a power of 2.
* If `h∈C`: reduce `a` by division, which lands in `C`, and apply PA.
* If `h∉C`: `h` is a nonunit in `B'`, and the same fibre argument applies at a maximal ideal containing `h`.
* `(P−1)/8∈R` because `8|840|L`. Its reduction gives `(1+4x̄)²=p`, or directly `r̄²=p` for any putative square root of
  `P` mod `h`. Correct.

**Largest convex Π-subring.** `Good` defines `C⁺` in `T_F`. For `y>C`, the z81 §2 approximant gives `b∈(y/2,3y/4)`,
and the largest PA power of 2 below `b` gives `C<h<y`. The target `P mod h` is below `y`. The miss and `D₂(h)` are
bounded statements, hence absolute for convex subrings, so no convex subring of `T_F` strictly larger than `C`
satisfies Π. Conversely `C⊨Π`, because `B≡ℤ` has polynomially bounded witnesses. Correct as scoped: the note says
nothing about nonconvex subrings.

**m3 (minor).** In the `D₂(H)` sentence, add the two one-line facts used above: divisibility of bounded elements is
absolute between `T_F` and `R`, and a scalar that is odd in `T_F` is PA-odd.

**m4 (minor).** The fibre-check items 2–3 should name **Dirichlet lines** and the **failing-case prefix (floor and
row edges)** explicitly as free or row edges. They should also state that PW, the factorial strings, scalar Lag
targets and the §§9–10 scalar base changes are not edges. Otherwise a reader has to reconstruct the inventory above
from z81 and z82.

## 3. §3: repairs

* **Henselian quotient.** The argument holds.
  * `A=R/hR` is local with maximal ideal `2A` (odd elements are invertible by `D₂` and Bézout) and residue field `F₂`
    (parity).
  * The Hasse expansion `f(c+2Y)=2(b+Y+2G(Y))` is correct, because the terms of order ≥2 carry a factor `4`.
  * Solving the stronger congruence `y+2G(y)≡−b (h)` with the §1 scheme gives the root.
  * Quotients of henselian local rings are henselian. A local Bézout domain is a valuation domain.
  * The `√2` argument (integral, so it lies in the maximal ideal `2D`; then `2(2z²−1)=0` and `2z²=1`) is correct in
    characteristic 0. As written, it is about `Frac(D)`, not the whole receiving field, and the note says so.
  * Citing Stacks 04GG for arbitrary (non-monic) `f` is appropriate.
* **Kummer and degree `d`.** The radicands `1+8(p+i)` are linear with distinct simple zeros, so any nonempty product
  is a nonsquare and the extension has degree `2^r`. For `2t^d+t=p`, the pole order at infinity gives degree `d`.
  Correct.
* **`S₅` for `T+2T⁵`.** Checked by hand and by computer (`/tmp/z83r/s5.py`).
  * The critical points are the four roots of `1+10T⁴`. There, `f(T)=T(1+2T⁴)=4T/5`, so the four critical values are
    pairwise distinct, and `f''=40T³≠0`. Numerically, the values are `±0.318±0.318i`, equal to `4T/5`.
  * So each finite branch point has exactly one simple ramification point, and the local monodromy is a
    transposition.
  * The group is transitive by irreducibility over `k̄(p)`, hence primitive (degree 5 is prime). A primitive group
    containing a transposition is `S₅`.
  * Arithmetic sanity check: `2T⁵+T−c` modulo the primes `<3000` for `c=1` and `c=7` shows every cycle type of `S₅`,
    including `(2,3)` and `(1,1,1,2)`. The case `c=3` is reducible at `T=1`, which is consistent.
  * The step "a solvable relative closure cannot contain even one root" is correct, because the normal closure of
    `k(p)(α)` is the full `S₅` splitting field.
  * Scope check: the claim is restricted to the degree-5 *instance*, not to Π. It is correct as worded.
* **Compatibility with `¬ES(P)`.**
  * In an external PID, the only positive divisors of 2 are 1 and 2. So 2 is prime, and `D₂(h)` gives `h=2^n` with
    ordinary `n`. External lifting then gives Π.
  * For the z78 tower, the argument via a positive axis value (giving `3|h`), singleton content and the old ring is
    consistent with the FRONTIER z79 entry ("first positive-value conductor … inside `(2)∩(3)`"). I checked this only
    at that level; I did not replay z78.
  * The note properly scopes this as "compatibility, not full Farey".
* **m5 (optional).** Mentioning that the monodromy at infinity is a 5-cycle gives a one-line alternative proof of
  transitivity.

## 4. §3.1 and §4 (light pass)

* **Ascending peeling.** The coefficient of `Z^i` is `2^i g_i` plus lower terms, and 2 is invertible in `B'`. So the
  localized seed is exactly `B'[X]`, with no division by `M₀`. Correct.
* **Newton identity.** `F(r−Eu)−A=E(1−(1+4r)u)+2E²u²` (with `E=F(r)−A`) is correct. I checked it symbolically with
  sympy (residual 0), and the author's script replays the lift.
* **Ordinary iteration bound.** A pure dyadic `h` in the cut divides `H^j` (respectively `N^j`) for an ordinary `j`.
  Correct.
* **Global failure via the target `X`.** The global failure moves to the target `X`, through `1+8X̄`. Correct.
* **`T_F^↓` size bound.** `q≈8LN²<y`, because `L∈C` and `N≤(3/2)y^{1/4}`. Correct.
* **Conditionality.** The "no least failure" claim is correctly labelled CONDITIONAL on ES in ℕ.
* **Unary `U₁` control.** The codes `(a+h)²+a<4u²+u<y` are coinitial above `C`, with none in `C`, so the set has no
  least element. Correct.
* **`IE₁⁻ ⊢ IU₁⁻`.** The reversal argument is valid because the IU₁ hypotheses are parameter-free *sentences*. One
  works inside a model where they hold, so the induction step for the packed formula holds there. The note's word
  "global" captures this.
* **Wilmers.** The duality paragraph is labelled Assessment. Its content is consistent with `LU₁⇒IE₁` and
  `IE₁⇔IU₁⇔LE₁` (with parameters).

## 5. Labels, scope and STATUS delta

* The Scope line explicitly denies `IE₁⁻ ⊬ ES` and any decision of ES in ℕ. Nothing in the note overreaches.
* The proposed STATUS qualifier, "`T_F ⊭ IE₁⁻`: `X+2X²` is injective but not onto mod `H=2^L`", is accurate.
  Injectivity follows from `D₂(H)` plus Bézout in `T_F`, and non-surjectivity from the fibre argument.
* Triage is appropriate: BARRIER-SCOPED for the tower lock, BARRIER-BROAD for the §3 fibre-field obstruction as
  stated with its hypotheses (`D₂(h)`, a map to a field of characteristic 0 killing `h`, `p` transcendental).

## 6. Things I tried that did not break it

* I looked for a hidden universal quantifier: none.
* I looked for a parameter, such as `H` or `P` sneaking into the formula: none. They enter only through the
  instantiated code.
* I checked whether the step fails at `d=j=h` or at `i>h`: the cases are excluded or trivial.
* I checked `a≥h`: the initializer works mod 1.
* I checked whether `2` being inverted in `B'` contradicts `H∈M`: it does not.
* I checked whether a sphere with reduced target 0 breaks the domain property: rank 4 is geometrically integral.
* I checked whether rows can lose both pivots: coprime contents prevent it.
* I checked whether any z82 edge adjoins a root: none does (§2 inventory).
* I checked whether the obstruction is an artifact of the cut: no. It already holds in the uncut `R`.

## Postscript (written after the verdict above; R1/R1V reports then read)

After writing the verdict I read `REVIEW_IE1_DECIDER_R1_OPUS.md` and `REVIEW_IE1_DECIDER_R1V_OPUS.md` at `8ef750588`.
They do not change any verdict above.

* **Agreement on substance.** Both reports accept §§1–2 and the §3 algebra. R1 independently noted the same
  `2∉M, 2^L∈M` consistency point. The `S₅` and threshold checks agree with mine.
* **R1 critiques already applied.** At the pin, the triage is BARRIER-SCOPED/BROAD rather than HEADLINE, the STATUS
  delta is compressed, the §4 `IU₁⁻` reversal is split out as PROVED, the §3.1 transfer audit is spelled out, and the
  Bézout citation and Stacks Tag 04GG have been added.
* **New here.** m1 is not in either earlier report: the step's reliance on totality of parity, which is a separate
  parameter-free theorem, and the observation that the single-pair successor root is open. R1 says only that the step
  needs no Bézout, which is true. The explicit inventory in m4 (Dirichlet lines, prefixes, non-edges) is also new.
* **R1 item 7 (debate).** R1 suggested a stronger "relatively algebraically closed image" barrier. I agree with the
  pinned note's retraction of the overreach (R1V item 4). The henselian-valuation-domain statement is the correct form.
  I do not see an extension to arbitrary separable polynomials *over the receiving field*, because of the integrality
  caveat stated in the note.
