# s3_isogeny_mixing — (J)35 certificate edges × (J)16 Prop 2.3 × expander mixing with structured sets

**Combines:** (J)35 (five-slice certificates = path-shaped edges of the supersingular 2-isogeny graph G(p,2); t is a
Frobenius distance, t = 1 is the F_p-spine), (J)16 Prop 2.3 (the ray condition is free on ONE endomorphism),
(J)26 by-product (#words ≪ n^{1/3+o(1)}), Pizer (G(p,2) is Ramanujan: 3-regular, λ ≤ 2√2).

## Idea
Force an edge between two STRUCTURED vertex sets (e.g. S = spine, T = CM-by-ℤ[√−A] vertices) by the expander mixing
lemma, and arrange that every S–T edge is a certificate.

## Literature
Pizer, *Ramanujan graphs and Hecke operators* (Bull. AMS 1990); Alon–Chung expander mixing lemma; CONSTRUCTIVE_ES.

## Barrier screen (Assessment; corrected after self-review R-O208 #6)
Centered mixing lemma: |e(S,T) − d|S||T|/N| ≤ λ√(|S||T|(1 − |S|/N)(1 − |T|/N)), d = 3, λ ≤ 2√2. With s = |S|/N,
t = |T|/N it forces e(S,T) ≥ N·F(s,t), F := d·st − λ√(st(1−s)(1−t)); e.g. s = t > λ/(d+λ) ≈ 0.485 suffices. Two regimes:
(i) s, t bounded away from the curve F = 0 inside F > 0: then e(S,T) ≥ cN, but all certificate edges together number
≤ #{χ = −1 words} ≪ p^{1/3+o(1)} = o(N) (PROVED, (J)26 by-product; empirically polylog-size), so S–T edges cannot all
be certificates; (ii) (s, t) within O(p^{−2/3+o(1)}) of the threshold curve, or one set co-small (S ⊇ almost all
vertices — then E(S,T) is essentially "all edges at T", a tautology that presupposes knowing T's edges). In neither
regime does the lemma supply a certificate that was not put in by hand. Structured sets of size o(N) (spine ≍ √p,
CM sets ≍ h(−4A)) satisfy F < 0 unless the partner set is co-small. Using (J)16 Prop 2.3 to place one endomorphism
freely does not change the count (the second endomorphism is the B3 cost).

## Cheap numerics (`scripts/s3_isogeny_counts.py`, 20 primes above each p₀)
#χ = −1 words: mean 43 / 82 / 98 / 148 and max 69 / 227 / 189 / 359 at p ≈ 10³ / 10⁴ / 10⁵ / 10⁶, against
N ≈ p/12 = 83 / 833 / 8333 / 83333 vertices: max/N = 0.83, 0.27, 0.023, 0.0043 → 0.

## Assessment
Assessment (with PROVED counting inputs), B3 in spectral form, extending (J)35 §5's Hecke remark: certificate edges
form an o(N) set (≪ p^{1/3+o(1)} proved, polylog-size empirically) that mixing cannot robustly force. A structured route would need the certificate property to be a *vertex* property on a
linear-size set, which the counts exclude. Promise 0.
