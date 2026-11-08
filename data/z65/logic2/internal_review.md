# Internal hostile review of `Z65_LOGIC2.md` (lane LOGIC2)

Reviewer: nested side agent (review only; memo not modified). Inputs read in full: `Z65_LOGIC2.md`, `Z64_UNPROV.md`
(all of it, in particular §§1–2, 5–6), the relevant parts of `Z58_LOGIC.md` (§1 definitions, §4 census, §6.1),
`Z57_SYNTH.md` Lemma A.1, `Z57_BFII.md` Prop 2.2 / Cor 2.3, `Z58_WILDCARD.md` (CONV-II-15), ET (`sources/elsholtz-tao-1107.1010.pdf`,
Prop 1.6, Prop 1.9 and the "solvable by polynomials" definition), `data/z65/logic2/lit_verify.md`, and the Jeřábek
author PDF (`jerabek_2010_abelian_qr.pdf`, via pdftotext).

## Verdict

* **No FATAL issue.** Thm P, Lemmas 2.1–2.2, Cor P.1 and Thm T (Lemmas 3.1–3.5, the perturbed arc, Type I/II, ES★) are
  correct as mathematics. A few slips in intermediate claims do not affect the conclusions (MINOR m1–m5).
  Props 4.1–4.3, Lemma 4.0, Props 5.1–5.4 and Remark 5.6 are also correct.
* **2 MAJOR issues.** Both are scope and labelling problems in the "reading" layer, not errors in the theorems.
  * M1: the inference in Prop 5.5(b), "arc refutations of ES are possible only at square-mimicking n", is invalid, even
    CONDITIONAL on CONV-II-15. The correct dividing line is *polynomial solvability* (ET Prop 1.9), not pointwise
    Type II existence. A short exact replacement is given below, and it is PROVED.
  * M2: brief (2) is answered with unproved superlatives ("the weakest natural axiom …"), and "square-compatible ⟹
    nothing in the T1 transfer conflicts / construction artefacts" is stated as fact.
* **22 MINOR issues**, with concrete fixes.
* All three scripts reproduce byte-identically. Independent reviewer checks (below) pass.

## Replay (all under `ulimit -v 4000000`, `timeout ≤ 1800`)

| command | result |
|---|---|
| `gcc -O2 scripts/z65_logic2_t1all.c && ./a.out 3000` | `M=3000 N=9000000 triples=269405802 squares_tested=3000 square_hits=0`, **identical** to `t1all_3000.txt` |
| `uv run --with sympy python scripts/z65_logic2_onlyprime.py 200` | **identical** to `onlyprime_200.txt` |
| `uv run --with sympy python scripts/z65_logic2_landing.py 200 6565` | **identical** to the first block of `landing_check.txt` (ALL PASS). The four negative-control lines at the end of the data file are not produced by the script (see m21). |

The scripts were also read. K2 uses the correct law: it enumerates S_ℓ directly, so it does not depend on the "2-to-1"
slip (m1). K1 implements exactly the CRT recipe of Lemma 3.5(iii). It tests only Y ∈ ℤ[β₁, β₂] (k = 2), so step (i)
(choosing b′) is not exercised; that step is proved, and the gap is harmless.

### Independent reviewer checks
1. **Negative control for Lemma 3.5, rewritten from scratch** (`/tmp` snippet, reproduced here; seed 7, D = 840,
   landing without the P-avoidance step):
   ```python
   import random; from math import gcd
   rng = random.Random(7); D = 840
   YS = {"b1+3": lambda x,y: x+3, "b1*b2+13": lambda x,y: x*y+13,
         "b1^2-b2^2+7b1b2-3": lambda x,y: x*x-y*y+7*x*y-3, "n+b1": lambda x,y: x*x+y*y+x}
   for name, Y in YS.items():
       bad = tot = 0
       for _ in range(4000):
           while True:
               s0, t0 = rng.randrange(D), rng.randrange(D)
               if gcd(s0*s0+t0*t0, D) == 1: break
           s = s0 + D*rng.randrange(1,200); t = t0 + D*rng.randrange(1,200)
           if gcd(s,t) != 1: continue
           ell = s*s+t*t; b1, b2 = s*s-t*t, 2*s*t
           tot += 1; bad += gcd(Y(b1,b2), ell) > 1
       print(name, tot, bad)
   ```
   Output: b1+3: 29/3878; b1*b2+13: 118/3876; b1²−b2²+7b1b2−3: 37/3873; n+b1: 0/3879. These match the lane's 33 / 121 /
   37 / 0 in order of magnitude. n + b1 is structurally 0, because gcd(b₁, ℓ) = gcd(s² − t², s² + t²) = 1. **So the
   P-avoidance step is necessary and the K1 test is not vacuous.**
