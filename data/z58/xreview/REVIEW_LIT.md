# z58 cross-model hostile review — LIT

**Verdict: ACCEPT-WITH-FIXES.** ES remains OPEN. The decisive citations and Prop I survive; the final screening inference still overclaims what finite counterexamples exclude.
Reviewed `side-agent/z58-lit` at `8964047675b928b059fd224ce82a96b66168ef5c`, principally `Z58_LIT.md`; sources independently fetched 2026-11-05.
All executed commands used `ulimit -v 4000000` and timeouts ≤1800 seconds. No external Lean build was attempted; CI evidence is explicitly not a local kernel replay.

## Per-claim audit

| Claim | Classification | Independent result / qualification |
|---|---|---|
| Kandukoori–Ramesh–Kumar (K-R-K), Thms 1–2 and prime normalization | CORRECT as cited theorem | Live PDF agrees byte-for-byte with archived PDF. Thm 1 is `E(N) ≪ N exp(−c(log N)^{3/4})`, N≥3; prime count is bounded by π(N) times the same saving after changing c; Thm 2 fixes m≥4 with m-dependent constants. This is not a fresh audit of the entire analytic proof. |
| K-R-K current formal statement / CI | CORRECT as repository fact | Read `Paper.lean`, `Basic.lean`, `Congruences/Certificates.lean`, and workflow at full SHA `f6c99eaaca6ec7a7226a7a16bef1cd2b09e36660`; endpoint really counts nonrepresentable positive-integer denominators, with rational division and real exponent 3/4. Run 41075205124 has successful Build and Check axioms steps; workflow requires five exact standard-axiom reports. |
| July claim precedes September internal note | CORRECT-WITH-FIX | Verified commit chronology, not public-priority chronology. July version has nine additional analytic axioms; do not backdate the October standard-axiom closure. Remove “First public commit” from archived-source README. |
| K-R-K supersedes count-paper results | NOT ESTABLISHED / not claimed in memo | Exceptional-set counting does not imply a lower bound for the line R, a sub-cube pointwise upper bound, or a genus-layer estimate. Add the explicit count-paper impact assessment below. |
| Akaka v0.8 | CORRECT as author claim | Zenodo metadata and actual PDF agree: Thm 2 has absolute c,C,X₀, each fixed block numerator 4≤m≤(log X)³, ≤CmX/(log X)⁴ bad primes, threshold c(log X)³/m. No simultaneous common good-prime set or explicit onset. Thm 1 retains v0.7. Lean certificate remains an author claim in this review. |
| Ventas 2610.41027v1 | CORRECT, prime-input qualification | API confirms 2026-10-29T22:13:30Z, 8 pp.; live PDF matches archive. Re-derived Thm 3.1, Prop 4.1, and Thm 6.1 below. Call its certificates Type I **for prime inputs**; composite inputs need not have the required coprimality. |
| Prop I and fixed-D corollaries (PROVED locally) | CORRECT | Complementary divisors give the involution; CRT and fixed-modulus PNT give the pattern-frequency assertion. No moving-cutoff/existence conclusion follows. |
| Pomerance–Weingartner publication and bound | CORRECT | Crossref confirms Ramanujan J. 69(2), article 31, online 2026-01-14, DOI 10.1007/s11139-025-01312-2. arXiv v2 (2026-01-15) Thm 1.3 has absolute C and range 4≤m≤(log N)² with saving exp(−C(log N)^{2/3}/φ(m)^{1/3}). |
| Negative Pell prime theorem / probe | CORRECT | Descent checked below; original probe rerun with exact agreement. The 6/26 conditional failures are not evidence for absence of a residual association. |
| Rickards–Stange Thm 2.8 (cited PROVED) | CORRECT as citation | Opened 2401.01860v3: missing numerators of Ψ(2/3) are squares plus exactly {3,6,7,10,12,15,18,19,27,31,34,55,63,99,115}. No ES transfer is supplied. |
| §3 “unless the exceptional set is unbounded or … restricted to primes” | WRONG inference | A finite sporadic set containing all 285 observed composite zeros is not excluded. This contradicts the memo’s own corrected §0 discussion. |
| “narrowed — no HOT LEAD” | CORRECT-WITH-FIX (Assessment) | Supported as “no direct transfer found in this search,” not an exclusion of all sufficiently-large-n non-square theorems or entire proof technologies. |

## Source and chronology checks

