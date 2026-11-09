# Hostile cross-model review — PC2

**Verdict: ACCEPT-WITH-FIXES (minor hypothesis clarification; no central mathematical gap found).**
Reviewed `side-agent/z68-pc2` at `0ed54edcdf4a7cf16ac627cd4a654f2784b51935`, not an earlier draft.
**ES is OPEN. Provider/auth/quota errors: NONE.** No merge performed.

## Per-claim audit

| Claim | Classification | Hostile finding |
|---|---|---|
| Theorem A: all seven family classes, two Q-shapes | CORRECT | Re-derived from literal ET Prop 1.9 and K11 Lemma M/Prop M′. Parameters outside the modulus remain unrestricted; family-specific S-free filters are essential and correctly implemented. I-3 needs its off-S root to be 1 and at most `2^ω(F)` on-S roots. |
| Lemma Q: uniform `Q(α,β) ≤ (αβ)^(2/5+o(1))` | CORRECT | All identities, eight determining quantities and four size cases check. The divisor arguments have polynomial size in αβ, even when the coefficients are extremely unbalanced. No coefficient-dependent hidden constant defeats uniformity. |
| Theorem E: count `N^(4/5+o(1))`, mass `N^(−1/5+o(1))` | CORRECT | Three-slot splits, seven-family/root multiplicities and NR conditioning all have the claimed cost. Uniformity is in N alone, not the ambient number of primes. |
| Theorem G / Cor G | CORRECT | Exact product law uses **pure** menus, not automatically the full single-prime menus. Denominators tend to 1 when both primes grow. The fixed-first-prime limit correctly assumes positive infinite-level survival and includes the finite-union upper-limit argument. |
| Cor K | CORRECT | Euler-product union bound gives survival `≥2−exp(2/5)>1/2`; PNT supplies the required large primes. Fixed-δ bounds imply `y^(1/5−o(1))` by slow diagonalisation. This restricts NR-count thresholds, not certificate support, and does not refute dense-profile PC. |
| Lemma P / square obstruction | CORRECT | Jacobi signs and reciprocity check family by family. The parity set cannot be empty for an actual event. Independent row audit finds no all-residue cylinder. |
| Lemma V: no integer threshold | CORRECT | Checked ET §2 maps and §10 formulas directly. All four core coordinates are positive integers for every positive member of the class; I-1's `te−a` is positive because its numerator reduces to `n(4a²d+1)+f>0`. |
| Theorem B(i),(ii): PC → MF → exceptional-prime bound | CORRECT | `m<p` supplies coprimality, not an assumed `y<F(y)`. Reciprocity and the classical classes dispose of exceptional primes outside `p≡1 mod 8`; the prime 2 then contributes no NR. EXSET Cor 5.4 applies. |
| Theorem B(iii),(iv): GRH strength and c-regimes | CORRECT-WITH-FIX | The cited LO estimate and `A>2` threshold are correct under GRH for `ζ_Q(√p)`. The opening L-function-only hypothesis is not identical to that hypothesis; clarify as below. Power laws on either side of 1/2 and the logarithmic boundary example are correctly scoped. |
| Theorem B(v): modulus lower bound / input limitation | CORRECT | Dense NR sets in `(cy,y]`, `0<c<1/2+η`, force `F(y)>cy`. The unconditional large-y input is explicitly an input limitation, not a general impossibility theorem. |
| CERTIFIED finite boxes / named classes | CORRECT | All four full rebuilds and literal modulus-10⁶ comparisons agree; independent bitmask audit confirms `146/23256`, `15/4290`, and `98/47190`. Both named classes recovered with actual II-3 parameters. |
| EVIDENCE trends / “park fable-3” / labels | CORRECT | Finite ratios are not infinite-level ratios. Nonexistence of a uniform fixed survival-ratio improvement is proved; useful many-component effects are not ruled out. Parking is honestly Assessment. The gate was delivered; dense-profile PC remains open. |

## Decisive proof details

Write `H=αβ` with positive integer coefficients. The identities are
`ZE=αX+βY`, `XP=βY+Z`, `YR=αX+Z`,
`EP=α+4βY²W`, `ER=β+4αX²W`, `PR=H+4Z²W`.
Every chosen divisor or ordered three-factorisation determines at most one remaining solution.
For pair product ≤T, squared monomials such as `Y²W` are ≤T², not an uncontrolled power of a free coordinate.
Since `(α+1)(β+1)≤4H`, the advertised M is `O(H^(9/5))`.
Thus `max_{m≤M} τ₃(m)=H^o(1)` uniformly; the six pair counts contribute only `O(T log T)`.
In case A1, `P²(XY)(YW)(XW)≤(4α/3)²`; in A2, `P²(XZ)(ZW)(XW)<(4H/3)²`.
These have **five factors counting P twice**, yielding 2/5, not an incorrectly inferred four-factor exponent.
The two reflected cases finish the cover. This is a valid extension of ET §3's Type-II argument, not an appeal to its prime-only normalisation.

