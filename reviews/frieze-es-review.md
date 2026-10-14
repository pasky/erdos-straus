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

## Claim 2′ — novelty of Thm 1.2 (D1)
FRIEZE_ES §1 Remark / §6 and memo y2_even_edge say Thm 1.2 "extends [DK Thm 4.5] to formal words and to N ≡ 3 (4)".
But MODEL_SPECIFIC Thm 3.1(a) ((J)32, on main) already states, for *every word incl. boundary words and every odd n*:
"a word lies in S₄ ⟺ χ(w) = −1", χ = (−A/n) = (−h′/N), S₄ = "some cluster variable ≡ 0 (mod 4)" — and notes "for
n ≡ 3 mod 4 it is new in this form". Since (−h′/N) = (−1/N)(h′/N), Thm 1.2 ⟺ "χ = −1 ⟺ 8 | ee′" ⟺ (by Lemma 1.1)
MODEL_SPECIFIC 3.1(a). So the *statement* of the extension is not new; CHI_FLIP Cor 1.2 (R198 repair) also gives a
self-contained proof of the same cell law. What IS new: (i) Lemma 1.1 (mod-2 rigidity, the even edge as a locating
device); (ii) a short computation-free proof of MS 3.1(a), avoiding DK Cor 4.1 (Hirzebruch–Zagier + Rademacher) and
any 512/320-cell enumeration. **Verdict: GAP (overclaim of novelty), repairable by rewording.**

## Claim 3 — transport law §2 (re-derived)
With o = q_{i+3} for the even edge (q_i, q_{i+1}) — o = h for {c,m}, h′ for {m,s}, s for {h′,c}, c for {s,h}, m for {h,h′}:
* Case A: (h′/N) = −(−1/N)(c/h), and (c/h) = (2/h)^a = (2/h) always (if a ≥ 2 then h ≡ 7 (8)). So
  (h′/N) = −(−1/N)(2/o) with o = h ✓ (mirror: o = h′).
* Case B: (h′/N) = (2/(Ns))^b(−1/s) = −(−1/N)(2/N)(2/s)·(2/(Ns))^{b−1}; if b ≥ 2 then 8 | h′c and Ns ≡ 7 (8), so the
  last factor is 1 and (h′/N) = −(−2/N)(2/o), o = s ✓. Case C identical with o = m ✓.
* N ≡ 1 (8) ⇒ (−1/N) = (−2/N) = 1 ⇒ (h′/N) = −(2/o) ✓.
My derivation (above) is cleaner than the memo's one-line "proof" (which compares (2/o) with (2/−στ⁻¹) without
defining σ, τ); suggest replacing it (D3). CERTIFIED independently: the full two-branch law (all N mod 8) holds on all
5 115 860 words N ≤ 10⁵ and 10⁶ random words (`review_r208_even_edge.py`, check TR/TR8; 0 failures).
Caveat (Assessment wording, D4): o is not "small" in general (o = h or h′ can be ≍ N); and given N mod 8, (2/o) is
simply a rewriting of v₂(ee′) through one Ptolemy relation, so "the character of N is carried by the character of 2 at
o" is a reformulation of Thm 1.2, not extra information. **Verdict: SOUND** (as a corollary of Thm 1.2).

## Claim 4 — 2-adic Bruhat–Tits "cherry depth" reading
For primitive u, v ∈ ℤ², v₂(det(u, v)) = max{k : u ≡ λv (mod 2^k), λ ∈ ℤ₂^×} = Gromov product of the ends [u], [v]
at v₀ = [ℤ₂²] (standard; Serre, *Trees* II.1 — from memory). The five V_i of LENGTH_THREE Prop 1.1 are primitive
(gcd(h,m) = gcd(N,h′) = 1). The quiddity at V_j is λ_{j−1,j+1}, so q_j even ⟺ V_{j−1}, V_{j+1} leave v₀ along the
same edge. Sides odd ⇒ adjacent ends leave along different edges; Lemma 1.1 gives the colour pattern (a,b,a,b,c) on
(V_{i−1},…,V_{i+3}) with a, b, c the three distinct neighbours, hence two cherries of depths v₂(q_i), v₂(q_{i+1}) and
a lone end V_{i+3} = the vertex carrying o ✓. "Sign ⟺ depth sum ≥ 3" and "T1 ⟺ depths (1,1)" are correct
restatements of Thm 1.2 / Cor 1.4; "depth ≥ 2 ⟺ the two ends agree mod 4 up to sign" ✓ (units mod 4 are ±1).
Small point: the depth-1 (k = 1) colour argument needs only that the three classes of P¹(F₂) are distinct, ✓.
**Verdict: SOUND** (a correct restatement; no new content beyond Thm 1.2).
