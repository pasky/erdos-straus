# REVIEW_SDEEP — hostile cross-review of Z64_SDEEP.md (branch side-agent/z64-sdeep @ f78e342d4)

Reviewer: Opus standing in for the cross-model reviewer (OpenAI quota exhausted). Brief: xreview_z58 with z58 → z64.
ES and (S) remain OPEN; the memo claims neither. Scripts `scripts/z64_xrev_s_{ks0,cells,small,u4}.py` (PARI via cypari2,
sympy; none share code with `scripts/z64_sdeep_*`). All runs under `ulimit -v 4000000`, `timeout`.

## 1. Per-claim table

| claim | memo label | verdict | check |
|---|---|---|---|
| Lemma 1: (d/n) = ((tr γ ± 2)/n) on Γ₀(n); χ_n(A) = (t(u+v)/n) | PROVED | **CORRECT** | Re-derived: ad ≡ 1 ⇒ tr ± 2 ≡ (d ± 1)²d⁻¹; γ_w = [[A,t],[n,A*]], det = AA* − tn = 1, tr + 2 = t(u+v). Independent: 265 362 coprime words, all n ≡ 1 (4) ≤ 6·10⁴, 0 mismatches (`cells.py`). |
| Lemma 1 class-invariance: genus character iff s ≢ 0 (mod 4) | PROVED + CERT | **CORRECT** | Genus argument re-derived (D₁ = ε(s+2) ≡ 1 (4) for s odd; D₁ = s+2 ≡ 0 (4) for s ≡ 2 (4), subtracted term (D/4)y² ≡ 0 mod D₁ since (s−2)/4 ∈ ℤ; Kronecker (D₁/·) is a character mod \|D₁\|; needs gcd(n, s+2) = 1, the Lemma-1 hypothesis). Z2825 pair re-verified with PARI: [17,2,−2] properly represents 13 via (1,−1) giving [13, 6 mod 26, ·] ⇒ ~ [13,6,−2]; signs (14/13) = +1, (14/17) = −1. `genus_check.py` re-run: 3 089 / 0 and 1 901 / 1 155 — identical. |
| Sign dictionary "χ_n(A) = χ_n(uv)" | PROVED, prior | **CORRECT-WITH-FIX** | Needs gcd(uv, n) = 1 (⟺ gcd(u,v) = 1; automatic at primes). Fails at composites: n = 21, (3,3,3): χ(A) = (8/21) = −1, χ(uv) = 0; 66 067 such words ≤ 6·10⁴. FOREST_DEEP_FABLE Thm A states the hypothesis; the memo dropped it. Other dictionary items correct. |
| Lemma 2: χ_n on L₃(n) = n-free mod-4 cell function σ, C₊ = 5 cells; (S) ⟺ ML on L₃ ≠ ∅ | PROVED (DK §8.1 restated) | **CORRECT; PRIOR** | 20 admissible cells mod 4; on all 1 280 admissible cells mod 16, σ = DK five-slot predicate = SDEEPF's 8∣(n+t)tuv (0 disagreements); 375 274 words ≤ 6·10⁴ vs Jacobi, 0 mismatches. Credit to DK §8.1 is given; "character blindness" is a name for a restatement (the memo says so). L₃ = ∅ only at 5, 105 among non-squares ≤ 2·10⁵ (`small.py`). |
| Prop 3: whole-fibre χ_n data = congruence data | PROVED | **CORRECT** | N ≡ u (mod n) ⇒ χ_n(N) = χ_n(u); (q/n) = (n/q) = (−u/q). Needs gcd(u,n) = 1 (stated). Restates CLASS_FORCING Thm 2.1 (credited). |
| Prop 4 (i): strip tn ≤ AA* < (t+1)n meets AA* ≡ 1 (n) only on AA* = tn+1 | PROVED | **CORRECT; PRIOR setup** | Trivial. The γ_w, form [n, A*−A, −t], disc T²−4 and the box modular-hyperbola picture are WINDMILL_REDUCTION §5.2–5.3 — cite. |
| Prop 4 (ii)–(iii), KS2 | heuristic / Assessment | honest | KS2's kill condition was true by construction; the memo says so explicitly. Accept as a scoped no-go, not an experiment. |
| §4(a) no polynomial word family for d·m²+k, k ≥ 0, two shapes | PROVED | **CORRECT** | Re-derived: shape 1 forces k = −d(x − β/d)² − αβ/d; shape 2 forces k = −dy² − v. DK §9.2 credited. Only these two shapes. |
| KS0 adversarial census: 0 failures, 19 179 n ≤ 9·10¹³; min N₋ = 65 (full rows) | CERT/EVIDENCE | **REPRODUCED** | Independent PARI enumeration (`ks0.py`): all 357 screen rows (F mode, all 5 columns) 0 mismatches; 14 full rows (4 smallest + 3 random of (a) and of (b), n up to 7.5·10¹³) all 5 columns identical; 400 random early rows (385 (c), 15 (d′)): least u with a −1 word and first word-u identical. File stats re-derived: 1 248 / 2 310 / 14 997 / 624 rows, all n ≡ 1 (4) non-square, min N₋ 69 / 65, min pairs 112 / 103, min N₋/\|L₃\| 0.466, max n 8.78·10¹³; 21 values of d. |
| KS1: NAP dead on registered dictionary | CERTIFIED | **REPRODUCED** | `z64_sdeep_words.c` (37 116 primes, cell-law and Lemma-1 failures 0) + `z64_sdeep_ks1.py` re-run: report byte-identical (modulo the PARI banner line). |
| Abelian law: #(−1 pairs with min(u,v) ≤ 4) odd ⟺ (3/p) = −1 | EVIDENCE | **REPRODUCED** | 14 085 primes p ≡ 1 (8) ≤ 7·10⁵, 0 violations (`u4.py`, independent). Not proved; label fine. |
| Prime-A failures 20521, 21841, 589681 | EVIDENCE | **PARTLY REPRODUCED** | ≤ 7·10⁵ exactly {20521, 21841}, and 589681 fails (N₋ = 3, 1, 5 pairs). Range 7·10⁵–2·10⁷ not re-run. |
| Census: N₋(21841) = 1 of 10 pairs; min N₋ = 1 at 17, 41, 21841 | EVIDENCE | **REPRODUCED** | `small.py` (p ≡ 1 (8) ≤ 2·10⁵): (1,1,17), (1,1,41), (1,10,21841). |

