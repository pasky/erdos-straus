# y10_hecke_witness — the ES witness on p = m² + k is a quadratic residue symbol of ℚ(√−k) (O221)

## Idea
Every Type I/II solution of n ≡ 1 (4) carries a witness D with (D/n) = −1 (NEAR_SQUARE Lemmas 1.1/1.3: D = d resp.
de). On p = m² + k = N(π), π = m + √−k, a polynomial witness D(m) gives (D(m)/p) = (D(−√−k)/π)_K. If D(−√−k) ∈ ℚ the
symbol is a character of p (bounded conductor ⇒ +1 at locally-square p: T1). Otherwise it is, by reciprocity in K,
a ray-class character evaluated at the principal ideal (m + √−k) — it sees the *imaginary direction* of π, which no
congruence on p sees.

## Literature
Quadratic reciprocity in imaginary quadratic fields (Hilbert symbols; e.g. Lemmermeyer, *Reciprocity Laws*, ch. 4);
the ES witness form is ET Prop 1.6's proof.

## Barrier screen
B2/B6: at a single p the symbol (D(−√−k)/π)_K is again a "divisor in a class" condition. T1: at k = 0 every
polynomial witness is rational. The dictionary is exactly the escape route of H-A (moving modulus): the modulus
D(m) grows, and the escape is the non-rationality of D(−√−k).

## Cheap numerics
See y10_poly_families_above (escaping families exist only for k < 0, where K is real and the sign at ∞ is free).

## Assessment
PROVED dictionary (elementary). For k > 0 it is empty in practice: Thm 2.2 shows no ES polynomial family has a
non-rational D(−√−k) — the positivity of the norm form of the *imaginary* quadratic field kills it. For k < 0
(K real) escaping families exist; whether they cover is the deep question (NEAR_SQUARE §3).
