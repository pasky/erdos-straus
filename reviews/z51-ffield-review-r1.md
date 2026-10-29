# Hostile referee report: EXSET_FUNCTION_FIELD, §§0–3

## Overall finding

**MAJOR revision required.** The core reciprocity obstruction, finite-flatness argument, boundary specialization, and fixed-degree positive-density lower bound survive scrutiny. I did not find a fatal counterexample to those theorems. Several surrounding assertions are false or stronger than the arguments: the claimed non-nesting of the two unions, the unrestricted large-q limit, occurrence of every Frobenius class for every q, the extension to *every* union of shapes, and parts of the numerical/depth commentary.

The independent divisor/shift enumeration agrees with the C engine on all monic polynomials over F₃ and F₇ of degrees 2–5. This verifies those finite computations, not the asymptotic interpretations.

**Scope and provenance.** I initially read the 320-line version ending in placeholders for §§4–6. The checkout was updated concurrently: during review HEAD became `8f585018e0e2b1834d8771a637bdaf5fe38640d4`, with additional material including Corollary 3.5′ and §3.8. The ten requested items below concern the original §§0–3.7; a separate addendum addresses the late additions. I changed no existing file and made no commit. The only repository files I created are this report and the explicitly requested `reviews/z51_ffield_r1_brute.py`.

## 1. Lemma 1.1 — SOUND

Write d = deg A and b = deg v. The assumptions imply gcd(A,v)=1, including v=1. Reciprocity gives

    (−v/A) = ε^d (v/A)
            = ε^(d+db) (A/v)
            = ε^(d+db+b).

This equals the displayed exponent `(d+1)(b+1)−1`. Modulo 2, d+db+b is zero precisely when d and b are both even. Since A+1 is nonzero, divisibility by v implies d≥b and t=(A+1)/v is monic of degree d−b. Thus the parity reformulation using deg t is also correct. Repeated prime factors of A cause no problem for the Jacobi symbol.

**Repair:** none. Retain the explicit convention that the Jacobi symbol with denominator 1 is 1.

## 2. Definition 1.2 and Theorem 1.3 — MINOR

**The definition's equivalence and the square obstruction are sound.** For a word, the parity condition excludes s=b=0. With a≥1, one has

    deg A=s+b=n−a ∈ [1,n−1],   deg v=b<n,
    deg(f+v)=n,                A=tv−1.

Conversely, the degree bound on A in Definition 1.2 forces deg v≤deg A<n; hence f+v is monic of degree n, and both t and u constructed there are monic, with deg u=n−deg A≥1. This also excludes both degenerate shapes. The only degree-n shape with just one nonempty block that survives the word-map conditions is (n,0,0), which is not a U-shape.

For f=g², every prime P dividing A is coprime to v and therefore to g. Thus −v is a nonzero square modulo P, and its Jacobi symbol modulo A is +1, even when A is not squarefree. This contradicts item 1.

**Actual defect:** the *earlier*, unrestricted converse immediately after (1.1) is false without a degree condition. For any monic f of degree n, take

    v=f+2,  A=f+1.

Then A is monic, A divides f+v=2(f+1), and A≡−1 mod v. But the alleged word has t=1 and u=2, which is not monic in odd characteristic. Definition 1.2 itself avoids this counterexample.

**Exact repair:** add `deg v<n` to that earlier converse, or impose `1≤deg A<n` there as in Definition 1.2.

## 3. Proposition 1.7(ii), leading coefficients free — SOUND

For v=cw with w monic, the actual reciprocity calculation is

    (−v/A)=χ(−c)^d ε^(b(d+1)),

as stated. Monic nonsquare f cannot be a nonsquare constant times a polynomial square: its leading coefficient would force that constant to be a square. The character-sum bound and the estimate for the number of nonresidue values are valid, also for nonsquare f with repeated factors. If q>(n+1)², the displayed lower bound is strictly positive. Taking A=T−y and the nonzero constant v=−f(y) gives all the required divisibility, colour, and proper-degree conditions.

