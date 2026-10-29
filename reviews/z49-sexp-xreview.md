# z49 sexp — hostile cross-model review

**Verdict: SOUND-AFTER-REPAIRS (minor repairs only).** No fatal or major mathematical defect found. In particular, **Theorem 2.1 and its fixed-H prime-density consequence are SOUND**, relative to the stated fundamental lemma and the supplied atomic-Janson proof. The lower-side conclusions remain conditional, not proved instances of FT or FT_β.

Reviewed `CONJECTURE_S_MODEL.md` at `side-agent/z49-sexp`, commit `7d7edb4d34588b024b5d55c55a696cd0cc8af3f2`, in worktree `0051`. This report and its computations are in the reviewer's own worktree `0025`. The preceding internal review concerns an older version; its substantive repairs are present in the version reviewed here.

| Claim | Verdict | Scope |
|---|---|---|
| Lemma 1.1, odd-pair colour | SOUND | Already explicit in z48; not a new colour theorem |
| Theorem 2.1 | SOUND | Uniform fibre mass, atomicity, local loads and compatible-pair sum check out |
| Theorem 2.6 | SOUND | The same-d cutoff really controls the hubs |
| Fixed-H prime consequence | SOUND | Exact limiting density, not merely a limsup |
| Theorem 3.4 | SOUND-AFTER-REPAIRS | Minor logarithmic-factor correction; still conditional on FT |
| Theorem 3.5 | SOUND | Conditional on both parts of FT_β |
| Corollary 5.1 | SOUND-AFTER-REPAIRS | Same minor correction; relative to FT, the imported energy lemma and the stated analytic input |

## 1. Findings by severity

### Fatal

None found.

### Major

None found in the revised mathematical argument. The earlier certain-event, FT-domain and digit-resolution defects have been repaired. FT and FT_β are substantial unproved hypotheses, but are now labelled as such rather than smuggled into a PROVED conclusion.

### Minor 1 — A logarithmic factor disappears in Theorem 3.4

At `CONJECTURE_S_MODEL.md:475`, FT and §3.4 give an error

```
O((log L)^2 m_c^(-1/2)),
```

not the printed `O(m_c^(-1/2))`. The implicit constant cannot absorb a growing logarithm. Retain that factor, also wherever this displayed load bound is reused in §5.

**The conclusions survive without a stronger hypothesis.** For `m_c ≥ Y = L^3(log L)^C`,

```
L (log L)^2 / (sqrt(m_c) log m_c)
 ≤ L (log L)^2 / (sqrt(Y) log Y) = o(1).
```

Thus the corrected error is still `o(log m_c/L)`. The main load term has the advertised slack, so both the ordinary LLL support sum and the stronger `1/64` transfer support sum still follow.

### Minor 2 — The odd-pair colour is prior work, not a new idea

The summary's “New ideas / Colour” item (`:26`) should cite `FOREST_CONNECTIVITY.md §2.3(C1)` (and its §2 proof). That passage already states exactly that an odd–odd edge is bichromatic iff its endpoints are not both 1 modulo 4. It even works for `n ≡ 1 (4)` with unit endpoints; `n ≡ 1 (8)` is stronger than needed here.

Keep Lemma 1.1 as a convenient self-contained restatement, but give it zero novelty credit. This does not diminish the genuinely new smooth-conditioning argument.

### Minor 3 — A real boundary bug in the finite LLL checker

In `scripts/z49_sexp_lllcheck.c`, `phiQinv` treats every prime `p≤Y` as if at least its unit digit were fixed. With the definition “largest prime power strictly below Y”, **when Y is prime, `kpow[Y]=1`**. That prime is not fixed by Q. The code then uses `p^e` rather than `φ(p^e)` in its denominator, undercounting probabilities and loads.

Concrete reproducible case: `H=Y=11`, `Q=2520`. The five live nontrivial edges are `(a,11)` with `a=1,2,3,4,6`. Each has conditional probability `1/10`, so **S=1/2**. The program reports **S=0.455**, namely `5/11`. Independent exact CRT enumeration confirms the former value; see `data/z49_sexp_xreview/checks.txt` and `lll_prime_cutoff.txt`.

Repair `phiQinv` by treating `kpow[p]==1` as an unconditioned unit coordinate. Alternatively change the Q definition consistently to include the prime cutoff itself. **The archived runs at Y=600 and 1500 are not affected**, and I reproduced their reported successful LLL quantities. This is a checker boundary defect, not a counterexample to a theorem or to those archived finite certificates.

### Minor 4 — Avoid literal “all edges” after excluding the two certain ones

At `:488`, write “all nontrivial edges in the bad family are avoided”. The actual statement “all edges are avoided” is false on this fibre: `(1,2)` and `(2,3)` occur certainly. The family definition in §3.1 is already correct, and both omitted edges are non-certifying, so this is a prose correction only.