2. **Law of (a₁, a₂) mod ℓ.** |S_ℓ| = 4, 36, 64 for ℓ = 5, 13, 17, i.e. (ℓ − 1)²/4. The ratio ℓ²/|S_ℓ| is 6.25 at
   ℓ = 5, 4.69 at 13 and 4.52 at 17. For ℓ = 3, 7, 11 the ratio is 2.25, 2.04, 2.02. This confirms m1/m2.
3. **T1_II at even squares (sanity only).** Brute force of 4abcd = a + b + m²c over a, c ≤ 3000 (all d with
   4acd − 1 ≤ a + m²c), m ≤ 60, odd and even, found **0** solutions. The search is not exhaustive in c, so this is a
   sanity check, not a certificate. The proof is in m6.
4. **Profile coverage probe for M1.** The profinite unit π with π₁₁ = 2 and π_p = 1 for every p ≠ 11 is a non-residue
   only at 11. It lies in the ET Type II class −4a²d mod f, 4ad | f + 1, with (a, d, f) = (4, 1, 143): π ≡ 79 ≡ −64
   (mod 143). The search covered a, d < 60, f ≤ 2·10⁵, f ≡ 0 (mod 11). So this particular non-square profile *is*
   polynomially solvable, consistent with the memo's expectation. The general question is open (M1).
5. **Jeřábek PDF re-read.**
   * Thm 5.7: QR, both supplementary laws and multiplicativity, in T⁰₂ + Count₂(PV) and IΔ₀ + Count₂(Δ₀), for distinct
     odd primes p, q of the model.
   * Def 5.2: the Legendre symbol is defined by squareness.
   * Thm 5.8: the Jacobi symbol is Δ₀-definable in IΔ₀, and its laws are proved in IΔ₀ + Count₂(Δ₀).
   * Thms 4.2, 4.6, 4.7 are as quoted. Intro p. 1–2: PWW, B–I and C–D are quoted correctly.
   * **The memo misses one item.** Directly after Thm 5.7 (p. 20), Jeřábek remarks that B–I's Lagrange proof uses only
     multiplicativity, so **Lagrange's four-square theorem is provable in IΔ₀ + Count₂(Δ₀)**. See m15.

## Step-by-step verification log (what was checked and found correct)

* **Lemma 2.1.** S is open by continuity, closed by positive closedness, and [0, ∞) is connected. ✓ (Relative version:
  see m4.)
* **Lemma 2.2.**
  * (a) 4C_j ≥ 1/u_j + 1/B_j with C_j bounded gives u*, B* > 0. Then 4u*B*C* ≥ u* + B* > 0 and C* ≥ 0 give C* > 0. ✓
  * (b) is analogous, using s²c ≥ 0. ✓
* **Theorem P.** (F4) gives integer specialisation and Lemma 2.3 gives the arc. γ = ψ(X̄, Ȳ) lies on V_Σ(ℝ) because ψ
  is a ring homomorphism. The X_i are eventually positive, and Lemma 2.1 gives X̄(b) > 0, hence ≥ 1 as integers. ✓
  Lemma 2.3(c), which needs b₁ ≥ 1, is not used. ✓
