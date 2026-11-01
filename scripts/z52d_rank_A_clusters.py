#!/usr/bin/env python3
"""Reviewer-A hand clustering and independent judgements (not keyword ranking).

Members share a target or a stated specialization of it, not necessarily an
iff-equivalent conjecture. Exact source targets remain in F.jsonl; corrections
and quantifier distinctions below are part of the clustering.
"""
import json
from pathlib import Path

OUT = Path('data/z52d/avenue/rank_A')
CLUSTERS = []


def cluster(cid, name, band, mids, statement, yield_es, plausibility, frontier,
            obstruction, ingredient, new, scores, assessment):
    relevance, information, novelty, gaps = scores
    score = 5*relevance + 2*plausibility + 2*information + novelty - 3*gaps
    CLUSTERS.append(dict(id=cid, name=name, band=band, members=mids.split(),
        clean_statement=statement, yield_for_ES=yield_es, plausibility=plausibility,
        frontier=frontier, obstruction=obstruction, ingredient_can_beat_obstruction=ingredient,
        genuinely_new=new, score_components=dict(relevance=relevance, tractability=plausibility,
        one_day_information=information, novelty=novelty, unsupported_bridges=gaps),
        proof_priority_score=score, label='Assessment', assessment=assessment))


# (i): possible proof components. A live mathematical question is not a live proof.
cluster('A01','Height-dependent cancellation','i',
'Z1034 Z1855 Z1570 Z2997 Z0211 Z1480 Z2958 Z3149 Z1854 Z2080 Z2975 Z2387 Z3113',
'For some δ>0, at each prime p bound a genuinely class-filtered dyadic block of R(p)-M(p) by cancellation below its current divisor bound; ultimate target: R(p)≥ε M_BM(p) for all p>p0.',
'partial: first fixed-p class-aware saving; full only after a one-sided lower bound and effective finite check',1,
'FRONTIER §7.1; §6 Weil/bilinear/spectral limitations',
'B2 tied height/modulus, B3 polylog scale, B6 no averaging p; upper-tail obstruction to two-sided polylog errors',
'No demonstrated saving. Voronoi dualisation, trace-function reorganisation and incidence methods are candidate inputs, not refuted by the failure of the current estimates.',
'No new target; audit rescues dispersion/incidence and repairs absolute-error targets to one-sided ones.',(3,2,1,1),
'Best relevance, low tractability. R-M may have positive spikes, so do not demand O(log^A p) absolute error. A p^{2/5-δ} bound is weaker and not refuted by those spikes. Z1854 must use the exact trial range: at p=17 the ordered triple (u,B,C)=(6,1,1) has m=4uC-1=23>p, so the quoted truncated m≤p count is not automatically R(p). Use PARITY_AUDIT and keep boundary/symmetry conventions explicit.')
cluster('A02','Bounded-exponent character obstruction','i',
'Z3003 Z2940 Z1787 Z0648 Z0674 Z2926',
'For every sufficiently large p, some admissible window e has -1 in {ab^{-1} mod e: ab|N_e}; prove this via a quantitative inverse theorem for a missing target in the bounded-exponent product set, followed by a theorem excluding simultaneous obstructions across windows.',
'full with finite check; an inverse theorem alone is a structural side result',1,
'FRONTIER §7.3 and §7.13; §6 single-character Siegel dichotomy',
'B2 class versus subgroup, B4 sparse bounded exponents, T1, privacy across windows',
'Z3003 supplies an exact Fourier identity, a real handle on failure. It does not give a shared character or cap-0 coverage; subgroup saturation alone is insufficient.',
'Fourier obstruction certificate is explicit; the global exclusion remains entirely missing.',(3,2,1,1),
'Keep representation multiplicities and prime-power exponents. For q^a||N, a convenient signed-exponent kernel is Σ_{j=-a}^a χ(q)^j; it is not a subgroup indicator. The source uses the squarefree 1+2Reχ kernel. The max-character sufficient criterion is very strong; cancellation in the whole character sum can certify without it. Z2926 restricted to prime windows needs exceptions (3361), not an all-prime claim.')
cluster('A03','Pell-cycle growing roots','i',
'Z0596 Z0465 Z1298 Z0385 Z1687 Z3053',
'For every sufficiently large prime p≡1 mod4, a specified root extracted from the full principal reduction cycle of Q(√p), or its forest component, meets a bichromatic edge of F_p.',
'full via ES5 plus finite check, provided the root recipe and traversal are proved',1,
'FRONTIER §7.2; §6 only CF-norm windows and fixed-root constructions are closed',
'B2; fixed-root Dickson obstruction; CF norms are QR windows (JOINT_BUDGET Prop 4.2)',
'Pell data depend on p non-polynomially and primality descent is an actual pointwise precedent; neither supplies the divisor class yet.',
'Only a specialization of the existing open root source; full-cycle tests differ from the refuted one-step tests.',(3,2,1,1),
'Z1687 and Z3053 overstate known-false: the cited result concerns norms as windows or fixed roots. Z0596 already reports six failed one-step examples below 30000. Do not repeat that exact test or interpret a bounded component traversal as an exhaustive failure.')
cluster('A04','Complementary-line switching','i','Z3182',
'Construct an explicit, uniformly valid switch from a defined set of wrong-class (★) factor pairs into b=1 certificates, with a defect inequality ensuring R_star(p)+R_b1(p)>0 for every p>p0.',
'full with finite check',1,
'FRONTIER §2.1 union conjecture; related §7.3; §6 transport limitations are scoped',
'B2 on each line; B3 target mass; no known sign-definite defect identity',
'A switch would use relation between two target families, not merely their empirical disjoint failures. No actual map is supplied.',
'Audit restores a mechanism wrongly called circular; complementary coverage itself is already known as a conjecture.',(3,2,1,1),
'The count union is a target, but a constructive switch is stronger structure and not equivalent to the union assertion. Prioritize a small algebraic falsifier over extending the census. A switch only on existing successes cannot prove coverage.')
cluster('A05','Growing positive minorants','i','Z1401 Z2845 Z2534 Z3041',
'Produce an explicit, independently evaluable lower minorant F(p)>0 of a nonnegative certificate count, using a growing-level identity or a dual combination of proved character-sensitive linear constraints, for every prime p>p0.',
'full with finite check; a new valid inequality alone is partial structure',1,
'FRONTIER §7.3; §6 finite Eisenstein identities versus open growing-level identities',
'T1 must be built into the RHS, B2, B3; zeta(0) and twisted charges can have either sign',
'LP duality and Shintani cone formulas are concrete ways to check identities. No nontrivial positive minorant is known; the known W(n) identity leaves a spin positivity problem.',
'LP dismissal was logically invalid; no new usable constraint has been identified.',(3,2,1,2),
'T1 does not prohibit an inequality true for all odd n whose RHS vanishes at squares and is positive at primes. Source Z1401 asserted otherwise. A numerical dual must not include the certificate indicators or the desired conclusion among its assumptions.')
cluster('A06','One-coordinate level bound','i',
'Z0501 Z2018 Z2017 Z1600 Z1335 Z3167 Z2935 Z1805',
'There exist A,p0 such that every prime p>p0 has C≤(log p)^A with a divisor d|4Cp+1 satisfying d≡-1 mod4C; leave the complementary divisor and other coordinates unrestricted.',
'full eventually on (★), plus finite check; quantitative strengthening, not equivalent to ES',1,
'FRONTIER §7.2 one-coordinate analogue, §2.4; §6 two-endpoint/window-modulus bounds do not apply',
'B2; B1 for fixed C only; (★) has finite known zeros; no general factor-count⇒class theorem',
'Anatomy of integers gives distributional intuition, not an every-p input. No member controls actual prime-factor residues.',
'No new ingredient; preserve level versus witness modulus distinction.',(3,1,0,2),
'Z2018 narrower exponent is a separate strengthening within this cluster; Z2935 additionally excludes boundary witnesses. Known zeros require p0 above them, not abandonment of an eventual claim. Z1805 factor-count/Davenport forcing is invalid without bounded-exponent target coverage. Do not call this a broader family than (★), as Z2017 does.')
cluster('A07','One-coordinate endpoint/window bound','i',
'Z0148 Z0534 Z3087 Z0847 Z2363 Z1406 Z1850 Z2145',
'For every p>p0 some ES certificate has ONE designated parameter bounded by (log p)^A: specify separately HC/interior endpoint, U-vertex, or e=4x-p; other coordinates remain unrestricted.',
'full with finite check for each correctly defined variant',1,
'FRONTIER §7.2; §7.17 certificate-restricted I3; §7.13 for window/cap distinction',
'B2; B1 excludes bounded menus, not growing one-coordinate sets; H4 excludes bounding both endpoints',
'No provable growth bound. Least-QNR seeding in Z2145 adds a character but no class-control theorem.',
'No new target; source ambiguities are repaired instead of merging level, endpoint and denominator size as equivalent.',(3,1,0,2),
'These are related one-coordinate conjectures, not proven equivalent. Z2363 least max-denominator≤polylog p is false since x≥p/4; retain only its level interpretation. The finite I3_C zeros 5,13,17,2521 are not ES5 zeros. Distinguish HC, least U vertex and full e-slices in any computation.')
cluster('A08','Non-CRT averaged lower tail','i','Z2356 Z2407',
'For some δ>0 prove #{primes p≤X:R(p)=0}≪X^{1-δ}, using a class-sensitive bilinear estimate or an arithmetic/product-measure comparison strong enough for a relative-entropy lower-tail bound.',
'partial: power-saving exceptional set for (★), not ES at every prime',1,
'FRONTIER §7.5 and §7.12; §6 CRT supply caps and critical variance',
'B6 average yield; CRT cap if the new estimate factors into known congruence marginals; dependence is not Bernoulli independence',
'Bilinearity at fixed C is explicit; entropy is a possible framework only after a proved arithmetic comparison. Neither has been supplied.',
'The statistical route is not circular merely because it is averaged; both target a genuinely stronger partial theorem.',(2,2,1,1),
'A successful estimate would change the exceptional-set frontier, not solve ES. Use modulus 4uB in p≡-(u+B) mod4uB; the source next-step modulus 4uBC includes a solution coordinate incorrectly.')
cluster('A09','Forced budgets in exponential families','i',
'Z2969 Z3189 Z3061 Z0417 Z2031 Z2995 Z1557',
'For each s in the open family n_s=15·2^s+1 (or one explicitly chosen family such as 4^s+297), construct positive integer ES parameters by finitely many exponent classes and verified polynomial-exponential recurrences.',
'partial: all members of a named infinite family, including its primes; no general-prime transfer',2,
'FRONTIER §7.8; §6 thin-family menu transfer is closed, not the family itself',
'B1 finite congruence cover may fail; algebraic forced budgets escape it only through p=φ(s); no transfer to free p',
'Known forced-budget proofs and recurrence/folding/primitive-divisor structures provide a concrete handle. Need a new identity on the open branch.',
'Recursion is a variant of known mechanism, not a new route to arbitrary primes.',(2,2,1,1),
'Best chance of a real positive theorem in one short lane. Z3061 all (a,b,c) Type-I/II version is false without exclusions: 4^s+0 is an odd/even issue, and n_s=9^s is an odd square; T1 forbids the asserted types. Restrict to a named nonsquare family. Berlekamp–Massey fit is evidence until symbolic verification and positivity.')
cluster('A10','Full-factor-multiset compatibility','i','Z2818',
'Find a stated property A of actual factor multisets of {4Cp+1:C≤K(p)}, prove it for all p>p0, and prove that CRT-consistent, size-correct multisets satisfying A cannot all miss -1.',
'full with finite check if both new lemmas hold',1,
'FRONTIER §7.6; §6 single-factor reciprocity and privacy',
'B1 small-factor information, B2 full target; CLASS_FORCING Thm 5.2 leaves individual large-factor classes free',
'No candidate A beyond congruences is presently proved. Joint full-multiset constraints are not excluded by the single-factor theorem.',
'Exactly an existing frontier question; useful adversary specification, not yet an ingredient.',(3,1,0,3),
'Keep as a precise residual question. A cannot just be the existential certificate condition, and its T1 behavior must be stated.')
cluster('A11','Well-founded certificate transport','i','Z2095 Z3028 Z1964 Z2351',
'Define a certificate transport across different n or from structured solutions at mp to p, with a strictly decreasing positive-integer rank and a coverage lemma applying to every prime input.',
'full with base cases',1,
'FRONTIER §6 propagation paragraph expressly retains rule Λ and unrestricted norm descent',
'B2 gates on the proposed maps; finite affine menus meet B1; ES surface lacks a known preserving group law',
'No coverage/rank theorem. Non-scaling moves do exist (audit: (2,4,4) at n=4 to (2,4,20) at n=5), so scaling is not a universal impossibility argument.',
'Audit corrects a false universal rejection; no new uniform rule.',(3,1,1,3),
'An existential map chosen after finding an ES solution is vacuous. Specify a rule computed from the smaller witness, then prove integrality and coverage independently.')
cluster('A12','Integral Y–Δ normal form','i','Z1153',
'For each prime p, an explicit terminating integral positive network rewrite takes four parallel p-resistors to three integer branches, with a proved normal form/confluence invariant.',
'full if rewriting and termination are proved',1,
'FRONTIER §6 integral Y–Δ remains open; PROPAGATION_CLOSURE',
'B2 integrality of star–triangle moves, positivity, no known confluence; finite move tests are not universal no-go results',
'Concrete move calculus exists, but no global invariant forcing a three-branch terminal graph.',
'Existing open mechanism, no new rule.',(3,1,0,3),
'Prior bounded-depth traps limit the chosen move set only. Ordinary rational Y–Δ equivalence does not preserve integer resistances.')
cluster('A13','Exception propagation','i','Z2809',
'Prove a 4-specific successor law: failure at p implies failure at a prime p′ with p<p′≤p+exp(o((log p)^{2/3})), uniformly; iterate against the exceptional-set upper bound.',
'full by contradiction, if the uniform propagation theorem is proved',1,
'FRONTIER §5.4 amplification criteria; §6 existing proposed transports fail',
'Numerator blindness (8/131,8/241), no transport law, quantitative branching/gap threshold',
'AMPLIFY_EXCEPTION supplies the implication, not the successor mechanism.',
'No new mechanism.',(3,1,0,3),
'Not circular as a logical strategy: a local propagation lemma could be structurally stronger than ES. No such lemma is in this candidate layer.')
cluster('A14','Non-affine congruence/parity forcing','i',
'Z2921 Z1386 Z1771 Z2609 Z3094 Z0469 Z2033 Z0556 Z3101 Z0441 Z1650',
'Construct finite p-dependent objects with an independently proved nonzero count modulo m, and an action/involution whose surviving orbits or fixed points produce ES certificates.',
'full if the count law and certificate extraction are proved',1,
'FRONTIER §3 M5; §6 WINDMILL finite-affine no-go is conditional and scoped',
'T1; natural ordered counts are even; B1 for finite affine rules; class-number parity may be congruence-only',
'No concrete new object/action. Larger finite groups and genuinely non-affine maps are not covered by an involution-only statement without checking its proof.',
'Formal group-action extension (Z3101), no positive construction.',(3,1,1,3),
'Forced parity of a set defined to be all certificates would be a reformulation. A count on independent objects plus a map would not. Do not accept the source demand that any parity not determined by p mod8 kills the idea: non-congruential dependence is precisely an allowed escape.')
cluster('A15','Character-sensitive topological index','i','Z2764 Z2765 Z3027',
'Construct a finite candidate complex K_p with a computable nonzero mod-2 index/Euler invariant, and a fixed-point or complementary-edge theorem extracting a certificate; the construction must degenerate at odd squares.',
'full if complex, index and extraction are all proved',1,
'FRONTIER §6 global-positivity shapes; adjacent to M5, not a numbered §7 problem',
'T1; natural complement action works identically at squares; Euler characteristic can be sign-indefinite',
'Shellability/discrete Morse are possible tools but no K_p is specified.',
'Formal topology packaging; no independently justified invariant.',(3,1,1,3),
'Retain as unconstructed, not refuted. Natural divisor-poset Euler sums should first be compared to existing theta/divisor identities.')
cluster('A16','Sparse geometric shrinking targets','i','Z2504 Z2513 Z2933 Z0266',
'Specify a p-dependent family of independently existing CM/lattice objects and a target Ω_p with a verified map to certificates; prove a pointwise positive target count at its actual sparse scale.',
'full if a target-hitting theorem and integrality map hold',1,
'FRONTIER §7.1 adjacent; §6 known Heegner/CM and spectral estimates fail at scale',
'B3 for bounded-fibre power-size targets, B6 if averaging p; target volume is not proof of an integer point',
'CM points/lattices independently exist; no estimate resolves this target. High fibres or polylog targets are not ruled out by B3 Remark 2.4.',
'Audit restores an open scope; no new target or stronger equidistribution theorem.',(3,1,0,3),
'The literal h(D)-sized detector version is blocked if h(D) is power-size and fibres are subpower. This does not refute all arithmetic Riemann–Roch or sparse target mechanisms.')
cluster('A17','Adaptive complementary regimes','i','Z2512 Z2941 Z3002 Z2964',
'Give a non-congruential computable statistic separating primes into regimes, with a certificate theorem in each regime; a possible form is failure forcing quadratic residuosity beyond the Burgess least-QNR bound.',
'full with finite check if every regime is covered',1,
'FRONTIER §7.3 and §7.15; §6 Siegel dichotomy supplies no working instance',
'B1 fixed congruence splits, B2 on each branch, no repelled/successful branch known',
'No proved hardness statistic implies success in either complementary branch.',
'No new split with verified content.',(3,1,0,3),
'(★) zeros have small least QNRs; ES5 zeros must not be inferred from I3_C zeros. Numerics can reject a particular split, not all dichotomies.')

