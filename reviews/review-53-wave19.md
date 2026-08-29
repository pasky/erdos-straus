# Wave 19 hostile review: §53 stacked slice sieve

## Overall verdict

**SOUND-AFTER-REPAIRS.** I tried to break the headline growing theorem at its overlap quotient, genus conditioning, Page deletion, growing-dimensional fundamental lemma, class summation, and low-tail optimization. The theorem survives. The large-$s$ form actually supplied by Friedlander–Iwaniec has the uniform error needed here, and the proof avoids any prime-counting theorem modulo $Q_T$ by sieving integers before summing classes.

I did find two proof-text defects with direct overclaim risk: the original corollary used the varying cutoff in the wrong inclusion direction, and the no-exception branch set $r=1$, which would literally delete every slice. Both are repaired. I also repaired the misstated “sharp $4T^2$” overlap threshold, wrote the exact growing-$\kappa$ fundamental-lemma error and corrected $s$, added the requested Dahan comparison, and fixed pre-existing eaten-backslash/array artifacts. No exponent, theorem statement, or effectivity label had to be weakened.

## Claim verdicts

| Claim | Verdict | Hostile finding |
|---|---|---|
| Lemma 53.1a, overlap geometry | **CONFIRMED-AFTER-REPAIR (applied)** | Common roots give $q\mid4(d_1-d_2)$, and equal radicands have identical roots. The old “sharp $4T^2$” threshold was false as a sharpness claim: at odd $q$, 4 is invertible, so $q>T^2$ already suffices. Repaired at `notes.md:19480-19489` and in `(az)`. |
| Exact equal-radicand class selection and $m_\#(C)$ | **CONFIRMED** | Equal $ck^2$ forces equal squarefree cores, hence identical activity bits, but not identical ray moduli. Definition (53.5) correctly takes the union of ray conditions for that one root pair. The $(5,2),(20,1)$ contribution is $1/8$, not $3/16$. |
| Theorem 53.1, fixed $T$ | **CONFIRMED** | The local count, omitted primes, CRT remainder, product exponent, and fixed-dimensional fundamental lemma replay. A one-slice stack gives exactly $1+2/\varphi(4ck)$, matching Theorem 52.1. Effectivity is honest for fixed $T$. |
| Total mass and (53.17) | **CONFIRMED** | The Dirichlet series has a double pole at $s=0$; its regular factor is $2C_{\rm sl}$, and Perron/Selberg–Delange contributes the factor $1/2$. An independent numerical check supports the $(\log T)^2$ shape and constant. It is explicitly record-only. |
| Exact genus distribution | **CONFIRMED** | On $C\equiv1\pmod{24}$, the $-1,2,3$ factors are pinned. Prime-power coordinates for distinct odd $q$ are independent under CRT, and each Legendre sign occupies exactly half the units. Shared conductor 4/8 parts create no dependence. |
| Lemma 53.2a | **CONFIRMED** | The $u\leftrightarrow qu$ pairing is injective, exactly one core is active, summing $k$ supplies the second logarithm, and deleting one exceptional conductor preserves a constant fraction. Conductor 8 and fixed conductor 4 are handled correctly. |
| Theorem 53.3, growing stack | **CONFIRMED-AFTER-REPAIR (applied)** | The complete quantifier chain closes. The cited fundamental lemma has the needed uniform growing-dimensional form. The old prose misstated $s=B K_T/3$; (53.25) gives $s=B K_T$. The no-exception Page branch is now logically correct, and the exact FL error is recorded at `notes.md:19825-19846`. |
| Corollary 53.4 | **CONFIRMED-AFTER-REPAIR (applied)** | The good-prime cutoff direction is correct, but the original $(\log p)^A$-to-$(\log X)^A$ sentence was not. The repair applies Theorem 53.3 with any fixed $A'<A$, for which $(\log X)^{A'}\le(\log p)^A$ on the top dyadic interval. |
| Computational 53.5 / $az)` | **CONFIRMED-AFTER-REPAIR (applied)** | All exact values replay. The overlap interval is strengthened further to `((30^2,10^5]$, containing 9,438 primes, after removing the spurious factor 4. Default and optional full scans pass. |
| Priority, cross-references, and hygiene | **CONFIRMED-AFTER-REPAIR (applied)** | Added the requested §51.9/Dahan comparison at `notes.md:19948-19954`. Repaired four eaten `\rm`/`\rho` artifacts and three malformed array row endings. Tags (53.1)–(53.39) are unique and consecutive; control-byte count is zero. |

## Severity-ranked defects

1. **Major, repaired — varying-cutoff inclusion gap in Corollary 53.4.** The old proof said asymptotic equality of $(\log p)^A$ and $(\log X)^A$ was enough. It is not: the latter box is larger, so a failure in the former need not be counted by failure in the latter. The $A'<A$ repair at `notes.md:19920-19928` restores the required containment without changing the rate shape.
2. **Major overclaim risk, repaired — growing-$\kappa$ FL was asserted rather than displayed, and $s$ was arithmetically misstated.** The exact large-$s$ error is $O(e^{9\kappa-s}K^{10})$, under $s>9\kappa+1$. The repaired proof records it and uses the actual $s=B K_T$ at `notes.md:19825-19846`. This is a citation/quantifier repair, not a theorem weakening.
3. **Moderate, repaired — empty exceptional-conductor branch was self-defeating.** “If none exists, take $r=1$” followed by retaining $r\nmid4sk$ retains no slice. The proof now deletes nothing when there is no exceptional conductor (`notes.md:19774-19798`).
4. **Moderate, repaired — false sharpness claim in Lemma 53.1a.** The factor 4 is invertible at every relevant odd prime. The valid uniform threshold is $T^2$, not $4T^2$; see `notes.md:19480-19489` and `verify.py:9445-9468`.
5. **Low, repaired — missing Dahan comparison.** Added at `notes.md:19948-19954`, with the different statistic, cubic shape, absence of genus gate, and ineffectivity all stated.
6. **Low, repaired — rendering hygiene.** Eaten backslashes had split $\rm active$, two “odd” qualifiers, “squarefree,” and $\rho_C$; table rows in (53.38) had one slash instead of two. These did not alter the intended mathematics but violated the section’s source hygiene.

No unrepaired defect remains.

## Attempted-breaks log

### Equal-radicand class-selection mismatch

Let $d=ck^2$. Since multiplication by $k^2$ does not change the squarefree kernel,

```text
sf(d)=sf(c).
```

Thus $d_1=d_2$ forces $\operatorname{sf}(c_1)=\operatorname{sf}(c_2)$, so two duplicate labels cannot disagree on activity. They can disagree on the ray modulus $h_i=4c_i k_i$, which is the actual danger. Definition (53.4) keeps all such $h_i$, while (53.5) tests whether at least one ray accepts the prime and counts the radicand once.

For $(5,2)$ and $(20,1)$, both cores are 5 and both norms are $p^2+80$. Their moduli are 40 and 80. On an active class,

```text
q == -C (mod 80)  =>  q == -C (mod 40),
```

so the ray union is the modulus-40 cylinder. Its root mass is

```text
2/phi(40)=2/16=1/8,
```

whereas raw addition gives

```text
2/phi(40)+2/phi(80)=1/8+1/16=3/16.
```

The corrected $m_\#$ passes this attack.

### Growing-$\kappa$ fundamental-lemma stress

The exact restatement of *Opera de Cribro* Theorem 6.9 used in the replay has

```text
s > 9*kappa+1,
main multiplier = 1 + O(exp(9*kappa-s) K^10),
```

with the $O$-constant absolute. Here

```text
kappa_C <= K_T = C0(1+log^2 T) = O_A(L^2),
s = log D/log z = B*K_T,
K = K0 = O(1).
```

After $C_0$ absorbs the comparison constant in $\kappa_C\ll1+m_r(C)$, choose $B>9$. For the worst class,

```text
exp(9*kappa_C-s) K0^10 <= K0^10 exp(-delta*K_T)
                         = exp(-Omega_A(L^2)).
```

This is much smaller than the final tail $\exp\{-c_A L^{3/2}/\sqrt{\log L}\}$. It does not accumulate over classes because the fundamental-lemma constant is absolute and classes are summed with their natural $X/Q_T$ main scale.

At the remainder level, with $R_T=O(T\log T)$,

```text
sum_{d<=D} mu^2(d) R_T^omega(d)
 <= D exp(O(R_T log log D)).
```

Since $T=e^{AL}$, $A<1$,

```text
R_T log log D = O(e^{AL} L^2) = o(e^L)=o(log X).
```

After summing at most $Q_T$ classes, (53.32) is $X^{1/3+o(1)}$, negligible against the claimed $X^{1-o(1)}$ bound.

### Per-class prime-count audit

No prime number theorem modulo the growing $Q_T$ is used. For each reduced hard class, the sieve starts from integers

```text
A_C={n<=X:n==C (mod Q_T)},
#(A_C)_d = X*rho_C(d)/(Q_T*d)+O(rho_C(d)).
```

The zero residue at ordinary sieve primes majorizes primality. Consequently the factor $1/\log X$ comes from the one-dimensional roughness product, not from counting primes in $C\pmod{Q_T}$. Summing the per-class main terms gives

```text
(X/Q_T) * (Q_T/(phi(Q_T) log z)) * #C_T
 = X/(phi(24) log z),
```

before averaging the genus factor, because $#C_T=\varphi(Q_T)/\varphi(24)$. This is (53.33), up to the displayed powers of $L$. There is no hidden Siegel–Walfisz or Bombieri–Vinogradov input at modulus $Q_T$.

### $q_0$ boundary stress

The proof need not extract mass from a first negative bit near $T$. It sets

```text
y=L^(3/2)*sqrt(log L)=T^o(1).
```

If no retained negative bit occurs by $y$, exact CRT independence already costs $\exp\{-c y/\log y\}$. If one occurs at $q\le y$, then for fixed $A>0$, eventually $q\le T/2$ and

```text
log(T/q)=A*L-O(log L) >= (A/2)*L,
m_r(C) >>_A L^2/q >=_A L^2/y.
```

Thus the degeneration when $q_0\asymp T$ lies wholly inside the already-paid delayed-permission branch. At the other boundary, fixed small $q_0$ gives the stronger $\gg_A L^2/q_0$ mass and does not exceed the elementary $O(L^2)$ total-mass ceiling.

### $A\to1^-$ window stress

For fixed $A=1-\varepsilon<1$,

```text
log log z = L-2 log L+O_A(1),
log log Q_T = A*L+O(1),
difference = epsilon*L-2 log L+O_A(1).
```

This is at least $\varepsilon L/2$ past an effective $A$-dependent threshold, and $Q_T<z$. The final $c_A$ can therefore shrink proportionally to this gap. The proof is not uniform when $1-A$ shrinks with $X$, and it does not claim to be. At $A=1$, both the Mertens window and $Q_T=X^{o(1)}$ mechanism fail, so the strict endpoint is necessary.

## Full theorem-53.3 quantifier chain

Fix $0<A<1$. Then choose the absolute sieve constants $C_0,B$, and take $X$ above an effective $X_A$ large enough for all following inequalities.

1. $T=(\log X)^A=e^{AL}$, $\log Q_T=O(T)$, so $Q_T=X^{o(1)}$. Also $\log z\asymp\log X/L^2$, and fixed $A<1$ gives $Q_T<z$.
2. Partition every relevant prime $p>T$ into one of the $\varphi(Q_T)/\varphi(24)$ reduced hard classes. The finitely many smaller primes are negligible.
3. Apply effective Page-deleted Siegel–Walfisz only to ray moduli $4sk\le4T$, not to $Q_T$. At most one relevant primitive real conductor $|r|\le4T$ is deleted; if none exists, delete nothing.
4. Canonical squarefree-core radicands are distinct. On root primes $Q_T<q\le z$, (53.29) gives their Mertens mass. Summing its error over $O(T\log T)$ labels is $o(1)$; quadratic local-log terms are $\exp\{-\Omega(T)\}$.
5. The local product is therefore the ordinary roughness factor $1/\log z$ times $\exp\{-m_r(C)((1-A)L+O(\log L))\}$.
6. The uniform fundamental lemma applies class by class with $\kappa_C=O(L^2)$ and $s=B K_T$. Its absolute multiplier is bounded, and the all-class elementary remainder is $X^{1/3+o(1)}$.
7. Summing classes cancels the $Q_T/\varphi(Q_T)$ and class-count factors as in (53.33); no prime equidistribution among those classes is invoked.
8. Excluding prime divisors of the possible $r$ removes only $O(L)$ independent bits. Classes with no negative retained bit through $y$ cost (53.35). Every other class has (53.36) by Lemma 53.2a.
9. Balancing $y/\log y$ with $L^3/y$ gives $y=L^{3/2}\sqrt{\log L}$ and the final $L^{3/2}/\sqrt{\log L}$ exponent. Powers of $L$ are absorbed by reducing effective $c_A$.

Every quantifier is fixed before $X$ is taken large, and every threshold after the one-conductor deletion is effective.

## Remaining claim replays

### Fixed-box sieve and single-slice specialization

For $q>T_0$, accepted root pairs for distinct radicands are disjoint and nonzero, while duplicate radicands contribute one root pair whenever at least one of their rays accepts $q$. Hence

```text
rho_C(q)=1+2*J_C(q mod Q_T).
```

Mertens in the fixed reduced classes modulo $Q_T$ gives average extra density exactly $m_\#(C)$. Small $q$, primes dividing $Q_T$, and overlap primes only alter fixed constants. With $D=X^{1/2}$, $\rho_C(d)=O_T(1)^{\omega(d)}$ makes the elementary remainder negligible. For one slice, the number of reduced lifts of $-C\pmod{4ck}$ into $Q_T$ is $\varphi(Q_T)/\varphi(4ck)$, so (53.5) gives exactly

```text
m_#=2/phi(4ck).
```

This matches Theorem 52.1, not merely up to constants.

### Selberg–Delange constant

For odd $p$, the local factor at $s=0$ is

```text
1 + p(2p-1)/(p-1)^3.
```

The 2-adic series equals 4; after dividing by $\zeta(1+s)^2$, its 2-factor contributes $4(1-1/2)^2=1$. Thus the regular factor at zero is the odd-prime product $2C_{\rm sl}$, and the double-pole partial sum is $(2C_{\rm sl})\log^2T/2$. Independently truncating the Euler product at $10^6$ gave

```text
C_sl = 0.7745656364...
```

and direct sums gave $\mathfrak M(T)/\log^2T=0.91942$ at $T=10^3$ and $0.84345$ at $T=10^6$, decreasing toward that constant. Only the elementary upper bound is used later.

### Genus bits and conductor deletion

The CRT argument is exact because each prime $q\le T$ occurs as an independent odd prime-power coordinate of $Q_T$. The conductor’s common 2-part is evaluated on $C\equiv1\pmod8$, and the 3-part on $C\equiv1\pmod3$, so neither varies. If $q$ divides the possible exceptional conductor it is omitted from the low-bit panel, not treated as random permission.

In Lemma 53.2a, $u$ is squarefree and coprime to $q$, so the pairs `\{u,qu\}` are disjoint. Equation (53.21) makes their activity signs opposite. The harmonic $k$-sum gives $\log(T/(qu))$, and the squarefree $u$-sum against $1/u$ supplies the second logarithm. For an odd prime $\ell\mid r$, restricting $\ell\nmid uk$ prevents $r\mid4sk$ whichever paired core is active. For $r=8$, taking $u,k$ odd works. Conductor 4 is fixed and has an effective zero-free gap, so it does not require Page deletion.

### Event dictionary

A good prime from (50.7) is automatically on an active slice: all prime divisors of the norm have $\chi_s(q)=1$, while $q\equiv-p\pmod{4ck}$ gives $\chi_s(q)=\chi_s(-p)=-\chi_s(p)$. Thus $\chi_s(p)=-1$. Failure of $H_{\rm SPF}(A)$ has no good prime of any size, so it is contained in the “no good prime $\le z$” event once the slice cutoff is chosen no larger than $(\log p)^A$. The repaired $A'<A$ argument ensures exactly that direction.

## Computation and hygiene

- Independent recomputation: $\operatorname{lcm}(1,\ldots,30)=2,329,089,562,800$, hence $Q_{30}=4\operatorname{lcm}(1,\ldots,30)=9,316,358,251,200$.
- The 256 random classes use local `Random(530019)` and rejection sampling from $C=1+24j$, so the sample is reproducible and uniform over reduced hard classes. The escape class is separately and explicitly $C=1$.
- The raw/corrected mass regression includes the hand-audited $3/16$-versus-$1/8$ duplicate mechanism. The $ck_{\rm pr}\le30$ histogram agrees with block `(aw)`.
- Default full `verify.py` after repairs: pass, 82.7 s wall, 333,532 KiB maximum resident set.
- Isolated `(az)` with `ES_FULL_SCAN=1` after repairs: pass, 2.5 s wall, 60,344 KiB maximum resident set; it reports the 9,438-prime overlap interval and the full 1,181-prime census.
- `notes.md` has zero control bytes. Equations (53.1)–(53.39) occur once each and in order. `git diff --check` is clean.

## Overclaim scan

- **Lemma 53.1a — “proved”:** justified after the threshold repair.
- **Theorem 53.1 — “proved, effective”:** justified; fixed-modulus Mertens/PNT constants are effective for each fixed finite $T$.
- **Corollary 53.2 — “proved”:** justified; relative zero density follows whenever $m_\#(C)>0$, and escape classes only receive the dimension-one bound.
- **(53.16) Selberg–Delange asymptotic:** justified and explicitly non-load-bearing.
- **“The genus distribution is exact”:** justified by finite CRT counting, not by sampled data or prime equidistribution.
- **Lemma 53.2a — “proved”:** justified, including one-conductor deletion.
- **Theorem 53.3 — “proved, effective”:** justified after the no-exception and FL repairs. No ineffective Siegel constant remains in a retained modulus.
- **Corollary 53.4 — “proved, effective”:** justified after the $A'<A$ repair.
- **Computational 53.5 — “exact ranges; informational”:** justified. Every finite count asserted; no asymptotic inference is made from the sample or mass bands.
- **Type-II cubic row:** still explicitly `CLAIMED/PROVISIONAL`; §53 does not claim a cubic exponent for its own Type-I statistic.
- **Scope exclusions:** the section still claims no pointwise $H_{\rm SPF}$, no conspiracy-depth bound, no parity-breaking lower bound, and no change to a §17 wall.

## Review scope signature

**Replayed fully:** Lemma 53.1a; definitions (53.3)–(53.5); Theorem 53.1 local densities, product, remainder, and single-slice specialization; genus CRT law; Lemma 53.2a and conductor cases; every quantifier and scale in Theorem 53.3; class summation; low-tail optimization; Corollary 53.4 event inclusions; `(az)` exact assertions and both scan modes.

**Structurally checked:** the standard explicit-formula derivation of Page-deleted Siegel–Walfisz and the Selberg–Delange theorem. For the load-bearing sieve citation I checked the exact large-$s$ error form, not merely a fixed-dimension paraphrase.
