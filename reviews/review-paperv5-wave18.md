# Paper v5 wave-18 fidelity review

**Overall verdict: FAITHFUL-AFTER-REPAIRS.**  The v5 paper faithfully carries source §§49–50 after four narrow repairs: three §50 label/caveat restorations in the TeX and correction of the stale README v6 queue.  No §51/§52 content has entered the paper.  The provisional record register remains intact.

## Defects and repairs

| ID | Severity | Finding | Source match | Disposition |
|---|---|---|---|---|
| D1 | **Moderate** | The original paper (50.17) silently shortened Bateman–Horn's output from “on average” to an unqualified output, omitted that the desired value is composite, and omitted that Linnik supplies a **prime**. These are load-bearing standard-hypothesis caveats. | `paper/espaper.tex:2967-2970`; `notes.md:18326-18328` | **REPAIRED**, with a `% wave-18 fidelity repair` marker. |
| D2 | **Moderate (scope metadata)** | README falsely said no post-§50 source existed, although merged notes now contain §§51–52. That could silently drop both from the next-paper queue. | `paper/README.md:96-100`; headings at `notes.md:18403`, `notes.md:18868` | **REPAIRED**: both are explicitly queued for v6 and declared out of v5 scope. |
| D3 | **Low** | Theorem 50.2's visible heading said only “conditional pointwise consequence”; it omitted the source heading's explicit “conditional on `H_SPF(A)`; `H_SPF(A)` unproved” label. The surrounding text was already honest. | `paper/espaper.tex:2760-2763`; `notes.md:18070-18072` | **REPAIRED**, with a `% wave-18 fidelity repair` marker. |
| D4 | **Low** | The `H_SPF(A)` commentary said no extra genus condition was needed but dropped the source's reason that genus compatibility is automatic from (50.3). | `paper/espaper.tex:2752-2758`; `notes.md:18060-18065` | **REPAIRED**, with a `% wave-18 fidelity repair` marker. |

No unrepaired fidelity defect remains.

## 1. Source §49 absorption — PASS

