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
σ_χ(N) = Σ_{d|N} χ(d), χ over Dirichlet characters mod t (the "−2/+2" removes the trivial divisors 1, N ≡ 1 (t)).
*Proof.* Kronecker (Weil, *Elliptic functions according to Eisenstein and Kronecker*, Ch. VIII; Zagier, Invent. Math.
104 (1991) §3): for |Q| < |x|, |y| < 1, Σ_{r,s≥0} x^r y^s Q^{rs} − Σ_{r,s≥1} x^{−r}y^{−s}Q^{rs} = (Q;Q)²θ(xy)/(θ(x)θ(y)).
Take x = y = X: |Q| < |X| < 1 for |q| < 1. Substituting u = r + 1, v = s + 1 (r, s ≥ 1) gives
q^{t−2}X^{r+s}Q^{rs} = q^{tuv−u−v}; substituting r = ρ + 1, s = σ + 1 in the negative quadrant gives
q^{t−2}X^{−r−s}Q^{rs} = q^{tρσ+ρ+σ}; the r = 0 or s = 0 terms of the positive quadrant sum to 2/(1−X) − 1 = (1+X)/(1−X).
(K2): (tu−1)(tv−1) = N and (tρ+1)(tσ+1) = N; u ≥ 2 ⟺ d = tu − 1 > t − 1. The character formulas are orthogonality
(1[d ≡ ±1] = φ(t)⁻¹Σ_χ χ̄(±1)χ(d)). ∎
Checks (`scripts/z39_kronecker.py`): (K1) numerically at q = 0.3 + 0.2i, t = 2..6 (|error| ≤ 10⁻¹³); (K2) for all
t ≤ 30, n ≤ 1500: 0 failures.

**Reading (modular status of each piece; standard facts, Assessment-level citations).**
* (Q;Q)²θ(X²)/θ(X)² is Kronecker's function F_{τ'}(z, z) = θ'(0)θ(2z)/θ(z)² (a meromorphic Jacobi form of weight 1,
  index 1) at τ' = tτ, z = ((t−1)/t)τ' — a **t-torsion point**. θ(X) ≠ 0 there, so it is holomorphic in τ; values of
  Kronecker's function at torsion points are weight-1 Eisenstein series (Hecke; Borisov–Gunnells, Invent. Math. 144
  (2001), "toric modular forms"). Concretely the odd part is Σ_N σ_χ(N)q^N, χ odd, = weight-1 holomorphic Eisenstein
  series E₁^{1,χ} ∈ M₁(Γ₀(t), χ) (Diamond–Shurman Thm 4.8.1, constant terms aside).
* The even part Σ_N σ_χ(N)q^N, χ even, is **not** holomorphic modular: it is the Fourier-coefficient sequence of the
  weight-0 (Maass) Eisenstein series E_χ(z, s) at the centre s = ½ (principal χ: the s-derivative, coefficients
  τ(N)·K₀ — the source of a log).
* So the level-t ES generating function is **half a weight-1 holomorphic Eisenstein series (a Kronecker theta
  quotient at a torsion point) plus half the coefficient sequence of a weight-0 Maass Eisenstein series**, minus the
  elementary boundary (1+X)/(1−X) (words with u = 1 or v = 1). No cusp form appears at any level.

**Corollary K1 (where the main term and T1 live; PROVED for the exact statements, EVIDENCE for sizes).**
Write R(n) = 𝔈(n) + 𝔒(n) − 𝔅(n) with 𝔈 = ½Σ_t E_t(tn+1) (weight-0 Maass part), 𝔒 = ½Σ_t O_t(tn+1) (weight-1
holomorphic part = Kronecker theta quotients at torsion points), 𝔅 = Σ_t β_t(n) = 2τ(n+1) − O(1) (words with u or v = 1).
1. *(T1 is an exact weight-0/weight-1 cancellation; PROVED.)* For odd m and every level t ≡ 0 (mod 4):
   R_t(m²) = 0 (all words with 4 | t lie in the (A)3 slice and have (A/n) = −1, DEDEKIND Thm 4.5 / QUESTION_R
   Prop 1.4; (A/m²) = +1), hence `E_t(tm² + 1) + O_t(tm² + 1) = 2β_t(m²)`: at every level 4 | t the coefficient of
   the Kronecker theta quotient equals **minus** the Maass-Eisenstein coefficient on the norm-form values 1 + tm².
   (Equivalently: tm² + 1 has no divisor ≡ −1 (mod t) beyond the boundary — the classical ET Type I obstruction.)
