# REVIEW_SDEEPF — hostile cross-review of Z64_SDEEPF.md (branch side-agent/z64-sdeepf @ 9625a0477)

Reviewer: Opus standing in for the cross-model reviewer (OpenAI quota exhausted). Brief: xreview_z58 with z58 → z64.
ES and (S) remain OPEN; the memo claims neither. Scripts `scripts/z64_xrev_s_{cells,cover,small,sdeepf_misc}.py`
(own Jacobi / sympy / PARI; no code shared with `scripts/z64_sdeepf_*`). `ulimit -v 4000000`, `timeout` on every run.

## 1. Per-claim table

| claim | memo label | verdict | check |
|---|---|---|---|
| Lemma 1.1, (W_t)/(W_u)/(W_A) | PROVED | **CORRECT** | Re-derived. (W_A): u = (−n mod A) since u < A. Standard; HJ_DEEP / FOREST_CONNECTIVITY Prop 3.1(i) / DK §1. |
| **Thm 2.1** (A/n) = −1 ⇔ 8∣(n+t)(n+u+v) ⇔ 8∣tuv(n+t) | PROVED | **CORRECT — but PRIOR in substance** | Case proof re-read (Case I k = 1 exponent E, Case II reciprocity, Case III j = v₂(A)): sound. Independent: on all 1 280 admissible cells mod 16 the predicate equals DK's five-slot predicate and SDEEP's σ (0 disagreements); 375 274 words, n ≤ 6·10⁴, direct Jacobi, 0 mismatches; `crit8 3000000` re-run reproduces `crit8_3e6.txt` exactly. **Prior:** DEDEKIND_ES Thm 4.5 ((A/n) = −1 ⟺ 4 divides one of t, u, v, A, A*; finite cell proof, mod 8) and §8.1 (mod-4 table); elementary proofs FOREST_DEEP_FABLE Thm A, FOREST_CONNECTIVITY Thm 2.1; "coordinate" form LOWERTAIL_ROUND2_FABLE Thm 1 (some letter ≡ 0 (4) or ≡ −n (8)); the t ≡ −n (8) piece is z1_legendre_levels Prop 1. New: only the one-product formulation 8∣(n+t)·tuv and its self-contained case proof. The lane was unprimed, so this is a rediscovery. The memo must say so; at present the summary presents it as the lane's main theorem. |
| Cor 2.2 (squares have no good word) | PROVED | **CORRECT; PRIOR** | T1 (DK Prop 3.1 / §8.1). |
| Thm 3.1 (a) n ≡ 5 (8): (3,3,(n+3)/8), A = 8 | PROVED | **CORRECT** | Re-derived; all 70 830 class members < 3·10⁵ of (a)–(c) checked (`sdeepf_misc.py`). (a) is elementary (n ≡ 5 (8) is the classical easy case; cf. DK §9 "A = 2" boundary). |
| Thm 3.1 (b) n ≡ 2 (3): ((n+7)/12, 4, 3) | PROVED | **CORRECT; PRIOR** | Same word and sign as bsG_primes_trivial / DISCOVERIES Prop 8.1 ("(3,·,4) word has sign (3/p) = −1"). Cite. |
| Thm 3.1 (c) n ≡ 3 (9): ((n+15)/36, 3, 12) | PROVED | **CORRECT** | (B/n) = (n/B) = (−12/B) = (−3/B) = (B/3) = −1 (B ≡ 2 (3)). Not found in repo; elementary. |
| Open classes mod 72 = {1, 9, 25, 33, 49} | — | **CORRECT** | n ≡ 1 (8), n ≢ 2 (3), n ≢ 3 (9): 1, 25, 49 (≡ 1 (24)); 9, 33 (≡ 9 (24)); 57 ≡ 3 (9) removed. |
| Prop 3.1′, 3.2 | PROVED | **CORRECT** | Examples re-checked by hand, incl. A = 63, u = 8 the least odd A with 7 ∣ A reaching n ≡ 6 (7). |
| Prop 3.3 (1)–(7) | PROVED | **CORRECT; (1),(3),(5) PRIOR** | Every side condition re-derived (for (6): B even and ≡ 2 (3) does not exclude B = 2; what excludes it is 4 ∣ 3n+1 ⇒ 4 ∣ B. One-word fix). Independent: 286 718 words built from the criteria (k ≤ 4, n ≡ 1 (8) non-square < 3·10⁵), all genuine with Jacobi −1. (1),(3),(5) = FOREST_CONNECTIVITY Prop 3.1(iii) (u = 4, 2, 3); the t-level forms are B1_LINE / z29_forced_level_characters territory. Cite. |
| Prop 3.5 (no finite covering) | PROVED | **CORRECT; PRIOR in kind** | (i) transfer to a large square s ≡ 1 (mod 8uv) is right; (ii) (A/n) has period ∣ 4A ∣ M. Analogue of HJ_DEEP Lemma 3.2 / B1 / invol_sign_identities Prop S. Cite. |
| **Thm 3.6** covering: (S) outside 𝔈 (28 classes mod 840) | PROVED + CERT | **CORRECT** | Periodicity argument re-derived (A-words: period ∣ 8A′ ∣ L; uv-words: goodness depends on n mod 8uv ∣ L via Thm 2.1, equivalently DK Thm 4.5). Independent checker (`cover.py`, own Jacobi on 3 representatives per class): the 57 listed words are legitimate (t ≥ 2 integral), A ∣ L, 8uv ∣ L, max threshold 2A − u = 24529 (word (12320,111)); **all 312 312 classes mod L off 𝔈 covered, 0 uncovered**; inside 𝔈, 15 331 of 48 048 classes uncovered by these 57. 𝔈 = the 24 odd-square classes ∪ {265, 321, 769, 825}, all ≡ 6 (7). Small-n part: (S) re-verified for all non-square n ≡ 1 (4) ≤ 2·10⁵ (only wordless: 5, 105). Remarks: the 57 are sufficient, not minimal ((12320,111) or (13,2) can be dropped; threshold then ≤ 9329). Cover2 fractions quoted (96 % in 769 at L·17) match the data files. Appears new in the repo (no prior (S)-covering mod 840 found). |
| Thm 4.1 E(x) ≪ x/√log x | PROVED given Landau | **CORRECT** | Re-derived: n ∈ E, n ≥ 13 ⇒ n ≡ 1 (8) ⇒ n+4 has no prime q ≡ 3 (4), q ≥ 7 (Prop 3.3(1)) ⇒ n+4 ∈ 3^ℕ·{primes ≡ 1 (4)}; splitting by 3^e is fine. Escape count for criterion (1) at 10⁵ (5 339) reproduced. |
| Thm 4.2 E(x) ≪_B x(log x)^{−B} | PROVED given sieve | **CORRECT** | Re-derived: upper-bound (Brun/Selberg) sieve of dimension κ_K = Σδ_i with residue sets Ω_p = ∪_{i: p∈P_i}{L_i ≡ 0}; ω(p) = #{i : p ∈ P_i} off resultant primes (16 ≡ 1 only for p ∣ 15, etc.); primes with ω(p) = p may be dropped (superset). δ's right (1/2 ×6, 1/φ(4k) ×2); side conditions automatic for q ≤ x^c, n ≥ √x. Routine; label "given a textbook sieve" is honest. No prior exceptional-set bound for (S) found (FOREST_CONNECTIVITY Prop 4.2: density 0, primes only). |
| §5 (S′) and "obvious routes stop" | PROVED/classical | **mostly CORRECT** | (S′) ⟺ (S) by Thm 2.1. Item 3's "Pell/Vieta-type involutions on words do not exist" is an Assessment, not proved: relabel. |
| §6 EVIDENCE (crit8 to 10⁸, families, minA) | CERTIFIED | spot-checked | crit8 to 3·10⁶ reproduced exactly; f4 witnesses all verified (below). Rest not re-run. |

