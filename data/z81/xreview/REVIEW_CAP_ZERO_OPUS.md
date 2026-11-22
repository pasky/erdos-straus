# Hostile cross-lab review (Claude Opus) of `notes/z81/CAP_ZERO.md` (commit 173a73634)

**Verdict:** ACCEPT IN SUBSTANCE. No mathematical error, circularity, overflow-accounting slip or disguised B2 re-encoding
was found. Form fixes (F1–F8) are owed before export. Labels are correct as written, but §0 is incomplete.

## Line-by-line verification
* **Lemma I (PROVED, checked):** m₀≡3 (4) (odd number of primes ≡3 (4)); F≡1 (4), F≡1 (s), F | s³+1 | s^h+1 (3|h, h odd);
  the lift p+m₀F ≡ (p+m₀)−s·m₀ (mod s²) with s∤m₀. p∤F: the order of a nonresidue would divide 6 yet carry the full 2-part
  (≥8). gcd(K,pm)=1 follows from 4K=p+m. Identity: 1/K+(K+d)/(pKA)=(p+m)/(pK)=4/p. v_s(A)=1, so den z=s^{h−1} and
  r=s^{(h−1)/2}; s|y; there is no other denominator prime. Correct.
* **Theorem I (PROVED rel. the stated inputs, checked):** the indicator [2d|t−1]−[4d|t−1] has mass 1/(2φ(d)). t≡3 (4) and
  t−1|L give (t−1)/2 | L_odd | h with an odd quotient, so (s/t)=−1 ⇒ t | s^h+1. Carrier count (TZ+Stark at modulus 4p≤4R,
  X=R^D; GRH smooth sum) is fine. Large sieve: moduli s≤X, length (2y)^l≤X², energy ≤ l!P^l, so the discarded count is
  ≤2X²(100l/P)^l = X^{.994+o(1)} (2y=X^{o(1)}). T₋: |T₋| ≥ (P−P/10)/2 − O(log X) ≥ .44P, and for χ∉{1,η}
  |Σ_{T₋}χ| ≤ .1P+O(log X). Random-subset coefficients: exactly 0 at η, ≤ e^{−.33P/4} elsewhere. Inversion hits −p, and
  η(−p)=−1 forces odd cardinality. T depends only on U (not on p), and the large sieve is uniform over s, so there is no
  adaptivity issue. Scaling by n/p uses s∤R. The finite range uses the z75 free carrier (`ANALYTIC_BREAK.md` §1, d=Ks^j,
  one prime). Rate: e=(h−1)/2 ≤ 1.5L, so log(1+e) ≤ log L+O(1), which is the same as QR (14). The GRH/Montgomery branches
  are consistent with z80 §12 (U=log₂R, so (log U)^C=(log₃R)^C).
* **Lemma H (checked):** with b=(s^h+1)/m, 4Kb=pb+s^h+1 gives s^c | pb+1; both size cases hold; den exponent h−c ≤ 2E. A brute
  force over s∈{3,5,7,11}, h≤8, all m | s^h+1 and p<2·10⁵ (914 161 cases) found 0 violations of h ≤ 4E+log_s(p+1).
* **Jacobi remark:** this is a correct reading of `CAP_BOUNDED.md` Lemma 1.1/Cor 1.2 at δ_p=0.
* **Theorem T (PROVED, checked):** the reading a_l=max(1,j−2C) is exactly `CAP_DOWN.md` Lemma 3.1. Overflow is
  (δ_l−v_l(K))/2, and a prime of den z must divide y, hence K. The size step m≡−1 (mod A) ⇒ bv≤4W, A_u | b+v ⇒ u≤(4W+1)W,
  G≤20W³ is correct. The B|K test is one reduced class (coprimality is automatic for valid data). log(MB)=o(log T), and BT
  gives O(1/B). The sum per candidate is ≪ G^{−1/4}Y^{2Ck} against (2YH)^k candidates, and it converges above the
  threshold. Ambiguity: "M=8∏_{l≤w}l^H" must include l=2 to the power H, or A|M fails at l=2 (F5).
