# Final hostile cross-lab review (Claude Opus): `notes/z80/BEYOND_34.md` §§15–16 (ST, LM), revised §0, QB2 fixes

Reviewer: Claude Opus (Anthropic), cross-lab. Author: GPT-6.2 Astra lane. The object is commit `cf856188b`, the diff
`ff57ac6f3..cf856188b`, which touches only `notes/z80/BEYOND_34.md` (+41/−9).

The scope is the new material only:
* the rewritten §0;
* the §10/§11 edits that answer `REVIEW_BEYOND_34_QB_OPUS2.md` (on `side-agent/z80-xrev-qb`, read with `git show`, not
  copied here);
* the new §15 (Theorem ST) and §16 (Theorem LM).

I did not re-review historical theorems (P, Lemmas 1–6, Q, QB, QR, UB) beyond what the new text relies on. This is an
internal review only. **ES in ℕ is OPEN.** Nothing here proves ES, cap zero, a bounded cap, or a new ambient exponent,
and the note does not claim any of these.

## Verdict

| item | verdict |
|---|---|
| **ST part 1** (polynomial pivot height; no §11-list slot is plantable at `L ≤ U^C`) | **ACCEPT** (trivial but correct) |
| **ST part 2** (GRH pivot height, unconditional on a subsequence; ≥ `⌈5D+10⌉` slots fail for all but `o(1)` of a hard prime profile) | **ACCEPT-WITH-FIXES** (mathematics correct; scope and wording fixes F1–F3) |
| ST "What this means" Assessment | ACCEPT-WITH-FIXES (one overstatement, one confusing parenthesis) |
| **LM** (exact marginals at every `Q ≤ N^{A_0}` plus balanced-avoider mass `≥ (1−o(1))e^{−F(λ)}`) | **ACCEPT-WITH-FIXES** (proof correct for all three universes claimed; wording F4–F6) |
| LM scope paragraphs (weighted law vs. interval counts) | ACCEPT. Correctly non-universal; cross-references should be added (F7) |
| Revised §0 | ACCEPT-WITH-FIXES (F8–F10: missing Q label, STATUS-delta pointers, line-cap risk) |
| QB2 fixes 1–4, 6 | **verified applied** |
| QB2 fix 5 | partially applied (F9) |
| Triage (ST, LM = BARRIER-SCOPED; explicitly not BARRIER-BROAD) | **AGREE** |

I found no mathematical error in the new material. On the points I was asked to probe:
* ST is *not* presented as a universal single-target impossibility, and it is not one.
* LM is *not* presented as a statement about integer intervals with `O(1)` counts, and it is not one.
* The word-universe version of LM is genuinely covered by `EXSET_BEYOND_CRT.md` Thm 2.1/Cor 2.5.
* The small-`A_0` and large-bias-period case is handled correctly by `λ = max(1,A_0) log N`.

## 1. QB2 fixes (independent check against `REVIEW_BEYOND_34_QB_OPUS2.md` §6)

| QB2 fix | status in `cf856188b` | check |
|---|---|---|
| 1. Reason the v-lists avoid `R` and `𝒞` (size is no argument under GRH) | Applied, §11 "Candidate lists" | The text says `v ≡ 3 (4)`, the primes of a hard `R` are `≡ 1 (8)`, and `𝒞 ⊂ 1 (4)`. It also says `v > 3` and that the residue at `q` is a unit (so `v ≠ q`). The nonhard-`n` branch is closed by integral scaling before the lists are formed. All correct. |
| 2. `j = 1` clash at the end of §11 | Applied: "with subgroup index one (no Minkowski or short-relation deletion)" | Correct. It also answers fix 6 (no Minkowski II, no deletion). |
| 3. "Ineffective" for both forms | Applied in the QB header ("both forms ineffective as written via Maynard's use of Siegel–Walfisz"), in the §0 Label ("GRH version … also ineffective as written") and in the STATUS delta | Correct. |
| 4. Cite an exact reconstruction, not only the modular `R=241` example | Applied: QB2 `scripts/z80_xrev_qb_opus2.py` and §5D, "25 full rational reconstructions at three small L, including reduced denominator support and scaling"; §5C described as a modular order-of-choices check | These match QB2 §5D (L ∈ {364, 6916, 1293292}, 25 Fraction reconstructions, scaling to `R²` and `R·p`) and QB2 §5C. Caveat: the pointer dangles until the orchestrator merges `side-agent/z80-xrev-qb` (F11). |
| 5. STATUS delta: keep Z75 effective; QB ineffective; GRH form supersedes Q and the z78 `2√2` clause; window and denominators unbounded | Partly applied | Z75 effective and the explicit prime bound are retained, and "ineffective" is present. But the delta does not explicitly drop the `2√2` GRH clause, and it omits the "no height limit on `qb` / den `z`" clause. That clause is in §0 Scope but not in the proposed STATUS text. See F9. |
| 6. (Optional) no Minkowski II, no deletion | Applied (see fix 2) | — |

