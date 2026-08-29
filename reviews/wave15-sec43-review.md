# Wave 15 hostile review — §43 general numerators

**Verdict: SOUND-AFTER-REPAIRS.**  I found no surviving MAJOR or BROKEN claim.  I found two real mathematical misstatements and three proof/quantifier defects, repaired and flagged in §43: the modified-prime deletion factor before (43.26) was not always exactly \(\eta _2(m)\); the Layer-2 all-denominator cutoff made the claimed \(\delta\log x_0=o(1)\) false; the reduced-fibre quantifier was absent from Theorem 43.7; the product-modulus/character-uniformity ledgers were too compressed; and (43.10) contained a malformed token.  The repaired conclusions and stated CLAIMED/PROVISIONAL register survive.

## Scope checked

Read line by line: §16 (Lemmas 16.1–16.3, Theorems 16.4–16.5), §34 including Theorem 34.8 and §§34.4–34.5, all of §39, all of §43, `sources/pw.txt` Theorem 1.3 and §4, and `verify.py` block `(ap)`.  “Transfers/verbatim” were checked against the actual source arguments rather than accepted by analogy.

## Graded checklist

### 1. Identity — CONFIRMED

Let \(A=(k\ell+1)/m=uvw\) and \(s=(nv+u)/(k\ell)\).  On the common denominator \(nsuvw\),
\[
 \frac1{suw}+\frac1{nsvw}+\frac1{nuvw}
 =\frac{nv+u+s}{nsuvw}
 =\frac{s(k\ell+1)}{nsuvw}=\frac mn.
\]
The congruence makes \(s\in\mathbb Z_{>0}\).  If \(d\mid(A,k\ell)\), then \(d\mid mA-k\ell=1\), so \((A,k\ell)=1\); hence every factor \(v\mid A\) is invertible modulo \(k\ell\).  The class \(-uv^{-1}\pmod{k\ell}\) is therefore well-defined.  No condition on \((m,n)\), parity, or primality is used.

### 2. Pairing and multiplier mass — REPAIRED

**(a) Atom.**  CONFIRMED.  The condition is literally
\[
 muv\mid k\ell+1.
\]
It simultaneously gives \(k\ell\equiv-1\pmod m\), \(uv\mid A\), and the prime progression \(\ell\equiv-k^{-1}\pmod{muv}\).  With \((k,muv)=1\), the residue is reduced.

**(b) Lattice/BV/BT threading.**  CONFIRMED after an explicit ledger was inserted.  At fixed \(k\), Lemma 16.2 still counts only
\(u+cv\equiv0\pmod k\); the pairing does not add an \(m\)-congruence to the \((u,v)\)-lattice.  The \(m\)-condition appears only when primes are counted, in the single product modulus \(q=muv\).  It is not a CRT between independently chosen classes modulo \(m\) and \(uv\), and it is not \(\operatorname{lcm}(4uv,m)\): the old factor 4 was the old numerator and is replaced by \(m\).  If \((m,uv)>1\), common prime powers occur with their summed exponent in \(muv\).  If \(m\) is even, \(k\) and \(-k^{-1}\pmod q\) are odd.  Thus the progression remains reduced and compatible, including the ramified 2-adic cases.

For one modulus, \(uv=q/m\) is fixed and coprimality permits at most \(2^{\omega(uv)}\) ordered prime-power allocations; multiplying by at most \(K\) choices of \(k\) gives the same \(K2^{\omega(uv)}\) BV multiplicity as §16.  With \(m,K\le(\log X)^B\), \(q\le(\log X)^Bx^{1/3}\) is below the BV level.  A fixed saving enlarged by \(B\) absorbs both multiplicity and the target factor \(1/\varphi(m)\).  Brun–Titchmarsh has the same safe modulus and \(\log(x/q)\asymp\log x\).

**(c) Multiplier progression mass.**  CONFIRMED; the character-uniformity claim was clarified.  For the first weight, the unrestricted local harmonic factor is
\[
 1+\sum_{e\ge1}\frac{\varphi(p^e)}{p^{2e}}=1+\frac1p,
\]
so excluding \(p\mid m\) contributes \(p/(p+1)\), giving \(\eta _1(m)\).  For \(b(k)=(\varphi(k)/k)^2\), the local factor is
\[
 1+\sum_{e\ge1}\frac{b(p^e)}{p^e}=1+\frac{p-1}{p^2},
\]
and exclusion contributes \(p^2/(p^2+p-1)\), giving \(\eta _2(m)\).  Character orthogonality gives \(1/\varphi(m)\) in a fixed reduced class because only the principal twist has the logarithmic pole.  This is a fixed-\(m\) asymptotic only.  The proof uses the aggregate nonnegative sum over \((k,m)=1\), so no Siegel-zero-sensitive uniform equidistribution assertion is assumed.

