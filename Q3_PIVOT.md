# Q3_PIVOT — two certified counterexamples to q = 3 pivot reachability

## 0. Summary

**CERTIFIED:** Astra's Q3 conjecture is false at **p = 7 909 441** and **p = 8 604 961**, both primes congruent to 1 modulo 840. The union of *all* seed components on U₃ₚ has respectively **57 = 53 + 4** and **76 = 72 + 4** unordered vertices, and contains no all-3-divisible triple. Two independently implemented complete-fibre searches give identical vertex sets; an additional static factor-certificate checker verifies closure. ES holds at both primes, with explicit solutions below. Thus even unbounded-depth q = 3 positive pivot rewriting can be trapped while its target is nonempty. The larger experiment processes 1 076 distinct primes: 1 063 successes, these two traps, and 11 explicitly censored cases. The deepest successful cases require seven pivots; small successful depths do not predict the existence of a path. This memo also preserves the board's three retained results, corrects its overly narrow identification of all spine exits with Type II, and answers its grep question.

**Verdict — COLLAPSES: Q3 itself, not ES or arbitrary positive rewriting. Promise: 1/5 for obstruction/classification; 0/5 for Q3 as an ES proof route.**

Labels: PROVED = argument supplied; CERTIFIED = independently checked finite calculation; EVIDENCE = remaining computational observations or extrapolation; CONJECTURE = explicitly open; Assessment = interpretation. ES remains open.

## 1. Setup, provenance, and the board's retained results

**Definition.** Work with unordered triples, represented in sorted order. U_N is the positive integral solution set of

    4xyz = N(xy + xz + yz).

A pivot holds one denominator and replaces the other two by any positive integral splitting of the residual rational number. Let S_q(p) = p·U_q, T_q(p) = U_qp ∩ (qℕ)³, and C_q(p) be the union of components meeting S_q(p). Distances are multi-source distances from **all** seeds. Passing to unordered triples loses neither reachability nor its minimum number of pivots when coordinate permutations are free, as in the board's graph.

**PROVED.** T_q(p) = q·U_p, so C_q(p) ∩ T_q(p) ≠ ∅ implies ES(p). Nonemptiness of T_q(p) alone does not imply that intersection. The new examples establish this distinction for q = 3, not merely for q = 2.

**Attribution / prior coverage.** The composite-pivot graph and its B-spine are Argon's item argon-2; Q3 is Astra's round-4 formulation. Source: board `20261019-es-sidestep/memo.md`, Bottom line §§1–3, with corrections in `rounds/03-astra.md` and `04-argon.md`; Fable's independent scripts and round-4 trap census supplied the validation fixtures. These files reside under `/home/pasky/.pi/boards/20261019-es-sidestep/`. `BREADTH_Z45.md` §§5–6 records the surrounding barrier landscape and this board. Earlier related work includes `BRAINSTORM/graph_cayley_moves.md` (different, signed chord/secant moves), `DETERMINISTIC_EXISTENCE.md` §§3,6–7 (subgroup versus divisor-box forcing), `CAP_POINTWISE.md` §§2–3, and `FORCED_WINDOW.md` §2. Repository-wide searches for pivot/rewriting and direct inspection of the three requested window memos found no earlier statement of the particular B-spine selector e | ((p+3)/4)². No literature-priority claim is made.

The three retained board results, with their actual scopes, are:

1. **PROVED, board Argon with Astra/Fable corrections:** an unconditional three-pivot B-spine on U₃ₚ; its exit conditions are ordinary fixed-denominator divisor events (§3.2). The middle residual is **(p+4)/(4pB)**, not numerator one. The board's explicit one-pivot divisor formula also needs a coprimality branch qualification; the unrestricted operation simply cancels q after dividing a target by q. The omission at p = 5, q = 3, held denominator 60 is witnessed by `(5,20,60) → (6,12,60)`.
2. **CERTIFIED, board Astra/Argon/Fable:** q = 2 pivot seed components and the four-particle collision seed component can be trapped despite ES. At p = 1321 they both have 20 vertices but respectively **57 and 47 edges**: they are different graphs. At p = 14281 the respective sizes are 36 and 92. Fable reports 21 q = 2 trapped primes below 10⁵, including composite-side-number traps, and Argon reports q = 5 trapped at 76/83 Mordell-hard primes below 30000. This work independently reproduces **all 21 listed q = 2 traps**, not a new census of every prime below 10⁵. The four-particle and q = 5 counts are attributed board results, not reruns here.
3. **PROVED, board parity audit by Astra and Fable:** pairing the sterile part only forces an even certifying count, and zero is even. The purported odd-square detector fails: d₁(9) = d₁(49) = 2, where d₁ counts divisors congruent to 1 modulo 4. The weighted (★)-word proposal already has empty support at 409. This closes those displayed parity proposals, not all possible parity arguments.

