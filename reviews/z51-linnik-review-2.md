# Hostile referee report, round 2: EXSET_LINNIK

Reviewed 2026-10-30. Checkout: `c54d8b113e2ea9e6cd32696564224845a9b0082a`.
Reviewed document SHA-256: `8d4a395cc7c45dead3ea2de79b72e6f3049975019ecaa413a0e4cab63892dc30`.
Scope: the R1 repairs, all new §§4–6, summaries §§0/8, and bounded numerical replication. ES remains OPEN.

**Concurrent-update note:** during this review, other work advanced HEAD through `8f8d492f` to `76b0e72c6d76374ea250877f0b35bd82e35b8051`, appending item 5 to §8. The original reviewed sections are unchanged. The completion-time document SHA-256 is `4b4e5b65ba7f8ca1dc10239c3b018976cc82144fd3207043128b18cc3745e465`; §6.1 of this report separately audits that addition. This review makes no edits to EXSET_LINNIK.md and creates no commits.

**Overall: MAJOR revision.** The main R1 repairs work: the fixed-order character theorem, sparse-plane theorem, whole-period hybrid lemma, and Heath–Brown cap upgrade survive. The new material contains two **FATAL-as-stated** claims: the purported general blocking lemma for p-dependent data, and the literal window hypothesis (WL_A), which is impossible because it includes primes in the wrong congruence class. Proposition 6.1 has a repairable majorant-assembly gap; its per-summand level calculation is correct. Section 6.3 then overextends its family scope and again overstates the necessity of pointwise input.

Here **FATAL** means a false claimed scope or an unusable hypothesis, not that ES is disproved or every ingredient must be discarded. **MAJOR** requires a substantive proof/scope repair; **MINOR** is local; **SOUND** is within the stated dependencies. The internal KARY/KARY2/Shiu cap is accepted with its explicitly stated provisos, not independently reproved here.

## 1. Round-1 repairs: §§1–3

### 1.1 Lemma 1.2 and equation (1.1) — SOUND; surrounding wording MINOR

The exact/approximate distinction is now explicit: the approximate input is a bound on `E\B`, not universal P(a,T). Nonzero a and the nonempty required high-bias set are correctly included. The support lower bound follows from Cauchy–Schwarz. Equation (1.1) is correct for odd squarefree support under unit Haar with x≡1 mod 8. The square illustration is now restricted to coherent nonnegative data, and standard CRT level is correctly identified as per-summand, not total period.

The repaired discussion of Gallagher's sieve concerns its reverse use with exceptional primes as moduli; it no longer asserts the false general requirement that a larger sieve needs polynomial-index subgroups.

**Remaining wording:** “Tests of order ≥3 are not periodic at all” is too absolute: a singleton-supported datum already has constant aggregate bias. Say that general higher-order tests are not ordinary Dirichlet-character tests in the prime variable, and state the actual obstruction through Proposition 2.2. No quantitative equidistribution in a growing field/progression follows from its qualitative Chebotarev argument.

### 1.2 Proposition 2.2, including the coset/Kummer step — SOUND

The repaired proof addresses every material R1 objection.

* `k|L′` and the compatible unit class C ensure that its Frobenius coset acts trivially on μ_k. Chebotarev averages over `g₀H`, not H.
* For distinct squarefree n,n′, put m=n/n′. If the multiplier of α_m is trivial on H, then α_m belongs to the cyclotomic field F. Its real subfield Q(α_m) is Galois because F/Q is abelian. Every conjugate is a real kth root of m, hence ±α_m; therefore α_m²∈Q. A valuation ±1 of m contradicts `m²∈Q^{×k}` for k≥3.
* The multipliers restricted to H are characters. Raising to a faithful exponent t preserves nontriviality. Since g₀ fixes μ_k, the off-diagonal coset average is its fixed multiplier times the zero H-average.
* Frobenius multipliers identify with power-residue characters at unramified primes. Summing over all faithful t makes the function conjugacy invariant; conjugation permutes those t. The diagonal contribution is exactly φ(k), for arbitrary complex a.
* Finite-valued Chebotarev averaging gives relative natural prime density; the stated half-density sublevel conclusion follows by Markov.

The squarefree restriction, fixed-order restriction, quartic-square counterexample, and withdrawal of the full Montgomery/Elliott/larger-sieve consequences are all present and correct. In summaries, “never CRT-certified” must mean a lower bound **T>φ(k)**, not the perfectly certifiable baseline φ(k). For a fixed finite set of orders, replace this baseline by the sum of their φ(k)'s.

### 1.3 Lemma 2.3(a)–(c) — SOUND

The W1 correspondence and the unit compatibility condition are correct. In (b),

`D = h₁/m₂ + h₂/m₁ + 1/(m₁m₂) ≤ h₁+h₂+1 ≤ h+2`.

Thus the repaired h+2 bound is valid, including u=1,v=h. Both factors in the factorization are positive integers, and their product is D+h≤2h+2. There is **no remaining error** in this inequality.

