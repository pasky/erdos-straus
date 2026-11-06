# z60 hostile cross-model review — LOPEZT

**Verdict: ACCEPT-WITH-FIXES.** The two-branch equivalence and numerical headlines survive. This is an independently rederived, largely prior reformulation, **not pointwise progress on ES**, which remains open. The memo's “NOT PROVED; no HOT LEAD” conclusion is justified; a claim that whole constructive/analytic approaches are dead is not.

Snapshot: `side-agent/z60-lopezt` at `b52ce8a37e0edbf5a482540eb3c0481d4398ff48`, `Z60_LOPEZT.md`. No author files changed. All executions used `ulimit -v 4000000` and timeouts ≤900 seconds; largest audit allocation ≈200 MB. Author code was extracted into `/tmp/xrev_LOPEZT/`.

## Per-claim audit

| Claim | Classification | Derivation / defect |
|---|---|---|
| Lemmas 0.1–0.2: branch identities | CORRECT | BN: `4ykg=p+y+g`; dividing by `pykg` gives the three terms. B4: `p+g=4Y'(gk−1)`; the last two fractions sum to `g/[pY'(gk−1)]`. All denominators are positive. |
| Corrected branch labels | CORRECT | **B4 (`4∣y`) fails at 193, 2521, 66529; BN (`4∤y`) at the 14 star-zero primes.** Neither §0 nor §4 retains the kickoff swap. See independent checks below. |
| Lemma 0.3: complete Type II form | CORRECT | With `y'=da,z'=db,(a,b)=1`, set `h=4dab−a−b`. Since `(h,ab)=1`, `x=abx'`, `x'h=pd`. Then `p∤x'` forces `h=mp,d=mx'`, hence the stated formula. Conversely `p≥(4d'−2)ab≥2abd'` ensures `p∤x`. |
| Lemma 0.4: complete Type I form | CORRECT-WITH-FIX | Necessity and sufficiency hold; the written assertion `p∤4abw−1` is false, since `4abw−1=mp`. Replace it by `p∣4abw−1`, which implies `p∤abw`. The omitted necessity proof is supplied below. |
| U1–U4, T-form, axes interpretation | CORRECT-WITH-FIX | Expanding `(4ta−1)(4tb−1)` and `(4ta−1)(tb−1)` proves U3↔U4; factoring `p+a` or `p+4a` gives U1/U2. For BN restricted to `4∤a`, explicitly justify the enlargement: if `4∣a` in `p=4tab−a−b`, then `b` is odd, and swapping `a,b` supplies an allowed BN witness. |
| Lemma 0.5 / U5 Jacobi obstruction / odd squares | CORRECT | For `D≡−1 (4t)`, reciprocity gives `(t/D)=1` including its 2-part, so `tn≡−1` or `4tn≡−1` gives `(n/D)=−1`. Squares cannot satisfy this. This proves a necessary witness property, not a prescribed organization of every possible proof. |
| Lemma 1.1 / U5 / P* | CORRECT | Let `Q=(g+1)/4`. BN is `p≡−a`, `a∣Q`. B4 is `p≡−4a`; writing `t=Q/a` gives `p⁻¹≡−t`, `t∣Q`. Thus `R_g⁻¹=−4Div(Q)`, and both U5 and the displayed P* are exact. Fixed-modulus BN here is explicitly the enlarged BN condition. |
| Witness bounds and numerator-8 form | CORRECT | BN: `g≤p+a≤p+(g+1)/K`, so `g≤(Kp+1)/(K−1)`. B4 analogue: `g∣tp+1`, cofactor `≡−1 (t)`; for `t≥2`, `g≤(tp+1)/(t−1)≤2p+1`, and `t=1` gives `g≤p+1`. These bounds apply to `K=4,8`. U5 with `K=8` implies U5 with `K=4`. |
| “Sharpened F2” and §3.4 2-adic slack | CORRECT-WITH-FIX | Correct with the **divisor of `−p` or `−p⁻¹` in U5**. It is false if the same test is applied to P*'s second-branch divisor `−p·4⁻¹`; the coordinates differ. Explicit counterexample and repair below. |
| Lemmas 1.2 and Prop. 3.1 | CORRECT | `p≡1 (L)` defeats every bounded modulus; Dirichlet gives infinitely many primes. `log L≤(1+o(1))M`, and Xylouris gives a prime ≤`C L⁵`, hence `g*(p)≥(1/5−o(1))log p` along an unbounded sequence. See primary-source check below. |
| Lemmas 2.1–2.2; full residue set | CORRECT | Type II: `mp+a=b(4amd'−1)` and `m∣a+b`. Dividing `a,m` by their gcd preserves divisibility since that gcd is coprime to `g`. Full residues are `−a/m`, `am∣Q`. Type I: multiplying `a+b` by `4aw` proves `m∣a+b` from the two divisibilities, and conversely. |
| 105 off-axis; 4545 no algebraic Type II witness | CORRECT-WITH-FIX | `(a,m,g)=(3,2,71)` works at 105. The 4545 negative search is reproducible and complete with a repaired bound. The claimed general bound `a≤n/4+1` is false: `n=73,a=21,m=2,g=167` is a witness. Use the bounds below; distinguish the algebraic composite extension from ET's coprimality definition. |
| U6 and U7 | CORRECT | In `p=kab−a−b`, the unit-fraction integrality conditions are `4∣k` or `4∣a` or `4∣b` for odd p. For U7, put `d=ak−1`; when `a≡1,2`, only `4∣k` survives; when `a≡3`, `4∣k` implies `4∣b`, leaving exactly `d∣(p+a)/4`. When `a≡0`, the original B4 condition remains. |
| C2: witnesses `g>p` for `p≡1 (8)` | CORRECT | BN forces `g=p+a` and `(p+1)/a≡3 (4)`. B4 with `t≥2` would require `4(t−1)∣p+1`, impossible; `t=1` is also impossible. Thus the stated prime-factor criterion follows. This does not prove every imaginable explicit formula is an axis construction. |
| §3.3 probability inequality / main-term constant | WRONG as displayed | At `g=15`, `Q=4`, `R_g∪R_g⁻¹={7,11,13,14}`, so probability `4/φ(15)=1/2 > 2τ(4)/15=2/5`. The valid upper bound has `φ(g)` in its denominator, not `g`. The asserted constants do not follow. |
| Remaining C1–C5 / counting-route conclusions | CORRECT only as scoped assessments | Bounded-witness no-covering is proved. Sparse target sets and subgroup obstructions are valid. “Circular,” “at best almost-all,” “nothing easier than ES,” and claims about all formula/main-term methods are not impossibility theorems. Keep the verdict inconclusive, not dead. |

