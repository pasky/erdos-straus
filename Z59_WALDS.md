# Z59_WALDS — the cusp / Waldspurger residue after TERNARY: odd squares force a *Gaussian-twist* central zero (Thm W1); the residue at a level is spanned by one line per such "Gauss-exceptional" eigensystem — confirmed exactly at 24 levels — and every one found is invalid at known (★)-zeros; single-twist positivity is not given by GRH and is conjecturally (and, at many 𝔐-primes, provably) false; validity is circular unless structural

Status: z59 lane WALDS (brief `z52bbriefs/z59_lanes.md` §WALDS; common rules `z52bbriefs/z58_lanes.md`, `z53_depth.md`).
Internal; internally reviewed only (§9). **ES is OPEN; nothing here proves or disproves ES, (★), (MS) or (MS⁺).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z59_walds_*`,
data `data/z59/walds/` (< 1 MB). Literature log: `data/z59/walds/lit_verify.md`.

**Verdict: narrowed** (exact dictionary + scoped no-go; no HOT LEAD). The Waldspurger residue left by TERNARY cannot
carry (MS) in the ternary-theta class:
1. T1 (odd squares) kills every Shimura eigensystem φ on the square class 𝒞₁ ⊇ 𝔐 unless the *Gaussian twist*
   G_φ = φ ⊗ ψχ_{−4} has L(G_φ, 1) = 0 (Thm W1, PROVED rel. Waldspurger 1981 Prop. 1 / Cor. 2, Shimura, TERNARY Thm F);
   each such φ contributes at most one line on 𝒞₁ (Lemma W1′).
2. Such Gauss-exceptional φ exist already at small level (e.g. φ = the conductor-84 curve y² = x³ − x² − 36x − 72,
   G_φ = φ ⊗ χ_{−168} of rank ≥ 2). An exact sweep of M_{3/2}(Γ₀(L), (D/·)) over 24 levels L | 3360 and all ψ
   (§5, CERTIFIED) finds T1-survivors on 𝒞₁ **exactly** where W1 predicts them (rank on 𝒞₁ = number of rational
   Gauss-exceptional φ, in every saturated run), and every survivor is non-zero at known (★)-zeros (5569, 9601, 23929,
   composite zeros): invalid.
3. Positivity of one eigensystem at a prime is L(G_φ ⊗ χ_p, 1) ≠ 0 for all large p in the class: not given by GRH, known
   only for positive proportions of fundamental discriminants, predicted false infinitely often by CKRS, and **proved
   false at many explicit 𝔐-primes** for the survivors found (§6).
4. Validity of an effective proxy *is* (MS) on its class (Prop W5); termwise (representation-recipe) validity is
   impossible on 𝒞₁ (Lemma W0).

Notation as in `Z58_TERNARY.md`. g ∈ M_{3/2}(Γ₀(4N), ψ) is a *ternary-theta proxy*: g = Σ cᵢθ_{Lᵢ} + h, Lᵢ positive
ternary lattices, h a cusp form, one nebentypus ψ (quadratic; pari/Shimura convention: θ_L has ψ = character of
ℚ(√det L), checked in §5.1), E = Σcᵢθ_{gen Lᵢ}. 𝒞₁(2N) = {n ≥ 1 : n ∈ ℤ_q^{×2} for every prime q | 2N}; for N with odd
prime divisors in {3,5,7}, 𝒞₁(2N) ⊇ {n : n mod 840 ∈ 𝔐} (TERNARY Cor F1). *Valid* (R-support): g(n) ≠ 0 ⟹ R(n) ≥ 1 for
all n ≡ 1 (4); *effective on a class 𝒞*: g(p) ≠ 0 for all sufficiently large primes p ∈ 𝒞. TERNARY Thm F: if g(ℓ²) = 0
for all large primes ℓ then E ≡ 0 on 𝒞₁(2N), the t = 1 unary thetas vanish, and g(p) = h⊥(p) at primes p ∈ 𝒞₁(2N).
D' := discriminant of ℚ(√−D) when ψ = (D/·); then ψχ_{−4} = χ_{D'} and G_φ := φ ⊗ χ_{D'}.

---

## 0. MANDATORY FALSIFIER TABLE

Mechanism examined: positivity of a valid half-integral-weight proxy at 𝔐-primes coming from its cusp coefficients,
i.e. (Waldspurger) from central values L(½, φ ⊗ ψχ_{−4}χ_p) at the single twist by p.

| screen | behaviour |
|---|---|
| **F1 odd squares** | **This is where the whole residue is decided.** An odd square m² (gcd(m,2N) = 1) lies in 𝒞₁ with squarefree part t = 1, and Waldspurger's twist character at t = 1 is χ₀^{−1} = ψ̄·(−1/·): the twist is **G_φ = φ ⊗ ψχ_{−4}**, field ℚ(√−d) for θ-lattices of determinant d (ℚ(i) for d = 1 — the field of the C = 1 norm form 4m²+1 = N(1+2mi) of T1; TERNARY Lemma D(d) uses ℚ(√−C)). Thm W1: T1 forces g_φ(1) = 0 for every eigensystem φ, and Waldspurger transports a(1) = 0 to the whole square class unless **L(G_φ, 1) = 0** ("Gauss-exceptional"). Non-squareness is used exactly here: the odd squares pin the anchor coefficient a(1). Exact check: the T1-kernel on 𝒞₁ has rank = #(rational Gauss-exceptional φ) at every saturated swept level (§5.2). |
| **F2 C-even (R₈)** | Everything negative here (W1, W2, W5, Lemma W0) is line-blind and applies verbatim to R₈-support proxies (R₈ also vanishes on odd squares), so nothing false is proved. The only positive statement (Prop W4, dictionary) is conditional on validity, which is the hypothesis; for an R₈-support proxy validity additionally demands L(½, G ⊗ χ_p) = 0 at the 4 in-𝔐 R₈-zero primes (not screened: conductors > 10¹⁴). |
| **F3 composites** | All 18 non-square composite R-zeros in 𝔐 ≤ 10¹⁰ (1969 … 17 401 609) are **squarefree**, hence in 𝒞₁ with their own twist χ_t; they enter exactly like prime zeros (Prop W4) and the survivors of §5.3 are non-zero at 1969, 2641, 5161 (invalid there too). Primality is *not* used anywhere in W1/W4/W5 beyond "t squarefree in 𝒞₁": the cusp route sees primes and squarefree composites of 𝒞₁ identically, so it cannot be the place where primality enters an (MS) proof. |
| **F4 known zeros** | Prop W4(d) (PROVED rel. Waldspurger Cor. 2): a proxy whose 𝒞₁-part is one Gauss-exceptional line is **invalid** as soon as that line is non-zero at one R-zero of 𝒞₁. **Exact screen (§5.3, CERTIFIED):** every T1-survivor found at the 24 swept levels is non-zero at known in-class R-zeros — the (★)-zero primes 5569 and 9601 (and 23929 at level 240), and the 𝔐 composite zeros 1969, 2641, 5161 — so every single-line proxy at these levels is invalid, and at every swept level with one survivor (all of them) **every valid proxy vanishes on 𝒞₁ ∩ [1, B]**. Supplementary numerical screen (§6.2): 7 larger-conductor Gauss-exceptional G (rank-2 curves) — each has rank-0 twists (numerically non-zero central value) at in-class (★)-zero primes. |

---

## 1. Precise statements attacked

**(Q1, dictionary).** For g a ternary-theta proxy (one ψ) with g(m²) = 0 for all odd m: give g(p), p ∈ 𝒞₁(2N) prime,
exactly in terms of Shimura eigensystems φ, twists and central values; say which non-vanishing would force a (★) hit.
**(Q2).** Is "L(½, G ⊗ χ_p) ≠ 0 for every large prime p in the class" implied by GRH, known, or as hard as (MS)?
**(Q3).** Falsifiers: central values / root numbers at t = 1 (F1), the in-class (★)-zero primes (F4) and the squarefree
composite zeros (F3).

**Prior closures used, not redone.** TERNARY Thm F, Cor F1, Lemma D; AUTOMORPH Thm A (integral weight);
POINTWISE_TERNARY Thm 4.1 (bounded-complexity recipes). TERNARY's single-eigensystem screen (15 curves, 4 zeros,
hypothesis (W-loc)) is superseded on 𝒞₁ by W1 + W4, which need neither (W-loc) nor the root-number case split.

## 2. Inputs (verified from sources; `data/z59/walds/lit_verify.md`)

* **(W-P1)** Waldspurger, *Sur les coefficients de Fourier des formes modulaires de poids demi-entier*, J. Math. Pures
  Appl. 60 (1981) 375–484, **Proposition 1 (Shimura), p. 377** (primary PDF read, pages 376–379 rendered and read):
  for k = 3 his S_{3/2}(N_W, χ) is the Petersson complement of the unary theta series in the cusp forms
  (p. 376, I.1); S_{k/2}(N_W, χ) = ⊕_{φ₀} S_{k/2}(N_W, χ, φ₀), φ₀ over the newforms (all levels) of weight k−1 and
  character χ², where S_{k/2}(N_W, χ, φ₀) = {f : T(p²)f = λ_p(φ₀)f for almost all p ∤ N_W}. His N_W is our 4N, χ = ψ.
  Prop. 2 (Flicker): this space is non-zero for some N_W iff (H1).
* **(W-C2)** ibid. **Corollaire 2, p. 379**: for φ₀ satisfying (H1), f ∈ S_{k/2}(N_W, χ, φ₀), n₁, n₂ squarefree with
  n₁/n₂ ∈ ℚ_p^{×2} for all p | N_W:
  a_{n₁}(f)² L(φ₀χ₀^{−1}χ_{n₂}, ½) χ(n₂/n₁) n₂^{k/2−1} = a_{n₂}(f)² L(φ₀χ₀^{−1}χ_{n₁}, ½) n₁^{k/2−1},
  with χ₀(n) = χ(n)(−1/n)^{(k−1)/2} (p. 377, I.3), χ_t = the quadratic character of ℚ(√t) (p. 378), and φν = the
  newform with λ_p(φν) = ν(p)λ_p(φ) for almost all p (p. 376). No hypothesis (H2) is needed for Cor. 2.
  For k = 3: χ₀^{−1}χ_t = ψ̄·χ_{−4}·χ_t, and L(·, ½) in his normalisation is the completed L-function at the centre
  (Γ-factor non-zero), i.e. the classical L(G, 1) for weight 2.
* **(W-T1)** ibid. **Théorème 1, pp. 378–379** (needs (H1) and (H2): the 2-adic component of φ₀ is not supercuspidal,
  or 16 | cond χ₀, or 16 | M(φ₀)): there is A: ℕ^{sc} → ℂ with A(t)² = L(φ₀χ₀^{−1}χ_t, ½)ε(χ₀^{−1}χ_t, ½), and every
  f ∈ S_{k/2}(N_W, χ, φ₀) is a combination of the series with coefficients a_n = A(n^{sc}) n^{(k−2)/4} ∏_p c_p(n), the
  c_p ∈ U_p(e_p, φ₀) being local functions invariant under ℤ_p^{×2}, with c_p = c_p⁰ (= 1 on v_p ∈ {0,1}) at p ∤ N_W.
  Used only in Prop W4(b) and Remark W3.
* **(S4)** Shimura 1973 Thm 1.7 (as in TERNARY (S4)): for ℓ ∤ 4N, (T(ℓ²)f)(n) = a(ℓ²n) + ψ(ℓ)(−n/ℓ)a(n) + ψ(ℓ²)ℓ a(n/ℓ²).
* **(IK)** Iwaniec–Kowalski, *Analytic Number Theory*, **Prop. 14.20, p. 377** (read by the research subagent from the
  book PDF): for a primitive f of level q, character χ, and a primitive ψ' mod r with (r, q) = 1, f ⊗ ψ' is primitive of
  level qr² with root number multiplied by χ(r)ψ'(q)τ(ψ')²/r; for χ trivial and ψ' = χ_t quadratic this factor is χ_t(−q).
* TERNARY Thm F and its inputs (S1)–(S5) (Siegel, Siegel–Weil, DSP 1990 Lemma 4, Shimura/Niwa, Deligne).

## 3. The exact dictionary (Q1)

### 3.1 Theorem W1 (T1 ⟹ Gaussian-twist filter)

**Theorem W1 (PROVED relative to TERNARY Thm F, (S4), (W-P1), (W-C2)).** Let g be a ternary-theta proxy in
M_{3/2}(Γ₀(4N), ψ), ψ quadratic, and suppose **(T1\*)**: g(m²) = 0 for every m ≥ 1 all of whose prime factors exceed some
fixed bound ℓ₀. (Every valid proxy satisfies (T1\*), since R(m²) = 0 for odd m.) Write h⊥ = Σ_φ g_φ with
g_φ ∈ S_{3/2}(4N, ψ, φ) (W-P1; finitely many φ with g_φ ≠ 0). Then:
(i) g_φ(1) = 0 for every φ;
(ii) for every squarefree t ∈ 𝒞₁(2N): g_φ(t)² · L(½, φ ⊗ ψχ_{−4}) = 0;
(iii) for every squarefree t ∈ 𝒞₁(2N), t > 1 (in particular every prime t ∈ 𝒞₁(2N)):
  **g(t) = Σ_{φ ∈ Φ_exc} g_φ(t)**, Φ_exc := {φ : g_φ ≠ 0, L(½, φ ⊗ ψχ_{−4}) = 0} ("Gauss-exceptional").
Here φ ⊗ ψχ_{−4} denotes the newform attached to the twisted eigensystem; put G_φ := φ ⊗ ψχ_{−4}.

*Proof.* (T1\*) contains g(ℓ²) = 0 for all primes ℓ > ℓ₀, so TERNARY Thm F applies: E vanishes on 𝒞₁(2N) and every
t = 1 unary series has coefficient 0 in g. Let P ⊇ {primes ≤ ℓ₀} ∪ {primes | 2N} be finite and so large that every
g_φ ≠ 0 is a T(ℓ²)-eigenform (eigenvalue λ_ℓ(φ)) for all ℓ ∉ P (finitely many φ, each "almost all ℓ").
*Step 1 (the square orbit is multiplicative).* Fix φ, f := g_φ, ℓ ∉ P, m with ℓ ∤ m, b_j := f(ℓ^{2j}m²),
ε(ℓ) := ψ(ℓ)(−1/ℓ). (S4) with n = m² gives b₁ = (λ_ℓ − ε(ℓ))b₀ (the last term vanishes as ℓ² ∤ m²); with n = ℓ^{2j}m²,
j ≥ 1, the middle term vanishes ((−n/ℓ) = 0) and b_{j+1} = λ_ℓ b_j − ψ(ℓ)²ℓ b_{j−1}. Hence
Σ_j b_j X^j = b₀(1 − ε(ℓ)X)/(1 − λ_ℓX + ψ(ℓ)²ℓX²), so b_j = α_{φ,ℓ}(j)·b₀ with α independent of m. Induction over
the prime factorisation gives f(m²) = f(1)·A_φ(m) for every m coprime to P, A_φ(m) := ∏_{ℓ^j ∥ m} α_{φ,ℓ}(j),
A_φ(1) = 1, and A_φ(ℓm) = (λ_ℓ(φ) − ε(ℓ))A_φ(m) for ℓ ∉ P, ℓ ∤ m.
*Step 2 (only the cusp part sees m²).* For m coprime to P: m² ∈ 𝒞₁(2N), so E(m²) = 0; a unary series h_{χ,t'} (t' | N)
has a non-zero coefficient at m² only if t' = 1, and those coefficients are 0. So (T1\*) gives
Σ_φ c_φ A_φ(m) = 0 for all m coprime to P, c_φ := g_φ(1).
*Step 3 (Dedekind-type independence).* Claim: if Σ_φ c_φ A_φ(m) = 0 for all m coprime to a finite set P' ⊇ P, then all
c_φ = 0. Induction on the number of φ with c_φ ≠ 0. One: c_φ = c_φ A_φ(1) = 0. At least two, say φ₁ ≠ φ₂: their
eigenvalue systems differ at infinitely many primes — otherwise S(4N, ψ, φ₁) = S(4N, ψ, φ₂) by the "almost all p"
definition, contradicting the directness of (W-P1) since g_{φ₁} ≠ 0. Pick ℓ ∉ P' with λ_ℓ(φ₁) ≠ λ_ℓ(φ₂). For m coprime
to P' ∪ {ℓ}, apply the relation at ℓm and subtract (λ_ℓ(φ₁) − ε(ℓ)) times the relation at m:
Σ_φ c_φ(λ_ℓ(φ) − λ_ℓ(φ₁))A_φ(m) = 0. The new coefficients vanish at φ₁ and not at φ₂; by induction (with P' ∪ {ℓ})
they all vanish — contradiction. Hence (i).
*Step 4.* For squarefree t ∈ 𝒞₁(2N), t/1 ∈ ℚ_q^{×2} for every q | 4N, so (W-C2) with (n₁, n₂) = (1, t) and f = g_φ (S ≠ 0
implies (H1) by Prop. 2) gives g_φ(1)²L(φψ̄χ_{−4}χ_t, ½)ψ(t)t^{1/2} = g_φ(t)²L(φψ̄χ_{−4}, ½); the left side is 0 by (i):
(ii). (ψ̄ = ψ.) *Step 5.* For squarefree t ∈ 𝒞₁, t > 1: E(t) = 0 (Thm F); a unary series h_{χ,t'} (t' | N) is supported
on t'k², and t = t'k² with t squarefree forces k = 1, t = t' | N, impossible for t > 1 a unit at every prime of N. So
g(t) = Σ_φ g_φ(t), and by (ii) only φ ∈ Φ_exc can contribute: (iii). ∎

**Remarks.** (a) Only *squares of integers built from large primes* are used (any ℓ₀). With prime squares only (Thm F's
hypothesis) Step 3 needs instead linear independence of cuspidal eigenvalue sequences and a character on primes
(Rankin–Selberg/Chebotarev; standard, *not verified here, not used*). (b) Mixed-nebentypus combinations are not
covered by Step 3 (pairs (φ, ψ) can share α_ℓ(1) on a density-½ set); positive mixed combinations are covered by
Lemma W0. (c) W1 is purely about 𝒞₁; off 𝒞₁ the genus term can survive (TERNARY Remark F2).

### 3.2 Corollary W2 and Lemma W1′ (structure of the residue on 𝒞₁)

**Corollary W2 (PROVED rel. the same inputs).** If L(G_φ, 1) ≠ 0 for every φ with S(4N, ψ, φ) ≠ 0, then every
ternary-theta proxy g ∈ M_{3/2}(Γ₀(4N), ψ) satisfying (T1\*) vanishes at every squarefree n ∈ 𝒞₁(2N) — in particular at
every 𝔐-prime when the odd primes of N lie in {3,5,7}. (W1(iii) with Φ_exc = ∅.) The residue is then empty, not merely
unforced. (§5: this is the situation at most swept (L, ψ); at the others exactly the predicted exceptional φ appear.)

**Lemma W1′ (one line per eigensystem; PROVED rel. (W-C2)).** Let φ be given and suppose L(G_φ ⊗ χ_{t₀}, 1) ≠ 0 for some
squarefree t₀ ∈ 𝒞₁(2N). Then for every squarefree t ∈ 𝒞₁(2N) the linear functionals x_t : f ↦ a_t(f) on S(4N, ψ, φ)
satisfy x_t = ±κ_t^{1/2}·x_{t₀} with κ_t := L(G_φ⊗χ_t, 1)t^{1/2}/(L(G_φ⊗χ_{t₀}, 1)ψ(t₀/t)t₀^{1/2}) (the sign may depend
on t, not on f). Hence the restriction of S(4N, ψ, φ) to the squarefree coefficients of 𝒞₁ has dimension ≤ 1, and
x_t ≡ 0 ⟺ L(G_φ ⊗ χ_t, 1) = 0 (if x_{t₀} ≢ 0).
*Proof.* (W-C2) with (n₁, n₂) = (t, t₀) gives x_t(f)² = κ_t x_{t₀}(f)² for every f, an identity of quadratic forms on
S(4N, ψ, φ); in the polynomial ring (a domain) x_t² − κ_t x_{t₀}² = (x_t − κ_t^{1/2}x_{t₀})(x_t + κ_t^{1/2}x_{t₀}) = 0
forces one factor to vanish. ∎
So the T1-valid part of M_{3/2}(Γ₀(4N), ψ) restricted to squarefree 𝒞₁ coefficients has dimension ≤ |Φ_exc(N, ψ)|,
one explicit line s_φ per Gauss-exceptional φ (whose t-th entry is ±(const)·(t·L(G_φ⊗χ_t,1))^{1/2}).

**Remark W3 (sign).** By (IK), for squarefree t ∈ 𝒞₁(2N) the root number of G_φ ⊗ χ_t equals ε(G_φ)χ_t(−M_{G_φ}) = ε(G_φ):
χ_t is even (t > 0), and χ_t(q) = (t/q) = 1 for every prime q | M_{G_φ} (all such q divide 2N; t ≡ 1 (8) and t is a
non-zero square mod each odd q | N). So the sign is constant on 𝒞₁. If ε(G_φ) = −1 then L(G_φ ⊗ χ_t, ½) = 0 for every
squarefree t ∈ 𝒞₁, and under (H2) Théorème 1 gives g_φ(t) = 0 there (constant local factor on 𝒞₁, see W4(b)); without
(H2) — e.g. φ supercuspidal at 2, which is automatic for trivial character and 2-adic conductor exponent 2 or 3 — this
case is CONDITIONAL on the factorisation (W-loc). Hence every φ that actually contributes on 𝒞₁ has (under (H2))
ε(G_φ) = +1 and a central zero of even order ≥ 2: **L(G_φ, s) has a double central zero**.

### 3.3 Proposition W4 (the dictionary at a prime, and the validity test)

**Proposition W4.** Let g be as in W1, φ ∈ Φ_exc, G := G_φ, and t, t₀ squarefree in 𝒞₁(2N).
(a) (PROVED rel. (W-C2)) If g_φ(t₀) ≠ 0 and L(½, G ⊗ χ_t) ≠ 0, then g_φ(t) ≠ 0.
(b) (PROVED rel. (W-T1), needs (H2) for φ) g_φ(t) = K_φ(g)·t^{1/4}·A_φ(t) with A_φ(t)² = L(½, G ⊗ χ_t)·ε(½, ψχ_{−4}χ_t),
    K_φ(g) a constant independent of t ∈ 𝒞₁ (the local functions c_p are ℤ_p^{×2}-invariant, so ∏_{p|4N} c_p(t) = ∏ c_p(1),
    and c_p(t) = 1 at p ∤ 4N for squarefree t). Hence for a prime p ∈ 𝒞₁(2N), p ∤ N:
    **g(p) = p^{1/4} Σ_{φ ∈ Φ_exc} K_φ(g) A_φ(p).**
(c) (Dictionary.) If g is valid, then Σ_{φ∈Φ_exc} K_φ A_φ(p) ≠ 0 ⟹ R(p) ≥ 1. For |Φ_exc| = 1 this reads:
    K_φ ≠ 0 and **L(½, G_φ ⊗ χ_p) ≠ 0 ⟹ R(p) ≥ 1**, where G_φ ⊗ χ_p = φ ⊗ ψχ_{−4p}; for ψ = 1 the twisting field is
    ℚ(√−p) (discriminant −4p), for θ-lattices of determinant d it is ℚ(√(−dp)) up to squares.
(d) (Validity test, single eigensystem; PROVED rel. (W-C2).) If g = E + u + g_φ with one φ ∈ Φ_exc and g(t₀) ≠ 0 for
    some squarefree t₀ ∈ 𝒞₁, t₀ > 1, then g is invalid as soon as L(½, G ⊗ χ_p) ≠ 0 for one squarefree R-zero
    p ∈ 𝒞₁(2N) (prime or composite).
*Proof.* (a) (W-C2) with (n₁, n₂) = (t₀, t): g_φ(t₀)²L(G⊗χ_t, ½)ψ(t/t₀)t^{1/2} = g_φ(t)²L(G⊗χ_{t₀}, ½)t₀^{1/2}; the left side
is non-zero. (b) is (W-T1)(ii) restricted to 𝒞₁ as indicated, with n^{(k−2)/4} = n^{1/4}. (c) is the definition of validity
plus (b) and W1(iii). (d) By W1(iii) g(t₀) = g_φ(t₀) ≠ 0; by (a) g(p) = g_φ(p) ≠ 0 while R(p) = 0. ∎

So the exact dictionary is: **forms** = Shimura eigensystems φ (weight-2 newforms of trivial character, level | 2N) that
are Gauss-exceptional; **discriminants** = −4t·(det-class) for squarefree t ∈ 𝒞₁ (−4p at an 𝔐-prime, −4 at the odd
squares); **the non-vanishing that would force a hit** = non-cancellation of Σ_φ K_φ A_φ(p), i.e. for one eigensystem
L(½, G_φ ⊗ χ_p) ≠ 0 — *provided* the proxy is valid, which is the subject of §4.2.

## 4. Q2: what kind of statement is the single-twist non-vanishing, and what would validity cost

### 4.1 GRH, known results, conjectures (literature verified, §2 and `lit_verify.md`)
* **GRH does not give it** (Assessment, elementary): GRH constrains Re ρ only; a zero at s = ½ is on the critical line.
  W1/W3 make the point sharp: every contributing G_φ *itself* has a central zero (of even order ≥ 2 in all cases found),
  and §6.1 exhibits, for the survivors actually found, many 𝔐-primes p with L(G_φ ⊗ χ_p, 1) = 0 (PROVED from exact
  half-integral coefficients via Lemma W1′).
* **Under GRH, only proportions**: Heath-Brown, Duke Math. J. 122 (2004), Thm 3 (average analytic rank ≤ 3/2 + o(1) in
  each sign family, under RH for the twists) and Thm 4 (≥ 1/4 of the + family has rank 0, weighted). Nothing pointwise.
* **Unconditionally, only positive proportions over fundamental discriminants, not primes**: Ono–Skinner, Invent. Math.
  134 (1998), Cor. 3: #{|D| ≤ X : L(F ⊗ χ_D, k) ≠ 0} ≫ X/log X; the prime-twist case is explicitly left open there.
  Ono, Crelle 533 (2001), Thm 1: non-vanishing for twists by products of an *even* number of primes from a Frobenius set.
* **Conjecturally it is false**: Conrey–Keating–Rubinstein–Snaith (Number Theory for the Millennium I, 2002;
  arXiv math/0012043), **Conjecture 1, eq. (25)**: for an elliptic curve E, #{p ≤ T prime : L_E(½, χ_p) = 0, sign +} ∼
  c_E T^{3/4}(log T)^{−5/8}. If this (or its natural residue-class version, not stated there — Assessment) holds for
  G_φ, then for every Gauss-exceptional φ there are ≫ T^{3/4−ε} primes p ≤ T in 𝒞₁ with L(G_φ ⊗ χ_p, 1) = 0: **a
  single-eigensystem proxy is never effective** (CONJECTURE via CKRS).
* **Sums of several eigensystems.** Effectiveness = non-cancellation of Σ_φ K_φ A_φ(p); the signs of the "square roots"
  A_φ(p) are not determined by L-values; the best sign results (Lester–Radziwiłł, Math. Ann. 379 (2021), Thms 1–2) give
  many sign *changes* of half-integral-weight coefficients (plus space / squarefree indices), nothing pointwise.
  *Heuristic (Assessment).* For g with rational coefficients, g(p) is a rational number of bounded denominator and size
  ≈ p^{1/4}·L^{1/2}; the CKRS discretisation heuristic (vanishing probability ≈ p^{−1/4} up to logs) applies to it
  unchanged, and Σ_p p^{−1/4}/log p diverges. So **any pure-cusp proxy is expected to vanish at ≍ T^{3/4} primes of its
  class**. Contrast (★): R(p) ≍ log²p on average, and the expected number of 𝔐-zeros is finite. *The cusp residue is
  heuristically strictly worse than (MS): (MS) is believed true, "an effective pure-cusp proxy exists" is believed false.*

### 4.2 Proposition W5 (validity is circular unless structural)
**Proposition W5 (PROVED, elementary).** Let 𝒞 be a set of primes and g any arithmetic function that is effective on 𝒞.
Then "g is valid at all sufficiently large p ∈ 𝒞" ⟺ "R(p) ≥ 1 for all sufficiently large p ∈ 𝒞".
*Proof.* ⟹: effective + valid gives R(p) ≥ 1. ⟸: if R(p) ≥ 1 for large p, the implication g(p) ≠ 0 ⟹ R(p) ≥ 1 holds
trivially there. ∎
So for an effective proxy, *validity on 𝔐-primes is (MS)*. A proxy helps only if its validity has a reason that does
not pass through R — a **structural** mechanism, e.g. g = Σ cᵢ θ_{Lᵢ} with a recipe turning each representation by Lᵢ
into a (★) certificate (termwise validity). Lemma W0 kills that on 𝒞₁:

**Lemma W0 (PROVED rel. TERNARY Thm F).** Let L be a positive ternary lattice of level dividing 4N with r_L(ℓ²) = 0 for
all sufficiently large primes ℓ. Then r_L(n) = 0 for every n ∈ 𝒞₁(2N). Consequently: (a) a non-negative combination
Σ cᵢθ_{Lᵢ} (cᵢ ≥ 0, *any* nebentypus, levels 4Nᵢ) vanishing at large prime squares vanishes on ∩ᵢ 𝒞₁(2Nᵢ);
(b) **no ternary lattice of level 4N whose representations all yield (★) certificates represents any n ∈ 𝒞₁(2N)** —
in particular none represents an 𝔐-integer when the odd primes of N lie in {3,5,7}, and for general N none represents
a prime p ≡ 1 (8) that is a quadratic residue modulo every odd prime of N (e.g. any p with n_p larger than every odd
prime of N).
*Proof.* Apply Thm F to g = θ_L (one lattice, (H_δ) trivial): E = θ_{gen L} vanishes on 𝒞₁(2N). θ_{gen L}(n) is Siegel's
weighted average of r_{L'}(n) ≥ 0 over the classes L' of the genus with positive weights, L among them; so r_L(n) = 0.
(a): T1 at ℓ² and non-negativity give r_{Lᵢ}(ℓ²) = 0 for each cᵢ > 0. (b): a recipe-valid L has r_L(m²) = 0 for all odd
m (T1). ∎
Finite sanity check (§5.2): diagonal forms ⟨a,b,c⟩ that miss all odd squares ≤ 10⁴ represent no n ∈ 𝒞₁ ≤ 10⁴.

**Consequence (scoped no-go, PROVED rel. cited inputs).** In the ternary-theta class (one ψ for W1/W2/W4, any ψ for
W0), a proof of (MS) through a half-integral-weight proxy on 𝔐 needs *simultaneously*: (1) Gauss-exceptional
eigensystems at the chosen level (none at the levels of §5); (2) a non-structural validity mechanism — an identity
forcing g(n) = 0 at every R-zero of 𝒞₁ through cancellation between lattices, which by W5 cannot be "validity at large
primes" itself; (3) non-cancellation of Σ K_φ A_φ(p) at every large 𝔐-prime — for one eigensystem a single-twist
non-vanishing statement that GRH does not give and CKRS predicts to fail infinitely often.

## 5. Computations I — the T1-kernel at small levels (CERTIFIED, exact rational linear algebra)

### 5.1 Setup
`scripts/z59_walds_halfint.py L D B l0`: full space M_{3/2}(Γ₀(L), (D/·)) (pari `mfinit(…,4)`: Eisenstein + cusp incl.
unary thetas), coefficients a(0…B) exactly; T1 rows g(m²) = 0 for all odd m ≤ √B (l0 = 0, validity) or for primes
ℓ ≥ 11 only (l0 = 11, Thm F's weaker hypothesis); exact kernel K; rank of K restricted to the coefficients at
n ∈ 𝒞₁(2N) ∩ [1, B] (and at squarefree / prime / 𝔐 members). Nebentypus convention checked: θ_{⟨1,1,1⟩} ∈ (4, χ₁),
θ_{⟨1,1,3⟩} ∈ (12, χ₁₂), θ_{⟨1,1,5⟩} ∈ (20, χ₅), θ_{⟨1,1,2⟩} ∈ (8, χ₈), θ_{⟨1,3,5⟩} ∈ (60, χ₆₀) (pari `mfparams`).
Sweep `scripts/z59_walds_halfint_sweep.sh`: every positive fundamental D (and D = 1) with D | L; negative D give 0.

### 5.2 Results: the T1-kernel on 𝒞₁ is exactly the predicted Gauss-exceptional span
Levels L = 4N for N | 840 with N squarefree or N ∈ {4, 8, 12, 20, 28, 60, 84, 140, 210}: L ∈ {4, 8, 12, 16, 20, 24, 28,
32, 40, 48, 56, 60, 80, 84, 112, 120, 140, 168, 240, 280, 336, 420, 560, 840} (24 levels), every admissible ψ, B = 10⁴
(8000 for L ∈ {16, 32, 48, 80, 112, 240, 336, 560, 840}; L = 840 also cusp space with B = 16 000), both T1 variants.
Files `halfint_sweep_{A,B,C}.txt`, `halfint_840_cusp_B16000.txt`; summary `sweep_summary.txt`, comparison
`compare_W1.txt` (`scripts/z59_walds_compare.py`).

**Prediction (W1 + W1′).** rank on 𝒞₁ ≤ |Φ_exc(N, ψ)|, with equality when every exceptional φ has a non-zero 𝒞₁ line.
The rational part of Φ_exc is computed independently (`scripts/z59_walds_identify.py` → `identify_rational_1680.txt`):
the 64 isogeny classes of conductor | 1680 found in the box |a₄| ≤ 150, |a₆| ≤ 1500 (completeness of the box not
claimed), twisted by all 16 negative fundamental D' | 3360; G_φ is *exceptional* if root number +1 and pari `ellrank`
proves rank ≥ 2 (so L(G_φ, 1) = 0 by Gross–Zagier–Kolyvagin; lit_verify #12).

**Outcome (CERTIFIED: exact rational arithmetic in pari; EVIDENCE for the B-independence).**
Of the 123 runs with all-odd-square rows (`compare_W1.txt`), 121 match the prediction exactly; the 2 that do not are
the unsaturated runs (840, χ₁₀₅) and (840, χ₈₄₀) at B = 8000 (rows at full rank 45 = #rows, observed 5), which match at
B = 16 000 (cusp space; rank 1 each). Non-zero survivors (all rank 1; φ given by its conductor and Weierstrass data):

| L | ψ | D' | φ (conductor | 2N) with L(φ ⊗ χ_{D'}, 1) = 0 |
|---|---|---|---|
| 168 | χ₁₆₈ | −168 | 84: [0,−1,0,−36,−72] |
| 240 | χ₁₂₀ | −120 | 120: [0,1,0,−136,560] |
| 280 | χ₅₆ | −56 | 70: [0,0,0,37,−138] |
| 336 | χ₅₆ / χ₁₆₈ | −56 / −168 | 24: [0,−1,0,−69,189] / 84 |
| 420 | χ₂₁ / χ₁₀₅ | −84 / −420 | 210: [0,−1,0,−56,−84] / 105: [0,1,0,−120,−432] |
| 560 | χ₅₆ / χ₂₈₀ | −56 / −280 | 70 / 56: [0,−1,0,−40,−84] |
| 840 | χ₂₁, χ₅₆, χ₁₀₅, χ₁₆₈, χ₂₈₀, χ₈₄₀ | −84, −56, −420, −168, −280, −840 | 210, 70, 105, 84, 420: [0,1,0,−85,83], 420 |

Every other (L, ψ) — in particular every ψ at the 16 levels L ≤ 140 and at L = 420 for ψ ∈ {1, 5, 12, 28, 60, 140} —
has T1-kernel identically 0 on 𝒞₁ ∩ [1, B] (Cor W2 situation). The l0 = 11 variant (prime squares ≥ 11 only) gives the
same survivors at saturated levels (`sweep_summary.txt`).
* In **every** run whose T1 rows did not reach full rank (the kernel is saturated in practice) the observed rank on
  𝒞₁ equals the number of rational Gauss-exceptional φ of conductor | 2N for the twist D' — 0 at most (L, ψ), 1 at
  the 11 (L, ψ) listed; the 2 unsaturated runs (L = 840, B = 8000) are resolved at B = 16 000 (cusp space).
  No irrational exceptional φ is visible at these levels.
* The survivors are *exactly* the ones W1 names, e.g. at (L, ψ) = (168, χ₁₆₈) the survivor's implied Shimura
  eigenvalues a(193ℓ²)/a(193) + ψ(ℓ)(−193/ℓ) are 4, 2, −6 at ℓ = 5, 11, 13 = a_ℓ of the conductor-84 curve
  y² = x³ − x² − 36x − 72, whose twist by χ_{−168} (conductor 28 224) has rank ≥ 2 (`ellrank` [2,2]); at (240, χ₁₂₀) the
  eigenvalues 4, 0 at ℓ = 7, 11 match the conductor-120 curve [0,1,0,−136,560] with G = twist by χ_{−120} of rank ≥ 2;
  at (280, χ₅₆) λ₃ = 0, λ₁₁ = 4 match the conductor-70 curve (`diag_survivors.txt`).

### 5.3 The survivors are invalid (F4/F3, CERTIFIED exact coefficients)
`scripts/z59_walds_diag.py L D 40000` (cusp space, all odd-square rows, B = 4·10⁴), `diag_survivors.txt`: at each of the
nine levels L ≤ 560 with a survivor, the survivor is non-zero at known R-zeros of its class 𝒞₁(2N):
(168, χ₁₆₈): (★)-zeros 5569, 9601; 𝔐 composite zeros 2641, 5161. (280, χ₅₆): 5569, 9601; composite 1969, 2641.
(240, χ₁₂₀): 5569, 9601, 23929; composites 1969, 2641, 5161. (420, χ₂₁), (420, χ₁₀₅): composites 1969/5161 resp.
2641/5161 (the prime zeros there vanish on the survivor — validity still fails at the composites).
(336, χ₅₆) and (336, χ₁₆₈): 5569, 9601; composites 1969 resp. 2641, 5161. (560, χ₅₆): 5569, 9601; 1969, 2641.
(560, χ₂₈₀): 5569, 9601; 1969, 5161. (The L = 840 survivors are the same eigensystems as at 168, 280, 420.)
Since each of these (L, ψ) has a one-dimensional 𝒞₁-restriction (rank 1), **every valid proxy of that level and
nebentypus vanishes at every n ∈ 𝒞₁(2N), n ≤ B** (CERTIFIED), and at every squarefree n ∈ 𝒞₁(2N) whatsoever
(PROVED rel. W1, W1′, *if* Φ_exc(N, ψ) contains no irrational φ — EVIDENCE only: none visible ≤ B).

### 5.4 Lemma W0 sanity check
`scripts/z59_walds_w0check.py 24 20000` (`w0check.txt`): of the 2106 primitive diagonal forms ⟨a,b,c⟩, c ≤ 24, 574
represent no odd square ≤ 2·10⁴, and none of these 574 represents any n ∈ 𝒞₁(2·lcm(a,b,c)), n ≤ 2·10⁴ (as Lemma W0
predicts; in these examples the obstruction is visibly 2-adic/local).

## 6. What the survivors say about Q2 and the larger-conductor screen

### 6.1 Single-twist positivity fails at explicit 𝔐-primes (PROVED from exact data via Lemma W1′)
For a survivor line s_φ (non-zero anchor t₀), Lemma W1′ gives: s_φ(p) = 0 ⟺ L(G_φ ⊗ χ_p, 1) = 0. The exact coefficients
show many such primes:
* (168, χ₁₆₈), φ = 84-curve, G ⊗ χ_p = E₈₄ ⊗ χ_{−168p}: the survivor vanishes at **57 of the 238 primes p ∈ 𝒞₁(84),
  p ≤ 4·10⁴**, 36 of them in 𝔐 (1009, 1129, 1201, 1801, 4201, 4729, 5209, 7561, …; `diag_168_168.txt`).
* (560, χ₂₈₀), φ = 56-curve: vanishes at 54 of 238 primes of 𝒞₁(280) ≤ 4·10⁴, 28 in 𝔐 (1009, 1801, 3889, 6841, …).
* Independent cross-check (`scripts/z59_walds_crosscheck.py` → `crosscheck_168.txt`): for the first 13 vanishing primes
  (337 … 4729) pari `ellrank` finds two independent points on E₈₄ ⊗ χ_{−168p} (rank ≥ 2, rigorous; hence
  L = 0 unconditionally by Gross–Zagier–Kolyvagin), and for 10 non-vanishing ones (193, 673, …, 5569, 9601) the
  numerical analytic rank is 0 with central value 1.6–19. The half-integral coefficients and the L-values agree in all 23
  cases — a direct check of the Waldspurger dictionary of Prop W4 / Lemma W1′ at this level.
(The PROVED reading of the full lists uses Lemma W1′ with Φ_exc = {φ}, i.e. no invisible irrational exceptional
eigensystem at that level; the 13 cross-checked primes are unconditional.)
So, for these eigensystems, "L(G_φ ⊗ χ_p, ½) ≠ 0 for all large p ∈ 𝔐" is false at every prime listed (a theorem, not a
heuristic), and its frequency is in line with CKRS (§4.1). A single-eigensystem proxy built from them is neither valid
(§5.3) nor effective.

### 6.2 Larger-conductor Gauss-exceptional G (EVIDENCE, numerical)
`scripts/z59_walds_rank2_search.py` (`rank2_search.txt`): rank-2, sign-+1 curves with conductor supported on {2,3,5,7}
(3888, 5184, 5760, 6912, 10368, 11520, 12096, 12544, 15552, 15680). For seven of them, `scripts/z59_walds_f4.py`
(`f4_screen.txt`, summary `f4_summary.txt`; conductor cap 5·10¹³) computes the twists G ⊗ χ_t at t = 1, the in-class
(★)-zero primes, composite zeros ≤ 3·10⁴ and 8 controls: t = 1 has rank 2 for all (sanity: they are Gauss-exceptional
for ψ = 1-type classes of the right level); **each G has rank-0 twists (numerically non-zero central values 0.31–11.3)
at in-class (★)-zero primes** (e.g. 9601 for six of the seven) ⟹ by Prop W4(d) every single-line proxy built on them
is invalid (EVIDENCE: numerical central values; `ellrank` upper bound 0 agrees). Rank ≥ 2 twists (rigorous lower bound)
occur among the controls at rates 1/8–5/8 — zeros and controls alike. (The levels 4N hosting these φ, and whether
S(4N, ψ, φ) ≠ 0 there, were not computed; the screen is of the L-functions.)

## 7. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: narrowed.**
* PROVED (rel. Waldspurger 1981 Prop. 1/Cor. 2, Shimura's T(ℓ²) formula, TERNARY Thm F): Thm W1 (T1 ⟹ only
  Gauss-exceptional eigensystems survive on the square class), Lemma W1′ (one line each), Prop W4 (dictionary and the
  validity test; (b) needs (H2)), Prop W5 (validity of an effective proxy = (MS) on its class), Lemma W0 (no recipe
  lattice represents the square class). Remark W3 (sign −1 harmless) needs (H2), else CONDITIONAL on (W-loc).
* CERTIFIED: at 24 levels L | 3360 and all ψ, the T1-kernel on 𝒞₁ is exactly the predicted exceptional span (rank 0 or 1);
  each survivor is non-zero at known R-zeros (5569, 9601, 23929; composites 1969, 2641, 5161), so at these (L, ψ) every
  valid proxy vanishes on 𝒞₁ ≤ B.
* PROVED from exact data: explicit 𝔐-primes p with L(G_φ ⊗ χ_p, 1) = 0 for the survivors (§6.1).
* Assessment/CONJECTURE: single-eigensystem effectiveness fails infinitely often (CKRS Conj. 1); rational pure-cusp
  proxies of any shape are expected to vanish at ≍ T^{3/4} primes ≤ T of the class — the cusp residue is heuristically
  *worse* than (MS).
* **Escapes left (named, not excluded):** (E-a) levels with many Gauss-exceptional φ (they grow with the level) and a
  *non-structural* validity identity — by W5 such an identity must not be "validity at large primes", it must explain the
  R-zeros of 𝒞₁ (finitely many known; their finiteness is (MS⁺)-type); (E-b) coset theta series / theta series with
  characteristics (Thm F and W0 not proved for them; a coset-Siegel–Weil version of Thm F is expected, Assessment);
  (E-c) mixed nebentypus signed combinations (W1 Step 3 not covered); (E-d) off-𝒞₁ classes at levels with primes
  ℓ ∉ {3,5,7}: there the genus term survives (TERNARY Remark F2), and Lemma W0 allows recipe lattices — but a fixed finite
  family of them only certifies primes that are non-residues mod some prime of their levels, so it misses every prime
  p ≡ 1 (mod 8·∏ℓ) (Dirichlet; Lemma W0(b)), i.e. p-dependent levels involving a prime ℓ with (p/ℓ) = −1, ℓ ≥ n_p are
  needed — this is the B2 / n_p wall (WITNESS Lemma 1.1) again.

**FRONTIER §4 hard screens.** T1 squares: W1 *is* T1, transported by Waldspurger from a(1) to the square class.
8/131 (line): all negative statements are line-blind (apply to R₈-support proxies). Tied modulus: the tied event is
invisible to the half-integral side — the survivors are dictated by L-values of G_φ ⊗ χ_t and are non-zero at
(★)-zeros. Fixed p: statements are pointwise in p after fixing the level; the positive direction would be a fixed-p
non-vanishing that is false at explicit p.

**Proposed FRONTIER §6/§7 text (do not edit FRONTIER here).**
> *Waldspurger residue (z59 WALDS, PROVED rel. Waldspurger 1981 Prop. 1/Cor. 2 + TERNARY Thm F).* For a ternary-theta
> proxy g ∈ M_{3/2}(Γ₀(4N), ψ) vanishing at the odd squares, every Shimura eigensystem φ contributes on the square class
> 𝒞₁ (⊇ 𝔐 for {3,5,7}-levels) at most one line, and only if its Gaussian twist G_φ = φ ⊗ ψχ_{−4} has L(G_φ, ½) = 0
> ("Gauss-exceptional"). Exact sweep (24 levels | 3360, all ψ): the surviving lines are exactly the predicted ones
> (rank 0 or 1) and every survivor is non-zero at known (★)-zeros (5569, 9601, …) — invalid; at these levels every valid
> proxy vanishes on 𝒞₁. Positivity of one line at p is L(G_φ ⊗ χ_p, ½) ≠ 0: not given by GRH, false at explicit
> 𝔐-primes, predicted false infinitely often (CKRS). Validity of an effective proxy is (MS) on its class; recipe
> lattices miss 𝒞₁ entirely (Lemma W0). Add to §6: "cusp/Waldspurger single-twist positivity for ternary proxies on 𝔐".
> Escapes: many-φ levels with a non-structural validity identity; coset thetas; mixed ψ; p-dependent levels (= B2).

**Bottom line.** TERNARY left (MS) on 𝔐, in half-integral weight, as a pure cusp problem governed by Waldspurger. Making
the dictionary exact shows the odd squares do far more than kill the Eisenstein part: since an odd square has
squarefree part 1, T1 pins the anchor coefficient a(1) of every Shimura component to zero, and Waldspurger's
Corollary 2 then forces each component to vanish on the entire square class unless its Gaussian twist has a central
zero. An exact computation at 24 levels finds the surviving lines precisely where this predicts (attached to elliptic
curves of conductor 24–420 whose twists by χ_{−56}, χ_{−84}, χ_{−120}, χ_{−168}, χ_{−280}, χ_{−420} have rank 2), and
every one of them is non-zero at the known (★)-zeros 5569 and 9601 or at composite zeros — invalid. Even granting a valid
line, positivity at a prime is a single central value L(G ⊗ χ_p, ½), which GRH does not control, which vanishes at
explicit 𝔐-primes for the survivors found, and which CKRS predicts to vanish infinitely often. And for an effective
proxy, validity is (MS) itself; the only non-circular validity (termwise representation recipes) is impossible on the
square class. The half-integral-weight escape E1 is closed on 𝔐 in the ternary-theta class; what remains (coset thetas,
mixed nebentypus, many-φ levels with a validity identity, p-dependent levels) is B2 in other clothes.

## 8. Commands and files
All runs under `ulimit -v 4000000`, `timeout` ≤ 1800, ≤ 2 concurrent processes; Python via `uv run --with cypari2`
(pari 2.17.2).
* `bash scripts/z59_walds_halfint_sweep.sh 10000 4 8 12 20 24 28 40 56 60 84 120 140 168 280 420 > data/z59/walds/halfint_sweep_A.txt`
* `bash scripts/z59_walds_halfint_sweep.sh 8000 16 32 48 80 112 240 336 560 840 > data/z59/walds/halfint_sweep_B.txt`
* the 12 (L, D) runs that crashed in A/B (an indexing bug in the "first non-zero" printout, triggered only when the rank
  was non-zero; fixed) or overflowed (L = 840, D ∈ {1, 8, 21}: cusp space) → `halfint_sweep_C.txt` (`/tmp` driver
  reproduced by: `for p in "168 168 10000 4" … "840 21 8000 1"; do for l0 in 0 11; do uv run … z59_walds_halfint.py $p-fields; done; done`)
* `uv run … scripts/z59_walds_halfint.py 840 105 16000 0 1`, same with 840 → `halfint_840_cusp_B16000.txt`
* `uv run … scripts/z59_walds_identify.py 1680 "-3,-4,-7,-8,-15,-20,-24,-35,-40,-56,-84,-120,-168,-280,-420,-840" 150 1500 > identify_rational_1680.txt`
* `python3 scripts/z59_walds_compare.py identify_rational_1680.txt halfint_sweep_{A,B,C}.txt halfint_840_cusp_B16000.txt > compare_W1.txt`;
  `python3 scripts/z59_walds_sweep_summary.py … > sweep_summary.txt`
* `uv run … scripts/z59_walds_diag.py L D 40000` for the nine survivor pairs → `diag_survivors.txt` (the last pair and
  `diag_168_168.txt` with the prime-vanishing count added later); `uv run … scripts/z59_walds_crosscheck.py > crosscheck_168.txt`
* `uv run … scripts/z59_walds_rank2_search.py` → `rank2_search.txt`; `uv run … scripts/z59_walds_f4.py > f4_screen.txt`
  (summary `f4_summary.txt`; an earlier, slower partial run without `ellrank`: `f4_screen_run1_partial.txt`)
* `python3 scripts/z59_walds_w0check.py 24 20000 > w0check.txt`

## 9. Review log
REVIEW_PLACEHOLDER
