# R282 — hostile review of O271 SYNTHESIS_SPARKS9 (synthesis IX)

**Repairs applied** (author quiet ≥ 2 h after its final status commit; all marked "(R282 repair)"): SYNTHESIS_SPARKS9.md — new
Lemma 2.0 (BL's class at level points: χ_{−t} for n ≡ 1 (4), −χ_t for n ≡ 3 (4); D1) and the n ≡ 1 (4) qualifiers in (I2), §4, §5;
collider correction of SHARP 2 in (I1), Prop 1.3, its Assessment, §4, §5 (D5); D3, D6, D7/D8, D11, D2 minors. Memos
s9_level_bm_character, s9_union_thinning, s9_disproof_class_layer (D10–D12), s9_fibration_level; BRAINSTORM/README s9 rows.
NOT edited: reviews/agent-reports/AGENT_REPORT_O271.md (SHARP 1/2 wording there still carries D1/D5 — parent should read this
review instead). D4 left as a note; D9 applied to the literature memo.

Reviewer branch: side-agent/review-synth-nine (merged side-agent/synthesis-nine at 572d541b; BRAINSTORM/README.md conflict
resolved by keeping both the z39 and s9 tables). From-scratch scripts: `scripts/review_r282_*`. ES is not solved anywhere.

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Prop 2.1 (a)–(d) (M^{lev}_t ≥ 0, = 0 at squares) | SOUND (as statements about the defined quantity M^{lev}) |
| Prop 2.2 (∃ 4 \| t with M^{lev}_t > 0 ⟺ non-square; witness t ≤ 4ℓ(n)) | SOUND |
| "in level coordinates BL's class IS χ_{−t}" (I2, §2 Reading, §4, §5, memo, README, report SHARP 1) | GAP → SOUND-AFTER-REPAIRS (unproved in the document; true only for n ≡ 1 (4); for n ≡ 3 (4) it is −χ_t, even) — D1 MAJOR |
| 0 failures over 499 500 odd non-squares ≤ 10⁶; 73.4 % witness-level hit rate | SOUND (reproduced exactly) |
| Lemma 1.1, Cor 1.2 (k-union ⟺ a word coordinate ≡ 0 (k)) | SOUND (holds for all n ≥ 1, k ≥ 2) |
| sign remark (4 \| t or 4 \| v ⇒ σ = −1) | SOUND |
| Prop 1.3 / SHARP 2 numbers (+0.37/+0.39; 0.03/0.01 given log W; 0.59×) | SOUND (reproduced) |
| SHARP 2 interpretation ("the shared factor is the size of W(p)") | GAP — collider artefact; disjoint size controls leave ≈ 0.35 (D5 MAJOR) |
| Lemma 3.1 (plain ℓ² certificate ⟺ m̄² > (\|G\| − 1)V, then all classes) | SOUND |
| Lemma 3.2 | SOUND (tautology, labelled as such) |
| Prop 3.3 / 3.4 (Janson, level-Poisson) | SOUND as EVIDENCE (D7, D8 minor) |
| literature map (Crocker 1971, Pan 2011, Erdős–Tetali 1990, Ghosh–Sarnak) | SOUND (D9 minor) |
| s9_no_fixed_integer (Hecke positivity pushes against ES) | SOUND (Assessment + PROVED inequality) |
| s9_fibration_level | SOUND-AFTER-REPAIRS (D1 propagates; collapse = Assessment, fine) |
| s9_disproof_class_layer / corollary scope after self-review | SOUND-AFTER-REPAIRS (D1, D10–D12 minor) |
| labels overall | SOUND after D1/D5 relabels; no FATAL defect; ES not claimed |

No FATAL defects. Two MAJOR (D1 dictionary scope/proof; D5 statistical interpretation), ten MINOR.

## Claim A — Prop 2.1, Prop 2.2 and the "BL's class is χ_{−t}" dictionary

**Re-derivation.** For 4 | t, D = −t ≡ 0 (4) is a discriminant, so χ_{−t} = (−t/·) is a real character mod t with
χ_{−t}(−1) = sign(D) = −1. (a) d ≡ −1 (t) ⇒ χ(d) = −1; #{d | N : χ(d) = −1} = (τ − σ_χ)/2 since gcd(N, t) = 1; positivity ⟺ an
inert prime factor (multiplicativity: σ_χ(ℓ^e) = e + 1 iff χ(ℓ) = 1). (b) orthogonality, trivial. (c) ℓ | 1 + tm² ⇒ ℓ odd, ℓ ∤ tm,
−t ≡ (m⁻¹)² — fine. (d) Dirichlet's formula, fine (gcd(N, t) = 1). Prop 2.2: n = n₀s² with n₀ > 1 squarefree; ℓ ↦ (n₀/ℓ) is a
non-principal character mod 4n₀ on odd primes, so infinitely many odd primes ℓ ∤ s with (n/ℓ) = −1 exist; multiples of 4 in
[4, 4ℓ] cover every residue mod ℓ (and −n⁻¹ ≢ 0, so in fact t ≤ 4(ℓ − 1)); (−t/ℓ) = (n⁻¹/ℓ) = (n/ℓ) = −1. Burgess applies to the
least ODD prime non-residue (restrict the Vinogradov argument to odd integers: Σ_{m≤x, m odd} χ(m) = S(x) − χ(2)S(x/2) = o(x));
GRH: Bach's "least prime outside a proper subgroup of (ℤ/8n₀)^*" gives an odd prime ≪ log² n. Both asides are fine.

**From-scratch checks.**
* `scripts/review_r282_levelbm.c` (own primality, Euler criterion, own witness search, own (★)-divisor scan): all 499 500 odd
  non-squares ≤ 10⁶: 0 failures, max ℓ = 71; witness level carries a (★) word for 366 491 = **73.37 %** (≤ 2·10⁵: 72.13 %) —
  matches the author's 73.4 % / 72.1 %. (Author's square counts 223 / 499 exclude n = 1; I count 224 / 500. Cosmetic.)