**Repair/qualification:** the threshold is sufficient, not necessary. Do not rewrite the proposition as “exactly when q>(n+1)².” For example, already at q=3,n=2 the monic U exceptional set consists exactly of the squares, so the larger U′ has the same exceptional set although 3<9. State explicitly that U′ retains the proper-divisor degree bounds from Definition 1.2.

Proposition 1.7(i) is sound if “analogue” means the union defined by the forced negative Jacobi colour, rather than mechanically retaining the parity definition at q≡1 mod 4.

## 4. Proposition 3.1 — SOUND

Every admissible shape has exactly q^n parameter triples, all mapping to monic degree-n polynomials. Multiple triples giving the same f are exactly what W counts. Therefore the mean is precisely the number of shapes, without any independence assumption.

An exact formula, useful for eliminating ambiguity in the asymptotic counting argument, is

    k = floor((n−1)/2),
    m(n) = n(n+1)/2 − (k+1)(k+2)/2.

The subtracted pairs are exactly the pairs (s,b) with both entries even, including (0,0). This gives 3n²/8+O(n) and all the displayed small values.

**Repair:** none; optionally replace the informal parity-density count by this formula.

## 5. Lemma 3.2 — SOUND, with a wording correction

The weighted argument works in every characteristic; it does not require any factorial to be invertible.

For the coefficient y_i, a contribution from u has source weight `i−(s+b)` when it exists, and a contribution from v has source weight `i−(s+a)`. Both are strictly less than i. At the leading coefficient of u the source weight is **0**: it occurs in target position i=s+b. The parenthesis saying that the leading 1 “sits at weight n−a” confuses target index with source weight; the preceding inequality is the correct one.

The top map h has zero fibre only at the origin over an algebraic closure. Its n homogeneous coordinates are a homogeneous system of parameters in the polynomial ring. Cohen–Macaulayness gives a regular sequence, and a homogeneous vector-space basis modulo (h₁,…,h_n) lifts to a free k[h]-basis. The Hilbert-series rank is the asserted integer n!/(s!a!b!).

The filtered lifting is legitimate, not an appeal to completion: h_i are algebraically independent, so a nonzero weighted polynomial in φ_i has the same nonzero leading term as the corresponding polynomial in h_i. This proves gr k[φ]=k[h]. To span k[x], subtract a basis expansion of the highest-weight term and induct downwards on the nonnegative integer weight. To prove independence, take the highest-weight part of a proposed relation and use independence over k[h]. The induction terminates.

The Jacobian has top weight

    Σ_i i − Σ_j wt(x_j) = sa+sb+ab.

Its top part is det Dh. At pairwise coprime t,u,v, reduction of the differential identity modulo each factor proves injectivity, hence invertibility, of Dh. Such points exist over the algebraic closure in every characteristic. Lower-weight terms cannot cancel this nonzero top part. The trivial shape (n,0,0), where φ(t)=t−2, also behaves correctly.

**Exact repair:** replace the misleading parenthesis by “the leading 1 of u contributes source weight 0 to target coefficient y_{s+b}.” The proof can be expanded by the filtered-basis argument above; no theorem downgrade is needed.

## 6. Theorem 3.3, Chebotarev and the alleged limit — MAJOR

**The displayed Chebotarev formula is sound, given the stated standard input.** Outside the union of the branch loci the maps are finite étale. A rational point of the fibre is exactly a Frobenius-fixed geometric point. This uses the finite étale cover's fibre functor, not an identification of the actual specialized coordinates with the generic coordinates. Normality causes no missing points here. The Galois closure is also étale on this open set.

The branch set has bounded complexity for fixed n, hence O_n(q^(n−1)) points. Uniformity in characteristic is defensible: use the bounded-degree equations for the original maps, construct an ordered splitting cover inside bounded fibre powers, and remove the diagonals/branch set. A connected component giving the Galois closure, and its twists, then have complexity bounded in n. Lang–Weil on those twists gives a constant independent of q, including small characteristic. **Degree of a field extension alone would not justify this conclusion; the bounded equations matter.**

The cited Fried–Jarden §6.4 / Proposition 6.4.8 is a curve/function-field source, not by itself an explicit verification of the higher-dimensional, complexity-uniform statement being used. I did not verify the claimed Serre §9 locator. A directly relevant, checked replacement is:

