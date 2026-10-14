# R208 — hostile review of O210 FRIEZE_ES.md (+ BRAINSTORM/y2_*.md)

Reviewer: R208 (side-agent/review-frieze). Reviewed at merge of side-agent/frieze-es @ 7bb85625.
From-scratch scripts: `scripts/review_r208_*.py`; logs `logs/review_r208_*.txt`.
**ES is not solved; nothing below changes that.**

## Summary verdicts (filled in claim by claim)

| # | claim | verdict |
|---|---|---|
| 1 | Lemma 1.1 (parity rigidity: exactly two adjacent even cluster variables) | SOUND |
| 2 | Thm 1.2 (even-edge sign law), 3-case proof | SOUND (minor typo, see D2) |
| 2′ | Novelty: "extends DK Thm 4.5 to formal words and N ≡ 3 (4)" | GAP (overclaim: already MODEL_SPECIFIC Thm 3.1(a); see D1) |

## Claim 1 — Lemma 1.1 (re-derived)
Ptolemy relations (P) re-derived from N = mcs − c − s, h = cm − 1, h′ = ms − 1 (all five are polynomial identities).
Mod 2 with N odd, all five read q_i q_{i+1} ≡ 1 + q_{i+3} (indices mod 5): checked for each i (the N in relations 1, 4
and the N·q₃ in relation 5 reduce to 1 resp. q₃). Memo proof: if all odd, q_{i+3} even — contradiction; if q_i even,
relations at i−1, i force q_{i+2}, q_{i+3} odd, and relation at i+3 gives q_{i−1} ≡ 1 + q_{i+1}; applying the same
to the even neighbour gives exactly two evens. Correct. No positivity used (only N odd) — correct as stated.
CERTIFIED independently (`scripts/review_r208_even_edge.py 100000 1000000 10000000`, 20 s): all 5 115 860 odd-N
formal words N ≤ 10⁵ (count and all five edge-position counts agree with the author's log exactly), plus 10⁶ random
words with letters ≤ 10⁷ (N up to ~10²¹): 0 failures.

## Claim 2 — Theorem 1.2 (re-derived line by line)
Positivity used: every Jacobi symbol in the proof has a positive odd bottom (N, h, c′, h″, s, m all ≥ 1), and
gcd(h′, N) = gcd(h, N) = 1 from hh′ = 1 + Nm, so no symbol vanishes.
* Case A {c, m}: h ≡ −1 (mod 2^{a+b}), a + b ≥ 2 ⇒ h ≡ 3 (4). Step 2 reciprocity sign (−1)^{(h−1)/2·(N−1)/2} = (−1/N) ✓.
  Step 3: N ≡ −c (h), (−1/h) = −1 ✓. Step 4: (c′/h)(h/c′) = (−1/c′) since h ≡ 3 (4), and (h/c′) = (−1/c′) ⇒ (c′/h) = 1 ✓.
  Step 5: a + b ≥ 3 ⇒ h ≡ 7 (8); a = b = 1 ⇒ cm ≡ 4 (8), h ≡ 3 (8), (c/h) = (2/h) = −1 ✓. Final sign bookkeeping
  −(−1)^{[cm≡4(8)]} = (−1)^{[8|cm]} uses 4 | cm ✓. Mirror {m, s} by reversal, using (h/N) = (h′/N) ✓.
* Case B {h′, c}: s ≡ −N (4) from h′c ≡ 0 (4) ✓; step 5 exponent ((h″−1)/2)((N−1)/2 + (s−1)/2 + 1) even since
  N + s ≡ 0 (4) ✓; step 7 Ns = Nh′c − N² ≡ h′c − 1 (mod 8) (uses (N − 1)h′c ≡ 0 (8)) ✓. In the "otherwise" branch
  the text says "b = v₂(c) = 1"; it should read "b = v₂(h′) = 1 (and v₂(c) = 1)" (D2).
* Case C {h, h′}: m ≡ −N (4) from hh′ = 1 + Nm ✓; (N/h″) = (−1/h″)(m/h″) uses ms ≡ 1 (h″) ⇒ (s/h″) = (m/h″) ✓;
  (h′/m) = (−1/m) from h ≡ −1 (m), hh′ ≡ 1 (m) ✓; step 7 Nm = hh′ − 1 exactly ✓.
* The five edges {h′,c}, {c,m}, {m,s}, {s,h}, {h,h′} are covered by A, A-mirror, B, B-mirror, C ✓.
Corollaries 1.3 (8 | ee′ ⟺ some q_i ≡ 0 (4), since both even letters have v₂ ≥ 1 and the others are odd) and 1.4
(N = M²: (h′/N) = (−1/N) = 1) ✓. Odd-square control: my count is 8 073 words vs the author's 8 068 — the difference
is exactly N = 1 (5 words; 1 is an odd square), which the author's control evidently excludes; all 8 073 have
ee′ ≡ 4 (8). Not a defect beyond wording.
**Verdict: SOUND.** The proof is complete, elementary and self-contained (no Dedekind sums, no cell enumeration).
