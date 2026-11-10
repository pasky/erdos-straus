# z71 LIT — shared context for research subagents (read fully before starting)

Repo: `/home/pasky/projects/math/erdos-straus-claude` (a long AI-run campaign on the Erdős–Straus conjecture, ES:
4/n = 1/x + 1/y + 1/z for every n ≥ 2). **ES is OPEN.** Today is 2026-11-10. Previous literature sweeps: `LITERATURE_2026.md`
(to 2026-09-28), `LITERATURE_2026_UPDATE.md` (10-21), `Z53_LIT.md` (11-01), `Z58_LIT.md` (11-05). This sweep (z71) covers what
appeared roughly 2026-10-10 … 2026-11-10 and asks one question: **does any new paper contain an idea/mechanism usable here?**

## What the campaign is stuck on (the "B2 atom")
ES reduces to primes p ≡ 1 (mod 24), really p mod 840 ∈ {1,121,169,289,361,529} ("Mordell-hard"). Every route ends at:
*one specific integer determined by p must have a divisor in a residue class whose modulus is itself part of the solution*
(tied-modulus divisor event), with only polylog(p) expected witnesses. Canonical form (★):
  R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n};  R(p) ≥ 1 ⇒ ES(p).
  Equivalent: R(p) = Σ_{C≥1} #{d | 4Cp+1 : d ≡ −1 (mod 4C)};  = #{(u,B): gcd=1, p ≡ −(u+B) (mod 4uB)};
  e-slice form: ES(p) ⟺ ∃ e ≡ −p (mod 4) with −1 ∈ {ab⁻¹ mod e : ab | N}, N = (p+e)/4 (Type II) or (pe+1)/4 (Type I);
  SL₂ form: [[a,p],[c,d]] ∈ SL₂(ℤ), c ∈ 4ℕ, a ≡ d ≡ −1 (mod c). Surface form: xyz = x + y + n with 4 | z (a log K3 / cubic surface).
Needed: a one-sided pointwise lower bound R(p) ≥ 1 at EVERY large prime (main term ≍ (log p)², proved unconditionally; the
lower tail at a single integer is the open problem). GRH / quasi-RH / Elliott–Halberstam / Kuznetsov are known NOT to give it
(they control averages over the integer, modulus or character).

## Falsifiers every candidate mechanism must survive (name the step that breaks)
* F1 (T1): odd squares n = m² have NO Type I/II solutions (R(m²) = 0) though all local/genus/Brauer–Manin conditions on the
  full ES surface hold. So the argument must use the quadratic character of n essentially; purely local/genus/spinor/
  Siegel–Weil/equidistribution-in-the-mean steps are true at m² and cannot carry it.
* F2: numerator 8: 8/n fails at n = 131, 241 (and the C-even sub-line R₈(p) = 0 at primes up to 2.3·10¹⁰). A step valid
  uniformly for numerators M ≡ 0 (4) with no threshold proves false statements.
* F3: composite non-square n where the (★) line is zero; F4: the 14 known primes ≤ 10¹⁰ with R(p) = 0 (409 … 8 813 281)
  ((★) failing is not ES failing, but an argument "R(p) ≥ 1 for all p" must have a threshold beyond them).

## Exceptional-set line (secondary target)
E(N) = #{n ≤ N : ES fails}. Vaughan 1970: N·exp(−c(log N)^{2/3}). Campaign (internal) and, earlier, Kandukoori–Ramesh–Kumar
(PDF 2026-07-29, Lean-formalised): **N·exp(−c(log N)^{3/4})**. Campaign theorem (internal): 3/4 is *sharp for every
CRT / coefficient-sum / all-level large-sieve architecture analysed* (`STATUS.md` "Exceptional-set exponent", `EXCEPTIONAL_KARY3.md`,
`paper/sieve-limits-note.tex`); θ > 3/4 needs genuinely non-CRT input (tuple counts of growing order, residue-dense
large sieves (A*), weak SPW, per-frequency weights). Known prior art by Dahan: arXiv:2608.24035 (in `sources/dahan-2608.24035v1.pdf`).

## Recent world facts the repo already knows (do NOT re-report as new)
OpenAI's `openai/math` release (Oct 2026): quasi-RH (Dirichlet L zero-free for Re s > 7/8), no Landau–Siegel zeros, etc.
(`OAI_DUMP_IMPACT.md`, `OAI_METHOD_003.md`). Ventas 2610.41027, Cao–Xu 2610.32302, Jiang 2609.09204, Akaka Zenodo v0.8,
K-R-K, Pomerance–Weingartner, Bright–Loughran, Elsholtz–Tao, López 2024, Banks 2610.15483, Banks–Shparlinski 2610.19597.
Every arXiv id cited anywhere in the repo is in `data/z71/lit/repo_arxiv_ids.txt` (grep it before calling something new;
also `git grep -n -i <author or keyword> -- '*.md'` to see what the repo already says).

## Rules for your report
* PDFs and `pdftotext -layout` text for the papers named in your task are already in `data/z71/lit/sources/<arxivid>.{pdf,txt}`.
  Read the .txt with the read tool (offset/limit); fetch other sources with curl only if needed (arXiv: be polite, ≥3 s between requests).
* Quote theorem/definition statements **verbatim** (or near-verbatim, fixing only PDF-extraction garbling) with theorem number and
  the .txt line number. Mark each item: READ (which sections) vs ABSTRACT-ONLY. Do not audit proofs; do say when a paper looks
  unrefereed/AI-generated/implausible and why (concrete red flags only).
* Separate clearly: (i) *facts from the source*; (ii) *your relevance pointers* labelled "Assessment (unreviewed)". Do not issue
  final verdicts; the orchestrator will review. Be blunt when nothing is there.
* For every mechanism you think is transferable, say in one line what happens at F1 (odd squares) and F2 (numerator 8) if you can tell.
* No heavy computation (no process > 2 GB RAM, nothing > 5 min). No `find` over the repo; use `git grep`. Do not modify any repo
  file other than your output note. Do not commit.
* Write your full note to the path given in the task (markdown, ≤ ~600 lines) and return a ≤ 400-word summary: top 3 findings,
  anything surprising, and what you could not check.
