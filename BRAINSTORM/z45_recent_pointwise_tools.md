# z45 — Recent pointwise tools: primitive divisors, Shimura heights, and the missing intersection

## 0. Summary

**Assessment.** This scan finds genuine single-integer factorisation theorems, not an ES proof. Pasten's 2024 theorem, its 2025 polynomial extension, and a September 2026 refinement are pointwise; BHV is even pointwise and sensitive to a modulus tied to the sequence index. But BHV supplies a divisor of the *wrong integer*, with no guaranteed inert sign, while Pasten supplies size/exponent information, not the required class. There is an especially sharp negative test: making `4Cp+1` literally a value `a²+1` forces **every divisor into 1 mod 4**, whereas ES needs −1 mod 4C. An elementary Lucas dictionary below identifies the exact missing intersection and counts its trace parameters. Most other recent breakthroughs average over the integer, require a dense auxiliary set, or allow the arithmetic object/ring to change. Several candidates were already examined in the campaign; no novelty is claimed for rediscovering those barriers.

**Verdict: PARTIAL — the open implication is a fixed-p, inert primitive-divisor intersection theorem; promise 1/5.** The direct `a²+1` embedding and integer cyclotomic construction COLLAPSE, not the whole fields of heights or recurrence sequences. ES remains open.

**Reading/novelty audit (Assessment).** Read FRONTIER §§2–4,6–7, B2_ACROSS_FIELDS §3 and synthesis, relevant sections of LITERATURE_2026 and LITERATURE_AUTOMORPHIC, and the brainstorm index. `git grep` found: Merikoski already in PARITY_AUDIT D6; BHV already in POINTWISE_TYPEI4; the *specific primitive-divisor analogy* already in TORSION_FIRING Prop. 3.5 and BRAINSTORM/y3_lucas_dickson_trace; Smith/Koymans–Pagano already in the Rédei memos, but not the H10 construction; Kelley–Meka already mentioned in technique_transfer_list. Pasten's bounds and the Green–Sawhney/H10 proofs were not found in the tracked memos. New here means this explicit comparison, recent-source update, and toy experiment—not priority for the elementary mathematics.

## 1. Exact dictionary

### 1.1 ES slice and its finite range

**PROVED (elementary; existing campaign dictionary).** Put `t=4C`, `N=tp+1`. A divisor `d|N`, `d≡−1 (mod t)`, yields

`u=(d+1)/t`, `B=(N/d+1)/t`, `p=tuB−u−B`.

Consequently

`4/p = 1/(uBC) + 1/(pBC) + 1/(puC)`.

Conversely every such triple gives `(tu−1)(tB−1)=tp+1`. Since `u,B≥1`, `p≥t−2`, so `C≤(p+2)/4`. This is only (★), not all ES; it has known prime failures. Requiring **prime** `d` is a further restriction.

### 1.2 Lucas rank, not just a character

**PROVED (standard finite-field argument).** Let `U_0=0,U_1=1,U_{r+2}=P U_{r+1}−Q U_r`, with coprime nonzero integer `P,Q`, discriminant `D=P²−4Q≠0`, and nondegenerate roots α,β. For an odd prime `ℓ∤QD`, its rank of apparition is

`r_ℓ = ord(α/β)`, and `r_ℓ | ℓ−(D/ℓ)`.

Indeed Frobenius fixes the two roots when D is a square and interchanges them otherwise; thus the ratio belongs respectively to `F_ℓ*` or its quadratic-extension norm-one torus. A primitive divisor at index t therefore satisfies `ℓ≡(D/ℓ) (mod t)`. **The minus sign is an extra condition, not a conclusion of BHV.** Inertness plus exact rank t forces the *whole* class −1 mod t, genuinely stronger than quadratic parity alone.

For ES take `D=p` with p ≡ 1 (mod 4) (R-z45 repair: needed for `(P²−p)/4` to be an integer), `P` odd, and `Q=(P²−p)/4`, with `p∤P`. These are legitimate nondegenerate Lucas pairs: `gcd(P,Q)=1`, Q is a nonzero integer, and the real roots have a ratio different from ±1. The desired prime certificate is obtained if

`ℓ | tp+1`, `r_ℓ(U(P,(P²−p)/4))=t`, and `(p/ℓ)=−1`.                         (PI)

**Assessment.** BHV proves that the rank-t condition has *some* prime solution for t>30, without either the first condition or the minus sign. It gives no lower bound on their intersection. Conversely, §3 proves that letting P vary through all residues merely re-encodes existing prime certificates.

### 1.3 Other dictionaries and their limits

**PROVED / Assessment.** Pasten attaches to the integer a the elliptic curve `y²=x³+3x+2a`, whose displayed discriminant is `−1728(a²+1)`; conductor/discriminant estimates constrain its prime exponents. Thus the relevant object is the *support and multiplicities* of the factorisation, not a divisor class. Additive-combinatorial tools could act on the residues of factors of N, but neither density nor Gowers-uniformity of that prescribed multiset is supplied by their theorems. Selmer theorems control groups attached to fields/curves, not ideal divisors of a prescribed element. Hilbert properties assert non-thinness of existing or potentially available points, not positive integral solvability in this fixed model.