In (c), the sum over unitary splittings is now explicit. Choosing the smaller factor f and a divisor D of f+h_j determines the remaining W2 parameters; overcounting is harmless. The W1 small-endpoint estimate and the ordinary divisor bound give `O_ε(2^{ω(h)}h^{1/2+ε})`. The fixed 2-adic coordinate makes at most one refinement compatible with each unrefined class. The earlier off-by-one and unbound-splitting issues are repaired.

### 1.4 Lemma 2.4: coprimality and U slots — SOUND

The new selection of n coprime to u is possible: gcd(u,M)=1, and the additional 2-adic refinement does not obstruct odd n. Then Mv=n+u gives gcd(n,v)=1, and a divisor common to u,v divides n, hence gcd(u,v)=1. Taking n large avoids positivity/degeneracy issues. W2's unit residue supplies its coprimality directly.

The identities `(tu−1)(tv−1)=tn+1` and `u(tv−1)=n+v` give `(M/n)=(uv/n)`. FOREST_DEEP_FABLE Theorem A explicitly allows composite n with these gcd hypotheses. Removing the 2-part and using n≡1 mod 8m′ gives `(M/n)=(c/h)`.

For U, the proof no longer improperly invokes a prime-only theorem: if u≡7 mod 8, then `8|v(tu−1)`, so one factor is divisible by 4. This is the required slot. Hence h=1 and square h carry no certificate box.

### 1.5 Theorem 2.5(a)–(b) — SOUND

For q≥11 and 0<ε≤1/8,

`Σ_{j≥1} q^{j(1/2+ε)}/φ(q^j) = [q/(q−1)] q^{−1/2+ε}/(1−q^{−1/2+ε}) ≤ 2q^{−1/2+ε}`.

Unconditional box mass is 1/φ(h). Conditioning on a full sign cell multiplies compatible box mass by `2^{ω(h)}`. Combining this with the class count produces exactly `4^{ω(h)}`, not `2^{ω(h)}`, in (b). The Euler products, `e^{8σ}−1≤16σ` for σ≤1/8, and `η₀=min(1/8,1/(32C_ε))` give covered mass at most 1/2 in every cell. No independence of boxes or local lemma is being assumed. The omission of h=1 is now justified by Lemma 2.4.

### 1.6 Corollary 2.6 — SOUND

The normalized sign characters are orthogonal. Integrating over the sterile set of mass at least 1/2 gives a sterile point with bias at most 2, strictly outside B_J when T>2. The integrand takes finitely many values, so there is no essential-infimum subtlety. The modulus in the Dirichlet step includes the refined class moduli and the support primes, and the witness is a unit modulo that modulus.

This gives infinitely many primes violating the advertised **avoidance-to-bias implication**, not ES counterexamples, and not necessarily primes in (X/2,X] for growing data. Those qualifications are now explicit. The result remains only for native ES₅/U classes and sparse Π.

### 1.7 Remark 2.7 — SOUND arithmetic; MINOR parameter bookkeeping

The corrected condition `ε<1/2−1/A` makes the support nonempty eventually and gives

`|𝒜|≥X^{1/2−ε−1/A−o(1)}`,

hence the stated Heath–Brown exceptional-set exponent `1/2+1/A+ε+2ε′+o(1)`. The per-sign sterility assertion now follows from Theorem 2.5(b).

Also retain the inherited condition ε≤1/8 explicitly: choose `0<ε<min(1/8,1/2−1/A)`, with a harmless endpoint adjustment. As printed, Remark 2.7 permits ε outside the domain in which η₀(ε) was defined. This is not an exponent problem.

### 1.8 Proposition 2.8 — SOUND, with the declared whole-period scope

The repair uses the right measure and the right complexity hypothesis. Under additive Haar in a residue fibre r mod L, write n=n₁n₂ with n₁|rad L and (n₂,L)=1. Distinct squarefree n₂ have zero cross-moments, while their squared norms are φ(n₂)/n₂. Thus

`E(|Σ a_n(x/n)|² | r) = Σ_{n₂} [φ(n₂)/n₂] |Σ_{n₁} a_{n₁n₂}(r/n₁)|² ≤ 2^{ω_Π(L)}‖a‖²`.

This remains valid for nonunit r; fixed Jacobi symbols can vanish. Since W is fixed, y/2>W eventually, and the whole-period budget gives `2^{ω_Π(L)}=X^{o(1)}<T`. The fibre contains an integer outside B_J. L-periodicity then promotes ν≥1 to the entire integer avoider, exactly the hypothesis needed by EXSET_SIEVE_MASS Theorem 3.2.

Rewriting with residue indicators mod L respects the charged radical level. Use `λ=max(λ₀,λ(L))` when quoting that theorem, rather than applying a logarithmic formula literally at λ=0. This is a minor normalization. **The result still says nothing about hybrids having only per-summand level control.**

### 1.9 Conjecture 2.9 and its evidence — SOUND labels in the body; MINOR summary overstatement

The body now distinguishes uncomputed triples from zero mass, lists the checked supports, and labels the averaged bound, higher-box control, and local-lemma mechanism as unproved. That repairs R1. The conditional low-bias conclusion follows from a sterile-measure lower bound and orthogonality. For the phrase “all polylog-smooth squarefree data,” mention the finite additional small-prime factors excluded by Π≥11; their Cauchy–Schwarz cost is only a constant, but the plane does not randomize them.

