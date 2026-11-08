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
particular not (MS). The model has exactly one nonstandard prime, n = β₁² + β₂². (iii) No-go (Props 4.1–4.3): the
present construction family ("polynomial-type" models) cannot satisfy Bezout at all (Prop 4.1′). Its models of OI + PB
(prime-Bezout: residue rings modulo primes are fields) have only standard primes. It cannot satisfy reciprocity against
standard primes at square-mimicking primes, nor Lagrange. (iv) Arc level (§5): the witness relations of these
principles have integer points at suitable odd squares (Prop 5.2). Whether arc models of them exist is OPEN. A natural
true principle that *does* kill every arc counter-model is the non-residue certificate NR (some d ≡ 3 (mod 4), coprime
to p, has d | x² + p). At square-mimicking primes every such certificate, and every (★)-hit, must use a nonstandard
modulus (Prop 5.3). Such primes exist in models of true arithmetic (Prop 5.4). (v) **Exact dichotomy (Thm D,
PROVED; found by the internal review).** For every primitive class r mod q, NOI proves ES at all large primes of the
class ⟺ IOpen proves ES on the whole class ⟺ the class is a finite union of ET Prop 1.9 family classes ⟺ its
profinite closure misses the closed set U of unit profiles covered by no family class. The square classes meet U (ET
Prop 1.6). CONJECTURE, with EVIDENCE from a covering tree to level 3·10¹³: U also contains non-squares. For example
the non-square class {n ≡ 1 (mod 840), (n/11) = −1} meets U, which would make ES on it NOI-unprovable as well.
(vi) IE₁, IΔ₀, IΔ₀ + exp: still OPEN. One new constraint: IΔ₀ + Count₂(Δ₀) proves QR (Jeřábek Thm 5.7) and Lagrange
(Jeřábek p. 20). So at square-mimicking primes its residue fields contain √ℓ* for every standard ℓ. What this tells a
proof is in §7 (Assessment).

## 0. Falsifier table (mandatory)

This lane proves non-provability theorems and no-go statements about model constructions. It proposes no positivity
mechanism; the table records how the results interact with the screens.

| screen | behaviour |
|---|---|
| **F1 odd squares** | Every non-provability result at square classes is T1 transferred into a model along analytic arcs (U64 §2.3); Thm T lands at Pythagorean odd squares (s² + t²)². New: T1 itself holds in the models (Thm P), so "use T1" is not a principle that helps. NR's *witness relation* has no integer point at any perfect square (Prop 5.1); it is a step "false at n = m²" in the T1 sense and kills the transfer. Thm D shows that the general obstruction is Mordell–Schinzel non-solvability by polynomials; T1 (ET Prop 1.6) is why squares are non-solvable. |
| **F2 C-even sub-line** | All model results apply verbatim to R₈ and every (★)-sub-line (subsets of R vanish at squares; Thm P covers the full Type II family too). Nothing distinguishes C odd from C even. No positivity is claimed, so nothing is falsified. |
| **F3 composites** | The counterexamples are *primes* of the models (Thm T: the only nonstandard prime). Pointwise landing at non-square integers cannot refute Type II solutions when CONV-II-15 holds (Remark 5.5′). The refutations that do exist at non-square profiles (if U ⊋ squares, CONJECTURE) come from polynomial non-solvability along whole progressions, not from composite zeros (Thm D). |
| **F4 known zeros** | No positivity claimed. The (★)-zero primes cannot be the profile of a nonstandard *prime*. If ϕ(n) = N₀ ∈ ℤ with |N₀| > 1, every standard prime factor of N₀ divides n in M, so n is not prime (Remark 5.6). |

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
| + **PB** (⇐ Bez ⇐ IE₁) | OPEN. Bez fails in *every* polynomial-type model (Prop 4.1′), and polynomial-type models of PB have no nonstandard prime (Prop 4.1). Bezout models with infinite primes exist (Smith 1993; Mohsenipour 2006, talk abstract) | §§4, 6 |
| + **QR_std** | OPEN; no polynomial-type model with a square-mimicking prime (Prop 4.2) | §4 |
| + **Lag** | OPEN; no polynomial-type model at all (Prop 4.3) | §4 |
| + **NR** | OPEN; kills *every* arc counter-model (Prop 5.1) | §5 |
| IE₁ / IΔ₀ / IΔ₀ + Count₂(Δ₀) / IΔ₀ + exp | OPEN (no computable nonstandard models of IE₁, Wilmers) | §6 |

| theory | ES on a primitive class r mod q (any class, square or not) | source |
|---|---|---|
| IOpen / NOI (tail form, n ≥ N₀) | provable ⟺ r mod q is a finite union of ET Prop 1.9 family classes ⟺ (r + qẐ) ∩ U = ∅ | **Thm D (§5)** |
| same, non-square classes | CONJECTURE: some non-square classes are unprovable, e.g. {1 mod 840, (n/11) = −1} (covering tree alive to level 3·10¹³, EVIDENCE) | §5.6 |

## 2. Theorem P: ordered universal facts that hold in the U64 models

Throughout, "a U64-type model" is M_ϕ := {g ∈ ℚ[β] : ϕ(g) ∈ Ẑ}. Here β = (β₁, β₂, …) are Berarducci–Otero's
algebraically independent elements with their order (U64 §2.1), and ϕ: ℚ[β] → 𝔸_f is the ring homomorphism with
ϕ(β_i) = a_i for an arbitrary sequence a ∈ Ẑ^ℕ. U64 §§2.1, 2.7 show M_ϕ ⊨ NOI for every such a (BO's proof uses ϕ only
through Lemmas 2.7, 2.8 and the ϕ-independent Lemmas 2.3, 2.6, 2.9; the lane re-read BO's proof of Thm 4.2: Lemma
2.10 is used only for primality, Thm 4.3). U64 Lemma 2.3(a),(b) supplies, for every b ∈ ℤ^k, an analytic arc ψ on an interval
I ⊃ [0, ∞) with ψ(g)(0) = g(b) and ψ(g) eventually of the M-sign of g (g ≠ 0).

**Definition.** A finite system Σ(x̄, ȳ) of polynomial equations over ℤ, with "positive" variables x̄ = (x₁..x_k)
and free variables ȳ, is *positively closed* if every point of V_Σ(ℝ) that is a limit of points of V_Σ(ℝ) with
x̄ ∈ (0, ∞)^k itself has x̄ ∈ (0, ∞)^k. More generally, for a closed set C ⊆ ℝ^{x̄,ȳ}, Σ is *positively closed
over C* if the same holds for limits of points of V_Σ(ℝ) ∩ C.

