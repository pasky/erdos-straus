# UNIT F20 report

## Outcome

Added §54, “The lower tail: logarithmic witness moduli are necessary,” and `verify.py (ba)`.  The section proves that both pointwise polylogarithmic hypotheses are false for every `0<A<1`, using residue-one escape classes and effective Linnik with the conservative published exponent `L=5.2`.

## Proved

- **Theorem 54.1 (Type II):** with `M(T)=lcm(1,...,floor(T))`, every prime `p=1 (mod M(T))` has `W(p)>T`.  The proof directly replays the full Lemma-16.1 datum: `m | u+v`, while `2 <= u+v <= uv+1 <= (m+1)/4+1 < m`, including `m=3`.
- Effective Linnik supplies an unbounded sequence with `p <= C M(T)^5.2 = exp((5.2+o(1))T)`.  Hence `limsup W(p)/log p >= 1/5.2 > 0.19`.
- **Corollary 54.2:** `H_MOD(A)` is false for every `0<A<1`; only `A>=1` remains open.  For each such `A`, the exceptional sets in Corollary 51.3 are nonempty at infinitely many heights, while retaining the section's stated almost-all upper bounds and review labels.
- **Theorem 54.3 (Type I):** with `R(T)=lcm(24, product of primes <=T)`, every prime `p=1 (mod R(T))` has `chi_s(p)=1` for every squarefree `s<=T`.  Thus every slice with `ck<=T` has zero unrestricted slice mass, no good prime, `ck_pr(p)>T`, and `ck_min(p)>T`.
- Effective Linnik gives `limsup ck_min(p)/log p >= 1/5.2 > 0.19` along hard primes.
- **Corollary 54.4:** `H_SPF(A)` is false for every `0<A<1`; only `A>=1` remains open.  The stronger unrestricted-slice lower bound is stated explicitly.

## Scope and prior results

- Theorem 48.5 does **not** already prove vanishing or an infinite lower-bound sequence; it only escapes bounded fixed-divisor guarantees.  §54 says this explicitly.  The actual vanishing input is Theorem 50.5/Theorem 48.1, now quantitatively coupled to Linnik.
- The constructed progressions have relative prime density `1/phi(M(T))=exp(-(1+o(1))T)`, so their existence is consistent with the much larger upper envelopes in §§51 and 53.  The true exceptional-set decay remains open.
- No exceptional denominator, representation failure, or new pointwise solvability result is claimed.  Larger multiplier moduli or slices may still work.

## Effectivity and citations

- Xylouris, *Acta Arith.* 150 (2011), 65–91, is cited at the conservative exponent `L=5.2`, with Heath-Brown (1992) as precursor.  The Linnik constant/threshold used are effectively computable.
- Rosser–Schoenfeld (1962) is cited for the explicit bounds `psi(x)<1.03883x` and `theta(x)<1.01624x`; the classical effective prime number theorem gives the `(1+o(1))x` asymptotic used for the limiting constant.
- Quadratic reciprocity and Bertrand's postulate are named where used.  No ineffective Siegel lower bound enters.

## Verification

`verify.py (ba)` checks:

- the full Lemma-16.1 class harvest at every `m=3 (mod 4)`, `m<=300`, including `1` absent and the size inequality on every datum (982 data); under `ES_FULL_SCAN=1` this extends through 3000;
- least-prime regressions `(T,R,p)=(5,120,241),(7,840,2521),(11,9240,9241)` by direct search;
- actual Jacobi/Kronecker values for every squarefree core and direct streamed grade counts proving `M_{c,k}(p)=0` with no good prime for every `ck<=T`;
- the `T=11` prime misses the `(ax)`-convention Type-II harvest through modulus 11;
- informational finite ratios `log p/log R`.

Pre-commit checks completed:

- `ast.parse(verify.py)`: passed.
- Full foreground run `uv run --with sympy,numpy,scipy python verify.py`: all blocks through `(ba)` passed in 1:28.65.
- `notes.md` forbidden control bytes: 0.
- Section-order grep: §54 follows §53; no §55 was created.
- `git diff --check`: passed.
