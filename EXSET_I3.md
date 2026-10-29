# I3 exceptional sets — wave z50, lane E (`i3ex`)

## 0. Status and summary

**Outcome: new scoped barrier, not an improved exceptional-set upper bound.** ES and Conjecture I3 remain open. The known log-loss 2/3 I3 bound is optimal in the native whole-avoider coefficient-sum CRT architecture, up to constants. Three rounds of cross-model review found no fatal or major defect; minor repairs are incorporated.

| Item | Status | Result / exact gap |
|---|---|---|
| Prior-work and barrier audit | COMPLETE | Native classes are not ES forced classes; zero base replaces square base. |
| Round 1: native multiplier atoms | PROVED / reviewed | Quadratic mass rules out cubic supply, including the standard selector. |
| Round 2: transfer / I3 cap | PROVED / reviewed | Native whole-avoider CRT cap C(log N)^{2/3}, superseded by Round 3. |
| Round 3: optimal cap | PROVED / reviewed | Cap C(log N)^{2/3}/(log log N)^{1/3}, matching the known native upper bound. |
| Beyond CRT / ES port | OPEN / scoped negative | Noncoprime endpoint events escape the base; interval error and colour-compatible transport remain missing. |
| Independent numerical checks | CERTIFIED, finite scope | 104 zeros through 5,000; largest zero separately; controls and truncated avoiders. |
| Literature after 2025 | CHECKED, limited search | PW v2 / Pomerance 2026 slides retain 2/3; September 2026 candidate is withdrawn. |
| Hostile reviews | SOUND after minor repairs | Three Opus deep reviews; exact `:high` identifier unavailable, same model without suffix used. |

## 1. Source audit and scope

**Assessment / audit.** The binding z48, z49 and z50 context files were read in order (z50 twice). Source inspection includes FRONTIER §§2–4,6–7; BREADTH_Z45 §§1–14; the PR-B main note and both supplements; OAI_DUMP_IMPACT; I3_DEEP_ASTRA in full; summaries of the six z48 forest/lower-tail notes; DISCOVERIES (D)17–(D)31; and the actual KARY2/KARY3 base, moment and cap proofs. The 3/4 note's atom identity and assembly are audited rather than accepted as an I3 witness map. No OAI hypothesis is used.

**PROVED previously relative to BV, Brun–Titchmarsh and Mertens, not re-claimed.** Write E₃(N)=#{3≤n≤N:I3(n)=0}. I3_DEEP_ASTRA §8.8 proves

`E₃(N) ≪ N exp(−c(log N)^{2/3}/(log log N)^{1/3})`.

Its §8.7 proves that the Vaughan ratio identity gives a word of bn, not n, and that I3 is not closed under multiplication (21 has a word; 42 does not). The requested 3/4 theorem therefore needs new atoms or a new transfer; the ES scaling argument cannot be reused.

**Definition (native divisor classes).** Let D be the universe of classes

`C(t,u) = {n : n ≡ −u (mod M)},  M=tu−1,  t,u≥3`.

Each class is reduced: gcd(u,M)=1. Above n≥3M it supplies v=(n+u)/M≥3. At a fixed M its labels are the distinct divisors `3≤u≤(M+1)/3` of M+1. A family means a finite subset of these classes, with no restriction on factorisation or size of its moduli. Its avoider set means all integers avoiding all those congruences, not merely actual I3 zeros.

**Assessment / barrier scope.** D is not an ES forced-class subfamily: the class n≡−5≡9 (mod 14), from t=3,u=5, contains the odd square 121=3·5·9−5−9. KARY2's unit-square base therefore fails. This does not refute its arithmetic-free comparison theorem. A replacement base is possible because every D-class is reduced: pin n≡0 mod every small prime, killing every native class with such a prime in its modulus. Sections 2–3 examine the resulting quadratic-mass rather than cubic-mass architecture. This base fails for nonunit endpoint classes n≡−u−v (mod uv) (u=v=3 gives 3 mod 9, meeting 0 mod 3), and is incompatible with selectors 0 mod p for p≤W (it lies inside them). A cap on D alone does not cover these classes, prime/rough-only majorants, or interval-only majorants.

**Assessment / novelty standard.** Dictionary identities and the mass calculation alone are not counted as exceptional-set progress. A genuinely new cap would have to check a new base, the smooth first moment, the leak uniformly in the cutoff, and the coefficient-sum projection. No numerical experiment or standard conjecture is promoted to a pointwise I3 result.

## 2. Round 1 — I3-native multiplier atoms

### 2.1 Quadratic supply rules out the requested cubic-supply lemma

**PROVED (elementary scope obstruction; not itself a new exceptional-set bound).** For Y≥8 the sum of Haar probabilities of all distinct D-classes of modulus ≤Y is O(log²Y). Consequently, if K≤X^κ with fixed κ<1/2, q∈(√X,X] is prime, and atoms are any distinct classes `n≡−u mod kq`, with `u|(kq+1)` and t=(kq+1)/u≥3, their total mass is O_κ(log²X). There cannot be conditional mass ≥c(log X)³ on a set of fibres of Haar probability bounded below, or even of probability ≫1/log log X.

*Proof.* The number of labels at M is at most τ(M+1). Divisor hyperbola counting gives `Σ_{M≤z}τ(M+1)≪z log(2z)`; partial summation gives `Σ_{M≤Y}τ(M+1)/M≪log²Y`. A modulus kq≤KX has only one prime factor in (√X,X], since k<√X, so different multiplier labels do not duplicate its q. Summing probabilities gives the assertion. For any conditioning, the average conditional hit count is the original mean. If mass ≥cT³ on a fibre set of probability b, then `b cT³≤CT²`, hence b≪1/T. ∎

**PROVED consequence for the proposed selector.** The standard selector `S_y=1[(n,P_y)=1]`, with y a fixed power of T=log X, has Haar probability `∏_{p≤y}(1−1/p)≍1/log T` (Mertens). Conditional on S_y=1, the mean of the native count is at most `O(T² log T)=o(T³)`. Thus cubic supply on all but an exponentially small proportion of these selector fibres is impossible. This does not exclude another I3 atom family or a non-CRT argument.

