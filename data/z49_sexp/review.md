# Hostile referee report: CONJECTURE_S_MODEL

Reviewed the complete main note, the requested background passages, the atomic-Janson proof, the relevant implementation/output files, and Shiu's original scanned Theorem 1 (printed pp. 162–163). Line references below refer to the reviewed, unchanged `CONJECTURE_S_MODEL.md`.

## Verdicts

| Result | Verdict | Qualification |
|---|---|---|
| Theorem 2.1 | **SOUND** | Relative to the fundamental lemma and the supplied internal atomic-Janson proof. Minor estimate-writing repairs below; no substantive obstruction found. |
| Theorem 2.6 | **SOUND** | Same dependencies. The same-d hub is genuinely controlled by the cutoff. |
| Theorem 3.4 | **SOUND-AFTER-REPAIRS** | Still CONDITIONAL. Exclude the two certain events and define FT correctly for residual prime-power coordinates. The corrected long-part estimate has an elementary proof given below. |
| Theorem 3.5 | **SOUND-AFTER-REPAIRS** | Still CONDITIONAL on its explicit weighted-load AND weighted-mass hypothesis, with sufficiently large cutoff exponent. It does not require proving the unweighted FT reduction. |
| Corollary 5.1 | **SOUND-AFTER-REPAIRS** | Still conditional on corrected FT, the stated energy input, and (G), or the stated alternative analytic input. Ungroup digits for the energy/BRW step. The exponents 1/3 and 1/6 then follow. |

**No FATAL counterexample to the principal exponent claims was found.** There are MAJOR formulation/interface defects: the current literal all-edge LLL is impossible, FT is not defined on all its displayed summands, and the minimal modulus of a lumped coordinate is not its arithmetic resolution for the energy lemma. These have explicit repairs, not new conjectural estimates. The asserted transfer of the I3 unconditional refinement is not established by the cited source.

## Numbered issues and repairs

### 1. MAJOR — The lower-bound family still contains two probability-one events

**Locations:** lines 367–368, 376, 448–462, 474–481, 494–495; inherited by §5.

Lemma 3.1 acknowledges the exceptional pairs but never removes them from the family used subsequently. On the class of one, `E_(1,2)` and `E_(2,3)` are certain. Thus the literal statement at line 456, `P(no event | Q) ≥ exp(−3S)`, is false; the left side is zero. At line 448 their proposed `x_E=2P(E)` equals 2. Under the beta weights they have `s(E)=0`, `x_E=1`, and escape every coordinate-load bound.

**Repair:** At the beginning of §3 define the bad family to be all coprime edges **except** `(1,2),(2,3)`, exactly as H4_NOT_POLYLOG Lemma 2 does. Carry this convention through S, FT_beta, the avoidance statements, and the data description. Say “all nontrivial edges” rather than “all edges” at line 462. Both omitted pairs are non-certifying, so the desired conclusions are unchanged. The implementation already excludes them (`z49_sexp_lllcheck.c`, `if(s==0) continue`); the prose should match it.

### 2. MAJOR — FT's prime-power progression and summation domain do not match

**Locations:** lines 417–427 and 433–436.

The asserted period `AB p_c` is correct for an actual edge with `q|v`, but not for every B in the displayed FT sum. For `q=p^(k+1)` with `p≤Y`, an actual B must contain the **full** `p^k` dividing Q. That restriction disappears at line 427. More generally the simultaneous conditions have period

```
lcm(AB, lcm(B,q)),
```

provided they are consistent at all.

Concrete checks with `Y=10`, `Q=2520`:

* `a=7, A=7, B=1, q=16`: the displayed conditions are `s=0 mod7`, `s=8 mod16`. Their period is 112, not `AB p=14`. The first qualifying `s≥24` is 56; 70 does not qualify.
* `a=2, A=2, B=1, q=16`: they require both `s=0 mod2` and `s=3 mod16`. No s exists, so the displayed `s_*` and FT summand are undefined.

