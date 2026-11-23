# Second independent hostile review: IE1_DECIDER Round 2 — (I) `T_Π` (§§6–9) and (II) §10 conservation

Reviewer: Claude Opus (smart mode), cross-lab, second independent R2 audit. Commissioned by the Wave z83 orchestrator.
Object: `git show bb06ac1bc:notes/z83/IE1_DECIDER.md` (branch `side-agent/z83-ie1-decider`). §§6–10 in full, §§1–3 only
where R2 depends on them.
Sources read: z81 `FAREY_PROOF.md` §§2–4, §12; z82 `FAREY_IE1.md` §§3–5.1, §§7–11; Lane 2
`side-agent/z83-bcm-ldiv:notes/z83/BCM_TS_LDIV.md` §§1–2; z76 `IE1_BREAK.md` §4; `LOGIC_BEZOUT_NORM_COLLECTION.md` §4;
`data/z66/ie1/lit_ie1.md` §6; the R1 audit `REVIEW_IE1_DECIDER_PI_OPUS2.md` (its verdict table only). Primary literature:
Jeřábek, *Induction rules in bounded arithmetic*, arXiv:1809.10718v2 = Arch. Math. Logic 59 (2020) 461–501, §§3, 5
(downloaded and read).
I wrote this verdict **before** opening `REVIEW_IE1_DECIDER_R2_OPUS.md`.

ES in ℕ is OPEN. Nothing below says `IE₁⁻ ⊢ ES` or `IE₁⁻ ⊬ ES`. Both theorems concern a relaxation or the logic of the
question, not ES.

## Bottom line

| Claim | Verdict | Deserved label |
|---|---|---|
| **(I)** `T_Π`: full `T_F` package + all of `DL` + `¬ES(P)`, `P≡1 (840)` prime, `−1` nonsquare mod `P`; §9 quintic failure; `IE₁⁻` status UNKNOWN | **ACCEPT WITH MINOR FIXES** (I-m1…I-m7). No gap found in any load-bearing step. | **PROVED (rel. z81 §§2–5,7,11–12, z82 §§7–11, ACVF quantifier elimination, henselization, Gauss valuations, PA CRT)**, at the campaign's usual detailed-sketch standard. The z82-queue preservation in §8 is an **interface audit**, not a replay; say so. RECORD for the relaxation. |
| **(II)** §10: `U`, `IE₁⁻` and `IE₁` have the same `∀E₁` consequences; hence `IE₁⁻ ⊢ ES ⇔ IE₁ ⊢ ES`; hereditary characterization | **ACCEPT WITH FIXES** (II-F1 attribution, required; II-m2…II-m4 minor). The mathematics is correct. | **PROVED, a known result** (Kaye, *Diophantine induction*, APAL 46 (1990), as credited in Jeřábek 2020 §5; cf. Cordón-Franco–Fernández-Margarit–Lara-Martín, J. Logic Comput. 19 (2009); the hereditary characterization is the ordinary-language analogue of Jeřábek Cor. 3.4). Label it as a direct verification of a **known** theorem, not a new result. The TARGET simplification ("one common provability question") stands. |

The main correction is to **(II)**. The literature already contains the conservation theorem. The note says "no priority
claim", but its §0 Result line and the STATUS delta present §10 as a campaign theorem. Jeřábek, in the paragraph
introducing his Theorem 5.1, writes: "an analogous result for `IE_n⁻` was shown earlier by Kaye [29]". Ref. [29] is
*Diophantine induction*. The campaign's own digest (`lit_ie1.md` §6) also records that Kaye's main theorem "is proved by
means of a conservation result relating parameter and parameter-free induction schemes". So the STATUS line should read
"IE₁⁻ proves ES iff IE₁ does (Kaye 1990 conservation; direct proof IE1_DECIDER §10)".

---

## (I) `T_Π`

### (a) `IE₁⁻ ⊢ DL` — ACCEPT

