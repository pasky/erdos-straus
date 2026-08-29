# UNIT A18 report

## Outcome

Section 51 defines the minimal Type-II witness modulus `W(p)` and proves, at the campaign's internal level of rigor, a parameterized truncated version of the Section 39 assembly.

- Fixed-polylogarithmic supply: `# {p <= N : W(p) > T} << N exp(-c (log T)^2 log log T)` in the exact window (51.12). This uses Lemma 16.3, not Theorem 34.8.
- Cubic supply: `# {p <= N : W(p) > T} << N exp(-c (log T)^3)` in the exact window (51.14). This inherits Theorem 34.8 and is CLAIMED/PROVISIONAL.
- At `T = exp(alpha (log N)^(1/4))`, the cubic tail reproduces Theorem 39.7. At `T = (log N)^A`, the two tails have exponents `(log log N)^2 log log log N` and `(log log N)^3`.
- `H_MOD(A)` is introduced as the Type-II pointwise analogue of Section 50's Type-I `H_SPF(A)`. Neither is claimed to imply the other.
- The PW Section 4 truncation is credited with the pre-existing square-log tail; the multiplier families add the `log log T` or `log T` factor.

## Effectivity result

The audit found that the premise “Lemma 16.3 is elementary” is false: its lower bound explicitly uses Bombieri--Vinogradov. Polynomially large moduli also do not by themselves eliminate a possible exceptional character, because imprimitive characters can have small conductor.

Section 51 repairs the supply chain by:

1. using effective Bombieri--Vinogradov after deleting moduli divisible by the at-most-one Landau--Page exceptional conductor; and
2. proving that the multiplier boxes retain a fixed positive harmonic mass after this deletion, uniformly in every multiplier subfamily and fibre.

This makes the class-supply conclusions needed by Theorems 16.4, 39.7, and 51.2 effective. The result is record-adjacent and is therefore marked CLAIMED/PROVISIONAL pending hostile review.

## Exact labels of new claims

- **Lemma 51.1:** proved internally; inherits the provisional review status of the Section 39 CRT/moment/Bonferroni machinery.
- **Theorem 51.2(1):** unconditional, proved internally, does not use Theorem 34.8; still carries the Section 39 review qualification.
- **Theorem 51.2(2):** proved internally conditional on the correctness of the inherited chain; CLAIMED/PROVISIONAL because it uses Theorem 34.8.
- **Corollary 51.3:** same split status as Theorem 51.2.
- **`H_MOD(A)`:** hypothesis, explicitly unproved.
- **Lemma 51.4:** standard cited effective Bombieri--Vinogradov input, with a proof/dependency sketch; not claimed as a new independent proof of Bombieri--Vinogradov.
- **Lemma 51.5:** proved internally.
- **Theorem 51.6:** proved internally; CLAIMED/PROVISIONAL because it is a record-adjacent repaired-chain effectivity claim.
- **Computational 51.7:** exact only for the stated finite range; informational.

## Honest failure log

- No pointwise prime is newly settled asymptotically. Neither `H_MOD(A)` nor `H_SPF(A)` is proved.
- The literal all-low-congestion-triples absolute-error `o(1)` assertion in the first sentence of Theorem 34.8 is not made effective. Exceptional-conductor deletion makes its class-mass consequence effective, which is all the exceptional-set chain uses.
- The fixed-polylogarithmic tail cannot honestly be called elementary: Lemma 16.3 uses Bombieri--Vinogradov.
- No direct comparison with Vaughan 1970 was possible; the paper remains inaccessible, so the comparison is only with Pomerance--Weingartner's reconstruction.
- The finite `W(p)` data and fitted curves prove no growth law.

## Hostile-review priorities

1. Check Lemma 51.5's uniform deletion argument, especially the `p > Ck` weighted box estimate, its boundary terms, and simultaneous intersection with the low-omega and low-congestion pruning.
2. Check that the standard effective Bombieri--Vinogradov statement (51.20) has exactly the max-over-residues and dyadic pi form used here after excluding all multiples of one conductor.
3. Replay Lemma 51.1 with `mu = t^2 log K`: the parameterized factorial moment, bad-fibre Chernoff bound, Bonferroni degree, and `exp(O(mu t))` rounding ledger are the load-bearing interpolation.
4. Check that Lemma 16.3's lower mass and Theorem 34.8's lower mass are indeed furnished inside the canonical dyadic boxes used by the c-free family.
5. Preserve the status distinction: effectivity does not validate the provisional correctness of Theorems 34.8 or 39.7.

## Verification

`verify.py (ax)`:

- exactly computes the Lemma-16.1 class harvest for every `M <= 3000`, `M = 3 mod 4`, and all 3,202 primes `p < 300000`, `p = 1 mod 24`;
- obtains tails `(226, 19, 0, 0)` at `T = (25, 100, 400, 1600)` and maximum `W = 279`;
- checks an exact six-atom inclusion--exclusion probability against direct counting over a period of 39,215; and
- checks three finite exceptional-conductor deletion toys for conductors 3, 5, and 7.

The full verification command passed in 87.7 seconds. AST parsing, `git diff --check`, and the notes control-byte scan also passed.
