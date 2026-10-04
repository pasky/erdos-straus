# EXCEPTIONAL_KARY2: second independent hostile review (headline)

Subject: branch `side-agent/kary-no-b` at `be227df` (EXCEPTIONAL_KARY2.md, checkpoint 1).
Reviewer branch: `side-agent/review-kary2b`. Scope: (A) the exponent chain and its consistency with
the lower bound, (B) mixing the three class types in one construction, (C) the scope of Cor 6.1
and the wording for DISCOVERIES. The analytic lemmas (3.1–3.6, 4.1–4.2) were checked only at the
level of exponents; a line-by-line check is the other reviewer's job.

Inputs read: EXCEPTIONAL_KARY2 (all), EXCEPTIONAL_KARY §§1–4, EXCEPTIONAL_TWIN §§1.2 and 2.2′,
EXCEPTIONAL_THETA Lemma 2.9, Remark 2.6, §§3.2/3.7 and 6.1, EXCEPTIONAL_NONCRT Thm 2.3, and
`paper/es-threequarter-note.tex` §§2 and 6–7.
New script: `scripts/kary2_review2_checks.py`, with output in `data/kary2/review2_checks.txt`
(about 3 min, < 1 GB).

## Verdicts

| item | verdict |
|---|---|
| Thm 5.1 (no B, all three types, `≤ Cλ^{3/4}(log λ)^{3/4}`) | **SOUND** at the exponent level. The (log λ)^{3/4} is correctly sourced. |
| Thm 5.2 (bounded B, `≪_B λ^{3/4}`) | **SOUND** |
| Lemmas 2.1–2.3 (square base handles mixed families) | **SOUND**, re-proved and re-checked independently (D1 asks for a small extension) |
| Mixing (B) | **SOUND**: the construction is type-blind except at the three inputs, and each of those is type-additive |
| Cor 6.1, mathematics | **SOUND** (projection plus Lemma 2.9 plus Thm 5.1) |
| Cor 6.1, coverage claims | **NEEDS REPAIR (D1, D3, D4)**: "contains the 3/4 note's majorant" is false as stated; the large-sieve and NONCRT scope is unstated |
| Consistency with the 3/4 note | **CONSISTENT**: no contradiction, the orders match, and both sides' constants are ineffective |

No critical defects. One moderate defect (D1), which is a scope gap with a five-line fix; the rest are minor.

## (A) The exponent chain, re-derived

Ledger (EK Thm 4.1): R-term `≤ 2W`, plus singletons below `e^{s₁}`, plus sequential dyadic blocks
`(e^s, e^{2s}]`, plus a linear block, plus 0 above `e^λ`. Write the class mass as
`𝔐(e^s) ≤ m·s³`. Then:

* singletons cost `≍ 𝔐(e^{s₁}) ≍ m s₁³`, because a unary step costs `(4/3)p_ℓ`;
* the block at scale s has `d = λ/s` primes per term (d-locality from the level). Its cost is
  `d·log(C(m s³ + 4d)/d) = (λ/s)(O(1) + log⁺(m s⁴/λ))`. Summing over dyadic s ≥ s₁ gives a
  geometric series dominated by s₁, which is `O(λ/s₁)` once `m s₁⁴ ≍ λ`.

Balancing `m s₁³ = λ/s₁` gives `s₁ = (λ/m)^{1/4}` and a total of `≍ m^{1/4}λ^{3/4}`.
So **the cap is (mass coefficient)^{1/4}·λ^{3/4}**. The exponent 3/4 is "cubic mass against
linear level".
* Bounded B: m = C(B), giving `λ^{3/4}` (Thm 5.2).
* No B: Cor 3.7 gives `m = K₃(log λ)³`, hence `(log λ)^{3/4}`, `s₁ = λ^{1/4}(log λ)^{−3/4}`, as in §5.
  The (log log y)³ in 𝔐 arises as follows. Smooth-dominated moduli (G > y^{u₀}, all primes ≤ y)
  are killed by Rankin `e^{−u/2}` against polylogarithmic Cauchy–Schwarz partners. That forces
  `u₀ ≍ log log y`, and the body `G ≤ y^{u₀}` then pays `(log y^{u₀})³ = u₀³(log y)³`. So the loss is
  `u₀^{3/4}`, nothing else.