**Assessment.** The board's caution that q = 2 traps need not have prime side numbers was pertinent. Its suggested “first q = 3 trap > 10¹⁵” was unsupported and is now contradicted by finite examples below 10⁷. No conclusion about necessity of B2 for *every possible* ES proof follows.

## 2. Questions and answers

**Q3 (formerly CONJECTURE, now refuted by CERTIFIED counterexamples).** For every prime p ≡ 1 (4), C₃(p) ∩ (3ℕ)³ ≠ ∅.

**Precise computational questions.** Can complete, denominator-uncapped exploration find a finite closed seed union missing T₃(p)? What are its minimum target distance (∞ for a trap), cardinality, and layer sizes? Does the conditional distance among successes grow with p? Are the particular B-spine windows already explicitly present in the requested files?

**Answers.** Two traps; distances ∞; complete certificates in §3.3. Successful distances remain small in this sample, but a finite-valued universal depth bound is impossible because Q3 is false. The B-spine's *selection rule* is not explicitly present in the three files; its underlying divisor-window test is already present. Full exits need both Type I and Type II branches, not just Type II (§3.2).

## 3. Mathematics and exact experiments

### 3.1 Complete fibres, finiteness, and the two implementations

**Lemma 1 (PROVED; standard two-unit-fraction factorization).** Let a/b > 0 be reduced. The positive unordered solutions of 1/y + 1/z = a/b correspond bijectively to

    d | b²,  1 ≤ d ≤ b,  d ≡ −b (mod a),
    y = (b+d)/a,  z = (b+b²/d)/a.

*Proof.* Rearranging gives (ay−b)(az−b) = b². Each factor is positive, since a/b > 1/y and > 1/z. Taking the smaller factor gives d ≤ b. Conversely gcd(a,b) = 1 makes d invertible modulo a; from d ≡ −b follows b²/d ≡ −b, proving integrality of both denominators. Substitution proves the identity. ∎

For a held x on U_N use a/b = (4x−N)/(Nx), reduced by gcd; no denominator cutoff is introduced.

**Lemma 2 (PROVED).** U_N is finite, and the complete seed union can be enumerated without exploring every member of U_N.

*Proof.* For a sorted solution, N/4 < x ≤ 3N/4. With x fixed, Lemma 1 gives finitely many pairs. Alternatively y ≤ 2Nx/(4x−N) ≤ 2Nx and z = Nxy/(4xy−N(x+y)) ≤ Nxy ≤ 9N⁴/8. Thus every BFS terminates in principle. Expanding all three fibres of every reached vertex gives exactly the seed union. ∎

**PROVED algorithmic optimization.** A coordinate fibre need only be expanded once, when the first vertex containing it is removed from the BFS queue. That vertex has minimum possible distance among all vertices containing the coordinate. Every vertex in its fibre is one edge away, so later expansions cannot discover a vertex or a shorter distance that the first expansion missed. Seeds are initialized together; target distances are minima over the whole completed union, not first paths in a depth-first walk.

**Implementation / verification.**

