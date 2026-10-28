# Hostile review: LOWERTAIL_ROUND2_ASTRA.md (branch side-agent/z49-ltastra2, commit c5c8b784)

Reviewer: Claude (cross-model), wave z49. Independent check script: `scripts/z49_ltastra2rev_check.py`. It does not import
`mordell_lib` or the author's script. Ran under `ulimit -v 8000000`, `timeout 900`, in about 1 minute.

## Verdict

**No FATAL errors, and no MAJOR mathematical errors.** Every stated implication I checked is correct as scoped. I verified
the ET inclusions, the Linnik quantifiers, the perturbation inequalities, the union bound, Markov sharpness, the
Lambert‑W root and (5.4).

**One MAJOR issue of framing and novelty (M1).** None of the five results is a genuine new theorem by the z49 bar ("strictly
strengthens a known statement / proves a barrier for a class not already barred"):

| Result | Correct? | What it really is |
|---|---|---|
| Thm 2.1 | yes (relative to import) | the sterile‑point theorem restricted to 2 of the 7 ET families, one modulus at a time, read through the definition L_Q = min. Logically **weaker** than the import. |
| Cor 2.2 | yes | Thm 2.1 plus Linnik/PNT bookkeeping. |
| Prop 3.1 | yes | "a nonnegative function with a zero and positive mean has a centred part of both signs". Tautology. |
| Thm 4.1 / Cor 4.2 / §4.2 | yes | Changing O(polylog) elements does not move averaged statistics. This is the campaign's T1 control in sequence language. Since M_gen(s²)=0 it bars no method that uses the genus main term. |
| Prop 4.3 | yes | A one‑line union bound. |
| Thm 5.1 | yes | Markov's inequality plus the obvious one‑atom extremiser. |
| Cor 5.2 | yes | Asymptotics of k log(A/k)=t. Standard calculus. |
| Thm 5.3 | yes | z48 Thm 7.1 with k retuned by a second‑order amount. |

The document is mostly honest about this in its own Assessment paragraphs. The header still presents §2 and §5 as the PROVED
deliverables, and the parent should not log any of them as a z49 proof step.

## 1. Theorem 2.1 and Corollary 2.2

**ET inclusions: verified.** With ET Prop 1.9 (v) / mordell_lib `II1` taking (a,b,e) = (u,v,u+v), the class is n ≡ −e (mod 4ab).
The conditions are e | a+b and gcd(e,4ab)=1. For e=u+v the gcd condition is exactly gcd(u,v)=1 together with u+v odd.
The residue −u−v mod 4uv is the R line. With ET (vii) / `II3` taking (a,d,e) = (1,x,y), the class is
n ≡ −4a²d−e (mod 4ade) = −4x−y (mod 4xy). Its condition is gcd(4x,y)=1, which is y odd plus gcd(x,y)=1. The author is right
that II3 imposes no divisibility condition. I checked 2,752 identities with hand‑derived formulas, not `solve`:

- (uvC, nuC, nvC) for R;
- (x(Cy−1), nCx, nCx(Cy−1)) for B, using n+y = 4x(Cy−1).

**Sterile point: scope is correct.** "Sterile" in DEPTH_ASPECT Thm 3.1 / STERILE_* means x(u) lies in **no class of any of the
seven families**, over all parameters. The point is x_q=1 for q≠r (including q=2,3) and x_r=u with u a non‑residue, so its
projections lie in Ω_Q(r). The zero envelope follows. For every positive n, n ≡ −u−v (mod 4uv) forces C ≥ 1. So
C_Q(n) ≤ T(n) for **all** n ≥ 1, and the §1 caveat about height domains is unnecessary (harmless).

**Positive mean: verified.** For (1,2r) and (2r,1) with r ≡ 3 (mod 4), the target −1−2r is 1 mod 8 and a non‑residue mod r.
Each contributes 2/(r−1). The two ordered pairs are the *same* congruence class counted twice, which is legitimate because R
is ordered. The same holds for the odd k case in Prop 3.1, with 4/φ(r^k).

**Independent numeric check at an r inside the theorem's range.** I used r = 2,840,087, the first prime ≡ 3 (mod 4) above
2^21.4375. Each fibre was enumerated by CRT, with no Cartesian product over moduli.

| Q | menu cells | fibre size | min | mean |
|---|---|---|---|---|
| 24r | 26 | 1,420,043 | **0** | 9/1,420,043 ≥ 4/(r−1) |
| 120r | 78 | 2,840,086 | **0** | 21/2,840,086 |
| 840r | 240 | 8,520,258 | **0** | 83/8,520,258 |

For small r the controls behave as the author says: r=7, Q=168 has min 1, and r=31 and r=43 have min 0. These checks only
show consistency. The content of the theorem is entirely the import.

**Linnik quantifiers: verified.**
- Q_Y = 8∏_{ℓ≤Y}ℓ, so 16 | Q_Y, which is harmless.
- p > Y because p is a prime unit mod Q_Y.
- log p ≤ L₀(1+o(1))Y + O(1), so c log p ≤ Y eventually for c < 1/L₀.
- p ≡ 1 (mod 8) and p ≡ 1 (mod 4) give (ℓ/p) = (p/ℓ), so the least QNR is exactly r.
- Q must contain r, so the statement is vacuous until r ≤ c log p, which is fine.

**M1 (MAJOR, novelty/framing).** Under the definitional dictionary "genus envelope = min over the coset" (z48 Thm 6.1),
"L_Q(Ω_Q(r)) = 0 for every Q" just says "for every finite R/B menu some point of the fibre is uncovered". STERILE_LOWER Thm 6.3
/ FRONTIER §3 already records something strictly stronger: one compatible profinite point avoids **all seven** families
simultaneously, so no finite ET covering exists. Thm 2.1 is therefore the imported theorem weakened in two ways (two
families, one Q at a time), not a new result.

The "strict extension of the z48 barrier" is true only relative to z48 §6.3, which turns out to have been superseded on these
fibres by an older campaign result. That is worth a cross‑reference line in FRONTIER, but it is not a proof step. The
fibres also differ: z48 covers small negative primes such as 11, 13, 17 and 19, while Thm 2.1 needs r ≥ 2.84·10⁶. So the two
results are complementary, not nested, and "strictly extends" should read "complements (on fibres with r ≥ r₀)".

**m1 (import robustness).** STERILE_LOWER Thm 6.3 (r₀ = 2^21.4375) rests for octaves 23–29 on "the same binary family and
spot checks (not re‑run end to end by a reviewer)" (DISCOVERIES (J)70 entry). STERILE_EXPLICIT Thm 3.4 (r₀ = 2³²) passed two
SOUND hostile reviews. Since the doc's argument is insensitive to r₀, it should lead with 2³² as the robust import and give
2^21.4375 as the stronger variant with its review status.

## 2. Proposition 3.1

Correct and trivial. X(z_Q) = −μ follows from C(z_Q)=0. "Both signs" follows from mean zero. The long‑modulus instances
(1,2r^k), with k odd at modulus 8r^k, check out. The scope paragraph is honest: it does not bar one‑sided estimates at actual
primes. The identity 4uC−1 | p+u is correct, since p+u = v(4uC−1). The "three attempts" paragraph contains no mathematics
beyond restating the gap. Grade: **tautology**.

## 3. Theorem 4.1, Corollary 4.2, §4.2

**Correctness.**
- (4.1): for each q, Σ_a |δ| ≤ D. This holds for every y ≤ x, since all δ ≥ 0 for an insertion and |δ| ≤ D in general.
- (4.2): Σ_a δ² ≤ (Σ_a|δ|)².
- (4.3): the reverse triangle inequality.

**Transfers.**
- EH: x^ϑ·polylog ≪ x/log^A x.
- Variance: |V′−V| ≤ 2√(V Q)D + QD², which is o(V₀) iff QD² = o(V₀). This holds for V₀ ≍ xQ log x.
- Montgomery: polylog ≪ x^ε.

All are correct. My own (not reused) check of (4.1)/(4.2) on a toy perturbation was unnecessary given the one‑line proof.
The author's script does it.

**§4.2.**
- s_{j+1} > s_j² gives K(x) = O(log log x).
- Odd squares are 1 mod 8, and T = 0 by T1.
- One square kills H⁻mom: m^{2k} ≫ N(Ckm)^k because (m/(Ck))^k = exp((1+o(1))L) ≫ X/log X.

All correct.

**Novelty: near‑tautology / restatement of the T1 control.** "A mechanism that cannot tell primes from primes ∪ {sparse odd
squares} fails" is exactly the existing control "any argument must pass odd squares (T1)". The doc's own limitation is the
decisive one: M_BM(s²) = M_gen(s²) = 0. So the barrier does **not** touch the campaign's actual route (∗) R ≥ εM, nor any
argument that feeds AP statistics through the genus main term. It bars only "AP statistics alone ⇒ T > 0 at every sequence
member", a method nobody proposed. The header phrase "black‑box stability barrier" is acceptable only together with that
limitation, and the doc does state it.