Exact check (`kary2_review2_checks.py` (4)): the §5 ledger with `𝔐(e^s) = s³(log s)³`, minimised
over s₁, divided by `λ^{3/4}(log λ)^{3/4}`, gives 11.29, 10.69, 10.43, 10.34, 10.33 for λ = 10⁴…10¹².
With `𝔐 = s³`, the ratio to `λ^{3/4}` is 31.06 … 31.37. Both converge, so the bookkeeping has
no hidden extra log.

**Lower-bound side.** The 3/4 note's atoms `−uv^{−1} mod kℓ` are ℛ(kℓ)-classes `−4u²w`.
Check (3) confirms this on 124,464 atoms (`v^{−1} ≡ 4uw`). Their moduli satisfy
`kℓ ≤ ℓ^{1+2κ}` with `κ < 1/240`, so the note is in Thm 5.2's class with B < 1/120.
* The note works at `t = log X = α(log N)^{1/4}`. That is exactly the singleton/first-block
  boundary `s₁ = λ^{1/4}` of the cap with `λ ≍ log N`.
* Its supply is ≍ t³, the same cubic mass. Its saving is `c(log N)^{3/4}`, against the cap
  `C(B)(log N)^{3/4}`. The orders agree.
* The constants cannot be compared. The note uses ineffective Bombieri–Vinogradov. The cap's
  W₀ is astronomically large: through the c₄ = 2^{29}+2 exponent in Lemma 4.2 (Case A),
  `W^{−1/4}(log W)^{3c+2} ≤ 1/2` needs log W ≈ 10^{10–11}, hence λ₀ ≳ W^{4/3} to absorb the
  R-term 2W.
* So there is no contradiction, and none is possible numerically.

Remark 3.8's heuristic `𝔐_R(y) ≍ (log y)³` is plausible. Under the weight 1/M on y-smooth M,
log M has mean and spread ≍ log y, so `Σ(log M)²/M ≍ (log y)³`. The `(log log N)^{3/4}` is then
a proof artefact, not an achievable gain. That is unproved, so the headline must not claim
"no power of log log can be gained" for unbounded-B families. EXCEPTIONAL_THETA Cor 3.4 claims
this only for its own class.

## (B) Mixing the types in one sequential construction

The construction (EK Thm 2.5/4.1, ETw Thm 2.3′) sees a family only as a set of forbidden cylinders
`n ≡ b (mod G)`. Types enter at exactly three places:

1. **Base (R1).** R_W^□ consists of the unit squares mod each `p^e ∥ Q₀`. It avoids a W-smooth class
   iff the class contains no unit square mod G. CRT lifting goes both ways: a unit square mod
   p^e lifts to one mod p^E, including p = 2 with E ≥ 3.
   * Lemma 2.1(1) re-proved: for p | A, `(p|M) = (M|p)(−1)^{(p−1)(M−1)/4} = (−1|p)(−1)^{(p−1)/2} = 1`,
     and `(2|M) = 1` as M ≡ 7 (8) when A is even. So `(−4D|M) = (−1|M) = −1`.
   * Lemmas 2.1(2) and 2.2 were checked; the proofs are correct.
   * Exact checks:
     - (1) all 15,754 ℛ(M)-classes with M ≤ 3000, including 532 composite and 5 prime-power M:
       none is a square mod M.
     - (2) **mixed base** with W = 13 and `Q₀ = 2⁶3⁴5³7²11²13²`. Every W-smooth class with
       G | Q₀ was tested: 5,572 ℛ(M), 35,950 (a,D) (a ≤ 200, D ≤ 4000) and 528,780 Case-A classes.
       These share primes, prime powers and moduli across types. None contains a unit square.
   * Types never interact in (R1): the condition is per class.
