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
* cp1 (parent note, R278 on O267): QUESTION_R Thm 1.5 is sound but **classical/RS §7.3** (cite as such, not new);
  QUESTION_R Cor 1.3's t ≡ 3 (mod 4) half is FALSE (only the 4 | t half and the mod-8 dependence hold) — not used
  here; Hypothesis TG false as quantified — not used.
* Construction log (barrier as steering wheel):
  - C1 "generating function of R is metaplectic?" → (J)39 kills finite holomorphic sums by growth; so look for
    infinitely many levels / non-holomorphic pieces → Thm K: each level = Kronecker theta quotient at a t-torsion
    point (weight 1) + weight-0 Maass Eisenstein; the infinite level sum is the B2 coordinate.
  - C2 "Sturm/Duke: Eisenstein main term + cusp bound" → Thm K: no cusp forms at any level; the main term is the
    weight-0 part, the holomorphic part is the oscillating one and carries T1 (Cor K1) → template inapplicable.
  - C3 "support = ES set at weight ½" → Serre–Stark (Prop S): impossible; the square part of the failure set is θ's
    support; the failure set including 105 is not an exact weight-½ support.
  - C4 "self-levelled set = kernel of a multiplier / Hecke image of θ" → the self-level condition is a Bruhat-cell
    condition (Γ_∞-bi-invariant); the multiplier is ±1 on the I cell, ≡ −i on the −I cell (§3). Not a semigroup
    (0 of the 4096 products γ_{w1}γ_{w2}, t, u, v ∈ [2, 5], is self-levelled), so not a kernel.
  - C5 "quartic multiplier for numerator 8" → u↔v symmetry forbids χ₄(A) itself as a symmetric sign; ordered bit
    balanced (§6); other quartic invariants not excluded.
  - C6 "levels with one odd character (t = 3, 4, 6)": D⁻ − D⁺ = −σ_χ(N) ≤ 0 always (theta-series positivity pushes
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
104 (1991) §3): for |Q| < |x|, |y| < 1, Σ_{r,s≥0} x^r y^s Q^{rs} − Σ_{r,s≥1} x^{−r}y^{−s}Q^{rs} = (Q;Q)²θ(xy)/(θ(x)θ(y)).
Take x = y = X: |Q| < |X| < 1 for |q| < 1. Substituting u = r + 1, v = s + 1 (r, s ≥ 1) gives
q^{t−2}X^{r+s}Q^{rs} = q^{tuv−u−v}; substituting r = ρ + 1, s = σ + 1 in the negative quadrant gives
q^{t−2}X^{−r−s}Q^{rs} = q^{tρσ+ρ+σ}; the r = 0 or s = 0 terms of the positive quadrant sum to 2/(1−X) − 1 = (1+X)/(1−X).
(K2): (tu−1)(tv−1) = N and (tρ+1)(tσ+1) = N; u ≥ 2 ⟺ d = tu − 1 > t − 1. The character formulas are orthogonality
(1[d ≡ ±1] = φ(t)⁻¹Σ_χ χ̄(±1)χ(d)). ∎
Checks (`scripts/z39_kronecker.py`): (K1) numerically at q = 0.3 + 0.2i, t = 2..6 (|error| ≤ 10⁻¹³); (K2) for all
t ≤ 30, n ≤ 1500: 0 failures.

