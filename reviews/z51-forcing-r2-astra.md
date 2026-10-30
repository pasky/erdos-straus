# Hostile referee report: EXSET_CHAR_FORCING (Astra, round 2)

Scope: §§5–7, the summary/bottom line and §9, and verification of the listed round-1 repairs in §§1–4. I read the specified briefs, CAP_BOUNDED §3, EXSET_SIEVE_MASS §§4–5, POINTWISE_MORDELL17, and DISCOVERIES (J)70, together with the relevant generic-line sources. ES remains open. Nothing in this report proves an ES forcing hypothesis.

**Principal findings.** The classical moment argument is correct, and the level-1 reach upper bound survives with explicit bookkeeping. However, the advertised general square-root barrier does not survive: a standard quadratic large sieve gives a stronger version of the very same moment argument. The claimed GRH distinction is wrong. The identification of the two-family reach with the seven-family generic-line analysis is false, with small explicit counterexamples. The requested numerical reach counts and all 2,682 stored witness identities pass independent checks, but some truncation claims and the numerical crossover calculation are false.

## 1. Verdict register

| Claim | Verdict | Finding |
|---|---|---|
| Round-1 repairs in §§1–4 / §8 | SOUND-WITH-MINOR | The listed substantive repairs are present; lifted sharpness reruns successfully. Some unrestricted barrier wording returns in the summary and §9. |
| Proposition 5.1, classical large-sieve inequality and exponents | SOUND-WITH-MINOR | Correct ordered-tuple energy, primitive-character sieve, and arithmetic. Treat r=0 separately and exclude/define p=2. This is not the strongest standard input. |
| Theorem 5.2, displayed inequality | SOUND | Direct partition into QR-biased and remaining primes, with the small p absorbed. |
| Theorem 5.2, equivalence of power savings | SOUND-WITH-MINOR | Correct for the explicitly defined X-dependent remaining set. “Balanced” is only one-sided as written. |
| Theorem 5.2, “each such prime” has many q≡3 (4) forced windows | MAJOR | Balance on all primes does not imply balance on that subset for each p. Remove another small exceptional set; also exclude η=1/2 from the ≫ assertion. |
| Corollary 5.3(a), MF implies the classical bound | SOUND-WITH-MINOR | Conclusion correct; the proof must use genuine dyadic intervals, not comparability on (√X,X]. |
| Corollary 5.3(b), MR implies MF | SOUND-WITH-MINOR | Correct pigeonhole argument, after specifying the odd-prime convention for reach. |
| §5, GRH does not make MF(A,η) imply ES for 2<A<4 | MAJOR | False: GRH gives QNR density 1/2+o(1) at every fixed scale (log p)^A, A>2. Thus MF is equivalent to eventual ES under GRH in this range. |
| §5, “weakest/exact” input and “genuinely weaker” claims | MAJOR | MF is sufficient, not necessary for a power saving; MR is a different, stronger certificate requirement. Moreover standard quadratic large-sieve moments already lower the sufficient threshold from A>2 to A>1. |
| Definition 6.1 and the two displayed identities | SOUND-WITH-MINOR | Finite, meaningful certificate-family definition. The equivalent profinite wording needs an explicit height parameter. It is not a definition of all congruence-certified forcing. |
| Definition 6.1, “exact” cutoffs and Type I tail restriction | MAJOR | E₁=p/12 is a truncation; the assertion that its tail needs b₁=1 or c=1 is false. E₂=p/4 is not globally exact either. |
| Lemma 6.2 | SOUND | CRT plus reciprocity, in the inherited p≡1 (4), q∤p domain. |
| Definition 6.1* | SOUND-WITH-MINOR | Retain modulus≤n explicitly and specify which parameter carries all q-adic valuation. The implications are then valid. |
| Proposition 6.3 | SOUND-WITH-MINOR | The stated level-1 bound is correct. The small-range error needs to be summed and absorbed with ε depending on C; Shiu needs a dyadic formulation. |
| Corollary 6.4(a)–(b) | SOUND-WITH-MINOR | Correct Markov and prime-normalisation bounds after domain conventions. They imply MR(A,η) is false for A>4. No maximum-reached-q or initial-segment assertion follows. |
| Corollary 6.4(c), common-set cardinality and N=X² classical cap | SOUND-WITH-MINOR | Correct under its positive-density common-set hypothesis; write an upper bound, not equality, for Ψ. |
| Corollary 6.4(c), arbitrary N and arbitrary coefficients | MAJOR | The final displayed inequality is false for unrestricted N. A uniform Rankin estimate repairs the conclusion for the fixed classical N+X² black box only. |
| Remark 6.5, displayed level-k estimate | MAJOR | Its small-range error loses a factor q^k. The desired Haar-measure conclusion is nevertheless repairable by summing the correctly weighted errors. |
| “Linnik fed by congruence-certified forcing is capped at X^{1/2}” | FATAL as an unrestricted method claim | Neither the common-set hypothesis nor the choice of sieve constant can be suppressed. Heath-Brown’s quadratic large sieve supplies a concrete counter-mechanism. A narrowly frozen classical-sieve bound survives. |
| §6.3, requested reach census and stored witnesses | SOUND | Independent enumeration matches all 16 requested q values; the special 17-line prime and all 2,682 rational identities check. |
| §6.3, medians and fitted exponents | SOUND-WITH-MINOR | Reproduced from raw files. They describe the searched subfamilies and cutoffs, not full ET reach or an asymptotic law. |
| §6.3, cubic-law/coupon “validation,” truncation transfer, MR crossover | MAJOR | Finite evidence is promoted too far; the stated crossover equation has log p≈840, not 200. |
| §6.4, circularity/CRT assessment | MAJOR | A nontrivial reach-failure bound could be genuine progress. A universal circularity theorem is not established by the displayed inclusion or by an unverified transfer of the supply-law hypotheses. |
| §7.1, generic-line reach identification | MAJOR | False even after removing the height cutoff: the two-family generic reach misses {3,5,6,7} at 17, whereas the seven-family analysis misses {5,7}. |
| §7.1, inference from generic coverage to ES on all n₂≤13 primes | MAJOR | The cited computation does not imply this. Supply a separate theorem; the local covering sources explicitly distinguish generic points from the whole least-QNR line. |
| §7.2, p=1240009 and table | SOUND-WITH-MINOR | The key arithmetic and table aggregates check. “ES through reach” means an actual-cell certificate, not Reach(p,17). The explanation by generic closeness is heuristic. |
| §7.2, finiteness prediction | SOUND-WITH-MINOR | Correct conditional prediction of the stated model, not a theorem or evidence of a proved uniform tail. |
| §7.3, growing coverings equal Reach / must reach both sterile cells | MAJOR | A covering proving ES need only certify the actual cell of each p. Full counterfactual reach is sufficient, not necessary. Generic sterility at all levels remains conditional at 17. |
| §0, bottom line and §9 | MAJOR | Repeat the false broad barrier, wrong GRH hierarchy, unsupported “full ET” terminology, erroneous crossover, and sufficient-to-necessary conversions. |

