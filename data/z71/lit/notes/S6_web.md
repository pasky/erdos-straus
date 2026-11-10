# S6 — non-arXiv web sweep (2026-10-21 to 2026-11-10)

Accessed 2026-11-10. Baseline: `LITERATURE_2026_UPDATE.md` (10-21) and `Z58_LIT.md` §2 (10-30/11-05). ES remains open. Fact/assessment distinction below; no proof audited. This is a web/API sweep, not an exhaustive census.

## 1. Erdős Problems #242; forum; linked pages

- **Page:** https://www.erdosproblems.com/242 (visit-webpage, 2026-11-10). Still lists the previously known Vaughan exceptional-set result, Bright–Loughran, Elsholtz–Tao/Planitzer and Mihnea–Dumitru 10^18 verification. No Kandukoori–Ramesh–Kumar (K-R-K) addition, no new status or reference visible. It has the same formula-stripping issue in the reader extraction; this is not evidence of unshown comment counts.
- **Forum:** https://www.erdosproblems.com/forum/thread/242 (linked claim threads accessed through Plasma page; direct full forum extraction was not obtained). Plasma repo's Oct 28 update records defects in Alomari (2023), Dyachenko (arXiv:2511.07465), Bradford (arXiv:2602.11774), standing regenerated “open / none”; Nov 10 merged PR #65, “reject the three claimed full proofs” (https://github.com/plasma-ai/erdos/commit/b6f7945a32a8892757db3d84cde1e4b21e557ce4). No evidence of a new valid #242 forum result. See access limitation below.
- Linked-problem sweep: search result on a recently solved AI-related Erdős problem returned no verified directly adjacent divisor/shifted-prime development; no specific related page with an applicable new theorem was confirmed. Do not infer ES relevance from AI solution status elsewhere.

## 2. Plasma AI / erdosproblems.ai

- https://erdosproblems.ai/problems/242, visited 2026-11-10. It says “Claimed · Proved” as derived from claims (not accepted): three full proof claims and 10^18 verification remain pending; its text explicitly says no proof/counterexample found within its search. This mirrors the baseline, with an important new community audit below.
- https://github.com/plasma-ai/erdos/commits/main API, 2026-11-10: Oct 23 and Oct 28 public releases; Oct 28 commit says three claimed proofs rejected as defective and labels standing open/none. Nov 10 merge PR #65 incorporates proof audits. These are review/status changes, not new mathematics. No interaction performed; read-only.

## 3. Repository/releases since baseline

- K-R-K Lean repo https://github.com/sushaan-k/erdos-straus-lean: API HEAD remains `f6c99eaa` (Oct 30), same as baseline. No commits/theorem advancement beyond the already recorded 3/4 exceptional-set exponent; Oct 30 commits prove BV in-project and reorganize/readme-map declarations. No short-interval or pointwise ES theorem surfaced.
- Google DeepMind formal-conjectures `ErdosProblems/242.lean`: https://github.com/google-deepmind/formal-conjectures/commits/main/FormalConjectures/ErdosProblems/242.lean API returned latest path commit Sep 18, 2026 (modularization); none since 10-21. No Erdős–Straus formalization addition observed.
- GitHub repository search `q=erdos-straus&sort=updated&order=desc` (API, 2026-11-10) surfaced new/updated small experimental repositories, including `hangyolkim-droid/erdos-straus-census` (Oct 24), `rajveersinh-is-dev/erdos-straus-conjecture-investigation` (Oct 22; claims parametric families), and solver/workbench/cluster projects. Descriptions and minimal public metadata only; no independently verified theorem. Search is relevance-ranked and not comprehensive. Akaka Zenodo v0.8 record 22905042 remains Sep 22 baseline; no newer version surfaced.

## 4. Newly indexed non-arXiv records

- **Zenodo record 23770866**, Deep Bhattacharjee and Ushashi Bhattacharya, “Erdős–Straus equation: an explicit exponent for the exceptional set and the Type II sieve sum; papers, Lean 4 formalization, verification code and engine runs,” published Oct 29. https://zenodo.org/records/23770866 (API record checked 2026-11-10). Description claims an explicit exceptional-set constant with exponent 2/3, adapting Dahan (already in baseline), plus Type-II sum expansion and 59 Lean declarations; expressly says it does not prove ES. The exponent is not above K-R-K's 3/4, so no campaign improvement apparent. **Assessment (unreviewed):** lower plausibility pending source reading; the abstract mixes distinct papers and heavy computational/AI-engine claims, gives two differing lower bounds for c1 (0.6931 then 0.6657), and claims constants not yet checked against the manuscripts. Not an arXiv result; no PDF read.
- Zenodo API search for “Erdős–Straus” showed older records mixed into results (including 2025–26 publications), and many irrelevant records. No other verified qualifying post-Oct-21 ES record identified. ResearchGate CAPTCHA/search metadata and viXra/HAL/Authorea/SSRN yielded no verified new record in this pass; absence is not exhaustive. The claimed new Zenodo record is a concrete hit to follow up.

## 5. OpenAI math release delta

- https://github.com/openai/math/commits/main API: after baseline 1581d4c (Oct 12), content update commit 42907c9 / merge 7ef5c0c (Oct 26) updates manuscripts/formalizations/verification; Oct 29/30 commits only align CM Hodge comparator declarations. GitHub commit-files API for 42907c9 (checked 2026-11-10) shows the update's new mathematical family material is CM Hodge formalization, LocalSmoothing and SubexponentialSAT; other file changes are comparator/proof updates. No new family touching the requested Egyptian-fraction, divisors-in-classes, sieve/parity, Titchmarsh, class-group, Markoff/cubic-surface or integral-point topics is named in this changed-file list. No relevant new family number/claim identified. This is a filename/commit-metadata inspection, not a complete manifest semantic diff.

## 6. Questions, journals, adjacent AI / blogs

- Search query for MathOverflow Erdős–Straus surfaced only old questions (2011/2012/2015 etc.); no post-Oct 1 question verified. Math.SE search surfaced https://math.stackexchange.com/questions/5153708/why-are-primes-p-equiv-1-pmod4-difficult-in-the-erd%C5%91s-straus-conjecture, “5 days ago” relative to the Nov 10 search; date appears Nov 5, 2026. It asks explanatory context, not a result.
- Crossref API date-window/title query 2026-10-21…11-10 (checked 2026-11-10) returned no Erdős–Straus/Egyptian-fractions journal item. Results containing “Erdős” were false positives (Erdős–Ko–Rado; Erdős–Loxton), not ES. No journal publication identified.
- Search did not verify an Oct 21–Nov 10 relevant new release/post from AlphaProof/AlphaEvolve, Anthropic, xAI, Harmonic, Epoch/FrontierMath, Tao’s blog or Mathstodon. This is a bounded search, not a monitored feed audit. No relevant new mathematical method can be reported.

## Limits / sources

Searches used `/home/pasky/.pi/agent/packages/pi-amplike/skills/web-search/search.py`; pages visited using the visit-webpage skill; GitHub, Zenodo and Crossref public APIs via curl. Search API is relevance-based; Zenodo result output truncated and contains broad/misleading keyword matches. Direct full erdosproblems.com forum thread comments could not be reliably extracted; no login-wall diagnosis. OpenAI family manifest comparison, the Zenodo manuscript, and platform-by-platform exhaustive OSF/ResearchGate/viXra/HAL/Authorea/SSRN checks remain undone. No large repository downloaded. Report access dates are 2026-11-10.