**Assessment / exact failure.** Splitting u or t into extra factors produces multiple labels for the same residue, not additional distinct classes. A count with duplicated labels cannot be fed into the independent-Bernoulli Bonferroni argument as though the labels were separate shots. The extra factor in the ES note comes from distinct ratio labels; §8.7 of I3_DEEP_ASTRA explains why those ratios give words of bn instead of n.

### 2.2 First attack on the surviving gap

**Assessment / candidate, not yet a theorem here.** Replace the failed cubic supply by an audit of the full D-universe. For fixed W, pin n≡0 modulo `P_W=∏_{p≤W}p`. All native classes with a prime ≤W in their modulus disappear. The remaining prime coordinates are independent initially, and their capped sequential laws have inflation factors `(1−p^{−1/2})^{−1}`. If the first moment is O(log²y), the KARY block balance is `s²≈λ/s`, giving a 2/3 cap rather than 3/4. This demands a new smooth shifted-divisor estimate and a leak bound uniform in W; they are supplied, or rejected, in Round 2. The abstract comparison theorem is not by itself an arithmetic cap.

**Hostile review R1 (Opus): SOUND after a minor witness correction.** The initial square example in §1 incorrectly put 121 in 5 mod 8; it is replaced by the correct word 121=3·5·9−5−9 and class 9 mod 14. The reviewer confirmed the quadratic-supply obstruction and zero base, and required the explicit selector/endpoint exclusions now stated. The stronger selector estimate suggested by the reviewer is not needed here; no unproved extension is imported. Model availability and review provenance are recorded in §6.

## 3. Round 2 — a native I3 cap, stronger than 3/4

### 3.1 Statement and precise architectural scope