- `scripts/z47_q3_pivot_search.py`: independently written BFS; streamed prime-power divisor recursion; exact integer identities on every generated triple; a 200000-vertex emergency limit and per-prime timeout produce **CENSORED**, never TRAP. All completed cases exhaust the queue, even after finding a target. The recorded `vertices` field is **the total seed-union size**, not necessarily one connected component and not |U₃ₚ|. Individual component sizes are additionally extracted for the trap certificates.
- `scripts/z47_q3_pivot_fable.py`: archived board script from `/tmp/z47q3/a2.py`, with only an attribution/caution header added. Its independent Pollard-rho factorization and unoptimized fibre enumeration are used by `z47_q3_pivot_verify.py` in a fresh BFS, not by the new explorer.
- Factor proposals are checked to multiply to the input and have prime factors. SymPy 1.14's documented deterministic seven-base Miller–Rabin test below 2⁶⁴ is used explicitly, bypassing its optional GMPY probable-prime shortcut and factor cache; a full recursively checked Lucas n−1 criterion handles any larger factor in the main scan. The seven bases and range were checked against the installed `sympy/ntheory/primetest.py` source. Fable's original probable-prime bases are **not** trusted as a proof: its factors are checked separately. The largest prime factor in the trap certificates and reference validation is **35 189 583 507 541 < 2⁶⁴**.
- `scripts/z47_q3_pivot_analyze.py` imports neither explorer. From the saved factorizations of every reduced b it regenerates **every** admissible divisor, verifies every corresponding neighbour lies in the saved set, checks all seeds, checks target avoidance, and checks each component contains a seed. This verifies full closure independently of search order and caching.

**CERTIFIED validation:** 142 reference comparisons, all matching exact vertex counts, layer counts and minimum distances: 21 q = 2 fixtures plus 121 q = 3 fixtures. The latter include all 83 Mordell-hard primes below 30000, all 27 of Astra's reported adversaries, every one of the 14 (★)-failures through 8 813 281, all three b = 1 failures, 3361, and 5101441. In particular 5209 and 15289 require 5 steps, and 104161 requires 7, agreeing with the corrected board claims.

The 17 early adversaries reconstructed from the board's A,B-prime/no-mod-7-exit rule are

    2689, 5209, 15289, 29401, 67369, 68041, 68209, 70729,
    92569, 95089, 101641, 104161, 125329, 134401, 146161,
    160441, 181609.

The ten later ones are 210169, 287281, 291481, 305761, 357169, 365569, 400009, 428401, 437809, 443689. Their distances are 4 except 400009 and 437809, which require 5.

### 3.2 Spine/window closure note, with a further branch correction

**Proposition 3 (PROVED; board Argon, corrected by Astra).** Put B = (p+3)/4. For p ≡ 1 (4), the following are valid positive pivots:

    (p,4p,12p)
      → (p,12B,4pB)               [hold p]
      → (4B,12B,pB)               [hold 12B]
      → (3(B+e),3(B+B²/e),pB)     [hold pB; e | B²].

*Proof.* The first residual is 1/(3p), and the displayed first split sums to it because p+3 = 4B. The second residual is (p+4)/(4pB) = 1/(4B) + 1/(pB). The third is 1/(3B), and the usual splitting identity with d = 3e gives the last two coordinates. All entries are positive integers. ∎

The A-branch, A = (3p+1)/4, similarly contains

    (p,4A,12pA) → (A,4pA,12pA)
      → (A,3pA+d,3pA+9p²A²/d),  d | 9p²A².

**PROVED (full exit condition).** Hold 3K, K = B+e, in the final B-spine vertex. After dividing a target by 3, the remaining equation is

    1/y + 1/z = (4K−p)/(pK) = m/(pK),   m = 4e+3.

When p ∤ K this is reduced, and exits are exactly divisors D | p²K² with D ≡ −pK (mod m). The p-adic possibilities give two branches:

    Type II: D = p d, d | K², d ≡ −K (mod m);
    Type I:  D = d, d | K², d ≡ −pK (mod m),

with D = p²d the reversed Type I pair. In particular the Type II solutions are

    (K, p(K+d)/m, p(K+K²/d)/m).

For this B-spine at a prime p ≥ 5, p ∤ K indeed holds: otherwise p divides both B+e and B+B²/e. Dividing the spine vertex by p would give a member of U₃ with two coordinates divisible by 3. Direct enumeration gives U₃ = {(1,4,12),(1,6,6),(2,2,3)}; the only such member is (1,6,6), forcing the remaining coordinate B = 1 and p = 1, impossible.

