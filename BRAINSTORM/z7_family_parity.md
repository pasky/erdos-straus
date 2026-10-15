# z7_family_parity — parity across a family of words sharing a side: the Flip Lemma and its collapse to B2 (O231, goal 2)

## Idea
Bridge U ≥ 1 ⇒ N₋ ≥ 1 by a parity argument across a *family*: words sharing a side value X ∈ {t, u, v}. On the
X-family, words ↔ divisors D ≡ −1 (mod X) of N_X, and χ = ψ(D) (UNFORCED_WORDS Lemma 2.2). If ψ is non-constant on
that class, the family has a certificate.

## Results
* **Flip Lemma 2.2 (PROVED).** The X-family contains a certificate ⟺ (−1, −1) ∈ image of
  Div(N_X) → (ℤ/X)^× × {±1}. Sufficient conditions:
  * a ψ-odd prime r ∥ N_X with r ≡ 1 (mod X);
  * or a matched swap r ∥ D, s ∥ N_X/D with r ≡ s (mod X) and ψ(r) ≠ ψ(s).
* Numerics (primes ≡ 1 (8) < 2·10⁵, 94 262 non-certificate unforced words):
  * 73 % are flippable;
  * 96 % have a certificate in one of their three families;
  * flippable but no family certificate: 0.
* **Collapse (Remark 4.1, PROVED, tautological).** With family-exact forcing ("the family has no certificate") in place
  of cleanliness, "unforced in all three directions" ⟺ "each of its families contains a certificate". So U_fam ≥ 1 ⟺
  N₋ ≥ 1. Every sharpening of the forcing notion moves U toward ES-five. The gap U → N₋ is exactly the words whose three
  families are certificate-free for non-clean reasons. Examples: R227 D18's congruence-pinned sides, and defective sides
  r²·clean.
* Lemma 5.2 (PROVED): on an automatic family the certificate count is (τ/2)(1 − ∏_{ψ(r)=−1}[e_r even]/(e_r+1)).

## Literature
* Subset-product images in (ℤ/X)^× × {±1}: zero-sum theory (Davenport constant; Olson, J. Number Theory 1 (1969)).
  It forces the image only when ω(N_X) ≳ D(G) ≈ X, never the case for large X.
* E-slice form: CONDITIONAL_ES / redteam-automorphic-2 (−1 ∈ Σ_e(N)).

## Barrier screen
* B2 verbatim: the flip needs a ψ-odd prime in a class mod X, with X part of the word.
* B4: the image filling by many small primes is a pigeonhole on small factors (LONGSHOT_PIGEONHOLE).
* T1: at squares ψ ≡ 1, no flip.
* B6: the 96 % is an average.

## Cheap numerics
`scripts/z7_flip.py 9 200000`.

## Assessment
PROVED lemma + EVIDENCE. Goal (2) answered negatively with exact scope: parity across a family *is* the e-slice
divisor-class condition. There is no deterministic bridge from U to N₋ beyond the automatic families (where it is
Prop F).