* `scripts/review_r282_levelbm2.py` (own Kronecker symbol; NO use of the witness formula): for every odd n ≤ 20 001, brute
  force over 4 | t ≤ 400 for an inert prime factor of tn + 1: found at every non-square (max minimal level 72), never at a
  square; D⁻_t(m²·t + 1) = 0 for t ≤ 40; Prop 2.1(a) inequality, parity of τ − σ and "τ − σ > 0 ⟺ inert factor" for all odd
  n < 400, t ≤ 120; χ_{−t} periodic mod t, multiplicative, odd for t ≤ 200. Odd squares ≤ 10⁶ × 4 | t ≤ 400: 0 inert levels.
* `scripts/review_r282_blevel.py` — **the dictionary itself**, by evaluating BL's α = (−x/z, −y/z) at the level-slicing rational
  points (C = t/4, u = (δ+1)/t, v = (N/δ+1)/t, α(P) = (−v/n, −v/u)) with an explicit odd-p Hilbert symbol, p < 400, t ≤ 60:
  p ≡ 1 (4): inv_p α = χ_{−t}(δ) at 2928/2932 points; p ≡ 3 (4): inv_p α = **−χ_t(δ)** (EVEN character) at 3052/3060 points
  (χ_{−t}(δ) only at 1074/3060). All 12 mismatches are p | t (non-generic); 6 points with p | δ + 1 skipped.

**Hand proof of what the dictionary really is.** For p ∤ t(δ+1)uv-denominators: inv_p α(P) = ((−v/u)/p) = (−uv/p), and mod p,
N ≡ 1 gives uv ≡ (δ + 1)²/(δt²), so inv_p = (−δ/p) = (−1/p)(δ/p). Quadratic reciprocity with tp ≡ −1 (mod δ):
(p/δ) = (−t⁻¹/δ) = χ_{−t}(δ), so **inv_p α(P) = (−1/p)·(−1)^{(δ−1)(p−1)/4}·χ_{−t}(δ)**, i.e. χ_{−t}(δ) for p ≡ 1 (4) and
−χ_{−4}χ_{−t}(δ) = −χ_t(δ) for p ≡ 3 (4). The BM factor 1 + inv_∞·inv_p is then 1 − χ_{−t}(δ) resp. **1 + χ_t(δ)** — for
p ≡ 3 (4) it is the {1, χ_t} projection, which never vanishes (σ_{χ_t}(N) > −τ(N) as χ(1) = 1). (For composite n the same
computation with the Jacobi symbol gives the same n mod 4 dichotomy at the product of the inv_ℓ, ℓ | n, at generic points.)

