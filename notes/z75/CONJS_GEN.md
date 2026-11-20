## §0
Result: A moving cyclotomic divisor proves (S) on the missing exponent classes for 15·2^s+1, completing ES for this family; one word closes the last four non-square classes mod 840. Label: PROVED (Theorem 1 elementary; full-family ES Lean-verified; Theorem 2 relative to the computer-assisted Z64_SDEEPF Thm 3.6)
Scope: ES(15·2^s+1) for every integer s≥0; (S) on 60|s, s>0, and outside the 24 odd-square classes mod 840; finite class-map tests only. General ES and (S) remain open.
Review: cross-model (Opus, `data/z75/thin_cyclo/REVIEW_OPUS.md`; ACCEPT-WITH-FIXES, applied)
Triage: HEADLINE
STATUS delta: for §1C see the combined row in `THIN_CYCLO.md` §0; replace 28 by 24 in the (S) row (Z64_SDEEPF Thm 3.6 + Theorem 2 below).

## 1. Two proofs about (S)

**Theorem 1 (moving cyclotomic divisor).** For every positive multiple s of 60, n=15·2^s+1 has an interior good word with u=14. In particular **ES(15·2^s+1) holds for every integer s≥0**, including composites. This does not assert (S) on the off-core exponents.

*Proof.* Write s=3^a m with 3∤m, a≥1 and 20|m. If m≡2 mod 3 take r=m. Otherwise take r=m/5: division by 5 interchanges 1 and 2 in the units mod 3. In either case 4|r, r≡2 mod 3, and h=s/(3r) is an odd positive integer (3^{a−1} or 5·3^{a−1}). Put x=2^r and

    A=x²−x+1,   t=(A+1)/14,   u=14,   v=(n+14)/A.

Because x≡4 mod 7, A≡6 mod 7; because x is even, A≡13 mod 14. Thus t is integral. Also A|(x³+1)|(x^{3h}+1) since h is odd, and n+14=15(x^{3h}+1), so v is integral. In fact v≥15(x+1); x≥16 gives t≥2. Now n=vA−14=tuv−u−v. Since 16|x, A≡1 mod 16, so 7t=(A+1)/2≡1 mod 8 and t≡7 mod 8. Since n≡1 mod 8 we have 8|n+t. This proves the good-word assertion without any search or primality hypothesis.

For a direct ES check: v≡7 mod 8 follows from Av=n+14, so B=tv−1 is divisible by 4. Set D=B/4. The positive ES denominators are **ADn, 14D, 14AD**: after multiplying the reciprocal identity by 14ADn it is just 14AB=14+(A+1)n (use 14B=n+v and Av=n+14). For s mod 360 outside {0,240}, invoke `proth15_offcore` in `lean/ES/ES/Proth15.lean`; both residual classes at s>0 have 60|s. At s=0 use 4/16=1/8+1/12+1/24. ∎

**Why the previous no-go does not apply.** `Z53_THIN15.md` Prop 7 excludes finite congruence coverings reaching the square limit exponent μ=0, not a variable-depth extraction. Here D_exponent=s/r can be 3^a or 5·3^a and is unbounded. Dividing by 3 *until the exponent is a unit* and optionally dividing by 5 steers the residue of x at 7 while preserving an odd quotient. Neither an assumed prime factor of Φ₆(x) nor a fixed root degree is needed. Discovery: a bounded-period divisor search kept producing A≡−1 mod 14 with the **same outer letter 14** across unrelated exponent periods; the identity n+14=15(2^s+1) makes that letter special. `Z53_THIN15.md`, `EXP_OPEN.md`, `MENU_STERILITY.md`, and the existing Lean theorem were checked for scope; no external priority claim.

**Theorem 2 (sharp residue reduction mod 840).** (S) holds outside the 24 odd-square classes mod 840. *Proof.* `Z64_SDEEPF.md` Thm 3.6 leaves only those classes and 265,321,769,825. Each extra class is 41 mod 56. For n≥97 there, use

    (t,u,v)=((n+15)/56,8,7).

Then tuv−u−v=n and 8|u, hence the word is good. Every positive n in the four classes is ≥265. This completes the covering. Squares prove the optimum only for **entire residue classes of good words**; this is no obstruction to (S) itself inside the remaining classes. This is an application of SDEEPF Prop 3.2: the scan required 8uv to divide the period, while this witness needs only uv=56 (general period 8uv unnecessary). The ordinary ES residue 41 mod 56 already appears in `notes.md`; the increment is the sharp (S) reduction. ∎

