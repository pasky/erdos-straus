# Hostile referee report: EXSET_CHAR_FORCING (Astra, round 3)

Scope: the post-round-2 material specified in the request, principally §5, Proposition 6.3′, Corollary 6.4, and the resulting claims in §§0 and 9. Reviewed snapshot: `8f354562`. I do not reopen the old window arguments. ES is OPEN.

## Overall verdict: MAJOR revisions, but the cap theorems survive

**The substantive positive result survives:** Corollary 5.5(a) gives the stated power saving at every cap exponent A > 1, and 5.5(b) gives the stated near-power saving at logarithmic caps. “T2-lite reached” is fair under the express definition in the z51 CONTEXT. These are transfers of established quadratic-character technology, not a new least-nonresidue theorem, an ES exceptional-set bound, or a solution of ES.

**The required revisions are chiefly a missing all-level argument and overstatement of scope.** Proposition 6.3′ needs a genuine treatment of large Q = q^k; its present “same argument” does not verify Shiu's range. I give a repair below, establishing the claimed theorem and hence MR(A) false for A > 3. Section 9 again turns an average bound into a maximum-reach cutoff. Finally, MF₁/MR₁ are valid sufficient conditions but do **not** presently meet CONTEXT's qualification for a counted conditional target: they are nonstandard, MF₁ has no nonvacuous numerical test, and neither is shown to be visibly weaker than the desired exceptional-set conclusion.

The requested independent MR₁ computation passes. There is no FATAL mathematical finding in this round.

## 1. Verdict register

| Claim | Verdict | Finding |
|---|---|---|
| Proposition 5.1′: Heath-Brown moment argument and exponent 1/A | SOUND | This is the R2 derivation, with the correct square-correlation energy, not an erroneous squarefree-coefficient assumption. |
| Proposition 5.2: quoted Lau–Wu Lemma 1 and its range | SOUND | The displayed inequality, absolute implied constant, 2 ≤ P ≤ Q, and integer j ≥ 1 agree with the supplied primary PDF. There is no additional short-moment restriction. |
| Proposition 5.2: prime discriminants and subset restriction | SOUND | Positive prime discriminants p ≡ 1 (4) are included. The subset argument is legitimate by rerunning the nonnegative coefficient bounds, not by pointwise comparison of character sums. |
| Proposition 5.2: choice of j, two terms, explicit c₀ | SOUND-WITH-MINOR | The scales and exponents are right. Fix η and specify its range; give slack in the first exponential constant and explicit constants sufficient to absorb the second term. The exact endpoint c₁ = c₀ is not justified by the stated asymptotic calculation. |
| Theorem 5.3(a) | SOUND | Correct partition, with the small primes absorbed. |
| Theorem 5.3(b) | SOUND-WITH-MINOR | Correct bound. For “any set of primes,” extend the character identification to d = (−1)^((p−1)/2)p; Proposition 5.2 is currently stated only for p ≡ 1 (4). |
| Theorem 5.3: additional removal for forced windows | SOUND-WITH-MINOR | The R2 repair is present. Restrict the window conclusion to p ≡ 1 (4), and use a subset bias threshold strictly below 1 in part (b), independently of a possibly unit η. |
| Corollary 5.4(a)–(c) | SOUND-WITH-MINOR | MF/MF₁ implications and MR/MR₁ pigeonhole arguments work. The genuine dyadic proof is now present; spell out the two moving endpoints in (b). |
| Status paragraph: GRH and necessity | SOUND | The A > 2 equivalence under GRH is correctly restored. No GRH equivalence is established at A ≤ 2 or at C log p. Sufficient is no longer confused with necessary. |
| Status paragraph: numerical MR₁ claims | SOUND | Independently reproduced from all 36 raw files; details below. Positive results are certified lower bounds for full defined reach, not estimates of the omitted search tail. |
| Status paragraph: coupon-model summability | SOUND-WITH-MINOR | Correct consequence of the extrapolated model, but not a proved probability estimate or empirically validated extreme-tail law. |
| Corollary 5.5(a) | SOUND | Squarefree products, Heath-Brown, and the cap containment give X^(1/A+o(1)) for every A > 1. |
| Corollary 5.5(b) | SOUND-WITH-MINOR | Correct transfer, including the C/2 cap. Supply explicit small constants for the density-1/2 subset instead of asserting that an unspecified c₂ is less than 1. |
| Corollary 5.5 novelty / “T2-lite reached” | SOUND-WITH-MINOR | Meets the written campaign target, but the A > 1 qualitative improvement was already sketched locally and the analytic technology is old. The architecture-specific question in CAP_INTERPOLATION Remark 3.2(c) is not automatically settled. |
| Proposition 6.3, repaired bookkeeping | SOUND | The R2 harmonic-sum, small-range, and +1 repairs are present and sufficient. |
| Proposition 6.3′: level-one V(T), BT, reciprocal-log sum | SOUND-WITH-MINOR | Valid after explaining coprimality before BT, enlargement of a truncated progression interval, and the corrected small-product height. |
| Proposition 6.3′: all levels and Haar summation | MAJOR | The written large-Q argument does not check Shiu's range, and the weighted error drops a factor log L. Both are repairable; a complete split is supplied below. |
| Corollary 6.4(a),(b) | SOUND-WITH-MINOR | Both conclusions follow from the repaired proposition. “Fixed q” means a prescribed q(X) in the uniform range, not a constant prime exceeding a growing threshold. |
| §0/§9: “only up to q ≈ (log p)^3” | MAJOR | An average/Markov theorem is not a pointwise maximum-q theorem. Average counts must also retain the proved range q ≤ (log X)^C. |
| §0: “T2-cond” as a campaign achievement | MAJOR | Valid reduction on new conjectural sufficient inputs; not an accepted conditional target under the stated hypothesis-quality requirement. |
| §9: remainder with forced windows | SOUND-WITH-MINOR | Retain the second exceptional-set removal explicitly; a residue box's number of distinct elements cannot exceed its group order. |

