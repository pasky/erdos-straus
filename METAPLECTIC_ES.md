# METAPLECTIC_ES — theta multipliers, Kronecker theta quotients and half-integral weight objects on the ES side (O269)

Status: working file (spark relay on O267 SHARP 1). **ES is not solved here or anywhere; no infinite case of ES is
claimed.** Labels as in DISCOVERIES.md. Scripts `scripts/z39_*`; memos `BRAINSTORM/z39_*.md`.

Notation (QUESTION_R, DEDEKIND_ES). A length-3 word of n is w = (t, u, v) ∈ ℤ³_{≥2} with tuv − u − v = n;
A = tu − 1, A* = tv − 1, AA* = tn + 1 =: N_t; γ_w = [[A, n],[t, A*]] ∈ SL₂(ℤ) (QUESTION_R Prop 1.1).
R_t(n) = #{words of level t}, R(n) = Σ_t R_t(n); N₋(n) = #{w : (A/n) = −1} (five-slice count, DEDEKIND Thm 4.5).
D^±_t(N) = #{d ≥ 1 : d | N, d ≡ ±1 (mod t)}. q = e(τ).

Prior campaign work that this file must not repeat: `bsB_theta_multiplier` (O175: the ES sign is the weight-½ theta
multiplier of the certificate matrix; Shimura zero-propagation refuted), `bsB_salie_duality` (Type II with p as
Kloosterman modulus, Salié; non-invariance = B2), SIGN_IDENTITY / (J)39 (no finite sum of holomorphic modular forms
has N₋ as coefficients — growth y⁻¹log²), QUESTION_R Thm 1.5 (RS's σ is the theta multiplier on the positive cone),
red team 2 Thm 2.2 (B2).

## 0. Iteration log
* cp0: merged side-agent/question-r (O267; README conflict resolved keeping R276-corrected z36 rows). Read QUESTION_R,
  red team 2 §2, (J)39, bsB_theta_multiplier, bsB_salie_duality.
* cp2 (R280 hostile review, no FATAL): all "(R280 repair)" items applied — (K1′) clean form and β_t closed form
  (D1), novelty framing (D2), Cor K1.1 restated as the classical D⁻ = 0 with a direct proof (D3), Cor K1 reading
  caveated as a non-modular renormalisation (D4), exact per-n t = 2 correction at 10⁶ (D5), Prop S(3) unconditional
  (D6), holomorphic scope (D7), §3 precise lemma (D8), §5 hatch screen incl. H-E (D9), Borisov–Gunnells title (D10),
  citation pointers marked unchecked (D11).
* cp1 (parent note, R278 on O267): QUESTION_R Thm 1.5 is sound but **classical/RS §7.3** (cite as such, not new);
  QUESTION_R Cor 1.3's t ≡ 3 (mod 4) half is FALSE (only the 4 | t half and the mod-8 dependence hold) — not used
  here; Hypothesis TG false as quantified — not used.
* Construction log (barrier as steering wheel):
  - C1 "generating function of R is metaplectic?" → (J)39 kills finite holomorphic sums by growth; so look for
    infinitely many levels / non-holomorphic pieces → Thm K: each level = Kronecker theta quotient at a t-torsion
    point (weight 1) + weight-0 Maass Eisenstein; the infinite level sum is the B2 coordinate.
  - C2 "Sturm/Duke: Eisenstein main term + cusp bound" → Thm K: no cusp forms at any level; the main term is the
    weight-0 part, the holomorphic part is the oscillating one and carries T1 (Cor K1) → template inapplicable.
  - C3 "support = ES set at holomorphic weight ½" → Serre–Stark (Prop S): impossible; the square part of the failure
    set is θ's support; the failure set including 105 is not an exact holomorphic weight-½ support (unconditional).
  - C4 "self-levelled set = kernel of a multiplier / Hecke image of θ" → the self-level condition is a Bruhat-cell
    condition (Γ_∞-bi-invariant); the multiplier is ±1 on the I cell, ≡ −i on the −I cell (§3). Not a semigroup
    (0 of the 4096 products γ_{w1}γ_{w2}, t, u, v ∈ [2, 5], is self-levelled), so not a kernel.
  - C5 "quartic multiplier for numerator 8" → u↔v symmetry forbids χ₄(A) itself as a symmetric sign; ordered bit
    balanced (§6); other quartic invariants not excluded.
  - C6 "levels with one odd character (t = 3, 4, 6)" (here r_K(N) means σ_χ(N), not the representation number wσ_χ;
    R280 remark): D⁻ − D⁺ = −σ_χ(N) ≤ 0 always (theta-series positivity pushes
    *against* ES); ES at these levels ⟺ τ(N) − r_K(N) > 2β — the classical Mordell families. No new forcing.

## 1. Each level is a Kronecker theta quotient at a torsion point (Theorem K)

**Theorem K (PROVED; classical input = Kronecker's double-series identity).** Fix t ≥ 2. Put X = q^{t−1}, Q = q^t,
θ(x) = (x; Q)_∞(Q/x; Q)_∞, and
* P_t(q) := Σ_{u,v ≥ 2} q^{tuv−u−v} = Σ_n R_t(n) q^n (ES words of level t),
* Q_t(q) := Σ_{r,s ≥ 0} q^{trs+r+s} (the "partner quadrant").
Then
`P_t − Q_t = q^{t−2}·[ (Q;Q)²_∞ θ(X²)/θ(X)² − (1+X)/(1−X) ]`,                                   (K1)
and coefficientwise, with N = tn + 1,
`R_t(n) = D⁻_t(N) − β_t(n)`,  `[q^n]Q_t = D⁺_t(N)`,  β_t(n) = #{d | N : d ≡ −1 (t), min(d, N/d) = t − 1}.   (K2)
Consequently R_t(n) = ½·E_t(N) + ½·O_t(N) − β_t(n) with
`E_t(N) = D⁻ + D⁺ − 2 = (2/φ(t)) Σ_{χ even} σ_χ(N) − 2`,  `O_t(N) = D⁻ − D⁺ + 2 = −(2/φ(t)) Σ_{χ odd} σ_χ(N) + 2`,
σ_χ(N) = Σ_{d|N} χ(d), χ over Dirichlet characters mod t (the "−2/+2" removes the trivial divisors 1, N ≡ 1 (t);
it is an elementary correction present in **every** coefficient, not a modular piece; for t = 2 the classes ±1
coincide, there are no odd characters, D⁻ = D⁺ = τ(N), O₂ ≡ 2).
*Proof.* Kronecker (Weil, *Elliptic functions according to Eisenstein and Kronecker*, Ch. VIII; Zagier, Invent. Math.
104 (1991) §3 — pointers not re-checked (R280 D11); the identity was verified numerically, also for x ≠ y by R280): for |Q| < |x|, |y| < 1, Σ_{r,s≥0} x^r y^s Q^{rs} − Σ_{r,s≥1} x^{−r}y^{−s}Q^{rs} = (Q;Q)²θ(xy)/(θ(x)θ(y)).
Take x = y = X: |Q| < |X| < 1 for |q| < 1. Substituting u = r + 1, v = s + 1 (r, s ≥ 1) gives
q^{t−2}X^{r+s}Q^{rs} = q^{tuv−u−v}; substituting r = ρ + 1, s = σ + 1 in the negative quadrant gives
q^{t−2}X^{−r−s}Q^{rs} = q^{tρσ+ρ+σ}; the r = 0 or s = 0 terms of the positive quadrant sum to 2/(1−X) − 1 = (1+X)/(1−X).
(K2): (tu−1)(tv−1) = N and (tρ+1)(tσ+1) = N; u ≥ 2 ⟺ d = tu − 1 > t − 1. The character formulas are orthogonality
(1[d ≡ ±1] = φ(t)⁻¹Σ_χ χ̄(±1)χ(d)). ∎
Checks (`scripts/z39_kronecker.py`): (K1) numerically at q = 0.3 + 0.2i, t = 2..6 (|error| ≤ 10⁻¹³); (K2) for all
t ≤ 30, n ≤ 1500: 0 failures.

**(K1′) Clean form (R280 repair, D1).** The boundary series q^{t−2}(1+X)/(1−X) has coefficients exactly β_t(n), and
β_t(n) = 2·1[(t − 1) | (n + 1)] − 1[n = t − 2] (closed form, R280). Hence
`q^{t−2}(Q;Q)²θ(X²)/θ(X)² = Σ_{n≥0} (D⁻_t − D⁺_t)(tn+1) qⁿ = −(2/φ(t)) Σ_{n≥0} Σ_{χ odd} σ_χ(tn+1) qⁿ`
— the theta quotient alone is **exactly** the odd-character divisor sum on N ≡ 1 (mod t), with no ±2 and no
boundary term. The ±2 in E_t, O_t above is only bookkeeping (removal of the trivial divisors 1, N from both parts).

**Reading (modular status of each piece; Assessment — R-self-review repair: the identity (K1)–(K2) is what is
PROVED; the modular identifications below need normalisations that are not carried out here).**
* (Q;Q)²θ(X²)/θ(X)² is, up to the Jacobi exponential normalisation, Kronecker's function F_{τ'}(z, z) =
  θ'(0)θ(2z)/θ(z)² (a meromorphic Jacobi form of weight 1, index 1) at τ' = tτ, z = ((t−1)/t)τ' — a **t-torsion
  point**. As a raw q-series it is *not* itself holomorphic modular (for t > 2 it has the leading term −q^{2−t},
  coming from θ(X²) ∋ (1 − Q/X²)); torsion specialisations become modular only after the elementary factor
  e(·)q^{(·)} of the Jacobi normalisation (Hecke; Borisov–Gunnells, Invent. Math. 144 (2001), "toric modular
  forms" [title corrected per R280 D10: *Toric varieties and modular forms*, Invent. Math. 144 (2001) 297–325, which
  attaches weight-r forms on Γ₁(l) to rank-r fans]). The arithmetic content that *is* proved (K1′): D⁻_t − D⁺_t =
  −(2/φ(t))Σ_{χ odd}σ_χ(N), restricted to the progression N = tn + 1 ≡ 1 (mod t); for each odd χ, Σ_N σ_χ(N)q^N is a
  weight-1 holomorphic Eisenstein series in M₁(Γ₀(t), χ) (Diamond–Shurman Thm 4.8.1, constant term aside), and the
  progression restriction N ≡ 1 (t) with reindexing n = (N − 1)/t preserves modularity up to level/shift (twisting by
  additive characters mod t, then q^{1/t}-rescaling).
