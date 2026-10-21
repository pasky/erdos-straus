# HARDNESS_MAP — implications, not analogies

## 0. Summary and arrow diagram

**Assessment.** The strongest useful downward arrow is computational: a deterministic polynomial-time algorithm returning **any** positive ES witness at primes would derandomise quadratic-nonresidue finding. No factorisation oracle is needed: the two denominators having the same p-divisibility, after removing p, have product of Legendre symbol −1. This extends the repository's five-slice extraction to unrestricted witnesses. Height arrows require care: `max(x,y,z) ≤ p·polylog(p)` is **already false**, by an elementary `max(x,y,z)>p^(3/2)/2` bound; genuinely informative least-nonresidue comparisons use reduced parameters or forest endpoints. The other substantive arrows are precisely scoped counterfactuals to Dickson/Hypothesis H and standard-conjecture implications into relaxations. An elementary extension of the repository's mute-prime sieve gives **EH ⇒ two fixed mute primes suffice**. None of these arrows proves ES, implies GRH, or identifies ES with factoring, three cubes, or another famous open problem.

**Verdict: relative-hardness map completed; ES remains open.** Novelty below means *relative to this repository*, not a claim of external priority. “New” denotes a new explicit deduction/extension of existing ingredients.

```text
 H4 <= f ──A1──> least QNR r <= f <──A2── reduced-pair height <= f
    │                         ▲                     │
    └──A1──> ES-five ──A1──> ES                     └──> ES
                              ▲
 efficient unrestricted ES ─A5┼──> deterministic QNR ─A6─> prime square roots
                              │          ▲
 S^1_2 proof of ES ──A8────────┘          └──A6── prime square roots
 FQ ──A7──> ES-SEARCH in FP^FACTOR       GRH ─A9─> r << log²p

 GRH ─A12─> polylog exponent cap       Dirichlet ─A13─> ES-square
 GRH ─A14─> one fixed mute prime       BV+sieve ─A14─> four mute primes
 EH  ─A15─> two fixed mute primes      GRH ─A16─> V_phi off its square set

 bounded formal-menu success ─A10─> NOT Hypothesis H
 linear-form version / fixed roots / bounded windows ─A10─> NOT Dickson
 finite ET congruence cover ─A10─> contradiction to Dirichlet + T1
 two-sided polylog R-asymptotic ─A11─> contradiction to Linnik
 H_BM^- ─A11─> eventual (star) ──> eventual ES [finite base still needed]
 exception amplification law ─A19─> ES [using Vaughan]
 positive integral BM sufficiency on the ES family <──A18──> ES
 Schinzel eventual-k conjecture ─A17─> eventual ES and eventual 5/n
```

**Labels.** All solid arrows are **PROVED implications** (sometimes relative to a cited theorem). A source such as GRH, EH, FQ or a proposed successful proof shape is not asserted true. When recording the resulting arithmetic theorem assuming such a source, the label is **CONDITIONAL on that source**. Refuted source nodes are explicitly marked; arrows from them are useful only as pruning statements. No missing arrow signifies a proved logical independence result.

**Prior-art audit.** Read the task's named files, `FRONTIER.md`, and the complete brainstorm index. The requested keyword harvest has 3,532 matching lines, retained in `data/z47_hardness_map/implication_harvest.txt.gz` (a search index, not 3,532 theorems). Principal predecessors: `BREADTH_Z45.md` §5; `FOREST_H4.md` §§3.1–3.3; `POINTWISE_SIZE.md` Lemma CT/Theorem C; `notes.md` Lemma 77.6; `CONSTRUCTIVE_ES.md` §4; `BRAINSTORM/z31_complexity.md`; `BRAINSTORM/logic_complexity.md` **including its errata**; `CONDITIONAL_ES.md`; `B2_ACROSS_FIELDS.md` §3; `PROPAGATION_CLOSURE.md`; `AMPLIFY_EXCEPTION.md` §1. The negative standard-conjecture audit in `CONDITIONAL_ES.md` is cited, not repeated as a purported independence proof.

## 1. Nodes and quantifiers

**Definitions.** Unless stated otherwise p is prime, `p≡1 (4)`. All numerical bounds are pointwise; implied constants are uniform in p.

| Node | Exact meaning |
|---|---|
| ES(n), ES | `4/n=1/x+1/y+1/z`, positive integers; respectively one n, or every n≥2. |
| eventual ES | There is P such that ES(p) holds for every prime p>P. This is not full ES without a finite base. |
| ES-five | A positive word `tuv−u−v=p` has a 4-divisible slot among `t,u,v,tu−1,tv−1`; equivalent to a bichromatic forest edge. |
| `r(p)` | Least positive integer a with `(a/p)=−1`; necessarily prime by multiplicativity. |
| `Q_f` | `r(p)≪f(p)`. Its all-odd-prime version is stated separately where necessary. |
| `H4(p)` | Least maximum endpoint of a bichromatic edge in `uv | p+u+v`, infinity if none. |
| `J(p)` | Minimum `max(a,b)` over normalized unrestricted ES witnesses in the dictionary below, infinity if none. |
| `D(p)` | Minimum `max(x,y,z)` over ES witnesses, infinity if none. |
| `C(p)` | Minimum `max_i(x_i/p^{v_p(x_i)})`; includes the p-free denominator(s), not just the p-divisible ones. |
| `B(p)` | Minimum, over witnesses and their p-free denominators x, of the largest prime factor `P⁺(x)`. |
| `a_min(p)` | Minimum p-free window `e=4x−p>0`, allowing Type I or II. This is not H4 or J. |
| `ES-SEARCH`, `ES-PRIME-SEARCH` | Output any ES triple, on n≥2 or on prime inputs. Invalid inputs may be handled separately by primality testing. |
| `QNR-SEARCH` | On an odd prime p, output `1≤a<p` with `(a/p)=−1`. Output need not be prime or the least nonresidue. |
| FQ | The Type-I slice of `CONDITIONAL_ES` Lemma 1.1 has a witness with `t≤(log p)^A`, for one fixed A and every prime p≥5. |
| `H_BM^-` | For some ε>0 and P, `R(p)≥ε M_BM(p)` for p>P, with the exact R and main term of `FRONTIER` §2. |
| ES-square | `4/n=1/x+1/y+Q²/Z`, x,y,Z positive integers, Q odd, `(Q,nZ)=1`. |
| `ES^(S)` | ES-square with Q supported on a fixed finite set S of odd primes; n>1 coprime to 2S. |
| `e*(n)` | Cap in `CAP_POINTWISE`: the rational third denominator has reduced denominator r², r odd, `(r,n)=1`, `rad(r)|y`, and every `v_l(r)≤e`. ES iff e*=0. |
| `V_phi` | `4/n=Σ1/x_i` over `Z[phi]`, positive at phi=(1+sqrt(5))/2, mixed signs at its conjugate; odd n>1. It is a related variant, **not** literally a superset of positive rational ES witnesses. |
| H, Dickson, BH | Schinzel Hypothesis H for admissible irreducible integer polynomials; its positive linear-form case Dickson; Bateman–Horn's quantitative strengthening. Not Schinzel's separate Egyptian-fraction conjecture. |
| EH | For every θ<1 and A>0, the max-over-reduced-residue-class prime-distribution error summed over moduli ≤X^θ is `O_A(X/log^A X)`. |

