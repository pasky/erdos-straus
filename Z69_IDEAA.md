# Z69_IDEAA — informed ideation after absorbing the campaign: 21 raw ideas, 5 shortlisted, 4 first tests run — no mechanism, no HOT LEAD

**ES is OPEN.** Nothing here proves, disproves, or shows unprovable any form of the Erdős–Straus conjecture.
Lane IDEAA of wave z69 (brief `z52bbriefs/z69_lanes.md` §IDEAA; common rules and falsifier table of
`z52bbriefs/z58_lanes.md`). Scripts `scripts/z69_ideaa_*`, data `data/z69/ideaa/`. Labels: PROVED / CERTIFIED /
EVIDENCE / CONJECTURE / Assessment. Internal only; nothing externally refereed. No provider / auth / quota error
occurred in this lane. (The internal hostile review ran through the `review` tool in deep mode; the tool reported the
reviewer model as `openai/gpt-6-astra` — see §6.)

**Verdict: null (blunt): no mechanism found.** I read OPERATIONS, FRONTIER §§1–4, §6, the z58–z68 blocks, the z61
board memo, and grepped the ledger for every idea below. In the form I could state them, the arithmetic re-encodings
of §1 either reduce to the tied divisor event B2, or are already proposed in the repository, or have no forcing lemma;
I say which, idea by idea. **This is "no mechanism found", not a closure of the 21 directions:** several dismissals
are of one stated form only (ideas 6, 7, 8, 11 (e = p + 2), 12, 13, 19 in particular; see §7). Four first tests were
run (§3).
The first version of this memo contained several false or over-scoped statements (a wrong hypothesis in Lemma T, a
false "trace" lemma, a sign slip, an ill-defined generating function, a false remark on the Lyness map, over-broad
"dead" verdicts); the hostile review found them and they are corrected or withdrawn below (§6). What survives is modest:

* **T2 (census CERTIFIED by one engine to 10¹⁰; independently recomputed to 10⁷ by the internal reviewer and to 10⁸
  by the cross-model reviewer, and at the extremes by both; fits
  EVIDENCE; the statistic and range are new, the methodology is not).** The α-class search cost
  K(p) = min{ab : p lies in a Type I-α or Type II-α class mod 4ab} for all 56 876 600 primes p ≡ 1 (24), p ≤ 10¹⁰:
  max K = 5777 (p = 1 775 179 561); tail −ln P(K > Q) ≈ κ(ln Q)^j with fitted j ≈ 2.2–2.3 on Q ≤ 4000 (κ₂ ≈ 0.215),
  approximately stable across the decades 10⁷–10¹⁰; the 14 largest attained values of K all occur at Mordell-class
  primes. No hardness statement follows; idea CPLX does not go beyond `Z58_LOGIC.md` Thm 3.1.
* **T2b (same census; refutes one rescue hypothesis).** At every reported threshold 21 ≤ Q ≤ 3152, Type I-α and
  Type II-α failures to depth Q are positively dependent: P(both)/(P(I)P(II)) grows from 2.2 to 660,
  θ = ln P(both)/ln P(II) ∈ [1.215, 1.420]. (At Q ≤ 9 the dependence is *negative*: ratio 0.889 at Q = 5.) So
  same-cap rescue of Type II-α by Type I-α via inversion is refuted at these depths; eventual pointwise
  complementarity is not excluded by such data (`Z57_COMPLEMENT.md` makes the same distinction).
* **T1 (EVIDENCE; kill fired for one dictionary).** The all-level signed word-count difference O(n) has no
  expression in a 20-function divisor dictionary once trivial words are removed (R² ≤ 0.58).
* **Lemma T (PROVED; negative for the total-norm / sign argument only).** For ℚ(ζ_m)/ℚ(ζ_m)⁺, Artin symbol −1 on an
  ideal means its norm is ≡ −1 (mod m) itself; so the sign-of-the-norm argument I attempted yields only the trivial
  hit. It does not prohibit forcing a *proper* ideal divisor with Artin symbol −1 by some other lemma. Negative norm
  alone forces nothing when the extension is ramified (explicit counterexample at m = 8, a (★) level).
* **T3 (EVIDENCE; pre-registered kill fired).** The slice singled out by factoring ES through ℤ[i] (e = 2a + 1,
  p = a² + b²) succeeds at 5.1 % of primes against 3.5 % for control slices (point-estimate ratio 1.46 ≤ 1.5).
  Not a universal rule; not killed as an enriched selector.

No idea passes F1–F4 as a *mechanism*.

## 0. Mandatory falsifier table (shortlisted ideas; restated in §5)

None of the five ideas, in the form tested, claims positivity anywhere; so none "proves" positivity at the 14 (★)-zero
primes, the 38 𝔊*-zeros, the R₈ zeros or the composite zeros. The cells say how each idea *would* have had to behave.

| idea | F1 odd squares | F2 C-even / numerator 8 | F3 composites | F4 known zeros |
|---|---|---|---|---|
| CPLX (search cost; bounded arithmetic) | no existence content; no Type I/II class contains an odd square (T1), so K(m²) = ∞ — consistent | numerator-blind: the witnessing argument applies verbatim to any numerator on the range where it is solvable (8/p fails at 131, 241; the C-even *line* R₈ has zeros near 10¹⁰); nothing distinguishes 4 | K is defined for every n; primes enter only because ES reduces to primes | uses the α-classes of full ES; a (★)- or 𝔊*-zero merely has its α-witness elsewhere (possibly still Type II, c > 1; e.g. 409: (a, b, c, d, e) = (1, 117, 2, 1, 59)) |
| IDENT-OE (all-level signed-count identity) | W⁻_{4∣t}(m²) = 0 verified (script), i.e. O₄ = −E₄ at odd squares for the 4 ∣ t sub-sums (the unrestricted all-level O is not constrained this way) | the sub-sum t ≡ 0 (8) is the R₈ analogue; an identity giving positivity for both would be refuted at certified R₈ zeros in its range — moot | all n ≡ 1 (4) used; a positivity identity for R would have had to give O₄ = −E₄ at the 285 composite (★)-zeros (a constraint on the (★) count only) — moot | likewise O₄ = −E₄ at the 14 (★)-zero primes (not at the other 24 𝔊*-zeros) — moot |
| INV (inversion ι: p ↦ p⁻¹ exchanges Type I-α ↔ II-α) | ι maps squares to squares: both types fail there | ι is numerator-blind (any numerator M ≡ 0 (4)) | profinite statement, primality-blind | no rescue law found (positive dependence of failures at 21 ≤ Q ≤ 3152) |
| SIGN (CM reciprocity, Lemma T) | forces class −1 (mod m) only of an integer ≡ −1 (mod m); at n = m₀² this would need n + u ≡ −1 (mod 4u), a non-square class — consistent, because the forcing is trivial | m = 4C with C a power of 2 is the ramified case, where even the sign statement fails (§3.3); other even C are not ramified | no primality used | forces nothing at any zero |
| GAUSS-SPLIT (ℤ[i] factorisation ⇒ slice e = 2a + 1) | at p = m², a = m, b = 0: M = ((m+1)/2)², e = 2m + 1; no Type II solution on this (or any) slice by T1 | not examined (no pass earned) | uses a prime p = a² + b² for uniqueness of e | sampled primes only (5.1 % success); not screened at the zero lists — a 5 % slice is not a rule |