* J. C. Andrade, L. Bary-Soroker and Z. Rudnick, *Shifted convolution and the Titchmarsh divisor problem over F_q[t]*, Appendix A, especially Theorem A.4 and the twisting/Lang–Weil proof: <https://pmc.ncbi.nlm.nih.gov/articles/PMC4375376/>.

For comparison, the restriction to transcendence degree one in the Fried–Jarden-style approach is explicit in <https://arxiv.org/html/1404.6345v2>. Neither citation relieves the author of bounding the complexity of this particular joint cover.

**Major overclaim:** the formula does not establish a single limit as q→∞ through *all* allowed prime powers. The document itself allows G_n to depend on small p. Regularity removes dependence on extension degree within a fixed characteristic, not dependence on p.

**Exact repair:** define

    ρ_{n,p} = |Der_{n,p}|/|G_{n,p}|,
    δ_{p^r}(n) = ρ_{n,p} + O_n(p^(−r/2)).

For U, restrict to q≡3 mod 4. State the limit at fixed p along the permitted r, and the characteristic-zero stable limit when p>p₀(n). A universal prime-power limit requires a further proof that all the relevant ρ_{n,p} agree. Rename §3.3 accordingly. This is a missing conclusion, not a demonstrated counterexample to existence of that universal limit.

## 7. Lemma 3.4 — SOUND

The scaling identity checks exactly. With c=1/μ,

    (S_c t)(S_c u)(S_c v) = c^n(tuv)(T/c),
    c^n μ^(s+b)u(T/c) = c^a u(T/c),
    c^n μ^(s+a)v(T/c) = c^b v(T/c).

These are precisely the two subtracted terms on the left. The variable change y′_i=μ^(−i)y_i makes the generic family a purely transcendental base change of the original joint cover, so its group and algebraic constants are unchanged.

There is no wild-ramification loophole at μ=0. Work over the henselization of F_q(y)[μ]_(μ). The special generic polynomial is squarefree, and the finite flat family has an étale special fibre there. Thus the whole finite algebra is étale over that local base. Finite étale algebras remain finite étale under conjugation and compositum; the Galois closure is unramified at **all** places over this divisor. Merely finding one unramified place of an arbitrary non-Galois extension would not suffice, but this argument gives more.

The étale algebra/residue-field equivalence identifies the decomposition group's action with the action on all ordered factor partitions of the special polynomial. The residue splitting field is contained in the generic polynomial's splitting field, and the shape (0,n−1,1), together with its conjugates, supplies every root. Hence it is exactly that splitting field, with group S_n. Its constant field is F_q, since the generic splitting field is F_q(r₁,…,r_n) with algebraically independent roots. Constants of the original Galois closure inject into this residue field, proving regularity.

**Repair:** no change to the conclusion. Add the henselian finite-étale explanation to make the passage to the Galois closure and the equality of residue splitting fields explicit.

## 8. Theorem 3.5 — MAJOR in surrounding claims; displayed lower bound SOUND

An n-cycle has only ∅ and the whole root set as invariant subsets. It fixes no ordered partition with at least two nonempty blocks. This remains true when block sizes coincide: the blocks are ordered, so permuting them does not fix a point of the word-map fibre. Every allowed nontrivial shape has at least two nonempty blocks. Lemma 3.4 therefore supplies a simultaneous derangement.

The bound |G_n|≤∏D_σ! is valid, and the complexity argument in item 6 permits a uniform C_n for fixed n. Small characteristic does not invalidate the error-bearing lower bound. For sufficiently large q in terms of n, it indeed gives a positive proportion of nonsquares failing U.

There are nevertheless two false assertions in the prose:

1. **“Every class occurs for every q” is false.** G=G^geo says that no arithmetic constant-field coset excludes a class. It does not guarantee an F_q-rational base point realizing it. The Chebotarev lower bound can be negative for small q. The engine independently confirms q=3,n=9 has zero U-failures, so no simultaneous-derangement Frobenius class can occur there. This also refutes any reading of the theorem as a strictly positive fraction for every odd q without the error term.
2. **“Every union of word shapes” is false without an exclusion.** Every f has the word `(f+2,1,1)` of shape (n,0,0). A union containing this shape has no exceptional set whatsoever.

