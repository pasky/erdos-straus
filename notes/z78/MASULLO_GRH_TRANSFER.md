Result: Nothing in Masullo's announced GRH manuscript transfers to the B2 lower tail or to any STATUS §2 target. Conditional on its claimed GRH for all Hecke L-functions, the campaign's Dirichlet-, Dedekind- and Kummer-GRH-conditional results would become conditional on the manuscript instead. The only inputs that strictly need Hecke rather than Dirichlet GRH are class-group characters of order ≥ 3, Kummer/ring-class Chebotarev and Bach-type class-group generation. They either never enter the (★) expansion (Lemma 2) or stop at the square-root barrier (Lemmas 3–4).   Label: Assessment (with four PROVED elementary/standard lemmas; every inferred consequence CONDITIONAL on GRH for Hecke L-functions, claimed in Masullo 2026, unrefereed)
Scope: Transfer question only, graded from the source (`/tmp/masullo/full.txt`, PDF sha256 e039d3f6…bf5; PDF page = printed page). No assessment of the manuscript's correctness. **GRH is not proved**: the manuscript is an unrefereed announcement. ES in ℕ is open. No CLAIMED-CONDITIONAL ES theorem results.
Review: none (authoritative grading pass by Claude; supersedes the verdicts of `notes/z78/MASULLO_GRH_SKIM.md`, which stays as a page map with an erratum)
Triage: NULL (plus one BARRIER-SCOPED dead-end line, §5)
STATUS delta: none

# z78 — Masullo's announced GRH manuscript: what, if anything, transfers to ES

**Bottom line.** Even granting the claim in full (GRH for every unitary Hecke character of every number field), the
campaign gains no mechanism. The (★)/B2 count expands only into Dirichlet characters, so Hecke GRH adds nothing beyond
the Dirichlet GRH the campaign already assumes. This was already priced in by `CONDITIONAL_ES.md` §5, table row "GRH
(Dirichlet, Hecke)". Every GRH route to a single integer N loses a factor N^{1/2−o(1)}. The manuscript's trace formula
has *verbatim* Weil's geometric side, and its live architecture uses no positivity. The only real change if the claim
survives refereeing is a relabelling of existing conditional results (§2.6). The skim's overall null stands, but the
skim has three errors and one over-generous LONGSHOT (§1.4, erratum added to the skim).

## 1. Scope audit (from the source)

### 1.1 What is claimed, and by whom
* Blog (`/tmp/masullo/post.html`; R. Vakil, 2026-11-20). Masullo has a "proposed proof of GRH". Conrad has been
  "looking closely at it for months … so far looking good". The draft is released early with a request to "check it,
  formalize, fill any small gaps". This is an announcement, not a theorem.
* Front matter (full.txt 147–167, PDF pp. 6–7). Masullo writes that "the math is complete" and that "only filling in some writing
  remains on several parts". The introduction "is unfinished and will be soon replaced". He and Conrad are aware of
  "several glitches here and there". The stated generality is "all number fields, all unitary Hecke characters".
* **The statement.** The claim is that nontrivial zeros of completed Hecke L-functions L(s, χ), for every number field F
  and every unitary χ ∈ Ĉ_F (Grössencharacters included), lie on Re s = 1/2.
  * It is qualitative zero location. No effective constants are needed for the consequences (§1.4 E1).
  * Multiplicity is *not* part of the claim. §1.7.3 (1772–1783, p. 37) says "This will not be a part of my paper,
    and it is reserved for a sequel … I have not fully worked out all details". The bound N(ρ) ≤ [F:Q] for non-central
    zeros (§14.1.2, p. 528) is an announced expectation only. No information is offered about central zeros (p. 528).
  * GL_n with n ≥ 2 is not claimed. §14.3 (p. 536) gives only a generic-zero multiplicity bound n[F:Q]. Its footnote
    says "the version for GL_n is the subject of ongoing work with Brian Conrad". GRH/GSH for cuspidal GL_n are listed as
    conjectures (Conj. 14.1.2.1, 31971–31974, p. 529).
  * Function fields are not affected. §14.2 (pp. 534–535) says "The short answer is 'no'", and the method "would
    recover Weil's own Explicit Formulas only". In any case function-field GRH is Weil's theorem.
* **Unfinished, per the source.**
  * Thm 13.3.1.2 (the zero-location theorem, p. 522) is "Insert statement". Footnote 3 reads "State and prove the Main
    Theorems". Thm 13.3.1.1 carries the footnote "Correct statement".
  * §1.3.3–1.3.4 are marked "Finish!" (1259–1260).
  * Ch. 14 cites a dangling "Theorem ??" (31929, 32164).
  * A B.6 footnote says "perhaps omit this mention if … zero-free regions is removed" (35326).
