# Hostile review since `side-agent/synthesis-two`

Reviewed endpoint: `feb51b72` (including the depth-aspect and sterile-steer work in the requested commit range, not only FF_MUTE).

## Verdict

**No fatal defect found in the qualitative one-mute-place existence theorem.** The identity, reciprocity reduction, character expansion, Weil estimates and large-Kummer-prime tail support existence unconditionally, including characteristic 2. The quantitative certificate bound, the description of the profinite sterile set, and several numerical claims need repair before the current package can be called fully verified.

The earlier DEPTH_ASPECT theorems survive this review at their stated relative scope. However, their synthesis contains a wrong measure limit, and STERILE_STEER's supposedly repaired golden-variant discussion still misses the square class of 5. Prior hostile-review labels do not discharge these defects.

Severity convention: MAJOR = false/unsupported mathematical or numerical conclusion, but repairable without losing the central existence theorem; MINOR = local proof/presentation defect or missing qualification. No source files were repaired in this review.

## Major findings

### M1. Prime-degree selection does not give the advertised additive-constant bound

Locations: `FF_MUTE.md:105–107,130–131,236–238,256–258`; `reviews/agent-reports/AGENT_REPORT_O195.md:11,51–52`.

The proof establishes positivity for every **prime** integer

`d ≥ 2 log_q n + C(q,A,h)`.

It then silently selects such a prime with `d ≤ 2 log_q n + O(1)`. That does not follow: primes have arbitrarily long gaps. As n varies, `2 log_q n` approaches every large real threshold arbitrarily closely, so its special form does not supply bounded prime gaps either.

The central existence conclusion is unaffected. A safe immediate replacement, using Bertrand, is `d ≤ 4 log_q n + O(1)`; using the prime number theorem one gets `d ≤ (2+o(1)) log_q n`. Corresponding shot-height upper bounds are `O(n^4)` or `n^{2+o(1)}`, not the currently advertised `C n²`. A separate argument allowing sufficiently general composite degrees would be needed to recover the sharper bound.

This is a proof gap in the claimed bound, not a counterexample to the possibility of a sharper theorem by another method. Also replace the informal strict `j < q^d` assertion by a proved bound allowing the lift needed for the degree inequality (e.g. `j = O(q^d+n+d)`).

### M2. The displayed profinite set is not sterile for all the allowed shot moduli

Location: `FF_MUTE.md:189–203` (Prop 5.4 and its Reading).

Prop 2.1 permits **composite** f. The Reading imposes `(−xA/f) = −1` only for **prime** f congruent to −1 modulo A. That excludes prime-modulus shots, not composite-modulus shots: a product can be −1 modulo A although none of its prime factors is.

Concrete counterexample to the claimed sterility of this set:

- Work over F₅, with `A=T`, `s=T+1`, `Q=s`, and `f=(T+2)²=T²+4T+4`.
- Then `f ≡ −1 mod A` and `−A Q² ≡ 2 mod f`.
- Choose a profinite unit x with `x ≡ 2 mod (T+2)²`. Independently, at every prime π satisfying `π ≡ 4 mod T`, choose its coordinate so that `−xT` is a nonsquare modulo π. These conditions are compatible: `T+2` is not one of those π.
- This x belongs to the displayed set, but the composite-modulus shot `(f,Q)` fires on it. The class contains monic irreducible P of arbitrarily large degree, where the small-Q version of the identity applies.

The **existence** of sterile points/no finite shot covering is readily repairable: impose nonsquareness at every prime π not dividing As, not merely at prime shot moduli. Every admissible composite f has such a prime divisor. For a finite list, apply CRT to its distinct prime-power factors, rather than assuming the distinct composite f are pairwise coprime.

Two related scope errors:

- “Yet no global ones”/“No polynomial P is such a point” is not an unrestricted statement: Thm 4.2 explicitly has global square failures when q ≡ 3 mod 4 and k is odd. In fact x=1 belongs to the displayed set for q=3, A=T. Say “no admissible irreducible P fails the mechanism,” not “no global points.” Nonconstant polynomials are not elements of R̂* in the first place, so distinguish the profinite-unit ambient space from actual polynomial inputs.
- “Invisible to **every congruence**/covering/compactness argument” is far stronger than no finite covering. The proof itself uses congruence characters and reciprocity. The valid obstruction concerns finite covers by the specified shot families, not all uses of congruences.

