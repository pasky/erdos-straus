# Paper draft status

`espaper.tex` is the v3 standalone `amsart` consolidation draft. It is about 40 pages and has two headline-class results:

- `E_all(N) ≪ N exp{-c(log N)^(3/4)}`;
- for every fixed `m >= 3`, `E_m(N) ≪ N exp{-c eta_1(m)(log N)^(3/4)/phi(m)}`.

Both remain visibly **CLAIMED/PROVISIONAL** and depend on the likewise provisional pruned cubic prime-slice theorem (the source notes' Theorem 34.8). “Unconditional” means that no unproved hypothesis is assumed; it does not mean externally validated. The draft does not claim a proof of the Erdős–Straus conjecture.

## v3 additions

- Full §43 general-numerator chain: the `m`-uniform identity, exact `eta_1` and `eta_2` thinning factors, aggregate `(k,m)=1` treatment, class-mass proof with modulus `muv`, first `2/3` layer, provisional cubic transfer, unequal-prime-power moment replay, conservative `y,r ~ (log X)^3` ledger, and the repaired `epsilon/4` semigroup cutoff.
- Exact uniformity ranges: prime/all-denominator first layer through `m <= (log N)^(2-epsilon)` / `m <= (log N)^(1-epsilon)`, and the provisional `3/4` layer through `m <= (log N)^(3/4-epsilon)`.
- Honest Pomerance–Weingartner comparison: the crossover is `phi(m) ≲ eta_1(m)^(3/2)(log N)^(1/8)` up to theorem constants; PW is better for larger `m`, so v3 makes no uniform-beating claim.
- Verification pedigree: §41's attested-blind S1–S7 reconstruction and caveats, §34.5's third internal Theorem 34.8 check against Shiu's 1980 hypotheses, two v2 fidelity passes, and the three repaired wave-15 hostile reviews. These are explicitly internal checks, not external validation.
- Brief §44 pointwise subsection: raw slice vanishing, the raw/primitive boundary, the squarefree-`c`-core obstruction, the exact small-box conspiracy census, and the explicit statement that all-prime slice positivity would prove the Type-I Erdős–Straus conjecture.
- Expanded frontier: §42 unique-cofactor/complement-divisor normal forms, fixed-`s` and fixed-polylog-prime closure; §45's exact Kloosterman matrix, DFI/Bettin–Chandee quantifier audit; and Theorem 45.9 closing `4c^2s <= (log X)^3/(loglog X)^2` over the full endpoint prime range. The complementary bulk and all higher codegrees remain open.
- Bibliography entries for Duke–Friedlander–Iwaniec and Bettin–Chandee. DFI is checked against the archived full 1997 PDF. Vaughan 1970 remains inaccessible and is discussed only through Pomerance–Weingartner plus confirmed metadata.

## Compile status

Run from `paper/`:

```sh
pdflatex -interaction=nonstopmode espaper.tex
pdflatex -interaction=nonstopmode espaper.tex
```

The v3 build completes with zero TeX errors and no undefined references or citations. The PDF and auxiliary files are generated locally and are not tracked. `espaper.toc` is tracked and updated. Manual source-style equation tags produce pre-existing duplicate-destination `hyperref` warnings; they are not unresolved references.

## Included foundation

- Complete prime-denominator criterion and forced identity families.
- Exact intrinsic classes `{-4D mod M : D | ((M+1)/4)^2}`, cubic class mass, Jacobi-sign/square escape, prime-slice avoidance, and the multi-shift certificate.
- Literal `H_PF`, its conditional consequence, weighted rough-modulus and local-lemma proofs, and the full-quantifier refutation.
- Critical-window transfer walls, prime-side minorant, composite factorial-moment reduction, complete fixed-`c`-free §39 assembly, honest `exp(O(J log X))` ledger, and semigroup transfer.
- The proved regular dispersion tail and the exact still-open endpoint target, now narrowed by §§42 and 45.

## Fidelity note

The v3 statements were checked directly against the post-review source text in `notes.md`. The following correspondences were rechecked symbol by symbol:

- notes (43.2)–(43.3) ↔ Lemma `m-identity`: hypotheses `k ell = -1 (mod m)`, `A=(k ell+1)/m=uvw`, and all three denominators;
- notes (43.4), (43.6)–(43.9) ↔ `m-thinning` and the exact `F_m` identity, including `eta_1`, `eta_2`, `C_2`, fixed-class versus aggregate scope, and no `(uv,m)=1` assumption;
- notes (43.10)–(43.15) ↔ `m-class-mass` and `general-two-third`: product modulus `muv`, `1/phi(m)`, theorem exponent, and all three uniformity ranges;
- notes (43.16)–(43.27) ↔ the c-free atoms, profiles, reduced-fibre quantifier in `m-pruned`, conditioned local-factor correction, and factorial-moment base;
- notes (43.28)–(43.31) ↔ `general-three-quarter`: `eta_1(m)/phi(m)`, `m <= (log N)^(3/4-epsilon)`, conservative degree/ledger, and the repaired cutoff `x_0=exp{m^(1/(3/4-epsilon/4))}`;
- notes (43.32)–(43.34) ↔ the PW theorem and two-regime crossover, with no uniform-beating claim;
- notes (44.3)–(44.4a), (44.8)–(44.10), and (44.16) ↔ the raw vanishing law, primitive caveat, four squarefree cores, `80/111`, and the seven-column census;
- notes (42.1)–(42.8), (42.10)–(42.11), and (42.17) ↔ endpoint uniqueness, collision law, fixed-fibre estimate, and fixed polylogarithmic prime range;
- notes (45.2)–(45.5), DFI (45.10), BC (45.12), and Theorem 45.9 (45.26) ↔ the exact matrix, both reciprocity orientations, actual coefficient quantifiers, `W_0 <= z/2`, and `W_0=floor(L^3/(log L)^2)`;
- notes §41.1–§41.5 and §34.5 ↔ the verification-pedigree counts and the attested-blind / internal-only caveats.

The initial v3 assembly pass reported no old paper/notes transcription error. The later hostile wave-16 fidelity review found and repaired the statement-domain and source-provenance defects listed below; the earlier eaten-backslash repairs recorded by v2 remain intact.

## Wave-16 v3 fidelity review

`reviews/wave16-paper-v3-review.md` records a **FAITHFUL-AFTER-REPAIRS** verdict. The repair restored the positivity hypotheses in the general-numerator identity, restored the prime domain in the general-$m$ class-mass lemma, retained the specifically requested $p=2521$ census datum, and limited the Bettin--Chandee bibliography entry to the archived arXiv source. No unadjudicated $[\eta_2(m)/\varphi(m)]^{1/4}$ strengthening was inserted.

**Pending v4 structural erratum (§47):** v3's statements that the raw factorial-moment target (37.19) and literal codegree target (40.28) remain open are now stale: notes §47 refutes both for the unreduced count $H$ and replaces them with the still-open implication-antichain target (47.16). The endpoint target (40.19) remains open; the v3 frontier text is intentionally not rewritten in this review.

## Priority and verification status

Vaughan's primary paper is R. C. Vaughan, “On a problem of Erdős, Straus and Schinzel,” *Mathematika* 17 (1970), 193–198, DOI `10.1112/S0025579300002886`. Its PDF remains access-blocked. Pomerance–Weingartner §4 reconstructs and cites Vaughan as the state of the art, and the campaign search found no post-1970 exponent improvement. This is search-limited evidence, not a literature guarantee. Do not remove any provisional label without independent expert review and a completed primary-literature check.

## Submission TODO

- Obtain external expert review of Theorem 34.8, the §39 chain, and the full §43 transfer.
- Obtain/read Vaughan 1970 and complete the priority search.
- Settle author metadata and final publication data for Pomerance–Weingartner and Bettin–Chandee.
- Prove or disprove the endpoint bulk `4c^2s > W_0`, then address prime-power and multi-coordinate codegrees.
- Add standard-reference citations if required by the target journal and perform a final line-by-line referee audit.
- wave-16 adjudication of the thinned-window strengthening: STRENGTHENING CONFIRMED; paper update pending next paper pass.
