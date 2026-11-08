# Hostile review of Z66_UCOVER.md

## Verdict: REJECT the current version; the central Theorem T appears salvageable and essentially correct

The rejection is **not** a refutation of the claimed strict inclusion U ⊋ squares. I checked ET’s source, including Lemma 2.8 and §3: its counting argument really does extend to all positive integral sextuples, without the coprimality restrictions. The main measure argument and Corollary T.1 survive the correction to Lemma 1 below. However, §5’s two-prime enumeration misses genuine families, including a family that kills an entire advertised surviving branch; several literal theorem/summary statements are false; and the floating-point computation is not yet a rigorous numerical certificate as advertised. ES remains open.

No authentication/quota/provider error occurred. No tracked repository file was changed. Review experiments and this report are in `/tmp`.

## Findings

### 1. MAJOR — The two-prime reduction is incomplete; an advertised surviving branch is already entirely covered

**Location:** §5, “Two-prime profiles”; opening result (iv); proposed FRONTIER text; `scripts/z66_ucover_levels2.c`, which enumerates only A, E/D, F.

The single-prime elimination of I-2, I-3 and II-3 does **not** extend by simply replacing ℓ^k by an S-number. Different primes of S can occur on opposite sides of the coprime factors in those families. These are additional omissions, unrelated to the two reported A-splits.

Explicit counterexample: ET II-3 with

- a = 11, d = 2, e = 247 = 13·19;
- gcd(4ad,e) = gcd(88,247) = 1;
- class n ≡ −4a²d−e = −1215 ≡ 20521 (mod 21736);
- 21736 = 11·13·152, and −1215 ≡ 1 (mod 152);
- −1215 ≡ 6 (mod 11), and ≡ 7 (mod 13).

Consequently **every** two-prime profile over (g,h) ≡ (6,7) mod (11,13) is caught by this one class, already at valuation level (1,1). It cannot survive to (2,2), (2,3), or (3,2). My literal mixed-family search found this omission. Replaying the existing enumerator gives 74 survivors at (2,2); this omitted class alone removes 37 of them.

**Fix:** Implement/derive the mixed-support cases of all seven ET families and independently cross-check the two-prime enumerator. Until then, mark *all* these counts as upper bounds from an incomplete family subset, remove the asserted survival of (6,7), and do not attribute incompleteness solely to the A cutoff. Check subprocess exit status in `z66_ucover_ktree.py` too. This finding does not settle whether K ∩ U is empty.

### 2. MAJOR — Lemma 1’s exact-level “iff” is false with only the displayed pure E/D equation

**Location:** §2, first paragraph and E/D bullet; §2.1 mixed-E reduction; §4 proof’s use of E_k.

The parent-cylinder argument is correct, but changes the level from k to k−2 min(k₁,k₂). It proves an equality of unions across levels, not the advertised characterization at each exact valuation level.

Concrete example: ℓ=23, k=3, II-1 parameters

    a=23, b=3703=23²·7, e=27, c=138.

Here e | a+b, gcd(e,4ab)=1, and 4ab=28·23³. Thus the class n ≡ −27 (mod 4ab) catches the exact-level residue 12140 mod 23³. The C enumerator prints it as

    E 12140 k1=1 a'=1 b'=7 c=138 D=1 e=27.

I checked the full level-3 enumeration: this residue is absent from the union of A, F and **pure** E/D at that level. Its parent is instead a level-1 event.

**Fix:** Define separate full exact-level sets and reduced generating sets. State that every family cylinder is contained in a reduced cylinder at a level ≤ its own, and that the union over all levels is unchanged. Use the reduced sets in Theorem T’s union bound; keep the full mixed-E enumeration for the exact-level tables. The theorem’s measure conclusion does not require the false exact-level assertion.

### 3. MAJOR — Several theorem/summary statements erase the non-square or “most” quantifier

**Location:** opening result (iii), §4 remarks, Theorem S(c), §6 discussion of e_{7,g}, §7 bottom line and FRONTIER text.

- “For ℓ=11,13 every e_{ℓ,g} is caught” is false: g=1 gives the square profile 1, which is never caught. The same error occurs in Theorem S(c) for ℓ=3,5,7. These statements concern **non-residue g only**.
- The bottom line says profiles non-residue at ℓ avoid all ET families, without the essential “most” qualification. This is false for arbitrarily large primes: if ℓ≡3 mod 4, take the F-event a=c=1, d=(ℓ+1)/4. It catches the non-residue g≡−1 mod ℓ.
- “For large ℓ almost every g works” is not a measure-one statement for a fixed ℓ. What is proved is that the successful proportion tends to one as ℓ tends to infinity.