## 2. Atomic Janson: checked, not assumed by analogy

I read the proof in `paper/es-subexp-note.tex`, §“A Janson-type inequality and the lower bound on the Haar side”. Its compatible-event inequality has the correct direction: after conditioning on an agreeing atom, delete its coordinates from each compatible event, enlarging those events and decreasing avoidance. The lopsided conditional estimate follows by splitting conflicting and nonconflicting predecessors.

In the Janson ordering argument, `B_i^d` involves only coordinates outside `E_i`. For a compatible predecessor the residual event `E_j'` has no new conflicts: every event conflicting with it also conflicts with `E_j`. This justifies the same K in the intersection subtraction. No Harris/FKG assumption is being substituted for the categorical-coordinate argument.

Taking `x_E=2P(E)`, the two `1/8` hypotheses give `x_E≤1/4`, conflict x-mass at most `1/4`, and `K≤exp(1/3)`. The argument works for an **indexed** family. Conditional duplicate atoms must contribute their full probability to Δ; the note does not illegitimately discard them.

### Atomicity on a fibre

Every endpoint's small part uses primes ≤Y, and its rough part is squarefree and uses primes >Y. Within a pair all parts required to be coprime are indeed coprime. After fixing the small coordinates, a live event fixes exactly one unit residue at each prime dividing `R=r_1r_2`. The residue cannot be zero: at a prime dividing one endpoint, the other endpoint is a unit. Thus

```
P(E | z) = 1/φ(R)
```

is exact. The liveness congruences (2.1) have invertible coefficients. Conditioning an infinite p-adic coordinate causes no measure-theoretic problem: the finite family uses only finitely many digits, so the proof can first condition that finite quotient. Higher rough digits do not enter.

### Local loads

The split at `p=H^(1/16)/S_0^2` (or `H^(1/2)/S_0^2`) really puts the divided rough variable above the progression modulus in the small-p case. In the large-p case the lost count of smooth parts is only S_0, and

```
H^(-1/16+3/400+o(1)) = o(H^(-1/30)).
```

The other endpoint retains its harmonic smooth-part weight. Summing loads over the at most `2L/log Y` coordinates of an event gives `o(1)`. Also `R≥H^(9/16-2/400)>H^(1/2)`, so the individual-probability condition holds. This verifies both Janson hypotheses uniformly in z, not merely on an average fibre.

## 3. The uniform mass claim is genuinely proved

This was the most important potential failure point. It passes.

For the sieve in a dyadic block, `q≤4H^(1/400)` and `X≥H^(1/20)`, whereas the sieve level is

```
Y^(log L) = exp(9(log L)^2) = H^o(1).
```

In each reduced progression the remainder for a squarefree sieve divisor is O(1). Summing those remainders at that level is negligible against `X V(Y)/q`, uniformly in the residue. Thus no distribution theorem for smooth moduli or for primes in growing progressions is hidden in the mass estimate: this is a sieve of **integers in a progression**.

The removals also have uniform room:

* Squareful rough numbers cost `O(X/(qY)+sqrt(X))`; `q log Y/sqrt(X)→0` uniformly.
* Coprimality to a prescribed rough m costs at most `ω(m)(2X/(qY)+1)`, negligible uniformly for `m≤H^2`.
* The actual lower rough ranges exceed `H^(1/20)`, and `4s_2` and `s_1` satisfy the stated modulus cutoff.

Consequently the rough harmonic mass for each small pair is bounded below by

```
c L^2 V(Y)^2 / (φ(s_1)φ(s_2)),
```

with **the same c for every z**. Restricting to squarefree small products `s_1s_2≤S_0` gives a legitimate subfamily, and replacing `1/φ(s_i)` by the smaller `1/s_i` is in the safe direction. The Rankin tail is

```
exp(-L/(3600 log L)) (log Y)^O(1) = o(1),
```

while the retained Euler product is `≫(log Y)^2`. This cancels both roughness losses and proves the claimed `μ(z)≥cL^2`, including the class of one. It is not an extrapolation from the finite μ(z) experiment.

The prose sometimes uses `μ(z) ≍ L²`; the proof only needs its displayed lower bound. An upper bound of that order can also be obtained from the corresponding uniform upper sieve and the convergent-factor comparison of the smooth Euler products. No upper bound is needed for the Janson conclusion.

## 4. The pair sum Δ survives the first-term audit

The four shared rough factors g,h,j,k are pairwise coprime. Their product is exactly the shared modulus, and the decomposition gives

```
lcm(R,R') = Dabcd.
```

There are two necessary checks which are easy to miss:

1. **Equal endpoint sums.** Compatibility alone does not bound D if the sums agree. Here distinctness gives `u≠u'`, hence `h | u-u'`, and `gjk≤uu'`. Therefore `D≤H^(3/8)`, below the large-endpoint scale. For unequal sums, divisibility of their nonzero difference gives `D≤3V'`. The needed `D≤4V'` is justified in both cases.
2. **Smooth factors in the extra CRT periods.** Given a,b, compatibility fixes c modulo hj and d modulo gk. Liveness independently fixes c modulo `s_2'` and d modulo `s_1'`. Rough/smooth disjointness gives the full product periods `hj s_2'` and `gk s_1'`. Coefficients are invertible; there is no missing common-factor correction.

The c,d harmonic product expands to exactly

```
1/(D s_1's_2') + 1/U' + 1/V' + s_1's_2'D/(U'V').
```

Keeping `D≤4V'` makes its error `O(S_0² H^(-1/16))`. The a,b product and its error after multiplication by `1/D` have the bounds stated in the note. Dropping remaining restrictions then only enlarges a positive sum. Finally, the `4^ω(D)` assignments are paid for by

```
Σ_(D>1 rough squarefree) 4^ω(D)/D² ≪ 1/Y,
Σ_(D≤4H) 4^ω(D)/D ≪ L⁴.
```

Thus `Δ≪L⁴(log Y)⁴/Y + L⁸H^(-1/16+6/400)=o(1)`. The exponentially small H-error beats its positive powers of S_0 and L. Nothing in this calculation assumes conditional atoms remain distinct.

**Conclusion:** fibrewise Janson followed by averaging is valid and proves Theorem 2.1.

## 5. Covering bound and prime consequences

**Theorem 2.6.** Lemma 2.5 follows by ordinary Jacobi reciprocity for odd d, including composite d. The progression `A≡-1 (4d)` is reduced even when d is not rough; its sieve density is at least the required multiple of V(Y). Its lengths and the squarefree removal are uniform for `d≤H^(1/10)`.

For equal d, orienting the distinct quotients `v<v'` forces `v'≥v+d`. After fixing v, g lies in a reduced progression modulo d, and the v' residue is then fixed by v. Switching the order is legitimate and yields `Δ_a≪L³/Y+L³/N_0=O(L)`. For unequal d, `g≤|d-d'|≤H^(1/10)` makes both quotient ranges long compared with d,d'; orienting `d'>d` gives the additional `1/g` saving. Thus `Δ_b≪L⁴/Y`. These errors are smaller than `μ≫L²/log L`.

**Fixed H primes.** `FOREST_H4 Proposition 5.1` already proves existence and exact CRT identification of the limit. For `p>H`, endpoints are coprime, their product divides `lcm(1,…,H)`, and edge/slot predicates depend only on finitely many reduced classes modulo `4 lcm(24,1,…,H)`. PNT in these **fixed** progressions identifies the relative density inside `p≡1 (24)` with δ(H). Removing finitely many small primes changes nothing. Therefore the stated upper bound is an actual limiting-density theorem for every fixed sufficiently large H. No growing-H uniformity is needed, and demanding it here would be an erroneous objection.

**Corollary 5.1.** The repaired argument uses lumped prime coordinates only for dependence and the twist, then actual absolute-index digits for the energy/BRW construction. That is the required interface. The support sum follows from `Σ log m_c≤log(av)≤2L`, including the corrected error from Minor 1. The imported energy/minorant bound gives `log D+log(2+K)≪L(S+L)=L³ polylog`, while `log Q=L³ polylog`. The linear transfer thus supplies `log p≪L³ polylog`; the strict range `κ<1/3` follows. The auxiliary prime forcing `p>H²` ensures infinitely many distinct primes. The squared-budget ordinary-PNT range is `κ<1/6`. I accept these **relative to the explicitly imported energy lemma and (G)**, not as independently re-proved source theorems in this review.

## 6. Lower-side hypotheses and Shiu

The exact totient ratios in Lemma 3.1 are correct, including partially conditioned prime powers. Removing the two safe-point edges leaves nonempty free support. Lemma 3.2 correctly retains the least progression member: `AB | a+v+1` and `v>a` imply `AB≤2v`. This handles the first term before summing over a.

For Lemma 3.3, `τ_Q` is multiplicative with uniform bounds `τ_Q≤τ`; its Shiu constants do not grow with Q. With `X'>2q`, the interval length is comparable to `qX'` and the stated fixed Shiu parameters are admissible. Prime-power q has `q/φ(q)≤2`. For small blocks, the supplied `q^(3ε)` bound, `ε=1/48`, and the split at `q=L³` correctly give the stated error. No extra pointwise divisor-distribution conjecture enters the smaller-endpoint result.

