# Literature update (2026-10-21)

Audit against `LITERATURE_2026.md` §2 and Waves Y/Z/AA. Search focused on new proof/disproof claims and partial results, plus opened primary sources; saved excerpts and source/access dates are in `sources/lit2026h/README.md`.

## 1. New relevant item: Lean exceptional-set formalization

A missed item is Sushaan K.'s GitHub project, [erdos-straus-lean](https://github.com/sushaan-k/erdos-straus-lean), last committed/released 30 July 2026. It formalizes an exceptional-set bound for the Erdős–Straus equation, with main theorem `erdos_straus_exceptional_set_bound : IsMainBound exceptionalCount`. Its formalization note explicitly says the “closed” proof depends on nine named analytic inputs (Brun–Titchmarsh, Suen, squarefree progression estimates, sieve/Mertens and weighted Bombieri–Vinogradov inputs); these are interfaces/specializations, not derived in Lean. Fixed-numerator/generalized modules remain conditional. This is meaningful machine-checked formalization of an exceptional-set result, but neither a pointwise proof nor a new bound shown to surpass Vaughan. No manuscript/arXiv record or comparison establishing a sharper exponent was found. Source excerpts: `sources/lit2026h/exceptional-set-lean-{github,formalization}.txt`.

## 2. New AI-assisted material; not a resolution

