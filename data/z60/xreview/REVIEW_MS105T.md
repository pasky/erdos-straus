# MS105T hostile cross-review — ACCEPT-WITH-FIXES

Reviewed `side-agent/z60-ms105t` at `2b88a14d399cf1c554cdd47a7e29107dae2fd952`.
Scope: every PROVED claim, decisive computations, F1–F4, and repository novelty. ES remains OPEN.
Outcome: the bounded-covering obstructions are correct, including the questioned q ≥ 19 / q = 17 step.
This narrows fixed-modulus methods; it neither disproves MS105 nor eliminates growing/size-controlled searches.

## Per-claim verdicts and independent derivations

| Claim | Classification | Check |
|---|---|---|
| Lemma 1.1, five forms | CORRECT | From d+1=4kC and n+k=ud obtain n=4ukC−u−k; reverse with d=4kC−1 and 1≤k<d. Divisibility gives j=(n+k)/u≡−1 mod 4k. Finally (4uC−1)(4kC−1)=4Cn+1; a positive −1-class divisor has a positive −1-class cofactor, recovering u,k≥1. |
| Lemma 1.2 | CORRECT | A common divisor of d,n divides k and d+1, hence is 1. Since 4ukC−u−k≥3uk−k≥2u, u<n; symmetry gives k<n. No primality assumption. |
| Lemma 1.3 | CORRECT | d=n+2≡3 mod 4, remainder k=2, and (n+3)/4 is even for n≡5 mod 8. |
| Lemma 2.1 | CORRECT | Write C=2^e c. For a≡−1 mod 4C, reciprocity gives (c/a)=1; if e>0, a≡7 mod 8 gives (2/a)=1. Thus (−C/a)=−1. Coprimality is automatic. |
| Lemma 2.2 / Cor 2.3 proof | CORRECT | 4Cn≡−1 mod a gives (n/a)=(−C/a)=−1. Reciprocity uses n≡1 mod 4; ka≡u mod n gives (uk/n)=−1 only when gcd(uk,n)=1. Squares are excluded using (n/a), which needs no extra gcd(uk,n) hypothesis. For n=sm², gcd(m,a)=1 gives (n/a)=(s/a). |
| Lemma 2.4 | CORRECT, PRIOR | Reducing modulo a prime dividing u,n forces that prime to divide k. Substituting u=gu′, k=gk′ divides n by g and replaces C by gC; the inverse requires g∣C. Exactly Z59_MSPLUS Lemma 5.1. |
| Proposition 3.1 | CORRECT, PRIOR | Dirichlet supplies primes 1 mod 420M. A D-class would require d∣k+1 with k≤(d+1)/4<d−1. A P-class would require 4uk∣u+k+1, but 4uk−u−k−1≥1. |
| Theorem 3.2 | CORRECT | Both D and P arguments re-derived below; the condition is sufficient, not asserted necessary. This concerns a profinite point, not an integer zero. |
| Corollary 3.3 | CORRECT | The elementary least-nonresidue bound and CRT/Dirichlet quantifiers check; details below. The q=5,7 assertion is only for the specified finite M. |
| Corollary 3.4 | CORRECT, PRIOR CONSEQUENCE | For integer B≥1 take M=4 lcm(1,…,4B). If uk≤B then 4uk∣M; if kC≤B or uC≤B then the corresponding d=4kC−1 or 4uC−1 divides M. Apply 3.1 simultaneously. For real B use its integer part. |
| Theorem 4.1 / coverage table | CORRECT / CERTIFIED | Independently rebuilt all five rows, including 6275 uncovered out of 164736 at M=1441440. A positive representative ≥M exceeds every relevant minimal solution. |
| Zero / near-square / signature tables | CORRECT / CERTIFIED | Original and independent complete sieves agree through 30000000; all stated counts and displayed signatures agree. |
| §5A character identity / evidence | CORRECT | Orthogonality applies since gcd(4Cn+1,4C)=1; ψ_C is a nonprincipal odd character. All five C≤3000 numerical rows and the n=29 positive-E control reproduce. |
| §5B–D failure diagnoses | Assessment, not impossibility theorems | Fixed menus are excluded; pointwise divisor bounds, growing menus, conditional inheritance, and other composite methods are not. “Every product/gluing rule” is too broad literally. |

