# Paper draft status

`espaper.tex` is the v4 standalone `amsart` consolidation draft (45 pages). Its two headline results are:

- `E_all(N) ≪ N exp{-c(log N)^(3/4)}`;
- for every fixed `epsilon > 0`, uniformly for `3 <= m <= (log N)^(3-epsilon)`,
  `E_m(N) ≪_epsilon N exp{-c_epsilon(eta_2(m)(log N)^3/phi(m))^(1/4)}`.

Both remain visibly **CLAIMED/PROVISIONAL**. The general-numerator headline inherits the likewise provisional source Theorem 34.8, paper Theorem `m-pruned`, and every source §39.7 qualification. “Unconditional” means only that no unproved hypothesis is assumed; it does not mean externally validated. The paper does not claim a proof of the Erdős–Straus conjecture.

## v4 changes

- Promoted source Theorem 43.12 to the abstract, introduction, and general-`m` headline. Its proof includes the finite relative-mass inequality (43.36), thinned quarantine and Bonferroni degree, `O(Mt)` ledger, full `m <= (log N)^(3-epsilon)` audit, and uniform semigroup transfer. Source Theorem 43.8 remains as the one-sentence conservative linear-thinning variant.
- Replaced the old Pomerance–Weingartner comparison by the adjudicated scales `R=(eta_2/phi)^(1/4)L^(3/4)` and `P=L^(2/3)/phi^(1/3)`, exact ratio/crossover (43.33)–(43.34), common-domain comparison, and separate `L^(3-epsilon)` range discussion. Layer 1 now has its repaired all-denominator range `m <= L^(2-epsilon)`.
- Extended the verification pedigree with the source §43.11 attested-blind protocol, freeze commit, convergence/divergence scope, and hostile strengthening adjudication. It remains explicitly internal.
- Added the §47 nested squarefree divisor cube. It refutes literal raw targets (40.28) and (37.19), not `H_PF'`, pair target (40.19), or the conjecture. The implication antichain preserves the void, and (47.16) is the exact replacement **OPEN** wall.
- Extended the endpoint frontier from Theorem 45.9’s injective `W_0` prefix to `W_1 ~ L^5 loglog L/(log L)^2` and the wedge `c >= z, m <= zW_1`. The distinct-cell collision sum (46.13) is the exact current **OPEN** pair remainder.
- Added source Theorem 48.1 in full, the fixed-divisor law (48.16)–(48.17), residue-one escape (48.20), and the finite depth census. Pointwise Type-I existence remains the conjectural target; no progress claim is made.
- Updated the abstract/frontier/status register, compacted already-resolved bibliography entries without adding citation keys, and regenerated the tracked table of contents.

## Wave-17 v4 fidelity review

- Review: `reviews/wave17-paper-v4-review.md`; verdict **FAITHFUL-AFTER-REPAIRS** after minimal source-§49 status corrections; two-pass build clean.
- wave-17: the antichain hierarchy is also refuted (notes §49); moment route closed; v5 queue.

## Resolved v3 errata

The pending v4 structural erratum in the wave-16 fidelity review is resolved: v4 no longer calls raw (37.19) or literal (40.28) open, states their precise refutation scope, and names implication-antichain (47.16) as the repaired open hierarchy. The review’s “do not insert an unadjudicated strengthening” guard is also resolved correctly: only the later hostile-adjudicated Theorem 43.12 is promoted, with every provisional label retained. The post-freeze Layer-1 all-denominator range correction and the §46 endpoint refinement are now incorporated.

## Statement fidelity

Every new or changed theorem statement was diffed against the post-review `notes.md` text symbol by symbol:

- notes Theorem 43.4, (43.13)–(43.15) ↔ `general-two-third`: unchanged exponent and local factor; both prime and all-denominator ranges are now exactly `m <= L^(2-epsilon)`.
- notes Theorem 43.8, (43.28) ↔ `general-three-quarter-conservative`: `eta_1(m)/phi(m)`, `L^(3/4)`, range `m <= L^(3/4-epsilon)`, primes and all denominators, and inherited status all agree.
- notes PW (43.32)–(43.34) ↔ paper (43.32)–(43.34): `R/P={eta_2(m)^3 phi(m)L}^(1/12)` and crossover `L >= 1/(eta_2(m)^3 phi(m))` agree; no old `eta_1` crossover or uniform-beating claim remains.
- notes Theorem 43.12, (43.35) ↔ `general-three-quarter`: `≪_epsilon`, `c_epsilon`, fourth root, `eta_2(m)L^3/phi(m)`, exact `3 <= m <= L^(3-epsilon)` range, prime/all-denominator scope, and all inheritance caveats agree.
- notes (43.36)–(43.42) ↔ the new proof: finite cutoff `K`, coefficient `(1-1/p)/p^e`, bound `H_m(K)/p`, fixed relative threshold, `M=eta_2(m)t^3/phi(m)`, `y,r=O(M)`, `O(Mt)` ledger, `t=alpha(L/theta_m)^(1/4)`, fixed-gap constraints, and semigroup `gamma` agree.
- notes §43.11 and Assessment 43.13 ↔ `pedigree` and the thinned-window preface: allowed reads, freeze hash, self-attestation limitation, S3/S6/S7 qualifications, adjudicated checks, verdict, and unchanged provisional status agree.
- notes Theorem 47.2, (47.10)–(47.14) ↔ `nested-cube`: squarefree top atom, `exp(cL/log L)` extension mass, conditioned raw-`H` moment failure for every fixed `C`, and the `Y`-to-`2Y` odd-subset mechanism agree.
- notes (47.16) ↔ `antichain-wall`: deletion direction, unchanged union/void, `Q_S`, `w_B`, every shared prime-power factor in `Gamma_S`, compatible-set quantifiers, even `m in [D Lambda,D Lambda+2]`, and `C Lambda` right side agree.
- notes Theorem 46.2, (46.8)–(46.10) ↔ `endpoint-wedge`: `W_1=floor(zL^2/log L)`, `W_2=floor(zW_1)`, full prefix, large-`c` wedge, and `O(Lambda^2)` conclusions agree. The preceding displayed diagonal/occupancy inequalities reproduce (46.3) and (46.9).
- notes Corollary 46.3, (46.11)–(46.13) ↔ `endpoint-core`: the sets `A,B`, ordered distinct-cell condition `m != m'`, congruence modulo `p`, weight `G_{m,p}G_{m',p}/p`, prime range, and equivalence to (40.19) agree.
- notes Theorem 48.1, (48.1)–(48.3) ↔ `moving-genus`: fundamental discriminant character, admissible hard-prime scope, implication `chi_s(p)=1 => M_{c,k}(p)=0`, exact set `{1,2,3,6}`, relative density `1/2`, and finite exclusions agree.
- notes Theorem 48.4, (48.15)–(48.17) ↔ `fixed-divisor-slice`: paper `L_d` is the notes’ local `L`; all three congruences, reduced-class and admissibility scope, explicit `e,a,b`, necessity within the fixed-`d` shape, and refinement clause agree.
- notes Theorem 48.5, (48.20)–(48.21) ↔ `slice-residue-one`: no residue one, bounded full-modulus union, `Lambda_Q`, infinite prime class, and factor-size contradiction agree.
- notes (48.8)–(48.14) ↔ the depth paragraph: `D=ck_min-1`, `385`, `77`, `(12289,76)`, `1181`, `103`, and `(92401,102)` agree and remain computational only.

The retained v3 correspondences were also rechecked after the edits:

- notes (43.2)–(43.3) ↔ `m-identity`, including positivity;
- notes (43.4), (43.6)–(43.9) ↔ `m-thinning`, including `eta_1`, `eta_2`, `C_2`, aggregate scope, and no `(uv,m)=1` assumption;
- notes (43.10)–(43.23) ↔ `m-class-mass`, `m-profiles`, and `m-pruned`, including the prime domain, product modulus `muv`, reduced-fibre quantifier, and `1/phi(m)`;
- notes (43.24)–(43.27) ↔ the unequal-prime-power moment replay and mixed local-factor correction;
- notes (44.3)–(44.16) ↔ raw slice vanishing, primitive caveat, `80/111`, `15/385`, and the retained `p=2521` datum;
- notes (42.1)–(42.17) and Theorem 45.9 ↔ endpoint uniqueness, collision law, fixed fibres, Kloosterman matrix, DFI/BC quantifiers, and `W_0` injectivity;
- notes §41.1–§41.5 and §34.5 ↔ all verification counts and internal-only caveats.

No statement discrepancy remains from this pass.

## Build and hygiene

Run from `paper/`:

```sh
pdflatex -interaction=nonstopmode espaper.tex
pdflatex -interaction=nonstopmode espaper.tex
```

The v4 build completes with zero TeX errors and no undefined references or citations. The PDF is 45 pages and is generated locally, not tracked; `espaper.toc` is tracked and updated. Manual source-style equation tags retain the pre-existing duplicate-destination `hyperref` warnings, which are not unresolved references. The control-byte scan of `espaper.tex` is zero.

## Submission TODO

- Obtain external expert review of Theorem 34.8, the §39 chain, and the full thinned-window §43 transfer.
- Obtain/read Vaughan 1970 and complete the priority search.
- Prove or disprove endpoint remainder (46.13); carry notes §49’s antichain and reduced-moment refutations into v5.
- Settle author metadata and perform a final line-by-line referee audit.
