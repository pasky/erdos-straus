# ZF0 part 1 — signed identities, refinements, and finite graphs
6 items completed: 5 interesting, 1 nothing; no covered/skipped/needs-compute.
Interesting: Z0307, Z0873, Z2780, Z2875, Z0984.
Z1901: concrete census completed; unrestricted rational composition is tautological.
ES remains OPEN; all finite counts below are CERTIFIED (computer), not universal positive ES claims.

## Shared exhaustive prime census

`scripts/z52d_p2_ZF0_Z1901_enumerate.cpp` enumerates **all** unordered positive triples `x≤y≤z` for every prime `p≤100000`, without a denominator cutoff. For `p/4<x≤3p/4`, reduce the residual to `a/b=(4x−p)/(px)` and use

`(ay−b)(az−b)=b²`, with `d=ay−b≤b`, `d≡−b mod a`, and `y≥x`.

For odd primes, `x<p` and `gcd(a,b)=1`. Consequently every eligible divisor of `b²=p²x²` is either `d=t`, `t|x²`, or `d=pt`, `t|x², t≤x`; a divisor containing `p²` is too large. The case `p=2` is handled separately. Products involving squares or three denominators use 128-bit arithmetic. Divisors of `x²` are cached; only one prime's anchor set is retained at a time.

Output: `data/z52b/pass2/ZF0/Z1901/primes.csv` (9592 rows). `scripts/z52d_p2_ZF0_Z2780_analyze.py` reuses the existing `pointwise_size_ct_check.py` divisor and brute enumerators to independently check every prime through 200; it also recomputes mergeability and Farey determinants using exact `Fraction` arithmetic. All comparisons pass. This is not a re-run of an existing test without a purpose: the existing enumerators independently validate the new census and its new classifications.

Reproduce from the repository root (all commands should retain these resource limits):

```sh
ulimit -v 8000000
timeout 30s g++ -O2 -std=c++17 scripts/z52d_p2_ZF0_Z1901_enumerate.cpp -o /tmp/zf0-part1-enum
timeout 1700s nice -n 10 /tmp/zf0-part1-enum 100000 > data/z52b/pass2/ZF0/Z1901/primes.csv
# Run the cubic-grid command in §Z2875 before this combined aggregation:
timeout 600s nice -n 10 uv run --with sympy python scripts/z52d_p2_ZF0_Z2780_analyze.py
```

The raw prime table is shared evidence for Z0873, Z1901 and Z2780; each has its own `results.json`. The three items are different classifications of a single complete enumeration, not three unrelated experiments.

## Z0307 — exact classification of the two-negative variant

**Audit.** `SIGNED_REFACTOR.md` is not wholly irrelevant: §1, line 26 explicitly displays `(t,-2pt,-2pt)` for primes `p=4t+1` (the scope is line 17), a genuine `(+,-,-)` identity. It does **not** perform the requested bounded-first-term search over all integers. Thus pass 1's blanket `covered` was insufficient, but claiming the file never treats this sign pattern would also be wrong.

**CERTIFIED.** Tested every `1≤n≤10000`, allowing all feasible `1≤x≤floor((n−1)/4)` and stopping at the first witness while scanning down from the upper endpoint. Failures are exactly **1,2,3,4,7**. Among inputs with a feasible first term, the nearest choice fails **142** times; for every such input except 7, moving down **one** repairs it. There are **10137** first-term trials and **8352** recorded witnesses with `y=z`. All 9995 witnesses and the full list of nearest-choice failures are saved in `Z0307/`.

**PROVED: positive integer solutions to `4/n=1/x−1/y−1/z` exist exactly for `n=5,6` or `n≥8`.** Here is the elementary mechanism, stronger than the finite test:

* Put `x=floor((n−1)/4)` and write `1/x−4/n=a/b`, initially with `a=n−4x`, `b=nx` (reduction is optional). If `n` is even and `n≥6`, then `a=2` or `4` and `y=z=2b/a` are positive integers. If `n≡1 mod4`, `a=1`, so the same equal split works.
* If `n≡3 mod4`, then `a=3`. If `3|b`, split the unit residual equally. If `b` is even and coprime to 3, one of `d=1,2` satisfies `d≡−b mod3`; then `y=(b+d)/3`, `z=(b+b²/d)/3`. Except for `n≡7 mod24`, either `3|b` or `2|b`: for odd residues 3,11,15,19,23 modulo 24 this is immediate.
* In the remaining class write `n=24k+7`. For `k≥1`, choose `x=6k=(n−7)/4`, so `a=7` and `6|b=nx`, with `b≥186`. If `7|b`, split the unit residual equally. Otherwise the divisors of 36 have every nonzero residue modulo 7: `1,2,3,4,6,12` already suffice. Choose such a `d≡−b mod7`; since `d|36|b²` and `d≤36≤b`, the same divisor formula gives positive integral `y,z`.

