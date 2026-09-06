# Hostile review: the three-quarter note

**Verdict: SOUND-AFTER-REPAIRS.** No load-bearing gap in the claimed exceptional-set implication was found. Two repairs are applied: an omitted weight comparison in the claim about discarded *main-term* mass, and an explicitly heuristic formulation of the methodological ceiling. Neither changes the exponent, parameters, analytic inputs, or CLAIMED/PROVISIONAL status.

This is an internal mathematical audit, not external human refereeing or a priority certification. It is not a blind review: the mandate identifies the vulnerable steps, and repository searches exposed earlier review summaries. The calculations below, rather than those verdicts, are the basis for this decision.

## Scope and explicit checkpoint decisions

I read `paper/es-threequarter-note.tex` in full (1199 lines at starting commit `4ecb5cb`), the complete substantive text of `paper/vaughan-loglog-note.tex`, and `notes.md` §§16, 34, 39. I inspected Shiu's original scanned pp. 161–163 in `sources/shiu-1980.pdf`, including (1.1), the two growth hypotheses, and Theorem 1. The re-derivation scratch file is `/tmp/es-threequarter-referee-scratch.md`; its essential arguments are recorded here. Standard Brun–Titchmarsh and Bombieri–Vinogradov are accepted in their stated classical forms, not re-proved.

1. **(i) Residue-resolved upper bounds: PROVED.** Uniformity holds in every multiplier, divisor, and unit residue; nonunit residues have zero atom mass. In particular the unpruned conditional bound `mu_c <= C t^3` holds for **every** multiplier fibre, including nonreduced fibres. No repair of this estimate is needed.
2. **(ii) Pruned cubic supply and `J_c`: PROVED-AFTER-REPAIR.** The incidence bound, Shiu applications, BV multiplicity, and arbitrary-subfamily inheritance are proved as written. The added comparison justifies the further statement that pruning removes `o(1)` of the totient-weighted prime main term, not merely harmonic mass. **The lower supply and exceptional-set theorem already require only the latter**, so this was not a missing load-bearing step in the implication.
3. **(iii) Factorial moments and Bonferroni transfer: PROVED.** Both the independent-coordinate proof and the ordered prime-power calculation close, uniformly in moment order. There is no hidden `L_K` expansion, no duplicate-atom multiplicity, and no finite-interval independence assumption.

**Unresolved load-bearing steps: none found.** This conclusion concerns the displayed proof, not an assertion of publication novelty or of a universal sieve-optimality theorem.

## Numbered defect list and applied fixes

Line numbers in this list refer to the **original** `.tex` at `4ecb5cb`; subsequent sections use the repaired file's lines.

1. **Medium — ancillary inference, not a gap in the lower supply; lines 515–516.** Exact quote: `We have pruned \emph{weighted harmonic/main-term mass}, not asserted that the discarded actual prime count is small.` The displayed second moment and `eq:prunedmass` control the discarded sum of `1/(uv)`. They do not immediately control the discarded sum of `1/phi(4uv)`: their ratio is not bounded by an absolute constant. The existing lower-bound proof is nevertheless valid because retained harmonic mass is a lower bound for the needed main term. **Applied fix, now lines 515–524:** use the elementary Mertens consequence `n/phi(n) << log log(3n)`; for `4uv <= 4X^(1/3)`, the extra weight is `O(log t)`. The discarded totient mass is therefore an `O(log t/t)=o(1)` fraction of the original main-term mass, uniformly even for `h(J)=1`. A short proof of the Mertens consequence is included. The caveat about *actual prime counts* is retained explicitly.
2. **Low — methodological overstatement; line 1056 and lines 1115–1120.** Exact quote: `No improvement in a fixed level of distribution changes $3/4$ for a sieve whose saving comes only from this summed identity-class mass and whose product or polynomial truncation has the stated $t\mu$ budget.` The original restriction to a mass-driven method is important and was already present. Nevertheless the categorical opening and heading can be read as an optimality assertion; the displayed sufficient truncation estimates do not establish necessity for every implementation. **Applied fix, now Section 9 and lines 1123–1135:** label the ceiling explicitly *heuristic*, state that the calculation predicts the exponent under the same budget, and explicitly disclaim a necessity/optimality theorem. All existing exclusions and provisional caveats remain.

