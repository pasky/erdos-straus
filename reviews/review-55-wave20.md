# Wave-20 hostile review: §55 general-numerator tails and effectivity

**Base reviewed:** `f1e7d56`.  **Overall verdict:** **SOUND-AFTER-REPAIRS**, in the section's stated internal, status-preserving sense.  The maximum-severity assertion survives: when the Page conductor divides `m`, modulus deletion is vacuous, but favorable-residue selection retains enough aggregate multiplier mass for the full Layer-1 family and the structured c-free fibres.  It does **not** work for arbitrary sparse multiplier subfamilies.  The original text eventually said that, but Lemma 55.4's opening quantifiers were broader and its structured-fibre subtraction and unfavorable `k=1` case were not explicit.  Those overclaim risks are repaired.

This verdict does not upgrade §39, Theorem 34.8, Provisional Theorem 43.7, or Theorem 43.12.  The cubic chain remains **CLAIMED/PROVISIONAL**.  I replayed §55's reductions into those inputs; I did not re-prove their inherited maximum-severity analytic claims.

## Claim verdicts

| Claim | Verdict | Hostile finding |
|---|---|---|
| `W_m(p)` and the `m=4` specialization | **CONFIRMED** | `(55.2)–(55.3)` are Lemma 43.1's exact data.  Since `((kℓ+1)/m,kℓ)=1`, `v` is invertible modulo `kℓ`, so `pv≡-u` is exactly §51's `p≡-uv^{-1}`.  At `m=4`, `kℓ≡-1 (mod 4)` is `(51.2)` with no primality requirement on `ℓ`; see `notes.md:20365-20384`. |
| Layer-1 truncated assembly and tail | **CONFIRMED-AFTER-REPAIR (applied)** | The mass is `M_1=λ_m t² log K`, the degree is `O(1+M_1)`, and the ledger is `O_B(t(1+M_1))`.  The original displayed sets were corrupted to `p { / m prime}` and did not state a predicate.  Prime scope is restored at `notes.md:20396-20418` and `20460-20483`.  The result retains §39's review qualification. |
| Thinned-cubic truncated assembly and tail | **CONFIRMED, STATUS-PRESERVING** | The mass is `M_2=θ_m t³`; `(43.27)` supplies the moment base, `(43.36)–(43.38)` the relative void, and `(43.39)` the `O(M_2t)` ledger.  No inverse power of `θ_m` is silently introduced.  This remains **CLAIMED/PROVISIONAL** through Theorems 34.8 and 43.7. |
| Uniform `(m,T)` windows | **CONFIRMED** | With `t=log X` and `X` a fixed power of `T`, `m≤t^B` is exactly `m≤(log T)^B` up to constants.  `K=t^{D(B)}` or `K=X^κ` satisfies `KX≤T`; the conditions become `log N≥C_B{log T+(log T)M_i}`.  The sign repair's extra `K≥m^D` is met uniformly by both choices. |
| Top-of-window recovery | **CONFIRMED** | From `L=log N≈θ_m s^4`, `s=log T≈(L/θ_m)^{1/4}` and `θ_m s³=θ_m^{1/4}L^{3/4}`, exactly `(43.35)`.  In `m≤L^{3-ε}`, the extra `s` term has ratio `s/L≪L^{-ε/4}`.  The Layer-1 balance similarly recovers `(43.13)` and its `m≤L^{2-ε}` fixed-gap range.  No range extension occurs. |
| `r∤m` Page case | **CONFIRMED** | Some prime `a` has `v_a(r)>v_a(m)`.  Imposing `a∤uv` forces `v_a(muv)<v_a(r)`, hence `r∤muv`.  Lemma 51.5's local mass retention is pointwise in `k`, including shared-but-incomplete conductor factors. |
| `r∣m`: every BV modulus contains `r` | **CONFIRMED** | The prime progression is literally `ℓ≡-k^{-1} (mod muv)`, not modulo `uv` or an lcm; this is `(43.12)`.  Thus `r∣m` implies `r∣muv` for every triple and excluded-conductor deletion removes the entire supply. |
| `r∣m`: favorable-sign retention | **CONFIRMED-AFTER-REPAIR (applied; maximum severity)** | From `(55.15)`, `ψ=main-χ_r(a)y^β/(βφ(q))+error`, and `a=-k^{-1}`.  Therefore `χ_r(-k^{-1})=-1` is genuinely favorable.  The repaired proof first gets `h(F_r)≥cH_m(K)` and then uses the adversarially safe subtraction `h(F_r∩J_c)≥(c-Z(c))H_m(K)`; see `(55.17a)–(55.17b)`, `notes.md:20626-20658`.  It now expressly excludes arbitrary sparse `J` and handles an unfavorable formal `k=1` without putting its progression into the BV lower sum. |
| Displayed-exceptional-term BV `(55.15)` | **CONFIRMED AT THE STATED DEPENDENCY-PROOF LEVEL** | Lenstra–Pomerance Lemma 11.2 directly prints the excluded-conductor form, not `(55.15)`.  Their character decomposition isolates the unique induced exceptional character; retaining its `-χ_r(a)y^β/β` term and applying the effective estimate to all other primitive characters gives the displayed variant.  §55 accurately says this is a dependency proof rather than a verbatim citation. |
| Effectivity perimeter `(55.18)` | **CONFIRMED-AFTER-REPAIR (applied)** | The repaired aggregate scope is exactly what the Layer-1 and c-free tails use.  At Theorem 43.12's full fixed-gap top, `K=e^{κt}≫m^D`, `M_2≫L^{ε/4}`, the ledger is effective, and the existing effective semigroup transfer applies.  The table correctly withholds effectivity from the ancillary all-triples absolute-error clause.  Two wrong §55.3 effectivity pointers now point to §55.2. |
| PW comparison and crossovers | **CONFIRMED-AFTER-REPAIR (applied)** | Relative truncated masses are exactly `η_1(m)log log T` and `η_2(m)log T`.  The old wording could suggest a below-crossover regime inside the theorem's uniform range; eventually none exists for fixed `B`.  The clarification at `notes.md:20709-20729` separates the unrestricted formal crossover from `m≤(log T)^B`, retains unknown-constant caution, and preserves PW's proved-status advantage. |
| Computational `(bb)` | **CONFIRMED-AFTER-REPAIR (applied)** | Harvest counts, intrinsic classes, `m=4` agreement, and exact `η_2` factors replay.  The old Page toy checked only existence of both signs.  It now also checks the relevant finite harmonic weight for `(m,r)=(5,5),(6,3)`; ratios are `0.431615` and `0.663543`.  It remains explicitly informational and does not purport to prove uniform retention. |
| Numbering, cross-references, and source hygiene | **CONFIRMED-AFTER-REPAIR (applied)** | Restored four eaten prime-scope displays and corrected two effectivity-section references.  `(43.4)`, `(43.7)`, `(43.12)`, `(51.1)`, Lemmas 51.4–51.5, and the `q=muv` reference all match.  Tags `(55.1)–(55.21)`, including new `(55.17a)–(55.17b)`, are unique.  No §54 reference occurs in §55; control-byte count is zero; `git diff --check` passes. |

