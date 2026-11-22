# Second independent hostile cross-lab review of `T_F` (`notes/z82/FAREY_IE1.md` §§2, 5.1, 7–12)

Reviewer: Claude Opus (smart mode), second independent reading, commissioned by the Wave z82 orchestrator.
Reviewed text: `notes/z82/FAREY_IE1.md` at `6a98cdb38` (HEAD `b2f2a260a`). I checked it against `notes/z81/FAREY_PROOF.md`
§§2–5, 7–8, 12, 14–15 and `notes/z80/IE1_SPLIT.md` §§2–6, 9.
Independence: I formed the whole critique below, including the verdict, **before** opening
`REVIEW_FAREY_IE1_R2_OPUS.md`. The comparison in §6 was written afterwards.

## 0. Verdict

**ACCEPT WITH MINOR FIXES.**

I found no broken line and no unproved load-bearing step. The claim is that `T_F` is a countable power cut with
* `IOpen + Bézout + global (Sep) + Lag + internal Dirichlet + full supplied-unit PW`,
* the flag and its all-PA-subrings factorial strings,
* `Th(n)` at every modulus, hence full Farey and proper reduction of every positive definite integral binary form,
* `¬ES(P)` at a nonstandard prime `P≡1 (840)`.

This holds **PROVED relative to the listed inputs**. Those inputs are the z80/z81 tower machinery (not replayed here),
Zariski–Nagata purity, the geometric étale `π₁` of `𝔸ⁿ`, `𝔸¹` and `TS³`, quadric Picard groups, real-closed-field
elementarity and planar Minkowski in `B≡ℤ`.

The fixes in §5 are about form, pointers and citations. None of them changes a conclusion.

Scope is stated honestly:
* `T_F` is a model of a **relaxation**.
* `T_F` is **not** claimed to satisfy `IE₁⁻`. Global BCM is proved **false** in it.
* ES in ℕ, `IE₁⁻` vs ES, and numerical leastness all remain OPEN.

Nothing here is a claimed proof of ES, so no CLAIMED flag is needed.

## 1. Queue dichotomy (§§5.1, 7)

* **`W` and the coordinates.** `W⁻¹=[[1/Q,0],[−Qτ,Q]]`, so `W⁻¹(q,p)=(q/Q,Q(p−qτ))`. This is correct. Substituting
  `Y=Qλ, Z=τQλ+μ/Q` into a homogeneous `G` of degree `k` gives exactly `(G∘W)(λ,μ)`. Different `k` give disjoint
  monomials.
* **Relative Gauss.** `λ̄,μ̄` are algebraically independent over the old residue field, so the size of a polynomial is
  its largest coefficient up to `O`-units. Hence `S[Y,Z]∩hull(F)=F` holds **iff** no nonzero positive-degree
  homogeneous `G/S` is bounded on `W`. Constants pass by the old invariant. Only the sufficiency direction is used by
  the queue.
* **Passing case.**
  * Two successive z81 free-line dilutions give `R_A[Y,Z]⊆R_new⊆S[Y,Z]`. The second sandwich composes with the first
    after localisation at `C∖0`.
  * Invariants 1–2 come from z81 §3 applied twice. The second line is over `E(Y)`, which the z81 lemma allows (any old
    stage field).
  * Invariant 3: the value group is unchanged, since this is a Gauss extension in `Y/Q` and `Q(Z−τY)` over a real
    closed field with divisible group. The residues are fresh in the same host. Sizes of `Q=√n` already have `K`
    representatives.
  * The witness is `X=aY−nZ=−μQ` with `|X|,Y<Q/2`. A signed `X` is allowed by `Th(n)`.
* **Failing case.** Appending a finite prefix of a temporary z81 floor/Bézout completion is legitimate:
  * each edge's valuations are completed inside that edge;
  * later main-line residues are chosen fresh over the real closure that already includes the prefix;
  * the prefix contains only ordinary floor/row edges.
* **Independent consistency check (degree 1).** Suppose a late z81 §14 Dirichlet gap (B) at slope `ζ`, boundary `B₀≫Q`,
  is still intact. A degree-1 obstruction would be a pair with `q≤cQ` and `|q(ζ−1)−p|≤c/Q+cQ/n=2c/Q`. That is
  `F`-infinitesimal at heights `≪_C B₀`, which (B) forbids. So the failing case cannot fire while such a gap survives,
  and there is no contradiction with z81 §14's "permanent under z81 edges".
  * Together with §7's just-born-line computation, this agrees with the structure of §§8–10: an obstruction yields a
    coarse pair inside a z81-only completion, and that would have to violate (B).
  * This complements the R2 degree-2 hand check.

