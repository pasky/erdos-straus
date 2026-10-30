# Hostile referee report: EXSET_LINNIK §§1–3

Reviewed 2026-10-29. Sections 4–8 are excluded. Reference checkout at report preparation: `17a46398b6d8dc27f509ee1b48b6a18409af1a9b`; reviewed `EXSET_LINNIK.md` SHA-256: `5512ad25fc6ef33ea1c537672de4412781fdab85bc03dfd8852dcb3b6a4c8335`.

**Overall verdict: MAJOR revision; Theorem 2.10's advertised universal conclusion is FATAL as stated.** The sparse-plane obstruction survives elementary repairs. The Heath–Brown exponent upgrade also survives, but its stated corollary does not follow from the stated bias theorem. Neither result establishes an ES exceptional-set power saving. ES remains open.

Verdicts distinguish a false/unsupported claimed scope (**FATAL**) from a substantially repairable argument (**MAJOR**), local errors (**MINOR**), and a verified claim within its hypotheses (**SOUND**). In particular, FATAL below does not mean every ingredient is false.

## 1. Lemma 1.2 — MINOR for the transfer; MAJOR for the pointwise interpretation

**What is sound.** For nonzero `a` and `T>0`, summing nonnegative biases proves `#B≤Δ/T`. Exact containment gives the claimed bound on `E`; approximate containment gives the same bound plus its exceptional remainder. If the numerical bound `Δ/T≤X^{1−c}` is being used and `Δ≥X`, then necessarily `T≥X^c`.

**What is not sound as written.** The permitted input `#(E_X\B)≤X^{1−c}` is not “literally” the universal implication P(a,T). It allows exceptional primes outside B. This matters later: the document repeatedly turns an allowed almost-everywhere implication into a necessary pointwise theorem. A generic larger-sieve argument is also not a datum of Definition 1.1, as §1.1 itself acknowledges.

The Cauchy bound is correct, but the deduction about support requires a prime actually required to have `β_p≥T`; an empty B/E does not force a large support. Add `a≠0` throughout to make normalization meaningful.

**Repair.** Separate exact and approximate transfer statements. For approximate transfer, P holds outside a specified remainder, not at every prime. State the support obstruction for a nonempty required high-bias set, and do not apply this lemma to L5 without a separate reduction.

## 2. Equation (1.1) and its interpretation — SOUND / MAJOR scope correction

For distinct odd squarefree n,n′, `(x/n)(x/n′)` is a nontrivial sign character on at least one odd-prime unit coordinate. Conditioning on `x≡1 mod 8` does not affect those coordinates. Thus the characters, including n=1, are orthonormal, and the second-moment identity and Markov bound are correct.

Two surrounding statements need correction:

* **CRT level is not total period.** The standard z50 framework bounds each summand modulus's charged radical level. The lcm of many such moduli can be exponentially larger than every individual modulus. “CRT methods need period ≤N^{O(1)}” is not the definition in EXSET_SIEVE_MASS Theorem 3.2. This same confusion reappears in Proposition 2.8.
* **Squares are not automatically in every B(a,T).** A square coprime to the support has all symbols +1, but then its value is `|Σa_n|²/‖a‖²`, which can be zero for signed coefficients. Ordinary odd squares need not even be coprime to every n. The square-floor illustration is valid for coherent nonnegative coefficients and the appropriate threshold, restricted to coprime squares, not for an arbitrary datum.

**Repair.** Retain (1.1); distinguish whole-period complexity from per-term level and qualify the square example.

## 3. Proposition 2.2 — MAJOR proof correction; fixed-order result survives

### 3.1 Missing compatibility and normalization

Nonempty U does not imply there are primes in U with `p≡1 mod k`. For example, `k=3`, `U={2 mod 3}` gives an empty averaging population. Require a compatible unit class modulo `lcm(k,L)` and `a≠0`. Discarding the finitely many ramified primes is harmless.

### 3.2 Frobenius lies in a coset, not Gal(K/F)

Let `G=Gal(K/Q)`, `H=Gal(K/F)`. Fixing the restriction `r` to F selects the coset `C_r=g₀H`. It does not make rational-prime Frobenius equidistributed in H. Moreover, Chebotarev averages conjugacy-invariant functions; there is no canonical labeling of “each of the φ(k) characters” across rational primes.

This is not merely terminological. Take `k=4`, `S={2}`, `L=8`, so the author's F is `Q(ζ₃₂)`, and prescribe `p≡5 mod 32`. On H the multiplier of `2^{1/4}` belongs to `{±1}`; on the prescribed coset it belongs to `{±i}`, because r negates `√2`. Substituting H for the coset gives a wrong value for the square of that multiplier.

Nevertheless, the second moment being claimed does survive. For `m=n/n′`, choose the positive real kth root and write its multiplier as `ψ_m(g)`. On the coset, and for a faithful exponent t,

`mean_{h∈H} ψ_m(g₀h)^t = ψ_m(g₀)^t mean_{h∈H} ψ_m(h)^t = 0`

when `n≠n′`, because the character on H is nontrivial. Sum over all faithful t before applying rational-prime Chebotarev: this sum is conjugacy invariant. The diagonal contribution is φ(k)‖a‖².