**Lemma 2.1 (positivity propagation; PROVED).** Let Σ be positively closed over a closed set C, and let
γ: [0, ∞) → V_Σ(ℝ) ∩ C be continuous, with x̄(γ(s)) ∈ (0, ∞)^k for all large s. Then x̄(γ(s)) ∈ (0, ∞)^k for
all s ≥ 0. (C = everything gives the plain notion.)
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
u(2B − 1) + B(2u − 1) > 0. N_II(m²) = 0 for every m ≥ 1: Z57_BFII Prop 2.2 / Cor 2.3 are stated for odd m, but
the proof extends verbatim. Take a solution 4abcd = a + b + nc and f := 4acd − 1 (so 4acd ≡ 1 (mod f)).
* a, c, d are units mod f, and bf = a + nc gives n ≡ −ac⁻¹ ≡ −4a²d (mod f).
* So (n/f) = (−d/f) = −(d/f) = −1, since f ≡ −1 (mod 4d) and Jacobi reciprocity give (d/f) = 1, as in Lemma A.1(b).
* For n = m², n is a unit mod f, so (n/f) = +1, a contradiction.

For m = 0, 4abcd > a + b.
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
* *ES(1) suffices for NOI ⊬ (MS) (PROVED; simplification of U64 Thm A in the model M_{q*}).* For the class 1 mod 840
  take q* = 1. The U64 proof can land at b = (1, 1, …, 1). There the transferred solution solves 4/1 = 1/x + 1/y + 1/z
  in positive integers, which is impossible since the right side is ≤ 3. In the (★)/Hit form in which (MS) is
  stated, it gives 4uBC − u − B = 1, impossible since R(1) = 0 (the left side is ≥ 2).
  * So NOI ⊬ (MS) is "4 > 3" transported along an arc.
  * This applies to U64 Thm A at q* = 1. It does not apply to Thm A′ or Thm T, whose generic residues forbid landing
    at 1; there ET Prop 1.6 is needed.

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
  * For odd ℓ ∤ q, (a₁, a₂) mod ℓ is uniform on S_ℓ := {(s² − t², 2st) : s² + t² ≢ 0}; Hensel applies because
    ℤ_ℓ[i] is étale over ℤ_ℓ. The squaring map w ↦ w² on 𝔽_ℓ[i]^× has fibres of constant size κ (κ = 2 for
    ℓ ≡ 3 (4), κ = 4 for ℓ ≡ 1 (4), where 𝔽_ℓ[i] ≅ 𝔽_ℓ × 𝔽_ℓ), and κ·|S_ℓ| = |𝔽_ℓ[i]^×| ≤ ℓ². Hence
    P(ℓ | f(a_ℓ)) = #{(s, t, z) ∈ 𝔽_ℓ^k : s² + t² ≠ 0, F ≡ 0}/(|𝔽_ℓ[i]^×|·ℓ^{k−2}) ≥ #{…}/ℓ^k.
  * F has an irreducible factor F₁ not dividing s² + t². Otherwise F = c(s² + t²)^e, and f involves only β₁, β₂.
    * Put u = s + it, v = s − it. Then ℚ(i)[s² − t², 2st] = ℚ(i)[u², v²] and s² + t² = uv, so (uv)^e lies in
      the image of ℚ[β₁, β₂] only for e even.
    * The map ℚ[β₁, β₂] → ℚ[s, t] is injective with n ↦ (uv)², so f = c·n^{e/2}.
    * Irreducibility then gives f ~ n, a contradiction.
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
  * The law of (a₁, a₂) has density ℓ²/|S_ℓ| ≤ 4ℓ²/(ℓ − 1)² ≤ 6.25 with respect to Haar measure on ℤ_ℓ²
    (ℓ ≥ 5 odd, ℓ ∤ q), and a bounded density at the finitely many ℓ | 6q. So (G1) holds: null sets stay null.
  * (G2) follows from the point-count lemma of U64 §2.7 with the constant 3 replaced by 6.25 (resp. the finite
    constants at ℓ | 6q).
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
  `lit_verify.md` §2) embeds M[x, y] with x² + by² = a into a model of NOI, except in trivial cases. So a single
  element can be given a representation x² + by² in an NOI extension. A TS model would need an ω-chain of such
  extensions, which may create new primes or destroy ES-failure. Thm T builds the representation into the generator
  system instead.
* *Two-squares proofs and the T1 transfer.* TS is true at odd squares (m² = m² + 0²). Its witness relation does not
  obstruct arcs, and Thm T confirms this at the level of models.

## 4. No-go: what the polynomial construction cannot accommodate

**Definition 4.0.** A *polynomial-type model* is a nonstandard M ⊨ OI with a ring embedding M ⊂ ℚ[β_i : i ∈ I]
(algebraically independent indeterminates) such that every g ∈ ℚ[β] has a multiple kg ∈ M, k ∈ ℤ_{≥1}. Every
U64-type model and the model of Thm T qualify: ϕ(g) ∈ D⁻¹Ẑ for some D, so Dg ∈ M.

**Lemma 4.0 (PROVED).**
* (a) M ∩ ℚ = ℤ, so nonstandard elements are nonconstant polynomials.
* (b) |I| ≥ 2.

*Proof.*
* (a) M is discrete and contains ℤ.
* (b) Suppose M ⊂ ℚ[β₁]. Some element G(β₁) of M is infinite, so β₁ is infinite (a polynomial in a bounded element is
  bounded). Hence a polynomial of higher degree is larger in absolute value. Take c = ±kβ₁ ∈ M with c > 0.
* By Shepherdson's criterion (U64 §1) some g ∈ M has g² ≤ c < (g + 1)², i.e. 0 ≤ c − g² < 2g + 1.
  * If deg g ≥ 1, then c − g² ≠ 0 has degree 2 deg g > deg(2g + 1), which contradicts the bound.
  * If deg g = 0, then c ≤ (g + 1)² is bounded, a contradiction. ∎

**Proposition 4.1 (PB; PROVED).** Let M be polynomial-type and p ∈ M nonstandard. Then M ⊭ "∀a (p ∤ a → ∃b
p | ab − 1)". Consequently **every polynomial-type model of OI + PB (a fortiori of OI + Bez) has only standard primes**,
and so cannot refute ES_prime on any class at a nonstandard element.
*Proof.*
* F := ℚ[β]/(p) is not a field.
  * If some β_j does not occur in p, then F = A[β_j, …] with A ≠ 0, and β̄_j is a nonzero non-unit.
  * Otherwise I is finite with |I| ≥ 2 (Lemma 4.0), and by Krull's principal ideal theorem (p) has height 1 < |I|, so
    it is not maximal.
