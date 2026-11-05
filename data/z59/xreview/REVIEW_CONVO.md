# z59 hostile cross-model review — CONVO

**Verdict: ACCEPT-WITH-FIXES.** The numbered algebraic results are correct; the numerical headlines reproduce. The falsifier audit is incomplete/mis-scoped, several prose barriers overclaim, and most structural content (including Theorem 7.7) is prior. Accept as a checked reformulation/computation memo, not a new pointwise mechanism. **ES remains open.**

Snapshot: `side-agent/z59-convo` at `a06fac2163e9ad98ad69a2100f3ea7dfe6c11634`, `Z59_CONVO.md`. Author files untouched. Independent review, not reliance on the author's earlier reviewer.

## Per-claim proof audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| Lemmas 1.1–1.2 | CORRECT | Divide the equation by c to get 4abd=n+ρ, ρc=a+b. Conversely the two divisibilities reconstruct positive integral c,d. Setting c=1, a=1, or 2∣d gives exactly the stated restrictions. Interpret divisibility of (n+ρ)/4 as requiring that quotient integral. |
| Lemma 1.3 | CORRECT | b(4acd−1)=pc+a; multiply by 4ad and subtract p(4acd−1) to obtain fρ=p+4a²d. Conversely f≡−1 mod 4ac gives positive d=(f+1)/(4ac), and b=(pc+a)/f restores the equation. |
| Lemma 2.1, including square obstruction and ab≥q(p) | CORRECT | The size inequality excludes a≥p or b≥p. The product identity gives gcd(2cdp,f)=1 and (−dp/f)=1 prime-factor by prime-factor. Since f≡−1 mod 4d, reciprocity gives (d/f)=1 and (−d/f)=−1, hence (p/f)=−1. Reciprocity and bf≡a mod p yield (ab/p)=−1. Multiplicativity forces a non-residue prime factor of ab. For n=m² the same Jacobi calculation contradicts (m²/f)=1 without primality or a coprimality assumption on m,ρ. In fact the prime result holds already for p≡1 mod 4. |
| Criterion 3.1, consecutive-integer version | CORRECT | ρ≤a+b≤ab+1≤(p+ρ)/4+1 gives ρ≤(p+4)/3<p. A common prime divisor of Nρ and ρ would divide p, impossible. Thus a,b are units and a+b≡0 iff a/b=−1. Conversely any such pair reconstructs a solution. The unbounded j version is also equivalent: any hit automatically satisfies the same bound. This is an equivalence, **not a positivity theorem**. |
| Identity 3.2 | CORRECT | Character orthogonality applied to −a/b gives Wρ=φ(ρ)⁻¹Σψ ψ(−1)Σabd=N ψ(a)ψ̄(b). Independent prime-power choices give the stated multiplicative local factor. Requires gcd(Nρ,ρ)=1, as stated. |
| Lemma 3.3 | CORRECT | Jacobi reciprocity gives (ℓ/ρ)=(−ρ/ℓ)=(n/ℓ) for odd ℓ∤ρ; the ℓ=2 case uses n≡1 mod 8. For coprime odd squares every prime factor has λ=1, while λ(−1)=−1, so every ratio misses −1. Non-coprime squares are handled by Lemma 2.1, not the unit-group expansion. For primes, τ₀−τλ counts twice the triples with λ(ab)=−1, and positivity is equivalent to an escaping prime factor. It does **not** imply Wρ>0. |
| Corollary 3.4 | CORRECT | Modulo 3 there are only two characters, so escape is sufficient there. If ρ∣p+4 then Nρ≡−1 mod ρ and (a,b)=(Nρ,1) works. Keep the standing ρ≡3 mod 4 convention. |
| Lemmas 4.1–4.2 | CORRECT | Reciprocity identifies λρ(ℓ) with χp(ℓ). The product λρ(Nρ)=(p/ρ)=−1 forces an odd number of negative factors; 2 contributes +1 on the standing domain. The same reciprocity identity exists for coprime composite n with its Jacobi character: the prime-specific distinction is conductor/nontriviality, not the algebra alone. |
| Lemmas 5.1–5.2 | CORRECT | If ab∣L then 4ab∣ρ+1, forcing ρ≥4ab−1>a+b. For finite S, the stated progression makes every q∈S a residue modulo p; an S-supported ab contradicts Lemma 2.1. Dirichlet applies to the progression 1 modulo the lcm with 24. These exclude fixed pairs or finite prime support, **not all residue-based arguments**. |
| Theorem 7.7 | CORRECT, CONDITIONAL | Nρ=sρPρ, Pρ>sρ and Pρ≡1 mod ρ. Every ab∣Nρ has a+b≡x+y with xy∣sρ and 2≤x+y≤sρ+1<ρ. The distinct linear forms have positive slopes, content 1 and product 1 at t=0, hence no fixed prime divisor. Hypothesis H supplies infinitely many simultaneous prime values. Dickson already suffices; H is not proved. The min∅=∞ convention correctly avoids assuming solvability. |
| §7 failed constructions / §8 universal methodological conclusion | CORRECT-WITH-FIX | These are unsuccessful attempts, not impossibility theorems for Pell, descent, short-interval methods, or every bounded-order-character argument. State only the actual finite-support barriers, failure of the single-character escape implication, and conditional bounded-ρ obstruction. |

