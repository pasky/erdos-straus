# z17_perkey — siblings as divisors in one residue class (function-field Lenstra per key) (O242)

## Idea
The sibling conjecture is an upper bound (≤ 2 balls of one level per alive parent). Upper bounds for divisors in a residue
class of large modulus are provable with bounded multiplicity (SP Lemma 1.4: ≤ 2 over F_q[T] when 3 deg Q > deg F). Organise
the balls in a parent V as divisors E of one polynomial in one class: for a fixed key (m', g', s, a), E | 1 + T^s m'g'² and
E ≡ σ (mod T^N m'g'), and 3(N + z + y) > s + z + 2y always — so ≤ 2 balls per key and parent (SIBLING Lemma 1.1). Over ℤ:
≤ 6 P-boxes per key (c, d) and class (Lemma 1.2).

## Literature
Lenstra 1984 (divisors in residue classes), Coppersmith–Howgrave-Graham–Nagaraj 2008; FF versions SP Lemmas 1.4, 1.5.

## Barrier screen
B2: the keys are part of the solution; the reduction leaves "few keys per parent", a divisor-in-class problem with moving
modulus. Data: no sibling pair at q = 3 (14 pairs, depth ≤ 9) shares a key.

## Cheap numerics
`scripts/z17_ffsibkeys.py`, `data/z17/ffsibkeys_d9.txt`.

## Assessment
PROVED lemmas, but they bound the wrong quantity (multiplicity per key, not per parent). Dead end for a proof; useful as a
normal form: a counterexample to the sibling conjecture needs ≥ 2 keys (q = 3) / ≥ 3 keys (r = 17).
