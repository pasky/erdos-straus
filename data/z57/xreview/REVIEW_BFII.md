# BFII hostile cross-review — ACCEPT-WITH-FIXES

Reviewed `side-agent/z57-bfii` at `47a02272400cea8dd0208bcaa95a01d1b2f828c4`, including Appendix A.
**Theorem G survives this review. The target f_II(p) ≥ 1 for every large prime is not proved; ES remains OPEN.**
No theorem-level GAP or counterexample to Theorem G was found. Required fixes concern the interpretation of the remainder and the general-n definitions, not its analytic estimates.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| §1 general-n ET correspondence | CORRECT-WITH-FIX | Keep ET's condition gcd(abd,n)=1 when asserting the converse correspondence. Primitive N-points alone need not give Type II at composite n; explicit example below. |
| Lemma 1.0 (prime existence equivalence) | CORRECT | If p divides abd, all three denominators are divisible by p, giving 4 ≤ 3. Dividing a,b,c by their common gcd g and replacing d by g²d preserves the equation and denominators. ET supplies the converse. |
| Lemma 1.1(a–c) | CORRECT | Set e=(a+b)/c; then 4abd=n+e. Substitution b=ce−a gives (b); solving b(4acd−1)=cn+a gives (c). All inverse maps preserve positivity, including ce>a in (b). |
| Lemma 1.1(d–f) | CORRECT | For f=4acd−1, a,c are units and d=(f+1)/(4ac). Multiplication by the units 4ad or 4cd yields the two nontrivial divisor slices. The c-line map is (u,B,C)=(a,b,cd), with c recorded. Multiplicities, not merely distinct targets, are retained. |
| Lemma 2.1 | CORRECT | Split k=2^s k′. For s>0, f≡7 mod 8 gives (2/f)=1. Odd reciprocity cancels (−1/k′) against the sign from f≡3 mod 4. |
| Proposition 2.2 | CORRECT | −n≡a/c mod f is a unit; (a/c/f)=(ac/f)=1 by Lemma 2.1. Thus (n/f)=−1; exchange a,b for f′. |
| Corollaries 2.3–2.4 and witness implication | CORRECT | A unit square cannot have Jacobi symbol −1. At p≡1 mod 4, some prime factor ℓ of f has (p/ℓ)=−1, hence (ℓ/p)=−1 and n_p≤ℓ≤f. The algebra actually extends the square obstruction to even squares too. |
| Proposition 3.1(a–c) | CORRECT | Direct target sets give completeness at 3,7,15. Since τ₃((f+1)/4)=f^{o(1)} and φ(f)=f^{1−o(1)}, completeness is finite. The mod-5 implication follows from (p/15)=(p/3)(p/5); small exceptional primes 3,5,7 are covered directly. |
| Proposition 3.2 | CORRECT | Dirichlet supplies infinitely many primes 1 mod 4·lcm(f_i); every listed Jacobi witness then fails. This forbids finite witness coverings, not arbitrary infinite constructions. |
| §5.2 Fourier identity | CORRECT | Character orthogonality counts p≡−e mod 4ab, with d=(p+e)/(4ab)>0. For prime p, any term with p dividing 4ab cannot be a solution, so zero-valued characters cause no loss. |
| §5.3 genus identity | CORRECT | Locally (c/a/ℓ)=(ac/ℓ); the weight depends only on u=ac. There are τ(u) ordered factorizations u=ac. Hensel lifting gives exactly 2^{ω(f)}/φ(f), not an extra factor two. |
| Appendix A Lemma 1 | CORRECT | Primitive discriminants are −4up or −up, with only the extra factor at 2 removed. Multiplying the local g-series by (1−Z)(1−χ(ℓ)Z) gives the stated h. At Z=1/ℓ the good-prime factor is 1+χ(ℓ)/ℓ². Thus H/φ(4u)=(1−1/p)B_u/(4u). Absolute convergence at t=1/3, B_u>1/2, and L(1,χ)≥0 all follow as stated. |
| Appendix A Lemma 2 | CORRECT | PV and Abel give the F-tail K_F/t; Burgess gives the G-tail K_G/√t. The hyperbola error is bounded by 2K_G√(z/y)+K_F/z+K_F K_G/√(yz). Taking z=(K_F²y/K_G²)^{1/3} gives 3E+E². The principal version follows from the harmonic-sum expansion; the sign of L′ is positive. The E>1 and y<1 cases are covered by the stated logarithmic bounds. |
| Appendix A Lemma 3 | CORRECT | ψ*χ_u retains a nontrivial component at p for every ψ mod 4u, including complex ψ. Its conductor divides 4up and is cube-free; removed primes divide 2u. Twisting the convolution, summing h absolutely, and subtracting endpoints kills nonprincipal constants. Character averaging preserves, rather than multiplies, the uniform error. |
| Appendix A Lemma 4 | CORRECT | Odd unrestricted harmonic mass is L_A L_C/4+o(1). The three exclusions each cost at most S times this mass plus vanishing error, with S=π²/8−1<1/4. The endpoint exponents make all listed errors vanish. |
| Appendix A Lemma 5 | CORRECT | Truncate at N=p^0.29. For nonsquare odd n=n₁s², (·/n₁) is primitive and nonprincipal. Expanding μ²(c), removing gcd(c,2as), and applying r=20 Burgess gives the claimed weighted c-sum. The e-sum converges since 2−2/r>1. Square n contribute nonnegatively; n=1 contributes the harmonic mass. |
| Theorem G / A.4 | CORRECT | The box has at most p^0.091 pairs. Its main coefficient is at least 1/16 times the L-value average. The total absolute error is O(p^−0.049); the resulting coefficient 1.7578125·10^−9 exceeds 10^−10. All limiting constants are effective, albeit uncomputed. |
| A.5 square audit | CORRECT | Every square-unit test fails at n=m². The character induced by χ_{−u} makes the twisted factor principal, and its progression coefficient is −1; its window cancels the principal window. This is exactly the missing hypothesis at squares. |
| §5.5 SB ⇒ existence | CORRECT | Lemma 3 is uniform for F≥p^0.9 and 2F≤p^0.99. Replacing log(X/Y) by log 2 and summing the same box yields positive G_F for every such F at sufficiently large p. SB then gives A_F>0. SB itself remains CONDITIONAL. |
| §5.3(ii): remainder “also scales up (it equals −G at squares)” | WRONG as justification | At squares A=G=X=0. The equality X=−G there provides no nonzero remainder lower bound and proves no scaling at primes. The identity itself is correct. |
| §§0,5–6: unbounded-order information “needed”; no independent averaging variable | Assessment only | These representations expose a difficult character remainder, but do not prove that every possible argument must estimate its individual characters, or that reorganising/summing c cannot help. |

