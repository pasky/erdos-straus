## Z0077 — Galois-orbit ES Tr_{K/Q}(1/x) = 4/p in cyclic cubic fields: a positivity mod-4 obstruction (shard S5)

**What.** For K cyclic cubic and x ∈ O_K totally positive, Tr(1/x) = s₂(x)/N(x), so the item's equation is p·s₂(x) = 4N(x).
* PROVED (elementary). If p is inert in K, p | N(x) forces p | x; with x = p·y the equation becomes Tr(1/y) = 4 — independent of p.
  Conversely any totally positive z ∈ O_K with Tr(1/z) = 4k gives x = p·k·z for every p (and every n). So all inert p are solvable or none is.
* PROVED. If 2 is inert in K and every totally positive unit is a square (true for conductors 7, 9, 13, 19, where the units have all
  sign patterns), then no totally positive unit u has 4 | Tr(u⁻¹): with u = w², Tr(u⁻¹) = Tr(v)² − 2s₂(v), v = w⁻¹, s₂(v) = ±Tr(w), so
  4 | Tr(u⁻¹) needs Tr(w̄) = Tr(w̄⁻¹) = 0 in F₈, impossible (the trace-0 Frobenius orbit of F₈^× is inverse to the trace-1 orbit, and Tr(1) = 1).
* EVIDENCE. Box search |coords| ≤ 60 in Z[θ] (≈ 4.1–5.9·10⁵ totally positive elements per field; conductors 7, 9, 13, 19): Tr(1/z) is
  an integer for 187 / 166 / 74 / 51 elements with residues only 1, 2, 3 (mod 4); 4 | Tr(1/z) never occurs. With signs allowed (box 25)
  4 | Tr(1/z) occurs 258 / 426 / 116 / 68 times. Polynomial census X³ − aX² + mcX − c (roots positive, Σ1/x_i = m, irreducible, D > 0),
  a ≤ 70: cyclic (D = □) counts for m = 1…16 are 18, 17, 11, **0**, 8, 6, 4, **0**, 6, 2, 3, **0**, 2, 2, 2, **0**; non-cyclic totally real
  counts are 1788–20968 for every m including 4 | m. In all 75 cyclic hits (m ≤ 11) Tr(z)·Tr(1/z) ≢ 0 (mod 4).
* EVIDENCE. Primes p ≤ 10⁴ solved in the box: exactly split primes (cond. 7: 13, 29, 41, 43, 71, 83, 97, 113, 127, 139 = all split p ≤ 139;
  cond. 9: 17, 19, 37, 53, 73, 89, 107, 109, 127; cond. 13: 5, 31, 47, 53, 73, 79, 83, 103; cond. 19: 7, 11, 31, 37, 83, 107, 113, 163, 179,
  191, 293); no inert or ramified prime.
* CONJECTURE. For every cyclic cubic field and totally positive z ∈ O_K with Tr(1/z) ∈ ℤ: 4 ∤ Tr(1/z) (stronger: Tr(z)Tr(1/z) ≢ 0 mod 4).
  Then the Galois-orbit ES fails for every inert prime (2/3 of all primes), and the obstruction needs both positivity and cyclicity.
  It is not a 2-adic condition on the discriminant alone (D ≡ 1 mod 8 is attainable with 4 | m, a, c odd).

**Reproduce.** `uv run --with numpy python scripts/z52d_p2_ZF1_Z0077_tr4.py 60` (add a 2nd arg for all signs; `SPLIT2=1` for
conductors 31, 43, 73); `gcc -O2 scripts/z52d_p2_ZF1_Z0077_poly.c -lm -o poly && ./poly 70 16`. Data: `data/z52b/pass2/ZF1/Z0077/`.

**Why it might matter for ES (Assessment).** It has no direct bearing on ES over ℤ: the item's "reformulation" premise is false. It is a
clean toy where positivity + a reciprocity-type parity blocks a whole Chebotarev class of primes, which is exactly the kind of
obstruction Bright–Loughran rule out for ES. A proof would be a useful calibration example for "positivity obstructions" (FRONTIER §1, T1).
**Next.** Prove the conjecture: am − 9 = Tr(u), u = (z − σz)²/(z·σz) totally positive with N(u) = (Δ/c)², or compute Hasse invariants of Tr(y v²).