**Theorem 3.1 (PROVED relative to Shiu's theorem and the internally proved arithmetic-free KARY comparison; Opus review SOUND).** There are absolute W₀,C,λ₀ such that, for every finite family F⊂D and every finite congruence expansion

`ν(n)=Σ_i a_i 1[n≡b_i (mod d_i)] ≥0` on all integers,

with ν≥1 on the entire congruence avoider set A(F), and with

`Σ_{p|d_i, p>W₀} log p ≤ λ` for every term,

one has `log(1/Eν) ≤ C λ^{2/3}` for λ≥λ₀. Mean means uniform Haar mean over a common finite period. The moduli of F are arbitrary: prime powers, balanced moduli, arbitrarily many large primes, and arbitrarily large cofactors are allowed.

**Corollary 3.2 (PROVED relative to the same inputs; sharpened by (4.1)).** Suppose every prime dividing a family modulus is ≤N^A, with A fixed. Every bound of the form `B=N Eν+Σ|a_i|`, with ν as above and Σ|a_i|<N, satisfies

`log(N/B) ≤ C_A (log N)^{2/3}`.

Thus no such native-class method proves a 3/4 I3 exceptional estimate, even after replacing Bonferroni by an arbitrary globally nonnegative congruence majorant. This does **not** assert a lower bound for E₃(N), or for the actual number of avoiders in [1,N]. A numerical E₃(N)=112 is entirely consistent with the theorem.

**Assessment / novelty.** D contains classes meeting odd unit squares and was not covered by (D)17–(D)29. The theorem supplies an I3-specific base and quadratic profile; it is not a substitution of the word I3 into an ES theorem. It extends the cap machinery to a new family, but is not yet a cap for the union of every ES class type with every I3 class type. The broader-union question is revisited in Round 3.

### 3.2 A base with no small-prime inflation

Fix W≥16, to be chosen absolutely after the leak estimate. Let Q₀ contain the full small-prime parts of the family and test periods and also P_W. On the base use the uniform law on

`R₀={n mod Q₀ : n≡0 mod p for every p≤W}`.

Its density is 1/P_W, so the base cost is `log P_W=O(W)`, independent of the exponents in Q₀. Every D-class whose modulus has any prime ≤W is killed outright: its target residue is a unit at that prime. Delete these classes. All remaining moduli and all their cofactors have prime factors >W. Subsequent coordinates are independent uniform prime-power residues before the KARY sequential modification.

Use light thresholds δ_p=p^{−1/2}. Define Γ multiplicatively by

`Γ(p^a)=1 (p≤W),   Γ(p^a)=(1−p^{−1/2})^{−1} (p>W), a≥1`.

For an active cofactor q (necessarily W-rough), the capped sequential law Q′ satisfies `Q′(n≡b mod q)≤Γ(q)/q`, by the arithmetic-free chain-rule bound KARY Lemma 2.1. Γ is **not** claimed to bound classes involving pinned small primes. None of the remaining patterns involves those primes, which is why this distinction causes no gap.

Write Γ=1*h, with h squarefree-supported and `0≤h(p)≤2p^{−1/2}` for every p. All Euler-product constants in the next two subsections are uniform in W. This is stronger bookkeeping than assigning a large inflation factor p to each pinned coordinate and then trying to send W→∞.

### 3.3 Smooth shifted-divisor mass of order two

**Lemma 3.3 (PROVED relative to Shiu).** Uniformly in W≥16,

`Σ_{m≤x} τ(m+1)Γ(m) ≪ x log(2x)`,

and, for y sufficiently large,

`M_D(y):=Σ_{P⁺(m)≤y} τ(m+1)Γ(m)/m ≪ (log y)²`.       (3.1)

The sums may include m=1; this changes only a constant. Dropping the W-rough restriction only enlarges them.

*Proof of the ordinary mean.* Work in dyadic m-blocks K<m≤2K. Expand Γ=1*h. For e≤K^{1/4}, Shiu for τ in the reduced progression m+1≡1 mod e gives

`Σ_{K<m≤2K,e|m}τ(m+1) ≪ (K/e)log K`.

Indeed the Shiu factor `(e/φ(e))∏_{p|e}exp(−2/p)` is ≤1. The case e=1 is the elementary divisor bound on average. Sum h(e)/e, whose Euler product converges absolutely. For e>K^{1/4}, the pointwise divisor bound and the fact that e≤2K give a contribution at most

`C_ε K^{1+ε} Σ_{e>K^{1/4}}h(e)/e ≪ K^{1+ε−1/16}`,

using `Σ h(e)e^{−3/4}<∞`. Choose ε<1/32 and sum blocks.

*Proof of the smooth mean without a log-log loss.* This is the local-moment device of KARY3 §2, checked with τ(m+1), whose prime value is 2 rather than 3. Put

`Z_y(m)=(log y)^{−1}Σ_{p^a|m,p^a≤y}log p`,

and let S_y(m) be the product of the full prime powers p^{v_p(m)}>y in m. If m is y-smooth, S_y(m) is squarefull, and for K<m≤2K, u=log K/log y,

`1[P⁺(m)≤y] ≤ 1[P⁺(m)≤y]1[S_y(m)>K^{1/2}] +(2Z_y(m)/u)^k`.

Fix k=3 and K≥y^{16k}. The squarefull contribution weighted by τ(m+1)Γ(m) is O(K^{4/5}), since the number of integers with a squarefull divisor >K^{1/2} is O(K^{3/4}). For the other term expand Z_y^k. Each tuple of prime powers has lcm D≤y^k≤K^{1/16}, ω(D)≤k. Put

`T(q)=Σ_{K<m≤2K,q|m}τ(m+1)`.

Shiu gives `T(q)≪(K/q)log K` for q≤K^{1/2}, and the trivial bound gives `T(q)≪_ε K^{1+ε}/q` for q≤2K (T(q)=0 for q>2K). Expanding Γ, the e≤K^{1/4} part satisfies

`Σ_e h(e)/[D,e] ≤ C Γ(D)/D`.

The e>K^{1/4} part satisfies

`Σ_{e>K^{1/4}} h(e)gcd(D,e)/e ≤ C 2^k K^{−1/16}`,

because its Rankin Euler factors at p|D are `1+h(p)p^{1/4}≤2`, and those elsewhere are `1+h(p)p^{−3/4}`. Thus

`Σ_e h(e)T([D,e]) ≪ [K log K Γ(D)+2^k K^{1−1/16+ε}]/D`.

The local moment identity KARY3 Lemma 2.2 applies with uniform constants:

`Σ_{d₁,…,d_k prime powers≤y} Λ(d₁)…Λ(d_k) Γ(lcm(d_i))/lcm(d_i) ≪_k (log y)^k`.

Its proof groups equal underlying primes and uses `Σ_{p≤y}Γ(p)log p/p≪log y`; it uses neither ES classes nor a square base. It also bounds the error term since Γ≥1. We obtain

`Σ_{K<m≤2K,P⁺(m)≤y}τ(m+1)Γ(m) ≪ K log K · u^{−3}`.       (3.2)

Power errors are absorbed for K≥y^{48}, since u≤log K/log 2. For m≤2y^{48}, the ordinary mean and partial summation give O(log²y). Beyond this body, each dyadic block contributes `O(log y·u^{−2})` to M_D(y), and the spacing of u is log 2/log y. Summing the convergent u^{−2} tail gives O(log²y). ∎

### 3.4 Cofactor second moment and uniform leak

**Lemma 3.4 (PROVED relative to Shiu).** For the remaining native classes and the capped sequential law,

`E_{Q′} p_ℓ² ≪ ℓ^{−7/4}(log ℓ)^c` for ℓ>W,       (3.3)

with an absolute exponent c and absolute implied constant independent of W and the finite family. Consequently the probability of hitting any heavy-top class is ≤1/2 when W is a sufficiently large absolute constant.

*Proof.* For top prime ℓ and exponent v write a modulus as m=qℓ^v, P⁺(q)<ℓ. There are at most `μ_v(q)=τ(qℓ^v+1)` labels. If N_{ℓ,v} counts active labels, `p_ℓ≤Σ_{v≥1}ℓ^{−v}N_{ℓ,v}`. Expanding a square and dropping incompatible pairs, the chain-rule estimate gives KARY2 Lemma 4.1's arithmetic-free bound

`E N_{ℓ,v}² ≪ log ℓ · Σ_{P⁺(q)<ℓ} μ_v(q)² τ(q)Γ(q)/q`.

Only W-rough q actually occur; enlarging to all q is harmless. The Euler-product factor `Σ_{P⁺(q)<ℓ}Γ(q)/q≪log ℓ` has an absolute constant here.

For completeness the shifted cofactor sum obeys, for any fixed η>0,

`Σ_{P⁺(q)<ℓ}τ(qℓ^v+1)²τ(q)Γ(q)/q ≪_η (v+1)^c[(log ℓ)^c+ℓ^{ηv}]`.       (3.4)

To verify it, split q into dyadic blocks K<q≤2K. For K≥4ℓ^{v/3}, apply Cauchy–Schwarz. The first factor, involving τ(q)²Γ(q)²/q over ℓ-smooth q, is at most `C exp(−u/2)(log ℓ)²`, u=log K/log ℓ. This is Rankin with exponent 1/log ℓ and the multiplicative prime value 4. The second factor is

`(Σ_{K<q≤2K}τ(qℓ^v+1)^4/q)^{1/2} ≪ ((v+u+1)log ℓ)^8`.

Here Shiu applies to τ⁴ in the reduced progression 1 mod ℓ^v: the interval has length Kℓ^v, modulus ℓ^v below a fixed 3/4 power of its scale, and τ⁴(p)=16. The harmless power 8 rounds up 15/2. Summing exp(−u/2)(v+u+1)^8 over dyadic u gives a polynomial in v+1 and log ℓ. In the short blocks K<4ℓ^{v/3}, qℓ^v+1≤Cℓ^{2v}; the divisor bound on the entire numerator, followed by Σ1/q≪v log ℓ, gives O_η(ℓ^{ηv}). This proves (3.4), including q=1 separately.

Take η=1/4. Minkowski over v gives `(E p_ℓ²)^{1/2}≪Σ_v ℓ^{−7v/8}(v+1)^c(log ℓ)^c≪ℓ^{−7/8}(log ℓ)^c`. All constants are uniform in W because h(p)≤2p^{−1/2} uniformly and no pinned small-prime cofactor survives. The heavy-top union bound is

`Σ_{ℓ>W} E[p_ℓ 1(p_ℓ>ℓ^{−1/2})] ≤ Σ_{ℓ>W}ℓ^{1/2} E p_ℓ² ≪ Σ_{ℓ>W}ℓ^{−5/4}(log ℓ)^c →0`.

Choose W=W₀ so this is ≤1/2. ∎

### 3.5 Comparison and coefficient ledger

*Proof of Theorem 3.1.* Use KARY Theorem 4.1 with the base in §3.2, the plain sequential process and thresholds above. Its hypotheses are purely product-space statements, not square-class statements: block conditional comparison for nonnegative low-locality functions, and leak ≤1/2. The latter is Lemma 3.4.

Set s₀=λ^{1/3}. Treat primes W₀<p≤exp(s₀) singly; their total comparison cost is O(M_D(exp s₀))=O(s₀²). On each successive block

`exp(s)<p≤min(exp(2s),exp λ),  s=2^i s₀<λ`,

a level-λ function is d-local, d=⌊λ/s⌋. KARY Corollary 2.6 supplies expected comparison cost

`≤ d log(C(E M_V+4d)/d)+O(d+log(d+1))`.

By Lemma 3.3, E M_V≪s². Since d≥λ/(2s), the logarithm is O(1+i), and the block cost is at most `C λ(1+i)/(2^i s₀)+O(log λ)`. Summing gives O(λ/s₀+log²λ)=O(λ^{2/3}). For primes >exp λ every test function is independent of that coordinate, so the same process has comparison cost zero; its possible heavy hits are already included in the leak bound. No linear-block lemma is needed. KARY Theorem 4.1 adds the fixed base cost log P_W₀ and log 2, and doubles the summed costs. This proves the claim. ∎

*Proof of Corollary 3.2.* Project ν onto the common family period Q. Each class d becomes its class modulo d′=gcd(d,Q) with coefficient multiplied by d′/d. Positivity, majorisation and mean are preserved; coefficient sum does not increase, and every remaining prime is ≤N^A. Put T=Σ|a_i| and S=log(1/Eν). The arithmetic-free coarsening in EXCEPTIONAL_THETA Lemma 2.9 yields a majorant ν′ of level `λ=A log N+log T+S`, with Eν′≤2Eν: drop negative high-level terms and enlarge positive ones by retaining a prefix of primes whose log product is in (λ−A log N,λ]. Thus

`S≤log 2+C((A+1)log N+S)^{2/3}`.

If S≤(A+1)log N this is the asserted bound; otherwise the inequality bounds S absolutely. Since log(N/B)≤S, the corollary follows. For bounded/small λ enlarge the absolute constants. ∎

**Imported-proof ledger.** The comparison uses KARY Lemma 2.1, Theorem 2.5, Corollary 2.6 and Theorem 4.1, together with EXCEPTIONAL_TWIN Theorem 2.3′, its singleton step and Lemma 2.1′. The elementary Euler/Rankin and cofactor reductions are KARY2 Lemmas 3.1 and 4.1; the local-moment identity is KARY3 Lemma 2.2. These are internally proved inputs, not externally refereed results. Opus R2 traced these proofs and found no fatal or major defect. Its minor repair retaining smoothness in the squarefull term is applied above. Finite checks in §5 do not certify the infinite proof.

**Scope and remaining gap.** This cap includes arbitrary balanced and prime-power native moduli, arbitrary real coefficients, Bonferroni, Selberg squares and CRT-evaluated moments, provided the final majorant covers the whole congruence avoider set. It does not include a rough-selector majorant that vanishes on the zero base, nor endpoint events with noncoprime endpoints, nor signed/position-sensitive rounding. At the end of Round 2 it left the log-log factor unresolved. Round 3 closes that architectural gap: both removing the factor and proving 3/4 require an exit from this native whole-avoider architecture.

## 4. Round 3 — the log-log loss is also intrinsic to this architecture

### 4.1 Attack: retain roughness instead of discarding it

Round 2 threw away a useful restriction: on the zero base every surviving modulus is W-rough. Let W grow with the level. The base costs O(W), but a one-dimensional upper-bound sieve now saves 1/log W in the shifted-divisor first moment. This yields a matching cap, including the log-log loss in the known I3 theorem.

**Theorem 4.1 (PROVED relative to the inputs of Theorem 3.1 and the classical fundamental lemma of the upper-bound sieve; Opus review SOUND).** Under the hypotheses of Theorem 3.1,

`log(1/Eν) ≤ C λ^{2/3}/(log λ)^{1/3}`.

Under the hypotheses of Corollary 3.2,

`log(N/(N Eν+Σ|a_i|)) ≤ C_A (log N)^{2/3}/(log log N)^{1/3}`.       (4.1)

**Assessment / consequence.** The existing I3_DEEP_ASTRA §8.8 bound attains this order within the native whole-avoider coefficient-sum architecture. Neither the 3/4 target nor removal of the log-log loss is possible **inside that architecture**. This is not a claim that either improvement is false for actual I3 exceptions.

### 4.2 Rough shifted-divisor bound with a uniform progression parameter

**Lemma 4.2 (PROVED relative to the classical dimension-one upper-bound sieve).** For W≥16, K≥W^{1000}, q≤K^{1/4}, and gcd(q,P_W)=1,

`T_W(q;K):=Σ_{K<m≤2K, q|m, gcd(m,P_W)=1}τ(m+1) ≪ K log K/(q log W)`,       (4.2)

with an absolute constant. If gcd(q,P_W)>1 the sum is zero.

*Proof.* Pair divisors of m+1 to bound τ(m+1) by twice the number of divisors d≤√(2K+1). Only gcd(d,q)=1 contributes. For each such d, solve `m≡0 mod q, m≡−1 mod d`; the solutions form one progression modulo qd, of length H=K/(qd)≥cK^{1/4}. For p≤W dividing d there is no forbidden residue, because m≡−1 mod p. For p≤W not dividing d there is exactly one forbidden residue of the progression index, because q is W-rough.

Use the standard upper-bound β-sieve fundamental lemma, in its dimension-one form (Halberstam–Richert, *Sieve Methods*, 1974, fundamental lemma; equivalently Friedlander–Iwaniec, *Opera de Cribro*, 2010). With fixed sieve parameter 20 it gives coefficients of absolute value ≤1 supported on squarefree r≤W^{20} dividing `∏_{p≤W,p∤d}p`, with upper main term at most C times

`V_d(W)=∏_{p≤W,p∤d}(1−1/p)`.

Its hypotheses are uniform in d: deleting primes only decreases the dimension-one product bound. Counting a residue of the progression index costs H/r with remainder of absolute value at most 1, so the sifted count is at most `C H V_d(W)+O(W^{20})`. Since V_d(W)≥c/log W and H≥cW^{250}, the error is absorbed uniformly. Mertens gives

`V_d(W) ≪ (log W)^{−1} ∏_{p|d,p≤W}(1−1/p)^{−1}`.

Finally

`Σ_{d≤z} (1/d)∏_{p|d,p≤W}(1−1/p)^{−1} ≪ log(2z)`

uniformly in W: expand the product as `Σ_{a|d,P⁺(a)≤W} μ²(a)/φ(a)` and use convergence of `Σ μ²(a)/(aφ(a))`. Summing C H V_d(W) over d proves (4.2). No distribution theorem for primes in a progression is used here. ∎

### 4.3 The improved smooth first moment

**Lemma 4.3 (PROVED relative to Lemma 4.2).** For W≥16 and y≥W^{1000}, with Γ as in §3.2,

`M_{D,W}(y):=Σ_{P⁺(m)≤y, gcd(m,P_W)=1}τ(m+1)Γ(m)/m`

`                 ≪ (log W)² +(log y)²/log W`,       (4.3)

uniformly in W and y.

*Proof.* The ordinary-mean and local-moment constants from §3.3 are uniform: Γ_W≤Γ_16 pointwise, and their Euler-product estimates use only h(p)≤2p^{−1/2}. First, for K≥W^{1000}, expand Γ=1*h and split e at K^{1/8}. For the small e, Lemma 4.2 applies to q=e and gives total O(K log K/log W), since Σh(e)/e is bounded. The large e tail is O(K^{1+ε−1/32}), by the same Rankin bound as §3.3 with cutoff K^{1/8}; it is absorbed uniformly since log W≤log K/1000. Thus the weighted rough ordinary mean on a dyadic block is O(K log K/log W).

For smooth blocks K≥y^{48}, repeat §3.3 retaining gcd(m,P_W)=1. In the local third moment D≤K^{1/16}. If D has a prime ≤W its term is zero. Otherwise expand Γ and split e at K^{1/8}. For small e, `[D,e]≤K^{3/16}≤K^{1/4}`, so Lemma 4.2 replaces the Shiu estimate and supplies 1/log W. The large-e sum is bounded by `C 2^3 K^{−1/32}` after extracting 1/D; the local-moment summation is unchanged. The squarefull term is still O(K^{4/5}), and all these power errors are absorbed into

`K log K/(log W) · (log K/log y)^{−3}`.

Uniform absorption follows from log W≤log K/1000 and u=log K/log y≤log K/log 2. Thus every smooth tail block has the old bound divided by log W.

For the body m≤2y^{48}, use the ordinary estimate of §3.3 below a cutoff 2W^{1000}, costing O(log²W); above it use the rough ordinary block mean just proved and partial summation, costing O(log²y/log W). Summing the smooth dyadic tail as in §3.3 costs O(log²y/log W). This proves (4.3). ∎

### 4.4 Matching cap and why this does not prove many exceptions

*Proof of Theorem 4.1.* In the base of §3.2 take `W=max(W₀,⌊λ^{1/2}⌋)` and pin all primes ≤W to zero modulo p. This costs O(W). The level still charges every prime >W₀: conditioning on the extra small coordinates can only reduce the remaining locality of the test. Explicitly, the ETw level measured over primes above the current W is at most λ, so the comparisons remain valid. Lemma 3.4 is uniform in W; the leak remains ≤1/2. Set

`s₀=(λ log W)^{1/3}`.

For sufficiently large λ, exp(s₀)≥W^{1000}, so Lemma 4.3 applies to every block used. Singleton costs are

`O(s₀²/log W+log²W)`.

For s=2^i s₀, d=⌊λ/s⌋, the block ratio in KARY Corollary 2.6 is at most

`C[1+s³/(λ log W)+s(log W)²/λ] ≤ C′(1+8^i)`.

The last inequality uses s₀³=λ log W and `s₀(log W)²/λ=o(1)`. The total block cost is O(λ/s₀+log²λ). Add the base O(λ^{1/2}), negligible compared with the claimed bound, to obtain

`log(1/Eν) ≪ λ^{2/3}/(log W)^{1/3} ≍ λ^{2/3}/(log λ)^{1/3}`.

The coefficient-sum statement follows from the same projection/coarsening as §3.5, now using the increasing sublinear function `f(x)=x^{2/3}/(log x)^{1/3}` in `S≤log 2+C f((A+1)log N+S)`. The two-case argument is unchanged. ∎

**Assessment / calibration.** The proof places mass on integers divisible by many small primes to demonstrate the unavoidable cost of a *globally valid majorant*. It does not assert that its comparison distribution is the distribution of integers in [1,N], nor that this fibre actually contains many total I3 zeros. Indeed the native congruence avoider set can be much larger than the set of genuine zeros: words with larger moduli remain available. The finite table in §5 makes that distinction visible.

### 4.5 Next attack: noncoprime endpoint events and actual interval information

**PROVED exact identity, not a new theorem.** Fix endpoints u,v≥3. The event `n≡−u−v mod uv` supplies a word once n≥3uv−u−v. Unlike native divisor classes, this event can be non-reduced: with u=v=3 it is n≡3 mod9. Thus it escapes the zero-base elimination. This is an actual door, not a claim that KARY is an impossibility theorem for I3.

**Assessment / attempt and exact stopping point.** Add all endpoint events with uv≤Y to the native events. Their unconditioned mass is still O(log²Y), but the needed low-cost base avoiding them is not furnished by §3.2. Pinning zero modulo p² removes u=v=p for odd p, but larger p-adic endpoint valuations introduce further classes; there is no uniform bound on required exponents in this attempt. Alternatively count simultaneous endpoint and divisor events directly in [1,N]. For any compatible tuple this is one progression of modulus `lcm(uv, t′u′−1, …)`, with count N/lcm+O(1). Paying those O(1)'s returns to the coefficient ledger. Reaching beyond it needs a signed aggregate error estimate when the combined modulus exceeds N, or another non-CRT interval theorem. Neither is established by a two-point divisor estimate, by the mean count, or by treating the atoms as independent. No untested hypothesis equivalent to the desired exceptional bound is proposed as progress.

**Assessment / log-loss removal outside the cap.** The rough-input 2/3 theorem in I3_DEEP_ASTRA §8.8 is not contradicted: its selector vanishes on the zero base. Recovering the all-integer estimate from it would require control of the inputs with many small factors without scaling I3 witnesses. I3(21)>0 but I3(42)=0 forbids the ES semigroup argument. A decomposition by smooth part does not fix this: substituting n=dm into a word requires divisibility conditions on endpoints or a level multiple of d, not just a word of m. That missing witness transport is left open.

### 4.6 ES₅/U port audit

**PROVED scope restriction / existing slot identities.** A native I3 hit is an ES₅ certificate only when one of t,u,v,tu−1,tv−1 is divisible by 4 (for n≡1 mod4 and gcd(n,uv)=1, equivalently the endpoint Jacobi product is −1; FOREST_DEEP_ASTRA Theorem 2.1 and LOWERTAIL_DEEP_FABLE §1.1–1.3). The unrestricted square word 121=3·5·9−5−9 has slots 3,5,9,14,26, none divisible by 4. Hence neither its class nor a sign-free I3 positivity theorem may be transported to U or ES₅ without a colour-compatible witness theorem. Restricting to 4|t makes the native detector a certificate family, but cannot increase its mass or defeat a cap already valid for the whole D-universe.

**Assessment.** No improved upper bound is available to port. The zero-base cap applies to that native certificate subfamily over all integers, not automatically to the full six-coordinate union U or to prime-only ES₅ sieves. The ES square floor survives those certificate restrictions, whereas I3 itself has both successful and unsuccessful squares. Numerator 8 requires its own divisibility condition (e.g. 8|t for the level identity); the I3 word of 241 has t=9 and is not an 8/241 certificate. No step here proves a false numerator-8 assertion.

## 5. Independent computations and calibration

**CERTIFIED finite scope.** `scripts/z50_i3ex_check.py`, output `data/z50_i3ex/checks.json`, passes under an 8 GB virtual-memory limit and 180-second timeout. Its memory is O(Y+N), Y=100,000 and N=1,000,000; it never constructs a Cartesian-product array. The source uses the existing 10⁹ zero list only for comparison, not for constructing witnesses or detecting the independently checked zeros. Existing z49 tests were inspected; they already cover the basic word/factor identities. The new checks target the native mass, zero-base elimination, exact conditional averaging, rough progression sums and the requested independent zero sub-range.

* Direct triple enumeration through 5,000 reproduces exactly 104 zeros (last 3,276), matching the restriction of the certified z48 list.
* Independent trial-divisor enumeration checks I3(2,433,600)=0, the square controls, and all 14 R-zero primes. It does not re-certify the full interval from 5,000 to 10⁹.
* All nine hard-prime controls have ordered counts 4,4,12,4,12,20,18,30,84 in the order 193,409,577,2521,3361,5569,9601,66529,8813281. All 14 R-zeros have interior words, including those not in this nine-prime list.
* At the square controls 49,1225,1600,19600,2433600, I3=0; at 121, I3=2 with word (3,5,9) and its swap. No tested square word has 4|t. Thus the mechanism neither assumes nor produces an I3 square floor.
* At 17, I3=0; at 241, I3=2, the words (9,4,7) and (9,7,4). Neither has 8|t. These checks are not a fresh proof of the independently certified failure of 8/n; no arbitrary I3 word is treated as a numerator-8 certificate.

**CERTIFIED class/fibre checks.** All native labels at every M≤100,000 are distinct and coprime to M; the program verifies their word reconstruction above onset and 730,684 small-prime incompatibilities with the zero base. A toy family with k≤4 and 13≤q≤101 has 176 atoms. On all 12 fibres modulo lcm(1,2,3,4), active same-q residues are distinct, and exact rational arithmetic verifies that the average conditional mass equals Σ1/(kq). Its fibre means range from 1.038 to 2.822. Complete CRT-period avoidance is checked for native cutoffs B=8,12,16:

| B | Period | Avoiding residues |
|---:|---:|---:|
| 8 | 8 | 7 |
| 12 | 88 | 63 |
| 16 | 9,240 | 5,418 |

**EVIDENCE, not asymptotic certification.** Native total mass divided by log²Y is 0.187, 0.272, 0.321, 0.354 at Y=10²,10³,10⁴,10⁵. At Y=10⁵ the total mass is 46.879; restricting moduli to have no prime ≤W gives masses 22.516,17.969,13.305,10.242 for W=5,11,31,101. This supports rough depletion, but these values do not test Lemma 4.2's astronomical K≥W^{1000} range or establish its constant. Toy rough progression sums at K=4096 check the divisor-switching inequality exactly and give normalized sizes; forbidden q sharing a prime with P_W give exactly zero. Smooth partial sums are also saved, but are lower bounds on the infinite smooth sum, not numerical verifications of its asymptotic upper bound.

**CERTIFIED truncated avoiders versus actual exceptions.** To avoid false positives below witness onset, compare only n∈[3B,10⁶], using all native moduli ≤B. The true-zero column comes from the previously certified 10⁹ list, with the limited fresh rechecks stated above.

| B | Lower endpoint | Native congruence avoiders | Actual I3 zeros |
|---:|---:|---:|---:|
| 32 | 96 | 250,411 | 57 |
| 128 | 384 | 23,943 | 26 |
| 512 | 1,536 | 1,492 | 14 |
| 2,048 | 6,144 | 81 | 5 |

The shrinking avoider set remains larger than the true exceptional set. No finite cutoff or observed absence of zeros establishes eventual positivity.

**Comparison of all exponent scales with empirical E₃.** Let L=log N. The last three columns are only the scales in the existing upper bound / matching cap, the weaker Round-2 cap, and the requested 3/4 target. Their unknown constants and thresholds prevent numerical testing of the asymptotic inequalities. In particular the cap is not an assertion that log(N/E₃(N)) is bounded by these scales.

| N | Certified E₃(N) | log(N/E₃(N)) | L^{2/3}/(log L)^{1/3} | L^{2/3} | L^{3/4} |
|---:|---:|---:|---:|---:|---:|
| 10³ | 93 | 2.375 | 2.912 | 3.627 | 4.261 |
| 10⁴ | 109 | 4.519 | 3.368 | 4.394 | 5.287 |
| 10⁵ | 111 | 6.803 | 3.785 | 5.099 | 6.250 |
| 10⁶ | 111 | 9.106 | 4.173 | 5.758 | 7.166 |
| 10⁷ | 112 | 11.400 | 4.538 | 6.381 | 8.044 |
| 10⁹ | 112 | 16.005 | 5.213 | 7.545 | 9.713 |

Reproduction:

```sh
ulimit -v 8000000
timeout 180 uv run python scripts/z50_i3ex_check.py
git diff --check
```

The exact arithmetic, count and identity checks are CERTIFIED; floating-point mass profiles and the interpretation of trends are EVIDENCE. None of this replaces the proof or hostile review of the cap.

## 6. Literature and final hostile-review ledger

### 6.1 Fresh literature check, 2026-10-29

**Verified source statements, not a priority claim.** Searches used the phrases `Erdos Straus exceptional set 2026 Vaughan Pomerance Weingartner` and `"Erdos Straus" "exceptional" "2026" bound improvement`. The attempted exact I3 numeric-string query returned HTTP 422 and is not counted as a successful search. The following pages were actually visited, rather than inferred from snippets:

1. Pomerance–Weingartner, [arXiv:2511.16817v2](https://arxiv.org/html/2511.16817v2), revised 2026-01-15. Introduction: the exception count “has been strongly improved, though not recently”, immediately followed by Vaughan's 1970 `N exp(−c(log N)^{2/3})` estimate. Theorem 1.3 gives `N exp(−C(log N)^{2/3}/φ(m)^{1/3})` uniformly for 4≤m≤(log N)². This verifies the supplied benchmark, not an I3 witness map.
2. Carl Pomerance, [*The Erdős–Straus Conjecture*, Alladi 70 conference, March 20, 2026](https://math.dartmouth.edu/~carlp/esconjfl.pdf). Slide 16 still states Vaughan's 2/3 estimate; slides 13–14 display the ratio identity that certifies Egyptian fractions but does not give an interior word of n.
3. Xinyang Jiang, [arXiv:2609.09204](https://arxiv.org/abs/2609.09204), *Counting Type I and Type II solutions of the Erdos-Straus equation: concentration, local obstructions, and a pointwise comparison*. The search surfaced it as a September 2026 candidate. The abstract page explicitly says **withdrawn**, with comment “some errors”; v2 withdrawal dated 2026-09-13. The HTML route returned 404/withdrawn. It is not used as a theorem or evidence of an exceptional-exponent improvement.

**Assessment.** This fresh search found no verified post-2025 improvement applicable to I3. It is not an exhaustive literature survey or a novelty claim beyond the repository. The original Vaughan proof was not freshly accessed; the published benchmark is verified through the sources above. The internal ES 3/4 note remains separately labelled internal/unrefereed and does not transfer to I3. Shiu and the standard dimension-one upper sieve are the classical analytic inputs; no GRH, EH, Dickson or OAI hypothesis is assumed.

### 6.2 Cross-model review ledger

All three reviews were fresh `subagent` calls in **deep mode** to **anthropic/claude-opus-5-5**. The exact requested identifier `anthropic/claude-opus-5-5:high` failed resolution (“not available”); the same model without the suffix succeeded. No review is falsely attributed to the unavailable identifier or to a particular unverified reasoning-effort setting. Each review was requested immediately after its claimed proof section was committed.

| Review | Commit reviewed | Verdict | Repairs incorporated |
|---|---|---|---|
| R1, native supply | 556de953 | SOUND; no fatal/major | Corrected square witness to 121=3·5·9−5−9; made zero-base failures for selectors/endpoints explicit. |
| R2, 2/3 cap | edb2a757 | SOUND; no fatal/major | Retained smoothness in squarefull error; expanded imported-proof dependency ledger. |
| R3, matching log-loss cap | 04219ba3 | SOUND; no fatal/major | Stated upper-sieve support/remainders and uniformity; clarified current-W level; restricted Jacobi equivalence to n≡1 mod4. |

Review sessions (under this worktree's pi archive):

* R1: `2026-10-29T14-32-27-801Z_01a18813-9799-7257-8abe-32f8cb2374b7.jsonl`.
* R2: `2026-10-29T14-42-56-868Z_01a1881d-30e4-7257-8abe-32fccaa05477.jsonl`.
* R3: `2026-10-29T14-57-14-059Z_01a1882a-454b-7257-8abe-33013f2c523f.jsonl`.

R2 re-derived the cited KARY/ETw comparison inputs and the Shiu moment bounds. R3 independently checked the rough shifted-divisor sieve, growing base and optimization, and reran the saved script byte-for-byte. Suggested statements beyond the proved scope were not silently adopted. All results remain internal and unrefereed.

### 6.3 Final labelled outcome and exact gap

**PROVED, relative to the named classical and internally proved inputs:** every native whole-avoider coefficient-sum CRT method has saving at most `C_A(log N)^{2/3}/(log log N)^{1/3}`. The previous native I3 exceptional-set proof attains that order. This is a new I3 barrier theorem for a family not covered by the ES forced-class caps; it does not claim a cap for the full union of the ES and I3 class universes. The crucial new arithmetic is the zero base and rough shifted-divisor mass. The arithmetic-free comparison is inherited.

**NOT ACHIEVED:** no new exceptional-set upper bound, no 3/4 exponent, no power saving, no removal of the log-log loss for actual I3 exceptions, and no positive ES₅/U port.

**OPEN, exact gap:** use noncoprime endpoint events or another non-native class family with a proved transfer, prove genuinely non-CRT signed interval information beyond coefficient-wise O(1) errors, or handle smooth inputs without the false I3 scaling rule. For ES₅/U, additionally enforce the colour/slot restriction; an unrestricted interior word is insufficient. The cap rules out none of these doors.

**CERTIFIED:** the finite checks in §5 pass. **Review verdict:** SOUND after minor repairs, three cross-model rounds. The original wrap-up above is supplemented and its U/ES₅ port limitation corrected by §7.

## 7. Parent follow-up — U and ES₅ are also quadratic-profile families

### 7.1 Boundary levels, colour and the relevant class universe

**PROVED dictionary / scope.** Work on n≡1 (mod4). Define ES₅ at composite inputs by existence of a positive word with a 4-divisible slot, equivalently a coordinate in 𝒞_n; no coprimality is needed for this slot/coordinate equivalence (LOWERTAIL_ROUND2_FABLE Theorem 1). The Jacobi interpretation additionally requires gcd(n,uv)=1. U uses an endpoint in 𝒞_n and its proper-divisor convention. For fixed t,u≥1 put A=tu−1. When A≥2, every possible word lies in `n≡−u mod A`, where u|A+1 and gcd(u,A)=1. There are at most τ(A+1) labels, including t=1,2 and u=1,2; duplicate residues are discarded. The case A=0 gives n=−1. If A=1, (t,u) is (1,2) or (2,1); at n≡1 mod4 neither word has a certificate slot. Thus no certificate is lost by A≥2.

The endpoint/coordinate predicates are determined by n mod 8A: v=(n+u)/A mod8 is determined there. Retain exactly those of the at most eight refinements of each native class which have n≡1 mod4 and satisfy the U or ES₅ predicate. Positivity and U's proper-divisor requirement hold sufficiently far along each retained class; finite initial points are not used as certificates. Every genuine U/ES₅ word is represented in this universe. In particular the family has at most 8τ(A+1) classes of modulus 8A, and each retained class is reduced at every odd prime dividing A. This is a statement about the native congruence presentation; it does not identify every possible sufficient congruence for U or ES₅ with this presentation.

### 7.2 Corollary — the matching cap transfers on n≡1 mod4

**Corollary 7.1 (PROVED relative to the inputs of Theorem 4.1; pending hostile review).** Let F be any finite family of the U or ES₅ refinements just defined, or any mixture of them. Let ν be a finite congruence combination, nonnegative on n≡1 mod4 and ≥1 on the entire F-avoider set in that progression. Measure its level above the same fixed W₀ as before. Then

`log(1/E₁ν) ≪ λ^{2/3}/(log λ)^{1/3}`,

where E₁ is Haar mean conditional on n≡1 mod4. Consequently the same coefficient-sum architecture, with family primes ≤N^A, cannot save more than `C_A(log N)^{2/3}/(log log N)^{1/3}`. In particular its exponent cannot exceed 2/3. The weaker cap of Theorem 3.1 also follows.

*Proof.* A literal zero base would be wrong here because it pins n even. Instead, at 2 choose uniformly the unit-square residues modulo the full 2-power of the common period (include 8); this has density 1/8 and lies in n≡1 mod8. At each odd p≤W pin n≡0 mod p. The base costs O(W), lies inside n≡1 mod4, and has bounded 2-adic inflation: probability of a specified residue mod2^a is at most 8/2^a. All classes with an odd p≤W dividing A are killed by reducedness. The remaining classes supported only at 2 are killed by the 2-adic square base: if one contained a unit-square residue, it would contain arbitrarily large odd integer squares, contradicting the known square obstruction for U/ES₅. Thus every surviving class is decided at an odd top prime >W.

In §§3–4 use Γ(2^a)=8, Γ(p^a)=1 for odd p≤W, and the previous capped factor above W. The single fixed Euler factor at 2 changes only absolute constants: h(2)=7, while h(p)≤2p^{−1/2} for p>2. In the local-moment tail bound, its factor `1+7·2^{1/4}` replaces at most one factor bounded by 2. Refining modulus A to 8A and taking at most eight labels per divisor likewise costs only constants in the first and second moments. The cofactor sums are the same sums with the fixed factor 8 removed from the cofactor. Lemma 4.2 now sieves only odd primes ≤W; q may be even, and its proof is unchanged since q is coprime to all the sieved primes. Hence the smooth first moment remains `O(log²W+log²y/log W)`, and the leak bound stays uniform in W. Take W=⌊√λ⌋ and repeat §4.4. Extending ν by zero off n≡1 mod4 multiplies it by a fixed modulus-4 selector and changes neither its charged level nor its coefficient-sum order; Eν=E₁ν/4. The projection/coarsening argument then proves the integer-count version. ∎

**Contrast and qualification.** This is a 2/3 cap for native U/ES₅ whole-avoider CRT methods, even allowing t=1,2, arbitrary balanced moduli, and the colour refinements. ES's internal 3/4 upper bound uses the larger Vaughan **ratio** family and a rough-input selector followed by multiplicative scaling; neither is included in this corollary. There is no contradiction. Nor does Corollary 7.1 cap methods restricted only to prime inputs: its odd-prime zero base is not a unit base. A square base is available for a separate prime-law audit, but that stronger scope is not claimed here.

### 7.3 The §8.8 upper bound transfers as well

**PROVED relative to BV, Brun–Titchmarsh and Mertens.** For failures among n≡1 mod4,

`E_ES₅(N) ≤ E_U(N) ≪ N exp(−c(log N)^{2/3}/(log log N)^{1/3})`.

*Proof sketch with exact change.* In I3_DEEP_ASTRA Lemma 8.7 and Theorem 8.8 retain only atoms with u≡0 mod4. The multiplier set B consists of y-rough k≤K (including 1), hence all k are odd. On the fibre c, active labels satisfy u≡−c mod k and u≡0 mod4. For (c,k)=1 this is one progression modulo 4k, so its harmonic mass is `log(z/U₀)/(4k)+O(U₀^{−1})`; the reciprocal-totient upper sum is bounded by the old unrestricted one. The lower BV main term is therefore still ≫x h(J_c) per prime block, up to an absolute factor, and the BV error is at most the original weighted error because the incidence function is only reduced. The prime progression q≡−k^{-1} mod u is reduced, since the active u is coprime to the odd k. Same-q distinctness and conditional independence are unchanged. Thus μ_c≍T h(J_c), with the same exceptional-fibre estimate, factorial-moment bound, even Bonferroni majorant and coefficient ledger `exp(O(T³/log T))` as §8.8. Every hit above n≥3KX has t,u,v≥3 and 4|u, hence is a U and ES₅ certificate at n≡1 mod4. Discarding the N^{o(1)} onset and choosing `T=α(log N log log N)^{1/3}` proves the estimate. No I3 scaling or arbitrary-word colour transfer is used.

**Assessment.** This is a transfer of the existing upper-bound architecture, not an exponent improvement. Together with Corollary 7.1 it identifies the optimal order for that native presentation of U/ES₅, up to constants. Squares remain exceptions but √N is smaller than this upper bound. The previous blanket statement in §4.6 that no U/ES₅ upper bound was available to port was too pessimistic: forcing the endpoint 4|u preserves the needed supply.