2. **First moment.** 𝔐 is a sum over the universe 𝔘 split by type. Over-counting and cross-type
   coincident classes only enlarge it. Step 1 of EK Lemma 4.2′ uses only the chain rule
   `Q'(n ≡ b mod q) ≤ Γ(q)/q`, which is type-free.
   * The square base changes γ(2) from 1 to 8. This matters only for (a,D) and Case A (ℛ(M)
     moduli are odd), and both lemmas use `Γ(4·) ≤ 8Γ(·)Γ(·)`, resp. h(p) ≤ 7.
   * Non-unit residues (for example p | gcd(a, 4D+a) with p ≤ W) are simply never activated
     under the base, which is consistent with the bound.
3. **Second moment and leak.** `p_ℓ` is the total activated density at ℓ over all types.
   Minkowski over types and over v (Lemma 4.3) handles the cross terms with no independence
   assumption. Lemma 4.1 is applied within a type, with the q′-sum over all (ℓ−1)-smooth q′.
   Classes at different powers `ℓ^v` of the same ℓ, from different types, share the coordinate
   `n mod ℓ^{E_ℓ}`, and `p_ℓ ≤ Σ_v ℓ^{−v}N_{ℓ,v}` counts them all.
4. **Decided at the top prime.** Every modulus is `qℓ^v` with `P(q) < ℓ`, whatever the type. Its
   W-smooth part is decided at the base and the rest at earlier primes. Classes with top prime
   above `e^λ` cost 0, because level-λ functions are independent of those coordinates. They enter
   only the leak, which Lemma 4.3 bounds over all ℓ.

On Q₀: KARY2 says "the lcm" of the family's W-smooth parts. ν may have larger W-smooth parts; this
is harmless, because ETw Thm 2.3′ works with conditional expectations and 𝒜 is measurable with
respect to the history. Not a defect.

## Defects

**D1 (moderate; scope). "This contains the 3/4 note's majorant" is false as stated.**
* The note's majorant is ν_X = S_y·Q_r(H_X), with Möbius selector `S_y = 1[(n,P_y) = 1]` and
  `y = Bt³ > W`. It is ≥ 1 only on y-rough avoiders. It is not ≥ 1 on 𝒜(𝔊), which contains
  multiples of small primes, so it is not a majorant in the sense of Thm 5.1 / Cor 6.1.
  EXCEPTIONAL_THETA handled the selector explicitly (its `log(P/φ(P))` term); KARY2 dropped it.
* Fix: add a fourth class type, **selector classes `0 mod p`**.
  - Base: they contain the square 0 but no *unit* square, so R_W^□ avoids them for p ≤ W.
    Check (2): 0 hits 0 unit squares and 6 plain squares.
  - For p > W they add `Σ_{W<p≤y}1/p ≤ log log y` to 𝔐 and `O(ℓ^{−2})` to `E p_ℓ²`. The
    multiplicity is 1, q = 1, v = 1.
* Then Thm 5.2 covers the note, and §6 "Still excluded" item 2(i) should read "**no class contains
  a unit square** mod its modulus".
* Related: the note bounds `E_pr(N)` and then transfers to E(N) by the multiplicative semigroup.
  That transfer is non-CRT post-processing, but it only loses, so it does not affect the reading.

**D2 (minor; notation). "ET" means two things.** In KARY2, "ET Prop. 1.4" is Elsholtz–Tao (2013),
while "ET Lemma 3.2 / 3.7 / 2.9 / §3" is EXCEPTIONAL_THETA. Lemma 3.6's proof uses both in one
sentence. Use e.g. "ElT Prop 1.4". Also replace the label "PROVED modulo ET Prop 1.4" with
EXCEPTIONAL_THETA's wording, "PROVED, using Elsholtz–Tao Prop. 1.4 (published, not re-proved)".
"Modulo" reads as conditional.