### Defects for Claim A
**D1 (MAJOR — overclaimed/unproved dictionary).** Locations: §1 (I2) "Answer (§2): one odd quadratic character χ_{−t} ∈ O_t …";
§2 "Reading" ("level slicing … χ_{−t}(d) (Prop 2.1)"); §4 row "Thm K × BM class … PROVED"; §5 first bullet; memo
`s9_level_bm_character.md` title + "PROVED dictionary"; BRAINSTORM/README s9 row label PROVED. (i) Nothing in §2 proves that
χ_{−t} is BL's class: Prop 2.1 only DEFINES M^{lev} as the {1, χ_{−t}} part; no local invariant is ever computed. (ii) The
claim is false as stated for odd n ≡ 3 (mod 4): there BL's class at the level points is the EVEN character χ_t ∈ E_t (with a
sign), see above. Prop 2.1/2.2 remain correct as statements about M^{lev}, but the sentence "the BM layer is χ_{−t} ∈ O_t" and
"Prop 2.2 proves the BM relaxation at every non-square" need the restriction n ≡ 1 (4) (for n ≡ 3 (4) the true BL factor is
trivially positive, so nothing is lost for ES). *Repair:* add a Lemma 2.0 with the inv_p computation above (generic points
p ∤ t, p ∤ δ + 1), state "for n ≡ 1 (mod 4) BL's class at level t is χ_{−t}; for n ≡ 3 (mod 4) it is −χ_t", restrict the
"twin of O268 Thm 1.1" claims to n ≡ 1 (4), and relabel the dictionary "PROVED (generic points, n prime ≡ 1 (4))".

**D2 (MINOR).** §2 Check: "odd squares … 223 squares … 499 squares" — these exclude n = 1 (224 / 500 odd squares ≤ 2·10⁵ / 10⁶).
Say "odd squares > 1". Also "t ≤ 4ℓ" can be sharpened to t ≤ 4(ℓ − 1).

## Claim B — Lemma 1.1, Cor 1.2 (k-union = some word coordinate ≡ 0 (mod k)), sign remark
Verdict: **SOUND** (Lemma 1.1, Cor 1.2 hold for every n ≥ 1, not only odd n, and every k ≥ 2).

**Re-derivation.** Lemma 1.1: (T, U, 1) ∈ W(cn) ⟺ U(T − 1) = cn + 1; with T = cs, c(n + s) = (cn + 1) + (cs − 1) and
gcd(c, cs − 1) = 1 give cs − 1 | n + s; inverse as stated; U = cg − 1 ≥ 1 since (c, g) = (1, 1) forces n = −1. Cor 1.2: c = 1 line
n + a + b = kabd ⟺ word (kd, a, b). b = 1 line cn + a + 1 = kacd ⟺ (kcd, a, 1) ∈ W(cn) ⟺ (Lemma 1.1, s = kd) (c, g, kd) ∈ W(n);
conversely (t, u, kd) ∈ W(n) ↦ (c, a) = (t, tu − 1): cn + a + 1 = t(n + u) = t·v(tu − 1) = kacd since n + u = v(tu − 1). The
side condition cs > 1 is automatic for k ≥ 2. u ↔ v symmetry of W(n) gives "k | v ⟺ k | u (for some word)". Correct.