## 2. §8: coarse to exact, and obstruction normalisation

* **Basis completion and shear.** After division by the gcd, and since `β:=‖W⁻¹v‖∞>1`, the Bézout completion and the
  floor shear give second-column bounds `β/2` and `β+1/β`. `M₈=W⁻¹B₈` has determinant 1, so its inverse is its
  adjugate and is bounded.
* **`F`-approximation at precision `1/(100c²)` with nonstandard `c`.** This needs bounded real-closure elements to have
  `F`-fractions within every `1/c`. It holds for two reasons:
  * `C` floors its own real closure (z81 §3), so `F` is dense in `rc(F)` at `F`-precision;
  * the residue host is the completion of `rc(F)`.

  The note says only "precisely the `F`-residue approximation invariant". A one-line pointer would help (fix m2).
* **Constants.**
  * `|det N−1|=O(1/c)`, `‖N⁻¹‖≤3c`.
  * Rectangle area `8/|det N|>16/3>4`.
  * `|z_i|≤13.5c`, `|(M₈z)₁|≤1/2+0.28/c≤1`, `|(M₈z)₂|≤5`.
  * `q=0` would force `|p|≤5/Q<1`.
  * `5/√n≤5/⌊√n⌋`, so the ordinary `K=5` lemma applies at level `⌊√n⌋`.
* **Minkowski transfer.** This transfer to `B≡ℤ` (degree-coded algebraic entries plus RCF quantifier elimination) is
  sound. `T_F` does start from the true-arithmetic flag.
* **Normalisation.**
  * A minimal-degree obstruction is irreducible over `Frac S`.
  * `S` is a gcd domain at row and sphere stages by the z80 §2 factor calculus, and localisation preserves this. The
    current text now says so.
  * Nonzero elements of `S` have size `≥1/c`: a nonzero `r∈R_A` with `|r|<1` would lie in `hull∩S=F` and in
    `R∩K=B`.
  * `Δ(G)` is `SL₂`-invariant, arithmetic and bounded, so `Δ(G)∈R∩hull=C∖0`.
  * The degree-1 identification `(q,p)=(β,−α)` checks out.
* **Replay.** I re-implemented the §2 local lemma exactly as written: clip, gcd, reflect, the `h≤K` Bézout progressions
  with ceiling, the right neighbour by the largest `z≤Q` in the class, and `K=5`.
  * On 3000 random `(t,Q,q,p)` with `|qt−p|≤5/Q`, it gave the brute-force Farey bracket every time (0 mismatches).
  * The two-error identity `rz+sv=n` yielded a valid `Th(n)` pair on 2000 random `(a,n)` (0 mismatches).
  * The script was a throwaway `/tmp` check and is not committed.

## 3. §9: horizontal descent (d≥3; d=2 also)

* **Finite étale root scheme.** A unit discriminant lies in the ideal generated by the coefficients. So `V(G)⊂ℙ¹_A` is
  finite étale over **all** of `Spec A`, not only at height-one primes. The note's DVR argument is correct, but this is
  the shorter route.
* **Purity.** Purity is invoked only on the **regular generic fibre** over `E₀`. This matters: the total sphere ring is
  singular along `{x=0, s=0}`, in codimension 4. Restricting to the generic fibre, the geometric `π₁` is trivial in
  each case:
  * `𝔸ⁿ` and `𝔸¹`;
  * `Σz²=1` in `ℂ⁴`, which is `≅TS³≃S³`. Riemann existence and invariance under algebraically closed extension in
    characteristic 0 cover this.
  * With geometric connectedness, the homotopy exact sequence then gives a constant extension `E₀'/E₀`.
* **Unramifiedness descends.** It descends through `e=1` persistence of old primes, and characteristic 0 rules out
  residue inseparability. The induction is correctly phrased on **divisorially unramified fields**, not on covers of
  singular total spaces. It ends at the seed `K[P]`.
* **Base change to `L`.**
  * Geometric integrality holds by induction: row charts with a nonempty overlap; monic sphere over a rank-4 generic
    fibre.
  * Row pivot coprimality over `L` holds because a common prime `ρ` has a nonunit norm dividing `a^{[L:K]}` and
    `b^{[L:K]}`. The norm is a nonunit because the units are `L*`.
  * The Nagata, quadric Picard and unit arguments are field-independent in characteristic 0. On the quadric threefold
    `Pic=ℤH`, and the boundary quadric surface of rank 4 is irreducible even when split.