**PROVED normalized dictionary (repo-known).** Every prime ES solution has exactly one or two p-divisible denominators. With `(a,b)=1`, positive a,b,c,k and `p∤abck`, it has, up to permutation, the form

```
Type I:  (ack, bck, pabc),    k(4abc−1)=p(a+b);
Type II: (abc, pack, pbck),   k(4abc−p)=a+b.
```

This is `notes.md` Theorem 17.1 / `POINTWISE_SIZE.md` §2, equivalent to Elsholtz–Tao, arXiv:1107.1010, Propositions 2.2 and 2.6. To recover a,b, take the two denominators with the **same** p-divisibility, divide both by p if necessary, and divide the resulting pair by its gcd. The remaining cofactor is abc; division by ab gives c, and division of the gcd by c gives k. No factoring is involved. In standard ET notation, these a,b are still the reduced pair; c,k here should not be confused with ET's other parameters.

## 2. Arrows with proofs and citations

### A1. Forest height → ES-five and least-QNR bounds

**PROVED; novelty: repo-known.** `H4(p)≤f(p)` implies ES-five(p), ES(p), `r(p)≤f(p)` and `a_min(p)≤2f(p)−1`. A bichromatic edge has a nonresidue endpoint, so its maximum endpoint is ≥r. The other implications are the five-slot identities; see `FOREST_H4.md` Propositions 3.1 and 3.4. On p≡1 (24), `H4≪log²p` would therefore prove the GRH-quality **numerical least-QNR bound** on that progression. The other p≡1 (4) progressions have nonresidue 2 or 3, so the numerical bound extends to all p≡1 (4). This does not establish a small least **positive** nonresidue bound on p≡3 (4); −1 is algorithmically cheap there but its positive representative p−1 is large.

**Assessment.** No reverse numerical implication from `r≪log²p` to H4 is known. A nonresidue endpoint need not have a parent: 11 is isolated at p=2521 (`LOWER_TAIL_ASTRA` Theorem 5.1). GRH supplies the sign, not attachment.

### A2. Universal character extraction; reduced parameters → least QNR

**PROVED; novelty: repo-known character lemma, new unrestricted extraction/height packaging.** For every normalized prime witness,

```
(ab/p)=−1;             additionally (c/p)=−1 in Type I.
```

Consequently `r(p)≤max(a,b)`, `r(p)≤J(p)`, and Type-I c≥r(p). Thus any strengthening giving `a,b,c≤f(p)` in the stated coordinates implies `r(p)≤f(p)`—not merely `f(p)^{O(1)}`. Bounding a alone, or an unspecified ratio of denominators, is not this assertion.

*Proof of the character assertion, included to expose the arithmetic input.* For Type II put `q=(a+b)/k=4abc−p≡3 (4)`. Since `(a,b)=1`, also `(a,q)=1`, and `ab≡−a² (q)` gives `(ab/q)=−1`. Reciprocity and `q≡−p (4ab)` give `(ab/q)=(ab/p)`: for the odd part this is ordinary quadratic reciprocity, and when ab is even, `q≡−p (8)` gives `(2/q)=(2/p)`.

For Type I set `D=4ack−p`, `D'=4bck−p`. They are positive (`bD=pa+k`) and

```
DD'=p²+4ck²,             D≡−p (4c),             gcd(D,2ckp)=1.
```

For every odd prime l dividing D, `−c≡(p/(2k))² (l)`, hence the Jacobi symbol `(-c/D)=1`. Reciprocity, `D≡3 (4)` and `D≡−p (4c)` give `(-c/D)=−(c/p)` (at 2, use D≡−p mod 8 if c is even). Thus `(c/p)=−1`. Reducing DD' modulo p in its two expressions gives `(ab/p)=(c/p)=−1`. This is exactly `notes.md` Lemma 77.6, not a new reciprocity theorem. ∎

**PROVED extraction.** At least one of a,b has negative symbol. Compute their symbols and return such an integer modulo p. Even the gcd is unnecessary for *some* nonresidue: the two p-adjusted same-type denominators are `ack,bck`, whose product has symbol `(ab/p)=−1`. Testing those two integers suffices. The gcd version additionally controls output height.

**Important correction.** Lemma CT says a p-free denominator **has a nonresidue prime factor**, not that the denominator itself has negative symbol: `4/5=1/2+1/4+1/20` contains the p-free square 4. The product identity, rather than attempting to factor that denominator, closes the algorithmic gap.

### A3. Actual denominator heights: a valid arrow and a false proposed strengthening

**PROVED; novelty: new explicit normalization audit, elementary.** Every prime witness satisfies

```
r(p) ≤ max(a,b) ≤ max(x,y,z)/p,
r(p) ≤ max_i(x_i/p^{v_p(x_i)}),
P⁺(x_i) ≥ r(p) for every p-free denominator x_i.
```

The first inequality uses A2. In Type II, a,b divide respectively y/p,z/p. In Type I, both a,b are at most `ab≤abc=z/p`. The last assertion is Lemma CT(a); the middle assertion follows from it. Therefore

```
D(p)≤p f(p)  ⇒  r(p)≤f(p),       C(p)≤Y  ⇒  r(p)≤Y,
B(p)≤Y      ⇒  r(p)≤Y.
```

**PROVED refutation of the polylog interpretation.** Nevertheless `D(p)≤p·(log p)^A` for every large prime is impossible, for every fixed A. Indeed every denominator is >p/4. In Type I, `4abc−1` is a positive multiple of p, since `p∤k`; hence

```
max(x,y,z) ≥ pabc ≥ p(p+1)/4.
```

In Type II, writing X=abc, Y=ack, Z=bck, one has `YZ=Xck²≥X>p/4`. Hence

```
max(x,y,z) ≥ p max(Y,Z) > p^(3/2)/2.
```

For p≥5 the Type-I bound is stronger. Also `C(p)>p/4` because at least one denominator is p-free. If “cofactor height” means only the cofactors of the p-divisible denominators, the same argument still bounds their maximum below by sqrt(p)/2. Thus **“polylog-height ES” must specify a reduced parameter height**: polylog C is false, as is polylog D/p. These cannot be presented as plausible GRH-strength strengthenings. The QNR-derived lower bound for D is valid but weaker than the elementary power lower bound.