- K-R-K live manuscript: https://sushaan-k.github.io/erdos-straus/paper.pdf ; SHA-256 `20a3290be4c1ea58ea39378cafe9287f7a338703d19512474a346bb468702acb`; printed date July 29, 2026 is not a timestamped public release.
- Root commit: https://api.github.com/repos/sushaan-k/erdos-straus-lean/commits/268ebdbfe19f52fd70ae4d7172fda7d492eb5b79 . Both author/committer dates are 2026-07-30T00:50:07Z; no parents. `EscAnalytic/Counting.lean` defines the 3/4 saving and actual exceptional count; `EscAnalytic/Paper.lean` exports `IsMainBound exceptionalCount`; `TrustBoundary.lean` explicitly lists three standard plus nine analytic axioms.
- Current proof and CI: https://github.com/sushaan-k/erdos-straus-lean/tree/f6c99eaaca6ec7a7226a7a16bef1cd2b09e36660 ; https://api.github.com/repos/sushaan-k/erdos-straus-lean/actions/runs/41075205124/jobs . The main-branch API returns f6c99eaa. A separate later workflow SHA also appears in the run list; it is not needed for this verification.
- GitHub repository creation is 2026-07-12T02:32:26Z. A server-dated root-commit CI run exists at 2026-07-30T00:50:47Z (30503910193), strengthening evidence of the commit’s existence then, **not** proving the repository was publicly readable then.
- Local `git log --follow -- paper/es-threequarter-note.tex` identifies first addition `4ecb5cb1dbd6b30a562d563f39bd40f08a59f14e`, 2026-09-06T03:14:25+02:00. This dates that file, not necessarily the campaign’s first discovery. No public-release priority or independent-development finding follows.
- Akaka primary record/PDF: https://zenodo.org/api/records/22905042 and its `prime-abundance-preprint-v0.8.pdf` attachment (22 September 2026).
- Ventas: https://arxiv.org/pdf/2610.41027v1 ; SHA-256 `140b8a75a92cf0304993282119765c6dc2bf520146fa5e562061e88c301d12e3`. API independently confirms title, author and v1 date.
- P-W: https://api.crossref.org/works/10.1007/s11139-025-01312-2 ; https://arxiv.org/pdf/2511.16817v2 . Crossref supplies publication status, not merely an inferred journal citation.
- Other historical survey entries are not blanket re-certified by this review. Negative search results remain bounded searches, not completeness or originality certificates.

## Proof re-derivations

1. **Prop I.** Write q=(d+1)/4, d≥3, d≡3 (4). For r|q, both r and C=q/r are units modulo d and lie in [1,q]⊂[1,d). Since 4rC=d+1, x=−r gives `(4x)⁻¹=−C (mod d)`. Also T(T(x))=x, proving both directions and the exact (u,C) swap. The original all-d≤20000 script returns zero violations and the stated three Mordell pairs.
2. **CRT / frequencies.** For every relevant d≤D, d divides L_D, so the same unit n* realizes T(n) at all levels. On Mordell classes use the odd modulus lcm(105,L_D) and residue 1 modulo 8. The map bijects reduced classes with each fixed hit pattern. PNT in APs gives equal limiting *conditional* prime frequencies. This is fixed D only. Indeed the stated L_D already contains p when D≥p, so this corollary cannot even be applied at the full prime cutoff D=⌊(4p+1)/3⌋ without changing its domain/modulus.
3. **Square/parity qualifications.** T(m²)=((2m)⁻¹)² is a square **residue**, not necessarily an integer square representative. Divisor complementation sends “C even” to “u even”; it does not preserve R₈. Neither statement uses primality.
4. **Ventas.** At a Grid hit, r|(4t+1), r≡3 (4), 1<r<4t. Its complementary divisor s=(4t+1)/r also lies strictly between 1 and 4t and is 3 modulo 4; inversion sends −r to −s. For Prop 4.1, a nonresidue modulo p≡1 (8) has a representative ≤(p−1)/2; one odd prime factor ℓ is a nonresidue, and reciprocity forces `(b/ℓ)=−1` from pb≡1 (mod ℓ). Hence b is not an integer square. Fixed-cutoff PNT proves Thm 6.1, not uniformity in T. For composite n, “Type I” needs care: n=21,t=2 yields denominators (6,48,336), whose first two are not coprime to n.
5. **Legendre descent.** Take the least positive Pell solution x>1 to x²−py²=1. Modulo 4 gives x odd,y even. The coprime integers (x−1)/2,(x+1)/2 multiply to p(y/2)², hence are a²,pb² in some order. If x+1=2a², then a²−pb²=1 with 1<a<x, contradicting minimality. Thus x−1=2a² and a²−pb²=−1. A square n>1 cannot satisfy x²−ny²=−1 by factorization; a prime divisor 3 modulo 4 prevents it locally. The claim is not a statement about R.

