# FOREST_H4 — endpoint height is not window depth

## 0. Summary

**PROVED.** The forest stopping time satisfies `r(p) ≤ H₄(p)` and `a_min(p) ≤ 2H₄(p)−1`, but it is not a reparametrisation of the window statistic: **for every H, infinitely many primes have simultaneously `a_min=3`, `λ=2`, and `H₄>H`**. There is an unconditional almost-all theorem, `H₄(p) ≤ h(p)` for every function `h(p)→∞`; this says nothing at a prescribed prime. **CERTIFIED:** 522,253 saved rows (517,362 distinct primes) pass independent primality, minimum-endpoint, least-nonresidue and fraction checks. The largest observed `H₄/log²p` is 1.612120 at `p=1002125860849`, with `H₄=1231`, `r=31`, but `a_min=3`. Four million additional prime draws supply tail statistics. No example refutes the proposed constant 2, let alone an unspecified big-O constant. **Assessment:** the forest removes factoring from verification, not the moving-class existence problem; neither GRH nor the data supplies an all-prime upper bound, and exponent 2 has no established sharpness argument.

**Verdict: PARTIAL — the open implication is small nonresidues ⇒ an actual opposite-coloured parent edge in a growing endpoint box. Promise: 1/5. ES remains open.**

## 1. Setup, prior work, and novelty

**Definition.** Throughout, `p≡1 (24)` is prime, logarithms are natural, and `r(p)` is the least positive quadratic nonresidue. Put

```
F_p: vertices 1,…,p+2; {u,v} an edge iff u≠v and uv | p+u+v;
χ_p(v)=(v/p);
H₄(p)=min{max(u,v): {u,v} is an edge and χ_p(u)χ_p(v)=−1},
```

with minimum infinity if empty. For a candidate larger endpoint v, let

```
a_v=(−p mod v),     q_v=ceil(p/v).
```

The unique possible parent is `a_v`, and, at a unit vertex, it is an edge iff `a_v>0` and `a_v | q_v+1`, equivalently `a_v | p+v`. Its label is `t=(q_v+1)/a_v`.

**PROVED, existing dictionary.** All non-diagonal prime edges have unit endpoints. Their signs satisfy `(tu−1/p)=(uv/p)`. An edge is bichromatic iff 4 divides a slot in `{t,u,v,tu−1,tv−1}`. This is five-slice ES, denoted ES₅, not known equivalent to unrestricted ES. The diagonal word is non-certifying. Sources: `LOWER_TAIL_ASTRA.md` Lemmas 2.1–2.2, `DEDEKIND_ES.md` Theorem 4.5/Corollary 4.6, and the corrected `LOWER_TAIL_FABLE.md` §§2.8–2.9. The parent scan costs exactly `H₄−1` probes, not H₄ probes.

**Assessment, novelty audit.** Read `BREADTH_Z45.md`, the complete `BRAINSTORM/z45_program_synthesis.md`, `LOWER_TAIL_ASTRA.md`, `LOWER_TAIL_FABLE.md`, `FRONTIER.md`, and the brainstorm index; searched `a_min`, `X_win`, `H₄`, least-certificate and Graham–Ringrose references. Relevant predecessors are:

- z45 §5: the H₄ definition, log-squared conjecture, `a_min≤2H₄`, and square-mimicking endpoint cutoffs; `reviews/z45-breadth-review.md` already warns that H₄ is not identical to X_win.
- `POINTWISE_SIZE.md` §8: unrestricted p-free-denominator window statistic and X_win; `BRAINSTORM/greedy_algorithm_dynamics.md`: its exact greedy interpretation.
- `BRAINSTORM/z45_siegel_dichotomy.md`: a_min census through 10⁷; `reviews/es-window-note-review.md`: census through 10⁸, maximum a_min=107 at 8803369. The unrelated `a_min` in `POINTWISE_TERNARY.md` is a different parameter.
- `BRAINSTORM/bsA_farey_lnr_pigeonhole.md`, `DEDEKIND_ES.md`: λ is minimal HJ **length**, not endpoint size. `BRAINSTORM/y5_ocensus_hard_primes.md` records the least opposite frieze vertex o*, again a different height.
- Astra §5 already observes that a parent of the least QNR automatically certifies, and explicitly disproves the universal least-QNR-root mechanism.
- `POINTWISE_OMEGA.md` §8 already transfers Graham–Ringrose to a different witness height; no novelty is claimed for that transfer template.

