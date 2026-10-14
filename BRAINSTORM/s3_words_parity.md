# s3_words_parity — (J)33 χ = −ε₂ (σ-invariance) × (J)15/(J)20 words × Zagier-type parity (E2: involutions)

**Combines:** (J)15 (W) words tuv − u − v = n, (J)32/(J)33 (S₄ = {χ = −1}; χ is a rational-class invariant, no classical
move flips it), and the parity/involution mechanism (Zagier's one-sentence proof) as an (E2) candidate.

## Idea
X(n) = positive words. σ: (t,u,v) ↦ (t,v,u) has the unique fixed point (n+2, 1, 1) (u = v forces u | n, u = 1), so
|X(n)| is odd for n > 3 (PROVED). χ is σ-invariant (AA* = tn + 1 ≡ 1 mod n). If a second involution existed whose
fixed points are controlled, parity could force a χ = −1 word (a finite-search existence mechanism).

## Literature
Zagier, *A one-sentence proof that every prime p ≡ 1 (mod 4) is a sum of two squares* (Amer. Math. Monthly 1990);
WINDMILL_REDUCTION / INVOLUTION_ES ((J)2, (J)5) for the campaign's earlier involution screens.

## Barrier screen
For p ≡ 1 (mod 4) the fixed word has χ = (−(p+1)/p) = +1, so #{χ = −1 words} is EVEN (σ pairs them): σ alone forces
nothing. A χ-flipping second involution is excluded among lattice/algebraic moves ((J)33 Cor 1.4). T1: at squares the
χ = −1 count is 0, so any parity argument must count a set whose parity differs between primes and squares.

## Cheap numerics (`scripts/s3_words_parity.py 20000`, 3 s)
Parity of the number of χ = −1 σ-orbits, primes 5 ≤ p < 20000, split by p mod 8: in every class the two parities
occur with frequencies 272:284, 260:310, 272:297, 275:290 (≈ uniform); the parity of the total orbit count is
likewise uniform. Odd squares 9 ≤ m² < 20000: 0 χ = −1 orbits (T1).

## Assessment
EVIDENCE negative: no parity law on χ = −1 orbits; an involution route would need a non-classical, χ-flipping move on
a non-obvious subset. Collapses into the (J)2 / (J)33 findings. Promise 0.
