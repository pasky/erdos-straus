# UNIT H20 report

## Outcome

Added `notes.md` §55, “General numerators: truncated tails and the effectivity of the m-uniform chain,” plus `verify.py (bb)`.

- Defined the minimal general-numerator witness modulus `W_m` compatibly with §43 and with `W_4=W` from (51.1).
- Proved the parameterized truncated assembly with the thinning retained.  With
  `lambda_m=eta_1(m)/phi(m)` and `theta_m=eta_2(m)/phi(m)`, the two tail masses are
  `lambda_m (log T)^2 log log T` and `theta_m (log T)^3`.
- Recorded the honest windows, including the term needed when thinning makes the mass bounded:
  `log N >= C[log T + lambda_m (log T)^3 log log T]` and
  `log N >= C[log T + theta_m (log T)^4]`, uniformly for each fixed `m <= (log T)^B` range.
- Checked that the cubic top `log T ~ (log N/theta_m)^(1/4)` exactly recovers Theorem 43.12 and that the Layer-1 top recovers (43.13).  No range extension is claimed.
- Added the polylogarithmic tails and the fixed-`m` pointwise frame `H_MOD,m(A)`; no pointwise result is claimed.

## Effectivity resolution

The flagged E19 case is not vacuous.  The BV progression modulus in §43 is `q=muv`.  If the Page conductor `r` divides `m`, every such modulus is divisible by `r`, so Lemma 51.5-style deletion would remove the entire supply.

The repair in Lemma 55.4 splits the cases exactly:

1. no Page conductor: retain all boxes;
2. `r` does not divide `m`: choose a prime-power component missing from `m`, impose that its prime does not divide `uv`, and apply the §51 deletion argument even when `gcd(r,m)>1`;
3. `r` divides `m`: retain multipliers with `chi_r(-k^{-1})=-1`.  The displayed exceptional explicit-formula term is then favorable.  An elementary dyadic progression count proves that this sign class retains a fixed fraction of `eta_1(m) log K`; (43.36) shows that the structured random fibres `J_c` retain such mass after quarantine.

This gives effective downstream Layer-1 tails and effective constants in the cubic tail and Theorem 43.12 conditional on their existing correctness labels.  It deliberately does not effectivize arbitrary adversarial sparse-`J` lower bounds, nor Theorem 43.7's ancillary all-triples absolute-error `o(1)` clause.  The effectivity perimeter is tabulated in (55.18).

## Computational companion

`verify.py (bb)`:

- exactly harvests all Lemma-43.1 classes for `m in {3,5,6,7}`, modulus at most 1500;
- reproduces the complete `(ax)` `m=4` class family through 1500 and spot-checks moduli 3, 7, and 23;
- records coprime-prime tail counts at `T=(25,100,400)`:
  - `m=3`: `(0,0,0)`;
  - `m=5`: `(875,61,5)`;
  - `m=6`: `(3136,663,77)`;
  - `m=7`: `(2222,438,35)`;
- checks `eta_2(3)=9/11`, `eta_2(5)=25/29`, `eta_2(6)=36/55`, `eta_2(7)=49/55` from both the product and direct local harmonic factors;
- prints informational Layer-1/cubic finite shape fits;
- verifies the true `m=r=5` shadow: every BV modulus is `5uv`, hence divisible by 5, while both exceptional-character signs occur.

## Validation

- `ast.parse(verify.py)`: passed.
- Full foreground verification: `uv run --with sympy,numpy,scipy python verify.py`: passed through `(bb)`.
- Control bytes in `notes.md` and `verify.py`: zero.
- `git diff --check`: passed.
- §55 follows §53 in this clone; no §54 was created or referenced.

## Status discipline

The Layer-1 tail uses no Theorem 34.8/43.7 but retains §39's internal-review qualification.  The cubic tail, its polylog corollary, and the Theorem-43.12 recovery remain **CLAIMED/PROVISIONAL**.  PW remains the proved general-`m` benchmark; §55 states both truncated crossover ratios and makes no priority or pointwise claim.
