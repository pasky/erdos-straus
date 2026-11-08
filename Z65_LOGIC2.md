# Z65_LOGIC2 — which principle does a proof of ES on Mordell classes need? Verdict: strengthened (logic) / narrowed; no HOT LEAD

Status: z65 lane LOGIC2 (brief `z52bbriefs/z65_lanes.md` §LOGIC2; common rules `z58_lanes.md`, `z53_depth.md`).
**ES is OPEN. Nothing here proves or disproves ES, (MS), (S), or any case of them.** Internal, unrefereed.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z65_logic2_*`,
data `data/z65/logic2/`. Builds on `Z64_UNPROV.md` (cited as **U64**: Thms A, A′, A″, B; Lemmas 2.3, 2.4; §§2.6–2.8;
Prop 6.2) and `Z58_LOGIC.md`. Literature checks: `data/z65/logic2/lit_verify.md` (made by the lane itself; the two
research subagents failed with an expired token).

**Results in one paragraph.** (i) T1 itself, read as an ordered ℕ-sentence, holds in the U64 models, together with
every "positively closed" ℕ-Diophantine non-existence fact (Thm P). So NOI + T1 ⊬ ES_prime on square classes; this
answers U64 §2.8's open item. (ii) A new model (Thm T) adds the two-squares theorem. NOI + GCD + PD + Th_∀(ℤ) + T1 +
"every prime p ≡ 1 (4) is a sum of two squares" does not prove ES (nor ES★) at the primes of any unit-square class, in
particular not (MS). The model has exactly one nonstandard prime, n = β₁² + β₂². (iii) No-go (Prop 4.1): the
present construction family ("polynomial-type" models) cannot be extended to prime-Bezout (residue rings modulo primes
are fields), to reciprocity against standard primes, or to Lagrange. Every polynomial-type model of OI + PB has only
standard primes. (iv) Arc level (§5): those three principles are *square-compatible*; nothing in the T1 transfer
conflicts with them. A natural true principle that *does* kill every arc counter-model is the non-residue certificate
NR (some d ≡ 3 (mod 4), coprime to p, has d | x² + p). At square-mimicking primes every such certificate, and every
(★)-hit, must use a nonstandard modulus (Prop 5.3). Such primes exist in models of true arithmetic (Prop 5.4).
CONDITIONAL on CONV-II-15, the transfer method can only ever refute ES at square-mimicking primes (Prop 5.5).
(v) IE₁, IΔ₀, IΔ₀ + exp: still OPEN. One new constraint: in IΔ₀ + Count₂(Δ₀), which proves QR (Jeřábek Thm 5.7),
square-mimicking primes have residue fields containing √ℓ* for every standard ℓ, so no polynomial-type model exists.
What this tells a proof is in §7.

## 0. Falsifier table (mandatory)

This lane proves non-provability theorems and no-go statements about model constructions. It proposes no positivity
mechanism; the table records how the results interact with the screens.

| screen | behaviour |
|---|---|
| **F1 odd squares** | Every non-provability result is T1 transferred into a model along analytic arcs (U64 §2.3); Thm T lands at Pythagorean odd squares (s² + t²)². New: T1 itself holds in the models (Thm P), so "use T1" is not a principle that helps. NR is singled out because it is *false at every odd square* (Prop 5.1): it is a step "false at n = m²" in the T1 sense, and it kills the transfer. |
| **F2 C-even sub-line** | All model results apply verbatim to R₈ and every (★)-sub-line (subsets of R vanish at squares; Thm P covers the full Type II family too). Nothing distinguishes C odd from C even. No positivity is claimed, so nothing is falsified. |
| **F3 composites** | The counterexamples are *primes* of the models (Thm T: the only nonstandard prime). Prop 5.5 uses the composite data in reverse. Non-square landing values cannot carry a refutation when genuine Type II solutions exist there; CONV-II-15 (CERTIFIED to 10⁸) says they do for all odd non-squares coprime to 15. So the counter-models are confined to square-mimicking primes. |
| **F4 known zeros** | No positivity claimed. The (★)-zero primes cannot serve as landing values for a nonstandard *prime* (a fixed landing value would force ϕ(n) ∈ ℤ, hence n = ϕ(n)·unit reducible; §5 Remark 5.6). |

No HOT LEAD.

## 1. Precise statements

Language L_or = {0, 1, +, −, ·, ≤}. OI, NOI, IOpen, ES(n), ES★(n), Prime(n) (= irreducible, n ≥ 2), Cl_{r,q}(n),
ES_prime[r mod q] and "square-mimicking" are exactly as in U64 §1. Ẑ[i] := Ẑ ⊗ ℤ[i] = ∏_ℓ ℤ_ℓ[i].

Natural axioms considered (all true in ℕ; quantifiers range over the ring, "p prime" is Prime(p)):
* **Bez**: ∀a, b ∃u, v, d (d = ua + vb ∧ d | a ∧ d | b).
* **PB** (prime Bezout: residue rings modulo primes are fields): ∀p ∀a (Prime(p) ∧ p ∤ a → ∃b p | ab − 1). OI + Bez ⊢ PB.
* **TS** (two squares): ∀p (Prime(p) ∧ ∃k p = 4k + 1 → ∃a, b p = a² + b²).
* **E(−1)**: ∀p (Prime(p) ∧ ∃k p = 4k + 1 → ∃x p | x² + 1).
* **QR_std** (reciprocity against standard primes; one axiom per standard odd prime ℓ, with ℓ* := (−1)^{(ℓ−1)/2}ℓ):
  ∀p (Prime(p) ∧ p ≠ ℓ ∧ ∃y, k (p = y² + ℓk) → ∃x p | x² − ℓ*). True in ℕ by quadratic reciprocity.
* **Lag** (Lagrange): ∀x ≥ 0 ∃a, b, c, d x = a² + b² + c² + d².
* **NR** (non-residue certificate): ∀p (Prime(p) ∧ ∃k p = 4k + 1 → ∃d, k′, x, y, u, v (d = 4k′ + 3 ∧ d ≥ 1 ∧
  x² + p = dy ∧ ud + vp = 1)). True in ℕ: for p ≡ 1 (4) take a prime d = q ≡ 3 (4) in the class of a quadratic
  non-residue mod p (Dirichlet). Then (q/p) = −1, so (−p/q) = (−1/q)(p/q) = −(q/p) = 1 by reciprocity.
* **T1★**: ∀u, B, C ≥ 1 ∀s (4uBC − u − B ≠ s²); **T1_II**: ∀a, b, c, d ≥ 1 ∀s (4abcd ≠ a + b + s²c).

**The brief's questions.**
* (1) For T ∈ {OI + Bez, OI + TS, OI + QR, IE₁, IΔ₀, IΔ₀ + exp}: does T prove ES_prime[r mod q] for a primitive
  unit-square class r mod q, e.g. 1 mod 840 (hence (MS))?
* (2) What is the weakest natural axiom the square-mimicking-prime construction cannot accommodate, and what does that
  tell a proof of ES?

**Why not closed.** U64 settled NOI + GCD + PD + Th_∀(ℤ) (ring language). It left open the ordered facts (T1), TS,
QR, Bez/IE₁ and IΔ₀ (U64 §§2.8, 5, 6.2 CONJECTURE, 9 O1–O4). This lane attacks those items.

**Results table (the ladder after z65).**

| theory (added to OI) | ES_prime[unit-square class], (MS) | source |
|---|---|---|
| NOI + GCD + PD + Th_∀(ℤ) | not provable | U64 Thms A, A′, A″ |
| … + T1★ + T1_II + every positively closed ℕ-non-existence fact | **not provable** | Thm P (§2) |
| NOI + GCD + PD + Th_∀(ℤ) + T1 + **TS** | **not provable** | **Thm T (§3)** |
| … + E(−1) | OPEN; not reached by Thm T's model (E(−1) fails there); not excluded for polynomial-type models | §4.4 |
| + **PB** (⇐ Bez ⇐ IE₁) | OPEN; **no polynomial-type model** with a nonstandard prime (Prop 4.1). Bezout models with infinite primes exist (Smith 1993; Mohsenipour 2006, talk abstract) | §§4, 6 |
| + **QR_std** | OPEN; no polynomial-type model with a square-mimicking prime (Prop 4.2) | §4 |
| + **Lag** | OPEN; no polynomial-type model at all (Prop 4.3) | §4 |
| + **NR** | OPEN; kills *every* arc counter-model (Prop 5.1) | §5 |
| IE₁ / IΔ₀ / IΔ₀ + Count₂(Δ₀) / IΔ₀ + exp | OPEN (no computable nonstandard models of IE₁, Wilmers) | §6 |

## 2. Theorem P: ordered universal facts that hold in the U64 models

Throughout, "a U64-type model" is M_ϕ := {g ∈ ℚ[β] : ϕ(g) ∈ Ẑ}. Here β = (β₁, β₂, …) are Berarducci–Otero's
algebraically independent elements with their order (U64 §2.1), and ϕ: ℚ[β] → 𝔸_f is the ring homomorphism with
ϕ(β_i) = a_i for an arbitrary sequence a ∈ Ẑ^ℕ. U64 §§2.1, 2.7 show M_ϕ ⊨ NOI for every such a (BO's proof uses ϕ only
through Lemmas 2.7, 2.8, 2.10). U64 Lemma 2.3(a),(b) supplies, for every b ∈ ℤ^k, an analytic arc ψ on an interval
I ⊃ [0, ∞) with ψ(g)(0) = g(b) and ψ(g) eventually of the M-sign of g (g ≠ 0).

**Definition.** A finite system Σ(x̄, ȳ) of polynomial equations over ℤ, with "positive" variables x̄ = (x₁..x_k)
and free variables ȳ, is *positively closed* if every point of V_Σ(ℝ) that is a limit of points of V_Σ(ℝ) with
x̄ ∈ (0, ∞)^k itself has x̄ ∈ (0, ∞)^k.

**Lemma 2.1 (positivity propagation; PROVED).** Let Σ be positively closed and γ: [0, ∞) → V_Σ(ℝ) continuous, with
x̄(γ(s)) ∈ (0, ∞)^k for all large s. Then x̄(γ(s)) ∈ (0, ∞)^k for all s ≥ 0.
*Proof.* S := {s ≥ 0 : x̄(γ(s)) > 0} is nonempty and open in [0, ∞). It is closed by positive closedness. [0, ∞) is
connected. ∎

**Theorem P (PROVED, relative to U64 §2.1 (M_ϕ ⊨ NOI), U64 Lemma 2.3 and (F4)).** If Σ is positively closed and has
no integer solution with x̄ ≥ 1, then every U64-type model satisfies ∀x̄ ≥ 1 ∀ȳ ¬Σ(x̄, ȳ).
*Proof.* Suppose X̄, Ȳ ∈ M_ϕ solve Σ with X_i ≥ 1; all lie in ℚ[β₁..β_K].
* By U64 (F4) there is D such that X̄(b), Ȳ(b) ∈ ℤ for every b ∈ ℤ^K with b ≡ a (mod D). Fix such a b.
* Lemma 2.3 gives ψ. Since ψ is a ring homomorphism, γ(s) := (ψX̄(s), ψȲ(s)) ∈ V_Σ(ℝ), and ψX_i is eventually positive.
* By Lemma 2.1, X̄(b) = x̄(γ(0)) > 0. So X̄(b) is a positive integer solution, a contradiction. ∎

**Lemma 2.2 (the two T1 systems are positively closed; PROVED).**
* (a) Σ★: 4uBC − u − B − σ = 0 with positive (u, B, C) is positively closed *over σ ≥ 0*, i.e. for limits of points
  with σ ≥ 0. In particular Σ_T1: 4uBC − u − B = s² (free s) is positively closed.
* (b) Σ_II: 4abcd − a − b − s²c = 0 with positive (a, b, c, d) and free s is positively closed.
*Proof.* (a) Take points (u_j, B_j, C_j, σ_j) → (u*, B*, C*, σ*) with u_j, B_j, C_j > 0 and σ_j ≥ 0. Then
4u_jB_jC_j ≥ u_j + B_j.
* Dividing by u_jB_j gives 4C_j ≥ 1/u_j + 1/B_j. C_j → C* < ∞, so u* > 0 and B* > 0.
* Then 4u_jB_jC_j ≥ u_j + B_j → u* + B* > 0 with u*B* < ∞, so C* > 0.

(b) 4a_jb_jc_jd_j = a_j + b_j + s_j²c_j ≥ a_j + b_j.
* Dividing by a_jb_j gives 4c_jd_j ≥ 1/a_j + 1/b_j, so a*, b* > 0.
* Then 4a_jb_jc_jd_j ≥ a_j + b_j → a* + b* > 0 forces c*d* > 0. ∎

The integer facts: R(m²) = 0 for every m ≥ 1 (Z57_SYNTH Lemma A.1(b) is stated "for every m": an element of H_d is a
unit with Jacobi symbol −1, while m² mod d is either a non-unit or has symbol +1). For m = 0, 4uBC − u − B ≥
u(2B − 1) + B(2u − 1) > 0. N_II(m²) = 0 for every m ≥ 1 (Z57_BFII Prop 2.2 / Cor 2.3, as quoted in Z58_WILDCARD §0
F1), and 4abcd > a + b for m = 0.
*Kill test K3 (CERTIFIED, `scripts/z65_logic2_t1all.c 3000` → `data/z65/logic2/t1all_3000.txt`).* Sieving all
2.7·10⁸ triples with 4uBC − u − B ≤ 9·10⁶ marks no square m², 1 ≤ m ≤ 3000, odd or even.

**Corollary P.1 (PROVED, same reliance plus Z57_SYNTH Lemma A.1(b), Z57_BFII Prop 2.2).** Every U64-type model
satisfies T1★ and T1_II. Hence **NOI + GCD + PD + Th_∀(ℤ) + T1★ + T1_II ⊬ ES_prime[r mod q]** for every primitive
unit-square class r mod q. (Use the models of U64 Thm A′; they are U64-type.) This answers U64 §2.8's "OPEN: whether
the non-negative part of M_ϕ satisfies … T1". The T1 obstruction is *already true* in the counter-models. A proof
that uses T1, or Jacobi reciprocity only to prove T1-type non-existence facts, gains nothing.

*Remarks.*
* *What Thm P does not cover.* Systems that are not positively closed, e.g. homogeneous ones such as x³ + y³ = z³,
  whose positive real points accumulate at the boundary. Their ring-language forms are covered by U64 A″ instead.
  Whether M_ϕ satisfies the whole universal theory of (ℤ, ≤) is OPEN. The obstruction is Diophantine approximation:
  sign conditions can define thin horns around the curve Γ that contain no lattice points.
* *ES(1) suffices for (MS) (PROVED; simplification of U64 Thm A).* For the class 1 mod 840 take q* = 1. The U64
  proof can land at ℓ = 1, i.e. at b₁ = 1 ≡ q* (mod D). There the transferred solution solves 4/1 = 1/x + 1/y + 1/z
  in positive integers, which is impossible since the right side is ≤ 3. So NOI ⊬ (MS) is "4 > 3" transported along
  an arc; ET Prop 1.6 is needed only for q* ≠ 1.

## 3. Theorem T: the two-squares theorem does not help

**Theorem T (PROVED, relative to U64 §2.1/§2.7 (M_ϕ ⊨ NOI for every ϕ), U64 Lemmas 2.3–2.4, (F4), the GCD argument of
U64 §2.7, ET Prop 1.6, Lang–Weil, Chebotarev, and Noether's reduction theorem for absolute irreducibility).** Let r mod q
be a primitive unit-square class. There is a model M ⊨ NOI + GCD + PD + Th_∀(ℤ) + T1★ + T1_II + **TS** containing an
infinite prime n ≡ r (mod q) with M ⊨ ¬ES(n) ∧ ¬ES★(n). Moreover n = β₁² + β₂² is the only nonstandard positive prime
of M. Hence
> **NOI + GCD + PD + Th_∀(ℤ) + T1 + TS ⊬ ES_prime[r mod q]** (and ⊬ ES★_prime[r mod q]); in particular ⊬ (MS), (MS★).

### 3.1 Construction
* *Residue law μ.* Fix w_q ∈ ((ℤ/q)[i])^× with N(w_q)² ≡ r (mod q). It exists: write r ≡ c² with c a unit. The norm
  ℤ_ℓ[i]^× → ℤ_ℓ^× is onto for odd ℓ, and onto {x ≡ 1 (4)} for ℓ = 2, so N(w) ≡ ±c is solvable. Take a = (a_i) ∈
  Ẑ^ℕ random, with ℓ-components independent across primes ℓ. At each ℓ:
  * (a_{1,ℓ}, a_{2,ℓ}) is Haar-distributed on ℤ_ℓ², conditioned on a₁ + ia₂ ∈ (ℤ_ℓ[i]^×)² and, if ℓ | q, on
    a₁ + ia₂ ≡ w_q² (mod ℓ^{v_ℓ(q)});
  * a_{j,ℓ} (j ≥ 3) is Haar on ℤ_ℓ.
  Every conditioning event is open and of positive measure, so μ is a probability measure.
* M := M_ϕ for ϕ(β_i) = a_i, and n := β₁² + β₂². In M, n > 0 because β₁ ≠ 0.

**Lemma 3.1 (PROVED).** ϕ(n) = N(w)², where w := √(a₁ + ia₂) ∈ Ẑ[i]^×. So ϕ(n) ∈ (Ẑ^×)² (n is square-mimicking) and
n ≡ r (mod q). n is irreducible in ℚ[β], since over ℚ(i) its factors β₁ ± iβ₂ are not rational. As ϕ(n) is a unit,
n is prime in M (U64 (F1)), and divisibility by n in M is divisibility in ℚ[β] (U64 (F3)).

**Lemma 3.2 (only nonstandard prime; PROVED, μ-almost surely).** Every irreducible element of M is ±ℓ for a standard
prime ℓ, or ±n.
*Proof.*
* (Reduction.) Let g ∈ M be irreducible and nonconstant. If ℓ | ϕ(g) for some standard ℓ then g = ℓ·(g/ℓ) with
  g/ℓ ∈ M a non-unit, which is impossible; so ϕ(g) ∈ Ẑ^×.
  * If g = g₁g₂ in ℚ[β] with both factors nonconstant, then ϕ(g_i) ∈ 𝔸_f^× (componentwise units at almost all ℓ, and
    the product is a unit). Pick c_i ∈ ℚ^× with ϕ(c_ig_i) ∈ Ẑ^×. Then g = (c₁c₂)⁻¹(c₁g₁)(c₂g₂), and (c₁c₂)⁻¹ ∈
    ℚ ∩ Ẑ^× = {±1}, so g is reducible in M. Contradiction.
  * So g = c·f with f ∈ ℤ[β] irreducible over ℚ (and primitive) and c ∈ ℚ^×, and ϕ(f) ∈ 𝔸_f^×; that is, ℓ ∤ f(a_ℓ)
    for almost all ℓ.
* (Claim.) For every f ∈ ℤ[β₁..β_k] irreducible over ℚ and not associate to n, Σ_ℓ P_μ(ℓ | f(a_ℓ)) = ∞.
  * Put F(s, t, z₃..z_k) := f(s² − t², 2st, z₃..z_k).
  * For odd ℓ ∤ q, (a₁, a₂) mod ℓ is uniform on S_ℓ := {(s² − t², 2st) : s² + t² ≢ 0}. Hensel applies because
    ℤ_ℓ[i] is étale over ℤ_ℓ, and w ↦ w² is 2-to-1 on 𝔽_ℓ[i]^×. Also |S_ℓ| ≤ ℓ²/2. Hence
    P(ℓ | f(a_ℓ)) ≥ #{(s, t, z) ∈ 𝔽_ℓ^k : s² + t² ≠ 0, F ≡ 0}/ℓ^k.
  * F has an irreducible factor F₁ not dividing s² + t². Otherwise F = c(s² + t²)^e. Then f involves only β₁, β₂, and
    since ℚ[β₁, β₂] → ℚ[s, t] is injective with n ↦ (s² + t²)², and s² + t² ∉ ℚ[s² − t², 2st] (degree-2 part),
    e is even and f = c·n^{e/2}. Irreducibility then gives f ~ n, a contradiction.
  * Let G₁ be an absolutely irreducible factor of F₁ over a number field L. G₁ is not associate to s ± it: otherwise
    the product of its conjugates, F₁, would be ~ s² + t².
  * For the primes ℓ splitting completely in L(i), which have positive density by Chebotarev, all but finitely many
    reductions G₁ mod 𝔓 stay absolutely irreducible of the same degree (Noether) and are not ~ s ± ιt.
  * Lang–Weil gives #V(G₁)(𝔽_ℓ) = ℓ^{k−1} + O(ℓ^{k−3/2}) and #V(G₁, s² + t²)(𝔽_ℓ) = O(ℓ^{k−2}). So the probability is
    ≥ 1/(2ℓ) for those ℓ, and Σ 1/ℓ over a set of positive density diverges.
* (Conclusion.) The events {ℓ | f(a_ℓ)} are independent across ℓ. By Borel–Cantelli II, almost surely
  ℓ | f(a_ℓ) for infinitely many ℓ, so ϕ(f) ∉ 𝔸_f^×. There are countably many f. So almost surely every nonstandard
  irreducible is c·f with f ~ n, i.e. g = c′n with c′ ∈ ℚ ∩ Ẑ^× = {±1}. ∎
*Kill test K2 (CERTIFIED for the stated range; `scripts/z65_logic2_onlyprime.py 200` →
`data/z65/logic2/onlyprime_200.txt`).* For 11 test polynomials f ≠ n, the exact value ℓ·P(ℓ | f(a)) averages
0.78–2.06 on the half of the primes where the claim needs it (e.g. ℓ ≡ 1 (4) for β₁² + β₂² + 1). For f = n it is 0.

**Lemma 3.3 (GCD and PD; PROVED, μ-almost surely).** M is a GCD domain and every element ≥ 2 has an irreducible
divisor.
*Proof.*
* *GCD.* U64 §2.7 uses only (G1) (the ℓ-components (a_{j,ℓ})_j are algebraically independent over ℚ) and (G2)
  (coprime f, g have ℓ | f(a_ℓ), g(a_ℓ) for only finitely many ℓ).
  * The law of (a₁, a₂) has density ≤ 2ℓ²/(ℓ − 1)² ≤ 4.5 with respect to Haar measure on ℤ_ℓ² (ℓ ≥ 3), so (G1)
    holds.
  * (G2) follows from the point-count lemma of U64 §2.7 with the constant 3 replaced by 4.5.
* *PD.* Let g ≥ 2. If ϕ(g) ∉ Ẑ^×, a standard prime divides g. Otherwise, by the factorisation step of Lemma 3.2,
  g = ±n^e with e ≥ 1, so n | g. ∎

**Lemma 3.4 (TS holds; E(−1), PB, QR_std, cofinality fail; PROVED, μ-a.s.).**
* M ⊨ TS. By Lemma 3.2 the positive primes are the standard primes and n. A standard prime ℓ ≡ 1 (4) is a sum of
  two standard squares, and n = β₁² + β₂² with β₁, β₂ ∈ M (ϕ(β_i) ∈ Ẑ). Also gcd(β₁, β₂) = 1 in M: a common divisor
  is a constant k ∈ ℤ with k | a₁, a₂, and then k² | N(a₁ + ia₂), a unit.
* M ⊭ E(−1) at n. If n | x² + 1 in M, then x̄² = −1 in ℚ[β]/(n) = A[β₃, …], with A := ℚ[β₁, β₂]/(n). Such an x̄ is
  algebraic over ℚ, so by degree it lies in A. A is a graded domain (n is homogeneous), and the top homogeneous
  component of x̄ squares to 0 unless it has degree 0, so x̄ ∈ A₀ = ℚ. That is impossible.
* M ⊭ PB and M ⊭ QR_std, by Props 4.1 and 4.2 below. Primes are not cofinal.

**Lemma 3.5 (landing points with coprimality; PROVED).** Let D be a multiple of 8q and Y ∈ ℚ[β₁..β_k] with n ∤ Y.
Then there are infinitely many b ∈ ℤ^k with the following properties:
* b ≡ a (mod D);
* b₁ = s² − t², b₂ = 2st with gcd(s, t) = 1, and ℓ := s² + t² is odd and coprime to D, so n(b) = ℓ²;
* gcd(Y(b), ℓ) = 1, and the same holds simultaneously for finitely many such Y.

*Proof.*
* (i) Choose b′ = (b₃..b_k) ≡ a′ (mod D) such that Y′ := Y(β₁, β₂, b′) ∉ nℚ[β₁, β₂]. This is possible: the image of Y
  in A[β₃..β_k] is a nonzero polynomial over the domain A ⊇ ℚ, so it does not vanish on the product of infinite sets
  a′ + Dℤ^{k−2}.
* (ii) G(T) := Y′(−2T, −2iT) ∈ ℚ(i)[T] is nonzero. Otherwise β₁ + iβ₂ divides Y′ (Y′ vanishes on β₂ = iβ₁); by
  conjugation so does β₁ − iβ₂, hence n | Y′.
* (iii) Choose s₀, t₀ with (s₀ + it₀)² ≡ a₁ + ia₂ (mod D) (reduce w); s₀² + t₀² is a unit mod D. Pick t ≡ t₀ (mod D)
  with G(t²) ≠ 0 (all but finitely many t). Let P be the set of primes dividing D, a denominator of Y′, or the
  numerator of N_{ℚ(i)/ℚ}(G(t²)). By CRT choose s ≡ s₀ (mod D) and, for primes r ∉ D:
  * s ≡ 1 (mod r) if r | t;
  * s ≡ 0 (mod r) if r ∈ P and r ∤ t.

  Then gcd(s, t) = 1 and gcd(s² + t², r) = 1 for all r ∈ P.
* (iv) Let r | ℓ be prime. Then r ∉ P, r ∤ st, r ≡ 1 (4), and a prime 𝔯 | r of ℤ[i] divides s + it or s − it. In the
  first case s ≡ −it (mod 𝔯) gives b₁ ≡ −2t² and b₂ ≡ −2it², so Y(b) = Y′(b₁, b₂) ≡ G(t²) (mod 𝔯); in the second case
  Y(b) ≡ Ḡ(t²) (mod 𝔯). So r | Y(b) would give r | N(G(t²)), i.e. r ∈ P, a contradiction.

For finitely many Y, take the product of the G's in (iii). ∎

*Kill test K1 (CERTIFIED for the tested inputs; `scripts/z65_logic2_landing.py 200 6565` →
`data/z65/logic2/landing_check.txt`).* 7 polynomials Y × 4 moduli D × 200 random targets: all landings satisfy the
residue, parity, gcd(s, t) and gcd(Y(b), ℓ) claims. Negative control: without the P-avoidance step, 33–121 of ≈ 3 900
landings have gcd(Y(b), ℓ) > 1 for Y = β₁ + 3, β₁β₂ + 13, β₁² − β₂² + 7β₁β₂ − 3.

### 3.2 Proof of Theorem T
NOI holds by U64 §2.1. GCD, PD and TS hold by Lemmas 3.3–3.4, Th_∀(ℤ) by U64 Thm A″ (any ϕ), and T1★, T1_II by Cor
P.1. n ≡ r (mod q) by Lemma 3.1.

*¬ES(n).* Suppose X, Y, Z ∈ M, all ≥ 1, satisfy 4XYZ = n(XY + YZ + ZX).
* *Type split.* n is prime in the UFD ℚ[β], so it divides one of X, Y, Z, but not all three: X/n, Y/n, Z/n ≥ 1 would
  give 4 ≤ 3, exactly as in U64 §2.5.
* *Type I* (n | X, n ∤ Y, Z). Put X₁ := X/n ∈ M and take D from (F4) for {X, Y, Z, X₁}, a multiple of 8q.
  * Lemma 3.5 (for Y and Z) gives b ≡ a (mod D) with n(b) = ℓ², ℓ odd, and gcd(Y(b)Z(b), ℓ) = 1. Also
    X(b) = ℓ²X₁(b), and all values are integers.
  * *The arc.* Take U64's arc for b, with the second coordinate perturbed:
    ψ(B₂)(s) := p₂(T + s) + π₂ + (b₂ − π₂ − p₂(T))e^{−s} + λs·e^{−s}.
    * The extra term vanishes at s = 0 and is O((1 + s)e^{−s}), so U64 Lemma 2.3(a),(b) hold verbatim.
    * ψ(β₁) ≢ 0 has finitely many zeros s₁..s_m on (0, ∞): it is analytic and eventually nonzero.
    * Choose λ with ψ(β₂)(s_j) ≠ 0 for all j. Each s_j excludes one λ, since the coefficient s_je^{−s_j} ≠ 0, and
      ψ(β₁) does not depend on λ.
    * Then ψ(n) = ψ(β₁)² + ψ(β₂)² > 0 on (0, ∞), and ψ(n)(0) = ℓ² > 0.
  * U64 Lemma 2.4 makes x₀ := X(b), y₀ := Y(b), z₀ := Z(b) positive integers with 4/ℓ² = 1/x₀ + 1/y₀ + 1/z₀,
    ℓ² | x₀ and gcd(ℓ², y₀z₀) = 1. That is a Type I solution for the odd square ℓ², contradicting ET Prop 1.6.
* *Type II* (n | Y, Z, n ∤ X). The same argument, with Lemma 3.5 applied to X and with Y/n, Z/n added to the (F4)
  set, contradicts f_II(ℓ²) = 0.

*¬ES★(n).* Suppose u, B, C ∈ M, all ≥ 1, satisfy 4uBC − u − B = n.
* Take D from (F4) and any b from Lemma 3.5 (no coprimality is needed).
* The unperturbed arc has ψ(n) = ψ(β₁)² + ψ(β₂)² ≥ 0. Apply Lemma 2.1 with Σ★, which is positively closed over σ ≥ 0
  (Lemma 2.2(a)), to γ = (ψu, ψB, ψC, ψn).
* So u(b), B(b), C(b) ≥ 1 with 4uBC − u − B = ℓ², contradicting R(ℓ²) = 0. ∎

*Remarks.*
* *What TS costs.* TS is satisfied cheaply here: the model has a single nonstandard prime, and that prime is a sum of
  two squares by design. A model of TS + "primes are cofinal" would need an infinite designed family, e.g.
  n_m = β₁² + γ_m² with γ_m := β₂^m(β₂ − β₃)² + β_{m+3}, each γ_m a coordinate, together with a family version of
  Lemma 3.2. **CONJECTURE (sketch only, not proved):** this works and gives NOI + GCD + TS + cofinal primes ⊬
  ES_prime on square classes.
* *Prior art.* Otero, *Quadratic forms in normal open induction* (JSL 58 (1993); abstract VERIFIED,
  `lit_verify.md` §2) embeds M[x, y] with x² + by² = a into a model of NOI, except in trivial cases. So TS-type
  witnesses can be added to *arbitrary* NOI models. That embedding gives no control of ES at n, which is why Thm T
  builds the representation into the generator system instead.
* *Two-squares proofs and the T1 transfer.* TS is true at odd squares (m² = m² + 0²). Its witness relation does not
  obstruct arcs, and Thm T confirms this at the level of models.