# (ii): bounded side targets with an identifiable mathematical or calibration payoff.
cluster('S01','Exponent-two failure taxonomy','ii','Z2409 Z1561',
'For t∈{4,8,12,24} and gcd(N,t)=1, -1 is a divisor residue of N iff it lies in the F2-span of the prime-factor residues; otherwise an odd real character is 1 on every factor.',
'none directly; exact baseline for beyond-BM inverse theorems',3,
'FRONTIER §7.3; METAPLECTIC_ES Thm K',
'Other levels have bounded-exponent gaps not detected by subgroup span; B1 forbids universal fixed-menu coverage',
'Elementary finite-group duality proves the statement; actual factor multiplicities matter only outside exponent two.',
'Useful explicit taxonomy already derived in this pass, not a proof advance.',(0,2,1,0),
'Bank the exact algebra, but separate it from unproved prime-density asymptotics. Level t=16 is NOT an elementary 2-group.')
cluster('S02','Fixed-level/joint failure densities','ii','Z1577 Z2619 Z2636 Z1927 Z3118 Z2399',
'For a specified fixed tuple of levels, establish upper/lower bounds for primes p for which each tp+1 lacks a -1 divisor; first treat t=4,8,12,24 with their exact character-kernel descriptions.',
'partial: quantitative densities of restricted failures, not a pointwise ES theorem',2,
'FRONTIER §7.3 calibration; §6 fixed-menu and averaged results',
'Prime-detection/half-dimensional sieve lower bounds; dependence between affine forms; bounded exponents outside t|24',
'Exact exponent-two descriptions make a fixed-depth sieve plausible, not arbitrary joint asymptotics automatic.',
'Explicit constants/joint dependence could be new; not new ES coverage.',(1,2,1,1),
'Downgrade source known-true claims for prime joint densities and every short interval unless a precise theorem is supplied. Z2399 finite congruence menus are easier than factorisation-defined fixed levels; keep that special case distinct.')
cluster('S03','Chain-denominator criterion','ii','Z0216',
'For p≡1 mod4 prime, a solution with x|y|z exists iff p+1 has a prime divisor ≡3 mod4.',
'partial: exact solvable restricted family; none on its complement',3,
'New elementary calibration relative to FRONTIER; boundary u=1 of (★)',
'Fixed line can fail; distribution of prime failures is a separate sieve question',
'Writing y=ax,z=abx reduces integrality to b=1 or p; b=p yields a -1 mod4 divisor of p+1.',
'Clean criterion, not a new global ES ingredient.',(1,2,1,0),
'Criterion is elementary and checked by the source. Infinite failure/density assertions must not be bundled into its PROVED label without verifying the shifted-prime sieve theorem.')
cluster('S04','Coprime-pair criterion','ii','Z0867',
'For p≡1 mod4 prime, a solution with some coprime denominator pair exists iff p+4 has a prime divisor ≡3 mod4.',
'partial: López d=1 subfamily; no coverage of its failures',3,
'FRONTIER §2.1 b=1 line; elementary subcase',
'B2 at general d; a fixed line has failures',
'Two-term factorisation gives an explicit criterion and construction.',
'New useful interpretation of an existing line.',(1,2,1,0),
'Check the coprimality converse algebra separately from the expected Landau failure density; they have different evidentiary status.')
cluster('S05','No-3 global failures','ii','Z0863',
'Classify the primes lacking an ES solution with 3∤xyz; conjectural list {3,241}, starting with a rigorous explanation of the finite 241 obstruction and a bounded census.',
'partial restricted-family theorem if classification were proved; finite/local work yields calibration only',1,
'Not a FRONTIER §7 target; related to §7.15 low-count sibling failures',
'B2 remains; global restriction is not a 3-adic obstruction',
'Finite exact enumeration is cheap; no mechanism proves only those two exceptions.',
'Audit-rescued distinct global problem; not logically equivalent to ES.',(1,2,1,2),
'checks.json independently enumerates all eight solutions at 241. (241,241,241/2) is a 3-adic-unit solution, excluding a naive local explanation. Do not infer universality from a finite list.')
cluster('S06','Primitive/all-even restricted worlds','ii','Z0866 Z0212 Z0524 Z2771 Z1942',
'Derive exact parameter and local-valuation criteria for a specified restriction (primitive gcd, all-even, allowed residues, or a power-of-two denominator), then compare its finite global failures with that criterion.',
'partial on restricted families; no unrestricted conclusion without a proved transport',2,
'Not one §7 problem; calibration for §7.13/§7.15 and numerator blindness',
'B2 for restricted universality; local admissibility is not sufficient; bounded number of adaptive powers is not a fixed polynomial menu',
'ET gcd/valuation parametrisations are elementary handles; no general conversion among these worlds is proved.',
'Primitive k=1 versus m=1 duality and the all-even converse are distinct subtargets, retained separately in member targets.',(1,2,1,1),
'This is a family of restriction-classification lemmas, not an assertion that the restrictions are equivalent. Universal conjectures merit plausibility 1; bounded algebra/census merits 3. checks.json supplies M=1 power-of-two failures only, not all-M density.')
cluster('S07','Uniform local-depression floor','ii','Z0671 Z2000',
'Define the joint local-density model F_Q(p) exactly and prove F_Q(p)≥c>0 uniformly over the growing admissible pinning moduli Q in the claimed range.',
'none directly: a refined main-term floor, not a lower bound on actual solutions',2,
'FRONTIER §2.2 RESIDUE_HARDNESS; adjacent to §7.4, but not M_gen itself',
'Accumulation of nonuniform higher-order local corrections; B3/B6 main term versus actual count',
'An explicit density formula would permit Euler-product analysis; multiplying fixed-Q first-order expansions is not a uniform proof.',
'Uniform growing-Q estimate, if true, is stronger than current fitted local factors.',(0,2,1,1),
'Do not assert F is already a proven Euler product with a floor. Source Z2000 itself calls its 1/log p formula a conjectural secondary term. First specify the joint model, then test/prove its bound.')
cluster('S08','Main-term secondary coefficients','ii','Z1760',
'Compute the log p and constant terms of M0(p)=Σ_{coprime u,B;u+B odd;4uB-u-B≤p}1/φ(4uB), with a rigorously justified error term.',
'none directly; improves a calibrated comparison count',2,
'FRONTIER §2.2; no new §7 lower-tail input',
'Hyperbolic boundary shifts affect secondary terms; claimed O(p^-δ) needs proof',
'Mellin/Euler-product expansion gives an accessible double pole; keep the shifted boundary rather than silently replacing it by 4uB≤p.',
'Potential new constants, not new existence mechanism.',(0,2,1,0),
'Plausibility 2, not automatic 3: the leading singularity is straightforward, the strong error and boundary contribution are not supplied.')
cluster('S09','Explicit BM/QNR constants','ii','Z2858 Z2901',
'Give effective numerical p1,c and a least-odd-QNR range T(p) such that p≥p1 implies M_BM(p)≥c log²p and some t≤T(p) has positive BM level mass.',
'none directly; explicit prerequisite/main term only',3,
'FRONTIER §2.2 and §7.3; already proved qualitative BM floor',
'B2 class inside allowed coset remains untouched',
'Explicit Pólya–Vinogradov/Burgess constants and finite verification are available in principle.',
'Effective thresholds only.',(0,2,0,0),
'Do not claim this would make H^- effective; the lower-tail hypothesis is a separate missing theorem.')
cluster('S10','Effective exceptional-set constants','ii','Z2418 Z2551',
'Produce effective c,C,N0 with E_ES(N)≤C N exp(-c(log N)^{3/4}) for N≥N0, handling an exceptional real character rather than hiding ineffectivity.',
'partial: an explicit exceptional-set theorem, not zero exceptions',2,
'FRONTIER §7.12; internal paper/es-threequarter-note.tex',
'Exceptional-modulus loss in sieve supply; Siegel–Walfisz/BV ineffectivity',
'Landau–Page exclusion is a concrete standard repair candidate, subject to checking the supply loss.',
'Effectivity, not a new exponent or pointwise theorem.',(1,2,1,1),
'Source claim that all relevant moduli are polylog or that BMOR alone suffices must be checked against the actual paper. One day should locate the exceptional-modulus deletion lemma, not promise all numerical constants.')
cluster('S11','Almost-all a²+b⁴ values','ii','Z0240',
'Prove #{(a,b):a²+b⁴≤X and ES(a²+b⁴) fails}=o(X^{3/4}/log X), with representation multiplicity handled, hence almost all primes in that thin family are ES-valid.',
'partial: thin-family almost-all result; no prescribed prime',2,
'FRONTIER §7.12 related; not already §7.8 every-exponent result',
'B6; uniform local occupancy for the two-dimensional sieve; thin sets cannot inherit ambient density one for free',
'Polynomial residue counts and a two-dimensional large sieve are concrete tools.',
'Plausible new thin-set restriction theorem.',(1,2,1,1),
'The source plausibility 3 is optimistic until the local character-sum loss and dimension supply are checked. The internal ambient exceptional bound alone is far larger than X^{3/4}.')
cluster('S12','Low moments and concentration calibration','ii','Z2362 Z2432 Z2461 Z1074',
'Prove first/second moment bounds for a specified R or f over primes (or integers), with correct log powers, sufficient for a positive-density lower bound or a quantitative variance theorem.',
'partial: positive density or weak exceptional bound, normally dominated by existing coverage theorems',2,
'FRONTIER §6 fixed-p variance/Dirichlet moments; §7.5 asks for much more',
'B6; large-lcm off-diagonal pairs; rare upper tails',
'Divisor switching can handle some pair correlations; no uniform high-order moment theorem supplied.',
'Sharp second moment could be publishable structure, not ES progress by coverage.',(1,1,0,1),
'Empirical second moments are not known-true theorems. Linnik upper spikes do not themselves rule out good averaged second moments. Positive-density yield and an exact variance law must not be conflated.')
cluster('S13','Average count asymptotics','ii','Z2597 Z2040 Z2481 Z2086',
'Establish a full main-term polynomial for Σ_{n≤N}f(n), or a specified prime/AP count, with justified error; use it to compute conditional count means.',
'partial: sharper average counts and arithmetic-progression means',2,
'FRONTIER §5.1 and §6 Manin/height-count interpretations',
'B6; prime AP asymptotics may need large-modulus divisor switching',
'ET divisor parametrisations give a concrete analytic route; height reinterpretation alone does not add input.',
'New constants/error terms are possible.',(1,1,0,1),
'Z2086 fixed-Q constant fractional depression is not implied by a local correction of order 1/log X; it may vanish asymptotically. Also Σ floor(N/den(P)) is not an exact equivalence of leading constants without a Tauberian/partial-summation argument. Drop those automatic implications.')
cluster('S14','Distribution in progressions','ii','Z2379 Z2400',
'Prove an explicit beyond-1/2 distribution estimate for the relevant weighted prime or ES-count progressions, keeping the moving residue and modulus dependence in the theorem.',
'partial: averaged sieve inputs, not necessarily a better exceptional-set exponent',1,
'FRONTIER §7.12; §6 CRT supply-law cap',
'B6; well-factorable weight hypotheses and moving residue differ from classical BFI; CRT cap may remain',
'Analytic distribution tools exist, but no cited theorem matches the full displayed parameters.',
'Potential parameter-range result, not a named standard conjecture⇒ES implication.',(1,1,0,2),
'Plausibility reduced from 2: establish an admissible estimate first and show the exceptional-set architecture actually needs its range. No automatic saving beyond 3/4.')
cluster('S15','Short-interval solved primes','ii','Z2947 Z2382',
'Combine a uniform interval exceptional bound for the SAME certificate family with a proven lower bound for primes in that interval to ensure at least one solved prime.',
'partial: one solved prime per interval, never every prime',2,
'FRONTIER §5.1 interval bounds; §7.12 adjacent',
'B6; ES versus (★) mismatch; short-interval prime lower bounds in APs require separate inputs',
'Existing interval bounds may prove an ES version; a (★)-only or fixed-840-class version needs its own theorem.',
'Bookkeeping corollary if hypotheses match.',(1,1,0,1),
'Do not label the optional Mordell-class BHP version known-true by citing an unrestricted prime interval theorem. Verify the family and progression uniformly.')
cluster('S16','S-integer positive ES','ii','Z0052 Z0054 Z0297 Z0251',
'For every integer ℓ≥2 and n≥2, prove positive ES over Z[1/ℓ] using an odd-order half-turn of ℓ modulo a Dirichlet prime q≡3 mod4.',
'none for integer ES without exponent-removal transport',3,
'FRONTIER §7.13 adjacent; §6 B-fin transport gap; POWER_LADDER_ES one-mute-prime theorem',
'B-fin finite integer certificate box versus unbounded unit powers',
'Dirichlet and reciprocity provide the needed q and odd k with q|1+ℓ^k; the unit-sum identity is explicit.',
'An elementary simplification of an existing relaxation mechanism.',(0,2,1,0),
'For composite ℓ reduce to rad(ℓ); do not assume every nonsquare integer has the same primitive-character modulus. The theorem remains a ring result; no downward transport follows.')
cluster('S17','Depth-one weighted numerator','ii','Z0053',
'For each odd ℓ≥5 and prime p∤ℓ, find positive integers x,y,z with 4/p=1/x+1/y+ℓ/z and ℓ∤z; settle a specified ℓ≡1 mod4 first.',
'none directly; a relaxation with prescribed third numerator',1,
'FRONTIER §6 power ladder/transport; no numbered §7 problem',
'B-fin; unbounded-power ring proof does not prove exponent-one claim',
'An explicit formula settles ℓ≡3 mod4; no uniform finite cover for ℓ≡1 mod4 is exhibited.',
'Distinct bounded-depth sibling, not automatically covered by flat power ladder.',(0,2,1,2),
'Downgrade source plausibility 3: “finite covering, easy” is not a proof. One counterexample or a genuine cover would be useful calibration.')
cluster('S18','Totally-positive unit mechanism','ii','Z0061 Z0086 Z0062',
'For a specified real quadratic K, determine which totally positive e admit e=1/u+1/v in O_K, and whether suitable units give rational-input ES; start with K=Q(√3) and the mod4 class restriction in Q(√5).',
'none for Z without a transport theorem',2,
'FRONTIER §6 other-ring transport; other_rings Prop 3.3',
'Congruence at one prime ideal is not divisibility by the rational prime ℓ; total positivity in every real embedding',
'Unit groups and finite residue rings are explicit. For split ℓ, η≡-1 at just one prime above ℓ does NOT imply (1+η)/ℓ∈O_K.',
'Potential broader ring classification; no ES-specific integer mechanism.',(0,2,1,1),
'Repair Z0061 before using Chebotarev: require rational divisibility or an algebraic e with a valid mod4 relation for rational n. Q(√5) six-class claim is evidence until proved. General number-field statement is harder than these first cases.')
cluster('S19','Function-field bounded-menu obstruction','ii','Z2579',
'For fixed admissible degree data and sufficiently large finite field size q, instantiate the finite polynomial system behind a specified bounded-menu obstruction using a proved function-field prime-tuple theorem.',
'none for Z; proves a model obstruction unconditionally in a different limit',2,
'FRONTIER §7.10 adjacent, not the fixed F3[T] sterility question',
'Separability, admissibility, characteristic exceptions and order of limits q→∞ versus degree→∞',
'Large-q prime-tuple theorems can replace H only after their exact hypotheses are verified.',
'Unconditional model of a conditional barrier.',(0,2,1,1),
'Do not present this as an unconditional integer theorem, or as the fixed-q F3[T] result. Handling 6402 polynomials is more than one routine substitution.')
cluster('S20','Function-field counts and short words','ii','Z2598 Z2483 Z0022',
'In a fixed, explicitly chosen F_q[T] model, determine short-word solvability and average counts of bounded-degree sections; state degree, characteristic, positivity surrogate and order of limits.',
'none for Z without a sharp transfer',1,
'FRONTIER §7.10 related but not identical; §6 function-field transfer gap',
'Characteristic can remove T1; bounded CF digits do not imply length≤3; a circle method needs enough variables',
'Finite-degree experiments and polynomial parametrisations are concrete, but the quoted general theorems do not yet match the model.',
'Sibling calibration only.',(0,1,1,2),
'These are model subtargets, not equivalent theorems; an average curve count cannot prove every irreducible has a short word. The source known-true label for section counts is unsupported without an actual formula/hypotheses.')
cluster('S21','I3 exponential covering','ii','Z2776',
'Prove I3 for all members of one new family 3^k±2 or 5·3^k+1 beyond explicitly checked exceptions, by a verified finite cover of the exponent.',
'none directly unless certificates satisfy the ES coordinate restriction',3,
'FRONTIER §7.17; existing I3 exponential families',
'Class-free I3 does not imply ES; small k may need exceptions',
'Existing exponent-cover machinery is a direct reusable handle.',
'New sibling families, not new pointwise ES input.',(0,2,1,0),
'Keep t,u,v≥3 and verify all base cases; small values can fail trivially. Record the certificate coordinate if claiming any ES consequence.')
cluster('S22','Numerator-nine complete exception list','ii','Z0735',
'Prove 9/n has a three-unit-fraction representation for every n≥20, with explicit verification of exceptions 2,5,11,19 for n≥2.',
'none for numerator 4; a complete sibling theorem if achieved',1,
'FRONTIER §7.15 numerator calibration; no dedicated §7 problem',
'Absence of T1 does not imply existence of a finite cover (5/n warns against this); coverage search can stall',
'Bounded identity search is concrete and may find a cover, but no cover or proof of coverability is supplied.',
'Potential complete numerator classification, not evidence B1 is exactly T1.',(0,2,2,2),
'Downgrade plausibility 2 to 1 for the universal theorem, retain a cheap falsification/cover-search task. No sterile point found is not equivalent to a finite covering.')
cluster('S23','Long-chain character sign rule','ii','Z2782',
'Derive the exact quadratic-character sign of a chain lattice/HJ word from its characteristic covector and signature, for length≥4 as well as the known three-slot case.',
'none directly; a dictionary/sign-calibration theorem',2,
'FRONTIER §7.11 adjacent; §6 lattice/HJ dictionary alone does not force existence',
'Correct quadratic refinement and parity conventions; naive coordinate mod4 rule fails at length4',
'van der Blij/Gauss-sum formulas give an explicit algebraic handle.',
'Long-word bookkeeping may be new; three-word equivalence is not.',(0,2,1,0),
'Do not classify the side sign theorem as circular merely because short-word existence is ES-strength. Specify the lattice parity conditions before enumerating 512 cells.')
cluster('S24','Triangle sandpile relaxation','ii','Z2652 Z2851',
'Construct, for every sufficiently large p≡1 mod4, a triangle multigraph with ab+bc+ca=p and a nonsquare sandpile pairing, under an explicit least-prime-in-coset bound; handle remaining primes separately.',
'none without transport from triangles to the ES fan shape',2,
'FRONTIER §6 B-fin; analogous to ES-square relaxation',
'Existence of q≡3 mod4 with (q/p)=-1 below √(2p); graph vertex count is not fan shape',
'The displayed triangle formula is constructive conditional on q; GRH supplies a polylog q for large p.',
'Useful graph analogue, but unconditional all-p status is not established in the source.',(0,2,1,1),
'Source known-true conflates a GRH asymptotic, a finite census and an unverified unconditional coset bound. Mark CONDITIONAL on that bound (or GRH), with finite exceptions not automatically covered.')
cluster('S25','Sibling geometry and non-BM failures','ii','Z2626 Z2687 Z2799',
'For one specified sibling (S_{n,-4}, coefficient A2 cluster fibre, or G4 short-word model), identify the arithmetic surface and local/BM invariants before testing whether its observed failures are explained.',
'none directly; calibration of genuine versus lottery-type obstructions',2,
'FRONTIER §7.15; §6 BM geometry',
'An apparent cluster/Hecke dictionary need not preserve integrality or positivity; non-density is not nonexistence',
'Explicit equations and low-count failure lists permit finite symbolic/local computations.',
'Potentially useful near-neighbour models; three distinct model instances, not an equivalence.',(0,2,1,1),
'Stop at an exact identification or explicit obstruction; do not infer ES truth from a sibling having no newly found invariant.')
cluster('S26','Identity/curve classification and discovery','ii',
'Z2352 Z2616 Z1296 Z1586 Z1583 Z1798',
'At a stated degree and parameter class, classify or construct rational/polynomial ES identity families, distinguishing linear p, positive-definite quadratic parameters, Type I versus Type II, and nonconstant levels.',
'partial: new explicit families/classes; finite universal cover remains obstructed',2,
'FRONTIER §7.8 adjacent; §6 B1 only in its proved scope; ident_form_families §§3–6',
'B1 finite universal coverage; conditional Gaussian trap for t²+1; nonconstant Type I remains unclassified',
'Coefficient equations and symbolic identity checking are concrete. A square class mod840 alone is not a no-go: checks.json supplies an identity on n=5881 mod9240.',
'Audit restores actual partial-family work; general classification is not already known.',(1,2,1,1),
'Sources Z2352/Z2616 label stronger classification known-true while admitting it is not done. No blanket extension from positive-definite quadratic Type II to every bivariate Type I family. Bounded discovery plausibility3; full classification plausibility1–2.')
cluster('S27','Witness-scale lower bounds','ii','Z0652',
'For a specified witness coordinate, improve the infinitely-often lower bound toward exp((log p)^{1/3-o(1)}) by sharpening Haar survival and proving the prime transfer with the correct energy hypothesis.',
'none directly; sharper obstruction-side quantitative theorem',1,
'FRONTIER §7.2; H4_NOT_POLYLOG and POINTWISE_OMEGA13',
'Coordinate definitions differ; current Haar upper/lower estimates are far apart; transfer costs matter',
'Existing energy architecture is explicit, but a sharper Haar survival theorem is missing.',
'Possible barrier exponent improvement, not a proof mechanism.',(0,1,1,2),
'Do not transfer the heuristic exponent 1/3 between least modulus, endpoint and menu size without a theorem. This is not a cheap numerical fit.')
cluster('S28','Divisor-in-progression algorithms','ii','Z1212',
'Instantiate a verified Lenstra/Coppersmith divisor-in-AP algorithm for N=4Cp+1, modulus 4C in its proved large-modulus range, and validate the count/range constants.',
'none for universal existence; faster finite certificates',3,
'FRONTIER §6 B2 finite search remains',
'Upper bounds and algorithms do not guarantee a target divisor exists',
'Published fixed-dimension lattice algorithms may speed large-level enumeration.',
'Engineering/literature-validation payoff only.',(0,1,0,0),
'The source explicitly did not reverify its strongest N^{1/4} threshold; do so before implementing or quoting it as a theorem.')
cluster('S29','Unified local-hardness regression','ii',
'Z0728 Z0515 Z0737 Z0824 Z0836 Z0900 Z0215 Z0275 Z0634 Z0697 Z0727 Z0917 Z0918 Z0968 Z1999 Z0686 Z2981 Z0808 Z0773',
'With a fixed definition of the local-density model and held-out matched-size/residue cells, test whether proposed extra features improve predicted count means/zero rates beyond existing F and BM factors.',
'none directly; EVIDENCE about models and informative hard test cases',3,
'FRONTIER §2.2 RESIDUE_HARDNESS and BM_LVALUE; §7.15 calibration',
'B6; overfitting, local/global confounding; subgroup model omits bounded-exponent failures',
'Existing count data and explicit local factors permit a disciplined residual test.',
'Possible model corrections (including inverted practical-p-1 ranking), not an independent positivity theorem.',(0,2,0,0),
'These are variants of the same conditional-mean/model comparison, not proofs of their fitted causes. Z0634 subgroup membership is only necessary. Z0808/Z0773 are legitimate measurements, wrongly labelled circular; neither justifies a uniform count floor.')
cluster('S30','Exact local-density formulas','ii',
'Z0282 Z1310 Z1311 Z2494 Z2566 Z2863',
'Compute a specified local p-adic or 2-adic density of ES solutions/words by valuation strata and Hensel lifting, with a rational expression and explicit singular cases.',
'none directly; local main-term data',3,
'FRONTIER §2.2; §6 local/BM data do not force global points',
'T1/global class not captured by naive local product; integrality and coprimality conventions',
'Finite residue counts plus lifting can prove an exact density once the polynomial and strata are specified.',
'Potential extra local constants; source Z1311 names no polynomial and needs a definition first.',(0,1,0,0),
'Known local solubility does not prove every claimed formula. The hard task is specification and singular lifting, not empirical counts alone.')
cluster('S31','Certificate-shape distribution','ii',
'Z3188 Z2523 Z3068 Z1762 Z0500',
'For a specified certificate measure (all witnesses versus minimal witness), derive or test its average log-coordinate/local-residue distribution and compare against the hyperbolic density model.',
'none directly; witness-location calibration or an averaged theorem',2,
'FRONTIER §7.2 and §6 B6',
'B6; minimal witnesses are biased order statistics, not samples from the all-witness measure',
'Explicit 1/φ weights and existing enumerators provide a model; a proof requires joint distribution estimates.',
'New shape statistics possible, not pointwise control.',(0,1,0,1),
'Unweighted C_min mod m need not equidistribute (C_min=1 has positive mass). Z3188 should be restated with the actual limiting distribution, not uniformity. Murmurations are not an additional theorem without a trace-family model.')
cluster('S32','Upper-tail extremal order','ii','Z0710',
'Bound max_{n≤X}U(n) above and below on the exp(c log X/log log X) scale, separating a proved order-of-magnitude exponent from an exact constant.',
'none for ES lower-tail positivity',2,
'FRONTIER §2.2 upper-tail Linnik construction',
'Exact constant is not supplied by matching rough divisor bounds',
'Linnik constructions and divisor estimates are concrete.',
'Potential extremal-count refinement only.',(0,1,0,1),
'Downgrade the source exact-c known-true claim: its stated upper/lower arguments do not establish a common limiting constant.')