**Assessment.** The additions here are the simultaneous separation theorem, an explicit height-aware HJ dictionary, the almost-all endpoint result, and adversarial statistics. These are elementary consequences/measurements of existing structures, not a new arithmetic existence mechanism or an external novelty claim.

## 2. Precise questions

**Question Q1.** Is `H₄≪log²p` merely X_win (`a_min≪log p`) in different coordinates? What information does λ retain?

**Question Q2.** Does a least QNR of size r force H₄ of comparable size, or can the parent-divisibility delay dominate r? How do QR-rich and near-square adversaries behave?

**Question Q3.** What upper bounds hold almost everywhere, and which additional statement would make a pointwise bound possible?

**Question Q4.** What is the right extreme-value scale? The requested log-squared bound is a conjecture to stress-test, not a known consequence of GRH or an established sharp exponent.

## 3. Mathematics and computations

### 3.1 Window and HJ comparisons

**Definition.** For `e≡3 (4)`, put `x_e=(p+e)/4` and

```
Rat_e(x)={a/b mod e: ab|x, gcd(a,b)=1}.
a_min(p)=min{e: p∤x_e, Rat_e(x_e) meets {−1,−p}}.
```

The targets give Type II and Type I respectively (`POINTWISE_SIZE.md`, Theorem 8.1). Let `a₅(p)` be the minimum e among the p-free denominators supplied by the five-slot identities, allowing every good word and every applicable slot. This restricted statistic is introduced only to make the comparison explicit.

**Proposition 3.1 (PROVED).** When H₄ is finite,

```
a_min(p) ≤ a₅(p) ≤ 2H₄(p)−1.
```

Consequently `H₄≪log²p` implies the weaker window estimate `a_min≪log²p`, **not** X_win's logarithmic estimate.

*Proof.* Take `u<v=H₄` and its label t. If `4|t`, the p-free denominator is `tuv/4=(p+u+v)/4`, so `e=u+v`. If `4|u`, it is `u(tv−1)/4=(p+v)/4`, so `e=v`; reverse for `4|v`. If `4|tu−1`, it is `v(tu−1)/4=(p+u)/4`, so `e=u`; reverse for the other slot. In every case e is positive and 3 modulo 4, and `e≤u+v≤2H₄−1`. These denominators are p-free: every word endpoint is a unit and all displayed factors in a p-free denominator are units modulo p. The unrestricted minimum is no larger. ∎

**Proposition 3.2 (PROVED: a genuine separation).** For every fixed integer `H≥4`, infinitely many primes `p≡1 (24)` satisfy

```
a_min(p)=3,     λ(p)=2,     H₄(p)>H.
```

In particular no finite-valued function `f(a_min,λ)` bounds H₄ pointwise.

*Proof.* Put `M=lcm(24,1,…,H)`. Choose distinct primes `q>H`, `q≡7 (12)`, and `s>H`, `s≡11 (12)`. Prescribe

```
p≡1 (M),       p≡−1 (q),       p≡−3 (s).
```

This is a reduced CRT class modulo Mqs, so Dirichlet supplies infinitely many primes, which may be taken larger than Mqs. The z45 cutoff lemma gives H₄>H: at `2≤v≤H` the only possible parent is v−1, and an edge requires `v−1|2`, leaving v=2,3; their words have no 4-divisible slot when p≡1 (24).

Since `s|(p+3)/4` and `s≡−1 (3)`, `Rat_3((p+3)/4)` contains −1; thus a_min=3. Since `q|p+1` and q≡3 (4), quadratic reciprocity gives `(q/p)=(−1/q)=−1`. Moreover `p/q=[[(p+1)/q,q]]` has HJ length 2. Length 1 is impossible for a QNR, so λ=2. ∎

**Assessment, exact logical scope.** This disproves every p-independent bound in terms of the two scalar minima. It does **not** formally disprove an implication from the global assertion X_win to a global log-squared H₄ bound: such an implication might use extra arithmetic beyond a_min. No such implication is obtained here or located in the campaign. The explicit prime at our largest ratio already has a_min=3.

**CERTIFIED, new separation toys.** The script chooses the first prime in each displayed CRT class and checks the minima:

| imposed H | prime p | actual H₄ | a_min | λ |
|---:|---:|---:|---:|---:|
| 4 | 3121 | 7 | 3 | 2 |
| 8 | 997081 | 11 | 3 | 2 |
| 12 | 25862761 | 19 | 3 | 2 |
| 16 | 837476641 | 17 | 3 | 2 |
| 20 | 109878088321 | 23 | 3 | 2 |
| 24 | 3667646782801 | 31 | 3 | 2 |

**Definition.** For `1≤A<p`, let `ℓ_HJ(p/A)` denote canonical negative-CF length, and put

```
C₅(p)={A: (A/p)=−1, ℓ_HJ(p/A)≤3},
D₅(p)=min C₅(p),
λ(p)=min{ℓ_HJ(p/A): (A/p)=−1}.
```

There is no unqualified “least five-slice certificate”: D₅, a₅, the least level, o*, and H₄ minimise different coordinates.

**Proposition 3.3 (PROVED: exact HJ height dictionary).** For `A∈C₅`, set

```
h_p(A)=min(A,(p+1)/A)                         if ℓ_HJ=2;
h_p(A)=max(ceil(p/A), (−p mod A))             if ℓ_HJ=3.
```

Then

```
H₄(p)=min_{A∈C₅(p)} h_p(A),
H₄(p)<∞  ⇔  C₅(p)≠∅  ⇔  λ(p)≤3.
```

*Proof.* At length 3, `p/A=[[v,t,u]]`, so `v=ceil(p/A)`, `u=vA−p`, and `t=(A+1)/u`. These are exactly the canonical word endpoints and the five-slice sign theorem applies. At length 2, `p=bc−1`, `A=c`, and both b,c have the same negative character because bc≡1 modulo p. The root-1 words with endpoint b or c give height min(b,c).

Conversely an edge with all three letters at least 2 is a canonical length-3 word. An endpoint 1 is a root-1 word with a QNR divisor v of p+1, hence is represented by length 2 at height at most v. If t=1, then `(u−1)(v−1)=p+1`; both factors have negative character, and replacing the word by a root-1 word gives strictly smaller height. Thus t=1 cannot attain H₄. This accounts for every boundary and proves equality of the minima. ∎

**PROVED consequences.** If D₅ has length 2, `H₄≤D₅`; if it has length 3,

```
H₄ ≤ max(ceil(p/D₅),D₅−1).
```

For an H₄-minimising interior word the associated smaller canonical numerator is `A=ceil(p/H₄)`; for a boundary minimum, a length-2 numerator is H₄ itself. Thus small endpoint height often means a **large** HJ numerator, not a small one. As another explicit comparison, for `P₅=min{uv: good edge}`,

```
H₄ ≤ P₅ ≤ H₄(H₄−1).
```

These follow directly by using the minimising word in the other minimisation. The λ bound alone supplies no endpoint control, by Proposition 3.2.

### 3.2 The least-nonresidue lower bound and the residual event

**Proposition 3.4 (PROVED).** For every prime in our progression,

```
H₄(p) ≥ r(p).
```

Equality holds iff, writing `a=(−p mod r)`, one has `a | p+r`.

*Proof.* The least nonresidue is prime: a composite least nonresidue would have a smaller nonresidue prime factor. All vertices below r have colour +1, so a bichromatic edge needs an endpoint at least r. At v=r, the parent a is positive and smaller than r, hence has colour +1. It is an edge exactly under the stated divisibility condition. ∎

**PROVED, scope warning.** At a general QNR vertex v, a parent edge is **not** automatically bichromatic: the parent may also be a QNR. The automatic implication uses v=r, or the additional assertion `(a_v/p)=+1`. Conversely the first good edge can have a QR larger endpoint and QNR smaller endpoint; 8,196 of the 517,362 distinct saved primes do so. A QNR-only larger-endpoint scan can therefore skip the true minimum.

**PROVED relative to published inputs; correction to the task's premise.** Unconditionally, the classical lower bound is

```
r(p) ≫ log p · log log log p   infinitely often,
```