- The chronology is exact: the §47 divisor cube refutes literal (40.28) and raw (37.19); the implication antichain is presented only as the historical proposed repair; the §49 complete-bipartite grid then refutes (47.16) and the ordinary reduced-count factorial moment. See `paper/espaper.tex:934-1005`, `:1007-1228`, and `:3298-3315`.
- Every grep hit for “antichain” or (47.16) was inspected. None calls the repaired hierarchy live or open. The proposal is in past tense at `:982-1005`, and the later status is **REFUTED/DORMANT** at `:1222-1228` and `:3298-3315`.
- Theorem 49.1 retains distinct retained atoms, both implication equivalences, the `M=tm` unpacking, divisor labels, survival of both classes, odd-modulus/no-extra-division condition, and inclusion-largest orientation (`:1010-1068`; source `notes.md:17556-17627`).
- Theorem 49.4 retains reduced classes, the uniform quantifiers in `X,g,a`, `g asymp X`, the exact semiprime intervals, residues `q=3 (mod 8)`, `p=5 (mod 8)`, maximal `D=2` atom `n=-8 (mod qp)`, and the `g^(1-o(1))` failure (`:1074-1116`; source `notes.md:17682-17745`). It does not overstate this as failure of every small-`g` or averaged profile.
- Theorem 49.5 preserves the order “for every fixed `C,D`; every sufficiently large `X`; every admissible even `m`; there exists `S`”, with compatible pairwise-coprime squarefree selected moduli and `|S|<m` (`:1133-1146`; source `notes.md:17766-17784`). The atoms are exactly `A_ij: n=-8 (mod q_i p_j)`. The diagonal intersection forces every off-diagonal edge with extension ratio exactly one; `L^dagger(S) >= t(t-1)`, and `t=m-1` makes this exceed `C Lambda` (`:1148-1169`).
- The moment construction retains the separate `t=floor(m/(2 log(2z)))`, primes in `(z,2z)`, one CRT class `C_R`, conditional probability at least `1/R`, `R <= (2z)^(2t)`, all `t^2` atoms firing, and the direct factorial-moment lower bound (`:1171-1196`). This is a failure at every relevant `m asymp Lambda`, not merely failure of one induction.
- Proposition 47.3's prime-only rung survives (`:1198-1200`). `(40.19)`, `(37.27)`, the existence of another minorant for `(33.16)`, `(33.16)` itself, and `H_PF'` remain explicitly **OPEN** (`:1201-1211`). Only the complete-system hierarchy/moment formulation is **DORMANT**, with the collapse in stakes tied to the §39 provisional record (`:1222-1228`).

## 2. Source §50 absorption — PASS AFTER REPAIRS

- The scope sentence is present verbatim in substance: this is “a rigorous conditional reduction and a map of its missing input, not an unconditional theorem” (`paper/espaper.tex:2664-2680`; source `notes.md:17947-17961`).
- Theorem 50.1 retains the exact good prime-factor class, admissible-slice hypothesis, prime divisor conditions, explicit reconstruction, positivity, Type-I identity, and raw/nonprimitive boundary (`:2681-2740`).
- `H_SPF(A)` is visibly boxed, bespoke, unproved, quantitative, and falsifiable (`:2742-2751`). Its quantifiers are fixed `A`, then a threshold, then every hard prime, then existence of positive `c,k` and prime `q`; it puts no bound on `q`, requires no primitivity, and now explicitly records genus automaticity (`:2752-2758`).
- Theorem 50.2 now visibly preserves both conditionality and the fact that `H_SPF(A)` is unproved (`:2760-2771`).
- Lemma 50.3 remains “prime norms are wrong-grade” (`:2784-2796`). Assessment 50.4 remains an assessment of standard Bateman–Horn/Hardy–Littlewood outputs and their quantifier failure, not an independence theorem (`:2798-2811`).
- Theorem 50.5 retains every fixed `B`, infinitely many hard primes, every squarefree `s <= B`, all `k`, and the exact `R_B=24 product_{ell<=B} ell` construction (`:2812-2831`). Theorem 50.6 is explicitly GRH-conditional and yields only an admissible unforced slice with `s << (log p)^2`; it explicitly does **not** assert positivity (`:2833-2853`).
- The §50.3 principal-ideal/Chebotarev wall is intact (`:2855-2878`). Formula (50.12) remains a prime-qualified class-mass envelope, not coverage (`:2879-2892`), while (50.13) is explicitly an independent-events **model** and “audit ceiling, not a conditional exceptional-set theorem” (`:2893-2914`).
- Formula (50.15) retains the exact genus pairing. Assessment 50.8 preserves the moving-family/Duke limitation as an assessment requiring a genuinely new uniform input, not a GRH consequence (`:2915-2959`).
- The repaired (50.17) table now matches every standard-output and missing-input qualifier (`:2961-2986`). Computational 50.9 retains all 385 observations, the exact distribution and eight records, the `311/74` comparison, gap 55 at `p=23689` with witness `(33,2,77951)`, and the streamed `ES_FULL_SCAN` maximum 282 at `p=83689` (`:2988-3025`). All are informational only and explicitly not evidence for `H_SPF`.

## 3. No contamination — PASS

- `espaper.tex` has no `H_MOD`, witness-modulus-tail phrase, §52 heading/content, truncated-window/polylog-corollary language, per-slice-frequency theorem, or empty-third-layer language.
- The requested `effectiv` grep has only the legitimate §50 Chebotarev discussion at `paper/espaper.tex:2876,2898`. The `52.` grep's other hit is the pre-existing bibliography identifier `arXiv:math/0309352` at `:3371`, not source §52.
- Source §§51–52 appear only in the repaired README v6 queue (`paper/README.md:96-100`).

## 4. Provisional records — PASS

- Source Theorem 39.7 is present with the same all-denominator and prime statement and a visible **CLAIMED/PROVISIONAL** heading (`paper/espaper.tex:1847-1855`; source `notes.md:13397-13408`).
- Source Theorem 43.12 retains `<<_epsilon`, `c_epsilon`, the fourth root of `eta_2(m)L^3/phi(m)`, exact range `3 <= m <= L^(3-epsilon)`, and both denominator scopes (`paper/espaper.tex:2387-2402`; source `notes.md:15292-15308`). Its inheritance of provisional Theorem 34.8/paper `thm:pruned`, paper `m-pruned`, and every §39.7 maximum-severity qualification is explicit.
- Theorem 34.8's paper analogue remains visibly provisional (`:1341-1367`) and is used with that status (`:1739`, `:1905-1908`, `:2396-2401`).
- The three §39.7 weakest-step qualifications remain at `:1912-1934`; the “do not cite as established” warning remains at `:1937-1947`.
- Vaughan's primary paper remains declared access-blocked; the DOI-only check and “search result, not literature guarantee” caveat survive (`:1948-1958`). The Pomerance–Weingartner comparison keeps published versus provisional status, common domain, fixed-`m`/range caveats, and unknown-constant limitation (`:2350-2380`).
- The pedigree is explicitly internal and not external validation (`:1960-2027`). The abstract and introduction likewise prohibit citation as established (`:36-65`, `:108-166`). No text says either record is externally reviewed or settled.

## 5. Compile and hygiene — PASS

- Ran `pdflatex -interaction=nonstopmode espaper.tex` twice after the final TeX repairs. Both exited zero; the final log has zero lines beginning `! ` and no `undefined` reference/citation diagnostics.
- Output is **54 pages**, within the expected 50–56 range.
- Forbidden control bytes (`<32`, excluding tab/LF/CR): **0**. Carriage returns: **0**.
- Eaten-backslash scans found no line beginning `mid `, `eq `, or `egthickspace`, and no bare unescaped `nmid` or `varphi`.
- `git diff --check` is clean. The known duplicate manual-equation-destination warnings are nonfatal and do not represent unresolved references.

## 6. README and unit report — PASS AFTER REPAIR

- The v5 entry has the correct date, 54-page count, both absorptions, exact dormant/open boundary, record caveats, and cleared §49 queue item (`paper/README.md:1-94`).
- The v6 queue now correctly records newer source §§51–52 and their intentional absence from v5 (`:96-100`).
- `UNIT_REPORT_P18.md` accurately describes the principal §49/§50 absorption, formula ranges, record preservation, and build. Its “no post-§50 queue” claim was stale after the later merge of §§51–52. Its claim that all §50 frontier-table/label caveats agreed was too strong before D1/D3/D4; the repaired TeX now makes that claim substantively true.

## 7. Formula-level transcription audit — PASS

The following were checked character/entry by character, allowing only TeX-equivalent spelling such as `\frac{a}{b}` versus `{a\over b}` and harmless line breaks:

| Formula | Paper | Notes | Result |
|---|---:|---:|---|
| one-prime reconstruction (50.5) | `2715-2718` | `18011-18015` | exact `e,a,b` numerators and denominators |
| Type-I identities (50.6) | `2720-2723` | `18018-18021` | exact two identities and three unit fractions |
| boxed `H_SPF(A)` (50.7) | `2747-2751` | `18056-18059` | exact log box, divisibility, and ray congruence |
| grid primes/atoms (49.12)–(49.13) | `1121-1129` | `17754-17761` | exact mod-8 classes and `n=-8 mod q_i p_j` |
| matching modulus/ratio (49.16)–(49.17) | `1151-1161` | `17790-17804` | exact product and extension ratio `1` |
| moment scale/cost (49.18)–(49.21) | `1172-1194` | `17820-17856` | exact floor, CRT probability, `(2z)^(-2t)`, and log lower bound |
| mass envelope (50.12) | `2883-2891` | `18218-18224` | exact `1/2`, prime `q=3 mod 4` sum, and `1/8` main scale |
| model ceiling (50.13) | `2902-2905` | `18239-18242` | exact iterated-log exponent; audit label retained |
| genus pairing (50.15) | `2929-2932` | `18280-18283` | exact `chi`/`chi chi_s` equality |
| frontier table (50.17) | `2964-2980` | `18319-18337` | exact after D1 repair |
| census distribution (50.19) | `3001-3010` | `18362-18372` | all 32 bins/counts exact; counts sum to 385 |
| strict records (50.20) | `3012-3017` | `18374-18382` | all eight `(p,ck_pr)` pairs exact |

No sign, exponent, denominator, range, local condition, or census-entry discrepancy remains.