The revised FT domain saturates the conditioned p-power in B and excludes `p|a`. On writing `s=ABt`, its progression is equivalently

```
t ≡ ((a+1)/B) A^(-1) (mod p).
```

This is well-defined and gives precisely period ABp. The smaller cutoff for the first term only increases the upper bound. The residual-prime long part retains the required `p^-k` saving from `a≡-1 (p^kB')`. Hence FT really implies the needed v-load estimate, modulo Minor 1.

**Do not overgrade the conditional part.** FT is still a hard, pointwise-in-prime first-term estimate. FT_β includes the entire weighted-load estimate and weighted-mass estimate as assumptions, not merely an already-proved weighted variant of FT. Theorem 3.5 is a valid LLL implication, but does not establish either assumption. Finite actual-load certificates cannot prove them.

## 7. Independent bounded checks

All executions used `ulimit -v 8000000` and explicit timeouts. Existing tests were inspected first. The additional script is `scripts/z49_sexp_xreview.py`; its output is `data/z49_sexp_xreview/checks.txt`. It uses standard-library arithmetic, no author implementation, and streams pairs (180 endpoints, 1,040 events; no dense pair array).

* 1,069 compatible indexed-pair/fibre checks verify the full smooth-factor CRT constraints and lcm decomposition, including 47 equal-sum cases and 1,019 cases with nontrivial smooth factors. No failure. There were no duplicate atoms in this finite sample; indexed-duplicate validity is checked analytically above, not claimed numerically.
* Direct enumeration of **FT itself**, missing from the author's load experiments, at H=1000 and Y=10,30,100 verifies the first-term-plus-long-part domination on every active coordinate. The maxima of `q FT(q)/L²` are 1.779, 2.358 and 3.185, respectively. These arbitrary finite cutoffs neither prove nor refute the asymptotic FT hypothesis. They also illustrate why actual loads are not measurements of the enlarged FT sum.
* Exact CRT at H=Y=11 establishes the finite-checker bug in Minor 3.
* The nine requested hard primes give H₄ = 5,7,5,29,29,17,19,26,51, respectively, with agreement between slot and Legendre tests. Forty-nine odd-square controls have no coprime certificate edge. Full positive three-unit-fraction searches for numerator 8 at n=17 and 241 return zero. The numerator-4 colour/slot bridge is not being promoted to a numerator-blind existence theorem.
* Reused `scripts/review_haar_janson_bf.py` with seed 49049 and 20 instances: 3 satisfy its LLL search, all conditional and Janson assertions pass; 17 do not satisfy that search and are not counted as Janson successes. Output: `atomic_janson.txt`.
* Recompiled the author's C checker and reproduced H=100000,Y=1500: S=19.586 and maximum event-support `2w` sum 0.2390. At Y=600: S_β=40.467 and maximum weighted load 0.2194. The repaired direct finite-beta argument is valid although beta exceeds the literal asymptotic lemma's stated range. Outputs: `lll_1500.txt`, `lll_600.txt`.

These are finite arithmetic/implementation checks, not numerical proofs of the asymptotic sieve, FT or the energy lemma.

## 8. Novelty grades (Assessment)

Scale: 0/5 = already explicit or a restatement; 5/5 = major new mechanism. These are **campaign-relative**, not literature-priority claims.

| Contribution | Grade | Reason |
|---|---:|---|
| Theorem 2.1: smooth conditioning with uniform fibre mass and retained Δ control | **4/5** | Genuine removal of both roughness losses; new constant-order log-square survival exponent |
| Fixed-H prime-density improvement | **3/5** | Genuine stronger theorem about primes, but its transfer is an immediate existing CRT/PNT consequence |
| Lemma 1.1 | **0/5** | Explicit z48 corollary |
| Theorem 2.6 | **2/5** | Useful new bound for this coordinate; close adaptation of the existing rough-modulus/hub-cutoff argument |
| Residual mass and smaller-endpoint Shiu loads | **2/5** | Useful prime-unit/non-adaptive bookkeeping; substantially inherited mass architecture and classical Shiu input |
| FT ⇒ exponent 3 and conditional κ<1/3 | **2/5** | Correct quantified conditional advance, with a substantial bespoke arithmetic hypothesis |
| FT_β ⇒ Conjecture S | **1/5** | Valid implication from hypotheses already containing the required weighted LLL loads and total mass |
| Empirical tail ratios | **1/5** | Calibration, not proof or asymptotic constant determination |

**Bottom line:** retain Theorems 2.1 and 2.6 and the fixed-H prime consequence as proof steps. Make the four minor repairs, keep FT/FT_β and the transfer dependencies explicit, and do not advertise the old colour law as new. No proof of ES, full Conjecture S, or growing-H upper-tail statistics for primes is supplied.