No other mathematical defect is asserted. In particular, the following tempting objections fail on inspection.

## (i) Re-derivation of local profiles and all-fibre upper mass

### Exact residue count, not an average over classes

Fix `k`, `g|k`, and a unit `a mod g`. Put `q0=lcm(g,rad k)`, so `q0|k`. Unit reduction from `q0` to `g` is onto with equal fibres. Hence the number of ordered unit-class pairs satisfying `-u/v=a mod g` is exactly

    phi(q0)^2 / phi(g).

This retains **all** exclusions from primes dividing `k`, not just those dividing `g`. A nonunit `a` permits no atom, because `u` and `v` are units modulo `k`.

For `F(n)=n/phi(n)`, Shiu on one full relative-length box gives

    sum_{u in box, u=r (q0)} F(u)
        <= C U/phi(q0) * A(k),
    A(k) = exp(-sum_{p|k} 1/(p-1)) ~ phi(k)/k.

Every prime dividing `k` is below the endpoint. The comparison is uniform: the logarithm of the ratio of the last two quantities is a sum of `O(p^-2)`, not `O(1/p)`. Multiplying the two one-variable bounds, summing over the exact number of allowed class pairs, and dividing by `UV` gives

    sum_box 1/(phi(u)phi(v))
        <= C/phi(g) * (phi(k)/k)^2.

There are `O((log z)^2)` box pairs. The modulus-one case is separately covered by the elementary nonnegative divisor expansion in the note. A short last box is **enlarged**, not fed into Shiu at an illegal short length.

For each original coprime pair, Brun–Titchmarsh gives reciprocal prime weight

    sum_{x<ell<=2x, ell=-k^-1 (4uv)} 1/ell
        <= C/[phi(4uv) log x]
        <= C/[phi(u)phi(v) log x].

Here `q=4uv<=4x^(1/3)`; `k` changes the reduced residue, not the prime-counting modulus. Drop pair coprimality only after applying the valid totient comparison on the original pairs. Summing blocks and dividing by `k` proves precisely

    W_{k,a}(g) <= C t^2 phi(k)^2/[k^3 phi(g)].

There is no suppressed divisor factor, `k^epsilon`, or `log log k` loss. See repaired lines 605–657.

### Nonreduced fibres do not cause an upper-bound failure

An active atom satisfies `c=-u/v mod k`, a unit class. Thus the eligible multipliers are exactly `J_c={k:(k,c)=1}`, with `1 in J_c`. On this subfamily `c` is reduced modulo its lcm, however nonreduced it is modulo the full `L_K`.

Either apply the elementary lattice upper bound and BT directly, or put `g=k`, `a=c mod k` in the profile just proved. The contribution to the conditional mass from multiplier `k` is `k W_{k,c}(k)`, and therefore

    mu_c <= C t^2 sum_{k in J_c} phi(k)/k^2
         = C t^2 h(J_c) <= C t^3.

The direct BT/lattice route, used in Corollary 4.3 (lines 564–587), does not even depend on the stronger profile lemma. Neither route averages over `c` or applies BV to an individually tiny main term.

For the separate fixed-`k` lower bound on `W_k`, summing the low-omega lattice lower bound over all `phi(k)` ratio classes gives harmonic pair mass `>>t^2(phi(k)/k)^2`. Fixed-`k` BV costs only `t^(D log 2)`, not `K`; its error is `O(x/t^10)`. The main term is at least `c x t/(log K)^2 >>_kappa x/t`, so it dominates uniformly. The Cauchy–Schwarz derivation of the full weighted multiplier sum is also valid.

### Deduplication is global across multipliers

At a fixed `ell`, equal projected residues imply

    ell | uv'-u'v,       |uv'-u'v| < z^2 < ell.

Reduced fractions force the ordered pairs to agree. The divisibility conditions then imply `k=k' mod 4uv`; since `4uv>4H^2>K`, the multipliers agree too. Consequently **two different atoms at the same prime cannot have the same projected residue**, even before fixing `c`. There are at most `z^2<=ell^(1/3)` atoms at that prime. This validates the lower incidence count and later Bernoulli assertion. Duplicate counting would not invalidate an upper bound, but it would invalidate those two steps; the note actually rules it out (lines 170–197).

