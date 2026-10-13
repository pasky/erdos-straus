# bsG_square_shadow — T1 acts partially on Lorenzini's (W): the square shadow (O180)

## Idea
HJ_DEEP calls (W) "T1-free". Test it: at n = m², every prime q | tn + 1 has (−t/q) = 1, so every divisor X of tn + 1 satisfies (−t/X₁) = 1.
On the word condition X ≡ −1 (mod t) this character is pinned down for some classes of t.
**Lemma (PROVED; LORENZINI_W Lemma 3.1).** At n = m² the middle letter satisfies t ≢ 0 (4) and t ≢ 7 (8), and t ≢ 3 (4) if m is even.
At n = k m², t ≢ 0 (mod 4k) (Remark 3.2). The t ≡ 0 (4) case is ES's T1 in HJ dress.
**Prop (PROVED; LORENZINI_W Prop 3.3).** Nevertheless every square except 1, 9 is a value: (2, n/4+1, 2) for even m, (2, 2, (n+2)/3) for 3 ∤ m,
and (3, (k²+1)/2, 6) for m = 3k with k odd.

## Literature
Lorenzini, J. Number Theory 257 (2024), Ex. 6.2(a), Prop 6.3 (does not single out squares). ES T1: Elsholtz–Tao Prop 1.6.

## Barrier screen
B5/T1: applies *partially*. Two of the four middle classes mod 4 survive, so the shadow lowers counts but never empties them. Lemma 3.2 of HJ_DEEP
(n ≡ −1 mod M escapes all finite coverings) is void on squares, because −1 is not a square mod 3 or 4. That is why squares are coverable.

## Cheap numerics
`scripts/bsG_sqslices.py 300`: middle letters mod 8 are {1,2,3,5,6} at odd squares and {1,2,5,6} at even squares, and all 8 classes occur at the control m² + 2.
`scripts/bsG_kshadow.py`: 35 372 words, 0 violations. `scripts/bsG_minR.c 10⁸`: from 2^14 on, the dyadic minima of R(n) are squares of smooth numbers,
e.g. R(2310²) = 4 (mean ≈ 104). `scripts/bsG_sqproof.py`: covering certificate.

## Assessment
PROVED (lemma and proposition). Interesting as a correction: genus characters do act on (W). The record-low R(n) are T1-shadowed squares,
not Lorenzini's exceptions. Promise for ES: 0 (squares are where ES is impossible anyway). Promise for (W): explains its hardest-looking inputs.
