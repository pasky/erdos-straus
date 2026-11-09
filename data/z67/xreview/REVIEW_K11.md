# Hostile cross-model review — K11

**Verdict: ACCEPT-WITH-FIXES (major fixes required). π° is REFUTED; K̄ ∩ U remains undecided. ES is OPEN.**
Reviewed `side-agent/z67-k11` at `e2711b6ad`, `Z67_K11.md`; source checked: Elsholtz–Tao, Prop 1.9 (p. 8), §10 (pp. 37–38).
No provider/auth/quota error occurred. All numerical runs used `ulimit -v 6000000`, timeouts ≤1800 s, and at most two concurrent numerical workers.

## Per-claim findings

| Claim | Classification | Independent finding |
|---|---|---|
| Lemma R, finite-cover equivalence | CORRECT | Closed decreasing inverse images in compact K̄; every class enters at finite P. Compactness of B_P supplies the finite subcover. |
| Lemma N, ambient Haar-null U | CORRECT | II-2 supplies −1 mod f for every prime f ≡ 3 mod 4. Independent coordinate events have divergent reciprocal-prime mass. |
| Compatibility with UCOVER / ELL0 | CORRECT | Their measure is Haar on ℤ_ℓ^×, pushed onto an ambient-null slice, not ambient product Haar. No contradiction. |
| Lemma M, I-1 / I-4 / II-1 / II-2 | CORRECT | Divisibility identities and cylinders agree with the actual ET formulas. Family hypotheses remain necessary. |
| Lemma M, mixed I-2 / I-3 / II-3 | CORRECT | CRT gives the displayed equations; I-3 is existential over the root whose off-S component is 1, as now explicitly stated. |
| Prop M′, all seven families | CORRECT | Re-derived each bound, including I-1's swap and both I-3/II-3 cases. Fixed S-parts, not merely support S, are essential. |
| 21 nonempty T7 rational slices | CORRECT / independently verified | All 21 q are T-units and non-residues mod 11. Each certificate covers its entire slice, not just sampled points. |
| Five covered T13 slices | CORRECT / independently verified | All five certificates cover all 51480 box residues. Total across both sets: 26 certificates, 39 class entries. |
| q=2 class 6481 mod 8360 | CORRECT | Genuine I-3 class, with the stated root; the CRT cylinder contains the whole T7 slice. |
| 13-smooth finite-level count | CORRECT / reproduced | Full replay agrees byte-for-byte: 1316612 / 1556755200 at Q=3116623910400. This does NOT prove X_13 nonempty. |
| Raw free-slice series divergence | CORRECT, scoped | The prime-modulus subseries alone diverges. This defeats that raw union bound, not compactness, conditioning, or overlap-aware arguments. |
| Fixed-P convergence | CORRECT | Can be justified by divisor bounds and the finite Euler product; see below. |
| Type-II exponent <1/2 completes the rigid counting route | GAP if asserted for all seven families | The supplied quantitative argument handles I-1. M′ supplies finiteness, not a uniform tail estimate for the mixed families. |
| π°=(2 at 11,13; 1 elsewhere) ∈ U | WRONG — explicit counterexample | II-3 with (a,d,e)=(8,33,11999) catches π°. An independent I-2 catch also exists. |
| Historical bounded survival of π° | CORRECT as bounded EVIDENCE only | Both new catches exceed the original literal-enumeration ceiling; the II-2-only falsifier cannot detect them. |
| F1–F4 / “HOT LEAD: no” | CORRECT with domain clarification | No positivity mechanism is asserted; square *unit profiles*, rather than diagonal integer odd squares, are the relevant F1 control. |
| “narrowed”; no proof/refutation of K11 | CORRECT after fixes | R/N/M and the certificates survive; one proposed witness is now dead, not the entire K11 conjecture. |

## Decisive counterexample (hand-checkable)

Take **a=8, d=33, e=11999=13²·71**. Then gcd(4ad,e)=gcd(1056,11999)=1.
ET II-3 therefore gives the primitive class

**r = −4a²d−e = −20447 (mod m=4ade=12670944=2⁵·3·11·13²·71).**

The three independent CRT components are:
- r ≡ 2 (mod 11), since r−2=−20449=−11·1859;
- r ≡ 2 (mod 169), since r−2=−169·121;
- r ≡ 1 (mod 6816=2⁵·3·71), since r−1=−20448=−3·6816.

Thus **π° belongs to this family class and is not in U**. In fact the whole rigid cylinder g≡2 mod 11, h≡2 mod 169 is caught.
This also validates M's mixed II-3 row: e+1=12000 is divisible by 4(ad)′=96, and e′=71 divides 4a²d+1=8449.
A second catch is I-2: (a,c,f)=(125,88,11999), class **426568001 mod 527956000**; checked directly against both ET congruences and π°'s CRT value.
Neither class covers all K̄. In particular, this does not decide the remaining h≡2 mod 13 lifts.

## Proof audit and scope