## (ii) Re-derivation of pruning, Shiu uniformity, and BV

### The feared large lcm cases are impossible

For every ordered pair of multipliers,

    d=lcm(k1,k2) <= k1*k2 <= K^2 < H=K^10 < z.

There are **no pairs with lcm exceeding `K^2`**, nor with lcm exceeding `H` or `z` in this setup. The magnitude of an integer representative of `c` is irrelevant.

Expanding `r_J(u,v;c)^2` requires precisely the one congruence `d|u+cv`. Since `(c,d)=1` and `(u,v)=1`, it implies `(v,d)=1`. Drop pair coprimality but keep this latter condition. Direct harmonic progression summation gives

    sum 1/(uv) <= C phi(d)/d^2 * Lambda^2
                   + C Lambda tau(d)/H.

The estimates include empty progressions. This is not an illicit application of the lattice lemma with the wrong floor `(K^2)^10`. Summing over multiplier pairs,

    sum phi([k1,k2])/[k1,k2]^2
      <= sum gcd(k1,k2)/(k1*k2)
      <= sum_{a<=K} (1/a)(1+log(K/a))^2
      << (1+log K)^3.

Also `tau(d)<=2K`, so all boundary errors together cost at most `O(K^3 (log z)^2/H)`. This proves the second moment uniformly in `c` and every permitted subfamily (lines 420–455).

### Shiu's actual hypotheses hold in every used box

The original paper states, with fixed `0<alpha,beta<1/2`, reduced `0<a<q`, and its fixed growth class,

    q < Y^(1-alpha),     V^beta < Y <= V.

Choose `alpha=beta=1/4`, `V=(1+1/20)U`, `Y=U/20`. At every box endpoint `U>=K^10`,

    q <= K <= U^(1/10) < (U/20)^(3/4),
    ((21/20)U)^(1/4) < U/20

once the fixed lower threshold is sufficiently large. The same holds in the other variable and for the auxiliary `q0<=K`. The last partial box is enlarged for upper estimates. The `q=1` exception to Shiu's `0<a<q` is handled separately, not ignored.

The functions `(3/2)^omega(n)` and `n/phi(n)` satisfy both prime-power growth and every-epsilon subpower growth. No function parameter grows with `X`. For the low-omega estimate, two applications of Shiu give the local coefficient

    [1/phi(k)] exp(-3 sum_{p|k} 1/p).

Its ratio to `phi(k)/k^2` has logarithm

    sum_{p|k} [-2 log(1-1/p) - 3/p],

which is bounded above uniformly; the linear term is negative. Hence the weighted moment is at most `C phi(k)/k^2 Lambda^2 log z`. Choosing fixed `D` with `D log(3/2)>3` makes the discarded omega tail negligible uniformly. The cutoff with `log log z` is stronger than the atom cutoff with `log log X`. See lines 232–262 and 364–408.

### Pruning and the data-dependent family

After low-omega deletion the harmonic triple mass is `>>t^2 h(J)`. With `T=t^4`, the discarded harmonic mass is bounded by

    T^-1 sum r_J^2/(uv) <= C t^2 (1+log K)^3/t^4 = O_kappa(t).

Its relative size is `O(1/(t h(J)))=O(1/t)` because `1 in J`. This is why arbitrarily sparse `J` are allowed. The repair in defect 1 adds the `O(log t)` weight comparison and proves the corresponding `o(1)` assertion for the prime main term. Neither calculation claims that discarded *actual* primes are negligible.

For one `q=4uv`, pair coprimality permits at most `2^omega(q/4)` ordered allocations of whole prime powers. Each allocation has at most `T` surviving incident multipliers. Therefore the **entire** modulus multiplicity, including different inverse residues, satisfies

    W_good(q) <= 2^omega(q/4) T <= t^(4+D log 2).

BV takes the maximum over reduced residue classes at each modulus. It therefore bounds any data-dependent selection of triples, without averaging over `c` or `J`. All these moduli lie below its level, and a fixed `R>4+D log 2+10` makes the error `O(x/t^10)`. Retained harmonic mass supplies the required prime main-term lower bound, and the global dedup argument turns incidences into distinct classes. Dividing by `2x` and summing the full canonical blocks gives `>>t^2 h(J)` reciprocal mass. BT gives the unpruned upper half.