**Reading (modular status of each piece; Assessment — R-self-review repair: the identity (K1)–(K2) is what is
PROVED; the modular identifications below need normalisations that are not carried out here).**
* (Q;Q)²θ(X²)/θ(X)² is, up to the Jacobi exponential normalisation, Kronecker's function F_{τ'}(z, z) =
  θ'(0)θ(2z)/θ(z)² (a meromorphic Jacobi form of weight 1, index 1) at τ' = tτ, z = ((t−1)/t)τ' — a **t-torsion
  point**. As a raw q-series it is *not* itself holomorphic modular (for t > 2 it has the leading term −q^{2−t},
  coming from θ(X²) ∋ (1 − Q/X²)); torsion specialisations become modular only after the elementary factor
  e(·)q^{(·)} of the Jacobi normalisation (Hecke; Borisov–Gunnells, Invent. Math. 144 (2001), "toric modular
  forms"). The arithmetic content that *is* proved: the odd part of the coefficient sequence, O_t(N) − 2 =
  −(2/φ(t))Σ_{χ odd}σ_χ(N), restricted to the progression N = tn + 1 ≡ 1 (mod t); for each odd χ, Σ_N σ_χ(N)q^N is a
  weight-1 holomorphic Eisenstein series in M₁(Γ₀(t), χ) (Diamond–Shurman Thm 4.8.1, constant term aside), and the
  progression restriction N ≡ 1 (t) with reindexing n = (N − 1)/t preserves modularity up to level/shift (twisting by
  additive characters mod t, then q^{1/t}-rescaling).
* The even part Σ_N σ_χ(N)q^N, χ even, is **not** holomorphic modular: it is the Fourier-coefficient sequence of the
  weight-0 (Maass) Eisenstein series E_χ(z, s) at the centre s = ½ (principal χ: the s-derivative, coefficients
  τ(N)·K₀ — the source of a log).
* So (Assessment, modulo the normalisations above) the level-t ES count is **half an odd-character divisor sum
  (weight-1 holomorphic Eisenstein data, packaged by a Kronecker theta quotient at a torsion point) plus half an
  even-character divisor sum (weight-0 Maass Eisenstein data)**, both on the progression N = tn + 1, plus the
  elementary ±2 correction and the boundary β_t (words with u = 1 or v = 1). No cusp form appears at any level
  (PROVED in the form: every term is a Dirichlet-character divisor sum).

**Corollary K1 (where the main term and T1 live; PROVED for the exact statements, EVIDENCE for sizes).**
**Convention:** all level sums run over 2 ≤ t ≤ (n + 4)/4 (R_t(n) = 0 beyond, but E_t, O_t, β_t individually are
not; the omitted pieces cancel in R only). Write R(n) = 𝔈(n) + 𝔒(n) − 𝔅(n) with 𝔈 = ½Σ_t E_t(tn+1) (even-character /
weight-0 part), 𝔒 = ½Σ_t O_t(tn+1) (odd-character / weight-1 part, incl. the elementary +2 per level),
𝔅 = Σ_t β_t(n) ≈ 2τ(n+1) (words with u or v = 1).
1. *(T1 as an exact even/odd cancellation; PROVED.)* For odd m and every level t ≡ 0 (mod 4): R_t(m²) = 0 (all words
   with 4 | t lie in the (A)3 slice and have (A/n) = −1, DEDEKIND Thm 4.5 / QUESTION_R Prop 1.4 (4 | t half, not
   affected by R278 D5); (A/m²) = +1), and β_t(m²) = 0 (t − 1 ≡ 3 (mod 4) cannot divide m² + 1). Hence
   `E_t(tm² + 1) + O_t(tm² + 1) = 0`: at every level 4 | t the odd-character (weight-1) term equals **minus** the
   even-character (weight-0) term on the norm-form values 1 + tm² (both including the elementary ±2).
   (Equivalently: tm² + 1 has no divisor ≡ −1 (mod t) — the classical (A)3 obstruction.)
2. *(Sizes; EVIDENCE, `scripts/z39_split.py`, `/tmp` logs summarised here. Self-review repair: the first runs
   mis-counted level t = 2 (an `elif` dropped every divisor from D⁺₂, since +1 ≡ −1 mod 2), biasing 𝔈 down and 𝔒 up
   by τ(2n+1)/2 each — mean 3.42 at the 10⁵ primes, 3.92 at the 10⁶ primes (reviewer's computation); R, N₋ and 𝔅
   were unaffected. Scripts fixed; the 10⁵ and near-square numbers below are re-runs, the 10⁶ ones are corrected by
   the stated mean bias.)* At 12 primes just above 10⁵ (re-run): 𝔈 ≈ 115.9 (97–134), 𝔒 ≈ +3.75 (−26…+35, sd ≈ 20), 𝔅 ≈ 54, R ≈ 67. At the odd squares 317², 319², 321², 323²:
   (re-run) 𝔈 ≈ 125, 𝔒 = −29, −50, −83, −81, and the split by t mod 4 shows 𝔒_{4|t} = −𝔈_{4|t} exactly (item 1) and most of
   the rest of the deficit at t ≡ 3 (4) (R_t small but non-zero there — consistent with R278's correction that
   QUESTION_R Cor 1.3's t ≡ 3 half is false).
   At 12 primes just above 10⁶ (`scripts/z39_split.py 1000000 12`, ≈ 1 h; corrected by the t = 2 bias): 𝔈 ≈ 163,
   𝔒 ≈ −0.5 (sd ≈ 40), R ≈ 113 (115.9 × (6/5)² ≈ 167, consistent with log² scaling of 𝔈); odd squares 1001², 1003², 1005², 1007²: 𝔒 = −97, −35, −19,
   −68 before the (small, ≈ τ(2m²+1)/2) t = 2 correction, and N₋ = 0 (T1 control). The spread of 𝔒 grows faster than log² in this tiny sample (Assessment only).
   Near-square primes m² + K, m > 300, 10 primes each (`scripts/z39_nearsq.py 300 10 4 24 -3`, re-run after the
   fix): 𝔈 = 113, 121, 140 and 𝔒 = −4.5, −15.3, −31.7 (sd ≈ 20, so SE of a mean ≈ 6–7) for K = 4, 24, −3. So 𝔒 is **not** a T1 detector by
   itself: K = −3 (no N₋ deficit, QUESTION_R §3.2) has the most negative 𝔒 together with the largest 𝔈 — 𝔒 depends
   on the shape of n beyond T1. What is exact is item 1 (cancellation on 4 | t at squares).
   **Reading (Assessment).** The power-free "main term" log²n of the ES count is carried entirely by the weight-0
   non-holomorphic part 𝔈 (one log from the s-derivative of E(z, s) at s = ½, i.e. τ(N), one from Σ_t 1/φ(t) over
   levels); the holomorphic part 𝔒 averages to ≈ 0 at generic primes (but not on all polynomial families, e.g. m² − 3)
   and at squares it cancels the main term exactly, level by level on 4 | t. So "Eisenstein main term + bounded cusp error" (Sturm/Duke) is the wrong
   template: at each level there is no cusp form; the competition is weight-0 Eisenstein vs weight-1 Eisenstein,
   both evaluated at the single integer tn + 1 — the divisor-in-class event (B2) in automorphic clothing.

## 2. Which half-integral weight objects can see the ES failure set (Prop S)

Full memo: `BRAINSTORM/z39_serre_stark_support.md`.
**Prop S (PROVED from Serre–Stark, LNM 627 (1977)).** Every holomorphic weight-½ form on Γ₁(4N) is a finite combination
of θ_{ψ,t} = Σ_m ψ(m)q^{tm²}; its support lies in finitely many square classes t·□, and on each class n = t₀m² the
coefficient is a periodic function of m. Therefore:
1. no weight-½ holomorphic form has support of positive density (the ES-five success set, or any ES success set);
2. the T1 part of the five-slice failure set **is** metaplectic: {m² : m odd} = supp(θ(z) − θ(4z));
3. the non-square failure 105 is **not** metaplectic, in the exact-support sense. Let Z = {n ≡ 1 (4) : λ(n) > 3}
   be DEDEKIND's five-slice failure set (boundary certificates included; census to 10⁶, DEDEKIND §9.1: Z \ □ = {105}).
   (Self-review repair: the interior-only zero set {N₋ = 0} is different — its non-square zeros ≤ 10⁶ are 5 and 105.)
   Suppose supp g = Z exactly (support over all n) for a weight-½ form g. Then m ↦ a_g(105m²) is periodic (period M)
   and non-zero at m = 1. If M is odd, 105(1 + M)² is even, outside Z: contradiction. If M is even and M ≤ 96, then
   m = 1 + M ≤ 97 is odd and 105m² ≤ 105·97² = 987945 < 10⁶ is a non-square ≡ 1 (4) outside Z (census; the reviewer
   also confirmed interior hits for all odd 3 ≤ m ≤ 97): contradiction. Under SQ₅ (CONJECTURE) every M is excluded.
   This forbids Z as an exact support; it does not forbid a weight-½ form whose support merely contains 105.
So the answer to the brief's literal question ("an ES-side half-integral weight object whose support is the ES set and
whose vanishing at squares IS T1") is: **at weight ½, no success set can be a support; the square part of the failure
set is exactly supp θ; the failure set with 105 is not an exact support (periods ≤ 96; all under SQ₅).** At weight
≥ 3/2 supports are not restricted by this argument but coefficients have power size (B3); (J)39 Thm 2.2 already
excludes N₋ as coefficients of finite holomorphic sums. (Zagier's ℋ is mock, holomorphic modular only after
completion, and is not used here.)

## 3. The multiplier on the cells ±Γ₁(c) (dictionary)

Full memo: `BRAINSTORM/z39_positive_coset.md`. In the normalisation γ_w = [[A, n],[t, A*]] the self-level condition
γ ∈ −Γ₁(t) is invariant under Γ_∞ × Γ_∞ (Γ_∞ = ⟨T⟩, without −I), so level-t ES words are the elements with b = n and
a, d ≥ 2t − 1 (not merely positive: [[3,5],[4,7]] is positive and self-levelled but is (4, 1, 2)) of the single
Bruhat cell Γ_∞[[−1, ∗],[t, −1]]Γ_∞ (one term of each Kloosterman sum mod t). Thm K's partner Q_t is the +I cell,
always non-empty ([[1,0],[t,1]][[1,n],[0,1]]); the −I analogue is not positive. Thm K's odd (weight-1) part is the
signed count over the two cells (parity of −I in odd weight), up to the elementary ±2 and boundary corrections. The theta multiplier refines this parity: on positive
self-levelled elements of −Γ₁(4), ν_θ = ε_d⁻¹(c/d) ≡ −i (QUESTION_R Prop 1.4; classical/RS input), on positive
elements of Γ₁(4) ν_θ = (a/b) ∈ {±1} (RS Lemma 3.1). T1 = imaginary multiplier on the −I cell is incompatible with
b = □. (PROVED dictionary; no mechanism.)

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
the main term.

## 5. Red team 2 Thm 2.2: which hypothesis a metaplectic construction violates

* Thm 2.2(iii) needs a **fixed finite** parameter set Θ₀. A single level t (or finitely many) is a finite union of
  slices; Thm K shows the automorphic content of a level is pure Eisenstein (weight-0 Maass + weight-1 Kronecker
  quotient), i.e. the "congruence/genus data only" of Thm 2.2(ii) in sharper form (not even CM cusp forms occur).
  So a finite-level metaplectic construction satisfies every hypothesis and is killed (CONDITIONAL on H).
* Using **all** levels t ≤ (n + 4)/4 violates the finiteness hypothesis (hatch H-A). But the per-level content is
  still abelian: the ES sign (A/n) is a character mod 4t of A (QUESTION_R Prop 1.2); where a genuine theta multiplier
  is defined (Γ₀(4)-type matrices, §3) it takes congruence values (−i on the self-levelled −I cell), so hatch H-D
  (non-abelian data with non-zero coefficient) is **not** opened — the metaplectic cover is non-split as a group
  extension, yet on the positive cone it is a semigroup character with congruence values (RS §7.3 / Kubota).
* The remaining requirement is the H-A one: polylog-accurate control of Σ_t (Eisenstein coefficient at tn + 1) at one
  n, where the levels are different groups Γ₁(t) and different torsion points — no modular structure in t
  (§4: the t-sum is a shifted GL(3) object at a single n). This is the regime red team 2 assessed as quantitatively
  blocked (𝓛³ mass, Planck-scale targets). Assessment: no hypothesis of Thm 2.2 beyond finiteness is violated.

## 6. Quartic (numerator 8/16) — negative

`BRAINSTORM/z39_quartic_slices.md`: for p ≡ 1 (4) and any word, χ₄(A*) = χ₄(A)⁻¹ (AA* ≡ 1 mod p), so χ₄(A) itself is
not a u↔v-symmetric sign on the k | t non-residue slices (PROVED; other quartic invariants are not excluded); the ordered smaller-divisor bit is balanced (EVIDENCE, p < 2·10⁴,
k = 4, 8, 16). The k = 8 exceptions 131 (inert in ℤ[i]), 17, 241 show no quartic signature; consistent with
QUESTION_R §4.1 (4 and 8 share the quadratic invariant; the difference is B3).

## 7. Verdict (Assessment) and exact scope

1. **Exact dictionary (identity PROVED, classical ingredients, new to the campaign; modular reading Assessment):** the
   level-t ES generating function is (with its partner quadrant) a Kronecker theta quotient θ'(0)θ(2z)/θ(z)² at the t-torsion point z = (t−1)τ'/t, τ' = tτ (weight-1 holomorphic
   Eisenstein, odd characters mod t), plus the coefficients of a weight-0 Maass Eisenstein series (even characters),
   plus elementary ±2 and boundary corrections (Thm K). Every term is a Dirichlet-character divisor sum: no cusp form.
2. **Where things live:** the log² main term in the weight-0 non-holomorphic part; T1 as an exact cancellation of
   the odd-character against the even-character term on every level 4 | t at squares (Cor K1); the full sum over levels is
   an additively shifted, boundary-truncated d₃ (GL(3)-Eisenstein-type analogy only) object (§4).
3. **Half-integral weight:** by Serre–Stark only square classes can be supports of weight-½ forms: T1's squares are
   θ's support; any non-square failure (105) is provably not metaplectic for periods ≤ 96 and conditionally (SQ₅) at
   all (Prop S). The theta multiplier on the self-levelled −I Bruhat cell is the constant −i (§3).
4. **Barriers:** a metaplectic construction violates only the finiteness hypothesis of red team 2 Thm 2.2(iii) (H-A);
   the constructions examined here do not open H-D (per-level content abelian/congruence; other metaplectic
   constructions are not excluded by this argument), and the sum over levels has no modular structure in
   t (B2); B3 is visible as "main term in weight 0, oscillation in weight 1".
No existence mechanism, no pointwise statement, ES not touched.
