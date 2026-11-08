# Z65_LIFT — internal review (AUTHOR SELF-REVIEW; the hostile-reviewer subagent could not run: auth token expired ×6)

Verdict (self): ACCEPT-WITH-FIXES. An independent hostile review is still owed.

Checked:
1. G0. Faithfulness on X_k: smooth proper base change H¹(X_K̄) ≅ H¹(X_k̄) is G-equivariant. A non-trivial finite-order
   automorphism in char 0 has Lefschetz number #Fix ≥ 0, versus 2 − 2g < 0 if it acts trivially on H¹. OK.
   G acts on the smooth model by uniqueness of the minimal regular model (g ≥ 1). OK (textbook, V2).
2. G1. Weierstrass preparation over complete R: g(Z) − Z has i(g) zeros in the open disc. Simplicity: g′(w) is a root
   of unity ≠ 1 in char 0. OK.
3. G2. Stab_G(w) ≤ I via equivariant specialisation; orbit ∩ D = one I-orbit; P is the unique Sylow-p of I = P ⋊ C_m,
   so Stab ∩ P = Syl_p(Stab). Both double counts re-derived. Checked on y² = x⁵ − 1 (p = 5, C_10; cluster {10, 5},
   m = 2: (a) 1/2 = 1/2) and on z^m = y^p − y (both (a) and (b)). OK.
4. G3. "At most one non-zero term" since each is ≥ 1/2 and the total is < 1. Single-point clusters are excluded by (b).
   OK.
5. G4. All cases re-derived: |W| = 3 (all pure; one non-pure); |W| = 2 with m = 1, π₁ = 1, a ≠ b, a = b ≥ 2
   (divisibility (4p^{a−1} − 1) | (p + 4)), a = b = 1. OK. The script (`z65_lift_goodred_check.py`) implements the
   G3/G4 necessary conditions over all set partitions:
   * singletons must be prime to p;
   * multi-point clusters need ≤ 1 non-p-power;
   * ≥ 1 wild cluster.
   It is non-vacuous: it accepts exactly the Mordell triples, and rejects everything else for p ≤ 1500.
6. Lemma A: for p ≡ 1 (4) prime only triangle signatures occur (Z64_EQUIV Corollary; sporadic odd n are composite or
   ≡ 3 mod 4). OK. Dependence now explicit in Theorem G.
7. G_k: added p > k (hyperbolicity); p ∤ k(k−1)(k−2) covers the π₁ = 1, m = 1 and k = 3 exits. OK.
8. Prop O: Wewers Lemma 1.4(3)(4) quoted correctly (math_0205026.txt l. 352–357); hypothesis p ∥ |G| (mild
   reduction) added to the statement.
9. Prop E: Obus Lemma 3.5 (σ_b ∈ (1/m_G)ℤ, new tails σ ≥ 1 + 1/m_G; 1208.3909.txt l. 352–355) + Wewers Cor 1.11
   (r = 3: sum = 1) + Def 2.1. OK. Marked-cover vs curve reduction clarified, with the Mordell consistency check
   (Ȳ₀ ≅ P¹ meets the tail in one point and is contracted in the stable model of the curve).
10. Lemma S: OK.
11. fpt: Hernández Thm 3.1 conventions (non-terminating digits, L = last carry-free digit) checked; script uses
    ceil(px) − 1 for non-terminating digits. Wording "equality only for …" was too strong: fixed.
12. Scope of the verdict: DEAD refers to the two lifting branches as constructions (Theorem G; Prop O + KT2 rule), not to
    every char-p argument. Fixed in §7.
