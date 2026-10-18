# z40 memo 1 — the two boundary points of 2^a3^b + 1 and why F2 was "trivial either way" (O270)

* The {2,3}-unit-square points of P = {2^a3^b + 1} are (0,1) (limit 4) and (3,0) (limit 9).
* (0,1): n = 3·2^{a}3^{b−1} + 1 = 48X⁴ + 1 on a ≡ 0, b ≡ 1 (mod 4), X = 2^{(a−4)/4}3^{(b−1)/4}. MENU_STERILITY Theorem B/C(a)
  are identities in X valid for every integer X in a class mod 11, so they transfer verbatim (EXP_15 Lemma 1.1).
  Lesson: a window whose budget is forced by an algebraic factorisation of a polynomial in X does not care how X is
  generated; "two-base" only adds the classes X ≡ 3, 5, 7, 9 mod 11 of the same rules (all eight X ≢ 0, ±1 occur).
* (3,0): n = 8X³ + 1 = (2X + 1)(4X² − 2X + 1) for 3 | a, 3 | b: an algebraic factor of n itself, a smaller Pierpont
  number. Unit-square boundary points of S-unit families of the shape u³·8 + 1 are dissolved by cyclotomic descent.
  General principle (spark): for F_S(k, 1) = {k·u + 1 : u ∈ ⟨S⟩}, an integer unit-square point k·u₀ + 1 = v² with
  k·u₀ a perfect p-th power (p odd) is dissolved by descent along {u ∈ u₀·⟨S⟩^p}; 15·2^s + 1 has no such escape since
  15 is not a perfect power (Capelli).
* What remains for "ES for all Pierpont numbers" is a pure covering/supply question (EXP_15 §1.3): no sterile point was
  detected at the levels reached, but the 2D tree did not close (open cells grow ×~4 per lift).
