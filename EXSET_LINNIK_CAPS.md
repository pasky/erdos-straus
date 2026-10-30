# EXSET_LINNIK_CAPS — wave z51, lane 2b (`lcaps`)

**Status: COMPLETE — T2-lite reached; T2-full not reached. ES remains OPEN.**
**Addendum (lane `lcaps2`, §4A):** Theorem 4.5 extends the loglog-cap power saving to **all odd
integers** by taking the mute alphabet among primes ≡3 (4). Proposition 4.6 is the scope-patched
short-window witness sieve. Both are cap-relaxation results only.
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
| 4A (`lcaps2`) | All-integer loglog cap (Thm 4.5); window-witness sieve (Prop 4.6) | PROVED relative to G + Montgomery / SW + Selberg | Astra (cross-lab): MINOR, repaired |

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

## 4A. All-integer corollaries (wave z51, lane `lcaps2`)

Source: advisory board `20261029-depth-break`, memo finalists astra-7 and argon-7 (board audits by
fable/argon/astra). This section is the lane formalisation, with its own independent checks
(`scripts/z51_lcaps2_check.py`) and its own cross-lab hostile review. Throughout n>1 is **odd** and
e*(n) is the cap of §1; the CAP_POINTWISE/EXPONENT_CAP normalisation is stated for every odd n>1,
not only primes, and ES(n)⟺e*(n)=0. **Neither result below concerns ES, ES₅ or U:** both are CRT
sieves for the cap relaxation, whose untruncated class supply exceeds that of cap zero.

### Lemma 4.3 — classical cap-zero inputs (PROVED, classical identities)

Let n>1 be odd. If n≡5 (8), or n has a prime factor q≡3 (4), then ES(n) holds, so e*(n)=0.
In particular {n odd: e*(n)>0} consists of n≡1 (8) all of whose prime factors are ≡1 (4).

**Proof.** For n=8k+5: 4/n=1/(2k+2)+1/(n(k+1))+1/(2n(k+1)), since 4/n−1/(2k+2)=3/(2n(k+1)).
For q|n, q≡3 (4), m=n/q: 4/q=1/((q+1)/4)+2/(q(q+1)/2), so
4/n=1/(m(q+1)/4)+1/(mq(q+1)/2)+1/(mq(q+1)/2), all denominators integral (CAP_POINTWISE
Cor 1.2(a)). Repeated denominators are allowed in ES and in Def 1.1. An n≡3 (4) has a prime
factor ≡3 (4). Integral z means den z=1, i.e. cap 0. ∎

### Lemma 4.4 — the box certificate for composite inputs (PROVED, elementary)

Let S be a finite set of odd primes, P=∏S, E≥1, and Q_a=∏_{s∈S}s^{a_s} with 0≤a_s≤E.
Let ℓ be a prime with ℓ≡−1 (mod 4P), A=(ℓ+1)/4, D=Q_a². Let n>1 be odd, **gcd(n,P)=1**,
and n≡−4D (mod ℓ). Put V=(n+4D)/ℓ and

    x=(n+V)/4,  y=nA,  z=nxA/D.                                   (4.7)

Then x,y∈ℤ_{>0}, 4/n=1/x+1/y+1/z, and den z=r² with

    r=∏_{s∈S} s^{max(0, a_s−v_s(A))}.                              (4.8)

Hence r is odd, gcd(r,n)=1, rad r⊆S, rad r|A|y and v_s(r)≤max(0,a_s−1)≤E−1: **e*(n)≤E−1.**

**Proof.** Since ℓ≡3 (4) and ℓV=n+4D≡n (mod 4), V≡−n (mod 4); so x∈ℤ, and x>0.
Also AV=(ℓV+V)/4=(n+4D+V)/4=x+D, hence
1/y+1/z=(x+D)/(nxA)=V/(nx)=(4x−n)/(nx)=4/n−1/x. The primes of D lie in S, so
gcd(D,n)=1 and den z=D/gcd(D,xA). Fix s∈S and put σ=v_s(A); σ≥1 because 4P|ℓ+1.