Replay: `ulimit -v 6000000; timeout 300 uv run --offline --no-project python -B scripts/z80_beyond34.py` reproduces
`data/z80/beyond34.txt` exactly (diff empty). That includes the 8266/2802/18 packet counts and the `R=241` binary packet
with `b = 702947178360131601769` and digit set `[71]`. The script is unchanged by this commit, so this only confirms
that the cited data still stand.

## 2. Theorem ST

### 2.1 Preliminaries (shared by both parts)

The cofactor primes satisfy `r − 1 | L ≤ U^C`, so there are at most `τ(L)` of them and each is `≤ L+1`. The classical
bound `τ(L) ≤ exp(O(log L/log log L)) = U^{o(1)}` gives:
* `log b ≤ τ(L) log(L+1) = U^{o(1)}`;
* `#{(L,b)} ≤ U^C · 2^{τ(L)} = exp(o(U))`.

Both are correct. **b is squarefree by hypothesis**, and this matters: with prime powers allowed, `b` and `K′` would be
unbounded and part 1 would fail. The statement says squarefree, and §12 already excludes "unbounded powers of cofactor
primes" from its own barrier. Consistent.

### 2.2 Part 1

With `U = log R` and `q ≤ e^{C_0U}`, we have `log K′ ≤ log(R + qb) ≤ (max(1,C_0) + o(1))U`. The §11 list lower endpoint
is `V^{1/2} = e^{C_1U/2}`, and §11 takes `C = C_1` with `C/C_0` large. So `K′ < v` for every list prime and large `U`,
and a positive integer has no divisor exceeding it. **Correct and unconditional.**

The restriction "Smaller generator primes are not covered" is stated. Part 1 is really an observation about the §11
parameters: QB *needs* `log L ≍ U^{ε/2}` so that `b` can be huge. Part 1 is a cleaner restatement of why the §11 list
heights are incompatible with polylog `L`. It does not supersede §12's divisor-bound barrier and does not claim to.

### 2.3 Part 2: inputs

**Clean conductors.** Take `Z_i = 2^{2^i}` and `c < c_P/2`. A zero `β_i > 1 − c/log Z_i` satisfies
`β_i > 1 − 2c/log Z_{i+1} > 1 − c_P/log Z_{i+1}`. Its conductor is `≤ Z_i ≤ Z_{i+1}`. Page's uniqueness at `Z_{i+1}`
therefore forces `χ_i = χ_{i+1}`, and inductively one character for all late `i`. That character would then have zeros
`β_i → 1`. This is impossible because `L(s,χ)` is analytic and nonzero at `s = 1`, so its zeros cannot accumulate
there. The note's phrase "nonvanishing in a neighbourhood of 1" is exactly this. **Correct.** The resulting set of
clean `Z` is infinite but possibly sparse, hence "along some sequence".

**Parameters.**
* `w = (log Z)/3`, `T = exp((log Z)²)`, `U = log₂T = 2 log₂Z`, so `log w = U/2 − log 3`. ✓
* `M = 8∏_{3≤s≤w} s` has `log M = log 4 + θ(w) ~ (log Z)/3 < log Z`. Chebyshev suffices. ✓
* The profile `R ≡ 1 (M)` gives `(s/R) = (R/s) = 1` for odd `s ≤ w`, using `R ≡ 1 (4)`, and `(2/R) = 1` from
  `R ≡ 1 (8)`. These `R` are hard, since their sole prime factor is `≡ 1 (8)`. They are `≡ 1 (3)`, so the
  carrier-at-3 escape is also closed.
