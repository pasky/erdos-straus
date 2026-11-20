# Cross-lab hostile review (Claude Opus) of the z72–z74 SHIFTS lane (Astra)

Result: every PROVED step re-derived by hand; every decisive finite claim recomputed by an independent engine; no WRONG
claim and no mathematical gap found. The fixes are scope wording, a ∀/∃ misreading and missing §0 blocks.
Label: Assessment (review)
Scope: the 11 root notes `SIGNED_ROOT_TRANSFER`, `Z74_ONE_SLOT`, `Z74_PRIMITIVE_TRANSFER`, `SIGNED_TWO_SHIFTS`,
`SIGNED_FACTOR_TRANSFER`, `PAIRED_SHIFT_EXTRACTION`, `SHARED_SCALED_SLOT`, `DIVISOR_SHIFT_CERTIFICATE`,
`DIVISOR_SHIFT_DOUBLE_MISS`, `CF_ADDITIVE_NEIGHBOUR`, `CF_SHIFT_SLOTS`, plus the lane paragraphs of `Z74_CHECKPOINT.md`.
These are all statements about ordinary integers and about specified *methods*: denominator windows at chosen shifts,
one- and two-slot transfers, CF-selected menus. None is a statement about ES at any prime. **ES is OPEN.** No PA/ZFC
independence is claimed or implied anywhere in this lane.
Review: this file (cross-lab: author GPT Astra, reviewer Claude Opus). Astra's audits were not relied on.
Verdict: **all 11 ACCEPT-WITH-FIXES** (the fixes are wording and format only).

## 1. Verdicts

| note | main labels | verdict | fix (applied, tagged "(z74 Opus xreview fix)") |
|---|---|---|---|
| SIGNED_ROOT_TRANSFER | CERTIFIED transfer; PROVED root lemma, two-miss consequences, two obstructions; Dickson family | ACCEPT-WITH-FIXES | §0 |
| Z74_ONE_SLOT | PROVED one-slot gate (p∣u and a second slot); polynomial no-go; CERTIFIED shift-11 null | ACCEPT-WITH-FIXES | §0; replay command |
| Z74_PRIMITIVE_TRANSFER | PROVED ceilings, primitive-pair test, three Dirichlet families, upper-direction test | ACCEPT-WITH-FIXES | §0 |
| SIGNED_TWO_SHIFTS | CERTIFIED 193; PROVED signed 11-classification, density one, Dickson k-shift obstruction | ACCEPT-WITH-FIXES | §0; "in any slot" scope (F2) |
| SIGNED_FACTOR_TRANSFER | PROVED large-f obstruction, 12h+11 sufficient condition, exact 23-classification | ACCEPT-WITH-FIXES | §0 |
| PAIRED_SHIFT_EXTRACTION | PROVED gcds; CERTIFIED finite falsifier; Dirichlet family; Dickson; Pell orbit | ACCEPT-WITH-FIXES | §0 |
| SHARED_SCALED_SLOT | PROVED gate, polynomial no-go, tied mod-23 test; CERTIFIED intersection table | ACCEPT-WITH-FIXES | §0 |
| DIVISOR_SHIFT_CERTIFICATE | CERTIFIED 214729; CONDITIONAL (Dickson) 840q+1 seed | ACCEPT-WITH-FIXES | §0; ∀→∃ wording in §2 (F1) |
| DIVISOR_SHIFT_DOUBLE_MISS | CONDITIONAL on Dickson: all divisor shifts miss both slots, infinitely often | ACCEPT-WITH-FIXES | §0 |
| CF_ADDITIVE_NEIGHBOUR | PROVED neighbour test, forced family, factor-sign obstruction, raw size audit | ACCEPT-WITH-FIXES | §0 |
| CF_SHIFT_SLOTS | CERTIFIED least miss 176401; PROVED period-one criterion (Schinzel for ∞), full-split test | ACCEPT-WITH-FIXES | §0 |

## 2. Per-claim table (re-derivations)

