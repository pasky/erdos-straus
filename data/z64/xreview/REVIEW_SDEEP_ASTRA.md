# Retro review — Z64_SDEEP (Astra)

Reviewed main snapshot `311454873d4461d48afbffbc29f4470a59dd5471`, including the applied Opus fixes.
Protocol: `xreview_retro.md` / `xreview_z58.md` items 1–5. **ES and (S) remain OPEN.**
Verdict: **ACCEPT-WITH-FIXES** — the census checks pass; the genus proof needs explicit scope.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| §1 sign dictionary | CORRECT | AB=tn+1 makes A,B units; A≡u/v requires the now-stated gcd(uv,n)=1. For odd A, reciprocity gives (A/n)=(−u/A)=(−t/A). |
| Lemma 1, trace identity | CORRECT | ad≡1 gives s±2≡(d±1)²/d. Taking Jacobi symbols is valid separately when gcd(s±2,n)=1. |
| Lemma 1(a), proper-class invariance | CORRECT-WITH-FIX / GAP if unrestricted | The displayed genus argument works when gcd(n,s+2)=1. This is not automatic at composites; its equality at m=n can otherwise be false (explicit example below). |
| Lemma 1(b), failure in general at s≡0 (4) | CORRECT | [17,2,−2] under the determinant-one substitution (x,y)↦(x,y−x) becomes [13,6,−2]; signs are −1 and +1. This proves “not in general”, not an iff for each trace. |
| Genus numerical check | REPRODUCED, scope correction | Original script: 3,089 comparisons / 0 disagreements for s≢0 (4); 1,901 / 1,155 for s≡0 (4). It skips imprimitive forms, unlike the memo's “all words” wording. |
| Lemma 2, cell function and (S)⇔ML | CORRECT; PRIOR | Read DEDEKIND_ES Thm 4.5 and §8.1 directly. Exactly five positive cells; equivalence requires L₃≠∅ as now stated. Independent 1,280 mod-16 cells agree with both the five-slot and SDEEPF product criteria. |
| Prop 3, whole-fibre product | CORRECT | χ(n+u)=χ(u); remove the 2-adic factor. For odd q dividing n+u, reciprocity gives (q/n)=(−u/q), using gcd(u,n)=1. Only this aggregate identity is proved. |
| Prop 4(i), modular-hyperbola description | CORRECT | AA*=tn+1; A≡−1 (t) forces A*≡−1 (t). The lower bounds give u,v≥2; each strip has just the one permitted product. |
| Prop 4(ii)–(iii), KS2 | ASSESSMENT, not a universal no-go | The square-root error is too large for the heuristic log²-sized target. The strip identity alone cannot rule out future cancellation/geometry arguments; read the kill as failure of the stated completion bound. |
| §4(a), polynomial-word obstructions | CORRECT for the two stated shapes | Coefficient comparison gives k=−d(x−β/d)²−αβ/d in the fixed-t shape, and k=−dy²−v in the fixed-v shape; positivity makes both negative. |
| KS0, adversarial census | REPRODUCED SLICE | Eight full adversarial rows, 130 early rows and all 357 screen rows reproduce exactly; independent early-row and small-n checks below. No counterexample. |
| KS1 | SCOPED EVIDENCE; partially rerun | Regenerated all 37,116 prime feature rows with 0 cell/trace failures. Reviewed fitting code and report; did not rerun the class-number regression (cypari2 unavailable). Saved report has 7,260 pairs and no 0.99 law with >4σ gain. |
| Prime census / prime-A | REPRODUCED | Pooled negative fraction 1,446,628/2,059,842=0.70230047; minimum one negative pair at 17,41,21841. Full prime-A run to 2·10⁷ is byte-identical: failures 20521,21841,589681 only. |
| §§5–9, missing lemma / NARROWED | JUSTIFIED with qualifications below | Cell escape is an exact reformulation, not a proof of positivity. No HOT LEAD or conclusion about ES follows from these computations. |

## Proof-scope finding missed by the prior review