* Every pivot with `(q/R) = −1` is `> w`. The small-nonresidue fallback at `r ≤ L+1 ≤ U^C+1 < w` cannot fire. ✓

**Profile lower bound (TZ Thm 1.4 over ℚ, `L = ℚ(ζ_M)`).**
* TZ's `Z`-parameter is `≤ M ≤ Z`, and `log T/log M ≥ log Z → ∞`, so the range holds and both relative error terms
  are `o(1)`.
* A harmful exceptional term (a real character mod `M`, conductor `≤ Z`) has `β ≤ 1 − c/log Z` by cleanness. Then
  `(1−β) log T ≥ c log Z → ∞`, so `Li(T^β) = o(Li(T))` at both endpoints.
* This holds even if TZ's own strip constant exceeds `c`; the note's sentence covers that case.
* The result is `≫ T/(φ(M) log T)` profile primes in `(T,2T]`. ✓

### 2.4 Part 2: union bound

* **Fixed data.** Fix `(q,L,b)`, a menu, `t` slots and a list of distinct primes `v_i ∈ (w, e^{DU}]`.
* **Gcd case.** If `v_i | qb`, then `v_i | R`, which is impossible since `v_i ≤ (log T)^D < T`. In fact this case is
  empty: `v_i` is a unit mod `q`, and every prime of `b` is `< w`. ✓
* **CRT.** Otherwise one reduced class mod `M∏v_i`. Its modulus satisfies
  `log(M∏v_i) ≤ log Z + tDU = O(√log T) = o(log T)`. ✓
* **BT.** `π(2T; m, a) ≤ (2+o(1))·2T/(φ(m) log T)` when `m = T^{o(1)}`. Dividing by the profile lower bound gives a
  relative probability `≪ φ(M)/φ(M∏v_i) = ∏(v_i−1)^{−1}`, with one absolute constant, not one per slot. ✓
* **Per-residue sum.** `Σ_{v ≡ a (q), w<v≤e^{DU}} 1/(v−1) ≤ O(1/w) + Σ_{k≥1} 1/(kq) ≪ 1/w + (1+DU)/q`. ✓
* **Per-slot cost.** With `q > w` and `≤ U^D` residues per slot, a slot costs `≤ U^{D+1}·O(D)/w = e^{−U/2+o(U)}`. ✓
* **Union.** The factors are:
  * `#q ≤ e^{DU}`;
  * `#(L,b) ≤ e^{o(U)}`;
  * `#menus ≤ e^{DU}`;
  * `#(t-subsets) ≤ U^{Dt} = e^{o(U)}` for fixed `t`;
  * the product over slots, dropping distinctness (an upper bound).

  The total is `exp((2D − t/2 + o(1))U)`, and `t = ⌈5D+10⌉` gives `exp(−(D/2+5+o(1))U) = o(1)`. Any `t > 4D` would do,
  so the stated `t` is generous. ✓

**Quantifiers.** The system may depend on `T, q, L, b` but not on `R`. The selection inside the system may depend on
`R`. The union bound sums over all selections, so this is legitimate. The conclusion is "∀ system, most profile `R`",
and the note says explicitly that it is not "∃ `R` failing every system". That would be false: a system tailored to one
`R` can encode its answer. **Correct as stated.**

**Uniformity.** The `o(1)` depends only on `D` and the clean sequence, not on the system. ✓

### 2.5 Does ST block what the Assessment says it blocks?

The menus are indexed by (generator of the squares, target, digit set). That is `≤ q·q·2^{k} = q^{O(1)} ≤ e^{O(DU)}`
menus, R-independent. The target `(−g^{L_o})^{−1}` depends on `R` through `K′`, so it is a selection, which is allowed.
The slot residues are the roots of `v^{2L} = h^{2^i}`, at most `gcd(2L, q−1) ≤ 2L ≤ U^D` of them after enlarging `D`.
§11's lists lie in `(V^{1/2}, V] ⊂ (w, e^{DU}]` for `D ≥ C_1`. So:
* a full binary basis of length `k ≍ log q ≥ U/2 > t` at `L ≤ U^C` fails on all but `o(1)` of the profile;
* so does any adaptive scheme that needs `≥ t` large slots.

