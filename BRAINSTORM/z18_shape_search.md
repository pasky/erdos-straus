# z18_shape_search — exact algebraic families on the higher rungs for 15·2^s + 1, none integral (O245)

## Idea
Type II families with a constant are exactly n = σTT′ − T − T′ (MENU_LADDER Lemma 2.2); each degree shape is a
2-dimensional variety (the Type II surface over ℚ(Y)), so rational points should be plentiful; Lemma 2.1 turns
"integral near μ = 0" into two specialisation conditions. Solve the shape equations exactly (resultants) and filter.
## Literature
Capelli's theorem (binomial factorisation), Schinzel, *Polynomials with special regard to reducibility* (CUP 2000), §2.1.
## Barrier screen
Pure construction attempt; positivity (Lemma 2.3) and magnitude (O239) are the screens that bite.
## Cheap numerics
`z18_tt.py 15 1 4 2 6` → 110 exact algebraic Type II families, 0 integral (99 fail at the 2-adic specialisation);
Type I mode and Y ↦ 2^{±1}Y rescalings: 118–148 algebraic, 0 integral; D = 5, 8 none in range; D = 6: 4 algebraic, 0 integral.
`z18_crt.py` (both types, small-coefficient a₁, b₁, D ≤ 8): 0 hits; sanity: recovers O240 Theorem B for (3,1).
The σ = 4/11 solutions are the Sophie-Germain Type II (a = 11, c = 4); their failure is O239's magnitude bound.
## Assessment
EVIDENCE (negative, bounded heights). 15·2^s + 1 stays undecided; CONJECTURE 6.4 (ladder-sterility) is weakly supported.
