# z7_automatic_families — on the families with a fixed small parameter, "unforced" and "certificate" coincide (O231)

## Idea
Look for *automatic* unforced words: words whose existence needs no divisor-in-class event, and whose three unclean
sides are forced by a symbol. Every word with min(t, u, v) ≤ 2 is automatic: t = 1 and u = 1 range over Div(n + 1),
t = 2 over Div(2n + 1), u = 2 over Div(n + 2). For s = 3, 4, 7 the fixed QR prime 2 (p ≡ 1 (8)) and 2-adic pinning
make the s-families automatic too.

## Results (UNFORCED_WORDS §1, §3)
* Lemma 1.1 (PROVED). For n ≡ 5 (8) the word (1, n + 2, 2) is unforced. So CONJECTURE U is about n ≡ 1 (8).
* **Prop F / F′ (PROVED).** Let X ∈ {p+1, p+2, 2p+1, p+3, 3p+1, p+4, 4p+1, p+7, 7p+1}. Then the family with fixed side X
  contains a certificate ⟺ it contains an unforced word ⟺ X is unclean.
  * The proof uses the flip by a ψ-odd prime (s ≤ 2) and the 2-trick (s = 3: 4 ∥ X and 2 ≡ −1 (mod 3)).
  * For s = 4 every word of the family is a certificate, by (−4/·).
  * For s = 7: 8 | X, ψ(r) = (r/7), and 2 generates the residues mod 7.
* Cor 1.2 / 3.1. U(p) = 0 or N₋(p) = 0 ⟹ the Landau depth K(p) ≥ 4, and p + 7, 7p + 1 are clean.

## Literature
* The t-side half for t ≤ 4 (signed and positive) is SYNTHESIS_SPARKS4 §2.3. Mordell's identities are the classical
  form of the small-t slots (Mordell, *Diophantine Equations*, 1969, §30).
* "Clean" = composed of primes split in ℚ(√−X): the Landau–Bernays set (Landau 1908; Bernays 1912), of density
  ≍ 1/√log x.

## Barrier screen
* B1: the families are polynomial in n, and they fail on the Landau set where all of X are clean.
* B2: for s ∉ {1, 2, 3, 4, 7} the family needs a ψ-odd prime in a moving class.
* T1: at squares every X is clean (respected).
* B5: n/a. B6: n/a (pointwise statements).

## Cheap numerics
* `scripts/z7_types.c`: least-min of an unforced word is ≥ 3 ⟺ Landau triple. 0 mismatches over 464 288 primes
  ≡ 1 (8) < 3·10⁷, and over all n ≡ 1 (8) ≤ 2·10⁵.
* `scripts/z7_propF.py 100000`: 0 mismatches for s = 1, 2, 3, 4, 7; mismatches at s = 5, 6, 8.

## Assessment
PROVED structure. It shows CONJECTURE U is *not* weaker than ES-five on any automatic family. Its extra content lives
only on words with min ≥ 3, outside {3, 4, 7}. Promise 1: a clean reduction, no mechanism.