* **Integer facts for Cor P.1.**
  * m = 0: 4uBC − u − B ≥ 4uB − u − B = u(2B − 1) + B(2u − 1) > 0. ✓
  * R(m²) = 0 for all m ≥ 1: Lemma A.1(b) is indeed stated "for every m". ✓
  * N_II(m²) = 0 for all m ≥ 1 is true, but the cited source only states odd m (m6).
* **"ES(1) suffices".** In M_{q*} with q* = 1, b = (1, 1, …, 1) is admissible. Lemma 2.3(c) applies (b₁ = 1), and
  Lemma 2.4 gives a positive solution of 4/1 = Σ 1/x_i ≤ 3. ✓ Scope: see m10.
* **μ.**
  * The norm ℤ_ℓ[i]^× → ℤ_ℓ^× is onto for odd ℓ, both split and inert. For ℓ = 2 its image is 1 + 4ℤ₂. Signs can be
    chosen per prime-power component. ✓
  * The squares of units are open, so every conditioning event is open with positive measure. ✓
* **Lemma 3.1.** ϕ(n) = N(w²) = N(w)². The congruence mod q passes through the norm polynomial. n is irreducible over
  ℚ, and primality in M follows by (F1), since ϕ(n) is a unit. ✓
* **Lemma 3.2.**
  * Reduction: ϕ(g) ∈ Ẑ^×. A ℚ[β]-factorisation lifts to M after rescaling by c_i, with (c₁c₂)⁻¹ ∈ ℚ ∩ Ẑ^× = {±1}. ✓
  * The probability lower bound holds. The intermediate counts are slightly wrong (m1), but the inequality survives.
  * F₁ exists (m3 for the odd-e gap). G₁ ≁ s ± it. Chebotarev applies to L(i), Noether gives absolute irreducibility of
    the reductions, and Lang–Weil gives ≥ 1/(2ℓ) on a set of positive density. ✓
  * Independence across ℓ plus Borel–Cantelli II, over countably many f. ✓
  * Constants and ±1. ✓
* **Lemma 3.3.**
  * (G1) holds under absolute continuity; the constant is wrong (m2) but harmless.
  * (G2) holds with any bounded point-mass ratio.
  * PD: ϕ(g) ∈ Ẑ^× forces g = ±n^e (all ℚ[β]-factors must be ~ n a.s.). ✓
* **Lemma 3.4.**
  * TS holds: the positive primes are the ℓ and n, and β₁, β₂ ∈ M. ✓
  * E(−1) fails: algebraic elements of A[β₃, …] lie in A, and the graded-domain top-degree argument applies. ✓
  * PB and QR_std fail by Props 4.1 and 4.2. Primes are not cofinal. ✓
* **Lemma 3.5.** Checked line by line:
  * (i) a nonzero polynomial over an infinite domain does not vanish on a grid. ✓
  * (ii) G ≡ 0 would give β₁ + iβ₂ | Y′, hence by conjugation n | Y′. ✓
  * (iii) CRT. gcd(s, t) = 1, including primes r | D, via s₀² + t₀² being a unit. s² + t² is coprime to every r ∈ P.
    b ≡ a (mod D) via (s + it)² ≡ (s₀ + it₀)². ✓
  * (iv) 𝔯 | s ± it; b₁ ≡ −2t², b₂ ≡ ∓2it²; Y(b) ≡ G(t²) or Ḡ(t²) (mod 𝔯); 𝔯 | G(t²) ⟹ r | N(G(t²)) ⟹ r ∈ P. ✓
  * b₁ ≠ 0, since s = ±t would force ℓ = 2.
* **Thm T proof.**
  * Type split. ✓
  * Perturbed arc: the extra term is O((1 + s)e^{−s}), so Lemma 2.3(a),(b) survive. ψ(β₁) has finitely many zeros on
    (0, ∞), each excludes one λ, and ψ(n) > 0 on [0, ∞). ✓
  * Lemma 2.4 then gives a Type I solution at ℓ² with ℓ² | x₀ and gcd(ℓ², y₀z₀) = 1, contradicting ET Prop 1.6. ✓
  * Type II likewise. ✓
  * ES★: the unperturbed arc has ψ(n) ≥ 0, Lemma 2.2(a) is the relative closedness, and R(ℓ²) = 0. ✓