**From-scratch checks.** `scripts/review_r282_lines.py 300 12`: for ALL n ≤ 300 and 2 ≤ k ≤ 12, both lines decided from their
original (a, b, c, d) definitions vs. word coordinates; Lemma 1.1 bijection for n < 120, c ≤ 6 — 0 mismatches (3 300 cases).
`scripts/review_r282_k8.c` (own word enumeration): k = 8 union fails at 35 primes 3 ≤ p < 8000 (22 ≡ 1 (4)), i.e. 34 primes
5 ≤ p < 8000 incl. 131, 241 — matches SPARKS8; k = 4: union never fails for p < 70 000, b = 1 fails exactly at 193, 2521, 66529.
Sign remark ("4 | t ⇒ σ = −1" three-line proof), re-derived: X = tu − 1 ≡ 3 (4), n ≡ 1 (4) so (X/n) = (n/X); XY = tn + 1
gives n ≡ −t⁻¹ (mod X), so (n/X) = (−1/X)(t/X) = −(t/X). With t = 4·2^e·C′ (C′ odd): (C′/X) = (X/C′)(−1)^{(C′−1)/2} =
(−1/C′)(−1)^{(C′−1)/2} = +1, and (2/X) = +1 when e ≥ 1 since then X ≡ −1 (8). So σ = −1. Correct (the document's sketch
"X ≡ −1 (mod C′) ⇒ (C′/X) = 1" silently uses reciprocity with the sign (−1/C′)·(−1)^{(C′−1)/2} = 1; fine).

### Defects for Claim B
**D3 (MINOR).** §1 "Checks": "the k = 8 union fails at exactly 34 primes < 8000" — p = 3 also fails; say "34 primes
5 ≤ p < 8000" (as SPARKS8 does) or "35 odd primes < 8000".
**D4 (MINOR).** Cor 1.2 is stated "for every odd n" but the proof never uses oddness (verified for all n ≤ 300); harmless.

## Claim C — Prop 1.3 / "SHARP 2" statistics (union correlation)
Verdict: numbers **SOUND (reproduced)**; the headline interpretation "the shared factor is the size of the common set" is
**GAP (collider artefact)** — see D5.

**From-scratch reproduction.** `scripts/review_r282_union.c` enumerates ALL words of all n ≤ X by a triple sieve
(t, u, w) ↦ n = w(tu − 1) − u (0.7 s for 10⁶, 20 s for 10⁷); `scripts/review_r282_union_stats.py` /
`review_r282_union_stats2.py` (own controls). Results, primes p ≡ 1 (4):
* census: (★) fails at exactly 9 primes ≡ 1 (4) ≤ 10⁶ and 14 ≤ 10⁷ (409 … 712321, 1134241, 1724209, 1726201, 5212561, 8813281);
  b = 1 fails at 193, 2521, 66529; the 4-union never fails ≤ 10⁷. ✓
* corr(A, B) standardised in (2000-prime window) × (p mod 24): **0.367 (≤ 10⁶), 0.387 ((10⁶, 10⁷])** ✓.
* A = 0: B/E[B | cell] = 0.60 (9 primes) / 0.59 (5 primes) ✓ — but these rest on 9 resp. 5 primes (see D6). Bottom 1 % of
  A/E[A]: 0.71 / 0.75 ✓.
* partial corr given p mod 840, log p, log 47-smooth parts of p ± 1: 0.353 / 0.393 ✓; + log W: **0.039 / 0.011** (author
  0.031 / 0.011) ✓. W/L² mean 0.959 / 0.917, 1 % quantile 0.525 / 0.532, min W (p > 10⁵) 43 / 45, U/W 0.423 / 0.436 ✓.
* ES-five count F checked = #{σ = −1 words} by brute force (Legendre) for all p ≡ 1 (4) < 3000 ✓ (supports the cited sign).

**Collider check (new).** W(p) CONTAINS the A- and B-words (U/W ≈ 0.43), so regressing on log W partly conditions on A + B
itself, which mechanically drives the partial correlation of two summands towards (and below) zero. Controlling instead
for size measures DISJOINT from A ∪ B (controls: p mod 840, log p):