* The even part Σ_N σ_χ(N)q^N, χ even, is **not** holomorphic modular: it is the Fourier-coefficient sequence of the
  weight-0 (Maass) Eisenstein series E_χ(z, s) at the centre s = ½ (principal χ: the s-derivative, coefficients
  τ(N)·K₀ — the source of a log).
* So (Assessment, modulo the normalisations above) the level-t ES count is **half an odd-character divisor sum
  (weight-1 holomorphic Eisenstein data, packaged by a Kronecker theta quotient at a torsion point) plus half an
  even-character divisor sum (weight-0 Maass Eisenstein data)**, both on the progression N = tn + 1, minus the
  boundary β_t (words with u = 1 or v = 1): R_t = ½(D⁻ + D⁺) + ½(D⁻ − D⁺) − β_t. No cusp form appears at any level
  (PROVED in the form: every term is a Dirichlet-character divisor sum).

**Corollary K1 (T1 in even/odd language; sizes; PROVED for item 1, EVIDENCE for sizes, Assessment with caveat for the
reading).** **Convention:** all level sums run over 2 ≤ t ≤ (n + 4)/4 (R_t(n) = 0 beyond, but E_t, O_t, β_t individually
are not). Write R(n) = 𝔈(n) + 𝔒(n) − 𝔅(n) with 𝔈 = ½Σ_t E_t(tn+1), 𝔒 = ½Σ_t O_t(tn+1) (E_t, O_t with the trivial divisors
1, N removed, as defined above), 𝔅 = Σ_t β_t(n) = 2·#{e | n + 1 : 1 ≤ e ≤ ⌊(n + 4)/4⌋ − 1} (≈ 2τ(n+1)).
1. *(T1 at 4 | t; classical; PROVED. R280 repair, D3.)* For 4 | t and **every** m: D⁻_t(tm² + 1) = 0. Direct proof: if
   d > 0, d | tm² + 1, d ≡ −1 (t), then gcd(d, tm) = 1 and −t ≡ (m⁻¹)² (mod d), so (−t/d) = 1; but d ≡ 3 (4) gives
   (−1/d) = −1, and for t = 4s one checks (s/d) = 1 (s odd: (s/d) = (d/s)(−1)^{(s−1)/2·(d−1)/2} = (−1/s)(−1)^{(s−1)/2} = 1;
   2 | s: d ≡ −1 (8), (2/d) = 1, same on the odd part), so (−t/d) = −1, contradiction. Hence R_t(m²) = β_t(m²) = 0
   (t − 1 ≡ 3 (4) cannot divide m² + 1). Since E_t + O_t = 2D⁻_t identically, in the even/odd language this **reads**
   E_t(tm² + 1) + O_t(tm² + 1) = 0 — a relabelling of the classical (A)3/Mordell obstruction, not new information.
   (R280 check: 4 | t ≤ 64, m ≤ 800: 0 exceptions.)
