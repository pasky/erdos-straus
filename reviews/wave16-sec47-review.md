# Wave 16 hostile review: §47

**Verdict: CONFIRMED-AFTER-REPAIRS**

The refutation itself is correct.  The squarefree divisor cube consists of genuine atoms of the exact only-prime-reduced family counted by §37's conditioned `H`, and it violates both original quantified targets.  The only repairs were stale status lines in §§37, 40, 42, 45, and 46; they now point to §47 and distinguish the refuted raw targets from the open antichain repair.

## 1. Quantifier match — CONFIRMED

### Exact original statement of (40.28)

Section 40.4 first says that the atoms include **every event counted by `H`, including the tail prime atoms**.  For a **compatible ordered set `S` of distinct atoms**, it defines

$$
 \mathcal L(S)=
 \sum_{B\notin S\atop S\cup\{B\}\ {
m compatible}}
 \frac{\Pr(\bigcap_{A\in S\cup\{B\}}A\mid T_0=1)}
      {\Pr(\bigcap_{A\in S}A\mid T_0=1)}.
$$

Its exact sufficient hypothesis is:

> If, for every $|S|<m$ with $m\asymp\Lambda$, one proved
> $$\mathcal L(S)\le C\Lambda,\tag{40.28}$$
> then induction on ordered compatible tuples would give
> $\mathbb E(H)_m\le(C'\Lambda)^m$.

There is no requirement that `S` have more than one member, have a special modulus type, or be maximal.  A singleton is compatible, ordered, and consists of distinct atoms.  Since $m\asymp\Lambda\to\infty$, Theorem 47.2's $S=\{A\}$ satisfies $|S|=1<m$.  Any putative restriction that selected moduli be squarefree or pairwise coprime also admits this singleton.

### Exact original statement of (37.19)

Section 37.3 says **“Condition on $T_0=1$”**, then defines `H` in that conditioned space to count the tail prime atoms together with the retained composite family $\mathcal C^\circ$.  Proposition 37.3 states:

> Suppose there are fixed constants $C,D>0$, with $D$ sufficiently large in terms of $C$ and the constant in (37.18), and an even integer
> $$m\in[D\Lambda,D\Lambda+2],$$
> such that
> $$\mathbb E(H)_m\le(C\Lambda)^m.\tag{37.19}$$

Thus the expectation in (37.19), although its notation suppresses the conditioning, is exactly expectation under $T_0=1$.  Equation (47.11) writes that same measure explicitly as $\mathbb E((H)_m\mid T_0=1)$.  Theorem 47.2 proves failure for every fixed $C$ and every $m\asymp\Lambda$, which includes every fixed-$D$ even choice allowed by Proposition 37.3.  It therefore negates the original existential choice of constants and admissible moment order, not a stronger replacement statement.

### Conditioning identity

From (37.8), $T_0$ uses exactly the prime coordinates

$$
 z<\ell\le Y,\qquad \ell\equiv3\pmod4.
$$

Every prime in the cube lies in $(Y,2Y)$.  Hence the top atom uses no coordinate occurring in $T_0$, and CRT gives

$$
 \Pr(A\mid T_0=1)=\Pr(A)=1/M.
$$

The quarantine coordinate change is harmless: $n=P_zm$ changes $n\equiv-8\pmod{M_I}$ to $m\equiv-8P_z^{-1}\pmod{M_I}$.  Since every $M_I$ is $z$-rough and $M_I\mid M$, the inverses restrict consistently, so all event containments survive in the actual `m`-space.

## 2. Atom membership — CONFIRMED

### All applicable retention rules

The family reaching §37.3 has undergone exactly these operations:

1. **Quarantine survival:** (31.23) makes atoms with a prime factor at most $z$ impossible; the surviving moduli are $z$-rough.
2. **Event deduplication:** an intrinsic residue class is one atom even if several divisors $D\mid((M+1)/4)^2$ produce it.  Section 40.1 records this by retaining the least positive divisor in each fibre of $D\mapsto-4D\pmod M$.
3. **Prime-implied deletion (§37.3):** delete a composite atom if its projection at any prime divisor belongs to the complete intrinsic prime residue set at that prime.

There is no further composite deletion in §37.3.  In particular, §37 has not yet removed composite atoms implied by other composite atoms; that omission is exactly what §47.4 repairs.

### Lemma 18.1 supply

For odd $I$,

$$
 M_I=q\prod_{i\in I}p_i\equiv3\cdot5^{|I|}
 \equiv3\cdot5\equiv7\pmod8.
$$

Writing $a_I=(M_I+1)/4$, $M_I\equiv7\pmod8$ gives $a_I$ even.  Therefore $2\mid a_I$, hence $D=2\mid a_I^2$.  Lemma 18.1 then supplies the intrinsic class

$$
 -4D=-8\pmod{M_I}.
$$

For even $|I|$, $M_I\equiv3\pmod8$, so $a_I$ is odd and $2\nmid a_I^2$; this explains why the construction uses odd subsets.  Other classes at even subsets are irrelevant.

### Prime-implied deletion

The only prime factor of $M_I$ congruent to $3\pmod4$ is $q\equiv3\pmod8$.  Directly,

$$
 \left(\frac{-8}{q}\right)
 =\left(\frac{-1}{q}\right)\left(\frac2q\right)^3.
$$

For $q\equiv3\pmod8$,

$$
 \left(\frac{-1}{q}\right)=-1,
 \qquad
 \left(\frac2q\right)=(-1)^{(q^2-1)/8}=-1,
$$

so the product is $(-1)(-1)^3=+1$.  Lemma 21.2 says every intrinsic unit class at prime modulus $q$ has Legendre sign $-1$.  Thus $-8\pmod q$ is not a prime intrinsic class and cannot trigger deletion.

Each $p_i\equiv5\pmod8$ is $1\pmod4$.  The intrinsic system only has prime-modulus atoms at primes $\ell\equiv3\pmod4$, because all participating moduli satisfy $M\equiv3\pmod4$.  Hence there is no prime atom at any $p_i$ against which §37.3 could delete $A_I$.

### Canonical representative

In the fibre of the class $-8$, equality $-4D'\equiv-8\pmod{M_I}$ is equivalent to $D'\equiv2\pmod{M_I}$.  The only smaller positive integer is $D'=1$, which is not congruent to 2 because $M_I>1$.  Thus $D=2$ is the least positive divisor representative.  Canonical bookkeeping retains the class.

### Modulus and roughness constraints

All prime factors exceed $Y>z$, so every $M_I$ is squarefree and $z$-rough.  It is composite because nonempty odd `I` gives both $q$ and at least one $p_i$.

Put $b=\log(2Y)$ and $a=L/(3b)$.  The largest odd integer $k\le a$ obeys $a-2<k\le a$.  Since $h(L)\to\infty$ and $z<Y=L^4/h(L)<X$,

$$
 \log Y=\Theta(\log L),\qquad b=O(\log L)=o(L).
$$

Therefore

$$
 \log M\le(k+1)b\le \frac L3+b<L=\log X
$$

for all sufficiently large $X$.  Hence $M<X$, and every divisor modulus $M_I$ also satisfies $M_I<X$.

## 3. Divisor-cube logic — CONFIRMED

The number of odd subsets of a $k$-element set is $2^{k-1}$; $k$ being odd makes the full set one of them.  Thus there are

$$
 K=2^{k-1}
$$

genuine retained atoms, of which $K-1$ are proper-subset atoms relative to the top atom.

For every odd $I$,

$$
 M_I\mid M,
 \qquad
 E_A=\{n\equiv-8\pmod M\}
 \subseteq
 E_{A_I}=\{n\equiv-8\pmod{M_I}\}.
$$

Consequently

$$
 \frac{\Pr(E_A\cap E_{A_I}\mid T_0=1)}
      {\Pr(E_A\mid T_0=1)}=1.
$$

Every such extension lies in $\mathcal B_\le(\{A\})$: both shared exponents are one.  Therefore

$$
 \mathcal L(\{A\})\ge2^{k-1}-1
 =\exp\!\left(\Theta\!\left(\frac L{\log L}\right)\right),
$$

which exceeds $C\Lambda$ for every fixed $C$, since $\Lambda=L^3/\log L$ is only polynomial in $L$.  This directly falsifies (40.28).

## 4. Factorial-moment arithmetic — CONFIRMED

On the top event, all $K$ odd-subset atoms fire, so $H\ge K$.  For every $m\le K$ the falling factorial is monotone, giving

$$
 \mathbb E((H)_m\mid T_0=1)
 \ge (K)_m\Pr(A\mid T_0=1)
 =\frac{(K)_m}{M}.
$$

Here

$$
 k=\Theta\!\left(\frac L{\log L}\right),\quad
 \log K=\Theta\!\left(\frac L{\log L}\right),\quad
 m\asymp\Lambda=\frac{L^3}{\log L}.
$$

Thus $K\gg m$, and eventually $m<K/2$, so $(K)_m\ge(K/2)^m$.  For fixed $C$,

$$
\begin{aligned}
 \log\frac{(K)_m/M}{(C\Lambda)^m}
 &\ge m\log(K/2)-m\log(C\Lambda)-\log M\\
 &=\Theta\!\left(\frac{L^4}{(\log L)^2}\right)
   -O(L^3)-O(L)>0.
\end{aligned}
$$

The first term is
$(L^3/\log L)\Theta(L/\log L)$; the second is
$(L^3/\log L)O(\log L)=O(L^3)$; and $\log M<L$ from the preceding audit.  This proves the strict reverse of (37.19) at every admissible fixed-constant moment scale.

## 5. Prime supply — CONFIRMED

The cutoff satisfies

$$
 Y>z=\frac{L^3\log\log L}{\log L}\longrightarrow\infty,
 \qquad \log Y=\Theta(\log L).
$$

The prime number theorem in each fixed reduced class modulo 8 gives

$$
 \pi(2Y;8,a)-\pi(Y;8,a)\sim\frac{Y}{4\log Y}
 \quad(a=3,5).
$$

Meanwhile $k=\Theta(L/\log L)$, and

$$
 \frac{Y/\log Y}{L/\log L}=\Theta(Y/L)\to\infty.
$$

Hence there is one $q\equiv3\pmod8$ and more than enough distinct $p_i\equiv5\pmod8$ in $(Y,2Y)$.  The two congruence classes also make $q$ automatically distinct from all $p_i$.

## 6. Scope and implication repair — CONFIRMED

The section correctly does **not** claim to refute (33.16), $H_{\rm PF}'$, or the Erdős–Straus conjecture.  It refutes one sufficient factorial-moment mechanism for one unreduced count.

It also leaves (40.19) and (37.27) untouched.  For these atoms $D=2$, so $R_0(D)=2$ and $M_I=8c-1$ with $c=(M_I+1)/8$.  Every $M_I$ has at least two factors exceeding $Y$, hence $c>Y^2/8>2Y$ for large $Y$, while every incident prime is below $2Y$.  Thus every incidence is in the `j>=1` regular-progression part, not the short-cofactor endpoint.  Logical nesting can destroy high conditional codegrees without violating the aggregate pair-dispersion estimate.

The §47.4 direction is correct.  If $M_B\mid M_A$ and $r_A\equiv r_B\pmod{M_B}$, then

$$
 E_A\subseteq E_B.
$$

The antichain keeps the inclusion-maximal **events** (the coarser events) and deletes finer events contained in them.  Because the family is finite, every deleted event lies along a finite chain inside a kept maximal event.  Therefore

$$
 \bigcup_{A\in\mathcal A}E_A
 =\bigcup_{A\in\mathcal A^*}E_A,
 \qquad
 H=0\iff H_{\mathcal A^*}=0.
$$

So the kept family still detects exactly the same intrinsic exceptional-prime predicate; this is stronger than mere majorization.  The original prime-implied deletion is the prime/composite special case of this operation.  Passing to the subfamily can only improve degree, modulus, and ledger budgets, and preserves the void lower bound used by Proposition 37.3.

Equation (47.16) is a falsifiable replacement: fixed $C,D$, every large $X$, every compatible $S\subset\mathcal A^*$ with $1\le|S|<m$, and an even $m\in[D\Lambda,D\Lambda+2]$.  Together with the $O(\Lambda)$ coprime part and the already known initial mean $\mathbb EH=O(\Lambda)$, it is equivalent up to constants to the needed one-step hierarchy.  It is correctly labelled **OPEN**.

## 7. Prime-only and prime-power checks — CONFIRMED

### Proposition 47.3

Distinct compatible prime atoms cannot lie at the same prime coordinate.  A retained composite atom sharing a selected prime has, by §37.3's deletion rule, a projection outside that prime's complete intrinsic residue set, while the selected prime atom lies inside it.  They are incompatible.  Any compatible extension is therefore coprime to the selected prime moduli, and (47.8) gives $\mathcal L(S)=O(\Lambda)$.  The proof is complete.

### Equal-$7^2$ collapse

For $(539,27,431)$,

$$
 539=7^2\cdot11, \quad (539+1)/4=135,
 \quad27\mid135^2, \quad-4\cdot27\equiv431\pmod{539}.
$$

For $(1519,76,1215)$,

$$
 1519=7^2\cdot31, \quad (1519+1)/4=380,
 \quad76\mid380^2, \quad-4\cdot76\equiv1215\pmod{1519}.
$$

Both project to $39\pmod{49}$.  At 7, $\mathscr R(7)=\{3,5,6\}$, so $f(7)=3$ and $\theta_7=4$; their projection $4\pmod7$ is retained.  Their shared-level collapse is

$$
 49\frac{7-3}{7}=28.
$$

The added atom has conditioned weight
$w=7/(4\cdot1519)=1/868$, hence $28w=1/31$.  Directly, the merged modulus adds only the unshared prime 31 to 539, so the intersection-to-old-event ratio is also $1/31$.

### Higher-$7$ corner

For $(119,3,107)$,

$$
119=7\cdot17, \quad (119+1)/4=30, \quad
3\mid30^2, \quad -12\equiv107\pmod{119}.
$$

For $(539,675,534)$,

$$
675\mid135^2, \quad -2700\equiv534\pmod{539}.
$$

Both project to $2\pmod7$, outside $\mathscr R(7)$.  Adding the 539 atom to the 119 atom raises the shared exponent from $7$ to $7^2$ and adds the new prime 11.  Formula (47.5) therefore charges $1/7$ for the genuinely new base-7 digit and $1/11$ for the new coordinate, for ratio $1/77$.  Equivalently, $w_{539}=7/(4\cdot539)=1/308$ and the old shared level contributes $7\theta_7/7=4$, giving $4/308=1/77$.

`verify.py (at)` checks retention, CRT compatibility, both exact ratios, the collapse 28, and a finite four-atom divisor cube.  The full required command

```text
uv run --with sympy,numpy,scipy python verify.py
```

completed successfully; every block through `(au)` passed.

## 8. Status/register sweep — REPAIRED

Stale lines in Proposition 37.3's aftermath, Assessment 37.5, §40.4/Assessment 40.8, §42's headline/Assessment 42.7, Assessment 45.8, and Assessment 46.8 still treated (40.28) or raw-`H` (37.19) as open.  They now explicitly point to §47, state that those literal targets are refuted, and keep (40.19), (37.27), (40.29), (47.16), (33.16), and $H_{\rm PF}'$ open as appropriate.  Every change is marked `(wave-16 review repair)`.

## Final disposition

| Check | Grade |
|---|---|
| 1. Quantifier match and conditioned space | CONFIRMED |
| 2. Atom membership and all retention rules | CONFIRMED |
| 3. Divisor-cube containment/count | CONFIRMED |
| 4. Factorial-moment arithmetic | CONFIRMED |
| 5. PNT supply and scale | CONFIRMED |
| 6. Scope and antichain repair | CONFIRMED |
| 7. Proposition 47.3, prime powers, verification | CONFIRMED |
| 8. Status-line sweep | REPAIRED |

**REFUTATION CONFIRMED.**  The repository verdict is `CONFIRMED-AFTER-REPAIRS` only because stale status text required repair; no mathematical repair to Theorem 47.2 was needed.