## Falsifier and numerical audit

| Screen | Recheck | Correct implication for this lane |
|---|---|---|
| F1 odd squares | Prop I residue identity and negative-Pell obstruction re-derived; complete R replay through 9·10⁶ consistent | No existence from symmetry; density theorems can ignore squares. |
| F2 12 R₈-zero primes | Recompiled `z57_synth_dec8.c`; ran each listed prime as singleton interval, one OpenMP thread: all R and R₈ columns agree, including minimum R=12; four are in 𝔐 | Akaka counts the full strict family, not this line. Prop I swaps parity sub-lines. These are not counterexamples to either source. |
| F3 285 composite zeros | Recompiled `z58_screens_rstar.c`, exhaustive R replay to 9·10⁶; exact list agreement through 7,999,801. Min/max 57/7,753,881; 71≡1 (24); 15 in 𝔐, max 3,210,601 | Refutes exception-free non-square positivity, **not** positivity outside a finite sporadic set or above a sufficiently large threshold. |
| F4 14 star / 38 genus-window zeros | All 14 star zeros independently recovered through 9·10⁶. Rechecked all 38 listed 𝔊*-zeros with `z56_famdesign_decide.c` (small p<1000 by direct enumeration). Counts in 𝔐 and paired classes agree | Refutes threshold-free prime positivity; finite-cutoff symmetry and density theorems remain compatible. Completeness to 10¹⁰ was not rerun. |

F3 half-decade counts independently recalculated: `1,3,5,12,12,25,35,45,50,62,35`, agreeing exactly; rising absolute counts do not establish a positive density.
Negative-Pell script replay: 259/285 have a prime factor 3 (4); the other 26 have 20 solvable, 6 insoluble. Thus total failures 265/285. Controls: 15,459/20,000 locally obstructed; 3,039/4,541 remaining solvable, hence total failure 84.805%, conditional failure 33.08%. All p≡1 (4) below 200,000 pass. These are descriptive, non-size-matched data, not a causal or independence test.
K-R-K Example 1.1 independently checked using exact rational arithmetic: `4/2521=1/644+1/30252+1/1217643`.

## Required fixes, in priority order

1. **MAJOR — repair the surviving finite-exception inference.** Replace §3’s “unless the exceptional set is unbounded or … restricted to primes” by “unless an exceptional set or threshold includes every observed zero.” Likewise §0’s “would need … restricted to primes” is not necessary: an eventual all-non-square theorem could imply (MS). The thin-orbit table’s “i.e.” must not exclude a sufficiently large finite sporadic set. No infinitude of composite zeros was proved.
2. **MAJOR — keep priority and proof dates separate throughout.** The required citation update is justified, but the sources README’s “First public commit” is stronger than the evidence. Use “root commit dated July 30; public accessibility on that date unverified.” State that the July formalization was conditional on nine analytic axioms; only the October checked version has the standard-only closure. “Separate proof” does not certify independent development.
3. **ADD explicit `paper/es-count-note.tex` consequences.** Its Theorems A–D are not superseded by the cited exceptional-set result; K-R-K’s h|a² family is broader than c=1, and positivity/counting in it does not force an R hit. Update the introductory exceptional-set literature around line 96 with a qualified K-R-K citation, not a claim that the count-paper results have lost priority. This review does not certify those proofs or establish their originality.
4. **Update Akaka references without breaking the comparison.** The count note currently cites v0.7 (bibliography line 1928). v0.8 retains that theorem and the same m=4 auxiliary family. Its §2, (5)–(7), Lemma 3 decoder has s/M=a/b∈(0,1), while an R solution has s/M=B or u, a positive integer. Thus the disjoint-*auxiliary*-family argument remains correct. Keep the v0.7 pinpoint or update all pinpoints when citing v0.8; do not call the full Type II families disjoint.
5. **MINOR — sharpen domains/status.** Say Ventas’s certificates are Type I at prime inputs; square preservation is modular; external analytic proofs are cited rather than newly proved here. Preserve “CI verified, not locally rebuilt” and “author claim” for Akaka. The proposed 3/4-note, FRONTIER and literature corrections are appropriate subject to these qualifications.

**Final assessment:** retain the new citations, Prop I, and the modest “no direct transfer found” verdict. Do not retain the stronger elimination of finite-sporadic/all-large-n mechanisms. No HOT LEAD or resolution of ES is supported.