The identification with multiplicative characters is otherwise right: at a prime ideal above an unramified rational prime `p≡1 mod k`, the Frobenius multiplier of `n^{1/k}` reduces to `n^{(p−1)/k}`; choosing a primitive kth root identifies this with an order-k character. Changing choices permutes the faithful characters, leaving β invariant.

### 3.3 Schinzel is being used correctly in this restricted situation

Schinzel, *Abelian binomials, power residues and exponential congruences*, Acta Arith. 32 (1977), Theorem 2, states the abelian-binomial criterion using the number of kth roots of unity in the base field. Over Q this gives `m²∈Q^{×k}` as a necessary condition (and the stronger `m∈Q^{×k}` for odd k). A valuation ±1 in the ratio of distinct squarefree integers contradicts this for k≥3.

There is an elementary proof avoiding the citation: if the positive root `α=m^{1/k}` belongs to the abelian field F, then `Q(α)/Q` is Galois and real. Its conjugates can only be the real roots ±α. Therefore `α²∈Q`, so `m²∈Q^{×k}`, impossible here. Positivity and squarefree support are essential to this simple argument.

### 3.4 Density

For fixed k, S and L, β is a finite-valued conjugacy-invariant Frobenius function. Chebotarev gives relative **natural prime density**, hence Dirichlet density too. The document's Dirichlet-density statement is not too strong; it can be strengthened. The ≤2φ(k) sublevel set has relative density at least 1/2. In fact a mean of φ(k) already excludes an eventual universal lower bound `T>φ(k)`.

There is no uniform assertion about primes up to X when the fields and progressions grow with X.

**Repair.** State the compatible fixed-order theorem, replace the subgroup assertion by the coset calculation, and apply Chebotarev to the sum over faithful characters rather than arbitrarily labeled individual characters.

### 3.5 Consequences (a), (b), and “order ≥3 entirely” — FATAL

These consequences go far beyond the repaired proposition.

**Wrong Parseval sign.** Put `M=|𝒜|` and let `C_p` count ordered congruent pairs in 𝒜. With p coprime to its elements,

`β_add = pC_p/M − M`,

`β_mult = (p−1)C_p/M − M`.

Consequently the correct identity is

`β_add = [p/(p−1)] β_mult + M/(p−1)`,

not the displayed formula with a minus sign. Already `𝒜={1}` detects the error.

**Fixed order is not the full varying-order spectrum.** For `𝒜={1}`, the sum over characters of order ≥3 is exactly `p−3`. Thus a nonquadratic aggregate has an arbitrarily large eventually universal lower bound on every unit progression, despite each fixed-order mean being exactly φ(k). This baseline alone is not an ES power-saving argument, but it decisively invalidates the claimed inference “the only certifiable part is the quadratic one.” Chebotarev for fixed k does not handle the unbounded list of orders dividing p−1.

**Squarefree support cannot be dropped.** Take `k=4`, distinct primes `q₁,…,q_M`, and `a=1_{ {q_i²} }`. For every prime

`p≡1 mod (8q₁⋯q_M)`,

all quartic characters have `χ(q_i²)=(q_i/p)=1`, so `β_p^(4)=2M`. This is an exact CRT-certified, arbitrarily large fixed-order bias. It is outside Proposition 2.2 but inside the blanket nonquadratic language of §§1.4/2.10.

**Gallagher does not require polynomial-index occupancy.** Its displayed inequality requires a positive denominator, not `ν_p≤p^{1−δ}`. For example, the squares in [1,N] occupy at most `(p+1)/2` classes. Using primes up to `Q=N^{3/4}` gives denominator `2 log Q−log N+O(1)`, positive of order log N, and an `O(N^{3/4}/log N)` bound. No higher-order character confinement is involved. Nor does small occupancy of a truncated product set imply containment in a small subgroup: `{1,2}` occupies two classes mod 11 but generates the full multiplicative group.

Even actual subgroup confinement with index `d(p)≥p^δ` need not have a common fixed divisor k≥3 as p varies. The proposition does not address this.

**Repair.** Delete the universal larger/additive/multiplicative-sieve exclusion. Retain only the fixed-order, squarefree-support obstruction, or a separately stated finite sum of fixed orders with its correct baseline threshold.

## 4. Lemma 2.3 — MINOR repairs; asymptotic counting result survives

### (a) W1 correspondence — SOUND, with endpoint bookkeeping

Since `gcd(u,M)=1`, the residue −u is automatically a unit modulo h. Compatibility with the fixed Π-free coordinates is exactly `m|(u+1)`. The complementary divisor `t=(hm+1)/u` then also satisfies `t≡−1 mod m`; setting `a=(u+1)/m`, `b=(t+1)/m` gives precisely `h=mab−a−b`. The reverse construction is valid.

Retain the W1 convention `M=hm≥2` in the converse. Otherwise, at h=1 the word `(m,a,b)=(1,2,3)` produces the excluded pivot M=1. For h>1 this caveat is automatic.

The independent definition-based check below confirms the correspondence, without importing the author's enumeration routines.

