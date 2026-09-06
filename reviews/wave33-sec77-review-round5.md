DEFECTIVE

Reviewed `9f02f7c0d713d3a0adfbde64be66d9dd2075800f`. Both substantive round-4 defects are repaired. One literal false statement remains in the wall-map: it omits the identity exception that the detailed theorem now correctly includes.

## Item status

1. **CRT — REPAIRED.** `notes.md:31213–31215` correctly describes the constraint imposed by the progression, not by primality. Writing `g = gcd(q,L)`, the congruences `p ≡ 1 (mod L)` and `p ≡ r (mod q)` are compatible exactly when `r ≡ 1 (mod g)`. This remains true for overlapping prime powers. Primality can impose additional restrictions, but those are not restrictions imposed by “the class.” Also, `−97 ≡ 1 (mod 7)` is correct.

2. **Fibre automorphisms and integrality — REPAIRED in Theorem 77.4(c), `notes.md:30853–30861`.** Put `a = px`. Every regular automorphism of the punctured projective line extends to its smooth projective completion and permutes the three deleted points. A Möbius transformation is uniquely determined by three distinct point images, and all six permutations exist. The displayed maps, in their stated order including identity and swap, induce the following permutations of the ordered punctures `(0,∞,−a)`:

       (0,∞,−a), (∞,0,−a), (−a,∞,0),
       (∞,−a,0), (−a,0,∞), (0,−a,∞).

   Thus they are exactly the six elements of `S_3`. The swap fixes `−a`, as required for the deleted point `y=z=0`.

   Substituting the other four images into `y′=(Y′+a)/q`, with `D′=a²/D` and `D+a=qm`, gives exactly

       −D/q, −D′/q, aD/(q²m), a²/(q²m).

   Since `DD′=a²` and `gcd(a,q)=1`, all four numerators are coprime to `q`. Here the section's standing assumption `p ≡ 1 (mod 4)` is important: `q=4x−p>0` implies `q ≡ 3 (mod 4)`, hence `q≥3`. Every displayed denominator retains a nontrivial factor from `q`, so none of these values is an integer. Identity and swap do carry solution points to integral points. The pointwise formulation no longer asserts a false uniqueness property for an empty integral subset.

3. **Wall-map item 1 — remaining LOW literal error.** `notes.md:31175–31176` says “only the swap carries solution points to integral points,” without “besides the identity.” The identity also does so. This is not an empty-fibre issue: for `p=5`, the allowed fibre `x=2` contains `(y,z)=(4,20)`, since `4/5=1/2+1/4+1/20`. Its identity automorphism carries that solution point to itself and is not the swap. The detailed theorem is correct, and the intended shorthand is evident, but the wall-map sentence as written is false. Insert “besides the identity” or say “only the identity and swap.” No mathematical change to the detailed proof is needed.

## Checks

- Read the round-4 review, the repaired consequences, the headline, and all of §77.7. Apart from the identity omission, no new false statement or newly mislabelled heuristic was found. The headline remains a scoped search outcome, not an impossibility theorem.
- SymPy verified all six puncture permutations and all four displayed coordinate identities exactly.
- Exhaustively enumerated all 257 unordered positive solutions for the 21 primes `p<200`, `p ≡ 1 (mod 4)`, using the smallest-denominator bound `p/4<x≤3p/4` and divisor enumeration. Permutation then covered all 854 ordered solution points with the fixed coordinate prime-free. All four nonintegrality checks and the swap check passed.
- Checked 625 complete CRT residue cycles, for `L=4,8,…,100` and `q=3,7,…,99`, and the `p=97,q=7` example.
- Scripts used `uv run --with sympy python`, a 60-second timeout and a 1,000,000-KiB virtual-memory cap. An initial symbolic harness run stopped on accidental Python floating-point division; exact SymPy coercion fixed the harness, and the complete rerun passed. No full-verifier run is claimed.

No source files were edited; only this review was added.
