# bsG_even_half — Lorenzini's family 2^m − 2 by a Sierpiński covering of the exponent (O180)

## Idea
Lorenzini (Prop 6.3(a), Remark 6.4) leaves the even values n = 2^m − 2, m odd, open. For such a one-parameter exponential family, a fixed-pair
family n ≡ c (mod d) becomes a condition m ≡ m₀ (mod ord_{d′}(2)). A covering system of the exponent (as in Sierpiński/Erdős coverings) may exist even though no
covering of all n does.

## Result (LORENZINI_W Thm 9.1; PROVED, computer-found certificate checked by hand)
Six families, with moduli 9, 72, 13, 27, 109, 592, cover all odd m mod 36. Hence every even n ≥ 16 except 510 is xyz − x − z with x, y, z ≥ 2.
(W) reduces to odd n ≡ 3, 9, 11 (12) with n + 2 prime.

## Literature
Lorenzini, JNT 257 (2024), Prop 6.3, Remark 6.4, Example 6.2(a); arXiv:2311.06367. Sierpiński numbers / covering systems (Erdős 1950, Sierpiński 1960).

## Barrier screen
It escapes B1/Lemma 3.2 legitimately: 2^m − 2 is not dense in Ẑ (it accumulates only on {2^μ − 2 : μ ∈ Ẑ}-type points), and none of those is sterile.
The odd residue (n + 2 prime) is dense in the relevant classes, so no such covering exists there.

## Cheap numerics
`scripts/bsG_pow2.py 20000 L` (L = 36 minimal among tested), `scripts/bsG_pow2_cert.py` (explicit check, odd m ≤ 4001).

## Assessment
PROVED. A small but genuine partial answer to a published open question. Promise for ES: 0. For (W): it closes one of Lorenzini's two open families.