* **`K`-point `o`.**
  * Every z81 sphere target is positive: the square content is removed and the target is a positive task.
  * Every row has a nonzero pivot at the generic ordered point.
  * Tarski transfer to `rc(K)` and inductive density of `K`-points then work. Positive `K`-targets are sums of four
    `K`-squares by PA Lagrange after clearing a square denominator, and stereographic density follows.
  * The temporary completion adds no spheres, and `o` is needed only on the main stage.
* **Galois invariance.**
  * `σ(l_i)=c_i l_{π(i)}`, `c_i∈L*`, and every `l_j` is an `L`-combination of `l₁,l₂`, so `σ(E)=CE` with `C` constant.
  * `σ(T)=(CE(o))⁻¹CE=T`. Here `σ` commutes with evaluation at the `K`-point `o`.
  * `A_L^{Gal}=A`.
  * The descent works for `d=2` too. The text now attributes the `≥3`-root requirement to §10's collision lemma only.

## 4. §§10–11: arithmetic basis change, window, scheduling, preservation

* **Hermite step, d≥3.** `mT` is arithmetic and the bottom-row Bézout in `R` gives `[[w,b],[0,v]]`. `wv=m²` is scalar,
  so `w,v` are scalar by the factor calculus.
* **`b₀` by congruence transfer.** The system has ordinary degree and number, with `B`-coefficients and a nonstandard
  modulus. The z81 §12 embedding of `(E,w_l)` over `K` into the henselian pair fixes all `B`-parameters. For each prime
  `l|M₀` the integer-sort approximant reflects to `B` by elementarity, then PA CRT applies. This needs `B≡ℤ`, which
  holds.
* **z81 §12 hypothesis for the new edges.** The two-free edges are two ordinary line dilutions with `B`-digit centres,
  and the prefixes are z81 floor/row edges. So the hypothesis is met. §10 now says so.
* **`δ∈S_R`.**
  * `v_𝔪∘c` is a genuine valuation. It is multiplicative by invariant 1. The ultrametric inequality holds because
    `c(x+y)/gcd(c x,c y)∈B`, and in the Bézout `B` the gcd attains the minimum.
  * The two forms have unit discriminant (`Δ∈C∖0⊂B'^*`).
  * The collision lemma is correct: primitive roots have distinct reductions, a non-integral `M` has rank-1
    reduction, and two of `≥3` roots collide.
  * The maximal-ideal argument puts the reduced denominator of `c(δ)` into `C`. Then `den·δ∈R_A`.
* **Degree 2.**
  * Signs and factors check out: `±2G=[a,2u,c]`, `a>0`, `D=ac−u²=−Δ(G)`.
  * For `D<0`, `−D` is a nonsquare by irreducibility, so `L=K(√−D)` is real quadratic. Domain, UFD and units `L*` come
    from §9.
  * The splitting at `π|h` holds because `u` is a unit mod `π` (`u²≡−D∈K*`).
  * `λ|(u+t₀)`, `Nλ=γh` with `γ∈B∖0` signed. `(γ/λ)·(u+t₀)=γ·(u+t₀)/λ` has integral coordinates, and the signed
    determinant is `H₀=γa₀`.
  * The column operation has determinant **one**, so the equivalence is proper whatever the sign of `H₀`.
  * Stability gives `v|w`, `v|b` and `m|r²+D`. §3.1 uses only `v_l(D)`, `|m|`, and `s∈C` (automatic since `|D|∈C`),
    and the sign plays no role there.
  * After the shear, `(r₀²+D)/m∈R∩K=B`.
* **Window, d≥3.** `N∈SL₂(rc(K))` exists by RCF model completeness. The collision lemma over `O[i]`, the unique
  extension to the algebraic closure, handles complex-conjugate roots. So `N⁻¹M∈SL₂(O)`.
* **Window, quadratic.**
  * Definite: `γ=√Δ/2` is an `O`-unit and the Gram positivity bounds `J₂M`.
  * Indefinite: Gauss gives `‖r₁‖‖r₂‖=O(1)`, and `det=1` gives `≥1/2`. The `K`-size representative `h` of `‖r₁‖`
    exists by invariant 3.
  * Minkowski (area 16) gives `z∈B²`. `M⁻¹z=(N⁻¹M)⁻¹N⁻¹z` is bounded and `T₁⁻¹z∈S_R²`, which hands over to §8.