| # | claim | verdict | what I checked |
|---|---|---|---|
| R1 | Root lemma: Q=4x−3, x=ab, a≡−1 (3), b≡−a (47) gives (x,QbE,QxE) for 4/Q and (12x,12paE′,12pbE′), E′=(a+b)/47, for 4/p | CORRECT | Both rows are the generic Type II identity (K,nADE,nBDE) with n+c=4ABD and A+B=cE. It needs neither gcd(a,b)=1 nor 47∤a; those are only normalisation. a²≡−x≡−p (47) since p≡x (47) |
| R2 | Dickson family on b=617+Tj keeps h=1 and both prior double misses | CORRECT | Q, L and the cofactors are constant mod 11·23·599. The classes (Q≡2; 5,9 mod 11; L≡14, M≡1 mod 23) feed the exact classifications. Admissibility: at 599 only R′ moves; elsewhere ≤5 distinct roots; primes ≤7 divide all slopes |
| R3 | Two misses at 11, 23 with h=1 force L=rs, x≡1 (15), gcd(xY,QLRM)=1 | CORRECT | Recomputed the four linear relations (−43,−45,3,1). 43∤R since 10 mod 11 is excluded by dual failure. 3∤Y, 5∤L |
| R4 | Donor at the minimum works ⇔ x has a prime ≡2 (3) | CORRECT | 4/Q−1/x=3/(Qx), and Q≡1 (3) is prime |
| R5 | r∤ any root-eligible shift (r≡1 (4)); large-r obstruction 4r≥138s+23 | CORRECT | (−p/r)=(23/r)=(r/23)=−1. Obstruction: c≡23 (4r), 0≤j<2s. The r∣D case gives c≤6s+j+1. Otherwise both 4jB and 23a lie in [0,c), so 4jB=23a, which forces B=23E, a=4jE, E=1 and 6s=j(92D−1), impossible since the divisors of 6s are 1,2,3,6 mod 23. The prime-L corollary needs r≥41, and L≡1 (35) prime gives L≥71 |
| O1 | One-slot gate (lower direction d=kQ−p>0): p∣u and p divides exactly one more slot | CORRECT | v=kpQr/(pt+4dr). For p∤u, h is prime to pr, so h∣kQ, but h≥p+4d>kQ. Mod p, p∣xy. Three multiples would give 4/Q≤3/p |
| O2 | No fixed rational-polynomial donor (or finite menu) at fixed k,d | CORRECT | p∣u(p) i.o. forces F(0)=0. The positive component on (−d,∞) is clopen (each entry ≥(T+d)/(4k)), so u(0)>0. The proof in SHARED_SCALED_SLOT is the same |
| O3 | Exhaustive tests (h∣kA² necessary; donor-first window Q/4<x≤pQ/(4p−2Q)) | CORRECT | — |
| P1 | Lower ceiling p≤Q(Q+r)/(4r)+1, attained at (23,139) with k=35, v=42 | CORRECT | The chain p≤(A+B)/a≤(b+1)/a≤Qx/T+1 is decreasing in x. Equality forces x=x₀, a=A=1, p=b+1. The top-half statement (A,B)=(1,b), j=a also checked |
| P2 | Primitive-pair criterion AB∣b, a∣A+B, g=(b/AB)(A+B)/a, p∣g ⇔ ap∣A+B | CORRECT | gcd(AB,A+B)=1 gives necessity; sufficiency by direct sum |
| P3 | Repair equation (4ek−pc)(4v−p)=p²c | CORRECT | Derived from 1/v=4/p−c/(ek) |
| P4 | Three infinite families: (j,s); growing k with p≡178081 (209160); upper k=2, d=161 | CORRECT | All identities were re-derived symbolically and checked at several members. gcd(840,4s²D)=8 and j≡−1 (8) are compatible. The nonsquare classes mod 19, 83, 11 are correct (falsifier F1) |
| P5 | Upper direction: exact test h=pt−4dr>0, h∣kQ; (p+d)/(8d)≤u/Q<p/(4d) | CORRECT | mt=1 would mean u/Q=1/4. Both endpoint examples verified |
| S1 | 193: six sorted triples; direct shifts {7,15,39,967,2511,5327,5607}, Type I {3,7,143}; J-eligible {15,39,5327,5607}; R-eligible none | CORRECT (CERTIFIED) | Brute-force y-loop with no factoring, and a divisor enumeration: they agree. Literal family: root-eligible d=103 hits (s=5018) |
| S2 | Exact signed classification at 11 (direct; Type I) | CORRECT | Complement of −{3^i p^j} is {1,2,6} for p≡2,6. Signed sets factor as products, because exponent intervals add, so it is valid even if 3∣Q. Dual: base-2 logs mod 10; all cases redone (pair + reserved ≤4<5) |
| S3 | J-repair from any Type I triple: exactly one p-free slot gives a J-eligible direct shift | CORRECT | (ss′/p)=(ab/p)=−1 (A2/CT), and (p/(4s−p))=(s/p) |
| S4 | Density one at the least eligible prime | CORRECT | Conditioning on (p/d)=−1 is independent of the residue mod q (CRT), and Σ1/q over q≡−1 (d) diverges |
| S5 | Dickson: first k eligible shifts are primes d_i, all failing in both families | CORRECT | ≤8 excluded roots at d_i. J-negative d≤2X must be a d_i (3d_i>2X, d_id_j>2X). The dual N_i≡1/4 is a square. Admissible at every ℓ |
| F1 | Keeping f: AB=f or h impossible; large-f (4f≥33h+11) excludes every normalised Type II K with f∣K at **every** shift | CORRECT | c≡11 (4w) holds for all shifts. Same template as R5 with 11, 3h |
| F2 | 12h+11 sufficient condition with unit root (4a)² | CORRECT | gcd(9h,12h+11)=1, so normalising by g keeps c∣A+B |
| F3 | Exact 23-classification (Type II = unrestricted direct; Type I) | CORRECT | Reserved {2^i3^j}= squares∖{9,18}, so the failures are exactly the inverse pair {5,14}. Three nonsquares orient to 10. Q≡3 (4) ⇒ 2∣L ⇒ hit |
| X1 | gcd(Q,R)=gcd(Q,D)=1, gcd(R,D)∣19, and 19 cannot be shared on a double miss | CORRECT | 11D−6R=665; 19≡8 (11) |
| X2 | Neighbour identity 4/p=1/(abt)+1/(pat)+1/(pbt); Dirichlet family with Q free of primes ≤B; Dickson for p,H,R | CORRECT | Primitive at M, L, q, b. The unhandled primes of b divide 27 or 417. H≡1 (11) since q≡p≡2 |
| X3 | Pell orbit T s²=Aq²+11q−1 and the dual triple (nN,7Ta,7Tb) | CORRECT | Integrality mod 9240 is kept by a unit ≡1 mod 4A·9240. n≡1, q≡3 (4), so N is integral. s/q→√(A/T)<7 |
| H1 | Tied mod-23 test for the least donor (x,2Qx,2Qx), Q≡3 (4) | CORRECT | 2 has order 11 mod 23, 3=2^(−3), and i−3j covers −5..5 |
| D1 | 214729: all 16 D∣(p−1)/4 miss both slots | CORRECT (CERTIFIED) | Two independent tests (signed reachability, divisor enumeration). The shift-19 triple is verified |
| D2 | DOUBLE_MISS (Dickson): for every D∣(p−1)/4 both slots miss | CORRECT | p₀=m² seed, gcd(a_F,Q₀p₀)=1, normalised L_F≡1 (c_d), admissibility at ℓ∣M (n=0) and at ℓ∤M (ℓ>b), nonproportionality via values at 0 and −1/(4T). Fixed d: every atom has Jacobi +1 mod c_d. Growing dq: a finite positive-rational list independent of q, so c∤A+B eventually. Dual identity N=dq(p−t), p−t=tc+1 recomputed |
| D3 | CERTIFICATE §2: q₀=21599 seed data (49 distinct roots, units at S, 32 fixed-row misses) | CORRECT | Recomputed. The first sentence reads as ∀ (F1) |
| C1 | Neighbour test f∣4P²+(1−4h)(r+1)+4h ⇔ B∈ℤ; triple (AB,pA,pB) | CORRECT | 20161 row 101 recomputed from the CF expansion |
| C2 | Forced family s=84+137·43680j: q=Q₁, f∣2m²−1, 13∣A, n≡8 (13) | CORRECT | Checked for j=0..3; 154853161 is prime |
| C3 | Every prime factor of a reduced CF denominator is a residue mod p (p≡1 (8)); CT(a)/A2 then exclude full support | CORRECT | CT(a) as stated in POINTWISE_SIZE (Type I: (c/p)=−1 gives each of ack, bck a negative prime) |
| C4 | Raw size audit q+r<2√p; δ∣(r+q) exact | CORRECT | The (1201; 30,43,7) row was recomputed |
| C5 | 176401 least miss (79th prime ≡1 (840)); expanded menu {3,419,839,1679,3359} all miss | CORRECT (CERTIFIED) | Recomputed with my own CF code. All 78 smaller primes hit on the narrow menu |
| C6 | Period one: the dual at 3 always fails; direct ⇔ (m/2)²+1 has a prime ≡5 (12); infinitely many under Schinzel | CORRECT | Both quadratics are irreducible and distinct, and take the value 1 at t=0 |
| C7 | Full-split test 16r²+4P²+Q_{i−1}≡0 (c), b has (b/p)=−1 | CORRECT | (K/p)=(c/p)=(p/c)=(−1/c)=−1 |

