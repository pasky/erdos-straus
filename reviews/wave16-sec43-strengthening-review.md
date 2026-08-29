# Wave 16 hostile review — §43 thinned-window strengthening

**Verdict: STRENGTHENING CONFIRMED.**  The fourth-root thinning is valid at the same internal, provisional level as §39.  The finite relative-mass inequality is strong enough to shrink both the quarantine cutoff and Bonferroni degree to the actual mass
\(M=\theta_m t^3\), \(\theta_m=\eta_2(m)/\varphi(m)\).  The resulting ledger is \(O(Mt)=O(\theta_mt^4)\), and optimization gives
\[
 E_m(N)\ll N\exp\{-c[\eta_2(m)(\log N)^3/\varphi(m)]^{1/4}\}
\]
uniformly for every fixed-gap range \(m\leq(\log N)^{3-\epsilon}\), for primes and all denominators.  This verdict does not upgrade Theorem 34.8, §39, or the new theorem beyond **CLAIMED/PROVISIONAL**.

## Scope and inherited status

I read §39 in full before adjudication, then checked the relevant §16 and §34 proofs, all of §43, and the frozen plus post-freeze portions of `blind43.md`.  In particular I replayed (39.13)–(39.19), (39.21)–(39.34), Theorem 34.8's arbitrary-subfamily quantifiers, the general-\(m\) profiles (43.19)–(43.27), and Theorem 16.5's Rankin transfer.  The review treats Theorem 34.8 and the three soft spots in §39.7 as inherited inputs, not as newly validated facts.

## 1. Relative multiplier mass and quarantine — CONFIRMED

Put
\[
 H_m(K)=\sum_{k\le K,(k,m)=1}\frac{\varphi(k)}{k^2}.
\]
For \(p\nmid m\), unique decomposition \(k=p^ea\), \(p\nmid a\), gives the finite inequality
\[
 \sum_{k\le K,(k,m)=1,p\mid k}\frac{\varphi(k)}{k^2}
 =\sum_{e\ge1}\frac{1-1/p}{p^e}
   \sum_{a\le K/p^e,(a,pm)=1}\frac{\varphi(a)}{a^2}
 \le \frac{H_m(K)}p.
\]
For \(p\mid m\) the left side is zero.  This does not use a fixed residue-class asymptotic and is uniform in finite \(K,m\).

If \(\mathcal J_c=\{k\le K:(k,m)=(k,c)=1\}\), the union bound therefore gives
\[
 h(\mathcal J_c)\ge H_m(K)\left(1-
   \sum_{y<p\le K,\ p\mid c,\ p\mid L_{m,K}}\frac1p\right).
\]
A fixed threshold \(Z(c)\le\eta_0<1\) retains a fixed fraction of the *actual* mass \(H_m(K)\asymp\eta_1(m)\log K\).  The old threshold \(Z\ll\eta_1(m)\), and its corresponding \(1/\eta_1\) penalty in \(y\), are unnecessary.

After conditioning on primes at most \(y\), the remaining coordinates are independent and
\[
 \mathbb E e^{yZ}\le
 \exp\{Cy\sum_{p>y}p^{-2}\}=e^{O(1)},\qquad
 \Pr(Z>\eta_0)\le e^{-\eta_0y+O(1)}.
\]
Taking \(y=B_0M\), where \(M=\theta_mt^3\), makes the bad-fibre cost \(e^{-cM}\) after choosing \(B_0\).  The ratio-of-constants issue closes: the target and bad tail have the same variable \(M\), and \(B_0\) is selected after the fixed good-fibre constant.  Also \(y\sum_{p>y}p^{-2}=O(1)\) remains uniform.

On a good fibre, Theorem 43.7 gives
\[
 \frac{t^2h(\mathcal J_c)}{\varphi(m)}
 \gg\frac{\eta_1(m)}{\varphi(m)}t^3\asymp M,
\]
because \(\eta_1\asymp\eta_2\).  Hence the conditioned void is \(e^{-cM}\).  This also resolves the quarantine-floor concern: disabling a fixed relative portion of the thinned multiplier family requires \(Z\gg1\), whose probability is \(e^{-cy}=e^{-cM}\).  No floor of the old size \(e^{-ct^3}\) remains when the target itself is only \(e^{-cM}\).

## 2. Selector and unconditioned primes — CONFIRMED

The selector \(S_y=\mathbf1_{(n,P_y)=1}\) has degree \(\pi(y)=O(M)\) and \(\log P_y=O(y)=O(M)\).  In the stated range \(M\to\infty\), \(2\le y<X^{1/2}\); every exceptional prime above the omitted finite range has \(S_y=1\).