Also, the long-part argument at lines 421–422 drops its displayed factor k. It cannot deduce the claimed bound from the unrestricted `tau_Q` estimate as written. The inverse `(AB)^(-1) mod p` at line 435 does not exist for these residual coordinates.

**Repair (preserves the stated long-part bound):** Restrict the first-term sum to admissible `(a,B)`:

* `gcd(a,p)=1`, `B|gcd(a+1,Q)`;
* for `p≤Y`, require `v_p(B)=k` (and hence `p^k|a+1`);
* define `s_*` from the two simultaneous congruences, with the displayed lower cutoff. Omit empty classes explicitly if using an enlarged domain instead.

Then the period is indeed `ABp`. The first-term cutoff can be below the actual `v>a` cutoff: this only enlarges a positive upper bound, and `1/v≤2/s` is used on the actual events.

For the long part, retain the saturated B condition instead of replacing it by all of `tau_Q(a+1)`. Write `B=p^k B'`, with `B'|Q/p^k`. Its required sum is bounded by

```
Σ_(B'|Q/p^k) Σ_(a≤H, a≡−1 mod p^k B') 1/a
  ≪ (L/p^k) Σ_(B'|Q/p^k) 1/B'
  ≪ L log Y / p^k.
```

Multiplication by the harmonic long-part factor `L/p` gives exactly `L² log Y/q`, without k. For `p>Y` the original mass argument gives the corresponding estimate with `k=0`. For residual coordinates, explain residues only after dividing the forced `p^k` factor out of the congruence.

This makes a precise corrected FT imply Theorem 3.4; the current literal FT is not a well-defined hypothesis on its entire displayed domain. These defects do not infect Theorem 2.1.

### 3. MAJOR — Minimal free-coordinate modulus is not the energy/BRW modulus

**Locations:** lines 564–569 and 580–585; compare H4_NOT_POLYLOG (7), (10), and Lemma 5.

The dependency graph can group all remaining digits at a prime into one coordinate. But `m_c=p^(k+1)` is only the **first free threshold**. A function of that coordinate can depend on digits through `p^e`, with `e≫k+1`. It need not be a congruence function modulo `m_c`.

Example: with `Y=10`, the live event `(a,v)=(31,64)` requires the 2-adic residue `n=33 mod64`. Its coordinate threshold is `m_2=16`. Residues 33 and 49 have the same residue modulo 16 but differ on this local event. Thus truncating a lumped-coordinate Efron–Stein expansion using the threshold modulus would not justify the low-modulus cell budget. “The energy lemma … needs absolute moduli m_c” at line 583 is not an adequate interface check.

**Repair:** Use the lumped-by-prime coordinates only for the LLL and the real-character twist. For the energy and BRW constructions, return to the actual independent digits, with H4_NOT_POLYLOG's weight

```
m_U = product_p p^(1+max digit index used at p).
```

Original events remain prime-power prefix cylinders of modulus `av≤H²`; after conditioning on Q or another cylinder, the remaining absolute digit indices are exactly the ones allowed by that imported lemma. Nothing requires Q to have been chosen adaptively. Apply Lemma 5 on this digit space, without substituting first-free thresholds for full cell moduli.

Also replace the introductory “coordinate loads ≤1/64” at line 568 by the stronger needed **event-support sum** condition (7). Line 581 does aim at that correct condition. One cannot “shrink the constant in FT/Lemma 3.3”: instead choose the cutoff exponent/prefactor with sufficient slack, under FT at that cutoff, so the resulting bounds are `o(log m_c/L)` and the support sum is at most 1/64.

After these repairs, Lemma 6 works: a real primitive conductor outside Q has an odd prime outside Q, and its entire free-prime coordinate is among the LLL coordinates. Removing that prime from an event leaves a cylinder with no larger neighborhood. Lemmas 7/7b allow overlapping Q/cell moduli. The auxiliary prime gives `p>H²`, hence distinct primes as H grows. The budgets are `log Q≪L³ polylog`, `S≪L² polylog`, and `log D+log(2+K)≪L³ polylog`, so the claimed strict ranges `κ<1/3` and `κ<1/6` survive.