### (b) W2 parametrization — MINOR: explicit false inequality

The intersection criterion, unitary splitting, factorization, and exclusion of noncoprime endpoints are correct. But

`D≤h+1`

is false. For every h, choose `u=1`, `v=h`, `m₁=m₂=1`. Then `m=1`, `D=h+2`, and the W2 class `n≡−1 mod h` meets the plane. At h=11 this gives `D=13>12` and `(Dm₁−h₂)(Dm₂−h₁)=24>2h+1=23`.

**Repair.** Use `D≤h₁+h₂+1≤h+2` and `f₁f₂≤2h+2`. Positivity follows from `Dm₁−h₂=(h₁m₁+1)/m₂>0`, and symmetrically. The supplied script already uses a cutoff based on `2h+2`, so its passing self-check does not verify the printed `h+1` inequality.

### (c) Counting — MINOR: unbound split variables and the same off-by-one

The displayed W2 term contains h₁,h₂ without binding them by a sum or maximum over unitary splittings. A clean valid upper bound is

`2 Σ_{a≤1+√(h+1)} τ(h+a)`

`+ Σ_{h₁h₂=h, gcd(h₁,h₂)=1} Σ_{f≤√(2h+2)} [τ(f+h₁)+τ(f+h₂)]`.

For each splitting, choose which f_i is the smaller factor and then a divisor D of `f+h_j`; this determines the remaining parameters. This may overcount, which is harmless. The ordinary divisor bound gives `≪_ε 2^{ω(h)}h^{1/2+ε}`, as claimed. The W1 smaller-endpoint estimate is also correct.

Refinements do not create an uncontrolled multiplicity on the plane: modulo 8M or 4uv the additional constraint is 2-adic, and the plane fixes that coordinate. Each original class has at most one compatible refined intersection, with the same h-box. State this explicitly. These counts are upper bounds on classes/labels; duplicates of a box do not hurt the union bound.

## 5. Lemma 2.4 — MINOR proof omissions; parity law SOUND

The claimed parity law survives hostile checking, including the 2-part and refinements.

**W1 identity.** Write `M=tu−1`, `M*=tv−1`. Since `MM*=tn+1`, their Jacobi symbols at n multiply to 1. Once coprimality holds, each symbol is ±1 and hence they are equal. Also `uM*=n+v` gives `(u/n)(M*/n)=(v/n)`, so

`(M/n)=(M*/n)=(uv/n)`.

**Coprimality needs justification, not merely “the plane point is a unit.”** An integer in a finite cylinder need not be a unit at primes not dividing its modulus. For W1, explicitly choose a sufficiently large n in the refined cylinder and coprime to u, adding finitely many CRT conditions. This is possible because `gcd(u,M)=1`; the only possible added overlap from refinement is at 2, where n is already odd. Then `Mv=n+u` forces `gcd(n,v)=1`. A common divisor of u and v divides n, giving `gcd(u,v)=1`. For W2, the unit residue modulo uv already supplies the needed coprimality. Take n large enough to have a genuine positive word/edge and to avoid degenerate endpoints.

Theorem A in FOREST_DEEP_FABLE explicitly covers odd composite n≡1 mod 4 under exactly these two gcd conditions. Its use here is valid after that selection.

**2-part and reciprocity.** With `n≡1 mod 8`, `(2/n)=1`. Remove powers of 2 from the pivot, use n≡1 mod 4 in reciprocity, and use `n≡1 mod m′`. The resulting symbol is exactly `(c/h)`, including nonsquarefree h. Thus `(c/h)=−1` excludes square h and h=1.

**U certificates.** The cited Theorem B is stated for primes, whereas the selected n can be composite. Do not silently extend its statement. The needed extension is elementary: an endpoint divisible by 4 already supplies a slot; if u≡7 mod 8, then `v(tu−1)=n+u≡0 mod 8`, so either v or tu−1 is divisible by 4. This proves the required U→ES₅ slot implication at every selected n≡1 mod 8.

**Repair.** Insert the CRT coprimality selection and the direct U-slot argument. Refinements preserve the slot predicate and only restrict the class, so they cause no additional problem.

## 6. Theorem 2.5 — SOUND after Lemma 2.3's local repairs

A unit residue box modulo h has measure `1/φ(h)`. The corrected counting bound gives the stated convergent Euler-product majorant. For q≥11 and ε≤1/8,

`Σ_{k≥1} q^{k(1/2+ε)}/φ(q^k)`

`= [q/(q−1)] q^{−1/2+ε}/[1−q^{−1/2+ε}] ≤ 2q^{−1/2+ε}`.

The inequalities `∏(1+4q^{−1/2+ε})≤exp(4σ_ε)` and `exp(4σ_ε)−1≤8σ_ε` for σ_ε≤1/4 are valid. The choice of η₀ gives covered measure ≤1/2. Countable subadditivity is sufficient; independence of certificate boxes is not assumed.

**Missing sentence.** h=1 is omitted from the sum because Lemma 2.4 rules out certificate boxes there. Thus the theorem depends on the parity law as well as Lemma 2.3, unless one separately checks h=1 directly.

