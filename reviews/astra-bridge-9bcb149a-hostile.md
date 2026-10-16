# Hostile review: O249 / ASTRA_BRIDGE

Reviewed `9bcb149a..5743a49`, including all five scripts, extracted data and three memos. Astra inspected read-only at `d7300f8`; no Astra programs executed or files changed. **Verdict: changes required. No FATAL defect in the core algebra; five MAJOR issues in the claimed dictionary, deductions and verification.**

## MAJOR

### M1. The slot separation is false for the stated state spaces

`ASTRA_BRIDGE.md:28–57, 241–259, 320–323` conflates **window shots** with all `ES^{(y,e)}` solutions, and **original genuine seeds** with all reachable Astra states.

* Lemma 1.2's twist calculation is correct, and its body correctly restricts the p-divisible-anchor formula to window shots. Its title and the table do not. The already-extracted Astra point at p=193, twist 5 gives
  `4/193 = 1/27985 + 1/6090 + 25/1218`.
  This is `ES^{(y,1)}` with y=6090, denominator root 5, but its distinguished numerator 1218 is **not divisible by 193**. It is the certified state `(1218,152250,699625)` from Astra STR §11.3. Thus the relaxations intersect away from ES; this actual Astra cross chain also takes this cap-1 point to cap 0. The blanket assertion that no listed operation changes a Claude state's cap is false. A universal/new cap-descent theorem is a different, still-open question.
* Lemma 1.3's p-free claim for reachable states is false. The existing genuine 193 source reaches `(450,19300,34740)` at `193·3²` (Astra STR §4; extracted data). Taking A=19300 gives `gcd(A,3)=1`, both other coordinates divisible by 9, **and 193 | A**. The 15241 forced fold is another explicit counterexample, acknowledged in §4 of the bridge itself. Astra STR §§11.4, 13 and 17 do not assert p-freeness for this entire class.
* Even the statement that genuine sources necessarily violate `rad(m) | y` needs `gcd(m,p)=1`: p=5,q=3,m=5,s=42,h=1 is genuine and rad(m) divides both integer coordinates 210 and 5. It fails the separate input-coprimality condition of `ES^{(y,e)}`.

Repair: distinguish seed, certified Type-I state, general coprime-anchor state, arbitrary capped solution, and Type-II square shot throughout. Keep the correct source/shot comparison, not a disjointness theorem for the programmes.

### M2. Type-I aliveness is not equivalent for the two relaxations

`ASTRA_BRIDGE.md:88–94` infers a converse not present in CAP_POINTWISE Prop 4.1(b). Explicit counterexample: **p=5, e=7, H=9**. Astra has the Thm 2.1 state with n=4,r=3:
`4/5 = 16/21 + 1/63 + 1/45`.
Nevertheless **no `ES^{(y,E)}` solution exists at the retained coordinate 45, for any cap E**, including infinity.

Proof of the negative: write `7/9 = 1/y + 1/z`, y a positive integer, and put `R=7y−9>0`, so z=9y/R. Self-muteness forces every prime of R to divide 9: a prime t|R with t∤9 cannot divide y, hence survives in den(z) without dividing y. Thus R=3^c. Integrality of y forces `c ≡ 5 (mod 6)`. Then v₃(y)=2 and `den(z)=3^(c−4)`, an odd positive exponent, never a square. If the retained coordinate 45 is instead assigned the mute-coordinate role, its only permitted denominator prime is still 3, since 5=p is forbidden by input coprimality; the same argument applies.

Cor 2.2 itself is correct. Its conclusion characterizes **Astra** aliveness; CAP_POINTWISE provides a sufficient dead-level test, not a complete classification of Claude aliveness. Delete the asserted agreement and correct the verdict/memos accordingly.

### M3. The all-shot lattice bijection silently drops even overflow and root branches

`ASTRA_BRIDGE.md:106–111, 154–168` asserts a bijection for all shot data but requires `gcd(Y,2k)=1`. The valid shot **p=5,Q=2,g=3** has h=1,Q₀=1,Q₁=2,k=1 and point `(x,y,z)=(3,5,15/4)`. Its normalized lattice point is `(M,Y)=(2,2)`, excluded by the purported bijection and the primitive surface hypothesis. The larger even-overflow 15241 fixture is omitted for exactly the same reason. The script only generates odd Y, so cannot detect this failure.

The denominator valuation proof, including ℓ=2, is sound. Either state the theorem only for odd-overflow shots (and a specified root branch), or extend the surface to `gcd(Y,k)=1`, retaining even Y and explicitly requiring odd Y for `ES^{(y,E)}`. The forward lattice identity remains valid even when the normalized point is not primitive. Also state `gcd(p,g)=1` before using ρ⁻¹: p=5,g=15,ρ=5 satisfies the printed root hypothesis but ρ has no inverse. The script silently excludes these moduli.