### Theorem 3.2, checked algebra

D-case: write d=Qt, Q=q^a, k+1=ts, k+r=cQ, Qt+1=4kj. If a=0, d∣k+1 is impossible.
Otherwise kf=rt+c with f=4cj−t≥1. For f>r, t≤k+1 implies k≤r+c, hence Q≤2r+1, contradiction.
For f≤r, substitution gives t(sf−r)=c+f, so g=sf−r≥1 and tg=c+f.
The memo's D=tg−f is simply c>0; using k=cQ−r gives c(Qf−1)=r(t+f).
Since t≤tg=c+f, obtain c(Qf−1−r)≤2rf, hence f(Q−2r)≤r+1, contradicting Q>3r+1.
P-case: q∤uk is excluded by 4uk>u+k+1; q∣u,k contradicts q∤r.
Otherwise k=Qk′, q∤u, gives u≥Q−r and 1+u+Qk′=4euk′.
Thus 1≤4eu−Q≤1+u, so 3u≤Q+1 and Q≤(3r+1)/2, contradiction. No quadratic assumption was used.

### Corollary 3.3, threshold and quantifiers

Let v be the least nonresidue modulo q. If v≥√q+1, put a=⌈q/v⌉ and b=av−q.
Then 1≤a,b<v, so both are residues, whereas χ(b)=χ(a)χ(v)=−1: contradiction. Thus v<√q+1.
For q≥19, √q+1≤(q−2)/3 (equivalently q−5≥3√q, true at 19 and increasing thereafter).
For q=11,13 use r=2; for q=17 use r=3, and 17>3·3+1. There is **no threshold error** here.
The CRT moduli q^{v_q(M)+1} and 420M/q^{v_q(M)} are coprime for q≥11; the prescribed class is a unit.
It agrees with the profinite point modulo M, so Dirichlet gives infinitely many avoiding primes for **each fixed M**.
The order is ∀M ∃infinitely many p, not ∃p ∀M; neither actual global zeros nor a rate of witness growth follows.
For q=5,7, the uncovered unit classes 577 and 409 at M=1441440 suffice for Dirichlet.
The additional example 29210401 is not itself a unit class modulo M (11 divides both), so is not a prime-progression certificate.
Cor 3.4 is similarly universal over solutions and may be vacuous at a zero; it does not prove existence.
Its one-small-coordinate example is valid: u=1, k=T−2, C=Th/4 gives p=T(T−2)h−T+1;
this progression also contains infinitely many primes since gcd(T(T−2),T−1)=1.

## Recomputations

All executions used `ulimit -v 4000000` and individual timeouts ≤900 s; no full Cartesian-product allocations.
The archived original C sieve reproduces its zero file byte-for-byte at N=30000000.
`scripts/z60_xrev_ms105t_check.c` independently sieves u≤k pair-progressions, retaining u+k≡3 mod 4.
It outputs exactly the same 3100 zeros: 2739 odd squares, 361 nonsquares; 38 unit nonsquares = 14 primes + 24 composites.
The other 323 nonsquares are nonunits. All factorizations/tags verify; only 752257 among the 38 is nonsquarefree.
The 285-composite screen agrees exactly below 7999802; all 2280 zeros ≥1441440 are uncovered modulo 1441440.
Independent coverage rows (admissible, uncovered, square-uncovered, nonsquare-uncovered):
`840:(96,11,6,5); 9240:(1056,94,36,58); 120120:(13728,899,252,647); 360360:(41184,2348,756,1592); 1441440:(164736,6275,3024,3251)`.
Original p-adic scripts reproduce all seven claimed no-hit checks and the q=37 list {23,24,32,35}.
The five character rows give R=(0,32,0,0,32), E=(−26.700,−12.520,−27.968,−31.181,−22.278); n=29,C≤4 gives E=1.
For the §5A “equality for all C iff square” assertion: a nonsquare n has an odd prime ℓ∤n with (n/ℓ)=−1;
choose C with 4Cn+1≡0 mod ℓ. Its divisor-character sum is then strictly below τ(4Cn+1). Squares give equality for every C.