* Suppose PB held at p. Let a ∈ M with ā ≠ 0 in F. Then p ∤ a in ℚ[β], so p ∤ a in M, and PB gives b with
  ab − 1 ∈ pM, i.e. āb̄ = 1 in F.
* Every element of F has the form k⁻¹ā with a ∈ M, so F would be a field. Contradiction. ∎

**Proposition 4.1′ (Bez; PROVED; from the internal review, extending U64 §2.6).** No polynomial-type model satisfies
Bez.
*Proof.*
* Take k, k′ ≥ 1 with g := kβ₁, h := k′β₂ ∈ M. A common divisor of g and h in M divides both in ℚ[β], so it is a
  constant, an integer (Lemma 4.0(a)).
* A Bezout identity ug + vh = d with d | g, d | h would make d a nonzero integer. But ug + vh has no constant term, so
  it is never a nonzero constant. ∎

**Proposition 4.2 (QR_std; PROVED).** Let M be polynomial-type and M ⊨ QR_std. Then every nonstandard prime n of M is a
nonzero square modulo only finitely many standard primes. In particular **no polynomial-type model of OI + QR_std has a
square-mimicking nonstandard prime**.
*Proof.*
* Suppose n is a nonzero square mod ℓ for infinitely many odd ℓ. QR_std gives x_ℓ ∈ M with n | x_ℓ² − ℓ*.
* Let h be an irreducible factor of n in ℚ[β] and K := ℚ[β]/(h), a domain. Then ℓ* is a square in K for infinitely
  many ℓ, so the algebraic closure of ℚ in K contains ℚ(√ℓ* : those ℓ), which has infinite degree.
* But K = A[β_j : j ∉ J] with A = ℚ[β_J]/(h) a finitely generated domain (J := the variables of h). Elements of K
  algebraic over ℚ lie in A (degree argument). The algebraic closure of ℚ in the finitely generated field Frac(A) is
  finite over ℚ. Contradiction. ∎

*Remark (where QR_std holds).* By Jeřábek's Theorem 5.7 (MLQ 56 (2010); author PDF read, `lit_verify.md` §1),
IΔ₀ + Count₂(Δ₀) proves quadratic reciprocity with the supplementary laws for all odd primes of the model, with the
Legendre symbol *defined* by squareness. So it proves QR_std. In every model of IΔ₀ + Count₂(Δ₀), the residue field
M/nM at a square-mimicking prime n therefore contains √ℓ* for every standard ℓ: its algebraic part is infinite.
* Jeřábek also remarks, directly after Thm 5.7 (p. 20; found by the internal review), that Berarducci–Intrigila's proof
  of Lagrange needs only multiplicativity, so IΔ₀ + Count₂(Δ₀) proves Lag.
* IΔ₀ ⊢ IE₁ ⊢ Bez already rules out polynomial-type models altogether (Prop 4.1′), and Lag does too (Prop 4.3).
* Prop 4.2 is an independent obstacle for any future non-polynomial construction.

**Proposition 4.3 (Lag; PROVED).** No polynomial-type model satisfies Lag, nor "every x ≥ 0 is a sum of k squares"
for any standard k.
*Proof.* ±kβ₁ ∈ M has total degree 1. A sum of squares of real polynomials of maximal degree δ ≥ 1 has degree 2δ:
its top form is a nonzero sum of squares of real forms. It cannot have degree 1. ∎

**4.4 E(−1) (OPEN for polynomial-type models).** Prop 4.2's argument allows finitely many square roots, so E(−1) is
not excluded.
* A polynomial-type model of E(−1) needs every nonstandard prime h to have i ∈ ℚ[β]/(h). For example n = A² + B² with
  (A, B) unimodular in ℚ[β], such as n = β₁² + (1 + β₁β₂)², where i = AB⁻¹ mod n.
* Thm T's proof then needs landing points b ≡ a (mod D) on {A² + B² = □} with the Lemma 3.5 coprimality. For
  (A, B) = (β₁, 1 + β₁β₂) these are Pythagorean pairs (x, B) with x | B − 1, which looks like a thin, Vieta-type set.
* Whether some unimodular (A, B) has profinitely dense square points is OPEN. So is NOI + TS + E(−1) ⊬ ES_prime.

## 5. Arc level: which principles a counter-model can survive, and which kill it

U64 Prop 6.2 (the arc criterion) concerns *odd-square arcs* at n. For each finite G ⊂ M there is a ring
homomorphism ψ: ℤ[G ∪ {n}] → C^ω(I) with:
* ψ(g)(0) ∈ ℤ;
* ψ(g) eventually of the M-sign of g;
* ψ(n) > 0 on [0, ∞), ψ(n)(0) = m² with m odd;
* the gcd condition for g with n ∤ g.

All results of U64 and §3 are proved by exhibiting such arcs.

**Proposition 5.1 (NR kills every arc; PROVED).** Let M ⊨ OI, n ∈ M with n > 0, and suppose M ⊨ "∃d, k′, x, y, u, v
(d = 4k′ + 3 ∧ d ≥ 1 ∧ x² + n = dy ∧ ud + vn = 1)". If G contains these witnesses, there is no ring homomorphism ψ as
above with ψ(n) > 0 on [0, ∞) and ψ(n)(0) a perfect square (of any parity). In particular **no model of OI + NR is an
arc counter-model** at any n ≡ 1 (4) it regards as prime.
*Proof.*
* ψ(d)ψ(y) = ψ(x)² + ψ(n) > 0 on [0, ∞). So ψ(d) never vanishes, and it is eventually positive, so d₀ := ψ(d)(0) ≥ 1
  with d₀ ≡ 3 (4).
* Pick a prime r ≡ 3 (4) dividing d₀. From u₀d₀ + v₀m² = 1, r ∤ m. Then x₀² ≡ −m² (mod r) makes −1 a square mod r,
  which is impossible. ∎

The same argument applies to any principle whose existential witnesses at n form a system with no integer solution at
n = m² (with the positivity transferred, as above).
* *Examples.* ES★ (by T1), the full Type II existence N_II ≥ 1 (by T1_II), and NR.
* *Negative Pell* ("every prime p ≡ 1 (4) has x² − py² = −1"; Legendre; example from the internal review): at n = m²,
  x₀² − m²y₀² = −1 forces m = 1. So it kills every arc whose landing values are not 1, i.e. every arc counter-model at a
  profile ϕ(n) ≠ 1, but not those at ϕ(n) = 1.