# (iii): no presently specified useful bridge, invalid targets, or already-known dictionaries.
cluster('R01','Exact lower-tail/SQ targets without input','iii','Z1891 Z0604 Z1426 Z0771 Z2681',
'Eventual positivity or a quantitative count floor for an ES-implying family; SQ additionally asserts a classification of composite zero counts.',
'full if the new positivity theorem is proved, but none from the supplied main terms/dictionaries',1,
'FRONTIER §2.4, §7.14/§7.17; §5.5 coprime SQ repair',
'B2 and B6; composite Type-I/II coprimality conventions; no standard conjecture supplies the lower tail',
'None beyond already-proved main terms and target equivalences.',
'No new theorem input.',(3,0,0,3),
'Z0604 known-true applies only to its main term, not the circle-method lower bound. Z1426 composite square-only statement must respect the documented 105,345,561,5985 counterexamples for coprime categories. Plain I3 does not imply ES.')
cluster('R02','Geometric/torsor dictionaries','iii',
'Z0603 Z1670 Z2029 Z2302 Z2699 Z2700 Z2708 Z2894 Z2645',
'Construct an integral positive point on the ES torsor/fibration at every prime; the known geometric equivalences and local/BM information do not supply existence.',
'full if the missing integral-point theorem holds; current dictionary yields none',1,
'FRONTIER §6 torsors, BM, fibrations; §7.3 remaining divisor class',
'B2 integral fibre, no BM obstruction, T1; HIT concerns rational finite covers rather than factorisation of one integer',
'No new homogeneous action, integral Hasse principle or certificate-producing cover is specified.',
'No new ingredient; Z2645 broad no-go is withdrawn but no actual cover appears.',(3,0,0,3),
'Known-true labels here belong to dictionaries, not ES. Under x=nX, an integer ES point maps to rational coordinates with denominators dividing n, but positivity/nonzero conditions remain; a geometric isomorphism over Q loses precisely that integral constraint.')
cluster('R03','Unspecified norm/Selmer existence bridge','iii','Z2922 Z0424 Z1649',
'Specify an order/norm form, abelian variety, or arithmetic module attached to p with a provable existence/nontriviality theorem AND an integral positive map to certificates.',
'full if such an object and bridge are found',1,
'FRONTIER §6 quaternion/genus and class-group dictionaries; related §7.2/§7.3',
'B2 integral side conditions, T1, rational points need not give positive integral points',
'None: no order, curve or module is actually defined that has the required bridge.',
'Audit removes an unjustified universal impossibility claim, not a mathematical gap.',(3,0,0,3),
'Keep in the rest rather than deleting: exact norm existence is not universally forbidden by B3. But naming a class-number-one order or root number is not yet a research theorem statement.')
cluster('R04','Ring/matrix relaxation transport','iii','Z0091 Z0338 Z0084',
'Prove a concrete integrality-preserving positive projection from Gaussian-cone or matrix reciprocal solutions to three positive integer unit fractions.',
'full if existence in the relaxation and transport are both proved; none currently',1,
'FRONTIER §6 other-ring transfer/B-fin',
'Norms not additive; traces produce variable numerators; positive-definite matrix inverse entries not unit fractions',
'No projection avoids a new divisibility condition. Trace/norm maps give explicit failed candidates, not a no-go for every map.',
'No new usable transport.',(3,0,0,3),
'A constant map chosen from an already-known ES solution is vacuous. Both ring existence and a genuinely constructive projection are needed.')
cluster('R05','Power-size lifts and short-interval amplification','iii','Z2928 Z2060 Z2982',
'Build an independent high-multiplicity detector or amplifier with a pointwise error below its main term after division by fibre size, rather than multiplying an unknown certificate count by a large factor.',
'full if the independent estimate holds; none from rescaling',1,
'FRONTIER §7.1 adjacent; §6 B3 and fixed-p variance',
'B3 fibre cancellation; B6 tiny-interval variance not available; two-sided polylog errors can be false',
'High-multiplicity encodings formally escape one B3 hypothesis, but no independent analytic estimate is provided.',
'No actual lift with a new count theorem.',(3,0,0,3),
'Z2982 includes the n=p summand: its bound already gives |R(p)-M(p)|≤M(p)/√2, an inadmissible global two-sided polylog target in the stated form. A one-sided amplifier would need a different inequality.')
cluster('R06','Stability and zero-temperature nonvanishing','iii','Z3103 Z3104 Z1325',
'Construct class-sensitive interlacing/partition polynomials with a uniform positive certificate-coefficient bound, not merely real-rootedness or nonvanishing at finite temperature.',
'full only with that new coefficient bound; current mechanisms yield none',1,
'FRONTIER §6 interlacing/stable displayed mechanisms fail, general variants remain open',
'T1; residue extraction destroys stability; zero-free functions can tend to zero',
'No new common interlacer; group-algebra stability is an unconstructed variant.',
'Audit exposes the exp(-β) counterexample to the zero-free⇒positive-limit inference.',(3,0,0,3),
'Do not infer nonexistence of every conceivable stable encoding. Existing counterexamples refute displayed projections, while zero-temperature positivity is the target itself.')
cluster('R07','Subgroup, smoothness and primitive-divisor forcing','iii',
'Z2426 Z0250 Z1954 Z0378 Z0258 Z0254 Z1715',
'Give an explicit auxiliary factorisation mechanism whose bounded subproducts hit the ES class, with all required valuations and target divisibilities verified.',
'full if a universal mechanism is found; known auxiliary facts alone yield none',1,
'FRONTIER §7.3/§7.13; §6 reciprocity, B4 and polynomial budgets',
'B2 class versus subgroup; B4 opaque large factors; primitive divisor rank usually yields ±1, not the required sign',
'Lucas rank can reduce a class to ±1, but no construction forces 4Cp+1 to contain the right primitive divisor. Binomial valuations do not force division of p+u.',
'E2 non-polynomial primitives and Lucas rank are genuine formal escape possibilities, not actual transfers.',(3,1,1,3),
'Z2426 D·D^-1 must enforce ab|N, not independent divisors with combined exponents exceeding N. The C=1 Lucas example gives a tautological sign. Z0254 generating all identities does not prove membership for a given prime.')
cluster('R08','Scale/digit induction without an invariant','iii','Z3005 Z0482',
'Specify a growing-length digit/scale recursion with an invariant implying eventual certificate output for every prime and a valid termination proof.',
'full if defined and proved',1,
'FRONTIER §3 B1 escape E1/E2; no dedicated §7 target',
'T1; privacy limits pooling; finite-state assumptions cannot silently replace a general recursive algorithm',
'Growing length is outside fixed formal runs, but neither an invariant nor a transition rule is given.',
'Scale induction is new packaging only.',(3,0,1,3),
'Z0482 Cobham argument is not a universal no-go: a set containing all squares need not equal the squares; unbounded-state digit algorithms need not be automatic. Retain the open scope but no lane until a rule is specified.')
cluster('R09','Abstract limit-measure rigidity','iii','Z2978',
'Define an ambient candidate measure even when no certificate exists and prove rigidity of all its prime-subsequence limits strong enough to force a certificate at finite p.',
'full only with a new quantitative extraction theorem',1,
'FRONTIER §6 B1/ultraproduct limitations',
'Residue-only measures have square-mimicking Dirichlet subsequences; weak convergence need not detect a vanishingly sparse target',
'No new measure or entropy/recurrence input.',
'Audit separates a false residue-Haar claim from unexcluded alternative measures.',(3,0,0,3),
'Even a correct limiting Haar theorem needs quantitative control at the shrinking certificate scale. Merely excluding a hypothetical infinite failure subsequence is not an independently proved rigidity result.')
cluster('R10','Density/mass tools without three-term recovery','iii',
'Z1262 Z1646 Z2446 Z2716',
'Provide a theorem that forces the prescribed three-term target in a sparse p-tied denominator set, rather than an arbitrary configuration or an unbounded-length reciprocal sum.',
'full only with a new sparse three-term theorem; named inputs do not yield it',1,
'FRONTIER §6 additive-density/spectral scale limitations; B2_ACROSS_FIELDS M1/M4',
'B3 sparse output, B6 average versus specified p; number-of-terms loss',
'No theorem in the candidate layer bridges these hypotheses. Direct Bloom/PP applications miss the target; a new structured lemma is not universally forbidden.',
'Audit restores scope but finds no concrete lemma.',(3,0,0,3),
'Z2716 product-size argument must use |AB|≥max(|A|,|B|), not |A||B|. Typical subpower output still blocks universal power-size input sets. Moment variants are separately retained in S12, not treated as full proofs.')
cluster('R11','Long-word or extra-term collapse','iii','Z0476 Z2027 Z1944',
'Construct a positive integral map collapsing long HJ words or ≥4-term Egyptian fractions to an ES three-term certificate at the same p.',
'full only with a new collapse theorem; relaxations alone yield none',1,
'FRONTIER §6 Zaremba length and B-fin transport',
'B2 on last merge, B3 sparse short-word set; extra freedom is lost in collapse',
'No collapse rule. Existing relaxation existence is not evidence that the final merge is easy.',
'No new bridge.',(3,0,0,3),
'The source phrase “no collapse exists” should read “none is known/supplied.” A finite failure of a particular merge does not settle arbitrary transport.')
cluster('R12','Already-known average coverage','iii',
'Z2372 Z2650 Z0567 Z0554 Z2490 Z2575 Z3164 Z2458 Z2601',
'Prove density-one or positive-density coverage by the stated restricted search; compare rigorously with the existing ES and subfamily exceptional-set bounds.',
'partial at best, normally weaker than current theorems; restricted subfamily versions may still be unproved',2,
'FRONTIER §5.1; §6 B6',
'B6; quantitative denominator caps/restricted prime levels require their own bounds',
'Known sieves suffice for some versions, not automatically all restrictions.',
'No identified improvement over the standing frontier.',(1,0,0,2),
'Z2372 confuses O(p²) certificate moduli with a uniform O(p²) bound on all denominators; a genuine height theorem is needed. Z3164 prime-C almost-all claim needs a proof, not just invoking CRT. Density inheritance into a restricted family is not automatic.')
cluster('R13','Necessary/local tests already free','iii','Z1316 Z0081 Z1493 Z2989 Z1048 Z0730',
'Use local solubility, a positive class-free count, or one QNR factor as an ES precursor, then prove the currently missing divisor-class or integral lifting step.',
'none from these precursors alone',3,
'FRONTIER §7.3/§7.17; §6 genus and least-QNR-root limits',
'T1 and B2; local/character information does not determine the full divisor class',
'No new lifting theorem; precursor statements are known in scoped forms.',
'No new ingredient.',(0,0,0,1),
'Z1316 claimed coverage of EVERY interval of length q^{1/2+ε} by three inverse sums does not follow from no local obstruction; check the precise incomplete-Kloosterman error threshold. Z1048 counterexamples concern a specified least-QNR root, not every function of the QNR.')
cluster('R14','Finite or diagnostic-only tasks','iii','Z0758 Z1084 Z3134 Z2522 Z2316',
'Perform a bounded census, classify sibling failures, or count primes inside a fixed sparse family; none of these tasks contains a mechanism for every p.',
'none for full ES; finite certificates/model information or unrelated prime-production theorems',2,
'FRONTIER §7.15/§7.17 related; §6 thin-family transfer and local/average limits',
'B1 finite verification, B6 averages; primes in a thin sequence can be a famous open problem',
'Finite computation is available; no new global implication.',
'Diagnostics may correct data, not a priority proof component.',(0,1,0,1),
'Z0758 smooth-n explanation is a conjectural model, not a classification. Z2522 Sato–Tate does not prove cross-box cancellation. Z2316 growing menus are not refuted by sparsity of a fixed list, but no growing coverage mechanism is provided.')
cluster('R15','Weak Fermat identity loses the class','iii','Z1956',
'Correct the Fermat conversion to require X-Y≡X+Y≡-1 mod4C as well as X²-Y²=4Cp+1 and positive factors.',
'none beyond the exact (★) reformulation',0,
'FRONTIER §2.1; QUATERNION_ES split binary dictionary',
'B2; source weaker X≡-1 mod2C is insufficient',
'None; X=2p+1,Y=2p always satisfies the weak C=1 condition.',
'Audit correction, not a revived avenue.',(0,1,0,0),
'CERTIFIED counterexample p=409 is in checks.json. This overturned verdict contributes to classification-error rate, not to the count of promising rescued methods.')
cluster('R16','Linear-height distinct-term cap is false','iii','Z0138',
'For fixed C, seek four DISTINCT positive denominators ≤Cp representing 4/p at every large prime.',
'none: false at this height scale',0,
'FRONTIER B3/height-scale related; source elementary p-adic obstruction',
'For p large relative to C, denominators divisible by p are pa_i with a_i≤C; their reciprocal sum must equal4 after multiplying by p, impossible with distinct positive a_i and only four terms.',
'No escape without raising the height cap or changing distinctness/term count.',
'A useful false-target calibration only.',(0,1,0,0),
'Do not transfer this four-distinct-term obstruction to unrestricted four-term or ordinary three-term representations with larger denominators.')
cluster('R17','Maynard with a distinguished prime','iii','Z1818',
'For each m, prove there exist fixed admissible C_1,…,C_k and infinitely many PRIME p for which at least m of 4C_i p+1 are prime.',
'none directly; obstruction-side calibration if proved',1,
'FRONTIER §6 fixed-menu/H obstruction; not a known unconditional consequence as stated',
'Maynard guarantees many primes among forms, not primality of a separately distinguished base form p',
'No argument forcing the base variable to be prime is supplied.',
'An unsupported known-true claim, not a bankable corollary.',(0,1,1,2),
'Downgrade to unclear/conditional on an appropriate prime-tuple input. One cannot silently replace “many prime forms at integer n” by “many forms at prime n.”')
cluster('R18','Weak-arithmetic and partition-regularity meta-questions','iii','Z0189 Z0135',
'Independently settle the specified meta-property: an actual IOpen model with an ES counterexample, or partition regularity of 1/x+1/y+1/z=4/w.',
'none for standard integer ES',1,
'No FRONTIER §7 item; §6 bounded-polynomial proof obstructions are related only to the logic question',
'Z[T] need not model IOpen; coefficient extensions can invalidate Mordell obstruction; varying w in a colouring theorem is not prescribed p',
'No valid IOpen countermodel or applicable partition-regularity theorem is exhibited.',
'Distinct meta-questions sharing zero ES yield, retained as separate member targets.',(0,1,1,2),
'The claim that a weak-arithmetic countermodel means “any ES proof needs non-open induction” requires formalization; it is not automatic from failure of polynomial identities. A colouring of degenerate solutions is not a colouring of all solutions.')