**m2.** §4.2 says the squares "violate the independently supplied prime‑only theorem M_gen ≫ log²n". The M_gen bound
(z48 Thm 5.4) is CONDITIONAL on a zero‑free strip, as the doc says in §1. The unconditional theorem is M_BM ≫ log²p
(FRONTIER Thm 2.2). Relabel it.

**m3.** §5's assessment cites "Theorems 4.1–4.3". There is no Theorem 4.3; the results are Thm 4.1, Cor 4.2 and Prop 4.3.

## 4. Proposition 4.3

Correct: each changed value L_i(t) ∈ AΔA′ has at most one preimage t when a_i ≠ 0. A union bound gives kK(Z), with a weight
of at most (log Z)^k. The growing‑k remark, (log Z)^k = X^{a+o(1)} for k = aL/log L and log log Z ~ log log X, is correct.
Grade: **trivial lemma**. The doc correctly declines to claim any non‑implication from HL to ES.

## 5. Theorem 5.1, Corollary 5.2, Theorem 5.3 (H⁻crit)

**Thm 5.1.** Correct. F is integer‑valued, so F ≤ ηm ⇔ F ≤ ⌊ηm⌋, and the deficit is at least d. Markov then gives
#bad ≤ N(k/A)^k. The single‑atom extremiser is also correct. This is Markov plus its equality case, not a theorem of
substance.

