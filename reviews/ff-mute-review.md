# R195 — independent hostile review of FF_MUTE.md (O195)

Reviewer: R195 side agent (independent of the author's self-review in reviews/synthesis-two-hostile-review.md).
Document reviewed: FF_MUTE.md at merge of side-agent/ff-mute (commit 2f212a84 + parent repairs e60d4352).
From-scratch scripts: `scripts/review_fm_*.py` (own GF(q) incl. q = 4, 8, 9, own F_q[T] arithmetic, own power-residue
symbols by direct exponentiation; nothing imported from `fm_*`).

**Overall: no FATAL defect. Headline Thm 3.5 SOUND; Thm 4.2 SOUND; Props 2.1/5.1–5.4 SOUND; two MAJOR framing/scope
defects (M1 char 2 has a finite covering; M2 measure asymmetry) and seven MINOR ones.**

Repairs applied: (filled in below once applied)

## Summary verdicts

* **Prop 2.1 (mute shot identity): SOUND.** Re-derived: Ef = P + AQ², f ≡ −1 (mod A) ⇒ A | P + E; the key relation
  X + Q² = E(f+1)/A gives 1/Y + 1/z = E/(PX) = A/P − 1/X. Degrees deg X = 2deg Q − d, deg Y = n + d − k,
  deg z = n − k, all monic (lc(P)=lc(X)=lc(f+1)=lc(A)=lc(Q)=1; f + 1 monic needs d ≥ 1, true in char 2 as well).
  Parity: AfX = P(f+1) + AQ² and s ∤ f (s | f, s | Q ⇒ s | P), so v_s(X) = σ when σ < 2c and v_s(z) = 2σ − 2c;
  if σ ≥ 2c, v_s(z) = v_s(X) + σ − 2c ≥ 0. Type II shape: gcd(f, P) = 1 ⇒ P ∤ E ⇒ P ∤ X. The low-shot variant
  (deg AQ² < n) also re-derived: E monic of degree n − d, X of degree n − k, deg z = 2n − 2k + d − 2deg Q > n − k.
  Numerically: every monic divisor f ≡ −1 (mod A) of random shots P + A s^{2j} (P composite allowed, both degree
  regimes), q ∈ {2, 3, 4, 5, 7, 8, 9}: identity, monicity, NC with min degree exactly n − k, parity, Type II shape
  (P prime): 0 failures (`review_fm_signs.py`, data/review_fm/signs_*.txt).
* **Cor 2.2: SOUND.** z = P·X·(f+1)/(A·Q²) with A | f + 1 and gcd(A, Q) = 1, so the only possible denominators
  are s | Q, and v_s(z) ≥ 0 ⇔ σ ≥ c in both parity cases. Checked on the same shots (0 mismatches of
  "z ∈ R ⇔ f ≡ −1 mod AQ").
* **Lemma 3.1: SOUND.** (R/f)^* cyclic of order q^d − 1; ⟨s²⟩ = squares; j₀ shifted by multiples of q^d − 1
  (any multiple of ord(s²) would do). Uses f ∤ M (so f ≠ P, s and gcd(f, P) = 1) — stated.
* **Lemma 3.2: SOUND.** Re-derived: (−1/f) = ε^d since 1 + q + … + q^{d−1} ≡ d (mod 2); (P/f) = ε^{nd}(f/P);
  (A/f) = ε^{kd}(f/A) (multiplicativity over the prime factors of A) and (f/A) = (−1/A) = ε^k. Hence
  (−PA/f) = ε^{d(1+n+k)+k}(f/P) = 1 ⇔ (f/P) = τ. ℓ-part: (s/f)_ℓ = (−1)^{((q−1)/ℓ)hd}(f/s)_ℓ, and the sign is 1
  for odd ℓ (q odd) and in char 2. Checked by direct exponentiation, without reciprocity, for
  q ∈ {2, 3, 4, 5, 7, 8, 9} (incl. ℓ = 3 at q = 4, 7; ℓ = 7 at q = 8; ℓ = 2 at q = 9 where ε = +1):
  ≈ 1100 random (A, P, s, f), 0 mismatches.
* **Lemma 3.3: SOUND.** −Σ_{deg F=d}Λ(F)χ(F) = Σ α_i^d over ≤ D' − 1 inverse roots of modulus ≤ √q; prime powers
  contribute ≤ Σ_{e ≤ d/2} q^e ≤ q^{⌊d/2⌋}·q/(q−1) ≤ 2q^{d/2}. Lower bound for dπ_q(d) likewise.
* **Lemma 3.4: SOUND.** Root-counting injection f ↦ its d roots in F_{q^d} (f ≠ s ⇒ s(α) ≠ 0), orthogonality, and
  Weil for the separable (h distinct roots) monic s — not an ℓ-th power since squarefree with h ≥ 1. The i = 0 term
  is ≤ q^d; the (ℓ−1)/ℓ factor is dropped (harmless).
* **Thm 3.5 (headline): SOUND** (minor wording defects m1–m3 below). Reconstructed in full:
  - primitive root ⇔ not an ℓ-th power for every prime ℓ | q^d − 1; split ℓ | q − 1 vs Λ_d. For ℓ ∈ Λ_d,
    ord_ℓ(q) | d prime and ≠ 1 ⇒ ℓ ≡ 1 (mod d); ℓ odd (2 | q^d − 1 ⇒ q odd ⇒ 2 | q − 1); d odd ⇒ ℓ ≡ 1 (mod 2d).
    Sorted ℓ_i ≥ 2di + 1 and ∏ℓ_i < q^d give |Λ_d| ≤ m_d and Σ1/ℓ ≤ H_{m_d}/(2d) ≤ L_d. Checked exactly by factoring
    q^d − 1 for q ∈ {2,3,4,5,7,8,9,11}, all odd primes d with q^d ≤ 10⁴⁰: 0 failures (`review_fm_bound.py`).
  - Indicator: (1/Φ(A))Σ_χ χ̄(−1)χ(f) = [f ≡ −1 mod A]; (1 + τ(f/P))/2 = [(f/P) = τ] = [(ii)] by Lemma 3.2;
    1 − (1/ℓ)Σ_i x^i = [x ≠ 1] with x = ε_ℓ^{dh}(f/s)_ℓ, and x = 1 ⇔ s is an ℓ-th power (Lemma 3.2; ε_ℓ = ±1).
    Trivial-term coefficient (1/Φ(A))·(1/2)·∏(1 − 1/ℓ) = δ. Total absolute weight ≤ 1·1·∏ 2(1 − 1/ℓ) ≤ 2^{ω(q−1)}.
    Non-triviality of the mixed characters mod M = APs: CRT components mod A, P, s; the s-component
    ∏ψ_ℓ^{i_ℓ} has order lcm of the ℓ with i_ℓ ≠ 0, so it is trivial only if all i_ℓ = 0; the P-component (·/P) is
    nontrivial for P prime (and for every non-square monic P — used in Thm 4.2(a)). ✓
  - Lemma 3.3 with D' = D (imprimitive characters mod M are fine: Rosen's degree bound holds for any nontrivial
    character mod M), f | M removed at cost ≤ D/d; Lemma 3.4 for Λ_d. The final inequality and the "in particular"
    criterion re-derived (the slack 2^ω q^{d/2} > δD holds because q^{d/2} > (2/δ)2^ω(D+2) > D). ✓
  - Effectivity: C(q, A, h) explicit; the dependence on A through δ ∝ 1/Φ(A) is stated (C grows with A and h —
    not uniform in A, correctly not claimed). Bertrand ⇒ an odd prime in (x, 2x] ⇒ degree ≤ 4 log_q n + 2C. ✓
  - Char 2: q − 1 odd, so no ℓ = 2 and condition (ii) is vacuous (squaring is bijective on F_{2^{rd}}^*); the ℓ-th
    power reciprocity sign is 1; δ with c_q = 1. Char 3: q − 1 even, ℓ = 2 is a Kummer prime and the square
    condition (ii) is a separate character mod P (independent of the mod-s characters by CRT). Nothing
    characteristic-specific fails; the only char-2/3 subtlety (NC not automatic) is handled by Prop 2.1's exact
    degree count. ✓
  - Explicit numbers (q = 3, A = T, h = 1, my evaluation of the stated bound): positive at d = 11 for n ≤ 3,
    d = 13 for n ≤ 17, d = 17 for n ≤ 271, d = 23 for n ≤ 9862, d = 29 for n ≤ 307381 (author: "~300", "~9800",
    "~3·10⁵" — fine except "~300" is generous for 271). Note the bound is **already positive at d = 11, 13**, not
    "only from d = 17". Other cases: q = 2, A = T first d = 7 (n ≤ 4); q = 5, A = T first d = 29; q = 3, A = T² first
    d = 23; q = 7, A = T first d = 83 and q = 9, A = T first d = 71 (δ = 1/36, 1/32: L_d decays like ln d/d).
    `data/review_fm/bound.txt`.
  - **Small-d "computational coverage" claim (§6): the theorem does NOT need it.** For every n there is a prime d
    with positive bound (d ≥ 2 log_q n + C), so every P is covered by the bound alone; the G(d) counts at d = 5, 7
    are EVIDENCE that the main term is accurate, not a component of the proof. The §6 sentence "so the small cases
    are covered by computation, not by the bound" can be misread as "small n need computation" (m2).
  - G(d) recomputed from scratch (direct exponentiation; `review_fm_count.py`, `data/review_fm/count.txt`):
    q = 3, A = T, d = 7: 29–45 (mean 37.7) vs 39.1; q = 3, A = T², d = 7: 11–16 vs 13.0; q = 5, A = T, d = 5: 36–41
    vs 39.1; q = 2, A = T, d = 7: 18 vs 18.3 (author 18 ✓); q = 4, A = T, d = 5: 40 vs 45.5; q = 9, A = T, d = 3:
    3–8 vs 7.6. Consistent with the author's figures.
  - Citations (no PDFs of Rosen or Lidl–Niederreiter in sources/; checked from memory of the standard statements,
    flagged as such): Rosen Thm 3.3 is the d-th power reciprocity law for *monic irreducible* P, Q,
    (Q/P)_d = (−1)^{((q−1)/d)deg P deg Q}(P/Q)_d — the Jacobi/composite extension used for (A/f) and in Thm 4.2 is by
    multiplicativity (Rosen's general law is Thm 3.5); Rosen Prop 4.3: L(s, χ) for nontrivial χ mod m is a
    polynomial in q^{−s} of degree ≤ deg m − 1 ✓; Lidl–Niederreiter Thm 5.41: |Σ_c ψ(a·g(c))| ≤ (e − 1)q^{1/2} for
    ψ of order m > 1 and monic g not an m-th power with e distinct roots ✓ (applied over F_{q^d} with s monic).
    The RH for the L-functions (|α| ∈ {1, √q}) is Weil; correctly attributed. (m4: cite Thm 3.5 / multiplicativity.)
* **Lemma 4.1: SOUND** (also for composite f, via multiplicativity of the Jacobi symbol in f). Checked by direct
  exponentiation/factorisation for prime f (q = 3, 5, 7, 9) and composite f (q = 3, 5, 7, 9; "Lemma4.1 composite" in
  data/review_fm/signs_*.txt): 0 mismatches.
* **Thm 4.2: SOUND** (one minor scope point, m5). Re-derived:
  (a) the only P-inputs of Lemmas 3.1–3.2/Thm 3.5 are: (·/P) nontrivial (⇔ monic P not a square: the Jacobi
  symbol is ∏(·/P_i)^{e_i}, trivial iff all e_i even), Jacobi reciprocity for monic coprime P, f (fine), and f ∤ M
  (gives gcd(f, P) = 1 for prime f). D = k + deg P + h unchanged. ✓
  (b)/(c) for f' | f prime: f' | Q ⇒ f' = s ⇒ s | M², excluded; f' | M would give f' | AQ², impossible; so
  −A ≡ (M/Q)² (mod f') and (−A/f) = 1 ≠ ε^{d(1+k)+k} = −1 when q ≡ 3 (4) and d(1+k)+k odd. Covers both degree
  regimes, every j, prime or composite f. ✓ (d) ε = 1 ⇒ τ = 1 = (f/M²): condition (ii) automatic, main term 2δ. ✓
  Numerics (`review_fm_search.py t1`, all monic P coprime to sA; squares searched exhaustively over the bounded
  (j, f) box *and* by the unbounded discrete-log route): see §6 below.
  The §7 "reverse question" claim "for every choice of s (and every S)" needs S coprime to P (m5).
* **Prop 5.1: SOUND.** Ef = Aacd·E − E = Aad(a + b) − E = Aa²d + P. deg X = n − k is forced (P | Y, Z ⇒ deg Y, Z ≥ n >
  n − k, so X is the unique least-degree term), hence deg(Aa²d) ≤ 2n − k and deg f ≤ 2n − k.
* **Prop 5.2: SOUND.** (a) P ≡ −AQ² (mod f), Q ∈ ⟨s⟩ ⇔ P ∈ −A⟨s² mod f⟩. (b) f = Aacd − 1 ⇒ ad | (f+1)/A and
  P ≡ −Aa²d; #{(a, d)} = τ₃((f+1)/A) = q^{O(d/log d)}. ("Half of all classes": of the unit classes, q odd; **all** unit
  classes in characteristic 2 — see M1.)
* **Prop 5.3: (a) SOUND, (b) correctly labelled Assessment.**
* **Prop 5.4: SOUND as stated (q odd).** CRT over the g_i; g_i ∤ Q ⇒ −PA ≡ (AQ)² square; g_i | Q ⇒ g_i = s ⇒ s | P,
  contradicting "−PA a unit non-square mod s"; Dirichlet in F_q[T] gives irreducibles of every large degree in the
  unit classes. Validity of each family for large deg P uses the low-shot regime (deg AQ² < n) of the remark — fine.
  **What is precisely proved:** for q odd, (i) every finite set of shot families misses irreducible P of every large
  degree; (ii) Thm 3.5 nevertheless solves every admissible irreducible P. So "no finite shot covering" does not
  preclude a theorem — *for this mechanism, whose sterile set is Haar-null*. Three scope defects in the surrounding
  prose: the 'Reading' sterile set is wrong as written (m6: f = s^m with Q = 1 fires on it; counterexample
  `review_fm_sterile.py`); the moral does not transfer to characteristic 2, where the mute mechanism **has** a
  finite covering (M1); and the comparison with DEPTH_ASPECT Thm 2.5 omits that the ES_q sterile set there has
  *positive* Haar measure, whereas the mute one is null (M2).
* **§6 EVIDENCE: SOUND after the minor repairs below.** Independently recomputed with my own code (`review_fm_search.py`:
  bounded divisor search + unbounded discrete-log route of Lemma 3.1, every reported solution verified exactly):
  - **all irreducible P solved**, 0 verification failures: q = 3, A = T, n ≤ 8 (1316 P); q = 3, A = T², n ≤ 8; q = 3,
    A = T² + 1, n ≤ 7; q = 5, A = T, n ≤ 5; **q = 4** (char 2, non-prime field), A = T², n ≤ 7 (3302 P); **q = 8**, A = T,
    n ≤ 4 (1210 P); **q = 9** (char 3, non-prime, ε = +1), A = T, n ≤ 4 (1903 P); q = 2, A = T³, n ≤ 13; q = 2,
    A = T⁴ + T + 1, s = T² + T + 1, n ≤ 12 (`data/review_fm/search_[AB].txt`);
  - **every known ES_q failure** from `data/ffl/fail_*` re-solved: q = 3, A = T² (n = 3, 4, 5) and A = T² + 1 (n = 3, 6);
    q = 5, A = T (n = 2–4); q = 5, A = T² (n = 3–8 — **including the 15 failures at n = 8, beyond the author's range**);
    q = 7, A = T (n = 2–6); and, not covered by the author, all q = 4, A = T² failures (n = 3–7; inside my full q = 4 run)
    and the q = 8 and q = 9, A = T failures of FUNCTIONFIELD_ES §3 with n ≤ 4 (inside the full runs).
  - **Thm 4.2** (`review_fm_search.py t1`; squares searched over the bounded box *and* the unbounded discrete-log
    route): q = 3, A = T, deg P ≤ 6: 0/17 squares, 468/468 non-squares; A = T³: same; q = 7, A = T, deg ≤ 4: 0/41,
    2016/2016; q = 3, A = T² (k even): 17/17 squares, moduli degrees used {4, 6} only (even ✓); q = 5, A = T and T²:
    19/19 squares, 480/480 non-squares; additionally q = 9, A = T (ε = +1): 7/7 squares, 640/640 non-squares; q = 3,
    A = T, s = T² + 1 (h = 2): 0/23 squares, 624/624 non-squares. All author counts reproduced exactly.
  - **Least shot height**: recomputed with sympy factorisation of the shots and my own exact verification —
    q = 3, A = T, n = 1..9 and q = 3, A = T², n = 2..8: **identical** max / mean / j = 0 share to `data/fm/minq_runs.txt`.
    BUT the author's least shots use degree regimes **outside Prop 2.1's stated hypothesis**: deg AQ² = n and
    n < deg AQ² < n + d (e.g. q = 3, A = T², n = 8: 106 + 57 of the 810 least shots). Restricting to the stated regimes
    (deg AQ² > n + d or < n; `--strict`) gives larger heights (A = T², n = 8: max 18, mean 2.31; `minj_q3_A100_strict.txt`).
    The solutions are valid (I re-derived that Prop 2.1 holds iff deg AQ² ≠ n + d, see m1), so this is a
    statement-scope defect, not a false number.
  - Population counts of §6 (506, 9379, 3500, 3407, 14 564, 23 630, 4134, 2535, 1371 P) re-derived from the Gauss
    formula minus excluded P: all correct.

## Defects

No FATAL defect. The headline Thm 3.5 and Thm 4.2 are correct as mathematics; the defects are in scope/framing (§§0, 5, 7)
and in statement precision.

**M1 (MAJOR) — characteristic 2: the mute mechanism *does* admit a finite covering; the "no finite covering" moral and the
X8 correction are silently q-odd.** Locations: §0 (P3) "the mute mechanism also has no finite covering (Prop 5.4)";
§5 Prop 5.2 "a mute modulus fires on half of all classes"; §7 PROVED list "(Prop 5.4) the mechanism admits no finite
covering by its shot families"; §7 "Correction to the X8 framing" (stated for all q); report O195 likewise. Prop 5.4 itself
correctly assumes q odd, but the conclusions drawn from it are stated for every q while §1–3 explicitly include char 2.
*Argument:* for q even, squaring is bijective on (R/f)^*, so if s is a primitive root mod a prime f ≡ −1 (mod A), f ≠ s,
then −A⟨s² mod f⟩ = (R/f)^*: the ord_f(s) families (f, Q = s^j) cover every P with f ∤ P (low-shot regime
deg AQ² < n, i.e. for n > k + 2h(ord_f(s) − 1)), and a second such prime f₂ covers P = f. Such f exist (Thm 3.5, or by
direct search). Verified: q = 2, A = T, s = T + 1, f₁ = T² + T + 1, f₂ = T³ + T² + 1 — 10 families cover all irreducible P of
degree 14–17 (15 133 P, exact verification; `review_fm_char2cover.py`, `data/review_fm/char2cover.txt`). So in char 2
X8's "sterile points vs none" is literally correct for the mute mechanism, and Thm 3.5 there reduces to an elementary
finite covering plus the existence of one good f (plus finitely many small n).
*Repair:* insert "q odd" in §0 (P3), §7 PROVED list and the X8 correction; in Prop 5.2(a) say "half of the unit classes
(q odd), all unit classes (q even)"; add a Remark after Prop 5.4 with the char-2 finite covering above.

**M2 (MAJOR) — the X8 correction omits the measure asymmetry.** Location: §7 "Correction to the X8 framing" ("the mute
mechanism *also* has profinite sterile points and no finite shot covering … That is not the separation"), echoed in
Prop 5.4 "This is the FF version of B1 + B5 … with the theorem on the other side". The mute sterile set is Haar-null (the
author says so in the Reading), whereas DEPTH_ASPECT Thm 2.5 gives an ES_q sterile set of *positive* Haar measure
(relative measure ≥ 0.97). What Prop 5.4 + Thm 3.5 precisely prove is: *a mechanism with a nonempty, null sterile set
and no finite covering can still be a theorem at every admissible P.* They say nothing about mechanisms whose sterile
set has positive measure, which is the ES_q situation. Hence "sterile points exist" is not a separation (correct), but
the measure-theoretic version of X8 ("positive-measure sterile set vs null") is untouched and is in fact consistent
with the data. *Repair:* add one sentence to the X8 correction: "Here the sterile set is Haar-null, in DEPTH_ASPECT
Thm 2.5 it has positive measure; the example refutes only the 'nonempty sterile set ⇒ no proof' reading, not a
measure-theoretic one" and scope the Prop 5.4 'Moral' accordingly.

**m1 (MINOR) — Prop 2.1's degree hypothesis is stronger than what is used in §6.** Location: Prop 2.1 hypothesis
"deg(A·Q²) > n + d" and the parenthetical remark (covers only deg AQ² < n). Re-derived: the construction is valid iff
deg AQ² ≠ n + d (then deg X = max(n, deg E) − k and deg z = n − k + (max(n, deg E) + d − deg AQ²) ≥ n − k; at
deg AQ² = n in odd characteristic E is not monic but P + E is). The §6 least-shot statistics (`fm_minq.py` accepts every
exactly-valid tuple) use the regimes deg AQ² = n and n < deg AQ² < n + d — e.g. 163 of the 810 least shots at
q = 3, A = T², n = 8. Restricted to the stated regimes the heights are larger (n = 8: max 18, mean 2.31 instead of 13,
1.33; `data/review_fm/minj_q3_A100_strict.txt`). The author's numbers are reproduced exactly with the full regime set
(`data/review_fm/minj_q3_A10*.txt`). *Repair:* restate Prop 2.1 with "deg(AQ²) ≠ n + d" (degrees as above), or say in
§6 that the least-shot counts use these extra regimes.

**m2 (MINOR) — §6 bound bracket.** "(The explicit lower bound … is negative at these small d … so the small cases are
covered by computation, not by the bound. For q = 3, A = T, h = 1 the bound is positive at d = 17 for n ≤ ~300 …)". (i)
The theorem covers *every* n by the bound alone (choose a larger prime d); the d = 5, 7 counts are EVIDENCE about the
main term, not part of the proof — the sentence reads as if small n needed computation. (ii) Exact values: d = 17:
n ≤ 271 (not ~300); the bound is already positive at d = 11 (n ≤ 3) and d = 13 (n ≤ 17); d = 23: n ≤ 9862, d = 29:
n ≤ 307 381 (✓). *Repair:* "…so the counts at small d are evidence for the main term; the theorem itself uses
d ≥ 11 (q = 3, A = T): positive at d = 11 for n ≤ 3, d = 13 for n ≤ 17, d = 17 for n ≤ 271, …".

**m3 (MINOR) — citation precision.** Lemma 3.2 cites Rosen Thm 3.3 for "monic coprime Jacobi symbols"; Thm 3.3 is the
law for monic *irreducibles*; (A/f) for composite A (Lemmas 3.2, 4.1, Thm 4.2 with composite P and composite f) follows by
multiplicativity (Rosen's general form is Thm 3.5). *Repair:* add "extended multiplicatively". Note: Rosen and
Lidl–Niederreiter are not in sources/; I checked the statements from my knowledge of the standard texts (Rosen Prop 4.3
and L–N Thm 5.41 as used are correct), not from the PDFs.

**m4 (MINOR) — Remark 3.5(2), ℤ analogue under GRH.** Over ℤ there is no "prime degree d" trick; the large-ℓ tail
needs Hooley's full GRH argument (Kummer fields ℚ(ζ_ℓ, s^{1/ℓ}) for all ℓ plus Brun–Titchmarsh for the middle range),
combined with a congruence and a quadratic-character condition (Lenstra-type generalised Artin). Plausible; already
labelled Assessment. *Repair:* say which ℤ-theorem would be needed (Lenstra 1977 / Moree's survey) instead of "the same
argument".

**m5 (MINOR) — reverse question "every S".** Location: §7 last paragraph ("for every choice of s (and every S, since
the proof of Thm 4.2(b) uses only f ∤ Q)"). The proof also uses s ∤ M (P coprime to S): if s | M, then a prime f' = s may
divide both Q and M² + AQ², and Prop 2.1's parity argument (s ∤ f) used s ∤ P. *Repair:* "every S coprime to P".

**m6 (MINOR) — the Prop 5.4 'Reading' sterile set is still wrong after the self-review repair.** Location: §5 Reading:
"the points x with −xA a non-square mod every prime g ∤ As are sterile for every shot (prime or composite modulus: an
admissible f has a prime divisor g ∤ As)". False: f = s^m is admissible when s^m ≡ −1 (mod A) (with Q = 1, j = 0 —
Prop 2.1's "s ∤ f" is only needed when s | Q), and then f has no prime divisor ∤ As. Example: q = 3, A = T, s = T + 2,
f = s³ = T³ − 1 ≡ −1 (mod T); the shot (f, Q = 1) fires on every P ≡ −A (mod s³), a class unconstrained at all g ∤ As
(10 irreducible P of degree 4–6 verified; `review_fm_sterile.py`). This defect was introduced by the self-review's
suggested repair ("Every admissible composite f has such a prime divisor"). The body of Prop 5.4 is unaffected (it
imposes the condition at s too). *Repair:* "with −xA a unit non-square mod every prime g ∤ A (including g = s)"; the
set remains nonempty and Haar-null, and the g = s case is handled exactly as in the proof of Prop 5.4.

**m7 (MINOR) — labels.** §7 "(Prop 5.4) the mechanism admits no finite covering … PROVED": add "q odd" (M1). Everything
else is labelled correctly: Thm 3.5/4.2 PROVED (I agree), §6 EVIDENCE, Prop 5.3(b) and the X8 correction Assessment.

## Checks performed (all from scratch; `scripts/review_fm_*.py`, outputs `data/review_fm/`)

* `review_fm_ff.py`: GF(q) for any prime power (tables; q = 4, 8 via irreducible moduli over F₂, q = 9 over F₃), F_q[T]
  arithmetic, Rabin irreducibility test (counts match Gauss's formula for q ∈ {2,3,4,5,8,9}), power-residue symbols by
  direct exponentiation, Jacobi symbols by factorisation.
* `review_fm_signs.py`: Prop 2.1 / Cor 2.2 on random shots incl. composite P and composite f, both degree regimes;
  Lemma 3.2 both statements and Lemma 4.1 (prime and composite f), q ∈ {2,3,4,5,7,8,9}: 0 failures.
* `review_fm_bound.py`: Thm 3.5 bound evaluation; exact Λ_d checks by factoring q^d − 1.
* `review_fm_count.py`: G(d) by brute force vs δq^d/d.
* `review_fm_search.py`: coverage (bounded divisor search + unbounded discrete-log route), all ES_q failure lists,
  Thm 4.2 on all monic P.
* `review_fm_minj.py`: least shot height via sympy factorisation, full vs strict regimes.
* `review_fm_sterile.py`: counterexample for m6. `review_fm_char2cover.py`: finite covering in char 2 (M1).
* Read the author's self-review (reviews/synthesis-two-hostile-review.md) only after finishing my own checks: its
  repairs M1 (4 log_q n), M3 (composite moduli in fm_minq), M4, M7, m1–m3, m7 are applied in FF_MUTE; its M2 repair
  introduced the error m6 above.
