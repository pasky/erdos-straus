# NONET_STEP — a genuine mixed-square hit, but not a propagation law

## 0. Summary

**PROVED:** the board's literal non-ET-step test has a positive answer. From the coordinate witness `(4,68,510) ∈ W₄(15)` at **289=15²+8²**, extracting the coprime ratio `1:17` and applying the exact-division rule below produces **`(73,7446,126582) ∈ W₄(289)`**. Its 17-adic valuations are `(0,1,2)`; it is not a scaling of a solution at 17, or at any proper divisor of 289. The same rule produces the known smallest-window solution at **3361**, using `(15,406,435) ∈ W₄(56)` and 3361=56²+15². An infinite mixed-square family verifies that square survival is not an isolated normalization accident. **CERTIFIED:** a broader, explicitly finite grammar succeeds at 536/542 tested primes but fails completely at 2521, 9601, 53881, 54121, 88321, 94441, even after examining every coordinate witness. Its integrality condition remains a target-dependent divisor gate. **Assessment:** the literal drop-condition is met, but it is too weak to reopen a B2-free proof route. The source-ratio operation is already implicit in board #4's argon-3; the addition here is its honest composite normalization, coordinate-source experiment, and rigorous separation from scaling.

**Verdict: PARTIAL, promise 1/5.** A non-ET coordinate-witness step exists; the missing implication is **source-fibre nonemptiness ⇒ some integral recombination at every target prime**. The tested grammar does not satisfy that implication. ES remains open.

## 1. Setup, prior coverage, and the exact meaning of ET form

**Definition.** `W_k(n)` is the finite set of unordered positive triples solving `k/n=1/x+1/y+1/z`. For an odd primitive representation

    n=a²+b²,  a>b≥1,  gcd(a,b)=1,
    Q(n)={a,b,a+b,a−b}∩[2,∞),

all sources are below n. At primes p≡1 (8), these are Astra's Gaussian-coordinate sources. At squares, use primitive Pythagorean representations, not `(m,0)` or a common-coordinate scaling. The experiment uses the Gaussian identity `(a+ib)(a−ib)=n` only through its integer norm; it does not search Gaussian prime factors.

**Prior results, not new claims.** Read in full: `FRONTIER.md`, `BRAINSTORM/README.md`, `BREADTH_Z45.md` (especially §§5–7), `AMPLIFY_EXCEPTION.md`, `NONCONG_LIFTS.md`, and the subsequently available `PROPAGATION_CLOSURE.md`. Also read board #4's memo, all three items files and all nine rounds under `~/.pi/boards/20261019-es-propagation/`. Relevant predecessors:

- `AMPLIFY_EXCEPTION` Thm 2.3: the square screen requires **ET normalization at the square**; Thm 2.4 is a no-free-lunch observation, not an impossibility theorem.
- `NONCONG_LIFTS` Thm 1.2: congruence-mediated fixed slices have a witness-dependent divisibility gate; its hypotheses do not classify arbitrary maps.
- `BRAINSTORM/README.md`, s7 and z35: norm-coordinate identities/windows, square budgets, and their null pairing tests were already tried. No novelty is claimed for using a Gaussian representation or completing two unit fractions.
- Board `items/argon.md`, argon-3: a source-pair ratio `(r,s)` gives `H=nX(r+s)/((kX−n)rs)`. Its prime-only divisor split was incorrectly extended to squares. Astra's rounds 01 and 03 refuted both square patches with **non-coordinate** sources 23 and 7 at n=9.
- Board rounds 02-fable/03-astra and `PROPAGATION_CLOSURE` §1 preserve the normalization loophole. The present experiment supplies coordinate-source examples in that loophole, not a new general transport identity.

### 1.1 Formal class used in this memo

**Definition (semantic ET-normalized step).** A partial integer procedure on `(n,a,b,source witnesses)` is ET-normalized on a domain if every successful output, after permutation, satisfies one of:

    I:  n|x, gcd(n,yz)=1;
    II: n|y,z, gcd(n,x)=1.

The usual explicit ET presentation uses positive integers A,B,C,D,E with `A+B=CE` and

    I: 4ABD=nE+1, output (nABD,ACD,BCD);
    II:4ABD=n+E,  output (ABD,nACD,nBCD),