## Maximum-severity sign replay

For a modulus `q` divisible by the primitive real conductor `r`, the exceptional contribution has the form

```text
ψ(y;q,a) = y/φ(q) - χ_r(a)y^β/(βφ(q)) + E_r(y;q,a).
```

In §43 the residue is `a=-k^{-1} (mod q)`.  Reduction modulo `r` therefore depends only on `k`, not on `u,v,w` or the denominator-side class.  Selecting `χ_r(-k^{-1})=-1` turns the exceptional term into a positive contribution.  Its magnitude need not be bounded: positivity of its sign is enough for the lower bound once the averaged remainder `E_r` is paid.

The dangerous issue is mass, not sign identification.  For an arbitrary sparse family the sign can be completely adversarial.  For example, with `r=3∣m=6`, all multipliers `k≡5 (mod 6)` have the unfavorable sign.  Adding the formally required `k=1` contributes only bounded harmonic mass and does not repair such a family.  Thus an arbitrary-`J` version of `(43.23)` is false as an effectivity claim obtainable by this argument.

The downstream families are different.  On the full coprime family, the induced nonprincipal character has equally many positive and negative unit classes modulo `m`.  Uniform dyadic counting gives favorable mass `≫η_1(m)` per interval once `Y≫m²`, and `K≥m^D` supplies `≫η_1(m)log K` in total.  For the structured fibre

