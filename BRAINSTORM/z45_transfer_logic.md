# z45_transfer_logic — transfer, nonstandard primes, and the information in an exception

## 0. Summary

**Assessment.** The proposed large-q bridge starts from a false premise for the campaign's actual monic, no-cancellation ES analogue: at fixed numerator degree k ≥ 1 and denominator degree d > k, the proportion of solvable irreducibles is O_d(q^(−k)), not 1. The previously proved characteristic-≥5 statement extends to every characteristic with the campaign's NC convention. A new elementary degree-two classification makes the reversal explicit: solvable inputs lie on five coefficient curves. Weil does prove the *mute* variant at each fixed P, but by allowing infinitely many shots and dropping the growing integrality modulus; it does not prove cap 0. Ax–Kochen transfers local valued-field sentences, not this global integral/sign problem. There is a rigorous complexity statement: Vaughan's exceptional-set theorem gives every hypothetical L-bit ES-exception the bound K(p | L) ≤ L − cL^(2/3) + O(1). This is enumeration compression, not an arithmetic explanation or a contradiction. Overspill gives a nonstandard initial interval of verified inputs, never verification at an arbitrary nonstandard counterexample.

**Verdict: PARTIAL — exact missing implication is fixed-input, cap-0 divisor-class nonemptiness (B2), or a genuinely arithmetic inverse theorem beyond enumeration compression. Promise: 1/5 for ES.** The displayed Ax–Kochen shortcut and the large-q universal premise collapse; model theory and function-field methods as whole fields are not ruled out.

**Assessment — prior coverage / novelty.** Read FRONTIER §§2–7, the brainstorm index, `FUNCTIONFIELD_ES*.md`, the relevant `FF_*` theorem statements/proofs, `DRINFELD_ES.md`, all four `BRAINSTORM/logic_*.md`, `padic_functionfield_igusa.md`, `noncounting_shapes.md`, and their errata. Repository searches for ultraproduct, overspill, Ax–Kochen, pseudofinite, Kolmogorov and fixed degree locate substantial prior coverage of transfer and nonstandard *profinite* points. In particular, the large-q negative theorem is already `BRAINSTORM/ff_erdos_straus.md` Thm 2.1; it is not new here. The all-characteristic NC extension, explicit five-curve quadratic calculation, and the Vaughan-to-conditional-complexity corollary were not found in the searched prior files. The latter is a standard coding argument, not a new complexity theorem. No claim of external priority.

## 1. Precise dictionary and theorem inventory

### 1.1 The two predicates are different

**Definition.** Write ES_Z(m,n) for positive integral solutions of mxyz = n(xy+xz+yz). ES is ∀n ≥ 2 ES_Z(4,n). For prime P ∈ F_q[T], monic A of degree k ≥ 1, and d = deg P > k, the campaign's ES_q(A,P) asks for **monic polynomial** X,Y,Z satisfying

    AXYZ = P(XY+XZ+YZ),    min(deg X,deg Y,deg Z) ≥ d−k.       (NC)

The latter condition is part of the definition, not an ordered-field positivity condition. It is automatic at prime P in odd characteristic (`FUNCTIONFIELD_ES.md` Lemma 1.2); in characteristic 2 it matters.

**PROVED — exact common divisor dictionary.** At an integer prime, the (★) subfamily is

    R(p) = Σ_C #{D | 4Cp+1 : D ≡ −1 (mod 4C)}.

For the polynomial analogue, `FUNCTIONFIELD_ES.md` Lemma 1.3 gives

    X monic, deg X=d−k; E=AX−P;
    a,b monic divisors of PX; E | a+b ≠ 0; lc(E)=lc(a+b).       (FF)

Then κ=(a+b)/E is monic and Y=κPX/a, Z=κPX/b. In the Type II chart the corresponding moving class is

    f=Aacd−1,    f | P+Aa²d,    f ≡ −1 (mod Aad).

Here the last d is an ET parameter, not deg P. These are exact divisor conditions, not statements solely about factorization degrees or Frobenius conjugacy classes.

**PROVED — a literal numerator 4 is the wrong polynomial model.** If char F_q ≥ 5, three monic reciprocals have leading coefficient 1, 2 or 3 at their least denominator degree, never 4. Thus 4/P with monic denominators is impossible for every P. Without the monic condition, constant nonzero numerator c is trivial in odd characteristic: c/P=1/(2P/c)+1/(4P/c)+1/(4P/c). See `ff_erdos_straus.md` Prop 1.2 and `padic_functionfield_igusa.md` §3.3. Neither version is integer ES.

### 1.2 Exactly what is proved over function fields

All repository theorems below are **PROVED internally**, not externally refereed; computer-assisted items have the archived review qualifications of their sources.