**together with the normalization conditions just stated**. A polynomial ET step is the subclass with polynomial parameter/output dependence on the coordinate and witness variables, and with validity, positivity, integrality and normalization persisting at the square being tested.

**PROVED, relative to ET Prop. 1.6 as quoted and audited in FRONTIER/AMPLIFY:** no such square-valid normalized step can succeed at an odd square. This conclusion does not require polynomiality. Conversely, polynomial syntax alone does not imply normalization, and gcd/lcm syntax alone does not imply escape. The source hypotheses must actually hold at the test square; merely substituting into a formula with an undefined denominator proves nothing.

**Definition (non-ET complement relevant here).** The ambient class consists of positive, exact integer partial procedures, allowed to reject on failed divisibility. A procedure is outside the square-valid normalized class if it succeeds at some admissible square with a mixed/scaled output. At primes p∤4, every successful output is automatically Type I or II; consequently “non-ET at primes” would be the wrong requirement. The complement is not a formal synonym for “non-polynomial.”

**Assessment.** This repairs the initial task's polynomial-versus-non-polynomial shorthand rather than silently using it as a theorem. The construction below is genuinely an exact-division/gcd procedure, but its infinite square subfamily simplifies to polynomial formulas on suitable parameter classes. That is legal.

### 1.2 What “essential” can rigorously mean

**Definition / audit criteria.** Separate three claims that a mere successful triple cannot conflate:

1. **Not root scaling:** at n=m², not every output denominator is divisible by m.
2. **Not any proper-divisor scaling:** `gcd(n,x,y,z)=1`. This stronger condition excludes direct scaling of a solution at every proper divisor of n.
3. **Essential source dependence for a specified rule:** the inherited denominator ratio is recoverable from its labelled output pair, and replacing the supplied witness at the same coordinate changes that ratio or the rule's success. No `W(m)` or precomputed target is queried. We additionally compare with a coordinate-only grammar.

**PROVED:** an output is a direct scaling from `W_k(d)`, d|n, exactly when `n/d` divides all three denominators; division proves the reverse direction. Thus criteria 1–2 are exact arithmetic tests, not provenance guesses.

**Scope warning.** Criterion 3 is operational dependence, not a theorem that a known target could never be constructed another way. The ratio procedure uses only a pair of source denominators; it would also accept an arbitrary pair with the same ratio. It does **not** exploit the full source equation to force integrality. Calling this a total law, or claiming that source solubility itself supplies arithmetic information, would overstate the result. The concrete hit satisfies the request's non-scaling/source-use test, not this stronger unproved forcing requirement.

## 2. Precise questions

**Questions, not assumptions.**

- **Q1:** Is there a coordinate-source procedure satisfying criteria 1–3 that succeeds at an odd square? Answer: yes, §3.1, including the stronger criterion 2.
- **Q2:** Does that same procedure succeed at primes, particularly the hard list? Answer: sometimes, with exact rates below; at 3361 it returns a known ET-II solution.
- **Q3:** Does the union grammar G below succeed for every relevant prime if all coordinate fibres are available? Answer: no; complete finite failures include 2521 and 9601.
- **Q4:** Is there a general norm-compatible, 4-specific forcing theorem beyond this grammar? Remains open. Failure of G is not a no-go theorem for that shape.

## 3. Construction, proofs, and computation

### 3.1 The simplest successful step: greedy ratio transplant

**PROVED (elementary identity; source-ratio version of board argon-3).** Given a source witness and any two of its denominators U,V, put

    g=gcd(U,V),  r=U/g, s=V/g;
    X=⌊n/k⌋+1,  d=kX−n;
    H = nX(r+s)/(d r s).                                      (G₀)

If H is an integer, return `(X,Hr,Hs)`; otherwise reject. It is positive and solves k/n because

    1/(Hr)+1/(Hs) = (r+s)/(Hrs) = d/(nX) = k/n−1/X.

Since gcd(r,s)=1, the integer common scale H is necessary for **both** Hr and Hs to be integral. At k=4, n≡1 (4), d=3 and

    X=(n+3)/4,     H=n(n+3)(r+s)/(12rs).                       (G₃)