**Not proved by this theorem:** every sign pattern has a sterile representative. Total sterile mass ≥1/2 does not imply that. See Remark 2.7 below for a repair with a smaller sparsity constant.

## 7. Corollary 2.6 — SOUND in its exact, infinite-range scope

For nonzero squarefree-supported a, the sign orthogonality is exact. If Z has measure at least 1/2, then

`∫_Z |Σa_n(x/n)|² dμ ≤ ‖a‖²`

forces a point of Z with value at most 2‖a‖². The integrand depends on finitely many sign vectors, so there is no subtle essential-infimum issue. Strict `T>2` gives a strict low-bias witness.

For finite 𝔊, include 8, every **refined class modulus**, and every support prime in L. The chosen plane point gives a reduced residue modulo L. Both avoidance and the quadratic profile are fixed on that class; Dirichlet's theorem gives infinitely many primes in it. Thresholds of word classes do not invalidate this negative result: the primes are outside the classes themselves, not just below their certificate thresholds.

**Family audit.** The families in EXSET_SIEVE_MASS Definition 1.2 are indeed the refined native W1/W2 families used here, with u=1 allowed and the specified 2-adic intersections. Nonunit W2 classes cannot meet the plane. On the n≡1 mod 8 plane, U's endpoint condition gives an ES₅ slot as above. The union `𝔉₅∪𝔘` is a legitimate, possibly redundant, family for the negative result. It is not the family of all possible ES certificates, nor the full ET/Vaughan ratio family.

**Repair/qualification.** Add a≠0, and explicitly distinguish the periodic extension of B from the initially defined set of primes p≤X. Do not promote “infinitely many primes” to “a counterexample in (X/2,X]” for growing data. Do not apply this corollary to dense Π failing its sparsity hypothesis.

## 8. Remark 2.7 — MAJOR qualification; exponent arithmetic itself correct

Put `b=1/2−ε` and `s=|Π|`. Then

`log s = Ab log log X + O(1)`,

`log r = log log X − log log log X − log A + o(1)`.

Consequently, when s≥r,

`log (s/r)^r = (b−1/A+o(1)) log X`.

The claimed exponent `1/2−ε−1/A` and the resulting bound `X^{1/2+1/A+ε+2ε′+o(1)}` are correct.

**But A>2 alone is insufficient for an already fixed ε.** One needs

`ε < 1/2−1/A`, and `2ε′ < 1/2−1/A−ε`.

For example, A=2.1 and ε=1/8 meet the preceding printed ranges but give s<r eventually, an empty product set and an undefined normalized datum. Choose ε after A, sufficiently small. The dyadic block has enough primes for the proposed sparse selection by PNT.

**Unsupported final assertion.** “Every sign pattern being realised by sterile points” does not follow from Theorem 2.5. It is also unnecessary for Corollary 2.6, which supplies a low-bias sterile point separately for each a.

There is a plausible elementary strengthening: conditional on a full sign pattern, a compatible h-box has mass `2^{ω(h)}/φ(h)`. Redo the union bound with `4^{ω(h)}` rather than `2^{ω(h)}` in the summand; its Euler product is bounded using `exp(8σ_ε)`. Shrink η₀ accordingly. This yields uniform positive sterile measure in every sign cell, but it must actually be stated and proved; the currently advertised η₀ is not justified for that stronger conclusion.

**Repair.** Add the ε inequalities, and either delete the sign-pattern sentence or prove the strengthened conditional union bound with a suitably smaller constant.

## 9. Proposition 2.8 — MAJOR: repairable whole-period lemma, not the advertised standard-level barrier

### 9.1 The two different levels

EXSET_SIEVE_MASS Theorem 3.2 assumes

`Σ_{ℓ|d_i, ℓ>W} log ℓ ≤ λ` **for every summand i**.

Proposition 2.8 instead assumes that same bound for the collective period L. The latter is much stronger. Many individually cheap moduli may collectively involve all primes in Π. Therefore this proposition does not cap every standard level-O(log X) hybrid majorant.

Even its own whole-period radical bound does not imply `L≤X^{K+o(1)}`: `L=q^{⌈X⌉}` has fixed charged radical level for fixed q>W.

**Repair.** Remove the false period-size assertion. Since every q∈Π eventually exceeds W,

`ω_Π(L) log(y/2) ≤ λ(L) ≤ K log X`,

which directly gives `2^{ω_Π(L)}=X^{o(1)}`. Call the result a **bounded whole-period radical-level hybrid lemma**.

### 9.2 Haar fibres and nonunits

The proof must cover every residue r in the integer avoider, including nonunits, because the cited cap requires global integer domination. Unit Haar cannot condition on a nonunit residue. Under additive Haar on profinite integers, the symbols are orthogonal but not normalized: `E(x/n₂)²=φ(n₂)/n₂`.

Define the periodic Jacobi extension

`B_J={x: |Σa_n(x/n)|²≥T‖a‖²}`.

Write the squarefree index `n=n₁n₂`, with `n₁|rad(L)` and `(n₂,L)=1`. The correct conditional formula is

`E[|Σa_n(x/n)|² | x≡r mod L]`