not `log p·log log p`. The latter is Montgomery's **GRH-conditional** lower bound. Graham–Ringrose, “Lower bounds for least quadratic non-residues”, *Progress in Mathematics* 85 (1990), 269–309, supplies the unconditional triple-log result. The progression restriction needed here follows from Lau–Wu, “On the least quadratic non-residue”, *Int. J. Number Theory* 4 (2008), 423–435, Proposition 5.1, DOI 10.1142/S1793042108001432: it supplies primes p≡1 (4) for which all primes up to `δ log X log₃X` are residues, with `X^{1/2}<p≤X log X`. The conditions at 2 and 3 imply p≡1 (24), and those at 5 and 7 put p in Mordell's classes. Therefore Proposition 3.4 transfers the **unconditional triple-log Ω bound to H₄ on Mordell-hard primes**.

**Source verification.** Read the archived Lau–Wu text, §1 (equations (1.3), (1.5), (1.7)) and Proposition 5.1 (`sources/lit2026/lau-wu-least-quadratic-nonresidue.txt:378–405`). Also visited Paul Pollack's *The smallest quadratic nonresidue modulo a prime*, 2012 lecture, slides 9–12, https://www.pollack-math.net/NTS0812.pdf: the same unconditional/conditional distinction and Bach's GRH upper bound `r<2log²p`. The original Graham–Ringrose and Montgomery proofs were not rechecked. This correction already appears in `POINTWISE_OMEGA.md` §8; it is not a new literature finding.

**CONDITIONAL on GRH, classical.** `r≪log²p`. **Assessment:** `H₄≪log²p` would imply this numerical least-QNR upper bound unconditionally on our progression, and additionally force a divisor-class hit. GRH's bound on r supplies no bound at all on the delay `H₄/r`. In particular “at least as strong as the GRH least-QNR bound” means an implication between numerical bounds, not an implication to GRH itself.

**PROVED, exact residual B2 event.** At each v the required conjunction is

```
a_v>0,    a_v | ceil(p/v)+1,    χ_p(a_v)χ_p(v)=−1.
```

Equivalently, in a smaller-root coordinate u, a larger neighbour must satisfy

```
v | p+u,    v≡−p (mod u),    χ_p(v)=−χ_p(u).
```

The candidate parent is unique, but it can be absent. At the record `p=1002125860849`, r=31, the candidate parent is 14 and `(p+31) mod14=4`; the first QNR does not attach. At 2521, r=11 is even isolated in the **full** forest (`LOWER_TAIL_ASTRA.md`, Theorem 5.1, with infinitely many such primes conditional on Dickson). Uniqueness of a potential neighbour is not an existence theorem.

### 3.3 An unconditional almost-all upper bound

**Theorem 3.5 (PROVED relative only to PNT in fixed APs and divergence of prime reciprocal sums in an AP).** Let `h:[2,∞)→[1,∞)` satisfy h(x)→∞, with no monotonicity requirement. Then

```
#{p≤X: p≡1 (24), H₄(p)>h(p)} = o(π(X;24,1)).
```

In particular, for every ε>0, `H₄≤(log p)^ε` for almost all such primes, unconditionally. Even `h(p)=log log log p` (eventually positive) works.

*Proof.* For every prime `q≡3 (4)`, q≥7, the class `p≡−1 (q)`, p≡1 (24), gives the edge `{1,q}` because q|p+1. Reciprocity gives `(q/p)=(−1/q)=−1`, hence `H₄≤q` (omit the finitely many small p).

For fixed Y let `Q(Y)={q≤Y: q prime, q≡3 (4), q≥7}`. CRT and PNT in the finitely many classes modulo `24∏_{q∈Q(Y)}q` give the relative density of primes avoiding **these root-1 shots** exactly

```
B(Y)=∏_{q∈Q(Y)} (1−1/(q−1)).
```

Thus the upper limiting density of `{H₄>Y}` is at most B(Y). The reciprocal-prime sum in the class 3 modulo 4 diverges, so B(Y)→0 (indeed `B(Y)≍1/√log Y`). For any fixed Y, eventually h(p)≥Y; consequently the upper density of `{H₄>h(p)}` is ≤B(Y). Send Y to infinity. ∎