## 3. Computation
`scripts/z74_xrev_shifts_check.py` is self-contained. It does not import any campaign code. It has its own Miller–Rabin,
Pollard–Brent, Jacobi and CF routines. Every completion test is run two ways and asserted to agree:
(i) signed-product reachability of −1; (ii) divisor enumeration with a returned, identity-checked triple. For small n a
factor-free y-loop is used as well. **248 checks pass in 5 s, 35 MB**:
`ulimit -v 6000000; timeout 1800 uv run --offline --no-project python scripts/z74_xrev_shifts_check.py`.
Coverage:
* 214729, all 32 slots.
* 193: complete triple list, shift lists, J/R sets, the d=11 table.
* 9565921: eligibility at 11/23/47, the double misses, the triples, the 47 hits, the five Dickson seeds and family
  members j=1..3.
* 6206649121: all 6 windows miss, the factorisations, the donor miss.
* The 1e7 survey: 3426 primes, a unique prime 6348721 needing 199, and the 11-counts (158,86,983,484).
* The Z74_ONE_SLOT shift-11 null by **complete donor brute force, all three slots replaced** (independent of the gate
  lemma). The k=3 census gives 1078 pairs and 5 hits, with the gate holding on every hit.
* The SHARED_SCALED_SLOT table.
* The PRIMITIVE examples and families.
* The factor-transfer certificates and table rows 1 and 4: (244,59,113,109) and (158,40,71,67).
* The paired-shift lists and the Pell seed.
* All CF claims.
* The divisor-certificate seed data.
* The PHASE43 and Z73 composite cross-check rows.

