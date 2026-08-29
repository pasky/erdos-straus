# UNIT B18 report

## Delivered

- **Theorem 52.1 (proved):** for each fixed unforced slice and fixed active hard-prime class, residual raw-slice vanishing is at most
  \(X(\log X)^{-1-2/\varphi(4ck)}\). The proof uses Theorem 50.1's contrapositive, a fixed-dimensional upper-bound beta/Selberg sieve on integers, ordinary Mertens, and Mertens in a fixed arithmetic progression. It does not use Bombieri--Vinogradov or Siegel--Walfisz.
- **Corollary 52.2 (proved):** no reduced refinement of an active slice-class is identically vanishing on its primes. Thus the universal-core and genus laws are the complete fixed-congruence vanishing layers for one fixed slice. This does not classify simultaneous multi-slice loci.
- **Proposition 52.3 (proved, ineffective):** uniformly for \(4ck\leq(\log X)^\theta\), the same method gives an epsilon-loss exponent and the natural \(1/\varphi(Q)\) progression factor. This version uses Siegel--Walfisz and is explicitly labelled ineffective; it does not perform slice stacking.
- **Computational 52.4 (exact ranges, informational):** exact default census through 30,000 and optional `ES_FULL_SCAN=1` census through 100,000. It records all 31 residual frequencies, four class panels, exact root and Type-I reconstruction checks, composite-witness shapes for the `ck_pr > ck_min` gaps, and selected same-core/different-core joint-frequency ratios.
- `verify.py (ay)` is self-contained after `(aw)`, streamed by norm, and contains regression assertions for every reported exact count.

## Honest failures and walls

- No pointwise bound on conspiracy depth \(D(p)\), no case of \(H_{\rm SPF}\), and no union or growing-dimensional sieve over slices was proved.
- No unconditional lower bound for residual vanishing in a fixed active class was proved. Prime-norm and prescribed almost-prime subfamilies meet the usual sieve parity barrier; infinitude per active slice-class remains open here.
- The census rejects the proposed oversimplification that every composite witness is a product of two distinct wrong-grade primes. Below 30,000, 68 of 98 canonical target divisors are such semiprimes, but 24 use at least three prime factors (with multiplicity) and 6 are prime powers. The corresponding full-range counts are 199, 93, and 16.
- Empirical pair ratios are often near independence after genus conditioning, but stable exceptions such as `(5,1)` with `(5,2)` and `(5,1)` with `(10,1)` prevent an independence claim.

## Labels

- **Proved:** Theorem 52.1, Corollary 52.2, Proposition 52.3.
- **Computational (exact range):** Computational 52.4 and all constants asserted by `verify.py (ay)`.
- **Assessment only:** approximate pair independence for many pairs; parity-barrier/lower-bound discussion.
- **Heuristic only:** the finite comparison to \((\log X)^{-2/\varphi(h)}\). No asymptotic fit is claimed.

## Hostile-review priorities

1. Check the exact upper-bound fundamental-lemma form in (52.12), especially the chosen level \(D=X^{1/2}\), fixed large sieve parameter \(u\), and the elementary remainder sum.
2. Check the local factor at good primes: three removed classes total, correction `(1-3/q)/(1-1/q)`, and exponent \(2/\varphi(h)\).
3. Check effectiveness wording for fixed-modulus Mertens in arithmetic progressions versus the explicitly ineffective growing-modulus Siegel--Walfisz proposition.
4. Check the uniform partial summation from \(y=\exp((\log X)^\epsilon)\) to fixed-power \(z\), which is where the factor \(1-\epsilon\) enters.
5. Check that Corollary 52.2 is only about reduced, fixed refinements and one fixed slice; it must not be read as a multi-slice or pointwise theorem.
6. Re-run `ES_FULL_SCAN=1` to scrutinize the 100,000 regression constants and memory behavior.