* **The gcd step.** At a state `d·e=h`, `d=j<h`, `0≤x<d`, `F(x)≡a (d)`, take `g=gcd(b,e)`. This exists by Bézout in `IE₁⁻`
  (z79 §4). If `g=1`, then `e>1` divides `h` and is coprime to `b`, which is the escape. Otherwise, since
  `G(x+dt)−G(x)=dt·Q(x,dt)` with `Q` an explicit integer polynomial,
  `[F(x+dt)−F(x)]/d = t(1+bQ) ≡ t (mod g)` because `g|b`. Choose `t≡−(F(x)−a)/d (mod g)`, `0≤t<g`. The new quotient is
  `((F(x)−a)/d+t)/g + t(b/g)Q`, which is explicit, needs only `g|b` and `g|(q+t)`, and is bounded polynomially. Then
  `x+dt ≤ d−1+d(g−1) < dg` and `dg | de = h`. Progress is `d' = dg ≥ 2d ≥ j+1`. At `j=h` the only non-escape state has
  `d=h`. The measure is the divisor `d≥j`, with no exponent and no factor list. **Correct.**
* **E₁ shape and parameter-freeness.** The state is a bounded ∃ over `(d,e,x,q)`, or over the escape `(d',e',u,v)` with
  `ud'+vb=1` and `|u|≤|b|+1`, `|v|≤d'` after reduction (division in `IE₁⁻`). Coefficients are packed with sign bits into
  the z79 unary block code. The step uses gcd and division, which are earlier `IE₁⁻` theorems, and isqrt for decoding.
  No named prime and no `D₂`-type universal guard appear in the matrix. This matches R1 §1, which the R1 audit already
  accepted.
* **"Non-escape ⇔ `b mod h ∈ Jac(R/hR)`"** (`h>1`, Bézout). If an escape `d` exists, Bézout gives `t` with `d | 1+bt`,
  so `1+bt` is a nonunit mod `h`. Conversely, if `1+bt` is a nonunit mod `h`, then `d=gcd(1+bt,h)>1` and
  `gcd(d,b) | gcd(1+bt,b) = 1`. **Correct.**
* **Sanity check (mine, not committed; `/tmp`, `ulimit -v 6000000`).** I simulated the exact state machine, with
  assertions on the difference identity, `dg|h` and `0≤x'<dg`. The sample was all `1≤h≤120`, 40 random `(a,b,G)` each,
  `|b|≤15`, and `G` of degree ≤3 with coefficients in `[−5,5]`: 4800 instances, 0 failures. It also confirmed three
  equivalences: non-escape ⇔ every prime of `h` divides `b` ⇔ `1+bt` is a unit mod `h` for all `t`. A second script
  checked the §8 horizontal iteration `v↦a−bG(v)` on 20 000 random cases with `t | b^j`: `j` iterations give a solution
  mod `t`, 0 failures.

### (b) The new edge — ACCEPT

* **Branch.** At `l|h` every PA prime divides `b` arithmetically, so `w_l(b)≥1`. `a`, `b` and the coefficients of `G` lie
  in `R_A`, hence are integral at the unique `w_l`. `f=U+bG(U)−a` reduces to `U−ā`. Uniqueness of the integral root in
  the valued algebraic closure holds: `f(u)−f(v) = (u−v)(1+b·[G(u)−G(v)]/(u−v))`, and the bracket is integral for
  integral `u,v`. The value of `u(α_l+hT)` does not depend on the choice of extension of `ν_l` to `E(T)^alg`, because
  Galois conjugation carries the integral root to the integral root. The pullbacks are injective, and the restriction to
  `E` is `w_l`, so constants contract. `x` and `(F(x)−a)/h = T(1+b·integral)` are integral at `l|h`. At `l∤h` the integrality
  of `x` and of `(F(x)−a)/h` is trivial (`h` is a unit there).
* **Invariant 1 (single PA profile).** The annihilator `Res_U(f', VZ−N)` is uniform in `l`. Here `f'` is `f` with the
  factors whose roots are roots of `V` removed, and `α_l` is a root of `f'` because `V(α_l)=0` would make `T`
  algebraic over `E`. A root value is one of finitely many `(ν c_i−ν c_j)/(j−i)`, with the `c_i∈E(T)` carrying
  provisional profiles. Selection uses one existential `L_div` formula: integral root of `f`, plus a cleared valuation
  comparison. ACVF has QE in `L_div` uniformly over all residue characteristics (Robinson), so a single QF Boolean
  combination works for every `l`. Its atoms `v(p)≤v(q)` with `p,q∈ℤ[params]` become PA comparisons of provisional
  profiles, and equality atoms do not depend on `l`. The values lie in the PA group by immediacy. Outside the union of
  supports all candidates are 0. Patching with the provisional profile off `h` gives one `γ∈K`. **Correct.**