cluster('A18','Self-levelled theta reciprocity','i','Z0416',
'Prove Question R/restricted Hypothesis TG for self-levelled SL2 words, then separately show its allowed sporadics contain no prime beyond an effective threshold.',
'partial for reciprocity alone; full only with the additional existence and prime-exclusion theorem',1,
'FRONTIER §7.11; §6 theta normal forms do not decide coefficients',
'B2 class in self-levelled word; T1 exact reciprocity is not existence',
'An exact SL2/theta dictionary exists; no new prime-exclusion input.',
'Existing named open problem, not a new ingredient.',(3,1,0,3),
'Do not identify observed U sporadics with a proved theta-sporadic set. Reciprocity must be stated independently of the desired ES conclusion.')
cluster('S33','Cap-relaxation transference constants','ii','Z2797',
'Under Hypothesis W, improve the covering-radius/dual-minimum constants or exponent in the known cap bound, with exact dimension dependence.',
'none for cap0; a conditional improvement for a relaxation',2,
'FRONTIER §7.13; BALANCED_LATTICE',
'B-fin; bounded positive cap is not integer ES; W is nonstandard',
'Reverse-Minkowski/transference inequalities may improve the geometry constants, not the class event.',
'Possible conditional constants only.',(0,1,0,1),
'First determine whether the new inequality changes an exponent or only a fixed factor. Neither removes the independent W hypothesis.')
cluster('R19','Finite QNR-class identity covering','iii','Z1840',
'For every fixed q, cover all primes with (q/p)=-1 by finitely many ET identities; distinguish this from the unrestricted implication (q/p)=-1⇒ES(p).',
'none for the stated universal finite-cover architecture; unrestricted implication remains open',0,
'FRONTIER §7.9 sterile r-generic points and §6 B1',
'Sterile r-generic points exclude the finite-cover proposal for large r; they do not refute ES in those classes',
'No ingredient beyond reciprocity and fixed congruence data.',
'Audit scope correction, not a new proof method.',(0,1,0,0),
'The r≤13 least-QNR coverings are not a theorem that every independent q-nonresidue class is finitely coverable. Keep those quantifiers distinct.')

