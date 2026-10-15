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

## 2. Where the anti-Landau content sits, and parity across a family
**Lemma 2.1 (symbol-visible and symbol-blind sides; PROVED).** ψ(N_u) = ψ(u), ψ(N_v) = ψ(v), ψ(N_t) = ψ(1) = +1, and
ψ(u)ψ(v) = χ. Hence:
(a) a word with ψ(u) ≠ ψ(v) is a certificate (χ = −1, all sides unclean);
(b) a word with ψ(u) = ψ(v) = −1 has N_u, N_v unclean for free. It is unforced iff N_t ∉ C_n, i.e. tn + 1 has
    ≥ 2 prime factors (with multiplicity) with ψ = −1;
(c) a word with ψ(u) = ψ(v) = +1 is unforced iff all three sides contain ≥ 2 ψ-odd prime factors.
So a non-certificate unforced word always needs the t-side event "tn + 1 ∉ C_n". No symbol can detect this event,
because ψ(tn + 1) = 1 identically. This is the precise "anti-Landau" kernel of CONJECTURE U beyond ES-five. In cases
(b)/(c) a congruence covering cannot supply it: any covering identity evaluates fixed symbols, and those are all +1 on
the class n ≡ 1 (mod M) (B1-type).

**Flip Lemma 2.2 (PROVED).** Fix X ∈ {t, u, v} and its value. The X-family of words is in bijection with the set of
divisors D of N_X in the class D ≡ −1 (mod X): D = A for X = t (then B = N_t/A), D = A for X = u (then t = (A+1)/u,
v = N_u/A), and D = B for X = v. On it, χ = ψ(D). Hence the family contains a certificate iff the image of
Div(N_X) → (ℤ/X)^× × {±1}, d ↦ (d mod X, ψ(d)), contains (−1, −1). In particular, if some word of the family has
D and N_X has
* a prime r ∥ N_X with ψ(r) = −1 and r ≡ 1 (mod X) (take D′ = Dr or D/r), or
* primes r ∥ D, s ∥ N_X/D with r ≡ s (mod X) and ψ(r) ≠ ψ(s) (take D′ = Ds/r),
then the family contains a certificate. *Proof.* D′ ≡ D ≡ −1 (mod X), D′ | N_X, and ψ(D′) = −ψ(D). Each D in the class
gives a positive word: for X = u, t = (D+1)/u ≥ 1 and v = N_u/D ≥ 1, and similarly for the others. ∎
For X ∈ {1, 2} every odd r is ≡ 1 (mod X), which recovers Prop F. For X ≥ 3 the flip needs a ψ-odd prime of N_X in
the class 1 (mod X) (or a matched swap). That is a divisor-in-class condition with the modulus X part of the word,
i.e. B2 verbatim.

**Numerics (EVIDENCE; `scripts/z7_flip.py 9 200000`, primes p ≡ 1 (8) < 2·10⁵).** There are 94 262 non-certificate
unforced words. 73 % are flippable by Lemma 2.2's two moves. 96 % have a certificate somewhere in one of their three
families. Flippable but no family certificate: 0, consistent with the lemma. So "parity across the family of a shared
side" is the typical mechanism by which an unforced word sits next to a certificate. But the flip needs a prime in a
moving residue class, so it is not a deterministic bridge U ≥ 1 ⟹ N₋ ≥ 1 (goal 2): Lemma 2.2 *is* the e-slice form
−1 ∈ Σ_e(N), with e = X.

## 3. Extending Prop F: s = 3, 4, 7; Landau depth; a Dickson-conditional obstruction
(I3) Construction attempt: push Prop F to larger fixed parameters s, using the *fixed* QR prime 2 as a flip tool.
**Prop F′ (PROVED; p ≡ 1 (8) prime).** For s ∈ {3, 4, 7} and X ∈ {p + s, sp + 1}: the X-family (u = s or v = s,
resp. t = s) contains a certificate ⟺ it contains an unforced word ⟺ X is unclean.
*Proof.* As in Prop F it suffices to show that X unclean ⟹ some admissible D (D | X, D ≡ −1 (mod s)) has ψ(D) = −1.
For odd primes r | X, Lemma S gives ψ(r) = (−s/r), and ψ(2) = +1.
* s = 3: 4 ∥ X (since p ≡ 1 (8)). Let r be an odd prime of X with ψ(r) = −1. Then D = r (if r ≡ 2 (3)) or D = 2r
  (if r ≡ 1 (3)) is admissible.
* s = 4: X is odd and ψ(r) = (−4/r) = (−1/r), so ψ(D) = (−1/D) = −1 for every D ≡ 3 (4). The family is nonempty ⟺
  X has a prime r ≡ 3 (4) ⟺ X is unclean, and then *every* word of the family is a certificate.