* **Scheduling, cut and non-leakage.**
  * The fair dovetail is fine and `n∈C` is covered by scalar PA.
  * Cut restriction: `Y,|X|≤√n`, and the quotient is `≤Y+1`.
  * The `−deg` valuation on a two-free block is trivial on `E_old`. The residues of polar `1/x_i` vanish, so the
    surviving constants sum to `4/P`, and positivity forbids omission. Degree-0 elements contract to `A_old`.
  * After descent, the z81 §4 thick square specialisation is untouched.
  * Fibre at `P`: two-free edges are purely transcendental, rows are generic lines, and spheres are geometrically
    integral. So `−1` remains a nonsquare mod `P` even though `Th(P)` holds and `P≡1 (4)`. This is consistent, since
    the two-squares route needs exactly the missing root.
  * PW, the flag, IOpen, (Sep), Lag and cut-height Dirichlet all follow from the z81 cut lemma's hypotheses: `C` is
    initial, there is a `B`-point in `(x,3x/2)`, and the factor calculus holds. Every new edge preserves these.
  * BCM fails in `T_F` by z81 §15 (power cut about an infinite `H`).

## 5. Fixes requested (minor; none load-bearing)

* **m1.** In the §0 Label, add **z81 §15**, which the §11 table cites for the BCM failure. It is missing from
  "z81 §§2–5,7–8,10–14".
* **m2.** In §8, at "F-residue approximation invariant", add a pointer: `F` is dense in `rc(F)` at `F`-precision because
  `C` floors `rc(F)` (z81 §3), and the host is the completion of `rc(F)`.
* **m3.** In §8, the cite "(§3.2)" for "Rows and monic spheres preserve the UFD and old primes" should point to z80 §4,
  z80 §9.1 and z81 §7. §3.2 is the base-change paragraph.
* **m4.** In §10, "each of the two charts" should read "each of the two successive line dilutions".
* **m5.** In §7, "The upper ring is polynomial in Y,Z because the ordered substitution is invertible" should be
  reworded. The ring is polynomial by construction; algebraic independence of `λ̄,μ̄` gives injectivity of the order.
* **m6 (optional).** In §9, add the one-line global finite-étale argument via the unit ideal of the coefficients.
* **m6b (optional).** In §9, state explicitly that all z81 sphere targets are positive tasks and that the temporary
  completion adds none. That is what makes the `K`-point exist.
* **m7 (optional).** "Proper reduction" here means `|b|≤a≤c`. The full Gauss boundary normalisation needs only a fixed
  finite set of extra `SL₂` moves in IOpen. A clause would preempt a pedantic objection.

## 6. Comparison with Round 2 (read after §§0–5 were drafted)

**Agreement.** R2 independently reached ACCEPT WITH FIXES. Its substantive items 1–5 all appear in the current text:
* the gcd domain at row and sphere stages (§8);
* §3.2 over real `t₀` and arbitrary `L/K` (§§9–10);
* the degree attribution (§9);
* `b₀` transfer with nonstandard coefficients and the edge-coverage statement (§10);
* §12 relabelled as depending on external Lane 2B §1, in §0 as well.

R2's form fixes also appear: the z75 §4 cite in §11, the §6 superseded note, the property table and the wording in §0.

**My additions.** Items m1–m7 are not in R2. So are:
* the degree-1 consistency check against z81 §14, complementing R2's degree-2 check;
* the explicit `F`-density justification;
* the observation that purity is never needed on the singular total sphere ring;
* the executed replay of the §2 lemma and of `Th(n)`.

**Disagreement.** None on substance.

## 7. Scope, labels, F1–F4 and Screen 18

* **Labels.** PROVED (rel. …) is appropriate. §6 is correctly CONDITIONAL on host ES at `P`. §12 correctly carries the
  external dependency.
* **F1–F4.** The §1 and §7 Assessments are honest:
  * only strict-square specialisations are excluded;
  * there is no `8/p` or `C`-even extraction at 11, 17, 131 or 241, nor at the two R₈ line zeros;
  * there is no II/U₇ transfer at 4545 or Z₇;
  * there is no `(★)` at the prime zeros or at 17, 401, 609.
* **Screen 18 (proposed rewrite).** It is right that full Farey, Thue and reduction no longer distinguish the z81
  relaxation from `IE₁⁻`. The proposed rewrite does not oversell: BCM failure is explicitly called **not** an
  induction refutation (z75 `IE1_ES.md` §4).
* **Not claimed.** `T_F` is **not** claimed to satisfy `IE₁⁻` or BCM. L(Div) and numerical leastness are UNKNOWN.
  ES in ℕ remains OPEN.

Bottom line: **ACCEPT WITH MINOR FIXES** (m1–m7). There is no gap in `T_F`. This is the second cross-lab hostile
review, after R2.
