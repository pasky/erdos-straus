# Z53 WILDCARD — independent hostile review

Reviewed `side-agent/z53-wildcard` at `7708457b800fc198a4da0b01910adf9e87c9d424`.
**Verdict: REJECT as written; retain the sound algebra and computations after repair. ES remains OPEN.**
The decisive defect is the “no false kill / no survivor” conclusion, not the numerical census.

## Per-claim audit

| Claim | Classification | Independent derivation / defect |
|---|---|---|
| §0, four (★) formulations; §1.4 spectrum | CORRECT | `(4Cu−1)(4CB−1)=4Cp+1`; `p+u=B(4uC−1)`. A common factor of u,B divides p and cannot equal p by positivity. Conversely coprimality gives uB dividing p+u+B, and the stated 2-adic condition gives 4uB. Finally u=(−p mod d), since 1≤u≤(d+1)/4<d. The r-spectrum intersection is exactly r=4C. |
| Lemma 2.1 | CORRECT | For u=2^a v, v odd, reciprocity gives (v/d)=(−1/v)(−1)^((v−1)/2)=1. If a>0 then d≡7 mod 8, so (2/d)=1; (−1/d)=−1. |
| Corollary 2.2, square obstruction and non-residue | CORRECT | A candidate d is coprime to 2u. At every prime factor of d, −u≡q² is a nonzero square, contradicting the lemma. For prime p≡1 mod 4, (d/p)=(p/d)=(−u/d)=−1. This concerns candidate divisors, not arbitrary divisors without the coprimality condition. |
| §2.2 derivation of II | CORRECT | With coprime a,b, gcd(ab,4gab−a−b)=1, hence ab divides x. Since x″(4gab−a−b)=pg and p∤x″, write 4gab−a−b=ph, x″h=g, g=hC. The displayed three reciprocals sum to 4/p. |
| II-i through II-v | CORRECT | i: d=4ahC−1, b=(hp+a)/d. ii: h=(d+1)/(4aC), gcd(h,d)=1, so d divides hp+a iff d divides p+4a²C. iii: multiply (4ga−1)(4gb−1); the complementary factor is also −1 mod 4g. iv: h divides a+b, t=(a+b)/h=4abC−p≡3 mod 4. v: a≤(d+1)/(4h)<d forces a to be the nonzero least residue of −hp; its divisibility condition recovers C. |
| §2.2(b), all-h square/non-residue obstruction | CORRECT | gcd(d,ah)=1. From d dividing hq²+a, −ah≡(hq)² mod d is a unit square. For prime p, (p/d)=(−ah/d)=−1 after multiplying hp≡−a by h. Apply Lemma 2.1 and reciprocity. |
| §2.2 heuristic “one of each divisor pair” cutoff | WRONG justification / GAP heuristic | At p=73, (a,b,C,h)=(2,5,2,1) is a genuine certificate. Its certifying d=15 exceeds √75; after swapping a,b, d=39 exceeds √78. The complementary factors 5 and 2 are not in the required classes. Thus the cutoff is not a symmetry reduction of the count. The log³ heuristic may be retained separately, not derived by this sum. |
| §2.3 Type I and divisor form | CORRECT | gcd(y₁z₁,y₁+z₁)=1 gives x′=abC, and C divides g. Then tp=4abC−1 and t divides a+b. Conversely k=(a+b)/t gives denominators pabC,aCk,bCk. Reducing t dividing a+b gives t dividing 4Ca²+1; tp≡−1 mod 4aC recovers b. |
| §2.3 Type I square citation | CORRECT | Checked the primary PDF `sources/elsholtz-tao-1107.1010.pdf`, Prop. 1.6 and §4 (not merely FRONTIER). Its odd-square vanishing statement is exactly the cited one. The proof compares (ab/t)=−1 with (oddpart(ab)/t)=1; if ab is even then t≡7 mod 8 and (2/t)=1, contradiction. |
| Proposition 2.4, as quantified | WRONG; repairable | Set Q=x²+y², Λ=ℤ², C=0, u=x³, B=−x³−x²−y². The identity holds but only C is constant. Alternatively u=0, B=−Q, C=x. The hypotheses explicitly omit positivity and do not require nonzero polynomials. |
| Proposition 2.4, intended positive/nonzero scope | CORRECT-WITH-FIX | Require CuB≠0. With at least two nonconstant factors, product degree strictly exceeds both subtraction degrees, so its degree is 2. Exactly two nonconstant factors must then be linear, factoring Q; three are impossible. With two constants, the remaining polynomial is quadratic. Congruence language additionally presumes integer constants/values, or explicitly cleared denominators. Full-rank and irreducibility restrictions remain essential. |
| §2.4 rank-1 example | CORRECT | 4·((x+1)/32)·8·x−8−x=x²−8; C is a positive integer on the indicated positive part of x≡63 mod 96. It does not contradict the repaired full-rank result. |
| Lemma 4.1, primitive-pair privacy | CORRECT | The common divisor divides h′a−ha′, nonzero for distinct positive primitive pairs, with magnitude <2AH. For nonprimitive a=ka₀,h=kh₀ the equation forces b=kb₀; reducing gives (a₀,h₀,b₀,C′=k²C). The certifying divisor satisfies a stronger congruence. |
| Lemma 4.1 strategic consequence | GAP / overclaim | Disjoint large prime factors do not imply independent events, absence of joint residue constraints, or absence of every deterministic cross-layer mechanism. FRONTIER's privacy barrier explicitly exempts mechanisms that never pool factors. |
| §3.1 CERTIFIED census | CORRECT | Original C program rerun to 200000 with a≤300 for Type I; output agrees byte-for-byte. Enumeration is exhaustive for (★)/II because p≥4ab−a−b and h divides a+b. For Type I, a≤b implies n≥2aC, giving its stated bound; the a≤300 restriction is honestly labelled. |
| §3.2 count table / six-of-nine observation | CORRECT | All 70 rows independently reproduced through II-ii, not the author's (a,b,h) loop. All 54 neighbouring primes independently checked. Exactly 5569,9601,83449,102001,329617,712321 satisfy the aggregate comparison. |
| §2.5 and §§4–5 strategic verdict | GAP / overclaim | Assessment labels are appropriate for limitations of known tools, but “dead”, “None as a route”, and “no false kill” are not consequences of the cited scoped results. See the audit below. |

