# REVIEW_EQUIV — hostile cross-review of `Z64_EQUIV.md` (branch side-agent/z64-equiv @ cd57b8a72)

Reviewer: Opus, standing in for the cross-model reviewer (OpenAI quota exhausted). **ES is OPEN.** The memo claims nothing
else. Independent checks: `scripts/z64_xrev_equiv_checks.py` → `data/z64/xreview/xrev_equiv_checks.txt` (written from
scratch, 18 s). Sources re-read by me: SWZ arXiv:2609.20572v1 (Thm 1.1, Lemma 2.5, Thm 4.8, §8 p = 2, CFG Cor 9.6
citation, ChatGPT acknowledgment); Petronio, Winter Braids LN 7, Thm 3.13/3.14 and Prop 1.18 (numdam PDF);
AMP arXiv:2208.02586 Thm 1.1 (PDF **page image**, not just the text layer); Lorenzini arXiv:2311.06367 Ex. 6.2(a);
MathOverflow 267209 (page); the in-repo catalogue `ES_CONNECTIONS_TODO.md` / `data/z52b/master.jsonl`.

## 1. Per-claim table

| claim | label in memo | my check | verdict |
|---|---|---|---|
| E1 k-Frobenius: (★)(p) ⟺ p = g_k(u,B), k ≡ 3 (4), coprime u,B | PROVED | Beck–Robins Thm 3 as transcribed; gcd(u,B) \| p and the 2p² bound re-derived; brute force 1287 cases (u,B ≤ 15, k ≤ 8), 0 bad | CORRECT; catalogue ID wrong (§2 fix 2) |
| E2 stacky ℙ(u,B) degree identity | PROVED | Pic, ω = O(−u−B), π*O(1) = O(uB): standard; trivial | CORRECT; it *is* catalogue Z1991 verbatim, not Z0418 |
| E3 = Lemma A (orbifold χ ⟺ Aut(X) ratio ⟺ ES, every odd n ≥ 5) | PROVED | Re-derived every case: h ≥ 2; h = 1 (r = 0,1,2,≥3); h = 0 (r ≤ 2, r = 3, r ≥ 6, r = 5 → n ∈ {4m, 24, 48, 120}, r = 4 with (2,2) → two-term split). (b)⟹(c): Selberg + normal core; g ≥ 2 since χ < 0. Independent integer enumeration over **all odd n ≤ 2·10⁶** (exhaustive: s < 0 cases have n ≤ 6888) gives exactly the memo's 15 sporadic n; r = 5 none; explicit ES reps for all 15 | CORRECT. Fix: "every reachable odd n ≤ 6888 (attained)" — the max *odd* n is 273; 6888 is even, attained at (2,3,7,41) |
| Lemma A corollary (only r = 3 at p ≡ 1 (4)) | PROVED | two-term ⇒ p ≡ 3 (4); sporadic primes 23, 47 are ≡ 3 (4) | CORRECT |
| E4 lct, Kollár (16.1) | PROVED rel. Kollár | min{1, Σ1/aᵢ}, 4/n < 1 | CORRECT |
| E5 pretzel / Seifert | PROVED (standard) | det P(x,y,z) = xy+yz+zx = \|e\|·xyz | CORRECT; "no row" is **false**: catalogue **Z0158** is this exact statement |
| E6 lens / plumbing: L₃(p) has a Legendre −1 word ⟺ ∃q, (q/p) = −1, len(p/q) = 3 | PROVED | [[v,t,u]] = (tuv−u−v)/(tu−1); (M⁻¹)₁₁ = (tu−1)/n by cofactor; HJ uniqueness + lens classification | CORRECT-WITH-FIX: the identification with (W)∧(S) and "Legendre class of the linking form" need **p ≡ 1 (4)** (for p ≡ 3 (4), ±A flips the symbol) — put the quantifier in the table row |
| E6 AMP locus: at primes, non-b₂-minimal (★) chains ⟺ C = 1 or 4 ∈ {u,B} | PROVED | AMP Thm 1.1 read from the **page image**: the memo's/subagent's transcription is wrong for (e) and (f). (e) = an isolated −3 plus an *adjacent* (−2,−2) pair; (f) = an **adjacent** (−3,−3) pair (only (d) is a non-adjacent pair). Conclusion survives: (e), (f) need the middle vertex to be −2 / −3, impossible as 4C ≥ 4. Independent induced-subgraph test on all 41 718 (★) chains (u,B ≥ 2) at primes ≤ 4·10⁴: only (a) ever fires, 0 mismatches with "C = 1 or 4 ∈ {u,B}" | CORRECT-WITH-FIX (proof text + `sources/equiv_lit.md` §4b) |
| E6 T(p) relaxation (b = 2 at p ≡ 5 (8)) | PROVED | p/2 = [[(p+1)/2, 2]], (2/p) = −1 | CORRECT |
| E7 (W) ⟺ n ∈ d_{A₃}(ℤ³_{≥2}); coker cyclic; discriminant form = A/n; Jacobi class well defined | PROVED | minor {1,2}×{2,3} = 1 ⇒ Smith form (1,1,n); e₁ of order n; (k²/n) = 1 for gcd(k,n) = 1; Lorenzini Ex. 6.2(a) quote confirmed | CORRECT ("= (W)∧(S)" only for non-square n ≡ 1 (4)) |
| E7 CONV-II ⟺ cn = K(a, 4cd, b) | PROVED | algebraic identity 4abcd − a − b = nc | CORRECT |
| E7 U₇ sentence: "the same A₃-value statement at gn with middle weight ≡ 0 (mod lcm(8,g))" | inside the PROVED block | **False.** n = 105 (U₇(105) = 0, Z₇): g = 2, K(3, 24, 3) = 210 = 2·105, 24 ≡ 0 (mod 8). Also 1465 (g=4,t=48), 3865, 4545. Correct form (from Z60's T-form gn+1 = (xg−1)(zg−1)): **U₇(n) ⟺ ∃ g, x, z ≥ 1 with n = K(x, g, z) and 8 \| xg** — at n itself, middle weight g; checked = U₇ on all odd n < 1600 | **WRONG** as written (fix 1) |
| E8 SL₂ / Farey / cat map | PROVED | T^u(−L^{−c})T^B product recomputed; converse via d ≡ −1; a,d ≥ c−1 ⇒ u,B ≥ 1; trace ≥ 6 (Anosov); torus point | CORRECT |
| E9 ray class / Frobenius | PROVED | (ℤ/4C)^× ≅ Gal(ℚ(ζ₄C)/ℚ), d ≡ −1 ⟺ complex conjugation; cofactor automatically ≡ −1 | CORRECT |
| E10 ℤ[√−p] ideals | PROVED | −p ≡ 3 (4) ⇒ maximal order; α primitive; inert ℓ would divide α; one prime above each ℓ | CORRECT |
| E11 = Lemma F (lcm-balanced, cyclic realisation; chain (★) ⟹ Φ ⟹ ES) | PROVED | lcm's need gcd(u,B) = 1, p ∤ uBC (bounds re-derived); CRT per prime incl. ℓ = 2 \| uB; connectedness; 1/x+1/y+1/z = (p+u+B)/(puBC) = 4/p. Independent search-based CRT on all 1718 (★) solutions at primes < 1500 (both classes mod 4): 0 failures | CORRECT (one-way chain, honestly labelled) |
| E12–E14 | quoted | labelled "quoted, not re-proved" in §4.1 and the headline | label HONEST |
| Hurwitz precedent: SWZ Thm 1.1, Lemma 2.5, Thm 4.8 (odd p), unrefereed, AI-assisted | V ✔ | quotes match the arXiv PDF verbatim; v1 17 Sep 2026; Meng–Wei–Zhou "unresolved in May 2026" quoted by SWZ | CORRECT, honestly labelled "claimed" |
| EKS 1984 Prop 5.7 datum {[a^b],[b+1,1^{d−b−1}],[a, a(b−1)]} non-realisable | V by subagent scan | **independently computed**: non-realisable for every factorisation d = ab, d ≤ 12 (exhaustive over the small class of σ₂); every compatible 3-point datum of degree 5 (67) and 7 (683) realisable (consistent with EKS p. 787 "d = 3, 5, 7") | CORRECT — upgrade the "not re-read by me" note |
| Petronio Thm 3.13 (and 3.14) | V | statement confirmed in the survey PDF (incl. its loose "an odd prime is always…"); datum realisable at d = 5, 9 by brute force | CORRECT |
| Lemma H (CONDITIONAL on SWZ) | CONDITIONAL, "trivial" | R(409) = 0 recomputed; 409 ≡ 1 (4); CFG Cor 9.6 subcase as cited by SWZ (V2) | CORRECT, label honest |
| §5 four-type "circularity" explanation | Assessment (+ type-I observation, Lemma R PROVED) | type-I observation trivial ✓; Lemma R(a) 3v−2 = m² for 3 ∤ m ✓; (c) F(2, m²+2) = m² ✓; (b) toric rays (1,1),(2,1),(3,1) re-derived and matched to Kollár (3.2) with (c₁,c₂) = (1,3) ✓ | CORRECT-WITH-FIX: (b) needs b ≥ 0 allowed (n = 6, 9 only via b = 0); "(S) fails at every odd square" should read "L₃(m²) has no Jacobi −1 word" ((S) is defined for non-squares) |
| §5.1 sign = mod-4 function of letters (20 cells) | EVIDENCE + classical | independent: 196 520 odd-n words (letters < 70) → 40 cells, 0 inconsistent, 20 negative | AGREES |
| F2 cell "8/131 has no 3-term representation" | — | exhaustive x ∈ [17, 49]: none | AGREES |

## 2. Required fixes (priority order)

1. **E7 U₇ sentence is false** (counterexamples 105, 1465, 3865, 4545 — all in Z₇). Replace by "U₇(n) ⟺ ∃ g, x, z ≥ 1:
   n = K(x, g, z), 8 | xg (Z60 Lemma 7(i) T-form; middle weight g at n itself)" or delete it.
2. **Prior-work / catalogue IDs.** Z0394–Z0402 (Sun 1-3-5 … Markoff), Z0417 (Niederreiter), Z0418 (Korobov) are
   unrelated items. Correct: E1 = **Z1970** (verbatim, "≤ t−1 representations"; Popoviciu Z1972); E2 = **Z1991**
   (verbatim); E5 = **Z0158** (verbatim; delete "Seifert: 61 mentions; no row"); E13 / dessins = **Z0167** (+ Z1922;
   Z0167 already notes "a dessin of type (x,y,z) exists iff the triple exists"). Fix §2 "Why not closed", the E-table
   catalogue column and the E11 row ("Z0417 neighbourhood"). Z0153, Z0155, Z0171, Z2606 are right.
3. **MO 267209 attribution.** The source is Ian Agol's *comment* (14 Apr 2017), phrased for hyperbolic 2-orbifolds:
   "one can realize −1 + 4/n (n > 4) iff the Erdős–Straus conjecture holds" — stated just after the triangle formula,
   no proof for other signatures. Credit Agol by name; "new here" = the proof of the all-signature direction (with the
   15 sporadic odd n) and the standard form (c), not the statement.
4. **AMP transcription** (`sources/equiv_lit.md` §4b and the E6 proof): (e) = −3 ∪ adjacent (−2,−2); (f) = adjacent
   (−3,−3). Rewrite "two non-adjacent −2's or −3's would need u = B ∈ {2,3}" as "(d) needs u = B = 2 (p even); (e),
   (f) contain an adjacent (−2,−2) / (−3,−3) pair, and every adjacent pair of the chain contains the middle −4C". Mark the list as re-read from the PDF.
5. **Quantifiers:** E6 row and E7's "= (W)∧(S)" only for (non-square) n ≡ 1 (4) / primes p ≡ 1 (4).
6. Lemma A: "max odd sporadic n = 273; all r = 4 values ≤ 6888 (even, at (2,3,7,41))".
7. Lemma R(b): state a ≥ 1, b ≥ 0; Lemma R consequence wording for (S) at squares (as in the table).
8. EKS Prop 5.7: note the independent computational confirmation (d ≤ 12) instead of "not re-read by me".

None of fixes 1–8 touches the verdict: fix 1 is a side remark (U₇ is not one of E1–E10), fixes 2–3 lower novelty
(E1, E2, E5, E13 were already catalogue rows; the memo already called E2/E5 relabellings), fix 4 leaves the AMP
locus theorem true.

## 3. Labels and overclaims

* "ten proved equivalences E1–E10": true after fixes 1 and 5 (E7's U₇ clause is not an equivalence row; the E7 row
  proper is correct). E11 correctly an implication chain; E12–E14 correctly "quoted".
* SWZ is consistently "claimed, unrefereed"; Lemma H consistently CONDITIONAL; the proposed FRONTIER text keeps
  "claimed and unrefereed". No claim about ES beyond "narrowed". The "every formula-level dictionary is circular"
  explanation is labelled Assessment and scoped to "tools met in this lane" — honest.
* Not re-verified by me (outside the lane focus): Elkies / Fouvry–Murty, Holzer, Waterhouse 4.1, Bhargava 15/290,
  LMWY, Hadamard 2396, Lisca Thm 1.2, Wang–Lu Thm 5. Nothing in the verdict rests on them.

## 4. Falsifier table

Entries checked against the proofs: E3/E13/E5/E8/E11 type-I cells are correct (the signature / chain / triple is
the certificate). E4's "8/131 diagonal stratum empty" confirmed. E7's "(W) at m², 3 ∤ m" is PROVED (Lemma R(a)).
E6's "AMP locus is one parity class of C" is inaccurate: the locus is C = 1 **or** 4 ∈ {u,B} (C arbitrary), as the
memo's own §4.1 says — reword the F2 cell. No HOT LEAD is claimed; none found.

## 5. Verdict

**ACCEPT-WITH-FIXES.** The ten equivalences, Lemma A, Lemma F, the AMP non-minimality locus and Lemma H (conditional)
re-derive; the Hurwitz-precedent citations check out from source and computation. The one false mathematical statement
(E7's U₇ re-reading) and the wrong catalogue attributions (fix 2: four rows were already in the catalogue verbatim)
must be fixed before recording. The verdict "narrowed, no HOT LEAD" follows from what is proved.
