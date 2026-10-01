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

---

# Round 2 / Steps 2–3

Reviewed: branch `side-agent/pointwise-size` at `a428b50`.

* **(a)** Commit `0bd5d80`: the D1–D8 repairs.
* **(b)** New §§7–12 and `AGENT_REPORT_C.md`.
* The Chang source, `sources/lit2026/chang-short-character-sums-composite-moduli.txt`.

New independent code: `scripts/review_pointwise_size_step3.py`. Its output is
`data/review_pointwise_size/step3_checks.txt`, and every check passed.

## Overall verdict (Round 2): **SOUND-AFTER-REPAIRS (minor repairs only)**

Every item labelled PROVED in §§7–11 is correct, or correct modulo the cited
theorem it names.

* No heuristic statement is labelled PROVED.
* Prop 11.4 is labelled SKETCH.
* Assessments 7.2, 8.5, 9.2, 11.5 and 11.6 are labelled as such.

One PROVED line contains a false formula, R2 below: Prop 7.1(b) gives the wrong
constant, contradicting Lemma 11.1. Everything else is a label, a stale cross-reference
or a small proof gap.

## A. Status of D1–D8

| | status | note |
|---|---|---|
| D1 | **FIXED** | (Prec) is introduced, Lemma D/(F3') are restated, and §3.3 is rewritten correctly. Nit R1 below; it is my own error, copied from my D1 text. |
| D2 | **FIXED** | (C3) is now a remark, automatic at a point. It is dropped from Λ' in Theorem C. |
| D3 | **FIXED** | |
| D4 | **FIXED** | 3 is added to Λ', so admissible values are `≡1 (24)` for every linear P. The parenthetical in Corollary E is now redundant but harmless. "correct" and "universally nondegenerate" are added. |
| D5 | **FIXED in §4.2** | The H-route and the Schinzel route are both given. The same issue recurs at Prop 8.4(c) (R3). |
| D6 | **FIXED** | Nit: for `c|M_g`, the step `(c/p)=(p/c)` needs `p≡1 (4)`, and needs `p≡1 (8)` when c=2. Simply pass to the subclass mod `lcm(M_g,8c)` compatible with q*, as in the `c∤M_g` case. |
| D7 | **FIXED** | |
| D8 | **FIXED** | |

**R1 (minor; reviewer erratum).** §1.2 (Prec) reads "Equivalently,
`v_ℓ(F^{(j)}(q*_ℓ)/j!)+jE_ℓ≥v_ℓ(D)` for all j≥1". I wrote the same in D1, and
it is wrong. The Taylor condition is only **sufficient**. Counterexample: take ℓ=2,
`F=(X−a)²−2^E(X−a)` and `D=2^{2E+1}`.

* Constancy holds on the ball: `F(a+2^Et)−F(a)=2^{2E}(t²−t)≡0 (mod 2^{2E+1})`.
* The j=1 term fails, since its valuation is `E+E=2E<2E+1`.

Nothing downstream uses the converse. *Fix:* replace "Equivalently" with "A
sufficient condition is".

## B. Steps 2–3: verdict per item

| item | verdict | checks |
|---|---|---|
| Prop 7.1(a) | **SOUND** | |
| Prop 7.1(b) | **DEFECTIVE formula** (R2) | |
| Theorem 8.1 | **SOUND** | ⇐ by Lemma 77.1. For ⇒: any p-free denominator x gives `q=4x−p>0`, `q≡3 (4)`, and `gcd(x,q)=gcd(x,p)=1` (so "for q<3p" is unnecessary, R8). The equivalent (s,u,v) form was re-derived. |
| Lemma 8.2 | **SOUND** | re-derived; 40292 brute-force (p,q,r) checks, 0 violations |
| Cor 8.3(a)(b)(c) | **SOUND** | (b): cyclic group of order 2m with m odd; 7345 prime windows, 0 violations |
| Prop 8.4(a) | **SOUND** | The hypotheses force `p>max(K,5)`, since p would otherwise have to be a residue mod itself. So `q≤K<3p` and Lemma 8.2 applies. |
| Prop 8.4(b) | **SOUND as CONDITIONAL** | No fixed prime divisor: the number of forms `⌊(K+1)/4⌋+1` is `<ℓ` for `ℓ∉Λ_K`, and the values are units on Λ_K. The repair remark (`x_19=5` resp. `p=49`) was re-derived and is correct, using the parities and residues mod 3 of `x_11`, `x_19`, `x_31`. |
| Prop 8.4(c) | **label** (R3) | |
| Lemma 9.1 | **SOUND, small proof gap** (R4) | 6750 seeded windows, 3414 of them with `n_p=2`; 0 violations |
| Lemma 11.1 | **SOUND** | `log L*/T`=0.6016, 0.6618, 0.6655, 0.6662 at T=10², 10³, 10⁴, 10⁵ |
| Thm 11.2(a) | **SOUND** | `1∉𝓡(M)` for all M≤20000. For T=15…47 the least prime `≡1 (L*(T))` has W recomputed independently: 39, 59, 47, 43, 139, all `>T`, all Mordell-hard. This matches `omega.txt`. |
| Thm 11.2(b) | **SOUND modulo Chang Cor. 11, correctly quoted** | see §C |
| Thm 11.2(c), (d) | **SOUND** | arithmetic `3/(2L)` checked; `p>L*` gives the 3/2 ceiling |
| Thm 11.2' | **SOUND modulo Chang** (label R6) | `R(T)` is T-smooth with `log R=θ(T)+log 4`, so `log p≤(12/5+o(1))T`, giving 5/12. The joint statement holds because `log lcm(R,L*)=(1+o(1))T`. |
| Prop 11.2'' | **SOUND** | see below |
| Lemma 11.3 | **SOUND** | 120 primes were constructed from random (q,Q,c); `−1∈Rat_q(x_q)` for all, by brute force |
| Prop 11.4 | **correctly labelled SKETCH** | The parity step and the "≤2 large bad primes for ε<1/6" step are right. The `ε^{3/2}` vs `ε^{1/2}` balance is plausible but unchecked, as the sketch says. |
| Lemma 11.7 | **SOUND** | see below |
| Assessments 7.2, 8.5, 9.2, 11.5, 11.6 | **labelled correctly** | 8.5 re-derived: `log P=−(Q/8)log log p(1+o(1))`, so `Q≥(8+ε)log p/log log p` |
| §7 multilevel splitting | **SOUND (unbiased)** | see §D |

**Prop 11.2'', re-derived step by step.**

1. Notes Thm 56.1 is stated for exactly this "prime certificate" notion. It gives
   `P_3(T)|Q`, using `D=1` at `M=ℓ`.
2. `𝓡(3)={2}` and 3|Q force `c≡1 (3)`.
3. At `M=3ℓ`, `D=r|(3ℓ+1)/4` with `r≡2 (3)`, the class `−4r` is `≡1 (3)`.
   Compatibility with c mod Q is needed only mod `gcd(Q,3ℓ)=3` (with ℓ∤Q). The class
   is a unit mod ℓ, since `r∤ℓ`. The script exhibits 9 explicit atoms with
   `W(p)≤3ℓ` on the combined class.
4. The exceptional ℓ have relative log-density `∏_{r∈S}(1−1/(r−1))` inside
   `ℓ≡1 (4)`. This tends to 0, because `Σ1/r` diverges over `r≡2 (3)`.

Hence `log Q≥T/2+T/6−o(T)`. Correct.

**Lemma 11.7, re-derived.**

* `log Q_y=θ(y)+O(√T)`: only `ℓ≤√T` carry exponent ≥2.
* Rough `M=mℓ` with `ℓ>y>√T` has `m<T/y<y`, so `m|Q_y`.
* `F_ℓ` never contains 0, since `ℓ∤D|((mℓ+1)/4)²`.
* `f_ℓ<ℓ/2`.
* The coordinates mod primes in `(y,T]` are independent of each other and of
  `n mod Q_y`.

*Machine check of the reduction* at T=4095, y=101: `F_ℓ` was computed exactly
(max `|F_ℓ|/ℓ=0.186`). Two directions were tested:

* 20000 random `n≡1 (Q_y)`: "W(n)>T" ⇔ "n mod ℓ∉F_ℓ ∀ℓ>y", with 0 mismatches.
* 2000 local survivors, all with `W(n)>T`: 0 failures.

The resulting rigorous bound, `log(1/δ*(4095))≲θ(101)+9≈100`, is consistent with the
measured 18.8.

*Remark (not a defect).* Combined with RA, Lemma 11.7 already gives heuristically
`W(p)>(log p)^{2−ε}` infinitely often from a *proved* Haar input. It may be worth
stating this next to Assessment 7.2.

## C. The Chang citation (read in the source)

**Exact statement.** Corollary 11 of the source reads: "Assume q satisfies that
`log p=o(log q)` for any `p|q`. If `(a,q)=1`, then there is a prime `P≡a (mod q)` such
that `P<q^{12/5+o(1)}`." The §11.1 quotation is accurate. 12/5 is Huxley's
zero-density exponent, from the third term of (8.4).

**Siegel zeros.** Siegel zeros are **not an exception**. The deduction
(source, after (8.4)) splits into two cases:

* `γ=(1−β_1)log q` small: Heath-Brown [HB2, Cor. 2] gives a prime
  `<q^{2+δ}<q^{12/5}`.
* Otherwise: `1−x^{β_1−1}/β_1≫1`, so (8.4) is positive.

So the corollary is unconditional, and Theorem 11.2(b) needs no Siegel caveat. The
"missing input, not handled" wording of `2472c15` refers to §11.3's superlinear route,
which is correct there. It is not about Thm 11.2.

**Uniformity at the borderline.** Read literally, the hypothesis is about a family
`q→∞` with `max_{p|q}log p/log q→0`. To absorb the `(log q)^C` loss in the Huxley
term, Chang's half-page deduction needs `θ log q≫log log q`. Under the bare
hypothesis `log P=o(log q)` this is not evident from the text.

Our moduli are far inside the safe range: `log P≈log T≍log log q`. Theorem 10 then
gives `θ log q≥c·min(log q/log P,(log q)^{c'})→∞` much faster than `log log q`. The
application is robust even if Corollary 11 were imprecise at its borderline.

**Effectivity.** It is not stated. The ingredients appear effective: Theorem 10's
region, Huxley, and HB2 Cor. 2 (which is effective). But we did not check this.
Notes Thms 54.1/54.3 are explicitly effective. §12 calls them "superseded in their
constants" and should say that the new constants come without a stated effectivity
claim (R6).

The 12/5 for smooth moduli is, to my knowledge, the commonly cited form of Chang's
result. Status: **PROVED modulo a cited theorem** is the right label.

## D. §7 Monte Carlo methodology (spot level)

I read `pointwise_size_wtail.py split`.

* The residues `n mod ℓ^{kmax(ℓ)}` are drawn **lazily**, at the first M divisible
  by ℓ, and at the full precision any later `M≤TMAX` needs. So the state of a
  particle is exactly the set of residues already drawn.
* At a threshold, the estimator `alive·weight` is recorded *before* splitting. Every
  survivor is then replicated `f=⌊batch/alive⌋` times, and the weight is divided by
  f.
* Clones share the drawn past, and they draw all not-yet-drawn primes independently.
  That is the correct conditional law of the future given the past.

So `E[Σ weights]` is preserved at every split (fixed-factor splitting with a
state-dependent factor is still a martingale), and the estimator is **unbiased**.

The hard-class normalisation is right: M is odd, so only `n≡1 (3)` matters, and the
script imposes it.

*Independent plain Monte Carlo (no splitting)* agrees:

| T | plain MC | split estimate |
|---|---|---|
| 127 | `4.29e−3±1.0e−4` | `4.21e−3` |
| 511 | `8.20e−5±5.2e−6` | `8.24e−5` |

*Caveat (EVIDENCE quality only).* With f up to `batch` (50000 clones of a single
particle), the estimator is extremely heavy-tailed. At T=65535, two of four runs give
0. The sample mean of a few runs then typically *underestimates* δ*, because the
median lies below the mean. So `−log δ*≈38.5`, and the ratio 0.74 at the top of the
table, are biased toward faster decay. The text already flags the noise. The
direction of the bias should be stated too.

## E. Defects (Round 2)

**R1 (MINOR).** (Prec) "Equivalently" should read "sufficient". See §A.

**R2 (MINOR–MODERATE; PROVED line with a false formula).** §7.1 Prop 7.1(b) says
"`δ*(T)≥1/φ_h(L(T))=e^{−(1+o(1))T}`", and the text after it says
"`L(T)=e^{(1+o(1))T}`". Here `L(T)=lcm(24, M≡3 (4), M≤T)` is exactly §11's `L*(T)`, and
Lemma 11.1 proves `log L*=(2/3+o(1))T`.

* The inequality `δ*≥e^{−(1+o(1))T}` remains true, but weaker.
* The equality is false.
* Lemma 11.7 itself cites the correct `e^{−(2/3+o(1))T}`.

*Fix:* `1/φ_h(L(T))=e^{−(2/3+o(1))T}` (Lemma 11.1). In §7.1, `L(T)=e^{(2/3+o(1))T}`.

**R3 (MINOR, label).** §8.3 Prop 8.4(c) is labelled "PROVED: every truncation … is
formally refuted at `q*_univ` (Theorem C)". Theorem C yields *formal* FAIL only via
the existence of admissible q, which is the H part. This is D5 again.

*Fix:* label it "PROVED modulo Schinzel's theorem (cited), via the §4.2 E1 route; or
CONDITIONAL on H via Theorem C". The Schinzel route applies because a formal SUCCESS
of a window test is a polynomial identity.

**R4 (MINOR, proof gap).** §9 Lemma 9.1's proof uses Jacobi reciprocity for odd n.
The lemma is stated for all `p≡1 (4)`, and `n_p=2` occurs when `p≡5 (8)`.

* The statement still holds there: `q≡−p≡3 (8)`, so `(2/q)=−1`. My check covered 3414
  such windows.
* The step "(Cor. 8.3(b))" for prime q imports Lemma 8.2's hypotheses `p≡1 (8)` and
  `q<3p`. These are not needed: `(n/q)=−1` already makes n a non-square mod the prime
  q, so the subgroup contains −1.

*Fix:* add the n=2 line, and argue directly.

**R5 (COSMETIC, stale cross-references).**

* §0 Scope 3, §4.3 (Q1), §7.3 ("the class of one gives only `W>log p/5.2`, and
  nothing better is proved") and the §10 table ("`W>log p/5.2`") are all superseded
  by Thm 11.2 (5/8) and 11.2' (5/12).
* §9 ("Escape … CONDITIONAL on H, through §4.2's argument for `n_p`") and §10 (a)
  ("conditionally on H"): after the D6 repair, §4.2's `n_p` argument is
  unconditional. These labels are now over-cautious.
* "Hard" means `p≡1 (24)` in §7 but Mordell-hard in §11. Say so where it switches.

**R6 (MINOR, labels).**

* Theorem 11.2' carries no status label. It should read "PROVED modulo Chang
  Cor. 11 (cited)".
* §12 and Theorem 11.2 should state that effectivity is not claimed or checked, in
  contrast with notes §54 (§C).

**R7 (REMARK).** The Chang hypothesis is used far inside its safe range (§C). Add a
sentence saying `log P≍log log q` for `L*(T)` and `R(T)`.

**R8 (COSMETIC).** §8.1: "For `q<3p` the second follows from the first". In fact
`gcd(x,q)=gcd(x,p)` for every q, so it always follows.

## F. Replay

```
(ulimit -v 8000000; uv run python scripts/review_pointwise_size_step3.py)   # ~10 min, 1 core
```