The [Zenodo record 23003413](https://zenodo.org/records/23003413), published 27 September 2026, describes “The Erdős–Straus equation through residual shells” (v4), written by Claude Opus 5.5 at the author's request and expressly published ahead of author review. It reports 72 proved statements and a 39-declaration Lean verification core, but its own description explicitly says the work “do[es] not prove or disprove” Erdős–Straus. It develops intermediate congruence/witness machinery, not a resolution; attribution/review caveat is material. Source excerpt: `sources/lit2026h/zenodo-23003413.txt`.

## 3. Tracked claims/status and problem-page check

* Shkredov, [arXiv:2603.14116](https://arxiv.org/abs/2603.14116), Ilya D. Shkredov, v2 dated 24 June 2026: abstract claims Zaremba for prime denominators and gives further conditional/general results. v2 clarifies technical Lemma 32; no subsequent revision or refutation found. This is not about unit fractions.
* Zhang, [arXiv:2605.02518](https://arxiv.org/abs/2605.02518), Xin Zhang, v2 dated 8 May 2026: abstract claims to confirm Zaremba via expansion in SL₂(Z/qZ) and Shkredov's framework. No subsequent revision or refutation surfaced. Also unrelated to unit fractions.
* The relevant Erdős Problems page is **#242**, covering Erdős–Straus and the generalized Schinzel/Sierpiński question. Its current page still lists the established Vaughan, Bright–Loughran, Elsholtz–Tao, Elsholtz–Planitzer and finite-verification results, with no new resolution or progress item. Page **#5 is unrelated**: it is about prime gaps. Excerpts: `erdosproblems-242.txt`, `erdosproblems-5.txt`.
* A search result surfaced a ResearchGate item titled “A simple solution of Erdős–Straus conjecture” with a 2026-09-21 date. Opening the actual page returned a CAPTCHA/security gate; the underlying title is an older item (publication ID 338282492). Could not inspect date history or assess contents, so do not treat search metadata as a new claim or evidence.

## 4. Partial results and negative findings

Searches for post-August 2026 work, new exceptional-set estimates, Elsholtz–Tao counting follow-ups, verification beyond 10¹⁸, Bright–Loughran/integral-point follow-ups, function-field results, and Lean/Mathlib work found no verified new paper/result beyond the formalization and AI archive above. No new actual or claimed full proof/disproof of Erdős–Straus, 5/n, or Schinzel's k/n was verified. The 2025/early-2026 claims and partial work in the existing literature file remain the substantive recent record; searches did not uncover an acceptance/refutation of its tracked proof claims. Finite verification remains at 10¹⁸ in the cited 2025 Mihnea–Dumitru work.

## Bottom line

As of 2026-10-21, nothing relevant has been proven in the sense of resolving Erdős–Straus, Sierpiński 5/n, or Schinzel's general conjecture. The genuinely new item located is a Lean formalization of an exceptional-set bound, with nine substantial analytic assumptions exposed at the trust boundary; it does not establish the conjecture or demonstrate improvement over Vaughan. The conspicuous September AI-produced archive explicitly disclaims proving or disproving the conjecture. No verified disproof, better verification bound, or new partial-result advance emerged.
## Addendum (2026-10-21): the OpenAI `openai/math` release (missed above)

The audit above missed `github.com/openai/math`, released 2026-10-06 (HEAD 1581d4cb). It holds 719 unrefereed
AI-produced manuscripts in 372 families, about 42% with Lean formalizations, three withdrawn on 2026-10-07. None
concerns Erdős–Straus, and the list of attempted problems is not published. Several claimed results bear on the
campaign's tools: family 003 (quasi-RH σ > 7/8 for all Dirichlet L-functions, plus a uniform Siegel-zero
exclusion; Lean-formalized), 142 (deterministic factorization over F_p), 029 (Artin), 007 (two-point Chowla),
021 (Jacobsthal), 025 (short Egyptian fractions Θ(log log b)) and 028 (Gaussian moat). The full impact analysis is
in `OAI_DUMP_IMPACT.md`, with excerpts in `sources/oai2026/`.

## TheoremDB monitoring (2026-10-21)

TheoremDB (theoremdb.org, CC0, an agent-oriented shared research memory) has two thin entries:
* P5 `erdos-straus-conjecture`: an admin seed of 2026-07-31 citing only Xu arXiv:2605.23601, with 2 records;
* `erdos-problem-242` (ES plus Schinzel's generalisation): 3 records, a status note, a source audit and a planned
  counterexample search.
Neither contains results beyond this repository. **Read-only watcher:** `uv run python scripts/theoremdb_watch.py`.
It uses the public API, never writes, and diffs against `data/theoremdb/snapshot.json`. It reports new or changed
records on those two problems, plus keyword-filtered hits of research search (Straus, Egyptian / unit fractions,
4/n, 5/n, Schinzel). Run it at every literature check. Nothing has been uploaded; per pasky, nothing goes external
before a final or crisp result.

## erdosproblems.ai (Plasma AI), checked 2026-10-21

erdosproblems.ai is an independent proof-claim and status site operated by Plasma AI and not endorsed by Bloom.
It started after erdosproblems.com paused claims in October 2026. It is built from the open repo
`github.com/plasma-ai/erdos` (Apache-2.0, plus CC-BY-4.0). Its problem-242 page and wiki give a careful,
source-level literature summary. Status "claimed": that rests on three pending full-proof manuscripts (Alomari
2023, Dyachenko arXiv:2511.07465, Bradford arXiv:2602.11774). Accepted partial results: Obláth 1950 and Terzi
1971. The 10¹⁸ verification is recorded as pending. Compared against this repository, the only item we had not
recorded is **Alomari, "A simple direct proof of the Erdős–Straus conjecture" (Feb 2023; Authorea
10.22541/au.167569747.72416313, OSF gecwa, Research Square rs-2579186)**. It is an elementary full-proof claim; **audited below: fatally flawed**. Everything else (Akaka Zenodo, Bello-Hernández et al., Dahan, Jiang 2609.09204
(withdrawn), the leochlon/erdstrau Lean repository, PW25, MiDu25) is already in LITERATURE_2026.md. The watcher
`scripts/theoremdb_watch.py` now also reports new commits to `wiki/problems/unit_fractions/E0242` in that repo.
Nothing has been posted there.

### Alomari 2023: audit (2026-10-21; text in `sources/lit2026j/`)

**Verdict: not a proof (fatal).** The 4-page note argues by contradiction with a least-upper-bound argument.
1. **Quantifier error.** The negation of ES is "∃ n ≥ 2 ∀ x, y, z: n(xy+xz+yz) ≠ 4xyz". The proof instead
   ranges over "for some n ≥ 2". Its set A := {n(xy+xz+yz) : x, y, z ∈ ℕ, n ≥ 2} lets n vary, and the final
   sentence concludes that the equation "holds true for some integers x, y, z **and n ≥ 2**". That is trivially
   true (n = 4, x = y = z = 3) and is not ES.
2. **Ill-defined supremum.** "sup(A) = α = 4xyz" equates the supremum of a set with an expression in the bound
   variables x, y, z. A is unbounded above in any case, and the dichotomy "either < for all x, y, z or > for all
   x, y, z" does not follow from the failure of equality.
3. **Broken inequality chain.** The displayed chain asserts 4m³ + 4m(·) − … < 4m³·(·) + 4m(·), then rewrites the
   right side as 4m³ + 4m·(·) (the product sign silently becomes a sum) and calls it "N·(mq+pm+pq) ∈ A".
4. **Numerator-blind, hence proves false statements (FRONTIER §4 line 2).** The author states that the argument
   works for every fixed numerator m. Read as a proof of "∀ n ≥ 2", it would give 8/11, 8/17, 8/131 and 8/241 as
   sums of three unit fractions. Exhaustive search (re-run 2026-10-21) confirms that none of these has such a
   representation.
