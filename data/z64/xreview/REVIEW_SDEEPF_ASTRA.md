# Retro review — Z64_SDEEPF (Astra)

Reviewed main snapshot `311454873d4461d48afbffbc29f4470a59dd5471`, after the Opus review/fixes.
Protocol: `xreview_retro.md` / `xreview_z58.md` items 1–5. **ES and (S) remain OPEN.**
Verdict: **ACCEPT-WITH-FIXES** — the main theorems survive; one structural “exactly when” claim is false.

## Per-claim audit

| Claim | Classification | Re-derivation / check |
|---|---|---|
| Lemma 1.1 and W_t/W_u/W_A | CORRECT | AB=tn+1 proves automatic coprimality and equal symbols. Reciprocity gives (−t/A)=(−u/A) for odd A. In W_A, u<A ensures u=(−n mod A); all inverse size conditions agree. |
| Thm 2.1, product/table criterion | CORRECT; PRIOR in substance | Re-derived all three parity cases. For even t the sign reduces to the stated exponent E; for odd t and even u it is −(−1)^{tu(t+1)/4}; for all-odd letters it is −(2/nt)^{v₂(A)}. If nt≡3 (8), v₂(A)=v₂(B)=1; otherwise nt≡7 (8). All cases give exactly 8∣(n+t)tuv. |
| Cor 2.2 | CORRECT | A is a unit modulo n=m², hence (A/n)=1. No primality hypothesis is needed. |
| Thm 3.1(a) | CORRECT | n≡5 (8), n≥13: (3,3,(n+3)/8), A=8, (8/n)=−1. n=5 is wordless. |
| Thm 3.1(b) | CORRECT; PRIOR | n≡5 (12), n≥17: ((n+7)/12,4,3), A≡3 (4), (A/n)=(−4/A)=−1. Read bsG_primes_trivial: same fixed outer letters and sign. |
| Thm 3.1(c) | CORRECT, small-case sentence needed | n≡21 (36), n≥57: ((n+15)/36,3,12), B=12t−1, (B/n)=(−3/B)=(B/3)=−1. The remaining n=21 is covered by (a), with (3,3,3); the displayed (c) word has t=1 there. |
| Remaining classes mod 72 | CORRECT | Removing 5 (8), 2 (3), 3 (9) leaves {1,9,25,33,49}. |
| Props 3.1′ / 3.2 | CORRECT | Integrality/thresholds give genuine words; reciprocity gives the asserted signs. With 4∣u, the odd part of u contributes +1 and the 2-power also contributes +1 to (u/A), leaving (−u/A)=−1. |
| Prop 3.3(1)–(7) | CORRECT as sufficient criteria | The proper-factor and lower-bound exclusions ensure every letter≥2. In (6), 4∣B and B≡2 (3) give B≥8. The u=2,3,4 mechanisms are prior in FOREST_CONNECTIVITY Prop 3.1(iii), originally stated for primes in a narrower class. |
| Remark 3.4 / Prop 3.5 | CORRECT | The universal words have t≥2. For finite (u,v), transfer the word/sign modulo 8uv to a sufficiently large square. For bounded A use the period dividing 4A. Neither argument rules out an unrestricted fixed-level divisor search. |
| Thm 3.6 | CORRECT; REPRODUCED | Original covering checker is byte-identical; independent sympy checks of the actual 57 words cover all 312,312 classes off E. Threshold 24,529. The small-n gap is covered by the reproduced 3·10⁶ census. |
| Thm 4.1 | CORRECT | The 3-power decomposition and split at √y prove the claimed bound. Alternatively a one-form upper-bound sieve proves it directly. The last sums-of-two-squares aside needs qualification (below). |
| Thm 4.2 | CORRECT, unconditional standard sieve input | Verified the distinct-root, dimension and remainder conditions explicitly below. κ_K is correct and diverges. No unproved distribution hypothesis is needed. |
| §5 (S′), odd-part formulation | CORRECT | The product criterion gives (S′); for n≡1 (8), (A/n)=(n/A′)=(−u/A′), with A′ the odd part. |
| §5 item 2, “exactly when … prime factor” | WRONG as necessity | Good words at general fixed levels can require composite divisors; n=21841, t=64 supplies an explicit counterexample below. Prop 3.3 only proves sufficiency. |
| §5 “no analytic sign cancellation argument … available” | ASSESSMENT | Locality reformulates cancellation as distribution among cells; it is not an impossibility theorem for analytic methods. Keep this scoped to the lack of a mechanism here. |
| §6 and no-HOT-LEAD verdict | SUPPORTED, sampled | Requested checks agree. The 10⁸ full census, large covering moduli and min-A table were not independently rerun; the 3·10⁶ check is already enough for Thm 3.6's finite gap. |

## Computation record

All commands use `ulimit -v 4000000` and timeouts ≤1,800 s. New independent audit:
`uv run --no-project --python .venv/bin/python python scripts/xrev_retro_sdeepf_checks.py`.
It uses sympy Jacobi symbols, not either original checker's symbol routine; coverage is streamed, not a dense matrix.
- All 1,280 admissible mod-16 cells: product criterion = DK five slots = SDEEP's five-positive-cell predicate.
- Explicit Thm 3.1 words through 300,000: 37,499 (a), 24,999 (b), 8,332 (c), all genuine and Jacobi −1;
  separately verified n=21 via (a). No primality restriction or omitted sign condition.
