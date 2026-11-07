# z62 INVERSE — cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES.** Audited `side-agent/z62-inverse` at `c8792ef3`, including checkpoint `6500828e`.
The elementary core survives; the QR-only interpretation is false, the novelty attribution is incomplete, and the empirical verdict needs narrowing. **ES remains OPEN.**

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| Two slicings | CORRECT | For fixed u, d = 4uC−1 divides n+u and B = (n+u)/d. For fixed C, (4Cu−1)(4CB−1) = 4Cn+1; each divisor ≡ −1 gives an ordered pair (u,B). |
| h/B/T/Q/S partition | CORRECT | Div ⊆ H. A B-kill is an odd real character trivial on H, hence cannot hit. Real characters factor through G/G²: a real odd annihilator exists iff −1 ∉ HG². If −1 ∉ H but lies in HG², character separation on G/H supplies only non-real odd annihilators. Remaining failures have −1 ∈ H but not Div. “Random” is a name for S, not a stochastic theorem. |
| Lemma 1(a–c) | CORRECT | For odd relevant ℓ, −u ≡ p, or −4C ≡ p⁻¹, modulo ℓ. Reciprocity at p ≡ 1 (4) gives (−4u/ℓ) or (−4C/ℓ) = (ℓ/p). When u < p, every odd factor of p+u is coprime to u; factoring (p+u)/p gives the stated 2-adic correction. |
| Lemma 2, converse, 409 example | CORRECT | λ(m)=2 exactly for m=4,8,12,24 among multiples of 4. Squarefree products realize every element of H there. Otherwise choose ord(g)>2 and primes in classes g,−g: H contains −1 but {1,g,−g,−g²} does not. For 413=7·59 mod 16 the stated Div and full H are correct. This is an abstract-slice converse; census evidence separately checks actual u/C slices. |
| Corollary 3 | CORRECT | Odd real characters at m=4,8,12,24 are precisely those listed. At u=2, p+2≡3 (8) excludes χ₋₄; at u=6, p+6≡7 (24) excludes χ₋₄ and χ₋₈. For u=3, the coprime part is (p+3)/4=6j+1, and χ₋₄ is possible only for p≡1 (16). C-slices have N≡1 (4C), excluding no odd character. Transfer gives all five clauses; all 14 zeros verified independently. |
| Cor 3 primitive-form reading | CORRECT | Item (i) implies all prime factors of (p+1)/2 and 4p+1 are 1 mod 4, and all factors of p+2 split for discriminant −8. Unique factorization in the corresponding class-number-one rings gives the stated primitive representations. This reading concerns item (i), not every alternative. |
| Prop 4, Dickson clause | CORRECT, CONDITIONAL | All integer forms have constant term 1, so t=0 witnesses admissibility at every prime. Slopes are distinct: q-slopes ≤ L/2, r-slopes ≥4L/5 and <L, with p-slope L. The prime multipliers are 1 modulo their slice modulus; adjoining them leaves Div unchanged, even if a multiplier repeats a fixed factor. The n=1 divisor sets miss −1 and are B-killed. This is ∀ fixed K, infinitely many p, not a growing-K theorem. |
| Prop 4, congruence/Type I clause | CORRECT | Congruence-determined certificates failing at 1 fail at p≡1 (L); Dirichlet supplies infinitely many such primes without the slice claim. If f divides 4dt²+1 then χ₋₄d(f)=1, whereas f≡−1 (4dt) gives −1. The STEP2 exclusion is confined to these certificates, not arbitrary adaptive certificates or growing scales. |
| Prop 4 scale remarks | CORRECT with stated scope | The imported HCSHIFTS wall concerns fixed families and non-least members, as disclosed. For this particular construction even p≥L+1 and lcm(1,…,K) divides L give a logarithmic bound directly. The Bateman–Horn growing-scale estimate is heuristic, not furnished by ordinary fixed-K Dickson. |
| Lemma 5 | CORRECT-WITH-FIX | On relevant ℓ, (−u/ℓ)=(n/ℓ), and twisting gives (ns/ℓ)=((n/s)/ℓ). If r is the squarefree kernel of s, use the primitive character of discriminant r or 4r, induced to modulus 4u; its conductor divides 4u iff r divides u. The literal χ_s/χ₄s for non-squarefree s has extra zeros: s=9,u=1 gives χ₉(3)=0, so it is not a character modulo 4 despite conductor 1. Restrict the equality to ℓ∤s (automatic for relevant factors). Same repair at C. For prime p and u<p, p∤D′, so pD′ is nonsquare: the transfer conclusion is valid. |
| Lemma 6 | CORRECT (state p prime explicitly) | The Type I conditions force coprimality, and 1=χ₋₄d(f)=χ₋₄d(−p)=−(d/p). For a hit divisor, χ₋₄u(d)=−1, so multiplicativity and Lemma 1 produce a non-residue factor; likewise for C. This proves the claims for the displayed witness families. |
| “Forced structure supplies only residue primes” | WRONG | At the genuine zero p=577, u=3 has p+3=4·5·29, both odd factors 1 mod 4, but (5/577)=(577/5)=−1. This is a T-kill allowed by Cor 3(ii). Moreover its factor 5 supplies the displayed Type I witness (d,t,f)=(5,1,3): 3 divides 21 and 3≡−577 (20). Restrict QR-only language to Cor 3(i) and B-killed slices; delete the general anti-support inference. |