The summary's “28% sterile incl. triples” still overstates the experiment. These are points avoiding the **checked singleton/pair/triple boxes**, not certified points avoiding every class at every modulus. Higher products and mixed powers remain unchecked. Likewise “the survivors match Poisson” is qualitative evidence, not an independence theorem.

### 1.10 Theorem 2.10(A)–(D) — MAJOR for D's proof; otherwise substantially honest rescoping

The universal first-draft theorem is genuinely withdrawn. Item B preserves sparse support, native families, and infinite-range scope. Item C now says whole-period level. The “not covered” list is material and appropriate.

Item A should explicitly say T>φ(k); without that qualification it overstates Proposition 2.2. Item D depends on Proposition 6.1, whose printed proof has the omitted-unit-fibre problem detailed in §4 below. After that repair, D is a legitimate scoped conjunction for the native family. It does not cover all p-dependent data or the full ratio family, and cannot support the stronger claims later in §§4/6.3.

### 1.11 Theorem 3.1 — SOUND

The ηs threshold repairs the vacuous κ=0 endpoint. The parity-kernel identity, including n₀=1, is correct for odd p∉S. The norm identity and pairing bound

`‖b‖²=E(Σ ε_q)^{2r}≤(2r−1)!!s^r≤(2rs)^r`

are valid. Heath–Brown applies because both variables are odd squarefree; restricting the outer variable to primes is legitimate. The exceptional count is

`≪_ε X^{1+2ε}(2r/(η²s))^r = X^{(1+2κ)/A+2ε+o(1)}`.

Taking a fixed sufficiently small ε gives the stated every-δ formulation. Discarding p=2 and p∈S costs only X^{o(1)}. The dense-block reading now explicitly acknowledges that this S is outside the proved sparse-plane barrier.

### 1.12 Corollary 3.2 and Remark (2) — SOUND

CAP_BOUNDED Lemma 3.1 gives the required implication to p≡1 mod 8 and q₃(p)>y. The progression PNT gives `s∼y/(4log y)`, and p∉S follows from the congruence classes, with no Pollack input. Now σ=s does satisfy the κ=0 threshold. The exponent 1/A and the distinction between large-cap primes and ES-exceptional primes are correct.

The GRH remark has the right normalization `2^{−k}π(X;8,1)`. The character expansion has coefficient ℓ¹ norm 1; its nonempty subsets give nonprincipal characters, even after the mod-8 expansion. For 0<A≤1 the conductor logarithm is O(log X), so the quoted `O(√X log²X)` error is safe and the main term is X^{1−o(1)}. This obstructs bounding that confinement superset by a fixed power saving, not every conceivable argument about q₃ or e*.

The §§3.3/8 heuristic comparisons are not proofs of bias for actual exceptional primes. In particular the measured bounded pair mass should not be described as established control of every higher-support box. The approximate-containment alternative is now present in §3.3, but is lost again in §6.3.

## 2. New §4: p-dependent data

### 2.1 Lemma 4.1 — SOUND

For an orthonormal basis of V, Cauchy–Schwarz bounds each selected vector's normalized character energy by the sum of the basis energies. Summing gives `T#E≤KΔ`. This is the correct dimension loss. It is sharp for abstract orthogonal test systems. The important parameter is **linear dimension**, not the cardinality of the image of p↦a^(p).

### 2.2 Proposition 4.2(i) — SOUND disjoint case; MAJOR gap in the overlap justification, repairable

When Π∩supp(L)=∅, every plane point is already 1 modulo L. Choose the datum a^(1) first, then apply Corollary 2.6. The notation c₀:=z mod L is unnecessarily self-referential, but there is no actual fixed-point problem in this disjoint case. One bad fibre suffices to defeat a universal implication.

When L meets Π, Theorem 2.5(b) provides sterility in **sign cells**, not in every residue class modulo powers of primes dividing L. The printed sub-cell argument does not establish what it invokes.

A useful repair requires no stronger sterility theorem. Let t=|Π∩supp L| and normalize each a^(c) to norm 1. On each plane fibre c mod L, orthogonality at the unfixed primes and Cauchy–Schwarz give conditional mean of the selected bias at most 2^t. Integrating over the whole plane gives the same upper bound. Since the global sterile set has measure at least 1/2, it contains a point with its **own fibre's** bias at most 2^{t+1}. Thus a universal implication fails for **T>2^{t+1}**. This proves existence of a suitable fibre, not sterility of every prescribed residue fibre.

Use a different symbol for the dimension: the exponent K in L≤X^K is not the dimension of the coefficient space. The rank is at most the number of relevant fibres, at most φ(L), apart from finitely many primes dividing L.

### 2.3 Proposition 4.2(ii) and the hybrid paragraph — MINOR/MAJOR precision repairs

The displayed maximal Haar bound is correct. If F_x(t)=Σa_n(x/n)n^{it}, then

`sup_{|t|≤T₀}|F_x(t)|² ≤ |F_x(0)|² + 2∫_{−T₀}^{T₀}|F_x(t)F'_x(t)|dt`.

Orthogonality and Cauchy–Schwarz give `E sup|F|²≤(1+4T₀log N)‖a‖²`. The sterile-set argument therefore works for **T>C(1+T₀log N)**. The printed `T>CT₀log N` is false without a lower bound on T₀: take T₀=0 and a=δ₁.

