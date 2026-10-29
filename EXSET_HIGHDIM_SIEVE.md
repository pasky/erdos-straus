# EXSET_HIGHDIM_SIEVE — z51 lane 1b (`hidim`)

ES remains OPEN. Internal research note; no external refereeing.

## 0. Outcome ledger (skeleton)

| Round | Question | Status | Review |
|---|---|---|---|
| 1 | Exact large-dimension literature and independent G1 audit | Completed within stated source-access limits; no advance claimed | Opus R1: no fatal issue; repairs recorded §6 |
| 2 | Named hypothesis ⇒ RLD-U or T1-min | Pending | Pending |
| 3 | RLD-U ⇒ recognised open statement | Pending | Pending |
| 4 | Non-Selberg weights and enumerable controls | Pending | Pending |

Labels: PROVED (internal proof), CONDITIONAL (explicit hypothesis), CERTIFIED (finite exact check), EVIDENCE, CONJECTURE, Assessment. A restatement of G1–G5 does not count as an advance. Every claimed advance receives hostile Opus review (`anthropic/claude-opus-5-5:high`, deep).

## 1. Definitions, scope, and source audit

**Scope audit (PROVED definitions; no advance claimed).** Write I_N={1≤n≤N:n≡1 (8)}, S=4ℕ∪(8ℕ+7), and

    F_l={−u mod l : u|(l+1), u∈S},  p_l=|F_l|/l,
    V(z)=∏_{3≤l≤z, l prime}(1−p_l),
    A_z(N)={n∈I_N : n mod l∉F_l for every l≤z}.

This is the **direct-endpoint family** actually computed by `scripts/z50_ajopus_chain.c`, and the one with empirical *local* mass slope ≈0.74 near 10⁶ in z51 CONTEXT. That number is not a proved asymptotic constant; every theorem here uses V(z) itself or two-sided mass comparability. RLD-U here means |A_{N^{1/s}}(N)∖□|≤C_s |I_N| V(N^{1/s}) for fixed s>1. We do not require the additional C_s→1 assertion to discuss T1-cond.

The broader prime-word family in `EXSET_SIEVE_MASS.md` Prop. 2.3 also allows the *other* endpoint v=(n+u)/l to lie in S. It is different: at l=13 the direct set is {6}, while u=2 gives v≡7 (8), hence adds residue 11 to the broader set. Its reported slope ≈1.07 must not be substituted for 0.74. The bound for one family does not automatically imply the corresponding product-normalised bound for the other. Both have cumulative mass Θ(log z) by the same BV/Brun–Titchmarsh argument, keeping the 4ℕ line for the lower bound.

Every direct class is a nonzero quadratic nonresidue modulo l (Theorem E/reciprocity), so all odd squares survive. Class labels are distinct: divisors of l+1 lie in [1,l+1], and the only potential collision is {1,l+1}; 1∉S. The proper-divisor exclusion in the census causes no change on I_N: l=n+u gives n=l−u; for u∈S this is incompatible with n≡1 (8) and l≡−1 (u). Explicitly, u=0 (4) gives l=3 (4) but n+u=1 (4); u=7 (8) gives l=n+u=0 (8). Thus a hit always supplies the proper prime divisor on this fibre.

**Inputs used, not re-proved:** z48–z51 CONTEXT (z51 binds); FRONTIER §§2–4,6–7; BREADTH_Z45 through §15; PR-B index/arithmetic/covers; OAI_DUMP_IMPACT; z48 forest/lower-tail summaries; DISCOVERIES (D)17–31; EXSET_SIEVE_MASS §2; EXSET_ARITH_JANSON_OPUS §§5.5–6. Quasi-RH, if discussed, remains CONDITIONAL on OAI-003. No claim concerns a proof or disproof of ES.

**Targets.** T1-min is |A_N(N)∖□|≤N exp(−(log N)^{1/2+δ}) for some δ>0. T1-cond asks for RLD-U or T1-min from a named standard hypothesis (or one visibly weaker), or a proved implication to a recognised open problem. G1 is the existing Θ(√log N) ceiling for whole-avoider, nonnegative CRT-majorant evaluations at polynomial level.

**Research plan after audit.** Test standard named inputs before inventing a new one. Three distinct statements must not be conflated: (a) a prime-tuple upper bound; (b) total-variation approximation of factor/hit vectors; (c) a one-sided estimate only for the all-zero event. Only (c) is RLD-U. We will also test necessary conditions for the reverse inclusion from prime tuples into A_z(N).

## 2. Round 1 — literature and independent G1 derivation

### 2.1 Verified literature (source audit, not a new theorem)