Also, the number of monic squares is q^(n/2) for even n and **zero** for odd n. Subtracting q^(n/2) as an upper bound is safe, but calling it the exact number for odd n is not.

**Exact repair:** say “every class is arithmetically permitted; each is realized for sufficiently large q depending on n”; replace “every union” by “every union excluding (n,0,0)”; replace “empty forest/no word” by “no nontrivial word”; give the correct parity-dependent square count. Preserve the theorem's error term when saying “every q.”

## 9. §3.6, cubic formulas, 29/144 and the Poisson conjecture — MAJOR in presentation

### Algebra and conditional number: SOUND

Substitution of t=T−x gives f(x)=−3x−c₂. Matching the other coefficients gives exactly

    α+β=−c₂−x,
    αβ=c₁+2+x(c₂+x),
    Δ(x)=−3x²−2c₂x+c₂²−4c₁−8.

The formula for W_(1,1,1) is correct when χ(0)=0 is stated and the sum is over distinct rational roots. It also works in characteristic 3. Independent exhaustive checks against all triples of linear monic t,u,v passed for q=3,7,11, giving U-failure counts 5,63,231.

The six-point wreath action has 29 derangements among its 48 elements. For the permutation of the three pairs, the contributions are: 1 flip pattern over the identity, 4 over each of three transpositions, and 8 over each of two 3-cycles; total 1+12+16=29. If the wreath group is full and is linearly disjoint from the S₃ splitting field of f+1, the product density is indeed 29/144.

**But those two hypotheses are not proved in this document.** The local conditional wording in §3.6 is fair; §2's unconditional “the limit is 29/144” is not. Nor does §3.3 compute that number.

### General model and labelling

The boundary-shape characterization is correct: U-failure implies that f+1 has no proper odd-degree divisor. This is equivalent to irreducibility for odd n, and to having only even-degree irreducible factors for even n. The displayed p_f(n) are the large-q permutation probabilities, not exact probabilities at finite q.

The displayed M_g(n) values and their leading terms are correct; I independently recounted them. The u↔v quotient for a=b has mean approaching 1/2, with the diagonal negligible at large q. This does **not** prove that the quotient's distribution is Poisson or that different shapes are independent. The CONJECTURE label is appropriate; the heading “the limit densities match” is too categorical. In particular the n=7 reported observation is over three times the model value, and there is no effective comparison here that decides whether this is finite-q error or model error.

The o(1) in Conjecture 3.6 needs its limit variable. For fixed n the group-theoretic probability is rational and does not approach a Poisson value merely by sending q to infinity. The intended claim should concern n→∞, after passing to stable characteristic, separately on the two parities. A relative `(1+o(1))` statement is substantially stronger than just its logarithmic exp(−(c+o(1))n²) consequence. Numerical agreement for n≤7 is not a justification of that strength.

Finally, “pairwise distinct branch divisors ⇒ linear disjointness” needs stronger wording. Distinct divisors may share branch components. For example, over an algebraically closed characteristic-zero base field, K(√x,√y) and K(√x,√z), with K=k(x,y,z), have different branch divisors but share K(√x). Pairwise disjoint sets of codimension-one branch components for the **Galois closures**, together with purity and geometric simple connectivity of A^n, give the intended sufficient criterion.

**Exact repairs:**

* Make every occurrence of 29/144 explicitly conditional or conjectural until the full joint monodromy is proved.
* Rename §3.6 “A Poisson heuristic and finite-q comparisons.” Define the stable-characteristic density and write `as n→∞ through each parity` in Conjecture 3.6.
* Replace the branch-divisor criterion by the no-common-components condition above; do not equate a single zero-event asymptotic with a proof of full independence.
* Correct q=163,n=3 from 0.2004 to **0.200120…** (866671/4330747). Reruns confirm q=179: 0.200618; q=191: 0.200707; q=167: 0.201370.
* The n=2 entry “largest q run: 0.5 (exact)” is not an exact finite-q value. Exactly, total U-failure fraction is `(q−1)/(2q)` and nonsquare failure fraction is `(q−3)/(2q)` for q≡3 mod 4. Only the limit is 1/2. Relabel the entry “limit 1/2 (proved).”