An integrated hybrid large sieve does not directly bound a p-dependent selected t_p. Applying Sobolev also charges the derivative, hence log N factors; the short-T₀ normalization must be stated. “Δ grows by the same factor T₀” is only a rough large-T₀ scale description, not the complete selected-t bound. This is repairable; it does not establish a general classification of p-dependence.

### 2.4 Proposition 4.2(iii) and the “exact blocking lemma” — FATAL as a general exclusion

If a family really has rank #E, Lemma 4.1 is tautological, since a valid Δ bounds the bias of each individual vector. The divisor-indicator example has a triangular largest-coordinate argument for independence. These are legitimate examples of an ineffective implementation.

But **injectivity of data is not linear independence of vectors**, and “generic” is not a theorem hypothesis. For example, the word-derived number max{d:d|p+1}=p+1 can define

`a^(p)=f+(p+1)g`

for fixed independent f,g. This is injective with arbitrarily many states but rank 2. It need not supply the desired bias; it does refute the proposed necessary dimension/state inference.

Nor does a small number of states make the selection rule depend on p modulo a polynomial-size L. An arbitrary partition of primes into a few states has no such guaranteed CRT description. Lemma 4.1 gives a sufficient bound when dimension is controlled, not the asserted necessary bound on the number of states or a proof that every useful family is covered by §2.

**Repair:** delete the general “exact blocking lemma” and the universal classification language. Retain Lemma 4.1, the explicitly CRT-dependent subclass in (i), the properly normalized twist estimate, and the genuinely full-rank examples in (iii). Other structured p-dependent families remain open.

## 3. New §5: relaxations and windows

### 3.1 Lemma 5.1 — SOUND abstract orientation; MAJOR overbreadth in the listed examples

For a genuine implication ES⇒R, the contrapositive E_R⊂E_ES is correct. Information about E_R alone does not bound the larger E_ES. A strengthening R′⇒ES has the desired reverse inclusion of failure sets.

Two listed instances are not justified by the alleged triviality:

* **Prescribed/restricted windows with a cap are not automatically relaxations.** Already p=5 has `4/5=1/2+1/4+1/20`, but the cap-0 window q=7 has x=3 and B=px=15. No two divisors of 15 sum to 0 mod 7, so this window fails. The independent check verifies this example. A global relaxed equation and a restricted window-certificate menu must not be conflated.
* **V_φ is not a tautological relaxation under its actual definition.** T1_TEMPLATE §1 requires mixed σ₂-signs. A positive integer ES triple embedded in Q(√5) has all three σ₂-signs positive and does not qualify. This is a missing implication proof, not a demonstrated counterexample to ES(p)⇒V_φ(p). Delete it from the trivial list or supply a separate theorem/construction.

“Properties pass only if E_ES⊂E_R” should read “they do not pass by this inclusion argument alone”: the same property could hold on E_ES for an independent reason.

### 3.2 Lemma 5.2 — SOUND colour observation; MINOR incorrect failure-set formula

The colour of an actual refined word certificate is fixed by its shape/congruence conditions; it is not additional free character information. Within the precise sparse/whole-period scopes, a finite sub-menu of native certificates is still covered by §2's obstruction.

However, `E′=E_X∩Ω(𝔊)` is the wrong failure set. Since E_X already avoids its certificate sub-menu, this intersection is just E_X. The failure set of the strengthening is instead

`E′={primes p∈(X/2,X]: p∈Ω(𝔊)}`,

with certificate thresholds accounted for. It contains E_ES (and the relevant native exceptional set). Infinite menus and finite-range threshold statements need the same qualifications as §1.3. The corrected set, not the printed intersection, supports the intended argument.

### 3.3 Window criterion — SOUND

Let B=p(p+q)/4, with p≡1 mod 4, q≡3 mod 4, and q≠p. Then gcd(q,B)=1. A direct ES solution at x=(p+q)/4 is equivalent to `q/B=1/y+1/z`.

For necessity, write y=gu,z=gv with gcd(u,v)=1. Then `qguv=B(u+v)`, so uv|B. Writing B=huv gives qg=h(u+v); since q∤h, q|u+v, with u,v divisors of B. Conversely, if d₁,d₂|B and q|(d₁+d₂), put

`y=(B/d₁)(d₁+d₂)/q`, `z=(B/d₂)(d₁+d₂)/q`.

These are positive integers and give q/B. The author's residue-set algorithm implements precisely this criterion in its tested range. The independent direct-y search agrees in all 273 small cases.

The claim that a nonresidue window always gives some capped certificate needs the existing CAP_DOWN restrictions. It is valid for the Mordell-hard p≡1 mod 8 population used in the experiment, not for all p≡1 mod 4 without the even-window exception.

### 3.4 Window-lottery evidence — SOUND finite evidence; MAJOR if read as an asymptotic implication

The reduced run agrees with the scale of the stored tables; details are in §5 below. The body honestly says that “failures” mean **no forced window fires**, ignoring unforced windows. These form a larger set than the actual failures of R′_y. Do not label their measured nonresidue fraction as the measured fraction for E′_y itself.