* **Invariant 2 (simultaneous digits at `d∈C`).** I checked the three-part structure: (a) existence in a host; (b) one
  QE list in the variable `z`, evaluated at the generic disc point `z+dU`; (c) scalar coefficient representatives modulo
  `d^{1+max n_i}` plus PA CRT.
  * Disc invariance of `Φ_l` is immediate.
  * At the generic point, `v(L_i(z+dU)/m_i)` is the Gauss minimum, which lies in `[0, n_i v_l(d)]`. Translation by an
    integral `z` preserves primitivity, and the `k`-th Taylor coefficient is multiplied by `d^k`. So precision
    `d^{n_i+1}` determines it.
  * Hence `Ψ(l,z)` is a PA formula, uniform in `l`, with finitely many scalar parameters.
  * The host step needs (E(T),ν_l) to embed over `K` into the henselian field sort of an elementary extension of the
    pair `(B,l) ≺ (∏ℤ,∏ℚ_λ)/U`. The provisional line is an ordinary z81 §3 free line, so z81 §12's edge induction
    supplies this embedding. The henselization's universal property then extends it to `E(T)^h ⊇` the image of `E(x)`.
  * Reflection of `∃z Ψ(l,z)` to `B` holds for each actual `l`. Since the `l | gcd(d,h)` are actual elements of `B`,
    the internal statement `∀l | gcd(d,h) ∃z Ψ(l,z)` holds, so internal least selection and CRT apply.
  * Off `h`, the content-multiplier trick is correct (the multiplier is a unit on the unselected part).

  **Correct.** The note rightly stresses that pointwise QE with unbounded precision would not suffice.
