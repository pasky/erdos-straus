# Hostile referee report, round 3: the large-q depth claim

## Overall verdict: MAJOR repairs; no FATAL obstruction found

The substantive chain **C2 → high transitivity → product of alternating groups → an exp(−c n²) upper bound** survives this review. I found no family contradicting the pair-overlap bound and no small-odd-characteristic obstruction to the monodromy argument.

There is, however, a **false intermediate assertion as literally written**: the event E₂ is defined using distinct *words*, whereas C2 controls distinct *unordered classes*. Swapping u and v gives a positive-density counterexample to the stated O(1/q) estimate for E₂. This is repairable by changing the event, not the theorem. There are also substantive overclaims about full independence, a Θ(n²) exponent, and integer transfer. The all-n numerical constant needs a short analytic completion, supplied below.

| Target | Verdict |
|---|---|
| (1) C2's weighted sum and its three counting cases | **SOUND** |
| (1) The asserted consequence P(E₂) = O(1/q), with E₂ as defined | **MAJOR: false literally; precise repair below** |
| (2) Proposition 3.8 | **SOUND after that event-definition repair; minor endpoint clarifications** |
| (3)(i) CFSG step | **SOUND** |
| (3)(ii) Goursat, perfect core, pair-surjective product lemma | **SOUND** |
| (3)(iii) Coset derangements and constants | **SOUND numerically; MINOR missing all-n justification** |
| (4) Moment computation | **SOUND computation; MINOR overinterpretation** |
| (5) Summary / “What this means” / transfer | **MAJOR overclaiming** |

References below are to `EXSET_FUNCTION_FIELD.md` in the reviewed checkout. Only this report and `reviews/z51_ffield_r3_check.py` were created by this review; no existing repository files were edited and no commit was made.

## 1. Lemma C2 (§3.8, lines 422–444)

### 1.1 The weighted pair bound is SOUND

Write d = a+b, d′ = a′+b′, h = gcd(uv,u′v′), and γ = deg h. The weight is exactly q^(−d−d′+γ), so the target count at fixed degrees and γ is O_D(q^(d+d′−γ−1)). There are only O_D(1) degree choices and γ values. Counting ordered polynomial pairs rather than unordered classes only enlarges the count by a bounded factor.

For fixed h, every divisibility h | uv permits an allocation h = h₁h₂ with h₁ | u and h₂ | v, including repeated prime powers. Consequently

    #{(u,v): h | uv} ≤ τ(h) q^(d−γ),     τ(h) ≤ 2^γ.

Allocations whose factor degrees exceed a or b contribute zero; there is no negative-degree parameter space to count.

**Case (i): h not squarefree.** The number of monic nonsquarefree h of degree γ is at most q^(γ−1) (zero for γ=1). Dropping compatibility and replacing exact gcd by divisibility gives

    O_D(q^(γ−1) q^(d−γ) q^(d′−γ))
      = O_D(q^(d+d′−γ−1)).

Thus repeated factors do not defeat the argument: they themselves supply the missing power of q. The occurrence of “τ(h)²” outside the count over h should formally be replaced by its uniform bound, but this is harmless.

**Case (ii): h squarefree, γ<d′.** For each allocation h=h₁′h₂′, put u′=h₁′x′ and v′=h₂′y′. The pieces are coprime, so compatibility gives one residue class for x′ modulo h₂′ and one for y′ modulo h₁′. Their degrees are a′−deg h₁′ and b′−deg h₂′. Hence the counts are bounded by

    q^max(a′−γ,0),    q^max(b′−γ,0).

This remains valid when a residue class has no monic representative of the required degree: the bound is then simply an overcount. After choosing h and (u,v), the total bound is

    O_D(q^(d + max(a′−γ,0) + max(b′−γ,0))).

All four exponent cases check:

| Degree configuration | Extra exponent | Why it is ≤ d′−γ−1 |
|---|---:|---|
| a′≥γ, b′≥γ | d′−2γ | γ≥1 |
| a′≥γ, b′<γ | a′−γ | b′≥1 |
| a′<γ, b′≥γ | b′−γ | a′≥1 |
| a′<γ, b′<γ | 0 | γ≤d′−1 |

**Case (iii): h squarefree, γ=d′, so u′v′ | uv.** If d=γ as well, the products agree. Since all four degrees are positive, the sum difference has degree strictly below d. Compatibility therefore gives u+v=u′+v′, and equality of sum and product gives {u,v}={u′,v′}; these classes are excluded.

