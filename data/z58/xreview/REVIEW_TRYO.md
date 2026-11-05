# z58 cross-model hostile review — TRYO

Reviewed `side-agent/z58-tryo` at `6a86d492ad2b0b5f4b9d88c29e13d1e9e56e9c28`, both rounds.
**Verdict: ACCEPT-WITH-FIXES.** No fatal mathematical or range-engine defect found. The almost-all result is weaker than prior project work; the pointwise attack remains inconclusive. The extended finite certification survives code audit and independent slices. ES remains OPEN.

## Per-claim findings

| Claim | Classification | Independent assessment |
|---|---|---|
| Lemma 1.1 | CORRECT | Expanding the product gives (ii); setting d=4uC−1 gives (iii); division by 4uB gives (iv). A common factor of u,B divides p; the alternative g=p forces 4uBC−u−B>p. Positivity is respected. |
| Lemma 1.2 | CORRECT | An admissible divisor uses only primes coprime to 2u. An odd character trivial on those primes excludes −1. Character separation in G/H proves (b); bounded divisor exponents invalidate the converse, exactly as n=33,u=5 demonstrates. |
| Lemma 1.3 | CORRECT | A common factor of m,d would divide u, impossible. Reciprocity gives (−u/d)=−1 while d divides m²+u gives +1. For each prime q coprime to 2u dividing m²+u, ψ_u(q)=1. |
| Lemma 1.4 | CORRECT | gcd(p+u,u)=1 for 0<u<p. Remove the power of 2; since (2/p)=1, the product of the remaining prime symbols is (u/p)=−1. Some factor has ψ_u(q)=−1. |
| Theorem 2(a–c) | CORRECT; PRIOR in substance | The sieve classes genuinely give positive integer solutions; the fixed-U Rankin argument works without growing-modulus uniformity. See derivation and prior comparison below. The C-even modification is valid. |
| Corollary 2.1 | CORRECT-WITH-FIX | The interval sieve works; cite the Dirichlet-character version of Huxley's density theorem, not just the ζ paper. State the usual 0<ε<5/12; larger ε follows separately from ordinary PNT and the exceptional-set bound. |
| Proposition 3.1 | CORRECT; PRIOR | u+B+1≤uB+2<4uB, including u=B=1. Thus p≡1 modulo the finite lcm misses every identity; Dirichlet supplies infinitely many Mordell primes. FAMTRY Prop. 2.2 already proves a broader obstruction. |
| Proposition 3.2 | CORRECT-WITH-FIX | For integer Y≥7, L=4 lcm(1,…,Y) includes 840 and log L~Y. Linnik gives log p≤(L₀+o(1))Y; p>L makes the selected primes unbounded. Hence uB>Y≥(1/L₀−o(1))log p. Correct the dissertation date to 2011. |
| §3.3 route B | CORRECT within stated scope | Independently confirmed a Mordell-zero nonresidue for each prime q=11,…,47. This kills the proposed *all-primes, no-size-condition* covering, not every least-nonresidue argument or an eventual theorem with finitely many exceptions. |
| Lemmas 8.1–8.2 | CORRECT | AB=p+s² gives discriminant −4p and the exact congruence on A. D is fundamental with two prime discriminants, hence two genera. A is odd and coprime to p: a solution has u=s²≤(p+1)/3<p. Thus χ₋₄(A)=−1 is legitimate. At C=1, q∣4p+1 splits and has nonprincipal genus iff q≡3 (4); a divisor ≡3 (4) exists iff such a prime factor exists. |
| Proposition 8.7 | CORRECT | The least NR is prime (otherwise all prime factors are smaller residues), odd, and <p. Apply Lemma 1.4. This removes ONE witness character, not all odd characters and not the bounded-exponent obstruction. Burgess/GRH bounds have the stated scope. |
| §5 numerical claims | AGREEMENT on decisive checks | The original range engine reproduces count 179468, nine HARD cases, max least-u 469 through 10⁸. Independent exhaustive point checks give min-u(53325721)=469, min-C(85664329)=41027, min-uB(3341881)=835986. The small-run histograms account for every prime, including the nine NOSOL sentinels. |
| §§8.2–8.4 numerical evidence | AGREEMENT, not a theorem | Original level and Legendre-effect runs reproduce their files byte-for-byte. Independent residue-symbol tests and all nine representations by x²+24y²,x²+48y²,x²+72y² agree. Independent §8.4 population counts agree exactly. |
| §8.6 CERTIFIED range | PASSES AUDIT + INDEPENDENT SLICES | All four logs terminate with DONE, hard=0, internally consistent histograms and valid record witnesses. No prime-skipping early exit found. Full 355096166-prime run was NOT independently repeated. |
| §§4,8.4–8.5 explanatory conclusions | OVERSTATED in places | Heuristic labels are appropriate, but sampled independence cannot establish that a forcing mechanism does not exist, nor that any proof must be algebraic or use growing moduli. Replace necessity/impossibility language by statements about the methods actually tried. |