* **Order placement (the prompt's "order placement of `x`!").** `x = hHξ` with a fresh relative residue. `x` is **not**
  the solution. The solution is `x₀ = x − h⌊x/h⌋` in the uncut `R`, which floors its real closure (z81 queue). Since
  `x₀ ≡ x (mod hR)`, `(F(x₀)−a)/h ∈ R`. Then `0≤x₀<h` and the bounded quotient put both in the cut. (Incidentally
  `x ≤ H^{j+1}` is itself in the cut, which does no harm.) The note says this ("after floor completion").
* **All `(h,a,b,G)`, including `h∉C` and new elements.** For a general modulus `s>0` with no escape, write `s = h·t`
  (scalar content × finite primitive horizontal part). Each scalar prime of `h` and each horizontal prime `π | t` must
  divide `b`, because an arithmetic prime not dividing `b` is coprime to it. `t | b^j` for ordinary `j` follows from the
  UFD plus content 1. The iteration and two-modulus CRT then finish. The support condition persists, and the fair queue
  dovetails by stage and index. **Correct.**

### (c) Discreteness and preservation — ACCEPT (interface audit)

* **Leading-coefficient bound.** `R(T) = Res_U(f(U), g(U+hT)) ≠ 0`, because `T` is transcendental over `E(α_i)`. Take a
  common freeze depth `(s,D)` for `R` and `g(T)`. Write `T = s+Dτ` with `τ` integral at every place. Then
  `ν(g(α_i+hT)) ≥ Gauss_U g(α_i+hs+hDU)` for every root `α_i ∈ E^alg`. Multiplicativity of the Gauss valuation over
  `E^alg`, together with the freeze `ν(R(T)) = Gauss(R(s+DU))`, forces equality termwise. Nonnegativity on the selected
  branch then gives `ν_l(b_n(hD)^n) ≥ 0` at `l|h`; off `h`, `ν_l(b_n D^n) ≥ 0`. **The argument is valid**, including
  repeated or non-integral roots.
* **Hull, invariant 3.** By old discreteness `|b_n|(hH)^n ≥ (H/D)^n`, which is unbounded over `F` since `D∈C`. By
  relative Gauss at a fresh `ξ̄`, every positive-degree element of `R_new`, even divided by `c∈C`, lies outside
  `hull(F)`. Constants contract to `R_A`. Hence `C` stays initial, the new ring is discrete, and sizes and residues are
  preserved. The note's remark that the scale `h` alone fails (`F=X, a=0`) is right.
* **Factor calculus, Bézout, `(Sep)`.** `R_new` is *all* integral elements of the UFD `A[x]`, whose units are `K*`, with
  one valuation per PA prime and PA profiles. So a content-normalized upper prime is an arithmetic prime, the
  scalar-content × horizontal gcd exists, and z82 §10's content-coarsened valuations are valuations. None of this uses
  a finite presentation of `R_new`. Rows (Bézout), the support partition (`(Sep)`), the Lag spheres and the Dirichlet
  lines all run over any base satisfying invariants 1–3.
* **z82 queue.** I checked the dependencies that could break:
  * §5.1/§7 use the sandwich of a line relative to the **current** `S`, whatever it is.
  * §8 uses Gauss over the gcd domain `S` plus invariant 3.
  * §9 needs only that each edge is generically affine space, a row line or a sphere; the new edge is an affine line.
  * §10 needs per-place embeddings, which the henselization supplies, together with content-coarsened valuations, the
    collision lemma, and §3.1/§3.2 for degree 2.
  * The only z82 lemma that uses regular **vertical** fibres is §4.1. It feeds the Round 1 `kP` theorems in `T*`, which
    are not part of `T_F`'s Round 2 package. §3.2's UFD after quadratic base change is about upper algebras.

  So the queue does run over the new edge type, and the note's §8 claim is correct. It is still an interface audit of
  roughly ten cited lemmas, not a replay, which is why I ask for the label qualifier.
* **PW, factorial strings, Lag, Dirichlet** come from the z81 §2 cut lemma and the unchanged `H`, `C`. They are
  unaffected.

### (d) `¬ES(P)` — ACCEPT

This needs no specialization of the new edge. That is the right answer to the prompt's worry about Hensel solvability
of the specialized congruence and the failure of finite presentation.

The argument:
* On `Frac(A)(x)`, the `−deg_x` valuation kills `1/u_i` for every positive-degree `u_i`.
* The residue identity is `4/P = Σ_{const} 1/u_i`. Subtracting it from the actual identity shows that the omitted terms
  have sum 0. They are positive in the order, so none are omitted.
* All three `u_i` therefore lie in `A ∩ R_new = R_A`, positive. Descent continues through the earlier, unchanged
  history, and the z81 §4 thick odd-square argument is applied **only at the seed**, whose valuations are untouched.

The descent uses only the upper ring `A[x]`, positivity, and the contraction of constants. It is insensitive to
`R_new` being non-finitely-presented. (The note's phrase "positivity forbids omitted positive terms" is the subtraction
argument above; correct.)

### (e) `P` — ACCEPT

* **`P` is prime.** Prime in `A[x]`, and `ν_l(P)=0` at every new valuation because `P∈A`, so `P|uv` in `R_new` gives a
  quotient in `R_new`.
* **`P≡1 (840)`** persists.
* **`−1` is nonsquare mod `P`.** `R_new/PR_new ↪ (A/P)[x]`, which is purely transcendental over the old fibre, and the
  old fibre has no `√−1`.

### (f) §9 and the `IE₁⁻` status — ACCEPT

* At `p>C`, `p|h`, the residue field of `E(x)` lies inside that of `E(T)^h`, which is `k_old(t̄)` (immediacy, Gauss
  provisional line at `p∉C`). That is a regular extension, so `X²−P` gets no root in `R/pR`, and `R/pR` maps into the
  residue field.
* At `p∤h` the new edge is Gauss. The reserve-prime scalar roots of `P` persist.
* Lane 2 §1's hypotheses 1–2 therefore hold, and the quintic `h²|(1+u)((1+u)²−P)²` has hits and no least element.
* DL itself forces only the trivial first digit `X≡a (p)` when `p|b`.
* The `IE₁⁻` status "UNKNOWN" is honest: the quintic has the nonstandard parameters `h,P`.

### Minor fixes for (I)

* **I-m1 (label).** §0/§6: append "(§8 preservation of the z82 Farey/Thue/reduction queue is an interface audit of the
  cited lemmas, not a replay)".