### 4. MAJOR — Unsupported unconditional refinement imported from a different model

**Location:** lines 514–515.

I3 §8.3 proves `exp(−C L⁶/log L)` for its integer-Haar interior-word model, whose conditional event probabilities are `D/M` and whose envelope sums to `O(L⁴)`. Here the prime-unit probabilities are totient ratios; H4_NOT_POLYLOG's supplied envelope is `S_sharp≪L⁴ log L`.

Even copying I3's improved charging `h(m)≪L/log L` into that supplied prime-Haar envelope gives a cost `O(L⁶)`, not the asserted `O(L⁶/log L)`. The extra log L cannot simply disappear by citing I3. This is an unsupported implication, not a counterexample to the possibility of proving the stronger bound separately.

**Repair:** Retain the stated established `exp(−C L⁶ log L)` status quo, or supply and audit an improved prime-Haar envelope and its transfer. Do not advertise the I3 refinement as already proved for δ(H).

### 5. MINOR — Make the beta cutoff and finite-H applicability explicit

**Locations:** lines 474–481 and 506–507.

The asymptotic implication needs `C>C_0+1` (with harmless additional slack), not an arbitrary C in `Y=L²(log L)^C`. Then the load bound is `o(1/log L)`, below eta, and the mass exponent is absorbed into the final bound. State this choice as explicitly as in Theorem 3.4.

At the reported finite `H=10^5`, beta is about 1.409 and eta about 0.2573. This is outside the literal `beta≤exp(1/3)`, `eta≤1/4` range of the cited OMEGA13 lemma. The finite certificate nevertheless has a direct repair: the measured maximal weighted load is 0.2194, so every `x_E≤0.2194<1/4`, and that is the bound actually needed for `−log(1−x_E)≤(4/3)x_E`. The rest of the beta proof goes through since loads are also below eta. Record that direct check rather than invoking the lemma outside its stated parameter range.

### 6. MINOR — A few §2 inequalities need harmless constant/power slack

**Locations:** lines 142, 177–178, 195, 199.

* The correct uniform square-removal comparison is `sqrt(X)/q ≥ H^(1/40−1/400)/4 → infinity`; merely comparing the printed lower bound on `X/q` to an unrestricted `sqrt(X)` is not the stated reasoning.
* Line 178 drops a polylog factor while retaining the identical H exponent. Write `H^(−1/16+3/400+o(1))`; it is still much smaller than the lemma's `H^(−1/30)` error.
* Apply the rough totient estimate also to `lcm(R,R')≤H⁴`, not just the `R≤H²` version of F1. The identical proof gives `phi(lcm)≥lcm/2` for large H.
* The intermediate chain `2v'+2H^(1/8)≤4V'` at line 199 does not follow from `v'≤2V'`. Instead use `|u+v−u'−v'|≤max(u+v,u'+v')≤H^(1/8)+2V'≤3V'` for large H. Thus the needed `D≤4V'` is valid.

None changes the pair-sum exponent or introduces a first-term problem.

### 7. MINOR — Finish the small-block bookkeeping in Lemma 3.3

**Locations:** lines 404–413.

The Shiu application itself is valid; I did not find the feared large-modulus obstruction. For clarity, select fixed Shiu parameters such as alpha=beta=1/4. With `X'>2q`, the interval length is comparable to `qX'`, is larger than `q²`, and satisfies both printed range conditions. The progression is reduced, `q/phi(q)≤2` since q is a prime power, and the family `tau_Q≤tau` has uniform growth constants. Dropping the omitted Euler factors only weakens the upper bound. The logarithmic Euler-product bound uses `log min(Y,x)≤log Y` if the block endpoint is below Y.

For the short blocks the missing explicit combination is