* **Lemma 4.0.**
  * (a) Discreteness: k(c − j) = a − kj fixes the position of c. ✓
  * (b) Integer square root, then a degree comparison in the ordered field ℚ(β₁) ⊂ Frac(M). ✓
* **Prop 4.1.** Krull height ≤ 1 < k = dim, so F is not a field. Every element of F is k⁻¹ā. ✓
* **Prop 4.2.** The algebraic closure of ℚ in a finitely generated field is finite. Algebraic elements of A[β_{∉J}]
  lie in A. ✓
* **Prop 4.3.** The top form of a sum of squares of real forms is nonzero, of degree 2δ. ✓
* **§4.4.** i = AB⁻¹ (mod n), and B·1 − β₂·A = 1. ✓
* **Prop 5.1.**
  * ψ(d)ψ(y) = ψ(x)² + ψ(n) > 0 on [0, ∞) and ψ(d) is eventually positive, so ψ(d) > 0 and d₀ ≥ 1 with d₀ ≡ 3 (mod 4).
  * There is a prime r ≡ 3 (mod 4) dividing d₀, with r ∤ m, and −1 ≡ (x₀/m)² (mod r), a contradiction. ✓
* **Prop 5.2.** Witnesses exist at n = m² (Hensel; (ℓ*/r) = (r/ℓ) = 1). ✓ The caveat (fourth powers mod ℓ ≡ 1 (4)
  when ℓ | D) is correct: for ℓ ≡ 3 (mod 4) exactly one of ±m is a residue.
* **Prop 5.3.**
  * (a) n = Bd − u, so n ≡ −u (mod d), and (−u/d) = −1. ✓
  * (b) x₀² ≡ −s² (mod d). ✓
  * (c) Proved via n ≡ −4a²d (mod f) and (−d/f) = −1. ✓
* **Prop 5.4.** For a finite part, c = s′² with s′ ≡ s (mod q) and s′ coprime to L; Dirichlet; compactness over the
  elementary diagram. ✓