Reproduce the independent audit after extracting the reviewed branch to `/tmp/xrev_MS105T`:
`timeout 30 cc -O2 -Wall -Wextra scripts/z60_xrev_ms105t_check.c -o /tmp/xrev_MS105T/check`
`timeout 900 uv run --python .venv/bin/python --no-project python scripts/z60_xrev_ms105t_audit.py /tmp/xrev_MS105T /tmp/xrev_MS105T/check`
Apply the memory limit before both commands. The audit prints coverage, near-square exceptions, signatures, and screen witnesses.

## Mandatory falsifiers

| Screen | Independent result / required interpretation |
|---|---|
| F1 odd squares / sm² | PASS. Jacobi proof excludes every odd square. All listed zero-free cores and exceptions reproduce; this is bounded evidence, not an eventual near-square theorem. Z59_MSPLUS Lemma 4.1 already proves the stronger density-zero result for each fixed nonsquare core. |
| F2 C-even / numerator 8 | PASS. Independent integer-only enumeration over the three order regions u≤k≤C, u≤C<k, C<u≤k reproduces all 12 R/R8 counts exactly: R>0, R8=0. Every exhibited full-family witness has odd C; e.g. 10532106649=(4·5·2472906·213)−5−2472906. A C-even positivity claim at these thresholds would fail; eventual C-even positivity at a higher threshold is not refuted. |
| F3 285 composite zeros | PASS with wording fix. Exact list equality and 24 coprime composites confirmed. 2929=29·101 disproves unconditional good×good closure, not all conditional gluing/descent rules. Lemma 2.4 is valid but already prior. |
| F4 14 ★ / 38 𝔊* prime zeros | INCOMPLETE IN MEMO. It discusses the 14 but omits the 38-family distinction. Independent full-family counts on all 38 give precisely those 14 zeros and 24 positives; e.g. 37 has (u,k,C)=(1,2,5), and 564661441 has (9,206,76141). The other 24 obstruct 𝔊*, not MS105. Their restricted-family zero status is inherited from the screen; full-family behavior was recomputed here. |

## Prior work and required fixes (priority order)

1. **Complete F4** with the 38/14/24 distinction above. Keep all impossibility readings restricted to fixed finite menus, with the correct quantifier order; replace “every product/gluing rule except…” by “unconditional good×good closure”. No HOT LEAD or ES claim is justified.
2. **Credit prior results, rather than presenting a new barrier/target.** `git grep` and source inspection give:
   - `Z59_MSPLUS` §1 already states MS⁺₁₀₅ with threshold 29210401 and certification to 10¹⁰; §5.3 already lists exactly 38 zeros. This 3·10⁷ census is a recheck of a subset, not a stronger census or new target.
   - Its Lemma 2.0 already gives dead moduli / common-prime constraints; Lemma 5.1 is exactly this Lemma 2.4; §4 and §5.1 already cover near-squares and failure of closure.
   - `Z58_LOGIC` §4 has the all-n census to 10¹⁰; Prop 5.4 reduces all three two-small-coordinate shapes to finite congruence menus. Together with B1 this already implies Cor 3.4. `Z58_LADDER` Cor 1.3 already excludes bounded SC(D).
   - `Z57_SYNTH` Lemma A.1 already supplies the hit-class/Jacobi/square mechanism; Prop A.3 already refutes finite-D nonresidue covering at q=11.
   - Its cited source `Z55_HCF` Thm 3.1 / Cor 3.2–3.3 already has the same q>3r+1 profinite obstruction and **every q≥11** specialization for D-certificates. A D-class here maps to line T with c=(d+1)/k. The explicit P-class proof here is an additional elementary formulation; do not call the whole nonresidue barrier new. No external-literature novelty is established.
3. **Fix certificate generator UB:** `z60_ms105t_zeros.c` prints the int-valued gcd expression with `%ld`; change it to `%d` or cast to long. `-Wall -Wextra` diagnoses this. The independent sieve validates the numbers despite that implementation defect.

**Final verdict: ACCEPT-WITH-FIXES.** All labelled proofs survive; decisive computations agree. The valid outcome is a largely prior fixed-covering obstruction plus reproducible finite checks, not a disproof of bounded single-coordinate or growing-modulus approaches, and not progress establishing MS105 positivity.