Because QB-type statements are **pointwise in R**, a thin profile suffices to block them. The profile has relative
density about `exp(−(1/3+o(1))√log T)` among primes. **The note should say this explicitly** (F2), because it is the
whole reason a thin, sparse-subsequence profile is a meaningful obstruction rather than a curiosity.

### 2.6 Scope: what ST does not exclude (checked against the text)

**No universal single-target impossibility.** The note says so three times: "ST does not force …"; "neither a polylog
cap by this route nor a universal impossibility theorem for single-target constructions"; Triage "Not BARRIER-BROAD for
general single-target". I agree that none is proved. ST says nothing about:
* `< t` contacts. In particular, a target that happens to have few nonzero digits is not excluded. Typical digit
  weight `≍ k/2` is plausible but not proved for profile `R`, and the note correctly does not claim it.
* non-squarefree `b`;
* cofactor mechanisms other than `r−1 | L`;
* small generators `v ≤ w` (see F1);
* pivots `q ≤ w`, which would not be QB pivots anyway.

**F1 (substantive scope point, should be stated).** The small-generator exclusion is more than a technicality on this
profile. Because `R ≡ 1 (s)` for all `s ≤ w`, the event `v | R+qb` for `v ≤ w` is **deterministic**: it is `v | 1+qb`,
independent of `R`. So ST's own hard profile is exactly the profile on which a scheme built from small generators
(`v ≤ w`) faces no randomness at all. Whether that helps or hurts depends on whether `1+qb` can be made to carry the
needed residues. The sentence "use small factors" in the Assessment gestures at this. It should be made explicit that
the profile **fixes**, rather than randomises, all small-prime divisibilities. Otherwise a reader may think ST is evidence
against small-generator variants, when it is silent on them.

## 3. Theorem LM

### 3.1 LP and duality

* **Primal.** `min E_0 f` over `f ∈ V`, `f ≥ 1_𝒜` pointwise on `ℤ/period`. Writing `f = Σ c_jφ_j` with free `c_j`, the
  dual is `max Σ_{x∈𝒜} μ(x)` subject to `μ ≥ 0` and `Σ_x μ(x)φ_j(x) = E_0φ_j` for all `j`. This is correct: free primal
  variables correspond to dual equalities.
* **Strong duality.** The primal is feasible (`f ≡ 1 ∈ V`) and bounded below by 0, so strong duality holds and the dual
  optimum is attained with value `v`. Normalisation follows from `1 ∈ V`. ✓
* **Exact marginals.** Every class mod `Q ≤ N^{A_0}` has level `≤ log rad Q ≤ A_0 log N ≤ λ` and `Q | period`, so its
  indicator lies in `V` and `μ(a mod Q) = 1/Q` exactly. ✓
* **Primal lower bound.** A feasible `f` is a combination of level-`≤ λ` classes on `ℤ`, `≥ 0` everywhere and `≥ 1` on
  `𝒜`. That is exactly a majorant in the sense of `sieve-limits-note` Def. `def:majorant` / Thm `noBcap`. Hence
  `v ≥ e^{−Cλ^{3/4}}` for `λ ≥ λ_0`. ✓
* **Difference from `compmeas`.** `compmeas` normalises `μ|_𝒜/m*`. LM keeps `μ`, which is why its marginals are exact.
  That is the whole novelty relative to `compmeas`, and the note's "uses the duality already present in `compmeas`" is
  honest.

**Bias removal.**
* `B = (S/(ηm))^{2k} ≥ 1_{|S|≥ηm}` and `B ≥ 0`.
* Each monomial in the expansion is a function mod a product of `≤ 2k` distinct `s ∈ (Y,2Y]`. Repeated `(n/s)²` is
  `1_{s∤n}`, still a class function mod `s`. The level is therefore `≤ 2k log(2Y) ≤ log N ≤ λ`, so `B ∈ V` and
  `E_μB = E_0B`.
* Re-deriving (17): `log E_0B ≤ k log(2k/(η²m)) = −((A−1)/(2A) + o(1)) log N`. This is a power saving, hence
  `o(e^{−Cλ^{3/4}})`. So `μ(𝒜 ∩ {|S|<ηm}) ≥ v − μ(|S|≥ηm) ≥ (1−o(1))e^{−F(λ)}`. ✓

