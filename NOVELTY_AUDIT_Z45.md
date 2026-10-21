# Novelty audit Z45

Literature check performed 2026-10-21 against the exact statements in the named campaign files. “NOT FOUND” means no matching result in the sources searched, not a priority proof. Search included the repository source archive and `git grep`, the named primary references, targeted web searches for later ES/surface/log-K3 work, and direct opening of Bright–Loughran and López. The archived Dahan 2026 preprint was checked for ES-surface follow-up; it concerns sieve depth, not the claims below. Search results are excerpts in `sources/lit2026i/README.md`.

## A. HARDNESS_MAP A5 + A2 — PARTIALLY KNOWN

**Known core.** Elsholtz–Tao, “Counting the number of solutions to the Erdős–Straus equation on unit fractions,” *J. Aust. Math. Soc.* 94 (2013), 50–105, arXiv:1107.1010, Propositions 2.2 and 2.6, classify the Type I/II prime solutions. Bright–Loughran, “Brauer–Manin obstruction for Erdős–Straus surfaces,” *Bull. Lond. Math. Soc.* 52 (2020), 529–543, arXiv:1908.02526v2, Corollary 1.3, states the quadratic-character constraint for prime solutions; Appendix A explicitly recovers the relevant Yamamoto conditions. Yamamoto, “On the Diophantine equation 4/n=1/x+1/y+1/z,” *Mem. Fac. Sci. Kyushu Univ. Ser. A* 19 (1965), 37–47, Lemmas 2–4, is the earlier reciprocity source. These cover the character arithmetic (in ET parameters it implies `(ab/p)=-1`), not the campaign’s stated package without checking the exact unrestricted-denominator extraction.

**Not found as a stated prior theorem:** deterministic one-call, no-factoring reduction `QNR-SEARCH ≤ ES-PRIME-SEARCH` for an arbitrary returned witness; the particular output-size consequence `r(p)≤max(a,b)` in the stated normalized coordinates; or its articulation as a complexity result. Bright–Loughran Corollary 1.4 is instead the no-Type-I/II result for odd squares, not a QNR-reduction theorem. Search also covered Monks–Velingker (2008 manuscript), TFNP/complexity/Egyptian-fraction queries, and the named ET paper. Verdict: known arithmetic ingredient, apparently new unrestricted extraction/algorithmic packaging. Do not present the quadratic character lemma itself as new.

## B. BRAUER_TWISTS — PARTIALLY KNOWN

**Known.** Bright–Loughran 2020, Theorem 1.6 and Corollary 2.9, compute the Brauer group of the standard Erdős–Straus smooth cubic (including its single nonconstant quaternion class); Theorem 1.2 and the proof of Theorem 1.8 establish no ordinary Brauer–Manin obstruction for positive integral ES points. Their model is the singular Cayley cubic/smooth resolution, not the campaign’s finite étale cover with twists. The paper’s §2 does give a torus chart and geometry, but no `π₁(U_n^sm)=Z/2` statement located. The archived literature map and searches for Wilsch, Mitankin, Harpaz, Colliot-Thélène–Wittenberg and Loughran–Mitankin found adjacent log-K3/Markoff/affine-cubic results, no computation of the stated cover.

**NOT FOUND in the literature searched:** the claimed smooth-locus fundamental group and cover `4dABC=n(A+B+C)` in this form; the full twist-specific dichotomy `Br(Y_d)/Br Q=Z/2` or `(Z/2)^2`; deck-adjustment of the extra class; and nonemptiness of the campaign’s descent–Brauer set for every `n≥2`. Bright–Loughran’s no-obstruction theorem is related but does not establish these stronger cover/descent assertions. Follow-up search through 2026 (including the archive’s 2026 Dahan preprint) revealed no matching result. These are NOT FOUND, not independently certified here; the cover calculation and its hypotheses require specialist verification before any priority or correctness claim.

## C. PROPAGATION_CLOSURE Lemma D; NONET_STEP ratio transplant — NOT FOUND

No exact match found for the mixed-valuation `4/p²` Jacobi-symbol necessity `(p/m)=-1`, or for the ratio-transplant rule with `X=(n+3)/4`, `H=n(n+3)(r+s)/(12rs)`. Searches covered Yamamoto, ET, Bright–Loughran, López and the archive’s solution-structure literature. These are narrowly formulated necessities/identities; the literature does contain numerous standard Type I/II parameterizations and divisor identities. In particular, do not infer the claimed necessary condition from a superficially similar reciprocity theorem without matching its mixed valuation hypotheses. Novelty verdict is NOT FOUND, not “new theorem” priority.

## D. FOREST_H4 — PARTIALLY KNOWN

López, “A Complete Congruence System for the Erdős–Straus Conjecture,” arXiv:2404.01508v3 (2024), Theorems 1–8, treats congruence families and solution forms, not the graph whose vertices are integers and whose edges satisfy `uv | n+u+v`. ET’s Type I/II classifications likewise do not state this graph/forest. Repository archive checks identified no exact graph/tree antecedent. The general Egyptian-fraction graph/rewriting search returned unrelated algorithmic/fraction graphs, no matching construction.

**Known overlap:** the five-slot characterization and standard divisibility identities from `LOWER_TAIL_ASTRA`/`DEDEKIND_ES` are established ES certificate material; they are not new merely because represented by edges. The specific forest `F_n`, its endpoint statistic `H₄(p)`, and the campaign’s endpoint/window separation results were NOT FOUND in the literature searched. Verdict partial: familiar certificate arithmetic, apparently new graph encoding/statistics.

## E. Q3_PIVOT pivot graphs/trapped components — NOT FOUND

No cited work located on the graph of all positive representations of `4/N` connected by re-splitting two unit fractions while holding the third denominator fixed, nor on trapped seed components for `U_{qp}`. Searches covered López 2024, ET, Monks–Velingker, and general Egyptian-fraction graph/tree/pivot terms. Generic two-unit-fraction divisor factorizations are classical and used in the memo; the graph closure/trapped-component results are the specific apparent novelty. The computed finite traps are not a theorem about all primes and must retain their “certified finite calculation” status.

## F. DELTA_TRANSPORT Thm 3.2 — NOT FOUND

No exact prior statement found for the marked overflow data and dyadic folding transport, including the `a=1`, `ℓ=2`, `k=4` identity and its explicit zero-window reconstruction. The identity is elementary and lies near the standard five-slot/Type-II divisor dictionary; that background is known. No literature source located the marked distance-one formulation, quotient obstruction, or this folding move. Verdict NOT FOUND for this exact formulation, with no claim that the underlying algebraic manipulation is independently significant.

## Search boundary / source notes

Verified primary texts opened: Bright–Loughran arXiv:1908.02526v2 (especially Corollary 1.3, Corollary 1.4, Theorem 1.6, Corollary 2.9, Appendix A); López arXiv:2404.01508v3 (Theorems 1–8); repository copies of ET arXiv:1107.1010 and Yamamoto 1965. The arXiv HTML endpoint for ET returned a broken/minimal extraction, so its archived PDF-derived text was used for propositions 2.2/2.6. `sources/lit2026i/README.md` records exact excerpts, links, and that limitation.
