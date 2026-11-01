# Z53_LIT — literature and tool sweep 2020–2026 for the B2 wall (wave z53, lane LIT)

**ES is OPEN.** Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only. Literature statements are quoted from the opened source
(theorem number + page); "abstract only" marks items whose PDF was not read; proofs of cited papers were **not** re-checked.

*Status: CHECKPOINT 1 skeleton (2026-11-01). Sections marked TODO are filled in later in the lane.*

## 0. Precise questions attacked

The lane is a verified literature sweep, so its "statements" are search questions with a sharp success criterion.
For each, success = a published or arXiv theorem (opened, theorem number quoted) that (i) is pointwise at one fixed
integer / one fixed modulus, and (ii) supplies the named missing input.

* **Q(a) — divisors of one integer in a class.** Is there a 2020–2026 theorem giving, for every (large) N in a natural
  family, a *lower bound* (existence) for #{d | N : d ≡ a (mod q)} with q ≥ (log N)^{c}, or any pointwise statement about
  the divisor classes of the family {p + u : u ≤ (log p)^A} at one p? (FRONTIER §7.2, §7.3.)
* **Q(b,c,d) — fixed-modulus cancellation.** Is there a theorem beating the trivial bound for #{(x,y) ∈ I × J :
  xy ≡ 1 (mod 4p)} with |I||J| < p (or for the height-tied subset x ≡ y ≡ −1 (mod 4C), C = (xy − 1)/4p), or for a bilinear
  Kloosterman / Kloosterman-fraction sum whose averaged variable is *not* attached to p, that improves the elementary
  E(p) ≪ p^{1/3+o(1)} (Z52D_HYPERBOLA Thm 1)? (FRONTIER §7.1.)
* **Q(e) — multiplicative representation mod a fixed modulus.** Is there a "two-modulus" representation theorem: every
  class a mod q is a product xy of small/smooth/prime x, y that are *also* constrained modulo a second modulus? (Target 5,
  non-CRT.)
* **Q(f) — ES itself.** Any new pointwise or exceptional-set result, proof claim, or formalisation since the repo's last
  sweep (2026-10-30 for arXiv; 2026-10-17 for erdosproblems #242)?
* **Q(g) — Zaremba.** What exactly is the *pointwise* input of Shkredov arXiv:2603.14116 / Zhang arXiv:2605.02518, and
  could it have an analogue at a polylog expected count?
* **Q(h) — the (J)103 test (highest priority).** Is there an every-n theorem, unconditional, for a natural problem, with
  a polylogarithmic expected number of witnesses (no averaging)? A positive answer would contradict the Assessment (J)103
  (`DISCOVERIES.md` item 103; FRONTIER §3 M-table) and is to be reported at the top.

## 1. Why this is not already closed

The repo has three earlier sweeps: `LITERATURE_2026.md` (to 2026-09-28, plus Wave Y/Z/AA/z52 additions to 2026-10-30),
`PARITY_AUDIT.md` §1 (tables 1A–1E: divisors in classes, fixed-modulus hyperbola/Kloosterman, short intervals, parity
breaking, ES-specific; to 2026-10-17), and the z52 lanes `BRAINSTORM/z52_lit_*.md` graded in `reviews/z52-lit-grading.md`.
The repo cites 685 distinct arXiv identifiers (`data/z53/lit/repo_arxiv_ids.txt`). Gaps this lane targets:
1. 2020–2026 items in areas (b)–(e) that the earlier tables cover only through classic results (e.g. post-2023 bilinear
   Kloosterman bounds for *general* moduli, Erdős–Hooley Δ work, Erdős–Odlyzko–Sárközy-type product representations,
   Lehmer-problem / modular-inverse short-interval results).
2. The *key pointwise input* of the Zaremba claims was never extracted (LITERATURE_2026 z52: "statements only checked").
3. The (J)103 Assessment has never been stress-tested against GRH-conditional and "structural" every-n theorems with a
   precise count of witnesses.
4. arXiv postings after 2026-10-30.

## 2. First falsifier (Checkpoint 1)

**Falsifier F1 (the (J)103 test).** Classify candidate every-n theorems by the expected number of witnesses at n. If an
unconditional, natural, non-designed one with a polylog count is found, (J)103 is false and that mechanism is the
headline. *Status at checkpoint:* systematic arXiv sweep 1 (47 queries, `data/z53/lit/queries.txt` →
`data/z53/lit/sweep1.tsv`, 262 unique rows from 2020 on, 203 not cited in the repo) plus two research subagents
(excerpts in `sources/z53_lit/excerpts_*.txt`). No counterexample yet. Two candidate families are being written up:
(i) GRH-conditional fixed-modulus events (least non-residue ≤ 2 log²p, Bach; least primitive root ≤ (log p)^6, Shoup) —
polylog windows, but mechanism M2, already in the FRONTIER table; (ii) "structural" unconditional statements of
Chebyshev type (every n has a prime non-divisor ≤ (1 + o(1)) log n: expected count ≍ log n/log log n, polylog,
unconditional, natural) — the mechanism is "failure forces n into one class modulo a modulus > n". TODO: decide whether
(ii) is covered by (J)103's "structural" clause and whether its mechanism has a scoped no-go for ES.

**First new items found (verified from PDF; details §3 TODO).** Pascadi arXiv:2511.08445v2 Thm 1.1 (bilinear Kloosterman
sums S(am, n; c) for *every* modulus c, M, N ≪ c^{1/2+o(1)}, saving c^{1/700}); Chan arXiv:2506.04087v1 Thms 1–2 (close
points on modular hyperbolas); Zhi arXiv:2608.15458v1 (five-term congruences with short intervals mod p); Banks–Shparlinski
arXiv:2610.19597 (Erdős–Odlyzko–Sárközy for prime-power moduli; abstract only so far).

## 3. Verified catalogue (TODO)
## 4. Hot leads (TODO)
## 5. Verdict, screens, proposed FRONTIER text, bottom line (TODO)