For `n≤4`, `1/x≤1≤4/n`, so subtracting two positive terms cannot work. For `n=7`, necessarily `x=1`, and `1/y+1/z=3/7` would require a divisor `d≤7` of 49 with `d≡2 mod3`; neither 1 nor 7 qualifies.

**Assessment.** The signed problem really is elementary, but not because the nearest first term always works. There is a universal two-choice construction with the small exceptional input 7. Nothing here transfers positivity to the ordinary ES problem.

```sh
ulimit -v 8000000
timeout 600s nice -n 10 uv run --with sympy python scripts/z52d_p2_ZF0_Z0307_signed.py
```

## Z0873 — only the largest denominator divisible by n

**Source check.** `data/z52b/variants2.json:212–235` really says:

```json
"only z div by n": {
  "n_fail_primes": 1,
  "last_fail_prime": 2,
  "n_fail_all3000": 11,
  "fail_all_head": [2,4,8,16,32,64,128,256,512,1024,2048]
}
```

Other intervening fields are omitted in this quotation. This is an all-inputs-through-3000 result, not just composites; its list includes the prime 2.

**PROVED obstruction, all k.** Suppose `n=2^k`, `k≥1`, and exactly one denominator, say z, is divisible by n. Then

`v₂(1/z)≤−k`, while `v₂(4/n)=2−k` and `v₂(1/x),v₂(1/y)≥1−k`.

But `1/z=4/n−1/x−1/y` would have valuation at least `1−k`, a contradiction. All three denominators cannot be divisible by n either: writing them `na,nb,nc` would give `4=1/a+1/b+1/c≤3`. Thus every power-of-two solution has zero or two n-divisible denominators, never one or three. This includes `2^k`, `1≤k≤40`, without any enormous finite-denominator search.

**CERTIFIED extension, 2≤n≤100000.** All **9591 odd primes** in the complete census have at least one sorted solution with `p∤x`, `p∤y`, `p|z`. For any n having an odd prime divisor p, multiply that solution by `n/p`. Sortedness is preserved and `n|(n/p)x` iff `p|x`, likewise for y,z. Therefore every non-power-of-two n in this finite range has the required solution. Exactly **16** inputs fail: `2,4,8,…,65536`; **99983** succeed.

This is an exact prime census plus a proved scaling reduction, **not** a claim to have directly enumerated every composite's triples. Beyond the finite prime range, the scaling argument remains conditional on having a suitable odd-prime witness; universal odd-prime existence is not proved here.

## Z1901 — what binary composition does and does not mean

**Definition.** Use the colored additive operad with colors positive rational numbers: an operation `(q₁,…,qₖ)→q` exists when `Σqᵢ=q`. Composition substitutes a decomposition of one input. The ES question asks for an operation from three unit-fraction inputs to `4/p`.

**PROVED formal statement.** Every existing triple factors as

`4/p = 1/x + r`, `r=(4x−p)/(px)=1/y+1/z`.

This uses a generally **non-unit** rational intermediate color r; it is a rebracketing, not a method that manufactures an ES solution. If one instead demands a tree of binary **unit-fraction** decompositions, a triple qualifies exactly when some pair sums to a unit fraction, i.e. `a+b | ab` for that pair.

**CERTIFIED full census:**

| Prime class | Primes | Unordered triples | Rational binary composites | Unit-only binary composites |
|---|---:|---:|---:|---:|
| p=2 | 1 | 1 | 1 | 1 |
| p≡1 mod4 | 4783 | 572425 | 572425 | **0** |
| p≡3 mod4 | 4808 | 1115222 | 1115222 | 531408 |
| All p≤100000 | 9592 | **1687648** | **1687648** | **531409** |

**PROVED zero on the hard-prime slice.** A unit-only binary refinement would give a positive two-term decomposition `4/p=1/a+1/b`. Then `(4a−p)(4b−p)=p²` with both factors positive. When `p≡1 mod4`, every divisor of `p²` is 1 modulo 4 but both required factors are 3 modulo 4: impossible. The unrestricted categorical observation is therefore tautological, and its restrictive, potentially useful interpretation fails exactly on this prime class. Outcome: **nothing**, after actually doing the concrete test.

