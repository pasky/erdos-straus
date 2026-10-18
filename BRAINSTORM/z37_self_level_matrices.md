# z37 — ES words are self-levelled SL₂(ℤ) matrices; the (A)3 slice is RS's Ψ with the coset flipped (O267)

## Idea
Put ES's length-3 words in RS's matrix language and see which part of RS survives.

## Literature
DEDEKIND_ES Lemma 1.1, Thm 4.5; RS Lemma 3.1, Prop 2.2; R276 (row 2 of ZAREMBA §5.2 exact).

## Content (QUESTION_R Props 1.1, 1.2, 1.4; PROVED)
* w = (t,u,v) ↔ γ_w = [[A, n], [t, A*]] ∈ SL₂(ℤ), A ≡ A* ≡ −1 (mod t): matrices congruent to −[[1,∗],[0,1]] modulo
  their own lower-left entry ("self-levelled"); RS's Ψ has the fixed level 4.
* χ(w) = (A/n) = (2/n)^e J(−t, A_o): reciprocity turns the symbol mod the target n into a character mod 4t of a divisor
  of tn + 1 (RS do the opposite turn: symbol on a line → character mod the target, then Pólya–Vinogradov).
* For 4 | t: γ_w lies in the a ≡ d ≡ 3 coset of Γ₀(4), where (a/b) = −(c/d) (vs RS Lemma 3.1's +), and self-levelling
  forces (c/d) = +1 ⇒ (A/n) = −1 ⇒ n ≠ □.

## Barrier screen
B2: the self-levelled congruence is the B2 hallmark (modulus part of the solution), here in RS coordinates. T1: proved
again in a new form. B1/B3: nothing new.

## Cheap numerics
`scripts/z37_dictionary.py 20000`: 192 283 words, sign formula 0 failures; 480 200 (A)3 words have (t/A*) = 1.

## Assessment
PROVED dictionary; no route. It locates the exact difference between RS (fixed level, fat orbit) and ES (moving level).