**Cor 5.2.** Correct.
- y = t/k gives y − log y = log(A/t), so −y e^{−y} = −t/A, so y = −W₋₁(−t/A).
- k(log(A/k)) is unimodal with its maximum at A/e, so E < 1 exactly between the two roots.

Numerical check of (5.4) with c=0.1, C=1, η=1/4, N = e^L/(2L), using mpmath's `lambertw` branch −1 (root residual
< 10⁻⁸ t). The denominator error L/k* − D_L is:

| L | 10² | 10³ | 10⁴ | 10⁶ | 10⁹ |
|---|---|---|---|---|---|
| L/k* − D_L | −0.279 | −0.124 | −0.074 | −0.020 | +0.008 |

So it is o(1), as claimed, though only slowly.

**Thm 5.3.** The implication is correct. For fixed δ > 0, k_X lies strictly between the roots for large X. The ceiling
shifts k by ≤ 1, while the gap to k* is ≍ δL/log²L. The final step uses only M_BM ≪ log²p.

**m4 ("slightly weaker hypothesis" is not proved, and true only after changing C).** The doc asserts that H⁻crit is weaker
than z48's H⁻mom without proof. The two are moments of *different* orders. Lyapunov gives
H⁻mom(c,C) ⇒ μ_{k₁} ≤ (Ck₁m)^{k₁}·(k₂/k₁)^{k₁}·O(1). Here k₂ = L/log L, k₁ is the H⁻crit order, and the factor
(k₂/k₁)^{k₁} ≈ exp(L(log log L + κ − δ)/log²L) → ∞. So H⁻mom(c,C) does **not** imply H⁻crit(c,C,η,δ) at the same C. It
implies H⁻crit(c,C′,η,δ) for every C′ > C, because (C′/C)^{k₁} beats that factor and the O(1) change in normalisation
(π(2X) against N_X). This should be stated, and it is the correct sense of "weaker".

**m5 ("safely above the critical value" holds only astronomically far out).** z48's k = L/log L exceeds k* iff
log log L + κ > 0 + o(1), where κ = log((1−η)²c/C). For c=0.1, η=1/4, C=1 that needs L ≳ e^{17.8} (X ≈ e^{5·10⁷}). For the
unconditional BM‑scale c ≈ 1/(32π²) it needs L ≳ e^{400}.

My script measured k₁·log(k₂/k₁) for c=0.1, η=1/4, C=1, δ=1. It is negative for every L ≤ 10¹⁵ that I tested, so the
H⁻crit order is *larger* than z48's order throughout any computable range. Everything is eventual, so this is not an error.
But "lowered by a second‑order amount" is purely asymptotic and should be said.

**m6 (sharpness at η=0 lies outside H⁻crit's range 0<η<1).** For η > 0 and +δ, the permitted atom is F = ⌊ηm⌋, not a zero.
A zero is permitted only when δ ≳ 2 log(1/(1−η)). The doc states the η=0 caveat. Keep it explicit and do not cite this as
"H⁻crit is sharp for zeros".

**Novelty.** Thm 5.1, Cor 5.2 and Thm 5.3 together retune the order of z48 H⁻mom by a factor 1 + O(log log L/log L), with
sharpness only for one displayed moment. It is not a new reduction, and no hypothesis here is more plausible than z48's
in any meaningful sense. Grade: **near‑tautology (Markov + calculus)**.

## 6. Other remarks

- **m7.** The "Hostile review (completed)" paragraph cites a deep‑mode internal review, but the branch has no review file
  (`reviews/` has nothing for ltastra2, and the commit touches only five files). Either commit the review or soften the
  paragraph.
- The controls (hard primes, squares, numerator 8) are irrelevant to every claim here, since none is a positive mechanism.
  Running them is harmless, and the doc says so.
- Cramér/presieved §4.4: correct (Borel–Cantelli II; s² with s prime survives any z(n) < √n). These are trivial.

## Bottom line

The document is mathematically sound and mostly candid in its Assessment paragraphs, with promise 1/5. Its results are:

- an import‑translation (Thm 2.1 / Cor 2.2), weaker than the already‑recorded sterile theorem;
- three elementary lemmas (Prop 3.1, Thm 4.1, Prop 4.3);
- a Markov/Lambert‑W retuning of z48's moment hypothesis (§5).

None qualifies as a new z49 proof step. Fold in m1–m7. Above all, M1 should be reflected in the header: Thm 2.1 is "a
corollary/re‑reading of STERILE Thm 6.3 for the R/B menu", not a new barrier. The exact gap is unchanged from z48: a
one‑sided estimate for the non‑real remainder at a fixed prime.
