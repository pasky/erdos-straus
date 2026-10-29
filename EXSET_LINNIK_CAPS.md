# EXSET_LINNIK_CAPS — wave z51, lane 2b (`lcaps`)

**Status: COMPLETE — T2-lite reached; T2-full not reached. ES remains OPEN.**
All proofs here are internal and unrefereed. Four hostile Opus rounds returned SOUND
with minor repairs, all incorporated. This lane follows z48–z51 CONTEXT, with z51 binding.
Committed on `side-agent/z51-lcaps`; WAITING for parent approval, no merge.

**Main result (PROVED relative to Gallagher and Montgomery).** For every ε>0,
cap ⌈(log log X)^{1+ε}⌉ suffices outside O_ε(X^{1−c_ε}) primes, with c_ε>0 (§4.2).
It uses a common set of O_ε(log log X/log log log X) mute primes, each O_ε(log log X).
The cap-zero case is not proved. The strict Linnik route separately improves the old
X^{2/A+o(1)} bound to X^{1/A+o(1)} at cap (log X)^A/4, A>1 (§2).

## 0. Outcome and review ledger

| Round | Target | Status | Hostile Opus review |
|---|---|---|---|
| 1 | Quadratic large sieve: cap log^A X, exceptional exponent 1/A, A>1 | PROVED (known analytic technique, new cap application) | SOUND; minors repaired |
| 2 | Weighted squareclass endpoint; full fixed-window sharpness | PROVED; infinitude uses Dickson | SOUND; scope/terminology repaired |
| 3 | Cap (log log X)^{1+ε}, common small mute support, power saving | PROVED relative to Gallagher + arithmetic large sieve | SOUND; minors repaired |
| 4 | EMV logarithmic endpoint (subpower); prime census through 10⁸ | PROVED relative to MV; CERTIFIED census | SOUND; source constant repaired |

## 1. Definitions, inherited facts, and non-CRT input

**Definitions.** ES^{(y,e)}(n) means 4/n=1/x+1/y+1/z with x,y positive integers,
z positive rational, reduced denominator den(z)=r², r odd, (r,n)=1, rad(r)|y,
and v_s(r)≤e. The y in this notation is a denominator, not a smoothness parameter.
Write e*(n) for the least such e; e*=0 is exactly ES. Below Y denotes a smoothness cutoff.

For p≡1 (8), let q₃(p) be the least prime q≡3 (4) with (q/p)=−1. Write
E(X,Y)={p≤X prime: p≡1 (8), (q/p)=1 for every prime q≤Y, q≡3 (4)}.
These p cannot equal a generating q, since their classes modulo 4 differ.

**Inherited PROVED input, not a new claim.** `CAP_DOWN` Theorem 1.2 and Proposition 1.3
produce a Type II-shaped capped solution at each such q. Put K=(p+q)/4 and choose an odd
prime s with b=v_s(K) odd and (s/q)=−1. Such s exists for p≡1 (8), including even K.
With j=ord_q(s)/2 (odd), d=Ks^j and A=(K+d)/q,

    (x,y,z)=(K,pA,pKA/d),   cap=max(0,(j−b)/2)≤(q−3)/4.          (1.1)

All overflow is at **one odd prime s**. The excluded 2-adic windows for p≡5 (8) are not
used: those p already satisfy classical ES. Therefore

    {p≤X:e*(p)>e} ⊆ E(X,4e+3).                                (1.2)

This is an implication, not an equivalence. Global e* is zero throughout the verified
prime range, so informative numerical quantities are q₃ and *restricted-window* caps.

**Non-CRT input.** Heath-Brown, “A mean value estimate for real character sums”,
Acta Arith. 72 (1995), 235–275, Theorem 1 / Corollary 1, gives for every η>0

    Σ_{m≤X, m odd squarefree} |Σ_{a≤N, a odd squarefree} c_a(a/m)|²
       ≪_η (XN)^η(X+N) Σ_a |c_a|².                            (HB)

Primary PDF checked: https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf, pp. 237–238.
Both squarefreeness restrictions are essential. The prime p is a **row modulus**;
this is not an integer-avoider CRT evaluation, so z51 G1 and the square floor do not cap it.
No claimed strengthening of HB is used. For nonsquarefree columns its Corollary 2
has the square-class energy Σ_{ab=square}|c_a c_b|, not the ordinary ℓ² norm.

