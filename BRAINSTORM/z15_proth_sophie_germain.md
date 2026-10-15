# z15_proth_sophie_germain — ES for all 3·2^s + 1 through a proved ET-sterile point (O240) — SHARP

## Idea
EXPONENT_COVERING Cor 1.5: 3·2^s + 1 has NO finite covering by ET/divisor classes (μ = 0 is a profinite unit-square point).
Add Lemma-1.1 windows whose budget is forced by an algebraic factorisation that survives near μ = 0. Cyclotomic windows
need e | j and then m ≡ 7 (mod 8), which is dead at μ = 0 (Prop 4.1, Jacobi). The Sophie Germain identity
4X⁴ + 1 = (2X² + 2X + 1)(2X² − 2X + 1) at window j = 2, m = 11 survives: for X ≡ 4, 6 (mod 11), n = 48X⁴ + 1,
4/n = 1/(3(4X⁴+1)) + 11/(6n(2X²−2X+1)(X²+X+2)) + 11/(2n(4X⁴+1)(X²+X+2)) — covers s ≡ 0, 12 (mod 40), X = 2^{(s−4)/4}.
With other divisor exponents the same window covers all s ≡ 0 (4) except 4, 24 (mod 40) (the T1 points X = ±1, n = 49);
six ET/divisor classes (moduli 5, 7, 15, 61) do the rest: **ES for every 3·2^s + 1** (Theorem C).
## Literature
Sophie Germain identity a⁴ + 4b⁴; Aurifeuillean factorisations; Sierpiński-type coverings; EXPONENT_COVERING (J)22;
O238 (4^s + 105). ES for this Proth family is not known to us from the literature (not searched exhaustively).
## Barrier screen
B1/Thm 1.4: hypothesis "ET/divisor classes" (identities polynomial in n) is exactly what is violated — the class
{s ≡ 0 (40)} is the n-congruence class n ≡ 4 (2⁴⁰ − 1), n ≡ 1 (16), which contains odd squares; the identity is polynomial in
X = ((n−1)/48)^{1/4}. T1: the menu is dead exactly at the T1 points X = ±1 (n = 49). B2/B3/B6: thin family, nothing for primes.
## Cheap numerics
`scripts/z15_proth_identity.py` (symbolic + s ≤ 4000), `z15_cert_proth_make.py`, `z15_cert_proth_check.py
data/z15_cert_proth3_et.json 1500` (re-verifies all rules, classes, coverage mod 360, exact solutions s ≤ 1500; 2 s).
## Assessment
PROVED (computer-assisted). First instance in the campaign of a *proved* ET/divisor-sterile point dissolving under a richer
(exponential-window) menu. Scope: one thin family.