**Assessment, the average leak made explicit.** This argument averages **p over reduced residue classes** with Y fixed, then sends Y to infinity. It does not provide a uniform prime-counting estimate for the gigantic modulus associated to a growing Y, does not give an effective exceptional-set rate in h, and never recovers one prescribed prime. The root-1 component may still be monochromatic infinitely often. This strong-looking almost-all statement is consistent with every obstruction in Astra and is far weaker than a pointwise theorem. No GRH assumption is needed for the almost-all task, and no pointwise upper bound on H₄, even mere finiteness, follows from GRH by the arguments here. The tautological `H₄≤p+2` applies **only when a certificate exists**.

### 3.4 Adversarial experiment and exact checks

**Protocol / CERTIFIED saved computations.** `scripts/z46_forest_h4_scan.c` uses 64-bit deterministic Miller–Rabin with the standard seven bases and 128-bit modular products. It scans parents without factoring, stopping at 10⁶ endpoints; zero saved prime is censored. Every saved row is independently checked in Python using SymPy primality, the **mutual-divisibility plus Legendre-colour** test (not the C five-slot condition), a complete scan below the returned H₄, and an integer cross-multiplication check of its reconstructed Egyptian-fraction identity. Least QNR is verified on every smaller prime. All scripts run under a 2,000,000 KiB virtual-memory cap and explicit timeouts. There is no dense mesh/array or Cartesian product over primes and endpoints.

**Protocol / EVIDENCE selection.** Samples are deliberately heterogeneous, not independent draws from one population:

- Five consecutive-prime samples: 100,000 primes p≡1 (24) each, starting near 10⁸, 10¹⁰, 10¹², 10¹⁴, and 10¹⁵.
- Near-squares `p=m²+k`, `k∈{−24,−8,−3,1,8,24}`, 12,000 consecutive m at each of five starting scales; retain primes p≡1 (24). Some k yield no admissible primes.
- First up to 300 primes `p≡1 mod lcm(24,1,…,H)` at H=4,8,…,32, subject to the stated 1.1·10¹⁵ limit.
- 1,500 random square CRT classes per y=11,13,17,19,23,29,31,37,41, prescribing p≡1 (24) and p a nonzero square modulo every prime 5≤ℓ≤y; search the first 200 progression steps above 10¹², respecting the same size limit. This uses arbitrary QR residues, not only residue 1.
- Four million pseudorandom **prime draws**, two million each from [10¹²,2·10¹²] and [10¹⁴,2·10¹⁴], with all tail counts recorded and only H₄≥256 rows retained. These aggregate counts are single-engine EVIDENCE; all retained records are independently CERTIFIED.
- Two million CRT draws square modulo primes through 31, followed by QR rejection through 97 and primality testing. This yields 26 primes with r>97, all below 10¹⁵ and independently CERTIFIED.

**CERTIFIED maxima / EVIDENCE interpretation.** The full saved union has 522,253 rows, 517,362 distinct primes, zero failed audits, and maximum ratio 1.6121202376. The fixed constant 2 survives these tests; an unspecified big-O statement cannot be falsified by any one finite record.

| family | prime inputs/draws | max H₄ | max H₄/log²p |
|---|---:|---:|---:|
| consecutive near 10⁸ | 100,000 | 407 | 1.191077 |
| consecutive near 10¹⁰ | 100,000 | 579 | 1.091982 |
| consecutive near 10¹² | 100,000 | 815 | 1.067489 |
| consecutive near 10¹⁴ | 100,000 | 855 | 0.822770 |
| consecutive near 10¹⁵ | 100,000 | 383 | 0.321059 |
| random [10¹²,2·10¹²] | 2,000,000 | 975 | 1.229811 |
| random [10¹⁴,2·10¹⁴] | 2,000,000 | 951 | 0.891340 |
| QR through 23 | 1,500 | **1231** | **1.612120** |
| QR through 97 | 26 | 906 | 0.779395 |

**CERTIFIED record.** At `p=1002125860849`, the minimal edge is `{64,1231}`, with `t=12719916`; `r=31`, `a_min=3`. Thus `H₄/r=39.709677…`. The explicit word equation is

```
12719916·64·1231 − 64 − 1231 = 1002125860849.
```

The largest r in the saved set is 113, at `p=130679098667329`, whose first good edge is `{227,283}` and `H₄=283`. At `p=641335046555449`, r=107 but H₄=906, with edge `{95,906}`. Large r is a floor, not a prediction of the attachment delay.