* **Remark 5.6.** If π = N₀ with |N₀| > 1, then every ℓ | N₀ divides n. (This is just "the profile of a nonstandard
  prime is a unit".) 8 813 281 mod 840 = 1. ✓
* **§6 JNR sketch.**
  * The least-square-root map [1, p − 1] → [1, (p − 1)/2] is injective if every unit is a square, and that is
    exactly an iWPHP instance.
  * d by CRT; (p/d) = (d/p) by Thm 5.8, since p ≡ 1 (4). ✓
  * As an Assessment, fine.

## FATAL

None.

## MAJOR

**M1. Prop 5.5(b) does not establish "arc refutations of ES are possible only at square-mimicking n". The same applies
to the ES★ clause, the abstract (iv), the F3 row, the §5 narrative and the §8 bullet.**

The argument shows only that a refutation whose contradiction is *pointwise* cannot work at non-square landing values N.
Pointwise means: transfer one hypothetical solution to one integer N and contradict "N has no solution". But arcs also
support a *global* contradiction: transfer the hypothetical solution to a whole arithmetic progression of landing values
and contradict *polynomial non-solvability*. CONV-II-15 says nothing about that. The following is PROVED with the
memo's own tools, U64 (F4) and Lemmas 2.3–2.4.

> **Criterion.** Let M_ϕ be a U64-type model with n = β₁ and π := ϕ(β₁) ∈ Ẑ^×. Then
> M_ϕ ⊨ ES(n) ⟺ π lies in some primitive residue class r mod D that is solvable by polynomials (ET p. 7–8).
>
> *Proof.*
> * (⇐) Let P₁, P₂, P₃ be the polynomials of the class.
>   * They are integer-valued on a tail of the AP r + Dℤ, hence on the whole AP (Newton basis). By continuity
>     P_i(π) ∈ Ẑ, so P_i(β₁) ∈ M.
>   * Their leading coefficients are positive, so P_i(β₁) ≥ 1 in M.
> * (⇒) Let X, Y, Z ∈ M, all ≥ 1, solve ES(n). Take D from (F4) and fix b′ ≡ a′ (mod D). Put P_X(t) := X(t, b′),
>   and similarly P_Y, P_Z.
>   * For integers t ≡ π (mod D) with t ≥ 1, (F4) makes P_X(t) ∈ ℤ.
>   * Lemma 2.3 (b₁ = t ≥ 1, so ψ(β₁) > 0) and Lemma 2.4 make P_X(t) > 0.
>   * The identity 4P_XP_YP_Z = t(P_XP_Y + P_YP_Z + P_ZP_X) holds in ℚ[t].
>   * So π mod D is solvable by polynomials. ∎
>
> With compactness of {π ∈ Ẑ^× : π ≡ r (mod q)}, and U64 Thm B including its threshold proviso:
> **NOI ⊢ ∀n ≥ N₀ (n ≡ r (q) → ES(n)) for some N₀ ⟺ r mod q is a finite union of polynomially solvable classes.**
> Moreover, NOI ⊢ ES_prime[r mod q] implies the right-hand side.

So the real dividing line for refutations is the **union of ET's Prop 1.9 families**, not square-mimicking. The latter is
contained in the uncovered set by ET Prop 1.6 (Mordell–Schinzel).
* **If** some non-square-mimicking unit profile lies in no family class, the U64 model refutes ES at β₁ there by an arc
  argument. That would hold even if CONV-II-15 is true, since a pointwise Type II solution at every landing N is
  compatible with polynomial non-solvability. Prop 5.5(b)'s conclusion would then be false.
* **If** every non-square-mimicking profile is covered, the conclusion is true *unconditionally* (by Thm B, ES then holds
  at every such n in every model of OI). CONV-II-15 is then irrelevant.

Either way CONV-II-15 is the wrong hypothesis. Whether the families cover every non-square-mimicking unit profile is a
concrete profinite covering question, essentially U64 O3. Check 4 shows that one natural test profile is covered. The
uncovered set is closed, but could be a nonempty null set; I could not settle it.

*Fix.*
* Replace Prop 5.5(b) by the Criterion above, labelled PROVED, with the proof sketch.
* State the open covering question as a new O-item: "does every unit profile that is not a square in Ẑ^× lie in an ET
  Prop 1.9 family class?" (generalises U64 O3).
* Restate Prop 5.5(b), if kept, as being about *pointwise* landing refutations only, still CONDITIONAL on CONV-II-15.
* Remove "the counter-models are confined to square-mimicking primes" from F3, the abstract (iv) and §8, or make it
  conditional on the covering question.
* Same for ES★. The relevant notion is (★)-polynomial solvability: classes −u mod (4uC − 1) with u | (d + 1)/4, the
  symmetric ones, and n ≡ −(u + B) (mod 4uB) from the C-linear degree pattern. Also note that the ES★ evidence cited
  (Z58_LOGIC census) covers only n ≡ 1 (mod 4) (m18).
* Bonus: the Criterion also generalises U64 Cor C from modulus 840 to all moduli. That is worth recording.

**M2. The brief-(2) answer is stated with unproved superlatives and an unproved "no conflict".**
* §7, the §8 bottom line, the FRONTIER text (iii) and the abstract (iv) say:
  * "the weakest natural axiom it cannot accommodate is PB";
  * "the weakest natural principle that defeats every arc counter-model is … NR";
  * PB/TS/E(−1)/QR_std/Lag are "square-compatible; nothing in the T1 transfer conflicts with them", "so they are
    construction artefacts, not T1 conflicts".
* None of this is proved.
  * "Weakest" presupposes a comparison. The candidates are pairwise incomparable: PB vs E(−1) vs Lag; NR vs ES★ vs ES.
    No minimality argument is given.
  * For PB the honest statement is stronger and cleaner. **Bez fails in every polynomial-type model**: kβ₁, k′β₂ ∈ M
    have only constant common divisors, and ukβ₁ + vk′β₂ has no constant term (U64 §2.6's argument). So "weakest" is
    really "PB is the weakest of the axioms *we tested* that is still excluded".
  * Other natural arc-killers exist. Example: the negative Pell principle "every prime p ≡ 1 (4) has x² − py² = −1"
    (Legendre). At n = m², x₀² − m²y₀² = −1 forces m = 1. So it kills every arc whose landing value is not 1, i.e. every
    arc counter-model at a profile ϕ(n) ≠ 1. It does not kill arcs at ϕ(n) = 1. NR is therefore not singled out by any
    proved property except "kills arcs at all profiles, including 1".
  * Prop 5.2 proves only that integer witnesses exist at suitable odd squares. Whether the witness relations admit arcs
    *jointly with* the model's other elements is exactly O1′, which §7 itself calls OPEN. "Nothing conflicts" therefore
    contradicts §7's own parenthesis.
* *Fix.*
  * Relabel these readings as **Assessment**.
  * Rephrase: "PB is the weakest axiom among those examined that the polynomial construction excludes (Bez is excluded
    outright)", and "NR is a natural true principle that kills every arc counter-model (Prop 5.1); negative Pell kills
    those at profiles ≠ 1".
  * Replace "nothing in the T1 transfer conflicts with them" by "their witness relations have integer points at
    suitable odd squares (Prop 5.2); whether arcs exist in models of them is O1′".

## MINOR (with fixes)

* **m1 (Lemma 3.2 Claim).** "w ↦ w² is 2-to-1 on 𝔽_ℓ[i]^×" is false for ℓ ≡ 1 (mod 4): 𝔽_ℓ[i] ≅ 𝔽_ℓ × 𝔽_ℓ, the
  kernel is {±1}², the map is 4-to-1, and |S_ℓ| = (ℓ − 1)²/4. The bound used is still correct, because
  (fibre size)·|S_ℓ| = |𝔽_ℓ[i]^×| ≤ ℓ² in both cases.
  *Fix:* state P(ℓ | f(a)) = #{(s, t, z) : s² + t² ≠ 0, F ≡ 0}/(|𝔽_ℓ[i]^×|·ℓ^{k−2}) ≥ #{…}/ℓ^k.
* **m2 (Lemma 3.3).** "density ≤ 2ℓ²/(ℓ − 1)² ≤ 4.5" is wrong. The point-mass ratio is 4ℓ²/(ℓ − 1)² for ℓ ≡ 1 (4)
  (= 6.25 at ℓ = 5) and 2ℓ²/(ℓ² − 1) for ℓ ≡ 3 (4) (Check 2). For ℓ | 2q it is some finite constant. Any bounded
  constant suffices.
  *Fix:* replace by "≤ 4ℓ²/(ℓ − 1)² ≤ 6.25 (ℓ ≥ 5 odd, ℓ ∤ q); bounded at the finitely many ℓ | 6q".
* **m3 (Lemma 3.2, "F = c(s² + t²)^e").** The argument "s² + t² ∉ ℚ[s² − t², 2st] (degree-2 part)" only excludes
  e = 1.
  *Fix:* use u = s + it, v = s − it. Then ℚ(i)[s² − t², 2st] = ℚ(i)[u², v²] and s² + t² = uv, so (uv)^e lies in it only
  for e even.
* **m4 (Lemma 2.1 vs its use).** Thm T's ES★ step applies Lemma 2.1 to Σ★, which is only "positively closed over
  σ ≥ 0".
  *Fix:* state Lemma 2.1 for a closed constraint set C (here σ ≥ 0) with γ ⊂ C.
* **m5 (Lemma 2.2(a) wording).** "Positively closed over σ ≥ 0" is not covered by the Definition.
  *Fix:* add a one-line relative definition.
* **m6 (T1_II at even m).** Cor P.1 needs N_II(m²) = 0 for *every* m ≥ 1, since T1_II quantifies over all s. Z57_BFII
  Prop 2.2 and Cor 2.3 state only odd n / odd m, and Z58_WILDCARD's "every m" is a paraphrase. K3 tests R only. The
  proof does extend verbatim:
  * 4acd ≡ 1 (mod f) makes a, c, d units mod f;
  * n ≡ −4a²d (mod f) gives (n/f) = (−d/f) = −1, using f ≡ −1 (mod 4d) and Jacobi reciprocity;
  * this is impossible for n = m², since n is a unit mod f.
  Check 3 found no solutions for m ≤ 60.
  *Fix:* add this two-line argument (it also covers Prop 5.3(c)).
* **m7 (Prop 4.1 / §4.2 Remark parenthetical).** "IΔ₀ ⊢ IE₁ ⊢ Bez already rules out polynomial-type models by Prop 4.1"
  overreaches: Prop 4.1 only excludes those *with nonstandard primes*. But Bez fails in **every** polynomial-type model
  (kβ₁, k′β₂, see M2).
  *Fix:* add this as Prop 4.1′. Then the parenthetical and the §6 rows ("not polynomial-type") are literally correct.
* **m8 (abstract (v)).** "… so no polynomial-type model exists" is attributed to QR. Prop 4.2 only excludes
  square-mimicking nonstandard primes.
  *Fix:* cite Prop 4.1′ (Bez) or Prop 4.3 (Lag; see m15).
* **m9 (§5, "(S) … is not expressible in L_or").** This is false as written. By Jeřábek Thm 5.8 the Jacobi symbol is
  Δ₀-definable in L_or over IΔ₀.
  *Fix:* "not expressible by an existential/polynomial system (so arcs do not apply directly); it is Δ₀-expressible over
  IΔ₀".
* **m10 ("ES(1) suffices").** "ET Prop 1.6 is needed only for q* ≠ 1" holds for U64 Thm A (M_{q*}). It does not hold
  for Thm A′ or Thm T, whose generic residues forbid landing at 1. Also, (MS) in this repo is the Hit / (★) form
  (`Z58_LOGIC` §1). The most direct transport is therefore "4uBC − u − B ≥ 2 > 1", i.e. R(1) = 0.
  *Fix:* scope the sentence to NOI ⊬ (MS) / U64 Thm A, and mention R(1) = 0.
* **m11 (§6 JNR).** "It is a Δ₀ statement in IΔ₀" should read: a Π₁ sentence ∀p θ(p) with θ Δ₀ (Thm 5.8).
* **m12 (§6, NR status).**
  * NR has explicit polynomial witnesses on non-square classes. For p ≡ 5 (8): d = (p + 1)/2 ≡ 3 (mod 4), x = 1, y = 2,
    and 2d − p = 1. For p ≡ 2 (3): d = 3. So OI proves NR there.
  * Only square-mimicking-type classes carry content, where Prop 5.3(b) forces a nonstandard d.
  * "IΔ₀ + exp ⊢ NR is OPEN" is fine as stated. Add "expected yes (genus theory for disc −4p is finitary; Friedman's
    grand conjecture), Assessment".