Here “FATAL” concerns the advertised unrestricted barrier, not the sound elementary lemmas or the narrower classical-sieve calculation.

## 2. Round-1 repair audit

The repairs listed in §8 are actually present:

* Observation 1.1(b) now uses (Z,2Z] and N=4Z², so the earlier A>4 small-prime loss is removed. The equivalence with eventual ES on n₂(p)≤R(p), and the distinction between unrestricted q and q≡3 (4) windows, are stated.
* Lemma 2.1 now says odd p and includes the Type II converse. Lemma 2.2 explains lifting the sharp quotient example by filling H.
* The sharpness script now constructs the lifted stabiliser. I reran `uv run --no-project scripts/z51_forcing_kneser.py 9 3`: 1,975 multisets, 908 failing boxes, no violations, lifted sharpness passed.
* The “exactly removes” claim is withdrawn, p=353 is included, and the relaxed Ω/Rankin limitation is no longer presented as loss of all window information.
* Theorem 3.1 retains p≡1 (4), is an upper bound at fixed q, and no longer claims a matching shifted-prime law. Growing-q uniformity of the Rankin argument is explicitly unproved.
* The real/nonreal Fourier split, exponent 1−1/√3, the corrected random-box saturation threshold 3 log 3, and the separate hypothetical joint-Fourier assumption are present.
* Proposition 4.1 includes the primality term in its Euler factor. Calculation 4.2 is now explicitly about two chosen envelopes, with uniformity in both k and the shifts hypothesised. The character-profile caveat is present.
* The RLD connection and correlation conclusions are appropriately weakened in §§4.2–4.3.

I do not reopen the round-1 proofs. The remaining problem is editorial backsliding outside those sections: §9 again says the “known multiplicative majorants” work “only” to a stated range and “jointly they give” a bound, without the selected-envelope and hypothetical-joint qualifications of Calculation 4.2.

## 3. Proposition 5.1 and the robust reduction

### 3.1 The supplied classical proof works

For p>y, no generator vanishes. With ordered r-tuples,

    a_n = #{(q₁,…,q_r)∈S^r : q₁⋯q_r=n},
    Σ_n a_n χ_p(n) = (Σ_{q∈S} χ_p(q))^r.

Each tuple has at most r! rearrangements with the same product, so

    Σ_n a_n² ≤ r! m^r.

Repeated primes cause no problem; they reduce the number of distinct rearrangements. No squarefree restriction is needed for the classical multiplicative large sieve. Each odd-prime Legendre character is primitive, and retaining just those characters from

    Σ_{d≤X} d/φ(d) Σ_{χ mod d primitive} |Σ_{n≤N} a_nχ(n)|²
        ≤ (N+X²−1) Σ|a_n|²

is legitimate, since d/φ(d)≥1. With N=y^r≤X² this gives the claimed 2X² energy bound.

The elementary lower bound π(y)≥y/log y for y≥17 gives

    m^r ≥ y^r/(log y)^r > X²/[y(log y)^r],

because y^{r+1}>X². Thus

    E ≤ y + 2y r!(log y)^r/(4η²)^r
      ≤ y + 2y (log X/(2η²))^r.

For fixed A and y=(log X)^A, r≤2log X/(A log log X). The logarithm of the last main factor is

    r[log log X + 2log(1/η) + O(1)].

This is (2/A+o(1))log X when log(1/η)=o(log log X), and ((2+4θ)/A+o(1))log X when η=(log X)^{−θ}. The prefactor y is X^{o(1)}. Restricting S to q≡3 (4) changes only a constant per moment, also X^{o(1)}. These claims are standard and correct.

Minor repairs: define the set using odd p, or explicitly use the Kronecker convention at 2; when r=0, discharge the result trivially rather than use 0^0 in r!≤r^r. The asymptotic claims are for fixed A>0 and fixed θ, where relevant.

### 3.2 Theorem 5.2: valid partition, invalid “each”

For p>y, if the number of QNR generators is at most (1/2−η)m, then Σχ_p(q)≥2ηm. Proposition 5.1 bounds that part of any prime set E. The remaining part is precisely the set displayed in Theorem 5.2. A power saving for it implies one for E, and conversely it is a subset of E. This equivalence is correct; it is a reduction of an exceptional-set problem, not a proof of an ES hypothesis.

However, the remainder only has a **lower** bound on its QNR count. It includes strongly NR-biased primes. Call it “not QR-biased,” or apply the absolute-value version of the same even-moment argument to obtain a genuinely two-sided balanced remainder.

More seriously, balance on all primes does not entail balance on the subset q≡3 (4) for each individual p. Apply Proposition 5.1 separately to that subset and remove its own X^{2/A+o(1)} bad primes. Only outside the union of these two small sets does the forced-window conclusion hold. At η=1/2 the claimed lower bound is zero, so it is not ≫y/log y. Use 0<η<1/2 for that assertion (or choose an independent fixed bias parameter for the subset).