| Status | Exact result | Actual mechanism |
|---|---|---|
| PROVED, elementary | q=2 or 3, A=T: every irreducible P≠T is solved | P(0)∈{−1,−2}; constant-E identities; `FUNCTIONFIELD_ES` Prop 1.4 |
| PROVED, elementary | q=2, A=T², deg P≥3 | explicit identity using P(0)=P(1)=1; Thm 6.1 |
| PROVED, computer-assisted | q=2, every monic A of degree 2 or 3; A=T⁴,T⁴+1; q=4,A=T; every irreducible P with deg P>deg A | finite congruence-family coverings and finite checks; Thms 6.3–6.4; other unarchived batch successes are only EVIDENCE |
| PROVED relative to Weil RH | fixed q,A: failure proportion ≤(Φ(A)+o(1))/log d as d→∞ | first/second moments **averaged over P**, using primes dividing P+1; Thm 5.3; not every P |
| PROVED relative to Weil, effective | every q,A, irreducible s∤A, and irreducible P∤As: ES_q^(s)(A,P) | one mute place: third term Q²/Z, Q a power of s; `FF_MUTE` Thm 3.5; fixed-P character sums and primitive-root sieve |
| PROVED, computer-assisted | q=3^r,r≥2,A=T^k,k≥1: no finite linear covering; also no finite covering by the specified seven ET types | sterile **profinite slice points**, root-product/reciprocity law, exact counts and convergent tail bounds; `FF_STERILE_SMALL` Thm 5.2/8.1, `FF_ODD_ABSENCE` Cor 2.3, `FF_INVERSION_CHECK` Cor 2.6 |
| CONJECTURE | the specified x*_c is sterile for q=3,A=T² | `FUNCTIONFIELD_ES2` Conj 0.2; `FF_THIRDS_CORNER` residual Bezout/divisor problem; not an ES theorem |

**PROVED / scope correction.** Sterility of a profinite point is not an exceptional irreducible P. Positive uncovered measure in the cited *slices* does not mean positive Haar measure in the full profinite unit group: `FF_STERILE_PROOF` Thm 3.2 proves the latter sterile set is Haar-null. Small-characteristic covering identities are not Weil existence proofs. `DRINFELD_ES` Thms 1.3 and 2.2 give obstruction-side identities (odd Kummer data split at P; odd prime-to-characteristic Brauer evaluations vanish), not new universal ES_q existence theorems.

### 1.3 The actual fixed-degree limit

**PROVED — all-characteristic NC extension of O140 Thm 2.1.** For any q, any monic A of degree k≥1 and d>k,

    #{irreducible monic P of degree d with ES_q(A,P)}
       ≤ 2·64^d q^(d−k).                                    (1)

Consequently the success proportion is O_d(q^(−k)), uniformly in A of degree k. There is **no** q₀(d,k) after which all degree-d P are solved, including along q=3^r→∞.

*Proof.* For any NC solution, at least one denominator is divisible by P and has degree ≥d. The coefficient at the least degree shows that exactly one denominator X has degree d−k: at most two denominators can occur at that degree, and their leading coefficients sum to 1 only when there is one. Use (FF). Since P∤X, each divisor of PX is either a₀ or Pa₀ for a monic divisor a₀ of X. If a,b contain the same power of P, gcd(E,P)=1 gives E | a₀+b₀, and the leading-coefficient condition says that E=(a₀+b₀)/κ₀ for a monic divisor κ₀. A zero sum is excluded. If just a contains P, reduce P≡AX mod E to get E | AXa₀+b₀. Here deg(Pa₀)>deg b₀, so E is monic. Each of these nonzero polynomials has degree ≤2d. A polynomial of degree at most 2d has at most 2^(2d) monic divisors: ∏(e_i+1)≤2^(Σ e_i)≤2^(2d). For each of q^(d−k) choices of X there are at most D² pairs (a₀,b₀) and D choices of E in each of two cases, D=2^(2d). Finally P=AX−E is determined. Counting extra invalid/reducible P only enlarges the bound. The irreducible polynomial theorem gives π_q(d)∼q^d/d for fixed d. ∎

**Assessment — integer meaning of “fixed degree, q→∞.”** There is no canonical ordered-integer transfer. In the norm dictionary |P|=q^d and |A|=q^k, this changes the numerator scale together with the denominator: heuristically m≈H^(k/d), H≈|P|, not m=4 fixed. In the coefficient dictionary it is bounded algebraic complexity with an increasingly large coefficient field; over Z the nearest geometric operation is reduction of a fixed-degree scheme modulo increasing residue primes, which counts congruence points. It is not the assertion about every positive integer of increasing height. The ES-like function-field asymptotic is **q,A fixed and deg P→∞**. Changing base in a digit expansion is not a ring homomorphism F_q[T]→Z and introduces carries.

