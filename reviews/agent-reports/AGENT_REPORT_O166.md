# AGENT_REPORT_O166 — function-field ES: extinction mechanisms, open cases (checkpoint 1)

Main file: FUNCTIONFIELD_ES2.md. Scripts: scripts/ff2_tree.c (ffl_tree copy, larger divisor buffers, FFL_ALLUNC),
ff2_point.c (test one class), ff2_slice.c (slice test x ≡ u at one prime, ≡ v elsewhere), ff2_crtpoint*.py,
ff2_caseB.py (exact Case B search at x*), ff2_polyq.py (tiny F_p[T] library).

## Results
1. **Compactness criterion (PROVED, §0.1).** A finite linear covering of ES_q(A,·) exists iff the closed
   obstructed set O(q,A) ⊂ R̂^* is empty. O140 Prop 4.1 is 1 ∈ O for char ≥ 5. So (c) is a question about points.
2. **The q = 3, A = T² tree plateau (≈1.06–1.15 % uncovered at depths 6–8) is (at least partly) an artefact.**
   ffl_tree only tries families with E | W (small primes). At points x ≡ 1 off T, families with large-prime E
   are valid deterministically and do cover many classes (random search found Case B factorisations with
   L' = T² − 1). Earlier "uncovered" slice counts are therefore upper bounds only.
3. **Candidate obstructed point x*_c (x ≡ 1 at every prime ≠ T, x ≡ 1 + cT at T), q = 3, A = T².**
   Case A families (E | a0 + b0) are impossible there (PROVED sketch in §0.2, valid for every odd q, A = T^k,
   k ≥ 2). Case B reduces to an explicit divisor problem (normal form (****)); exact search finds no family for
   deg L' ≤ 7, j ≤ 8 (c = 1) and deg L' ≤ 5, j ≤ 5 (c = 2). **Conjecture 0.2** (EVIDENCE only): x* ∈ O(3,T²), so
   ES₃(T²) has no finite linear covering. Not proved: Case B for all L' remains open.
4. **Proposition 1.1 (PROVED, char ≥ 5):** even n-dependent collections of linear families fail unless their
   moduli reach degree ≥ n/2 − O(log n) (Weil gives a prime P ≡ 1 mod W(n); O140 Prop 4.1 applies). This is the
   lottery scale proved in F_q[T]. (a)/(b): no non-linear deterministic mechanism found; Assessment in §§1–2.
5. **(d) Proposition 3.1:** linear-family validity is independent of deg P (Lemma 6.2), so no degree-parity
   obstruction classes exist for linear coverings; data show no parity pattern.
6. q = 4, A = T²: slice x ≡ 1 off T is fully covered (0/192 mod T⁴); a deeper ffl tree (NTH 13, depth 6) was
   started — see FUNCTIONFIELD_ES2.md for its result if it finished.

## Not achieved
No proof of extinction in char ≥ 5 (the prize). No settlement of q = 3 or q = 4 with A = T². Conjecture 0.2 is
unproved.

## Sparks (not pursued)
* Prove Case B at x*: the covered T²-digit is exactly where the Artin–Hasse coordinate at T² of u vanishes
  (u ≡ E_AH(cT) mod T³). A char-3 Artin–Schreier–Witt (wild) reciprocity, Σ_v Res_v(f·dE/E) = 0, might give the
  invariant that kills Case B. Quadratic (Jacobi) reciprocity only gives "deg E, deg E' even".
* A covering search that handles large-prime E: at each uncovered class, families with new prime E are valid on
  explicit subclasses mod E; refine on those E only (adaptive), instead of a fixed refinement list.
* Non-formal E: E | P − P^σ (q = p^r), or E from Frobenius residues T^{q^j} mod P.
* Same slice analysis for q = 3, A = T²+1 and A = T³ (slice counts 28/72, 35/54, under-powered as in item 2).