## Registration and statistical verdict

Checkpoint `6500828e` (2026-11-07 11:24:51 +01:00) fixes the fresh interval, R≤2 selection, ±50 same-class-prime window median, three nearest controls, both families/bands, and both ±0.05 tests. Fresh code/data/results first enter descendant `d1c45055` (11:44:16). The implemented selection matches that checkpoint exactly. This supports **repository pre-registration**; git cannot establish the absence of earlier uncommitted runs. The earlier census was explicitly exploratory.

Independently recomputed pooled conditional-share differences (near-zero minus control):

| Family/band | Δ structured | Δ B | Pre-set point criterion |
|---|---:|---:|---|
| u 17–64 | −0.011334 | +0.023933 | pass |
| u 65–256 | +0.026102 | +0.047782 | pass |
| C 17–64 | −0.031114 | −0.000061 | pass |
| C 65–256 | +0.007347 | −0.005762 | pass |

The original bootstrap rerun reproduces every reported SE. Nevertheless:
- Six near-zeros, all R=2, are not a confirmatory sample of zeros; the fourteen actual zeros were already explored.
- Passing a point-estimate tolerance is not an equivalence test. For example ΔB=0.0478 with SE=0.035 has a rough 95% interval [−0.021,0.116], far outside the equivalence margin. Resampling independent rows also does not preserve the matched near-zero/control triplets.
- The registered test checks B and B+T+Q, not the full distribution, individual indices, or general cross-slice structure. Our separate T/Q differences are also small here, but that does not make the registered statistic omnibus.
- The zero-set B residuals reproduce (+0.039462 at u 65–256; +0.032902 at C 65–256). Calling them “small-M_BM selection” is an untested explanation, not a result of conditioning on failure.
- Test 2's [1/3,3] band is an operational factor-three tolerance, not an independence test. Reproduced first/fresh-window O/E: U=16, 0.73/0.67; U=32, 1.48/0.72; U=64, 3.19/1.65. The memo correctly discloses repulsion and the first-window U=64 excess.
- Test 3 is post-hoc and tests one all-fail event against fitted signature-conditioned marginals, not full independence of private layers. I inspected its aggregator but did not regenerate the private-layer files; its numerical tables are not independently certified by this review.

Thus “registered operational kill fired” is accurate; “no structure beyond selection,” “the statistics say no,” and killing INV-main with K(p)→∞ do **not** follow. Use **narrowed / no excess above the chosen point threshold in the tested summaries**, at u,C≤256 and n≤10⁸, with the disclosed residuals and power limits. Assessment labels do not repair an invalid inference. Keep the separate F2 population near 10¹⁰ explicitly outside that inferential scope.

## Falsifiers and prior work