### M3. “Least shot height” is only least among prime-modulus shots

Locations: `scripts/fm_minq.py:1–4,65–68`; `FF_MUTE.md:228–232`.

The script factors the shot and tests each irreducible factor separately. It never tests composite divisors, although Prop 2.1 allows them. Its docstring does acknowledge the restriction; the paper and output labels do not.

Small exact counterexamples over F₃ with A=T², s=T+1:

1. `P=T²+1`, j=0 has the composite divisor `f=T²+2=(T+1)(T+2)` of `P+A`. The formulas give `X=1`, `Y=z=P`, hence `T²/P=1+1/P+1/P`, monic and NC. The script's first prime-modulus solution for this P is j=2.
2. Even if “shot” is restricted to the **strict large-Q hypotheses of Prop 2.1**, `P=T²+2T+2` has its first valid composite-modulus shot at j=5, whereas its first prime-modulus shot is j=11. A witness at j=5 is
   `f=(T+2)(T⁵+2T²+T+1)=T⁶+2T⁵+2T³+2T²+2`.
   It has `f ≡ −1 mod T²`, divides `P+T²(T+1)^10`, and `12 > deg P+deg f = 8`.

Thus the reported means/maxima are upper bounds for the general least shot height, not its exact measurements. Relabel throughout or enumerate all monic divisors. This affects claims about ES-integrality of “the least shots” too. Finite data also cannot establish that heights “do not grow with n”; say “show no growth trend in these ranges.”

### M4. Two numerical diagnostics give wrong answers

Locations: `scripts/fm_mute.py:40–41`; `scripts/fm_count.py:40,54–60`.

**False primitive-root flags.** The odd-characteristic test `2*ord(s²) == q^d−1` does not imply s is primitive when `q^d−1 ≡ 2 mod 4`. s may have the odd order `(q^d−1)/2`.

Explicitly, over F₃ take `s=T³+2T+1`, `f=T+2`. Then s mod f = 1, so its order is 1, but the script labels it primitive because `2*1=3−1`. This is one of the parameter sets in the committed numerical output. The orbit solver and verified identities remain valid; `s-primitive-at-chosen-f` does not. Compute ord(s), or add the missing quadratic-nonresidue test in odd characteristic.

**Characteristic 2 is mishandled in fm_count.** The script always divides δ by 2 and tests squares with exponent `(q^d−1)//2`. Neither is appropriate in characteristic 2. Reproduction:

`uv run python scripts/fm_count.py 2 10 11 3 111`

prints `G(d)=0`, while the true answer is 2: both irreducible cubics `T³+T²+1` and `T³+T+1` qualify; s=T+1 has order 7 in each field, and every nonzero element is a square. The correct main term is `8/3`, not `4/3`. Either implement the characteristic-2 branch or reject even p explicitly. The paper's characteristic-2 theorem is not invalidated by this script bug.

### M5. The golden-variant pattern argument omits n=5m²

Location: `STERILE_STEER.md:150–154`; inherited review assertion `reviews/sterile-steer-review.md:204–214`.

The text says that in V_φ the non-square pattern of **every non-square integer** is in the divergent regime. But the residue symbols here are over `K=Q(√5)`: 5 is a square in K, with square root `2φ−1` in O. Therefore `(5/𝔮)=1` at every odd prime ideal not dividing 5. Its non-square pattern is empty, not positive-density or divergent. The same applies to every 5m².

Repair to “positive integers nonsquare in K,” i.e. outside `{m²,5m²}`, and explicitly intersect with the eligible prime set `χ_{−φ}(𝔮)=−1`. The Chebotarev independence argument must be made over K. This exception is already recognized in T1_TEMPLATE/UNIT_ORBIT, so omitting it here is a genuine synthesis regression, not a new obstruction.