**PROVED correction to the board's “exactly Type II” wording.** The *locations* are standard windows, but all exits are not exclusively Type II. At p = 13, B = 4, e = 1, K = 5, m = 7, divisors of K² are {1,5,25}, none ≡ −K ≡ 2 (7). Thus there is no Type II exit at this held coordinate. Nevertheless

    (13,52,156) → (13,48,208) → (16,48,52)
      → (15,52,60) → (15,30,390)

is a valid four-pivot path. It gives 4/13 = 1/5 + 1/10 + 1/130, a Type I solution. The final divisor is d = 5 ≡ −pK (7). The script `z47_q3_pivot_toys.py` checks these identities. This correction does not weaken the B2 diagnosis; both branches are tied-class divisor events.

**PROVED sufficient exit (board Astra; an equivalent Type II proof).** If p ≡ 1 (8), K = (p+7)/4 is even and coprime to 7 unless p = 7, which is excluded. An odd prime ℓ | K with (ℓ/7) = −1 supplies the three nonresidue divisor classes through ℓ,2ℓ,4ℓ | K². The divisors 1,2,4 supply all three residue classes. Thus divisors of K² cover every unit modulo 7, in particular −K, and give a Type II depth-at-most-four exit. The assumption on ℓ is not automatic.

**Answer to the grep drop-condition (source inspection, not a novelty theorem).**

| requested file | what is explicitly there | exact selector e ∣ B², m = 4e+3? |
|---|---|---|
| `CAP_POINTWISE.md` §§2–3 | general Type II test d ∣ K², d ≡ −K (m); square-shot subfamily distinguished | No |
| `FORCED_WINDOW.md` §2, Prop. 2.1; §8.6 | general window/least-residue event; the fixed window m = 3 and K = (p+3)/4 | No |
| `DETERMINISTIC_EXISTENCE.md` §§3.4,6–7 | general divisor-ratio box and subgroup forcing | No |

**Assessment:** the literal drop-condition “already explicitly listed” is not met, but the arithmetic test is old; only its accessibility by this three-step path was added by the board. The proper short diagnostic is therefore the spine plus the two exit branches, not a new window-existence mechanism. The new traps, rather than this dictionary, justify the present longer memo.

### 3.3 Certified q = 3 traps; ES still holds

**Theorem 4 (CERTIFIED, computer-assisted).** Q3 fails at both primes in the following table. Vertex/edge counts are for simple graphs on sorted triples, no self-loops.

| p | p mod 840 | seed-union vertices | individual component sizes | edges | coordinate fibres | layer counts, depths 0…4 | targets |
|---:|---:|---:|---|---:|---:|---|---:|
| 7 909 441 | 1 | 57 | 53, 4 | 221 | 108 | 3, 11, 2, 17, 24 | 0 |
| 8 604 961 | 1 | 76 | 72, 4 | 394 | 146 | 3, 12, 2, 17, 42 | 0 |

*Certificate proof.* U₃ has exactly the three members listed in §3.2, by Lemma 1 and the bound x ∈ {1,2}. `verification.json` supplies a finite set S for each p containing all three scaled seeds. Every member satisfies the cubic exactly. For every coordinate occurring in S, the certificate gives reduced a,b, the prime factorization of b, and the complete list of d ≤ b dividing b² with d ≡ −b (a). Every resulting triple belongs to S. Consequently S is pivot-closed. Each of its two connected components contains a seed, so S equals C₃(p), not merely a closed superset. No member has all coordinates divisible by 3. The independent graph implementation and the static checker both verify every assertion. ∎

The larger component contains the seeds `(p,4p,12p)` and `(p,6p,6p)`; the four-vertex component contains `(2p,2p,3p)`. Thus checking just the displayed B-spine seed would not have sufficed to refute the stated *union* conjecture; all seeds have been included.

**CERTIFIED side numbers.** Write A = (3p+1)/4, B = (p+3)/4, C = (p+1)/2, K₇ = (p+7)/4:

| p | A | B | C | K₇ |
|---:|---|---|---|---|
| 7 909 441 | 5 932 081 prime | 1 977 361 prime | 47·84 143 | 2·988 681 |
| 8 604 961 | 6 453 721 prime | 2 151 241 prime | 4 302 481 prime | 2·1 075 621 |

Both odd factors of K₇ are prime and ≡ 1 (7), so Astra's sufficient exit condition fails. The first trap has **composite C**; the second has all three A,B,C prime. Therefore a q = 3 trap also need not have every first-generation side number prime.