The comparison products are correct:
\[
 \eta _1(m)\asymp\eta _2(m)\asymp\varphi(m)/m.
\]
The exact local factor \(C_2\) in (43.5) is also correct.

### 3. Layer 1 assembly — CONFIRMED

#### Load-bearing derivation A: class mass

For coprime \(u,v\), prime-power inspection gives exactly
\[
 \frac1{\varphi(muv)}=
 \frac{F_m(u)F_m(v)}{\varphi(m)uv},
 \qquad F_m(p^a)=\begin{cases}1&p\mid m,\\p/(p-1)&p\nmid m.\end{cases}
\]
The equality remains true when \((m,uv)>1\).  Since \(1\le F_m(n)\le n/\varphi(n)\), Lemma 16.2’s harmonic lower bound and weighted upper bound yield, in each dyadic prime block,
\[
 \#\text{classes}\asymp \frac{x\log x}{\varphi(m)}h(\mathcal J).
\]
Division by \(x\) and summation over \(\asymp\log X\) blocks gives
\[
 \sum_{X^{1/2}<\ell\le X}\frac{f_{m,c}(\ell)}\ell
 \asymp\frac{(\log X)^2}{\varphi(m)}h(\mathcal J),
\]
which is (43.11).  For the full family, \(h\asymp\eta _1(m)\log K\).

Deduplication is valid: a same-\(\ell\) collision has determinant of absolute value below \(\ell\), so reduced pairs agree; then \(k\equiv k'\pmod{muv}\), and \(muv>mH^2>K\) forces \(k=k'\).

#### Load-bearing derivation B: optimization

Put \(L=\log N\), \(t=\log X\), and
\(\lambda_m=\eta _1(m)/\varphi(m)\asymp1/m\).  The class mass is
\[
 \mu\asymp\lambda_m t^2\log K.
\]
The larger-sieve Rankin tail closes when
\[
 t\mu\asymp\lambda_m t^3\log K\ll L.
\]
With \(K\asymp L\),
\[
 t\asymp\left(\frac{L}{\lambda_m\log L}\right)^{1/3},
 \qquad
 \mu\asymp\lambda_m^{1/3}L^{2/3}(\log L)^{1/3},
\]
exactly the exponent in (43.13).  There is no lost \(m\), \(\varphi(m)\), or local factor.

The subsequence modulus obeys \(\log L_{m,K}\le(1+o(1))K\).  Every prime denominator above \(K\), except the finitely many primes dividing \(m\), is reduced in the required fibre.  The divisor-closed step is exact: if \(a\mid n\) and \(m/a=\sum1/x_i\), then \(m/n=\sum1/((n/a)x_i)\).  Hence an exceptional denominator has only exceptional prime factors, and Theorem 16.5’s Rankin semigroup transfer applies.

### 4. Layer 2 transfer — REPAIRED

**(i) Deduplication.**  CONFIRMED.  The \(z^2<\ell\) determinant argument is unchanged.  Once \((u,v)\) agrees, \(muv\mid k\ell+1\) determines \(k\pmod{muv}\); since \(muv>K\), it determines the admissible \(k\) uniquely.  Thus compatible atoms have distinct \(\ell\)’s and (43.18) follows by CRT.

**(ii) Shiu/residue profile.**  CONFIRMED.  The auxiliary modulus remains
\(q_0=\operatorname{lcm}(g,\operatorname{rad}k)\le k\), not a modulus containing \(m\), because \((uv,m)=1\) is not imposed.  Since \((k,m)=1\), the compatible reduced pair count is still \(\varphi(q_0)^2/\varphi(g)\).  Shiu applies with \(q_0<U^{1/10}\).  Formula (43.9) extracts \(1/\varphi(m)\), giving
\[
 W_{k,a}(g)\ll\frac{t^2}{\varphi(m)\varphi(g)}\frac{\varphi(k)^2}{k^3}.
\]
For the lower profile, replacing \(n/\varphi(n)\) by \(F_m(n)\) at \(p\mid m\) has pair-local ratio
\[
 \frac{1+2/(p-1)}{1+2p/(p-1)^2}=\frac{p^2-1}{p^2+1};
\]
its product is bounded away from zero.  Thus (43.19)–(43.20) are correct.

