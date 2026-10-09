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