## 2. Which existence mechanisms act on one fixed input?

### 2.1 Weil can be pointwise in P, but only for the predicate it counts

**PROVED relative to Weil — precise useful estimate.** Fix P,A,s over F_q, put D=deg(APs), and let h=deg s. For a nontrivial Dirichlet character χ modulo APs,

    |Σ_{deg f=e, f irreducible monic} χ(f)| ≤ (D+1)q^(e/2)/e.

For a character ψ of prime order ℓ|q^e−1,

    |Σ_{α∈F_(q^e)} ψ(s(α))| ≤ (h−1)q^(e/2),

with ψ extended by zero. These are `FF_MUTE` Lemmas 3.3–3.4, derived from Weil and the standard multiplicative character-sum bound (Rosen, *Number Theory in Function Fields*, Chs. 3–4; Lidl–Niederreiter, *Finite Fields*, Thm 5.41, citation as in the source).

**PROVED relative to that source.** Taking e to be an odd prime controls the tail ℓ|q^e−1, ℓ∤q−1 by ℓ≡1 mod 2e. The count of shot primes f satisfying

    f≡−1 mod A,    −P/A is a square mod f,    s primitive mod f

has positive main term δq^e/e and error O_(q,A,s)((deg P+e)q^(e/2)/e), after the small tail loss. A suitable e≤4log_q(deg P)+O_(q,A,s)(1) exists (`FF_MUTE` Thm 3.5). P stays fixed: the summed variables are f, or its roots α, and the subsequent exponent j in Q=s^j is free. This is a genuine single-P theorem.

**Assessment / necessary correction to the brief.** A fixed smooth projective geometrically integral curve of genus g satisfies |#C(F_Q)−Q−1|≤2g√Q; this can force a point on **that fibre** when Q is large (for an affine open, subtract the removed boundary points). But the mute proof actually also uses a family of Kummer conditions and a sieve; it is not one universal fixed ES curve. Its clean asymptotic is fixed q,P with e growing. At fixed P the relevant conductors are bounded, while P varying makes their complexity grow. No positive-dimensional, geometrically irreducible fixed-P *integral cap-0 certificate* fibre has been supplied. Equation (1) prevents assuming every such fibre is populated. Katz–Sarnak-style statistics or Chebotarev averaged over coefficient vectors do not repair that missing hypothesis.

**PROVED — exact loss on returning to cap 0.** The mute construction needs only f≡−1 mod A. The resulting third denominator is polynomial-integral iff

    f≡−1 (mod A Q),    Q=s^j,                               (2)

by `FF_MUTE` Cor 2.2. Thus the modulus grows with the exponent chosen to fire the shot. The analogous integer condition is f≡−1 mod 4Q. Primitive-root/Frobenius conditions force membership in a group generated modulo f, not the exponent budget required by (2). This is B2/B-fin, even after unconditional RH over function fields. Over Z a generalized Artin/Hooley theorem would at best reproduce the mute theorem, not remove (2).

### 2.2 What Ax–Kochen and pseudofinite fields actually transfer

**PROVED, classical — AKE, with source scope.** For every fixed first-order sentence φ in the language of valued fields there is N_φ such that, for every prime ℓ>N_φ,

    Q_ℓ ⊨ φ  iff  F_ℓ((t)) ⊨ φ.                            (AKE)

One obtains this from elementary equivalence of the ultraproducts: both have characteristic-zero pseudofinite residue field ∏_U F_ℓ and the same value group ∏_U Z. Reference: Ax–Kochen, “Diophantine problems over local fields I,” *Amer. J. Math.* 87 (1965), 605–630; the statement was checked through the linked secondary account, and Denef's primary abstract confirms the local transfer scope: [arXiv:1601.03607](https://arxiv.org/abs/1601.03607). The original Ax–Kochen proof was not re-read.

**PROVED — elementary scope distinctions.**

* The variable ℓ in AKE is the characteristic of the residue field; it is not the ES input p in a global assertion about Z.
* Integrality in Q_ℓ means Z_ℓ, not Z. Adding a valuation-ring predicate does not add simultaneous integrality at all places or real positivity. Local/BM solubility is already known for the ES surface.
* Fixed d, bounded polynomial degrees can be encoded by finitely many coefficient variables and first-order field formulas. Degrees growing with the input change the formula; the bound N_φ is not uniform over an unbounded sequence of formulas.
* q=3^r→∞ is not residue characteristic→∞; it does not enter the displayed Q_ℓ/F_ℓ((t)) transfer.
* If K=∏_U F_q, then ∏_U F_q[T] contains [T^(e_q)] with e_q→∞. It is not just K[T], whose individual polynomials have standard finite degree. Replacing the former by the latter loses precisely unbounded-degree witnesses.