## 2. Falsifier table — entries checked
* **F1** correct: every PROVED positive statement lives in classes avoiding squares (n ≡ 5 (8), n ≡ 2 (3), n ≡ 3 (9),
  classes off 𝔈); Thms 4.1/4.2 are upper bounds on sets containing squares.
* **F2** essentially correct, two factual slips. (i) "the words (8,3), (u,v) = (3,4), (3,12) are among the 57 of Thm 3.6"
  is **false for (3,12)**: no uv-word (3,12) is among the 57 or the 77 (`cover_check.txt`, `cover_words_1441440.txt`).
  Harmless (3.1(c) is proved directly), but fix the sentence. (ii) §6/F2 list prime 13 among the "4∣u or 4∣v"
  misses in a sentence about n ≡ 1 (8); 13 ≡ 5 (8) (the `families` output reports n ≡ 5 (8) separately). Fix.
* **F3** correct (no primality used anywhere; 105 wordless).
* **F4** correct: `f4_witnesses.txt` re-verified independently: 334 distinct values, every word satisfies
  tuv − u − v = n, letters ≥ 2, A = tu − 1, (A/n) = −1; the only screen value without a witness is 105 (wordless).

## 3. Labels / overclaims
* Summary bullet 1 ("So (S) is a purely 2-adic statement …") and §5 present Thm 2.1 as the lane's discovery. It is
  DK Thm 4.5 / §8.1 in a new one-line form. Relabel "PROVED (new compact form of DK Thm 4.5; cf. FOREST_DEEP_FABLE
  Thm A, LOWERTAIL_ROUND2_FABLE Thm 1)".
* No HOT LEAD claimed; no overclaim about ES. "No finite covering can remove the 24 square classes" is a theorem
  (Cor 2.2 + Prop 3.5); "whether the four classes ≡ 6 (7) are finitely coverable is open" is honest.
* Net new content: Thm 3.6 (certified covering mod 840; 4 non-square stubborn classes, all ≡ 6 (7)), Thm 3.1(c),
  Thms 4.1/4.2 (routine sieve bounds for the (S)-exceptional set incl. composites), and the compact form of Thm 2.1.

## 4. Required fixes (priority order)
1. Thm 2.1 + summary + §5: state the priority (DK Thm 4.5 & §8.1; FOREST_DEEP_FABLE Thm A; FOREST_CONNECTIVITY Thm 2.1;
   LOWERTAIL_ROUND2_FABLE Thm 1; z1_legendre_levels Prop 1). Only the product form 8∣(n+t)tuv is new.
2. Credit Thm 3.1(b) (bsG_primes_trivial / DISCOVERIES Prop 8.1), Prop 3.3(1),(3),(5) (FOREST_CONNECTIVITY
   Prop 3.1(iii)) and Prop 3.5 (HJ_DEEP Lemma 3.2; invol_sign_identities Prop S).
3. F2: delete "(3,12)" from the "among the 57" sentence; move 13 out of the n ≡ 1 (8) list.
4. Prop 3.3(6): B ≥ 8 because 4 ∣ 3n+1 (n ≡ 1 (8)) forces 4 ∣ B, not "B even and ≡ 2 (3)".
5. §5 item 3: "no Pell/Vieta involutions" → Assessment.
6. (optional) Thm 3.6: note that the 57-word list is sufficient but not minimal.

## 5. Verdict: **ACCEPT-WITH-FIXES**. All PROVED statements re-derive. Thm 3.6's certificate re-checks independently
with 0 uncovered classes. Fix 1 (priority of Thm 2.1) is mandatory before FRONTIER records anything from this memo.