For E, `αβ=NF` or `N²/D`, hence ≤N². The factor `(6+2^ω(N))τ₃(N)` is `N^o(1)`.
An NR-compatible level-N cylinder has relative mass exactly `2^ω(N)/φ(N)`; unused coordinates contribute 1.
Summing `N^(−θ)` over two positive depths gives the stated geometric tails, with fixed-small-prime constants as written.
For both primes large, `s_i^pure≥1−2ℓ_i^(−θ)`, so Γ is negligible **relative** to their product.
For fixed ℓ₁, positivity of `s_ℓ₁^U` is indispensable; finite-level positivity at 17 or 19 does not certify it.
The finite approximation of the single-prime caught union proves `s₁^pure(ℓ₂)→s_ℓ₁^U`, supplying the missing direction that a liminf alone would not give.

LO Thm 1.1 has an absolute constant and assumes GRH for the **Dedekind zeta function**.
For `L=Q(√p)`, `p≡1 mod 4`, it gives error `O(√y log(py²)+log p)`.
Relative to `y/log y`, the relevant error is `O(log p·log y/√y+(log y)²/√y)`.
This verifies `A>2`, the general criterion, and `y=(log p)²(log log p)³` for `log F(y)=√y/(log y)²`.
For `1/2<c<1`, the displayed implication is unavailable, not disproved by a converse theorem; all admissible `A<1/c` still yield `X^(c+o(1))`.

## Replays and independent checks

All executed with `ulimit -v 6000000`, command timeouts ≤1800 seconds, and no more than two compute processes.
- `events.py selftest 60 60`: 0 mismatches; `qcheck.py 120 120`: passed, maximum ratio 5.662113910164856.
- Rebuilt all four lists: `(11,13)` boxes (2,2), (3,2), (2,3): **2509, 10188, 9312**; `(17,19)` (2,2): **4200**.
- Literal brute force with modulus ≤10⁶: **534, 1000, 840, 682**; zero missing, extra, or minimum-modulus mismatches.
- Rebuilt single-prime level-2 lists for 11,13,17,19 and reran both decisive `survive.py` cases: complete agreement.
- Independent reviewer script uses no lane imports; checks every row's primitivity, exact level, off-S congruence, residues, square obstruction, and computes survival via row bitmasks.
- It verifies **26,209 rows across overlapping lists**, not 26,209 globally distinct cylinders; survivors **15/4290**, **98/47190**, **140/55770**, **146/23256** respectively.
- Independent II-3 recovery: `(a,d,e)=(11,2,247)` gives `−1215 mod 21736`; `(8,33,11999)` gives `−20447 mod 12670944`.
- At (17,19), independent pure product **169/2907**, Γ **67/1292**, ratio **73/676≈0.1080**. At (11,13), pure product **8/143**, Γ **15/286**; the full single-prime level-2 denominator is zero and is correctly not used.
- `validity.py 300 3000 1`: **65,456** exact-rational positive-solution checks passed, all seven families represented.
- The level-(1,1) trend log was inspected, not independently regenerated in full; it is not needed for the proved negative survival-ratio result and remains EVIDENCE.

Sources inspected directly: ET PDF Prop 1.9, §§2,3,10; K11 Lemma M/Prop M′; EXSET §§5.1′–5.4; board final memo.
LO source downloaded and Thm 1.1 read: <https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf>.
Reviewer replay: `uv run python scripts/z68_xrev_pc2_audit.py /tmp/xrev_PC2` after rebuilding the four `replay_*` files there.

## Falsifier table audit

| Screen | Finding |
|---|---|
| F1 odd squares | Correct obstruction: unit square profiles are uncaught; diagonal squares have no NR primes (divisor primes give zero, not NR). All 26,209 replay rows pass the all-residue exclusion. |
| F2 12 numerator-8 zeros | Correctly not applicable: numerator-4 family counting supplies no numerator-8 positivity. Read the screen list; nothing asserts these zeros are eliminated. |
| F3 285 non-square composites | Correct primality dependence: `m<n` need not imply coprimality. A composite quadratic character does exist; the memo no longer denies this. No composite positivity conclusion follows. |
| F4 14 (★)-zeros / 38 𝔊*-zeros | Correctly not applicable to this counting/conditional-covering theorem. These are restricted-family zeros, not ES counterexamples; no assertion of catching them or “survives all four” is made. |

## Required fixes, priority order

1. **MINOR, B(iii): align the hypothesis with the invoked source.** Replace “GRH for `L(s,(·/p))` … (GRH for `ζ_Q(√p)`, i.e. RH and GRH for L)” by “GRH for `ζ_Q(√p)` (equivalently RH and GRH for the quadratic L-function)”. Alternatively provide a separate argument using only quadratic-L GRH. The existing invocation does not itself establish that weaker assumption. Global “GRH ⇒ eventual ES” and the c-regime conclusions are unaffected.
2. **MINOR exposition:** declare `α,β∈N` explicitly in Lemma Q and `0<δ<1/5` in Cor K, as already intended elsewhere. B(ii) can retain exactly η by explicitly noting `(2/p)=1` for remaining exceptional primes; its η/2 fallback also suffices for the exponent.

No retraction of A/Q/E/G/K/V or the certified numbers is required. Accept the reusable reduction and uniform tail after these precision fixes; accept parking only as the stated Assessment, not as a no-go theorem for dense many-prime PC.