## False-kill audit of every §1 idea

Here “false kill” means an unsupported exclusion, **not** a proof that the idea works or deserves priority.
Moreover, universal (★) is already false at p=409: reopening structural investigations of its spectrum/graph/ray classes cannot revive that universal assertion. A route to ES must use a broader family or handle these failures separately.

| Idea | Does the cited barrier actually cover it? |
|---|---|
| 1, full Type II | **False kill if “None as a route” is literal.** FRONTIER B2 explicitly confines its conditional impossibility to a fixed finite menu and exempts growing p-dependent families. T1 only kills square-blind arguments; B6 only prevents inference from averages. None excludes a prime-specific mechanism across the full family. Already-known parametrisation is a novelty verdict, not a no-go theorem. |
| 2, Type I | Same distinction. Identification with ET and forced non-residues do not kill every possible pointwise argument. No new argument was supplied, so “not advanced here” is justified, “None” is not. |
| 3, nonsquare exceptional set | **Not killed by T1.** T1 proves squares fail, not that no mechanism can prove a converse for the noncoprime algebraic family. The finite census is consistent with that conjecture. Mark open/reformulation, not excluded; strict ET coprimality has the five observed extra exceptions. |
| 4, r-spectrum composition | **Clear scope mismatch.** Checked the actual (J)82 source `LATTICE_MEETING.md` §§1.3,2.1–2.3. Downward propagation fixes (k,d) and uses controlled lifts u≡1 mod 4h in particular split-slice lattices. It is not a theorem about every closure/selection law on R(p). Cor. 1.5's repaired reading explicitly does not exclude class data guiding produced norms. Two spectra lacking an obvious pattern are not a no-go result. |
| 5, non-CRT covering | Correctly retained only as an already-listed open averaged target. Density bounds alone do not prove a prescribed prime covered; no impossibility for non-CRT improvements follows. |
| 6, genus/ray-class | **Clear scope mismatch.** `CLASS_FORCING.md` Thm. 2.1 concerns characters of the total product [N], whose residue is already known. It does not eliminate joint constraints on divisors, nor all varying quadratic fields/ray-class groups. Here Q(√−Cp) itself varies with p. “Its only p-dependent part is parity” is unproved. Pure genus/parity repackaging is blocked; the entire proposed investigation is not. |
| 7, quadratic-form polynomial identities | Not a false kill for the intended positive, nonzero, full-rank polynomial identity: the repaired degree argument covers it even though T1 alone does not. It says nothing about rational functions, thin loci, or nonpolynomial choices. Do not record the current malformed proposition. |
| 8, graph/Vieta moves | Linearity rules out a second root with the other two variables fixed, not all multivariable graph moves or a global existence argument. The cited signed-reflection result also has a square-class-preserving hypothesis. Broad “None” overreaches; the single-variable Vieta proposal is genuinely unavailable. |
| 9, C=2^j | The universal slice is genuinely false: p=409 has no (★) certificate at all, independently confirmed. Directly enumerated all possible C=1,2,4,8,16,32,64; no hit. Symmetry u≤B gives 4C−2≤p, so larger C are impossible. No reliance on the inherited 1298 count is needed. |
| 10, Davenport | Plain zero-sum/cardinality forcing does not force the target −1: arbitrarily many identity residues still fail. But “Davenport requires length comparable to group order” is not a general theorem (D(C₂^r)=r+1). This does not exclude arithmetic information on the full multiset; the memo appropriately points to that open problem. |
| 11, LLL/polynomial/circle/modular | These are objections to the sketched naive applications, not exclusions of entire methods. B3 expressly leaves polylog main terms with sufficiently small errors open. No randomisation or appropriate modular theorem is supplied, which supports “not developed”, not “dead”. |