### 3.3 MF: the dyadic proof needs an actual repair

The parenthetical “p∈(X^{1/2},X], (log p)^A≍(log X)^A; adjust η” is not a valid bias transfer. Constant-factor changes in the generator population can swallow an arbitrarily small fixed bias. It also revives the old small-p problem if used only once.

Use p∈(Z,2Z] and y_Z=(log Z)^A. Uniformly on this interval,

    π((log p)^A) = (1+o(1))π(y_Z).

Deleting the o(m) generators above y_Z preserves a bias η−o(1), hence at least η/2 for large Z. Apply Proposition 5.1 with outer parameter 2Z and sum over all dyadic intervals. Since y_Z=(log(2Z))^{A+o(1)}, the claimed exponent 2/A is unchanged. Finitely many small primes contribute O(1).

MR⇒MF is the straightforward pigeonhole argument in the manuscript. Define reach only at odd primes and replace π(y) by π(y)−1, or absorb the single generator 2 with an O(1)/slightly smaller η adjustment. For p≡1 (8), 2 is already a QR.

### 3.4 The GRH distinction is false

The actual manuscript claims that MF(A,η), 2<A<4, is not known to imply ES even under GRH. It reaches this conclusion from an unnecessarily coarse O(√y log²p) estimate. A weak estimate cannot establish the absence of a stronger standard consequence.

Under GRH, apply effective Chebotarev to K=Q(√p), p≡1 (4), discriminant p and degree 2. For the nonsplit conjugacy class,

    #{q≤y : (q/p)=−1}
      = (1/2)Li(y) + O(√y(log p+log y)+log p).

For y=(log p)^A and every fixed A>2, the error divided by π(y) is

    O((log p)^{1−A/2} log log p) = o(1).

Thus the QNR proportion is 1/2+o(1), uniformly in p. It exceeds 1/2−η for every fixed η>0 and every sufficiently large p. Consequently

    GRH ⇒ [MF(A,η) ⇔ eventual ES],  A>2, η>0 fixed.

This does **not** prove MF or ES from GRH. If the summary merely says “MF is not known to follow from GRH,” that remains consistent with ES being open under GRH; it is not a reason to call MF easier than ES under GRH.

Source checked: Lagarias–Odlyzko, *Effective Versions of the Chebotarev Density Theorem*, Theorem 1.1, including its range “every x>2,” in the [typeset primary text](https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf). Its error includes the harmless additional log discriminant term. The same estimate is already used in local `FROBENIUS_FIRING.md` Theorem 1.4.

### 3.5 A stronger standard sieve already breaks the claimed threshold

This is not an ES advance, but it is decisive against the manuscript’s “exact/weakest” and general barrier language.

Heath-Brown’s quadratic large sieve, in its version for arbitrary coefficients, states

    Σ_{χ primitive real, cond(χ)≤X} |Σ_{n≤N} a_nχ(n)|²
      ≪_ε (XN)^ε (X+N) Σ_{n₁n₂=square}|a_{n₁}a_{n₂}|.

