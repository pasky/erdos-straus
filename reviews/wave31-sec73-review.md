# Hostile referee report: §73 and (bt)

**Verdict: SOUND-AFTER-REPAIRS.** Reviewed against parent `4f061a7` on
`wave31-unitA`, solely in `/tmp/es-w31A`. Line references in the defect list
refer to that parent, so they remain reproducible after the repairs.

The confinement sieve survives maximum-severity scrutiny. Its dimension
uniformity is proved, not imported from a fixed-dimensional theorem. The
exceptional-zero sign is correct and favorable. There is **no unconditional
Erdős–Straus exceptional-set improvement**, and no crossing of the §14.4–14.6
witness-entropy wall. The original section already acknowledged blocks and
conditionality; several standalone statements nevertheless needed tightening.
All repairs are confined to §73; `verify.py` is unchanged.

## Defects and exact repairs

1. **HIGH — potential scope overclaim, status and Theorem 73.B,
   lines 28525–28526, 28917–28927; missing explicit entropy-wall comparison.**
   Quote: “The resulting stack is unconditional for every fixed
   \(0<\theta<1\)”. The actual assertion concerns confinement intersections,
   not the full failure intersection. F1 implies failure, not conversely;
   CF3 majorants still omit full-generation BLK. Extracting this statement
   without the later walls can falsely suggest an unconditional record.
   **Fix applied:** qualify the status as “confinement-only”; insert a
   scope paragraph directly in Theorem 73.B, give its F1-only exponent, and
   explicitly deny a first-witness/exceptional-set consequence. Add honest
   wall 7 distinguishing the old signed-product `3^K` entropy from the
   mechanism/subgroup-cover entropy here, and explicitly disclaim
   unconditional improvements on Vaughan's 2/3 and the provisional 3/4.
   The valid CF3 confinement majorants are retained, not mislabeled as F1.

2. **MEDIUM — event domain omitted on the integer frame,
   lines 28546–28552 and 29028–29030.**
   Quotes: “For \((h,a)=1\), let” and
   “\({\rm BLK}_b(h_b(n))\ (b\in\mathcal B)\)”. BLK uses a subgroup and
   spectrum defined only for units, but the later count ranges over all
   integers in the hard progression, including multiples of a selected
   modulus. **Fix applied:** after (73.2), explicitly extend all event
   indicators by zero on nonunits, and specify positive integer counts.
   This loses no application prime above the existing small-prime cutoff.

3. **MEDIUM — incomplete quantifiers in the explicit sieve lemma,
   lines 28632–28642; LOW — limit wording, line 28666.**
   Quotes: “Then the sifted set … satisfies” (73.8), followed only afterward
   by “where, whenever \(m\geq2G\)”; and “the relative error tends to zero
   uniformly with \(G\)”. Outside that condition the displayed E1 had not
   been defined, so (73.8) was not a standalone all-k theorem. Uniform
   convergence also needs its limiting parameter specified.
   **Fix applied:** put “provided \(m\geq2G\)” directly before (73.8),
   explicitly require positive integral M and `1 <= t <= N`, and state
   convergence as G tends to infinity subject to the displayed constraints.
   No numerical constant or valid bound changes.

4. **MEDIUM — missing character hypotheses, lines 28758–28767.**
   Quote: “an effective absolute \(C_\chi\) such that, whenever
   \(v\geq u\geq k\geq3\)”. Lemma 73.3 did not explicitly require the
   primitive nonprincipal character to which Standard Fact 73.1 applies.
   Read as a standalone statement for real characters it includes the
   principal character and is false: its reciprocal-prime sum diverges.
   **Fix applied:** quantify explicitly over primitive nonprincipal
   characters modulo k and say the absolute constant is independent of chi.
   All actual uses have prime modulus and satisfy this restriction.

5. **LOW — exceptional-zero terminology insufficiently specified,
   lines 28736–28738; analytic-input inventory, lines 28522–28524.**
   Quotes: “the possible exceptional real zero”; “The only non-elementary
   analytic input is the effective prime number theorem for characters”.
   A precise uniform PNT statement needs a fixed effective zero-free-region
   cutoff for what is removed. The inventory also omits the ordinary
   Mertens and fixed-progression PNT used explicitly later.
   **Fix applied:** define exceptional by the interval
   `(1-c0/log(3k),1)` for a sufficiently small effective absolute c0;
   state simplicity, reality, and that no effective lower bound for
   `1-beta` is used. List all three classical analytic inputs in the status.
   The exceptional term and its sign are unchanged and correct.

6. **LOW — unverified branch of the CRT-error estimate,
   lines 28882–28883.**
   Quote: “\(A\leq z\), and (73.11) is \(x^{1/16+o(1)}\)”. Formula
   (73.11) requires A >= k, which this proof did not establish.
   **Fix applied:** explicitly split A >= k, using (73.11), and A < k,
   using `E2 <= exp(A) <= exp(k) = x^{o(1)}`. Both are negligible.
   No theorem is weakened.