Near-zero pair correlations do not prove mutual independence, nor uniform exponentially small failure probabilities. The “within 10–20%” description is only approximate: even the stored y=200 k=8 entry differs by about 23%, and tiny tail bins cannot support such a uniform statement. Stored correlations also reach 0.1098, slightly beyond a literal ±0.1.

The model's claimed `exp(−c(log X)^{A−o(1)})` failure probability additionally requires adequate asymptotic firing rates when y=(log X)^A, not merely independence. The measured forced rates vary greatly with q and the mean drops from approximately 0.47 to 0.34 when the tested block is doubled. A fixed positive or `(log X)^{−o(1)}` rate at the growing block is an extra model assumption. Label it explicitly; the experiment does not establish it for every A>1.

### 3.5 (WL_A) and Corollary 5.3 — FATAL hypothesis as printed; SOUND intended conditional after repair

**The literal (WL_A) is false.** It quantifies over every prime p in (X/2,X], while its windows use primes q≡3 mod 4 and require x=(p+q)/4∈Z. For p≡3 mod 4, x is never integral.

This is not a vacuous edge case in the antecedent. Put α=(1+2κ)/A<1, with the intended 0≤κ<(A−1)/2. Theorem 3.1, using δ<1−α, bounds the biased primes by o(X/log X). The progression PNT supplies ≍X/log X primes p≡3 mod 4 in the dyadic interval. Consequently many of those primes are unbiased and violate (WL_A). A conditional theorem on this impossible hypothesis has no substantive content.

**Repair:** restrict (WL_A) to Mordell-hard primes, or at least p≡1 mod 4, and invoke classical ES solutions outside the chosen unsolved classes. Require fixed `A>1`, `0≤κ<(A−1)/2`, and the hypothesis **at every sufficiently large scale**. Then exceptional primes in each dyadic interval have `|σ_S|≥ηs`; Theorem 3.1 applies and dyadic summation yields, for every δ>0,

`#{p≤X: ES(p) fails} ≪_{A,κ,δ} X^{α+δ}`.

This justifies the `X^{α+o(1)}` shorthand without varying the Heath–Brown epsilon uncontrolledly. A hypothesis only at one scale bounds that dyadic interval, not all p≤X.

The reading also has a minor factor-of-two error: the number of q≡3 mod 4 in (y/2,y] is asymptotic to `y/(4log y)`, not `y/(2log y)`.

Finally, “It is not a CRT consequence” is not proved for these full ES window classes. The paragraph itself admits that the analogue of Corollary 2.6 was not attempted. The one-coordinate collapse is motivation, not a global window-certification obstruction.

## 4. New §6: ratio forcing and reverse-role sieves

### 4.1 Section 6.1: ratio classes and generic forcing numerics — SOUND finite evidence

CAP_INTERPOLATION Proposition 5.1 at e=0 gives the stated ℛ(M) class family, with its p∤DM condition. The C program tests `M=qm≡3 mod 4`, q∤m, D|((M+1)/4)², `m|p+4D`, and the label −4D mod q. For the requested bounds its integers, divisor buffer, and allocation sizes are safe. Since M≤p in these runs, p|M cannot cause an accepted unit class; the explicit D filter is consistent.

The reduced mode-0 output has mean 99.57 raw labels per q≥25 through q=113, versus the table's approximately 96 over its larger q/sample range at p≈10⁶. Its ratio to log³p is 0.03776 and first hole is q=29, consistent with the advertised scale and 17–37 range. This does not independently reproduce all four decades or establish an asymptotic cubic law.

“Labels” here counts accepted **(M,D) occurrences**, not distinct residues mod q, and not independent coupon draws. The output separately counts distinct residue coverage. Keep that distinction in the cubic-supply/coupon-collector discussion. “Cubic supply confirmed” should mean a fit consistent with the finite data, not a proved per-prime asymptotic.

### 4.2 Plane equation and saturation — SOUND for fixed q; independently CERTIFIED over the table's finite q-range

At the one-coordinate plane, put D′=A²/D. From `4D≡−1 mod m` and `16DD′=(qm+1)²≡1 mod m`, also `4D′≡−1 mod m`. Define k=(4D+1)/m and k′=(4D′+1)/m. Then

`(km−1)(k′m−1)=(qm+1)²`.

The converse requires the original congruence restrictions, positivity, divisibility by 4 of both factors, and q∤m; the naked equation alone overcounts.

There is a complete finite enumeration, not merely an observed cutoff. Order k≤k′. Then k≤q+2 and

`m=(k+k′+2q)/(kk′−q²)`.

For k≥2, m≥1 implies `(k−1)(k′−1)≤(q+1)²`. For k=1,

`(m−1)(k′−q²)=(q+1)²`.

These give finite ranges for both cases. My independent script enumerates them, filters the original conditions, and checks agreement with a separate original-definition divisor scan at M≤5000 for every odd prime q≤300. It also exactly matches every requested mode-1 output row through q=113.

