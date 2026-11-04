# K4LIT cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES.** The formal new lemmas pass; the literature supports a bounded-search **narrowed** assessment, not a necessity/impossibility theorem. ES remains OPEN.
Reviewed `side-agent/z56-k4lit` at `09da8f3e5be5d71a9d3c0d5faf87da67fb3032db`, including §9's overrides of the reports.
Independent review: downloaded primary sources anew; read theorem text/page images rather than accepting the internal review. Source proofs are not themselves independently certified here.

## Per-claim findings

| Claim | Classification | Independent check |
|---|---|---|
| §3 Lemma P(a), including shifted-prime density | CORRECT | All eight proof steps checked; Euler product and summed truncation error give the claimed power saving. |
| §3 Lemma P(b) | CORRECT | Hidden primes exceed every sieving prime; `Dz ≤ x^(1−ε)` controls counting errors, including `D=1`. |
| §3 Prop P′ | CORRECT relative to Iwaniec Thm 1 | Nonnegative weights are legitimate; parity and support `n<x` turn √x-sifting into S-membership; remainder is negligible. |
| H2/§7 density shorthand and threshold | CORRECT-WITH-FIX | Restore the admissible-density restriction. The unrestricted shorthand admits `g(3)=1`, for which the above-half guarantee is false; see F1. |
| §4.2 primitive representation identity | CORRECT | For odd prime powers, `r*/4` has local factors 2 at split primes and 0 at inert primes, including repeated factors; units give 4 at 1. |
| §4.3 “0 vs 2” identity and prime-sum identity | CORRECT | Four inert prime factors would exceed N; parity excludes 1 and 3. S-members automatically survive the preliminary sieve. |
| §4.2 coprime CRT formula; conditional Cauchy–Schwarz count | CORRECT | Substitution gives `4a+1 ≡ 0 (e)`; `(x/log^(3/2)x)^2/(x log^3x)=x/log^6x`. |
| §4.2 (★K)+(★K′) route | GAP, honestly labelled Assessment | Main mass, local factors, switched constants and complementary-divisor analysis remain missing. The later asserted square-root truncation is not established; F2. |
| Iwaniec 1972 Thm 1, A=−4 | CORRECT relative to source | pp. 203–205: S₁ counts primes with a proper representation; take B=1, form `u²+v²`. Odd primitive norms are precisely S. No extra `p≡1 (8)` conclusion is inferred here. |
| Iwaniec 1976 Thms 1–2 and Cor. 2 | CORRECT relative to source | pp. 71–73 give β=1, the stated asymptotic error/level, and the `E(N,N^(1−ε))` conditional formula. No necessity result. |
| FI 2009 Thms 2–4; det-1 comparison | CORRECT relative to source | pp. 3–5: lower bound conditional on one fixed θ<1 sufficiently close to 1; upper bound unconditional. SOTS is not primitive S. |
| Nath–Xie v3 Thm 1.1 / Remark 1.1 | CORRECT relative to source | p. 3 explicitly has Ω≤9 and the proposed EH-variant Ω≤3. The latter is a remark, not an unconditional theorem. |
| Sedunova Thms 2–3 | CORRECT as reported source statements | pp. 3–4 define a quadruple/representation-weighted count, state 7 and floor(2/θ), and identify the det-1 level 1/6. Distinct-count order is not inferred. |
| Beyond-half level ledger | CORRECT for checked statements | Maynard II 3/5 needs triply well-factorable weights; 7/12 uses special linear upper weights. Lichtman 66/107 and Pascadi 5/8 likewise need triple factorability and one fixed integer residue. |
| Smooth-modulus / semilinear qualifications | CORRECT | Polymath8a Thm 1.1 allows prescribed residues per prime but smooth squarefree moduli; Stadlmann Cor. 2 gives the improved MPZ range. Teräväinen Lemma 9.2/Remarks 9.3–9.4 give 3/7 and 2/5 only for the stated factorization assertions. |
| Siegel-zero numerical inputs | CORRECT as qualified source statements | Wright Thms 3.1–3.2: 30/59 and 16/31 with exceptional-zero quality/conductor restrictions; fixed-residue 2/3 separately recalled. Merikoski Thm 15: threshold 0.61634 plus its other hypotheses. Tao–Teräväinen Thm 1.6: at most two Λ-factors. |
| GMPP, Lü–Wang–Wu, Banks abstracts | CORRECT as reports of claims | Retrieved abstracts confirm almost-all shifts, signed Möbius cancellation, and the claimed explicit zero-free constant respectively. This review does not validate the latter two breakthroughs. |
| Dimitrov erratum | CORRECT | Printed Thm 1 has the global `1/φ(q)` main term and only `(a,q)=1`; at q=8,a=7 every `r(p−1)` vanishes. This objection does not depend on proving a new distribution theorem. |
| Literature nonexistence / “EH-hard” / rankings | Assessment only | The bounded-search wording is appropriate; “probability 0, unconditionally” and the unported shell-level assertion need softening (F3). No general no-go result follows. |
| Inherited HCKILL/P415 results and K4CHEN recommendation | Not recertified here | Those are dependencies from other lanes, not new K4LIT proofs. This review does not certify their constants or license banking an unaudited explicit K. |