# Split unrelated side theorems rather than pretending that a shared mathematical
# vocabulary makes them equivalent. Remaining siblings are scoped versions of
# a common target and their differences are stated explicitly above.
def split(source, cid, mids, name, statement, assessment):
    parent = next(c for c in CLUSTERS if c['id']==source)
    child = dict(parent)
    chosen = mids.split()
    assert set(chosen) < set(parent['members'])
    parent['members'] = [m for m in parent['members'] if m not in chosen]
    child.update(id=cid, members=chosen, name=name, clean_statement=statement, assessment=assessment)
    CLUSTERS.append(child)

split('S06','S34','Z0866','Primitive Type-II line',
'For every p>p0 prime, find coprime a,b and m|(a+b) with p=4ab-(a+b)/m; first prove the primitive-solution parametrisation and audit its failures.',
'The universal statement is a genuine strengthening, plausibility1; the finite algebra/census is plausibility3. It is not equivalent to all-even or allowed-residue ES. The exact primitive criterion gives a useful restricted model.')
split('S06','S35','Z0212','All-even converse',
'For every prime p, existence of an ES solution with one denominator divisible by4 implies existence of an all-even ES solution.',
'The easy reverse implication follows from the 2-adic maximum appearing twice. The converse is a separate transport conjecture; local valuations do not prove it. No uniform conversion is supplied.')
split('S06','S36','Z1942','Power-of-two denominator restrictions',
'For each fixed M, determine whether infinitely many primes fail to have any denominator 2^k m with m|M; start with exact M=1 failures.',
'checks.json certifies M=1 failures. The all-M infinitely-often theorem is not proved by B1 because k grows with p; positive-density claims need a separate counting argument.')
next(c for c in CLUSTERS if c['id']=='S06').update(name='Allowed-residue denominator restrictions', clean_statement='Classify local obstructions for denominators in a specified residue set S mod q, then test global failure sets with a complete bounded enumerator.')
split('S18','S37','Z0062','Q(sqrt5) unit-sum residue classes',
'For totally positive integers u,v in Q(√5), prove that odd e=1/u+1/v lies in the six ±square classes mod4, and determine which classes are attained.',
'A concrete local/global unit-sum classification, distinct from universal existence over arbitrary fields. The source reports finite-box evidence, not a proof; total positivity and integrality of e are essential.')
split('S20','S38','Z0022','Function-field length-three target',
'In a specified F_q[T] ES model, determine whether every sufficiently large-degree irreducible has a certificate with Artin/HJ length≤3 and the appropriate sign condition.',
'Bounded digits or ordinary function-field Zaremba do not imply bounded length. A small-degree computation is diagnostic only; characteristic and the sign surrogate must be fixed first.')
split('S20','S39','Z2483','Function-field section counts',
'For a fixed degree d and explicitly chosen ES total-space compactification over F_q(t), compute the dimension/count of polynomial sections with the required integrality conditions.',
'This is a section-count theorem, not an average over target irreducibles. No result in the source proves the claimed universal count; quoted circle-method/free-curve hypotheses must be checked.')
next(c for c in CLUSTERS if c['id']=='S20').update(name='Function-field average count', clean_statement='For a fixed F_q[T] ES model, prove an asymptotic for the number of certificates summed over degree-n irreducibles, with explicit main term and error in a stated limit.')
split('S25','S40','Z2687','Cluster-fibre geometric identification',
'Identify the coefficient-N ES5 frieze fibre with a specified twisted A2 log-K3/degree-five-del-Pezzo-complement model, or exhibit the precise boundary/integrality mismatch.',
'The identification is a bounded symbolic task. Harpaz non-density is not a pointwise existence theorem; even an exact variety isomorphism needs an integral-model comparison.')
split('S25','S41','Z2799','Hecke-G4 short-word sibling',
'Define G4 length-three words with cusp entry p and a precise quadratic-character surrogate, then derive their square-obstruction law and classify finite nonsquare failures.',
'This is a new sibling definition/sign calculation, not a theorem about the ES surface. Arithmetic versus nonarithmetic Hecke groups do not by themselves settle existence.')
next(c for c in CLUSTERS if c['id']=='S25').update(name='Negative-deformation BM failures', clean_statement='Evaluate the relevant Brauer classes on S_{n,-4} at its six recorded failing n, or prove those classes do not obstruct its positive integral adelic set.')
split('R18','R20','Z0135','Partition regularity of reciprocal ES equation',
'Determine whether every finite colouring of N has monochromatic x,y,z,w with 1/x+1/y+1/z=4/w.',
'This existential w is not a prescribed prime. Nonregularity of x+y+z=4w only blocks the quoted transfer theorem; a colouring that kills (3k,3k,3k,4k) does not kill all solutions.')
next(c for c in CLUSTERS if c['id']=='R18').update(name='Open-induction countermodel', clean_statement='Construct an actual model of IOpen containing an n≥2 without positive ES denominators, with a proof that the polynomial obstruction survives its coefficient field.')