* NR is singled out only by this: it kills arcs at every profile, 1 included, and it is weaker than ES★.
* The Z64 statement (S) uses Jacobi symbols. It is not an existential polynomial system, so arcs do not apply to it
  directly. It is Δ₀-expressible over IΔ₀ (Jeřábek Thm 5.8), whose natural extension IΔ₀ + Count₂(Δ₀) proves the
  Jacobi laws.

**Proposition 5.2 (square-compatibility of PB, TS, E(−1), QR_std, Lag; PROVED, elementary).** Fix D ≥ 1 and a finite
set L of standard odd primes. Let m be any product of primes r ≡ 1 (mod 8∏_{ℓ∈L} ℓ) with m ≡ 1 (mod D); by Dirichlet
there are infinitely many. (This is the landing pattern for the profile ϕ(n) = 1. For a general square-mimicking
profile take m² ≡ ϕ(n) (mod D), with prime factors ≡ 1 (mod 8∏_{ℓ∈L, ℓ∤D} ℓ) and the caveat below for ℓ | D.
TS, E(−1), PB and Lag need only prime factors ≡ 1 (4).) Then at n := m² every instance (with integer parameters) of
the following has an integer witness:
* PB, for a coprime to m;
* TS (m² = m² + 0²);
* E(−1) (every prime of m is ≡ 1 (4));
* QR_std for ℓ ∈ L (every prime of m splits in ℚ(√ℓ*));
* Lag.

So none of these witness relations has an integer obstruction at the landing squares. Whether arcs exist *jointly*
with the other elements of a model of these axioms (Bezout coefficients interpolated along arcs, etc.) is O1′, which
is OPEN. **Assessment:** the obstacles of §4 are plausibly artefacts of the polynomial realisation rather than T1
conflicts, but this is not proved.

*Caveat (PROVED).* For QR_std with ℓ | D, the landing m must be a quadratic residue mod ℓ (all prime factors of m
split in ℚ(√ℓ*)). So ϕ(n) ≡ m² must be a fourth power mod ℓ for ℓ ≡ 1 (4). Square-mimicking residues that are also
fourth-power-mimicking at the odd primes, e.g. ϕ(n) = 1 for the class 1 mod 840, satisfy this. QR_std therefore
constrains *which* square-mimicking residues arc models can use, but not (MS).

**Proposition 5.3 (at square-mimicking n the certificates are nonstandard; PROVED).** Let M be a discretely ordered
ring with division with remainder by standard integers (e.g. M ⊨ IOpen). Let n ∈ M, and suppose that for every standard
d ≥ 1 there is a standard s, coprime to d, with n ≡ s² (mod d). Then:
* (a) every (★)-hit of n has nonstandard modulus: if u, B, C ∈ M are ≥ 1 with 4uBC − u − B = n, then d := 4uC − 1 is
  nonstandard;
* (b) every NR-witness d of n is nonstandard;
* (c) every Type II witness f = 4acd − 1 of N_II at n (4abcd = a + b + nc) is nonstandard.

*Proof.*
* (a) If d is standard, then 1 ≤ u ≤ (d + 1)/4 is standard and n ≡ −u (mod d) with u | (d + 1)/4. Then s² ≡ −u
  (mod d) in ℤ with gcd(s, d) = 1, but −u has Jacobi symbol −1 and s² has +1 (Z57_SYNTH Lemma A.1(b)). Contradiction.
* (b) Reduce x mod d to a standard x₀. Then x₀² ≡ −s² (mod d), so −1 is a square mod d ≡ 3 (4), d ≥ 3, which is
  impossible.
* (c) As in (a), with Z57_BFII's Jacobi lemma for the Type II witness classes (every witness f has (n/f) = −1). ∎

**Proposition 5.4 (square-mimicking primes exist in models of true arithmetic; PROVED).** For every primitive
unit-square class r mod q there is N ≻ ℕ (so N ⊨ Th(ℕ) ⊇ PA) containing a nonstandard prime n ≡ r (mod q) that is
square-mimicking in the sense of Prop 5.3.
*Proof.* Consider the type {Prime(x)} ∪ {x > k : k ∈ ℕ} ∪ {x ≡ r (mod q)} ∪ {∃s < d (gcd(s, d) = 1 ∧ x ≡ s² (mod d)) :
d ∈ ℕ}.
* Each finite part asks for a prime above some k₀ in a class c mod L := lcm(q, d₁, …), with c a unit square ≡ r
  (mod q). Take c := s′² with s′ ≡ s (mod q) and s′ coprime to L.
* Dirichlet's theorem supplies such primes.
* Compactness, over the elementary diagram of ℕ, realises the type. ∎

So any theory T ⊆ Th(ℕ) that proves ES_prime[r mod q] proves ES at primes all of whose standard-modulus information is
that of a square. There, every (★)-hit, NR-witness and Type II witness is nonstandard (Prop 5.3).

### 5.5 The exact dichotomy (Thm D)

The draft of this memo claimed here, CONDITIONAL on CONV-II-15, that arc refutations live only at square-mimicking
primes. The internal review showed that this inference is invalid. Arcs can also transfer a hypothetical solution
along a whole progression and contradict *polynomial non-solvability*; pointwise solvability at the landing integers
does not prevent that. The correct statement is the following, and it is PROVED.

**Proposition 5.5 (polynomial criterion; PROVED, relative to U64 (F1), (F4), Lemmas 2.3–2.4 and ET Prop 1.9; supplied
by the internal review).** Let M_ϕ be a U64-type model, n := β₁ and π := ϕ(β₁) ∈ Ẑ^×. Then M_ϕ ⊨ ES(n) ⟺ π lies
in some primitive class r mod D that is solvable by polynomials ⟺ π lies in some ET Prop 1.9 family class.
*Proof.*
* (⇐) Let P₁, P₂, P₃ be the polynomials of the class.
  * Each P_i(r + Dk) is integer-valued for all large k, hence for all k ∈ ℤ (Newton basis), hence P_i(r + Dκ) ∈ Ẑ
    for κ ∈ Ẑ by continuity. So ϕ(P_i(β₁)) = P_i(π) ∈ Ẑ and P_i(β₁) ∈ M_ϕ.
  * The leading coefficients are positive and β₁ is positive infinite, so P_i(β₁) ≥ 1.
  * The identity 4P₁P₂P₃ = t(P₁P₂ + P₂P₃ + P₃P₁) in ℚ[t] gives ES(β₁).