Source checked: D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995), 235–275, Theorem 1 and especially Corollary 2, [original author PDF](https://ora.ox.ac.uk/objects/uuid:b188b365-d8d1-4267-8548-49f01e6cb6a7/files/m6af40476f1b860392271a2d8ecae593b). The exact arbitrary-coefficient formula is also displayed as equation (2) of [Liu’s exposition](https://arxiv.org/html/2505.09637v1); no new result from that preprint is needed.

Use the manuscript’s ordered-tuple coefficients, but take

    r = floor(log X/log y),   N=y^r≤X.

The square-correlation energy counts ordered 2r-tuples whose product is a square. Every such tuple admits a perfect matching of its 2r positions into equal-prime pairs. There are (2r−1)!! matchings and m^r choices of the pair labels. Hence

    Σ_{n₁n₂=square} a_{n₁}a_{n₂} ≤ (2r−1)!! m^r ≤ (2r)^r m^r.

This explicitly handles the squarefree issue; one must not falsely replace the quadratic-sieve energy by Σa_n² for these coefficients.

On the biased set the signal is still at least (2ηm)^r. Since m^r>X/[y(log y)^r], the result is

    E ≪_ε y + X^{2ε} y (log X/(2η²))^r
      ≤ X^{1/A+2ε+o(1)}

for fixed η and y=(log X)^A. As ε>0 is arbitrary, this is X^{1/A+o(1)} in exponent notation. The vanishing-bias version has exponent (1+2θ)/A. The same argument works for q≡3 (4).

Therefore a robust power-saving reduction is available already for **A>1**, not only A>2. Under the same hypothetical MF or MR with A=3, this standard sieve would give X^{1/3+o(1)}, beating the advertised square-root cap. No forcing hypothesis is supplied here; the point is that the alleged obstruction is an artefact of freezing the classical sieve constant at N+X².

One can see the same failure even without moments: take squarefree S-smooth numbers up to X, with S the odd primes ≤(log X)^A. Products of r distinct generators give X^{1−1/A−o(1)} such numbers for A>1. If all exceptional primes are QR on S, Heath-Brown’s squarefree theorem gives X^{1/A+o(1)} exceptions. These coefficients are supported on S-smooth numbers, exactly as in the broad wording under review.

### 3.6 Logical hierarchy and “circularity”

F((log p)^A) implies MF(A,η) for 0<η≤1/2, since exceptional primes then have no small QNRs. MF permits some small QNRs on an exceptional character profile, so it is formally less restrictive as a condition on such profiles. Strict mathematical weakness relative to ES is not established, and for A>2 it disappears under GRH as above.

MR is not simply a weaker F. F is automatic if ES is true, whereas MR demands counterfactual certificates and is provably false for A>4 even if ES is true. The valid implication is MR⇒MF, not an asserted equivalence among all three inputs.

MF is also not necessary for an ES power saving: an infinite power-small set of balanced exceptional primes would be compatible with that saving and would violate pointwise MF. Likewise “MF outside a power-small set” is a useful sufficient exceptional-set theorem, not intrinsically a circular argument. Its proof may be as hard as the desired conclusion, but that is an assessment, not a theorem established by set inclusion.

## 4. Reach definitions and certificate scope

The two displayed rational identities are valid. For Type I, the congruence en+1≡0 (mod 4bc) enforces the invertibility needed for −e^{-1}; e|(b+c) makes g integral. For Type II, c=(a+b)/e and d=(n+e)/(4ab) are positive integers at every positive n in the class.

At level 1, q∤a₁be or q∤b₁ce makes the q-coordinate independent of the off-q congruence, by CRT. The number of parameter pairs is finite under 4quv≤n, and

    qu+v ≤ quv+1 ≤ n/4+1.

Thus e≤n/4+1 does make both searches finite. Define the reached count as zero, or exclude n, when q|n, since Definition 6.1 itself assumes q∤n.

The “profinite point” wording describes membership in a finite class menu, but a profinite point has no size n. Introduce Reach_M(x,q), with a separate real/integer height M, if evaluating the definition at generic points later. Taking the off-q point equal to 1 is not the same as taking n=1 with modulus≤1.

For Definition 6.1*, explicitly carry forward modulus≤n and specify whether only classes with all q-power in one parameter are admitted. Remark 6.5 counts a=q^k a₁, q∤a₁be (and its Type I analogue). A broader interpretation allowing q in both parameters needs reduction or additional counting, not silent inclusion. With the stated one-parameter shape, Reach⇒Reach* and the forcing lemma are immediate. Use additive Haar measure on Z_q, so a q^k-box has mass q^{-k}; the nonresidue-unit set has mass (q−1)/(2q).

The universal paraphrase “any forcing statement proved from certificate congruence classes … is a reach statement” is unjustified. It must retain **this class family, this height bound, and the permitted q-adic levels**. Other ET families, general Type I certificates, larger moduli, and joint character arguments are not captured. Off-q classes can certify p directly; they are irrelevant after assuming p exceptional, but that does not make them irrelevant to every forcing proof. Moreover knowing an integer at all off-q moduli is itself injective information about that integer; the meaningful restriction is the finite certificate architecture, not merely saying that a proof “sees residues off q.”

### Concrete cutoff counterexamples

1. The assertion that Type I e>p/12 requires b₁=1 or c=1 is false already in the requested small sample. At p=100049,

       q=23, b₁=499, c=2, e=11479.

   Here e=23·499+2, q∤b₁ce, 4q b₁c=91816≤p, and 4b₁c divides ep+1. Both parameters exceed 1 and e>p/12. Another example is q=29, b₁=401, c=2, e=11631.
2. E₂=p/4 is not globally exact: p=89, q=11, a₁=2, b=1, e=23 gives modulus 88≤89, e|22+1, 8|89+23, and q∤a₁be, but e>89/4. It reaches the nonresidue 10 mod 11. This is a counterexample to the exact-cutoff assertion, regardless of whether another tuple reaches the same cell.

The independent p=100049 run finds 21 valid tuples beyond the advertised cutoffs among q≤60. They add no new QNR cells in that particular comparison. This validates the reported counts there, not the general claim that the truncated searches are exact or that tails can never fill the last hole.

## 5. Proposition 6.3: line-by-line check and repair

Write L=log X and

    H_q = Σ_{uv≤X/(4q)} τ(qu+v)/(uv).

A tuple contributes at most X/(4uv)+1 integers. For Type II its off-q class is n≡−e (mod 4uv). For Type I there is either no class, or exactly one class n≡−e^{-1} (mod 4uv); tuples with noninvertible e contribute zero. Dropping all coprimality restrictions only enlarges the τ bound. Thus the factor 2 for the two families is legitimate.

Under the product constraint, qu+v≤X/4+1≤X in the nonempty range. Grouping by t=qu+v is valid. The exact partial fraction identity is

    1/[u(t−qu)] = (1/t)[1/u + q/(t−qu)].

The first harmonic sum is ≤1+log t. The second is a progression beginning at its least positive representative r₀∈[1,q], and is ≤q/r₀+1+log t. This gives precisely the displayed upper bound. The regular term satisfies

    Σ_{t≤X} τ(t)(2+2log t)/t ≪ L³.

For the singular part, define

    A_r = Σ_{q<t≤X, t≡r (q)} τ(t)/t.

For r≠0 and t>q², use dyadic intervals (T,2T], not a pointwise application “at n′.” Shiu for f=τ gives

    Σ_{T<t≤2T, t≡r (q)} τ(t) ≪ (T/q)log(2T),  T≥q²,

up to harmless endpoint blocks. For example choose Shiu parameters α=β=1/4, interval length T and upper endpoint 2T: q≤√T<T^{3/4}, (2T)^{1/4}<T. The constants are uniform. τ belongs to Shiu’s class since τ(ℓ^j)=j+1≤2^j and τ(n)≪_δ n^δ. Partial summation/dyadic summation gives A_r^{large}≪L²/q.

I checked Shiu’s range and function hypotheses in Theorem A of [Pollack, *Nonnegative multiplicative functions on sifted sets*](https://www.pollack-math.net/brunmultiplicative4.pdf), which restates Shiu’s theorem with k<y^{1−α}, x^β<y≤x and gcd(a,k)=1. The local Shiu PDF is image-only under pdftotext; I do not claim to have read machine-extracted text from that original scan.

For q<t≤q², the elementary divisor bound gives, for any fixed ε>0,

    A_r^{small} ≪_ε q^{ε−1}log q.

This is correct. But after multiplying by q/r and summing over r, its contribution is

    O_ε(q^ε(log q)²),

not simply O((log X)²log q) without choosing ε. Since q≤L^C, choose ε=min(1/2,1/C). Then q^ε≤L, and this error is absorbed by O_C(L³). This is the missing uniformity bookkeeping.

For r=0, no coprime Shiu assertion is needed:

    Σ_{q<t≤X, q|t} τ(t)/t ≤ (2/q)Σ_{v≤X/q} τ(v)/v ≪ L²/q,

using τ(qv)≤2τ(v). The manuscript’s weaker O(L²) is sufficient as well. In fact the original q∤v condition excludes this progression, but retaining it costs nothing serious.

Consequently

    H_q ≪ L³ + L²log q + q^ε(log q)² ≪_C L³.

Finally, with B=X/(4q), each uv≤B satisfies 1≤B/(uv), so

    Σ_{uv≤B} τ(qu+v) ≤ B H_q ≪_C XL³/q.

This handles the +1 terms for both types. Multiplying the weighted part by X gives the proposition. No hidden factor q is lost in the level-1 conclusion.

## 6. Corollary 6.4 and Remark 6.5

### 6.1 Markov and prime normalisation

If Reach(n,q) holds, the reached count is at least (q−1)/2. Proposition 6.3 therefore gives O_C(XL³/q) reached integers. Restrict to primes and use π(X)≍X/L to obtain

    #{p≤X: Reach(p,q)} ≪_C π(X)L⁴/q.

This is an upper bound, also to be capped by π(X). It proves pointwise-in-q density zero when q≥L^{4+ε} within the stated polylog range. It does **not** prove that almost every p has no reached q above that scale, or that the reached q form an initial segment.

Summing over q≤L^A gives average number of reached q at most O(L⁴ log log X), with room to spare in the logarithm. Markov at ηπ(L^A) gives the stated L^{4−A+o(1)}/η prime proportion. Thus MR(A,η) really is false for A>4, even on the fixed positive-density progression p≡1 (8). To use the p-dependent threshold in MR, work dyadically as in §3.3 of this report.

For a common S, the hypothesis in (c) implies each q∈S is reached for a positive fraction of the prime population, so summing (a) proves |S|≪L⁴ log log X. “Half of all primes” is an awkward normalisation when the domain is p≡1 (4), or p≡1 (8) in the main application; replace it by a fixed positive fraction of the specified progression. Constants change, not the exponent.

### 6.2 The coefficient cap: a valid narrow statement, an invalid displayed proof for arbitrary N

Let K=|S| and let z be the K-th prime (or use a larger z if K is smaller). Replacing the generators by the first K primes can only increase the smooth count. Since

    K≪L⁴ log log X,   z≤L^{4+o(1)},

one obtains Ψ(X²,z)≤X^{3/2+o(1)}. Equality need not hold for a small S; write ≤.

For a common coefficient sequence supported on S-smooth n≤N and any character,

    |Σ a_nχ(n)|² ≤ #supp(a) Σ|a_n|².

Therefore an argument that **uses the classical numerical bound**

    (N+X²)Σ|a_n|² / (uniform signal lower bound)²

cannot return less than (N+X²)/#supp(a). At N≤X² the claimed square-root floor follows immediately.

For N>X², the manuscript replaces the numerator by X² and then asserts

    X²/Ψ(N,z) ≥ X^{1/2−o(1)}.

That is false: Ψ(N,z) is unbounded as N→∞ for nonempty S. Keep N in the numerator. A correct all-N repair is Rankin’s bound: for α=3/4+δ, 0<δ<1/4 fixed,

    Ψ(N,z) ≤ N^α ∏_{ℓ≤z}(1−ℓ^{−α})^{-1}
           ≤ N^α exp(O_δ(z^{1−α}/log z))
           = N^α X^{o(1)}.

Uniformly in N,

    (N+X²)/Ψ(N,z) ≥ X^{-o(1)}(N+X²)/N^α
                  ≫_δ X^{2(1−α)−o(1)}.

The minimum is at N comparable to X². Letting δ be arbitrarily small yields the intended X^{1/2−o(1)} floor for this classical formula. This correctly includes arbitrary signed/complex coefficients and the classical moment construction; it does not classify all ways to estimate the same character family.

### 6.3 Why the advertised barrier is not honestly scoped

There are two independent failures of generalisation.

**Population failure.** Corollary (c) assumes a fixed S reached on a positive-density population of primes. A confinement argument only needs its character conclusion on the actual exceptional primes, which could all lie in the rare reach-rich population. Reach availability on most ambient primes does not bound its availability on that specially selected exceptional set. Likewise a bound on |S_p| for almost all p does not manufacture a common S. Partitioning into subfamilies, using several sequences, or establishing conditional statements only after prior ES exclusions is not ruled out.

**Sieve failure.** The Cauchy–Schwarz floor is a floor for the chosen constant N+X². It is not a lower bound on the best quadratic-character large-sieve constant. Heath-Brown’s N+X estimate, with the appropriate square-correlation energy, breaks the broad conclusion as shown in §3.5. Even pointwise MR at A=3, if proved, would yield X^{1/3+o(1)} by that argument. It is consistent with the reach upper bounds; Corollary (b) only rules out A>4.

Thus retain, at most:

> For the specified ET subfamilies, a common generator set certified on a fixed positive-density prime population has size at most L^{4+o(1)}. Feeding only that set into the classical N+X² large-sieve formula, with S-smooth coefficients, cannot yield a bound below X^{1/2−o(1)}.

Explicitly exclude quadratic-large-sieve improvements and the other population architectures. Do not call this a barrier to “Linnik + congruence-certified forcing” generally.

It also does not meet the brief’s **T2-barrier** target as stated: that target was a proved circularity/necessity theorem whose input is at least as strong as the desired conclusion. A restricted floor that still permits a power saving is not such a theorem.

### 6.4 All levels: repairable conclusion, wrong per-level error

Put Q=q^k, and retain the one-parameter q-power shape a=Qa₁, q∤a₁be. Define H_Q with the restrictions q∤uv retained, so t=Qu+v is coprime to Q. The correct analogue of the preceding calculation is

    H_Q ≪_ε L³ + Q^ε L²,

uniformly for Q≤X/4. For t>Q² use Shiu in the progressions coprime to Q; Q/φ(Q)≤3/2. For Q<t≤min(Q²,X), the same elementary estimate gives the Q^ε term after summing Q/r. This argument does not require Q itself to be polylogarithmic.

The unweighted tuple/incidence count is consequently

    ≪_ε X[L³+Q^ε L²].

The manuscript instead displays X L³+X Q^{ε−1}L² before applying the Haar factor Q^{-1}. That loses a factor Q in the short-range error.

After applying the Haar weight, the correct total is nevertheless

    Σ_{n≤X} μ_q(covered NR units)
      ≪_ε X Σ_{k≥1}[q^{-k}L³ + q^{-k(1−ε)}L²]
      ≪_ε X[L³/q + L²q^{-1+ε}].

Choose ε=min(1/2,1/C). Since q≤L^C, q^ε≤L, and the last expression is O_C(XL³/q). Markov at mass (q−1)/(2q) gives the same corollary. This supplies a repair for the stated Haar conclusion, not a validation of the erroneous per-level display or an extension to uncounted ET families.

### 6.5 Novelty relative to EXSET_SIEVE_MASS

The repaired incidence bound is not literally EXSET_SIEVE_MASS Theorem 5.2. That theorem concerns depletion certified uniformly on a whole profinite avoider of a finite family and bounds Montgomery’s depletion sum. Here the off-q fibre is fixed at n, the class menu has height≤n, and one averages fibrewise coverage over n≤X. The new quantitative estimate for this restricted family is a distinct, elementary Shiu-based calculation.

It is not a strict extension of the old theorem to all Linnik methods. EXSET_SIEVE_MASS §4.2 expressly withdrew that kind of general claim, emphasised the prime-modulus/non-CRT door, and left other configurations open. The new manuscript must not reinstate the withdrawn conclusion under a broader-sounding “exact scope” label.

## 7. Independent numerical audit

I wrote `reviews/z51-forcing-r2-astra-check.py`. It imports no campaign mathematics code and does not use `scripts/z51_forcing_reach.c`. Its pair-first enumeration runs over every u,v with 4quv≤p, q∤uv, factors qu+v with a small SPF table, enumerates its divisors e, and checks the two divisibilities independently. It computes both the recorded cutoffs and the full finite Definition-6.1 search. No large Cartesian-product array is formed; at p=1240009 the SPF array has fewer than 310,005 32-bit entries.

Command, successfully run:

    ulimit -v 8000000; timeout 120s uv run --no-project reviews/z51-forcing-r2-astra-check.py

All executed shell commands used the requested memory limit and explicit timeouts. The script also independently regenerates the statistics from the raw text files, enumerates the generic two-family cells, and rebuilds the stored witness identities using exact rational arithmetic.

### 7.1 p=100049: columns 1 and 4

| q | Independent unreached QNR count | Stored column 4 |
|---:|---:|---:|
| 3 | 0 | 0 |
| 5 | 0 | 0 |
| 7 | 0 | 0 |
| 11 | 0 | 0 |
| 13 | 0 | 0 |
| 17 | 1 | 1 |
| 19 | 1 | 1 |
| 23 | 3 | 3 |
| 29 | 2 | 2 |
| 31 | 3 | 3 |
| 37 | 6 | 6 |
| 41 | 5 | 5 |
| 43 | 10 | 10 |
| 47 | 9 | 9 |
| 53 | 11 | 11 |
| 59 | 14 | 14 |

All 16 comparisons pass. Including the omitted Type I tail does not change these QNR counts at this p, although it adds valid tuples. At q=17 the missing cell is {5}; at q=19 it is {2}.

### 7.2 p=1240009

Trial division verifies primality. Euler’s criterion gives QR at 3,5,7,11,13 and QNR at 17, while p≡1 (8), so n₂(p)=17. The independent complete pair search at q=17 finds exactly one missing nonresidue, **{5}**, both with the recorded cutoffs and with the full finite Definition-6.1 bounds. Also

    p mod 17 = 12,
    p−1 = 2³·3·7·11²·61.

An independently found actual-cell Type I witness is

    q=17, b₁=1, c=4, e=7,
    b=17, k=31912, g=95736.

It gives, checked by exact fractions,

    4/1240009 = 1/2690839370144 + 1/1627512 + 1/382944.

Thus ES at this prime is certified, despite Reach(p,17) being false. This is also a concrete warning against equating ES on a line with full counterfactual reach.

The stored line17 table aggregates reproduce exactly: 285/286, 84/84, 36/36 at q=17, and every other entry of the displayed six-column table. This is an aggregate check of those files, not a fresh full enumeration of all 406 primes.

### 7.3 All stored sampled witnesses

I independently reconstruct a positive integer in each witness’s CRT class and verify the resulting three denominators by exact rational addition. Counts:

    Type I:  1,274
    Type II: 1,408
    Total:   2,682
    Failures:    0

This certifies soundness of those witnesses, not completeness of the search menu.

### 7.4 Fits and modelling errors

From the raw files I recover the median supplies

    49.0684, 85.8102, 128.0415, 202.0922, 318.1761, 421.7913,

the q* medians 17,29,36,50,60,93, and R_maj medians 34,43,67,96,141,186. The least-squares slopes are **3.14673** for supply and **2.28611** for first holes. The individual S_e/(log p)³ range is **0.0273168–0.0440847**. These reported numerical summaries are sound.

Qualify the interpretation:

* These are two ET subfamilies, with explicit e truncations, not “full ET Type I/II.” Remark 6.5 itself admits the omitted general Type I family; the generic-line counterexample below shows omitted families change coverage materially.
* “Supply is cubic” should be “the sampled supply is consistent with cubic growth.” Thirty-six deliberately selected primes spanning a factor two in log p do not establish a uniform asymptotic or its uncertainty interval. The median ratios do not validate an asymptotic law at exceptional primes.
* A coupon comparison is evidence of a fit in the measured bands, not validation of independent coupons or of the extreme tail needed to predict absence of all holes. With a cell-weighted aggregation over the four 10¹⁰ samples, I get 0.13635 observed versus 0.12246 for the averaged exp(−λ_q) prediction on [128,256), and 0.37899 versus 0.35551 on [256,512). The manuscript’s nearby numbers presumably use another aggregation; specify it. Mean of exp(−λ) and exp(−mean λ) are different.
* The claim that e≤10⁷ loses about 3% at the larger scales is not established by the displayed 10⁸ calibration. At that calibration the text itself says 99.97%, not 97%, is captured at 10⁷; 97% is its 10⁶ cutoff. A relative-cutoff extrapolation to 10¹⁰ is not a certified error estimate. Small supply loss can still alter a first hole.
* R_maj is computed at prime endpoints. Say “largest prime R≤1000”; the literal largest real R may not exist, and the largest integer R need not be prime.
* Most importantly, the displayed crossover arithmetic is wrong. For δ=0.1 the manuscript’s equation is

      0.033 L^{0.9} ≳ 2.1 log L,  L=log p.

  At L=200 its sides are **3.88545** and **11.12647**. Equality occurs at **L≈840.2279**, or **log₁₀p≈364.9063**, not p≈10⁸⁷. A 60%-majority threshold needs a separate calculation integrating full-reach probabilities over q; it is not identical to the boundary-q or first-hole equation. Neither version should be advertised with the current unsupported crossover.
* The assertion that MR is “numerically false at every accessible p” overstates the sampled population and confuses failure in a finite range with an eventual hypothesis. At the largest scales y=(log p)^{2+δ} can also exceed the searched q≤1000 range. In any case the standard quadratic sieve means A>2 is not the necessary threshold for a power saving.

## 8. The 17-line dictionary is false as written

### 8.1 Two families are not seven families

POINTWISE_MORDELL17 Lemma 1.1 distinguishes P, Q, Q^{-1}, U, U^{-1} (with the square-root type empty). Definition 6.1 contains the U and U^{-1} shapes, not the other families. Equality of their generic coverage is neither stated in that source nor true.

Here is a complete independent finite calculation at generic off-q coordinates, **without any modulus-height cutoff**. In the two families, e must satisfy

    e = 4uvt−1,    qu+v = ce,
    u = (v+c)/(4vtc−q),

for positive integers u,v,c,t, with q∤uve. Positivity and u≥1 give

    4vtc≤q+v+c,
    v,c≤(q+1)/3,
    t≤(q+v+c)/(4vc).

These are finite exhaustive bounds. The script enumerates them and takes residues −e and −e^{-1}. Results:

| q | Nonresidues missed by the two Definition-6.1 families at the generic point |
|---:|---|
| 3 | none |
| 5 | none |
| 7 | none |
| 11 | {2,6} |
| 13 | {2,5,7,8} |
| 17 | {3,5,6,7} |

At 17 the covered set is {10,11,12,14}. The seven-family computation in (J)70 instead leaves only {5,7}. At 11 and 13 it leaves no nonresidue cells, whereas the two-family search still misses cells. This is an explicit refutation of “precisely Definition 6.1’s reach,” even after forgiving the missing profinite height parameter.

The one-way inference survives: a cell missed by **all seven** families at level 1 is missed by the two-family subset at that generic point. This is enough for some obstruction comparisons, but not for equality, exhaustiveness, or claims of “full ET” reach.

### 8.2 Generic coverage is not coverage of every least-QNR prime

A point whose off-r coordinates are all exactly 1 is much more restricted than a prime that is merely a quadratic residue at primes below r. The (J)70 computation certifies the former.

The supplied brief repeats “ES is known whenever n₂≤13,” but its cited source does not establish that assertion. `POINTWISE_MORDELL.md` explicitly distinguishes the whole np variant from the r-generic point; its §2 reports an open covering search for the np variant at r=13. `POINTWISE_MORDELL13C.md` likewise records remaining covering leaves. A finite search with survivors does not prove the ES theorem false or impossible, but it certainly cannot be cited as a completed covering theorem. Supply a separate, precise reference for the asserted n₂≤13 theorem, or withdraw the inference and state only the verified generic-line result. The same issue affects the explanation of the two Reach(p,13) failures in §7.2: omitted families are already a possible cause, not merely the modulus bound or level≥2.

The large-r sterile-point citation should use the actual proved threshold 2^{21.4375}≈2.84·10⁶. Writing a literal theorem “for r≥2.8·10⁶” rounds the threshold in the unsafe direction.

At 17, the uniform-multiplicity Conjecture 4.2 is in `SIBLING.md`, recorded in DISCOVERIES (J)77, not POINTWISE_MORDELL17’s Conjecture 4.2. The latter document has a conditional Corollary 4.2 and a sterility Conjecture 4.3. Give the exact reference and retain the conditional status. The unconditional “finite coverings are dead there” phrasing in §1.2 is not justified at 17.

### 8.3 Growing coverings and B2

A p-dependent certificate for each prime on the 17-line proves ES there. It need only hit **p’s actual residue**, and it may use other families, higher levels, or moduli outside this menu. Requiring every counterfactual nonresidue cell to be covered at each p is strictly more demanding as a certificate problem. The verified p=1240009 example demonstrates the distinction inside the very same bounded menu.

Thus replace “a growing covering is exactly Reach(p,17)” by “pointwise Reach(p,17) is one sufficient growing-covering target.” Likewise a proof of ES on the line need not reach both cells 5 and 7 for every line prime.

A limited statement from Comp. 4.1 is valid: if p≡1 modulo a 17-free L, a level-1 class whose **entire off-17 modulus** divides L cannot cover the generic survivor cells. For this level-1 strategy a certificate hitting those cells must use off-17 information not fixed by L. Higher levels already cover portions of C₅ and C₇ in POINTWISE_MORDELL17; level-1 survival does not exclude them. Also keep the factor 4 in the modulus: if L denotes the full off-17 modulus, the correct failure of containment is 4a₁b∤L, not automatically a₁b∤L.

Calling the remaining fixed-p divisor event “B2-type” is a reasonable assessment. “No congruence argument can supply it uniformly” is not an unconditional theorem for 17: full sterility is conditional, and a sterile profinite limit excludes a finite covering, not an arbitrary unbounded p-dependent procedure.

Finally, Proposition 6.3 is an **upper** bound. It does not show that supply is ≍(log p)³ per prime, nor that a particular cell has abundant supply at a fixed prime. The sentence attributing that abundance to the proposition repeats exactly the upper-bound-to-asymptotic error repaired in round 1.

### 8.4 Finiteness heuristic and composite window

Under the asserted uniform coupon model, Σ_p exp(−c(log p)³)<∞, so finite expected failures and an almost-sure finiteness prediction are legitimate. Independence across p is not needed for this first-moment/Borel–Cantelli implication. What is unproved is the model’s uniform tail, especially on primes approximating generic obstructions. Keep the label heuristic; “all tested primes beyond” must mean the specified samples, not all primes beyond the cutoff.

The final window observation is correct in its limited sense: 17≡1 (4), so it is not a prime window for p≡1 (4); at m=51, x=(p+51)/4 is a residue modulo 3 and a nonresidue modulo 17 on this line. That does not force the target −1 modulo 3. Existing prime-window results apply to the later q≡3 (4) forced windows, but their unrestricted prime-average estimates do not automatically become uniform conditional estimates on a thin character-selected subpopulation.

## 9. Required scope changes in the summary and conclusion

The opening disclaimer that ES is open is correct and should remain. It does not cure the following overclaims:

* Replace “the exact/weakest input Linnik needs” by a specified sufficient hypothesis for a specified sieve. Include or explicitly distinguish the stronger standard quadratic sieve.
* Remove the GRH-based claim of strict weakness for MF at 2<A<4. State the actual GRH equivalence.
* Replace the broad square-root headline by the common-set/classical-N+X² proposition, if retained. “For most p at most L^{4+o(1)} moduli” is not a statement about the actual exceptional set or an upper bound on the largest reached modulus.
* Replace every “full ET”/“exact reach” label with the precise two-family, level-1 and cutoff description, except where a complete finite enumeration is actually supplied.
* Downgrade “cubic,” “validated coupon model,” and fixed numerical crossover claims to measured fits with explicit limitations; correct the crossover arithmetic.
* Replace “equivalently the needed pointwise input is MF,” “only a pointwise proof breaks the circle,” and “ES on the line is Reach” by the valid sufficient implications. Power-small exceptional reach failures can also be useful if proved independently.
* Preserve the round-1 qualifications on selected window envelopes and hypothetical joint estimates in §9.
* Distinguish generic-point coverage, all-level sterility, and coverage of every actual prime on a least-QNR line. None is interchangeable with the others.

## Overall verdict

**MAJOR revisions required; the general T2/square-root barrier is FATAL as advertised, but several useful restricted results survive.** Proposition 5.1 is a sound classical moment argument, Proposition 6.3 has a short rigorous repair, Corollary 6.4(a)–(b) survives, and the all-level Haar conclusion can be repaired. The requested numerical audit is unusually clean: all small-prime reach counts, the special 17-line example, the fit summaries and all 2,682 sampled identities check. Nevertheless, the manuscript’s principal interpretation is not reliable. Standard GRH contradicts its asserted hierarchy, standard quadratic large-sieve moments beat its headline method floor, its common-set hypothesis cannot be transferred to arbitrary exceptional primes, and its generic-line dictionary omits certificate families that demonstrably change the answer. The deliverable is currently a restricted incidence upper bound and numerical study, not a proved general Linnik barrier, a full ET reach census, or a pointwise ES theorem.

## Required repairs

1. Correct the GRH discussion: for fixed A>2 and η>0, GRH makes MF(A,η) equivalent to eventual ES; do not infer a threshold 4 from a coarse error estimate.
2. Account for Heath-Brown’s quadratic large sieve and the square-correlation moment energy. Withdraw the general square-root barrier and the claim that A>2 is the weakest standard power-saving threshold.
3. Repair Theorem 5.2’s subset-window assertion by deleting another small exceptional set, distinguish one-sided from two-sided balance, and exclude η=1/2 from the many-window lower bound.
4. Give the genuine (Z,2Z] proof of Corollary 5.3(a), define the odd-prime convention, and replace necessity/equivalence claims for MF and MR by the actual sufficient implications.
5. State the certificate family, height bound and q-adic support in both reach definitions; retract the universal characterisation of congruence-certified forcing and all unsupported “full ET” labels.
6. Fix the finite-search cutoffs and the false Type I tail restriction, with convergence checks or lower-bound labels wherever completeness is not established.
7. Supply the explicit Shiu range and ε(C) bookkeeping in Proposition 6.3; correct Remark 6.5’s factor-q^k error and sum the weighted errors as shown here.
8. Repair the arbitrary-N proof in Corollary 6.4(c), retain its positive-density common-set hypothesis and classical N+X² black-box scope, and do not call it the brief’s general T2-barrier.
9. Correct the numerical crossover, specify coupon aggregation and prime-endpoint R_maj, and separate fitted evidence from asymptotics, validated tail laws, or assertions about every accessible prime.
10. Replace the false generic-line equality by a subset relation; distinguish the two families from the seven-family computation, give a valid reference for any n₂≤13 theorem, and correct the large-r threshold and 17-sterility citation.
11. Replace “growing coverings equal Reach” by sufficiency, retain conditionality of the all-level 17 obstruction, and remove the claim that Proposition 6.3 proves positive supply at each prime.
12. Propagate every scope repair to §0, the bottom line, §1.2, §6.4 and §9; preserve the selected-envelope/hypothetical-joint qualifications from round 1.