## Z2780 — positive unit-step overlap and Farey structure

**Premise correction (PROVED).** An **undirected** graph with edges between r and `r+1/k` allows negative steps. For `p=4t+1`, it already has the positive-vertex path `0→1/t→4/p`, because `1/t−4/p=1/(pt)`. Thus undirected distance ≤3 does not encode the positivity constraint of ES. The computation uses **directed increasing** unit steps and adjoins the vertex 0.

**Exact finite object.** Let `S₂={1/y+1/z:y,z≥1}` and `Rₚ={4/p−1/x>0:x≥1}`. The relevant overlap `S₂∩Rₚ` is finite; complete triple enumeration determines it without trying to store the infinite S₂. For a given p, each distinct denominator occurring anywhere in a triple gives one distinct residual vertex. An anchor/pair certificate is one such choice inside a triple, with the remaining pair unordered. We also enumerate every distinct ordering of the three terms, i.e. every positive three-step path. For `p≡1 mod4` all terms are distinct in this census.

A reduced pair `a/b<c/d` is Farey adjacent iff `bc−ad=1`. The first edge `0→1/u` is always Farey. Classify the **middle** and **last** edges separately.

**CERTIFIED, all 4783 primes p≡1 mod4 through 100000:**

* **572425** unordered triples, **1294859** distinct `(p,residual)` overlap vertices, **1717275** anchor/pair certificates; **288982** distinct smallest-term anchors.
* Ordered path masks `(middle,last)` = `00,01,10,11` have counts **2613301,805504,15745,0** (total **3434550=6×572425**).
* A last-Farey path occurs for **402752** triples, exactly the Type I triples, and for **all 4783 primes**. A middle-Farey path occurs for **15745** triples and **3498 primes**. Triple classes can overlap through different orderings; these are not disjoint counts.
* No all-Farey increasing three-step certificate occurs. The maximum overlap is **822** residual vertices at `p=80077`.

Residue-stratified counts (no hardness comparison across unmatched residue classes):

| p mod24 | Primes | Triples | Overlap vertices | Last-Farey triples | Middle-Farey triples |
|---|---:|---:|---:|---:|---:|
| 1 | 1181 | 99123 | 229156 | 66440 | 1772 |
| 5 | 1206 | 170208 | 382874 | 121121 | 6121 |
| 13 | 1193 | 160271 | 357906 | 117747 | 1722 |
| 17 | 1203 | 142823 | 324923 | 97444 | 6130 |

**PROVED explanation of last-edge dominance.** If w is the last denominator, the reduced prefix `(4w−p)/(pw)` has denominator `pw/g`, `g=gcd(4w−p,pw)`. Its Farey determinant with `4/p` is `p²/g`. For odd prime p this equals 1 exactly when `w=pm` and `4m≡1 modp`. With exactly one p-divisible denominator this congruence follows from the ES equation; with two p-divisible denominators it cannot hold, since multiplying by p and reducing modulo p would leave the other nonzero reciprocal uncancelled. The last-Farey condition thus selects the Type I denominator rather than discovering a different family.

**PROVED obstruction to an all-Farey path.** Write the path `0,1/u,h/k,4/p`, with reduced positive fractions. Middle adjacency gives `hu−k=1`; last adjacency gives `4k−hp=1`. Substituting yields `h(4u−p)=5`. Both factors are positive; hence `4u−p` is 1 or 5, impossible when `p≡1 mod4` (it is 3 modulo 4). Every positive ES path on that prime slice necessarily has a non-Farey edge. The topical memo `BRAINSTORM/bsA_farey_graph_metric.md` concerns non-residue distances instead and does not perform this overlap census.

## Z2875 — coefficient pairs, discriminants, and irreducible impostors

For `e₁=x+y+z`, `e₂=xy+xz+yz`, `e₃=xyz`, set

`f(T)=T³−e₁T²+e₂T−e₃`, `e₃=n e₂/4`.

**PROVED identities.** Positive integer-root cubics on this slice are in bijection with unordered ES triples. Their discriminant is

`Δ=e₁²e₂²−4e₂³−4e₁³e₃−27e₃²+18e₁e₂e₃=(x−y)²(x−z)²(y−z)²`.

**CERTIFIED, two independent enumerations.**