7. **MEDIUM — misleading identification with the old full-range
   hypothesis, lines 29054–29058.**
   Quote: “At the exponent \((\log x)^{-1/2+o(1)}\), … the all-non-block
   portion of \(H_{\rm STACK}\) [is] unconditional.” This conflates the
   one-coordinate exponent with the moving-dimensional saving, where the
   fixed factor `1-theta` cannot be absorbed into o(1). The next sentences
   acknowledge the distinction, but do not make the quoted sentence true
   as a literal identification with (71.38).
   **Fix applied:** separate the one-coordinate bound from the stack at
   `Delta_N ~ (1-theta) log L`; explicitly say that H_STACK's full-range
   saving is not proved. H_BLK names only the missing joint cases at the
   reduced range.

8. **LOW — uniform thresholds and the empty-block specialization need
   explicit quantification/justification, lines 28925–28927,
   29023–29026, 29036–29038.**
   Quotes: “every sufficiently large \(N\)” and “For
   \(\mathcal B=\varnothing\), (73.43) … is Theorem 73.B”. The selections
   themselves grow with N; the large-N threshold must not depend on them.
   Also the displayed o(1) in (73.35), alone, does not imply the more
   quantitative `C J log log L` error in (73.43).
   **Fix applied:** specify C(theta), a common N0(theta), and uniformity
   across all partitions/selections; clarify the analogous effective
   thresholds in Theorem 73.B and `0 < rho <= 1` for subfamilies. Explain
   that the empty-block case follows from the *proof*, specifically the
   O(J log log L) error in (73.40) and bounded multiplicative sieve errors.
   No effectivity of the open hypothesis's N0 is newly imposed.

## Independent mathematical audit

- **Trichotomy and cover:** a cyclic group of order 2n, n odd, has an
  odd-order subgroup exactly when that subgroup lies in the squares.
  Every proper even subgroup has index an odd integer at least 3 and
  lies in an index-ell subgroup for some prime ell dividing n. The
  nonnested subgroup union is necessary and correctly retained.
- **Explicit lemma:** CRT supplies remainder at most rho(d), independently
  of M, dimension, or d. Even Bonferroni gives the asserted upper bound.
  The omitted absolute tail is at most `2(eG/m)^m` for m >= 2G. The lower
  product bound is `V >= exp(-G-B/(2(1-eta)))`. For eta <= 1/3,
  `B <= G/3`, so the exponent is at most 5G/4. With m >= 8G the decay
  constant is exactly `8 log 8 - 37/4 = 7.3855323334... > 0`.
  The zero-mass/empty-prime-set case is harmless. These constants have no
  concealed dependence on kappa or the number of forms.
- **Actual level, not merely a support slogan:** when A >= k,
  `E2 <= (k+1)(eA/k)^k`; condition (73.12) is sufficient in precisely
  that branch. In 73.B, `A <= Jz`, eventually `k >= eJ`, and (73.40)
  plus `A >= ZG` supplies A >= k (also for a fixed positive fraction of
  coordinates). Thus `E2 <= (k+1) z^k`, with
  `z^k = N^{1/16}` exactly. In particular `z^{2r} <= N^{1/2}` and the
  *weighted* remainder condition both hold. The support condition alone
  would not have sufficed, but the weighted condition is actually proved.
- **Growing dimension:** `J ~ L^theta/(2 theta log L)`,
  `k ~ (4/theta)L^theta`, and `log z ~ (theta/64)L^{1-theta}`.
  Here `kappa` is between J/2 and J (thus of order L^theta/log L,
  not literally L^theta); total mass G has order L^theta for fixed theta.
  `eta <= J/Z = O_theta(1/log L)`, and (73.17) gives
  `NV >= N exp(-O_theta(L^theta))`, dwarfing the remainder. The character
  threshold holds since `L^{1-theta}/(log L)^2` tends to infinity.
  The mass is at least `kappa Delta_N - O(J log log L)`, with
  `Delta_N = (1-theta) log L + O(log log L)`. This proves the stated
  uniformity; it is not assumed. Thresholds depend on fixed theta (and
  fixed rho), not uniformly on theta approaching 1.
- **Siegel sign and effectiveness:** partial summation of
  `-t^beta/beta` contributes exactly
  `-integral_s^v t^{beta-2}/log(t) dt <= 0`. An *upper* character-sum
  bound is needed to obtain a *lower* nonresidue mass, so discarding this
  term is legitimate and favorable. The PNT error integrates absolutely,
  effectively and uniformly; the initial segment to
  `exp(C log^2(3k))` costs O(log log(3k)). The quotient by a proper even
  subgroup has odd order, hence no real nonprincipal characters; averaging
  its m-1 character errors by 1/m keeps the constant uniform in m.
  There is no concealed effective Siegel lower bound. Only the elementary
  lemma has fully numerical constants; the classical inputs provide
  effective absolute constants, not numerical values tabulated here.