### 3.2 The "special small-A level" and the bias period

The bias primes number `m ≍ (log N)^A/log log N`. Their **product** is `e^{(1+o(1))2Y}`, far above `N^{A_0}` for any
`A_0`. So the bias period is not among the `Q ≤ N^{A_0}` cylinders, and the proof correctly adds it to the common period
separately. Three checks:

1. **Do extra primes in the period hurt `noBcap`?** No. `noBcap` is a statement about majorants on `ℤ` with arbitrary
   moduli. It charges only primes `> W`, each once. Adding coordinates on which `𝒜` does not depend cannot lower the
   primal optimum below the `noBcap` bound. (Equivalently, conditional expectation onto the family coordinates maps a
   level-`≤ λ` majorant to one of no larger level and equal mean.) If a bias prime also divides a family modulus,
   nothing changes. The bias primes exceed the theorem's fixed `W` for large `N`. ✓
2. **Is `B` inside `V` when `A_0 < 1`?** Only because `λ = max(1,A_0) log N ≥ log N`. With `λ = A_0 log N` and the §13
   choice `k = ⌊log N/(2 log 2Y)⌋`, `B` would have level up to `log N > λ` and would **not** lie in `V`. The `max` is
   therefore essential as written, and it is present. (Optional: for `A_0 < 1` one could take
   `k = ⌊A_0 log N/(2 log 2Y)⌋`. That keeps a power saving `N^{−A_0(A−1)/(2A)}` and gives `F(A_0 log N)`, a better
   constant. This is not needed.)
3. **Many or large bias primes.** Bias primes beyond `N^{o(1)}` (e.g. a bias test at primes `≍ N^{a}`) would charge level
   `≍ 2k·a log N`, and the fixed-level scheme would need `k = O(1/a)`, losing the high moment. LM is explicitly tied to
   §13's `S, η, m` (polylog primes), so this is outside its scope. It is not a gap, but it is worth one clause (F6).

### 3.3 Does the word result really cover the claim?

* **(★) is in the word universe.** (★) `n = 4uBC − u − B` is the word `(t,u,v) = (4C,u,B)` with `4 | t`, a
  certificate word, so the native (★) classes are a subfamily of `𝔘_W`. ✓
* **Cor 2.5 is the right input.** `EXSET_BEYOND_CRT.md` Cor 2.5 gives `log(1/Eν) ≤ Cλ^{2/3}(log λ)^{2/3}` for **every
  majorant** of the whole avoider set of any finite mixture of certificate word classes and selector classes, with
  arbitrary moduli. `Eν` is the uniform mean over a common period, and the level is charged as in K2 (primes `> W`).
  This is precisely the primal bound the LP needs. The bias moment is under the same uniform `E_0`. So the integer
  word-universe version of LM is **covered**. ✓
* **The general form matches Thm 2.1.** "Square-avoiding base, inflated first-mass bound with parameters `d, γ`, and
  uniform weighted cofactor second moment" are Thm 2.1's (i), (ii)_{β,γ} and (iii), with LM's `d` = Thm 2.1's `β`.
  The note says "its exact hypotheses", which includes `β ≥ 1` and the W-uniformity in (iii). ✓ The notation clash is
  in F5.
* **The prime-unit word claim is correctly disclaimed.** Cor 2.5 itself says the (P) rerun is unchecked.
* **Not every ES₅/U method is covered.** As Cor 2.5's review-D8 scope says, LM covers majorants over the word *class*
  universe, not every method for U/ES₅. The note's "not every possible representation of that equation" matches this.
  ✓

Units (full ES): `PLcap` gives `S*(λ) = Cλ^{3/4}(log λ)^{3/4}` (reviewed), or `C(B)λ^{3/4}` with bounded `B`. The
moment (17) holds under unit Haar, where the signs are independent and symmetric. Masses `1/φ(Q)` on unit classes follow
because the period includes every prime `≤ N^{A_0}`. ✓ The note says "with the qualifications of §13" but never writes
`F = S*` for units (F4).

### 3.4 Weighted law vs. integer interval `O(1)` counts, and the existing sieve-limits note