* **By-products actually stated.**
  * The trace formula, Thm 12.5.1.1 (31509–31574, pp. 519–520).
  * Theorem 1.7.1.1 on polar multiplicities of local Euler factors (1668–1684; "has nothing to do with the zeros").
  * Theorem 7.5.0.1 ("Strong Co-Primality", a topological isomorphism of function spaces; "not logically necessary",
    22419–22447).
  * A uniform Kronecker–Weyl lemma (App. B.5).
  * **None** of these is a statement about arithmetic sums: no zero-density result, explicit least-prime bound,
    Chebotarev bound, large sieve, distribution in progressions, or lower bound for any count. Appendix B (convexity,
    explicit formulas, classical zero-free regions) is recalled background.

### 1.2 The trace formula (Thm 12.5.1.1) and what it is logically
For F a number field and φ ∈ D(C_F) (smooth, compactly supported) with **φ(C_F¹) = 0**, the theorem states:

  [archimedean principal values] + Σ_{v finite} (log q_v/μ_v(O_v^×)) ∫′_{F_v^×} φ(g_v)|g_v|^{1/2}/|1−g_v|_v dμ_v
    = M(φ)(|·|^{1/2}) + M(φ)(|·|^{−1/2}) − Σ_{c : L(c)=0, σ(c) ∈ 1/2+I} N(c) M(φ)(c|·|^{−1/2}),

with I = [−a, a] and a > 0 arbitrary (intro statement 1258–1293, p. 28; same theorem at p. 519).

The left side is Weil's prime side exactly. The letter says so itself: "the side involving the places … (the Geometric
Side) is identical to that from the Explicit Formulas, and the side involving the zeros (the Spectral Side) is not"
(§1.7.2, 1753–1755, p. 36). Subtract the classical explicit formula, which runs over all nontrivial zeros. The theorem
becomes Σ_{zeros with |σ−1/2|>a} N(c)M(φ)(c|·|^{−1/2}) = 0 on the admissible test class.

So, modulo the classical explicit formula, the trace formula *is* a zero-location statement (Assessment, standard). It
carries no arithmetic information that GRH does not already imply. The intro deduces GRH from it by approximating the
holomorphic family φ_s(t) = t^s·1_{t>1} and using Montel's theorem and holomorphy of L′/L on Re s > 1/2 (§1.4.3–1.4.5,
1340–1420, pp. 29–30).

### 1.3 Positivity: which architecture is live (orchestrator's question)
The draft contains two incompatible strata.

* **Live stratum: no positivity.** This is §1.4.6 (1422–1441, p. 30) and the Sarnak letter of mid-October 2026
  (§1.7.2, 1686–1697, p. 35). The trace formula "can only be proved for test functions φ … such that φ(C_F¹) = 0", and
  "Weil's Positivity Criterion uses test functions of the form φ = ψ₁∗ψ₂, ψ₂(g) = ψ₁(g⁻¹), and the only φ of this form
  that satisfies (1.7.2.1) is identically zero".
  * The last claim is correct: (ψ∗ψ̃)(1) = ‖ψ‖₂² and 1 ∈ C_F¹.
  * Hence Weil positivity is *vacuous* on the test class of Thm 12.5.1.1, which is the theorem the text calls "the
    Main Theorem of this work" (31498).
* **Stale stratum: "trace formula + Positivity Criterion".**
  * Thm 13.3.1.1 (31605–31646, p. 522) is called "Trace Formula", but it has different hypotheses: vanishing of the
    first [F:Q] s-derivatives of the isotypic Mellin transforms at the central points. Its spectral side is also
    different: only zeros with σ = 1/2, counted with N_spec = min{N, [F:Q]}. It carries the footnote "Correct
    statement".
  * This is the degenerate a = 0 case. The letter says that case yields *no* trace formula: "The degenerate case a = 0
    does not lead to a Trace Formula anymore" (1756) and "For a = 0, no trace formula can be proved for any b ≥ 0"
    (1783).
  * §14.1.2 (31927–31932, p. 528; 32162–32165, p. 533) still calls Thm 13.3.1.2 "a consequence of the Trace Formula
    combined with the Positivity Criterion (in its form from Theorem ??)", and the cited theorem is a dangling
    reference.

**Decision (Assessment).** Chapters 13–14 are an older a = 0 + positivity architecture that was not revised. The live
proof is Thm 12.5.1.1 plus the holomorphic-family deduction. It contains **no positivity or nonnegativity statement
about any arithmetic quantity**. The only "positive" inputs are technical: Riesz-positivity of measures (30629) and
the classical nonvanishing of L_f(s, χ) on Re s = 1 (§1.4.7, 1444–1470; letter bullet 1698–1703), used to transfer
S-local bases to global ones.

Even the stale stratum would not matter for ES. Weil's criterion is an *equivalence* with GRH: positivity of
W(ψ∗ψ̃) = Σ_ρ |ψ̂(ρ)|² adds nothing to GRH. Its arithmetic content is an *upper* bound on prime sums with
positive-definite weights (the Odlyzko–Poitou discriminant-bound mechanism). A positive-definite kernel also peaks at
the identity (|ψ∗ψ̃(g)| ≤ ψ∗ψ̃(1)), so it cannot isolate a far norm N without an equal mass at |g| = 1. It is the wrong
direction and the wrong localisation for a lower bound on a nonnegative count such as R(p).

