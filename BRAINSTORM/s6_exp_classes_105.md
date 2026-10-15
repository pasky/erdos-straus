# s6_exp_classes_105 — exponential window classes close 4^s + 105 (O238; deep item, SYNTHESIS_SPARKS6 §1)

## Idea
Mandatory (ii)+(v): force the exponent budget of a window algebraically. On n_s = 4^s + k, the window m_j = 4^j − k has
x = K = 4^{j−1}(4^r + 1) (r = s − j): 2-budget 2j − 2 and the cyclotomic/Aurifeuillean factors G_e = 4^{r/e} + 1,
A± = 2^g ∓ 2^{(g+1)/2} + 1 (g = r/e odd) are forced for every s, and their residues mod m_j are periodic in r. A cap-0
relation 2^i·U ≡ −V (mod m_j) among them (CAP_DOWN Lemma 1.1, d = K·d₁/d₂) gives an *exponential class*: a congruence
condition on s whose ES solution has a divisor d growing with s — not a fixed-modulus ET class.

## Literature
EXPONENT_COVERING Thm 1.4 / (J)22 (covering ⟺ limit set avoids the sterile set, for ET + divisor classes with fixed
moduli); SIGN_FIELDS §1.4 ((J)62: k = 105 open, mixed points); Sierpiński-type coverings (Sierpiński 1960, Erdős covering
systems) for thin exponential families; algebraic factorisation of 2^{2r} + 1 (cyclotomic, Aurifeuille: 4x⁴ + 1 =
(2x² + 2x + 1)(2x² − 2x + 1)), standard (Brillhart et al., *Factorizations of bⁿ ± 1*, AMS 1988).

## Barrier screen
B1: the classes ARE congruences on s, but not on n: the fixed-modulus hypothesis of EXPONENT_COVERING Thm 1.4 is violated,
which is the whole point. The family is thin, so B1's Thm M (no covering for all n) is not in play. B2: the "divisor in a
class" is supplied by an algebraic identity (u + 1 | u³ + 1), a non-formal input available only on the family. B3/B6: no
counting. T1: the class contains no square (Lemma-1.1 T1, CAP_DOWN §3). Thm 9.1 / Prop 10.3: not applicable (finite
certificate).

## Cheap numerics
`scripts/s6_expwin105.py`, `s6_expclass.py` (≈ 85 % of s ≤ 300 cap-0 by exp + small-prime classes), `s6_expclass_pts.py`
((J)62's residual exponents 124 (360), 844 (2520) all hit by the (151, G₃) class), `s6_cover105.py` (exp + divisor classes
alone: 79 % of s mod 4 754 520), `s6_hybrid105.py` (z8 seed + exp classes: closes k = 105 at L = 360 with one class;
k = 33, 273, 297 stall), `s6_cert105_make.py` + `s6_cert105_check.py` (certificate and independent checker; exact to s = 1500).

## Assessment
**PROVED (computer-assisted): ES for all 4^s + 105** (SYNTHESIS_SPARKS6 Thm 1.1), via the identity on n = 256u³ + 105,
u ≡ 32 (mod 151). SHARP. Not a statement about primes; a precise demonstration that "sterile mixed points" are relative to
the class menu.