*If a_s=0*, then s∤D and s contributes nothing to den z. **No valuation statement about V is
needed or true here** (astra's round-4 narrowing): e.g. P=21, ℓ=83, Q=27, n=6961 gives V=119,
so 7|V although a₇=0.

*If a_s>0*, then s|D and s∤n, so ℓV=n+4D≢0 (mod s); hence v_s(V)=0 and v_s(AV)=σ.
If σ<2a_s, then v_s(x)=v_s(AV−D)=σ, v_s(xA)=2σ, and the s-part of den z is s^{2max(0,a_s−σ)}.
If σ≥2a_s, then v_s(x)≥2a_s, so v_s(xA)≥2a_s and s∤den z. In both cases the exponent is
2·max(0,a_s−σ), proving (4.8). The remaining assertions follow from σ≥1 and gcd(n,P)=1. ∎

Primality of n is never used: this is CAP_INTERPOLATION Proposition 5.1 with M=ℓ, whose proof
uses its prime p only through p∤DM, read for odd composite n. The classes −4D are quadratic
nonresidues mod ℓ (−1 is one, ℓ≡3 (4)), so **no square is ever certified** (T1).
The two worked examples of the board (n=985, 6961; P=21, ℓ=83, Q=27, cap 2) are rechecked.

### Lemma 4.1′ — Lemma 4.1 for an arbitrary odd alphabet (PROVED relative to G)

Lemma 4.1 holds verbatim with “the first k+1 odd primes” replaced by **any** set 𝒮₀ of k+1
distinct odd primes, with P₀=∏𝒮₀ subject to the same hypotheses (P₀ sufficiently large,
log(4P₀)≥√log(2T), T as in (4.1)).

**Proof (audit of the four steps of Lemma 4.1).**
(i) *Prime supply.* (G) is applied at x=T with modulus cutoff Q_G=4P₀ to the progression
ℓ≡−1 (mod 4P), P|P₀. This needs only 4P≤4P₀ and gcd(−1,4P)=1; the residue classes of the
alphabet primes play no role.
(ii) *Exceptional-conductor deletion.* If a Gallagher-exceptional real primitive character χ₁
exists, its conductor is f=2^j f′ with f′ odd squarefree and 2^j∈{1,4,8}. If f′ has a prime
factor in 𝒮₀, omit that prime; otherwise omit any prime. If f′>1, then f∤4P: either the omitted
prime divides f′ but not P, or f′ has a prime factor outside 𝒮₀. If f′=1, then f∈{4,8}. Since P is
odd, 8∤4P. The fixed character χ₋₄ has no real zero in Gallagher's exceptional range once Q_G
is large. Every case avoids f|4P. None of this depends on the alphabet primes being consecutive
or lying in a particular class.
(iii) *Collisions.* The Q_a are distinct integers by unique factorisation. Every Q_a²−Q_b²≠0 has
modulus <P^{2E}, so it has at most 2E log P/log T prime factors exceeding T. The number of bad
ℓ∈(T,2T] is therefore ≤B(B−1)E log P/log T, as before.
(iv) *Main term.* Only φ(4P)≤4P₀ is used. ∎

For the first k+1 primes ≡3 (4), the PNT for the progression 3 mod 4 (θ(x;4,3)∼x/2) shows that
the (k+1)-st such prime is (2+o(1))k log k and log P₀=(1+o(1))k log k. This is the same
first-order size as for the first k+1 odd primes, which is all that the parameter bookkeeping
(4.5) uses.

### Theorem 4.5 — all-integer power saving at loglog caps

**PROVED relative to G and Montgomery's arithmetic large sieve.** For every fixed ε>0 there is
c_ε>0 such that for large N

    #{1<n≤N : n odd, e*(n)>⌈(log log N)^{1+ε}⌉} ≪_ε N^{1−c_ε}.          (4.9)

All counted n satisfy n≡1 (8) (Lemma 4.3), so (4.9) is the board's statement for n≡1 (8).
More precisely, let 𝒮_N (product P) be the alphabet chosen by Lemma 4.1′ from the first k+1
primes ≡3 (4), where k=⌊(2/ε)log log N/log log log N⌋. Each of its primes is O_ε(log log N).
Let ℰ_N be the set of odd 1<n≤N coprime to P that avoid every box class −4Q_a² modulo every
good ℓ of Lemma 4.1′. Then ℰ_N contains the set counted in (4.9) and |ℰ_N|≪_ε N^{1−c_ε}.
Every odd 1<n≤N outside ℰ_N falls into one of two cases. Either n has a prime factor in 𝒮_N,
hence a classical ES solution, or it has the certificate (4.7). That certificate has
rad(den z)⊆𝒮_N, cap ≤E−1 and ℓ≤(log N)^{O_ε(1)}. ℰ_N may be strictly larger than the
high-cap set: 25=5² lies in ℰ_N (squares never hit a box class), yet 4/25=1/10+1/20+1/100.

**Proof.** Take the parameters of Theorem 4.2 with X=N: L=log N, λ=log L, a=2/ε,
k=⌊aλ/log λ⌋, E=⌈λ^{1+ε}⌉, and 𝒮₀ = the first k+1 primes ≡3 (4). By the size remark after
Lemma 4.1′, (4.5) holds unchanged: log P₀=(a+o(1))λ, log B=(a(1+ε)+o(1))λ,
log T=(H+o(1))λ, H=Da(3+2ε), and the Gallagher range of Lemma 4.1′ holds for large N.
Lemma 4.1′ yields P (k primes, all ≡3 (4)) and M≥cT/[φ(4P)log T] primes ℓ∈(T,2T],
ℓ≡−1 (4P), each with B distinct classes −4Q_a² mod ℓ.

Let 𝒮={1<n≤N: n odd, e*(n)>E}. By Lemma 4.3 every n∈𝒮 is coprime to P, because each prime
of P is ≡3 (4). If some n∈𝒮 lay in a class −4Q_a² modulo a good ℓ, Lemma 4.4 would give
e*(n)≤E−1. Hence 𝒮⊆ℰ_N, and ℰ_N avoids B residue classes modulo every good ℓ by definition.
Montgomery's arithmetic large sieve holds for an arbitrary set of integers in an interval of
length N; its inputs need not be prime. It gives |𝒮|≤|ℰ_N|≤(N+Q²)/𝓛(Q). With Q=√N, the lower bound (4.6) for 𝓛 and its evaluation
are unchanged: log𝓛≥(1/(2H)+o(1))L. Hence |ℰ_N|≤N^{1−1/(2H)+o(1)}, and c_ε=1/(4H) works.
The two-case description outside ℰ_N is Lemma 4.3 plus Lemma 4.4. ∎

**What changed from Theorem 4.2, and why the alphabet must be ≡3 (4).** For prime inputs, the
finitely many p|P were simply discarded. For integers, the multiples of an alphabet prime have
positive density and cannot be discarded; Lemma 4.4 does not apply to them (gcd(n,P)=1 is used).
With the first k+1 odd primes, the n divisible by 5 (or by any alphabet prime ≡1 (4)) would
need another argument. Primes ≡3 (4) make every such n classically solvable (Lemma 4.3). The
cost is nothing: the alphabet size and log P₀ are unchanged to first order.

**Remarks (Assessment).** (a) *T1 consistency.* Odd squares coprime to P are never in the box
classes, so they all lie in the class-avoider set ℰ_N. This puts a √N floor on ℰ_N, but not
necessarily on the high-cap set. The bound is consistent with that floor because
c_ε≤1/(4H)<1/2. It says nothing about the caps of squares beyond the trivial count √N. (b) *Comparison.* The all-integer ES bound
N exp(−c(log N)^{3/4}) (`paper/es-threequarter-note.tex`, which counts all n) bounds every
{e*>0}; (4.9) is a power saving, but only above cap ⌈(log log N)^{1+ε}⌉. (c) *Classification.*
This is a CRT class sieve with power-dense forbidden sets, B=ℓ^{θ+o(1)},
θ=(1+ε)/(D(3+2ε)), at polylog primes. It does not breach the G1 cap for the sparse prime-family
classes. The degenerate box E=0 gives B=1. The box E=1 already guarantees cap zero (r=1 in
(4.8), since a_s≤1≤σ), but then log B=k log 2=o(log P₀), so the supply gain required by (4.6)
disappears. The gain comes from large exponents, i.e. from the untruncated classes D_a>ℓ/4. **No transfer to ES/ES₅/U follows.** (d) *Novelty.* The board checked main at
3f502fd4 and found only the prime-input Theorem 4.2. This lane's `git grep` of main, still at
3f502fd4 when this section was written, found no all-integer cap-count statement in the
CAP/EXSET documents. CAP_POINTWISE and CAP_DOWN give pointwise caps for odd n; counts are over
primes.

### Proposition 4.6 — short-window, one-prime witness sieve (argon-7, scope-patched)

**PROVED relative to Siegel–Walfisz and Selberg's Λ² sieve.** Fix 0<α<1. Put L=log N,
y=L^α, 𝒬={q≤y prime: q≡3 (4)}, K=#𝒬 and Π_y=∏𝒬. Say that n≡1 (4) has a
**y-window witness** (q,s) if q∈𝒬, q∤n, s is an odd prime with v_s(n+q) odd, and (s/q)=−1.

(a) *Certificate.* If (q,s) is a y-window witness for n, put K_n=(n+q)/4, b=v_s(n+q),
o=ord_q(s), d=K_n s^{o/2} and A=(K_n+d)/q. Then

    (x,y,z)=(K_n, nA, nK_nA/d)

is an ES^{(y,e)}(n) solution with den z=s^{2h}, h=max(0,(o/2−b)/2)≤(q−3)/4≤(y−3)/4.
It has a **window** x=(n+q)/4 with q≤y and **at most one** overflowing prime s (none when h=0).

(b) *Sieve.* For every δ>0 and N≥N₀(α,δ),

    #{n≤N: n≡1 (8), gcd(n,Π_y)=1, n has no y-window witness}
        ≤ N exp(−((1−α)/(4α)−δ)L^α).                             (4.10)

(c) *Scope (astra's patch).* Hence every n≤N, n≡1 (8), outside a set of size (4.10) either has a
prime factor q≤y, q≡3 (4), and thus a classical ES solution (Lemma 4.3), **or** has a y-window
witness. We do **not** claim a window witness for n sharing a prime with Π_y: the sieve uses
q∤n for every q∈𝒬.

**Proof of (a).** This is CAP_DOWN Lemma 1.1 and Proposition 1.3 with m=q. Their hypotheses
are m≡−n (mod 4), gcd(m,n)=1 and gcd(K_n,n)=1, and neither uses primality of n. The last
holds because a prime t|K_n, t|n divides 4K_n−n=q, so t=q|n, which is excluded. As q≡3 (4) and
(s/q)=−1, the order o has v₂(o)=1 and s^{o/2}≡−1 (mod q). Thus d≡−K_n (mod q) and A∈ℤ.
Furthermore s≠q and s∤n (s|n would give s|q). Since s is odd, v_s(K_n)=b is odd. The exponent
of s in d is b+o/2, which is even; the other exponents are those of K_n. Lemma 1.1 gives den z=s^{2h}
with the stated h, and o≤q−1 gives h≤((q−1)/2−1)/2. ∎

**Proof of (b).** Fix A₀>max(α/(1−α),1/δ) and put log z₀=y^{1/A₀}, log z=L/(100K), and
𝒫={s prime: z₀<s≤z}. For large N, y<z₀<z, since K=(1+o(1))L^α/(2α log L) and
α/A₀<1−α. For s∈𝒫 let w(s)=#{q∈𝒬:(s/q)=−1} and

    Ω_s={−q+js mod s² : q∈𝒬, (s/q)=−1, 1≤j≤s−1}.

These w(s)(s−1) residues are distinct, since s>y separates the q modulo s. Put
ρ_s=w(s)(s−1)/s²≤K/s<1. Primes with w(s)=0 have Ω_s=∅ and ρ_s=0; discard them from 𝒫. This
changes neither the sifted set nor the mass, and afterwards 0<ρ_s<1 for every s∈𝒫.

*Inclusion.* Let n be counted in (4.10) and s∈𝒫. If n≡−q+js (mod s²), then v_s(n+q)=1 is odd,
(s/q)=−1 and q∤n, so (q,s) is a witness. Hence n mod s²∉Ω_s for every s∈𝒫.

*Selberg.* Let 𝒜={n≤N: n≡1 (8)}, and for squarefree d|∏𝒫 let 𝒜_d be the n∈𝒜 with
n mod s²∈Ω_s for all s|d. The moduli 8 and s² are pairwise coprime, so CRT gives
|𝒜_d|=(N/8)ρ(d)+r_d, ρ(d)=∏_{s|d}ρ_s and |r_d|≤∏_{s|d}#Ω_s≤d². For each n write
𝒟(n)=∏{s∈𝒫: n mod s²∈Ω_s}; then d|𝒟(n) and e|𝒟(n) iff [d,e]|𝒟(n). For any real λ_d with
λ₁=1, supported on d≤Q, we have 1_{𝒟(n)=1}≤(Σ_{d|𝒟(n)}λ_d)². Summation gives the usual
quadratic form. With g(s)=ρ_s/(1−ρ_s) and G(Q)=Σ_{d|∏𝒫, d≤Q}g(d), Selberg's choice yields

    #(counted set) ≤ (N/8)/G(Q) + Σ_{d,e≤Q}|λ_dλ_e||r_{[d,e]}|.

The minimisation uses only the multiplicativity of ρ with 0<ρ_s<1. The standard axiomatic Λ²
sieve applies to such events at pairwise coprime moduli; see Friedlander–Iwaniec, *Opera de
Cribro*, Ch. 7, and Halberstam–Richert, *Sieve Methods*, Ch. 3. The optimal weights satisfy
|λ_d|≤1. Indeed λ_d=μ(d)∏_{s|d}(1−ρ_s)^{−1}·G_d(Q/d)/G(Q), where G_d sums g over m coprime
to d, and G(Q)≥Σ_{e|d}g(e)G_d(Q/d)=∏_{s|d}(1−ρ_s)^{−1}G_d(Q/d). Take Q=N^{1/20}. The
remainder is then ≤Σ_{d,e≤Q}[d,e]²≤Q⁶=N^{3/10}.

*Lower bound for G.* Let Π=∏_{s∈𝒫}(1−ρ_s)^{−1}=Σ_{d|∏𝒫}g(d). Differentiating the Euler product,
Σ_d g(d)log d=Π Σ_s ρ_s log s. Hence the tail d>Q has g-mass ≤Π Σ_sρ_s log s/log Q. By
ρ_s≤K/s and Mertens, Σ_sρ_s log s≤K(log z+O(1))=L/100+O(K). Since log Q=L/20,
G(Q)≥(4/5−o(1))Π≥(3/4)exp(Σ_{s∈𝒫}ρ_s).

*Mass.* Σρ_s≥Σ_{q∈𝒬}Σ_{z₀<s≤z,(s/q)=−1}1/s−K/z₀. For t≥z₀ and q≤y we have
q≤(log t)^{A₀}. Siegel–Walfisz therefore gives #{s≤t:(s/q)=−1}=li(t)/2+O_{A₀}(q t e^{−c√log t}),
summing over the (q−1)/2 nonresidue classes. By partial summation the inner sum is
(1/2)log(log z/log z₀)+O_{A₀}(q·log z₀·e^{−c√log z₀}). Here log z₀=y^{1/A₀}, so the error summed
over K≤y primes q is o(1). Also

    log(log z/log z₀)=log L−log(100K)−(α/A₀)log L ≥ (1−α−α/A₀)log L.

With K=(1+o(1))L^α/(2α log L) this gives
Σρ_s≥(1+o(1))((1−α)/(4α)−1/(4A₀))L^α>((1−α)/(4α)−δ/2)L^α.
Therefore the count is ≤(N/6)e^{−((1−α)/(4α)−δ/2)L^α}+N^{3/10}. This implies (4.10), since L^α=o(L). ∎

**Scope (Assessment).** The unrestricted count {e*>(y−3)/4} is dominated by Theorem 4.5 for
every α, and by the 3/4 note for α<3/4. At α=3/4 the note gives the same exponent scale; we
make no comparison of constants. At primes, CAP_INTERPOLATION Theorem 2.1 is stronger.
Only the **restricted witness reading** is new: a window x=(n+q)/4 with q≤(log N)^α and at most one
overflowing prime, for all integers coprime to Π_y. The sieve dimension grows (K≍y/log y), but
every window can fail only in Landau mode at the moduli s², so a classical sieve collects the
full mass. Nothing transfers to U/ES₅. For a shift v≥(log N)^{0.129}, U's subset-product failure
is dominated by n+v with few prime factors, not by Landau mode (board item fable-1, scoped).

### Checks for §4A (CERTIFIED finite computation; independent code)

`scripts/z51_lcaps2_check.py` shares no code with the board scripts or `z51_lcaps_*`. It uses
exact rationals and checks Def 1.1 directly, including a full factorisation of den z. Results
are in `data/z51_lcaps2/check.json`; the run takes 4 s and a few MB.

- **Lemma 4.4, exhaustive:** six alphabets of primes ≡3 (4), namely {3,7} (E=3,5), {3,7,11},
  {3,11,19}, {7,23} and {3,7,11,19}. For each, every prime ℓ≡−1 (4P) in a range and every box
  class were checked against every n≡1 (8) coprime to P in a range. This gives
  **51,915 certificates, 36,559 with composite n**, and 0 failures. Each check verifies
  the identity, the den z conditions and the exact formula (4.8). The cap reaches E−1 in every
  row, and 40,305 certificates have positive cap. For every a_s>0, s∤V. In 7,535 cases
  a_s=0 and s|V: the narrowed sentence is necessary. Also 3000 random composite n of size
  ≈10²⁷ with ℓ<10⁷ pass, and the board's two worked examples are reproduced exactly.
- **Lemma 4.3:** integral triples verified for all 136,216 odd n<3·10⁵ with a prime factor ≡3 (4)
  or n≡5 (8). Every other odd n in range is ≡1 (8) with all prime factors ≡1 (4).
- **T1:** 5,424 box classes are all quadratic nonresidues, and no square residue lies in a class.
  In the toy sieve every odd square coprime to 2P survives.
- **Lemma 4.1′ collisions:** alphabets drawn from the first primes ≡3 (4), with one prime omitted.
  Bad ℓ ≤ pair incidences ≤ B(B−1)E log P/log T in all six rows; five rows contain genuine
  collisions (non-vacuous).
- **Montgomery on integers (toy):** N=2·10⁶, P=21, E=3, eight collision-free ℓ≤√N. The sifted
  set has 373,365 elements, below the exact bound (N+Q²)/𝓛=844,746.
- **Proposition 4.6(a):** 33,288 window-witness checks on n≤6·10⁴ (25,465 of them with composite
  inputs; 27,567 with positive cap), checked exactly with den z a power of s and 4h≤q−3. The class inclusion
  “n≡−q+js (mod s²) ⇒ witness” was checked on 5,170 classes.
- **Controls:** all 18 hard primes/R-zeros receive an exact (4.7) certificate with P=21 and E=6.
  The search factors p+4Q_a²; the best caps are 0–5. Numerator 8 (n=17, 241) is outside
  scope: (4.7) uses 4|n+V and is numerator-4 specific; nothing here transfers to 8/n.

The asymptotic constants (D, c_ε, the Siegel–Walfisz error) are not numerically certified; the
toy rows test the identities and inequalities, not the asymptotic regime.

**Hostile cross-lab review of §4A (Astra, `openai-codex/gpt-6-astra`, deep mode): MINOR — no
MAJOR/FATAL; the two exceptional-set bounds survive.** The tool does not resolve the `:high`
suffix. Session: `2026-10-30T01-11-46-620Z_01a18a5c-e6bc-708e-bdc7-d06d1525e888.jsonl`.
Lemma 4.3, Lemma 4.1′ (including every conductor case of the deletion and log P₀) and
Prop 4.6(a) were judged SOUND. The Selberg weights, the Q⁶ remainder, the G(Q) tail bound and
the Siegel–Walfisz mass in Prop 4.6(b) were all re-derived. The reviewer reran the script
byte-identically and added its own checks: 1,700 composite box certificates over arbitrary
alphabets and all odd classes; 14,059 composite window witnesses (274 with v_s>1, 6,631 with
even K_n); and an exact Selberg quadratic-form/weight/tail check. All passed.

Repairs applied:
(1) Positive parts in the intermediate valuation sentences of Lemma 4.4. The reviewer's
    counterexamples were n=95 (a₃=0) and n=425 (a₃=2, σ=3); formula (4.8) was already right.
(2) The two-case description in Thm 4.5 is now stated outside the class-avoider set ℰ_N, which
    is sieved directly. The earlier wording "outside the exceptional set" was false at squares
    such as 25.
(3) Zero-density primes are discarded in Prop 4.6(b), and "at most one" overflow prime is used.
(4) Cap zero corresponds to E≤1, not to B=1.
(5) The comparison with the 3/4 note is stated as strict for α<3/4 only.
(6) Counts and script labels were corrected.

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
timeout 600 uv run scripts/z51_lcaps2_check.py > data/z51_lcaps2/check.json   # §4A
```

## 6. Final assessment and exact remaining gap

**PROVED — T2-lite, strongest retained theorem.** Theorem 4.2 gives

    #{p≤X:e*(p)>⌈(log log X)^{1+ε}⌉} ≪_ε X^{1−c_ε},  c_ε>0,

with a common tiny mute-prime alphabet. This goes well below both CAP_BOUNDED's
log^{2+ε} threshold and CAP_INTERPOLATION's log^{1+ε} sketch. Its ingredients are the
untruncated cap dictionary, elementary collision counting, Gallagher's exceptional
conductor deletion, and the arithmetic large sieve. No GRH, OAI-003, or new conjecture
is used. **This is a cap-relaxation theorem, not an ES exceptional-set improvement.**

**PROVED (§4A, lane `lcaps2`) — all-integer version.** Theorem 4.5 gives
#{1<n≤N odd: e*(n)>⌈(log log N)^{1+ε}⌉} ≪_ε N^{1−c_ε}, relative to the same inputs, with the
mute alphabet restricted to primes ≡3 (4). Proposition 4.6, relative to Siegel–Walfisz and Selberg,
shows the following for n≡1 (8) outside N exp(−((1−α)/(4α)−δ)(log N)^α) exceptions. Each such n either
has a classical solution through a prime q≤(log N)^α, q≡3 (4), dividing n, or has a window witness
with q≤(log N)^α and one overflow prime. Neither moves ES/ES₅/U or cap zero.

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
For §4A (lane `lcaps2`), one cross-lab review was run, Astra (`openai-codex/gpt-6-astra`, deep).
Its verdict was MINOR, with no MAJOR or FATAL findings, and its repairs are recorded in §4A.

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