- **Entropy and H_BLK:** F1/CF3/BLK labels alone give 3^J possibilities,
  but CF3 must be expanded. The actual full count is at most
  `product_a(2+omega(n_a)) <= 2^J product_a(1+omega(n_a))`, with logarithm
  O(J log log(3Z)), lower order than J log L. Every term of (73.43) has
  `kappa + |B|/2 >= J/2`, yielding exactly
  `(1-theta)L^theta/(4 theta)` in the conditional full tail; (73.41)
  adds the fraction rho. H_BLK is a genuinely joint assertion, including
  sparse block partitions and the all-block partition, not a consequence
  of marginal estimates. There is no density-among-deep-primes conclusion.

## Computational replay

Ran the requested command in the foreground under its 900-second timeout:

```sh
cd /tmp/es-w31A
timeout 900 uv run --with sympy,numpy,scipy python verify.py
```

Exit status **0**, ending `all checks passed`. All six structural rows,
the toy `(12676, 20281, 28075)`, all four Mertens rows, and the path totals
`(F1, CF3, BLK) = (6054, 12, 136)` and deep totals `(64, 4, 10)` reproduce.
The default (bt) block took approximately 5.18 seconds; no full-scan claim
is inferred from the default run. No change to verify.py requires a rerun.

Also wrote and ran a separate standard-library script under a **256 MiB
address-space limit** and a 90-second timeout. It does not import verify.py,
SymPy, or its helper functions. It reconstructs the a=43 structural row via
*divisor residue pairs* and the lcm of individual multiplicative orders,
not bounded-exponent convolution or generated-subgroup set multiplication.
It independently computes the toy using square-residue sets and direct
pair sums for the elementary polynomials. Output:

```text
Independent divisor/order row: {'units': 19535, 'fail': 14120, 'F1': 1935, 'CF3': 1146, 'BLK': 11039} {3: 1007, 7: 139}
Independent toy: 12676 20281 28075 2.2147386546282295
Independent checks passed (256 MiB address-space cap).
```

The independent script is preserved verbatim below, rather than leaving
an untracked audit artifact. Save the code block to a file and run with
`timeout 90 uv run python <file>` to reproduce it.

```python
"""Independent §73 audit; standard library only; streamed, 256 MiB ceiling."""
import resource
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import ceil, gcd, isqrt, lcm


def primes_to(n):
    return [v for v in range(2, n + 1)
            if all(v % d for d in range(2, isqrt(v) + 1))]


# Independent of (bt)'s exponent-box convolution and generated-subgroup sets:
# Rat(h) = {d/e : d,e divide h}; generated group order is lcm of orders.
a = 43
counts = Counter()
indices = Counter()
for h in range(1, 20_001):
    if h % a == 0:
        continue
    counts['units'] += 1
    divisors = set()
    for d in range(1, isqrt(h) + 1):
        if h % d == 0:
            divisors.update((d, h // d))
    residues = {d % a for d in divisors}
    # d/e == -1 iff d == -e: no inversion or signed-product routine.
    if any((-r) % a in residues for r in residues):
        continue
    counts['fail'] += 1
    prime_factors = [q for q in divisors if q > 1 and
                     all(q % d for d in range(2, isqrt(q) + 1))]
    order = 1
    for q in prime_factors:
        oq = next(j for j in range(1, a) if pow(q, j, a) == 1)
        order = lcm(order, oq)
    if order % 2:
        counts['F1'] += 1
    elif order < a - 1:
        counts['CF3'] += 1
        indices[(a - 1) // order] += 1
    else:
        counts['BLK'] += 1
assert counts == Counter(units=19535, fail=14120, F1=1935, CF3=1146, BLK=11039)
assert indices == Counter({3: 1007, 7: 139})
print('Independent divisor/order row:', dict(counts), dict(indices))

# Construct the toy bad classes using quadratic-residue sets, not Euler tests.
moduli = (3, 7, 11, 19, 23, 31, 43, 47)
primes = [q for q in primes_to(200) if q > 47]
squares = {a: {r*r % a for r in range(1, a)} for a in moduli}
badclasses = {q: {(-a) % q for a in moduli if q % a not in squares[a]}
              for q in primes}
survivors = bonf = 0
for n in range(1, 1_000_001, 24):
    b = sum(n % q in badclasses[q] for q in primes)
    survivors += b == 0
    bonf += 1 - b + b * (b - 1) // 2
# Compute elementary polynomials by direct pair enumeration, not recurrence.
w = [len(badclasses[q]) for q in primes]
x = [Fraction(len(badclasses[q]), q) for q in primes]
density = 1 - sum(x) + sum(s*t for s, t in combinations(x, 2))
error = 1 + sum(w) + sum(s*t for s, t in combinations(w, 2))
upper = Fraction(1_000_000, 24) * density + error
assert (len(primes), survivors, bonf, ceil(upper)) == (31, 12676, 20281, 28075)
assert survivors <= bonf <= upper
print('Independent toy:', survivors, bonf, ceil(upper), float(upper / survivors))
print('Independent checks passed (256 MiB address-space cap).')
```