For `J=J_c`, `1 in J_c` and `(c,L_{J_c})=1` hold by definition. Every estimate is simultaneous in this subfamily, and its retained canonical triples lie in the original fixed `A_X`. There is no selection-after-average fallacy. Neither literal `H_kBV` nor the old partition-free hypothesis is used.

## (iii) Re-derivation of moments, void, and integer transfer

### Exact conditional space and both moment proofs

The probability space is explicitly

    Z/MZ,  M=lcm(L_K,P_y) * product_{sqrt X<ell<=X prime} ell.

All atom moduli and selector moduli divide `M`. The multiplier conditions are functions of `n mod L_K`, since each `k|L_K`. The large primes are distinct and coprime to its small part. Given `c mod L_K`, their coordinates are independent and uniform. Conditioning further on `S_y=1` does not affect them when `y<sqrt X`.

By global same-prime deduplication, `H_X` in a fibre is a sum of independent **Bernoulli** variables with means `f_c(ell)/ell`, not a sum of multiply counted atoms at one coordinate. Thus for every integer `j>=1`,

    E[(H_X)_j | c,S_y=1]
      = sum_{ordered distinct ell_1,...,ell_j} product f_c(ell_i)/ell_i
      <= mu_c^j <= (C t^3)^j.

Average over admitted fibres. The constant is independent of `j`, including `j` larger than the number of coordinates. There is no assertion of conditional independence on `[1,N]` (lines 717–742).

Independently, let the previous multiplier lcm have exponent `f` at `p`, and the next multiplier have exponent `e`. Subject to agreement, the local relative probability is `p^(min(e,f)-e)` for `f>0`; for `f=0` it is `1/phi(p^e)` if selected and `p^-e` otherwise. This is exactly `q_y(k)b_y(g)/k`, with `g=(k,R)`, including unequal exponents. The profile bound divides by `phi(g)`, leaving only `product_{p|g,p>y}p/(p-1)`.

The two modifying prime sets are disjoint. Each modification changes the nonconstant local Euler mass from `(p-1)/p^2` to `1/p`; the ratio of full factors is `1+O(p^-2)`. Thus the sum over next multipliers is `O(log K)` uniformly even for enormous `R`. Excluding old large primes only decreases it. This independently establishes the ordered induction with base `C t^3`, not a hidden order-dependent base (lines 700–715 and 744–784).

### Exponentially rare bad multiplier fibres

Only primes actually dividing `L_K` occur in `Z(c)`. Their coordinates for `p>y` remain independent Bernoulli divisibility events with probabilities `1/p` under `S_y=1`. Consequently

    E exp(y Z) <= exp((e-1)y sum_{p>y} p^-2) <= exp(C),
    Pr(Z>eta | S_y=1) <= exp(-eta y+C).

The sum can even be bounded over all integers. The elementary union bound gives

    h(full)-h(J_c)
       <= (1+log K) sum_{supported p>y, p|c}1/p
       <= 2(log K) Z.

Choose fixed small `eta`. On `Z<=eta`, `h(J_c)>=c log K`, and the arbitrary-subfamily lower estimate applies. The exact conditional void is

    product_ell (1-f_c(ell)/ell) <= exp(-mu_c) <= exp(-c t^3).

Here the classes really are distinct, so every factor is a legitimate probability. With `y=B t^3`, fixed sufficiently large `B` makes bad fibres equally rare. This verifies every independence and union-bound step in lines 803–868.

Caution on support: `y<K` alone does not logically imply all selector primes divide `L_K`; `2` never does, and an odd prime congruent to 3 modulo 4 near `K` may not. The proof handles this correctly using `lcm(L_K,P_y)` and restricting `Z` to supported primes. In the final range, actually `3y<K` eventually, so every odd selector prime is supported; the separate factor `2` remains harmless.

### Bonferroni and the complete ledger

For even `r`, the alternating identity is exact: `Q_r(0)=1`, and `Q_r(h)=binom(h-1,r)>=0` for positive integers `h`. For `h>=r+1` this is at most `binom(h,r+1)`; for `1<=h<=r` both vanish. Therefore

    E[Q_r(H_X)|S_y=1]
        <= exp(-c_v t^3) + (C t^3)^(r+1)/(r+1)!.