## 1. Raw ideas (21), each with its first lemma and an honest screen

Notation: (★) 4uBC − u − B = p. Type II (ET): 4abd = p + e, a + b = ec, giving 4/p = 1/(abd) + 1/(pacd) + 1/(pbcd).
Type I: 4abd = pe + 1, a + b = ec, giving 4/p = 1/(pabd) + 1/(acd) + 1/(bcd). (Both identities checked by hand and by the
reviewer; they hold for arbitrary positive a, b.) "Prior" = already in the repository. "→ B2" = collapses to the tied
divisor event.

1. **CPLX — search complexity and bounded arithmetic.** *Lemma (prior, `Z58_LOGIC.md` Thm 3.1 for (MS)):* a proof in
   S¹₂ yields a polynomial-time witness search (Buss). *Question added here:* how expensive is the obvious search
   (enumerate classes by modulus), and is there a hardness reduction? Tested (T2): cost law measured; **no reduction
   found** (the searcher chooses the slice e, and p + e can be given known factors). *Scope warning (review):*
   `POINTWISE_OMEGA13.md` Thm 5.1 bounds one specific multiplier witness
   W(p) = min{M ≡ 3 (4) : p mod M ∈ {−4D : D | ((M+1)/4)²}} from below i.o. (relative to Gallagher, Nair–Tenenbaum and
   OMEGA10 Thm 3.4); it is **not** a bound for the least modulus over all ET families nor for K, and witness size is
   not a running-time lower bound for arbitrary algorithms (`H4_NOT_POLYLOG.md` gives the same warning). **Narrowed
   to a data point.**
2. **IDENT-OE — identity route with a concrete candidate.** Per level t ≥ 3, with W_t^∓(n) = #{(u, v) ≥ 1 :
   tuv ∓ (u + v) = n}: W_t⁻ = D_t⁻(tn+1), W_t⁺ = D_t⁺(tn+1) − 2, so O_t := W_t⁻ − W_t⁺ = (D_t⁻ − D_t⁺)(tn+1) + 2 is the
   odd-character (Kronecker theta-quotient) component of FRONTIER §2.3 plus the trivial-divisor correction.
   *Lemma sought:* a closed form for O = Σ_t O_t (then R ≥ 1 ⟸ a bound on the sign-free E = Σ_t (W_t⁻ + W_t⁺)).
   *Relation to prior work:* `STRONG_APPROX_ES.md` Thm 9.1 ((J)7) excludes finite n-local Eisenstein-type combinations
   (not every fixed-level or shifted identity); its §9.1 already ran an
   all-level shifted-count dictionary experiment (150 columns, held-out test) on other counts; the board (F3/F4) had
   no candidate formula. This is a different signed count, not exhausted by either. Tested (T1). **Kill fired for the
   tested dictionary only.**
3. **INV — inversion.** ι: p ↦ p⁻¹ (mod 4ab) maps the Type II-α class −e to the Type I-α class −e⁻¹ (same (a, b, e)).
   *Prior:* the symmetry (`POINTWISE_MORDELL17.md` Lemma 1.1; `Z60_LOPEZ.md` Prop E and `Z60_LOPEZT.md` for the U_II
   branches, including inverse-branch least-witness data). *Hypothesis tested:* "p deep in the Type II-α avoider set
   ⟹ p⁻¹ is not". T2b: **refuted at the tested depths.**
4. **TRACE — WITHDRAWN (false as first stated).** I claimed that ι-invariance makes α-avoidance a function of the
   profinite trace p + p⁻¹. Wrong: modulo a composite q the fibres of x ↦ x + x⁻¹ allow *independent local*
   inversions, and the α-system is invariant only under the global ι. Reviewer's counterexample: invert only the
   7-adic component of the profile of p = 7 183 201 (K = 1133); the new profile has the same trace at every modulus and
   an α-hit at ab = 721 (a = 1, b = 721, e = 19). What remains is the global symmetry of idea 3 (so a profile and its
   global inverse are covered together; not checked against the seven-family code of `Z67_K11.md`).
5. **TORUS — group-order encoding.** For a prime d ≡ 3 (4): d ≡ −1 (mod 4C) ⟺ the norm-one torus of 𝔽_{d²}/𝔽_d
   (order d + 1) has a point of order 4C ⟺ 4C | #E(𝔽_d) for E: y² = x³ − x (supersingular at d ≡ 3 (4)). At a (★)
   solution with d = 4uC − 1, d′ = 4BC − 1 both prime (gcd(u, B) = 1), the non-split torus T_{−1}(ℤ/N), N = 4Cp + 1,
   has exponent lcm(4Cu, 4CB) = 4CuB = p + u + B: raising to the p-th power equals raising to the −(u + B)-th. *Prior
   in spirit:* `BRAINSTORM/y3_lucas_dickson_trace.md` (Prop G; genuinely related); z52b item Z1958 is only the much weaker
   prime-level Pocklington anti-certificate. A Lucas-test *certificate*, not a forcing
   step → B2.
