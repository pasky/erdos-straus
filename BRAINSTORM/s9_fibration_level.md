# s9_fibration_level — fibre ES over the level t: every fibre has an integral point, the obstruction group of the fibre is (ℤ/t)^* = ray classes mod t∞, and only one character comes from the total space (O271, mandatory (v))

## Idea
Fibration method (Colliot-Thélène–Skorobogatov–Swinnerton-Dyer; Harpaz–Wittenberg; for integral points Harpaz) with Schinzel /
Bateman–Horn on the base: fibre the ES-five surface X_n : tuv − u − v = n over the level t and ask what the method would need.

## Literature
Harpaz–Wittenberg, *On the fibration method for zero-cycles and rational points*, Ann. of Math. 183 (2016) (from memory);
Y. Harpaz, *Integral points on conic log K3 surfaces*, J. Eur. Math. Soc. 21 (2019) 627–664, arXiv:1511.04876 (abstract checked:
explicit sufficient conditions for integral points on schemes fibred into affine conics, adapting Swinnerton-Dyer's method);
Bright–Loughran arXiv:1908.02526 (Br U_n/Br ℚ = ℤ/2, no BM obstruction for n ≥ 2); repo (J)50/(J)52 ("ES imitates ∞").

## Dictionary (PROVED, elementary)
* For t ≥ 1 the fibre F_t : (tu − 1)(tv − 1) = tn + 1 =: N is, over ℚ, a torsor under the split torus G_m (X = tu − 1, Y = tv − 1,
  XY = N); its integral points in the (u, v) model are the factorisations N = XY with X ≡ Y ≡ −1 (mod t).
* **Every fibre has an integral point**: (u, v) = (0, −n). So integral solvability of fibres is never the issue; ES is
  integral solvability **in the positive region** u, v ≥ 1 (the archimedean condition; cf. (J)52).
* With positivity, X runs over positive divisors of N, and the condition is: the ray class of X modulo t∞, i.e. its image in
  (ℤ/t)^* ≅ Gal(ℚ(ζ_t)/ℚ), is −1 — the class of **complex conjugation**. So the level-t event is "some positive divisor of tn + 1
  has Frobenius = c_∞ in ℚ(ζ_t)" (the (J)50 dictionary, fibrewise). Its obstruction group is all of (ℤ/t)^*^ — Thm K's
  characters (O269).
* Only one of these characters is the restriction of the total space's Brauer class: χ_{−t} (SYNTHESIS_SPARKS9 Prop 2.1), the
  quadratic shadow of c_∞ in ℚ(√−t) ⊂ ℚ(ζ_t); and that layer is solvable at every non-square n (Prop 2.2).

## Barrier screen
The fibration method needs (a) fibres whose integral/strong-approximation obstruction is controlled by a vertical Brauer group of
bounded size, and (b) a base-point choice (Schinzel) making the fibre's local data favourable. Here (a) fails maximally: the
fibrewise obstruction group (ℤ/t)^* grows with the base point while Br(X_n)/Br₀ = ℤ/2 (BL); and (b) points the wrong way:
Schinzel-type hypotheses make N_t = tn + 1 prime (or a prime times fixed factors), which empties the fibre's positive divisor set,
whereas ES needs N_t to have a prime factor in a prescribed class mod t — the B2 event itself. The split fibres also fall outside
"affine conics with non-split norm form" settings as far as we can see (Assessment; we did not check Harpaz's exact hypotheses).
T1: on fibres of n = m² the classes of all prime factors lie in ker χ_{−t} ∌ −1 (Prop 2.1(c)). B1: a fixed finite set of fibres is
a fixed slice set (redteam-2 Thm 2.2, fails i.o. under H).

## Cheap numerics
Covered by `scripts/s9_level_bm.py` (fibre-wise quadratic layer) and `scripts/s9_words.c` (fibre counts).

## Assessment
A clean dictionary (fibre = G_m-torsor; integral point always; positivity + ray class mod t∞ = "a divisor imitates ∞"), and a
precise statement of why the fibration method collapses to B2: unbounded fibre obstruction groups with a ℤ/2 total-space Brauer
group. Label: PROVED (elementary dictionary) + Assessment (method collapse). No route.