**CERTIFIED saved-set summaries; EVIDENCE only for trends.** The following pool includes deliberately oversampled QR-rich inputs and retained large-H hunt records; it is **not** a population estimate conditional on r.

| r range | distinct saved primes | fraction H₄=r | mean H₄/r | max H₄/r | max H₄/log²p |
|---|---:|---:|---:|---:|---:|
| 5–13 | 476,659 | 0.919 | 1.092 | 56.538 | 1.191 |
| 17–23 | 28,943 | 0.416 | 1.611 | 50.294 | 1.314 |
| 29–43 | 10,738 | 0.254 | 1.900 | 39.710 | 1.612 |
| 47–71 | 978 | 0.385 | 1.857 | 17.340 | 1.074 |
| 73–97 | 18 | 0.111 | 1.803 | 3.603 | 0.253 |
| 101–113 | 26 | 0.115 | 2.299 | 8.467 | 0.779 |

**EVIDENCE.** Each unconditioned consecutive sample has mean H₄ between 9.44 and 9.50 and fraction H₄=r between 0.885 and 0.887. Fixed-size samples show no increasing normalised maximum with p. QR conditioning produces a larger absolute maximum, but not monotone growth of the ratio with r. Near-square samples attain at most H₄=172 and ratio 0.443430; this small selected set is not evidence against the established near-square depletion of **total** certificate counts. It measures the first small-endpoint hit, a different statistic.

**CERTIFIED finite harness.** The fixture file includes 193, 409, 577, 2521, 3361, 5569, 9601, 23929, 66529, 83449, 102001, 329617, 712321, 8813281, 5101441, 59929, 4962049, 8803369 and 9257329. All succeed. The underlying odd-square/numerator-8 controls are already fully tested by the z43/z45 suites; they are not duplicated as new tests here. Their mathematical reason remains essential: odd-square unit colours are all +1, whereas a negative character is **not** an 8-certificate condition.

### 3.5 What can honestly be conjectured about the exponent?

**CONJECTURE H₂ (inherited, still open).** `H₄(p)≪(log p)²` for all primes p≡1 (24). The new computation supports no larger required constant than 1.613 on its sample. It supplies no all-prime theorem.

**PROVED limitation on any logarithmic-power claim.** The transferred Graham–Ringrose lower bound excludes `H₄=O(log p)` and hence every `O((log p)^α)` with α≤1. It does **not** force α≥2. All exponents strictly between 1 and 2 remain compatible with this lower bound. No “sharp exponent 2” conclusion follows from least-QNR theory.

**Assessment, competing heuristic rather than a selected law.** H₄ is not just a least-QNR problem: at a fixed endpoint cutoff, the expected number of actual good edges has scale log²H, not log²p. A naive occupancy model would therefore predict a much heavier extreme tail than H₂. Conversely the forest's arithmetic dependencies could force much more efficient escape than that model. At present it would be unjustified to advertise either `H₄≍r·polylog` or exponent 2 as established sharp conjectural behaviour. Section 5 states the precise competing survival-law conjecture and its proposed extreme exponent; resolving this competition, rather than fitting another constant to finite maxima, is the next theoretical task.

## 4. All 17 FRONTIER screens

Here PASS means the scoped results avoid the prohibited inference, not that an all-prime proof has been found.

| line | status | reason |
|---:|---|---|
| 1 | PASS | Essential negative endpoint character vanishes at odd squares; no composite scaling claim. |
| 2 | PASS | Five-slot/character equivalence is numerator-4-specific; not applied to 8/131 or 8/241. |
| 3 | PASS | No numerator-uniform success, transport or recombination law is asserted. |
| 4 | **FAIL** | At fixed p, `a_v | ceil(p/v)+1` remains an uncontrolled moving-modulus event. |
| 5 | **FAIL for pointwise use; PASS as scoped theorem** | Theorem 3.5 averages p, and explicitly does not recover a prescribed prime. Computed certificates themselves are pointwise. |
| 6 | PASS | Endpoint-box mean is only Θ(log²H); no power-size main term or error domination is claimed. Prime classes use 1/φ, not 1/m. |
| 7 | PASS | Existence/stopping-time bounds, not two-sided asymptotics for R(p). The model concerns a different averaged survival probability. |
| 8 | PASS as a growing target; **FAIL as a forcing method** | H grows, so fixed-menu B1 does not refute H₂; the finite menu still has explicit square-mimicking avoiders. |
| 9 | **FAIL at existence** | The least QNR provides a sign, not the parent divisibility; the checker tests both exactly. |
| 10 | PASS | No large-prime pooling across shifts. |
| 11 | N.A. | All words are positive; no reflection from signed solutions. |
| 12 | N.A. | No long-CF or cap-relaxed solution is transported to length 3/cap zero. |
| 13 | PASS | No local/BM positivity is promoted to occupancy. |
| 14 | PASS as finite test | Listed hard fixtures all pass; no universal fixed-line claim. |
| 15 | PASS as finite test | CRT square-mimickers, QR-rich primes and bounded-distance near-squares are explicitly sampled. |
| 16 | N.A. | No thin-family algebraic factorisation is transferred to arbitrary primes. |
| 17 | N.A. | No full-coset covering theorem; a factoring-free check still does not force the large factor's class. |