Otherwise γ<d. Allocate the prime factors of h into the four pairwise coprime pieces in the text:

    u′=α₁β₁, v′=α₂β₂, u=α₁α₂x, v=β₁β₂y.

All four displayed congruences are correct:

    β₁y ≡ α₂ (mod α₁),    β₂y ≡ α₁ (mod α₂),
    α₁x ≡ β₂ (mod β₁),    α₂x ≡ β₁ (mod β₂).

For example, modulo α₁ cancel the invertible β₂ from β₁β₂y ≡ α₂β₂. The other cancellations are equally legitimate. Unit pieces impose no conditions and cause no problem. CRT then fixes y modulo α₁α₂ and x modulo β₁β₂. Subtracting the degrees of the allocated factors and of these moduli gives exactly b−γ and a−γ, respectively, not b−deg h₁ or a−deg h₂.

There are O_D(q^γ) choices of the four pieces, and thus

    N_γ ≤ O_D(q^(γ + max(a−γ,0) + max(b−γ,0)))
        ≤ O_D(q^(d−1)).

The last inequality is the same four-case calculation, using γ≤d−1. This is the required exponent because d′=γ. Additional common factors of u and v do not invalidate the allocation or any cancellation; if they make compatibility impossible, the count only decreases.

**Adversarial families considered:** common repeated factors, shared linear factors, partial squarefree overlap, strict divisibility, and identical products with different factorizations. None evades the degree loss. In particular, identical products are not a hidden diagonal contribution: compatibility forces the excluded identical unordered class.

### 1.2 MAJOR: E₂ is the wrong event

At lines 420–425, E₂ is defined as “f has two distinct small-modulus witness words whose moduli have a common root.” This includes the two distinct ordered words

    (t,u,v), (t,v,u),     u≠v.

They have the *same* unordered class, which C2 expressly excludes.

Here is a quantitative counterexample to the stated consequence P(E₂)≤C(D)/q. Fix D=2 and any n≥4, and take shape (n−2,1,1). It is U-admissible. There are

    q^(n−2) · (q²−q) = q^n−q^(n−1)

ordered words with u≠v. Every image f satisfies the literal E₂ by swapping u and v. Finite flatness bounds the number of words above any f by D_σ=n(n−1), so

    P_f(E₂) ≥ (1−1/q)/(n(n−1)).

This is not O_n(1/q). Indeed, for D=2 the actual C2 sum over distinct unordered classes is zero, making the distinction particularly stark.

**Exact repair:** define E₂ throughout §§3.8–3.9 as

> There exist two distinct unordered small classes c={u,v} and c′={u′,v′}, both hit by f, with gcd(uv,u′v′)≠1.

Then C2 plus the union bound gives P(E₂)≤C(D)/q whenever 2D≤n. Every non-coprime tuple of *distinct classes* in Bonferroni contains such a pair, so the B(n)^j reduction is valid. In Proposition 3.8, distinct words of one fixed asymmetric shape give distinct unordered classes; the same repair validates its reduction. No new estimate is necessary.

### 1.3 Numerical checks and a MINOR normalization error

I reran the author's D=3 script and independently counted through product buckets, computing gcd once per pair of moduli and matching sum residues modulo that gcd. The independent code imports nothing from the author's checker, uses exact rational accumulation, and separates all three proof cases.

| D | q | Ordered q·C2 sum | Nonsquarefree | Strict containment | Other squarefree overlap |
|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 4.370370370 | 0.666666667 | 1.333333333 | 2.370370370 |
| 3 | 7 | 5.650145773 | 0.285714286 | 1.714285714 | 3.650145773 |
| 3 | 11 | 6.093163035 | 0.181818182 | 1.818181818 | 4.093163035 |
| 4 | 3 | 21.176954733 | 4.320987654 | 4.000000000 | 12.855967078 |
| 4 | 5 | 25.725440000 | 2.707200000 | 4.800000000 | 18.218240000 |

The three case columns also report q times the corresponding weighted sum. These finite checks do not establish asymptotics; the proof above does.

The text quotes 2.19, 2.83, 3.05: those are for **unordered pairs of classes**, because the author's script uses i<j. C2 states an **ordered** sum. Label the numerical convention explicitly or double the quoted values. This does not affect O_D(1/q).