* **I-m2.** §7, invariant-2 host step: say explicitly that the provisional `T`-line is an ordinary z81 §3 free line, so
  z81 §12's edge induction gives its embedding, and that the henselization's universal property then extends it.
* **I-m3.** §8 mixed moduli: state that content-normalized upper primes are arithmetic primes of `R_new` because `R_new`
  is *all* integral elements. This is the reason a horizontal `π∤b` is coprime to `b`, and it should be flagged as the
  point where "all everywhere-integral elements" (rather than the dilatation) is used.
* **I-m4.** §8 order paragraph: one sentence saying `x` itself is not the solution and `x₀ = x − h⌊x/h⌋` is taken in the
  uncut `R` (an integer part of its real closure). The text says "after floor completion" but is easy to misread.
* **I-m5.** §8 discreteness: name invariant 3 (`S_new ∩ hull(F) = F`) as the target of the leading-coefficient bound;
  `C` initial and the integer part follow as in z81 §4.
* **I-m6.** §9 or the table: add the immediate consequence that **`T_Π ⊭ IE₁`** (with parameters). The quintic is an
  `E₁` least-number failure with parameters, and `IE₁ ⊢ LE₁` (Smith NDJFL 1993; Wilmers 1985, both in the digest). The
  same holds for `T_F`. This makes the "IE₁⁻ UNKNOWN" row sharper and fits §10: `T_Π` cannot bear on `IE₁ ⊢ ES` either.
* **I-m7 (wording).** §6 says "moduli `h∉C`" in places where the task set is "all positive **cut** scalars `h`",
  including `h∉C`. Keep that phrasing uniform.

---

## (II) §10

### Definitions

* `E₁`: bounded-∃ prefix (term bounds) over an open matrix.
* `IE₁⁻`: PA⁻ plus parameter-free `E₁` induction.
* `IE₁`: with parameters.
* `IOpen`: open induction with parameters.
* `IR`: the Hilbert rule on **theorems**, with parameters universally closed.
* `U`: the closure of `IOpen` under `IR`.

These are stated correctly, and the note correctly separates rule-on-theorems from hereditary closure.

### Lower inclusion `U ⊆ IE₁⁻` — ACCEPT with one omission (II-m2)

* **Closure of `IE₁⁻` theories under `IR`.** Pack `(p,H)` into the z79 block `y=m²+i` and ask for `V(min(i,H),p)`. Block
  starts use the theorem `∀p V(0,p)`; steps inside a block use `∀i,p(V(i,p)→V(i+1,p))`. Instantiate at `y=m²+i` with
  `m ≥ code(p,i)`, so `i ≤ 2m`. Correct.
* **`IOpen ⊆ IE₁⁻` is needed and not proved in §10.** z80 `IE1_SPLIT` §0 asserts `IE₁⁻ ⊢ T ⊇ IOpen`. A one-line proof:
  for open `φ(x,p)` induct on the parameter-free `E₁`
  `ψ(y) := [φ(0,p) → ∃j<min(i,H)(φ(j,p)∧¬φ(j+1,p)) ∨ φ(min(i,H),p)]`,
  which is `E₁` because `¬φ` is open. Its step is pure logic. This gives the counterstep form of open induction. Cite z80
  or insert this.

### Upper bound — ACCEPT (I verified it line by line, and it is Jeřábek's Thm 5.1 proof pattern)

* **Step 1 (calculus).** The induction inference `Γ,V(i,p) ⇒ V(i+1,p),Δ / Γ,V(0,p) ⇒ V(t,p),Δ`, with eigenvariable `i`,
  presents `IE₁`. `PA⁻`'s difference axiom is `∀x<y∃z≤y(x+z+1=y)`, which is `∀E₁`; as an eigenvariable left rule or an
  anchored initial sequent it introduces only `E₁`/open formulas. `IOpen` enters as the `∀E₁` counterstep axioms, so no
  open-induction inference with `E₁` side formulas needs separate treatment. (If it is kept as an inference, it is
  translated by the same `IR` step, which `U` has.)
