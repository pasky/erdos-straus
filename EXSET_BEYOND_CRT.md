# EXSET_BEYOND_CRT — breaking the CRT-architecture barrier for the ES / ES₅ exceptional set

Wave z50, lane (A), slug `ncrt`. ES is OPEN; nothing here claims otherwise.
Scripts: `scripts/z50_ncrt_*`; data: `data/z50_ncrt/`.

## §0 Summary table (filled in as sections land)

| # | Claim | Label | Section | Hostile review |
|---|-------|-------|---------|----------------|
| 0.1 | Round-1 audit: union of barred method classes | (pending) | §1 | (pending) |
| 0.2 | ES₅ / U certificate classes ⊂ KARY2 mixture? | (pending) | §1.3 | (pending) |
| 0.3 | Open doors, two chosen | (pending) | §1.4 | — |
| 0.4 | Round-2 attack | (pending) | §2 | (pending) |
| 0.5 | Round-3 attack / barrier theorem | (pending) | §3 | (pending) |

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
### §1.3 Are ES₅ and U subfamilies of the KARY2 mixture? (decided: no as families; yes-but-irrelevant as sets)

**Words.** A word of n is (t,u,v) ∈ ℕ³ with `n = tuv − u − v`, equivalently `(tu−1)(tv−1) = tn+1`. It is a
*certificate* if one of t, u, v, tu−1, tv−1 is ≡ 0 (mod 4); ES₅(n) := n has a certificate word (at primes this is
the z48 ES₅, Theorem A). U(n) := n has a word with an endpoint ≡ 0 (4) or ≡ −n (8) and both `tu−1, tv−1 > 1`
(z49 definition). Every U-word is a certificate: if v ≡ −n (8) is odd, then 8 | n+v = u(tv−1), so 4 | u or
4 | tv−1. Each word lies in three classes, one per **grouping**:

    pair class      P(u,v) = {n ≡ −(u+v) (mod uv)}        (t free),
    endpoint class  E(t,v) = {n ≡ −v (mod tv−1)}          (u free),   and E(t,u) symmetrically (v free).

Every n ≥ 1 in such a class has the word (the free coordinate is automatically a positive integer). The
certificate condition is a condition on the free coordinate mod 4, i.e. it cuts the class into subclasses of
modulus `4·(modulus)`; U adds n mod 8. Call these *word classes*; 𝔘_W is the set of all word classes
(certificate or U-refined) together with the selector classes `0 mod p`.

**The identity behind each certificate** (verified symbolically and numerically, `scripts/z50_ncrt_identities.py`):

