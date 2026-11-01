# HYPSUMPROD hostile cross-review

Reviewed `side-agent/z53-hypsumprod` at `f4377ccc842b4046ee8c03b4cb6875308b003ec1`, principally `Z53_HYPSUMPROD.md` §3.
**Verdict: ACCEPT-WITH-FIXES. Theorem 1 survives; no exponent or coverage gap found.** ES remains OPEN.

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| Three fibrations; elementary block exponent | CORRECT | Direct factorisation; fixing any coordinate leaves a divisor count. Also n/4 ≤ uBC ≤ n/2. |
| §3.1 ranges; Lemma 1.1 square detection | CORRECT | M(4T^(2−2η)−2) ≤ n; parity and positivity give integral positive roots. Ordered multiplicity ≤2; u=B contributes ≤τ(n). |
| Lemma 1.2 square sieve | CORRECT-WITH-FIX | Valid self-contained variant, not the exact statement of Heath-Brown's Theorem 1; distinguish these explicitly. |
| Lemma 1.3 complete Jacobi sums | CORRECT | Discriminant 16(4cn+1); linear case c=0 gives 0, repeated-root case q−1, otherwise −1. CRT factorisation is exact. |
| §3.5 main term/discrepancy split | CORRECT | Half-open endpoint identity is exact, including integer endpoints; decreasing weights give the claimed AP bound. |
| Lemma 1.4 third-derivative discrepancy | CORRECT | All powers of Q, W, T and H re-derived below; there is no missing Q² class factor. |
| Theorem 1(a,b,c) | CORRECT | Exponents 24/25+2η, 74/225 and 8/25 follow. Shiu supplies the exact logarithmic version of (b). |
| Props B, C; Fejér/max-input floor; divisor-class floors | CORRECT, scoped | Averaging proves B and C; inserting square-root max input gives √(UV) ≥ min(U,V,W). Per-fibre majorants do not prove most fibres empty. |
| Lemma D, Z1855 reduction | CORRECT | m=4uC−1 and Bm=n+u are inverse parametrisations; u divides n+B. Not a general impossibility theorem. |
| Lemma A / Cor A′ | CORRECT-WITH-FIX | Algebraic bijection and universal congruence implication are correct. Strict Type II terminology for composite n needs the coprimality qualification below. |
| Lower-bound-tool survey; full-Type-II obstruction | Assessment, not theorem | Appropriate only as statements about the listed implementations. The tie-free main term is not a lower bound for the tied count. |
| §4 off-cube grid, candidate 0.3272 | EVIDENCE only | Correctly not used to prove Theorem 1. Sampling shapes and frequency exponents does not certify a continuous optimum. |
| §7 exhaustive counts / character controls | CERTIFIED / EVIDENCE as labelled | Full exhaustive output reproduced byte-for-byte; all eight bijection cases and four large controls agree. |
| §9 strengthened/narrowed; novelty | Supported with scope | Restricted R(n) counting benchmark improves; not full Type II, not positivity, and not certified literature priority. |

## Square-sieve source and hypotheses