**PROVED scope of a minimum-ratio claim.** For ordered x≤y≤z, `1/4<x/p≤3/4` automatically. A bounded smallest-denominator ratio has no such hardness content. Even a small additive p-free window does not control r: for each fixed H choose `M=24∏_{l≤H, l prime}l`, then a fixed prime s>H with s≡11 (12). CRT and Dirichlet give infinitely many primes `p≡1 (M), p≡−3 (s)`. They have r(p)>H, yet s divides `(p+3)/4` and s≡−1 (3), giving a Type-II window e=3. Explicitly take ET parameters `a=1,b=s,c=(s+1)/3,d=(p+3)/(4s)`. Thus a_min=3. This is the `FOREST_H4` Proposition 3.2 CRT template with its QNR consequence made explicit; no scalar bound `r≤F(a_min)` exists.

### A4. Graham–Ringrose → unconditional witness lower bounds infinitely often

**PROVED relative to Lau–Wu Proposition 5.1; novelty: repo-known transfer template, new J/B formulation.** There are a constant c>0 and infinitely many Mordell-hard primes p such that

```
r(p) ≥ c log p log log log p,
H4(p), J(p), B(p) ≥ c log p log log log p.
```

At each of those primes **every** Type-I c and every p-free denominator's largest prime factor obey the same lower bound. Also `D(p)≥c p log p log log log p`, but, as A3 explains, this last corollary is not an improvement on elementary height theory. Minima are infinity if the witness set is empty, so this theorem does not assume ES.

*Proof.* Lau–Wu construct primes `X^(1/2)<p≤X log X`, p≡1 (4), all primes through `δ log X log_3 X` quadratic residues. Their Proposition 5.1 applies at this upper endpoint y. Since log p≍log X, this gives the displayed bound. The conditions at 2,3,5,7 force p into Mordell's unit-square classes modulo 840. Apply A1–A3. ∎

**Verified citation.** Y.-K. Lau and J. Wu, “On the least quadratic non-residue”, *International Journal of Number Theory* **4** (2008), 423–435, Proposition 5.1, DOI 10.1142/S1793042108001432; archived primary text `sources/lit2026/lau-wu-least-quadratic-nonresidue.txt`, §1 and §5 read here. The underlying result is S. W. Graham–C. J. Ringrose, *Progress in Mathematics* **85** (1990), 269–309. Lau–Wu §1 also records the distinction: unconditional `log p·log_3 p`, versus Montgomery's **GRH-conditional** `log p·log_2 p` lower bound. The latter is not imported with a progression restriction not verified here.

**PROVED consequence.** O(log p) bounds for H4, J or B are ruled out. Exponents strictly between 1 and 2 are not ruled out by this result. Calling exponent 2 “sharp” on this basis is unjustified.

### A5. Efficient unrestricted ES → deterministic QNR finding

> **Status note (2026-10-21, OAI_DUMP_IMPACT.md).** If the OpenAI-release claim 003 (Lean-formalized, unrefereed; all Dirichlet L-functions zero-free for Re s > 7/8) holds, then r(p) ≪ (log p)^8 and deterministic QNR finding is in P (trial search). Claim 142 would give the same independently. A5 then stays a valid reduction but loses its hardness content: it no longer shows that efficient ES would solve an open problem.

**PROVED; novelty: new explicit unrestricted extension of a repo-known five-slice arrow.** There is a deterministic polynomial-time witness transformation

```
QNR-SEARCH ≤ ES-PRIME-SEARCH
```

with one oracle call and no factoring oracle. For p≡3 (4), output p−1. For p≡1 (4), obtain any ES witness and apply A2. All steps are gcd, exact division and modular exponentiation. Thus a deterministic poly(log p) ES algorithm at primes would solve the currently open deterministic polynomial-time QNR problem. A solver only on p≡1 (24) also suffices: use 2 for p≡5 (8), and 3 for the remaining p≡17 (24).

**PROVED size audit (folklore).** Every positive ES witness has O(log n) bits. Ordered x≤y≤z satisfy

```
x≤3n/4,
y≤2nx/(4x−n)≤2nx,
z=nxy/(4xy−nx−ny)≤nxy≤9n⁴/8.
```

The positive integer in the last denominator is ≥1. Thus “unrestricted witnesses” does not mean superpolynomial bit length. The transformation is polynomial in the ordinary input length even for an arbitrary valid oracle output.

**Scope.** This is not a reduction from factoring, does not find the *least* nonresidue, and does not necessarily output a *prime* nonresidue. Factoring an output to extract a nonresidue prime is a different problem. A mere existence theorem ES gives no running-time conclusion. Prior coverage: `CONSTRUCTIVE_ES` Proposition 4.1 and `BRAINSTORM/z31_complexity` only explicitly state the five-slice solver arrow; the needed general character identity was already in Lemma CT's proof.

### A6. QNR finding ↔ square roots over prime fields (algorithmic)

**PROVED / folklore-cited; novelty: folklore.** A deterministic polynomial-time QNR solver yields deterministic polynomial-time square-root extraction modulo primes on quadratic-residue inputs, by Tonelli–Shanks. Conversely a deterministic polynomial-time prime-field square-root solver yields QNR finding: start at a=−1 and, while `(a/p)=+1`, replace a by a square root. Its 2-power order doubles at each step, so after at most log₂p steps a is a nonresidue. For p≡3 (4) start already succeeds. This concerns prime moduli, **not** the factoring-equivalent square-root problem at composite moduli.

**Verified citation.** E. Jeřábek, “Integer factoring and modular square roots”, *J. Computer and System Sciences* **82** (2016), arXiv:1207.5220v3, Lemmas 3.2(ii), 3.11 and Theorem 3.12; the relevant HTML statements/proofs were read at https://arxiv.org/html/1207.5220v3 . His Lemma 3.11 uses the same order-doubling argument. His Theorem 3.12 already puts QNR finding in PPA unconditionally. Therefore an ES→QNR reduction is a useful **FP/derandomisation** constraint, not evidence that ES is outside PPA.

### A7. FQ → factoring-assisted polynomial-time ES search

**PROVED implication; CONDITIONAL on FQ; novelty: repo-known/folklore.** FQ implies `ES-SEARCH∈FP^FACTOR`. At a prime, test all `t≤(log p)^A`, factor `tp+1`, and find a divisor m with

```
m≡−1 (t),       m≡0 (4).
```