**CERTIFIED ES witnesses, independently checked by integer cross-multiplication:**

    4/7909441 = 1/1977365 + 1/823451902510 + 1/2245882718905774,
    4/8604961 = 1/2151243 + 1/1682872222770 + 1/134083966264014930.

They are Type II windows (m,d) = (19,725) and (11,27), with d | ((p+m)/4)² and d ≡ −(p+m)/4 (m). The stored divisor may be the complementary divisor, producing the same unordered solution. Their small-denominator offsets from B are respectively **4 and 2**, neither dividing B² since B is prime. Multiplying either solution by 3 gives a genuine target on the same U₃ₚ surface, outside the entire seed union.

**Certificate sizes / no hidden denominator cutoff.** The largest denominators in the two closed unions are respectively

    19 812 908 598 947 084 016 127 836 732,
    27 756 243 907 090 092 137 446 237 092.

Searching only moderate denominators would have been unsound. The closure tables include these vertices and all their fibres. The SHA-256 hashes of the sorted state lists are recorded in `summary.json`.

### 3.4 Search design, censored cases, and depth/size trends

**EVIDENCE (exact completed searches; independent recertification only for the fixtures and traps stated above).** Every candidate prime is deterministic-primality checked. Priorities were Mordell classes, B prime to restrict e | B², A prime, absence of an odd nonresidue-mod-7 factor of B+1, the q = 2 shadow condition A,C prime, and near-squares p = m²−3. The strongest AB/no7 scan is exhaustive over its **295 selected primes in (443689,10⁷)**; it is not a census of all Mordell-hard primes there. Beyond 10⁷, the prescribed caps select the first qualifying primes in each decade. The trend cohort selects initial Mordell-hard primes of each decade, so it is not random or representative of an entire decade.

| cohort | prime attempts | completed unions | hits | traps | censored | attempted p range |
|---|---:|---:|---:|---:|---:|---|
| board fixtures + standard hard tests | 121 | 121 | 121 | 0 | 0 | 193…8 813 281 |
| A,B prime; no7 | 458 | 457 | 455 | 2 | 1 | 463 849…1 000 418 161 |
| A,C prime shadow | 182 | 176 | 176 | 0 | 6 | 1 015 561…1 001 320 321 |
| p = m²−3 | 30 | 26 | 26 | 0 | 4 | 1 162 081…10 568 251 201 |
| trend | 334 | 334 | 334 | 0 | 0 | 10 369…100 037 569 |
| **deduplicated** | **1 076** | **1 065** | **1 063** | **2** | **11** | 193…10 568 251 201 |

Every JSONL completed record includes its minimum depth, full union size, layer histogram, number of expanded fibres, number of targets, a shortest path, and CPU time. A trap has `depth: null`, meaning ∞, not zero. Budget stops are separate records identifying the next unevaluated prime.

**Censored, unresolved by these runs:** 102159961, 1000155241, 1000190041, 1000468081, 1000672681, 1000741921, 1001063641, 10039639201, 10225658881, 10416651841, 10568251201. These are timeouts during component completion; none is reported as a trap or a completed success. All three global budget stops occurred between primes. The first near-square generator mistakenly used odd m (making m²−3 even and selecting no primes); it was corrected to even m before the retained 30-case run. That empty initial pass contributes no evidence.

**EVIDENCE, successful depth records.** Across distinct completed successes the depth histogram is

    1: 6;  3: 138;  4: 801;  5: 108;  6: 8;  7: 2.

The two maximum-depth cases are **104161** (233 vertices, 14 targets) and **4889641** (392 vertices, 13 targets). The former is independently recertified against the board script; the latter's full layer counts and shortest seven-edge path are saved in `summary.json`. The largest completed seed union has 1663 vertices. The traps are *smaller* and have saturated by depth four, despite successful instances requiring seven steps.

**EVIDENCE, trend cohort only:**

| decade starting at | count | mean minimum depth | maximum minimum depth | mean seed-union size |
|---:|---:|---:|---:|---:|
| 10⁴ | 26 | 3.769 | 5 | 312.4 |
| 10⁵ | 80 | 3.875 | 7 | 440.8 |
| 10⁶ | 80 | 3.763 | 5 | 592.1 |
| 10⁷ | 80 | 3.775 | 5 | 767.0 |
| 10⁸ | 68 | 3.676 | 4 | 959.8 |

