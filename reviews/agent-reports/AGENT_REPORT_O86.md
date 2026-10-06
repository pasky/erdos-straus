# AGENT REPORT O86 — `paper/es-coverings-note.tex` (coverings note)

Branch `side-agent/coverings-note`. Deliverable: `paper/es-coverings-note.tex` / `.pdf` (amsart, 20 pp,
clean two-pass pdflatex build: no errors, no undefined references, no overfull boxes). README entry added.
Author/date block copied from `es-window-note.tex` ("Anonymous"; "Draft …; internal checks only, not
externally refereed"). No new mathematics; no new computations except a replay of the two r=13
certificates (`mordell_check.py`: both CERTIFICATE OK).

## Structure and source of every labelled statement

| paper | statement | source | label in paper |
|---|---|---|---|
| Lemma 2.1 | every n≥1 in an ET class has the explicit positive solution | ET §§2,10; MORDELL §0 (R80 repair, O85 degree correction) | PROVED |
| Cited Thm 2.2 | ET Prop 1.9 converse direction | ET p. 8 | cited |
| Lemma 2.4, Prop 2.5 | accumulation sets ⊂ Ẑ^×; cofinite polynomial covering of 𝒫 ⟺ 𝒫′ has no sterile point | written here from MORDELL §0 + R80 #8 | PROVED (elementary) |
| Remark 2.6 | for a single point only "sterile ⇒ no covering"; modulus-≤Y version | R80 #8, MORDELL Consequence of 4.1 | — |
| Remark 2.7 | heights / finite intersection; sterile set closed | TYPEI2 Thm A(iii) proof | — |
| Prop 3.1 | square points sterile (x=1 elementary; general via Mordell–Schinzel as quoted in ET p. 8) | ET p. 8; notes Prop 77.3 idea | PROVED; known |
| Cited Thm 3.2 | Theorem C / C1 | POINTWISE_SIZE §2 | CONDITIONAL (H); novelty partial per audit |
| Remark 3.3 | targets/candidates not square-mimicking; rigidity reading | MORDELL §4 (R80 #9) | Assessment |
| Thm 4.1 | C(5)=10 | TYPEI Thm 6.1 | PROVED |
| Thm 4.2 | Theorem A (i) PROVED, (ii) CONDITIONAL H, (iii) X_r=∞ ⟺ Type-I-sterile point PROVED; C*=X_r under H | TYPEI2 Thm A (R69 D1/D4/D5 wording) | as stated |
| Thm 4.3 | ck_min > g·n_p i.o.; ≥ n_p^{2−ε} | TYPEI Thm 2.1 | CONDITIONAL (H) |
| text after 4.3 | 539 / >3000 (H); Σ_11 coverings height >3000 | TYPEI Cor 6.4 (R31 D1) | CONDITIONAL / CERTIFIED (two engines) |
| Lemma 4.4 | square-off-r points: v_r(c) odd | TYPEI2 L2.1 | PROVED |
| Prop 4.6 | (a) no square certificate for r≡7(8); (b) r≡3(8) killed | TYPEI2 L3.1, P4.1 | PROVED |
| Lemma 4.7 | f-graded reduction, f-bound ⇒ height bound; finiteness only for finite role depth (w=−71 example) | TYPEI3 L1.1–1.2 (R72 self-review #1) | PROVED |
| Comp 4.8 | no certificate at x̂_9 with f<10¹² (two engines <10¹¹, one engine [10¹¹,10¹²)); r=23 two engines, r=31,47 one, f<10¹¹ | TYPEI3 C2.1, C2.3 (R72 D4); TYPEI2 C3.2 | CERTIFIED, engine scope stated |
| Cor 4.9 | heights >1.32·10¹² etc.; C(7)>1.32·10¹² under H | TYPEI3 C2.2 | CERTIFIED / CONDITIONAL |
| Lemma 4.10, Prop 4.11 | Vieta descent; t≥5, α+2γ≥7 (level 5 credited to reviewer) | TYPEI3 L5.1, C5.2, P5.3–5.5 | PROVED (sketch + pointer for 5.3–5.5) |
| Prop 4.12 | Type-I-sterile set of Σ_7 closed, nowhere dense; scope weakened per R72 #3 | TYPEI3 P3.1 | PROVED |
| Remark 4.13 | measure route; μ(U_{10¹⁰})≥0.6086 incl. depth truncation; o(2^T) insufficient | TYPEI3 Rem 4.1 (R72 D2, #2, #5) | PROVED reduction / EVIDENCE |
| Conj 4.14 | x̂_9 Type-I-sterile | TYPEI2 Conj 3.4 | CONJECTURE |
| Thm 5.1 | r=13 finite-exception theorem incl. (c) | MORDELL Thm 3.1 (R80 #1, #3) | PROVED by finite computation; novelty = packaging of Salez (R80 #6) |
| §5.2 | T-generic boxes; II1/I4/II2 rigid forms | MORDELL §2.1 (R80 #10; full T={17} table re-derived in R83 Claim A) | PROVED with stated re-derivation scope |
| Comp 5.2, Cor 5.3 | x* in no class of modulus ≤10⁶ (two engines); rigid II levels (scope: 11³13³ and exponent-4 levels one engine) | MORDELL Comp 4.1, §4.1 (R80 #4, #5) | CERTIFIED / PROVED |
| Conj 5.4 | x* sterile; consequence stated as implication only | MORDELL Conj 4.2 (R80 #8) | CONJECTURE |
| Lemma 6.1 | box types; √Q empty; Q, P odd levels; no level 0 | MORDELL17 L1.1–1.3, C2.4 | PROVED |
| Prop 6.2 | boxes = ES points at 17^k; U never new; centres −a/b | MORDELL17 L2.1–2.3, 5.1, 5.2 | PROVED |
| Comp 6.3 | covered fractions through level 5 (67.72% uncovered), two engines; brute-force completeness check; x(5) ∉ classes M≤10⁶ | MORDELL17 Comp 3.1 (R83 r1); MORDELL Comp 5.1 | CERTIFIED |
| Thm 6.4 | tail criterion with 56561/83521 (exact, R83 m4) | MORDELL17 Thm 4.1 | PROVED |
| Cor 6.5 | no finite polynomial covering of Mordell-hard n_p=17 primes | MORDELL17 Cor 4.2 (R83 m5) | CONDITIONAL on the hypothesis of Thm 6.4 |
| Conj 6.6 | C_5 has a sterile point | MORDELL17 Conj 4.3 | CONJECTURE |
| status para, (6.1), Assessment 6.7 | non-explicit convergence (PROVED via ET Prop 1.7 proof, R83 m1); P critical; P-count; K³ fit (EVIDENCE); discrete-log; digit-set test fails | MORDELL17 §4, §6 (R83 n4, n5, n6, r2) | PROVED / EVIDENCE / Assessment |
| §7 | six open problems | — | — |

## Points for the referee

1. **Prop 2.5 is written here** (the sources only state the clopen/compactness remark and R80's
   corrected implication). Please check the derived-set argument (primes are not units of their own
   ℤ_p, hence accumulation points rather than closure) and the use of ET Prop 1.9 in (b).
2. **Prop 3.1 general case** relies on the Mordell–Schinzel theorem as quoted in ET p. 8 (neither
   original was accessed). Only x=1 is proved from scratch.
3. **Problem 1's "equivalently"** (sterile non-square point ⟺ clopen Σ without square points with no
   finite covering) uses that the square points form a closed set; check.
4. Bibliographic details of Browning–Elsholtz (Illinois J. Math. 55, 2011), Coppersmith–Howgrave-Graham–
   Nagaraj (Math. Comp. 77, 2008), Nicolas–Robin (Canad. Math. Bull. 26, 1983) and Lenstra (Math. Comp. 42,
   1984) are from memory and were not checked against the publications (BE's title matches ET's ref. [8]).
5. Prop 4.11 (levels 5–6 empty) and the classification half of Lemma 6.1 are given as sketches with
   precise pointers, to keep the note at 20 pages; full proofs are in TYPEI3 §5 and MORDELL17 §1.
6. Length is 20 pp, the upper end of the brief; §4 could be shortened by dropping Thm 4.3 if needed.

## Not done
No new mathematics; nothing beyond the reviewed sources is claimed. ES is stated as open throughout.