Read the original Heath-Brown, *Math. Ann.* 266 (1984), pp. 251–253, Theorem 1 and its proof:
[GDZ scan, p. 251](https://gdz.sub.uni-goettingen.de/iiif/image/gdz:PPN235181684_0266:00000253/full/1800,/0/default.jpg),
[article record](https://eudml.org/doc/163852).
The original has nonnegative summable weights on **all integers**, w(0)=0 and w(a)=0 for |a|≥exp(P₀), and concludes
Σ_m w(m²) ≪ P₀⁻¹Σ_a w(a) + P₀⁻²Σ_{q≠q′}|Σ_a w(a)(a/qq′)|.
Thus negative values are explicitly allowed; primes dividing n are not excluded by this theorem.
The memo instead only restricts supported **positive squares** to a≤2^P₀ and proves constants 4,4 directly.
That proof is valid: ω(m)≤log₂m≤P₀/2; every square has at least P₀/2 nonzero Legendre symbols, and all added weights times squared character sums are nonnegative.
Zero values must be removed and are removed. For the strip, even the original stronger support hypothesis holds eventually:
|f|≪T^(2+4η)+T^(2+η), whereas P₀≫T^(1/25)/log T. No circular assumption about the number of squares occurs.
The threshold P₀≥3log₂T is sufficient for the memo's variant, uniformly for η≤1/20.

## Independent exponent reconstruction

On a dyadic C-piece C≈W, write C=c₀+Qj; N≪W/Q, g(j)=(n+S)/(4Q(c₀+Qj))−k₀/Q.
Then (hg)'''=−(3/2)h(n+S)Q²/C⁴, with magnitude comparable to λ=hT³Q²/W⁴ (ratio ≤16).
The third-derivative bound Nλ^(1/6)+N^(1/2)λ^(−1/6) gives respectively
h^(1/6)T^(1/2)W^(1/3)Q^(−2/3) and h^(−1/6)T^(−1/2)W^(7/6)Q^(−5/6).
Vaaler's inequality therefore bounds each endpoint/class by
T^(1+2η)/(QH) + H^(1/6)T^(5/6+2η/3)Q^(−2/3) + T^(2/3+7η/3)Q^(−5/6)log(2H).
With H=ceil(T^(1/7)Q^(−2/7)), the first term is T^(6/7+2η)Q^(−5/7);
the second actually has the smaller η-loss 2η/3 and is bounded by the same expression.
Multiplying by Q² classes, two endpoints and O(log T) pieces yields exactly Lemma 1.4.
The monotone-weight main term is ≤4Σ_J/Q+3J_max ≪ T^(1+2η)log T/Q+T^(3η), and |A|≪T^(1+2η)log T.
For P=T^ρ, Q≈P², the relevant T-exponents are 1+2η−ρ, 6/7+2η+18ρ/7, and 2/3+7η/3+7ρ/3.
Balancing the first two gives ρ=1/25 and exponent 24/25+2η; the third is 19/25+7η/3≤263/300<0.88.
The omitted main-term exponent 1+2η−2/25 is smaller; τ(n) is also negligible. At the cube H≈T^(3/25), and division by 3 gives 8/25.
The P₀⁻¹ diagonal costs one logarithm, |A| another; the discrepancy uses at most log²T. No n^ε loss is hidden in the near-cube result.
Checked the derivative input against Heath-Brown's later [k-th derivative paper](https://ora.ox.ac.uk/objects/uuid:18acb1dd-6b8b-43a7-8205-2b97a6da55fb/files/md99f066b322997f619c4e9e272ebd878), eq. (1), k=3.
Vaaler's coefficient envelope was checked against [Ma–Sun, Lemma 2.1](https://arxiv.org/pdf/2109.02924): pairing ±h gives 1/(πh)+1/(H+1). Original Vaaler PDF access was blocked.

## ALL complementary blocks and Shiu

Put X=T^(1−η). Every triple either has u<X, B<X or C<X, or belongs to S_η. This is an exact covering, not a grid argument.
The three complementary counts are bounded by Σ_{u<X}τ(n+u), its B-analogue, and Σ_{C<X}τ(4nC+1).
Read Shiu's original Theorem 1, p. 163 (`sources/shiu-1980.pdf`): k<y^(1−α), x^β<y≤x, 0<α,β<1/2, (a,k)=1; f=τ satisfies its growth conditions.
Take α=1/5, β=1/4 (the memo swaps the letters in its abbreviated modulus condition, harmlessly).
For the short interval, x≈n, y≈X=n^((1−η)/3)>x^(1/4); use the usual trivial-modulus version.
For C, take k=4n, a=1, x=y≈4nX. At η=1/75, y^(4/5)≈n^(1196/1125), so k<y^(4/5) holds with a fixed power margin.
Moreover exp(Σ_{ℓ≤x,ℓ∤k}2/ℓ)≪(log x)²(φ(k)/k)², giving O((y/k)(φ(k)/k)log x)≤O(X log n).
Consequently the complement has exponent (1−η)/3, **equal to**, not strictly below, 74/225 at η=1/75; equality suffices.
Since 24/25+2/75=1−1/75=74/75, every block is covered with the claimed bound. The pointwise divisor bound alone would only give 74/225+o(1).

## Numerical reproduction

Inspected allocations and integer ranges before running: four arrays total 7(X+1) bytes at X=500000000 (about 3.5 GB).
All shell invocations had ulimits and timeouts; the exhaustive executable had 6,000,000 KiB virtual-memory and 1500-second limits; exit status 0.
Recompiled and reran `z53_hypsumprod_rmax.c 500000000`; `cmp` agrees with `data/z53/hypsumprod/rmax_5e8.txt`.
SHA256 of both: `518b00dcf94a72ebb4be7c3bb8fa39f667aedc9081173edd78f2e15a93762181`.
Confirmed max Q=22 at 199582860, prime-1-mod-4 max Q=16 at 9405457, max R=439 at 480134654; top means 50.813 and 63.279.
R saturation would have printed 65535, so the observed maximum rules out saturation and also Q-counter wraparound (Q≤R).
All eight stated n-values pass the independent brute-vs-square comparison in the supplied executable.
Large controls reproduce (|A|,max|S_Q|,rms): (60774,614,256.6), (60773,597,259.0), (60676,636,272.6), (60635,612,232.2).
Separate direct modular enumeration verifies 8,253 (n,c,q) cases for odd primes q≤43 and 4,018 CRT cases; exact rational arithmetic confirms every exponent above.
These checks validate finite outputs, not an asymptotic square-root character-sum theorem. The full exponent grid was not rerun and is not needed for the verdict.

## Literature and required fixes (priority order)

1. **Qualify composite-n Type II language in Lemma A and the summaries.** The algebraic quadruples are correct, but Elsholtz–Tao additionally require gcd(abd,n)=1. Counterexample: n=12, (a,b,c,d)=(2,2,1,1), H=1, (x,y)=(7,7) satisfies the tie yet gives denominators (4,24,24), not strict Type II. Call these algebraic quadruples, restrict the Type II interpretation to primes, or add the coprimality filter. Theorem 1 is unaffected.
2. **Call Lemma 1.2 a proved variant of Heath-Brown's theorem**, and quote the original support hypothesis separately, as above. Its actual proof needs no repair. Also fix §0's “±1 except on one class” shorthand: the c=0 class gives 0, independently of the exceptional discriminant class; Lemma 1.3 already handles this correctly.
3. **Correct the Elsholtz–Tao product in §3 Remark 4 to e²·ad·ac·cd=(acde)²≤n².** Read their [paper](https://arxiv.org/pdf/1107.1010), Prop. 1.7, Prop. 2.6, equations (2.13)–(2.22), and §3: f_II(n)≪n^(2/5+O(1/log log n)) counts the full family, whereas R is the c=1 algebraic slice. Their bound neither subsumes 74/225 for this slice nor is improved by it. The stated extremal exponents (1/5,3/5,1/5,1/5,2/5) are consistent after restoring e².
4. **Retain unverified-priority wording.** Targeted searches did not establish a predecessor, but some searches failed or returned inaccessible material; absence of a hit is not a novelty certificate. Do not advertise an improvement to the full Type II bound.

With these local fixes, “strengthened” for the restricted counting benchmark and “narrowed” for the specified majorants follow. No ES positivity claim, general method exclusion, or continuous-grid optimum is warranted.
