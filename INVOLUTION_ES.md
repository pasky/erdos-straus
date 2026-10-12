# Involution / windmill route to Erdős–Straus: obstruction theorems (O158)

**Status: ES is not solved here.** This file is the depth follow-up of `BRAINSTORM/invol_windmill_signature.md`
(O152a), `invol_topological.md`, `invol_sign_identities.md` and `WINDMILL.md`. Labels as in DISCOVERIES.md.
Scripts: `scripts/inv_*`.

Notation. ES(n): `4/n = 1/x+1/y+1/z` has a positive solution. For a finite set `S` and an involution ι,
`|S| ≡ |Fix ι| (mod 2)`. A *windmill argument* for ES (WINDMILL Lemma 1) consists of finite sets `X(n)`,
involutions `σ_n, τ_n` of `X(n)` and a map `Φ_n : Fix τ_n → {ES certificates of n}`, with `|Fix σ_n|` odd;
then `|Fix τ_n|` is odd, so ES(n). The *O152 odd set* is

  `X(n) = {(t,u,v) ∈ ℤ³_{≥1} : tuv − u − v = n}` ⟺ `(tu−1)(tv−1) = tn+1`,

with `A = tu−1`, `B = tv−1`. Its *ES part* is `E(n) = {4 | A}`; by CONDITIONAL_ES Lemma 1.1 (with
`(g,f,c) = (t,u,v)`) every element of `E(n)` gives an explicit solution of 4/n (Type I, slice a = 1).
`ρ` denotes the swap `u ↔ v` (i.e. `A ↔ B`).

## 1. T1 for involution families (squares)

**Lemma 1.1 (PROVED, elementary).** Let `F` be a set of odd integers and suppose that for every `n ∈ F`
we are given `(X(n), τ_n, Φ_n)` as above with `Φ_n` taking values in a set `C(n)` of certificates that is
empty whenever n is an odd square (e.g. ET Type I/II solutions, ET Prop 1.6; or `E(n)`, Lemma 2.2 below).
Then `|X(m²)|` is even for every `m² ∈ F`. ∎ (`Fix τ_{m²} = ∅`.)

So a windmill *family* that is defined on a congruence class `n ≡ h (mod M)` with h a square class must
use sets with `|X(m²)|` even for all `m² ≡ h`; by Dirichlet such m² include `q²` for infinitely many primes
`q ≡ a (mod M)` (`a² ≡ h`).

## 2. The O152 set X(n) fails T1

**Lemma 2.1 (PROVED; O152 E4 extended to all n).** For every n ≥ 1, `|X(n)| ≡ #{(t,u) ∈ ℤ²_{≥1}: u(tu−2) = n} (mod 2)`.
*Proof.* ρ is an involution of X(n) with fixed points `u = v`, i.e. `tu² − 2u = n`. ∎

**Lemma 2.2 (PROVED).** If m is odd then `E(m²) = ∅`: there is no `(t,u,v) ∈ ℤ³_{≥1}` with
`tuv − u − v = m²` and `4 | tu − 1`.

*Proof.* Put `A = tu−1 = 4δ`. Then `A | tm²+1` and `t | A+1 = 4δ+1`, so t is odd and `gcd(t,δ)=1`.
From `4 | tm²+1` and `m² ≡ 1 (8)`: `t ≡ 3 (4)`; if δ is even then `8 | tm²+1`, so `t ≡ 7 (8)`.
Write `δ = 2^s δ₀`, δ₀ odd. Every prime `ℓ | δ₀` divides `tm²+1`, so `ℓ ∤ t` and `(−t/ℓ) = 1`; hence
the Jacobi symbol `(−t/δ₀) = 1`. On the other side, `4δ ≡ −1 (mod t)` gives `(δ/t) = (−1/t) = −1`, and
`(2/t) = 1` if s ≥ 1, so `(δ₀/t) = −1` (this already contradicts δ₀ = 1). By reciprocity, as
`(t−1)/2` is odd, `(t/δ₀) = (δ₀/t)(−1/δ₀) = −(−1/δ₀)`, hence `(−t/δ₀) = (−1/δ₀)(t/δ₀) = −1`.
Contradiction. ∎

(This is the a = 1 case of ET Prop 1.6, but proved for the parametric set, without ET's coprimality
convention.)

**Proposition 2.3 (PROVED).** For every odd prime q, `|X(q²)|` is odd and `E(q²) = ∅`. Consequently:
(i) for every n = q², every involution of X(q²) has a fixed point outside the ES part;
(ii) no family of involutions `τ_n` of `X(n)` with `Fix τ_n ⊆ E(n)`, of *any* description complexity, can be
defined on all n of a square class `h (mod M)` (it fails at `n = q²` for every prime `q` with `q² ≡ h`);
(iii) more generally, for odd n, `|X(n)| ≡ #{u | n : n/u ≡ −2 (mod u)}`, where u runs over unitary
divisors of n (for odd n, `u | n/u + 2` forces `gcd(u, n/u) = 1`); `u = 1` always contributes.

*Proof.* Lemma 2.1: `u | q²` and `u | q²/u + 2`; u = q fails (`q ∤ q+2`), u = q² fails (`q² ∤ 3`), u = 1
works (`t = q²+2`). So `|X(q²)| ≡ 1`. `E(q²) = ∅` by Lemma 2.2. (i), (ii) follow; (iii) is Lemma 2.1. ∎

So the O152 set has the right parity at primes for the *wrong* reason: its odd point `(n+2,1,1)` exists for
every n (a "periodic" fixed point), and nothing cancels it at squares. A windmill on X can therefore only
work if it uses the primality of p in its very definition, which rules out every uniformly defined
construction on a congruence class (in particular every piecewise-affine one whose pieces and maps do not
depend on n). §4 treats constructions defined on primes only.

EVIDENCE (`scripts/inv_x_squares.py 1500 90000`, 4 min): Lemma 2.1 checked for all odd n ≤ 1500; `E(m²) = ∅`
for all odd m ≤ 300; `|X(m²)|` odd for 137 of the 149 odd m in [3,300], and for every odd prime m there.