A dynamic program over residues modulo 4t builds divisors from the prime-power factors, keeping one representative divisor per attainable residue. There are 4t states and polynomially many prime-power choices in log p; store predecessors to reconstruct m. Its complementary divisor is automatically −1 modulo t. Apply `CONDITIONAL_ES` Lemma 1.1. On composite n, use FACTOR to select a prime divisor, solve it and scale. Small primes are explicit.

**Correction retained from the old memo.** Enumerating *all divisors* is not polynomial in log p in the worst case. Residue DP is what makes this particular small-modulus search polynomial. FQ does not follow from the availability of factorisation. Combining A5 and A7 only gives QNR in `FP^FACTOR`, not unconditional FP. The heuristic NFS runtime is not an unconditional complexity bound.

**PROVED, literature-cited per-slice algorithm; novelty: repo-known.** Lenstra's divisors-in-a-residue-class algorithm enumerates the divisors of N congruent to a coprime residue modulo s in polynomial time when s>N^(1/3); Coppersmith–Howgrave-Graham–Nagaraj reach s≥N^α for fixed α>1/4. See the exact abstract statements and citations in `BRAINSTORM/z31_complexity.md` §(a): Lenstra, *Math. Comp.* **42** (1984); CHN, *Math. Comp.* **77** (2008). Thus a B2 slice in that range is efficiently decidable without factoring. The output may be the empty list: these are solved **enumeration** problems, not an existence theorem or a polynomial bound on the number of slices needed.

### A8. Feasible formal proofs and TFNP classes

**PROVED equivalence; novelty: folklore/repo-known.** With the explicit O(log n)-bit bound in A5 and the polynomial-time identity verifier,

```
ES is true  ⇔  ES-SEARCH is a total polynomially balanced NP search relation.
```

Thus membership in TFNP is **conditional on ES**, not an unconditional theorem. The prime-input formulation may be made total on all bit strings by returning an invalid-prime flag on nonprimes.

**CONDITIONAL metatheoretic arrows; novelty: folklore/repo-known.** A proof of the bounded ES assertion in `S^1_2` yields an FP witness function by Buss witnessing, hence deterministic QNR by A5. A proof in `T^1_2` yields a reduction to PLS; it does **not** yield FP. The S¹₂ witnessing theorem is cited from S. Buss, *Bounded Arithmetic* (1986), **memory, not reverified here**. The T¹₂/PLS characterization is verified in the authors' abstract: S. Buss–J. Krajíček, “An application of Boolean complexity to separation problems in bounded arithmetic”, *Proc. London Math. Soc.* **69** (1994), 1–21, https://mathweb.ucsd.edu/~sbuss/ResearchWeb/Si2Ti2sep/index.html . These are hypothetical proof-shape implications; no such proof of ES is supplied.

**Assessment.** No unconditional ES membership in PPP, PPA or PLS is established in the cited campaign. A genuinely polynomially encoded parity/pigeonhole/local-search reduction would give the corresponding membership by definition; naming an involution or a pigeonhole argument is not a reduction. The formal finite-menu obstruction does not exclude all such reductions. Nor does a large numerical witness modulus imply a running-time lower bound: its bit length may be small (`logic_complexity` erratum).

### A9. Standard least-QNR bounds: direction and terminology

**PROVED / CONDITIONAL as indicated; novelty: folklore-cited.** Burgess gives unconditionally

```
r(p) ≪_ε p^(1/(4 sqrt(e))+ε),       1/(4 sqrt(e))≈0.15163.
```

GRH for quadratic Dirichlet L-functions gives `r(p)≪log²p` (Ankeny). These are verified as statements in Lau–Wu §1, equations (1.3), (1.5); their bibliography gives Ankeny, *Annals of Mathematics* **55** (1952), 65–72, and Burgess, *Mathematika* **4** (1957), 106–112; *PLMS* **13** (1963), 524–536.

**Terminology correction.** Vinogradov's least-nonresidue conjecture is `r(p)≪_εp^ε` for every ε>0. A polylog bound is stronger; exponent 2 matches the standard GRH consequence. Neither a polylog bound nor deterministic QNR finding is known to imply GRH. A1's numeric implication has p≡1 (4) scope; A5's algorithmic implication covers all odd primes because a large positive representative of −1 is sufficient algorithmically.

### A10. Finite proof menus → contradictions to H/Dickson, with exact scope

**PROVED implications; novelty: repo-known.** Distinguish three classes rather than calling every finite-looking argument a congruence cover.

1. **Fixed finite ET congruence/identity menu.** It cannot cover all primes, **unconditionally**. For its finitely many reduced pairs a,b, take L divisible by 24 and every `8ab`. At primes p≡1 (L), all prime factors of ab are quadratic residues, whereas each certificate requires `(ab/p)=−1`. Dirichlet supplies infinitely many such primes. More general polynomial-identity covering formulations are subject to the classical Mordell–Schinzel square-class obstruction, as cited by Elsholtz–Tao following Proposition 1.6. This is stronger than the vacuous arrow “such a cover would refute Dickson”. Arbitrary finite English descriptions or algorithms with growing searches are not fixed menus.

2. **Bounded formal programs allowing factorisation.** For the precise ring/floor/sign/size/factorisation language and a finite defined formal run at a nondegenerate square-mimicking point, `POINTWISE_SIZE` Theorem C proves

   ```
   H for the finite polynomial family attached to the program
       ⇒ infinitely many prime inputs where that correct program fails.
   ```

   Contrapositively, universal success of this *specified program* refutes that instance of H, hence universal H and BH. It refutes Dickson **only when the required irreducible factors are all linear**. H failure does not logically imply Dickson failure. The formal-run hypotheses and the p-independent bound cannot be dropped.

3. **Fixed roots or bounded windows.** `LOWER_TAIL_ASTRA` Theorem 3.2 proves, under Dickson, that for every fixed H infinitely many p≡1 (24) have every component meeting {1,…,H} monochromatic—even after unrestricted component exploration. The explicit admissible forms are `p=1+Mk`, `L_i=1+Mk/(i+1)`, with `24` and every `i(i+1)` dividing M. All equal 1 at k=0; for primes dividing M choose k=0, and for primes not dividing M the number of forms is smaller than the prime (M contains every prime ≤H+1). The factorisations `p+i=(i+1)L_i` isolate roots ≥4 and freeze the component of 1. Theorem 5.1 also defeats the **least-QNR root** under the two-form Dickson instance `p=2521+9240a`, `(p+11)/12=211+770a`. Already p=2521 is an actual isolated-root counterexample.

   `CAP_BOUNDED` Theorem 1.3 similarly gives infinitely many p with **no** certificate at any cap in any p-free window m≤M. Its forms are `Lt+1` and `L t/(m+1)+1`, with the lcm/valuation divisibility specified there; their simultaneous primality makes every generator in each window a residue. Universal success with any fixed window bound therefore implies ¬Dickson. This includes unrestricted ordinary ES if it promises a bounded p-free window, not arbitrary searches with a bounded exponent cap but unbounded windows.

