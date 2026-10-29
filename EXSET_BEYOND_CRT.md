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
| 4 \| tu−1 (in E(t,v)) | 1/(m'v) + 1/(m'v(tv−1)) + 1/(nm'(tv−1)), tu−1 = 4m' | Type I, (1, tv−1, v, m') | subclass of E(t,v) mod 4(tv−1): Type I with **d = m' free** |

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
### §1.4 Open doors (my words) and the two chosen

By the operational definition of §1.2, a door is a true property of [1,N] (or of the primes) that fails for N·π.

* **D1 Archimedean truncation.** On [1,N] a class of modulus > N holds ≤ 1 integer, words with u = 1 or t = 1
  are single points, and a k-fold intersection of lcm > N is empty unless its CRT residue lies in [1,N]. π knows
  none of this. (CONTEXT doors (i), (ii); IF2 hybrids / weak SPW.)
* **D2 True high-order correlations.** Exact k-fold witness counts on [1,N] for k ≥ (log N)^θ/log log N
  (TC^alt_θ). Bounded k is useless whatever its precision (TU Thm 3.1; NC Cor 8.7).
* **D3 Super-polynomial frequency level** against residue-DENSE classes with ≥ 2 primes above exp((log N)^{1/4})
  ((A*), (DCC), (RD′)).
* **D4 Shift-uniform avoider count** (W_𝔊) (per-frequency weights < 1).
* **D5 Primes of the family beyond N^{O(1)}.** Multiplicative (Landau-type) events such as "tn+1 has a prime
  factor q ≡ −1 (mod 4t)" are unions of classes over all primes q ≤ tN+1, i.e. not of bounded level; their
  densities come from Selberg–Delange, not from CRT. (This is lane D's object; I do not work it.)
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
  `Σ_{P(q)<ℓ} μ_{ℓ,v}(q)² τ(q)Γ(q)/q ≤ C_κ(v+1)^c[(log ℓ)^c + ℓ^{κv}]`.

Then there are W, λ₀, C (depending on K, β, γ, c, C_κ only) such that for every finite family 𝔊 of classes of
𝔘 and selector classes `0 mod p`, mixed arbitrarily, arbitrary moduli, and every majorant ν of 𝒜(𝔊) of level
λ ≥ λ₀,

    log(1/Eν) ≤ C λ^{β/(β+1)} (log λ)^{γ/(β+1)}.

If every modulus of 𝔊 satisfies `G ≤ P(G)^{1+B}` and (ii) holds with γ = 0 for such classes, the bound is
`C_B λ^{β/(β+1)}`.

*Proof.* K2 Thm 5.1's proof uses exactly the three listed inputs (K2 §6 item 2; checked line by line: the base
Lemma 2.3 uses only (i); the chain-rule density `Q'(n ≡ b (m)) ≤ Γ(m)/m`, EK Thm 4.1/Cor 2.6 and the leak mechanism
are arithmetic-free; first moments enter only through 𝔐; second moments only through Lemma 4.1, whose proof is
family-free, fed by (iii); Lemma 4.3 then gives `E p_ℓ² ≤ C(W)ℓ^{−7/4}(log ℓ)^c` and leak ≤ 1/2). Only the cost
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
(tu−1)/4, since `t | 4d+1` and `nt + 1 = (tu−1)(tv−1) ≡ 0 (mod 4d)`). A Type II solution at `n = y²` is
excluded by Lean L9903 (`4abcd ≠ a+b+m²c` for all positive integers; re-checked by brute force for m < 60,
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
use `τ ≤ x^{ε}`. So the sum is `≤ x log x Σ_s h(s)/s + x^{1+ε}x^{−1/4}Σ_s h(s)s^{−3/4} ≤ C(W)x log x` (both Euler
products converge). By partial summation the *body* `A ≤ X := y^{u₀}`, `u₀ = 12 log log y`, contributes
`≤ C(log X)² = C·144(log y)²(log log y)²`. *Tail:* for a block `K < A ≤ 2K`, `K ≥ X/2`, `u = log K/log y`,
Cauchy–Schwarz gives `≤ (Σ_{P(A)≤y, A~K} Γ(A)²/A)^{1/2}(Σ_{A~K} τ(A+1)²/A)^{1/2} ≤ Ce^{−u/2}(log y)^{1/2}·C(u log y)^{3/2}`
(K2 Lemma 3.1 with F = Γ², κ = 1; `Σ_{m≤x}τ(m)² ≪ x log³x`). Summing over blocks (u-spacing log 2/log y) the tail
is `≤ C(log y)^3u₀^{3/2}e^{−u₀/2} ≤ C`. Under bounded B the body with `X = 8y^{1+B}` is the whole sum. ∎

**Lemma 2.4 (word cofactor sums; PROVED).** The word universe satisfies (iii).

*Proof.* Mirror of K2 Lemma 4.2. *Pair part:* `μ(q) ≤ 8Σ_{i≤3}τ(qℓ^v/2^i) ≤ 32(v+1)τ(q)`, so the sum is
`≤ C(v+1)²Σ_{P(q)<ℓ}τ(q)³Γ(q)/q ≤ C(v+1)²(log ℓ)^8` (K2 Lemma 3.1, κ = 8). *Endpoint part:*
`μ(q) ≤ 8Σ_{i≤3}τ(qℓ^v/2^i + 1)` (terms with `2^i ∤ qℓ^v` omitted), so `μ² ≤ 256Σ_iτ(A_i+1)²`, `A_i = qℓ^v/2^i`.
Long blocks `K < q ≤ 2K`, `K ≥ 4ℓ^{v/3}`: Cauchy–Schwarz gives
`(Σ_{block,P(q)<ℓ}τ(q)²Γ(q)²/q)^{1/2}(Σ_{block}τ(A_i+1)⁴/q)^{1/2}`; the first factor is `≤ Ce^{−u/2}(log ℓ)²`
(κ = 4, u = log K/log ℓ); in the second, `m = A_i + 1 ≡ 1 (mod ℓ^v)` runs over an interval of length `≍ Kℓ^v`
with `ℓ^v < (Kℓ^v)^{3/4}`, so Shiu (F = τ⁴, F(p) = 16) gives `≪ (Kℓ^v/φ(ℓ^v))(log Kℓ^v)^{15}` and the factor is
`≤ C((u+v+1)log ℓ)^{15/2}`. Summing over blocks: `≤ C(v+1)^c(log ℓ)^c`. Short blocks `K < 4ℓ^{v/3}`: `m ≤ ℓ^{2v}`,
so `τ(m)²τ(q)Γ(q) ≤ C_κℓ^{κv/2}` and `Σ_{q≤8ℓ^{v/3}}1/q ≤ C_κℓ^{κv/2}`. ∎

**Corollary 2.5 (the ES₅/U ceiling is 2/3; PROVED given K2/EK, Lemmas 2.2–2.4).** For every finite mixture 𝔊 of
word classes (any grouping, certificate or U refinement) and selector classes, every majorant of 𝒜(𝔊) of level λ
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

**Reading.** For U and ES₅ every CRT method in the barred union is limited to the **Vaughan exponent 2/3**, not
3/4. The 3/4 note's extra factor comes from `τ₃`-type classes (`D | A²`), which certify ES but not ES₅ or U.
So for U and ES₅, Target 3 ("beat 3/4") already needs a non-CRT input to beat **2/3**. Mixtures of K2 types and
word classes have β = 3 (the maximum), so Theorem 1.1's list extends verbatim to the union of the K2 universe and
the word universe: this is a barrier for a class strictly larger than (D)17–(D)29.

**Remark 2.6 (I3; Assessment, flagged for lane E).** I3 words are words with t,u,v ≥ 3, so their (ii)/(iii) are
those of Lemmas 2.3–2.4 (β = 2). Condition (i) fails: I3 holds at squares. Theorem 2.1's base needs only *some* set
`R ⊆ ℤ/Q₀` avoiding the W-smooth classes with `log(Q₀/|R|) = O_W(1)` uniformly in the 2,3,…,W-exponents of Q₀ (K2
uses unit squares). If such an R exists for I3, the CRT ceiling for I3 is also 2/3, and **"reach 3/4 for I3 by
multiplier atoms" (lane E goal 1) is impossible by CRT majorants**: multipliers do not change β. I have not proved
the I3 base lemma.

## §3 The ceiling is attained: a Vaughan-exponent theorem for U and ES₅

**Theorem 3.1 (PROVED, relative to Bombieri–Vinogradov, Brun–Titchmarsh (Montgomery–Vaughan form) and the
elementary lemmas below; ineffective constants).** There are absolute constants c, C > 0 such that for N ≥ 3

    #{p ≤ N prime, p ≡ 1 (mod 4) : U(p) fails} ≤ C N exp(−c(log N)^{2/3}),

and hence the same bound holds for #{p ≤ N : ES₅(p) fails} (U(p) ⟹ ES₅(p), §1.3). More generally, with
`y = B₀(log N)^{2/3}`, the bound holds for #{n ≤ N : n ≡ 1 (4), (n, P_y) = 1, U(n) fails}, and in every interval
(x, x+H] with H ≥ 2 in place of [1,N] with N replaced by H (shift-uniformity, as in EXCEPTIONAL_SHORT Thm 1).

By Corollary 2.5 (bounded-B case: the atoms below have modulus kℓ ≤ ℓ^{1+2κ}) no CRT method over word classes
can improve the exponent 2/3; Theorem 3.1 is sharp for that architecture, up to the constant c.

Within the campaign, the strongest previous statement for U or ES₅ at primes was qualitative:
`H₄ ≤ h(p)` for almost all p (FOREST_H4 Thm 3.5, rate ≍ (log Y)^{−1/2} at fixed Y), and, for each fixed H, density
≤ exp(−c log²H) (CONJECTURE_S_MODEL). Neither has N-dependence beyond what PNT in fixed APs gives. (git grep; U and
ES₅ are campaign-internal notions, so no literature comparison applies.)

### §3.1 Atoms (the only new design choice)
Keep the note's parameters: κ = 1/480, t = log X, K = ⌊X^κ⌋, H = K¹⁰, K(K) = {k ≤ K : k ≡ 1 (4)},
L_K = lcm K(K), blocks I_j = (x_j, min(2x_j, X)], x_j = 2^j X^{1/2}, z_j = x_j^{1/6}. A **U-atom** is a triple

    A = (k, ℓ, w):  k ∈ K(K),  ℓ ∈ I_j prime,  H < w ≤ z_j,  4w | kℓ + 1;   class  E_A = {n ≡ −4w (mod kℓ)}.

(Then gcd(w,k) = 1 and ℓ ≡ 3 (4).) *U-certificate:* if n ∈ E_A and n > kℓ − 4w, then (t, u, v) = ((kℓ+1)/(4w),
(n+4w)/(kℓ), 4w) is a word of n with endpoint v ≡ 0 (4), u ≥ 2, `tv − 1 = kℓ > 1`, `tu − 1 ≥ 2t − 1 > 1`; so
U(n) holds, with the identity 4/n = 1/(w(tu−1)) + 1/(ntw) + 1/(ntw(tu−1)) (row 2 of §1.3; checked in
`scripts/z50_ncrt_identities.py`, 25 230 atom words, 0 failures). Compared with the note: the note's two free
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

**Lemma 3.3 (one-variable lattice sums; PROVED).** For k ≤ K, (a,k) = 1, d | K²-bounded with (a,d) = 1,
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
note's Cor 4.3: an active atom has k | c + 4w with (w,k) = 1, so (c,k) = 1. ∎

**Lemma 3.6 (moments, void; PROVED).** (a) For every m ≥ 1, `E((H_X)_m | S_y = 1) ≤ (C_u t²)^m`. (b) With
`y = Bt²`, B ≥ B₀: `P(H_X = 0 | S_y = 1) ≤ e^{−c_v t²}`.
*Proof.* (a) verbatim note Thm 5.1. (b) Note Lemma 6.1 with h replaced by g and `t³` by `t²`: `Σ_{k≤K, p|k}1/k ≤
(1+log K)/p` gives `g(J_c) ≥ (a₀ − 2Z(c))log K`, `Z(c) = Σ_{y<p≤K, p|L_K, p|c}1/p`; `E(e^{yZ} | S_y = 1) ≤ e⁴`, so
`P(Z > a₀/4 | S_y=1) ≤ e^{4 − a₀Bt²/4}`; on `Z ≤ a₀/4`, `μ_c ≥ a t·(a₀κ/2)t`. Take B₀ = 8a a₀κ/a₀ … i.e. B₀ with
`a₀B₀/4 ≥ 2a_v`, `a_v = a a₀ κ/2`. ∎

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
g(J_c), and `#{d : φ(d)/d < δ}` decays doubly exponentially in 1/δ). I have not written this out. The square floor
(E_U(N) ≥ √N/2) is far below either bound.

**Remark 3.9 (controls).** Odd squares lie in no atom class (Lemma 2.2; CERTIFIED for the toy family below, 0 of
≈2 100 squares hit). The hard primes 193, 2521, 3361, 9601, 66529 are hit by no toy atom (X ≤ 3000, K = 21), while
409, 577, 5569, 8813281 are; this is consistent with a density statement and says nothing pointwise. Numerator 8:
the atom identity is specific to 4 (it needs 4w | kℓ+1); the m/n analogue (mw | kℓ+1) would give a density
statement for m/n, which is consistent with the finitely many 8/n exceptions (11, 17, 131, 241). Linnik: the theorem
is one-sided (an upper bound for a lower-tail event); no two-sided asymptotic is asserted.

## §3b Round 3 (pending)

## §4 Numerics and controls

## §5 Hostile reviews (verdicts)

## §6 Remaining gap
