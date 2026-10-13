# bsH_twisted_targets — ES_q^c: A/P = c₁/X + c₂/Y + c₃/Z restores an order-m reciprocity; m-th powers lose degree classes, never all (O181; "never all" is EVIDENCE, R181 repair D6)

**ES is not solved here.** Deep version: DRINFELD_ES.md §3. Script `scripts/bsH_twisted.py`.

## Idea
Construction-first: Thm 2.2 of DRINFELD_ES uses the ES target only via x ≡ −1 and the sign at ∞. Twist the target
by constants c_i of order m in F_q^*/F_q^{*m} (the denominators keep monic normalisation) and see whether the
order-m engine produces a T1_m (m-th powers sterile).
## Literature
As bsH_bl_order_q1; Hayes, *Explicit class field theory in global function fields* (1979) for sign functions.
## Statement (PROVED)
Finite places ≠ Q: 2-torsion (unchanged). ∞: odd part = class of c₁^{deg X₂−deg X₃}(c₃/c₂)^{deg A + deg X₁ − n} — a
degree character. At P = Q^m, Type I/II-shaped solutions have inv_Q = 0, hence must lie in degree classes where the
∞-character is trivial (Thm 3.3).
(R181 repair D3: the ∞-formula needs a denominator of degree > n − deg A, which always exists — Q^e divides some
X_i; so the case c₁ + c₂ + c₃ = 1 is no exception and the corresponding spark is vacuous.)
## Barrier screen
T1: a genuine order-3 analogue, but only on degree classes (non-primitive solutions inherited from Q exist anyway).
B1: the restriction is a congruence on degrees — finite data. No existence content.
## Cheap numerics (EVIDENCE)
q = 7, m = 3, c ∈ {(1,1,2), (1,2,4), (1,1,4)}: at primes inv_Q ∈ {0,1,2} all occur (e.g. 402/431/431 Type I); at
cubes all Type I/II solutions have inv = 0 (82 + 30, 18 + 17), others carry all values; Lemma 3.2 formula matches
on 4 074 solutions (R181: re-checked on 20 464 (point, labelling) pairs, 0 mismatches; that m-th powers never lose
*all* solutions is EVIDENCE only, R181 repair D6).
## Assessment
Positive as a *dictionary*: an order-m T1 exists over F_q(T) and behaves exactly as predicted; it is partial
because F_∞^*/U₁ has a free degree coordinate that no positivity can pin. Promise 1–2 (clean model of "what T1
needs"); no ES route.