**PROVED, classical — Ax's theorem.** Infinite pseudofinite fields are exactly the perfect PAC fields with one extension of each finite degree. Reference: Ax, “The Elementary Theory of Finite Fields,” *Ann. Math.* 88 (1968), 239–271; characterization and bibliographic details checked at the [Oxford seminar page](https://people.maths.ox.ac.uk/bays/mtpsf/). PAC gives rational points on geometrically integral varieties, not integral polynomial points with NC, monic normalization and degree caps. Q is not PAC: x²+y²+1=0 is geometrically integral and has no Q-point. Thus an ultraproduct being PAC supplies no elementary-equivalence bridge to Q.

**Assessment.** “No Frobenius” must be qualified: integers certainly have residue-field Frobenius and associated Galois representations. What is missing is a uniformly controlled finite-field fibre whose points encode **exact positive divisors of the specified integer**, with the tied class and height retained. Frobenius of a polynomial modulo ℓ usually counts modular roots/factorization, not factors in Z. The congruence xy≡N mod ℓ permits xy=N+kℓ; enforcing k=0 is the height problem. No impossibility theorem against all geometric encodings is claimed.

### 2.3 A maximally honest transfer target

**CONJECTURE — height-aware lower-tail transfer, HT(ε,p₀).** After imposing the quadratic/BM correction and retaining cap 0, a function-field-style incidence model should transfer to the integer detector with

    R(p) ≥ ε M_BM(p)    for every prime p>p₀,    0<ε<1.       (HT)

The proposed bridge must be certificate-preserving: no change of p, positive integer outputs, correct divisor class, and no relaxed exponents. This is deliberately one-sided, not an assertion of transferable two-sided square-root errors. Necessarily p₀≥8,813,281, the known last (★) failure.

**Assessment — this is a target, not new conditional progress.** HT is exactly FRONTIER's H⁻_BM in transfer language. The known FF results supply neither its cap-0 premise nor the bridge; presenting it as a corollary of AKE, Weil or GRH would be circular. A more geometric proposal would have to exhibit fibres V_p and maps V_p(F_q)→integer certificates and prove a lower count with normalized error o(log²p). B3 requires recording fibre multiplicity: a power-size point count with subpower multiplicity cannot map into the sparse ES solution set for almost all p. If multiplicity is huge, it and the resulting error have to be controlled, not silently canceled. At the shot level the precise missing implication is (Frobenius firing)⇒(some firing with (2)); at the detector level it is BM-allowed coset⇒target divisor class.

## 3. Attempts with proofs and numbers

### 3.1 A degree-two classification: five curves, almost every fibre empty

**PROVED — quadratic toy theorem.** Let q be odd, A=T, and P=T²+bT+c irreducible. Put v=c+b+1. Then ES_q(T,P) holds iff at least one of

    c=−1;   c=−2;   v=−1;   cv=−1;   cv²=−1                (3)

holds in F_q. In particular at most 5q coefficient pairs are solvable, so for every odd q>11 some irreducible quadratic fails, and the failure proportion tends to 1.

*Proof.* The unique least-degree denominator is X=T+x and E=(x−b)T−c. The monic divisors of PX are 1,X,P,PX, of distinct degrees 0,1,2,3. Also gcd(E,PX)=1. If E is constant, its leading coefficient −c must be 1 or 2, giving c=−1 or −2; conversely both are solved by the constant-E identities. If E is linear and lc(E)=2, (FF) requires a,b to have equal degree, hence to be equal. Then E | 2a contradicts gcd(E,PX)=1. All other linear hits require lc(E)=1, hence x=b+1 and E=T−c. Evaluating the four divisors at T=c gives 1,v,cv,cv², all nonzero. The sums of two *distinct-degree* divisors vanish exactly when v=−1, cv=−1, cv²=−1, or c=−1. This proves necessity and sufficiency by (FF). Each locus has ≤q pairs: for cv²=−1 choose v≠0 then c=−v^(−2), b=v−c−1; the others are just as simple. There are q(q−1)/2 irreducible quadratics, exceeding 5q for q>11. ∎

**CERTIFIED — finite arithmetic / independently checked small range.** `scripts/z45_transfer_logic_toy.py` streams the coefficient pairs. For q≤19 the classification is compared to the existing complete divisor engine `scripts/bs_ff_es.py`: **474 irreducible inputs, zero disagreements**. The q=5,…,19 totals also reproduce the archived O140 census. Larger rows are exact evaluations of (3), not an independent general solver run.