## Almost-all proof and prior work

For fixed U, the excluded nonzero residues −u are distinct because u≤(ℓ+1)/4<ℓ. Including 0 is valid only for primes above Q; deleting it gives the integer version. In the C-even version require 8u∣ℓ+1. In every case ω(ℓ)<ℓ.
Fixed-modulus Mertens gives Σh=κ log log y+O_U(1), Σh log ℓ=κ log y+O_U(1), and Σh²=O_U(1). Therefore F=∏(1+h)≫_U(log y)^κ.
For y=Q^(1/K), δ=1/log y, the mass above Q is ≤F exp(−K+(e−1)κ+o(1)); choosing K=ceil((e−1)κ)+1 leaves a positive fraction below Q. Montgomery's sieve then gives O_U(X/log^κ X). Since κ→∞ with U, selecting U AFTER fixing A proves the advertised quantifiers. No effective uniformity in A or individual-prime conclusion follows.
**Priority comparison:** `FRONTIER.md` §5.1 records `Z56_FAMTRY.md` Theorem A: X exp(−0.08√log X), also shift-uniform and already bounding odd integer avoiders. This is strictly stronger than every fixed logarithmic saving for (★). TRYO's proof has a simpler fixed-modulus input, not a stronger target conclusion.
`Z53_PZ.md` Theorem A, also in FRONTIER §5.1, already gives R(p)≫log²p for almost all primes. PZ gives multiplicity information, unlike TRYO; FAMTRY supplies the stronger zero-set bound. The C-even variant is valid but does not rescue a claim of a new general almost-all breakthrough.

## Exhaustiveness / early-exit audit

The outer loop visits all six residues in every 840-block, clips both endpoints, and increments count for each primality-qualified p. The 12-base Miller–Rabin test is deterministic far beyond these ≤3·10¹¹ inputs; modular products use 128 bits.
Trial division followed by recursive rho fully factors p+u. Omitting prime factors dividing 4u is legitimate because a divisor ≡−1 modulo 4u cannot contain them. Every remaining prime-power combination is enumerated; overflowing the divisor buffer terminates with failure, not truncation.
`hasdiv` returns after the first divisor; the u-loop breaks after the first successful u. Neither exits the prime loop. The witness is rechecked in 128-bit arithmetic. UMAX=100000 is **not** an exhaustive bound for proving a negative: HARD means unresolved, not a certified zero. This does not harm the range claim because all four completed runs have hard=0.
Important operational caveat: the engine returns success even with HARD cases; accepting a future run requires parsing DONE and hard=0, not merely exit status. Here the nine small HARD cases were separately proved to be genuine zeros.
The four log counts sum to **355096166**; histogram counts match each run. Adjacent interval endpoints leave no gap or counted-prime overlap. Every logged record identity checks exactly; tails above 256 are 1,1,0,1.

Independent checker `scripts/z58_xrev_tryo_check.c` uses segmented Eratosthenes, trial factorization to completion, and recursive divisor generation: no Miller–Rabin, rho, or code copied from the reviewed engine. The serial driver is `scripts/z58_xrev_tryo_audit.py`.

| Inclusive independent slice | Primes in 𝔐 | Max least-u | Result |
|---|---:|---:|---|
| 10000000000–10001000000 | 1309 | 71 | exact records/count/histogram match; no HARD |
| 54999500000–55000500000 | 1239 | 20 | same |
| 99999500000–100000500000 | 1267 | 19 | same |
| 199999500000–200000500000 | 1209 | 26 | same |
| 299999000000–300000000000 | 1229 | 14 | same |
| 53498561849–53499561849 | 1291 | 316 | same; global record included |
| 219563649401–219564649401 | 1188 | 289 | same; run-d record included |

