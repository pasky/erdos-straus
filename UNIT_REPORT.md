# UNIT D15 report

## Outcome

The Kloosterman-fraction technology does **not** close (40.19).  Section 45 gives an exact endpoint matrix

\[
G_{4c^2s,p}=\sum_q \kappa(pq)/q
\]

with every roughness, cofactor, canonical, and retention condition carried.  Its full Parseval norm is exactly \(\mathcal V_X^{\rm end}\).  The key audit result is that DFI/BC permit arbitrary separate one-variable sequences, not the joint coefficient matrix \(G_{m,p}\).  Exact singular-value decomposition makes DFI applicable but introduces a nuclear norm; summing the complete \(h\)-range then overwhelms the scalar saving.

The cofactor orientation also fails exactly: reciprocity changes the modulus from \(p\) to \(m=4c^2s\), while the valid lift has modulus \(pq\).  It never produces modulus \(q\) in general.

## Proved additions

- `notes.md` §45: exact reduction Lemma 45.1, coefficient \(\ell^1/\ell^2\) audit, exact DFI and BC quantifiers and scale windows, DFI nuclear-norm Lemma 45.2, strongest assembled partial Proposition 45.3, and three exact failure logs.
- `verify.py (ar)`: independently reconstructs the toy endpoint systems, forms the joint matrix, checks both reciprocity identities and exact Parseval equality, and reports exact rational coefficient norms.
- `sources/bettin-chandee-1502.00769.pdf`: arXiv PDF archived with SHA-256 provenance in `sources/README.md`.

A legitimate full open DFI copy was not found.  Springer is paywalled and the ProQuest open result exposes only a one-page preview, so no incomplete PDF was committed as the paper.

## Remaining status

The strongest closed family remains fixed-polylogarithmic primes plus at most \(O(L^{3/2}/\log L)\) prescribed fixed-\(s\) fibres.  The moving-\(s\) range \(L^B<p\le X/z\), (40.19), and (37.27) remain open.  Even closing them would leave (40.28), (37.19), (33.16), and the internal refutation of \(H_{\rm PF}'\) open; this arc does not settle the Erdős–Straus conjecture.

## Verification

- `ast.parse(verify.py)`: pass.
- Control-byte scan of `notes.md`: zero.
- `uv run --with sympy,numpy,scipy python verify.py`: pass, including block (ar).