## 2. Proposition 3.8 (§3.9, lines 464–480)

**Verdict: SOUND after the E₂ repair.** The following potential failures do not occur.

1. **Components versus orbits.** Over a common étale open subset U of A^n, the off-diagonal fibre power is finite étale. Its geometric connected components correspond to geometric-monodromy orbits on ordered distinct k-tuples. Since U is smooth and geometrically integral, the finite étale scheme is smooth; its connected components are irreducible. Each has dimension n. Taking the closure adds only boundary points for purposes of the leading point count.

2. **Descent of every component.** The equality G^arith=G^geo makes the arithmetic action preserve each geometric orbit. Thus every component descends to F_q. Merely knowing that the original word cover is geometrically connected would not suffice, but Lemma 3.4 gives the stronger equality needed. Its boundary argument is applicable to the compositum, not just an individual cover: constants inject into the residue splitting field of the generic polynomial, whose constants are F_q. I found no new defect here.

3. **Words versus parameters.** For fixed f, t=(f+u+v)/(uv) is unique. Thus distinct words give distinct ordered (u,v) even without a≠b. The role of a≠b is the stronger assertion that they give distinct *unordered* classes. If the unordered pairs agree, a swap cannot remain in that fixed asymmetric shape. This distinction should be stated explicitly, especially given the E₂ error.

4. **Main term.** Pairwise coprimeness of the k moduli is a nonempty open condition on the kd-dimensional parameter space. It has q^(kd)+O(q^(kd−1)) rational points. For every such tuple, CRT gives exactly q^(n−kd) monic f. The numerator f+u_i+v_i still has degree n and leading coefficient 1, so the resulting t_i are monic of the required degree. Thus the count really is q^n+O(q^(n−1)).

5. **Bad tuples.** With the corrected class-based event, each f has at most B(n)^k tuples, and each bad tuple forces E₂. Therefore the bound B(n)^k·#{f:E₂} is correct and is O_n,k(q^(n−1)). The inequality with the *literal* word-based E₂ is also an upper bound, but the asserted estimate for that event is false; this is why the repair in §1.2 matters.

6. **Lang–Weil.** If there are r geometric components, all defined over F_q, their point count is r q^n+O(q^(n−1/2)). Comparing with the independent CRT count as q=p^r′ tends to infinity forces r=1. There is no need to improve Lang–Weil's error to O(q^(n−1)), nor to use different primes in this limiting argument.

7. **Small odd p.** The overlap count is characteristic-free; finite flatness and generic étaleness were proved without a large-characteristic assumption. Neither this argument nor the abstract permutation-group step requires p∤D_σ or tame ramification. Passing to extension fields of each fixed odd p is enough. I found no exclusion of p=3 or of primes dividing n!.

**Two MINOR proof cleanups:** For k=1, omit the bad-pair paragraph: kd≤n does not imply 2d≤n, but there are no bad pairs to count. For the mixed-shape assertion, d_σ+d_τ≤n need not imply 2 max(d_σ,d_τ)≤n. Apply C2's fixed-degree pair sum directly: every relevant lcm has degree at most d_σ+d_τ≤n. Do not invoke the global 2D≤n corollary with D=max(d_σ,d_τ) without that clarification.

## 3. Theorem 3.9

### 3.1 CFSG step — SOUND

The classification used is correct: apart from the symmetric and alternating natural actions, the finite 4-transitive groups are M₁₁, M₁₂, M₂₃, M₂₄ in their indicated degrees. Thus degree >24 rules out all exceptions. The lower bound D_σ≥n(n−1)>24 is more than sufficient for n≥12 and the selected shapes.

**Citation repair:** supply an actual reference, e.g. Dixon–Mortimer, *Permutation Groups*, GTM 163 (1996), p. 218; alternatively Cameron, *Permutation Groups* (1999), p. 110. The Dixon–Mortimer statement is quoted in the reference discussion at <https://mathoverflow.net/a/136016>, which I visited; Cameron independently states the same classification consequence at <https://cameroncounts.wordpress.com/2014/11/27/three-versus-four/>. This is the classification of 4-transitive groups, not merely of *sharply* 4-transitive groups.

### 3.2 Goursat and the perfect core — SOUND

Each coordinate image is A_D or S_D, with D>24. In Goursat's lemma, if the common quotient is trivial or C₂, the pair projection contains A_D×A_E. If the quotient is nonabelian, the possible normal subgroups force both kernels to be trivial; the factors must have equal degree and the same type. There is no A_D≅S_E accident in these degrees.