* (⇒) Let X, Y, Z ∈ M_ϕ, all ≥ 1, solve ES(β₁); all lie in ℚ[β₁..β_K]. Take D from (F4), fix b′ ≡ a′ (mod D),
  and put P_X(t) := X(t, b′), and similarly P_Y, P_Z.
  * For integers t ≥ 1 with t ≡ π (mod D), (F4) gives P_X(t) ∈ ℤ.
  * U64 Lemma 2.3 (b₁ = t ≥ 1, so ψ(β₁) > 0 on [0, ∞)) and Lemma 2.4 give P_X(t), P_Y(t), P_Z(t) ≥ 1.
  * The identity 4P_XP_YP_Z = t(P_XP_Y + P_YP_Z + P_ZP_X) holds in ℚ[t].
  * So the primitive class π mod D is solvable by polynomials.
* (Families.) ET Prop 1.9: every solvable class has all its large primes in finitely many family classes. By
  Dirichlet, its unit profiles then lie in their union; otherwise a clopen subclass outside the union would contain
  infinitely many primes. Conversely, every family class is solvable (ET, loc. cit.). ∎

Define the closed set **U := {π ∈ Ẑ^× : π lies in no ET Prop 1.9 family class}**. ET Prop 1.6 (Mordell–Schinzel) gives
(Ẑ^×)² ⊆ U. Mordell's covering (U64 Cor C, re-run by `scripts/z65_logic2_cover.py 840 nonsq`: 186/186 non-square
classes mod 840 covered, 0/6 squares) gives U ⊆ {π : π mod 840 ∈ 𝔐}.

**Theorem D (exact dichotomy for all moduli; PROVED, relative to Prop 5.5, U64 Thm B and ET Prop 1.9).** For a
primitive class r mod q, with K_{r,q} := (r + qẐ) ∩ Ẑ^× (compact), the following are equivalent:
* (i) K_{r,q} ∩ U = ∅;
* (ii) for some L with q | L, every primitive class s mod L with s ≡ r (mod q) is solvable by polynomials;
* (iii) IOpen ⊢ ∀n ≥ N₀ (Prime(n) ∧ Cl_{r,q}(n) → ES(n)) for some numeral N₀;
* (iv) NOI ⊢ ∀n ≥ N₀ (Prime(n) ∧ Cl_{r,q}(n) → ES(n)) for some numeral N₀.

*Proof.*
* (i)⇒(ii): K_{r,q} is compact and covered by the open family classes, so finitely many suffice. Refine to a common
  modulus L: a subclass of a solvable class is solvable (substitute n = s + Lk).
* (ii)⇒(iii): A prime n > L of the class is coprime to L, so it lies in one of the finitely many solvable classes.
  Thm B (tail form) applies to each.
* (iii)⇒(iv) is trivial.
* (iv)⇒(i): If π ∈ K_{r,q} ∩ U, take M_ϕ with ϕ(β_i) := π for all i. Then β₁ is an infinite prime ≡ r (mod q)
  (U64 (F1), (F2)) with ¬ES(β₁) (Prop 5.5). ∎

*Reading.*
* Thm D generalises U64 Cor C from modulus 840 to every modulus. Open induction proves ES on exactly the classes that
  polynomial identities cover. The obstruction is Mordell–Schinzel non-solvability, and T1 (ET Prop 1.6) is the reason
  why squares are non-solvable.
* (MS) is the case r = 1, q = 840, which meets U at π = 1.
* Whether non-square classes can meet U is question Q_U below.


*Remark 5.5′ (pointwise landing; the old Prop 5.5, rescoped).* If π ∉ (Ẑ^×)², some D₀ makes every positive integer
N ≡ π (mod D₀) an odd non-square coprime to 105 (PROVED; D₀ := 210ℓ^e or 1680, where π is a non-square mod ℓ^e or
mod 8). CONDITIONAL on CONV-II-15 (CERTIFIED to 10⁸ in `Z58_WILDCARD.md`), every such N has a genuine Type II
solution. So a refutation that contradicts the absence of solutions *at a single landing integer* cannot work at
non-square profiles. Refutations along whole progressions (Prop 5.5) are not affected.

*Remark 5.6 (fixed landing values; PROVED).* If π = N₀ ∈ ℤ with |N₀| > 1, then every prime ℓ | N₀ divides n in M,
since n ≡ N₀ (mod ℓ). So n is not prime. Hence the CERTIFIED prime zeros of R, e.g. 8 813 281 ≡ 1 (mod 840), cannot be
the profile of a nonstandard prime. "Pseudo-zero primes" (the prime analogue of Z58 Thm 6.2) do not exist, and for
primes only the profinite *limits* of zeros matter.

### 5.6 Question Q_U: is U = (Ẑ^×)²? (CONJECTURE: no; EVIDENCE)
* *Why it matters (PROVED, from Thm D).* If U = (Ẑ^×)², NOI-provability of ES on a primitive class is decided exactly
  by whether the class contains a unit square, at every modulus. If U ⊋ (Ẑ^×)², some non-square classes are
  NOI-unprovable too, by polynomial non-solvability rather than T1.
* *Probe.* Take K := {n ≡ 1 (mod 840), (n/11) = −1}, a non-square class mod 9240. By König's lemma, K ∩ U ≠ ∅ iff
  the tree of residue classes of K that are uncovered at level Q is infinite along a cofinal chain of levels. Coverage at
  level Q uses all family classes whose modulus divides Q.
* *Implementations.* `scripts/z65_logic2_covertree.py` (sparse refinement tree) and `scripts/z65_logic2_cover.py` (dense
  marking) agree on every common level (2, 6, 18, 81 uncovered at Q = 9240, ·13, ·13·17, ·13·17·19).
* *Data (CERTIFIED for the stated levels; `data/z65/logic2/covertree.txt`, `covertree_deep.txt`, `covertree_powers.txt`,
  `cover_probe.txt`).*
  * Squarefree chain 9240·13·17·19·23·29·31·37 (final level 3.0·10¹³; `covertree_deep.txt`): open nodes
    2 → 6 → 18 → 81 → 444 → 2 842 → 21 785 → **191 017**. The surviving fraction of children is 0.25, 0.19, 0.25,
    0.25, 0.23, 0.26, 0.24: stable at ≈ 1/4, while the branching p − 1 grows.
  * Chain with prime powers (·13, ·3, ·17, ·2, ·5, ·19; final level 1.16·10⁹): 2 → 6 → 5 → 13 → 18 → 57 → **163**.
  * Between 19 % and 28 % of the children of an open node stay uncovered when a new prime is added. So the uncovered
    fraction of K falls (0.4, 0.1, 0.019, 0.0047, 0.0012, …) while the *number* of open nodes grows about ×3–9 per
    prime.
  * Controls (`cover_controls.txt`):
    * unit squares mod 840, 9240, 120120 and 360360: 0 % covered, as Mordell–Schinzel requires (this also checks the
      encoding of the families);
    * non-squares mod 840: 186/186 covered (Mordell);
    * non-squares mod 9240: 1886/1890 covered.