**Assessment.** The last two are meaningful pruning counterfactuals because the infinite-family obstruction uses a famous conjecture. They do not say ES itself would refute Dickson. Fixed-root strategies may already have finite counterexamples; Dickson strengthens this to infinitely many failures. All three conclusions leave growing, p-dependent menus open.

### A11. Lower-tail count → eventual ES; two-sided count → a false statement

**PROVED; novelty: repo-known.** `H_BM^- ⇒ eventual (star) ⇒ eventual ES`, since `M_BM(p)≥(3/(16π²)−o(1))log²p` unconditionally. A finite census covering the resulting threshold is an additional premise for full ES. Sources: `BM_CORRECTED_COUNT` Theorem 2.2/§3.1; `FRONTIER` §2.4. No standard conjecture is known in this campaign to imply this lower tail; the candidate arrow is not a theorem from GRH, EH or Hooley R*.

**PROVED refutation, relative to Linnik; novelty: repo-known.** The two-sided assertion `|R−M_BM|≤(log p)^A` for all sufficiently large p, for any fixed A, contradicts Linnik's theorem. Let Q be the product of the first k primes ≡3 (4), choose `p≡−1 (Q), p≡1 (4)` with `p≪(4Q)^L`. Every divisor d|Q having an odd number of factors gives a distinct triple `(u,B,C)=(1,(p+1)/d,(d+1)/4)`. Thus `R(p)≥2^(k−1)` while `log p≪k log k`, whereas `M_BM≪log²p`. See `BM_CORRECTED_COUNT` Proposition 3.1. This is not merely a “would require better prime distribution” warning: the two-sided source is false.

**Assessment / exact absent arrow.** No reduction from H_BM^- to a least prime in every progression, a least prime ideal in an arbitrary ray class, or another famous lower-tail conjecture is established. A count without witness-location control gives no prescribed Frobenius/class witness in those other problems. The parallel words “lower tail” and “class” do not construct a reduction. `CONDITIONAL_ES` §§3–5 and `SINGLE_P_COUNT` §4.2 explain the failed *mechanisms*, not logical non-implications.

### A12. Least forced prime → a cap; GRH/Linnik go upward into relaxations

**PROVED; novelty: repo-known.** For p≡1 (4), let q*(p) be the least prime

```
q≡4−p (8),       (q/p)=−1.
```

Then `r(p)≤q*(p)` and `e*(p)≤q*(p)−3`, by `CAP_POINTWISE` Theorem 1.1. The proof takes K=(p+q)/4; its prime factors generate −1 modulo q, and reducing exponents modulo their orders produces a square-numerator certificate. It does not give cap zero.

**PROVED relative to Linnik / CONDITIONAL on GRH; novelty: repo-known.** Linnik bounds a prime in one suitable reduced class modulo 8p, giving `q*≪p^L` and a polynomial cap. Effective Chebotarev under GRH in `Q(i,sqrt(2),sqrt(p))`, discriminant `2^16p^4`, gives `q*≪log²p` and `e*≪log²p`. For general odd n use the squarefree part and the scaling argument of `CAP_POINTWISE` Corollary 1.2/Theorem 1.3. The primary GRH input is Lagarias–Odlyzko, “Effective versions of the Chebotarev density theorem”, in *Algebraic Number Fields* (1977); the repository's precise theorem/citation audit is in `CAP_POINTWISE` §1. We use no explicit numerical constant requiring a fresh Bach–Sorenson audit.

**What is genuinely a least-prime statement.** A strengthening *requiring* q*≤Y implies that bound for this one Frobenius class (and r≤Y). It does not imply Linnik's theorem for arbitrary moduli/classes. Conversely a general least-prime theorem implies such a q* bound. Ordinary small ES parameters provide a nonresidue prime existentially, but do not prescribe its class 3 modulo 4, much less an arbitrary AP. No reverse least-prime-in-AP arrow is supplied.

### A13. Dirichlet → ES-square; flat power ladder

**PROVED relative to Dirichlet; novelty: repo-known.** For odd nonsquare n, choose a prime r≡3 (4) with `(n/r)=−1`. Such a reduced progression exists. Choose odd Q coprime to n with `4Q²≡−n (r)` and set `e=(n+4Q²)/r`. Then

```
x=(n+e)/4,    y=n(r+1)/4,    z=nx(r+1)/(4Q²)
```

satisfy `4/n=1/x+1/y+1/z`, with x,y positive integers. On reducing z its denominator is an odd square: if l|Q and `v_l(r+1)<2v_l(Q)`, then `v_l(x)=v_l(r+1)`, so the negative valuation of z is even; otherwise it is nonnegative. This proves ES-square. Even n and odd squares follow by an explicit even identity or scaling from a nonsquare divisor with Q chosen coprime to n. Sources: `UNIT_ORBIT_ES` Proposition 2.1; `FIXED_MODULUS_SHOTS`; `POWER_LADDER_ES` Corollary 2.5.

**PROVED, repo-known.** Allowing any fixed power Q^k in the third numerator in lowest terms gives a theorem for every k, not an intermediate unproved ladder to ES (`POWER_LADDER_ES` Theorems 2.1, 2.3). There is no proved transport back to Q=1. The numerator-8 failures also admit the square relaxation, so threshold-free numerator-uniform transport is false.

### A14. Artin/GRH → one mute prime; sieve → four

**PROVED implications; novelty: repo-known.** For a fixed odd prime s and odd nonsquare n coprime to s, the following **precise Artin–Chebotarev assertion** suffices:

```
There is a prime r≡3 (4), (n/r)=−1,
with [F_r^*: <s>] dividing 2.
```

Then `<s²>` is the whole square subgroup (of odd order), contains −n/4, and A13's construction works with Q=s^j. This proves `ES^({s})(n)`. The condition is sufficient, not necessary. The ordinary assertion “s is a primitive root infinitely often” does not by itself prescribe the simultaneous n-dependent Frobenius condition.

**CONDITIONAL on the requisite Kummer-field GRH; repo-known citation-level input.** `FROBENIUS_FIRING` Theorem 4.4 verifies compatibility and obtains the needed primes by Hooley–Lenstra; after scaling, one mute prime suffices for every odd n>1 coprime to s. Cite H. W. Lenstra, “On Artin's conjecture and Euclid's algorithm in global fields”, *Inventiones Mathematicae* **42** (1977), with the compatibility criterion of Corollary 4.8 used in the repository. Interpret GRH broadly enough for the Kummer fields and fixed cyclotomic composita in that application; do not substitute Dirichlet-only GRH for this rank-one Artin input.

