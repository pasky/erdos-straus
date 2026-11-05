# Z59_WALDS — the cusp / Waldspurger residue after TERNARY: odd squares force a *Gaussian-twist* central zero; without such exceptional eigensystems the residue is empty, with them single-twist positivity is conjecturally false, and validity is circular

Status: z59 lane WALDS (brief `z52bbriefs/z59_lanes.md` §WALDS; common rules `z52bbriefs/z58_lanes.md`, `z53_depth.md`).
Internal; internally reviewed only (§9). **ES is OPEN; nothing here proves or disproves ES, (★), (MS) or (MS⁺).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z59_walds_*`,
data `data/z59/walds/` (< 1 MB). Literature notes: `data/z59/walds/lit_verify.md`.

**Verdict: narrowed** (scoped no-go + an exact dictionary; no HOT LEAD). The Waldspurger residue left by TERNARY
cannot carry (MS): (i) T1 kills every Shimura eigensystem on 𝒞₁ except "Gauss-exceptional" ones (Thm W1, PROVED rel.
cited inputs); (ii) at the computed small levels there are none and every T1-valid proxy vanishes on 𝒞₁ (CERTIFIED
finite check, §5); (iii) where they exist, positivity of a single one is a single-twist non-vanishing statement that GRH
does not give and that CKRS's conjecture predicts to fail infinitely often (§4); (iv) *validity* of an effective proxy
is literally (MS) on its class unless it is structural, and structural (termwise representation) validity is
impossible on 𝒞₁ (Lemma W0, Prop W5).

Notation as in `Z58_TERNARY.md`. g ∈ M_{3/2}(Γ₀(4N), ψ) is a *ternary-theta proxy*: g = Σ cᵢθ_{Lᵢ} + h, Lᵢ positive
ternary lattices, h a cusp form, one nebentypus ψ (quadratic; pari/Shimura convention: θ_L has ψ = χ of ℚ(√det L),
checked in §5.1), E = Σcᵢθ_{gen Lᵢ}. 𝒞₁(2N) = {n ≥ 1 : n ∈ ℤ_q^{×2} for every prime q | 2N}; for N with odd prime
divisors in {3,5,7}, 𝒞₁(2N) ⊇ {n : n mod 840 ∈ 𝔐} (TERNARY Cor F1). *Valid* (R-support): g(n) ≠ 0 ⟹ R(n) ≥ 1 for all
n ≡ 1 (4); *effective on a class 𝒞*: g(p) ≠ 0 for all sufficiently large primes p ∈ 𝒞. TERNARY Thm F: if g(ℓ²) = 0 for all
large primes ℓ then E ≡ 0 on 𝒞₁(2N), the t = 1 unary thetas vanish, and g(p) = h⊥(p) at primes p ∈ 𝒞₁(2N).

---

## 0. MANDATORY FALSIFIER TABLE

Mechanism examined: positivity of a valid half-integral-weight proxy at 𝔐-primes coming from its cusp coefficients,
i.e. (Waldspurger) from central values L(½, φ ⊗ ψχ_{−4}χ_p) at the single twist by p.

| screen | behaviour |
|---|---|
| **F1 odd squares** | **This is where the whole residue is decided.** An odd square m² (gcd(m,2N) = 1) lies in 𝒞₁ with squarefree part t = 1, and Waldspurger's twist character at t = 1 is χ₀^{−1} = ψ̄·(−1/·): the twist is **φ ⊗ ψχ_{−4}**, the field ℚ(√−d) for a lattice of determinant d (ℚ(i) for d = 1 — the same field as the C = 1 norm form 4m²+1 = N(1+2mi) of T1; Lemma D(d) of TERNARY uses ℚ(√−C)). Thm W1: T1 at odd squares forces g_φ(1) = 0 for every eigensystem φ, and then g_φ vanishes on all squarefree t ∈ 𝒞₁ unless **L(½, φ ⊗ ψχ_{−4}) = 0** (φ "Gauss-exceptional"). Non-squareness is used exactly here; the odd squares do not just "give square discriminant": they pin the anchor coefficient a(1), and Waldspurger transports a(1) = 0 to the whole square class. |
| **F2 C-even (R₈)** | Everything negative here (W1, W2, W5, Lemma W0) is line-blind and applies verbatim to R₈-support proxies (R₈ also vanishes on odd squares), so nothing false is proved. The only positive statement (Prop W4, dictionary) is conditional on validity, which is the hypothesis; for an R₈-support proxy validity additionally demands L(½, G ⊗ χ_p) = 0 at the 4 in-𝔐 R₈-zero primes (not screened: conductors > 10¹⁴). |
| **F3 composites** | All 18 non-square composite R-zeros in 𝔐 ≤ 10¹⁰ (1969 … 17 401 609) are **squarefree**, hence in 𝒞₁ with their own twist χ_t. They enter exactly like prime zeros (Prop W4); the screen of §6 includes the small ones. Primality is *not* used anywhere in W1/W2/W4 beyond "t squarefree in 𝒞₁": the cusp route sees primes and squarefree composites of 𝒞₁ identically. |
| **F4 known zeros** | Prop W4 (PROVED rel. Waldspurger Cor. 2): a proxy supported on one Gauss-exceptional φ that is non-zero at some squarefree t₀ ∈ 𝒞₁ is **invalid** as soon as L(½, G_φ ⊗ χ_p) ≠ 0 at one R-zero p ∈ 𝒞₁. Screen (§6, EVIDENCE: numerical central values + rigorous `ellrank` lower bounds): for every tested Gauss-exceptional G (7 elliptic curves of rank 2, conductor supported on {2,3,5,7}) some screened zero has rank-0 twist with central value numerically ≈ 0.4–4.7 ⟹ every single-eigensystem proxy built on them is invalid. At the small levels of §5 there is nothing to screen (no Gauss-exceptional φ: the T1-kernel already vanishes on 𝒞₁). |

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

### 3.2 Corollary W2 (no Gauss-exceptional eigensystem ⟹ the residue is empty)

**Corollary W2 (PROVED rel. the same inputs).** If L(½, φ ⊗ ψχ_{−4}) ≠ 0 for every φ with S(4N, ψ, φ) ≠ 0, then every
ternary-theta proxy g ∈ M_{3/2}(Γ₀(4N), ψ) satisfying (T1\*) vanishes at every squarefree n ∈ 𝒞₁(2N) — in particular at
every 𝔐-prime when the odd primes of N lie in {3,5,7}. (Proof: W1(iii) with Φ_exc = ∅.) So at such a level the
"cusp/Waldspurger residue" of TERNARY is not merely unforced: it is identically zero on the class.

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
  W1/W3 make the point sharp: every contributing G_φ *itself* has a double central zero, and §6 exhibits (PROVED via
  `ellrank` + Gross–Zagier–Kolyvagin, see §6) twists G ⊗ χ_p with p ∈ 𝒞₁ prime and L(G ⊗ χ_p, 1) = 0.
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

### 5.2 Results
RESULTS_PLACEHOLDER

## 6. Computations II — Gauss-exceptional eigensystems exist at larger levels; the F4/F3 screen

RESULTS2_PLACEHOLDER

## 7. Verdict, screens, proposed FRONTIER text, bottom line

VERDICT_PLACEHOLDER

## 8. Commands and files
COMMANDS_PLACEHOLDER

## 9. Review log
REVIEW_PLACEHOLDER
