# Paper draft status

`espaper.tex` is the v5 standalone `amsart` consolidation draft (54 pages). Its two headline results are:

- `E_all(N) ≪ N exp{-c(log N)^(3/4)}`;
- for every fixed `epsilon > 0`, uniformly for `3 <= m <= (log N)^(3-epsilon)`,
  `E_m(N) ≪_epsilon N exp{-c_epsilon(eta_2(m)(log N)^3/phi(m))^(1/4)}`.

Both remain visibly **CLAIMED/PROVISIONAL**. The general-numerator headline inherits the likewise provisional source Theorem 34.8, paper Theorem `m-pruned`, and every source §39.7 qualification. “Unconditional” means only that no unproved hypothesis is assumed; it does not mean externally validated. The paper does not claim a proof of the Erdős–Straus conjecture.

## v5 changes — 2026-08-29, wave 18

- Absorbed source §49's exact implication criterion, pointwise antichain void identity, failure of a uniform residue profile, and complete-bipartite semiprime grid. The grid refutes both repaired hierarchy (47.16) and the ordinary factorial-moment target for the reduced count, with the full every-even-`m`, pairwise-coprime squarefree, extension-ratio-one, and conditional CRT-cost quantifiers retained.
- Reclassified the complete-system hierarchy/moment axis as **DORMANT**. The nested cube remains the refutation of the raw formulations; the grid is the separate collective refutation of their antichain replacements. Proposition 47.3's prime-only rung survives, while `H_PF'`, (33.16), (37.27), and (40.19) remain open.
- Added source §50 as a new conditional pointwise section: the proved one-prime-factor slice criterion and explicit Type-I reconstruction, bespoke unproved `H_SPF(A)`, its conditional consequence, prime-norm and bounded-core walls, the GRH active-slice-only theorem, the GRH/Chebotarev mass audit, exact genus pairing, Duke assessment, frontier table, and exact finite census.
- Preserved the section's scope: §50 is a conditional reduction and map of missing input, not an unconditional theorem. The provisional record labels, source §39.7 qualifications, Vaughan-access warning, Pomerance–Weingartner comparison limits, and internal-only verification register are unchanged.
- Extended the internal pedigree with the hostile §49 and §50 reviews, updated the abstract/introduction/status register, and regenerated the tracked table of contents.

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
- wave-17: the antichain hierarchy is also refuted (notes §49); the pending paper absorption is resolved in v5.

## Resolved v3 errata

The pending v4 structural erratum in the wave-16 fidelity review was resolved in v4: raw (37.19) and literal (40.28) were no longer called open, and implication-antichain (47.16) was identified as the then-current repair. V5 now absorbs source §49's later refutation of that repair and of the reduced-count moment itself. The review’s “do not insert an unadjudicated strengthening” guard remains resolved correctly: only the hostile-adjudicated Theorem 43.12 is promoted, with every provisional label retained. The post-freeze Layer-1 all-denominator range correction and the §46 endpoint refinement remain incorporated.

## Statement fidelity

Every new or changed theorem statement was diffed against the post-review `notes.md` text symbol by symbol:

- notes Theorem 43.4, (43.13)–(43.15) ↔ `general-two-third`: unchanged exponent and local factor; both prime and all-denominator ranges are now exactly `m <= L^(2-epsilon)`.
- notes Theorem 43.8, (43.28) ↔ `general-three-quarter-conservative`: `eta_1(m)/phi(m)`, `L^(3/4)`, range `m <= L^(3/4-epsilon)`, primes and all denominators, and inherited status all agree.
- notes PW (43.32)–(43.34) ↔ paper (43.32)–(43.34): `R/P={eta_2(m)^3 phi(m)L}^(1/12)` and crossover `L >= 1/(eta_2(m)^3 phi(m))` agree; no old `eta_1` crossover or uniform-beating claim remains.
- notes Theorem 43.12, (43.35) ↔ `general-three-quarter`: `≪_epsilon`, `c_epsilon`, fourth root, `eta_2(m)L^3/phi(m)`, exact `3 <= m <= L^(3-epsilon)` range, prime/all-denominator scope, and all inheritance caveats agree.
- notes (43.36)–(43.42) ↔ the new proof: finite cutoff `K`, coefficient `(1-1/p)/p^e`, bound `H_m(K)/p`, fixed relative threshold, `M=eta_2(m)t^3/phi(m)`, `y,r=O(M)`, `O(Mt)` ledger, `t=alpha(L/theta_m)^(1/4)`, fixed-gap constraints, and semigroup `gamma` agree.
- notes §43.11 and Assessment 43.13 ↔ `pedigree` and the thinned-window preface: allowed reads, freeze hash, self-attestation limitation, S3/S6/S7 qualifications, adjudicated checks, verdict, and unchanged provisional status agree.
- notes Theorem 47.2, (47.10)–(47.14) ↔ `nested-cube`: squarefree top atom, `exp(cL/log L)` extension mass, conditioned raw-`H` moment failure for every fixed `C`, and the `Y`-to-`2Y` odd-subset mechanism agree.
- notes (47.16) ↔ `antichain-wall`: deletion direction, unchanged union/void, `Q_S`, `w_B`, every shared prime-power factor in `Gamma_S`, compatible-set quantifiers, even `m in [D Lambda,D Lambda+2]`, and `C Lambda` right side agree; it is retained historically and immediately refuted by the §49 grid.
- notes Theorem 49.1, (49.1)–(49.5) ↔ `implication-criterion` and `antichain-void`: distinct retained-atom scope, both implication equivalences, `M=tm` unpacking, survival hypotheses, inclusion-largest orientation, and pointwise conditioned void identity agree.
- notes Theorem 49.4, (49.8)–(49.11) ↔ `antichain-profile`: reduced-class scope, uniform-`C` negation, `g asymp X` strength, exact semiprime intervals and `D=2` retention, and `g^(1-o(1))` ratio agree.
- notes Theorem 49.5, (49.12)–(49.21) ↔ `grid-obstruction`: every fixed `C,D`, every sufficiently large `X`, every admissible even `m`, compatible pairwise-coprime squarefree `S`, exact extension ratio one, prime-supply ranges, `(2z)^(-2t)` CRT cost, and direct reduced factorial-moment failure agree.
- notes Computational 49.7 and Assessment 49.8 ↔ the distinct paper registers: finite fractions remain diagnostics, the two formulations alone are refuted, narrower open routes survive, and the complete-system moment axis alone is dormant.
- notes Theorems 50.1–50.2, (50.1)–(50.8) ↔ `one-prime-slice`, `SPF`, and `hyp:SPF`: exact good class, raw/nonprimitive boundary, explicit `e,a,b`, Type-I identity, fixed-`A` hypothesis quantifier, no bound on `q`, and all-large-hard-prime conclusion agree.
- notes Lemma 50.3 and Theorems 50.5–50.6, (50.9) ↔ `prime-norm`, `bounded-core`, and `GRH-active`: wrong-grade prime norm, every-fixed-`B` genus escape for all `k`, and GRH's unforced-slice-only conclusion agree.
- notes (50.10)–(50.17) ↔ the Chebotarev and genus-pairing audits: principal-ideal divisor condition, prime-qualified `1/8` mass envelope, heuristic-only (50.13), exact pairing, residual projector, and assessment—not independence-theorem—register agree.
- notes Computational 50.9, (50.18)–(50.20) ↔ the census: all 385 counts, eight records, `311/74` split, gap 55 witness, and informational-only optional maximum agree.
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

The v5 build completes with zero TeX errors and no undefined references or citations. The PDF is generated locally, not tracked; `espaper.toc` is tracked and updated. Manual source-style equation tags retain the pre-existing duplicate-destination `hyperref` warnings, which are not unresolved references. The control-byte scan of `espaper.tex` is zero.

## Submission TODO

- Obtain external expert review of Theorem 34.8, the §39 chain, and the full thinned-window §43 transfer.
- Obtain/read Vaughan 1970 and complete the priority search.
- Prove or disprove endpoint remainder (46.13); any revival of the dormant complete-system moment axis needs a genuinely new pointwise formulation.
- Obtain external expert review of the proved §49 and §50 theorem transcriptions and the §50 standard-hypothesis assessments.
- Settle author metadata and perform a final line-by-line referee audit.

## v6 queue

- Absorb notes §51, “The witness-modulus tail: truncated windows, the polylog corollary, and the effectivity audit.”
- Absorb notes §52, “Per-slice vanishing frequency: the sieve upper bound and the empty third layer.”
- Both sections postdate the v5 snapshot and are intentionally absent from `espaper.tex`.