This is a uniform formula, not a table of target answers. Extracting the ratio, exact division and rejecting failures are non-polynomial integer operations. The rule reads the coordinate through its source fibre.

**PROVED / directly checked example, satisfying all three criteria.**

    n=289=15²+8², Q={7,8,15,23};
    (U,V,W)=(4,68,510) ∈ W₄(15), g=4, (r,s)=(1,17);
    X=73, H=289·73·18/(3·17)=7446;
    4/289 = 1/73 + 1/7446 + 1/126582.

Here `7446=17·438`, `126582=17²·438`, `17∤73·438`. The output valuations are exactly `(0,1,2)`. In particular `gcd(289,73,7446,126582)=1`; no proper-divisor scaling is possible. The coordinate-only grammar below has **zero** outputs at 289. For the same coordinate, `(4,84,210) ∈ W₄(15)` supplies first-pair ratio `1:21`; the **same** rule now asks for `H=464134/63` and rejects. The source data genuinely alter validity; the labelled output pair recovers the original reduced ratio.

**PROVED / prime example.**

    3361=56²+15²;
    (15,406,435) ∈ W₄(56), choose (U,V)=(15,435);
    (r,s)=(1,29), X=841, H=974690;
    output (841,974690,28266010).

This is exactly FRONTIER's known solution `(841,3361·290,3361·8410)`. It proves that the *same square-surviving step* operates at a genuinely hard prime; it does not discover a new target family. At 577 it similarly uses `(6,174,667) ∈ W₄(23)` to obtain `(145,28850,836650)`.

### 3.2 An infinite, non-scaling square family

**PROVED (elementary; no novelty claim for the resulting Egyptian-fraction identity).** For any integer t≥1 with 3∤t, put

    m=16t²+1,  a=m−2, b=8t,  n=m²;
    w=(4t², 4t²m, 2t²am) ∈ W₄(a).                            (F)

Then a²+b²=m², gcd(a,b)=1, and every prime factor of m is 1 mod 4: a prime dividing `(4t)²+1` sees −1 as a nonzero square. The first two denominators of w have ratio 1:m. Rule G₃ gives

    X=(m²+3)/4,
    H=m(m+1)(m²+3)/12,
    output (X,H,mH).                                         (F′)

*Proof.* The norm identity is `(m−2)²+64t²=m²`. For the source equation, with U=4t²=(m−1)/4,

    1/U+1/(mU)+2/(amU)=(am+a+2)/(amU)=4/a.

The denominators in (F) are positive integers. Since m≡1 (16), the factor 4 divides `(m+1)(m²+3)`; since 3∤t, m≡2 (3), so 3 divides m+1. Thus H is integral, and G₃ proves (F′). Also

    gcd(X,m)=1,  gcd(H/m,m)=1,

because m is prime to 6 and gcd(m,(m+1)(m²+3)) divides 3. Therefore `gcd(n,X,H,mH)=1`, and at each prime ℓ^e∥m the output valuations are `(0,e,2e)`. This is not a scaling of any lower-level solution. ∎

**CERTIFIED toy:** exact fractions verify (F)–(F′) for all **667** eligible t≤1000. The proof is unconditional; this finite check is only an implementation audit. The family provides infinitely many examples inside the task's allowed square-root factorization class, with no assumption that m is prime.

**Assessment.** This meets the literal board drop-condition robustly, but the target identity is elementary and square-specific. Substituting n=p into this parameterized square family does not prove anything about general primes. Nor does the family turn the partial rule into an all-witness map.

### 3.3 Exact composite-valid ratio completion

**PROVED (complete identity and enumeration).** For coprime positive r,s, all solutions `(X,Hr,Hs)` at any n,k are parameterized by positive divisors D of `N=n²(r+s)` such that

    D≡−n (mod k),
    N/D ≡ −n(r+s) (mod krs),
    X=(D+n)/k,   H=(N/D+n(r+s))/(krs).                       (R)

*Proof.* The equation is `kHrsX=nHrs+n(r+s)X`. Multiplying out gives

    (kX−n)(kHrs−n(r+s))=n²(r+s).

Both factors are positive for a solution. Taking D as the first factor gives the two integrality conditions and the inverse formulas; conversely they imply the original equation. ∎