The old review's ancillary assertion that *any* infinite pattern can be thinned to make `Σ1/i_𝔮` finite is also unjustified without `1/i_𝔮 → 0` along a subsequence; it certainly fails on an infinite set with i_𝔮=1. Do not use that assertion as a general argument about sparse patterns.

### M6. Wrong limiting measure in the depth-aspect synthesis

Location: `DISCOVERIES.md:788`.

“The sterile measure on the line tends to 1/2” is not what DEPTH_ASPECT Thm 3.1 proves. Its displayed expression `(r−1)/(2r)−S(r)` is a lower bound for the sterile **nonresidue portion**, not an asymptotic for the whole line.

The square-unit half of the r-generic line is already sterile by T1: all its coordinates are local squares, hence it is a profinite square. Add that half to the proved nonresidue portion. The sterile measure on the whole unit line is at least `(r−1)/r−S(r)`, hence tends to **1** (and likewise after normalizing Haar measure on the units). Alternatively retain the theorem's limited claim: “the sterile nonresidue portion has measure tending to 1/2.”

### M7. The denominator-height comparison is unsupported and false as a bound on all certificates

Locations: `FF_MUTE.md:130–131,256–258`.

Prop 5.1 bounds the **modulus f of a Type II datum**, not the degrees of all its denominators. The final paragraph turns this into an ES_q certificate-height bound `2n−k+O(1)` without proof.

For every monic irreducible `P ≡ −1 mod A` of sufficiently large degree, put `X=(P+1)/A`. The standard E=1 solution is

`A/P = 1/X + 1/[P X(X+1)] + 1/[P(X+1)]`.

Its degrees are `n−k`, `3n−2k`, `2n−k`. There are such P of arbitrarily large degree by the prime polynomial theorem in progressions. Consequently no fixed additive constant makes the asserted height bound true for all these certificates. If the intended claim is that a *different*, shorter certificate always exists whenever ES_q holds, that requires a new argument; Prop 5.1 does not supply it. Retain the modulus comparison and remove the unsupported height comparison.

## Minor findings and label hygiene

1. **Missing low degrees in “all P” experiments.** `scripts/fm_mute.py:92` starts at `max(1,k)`, not 1, whereas FF_MUTE allows n<k and §6 says all irreducible P of degree ≤N. For example the F₂, A=T³, s=T+1 run omits P=T²+T+1. State k≤n≤N or actually test the omitted cases. The existence theorem does handle n<k because z can have negative degree.
2. **Composite-f wording in Prop 2.1.** `s∤f` follows directly from `f | P+AQ²` and s|Q: if s|f then s|P, contradiction. The printed “else s=f” assumes irreducibility not present in the proposition. Similarly prove gcd(f,P)=1, rather than merely f≠P, before the Type II assertion. Both conclusions are valid after these local repairs.
3. **Thm 4.2 needs its existing qualifications in every headline.** Parts (a), (b), (c), (d) are sound as written. But (c) only prohibits odd-degree moduli; it does not prove that every square is solved by even-degree moduli. “Exact-T1 iff the anchor is alive” without k odd/the degree restriction overstates the theorem. The final verdict is more careful than the prose after the theorem and the report.
4. **Mechanism T1 is not an existence T1.** `STATUS.md:19` says the integer mute variant holds for every n, “while keeping T1 exactly.” This includes squares. Specify that the *shot mechanism* retains T1, not existence in the full variant. Similarly `AGENT_REPORT_O195.md:42–44` cannot infer a universal “no existence-T1” from the existence of some square examples with even-degree data.
5. **Review provenance is overstated.** `STATUS.md:10` says every headline has two independent hostile reviews; the new (J)25 and (J)27 ledger entries identify only R191 and R188 respectively. Give the second review references or weaken the statement. Also remove stale “CLAIMED/under review” text where the referenced reviews are now applied.
6. **A repair did not propagate to O188's report.** `reviews/agent-reports/AGENT_REPORT_O188.md:37` still gives `C_adm ≈ r^{0.1K₁+0.1}`; STERILE_STEER correctly repairs it to exponent `0.1K₁+0.5`.
7. **Some research conclusions remain too categorical even under Assessment.** “No Frobenius description” and “not ... any fixed extension” need a specified class of extensions and a nonexistence proof; factorization dependence by itself is not such a proof. No finite shot covering proves neither this assertion nor exclusion of all congruence-based proofs. Likewise STERILE_STEER §6 has not proved the necessity of a *loss-free* divisor bound: a sufficiently small exponent loss can still leave a convergent tail. Separate failure of current computable estimates from impossibility of the method.
8. **Computational proof presentation.** DEPTH_ASPECT Thm 2.5 has huge safety margins and two recomputations, but its r=27 numerical certificate remains floating-point, not an outward-rounded/rational enclosure. This is acknowledged, not a newly discovered gap; a short rigorous enclosure would make the PROVED label cleaner. `verify.py`'s new subprocess check tests formatted strings and exits correctly, but is not such an enclosure. Book theorem numbers in O195 are explicitly “from memory”; verify those references before publication.

