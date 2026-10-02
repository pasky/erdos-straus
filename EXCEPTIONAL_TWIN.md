# EXCEPTIONAL_TWIN — (E_δ), the heavy coordinates, and η-twin windows (task O1)

Status: **in progress.** Labels follow `DISCOVERIES.md`. PROVED means proved
here and checked internally only. Notation follows `EXCEPTIONAL_THETA.md`
(ET) and `EXCEPTIONAL_BALANCED.md` (EB).

## 0. Status at a glance

| item | statement | label |
|---|---|---|
| Lemma 1.1 | every Case-B class `−4D (mod M)` has Jacobi symbol `(−4D \| M) = −1` | PROVED (classical; Mordell) |
| Cor 1.2 | an n that is a nonzero square mod every prime of M avoids every class of ℛ(M) | PROVED |
| Lemma 1.3 | QR base: a product measure on small residues, supported on avoiders of all W-smooth classes, inflation `2p/(p−1)` per prime | PROVED |

## 1. The quadratic-residue base (Mordell obstruction, used constructively)

### 1.1 Forced classes are Jacobi non-residues

**Lemma 1.1 (PROVED; classical, Mordell).** Let `M ≡ 3 (mod 4)`,
`A = (M+1)/4`, and `D | A²`. Then `gcd(D, M) = 1` and the Jacobi symbol
satisfies `(−4D | M) = −1`.

*Proof.* `gcd(A, M) = gcd(A, 4A−1) = 1`, so `gcd(D, M) = 1`. Write
`D = s r²` with s squarefree. Then `g(D) = s r`, and `D | A²` iff
`sr | A` (EB Lemma 4.1). So `4s | M+1`, i.e. `M ≡ −1 (mod 4s)`. Now
`(−4D|M) = (−1|M)(2|M)²(r|M)²(s|M) = −(s|M)`, because `M ≡ 3 (mod 4)`.
* If s is odd: reciprocity gives `(s|M) = (M|s)(−1)^{((s−1)/2)((M−1)/2)}`.
  Here `(M|s) = (−1|s) = (−1)^{(s−1)/2}` and `(M−1)/2` is odd. So
  `(s|M) = 1`.
* If s is even, `s = 2s'` with s' odd: `8 | M+1`, so `(2|M) = 1`, and
  `(s'|M) = 1` as before (`M ≡ −1 (mod 4s')`).

Hence `(−4D|M) = −1`. ∎

Check: `scripts/twin_jacobi_check.py` verifies the statement for all
159,390 classes with `M ≤ 20000`.

**Corollary 1.2 (PROVED).** Let n be an integer that is a nonzero quadratic
residue modulo every prime p | M. Then n lies in no class of ℛ(M).

*Proof.* `(n|M) = Π_{p^e ∥ M} (n|p)^e = 1 ≠ −1 = (−4D|M)`. ∎

This is the classical obstruction (Mordell; Schinzel; Elsholtz–Tao's
"odd-square" remark): polynomial ES identities never cover squares. Here it
is used in the opposite direction, as a cheap way to build measures that
live on avoiders.

### 1.2 The QR base

Fix `W ≥ 3`. Let `Q₀` be a common multiple of the W-smooth parts of all
moduli of the family, with `P_W | Q₀`. Put

    R_W = { c mod Q₀ : (c|p) = 1 for every odd prime p ≤ W }.

**Lemma 1.3 (QR base; PROVED).**
1. Every `c ∈ R_W` avoids every class of ℛ(M) whose modulus M is W-smooth.
   More generally, if `n mod Q₀ ∈ R_W`, the Jacobi factor `(n|q_s)` equals 1
   for every W-smooth odd `q_s`.
2. `log(Q₀/|R_W|) = Σ_{3≤p≤W} log(2p/(p−1)) = π(W) log 2 + O(log log W)`.
3. Under the uniform measure on `R_W`, the residues `c mod p^{e}` for
   distinct primes p are independent, and for every `a` and `p^e ∥ Q₀`,

       P(c ≡ a (mod p^e)) ≤ γ(p)/p^e,    γ(p) = 2p/(p−1) (p odd),  γ(2) = 1.

*Proof.* (1) Corollary 1.2, since every prime of M is ≤ W. The Jacobi factor
`(n|q_s)` depends only on n modulo the primes of `q_s`.
(2) By CRT, `R_W` is a product over the prime-power factors of Q₀. For odd
`p ≤ W` with `p^e ∥ Q₀` the factor has `p^{e−1}(p−1)/2` elements out of
`p^e`. (3) The product structure gives independence. A single residue
`a mod p^e` has probability `≤ 1/(p^{e−1}(p−1)/2) = (2p/(p−1))/p^e`. ∎

So the QR base is a **product** measure. This is the point: the base
inflation in every later estimate is the multiplicative weight γ, whose
Euler product over `p ≤ W` is `Π(1 + γ(p)/(p−1)) ≍ (log W)^{O(1)}`. The
uniform measure on the exact small-avoider set (ET Cor 3.6) has inflation
`≤ L' = e^{O(W^{1+C})}` instead, with no product structure.