* **m13 (§6 IΔ₀ + exp row).** FLT/Euler are cited from S²₂ + iWPHP(PV) + PHP(PV) without saying that this theory is
  contained in IΔ₀ + exp.
  *Fix:* add "(S²₂ ⊆ IΔ₀ + Ω₁; iWPHP and PHP for PV/Δ₀ maps are provable in IΔ₀ + exp, standard, Assessment)", or
  move the item to its own row.
* **m14 (Otero remark, §3.2).** "So TS-type witnesses can be added to *arbitrary* NOI models" overstates the abstract,
  which gives one representation of one element a per extension. A TS model would need an ω-chain, which may destroy
  primality or create new primes.
  *Fix:* "a single element can be given a representation x² + by² in an NOI extension (Otero)".
* **m15 (§6 table).** Missing: Jeřábek p. 20 says Lagrange is provable in IΔ₀ + Count₂(Δ₀).
  *Fix:* add this to the IΔ₀ + Count₂(Δ₀) row ("Lag holds ⟹ no polynomial-type model, Prop 4.3"). Note also that
  Jeřábek's body text gives B–I's Lagrange as IΔ₀ + iWPHP(IΔ₀), while the intro says WPHP(Δ₀).
* **m16 (Prop 5.2 statement).** It is stated for m ≡ 1 (mod D). Arc landings need m² ≡ ϕ(n) (mod D), with sign
  choices per prime-power component.
  *Fix:* state it for m with m² ≡ ϕ(n) (mod D), prime factors ≡ 1 (mod 8∏_{ℓ∈L, ℓ∤D} ℓ) and the caveat's condition
  for ℓ | D. Note that TS/E(−1)/PB/Lag need only prime factors ≡ 1 (4), which a suitable sign of m mod 4 allows.
