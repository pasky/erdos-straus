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