### 1.4 Where the skim (`MASULLO_GRH_SKIM.md`) is wrong or too generous
* **E1 (error).** The skim says the draft "does not provide usable explicit error terms of the kind needed for effective
  GRH consequences", does not announce "Siegel-zero exclusion", and "adds no explicit constants". This is a category
  mistake. Zero location *is* the whole hypothesis of the explicit-constant GRH literature (Lagarias–Odlyzko 1977,
  Oesterlé, Bach 1990, Bach–Sorenson 1996). A Siegel zero is excluded by definition. If the claim holds, every such
  consequence follows with its published constants. The absence of a numerical onset in Thm G is a property of the
  *campaign's* proof (`notes/z76/ALPO_TRANSFER.md` §5), not of GRH.
* **E2 (misleading scope).** The skim says the claim "is not a theorem for arbitrary Artin L-functions". That is true
  of what the manuscript claims, and Artin holomorphy is untouched. For the transfer question, however, Prop 5 below
  applies: Hecke GRH implies Dedekind GRH for **every** number field, and puts all zeros *and poles* of every Artin
  L-function in 0 < Re s < 1 on the critical line. GRH-effective Chebotarev (Lagarias–Odlyzko assume GRH for ζ_L only)
  therefore holds in every finite Galois extension, including non-abelian ones.
* **E3 (omission).** The skim reports "positivity not used" without noticing the contrary Ch. 13–14 stratum (§1.3).
* **Verdict disagreement.** The skim rates "orbital Schauder bases / kernel splitting" a LONGSHOT "as inspiration". I
  rate it NOT APPLICABLE. The machinery's arithmetic output is Weil's Λ-weighted geometric side verbatim (§1.2). Any
  specialisation inherits the square-root loss of Lemma 3, and there is no divisor-type functional anywhere in it.

## 2. Conditional-upgrade ledger: Hecke GRH versus the Dirichlet/quadratic GRH the campaign already uses

Throughout this section **Hyp** is GRH for all Hecke L-functions of all number fields, as claimed in Masullo 2026
(unrefereed). Hyp contains Dirichlet GRH (F = ℚ). It strictly exceeds Dirichlet GRH in two ways. First, it covers
class-group, ring-class and ray-class characters of ℚ(√−dp) that do not factor through the norm: these are L-functions
of weight-one dihedral forms, not Dirichlet L-functions. Second, via abelian factorisation and Brauer induction it
gives Dedekind GRH for Kummer, ring-class and non-abelian fields.

**Proposition 5 (Brauer; PROVED, classical).** Hyp implies that, for every finite Galois L/ℚ and every Artin
representation ρ, all zeros and poles of L(s, ρ) in 0 < Re s < 1 lie on Re s = 1/2. In particular it implies GRH for
ζ_L for every number field L.

*Proof.* By Brauer, L(s, ρ) = ∏ L(s, ψ_i, K_i)^{n_i} with n_i ∈ ℤ, K_i ⊂ L and ψ_i finite-order Hecke characters.
Each factor is entire, except for the pole of ζ_{K_i} at s = 1, and has no zeros in 0 < Re s < 1 off the line (Hyp)
and none on Re s = 1 (classical). So at s₀ with 0 < Re s₀ < 1 and Re s₀ ≠ 1/2 every factor is holomorphic and
nonzero, and so is L(s₀, ρ). The case ζ_L is ρ = Ind_L^{Gal} 1. ∎

### 2.1 (1) The (★)/B2 count through ideal classes
**Lemma 1 (ideal-divisor form of the square levels; PROVED, elementary).** Let p ≡ 1 (4) be prime, K = ℚ(√−p),
O_K = ℤ[√−p] (disc −4p), s ≥ 1, β_s = 1 + 2s√−p and N_s = Nβ_s = 4s²p + 1. Then 𝔡 ↦ N𝔡 is a bijection from the
integral ideal divisors of (β_s) onto the positive divisors of N_s. Hence, at the level C = s²,

  R_{s²}(p) := #{d | 4Cp+1 : d ≡ −1 (mod 4C)} = #{𝔡 | (β_s) : N𝔡 ≡ −1 (mod 4s²)}
             = #{𝔡 | (β_s) : [𝔡] ∈ 𝒩⁻¹(−1) ⊂ Cl_{(4s²)}(K)},

where 𝒩 : Cl_{(4s²)}(K) → (ℤ/4s²)^× is the norm map on the ray class group mod 4s².

*Proof.* The integer N_s is odd, and it is ≡ 1 mod p and mod s. For a prime ℓ | N_s we have −p ≡ (2s)^{−2} mod ℓ, so
ℓ splits as 𝔩𝔩̄, 𝔩 ≠ 𝔩̄. If both 𝔩 and 𝔩̄ divided β_s, then ℓ | β_s in ℤ[√−p], i.e. ℓ | 1, which is absurd. So
(β_s) = ∏ 𝔩_i^{v_{ℓ_i}(N_s)} with one prime ideal over each ℓ_i, and divisors correspond to divisors via the norm.