## Decisive analytic checks and sources

Recomputed the exponent margins exactly: slice −0.148457606; L-series tail −0.000179534;
outer nonsquare sum −0.00019346. Each has genuine room for effective p^{o(1)} losses.
The convolution extension to k>T is legitimate: Lemma 2 includes y<1 and Σ |h(k)|k^{−2/3}(1+log k)² converges.
No Siegel lower bound, zero-free region, GRH, or prime-average estimate is hidden in the proof.

ET was checked directly in `sources/elsholtz-tao-1107.1010.pdf`, §2, pp. 14–15, (2.13)–(2.22), Propositions 2.6–2.7.
The Burgess input was checked against [arXiv:2511.17778v2, §1 and Theorems 1.1–1.2](https://arxiv.org/html/2511.17778v2):
primitive complex characters are allowed; arbitrary r is allowed for cube-free conductor; effective constants are available.
PV also follows directly from the primitive Gauss-sum Fourier expansion and the O(log Q) harmonic bound.
I rederived the tail and hyperbola inputs in `Z53_GENUSLVAL.md` §§2.2–2.3 rather than importing its later theorems.
The memory-qualified Graham–Ringrose/Montgomery progression assertions were not promoted to verified inputs; they are unnecessary here.

## Reproduction and numerical agreement

All shell invocations had memory/CPU limits and `timeout`; computations used `ulimit -v 6000000`, with a 1000-second timeout for the enumerator.
Files were extracted from the pinned branch into `/tmp/xrev_BFII`; no source-branch files were changed.
I inspected the enumerator, witness sieve, block engine, validators, and numerical L-value implementation before running them.
The enumerator's stopping bounds follow from e≤a+b and d≥1; the witness test uses a≤m_f<f, so its residue candidate is unique.
The enumerator uses approximately 1 GB; the L-check streams 250000-element chunks and uses bounded sieve arrays.

| Re-run | Result |
|---|---|
| `z57_bfii_enum.c 10000000` + `z57_bfii_stats.py` | Full statistical output matches byte-for-byte: 1580 odd-square zeros and only nonsquare zero 4545; every odd prime is covered. |
| Same full count, independently queried | The 14 p≡1 mod 4 with R=0 have N in [14,156]. At 2031121, (N,R,primitive)=(40,6,36). Mean N/log³p=0.0756 and c≥2 share=0.858 in [10⁶,10⁷). |
| Existing brute validator through 400 | Zero mismatches against direct quadruples and direct Egyptian-fraction Type II counts; every odd square has zero count. |
| Existing f-form validator, all 10 listed n through 99991 | All agree, including 4545 and the diagonal correction at 99991. |
| Witness scan [5,10⁹), FMAX=400000 | 25423491 primes; maximum least f=3263 at 605531161; 18 c=1 misses; zero least-QNR violations. All output agrees apart from archived timing lines. |
| Witness scan [10¹²,10¹²+10⁸), same cap | 1809206 primes; maximum least f=1079 at 1000077030541; no c=1 misses; zero QNR violations. Same agreement. |
| Complete-modulus scan f<4000 | Exactly [3,7,15], zero target-Jacobi violations; output identical. |
| Block engine [10⁷,10100000), f∈[1024,16384), then statistics | All 3087 primes rerun; statistics identical: mean relative errors 0.202 versus 0.358, minimum full A/G=0.301, zero full-count misses. |
| All nine Appendix A.6 slice checks | Exact output identical, including all local-factor ratios and pooled values. These remain numerical evidence, not a test of the asymptotic thin box. |

The separate six-prime dyadic profile (§4.3) was not rerun; no acceptance decision depends on its extra percentages.
These are reruns of inspected code, supplemented by the existing independent enumeration forms, not a new independently written exhaustive engine.

## Required fixes, in priority order

1. Remove the inference that the remainder scales up because of squares. Write explicitly **A(m²)=G(m²)=X(m²)=0**.
   Replace “controlling it needs information of unbounded order” by “this expansion contains unbounded-order characters, and no sufficient aggregate bound is supplied.”
   Mark the broad impossibility language in §§5.1,5.4 and the verdict as Assessment; only the finite-covering and least-QNR implications are proved barriers.
2. In §1 retain **gcd(abd,n)=1** in the general-n ET correspondence, or make it explicitly one-way before specialising to primes.
   For n=63, (a,b,c,d)=(3,6,1,1) is primitive and satisfies (2.15), but gives (x,y,z)=(18,189,378) with gcd(x,63)=9, not Type II.
   This does not invalidate the deliberately unrestricted N-count or the prime equivalence.
3. In §5.5 replace “GRH controls χ(p) on average over characters” with “standard GRH character-sum/AP estimates do not directly supply SB; no implication is established here.”
   Keep the memory-qualified least-non-residue lower bounds outside the PROVED inventory. The c=1 genus mean comparison should have a same-coordinate citation/proof or an explicit heuristic label; it is not a pointwise upper bound.

## Verdict

**ACCEPT-WITH-FIXES.** The proved genus lower bound strengthens the genus side, and the decisive finite computations reproduce.
The honest lane outcome is **narrowed / target unresolved**, not dead: no bound on the actual remainder proves eventual Type II existence or rules out future use of c.
After the wording and hypothesis fixes, the listed exact identities, witness barriers, finite-covering theorem, Theorem G, and SB implication may be retained as PROVED.
