# Paper draft status

`espaper.tex` is a standalone 20-page `amsart` consolidation draft of the intrinsic-system / H_PF arc. It is not submission-ready and does not claim a proof of the Erdős–Straus conjecture.

## Compile status

Verified with the repository host's `/usr/bin/pdflatex`:

```sh
mkdir -p /tmp/es-paper-build
pdflatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/tmp/es-paper-build paper/espaper.tex
```

Three passes complete with zero errors and resolved references. The generated PDF and auxiliary files live outside the repository and are not committed. `lacheck paper/espaper.tex` also exits successfully; its remaining messages are cosmetic false positives about set braces and factorial punctuation.

## Included

- Complete prime-denominator criterion and forced identity families.
- Exact intrinsic classes `{-4D mod M : D | ((M+1)/4)^2}` and cubic class-mass theorem.
- Jacobi-sign/square escape, prime-slice mass, two-sided prime-slice avoidance, and the multi-shift certificate.
- Literal H_PF quantifiers, its conditional 3/4 consequence, weighted rough-modulus and softened-neighborhood proofs, the natural-density lower bound, and the full-quantifier refutation.
- Open critical-window H_PF' with the cylinder wall, non-tensor example, monomial and residue-set transfer criteria, prime-side two-level minorant, factorial-moment reduction, and residue-dispersion frontier.
- Brief record context for Theorem 16.4 and Theorem 34.8, both kept visibly `CLAIMED/PROVISIONAL` with their internal arguments and caveats.
- Bibliography entries requested in the brief, based on `sources/README.md`, supplied PDF front matter, and explicit TODO comments where publication status remains unverified.

## Excluded

- Computational tables, finite-fit heuristics, and exploratory/assessment material not needed for this paper's theorem chain.
- Other research-log arcs, including pointwise tuple dynamics and computational frontier searches.
- A sharpened theorem from §27 beyond the specifically requested §24.8 result.
- Any PDF, `.aux`, `.log`, `.out`, or `.toc` artifact.

## Priority and verification status

Vaughan's primary paper is R. C. Vaughan, “On a problem of Erdős, Straus and Schinzel,” *Mathematika* 17 (1970), 193–198, DOI `10.1112/S0025579300002886`. The publisher and Cambridge records were found, but primary PDF access remained blocked. The provisional record comparison was checked only against Pomerance–Weingartner's 2025 reconstruction, whose §4 says it largely follows Vaughan. The draft states this explicitly and does not represent Vaughan's paper as directly read.

## Transcription flags

- Notes §31.4 contains a malformed TeX fragment in the definition of `P_z` (`p\ {m prime}` in the source text). It is transcribed as “odd prime `p <= z`”; this is a typography repair, not a mathematical change.
- Notes §33.3's monomial coefficient ledger is valid for compatible atom monomials, but §37.1 later corrects the general residue-set ledger by inserting the class count `rho(U)`. The paper presents §33.3 only as the monomial corollary of the corrected §37.1 statement.
- Stale pre-§31 status prose saying H_PF was merely “false-looking/open” is not reproduced as current status; the paper follows the explicit supersession pointers and §31's proved refutation.
- No additional proof gap was identified while transcribing. The two campaign records remain provisional for external review rather than being silently upgraded by this consolidation.

## Submission TODO

- Settle author, affiliation, acknowledgments, and date metadata.
- Obtain independent referee checks of the §31 Henriot/local-lemma chain and the literal-quantifier refutation.
- Complete priority searches and external verification for the provisional Theorems 16.4 and 34.8, especially the power-range Shiu/box extension and incidence boundary estimate.
- Obtain/read Vaughan's primary paper and reconcile the historical record directly.
- Confirm final publication metadata for Pomerance–Weingartner and whether Salez has a journal version; update the `% TODO(submission)` bibliography comments.
- Add precise citations for standard Bombieri–Vinogradov, Brun–Titchmarsh, Bonferroni, and maximal-order divisor inputs if required by the target journal.
- Perform a line-by-line source audit and a separate mathematical referee pass before changing “draft” status.
