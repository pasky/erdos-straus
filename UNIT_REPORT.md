# UNIT C15 report

## Outcome

Added §44, “Slice conspiracies: joint vanishing structure of the ray-character mass,” and verifier block `(aq)`.

- **Exact vanishing theorem:** the `(c,k)` slice vanishes exactly when the bounded exponent box of the factorization of `p²+4ck²` misses the grade `−p mod 4ck`. The equivalent character coefficient, quadratic-root progression union, and finite-set conspiracy locus are explicit in (44.2)–(44.7).
- **New proved obstruction:** if the squarefree core of `c` is `1, 2, 3`, or `6`, every such slice vanishes for every hard prime. This extends the `c=1` Gaussian obstruction; it forces 80 of the 111 slices with `ck≤30` to zero identically.
- **Structured-prime result:** every prime `p≡97 (mod 120)` has a positive `(5,1)` slice, witnessed by `D=3`.
- **Moving-divisor obstruction:** joint vanishing of `(5,1)` and `(7,1)` is not determined by their natural modulus 840: `193≡1033 (mod 840)`, but both slices vanish at 193 while `(5,1)` survives at 1033 through the moving divisor 67.
- **GRH audit:** the exact `k=1` principal mass is between logarithmic and subpower size. Standard GRH does not estimate the selected divisors of each moving `pa+1`; even an additional idealized square-root cancellation across the `O(p)` fibres leaves a `p^(1/2+o(1))` error against a `p^o(1)` principal term.

## Exact census

For all 385 primes `p≡1 (mod 24)`, `p<30000`, verifier block `(aq)` checks all 111 slices `ck≤30` by exact factor-grade dynamic programming and literal divisor enumeration.

- Vanishing depths range from 99 to 111.
- Fifteen primes vanish on all 111 slices: `2521, 9601, 12289, 13729, 15289, 18481, 19009, 20089, 21121, 21169, 21841, 27361, 27481, 28921, 29569`.
- Thus 2521’s known `k=1` zero is accompanied by vanishing of every slice in this box.
- The full histogram and cutoff table are recorded in (44.16)–(44.18) and hard-asserted in `verify.py`.

## Failure log

No finite small-box positivity theorem survives: all slices through `ck≤4` vanish identically, 161 primes still vanish through `ck≤10`, and 15 still vanish through `ck≤30` in the stated range. The exact conspiracy locus remains an infinite union/complement involving actual moving divisors, so it yields no new effective all-large-prime or exceptional-set bound. No claim is made about Erdős–Straus witness nonexistence.

## Files

- `notes.md`: §44 plus repair of one pre-existing eaten-`\r` artifact in (31.23).
- `verify.py`: exact memory-bounded block `(aq)`; `(ap)` remains reserved for the parallel unit.
- `UNIT_REPORT.md`: this report.

## Validation

- `python3 -c "import ast; ast.parse(open('verify.py').read())"`
- `uv run --with sympy,numpy,scipy python verify.py` — all checks passed in 78.93 seconds.
- `notes.md` control-byte count: zero; eaten-`\\r` pattern count: zero.