## 2. Pre-registration (checkpoint 7bd1196af) — honoured, with disclosed deviations
* KS0: families (a)–(d) and the kill criterion match the registration; |k| ≤ 48 instead of 60, the added (d′), and the
  secondary criterion's scope are disclosed. No failure, so the kill did not fire. OK.
* KS1: dictionary as registered (h(−3p) bit implemented as h(−3p)/2, h(−3p)/4 — disclosed); abelian modulus 13440
  run as registered. The implemented test (best congruence predictor of f ⊕ ρ, in-sample class majority) is more general than
  the registered "c ≡ ρ or ρ + 1". **Literal reading:** the registered kill required "no pair ≥ 99 %"; one pair reached
  0.9981, which under the registration's survive clause means "examine". The memo did examine it: ρ = (3/p)₄·h(−3p)/4 is
  itself constant on its domain (a dictionary redundancy), gain 0. Required: say in §3 KS1 in one sentence that the
  survive clause was triggered and resolved this way (now only implicit).
* KS2: registered as "decided by proof"; the kill condition is a tautology and the memo admits it. OK.

## 3. Falsifier table — entries checked
F1 correct (σ-blindness at squares; −1 sub-counts vanish at m²). F2 correct (the 12 R₈ rows re-enumerated: all have −1
words). F3 correct (284 composite R-zeros with −1 words, 105 vacuous; minima 1 pair at 5481 and 13041 reproduced).
F4 correct (14 + 38 + 12 screen primes re-enumerated; 21841 ≡ 1 (mod 840)). No HOT LEAD is claimed, so nothing to break.

## 4. Labels / overclaims
* §6/§8 say "Lemma 1 … new in the repo". True for the one-line identity ((tr+2)/n) as far as `git grep` shows, but the
  objects γ_w, f_w = [n, A*−A, −t], disc s²−4 and the modular-hyperbola box are WINDMILL_REDUCTION §5.2–5.3. Also
  relate it to BRAINSTORM/y1_gamma8_trace Fact G2, which claims no function of the SL₂(ℤ)-class (incl. the genus of f_w)
  can be the sign. There the matrix is M_w = S_vS_tS_u (trace n − t) and the counterexample crosses n mod 4 (n = 37 vs 39). So
  there is no contradiction, but Lemma 1(a) is a positive genus-character statement on n ≡ 1 (4), s ≢ 0 (4), and it
  sharpens G2's reading. Say so.
* "Lemma 2 (character blindness)" and the §9 claim "it is not a character problem" are labelled Assessment, and that is
  where they belong. They are true for the *values* of χ_n on L₃(n), which is how §2 is scoped. Keep that scope in §8's
  FRONTIER text.
* Verdict NARROWED follows: nothing proved advances (S); all kill tests honest.

## 5. Required fixes (priority order)
1. Sign dictionary (§1): add "when gcd(uv, n) = 1 (automatic at primes)" to χ_n(A) = χ_n(uv). Counterexample n = 21, (3,3,3).
2. Credit WINDMILL_REDUCTION §5.2–5.3 for γ_w / f_w / modular-hyperbola box (Lemma 1 setup, Prop 4), and relate
   Lemma 1(a) to y1_gamma8_trace Fact G2 (see §4).
3. KS1: one sentence that the registered survive clause (a pair ≥ 0.99) was triggered by a constant-ρ redundancy and
   resolved (gain 0) before the DEAD verdict.
4. (cosmetic) Prime-A: say that the decade means c(p) are means over p ≡ 1 (8) and that failure ⇔ every −1 pair has
   both A, A* composite. This is what the script computes and what I re-checked.

## 6. Verdict: **ACCEPT-WITH-FIXES** (all fixes minor; no proof gap affects any PROVED label after fix 1).