Unlike the board's prime-only split, this proof never assumes `gcd(s,n)∈{1,n}`. Squares need no artificial exclusion. G₃ is its D=3 subcase. **Assessment:** R is explicitly B2, not an escape: the class condition on a divisor/co-divisor of **one integer** is modulo krs, tied to the inherited source ratio.

**PROVED limitation of the easiest scaling idea.** If gcd(n,q)=1 and k≥4, rationally scaling an entire source triple by n/q can never give three integer denominators. Integrality would force q|U,V,W; writing them q times integers gives `k=1/U′+1/V′+1/W′≤3`. For a primitive odd norm, gcd(n,q)=1 for every q∈Q: this is immediate for a,b and, for a±b, from `n≡2b² (q)` and gcd(a,b)=1. Thus direct whole-witness coordinate scaling is ruled out, without any search.

### 3.4 Exhausted grammar G

**Definition (exact finite search domain).** For each representation and each *complete* source fibre W_k(q), q∈Q, form the following branches. No target triple is precomputed during search.

- **Coordinate atoms:** `C={1,2,k,a,b,a+b,a−b,a²,b²,ab,2ab,n}`. Retain positive distinct values.
- **Witness features D₀(w):** the three denominators; for every pair, including a repeated index, their product, gcd, lcm, and either denominator divided by their gcd; also the total gcd and total lcm.
- **One-split features D₁(w):** D₀ plus `u+1,u(u+1)` for each source denominator u. These are the denominators in the exact split `1/u=1/(u+1)+1/(u(u+1))`. There is no recursive splitting or unbounded rewrite closure.
- **Pool P(C,D):** C itself, and `cd,gcd(c,d),lcm(c,d),d/c,c/d` for c∈C,d∈D, retaining quotients only when integral and retaining values ≤10n². There is one such operation layer, not its transitive closure.
- **Core / Split:** select the two least output denominators x≤y from P(C,D₀) / P(C,D₁). Test `n/k<x≤3n/k`, `y>nx/(kx−n)`, `y≤2nx/(kx−n)`. Set

      z=nxy/((kx−n)y−nx),

  accepting exactly when integral. The inequalities ensure z≥y. No bound is imposed on z.
- **Baseline:** the identical two-held-denominator completion using P(C,C), with **no witness features**. This controls arithmetic coincidence, though it is not claimed to contain every coordinate-only formula.
- **Repair:** for each supplied w=(u,v,z), choose which term u to replace, and let `h=c/e` with c,e in `C∪{q,n+q,n−q}`. Require hv,hz to be integers and set

      X = n h q u / (k h q u − n(ku−q)).

  Accept exactly when positive integral. This follows from `1/v+1/z=k/q−1/u`. It includes rational coordinate scaling of a pair, but not of all three terms.
- **Ratio:** for each pair of source denominators, extract its coprime ratio and exhaust the full divisor enumeration R of §3.3, with **no denominator/multiplier cutoff**. Factor n and r+s separately; combine their exponent lists to enumerate divisors of n²(r+s). This branch contains Repair and Greedy, but is reported separately from their restricted rules.

**Scope.** G is the union of these branches. It combines ×, gcd, lcm, common-factor division, exact splitting atoms, rational pair scaling, case splits, and the norm identity. A branch may use any one coordinate witness; it does not combine two different witnesses in a single expression. Its “all sources” result unions over every witness at every coordinate. Gaussian factorization, deeper expression trees, recursive splitting, and joint cross-witness operations are outside G. The Split branch uses split *denominator features*, not a claimed four-to-three fraction-preserving rewrite.

**PROVED / computational completeness within G.** For sources, every sorted witness has `q/k<u≤3q/k`; after u is chosen the residual A/B is reduced and `(Av−B)(Az−B)=B²` exhausts the two-term choices. The pool rules are explicit finite sets. The bounds in the two-held branch are necessary for x≤y≤z. R is an exact bijective parametrization with a finite divisor set. Therefore an empty G image is a genuine negative for this grammar and supplied coordinate block, not a denominator timeout.

### 3.5 Census and hard-prime results

**CERTIFIED finite experiment.** Census populations:

- **32 primitive representations** of **28** squares m² with 3≤m≤200 odd and all prime factors of m ≡1 (4). This includes the requested roots 5,13,17,25,29,37,65; 21 representations have prime m.
- **542 distinct primes:** all 295 p≡1 (8), p<10⁴; all 273 Mordell-hard p<10⁵; the requested hard/board fixtures, with overlaps removed (the extra large fixture is 233689).
- Four in-domain model targets: 8/17, 8/241, 10/181, 12/1657. The other two numerator-8 controls are independently exhausted outside the Gaussian norm domain.

Entries count target representations/integers with at least one output, not source witnesses:

| cohort | Baseline | Repair | Greedy G₀ | Ratio R | Core | Split | union G |
|---|---:|---:|---:|---:|---:|---:|---:|
| all 32 square representations | 2 | 20 | 11 | 32 | 19 | 22 | 32 |
| square representations with **no proper-divisor scaling** | 2 | 2 | 11 | 18 | 15 | 15 | — |
| 21 prime-square representations | 1 | 13 | 1 | 21 | 8 | 11 | 21 |
| prime squares with **mixed** output | 1 | 0 | 1 | 7 | 5 | 5 | — |
| all 542 primes | 6 | 43 | 175 | 528 | 382 | 425 | 536 |
| 273 Mordell-hard primes <10⁵ | 0 | 6 | 69 | 259 | 139 | 169 | 267 |
| 295 primes <10⁴ | 6 | 38 | 113 | 290 | 260 | 277 | 293 |

The distinction between scaling tests matters: Repair has **6/32** square representations with an output not divisible throughout by m, but only **2/32** with `gcd(n,x,y,z)=1`; the other apparent escapes can still scale from another proper divisor. G₀ has genuinely non-scaling outputs on all its 11 successful square representations. At 169, Ratio finds only scaled outputs, whereas Core/Split produce mixed outputs, e.g. `(60,156,1690)` from features of `(4,13,156) ∈ W₄(12)`.

**CERTIFIED hard list.** Numbers are distinct output triples, not merely yes/no:

| p | (a,b) | Greedy | Ratio | Core | Split |
|---|---|---:|---:|---:|---:|
| 409 | (20,3) | 0 | 1 | 7 | 8 |
| 577 | (24,1) | 2 | 5 | 1 | 2 |
| 3361 | (56,15) | 1 | 2 | 0 | 0 |
| 5569 | (63,40) | 0 | 1 | 0 | 0 |
| 9601 | (95,24) | 0 | 0 | 0 | 0 |
| 193 | (12,7) | 0 | 2 | 3 | 5 |
| 2521 | (36,35) | 0 | 0 | 0 | 0 |

Baseline and Repair give zero at every listed hard prime. **Complete union failures:**

    2521, 9601, 53881, 54121, 88321, 94441.

At 2521, all **184** source-witness occurrences and **283** distinct inherited ratios were exhausted. An independent full target enumeration finds **9** solutions, none in the grammar. At 9601 the independent enumerator finds **23** target solutions, also none in G. Thus these are failures of transport, not ES failures.

**CERTIFIED / interpretation.** The unrestricted Ratio branch fails at 14 of the 542 primes:

    1201,2521,4729,8761,9601,12601,18481,
    43969,53881,54121,87049,87481,88321,94441.

The apparently high 528/542 target coverage conceals very low all-witness totality: only **9798/243192** source-witness occurrences at the prime targets admit a Ratio completion; Greedy admits **1466/243192**. These are deterministic finite counts, not probabilistic independence claims. A law allowed to inspect complete fibres can ignore bad witnesses, but it cannot rescue the six empty target images within G.

**CERTIFIED near-square screen:** all 56 sampled primes with `p−⌊√p⌋²≤16` have a Ratio output; Greedy reaches 27, Core 51, Split 52. **Assessment:** this is a selected, small-range diagnostic, not evidence against FRONTIER's near-square depletion or a uniform bounded-gap theorem.

### 3.6 Numerator controls

**CERTIFIED:** all branches give zero at 8/17 and 8/241. Complete independent enumeration also gives zero for 8/11 and 8/131. The latter two are 3 mod 4, so they have no integer sum-of-two-squares representation and the coordinate procedure is outside its domain. At 17 the source block includes the numerator-8 exception 3; at 241 it includes 11. Thus those two Gaussian block implications are not counterexamples with true antecedents.