A separate composite-root error is in Prop 3.2, line 136: `Q₀² ≡ Q² (mod q)` does **not** imply `Q₀ ≡ ±Q` for composite q. For **p=17,q=39,h=10**, the genuine source m=61,s=1622 corresponds to Q=8; the ES shot Q₀=5 divides h and gives `(5,170,34)`, but 5 is neither ±8 modulo 39. Use equality of squares, or specify independent CRT sign choices. Likewise, with a fixed ρ the lattice maps must say “sources/shots in this root branch,” not all data of modulus g.

### M4. The negative verdict is not proved by the size comparison

`ASTRA_BRIDGE.md:291–315, 341–343` labels “the exit cannot be [forced]” PROVED and concludes that level size forbids the required content. Prop 6.2 proves only **aliveness and subgroup membership**. Prop 6.1 obstructs **covering the entire square subgroup**, not representing one specified target. Small boxes can contain a prescribed target; small multiplicative orders/short relations are not excluded. The cited Astra SATURATION §3 explicitly says failure of saturation is not an endpoint obstruction; GATEWAY_COMPATIBILITY §3 supplies an actual successful target when saturation fails.

Moreover, B3 is a theorem about bounded-multiplicity main-term certificates, not a general theorem that a small divisor box cannot hit one residue. Neither that hypothesis nor a main-term certificate is supplied here. The e=p^{o(1)} range left by Prop 6.1 is also not ruled out. Memorylessness of an endpoint parametrization does not rule out a genealogy forcing its arithmetic data.

Downgrade the title and §6.3 to **Assessment: no bounded-cap proof obtained by this attempt**. Keep the genuine saturation necessary condition. The same overstatement propagates into `BRAINSTORM/z21_gates_are_B2.md` and the other memos' references to “Prop 6.2's obstruction.” In the explanatory construction also write `−H ≡ ℓY² (mod e)`, not equality of positive integers; a square denominator is not sufficient for `ES^{(y,E)}` if it has a 2-part.

### M5. The fixture verifier mislabels self-muteness and silently omits data

`scripts/z21_fixtures.py:55–93`, `data/z21_fixtures_translated.txt`, `ASTRA_BRIDGE.md:181–184,334`:

* `range(3,r_+1)` ignores the prime 2. Consequently the 15241 twist-2 point is printed as self-mute, although its integral coordinates are 3813 and 5288627, **both odd**. The 193 twist-2 states receive the same false label. This is particularly damaging in a dictionary whose main claimed distinction is self-muteness. Report radical divisibility correctly and separately enforce odd overflow/input coprimality before calling a point capped.
* Replay produces **49**, not 50, distinct checked states. Two additional numeric triples are silently skipped because `N=?`: data line 22 is at `233689·8²`; line 94 `(204,3860,49215)` is at `193·2²`. Both identities are correct when restored. The claim to recheck every numeric triple is false.
* The script prints `exact=False` rather than asserting failure. Type-II divisibility checks are also merely printed. A green process exit is not a certification. Report skipped rows explicitly and fail on failed identities/claimed classifications.

The other scripts pass the tested ranges, but they enumerate forward constructions, not independent completeness checks of the claimed state-space bijections. In particular neither a Claude Type-I aliveness oracle nor a reverse enumeration of all shot data is present.

## Proof audit: what survives

| Claim | Line-by-line outcome |
|---|---|
| Def 1.1 / Lemma 1.2 | τ=r and cap=max valuations are correct; anchor formula correct for window shots. “Unique coprime coordinate” assumes r>1. Scope error M1. |
| Lemma 1.3 | Source identity, C=s+1 and general scaling/defect equations correct. Genuine m>1 sources cannot be scalar-divided: the displayed congruences indeed force m=1. Reachable p-free assertion fails (M1). |
| Thm 2.1 | Both directions work, including positivity, r|HU, coprimality and cancellation of n² to get r|H². The ordered-point bijection is correct. |
| Cor 2.2 | Both directions and the choice between n₀,e−n₀ are valid. Reciprocity is correct; s=2 uses pe≡7 mod8 exactly as stated. Only the following Reading is false (M2). |
| Thm 3.1(c),(d) | Correct: even m gives qs≡1 mod2m and q a unit; s≡−1 iff q≡−1 iff m|2h. With k=m/2, D=s, Q₁=1, all Prop 1.3 converse congruences hold. Q₀=h/k; the stated gcd(Q₀,p) safeguard suffices. The converse for ES shots works. Genuine m=2 is an explicit exception. |
| Prop 3.2 | The retained-slice divisor criterion and target square are correct. Global ± root clause fails for composite q (M3). |
| Prop 3.3 | Source/primitive-shot T1 is correct. For composite e, use Jacobi symbols explicitly: all prime factors of H have symbol +1, whereas a candidate r≡−n²/4 has symbol −1. This proves (b), without incorrectly identifying the Jacobi kernel with the square subgroup. It is not emptiness of arbitrary W(a²m²). |
| Thm 3.4 | Basis (1,ρ),(0,g) gives the form `((p+ρ²)/g)u²+2ρuv+gv²`, discriminant −4p. The stated domain's reverse shot construction and den(z)=Y² are correct, also at 2. M3 concerns missing data and hypotheses, not that valuation computation. |
| Prop 5.1 | Correct for prime q: (K/q)=−1, −K is square in the generated subgroup since its square part has odd order; (h/q)=+1 does not force a nonresidue factor. |
| Prop 5.2(a),(b) | Correct with the printed gcd(Q,p)=1 restriction. The p=5,q=103,Q=30 counterexample really gives den(z)=20 without it. Pollack detector matches CAP_DOWN's cited result. The explicit cap bound in (c) is cited there only for p≡1 mod8; say so, or separately invoke classical cap-0 identities for p≡5 mod8. |
| Prop 6.1 | Correct: for odd e, CRT gives exactly 2^{ω(e)} square roots of 1, hence |K|=φ(e)/2^{ω(e)}. The relative-order/cap product is bounded by τ(H²); divisor and totient bounds imply the stated subpolynomial bound after absorbing log e. No general exit obstruction follows. |
| Prop 6.2 | The positive statement and Dirichlet compatibility (including ℓ=2,p≡5 mod8) are correct. −1 comes from the even-order nonresidue generator; −H≡−4⁻¹ then lies in the subgroup. The negative title/consequences are not proved (M4). |

