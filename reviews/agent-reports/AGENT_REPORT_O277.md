# AGENT_REPORT_O277 — consolidation C1: internal paper on ES for exponential families

Branch `side-agent/paper-expfam`. Internal only, no external release.

## Deliverables
* `paper/es-exponential-families.tex` / `.pdf` (22 pp, compiles clean with pdflatex; `.toc` is git-ignored).
  Title: "The Erdős–Straus equation on exponential families beyond every Elsholtz–Tao covering".
* `scripts/c1_expfam_verify.py` (~520 lines, sympy + stdlib only, imports no campaign code, **runs in ~4 s**).
  It re-verifies every certificate in the paper (see "What the verifier proves" below), plus the Theorem W finite
  enumeration (with positive controls) and the boxed-equation enumeration of Lemma 5.14.
  Run: `PYTHONPATH=scripts uv run python scripts/c1_expfam_verify.py [--tables]`.
* Helpers (not part of the proof): `scripts/c1_extract_z14.py` (flattens the z14 tree certificates into explicit
  leaves with explicit window relations, output in `data/c1/*_leaves.json`) and `scripts/c1_tables.py` (prints the
  LaTeX rows of the certificate tables from the classes the verifier *derives*). Transcript `data/c1/verify_tables.txt`.

## Paper structure
§1 intro (ES, Mordell/ET coverings, Sierpiński/Izotov analogy, main theorem, scope, labels, provenance);
§2 exponent coverings and unit-square points (ET table; **self-contained odd-square Lemma 2.2 incl. the Type II
case**, Cor 2.3 with gcd bookkeeping; rules, periodicity, Theorem 2.7 = no ET/divisor covering when c₀+k = 4^J,
k ≡ 1 (8); Prop 2.8 integer unit-square points; Remark (EH));
§3 window lemma (Rav form + d | x² form), forced budgets (SG, CY, binomial/moving gap), specialisation lemma;
§4 Theorems: 3·2^s+1 (complete hand proof), 63·2^s+1, 7·4^s+9 (22 window rules + 11 ET classes, tables),
4^s+105, nine 4^s+k (tables);
§5 limits: Theorem W with full proofs of the lemma chain, Cor 5.9 (constant ratio), Cor 5.10 (no covering);
15·2^s+1 (Prop 5.12, Lemma 5.13, Lemma 5.14, Thm 5.15, open branches); open problems;
App. A verifier; references with exact attributions (ET, Mordell, Schinzel, Yamamoto, Salez, Mihnea–Dumitru,
Sierpiński 1960 and Izotov 1995 via Filaseta–Finch–Kozek 2008, Bertók–Hajdu, Rav, Ridout, Lang/Capelli;
not-accessed sources marked).

## What is new relative to the campaign files (needs the parent's critical check)
1. **Proposition 5.12 (NEW, computer-assisted): ES for every 15·2^s + 1 with 60 ∤ s**, by 11 ET/divisor classes
   (II2 and D only, moduli 7, 11, 31, 39, 99, 287), with a short by-hand coverage argument in the proof. EXP_OPEN §0
   had only EVIDENCE for the odd half 30·4^t+1; this certifies both halves except s ≡ 0 (mod 60). Checked only by
   my verifier so far (no independent reviewer). Members with 3 | s are Mordell-hard (n ≡ 121 mod 840).
2. **Lemma 2.2 / Cor 2.3**: the sterility of the unit-square point no longer rests on Mordell/Schinzel (not
   accessed; flagged by R189 for EXPONENT_COVERING Thm 1.2). Proof via ET's Σ-variety identities; the Type II case
   (omitted by ET) is written out; Cor 2.3 handles coprimality family by family (P_κ includes the constant
   coordinates e for I1, c for I4/II1/II2). Theorem 2.7's proof is purely elementary (no profinite language).
3. Lemma 5.14 (boxed equation): new, simpler completeness bounds (a ≤ 81, m₁ ≤ 100, m₁d ≤ 120); same 39 solutions.

## Gaps / discrepancies found in the campaign files (flagged, not papered over)
* **Table-level ET membership (found by my reviewer pass, now repaired):** "integrality of x, y, z" is weaker than
  "n lies in the named ET class". Two certificate leaves are valid only through cancellation on extra residues
  (II1(1,254,15) at s ≡ 1 mod 7 for 63·2^s+1; I3(1,11,3) at s ≡ 2 mod 5 for 7·4^s+9; also I3(1,5,3) at odd s for
  6·4^s+1). The verifier now also requires integrality of the ET parameters (resp. (d₁+d₂)/m for windows), and
  the tables list exactly those classes; coverage is unaffected (D₁₂₇, D₁₁, D₅ cover those residues).
