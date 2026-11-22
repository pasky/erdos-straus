# z81 LIT subagent brief (shared context)

Repo: /home/pasky/projects/math/erdos-straus-claude-agent-worktree-0012 (Erdős–Straus campaign). ES: 4/n = 1/x+1/y+1/z
in positive integers for every n ≥ 2. **ES is OPEN.** Never overclaim. Today is 2026-11-22.

Papers are in `data/z81/lit/src/<arxivid>.pdf` with `pdftotext -layout` output `<arxivid>.txt` (cite line numbers of the
.txt). Listing metadata: `data/z81/lit/all.tsv`, `authors.tsv`.

Campaign essentials (do not re-derive; just use as relevance filter):
* Everything ends at **B2**: at one fixed prime p, one integer (e.g. (p+e)/4-type side number, or 4Cn+1) must have a
  divisor in ONE residue class (−1) modulo a modulus that itself moves with the solution; expected count is only
  ~log²p. Averages over p / over shifts / over moduli do not reach a fixed p (screen B6). Quadratic-character / Chebotarev
  / genus information gives only the quadratic shadow of the class, not the class (screen 9). Any mechanism must fail at
  odd squares n = m² (F1), must not also prove 8/n at n = 11, 17, 131, 241 (F2: numerator-8 blindness), must respect the
  composite zero 4545 and Z₇ = {105,1465,3865,4545,10305,12145,39361,67425} (F3), and the (★)-zero primes
  409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, …, 8 813 281 and composite 17,401,609 (F4).
* Known results: E(N) ≪ N exp(−c (log N)^{3/4}) for the exceptional set (campaign note + Kandukoori–Ramesh–Kumar 2026;
  Dahan arXiv:2611.08717 gets 5/7); numerators m ≥ 4 variant with m^{−1/4} dependence; FHRSS arXiv:2504.20289 Thm 1.1(2)
  (primes represented by shifted quadratic forms) gives single-window failure counts X/log^{3/2}X for g(p)=4x_min−p.

The seven z81 lanes (what to look for):
1. cap-zero: bounded/zero valuation cap e* for a capped relaxation (common-exponent barrier r−1 | L).
2. gap: pointwise multi-window coupling on g(p) = min(4x − p); want g ≥ 11 infinitely often ⇒ needs JOINT lower bounds
   for primes p where several shifted quadratic-form / divisor-window conditions fail simultaneously (simultaneous primes
   in several linear forms + quadratic norm forms, half-dimensional sieves with several windows, FHRSS multi-form).
3. b2-duality: Type I/II duality, amicable cubic p+e+b = ebt, Vieta involutions / elliptic fibrations on
   4xyz = p(xy+yz+zx), Markoff-type orbit arguments.
4. specific-class: breaking 3/4 on E(N): large-modulus dispersion, bilinear Kloosterman forms, character bias,
   Bettin–Chandee(–Radziwiłł) Kloosterman-fraction trilinear forms, ratios conjectures.
5. farey-proof: weak arithmetic IE₁⁻ / IOpen vs ES: Farey, prime short vectors, Gauss reduction, factorial splitting,
   Diophantine definability.
6. s-u7: reciprocal bichromatic pairs, class groups / Rédei 4-rank, products of primes in residue classes.
7. geom-comb: inhomogeneous geometry of numbers / covering radius, smooth-x / smooth-k divisor-box additive
   combinatorics (Davenport constant, Kneser, sum-product, zero-sum), polynomial method.

Output rules: quote theorem statements ONLY from the opened .txt with theorem number + line numbers; say "proof not
audited". For each paper give: exact main theorem(s) (verbatim, compact), averaged variables (is anything pointwise in a
fixed n/p?), which lane(s) it could serve and HOW concretely (a usable lemma? a technique?), and a trap/limitation.
Keep each paper ≤ 25 lines. Write ONLY your output file under `data/z81/lit/notes/`. Do not edit anything else, do not
commit.
