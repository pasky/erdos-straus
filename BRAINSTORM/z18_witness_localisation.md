# z18_witness_localisation — the μ = 0 witness condition is a parity over the primes of Res(f, φ) (O245)

## Idea
Theorem A's computation at μ = 0 gives, for any root family with witness polynomial f (Type II: f = 4acd − 1),
(f(Y)/n(Y)) = W(f) := Π_{v|2}(f(θ), θ(θ − 1))_v for Y near μ = 0; the family needs W(f) = −1. Push this through the
product formula for (α, β), α = f(θ), β = θ(θ − 1).
## Result (PROVED; MENU_LADDER §3)
If k = 1 and c₀ is odd squarefree (e.g. c₀ = 3, 15, 63 is not squarefree — 63 = 9·7 excluded), 1/θ is Eisenstein at every
q | c₀, ϖ = 1/θ, β = ϖ^{−2}(1 − ϖ) ≡ ϖ^{−2}·1, so every tame symbol (α, β)_𝔮, 𝔮 | c₀, is 1; real places contribute 1
(β > 0 at the negative real root). Hence
  W(f) = Π_{v ∤ 2c₀} ((θ(θ − 1) mod v)/v)^{v(f(θ))},
a parity count over the prime ideals dividing f(θ) (i.e. the primes of Res(f, φ) and of the denominators of f) at which
θ(θ − 1) is a non-residue. For a degree-one prime (p, y₀) (φ(y₀) ≡ 0 mod p) the factor is the Legendre symbol
(y₀(y₀ − 1)/p).
## Literature
Tame symbol and Hilbert reciprocity: J. Neukirch, *Algebraic Number Theory*, V.3; MENU_STERILITY Theorem A.
## Barrier screen
This is a refinement of Theorem A, a necessary condition only. It shows the condition is cheap to satisfy (a random f has
W = ±1 with probability ≈ 1/2): the witness/descent level is NOT the bottleneck at μ = 0 for 15·2^s + 1.
## Cheap numerics
`scripts/z18_witness2.py 3 1 4 '(3/11)*(Y^2+2*Y+8)*(Y^2-2*Y+2)-1'` (O240 Theorem B's witness): W = −1, 2-part −1, c₀-part +1,
other odd −1 ✓ (product formula). Changing the sign of the constant gives W = +1.
## Assessment
PROVED. A computable filter for candidate shapes; confirms that sterility, if any, is global-algebraic + archimedean.