2. *(Sizes; EVIDENCE, `scripts/z39_split.py`. Self-review repair: the first runs mis-counted t = 2 (an `elif` dropped
   every divisor from D⁺₂); the bias is exactly τ(2n+1)/2 per n. The 10⁵ and near-square numbers are re-runs; the 10⁶
   numbers are corrected exactly per n (R280 repair, D5).)* 12 primes just above 10⁵: 𝔈 = 115.9 (97–134), 𝔒 = +3.75
   (sd ≈ 20), 𝔅 = 52.7, R = 67.0 (reproduced exactly by R280). Odd squares 317²–323²: 𝔈 = 127, 124, 109, 139,
   𝔒 = −29, −50, −83, −81, with 𝔒_{4|t} = −𝔈_{4|t} (item 1) and the bulk of the deficit at t ≡ 3 (4) (𝔒_{t≡3} = −24,
   −47, −55, −43, R280). 12 primes just above 10⁶ (exact per-n correction): 𝔈 = 162.7 (139–201), 𝔒 = −0.5 (sd ≈ 40),
   R = 113; 𝔈 ≈ 163 vs 115.9·(log 10⁶/log 10⁵)² ≈ 167. Odd squares 1001²–1007²: 𝔒 = −103, −37, −23, −72, N₋ = 0 (T1
   control). Near-square primes m² + K, m > 300, 10 each (`scripts/z39_nearsq.py 300 10 4 24 -3`): 𝔈 = 113, 121, 140,
   𝔒 = −4.5, −15.3, −31.7 (SE ≈ 6–7) for K = 4, 24, −3 — 𝔒 is not a T1 detector by itself (K = −3 has no N₋ deficit).