`= Σ_{n₂} [φ(n₂)/n₂] |Σ_{n₁} a_{n₁n₂}(r/n₁)|²`

`≤ 2^{ω_Π(L)}‖a‖²`.

This also covers nonunit r; relevant fixed symbols can be zero. Since the last bound is <T‖a‖², the fibre has a low-bias point, and in fact an integer lift because the expression depends on finitely many residues. Periodicity of ν then promotes domination from `Ω(𝔊)\B_J` to all of Ω(𝔊).

The repaired proof works for arbitrary coefficients on squarefree Π-numbers, not merely the indicator coefficients of Remark 2.7. It also does not need plane sparsity. What it needs is the whole-period overlap bound. These are possible useful extensions, not licenses to replace whole-period level by per-term level.

### 9.3 Does the cited cap apply after promotion?

Yes, with its stated KARY/KARY2/Shiu proviso, global nonnegativity, and domination on the **whole integer avoider**. If the displayed d_i have extra prime factors not in L, rewrite the L-periodic function using residue indicators modulo L; those have the required charged level. The modulus of each word class dividing L is compatible with the setup.

Prime-only domination, positivity only at primes, or domination merely on a finite interval does not imply the cited hypothesis. The same caveat applies to the parenthetical ES/ET extension, which must name the audited ET/Vaughan family rather than all ES certificates.

**Repair.** Use the additive-Haar formula, define B_J, retain the whole-period budget explicitly, and narrow every later invocation to those hypotheses. A standard per-term-level hybrid theorem would require a genuinely additional argument.

## 10. Section 2.5 / Conjecture 2.9 — MAJOR evidentiary and scope qualifications

The conjecture is labeled as a conjecture, appropriately; the computations below do not refute it. They also do not establish it.

* The pair-mass computation is after deleting singleton boxes. A random “pair-sterile” point is not known to avoid triples, larger squarefree products, or mixed prime powers. `mass_trip=0` in a run without `--triples` means **not computed**, not zero true mass.
* “Triple boxes have mass O(1/log y)” is an unproved asymptotic here. Lemma 2.3's pointwise bound does not imply it. A pair fit `≈1.1(log h)²` does not control triples or the entire h-tail.
* The proposed Lovász-local-lemma justification is not supplied by a total pair-mass estimate and a singleton bound alone. One needs appropriate local dependency bounds and control of all higher-support events. Total event mass of order one can, without such structure, cover the entire probability space.
* The conjectural consequence must retain squarefree support and Π≥11 (or separately handle the finitely many omitted small primes). “Every datum supported on Π-numbers” cannot literally include arbitrary square powers: many distinct square indices collapse to the same sign character and destroy the norm identity.

**Repair.** Label the triple estimate and local-lemma mechanism as additional heuristics/hypotheses. State exactly which boxes the numerical search avoids. The conditional low-bias conclusion is valid for squarefree-supported data once a lower bound on sterile measure is assumed.

## 11. Theorem 2.10 — FATAL as a universal circularity theorem

It is not an honest conjunction with the scope currently printed.

1. **Item 1:** Lemma 1.2 permits an exceptional remainder. It does not force universal P. L5 is explicitly not a datum. The lower bound on T requires the relevant lower bound on Δ and an estimate actually obtained through Δ/T.
2. **Item 2:** Proposition 2.2 addresses fixed order, squarefree support and a baseline threshold depending on φ(k). It does not exclude all higher-order tests, arbitrary supports, the full variable-order spectrum, or the larger sieve. Explicit counterexamples appear in §3.5 of this report.
3. **Item 3:** This is the defensible new obstruction, but only for sparse Π, native ES₅/U classes, and an implication valid at all sufficiently large primes. It does not exclude finite-range or alternative-family certification.
4. **Item 4:** Proposition 2.8 has a whole-period radical budget, not the standard per-term CRT level budget. Its printed hypotheses also specialize the data much more than the opening universal sentence.

**“Hence the input … is not periodic” does not follow.** Other periodic forcing families, different data, higher collective periods, and finite-range uses of periodic information remain possible. On a finite interval every subset can even be encoded periodically with a sufficiently large modulus; the meaningful issue is the specified certification architecture and its complexity, not a categorical periodic/nonperiodic dichotomy. A sufficient strong implication is not, by itself, a proof of mathematical circularity.

### Linnik's least-prime assertion