R: each family cylinder is clopen; X_P is closed in compact B_P. Its inverse image Y_P in K̄ is nonempty iff X_P is, since all higher coordinates are free. The Y_P decrease, and their intersection is exactly K̄∩U. Finite intersection/finite-subcover arguments prove every direction claimed.
N: f=4d−1, a=1 yields −4d≡−1 mod f. For distinct prime f≥13, the events are independent, also after conditioning on K̄. The sum of 1/(f−1) over primes 3 mod 4 diverges. Borel–Cantelli proves ambient nullity, not emptiness. Fixing all coordinates except ℓ to 1 already defines an ambient-null slice, so UCOVER/ELL0's positive slice masses are consistent.
M′: II-2 gives 3adw≤2N; E/D gives 3a′cD≤2N₂ after orienting a≤b; I-1 gives 2d′Cw≤n after allowing both orientations. I-2 gives 3wxD≤2FB (or the swapped bound). For I-3/II-3, x(4tyu−G)=u+tF implies the stated bound when 4yu>F; otherwise the positive integer-distance η bounds t. Denominators must be positive and integral, then exact family/S-part filters apply.
Fixed-P convergence: the number of parameter/root occurrences at modulus m is O_ε(m^ε), using divisor bounds (and bounded 2^{ω(m)} on P-smooth moduli). Each cylinder has mass O_P(1/m). Choose ε<1 and sum over P-smooth m via ∏_{p≤P}(1−p^{−1+ε})^{-1}. This supplies the omitted domination argument.
The rigid-tail claim needs qualification: the I-1 estimate n^θ/N with n≤N² is summable over S-levels for θ<1/2. No corresponding quantitative domination of all mixed M events is established here. Even a valid total tail bound must be smaller than the actually surviving finite-level mass; summability alone does not establish that inequality or nonemptiness.

## Computation audit

Verifier/search: `scripts/z67_xrev_k11_check.py` (no original enumeration code used for certificate validity or witness search).
- `check /tmp/xrev_K11`: verifies every certificate directly against all seven ET definitions, rigid rational congruences, and exhaustive finite T-box coverage. All 26 pass; all 21 T7 slices are nonempty.
- Independently enumerates the entire small shadow class set using SymPy roots and compares it to the PARI/Hensel enumerator: agreement at Q=120120; survivors 2/5 at 9240 and 6/60 at 120120.
- Recovers UCOVER's −1215 mod 21736, from (a,d,e)=(11,2,247), including its rigid (6,7) cylinder.
- Checks q=2: c=2,d=19,f=55, root 46 gives 6481≡−55 mod 152 and 6481²≡26≡−304 mod 55; 6481≡1 mod 40 and ≡2 mod 209. These conditions hold on every point of Σ(2,{2,3,5,7}).
- Replays `z67_k11_tree.py 13,3,2,5,7,11,13,3,2,3,2,2,2,2,3`; exact agreement with archived `tree13.txt`, including intermediate counts.
- `search 300000`: exhausts 3829833 positive parameter pairs, pair product ≤300000, in **all seven families, with no modulus or valuation cap on the remaining parameter**. Exactly two catches: II-3 and I-2 above; none in the other five families. In particular II-2 is extended from ad≤100000 to ad≤300000.
- Search derivation: for A=4a²d, I-3 uses f_S | A+4 and f′ | A+1; II-3/II-2 use e_S/f_S | A+2 and e′/f′ | A+1. I-2 uses f_S | 2a+c and f′ | a+c. All candidate divisors then pass the original congruences. S-free classes cannot catch the square profile 1. The search streams pairs/divisors, not a Cartesian-product array.
Replay commands: `uv run --with cypari2 --with sympy python scripts/z67_xrev_k11_check.py check /tmp/xrev_K11` and `uv run --with cypari2 python scripts/z67_xrev_k11_check.py search 300000`, each under the limits above. Archive the reviewed branch's scripts/data into that temporary root first; tree replay additionally needs NumPy.

## Falsifier table audit

Read all four files in `data/z58/screens/`: 12 R₈-zero primes, 285 non-square composite zeros, 14 (★)-zero primes, and 38 𝔊*-zero primes.
F1 is logically compatible: square unit profiles lie in U and cannot lie in K̄ because their 11-component is a square. This is not a claim that every diagonal odd square is a unit of Ẑ.
F2 is genuinely outside scope: the claim concerns numerator-4 polynomial families, not positivity on the C-even/numerator-8 sub-line.
F3 is genuinely outside the claimed large-prime/unit-profile conclusion; no individual composite is asserted to have a witness.
F4 is also outside any positivity assertion: zeros of those narrower mechanisms neither refute nor verify finite ET coverability. No “survives all four” or HOT LEAD inference is justified or made.

## Required fixes, in priority order

1. **Remove the π°∈U conjecture and proposed-witness promotion everywhere** (abstract, §3, §7/FRONTIER proposal, bottom line, O1); replace with the explicit II-3 refutation above. Preserve the bounded historical computations with their actual scope. K11 itself stays open.
2. **Restrict the θ<1/2 sufficiency claim to the I-1 tail**, or supply a quantitative all-family reduction/tail estimate for the mixed events, plus the required survivor-minus-tail inequality. Per-level finiteness does not fill this gap.
3. Keep “finite covering of K” explicitly about K's **unit profiles / large-prime tail**, not arbitrary integers or ES counterexamples; call F1's objects square unit profiles. Add the short fixed-P convergence justification if retaining that assertion as proved.

The reductions and certified finite computations are usable after these fixes. The explicit candidate is not. Do not record an unqualified acceptance of the current FRONTIER paragraph.
