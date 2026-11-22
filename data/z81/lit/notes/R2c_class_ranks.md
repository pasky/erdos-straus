# z81-s-u7 — joint class-rank literature (arXiv 2024-01-01..2026-11-22)

## Relevant hit

**Xu–Zhu, “Asymptotic independence of class-group 4-ranks in correlated pairs of imaginary quadratic fields,” arXiv:2608.00387v1 (2026).** PDF/text: `data/z81/lit/src/2608.00387.pdf`, `.txt`.

> “Theorem 1.1. Let \(d_0>1\) be squarefree. There exists \(c=c(d_0)>0\) such that \(d_{TV}(\mu_X^{(d_0)},\pi_{CL}\otimes\pi_{CL})\ll_{d_0}(\log\log X)^{-c}.\)” (txt lines 141–147; symbols normalized from layout text.)
>
> For \(d_0=2\), “as \(d\) ranges over the odd squarefree integers, \(\mathbb Q(\sqrt{-d})\) and \(\mathbb Q(\sqrt{-2d})\) run respectively through the families … Theorem 1.1 shows that, under the natural pairing \(d\mapsto2d\), their class-group 4-ranks are asymptotically independent.” (lines 147–151.)
>
> “Theorem 1.3. Assume that the class number of \(k_0=\mathbb Q(\sqrt{d_0})\) is odd. For all but \(o(\#F_{d_0}(X))\) values \(d\in F_{d_0}(X)\), … extension of ideals induces an isomorphism \(4\,\mathrm{Cl}_{K(d)}[2^\infty]\cong\bigoplus_{i=0}^2 2\,\mathrm{Cl}_{k_i(d)}[2^\infty]\).” (lines 178–186; layout line breaks elided.)

- **Pointwise vs averaged:** averaged over *all positive squarefree* \(d\le X\), coprime to \(2d_0\), not a pointwise relation; the theorem asserts asymptotic independence, not a constraint linking the two ranks at each parameter. For \(d_0=2\), the paired fields include \(\mathbb Q(\sqrt{-p})\), \(\mathbb Q(\sqrt{-2p})\) when \(d=p\), but primes are a sparse subfamily and the theorem gives no prime-subfamily result. Theorem 1.3 is also density-one in squarefree \(d\), not pointwise.
- **Verdict:** strongest recent direct match: genuine cross-field, same-parameter 4-rank theorem, with explicit d0=2 twist pair; useful as an averaged model/technique, not a fixed-prime forcing mechanism. No 8-/16-rank pointwise relation.
- **Trap:** do not turn “asymptotically independent” into “independent for each p” or infer any forced rank combination. The full 2-primary-group independence is Conjecture 1.2, not proved; theorem proves its 4-rank projection only (lines 153–173). The paper itself says the 2-ranks have a deterministic genus-theoretic relation (lines 78–82), but that is not a higher-rank pointwise relation.
- **Repo novelty:** already covered by `Z53_LIT.md:138` (abstract-level summary, including “no pointwise-in-p joint-class statement found”); `git grep` finds no other note citing this arXiv ID. Proof not audited.

## Other screened results

- **Joppe Stokvis, arXiv:2505.20117**, “Governing fields for hyperelliptic function fields”: 8-rank governing fields are for *function-field* class groups, not quadratic number fields; no cross-field fixed-prime theorem. Not pursued to full text.
- **Ngiza Mfumu–Maire, arXiv:2407.03754**, “Genus theory, governing field, ramification and Frobenius”: governing-field genus-rank matrices for number-field extensions, but the quadratic-over-Q specialization is built from Legendre symbols among ramified primes; no joint 4/8/16-rank theorem for the requested imaginary quadratic twist pair. Abstract only.
- Searches produced no other directly relevant new pointwise/joint number-field result. Pre-2024 works on joint 16-ranks of \(\mathbb Q(\sqrt{-p})\), \(\mathbb Q(\sqrt{-2p})\) are outside this date window; 2608.00387 itself cites them (txt lines 94–100).

## Queries / hit counts

- `abs:"8-rank" OR abs:"16-rank" OR abs:"4-rank"`: 31 API hits; relevant number-field joint hit: 2608.00387 (plus unrelated function-field result 2505.20117).
- `abs:"governing field"`: 13 API hits; relevant number-field cross-field rank hit: none additional (2407.03754 is genus theory only).
- `all:"joint distribution" AND (all:"class group" OR all:"class groups")`: 1 API hit, 2608.00387.
- Author search `au:"Koymans" OR au:"Milovic" OR au:"Chan" OR au:"Smith" OR au:"Pagano"` failed with arXiv API HTTP 429 on retries; no result inferred from that failed query. Web search used as a supplementary check.
