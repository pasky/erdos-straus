# y5_transport_is_ptolemy — the transport law is the Ptolemy relation mod 8 (O213)

## Idea
O210's transport law says that for N ≡ 1 (8), (h′/N) = −(2/o), where o is the odd cluster variable opposite the even
edge {e, e′}. The question was whether the character of 2 at the small modulus o is a better-behaved quantity than
(A/N). This memo shows that the law has no content beyond Thm 1.2 of FRIEZE_ES. It is the Ptolemy relation through
the even edge, read mod 8.

**Lemma 1 (PROVED, one line).** In the pentagon frieze (q₁, …, q₅) = (h′, c, m, s, h), with frozen sides
(1, 1, 1, 1, N), the product of an adjacent pair is "frozen + frozen·opposite":
* {h′, c}: h′c = N + s (o = s);
* {c, m}: cm = 1 + h (o = h);
* {m, s}: ms = 1 + h′ (o = h′);
* {s, h}: sh = N + c (o = c);
* {h, h′}: hh′ = 1 + Nm (o = m).

So ee′ ∈ {1 + o, N + o, 1 + No}, and mod 8, ee′ ≡ 1 + N^ε o with ε = 1 iff the relation contains N
(N + o ≡ N(1 + No) and N² ≡ 1 (mod 8)). (Read off from (P) of FRIEZE_ES; each relation is the definition
h = cm − 1, h′ = ms − 1, or N = cms − c − s.)

**Corollary 2 (PROVED).** For odd N and the unique even edge {e, e′}:
1. 4 | ee′, hence o ≡ −N^ε (mod 4).
2. 8 | ee′ ⟺ o ≡ −N^ε (mod 8).
3. With Thm 1.2, (h′/N) = (−1/N)·(−1)^{[oN^ε ≡ 7 (8)]} = −(−1/N)(2/o)(2/N)^ε.

The last equality holds because oN^ε ≡ 3 (mod 4), and for such x, (2/x) = +1 ⟺ x ≡ 7 (8). Item 3 is FRIEZE §2,
including the extra (2/N) factor when the relation through o contains N. For N ≡ 1 (8):

* o ≡ 3 (mod 4) for **every** word (not only certificates);
* the word is a five-slice certificate ⟺ o ≡ 7 (mod 8) ⟺ 8 | ee′ ⟺ one of e, e′ is ≡ 0 (mod 4).

So "−(2/o)" is a relabelling of "o mod 8". o mod 8 is congruent to ee′ − 1 mod 8, i.e. it is the 2-adic depth of the
even edge again. The "character of 2 at a small modulus" is the residue class of o mod 8, not a Legendre symbol
carrying arithmetic information about N.

## Literature
* Ptolemy/exchange relations of A₂ friezes: Conway–Coxeter (1973); Fomin–Zelevinsky cluster algebras of type A₂
  (pentagon recurrence).
* FRIEZE_ES §1–2 (O210).

## Barrier screen
Nothing to screen: this is a reduction of a claimed mechanism to an identity. Consequence for the relay: Spark 2 of
O210 ("Chebotarev in the o-aspect") cannot gain from (2/o) itself, because o mod 8 already *is* the slice condition.
Any gain must come from how o is constrained by the *rest* of the word (memo y5_five_positions).

## Cheap numerics
`scripts/y5_ptolemy_check.py X` checks Lemma 1 (exact, not just mod 8) and Cor 2(3) on all formal words with odd
N ≤ X, in all N mod 8 classes. X = 20000: 784 732 words, 0 failures (CERTIFIED).

## Assessment
PROVED and near-tautological. This is a sharp *negative* reading of O210 SHARP 2. The transport law is Thm 1.2 plus
one Ptolemy relation. "Find a word with (2/o) = +1" is literally "find a word one of whose cluster variables is
≡ 0 (mod 4)", i.e. the five DK slices.
