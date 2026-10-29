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
### §1.3 Are ES₅ and U subfamilies of the KARY2 mixture?
### §1.4 Open doors

## §2 Round 2

## §3 Round 3

## §4 Numerics and controls

## §5 Hostile reviews (verdicts)

## §6 Remaining gap