2. *(Sizes; EVIDENCE, `scripts/z39_split.py`, `/tmp` logs summarised here.)* At 12 primes just above 10⁵: 𝔈 ≈ 113
   (range 96–130), 𝔒 ≈ +7 (range −22…+37, sd ≈ 18), 𝔅 ≈ 54, R ≈ 67. At the odd squares 317², 319², 321², 323²:
   𝔈 ≈ 121, 𝔒 = −23, −46, −82, −77, and the split by t mod 4 shows 𝔒_{4|t} = −𝔈_{4|t} exactly (item 1) and most of
   the rest of the deficit at t ≡ 3 (4) (R_t small but non-zero there — consistent with R278's correction that
   QUESTION_R Cor 1.3's t ≡ 3 half is false).
   **Reading (Assessment).** The power-free "main term" log²n of the ES count is carried entirely by the weight-0
   non-holomorphic part 𝔈 (one log from the s-derivative of E(z, s) at s = ½, i.e. τ(N), one from Σ_t 1/φ(t) over
   levels); the holomorphic part 𝔒 averages to ≈ 0 at primes and is **where T1 lives**: at squares it cancels the
   main term level by level on 4 | t. So "Eisenstein main term + bounded cusp error" (Sturm/Duke) is the wrong
   template: at each level there is no cusp form; the competition is weight-0 Eisenstein vs weight-1 Eisenstein,
   both evaluated at the single integer tn + 1 — the divisor-in-class event (B2) in automorphic clothing.

## 2. Which half-integral weight objects can see the ES failure set (Prop S)

Full memo: `BRAINSTORM/z39_serre_stark_support.md`.
**Prop S (PROVED from Serre–Stark, LNM 627 (1977)).** Every holomorphic weight-½ form on Γ₁(4N) is a finite combination
of θ_{ψ,t} = Σ_m ψ(m)q^{tm²}; its support lies in finitely many square classes t·□, and on each class n = t₀m² the
coefficient is a periodic function of m. Therefore:
1. no weight-½ holomorphic form has support of positive density (the ES-five success set, or any ES success set);
2. the T1 part of the five-slice failure set **is** metaplectic: {m² : m odd} = supp(θ(z) − θ(4z));
3. the non-square failure 105 is **not** metaplectic: a weight-½ form vanishing exactly off the failure set would
   force failures at 105m² for all m ≡ 1 (mod M) (M = period); the exhaustive census to 10⁶ (DEDEKIND §9.1)
   excludes every M ≤ 96, and SQ₅ (CONJECTURE) every M.
So the answer to the brief's literal question ("an ES-side half-integral weight object whose support is the ES set and
whose vanishing at squares IS T1") is: **at weight ½, only the complement of the success set can be modelled, and only
its square part; T1 is the support of θ, nothing else in the failure set is.** At weight ≥ 3/2 (e.g. Zagier's ℋ)
supports are unrestricted but coefficients have power size (B3) — (J)39 Thm 2.2 already excludes N₋ as coefficients.

## 3. The multiplier on the cells ±Γ₁(c) (dictionary)

Full memo: `BRAINSTORM/z39_positive_coset.md`. In the normalisation γ_w = [[A, n],[t, A*]] the self-level condition
γ ∈ −Γ₁(t) is invariant under Γ_∞ × Γ_∞, so level-t ES words are the positive elements with b = n of the single
Bruhat cell Γ_∞[[−1, ∗],[t, −1]]Γ_∞ (one term of each Kloosterman sum mod t). Thm K's partner Q_t is the +I cell,
always non-empty ([[1,0],[t,1]][[1,n],[0,1]]); the −I analogue is not positive. Thm K's odd (weight-1) part is the
signed count over the two cells (parity of −I in odd weight). The theta multiplier refines this parity: on positive
self-levelled elements of −Γ₁(4), ν_θ = ε_d⁻¹(c/d) ≡ −i (QUESTION_R Prop 1.4; classical/RS input), on positive
elements of Γ₁(4) ν_θ = (a/b) ∈ {±1} (RS Lemma 3.1). T1 = imaginary multiplier on the −I cell is incompatible with
b = □. (PROVED dictionary; no mechanism.)

## 4. The sum over levels: a shifted ternary-divisor (GL(3)-Eisenstein-type) object

Summing Thm K over t first in the other order: Σ_n R(n)q^n = Σ_{t,u,v≥2} q^{tuv−u−v} = Σ_{u,v≥2} q^{2uv−u−v}/(1−q^{uv})
(PROVED, trivial), the specialisation x = y = q⁻¹ of the "rank-3 Kronecker series" Σ_{t,u,v} x^u y^v q^{tuv}, whose
x = y = 1 value is Σ d₃(n)q^n (minimal-parabolic SL₃(ℤ) Eisenstein coefficients). So (Assessment): the level-wise
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
  still abelian: the theta multiplier on γ_w is (A/n) = a character mod 4t of A (QUESTION_R Prop 1.2), so hatch H-D
  (non-abelian data with non-zero coefficient) is **not** opened — the metaplectic cover is non-split as a group
  extension, yet on the positive cone it is a semigroup character with congruence values (RS §7.3 / Kubota).
* The remaining requirement is the H-A one: polylog-accurate control of Σ_t (Eisenstein coefficient at tn + 1) at one
  n, where the levels are different groups Γ₁(t) and different torsion points — no modular structure in t
  (§4: the t-sum is a shifted GL(3) object at a single n). This is the regime red team 2 assessed as quantitatively
  blocked (𝓛³ mass, Planck-scale targets). Assessment: no hypothesis of Thm 2.2 beyond finiteness is violated.