**PROVED / CERTIFIED stronger control:** the conditional identities G₀ and R are numerator-uniform, but their integrality gates are not automatically satisfied. The threshold-free **total** Gaussian block law is refuted at 10/181 and 12/1657, where all source fibres are nonempty and G is empty, agreeing with Astra and `PROPAGATION_CLOSURE` §2. No 4-specific theorem forcing the gate is supplied. Consequently the construction passes the false-output control but fails as a numerator-uniform existence law.

### 3.7 Reproducibility and independent audit

**CERTIFIED implementation record.** The final census exhausts **255476 source-witness occurrences**, **394182 distinct ratio fibres** (counted separately at each target), **123172020** bounded pair-repair trials and **83141586** two-held pool pairs. Maximum pool size is **481**; no Cartesian-product array is allocated. Final census CPU time is approximately **115 seconds**; all exploratory reruns and audits together remain far below the 1.5-hour budget. Memory is limited to 1.5 GB in Python plus a shell limit, factor caches are bounded, and commands have timeouts. Data total is under 1 MB.

The audit independently enumerates **all target triples** with a C `x,y` loop at 25,169,289 and the seven hard primes; it then filters by source ratios/pool membership, rather than reusing R or the residual construction. Source fibres at those targets are independently checked with direct `y` enumeration. Core, Split, Greedy and Ratio image counts agree exactly at all ten targets, including the complete negative images at 2521 and 9601. The source engine is also cross-checked on 316 small `(k,q)` fibres. All **4952 saved source/output examples** pass exact rational checks; the 667 infinite-family toy cases pass too.

```sh
ulimit -v 1800000
cc -std=c11 -O2 -Wall -Wextra -Werror scripts/z47_nonet_step_brute.c -o /tmp/z47_nonet_brute
timeout 180 uv run python scripts/z47_nonet_step_search.py --mode audit
timeout 1200 uv run python scripts/z47_nonet_step_search.py --mode census \
  --out data/z47_nonet_step/census.jsonl
timeout 120 uv run python scripts/z47_nonet_step_search.py --mode fixtures
timeout 600 uv run python scripts/z47_nonet_step_audit.py /tmp/z47_nonet_brute
```

Target enumeration occurs **only in the independent audit**, after the search; it is not used to select sources, manufacture the hit, or train a formula. Timings in JSON vary between runs; arithmetic counts do not.

## 4. Every FRONTIER §4 screening line

**Assessment; PASS means the scoped experiment respects the screen, not that it proves ES.**

| # | status | reason |
|---|---|---|
| 1 T1 | **PASS** | Explicit square output is mixed, valuations (0,1,2); no ET normalization is claimed there. At primes, the exact gate must produce the necessary nonresidue data. |
| 2 numerator 8 | **PASS** | No outputs at 17/241; independent zeros at 11/131, outside the norm domain. |
| 3 uniform laws | **FAIL as a total law** | Identities work for every k; the missing forcing theorem would need a 4-specific input. 10/181 and 12/1657 refute universal block closure. |
| 4 B2 | **FAIL** | R explicitly tests a divisor/co-divisor of n²(r+s) modulo krs; Greedy tests `12rs | n(n+3)(r+s)`. No forcing theorem removes this gate. |
| 5 fixed p | **PASS** | Every target and fibre is treated separately; no averaged estimate is used as a pointwise theorem. |
| 6 scale B3 | **N.A.** | No main-term/error argument or power-size lower bound. |
| 7 one-sided | **PASS** | No two-sided asymptotic or uniform discrepancy assertion. |
| 8 B1 | **PASS, scope only** | Complete source fibres and norm coordinates grow/change with p; no fixed finite congruence covering or finite formal run is asserted sufficient. This supplies no arithmetic forcing by itself. |
| 9 class vs parity | **FAIL as forcing** | The diagonal Legendre lemma does not guarantee either congruence in R; actual divisibility is still tested. |
| 10 privacy | **PASS** | No pooling or collision of large prime factors across shifts. |
| 11 signed detour | **N.A.** | Every accepted denominator is positive; there is no reflection. |
| 12 relaxation transport | **PASS, partial only** | The displayed formulas genuinely transport to exact triples; no claim of universal landing from a relaxed object. |
| 13 BM shortcut | **PASS** | No use of local/BM sufficiency. |
| 14 hard primes | **FAIL as a universal grammar** | G is completely empty at 2521 and 9601, plus four further Mordell primes. |
| 15 Mordell/near-squares | **PASS diagnostic** | All 273 Mordell-hard primes <10⁵, 32 square representations and the bounded-gap subsample are reported. |
| 16 thin-family transfer | **PASS** | The infinite square family is not transferred to general primes; prime success is separately measured. |
| 17 covering/large factors | **N.A.** | No coset-covering or pigeonhole theorem is proposed. Factor lists are used exactly, without an assumed residue distribution. |