**PROVED unconditionally relative to BV and the linear sieve; repo-known.** `UNIT_ORBIT_ES` Theorem 2.4/Corollary 2.5 prove `ES^(S)` for |S|≥4 and every n>1 coprime to 2S. The sieve finds many primes with `(r−1)/2` rough; multiplicative independence bounds the primes where the S-image is too small. These prime averages are over auxiliary r with n **fixed**, and a single suitable r suffices. This is not the forbidden average-over-input-p inference.

### A15. EH → two fixed mute primes (and the general level/rank inequality)

**PROVED implication, CONDITIONAL arithmetic conclusion on EH; novelty: new-to-repo elementary extension.** Suppose prime distribution has level θ in the max-over-residue-class sense, with arbitrary logarithmic savings. For a fixed set S of k≥2 odd primes, if

```
θ > 2/(k+1),
```

then `ES^(S)(n)` holds for every n>1 coprime to 2S. In particular **EH implies the two-mute-prime relaxation** (choose θ>2/3). This is a relaxation theorem, not an implication into ES.

*Proof.* The case n≡3 (4) is immediate from Q=1. For nonsquare n≡1 (4), choose exactly as in `UNIT_ORBIT_ES` Theorem 2.4 a fixed reduced class a modulo `M=4 rad(n)` such that a≡3 (4), `(n/a)=−1`, and a≢1 modulo every odd prime divisor of M. There is a prime l₀≥5 occurring to odd valuation in n, so these conditions can be chosen by CRT while avoiding the residue 1.

Apply the dimension-one lower-bound sieve to primes r≡a (M), removing prime divisors of `(r−1)/2` below `z=X^α`, where

```
1/(k+1) < α < θ/2.
```

The input level for sieve moduli d is `X^θ/M`; since M is fixed, the sieve parameter tends to θ/α>2. The assumed distribution bound therefore gives `≫_{n,α} X/log²X` such primes r≤X. Primes dividing M are already excluded from `(r−1)/2`; discard the finite set S.

Let Γ_r be generated by S modulo r. If its index has an odd prime factor, that factor is ≥z, hence `|Γ_r|≤X^(1−α)`. The elementary collision bound `UNIT_ORBIT_ES` Lemma 2.3 gives

```
#{r: |Γ_r|≤X^(1−α)} ≪_S X^((1−α)(1+1/k)) = o(X/log²X),
```

since α>1/(k+1). Some remaining r therefore has index 1 or 2 (r≡3 mod 4), so Γ_r contains all squares and Γ_r² is exactly the square subgroup. Since `(n/r)=−1`, −n/4 is a square; choose Q supported on S with `4Q²≡−n (r)` and use A13. For square n, scale a solution for a nonsquare divisor; scaling is coprime to S and preserves reduced even negative valuations. ∎

**Assessment / novelty audit.** This replaces the exponent 1/4 in the repository's existing BV proof by θ/2. It recovers k≥4 from θ=1/2, gives k≥3 from any θ>1/2, and k≥2 from θ>2/3. The inequality cannot reach k=1 even at θ arbitrarily close to 1, so it does not silently prove the one-generator Artin theorem. No external priority claim is made, and numerical tests cannot certify EH; the proof uses the same standard linear-sieve statement explicitly cited in `UNIT_ORBIT_ES` Lemma 2.2: Friedlander–Iwaniec, *Opera de Cribro*, Theorem 11.13 (equivalently the cited Halberstam–Richert Theorem 8.4), with sieve parameter greater than 2.

### A16. GRH → V_phi; what EH and Hooley R* do not currently supply

**CONDITIONAL on Kummer-field GRH; novelty: repo-known.** `UNIT_ORBIT_ES` Theorem 5.2, using Lenstra's criterion, proves that every odd n>1 outside

```
T={m²,5m² : m odd}
```

is solved by the golden-unit orbit, hence satisfies V_phi(n). This includes every odd prime other than 5. The statement is about **orbit-solvability**; T is not claimed to be the full failure set of V_phi, whose mixed/scaled solutions can survive there. The same source Theorem 5.1 gives unconditionally at most `O(X^(3/4)log²X)` non-orbit-solved odd inputs up to X.

**PROVED existing relaxations, not new conjectural arrows.** `FOREST_H4` Theorem 3.5 gives the five-slice result `H4≤h(p)` for almost all p≡1 (24) for every h→∞. A different result, `FORCED_WINDOW` Theorem 8.5 as recorded in `BOARD2_SLATE` §(2), gives general Type-II witnesses at moving prime windows, with exceptional bound `O(X/(log X)^(4/3−2α−ε))` for `0<α<1/6`; these are not asserted to lie in the five slices. The long-CF relaxation `λ(p)≤(6/π²)log p log log p+O(log p)` is already unconditional (`BOARD2_SLATE` §(1), from Aistleitner–Borda–Hauke arXiv:2210.14095v2, Theorem 1). No standard-conjecture implication to **every-prime** five-slice existence was located. None of these almost-all statements may be turned into a pointwise result.

**Assessment.** Hooley R* (Kloosterman-sum cancellation) is not Hooley's GRH proof of Artin. `SINGLE_P_COUNT` §4.2 finds no R*→ES or R*→every-prime five-slice arrow: its complete/modulus-averaged sums do not match the divisor-restricted single-p sum. EH does have the precise relaxation arrow A15, but not an established ES arrow. GRH bounds the BM main term and caps, not cap zero. No implication from a Chowla sign-correlation conjecture to this divisor-class event is established by the harvest.

### A17. Numerator scaling and Schinzel/Sierpiński

**PROVED; novelty: folklore.** Write `E_k(n)` for a positive three-term representation of k/n. For every positive integer d,

```
E_k(n) ⇒ E_k(dn),
E_(dk)(n) ⇒ E_k(n),
E_k(n) ⇔ E_(dk)(dn).
```

The first two arrows multiply all denominators by d; the last equates the rational numbers. Thus ES gives representations for 2/n and 1/n, which are already elementary; a representation of 2/n in three terms does **not** give 4/n in three terms by this scaling. Also `ES(n)⇒E_5(n)` is not a scaling identity. Adding `1/n` gives a **four-term** representation of 5/n, not Sierpiński's three-term assertion.

**PROVED implication; novelty: folklore.** Schinzel's Egyptian-fraction conjecture, “for every k there exists N(k) such that E_k(n) for all n≥N(k)”, implies eventual ES and eventual 5/n by specialization. It does not alone resolve the finite small-n assertions ES for n≥2 or Sierpiński for n≥2. Conversely ES settles only k=4 (and downward divisor numerators), not all k. No arrow between full ES and full Sierpiński 5/n was located. No arrow between either and sums of three cubes was located. `BRAINSTORM/z31_integral_points_cubics.md` labels three cubes an **analogue**, not a reduction: its height is unbounded, whereas all positive ES witnesses lie in the polynomial box A5.

