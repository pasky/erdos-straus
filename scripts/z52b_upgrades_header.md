# z52b lane `upgrades` — almost-all → every upgrades in history, and what each could mean for Erdős–Straus

**ES is OPEN.** Nothing here proves or claims to prove it. This is a breadth-first list of candidate connections; the only filter
was "drop obvious nonsense" (false, meaningless, category error, literal duplicate). Items were **not** screened against the
barrier checklist (B1–B6 etc.), on purpose. Data: `data/z52b/upgrades.jsonl` (one JSON object per item); generator:
`scripts/z52b_upgrades_build.py` (catalogue `scripts/z52b_upgrades_catalogue.py`, items `scripts/z52b_upgrades_items*.py`,
this header `scripts/z52b_upgrades_header.md`). Regenerate with `python3 scripts/z52b_upgrades_build.py`.

## Summary

* **{{N}} items** from **{{NCAT}} catalogued historical upgrades** (almost-all / density-one / infinitely-many / conditional /
  randomized / case-by-case → every or all-sufficiently-large), across additive and multiplicative number theory, quadratic forms,
  Diophantine equations, automorphic forms, homogeneous dynamics, additive combinatorics, extremal/probabilistic
  combinatorics, Egyptian fractions, function fields, model theory, complexity theory and topology. Also catalogued: **failed or
  stuck upgrades** (binary Goldbach, Apollonian local–global [false], Goldbach's other conjecture [false], Erdős's p + 2^k
  covering obstruction, Ghosh–Sarnak Markoff Hasse failures, Zaremba, Collatz, Lehmer τ(n) ≠ 0, Littlewood, p + m², three
  cubes) because they show where the step can fail.
* {{TAGS}}
* {{NSEEN}} items carry a `seen:<file>` tag (a quick keyword grep or my own
  knowledge of the repo — not an exhaustive novelty check).
* Every catalogue entry except `GSMARKOFF` (added last; citations as in FRONTIER §2.4) had its "last step" checked by research subagents (`data/z52b/upgrades_verify_out_{0..5}.md`); ~60 corrections
  were applied as overrides (two verifier "corrections" were rejected and say so: Dirichlet's Pell proof, Ramanujan's τ ≡ σ₁₁ (mod
  691)). Item-level literature leads were checked separately (`data/z52b/upgrades_leads_check.md`); unverified leads are phrased
  "check whether …".
* A hostile self-review (reviewer subagent over the whole lane) found 20 concrete errors (e.g. a window-equivalence missing the −p
  branch, (★) conflated with ES in two items, a false fixed-p equidistribution claim, a missing size condition in the trial form,
  an over-strong zero-sum claim, a wrong arXiv id, a degenerate quadric called a ternary form); all were repaired in place and are
  marked "reviewer repair" where the text changed substantively.

### Template taxonomy (how upgrades actually happened) → ES status in one line each

1. **Explicit threshold + verification** (Helfgott, BDD g(4), Bertrand, BHV): ES has no all-large-p theorem at all, so the first
   gap is any effective statement (items 0001, 0002, 0217, 0222).
2. **Complementary methods / pick one of several** (Holowinsky–Soundararajan, Heath-Brown's Artin, Heilbronn's case split): the
   (★) and b=1 lines never fail together ≤ 10⁸ — the most concrete data-backed template (items 0095, 0096, 0059, 0061, 0284, 0327).
3. **Pigeonhole + group law** (Pell/Dirichlet, Lagrange, Spencer): needs a combination law on near-certificates; the SL₂ form is
   the candidate (items 0084, 0023, 0025, 0168, 0205).
4. **Local–global via one class / equidistribution of always-existing objects** (Gauss three squares, Duke, Linnik): needs an
   ES encoding with class number one or canonical objects attached to every p (items 0031, 0036, 0039, 0040, 0319).
5. **Congruence / divisibility forcing** (Chen's Markoff theorem, Ono, Lehmer's τ, Wielandt, Mihăilescu): find a nonzero
   congruence for a certificate count (items 0105, 0154, 0228, 0239, 0269).
6. **Parity / involution / topology** (Zagier, Kneser, Galois parity): finite sets with forced odd size or nontrivial ℤ/2-index
   (items 0026, 0027, 0099, 0155, 0257).
7. **Hecke/multiplicative rigidity** (QUE, Soundararajan): relations between counts at p, pℓ, pℓ² (items 0092, 0285).
8. **Amplification / complement counting** (Friedlander–Iwaniec, Stepanov–Weil): items 0097, 0090, 0331.
9. **Closure / recursion / absorption** (Wilson, Graham, Keevash, Bose–Shrikhande–Parker): ES is closed only under n → kn;
   items 0136, 0138, 0148, 0255.
10. **Exact formulas / identities outside Schinzel's reach** (Rademacher, Mordell's 3G(n) − 3, identities in (a, b) or m):
    items 0176, 0232, 0276, 0328.
11. **Characterise the exceptional set exactly** (Yoccoz/Brjuno, Apollonian corrected conjecture): items 0267, 0213, 0107.
12. **Failed upgrades as hygiene** (Apollonian, Ghosh–Sarnak, Erdős covering, 8/n, fake models): items 0108, 0322, 0323, 0171,
    0190, 0118.