* **Step 2 (free-cut elimination).** Standard (Buss, *Handbook of Proof Theory* ch. II, free-cut elimination with
  induction inferences). Every formula in the proof is a term-instance of a subformula of the end sequent, of an
  induction formula or of an axiom. All of these are `E₁` or open, and a guard conjunct plus a block suffix is `E₁`.
  `¬` occurs only inside open matrices. So **no negated `E₁` and no bounded ∀ formula ever appears on either side**.
  Multiple succedent formulas are disjunctions of `E₁`, which is `E₁` because `ℕ`-bounded domains are nonempty (pad with
  0).
* **Step 3 (absorption).**
  * Antecedent `E₁` side formulas, and `V(0,p)`, are replaced by fresh witness variables with open certificate `W`, as in
    Jeřábek's proof: "replace each formula `∃u≤s ψ(u)` in Γ with `v≤s∧ψ(v)` …".
  * `χ(i) = ¬W ∨ δ ∨ V(i,p)` is `E₁`.
  * Base: `W→V(0,p)` holds openly.
  * Step: if `¬W∨δ`, carry it; else use the translated premise. `i` is not free in `W,δ` (eigenvariable condition), and
    `δ` may contain `E₁` formulas in other variables.
  * `IR` with parameters `(p,w,…)` gives `χ(t)`, i.e. the conclusion sequent after the ∃-left on the witnesses.
  * Contraction and multiple succedents are handled by the disjunction.

  **Correct.**
* **Literature consistency.** I found no contradicting result. This is exactly the bounded-ordinary-language analogue of
  "`IΣₙ` is `Π_{n+1}`-conservative over `Σₙ-IR` ⊆ `IΣₙ⁻`", and of Jeřábek Thm 5.1 ("`T+T^i_2` is `∀Σ̂^b_i`-conservative
  over `T+Σ̂^b_i-IND^R`"). The `IE_n⁻` case is credited there to **Kaye 1990**. The hereditary characterization is the
  analogue of Jeřábek Cor. 3.4 ("`Γ-IND⁻` is the weakest theory all of whose extensions are closed under `Γ-IND^R`"),
  and its proof is identical (deduction theorem for one-sentence extensions). Jeřábek Lemma 3.3 (parameter removal from
  **rules**) is the bounded analogue of the packing direction. Kaye's "`∀E₁(ℕ) ⊢ IE₁⁻`" (quoted in z76 §4) is
  compatible.

### Is ES literally `∀E₁`? Bounded vs unbounded

* **The form of ES.** As written, ES is `∀n≥2 ∃x,y,z≥1 (4xyz = n(xy+yz+zx))`, which is `∀∃`(open), not literally `∀E₁`.
* **The bound is a `PA⁻` theorem.** For a sorted triple `x≤y≤z`, `4xyz = n(xy+yz+zx) ≤ 3nyz` gives `4x≤3n` by
  cancellation. Then `(4x−n)yz = nx(y+z) ≤ 2nxz`, with `4x−n ≥ 1` because the left side is positive, gives `y ≤ 2nx`.
  Then `((4x−n)y−nx)z = nxy` gives `z ≤ nxy ≤ 2n⁴`. All of this is ordered-semiring algebra plus an open case split for
  sorting, so it holds in `PA⁻`. Hence `PA⁻ ⊢ ES ↔ ES_bdd` (bound `2(n+1)⁴`).
* **Consequence.** The biconditional holds for **either** reading:
  `IE₁ ⊢ ES ⇒ IE₁ ⊢ ES_bdd ⇒ U ⊢ ES_bdd ⇒ IE₁⁻ ⊢ ES_bdd ⇒ IE₁⁻ ⊢ ES`. The converse is trivial.
* **Sources.** `LOGIC_BEZOUT_NORM_COLLECTION` §4 states exactly these "ordered-ring bounds `x≤3p/4, y≤2px, z≤pxy≤2p⁴`".
  z76 §4 calls ES "itself `∀E₁`". The note should say "**`PA⁻`-provably equivalent to** a `∀E₁` sentence" (II-m3).

### Fixes for (II)

* **II-F1 (required: attribution and label).**
  * §0 Result, §10 heading and the STATUS delta should credit the conservation to **Kaye, *Diophantine induction*, APAL 46
    (1990) 1–40**. Jeřábek 2020 §5 credits it to Kaye, and the model-theoretic bounded version is Cordón-Franco,
    Fernández-Margarit and Lara-Martín, J. Logic Comput. 19 (2009) 123–143.
  * Cite the hereditary characterization as the analogue of Jeřábek 2020 Cor. 3.4 (and Beklemishev / KPD for `IΣₙ⁻`).
  * Label: "PROVED (known: Kaye 1990; direct verification here)".
  * STATUS §2 item 4 wording: "IE₁⁻ proves ES iff IE₁ does (Kaye 1990 ∀E₁-conservation; IE1_DECIDER §10)". Otherwise a
    reader of STATUS alone would take a 1990 theorem for a z83 result. The TARGET triage (merging the two provability
    questions) is still right.
* **II-m2.** Cite z80 (or add the `ψ` proof above) for `IOpen ⊆ IE₁⁻`, which `U ⊆ IE₁⁻` needs.
* **II-m3.** Replace "so ES is `∀E₁`" by "ES is `PA⁻`-provably equivalent to its bounded `∀E₁` form (ordered-ring bounds
  `x≤3n/4`, `y≤2nx`, `z≤nxy`)".