Primary PDFs were downloaded, converted with `pdftotext`, and the relevant statements read. Full URLs and access limitations are in `data/z51_hidim/literature_{classical,modern}.md`. Research-agent transcriptions were independently checked: corrections include the author of arXiv:1012.3809 (C. S. Franze, **not** Sara Blight), its upper bound on a *lower-sieve* threshold, and several squared-versus-iterated-log errors in the Banks–Ford–Tao ranges.

| Source actually read | Precise usable statement | Limitation here |
|---|---|---|
| Richert, *Lectures on Sieve Methods*, Ch. 11, Thm 11.4, pp. 134–136 | Under Ω₁, Ω₂(κ,L), and |R_d|≤ω(d), S≤Γ(κ+1)·singular product·X/(log z)^κ·[1+O((log log(3z)+L)/log z)], z≤√X. Constants depend on κ,A₁,A₂. | For fixed k this gives (2^k k!+o(1))𝔖(H)X/log^k X. It does **not** supply uniformity when k grows. |
| Richert, Ch. 12, pp. 159–160, discussion of Ankeny–Onishi | AO replace Kuhn's constant prime-divisor weight by a logarithmic smoothing weight. | Original AO paper not obtained; no numerical AO large-dimension constant is used. |
| Franze, arXiv:1012.3809, Thm 1 and Table 1, p. 2 | Explicit positive lower-sieve thresholds for integer κ=2,…,10 under (2)–(4). Introduction reports DHR βκ≲2.44κ and Selberg βκ≲2κ+19/36 for large κ. | βκ is where a **lower** bound becomes positive, not the prime-tuple upper constant. Original DHR large-κ calculation not verified; no βκ∼cκ formula used. |
| GKM, arXiv:1606.06781, Thm 1.3, p. 9 | For fixed k,A, M_{f_A,2k}(R)=c_{k,A}(log R)^{max{binom(2k,k)−2k(A+1),−1}}+O((log R)^{E−1}). | Constants depend on k,A. These are moments of smoothed Möbius divisor sums, not a growing-k tuple upper theorem. |
| GKM, Thm 1.4 | If f∈C^A, A≥2, derivatives bounded, support (−∞,1], and A>binom(2k,k)/(2k), then Σ_{n≤x,∃p|n:p≤R^η} M_f(n;R)^{2k}≪ηx/log R, x≥R≥2 and log2/logR≤η≤1. | A fixed-moment weight theorem. Remark 1.4 explicitly says they study Selberg-style, not combinatorial-style, weights. |
| Maynard, arXiv:1405.2593, Thm 3.1, pp. 2–3 | With C(α,θ)≤k≤(log x)^α, coefficients≤x^α, and Hypothesis 1 (progression errors ≤#A/log^{100k²}x, corresponding prime errors, and #A(x;q,a)≪#A(x)/q), A(x)=A∩[x,2x), a mean prime density δ>1/log k yields ≫#A/[(log x)^k exp(Ck)] points with ≥C^{-1}δlog k prime forms. | Lower bound for **some**, not all, prime forms. Verifying Hypothesis 1 for an already sifted U set is additional non-CRT information. |
| Banks–Ford–Tao, arXiv:1908.08613v3, Thm 1.5, p. 7 | Uniform HL with error O(x^{1−κ}) for H⊂[0,(log x)²], |H|≤2κlog x/log₂x, 2log₂x/log x≤κ≤1/2, implies G_A(x)≫κ(log x)²/log₂x. | A genuine named growing-tuple hypothesis, but no U transfer is in the statement. |
| Ford, arXiv:2408.03803, Thm 1, p. 3 | Under Z(γ), fixed a≠0,A>0,α<γ: d_TV(W_y,U_{x,y})≪exp(−αu log u)+(log x)^{-A}, u=log x/log y. W_q has P(W_q=0)=1−1/(q−1), P(W_q=v)=q^{-v} for q∤a,v≥1; W_q=0 if q|a. | One shifted prime p+a, not many shifts; at fixed u the displayed error is not a decaying relative error for a power-small avoidance event. Z(1) follows from EH, but this limitation remains. |

**Access/coverage limit.** *Opera de Cribro* book text and the original AO/DHR large-dimension calculation were not accessible in this pass. We do not present secondary snippets as verified exact theorems. Ford's uniform factor-count bound concerns ω(p+a)=k, not prime k-tuples. No verified theorem with an e^{O(k)} all-prime tuple upper constant in the requested growing range was located. This is a search-limited negative, not a claim to have established the current optimum. In particular 2^k k! is the classical general benchmark, not claimed optimal for each k (already k=2 has improvements).

### 2.2 Independent saddle calculation (PROVED calculation; rederivation, not advance)

Let h_l=p_l/(1−p_l), G(Q)=Σ_{d≤Q,d squarefree}∏_{l|d}h_l. The direct U family satisfies

    c log y≤μ(y):=Σ_{l≤y}p_l≤C log y,
    Λ(y):=Σ_{l≤y}p_l log l ≍(log y)²,
    Σ_{l≤y}p_l(log l)²≪(log y)³.                       (2.1)

These cumulative statements follow from the established BV/BT prime-divisor supply argument, not pointwise w(l)≍log l. Also p_l≤1/2 and p_l≤l^{-1+o(1)}.

For σ>0, Rankin gives

    log G(Q)≤σlog Q+Σ_l log(1+h_l l^{-σ})
            ≤σlog Q+C'/σ+O(1).

The last inequality is partial summation of μ(y)≪log y, with h_l≪p_l. Optimise σ≍1/√log Q: log G(Q)≪√log Q. Conversely restrict to primes≤y with log y=c₀√log Q, c₀ small. Normalised weights ∏h_l define a random squarefree d whose prime inclusions are independent Bernoulli(p_l). Its mean log d is Λ(y)≤(log Q)/2; Markov gives P(d≤Q)≥1/2. Therefore

    G(Q)≥(1/2)∏_{l≤y}(1+h_l)≥(1/2)exp(μ(y)),
    log G(Q)≍√log Q.                                  (2.2)

This independently rederives the optimised Selberg/Montgomery loss, including its cause: most mass of the full Euler product lives at products far beyond Q. At Q=N^θ for fixed θ>0, log G(Q)=Θ(√log N); choosing Montgomery's Q≈√|I_N| gives an actual upper bound with this saving and no coefficient-remainder issue. The extension to **all** nonnegative level-limited CRT majorants uses the existing comparison theorem `EXSET_SIEVE_MASS` Thm 2.2(b), not an unproved assertion that Selberg is universally optimal. To meet its p_l≤1/4 hypothesis, absorb all primes≤100 into the fixed base modulus Q₀=8∏_{3≤l≤100}l and its allowed residue set R. For l>100, w(l)≤τ(l+1)≤2√(l+1)<l/4. The cost relative to the original mod-8 fibre is the fixed constant −Σ_{l≤100}log(1−p_l); the full ambient normalisation also includes log 8. The remaining slice primes are disjoint from Q₀, s_*≥log101, and truncated μ̄≪λ, as required. This finite-base qualification is implicit but missing from the cited proposition. Here a whole-avoider majorant is ≥1 on the periodic avoider set on **all integers**, not merely on its intersection with [1,N]. Level counts the slice-prime part; the fixed base costs O(1). Interval-only or prime-only positivity is not covered.

### 2.3 Which weights lie outside G1? (Assessment with algebraic check)

A divisor polynomial Σ_{d≤R}λ_d 1[d|P(n)] raised to an even power 2r expands into congruence intersections with lcm≤R^{2r}. A multidimensional weight Σ_{d_1,…,d_k}λ_{d_1,…,d_k}∏1[d_i|L_i(n)] with support ∏d_i≤R has square level≤R². Smooth coefficients alter the coefficients, not these support bounds. If such a weight majorises **the U avoider set**, is nonnegative on all integers, and is evaluated by CRT means plus the admitted errors, G1 applies. A prime-tuple majorant is not automatically a U majorant.

Rosser/β/Brun–Hooley upper-bound weights also expand in congruence intersections at their stated level. Selberg's Λ²Λ⁻ lower sieve is not globally nonnegative, but is a **minorant**, not an upper bound for U avoidance; it supplies no escape by changing the sign of the desired inequality. GKM/Maynard weights do not escape by their name. Genuinely signed high-modulus interval evaluations or prime-supported positivity could escape; none of the cited results supplies the required U estimate. This confirms G1's audited scope without extending it to every conceivable use of those authors' methods.

## 3. Round 2 — implication up

### 3.1 Named-input audit (Assessment: no implication up established)

Ranked by standardness, not by an unproved logical ordering:

1. **GRH, EH/GEH:** standard. Their usual statements concern characters or distribution of named sequences in progressions. Using them only to evaluate polynomial-level congruence weights retains §2's cap. This does not prove that GRH/EH cannot imply RLD-U by another argument.
2. **Uniform HL as in Banks–Ford–Tao Thm 1.5:** a precise named growing-tuple hypothesis. It concerns prime values of bounded-height shifts, not the factorizations of all n+u with u|l+1. No inclusion or positive decomposition of the U avoiders into the counted prime tuples has been found. Improving the all-prime constant to e^{O(k)} would not by itself supply that missing decomposition.
3. **Kubilius independence:** established in short ranges for one integer/shifted prime, with explicitly absolute errors (Ford Thm 1). A full-law extension to the present growing system is not merely unproved: the following theorem rules it out. This is a different obstruction from squares and from the nonnegative CRT-majorant cap.
4. **Only an all-zero-event upper bound with error O(V(z)):** this would suffice but is RLD-U itself up to constants. Calling it a relative Kubilius hypothesis adds no standardness and is not T1-cond progress. The same warning applies to putting a relative-distribution hypothesis directly on the already sifted set.

### 3.2 Full-law support obstruction (PROVED; new scoped barrier, not T1-cond)

Let ν_z be the product law of independent Bernoulli variables X_l with P(X_l=1)=p_l for the direct U family. Let μ be **any** probability measure supported on at most M bit-vectors. This includes the vector

    (1[n mod l∈F_l])_{l≤z}

for any probability distribution on at most M integers, after removing any specified exceptional set (in particular squares), or restricting to primes.

**Theorem 3.1.** For every a>0,

    d_TV(μ,ν_z) ≥ 1−min{1, exp(B_a)},
    B_a = [a log M + Σ_{l≤z}log((1−p_l)^{1+a}+p_l^{1+a})]/(1+a).       (3.1)

If μ(z)=Σp_l≍log z and p_l≤l^{-1+o(1)}, there are c,C>0 such that, for all sufficiently large z,

    log M ≤ c (log z)²  ⇒  d_TV(μ,ν_z) ≥ 1−exp(−C log z).             (3.2)

In particular, for any fixed δ>0 and z=exp((log N)^{1/2+δ}), every law of at most N integers has d_TV→1. This holds a fortiori at z=N^{1/s}, fixed s>1, and still holds after removing all squares.

*Proof.* Let T be the support of μ. Then d_TV≥μ(T)−ν_z(T)=1−ν_z(T). Hölder gives

    ν_z(T) ≤ |T|^{a/(1+a)} [Σ_x ν_z(x)^{1+a}]^{1/(1+a)}.

The last sum factors over the primes, proving (3.1), including degenerate coordinates p_l=0. Write L=log z and c₁log y≤Σ_{l≤y}p_l≤c₂log y for large y. Choose fixed η=c₁/(2c₂) (decrease it if necessary to lie in (0,1)). The band z^η<l≤z has Σp_l≥(c₁/2)L. For large z, p_l≤l^{-1/2} throughout this band. Take a=1/L. Then p_l^a≤exp(−η/2), and

    (1−p_l)^{1+a}+p_l^{1+a}
       ≤1−(1−exp(−η/2))p_l.

All outside-band logarithmic terms are nonpositive. Thus

    B_a ≤ [log M/L − bL]/(1+1/L),
    b=(1−exp(−η/2))c₁/2>0.

If log M≤bL²/2, then B_a≤−bL/4 for L≥1. Take c=b/2,C=b/4. ∎

**Why this exceeds G1's scope.** No majorant, congruence level, coefficient bound, or algorithmic restriction is assumed. It rules out *every* small-error total-variation coupling of the full hit vector to the independent model in the depth-breaking range, including hypothetical non-CRT couplings. Its elementary Hölder/support principle is standard information theory; the application identifies a specific impossible strengthening of RLD-U. It does **not** bound a single-event relative error: ν_z({0})=V(z) is tiny, and TV near 1 can coexist with a correct zero-event probability. It therefore neither refutes RLD-U nor asserts it is as hard as an independent recognised conjecture.

**Square floor and private primes.** The proof holds for arbitrary supports and uses neither squares nor large-prime sharing. For shifts u≠v, l|n+u and l|n+v force l|u−v; if l exceeds the shift diameter, it is private to one shift. This gives exclusivity *within* a prime coordinate, not independence *between* primes for an integer drawn from [1,N]. The finite-support restriction survives after conditioning away every square. A full factorisation-law coupling would imply a hit-vector coupling by deterministic projection, and hence is ruled out too whenever its independent-prime model projects to ν_z.

### 3.3 Attempt to weaken the impossible input

**PROVED elementary implication, explicitly not a target advance.** If a law on nonsquares satisfied E exp(−tΣ_l X_l)≤K∏_l(1−(1−e^{−t})p_l) for one fixed t>0 and K=O(1), then its zero-event probability would be ≤K exp(−(1−e^{−t})μ(z)). At a power level this gives a power saving and T1-min. This is weaker than full-law coupling but no standard named hypothesis has been shown to imply it; it is not visibly weaker than its desired exceptional-set consequence. We do not promote it to a new conjectural 'conditional theorem'. The exact missing input is a one-sided **rare-event** estimate, not a full probability-law approximation.

## 4. Round 3 — implication down

Pending. An upper bound for a full avoider set is not automatically an upper bound for a larger subfamily avoider set. Require an explicit inclusion/reduction and quantitative scales.

## 5. Round 4 — numerical controls and further attacks

Pending. Scripts `scripts/z51_hidim_*`; data `data/z51_hidim/` (<20 MB). All commands bounded in time and memory. Include odd squares, the hard primes and 14 R-zeros; numerator 8 controls wherever a mechanism transfers.

## 6. Reviews and exact remaining gap

Pending. Commit after each completed section. Do not merge without parent instruction.