| q | irreducibles | solved | failed | success proportion |
|---:|---:|---:|---:|---:|
| 3 | 3 | 3 | 0 | 1 |
| 5 | 10 | 8 | 2 | .8000 |
| 7 | 21 | 15 | 6 | .7143 |
| 19 | 171 | 44 | 127 | .2573 |
| 31 | 465 | 79 | 386 | .1699 |
| 101 | 5,050 | 236 | 4,814 | .0467 |
| 503 | 126,253 | 1,250 | 125,003 | .00990 |

**PROVED — PAC does not repair even this toy.** Take odd q_i→∞ and a failing irreducible quadratic P_i from each field. In K=∏_U F_(q_i), the polynomial P=T²+[b_i]T+[c_i] remains irreducible (absence of a root is first-order) and violates all five conditions (3), by Łoś. The algebraic proof of (3) works over any field of odd characteristic, or characteristic zero, so P has no monic NC decomposition in K[T]. Yet K is PAC. Thus even an explicit pseudofinite coefficient-field limit retains polynomial-integral failures.

**Assessment.** A Weil calculation on the coefficient curves could refine the number of *base polynomials P* represented. It would not prove a point on a prescribed empty fibre. This toy reverses the “exceptional means structured” intuition too: here **successes** have five simple algebraic explanations and failures are generic. It is not evidence that integer ES has generic failures; it is evidence that the models and limits cannot be interchanged.

### 3.2 What “nearly independent events” does and does not imply

**Assessment — premise correction.** The ∼log³p figure is a heuristic/average number of full ES successes per prime, not a theorem that a fixed prime supplies that many independent fair bits. For (★) the trial set has size ∼p log p and rare-event mean ∼(3/(2π²))log²p over primes, with swap pairing and arithmetic dependence. None of these averaged facts gives an individual prime a probability space on which a concentration inequality is already proved.

**PROVED — a rare event can contain unstructured free bits.** On Ω={0,1}^L with the uniform measure, let the success tests be “bit i equals 1” for i=1,…,h. They are exactly independent, and their simultaneous failure set F has size 2^(L−h). For any auxiliary datum a of at most s bits and integer t>0, there is x∈F with

    K(x | L,h,a) ≥ L−h−s−t

simultaneously against all such a, once t is a suitable absolute constant: the union over <2^(s+1) choices of a of the outputs of programs shorter than L−h−s−t has fewer than |F| elements. Thus rare all-fail outcomes need not have O(log L) conditional complexity relative to a short invariant. They can retain essentially every free bit. Taking h=⌊L^(2/3)⌋ gives the same information-deficit scale as the known ES exceptional-set bound. ∎

**PROVED — why sufficiently strong independence would already solve the problem.** If, on the **actual uniform finite population of L-bit primes**, one proved an all-fail fraction ≤exp(−cL³), then multiplying by at most 2^L primes makes the number of failures <1 for all sufficiently large L. They would be absent by integrality. This is a lower-tail theorem stronger than needed, not an independent complexity argument. With (★), an actual exp(−cL²) bound would likewise suffice. A heuristic probability law does not give the finite-population inequality.

### 3.3 The rigorous, but weak, compression theorem

**Definition.** K denotes prefix-free Kolmogorov complexity for a fixed universal conditional machine. Let E_L be the finite set of exceptional primes in [2^(L−1),2^L). Its membership is decidable by bounded exhaustive ES search (§3.5).

**PROVED — rank coding lemma.** For a uniformly computable finite set F_y and x∈F_y,

    K(x | y) ≤ ⌈log₂ |F_y|⌉ + O(1).                         (4)

*Proof.* From y enumerate F_y, compute its size, then read an index of exactly ⌈log₂|F_y|⌉ bits and output the indexed element. For each fixed y all codes have the same length, hence are prefix-free. The decoder has constant description length. Its runtime can be enormous. ∎

**PROVED relative to Vaughan's published bound.** There exists c>0 such that every hypothetical exceptional prime p of sufficiently large bit length L satisfies

    K(p | L) ≤ L−cL^(2/3)+O(1).                             (5)

*Proof.* Vaughan gives #E∩[1,X]≪X exp(−c₀(log X)^(2/3)). Take X=2^L and apply (4) to E_L. ∎

Reference: R. C. Vaughan, “On a problem of Erdős, Straus and Schinzel,” *Mathematika* 17 (1970), 193–198, DOI 10.1112/S0025579300002886. The primary text remains unavailable in the campaign; the bound is quoted by Elsholtz–Tao, arXiv:1107.1010v6, Introduction p. 3, as documented in `reviews/lit-audit-C-exceptional-set.md`. **PROVED relative to the internally reviewed, unrefereed 3/4 theorem:** replace 2/3 in (5) by 3/4 if using `paper/es-threequarter-note.tex`.