## 2. Verified theorem inventory and actual existence mechanisms

**Source convention.** “PROVED (literature)” records a published theorem or theorem stated in a cited preprint, not an independent proof audit. Preprint status is stated where material. Numbered statements below were read in fetched full-text excerpts, except the explicitly marked secondary verifications. Files in `data/z45_recent_pointwise_tools/` retain excerpts; some long HTML extractions are truncated after the introductory/main statements. This is a targeted scan through 2026, not an exhaustive bibliography.

### A. Pasten and effective abc: genuinely pointwise

**PROVED (literature).** Hector Pasten, *The largest prime factor of n²+1 and improvements on subexponential ABC*, Invent. Math. 236 (2024), 373–385, [arXiv:2312.03566](https://arxiv.org/abs/2312.03566), Thms 1.1–1.2: for all sufficiently large a,

`P⁺(a²+1) ≫ (log₂ a)²/log₃ a`,
`log rad(a²+1) ≫ (log₂ a)²/log₃ a`.

Here `log_j` means j-fold iterated logarithm, not base j. Lemma 3.2 gives `∏_{ℓ|a²+1}v_ℓ(a²+1) ≪ rad(a²+1)^8` for every a. Theorem 2.4 (quoting Cor. 16.3 of *Shimura curves and the abc conjecture*, JNT 254 (2024), 214–335) states that for E/Q semistable outside fixed S,

`∏_{ℓ|N, ℓ∉S}v_ℓ(Δ_min) ≪_{S,ε} N^{11/2+ε}`.

**Mechanism (Assessment, read in §2.3).** Modularity and Jacquet–Langlands give parametrisations from different Shimura curves; a Ribet–Takahashi degree-ratio formula detects products of discriminant valuations. Arakelov lower bounds for quaternionic-form norms bound that product. Linear forms in logarithms, applied after separating high- and low-exponent primes, then force a large radical/prime. No averaging over a occurs. The displayed output uses prime magnitudes and exponents, not ℓ mod 4C. A refined ray-class height inequality would be new input; it is not present here.

**PROVED (2025 preprint statement).** José Cuevas Barrientos–Pasten, [arXiv:2504.15971](https://arxiv.org/abs/2504.15971), Thm 1.3, gives the same two lower bounds with constants depending on f for quadratic f with two distinct complex roots (real roots are allowed), and for `f(x)=(ax+b)³+c`, `ac≠0`; the statement uses truncated iterated logarithms. Thm 1.1 gives a conductor/Faltings-height bound for every nonsingular integer fibre of `y²=x³+A(t)x+B(t)`, A,B coprime over Q and not both constant. **Assessment:** pointwise in the fibre, but constants depend on the entire polynomial/family. Substituting a p-dependent polynomial without tracking those constants is invalid.

**PROVED (September 2026 preprint statement, not independently refereeing it).** Pasten, [arXiv:2609.01327v1](https://arxiv.org/abs/2609.01327), Thm 1.1 and Cor. 1.2:

`(log₂ a)² ≪ log rad(a²+1) · log₂ P⁺(a²+1)`,
`P⁺(a²+1) ≫ (log₂ a)²/log₄ a`.

Cor. 1.3 also forces many moderately large prime factors *if the largest factor is near the lower-bound scale*: writing P=P⁺(a²+1), for an absolute κ>0,

`#{ℓ|a²+1 : ℓ>κ(log₂ a)²/log₂P} ≫ (log₂ a)²/((log P)log₂P)`.

**Assessment:** this is a useful correction to any claim that all recent factorisation progress averages. But the multiplicity conclusion is conditional on a restrictive size regime if it is to be large, and still specifies no target residue class.

**PROVED (literature, verified through Pasten's introduction, not the original PDF).** Stewart–Yu, *On the abc conjecture II*, Duke Math. J. 108 (2001), 169–181, Thm 1: for coprime positive a+b=c and R=rad(abc), `log c ≪ R^{1/3}(log R)³`. Pasten Thm 1.4 improves special regimes: if `a≤c^{1−η}`, then `log c ≤ η⁻¹ exp(K√(log R log₂R))`; also `log c ≤ q exp(K√(log R log₂R))`, `q=min(P⁺(a),P⁺(b),P⁺(c))`. **Assessment:** every triple is covered, using logarithmic forms and heights; no class-sensitive existence follows. Even abc itself is not a divisor-class theorem.

### B. BHV, Zsigmondy, Schinzel: pointwise moving-class analogues

**PROVED (literature; primary BHV access blocked, verified in Voutier and Stewart).** Bilu–Hanrot–Voutier, J. reine angew. Math. 539 (2001), 75–122, Thm 1.4: every Lucas or Lehmer number of index t>30 has a primitive prime divisor. Lucas pairs have α+β and αβ nonzero coprime integers and α/β not a root of unity. Lehmer pairs replace α+β by `(α+β)²`; their even terms divide by `α²−β²` rather than α−β. “Primitive” excludes the discriminant factors and all earlier terms. The t>30 assertion is reaffirmed in P. Voutier, [arXiv:2411.07909v2](https://arxiv.org/abs/2411.07909), introduction; its Thm 1 corrects small-index **Lehmer** classifications, not t>30. The original theorem number is also explicitly cited in [arXiv:1304.6413](https://arxiv.org/abs/1304.6413).

**Mechanism (Assessment, verified historical account in Stewart §1).** Cyclotomic factorisations isolate new factors; bounds for logarithmic forms and reduction to finitely many Thue equations exclude defective large indices. This controls one term, with no average. It does **not** impose `(D/ℓ)=−1`, nor make ℓ divide an independently prescribed `tp+1`.

**PROVED (classical; secondary exact statement checked at [MathWorld](https://mathworld.wolfram.com/ZsigmondyTheorem.html)).** For coprime integers a>b>0 and t≥2, `a^t−b^t` has a prime dividing no earlier `a^j−b^j`, except `(a,b,t)=(2,1,6)` and `t=2` with a+b a power of 2. Such a prime has `ord_ℓ(a/b)=t`, hence `ℓ≡+1 mod t`, **not −1**. Schinzel's algebraic-number generalisation and its uniform Lucas/Lehmer predecessor are documented in Stewart, [arXiv:1008.1274v1](https://arxiv.org/abs/1008.1274), §1; for ES the precise applicable uniform version is BHV above. No unverified general-field threshold is used.

**PROVED (older quantitative benchmark).** Stewart, same paper, Thm 1: if `(α+β)²,αβ` are nonzero integers and α/β is not a root of unity, then

`P⁺(Φ_t(α,β)) > t exp(log t/(104 log log t))`

for t>C, C effectively depending on `ω(αβ)` and the discriminant of Q(α/β). **Assessment:** again pointwise, but the threshold is not uniform in a p-dependent quadratic field; more size does not supply the missing sign/intersection.

### C. Analytic primes and correlations: the fixed integer is averaged away

**PROVED (literature).** Merikoski, [arXiv:1908.08816](https://arxiv.org/abs/1908.08816), Thm 1: `P⁺(n²+1)>n^{1.279}` infinitely often; Thm 2 replaces 1.279 by 1.312 under Selberg's eigenvalue conjecture. Grimmelt–Merikoski, [arXiv:2505.00493](https://arxiv.org/abs/2505.00493), Thm 1.1, makes the latter exponent unconditional at a=h=1, and treats `an²+h` uniformly under its explicit prime-root-density hypothesis. In particular for every sufficiently large X some n∈[X,2X] has `P⁺(n²+1)>X^{1.312}`. **Mechanism/Assessment:** Chebyshev–Harman sieve plus spectral Type I/II estimates; averaged variables include n, divisibility moduli, and bilinear factors. Fixed h (even h=p) is allowed in some ranges, but then the ES class modulus depends on the free variable n; no hit for one prescribed side number follows. Already screened in PARITY_AUDIT D6.

**PROVED (2024 preprint statement).** Green–Sawhney, [arXiv:2410.04189v2](https://arxiv.org/abs/2410.04189), Thm 1.1: for fixed positive n≡0 or 4 mod 6 and smooth compactly supported W,

`Σ_{x,y} Λ(x)Λ(y)Λ(x²+ny²) W(x/N,y/N)`
`= κ_n N² ∫W + O_W(N²(log log N)²/log N)`.

Here κ_n is their explicit positive singular product, and n is fixed throughout the asymptotic. Thus infinitely many primes are `x²+ny²` with **both x and y prime**. **Correction:** this is not an every-output-prime representation theorem, and it is not the theorem about `x²+ny⁴`. Their §1.1 attributes `x²+y⁴` to Friedlander–Iwaniec and the square-of-a-prime refinement to Heath-Brown–Li. **Mechanism/Assessment:** Gowers-norm control of coordinate weights, concatenation, a number-field DFI sieve, and a three-dimensional upper-bound sieve. Both x and y and hence the output prime vary. Fixing the coefficient n does not fix the output integer. The power-size N² main term is bought by those free coordinates.

**PROVED (literature).** Pilatte, [arXiv:2310.19357v2](https://arxiv.org/abs/2310.19357), Thm 1.1: some absolute c>0 satisfies

`Σ_{n≤X} λ(n)λ(n+1)/n ≪ (log X)^{1−c}`.

**Mechanism/Assessment:** high-trace estimates for a graph with edges indexed by products of ≍log log X primes, plus multiplicative-function estimates; a dense exceptional-vertex deletion is part of the proof. It averages n logarithmically and additional divisor/shift variables. It is not pointwise control of the parity of Ω(n), much less divisor classes. A spectral bound on the surviving graph is not a guarantee for an arbitrary deleted fixed vertex.

**CONDITIONAL (on the specified Siegel zero).** Tao–Teräväinen, [arXiv:2109.06291](https://arxiv.org/abs/2109.06291), Thm 1.6: if a primitive quadratic character of conductor q has zero `β=1−1/(η log q)`, η≥10, then for fixed distinct shifts, `0≤k≤2`, l≥0, and

`q^{10k+1/2+ε₀}≤X≤q^{√η}`,

`E_{n≤X} ∏_{i≤k}Λ(n+h_i) ∏_{j≤l}λ(n+h'_j)`
`= S + O((log η)^{-1/(10 max(1,k))})`,

where S is the prime-tuple singular series if l=0 and zero otherwise. **Mechanism/Assessment:** exceptional-character approximations and sieve/divisor correlations; n is averaged. It neither proves absence of Siegel zeros nor settles both sides of a zero/no-zero dichotomy for fixed-p ES.

### D. Additive combinatorics and Selmer: every set/field is not every integer

**PROVED (literature).** Kelley–Meka, [arXiv:2302.05537](https://arxiv.org/abs/2302.05537), Thm 1.2: if A⊆[N] has density ≥2^{−d}, it has at least `2^{−O(d^{12})}N²` triples x+y=2z. Hence Thm 1.1 gives `r_3(N)≤N exp(−c(log N)^β)` for some β>0. Bloom–Sisask, [arXiv:2007.03528v2](https://arxiv.org/abs/2007.03528), Thm 1.1: `r_3(N)≪N/(log N)^{1+c}`, c>0. **Mechanism/Assessment:** density increments, high moments/sifting, almost-periodicity and additive structure. They apply to each sufficiently dense set, not just an average over sets; that distinction matters. But the theorem supplies neither density of a prescribed divisor-residue set nor a representation of the specified element −1. A three-term progression somewhere is not a prescribed product target.

**PROVED (2024 preprint statements).** Leng–Sah–Sawhney, [arXiv:2402.17994](https://arxiv.org/abs/2402.17994), Thm 1.2: a 1-bounded f:[N]→C with `||f||_{U^{s+1}[N]}≥δ` correlates by at least ε with a degree-s nilsequence, with dimension `≤log(1/δ)^{O_s(1)}` and complexity, Lipschitz norm, and ε⁻¹ `≤exp(log(1/δ)^{O_s(1)})`. Their [arXiv:2402.17995](https://arxiv.org/abs/2402.17995), Thm 1.1, gives `r_k(N)≪N exp(−(log log N)^{c_k})` for fixed k≥5. **Mechanism/Assessment:** efficient inverse theorem plus nilsequence recurrence/decomposition and density increment. Deterministic for a given function/set, but does not establish that an ES-weight function has a small uniformity norm or that its structured alternative forces the specified target. It is a quantitative component of Green–Sawhney, not a pointwise divisor theorem.

**PROVED (literature/preprint theorem).** Koymans–Pagano, [arXiv:2412.01768v3](https://arxiv.org/abs/2412.01768), Thms 1.1–1.2: H10 has a negative answer for every infinite finitely generated ring over Z; Z is Diophantine in O_K for every number field K. The actual useful existence input, Thm 2.4, is: if K has at least 32 real places and L=K(i), some elliptic curve E/K satisfies `rank E(K)=rank E(L)>0`.

**Mechanism (read in §§1.3–1.4).** Start with full rational 2-torsion `y²=∏(x−a_i)`; twist by `t=d∏(c−a_i d)`, which contains the explicit point `(c/d,1/d²)`. A number-field Green–Tao theorem chooses d and the three linear factors prime simultaneously. Controlled 2-descent makes the complementary twist have rank zero; real places resolve reciprocity compatibility. **Assessment:** a genuinely every-field existence theorem, but the curve, twist, c,d and prime factors are *chosen*, not prescribed. Requiring their product equal one specific N(p) removes that freedom. Also a rational non-torsion point gives no bounded positive integral ES point. H10 undecidability itself has no bearing on the finite ES search.

**PROVED (literature theorem statements, final two-paper revision read).** Smith, [arXiv:2207.05674](https://arxiv.org/abs/2207.05674), Thm 1.2: for E/Q satisfying Assumption 1.1, the 2^∞-Selmer coranks of quadratic twists have densities 1/2,1/2,0 for ranks 0,1,≥2. The assumptions are: E[2](Q)=0; or exactly one rational 2-torsion point and the 2-isogenous curve's 2-torsion field is neither Q nor the original field; or full rational 2-torsion and no rational cyclic 4-isogeny. Thm 1.9: the higher 2-class ranks of Q(√−d), ordered by positive integers d<H, have Markov law

`P^Mat(r_4|∞) ∏_{j≥3}P^Mat(r_{2^j}|r_{2^{j−1}})`,

where P^Mat(b|a) is the nullity distribution of uniform a×a matrices over F₂. The base 2-rank is **not** assigned a bounded Cohen–Lenstra distribution; it has the genus-theoretic growth. Main general theorem: sequel [arXiv:2207.05143](https://arxiv.org/abs/2207.05143), Thm 2.14.

**Mechanism/Assessment:** governing pairings, bilinear character sums and combinatorial grids with varying prime factors. These give distributions across twists/discriminants, not constraints on one specified class group, and not on all prime factors of a fixed N. “100%” does not mean every twist; Selmer corank is not automatically Mordell–Weil rank equality without extra input.

### E. Integral Hilbert properties and the log-K3 boundary

**CONJECTURE (not a breakthrough theorem).** The Corvaja–Zannier integral weak-Hilbert prediction says that Zariski-dense S-integral points on a smooth variety imply the weak Hilbert property after a possible field extension and enlargement of S; precisely quoted as Conj. 1.3 in Luger, [arXiv:2410.13403v3](https://arxiv.org/abs/2410.13403). **PROVED (same source, Thm 1.4):** for connected linear algebraic G/K and Z⊂G of codimension ≥2, some finite L/K and finite T give the weak Hilbert property on `(G\Z)_L` over O_{L,T}. This uses strong approximation, Kummer theory and Hilbert irreducibility, not a positive integral-point theorem on U_p.

**PROVED (literature).** Coccia, JNT 200 (2019), 353–379, [arXiv:1807.03349v1](https://arxiv.org/abs/1807.03349), Thm 1.14: for smooth cubic surface F̃ and smooth hyperplane section H over k, there exist K/k finite and finite S such that `(F̃\H)(O_{K,S})` is Zariski dense and has the integral Hilbert property. Thm 1.15 gives non-thin rational-integer points on `x³+y³+z³=1`. Mechanism: two conic fibrations, integral Pell-type fibres and avoidance of ramified covers. **Assessment:** fixed variety, but potential integrality changes K,S; ES's singular cubic/model and positivity do not satisfy this theorem by analogy. Even its Fermat conclusion allows signed points, not positive ones.

**CONJECTURE.** Lang–Vojta for surfaces: if X is of log general type, then X(O_{K,S}) is not Zariski dense (e.g. Conj. 1.1 as quoted in [arXiv:1310.7871v2](https://arxiv.org/abs/1310.7871)). Log general type means `K_Xbar+D` big; a log K3 pair instead has trivial log canonical class. **Assessment:** this is a degeneracy/upper-bound conjecture in the wrong geometric class, not existence at a fixed p. Deleting additional boundary to obtain log general type further restricts points; it cannot create ES solutions. BM has already been settled negatively as an obstruction by Bright–Loughran. No Vojta/Lang-to-ES implication is asserted.

## 3. Attempts with proofs and numbers

### 3.1 The literal Pasten substitution is sterile

**PROVED (elementary, scoped no-go).** If p is an odd prime and C≥1 satisfy `4Cp+1=a²+1`, then `a=2pk`, `C=pk²` for an integer k≥1. Every prime divisor ℓ of this odd number is 1 mod 4, so every divisor is 1 mod 4. Therefore there is no divisor −1 mod 4C.

*Proof.* `a²=4Cp` implies a even and p|a. For ℓ|a²+1, ℓ is odd, a is a unit modulo ℓ and `a²≡−1`; its order is 4, so 4|ℓ−1. Products of those factors remain 1 mod 4. ∎

**PROVED (additional size check).** These C satisfy C≥p, already outside the positive (★) range C≤(p+2)/4. The residue obstruction is stronger in that it explains sterility directly at the factor level.

**Assessment.** Applying even an arbitrarily strong largest-prime-factor theorem to this exact substitution produces only forbidden divisors. This does not exclude other polynomials or weighted class-sensitive height inequalities. It does show that “Pasten is pointwise, therefore take C to make his polynomial appear” is not a route.

### 3.2 Exact trace census: where the information is hidden

**PROVED (standard torus parameterisation, specialised here).** Fix p≡1 mod 4 prime, t=4C, and a prime `ℓ|tp+1`. There is an integer P odd, p∤P for which ℓ is an inert primitive divisor of `U_t(P,(P²−p)/4)` **iff** `ℓ≡−1 mod t`. When that class condition holds, exactly φ(t) residues P mod ℓ give rank t.

*Proof.* The forward direction is §1.2. Conversely, ℓ≡−1 mod 4C implies `(C/ℓ)=1`: write C as a square times a squarefree integer and apply quadratic reciprocity to its odd factors; when C is even, ℓ≡−1 mod 8 also gives `(2/ℓ)=1`. As `p≡−(4C)⁻¹ mod ℓ`, it follows that `(p/ℓ)=−1`.

Choose s∈F_{ℓ²} with s²=p. The map

`P ↦ ζ=(P+s)/(P−s)`

is a bijection from F_ℓ to the norm-one torus with 1 removed: its inverse is `P=s(ζ+1)/(ζ−1)`, fixed by Frobenius. This cyclic torus has order ℓ+1. Exactly φ(t) elements have order t. Their P are not zero (zero gives ζ=−1, order 2). Lift each residue to an odd integer P not divisible by p, using CRT. The Lucas pair then has discriminant p and is coprime; modulo ℓ its rank is t, so ℓ divides no earlier term or discriminant factor. ∎

**Assessment.** This is not a new primitive-divisor existence theorem. It quantifies why choosing the recurrence *after finding ℓ* is circular. Unlimited trace choice is exactly equivalent to an existing prime certificate, with trace fraction φ(t)/ℓ. A fixed or short trace list must hit an unknown subset attached to an unknown divisor of N. BHV does not solve that simultaneous constraint.

**PROVED (index-mismatch warning).** `U_4(1,−2Cp)=1+4Cp` exactly. This apparently perfect embedding only supplies rank 4, not rank 4C. Its discriminant is `1+8Cp≡−1 mod ℓ` for ℓ|N, so `ℓ≡(−1/ℓ) mod 4` is a tautology. BHV is not even in its guaranteed t>30 range here. Raising the index changes the integer; it is not a free upgrade of the modulus.

**PROVED (cyclotomic sign warning).** If a,b are rational integers and ℓ is primitive in `a^t−b^t`, then ℓ≡+1 mod t. Products of these primitive factors are still +1 mod t. Replacing the difference by `a^t+b^t` leads to order 2t and again the plus class. Obtaining −1 requires a nonsplit torus, not ordinary integer cyclotomy.

**Assessment (prior obstruction, not new).** TORSION_FIRING Prop. 3.5 already proves that an identity forcing exact rank t at a rational specialisation in a fixed degree-D algebraic field entails φ(t)≤D. For quadratic Lucas data this leaves t∈{3,4,6}, hence only t=4 among 4C. It does not rule out p-dependent growing recurrences whose intersection is established non-identically. That is precisely the remaining gap.

### 3.3 Exact finite experiment

**CERTIFIED (bounded computation; not an asymptotic).** Script `scripts/z45_recent_pointwise_tools_scan.py` factors only the small side numbers, computes Lucas terms modulo each factor, and never constructs huge U_t. It checks factor products and primality. The trace-count toy has two engines: recurrence ranks and direct multiplication in F_ℓ[s]/(s²−p). Run with an 8 GB address-space cap and 180-second timeout; results are `scan.json` and `scan_summary.json`.

For all 80 primes p≡1 mod 4 below 1001, with `1≤C≤min(64,⌊(p+2)/4⌋)`:

| detector | primes hit | hit levels |
|---|---:|---:|
| arbitrary divisor −1 mod 4C | 78 | 222 |
| prime divisor −1 mod 4C | 76 | 175 |
| inert primitive divisor, trace P=1 | 46 | 53 |
| inert primitive divisor, odd P≤15 | 74 | 145 |

There are hits with t>30 for 29 of the 80 primes using odd P≤15. Separately enumerating the **entire** finite C range below 1001 reproduces exactly the (★) failures 409 and 577. The φ(t) trace formula holds in 11 small `(p,C,ℓ)` cases, totalling 221 trace residues, with both engines agreeing.

Selected cases, C≤64:

| p | arbitrary-divisor levels | prime levels | P=1 levels | odd P≤15 levels |
|---|---:|---:|---:|---:|
| 193 | 2 | 1 | 0 | 1 |
| 2521 | 1 | 0 | 0 | 0 |
| 3361 | 1 | 0 | 0 | 0 |
| 66529 | 3 | 0 | 0 | 0 |
| 5101441 | 4 | 2 | 0 | 1 |

All these detectors are zero in this range at 409,577,5569,9601,23929,83449,102001,329617,712321,8813281. These range-restricted zeros are not new global failure certificates for the larger p; the global (★) census is in FRONTIER.

Concrete successes: `(p,C,ℓ,P,Q)=(193,2,103,9,−28)` and `(5101441,48,17471,11,−1275330)`. The second has t=192>30. For 193, `1545=103·15`, so `(u,B,C)=(13,2,2)` and the denominators are `52,772,5018`.

The first 30 Mordell-hard primes between 1001 and 20000 were also scanned. For example 1129 has two divisor levels and one prime level but no odd-P≤15 hit; 2521,3361,5881,12289 have divisor hits but no prime hits in this range. All 55 primes p≡1 mod 4 in (1000,20000] within distance 4 of a square were scanned. Nine have no trace-list hit: 1093,3361,4357,7057,7393,8101,9601,15373,15877. Examples include `1093=33²+4`, `3361=58²−3`, and `4357=66²+1`; 4357 even has a prime-divisor hit that the trace list misses. These data give no universal trace-list rule. Eight odd-square controls have no (★) hit over their full C range; the numerator-8 analogues have none at 11,17,131,241. Fifteen exact Pasten embeddings at p∈{5,13,97,193,409}, k∈{1,2,3} have only prime factors 1 mod 4, as proved above.

**Assessment.** These computations test a dictionary and show its loss, not a new ES family. The strong apparent success of a short trace list is largely success of existing small-C certificates. At 3361 a universal prime-divisor mechanism would in any event miss the campaign's known prime-modulus Type-II obstruction; allowing composite divisors or other slices cannot be silently omitted.

## 4. All 17 FRONTIER screens

The ratings concern the strongest proposed route (discriminant-p primitive intersections), with the other tools noted where they differ. PASS means this obstruction is respected, not that an existence proof is supplied.

| # | status | reason |
|---|---|---|
| 1 odd squares | PASS for (PI); FAIL for bare size forcing | Essential `(p/ℓ)=−1` is impossible at odd squares. Pasten's size theorem still holds there and cannot be the missing step. |
| 2 8/131,241 | FAIL as an existence mechanism | The norm-one/rank dictionary works equally with t=8C. The scan finds no hits at the controls; no 4-specific existence input or proved threshold is available. |
| 3 numerator-uniform laws | FAIL | No reason the hoped-for intersection lower bound should distinguish 4 from other multiples of 4. We assert no transport/square/recombination law. |
| 4 tied modulus | FAIL — principal gap | Need one ℓ simultaneously primitive of index t, inert, and dividing tp+1. BHV proves only the first part for some ℓ. |
| 5 fixed p | PASS for BHV/Pasten; FAIL for analytic transfers | p stays fixed in (PI) and the computation. Merikoski/Green–Sawhney/Pilatte/Tao–Teräväinen/Smith average the integer or arithmetic objects; no recovery step exists. |
| 6 scale | N.A. for noncounting BHV; FAIL for dense counting transfer | No power-size ES main term is claimed. Dense combinatorics/prime-value estimates have not been pushed to the polylogarithmic target. |
| 7 one-sided | PASS | Proposed need is nonemptiness only, never a two-sided asymptotic for R(p). |
| 8 B1 | PASS only for a growing t-family | Full C≤(p+2)/4 is p-dependent. A fixed finite selection of t cannot be promoted to a theorem; past fixed-degree identity coupling already fails. |
| 9 class not parity | PASS conditionally on the missing intersection | Inertness plus exact rank t forces ℓ≡−1 mod t. Inertness alone does not. This is BHV's real advantage as an analogy. |
| 10 privacy | PASS | No pooling/collision of large primes across shifts is used. |
| 11 signed reflection | N.A. | Certificates from (PI) are positive directly; no reflection argument. |
| 12 relaxation transport | FAIL for unrestricted primitive primes / geometric potential points | BHV primes lie in U_t, not the finite ES box; potential S-integral points have no descent/denominator-removal theorem. Direct (PI) hits already lie in the box, but are not guaranteed. |
| 13 BM shortcut | PASS as a safeguard | No BM-only or local-global sufficiency is claimed; the gap is after the sign layer. |
| 14 test primes | FAIL for a universal (★)/prime detector | Explicit failures 409,577 and prime-factor losses 2521,3361 appear; any eventual claim needs a threshold and separate finite coverage. |
| 15 Mordell/near squares | FAIL as a uniform mechanism | Tested above; the trace-list misses include 1129 and 1093=33²+4. No uniform arithmetic argument survives. |
| 16 thin-family transfer | PASS as a safeguard | No transfer is asserted. Literal square-polynomial embedding is proved sterile, not promoted to general primes. |
| 17 large factor residues | FAIL at existence step | Primitive inert factors would be class-controlled and at least t−1, but neither their required intersection nor composite-divisor assembly is supplied. No small-factor covering argument is substituted. |

## 5. New-theory sketch and toy test

**Assessment (framework suggestion, not a claim of a new established theory).** Study **targeted primitive intersections**, rather than primitive divisors of isolated terms. For a fixed prime p define

`I_p(t,H) = {ℓ : ℓ|tp+1, (p/ℓ)=−1, ∃ odd P≤H, p∤P, r_ℓ(U(P,(P²−p)/4))=t}`.

This separates three demands that are routinely conflated: novelty of a factor, Frobenius sign, and membership in the prescribed integer. Its advantage over a reciprocity-only framework is that exact order really can force a full moving class. Its disadvantage is the third condition: the standard existence theorem says nothing about it.

**CONJECTURE-shaped first theorem needed (not endorsed as plausible).** For some A,p₀, every prime p≡1 mod 24 with p>p₀ has `I_p(t,(log p)^A)≠∅` at some `4|t≤p+2`. Such a theorem would imply an eventual **prime-divisor (★)** assertion, stronger than eventual (★). Its threshold must exceed all known (★) failures, and it would need to deal explicitly with the prime-only restriction. There is no argument or large-range evidence for it. Replacing this by a union over Type-I/II slices avoids the known fixed-line failures but adds further exact intersections—it does not weaken B2 automatically.

**PROVED toy theorem.** With unlimited trace residues, at each prime ℓ|tp+1 the number of inert exact-rank-t traces is φ(t) if ℓ≡−1 mod t and zero otherwise. This is §3.2, tested by the 221-residue two-engine census. Thus unrestricted trace freedom does not solve anything: it exactly recovers the target class already sought. The genuinely new theorem would have to choose a recurrence *without first discovering a certificate factor* and force one of its primitive inert factors to divide tp+1.

**Assessment (height variant).** A second possible framework would bound a **class-restricted radical**, e.g. the product of prime factors of N in selected classes, via a height of a marked arithmetic object. Pasten bounds an unweighted product of valuations/radical; simply inserting Dirichlet-character signs destroys the positivity behind that bound. Even an inert-factor theorem would be short of class −1 unless paired with an exact-order input. Test any proposed inequality first on the sterile `N=(2pk)²+1` family and on 409/577; it must permit their target radical to be 1. No such inequality is formulated as an established conjecture here.

## 6. Ranking, verdict, next steps

**Assessment.** Scores below are qualitative, not probabilities: pointwise refers to a *prescribed integer*, class-sensitive to its divisor class (not just a field invariant), and link to a concrete ES dictionary. “Partial” denotes a different fixed parameter or an additional sign requirement.

| tool | pointwise integer? | class-sensitive? | ES link |
|---|---|---|---|
| BHV / nonsplit Lucas | yes | yes, ±1; −1 needs inertness | strongest exact analogy; wrong-integer intersection |
| Pasten 2024–26 / polynomial heights | yes | no | exact side-number/smoothness question; literal embedding sterile |
| Stewart–Yu / Stewart Lucas | yes | no / ±1 for primitive part | quantitative antecedents; no class/sign intersection |
| Zsigmondy for integer powers | yes | yes, but +1 | wrong sign; does not yield −1 |
| Koymans–Pagano H10 mechanism | every field, not integer | Selmer/local signs only | best constructive cross-field template; loses fixed product |
| LSS, Kelley–Meka, Bloom–Sisask | every function/dense set | no prescribed multiplicative class | auxiliary machinery; no density/uniformity input |
| Green–Sawhney | no, output prime varies | quadratic-form structure | fixed coefficient is not fixed output |
| Merikoski / Grimmelt–Merikoski | no, sequence variable varies | root distribution, averaged | already screened B6/tied modulus |
| Pilatte | no | parity correlation, averaged | no pointwise exceptional-vertex control |
| Smith | no | class-group ranks, averaged | not divisors of a fixed principal element |
| Tao–Teräväinen | no; conditional | character approximations, averaged | Siegel-zero hypothesis does not remove B6 |
| integral Hilbert property | potential fixed-variety existence | not target divisor class | changes field/S, no positive integral transfer |
| Lang–Vojta | no existence theorem | no | log-general-type degeneracy, wrong direction/class |

**Top three concrete follow-ups (Assessment).**

1. **Nonsplit primitive divisors.** Before any further ES census, seek a theorem on primitive factors in a *prescribed gcd* `gcd(U_t(P,Q),tp+1)`, with discriminant p and a recurrence chosen independently of the successful factor. Compare to TORSION_FIRING Prop. 3.5 immediately. A size theorem for U_t or a CRT choice made after factoring N is not progress. Extend to composite certificates only with an explicit assembly theorem.
2. **Pasten's valuation-product inequality.** Inspect whether the Shimura degree-ratio construction admits marked local data strong enough to bound a class-restricted radical, keeping constants uniform in the moving modulus. A useful first result would be a concrete signed/refined inequality on a nonsterile polynomial family, not another unweighted largest-factor bound. The direct a²+1 version is already excluded by §3.1.
3. **Koymans–Pagano's constructive Selmer method.** Isolate their freedom to choose four prime linear forms and ask whether *any* analogue survives with their product prescribed. First prove this in an auxiliary model with an explicit extra free coordinate. Without a theorem removing that coordinate while preserving integrality, do not claim transfer to ES. This ranks third as a design lesson, not as an immediate tool.

**Self-review (Assessment).** Rechecked the highest-ranked sources and decisions: BHV does not guarantee an inert divisor; Pasten's iterated logarithms are not powers of log p; the Cayley parameterisation only gives traces after a certificate factor exists; prime-divisor (★) is strictly narrower than ES; potential integral Hilbert properties allow changing both field and S. These checks reduce the verdict to a missing intersection, not an assertion that all recurrence/height approaches are impossible.

**Final assessment: PARTIAL, 1/5.** New source coverage and a precise, tested rank/intersection dictionary are useful. No named ES barrier is escaped by an existence mechanism. The genuinely pointwise tools do refute the overly broad heuristic “all factorisation progress is averaged”; they do not refute B2. The surviving arithmetic requirement is exactly the single-integer, moving-class intersection specified in §5.