## 5. New-theory sketch: valuation-stratified source-ratio transport

**Definition / proposed bookkeeping framework, not an established new theory.** For a source block Q, let `R_k(Q)` be the set of reduced denominator ratios in its complete fibres. Attach to each ratio its valuation-difference vector at primes dividing n. The transport correspondence `T_{k,n}(r,s)` is the finite divisor set in (R). Separate three layers: source occurrence, permissible valuation stratum, and the two actual divisibility congruences. This keeps mixed-square outputs visible instead of incorrectly normalizing them away.

**PROVED first structural lemma.** Let n=ℓ², ℓ an odd prime, k=4. If a target triple is not ℓ-scaled, its ℓ-adic denominator valuations are `(0,1,2)` up to permutation. Therefore every inherited coprime pair ratio r:s used to obtain such a triple satisfies

    v_ℓ(rs) ∈ {1,2}.                                       (V)

*Proof.* There is a denominator prime to ℓ, and the sum has ℓ-adic valuation −2, so some denominator has valuation at least 2. Two denominators divisible by ℓ² would give ET-II, forbidden by T1. If the remaining denominator were also prime to ℓ, this would be ET-I, also forbidden. It must have valuation 1; the unique most divisible denominator then has valuation exactly 2, since a unique term of valuation below −2 cannot cancel. The valuation difference in any pair is 1 or 2, which is exactly v_ℓ(rs) after removing its gcd. ∎

**CERTIFIED toy, and refutation of the first tempting conjecture.**

| square | source ratios | ratios exposing its root prime | mixed Ratio outputs? |
|---|---:|---|---|
| 169=12²+5² | 42 | 4:13, 1:39 | **no** |
| 289=15²+8² | 127 | 1:17, 2:255, 4:85, 1:51 | yes |
| 1369=35²+12² | 245 | 5:37, 2:259 | yes |

Thus **“valuation exposure implies a mixed-square landing” is false already at 169**. The stronger prime-side conjecture `T_{4,p}(R₄(Q(p)))≠∅` is also false, at the 14 Ratio failures. Source ratios add genuine witness dependence but not automatic validity.

**Assessment / theory needed next.** A useful enlargement would need a 4-specific closure operation on source data that provably creates a ratio satisfying the full gate, not merely its valuation/parity conditions. Its first concrete obligation is to escape the empty images at 2521 and 9601 without importing a known target. No such operation is established here. This is the exact open implication, not an invitation to rename the divisor search as a theory.

## 6. Verdict and next steps

**Assessment: PARTIAL, 1/5; the displayed universal grammar COLLAPSES at B2 and explicit finite failures.** The literal square-normalization loophole is occupied: a witness-essential, genuinely mixed square hit exists, persists on an infinite square family, and the same partial rule works at primes including 3361. Therefore “an honest search found no non-ET step” would be false. However, square survival alone does **not** change the route verdict: the successful operation was already implicit in the board's residual-ratio algebra and has an explicit integrality gate. The board's stronger open crux—a uniform useful total map between distinct prime fibres without that gate—is untouched.

**Concrete next steps (Assessment):** retain the normalized-versus-mixed distinction and the 289→3361 rule examples in the campaign's closure record. Do not fund a larger blind grammar sweep merely because of 536/542 finite coverage. Reopening the propagation route should require a named new closure/forcing input that handles **2521 and 9601**, is not merely target enumeration, and distinguishes numerator 4 from the 10/181 and 12/1657 controls. No theorem here rules out such an input or proves that B2 is necessary for every possible ES proof.