**Assessment — exact answer to the conditional-complexity question.** Bit length L is a short invariant, with K(L)=O(log L); (5) is a legitimate nontrivial compression statement for *every* exception, without assuming independence. It is still K≈L, not K=O(log L). The decoder uses the exception predicate itself and searches it exhaustively: this provides no arithmetic structure that forces factors into wrong residue classes. Relative to arbitrary primes, which already admit an index of length L−log₂L+O(1), the saving is of order L^(2/3), not a new pointwise theorem. An invariant containing the entire failure pattern, or “rank among exceptions,” makes stronger slogans tautological unless its description length and computation budget are charged.

**PROVED — the least exception is maximally compressible in a vacuous way.** If ES is false, a fixed program enumerating n and halting at the first failure outputs the least exception, so its unconditional K is O(1). This does not bound its value or runtime. “All sufficiently simple numbers satisfy ES” would therefore itself imply ES (if it includes this fixed program). Kolmogorov lower bounds cannot be inferred from primality, and no contradiction follows from (5).

### 3.4 Controls: 131, 241, 409, 577

**CERTIFIED, inherited rather than redundantly recomputed.** The campaign's exhaustive tests give 8/p exceptions among primes <2000 exactly {2,3,11,17,131,241}; 409 and 577 fail (★) but satisfy full ES. Sources: `AMPLIFY_EXCEPTION.md` Thm 2.5, `FRONTIER` §§1–2, `B1_LINE.md` §3.6. Thus 131 and 241 are the fifth and sixth entries of one short decidable exception list; 409 and 577 are the first two entries of the (★)-failure list **restricted to p≡1 mod 4**. Calling them compressible by these descriptions explains nothing about the factors responsible for failure.

**PROVED — elementary comparisons.** 131=11²+10, 241=15²+16, 409=20²+9, and 577=24²+1. Modulo 840 their residues are respectively 131,241,409,577, none of the six full-ES Mordell-hard classes. These four examples therefore do not identify a common “prime T1.” The near-square description of 577 is relevant to known level depletion, but a small offset selected *after* seeing an integer is not a complexity certificate with a proved causal implication. A finite collection of 8–10-bit numbers cannot reveal an asymptotic Kolmogorov law; universal-machine additive constants dominate.

**Assessment, corroboration from another already-present memo.** `BRAINSTORM/z45_prime_t1_dual.md` and its exact data separate subgroup-kernel obstruction from exponent-budget failure: at 8/131, 27 of 33 first-denominator fibres are budget failures rather than kernel obstructions; at 8/241, 34 of 60 are. This does not imply incompressibility—the same memo explicitly exhibits short budget-sensitive quotient explanations. I inspected its summary and representative fibre, not independently recertified its entire computation. It supports distinguishing “short description of an exception” from “one arithmetic character kills all fibres.”

### 3.5 Π₁, nonstandard counterexamples, and overspill

**PROVED — explicit bounded formula.** Order a positive solution x≤y≤z. Then x≤3n/4. With r=4x−n>0,

    r/(nx)=1/y+1/z ≤2/y,    hence y≤2nx.

With s=4xy−n(x+y)>0, z=nxy/s≤nxy. Therefore x≤n, y≤2n², z≤2n⁴. These inequalities and the sorting argument are provable in PA. Thus ES(n) is equivalent in PA to the bounded formula

    ∃x,y,z≤2n⁴ [x,y,z≥1 ∧ 4xyz=n(xy+xz+yz)],

and ES is Π₁. The same bound works for fixed positive numerator m, using mx−n and mxy−n(x+y).

**PROVED — three logically different models.**

1. In an elementary extension *N of the standard arithmetic structure, ES has exactly its standard truth value. If ES is true, there are no nonstandard counterexamples in *N or any ultrapower of N. Conversely, a counterexample in such an ultrapower means standard counterexamples occur on an ultrafilter-large set of coordinates. If it is nonstandard, those coordinates cannot be confined to a finite set of values.
2. An arbitrary M⊨PA need not satisfy all true Π₁ sentences. If ES is true but PA does not prove it, completeness gives a model of PA+¬ES, necessarily with a nonstandard least counterexample. This is **CONDITIONAL on truth and PA-unprovability of ES**, neither of which has been established. The least counterexample is prime by the usual divisor/scaling descent, formalizable in PA.
3. Failure of every *standard fixed template* is weaker still. By Dirichlet, choose standard primes p_i≡1 mod i!, p_i→∞. Their ultraproduct p* is prime and ≡1 modulo every standard integer. Every fixed ET family missing the sterile residue 1 fails there. If ES is true, Łoś nevertheless gives ES(p*), with unbounded template parameters. No contradiction: a countable intersection of standard avoidances is not the internal universal quantifier over all parameter values.

