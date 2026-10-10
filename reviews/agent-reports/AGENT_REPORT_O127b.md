# AGENT REPORT O127b — round 2 (covering paradigm, hard-prime tail, single-coefficient)

Branch `side-agent/conditional-es` (the red-team branch `side-agent/redteam-automorphic` has been
merged in so that its file could be read). New: `CONDITIONAL_ES.md` §§7–9; tools
`scripts/cond_slice_scan.c` and `scripts/cond_divtarget.c`; data `data/cond/scan_hard_1e7.txt`.

## R125 repairs (5.6 a–d), all marked "(R125 repair)"
* (a) §3.2: primitive χ* recurs along g ∈ qℕ; the conclusion is re-derived via the AP-sum
  argument (now Prop 9.1).
* (b) "OMEGA13 kills Chebotarev witnesses" is restricted to Type II, in §0, §3.2, the §5 table,
  §6 and report O127. For Type I only `ck_min ≫ log p·log₃p` i.o. is known.
* (c) The `p^{o(1)}`-to-one qualifier is restored in the §0 and §5 Cor 4.1 rows and in report
  O127.
* (d) The odd-square Lemma 5.1 is added to Prop 3.1 as item 3.

## (1) Covering paradigm — verdict: no natural covering conjecture ⇒ ES was found
**This is a negative result**, with the following proved pieces:
* **Survey (sources read):**
  * BKS arXiv:1609.06097: twisted Linnik ⇒ `K(S³) = 4/3`; big holes give `K ≥ 4/3`.
  * Sardari arXiv:1510.00462: d ≥ 5, exponent 4 optimal; d = 4 conjectured.
  * GGN cited from memory.
  * All of these are existence statements at expected count ≥ (#points)^δ. Big holes show
    that existence at smaller expected count fails at special centres.
* **Prop 7.1 (PROVED):** a `p^{o(1)}`-to-one encoding forces the ES targets to be
  power-deficient for almost all p. Those are exactly the targets where covering fails in the
  model case.
* **Prop 7.2 (PROVED):** every covering statement at Cramér scale for general unit-class systems
  with locally infinite expectation is false. The construction is a diagonal one, with
  Dirichlet primes ≡ −1 and the class −1 reserved.
* **Prop 7.3 (PROVED, using R125 Lemma 5.1):** any hypothesis depending on (dyadic size,
  `n mod Q`), with `Q ≤ n^{1/2−ε}`, that holds at one square-mimicking prime also holds at an
  odd square, where S' = 0. So a conjecture implying X_slice must either use primality
  explicitly or use E1 data at moduli `> n^{1/2}`.
* **Bright–Loughran (read):**
  * There is no BM obstruction to existence for any n ≥ 2 (Thm 1.1/1.8).
  * BM does not explain all failures of strong approximation (Thm 1.9).
  * Hence "BM is the only obstruction" is exactly ES, and its density form is false.
* **Divisor-target class (EVIDENCE):** the target `r_m | m+3`, `4 | m` fails for 23 primes up
  to 26029. So the natural class generalisation of X_slice is doubtful.
* **Strongest surviving statement:** X_slice itself (now also in a remainder form:
  `(cm − p) | (m+1) ⟺ (cm − p) | (p + c)`). The implication X_slice ⇒ ES (Thm 6.1) is PROVED
  but trivial. X_slice is ES-specific; it is not a covering conjecture.

## (2) Hard-prime tail (EVIDENCE, §8)
All 20513 Mordell-hard primes below 10⁷ satisfy X_slice. But **S(p) = 1 at p = 5101441**
(single solution g = 147, `147p+1 = 5732·130829`; re-derived in Python), and also at 2521, 5569,
21169 and 43969. The mean of S/log²p is ≈ 0.1, but its minimum keeps falling, to 0.0042. The
lower tail is heavy, consistent with Prop 7.3. X_slice is fragile and may fail for some larger
p. Any conjecture of this type should be stated for the full Type I (or Type I ∪ II) count.

## (3) Single-coefficient GRH limitation (§9)
This is now **Prop 9.1, PROVED as bookkeeping with mechanism scope**: the per-primitive-character
AP-sum GRH bound exceeds the length of the sum. The broad claim "no use of GRH helps" is
**explicitly an Assessment**. Its strongest rigorous support is Prop 7.3 applied to arguments
that see p only through `p mod q` with `q ≤ p^{1/2−ε}`.
(R127 repair: only for a *single* modulus, i.e. lcm of moduli used `≤ p^{1/2−ε}`; the joint
residues mod all `q ≤ p^{1/2−ε}` determine p, so GRH for all small moduli is not covered.)

## Weak points
* Prop 7.1's "natural ⇒ not deficient" step is an Assessment, and so is "artificial
  multiplicity reduces to the quotient".
* Prop 7.2 refutes only the *general* class statement; definable classes are tested only
  numerically.
* GGN is not checked. The divisor-target failures (`m+3`) only go up to 3·10⁴.
* A full Type I count at the singleton primes (to show that the full family is healthier)
  was not computed: my quick script had a non-terminating loop and was discarded.

## Suggested next step
Compute the full Type I ∪ II solution counts at the S(p) ≤ 2 primes. If those are also O(1),
that is strong evidence that ES at hard primes is decided at Planck scale with no margin. That
is the regime where no conjecture of any listed type can be the input.