## Mathematical audit of the main FF argument

This section records the checks that did **not** produce defects; the negative findings above should not obscure that the principal proof is strong.

### Prop 2.1 and Cor 2.2

Write `B=deg(AQ²)`. Under B>n+d, E is monic of degree B−d>n, so X is monic of degree B−d−k; Y is monic of degree n+d−k. Because A divides f+1, z belongs to R[1/S] despite the displayed denominator A. Direct expansion of `AfX=P(f+1)+AQ²` gives the claimed identity and `deg z=n−k`, hence NC in every characteristic.

At s|Q, let c=v_s(Q)>0 and σ=v_s(f+1). Since s divides neither Af nor P, σ<2c gives v_s(X)=σ and v_s(z)=2σ−2c. If σ≥2c, v_s(X)≥2c and z is integral at s. At s∤Q there is no negative valuation. This proves parity and the exact integrality criterion σ≥c, including all cancellation cases. The argument also works in characteristic 2.

### Lemma 3.2

For odd q,

`(−PA/f) = ε^{d+nd+kd+k}(f/P)`,

because `(f/A)=(−1/A)=ε^k`, including non-squarefree A. This matches τ exactly. For ℓ|q−1, the power reciprocity sign is `(-1)^((q−1)hd/ℓ)`, matching ε_ℓ^{hd}; the inverse sign is the same sign. Each character modulo the irreducible s has exact order ℓ. In characteristic 2 the sign is 1 and the quadratic condition disappears.

### Character expansion and Lemma 3.3

The progression indicator has coefficient ℓ¹-norm 1, as does the quadratic indicator. A single small-prime exclusion has ℓ¹-norm `2(1−1/ℓ)`, so the total norm is

`∏_{ℓ|q−1} 2(1−1/ℓ) ≤ 2^{ω(q−1)}`.

CRT across A, P, s and the distinct prime orders at s prevent a nontrivial product from becoming principal. Thus the constant coefficient really is δ; no hidden entanglement or missing Φ(A) factor occurs. For nonsquare composite P in Thm 4.2, the Jacobi character is still nontrivial, though possibly imprimitive, which Lemma 3.3 allows.

For a nonprincipal character, the inverse-root bound gives `(D'−1)q^{d/2}` for the von Mangoldt sum; proper prime powers contribute at most `Σ_{e≤d/2}q^e ≤ 2q^{d/2}`. This yields the displayed `(D'+1)/d` bound. Excluding the primes dividing M costs at most D/d, also correctly accounted for.

### Lemma 3.4 and the large-prime tail

The root-counting reduction does not assume every α has degree d: counting *all* α only increases the upper bound. The irreducible s is separable, hence over F_{q^d} it has h distinct roots and is not an ℓ-th power; the `(h−1)q^{d/2}` multiplicative Weil bound applies. The principal term is at most q^d; zeros of s are correctly omitted. This works in characteristic 2 as well (ℓ is then odd).