## Proof audit details

1. Lemma P support: `n=qm`, with q,m≡3 (4), is parity-forced and never in S. The hidden prime is coprime to each data modulus; `E<H` holds in both cases.
2. CRT counts one class modulo `4[d,e]`, with error O(1). Summing its nonnegative coefficients costs at most `O_C(log^C x)` per hidden prime.
3. Completing the e-sum gives `d^(−1)∏_(q∤d)(1+c_q/q)∏_(q|d)(1+c_q)=Gg(d)`, exactly the asserted density, not merely an approximation.
4. Set `f=(d,e)`. The discarded tail is bounded by `d^(−1)E^(−1/2)∏_(q|d)(1+C/√q)`; the estimate also holds when `E/f<1`.
5. The d-sum of this bound is `O_C(X x^(−ε/4)log x)`. Counting errors are `O_C(DH log^C x)`; the two DH restrictions and `X≍x/log x` give `O_(ε,C)(Xx^(−ε/5))` for sufficiently large x.
6. PNT in the fixed progression gives `Σ_(H<q≤2H,q≡3(4))1/q ~ log 2/(2 log H)`. Thus the claimed X-size and all dependencies are valid.
7. For Prop P′, an inert factor surviving √x-sifting would require a second one, hence n≥x. Iwaniec's lower function is positive for s=2θ>1; `X/log x=o(XW(√x))`. Multiplication of pointwise sieve inequalities by nonnegative weights is valid.
8. The below-half statement for exponents ≤1/4 follows by restricting data from any fixed admissible exponent in (1/4,1/2). No endpoint result and no joint-data obstruction follow.

## Required fixes, in priority order

**F1 — Density scope in H2, §3's reading, and proposed FRONTIER text.** State the §3 admissible family explicitly, or at least `1/q≤g(q)<1`, `g(q)=1/q+O(1/q²)`, with fixed constants. “Any density … ≥1/q” alone is not sufficient.
Counterexample to the unrestricted above-half summary: let `a_n=1[n<x, n≡9 (12)]`, `X=x/12`, `g(3)=1`, and `g(q)=1/q` for other inert primes, extended multiplicatively.
For every squarefree inert-composed d, `A_d=Xg(d)+O(1)` by CRT. At `D=x^(3/4)` the total remainder is `O(D)≪X/log x`, yet all elements contain 3 and none is in S. The displayed big-O density condition holds (constant 6 suffices).
This does **not** contradict the formal Prop P′, whose sieve hypotheses exclude g(3)=1. Restricting the summaries fixes the issue without altering either proof.

**F2 — Do not perform the unproved complementary-divisor step in prose.** §4.2 says “After switching e↔(4p+1)/e, e is ≤√x”; its own to-do list correctly says this transfer is unproved.
Already for N=25, the primitive coefficients at complementary divisors 1 and 25 are 1 and 0. A hyperbola split is possible, but it leaves coefficients depending on the complementary large divisor; it is not the asserted ordinary small-divisor prime-AP sum.
Likewise “e consists of split primes” holds on the final primitive support, not termwise when opening `Σ μ²(e)χ(e)` over all primes. Reimposing that support would assume the confinement being sought.
Keep the CRT calculation, but describe total modulus ≈x as the intended critical range of a still-missing reduction, not an established equivalence or sufficient specification.