**PROVED — literal standard-size denominators are the wrong test.** Each denominator satisfies x>p/4 because 1/x<4/p. Thus *any* nonstandard prime, solved or not, has no solution with all three denominators standard. The useful distinction is between standard auxiliary template parameters and p-dependent denominators, not “standard-size witness tuples.” A genuine internal counterexample defeats standard and nonstandard certificates alike, including the entire internal box ≤2(p*)⁴.

**PROVED — exactly what overspill gives.** Suppose f is a fixed PA-definable total function and every standard prime has a witness of size ≤f(p). For M⊨PA in which these standard instances hold, define

    A(B) : ∀p≤B [Prime(p) ⇒ ∃w≤f(p) Cert(p,w)].

For every standard B, M⊨A(B). Overspill gives a nonstandard B with M⊨A(B). One can see this without invoking saturation: if ¬A has a least element b, it is nonstandard and b−1 is a nonstandard element satisfying A; if ¬A is empty, choose any nonstandard B. This reaches some nonstandard primes: the internally largest prime ≤B cannot be standard, since then a larger standard prime would still lie below B. It does **not** reach an arbitrary prescribed p*. If M has a least counterexample p*, the verified initial interval can end below p*. A fixed numeric bound on the denominators could not hold for all standard primes; f(p) is essential.

**PROVED — uniformity that ES would imply, and nothing extra.** If ES is true, its bounded search provides a total computable witness selector, with witnesses of O(log n) bits; polynomially many arithmetic steps in the *value* n suffice by brute force (e.g. O(n³) pairs (x,y), solving for z). This is exponential time in input bit length, not FP. If PA proves ES, the same witness existence holds internally at **every** prime in **every** PA model. If it holds in every PA model, completeness gives PA⊢ES. There is no overspill argument converting truth on the standard cut to that stronger assertion, nor a standard bound on the least successful template obtained from compactness.

## 4. FRONTIER §4 screening checklist

**Assessment.** PASS below means the restricted formulation respects the screen, not that it proves ES. FAIL identifies missing arithmetic in the proposed transfer/complexity route. N.A. means no mechanism of that type is used.

| # | Result | Reason |
|---:|---|---|
| 1 | FAIL | Raw local/PAC transfer does not carry integer T1. Monic FF Type II squares can be solved; DRINFELD gives only degree-parity restrictions. HT repairs the statement by M_BM(m²)=0, but no class-existence proof follows. |
| 2 | FAIL | Generic logic/rank coding/Weil transfer does not distinguish numerator 4 from 8. The genuine 8/131,8/241 exceptions rule out threshold-free versions; HT must be 4-specific and eventual. |
| 3 | FAIL | No numerator-specific inverse theorem is obtained. Compression is valid for arbitrary computable sparse exception sets and supplies no k-uniform transport law. |
| 4 | FAIL | Exact lost condition is f≡−1 mod AQ (integer 4Q), or D≡−1 mod 4C inside D|4Cp+1. No new tied-modulus divisor theorem. |
| 5 | FAIL | Mute Weil keeps P fixed, but transfers only relaxed certificates. The FF density theorem and complexity rank estimate average over P/p; no recovery of the prescribed cap-0 fibre. |
| 6 | FAIL | Mute main term δq^e/e has an infinite auxiliary source. Fixed-degree ES_q successes instead have density O(q^(−k)); over Z the target main term is log²p, not a power count. No sufficiently small error or controlled high-multiplicity encoding. |
| 7 | PASS | HT is explicitly one-sided; no two-sided R(p) asymptotic is proposed. FF point counts are not asserted to transfer as two-sided integer counts. |
| 8 | FAIL | Standard-template compactness sees fixed congruence menus; p*≡1 at every standard level survives them. Unbounded arithmetic formulas are not ruled out, but their nonstandard witnesses are uncontrolled. |
| 9 | FAIL | Primitive-root/character firing gives the allowed group/coset, not the exponent-bounded divisor class. Higher residue symbols and PAC do not supply that class. |
| 10 | N.A. | No pooling of large prime factors across shifts is used. |
| 11 | N.A. | No signed-to-positive reflection is proposed. The failure to transfer positivity is stated explicitly. |
| 12 | FAIL | This is exactly the mute-to-integral transport gap (2); no cap-reduction theorem. |
| 13 | FAIL | Local AKE statements cannot upgrade known BM solubility to integral existence. No new global obstruction is exhibited. |
| 14 | PASS | 409,577 are respected as (★), not ES, failures; HT allows all 14 known (★) failures below p₀. No claim that the b=1 line or prime-modulus Type II always succeeds; 193,2521,66529 and 3361 remain controls, and 5101441 is not predicted to have many a=1 witnesses. |
| 15 | FAIL | Generic compression is insensitive to Mordell cells/near-square depletion; 577's offset is descriptive only. No inverse theorem after conditioning on these cells is proved. |
| 16 | N.A. | No thin-family win is transported to arbitrary primes. Fixed coefficient degree is explicitly not an integer thin-family proof. |
| 17 | FAIL | The desired class depends on actual large factors; neither overspill nor rank compression controls their residues. The finite-field shot theorem only controls a group orbit before the exponent cap. |