The norm is well defined on ray classes: if α ≡ 1 mod^× 4s², then Nα ≡ 1, and (−α) = (α). The level C = s² term is
one summand of the divisor form of R(p) (FRONTIER §2.1). General C = t₀s² is the same with ℚ(√−t₀p) and an order
containing β (`Z60_RAYCLASS.md` Lemma 1). ∎

**Lemma 2 (only norm pull-backs occur; PROVED, standard).** The indicator of N𝔡 ≡ −1 (mod 4C) on ideals prime to 4C
is φ(4C)^{−1} Σ_{χ mod 4C} χ̄(−1) (χ∘𝒩)(𝔡). Up to finitely many Euler factors, L(s, χ∘𝒩) = L(s, χ)L(s, χχ_K).

*Proof.* At a split prime ℓ the Euler factors are (1 − χ(ℓ)ℓ^{−s})^{−2}. At an inert prime they are
(1 − χ(ℓ)²ℓ^{−2s})^{−1} = (1 − χ(ℓ)ℓ^{−s})^{−1}(1 + χ(ℓ)ℓ^{−s})^{−1}. ∎

**Consequence (Assessment, from Lemmas 1–2).** In every harmonic expansion of the (★)/B2 count, whether over ℚ (CONDITIONAL_ES
(3.2)) or over K (RAYCLASS, Lemma 1), the only L-functions are Dirichlet L-functions. The Hecke characters that Hyp
adds beyond Dirichlet GRH (class-group characters of order ≥ 3, ring-class characters) would enter only through a
*class* condition on the divisor 𝔡. Solution-hood imposes no such condition beyond its norm and genus:
* `Z60_RAYCLASS.md` Prop 3.1: the condition is class-determined only for C ∈ {1, 2, 3, 6}, exactly when (ℤ/4C)^× has
  exponent 2.
* `Z70_CLASS.md` §1.1: the "good classes" G_d(n) are classes of solution ideals, a consequence of a solution and not a
  condition for one.

The genus/BM layer that *is* GRH-accessible is already done under Dirichlet GRH alone: M_gen(p) ∼ M₀(p)
(`notes/z76/ALPO_TRANSFER.md` Thm G) and M_BM ∼ M₀ (FRONTIER §2.2).

**Where the class-group route stops.** There are two equidistribution statements one might hope to use.
* For *prime* ideals in a class c of a ray/ring class quotient G of order H, Lagarias–Odlyzko 1977 Thm 1.1 (|C| = 1,
  [L:K] = H) under Hyp gives

    π_c(x) = Li(x)/H + O(√x · log(𝔮_G x)),

  with 𝔮_G = |Δ_K| N𝔣_G. This is positive only once x ≫ H² log²(𝔮_G x) log² x. That is the square-root barrier.
  Going below x ≈ H² requires cancellation *between* the zero sums of different characters, a statement about the
  joint statistics of ordinates, not about their location.
* For *all* ideals, counts in a class are lattice-point counts and need no GRH.

Neither statement touches B2. At level C the event is "one of the τ(N_C) ideal divisors of the single element β_C has
norm ≡ −1 (mod 4C)". Its ideals are a set of relative density ≤ τ(N_C)/N_C among ideals of norm ≤ N_C. No statement
about all ideals, or all prime ideals, in norm windows sees such a set. The exact location of the wall is Lemma 3.

**Lemma 3 (square-root loss in isolating one integer; PROVED rel. the explicit formula, zero counting, and GRH ⟹
Lindelöf in the form log|L(½+it)| ≪ log 𝔮(t)/log log 𝔮(t)).** Let L(s, ψ) be a Hecke L-function over K of analytic
conductor 𝔮 satisfying GRH. Fix h ∈ C_c^∞(−½, ½) and put φ_N(t) = h(N log(t/N)). Then:
* (a) **Explicit formula.** In the explicit formula for φ_N (weights N𝔞^{−1/2}Λ(𝔞)ψ(𝔞)), the geometric side is
  supported on prime-power ideals of norm exactly N. It has size ≤ τ_K(N)·log N·N^{−1/2}. The GRH bound for the
  zero side is Σ_ρ |Φ_N(ρ)| ≍_h [K:ℚ]·log(𝔮N). Indeed |Φ_N(½+iγ)| = N^{−1}|ĥ(γ/N)|, and there are
  ≪ log(𝔮(|T|+2)^{[K:ℚ]}) zeros per unit height, with essentially all mass at |γ| ≲ N.
* (b) **Perron.** Shifting the smoothed Perron integral for the coefficient a_ψ(N) to Re s = ½ gives a bound
  ≪ N^{1/2} exp(C log(𝔮N)/log log(𝔮N)). The target satisfies |a_ψ(N)| ≤ τ_K(N).