13. **Self-corrections** found while generating: 0265 (power-size main terms are not sufficient: p + m² is open), 0275
    (Green–Tao–Ziegler is not uniform in coefficients at fixed p), 0315 (a single level already gives density one — the
    information is all in exceptional-set decay).

### Ten items I find most exciting (cheap first steps, and either new to the repo or sharper than what I found there)

1. **upgrades-0151** — ES as an infinite congruence "covering" of the non-squares (Hough / Balister et al. distortion method): the
   (★) congruences p ≡ −(u+B) (mod 4uB) never cover odd squares (T1); study the uncovered set as moduli grow.
2. **upgrades-0095 / 0096** — Holowinsky–Soundararajan template: find one statistic (e.g. L(1,(·/p)) or the BM correction T(p))
   such that (★) failure and b=1 failure push it in opposite directions.
3. **upgrades-0105** — Chen's Markoff mechanism: look for a congruence R(p)/2 ≡ g(p) ≢ 0 (mod m) on residue classes (cheap mining;
   cf. Lehmer's τ, items 0269–0270, and Ono-type mod-ℓ structure, 0154 and 0228).
4. **upgrades-0084** — Dirichlet's Pell proof (fails exactly at squares, like T1): pigeonhole two near-certificates in M₂(ℤ) with
   the same defect and take a quotient.
5. **upgrades-0092** — Soundararajan's no-escape-of-mass: Hecke-type relations between ES counts at p, pℓ, pℓ².
6. **upgrades-0090** — Stepanov/Weil "lower bound from upper bounds on the complements": the total over all divisor classes is
   known pointwise in p; only upper bounds on wrong classes are needed.
7. **upgrades-0328** — Mordell (1923): for prime n the number of positive solutions of yz + zx + xy = n is 3G(n) − 3, an exact
   class-number-sized count; look for maps from these to ES solutions.
8. **upgrades-0232 / 0276** — identity searches outside Mordell–Schinzel's scope: polynomial in the Gaussian coordinates (a, b)
   of p = a² + b², or in m for n = m² + k.
9. **upgrades-0201** — Linnik with a fixed split prime: prove ES for all p with (p/ℓ) = −1 for one fixed ℓ (BM layer guaranteed):
   the first possible infinite every-p family of Mordell-hard primes.
10. **upgrades-0314 + 0316** — positivity means there are no minor arcs: ES ⟸ a certificate at levels C ≤ (log p)^A, i.e. a sieve of
    growing dimension over the thin multiplicative sets S_C (failures of single levels have density 0 already at C = 1, item 0315).

Honourable mentions: 0191 (exact group-ring formula for window counts), 0097 (amplified short-family moment), 0241 (LPS → MSS:
arithmetic constructions stop at a class barrier, existence methods cross it), 0322 (why Ghosh–Sarnak's failure mechanism might
or might not apply to ES), 0222 (an every-n bound must save in log x, not log H).

## Method

1. Catalogued historical upgrades (brief's list + ~70 more), each with *before*, *after*, and the **last-step ingredient** — the
   thing that actually crossed from "almost all" to "every". 99 entries were checked by four research subagents, 23 later ones by
   two more (GSMARKOFF unchecked); corrections are applied in the catalogue file as `FIX`/`FIX2` overrides and the raw reports kept in `data/z52b/`.
2. For each upgrade, generated items by asking: (a) can the last-step ingredient be **imported** literally (same tool on an ES
   count)? (b) **imitated** (same proof shape with ES objects)? (c) **analogised** (dictionary between the objects)? (d) what is the
   **intermediate statement** that would be ES's analogue of the historical intermediate step? (e) what does the upgrade's
   *failure* (if it failed) warn about? Several odd items are included on purpose (marked `odd`).
3. Eight generation passes; later passes deliberately revisited the strongest templates and filled upgrades with ≤ 1 item.
   Two self-corrections were added as items when verification showed a template does not transfer as stated
   (Green–Tao–Ziegler uniformity at fixed p: item 0275; power-size main terms are not sufficient, p + m² is open: item 0265).
4. `seen:` tags come from specific-keyword `git grep` over `*.md` (and my knowledge of the repo); they mean "related material
   exists there", not "this exact item was done".

## Coverage notes / what I did NOT get to

* Not done: any of the computations proposed (all first steps are untested); no deep reading of the primary sources beyond
  abstracts and the verifiers' checks; no systematic novelty check against the ~470 brainstorm memos beyond keyword greps.
* Under-covered fields: PDE/analysis "almost sure → deterministic" (only Kolmogorov/Carleson as a warning), mathematical physics
  beyond Lee–Yang, logic beyond Ax–Kochen, computational complexity beyond AKS/Reingold, algebraic topology beyond Kneser/Perelman.
* Not catalogued (considered, skipped as too far or redundant): Kepler, Hadamard matrices (open), Szemerédi/van der Waerden
  (colouring → density is the reverse direction), Hindman, Poincaré beyond one odd item, uniform Mordell.
* Several historical "before/after" summaries are compressed; for anything load-bearing, read the source named in the catalogue.