* **m17 (Prop 5.5(a)).** D₀ = 30ℓ^e or 240 gives coprimality to 15 only. The ES★ clause needs 105.
  *Fix:* D₀ := 210ℓ^e or 1680 for that clause.
* **m18 (Prop 5.5(b) ES★ evidence).** The Z58_LOGIC census (and hence "last ones 12 538 801, 17 401 609, 29 210 401")
  covers only n ≡ 1 (mod 4). Profiles ≡ 3 (4) are not covered by that evidence, and R has prime zeros ≡ 3 (4) (e.g.
  6 266 527).
  *Fix:* restrict to π ≡ 1 (4) or cite data. This is moot after M1.
* **m19 (F4 row).** "Hence n = ϕ(n)·unit reducible" is wrong wording.
  *Fix:* "every standard prime factor of ϕ(n) divides n in M, so n is not prime" (as Remark 5.6 says).
* **m20 (F1 row; §5 after Prop 5.1).**
  * "NR is false at every odd square": it is the *witness relation* of NR that has no integer point at any perfect
    square (any parity, Prop 5.1).
  * "The (★) system (T1) … are the examples": T1 is the universal non-existence fact; the arc-killing *principle* is
    ES★ (existence of (★)-witnesses).
  *Fix:* wording.
* **m21 (§10 replay).** "The two negative-control blocks … produced by inline snippets (seeds 1, 2), whose code is
  reproduced in the review file." That code is not in the repo, and the data file has four control lines, not two
  blocks.
  *Fix:* either commit the lane's snippet into `scripts/z65_logic2_landing.py` (e.g. a `--no-avoid` flag), or point to
  the reviewer's independent control above (Check 1; same qualitative result).