In both cases the GRH bound exceeds the single-integer quantity by N^{1/2−o(1)}. A single-integer conclusion would need
cancellation among ≍ N log(𝔮N) zero terms to precision N^{−1/2}. That amounts to knowing the factorisation of N
(Assessment). For R(p) the relevant integers are N_C = 4Cp + 1 with C ≤ p, each carrying its own tied modulus 4C. The
loss per integer is therefore ≥ p^{1/2−o(1)}, against a total main term ≍ log²p.

This sharpens, and agrees with, FRONTIER §2.4 ("Each of those controls averages … never one integer with a polylog main
term"), B3 ("termwise GRH") and `CONDITIONAL_ES.md` §3.2. The latter has GRH "character by character … missing by
p^{1−o(1)}" at X ≍ p², which is the same loss X^{1/2} written for its AP of length X.

**Verdict (1):** **NOT APPLICABLE.** Hecke GRH reaches neither R(p) ≥ 1 nor H⁻_BM. It adds no character to the (★)
expansion, and GRH in any form stops at the N^{1/2} wall for every integer.

### 2.2 (2) Effective Chebotarev in the abelian extensions that "encode" the B2 conditions
Hyp plus Prop 5 give Lagarias–Odlyzko / LMO bounds in every Galois field: least prime in a class ≪ (log d_L)². There
are three reasons this does not reach B2.
* **(a) Divisibility is ramification, not Frobenius.** "ℓ | 4dp + 1" picks a finite set of primes (ramified in
  ℚ(√(4dp+1)) when that integer is squarefree), whereas a Chebotarev set has positive density (`CONDITIONAL_ES.md` §3.2).
* **(b) Fixed fields see only parity.** In a field of bounded level, Frobenius sees p mod t, i.e. the quadratic/genus
  layer and never the class (`CLASS_FORCING.md` Thm 2.1, FRONTIER §4 item 9).
* **(c) The free-prime form needs Kummer level ≍ ℓ.** Lemma 4 below quantifies this.

**Lemma 4 (Kummer resolution of the tied event; PROVED, elementary plus Kummer theory).** Take the free-prime form of
(MS): a prime ℓ ≡ 3 (4), ℓ ∤ p, is a witness iff its residue r := (−p mod ℓ) ∈ {1, …, ℓ−1} divides (ℓ+1)/4, i.e. iff
p mod ℓ ∈ T_ℓ := {−r mod ℓ : r | (ℓ+1)/4}.

For m | ℓ − 1, the Frobenius at primes above ℓ in L_m = ℚ(ζ_m, p^{1/m}) determines p mod ℓ exactly up to (𝔽_ℓ^×)^m,
via the m-th power residue symbol (p/𝔩)_m ≡ p^{(ℓ−1)/m}. Since −1 ∈ T_ℓ, the set T_ℓ is a union of such cosets only if
(ℓ−1)/m ≤ |T_ℓ| ≤ τ((ℓ+1)/4).

So a Kummer-Chebotarev description of the event at ℓ requires
* m ≥ ℓ^{1−o(1)};
* [L_m:ℚ] = mφ(m) ≥ ℓ^{2−o(1)} and log d_{L_m} ≍ mφ(m) log(mp);
* a GRH-Chebotarev range of x ≫ ℓ^{4−o(1)}.

The event, moreover, concerns the Frobenius of the *single* prime ℓ. The other primes counted in L_m are primes
ℓ′ ≡ 1 (m), and for them the witness event involves ℓ′ + 1 and p mod ℓ′ instead.

Such fields (abelian over ℚ(ζ_m)) are exactly what Hyp adds over Dirichlet GRH, and they fail by a power. This makes
quantitative `CONDITIONAL_ES.md` §3.2's Assessment that power-residue symbols give p only modulo k-th powers. The
Type II conditions ("p + e has a divisor 4ab …", `Z68_PC2.md` Thm A) have the same shape and the same verdict.

**Verdict (2):** **NOT APPLICABLE** to B2.
* It is genuinely new as Chebotarev input, and is used where primes are *free*: window supplies for caps (§2.4) and
  nonresidue counts (§2.3).
* Those uses are already covered by Dirichlet GRH or by the Kummer GRH the campaign had already assumed
  (`CAP_INTERPOLATION.md` Thm 4.2; (J)91 Prop 2.1).

### 2.3 (3) PC(F, η) and the bridge of ALPO_TRANSFER §6
`Z68_PC2.md` §1: PC(F, η) says that every profile π ∈ Ẑ^× with at least (½ − η)π(y) odd quadratic-nonresidue
components below y lies in an Erdős–Straus family class of modulus ≤ F(y).

This is a statement about congruence classes in Ẑ^× and contains no L-function. **Hyp neither implies nor partially
implies PC.** In the bridge, GRH is used only to certify the *hypothesis* of PC at the actual profile of p:
* by Lagarias–Odlyzko for ζ_{ℚ(√p)} (Z68 Thm B(iii)), or
* by the smoothed explicit formula for χ_p (ALPO §6, y = C_η(log p)², c_η = 3/(2√C_η)).

Hyp improves neither. The error √y·log p for the single character χ_p is the same L-function with the same GRH bound,
so c_η and the √y exponent are unchanged.

**Exact missing statement:** PC(F, η) with log F(y) ≤ c_η√y for one fixed η ∈ (0, ½). Equivalently, any covering
statement in Ẑ^× strong enough to cover the GRH-certified profile of every large p by ET classes of modulus < p^{3/2}
(transfer lemma, ALPO §6).

**Possible weakening (Assessment; not Masullo-specific).** GRH certifies more of p's profile than one nonresidue count.
* Quadratic GRH alone gives ≈ ½ nonresidues in every dyadic block [z, 2z] with z ≫ (log p)²(log log p)².
* Hyp additionally gives m-th-power-residue frequencies (Kummer fields over ℚ(ζ_m), fixed m).

A PC variant quantifying only over profiles with these statistics is formally weaker. It escapes the explicit z68 lower
bounds, whose extremal profiles have nonresidues concentrated in (cy, y] or in (y^{1/2}, y] and are 1 elsewhere
(`Z68_PC2.md` Thm B(v)). Two caveats apply:
* **Narrower y-range.** Certifying blocks down to y^{1/2} needs y ≥ (log p)^{4+ε}, which shrinks the allowed growth of
  F.
* **Drift toward ES.** Restricted to *actual* prime profiles, "covered by an ET class of modulus < p" is ES(p) through
  ET families (Z68 Thm B(i)). Every GRH-certifiable statistic added to the hypothesis moves the covering statement
  toward ES itself.

The covering content is untouched by any analytic input.

**Verdict (3):** PC is **untouched**; the bridge is **NOT APPLICABLE** to upgrade. The weakened-PC observation is a
**LONGSHOT** for the PC line, and it needs only quadratic GRH (follow-up F1).

**No CLAIMED-CONDITIONAL theorem.** I found no implication "Hyp + (clean, non-ES-strength hypothesis) ⟹ eventual ES"
beyond ALPO §6. That bridge needs only quadratic GRH and still needs PC.

### 2.4 (4) The capped relaxation e*(n), M_gen ∼ M₀, least prime ideals, Bach's bound
* **M_gen ∼ M₀.** This is already CONDITIONAL on Dirichlet GRH alone (Thm G), and Hyp adds nothing. Any numerical onset
  would have to come from redoing Thm G's proof with explicit GRH constants. That is possible in principle under
  either hypothesis, and nothing Masullo-specific is involved (E1).
* **e*(n).** The best constant is exp((2√2 + o(1))√(log₂R·log₃R)) under Dirichlet GRH (`notes/z78/ANALYTIC_WILD.md` §4).
  Its bottleneck is combinatorial: the cost of planting k primes (log D ≈ k log k) against the Minkowski
  deletion/diameter term 2u/(k+1). This floor holds for the certificate class *even granting perfect distribution of
  the eligible primes* (ANALYTIC_WILD §2). Kummer-Frobenius data, which is what Hyp adds, "sees only the discrete logs
  modulo the M-smooth part of q − 1", so Hooley/Kummer accounting certifies only the index condition ((J)91 Prop 2.1,
  `BALANCED_LATTICE.md`). The index term is already dominated by the Minkowski term.