## 2. Heath-Brown: Proposition 5.1′ and Corollary 5.5(a)

### 2.1 The adopted R2 argument is the right one

With r = floor(log X/log y), N = y^r ≤ X, and ordered-tuple coefficients a_n, the arbitrary-coefficient quadratic large sieve uses

    E_sq = Σ_{n₁n₂ a square} a_{n₁}a_{n₂},

not merely Σ a_n². Each ordered 2r-tuple with square product admits a matching into equal-prime pairs. Thus

    E_sq ≤ (2r−1)!! m^r ≤ (2r)^r m^r.

The signal on a QR-biased character is at least (2ηm)^r. Consequently

    count(p > y) ≪ε X^(2ε) X (2r)^r / ((2η)^(2r)m^r),

which gives the displayed bound and exponent 1/A + 2ε + o(1). Taking every fixed ε > 0 gives exponent notation X^(1/A+o(1)); this does not mean substituting an X-dependent ε into a bound with an uncontrolled implied constant. This matches R2 §3.5.

For the asymptotic application, m = (1+o(1))y/log y is enough. The finite-range shortcut m ≥ y/log y for odd primes, inherited from Proposition 5.1, should not be regarded as universally valid merely because π(y) has that lower bound: one must subtract the prime 2. This does not affect the claimed asymptotic exponents. One can use the lower bound for sufficiently large y and handle bounded y trivially.

### 2.2 The squarefree cap application is even simpler

For p ≡ 1 (8), CAP_BOUNDED Lemma 3.1 gives

    e*(p) ≤ (q₃(p)−3)/4.

Therefore e*(p) > y/4 implies q₃(p) > y+3, hence χ_p(q) = 1 at every prime q ≡ 3 (4), q ≤ y. There is no vanishing generator: p ≡ 1 (8) cannot equal such a q. Primes outside p ≡ 1 (8) have e* = 0 and contribute nothing.

Let k = π(y;4,3) and take the squarefree products of r distinct generators, r = floor(log X/log y). For A > 1 and y = (log X)^A, k/r tends to infinity and

    |A_set| = binomial(k,r) ≥ (k/r)^r = X^(1−1/A−o(1)).

Every product is odd, squarefree, and at most X. In Heath-Brown's squarefree theorem, the energy is exactly |A_set|: two squarefree positive integers have square product only when equal. The signal is |A_set|, giving

    count ≪ε X^(1+2ε)/|A_set| = X^(1/A+2ε+o(1)).

