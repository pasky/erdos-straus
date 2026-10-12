# Brainstorm O152(a): the "windmill signature" of a parity proof, and a test on all n

Status: **ES is not solved here.** Labels as in DISCOVERIES.md. Builds on `WINDMILL.md` (earlier wave,
all negative); this memo does not repeat its catalogue but adds (i) a precise statement of *why* a
parity proof escapes B1/B3/B5 and what single property it would still need, and (ii) a new test that uses
composite n (the earlier wave tested primes only).

## 1. Idea

**1.1 What a windmill proof actually proves.** Zagier: `S(n)={(x,y,z)∈ℤ³_{>0}: x²+4yz=n}`, the
windmill σ is piecewise in `O(x²+4yz)(ℤ)` and `τ:(x,y,z)↦(x,z,y)`. For *every* n (not only primes),

  `#{x²+4y²=n, x,y>0} ≡ #Fix τ ≡ |S(n)| ≡ #Fix σ = #{n=u·v: u<v, u≡v (mod 4)}  (mod 2)`   (Z)

(σ fixes exactly `x=y`, where `n=x(x+4z)`; squares `n=u²` contribute nothing since z>0). Primality is
used **only** in evaluating the right side: for `n=p≡1 (4)` it has exactly one term `1·p`.

General shape (folklore, elementary). If σ is piecewise integral-affine with pieces preserving a quadratic
Q, each piece's fixed set is an affine sublattice L on which Q restricts to a form of lower rank; on a
rank-2 piece this is a binary form `F_i`, so `#Fix σ = Σ_i r_{F_i}(n; congruence/positivity conditions)`.
If `F_i` has square discriminant (Zagier: `x(x+4z)`), `r_{F_i}(n)` is a **divisor-type** count
`D_φ(n)=Σ_{n=uv, u<v} φ(u mod M, v mod M)` (+ a square term). A windmill proof of a statement about
weighted ES counts `W(n)=Σ_{sol of 4/n} w(sol)` therefore has the form

  `W(n) ≡ D_φ(n)  (mod 2)  for all n in a congruence-defined family`,                (W)

and concludes `W(p)≥1` for primes p with `φ(1,p mod M)=1`.

**1.2 Why such a proof is not ruled out by the barrier map.**
* *B1 / Theorem C.* (W) is not a congruence covering and produces no polynomial identity family. The
  conclusion at a single prime p is `W(p) odd`, deduced from `D_φ(p)=φ(1,p)` — a statement that uses the
  **global factorisation** of p (p has exactly the factorisations 1·p, p·1). Theorem C's mechanism
  (square-mimicking primes: p agrees locally with an odd square m² modulo every witness modulus) does not
  apply, because `D_φ(p)` and `D_φ(m²)` differ although p ≡ m² locally: m² has the extra factorisations
  `ℓ·(m²/ℓ)`. Parity of a *global* divisor count is not a local invariant.
* *B5 (odd squares).* For Type I/II weights, `W(m²)=0`. (W) then only says `D_φ(m²)` is even — no
  contradiction. **The step that fails at n=m² is "D_φ(n) is odd"**, i.e. the evaluation of #Fix σ, which
  uses primality. So a windmill route passes T1 automatically, in a principled way.
* *B2/Theorem M (finite slice sets).* Zagier's σ moves between slices: it maps a factorisation
  `yz=(p−x²)/4` to a factorisation of `(p−x'²)/4` with x'≠x. A windmill is a **cross-slice coupling** of
  the per-slice divisor lotteries, using *all* ≍√p slices; Theorem M (fixed finite slice set) is irrelevant.
* *B3 (scale), B6 (average leak).* No main term; the statement is pointwise in p.

So the windmill route is a genuine gap in the barrier map. Its whole content is the existence of an
identity (W) with ES on the left. The earlier wave (WINDMILL §2.1) proved that no piece can preserve the
multilinear ES equation as an *integral affine map identically*, and found no weight w with `W(p)` odd for
all hard primes. Both leave open set-theoretic pieces and identities valid on primes only.

**1.3 New necessary condition, testable on composites.** If (W) holds for all n coprime to M (as every
Zagier-type identity does), then the parity vector `(W(n) mod 2)_{n≤X}` lies in the F₂-span of the
divisor-type vectors `D_{r,s}(n)=#{n=uv, u<v, u≡r, v≡s (M)}` and square vectors
`Q_r(n)=[n=u², u≡r (M)]`. Over all n this is a **strong** constraint (≈X equations, 2φ(M)²... unknowns),
much stronger than "W(p) odd for p in a class", which needs only ≈φ(M) unknowns. The test is GF(2) linear
algebra on the span of many candidate weights at once.