The scope paragraphs are the strongest part of §16, and I agree with them:
* LM is a positive measure on residues, not an `N`-point set and not supported on `[1,N]`.
* Its marginals are expectations.
* For `A_0 > 1`, classes mod `Q > N` have true count 0 or 1 on `[1,N]`. Both the law (`N/Q < 1`) and the integers
  satisfy a position-blind `O(1)` count, so LM refutes only implications whose premises are such position-blind counts
  or exact marginals.
* Any argument using position, integrality, or correlations of the rounding errors is untouched.
* The note explicitly declines "the unrestricted assertion about every argument on `[1,N]` using interval counts". That
  is correct, because nothing in an LP comparison yields it.

**F7 (missing cross-reference, not an error).** The sieve-limits note already contains the integer-interval
*evaluation* results:
* (eq:transfer), `Σ_{n≤N}ν = N·Eν + O(Σ|a_i|)`;
* architecture (A2);
* `EXSET_BEYOND_CRT` Cor 2.5 (M2): IF Thm 2.2 `Σ_{n≤N}ν ≥ (N−D)Eν` for moduli `≤ N/2`;
* `thm:LScap` and `thm:hybrid` for the large-sieve, hybrid and fibrewise integer methods.

These are what cap actual **integer** majorant evaluations. §16 should say in one sentence that integer-interval
methods of the *majorant/large-sieve* type are already capped there, and that LM adds only the "arbitrary-law"
counter-model. Without it, a reader of "we do not claim the unrestricted assertion … on `[1,N]`" may infer that *no*
integer-interval barrier exists. That would understate the existing internal results.

**The Janson / FKG sentences.**
* "If all its premises are logical consequences of these marginals" is the correct qualifier. Janson's product-space and
  dependency-graph premise is *not* such a consequence: `μ` is not a product measure, although `E_0` is.
* The FKG sentence ("not a theorem that applies below a modulus cutoff and stops above it") is a rebuttal to an argument
  that does not appear in the note. As written it is cryptic; rewrite or delete (F6).

## 4. Revised §0

* **Result.** Accurate. It no longer front-loads QB, and it names ST and LM as delimitations, not results about ES. ✓
* **Label.** It is complete for P/PP, QB/QR (ineffective in both forms), Montgomery, and the method results.
  **F8:** Theorem Q (§7, CONDITIONAL on Dirichlet GRH, superseded by QB-GRH) and Lemma 5 (BV) lost their §0 labels in the
  rewrite. Both are still stated in the body. Add a half-line: "Q (§7) CONDITIONAL on GRH, superseded; Lemma 5 rel. BV."
* **Scope.**
  * "No change to the ambient 3/4" ✓.
  * "neither bounded cap nor ES follows" ✓.
  * "Counts exceptional integer arguments `j` with `F(j)>0` … not relative to prime values `F(j)`" ✓. This is consistent
    with P's prime-value word tail being an absolute count.
  * The phrase "the cap bounds allow an odd-square reduced denominator for rational `z`, without imposing a height limit
    on `qb` or the denominators" is accurate but clumsy. Suggest: "The relaxation and the packets impose no height limit
    on `b`, `qb` or den `z`."
* **Review.** Accurate, and "§§15–16 cross-review owed" is correct before this file. After this review, replace it with
  this file's pointer.
* **Triage.** RECORD (P, QR) and BARRIER-SCOPED (ST, common exponent, LM). Explicitly not BARRIER-BROAD. **Agree.**
  Suggested placement: ST goes as one FRONTIER §6 line merged with the §12 common-exponent line (same root cause:
  `r−1 | L` with polylog `L` gives too few cofactor windows). LM is merged into the existing UB/whole-avoider §6 line;
  it is not a new line.

**STATUS delta.**
* **§1A text.** It matches Theorem P and Corollary PP (coefficient ceiling, `H e^{−c_d(log H)^{3/4}}`, the prime-argument
  population hypothesis, word tails, priority unverified). ✓
* **§1B text.** The QR form `exp(o(log U log₃U/log₂U))` is a correct rendering of "for every fixed `c > 0`" in (14). The
  Montgomery form `(log₃R)^{2+ε}` matches "for each `C > 2`". ✓

**F9** (STATUS delta form; orchestrator should apply at export):
* (a) Say explicitly "drop the CONDITIONAL `(2√2+o(1))√(log₂R log₃R)` clause (superseded by QR-GRH)". "Replacement cap
  clause" does not say what it replaces.
