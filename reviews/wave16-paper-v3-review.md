# Wave-16 hostile fidelity review: `paper/espaper.tex` v3

## Verdict

**FAITHFUL-AFTER-REPAIRS.** Two theorem statements had dropped source hypotheses and thereby read more broadly than `notes.md`; both are fixed. Two smaller fidelity/provenance defects are also fixed. No unadjudicated general-$m$ strengthening appears, and no headline is promoted beyond **CLAIMED/PROVISIONAL**.

## Defects

1. **OVERCLAIM — fixed in place.** Lemma `m-identity` omitted `k,ell >= 1` and that `A=uvw` is a factorization into positive integers. Without those hypotheses the positivity conclusion was not the source Lemma 43.1. They are restored at `paper/espaper.tex:1691`, with a fidelity-repair comment.
2. **OVERCLAIM — fixed in place.** Lemma `m-class-mass` omitted that `ell` ranges over primes `X^(1/2) < ell <= X`; its displayed reciprocal sum therefore read as if composite `ell` were included. The exact prime domain from notes Lemma 43.3 is restored at `paper/espaper.tex:1773`.
3. **TRANSCRIPTION — fixed in place.** The compressed §44 census retained `15/385` and 111 slices but omitted the specifically tracked conspiracy prime 2521. The paper now states that 2521 is among the 15 and that its twelve ordered Type-I rows lie outside `ck <= 30` (`paper/espaper.tex:2129`).
4. **TRANSCRIPTION — fixed in place.** The Bettin--Chandee entry asserted publication metadata not recorded by the archived-source ledger. It now cites exactly the archived `arXiv:1502.00769v1` source (`paper/espaper.tex:2387`). DFI remains `Invent. Math. 128 (1997), 23--43`.
5. **STRUCTURAL — README erratum only.** Post-v3 notes §47 refutes the literal codegree target (40.28) and the raw-`H` factorial-moment target (37.19). V3 still calls those raw targets/hierarchies open at lines 901, 2369, and 2382. Per the brief, the frontier was not rewritten; `paper/README.md` records the pending-v4 correction and the still-open implication-antichain replacement (47.16). Target (40.19) remains open.

No unresolved **OVERCLAIM** remains after these repairs.

## Fidelity findings

- **General `m`.** The two layers, `eta_1`, `eta_2`, `C_2`, aggregate `(k,m)=1` family, product modulus `muv`, absence of `(uv,m)=1`, and no short-class equidistribution all match §43. Prime/all-denominator Layer-1 ranges are respectively `(log N)^(2-eps)` and `(log N)^(1-eps)`; Layer 2 stops at `(log N)^(3/4-eps)`. The semigroup cutoff has the repaired `eps/4` denominator. The PW crossover is the two-regime `phi(m) \lesssim eta_1(m)^(3/2)(log N)^(1/8)` comparison, with PW better after crossover and no uniform-beating claim.
- **No premature strengthening.** The paper contains no `[eta_2(m)/phi(m)]^(1/4)` headline or thinned-degree theorem. Notes §43.11 and §§46--48 postdate v3 and are not imported.
- **Pedigree.** The three internal Theorem 34.8 checks, third re-derivation scope, Shiu parameters, blind S1--S7 freeze/attestation limitations, order-six stress, 14,210 atoms, 1,128,378 compatible pairs, and three wave-15 hostile reviews match §§34.5 and 41. Every such pass is called internal; none is presented as external validation or priority certification.
- **Slices.** The raw character/exponent-box vanishing law, primitive counterexample `(241,7,3)`, four `c`-cores, `80/111`, seven-column census, `15/385`, and open all-prime positivity target match §44. The text does not turn finite vanishing into a no-representation claim.
- **Endpoint.** The unique-cofactor and complement-divisor forms, fixed-`s` and fixed-polylog-prime closures, exact Kloosterman matrix, both reciprocity orientations, and DFI/BC coefficient-quantifier obstruction match §§42 and 45. Theorem `small-fibre` has `4 <= W_0 <= z/2`, `W_0=floor(L^3/(log L)^2)`, cell injectivity, full endpoint-prime range, “widest proved subfamily” scope, and leaves (40.19) open on `4c^2s>W_0`.
- **Global register.** Abstract, introduction, status box, and acknowledgment consistently label both `3/4` headlines and Theorem `pruned` **CLAIMED/PROVISIONAL**. “Unconditional” is explicitly limited to “no unproved hypothesis”; the first-since-1970 language is conditional on external review and search-limited. Vaughan remains accessed only through PW plus metadata.

## README spot checks

Checked six claimed correspondences: (43.2)--(43.3), (43.4)/(43.6)--(43.9), (43.10)--(43.15), (43.28)--(43.31), (44.3)--(44.16), and Theorem 45.9/(45.26). The first and third exposed the two repaired domain omissions; all six now agree with `notes.md` in hypotheses, constants, ranges, and status.

## Build and hygiene

Two `pdflatex -interaction=nonstopmode espaper.tex` passes exit 0 and produce a 41-page PDF. `espaper.log` contains no `undefined` or `multiply defined` references/citations. Every `\cite` key has a bibliography item. The control-byte scan of `paper/espaper.tex` reports zero bytes in `00--08`, `0B--0C`, `0E--1F`, or `7F`.