**Literature check (Assessment, limited search).** A fresh search for 2026 ES exceptional-set
improvements found no replacement for the published Vaughan bound. Pomerance–Weingartner,
https://arxiv.org/html/2511.16817v2, introduction and Theorem 1.3, still cite Vaughan;
this is not a proof that no later result exists. Liu, https://arxiv.org/html/2505.09637v1,
restates HB with its square-class energy and gives an explicit variant. No new theorem
from that preprint is needed. Retrieved text is in `data/z51_lcaps/literature_*.txt`.

## 2. Round 1: confinement and the quadratic large sieve

### Theorem 2.1 — quadratic Linnik confinement (PROVED relative to HB)

Let S be any set of odd primes, all ≤Y, and let E be odd primes p≤X, p∉S, such that
(q/p)=1 for every q∈S. Let B_S(N) be the number of squarefree positive integers ≤N
supported on S (including 1). For every η>0,

    |E| ≪_η (XN)^η (X+N)/B_S(N).                              (2.1)

**Proof.** Take c_a=1 on these squarefree integers and zero elsewhere in HB. Each row
p∈E has inner sum exactly B_S(N), since every factor is a unit quadratic residue.
Its squared contribution is B_S(N)², while the coefficient norm is B_S(N). Drop every
other nonnegative row and divide. ∎

### Corollary 2.2 — cap threshold log^{1+ε}, exponent 1/A (PROVED)

For every fixed A>1,

    #E(X,(log X)^A) ≤ X^{1/A+o(1)},
    #{p≤X:e*(p)>(log X)^A/4} ≤ X^{1/A+o(1)}.                  (2.2)

The meaning of o(1) is: for every δ>0 the bound is O_{A,δ}(X^{1/A+δ}).
No effective uniform dependence of the HB constant on δ is asserted.

**Proof.** Let L=log X, Y=L^A, k=π(Y;4,3) and r=⌊L/log Y⌋. The products of r distinct
primes q≤Y, q≡3 (4), are ≤X and distinct. By the fixed-modulus PNT,

    B_S(X) ≥ binom(k,r) ≥ (k/r)^r,
    log(k/r)=(A−1)log L+O_A(1),
    log B_S(X) ≥ (1−1/A)L−o(L).

Apply (2.1) with N=X, then take any fixed η arbitrarily small. Equation (1.2) transfers
the result to caps. This halves the old exponent 2/A and gives a fixed power saving
for every A>1, not just A>2. No improvement in the pointwise cap identity is required. ∎

### Corollary 2.3 — one overflowing prime and a short window (PROVED)

Outside at most X^{1/A+o(1)} primes p≡1 (8), a solution exists with

    x=(p+q)/4,  q≤(log X)^A prime, q≡3 (4),
    den(z)=s^{2h},  s odd prime dividing x,  0≤h≤(q−3)/4.

Allow den(z)=1 when h=0. This is the actual witness (1.1), not merely a statement
about e*. Thus the improvement still holds after simultaneously imposing a polylog
window and **at most one p-dependent mute prime**. Its relation to ES is discussed
in §4; s is not a fixed prime independent of p.

**Independent checks.** `scripts/z51_lcaps_toy.py` compares the squarefree-product set
with an independent factorization enumeration, checks every confined character sum,
and checks the binomial construction. The analytic constant in HB is unspecified;
a finite calculation cannot certify its asymptotic inequality. The first toy rows had no
confined primes; Opus identified this vacuity, and the retained rows now assert nonempty E.

**Round-1 Opus verdict: SOUND, minor repairs applied.** Reviewer independently rebuilt
4466 exact rational witnesses for p≡1 (8), p≤200000, with zero violations. The tool rejects
`:high` as part of a model ID; the actual review used `anthropic/claude-opus-5-5`, `mode=deep`.
Session: `2026-10-29T22-39-32-614Z_01a189d1-8706-70d6-863f-0bde7e771866.jsonl`.

**Novelty qualification (Assessment).** HB smooth-product amplification is a known
least-nonresidue technique (Baier 2006, also discussed by Lau–Wu 2008); the analytic
argument is not new. What is added here is its complete restricted-prime adaptation,
the cap exponent 1/A, and the simultaneous one-mute/short-window conclusion. This
strengthens CAP_BOUNDED; CAP_INTERPOLATION already sketched the A>1 range by a different
method. Neither the existing sketch nor (2.2) establishes a power saving at A=1.

### Proposition 2.4 — Elliott–Montgomery–Vaughan at the logarithmic endpoint