## 10. §3.7, depth accounting — MAJOR

Parts (a) and (b) contain sound fixed-degree facts, with qualifications: (a) holds for sufficiently large q and a possibly reduced positive constant; (b)'s error conversion is correct. That error exponent is above the square-floor exponent for every n≥2, so the stated error estimate alone cannot resolve that floor in even degree. There is no square floor in odd degree.

Part (c) mixes assumptions, inequalities, and conclusions:

* `δ≥1/|G_n|` holds for the **limiting group density**, not necessarily for δ_q(n). The finite-q counterexample q=3,n=9 already demonstrates the distinction.
* A bound `E_n=poly(|G_n|)` does **not** mean `log E_n≍m`. The argument only gives `log|G_n|≥m+o(m)`, not an upper bound of order m. The group may be vastly larger. Separately assume `log E_n=O(m)` if that is the optimistic scenario intended.
* From `log q≳n²` one obtains `m=O((log N)^(2/3))`, not comparability for arbitrary q. Equality in order requires choosing q near the threshold. Similarly the n³ threshold yields `m=O(sqrt(log N))`; it is an optimized budget scenario, not an equality for every hybrid sequence.
* `log E_n≍Σ log D_σ≍n³` is another unproved complexity model. Typical interior fibre degrees are exponential in n, but not every D_σ is approximately 3^n; boundary shapes have much smaller degrees. The sum's n³ order is reasonable, but its asserted relation to E_n has not been established.

**Exact repair:** formulate the general condition first. If the main density is ρ_n=exp(−m_n) and the certified relative error bound is E_n q^(−1/2), then controlling that error relative to ρ_n is ensured by

    (1/2) log q − log E_n − m_n → +∞.

Under the *additional* model log E_n=O(n²), the least-q scale gives a potential saving of order (log N)^(2/3). Under log E_n≍n³ it gives a potential sqrt(log N) saving. For larger q these become upper bounds on what m_n supplies. Call these **conditional budget analogies**, not an established reappearance of the integer barrier or an impossibility theorem for all large-q methods. The exact optimal threshold may also be worse because p>p₀(n) has not been quantitatively controlled.

Part (d) is a proposed direction, not a demonstrated depth breaker. An error `exp(O(n))q^(n/2)` still needs its exponential coefficient controlled relative to q, and one also needs a useful bound on the main density in the actual characteristic/regime. The stable-characteristic conjecture alone supplies no fixed-small-q main-term estimate. Purity by itself does not suppress the higher cohomology causing the Lang–Weil error; the relevant cancellation/vanishing for the indicator's trace function must be stated as a separate hypothesis.

For a cost model 3^(nk) for k interior events, the inequality `3^(nk)≤q^(n/2)` gives `k≤log q/(2 log 3)`: this is a bound on the **total** such events, not k events per degree. Repair that phrasing as well.

## 11. Other claims in the requested sections

### 11.1 Lemma 1.6 and the claimed non-nesting — MAJOR

The Jacobi-symbol formula in Lemma 1.6 is correct under gcd(u,v)=1. The conclusion “they are no longer nested” is false.

Indeed, a bichromatic word requires

    s(a+b)+ab ≡ 1 mod 2.

If s is even, a and b are both odd, and the original word is a U-witness. If s is odd, at least one of a,b is odd and hence positive; the original word is a U-witness when a≥1, and swapping u,v gives one otherwise. The equation is symmetric in u,v. Consequently

    ES₅,q(f) ⇒ U_q(f).

A U-witness that is not itself bichromatic does not prove that the unions of f are non-nested; another word might be a witness. In fact the inclusion above is strict already for q=3,n=3: the C run gives 5 U-failures versus 18 ES₅-failures among 27 polynomials, consistent with that inclusion.

**Exact repair:** replace the non-nesting paragraph by the displayed implication and its parity proof. Say that U is not contained in ES₅, and that a given U-witness need not be bichromatic. The shape (0,2,1) has symbol +1 only when the coprimality condition holds; without it the symbol can be 0.

### 11.2 §2, extinction and square proximity — MAJOR