* (b) Add a file pointer `notes/z80/BEYOND_34.md` §§10–12 plus the review files, as AGENTS §3 requires. The §1A clause
  also needs the z80 pointer beside z79's.
* (c) Add QB2 fix 5's clause "(no height limit on `qb` or den `z`)". Otherwise STATUS readers may see a conflict with
  `EXPONENT_CAP.md` Thm 2.1.
* (d) Name the Montgomery hypothesis ("weak per-class Montgomery conjecture, §12"), not just "§12 Montgomery".

**F10 (cap risk).** The current §1B capped-relaxation item is already 6 lines (STATUS l. 83–88). The proposed clause is
longer than the `2√2` clause it replaces. Compress, for example by moving "ES ⟺ `e* = 0`" and the CAP_DOWN B2 remark
onto one line, or the 6-line cap is violated.

## 5. Form

* **Overstatement (F3).** "In particular a full new binary basis … is impossible here" should read "fails for all but a
  relative `o(1)` of the profile primes (along the clean sequence)". ST is a most-`R` statement on a thin profile, not
  an impossibility for every `R`.
* **Confusing parenthesis (F3).** "do not justify a statement that any fixed number of large pivot slots (however large
  a fixed number is requested) can always be planted" can be read as "every fixed `t` fails", which is false for small
  `t`. Replace with: "for `t ≥ 5D+10` large slots, planting fails on most of the profile; nothing is said for smaller
  `t`."
* **Labels.** "(Assessment with the implication from ST proved)" is awkward. Use: "(Assessment; the deduction from ST
  is PROVED)".
* **F4 wording.** "Subtract this bad mass without conditioning the law" reads as if mass is removed from `μ`, which would
  destroy the exact marginals. Replace with: "We do not modify `μ`; we only bound `μ(𝒜∩\{|S|<ηm\}) ≥ μ(𝒜) − μ(|S|≥ηm)`."
  Also define `c_A = (A−1)/(2A)` from (17), which is currently undefined. Also state `F = S*(λ)` for units.
* **F5 notation.**
  * LM's `d` (supply exponent) clashes with P's degree `d` and with Thm 2.1(iii)'s `(log W)^d`. Use `β`.
  * `C` in ST (`L ≤ U^C`) coexists with §11's `C` (renamed `C_1` here, which is fine) and with unnamed constants.
  * `A` (§13 bias exponent), `A = 10000` (§10) and `A_0` (LM) all coexist. A one-line notation reset for §§15–16 would
    help.
* **F6 wording.**
  * The §16 heading says "removing an exceptional population". In this campaign "exceptional" means ES failures, but the
    removed set is the *biased* population. Retitle.
  * Add a clause that LM is specific to the polylog bias primes of §13 (§3.2 item 3 above).
  * Rewrite or delete the FKG sentence.
  * "the requested unrestricted assertion" is process language ("requested" by whom?). Use "the unrestricted assertion".
* **F11 (process).** The §0 Review line and the §11 CERTIFIED block cite files that exist only on
  `side-agent/z80-xrev-qb`. The pointers dangle until that branch is merged, so the merge should precede or accompany
  the export.

## 6. Debate and challenge

* **Is ST worth its space?** Mathematically it is a first-moment count. Polylog `L` leaves only `e^{O(U)}` windows `qb`,
  each large slot costs `e^{−U/2}` on a profile with no small nonresidues, and `t > 4D` slots therefore cost more than
  the window budget. The Landau–Page subsequence and the TZ profile count are the only nontrivial ingredients, and both
  are handled correctly. The value is real but narrow. It shows that the obvious "make `L` polylog and plant only the
  needed digits" upgrade of QB cannot reach a `(log U)^{O(1)}` log-cap pointwise, *unless* it uses small generators, few
  contacts or another cofactor mechanism. That is the right BARRIER-SCOPED size. It should not appear in STATUS, and the
  note proposes nothing for STATUS.
* **Is LM new?** Only marginally. It is `compmeas` without the normalisation, plus §13's bias moment. The correct
  reading is "consolidation". It records that one law has *exact* simultaneous marginals at every polynomial level and
  essentially the full balanced-avoider mass. Its use is as a ready counter-model against proposals that derive a void
  bound from marginal data alone (Bonferroni, factorial moments, cumulant expansions). The note says this. I would not
  give LM a FRONTIER §3 entry.