Choosing `r` as the least even integer at least `D_B t^3`, with fixed sufficiently large `D_B`, makes the second term exponentially small. This is an upper factorial-moment argument, not an unjustified Poisson approximation.

The identity expanding `binom(H_X,j)` has one coefficient per **unordered atom subset**, with no extra factorial. Intersecting such a subset and a selector divisor gives either the empty set or one residue class. Prior to merging equal classes, the absolute coefficient sum is bounded by

    2^pi(y) sum_{j<=r} binom(|A_X|,j),
    |A_X| <= K X^(4/3).

Thus its logarithm is `O(pi(y)+rt)=O(t^4)`, not `O(r)`. Every term modulus is at most `P_y(KX)^r`, whose logarithm is `O(Bt^3)+(1+kappa)rt=O(t^4)`. No term enumerates a multiplier fibre, and the possibly enormous full probability-space modulus never appears in this ledger.

For **every** modulus `q`, the count of one residue class is `N/q+epsilon`, `|epsilon|<=1`. When `q>N`, the count is zero or one and the same estimate remains valid. Signed coefficients therefore introduce at most the absolute coefficient sum as rounding error. This justifies the exact transfer, rather than a heuristic equidistribution approximation.

Choose fixed `C0` larger than twice both ledger constants, and then `t=alpha(log N)^(1/4)` with `alpha<=C0^(-1/4)`. Both the absolute coefficient sum and `P_y(KX)^r` are at most `N^(1/2)` for large `N`, while `N^(1/2)=o(N exp(-c t^3))`. All constants are fixed before the limit. Although onset thresholds can be enormous, `y=B t^3<K= floor(exp(kappa t))<sqrt X` and `3y<K` eventually hold. The small exceptional-prime range `<=max(K,y)` is negligible. This checks lines 878–1025 without any prime-progression estimate at scale `N`.

## Remaining argument and ceiling

The multiplier identity is exact, positive, and valid for all positive integers in an atom, not only primes. If one prime divisor of an integer is representable, scaling its three denominators represents that integer. Exceptional integers consequently lie in the semigroup generated by exceptional primes; the converse is not asserted.

With `delta=eta(log x)^(-1/4)` and the prime bound, partial summation bounds the first-prime contribution to the Rankin Euler product by

    O(1) + integral_{log x0}^{log x} exp(delta u-c0 u^(3/4)) du.

For `u<=log x`, `delta u<=eta u^(3/4)`, so the integral is uniformly finite when `eta<c0`. Higher prime powers cost `O(sum_p p^-3/2)` for `delta<1/4`. This proves the semigroup transfer with the same logarithmic exponent, including the empty product `1` (lines 1027–1061).

The Section 9 identity-class supply calculation is also consistent: the classes are `-4D mod M`, `D|((M+1)/4)^2`; divisors below the square root give distinct residues. The divisor-series identity gives cubic total harmonic supply. That supply estimate and the sufficient truncation budget explain the **heuristic** three-quarter balance; they do not prove universal optimality. Nothing from this remark enters the main implication.

## Validation and artifacts

- `uv run python reviews/es-threequarter-note-check.py`: **PASS**. The companion imposes a 512 MiB address-space limit and a 60-second CPU limit, uses streaming enumeration, and checks 3,014 unit/nonunit residue-profile counts, 120 unequal-prime-power relative probabilities, all 404,550 residues of a small CRT model (150 admitted multiplier fibres; factorial moments through order 7), 4,221 even-Bonferroni inequalities, and 5,620 exact integer-class rounding cases including `q>N`.
- The finite model checks algebra and conditional probability only. It is **not** an asymptotic verification of Shiu, BV, or the infeasibly large literal range `H=K^10`, `z>=H^2`.
- Two requested `pdflatex -interaction=nonstopmode` passes: **PASS**, output remains **18 pages**. The final log has no warnings, undefined references, or overfull/underfull boxes.
- `git diff --check`: **PASS**.
- Changed deliverables: `paper/es-threequarter-note.tex`, rebuilt `paper/es-threequarter-note.pdf`, this review, and the bounded finite-check companion. No notebook or LL result is changed; no provisional caveat is weakened.