```text
J_c = {k≤K : (k,m)=(k,c)=1},
```

no sign-independence assumption is needed.  Remove from the already balanced full favorable set every `k` divisible by a prime divisor of `c`.  Equation `(43.36)` bounds the entire removed mass for prime `p` by `H_m(K)/p`, even if every removed multiplier was favorable.  Hence

```text
h(F_r ∩ J_c) ≥ h(F_r) - Z(c)H_m(K) ≥ (c_1-Z(c))H_m(K).
```

The same Chernoff quarantine as `(43.37)`, with threshold below `c_1`, leaves a fixed fraction except on an `exp(-cM_2)` set of fibres.  This survives arbitrary correlation between the fibre deletion and the character sign.  Low-`ω` deletion can be made a smaller prescribed fraction, and low-congestion pruning is `o(1)` of the original mass, so both fit inside the retained fixed fraction.

### Concrete `r=3∣m=6` walk-through

The units modulo 6 are 1 and 5.

| `k mod 6` | `-k^{-1} mod 3` | `χ_3(-k^{-1})` | exceptional effect |
|---|---:|---:|---|
| 1 | 2 | -1 | adds to the main term |
| 5 | 1 | +1 | subtracts from the main term |

Every progression modulus is `q=6uv`, hence divisible by 3.  Excluded-modulus BV would retain none.  Favorable selection keeps the `k≡1 (mod 6)` half.  The finite `(bb)` harmonic ratio through `K=1500` is `0.663543`; its deviation from one half is a bounded-range effect and is not used in the proof.

### Is sign selection actually necessary?

An effective class-number lower bound and the standard relation between `L(1,χ_r)` and a real zero give, at the scale needed here,

```text
1-β ≫ 1/(sqrt(r) log²r),
x^(β-1) ≤ exp{-c log x/(sqrt(r)log²r)}.
```

Since every dyadic prime block has `log x≈t`, this directly makes the exceptional term negligible when, for example, `r≤m≤t^{2-δ}`.  That clean domination route can replace sign selection in that smaller regime.

It does **not** cover §55 as stated.  The truncated theorem permits arbitrary fixed `m≤t^B`; for `B≥2` the displayed bound need not tend to zero uniformly.  The full Theorem 43.12 window allows `m` close to its `L^{3-ε}` boundary, where `t/sqrt(m)` can even tend to zero.  The favorable-sign argument is therefore not decorative cover for a bound that already dominates the exceptional term: it is needed for the largest claimed ranges.

## Parameter and uniformity replay

Write `t=log X`, `L=log N`, `λ_m=η_1(m)/φ(m)≈1/m`, and `θ_m=η_2(m)/φ(m)≈1/m`.

### Layer 1

- Choose `X=T^{1/2}` and `K=t^{D(B)}`.  Then `KX≤T` for large `T` and `log K≈_B log t`.
- Lemma 43.3 supplies lower active mass `t²h/φ(m)` with `h≈η_1(m)log K`, hence `M_1≈λ_mt²log t`.
- The residue upper profile and factorial moments use `η_2` instead of `η_1`; their ratio is bounded above and below by absolute constants.
- Quarantine and even Bonferroni degree are `O(M_1)` when `M_1` grows and fixed when it is bounded.  Atom choice and modulus ledgers are `O_B(t(1+M_1))`, exactly the first condition in `(55.11)`.
- At the optimized top, `L≈λ_mt³log t`; this gives saving `λ_m^{1/3}L^{2/3}(log L)^{1/3}`.  If `m≤L^{2-ε}`, then `t=o(L)` and `m≤t^2` after a fixed-gap enlargement, matching `(43.13)`.