### A18. Positive integral Hasse principle on the ES family ↔ ES

**PROVED relative to Bright–Loughran; novelty: repo-known/tautological specialization.** Let HP_ES assert, for every n≥2, that nonempty positive-real/integral-finite-place Brauer–Manin set on

```
U_n: 4xyz=n(xy+yz+zx)
```

implies a positive integral point. Bright–Loughran prove that this BM set is nonempty for **every** n≥2. Consequently `HP_ES ⇔ ES`. This is the exact positivity/model-specific statement; an unspecified “integral Hasse principle for log K3” is not a theorem that can be plugged in. A hypothetical theorem covering precisely these models and real components would imply ES by specialization, but merely invoking the geometric class does not supply that theorem.

**Verified-in-repo external citation.** M. Bright–D. Loughran, arXiv:1908.02526, Theorems 1.1/1.8 (no BM obstruction), 1.9 (BM does not explain strong approximation). See `CONDITIONAL_ES` §7.4 and `BRAINSTORM/z31_integral_points_cubics.md`. Generic BM-only integral principles have counterexamples on related affine cubic families; neither their failure nor their successes are an implication between ES and three cubes. A counterexample to ES would be a non-BM integral failure on this particular family, not a contradiction to the no-obstruction theorem.

### A19. A genuine exception-propagation law → ES by Vaughan

**PROVED relative to Vaughan; novelty: repo-known.** Suppose every exceptional prime p₀ generates a subset F⊆E with

```
F(N) ≥ N exp(−o((log N)^(2/3))) infinitely often.
```

Then ES follows, since Vaughan's `E(N)≪N exp(−c(log N)^(2/3))` contradicts that inequality. Likewise a law sending every exceptional prime to a larger exceptional prime at nondecreasing gap `f(p)=exp(o((log p)^(2/3)))` suffices: an iterated chain has at least `(N−p₀)/f(N)−1` members up to N. These are `AMPLIFY_EXCEPTION` Theorems 1.1, 1.3(c). A smaller exceptional input would suffice by minimality alone. External input: R. C. Vaughan, “On a problem of Erdős, Straus and Schinzel”, *Mathematika* **17** (1970), 193–198, DOI 10.1112/S0025579300002886; the bound is checked through the repository's cited secondary literature, not a fresh reading of Vaughan's inaccessible primary PDF.

**Assessment.** These arrows use a famous *solved* exceptional-set bound; they do not make propagation easier than ES. `PROPAGATION_CLOSURE` leaves no constructed propagation law outside a witness-dependent divisibility gate. A proof shape with a valid density-amplifying law would prove ES, not a new famous open prime-distribution theorem. Fixed bounded branching at power-increasing scales does not meet the necessary counting threshold.

## 3. Pruning corollaries

**PROVED implications / Assessment of proof design.** This is the actionable table; “must solve” means the stated consequence, not a claim that all proofs take this shape.

| Proposed strengthening or shape | What it would also establish | Novelty / status |
|---|---|---|
| H4≪log²p on hard primes | Least-QNR `r≪log²p` on p≡1 (4), plus ES-five | Repo-known; open antecedent |
| Reduced pair max(a,b)≪f(p) for every prime | `r≪f(p)` on that domain | New packaging of CT; no converse |
| All p-free denominator prime factors ≤f(p) | `r≤f(p)`; impossible for f=O(log p) | Repo-known CT + transferred lower bound |
| Max denominator ≤p·polylog(p), or all p-free cofactors polylog | Already contradicted by A3, before QNR theory | New explicit audit; **discard** |
| Deterministic polynomial-time arbitrary ES witnesses | Deterministic polynomial-time QNR and prime-field square roots | New unrestricted reduction; open derandomisation consequence |
| S¹₂/PV-style feasible witnessing proof | Same FP consequence, provided the witnessing hypotheses hold | Folklore theorem + A5 |
| T¹₂ proof / explicit local search | PLS membership only, not FP | Folklore; no proof supplied |
| Fixed finite ET cover | Contradicts Dirichlet + T1 unconditionally | Classical/repo-known; **discard** |
| Universal bounded formal factorisation program | Refutes its finite Schinzel-H instance; Dickson only in the linear case | Repo-known; exact program scope |
| Fixed forest roots / bounded p-free windows | Refutes specified Dickson prime-tuples instances | Repo-known; fixed-root examples already fail |
| Pointwise two-sided polylog asymptotic for R | Contradicts Linnik's theorem | Repo-known; **discard** |
| Pointwise one-sided BM lower bound | Eventual ES, **no established extra famous open consequence** | Repo-known; B2 remains |
| Positive integral BM sufficiency on U_n | Exactly ES itself | Repo-known; not an easier geometric theorem |
| Density-amplifying exception transport | ES by Vaughan; no new prime theorem required | Repo-known; no transport constructed |

**Assessment.** The best non-vacuous famous-open-problem pruning is **efficient arbitrary ES ⇒ deterministic QNR**. Height comparisons provide a second quantitative constraint only when the height has been normalized meaningfully. H/Dickson contrapositions apply to particular successful restricted programs, not “a proof of ES” in general. A15 is a useful converse-direction calibration: standard conjectures readily solve enlarged search spaces while leaving exponent cap zero untouched.

## 4. What is not implied, and finite verification

### 4.1 Honest gaps

**Assessment (absence of established reductions, not independence claims).**

- ES existence does not currently give deterministic polynomial-time search, a subpower least-QNR bound, or factoring. Its O(log p)-bit certificates alone are not an FP algorithm.
- The unrestricted QNR extraction removes the **factoring of denominators** caveat, but not the problem of finding an ES witness. It gives arbitrary integer nonresidues, not small or prime nonresidues by default.
- Small integer nonresidues, even on GRH, do not force a divisor into the ES target class. Neither a forced-window prime nor H4 is known bounded by a function of r of useful size merely from the available theorems.
- `a_min≪log p` is not known to imply a least-QNR bound. A3 even separates fixed a_min=3 from arbitrarily large r. This does not disprove every conceivable global implication between uniform assertions.
- GRH-quality numerical consequences do not imply GRH. A1 alone does not cover numerical least-positive-QNR bounds on p≡3 (4); A5 covers their **algorithmic** problem trivially with −1.
- The least prime in a specific quadratic Frobenius class is not a least prime in an arbitrary residue class/ray class. A12 keeps the quantifiers distinct.
- No reverse ES→ES-five arrow is known. No H_BM^-→famous ray-class/Linnik strengthening is established. Conversely no GRH/EH/R*/Chowla→H_BM^- arrow is established.
- Plain Artin infinitude is not an Artin–Chebotarev theorem with all the prescribed compatibility conditions. A14 explicitly states what is needed; A15 uses EH instead, with a proved level/rank inequality.
- ES-square, capped ES and mute variants are not ES until an integrality/exponent-budget transport is proved. V_phi has different real signs and is not literally a relaxation by inclusion.
- No ES↔Sierpiński, ES↔three-cubes or ES↔factoring equivalence is asserted. Nor does Schinzel's eventual-k assertion automatically include its unknown finite base for k=4.
- The no-BM-obstruction theorem is not integral BM sufficiency. Fixed-input positive integral points remain the entire issue.
- A large value of a minimal modulus or parameter is not an unconditional lower bound on adaptive algorithm time.

