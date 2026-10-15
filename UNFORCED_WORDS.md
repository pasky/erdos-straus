# UNFORCED_WORDS — forced vs unforced words, CONJECTURE U and the anti-Landau event (task O231, spark relay Z1)

**ES is not solved here, and no infinite case of it is claimed.** Labels as in DISCOVERIES.md. Memos `BRAINSTORM/z7_*.md`;
scripts `scripts/z7_*`. Notation (SYNTHESIS_SPARKS5): n ≡ 1 (4) odd, ψ = (·/n) (Jacobi; Legendre at primes); words
w = (t, u, v) ∈ ℤ³_{>0}, tuv − u − v = n; A = tu − 1, B = tv − 1; sides N_t = tn + 1 = AB, N_u = n + u = Av,
N_v = n + v = Bu; χ(w) = ψ(A) = ψ(B); certificate ⟺ χ = −1 (N₋ = #certificates). A positive integer x is *clean* if no
prime r | x has ψ(r) = −1. C_n := the multiplicative semigroup of clean integers. Forced = some side clean
(⟹ χ = +1, Lemma S); U = #words with no clean side. Words are counted ordered in (u, v), as in s5_U.c.

## 0. Iteration log (construction → kill → which hypothesis → modification)
(I1) Construction: look for "automatic" unforced words — words whose sides are polynomials in n with an NR factor
forced by a symbol. Found: n ≡ 5 (8) is trivial (ψ(2) = −1). For n ≡ 1 (8): the word (n + 2, 1, 1) has sides
(n + 1)², n + 1, n + 1, so it is unforced iff n + 1 is unclean. → §1.
(I2) Kill: the same n + 1 also carries a *certificate* (u = 1 family, A ranges over all divisors of n + 1). Every word
with min(t, u, v) ≤ 2 lives on one of the three "automatic" side numbers n + 1, n + 2, 2n + 1, and on each of these
families unforced ⟺ certificate (Prop F). So nothing is gained over ES-five unless min ≥ 3. → §1.

## 1. The automatic families: unforced ⟺ certificate when min(t, u, v) ≤ 2 (PROVED)
**Lemma 1.1 (n ≡ 5 (8)).** For odd non-square n ≡ 5 (8), the word (1, n + 2, 2) is unforced: N_t = n + 1 and
N_u = 2(n + 1) are even and ψ(2) = −1; N_v = n + 2 has ψ(n + 2) = ψ(2) = −1, so it has a prime factor with ψ = −1.
Hence U(n) ≥ 1. (Not a certificate: χ = ψ(n + 1) = +1.) So CONJECTURE U has content only at n ≡ 1 (8). ∎

**Families with a small parameter.** A word with t = 1 is (1, d + 1, (n+1)/d + 1) for a divisor d = A of n + 1 (every
divisor occurs); u = 1: (d + 1, 1, (n+1)/d), A = d, again every divisor of n + 1; t = 2: A any divisor of 2n + 1,
u = (A+1)/2, v = ((2n+1)/A + 1)/2; u = 2: A = 2t − 1 any divisor of n + 2 (odd), v = (n+2)/A. (v = 1, 2: symmetric.) The
fixed side of these families is n + 1 (t = 1, u = 1, v = 1), 2n + 1 (t = 2) or n + 2 (u = 2, v = 2).

**Prop F (PROVED).** Let n ≡ 1 (8) be odd, X ∈ {n + 1, n + 2, 2n + 1} and F_X the family(ies) with fixed side X. TFAE:
(i) F_X contains a certificate; (ii) F_X contains an unforced word; (iii) X is unclean.
*Proof.* (iii) fails ⟹ every word of F_X has the clean side X, so it is forced and (Lemma S) not a certificate. (iii) ⟹
(i): pick a prime r | X with ψ(r) = −1 and take A = r (every divisor of X is an admissible A in F_X); χ = ψ(r) = −1.
(i) ⟹ (ii): a certificate has no clean side (Lemma S). ∎
**Corollary 1.2.** If U(n) = 0 or N₋(n) = 0, then n + 1, n + 2 and 2n + 1 are all clean (a *Landau triple*), and
then every word with min(t, u, v) ≤ 2 is forced. Conversely, at a Landau triple U(n) ≥ 1 ⟺ some word with
min(t, u, v) ≥ 3 has three unclean sides. At primes p ≡ 1 (8), by Lemma S's formula ψ(r) = (−X/r): p + 1 clean ⟺ all odd
r | p + 1 are ≡ 1 (4); p + 2 and 2p + 1 clean ⟺ all their prime factors are ≡ 1, 3 (8). (Same for composite n with
Jacobi symbols.)
So the anti-Landau event is genuinely weaker than a certificate only on words with min ≥ 3. On the automatic families
the two coincide exactly, and both reduce to the Landau-type condition "one of three fixed linear forms has a prime
factor in a non-split class".

**Numerics (EVIDENCE; `scripts/z7_types.c`).** All 464 288 primes p ≡ 1 (8), p < 3·10⁷: U ≥ 1 everywhere. The least
min(t, u, v) of an unforced word is ≥ 3 exactly at the 10 508 Landau-triple primes (0 mismatches), as Prop F
predicts. Over n ≡ 1 (8) non-square ≤ 2·10⁵ including composites there are 0 mismatches, and the only U = 0 case is
105 = 3·5·7, a Landau triple (106 = 2·53, 107, 211 are all clean mod 105). The Landau-triple fraction among primes
≡ 1 (8) is 3.3 % / 2.7 % / 2.2 % on the decades (3·10⁴, 3·10⁵) / … / (3·10⁶, 3·10⁷). This slow decay matches the
(log p)^{−3/2} heuristic for three half-dimensional conditions. Largest least-min observed at a Landau triple: 18.