Finite data through n=15 do not show that the nonsquare exceptional set “dies out” as n→∞. They support that conjecture, not its assertion. The analogy with the finite integer search also does not establish an integer asymptotic theorem.

The stated square-defect computation is actually wrong. Direct expansion of the listed even-degree failures gives:

| n | degrees of f−g², with multiplicities |
|---|---|
| 6 | 1: 6; 2: 15 |
| 8 | 2: 6; 3: 15 |
| 10 | 3: 9; 4: 3 |
| 12 | **3: 7** |
| 14 | 6: 3 |

At n=12, degree 3 is n/2−3, not either of the two asserted possibilities. For example, the first stored failure is

    f=T¹²+2T⁸+T⁷+T⁴+2T³+T²+2T,
    g=T⁶+T²+2T,
    f−g²=T³+2T.

Moreover the n=7 failures do not have a Laurent-series square root at infinity in F₃((1/T)), since their degree is odd. The wording “all of them (n=6..14)” needs an even-degree restriction.

**Exact repair:** label extinction as a conjectural interpretation of the finite sample; replace the square-defect claim by the actual table and restrict it to even degrees. Define a quantitative meaning of “∞-adically close” before drawing a conclusion from these defects. Truncating the square root already gives deg(f−g²)≤n/2−1 for every monic even-degree f in odd characteristic; that inequality alone is not an exceptional feature.

### 11.3 Prime-family mass and normalization commentary — MINOR

The exact description of F(A), the duplicate residues v=1 and v=A+1, and the resulting w(A) formulas are sound. The large-q averaged divisor assertion needs an explicit joint-factorization theorem/citation for A and A+1. Specify that the limit in the sum through z is taken with z fixed first. A statement uniform for z growing with q does not follow from the individual fixed-degree limits. The fixed-q Titchmarsh sentence is explicitly an Assessment and should remain one unless a theorem with its constant and degree regime is supplied.

“Over ℤ ... positivity leaves no unit shift” is literally false: positivity leaves +1. It can belong to the indicated U shift family, for example when the integer input is 7 mod 8. **Repair:** say “positivity leaves only one unit, not a family carrying arbitrary square-class data.” The claim of uniqueness of the chosen normalization should be restricted to the normalizations actually compared, not all conceivable analogues.

## 12. Independent numerical audit

Every shell invocation used `ulimit -v 8000000` and timeout-wrapped executable commands. The C binary was compiled with

    timeout 30s gcc -O2 -o /tmp/rev_enum scripts/z51_ffield_enum.c

No repository output file from the engine was overwritten.

### Requested sample runs

| q,n | U-shapes / mean W_U | squares failing | nonsquare failures | fraction |
|---|---:|---:|---:|---:|
| 7,4 | 7 / 7.000000 | 49/49 | 189 | 0.078717 |
| 11,3 | 3 / 3.000000 | 0/0 | 231 | 0.173554 |
| 3,8 | 26 / 26.000000 | 81/81 | 21 | 0.003201 |

These agree with Table 2.1's respective entries .0787, .174 and 21. The (3,8) summary and histogram agree with `data/z51_ffield/enum.txt`. That file does **not** contain the (7,4) or (11,3) runs, so those comparisons are to the table, not to a nonexistent raw record. Several other tabulated small-degree runs are likewise absent from that particular raw file; complete the provenance before treating the entire table as reproducibly archived there.

### Independent Python algorithm

`reviews/z51_ffield_r1_brute.py` does not enumerate t,u,v or invert the word map. It constructs the complete proper-monic-divisor table by multiplying each monic A of degree 1..n−1 by every monic complementary factor. For every monic f and every monic v of degree <n, it looks up the actual divisors of f+v and directly tests

    A+1 ≡ 0 mod v,   1≤deg A<n,   deg A or deg v odd.

The full-scan option visits every shift, even after a witness is found. Only O(nq^n) small polynomial tuples are stored. I ran both early-exit and full-scan modes; both agree with the C engine:

| q | n | all failures | square failures | nonsquare failures |
|---|---:|---:|---:|---:|
| 3 | 2 | 3 | 3 | 0 |
| 3 | 3 | 5 | 0 | 5 |
| 3 | 4 | 15 | 9 | 6 |
| 3 | 5 | 6 | 0 | 6 |
| 7 | 2 | 21 | 7 | 14 |
| 7 | 3 | 63 | 0 | 63 |
| 7 | 4 | 238 | 49 | 189 |
| 7 | 5 | 301 | 0 | 301 |

Reproduction:

    ulimit -v 8000000
    timeout 150s uv run --no-project reviews/z51_ffield_r1_brute.py \
        --engine /tmp/rev_enum --full-scan

The largest full-scan case visits 47,076,407 (f,v) pairs and completed in approximately 40 seconds here. The cubic formulas, wreath derangement count, shape means, square-defect table, and additional C runs reported above were checked separately under the same memory/time discipline. This audit does not independently certify every larger-n row in the archive.

## 13. Addendum on material added concurrently

These additions were not in the initially supplied 320-line text. The following is supplementary, not a claim that the new §4 has been audited.

### Corollary 3.5′ — MINOR

The intended irreducible-polynomial extension of the boundary argument works: adjoin the splitting field of the target polynomial, whose boundary specialization has the same generic S_n root action, then apply Chebotarev to the simultaneous n-cycle class. Regularity follows by the same residue-field argument; constants and complexity bounds are still bounded in n.

**Exact repairs:** the roots of `y′=S_{1/μ}^{(n)}y` are **μ⁻¹ times** the roots of y, not μ times them. “Have no word” must mean “have no nontrivial word.” Interpret the positive proportion for sufficiently large q, with a Chebotarev error or an explicit threshold. These changes preserve the substantive prime-polynomial conclusion.

### New Proposition 3.7 / §3.8 — MAJOR proof-completeness concern

The displayed Bonferroni inequality in (a) is correct: the even truncation bounds the actual avoidance probability, and the independent-model remainder is at most e_(2L+1), itself at most μ^(2L+1)/(2L+1)!. The proposed low-degree-divisor/prime-progression route to a uniform linear lower bound on μ is plausible and has the right budget. However, the final optimization needs an upper bound on the mass used, not just a lower bound. A direct repair is to select a subfamily of forbidden classes with total mass Θ(z), using the lower bound and trimming; then use that subfamily's mass in the factorial remainder. Alternatively prove a uniform μ(z)=O(z) with a suitable prime-progression upper bound. Handle k₀<0 and the bounded small degrees explicitly.

Part (b)'s key assertion is a factorial-moment limit for **all** j≤n/D. A pairwise overlap sketch is not yet that proof. In an overlapping tuple, the intersection probability has the factor q^(−deg lcm), not the product of the single-event probabilities. Compatibility costs and losses of independent constraints must be counted together over whole overlap configurations. An unweighted pairwise collision bound does not establish that their weighted contribution to every required j-th Bonferroni sum is o(1). Also, the elementary symmetric sum includes noncoprime pairs, so saying the coprime tuples contribute exactly e_j requires an error qualification.

**Exact repair:** supply a cluster/overlap-counting lemma showing that, for each fixed D,j in the required degree range, the total contribution of compatible noncoprime j-tuples to S_j(q) is O_(D,j)(q⁻¹), or another explicit o(1), with all shared-factor patterns covered. Then show that the coprime contribution tends to μ_D^j/j!, before the Bonferroni optimization. Until that is supplied, mark the n^(2/3) conclusion as conditional on this lemma rather than PROVED. This is a proof gap identified in the late addition, not a counterexample to its proposed asymptotic bound.

## Final verdict

**MAJOR.** Keep Lemmas 1.1, 1.6, 3.2 and 3.4, Theorem 1.3, Proposition 3.1, Proposition 1.7, and the error-bearing positive-density statement of Theorem 3.5, with the local repairs specified above. The central obstruction and boundary-monodromy mechanism are credible. Do not retain as established facts the non-nesting claim, an unrestricted prime-power limit, 29/144 without its joint-monodromy hypotheses, fixed-q extinction, the incorrect square-defect statement, or a universal depth-barrier conclusion from the hypothetical cost models. The finite numerical audit passes; the manuscript's claims discipline does not yet pass.