3. *Reading (Assessment, with caveat — R280 repair, D4).* The genuinely modular per-level pieces are ½(D⁻ + D⁺) and
   ½(D⁻ − D⁺) (the latter exactly the Kronecker quotient, (K1′)); summed over the ≈ n/4 levels they are ≈ +n/4 and
   ≈ −n/4 (trivial divisors 1, N at every level). 𝔈 and 𝔒 arise only **after removing the trivial divisors at every
   level — an elementary, non-modular renormalisation of total size ≍ n, forced by the truncation t ≤ (n + 4)/4**.
   After it, "𝔈 carries the log², 𝔒 averages ≈ 0" just says that the non-trivial divisors of tn + 1 are on average
   equidistributed between the classes ±1 (mod t) — elementary equidistribution, not an automorphic fact. So the
   statement "main term in weight 0, oscillation in weight 1" is a bookkeeping reading, not a structural theorem.
   What remains true: at each level there is no cusp form, so a "main Eisenstein term + cusp-form bound" (Sturm/Duke)
   argument has nothing to bound; the competition is between divisor sums at the single integer tn + 1 (B2).

## 2. Which half-integral weight objects can see the ES failure set (Prop S)

Full memo: `BRAINSTORM/z39_serre_stark_support.md`.
**Prop S (PROVED from Serre–Stark, LNM 627 (1977)).** Every holomorphic weight-½ form on Γ₁(4N) is a finite combination
of θ_{ψ,t} = Σ_m ψ(m)q^{tm²}; its support lies in finitely many square classes t·□, and on each class n = t₀m² the
coefficient is a periodic function of m. Therefore:
1. no weight-½ holomorphic form has support of positive density (the ES-five success set, or any ES success set);
2. the T1 part of the five-slice failure set **is** metaplectic: {m² : m odd} = supp(θ(z) − θ(4z));
3. *(R280 repair, D6: now PROVED unconditionally.)* Let Z = {n ≡ 1 (4) : λ(n) > 3} be DEDEKIND's five-slice failure
   set (boundary certificates included; R280 census: Z \ □ = {105} for n ≤ 10⁸; the interior-only zero set
   {N₋ = 0} \ □ = {5, 105}). **Z is not the exact support of any holomorphic weight-½ form.** Proof (R280): suppose
   supp g = Z (over all n). Then m ↦ a_g(105m²) is periodic, period M, and non-zero at m = 1. If M is odd, 105(1 + M)²
   is even, not in Z. If M is even, take a prime ℓ ≡ 3 (4) with (ℓ/105) = −1 and ℓ ∤ M (ℓ = 11, 19, 31, 43, …;
   infinitely many by Dirichlet). Then (−105/ℓ) = (−1/ℓ)(ℓ/105) = +1, so 105m² ≡ −1 (ℓ) is solvable (m ≡ ±r_ℓ; r₁₁ = 3).
   By CRT choose m ≡ 1 (M), m ≡ r_ℓ (ℓ); m is odd, a_g(105m²) ≠ 0, but n = 105m² has ℓ | n + 1 and
   (ℓ/n) = (ℓ/105)(ℓ/m)² = −1, so n/ℓ is an HJ length-2 certificate, λ(n) ≤ 2, n ∉ Z: contradiction. No census, no
   SQ₅. (Same for Z ∪ F, F finite, 105 ∈ Z ∪ F.) Checked by R280 (`scripts/review_r280_propS_uncond.py`). Note this
   shows the obstruction is elementary — Z misses whole residue classes of m on 105·□ — and it is an exact-support
   statement only: θ_{1,105} = Σ q^{105m²} has 105 in its support.