### Cubic chain

- Choose a fixed rescaling of `X` with `K=X^κ` and `KX≤T`.
- Theorem 43.7 supplies lower active mass comparable to `θ_mt³=M_2`; `(43.27)` bounds every factorial moment by `(CM_2)^j`.
- The quarantine and degree are `O(M_2)` and the exact ledger is `O_B(t(1+M_2))`; this is `(55.8)`.
- At the top, `L≈θ_mt^4`, `M_2≈θ_m^{1/4}L^{3/4}`, and `m≤L^{3-ε}` implies `M_2≫L^{ε/4}`.  This is exactly Theorem 43.12's nontrivial range.

### `θ_m→0` stress

Take the edge family `m≈t^B`.  Then

```text
M_1 ≈ t^(2-B) log t,
M_2 ≈ t^(3-B).
```

For `B>2` or `B>3`, respectively, the mass can be bounded or tend to zero.  The proof does not pretend otherwise: it uses fixed degree there, pays an explicit `t` ledger, and yields at most a constant-factor bound `N exp(-cM_i)`.  There is no hidden growing-saving assertion and no threshold depending on the particular `m`; `K=t^{D(B)}` in Layer 1 and `K=e^{κt}` in the cubic family both dominate `m^D` uniformly after a threshold depending only on the displayed fixed parameters.

## `m=4` degeneration

At `m=4`,

```text
η_1(4)=2/3,  λ_4=1/3,
η_2(4)=4/5,  θ_4=2/5.
```

These are fixed constants, so `(55.10)` has exactly §51's two exponent shapes.  More importantly, the object itself is literal, not merely comparable: `kℓ≡3 (mod 4)`, `((kℓ+1)/4)=uvw`, and `pv≡-u (mod kℓ)` are `(51.1)–(51.2)`.  Block `(bb)` reproduces every `(ax)` class set through modulus 1500 and the spot checks at 3, 7, and 23.  No claim of exact equality of unnamed asymptotic constants is made.

## PW comparison replay

PW's truncated `k=1` mass is `(log T)²/φ(m)`.  Dividing §55's masses by it gives exactly

```text
η_1(m) log log T,
η_2(m) log T.
```

At the optimized `N`-window, the ratio in `(43.34)` also recomputes:

```text
R/P = {η_2(m)^3 φ(m)L}^{1/12},
R≥P iff L≥1/(η_2(m)^3φ(m)).
```

The repaired paragraph is now honest about three different facts: PW is proved while the cubic side is provisional; unknown constants prevent a finite crossover; and the formal below-crossover region eventually lies outside §55's own fixed-power `m` window.

## Computational audit

Block `(bb)` was inspected line by line and rerun as part of the full suite.

- Harvesting enumerates every ordered factorization `uvw=(M+1)/m`, compares it with the intrinsic divisor-of-a-square description, and minimizes over every `M=kℓ≤1500` with `M≡-1 (mod m)`.
- The printed tail rows for `m=3,5,6,7`, the unresolved counts, and monotonicity checks match `(55.20)`.
- The `m=4` family equals the `(ax)` construction through 1500, including the three literal class sets.
- The `η_2` checks are exact local-factor algebra.  They are not an asymptotic test of Lemma 43.2, and §55 does not call them one.
- The Page toy verifies `q=5uv` for sampled valid atoms and sees both signs.  The added harmonic-weight check is closer to the actual retention statement and includes the requested `r=3∣m=6` case.  It is still only a finite shadow, as the text now says.
- Continuity-corrected fits are informational only and do not enter a verdict.

## Severity-ranked defects