* **CONJECTURE (Q_U negative).** K ∩ U ≠ ∅, so U ⊋ (Ẑ^×)², and NOI ⊬ "ES at all large primes ≡ 1 (mod 840) that
  are non-residues mod 11" (Thm D).
  * EVIDENCE: the growing tree above.
  * *Heuristic (Assessment).* Adversarially chosen square components at the new primes meet only O((log ℓ)²) active
    family constraints per prime ℓ, against ≍ ℓ available residues.
  * Not proved. Higher prime powers and larger primes add family classes at every level, and finite levels cannot
    certify an infinite branch.

## 6. The ladder: IE₁, IΔ₀, IΔ₀ + exp (status and constraints)

| theory | proves (verified where cited) | consequence for ES_prime[square class] |
|---|---|---|
| OI + Bez | models with infinite primes exist: Smith, J. Algebra 159 (1993), "an open induction domain can be a principal ideal domain different from Z" (abstract snippet, PARTLY); a computable Bezout model with cofinal primes is announced by Mohsenipour (2006 talk abstract, VERIFIED abstract) | OPEN. Not polynomial-type (Prop 4.1′). No integer obstruction at the landing squares (Prop 5.2). The next step is to test arcs in the Smith/Mohsenipour chain models (O1′) |
| IE₁ | ⊢ IOpen + Bez (Smith 1992, U64); no computable nonstandard model (Wilmers 1985, as reported by Mohsenipour) | OPEN; any counter-model is non-computable and not polynomial-type |
| IΔ₀ | ⊢ IE₁; Jacobi symbol Δ₀-definable (Jeřábek Thm 5.8) | OPEN |
| IΔ₀ + Count₂(Δ₀) | QR + supplementary laws + Jacobi laws for all moduli (Jeřábek Thms 5.7, 5.8, VERIFIED) | OPEN; QR_std holds, so residue fields at square-mimicking primes contain all √ℓ* (Prop 4.2 Remark); Lag holds too (Jeřábek p. 20) |
| IΔ₀ + WPHP(Δ₀) | Lagrange (Berarducci–Intrigila 1991); infinitely many primes (Paris–Wilkie–Woods 1988) (both as reported by Jeřábek, PARTLY) | OPEN; Lag holds, so no polynomial-type model (Prop 4.3) |
| IΔ₀ + exp | PNT (Cornaros–Dimitracopoulos 1994, as reported by Jeřábek, PARTLY); FLT/Euler's criterion are proved in S²₂ + iWPHP(PV) + PHP(PV) (Jeřábek Thms 4.2, 4.7); that theory is contained in IΔ₀ + exp (standard, Assessment) | OPEN. **Whether IΔ₀ + exp ⊢ NR is OPEN** (needs Dirichlet for the nonstandard modulus 4p or genus theory for discriminant −4p; nothing found in the literature; expected yes, Assessment). If it does, every model of IΔ₀ + exp is an arc non-model (Prop 5.1). Note that OI already proves NR on non-square classes such as p ≡ 5 (8) (d = (p + 1)/2, x = 1, y = 2, 2d − p = 1) or p ≡ 2 (3) (d = 3); only square-mimicking-type classes carry content |
| PA | NR (Dirichlet's theorem; standard formalisation, Assessment) | every model of PA is an arc non-model; independence of ES from PA is not a target (U64 §4) |

*Partial provability (Assessment, with a proof sketch, not claimed as PROVED).* Define the Jacobi-level non-residue
certificate **JNR**: for every prime p ≡ 1 (4) there is d ≡ 3 (mod 4), 3 ≤ d < 4p, with Jacobi (p/d) = −1. It is a
Π₁ sentence ∀p θ(p) with θ a Δ₀ formula over IΔ₀ (Jeřábek Thm 5.8), and θ is false at every odd square, since (m²/d) ∈ {0, 1}. Sketch of a proof in
IΔ₀ + Count₂(Δ₀) + (an injective weak pigeonhole principle for Δ₀ maps 2a → a):
* the least-square-root map [1, p − 1] → [1, (p − 1)/2] would be injective if every unit were a square, so a quadratic
  non-residue a exists;
* take d ≡ a (mod p), d ≡ 3 (mod 4), d < 4p;
* Jacobi reciprocity (Thm 5.8) gives (p/d) = (d/p) = (a/p) = −1.

The exact form of WPHP needed was not checked against PWW or Berarducci–Intrigila. **If this sketch is right, the
Jacobi-level certificate of non-squareness at a nonstandard modulus is cheap.** The certificates that a proof of ES
needs are *shaped* ones: −p ≡ x² (NR), or −p ∈ H_d ((★)-hit, i.e. B2). The partial result found is therefore exactly
the part that is not hard.

## 7. Answer to brief (2): what the construction cannot accommodate, and what a proof must use (Assessment, except where marked PROVED)

* **Against the present (polynomial-type) construction (PROVED: Props 4.1, 4.1′, 4.2, 4.3).**
  * Bez fails in every polynomial-type model.
  * Polynomial-type models of OI + PB ("modulo every prime, every non-multiple is invertible") have no nonstandard
    prime at all.
  * QR_std fails at every square-mimicking prime, and Lag fails always.
  * Of the Bezout-type axioms examined, PB is the weakest that the construction excludes. It is a single Π₂ sentence,
    implied by Bez and IE₁. QR_std and Lag are excluded as well, and they are incomparable with PB as far as we know.
    No minimality claim is made.
  * Accommodated: TS (Thm T), and GCD, PD, normality, Th_∀(ℤ) and T1 (U64, Thm P). E(−1) is OPEN (§4.4).
* **Against arc-type constructions.**
  * PROVED: the witness relations of PB, TS, E(−1), QR_std and Lag have integer points at suitable odd squares
    (Prop 5.2).
  * Whether arc models of these axioms exist is OPEN (O1′). The Assessment is that §4's obstacles are artefacts of
    the polynomial realisation.
  * A natural true principle that defeats *every* arc counter-model is NR, a square-root certificate of
    non-residuosity at some d ≡ 3 (mod 4) (Prop 5.1, PROVED); it is true in ℕ by Dirichlet. Negative Pell kills
    every arc counter-model except those at the profile 1. Whether some weaker natural principle does the job is not
    known.
* **What the obstruction is (PROVED: Thm D).** At the level of open induction the obstruction is exactly
  Mordell–Schinzel: a class is NOI-provable at large primes iff polynomial identities cover it. T1 is why the square
  classes are not covered. Whether other classes escape is Q_U (CONJECTURE: some do).
* **What a proof of ES on Mordell classes must use.**
  * PROVED (Props 5.3–5.4): it must handle nonstandard primes whose every standard residue is that of a square; such
    primes exist in models of true arithmetic. There every (★)-hit, NR-witness and Type II witness has a
    *nonstandard modulus*.
  * PROVED (U64 Thms A/A′/A″, Thms P, T, D): none of the following suffice, alone or together:
    * identities, residues and polynomial covering (Thm D);
    * Euclidean division, gcds, irreducible divisors, normality;
    * all universal ring facts about ℤ, all positively closed ℕ-non-existence facts (T1 included), and the
      two-squares theorem.
  * Assessment. Every (★) or Type II solution *is* a non-residue certificate of a specific shape (Z57_SYNTH
    Lemma A.1, Z57_BFII Prop 2.2), so "a proof must produce shaped certificates" restates "a proof must produce
    solutions". The non-tautological content is the nonstandard modulus (Prop 5.3), together with the cost ladder:
    * Jacobi-level certificates are plausibly cheap (IΔ₀ + counting, §6 sketch);
    * square-root certificates (NR) need Dirichlet or genus theory at the nonstandard discriminant −4p (OPEN in weak
      theories);
    * divisor-shaped certificates are B2.

    The logic ladder thus puts the missing step where the analytic campaign puts it: from "(p/d) = −1 for some d" to
    "−p ≡ k (mod d) with k | (d + 1)/4 for some d".

## 8. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: strengthened (logic) / narrowed (model-construction side).** No bearing on the truth of ES; no HOT LEAD.

What was proved:
* **Thm P / Cor P.1.** Positively closed ℕ-non-existence facts, T1★ and T1_II included, hold in every U64-type model.
  So NOI + GCD + PD + Th_∀(ℤ) + T1 ⊬ ES_prime[square class]. This closes U64 §2.8's OPEN item.
* **Thm T.** NOI + GCD + PD + Th_∀(ℤ) + T1 + TS ⊬ ES_prime[square class], ES★_prime, (MS). This answers brief (1)
  for TS: unprovable.
* **Thm D + Prop 5.5** (Prop 5.5's proof was supplied by the internal review). In U64-type models ES(β₁) holds iff
  ϕ(β₁) lies in a polynomially solvable class. NOI (equivalently IOpen) proves ES at the large primes of a class r mod q
  iff the class is covered by finitely many ET Prop 1.9 family classes, i.e. iff its closure misses U. This is U64
  Cor C for every modulus.
* **Props 4.1, 4.1′, 4.2, 4.3.** Polynomial-type models never satisfy Bez; their models of PB have no nonstandard
  primes; they fail QR_std at square-mimicking primes; they fail Lag.
* **Props 5.1–5.4, Remarks 5.5′–5.6.**
  * NR kills every arc counter-model, and negative Pell kills those at profiles ≠ 1.
  * The witness relations of PB, TS, E(−1), QR_std and Lag have integer points at suitable odd squares.
  * At square-mimicking primes the hit/NR/Type II moduli are nonstandard, and such primes exist in models of Th(ℕ).
  * Primes cannot have an integer profile.
* Simplification: in U64's M_{q*} with q* = 1, NOI ⊬ (MS) is "4 > 3" (R(1) = 0) at n = 1 (§2 Remark).

What was computed:
* K1–K3 kill tests: passed.
* ET Prop 1.9 covering tree for the non-square class {1 mod 840, (n/11) = −1}: CERTIFIED to level 3·10¹³ (squarefree
  chain; 191 017 open nodes) and 1.2·10⁹ (with prime powers; 163), two implementations on common levels; still alive. EVIDENCE for the CONJECTURE U ⊋ (Ẑ^×)².

What stays open: OI + Bez, + QR, IE₁, IΔ₀, IΔ₀ + exp (each with the constraints of §6); E(−1); TS + cofinal primes;
Q_U.

**Hard screens (FRONTIER §4).**
* *T1 squares.* Built in: every square-class model result is T1 transported. New:
  * T1 holds in the models (Thm P);
  * NR, which kills the transport, is a "step false at squares" (Prop 5.1);
  * Thm D shows that the general obstruction is polynomial non-solvability, with squares as the known instance.
* *8/131, numerator 8.* All model results apply verbatim to R₈ and every (★)-sub-line, and Thm P covers the full Type II
  family. Nothing separates C odd from C even; nothing is falsified.
* *Tied modulus (B2).* Not moved. §§6–7 locate B2 on the logic ladder as the step from a Jacobi certificate to a shaped
  certificate at a nonstandard modulus (Assessment).
* *Fixed p.* Not applicable: no positivity is claimed.

**Proposed FRONTIER text** (do not edit FRONTIER here).
* §3, extend the B1-formal entry:
  > *(z65 LOGIC2.)*
  > (i) T1 itself holds in the U64 counter-models, since every positively closed ℕ-non-existence fact transfers along
  > arcs. So NOI + T1 ⊬ ES_prime[square class].
  > (ii) The two-squares theorem does not help: NOI + GCD + PD + Th_∀(ℤ) + T1 + "every prime ≡ 1 (4) is a sum of two
  > squares" ⊬ ES_prime[square class], (MS) (`Z65_LOGIC2.md` Thm T; the model's only nonstandard prime is
  > n = β₁² + β₂²).
  > (iii) Exact dichotomy (Thm D): NOI/IOpen prove ES at the large primes of a class iff ET's Prop 1.9 families cover
  > it finitely, iff its profinite closure misses the closed set U of uncovered unit profiles. This is U64 Cor C at
  > every modulus. U contains the unit squares. CONJECTURE (EVIDENCE: covering tree alive to level 3·10¹³ with ≈ 1/4 survival per prime) that U contains
  > non-squares, e.g. some profile ≡ 1 (mod 840) that is a non-residue mod 11.
  > (iv) The polynomial construction cannot reach Bezout, prime-Bezout, reciprocity against standard primes or
  > Lagrange (Props 4.1–4.3). Their witness relations have integer points at odd squares; arc models of them are OPEN.
  > NR, "−p is a square modulo some d ≡ 3 (4) coprime to p", kills every arc counter-model (Prop 5.1).
  > (v) At square-mimicking primes, which exist in models of true arithmetic, every (★)-hit and NR-witness has a
  > nonstandard modulus (Prop 5.3).
  > Open: OI + Bez, IE₁, IΔ₀(+exp), E(−1), Q_U.

**Bottom line.**
* Brief (1), answered as far as it goes. Adding the two-squares theorem, and T1 itself, to normal open induction with
  gcds still does not prove ES on any square class (Thms P, T).
* Open induction proves ES on a class exactly when polynomial identities cover it (Thm D). Whether non-square classes
  can escape is the new concrete question Q_U. The data suggest yes.
* Bezout, reciprocity and Lagrange cannot be added *by this construction* (Props 4.1–4.3). Their witness relations do
  not conflict with landing at odd squares (Prop 5.2), so their status, and that of IE₁, IΔ₀ and IΔ₀ + exp, stays
  OPEN. Bezout models with infinite primes exist in the literature (Smith 1993; Mohsenipour 2006), so O1 is now a
  concrete question about those models.
* Brief (2), as an Assessment:
  * PB (prime-Bezout) is the weakest Bezout-type axiom examined that the present construction excludes. QR_std and
    Lag are incomparable further exclusions.
  * NR is a natural true principle that excludes every arc construction.
  * At the level of open induction the exact obstruction is polynomial non-coverage (Thm D).
* The message for a proof is the T1 slogan made formal. At primes whose every standard residue is a square, which exist
  in models of true arithmetic, a proof must work at nonstandard moduli (PROVED). The cheap Jacobi-level non-squareness
  is not the issue (Assessment); the shaped, divisor-level certificate is B2.
* No progress on ES itself.

## 9. Open problems (precise)
* **O1′** Do the Smith (1993) / Mohsenipour (2006) Bezout models of OI admit odd-square arcs at some infinite prime
  of a square class (U64 Prop 6.2)? If yes, OI + Bez ⊬ ES_prime[square class]. The full constructions were not
  accessible here (`lit_verify.md` §§3–4).
* **O2′** A polynomial-type model of NOI + TS + E(−1) with ¬ES at a square-class prime (§4.4). It needs a unimodular
  pair (A, B) whose square points A² + B² = □ are profinitely dense.
* **O3′** TS + cofinal primes (§3.2 Remark, CONJECTURE).
* **O4′** IΔ₀ + exp ⊢ NR? (Dirichlet / genus theory for nonstandard discriminants in weak arithmetic.)
* **O5′** A formal proof of JNR in IΔ₀ + Count₂(Δ₀) + WPHP(Δ₀) (§6 sketch), with the exact WPHP form.
* **O6′** Does M_ϕ satisfy the whole universal theory of (ℤ, ≤)? (§2 Remark: thin horns.)
* **O7′ (Q_U)** Is U = (Ẑ^×)²? Concretely: is {n ≡ 1 (mod 840), (n/11) = −1} covered by finitely many ET Prop 1.9
  family classes? This generalises U64 O3; by Thm D it decides NOI-provability of ES at the large primes of that
  class. The (★)-analogue (★-solvable classes) is open likewise.

## 10. Review log and replay

**Internal hostile review** (`data/z65/logic2/internal_review.md`; Opus nested side agent; it reran all three scripts
byte-identically and made independent checks). Verdict: **no FATAL issue, 2 MAJOR, 22 MINOR, all applied.**
* **(M1)** Prop 5.5(b) ("arc refutations only at square-mimicking primes, CONDITIONAL on CONV-II-15") was an invalid
  inference. Refutations can contradict polynomial non-solvability along whole progressions.
  * Replaced by Prop 5.5 (polynomial criterion, PROVED; the proof was supplied by the reviewer) and Thm D.
  * The old statement survives as Remark 5.5′ (pointwise landing only).
  * The covering question became Q_U (§5.6). The lane then ran the covering-tree probe; this was new work after the
    review.
* **(M2)** The superlatives "weakest axiom …" and "nothing in the transfer conflicts" were unproved.
  * They are now labelled Assessment and scoped to "among the axioms examined".
  * Prop 4.1′ (Bez fails in every polynomial-type model) was added.
  * The negative-Pell example was added.
* **(m1–m3)** Lemma 3.2: fibre size 4 for ℓ ≡ 1 (4); the bound kept. The even-e argument via u = s + it, v = s − it.
* **(m2)** Lemma 3.3 density constant 6.25.
* **(m4, m5)** Lemma 2.1 and the definition were relativised to a closed set C.
* **(m6)** T1_II for even m: proof added in §2.
* **(m7, m8)** Prop 4.1′ is cited for "no polynomial-type model of IΔ₀".
* **(m9)** (S) wording.
* **(m10)** The ES(1) remark is scoped to M_{q*}, with R(1) = 0.
* **(m11)** JNR as a Π₁ sentence.
* **(m12)** NR is OI-provable on non-square classes such as p ≡ 5 (8) and p ≡ 2 (3).
* **(m13)** Theory containment note.
* **(m14)** Otero remark weakened.
* **(m15)** Lagrange in IΔ₀ + Count₂(Δ₀) (Jeřábek p. 20).
* **(m16)** Prop 5.2 for general profiles.
* **(m17, m18)** D₀ with 105; moot after M1.
* **(m19, m20)** F4/F1 wording.
* **(m21)** Replay of the negative control: the reviewer's independent snippet is in the review file (Check 1; 29/118/37/0).
  The lane's numbers (33/121/37 with seed 2) are recorded in `landing_check.txt`.
* **(m22)** The "shaped certificate" tautology is acknowledged in §7.

A cross-model review will follow.

**Replay** (each under `ulimit -v 4000000`, `timeout 1800`):
```
gcc -O2 -o /tmp/z65t1all scripts/z65_logic2_t1all.c && /tmp/z65t1all 3000        # = data/z65/logic2/t1all_3000.txt (~10 s)
uv run --with sympy python scripts/z65_logic2_onlyprime.py 200                     # = onlyprime_200.txt (~2 min)
uv run --with sympy python scripts/z65_logic2_landing.py 200 6565                  # = landing_check.txt, first block (~1 min)
uv run --with numpy --with sympy python scripts/z65_logic2_cover.py 840 nonsq      # Mordell control: 186/186 covered
uv run --with numpy --with sympy python scripts/z65_logic2_cover.py Q 1mod840_nr11 # = cover_probe.txt lines (Q as listed)
uv run --with sympy python scripts/z65_logic2_covertree.py 13 17 19 23             # = covertree.txt (< 1 min)
uv run --with sympy python scripts/z65_logic2_covertree.py 13 3 17 2 5 19          # = covertree_powers.txt (~20 min)
uv run --with sympy python scripts/z65_logic2_covertree.py 13 17 19 23 29 31 37    # = covertree_deep.txt (~17 min)
```
Everything else is proof.