The authors' replays (`cf_shift_slots`, `divisor_shift_certificate`, `signed_root_transfer`, `signed_two_shifts`,
`signed_factor_transfer`, `paired_shift_extraction`, `shared_scaled_slot`, `z74_single_retune`,
`z74_primitive_transfer`) were all re-run, and all pass with the outputs quoted in the notes. Not independently redone:
SIGNED_FACTOR_TRANSFER table rows 2, 3, 5 and 6, and the falsifier-screen counts. These are DATA and not load-bearing.

## 4. Labels, scope, priority
* **Scope.** All notes say the right thing: method counterexamples, not ES counterexamples. Each Dickson/Schinzel use is
  labelled CONDITIONAL. Each Dirichlet family is honestly called ET territory and not new coverage
  (ET Prop. 1.9 checked at `sources/lit2026/audit-elsholtz-tao-1107.1010.txt:371`).
* **One ∀/∃ slip.** DIVISOR_SHIFT_CERTIFICATE §2 opens "for p=840q+1 with q prime, the … construction obstructs all
  shifts". That reads as *every* such p. The construction gives **infinitely many** such p, under Dickson (F1).
* **"Root-eligible" scope.** "193 fails every root-eligible shift" is true for the two windows K=(p+d)/4 and pN. It is
  **false** for the literal slot p(d+1)/4: the root-eligible prime d=103 hits there, with s=5018 in (52,772,5018). The
  note says this in its body, but its opening "in any slot" and the WAVES line drop the qualifier (F2, M1).
* **Priority.** The character inputs are repo-known: CT(a) and A2 (`notes.md` Lemma 77.6), and Z52D Prop 2.4. The notes
  cite them as such. No claim of novelty beyond explicit packaging and certificates.

