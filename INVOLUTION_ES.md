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

## 3. Divisor-type fixed-point counts: what T1 forces

In a Zagier-type windmill the σ-fixed count is evaluated through binary forms of square discriminant on
the fixed loci (O152a §1.1), i.e. it is *divisor-type*. Fix a modulus M and a square class
`h ≡ a² (mod M)`, `gcd(a,M)=1`. Consider

  `D(n) = Σ_{uv=n, u<v} φ(u mod M, v mod M) + [n = u²]·ψ(u mod M) + c(n mod M)   (mod 2)`,        (D)

with arbitrary `φ, ψ, c` (values in 𝔽₂). This covers divisor counts restricted by congruences mod M and by
finitely many homogeneous cones `λu < v` (see the proof), square loci (Zagier's boundary correction) and
isolated "periodic" fixed points (the `(1,1,(n−1)/4)` of Zagier, the `(n+2,1,1)` of X(n)).

**Proposition 3.1 (PROVED).** Suppose `D(m²) ≡ 0` for every odd m with `m² ≡ h (mod M)` (Lemma 1.1 forces
this when D is the σ-fixed count of a windmill family on the class h whose τ-fixed points are certificates
that do not exist at odd squares). Then `φ(1,h) = 0`; hence `D(p) = c(h)` for every prime `p ≡ h`, and
`ψ(a') = c(h)` for every `a'` with `a'² ≡ h`. In particular, if `D(p)` is odd then `c(h) = 1` and `ψ(a') = 1`.

So *the odd fixed point at primes can never come from the divisor part `1·p`* (as it does in Zagier's proof,
where the fixed point `(1,1,(p−1)/4)` is the factorisation `p = 1·(1+4z)`); it must be a periodic point
present for every n of the class, and then the fixed locus must contain a square-detecting piece that cancels
it at every m². (For X(n) the periodic point is `(n+2,1,1)` and the square piece is missing: Prop 2.3.)

*Proof.* `D(p) = φ(1,h) + c(h)`. Choose primes `q_1 < q_2 < …`, prime to M, in prescribed classes, with
`q_j > ∏_{i<j} q_i^{2e_i}` (Dirichlet). For `m = ∏ q_i^{e_i}` and `d | m²`, `d ≠ m`, the comparison
`d < m²/d` is decided by the largest index where the exponents of d and m²/d differ (that `q_j^{±1}`
dominates the rest). [The same holds for any fixed cone `λd < m²/d` once the q_j are large compared with
λ^{±1}; the diagonal `d = m` is the ψ-term, so finitely many cones only change ψ.] Write `ā = a⁻¹`, and
`φ_r := φ(a^r, a^{2−r})`, `ψ := ψ(a)`. The patterns (classes; exponents)

| pattern | m | expansion of `D(m²) − c(h)` |
|---|---|---|
| P1 | `q₁²q₂³`, `q₁≡ā, q₂≡a` | `φ₀+φ₃+φ₋₁+φ₋₂+φ₋₄+ψ` |
| P2 | `q₁q₂`, `q₁≡ā, q₂≡a²` | `φ₀+φ₂+φ₋₁+φ₋₂+ψ` |
| P3 | `q₁q₂`, `q₁≡1, q₂≡a` | `φ₀+φ₁+ψ` |
| P4 | `q₁²q₂q₃`, `q₁≡ā, q₂≡a, q₃≡a²` | `φ₁+φ₂+φ₃+φ₋₄+ψ` |

all have `m ≡ a`, `m² ≡ h`. (E.g. P3: the smaller member of each pair `{d, m²/d}` is `1, q₁, q₁²` (residue 1,
giving `3φ₀`) and `q₂` (pair `(q₂, q₁²q₂)`, giving `φ₁`).) The four expansions sum to `φ₀ = φ(1,h)` mod 2, so
`0 = Σ D(m_i²) = φ(1,h) + 4c(h) = φ(1,h)`. Then `D(p) = c(h)`, and `m = q ≡ a'` gives
`0 = D(q²) = φ(1,h) + ψ(a') + c(h)`. ∎

The rows are computed in the *free model* (`a` of infinite order; `scripts/inv_t1_free.py 3 3 -1 2` finds this
certificate); specialising to an actual `(M, a)` only identifies variables, so the cancellation persists for
every M and every unit a. Independent check on actual integers (actual primes with the size condition,
divisors enumerated, all variables cancel): `scripts/inv_t1_cert_check.py M a` for
`(M,a) = (840,11), (24,5), (120,7), (1,1), (7,3)`. In the free model restricted to residues `{1, a}` no
certificate exists (`inv_t1_free.py 3 2 0 1`): the classes `ā, a²` are needed.

**Remark 3.2 (what this does and does not exclude).** Prop 3.1 does **not** exclude divisor-type windmills:
`D(n) = 1 + [n = □]` (`c = 1`, `ψ = 1`, `φ = 0`) satisfies all T1 constraints. What it shows is the *shape*
any T1-compatible windmill must have: a periodic odd fixed point plus a fixed piece that sees exactly the
squares. Neither ingredient uses more about p than "p is not a square", so all the content of such a
windmill sits in the identity `W ≡ D (mod 2)` at composite non-squares of the class, about which T1 says
nothing. T1 alone is therefore no barrier to the windmill route; a barrier must come from the structure of
the maps (§4).
