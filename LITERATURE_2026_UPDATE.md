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