## 5. New-theory sketch: character-conditioned endpoint survival

**Definition (organising framework, not claimed new external theory).** Let `N_H(p)` count good unordered edges with larger endpoint ≤H. Define the fixed-H prime-Haar survival law

```
δ(H)=lim_{X→∞} #{p≤X: p≡1 (24), N_H(p)=0}/π(X;24,1),
δ(H;y)=the same law conditioned on (ℓ/p)=+1 for every prime ℓ≤y.
```

**Proposition 5.1 (PROVED).** These limits exist at every fixed H,y, and are exactly computable finite CRT probabilities. Also `δ(H;y)=1` when y≥H. For unconditioned δ,

```
0<δ(H)≤∏_{7≤q≤H, q prime, q≡3(4)}(1−1/(q−1)),
δ(H)→0.
```

*Proof.* Set `L=lcm(24,1,…,H)`. For a prime p>H, any edge has gcd(u,v)=1, and `uv|L`. The edge and slot conditions depend only on p modulo 4uv, hence on p modulo 4L. Intersect with reduced classes p≡1 (24), and apply PNT in fixed APs. Adding the quadratic conditions only adds finitely many moduli (and 8), so gives the conditional limit. If all primes through H are QRs, all endpoints through H have colour +1. Strict positivity follows from the reduced class p≡1 modulo 4L and z45's cutoff lemma. The upper bound is the root-1 argument of Theorem 3.5. ∎

**Proposition 5.2 (PROVED, mean scale only).** The fixed-H prime-Haar expectation satisfies

```
E N_H = Θ((log H)²)   as H→∞.
```

*Proof.* A coprime pair u<v has at most four certifying classes modulo 4uv. Conditional on p≡1 (24), each has relative prime density at most `8/φ(4uv)`. Thus `E N_H≪(Σ_{n≤H}1/φ(n))²≪log²H`; the last elementary estimate follows from `n/φ(n)=Σ_{d|n} μ²(d)/φ(d)` and convergence of `Σ μ²(d)/(dφ(d))`.

For a lower bound take coprime `u≡1 (24)`, `v≡22 (24)`, `u<v≤H`, and the progression `p≡−u−v (12uv)`. It is reduced, lies in p≡1 (24), and gives a word with t divisible by 12, hence a good edge. Its relative prime density is `8/φ(12uv)≥2/(3uv)`. The harmonic sum of coprime pairs in these two classes is ≫log²H: Möbius inversion over the common divisors, necessarily coprime to 24, gives a positive Euler-product coefficient of log²H; restricting u<v retains half the leading term. Sum these densities. ∎

**Assessment.** Mean size does not determine δ; dependencies are precisely the issue. The proof is not a lower-tail estimate. This distinction also explains why one must not substitute log²p for log²H in a small-endpoint experiment.

**CONJECTURE S, competing model (low confidence).** A possible survival law is

```
−log δ(H) = (log H)^{2+o(1)}.
```

If accompanied by sufficiently uniform growing-H prime statistics and a suitable non-clustering statement across p, this predicts the extreme-value scale

```
log(max_{p≤X, p≡1(24)} H₄(p)) = (log X)^{1/2+o(1)}.
```

