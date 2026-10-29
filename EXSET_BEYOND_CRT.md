# EXSET_BEYOND_CRT — the CRT-architecture barrier (audit; word-class ceiling 2/3 and its attainment at primes; no barrier broken) for the ES / ES₅ exceptional set

Wave z50, lane (A), slug `ncrt`. ES is OPEN; nothing here claims otherwise.
Scripts: `scripts/z50_ncrt_*`; data: `data/z50_ncrt/`.

## §0 Summary table (one-line verdict: no CRT barrier is broken; the U/ES5 word-class architecture is capped at 2/3 and attained at primes)

| # | Claim | Label | Section | Hostile review |
|---|-------|-------|---------|----------------|
| 0.1 | Round-1 audit: union of barred method classes (Thm 1.1) and the comparison-measure definition of "non-CRT" | conjunction of PROVED internal results; Assessment for the operational definition | §1 | (pending) |
| 0.2a | Word-class certificate families are not K2 families as parametrised families (Prop 1.2); set containment undecided (EVIDENCE for small moduli) | PROVED / EVIDENCE | 1.3 | review 1: SOUND-WITH-REPAIRS (D1-D3 applied) |
| 0.2b | Theorem 2.1: supply exponent beta gives cap lambda^{beta/(beta+1)}; Cor 2.5: word-class architecture for U/ES5 (all groupings, non-reduced pair classes, selectors) capped at lambda^{2/3}(log lambda)^{2/3}, M1/M2/L1/C transferred | PROVED given K2/EK (after repairs D4-D10) | 2 | review 1: MAJOR, repaired (scope narrowed); review 2 below |
| 0.2c | Theorem 3.1: #{p <= N : U(p) fails} and #{p <= N : ES5(p) fails} << N exp(-c(log N)^{2/3}), no log log loss; also y-rough n, short intervals | PROVED rel. BV, BT (adaptation of I3_DEEP_ASTRA 8.8 / lane E 7.3) | 3 | review 1: SOUND-WITH-REPAIRS |
| 0.4 | Divisor switching: min modulus <= (2n+4)^{2/3} (Prop 4.1), bounded mass factor (Prop 4.2), switched detectors (with certificate refinements) capped (Thm 4.3); the high-lcm Bonferroni terms are a D2-type correlation problem, no unconditional depth threshold | PROVED / Assessment | 4 | review 2: MAJOR items repaired (R2-5, R2-6) |
| 0.5 | Primes (door D7): no applicable prime-specific input found | Assessment, no barrier claimed | 4.3 | review 2: overclaim removed (R2-8) |
| 0.3 | Open doors D1-D8 in my words; chosen: D8 (class universe) and D1 (divisor switching) | Assessment | §1.4 | — |

## §1 Round 1 — exact audit

Conventions. K2 = `EXCEPTIONAL_KARY2.md`, K3 = `EXCEPTIONAL_KARY3.md`, LS*k* = `EXCEPTIONAL_LARGESIEVE`*k*,
IF/IF2 = `EXCEPTIONAL_INTERFREQ{,2}`, NC = `EXCEPTIONAL_NONCRT`, TU/TU2 = `EXCEPTIONAL_TUPLES{,2}`,
PL = `EXCEPTIONAL_PRIMELAW`, WT/WT2 = `EXCEPTIONAL_WEIGHTS{,2}`, SPW/SPW2, ET-file = `EXCEPTIONAL_THETA`,
ElT = Elsholtz–Tao (2013). A *class* is `b mod G`. A *majorant* of a set 𝒜 ⊂ ℤ is a finite real combination
`ν = Σ_i a_i 1[n ≡ b_i (d_i)]` with `ν ≥ 0` on ℤ and `ν ≥ 1` on 𝒜; its *level* is
`max_i Σ_{ℓ | d_i, ℓ > W} log ℓ` (K2, W absolute). `𝒜(𝔊)` is the set of ALL integers in no class of the finite
family 𝔊 (a periodic set).

### §1.1 What the 3/4 note proves and how (read in full)

`paper/es-threequarter-note.tex` (version C2, internal) proves `E(N) ≪ N exp(−c(log N)^{3/4})`. The mechanism, in
five steps, with the exact place each parameter enters:

1. **Atoms.** `A = (k,ℓ,u,v)`, `k ≤ K = X^κ`, `k ≡ 1 (4)`, ℓ ∈ (X^{1/2}, X] prime, `H = K^{10} < u,v ≤ ℓ^{1/6}`,
   `4uv | kℓ+1`; class `E_A = {n ≡ −u v^{−1} (mod kℓ)}` (Lemma 2.1: a Type II identity; it is an `ℛ(kℓ)`-class
   with `D = u²w`, `w = (kℓ+1)/(4uv)`). The family is fixed, independent of N.
2. **Conditioning.** Given `c = n mod L_K` (`L_K = lcm K(K)`, astronomically larger than N) and `n mod P_y`, the
   residues `n mod ℓ` are independent and the active atoms at one ℓ occupy distinct classes mod ℓ
   (Lemma 2.2). So `H_X = Σ_ℓ I_ℓ`, a sum of independent Bernoullis in every fibre. This is a CRT computation; the
   fibres are never enumerated on [1,N].
3. **Cubic supply** (Thm 4.2, Cor 4.3): `μ_c = Σ_ℓ f_c(ℓ)/ℓ ≍ t² h(J_c) ≤ C t³` in every fibre (Brun–Titchmarsh
   up; BV + Shiu + Cauchy–Schwarz down, uniform in c and J). The exponent 3 = 2 (two free divisors u, v of
   `(kℓ+1)/4`, i.e. `τ_3`-type supply) + 1 (the multiplier harmonic sum `h(K(K)) ≍ log K`).
4. **Void and moments.** Selector `S_y`, `y = Bt³`, makes low-mass fibres exponentially rare (Lemma 6.1:
   `P(H_X = 0 | S_y = 1) ≤ e^{−c_v t³}`); factorial moments `E((H_X)_m | S_y=1) ≤ (C_u t³)^m` for every m (Thm 5.1).
5. **Assembly.** `ν_X = S_y·Q_r(H_X)`, `r ≍ t³` even Bonferroni. `Eν_X ≤ e^{−c t³}`; expansion into
   `T_abs ≤ e^{C t⁴}` classes (each degree costs a choice among `e^{O(t)}` atoms); count on [1,N] with error ≤ 1
   per class: `Σ_{n≤N} ν_X ≤ N e^{−ct³} + e^{Ct⁴}`. Balance `t ≍ (log N)^{1/4}`. All n: multiplicative semigroup
   + Rankin (ES is divisor-closed).

**The single binding constraint** is step 5's ledger: depth `r ≍ mass ≍ t^{B}` times cost per atom `≍ t` must be
`≤ log N`. With supply exponent B the saving is `(log N)^{B/(B+1)}`. Every other step (BV, Shiu, conditioning)
has slack. Note for §1.3: B is a property of the **class family**, and the 3/4 needs B = 3, which comes from
`τ_3`-type (two-free-divisor) Type II classes. That fact is decisive below.

### §1.2 The barred union (theorem-style statement)

**Theorem 1.1 (the barred union; a conjunction of internally PROVED results, as labelled in DISCOVERIES (D)17–(D)29;
not re-proved here).** Let 𝔊 be any finite family of classes of the four K2 types — `ℛ(M)` (`−4D mod M`,
`M ≡ 3 (4)`, `D | ((M+1)/4)²`), `(a,D)` (`−(4D+a) mod 4a·g(D)`), Case A (`−m^{−1} mod 4g(d)`, `m | 4d+1`) and
selector (`0 mod p`) — mixed arbitrarily, arbitrary moduli, every prime of every modulus `≤ N^A`. Let
`𝒜 = 𝒜(𝔊)`. Every bound `#(𝒜 ∩ [1,N]) ≤ 𝐁` produced by one of the following satisfies
`log(N/𝐁) ≤ C_A(log N)^{3/4}` (in (L2), (L3) with an extra `(log log N)^3`):