1. Complete denominator enumeration for **1≤n≤100**, without a denominator cap, gives **6484** split cubics: **529** with repeated roots, **5955** with distinct roots. Every `(n,e₁,e₂,e₃,Δ,x,y,z)` is recorded in `Z2875/all_split_n100.json`.
2. An independent coefficient scan over **1≤n≤100**, **1≤e₁≤200**, **1≤e₂≤10000**, retaining integral `e₃=n e₂/4`, finds **1586** nonnegative-square-discriminant cubics. Exactly **682** split over the integers; **904** are irreducible. The 682 pairs agree **exactly** with the corresponding bounded subset of enumeration 1. All candidates are in `Z2875/grid.csv`; exact SymPy discriminants independently agree for all 1586 candidates, and SymPy confirms irreducibility of all 904 nonsplit candidates.

**PROVED counterexample to sufficiency of square discriminant.** At `n=2`, the cubic `T³−7T²+14T−7` satisfies `4e₃=2e₂` and has discriminant **49**, yet its possible rational roots ±1,±7 are not roots. Hence it is irreducible despite having three positive real roots. More generally, in this positive-coefficient slice nonnegative discriminant gives real roots and `f(−t)<0` for `t≥0`, but integrality is an extra requirement. For an integral monic cubic, square discriminant plus a rational root would imply complete integral splitting; without that root, cyclic irreducible cubics survive.

**Assessment.** The discriminant is a useful necessary filter, not an integrality certificate. This computation makes the failure concrete rather than dismissing the symmetric-function formulation as merely formal.

```sh
ulimit -v 8000000
timeout 30s gcc -O2 scripts/z52d_p2_ZF0_Z2875_cubics.c -lm -o /tmp/zf0-part1-cubics
timeout 600s nice -n 10 /tmp/zf0-part1-cubics > data/z52b/pass2/ZF0/Z2875/grid.csv
# Then run the shared aggregation command above.
```

## Z0984 — an actual bounded split/merge graph

**Definition.** For each **2≤n≤100**, vertices are sorted multisets of positive denominators at most **D=1000000**, with at most **L=10** terms, summing reciprocally to `4/n`. Edges replace one a by `(a+1,a(a+1))` or perform that exact inverse merge, including multiplicity at a=1. We enumerate the **complete components reached from** `(n,n,n,n)` and from every bounded three-term ES target. Components with neither kind of seed are outside the experiment. The search retains just one n's vertex set; the largest such set has 77670 vertices, well below the explicit 500000-state safety cap.

**CERTIFIED graph counts:** **6460** bounded three-term targets; **2180410** vertices; **5302860** undirected edges; **6372** seeded components. Exactly **186** components contain two triples, and no component contains more than two. All stored states are independently checked with exact rational sums. Only **n=2** has any three-term target reachable from the four-copy seed.

There is **one** component whose two triples require an excursion above length 3, at **n=11**:

`(3,44,132) → (4,12,44,132) → (4,11,44)`.

The first move splits 3; the second merges `(12,132)` to 11. Both endpoints sum to `4/11`. Exhaustive searches restricted to length at most 3 cannot connect them. Thus the proposed longer-identity mechanism genuinely operates, even though it does not connect the four-copy seed in this example.

**PROVED bounded-denominator normal-form criterion.** With D fixed, repeatedly split every splittable denominator until all a satisfy `a(a+1)>D`. Denominators strictly increase, so each starting term has a finite expansion tree. Different splits commute as multiset operations; therefore the terminal multiset is unique. Two identities are connected by elementary splits/merges, with denominator cap D but **no length cap**, iff their terminal multisets agree: each edge preserves the multiset, and equal normal forms give a common expansion. The script computes these multisets symbolically with multiplicity counters, rather than materializing potentially long identities.

**CERTIFIED strengthening.** The terminal normal forms give exactly **6372** seed/target classes, agreeing separately for every n with the length-10 BFS. Thus, for the selected seeds and targets at D=1000000, length 10 already detects all possible connectivity even allowing arbitrarily long identities. In particular, removing only the length cap cannot connect any additional four-copy seed to a three-term target. This is **not** a claim after removing the denominator cap, nor a statement about arbitrary exact two-term splits instead of the specified elementary split.

Runtime of the final graph run is approximately one minute on one core; no dense Cartesian-product arrays or unbounded mesh-like allocations are used. Detailed per-n results, the detour path, and aggregate counts are in `Z0984/results.json`.

```sh
ulimit -v 8000000
timeout 900s nice -n 10 uv run python scripts/z52d_p2_ZF0_Z0984_graph.py 1000000 10 100
```