**D3 (minor; scope). Cor 6.1's "Architecture class covered" overreaches by omission.**
* It lists "all prime-slice / sequential / Λ² / Selberg-type majorants of ET, ETw, TW2–TW4, EK".
  It must also say what does *not* transfer from those files:
  - Montgomery's large sieve is covered only fibrewise over ET prime slices (ET Remark 2.6;
    ET §6.1 item 8). KARY2 gives no large-sieve statement for mixtures or arbitrary moduli. The
    large sieve is not a pointwise majorant, and its prime-local input does not see
    composite-modulus forced classes.
  - NONCRT Thm 2.3 (per-frequency rounding with weights w ≥ 1, and no bound on slice-prime size)
    rests on the ET product/fibre argument with a high-level Fourier tail ε. It is not proved for
    the KARY sequential construction. KARY2's Cor 6.1 needs `Σ|a_i|` rounding and primes ≤ N^{A},
    and its exclusion item 3 is correct on this.
* The headline must not import either extension.

**D4 (minor; scope). One relaxation is missing from "Still excluded".**
* Thm 5.1 needs ν ≥ 1 on **all of 𝒜(𝔊) ⊂ ℤ**, because EK Thm 4.1 ends with `g_{J+1} ≥ 1_𝒜` on
  residue histories. Methods with ν ≥ 1 only on `𝒜 ∩ [1,N]`, or only on the exceptional set, are
  outside the theorem. This is distinct from "ν ≥ 0 only on [1,N]", which is listed.
* Also add ET §6.1 item 3 explicitly: majorants ≥ 1 only on exceptional *primes*, used through
  prime equidistribution beyond a selector.
* Comment: with D1's selector classes extended to all p, the *mean* side of a prime-law method is
  capped by the same proof (extra mass log log). The open part is the BV-type error accounting.
  Do not claim this.

**D5 (minor; presentation).** The proof of Thm 5.1 ends with `2W + log 2 + Cλ^{3/4}(log λ)^{3/4}`.
Say that C absorbs `2W + log 2` (W is absolute; λ ≥ λ₀). Also state that W₀ and λ₀ are
astronomically large (see (A)). The theorem is asymptotic only, and Cor 6.1 holds for
`log N ≥ λ₀`-scale N.

**D6 (minor; suggestion, not a defect).** Exclusion item 2's three sufficient conditions could cite
Schinzel's theorem (no polynomial identity for 4/(at+b) when b is a quadratic residue mod a, as
quoted in the Elsholtz–Tao intro). This would make (i) automatic for every polynomial-identity
family, leaving only the moment conditions family-specific. Not checked here, so attribute it if
used.

## (C) Scope of "no θ > 3/4", and wording for DISCOVERIES

**Covered.** Methods of this form: #(𝒜(𝔊) ∩ [1,N]) ≤ N·Eν + Σ|a_i| with Σ|a_i| < N, where
* ν = Σ a_i 1[n ≡ b_i (d_i)] is ≥ 0 on ℤ and ≥ 1 on 𝒜(𝔊);
* 𝔊 is any finite mixture of ℛ(M), (a,D), Case-A (and, after D1, selector) classes;
* all primes are ≤ N^{O(1)}.

This includes:
* Bonferroni / inclusion–exclusion truncations. `C(H−1, 2m) ≥ 0` pointwise, and the coefficient
  sum is the rounding.
* Selberg Λ² over any set system of these classes. The Λ² error `Σ|λ_Tλ_{T′}|` is ≥ the merged Σ|a_i|.
* β-/Rosser and any combinatorial upper-bound sieve on the class system. `(1∗λ⁺)(m) ≥ 0` for every
  hit-set makes ν ≥ 0 on all of ℤ.
* Moment/variance methods evaluated by CRT (NONCRT Prop 4.1).
* Any number of prime factors per modulus, prime powers, and no B. The cost is a factor
  (log log N)^{3/4} without B and none with B.