* **(M) majorant evaluations.** ν a majorant of 𝒜 (≥ 0 on ℤ, ≥ 1 on all of 𝒜), and
  * (M1) coefficient rounding `𝐁 = N·Eν + Σ|a_i|` (K2 Cor 6.1, K3 Cor 4.2) — covers Bonferroni, Selberg Λ²,
    β/Rosser, CRT-evaluated moments of any order;
  * (M2) any evaluation at all (exact counts, dispersion, Kloosterman, Vaaler, smoothing) **provided every
    modulus `d_i ≤ N/2`** (IF Cor 2.3, via Selberg's minorant: `Σ_{n≤N}ν ≥ (N−D)Eν`);
  * (M3) any evaluation whose bound dominates `T_>^*/c`, the least coefficient mass on moduli `> N/2`, with
    `c ≤ exp(C(log N)^{3/4})` (IF Thm 2.5);
  * (M4) per-frequency weighted rounding `N·Eν + Σ_{θ≠0}|ν̂(θ)|w(θ)`, `w ≥ 1` — **only for ET-file Cor 3.4
    prime-slice families** (NC Thm 2.3), no bound on slice primes needed there;
  * (M5) hybrids charging classes of modulus > N/2 their trivial count, when the right-signed large mass is
    `≤ c·𝐁` (IF2 Cor 5.1); beyond that only CONDITIONAL on weak SPW (IF2 Thm 5.2; SPW2 Lemma 1.1).
* **(P) prime-law methods.** ν ≥ 0 at primes, ≥ 1 at the primes of 𝒜, bound `π(N)E*ν + Err` with all moduli
  `≤ N^A`; includes any BV/BDH/EH/GRH-quality Err (PL Cor 4.2; NC Thms 3.2–3.3).
* **(L) large sieves.** (L1) every CRT-admissible Bessel-type inequality with periodic rows of polynomial period
  (additive, multiplicative, Gauss-sum, mixed, fibrewise) (LS1 Thm 3.1, LS2 Thm 2.4, Cor 2.5), and the large sieve
  applied to primes (LS2 Thm 3.1); (L2) at **any** frequency level, for mixtures with ≤ 1 prime above
  `exp((log N)^{1/4})` per modulus (LS3 Thm 3.1); (L3) at any level for residue-sparse multi-rough mixtures
  (LS4 Thm 5.2, Cor 5.3); (L4) Gallagher's larger sieve with prime-power kernels: saving `≤ 26 log log N + C`
  (LS2 Thm 4.3).
* **(C) correlation input.** Order-k majorants save `≤ C(k log N)^{3/4}` (TU Cor 3.4 + K3), so bounded-order
  correlation data of any precision, evaluated with CRT main terms, is useless (TU Thm 3.1, Cor 3.3); degree-k
  moment methods save `O(k log log N)` (NC Props 4.1–4.2); TC_θ (literal form) is obstructed above 2/3 (TU2).

**Common mechanism (LS2 Lemma 1.1, PROVED given K2).** All of (M1)–(M3), (L1) and (C) are consequences of one
object: for every finite set 𝒟 of moduli of level ≤ λ there is a probability measure π on `𝒜 mod M'` with
`E_π f ≤ e^{Cλ^{3/4}} E_U f` for every `f ≥ 0` in the span of classes of 𝒟. A method is barred as soon as its
certificate (the inequality it actually uses) would remain valid if the integers in [1,N] were replaced by
"N copies of π". So the **operational definition of "non-CRT"** is: *an inequality that is true for [1,N] but
false for N·π for every comparison measure π of level ≲ log N.* (P) is the same statement on unit groups.

**Hypotheses that are NOT in the union** (these define the open doors, §1.4): ν ≥ 0 only on [1,N] or only at
primes ≤ N with period > N^c; primes of the family beyond `N^{O(1)}`; per-frequency weights `< 1` (reduced to the
shift-uniform avoider count (W_𝔊), WT Cor 2.2, open); right-signed large-class mass at moduli in (N/2, CN]
(weak SPW, open); large sieves at super-polynomial frequency level against residue-DENSE classes with ≥ 2 primes
above `exp((log N)^{1/4})` ((A*)/(DCC)/(RD′), open); correlation input of order `≥ (log N)^{θ}/log log N` with
non-CRT (true) values (TC^alt_θ, open); **any family of classes that is not a K2 mixture** (decided for ES₅/U/I3 in
§1.3 — this turns out to matter).
### §1.3 Are ES₅ and U subfamilies of the KARY2 mixture? (decided: no as families; set containment undecided)

**Words.** A word of n is (t,u,v) ∈ ℕ³ with `n = tuv − u − v`, equivalently `(tu−1)(tv−1) = tn+1`. It is a
*certificate* if one of t, u, v, tu−1, tv−1 is ≡ 0 (mod 4); ES₅(n) := n has a certificate word (at primes this is
the z48 ES₅, Theorem A). U(n) := n has a word with an endpoint ≡ 0 (4) or ≡ −n (8) and both `tu−1, tv−1 > 1`
(z49 definition). Every U-word is a certificate: if v ≡ −n (8) is odd, then 8 | n+v = u(tv−1), so 4 | u or
4 | tv−1; if v ≡ −n (8) is even then tv−1 is odd and 8 | u (review D3). Endpoint moduli tv−1 = 0 are excluded. Each word lies in three classes, one per **grouping**:

    pair class      P(u,v) = {n ≡ −(u+v) (mod uv)}        (t free),
    endpoint class  E(t,v) = {n ≡ −v (mod tv−1)}          (u free),   and E(t,u) symmetrically (v free).

Every n ≥ 1 in such a class has the word (the free coordinate is automatically a positive integer). The
certificate condition is a condition on the free coordinate mod 4, i.e. it cuts the class into subclasses of
modulus `4·(modulus)`; U adds n mod 8. Call these *word classes*; 𝔘_W is the set of all certificate word
classes, in all three groupings, **including non-reduced pair classes** (e.g. u = 12, v = 3: `n ≡ 21 mod 36`).
Selector classes `0 mod p` are kept separate (they contain squares; review D5). U's inequalities `tu−1, tv−1 > 1`
are not congruence conditions: a U-refined class is a certificate-word class whose finitely many initial members
may fail U; that prefix is paid separately wherever U itself is counted (review D3; e.g. (t,u,v) = (1,2,4)). Endpoint groupings with a *fixed* adjacent factor tv-1 <= 1 are discarded for U: they
never supply U-words (e.g. E(1,2)); this is not a finite-prefix issue (review 2, R2-7).

**The identity behind each certificate** (proved by clearing denominators as in Prop 1.2's proof; exact-arithmetic checks in `scripts/z50_ncrt_identities.py`):

| slot | identity 4/n = … | ET type | class it gives, as a set |
|---|---|---|---|
| 4 \| t, t = 4C | 1/(uvC) + 1/(nvC) + 1/(nuC) | Type II, (a,b,c,d) = (v,u,1,C) | E(t,v): `−v mod 4Cv−1` is the ℛ(4Cv−1)-class `−4D`, D = Cv² \| (Cv)² |
| 4 \| v, v = 4w | 1/(w(tu−1)) + 1/(ntw) + 1/(ntw(tu−1)) | Type II, (1, tu−1, t, w) | E(t,v): `−4w mod 4wt−1` is the ℛ-class with D = w \| (wt)² |
| 4 \| tv−1 = 4m | 1/(mu) + 1/(mu(tu−1)) + 1/(nm(tu−1)) | Type I, (1, tu−1, u, m) | E(t,v) ⊂ Case-A class `−t^{−1} mod 4g(m)` (m' = t, d = m, 4g(m) \| 4m) |
| 4 \| u (in E(t,v)) | 1/(d(tv−1)) + 1/(ntd) + 1/(ntd(tv−1)), u = 4d | Type II, (1, tv−1, t, d) | subclass `−v mod 4(tv−1)` of E(t,v): ET's Type II with **d free** |
| 4 \| tu−1 (in E(t,v)) | 1/(m'v) + 1/(m'v(tv−1)) + 1/(nm'(tv−1)), tu−1 = 4m' | Type I, (1, tv−1, v, m') | subclass of E(t,v) mod 4(tv−1): Type I with **d = m' free** |

**Proposition 1.2 (PROVED).** (a) The rows 4|t, 4|v (each read in the grouping where the slot is fixed) are literally
ℛ(M)-classes; the row 4|tv−1 is a subset of a single Case-A class of modulus dividing the word-class modulus.
(b) The rows 4|u and 4|tu−1 read in E(t,v), and every refinement of a pair class P(u,v) by t mod 4, are classes of
a **parameter-freezing rule** that is not one of the four K2 rules: K2's types are the Type II groupings with the ET parameter
a free (ℛ(M)), (q,δ) = ((a+b)/c, a²d) fixed ((a,D)), and the Type I grouping of Case A; the class `−v mod 4(tv−1)`
is the Type II grouping C_II(1, tv−1, v) = `{n ≡ −e (mod 4ab)}` with (a,b,c) = (1, tv−1, t) fixed and d free.
The displayed witness-to-K2 map sends its members to ℛ- and (a,D)-classes of moduli `4td−1` and `4v·g(d)` that grow
with d. This does **not** exclude coincidences as sets: e.g. `17 mod 20` ((t,v) = (2,3), 4|u) is exactly the Case-A
class (d,m) = (5,7); `7 mod 8` ((t,v) = (3,1), 4|u) is the fixed (a,D) = (1,2) class; the pair certificate class
`13 mod 24` ((u,v) = (2,3), t ≡ 3 (4)) is (a,D) = (3,2) (review D1, checked).
(c) So ES₅ and U certificate families are **not** subfamilies of the K2 mixture *as parametrised families*, and
the "a fortiori" argument of z50 CONTEXT §3 does not apply verbatim; set-level containment is open (below).

*Proof.* (a) is the table (each identity checked by clearing denominators: e.g. row 2 sums to
`(nt + tu − 1 + 1)/(ntw(tu−1)) = t(n+u)/(ntw(tu−1))` and `n+u = 4w(tu−1)`). For row 3, Case A (ET-file §3) is
`n ≡ −m'^{−1} (mod 4g(d))` with `m' | 4d+1`; take m' = t, d = m: `4m+1 = tv` so t | 4d+1, and `tv ≡ 1 (mod 4m)` gives
`−t^{−1} ≡ −v (mod 4m)`, hence mod `4g(m)` since `g(m) | m`. (b) Read off (a,b,c,d) from the identity: row 4 has
b = tv−1, c = t fixed and d = u/4 varying; the ℛ-grouping fixes (b,c,d) and the (a,D)-grouping fixes
(q,δ) = (v, d); both vary along the class. ∎

**But as sets the difference is small (CERTIFIED, `scripts/z50_ncrt_k2contain.py`, `data/z50_ncrt/k2contain_400.txt`).**
For the endpoint subclasses of type 4|u or 4|tu−1 with modulus 4A ≤ 400 and no fixed certificate slot (A ≢ 0 (4),
4 ∤ t, 4 ∤ v): 392 parameter instances, **318 distinct residue classes** (review D2). 299 instances are contained in a
*single* K2 class of modulus dividing 4A (typically Case A; e.g. the U-class `97 mod 104` (t=2, v=7) is the Case-A
class (r,h,m) = (26,1,15), and `5 mod 8` is Case A (2,1,3)). The other 93 have all their members n ≤ 10⁵ covered by
K2 classes of modulus ≤ 400 (largest least modulus 328); this tests coverage of members below 10⁵, not coverage
of the whole progression and not equality. Whether every word class is covered by finitely many K2 classes of
polynomially related modulus is **undecided** (EVIDENCE for yes at small moduli). **For caps it does not matter:**

**The decision that matters (§2, Theorem 2.1).** K2's proof uses only (i) no W-smooth class contains a unit square,
(ii) first moments `𝔐(y) ≪ (log y)^{β}·polylog`, (iii) cofactor second moments `≪ ℓ^{o(1)}`, with W-uniform
constants (K2 §6 item 2; review D4). The word universe satisfies (i) (no certificate word exists at a square:
Type II by K2 Lemma 2.1 / Lean L9903, Type I via Case A and K2 Lemma 2.2) and (iii), and satisfies (ii) with
**β = 2, not 3**: a word has one free divisor, an ℛ-class `D | A²` has two (`τ(A+1)` versus `τ(A²)`). Hence the
caps apply to the word-class architecture for ES₅/U not at 3/4 but at **2/3**.

**Relation to lane E (merged to main during this work; EXSET_I3.md §§3–4, 7, z50 CONTEXT §6).** Lane E proved
independently, for the *native* endpoint-class presentation `n ≡ −u (mod tu−1)` on n ≡ 1 (4), the sharper cap
`λ^{2/3}/(log λ)^{1/3}` (zero base at odd p ≤ W, 2-adic square base), and `E_U(N) ≪ N exp(−c(log N)^{2/3}(log log N)^{−1/3})`
over all n ≡ 1 (4). I do not re-prove that. What §§2–3 add, and why they are not redundant:
* lane E's zero base pins n ≡ 0 mod every odd p ≤ W, so its cap **does not cover** families containing selector
  classes `0 mod p` (the architecture actually used at primes and in the 3/4 note), nor prime-only methods
  (EXSET_I3 §7.2, "Contrast and qualification"), nor the **non-reduced pair presentations** such as
  `n ≡ 21 mod 36` (its open door, §§4.5, 7.2). Corollary 2.5 below uses the unit-square base and covers selector-augmented whole-avoider families (including
  their use for prime bounds) and non-reduced certificate pair classes; genuinely prime-only majorants (P) remain
  outside its proved scope (review 2, R2-1). It does so
  at exponent 2/3 (with a `(log λ)^{2/3}` factor instead of lane E's `(log λ)^{−1/3}`);
* at primes and rough n, Theorem 3.1 attains `N exp(−c(log N)^{2/3})` **without** the log-log loss, which lane E's
  Thm 4.1 shows is intrinsic only for all-integer whole-avoider methods. The two results together locate the
  (log log N)^{1/3}: the native whole-avoider obstruction is witnessed on small-prime-divisible fibres, which the rough-input
  construction excludes (review 2, R2-2). Lane E's intrinsic-loss statement is for the native architecture only.
### §1.4 Open doors (my words) and the two chosen

By the operational definition of §1.2, a door is a true property of [1,N] (or of the primes) that fails for N·π.

* **D1 Archimedean truncation.** On [1,N] a class of modulus > N holds ≤ 1 integer, and a k-fold intersection of lcm > N is empty unless its CRT residue lies in [1,N]. π knows
  none of this. (CONTEXT doors (i), (ii); IF2 hybrids / weak SPW.)
* **D2 True high-order correlations.** Exact k-fold witness counts on [1,N] for k ≥ (log N)^θ/log log N
  (TC^alt_θ). Bounded k is useless whatever its precision (TU Thm 3.1; NC Cor 8.7).
* **D3 Super-polynomial frequency level** against residue-DENSE classes with ≥ 2 primes above exp((log N)^{1/4})
  ((A*), (DCC), (RD′)).
* **D4 Shift-uniform avoider count** (W_𝔊) (per-frequency weights < 1).
* **D5 Primes of the family beyond N^{O(1)}.** Multiplicative (Landau-type) events such as "tn+1 has a prime
  factor q ≡ −1 (mod 4t)" are unions of classes over all primes q ≤ tN+1. For t ≤ N^{O(1)} these primes are still
  polynomial in N, so this is not a super-polynomial-prime family; the door is the *evaluation*: their densities
  come from Selberg–Delange (multiplicative), not from CRT (review D13). (This is lane D's object; I do not work it.)
* **D6 Global multiplicative structure of the exceptional set**: E(ES) is divisor-closed (a fact about integers,
  false for π); semigroup/Rankin; density increment; entropy.
* **D7 Prime-specific bilinear structure** (Vaughan/Heath-Brown, Harman, zero-density): only through (P) so far.
* **D8 (new, from §1.3) Other class families.** A cap is a statement about one class universe. The universe is
  part of the method. Before asking for a non-CRT input one must know the CRT ceiling **of the universe at hand**.

**Chosen.** (A) **Door D8 first**, because §1.3 shows the barrier for ES₅/U was mis-stated: prove the CRT ceiling
of the word universe (2/3, Theorem 2.1, a barrier for a class not covered by (D)17–(D)29) and show it is attained
(Theorem 3.1, a new exceptional-set theorem for U and ES₅ at primes). (B) **Door D1 via divisor switching**
(brief candidate 1): decide what switching to the complementary divisor can and cannot buy (§4). Candidate 2
(transfer range) is lane C's chain-rule object and candidate 3 (primes) is assessed briefly in §4.4.

## §2 The CRT ceiling of a class universe, and the word universe (door D8; a new barrier theorem)

Notation as in K2 §§2–4: W absolute; `Γ(m) = Π_{p|m} γ'(p)` with `γ'(p) = γ(p)` (= 2p/(p−1), γ(2) = 8) for p ≤ W
and `γ'(ℓ) = (1 − ℓ^{−1/2})^{−1}` for ℓ > W; P(G) the largest prime factor; for a class with modulus G = qℓ^v,
P(q) < ℓ, `μ_{ℓ,v}(q)` is the number of classes of the universe with that modulus.

**Theorem 2.1 (supply-exponent cap; PROVED given the K2/EK machinery as reviewed).** Let 𝔘 be a universe of classes
such that
* (i) no class of 𝔘 contains a perfect square `y² ≥ 1` (so no W-smooth class contains a unit square);
* (ii)_β,γ `𝔐_𝔘(y) := Σ_{C∈𝔘, W<P(G_C)≤y} Γ(G_C)/G_C ≤ K(log y)^β(log log y)^γ` for `y ≥ y₀`, with β ≥ 1, γ ≥ 0;
* (iii) for every κ ∈ (0,1], every prime ℓ > W and v ≥ 1:
  `Σ_{P(q)<ℓ} μ_{ℓ,v}(q)² τ(q)Γ(q)/q ≤ C_κ(W)(v+1)^c[(log ℓ)^c + ℓ^{κv}]`, **for every W ≥ W₁, with
  `C_κ(W) ≤ A_κ(log W)^d`** (fixed d; review D4: K2 Lemma 4.3 chooses W large, which needs this uniformity; the
  constants K, y₀ in (ii) may depend on the finally fixed W).

Then there are W, λ₀, C (depending on K, β, γ, c, d, A_κ only) such that for every finite family 𝔊 of classes of
𝔘 and selector classes `0 mod p`, mixed arbitrarily, arbitrary moduli, and every majorant ν of 𝒜(𝔊) of level
λ ≥ λ₀,

    log(1/Eν) ≤ C λ^{β/(β+1)} (log λ)^{γ/(β+1)}.

If every modulus of 𝔊 satisfies `G ≤ P(G)^{1+B}` and (ii) holds with γ = 0 for such classes, the bound is
`C_B λ^{β/(β+1)}`.

*Proof.* K2 Thm 5.1's proof uses exactly the three listed inputs (K2 §6 item 2; checked line by line: the base
Lemma 2.3 uses only (i); the chain-rule density `Q'(n ≡ b (m)) ≤ Γ(m)/m`, EK Thm 4.1/Cor 2.6 and the leak mechanism
are arithmetic-free; first moments enter only through 𝔐; second moments only through Lemma 4.1, whose proof is
family-free, fed by (iii); Lemma 4.3 then gives `E p_ℓ² ≤ C(W)ℓ^{−7/4}(log ℓ)^c` with `C(W) ≤ C(log W)^{d+c}`, so
`leak ≤ Σ_{ℓ>W} ℓ^{1/2}E p_ℓ² ≪ W^{−1/4}(log W)^{C}` and an absolute W gives leak ≤ 1/2). Selector classes are
handled as in K2 (no unit square; first moment O(log log y); cofactor sum 1). The independence of EK/ETw from
the class types and from cubic supply was re-checked by the reviewer (review 1, §2). Only the cost
bookkeeping changes. Take `s₁ = λ^{1/(β+1)}(log λ)^{−γ/(β+1)}`, singletons `W < ℓ ≤ e^{s₁}`, blocks
`V_i = {2^i s₁ < log ℓ ≤ 2^{i+1}s₁}` below `e^{λ/2}`, one linear block, as in K2.
* Singletons cost `≤ (8/3)𝔐(e^{s₁}) ≤ C s₁^β(log λ)^γ = Cλ^{β/(β+1)}(log λ)^{γ/(β+1)}`.
* Block i, `s = 2^i s₁`, `d_i = ⌊λ/s⌋`: `E M_{V_i} ≤ 𝔐(e^{2s}) ≤ K(2s)^β(log λ)^γ`, so
  `(E M_{V_i} + 4d_i)/d_i ≤ 2^{β+1}K s^{β+1}(log λ)^γ/λ + 4 = 2^{β+1}K·2^{i(β+1)} + 4`, and
  `E Φ_i ≤ (λ/(2^i s₁))(c₁ + i(β+1)log 2) + O(log λ)`. Summing, `Cλ/s₁ + O(log²λ)`.
* Linear block `O(e^{−λ/4})`; base `2W + log 2`.

Both main terms are `Cλ^{β/(β+1)}(log λ)^{γ/(β+1)}`. Under bounded B, drop the smoothness: 𝔐 over `G ≤ y^{1+B}` is
`≤ C_B(log y)^β`, and EK Thm 4.5's bookkeeping with `s₁ = λ^{1/(β+1)}` gives `C_Bλ^{β/(β+1)}`. ∎

β = 3, γ = 3 is K2 Thm 5.1; KARY3 removes γ for the K2 types. The exponent of the cap is the supply exponent
alone: `β/(β+1)`. The relevant question for any problem is therefore: **what is β for the class universe the
problem can use?**

**Lemma 2.2 (the word universe satisfies (i); PROVED).** No word class (§1.3: endpoint or pair class, certificate
or U refinement) contains a perfect square `y² ≥ 1`.

*Proof.* Every n ≥ 1 in a word class has the class's certificate word, hence (table of §1.3) a Type II solution
`4abcd = a+b+cn` or a Type I solution lying in a Case-A class (rows 3 and 5: m'' = t, d = (tv−1)/4 resp.
(tu−1)/4, since `t | 4d+1` and `nt + 1 = (tu−1)(tv−1) ≡ 0 (mod 4d)`). A Type II solution puts n in the
ℛ(M)-class `−4D`, `M = 4bcd−1`, `D = b²d | (bcd)²` (mod M, `4bcd ≡ 1` gives `cn ≡ −b` and `−4b²d ≡ −b/c`), so
K2 Lemma 2.1(1) excludes squares; independently, Type II at `n = y²` is excluded by Lean L9903 (`4abcd ≠ a+b+m²c` for all positive integers; re-checked by brute force for m < 60,
a ≤ b < 60, c < 40). A Type I solution puts n in a Case-A class, which contains no square (K2 Lemma 2.2). ∎

**Lemma 2.3 (word first moment, β = 2; PROVED).** `𝔐_W(y) ≤ K(W)(log y)²(log log y)²`, and over moduli
`G ≤ y^{1+B}` the sum is `≤ K_B(log y)²`.

*Proof.* A word class has modulus G with `A | G | 8A` (endpoint class of modulus A = tx−1) or `uv | G | 8uv`
(pair class); each endpoint (pair) class has at most 8 refinements. As `Γ(G)/G ≤ Γ(8)Γ(A)/A` for `A | G | 8A`,

    𝔐_W(y) ≤ C[ Σ_{P(A)≤y} τ(A+1)Γ(A)/A + Σ_{P(m)≤y} τ(m)Γ(m)/m ].

The pair part is `≤ C(log y)²` by K2 Lemma 3.1 (F = τΓ, `F(p) ≤ 2 + 4p^{−1/2}` for p > W, κ = 2). For the endpoint
part, first `Σ_{A≤x} τ(A+1)Γ(A) ≤ C(W)x log x`: write `Γ = 1 ∗ h`, h squarefree-supported, `h(p) = γ'(p) − 1`
(≤ 7 for p ≤ W, ≤ 2p^{−1/2} for p > W). For `s ≤ x^{1/2}`,
`Σ_{A≤x, s|A} τ(A+1) = Σ_{m≤x+1, m≡1 (s)} τ(m) ≤ 2Σ_{d≤√(x+1)}((x+1)/(ds) + 1) ≪ (x/s)log x`; for `s > x^{1/2}`
use `τ ≤ x^{ε}`. So the sum is `≤ x log x Σ_s h(s)/s + x^{1+ε}x^{−1/8}Σ_s h(s)s^{−3/4} ≤ C(W)x log x` (ε = 1/16; review D6) (both Euler
products converge). By partial summation the *body* `A ≤ X := y^{u₀}`, `u₀ = 12 log log y`, contributes
`≤ C(log X)² = C·144(log y)²(log log y)²`. *Tail:* for a block `K < A ≤ 2K`, `K ≥ X/2`, `u = log K/log y`,
Cauchy–Schwarz gives `≤ (Σ_{P(A)≤y, A~K} Γ(A)²/A)^{1/2}(Σ_{A~K} τ(A+1)²/A)^{1/2} ≤ Ce^{−u/2}(log y)^{1/2}·C(u log y)^{3/2}`
(K2 Lemma 3.1 with F = Γ², κ = 1; `Σ_{m≤x}τ(m)² ≪ x log³x`). Summing over blocks (u-spacing log 2/log y) the tail
is `≤ C(log y)^3u₀^{3/2}e^{−u₀/2} ≤ C`. Under bounded B the body with `X = 8y^{1+B}` is the whole sum. ∎

**Lemma 2.4 (word cofactor sums; PROVED).** The word universe satisfies (iii).

*Proof.* Mirror of K2 Lemma 4.2. *Pair part:* `μ(q) ≤ 8Σ_{i≤3}τ(qℓ^v/2^i) ≤ 32(v+1)τ(q)`, so the sum is
`≤ C(v+1)²Σ_{P(q)<ℓ}τ(q)³Γ(q)/q ≤ C(v+1)²(log ℓ)^8` (K2 Lemma 3.1, κ = 8). *Endpoint part:*
`μ(q) ≤ 8Σ_{i≤3}τ(qℓ^v/2^i + 1)` (terms with `2^i ∤ qℓ^v` omitted), so `μ² ≤ 256Σ_iτ(A_i+1)²`, `A_i = qℓ^v/2^i`.
Long blocks `K < q ≤ 2K`, `K ≥ 16ℓ^{v/3}` (review D7: then the m-interval length `Y ≥ Kℓ^v/8 ≥ 2ℓ^{4v/3}` and
`ℓ^v < Y^{3/4}`; q = 1 is a short block): Cauchy–Schwarz gives
`(Σ_{block,P(q)<ℓ}τ(q)²Γ(q)²/q)^{1/2}(Σ_{block}τ(A_i+1)⁴/q)^{1/2}`; the first factor is `≤ Ce^{−u/2}(log ℓ)²`
(κ = 4, u = log K/log ℓ); in the second, `m = A_i + 1 ≡ 1 (mod ℓ^v)` runs over an interval of length `≍ Kℓ^v`
with `ℓ^v < (Kℓ^v)^{3/4}`, so Shiu (F = τ⁴, F(p) = 16) gives `≪ (Kℓ^v/φ(ℓ^v))(log Kℓ^v)^{15}` and the factor is
`≤ C((u+v+1)log ℓ)^{15/2}`. Summing over blocks: `≤ C(v+1)^c(log ℓ)^c`. Short blocks `K < 16ℓ^{v/3}`: `m ≤ ℓ^{2v}`,
so `τ(m)²τ(q)Γ(q) ≤ C_κℓ^{κv/2}` (using `Γ(q) ≤ 8·3^{ω(q)}`, uniform in W) and `Σ_{q≤32ℓ^{v/3}}1/q ≤ C_κℓ^{κv/2}`.
*W-uniformity (review D4):* W enters only through Euler factors at p ≤ W in K2 Lemma 3.1 (each `1 + O(1/p)`, product
`≤ C(log W)^d`) and through the pointwise `Γ ≤ 8·3^ω`; Shiu's constant is W-free. So (iii) holds with
`C_κ(W) ≤ A_κ(log W)^d`. ∎

**Corollary 2.5 (the ES₅/U word-class architecture has ceiling 2/3; PROVED given K2/EK, Lemmas 2.2–2.4).** For every finite
mixture 𝔊 of certificate word classes (any grouping, including non-reduced pair classes; certificate or eventual-U
refinements) and selector classes, every majorant of 𝒜(𝔊) of level λ
has `log(1/Eν) ≤ Cλ^{2/3}(log λ)^{2/3}`, and `≤ C_Bλ^{2/3}` if all moduli satisfy `G ≤ P(G)^{1+B}`. Consequently
(the reductions below use the family cap only as a black box):
* (M1) coefficient-sum methods (`N·Eν + Σ|a_i|`, family primes ≤ N^A) for E_{ES₅}, E_U, at primes or over all n,
  save `≤ C_A(log N)^{2/3}(log log N)^{2/3}` (K2 Cor 6.1's projection + ET-file Lemma 2.9, family-free);
* (M2) any evaluation of a majorant whose classes all have modulus ≤ N/2 is capped at the same order (IF Thm 2.2:
  `Σ_{n≤N}ν ≥ (N−D)Eν`, family-free);
* (L1) every CRT-admissible large sieve with polynomial-period rows (LS1 Thm 2.1 duality to a Selberg-square
  majorant, family-free);
* (C) order-k majorants save `≤ C(k log N)^{2/3}(log(k log N))^{2/3}`.

The prime-law version (P) needs PL's unit-group rerun; I expect it verbatim but have not checked it (Assessment).

**Reading.** For U and ES₅ every CRT method of the word-class architecture (whole-avoider majorants of word-class
families plus selectors, with the transferred evaluations M1, M2, L1, C above) is limited to the **Vaughan exponent
2/3**, not 3/4. The 3/4 note's extra factor comes from `τ₃`-type classes (`D | A²`), which certify ES but not ES₅ or U.
So for U and ES₅, Target 3 ("beat 3/4") is, for these architectures, a target beyond the ceiling at 2/3 already.
**Scope (review D8).** This caps majorants of the whole periodic avoider set of a finite *word-class* family. It
does **not** cap every method for U/ES₅: a method may use any progression separately proved to force the target
(coverings by different words in different residue subcases, non-word classes with a separate forcing argument),
and such a universe needs its own supply estimate. No universe-exhaustion theorem is claimed; whether a larger
U/ES₅-forcing class universe has cubic supply is OPEN. **Mixtures** of K2 types and word classes satisfy (i)–(iii)
with β = 3 (sum of the two universes' moments), so M1 and M2 hold for them at 3/4: a barrier for a class strictly
larger than (D)17–(D)29; the other items of Theorem 1.1 are not claimed for the mixture without their own
transfer (review D9). **Sharpness (review D10):** exponent sharpness for the unrestricted word architecture (a
`(log log N)^{2/3}` gain is not excluded), order sharpness only within bounded-B families.

**Remark 2.6 (I3; original Assessment, now superseded by lane E).** I3 words are words with t,u,v ≥ 3, so their (ii)/(iii) are
those of Lemmas 2.3–2.4 (β = 2). Condition (i) fails: I3 holds at squares. Theorem 2.1's base needs only *some* set
`R ⊆ ℤ/Q₀` avoiding the W-smooth classes with `log(Q₀/|R|) = O_W(1)` uniformly in the 2,3,…,W-exponents of Q₀ (K2
uses unit squares). If such an R exists for I3, the CRT ceiling for I3 is also 2/3, and **"reach 3/4 for I3 by
multiplier atoms" (lane E goal 1) is impossible by CRT majorants**: multipliers do not change β. I had not proved
the I3 base lemma. **Update:** lane E proved it with a zero base (pin n = 0 mod every p up to W) and obtained the
I3 cap `C lambda^{2/3}/(log lambda)^{1/3}`, matching the known I3 upper bound (EXSET_I3 Thms 3.1, 4.1). So the
prediction above is now a theorem of lane E, not of this document.

## §3 The ceiling is attained: a Vaughan-exponent theorem for U and ES₅

**Theorem 3.1 (PROVED, relative to Bombieri–Vinogradov, Brun–Titchmarsh (Montgomery–Vaughan form) and the
elementary lemmas below; ineffective constants).** There are absolute constants c, C > 0 such that for N ≥ 3

    #{p ≤ N prime, p ≡ 1 (mod 4) : U(p) fails} ≤ C N exp(−c(log N)^{2/3}),

and hence the same bound holds for #{p ≤ N : ES₅(p) fails} (U(p) ⟹ ES₅(p), §1.3). More generally, with
`y = Bt²` as in Lemma 3.6 (so `y ≍ (log N)^{2/3}`), the bound holds for #{n ≤ N : n ≡ 1 (4), (n, P_y) = 1, U(n) fails}, and in every interval
(x, x+H] with H ≥ 2 in place of [1,N] with N replaced by H (shift-uniformity, as in EXCEPTIONAL_SHORT Thm 1), for intervals in the positive integers, after adding the
prefix terms O(y + KX) (review D11). For ES5 at *all* primes: p = 3 (mod 4) always has the certificate
(t,u,v) = (p+2, 1, 1) (tu-1 = tv-1 = p+1 = 0 mod 4), and p = 2 is trivial, so only p = 1 (mod 4) counts.

By Corollary 2.5 (bounded-B case: the atoms below have modulus kℓ ≤ ℓ^{1+2κ}) no CRT method over word classes
can improve the exponent 2/3; within fixed bounded-B word families (which contain Theorem 3.1's atoms) it is sharp
up to the constant c; for unrestricted word families a (log log N)^{2/3} gain is not excluded (review D10).

**Prior work (corrected after review D12 and lane E).** I3_DEEP_ASTRA (line 146) already proves an
`N exp(-c sqrt(log N))` bound for the 4|t interior-star subfamily, hence a quantitative ES5 bound; and I3_DEEP_ASTRA
Lemma 8.7 / Thm 8.8 contain the one-divisor multiplier atoms, same-prime distinctness, fibre supply t*Sum 1/k,
mean-square incidence, exponential Z-moment and t^3 ledger used below. Lane E (EXSET_I3 §7.3) transferred that
construction with 4|u to `E_U(N) << N exp(-c(log N)^{2/3}(log log N)^{-1/3})` over all n = 1 (mod 4). Theorem 3.1 is
therefore the certificate/U-restricted adaptation of that construction (with the 3/4 note's selector); its only new
content is the **removal of the (log log N)^{1/3} at primes and rough n**. No external priority claim; equivalent
arithmetic formulations have not been literature-audited. [Superseded original text, kept for the record: "Within
the campaign, the strongest previous statement for U or ES₅ at primes was qualitative:
`H₄ ≤ h(p)` for almost all p (FOREST_H4 Thm 3.5, rate ≍ (log Y)^{−1/2} at fixed Y), and, for each fixed H, density
≤ exp(−c log²H) (CONJECTURE_S_MODEL). Neither has N-dependence beyond what PNT in fixed APs gives. (git grep; U and
ES₅ are campaign-internal notions, so no literature comparison applies.)" 
That claim was false.]

### §3.1 Atoms (the only new design choice)
Keep the note's parameters: κ = 1/480, t = log X, K = ⌊X^κ⌋, H = K¹⁰, K(K) = {k ≤ K : k ≡ 1 (4)},
L_K = lcm K(K), blocks I_j = (x_j, min(2x_j, X)], x_j = 2^j X^{1/2}, z_j = x_j^{1/6}. A **U-atom** is a triple

    A = (k, ℓ, w):  k ∈ K(K),  ℓ ∈ I_j prime,  H < w ≤ z_j,  4w | kℓ + 1;   class  E_A = {n ≡ −4w (mod kℓ)}.

(Then gcd(w,k) = 1 and ℓ ≡ 3 (4).) *U-certificate:* if n ∈ E_A and n > kℓ − 4w, then (t, u, v) = ((kℓ+1)/(4w),
(n+4w)/(kℓ), 4w) is a word of n with endpoint v ≡ 0 (4), u ≥ 2, `tv − 1 = kℓ > 1`, `tu − 1 ≥ 2t − 1 > 1`; so
U(n) holds, with the identity 4/n = 1/(w(tu−1)) + 1/(ntw) + 1/(ntw(tu−1)) (row 2 of §1.3; checked in
`scripts/z50_ncrt_identities.py`, 25 230 atom words, 0 failures; these are algebraic checks of the word equation and the identity, not of the full U
predicate, review D14). Compared with the note: the note's two free
divisors u, v of (kℓ+1)/4 become one free divisor w. That single change is β = 3 → β = 2.

### §3.2 The note's lemmas, changed where needed

**Lemma 3.2 (distinctness, conditional independence; PROVED).** For X large: (1) distinct atoms with the same ℓ
have distinct classes mod ℓ; (2) given c = n mod L_K and any event determined by n mod P_y, the residues n mod ℓ
(ℓ ∈ (X^{1/2}, X]) are independent and uniform; (3) A meets the fibre of c iff k | c + 4w, and then
E_A ∩ fibre = {n ≡ c (L_K), n ≡ −4w (ℓ)}.
*Proof.* (1) −4w ≡ −4w' (mod ℓ) with 4w, 4w' ≤ 4z_j < ℓ gives w = w'; then kℓ ≡ k'ℓ ≡ −1 (mod 4w) and
gcd(ℓ, 4w) = 1 give k ≡ k' (mod 4w), and 4w > 4H > K forces k = k'. (2) CRT (ℓ > K > y). (3) k | L_K. ∎

So in each fibre `H_X = Σ_ℓ I_ℓ` with independent Bernoulli `I_ℓ`, `P(I_ℓ = 1 | c) = f_c(ℓ)/ℓ`,
`f_c(ℓ) = #{active atoms at ℓ}`, exactly as in the note.

**Lemma 3.3 (one-variable lattice sums; PROVED).** For k ≤ K with (a,k) = 1, and every d ≤ K² with (a,d) = 1,
Λ = log(z/H), z ≥ H²:
(a) `Σ_{H<w≤z, w≡a (k)} 1/w = Λ/k + O(1/H)`;
(b) `Σ_{H<w≤z, w≡a (d)} 1/φ(4w) ≤ C Λ/d` for every d ≤ K².
*Proof.* (a) comparison with an integral. (b) `φ(4w) ≥ 2φ(w)` and `1/φ(w) = w^{−1}Σ_{e|w}μ²(e)/φ(e)`; a divisor e
with (e,d) > 1 contributes nothing (w ≡ a, (a,d) = 1); for e ≤ H use (a) on (H/e, z/e] (length ratio Λ), for e > H
the bound 1 + log z; so the sum is `≤ (Λ/d)Σ_e μ²(e)/(eφ(e)) + O(log H/H + (log z)H^{−1/2})`, and the error is
`≪ Λ/K² ≤ Λ/d` because H = K¹⁰ and Λ ≥ ½ log z ≥ 5 log K. ∎

**Theorem 3.4 (quadratic supply in every fibre; PROVED given BV, BT).** For 1 ∈ J ⊆ K(K), (c, L_J) = 1, put
`g(J) = Σ_{k∈J} 1/k` and `f_{c;J}(ℓ) = #{(k,w) : k ∈ J, H < w ≤ z_j, w ≡ −c·4^{−1} (mod k), 4w | kℓ+1}`. Then

    a t g(J) ≤ Σ_{X^{1/2}<ℓ≤X} f_{c;J}(ℓ)/ℓ ≤ A t g(J)

with absolute a, A > 0, for X ≥ X₀, uniformly in c and J.
*Proof.* Fix a block (x, 2x], z = x^{1/6}, so 4w ≤ 4x^{1/6}. For k ∈ J and w ≡ −c/4 (mod k), (k, 4w) = 1 and
4w | kℓ+1 is ℓ ≡ −k^{−1} (mod 4w), a reduced class. So
`Σ_{x<ℓ≤2x} f_{c;J}(ℓ) = Σ_{k∈J}Σ_{w} [π(2x;4w,−k^{−1}) − π(x;4w,−k^{−1})]`.
*Upper.* BT (q = 4w ≤ 4x^{1/3}) gives ≤ (4x/log x)Σ_kΣ_w 1/φ(4w) ≤ (4x/log x)·CΛ g(J) ≤ C'x g(J) by Lemma 3.3(b) with
d = k. Divide by x; sum over O(t) blocks.
*Lower* (full blocks). Main terms: `(li 2x − li x)/φ(4w) ≥ x/(2w log 2x)` (φ(4w) ≤ 2w), and Lemma 3.3(a) gives
`≥ (x/(2 log 2x))Σ_k(Λ/k − O(1/H)) ≥ xΛg(J)/(4 log 2x) ≥ c₀ x g(J)` (Λ ≥ log x/12; K/H negligible).
Errors: group by q = 4w with multiplicity `W(q) = r(w) = #{k ∈ J : k | c + 4w}`. By BT, `E*_x(q) ≤ 4x/(φ(q) log x)`,
and `Σ_w r(w)²/φ(4w) = Σ_{k,k'∈J}Σ_{w≡−c/4 ([k,k'])} 1/φ(4w) ≤ CΛΣ_{k,k'≤K}1/[k,k'] ≤ CΛ(1+log K)³` (Lemma 3.3(b),
d = [k,k'] ≤ K²; the same sum appears in the note's Lemma 4.1). So `Σ_q W(q)²E*(q) ≪ x t³`. Cauchy–Schwarz with BV
(R = 10) gives `|Σ E| ≤ (x t³)^{1/2}(x t^{−10})^{1/2} = x t^{−7/2} = o(x g(J))` since g(J) ≥ 1. Divide by 2x and sum
over ≍ t full blocks. No constant depends on c, J or x. ∎

The BV input is used through E*(q) = max over reduced classes, so the supply holds for every c and J, including
data-dependent ones, with no averaging over c (as in the note). The multiplicity r(w) is paid in mean square; no
Shiu input is needed here, because a single divisor w carries no τ-weight.

**Corollary 3.5 (fibre masses).** With `J_c = {k ∈ K(K) : (k,c) = 1}` and `μ_c = Σ_ℓ f_c(ℓ)/ℓ`:
`f_c = f_{c;J_c}`, and `a t g(J_c) ≤ μ_c ≤ A t g(J_c) ≤ C_u t²` (as `g(K(K)) = ¼log K + O(1) ≤ κt`). *Proof.* As the
note's Cor 4.3: an active atom has k | c + 4w with (w,k) = 1, so (c,k) = 1. (Throughout, a0 := 1/8; then
g(K(K)) >= a0 log K for large K, since g(K(K)) = (1/4)log K + O(1).) ∎

**Lemma 3.6 (moments, void; PROVED).** (a) For every m ≥ 1, `E((H_X)_m | S_y = 1) ≤ (C_u t²)^m`. (b) With
`y = Bt²`, B ≥ B₀: `P(H_X = 0 | S_y = 1) ≤ e^{−c_v t²}`.
*Proof.* (a) verbatim note Thm 5.1. (b) Note Lemma 6.1 with h replaced by g and `t³` by `t²`: `Σ_{k≤K, p|k}1/k ≤
(1+log K)/p` gives `g(J_c) ≥ (a₀ − 2Z(c))log K`, `Z(c) = Σ_{y<p≤K, p|L_K, p|c}1/p`; `E(e^{yZ} | S_y = 1) ≤ e⁴`, so
`P(Z > a₀/4 | S_y=1) ≤ e^{4 − a₀Bt²/4}`; on `Z ≤ a₀/4` (no prime ≤ y divides c on S_y = 1), `g(J_c) ≥ (a₀/2)log K`, so
`μ_c ≥ a_v t²` with `a_v = a a₀ κ/3` for large X. Take `B₀ = 8a_v/a₀ + 1`: then `P(Z > a₀/4 | S_y = 1) ≤ e^{4−2a_v t²}`
and `P(H_X = 0 | S_y = 1) ≤ e^{−a_v t²} + e^{4−2a_v t²} ≤ e^{−a_v t²/2}`; `c_v = a_v/2`. ∎

**Theorem 3.7 (assembly; PROVED).** `ν = S_y·Q_r(H_X)`, r the least even integer ≥ D_B t², satisfies ν ≥ 0,
ν ≥ 1 on every n coprime to P_y in no atom class, `Eν ≤ e^{−c_a t²}`, and
`Σ_{n≤N}ν(n) ≤ N e^{−c_a t²} + e^{C_L t³}` for every N.
*Proof.* Note Thm 7.2 verbatim with t³ → t² in the mean, and `|A_X| ≤ K·X·X^{1/6}`, so
`log T_abs ≤ Bt² log 2 + log(r+1) + r(7/6 + κ)t ≤ C_L t³`. ∎

*Proof of Theorem 3.1.* Take t = α(log N)^{1/3} with C_Lα³ ≤ 1/2. A prime p ≡ 1 (4), p > max(y, KX), with U(p)
failing lies in no atom class (U-certificate of §3.1), so ν(p) ≥ 1. Hence the count is
`≤ y + KX + N e^{−c_aα²(log N)^{2/3}} + N^{1/2} ≪ N exp(−c(log N)^{2/3})` (KX = e^{(1+κ)t} = N^{o(1)}). The rough-n
statement is the same computation. For an interval (x, x+H], ν is a combination of classes counted class by class
(each with error ≤ 1), so `Σ_{x<n≤x+H}ν ≤ H e^{−c_a t²} + e^{C_L t³}`; take t = α(log H)^{1/3}. ∎

**Remark 3.8 (all n ≡ 1 (4); Assessment, not claimed).** U is not divisor-closed, so the note's semigroup/Rankin
step is unavailable. A local decomposition n = d·m (d the y-smooth part) should give
`E_U(N) ≪ N exp(−c(log N)^{2/3}/log log N)` (fibres with many small primes dividing c lose a factor `φ(d)/d` in
g(J_c), and `#{d : φ(d)/d < δ}` decays doubly exponentially in 1/δ). I have not written this out. **Superseded:** lane E (EXSET_I3 Section 7.3) proves the all-n bound with
`(log log N)^{-1/3}`. The square floor
(E_U(N) ≥ √N/2) is far below either bound.

**Remark 3.9 (controls).** Odd squares lie in no atom class (Lemma 2.2; CERTIFIED for the toy family below, 0 of
≈2 100 squares hit). The hard primes 193, 2521, 3361, 9601, 66529 are hit by no toy atom (X ≤ 3000, K = 21), while
409, 577, 5569, 8813281 are; this is consistent with a density statement and says nothing pointwise. Numerator 8:
the atom identity is specific to 4 (it needs 4w | kℓ+1); the m/n analogue (mw | kℓ+1) would give a density
statement for m/n, which is consistent with the finitely many 8/n exceptions (11, 17, 131, 241). Linnik: the theorem
is one-sided (an upper bound for a lower-tail event); no two-sided asymptotic is asserted.

## §4 Round 3: divisor switching (door D1, brief candidate 1) and primes (door D7)

### 4.1 Switching is regrouping, and every word has a cheap grouping

**Proposition 4.1 (PROVED).** Every word (t,u,v) of n lies in its three classes P(u,v), E(t,v), E(t,u), of moduli
uv, tv-1, tu-1, and

    min(uv, tv-1, tu-1) <= (n+u+v)^{2/3} <= (2n+4)^{2/3}.

*Proof.* (uv)(tv)(tu) = (tuv)^2 = (n+u+v)^2 and tv-1 < tv. For the second inequality: if u = 1 then t >= 2 and
v = (n+1)/(t-1) <= n+1; if u, v >= 2 then (u-1)(v-1) <= n+1 gives u+v <= n+4. (Modulus 1 occurs only for tu-1 = 1, i.e.
(t,u) = (1,2), (2,1); these lie in the level-1/2 free word families counted by tau(n+1), tau(2n+1),
LOWERTAIL_DEEP_FABLE Thm 4.1.) QED

CERTIFIED for all words of all n in [20000, 21000): max of min-modulus/(2n+4)^{2/3} is 0.616
(`scripts/z50_ncrt_switch.py`, `data/z50_ncrt/switch.txt`).

So *divisor switching* (replacing the class mod A = tv-1 by the class of the complementary divisor) is the passage
between the groupings of one word. In particular: (a) for n <= N every certificate word is visible in a certificate class (refined by the free coordinate mod 4,
or mod 8 for U) of modulus <= 8(2N+4)^{2/3} < N/2 for large N (review 2, R2-3: the raw cheapest class need not be a
certificate class, e.g. n = 5, word (1,3,4), raw class 1 mod 2 vs certificate class 5 mod 8), so single classes of
modulus > N are never needed; IF Thm 2.2 then applies to a majorant **whose own expansion** has all denominators
<= N/2 (products of such classes may still have lcm > N, see 4.2); (b) for the Type II R(M)-classes, switching M to the
cofactor j = (n+4D)/M is exactly K2's (a,D) grouping (ET-file Lemma 3.2), already in the K2 universe.

**Proposition 4.2 (switching buys a bounded factor of mass; PROVED).** Let w_g(T) = lim_N N^{-1} sum_{n<=N} of the
number of unordered, unrestricted (not certificate-restricted) words of n whose grouping-g modulus is <= T, and w_min(T) the same for the cheapest grouping. Then
w_g(T) = (1/2 + o(1))(log T)^2 for g = pair (sum over uv <= T of 1/uv) and for the endpoint groupings (sum over
A <= T of tau(A+1)/A, each endpoint), and w_max(T) <= w_min(T) <= w_pair(T) + 2 w_end(T) = O((log T)^2).
*Proof.* A word whose cheapest modulus is <= T is counted in at least one grouping; densities are 1/modulus. QED
(Numerically the ratio cheapest/either-endpoint is 1.25-1.51 for T in [10, 1000], unordered words, n in
[20000, 21000): EVIDENCE, same data file. For certificate-restricted counts only the inherited upper bound is
asserted.)

**Theorem 4.3 (divisor-switching detectors are capped; PROVED given Cor 2.5 and K2).** Let a detector choose, for
each word, any one of its three groupings (switching freely, word by word, even depending on sizes) **together with
the certificate-preserving refinement** of that grouping by the free coordinate mod 4 (mod 8 for U; structurally
degenerate U groupings discarded), and let nu be a globally nonnegative majorant of the **whole** avoider set of the
resulting finite family, possibly with selectors. Then Corollary 2.5 applies (2/3, evaluations M1, M2, L1, C). If
K2 classes are mixed in, M1 and M2 hold at 3/4 (Section 2, Scope); L1 and C for the mixture are not claimed.
*Proof.* Each chosen class is a certificate word class (all three groupings are in the universe, including
non-reduced pair classes). QED Without the refinement the statement is false: the raw class P(1,1) = Z covers
every integer (review 2, R2-5).

This answers the brief's question "do the moduli products above N become countable, and what depth does that
buy": switching lowers each single modulus to <= N^{2/3+o(1)} and changes the mass profile by a factor <= 3; the
CRT ledger (depth ~ mass, cost ~ log modulus per event) changes by a constant. **Depth bought: O(1) factor; exponent
unchanged.**

### 4.2 What is left of door D1: exact counts of products above N

A Bonferroni/hit-pattern majorant still contains r-fold products of (switched) classes with lcm L > N. On [1,N] such
a product holds floor(N/L) or ceil(N/L), i.e. 0 or 1, integers: one bit, the position of its CRT residue.
Summing those bits over all r-tuples of a family is exactly the r-th factorial moment
S_r(N) = sum over n <= N of binom(H(n), r), i.e. a count of lattice points on the variety
{u_j A_j = n + v_j, j <= r, n <= N}: an r-point correlation of restricted divisor functions along the shifts v_j.

**Blocking step (Assessment, with the proved parts cited).** (1) r = 1 is the Dirichlet hyperbola: exact, with
power-saving error, and already equal to the CRT mean (IF Thm 2.2). (2) r = 2 is a shifted-convolution problem with
power-saving asymptotics (Kloosterman/spectral; DI-type), for each fixed pair of shifts. (3) r = 3: no individual
asymptotic is known (z50 CONTEXT note (d)); only shift-averaged forms. (4) The existing caps on
bounded-order moment data concern CRT-evaluated moments (NC Props 4.1-4.2, TU Thm 3.1); for exact interval
moments NC Cor 8.7 is CONDITIONAL on its unproved node hypothesis H_node, and favourable exact-interval deviations
from CRT are not excluded (review 2, R2-6). So: for Bonferroni/hit-pattern implementations, counting the
high-lcm terms is a correlation problem of the D2 type, and divisor switching does not simplify it; **no
unconditional depth threshold is proved here**, and interval-only or position-sensitive certificates are not
reduced to D2.

### 4.3 Door D7 (primes): Assessment

* Prime structure enters a counting argument as sum over p <= N of nu(p). Vaughan/Heath-Brown split Lambda into
  Type I sums (nu on progressions dZ: CRT evaluations; PL caps these for K2 families, for word families this is unchecked) and Type II
  sums sum a_m b_k nu(mk). For nu periodic of period Q >> N, a Type II bound for nu is a large-sieve/character-sum
  statement at level Q (heuristically the LS1/LS2 regime) unless nu has extra multiplicative structure; word-class majorants have none
  (nu(mk) is not a function of nu(m), nu(k)).
* Harman's sieve turns Type I/II information about a set S into LOWER bounds for primes in S; an UPPER bound for
  exceptional primes gains nothing over #(S cap [1,N]) without information about S itself.
* Montgomery-Vaughan's power-saving Goldbach exceptional set uses a main term with singular series bounded below and
  an L^2 minor-arc bound. The ES/U representation count f(n) is a sum of shifted restricted divisor functions; its
  normalised variance is not o(1/polylog) (Linnik-type fluctuation; NC Props 4.1-4.2: degree-k moment methods save
  O(k log log N)). No reformulation with an L^2-small error term was found.

Outcome for D7: **no applicable prime-specific estimate or L^2-small reformulation was found.** The bullets are
heuristic reasons, not reductions (review 2, R2-6/R2-8); no barrier theorem for prime-specific methods is claimed.

### 4.4 Sanity checks

* **Square floor.** Corollary 2.5 and Theorem 3.1 are consistent with E_U(N) >= sqrt(N)/2: the cap is a lower bound
  for the *method's* bound, sqrt(N) is far below N exp(-c(log N)^{2/3}), and odd squares are in no word class
  (Lemma 2.2). Any argument beating 2/3 for U over all n must still stop at sqrt(N).
* **Linnik.** All statements are one-sided; no two-sided asymptotic for f(n) is used or claimed.
* **Numerator 8.** The word identities need 4 | slot; the m/n analogue changes the slot condition, and finitely many
  8/n exceptions (11, 17, 131, 241) are consistent with any density statement.

## §5 Numerics and controls (all EVIDENCE/CERTIFIED, finite scope)

| script | what | result |
|---|---|---|
| `z50_ncrt_identities.py` | five certificate identities + ET parameters on 200 000 random words; R-class and Case-A memberships; U-atom word identity | 0 failures (algebraic checks; the U predicate itself is not checked there) |
| `z50_ncrt_k2contain.py 400 400 100000` | endpoint 4\|u, 4\|tu-1 subclasses vs K2 classes | 392 instances / 318 classes; 299 inside one K2 class; rest covered below 10^5 |
| `z50_ncrt_uatoms.py 2e7 X 21 1e6`, X = 300, 1000, 3000 | toy U-atoms: actual avoid fraction of primes p = 1 (4) vs prime-Haar CRT prediction | 0.0952/0.0958, 0.0738/0.0726, 0.0397/0.0382; 0 odd squares hit |
| `z50_ncrt_switch.py 20000 21000` | Prop 4.1, 4.2 | max ratio 0.616; switching ratio 1.25-1.51 |
| reviewer's independent script | identities for all t,u,v <= 24, K2 coincidences, exact toy CRT void 765/1463 | agrees |

The toy comparison is a check that the CRT computation in Theorem 3.1's proof models actual primes at small depth; it
does not test the asymptotic supply theorem (relaxed toy parameters: w >= 1, K = 21). An earlier version of the toy
model counted atoms instead of distinct classes mod l and was off by a factor 2; fixed before any claim was made.

## §6 Hostile reviews (verdicts)

* **Review 1** (Astra, `openai-codex/gpt-6-astra`, deep; the `:high` suffix was not resolvable, same model without
  suffix used; `reviews/z50-ncrt-review-1.md`). Overall MAJOR revision, *not* rejection: the quadratic-supply
  construction and the prime U/ES5 bound survive; the problem-wide reading of the cap and the W-uniformity
  interface did not. Defects D1-D14 and their repairs: D1 exclusivity wording (fixed, coincidences listed); D2
  census counting (fixed); D3 U definitions, even endpoint branch, finite prefix (fixed); D4 W-uniformity of (iii)
  (hypothesis added to Thm 2.1 and verified for words in Lemma 2.4); D5 selectors vs (i) (separated); D6, D7
  elementary slips in Lemmas 2.3, 2.4 (fixed); D8 cap for one universe promoted to a problem (re-scoped: word-class
  architecture only, universe exhaustion OPEN); D9 transfers (only M1, M2, L1, C claimed); D10 sharpness (qualified);
  D11 prefix terms, ES5 at p = 3 (4) (added); D12 prior work (I3_DEEP_ASTRA 8.7-8.8, line 146; lane E 7.3 cited;
  novelty reduced to the removal of the log log loss at primes); D13 door examples (fixed); D14 labels, script
  description, title (fixed).
* **Review 2** (same model, deep; `reviews/z50-ncrt-review-2.md`). Overall MAJOR, confined to the new scope and
  door-closing claims; **no fatal flaw in Sections 2-3**; D4 repair, selector-augmented cap, non-reduced pair
  classes, Theorem 3.1 and Prop 4.1 SOUND. Repairs applied: R2-1 ("covers all three" narrowed: prime-only methods
  stay outside), R2-2 (log-log attribution made architectural), R2-3 (certificate modulus <= 8(2N+4)^{2/3}; IF Thm
  2.2 needs the expansion's denominators), R2-4 (averaging convention, numerics labelled), R2-5 (Thm 4.3 needs
  certificate-preserving refinements; raw P(1,1) = Z would falsify it), R2-6 (D1 = D2 and the depth threshold
  retracted; NC Cor 8.7 is conditional on H_node), R2-7 (fixed degenerate U groupings discarded), R2-8 (D7
  reductions downgraded to heuristics), plus a0 defined, heading and script description fixed, Remark 3.8 marked
  superseded. Notation: C_II(a,b,e) means `n = -e (mod 4ab)` with e = (a+b)/c, so C_II(1, tv-1, v) has c = t.

## §7 Remaining gap (exact)

1. **No CRT barrier was broken.** Targets 1-3 are not reached for ES, ES5 or U. What is new: a supply-exponent
   cap (Thm 2.1) whose application to the full word universe (all groupings, non-reduced pair classes, with
   selectors) gives the 2/3 ceiling of the word-class architecture (Cor 2.5), complementing lane E's zero-base cap;
   and its attainment at primes without the log log loss (Thm 3.1).
2. **Universe exhaustion (open).** Is there a U- or ES5-forcing class universe (coverings, alternative identities)
   with cubic supply? If yes, CRT methods could reach 3/4 for U/ES5; if every U/ES5-forcing progression is covered
   by finitely many word classes of polynomially related modulus, the 2/3 ceiling is the ceiling for all CRT
   methods for U/ES5. The K2-containment census (Section 1.3) is the kind of computation that would test this.
3. **Door D1.** Regrouping (divisor switching) is capped (Thm 4.3). For Bonferroni-type implementations the
   high-lcm terms are exact r-point correlations of restricted divisor functions along shifts; hyperbola / Type
   I-II technology gives r = 1, 2 (r = 3 on average). Whether favourable exact-interval deviations at bounded order
   could help is not excluded unconditionally (NC Cor 8.7 needs H_node); interval-only certificates remain open.
4. **Door D7** (primes): no prime-specific input found that is not already inside (P), (L) or the moment caps.
5. **For lane-level bookkeeping:** for U and ES5 the honest Target 3 is "beat 2/3", which needs a non-CRT input of
   one of the open types D1-D7 (including interval-only and prime-only architectures, which are not capped here), or a
   cubic-supply forcing universe (item 2). This list is not claimed to be exhaustive.
