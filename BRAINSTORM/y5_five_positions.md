# y5_five_positions — where B2 re-enters when o is chosen free (O213, brief item (a))

## Idea
O210 spark 2 asked for families of words at N ≡ 1 (8) whose opposite vertex o runs over primes in a progression
independent of N. For such families "o ≡ 7 (8)" would be a Dirichlet condition of density 1/2. The pentagon has five
positions for o, and up to the reversal (c, m, s) ↦ (s, m, c) there are three. For each, write down the remaining
condition on N.

By the mod-2 rigidity (FRIEZE Lemma 1.1), the parity pattern of (c, m) fixes the position:
* c, m both even: edge {c, m}, o = h;
* c even, m odd: edge {h′, c}, o = s (mirror of P_c);
* c odd, m even: edge {m, s}, o = h′ (mirror of P_h);
* c, m both odd, s even: edge {s, h}, o = c;
* c, m, s all odd: edge {h, h′}, o = m.

Throughout, N ≡ 1 (8) and o ≡ 3 (4) (memo y5_transport_is_ptolemy), and the word is a certificate ⟺ o ≡ 7 (8).

**P_h (o = h, the Mordell position).** c, m even with cm = o + 1, and o | N + c, s = (N + c)/o.
* The factorisation event is on the SMALL number o + 1. N enters only through the congruence N ≡ −c (mod o).
* Prop 1 (PROVED). For fixed odd o, the words in P_h at N are in bijection with
  C(o) ∩ {N mod o}, where C(o) = {−c mod o : c | o + 1, c and (o+1)/c even}.
  (R211 repair: so there is at most one such word per o, and it also needs s = (N + c)/o ≥ 1 (≥ 2 interior);
  |C(o)| = τ((o+1)/4) when 4 | o + 1.)
  All of them are certificates iff o ≡ 7 (8).
* Moreover (N/o) = (h/N) = (h′/N) for N ≡ 1 (4): Jacobi reciprocity and hh′ ≡ 1 (N).
  So C(o) ⊂ {Jacobi non-residues mod o} when o ≡ 7 (8). Directly: (−c/o) = −(2/o)^{v₂(c)}(c′/o) and
  (c′/o) = (−1/c′)² = 1, since o ≡ −1 (c′).
* **This is the family spark 2 asked for:** o runs over a progression independent of N and the condition on N is a
  congruence mod o. But its density is |C(o)|/o ≤ τ(o+1)/o, not 1/2. The (2/o) factor is automatic in it, and the
  missing factor is "N mod o lands in the divisor image −D(o+1)".
* For o = q prime: |C(q)| ≤ τ(q+1), against (q−1)/2 non-residues. (R211 repair of "Equality holds only for q = 7": there is no
  equality — C(7) = {3, 5} has 2 of the 3 non-residues; the class 6 comes from the words (1, 8, s) and (8, 1, s), whose
  o is h′ = 8s − 1 resp. s, not 7.) Then C(7) ∪ {6} is Mordell's 7-class, which is (J)33 §3.1.

**P_c (o = c, the Type II position).** c = o, sh = N + o, h = om − 1, h and s even.
* With o free and small, the condition is "N + o has a divisor h ≡ −1 (mod o) with h and (N+o)/h even". That is the
  Type II e-slice divisor event with e = o: B2 in full.
* Read with h small instead, it is the congruence N ≡ −o (mod h). This is again a Mordell class, now with modulus h
  and residue −o, where o | h + 1.

**P_m (o = m, the Type I position).** hh′ = 1 + oN, h ≡ h′ ≡ −1 (mod o), both even. This is the Type I shape
ff′ = 1 + 4c²dp. B2 again.

**Unified (PROVED, trivial).** Every word is the single relation sh = N + c with h = cm − 1, i.e.
"N ≡ −c (mod h), c | h + 1". The five positions are the parity patterns of this one relation. Choosing which
cluster variable plays o only decides which number carries the factorisation event: N + o, 1 + oN, or o + 1. The last
is N-free, and there N appears through a congruence modulo o itself.

**T1 per position (PROVED).**
* P_h needs (N/o) = −1. That is impossible at N = n² because gcd(n, o) = 1: a prime ℓ | o, n would divide c | o + 1.
* P_c and P_m: (h′/N) = −1 is impossible at squares because gcd(h′, N) = 1 (hh′ = 1 + Nm).
* At squares all three positions die by the same Jacobi symbol. No position is T1-free, as expected.

## Literature
* Mordell's classes and their congruence identities: Mordell, *Diophantine Equations* (1969), §30.
* Covering by Mordell/ET classes fails: Yamamoto (1965); ET Prop 1.6 / POINTWISE_SIZE Thm M; (J)26 (sterile points
  for all large least-QNR r).

## Barrier screen
* P_h with a fixed finite set of o: B1. The union of C(o) is a finite congruence covering, which misses the sterile
  points of (J)26 and all locally square primes.
* P_h with o growing: a covering by growing moduli. This is H-A, phrased as "N lies in −D(o+1) mod o for some
  o ≤ Y". The heuristic count is Σ_{o≤Y, o≡7(8)} |C(o)|/o ≍ log²Y, so there is no B3 obstruction at the main-term level.
  The barrier is pointwise (B6): no equidistribution of N mod o in thin sets at a single N.
* P_c and P_m: B2 directly.
* T1: all positions are T1-killed by one Jacobi symbol, consistent with B5.

## Cheap numerics
`scripts/y5_ocensus.c` implements the three position tests (P_s, P_h′ are mirrors), with the T1 control: all 499 odd
squares ≤ 10⁶ have no certificate with o ≤ 3000 (logs/y5_ocensus.txt). Position statistics: memo
y5_ocensus_hard_primes.

## Assessment
PROVED dictionary, negative for spark 2. The progression-in-o family exists, namely P_h. In it the sign is free
(automatic for o ≡ 7 (8)), and existence is a thin congruence (Mordell class) mod o. The divisor event has moved from
N to o + 1, which is cheap, but the price is a density-τ(o+1)/o congruence on N mod o, i.e. B1/H-A. No density-1/2
family exists in any position: in P_c/P_m the existence condition is a divisor event, and in P_h it is a congruence
of density ≤ τ(o+1)/o.