Every isomorphism between the resulting natural permutation groups is induced by a bijection of their point sets: Aut(A_D)=S_D and Aut(S_D)=S_D here. The degree-6 exceptions are irrelevant. Its invariant graph contradicts the mixed transitivity in Proposition 3.8. Thus every pair projection contains the product of the two alternating groups.

Taking the terminal derived subgroup H=(G*)^(∞) is legitimate. Surjective images commute with every term of the derived series, and the perfect core of each pair projection is A_D×A_E: its quotient by that product is abelian, while the product is perfect. Hence H has all the claimed pair projections and lies inside the product of alternating groups.

The pair-surjective-product lemma is also correct. One short independent proof is induction with Goursat: if a subdirect subgroup of (∏_{i<m} A_i)×A_m were proper, the simple quotient A_m would have to be identified with one simple coordinate of the first product, contradicting pairwise surjectivity. The m=1 case follows from the single projection. Equivalently, one can use iterated commutators and perfectness. The cited Ribet/Serre lemma is corroborated by Lemma 14 and its proof at <https://terrytao.wordpress.com/2021/05/07/goursat-and-furstenberg-weiss-type-lemmas/>. Give the full reference: Ribet, “On ℓ-adic representations attached to modular forms”, *Invent. Math.* 28 (1975), 245–275, Lemma 3.3.

**Important limitation:** this proves ∏A_D⊆G*, not G*=∏G_c. Arbitrary sign relations can remain. The theorem's proof handles them correctly by conditioning on a coset; the surrounding prose does not (see §5).

### 3.3 Derangements — SOUND

The signed derangement count is

    #even derangements − #odd derangements = (−1)^(D−1)(D−1).

Thus the two counts are (d_D±(D−1))/2, with the sign assigned according to D. Dividing by the coset size D!/2 gives the upper bound

    (d_D+D−1)/D! ≤ (d_D+D)/D! < 0.38,  D≥6.

For example the latter bound at D=6 is 271/720≈0.376389; the alternating-series estimate d_D/D!≤1/e+1/(D+1)! makes the uniform inequality immediate for larger D. There is no missing factor 2.

A coset of N=∏A_D is a Cartesian product of coordinate cosets, with uniform independent coordinates. The pushforward of uniform measure on G_{n,p} to G* is uniform. Consequently the uniform coset bound gives ρ≤0.38^|𝒞*| even with arbitrary correlations of signs. This part of the argument does not assume the full independence that the prose incorrectly claims.

### 3.4 Class counts and exponents — correct, with a MINOR all-n proof gap

There is a simple exact formula. Put

    m=⌊n/4⌋,    F(m)=⌊(m−1)²/4⌋.

Then

    |𝒞*_n| = F(m)                         if n is odd,
    |𝒞*_n| = F(m)−F(⌊m/2⌋)              if n is even.

Indeed F(m) counts 1≤a<b with a+b≤m; in the even case the excluded even-even pairs are obtained by halving both coordinates. This proves the stated asymptotic constants 1/64 and 3/256, with an O(n) count error.

Independent direct enumeration through n=1200 agrees with the formula, and gives

    min_{12≤n≤1200} |𝒞*_n|/n² = 1/225,       attained at n=15;
    min_{100≤n≤1200} |𝒞*_n|/n² = 30/2809,    attained at n=106.

Multiplying by −log(0.38) gives respectively

    0.004300373450… > 0.0043,
    0.010333756065… > 0.0103.

The script additionally checks these minima through n=1,000,000, but that is not a proof for all n. The manuscript currently jumps from a finite check and an unquantified asymptotic to “for n≥12.” That implication needs completion.

**Exact repair for all n:** for m≥3,

    F(m)≥m²/4−m/2,    F(⌊m/2⌋)≤m²/16,

so for either parity and n≥12,

    |𝒞*_n| ≥ 3m²/16−m/2 ≥ 3n²/256−7n/32.

For n≥1200, division by n² gives at least 0.0115364583…, which exceeds both 1/225 and 0.0103/(−log 0.38). Combine this with the finite checks. This proves the advertised 0.0043 bound for **all n≥12**, and even upgrades the stated 0.0103 bound to **all n≥100**.