def main():
    rows = [json.loads(l) for l in (OUT/'F.jsonl').read_text().splitlines()]
    by_mid = {r['mid']:r for r in rows}
    seen = {}
    for c in CLUSTERS:
        for mid in c['members']:
            if mid in seen:
                raise AssertionError(f'duplicate member {mid}: {seen[mid]}, {c["id"]}')
            assert mid in by_mid, mid
            seen[mid] = c['id']
        c['member_target_scope'] = 'Shared output theorem or expressly scoped specializations; not an assertion of logical equivalence. Original individual statements are preserved in F.jsonl.'
        c['audit_rescues'] = [m for m in c['members'] if by_mid[m]['audit_rescue']]
    missing = sorted(set(by_mid)-set(seen))
    assert not missing, f'unassigned candidates: {missing}'
    ranked = sorted(CLUSTERS, key=lambda c: ({'i':0,'ii':1,'iii':2}[c['band']], -c['proof_priority_score'], c['id']))
    for band in ['i','ii','iii']:
        for i,c in enumerate([c for c in ranked if c['band']==band],1):
            c['rank_in_band'] = i
    payload = dict(reviewer='A', label='Assessment', ES_status='OPEN',
        candidate_count=len(rows), cluster_count=len(ranked),
        scoring=dict(formula='5R + 2H + 2I + N - 3G; rank within bands, never as a probability',
            R='proof relevance: 3 potential full pointwise conclusion, 2 frontier-changing partial theorem, 1 ordinary partial theorem, 0 no ES implication',
            H='plausibility 0–3 of the clean theorem with current/foreseeable tools, not inherited from source',
            I='one-day information gain: 0 slogan/no discriminating test, 1 bounded diagnostic, 2 clear falsifier or first lemma',
            N='new mechanism relative to FRONTIER: 0 existing, 1 variant/audit repair, 2 genuinely distinct',
            G='unsupported bridge burden: 0 direct algebra/known theorem, 1 one difficult named step, 2 several gaps, 3 object/mechanism not defined or global bridge absent',
            caveat='Ordinal expected-proof-value proxy, not calibrated success odds; bands separate proof components from side work and rest. High relevance does not mean a viable proof.'),
        clusters=ranked)
    (OUT/'clusters.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('partition:',len(rows),'candidates,',len(ranked),'clusters')
    for band in ['i','ii','iii']:
        print(band,[(c['id'],c['proof_priority_score'],len(c['members'])) for c in ranked if c['band']==band])


if __name__ == '__main__':
    main()