| slot | identity 4/n = … | ET type | class it gives, as a set |
|---|---|---|---|
| 4 \| t, t = 4C | 1/(uvC) + 1/(nvC) + 1/(nuC) | Type II, (a,b,c,d) = (v,u,1,C) | E(t,v): `−v mod 4Cv−1` is the ℛ(4Cv−1)-class `−4D`, D = Cv² \| (Cv)² |
| 4 \| v, v = 4w | 1/(w(tu−1)) + 1/(ntw) + 1/(ntw(tu−1)) | Type II, (1, tu−1, t, w) | E(t,v): `−4w mod 4wt−1` is the ℛ-class with D = w \| (wt)² |
| 4 \| tv−1 = 4m | 1/(mu) + 1/(mu(tu−1)) + 1/(nm(tu−1)) | Type I, (1, tu−1, u, m) | E(t,v) ⊂ Case-A class `−t^{−1} mod 4g(m)` (m' = t, d = m, 4g(m) \| 4m) |
| 4 \| u (in E(t,v)) | 1/(d(tv−1)) + 1/(ntd) + 1/(ntd(tv−1)), u = 4d | Type II, (1, tv−1, t, d) | subclass `−v mod 4(tv−1)` of E(t,v): ET's Type II with **d free** |
| 4 \| tu−1 (in E(t,v)) | as row 3 with u ↔ v | Type I, c = u... free | subclass of E(t,v) mod 4(tv−1): Type I with a free coordinate |

**Proposition 1.2 (PROVED).** (a) The rows 4|t, 4|v (each read in the grouping where the slot is fixed) are literally
ℛ(M)-classes; the row 4|tv−1 is a subset of a single Case-A class of modulus dividing the word-class modulus.
(b) The rows 4|u and 4|tu−1 read in E(t,v), and every refinement of a pair class P(u,v) by t mod 4, are classes of
a grouping that is **not** one of the four K2 types: K2's types are the Type II groupings with the ET parameter
a free (ℛ(M)), (q,δ) = ((a+b)/c, a²d) fixed ((a,D)), and the Type I grouping of Case A; the class `−v mod 4(tv−1)`
is the Type II grouping C_II(1, tv−1, v) = `{n ≡ −e (mod 4ab)}` with (a,b,c) = (1, tv−1, t) fixed and d free.
Its members lie in ℛ- and (a,D)-classes only through moduli `4td−1` and `4v·g(d)` that grow with d.
(c) So ES₅ and U certificate families are **not** subfamilies of the K2 mixture *as parametrised families*, and
the "a fortiori" argument of z50 CONTEXT §3 does not apply verbatim.

*Proof.* (a) is the table (each identity checked by clearing denominators: e.g. row 2 sums to
`(nt + tu − 1 + 1)/(ntw(tu−1)) = t(n+u)/(ntw(tu−1))` and `n+u = 4w(tu−1)`). For row 3, Case A (ET-file §3) is
`n ≡ −m'^{−1} (mod 4g(d))` with `m' | 4d+1`; take m' = t, d = m: `4m+1 = tv` so t | 4d+1, and `tv ≡ 1 (mod 4m)` gives
`−t^{−1} ≡ −v (mod 4m)`, hence mod `4g(m)` since `g(m) | m`. (b) Read off (a,b,c,d) from the identity: row 4 has
b = tv−1, c = t fixed and d = u/4 varying; the ℛ-grouping fixes (b,c,d) and the (a,D)-grouping fixes
(q,δ) = (v, d); both vary along the class. ∎

**But as sets the difference is small (CERTIFIED, `scripts/z50_ncrt_k2contain.py`, `data/z50_ncrt/k2contain_400.txt`).**
For every endpoint subclass of type 4|u or 4|tu−1 with modulus 4A ≤ 400 (392 classes), 299 are contained in a
*single* K2 class of modulus dividing 4A (typically Case A; e.g. the U-class `97 mod 104` (t=2, v=7) is the Case-A
class (r,h,m) = (26,1,15), and `5 mod 8` is Case A (2,1,3)). The other 93 have all their members n ≤ 10⁵ covered by
K2 classes of modulus ≤ 400 (largest least modulus 328). Whether every word class is a finite union of K2 classes
of polynomially related modulus is **undecided** (EVIDENCE for yes at small moduli). **It does not matter:**

**The decision that matters (§2, Theorem 2.1).** K2's proof uses only (i) no W-smooth class contains a unit square,
(ii) first moments `𝔐(y) ≪ (log y)^{β}·polylog`, (iii) cofactor second moments `≪ ℓ^{o(1)}` (K2 §6 item 2). The word
universe 𝔘_W satisfies (i) (no word certificate exists at an odd square: Type II by Lean L9903, Type I by K2
Lemma 2.2 via row 3) and (iii), and satisfies (ii) with **β = 2, not 3**: a word has one free divisor, an ℛ-class
`D | A²` has two (`τ(A+1)` versus `τ(A²)`). Hence the caps apply to ES₅/U not at 3/4 but at **2/3**. The
CONTEXT's reading "Target 3: beat 3/4 for ES₅ or U" mis-states the barrier for those two problems: for ES₅ and U
the CRT ceiling is (log N)^{2/3+o(1)}, and it is attained (§3, Theorem 3.1).
### §1.4 Open doors

## §2 Round 2

## §3 Round 3

## §4 Numerics and controls

## §5 Hostile reviews (verdicts)

## §6 Remaining gap
