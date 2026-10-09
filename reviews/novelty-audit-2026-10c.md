# Novelty audit 2026-10c (task O101): m/n exceptional sets, finite coverings, Pell/Type-I

**Auditor:** side agent O101 (branch `side-agent/novelty-audit-10c`). Priority audit only;
correctness is taken from the cited internal reviews.

**Objects audited.** DISCOVERIES (D)29–(D)31, (H)17 follow-ups 2–4, (H)34 + follow-ups,
(F)11; `paper/es-mn-short-note.tex`, `paper/es-coverings-note.tex`.

**Search method.** Jina web search + Jina reader (internet available in this pass).
Tags: **[visited URL]** = page/PDF read in this pass; **[snippet]** = search-result snippet
only; **[memory]** = auditor recollection (weak). "Apparently new" = not found in what was
searched; not a priority certificate.

(work in progress — sections filled in below)

Archived in this pass: `sources/o101/` (Elsholtz 2001 PDF from the author's page;
Pomerance's 2026 talk text).

---

## 1. Exceptional sets for m/n ((D)30, (D)31, `paper/es-mn-short-note.tex`)

### 1.1 Findings (verified)

* **Elsholtz, "Sums of k unit fractions", Trans. AMS 353 (2001) 3209–3227**
  [visited: author copy https://www.math.tugraz.at/~elsholtz/WWW/papers/papers03sumofk.pdf,
  archived `sources/o101/elsholtz-2001-sums-of-k-unit-fractions.pdf`].
  * Thm 1.3 (p. 3210): for fixed k ≥ 3, m > k,
    `E_{m,k}(N) ≪ N exp(−c_{m,k}(log N)^{1−1/(2^{k−1}−1)})`. For k = 3 this is exponent
    2/3, i.e. Vaughan. Elsholtz states (p. 3210) that Viola (Acta Arith. 22 (1973)
    339–352) had exponent `1 − 1/(k−1)` (= 1/2 at k = 3) and Shen Zun (Chinese Ann.
    Math. B 7 (1986) 213–220) `1 − 1/k` (= 2/3 at k = 3). So for three unit fractions
    **no exponent above 2/3 appears in the Viola–Shen–Elsholtz line**.
  * **Remark 7.3 (p. 3225): for k = 3 an admissible constant is
    `c_{m,3} = (3/e^{2/3})(1/(8m))^{1/3} − ε`, for N > N_m ("in principle effective");
    c_{4,3} = 0.5645 (citing his 1996 Diplomarbeit).** This is an explicit-in-m Vaughan
    bound `N exp(−c m^{−1/3}(log N)^{2/3})` 24 years before PW Thm 1.3 — but **not
    uniform**: it holds only for N > N_m with unspecified N_m. PW Thm 1.3 (uniform for
    4 ≤ m ≤ (log N)², with φ(m) in place of m) remains the first *uniform* statement
    found.
  * **Consequence for our texts (correction needed):** `es-mn-short-note.tex` §Literature
    says "[PW, Thm 1.3] is the first bound *explicit* in m that we can cite", and
    DISCOVERIES (D)31 says Thm A improves "Pomerance–Weingartner's explicit-in-m Vaughan
    bound". Both should cite Elsholtz 2001 Rem 7.3 as the first explicit-in-m constant
    (non-uniform in N), with PW Thm 1.3 the first uniform one. Our Thm A comparison is
    unaffected: `(log N)^{3/4}m^{−1/4}` beats `(log N)^{2/3}m^{−1/3}` as soon as
    `(Lm)^{1/12}` is large, exactly as for PW (indeed with m instead of φ(m) the ratio is
    `(Lm)^{1/12}`, without the log log factor).
  * Elsholtz also cites Ahmadi–Bleicher (Int. J. Math. Stat. Sci. 7 (1998) 169–185) for
    "an entirely effective but very weak upper bound" for 4/n and 5/n [snippet of the
    reference list only; not read].
* **Pomerance–Weingartner, arXiv:2511.16817 v2** [archived `sources/pw.txt`,
  re-read]: Thm 1.3 (p. 2) exactly: "absolute C such that for each pair m, N with
  4 ≤ m ≤ (log N)² the number of n ≤ N with m/n not the sum of 3 unit fractions is at
  most `N/exp(C((log N)²/φ(m))^{1/3})`". Pp. 2–3: the transition between "usually
  false" and "usually true" lies between `exp(m^{1/3})` and `exp(m^{1/2})`; the Poisson
  heuristic (intensity `(log p)³/m`) predicts most primes `p > exp(m^{1/3+ε})` have
  solutions. Our Cor D proves the density half of this prediction up to logs; this is
  correctly described in the short note (lines ~177–186).
* **Pomerance, talk text "The Erdős–Straus conjecture"** (dated Mar 2026)
  [visited https://math.dartmouth.edu/~carlp/esconjfl.pdf, archived
  `sources/o101/pomerance-esconjfl-slides-2026.md`], slides 19–27: restates Vaughan's
  2/3 as the state of the art, PW Thm 1.3, and the open transition question ("This
  raises the question of where the transition is from almost never to almost always to
  always"). PW is listed as "Ramanujan J., to appear". No better exponent, no
  short-interval or progression result is mentioned. So as of Mar 2026 Pomerance himself
  regards 2/3 as the record and the m^{1/3}-transition as open (density version) —
  this supports the significance of Cor D.
* **Other 4/n and m/n exceptional-set literature** (zbMATH Open API reviews, visited
  `https://api.zbmath.org/v1/document/<id>`):
  * Ahmadi–Bleicher 1998 (zbMATH 0919.11027, review by W. Schwarz): for every a ≥ 4,
    `S_a(N) < N/(log N)^k` for every k, N ≥ N_0, via the Selberg-sieve method "of
    W. A. Webb (1970) and Li Delang (1981)", which the reviewer calls "much [weaker]"
    than Vaughan's. So Webb (PAMS 25 (1970)) and Li (JNT 13 (1981) 485–494) are
    power-of-log results, consistent with ET p. 3 ("weaker results"). Li's full text is
    Elsevier open-archive but Cloudflare-blocked here; Yang (PAMS 85 (1982)) has no
    zbMATH review and was not read. Neither is a short-interval/progression result as far
    as the secondary sources describe them [secondary only].
  * Sander, Acta Arith. 59 (1991) 183–204 and JNT 46 (1994) 123–136 (zbMATH 4215983,
    556361): for **one** Type II subfamily (gh/w = t), the number of primes
    q ≤ x, q ≡ ℓ (k) for which that subfamily fails is `≥ C(t,k)x/(log x)^{3/2}`
    (half-dimensional sieve). This is a *progression* statement, but a **lower** bound for
    the failure of a single family — not an exceptional-set upper bound. Not a competitor;
    worth one sentence in the short note's literature section as the only
    progression-restricted ES sieve result found.
  * Jia Chaohua, Sci. China Math. 55 (2012) 465–474 (zbMATH 6040081): mean values of
    f_1(p), f_2(p); superseded by ET. Not an exceptional-set result.
  * PW is now published: **Ramanujan J. 69 (2026), no. 2, Paper 31** (zbMATH 8154259).
* **Recent arXiv (2025–2026)**, arXiv API listing of all abstracts containing "Straus",
  sorted by date to 2026-10-01 [visited `export.arxiv.org/api/query?search_query=abs:Straus`],
  abstracts read for 2512.01739, 2602.11774, 2602.20036, 2605.04551, 2605.23601,
  2606.10922, 2609.09204, 2609.29250: none gives an exceptional-set bound, short-interval or
  progression density result. (2602.20036 claims a density-zero exceptional set for
  n ≡ 1 (4) with no rate; 2605.04551 is heuristic; 2602.11774 claims a full proof in a
  one-line abstract and was not examined further.)
* **erdosproblems.com/242** [visited 2026-10-09]: still lists Vaughan 1970 as the
  exceptional-set record; cites PW for the Schinzel generalisation.
* **Searches with no relevant hit:** "Erdős–Straus exceptional set short intervals",
  "three unit fractions exceptional set arithmetic progression large sieve", plus the
  short note's earlier searches. Semantic Scholar lists 0 citations of arXiv:2511.16817
  (rate-limited for the journal record); OpenAlex full-text search for the PW title finds
  only ES papers that do not cite it for density results.

### 1.2 Verdicts

| Claim | Verdict | Notes |
|---|---|---|
| (D)31 Thm A: `E_m(I) ≤ CH exp(−c(log H)^{3/4}m^{−1/4})`, uniform in m | **APPARENTLY NEW** (relative to the internal 3/4 note) | No exponent > 2/3 for three unit fractions exists in Vaughan/Viola/Shen/Elsholtz/PW. **Correction:** explicit m-dependence is not first due to PW — Elsholtz 2001 Rem 7.3 has `c_{m,3} = (3e^{−2/3})(8m)^{−1/3} − ε` (for N > N_m). PW Thm 1.3 is the first *uniform* bound. |
| (D)31 Cor D: density transition at `log n = m^{1/3+o(1)}` | **APPARENTLY NEW**; confirms the density half of PW's Poisson heuristic (PW pp. 2–3), still posed as open in Pomerance's Mar 2026 talk | Strongest selling point of the m/n note; PW's rigorous range was m^{1/3}..m^{1/2}. |
| (D)30 Thms 1–2, Cor 3.1, (D)31 Thm B/Cor C: short intervals / progressions | **APPARENTLY NEW as stated (3/4)**; **KNOWN IN SUBSTANCE at 2/3** | Montgomery's large sieve is translation-invariant and Vaughan's forced classes are identities, so Vaughan's 2/3 holds for any interval of length H with saving in log H (the note already says "presumably"). No published statement found. Sander 1991/94 is the only progression-restricted ES sieve result found (lower bound for one family). Novelty "modest", as (D)30 says. |
| (D)30 Prop 4.1 (no log-x saving for H < e^{c(log x)^{3/4}} without ES) | trivial-but-new remark | — |

**Required text changes.**
1. `paper/es-mn-short-note.tex` §Literature: replace "[PW, Thm 1.3] is the first bound
   *explicit* in m that we can cite" by "Elsholtz [Trans. AMS 353 (2001), Rem. 7.3]
   gives the admissible constant `c_{m,3} = 3e^{−2/3}(8m)^{−1/3} − ε` in Vaughan's bound
   for N > N_m; [PW, Thm 1.3] is the first bound uniform in m"; add Elsholtz 2001 (and
   Viola 1973 / Shen 1986 via Elsholtz p. 3210) to the bibliography; update [PW] to
   Ramanujan J. 69 (2026) Paper 31. Optionally mention Sander 1991/1994.
2. In the ratio comparison (eq. `ratio`), add that against Elsholtz's `m^{−1/3}` the ratio
   is exactly `(Lm)^{1/12}` (no log log loss), for N > N_m.
3. DISCOVERIES (D)31 bullet 2: "improves PW's explicit-in-m Vaughan bound" →
   "improves the explicit-in-m Vaughan bounds of Elsholtz (2001, Rem 7.3; non-uniform)
   and PW (2026, Thm 1.3; uniform for m ≤ (log N)²)".

---

## 2. Finite polynomial coverings and sterile points ((H)34 + follow-ups, (F)11, `paper/es-coverings-note.tex` §§2–6)

### 2.1 Findings (verified)

* **Yamamoto, Mem. Fac. Sci. Kyushu Univ. Ser. A 19 (1965) 37–47** [visited
  https://www.jstage.jst.go.jp/article/kyushumfs/19/1/19_1_37/_pdf, image PDF; archived
  with our OCR as `sources/o101/yamamoto-1965-kyushu.{pdf,ocr.txt}`; Table 1 read from
  the page image].
  * Thm 1 (p. 39): p is solvable iff p lies in the union S of his system Σ of
    "coverings" {r/m} (Type I/II congruences, ≡ ET's families). Lemma 4 + Thm 2
    (pp. 41–42): every non-empty covering has Kronecker symbol −1, so S contains no
    square — the square obstruction, as the campaign already cites.
  * **Table 1 (p. 44): for each prime q, 11 ≤ q ≤ 97, the s with {−s/q} ∈ Σ₁** (his
    simplified coverings on N₀ = the Mordell-hard classes mod 840). Reading off the
    non-residue classes mod q **not** covered at level q:
    * q = 11: covered n ≡ −1, −3, −4 ≡ 10, 8, 7; **uncovered non-residues 2, 6**;
    * q = 13: covered n ≡ 11, 8, 6, 5; **uncovered non-residues 2, 7**;
    * q = 17: covered n ≡ 14, 12, 11, 10; **uncovered non-residues 3, 5, 6, 7**.
    (Each uncovered set is closed under s ↦ s⁻¹, matching his Thm 4 "inverse property".)
  * **Relevance.** The point x* = (2 mod 11, 2 mod 13) of POINTWISE_MORDELL Comp 4.1 sits
    exactly on Yamamoto's level-q uncovered residues at both primes; all six exceptional
    classes of our r = 13 Thm 3.1 are ≡ 2 or 7 (mod 13) and ≡ 2, 6 or 9 (mod 11)
    (checked: 112561, 352801, 380881, 418321, 473761, 483841 mod 11/13 =
    (9,7),(9,7),(6,7),(2,7),(2,2),(6,7)); and the r = 17 candidate cells C₅, C₇ are
    among Yamamoto's uncovered 3, 5, 6, 7 (mod 17). So the *first layer* of the campaign's
    r = 11/13/17 analysis is in Yamamoto's Table 1 (1965). Nobody (found) treats the joint
    cell (2,2) mod (11,13) or the profinite point x*.
  * **Last paragraph (p. 47):** "it is believed that any positive integer, which is a
    quadratic residue of 3, 5, 7 and 8, and still is not a perfect square, is contained
    in some covering of the system Σ₁." This is an *integer* statement (for primes it is
    ES itself, by his Thm 1), so a non-square sterile **profinite** point would not
    contradict it. But it is the earliest place where "only squares are obstructed" is
    floated, and should be cited as the historical counterpoint to the sterile-point
    conjectures (x** sterile, C₅/C₇ on the 17-line, x̂₉ Type-I-sterile).
* **Terzi, BIT 11 (1971) 212–216** [zbMATH 3355115, no review; content via
  Ionascu–Wilson below]: a list of **198 exceptional residues mod 120120** (= 840·11·13).
  Hence a Mordell-type finite-exception statement involving 11 and 13 dates to 1971,
  earlier than Salez 2014.
* **Ionascu–Wilson, Rev. Roum. Math. Pures Appl. 56 (2011) 21–30** [visited author
  copy https://csuepress.columbusstate.edu/cgi/viewcontent.cgi?article=1846&context=bibliography_faculty
  via Jina reader; archived `sources/o101/ionascu-wilson-2011.md`]:
  * Thm 3 (mod 1320, "analysis modulo 11") and Thm 4 (mod 9240): explicit exception
    lists; they give identities removing Terzi's prime residues 2521 and 9601 mod 120120
    and others (pp. 7–9).
  * Pushed the sieve to M = 2762760 = 2³·3·5·7·11·13·23 (2299 exceptions).
  * Conjecture (abstract, p. 8): the excluded residues are eventually all squares or
    composite, i.e. "Mordell type results for bigger moduli" keep improving. Again an
    integer/residue-level statement, not a profinite one.
  * They state that Yamamoto has, for each prime p ≡ 3 (mod 4) between 11 and 97, "a table
    of exceptions for congruency classes" (p. 9) — consistent with the reading above.
* **Salez, arXiv:1406.6307** [archived `sources/lit2026/arxiv-1406.6307.pdf`, re-read]:
  Prop 2 (p. 4) is Schinzel's theorem (polynomial families need b a non-residue mod a);
  §4.2 (p. 11): empirically every non-square n < 10¹⁷ in N₇ has a certificate with odd
  modulus < 5000. No covering-impossibility statement beyond squares.
* **Mihnea–Dumitru, arXiv:2509.00128** [archived, re-read]: purely computational
  (sieve depth G₈ = 25878772920, verification to 10¹⁸); nothing on coverings or
  sterile points.
* **Bright–Loughran, BLMS 52 (2020)** [archived, re-read]: no Brauer–Manin obstruction;
  App. A relates Yamamoto's conditions to Cor 1.3. Nothing on finite coverings.
* **Monks–Velingker (2008 preprint)**: only Semantic Scholar/OEIS metadata found
  [snippet]; title "properties of solutions to its underlying diophantine equation".
  Not read; no indication of covering results.
* **Bradford** (Integers 21 (2021) A24; Integers 25 (2025) A54; with Ionascu, Adv. Model.
  Optim. 17 (2015)) [zbMATH reviews 7342409, 8081443, 7009432]: reductions/patterns,
  conjectures; nothing on finite coverings. Chamberland, Integers 26 (2026) A42 [zbMATH
  8192447]: Type II ⇔ `p = qr − 4s₁s₂` (q ≡ 3 (4), s_i | (q+1)/4) — a restatement of the
  Yamamoto/ET Type II class. Bueno 2026 (academia.edu, abstract only) covers difficult
  primes ≤ 10⁹ by "a family selected from four prime non-residues" — computational.
* **Searches with no relevant hit:** "Erdős–Straus polynomial identities cannot cover
  quadratic non-residue primes / finite covering impossible", "sterile" + Egyptian
  fractions; Tao's 2011 blog post states only the residue/non-residue heuristic
  ("congruence relations cannot eliminate quadratic residues, only quadratic
  non-residues") [snippet].

### 2.2 Verdicts

| Claim | Verdict | Notes |
|---|---|---|
| Compactness framework: finite covering of all but finitely many p ∈ 𝒫 ⇔ no sterile accumulation point (coverings note Prop `compact`) | **APPARENTLY NEW as stated; folklore in substance** | ET p. 6 ("rules out … finite set of covering congruence strategies") is the closest; nobody phrases it profinitely. Trivial once stated. |
| "No finite set of polynomial identities covers a non-square-obstructed set" (sterile non-square points) | **APPARENTLY NEW question**; **no result either way in the literature** | Only the square obstruction is known (Mordell 1969; Yamamoto 1965 Thm 2; Schinzel 2000; ET Prop 1.6; Salez Prop 2). The literature leans the *other* way: Yamamoto p. 47 and Ionascu–Wilson's conjecture expect non-squares to be coverable (at integer level). Our r = 17 result is CONDITIONAL and x** is EVIDENCE, so nothing contradicts the literature. |
| r = 13 finite-exception Thm 3.1 (6 classes mod 720720) | **KNOWN IN SUBSTANCE** | Terzi 1971 (198 residues mod 120120), Ionascu–Wilson 2011 (mod 9240, 2762760), Salez 2014 (levels 120120 …). Our version: one level deeper, sliced by (p/13), with independently checkable certificates. The note already says "explicit packaging of Salez"; **add Terzi 1971 and Ionascu–Wilson 2011**. |
| x* = (2 mod 11, 2 mod 13) as the hard cell; 17-cells C₅, C₇ | **PARTIAL** | The residues 2, 6 (mod 11), 2, 7 (mod 13), 3, 5, 6, 7 (mod 17) are exactly Yamamoto's 1965 Table 1 non-residue classes not covered at level q. The joint cell, the profinite point, the 10⁶ / 12670944 covering heights and the refutation (F)11 are apparently new. |
| r = 17 line → boxes = ES solutions at prime powers (MORDELL17/17B) | **APPARENTLY NEW** | Nothing similar found. |
| Type-I covering heights C(5) = 10, C(7) > 1.32·10¹² ((H)17) | **APPARENTLY NEW** | Graham–Ringrose / Lau–Wu concern n_p, not ck_min coverings. |

**Required text changes.**
1. `paper/es-coverings-note.tex` §5 (r = 13 novelty paragraph) and DISCOVERIES (H)34
   bullet 1: add "a list of 198 exceptional residues mod 120120 is already in Terzi (BIT
   11 (1971)); Ionascu–Wilson (Rev. Roum. 56 (2011)) push the analysis to 9240 and
   2762760".
2. Same section, §"The point x* and the candidate x**": add "the residues 2 (mod 11) and
   2 (mod 13) are among the non-residue classes not covered at level q in Yamamoto's
   Table 1 [Yamamoto 1965, p. 44], which leaves 2, 6 (mod 11), 2, 7 (mod 13) and
   3, 5, 6, 7 (mod 17)". Same remark at the r = 17 section for C₅, C₇.
3. Introduction / §open: cite Yamamoto p. 47 ("it is believed that any … not a perfect
   square, is contained in some covering") and Ionascu–Wilson's conjecture as the
   opposite expectation at integer level, and say explicitly that a sterile non-square
   profinite point would not contradict them.