| extra control | ≤ 10⁶ | (10⁶, 10⁷] |
|---|---|---|
| none | 0.421 | 0.449 |
| log W (author's) | 0.033 | 0.006 |
| log(W − U) (words with no coordinate ≡ 0 (4)) | **0.346** | **0.353** |
| log W₊ (σ = +1 words) | 0.383 | 0.401 |
| log(W₋ − U) (σ = −1 words outside the union) | 0.343 | 0.357 |
| log W₋ (superset of A ∪ B, larger share) | −0.189 | −0.225 |

So a size variable that does not contain A, B explains only ≈ 15–20 % of the correlation; the residual ≈ 0.35 is a genuine
co-movement of the 4-divisible words (both lines) beyond the size of the rest of W(p). The vanishing after log W and the
sign flip after log W₋ are the signature of conditioning on a superset count, not evidence of "one shared size factor".

### Defects for Claim C
**D5 (MAJOR — interpretation not supported by the data).** Locations: §0 (I1) "the whole correlation is the shared size
|W(p)| (partial corr 0.35 → 0.01 after controlling log |W|)"; Prop 1.3 bullet "The shared factor is the size of the common
set"; Assessment "No identity couples the two lines beyond sharing W"; §4 row "union × correlation"; §5 third bullet;
memo `s9_union_thinning.md`; README s9 row. *Repair:* report the disjoint-control numbers above; replace the sentence by
"the correlation is not explained by the size of the rest of W(p) (partial corr ≈ 0.35 given log(W − U)); the drop to
0.01–0.03 given log W is largely mechanical since W ⊇ A ∪ B". The negative conclusion of (iv) ("no negative correlation, no
complementarity") is unaffected — it is in fact strengthened (the two lines co-fail more than size predicts). The "thinning
of one set" picture should be weakened to "both lines are 2-adic subsets of one set and co-vary positively beyond its size".
**D6 (MINOR).** "Primes with A = 0 have B at 0.59× its cell mean" — based on 9 (≤ 10⁶) and 5 ((10⁶, 10⁷]) primes; state the
sample sizes and drop the two-digit precision.

## Claim D — Lemma 3.1, Lemma 3.2, Prop 3.3, Prop 3.4
Verdicts: **Lemma 3.1 SOUND; Lemma 3.2 SOUND; Prop 3.3 / 3.4 SOUND as EVIDENCE (labels correct), with D7–D8.**

**Lemma 3.1 re-derived.** n(g₀) = |G|⁻¹Σ_ψ n̂(ψ)ψ̄(g₀) ≥ S/|G| − |G|⁻¹Σ_{ψ≠1}|n̂(ψ)| ≥ S/|G| − |G|⁻¹√(|G|−1)·E^{1/2}, E =
Σ_{ψ≠1}|n̂|² = |G|Q − S² (Parseval). Certificate > 0 ⟺ S² > (|G|−1)(|G|Q − S²) ⟺ S² > (|G|−1)Q; with S = |G|m̄,
Q = |G|(V + m̄²): ⟺ m̄² > (|G| − 1)V. The bound is g₀-independent, hence certifies all classes. Correct. The F4-tube
consequence (m̄ ≍ log²p, |G| = p − 1 ⇒ V ≲ log⁴p/p) is correct arithmetic; scope repair ("this plain certificate only") is
adequate. From scratch: `scripts/review_r282_l2cert.py` — 20 000 random count vectors on cyclic and product groups
(FFT characters): bound always ≤ n(g₀); "certificate > 0 ⟺ S² > (|G|−1)Q ⟺ m̄² > (|G|−1)V" exact; positivity ⇒ all classes
occupied — 0 violations (7 hits at c = 10⁻¹⁶ were the boundary S² = (|G|−1)Q in floating point).

**Lemma 3.2 re-derived.** P_Ω(R = 0) ∈ |Ω|⁻¹ℤ, so a bound δ < 1/|Ω| forces 0; with δ ≥ 1/|Ω| one failure is compatible.
π(2N) − π(N) ∼ N/log N gives δ < (1 + o(1)) log N/N. Correct (a tautology, correctly labelled as such).

**Prop 3.3 / 3.4 spot checks (own sieve `scripts/review_r282_levels.c`, all (★)-words of all n ≤ 3·10⁶ by t-outer sieve,
NL = #distinct levels carrying a word).** Number of primes p ≡ 1 (4) ≤ 3·10⁶: 108 283 ✓; (★) zeros ≤ 3·10⁶: 12 = sum of the
author's bin zeros ✓; ≤ 5.37·10⁶: 13 ✓. Mean NL / log p by p-range: (10², 10³] 0.53, (10³, 10⁴] 0.61, (10⁴, 10⁵] 0.75,
(10⁵, 10⁶] 0.89, (10⁶, 3·10⁶] 0.98 — consistent with the author's "0.44 → 0.97, rising" (which was read off M_BM8 bins,
not p-ranges). Also E[NL]/E[R] = 0.40–0.42 at every height.

### Defects for Claim D
**D7 (MINOR — interpretation).** Prop 3.3/3.4 present "level-Poisson" as a third model between Poisson and swap-Poisson. Since
R counts every divisor pair twice (mirror (t, u, v) ~ (t, v, u)), NL ≈ 0.40·R ≈ 0.8·(μ/2) at all heights; the level-Poisson
model is therefore swap-Poisson with ≈ 20 % fewer units, not an independent "granularity". State this (it also explains why
level-Poisson and swap-Poisson totals are of the same order in Prop 3.4).
**D8 (MINOR).** Prop 3.3 bullet 2 "0.44 … 0.97 × log p (rising with p)" — the numbers are per M_BM8 bin; the "rising with p"
reading conflates M-bins with height. Give the p-range figures (above) or say "rising with M_BM8".

## Claim E — literature map (i), `s9_lower_tail_literature.md`
Verdict: **SOUND** (citations checked; conclusion correctly labelled Assessment).

Checked via web search / arXiv full text (R282):
* Crocker, *On the sum of a prime and of two powers of two*, Pacific J. Math. 36 (1971) 103–107 — Thm I: infinitely many odd
  positive integers not of the form p + 2^a + 2^b (a, b ≥ 1). ✓
* H. Pan, *On the integers not of the form p + 2^a + 2^b*, Acta Arith. 148 (2011) 55–61 (arXiv 0905.3809): #{odd y ≤ x not of
  this form} ≫_ε x^{1−ε}. ✓