**F3 — Keep the verdict's exclusions local to the audited implementations.** Replace §4.1's “Probability: 0, unconditionally” for algebraic families by “no applicable unconditional construction located under the audited hypotheses.” A1/A2 do not exclude all uses of prime-value technology.
H4's “only … x^(1/12) … available” for the det-15 shell is not proved by the det-1 FI citation; §4.4 itself calls the transfer an unproved plan, and Sedunova supplies det-1 1/6. Say that no adequate det-15 Type-I/Type-I-χ theorem was located, and distinguish those two analogues.
Scope “every implementation audited needs EH-strength input” to the audited exact two-component **sieve** implementations: the memo itself also lists Theorem Q's Bunyakovsky route, whose hypothesis is different and not shown to be EH-equivalent.

**F4 — Citation/status precision.** In §1 replace the blanket “each cited result is PROVED relative to its source” by “reported theorem/claim of the source; accepted as an input only where explicitly stated,” especially for abstract-only unverified 2026 breakthroughs.
In §§7–8 use FI's actual hypothesis “one fixed θ<1 sufficiently close to 1,” rather than `θ→1` or wording suggesting full EH is necessary. Keep “EH-hard for audited methods” explicitly an Assessment.

## Reproducibility

All execution had command timeouts; numerical runs additionally used `ulimit -v 6000000` and `OPENBLAS_NUM_THREADS=1`. Array sizes were inspected before execution (largest declared natural sieve: 10⁸ booleans, not a dense Cartesian product).
Re-ran `uv run --with numpy python scripts/z56_k4lit_lemmaP.py 12 0.45 8`, the `(13,0.49,7)` run, and `z56_k4lit_phiweight.py` with default `(20000000,2000)` from an archived copy in `/tmp/xrev_K4LIT`.
All three outputs agree **byte-for-byte** with `lemmaP_1e12_045.txt`, `lemmaP_1e13_049.txt`, and `phiweight.txt`.
Thus the stated sieve ratios, tested-modulus errors, crude remainder ratios 0.36/3.2, and density-adjustment ratios reproduce. These remain illustrations, not finite verification of the asymptotic remainder hypothesis.
Independently checked `cosh²(1/2)=(1+cosh 1)/2≈1.27154`; the ≈0.996 optimized ledger remains explicitly inherited model evidence, not a newly certified threshold.

## Primary-source audit trail

- [Iwaniec 1972](https://matwbn.icm.edu.pl/ksiazki/aa/aa21/aa21118.pdf), pp. 203–205; [Iwaniec 1976](https://matwbn.icm.edu.pl/ksiazki/aa/aa29/aa2914.pdf), pp. 71–73 and §4 (scans read as images).
- [FI 2009](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6709-11511_2009_Article_33.pdf), assumption A(θ), Thms 2–5, §§5–7; [Nath–Xie v3](https://arxiv.org/pdf/2501.16723v3), p. 3.
- [Sedunova](https://arxiv.org/pdf/2609.28200), Thms 2–3; [Maynard II](https://arxiv.org/pdf/2006.07088), Thms 1.1–1.2; [Lichtman](https://arxiv.org/pdf/2309.08522), Cor. 1.5; [Pascadi](https://arxiv.org/pdf/2505.00653), Thm 1.3.
- [Polymath8a](https://arxiv.org/pdf/1402.0811), Thm 1.1; [Stadlmann](https://arxiv.org/pdf/2309.00425), Thm 1/Cor. 2; [Teräväinen](https://arxiv.org/pdf/1611.08585), Lemma 9.2/Remarks 9.3–9.4.
- [Wright](https://arxiv.org/pdf/2609.35950), §3; [Merikoski](https://arxiv.org/pdf/2108.01355), Thm 15; [Tao–Teräväinen](https://arxiv.org/pdf/2109.06291), Thm 1.6; [Dimitrov](https://arxiv.org/pdf/2402.16425), Thm 1.
- Abstracts independently retrieved: [GMPP](https://arxiv.org/abs/2610.41356), [Lü–Wang–Wu](https://arxiv.org/abs/2610.20242), [Banks](https://arxiv.org/abs/2610.15483). Verification is of what they claim, not of their proofs.

**Bottom line:** retain the two formal sieve results and the “narrowed” literature assessment after F1–F4; do not promote (★K), a joint-data barrier, or an unconditional impossibility claim to PROVED.