**Fix:** Restore “every non-residue profile” in the small-prime failures, and “a proportion 1−o(1), as ℓ→∞” / “most non-residue profiles” in the large-prime conclusions. Do not publish the current bottom-line quantifier.

### 4. MAJOR — The FRONTIER event exponent and bottom-line proof summary omit the A-family scale

**Location:** §7 proposed FRONTIER text, “≤ ℓ^{3k/5+o(k)} events”; bottom line, “n=ℓ^k” and “≪ n^{3/5} solutions.”

The proof supplies an A contribution as large as

    sum_{K'=k}^{2k−1} P_II(ℓ^{K'}),

whose available bound is of order k·ℓ^{(4k−2)/5+o(k)}, not ℓ^{3k/5+o(k)}. Also, ET’s bound has a subpower factor; it is not the stated ≪n^{3/5} bound. The body of §4 correctly handles both issues, but the exported summary does not.

**Fix:** Quote the actual three-term bound, or explicitly distinguish F at n=ℓ^k from A at n=ℓ^{K'}, K'≤2k−1, using exponents 3/5+o(1) and 2/5+o(1). Retain the crucial inequality 2·(2/5)<1.

### 5. MAJOR — Theorem S’s analytic candidate bound is sound, but its implementation is not a rigorous all-level upper-bound certificate

**Location:** §6 Lemma S2/Theorem S; `scripts/z66_ucover_stree.py`, `B_ratio`, mass accumulation, and lines 92–98.

I found no mathematical counterexample to the displayed B(N,k): the harmonic-sum bounds dominate every scan, including the large-X / large-s scans. This is a genuine all-level analytic argument, not merely an observed `cand <= B` property. But the numerical certificate has gaps:

1. `B_ratio` uses ordinary floating-point `exp`, `log`, `sqrt`, arithmetic and summation without directed rounding or an error bound. Adding 1e−9 to one logarithm does not establish outward rounding of the complete calculation.
2. It actually underflows: `B_ratio(101,400) == 0.0`, although the mathematical bound and the remaining tail are positive. Thus “twice the last term” becomes zero in some certified runs. At ℓ=100000 it also underflows before k=400.
3. The stated ratio <1/2 is false for the included ℓ=3 run: B_ratio(3,401)/B_ratio(3,400) is approximately 0.580223. Twice the last term can still be justified there using a different ratio bound, and no surviving branch is claimed there, but the written justification is false.
4. The literal C program is fixed-width, not an executable enumeration at arbitrary k. Its all-level use must be a mathematical arbitrary-integer algorithm/count, with the actual executions separately restricted to a proved overflow-safe range.

The positive margins are large; these look repairable rather than evidence against Theorem S’s intended conclusion.

**Fix:** Count branch masses as integer counts over exact denominators; use outward-rounded or rational upper bounds for removals/tails, or provide a conservative analytic error allowance. Bound the infinite remainder by an explicit positive geometric majorant before floating underflow. Prove its ratio over the stated prime range. For S(b), supply an analytic monotone majorant or interval-certified evaluation; my ordinary-float check gives 0.3072248625 at ℓ=100000, consistent with 0.31 but not itself a proof. Distinguish the mathematical enumeration from machine-range claims.

### 6. MINOR — The reported maximum tail is wrong once the small-prime certificate is included

**Location:** §6 proof of S(a), “tail ≤9.4·10⁻⁴.”

The requested replay `z66_ucover_stree.py 11 6 11` gives tail 1.009·10⁻³, also present in `stree_certified_small.txt`. The quoted bound applies to the 17–101 block, not to all primes in S(a). The lower bound approximately 0.095623 for each ℓ=11 branch is reproduced, so this does not threaten positivity. Across the stored positive branches, the smallest printed lower bound is 0.009911, consistent with ≥0.0099.

**Fix:** Use a safe bound such as 1.01·10⁻³ for all S(a) cases, or explicitly restrict 9.4·10⁻⁴ to ℓ≥17.

### 7. MINOR — “Caught mass at level k” is not the newly removed survivor mass

**Location:** §3 after the table, and §0’s kill-test discussion.

The numbers 0.375, 0.169, 0.065, 0.0072 are |E_k|/φ(ℓ^k), including overlaps with cylinders caught earlier. They are not successive decrements of the surviving mass. At ℓ=17 the first three actual decrements are 0.375, 0.0294118 and 0.0099481.

**Fix:** Label these numbers “mass of the level-k event set, before subtracting previous coverage.” Report new loss separately, and replace “stabilises” by a finite-level observation rather than an assertion about the limit.

### 8. MINOR — “Only the II-2 classes” is true at most for reduced generators, not for all ET classes

**Location:** §5 “Single prime,” assertion that residues 2 and 6 are caught only by two II-2 classes.

For example, II-3 with a=4,d=1,e=143 gives n≡−207 (mod 2288). Since 2288=11·208 and −207≡1 (mod 208), it also catches the single-prime branch g≡2 (mod 11). It is redundant with an F-event on these profiles, but it is a different ET class.

Similarly, the opening “four of ET’s seven families are redundant” obscures the actual bookkeeping: I-2, I-3 and II-3 are eliminated; I-4 and II-1 are paired as E/D, with two residue outputs.

**Fix:** Say “among the reduced A, E/D, F generators,” and describe the family pairing explicitly. Do not confuse reduction of profile coverage with identity of the original classes.

### 9. MINOR — Several auxiliary assertions need qualification

**Locations:** §0 F4; §4 remarks; §8 O1/O3; §6 setting.

- “Integer profiles are impossible (Ẑ^×∩ℚ={±1})” contradicts its own parenthesis: ±1 are integer unit profiles, and e_{ℓ,1}=1 is used throughout. Say “no positive integer prime is a unit profile; the rational unit profiles are ±1.”
- An effective ℓ₀ is justified, but “the explicit ℓ₀ is astronomically large” is an unsupported assessment when no threshold has been calculated.
- O1’s assertion that an explicit exponent θ<1/2 would turn the current ℓ=17 computations into a proof is not automatic: its constants must give a tail smaller than the surviving mass, perhaps only after much deeper enumeration.
- In O3, specify that m_ℓ is the surviving **non-square** mass. Total mass of U on the single-prime slice tends to 1, not 1/2.
- Compactness gives a **finite cover** by good-word classes, or a union of their intersections with the target class; it does not literally give equality with a finite union of unrestricted original classes. Use “finitely coverable,” consistently.

**Fix:** Make these local wording corrections and label uncomputed size estimates as Assessment.

## Checks that passed

- **ET input / Theorem T:** Read the requested source passages via `pdftotext -layout`. Lemma 2.8’s proof uses the defining equations and positivity, not coprimality. Both reflection maps preserve positive integral points. Every divisor-count case in §3 remains valid for all such points. Thus P_I(n)≤n^{3/5+o(1)} and P_II(n)≤n^{2/5+o(1)} are justified in the required sense. The maps in §2.2 are positive integral and injective for each fixed level/split; the single-prime C enumeration bounds are valid. The E/D injection is for the pure events, as stated in §2.2, not every mixed event at its original level.
- **Lemma 1 algebra:** Jacobi fact (J), the χ_{−4d} parity calculation, the single-prime I-3 impossibility argument, the reductions of I-2/II-3, and the impossibility of k=0 are correct. The mixed-E parent argument is correct; the error is its promotion to an exact-level equivalence.
- **Exponent arithmetic / corollary:** After using reduced generating sets, the A-tail has exponent −(1/5−2η)k−2/5−η, while F starts at −2/5+η. The claimed μ_ℓ≤ℓ^{−2/5+o(1)} follows. Counting completely caught first-level cylinders gives O(ℓ^{3/5+o(1)}) bad g₀. LOGIC2 Theorem D then applies as cited. I found no circularity in this argument.
- **S1/S2 structure:** W1/W2 are complete for eventually positive integral polynomial words with t,u,v≥2: exactly one coordinate can be nonconstant, and it must be linear. This does not classify arbitrary non-polynomial word-producing methods. The W1 character and W2 2-adic quotient formula are correct. For large-s W2, r²≤N+s and s≤N+r give r<√(2N)+1, which justifies the scan and its cofactor bound. The corresponding W1 bounds and the harmonic-sum candidate count also check out. Positive remaining Haar mass really does imply a nonempty complement; there is no compactness/measure gap there.
- **Replays:** Compiled all three C programs with `gcc -O2`. Reproduced `tree.py 17 3`: event counts 6,46,300 and survivor counts 2,26,396; and `stree.py 11 6 11`, including its positive branch bounds. Literal ET brute output for ℓ=17, MMAX=100000 matched the stored file; its 106 distinct (level,residue) pairs through level 3 all occur in the exact list. The S brute output at ℓ=17, A,uv≤30000 matched its stored file; independent filtering of exact output agreed on all 45 distinct (level,residue,family) keys (79 emitted good rows). The 95/77 good rows for ℓ=11/13 also reproduce when non-unit residues are excluded.

All compute commands used the requested 4 GB virtual-memory limit and 1200-second timeout, with at most two simultaneous jobs. No large dense Cartesian-product computation was used.

**Bottom line:** Preserve and carefully restate Theorem T and Corollary T.1. Repair the numerical certification of Theorem S. Withdraw/recompute §5’s two-prime evidence before accepting or exporting the memo.