**Assessment.** Conditional on success, this sample shows increasing component size but no increasing mean shortest depth, certainly no evidence requiring depth proportional to log p. It also does not prove bounded successful depth. The correct unconditional distance distribution has an atom at ∞, already at 7.9·10⁶. Extrapolating a finite-depth law without that atom is false. No claim is made that 7 909 441 is the *least* Q3 trap; only the smallest found in this selection.

**Resources / reproducibility.** Python 3.12.9, SymPy 1.14.0, `uv run`; every computational process was run under `ulimit -v 8000000` and an outer `timeout`. Per-prime wall-time limits were 30 seconds, 20 for near-squares, 90 for reference validation. Selection/search runs plus repeated validation used approximately **4.4·10³ CPU seconds (74 minutes)**, below the two-hour allowance. Stored data are below 1 MB. Representative commands:

    ulimit -v 8000000
    timeout 120 uv run python scripts/z47_q3_pivot_search.py one --p 7909441 --out /tmp/q3-one.jsonl
    timeout 120 uv run python scripts/z47_q3_pivot_verify.py --quick --out /tmp/q3-quick.json
    timeout 60 uv run python scripts/z47_q3_pivot_analyze.py
    timeout 220 uv run python scripts/z47_q3_pivot_toys.py

For full replication, the search modes are `q2`, `baseline`, `adversarial` (CPU budget 1400), `shadow` (1200), `trend` (1200), and `near` (400; `--seconds 20`); use distinct JSONL output paths. Timing-based endpoints can differ across hardware, so the retained files specify the exact tested primes. `verification.json` is the portable complete trap certificate; the static analyzer is the cheapest verification and needs no refactorization.

### 3.5 Controls

**EVIDENCE (exact single-implementation toy computations).** The numerator-8 analogue with q = 7 has nonempty seed unions of sizes 38,75,81,73 at p = 11,17,131,241, respectively, all closed and target-free. These are consistent with the known genuine failures of 8/p; the q = 3 counterexamples differ because their targets are nonempty. For numerator 4 at n = 9 and 25, q = 3 reaches targets at depths 0 and 1, with union sizes 29 and 128. These unrestricted mixed/scaled solutions do not contradict the Type I/II odd-square obstruction. The algebraic spine uses 4−3 = 1, but that identity never proved target intersection; changing to 8−7 = 1 does not supply a transport theorem either.

## 4. All 17 FRONTIER screening lines

**Assessment of the proposed universal Q3 proof route**, not of the validity of the negative finite certificates:

| line | result | reason |
|---:|---|---|
| 1, odd squares | N.A. | Full U_N solutions are unrestricted; mixed/scaled square solutions are legitimate. No Type I/II existence theorem at squares is asserted. |
| 2, 8/131 and 8/241 | PASS | Explicit target-free q = 7 control components; the spine alone does not claim success. |
| 3, numerator-uniform laws | PASS | No such transport law is used; the controls refute an unqualified one. |
| 4, tied modulus | FAIL | Exit modulus m = 4K−p, with a divisor of p²K² in class −pK; no theorem forces a hit. |
| 5, fixed p | PASS | Every closure and every witness is verified at the prescribed p; no averaged theorem is invoked. |
| 6, count scale | N.A. | No power main term or count-versus-error proof is proposed. |
| 7, one-sided only | PASS | Only existence/nonexistence of a reachable target; no false uniform two-sided asymptotic. |
| 8, bounded formal menu | FAIL for the displayed spine | Its formal preamble supplies no arithmetic exit. The general growing graph is not refuted by the fixed-menu theorem; it is refuted here by actual closed unions. |
| 9, class not parity | FAIL | Missing mod-7 forcing and later class hits cannot be replaced by subgroup/parity information. |
| 10, pooling large primes | PASS | No pooling or privacy-violating collision claim. |
| 11, signed reflection | PASS | Every move stays positive; the obstruction persists without signed points. |
| 12, relaxation transport | FAIL | Solubility at 3p plus pivot rewriting does not transport to a reachable solution at p. |
| 13, BM shortcut | PASS | No local/global or Brauer–Manin sufficiency is asserted. |
| 14, test primes | FAIL as a universal claim | All original fixtures pass, but the expanded test set gives two counterexamples. |
| 15, Mordell/near-squares | PASS | Both traps are 1 (840); the explicit near-square sample includes censor accounting. |
| 16, thin-family transfer | PASS | No thin-family identity is transferred to all primes. |
| 17, covering via small factors | N.A. | No coset-covering proof is used; complete exact factors, including large ones, enter the closure certificates. |

