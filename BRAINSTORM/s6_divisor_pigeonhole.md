# s6_divisor_pigeonhole — a deterministic cap-0 criterion at a forced window, and why it is linear (O238; mandatory (i))

## Idea
Cap 0 at window q is −1 ∈ Σ_q(K) = {d₁/d₂ : d₁, d₂ | K} (CAP_DOWN Lemma 3.1, δ_n = 0). Let P := {d mod q : d | K}.
**Prop (PROVED, pigeonhole).** If |P| > (q − 1)/2 then P ∩ (−P) ≠ ∅ (|P| + |−P| > q − 1), so d₁ ≡ −d₂ and cap 0 holds.
**Prop (PROVED, Cauchy–Davenport; sharpness).** Write (ℤ/q)^* = {±1} × U, |U| = u = (q−1)/2 odd. If the only QNR prime of K is
s₀ with exponent 1 and the other primes map to even exponents in log coordinates, the cap-0 condition is u − log s₀ ∈ the
signed subset-sum set of the remaining log-images in ℤ/u; for u prime this set has size ≥ min(u, 2N + 1) (N = total
multiplicity), sharp when all images are equal. Hence the forced bit plus any *structure-free* argument needs
Ω(K) ≳ q/4: linear in q, while Ω(K) ≤ log₂K. With q ≥ q*(n) ≳ log n (Burgess–Pollack lower range; under GRH q* ≤ C log²n)
this is satisfiable only for extremely smooth K: a lottery (B3 in additive-combinatorics form).
Weighted Davenport constants (±-weights: D_±(ℤ/n) = ⌊log₂n⌋ + 1) give zero-sums, i.e. the trivial relation 1 ∈ Σ, never the
target −1: the forced parity cannot be transported into the odd part by zero-sum theory.

## Literature
Cauchy–Davenport; Olson; Adhikari–Rath / Adhikari–Chen–Friedlander–Konyagin–Pappalardi on ±-weighted Davenport constants
(D_A(ℤ/n) with A = {±1}: ⌊log₂ n⌋ + 1); Erdős–Heilbronn / Dias da Silva–Hamidoune for distinct summands.

## Barrier screen
B2/B3: the criterion needs τ(K)-type size ≳ q; at the least forced window that is a coin (EVIDENCE below). B6 not invoked.
T1: at n = a² no window has a Lemma-1.1 solution, consistent: at squares K is a QR and P sits in a coset structure
with P ∩ −P = ∅ forced (CAP_DOWN §3).

## Cheap numerics
`scripts/s6_divisor_pigeonhole.py 200000`: 8 977 primes p ≡ 1 (4); at the least odd-K forced window the criterion fires for
4 870, cap 0 holds for 6 149 (no case with criterion true and cap 0 false — as proved).

## Assessment
PROVED criterion + PROVED sharpness of the structure-free version. Negative for (i): the forced bit lifts to cap 0 only
with a linear-in-q budget. EVIDENCE: criterion covers ≈ 54 % of primes at the least window (mostly q = 3, 7).