**(iii) Collapse versus consistency.**  REPAIRED.  The prime-power identity
\(b_y(g)/\varphi(g)=\prod_{p\mid g,p>y}p/(p-1)\) is exact, including unequal exponents.  Primes dividing \(m\) do not divide any multiplier, so they create no shared-coordinate correlation.  The original text nevertheless said deleting all \(p\mid m\) contributed *exactly* \(\eta _2(m)\).  At a conditioned prime \(p\le y\), the modified local factor is \(1+1/p\), so deletion contributes \(p/(p+1)\), not \(p^2/(p^2+p-1)\).  Since the former is smaller, the needed upper bound
\[
 \sum_{(k,m)=1}\frac{\varphi(k)^2}{k^3}q_y(k)
 \prod_{p\mid(k,R),p>y}\frac p{p-1}
 \ll\eta _2(m)\log K
\]
still follows.  §43 now states the correct mixed local product and inequality.

**(iv) Void input.**  CONFIRMED.  §43 states a genuine general-\(m\) Theorem 34.8 analogue (Theorem 43.7), including the repaired requirements \(\mathcal J\subseteq\{(k,m)=1\}\), \(1\in\mathcal J\), and \((c,L_{\mathcal J})=1\).  Lemma 34.7’s incidence square has no \(m\)-term.  Pruning loses \(o(t^2h)\), and (43.9) converts retained mass to \(\gg t^2h/\varphi(m)\).  For
\(\mathcal J_c\), the bad-coordinate variable satisfies
\[
 \Pr(Z>C\eta _1(m))\le e^{-c\eta _1(m)y},
\]
while good fibres have active mass \(\gg\eta _1(m)t^3/\varphi(m)\).  The bad tail is stronger than needed.

**(v) Bonferroni and ledger.**  CONFIRMED after the uniform cutoff repair.  The ordered moments have base
\(C\eta _2(m)t^3/\varphi(m)\le Ct^3\).  Keeping
\(r\asymp t^3\), \(y\asymp t^3\) makes the factorial tail \(e^{-ct^3}\), hence smaller than the desired \(e^{-c\eta _1t^3/\varphi(m)}\).  The exact ledger remains
\[
 \deg=O(t^3),\quad \log d_{\rm term}=O_B(t^4),\quad
 \log\sum|c_{\rm term}|=O_B(t^4).
\]
No factor \(m^r\) enters the congruence modulus: atom moduli are \(k\ell\), while \(m\) only selects atoms.  With \(\log N\ge C_0t^4\), rounding is absorbed.

#### Load-bearing derivation C: Layer-2 semigroup uniformity

The prime saving is \(\theta_mL^{3/4}\), where
\(\theta_m=\eta _1(m)/\varphi(m)\asymp1/m\), and Rankin uses
\(\delta\asymp\theta_mL^{-1/4}\).  The original cutoff
\(\log x_0=m^{1/(3/4-\epsilon/2)}\) gives, at
\(m=L^{3/4-\epsilon}\), a *positive* power of \(L\) in
\(\delta\log x_0\); the claimed \(o(1)\) was false.

The repaired cutoff invokes the prime theorem with margin \(\epsilon/4\):
\[
 \log x_0=m^{1/(3/4-\epsilon/4)}.
\]
Then
\[
 \delta\log x_0
 \ll L^{-1/4}m^{1/(3/4-\epsilon/4)-1}
 \le L^{-\epsilon^2/(3-\epsilon)}=o(1).
\]
Small primes cost only \(m^{O_\epsilon(1)}\).  Above \(x_0\),
\(m^{-1}(\log x_0)^{3/4}\) is a positive power of \(m\), so the prime-bound tail is uniformly integrable.  The polynomial small-prime cost is absorbed by
\(\theta_mL^{3/4}\gg L^\epsilon\).  Thus the all-denominator range in (43.28) survives.

### 5. Uniformity ranges — REPAIRED

Let \(L=\log N\).

