# s3_isogeny_mixing — (J)35 certificate edges × (J)16 Prop 2.3 × expander mixing with structured sets

**Combines:** (J)35 (five-slice certificates = path-shaped edges of the supersingular 2-isogeny graph G(p,2); t is a
Frobenius distance, t = 1 is the F_p-spine), (J)16 Prop 2.3 (the ray condition is free on ONE endomorphism),
(J)26 by-product (#words ≪ n^{1/3+o(1)}), Pizer (G(p,2) is Ramanujan: 3-regular, λ ≤ 2√2).

## Idea
Force an edge between two STRUCTURED vertex sets (e.g. S = spine, T = CM-by-ℤ[√−A] vertices) by the expander mixing
lemma, and arrange that every S–T edge is a certificate.

## Literature
Pizer, *Ramanujan graphs and Hecke operators* (Bull. AMS 1990); Alon–Chung expander mixing lemma; CONSTRUCTIVE_ES.

## Barrier screen (PROVED, elementary)
Mixing forces e(S,T) > 0 only if √(|S||T|) > λN/d = (2√2/3)N, i.e. |S|, |T| > (8/9)N (as |S|, |T| ≤ N). But the
endpoints of certificate edges form a set of size ≤ 2·#{χ = −1 words} ≪ p^{1/3+o(1)} = o(N). Hence no pair (S, T)
passing the mixing threshold can have all its edges among certificates, and structured sets of size o(N) (spine ≍ √p,
CM sets ≍ h(−4A)) are below the threshold: the mixing lemma cannot force a certificate. Using (J)16 Prop 2.3 to place
one endomorphism freely does not change the count (the second endomorphism is the B3 cost).

## Cheap numerics (`scripts/s3_isogeny_counts.py`, 20 primes above each p₀)
#χ = −1 words: mean 43 / 82 / 98 / 148 and max 69 / 227 / 189 / 359 at p ≈ 10³ / 10⁴ / 10⁵ / 10⁶, against
N ≈ p/12 = 83 / 833 / 8333 / 83333 vertices: max/N = 0.83, 0.27, 0.023, 0.0043 → 0.

## Assessment
PROVED negative (B3 in spectral form, extending (J)35 §5's Hecke remark): certificate edges are a polylog-size,
spectrally invisible subset. A structured route would need the certificate property to be a *vertex* property on a
linear-size set, which the counts exclude. Promise 0.