So the answer to the brief's literal question ("an ES-side half-integral weight object whose support is the ES set and
whose vanishing at squares IS T1") is (R280 repair, D7: holomorphic scope throughout): **no ES success set is the
support of a holomorphic weight-½ form; the square part of the failure set is exactly supp θ (θ(z) − θ(4z)); Z is not
the exact support of any holomorphic weight-½ form (unconditional).** Weight-½ mock theta functions, weakly
holomorphic forms and harmonic Maass forms have positive-density supports and are not covered. At weight ≥ 3/2
supports are not restricted by this argument but coefficients have power size (B3); (J)39 Thm 2.2 already excludes N₋
as coefficients of finite holomorphic sums. (Zagier's ℋ is mock, holomorphic modular only after completion, and is
not used here.)

## 3. The multiplier on the cells ±Γ₁(c) (dictionary)

Full memo: `BRAINSTORM/z39_positive_coset.md`. In the normalisation γ_w = [[A, n],[t, A*]] the self-level condition
γ ∈ −Γ₁(t) is invariant under Γ_∞ × Γ_∞ (Γ_∞ = ⟨T⟩, without −I), so level-t ES words are the elements with b = n and
a, d ≥ 2t − 1 (not merely positive: [[3,5],[4,7]] is positive and self-levelled but is (4, 1, 2)) of the single
Bruhat cell Γ_∞[[−1, ∗],[t, −1]]Γ_∞ (one term of each Kloosterman sum mod t). Thm K's partner Q_t is the +I cell,
always non-empty ([[1,0],[t,1]][[1,n],[0,1]]); the −I analogue is not positive. Thm K's odd (weight-1) part is the
signed count over the two cells (parity of −I in odd weight): by (K1′), D⁻ − D⁺ is exactly the signed count of the
cell elements with a, d ≥ 1. The theta multiplier refines this parity: on positive
self-levelled elements of −Γ₁(4), ν_θ = ε_d⁻¹(c/d) ≡ −i (QUESTION_R Prop 1.4; classical/RS input), on positive
elements of Γ₁(4) with b odd ν_θ = (a/b) ∈ {±1} (RS Lemma 3.1). *Precise lemma (R280 repair, D8; verified by R280 on
20 000 random matrices):* for positive γ ∈ Γ₀(4) with b odd and d ≡ 3 (4), (c/d) = −(−1/b)(a/b); if b = m² this is −1,
whereas self-levelling with 4 | c forces (c/d) = +1 — this is T1 at 4 | t. The self-levelled set is not a semigroup
(0/4096 products, R280: also 0/117 649 for letters ≤ 8), so it is not (kernel ∩ positive cone) of a multiplier.
(PROVED dictionary; no mechanism.)