* **Bach-type class-group generation** (prime ideals of norm ≤ 12 log²|Δ|). This is genuinely Hecke and not Dirichlet.
  It is irrelevant here because the cap lives in 𝔽_q^×, and the genus explicit bound needs a *nonresidue*. That is
  Dirichlet GRH (Ankeny/Bach: n_p ≤ 2 log²p; `Z57_BFII.md` Cor 2.4).
* **Expander/diameter results (Jao–Miller–Venkatesan type).** These give word length O(log q) in 𝔽_q^× or Cl(O) with
  generators of norm ≤ (log q)^{2+δ}, using GRH for the same Dirichlet or class-group characters. They would need
  ≍ (log X)^{2+δ} generators planted in K = (R+q)/4. Planting k primes forces X ≥ φ(D)² with log D ≈ k log k, so
  k ≲ log X/log log X. This is the same square-root wall in the generator-size aspect.
* **Least prime ideal in a class.** Under Hyp, LMO gives ≪ (H log 𝔮)², with no ES use (§2.1).

**Verdict (4):** **NOT APPLICABLE.** There is no improvement in the GRH cap constant, in M_gen, or in the explicit genus
cap. FRONTIER §5.4's "GRH alone does not reach (log₂p)^{O(1)} this way" ((J)91) applies verbatim to Hyp.

### 2.5 (5) STATUS §2 targets: (MS-U₇), (MS⁺₁₀₅), H⁻_BM
* **(MS-U₇) / U₇.** Each witness is "some f ≡ 7 (8) with (−n mod f) | f + 1": the same full-residue, tied-modulus
  event as Lemma 4 (`Z60_LOPEZ.md` §4.2).
* **(MS⁺₁₀₅).** This is R(n) ≥ 1 at non-square n including composites. Lemmas 1–3 apply verbatim. Composite n removes
  even the primality-based Frobenius inputs.