### Proof details / required algebra repairs

Type I necessity: write `x=da,y=db,(a,b)=1`, with `p∤dab`. The equation becomes `(4dab−p(a+b))z'=dab`. Its parenthesis is coprime to `ab`, so `z'=abw`; consequently `d=w d'` and `d'(4abw−1)=p(a+b)`. Since `p∤d'`, set `4abw−1=mp`; then `a+b=d'm`. Conversely the identity holds and `0<d'=p(a+b)/(4abw−1)<p`, proving genuine Type I for primes. The alternate `c∣4a²w+1`, `4aw∣p+c` form follows by taking `m=(4a²w+1)/c`.

Complete Type II search bound: `4amk−1≤mn+a` gives `a≤(mn+1)/(4m−1)≤(n+1)/3`. Also `g∣n+4a²k`, so `m≤a+(n+1)/(4ak)≤7(n+1)/12<n+1` for `n>1`. The author's `m≤n+1` enumeration therefore suffices despite the incorrect bound in the prose.

**2-adic coordinate counterexample:** `p=83449`, an S8-zero, has B4 witness `g=679`, `Q4=170`, P* divisor `a=(−p·4⁻¹ mod g)=17`. Yet `17∣Q8=85` and `g≡7 (8)`. Thus §3.4's slack description is not correct in those coordinates. U5's inverse divisor is instead `t=Q4/a=10`, which does not divide 85. Fix: use U5's divisor consistently; or in P* coordinates, for `g≡7 (8)`, non-liftability means `v₂(a)=v₂(Q4)` on BN, but **a odd on B4**. The numerator-8 P* also replaces `4⁻¹` by `8⁻¹`, not just Q and the modulus progression.

## Numerical verification

Independent auditor: `scripts/z60_xrev_lopezt_check.c`; screen driver: `scripts/z60_xrev_lopezt_screens.py`. Census enumerates the actual shifted-number factors `n=(Kat−1)b−a` and `n=(Kat−1)b−Ka`, not modular-inverse queries. The bounds above make it exhaustive. Single-number star enumeration splits `a≤b` into `t≥b`, `a≤t<b`, `t<a`; direct enumeration agrees for all odd `n<1000`.

| Check | Outcome |
|---|---|
| Independent `census 200000 4` | BN prime zeros `409,577,5569,9601,23929,83449,102001`; B4 zeros `193,2521,66529`; no union prime zero; non-square union zeros exactly `105,4545`; every odd square in range has no witness. |
| Independent `census 100000000 8` | **Exactly 45 union-zero primes `≡1 (4)`, last 3869153**. The complete list equals the author's 45-entry file. Individual branches have 1270 and 258 prime zeros. This independently extends the author's executable rerun range from 4·10⁶ to the brief's 10⁸. |
| Author U5, numerator 8 through 4·10⁶ | Output byte-identical to `s8_zeros_le4e6.txt`. |
| Author least-g census through 10⁸ | Output byte-identical to `leastg_1e8.txt`: 719781 primes `≡1 (24)`; record `g*=10487` at 9658489; `g*=7`: 50.0587%; `g*≤23`: 90.1207%; 172 above 1000, 12 above 3000. All quoted rounded figures agree. |
| Author U7 versus U5 through 20000 | Zero lists identical. |
| Author `typecheck.py` | 0 reported mismatches for primes below 700; returns `(3,2,71)` at 105 and no Type II witness at 4545. Its Type I search has a heuristic cap, so this is a consistency check, not an independent classification proof. |
| Author `branches.c` through 200000 | Matches the independent exact lists, **but contains a heuristic early break** after `y>4√n+100` once either branch hits. Remove it or prove completeness before calling this program a certifier. |