The classical effective result `p_min(a,L)≪L^5` does imply a prime below X if `L≤cX^{1/5}` with c sufficiently small. The exponent 5 attributed to Xylouris is admissible; its precise reference is his dissertation (the Acta Arithmetica 2011 paper's displayed exponent is 5.18).

But this does not repair the paragraph:

* L must encode the full relevant quadratic profile as well as the avoided classes. Otherwise a nearby prime need not be outside B.
* Least-prime bounds do not place that prime in `(X/2,X]`, the interval defining E_X, or above an arbitrary certificate threshold.
* In Remark 2.7's genuine power-saving regime, `|Π|≈y^{1/2−ε}` and

  `log ∏_{q∈Π}q ≍ y^{1/2−ε} log y ≫ log X`.

  The modulus encoding the whole independent Π-profile is already superpolynomial in X. The proposed small-L illustration therefore does not apply to those data.
* Even a low-bias prime avoiding 𝔊 is not a counterexample to P unless it is actually exceptional. It is a counterexample to deriving P solely from the advertised avoidance input. The document must maintain that distinction.

**Repair.** Replace Theorem 2.10 by separately scoped certification obstructions. Keep Dirichlet's qualitative conclusion, or state a finite-range result only with the necessary full modulus and interval hypotheses. Replace “must be nonperiodic / individual-prime B2” by “must use input outside these particular certification mechanisms.”

### Novelty audit

BREADTH_Z45 §15 and EXSET_SIEVE_MASS §§4–5 already say that Linnik duality lies outside the CRT caps, that character confinement is the ES-specific missing input, and that word-certified marginal depletion is thin. They explicitly leave other Linnik configurations open. DEPTH_ASPECT §3 already proves one-coordinate sterile nonresidue points for the seven ET families and uses Dirichlet to obstruct finite coverings.

The defensible new pieces are **multi-coordinate sparse planes for native ES₅/U classes**, their **low-bias witness**, and the **repaired bounded-whole-period fibre promotion**. The multi-coordinate assertion is not a multi-coordinate theorem for the full ET family. Calling the conjunction universal, or promoting the old G3 Assessment to a theorem at that universal scope, is label inflation.

## 12. Theorem 3.1 — MINOR in the moment theorem; MAJOR surrounding application/scope errors

### Kernel collapse and norm: SOUND

“Squarefree kernel” must mean the parity kernel `∏_{q:v_q(product) odd}q`, not the radical. Then b is supported on odd squarefree numbers, including 1, at most `y^r≤X`. For odd primes p∉S,

`Σ b_{n₀}(n₀/p) = σ_S(p)^r`.

No coefficient is lost: repeated-square factors are accounted for by b's multiplicity. Orthogonality on the independent sign cube gives

`‖b‖² = E(Σ_{q∈S} ε_q)^{2r}`.

Every tuple contributing to this moment has an even number of appearances of each q and can be paired into equal labels. Counting all pairings overcounts such tuples, so

`‖b‖²≤(2r−1)!! s^r≤(2rs)^r`.

This is a legitimate use of Heath–Brown Theorem 1. I checked the original statement: both summation variables are positive **odd squarefree** integers, and the bound is `≪_ε(MN)^ε(M+N)Σ*|a_n|²`. Restricting its outer sum to odd primes only decreases the nonnegative sum.

### Small omissions and exponent arithmetic

The definition of σ excludes p∈S, but the theorem and displayed moment sum include them and p=2. Simply restrict the proof to odd p∉S and charge at most `s+1=X^{o(1)}` omitted primes; this does not affect the conclusion. The identity must not be asserted unchanged at p∈S.

For fixed ε the argument yields

`≪_ε X^{(1+2κ)/A + 2ε + o(1)}`.

Conclude explicitly that for every fixed δ>0 the bound is `≪_{A,κ,δ}X^{(1+2κ)/A+δ}`; this justifies the stated `X^{(1+2κ)/A+o(1)}` notation. Do not substitute an uncontrolled ε(X) into Heath–Brown's constant. The calculation of r and the exponent is otherwise correct, uniformly for the given lower bound on s.

### The κ=0 threshold and a clean repair

As stated, at κ=0 the theorem counts `|σ_S(p)|≥2s`, an impossible condition. This makes that endpoint true but vacuous. Full confinement gives only σ=s.

**Repair.** Replace the threshold by `ηs`, `η=(log X)^{−κ}`. The quotient becomes

`C_ε X^{1+2ε} [2r/(η²s)]^r`,

with the identical final exponent, since fixed constants to the rth power contribute only `X^{o(1)}`. The reading then requires nonresidue fraction `θ≤1/2−η/2`. Alternatively retain the original theorem and prove the σ=s case separately with denominator `s^{2r}`.

### “The barrier applies unchanged” — MAJOR, false scope

The dense S in this theorem satisfies

`Σ_{q∈S}q^{−1/2+ε} ≥ y^{1/2+ε}/(5 log y) → ∞`.

It is outside Theorem 2.5/Corollary 2.6. The condition T>2 is not that corollary's only hypothesis. Therefore the reading after Theorem 3.1 cannot invoke the proved exact sparse-plane barrier for these dense-block data. Conjecture 2.9 would be relevant, but it is not proved.

The Haar rarity statement itself is sound: Hoeffding gives `exp(−cη²s)`, and `A−2κ>1` makes this superpolynomially small in X. That does not extend a sparse-plane theorem to dense S.

## 13. Corollary 3.2 — MAJOR proof error; claimed exponent recoverable

The literal application “σ=s, hence Theorem 3.1 with κ=0” is invalid because that theorem requires σ≥2s. This is a decisive error in the displayed proof, not a counterexample to the claimed cap bound.

CAP_BOUNDED Lemma 3.1 does give

`e*(p)>y/4 ⇒ p≡1 mod 8 and q₃(p)>y+3`,

which is stronger than the implication used here. The progression PNT gives `s∼y/(4 log y)`, hence the lower bound `s≥y/(5 log y)` is correct. With the repaired threshold in Theorem 3.1, or by running its moment proof with threshold s, one obtains

`#{p≤X:e*(p)>(log X)^A/4} ≤ X^{1/A+o(1)}`

for every fixed A>1.

The claim “such p exceed y” imports Pollack through the last assertion of CAP_BOUNDED Lemma 3.1, not merely CAP_DOWN Thm 1.2/Prop 1.3 as listed. It can be deleted: p≡1 mod 8 and q∈S⇒q≡3 mod 4 already ensure p∉S. Thus the corollary's proof need not use Pollack at all.

**Repair.** Fix the threshold and update the dependency sentence or remove p>y. Describe the contribution as the application of the known quadratic large sieve to the cap, not a new general large-sieve theorem. CAP_BOUNDED §3 already mentions an earlier A>1 reviewer sketch in CAP_INTERPOLATION; the precise exponent/complete proof here can still be useful, but the broad threshold idea is not wholly new within the repository.

This counts **large-cap primes**, not ES-exceptional primes. No ES exceptional-set estimate follows without an additional forcing input.

## 14. Remark (2) after Corollary 3.2 — MINOR normalization; conditional scale claim SOUND

CAP_BOUNDED defines `𝒫(y)` with the restriction `p≡1 mod 8`. Thus `2^{−π(y;4,3)}` is a density **relative to that progression**. Put `k=π(y;4,3)`. The corrected GRH count is

`#(𝒫(y)∩[1,X]) = 2^{−k}π(X;8,1) + O(√X log²X)`

`= 2^{−k−2}Li(X) + O(√X log²X)`.

If a new set without p≡1 mod 8 is intended, define it under a different symbol; the stated all-prime main term then has a different meaning.

The character expansion is legitimate. Expand both the progression indicator and `∏(1+(q/p))/2`. All characters have conductor at most `8∏_{q≤y,q≡3(4)}q`, of logarithm O(y). The expansion's coefficient ℓ¹ norm is 1, so **there is no missing factor 2^k in the GRH error**. For fixed `0<A≤1`, log conductor is O(log X), and the displayed error is a safe bound. The main term is `X^{1−o(1)}`, larger than that error. The endpoint A=1 can also be included in this conditional obstruction to a fixed power saving.

The Lau–Wu/Graham–Ringrose comparison is correctly labeled analogous: their Theorem 1.2 gives a near-linear number of large-least-nonresidue primes along a sequence. It does not prove many genuinely large-cap primes. Counting the confinement superset is the route obstructed here, not every possible argument involving q₃ or e*.

## 15. Section 3.3 heuristics — MAJOR scope/label cleanup

The “Heuristically … (Assessment)” label is appropriate for the coupon-collector/tilting model, but not every sentence around it is safely qualified.

* The proved exact barrier only applies to qualifying sparse supports. Proposition 2.8 additionally needs its whole-period budget; “any approximate certification at level O(log X)” is too broad.
* Moving the analytic requirement from `(log X)^{2+δ}` to `(log X)^{1+δ}` does create heuristic room relative to reach `(log p)²/log log p`. The ratio is `(log X)^{1−δ}/log log X`, not literally `(log X)^{1−δ}`. The claimed exponential tilt assumes a model for label distributions and dependencies; no conditional distribution of actual exceptional primes has been established.
* On a Π-plane the possible labels are not “the words of q alone.” Lemma 2.3 allows every Π-number h, including qq′, q²q′ and larger products. Only the h=q slice is described by words of q.
* The fitted 1.1 coefficient concerns pair boxes in the displayed table; it is not a proved singleton-word asymptotic.
* “Per-prime forcing reach is zero at plane points” is false as a statement about all plane points: many such points lie in certificate boxes. Theorem 2.5 constructs a positive-measure sterile subset under sparsity, not universal sterility.
* “Exactly at the planes” is unsupported: no classification of all nongeneric profiles is proved.
* “Forcing must be pointwise” disregards the approximate-containment option in Lemma 1.2. Controlling a small exceptional set of nongeneric primes could also suffice. Finite-coordinate genericity can itself be a congruence property.

**Repair.** Present the heuristic as motivation only. Describe planes as explicit nongeneric obstructions in the proved scope; leave open both pointwise forcing and averaged control of nongeneric exceptional primes. Do not claim that the dense-block Heath–Brown route has been ruled out by the sparse-plane theorem.

## 16. Numerical checks and independent verification

Every Python execution below used `ulimit -v 8000000`, an explicit `timeout`, and `uv run --no-project` (with numpy supplied for the optional mass check). No unconstrained array calculation was used. The independent script streams divisor/word enumeration and imports no project code.

### Supplied self-check

Command: `timeout 180 uv run --no-project python3 scripts/z51_linnik_plane.py`.

All eight checks passed for Π={11,13,17,19,23,29,31}, m≤3000:

| h | W1 labels | W2 labels |
|---:|---:|---:|
| 11 | 16 | 13 |
| 221 | 27 | 48 |
| 253 | 26 | 41 |
| 31 | 20 | 17 |
| 551 | 55 | 53 |
| 121 | 17 | 13 |
| 2431 | 43 | 117 |
| 3211 | 61 | 45 |

This certifies finite agreement with brute force, not the infinite counting estimate or the printed D bound.

### Optional plane mass

Command: `timeout 900 uv run --no-project --with numpy python3 scripts/z51_linnik_planemass.py 200 es5 haar --search 300`.

Results: 21 primes; square mass 0; pair mass **1.0175920333384119**; mean certified boxes per pair **110.25238095238095**; mean `(log h)²` **99.77941887794775**, ratio ≈1.105; **100/300** search trials avoid singleton/pair boxes. All built-in parity assertions passed. This agrees with the table's scale; it does not test all higher-order boxes. `mass_trip=0` was the uncomputed default.

### Supplied bias check

Command: `timeout 120 uv run --no-project python3 scripts/z51_linnik_bias_check.py`.

All kernel identities and moment bounds passed for s=7 and r=2,3,4. Exact norm squares were **133, 3787, 134953**, against pairing bounds **147, 5145, 252105**. The largest reported empirical sieve ratio was about **0.044**. The script does not test the erroneous application at κ=0 and cannot establish a universal large-sieve constant from these samples.

### Independent check from definitions

Reproducible script: `reviews/z51-linnik-review-1-check.py`.

Command: `ulimit -v 8000000; timeout 120 uv run --no-project python3 reviews/z51-linnik-review-1-check.py`.

The script directly enumerates divisors of M+1 for W1 and factorizations uv for W2; independently reconstructs W1 from the integer word equation; explicitly enumerates v modulo 8 and t modulo 8 to handle refined classes on n≡1 mod 8; chooses coprime integer representatives; and computes Jacobi symbols by a standalone Euclidean algorithm. Π={11,13,17,19,23}, m≤120. Counts differ from the supplied check because Π and m-cutoff differ.

| h | W1 classes/words | W2 classes | symbol identities | certified W1/W2 |
|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 6 | 0 / 0 |
| 11 | 16 | 13 | 29 | 10 / 9 |
| 13 | 15 | 14 | 29 | 8 / 8 |
| 17 | 18 | 14 | 32 | 8 / 6 |
| 121 | 18 | 9 | 27 | 0 / 0 |
| 143 | 43 | 41 | 84 | 39 / 33 |
| 187 | 30 | 34 | 64 | 20 / 23 |
| 2431 | 34 | 78 | 112 | 28 / 56 |

**All W1 correspondence and parity assertions passed.** The independent check finds a `D>h+1` example at every tested h, exactly as described in §4(b). It covers square h, mixed products, even pivots, u=1, and h=1; it is evidence supporting the algebra, not a substitute for it.

## 17. Sources and review method

I checked the named internal definitions and theorem scopes directly, including FOREST_DEEP_FABLE Theorem A/B, EXSET_SIEVE_MASS Definition 1.2/Theorem 3.2/§§4–5, CAP_BOUNDED §3, BREADTH_Z45 §15, and DEPTH_ASPECT §3. Three independent mathematical audits were used for the character argument, the analytic upgrade, and CRT scope; their conclusions were checked against those sources and the explicit calculations above before inclusion.

External theorem checks:

* Heath–Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995), **Theorem 1, p.237**, original PDF: <https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf>. The reader proxy initially failed; a direct bounded download succeeded. The odd-squarefree restrictions and exact `(MN)^ε(M+N)` form were read from the original.
* Schinzel, *Abelian binomials, power residues and exponential congruences*, Acta Arith. 32 (1977), **Theorem 2**, checked in the scanned first page of `sources/uo/schinzel-1977-aa32-abelian-binomials.pdf`. The restricted necessary implication also has the independent elementary proof in §3.3 above.
* Lau–Wu, *On the least quadratic non-residue*, Theorems 1.1–1.2 and the Baier discussion, checked in `sources/lit2026/lau-wu-least-quadratic-nonresidue.txt` against the local source citation.
* Linnik/Xylouris reference and the distinction between the published 5.18 result and dissertation exponent 5: <https://teorth.github.io/optimizationproblems/constants/65a.html>. No newer claimed improvement is needed or assumed here.

## Most serious issues

1. **Theorem 2.10 overclaims a universal barrier:** fixed-order squarefree Chebotarev, sparse planes, and a bounded-whole-period hybrid lemma do not cover every L1–L5 argument or force nonperiodic/pointwise input.
2. **The higher-order consequences are false:** wrong Parseval sign, variable-order aggregate counterexamples, omitted squarefree restriction, and an incorrect description of Gallagher's larger sieve.
3. **The hybrid cap changes the definition of level:** the proof controls the whole period's radical, whereas the standard CRT cap charges each summand separately.
4. **Corollary 3.2 applies a vacuous κ=0 theorem:** σ=s does not meet σ≥2s. A constant-threshold repair recovers the useful exponent `1/A`.
5. **Sparse results are repeatedly applied to dense data or every sign pattern:** these extensions are not proved. Lemma 2.3's false D bound is smaller and readily fixed; the exact sparse-plane low-bias obstruction itself survives.