* **Could LM be over-read as a barrier for interval methods?** The text defends against this adequately. The residual
  risk is the omission in F7 (existing integer-interval caps not cross-referenced).
* **Hidden gap hunt in LM.** I looked for three failure points:
  * whether `noBcap` tolerates an enlarged period: it does, being a statement on `ℤ`;
  * whether `B`'s monomials with repeated primes leave `V`: they do not, since `(n/s)²` is a class function;
  * whether the unit version's `E_0` differs from `PLcap`'s `E*`: both are uniform on units of a common period.

  None fails.
* **Hidden gap hunt in ST.** I looked for four failure points:
  * the gcd case: it is empty;
  * BT uniformity at modulus `T^{o(1)}`: fine;
  * whether TZ's exceptional-zero strip constant must equal the clean constant `c`: it need not, since
    `(1−β) log T ≥ c log Z` suffices;
  * whether `t`-subset counting is affordable for `t ≍ U`: it is, since `U^{Dt} = e^{O(U log U)}` against the
    `e^{−tU/2} = e^{−Θ(U²)}` slot cost.

  None fails. The binding restrictions are the *hypotheses*: squarefree `b`, `r−1 | L`, `v > w`, `q > w`. They are all
  stated.

## 7. Required fixes (summary)

| # | where | type | fix |
|---|---|---|---|
| F1 | §15 Assessment | scope | The profile makes all `v ≤ w` divisibilities deterministic (`v | 1+qb`). Say that ST is silent on small-generator schemes on its own profile. |
| F2 | §15 | scope | State that a thin profile suffices *because* QB/QR-type bounds are pointwise in `R`. Give its relative density `exp(−(1/3+o(1))√log T)`. |
| F3 | §15 Assessment | wording | "impossible here" → "fails on all but `o(1)` of the profile"; fix the "however large" parenthesis; fix the label. |
| F4 | §16 proof | wording | "Subtract this bad mass" → lower-bound statement; define `c_A = (A−1)/(2A)`; state `F = S*(λ)` for units. |
| F5 | §16 | notation | `d` → `β` for the supply exponent; add a notation reset for `A, A_0, C`. |
| F6 | §16 | wording | Retitle ("biased", not "exceptional"); note LM is tied to polylog bias primes; fix the FKG sentence; drop "requested". |
| F7 | §16 scope | cross-ref | Point to (eq:transfer)/(A2), IF Thm 2.2 (M2), `thm:LScap`, `thm:hybrid` as the existing integer-interval caps. |
| F8 | §0 Label | completeness | Restore the labels for Q (§7, GRH, superseded) and Lemma 5. |
| F9 | §0 STATUS delta | form | Explicitly drop the `2√2` clause; add file and review pointers; add the "no height limit on `qb`/den `z`" clause; name the Montgomery hypothesis. |
| F10 | STATUS export | cap | The §1B item is already 6 lines. Compress at export. |
| F11 | §0, §11 | process | Merge `side-agent/z80-xrev-qb` with or before the export so that the QB2 pointers resolve. |

None of these is mathematical. After F1–F11, ST and LM are acceptable as BARRIER-SCOPED results:
* ST is PROVED rel. PNT/Chebyshev, BT, Landau–Page, TZ Thm 1.4 and the classical divisor bound.
* LM is PROVED rel. finite LP duality, `noBcap`, `EXSET_BEYOND_CRT` Thm 2.1/Cor 2.5 and `PLcap`. Those are internal and
  unrefereed, and Case A is rel. the Elsholtz–Tao inputs.

The QB2 fixes are in place, except for the STATUS-delta half of fix 5.

**Bottom line.** §§15–16 are correct and correctly scoped. They delimit two specific routes:
* planting `≥ t` large slots at polylog `L` with squarefree `r−1|L` cofactors (ST);
* arguments that use only low-level marginal data (LM).

They are neither a universal single-target impossibility nor a barrier for integer-interval or non-CRT arguments, and
the note says so. They do not touch the ambient 3/4, ES, cap zero or a bounded cap.