* **EXP_15 Lemma 2.1 / Thm 2.2 scope:** the proof needs b, c ∈ ℚ[Y] *themselves* integer-valued (it specialises b
  and c). This is not implied by integrality of x, y, z: (a,b,c,d) ↦ (a/h,b/h,c/h,h²d) preserves x,y,z; with h = 5
  on the 63·2^s+1 family it gives a = 1, d = 425, b(1) = c(1) = 1/20. The paper states the hypothesis explicitly
  (Lemma 5.13) and adds Remark 5.16. Theorem 5.15 is a statement about the (BI) menu as defined in EXP_15 — the
  ledger's "for every root degree and every factorisation" is right, "every II-ad family" should carry this caveat.
* 7·4^s+9: two leaves of the 59-leaf tree (I3(1,74,39), II2(9,1,935)) are redundant; 33 distinct rules suffice.
* 4^s+105: the coverage period is 180 (not 360); SYNTHESIS_SPARKS6 Thm 1.1(c) still says "positivity n ≥ 4⁴"
  (R246 D1: n ≥ 1) — the paper uses n ≥ 1.
* 63·2^s+1: derived thresholds are ≤ 5 and every small s except s = 0 is covered by a class (source used a cut
  s ≥ 10 with brute force below).
* EXP_OPEN Lemma 1.1 (reduction to polynomial divisors) was terse; expanded (resultant ⇒ constant gcd on a
  neighbourhood; polynomial divisibility by the vanishing-remainder argument; gcd(N(Y), m) = 1 near μ = 0).
* Not closed and stated as such: EXP_OPEN Prop 4.1 for windows with 19 | m (4^s+297) remains OPEN (cited only,
  Remark 5.11(iii)); the remark on the two dead classes X ≡ ±1 (mod 11) in Thm 4.1 cites NEAR_SQUARE Thm 3.3 /
  MENU_STERILITY §4.3 without reproving it; the extension of Thm 2.7 to all polynomially solvable classes (via
  ET Prop 1.9) is mentioned but not used.
* Stale items in source files noted by my research pass (not used in the paper): status lines "unreviewed" in
  MENU_STERILITY / SYNTHESIS_SPARKS6 / EXP_105; SIGN_FIELDS §2 "failures" paragraph mixes 21/22 word counts;
  EXPONENT_COVERING §0 still tags the Bertók–Hajdu dictionary "SHARP".

## What the verifier proves (and how)
For each family and each rule (x, y, z ∈ ℚ[Y], Y = 2^{ωt}, s = s₀ + σt): symbolic identity; the exact set of
residues t (mod T) on which x, y, z **and the class parameters** are integral, derived from one full period of
R₁(2^{ωt}) mod N beyond the 2-adic/positivity threshold (Lemma 2.5); positivity by exact Sturm root counting;
coverage of all residues mod the lcm of the periods (9180 for 7·4^s+9, 2520 for 63·2^s+1, 120 for 3·2^s+1,
180 for 4^s+105; s ≡ 0 mod 60 excluded for 15·2^s+1); every s below the largest threshold solved by a rule at that
s or by exhaustive divisor search (only s = 0 needs it, in four families); exact solutions built and checked for all
s ≤ 1000 (≤ 600 for the nine 4^s+k). Also the EXP_105 second certificate for 3·2^m+1. Theorem W: enumeration of all
odd w with 0 < m ≤ B(m), all a₁, a₂, all admissible (e₁, e₂) without the parity filter — no relation for the six
families; positive controls (3,1), (7,9), (23,41), (39,25) give exactly m = 11, 19, 51, 131.

## Review status
A deep hostile self-review (review tool, since ace654cf) found no FATAL; MAJOR 1 (table ET membership) and MAJOR 2
(II-ad integrality hypothesis) and all minors were repaired in the last two commits. The paper has had no
independent referee pass yet; recommended next step: an independent hostile referee on the .tex (in particular
Lemma 2.2/Cor 2.3, Theorem W chain, Prop 5.12) with an independent re-implementation of the coverage checks.
ES is not solved; all theorems are about thin families.