Reproduction (each executable run with the resource limits stated above): compile the auditor with `gcc -O2 -Wall -Wextra`; run `selftest`, `census 200000 4`, `census 100000000 8`; then `uv run scripts/z60_xrev_lopezt_screens.py /path/to/auditor`. No ≥10¹⁰ global census was rerun; those ranges are inherited prior results, not this review's certifications.

## Mandatory falsifiers

| Screen | Independently checked behavior | Memo adequacy |
|---|---|---|
| F1 odd squares | Empty by Jacobi proof; independent census confirms through 200000. | Correct. |
| F2 twelve C-even / R8-zero primes in `[10¹⁰,1.1·10¹⁰]` | Full enumeration gives ordered R counts `56,52,30,42,12,28,66,58,30,66,18,52`, with R8=0 throughout. **All twelve have both B4 and numerator-8 B4-analogue witnesses.** The latter moduli, in file order, are `1479,159,2239,111,11087,143,447,143,15,1663,39,31`. | **Missing:** the memo substitutes the separate 45-zero S8-union census. These are different tests, not interchangeable. Add this row; the twelve refute the C-even star sub-line, not S8 or full Type II. |
| F3 285 non-square composite star zeros | All 285 have BN count zero; **283 are rescued by B4**, with exactly `105,4545` remaining. | The two exceptional integers are correct, but the mandatory 285-object behavior is omitted. |
| F4 14 star-zero and 38 G*-zero primes | All 14 are rescued by B4; all 38 have B4 witnesses, and exactly 24 also have BN witnesses. Complete star counts reproduce precisely the 14-element zero subset. | Correct branch lists, but the 38-object screen is omitted. |

## Prior work and citations

- **U5 and its inversion symmetry are explicitly prior**, not merely similar: `Z59_CONV2.md` Lemma 1(vi) states `−n∈D_f` for c=1 and `−n∈D_f⁻¹=4D_f` for a=1, with exactly the same divisor set. It also gives the full ratio set. Lemma 1(iii–iv) already gives both piecewise T/shift profiles; Proposition 3.1 gives branch domination.
- `Z59_CONV2.md` §0 already gives **45 S8-union zeros for primes ≡1 (4) through 10⁸**, and **61** over all odd primes (16 more ≡3 (4)); the domain restriction must stay explicit. It already records the 285/12/38 screen behavior and `{105,4545}` through 10¹⁰. Thus the present 45-zero rerun is verification, not a discovery.
- `B1_LINE.md` §§0–2 credits López for Type A/B, branch divisor identities, the three B4 exceptions and the union conjecture; its B4 census already reaches 10¹¹. Lemma 1.1 supplies the B4 part of U6. `CLASS_FORCING.md` §1 already has both `p+4d` and `cp+1` lines; its distinction between character information and divisor classes predates this memo.
- `Z58_CONVF.md` Lemmas 1.1–1.4 already give the full Type II divisor forms, both axes, Jacobi obstruction and no-finite-covering theorem, with explicit attribution to Elsholtz–Tao and López. Type I/II classification is standard, not newly discovered here. U7 is a useful case-split presentation; the least-g census is the clearest incremental numerical deliverable found in this audit.
- Primary citation checked: Xylouris, *Über die Nullstellen der Dirichletschen L-Funktionen und die kleinste Primzahl in einer arithmetischen Progression*, BMS 404 (2011), **Theorem 2.1**, [PDF](https://bib.math.uni-bonn.de/downloads/bms/BMS-404.pdf), states `P(q)≪q⁵` with an effective constant. Its §2 definition takes the maximum least prime over reduced classes. This validates Proposition 3.1's exponent; the hidden multiplicative constant is absorbed by `o(1)`. Graham–Ringrose/GRH remarks are not premises of the verdict and were not independently source-certified here.

## Required fixes, priority order

1. Distinguish U5's inverse divisor from P*'s shift divisor in the numerator-8/slack claims; include the 83449 counterexample and the correct branch-dependent condition.
2. Replace the false `φ(g)`-to-`g` probability inequality and withdraw its unsupported constants; keep log-squared behavior heuristic and prime-progression conditioning explicit.
3. Add the actual F2/F3/F4 screen rows above. Keep the 45-zero S8-union census as an additional test, not a substitute.
4. Attribute U5, the branch identities, axes, obstruction, union conjecture and prior censuses explicitly. “Unprimed” is not novelty evidence.
5. Fix the Type I divisibility typo and Type II search bound; justify the restricted/enlarged BN equivalence. Remove the branch code's heuristic cutoff before claiming it certifies absences.
6. Mark C2–C5/counting-method pessimism as scoped assessments. The valid fixed-modulus obstruction does not kill growing witnesses, all explicit constructions, or all pointwise methods.

**Final assessment:** accept the corrected identities and reproducible census as a useful audit/reformulation. The pointwise target remains inconclusive; no new positivity mechanism or ES proof is established.