The actual asymptotic coefficients supplied by the 0.38 estimate are

    (−log 0.38)·3/256 = 0.011338875308…   (even n),
    (−log 0.38)/64    = 0.015118500410…   (odd n).

Thus 0.0103 is a conservative uniform coefficient, not an asymptotic equality or a numerical fit to ρ.

**Minor scope notation:** ρ_{n,p} was initially defined in Theorem 3.3 only for p≡3 (mod 4), whereas Theorem 3.9 quantifies over every odd p. Extend its definition explicitly to the same formal set of U-shapes in all odd characteristics, or restrict the density notation to p≡3 (mod 4). The group statements themselves work for every odd p. Summary row 7′ should say “every odd characteristic,” not unqualified “every characteristic.”

## 4. Moment computation (§3.9, lines 510–515)

**Verdict: SOUND numerical computation; MINOR overinterpretation.** I inspected the enumerator and reran all five listed primes. It forms u(tv−1)−v and exhausts the monic triples. Its base-p incremental updates, including carries, are correct. For the requested n=5, D_σ=30, so uint16_t counts cannot overflow; at q=31 the array is about 57.3 MB. The factorial-moment sums in these runs are small enough for exact integer accumulation in double before division. The two compiler warnings concern misleading indentation and unused argc, not a discrepancy in these runs. The executable is not a generally validated arbitrary-parameter tool, but that does not undermine these particular computations.

| q | P(W=0) | m₂ | m₄ | m₆ | m₈ |
|---:|---:|---:|---:|---:|---:|
| 7 | 0.33236 | 0.8638 | 0.5898 | 0 | 0 |
| 11 | 0.35237 | 0.9135 | 0.4623 | 0.0492 | 0 |
| 19 | 0.35779 | 0.9485 | 0.7497 | 0.3702 | 0 |
| 23 | 0.35939 | 0.9558 | 0.7725 | 0.5017 | 0 |
| 31 | 0.36106 | 0.9655 | 0.8160 | 0.5301 | 0.0873 |

At q=31 the full sequence is exactly the stated rounded sequence. Certification applies to these finite-field enumerations, **not** to high transitivity or a limit inferred from them.

The proposed 1−binom(k,2)/q correction is an empirical first-order fit at q=31, not a consequence of k-transitivity. Transitivity controls the leading limiting moment; general Chebotarev/Lang–Weil supplies an O(q^(−1/2)) error, not that particular coefficient or even automatically O(1/q). The small-q high moments are not uniformly well described by this fit: at q=7, k=4, the formula predicts 0.1429 against 0.5898; for k=8 and q≤23 it predicts a negative number. Those cases are outside a credible first-order regime.

Furthermore these are different primes, not an extension-field sequence at fixed characteristic, and n=5 lies outside Theorem 3.9. They cannot establish that theorem or certify monodromy at n=5. Eight moments also do not identify a group.

**Exact wording repair:**

> The listed moments are CERTIFIED finite-field computations. At q=31 they are consistent with a heuristic 1−binom(k,2)/q correction to limiting factorial moments 1, but the high moments have large finite-q defects. High transitivity for this n=5 shape, the correction coefficient, and convergence to the S₃₀ derangement probability are EVIDENCE/CONJECTURE, not consequences of Theorem 3.9.

Replace “→1/e for S₃₀” by “the S₃₀ prediction is d₃₀/30!≈1/e”; n=5 fixes D=30, so even under that group hypothesis the exact limit is not 1/e.

## 5. Overclaiming and transfer (§0 rows 7′–8; §3.9 closing paragraph; §5.2)

**Verdict: MAJOR.** These are not objections to the repaired upper-bound theorem, but they change what that theorem says.

### 5.1 No Θ(n²) conclusion

“exp(−Θ(n²)) from above” is nonstandard and invites a false two-sided reading. “The true exp(−Θ(n²))” in row 8 is plainly not proved. A positive constant ρ_{n,p} at each fixed n supplies no lower bound exp(−Cn²) as n grows. The paragraph admits this, but its headline contradicts the admission.

**Repair everywhere:** write “ρ_{n,p}≤exp(−c n²)” or “an exp(−Ω(n²)) upper bound.” Reserve exp(−Θ(n²)) for the conjecture. Theorem 3.9 establishes an upper-bound consequence of Conjecture 3.6, not its asymptotic rate or leading constant.

### 5.2 Not exact four-wise independence, and not full independence