* **H⁻_BM.** This is a lower tail with error < ε·M_BM ≍ log²p. The error E(p) = R − M is bounded only through Weil and
  exponent-pair estimates, which are algebraic and not L-function zeros (`notes/z76/ANALYTIC_34.md`, ANALYTIC_WILD §§7–8).
  Lemma 3 shows that GRH-type inputs lose p^{1/2} per integer.
* The certified censuses and the Salez 10¹⁷ threshold are exact computations, and Hyp is irrelevant to them.

**Verdict (5):** **NOT APPLICABLE** to all three.

### 2.6 What the claim *would* change: relabelling only (Assessment; do not edit master files unless the manuscript is accepted)
If the claim is accepted, the following would read "CONDITIONAL on GRH (Masullo 2026; claimed, unrefereed)". Hyp
covers their hypotheses directly or by Prop 5.
* **Dirichlet GRH.**
  * Thm G (M_gen ∼ M₀).
  * M_BM ∼ M₀ (FRONTIER §2.2).
  * The e*(n) bounds of `ANALYTIC_BREAK.md` §4a and ANALYTIC_WILD §§4, 9.
  * The GRH variant of `H4_NOT_POLYLOG.md` (κ < 1/6).
  * n_p ≤ 2 log²p in `Z57_BFII.md` Cor 2.4.