Shrinking \(y\) exposes more shared primes in (39.15)/(43.25), but the general-\(m\) Euler inequality (43.26) is uniform in every \(y\ge2\).  At a conditioned prime \(p\mid m\), deletion contributes \(p/(p+1)\), not the \(\eta_2\)-factor \(p^2/(p^2+p-1)\); it is smaller, so the required upper bound by \(\eta_2(m)\log K\) survives.  This is a wave-15 correction to one sentence in the blind proof, not a failure of the thinned argument.

The mass-profile proof is likewise uniform in the cutoff: the \(q_y(k)\), \(b_y(g)\), and \(1/\varphi(g)\) cancellation leaves only \(p/(p-1)\) at an unconditioned shared prime, and the quotient from the unmodified local factor is \(1+O(p^{-2})\).  Thus no new \(\log\log m\), \(m/\varphi(m)\), or cutoff-dependent factor appears.

## 3. Factorial moments and Bonferroni — CONFIRMED

Equation (43.27) gives, at every order \(j\),
\[
 \mathbb E(H_{m,X})_j\le(CM)^j,
 \qquad M=\frac{\eta_2(m)}{\varphi(m)}t^3.
\]
This is the needed thinned base, not merely the old \((Ct^3)^j\) bound.  Take the least even \(r\ge D_0M\).  Stirling gives
\[
 \frac{(CM)^{r+1}}{(r+1)!}
 \le \left(\frac{eCM}{r+1}\right)^{r+1}
 \le e^{-cM}
\]
for fixed sufficiently large \(D_0\).  Combining this with the void and the exact nonnegative even-Bonferroni identity proves
\(\mathbb E S_yQ_r(H_{m,X})\le e^{-cM}\).  If \(M=O(1)\), fixed even degree gives only constant strength; the uniform theorem avoids this case by imposing a fixed gap below \(m=(\log N)^3\).

## 4. Congruence ledger and window — CONFIRMED

With \(y,r=O(M)\),
\[
 \deg=O(M),\qquad
 \log d_{\rm term}\le O(y)+r(\log K+t)=O(Mt),
\]
while \(\log|\mathcal A_{m,X}|=O(t)\) gives
\[
 \log\sum|c_{\rm term}|=O(rt)=O(Mt).
\]
The atom cylinder has modulus \(k\ell\).  The factor \(m\) selects which atoms exist via \(muv\mid k\ell+1\), but it does not enter the cylinder modulus and therefore does not contribute an \(m^r\) ledger term.  Since \(\log K=\kappa t\), the full rounding condition is
\[
 \log N\ge C_0Mt=C_0\theta_mt^4.
\]
Choosing \(t=\alpha(\log N/\theta_m)^{1/4}\) yields
\[
 M\asymp\theta_m^{1/4}(\log N)^{3/4},
\]
which is exactly the claimed fourth-root exponent.  The selector modulus costs \(O(M)\), strictly below the existing \(O(Mt)\) budget.

## 5. Analytic and uniformity range — CONFIRMED WITH EXPLICIT RANGE

Let \(L=\log N\) and \(\Theta_m=1/\theta_m=\varphi(m)/\eta_2(m)\asymp m\).  At the optimum
\[
 t\asymp(L\Theta_m)^{1/4},\qquad
 \frac tL\asymp(\Theta_m/L^3)^{1/4},\qquad
 M\asymp L^{3/4}\Theta_m^{-1/4}.
\]
Thus \(\Theta_m\le L^{3-\epsilon}\) gives \(t=o(L)\) and \(M\gg L^{\epsilon/4}\).  Conversely, at \(\Theta_m\asymp L^3\), \(t\asymp L\) and \(M\asymp1\); both the growing saving and finite-window separation disappear.  The honest clean theorem is therefore the fixed-gap range
\[
 m\le L^{3-\epsilon}.
\]

All subsidiary constraints have room there:

- Since \(t^4\asymp L\Theta_m\) and \(m\asymp\Theta_m\), one fixed log-power bound \(m\le t^B\) suffices; \(B=4\) works for large \(L\).
- Consequently \(K=e^{\kappa t}\gg m\), so the aggregate multiplier sums are in their valid regime; no short fixed-class asymptotic is used.
- In the bottom block, \(muv\le t^Bx^{1/3}\) is exponentially below the Bombieri–Vinogradov level.  The fixed BV saving may depend on the fixed \(B\), not on \(m\).
- The extended Lemma 16.2 and Theorem 34.8 retain \(z>K^{20}\) because \(\kappa<1/240\); shrinking \(y\) does not alter \(H,z,K\), the incidence pruning, or the canonical boxes.
- \(y=O(M)\le O(t^3)<X^{1/2}\), and \(\max(m,K,y)=e^{o(L)}\), so the omitted denominator range is negligible.

This confirms the range rather than the blind file's compressed statement that there was merely “room.”

## 6. All-denominator transfer — CONFIRMED