**PROVED relative to Montgomery–Vaughan Lemma 2, via Lau–Wu's reproduced proof.**

For an absolute c>0,

    #E(X,2log X) ≪ X exp(−c log X/log log X).                   (2.3)

Consequently the one-mute-prime, short-window conclusion of Corollary 2.3 holds with
q≤2log X, cap≤(log X)/2, outside this **subpower**, not power-saving, exceptional set.
This is weaker than Theorem 4.2 for global caps but uses only one mute prime.

**Input and adaptation.** Lau–Wu, “On the least quadratic non-residue”, IJNT 4 (2008),
pp. 423–435, Lemma 2.1, https://hkumath.hku.hk/~yklau/p/34.pdf, prove from the
Elliott–Montgomery–Vaughan large sieve that, for every subset V of primes in (P,2P],

    Σ_{d fundamental, |d|≤X}|Σ_{q∈V}χ_d(q)/q|^{2j}
       ≪ X[6j/(P log P)]^j + [36P/(log P)²]^j.                (EMV)

Their statement uses all primes; the identical proof permits a subset: coefficients
of (Σ_{q∈V}χ_d(q)/q)^j remain nonnegative, and both sums Σq^{−2} and Σq^{−1/2} in
their proof only decrease. More explicitly, the convolution over m₁m₂=n² equals
b_{2j}(n²), where b_j counts ordered V-prime products; for a V-supported n,
b_{2j}(n²)≤j^j b_j(n), exactly as in their proof. The absolute implied constant is
uniform in j,P,X. We use 36, not the printed 6, in the second term: squaring their
bound Σq^{−1/2}≤6√P/log P requires 36. This harmless source arithmetic typo was found
by the round-4 reviewer.
This citation-level analytic input, not a new large-sieve theorem, is essential.

**Proof.** Put P=log X, V={q∈(P,2P]:q≡3 (4)}. For p∈E(X,2P), p>√X, none of these q
ramifies and their sum is Σ_{q∈V}1/q≥1/(4log P) by the fixed-AP PNT. Here χ_p(q)=(q/p)
since p≡1 (4), and p is a fundamental discriminant. Thus (EMV) gives

    #E(X,2P) ≤√X+O(X[96j log P/P]^j+(576P)^j).

Take j=⌊log X/(384log P)⌋. The first bracket is ≤1/4 and the second term is ≤X^{1/192}
for sufficiently large X. This proves (2.3). Equation (1.1) gives the witness claim. ∎

**Literature audit correction.** The Lau–Wu introduction explicitly credits Baier's
HB improvement from exponent 2+ε to 1+ε and distinguishes the logarithmic endpoint.
Their bound is subpower. We inspected their actual moment proof rather than assuming
their all-prime confinement hypothesis contained our restricted q≡3 (4) event.
The subset adaptation above is the needed additional step. The retrieved text is the
authors' preprint; published bibliographic data are IJNT 4(3), 423–435 (2008), but the
published typeset proof and the original MV Lemma 2 were not independently retrieved.

**Round-4 Opus verdict on Proposition 2.4: SOUND, minor repairs applied.** The constant
36/576 and the subset convolution detail above incorporate its corrections.

## 3. Round 2: the forcing threshold and its exact scope

### Theorem 3.1 — exact square-class budget of the amplifier (PROVED)

Let S⊆{primes≤Y}. Allow arbitrary nonnegative coefficients c_n supported on integers
n≤N whose squarefree parts (cores d in n=dv²) belong to the multiplicative squareclass span of S;
arbitrary square multipliers and repeated prime factors are allowed. Put

    H=Σ_n c_n,   J=Σ_{ab=square}c_a c_b.

Then H²/J≤B_S(N), where B_S(N) counts squarefree kernels ≤N supported on S (here and below “kernel” means this core, not rad(n)). Equality
is attainable by assigning equal total weight to every available kernel. Consequently
HB Corollary 2 with a guaranteed sum H cannot improve the bound (X+N)/B_S(N), apart
from its (XN)^η factor, by adding prime powers, squares or nonnegative weights.

**Proof.** Group coefficients by kernel d: w_d=Σ_{n=dv²}c_n. Then J=Σ_d w_d² and
H=Σ_d w_d. Cauchy gives H²≤#{d:w_d≠0}J≤B_S(N)J; take only n=d with equal weights
for equality. If some row has a common factor with a square multiplier, its sum may
be smaller than H, never larger; this cannot improve a guaranteed lower bound. ∎