* Erdős–Tetali, *Representations of integers as the sum of k terms*, Random Struct. Alg. 1 (1990) 245–261: for each fixed k an
  asymptotic basis of order k with r(n) = Θ(log n). ✓ (probabilistic construction — "designed set", M4, fair.)
* Ghosh–Sarnak, *Integral points on Markoff type cubic surfaces*, Invent. Math. 229 (2022) 689–749 (arXiv 1706.06712, full
  text read): Hasse principle for almost all k, infinitely many failures; §7: the average of the class numbers h^±(k) is
  C^±(log k)² ✓ (so "(log k)²" is the average ORBIT count, not a point count — the table's "typical r(n)" column should say
  "average number of Markoff orbits"); the abstract/intro says part of the failures are explained by BM (refs [CTWX20], [LM20])
  and part (their Prop 8.1(iii)-type) are far more numerous than the BM-explained ones ✓ ("many explained by reciprocity" OK).
* Not re-checked (memo marks them as unchecked, honestly): Kolountzakis 1995, Graham 1963, Duke–Schulze-Pillot 1990,
  Pintz–Ruzsa, Bloom 2021. Plausible as cited.

**D9 (MINOR).** Literature table, Markoff row: "typical r(n) (log k)²" — Ghosh–Sarnak's (log k)² is the average number of
orbits of the Markoff group action (each orbit is infinite), not a representation count; say so, since the analogy to
R(p) ≍ (log p)² is only at the level of "number of fundamental-domain points".

## Claim F — memos s9_no_fixed_integer, s9_fibration_level, s9_disproof_class_layer (corollary scope)
Verdicts: **s9_no_fixed_integer SOUND (Assessment + PROVED inequality); s9_fibration_level SOUND-AFTER-REPAIRS (D1 propagates);
s9_disproof_class_layer SOUND-AFTER-REPAIRS (D1, D10, D11).**