```
T(q) ≪ L log Y + O_epsilon(q^(3 epsilon)).
```

Choose, for example, epsilon=1/48. If `q≤L³`, the second term is swallowed by `L log Y`. If `q>L³`, after multiplying by `L(log L)²/q` it is `O(q^(−1/2))`. This also covers `q>sqrt(H)`, where all blocks are short. Thus the stated lemma is salvageable as written without any new first-term hypothesis. Add these details so “Combine” does not conceal the absorption.

### 8. MINOR — Distinguish an available budget from a proved transfer ceiling

**Locations:** lines 17, 591–594.

Lemma 5 supplies an **upper bound** `log D≪mathcal L(S+mathcal L)`, not a matching lower bound or a lower bound on every possible minorant's degree. Writing `log D≈mathcal L S` and “cannot reach 1/2” overstates what has been shown, even under an Assessment heading.

**Repair:** Say the currently quantified generic budget only delivers `κ<1/3` from these estimates, and that reaching 1/2 would require a stronger bound or additional structure. No impossibility theorem for this class of methods has been proved.

### 9. MINOR — Numerical interpretation and two assessment overstatements

**Locations:** lines 314–316, 512–515, 536–546.

* A crude upper estimate for the unsolved A_min hub does not establish the lower bound `Delta≫S_0 L²/Y` printed at line 316. Say that the crude upper bound is too large, or supply an actual lower-bound construction.
* The load programs verify actual loads and sufficient finite LLL conditions, not the separately defined `FT(q)` sum. Do not say every hypothesis has been numerically checked. FT includes enlarged first terms that these programs do not enumerate.
* The simulation supports a ratio to the Poisson benchmark. It does not identify the causal contribution of small-prime positive dependence (conflicting events also occur), or establish a law for “typical survivors.” In particular “typical survivors do not condition at all” is not a demonstrated statement about their small-coordinate distribution.

The empirical numbers themselves match the archived output. Fixed-H density transfer is legitimate and correctly separated from growing-H prime statistics. The final tail row has only 200 survivors, so the ratio 0.640 should not be read as a precision asymptotic constant.

## Detailed checks that did not break

### Theorem 2.1