Checked H's precise **product** admissibility formulation against [the hypothesis statement](https://en.wikipedia.org/wiki/Schinzel%27s_hypothesis_H), also [MathWorld](https://mathworld.wolfram.com/SchinzelsHypothesis.html); all forms here equal 1 at 0, so admissibility is especially direct. No analytic theorem is being used to manufacture pointwise positivity.

## Decisive computations

All executions used `ulimit -v 4000000` and timeouts ≤1800 seconds. Reviewer scripts are `scripts/z59_xrev_convo_census.c` and `scripts/z59_xrev_convo_check.py`; invocation instructions are in their headers. Lane files were archived to `/tmp/xrev_CONVO/`. No large Cartesian-product arrays; the independent C census allocates <210 MB.

- **Full 10⁸ census independently reproduced**, using a prime/SPF sieve and signed-prime-exponent residue DP, not the lane's divisor-pair search. Each ℓᵉ contributes exponents −e,…,e, exactly the possible differences vℓ(a)−vℓ(b) with ab∣N. Count **719781**, maximum minimum ρ **107**. Records: **73→7, 1129→11, 1201→23, 21169→31, 67369→35, 87481→63, 1430641→71, 8803369→107**.
- Exact histogram bins ≤4, (4,8], (8,16], (16,32], (32,64], (64,128]: **430409, 235146, 42772, 10859, 585, 10**. All memo percentages agree. At p≤3·10⁶, ρ=3 succeeds at **14878/26983 = 55.1384%**, agreeing with “55%”.
- Independent complete (a,b)-enumeration verifies the character lemma for **all solutions** at every p≡1 mod 8 below 20000, and no solutions at odd m² with m≤149. Author's `z59_convo_check_lemmas.py` also reruns to **bad 0**.
- The independent enumerator matches every minimum ab and minimum q-divisible ab in **all 2212** rows of `nr_small.txt`. Maximum **49170 at p=186841**; exactly **30** no-q-witness cases. All three unordered solutions at **2521** agree. In fact all 30 absences are complete, not merely search-limit evidence: 4ab≤p+a+b≤p+ab+1 implies ab≤(p+1)/3<66667 for p≤200000, far below 2·10⁶.
- The five escaping but failing ρ values for **4545**, and **43,59,67,83,103** for **8803369**, all reproduce, including factorizations and first success **107**. Complete enumeration confirms NII(4545)=0.
- All **11** numerical examples of Theorem 7.7 reproduce: primality of every required form, and the stated minimum ρ for R=7,15,23.
- Author's mode-3 scan independently rerun to 3·10⁶ returns the exact **15** listed d-even prime zeros among **108283** primes p≡1 mod 4. All **22** prior K=8 prime zeros were additionally tested by a separate exhaustive K=8 enumerator; see the scope correction below.

## Mandatory falsifier audit

| Screen | Finding and correction |
|---|---|
| **F1 odd squares** | PASS. The proof really excludes every odd square, including gcd(m,ρ)>1. Preserve that qualification in the closing prose: “all residues lie in ker λρ” only applies when the unit-group formulation applies. |
| **F2 C-even / numerator-8 sub-line** | **INCOMPLETE in memo.** F2 is c=1 **and** d even, not unrestricted d even. At all **12** archived R8-zeros, I find full-family witnesses with minimum ρ≤15 and d-even witnesses with minimum ρ≤31; every latter witness has c>1. Example at 10156800001: **(17,53,10,2818202)**, ρ=7. Thus full d-even survives these 12, whereas its c=1 sub-line fails. Distinguish these predicates explicitly. |
| **F2 “15 versus 22” discrepancy** | **WRONG claim that the counts cannot describe the same property.** The 22 are over **all odd primes**; the 15 scan is restricted to p≡1 mod 4. Exactly the missing seven are **3,11,19,131,491,739,2531**, all 3 mod 4 (`data/z58/wildcard/census_K8_1e7.txt`). Their failure independently checks. Delete “unreconciled”; the counts are consistent. |
| **F3 285 composite zeros** | **INCOMPLETE in memo**, which tests only 4545. Independent divisibility search finds witnesses with minimum ρ≤51 at **284/285**, and complete enumeration leaves **4545** alone. The ratio-in-units criterion is prime-scoped; for composite screens I use the unrestricted divisibility form, not illegitimate inverses. The 4545 example genuinely refutes escape⇒solution, but cannot refute every argument exploiting the full primitive conductor p. |
| **F4 14 (★) and 38 𝔊* zeros** | **INCOMPLETE in memo.** Replacing the 38 by the three a=1 zeros is not the requested test. All **14** and all **38** have full witnesses with minimum ρ≤23; all 14 stated minimum values reproduce. The 14 require c≥2; the 38 need not: **37 has (1,2,1,5)**. The a=1 zeros 193,2521,66529 are a useful **additional** screen and their minima 7,23,31 agree. |