If Y=(log X)^{1+o(1)}, then **uniformly for every N≥1**,

    (X+N)/B_S(N) ≥ X^{1−o(1)}.                               (3.1)

Thus this common-positive smooth-squareclass amplifier cannot prove a fixed power
saving at Y=log X·(log log X)^C for any fixed C, even using *all* primes ≤Y, arbitrary
lengths, square multipliers and optimized weights. This is a limitation of this
specific HB estimate, not a lower bound on the exceptional set.

**Proof of (3.1).** For any fixed 0<t<1, Rankin gives

    B_S(N)≤N^t ∏_{q≤Y}(1+q^{−t})
           ≤N^t exp(O_t(Y^{1−t})) =N^t X^{o(1)}.

The minimum of (X+N)/N^t over real N>0 is c_t X^{1−t}; the product bound is independent
of N. Take any fixed t arbitrarily small. Conversely, for Y=(log X)^A, A>1, §2 gives
a power saving. In the fixed logarithmic-exponent scale the boundary of this
amplifier is therefore exactly A=1. No claim is made about arbitrary signed amplifiers,
Elliott-type estimates, or profiles not confined to a common smooth squareclass span.
The known condition (2/p)=1 adds at most a factor two to the kernel budget.

### Theorem 3.2 — full-window sharpness

**PROVED algebra; infinitude CONDITIONAL on Dickson.**

Fix a prime q≡3 (8), q≥11. Let s be an odd prime primitive modulo q, put p=4s−q,
and suppose p is prime, p>q. Let c_q(p) be the least cap of **any** ES^{(y,e)}(p)
solution with x=s, including the δ_p=±1 families of CAP_DOWN Lemma 3.1. Then

    c_q(p)=0                if p≡−1 (mod q),
    c_q(p)=(q−3)/4         otherwise.                         (3.2)

For each such q, Dickson implies infinitely many primes p in the second case.
This extends CAP_DOWN Proposition 4.1(a), whose sharpness statement excludes δ_p≠0.

**Proof.** The full fixed-x dictionary permits precisely

    s^δ p^ε ≡−1 (mod q),  ε∈{−1,0,1},
    δ∈{−1,0,1}∪{3,5,…,2e+1}.

There is no 2-coordinate since x=s is odd; p and s are distinct. Write q−1=2h,
h odd, and 4=s^a mod q, where a is even. Then
δ+ε≡h−aε (mod 2h). If ε=±1, δ must be even, hence δ=0, and this case works exactly
when p≡−1 mod q. If ε=0, δ≡h mod 2h: since h≥5 its first permitted representative
is h, giving e=(h−1)/2=(q−3)/4. This also proves the first case via δ=0, ε=1.

Choose a primitive residue g≠−4^{−1} mod q (there are at least four primitive residues).
Choose an odd positive a₀≡g mod q and consider s=a₀+2qt, p=4a₀−q+8qt.
The two distinct linear forms are admissible: modulo 2 and q they never vanish;
modulo any other prime ℓ≥3 at most two residues are roots. Dickson supplies infinitely
many simultaneous primes. They have p≡1 (8), p≢−1 (q), so (3.2) applies. ∎

**Exact interpretation.** With only a nonresidue bit at a single q and no factorization
information, cap (q−3)/4 is genuinely needed for some full fixed-x problems. At lower
caps the bit (q/p)=−1 need not force a solution **at that q**. Globally, however,
(1.2) remains true at *every* e≥0; it never “ceases to be pointwise-forced”. Its
confinement cutoff simply shrinks to 4e+3. A theorem that it fails globally beyond
that cutoff would require an actual cap/ES counterexample and is not claimed.
Local sharpness is proved only for q≡3 (8), q≥11; even-K windows q≡7 (8) are not addressed.
An exact universal global stopping threshold, as literally asked in the brief, is
therefore not established. Other windows may solve p with cap zero (and do in our
entire census). This local theorem must not be advertised as a barrier for global ES.

**Round-2 Opus verdict: SOUND, minor terminology/scope repairs applied.** The retained
script enumerates the known fixed-x dictionary and rebuilds exact rationals; it does
not independently prove that dictionary. 850 cases pass (74 cap-zero, 776 sharp-positive).
Opus independently tested the definition with extra 2- and p-powers on 1350 cases,
all matching (3.2). Session: `2026-10-29T22-46-32-054Z_01a189d7-ed76-70d6-863f-0be3a0a4cd2b.jsonl`.
The cap-zero branch is possible only if −4^{−1} is primitive modulo q; otherwise every
admissible pair is sharp. The exact q-by-q restriction is part of the theorem.