* **Colour:** reciprocity gives exactly the displayed sign table. Repeated prime factors in odd endpoints do not invalidate Jacobi reciprocity. On the relevant congruence the symbol is nonzero. The 2-adic coordinate disappears for this odd family.
* **Conditioning:** conditioning all small coordinates is harmless; equivalently condition only the finitely many digits used by this finite family. Small/rough supports are disjoint, the residual rough parts are squarefree, and the target residues at rough primes are units by endpoint coprimality. Thus the conditional events are genuinely atomic with probability `1/phi(r_1 r_2)`. Formula (2.1) is correct. A uniform bound on every fibre may be averaged or bounded by its supremum; no exceptional class-of-one issue occurs.
* **Mass:** the sieve has progression length `X/q≥H^(1/20−1/400)/4`, while its level is `exp(O((log L)²))`. Progression remainders are therefore negligible uniformly in the reduced residue and smooth q. The squarefree and fixed-rough-m coprimality removals are uniformly negligible. Cross-coprimality between any small part and any rough part is automatic. The r_2 sieve explicitly excludes primes dividing r_1. Restricting to squarefree `s_1 s_2≤S_0` is a legitimate subfamily; the Rankin tail is exponentially small in `L/log L`, and the Euler product restores both roughness losses.
* **Loads:** the small-p and large-p split controls precisely the first terms created by writing `r_i=px`. Summing small parts uses harmonic weight on the other side and only `S_0` unweighted possibilities on the dangerous side. The exponent margin to `−1/30` is ample.
* **Pair sum:** all four shared factors are pairwise coprime. The residual factors have exactly the coprimality needed for the lcm identity. With smooth multipliers retained, compatibility yields the stated congruences for c and d. Coefficients can be inverted because g,h,j,k are pairwise coprime and rough, while all s's are smooth. In particular `gcd(hj,s_2')=gcd(gk,s_1')=1`. The CRT periods really are the products asserted. The equal-sum case gives `h|u−u'` and `gjk≤uu'`; separated endpoints control D. The products of harmonic-sum bounds, the `4^omega(D)` assignment count, and both final summations check out. Large progression moduli do not escape the explicitly retained first terms.
* **Repeated conditional events:** the original pairs may become repeated atoms on a fibre. The cited Janson proof works for indexed families: a duplicate contributes its full probability to Delta, and the same pair decomposition includes it. No illicit deduplication is used.

### Theorem 2.6

The colour lemma is correct for every odd divisor d. The progression `A=−1 mod4d` gives the required reduced class and colour, even when d is not rough. The sieve and squarefree removal are uniform because `d≤H^(1/10)` and `A≥H^(1/2)`. For `d=d'`, orienting `v<v'` forces `v'≥d`, and switching the summation order leaves g in one reduced class modulo d; the resulting `L³/N_0=O(L)` hub bound is valid. For unequal d's, `g≤|d−d'|≤H^(1/10)` makes both endpoint progressions long, and orienting `d'>d` controls the d' first term. The resulting `L⁴/Y` is negligible. The mass dominates both errors.

### Lower-side probabilities, mass, and LLL constants

The exact totient-ratio formula remains correct with partial powers in Q, including the residual digits at 2 and 3. The mass proof groups by the actual B before enlarging to divisors, so no equality of exact and arbitrary B is needed there. Its first member satisfies `AB≤2v_*`, which genuinely eliminates that first-term problem. The dependency graph by free primes is valid for arbitrary prefix cylinders, not only atomic events. After deleting the two certain events, the support is nonempty, `sum log m_c≤log(av)≤2L`, and Theorem 3.4's constants give neighborhood x-mass at most 1/4 and avoidance at least `exp(−3S)`. The conditioning cost is `phi(24)/phi(Q)=8/phi(Q)`, and `log Q=(1+o(1))Y` follows from the prime-power Chebyshev sum. Nothing about these checks proves FT or FT_beta.

## Independent computations

All executed verification programs used `ulimit -v 8000000` and an explicit timeout. Scripts/binaries were placed in `/tmp`; no Cartesian-product arrays were built. Existing checks were inspected first: the old decomposition test does not check the smooth-multiplier CRT periods, and its exact probability test restricts the rough part to squarefree factors, motivating the distinct checks below.

1. `/tmp/z49-hostile-review-checks.py`, `timeout 60 uv run python ...`:
   * Exact conditional CRT enumeration on **1,229** coprime endpoint pairs with partial-power `Q=2520`: **377 live**, including **32** using residual small-prime digits; zero probability/support failures.
   * Streamed random smooth/rough decompositions: **138 compatible distinct indexed pairs**, including **6 equal-sum pairs**; all four smooth-multiplier compatibility congruences and the lcm identity passed.
   * Verified the two concrete FT-domain counterexamples and the high-digit/block-modulus example in issues 2–3.
2. Recompiled the existing load checker into `/tmp/z49-review-lllcheck` and ran each case with `timeout 60`:
   * `H=100000,Y=1500`: `log Q=1509.3`, `S=19.586`, maximum event-support `2w` sum **0.2390**; reproduces the archived ordinary-LLL calculation.
   * `H=100000,Y=600`: `S_beta=40.467`, maximum weighted coordinate load **0.2194**, `eta=0.2573`; reproduces the archived numbers and supports the direct finite-H repair in issue 5.
3. Rendered and read the local primary Shiu scan, printed pp. 162–163. Its actual requirements are `0<alpha,beta<1/2`, `q<y^(1−alpha)`, and `x^beta<y≤x`. These allow the long blocks used here.

These are finite algebra/implementation checks, not evidence that the asymptotic FT hypotheses hold. No claim about ES existence follows.