* **m22 (§7 last bullet / §8 "message").** "A proof must produce … a certificate *in the specific shape* −p ∈ H_d (or
  another Type I/II shape)" is close to tautological. By Z57_SYNTH Lemma A.1 and Z57_BFII Prop 2.2, every (★)/Type II
  solution *is* such a certificate. So "a proof of ES must produce shaped certificates" restates "a proof of ES must
  produce solutions". The non-tautological content is Prop 5.3: at square-mimicking primes the modulus is nonstandard.
  *Fix:* say so, and keep the "logic ladder locates B2" sentence as Assessment.

## Items checked and correct (no action)

* Results table rows and labels, apart from those touched by M1, M2, m7, m8 and m15.
* Literature claims vs `lit_verify.md` and the PDF:
  * Jeřábek Thms 4.2, 4.6, 4.7, 5.7, 5.8 and Def 5.2: VERIFIED.
  * Otero 1993 (abstract): as quoted.
  * Mohsenipour 2006 (talk abstract) and Wilmers "as reported": labelled PARTLY, correctly.
  * Smith 1993 "PID ≠ ℤ": a nonstandard UFD element has a nonstandard prime factor, so "infinite primes exist" follows. ✓
* "OI + Bez ⊢ PB" ✓.
* NR true in ℕ via Dirichlet + QR ✓. QR_std true in ℕ ✓.
* Prop 5.2 caveat on fourth powers ✓.
* K2 / K3 / K1 numbers, and "2.7·10⁸ triples" (269 405 802) ✓.
* 8 813 281 ≡ 1 (mod 840) ✓.
* Remark "Whether M_ϕ satisfies Th_∀(ℤ, ≤) is OPEN": fair. I found no counterexample.