* s = 7: 8 | X, and 7 ∤ X since p ≠ 7. ψ(r) = (−7/r) = (r/7) (quadratic reciprocity), so a ψ-odd r is a
  non-residue mod 7. The powers 1, 2, 4 of 2 run through the residues mod 7, so one of r, 2r, 4r is ≡ 6 (mod 7), and it
  divides X. ∎
*2-adic remark.* For X = s ≡ 7 (8), or 4 | s, every word of the family is a certificate. For t ≡ 7 (8), 8 | AB forces
4 | A or 4 | B; for u ≡ 7 (8), 8 | Av forces 4 | A or 4 | v. This is the three-bit law on a family: χ is 2-adic
(SYNTHESIS_SPARKS4 §1). For s = 7 it combines with the 2-trick, so nonemptiness ⟺ uncleanness. For s = 8 the
equivalence fails (nonempty needs a divisor ≡ 7 (8)).
**Numerics (EVIDENCE; `scripts/z7_propF.py 100000`, primes p ≡ 1 (8) < 10⁵).** For s = 1, 2, 3, 4, 7 and both kinds
of family there are 0 mismatches in "unclean ⟺ certificate ⟺ unforced". At s = 5, 6, 8, "unclean ⟹ certificate" fails
at 183–328 primes per family. "Unforced ⟺ certificate in the family" fails only at s = 5 (24 resp. 39 primes). At
s = 6, 8 the family's unforced words all coincide with its certificates even when the side is unclean.

**Landau depth.** Let K(p) = max{K : p + s and sp + 1 are clean for all 1 ≤ s ≤ K}.
**Corollary 3.1 (PROVED).** U(p) = 0 or N₋(p) = 0 ⟹ K(p) ≥ 4 and also p + 7, 7p + 1 are clean. If K(p) ∈ {2, 3, 6},
then some word with min(t, u, v) = K(p) + 1 is a certificate (s = 3, 4, 7 respectively).
**Numerics (EVIDENCE; `scripts/z7_depth.c`, all 464 288 primes p ≡ 1 (8) < 3·10⁷).** The histogram of K is
0: 356 992, 1: 96 788, 2: 7 619, 3: 1 965, 4: 715, 5: 153, 6: 37, 7: 6, 8: 8, 9: 4, 10: 1 (p = 21 746 761).
The least min(t, u, v) of an unforced word equals K(p) + 1 at every prime with K ∈ {2, 3, 6, 7, 9, 10}. It exceeds
K(p) + 1 at 41/715 primes with K = 4, at 29/153 with K = 5 and at 3/8 with K = 8, always by ≤ 9.
**Theorem 3.2 (CONDITIONAL on Dickson's prime k-tuples conjecture).** For every K ≥ 1 there are infinitely many primes
p ≡ 1 (8) with K(p) ≥ K. At these primes every word with min(t, u, v) ≤ K is forced (neither a certificate nor
unforced).
*Proof.* Let M = 8·∏_{3 ≤ ℓ ≤ 2K+1} ℓ^{a_ℓ} with ℓ^{a_ℓ} > K + 1 (ℓ prime; also 2^{a_2} > K + 1). Put p = 1 + Mx. For
1 ≤ s ≤ K and ℓ ≤ 2K + 1, p + s ≡ sp + 1 ≡ s + 1 (mod ℓ^{a_ℓ}), so v_ℓ(p + s) = v_ℓ(sp + 1) = v_ℓ(s + 1). Hence
p + s = (s + 1)·L_s(x), sp + 1 = (s + 1)·L′_s(x) with L_s = 1 + (M/(s+1))x and L′_s = 1 + (sM/(s+1))x. The forms p,
L_s, L′_s (L′_1 = L_1) are pairwise non-proportional, ≡ 1 mod every ℓ ≤ 2K + 1, and number ≤ 2K + 1 < ℓ for every
other prime ℓ. So the system is admissible, and Dickson gives infinitely many x with all of them prime. Then every
prime factor of s + 1 is ≤ K + 1 and is a residue mod p (p ≡ 1 mod ℓ for odd ℓ, p ≡ 1 (8) for ℓ = 2). Also
ψ(L_s) = ψ(p + s)ψ(s + 1) = ψ(s) = +1, because s is a product of primes ≤ K. Likewise ψ(L′_s) = ψ(1)ψ(s + 1) = +1. So
p + s and sp + 1 are clean. A word with min = s ≤ K has the side sp + 1 (if t = s) or p + s (if u or v = s). ∎
So **no proof of CONJECTURE U (or of ES-five) can use only words of bounded minimum parameter**. This is the U-analogue
of B2's "fixed finite slice sets fail i.o. under H" and of SQ_±'s Dickson-conditional "no finite t-set". The
hypothesis a U-proof must violate is boundedness of the family; the escape is H-A (growing family). The observed depth
grows slowly: max K = 10 below 3·10⁷.