**Not covered.**
* The Montgomery large sieve beyond ET prime slices.
* Inter-frequency cancellation in Σν − N·Eν (Kloosterman/dispersion, Erdős–Turán/Vaaler). Note
  that even the per-frequency w ≥ 1 version is proved only for ET Cor 3.4 families.
* Per-frequency weights < 1 (NONCRT §2.5, open).
* ν nonnegative only on [1,N], or ≥ 1 only on 𝒜 ∩ [1,N], on the exceptional set, or on
  exceptional primes.
* Non-CRT arithmetic input (Type I/II, Halász, prime equidistribution beyond a selector).
* Classes of other types, unless they satisfy (i) no unit square, (ii) first moment
  `≪ (log y)³·polylog log y`, and (iii) cofactor second moments `≪ ℓ^{o(1)}`.
* Family primes beyond N^{O(1)}.
* Whether unbounded-B families can beat the 3/4 note by a power of log log N (expected not,
  Remark 3.8; open).

**Suggested DISCOVERIES entry (after D1 is applied):**

> **No θ > 3/4 for coefficient-sum CRT sieves over any mixture of forced classes
> (EXCEPTIONAL_KARY2 Thm 5.1, Cor 6.1).**
> * Setting: any finite family of ℛ(M)-, (a,D)-, Case-A and selector classes, with arbitrary
>   moduli (no B, no dominant prime, any number of prime factors) and all primes ≤ N^{O(1)}.
> * Claim: every ν ≥ 0 on ℤ, ≥ 1 on the whole avoider set, used through
>   `#(𝒜∩[1,N]) ≤ N·Eν + Σ|a_i|` (with Σ|a_i| < N), saves ≤ C(log N)^{3/4}(log log N)^{3/4}.
>   If every modulus has G ≤ P(G)^{1+B}, the saving is ≤ C_B(log N)^{3/4}. This matches the 3/4
>   note, whose atoms have B < 1/120.
> * Covers Bonferroni, Selberg Λ², β/Rosser and any combinatorial upper-bound sieve on these
>   classes, and CRT-evaluated moment methods.
> * Does not cover: the large sieve beyond prime slices; rounding cancellation; weights < 1;
>   majorants ≥ 1 only on [1,N] or on exceptional primes; non-CRT input; other class types; or
>   primes beyond N^{O(1)}.
> * Key new inputs:
>   - (a,D)- and Case-A classes contain no square (Mordell/Jacobi), so one unit-square product base
>     serves all types;
>   - Rankin plus Cauchy–Schwarz on smooth-dominated moduli removes B at the price of (log log)³
>     in the mass.
> * Status: **PROVED** (internal). The Case-A part uses Elsholtz–Tao Prop. 1.4 (published). The
>   ℛ(M)/(a,D)/selector part is unconditional.

## Replay

```
ulimit -v 8000000; timeout 900 env PYTHONPATH=scripts uv run --with sympy python \
  scripts/kary2_review2_checks.py 3000 > data/kary2/review2_checks.txt   # ~3 min, < 1 GB
```

---

## Round 2 (author's repairs at `side-agent/kary-no-b` 575e913)

The full diff `be227df..575e913` of EXCEPTIONAL_KARY2.md was read, along with the O14 report's
headline lines.

**D1 (selector classes): FIXED, SOUND.**
* *Definition 2.0.* `0 (mod p)` is added as a fourth type. It is correctly marked as not forced.
* *Base.* Lemma 2.3(R1) is now stated for "W-smooth classes containing no unit square". The
  proof is correct: CRT turns `c ≡ b (mod G)`, with c a unit square at every `p^e ∥ Q₀`, into b
  being a unit square mod G. Selector classes with p ≤ W contain no unit, and the first three
  types exclude even non-unit squares. The R-term `≤ 2W` is unchanged, since `P_W | Q₀` already.