These are bounded checks, not proof that a mechanism “survives” beyond the tested ranges. No HOT LEAD is justified or claimed.

## Priority / novelty versus repository

`git grep` and direct source reads establish the following prior content; being unprimed explains rediscovery but does not confer novelty.

- **Exact forms and square/QNR obstruction:** `Z57_BFII.md` Lemma 1.1(a)–(e), Proposition 2.2 and Corollary 2.3; `Z58_CONVF.md` Lemmas 1.1–1.3. CONVO's ρ is their e/σ. The character expansion is a useful coordinate presentation of the same divisor-ratio problem, not a new positivity result.
- **Even-d/numerator-8 distinction, 4545, and complete screen behaviour:** `Z58_WILDCARD.md` §0 and Lemma 4.1 already give these, with stronger census ranges. `Z58_CONVF.md` §0 already separates F2's sub-line and the 38 𝔊* zeros.
- **ρ=3 exact criterion:** already explicit in `Z58_CONVF.md` Lemma 1.5's proof. **a=1 / (★) exceptions and their union:** prior `B1_LINE.md` §§0,2,3.6; `Z58_CONVF.md` §2 explicitly attributes them to López/B1_LINE.
- **Character ab/p and fixed-pair obstruction:** `JOINT_BUDGET.md` Remark 4.4 already states (ab/p)=−1 for Type II, and Proposition 4.3 already proves 4ab∤p−1. Lemmas 2.1 and 5.1 here rederive these; finite-S exclusion is their immediate reciprocity consequence. `Z57_BFII.md` §3 separately proves no finite witness-modulus covering.
- **Theorem 7.7 is an exact prior specialization**, not merely analogous to `B1_LINE.md` Theorem 4.2: `DISPROOF_AVENUES.md` §3, Proposition 3.1, **Type II e-slice row**, already uses N=(p+e)/4, e(e+1)∣Q, prime P≡1 mod e, and 2≤x+y≤(e+5)/4<e to kill every finite set, conditionally on **Dickson**. B1_LINE is the earlier freezing mechanism; the full e-slice theorem is already in the repo.
- **Incremental outputs:** the independently checked minimum-ρ census, the least-non-residue divisibility census (including 2521), and this explicit ρ-character packaging. No new pointwise theorem or fundamentally new obstruction is established.

## Required fixes, in priority order

1. **Narrow the barriers (§§3–5,7–8).** “No residue condition on p supplies” a hit / “residue information alone is useless” is false literally: **p≡73 mod 168** forces ρ=7 via 7∣p+4, giving (a,b,c,d)=((p+7)/4,1,(p+11)/28,1). Lemmas 5.1–5.2 exclude specified finite-support coverings, not all congruence arguments. Likewise the examples disprove the one-character escape implication, not all bounded-order-character methods. State failures of the attempted methods, not necessities for every possible proof. Keep bounded-ρ unboundedness explicitly conditional and do not imply ρ must tend monotonically to infinity.
2. **Replace the F2/F4 substitutions with the actual screens; complete F3.** Incorporate the checked outcomes above and reconcile 15 versus 22 by the prime domain. Do not conflate C-even (★) with full even-d Type II.
3. **Attribute all prior results**, especially Theorem 7.7's exact e-slice predecessor. The unprimed lane produces independent derivations, not priority.
4. **Fix §7.1 “by §6 not bounded for q≥11”.** §6 proves no such unboundedness; it gives a finite maximum and some genuine nonexistence cases for the least-q restriction. Say that restriction is not universal (2521), while the finite-pair barrier separately rules out a universal finite menu. Optionally upgrade all 30 bounded-search absences using ab≤(p+1)/3.

**Final assessment:** the correct verdict is **inconclusive on pointwise solvability; useful checked repackaging and numerics**. The algebra and conditional theorem are bankable with attribution, but the current audit/prose requires the fixes above before export. Nothing proves or disproves ES.