### 4.2 CERTIFIED finite audit of the new extraction

Existing `scripts/pointwise_size_ct_check.py` already checks CT prime-factor assertions and verifies its complete unordered-triple enumeration against a separate brute-force routine. Rather than duplicate that test, the new script imports its enumerator and checks the **new factor-free extraction and height corrections**. It retains only one prime's solutions at a time. The extraction function itself uses no factorisation; the independent production of all test witnesses does.

**CERTIFIED:** all 80 primes p≡1 (4) through 1000, plus 1201,2521,3361: **83 primes, 2,113 unordered witnesses**, consisting of **1,421 Type I and 692 Type II**, zero violations. Every witness passes the rational identity by integer cross-multiplication, primitive parameter recovery, the opposite-symbol pair test, `p·extracted_QNR≤max denominator`, and `4(max denominator)²>p³`.

| p | Number of unordered witnesses | Minimum max denominator | A minimizing triple | Extracted QNR |
|---:|---:|---:|---|---:|
| 193 | 6 | 4,825 | (50,1930,4825) | 5 |
| 409 | 15 | 12,270 | (105,5726,12270) | 7 |
| 577 | 18 | 167,330 | (145,33466,167330) | 5 |
| 1201 | 11 | 46,839 | (312,9608,46839) | 39 |
| 2521 | 9 | 804,199 | (638,55462,804199) | 29 |
| 3361 | 15 | 571,370 | (850,84025,571370) | 34 |

**Scope.** The QNR can be composite (39,34). This is deliberate, and suffices for the derandomisation arrow. The table is not a new large-scale ES verification or evidence for a pointwise height bound. The known (star) failures 409,577 do not affect extraction from unrestricted witnesses. Existing numerator-8 and square controls are not redundantly rerun: no extraction theorem asserts existence there, and T1 excludes normalized prime-like square data.

**Reproduce:**

```sh
ulimit -v 2000000
timeout 180 uv run python scripts/z47_hardness_map_check.py
```

Output: `data/z47_hardness_map/check.json`. The keyword harvest records the pre-document repository search and includes reviews/errata; it must not be read as an endorsement of every matched claim. External source statements specifically rechecked here are Lau–Wu §1/Proposition 5.1, Jeřábek Lemmas 3.2/3.11/Theorem 3.12, and the Buss–Krajíček author abstract. Other external inputs are identified through their precise reviewed repository citations, or explicitly marked memory.

### 4.3 Is there a new theory?

**Assessment.** No new arithmetic framework is claimed. The useful organizing object is a **resource-labelled witness reduction**: input domain, output relation, height measure, bit complexity, and oracle access are separate coordinates on an arrow. The first theorem such a framework needs is a factor-free map from arbitrary ES witnesses to a familiar search problem; A2/A5 provide exactly that elementary toy. The 2,113-witness audit checks the map. The missing converse would have to convert a nonresidue into an actual divisor-class hit; it is B2, not supplied by the framework. A15 independently tests the “more resources” side by explicitly trading prime-distribution level for number of mute generators.

## 5. FRONTIER §4 cross-reference

**Assessment.** PASS means an implication is correctly scoped, not that this document supplies a proof of ES. FAIL below identifies the missing existence step in a tempting reverse/transport arrow.

| Line | Result | Reason |
|---:|---|---|
| 1 | PASS | A2 explicitly uses a negative quadratic symbol; normalized square data cannot satisfy it. Scaled/mixed square solutions are not excluded. |
| 2 | PASS | No existence is inferred for 8/131 or 8/241. Their square relaxations refute unrestricted numerator-uniform transport. |
| 3 | PASS | Only exact numerator scaling A17 is used; no uniform recombination law. |
| 4 | FAIL for reverse arrows | QNR→ES, cap→cap-zero and main-term→occupancy still need the moving divisor class. No theorem here bridges it. |
| 5 | PASS | Extraction is at one p; Lau–Wu is explicitly i.o. Auxiliary-prime averaging in A14/A15 keeps n fixed. Almost-all five-slice results remain almost-all. |
| 6 | PASS / N.A. | No power-main-term ES detector. The mute relaxation's sieve counts auxiliary primes, not a bounded-multiplicity ES family. |
| 7 | PASS | A11 explicitly prunes the false two-sided assertion and keeps only a one-sided hypothesis. |
| 8 | PASS for the map; FAIL for bounded proof shapes | A10 states finite-run/menu hypotheses exactly, with the correct H-versus-Dickson distinction. |
| 9 | FAIL for QNR→certificate | Parity is extractable, but it does not determine the divisor class. This is the explicitly missing converse. |
| 10 | PASS | No pooling of large prime divisors across shifts. |
| 11 | N.A. | No signed reflection argument; V_phi's different sign model is not transported back. |
| 12 | FAIL for transport | A12–A16 stop at their relaxations. No integrality transport is asserted. |
| 13 | PASS | HP_ES is identified as equivalent to ES, not justified by BM nonemptiness. |
| 14 | PASS, finite audit | 193,409,577,2521,3361 enter the unrestricted extraction audit; no one-line universal solver is claimed. |
| 15 | PASS, theorem scope | A4's infinite lower-bound sequence lies in Mordell's square classes. The algebraic extraction needs no near-square exclusion. |
| 16 | N.A. | No thin-family success is transferred to all primes. |
| 17 | N.A. / FAIL if used to force ES | No transparent coset cover is claimed. Exponent-unrestricted subgroup success in A15 is not cap-zero box coverage. |

**Final Assessment.** The new useful entries are A5's unrestricted, factoring-free search reduction, A3's rejection of a misleading height normalization, and A15's EH/two-mute implication. The classical/repo-known arrows remain valuable only with their domains, height measures, and hypotheses attached. There is still no standard-conjecture proof of ES in this map and no reduction making plain ES equivalent to another famous open problem.