For primes **25≤q≤300**, the complete mean is **39.8301886792** labels; the largest required pivot is **5,706,695**. Thus the table's saturation for PB≥10⁷ is valid over that range, not an assertion uniform over all q. The coverage fractions are exactly the displayed rounded values. All labels are nonresidues. Algebraically, the square-avoidance Jacobi law for ℛ(M), with x≡1 mod m, gives the same parity conclusion.

This is a **one-coordinate** calculation. It neither constructs a point avoiding every ratio-class box on a multi-coordinate Π-plane nor proves that the native sterile points of Theorem 2.5 are sterile for ℛ(M).

### 4.3 Proposition 6.1 — MAJOR proof gap; native-family numerical cap is repairable

#### What is correct

Montgomery's residue-only lower bound is CRT-admissible for the whole fibre avoider. Under n=c+Lk and gcd(q,L)=1, multiplication by L permutes the q-residues; the number of missed classes is unchanged.

The Montgomery product denominator uses Farey frequencies with **squarefree composite denominators d≤Q**, not only individual primes q≤Q. This does not alter the desired bound: squaring combines two such denominators d₁,d₂≤Q. A k-class mod d lifts to

`n≡c+Lb mod Ld`.

Therefore every term in the assembled square has modulus dividing `L·lcm(d₁,d₂)` and charged level at most

`λ(L)+log d₁+log d₂ ≤ log L+2log Q ≤ (K+2)log X`.

This is genuinely **per-summand** control. There is no need to charge the enormous lcm of all denominators, and no new version of the old period/level mistake here.

#### The printed assembly does not majorize its claimed avoider

Only **unit** fibres c mod L are summed. Thus ν is zero on every nonunit fibre, yet Ω(𝔊) need not exclude those integers. For example, with 𝔊 empty and L=2, the constructed ν is zero at even integers although Ω(𝔊)=Z. The statement “ν≥1 on all of Ω(𝔊)” is false. EXSET_SIEVE_MASS Theorem 3.2 requires domination on the whole integer avoider, so it cannot be applied as printed.

**Repair:** enlarge the family to

`𝔊′=𝔊∪{0 mod ℓ : ℓ|L}`.

Then Ω(𝔊′)=Ω(𝔊)∩{(n,L)=1}, which the assembled ν does majorize. The cited Theorem 3.2 explicitly allows these selector classes, with arbitrary moduli for the native word part. Their addition does not enlarge any summand modulus of ν. Separately charge the primes p|L in (X/2,X]: there are O_K(1). Also retain the certificate-threshold assumption needed to put E_X inside the chosen avoider; an arbitrary certificate with an unhandled initial prefix is not an automatic finite-range input.

#### Reparametrisation and short fibres

The literal invocation of Corollary 2.2 at N=X/L ignores integer interval lengths; the cited general fibre theorem imposes L≤X/2. It would be wrong simply to inherit that theorem for all L≤X^K.

However, this is **not a counterexample to the displayed numerical lower bound**, and a stronger repair is available. Let `D=X/L+Q²` and use the unweighted Farey functional F₁. Montgomery admissibility gives `L_c(Q)≤F₁*`. The pure duality theorem gives a majorant ν_c with

`D/L_c(Q) ≥ D/F₁* = D·Eν_c ≥ (X/L)Eν_c`.

Here Parseval identifies the unweighted dual objective with Eν_c; no real-valued “interval of X/L integers” is required. For an actual nonempty fibre interval, `N_c≤ceil(X/L)`, and Montgomery–Vaughan's sharper constant satisfies `N_c−1+Q²≤X/L+Q²`, even when L>X. Empty avoider fibres can be assigned ν_c=0.

Assembly then gives `Σ_c(X/L)Eν_c=X Eν`, and the selector-compatible cap yields the claimed `X exp(−C(log X)^{2/3+o(1)})` floor for the displayed sum over **all unit fibres**. Do not silently replace that sum by a sum discarding geometrically empty fibres; the global-majorant argument for such a different expression is not supplied.

Thus the native-family result can remain PROVED relative to the cited cap **after these explicit repairs**. The current proof is not complete.

### 4.4 “Why the cubic reach does not enter” and §6.3 decision — MAJOR scope errors

Proposition 6.1 assumes **𝔊⊂𝔉₅∪𝔘**. The cubic experiment uses **ℛ(M)**. These are not interchangeable family hypotheses. The statement that the CRT-certified part of that cubic reach is capped *by Proposition 6.1* is unsupported. EXCEPTIONAL_LARGESIEVE Theorem 3.1 does explicitly treat ℛ(M) mixtures, but gives the **3/4** cap, with its own hypotheses (in particular its stated fibre-length restriction). That is a possible route to a correctly scoped no-fixed-power-saving conclusion, not a 2/3-cap proof for ℛ(M).

Also, the estimate `Σ_{m|L}τ(A_m²)/m≈(log log X)³` is not the literal number of labels on a fixed fibre: a compatible label is selected by a 0/1 congruence condition. The 1/m is an averaging heuristic over c. No uniform-in-c result follows from it. Keep this as a model, identify the averaging, and do not use it as a theorem excluding unusually dense fibres.

“At the sterile plane points it is zero” again crosses the family boundary. Theorem 2.5's sterile points concern native word classes, not ℛ(M). The ratio experiment itself has nonzero one-coordinate coverage. Nor does saturation of those slices control all higher-support boxes on a multi-coordinate plane.