## Minor / form / completeness

* `ASTRA_BRIDGE.md:328–329` and the lattice Reading omit the genuine m=2 exception explicitly retained in Thm 3.1(d). Example p=5,q=3,m=2,s=7,h=1 is genuine **and** ES-ready.
* Line 166 asserts `v_ℓ(Q)=v_ℓ(Y)` before its own parenthesis correctly allows an extra `v_ℓ(h/k)`. Delete the false intermediate equality.
* Raw divisibility pipes break Markdown tables (§1, §5.3, §6.1). Escape `|` or use `∣`. The fold row also reads “shot at a prime R | r” across unintended cells.
* CAP_POINTWISE Lemma 2.1 is an exact box/divisibility characterization, **not** the mixed-radix saturation theorem; the closer coverage discussion is EXPONENT_CAP §3. Call the relation analogous, not literally the same criterion.
* The CRT/finite-chain table needs the actual map: Astra forces `t² | J=(p+q)/4` and t|m, with compatibility `gcd(t,p(p−1))=1`; it does not directly prescribe a free Type-I level. One can derive H=sJ, e=s+m² and then normalize, but that derivation and its closure gates are omitted.
* The brief's height dictionary/comparison with `O_{p,s}(r^{32/11})`, strict normalization and height-floor gateway are not delivered. The gateway can have g=s>1 and **no inherited certificate** (Astra GATEWAY_COMPATIBILITY §1), so Thm 2.1 cannot silently cover it. Cofactor supply also has a separate forced composite-R rule absent from the macro table. Limit the verdict to the operations actually analyzed.
* `scripts/z21_phase.py 20 3` crashes sorting mixed `None`/integer histogram keys. It also skips the q₀ construction whenever q₀>QM, although its docstring promises a q₀ check independently of the bounded-window search. Separate these tasks and report “no bounded-window hit” explicitly.
* The lattice memo's ideal-class reading needs the same coprimality/primitive-form qualification as M3; its “ES=intersection” must remain **ES shots**, not all ES solutions.

## Replays

All commands run in this worktree with `PYTHONPATH=scripts`, `uv run python`, `timeout` (30–90 seconds) and a 800,000-KiB virtual-memory limit, sequentially.

| Command | Result |
|---|---|
| `scripts/z21_dict.py 500 60 100` | PASS: 3591 sources, 1809 even, 76 ES-ready/exact; 217 slices, 118 ES. |
| `scripts/z21_typeI.py 500 60 10000` | PASS: 396 pairs, 273 Astra-alive, 130 ES; max twist 11; 402 square/level T1 checks. |
| `scripts/z21_lattice.py 500 100 100` | PASS on its restricted domain: 5309 shots, 139 ES, 5013 sources. |
| `scripts/z21_phase.py 500 100` | PASS: 44 primes, max q₀=19, max least-root twist 9. |
| `scripts/z21_fixtures.py` | 49 exact states printed, 25 Type-I and 5 Type-II endpoint records; omissions/mislabels in M5. |
| `scripts/z21_phase.py 20 3` | FAIL: TypeError at line 61, comparing NoneType and int. |

Independent exact-rational calculations confirmed all counterexamples in M1–M3, restored both omitted triples, and checked the c≡5 mod6 residue calculation in M2. `git diff --check 9bcb149a..5743a49` passes. No existing mathematical claims or scripts were edited during this review.