## 4. The sum over levels: a shifted ternary-divisor (GL(3)-Eisenstein-type) object

Summing Thm K over t first in the other order: Σ_n R(n)q^n = Σ_{t,u,v≥2} q^{tuv−u−v} = Σ_{u,v≥2} q^{2uv−u−v}/(1−q^{uv})
(PROVED, trivial). Analogy (Assessment): with t, u, v ≥ 2 the unshifted series Σ q^{tuv} has coefficients
d₃(n) − 3d₂(n) + 3 − 1[n = 1] (boundary removal), and the x = y = q⁻¹ specialisation of Σ_{t,u,v≥1} x^u y^v q^{tuv}
diverges (t = u = 1), so the link to Σ d₃(n)q^n (minimal-parabolic SL₃(ℤ) Eisenstein coefficients) is only up to
boundary terms. So (Assessment): the level-wise
objects are GL(2) Eisenstein (weight 0 and 1), and the full count is an additively shifted d₃ — matching (J)39's
"d₃-size" (Σ_{n≤X}N₋ ~ (15/64)X log²X vs Σ d₃ ~ ½X log²X) and its steering ("divisor rank ≥ 3, unboundedly many
levels"). Two equivalent descriptions of the log²: (level side) τ(tn+1) from the weight-0 s-derivative × Σ_t 1/φ(t);
(GL(3) side) the triple pole of ζ³. Neither description has a holomorphic/half-integral weight component carrying
the main term. (R280 remark: the GL(3) object here is Eisenstein — d₃ = 1∗1∗1, abelian — so it does not touch H-D's
"GL₃ or higher automorphic forms"; (J)39's open GL(3) *cuspidal* contributions are not addressed.)

## 5. Red team 2 Thm 2.2 and the escape hatches (R280 repair, D9: rewritten as a hatch screen)

Thm 2.2(iii) has essentially one hypothesis (Θ₀ finite; H for the conclusion). For a fixed finite set of levels the
witness is a divisor ≡ −1 (t) of the fixed linear polynomials tp + 1, so Thm 2.2(iii) applies (CONDITIONAL on H): a
finite-level metaplectic construction is killed; Thm K sharpens Thm 2.2(ii) for these slices (every term is a
character divisor sum; not even CM cusp forms occur). The meaningful screen is against the hatches of red team 2 §3:
* **H-A (growing family, all levels t ≤ (n + 4)/4): touched.** Needs polylog-accurate control of Σ_t (divisor-sum
  coefficient at tn + 1) at one n, over different groups Γ₁(t) and torsion points, with no modular structure in t
  (§4) — the regime red team 2 assessed as quantitatively blocked (𝓛³ mass, Planck-scale targets).
* **H-E (exact identity with a positive main term): formally touched, not opened.** Thm K / Cor K1 give an exact signed
  expansion R = 𝔈 + 𝔒 − 𝔅 with 𝔈 > 0. Using it needs |𝔒 − 𝔅| < 𝔈 at a single prime, i.e. a pointwise bound on ≍ n/4
  weight-1 Eisenstein coefficients at different levels and points; the per-level modular pieces are of size ≍ n before
  the non-modular renormalisation (Cor K1.3), so the "cancellation" is termwise elementary and the remaining sum is the
  H-A/B2 object again.
* **H-D (non-abelian data with non-zero coefficient): not opened by the constructions examined.** The ES sign (A/n)
  is a character mod 4t of A (QUESTION_R Prop 1.2); where a genuine theta multiplier is defined (§3) it takes
  congruence values (−i on the self-levelled −I cell); the metaplectic cover is non-split, but on the positive cone it
  is a semigroup character with congruence values (RS §7.3 / Kubota). Other metaplectic constructions are not excluded.
* H-B, H-C, H-F, H-G: not engaged.
Summary (Assessment): the metaplectic constructions examined touch only H-A (and, formally, H-E).

## 6. Quartic (numerator 8/16) — negative

`BRAINSTORM/z39_quartic_slices.md`: for p ≡ 1 (4) and any word, χ₄(A*) = χ₄(A)⁻¹ (AA* ≡ 1 mod p), so χ₄(A) itself is
not a u↔v-symmetric sign on the k | t non-residue slices (PROVED; other quartic invariants are not excluded); the ordered smaller-divisor bit is balanced (EVIDENCE, p < 2·10⁴,
k = 4, 8, 16). The k = 8 exceptions 131 (inert in ℤ[i]), 17, 241 show no quartic signature; consistent with
QUESTION_R §4.1 (4 and 8 share the quadratic invariant; the difference is B3).

## 7. Verdict (Assessment) and exact scope

1. **Identity (PROVED; classical, new only as a packaging in the campaign — R280 D2):** the level-t ES series minus
   its partner quadrant is Kronecker's theta quotient θ'(0)θ(2z)/θ(z)² at the t-torsion point z = (t−1)τ'/t,
   τ' = tτ, plus the boundary series; the theta quotient alone has coefficients exactly (D⁻_t − D⁺_t)(tn + 1), the
   odd-character divisor sum (K1′); the coefficient content (divisors ≡ −1 mod t of tn + 1) is the long-standing
   campaign reformulation. Modular reading (weight-1 Eisenstein after Jacobi normalisation; even part = weight-0
   Maass data): Assessment. Every term is a Dirichlet-character divisor sum: no cusp form.
2. **Where things live (Assessment with caveat, Cor K1.3):** after the non-modular removal of trivial divisors, the
   log² sits in the even part and the odd part averages ≈ 0 — elementary equidistribution of non-trivial divisors
   between ±1 mod t. T1 at 4 | t is D⁻_t(tm² + 1) = 0 (classical), which in even/odd language reads E_t + O_t = 0.
   The full level sum is a boundary-truncated, additively shifted relative of d₃ (GL(3) Eisenstein analogy, §4).
3. **Half-integral weight (PROVED, holomorphic scope):** by Serre–Stark only periodic square classes can be supports
   of holomorphic weight-½ forms: T1's squares are θ's support; the five-slice failure set Z (containing 105) is not
   the exact support of any holomorphic weight-½ form — unconditionally (R280 D6). Mock / weakly holomorphic /
   harmonic weight-½ objects are not covered. The theta multiplier on positive self-levelled elements of −Γ₁(4) is
   the constant −i (§3).
4. **Barriers:** the examined metaplectic constructions touch only hatch H-A (and formally H-E, not opened); they do
   not open H-D; the sum over levels has no modular structure in t (B2).
No existence mechanism, no pointwise statement, ES not touched.