* *First moment.* Lemma 3.3′ gives `Σ_{W<p≤y}γ'(p)/p ≤ log log y + O(1)`, with
  `γ'(p) ≤ 1+2p^{−1/2}` for p ≥ 16. Correct.
* *Second moment.* Lemma 4.2 has v = 1, q = 1, μ = 1, so the sum is 1. The class is always active
  and adds 1/ℓ to `p_ℓ`, so under Minkowski it contributes `ℓ^{−1}`, within `ℓ^{−7/8}`. The leak
  is unaffected. "Decided at the top prime" holds trivially.
* *Theorems.* Thm 5.2's `G ≤ P(G)^{1+B}` is automatic for selector classes, and the proof cites
  Lemma 3.3′.
* *The 3/4 note is now literally covered (Remark 5.4).*
  - Pointwise on ℤ, `ν_X = S_y·Q_r(H_X)` with `S_y ∈ {0,1}` and `Q_r(H) = C(H−1,r)`, r even. This
    is ≥ 0 for H ≥ 0 and equals 1 at H = 0. Checked exactly for H ≤ 199, even r ≤ 20.
  - So ν_X ≥ 1 on all of `𝒜(𝔊₀ ∪ {0 mod p : p ≤ y})`, including n ≤ 0 (0 lies in a selector class).
  - Its ledger satisfies Cor 6.1: primes ≤ X ≤ N, `T_abs ≤ N^{1/2} < N`, error ≤ `T_abs`.
  - The atoms have B < 1/120. Thm 5.2 therefore applies, with no gap.

**D2: FIXED.** "ElT" is defined, and no "ET Prop" or "modulo" survives. The labels read
"PROVED, using ElT Prop 1.4 (published, not re-proved)". "No external input" replaces
"unconditional", which is accurate.

**D3: FIXED.** The large sieve (fibrewise ET slices only) and NONCRT Thm 2.3 are explicitly marked
"not transferred".

**D4: FIXED.** "Still excluded" item 3 lists three relaxations: ν ≥ 0 only on [1,N]; ν ≥ 1 only on
𝒜∩[1,N] or on the exceptional set; and the prime-law case. The prime-law mean-side remark is
correctly marked as not claimed. Thm 5.1 and Cor 6.1 now say "all of 𝒜(𝔊) ⊂ ℤ".

**D5: FIXED.** C absorbs `2W + log 2`, and §0, Thm 5.1 and Cor 6.1 state that the result is
asymptotic only, with astronomical constants.

**D6: FIXED** as a pointer ("not checked here"). Condition (i) is correctly restricted to W-smooth
classes and to unit squares.

**Other changes checked in passing.**
* Lemma 3.1: the p ≤ W step now uses `p^η ≤ e` and `p^{−e(1−η)} ≤ p^{−0.9e}`. Correct.
* `c_q = 2^{7q+1}+1` matches the final line of Lemma 3.5's proof.
* §1's B3 is refined into three uses; consistent.
* Cor 6.1 now says "no method *of this class*". The O14 report's headline is qualified the same way.

**New residual (cosmetic, not blocking).**
* **R2-1.** Remark 5.4 says "the R-term here is ≤ 2W, smaller than ET's `log(P/φ(P))` for
  selectors". This is misleading. Selector primes p > W are not free: they are paid in the
  singleton ledger, about `(8/3)Σ_{W<p≤y}1/p ≍ log(log y/log W)`. Only p ≤ W go into the R-term.
  Numerically, 2W ≈ exp(10^{10}) is far larger. Suggest instead: "selector primes ≤ W are absorbed
  by the base, and those > W cost `O(log log y)` in the singleton steps, the same order as ET's
  term."

**Verdict, round 2:** all six defects are resolved. Theorems 5.1 and 5.2 and Cor 6.1, with the
four types, are SOUND at the level this review covers (exponents, mixing, scope). The 3/4 note
is literally inside Thm 5.2. The DISCOVERIES entry proposed in round 1 can be used as-is.