- `gcc -O2 scripts/z64_sdeepf_crit8.c -lm …`, run with 3000000: byte-identical to `crit8_3e6.txt`;
  76,824,951 words, 0 mismatches, 749,132 non-squares with words, 0 failures, 0 good square words.
- `z64_sdeepf_cover_check.py`: byte-identical to `cover_check.txt`; 46 A-words + 11 uv-words, threshold 24,529.
- Independent 57-word check: direct Jacobi on n₀+3L and n₀+7L, L=1,441,440; every off-E class covered.
  Exactly 15,331 classes inside E are uncovered by these 57 words. Checked A∣L, 8A′∣L, 8uv∣L and all thresholds.
- `z64_sdeepf_cover2.py 1441440`: byte-identical; 346,618/360,360 classes covered, hence 13,742 uncovered.
  Those 13,742 are a **subset** of the 48,048 classes lying over E, not all classes over E.
- Independent square residues: E is exactly the 24 odd-square residues mod 840 plus {265,321,769,825}.
- Every stored good witness checks: 348 rows, 334 distinct n. All 14 star, 38 gstar, 12 R₈ primes and
  284/285 composite screen values have witnesses; only 105 is missing, and the independent SDEEP audit finds no word.
- Reran `z64_sdeepf_escape.c 10000000 4` (160-million-entry uint32 sieve, about 640 MB): the 10⁷ counts agree.

## Thms 4.1 / 4.2: source and hypotheses audit

For 4.1, failure implies n≡1 (8) and n+4=3^e m with every prime of m≡1 (4).
The stated estimate G(y)≪y/√log(2y), followed by the geometric sum over e, is sound.
The assertion that the entire set S=3^ℕ·{products of primes≡1 (4)} is a subset of sums of two squares is false:
3∈S. It becomes true after retaining n+4≡1 (4), which forces e even. This repairs the claimed Landau-only shortcut.

For 4.2 let r=2K+4 and discard the finite set of primes dividing leading coefficients or pairwise resultants,
and any p≤r. For each remaining p let Ω_p be the roots of the selected forms with p in their prime sets.
The forms n+a and an+1, a∈{2,3,4,8,…,4K}, are primitive and pairwise non-proportional:
same-type resultants are nonzero differences, opposite-type resultants have absolute value ab−1>0.
Thus ω(p)=|Ω_p| equals the number of active forms and ω(p)<p. CRT gives
A_d=x·ω(d)/d+O(ω(d)), with ω(d)≤r^{ω₀(d)} for squarefree d (ω₀ counts distinct prime factors).
PNT in the fixed arithmetic progressions gives V(z)=∏(1−ω(p)/p)≍_K(log z)^{−κ_K},
κ_K=6/2+2Σ_{k=2}^K1/φ(4k). The required interval product bound follows from the same estimates.
Take D=x^{1/2}; Σ_{d≤D}|R_d|≪_K D(1+log D)^{r−1}. A fixed sufficiently large sieve parameter s
and z=D^{1/s} give the claimed upper bound; all witness side conditions hold for n≥√x and large x.
Add O(√x) for smaller n. Finally 1/φ(4k)≥1/(4k), so κ_K→∞.
Source checked directly: Tao, *254A Notes 4: Some sieve theory*, Corollary 19 and condition (22),
https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/ , in the repository source copy
`sources/lit2026/audit-tao-254a-notes4-sieve-theory.md`. This also proves 4.1 with one form.
I did not authenticate the memo's exact Halberstam–Richert theorem numbers or Wirsing Satz number;
the checked equivalent source plus the verification above suffice for the conclusions, without relying on those numbers.

## Falsifiers, attribution, required fixes

F1–F4 pass for the actual theorems: squares have no good word, the covering omits their residues,
all screened non-vacuous composites/primes have witnesses, and no single sub-family is claimed universal.
Read DK Thm 4.5 and §8.1 directly: the five-slot theorem and exact mod-4 table already give Thm 2.1's content.
The repaired attribution is correct: only the one-product packaging is new relative to these sources.
The forest theorems assume gcd(uv,n)=1, whereas DK and this memo's case proof cover all interior words.

1. **Fix §5 item 2's false necessity.** At n=21841, (t,u,v)=(64,9,38) has A=575, B=2431 and Jacobi −1.
   But 64n+1=5²·11·13·17·23 has no prime factor ≡−1 (64). Replace “exactly when” by “the sufficient
   prime-factor criteria in Prop 3.3”; general fixed levels require divisors in a class, potentially composite.
2. Fix the last sentence of Thm 4.1's aside to use S∩{m≡1 (4)}, not S. Keep the already-correct 3-power proof.
3. Add “n=21 is handled by (a)” to Thm 3.1(c). In Thm 3.6 say “13,742 uncovered classes, all lying over E”.
4. In §F F1 qualify the prime-factor +1 statement by q odd and q∤u (respectively q∤t): without coprimality,
   zero is possible, e.g. q=3 divides 3²+3 and (−3/3)=0. All primes used by Prop 3.3 meet the needed conditions.
5. Keep §5's analytic-method dismissal as Assessment, not a consequence excluding future cell-count estimates.
   Optionally replace the unverified textbook numbering with the checked sieve source and verification above.

**Final verdict: ACCEPT-WITH-FIXES.** Thms 3.1, 3.6, 4.1 and 4.2 stand; no theorem here resolves (S) or ES.
