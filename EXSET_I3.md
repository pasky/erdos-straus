# I3 exceptional sets — wave z50, lane E (`i3ex`)

## 0. Status and summary

Work in progress. ES and Conjecture I3 remain open. No improvement claimed at initialization.

| Item | Status | Result / exact gap |
|---|---|---|
| Prior-work and barrier audit | PENDING | Read source proofs, distinguish words of n from words of bn. |
| Round 1: native multiplier atoms | PENDING | Seek cubic supply, selector and coefficient ledger. |
| Round 2: transfer / I3 cap | PENDING | Audit KARY transfer; attack surviving gap. |
| Round 3: beyond CRT / port | PENDING | Test another route and state ES colour requirements. |
| Independent numerical checks | PENDING | Zero sub-range, truncated avoiders, controls. |
| Literature after 2025 | PENDING | Search and verify sources. |
| Hostile reviews | PENDING | Opus after each claimed advance. |

## 1. Source audit and scope

**Assessment / audit.** The binding z48, z49 and z50 context files were read in order (z50 twice). Source inspection includes FRONTIER §§2–4,6–7; BREADTH_Z45 §§1–14; the PR-B main note and both supplements; OAI_DUMP_IMPACT; I3_DEEP_ASTRA in full; summaries of the six z48 forest/lower-tail notes; DISCOVERIES (D)17–(D)31; and the actual KARY2/KARY3 base, moment and cap proofs. The 3/4 note's atom identity and assembly are audited rather than accepted as an I3 witness map. No OAI hypothesis is used.

**PROVED previously, not re-claimed.** Write E₃(N)=#{3≤n≤N:I3(n)=0}. I3_DEEP_ASTRA §8.8 proves

`E₃(N) ≪ N exp(−c(log N)^{2/3}/(log log N)^{1/3})`.

Its §8.7 proves that the Vaughan ratio identity gives a word of bn, not n, and that I3 is not closed under multiplication (21 has a word; 42 does not). The requested 3/4 theorem therefore needs new atoms or a new transfer; the ES scaling argument cannot be reused.

**Definition (native divisor classes).** Let D be the universe of classes

`C(t,u) = {n : n ≡ −u (mod M)},  M=tu−1,  t,u≥3`.

Each class is reduced: gcd(u,M)=1. Above n≥3M it supplies v=(n+u)/M≥3. At a fixed M its labels are the distinct divisors `3≤u≤(M+1)/3` of M+1. A family means a finite subset of these classes, with no restriction on factorisation or size of its moduli. Its avoider set means all integers avoiding all those congruences, not merely actual I3 zeros.

**Assessment / barrier scope.** D is not an ES forced-class subfamily: the class n≡−3 (mod 8), from t=u=3, contains the odd square 121. KARY2's unit-square base therefore fails. This does not refute its arithmetic-free comparison theorem. A replacement base is possible because every D-class is reduced: pin n≡0 mod every small prime, killing every native class with such a prime in its modulus. Sections 2–3 examine the resulting quadratic-mass rather than cubic-mass architecture. A cap on D alone will not automatically cover endpoint classes n≡−u−v (mod uv), selectors imposing roughness, or interval-only majorants; those scopes are kept separate.

**Assessment / novelty standard.** Dictionary identities and the mass calculation alone are not counted as exceptional-set progress. A genuinely new cap would have to check a new base, the smooth first moment, the leak uniformly in the cutoff, and the coefficient-sum projection. No numerical experiment or standard conjecture is promoted to a pointwise I3 result.

## 2. Round 1 — I3-native multiplier atoms

### 2.1 Quadratic supply rules out the requested cubic-supply lemma

**PROVED (elementary scope obstruction; not itself a new exceptional-set bound).** For Y≥8 the sum of Haar probabilities of all distinct D-classes of modulus ≤Y is O(log²Y). Consequently, if K≤X^κ with fixed κ<1/2, q∈(√X,X] is prime, and atoms are any distinct classes `n≡−u mod kq`, with `u|(kq+1)` and t=(kq+1)/u≥3, their total mass is O_κ(log²X). There cannot be conditional mass ≥c(log X)³ on a set of fibres of Haar probability bounded below, or even of probability ≫1/log log X.

*Proof.* The number of labels at M is at most τ(M+1). Divisor hyperbola counting gives `Σ_{M≤z}τ(M+1)≪z log(2z)`; partial summation gives `Σ_{M≤Y}τ(M+1)/M≪log²Y`. A modulus kq≤KX has only one prime factor in (√X,X], since k<√X, so different multiplier labels do not duplicate its q. Summing probabilities gives the assertion. For any conditioning, the average conditional hit count is the original mean. If mass ≥cT³ on a fibre set of probability b, then `b cT³≤CT²`, hence b≪1/T. ∎

**PROVED consequence for the proposed selector.** The standard selector `S_y=1[(n,P_y)=1]`, with y a fixed power of T=log X, has Haar probability `∏_{p≤y}(1−1/p)≍1/log T` (Mertens). Conditional on S_y=1, the mean of the native count is at most `O(T² log T)=o(T³)`. Thus cubic supply on all but an exponentially small proportion of these selector fibres is impossible. This does not exclude another I3 atom family or a non-CRT argument.

**Assessment / exact failure.** Splitting u or t into extra factors produces multiple labels for the same residue, not additional distinct classes. A count with duplicated labels cannot be fed into the independent-Bernoulli Bonferroni argument as though the labels were separate shots. The extra factor in the ES note comes from distinct ratio labels; §8.7 of I3_DEEP_ASTRA explains why those ratios give words of bn instead of n.

### 2.2 First attack on the surviving gap

**Assessment / candidate, not yet a theorem here.** Replace the failed cubic supply by an audit of the full D-universe. For fixed W, pin n≡0 modulo `P_W=∏_{p≤W}p`. All native classes with a prime ≤W in their modulus disappear. The remaining prime coordinates are independent initially, and their capped sequential laws have inflation factors `(1−p^{−1/2})^{−1}`. If the first moment is O(log²y), the KARY block balance is `s²≈λ/s`, giving a 2/3 cap rather than 3/4. This demands a new smooth shifted-divisor estimate and a leak bound uniform in W; they are supplied, or rejected, in Round 2. The abstract comparison theorem is not by itself an arithmetic cap.

**Review status:** hostile cross-model review requested after this section; verdict to be recorded in §6.

## 3. Round 2 — the surviving transfer gap

Pending.

## 4. Round 3 — further attack and ES port

Pending.

## 5. Independent computations and calibration

Pending.

## 6. Literature and final hostile-review ledger

Pending.