## 4. Round 3: intermediate relaxations and further attacks

The smooth-character amplifier stops at §3.1, but the cap problem need not. We now
change methods: keep the **untruncated** classes of CAP_INTERPOLATION Proposition 5.1,
and use a growing, common set of small mute primes. This is a cap-specific class sieve,
not Linnik confinement; the class supply exceeds the cap-zero ES supply. Therefore
there is no conflict with z50's CRT barrier for ES.

### Lemma 4.1 — a collision-free exponent box at many primes (PROVED relative to G)

Let k≥1 and E≥1, let P₀ be the product of the first k+1 odd primes, and B=(E+1)^k.
Fix an absolute sufficiently large integer D (including D≥1/b for Gallagher's range).
For parameters with P₀ sufficiently large and log(4P₀)≥√log(2T), where

    T=⌈[4P₀ B²(E+1) log(4P₀)]^D⌉,                           (4.1)

one can select k of these k+1 primes, with product P, so that at least

    M ≥ c T/[φ(4P)log T]                                    (4.2)

primes ℓ∈(T,2T], ℓ≡−1 (4P), have the B numbers

    Q_a² mod ℓ,  Q_a=∏_{s|P}s^{a_s},  0≤a_s≤E,

pairwise distinct. The growing parameters in Theorem 4.2 satisfy these hypotheses.
No uniform statement for fixed k and arbitrarily large E is asserted by this lemma.
Here T is the prime scale, and Q_G=4P₀ is the modulus cutoff (called T in the inherited
statement of G); Gallagher's exceptional zero is defined relative to Q_G.

**Proof.** Use the Gallagher input (G) recorded and source-audited in
CAP_INTERPOLATION §1, at x=T, modulus cutoff 4P₀. It gives relative PNT in this
progression with error <1/4 if D is sufficiently large, except when the exceptional
primitive real conductor f divides 4P. If f has an odd prime divisor in P₀, omit that
prime; otherwise omit any prime. Then f∤4P. A pure 2-power primitive real conductor
is 4 or 8 and is not exceptional for sufficiently large cutoff. Thus the progression
has ≥c₀T/[φ(4P)log T] primes. This uses the same exceptional-prime deletion as
CAP_INTERPOLATION Proposition 1.2; P is common to all input primes p at a given X.

If Q_a²≡Q_b² (ℓ) for a≠b, ℓ divides the nonzero integer Q_a²−Q_b². Unique factorization
ensures it is nonzero and log|Q_a²−Q_b²|≤2E log P. Hence the number of bad primes in
(T,2T] is at most

    B(B−1)E log P/log T.

By (4.1), this is o(T/[φ(4P)log T]) in the growing regime (and can be made less than
half the main term by enlarging the absolute constant). Subtract them to get (4.2). ∎

**Certificate check (inherited dictionary).** Each of these B distinct classes
p≡−4Q_a² (ℓ) certifies cap max_s(0,a_s−v_s(A_ℓ))≤E−1, hence certainly ≤E, with all denominator
primes among the k primes of P.
Indeed write A_ℓ=(ℓ+1)/4, D_a=Q_a², V=(p+4D_a)/ℓ, and

    x=(p+V)/4,  y=pA_ℓ,  z=pxA_ℓ/D_a.                        (4.3)

Since P|A_ℓ, v_s(D_a)=2a_s≤2v_s(A_ℓ)+2E, exactly the condition of
CAP_INTERPOLATION Proposition 5.1. Exclude the finitely many p|P; a hit automatically
has p≠ℓ. All classes are nonresidues mod ℓ, so odd squares are never hit.
**No bound D_a<ℓ/4 is imposed.** That truncation would destroy the argument.

### Theorem 4.2 — cap (log log X)^{1+ε} with a power-saving exceptional set

**PROVED relative to G and Montgomery's arithmetic large sieve.**

For every fixed ε>0 there exists c_ε>0 such that, for large X,

    #{p≤X:e*(p)>⌈(log log X)^{1+ε}⌉} ≪_ε X^{1−c_ε}.          (4.4)

More strongly, one common set S_X of

    k=⌊(2/ε) log log X / log log log X⌋

odd primes, each O_ε(log log X), suffices for all the nonexceptional p. Their solutions
(4.3) have rad(den z)⊆S_X, exponent cap E=⌈(log log X)^{1+ε}⌉, and
ℓ≤(log X)^{O_ε(1)}. Constants are not evaluated; the theorem is asymptotic.

**Proof.** Put L=log X, λ=log L, a=2/ε, k=⌊aλ/log λ⌋ and E=⌈λ^{1+ε}⌉.
Prime-number estimates for the first k+1 primes give

    log P₀=(a+o(1))λ,  log B=(a(1+ε)+o(1))λ,
    log T=(H+o(1))λ,  H=D a(3+2ε).                           (4.5)

Consequently the Gallagher range required in Lemma 4.1 holds. There are M good primes,
each with B forbidden classes. Set r=⌊L/(2log(2T))⌋. Then every product of r distinct
good primes is ≤√X, and M≫r, since log M=(H−a+o(1))λ while log r=(1+o(1))λ;
take D large enough that H−a>1.

Montgomery's sieve for the exceptional inputs p∤P gives |E_bad|≤2X/𝓛, where

    𝓛≥binom(M,r)(B/(2T))^r
      ≥[cB/(rφ(4P)log T)]^r.                                (4.6)

Here B/(ℓ−B)≥B/ℓ≥B/(2T), and binom(M,r)≥(M/r)^r. No independence assumption or
repeated-prime approximation is hidden in this step. Because φ(4P)≤4P₀,

    log[cB/(rφ(4P)log T)] ≥ (aε−1+o(1))λ=(1+o(1))λ.

It follows that log𝓛≥(1/(2H)+o(1))L. Thus any fixed c_ε<1/(2H), for example
1/(4H), works after absorbing the p|P exceptions and constants. Primes not ≡1 (8)
already have cap zero. All representatives Q_a and the sieving primes are independent
of the input p; the exact dictionary supplies genuine solutions at every class hit. ∎

**What is new (Assessment).** CAP_INTERPOLATION Remark 3.2(b) used one fixed base and
sketched a power saving at E≥log^{1+ε}X. A fixed k-base version already gives the
threshold E≥log^{(1+ε)/k}X. The growing box and exceptional-prime deletion here lower
it further to E≥(log log X)^{1+ε}, while keeping a fixed power saving. This statement
is not claimed in the inherited CAP documents. It is a CRT theorem for a relaxation,
not a depth-breaking ES theorem; its novelty is the untruncated growing-rank count.

### Relationship of the relaxations (PROVED inclusions; Assessment of distance)

Let R_{S,E}(p) mean ES^{(y,E)} with the additional restriction rad(den z)⊆S (no window
or y restriction in its definition). Then

    ES(p) ⇒ R_{S,E}(p) ⇒ ES^{(y,E)}(p),  R_{S,0}(p) ⇔ ES(p).

Thus (4.4) proves an actual intermediate relaxation, not just a differently restricted
search: a common extremely small alphabet of mute primes suffices with a small cap.
The theorem also supplies the optional shot shape (4.3). Imposing that shape in the
*definition* would make its cap-zero version only PM-II, not all ES; we do not conflate them.

Separately define R^{one}_{E}(p) by allowing den z=1 or s^{2h}, one arbitrary odd prime
s, h≤E, s|y, s∤p. It too lies between ES and the cap relaxation. Corollary 2.3 proves
a power saving for R^{one}_{(log X)^A/4}, A>1, plus a short window. The two positive
results trade a smaller cap against a smaller mute support: (4.4) does **not** guarantee
one mute prime, and (2.3) does **not** guarantee a common mute prime. At E=0 both become
ES and neither proof survives. In the growing-box proof B=1 at E=0; the supply gain
is precisely non-integrality, not an extra hidden ES dimension.

**Further attack (Assessment, not a universal barrier).** Keeping this particular
collision-free box proof, a fixed power saving needs log B−log P−log log X to be a
positive fraction of log T, with log T≥2log B+log P. For E=λ^{1+o(1)} and
k log(E+1)=O(λ), log B−log P=o(λ) (or negative) in the useful k range, so these
parameters cannot reach E=λ or bounded E with fixed power saving. This is bookkeeping
for this construction, not a theorem that the full untruncated class sieve stops there.
Joint character confinement is not needed for (4.4), so §3.1 does not contradict it.

**Round-3 Opus verdict: SOUND.** The reviewer checked Gallagher's primary theorem OCR
(`data/r237/gallagher1970_thm7_ocr.txt`), the omission order, all asymptotic exponents,
and the exact dictionary. Quantifier and notation minors are repaired above. Its
independent checks rebuilt 3000 certificates (D/ℓ up to 9·10³⁷), found five genuine
collision primes, checked a toy Montgomery bound and tested parameter convergence.
The latter is slow: no practical numerical threshold for (4.4) is claimed.
Session: `2026-10-29T22-53-41-000Z_01a189de-7908-70d6-863f-0be64ee208ec.jsonl`.
Our retained test now includes actual collisions, rather than only collision-free rows.

## 5. Computation and controls

### Full census (CERTIFIED finite computation)

The range contains 5,761,455 primes, 2,880,504 in 1 mod 4, and **1,439,970 in 1 mod 8**.
The nonclassical statistics below concern the latter set. All other primes are handled
by the inherited classical ES identities; no artificial q₃ forcing at p≡5 (8) is used.

| Statistic on p≡1 (8), p≤10⁸ | Result | A maximizing prime |
|---|---:|---:|
| Least prime q₃≡3 (4), (q₃/p)=−1 | max 151 | 52,373,017 |
| Best explicit one-prime cap (1.1) at q₃ | max 37 | 52,373,017 |
| Exact Type II cap at the q₃ window | max 24 | 51,760,129 (q₃=103) |
| Exact full fixed-x cap at q₃, δ_p=±1 included | max 24 | 51,760,129 |
| Least cap-zero Type II window m≡3 (4), m≤255 | max 107 | 8,803,369 |
| Primes censored by the window cutoff 255 | **0** | — |

At the least q₃ window, 1,366,823 Type II caps and 1,383,310 full caps are zero.
The explicit one-prime witness has cap zero at 892,207 primes. The q₃ distribution
starts 720,189 at 3; 360,313 at 7; 180,095 at 11; 90,141 at 19, and has one prime at 151.
Complete histograms and record/sample rows are in `census_1e8.json` and `sample_1e8.csv`.
The all-window result certifies e*(p)=0 for these primes; **no positive restricted cap
is evidence for a positive global cap or an ES failure**.

### Independent checks and controls (CERTIFIED)

- `z51_lcaps_census.cpp`: byte sieve, SPF factorization, min–max residue convolution
  over all admissible local exponents; full fixed-x targets include p^{±1}.
- `z51_lcaps_independent.cpp`: retained Opus implementation, trial division, direct
  Jacobi q₃ tests, reachable-residue sets recomputed successively for e=0,1,….
  All five histograms match at **every prime through 10⁸**, not merely a sample.
- `z51_lcaps_verify.py`: a third full prime/q₃ census in Python; compares both engines'
  complete histograms; independently checks 583 retained cap rows and exact one-prime
  rational witnesses, and enumerates actual divisors for the least-window checks.
  Its cap search uses the inherited dictionary; it does not independently prove it.
- The Opus reviewer additionally enumerated unrestricted local exponents, including
  forbidden 2- and p-overflows, on these 583 rows: 1166 minimum-cap checks, no skips.
- All nine requested hard primes and all 14 R-zeros appear exactly once (18 distinct
  primes after overlap); the retained verifier asserts their presence. In particular
  3361 has q₃=11, restricted cap 1, but cap zero at m=3; 66529 has Type II cap 1 versus
  full cap 0 at q₃=19. The R-zero 8813281 has cap zero at m=3.
- Fifty odd squares ≤10201 have no admissible cap-zero Type II window m≤255 and no
  nonresidue forcing prime q≤151 coprime to the square. The all-cap exclusion is the
  inherited T1 theorem, not inferred from this finite test.
- Exhaustive sorted-denominator tests recheck **8/17 and 8/241 fail**, while 4/17 and
  4/241 succeed. Our claims concern capped numerator 4 and average exceptional sets;
  neither the 4-specific identity nor an average bound proves ES for numerator 8.

`toy.json` verifies nonempty confined rows, squarefree product counts and EMV subset
moment expansion/diagonal bounds. `threshold.json` has 850 exact full-window checks.
`boxes.json` rebuilds 600 untruncated certificates and includes four genuinely bad
collision primes (30 colliding pairs), plus an exact toy Montgomery denominator.
The asymptotic constants in HB/G/EMV are not numerically certified by these tests.

**Round-4 Opus census verdict: SOUND.** It reproduced both the entire character
histogram and all cap/window histograms independently, checked the exponent rules,
and verified the exact definition on the sample. Its session is
`2026-10-29T23-08-06-004Z_01a189eb-abf4-70d6-863f-0beb56a0bc76.jsonl`.
The independent full-range code is now retained rather than only living in /tmp.

### Reproduction and resource bounds

All scripts/data are under `scripts/z51_lcaps_*` and `data/z51_lcaps/` (well below 20 MB).
Peak measured memory: original census about 201 MB, Python verification about 213 MB;
no unbounded pair-product arrays. The displayed commands include explicit timeouts.

```sh
ulimit -v 8000000
timeout 30 g++ -O3 -std=c++17 -Wall -Wextra -Werror scripts/z51_lcaps_census.cpp -o /tmp/z51_lcaps_census
timeout 30 g++ -O3 -std=c++17 -Wall -Wextra -Werror scripts/z51_lcaps_independent.cpp -o /tmp/z51_lcaps_independent
timeout 360 /tmp/z51_lcaps_census 100000000 data/z51_lcaps/sample_1e8.csv > data/z51_lcaps/census_1e8.json
timeout 240 /tmp/z51_lcaps_independent 100000000 > data/z51_lcaps/independent_1e8.txt
timeout 180 uv run scripts/z51_lcaps_verify.py > data/z51_lcaps/verify_1e8.json
timeout 60 uv run scripts/z51_lcaps_toy.py > data/z51_lcaps/toy.json
timeout 120 uv run scripts/z51_lcaps_threshold.py > data/z51_lcaps/threshold.json
timeout 60 uv run scripts/z51_lcaps_boxes.py > data/z51_lcaps/boxes.json
```

## 6. Final assessment and exact remaining gap

**PROVED — T2-lite, strongest retained theorem.** Theorem 4.2 gives

    #{p≤X:e*(p)>⌈(log log X)^{1+ε}⌉} ≪_ε X^{1−c_ε},  c_ε>0,

with a common tiny mute-prime alphabet. This goes well below both CAP_BOUNDED's
log^{2+ε} threshold and CAP_INTERPOLATION's log^{1+ε} sketch. Its ingredients are the
untruncated cap dictionary, elementary collision counting, Gallagher's exceptional
conductor deletion, and the arithmetic large sieve. No GRH, OAI-003, or new conjecture
is used. **This is a cap-relaxation theorem, not an ES exceptional-set improvement.**

**PROVED — strict Linnik route.** Squarefree products and HB give exceptional exponent
1/A at cap log^A X/4, A>1, including a one-mute-prime polylog-window witness. At cap
(log X)/2 the EMV adaptation gives the subpower exceptional bound (2.3). These are
routine adaptations of established least-nonresidue methods, not new analytic theorems.

**PROVED — scoped stopping results.** The common positive smooth-squareclass HB
amplifier cannot give a fixed power saving at Y=(log X)^{1+o(1)}, even with optimized
length, arbitrary prime classes up to Y, weights or square multipliers. Full fixed-x
sharpness at prime K extends the old Type II-only statement, with the exact cap-zero
exception p≡−1 (q). **CONDITIONAL on Dickson:** those sharp positive-cap windows recur
infinitely often. Neither statement forbids other windows or other cap methods.

**CERTIFIED — numerical controls.** Two retained independent engines agree through
10⁸ on all five cap/character/window histograms; the exact rational and control checks
pass. All primes in the nonclassical class have a Type II cap-zero window ≤107. Thus
these computations test the proof identities and restricted quantities, not hypothetical
ES exceptions. They do not validate the asymptotic constants numerically.

**Reviews.** Round 1 HB and witness: SOUND. Round 2 endpoint and full-window sharpness:
SOUND. Round 3 growing-rank loglog cap: SOUND. Round 4 EMV endpoint and full census:
SOUND. All minor repairs are recorded at the affected claims. The specified model
family was used throughout: `anthropic/claude-opus-5-5`, deep mode; the tool would not
resolve a model ID containing the requested `:high` suffix. No other model substituted.

**Exact remaining gap.** A fixed or zero cap needs a pointwise divisor-box hit or a
stronger average supply/transfer theorem. The loglog cap proof gains its power from
nonintegral exponents and loses that gain at e=0. The Linnik implication confines only
q≤4e+3; no stronger pointwise implication from a generic character profile to ES was
proved. We do **not** establish the brief's literal global threshold at which such an
implication becomes impossible: that would overstate both our local sharpness theorem
and current knowledge of ES. No power saving for ES/ES₅/U itself, and no transport to
cap zero, follows from these results.

**Disposition:** all sections committed; deliver this labelled report and WAIT.
Do not merge until explicitly told.