Total independently checked: **8732 primes**. This is a cross-check of the certification, not an independent certification of the entire range.
For pointwise zero checks, symmetry permits u≤B, hence 4u²−2u≤n and u≤floor((1+√(1+4n))/4). Enumerating every divisor at each such u exhausts all solutions, including C-even and 𝔊* restrictions.

## Falsifier ledger audit

| Screen | Checked outcome and required interpretation |
|---|---|
| F1 odd squares | Lemma 1.3 is correct; independent exhaustive checks of all 50 odd squares m² with 1≤m≤99 return zero. Fix §§8.7–8.8: (u/m²)=1 only when gcd(u,m)=1; otherwise it is 0. |
| F2 C-even / numerator 8 | All 12 listed primes independently have zero C-even solutions; their full ordered R counts reproduce 56,52,30,42,12,28,66,58,30,66,18,52. The almost-all statement tolerates these; the new full-(★) range does NOT certify C-even positivity. |
| F3 composites | All 285 listed numbers independently have zero solutions. Counts in §8.4 reproduce: 269758 primes, 643882 nonsquare composites; 13 prime zeros, 20 composite zeros coprime to 210, 15 of these in 𝔐, and 214/285 divisible by 3. Comparable small-sample rates are not proof that primality supplies only local information. |
| F4 prime / 𝔊* zeros | Independently reproduce all 14 full zeros and all 38 𝔊* zeros; exactly 24 of the latter have full-(★) solutions. The memo omits the 38-zero half of the mandatory ledger: add it explicitly. Prop. 8.7 holds at all 14 full zeros, with least NR set {5,7,11,13,17,19,23}, restricted to {11,13,17,19,23} inside 𝔐; an actual prime factor with ψ_u(q)=−1 was checked in each case. |

## Required fixes, in priority order

1. **Prior attribution:** explicitly compare with FAMTRY and PZ; do not record Theorem 2 or Proposition 3.1 as new frontier advances. Keep the simpler proof and C-even variant as such.
2. **Scope:** restrict “dead” to the specified no-threshold fixed-q covering. Replace “any proof must use moduli that grow with p”, “not accessible”, and “needs an algebraic forcing mechanism” by qualified reports of this lane's unsuccessful approaches. Pairwise sample ratios do not rule out higher-order or eventual forcing laws.
3. **Mandatory ledger:** include all 38 𝔊* zeros and distinguish full-family positivity from restricted-family positivity. No HOT LEAD is established.
4. **Minor precision:** correct the Jacobi coprimality proviso, the 2011 dissertation date, and the Huxley AP citation; state the short-interval ε range used in the displayed proof.

## Sources and reproduction

Huxley, *Large values of Dirichlet polynomials, III*, Acta Arith. 26 (1975), p.435, (1.1), explicitly treats Dirichlet characters with exponent 12/5: https://matwbn.icm.edu.pl/ksiazki/aa/aa26/aa2648.pdf (first page inspected). For the AP short-interval implication, see https://arxiv.org/html/2507.15334v1 §1 and Cor.2.4. Use the standard Vinogradov–Korobov region in that implication, rather than leaving the zero-free input ambiguous.
Bonn's original dissertation record explicitly states L=5 and year 2011: https://bonndoc.ulb.uni-bonn.de/xmlui/handle/20.500.11811/5074 . Burgess and Ankeny–Bach bounds checked against https://campus.lakeforest.edu/trevino/SurveyLeastNonResidue.pdf §§2,5,7.
All executed commands used `ulimit -v 4000000` and timeout≤1800; computations were serial. Compile the independent checker with `gcc -O2 -std=c11 -Wall -Wextra -Werror`; compile the extracted reviewed range engine as `/tmp/xrev_TRYO/original`; run `timeout 1800 uv run python scripts/z58_xrev_tryo_audit.py /tmp/xrev_TRYO` under the memory limit. Driver finishes PASS. Original levels/legeffect reruns match saved files; original range rerun [1,10⁸] gives the stated nine HARD primes and max-u 469.
**Final assessment:** narrowed/inconclusive analytically, with a valid extended computational range. ACCEPT-WITH-FIXES, not a pointwise ES breakthrough.