Finally, “It needs pointwise input” is stronger than the proved conclusion. An approximate containment with a power-saving exceptional remainder could also suffice, as Lemma 1.2 already states. A finite-range/non-CRT averaged input is not excluded. The honest decision is: **the measured individual-integer reach is not supplied as a valid bias/depletion theorem by these computations; the specified CRT-admissible implementations are capped within the appropriate family and level hypotheses; other pointwise or approximate inputs remain open.**

## 5. Numerical replication and independent checks

All executions used `ulimit -v 8000000` and explicit timeouts. Python ran through uv; `OPENBLAS_NUM_THREADS=1` bounded the NumPy backend. The supplied windows script's largest initial array is about 25.75 million int32 entries (about 103 MB), not a dense geometry/product allocation. The independent script uses trial division, small sets, and streamed loops; it imports no project code.

Commands (outputs under `/tmp/z51-r2-*`):

```sh
ulimit -v 8000000
gcc -O2 -o /tmp/r2fes scripts/z51_linnik_forcing_es.c
timeout 300 /tmp/r2fes 1000609 120 1000609 0
timeout 300 /tmp/r2fes 1000609 120 1000609 1
OPENBLAS_NUM_THREADS=1 timeout 1200 uv run --with numpy python3 \
  scripts/z51_linnik_windows.py 100000000 3000000 200
timeout 180 uv run --no-project python3 \
  reviews/z51-linnik-review-2-check.py --runs
```

Both C modes completed all 29 odd primes through 113. The windows run completed with 5,051 Mordell-hard primes and 11 windows. The final independent script exited 0 with all assertions passing. The `--runs` option only compares already-produced `/tmp` outputs; without it the mathematical checks are self-contained.

### 5.1 Requested forcing runs

Fractions use the driver's convention: total nonresidues reached divided by total nonresidues in the band, not an unweighted average of per-q fractions.

| quantity | actual p, mode 0 | one-coordinate plane, mode 1 |
|---|---:|---:|
| mean raw labels, 25≤q≤113 | 99.57143 | 24.85714 |
| mean / log³(1000609) | 0.0377552 | 0.00942525 |
| coverage [25,50) | 0.864865 | 0.567568 |
| coverage [50,100) | 0.703601 | 0.401662 |
| coverage [100,120) | 0.526515 | 0.325758 |
| first hole | 29 | 17 |
| residue-class hits | present | zero for every q |

The plane mean 24.86 is **not** a discrepancy with approximately 40: the requested run stops at q=120, whereas the final table's mean covers primes through 300. The independent complete enumeration over that latter range gives:

| band | exact plane coverage |
|---|---:|
| [25,50) | 0.567567568 |
| [50,100) | 0.401662050 |
| [100,150) | 0.320066335 |
| [150,200) | 0.313402062 |
| [200,300) | 0.258928571 |

Mean labels: **39.830188679**. Maximum pivot: **5,706,695**. All 61 odd primes q≤300 passed the independent original-definition comparison at M≤5000. For q≤113, the complete parametrization truncated at PB=1000609 agrees exactly with every label count, reached count, and zero-residue count from the C mode-1 run.

### 5.2 Requested reduced window run

| quantity | reduced [10⁸,1.03·10⁸) | stored full [10⁸,1.2·10⁸) |
|---|---:|---:|
| hard primes | 5,051 | 33,663 |
| mean forced / unforced rate | 0.4683 / 0.2274 | approximately 0.47 / 0.23 |
| pair correlation mean | −0.0087 | −0.0056 |
| pair correlation range | [−0.1149,0.1078] | [−0.0922,0.1098] |
| nonresidue fraction, all | 0.5016 | 0.5010 |
| nonresidue fraction, forced-only failures | 0.3563 | 0.3390 |
| forced-only failures | 236 | 1,556 |

Selected conditional failure probabilities:

| forced count k | reduced bin size | observed | independence prediction | full-table observed / prediction |
|---|---:|---:|---:|---:|
| 2 | 123 | 0.2846 | 0.2939 | 0.2790 / 0.2891 |
| 4 | 826 | 0.0678 | 0.0725 | 0.0681 / 0.0739 |
| 6 | 1,105 | 0.0217 | 0.0193 | 0.0165 / 0.0186 |
| 8 | 440 | 0.0068 | 0.0045 | 0.0054 / 0.0044 |

The reduced experiment supports the qualitative effect; it does not replicate the full interval or prove independence. The stored y=400 JSON agrees with the document's rounded entries (mean correlation −0.0039, failure nonresidue fraction 0.3823); that full run was inspected, **not rerun**.

### 5.3 Independent direct ES check

For all primes p≡1 mod 4 with 5≤p≤200 and primes q≡3 mod 4 with q≤100, the independent script computes the divisor-sum criterion and separately searches y directly. With B=px and y≤z, the exhaustive range is

`B/q < y ≤ 2B/q`, `z=By/(qy−B)`.

It checks integrality and the integer identity `4xyz=p(xy+xz+yz)`. Results: **273 cases, 86 live windows, zero disagreements**. No author's factoring, Legendre, or window functions are imported. The additional p=5,q=7 example verifies the orientation warning in §3.1.