For prime d and ℓ|q^d−1 with ℓ∤q−1, ord_ℓ(q)=d. Such ℓ is odd, so both 2 and d divide ℓ−1, giving ℓ≡1 mod 2d. If there are r such primes, their product is at least `(2d+1)^r` and at most q^d. Hence r≤m_d, and ordering the distinct integers `(ℓ−1)/(2d)` gives `Σ1/ℓ ≤ H_{m_d}/(2d) ≤ L_d`. No exceptional ℓ=d case survives the order condition. Also m_d≥1 for q≥2 and odd prime d≥3, so ln m_d is defined.

Subtracting this tail gives precisely the claimed lower bound. The sufficient positivity condition has enough slack to absorb the final −δD term. Since the error bracket is linear in n plus O(d), every prime d beyond `2 log_q n+C` does work. The problem is solely the subsequent *choice of a prime in a bounded-length interval* (M1), not these estimates.

### Thm 4.2 and Prop 5.4

Thm 4.2(a) extends to nonsquare composite P because the Jacobi character has nontrivial squarefree conductor and remains independent of the A and s characters. Coprimality at every prime dividing P gives the stated shape. For square P, the obstruction uses the symbol at **every prime factor** of composite f; multiplying gives the Jacobi symbol 1, contradicting Lemma 4.1 in precisely the stated parity cases. Part (d) correctly drops the quadratic condition and doubles the main term.

Prop 5.4's finite noncovering conclusion is valid after the CRT clarification in M2. Its incorrect displayed description of the full sterile set should not be confused with a failure of that conclusion. Nothing here proves noncovering by all possible families of the full mute variant.

## Baseline review beyond FF_MUTE

- Re-expanded DEPTH_ASPECT's four Case B identities and the Case A substitutions. The minimum-of-four-counts exponent argument and the Case A degree restrictions are consistent; no new algebraic defect found.
- Rechecked the general-r geometric-series argument: all-n counting (not a prime-only bound at r^k), uniform exponent loss, and the ET-only effectivity alternative are the important qualifications. The repaired text contains them. The theorem proves existence of sterile nonresidue points, not failure of ES at nearby primes.
- Rechecked STERILE_STEER's escape lemma, product-measure Borel–Cantelli statement, positive-integer quadratic-character independence in Cor 3.3, and the exponential pushforward weight 1/ord. These pass with their stated domain restrictions. The transfer of the pattern discussion to Q(√5) does not pass (M5).
- Inspected the new `verify.py` block, the prime-power counting/completion scripts, the escape script, the fm scripts, and the independent union-bound/general-r checkers. Did not rerun the large prime-power/escape censuses or the entire accumulated `verify.py` suite. The existing Type-I truncation caveat is real but documented, and the completion checker is the relevant support for the quoted failure counts.
- Form is unnecessarily hard to audit: source statements followed by several inline “R178/R187 repair” paragraphs leave stale claims beside their corrections. Consolidate final statements and move repair history into reviews. Preserve the sharp distinctions between theorem, numerical evidence, and suggested mechanism; repetition in a report should not upgrade the label.

## Bounded checks performed

All Python execution used uv, `ulimit -v 4000000`, and `timeout 300`; no large jobs were launched and no production script was changed.

- Small exact fm counterexamples for M3/M4, including enumeration of every monic divisor for the degree-2 examples and exact verification with the existing arithmetic.
- `fm_count.py 3 10 11 3 101` and `fm_count.py 7 10 11 3 101`: no reciprocity mismatches; the latter exercises the cubic-residue factor too.
- `fm_t1.py 3 10 11 3 4`: 0/1 squares, 16/16 nonsquares, zero identity verification failures.
- `fm_mute.py 2 1000 11 3 5`: both included degree-3 primes solved and verified. A preceding deliberately smaller maxd=4 run left both unsolved; this is a search cutoff, not a theorem failure.
- `review_da2_rgeneric.py 17 300 2`: all six enumerated boxes contained in predicted boxes, no level-0 box; ordered counts `{1:24,2:162}`.
- Independent union-bound checker functions at r=27, S=100: Case B `0.001331772736284676`, Case A `3.147294365854539e−12`, tail `0.0064109707079972635`, total `0.007742743447429234 < 0.03`. This supports the published margin, without pretending floating-point evaluation is a directed-rounding certificate.