* No fixed integer. gcd(tn + 1, t′n + 1) | t − t′ (t′(tn+1) − t(t′n+1) = t′ − t) ✓. D⁻_t ≤ (τ − σ_{χ_{−t}})/2 (Prop 2.1(a)) and
  equality at t = 4 (the only 4 | t with φ(t) = 2): D⁻_4(N) = #{d | N : d ≡ 3 (4)} = (τ − σ_{χ_{−4}})/2 ✓. Dirichlet's formula
  Σ_{d|N} χ_D(d) = R_D(N)/w_D holds for any (also non-fundamental) discriminant D = −t with gcd(N, D) = 1, counting
  representations by a full system of primitive forms ✓. Hence a LOWER bound for R_{−t}(N) is an UPPER bound for M^{lev}_t and
  for (τ − σ)/2 ≥ D⁻ — "Hecke positivity pushes against ES" is correct in the sense stated. (Upper bounds on representation
  numbers are trivial and give only M^{lev} > 0, which Prop 2.2 already has.) The "no fixed-integer packaging" claim is an
  Assessment and labelled so.
* Fibration. F_t : (tu − 1)(tv − 1) = tn + 1 ✓ (expand: t(tuv − u − v) + 1); (0, −n) ∈ F_t(ℤ) ✓; positive integral points ⟺
  divisors X ≡ −1 (t) ✓; t = 8, n = 73: 585 = 3²·5·13, 15 ≡ −1 (8), no prime factor ≡ 7 (8) ✓. The line "only one of these
  characters is the restriction of the total space's Brauer class: χ_{−t}" inherits D1 (for n ≡ 3 (4) the restriction
  evaluates as −χ_t on fibre points, `review_r282_blevel.py`). Method-collapse part: Assessment, Harpaz hypotheses admittedly
  unchecked — fine.
* Disproof class layer. The no-go "obstructed by χ_{−t} at all levels 4 | t ≤ T, T ≥ 4ℓ(n) ⟹ square" is a restatement of
  Prop 2.2 and is correct; the self-review repair (other genus characters can still obstruct) is correct and adequate. Example
  n = 7, t = 12: 85 = 5·17, χ_{−12}(5) = χ_{−12}(17) = −1, χ_{−4} = +1 on both; divisor classes {1, 5, 5, 1} mod 12 ✓.

**D10 (MINOR).** `s9_disproof_class_layer.md` Statement: "ℓ(n) is the least prime with (n/ℓ) = −1" — must be the least ODD prime
(as repaired in Prop 2.2; for n ≡ 5 (8), ℓ = 2 would not work since t would have to be odd/ℓ | tn + 1 impossible for even ℓ).
**D11 (MINOR).** The n = 7, t = 12 example is also killed by SIZE: a (★) word at level t needs d ≥ t − 1 and N/d ≥ t − 1, i.e.
N ≥ 121 > 85 (indeed all words of 7 have t ≤ 9). So it does not isolate a genus obstruction from the size constraint β_t. Use an
example where size allows a hit, e.g. scan (n, t) with tn + 1 ≥ (t − 1)², an inert prime factor present, and class −1
absent only because of a second real character. Concrete replacement (R282 search, `/tmp`-free: rerunnable in a few lines with
`review_r282_levelbm2.kron`): **n = 17 (≡ 1 (4), non-square), t = 12**: N = 205 = 5·41 ≥ 11², χ_{−12}(5) = χ_{−12}(41) = −1 but
χ_{−4}(5) = χ_{−4}(41) = +1, divisor classes {1, 5, 5, 1} mod 12 — class 11 excluded by χ_{−4} alone, size not binding. (Others:
n = 23, t = 8, N = 185 = 5·37, χ_{−4}; n = 23, t = 16, N = 369 = 3²·41, χ_{−8}.)
**D12 (MINOR — label consistency).** "level form of BL Thm 1.8" (memo Assessment; report SHARP 1) — for n ≡ 3 (4) the
character involved is not BL's (D1); restrict to n ≡ 1 (4).
