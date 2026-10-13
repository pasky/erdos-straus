# bsE_depth_characters — depth-aspect character/Kloosterman sums: what they can and cannot see (O178)

## Idea
(a) Over ℤ, detect "divisor of N_s in a class mod q^s" with characters mod q^s, and use Postnikov's formula
(χ(1 + q^k x) = e(f(x)/q^{s−k}), f a polynomial). (b) In F_q[T], count the slice families (a hyperbola EE' ≡ 1 mod T^s in a
box) with Kloosterman sums mod T^r. These are explicitly evaluable: S(a, b; T^r) = 0 for r ≥ 2 when T | b, T ∤ a, and Salié-type
closed forms hold otherwise (stationary phase).
## Literature
Postnikov (1956); Iwaniec (1974); Milićević (2016); Banks–Shparlinski (J. Anal. Math., 2019, powerful moduli); for F_q[T]
Kloosterman sums: Weil, and the elementary stationary phase (e.g. Iwaniec–Kowalski §12.3 for p^r, transcribed).
## Barrier screen
(a) B6/B3: the sum over χ of Σ_{ab | N} χ(a)χ̄(b) is a sum over ≤ τ(N)² terms, with no interval to cancel over. (b) The box count
by Fourier analysis is main term plus square-root-size Kloosterman terms. It cannot beat square root termwise, but the
elementary casework of DEPTH_ASPECT Lemma 2.2 does (2/5 < 1/2).
## Cheap numerics
`scripts/bsE_famcount.c`: actual Case B counts at q = 3 are 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104, 48 for s = 4..15, polynomial-looking, far
below q^{s/2}.
## Assessment
PARTIAL → the analytic depth tools are the *wrong* tool here. The win is elementary (divisor casework); see bsE_et_casework_depth.