1. **Maximum-severity overclaim risk, repaired — Lemma 55.4's original opening could be read as effectivizing all subfamilies in Lemma 43.3/Theorem 43.7.**  That is false for the sign method: an adversarial `J` can contain only `χ_r(-k^{-1})=+1`.  The lemma now states only the full Layer-1 family and structured c-free fibres (`notes.md:20581-20589`).
2. **Maximum-severity proof omission, repaired — favorable residue mass was asserted without the exact structured-fibre inequality.**  Balance in the full family alone does not imply balance after intersecting with `J_c`.  New `(55.17a)–(55.17b)` subtract the worst possible correlated deletion and close the Chernoff argument (`notes.md:20626-20650`).
3. **High, repaired — the formal `k=1` instruction could reintroduce an unfavorable exceptional progression.**  This happens concretely for `m=r=5`, where `χ_5(-1)=+1`.  The proof now uses `k=1` only for incidence bookkeeping and omits its triples from the lower BV sum when unfavorable (`notes.md:20651-20655`).
4. **Moderate, repaired — the PW crossover prose mixed an unrestricted formal comparison with the actual uniform window.**  The distinction is now explicit (`notes.md:20718-20729`).
5. **Moderate, repaired — `(bb)`'s Page shadow tested existence of signs, not retained harmonic mass.**  The new finite weighted checks cover `(5,5)` and `(6,3)` and remain correctly labelled non-asymptotic (`verify.py:9849-9883`, `notes.md:20768-20777`).
6. **Low but literal, repaired — four theorem displays had eaten prime scope.**  Before repair they were not meaningful set predicates.  All now say `p` is prime (`notes.md:20396-20418`, `20460-20483`).
7. **Low, repaired — two effectivity pointers named §55.3 instead of §55.2.**  Both now point to the conductor/effectivity subsection.

No unrepaired §55 defect remains.

## Overclaim and label scan

- `notes.md:20348-20354` correctly says truncation adds no range and effectivity does not upgrade correctness.
- Lemma 55.1 and the first tail are “proved internally” only with §39's review qualification.  They use no Theorem 34.8 or 43.7; this is accurate, not an unqualified external theorem label.
- Every cubic occurrence in Lemma 55.1, Theorem 55.2, Corollary 55.3, and `(55.18)` remains **CLAIMED/PROVISIONAL**.
- “Effective” consistently means computable constants and thresholds conditional on the existing correctness label.  It does not mean uniform arbitrary-`J` class mass or effective all-triples absolute error.
- `(55.15)` is not falsely attributed verbatim to Lenstra–Pomerance; the text identifies the exact printed excluded-conductor form and its own dependency derivation.
- Theorem 43.12's full fixed-gap row is honest: effectivity survives the full window, while correctness still inherits Theorems 34.8, 43.7, and §39.7.
- PW is identified as the proved benchmark; §55 makes only exponent-scale comparisons and no finite, pointwise, or priority claim.
- Computational 55.6 is consistently labelled exact finite/informational and does not claim asymptotic evidence.

## Validation and scope signature

**Replayed directly:** `W_m` algebra; the `X,T,K,t` dictionary; `λ_m,θ_m` mass thinning; Bonferroni degree and ledger; both top-window balances; `q=muv`; exceptional-term sign; the `r∤m` valuation deletion; full-family character balance; structured-fibre worst-case subtraction; the `r=3,m=6` case; `θ_m→0`; `m=4`; PW ratios; block `(bb)`; tags, cross-references, and source hygiene.

**Structural/inherited only:** the underlying residue-profile estimate in §39, Theorem 34.8's pruned supply, Provisional Theorem 43.7, the exact analytic proof of the standard displayed-exceptional-term BV variant beyond the checked character-decomposition dependency, and Theorem 43.12's semigroup transfer.  Their existing labels are preserved.

Validation command:

```text
uv run --with sympy,numpy,scipy python verify.py
```

The full suite passes in 81.48 seconds (333,732 KB maximum resident memory).  `git diff --check` passes; §55 has no control bytes and no accidental §54 reference.