## 5. New-theory direction: factor-certified closed-component templates

**Definition / Assessment.** A *closed-coordinate certificate* for a pivot seed set consists of a finite triple set S and, for every coordinate x occurring in S, a complete factor-certified residual fibre. It is a finite obstruction certificate when S contains the seeds, is closed under those fibres, and avoids the target. This is ordinary hypergraph saturation with arithmetic edge certificates, not a newly claimed general mathematical theory. Its possible new application is to classify symbolic families of trapped positive Egyptian-fraction rewrite systems rather than conjecture their universal connectivity.

**PROVED first theorem.** The certificate conditions are necessary and sufficient for containing the whole seed union inside a target-free finite set. Sufficiency is induction on pivot-path length. Necessity follows by taking S to be the seed union and applying Lemmas 1–2. If every component of S contains a seed, then S is exactly the seed union. This is the completeness principle used in Theorem 4, not a positive ES mechanism.

**Testable toy: a four-vertex seed island.** For primes p > 5 with p ≡ 1 (5), define

    V0 = (2p,2p,3p),
    V1 = (p+1,3p,p(p+1)),
    V2 = ((6p+4)/5,2p,3p(3p+2)/5),
    V3 = ((6p+9)/5,2p,2p(2p+3)/5).

**PROVED.** The fibre at 3p consists exactly of V0,V1, and the fibre at 2p consists exactly of V0,V2,V3. The first assertion is the factorization of p² for residual 1/p. For the second, the reduced residual is 5/(6p); its divisor parameter is d | 36p² with d ≡ −6p (5). Write d = c pʲ, c | 36, j = 0,1,2. Since p ≡ 1 (5), only c = 4,9 work; complementary pairs yield the three displayed triples. ∎

The other occurring coordinates are the *ports*: their complete fibres decide whether the island is closed. **CERTIFIED toy result:** at both new traps every port stays inside these four vertices; this is precisely the four-vertex component of the seed `(2p,2p,3p)`. The other seed component is separately closed at 53 or 72 vertices. The larger component's detailed factor data, rather than a parity colour alone, explains the lack of exits. The full unions have respectively 37/20 and 44/32 vertices with one/two coordinates divisible by 3, and none with three.

**Open research question, not a conjectured answer.** Can one give finitely checkable symbolic factor-class conditions on p that close both this island and a larger seed template for infinitely many primes? Even a conditional infinite family would require admissibility and a correctly stated prime-values hypothesis (quadratic side polynomials are not covered by Dickson's linear-forms conjecture). No such family is proved here. Its output would classify failure of a method, not failure of ES. A positive replacement would have to add a genuinely new move or an independently justified escape invariant; merely increasing pivot depth cannot repair Q3.

## 6. Verdict and next steps

**COLLAPSES, exact scope:** universal q = 3 pivot reachability from p·U₃. The failed implication is **known seed existence + closure under all positive two-term re-splittings ⇒ intersection with (3ℕ)³**. It is false at two certified primes, even though ES holds there. The board's spine/window explanation remains useful after adding the Type I exit branch; the arithmetic gap is still B2, but here an actual component obstruction, not merely a barrier heuristic, ends the proposed route.

**Assessment / promise:** 0/5 as a proof of ES via Q3; **1/5** for finite-component classification and prevention of rediscovery. No general no-go for other q, enlarged move sets, or global ES arguments follows.

**Concrete next steps:** independently review the small static certificates; update the parent campaign's Q3 status from open to refuted; only then consider a narrowly scoped symbolic trap-family classification. No further open-ended Q3 success search is warranted, and none of the 11 timeouts needs resolution to establish the counterexamples.