## Numerical reproduction and limits

- Census: 8333 integers; failures (★)=189, II=148, coprime II=153, restricted I=148, neither=148; 2212 primes, seven (★) failures.
- Independently checked list equality: the 148 II/I failures are precisely the squares; extra coprime failures are 1705,3985,4585,6265,12145; seven prime failures match exactly.
- `scripts/z53_xrev_wildcard_counts.cpp` factors p+4a²C, with a≤b and 4a²C−2a≤p; each divisor recovers h,b uniquely. All hard/control/near-square rows agree. Memory O(max p), input cap 10⁶.
- Recomputed both R(409),R(577)∩[1,40]; both printed lists agree. Verified the Proth-slice counterexample and heuristic-cutoff counterexample directly.
- Commands used `ulimit -v 6000000`, CPU limits, and `timeout`; no unbounded computation. Source compilation, original census, and independent counts all completed successfully.
- Reproduce after extracting the reviewed branch under `/tmp/xrev_WILDCARD`: compile the C++ verifier with `g++ -O2 -std=c++17`; pass each `counts_{hard,ctrl,nearsq}.out` on stdin. It asserts equality of every field.
- The six-of-nine statistic does **not** test complementarity of zero events: all nine have positive II counts. It cannot support “the only thing widening buys is a larger mean”.

## Required fixes, priority order

1. Retract “no false kill”, “no idea survived”, and blanket route deaths. Restore the broader structural inquiries in ideas 4 and 6 as **unexcluded but undeveloped**, not universal-(★) conjectures; give ideas 1–3,8,11 their actual limited verdicts. None is thereby a demonstrated route to ES.
2. Repair Prop. 2.4 with nonzero factors and the integrality qualifications; only then export its scoped statement to FRONTIER.
3. Remove the invalid divisor-pair cutoff argument; separate the log³ heuristic/ET average from a fixed-p assertion.
4. Keep primitive-pair privacy, but remove the inference that it forbids every cross-layer mechanism. Keep the numerical comparison, but remove the inference against complementarity.
5. Recast §5 as **inconclusive: sound reformulations and finite data, one repairable scoped polynomial no-go, no new pointwise theorem**. The present claim to have eliminated the entire from-scratch list is not established.