**A square-class prime corollary (rel. Dirichlet).** For arbitrarily large primes q, there are infinitely many p≡1 mod 840 with *least* positive quadratic nonresidue q and *least* good word denominator also q. In fact choose any prime q≡97 mod 112; impose p≡1 mod 840 and mod every prime <q, and p≡−14 mod q. This is a reduced residue class and hence has infinitely many primes p>2q. Reciprocity and (2/p)=1 make every positive integer <q a residue. At A=q take t=(q+1)/14≡7 mod 8, u=14, v=(p+14)/q: the sign is negative by the 2-adic criterion. Dirichlet also supplies infinitely many q. Thus in this explicit family a good denominator can be arbitrarily large yet attain the elementary lower bound exactly. It uses increasing moduli and gives no pointwise upper bound for arbitrary p≡1 mod 840.

## 2. Class-map tests

### Before looking at results
Use the first 40 primes ≡1 mod 24 above each of 210000 and 2100000. First three odd unramified split primes per actual square genus with smaller positive root; top means decreasing exact |b|/a, ties increasing (a,b,c). Apply the same four-class cap after pooling halves and quarters of the smaller-root anchor. For the representation rule also freeze alternate d=2,3,5,7 with p=x²+4da_c² and ideal root 2da mod q; choose least positive a_c (this also defines the composite extension, without a primitivity restriction). Keep prime q only when invertible, and use the Jacobi product on composite inputs. Do not prefilter representation outputs by genus when determining coverage. Match null by exact reduced leading coefficient at the same input and d among target classes (and score out-of-target selections as certain misses); report observed and expected hits, not a calibrated significance test. Compute all five d in windows/F4, d=1,2 at F2 per z70 screen, d=1 on all F3 inputs, and shortcut squares by empty target, independently testing G on the z70 square screen. An absent anchor, representation or q is not a hit. Coverage and null agreement are different questions. Full menus fail as soon as a nonempty G on an input is missed at every tested d. No tuning on screens.

### Results (CERTIFIED counts; EVIDENCE comparisons)

`data/z75/conjs/summary.txt` has all per-d tables, output fractions (sum outputs / sum T), exact rational null totals and first simultaneous failures. Below, cells give **inputs covered / individual class hits / expected class hits**. A covered input has a hit at some tested d. `eligible` counts inputs with G nonempty for at least one tested d; all absences count as misses. `all` is the union of the three rules.

|sample|eligible / tested|mixed|anchor|neighbour incl. extensions|all|
|---|---:|---:|---:|---:|---:|
|W1|40/40|32 / 120 / 91.5|8 / 8 / 9.75|24 / 30 / 30|37|
|W2|40/40|29 / 88 / 61.25|2 / 3 / 4.5|22 / 28 / 28|36|
|F1 odd squares|0/150|0 / 0 / 0|0 / 0 / 0|0 / 0 / 0|0|
|F2 R₈ zeros|12/12|1 / 2 / 1|0 / 0 / 0|9 / 11 / 11|9|
|F3 composites, d=1|276/285|8 / 9 / (41/3)|44 / 52 / (1771/30)|14 / 15 / 15|61|
|F4 star + gstar + named hard zeros|39/39|8 / 30 / 29|7 / 10 / 10.5|6 / 6 / 6|16|

The **original d=1 neighbour** covers 22/40 and 19/40 in W1/W2, with 25 vs 25 and 22 vs 22 hit classes, respectively. The three rules across all d select (800,390,155) classes out of summed |T|=51646 in W1 and (800,400,163) out of 165972 in W2 (for the third rule counts include out-of-target selections). Exact-α is a *descriptive* conditional expectation; for a norm giving just one inversion pair whose goodness is identical it has no power to detect selection within the pair. Neither agreement nor disagreement proves a distribution law. Halving the odd anchor fails as a cover; representation neighbours are productive individual hits, not universal, with no excess in this contrast. All three rules together miss 210193 and 2100001, first simultaneous failures of W1/W2. These are failures of the menus, **not** conjecture (S).

