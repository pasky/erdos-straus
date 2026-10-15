# MENU_STERILITY — sterility is menu-relative (task O240, spark relay Z9)

Status: O240 work in progress (unreviewed). **ES is not solved here, and no infinite case of ES for primes is claimed.**
Labels as in DISCOVERIES.md. Memos `BRAINSTORM/z15_*.md`; scripts `scripts/z15_*`.
Builds on SYNTHESIS_SPARKS6 (O238, Thm 1.1: ES for all 4^s + 105), EXPONENT_COVERING ((J)22 Thm 1.2/1.4, Cor 1.5),
NEAR_SQUARE ((J)55 Lemmas 1.1/1.3, Thm 2.2, 3.3, 3.4), POINTWISE_BINARYFORM ((J)3 Thm 3.2, §4.1), CAP_DOWN (Lemma 1.1 windows).

## 0. Iteration log
(I1) Reading. Every B1 barrier in the list is proved by the same two-step mechanism: (a) a *pointwise witness*
(NEAR_SQUARE Lemma 1.1/1.3: every Type I/II solution of odd n carries D with (D/n) = −1), (b) a *gluing statement* that
the parameter set of the menu item contains points where (D/n) = +1 is forced (actual odd squares: Schinzel, (J)3,
Thm 3.3; or Hilbert reciprocity in the parameter algebra: Thm 3.4). Step (a) is menu-independent. Step (b) is where the
menu enters: it is a statement about the *parameter algebra* A = ℚ[u]/(φ) of the family n = φ(u).
(I2) Plan: generalise Thm 3.4 to every φ (§1, "witness reciprocity"), identify the sterile set of a one-parameter menu as a
2-descent object of the double cover w² = φ(u) (§2), read O238's 105 point and the near-square sets through it (§3),
then attack the uncoverable Proth family 3·2^m + 1 of (J)22 with root menus (§4), and the (J)54 prime points (§5).