* **II-m4.** Step 2: cite Buss, Handbook ch. II, for free-cut elimination with induction inferences. Jeřábek's locators
  are verified: Thm 5.1 is in §5, its proof gives exactly this side-formula absorption, and Lemma 3.3 is the rule
  parameter removal. Also state that the subformula property is what excludes `¬E₁` formulas, since the end sequent,
  induction formulas and axioms are all `E₁`/open.

---

## What I tried that did not break

* A nonunit `b` with `G` linear (`F=(1+bc)X`). This is consistent: Jacobson-radical non-escape makes `1+bc` a unit.
* Moduli `s` involving the horizontal `P` (non-escape forces `P|b`, so the root is trivial).
* Pure dyadic `h∉C` at the old `T_F` miss `X+2X²≡P`. This is now repaired upstairs; it puts `√(1+8p)` into the vertical
  fibre, which `T_Π` is allowed to have, because no z82 Round 2 lemma uses regularity of vertical fibres.
* Hull failure through small leading coefficients (excluded by the resultant bound).
* A hidden use of finite presentation in descent (none; descent is on `A[x]`).
* `ν` depending on the choice of extension to `E(T)^alg` (it does not).
* Internal CRT over a non-coded set of primes (avoided by reflection for each actual `l`).
* Negated-`E₁` cut formulas in §10 (excluded by the subformula property).
* The bounded vs unbounded ES form (`PA⁻` equivalence).

Scripts: `/tmp/opus2tpi/dl.py` and `/tmp/opus2tpi/it.py` (not committed; one engine; finite `ℤ` sanity only, not a test
of the nonstandard tower).

## Postscript (written after the verdict above; `REVIEW_IE1_DECIDER_R2_OPUS.md` on `side-agent/z83-ie1-decider` then read)

The postscript does not change any verdict above.

* **Agreement.** Both reviews give ACCEPT WITH FIXES for §§6–10, read §8 as an interface audit against z81 §3 and z82
  §§7–11, and accept the free-cut translation (`¬W` open; `δ` and `V` are `E₁`).
* **New here.**
  1. *II-F1:* the conservation theorem is **already in the literature for `IE_n⁻`: Kaye, *Diophantine induction*
     (1990)**, credited as such in Jeřábek 2020 §5, and in bounded arithmetic Cordón-Franco–Fernández-Margarit–Lara-Martín
     (2009). The earlier report's caveat cites only the analogy with Parsons/Beklemishev/Jeřábek. The STATUS line should
     credit Kaye.
  2. *II-m3:* ES is `∀∃`, and its equivalence to the bounded `∀E₁` form is a `PA⁻` theorem. The earlier report repeats
     "ES is `∀E₁`".
  3. *II-m2:* the missing `IOpen ⊆ IE₁⁻` step.
  4. *I-m6:* the explicit consequence `T_Π ⊭ IE₁` via `IE₁ ⊢ LE₁`.