The proof establishes limiting factorial-moment identities for distinct *words within a shape* and a mixed first moment for two shapes. CRT is exact for each compatible tuple whose lcm degree is ≤n; the aggregate counts still have O(1/q) overlap and boundary corrections. This is not an assertion that the shape-existence indicators are exactly four-wise independent.

Nor does ∏A_D⊆G* give unconditional independence across shapes. For a concrete abstract obstruction, consider

    H={(g,h)∈S_D×S_D : sign(g)=sign(h)},  D>24.

It contains A_D×A_D, has all the coordinate and pair-action transitivity used here, and satisfies the theorem's group conclusion. Yet its two derangement indicators have covariance

    ((D−1)/D!)² > 0,

because their conditional probabilities differ between the common even and odd cosets. Thus “upgraded to full independence” is not a consequence of the proved structure. The same issue applies to unequal degrees, with the product of the corresponding signed biases.

**Exact replacement for the mechanism:**

> Low-order CRT counts, after removing an O(1/q) exceptional overlap contribution, prove high transitivity of the word covers. CFSG and mixed transitivity force their joint monodromy to contain a product of alternating groups. This gives independent coordinates conditional on the remaining sign-coset data, and a uniform derangement bound in every such coset. That is sufficient for the exp(−c n²) upper bound; unconditional independence is not asserted.

### 5.3 The integer analogy is not an exact theorem

For integers in [1,N], CRT gives a count N/M+O(1) in a compatible residue class modulo M, not exact uniformity. If four pairwise coprime moduli have product comparable to N, that O(1) can be comparable to the main term. Moduli individually ≤N^(1/4) also need not be pairwise coprime. Neither point is a technicality when summing over large families of words.

More importantly, the function-field argument identifies factorial moments with orbit counts of finite covers of coefficient space. Calling its integer analogue “just CRT and true” skips precisely that geometric identification and conflates fixed residue classes with the shape-existence union.

The absolute statement that nonabelian monodromy “has no integer counterpart” is also too broad: nonabelian Galois groups, covers over number fields, and Chebotarev certainly have number-field counterparts. What is missing here is an established analogue of **this coefficient-space family and its word-count/orbit correspondence**, with estimates for integer targets at the required scale. The document has not proved that no alternative construction can exist.

**Repair:** say that no such integer counterpart or transfer theorem is supplied/known in this framework. State the CRT interval error and distinguish individual congruence classes from word-shape unions. “GRH is not the missing input over ℤ” should remain an explicitly methodological assessment, not a logical consequence of the function-field example.

### 5.4 What “depth barrier broken” can legitimately mean

The improvement is real in the **iterated large-q model**: first fix n and p, take q=p^r to infinity, then compare the resulting densities as n varies. It proves no corresponding decay in the fixed-q regime and no uniform bound of that strength in N=q^n as n grows. The O_n(q^(−1/2)) term is not controlled relative to exp(−c n²) in such a regime.

Keep the qualification in the headline itself: “A quadratic-in-n exponent upper bound for the limiting large-q densities.” Do not suggest that the fixed-q/integer depth barrier from §3.7 has been resolved. Row 7′'s “≈exp(−0.0103 n²)” should be an upper-bound inequality, after adding the all-n counting repair in §3.4 of this report.

## 6. Reproduction and final disposition

All executions were under `ulimit -v 8000000` and explicit timeouts. The independent check streams pairs of polynomial-product buckets, not a dense Cartesian-product array; its largest overlap run has 1,090 classes. The million-degree constant scan keeps scalar state.

Representative commands:

```sh
ulimit -v 8000000
timeout 120s uv run --no-project scripts/z51_ffield_c2check.py 3 3 7 11
timeout 30s uv run --no-project scripts/z51_ffield_c2check.py 2 3 7 11
timeout 180s uv run --no-project reviews/z51_ffield_r3_check.py
timeout 30s gcc -O2 -Wall -Wextra -o /tmp/r3mom scripts/z51_ffield_moments.c
timeout 120s /tmp/r3mom 31 5 2 1 2
```

**Disposition:** retain C2, Proposition 3.8, and the substantive claims of Theorem 3.9 after correcting E₂ and completing the elementary constant argument. Do not retain the literal word-based E₂ estimate, unconditional/full-independence language, Θ(n²) claim, or exact integer-transfer claim. The repaired result is a genuine large-q upper-bound theorem, not a proof of the full Poisson conjecture or an integer/fixed-q depth breakthrough.