**Proposition 3 (why mixed wins).** Suppose a reduced primitive form [α,β,γ] of discriminant −4dn has |β|=α−1 and α≡−1 mod 4d. Then it belongs to G_d(n), explicitly on the c=1 line. Indeed α divides 4dn+1 by the discriminant congruence; B=(4dn+1)/α≡−1 mod 4d. Set a=(α+1)/(4d), b=(B+1)/(4d). These are positive and 4abd=n+a+b. The natural form of (a,b,1,a+b) has first coefficients (α,α+1); translating the middle coefficient by −2α gives (α,1−α), and the discriminant determines the third coefficient. For the opposite sign use inversion (G=−G by exchanging a,b, `Z70_CLASS.md`). This needs no assumption on how the class was generated. ∎

Splitting **post hoc** on precisely this test gives:

|window|hits vs exact-α expected on test|hits vs exact-α expected off it|
|---|---:|---:|
|W1|110/110 hits, 78 expected|10/690, 13.5 expected|
|W2|86/86 hits, 59.75 expected|2/714, 1.5 expected|

The ranking by |β|/α preferentially selects these classes; matching α does not match β. The certificate accounts for the replicated positive contrast (196 of 208 observed hits), not an independent source of c=1 positivity. Notably mixed **rescues 3361** at d=5: [99,±98,194], with a=5,b=34 (B=679). It misses 2094481 and 85664329 at every d. All rules miss both. At F2,d=2, mixed yields no hit: Prop 3 could not fire there because that very c=1 fibre is empty. At 4545, G₁ is empty (four mixed outputs, no shifted roots, two neighbours, no hits); a prime statement is not inferred from this. At squares no admissible norm can have negative Jacobi symbol; 648 coprime square/d pairs were also checked directly for empty G.

**Exactness/replay.** `scripts/z75_conjs_gen.py` imports the z70 small-fibre solution engine. It builds groups with PARI but, unlike the original run, checks every group size independently by counting reduced primitive forms: for |β|=2r≤α≤γ one needs α|(dn+r²), r≤√(dn/3); count both signs except on the canonical boundaries. It checks distinctness of the enumerated group tuples and the invariant-factor power relations, so candidate enumeration does not require trusting an unverified GRH group size. Split primes are unramified odd primes in ascending order; the target test on them uses Jacobi(q/n)=−1 and the assigned characters at 2 and the odd primes of d evaluated at −1 (a **union** of genera can be allowed on composites, not a prescribed −1 at each prime factor of n). G⊆T is checked. Individual null contributions in JSONL are `[form,hit,good_at_α,total_at_α]` with contribution 0/1 for an out-of-target class. Groups and hits use PARI composition and the existing z70 ideal convention; no second implementation of the entire seed pipeline. `scripts/z75_conjs_check.py` separately constructs every Prop 3 solution flagged in the five nonsquare samples and cross-multiplies 102 thin-family triples (including s=43740); these checks are supplementary to the proofs.

```
ulimit -v 6000000
export PYTHONDONTWRITEBYTECODE=1
timeout 1100 uv run --offline --no-project --with cypari2 python scripts/z75_conjs_gen.py W1 W2 F1 F2 F3 F4
timeout 60 uv run --offline --no-project python scripts/z75_conjs_report.py
timeout 60 uv run --offline --no-project python scripts/z75_conjs_check.py
```

## 3. Boundary and next push

The new word does not use a Markoff involution or a homology conservation law. In fact `Z68_SIGN.md` §10 already tested multi-step rescaling beyond its initial §§1–8 (some starting components miss); that experiment does not give termination. The raw integer balance in `Z63_EUCLID.md` also vanishes mod 4 at **every** p≡1 mod 840, since (p−1)/2 is divisible by 420; over ℤ the nonzero total still includes all lengths. No explanation of the +0.65 correlation, signed descent, or general pointwise character-sum bound is claimed. F1 prohibits a good word at a square by Jacobi; F2/F4 do not forbid our thin-family word (it is not a claim of fixed-slice coverage there); the arguments of Theorems 1–2 do not require primality (F3).

**Round 2:** the Lean formalisation and all three offset-family proofs are now complete (`THIN_CYCLO.md`). The discovery logs `data/z75/conjs/periods-{240,360}.txt` were generated by `scripts/z75_conjs_periods.c` with K=1024, B=2000000, starts 240 and 360; they record the repeated letter 14 (§1), not premises of any proof.
