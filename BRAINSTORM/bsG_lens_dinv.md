# bsG_lens_dinv — (W) in 4-manifold language: lens spaces bounding 3-vertex plumbings; Dedekind sums see Σ letters, not length (O180)

## Idea
(W)(n) ⟺ some lens space L(n,q) is the boundary of a negative-definite linear plumbing of three spheres with weights −x, −y, −z ≤ −2
(the canonical/minimal resolution plumbing of the cyclic quotient singularity 1/n(1,q) has exactly 3 curves). Do the standard invariants
(d-invariants, Casson–Walker, Rokhlin/Wu, Donaldson diagonalisation) detect this "b₂ = 3" property?

## Findings
* **Hirzebruch–Zagier/Myerson (checked):** for n/q = [[b₁,…,b_r]], 12 s(q,n) = (q + q*)/n + Σ(b_i − 3), with q q* ≡ 1 (n).
  So the Casson–Walker invariant (∝ s(q,n)), and the d-invariants (which are Dedekind-sum-type rationals by the Ozsváth–Szabó recursion), see
  Σ b_i but not r. For r = 3: x + y + z = 12 s(q,n) − (q+q*)/n + 9 and xyz − x − z = n. (`scripts/bsG_dedekind_hj.py`: 4 353 pairs n < 120, 0 failures.)
* r itself is the popcount of ?(q/n) (bsA_minkowski_stern M1). It is a *combinatorial* invariant of the plumbing, not a Floer-theoretic one: every
  L(n,q) bounds its canonical plumbing (sharp in the Ozsváth–Szabó sense), whatever r is.
* Donaldson/Greene-type lattice-embedding obstructions constrain *other* fillings (rational balls, definite fillings of small b₂ for *all* q at once).
  Their positive direction ("some q works") is exactly the counting statement (W).
* Wu/Rokhlin sign (bsA_wu_rokhlin_sign): sign layer only, irrelevant to (W) (sign-free).

## Literature
Hirzebruch–Zagier (1974), Myerson (1987) for the Dedekind-sum/HJ formula (from memory, verified numerically). Ozsváth–Szabó, *Absolutely graded
Floer homologies* (2003), d-invariant recursion for lens spaces. Owens–Strle, definite fillings and d-invariants. Lisca (2007), lens spaces bounding
rational balls.

## Barrier screen
All invariants considered are functions of the class of q; the existence quantifier over q is the class layer (B2). Floer invariants are blind to r.

## Assessment
Dictionary (PROVED identity, classical). No topological theorem bears on the existence of a length-3 q. Promise 0.