The proposed **extreme exponent is 1/2 in log H**, not 2 in log p. This competing conjectural scale would eventually exceed every fixed power of log p. It is offered as an adversarial, falsifiable alternative, **not a conclusion or a claimed refutation of H₂**. Neither a mean Θ(log²H), the exact finite laws below, nor the numerical hunts proves Conjecture S; even fixed-H S alone would not justify interchanging limits or infer the extreme envelope. A genuinely new theorem would have to determine the conditioned lower tail and its uniformity, or instead prove a deterministic attachment theorem strong enough to invalidate this model.

**CERTIFIED toy case: exact CRT probabilities.** Exhaustive reduced-class enumeration (no probabilistic primality test) gives:

| H | reduced p≡1 (24) classes modulo 4L | avoiding classes | δ(H) | E N_H |
|---:|---:|---:|---:|---:|
| 4 | 4 | 4 | 1 | 0 |
| 6 | 16 | 8 | 0.5 | 0.5 |
| 8 | 96 | 24 | 0.25 | 1.208333 |
| 10 | 288 | 72 | 0.25 | 1.25 |
| 12 | 2880 | 444 | 0.154167 | 1.725 |
| 14 | 34560 | 4664 | 0.134954 | 2.073611 |
| 16 | 69120 | 9328 | 0.134954 | 2.723611 |

**EVIDENCE, larger toy test.** The two independent-scale C hunts each use two million prime draws. Counts of H₄>B are:

| B | near 10¹² | near 10¹⁴ |
|---:|---:|---:|
| 16 | 270440 | 269198 |
| 32 | 58004 | 56976 |
| 64 | 12511 | 12490 |
| 128 | 1473 | 1522 |
| 256 | 139 | 155 |
| 512 | 17 | 9 |
| 1024 | 0 | 0 |

At B=16 the proportions 0.135220 and 0.134599 closely match the exact 0.134954. More importantly, the tails at a **fixed H** are nearly stationary across p-size, as the CRT formulation predicts. The data are too shallow to decide either proposed extreme law. The numerator-4 fibre and odd-square extinction survive in this framework; exact-class occupancy remains the new theory it would need, not something the framework supplies.

## 6. Verdict and next steps

**Assessment — PARTIAL, promise 1/5.** H₄ is a useful, factor-free and exactly checkable ES₅ target. It is strictly different from the least window and from HJ length, even at their smallest values. Its unconditional almost-all upper bound is easy and uninformative about the worst prime. Its pointwise lower bound imports least-QNR difficulty; its pointwise upper bound needs a further class-sensitive attachment theorem. The forest structure supplies no such theorem, and fixed/least-root methods are already refuted in the appropriate scopes.

**Concrete next steps (Assessment).** First study δ(H;y), separating the all-QR delay from parent failures after r; do not label a fitted log-squared budget sharp. Second seek a uniform survival estimate or a deterministic implication from a growing collection of QNR vertices to one opposite-coloured parent. The required conclusion is the exact divisibility in §3.2. A GRH bound on r, larger synthesis grammar, or another fixed-root exploration alone does not address it.

**Reproducibility.** Only the following new files belong to this task: this memo; `scripts/z46_forest_h4_scan.c`, `scripts/z46_forest_h4_analyze.py`, `scripts/z46_forest_h4_toys.py`; and `data/z46_forest_h4/` (compressed raw census/hunt/QNR rows, aggregate logs, summary JSON, exact toys). Total data are below 5 MB. Commands from the repository root:

```sh
set -o pipefail
ulimit -v 2000000
gcc -O3 -Wall -Wextra -Werror scripts/z46_forest_h4_scan.c -o /tmp/z46_forest_h4_scan
timeout 480 /tmp/z46_forest_h4_scan 100000 | gzip > data/z46_forest_h4/census.csv.gz
timeout 600 /tmp/z46_forest_h4_scan hunt 2> data/z46_forest_h4/hunt_counts.txt | gzip > data/z46_forest_h4/hunt.csv.gz
timeout 180 /tmp/z46_forest_h4_scan qnr 2> data/z46_forest_h4/qnr_counts.txt | gzip > data/z46_forest_h4/qnr.csv.gz
timeout 600 uv run python scripts/z46_forest_h4_analyze.py > data/z46_forest_h4/analysis.txt
timeout 180 uv run python scripts/z46_forest_h4_toys.py
```

No existing file was edited. No new claim about ES truth or its global verification range is made.