## 5. Required fixes, in priority order (note-level ones applied by me)
1. **F1 (DIVISOR_SHIFT_CERTIFICATE §2, quantifier).** "for `p=840q+1` with `q` prime, … obstructs all shifts" →
   "there are **infinitely many** primes `p=840q+1` with `q` prime at which every divisor shift `c=4D−1`, `D|(p−1)/4`,
   misses both slots". Applied, with the original kept in strikethrough.
2. **F2 (SIGNED_TWO_SHIFTS opening, scope).** "in either denominator, in any slot" → add "(i.e. as either of the two
   window denominators `(p+d)/4`, `p(pd+1)/4`, in any position of the triple; the literal slot `p(d+1)/4` does hit at
   the root-eligible prime 103)". Applied.
3. **F3 (§0 blocks).** None of the 11 notes had the AGENTS.md §0 block. Added to each, with Review pointing here.
4. **F4 (Z74_ONE_SLOT replay line).** Changed `uv run --no-sync` to `uv run --offline --no-project`, the house
   convention. (It ran either way.)
5. **F5 (Z74_CHECKPOINT, lane paragraph).** "`DIVISOR_SHIFT_CERTIFICATE.md` is unconditional" → "the finite certificate
   in `DIVISOR_SHIFT_CERTIFICATE.md` is unconditional (its §2 seed is Dickson-conditional)". Applied.
6. Optional, not applied: SIGNED_ROOT_TRANSFER's root lemma could say explicitly that gcd(a,b)=1 and 47∤a are only
   normalisations, since the identity holds without them.

## 6. Master-file corrections (for the orchestrator; I did not edit master files)
**M1. WAVES.md line 23–24 (z74).** Current:
> `−` Method counterexamples: a one-slot obstruction (`Z74_ONE_SLOT.md`); 214729 misses all 16 divisor shifts
>     (`DIVISOR_SHIFT_CERTIFICATE.md`); 193 fails every root-eligible shift (`SIGNED_TWO_SHIFTS.md`); elementary-hull BCM.

Replacement:
> `−` Method counterexamples: a one-slot obstruction (`Z74_ONE_SLOT.md`); 214729 misses both slots at all 16 divisor
>     shifts (`DIVISOR_SHIFT_CERTIFICATE.md`; ∞ under Dickson in `DIVISOR_SHIFT_DOUBLE_MISS.md`); 193 fails every
>     root-eligible shift in both windows (p+d)/4, p(pd+1)/4 (`SIGNED_TWO_SHIFTS.md`); elementary-hull BCM.

**M2. WAVES.md z74 `R` line.** Current: "… The joint note's ordinary-prime NR Variant is a GAP. Other z74 items are not
cross-reviewed." Replacement: "… The joint note's ordinary-prime NR Variant is a GAP. The SHIFTS lane (11 ordinary-integer
notes) is ACCEPT-WITH-FIXES, with no gap (`data/z74/xreview/REVIEW_SHIFTS_OPUS.md`). Other z74 items are not
cross-reviewed." (Adjust this if other lanes land in the same export.)

**M3. FRONTIER §6** has no line for this lane yet. I propose one merged line, since the root cause is shared:
> * (z72–z74) Fixed-shift denominator windows and slot transfers. These are root-eligible shifts 11/23/47, one-slot
>   repairs of a scaled Q-donor, divisor shifts 4D−1 with D|(p−1)/4, and CF-selected or factor-of-Q menus. Each one
>   misses at an explicit certified prime: 9565921/6206649121, 2521/12601/31081, 214729, 176401, 1711921. The infinite
>   versions hold under Dickson or Schinzel. The positive successes are ET congruence classes. → `SIGNED_TWO_SHIFTS.md`,
>   `Z74_ONE_SLOT.md`, `DIVISOR_SHIFT_DOUBLE_MISS.md`, `CF_SHIFT_SLOTS.md`; review `data/z74/xreview/REVIEW_SHIFTS_OPUS.md`.

**STATUS.md:** no change needed. None of these notes is quoted there, and none meets the STATUS test: they are
BARRIER-SCOPED, METHOD-CX or DATA.