* **Prop S / fixed-x / Dickson (checked):** 4(9K+1)=9(p+m)+4 ⇒ m | 9K+1, so z=p((1+9K)/m)/9 and den 9. For p=2521, m=11,
  the box {2,3,2}^{±1,0} mod 11 = {1,…,9}, and 10 is missed (verified by hand). The Dickson forms are admissible
  (2521∤M; primes ∤M are ≥5), and t≡1 (11) leaves the box unchanged. F1: 9a²+4 is a sum of coprime squares ✓.
* **Replay:** `scripts/z81_cap_probe.py` reproduces `probe.txt` byte-for-byte in 0.2 s. The independent script
  `scripts/z81_xrev_cap_zero_opus.py` builds Lemma I packets from the actual factorisations of s^h+1
  (s≤53, h≤45, including the lift) and reconstructs exact Fractions. All 567 satisfy the relaxation: den = r², s | y, s∤p.

## Challenges and debate
1. **The method has a limit the note does not state.** The z80 §12 synchronised-alphabet barrier applies verbatim. Full
   coverage of (ℤ/s)^* by subset products needs |T₋| ≫ log s ≍ U primes with (t−1)/2 | L, hence τ(L) ≫ U and
   log L ≫ log U·log₂U. Theorem I cannot reach a polylog cap without changing the alphabet, so say so.
2. **Lemma H should be applied to Theorem I's own carriers.** On the unconditional branch s ≥ R^{D/2} ≥ p^{D/2}, so Lemma H
   gives h ≤ 4E+1. Planting more of s into K could improve Theorem I's cap by at most a factor of 2 in this pattern. That is
   the honest reading, and it is currently left implicit.
3. **Scope of T vs I.** T needs support ≤ Y=(log p)^D. The unconditional carriers of Theorem I (s ≈ R^D) lie outside T. Only
   the GRH branch lies inside it, and there C=(h−1)/2 is unbounded, so T is consistent with I. The Assessment after T should
   say this, so that nobody reads T as a barrier to Theorem I at unconditional heights.
4. **Simplification credit.** Theorem I reproves the QR rates with no pivot q, no binary basis and no bad-conductor sieve over
   generator lists. It is a genuinely simpler proof of z80 QR as well as a support refinement. That deserves a sentence. It
   is also the main reason why an independent second check of §1 is cheap.
5. **Not a B2 re-encoding.** Theorem I is a positive capped construction. Its cap-zero content is nil, and the note says so.
   The file name "CAP_ZERO" oversells this: only §2 concerns cap 0.

## Form fixes owed
* **F1.** §0 lists only Theorem I (RECORD). Add triage for H/T (BARRIER-SCOPED, and merge with the z80 ST FRONTIER §6 line:
  the same thin-profile BT root cause) and for the fixed-x obstruction (METHOD-CX), with proposed one-line FRONTIER §6 text.
* **F2.** Label: mark the z75/z80 inputs as internal and unrefereed, and add "ineffective" in the Label as well as in Scope.
  "Effective Linnik-range estimates" is not what the proof uses; it uses TZ Thm 1.4 plus Stark.
* **F3.** The Theorem I statement should say s is a prime with s∤n, r=s^e, e=(h−1)/2.
* **F4.** The STATUS delta needs a pointer `notes/z81/CAP_ZERO.md` §1 and "cross-review owed" until a second review. The §1B
  item is already at its 6-line cap, so the added sentence needs compensating compression.
* **F5.** Theorem T: state explicitly that 2^H | M (or treat l=2 separately).
* **F6.** The letter y is overloaded: it is both the Maynard scale and the ES denominator.
* **F7.** Unclear sentences: "This is why simply treating the adaptively selected t's as independent samples would be wrong"
  and "Here is the deterministic size step that a mere union bound on m would miss". Either say what they refer to or delete
  them.
* **F8.** Review line: point it to this file.