This proves 5.5(a). The density-1/2 restriction on generators changes an O(r) logarithmic term, not the exponent. The bottom-line version with a p-dependent cap follows by the same genuine dyadic argument used elsewhere, not by directly replacing X by p in a counting statement.

## 3. Lau–Wu: primary-source check and the logarithmic scale

Source visited and read: [Lau–Wu, *On the least quadratic non-residue*, supplied HAL PDF](https://hal.science/hal-00097136v1/document), particularly the definitions on printed p. 2, Theorem 2 on p. 3, and Lemma 1 and its proof on p. 6. The PDF is the HAL v1 manuscript associated with IJNT 4 (2008), 423–435; I do not claim a separate collation of the journal typesetting.

### 3.1 Exact quotation and discriminant family

Lemma 1 states

    Σ_{d∈D(Q)} |Σ_{P<ℓ≤2P} χ_d(ℓ)/ℓ|^(2j)
       ≪ Q (6j/(P log P))^j + (6P/(log P)^2)^j,

uniformly for 2 ≤ P ≤ Q and integers j ≥ 1, with an absolute implied constant. This is the manuscript's quotation. In particular, j is not restricted by (2P)^j ≤ Q. The second term is the price that makes the unrestricted moment statement possible.

D(Q) consists of fundamental discriminants of either sign with |d| ≤ Q. For a prime p ≡ 1 (4), d = p is a fundamental discriminant and

    χ_d(ℓ) = (p/ℓ) = (ℓ/p)

for odd ℓ, including the zero case. More generally d = p* := (−1)^((p−1)/2)p represents the Legendre character for every odd prime p. This one-line extension repairs the mismatch between Proposition 5.2's stated p ≡ 1 (4) domain and Theorem 5.3(b)'s arbitrary prime set. It does not change Q or cost a factor in the conductor.

### 3.2 Restricting the prime set is legitimate, for the stated reason

It would be false to justify this by saying the absolute value of a restricted character sum is at most that of the full character sum. Cancellation forbids that comparison. The manuscript instead invokes the coefficient proof, which is valid.

For a fixed subset S, let a′_j(n) count ordered j-tuples from S∩(P,2P]. Then 0 ≤ a′_j ≤ a_j. Repeat Lau–Wu's application of the Montgomery–Vaughan inequality to a′_j(n)/n. The square-correlation contribution is bounded using the restricted concatenated 2j-tuples, and then by the unrestricted a_{2j}(n²). The other term is bounded by

    (Σ_{ℓ∈S∩(P,2P]} ℓ^(−1/2))^(2j)
      ≤ (Σ_{P<ℓ≤2P} ℓ^(−1/2))^(2j).

Thus the same two-term bound holds. This includes S = {q ≡ 3 (4)}. No character orthogonality specific to the complete prime interval has been discarded.

For the quantitative signal, state what “relative density δ” means: for example π_S(t) ~ δπ(t), so partial summation gives

    σ_S(P) := Σ_{ℓ∈S∩(P,2P]} 1/ℓ
             = (δ log 2 + o(1))/log P.

The required asymptotic holds unconditionally for the congruence subset in Corollary 5.5.

### 3.3 Choice of j and a safe explicit calculation

Fix 0 < η ≤ 1 and C > 0; put a = δ log 2. Dividing Lemma 1 by (ησ_S)^(2j) gives

    count ≪ X [6j log P/(η²a² P) · (1+o(1))]^j
              + [6P/(η²a²) · (1+o(1))]^j.

Taking j ≍ η²P/log P with a sufficiently small proportionality constant makes the first base less than 1, whereas the second has logarithm log P + O_η,δ(1). Hence the asserted shapes are correct:

    X exp(−c₁η² C log X/log log X),
    X^(c₂η² C(1+o(1))).

For a fully explicit version with slack, take

    κ = a²/(12e),       j = floor(κ η²P/log P).

The first base tends to 1/(2e). Since log(2e) > 1, for sufficiently large X it gives

    count ≪ X exp(−κ η² C log X/log log X)
              + X^(κ η² C(1+o(1))).

For all primes, κ = (log 2)²/(12e) ≈ 0.01473. For primes ≡ 3 (4), κ = (log 2)²/(48e) ≈ 0.003682. Thus for 0 < C ≤ 1 the second term is comfortably power-small and is absorbed by the first. This supplies the missing numerical justification in 5.5(b).

The manuscript's c₀ = (log 2)²/(6e) is the leading optimized constant from the quoted inequality. The calculation with σ = (log 2+o(1))/log P gives a first exponential coefficient c₀+o(1), not automatically a strict big-O bound with the exact endpoint coefficient c₀. An error o(j) in an exponent need not be O(1). State any fixed smaller coefficient, or prove a sharper estimate from the underlying coefficient argument. No application here needs the endpoint constant. Also specify that η is fixed; the displayed X-exponent calculation is not uniform in arbitrary η = η(X).

### 3.4 Corollary 5.5(b), constants and prior art

With P = C log X, e*(p) > (C/2) log X implies q₃(p) > 2P+3. Every q ≡ 3 (4) in (P,2P] therefore has χ_p(q) = 1. This is full bias η = 1 on that subset, and the preceding calculation proves exactly the claimed near-power bound. The factor C/2, the strict inequality, and the restriction p ≡ 1 (8) are all handled correctly.

Lau–Wu Theorem 2 already proves the same near-power exceptional-set shape for no nonresidue in (P,2P], for C₀ log Q ≤ P ≤ (log Q)² with a sufficiently large absolute C₀, over all fundamental discriminants. Its proof needs the large C₀ to control ramified primes. The present prime-character signal formulation avoids that issue and directly handles a fixed smaller C and a density-1/2 subset. This is a straightforward adaptation of Lemma 1, not a new analytic phenomenon.

The same paper explicitly attributes the A > 1 least-nonresidue improvement to Baier using Heath-Brown; its reference [2] is S. Baier, *A remark on the least n with χ(n) ≠ 1*, preprint. I checked that attribution in Lau–Wu, not a separate original copy of Baier's preprint. Credit the result as established technology; do not imply this campaign first discovered the least-nonresidue threshold.

CAP_INTERPOLATION Remark 3.2(b) already sketches a power saving for caps at least (log N)^(1+ε). Thus 5.5(a) supplies a clean complete proof and an explicit exponent by another route, rather than the first local suggestion of that qualitative threshold. Part (b) improves the known cap exceptional-set bound at logarithmic caps. However, Remark 3.2(c) asks about the ceiling for a specified full D_e(ℓ) family/prime-modulus sieve architecture. Reversing the sieve moduli and using quadratic-character moments does not, by itself, determine that original architecture's optimal sieve mass. Say “improves the cap exceptional-set bound in that numerical range,” not that every architecture-specific OPEN question there is resolved.

## 4. Robust reduction, dyadic repair, and hypothesis status

### 4.1 The implications are valid

For part (a), except for p ≤ y, having at most (1/2−η)m nonresidue generators is exactly QR bias at least 2ηm. The small primes are absorbed by the X^(1/A+o(1)) term. For part (b), after extending Proposition 5.2 to p* as above, the partition is immediate and its second moment term is absorbed for C ≤ 1.

The R2 correction of the forced-window statement is present: bias on all primes does not control the q ≡ 3 (4) subset, so remove its own small biased set. Make two domain conventions explicit:

* Actual windows x = (p+q)/4 with q ≡ 3 (4) require p ≡ 1 (4). The clause is not a statement about every odd prime in an arbitrary E.
* In the weighted version use, for example, subset QR-bias threshold 1/2. A threshold η = 1 only guarantees at least one nonresidue in the complement, not ≫ P/log P of them. An independent fixed threshold below 1 proves the desired conclusion even if the η in 5.3(b) equals 1.

For Corollary 5.4, work on p∈(Z,2Z]. At the power-log scale the differing primes are o(m), preserving any fixed bias after a fixed reduction in η. For P = C log p, both interval endpoints move by O(C): only O_C(1) integers, hence O_C(1) primes, can be affected. Their total reciprocal weight is O_C(1/log Z), whereas the full interval mass is ≍ 1/log log Z. The relative error tends to zero. Apply the sieve with outer parameter 2Z and sum dyadically; the constants may be decreased. This proves the stated bound without the old square-root splitting loss.

On an ES-exceptional prime, every reached q is a residue by Lemma 6.2. In the weighted case, reached weight at least (1+η)/2 of the total leaves character sum at least η times the total. The unweighted MR⇒MF calculation is the same pigeonhole argument; 2 is already a residue on p ≡ 1 (8). Specify a fixed admissible η, not an unquantified “MR₁(C,η)” for all η.

### 4.2 GRH statements are repaired

The corrected A > 2 conclusion agrees with R2: effective Chebotarev gives nonresidue density 1/2+o(1) uniformly at y = (log p)^A, so under GRH MF(A,η) is equivalent to eventual ES. At A ≤ 2 the cited error does not establish that density. Nor does it establish density in an interval of size C log p. “No such GRH equivalence is known here” is appropriate; failure of a particular error estimate is not a theorem of logical independence.

The necessity paragraph is also right: a small infinite set of unbiased ES exceptions is compatible with the desired exceptional-set upper bound and violates pointwise MF/MF₁.

### 4.3 Do these count as acceptable conditional targets? No, not yet

The binding z50 CONTEXT requires either a standard hypothesis or a clean, falsifiable, numerically tested hypothesis visibly weaker than the conclusion. Merely attaching a name to a sufficient condition is not enough.

* **MF₁:** precisely defined and sufficient, but nonstandard. It says that every sufficiently large prime in an overwhelmingly common unbiased character population satisfies ES. It rules out even sparse ES exceptions in that population, whereas the desired counting bound permits them. Every tested p already satisfies ES, so testing those p supplies no nonvacuous evidence for an implication whose antecedent is “ES fails.” There is no demonstrated visible weakening relative to the target exceptional-set statement.
* **MR₁:** a clean finite certificate condition at each p, with genuine numerical checks and a plausible heuristic. But it requires counterfactual coverage for every large prime, even those whose actual ES solution is already known. It is stronger than the sufficient MF₁ route and is not implied by an exceptional-set bound. No argument shows it is a visibly weaker assumption in the required campaign sense.

The lack of a known GRH equivalence for MF₁ does not establish that it is weaker than the desired conclusion. Conversely, neither condition should be dismissed as a formal tautology: MR₁ is a meaningful separate research conjecture, and the reduction identifies a useful scale.

**Required label:** “PROVED robust reduction; CONDITIONAL consequence of new, unproved sufficient hypotheses MF₁/MR₁; not a counted conditional target under CONTEXT.” Replace the achievement-style “T2-cond” bullet accordingly. The unconditional T2-lite result is unaffected.

## 5. Independent numerical audit of MR₁

I read the raw `data/z51_forcing/reach/*.txt` files directly, not `mr1_summary.txt` or the project's MR₁ implementation. There are 36 files, about 288 KiB total. The script streams one file at a time; it checks the header p and QMAX, uniqueness of q, nQNR = (q−1)/2, and completeness of the tiny prime interval by independent trial division. It uses column 4, `unreachedQNR`, and exact rational sums of 1/q.

The statistic is

    R_C(p) = [Σ_{C log p < q ≤ 2C log p, unreachedQNR(q)=0} 1/q]
             / [Σ_{C log p < q ≤ 2C log p} 1/q].

It is not the proportion of reached cells within partially reached moduli. A modulus contributes only if all its nonresidue cells are reached.

Execution used `ulimit -v 8000000; timeout 30s uv run --no-project /tmp/z51-r3-mr1-check.py` with a bounded tool timeout. All numerical assertions passed.

| p scale | files | min/max R_(1/2) | min R_1 | max R_1 | R_1 < 0.6 |
|---|---:|---|---:|---:|---:|
| 10⁵ | 8 | 1 / 1 | 0.253706681 | 0.772999285 | 6 |
| 10⁶ | 8 | 1 / 1 | 0.620330148 | 1 | 0 |
| 10⁷ | 8 | 1 / 1 | 0.803864129 | 1 | 0 |
| 10⁸ | 4 | 1 / 1 | 1 | 1 | 0 |
| 10⁹ | 4 | 1 / 1 | 1 | 1 | 0 |
| 10¹⁰ | 4 | 1 / 1 | 1 | 1 | 0 |

At C = 1 near 10⁵, the individual fractions are:

| p | R_1(p) | q in the interval not fully reached by the recorded search |
|---:|---:|---|
| 100049 | 0.331770275 | 17, 19, 23 |
| 101009 | 0.558770990 | 17, 23 |
| 102001 | 0.746293319 | 17 |
| 103001 | 0.253706681 | 13, 19, 23 |
| 104009 | 0.772999285 | 19 |
| 105097 | 0.585476956 | 19, 23 |
| 106033 | 0.585476956 | 19, 23 |
| 107033 | 0.558770990 | 17, 23 |

The minimum above 10⁶ occurs at p = 1020001, where q = 17 is the only missing modulus in the interval. Thus η = 0.2 is a valid fixed sample margin for MR₁(1,η) at all sampled p ≥ 10⁶. At C = 1/2 all 36 samples have fraction exactly 1, so every fixed 0 < η ≤ 1 works on that sample.

Be precise about “failures only near 10⁵”: six samples fail the **0.6 test in the recorded search**, but only two have recorded fraction below 1/2. Since the files are truncated lower bounds for Definition 6.1, a negative test is not necessarily a mathematical counterexample to full MR₁. Positive tests are valid lower-bound certifications, assuming the previously audited search/witness code; this round independently checks the aggregation, not every underlying tuple again.

The extrapolated coupon calculation is algebraically plausible: supply ≍ (log p)³ divided by q ≍ log p gives per-cell mean ≍ (log p)², and a polynomial-in-log-p union factor does not change exp(−c(log p)²). That expression is summable even over all integers. However, these measurements at small q and only 36 primes do not test an extreme tail uniformly over all large primes. Label the summability inference conditional on the coupon model, as the body largely does already.

For reproducibility, this is a short independent version of the check (no project analysis modules are imported):

```python
from pathlib import Path
from fractions import Fraction
from math import log
import re

root = Path('data/z51_forcing/reach')
results = []
for path in root.glob('*.txt'):
    with path.open() as f:
        header = next(f)
        p = int(re.search(r'\bp=(\d+)', header)[1])
        qmax = int(re.search(r'\bQMAX=(\d+)', header)[1])
        rows = {}
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            q, _, n, missing = map(int, line.split()[:4])
            assert q not in rows and n == (q-1)//2
            assert 0 <= missing <= n
            rows[q] = missing
    ratios = []
    for C in (0.5, 1):
        lo, hi = C*log(p), 2*C*log(p)
        assert hi < qmax
        primes = [q for q in range(3, int(hi)+1) if lo < q
                  and all(q % d for d in range(2, int(q**0.5)+1))]
        assert primes and all(q in rows for q in primes)
        den = sum((Fraction(1,q) for q in primes), Fraction())
        num = sum((Fraction(1,q) for q in primes if rows[q] == 0), Fraction())
        ratios.append(num/den)
    results.append((p, *ratios))
assert len(results) == 36
assert all(r[1] == 1 for r in results)
assert all(r[2] >= Fraction(3,5) for r in results if r[0] >= 10**6)
for p, half, one in sorted(results):
    print(p, float(half), float(one))
```

## 6. Reach upper bounds: what works and the missing all-level proof

I checked the argument independently against Shiu's range as restated in [Pollack, Theorem A](https://www.pollack-math.net/brunmultiplicative4.pdf): modulus k < y^(1−α), interval length x^β < y ≤ x, coprime residue, with fixed positive α,β < 1/2. For f = τ, the hypotheses on prime powers and subpower growth hold, and the resulting upper bound is ≪ (y/φ(k))log x. A parallel analytic audit identified the same large-Q issue; I checked the repair below rather than adopting its conclusion without review.

### 6.1 Proposition 6.3 is repaired

The weighted sum H_q and its partial-fraction decomposition are as in R2. The coprime progression terms above q² contribute O(L²/q) to A_r; the small range contributes Oε(q^(ε−1)log q); after the q/r sum this becomes Oε(q^ε(log q)²). With q ≤ L^C and ε = min(1/2,1/C), the latter is absorbed by O_C(L³). The noncoprime r = 0 term is handled by τ(qv) ≤ 2τ(v), not by a false application of coprime Shiu. The +1 terms are bounded using 1 ≤ X/(4quv). This establishes the stated integer bound.

### 6.2 Before Brun–Titchmarsh, discard noncoprime tuples correctly

A prime counted by a tuple at level Q must satisfy 4Quv ≤ p. For Type II the off-q progression is p ≡ −e (mod 4uv). If d = gcd(e,4uv) > 1, then d divides p, impossible since d ≤ 4uv < p. Thus those tuples contribute zero **while the lower height restriction on p is retained**. Discard them first, then enlarge the surviving counts to π(X;4uv,c) and use BT.

For Type I, ep ≡ −1 (mod 4uv) already implies gcd(e,4uv) = 1; otherwise there is no progression. Its tuple count is bounded by the same τ(Qu+v), with the parameters renamed. This is the missing justification for treating the two types identically.

### 6.3 Level-one dyadic estimate

Choose a fixed small θ > 0, for example θ = 1/12, independently of the later divisor-bound exponent. For uv∈(T,2T], T ≥ X^(3θ):

1. If u ≤ TX^(−θ), the v-interval has length T/u ≥ X^θ. Its translated endpoint qu+2T/u is at most a fixed power of X, so Shiu at modulus 1 applies with a fixed sufficiently small β. It gives O((T/u)L), summing to O(TL²).
2. If u > TX^(−θ), then v < 2X^θ. For each v, enlarge the permitted u to the full interval (T/v,2T/v]. The cutoff on u could otherwise leave an arbitrarily short interval. The resulting progression in t = qu+v has length qT/v and endpoint comparable to that length; its residue v mod q is coprime. For polylogarithmic q, Shiu applies uniformly, giving O((T/v)L). Summing over v gives O(TL²).

Consequently V(T) ≪ TL². The use of 1/φ(4uv) ≪ (log L)/T is valid, and the block bound is

    ≪ X L² log L / log(X/(8T)).

The dyadic reciprocal-log sum is O(log L): denominators are separated by log 2 and bounded below by log(q/2) ≥ log(3/2). This includes the end block and q = 3; there is no singular zero denominator.

For T < X^(3θ), “Proposition 6.3 at height X^(3θ)” is not quite the right invocation, since its product bound contains 1/(4q). Use height Y = 8qX^(3θ), or directly use t ≤ 2qX^(3θ)+1 in the harmonic argument. Since q is polylogarithmic, this changes no logarithmic order. The BT denominator is ≫ L here, and the small-product contribution is O_C(XL² log L). Thus the level-one conclusion follows.

### 6.4 Why merely substituting Q = q^k is insufficient

At large levels Q need not be polylogarithmic. The length QT/v in the second case does not automatically satisfy Shiu's modulus restriction for all admissible Q,T,v. The sentence about t > Q² does not explain how the other contribution interacts with the BT denominator or repair the first dyadic case. This is a substantive omitted uniformity argument, not just a missing citation.

Here is a repair. Let F_Q(X) count prime–tuple incidences at level Q, with q∤uv retained. The harmonic argument gives, for every fixed 0 < δ < 1,

    H_Q := Σ_{uv≤X/(4Q), q∤uv} τ(Qu+v)/(uv)
           ≪δ L³ + Q^δ L²,                         Q ≤ X/4.

To verify this, write t = Qu+v and use the same partial fractions as in Proposition 6.3. Now gcd(t,Q) = 1. Above Q² apply Shiu dyadically in coprime classes mod Q; Q/φ(Q) = q/(q−1) ≤ 3/2. Below Q² use τ(t) ≪δ t^(δ/2), which gives A_r ≪δ Q^(δ−1)log Q and hence the error Q^δ(log Q)² after summing Q/r. The regular term and the remaining harmonic sum contribute O(L³), since log Q ≤ L. This proves the displayed bound uniformly even when Q is a power of X.

Split the levels themselves:

* **Q > X^θ.** Every admissible pair has log(X/(4uv)) ≥ log Q > θL. BT and the totient bound therefore give

      F_Q(X) ≪θ,δ X[L² log L + Q^δ L log L].

* **Q ≤ X^θ.** Repeat the two-case dyadic proof for T ≥ X^(3θ). In case 1, intervals remain polynomially long relative to their endpoints. In case 2, their length y = QT/v satisfies y ≥ (Q/2)X^(2θ), so Q < y^(1/2) for large X. This is more than enough for Shiu's modulus restriction. Hence V_Q(T) ≪ TL² uniformly. Small products are bounded using H_Q and their BT denominator ≫ L.

Combining gives the needed per-level estimate

    F_Q(X) ≪δ X[L²(log L)² + Q^δ L log L]
           ≪δ π(X)[L³(log L)² + Q^δ L² log L].

Each level-Q class has additive Haar mass 1/Q. Union subadditivity permits summing these masses even when boxes overlap. Thus

    Σ_p μ_q(covered)
      ≪δ π(X)[L³(log L)²/q + L² log L · q^(−1+δ)].

The manuscript drops **log L** from the second term in this summation. Restore it. Choose δ = min(1/2,1/C); then q^δ ≤ L for q ≤ L^C, and the error is absorbed into π(X)L³(log L)²/q. The desired all-level conclusion is therefore true after the repair.

### 6.5 Corollary 6.4 follows, but is not a cutoff theorem

Full coverage of the nonresidue units has Haar mass (q−1)/(2q) ≥ 1/3. Markov proves (a). Summing over q ≤ L^A and applying Markov at ηπ(L^A) proves (b): the extra logarithms are L^o(1), giving the stated L^(3−A+o(1))/η fraction. Dyadic intervals transfer the result to (log p)^A. A fixed reduced progression containing admissible primes has a positive constant fraction of the prime population, so restricting to it does not alter the density-zero conclusion. This proves MR(A,η) false for A > 3 for these families and this height.

But it does not say that no prime has a reached q above (log p)^3, or that reach forms an initial segment. It says that a prescribed q = q(X) sufficiently above that scale is reached by a vanishing fraction of primes, and that few primes have a positive-density collection of reached q below L^A. Every global average-count paraphrase must retain the range q ≤ L^C for fixed C; this proof does not sum uniformly to q ≍ p.

## 7. Summary and required repairs

“T2-lite reached” is fair because z51 CONTEXT expressly lists lowering the cap threshold from A > 2 toward A > 1. Part 5.5(a) does that unconditionally, using established theorems. Part (b) is an additional near-power result at a lower cap; it is **not** itself a fixed power saving. The bottom line appropriately disclaims an unconditional ES power saving.

The following repairs are required before acceptance:

1. **Complete Proposition 6.3′ at all levels.** Add the Q ≤ X^θ / Q > X^θ split, verify Shiu's interval and modulus conditions, and restore the log L in the Haar error. A correct proof is given in §6.4 of this report.
2. **Justify BT and the level-one boundary cases.** Discard noncoprime Type II tuples before dropping the height lower bound; explain Type I invertibility, the full-interval enlargement, and the corrected small-T height.
3. **Fix the overclaim in §9 and associated summary prose.** Replace “exists only up to q ≈ (log p)^3” by the uniform average/Markov statement. Retain the two subfamilies, height ≤ p, levels, and range q ≤ (log X)^C. An average bound is not a maximum-reach bound.
4. **Relabel the MF₁/MR₁ deliverable.** Keep the valid proved reduction and conjectural sufficient inputs, but do not count “T2-cond” as achieved under CONTEXT's hypothesis requirement. State explicitly that the MF₁ tests are vacuous on known ES primes and the MR₁ evidence does not establish visible weakness relative to the target conclusion.
5. **Make Proposition 5.2 quantitative without endpoint ambiguity.** Specify fixed η, the density asymptotic, and either slack constants such as those in §3.3 or a sharper proof of the exact c₀ endpoint. Exhibit a subset constant < 1 so 5.5(b)'s second term is demonstrably absorbed.
6. **Close the small domain gaps in Theorem 5.3.** Use p* for all odd prime characters; restrict actual forced windows to p ≡ 1 (4); choose an independent subset bias threshold below 1 for the weighted window count. Repeat the extra subset exceptional-set removal in §9.
7. **Qualify novelty and numerical language.** Credit Baier/Heath-Brown and Lau–Wu; distinguish the previously sketched A > 1 improvement from the new complete cap transfer and explicit bound. Do not claim to settle the architecture-specific ceiling question merely by improving e*. Specify η = 0.2 when citing the 0.6 MR₁ test, and call negative truncated-search tests failures of the recorded test, not proved failures of full reach.
8. **Keep heuristics visibly heuristic.** In §9, “typically (log X)^1.1 elements” can describe unreduced divisor-product choices, not distinct elements in a group of order ≍ log X. The pointwise coupon tail and its summability are model predictions, not a verified uniform law.

No change to `EXSET_CHAR_FORCING.md` is made in this review. No ES forcing hypothesis has been proved here.
