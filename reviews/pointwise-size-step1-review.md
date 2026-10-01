# Hostile review: POINTWISE_SIZE.md §§0–5 (branch `side-agent/pointwise-size`, Step 1)

Reviewed: `POINTWISE_SIZE.md` at `61b3de8` (Theorem M, Lemma D, (F3'), Lemma I,
Corollary M1, Lemma CT, Theorem C, §3 instances, Proposition A, Corollary E,
§4.3, §5), plus `AGENT_REPORT_C.md` and the two `scripts/pointwise_size_*.py`.
Context read: FORMAL_CLOSURE.md, DEPTH3.md §3, notes Lemma 77.6 and §54.
I did not rely on the author's self-review. Every proof below was re-derived. The
code is independent: it imports nothing from `pointwise_size_*`, `formal2*` or
`formal_closure*`.

## Verdict: **SOUND-AFTER-REPAIRS**

Every load-bearing statement is correct as mathematics, with full proofs:

* Theorem M(a)–(d), Lemma D, (F3'), Lemma I and Corollary M1;
* Lemma CT and Theorem C, including the character formula and the choice of Λ';
* Proposition A.

One claim is **false as literally stated**. That is the §3.3 assertion that the
FORMAL_CLOSURE certificate's own `Λ, E_ℓ` "serve as the data of §1.2", so that
"nothing needs refining" (D1). The certificate violates §1.2's precision rule
`E_ℓ ≥ v_ℓ(D)` at ℓ=2 (it would need 20; the certificate has 14) and at ℓ=233. The
repair is a one-line weakening of the precision hypothesis in Lemma D/(F3'), and it is
proved below. After the repair the "exact instance" claim holds, and so does the
literal 13521-polynomial match, which I verified.

The remaining defects are minor: quantifiers, labels, an unhandled error case, and a
redundant condition. None affects a theorem.

## 1. Re-derivations

**Lemma D.** Let `q≡q* (mod D)`. Since `F∈Z[X]`, we have `F(q)≡F(q*)≡ρ (mod D)`.
Also `A/B=F/D+ε` with `ε=R/B`, where `|ε|<1/D` once `deg R<deg B` and q is large.
Then `⌊A/B⌋=(F−ρ)/D+⌊ρ/D+ε⌋`.

* If `1≤ρ≤D−1`, then `ρ/D+ε∈((ρ−1)/D,(ρ+1)/D)⊂[0,1)`.
* If `ρ=0`, the floor is 0 or −1 according to `sign ε`. When `R=0` it is 0.

The remainder-zero criterion is correct, because the remainder is `B·const+R` with
`deg R<deg B`. The proof uses only `F(q)≡ρ (mod D)`, which matters for D1.

*Machine check:* 2908 random `(A,B,q*)` triples, with all three branches exercised
(`ρ=0,σ<0`: 273). There were 0 mismatches at q above a rigorous Cauchy-bound
threshold. A mutant without the `[ρ=0, σ<0]` correction is caught (78 detections).

**(F3'), including R=0.**

* `B=0`: correct, with the convention `0|0`.
* `R≠0`: `B(q)|A(q)` would give `B(q) | D'A(q)−F(q)B(q)=D'R(q)`. All three
  quantities are integers at admissible q, and `0<|D'R(q)|<|B(q)|` eventually. So
  the answer is robustly false.
* `R=0`: `A(q)/B(q)=F(q)/D'`, and `F(q)≡F(q*) (mod D')`. Correct.

It is also correct that precision is needed only when `R=0`. *Machine check:* 304
DIVIDES calls in random programs (`R=0`: 253, `R≠0`: 51, `B=0`: 51), with 0 mismatches.

**FACTOR/DIVISORS ordering. The brief asked about ties and equal leading behaviour.**
There are no ties, for the following reasons.

* Elements of 𝒫 are primitive with positive leading coefficient, so distinct
  elements are non-proportional. Hence `h/C_h−g/C_g` is a *nonzero* polynomial,
  whatever the leading terms. For example, 6X+1 and 2·(3X+1)=6X+2 are ordered by
  their constant terms. My T2 program contains exactly this pair.
* Formal divisors `d∏(h/C_h)^{j_h}` with `d>0` and distinct `(d,j)` are distinct
  polynomials, by unique factorisation in `Q[X]`. So every pairwise difference has
  an eventual sign, and finitely many comparisons give a threshold.
* At admissible q, `|A(q)|=|K_A|∏r_h(q)^{e_h}`, where the `r_h(q)` are distinct
  primes exceeding every prime of `K_A` (for large q). So the actual divisors are
  exactly the values of the formal divisors.
* The constant primes precede the formal primes for large q, because h is
  nonconstant (a primitive irreducible polynomial has degree ≥1).

*Machine check:* the formal log *including complete divisor lists* matched the
actual log at all admissible q. A mutant ordering, by (degree, constant term), is
caught at 35/35 admissible q.

**Lemma I.**

* Formal floors are integral at ℓ|D because `F(q*_ℓ)≡ρ (mod ℓ^{v_ℓ(D)})`.
* Formal primes are ℓ-adic units at every ℓ, by the definition of `C_h`.
* Hence `v_ℓ(K_A)=v_ℓ(A(q*_ℓ))≥0` at every ℓ. This includes ℓ∉Λ, which is where
  integrality of `K_A` really needs the profinite formulation.
* The (F9) outputs are integral by density of large integers of the class in
  `q*_ℓ+ℓ^{v}Z_ℓ`.

All correct. The engine asserts `K_A∈Z` at every FACTOR, and the assertion never
fired.

**Theorem M(a), the simulation induction.** The invariant (actual register = formal
register at q) holds through every step:

* (P1)/(P2);
* divmod/DIVIDES, by Lemma D and (F3'). A formal zero divisor is an actual zero;
  a nonzero formal divisor is a nonzero actual one beyond a threshold;
* signs;
* FACTOR/DIVISORS, as above;
* (F9), by definition;
* loops, which run over identical lists. A while-test is a sign test.

A finite formal run has finitely many thresholds. The definition of admissibility
cites `q_0` before Theorem M constructs it, but the circularity is harmless.
*Machine check (T1):* 300 random programs combine ring ops, divmod by constants and
by polynomials, DIVIDES, sign branches and `p^{1/k}` comparisons. They were run at
1800 random q of the class, all above an explicitly computed rigorous `q_0`. There
were 0 log mismatches.

**Theorem M(b): are the H polynomials irreducible, primitive, and free of fixed
prime divisors? Yes.**

* *Integrality:* `C_h|M`, and `v_ℓ(h(q̃))=v_ℓ(h(q*_ℓ))` for ℓ∈Λ.
* *Irreducible:* an affine substitution preserves irreducibility.
* *Positive leading coefficient.*
* *Primitive:* at ℓ∈Λ the constant term is a unit. At ℓ∉Λ, the reduction mod ℓ is
  `C_h^{-1}h∘(invertible affine)`, which is ≢0.
* *No fixed prime divisor at ℓ∈Λ:* the coefficients of `y^j` (j≥1) have valuation
  `≥jE_ℓ−v_ℓ(C_h)≥1`, so every value is a unit.

At ℓ∉Λ the authors use (C3), but see D2: it is automatic. H yields infinitely many
y, hence admissible q above any threshold. Distinct y give distinct p. So the
admissible set is infinite under H for exactly the stated family.

**Lemma CT.** The statement agrees with the notes' parametrisations:

* Type II, `kp=4abck−a−b`, gives `(abc,pack,pbck)`.
* Type I, `k(4abc−1)=p(a+b)`, gives `(ack,bck,pabc)`.

I checked both sums against `4/p` by hand. Notes Lemma 77.6 gives `(ab/p)=−1` in
Type II, and `(c/p)=(ab/p)=−1` in Type I. Multiplicativity of the Legendre symbol
then gives (a)–(c). *Independent enumeration* (`review_pointwise_size_ct.py`, a
different algorithm from the author's):

* p≤5000: 15555 solutions (10656/4899), and 1574 two-p-divisible solutions with a
  bare cofactor. These agree with the author's numbers exactly.
* p≤20000: 83652 solutions, with 0 violations of CT(a), (b), (c) or of Lemma 1.3.
  6947 solutions confirm the non-splitting remark in (c).

**Theorem C, the character computation.** From `uq≡−v (mod p)` we get
`u^{deg h}h(q)≡u^{deg h}h(−v/u)=H_h`, and `h(q)=C_h r_h`. Hence
`(r_h/p)=(H_h/p)(u/p)^{deg h}(C_h/p)`; the exponent sign is immaterial for ±1
values. The surrounding facts check out:

* `H_h≠0`, since otherwise `P|h` would force `h=P` for `h,P∈𝒫`.
* `p∤H_h`, because the class makes p a unit at every ℓ∈Λ'.
* Every ℓ∈Λ' has `(ℓ/p)=(p/ℓ)=+1`, because `P(q*_ℓ)` is a square unit. For ℓ=2 this
  uses `p≡1 (8)`, from `E_2≥3`; also `(−1/p)=+1`.

So Λ' (2, primes of u, of every `K_A`, of every `C_h` and of every `H_h`) is exactly
what the argument consumes. The "degenerate outputs" case is handled correctly. So is
the logic "formal SUCCESS ⇒ no admissible q": by itself this is unconditional, and H
then excludes it.

*Machine checks (T2/T3):*

* The character formula was evaluated numerically at every admissible q for every
  `h∈S∖{P}`, including a quadratic h: 0 violations.
* At 231 random square-mimicking points (square at all ℓ≤37), Λ' lay inside the
  specified primes each time, and the formal output was FAIL each time.
* At 281 non-square points the output was SUCCESS each time.
* At admissible q, actual equals formal: 35 admissible q at the square point (p up
  to `~10^{33}`, S containing `72X²+27X+59` with `C=928`), and 13580 at the
  non-square point. There were 0 mismatches of the full log, the witness included.

**The author's toy check** (`pointwise_size_toy_formal.py 2e7`) reruns to a
byte-identical output. Its `sq` point is a genuine Theorem C instance, because its
Λ'={2,3,5,7,11} contains every `H_h` prime: `H_h∈{22,21,18,6,3}`.

## 2. Defects

**D1 (MODERATE). §3.3: "the certificate's Λ and `E_ℓ` serve as the data of §1.2.
Nothing needs refining … Hence the H-family of Theorem M(b) is exactly
FORMAL_CLOSURE's"; and AGENT_REPORT_C item 4.**

§1.2 demands `E_ℓ≥v_ℓ(D)` for every divmod denominator D, and `E_ℓ≥v_ℓ(D')` for
every DIVIDES test with `R=0`. In `BFS_∞`, every non-seed vertex entry W is produced
by an exact divmod with `D=den(W)`, where W is a formal integer `c∏(g/C_g)^e`. The
script `review_pointwise_size_fc_dict.py` checks the certificate. It finds that 2
primes violate the rule:

* ℓ=2: an entry `2254842069·(459X+19)/C·(X+4569)/C'` with `v_2(C)=v_2(C')=10` has
  `v_2(den)=20`, while `E_2=14`;
* ℓ=233: an excess of 1.

So the certificate's data do **not** satisfy §1.2 literally. Raising `E_ℓ` changes M,
which turns the H-family into a reparametrised sub-progression of FORMAL_CLOSURE's
family. It is then no longer "exactly" theirs. FORMAL_CLOSURE's own precision rule
(C2), `E_ℓ≥v_ℓ(c_r)+v_ℓ(den)`, is genuinely weaker than §1.2's. The dictionary row
"(B)/(C2) ↔ (F3') with R=0" hides this.

*Fix (proved).* The proof of Lemma D uses only `F(q)≡ρ (mod D)`. So replace
"`E_ℓ≥v_ℓ(D)`" (and likewise for D') by the intrinsic condition

> **(Prec)** F mod `ℓ^{v_ℓ(D)}` is constant on `q*_ℓ+ℓ^{E_ℓ}Z_ℓ`, equivalently
> `v_ℓ(F^{(j)}(q*_ℓ)/j!)+jE_ℓ≥v_ℓ(D)` for all j≥1.

`E_ℓ≥v_ℓ(D)` implies (Prec). For a quotient that is a formal monomial
`c∏(g/C_g)^{e}`, (Prec) already holds when `E_ℓ>max_g v_ℓ(g(q*_ℓ))`, because every
factor is an ℓ-adic unit throughout that ball. For the `R=0` tests
`DIVIDES(D+s,r)`, the quotient is the polynomial `Q=k∏C_h^β/c_r`, where
`k=(D+s)/∏h^β`, and (Prec) holds at every ℓ:

* At ℓ|c_r: `den(k)=den(D+s)` (Gauss), so
  `Q(x)−Q(q*)∈ℓ^{E_ℓ−v_ℓ(den)−v_ℓ(c_r)}Z_ℓ`. This is integral under
  FORMAL_CLOSURE's (C2), `E_ℓ≥v_ℓ(c_r)+v_ℓ(den(D+s))`.
* At ℓ∤c_r it is automatic. D and s are formal monomials, hence integral on the
  ball, and r is `c_r` times a unit there.

The remaining divmods of `BFS_∞` are also monomial quotients. These are `s²/D`, the
exact quotients y and w, and the reduction `(4Z−P)/gcd`. With (Prec), the
certificate's `Λ, E_ℓ` do serve.

I also checked the other half of "exactly": the literal S of `BFS_∞` is {P} together
with the factors of `4z−p` and `pz` over the *non-dead* z. Polynomials occurring only
in dead entries are never factored by `BFS_∞`. The author did not check this. On the
certificate, none of the 6402 entry polynomials occurs only in dead entries, so
`|S_M|=6402+7119=13521=|S_FC|`. This holds for this certificate, not a priori.

**D2 (MINOR). §1.2 (C3), M(b) proof, and Λ' in Theorem C ("every prime
`≤Σdeg` (for (C3))").**

(C3) is automatic. For ℓ∉Λ we have `ℓ∤C_h`, so `v_ℓ(h(q*_ℓ))=0` for every h∈S. Hence
the residue `q*_ℓ mod ℓ` is a root of no h∈S.

The phrasing "must also satisfy (C3) … can always be arranged by adjoining the
offending ℓ" suggests a binding constraint where there is none. (C3) is needed only
when a congruence *class* is lifted to a profinite point, as in §3.3 and in
FORMAL_CLOSURE. *Fix:* state it as a remark. In Theorem C, drop "every prime
`≤Σdeg`" from Λ', or label it harmless.

**D3 (MINOR). §1.1 (P5)/§1.2 (F5): `DIVISORS(0)` is not totalised.**

Only `FACTOR(0)` and division by 0 are. The claim "a bounded program halts on every
input", and the claim that the formal run is defined at `q*_univ`, both need
`DIVISORS(0)→FAIL`, both actually and formally. *Fix:* add it to the totalisation
list.

**D4 (MINOR, quantifiers). Corollary E, §0 Theorem C bullet.**

* Corollary E says "at every square-mimicking, universally nondegenerate point"
  without naming P. Its hypothesis is about `p≡1 (24)`. This is right for
  `P=24X+1`. For a general linear P, Theorem C's admissible p are only `≡1 (8)`
  unless 3∈Λ'. *Fix:* say "for `P=24X+1`" (or every linear P), and add 3 to Λ'.
* §0 states "Every bounded witness-producing procedure fails" and omits
  **correct**. Without correctness the claim is false: "output SUCCESS (1,1,1)" is a
  counterexample.
* §0 says "the same holds for unbounded procedures whose formal run at a
  square-mimicking point is finite". This also needs "(universally) nondegenerate",
  or at least nondegeneracy for the factors of the output denominators that Π'
  factors.

**D5 (MINOR, label). §4.2 E1 example: "Every finite truncation is bounded, so
Theorem C makes every iteration formally FAIL at `q*_univ`".**

Theorem C proves FAIL at admissible q, which holds unconditionally. *Formal* FAIL
follows only if admissible q exist, which is the H part. As written, the sentence is
unlabelled and cites a conditional theorem. *Fix:* mark it CONDITIONAL on H. There is
also an unconditional route: the window test verifies the identity, so a formal
SUCCESS would be a polynomial identity covering a square class, which Schinzel's
theorem forbids.

**D6 (MINOR). §4.2 E2, least non-residue.**

The argument invokes H ("Under H, which makes the admissible q exist"), but (F9)
quantifies over *all* large q of a class. A constant value c∉Λ is excluded
unconditionally by CRT/Dirichlet inside the class. Also, "least non-residue mod r"
for composite or square r needs a definition. *Fix:* give the unconditional argument
and specify the primitive's domain.

**D7 (MINOR, scope wording). §0 Scope 1 / §4.1.**

Proposition A is correct, including the case of irrational `c^b`. It covers
comparisons whose sign is *eventually constant*: the same proof works for any
Hardy-field threshold, such as `p^θ(log p)^k`, `r₁^{θ₁}` against `c·r₂^{θ₂}`, or
`log p`. Archimedean tests whose answer oscillates along every class are not inside.
Examples are fractional-part or nearest-integer tests on `p^θ`, such as
"`{√p}<1/2`". They fall under E2 only because they implicitly need `⌊p^θ⌋`.

The headline "size information … is inside the scope" is correct for eventual-sign
comparisons of formal quantities. It should say that, and list oscillating
archimedean tests under E2 explicitly. Proposition A therefore does *not* put "all
archimedean comparisons" inside. It covers exactly the eventual-sign ones, which is
what the proof gives.

**D8 (COSMETIC).**

* §1.2: "`d|K_A`" should read "positive `d|K_A`", i.e. `d||K_A|`.
* Theorem M(a) cites `q_0` before constructing it (admissibility (3)).
* Lemma D should state `σ:=0` when `R=0`.
* §0 calls E3 "probably does not escape", while §4.2 says it is **open**. The
  wording should agree.

## 3. Answers to the brief's specific questions

| question | finding |
|---|---|
| Lemma D | correct; uses only `F(q)≡ρ (mod D)` (basis of the D1 fix) |
| eventual order of FACTOR/DIVISORS, ties, equal leading terms | strict total order by non-proportionality and unique factorisation; no ties possible; machine-checked, with a mutant detected |
| (F3') incl. R=0 | correct; precision needed only for R=0 (and (Prec) suffices) |
| Lemma I | correct |
| induction incl. loops and thresholds | correct; a rigorous threshold computed per run, 0 mismatches above it |
| admissible set nonempty/infinite under H as stated | yes; family irreducible, primitive, no fixed prime divisor ((C3) automatic, D2) |
| Theorem C character formula and Λ' | correct; Λ' is exactly what is consumed; checked numerically |
| Theorem F dictionary exact? | in substance yes, and S matches literally (13521, verified); the precision data do **not** match §1.2 as written (D1); exact after the (Prec) repair |
| DEPTH3 Thm 2 as instance | yes at statement level; DEPTH3's H-family is larger (it also factors `D+s`, adds leading-coefficient primes and primes ≤Σdeg), which is harmless |
| Proposition A scope | eventual-sign comparisons only (D7) |
| Corollary E quantifiers | correct for `P=24X+1`; needs P named and 3∈Λ' otherwise (D4) |

## 4. Code and data (all memory-bounded, ≤1 core)

* `scripts/review_pointwise_size_engine.py`. One program text runs on two machines,
  `ActualMachine` and `FormalMachine` (a literal implementation of §1.2 at a lazily
  specified profinite point). The engine:
  * compares the full instruction logs;
  * computes a rigorous `q_0`;
  * runs T1 (random programs), T2 (an adaptive ES program with a Euclid while-loop,
    FACTOR/DIVISORS, a formal-prime-dependent Type I step creating a quadratic h,
    and a `√p` size filter) and T3 (a Theorem C scan);
  * runs mutation tests.

  Output: `data/review_pointwise_size/engine_run.txt` (under 50 min).
* `scripts/review_pointwise_size_ct.py`: independent Lemma CT enumeration.
  Output: `data/review_pointwise_size/ct_5000.txt`, `ct_20000.txt`.
* `scripts/review_pointwise_size_fc_dict.py`: the D1 data (S_M vs S_FC; precision).
  Output: `data/review_pointwise_size/fc_dict.txt`.

```
(ulimit -v 8000000; PYTHONPATH=scripts uv run python scripts/review_pointwise_size_engine.py 300 30000000)
(ulimit -v 8000000; uv run python scripts/review_pointwise_size_ct.py 20000)
(ulimit -v 8000000; uv run python scripts/review_pointwise_size_fc_dict.py)
```