## 5. New-theory sketch and its tested toy case

**Definition / proposed framework — resource-aware transfer profiles.** For a certificate predicate record the tuple

    (input fibre, degree/height budget, sign/NC condition, exponent cap,
     formula/conductor complexity, encoding multiplicity, counting measure).

A transfer is *faithful* only if its witness map preserves the input and cap 0, sends normalized signs to positive denominators, and gives explicit bounds on all growing resources. Model-theoretic elementary equivalence without that witness dictionary is a local/formal transfer, not an ES transfer. This bookkeeping is modest and overlaps prior barrier language; it is not claimed as a developed new theory.

**First theorem needed (CONJECTURE-level target).** Construct a faithful profile for a p-dependent growing family with BM-corrected mass ≫log²p and one-sided remainder <that mass at each prescribed p. Its missing component is a bounded-height, bounded-exponent inverse theorem for the divisor incidence, not PAC or compactness. This is stronger data than HT and would imply it; no such construction is known.

**PROVED toy test.** For deg P=2,A=T the profile has fixed formula complexity and exact monic/NC constraints, but the success image is the union of five coefficient curves (3), not a uniformly nonempty fibre over the two-dimensional base. The script and table in §3.1 test the entire image, not selected examples. At q=503, 125,003 of 126,253 fibres are empty despite bounded algebraic complexity. For the mute profile cap>0, the theorem supplies fibres; the witness map fails the cap-preserving entry exactly at (2). This explicitly identifies *which profile coordinate* is lost.

**Alternative inverse-theory target (CONJECTURE-level, not established).** Replace unrestricted K by an a priori chosen, efficiently computable arithmetic description language: invariant I(p) with description O(log L), and a short certificate explaining simultaneous divisor-class failure **without enumerating ES failures**. An inverse theorem “every exception has such a certificate” would be new and falsifiable against numerator controls; it would still need a separate theorem excluding those certificates for numerator 4. The toy bit lemma shows rarity/independence alone cannot give it, and the degree-two experiment shows which side of a problem is structured can reverse under transfer. Merely demanding low K is already supplied by (5) and does not constitute this theory.

## 6. Verdict and next steps

**Assessment — PARTIAL, promise 1/5.** There are useful rigorous corrections and a small explicit FF classification, but no new arithmetic input toward ES. The exact open implication is Frobenius/group firing with unlimited shots ⇒ a cap-0 divisor in the tied class at this one p. The alternative “exception⇒structure” implication is proved only in the weak, enumeration-based Kolmogorov sense; its arithmetic inverse version is entirely open. The largest practical finding is that the hoped-for fixed-degree large-q universal ES_q theorem is false, in the opposite density direction.

**Assessment — concrete next steps.** (i) Archive/review the five-curve calculation and the all-characteristic NC extension; they are short, independently checkable side results. (ii) If pursuing logic, specify an actual height/cap-preserving interpretation before any more AKE/PAC work. (iii) If pursuing structure, fix a non-tautological arithmetic invariant language and decoder budget first, then test it on the existing numerator-8 and (★) failure data. Do not run a Kolmogorov-complexity “measurement”: K is uncomputable, and these tiny controls cannot estimate it.

**CERTIFIED — reproducibility / resource limits.** Ran `ulimit -v 2000000; timeout 180 uv run python scripts/z45_transfer_logic_toy.py` successfully; small-case independent-engine mismatches=0. The scan streams O(q²) coefficient pairs, keeps only row summaries and small cleared caches, and writes `data/z45_transfer_logic/toy.json`. No existing file is modified. This memo's verdicts were self-reviewed against the source errata: in particular no inference from shared profinite limit points to blindness of all first-order arithmetic; no claim that AKE has an ineffective bound in every formulation; no claim that FF sterility gives exceptional P; no claim that low complexity implies a common character obstruction; no positive-dimensional fixed-fibre assertion without geometric hypotheses.