* **Quadratic GRH plus PC (still needs PC).** Z68 Thm B(iii) and the bridge of ALPO §6.
* **Dedekind/Kummer GRH.**
  * `CAP_INTERPOLATION.md` Thm 4.2, together with CAP_POINTWISE's (16 log n + 70)².
  * V_φ over ℤ[φ] ((J)21, through Lenstra's Euclidean/Kummer result).
  * The GRH part of (J)91 Thms 4.1–4.2. These still need EQ or S.
* **Not covered.** GLH, GRH for GL(2)/Rankin–Selberg or cusp forms (`CONDITIONAL_ES.md` §§4–5, `Z59_WALDS.md`,
  `Z60_SIGNED.md`), and Artin holomorphy.
* STATUS §0's "No standard conjecture is known to imply the lower tail" is **unchanged**.

## 3. Method audit (from §1 of the manuscript, Thm 12.5.1.1 and §1.4)
* **Trace identity on theta-function spaces with φ(C_F¹) = 0.** The geometric side is a linear functional supported on
  prime-power ideles. In idelic form it equals Σ_{𝔭,m} log N𝔭·N𝔭^{−m/2}[φ(π_𝔭^m) + φ(π_𝔭^{−m})] plus archimedean terms,
  and is linear in Λ.
  * R(p) counts divisors, i.e. coefficients of ζ·L(χ) and not of their logarithmic derivatives. So no φ has geometric
    side R(p) or a smoothing of it.
  * The best one can represent is a *prime*-restricted sufficient count, P(p) = Σ_C Σ_{ℓ | N_C, ℓ ≡ −1 (4C)} log ℓ
    (where P > 0 implies R ≥ 1).
  * Even P(p) is a geometric side only if φ has bumps of width < 1/N_C at the *unknown* prime factors of N_C. Any
    φ ∈ D(C_F) has finite conductor and sees a prime ideal only through (ray class, norm). "𝔭 | β_C" is not a function
    of these data without the factorisation, so the construction is circular.
  * The vanishing condition φ(C_F¹) = 0 is harmless for such φ, since the support is away from |g| = 1. It is not what
    blocks the approach.
  * **What the spectral side would have to satisfy:** an evaluation of Σ_ρ M(φ)(ρ) over ≍ N_C log N_C zeros to
    precision ≪ N_C^{−1/2}, separately for ≍ p integers. Zero location bounds this sum only by its absolute value
    (Lemma 3), which is too large by N_C^{1/2}.
* **Explicit-formula variant.** The spectral side counts only the zeros inside the strip. Since the geometric side is
  Weil's, the formula carries no arithmetic information beyond GRH (§1.2).
* **Positivity / nonvanishing.** There is none in the live proof (§1.3). The stale Weil positivity gives only upper
  bounds on prime sums, and nonvanishing on Re s = 1 is classical.
* **Large sieve, duality, pointwise sums in progressions to large moduli.** There are none. Chapters 4–11 and
  Appendices C–E are functional analysis on GL₁ theta-function spaces: Schauder and Markushevich bases, nuclearity,
  Hardy–Sobolev completions and topological stacks. Appendix B recalls convexity, explicit formulas and zero-free
  regions.
* **The genus/class-group count.** Its GRH-accessible part is L(1, χ) for quadratic/genus χ: Dirichlet, done (Thm G,
  BM_LVALUE). The order-≥3 class-group characters do not occur (Lemma 2).

## 4. Verdict table

| candidate | verdict | reason a hostile expert would accept |
|---|---|---|
| Trace formula Thm 12.5.1.1 as an arithmetic identity | NOT APPLICABLE | Its geometric side is Weil's verbatim (letter 1753), so it is equivalent to zero location modulo the classical explicit formula; any single-integer use loses N^{1/2} (Lemma 3) |
| Orbital Schauder bases, kernel deconstruction, nuclear trace, Hardy–Sobolev norms | NOT APPLICABLE | Functional-analytic GL₁ infrastructure whose only arithmetic output is the Λ-linear geometric side; no divisor-type functional; the skim's LONGSHOT is withdrawn |
| Positivity / nonnegativity | NOT APPLICABLE | The live architecture has none (positive-definite φ violate φ(C_F¹) = 0); the stale Ch. 13–14 Weil positivity ⟺ GRH and yields only upper bounds on prime sums |
| Nonvanishing on Re s = 1 used as input | NOT APPLICABLE | Classical (Hadamard–de la Vallée Poussin, Hecke); averages over free primes |
| (1) Hecke-GRH class-group/ideal equidistribution for (★) | NOT APPLICABLE | Only χ∘𝒩 = Dirichlet characters occur (Lemma 2); B2 is a divisor-of-one-element event (Lemma 1); prime ideals are equidistributed only for x ≫ H² |
| (2) Effective Chebotarev in Kummer/ring-class/non-abelian fields | NOT APPLICABLE (to B2) | Divisibility is ramification; fixed fields give parity; the full residue needs degree ≥ ℓ^{2−o(1)}, so the range starts at ℓ^{4−o(1)} (Lemma 4) |
| (3) PC(F, η) / ALPO §6 bridge | NOT APPLICABLE (PC untouched); LONGSHOT for a statistics-restricted PC variant | PC has no L-function; GRH only certifies its hypothesis, and Hyp does so no better for χ_p |
| (4) e*(n), M_gen ∼ M₀, Bach / expander / least prime ideal | NOT APPLICABLE | Cap floors are combinatorial (ANALYTIC_WILD §2, (J)91); Kummer data certifies only the index; planting budget k ≲ log X/log log X rules out GRH-range generator sets |
| (5) (MS-U₇), (MS⁺₁₀₅), H⁻_BM | NOT APPLICABLE | Same tied full-residue event; composites; lower-tail error is bounded algebraically, and GRH loses p^{1/2} per integer |
| Multiplicity bounds (§14.1.2), function fields (§14.2), GL_n (§14.3) | NOT APPLICABLE | Not claimed (sequel or ongoing); function-field RH is Weil's theorem; no ES content |
| Relabelling of the conditional results of §2.6 | bookkeeping only, if the manuscript is accepted | No mechanism; no STATUS change now |

**Follow-up (at most one, LONGSHOT, not Masullo-specific).**
* **F1.** Restrict PC(F, η) to profiles with GRH-certifiable dyadic nonresidue statistics (quadratic GRH suffices).
  Optionally add fixed-m power-residue frequencies (Hyp). Then decide whether any z68-type explicit lower bound
  F(y) ≥ y^{c} survives. If F could be shown to be forced ≥ exp(y^{1/2+δ}) even there, the PC line closes. Only a
  positive covering construction would matter for ES.

Nothing else is worth a lane.

## 5. Proposed export lines (orchestrator decides)
* **WAVES (z78):** Masullo GRH announcement graded: NULL. Hecke GRH adds no character to the (★) expansion (norm
  pull-backs only). Kummer full-residue Chebotarev needs degree ℓ^{2−o(1)}. There is an N^{1/2} loss per integer. The
  live proof has no positivity (the Ch. 13–14 positivity text is stale). Conditional rows would be relabelled only.
  `notes/z78/MASULLO_GRH_TRANSFER.md`.
* **FRONTIER §6 (one line, BARRIER-SCOPED):** "Masullo's announced GRH for Hecke L-functions (2026, unrefereed) →
  Hecke ⊇ Dirichlet GRH adds nothing to (★) (only χ∘𝒩 occur), Kummer level ≍ ℓ needed, N^{1/2} wall →
  `notes/z78/MASULLO_GRH_TRANSFER.md`." It can be merged with the existing "GRH character-by-character on (★)" line.

## 6. Hostile checks
* **F1 (T1).** Nothing here proves positivity, so there is nothing to fail at squares. As a consistency check, at
  n = m² (odd) the level-s² count is #{d | (2sm)² + 1 : d ≡ −1 (4s²)} = 0. Every divisor of x² + 1 is ≡ 1 (4). This is
  T1, elementary, and sees no L-function; Lemma 1's primality hypothesis fails there.
* **F2–F4.** These do not apply, since no positive claim is made. The lemmas hold verbatim for numerator 8, composites
  and known zeros, and none of them asserts existence.
* **B6.** Every GRH statement used is about free primes or ideals in growing windows. No step averages over p.
* **Source fidelity.** All manuscript claims above are quoted with full.txt line numbers (PDF page = printed page; spot
  check: PDF p. 519 is §12.5, PDF p. 30 is §1.4.6). Neither the PDF nor its text is in the repository.