For (t,u,v)=(7,3,9), n=177, A=20, A*=62, s=82 and f=[177,42,−7] is primitive.
Here s≡2 (4), D₁=s+2=84, but **(20/177)=−1 whereas (84/177)=0**.
Thus “at m=n it equals … χ_n(A)” in the genus proof is false without gcd(n,s+2)=1.
This does **not** refute class invariance in the ramified cases; it identifies the missing proof there.
With coprimality, the proof works: D₁ and D/D₁ are discriminants; reducing the completed-square identity
modulo D₁ shows χ_D₁(a)χ_D₁(m)=1 for represented m coprime to 2D₁, since a=n is also a unit.
At primes the needed coprimality is automatic: p|(s+2) would force A≡−1 (p), impossible for an interior word.
The prior Opus table implicitly inherited the gcd condition; the standalone claim and exported summaries do not state it.

## Computation record

All shell runs use `ulimit -v 4000000` and timeouts ≤1,800 s. Added reproducible audit:
`scripts/xrev_retro_sdeep_checks.py /tmp/xrev_retro_sdeep_decide` (uv + existing sympy environment).
Compile the executable from `scripts/z64_sdeep_decide.c` with `gcc -O2 … -lm`.
- Independent t,u,v enumeration: all 4,999 n≡1 (4), 5≤n≤20,000, 96,707 reversal orbits;
  every full-mode count agrees, including singleton u=v orbits, direct Jacobi/cell/product/eligible trace identities.
- Full adversarial reruns: near-square n=1024625768605,80939027478553,6105490123065,35134663502505;
  d·m² n=457709742405,79895846970441,16523165791125,42839590235469. All eight-column rows agree.
- Early reruns: 65 rows from each family (seed 64042, including a maximal-exit row), independently enumerating
  divisors of n+u with sympy and evaluating Jacobi. Counts, first-word u and exit u all agree; maxima 24 and 7.
- Recomputed file statistics: 1,248 / 2,310 full rows; minima N₋=69 / 65, total pairs=112 / 103;
  smallest negative fraction 0.46594982 / 0.55688623. Early families have 14,997 / 624 rows.
- All 357 full screen rows reproduce. The only wordless value is 105 (listed twice across screen families).
- Also reran `z64_sdeep_words.c 2000000`, `z64_sdeep_primeA.c 20000000` and `z64_sdeep_genus_check.py`.
  The full KS0 3,558-row enumeration and the KS1 class-number fit were **not** rerun; no claim otherwise.

## Falsifiers and prior attributions

F1: squares have χ=+1 on units, hence no negative words; “χ≡1” should always be read on units.
F2/F4: all 14 star, 38 gstar and 12 R₈-zero primes pass the screen rerun; independent direct checks of the
SDEEPF witness file also verify all these inputs. A hit in the union does not certify a fixed sub-family.
F3: all 284 non-vacuous composite R-zeros have witnesses; 105 is vacuous, including in Z₇.
The minimum-one-pair cases and 21841's one-of-ten statistic agree. Primality is not needed for cell escape.
Read the actual prior sources: DK Thm 4.5/§8.1 establish the all-composite five-slot/cell law;
WINDMILL_REDUCTION §§5.2–5.3 supply γ, f and the hyperbola; y1_gamma8_trace G2 uses the different matrix
of trace n−t and a 37/39 counterexample. The memo's added credits are appropriate.
However FOREST_CONNECTIVITY Thm 2.1 and FOREST_DEEP_FABLE Thm A explicitly assume gcd(uv,n)=1:
they are **not**, as Lemma 2's proof says, elementary proofs covering all composite words.
DK supplies the unrestricted result; SDEEPF Thm 2.1 now supplies an unrestricted elementary proof.

## Required fixes, priority order

1. Explicitly retain gcd(n,s+2)=1 in the genus assertion and §§6/8/10 summaries, or prove the omitted
   ramified cases. Restore the separate gcd(n,tr γ±2)=1 conditions in §8's exported trace formula.
   Change §10's “iff s≢0 (4)” to “for s≢0 (4); not in general for s≡0 (4)”; identify the genus census as primitive-only.
2. Correct Lemma 2's source-scope sentence: the two forest proofs require gcd(uv,n)=1; cite DK for all n
   (or the independently proved SDEEPF criterion), rather than silently extending those sources.
3. In §9 qualify “N₋≥65 there” as the **3,558 fully enumerated adversarial rows**, not all 19,179 rows.
   Preserve “current completion estimate / Assessment” when exporting KS2; the strip tautology is not a general impossibility theorem.

**Final verdict: ACCEPT-WITH-FIXES.** Core algebra and decisive requested census checks survive;
the unrestricted genus proof is not certified by this review. No memo/source files were changed.