6. **SIGN — class forcing by CM reciprocity.** Ideal norms from K⁺ = ℚ(ζ_m)⁺ prime to m are ≡ ±1 (mod m), the sign
   being the Artin symbol for ℚ(ζ_m)/K⁺. Could a sign/reciprocity argument force the class −1 at a tied modulus?
   Lemma T (§3.3): the *total-norm / sign* argument does so only trivially. **Dead in that form.** Not excluded
   (`Z60_RAYCLASS.md` §3 makes the same exemption): a new lemma forcing an Artin −1 *proper* ideal divisor without
   assuming its norm or the factorisation; such a lemma should be screened first at 409 and the R₈ zeros.
7. **GAUSS-SPLIT.** Factor 4/p = (2/π)(2/π̄) over ℤ[i]. *Lemma (PROVED, §3.4):* the solutions of 2/π = 1/α + 1/β are
   α = (π ± 1)/2, β = ±πα (and α = β = π), giving the e-slices e = 1 ± 2a. *Differs from* `Z58_WITNESS.md`
   (two-square data as selectors of d) by deriving one slice. Tested (T3). **Not a universal rule; not killed as an
   enriched selector** (a divisor-matched control is the legitimate next test). (Other nonlinear
   Gaussian rules are lane NL7's brief.)
8. **LYNESS.** For a word, t = (p + u + v)/(uv) ∈ ℕ and (tu − 1, u, v, tv − 1) are four consecutive integer terms of
   x_{k+1}x_{k−1} = x_k + p. The map F(x, y) = (y, (y + p)/x) preserves each curve (x+1)(y+1)(x+y+p) = Kxy of the
   pencil (generically elliptic; F is a translation on it), and a word is an integral point P with F^{±1}(P)
   integral, on the fibre K = t(u+1)(v+1) determined by the word itself. *Related prior:*
   `BRAINSTORM/z52b_translate.md` #49, `y2_zamolodchikov_forcing.md` (twisted period-5 version). Assessment: no
   argument selecting a fibre and forcing integral neighbours is supplied. **Left open, not ruled out** (the cited
   prior items concern the twisted version and are no no-go for this autonomous pencil); a restart would choose K(p)
   independently of a known word and test integral neighbours on F1–F4.
9. **E₂-FORM.** For gcd(e, p) = 1 (automatic when e < p): Type II at slice e ⟺ M² has a divisor f ≡ −M (mod e),
   M = (p + e)/4 (then the cofactor is ≡ −M too) ⟺ p(k + 1) = 4(kM − f) with f | M², k the witness modulus 4acd − 1.
   Classical two-unit-fraction criterion; restatement → B2.
10. **TYPE-I-FIXED.** For a prime p: Type I ⟺ some *p-independent* integer 4a²d + 1 has a divisor f ≡ −p (mod 4ad)
    (f = 4acd − p; conversely c = (p + f)/(4ad), e = (4a²d + 1)/f, b = (pe + 1)/(4ad); cross-review's derivation).
    *PROVED restricted statement:* if d is a square, every divisor of 4a²d + 1 is ≡ 1 (4) ≠ −p, so square-d slices are
    sterile (in line with `SYNTHESIS_SPARKS8.md` Lemma 4.1 / (J)89 Lemma 4.1). *Correction (cross-review):* my claim
    that algebraic factorisations of 4dm² + 1 need d square was false: d = 4m²k² − 2k gives 4dm² + 1 = (4m²k − 1)², and
    at m = 1, k = 6 (d = 132, non-square) the prime p = 1033 ≡ 1 (24) has the Type I point
    (a, b, c, d, e) = (1, 45, 2, 132, 23). Such factorisations give ordinary ET congruence families (B1), not a new
    mechanism; but there is **no blanket algebraic sterility**. No forcing lemma proposed.
11. **ALG-SLICE.** Type I slices with (pe + 1)/4 a perfect square: e = p ∓ 2 gives ((p ∓ 1)/2)². *Lemma (PROVED):* for
    p ≡ 1 (8) no solution lies on e = p − 2: a, b | ((p−1)/2)² makes p ≡ 1 modulo every odd prime of ab, hence a
    square mod 4ab, contradicting `JOINT_BUDGET.md` Remark 4.4 (the Type I extension of Prop 4.3). For e = p + 2 no
    such argument applies; the reviewer found no solution on either slice for p ≡ 1 (8), p < 10⁴ (EVIDENCE; e.g.
    p = 17: N_e = 81, none); the cross-review extended the emptiness to all 19 552 primes p ≡ 1 (8), p ≤ 10⁶.
    **e = p − 2: sterile (PROVED). e = p + 2: empirically empty, unproved** — the open statement is: for
    M = (p+1)/2, M⁴ has no divisor ≡ −M² (mod 2M + 1).
12. **SUBSET-COVER.** Idea: when p + u has many prime factors, a zero-sum / subset-product theorem in (ℤ/4u)^× might
    give a sub-product ≡ −1 (mod 4u) pointwise. *What I can actually state:* the only prime factors of p + u that one
    can force for some u ≤ H are those of a modulus Q ≤ H with u ≡ −p (mod Q) (so ω ≤ (1 + o(1)) log H/log log H), and
    divisors built from them are congruence data on p (B1). *Withdrawn (cross-review):* my threshold
    "ω(p + u) ≳ log₂(4u) is needed" and the appeal to Olson / Erdős–Heilbronn "in general position" were not a theorem —
    a single target can be hit by one factor, and the relevant scales differ (logarithmic for random sets, square-root
    for spread sets, linear in the worst case; `BRAINSTORM/z31_zero_sum.md`). **No mechanism in the form stated; not
    ruled out** — a restart must name the target-specific subset-product theorem and its deterministic hypotheses.
13. **SIEVE-FL.** For fixed p and ℓ ∤ 4p, the residues of 4Cp + 1 mod ℓ over C ≤ T are equidistributed up to O(1) per
    class (so the fundamental lemma is pointwise in p). But a divisor d ≡ −1 (mod 4C) has d ≥ 4C − 1, and each d has a
    unique candidate level C_d = (−(4p)⁻¹ mod d): the naive free-variable argument has no free variable. → B2 for that
    argument; **not a sieve no-go** (a specified tied-incidence weight summing over d is not excluded).
14. **MONOID-DESCENT.** {n : 4Cn + 1 ∈ 𝔬_C·𝔬_C}, 𝔬_C = 4Cℕ − 1, is an ideal for n ⊙ n′ = n + n′ + 4Cnn′, and division
    by primes ≡ 1 (4C) preserves it. Trivial equivalences. *Prior (already proposed, not proved impossible):*
    `BRAINSTORM/z52b_translate.md` #265 / `ES_CONNECTIONS_TODO.md` Z2847; a related coherence item (astra-4) was
    withdrawn on the z61 board (`~/.pi/boards/20261107-es-newmech/memo.md`, outside the repository). **No mechanism
    in this form.**
15. **RSR — worst-case to average-case.** Use E(N) ≪ N exp(−c(log N)^{3/4}) at one p via a family {n_r} such that
    ES(n_r) for one r gives ES(p). The only known links between different n are congruences (same word) and scaling
    (`Z59_CONV2.md` Prop 4.1: no descent into a prime within equation-scaling transports); a new link *is* the missing
    mechanism. **Open, empty.**
16. **UNDEC.** Is "every large n in a class is F(x, y, z), F a cubic with a congruence side condition" undecidable in
    general (Conway-style)? Three variables are far below every known universal Diophantine construction.
    **Speculative; no first lemma.**
17. **INVERSE-SIEVE.** The (★) zero set avoids H_d for every d ≡ 3 (4), every removed class being a Jacobi
    non-residue. Inverse large-sieve results need a positive proportion of removed classes; here |H_d|/d → 0.
    *Related prior:* `BRAINSTORM/bsL_sieve_saturation.md`; size-controlled covering rigidity in `Z58_LADDER.md` (neither
    is an inverse-sieve no-go). **Dead for the unadapted standard theorems only.**
18. **TIE-LADDER.** Relax d ≡ −1 (mod 4C) to (mod 4C/g) *with g² | C*: with C = g²d′ this is exactly the Type II
    family with c = g (`Z59_CONV2.md` Prop 2.1, m = c²d). Linnik gives a divisor ≡ −1 (mod G) of some 4Cp + 1 with
    C ≤ G^L, but C is then not a function of G. **Dead (prior).**
19. **4-TERM-MERGE.** ES ⟺ some 4-term representation of 4/p has a mergeable pair ((c + d) | cd) (split one unit
    fraction into two equal halves for the converse). *Already proposed:* `BRAINSTORM/z52b_analogues.md` #312,
    `z52b_upgrades.md` #208. I have no forced merge / divisibility invariant to offer; **no mechanism, not a no-go**
    (my earlier "polylog count" assertion was unsupported and is deleted).
20. **MIRROR-SIZE.** By ι, Type I-α at p is "Type II-α at the inverse profile without the size cap p ≥ 4ab − e".
    More tickets, same lottery (Assessment). No forcing.
21. **QR-FLOOR.** *Lemma (PROVED, from `JOINT_BUDGET.md` Remark 4.4):* if p ≡ 1 (8) is a quadratic residue modulo
    every odd prime ≤ y, then every class modulus 4ab containing p has a prime factor > y, so K(p) > y. (Prior in
    substance: every hit modulus has a prime factor ≥ n_p; `Z58_LADDER.md` Lemma 1.1(c).) It explains none of the observed tail
    (2^{−π(Q)} ≪ exp(−κ ln^j Q)).

## 2. Kill tests — what was and was not pre-registered (honest record)

Checkpoint discipline was *not* met for T1 and T2: I ran them before committing the memo.
* **T1** — the kill criterion (R² < 0.9 on the dictionary for every level set) was in the script docstring before the
  first run. The first run (all words) gave R² = 0.907 for O over all levels, carried by τ(n ± 1), i.e. by the
  trivial words u = 1. I then restricted to interior words (u, v ≥ 2). That restriction is post hoc; both runs are
  reported.
* **T2** — exploratory; the j = 2 vs 3 comparison and the dependence exponent were chosen after seeing the survival
  table. No pass/fail criterion.
* **T3** — the criterion *"KILL if the success rate of the Gaussian slice e = 2a + 1 on a random sample of 20 000
  primes p ≡ 1 (24), p ≤ 3·10⁶, is ≤ 1.5 × the rate of the control slices e ± 4k, k = 1, 2, 3"* is in §2 of commit
  `e9a856348`, made before the run (results first appear in `5d4e9d133`). **Blemish (found by the review):** the
  summary of that same checkpoint commit already contained an anticipatory line "T3 … kill fired … not better than
  control slices", which I wrote before running T3 while §3.4 still said "to be filled in". That line was a guess,
  not a result; the criterion and sample were fixed beforehand, the outcome claim was premature. The actual run is
  reported in §3.4.
* **Lemma T** — a proof, no kill test.

## 3. First tests

### 3.1 T1 — all-level signed word counts (idea IDENT-OE). EVIDENCE.
`scripts/z69_ideaa_oe.py N UMIN`, data `data/z69/ideaa/oe_fit_umin{1,2}.json`. For n ≤ 6000:
W⁻_T(n) = #{(t, u, v) : t ∈ T, tuv − u − v = n}, W⁺_T(n) = #{tuv + u + v = n}, O = W⁻ − W⁺, E = W⁻ + W⁺;
R(n) = W⁻_{4∣t}(n) (u, v ≥ 1). Generating function (review-corrected), with t₀(u, v) = ⌊(u + v)/(uv)⌋ + 1:
Σ_{n ≥ 1} O_all(n)qⁿ = Σ_{u,v ≥ 1} (q^{t₀uv − u − v} − q^{uv + u + v})/(1 − q^{uv}).
Floating-point least squares on n ≡ 1 (4), n ∈ [3000, 6000] (750 points) against {1, τ(n), τ(n ± 1), τ(n ± 2),
τ(n ± 4), τ(2n ± 1), τ(4n ± 1), (d₁ − d₃) at n, n + 2, n + 4, 4n + 1, d₃(n + 1), d₃(4n + 1), log n, log²n}:

| level set | O, all words: R² | O, interior words (u, v ≥ 2): R² |
|---|---|---|
| all t | 0.907 (carried by −1.96 τ(n−1) + 1.52 τ(n+1): trivial words) | 0.578 |
| t ≡ 0 (4) | 0.591 | 0.391 |
| t ≡ 2 (4) | 0.551 | 0.373 |
| t ≡ 1 (4) | 0.514 | 0.281 |
| t ≡ 3 (4) | 0.752 | 0.145 |

T1 check: W⁻_{4∣t}(m²) = 0 at every odd square ≤ 6000. On primes n ≡ 1 (4): corr(O, E) = 0.23 (4 | t, all words).
An endpoint bug found by the review (the words (1, 2, N+2), (1, N+2, 2) at n = N were missed) is fixed; n = 6000 is
not ≡ 1 (4), and the regenerated JSON files are byte-identical. *Scope:* one dictionary, one range, a signed count
that differs from the theta-quotient component by boundary terms. **Kill fired for this dictionary**; this is not a
statement about every odd-character identity.

### 3.2 T2 — α-class search cost K(p) (ideas CPLX, INV).
`scripts/z69_ideaa_kcost.c`, analysis `scripts/z69_ideaa_kfit.py`, data `data/z69/ideaa/kcost_*.txt`, `kfit.json`,
`kfit.log`.

**Definition.** K(p) = min{ab : a ≤ b, ∃ e | a + b with 4ab | p + e [II-α] or 4ab | pe + 1 [I-α]}, restricted to
p ≥ 4ab (a restriction of the *definition*, harmless here since K ≪ p; the Type I identity itself needs no size
condition). For p ≡ 1 (4) the script's filter e ≡ 3 (4) is automatic, and restricting to gcd(a, b) = 1 does not change
the minimum (reviewer's check). K is an *upper bound* for the least family-class modulus/4: the other cheap class
shapes — II-β (p ≡ −4a²d mod 4acd − 1), II-γ (p ≡ −e − 4a²d mod 4ade), I-γ (p ≡ −e⁻¹ mod 4ad, e | 4a²d + 1), I-δ
(f ≡ −p mod 4cd, f | p² + 4c²d, f small) — are *not* included. Everything below is about α-classes only.

**Census (CERTIFIED: one exhaustive engine to 10¹⁰ — the full range is not independently duplicated. Independent
prime-by-prime searches: internal reviewer, all 34 survival thresholds for the 82 887 primes ≤ 10⁷; cross-model
reviewer, all 137 joint/marginal survival cells for the 719 781 primes ≤ 10⁸ (max joint K = 2388 at 66 306 529;
marginal maxima I: 9499, II: 7348); both, by direct search excluding all smaller products, the extreme values below).** All 56 876 600 primes p ≡ 1 (24), 5 ≤ p ≤ 10¹⁰ have K(p) ≤ 5777, attained at
p = 1 775 179 561 (≡ 1 mod 840, n_p = 41); next 4460 (2 431 459 801), 3657 (278 893 729, the maximum ≤ 10⁹);
K(7 183 201) = 1133 is the maximum ≤ 10⁷. The 14 largest attained values of K (one representative prime each, as
logged) all occur at primes in Mordell's classes 𝔐, with least non-residue 13–41. Type II-α alone: max 35 967
(p = 6 106 475 761); Type I-α alone: max 22 628 (p = 3 280 856 329).

**Tail (EVIDENCE).** S(Q) = #{p : K(p) > Q}:

| Q | 21 | 54 | 108 | 214 | 421 | 824 | 1612 | 3152 | 4927 |
|---|---|---|---|---|---|---|---|---|---|
| S(Q) | 8 290 710 | 2 738 418 | 844 914 | 180 277 | 31 894 | 3 825 | 317 | 13 | 1 |

One-parameter fits on 50 ≤ Q, S ≥ 20 (18 points): −ln(S/N) = κ₂ ln²Q, κ₂ = 0.215 (rms 0.43); = κ₃ ln³Q, κ₃ = 0.0316
(rms 0.78); two-parameter fit with free exponent: j = 2.28. The ≤ 10⁹ census gives κ₂ = 0.213, j = 2.29; the
normalised tail is approximately stable across the decades 10⁷–10¹⁰ (−ln P/ln³Q at Q = 1031: 0.0319, 0.0317, 0.0313).
The local slope steepens with Q, so j may drift towards 3 (the full solution count is ≍ log³); the range does not
decide. Model extrapolation of the *extreme envelope* max_{p ≤ X} K ≈ exp((ln N/κ)^{1/j}) (no error bar; not the cost
at a given p): at X = 10¹⁷: 2.7·10⁴ (j = 3), 1.0·10⁵ (j = 2.28), 2.6·10⁵ (j = 2).

*Prior work on the methodology (review):* fixed-cutoff survival and stretched-exponential extreme scales are in
`FOREST_H4.md` §5; `Z58_WITNESS.md` §2.1 fits exp(−κ log²D) for its witness coordinate; DISCOVERIES records fitted
exponents 2.3–2.6; `BRAINSTORM/z52b_dividing.md` item 312 proposes the cubic-tail extreme-value extrapolation;
`Z60_LOPEZT.md` has inverse-branch least-witness data. New here: this statistic (joint Type I ∪ II α-classes), the
range 10¹⁰, the maxima, and the joint table below.

**Reading for CPLX (Assessment).** Class enumeration finds an ES decomposition after ≈ K(p) moduli; on this evidence
the envelope is exp(O((log p)^{1/j})), j ∈ [2, 3] — super-polynomial in log p, tiny in practice. This is a statement
about one search procedure; the fits establish no tail theorem, no search lower bound and no unprovability. I found no reduction from a recognised hard problem and **claim no conditional
unprovability statement**.

**Joint failure of the two types (census counts CERTIFIED as above; reading EVIDENCE).**

| Q | P(II-α fails) | P(I-α fails) | P(both fail) | θ = ln P(both)/ln P(II) | P(both)/(P(I)P(II)) |
|---|---|---|---|---|---|
| 5 | 0.7500 | 0.7500 | 0.5000 | 2.41 | 0.889 |
| 21 | 0.2578 | 0.2577 | 0.1458 | 1.42 | 2.2 |
| 68 | 0.0634 | 0.0634 | 0.0351 | 1.215 | 8.7 |
| 108 | 0.03657 | 0.03658 | 0.01486 | 1.27 | 11 |
| 421 | 3.258·10⁻³ | 3.259·10⁻³ | 5.61·10⁻⁴ | 1.31 | 53 |
| 1031 | 4.400·10⁻⁴ | 4.374·10⁻⁴ | 2.86·10⁻⁵ | 1.35 | 149 |
| 3152 | 1.90·10⁻⁵ | 1.83·10⁻⁵ | 2.29·10⁻⁷ | 1.41 | 660 |

The two marginals are close at every Q (as the ι-symmetry of the class system and equidistribution of primes in unit
classes suggest; no error analysis was done). For Q ≤ 9 the failures are negatively dependent (the first classes,
p ≡ 17 and p ≡ 13 mod 20, are disjoint). For all reported 21 ≤ Q ≤ 3152 the joint failure exceeds independence, by a
factor growing to 660; θ ranges over [1.215, 1.420] (minimum at Q = 68). A natural explanation (Assessment, not
tested by conditioning) is the ι-invariant data shared by p and p⁻¹, e.g. the quadratic profile
((p/ℓ) = (p⁻¹/ℓ)). **Conclusion:** *guaranteed* same-cap rescue of II-α by I-α is refuted at these depths (positive joint counts). This says nothing about
eventual pointwise complementarity of the full families (`Z57_COMPLEMENT.md`: positive covariance does not forbid
pointwise coverage; pointwise complementarity at primes not excluded for five pairs).

### 3.3 Lemma T — the total-norm / sign argument forces only the trivial hit (idea SIGN). PROVED (review-corrected).
Let m ≥ 3, K = ℚ(ζ_m), K⁺ its maximal real subfield, f the conductor of K (f = m if m ≢ 2 (4), f = m/2 otherwise).

**(i)** For every integral ideal 𝔞 of K⁺ prime to m, N𝔞 ≡ ±1 (mod m), and the sign is the Artin symbol of 𝔞 for
K/K⁺ under Gal(K/K⁺) = {±1} ⊂ (ℤ/m)^×. (A prime 𝔩 ∤ m of residue degree f₀ over ℓ has N𝔩 = ℓ^{f₀}; ℓ mod m is the Frobenius in
Gal(K/ℚ) = (ℤ/m)^×, its f₀-th power is trivial on K⁺, hence lies in {±1}, and it is −1 iff ℓ has order 2f₀ mod m,
i.e. iff 𝔩 is inert in K.) Checked
numerically by the reviewer on 315 prime ideals for m ∈ {5, 7, 8, 9, 12, 15, 16, 20, 24}.

**(ii) Corollary (the triviality).** If any argument forces Artin symbol −1 on an ideal 𝔞 — i.e. an odd number of
inert prime factors counted with multiplicity — then the integer N𝔞 is itself ≡ −1 (mod m). In the level form of (★)
the integer is 4Cp + 1 ≡ +1 (mod 4C): its Artin symbol is +1 and nothing is forced. In the shift form, N𝔞 = p + u
≡ −1 (mod 4u) means p ≡ −1 − u (mod 4u), where d = p + u, B = 1 is already a solution (p = 4uC − u − 1); and
"p + u = B·N𝔞" presupposes the factorisation sought.

**(iii) Sign of the norm (only when f is not a prime power).** Then K/K⁺ is unramified at all finite primes and, for
γ ∈ 𝒪_{K⁺} prime to m, Art((γ)) = ∏_{σ real} sgn σ(γ), i.e. N_{K⁺/ℚ}(γ) ≡ 1 (mod m) as a signed integer (m = 12:
a² − 3b² ≡ 1 (mod 12) whenever prime to 6; e.g. −11). So a negative norm does force an inert prime factor of odd
exponent — of an integer that is ≡ −1 (mod m), by (ii).
*The hypothesis is necessary* (my first version assumed only "m not a prime power" and asserted the prime-power case
similarly; both wrong): for m = 10 (f = 5) the unit ζ₁₀ + ζ₁₀⁻¹ has norm −1 ≢ 1 (mod 10); for m = 8,
N(3 + 93√2) = −17 289 = −(8·2161 + 1) with 2161 ≡ 1 (24) prime, and 17 289 = 3²·17·113 has no divisor ≡ 7 (mod 8). In
the ramified case the local symbol at the ramified prime enters, and the real sign alone decides nothing. Note that
m = 4C with C a power of 2 — (★) levels — is exactly this case.

**Reading (scoped; cross-review).** The *total-norm / sign* argument for ℚ(ζ_m)/ℚ(ζ_m)⁺ forces the class −1 at the
tied modulus only where a congruence on p already gives it. Lemma T identifies a character with a residue; it is
**not** a general no-go: it does not prohibit a different lemma forcing a proper ideal divisor with Artin symbol −1.
For the argument attempted, this is the cyclotomic incarnation of "reciprocity forces parity, never class" (FRONTIER §3;
`Z60_RAYCLASS.md` Prop 3.1), with the reason spelled out: inside the family of K⁺-norms the class is a parity, and
that parity is the residue of the integer itself.

### 3.4 T3 — the Gaussian slice (idea GAUSS-SPLIT). EVIDENCE; pre-registered kill fired.
*Lemma (PROVED; sign corrected by the review).* For a Gaussian prime π = a + bi of norm p ≡ 1 (4) (a odd, b even),
2αβ = π(α + β) ⟺ (2α − π)(2β − π) = π². The divisors of π² are uπ^j (u a unit, j ≤ 2), and 2 | π + uπ^j forces
(j, u) = (0, ±1), (2, ±1) (the swap) or (1, 1). So the solutions are α = (π + 1)/2, β = πα; α = (π − 1)/2, β = −πα;
their swaps; and α = β = π. Multiplying by the conjugate equation, with u = ±1 and M = N((π + u)/2) = (p + 1 + 2ua)/4:
4/p = 1/M + 1/(pM) + 2ua/(pM) = 1/M + e/(pM), e = 1 + 2ua — the positive slice e = 2|a| + 1 and one signed slice.
For gcd(e, p) = 1: Type II at slice e ⟺ M² has a divisor ≡ −M (mod e) (idea 9; gcd(M, e) = 1 is asserted in the
script; the reviewer compared `slice_ok` with an explicit two-factor test on 976 slices: no mismatch).
`scripts/z69_ideaa_gauss.py`; data `data/z69/ideaa/gauss_slice.txt`.

**Result (the pre-registered run; 20 000 random primes p ≡ 1 (24), 1000 < p ≤ 3·10⁶).** Gaussian slice:
1015/20 000 = 5.08 % ± 0.16 %; control slices e ± 4k (k ≤ 3): 4176/119 826 = 3.49 % ± 0.05 % (binomial errors; the six
controls per prime are not independent); ratio 1.456 ≤ 1.5: **kill fired on the point estimate**
(narrowly; the cross-review's paired-prime delta-method 95 % interval for the ratio is [1.364, 1.549], or
[1.409, 1.503] with finite-population correction for the 26 969 eligible primes — so "population ratio ≤ 1.5" is not
statistically established; the enrichment itself is real). A rule needs ≈ 100 %; this slice succeeds at 1 prime in 20.

*Post hoc follow-up (not pre-registered; `scripts/z69_ideaa_gauss2.py`, `gauss_slice_followup.txt`, 8000 primes).*
M = ((a+1)/2)² + (b/2)² has mean τ(M²) = 98.6 against 58.8 for the controls (4 | M with frequency 0.50 against 0.17;
primes ≡ 3 (4) enter only squared), and the crude ticket count (τ(M²) − 2)/φ(e) is 1.70× larger, against a success
ratio of 1.46. So the enrichment is *consistent with* increased divisor availability; the follow-up compares
aggregate means only (no matching on τ, φ(e) or local factors; the crude count also wrongly discards the endpoint
divisors, which can hit, e.g. p = 2089, e = 91, M = 545, f = 1), so a class effect is neither isolated nor excluded.
**Not a universal rule; as an enriched selector it is neither established nor killed.** Lanes NL7 / MINE scoring
Gaussian-norm rules should compare against controls matched on divisor availability, φ(e) and local factors.

## 4. Limits of this memo
* The K census beyond 10⁸ rests on one engine (plus direct verification of six extreme values); K covers α-classes
  only; the tail fits are eyeball fits on 18–23 points and do not determine j (2.2–3).
* T1: n ≤ 6000, one dictionary, a signed count with boundary corrections.
* T3: one slice, one sample; the follow-up is not a controlled comparison.
* Ideas 15 (RSR), 16 (UNDEC) have no test because they have no first lemma that a ≤ 2-hour test could decide; idea 4
  was false.
* Verdicts "dead" in §1 mean: dead in the stated form, for the stated reason — not no-go theorems. Ideas 6 (beyond
  total norms), 7 (as a selector), 8, 11 (e = p + 2), 12, 13, 19 are explicitly *not* ruled out.

## 5. Shortlist (≤ 5), ranked, with the four required items

| # | idea | (i) first lemma | (ii) relation to existing routes | (iii) F1–F4 | (iv) first test, outcome |
|---|---|---|---|---|---|
| 1 | CPLX | S¹₂-provability ⟹ polynomial-time witness search (prior, `Z58_LOGIC` Thm 3.1); cost of class enumeration ≈ K(p) | FRONTIER §3 "Logic" has the witnessing; the α-cost census to 10¹⁰ is new, the tail methodology is not (`FOREST_H4` §5, `Z58_WITNESS` §2.1) | §0 row 1 | T2: max K = 5777 ≤ 10¹⁰, tail exponent j ≈ 2.3; no hardness reduction. **Narrowed to a data point** |
| 2 | INV | ι exchanges I-α ↔ II-α (prior: MORDELL17 L1.1) | FRONTIER §6 z57 "statistical complementarity" tested pair counts; here a depth-resolved joint law for Type I vs Type II α-classes | §0 row 3 | T2b: failures positively dependent at 21 ≤ Q ≤ 3152 (θ ∈ [1.215, 1.42]). **Same-cap rescue refuted**; TRACE withdrawn |
| 3 | SIGN | Lemma T(i)–(ii): Artin symbol −1 ⟹ norm ≡ −1 (mod m) | FRONTIER §3 "reciprocity forces parity, never class" / RAYCLASS Prop 3.1 concern quadratic orders and total products; this is the real-cyclotomic norm version | §0 row 4 | Proof: the total-norm / sign argument gives the trivial hit only; ramified counterexample at m = 8. **Dead in that form** (proper-divisor forcing not excluded) |
| 4 | IDENT-OE | closed form for O = Σ_t [(D_t⁻ − D_t⁺)(tn+1) + 2] | `STRONG_APPROX_ES` Thm 9.1 (finite n-local Eisenstein combinations) and §9.1 (other all-level counts); board F3/F4 (no candidate) | §0 row 2 | T1: R² ≤ 0.58 on interior words. **Kill fired (this dictionary)** |
| 5 | GAUSS-SPLIT | 2/π = 1/α + 1/β ⟹ α = (π ± 1)/2, slice e = 1 ± 2a | `Z58_WITNESS` tested two-square data as d-selectors, not this derived slice | §0 row 5 | T3: 5.1 % vs 3.5 %, ratio 1.46 (pre-registered point-estimate kill ≤ 1.5 fired). **Not a universal rule** |

**What I would and would not fund (Assessment).** Nothing above justifies a lane. If one more bounded test is wanted:
complete the cost census with the β/γ/δ class shapes (the least modulus over all ET family classes to 10¹⁰ and its tail
exponent), and compare it with OMEGA13's specific witness W(p); minutes of compute. The ideation outcome itself is a
data point: an informed pass deliberately looking for non-counting, non-covering, non-local-global shapes (group
order, CM sign, identities across levels, complexity, inversion) found no mechanism: each item ended at B2, at a
prior ledger entry, or without a forcing lemma — and my two attempts at "new lemmas" beyond restatement (TRACE, the first Lemma T) were false as first written.

## 6. Internal hostile review (record)
Run through the `review` tool, deep mode, on commits `e9a856348..5d4e9d133`; the tool reported the reviewer as
`openai/gpt-6-astra` (so this internal review was already cross-model; no provider error). Verdict: *major revision
required*; 10 MAJOR and 6 MINOR findings, **all accepted and applied in this version**:
1. OMEGA13 Thm 5.1 bounds one specific witness, not all family classes or K; all-family / all-search consequences
   deleted (idea 1, §3.2).
2. Lemma T: hypothesis corrected to "conductor not a prime power"; prime-power claim withdrawn; counterexamples
   m = 10 and m = 8 added; the triviality restated via the Artin symbol (§3.3).
3. TRACE lemma false (independent local inversions; explicit counterexample) — withdrawn (idea 4).
4. Gaussian lemma: β = ±πα, diagonal solution, sign of the cross term; gcd(e, p) = 1 stated; script asserts
   gcd(M, e) = 1 (§3.4, idea 9).
5. Generating function replaced by a well-defined one; O identified as theta-quotient component + boundary terms;
   T1 verdict scoped to the dictionary (§3.1, idea 2).
6. "Positively dependent at every depth" was false (negative for Q ≤ 9); θ range corrected to [1.215, 1.420];
   "kills complementarity" replaced by the scoped statement (§3.2).
7. "Fully accounted for by divisor count" withdrawn; follow-up described as uncontrolled (§3.4).
8. False remark that the Lyness map does not preserve the pencil's curves removed (idea 8).
9. TIE-LADDER: g² | C added (idea 18).
10. Falsifier cells corrected ((★)-zeros can be rescued inside Type II, e.g. 409; O = −E; slice-level wording).
11. ALG-SLICE: citation corrected to Remark 4.4; e = p + 2 no longer identified with the classical identity (idea 11).
12. Prior-work paragraph added for the tail-law methodology and the all-level dictionary experiment.
13. T3 pre-registration: criterion was committed first, but the checkpoint summary contained a premature outcome
    line — disclosed (§2); `kfit.py` docstring corrected.
14. T1 endpoint bug fixed (results unchanged, JSON byte-identical); "exact rational" → floating-point.
15. "Record-setters" → "largest attained values"; "stationary" → "approximately stable"; fit-parameter counts.
16. Torus / supersingular statement restricted to d ≡ 3 (4) with the non-split torus named; "exactly equidistributed"
    → up to O(1).

Reviewer's independent confirmations: all 34 survival thresholds for p ≤ 10⁷ (82 887 primes) by a separate
prime-by-prime search, matching the corresponding sums in the 10⁹ and 10¹⁰ files; direct minimum searches at
1 775 179 561 (5777), 278 893 729 (3657), 7 183 201 (1133), 2 431 459 801 (4460), 6 106 475 761 (II-only 35 967),
3 280 856 329 (I-only 22 628); both decomposition identities; all T1 R² values and the T1 check; the `kfit` numbers;
the T3 counts. Not independently re-run: the full 56 876 600-prime range. The fixes above were applied after the
review; the cross-model review (§7) then audited that version.

## 7. Cross-model review (record)
`data/z69/xreview/REVIEW_IDEAA.md` (Astra; branch `side-agent/z69-xrev-ideaa`), on commit `5f4c3cc68`:
**ACCEPT-WITH-FIXES** — "accept the numerical results and scoped null outcome, not a blanket closure of the 21
directions". All four required fixes are applied in this version (not re-reviewed):
1. **Idea 10 (TYPE-I-FIXED):** the claim that algebraic factorisations of 4dm² + 1 need d square was false
   (d = 4m²k² − 2k; fixture p = 1033, (1, 45, 2, 132, 23), re-checked by hand: 4·45·132 = 23 760 = 1033·23 + 1,
   1 + 45 = 23·2). Only the square-d sterility is kept as PROVED. **Idea 12 (SUBSET-COVER):** the unsupported
   threshold ω ≳ log₂(4u) and the "general position" appeal are withdrawn; only the forced-factor budget remains.
2. **Scope:** the opening "every arithmetic re-encoding collapses" and the blanket "dead" language are narrowed to
   "no mechanism found"; Lemma T's reading is restricted to the total-norm / sign argument (proper-divisor forcing not
   excluded); ideas 8 (LYNESS), 11 (e = p + 2: empirically empty to 10⁶, unproved), 13, 19 and the structured
   variants are recorded as unproved, not ruled out; GAUSS-SPLIT is "not a universal rule", not killed as a selector.
3. **Prior-art scope:** `STRONG_APPROX_ES` Thm 9.1 described as a statement about finite n-local Eisenstein
   combinations; MONOID-DESCENT now cites `z52b_translate` #265 / Z2847 (the z61 board memo is outside the repository);
   "already proposed" is distinguished from "proved impossible" (ideas 5, 14, 17, 19); the "polylog count" assertion
   of idea 19 is deleted.
4. **Kept / made explicit:** the one-engine limitation of the 10¹⁰ census (independent duplication now to 10⁸ by the
   cross-reviewer, not beyond); the T3 kill is a point-estimate statement (interval [1.364, 1.549] quoted); O₄ / E₄
   notation in the falsifier table (only the 14 (★)-zeros and the 285 composites constrain O₄ = −E₄; the other 24
   𝔊*-zeros do not).

Cross-reviewer's independent confirmations (quoted from the review): Lemma T(i)–(iii) and the m = 8, m = 10
counterexamples; both decomposition identities; the census to 10⁸ and the six extreme minima; the `kfit` replay
(byte-identical JSON); the dependence ratios 0.888874, 2.19410, 8.71944, 11.1047, 52.8108, 148.547, 660.174; both T1
replays; the Gaussian lemma and the entire T3 sample by actual divisor/cofactor tests; ALG-SLICE (e = p − 2) and
QR-FLOOR; the TRACE counterexample; 8/131 and 8/241 have no three-term representation. No new computation was
required for the null verdict. **No provider / auth / quota error occurred in either review.**