| Screen | Review |
|---|---|
| F1 odd squares | CORRECT: relevant factors see a nonzero square in the Jacobi transfer, hence every slice is B. Checked 768 square slices. Conditional mimicry defeats the stated bounded certificate strategy, not all prime-only inverse theorems. |
| F2 C-even/R₈ | CORRECT parity distinction; all 12 screen primes occur, and independently recomputed even-C slices through 256 never hit. “35% of cases” means 17/48 u≤4 **slices**, not primes: 7/12 primes have such a hit. R≥12 is inherited from the screen ledger, not a new full 10¹⁰-range verification here. |
| F3 composites | All 285 screen integers occur; structured excesses independently reproduce: u +0.056819/+0.086054, C +0.053086/+0.070094. T is the largest contributor. Lemma 5 gives a valid partial-square mechanism, not a proof that it accounts for every excess or every composite zero; the corrected checkpoint description is appropriate. |
| F4 prime zeros | Exact membership: 14 Z plus 24 G gives all 38 𝔊*-zeros. Cor 3 verified on all 14 Z; excluding the 24 R>0 primes from its hypothesis is correct. Their mere census inclusion is not a comparative test. No HOT LEAD or positivity claim is justified or made. |

Attributions checked in the source memos: `Z52D_FOURIER` §§0(b),3.2–3.3,4.2 already supplies the BM/genus/non-real/poverty taxonomy, real-character coset decomposition, and selection interpretation; final credit is appropriate. `Z54_HCKILL` Lemma 1.2 supplies the exponent-2 criterion/converse; `CAP_BOUNDED` Lemma 1.1 and Thm 1.3 supply transfer and constant-times-prime mechanism. For the non-residue barrier cite `Z57_BFII` Prop 2.2/Cor 2.4, not merely its auxiliary Lemma 2.1, alongside `Z59_MSPF` Lemma 1.5.

**Missing prior:** `Z60_LOPEZ` Prop D(a,T), not only its unconditional clause, already simultaneously constructs p+k=(k+1)q_k and kp+1=(k+1)Q_k with multipliers 1 modulo L_k. Its proof uses M divisible by 4k(k+1). Taking X=4K, k=u for u-slices and k=4C for C-slices yields Prop 4's divisor-residue mimicry (q_u is actually 1 mod 4u from that M). The C-slice extension and whole-vector identification are therefore already implicit in this explicit prior construction; call Prop 4 a specialization/repackaging, not new two-slicing mimicry.

## Reproduction and required fixes

Independent script: `scripts/z62_xrev_inverse_audit.py`; inputs extracted from the audited commit under `/tmp/xrev_INVERSE`.
All compute used `ulimit -v 4000000`, timeouts ≤950 seconds per tool call, and at most two concurrent compute processes.
- `timeout 900 uv run --with sympy python scripts/z62_xrev_inverse_audit.py /tmp/xrev_INVERSE`: SymPy factorization, actual integer divisors, cyclic-subgroup products; **31,744 slices / 62 rows, zero mismatches**, including all 24 fresh rows, all 14 zeros, all 12 R₈ primes, and stratified other rows. All five codes occur.
- Recompiled/reran lane `z62_inverse_rsieve.c` through 10⁸, then independently rebuilt near-zero/control selection with the audit script's `--rfile` option: **six near-zeros, exact 18 controls, fourteen total prime zeros, none fresh**. This is a rerun of the original sieve, not a second sieve algorithm.
- Recompiled/reran `z62_inverse_joint.c` for both complete windows and `z62_inverse_joint_oe2.py ... 840 11,13`: every main Test 2 number agrees. No unbounded arrays or dense Cartesian-product checks were used.
- Cor 3 and the QR-only counterexample checked independently; all 1,255 stored rows satisfy exponent-2 consistency. Finite Prop 4 examples reproduced at (K,L,t,p)=(1,840,11,9241) and (2,2520,477,1202041), without treating examples as proof of Dickson.

Required fixes, in priority order:
1. Remove the false QR-only/anti-support assertion for the entirety of Cor 3; retain only the properly scoped B/Cor 3(i) statement and acknowledge the p=577 counterexample.
2. Narrow the title, verdict, proposed FRONTIER text, and bottom line to the operational finite-summary result. Do not infer equivalence, a causal selection explanation, private-layer independence, or death of a growing-scale inverse theorem.
3. Credit `Z60_LOPEZ` Prop D(a,T) for both slicings and divisor-residue mimicry; correct the `Z57_BFII` citation.
4. Normalize Lemma 5's twist via the squarefree kernel and induction; explicitly assume prime p in Lemma 6; clarify F2's slice denominator.

**Disposition:** retain the proofs and reproducible finite census after these fixes; retain “narrowed, no HOT LEAD,” not a mathematical elimination of INV-main or unrestricted STEP2.