For the strengthened prime bound use
\(g_m(u)=\Theta_m^{-1/4}u^{3/4}\) and
\(\delta\asymp g_m(L)/L=\Theta_m^{-1/4}L^{-1/4}\).  Fix a final margin \(\epsilon_0\), choose
\(0<\epsilon'<\epsilon_0/(4-\epsilon_0)\), and invoke the prime theorem only above
\[
 u_0=\log x_0\asymp\Theta_m^{1/(3-\epsilon')}.
\]
Then, under \(\Theta_m\le L^{3-\epsilon_0}\),
\[
 \delta u_0\ll
 L^{-1/4}\Theta_m^{1/(3-\epsilon')-1/4}
 \ll L^{-\gamma},
 \quad
 \gamma=\frac{\epsilon_0(1+\epsilon')-4\epsilon'}{4(3-\epsilon')}>0.
\]
Allowing every prime below \(x_0\) therefore costs an Euler factor
\(\exp\{O(\log\Theta_m)\}=e^{o(g_m(L))}\).  Above \(x_0\),
\(g_m(u)/u\) decreases, so \(\delta u\le\eta g_m(u)\) as in Theorem 16.5.  Moreover
\(g_m(u_0)=\Theta_m^{\epsilon'/(4(3-\epsilon'))}\); after the substitution
\(w=\Theta_m^{-1/4}u^{3/4}\), this positive-power lower endpoint beats the polynomial Jacobian uniformly.  Partial summation is therefore summable with room.  The semigroup transfer preserves both the exponent shape and the full fixed-gap range.

## 7. PW crossover and Layer 1 — CONFIRMED AFTER RECOMPUTATION

For the strengthened Layer 2 and PW,
\[
 R=(\eta_2/\varphi)^{1/4}L^{3/4},\qquad
 P=L^{2/3}/\varphi^{1/3},
\]
so
\[
 \frac RP=(\eta_2^3\varphi L)^{1/12},
 \qquad
 R\ge P\iff
 L^{1/12}\ge\varphi^{-1/3}(\varphi/\eta_2)^{1/4}
 \iff L\ge(\eta_2^3\varphi)^{-1}.
\]
The inverse \(\varphi^{-1/3}\) is essential.  The former crossover
\(\varphi\lesssim\eta_1^{3/2}L^{1/8}\) applies only to conservative Theorem 43.8 and must not be retained as the headline comparison.  In PW's range \(m\le L^2\), the new provisional scale wins after the exact crossover; the new theorem itself continues through \(m\le L^{3-\epsilon}\), while PW's quoted theorem stops at \(L^2\).  Unknown absolute constants and the provisional-versus-literature status prevent interpreting the scale identity as a literal finite threshold.

The blind S3 range repair is also correct after replacing its frozen cutoff.  Put \(\Theta_1=\varphi(m)/\eta_1(m)\asymp m\), start the prime estimate at
\(u_0=\Theta_1^{1/(2-\epsilon')}\), and use
\(\delta\asymp\Theta_1^{-1/3}L^{-1/3}(\log L)^{1/3}\).  If
\(\Theta_1\le L^{2-\epsilon_0}\) and
\(\epsilon'<\epsilon_0/(3-\epsilon_0)\), then
\[
 \delta u_0\ll L^{-\gamma}(\log L)^{1/3},
 \quad
 \gamma=\frac{\epsilon_0(1+\epsilon')-3\epsilon'}{3(2-\epsilon')}>0.
\]
Small primes cost \(\exp\{O(\log\Theta_1)\}\), absorbed by the Layer-1 saving, and the large-prime tail is uniform.  Hence §43's old all-denominator range \(L^{1-\epsilon}\) was conservative and is repaired to the prime range \(L^{2-\epsilon}\).  This uses no new distribution theorem.

## 8. Blind attestation and disposition

The attestation correctly records convergence on S1, the aggregate S2 structure, S4, and S5.  It must not call every sentence of S2 or S6 converged: fixed-class short-range uniformity is not used, and the frozen S6 local-deletion sentence required the wave-15 correction.  S3 diverged only in the all-denominator cutoff; its conclusion survives after the post-freeze repair.  S6 and S7 genuinely diverged substantively and supplied the confirmed strengthening.  §43.11 now states these qualifications explicitly.

Repairs made in `notes.md`:

- added Theorem 43.12 with the finite inequality, quarantine, moments, ledger, range, and semigroup proof;
- retained Theorem 43.8 as a valid conservative replay and revised Failure log 43.9;
- replaced the PW crossover with the exact fourth-root comparison;
- enlarged Layer 1's all-denominator range to \(m\le L^{2-\epsilon}\) with a corrected cutoff;
- tightened §43.11's convergence table and added Assessment 43.13.

**Final verdict: STRENGTHENING CONFIRMED.**