## 6. Labels and summary fidelity: §§0,7,8

**Section 7's R1 repair ledger is substantially accurate**, subject to the inherited ε≤1/8 bookkeeping and the summary scope language noted above. The repaired core proofs do not need to be reverted. This review does not accept unverified objections to the correct h+2 inequality or to the disjoint-fibre argument.

**Section 0 needs MAJOR updates.** Its §4 row promotes a false general p-dependence exclusion to PROVED. Its §5 orientation row inherits the overbroad example list; the 5.3 row rests on a literally impossible (WL_A). Its reverse-role row needs the selector repair and explicit native-family scope. The dense-plane “28% sterile” shorthand must name the checked boxes. “Cubic supply confirmed” is evidence of a finite fit, not an asymptotic theorem. The first-draft universal theorem should remain withdrawn.

**Section 8 is directionally right but not fully faithful.** Preserve that T2-full is not reached and Corollary 3.2 is a cap-relaxation result. Replace item 1(C)'s “bounded-level hybrids” by **bounded whole-period-level hybrids**; retain the per-summand-only case as open. State D with CRT-admissibility, native-family and fibre hypotheses, or separately invoke the appropriate 3/4 ratio-family cap. Add non-CRT/nonperiodic structured p-dependence to the open routes: §4 has not excluded it. Do not identify native sterile points with ratio-class sterile points. Distinguish the measured forced-only window failures from actual E′_y failures, and state the extra asymptotic lottery assumptions.

The PROVED labels are justified for the repaired core, Lemma 4.1, and the local algebra. EVIDENCE is the correct label for the finite generic forcing and lottery observations. CONDITIONAL is appropriate for a **correctly restricted** (WL_A), not for presenting an impossible hypothesis as a viable escape. Assessment does not excuse citing a theorem outside its family scope or asserting universal necessity of pointwise input.

### 6.1 Concurrent addition: §8 item 5, the fibre-majorant hybrid door — SOUND open direction; MAJOR precision repairs

This addition correctly identifies a gap not covered by Proposition 2.8: many cheap summands can jointly involve the block. It appropriately labels the proposed U/ES₅-versus-ES asymmetry as heuristic and the fibre cap as unknown. Native sterile planes have zero ambient Haar measure and, without a thickening/level argument, do not settle this proposed hybrid.

The elementary averaging construction is valid if **0<η<1/2**, Ω_λ is explicitly defined, and each ν_q is globally nonnegative and dominates the stated fibre avoider. Any unbiased point then has enough nonresidue coordinates to make the sum dominate it. The fixed choice κ=0 from the earlier notation gives η=1 and a negative denominator here, so this paragraph needs its own parameter restriction. The precise bias threshold and B_J must be matched to the datum counted by Theorem 3.1.

Two asserted equivalences need correction. First, a power saving requires a power-small **average** `s^{−1}Σ_q Eν_q`, not just power-small means for “most q.” An exceptional fraction 1/log X with means of order one prevents a power saving even though a proportion tending to one of the means are tiny. Second, a small joint majorant mean is not equivalent merely to knowing the conditional nonresidue probability ρ_q: its normalization by the avoider's density, the level cost, and the existence of a majorant attaining the proposed density are exactly the missing input. State the quantitative average-majorant hypothesis directly.

The λ²-versus-λ³ comparison is a coherent label-model calculation, not a proved exclusion of the U/ES₅ hybrid or a proved ES opportunity. Say the old cap **does not directly apply to the weakened domination set**, rather than claiming a new theorem that no such cap can apply. Linnik does not remove “exactly” the square-like points in any literal classification established here.

The appended tilt statistics are clearly EVIDENCE with a stated finite range and loss of survivors. That is an honest label, but I did **not** rerun this concurrently added experiment, and the stated small-q tilt does not validate the growing-q fibre-cap hypothesis. This paragraph usefully acknowledges an open CRT-hybrid route; it does not repair the separate overclaims in §§4 and 6.3.

## Most serious remaining issues

1. **(WL_A) is impossible as written:** unbiased primes p≡3 mod 4 cannot have its q≡3 mod 4 windows. Restrict the hypothesis and quantify it at all sufficiently large scales.
2. **The §4 exact blocking lemma is false:** dimension is not state count; injectivity is not independence; a small-state rule need not be CRT-dependent. Withdraw the general exclusion.
3. **Proposition 6.1 omits nonunit fibres:** add unit selectors, justify the uniform-weight duality/reparametrisation correctly, and handle primes dividing L. The per-summand level bound itself is sound.
4. **Section 6.3 crosses family and logical scopes:** a native 2/3 cap is not an ℛ(M) cap; native sterile points are not proved ratio-sterile; approximate inputs remain possible. A properly scoped 3/4-family cap is available by a different citation.
5. **The numerical models are not forcing theorems:** the runs validate the finite scale, cap-0 criterion and one-coordinate collapse, not uniform independence, large-X window rates, or multi-coordinate ratio sterility.

The useful surviving results are the repaired sparse-plane obstruction, the bounded-whole-period promotion lemma, and the Heath–Brown exponent upgrade. None proves a power-saving ES exceptional-set estimate without genuinely additional input.