| layer | denominator type | stated range | check |
|---|---|---:|---|
| 1 | primes | \(m\le L^{2-\epsilon}\) | \(t\asymp(mL/\log L)^{1/3}=o(L)\), and \(m,K\) are fixed powers of \(t\) |
| 1 | all | \(m\le L^{1-\epsilon}\) | the printed \(2-\epsilon/2\) start gives \(\delta\log x_0=o(1)\) |
| 2 | primes | \(m\le L^{3/4-\epsilon}\) | \(m\le t^{3-4\epsilon}\) for \(t\asymp L^{1/4}\), and the saving grows like \(L^\epsilon\) |
| 2 | all | same | valid only after the \(\epsilon/4\) cutoff repair above |

BV errors pay one fixed extra log-power for \(m\le t^B\); Shiu sees modulus at most \(k\), not \(mk\); the box error remains \(K^2/H=K^{-8}\); and the Layer-2 ledger absorbs \(\log m=O_B(\log t)\).  I found no omitted enumeration of \(\varphi(m)\) classes: all uniform proofs use the aggregate coprime multiplier family.

### 6. Verification block — REPAIRED

`verify.py (ap)` already checked the symbolic and exact identity for odd/even numerators and even/composite denominators, and its atom census streamed by \(\ell\)-bucket with bounded memory.  It did not explicitly assert that any tested denominator shared a factor with \(m\), and its fixed-modulus key unnecessarily included \((u,v)\), weakening that particular assertion.  I repaired it to:

- assert \((A,k\ell)=1\), \(s>0\), and nonzero coverage of \((m,n)>1\);
- deduplicate directly by `(modulus, residue)`;
- require atoms with \((m,uv)>1\), exercising the ramified product modulus;
- retain streaming same-\(\ell\) compatibility checks.

Observed block `(ap)`: 364 exact instances, 217 with \((m,n)>1\); 278 toy atoms, all 278 deduplicated/coupled; 102 atoms with \((m,uv)>1\).  Full command
`uv run --with sympy,numpy,scipy python verify.py` passed.  `ast.parse` passed.  Memory remains \(O(|\mathcal A|+30000)\), with no atom Cartesian array.

### 7. Register, PW, and crossover — CONFIRMED

PW Theorem 1.3 is transcribed accurately from `sources/pw.txt`: an absolute \(C>0\), \(4\le m\le(\log N)^2\), and the count of **all integers** \(n\le N\), not only primes or a residue class,
\[
 E_m(N)\le N\exp\{-C((\log N)^2/\varphi(m))^{1/3}\}.
\]
PW’s auxiliary \(f_m(p)\) is supported on primes \(p\equiv-1\pmod m\); those are sieve coordinates, not the denominators being counted.  Their Lemma 4.1 has mass \((\log x)^2/\varphi(m)\), and their larger-sieve choice gives exactly the displayed \(\varphi(m)^{-1/3}L^{2/3}\) exponent with no hidden \(\log\log N\).

The Layer-2/PW crossover is arithmetically correct:
\[
 \frac{\eta _1}{\varphi}L^{3/4}>
 \frac{L^{2/3}}{\varphi^{1/3}}
 \iff \varphi(m)<\eta _1(m)^{3/2}L^{1/8},
\]
up to theorem constants.  Hence Layer 2 wins for fixed \(m\), while PW wins in the larger-\(m\) regime; §43 explicitly does not claim a uniform improvement.  PW’s range extends to \(L^2\), beyond Layer 2.  Layer 1 has the extra \((\log L)^{1/3}\) multiplier gain but remains CLAIMED/PROVISIONAL.

All record-class labels remain honest: Layer 1 is internally proved only at §16’s provisional level; Layer 2 explicitly inherits Theorems 34.8/39.7; no hypothesis or provisional theorem was silently upgraded.  The malformed token and omitted quantifier were repaired rather than hidden.

## Repair disposition

- **REPAIRED:** product-modulus/even-\(m\) ledger and Shiu-modulus clarification near (43.12).
- **REPAIRED:** fixed-class character uniformity/effectivity clarification after Lemma 43.2.
- **REPAIRED:** Theorem 43.7’s reduced-fibre and multiplier-family quantifiers.
- **REPAIRED:** false “exactly \(\eta _2\)” claim before (43.26); inequality unchanged.
- **REPAIRED:** false Layer-2 \(\delta\log x_0=o(1)\) cutoff; corrected to the \(\epsilon/4\) margin.
- **REPAIRED:** `(ap)` coverage and the malformed (43.10) token.
- **MAJOR:** none.
- **BROKEN:** none.

**Final verdict: SOUND-AFTER-REPAIRS.**
