# LOWER_TAIL_ASTRA — O275: single-integer lower-tail attack

**Status: construction phase. ES is not solved.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE; interpretations are Assessment. Work is confined to `side-agent/lower-tail-astra`.

## 0. Reading and attack contract

Read STATUS.md's current headlines, DISCOVERIES.md (J)84–104, BM_CORRECTED_COUNT, SINGLE_P_COUNT, METAPLECTIC_ES, SYNTHESIS_SPARKS9, TWO_POWER_LADDER, CLASS_FORCING, B2_ACROSS_FIELDS, both 20261018 advisory-board memos, CONDITIONAL_ES, DISPROOF_AVENUES.

The unconditional BM main term is not the missing ingredient. Nor does a positive mean prove occupancy at one prime. I will not re-propose the boards' killed counting, bounded-reciprocity, norm-trap, or fixed-menu descent mechanisms.

### Construction queue (Assessment, not claims)

1. **Euclidean remainder dynamics at one p.** Enlarge the length-three word set to a power-size set of residue pairs; seek a primality-sensitive descent or collision whose boundary contains a good word. The enlargement must not silently count multiples of p, and the final map need not have bounded fibres. This targets M1b/M5 rather than a main-term driver (B3).
2. **Local-to-global failure rigidity.** If all positive word targets fail, derive an invariant of the *actual* division table, rather than prescribing independent factorisations at finitely many levels. The board left an inverse-theorem gate open; no claimed result is imported from that gate.
3. **Canonical real-quadratic data.** Use the full reduction cycle, not a finite list of polynomial recipes. JOINT_BUDGET Prop 4.2 only proves the resulting norm windows are not Jacobi-forced; it does not exclude a global cycle argument.

Each attempt must identify its exact missing implication, distinguish the two-line union from full ES, and retain odd-square and numerator-8 controls. No all-prime claim will be reported without exhaustive checks through 10^6 and independent certificate reconstructions.

## 1. Starting object

Use positive words `tuv − u − v = n`. Their two-line union for numerator k is exactly the presence of a coordinate divisible by k (SYNTHESIS_SPARKS9 Cor 1.2). The full five-slice condition for n ≡ 1 (4) adds `4 | tu−1` or `4 | tv−1` and is the negative Jacobi-sign fibre (DEDEKIND_ES Thm 4.5).

A new mechanism must force a good word, not merely a nonempty word set, a nonempty genus fibre, or reachability inside an already nonempty good fibre.

## 2. The arithmetic word forest

**Definition.** For n ≥ 1 let F_n have vertex set {1,…,n+2}. Distinct u,v are joined when `uv | n+u+v`. Label the edge by `t=(n+u+v)/(uv)`. Loops are deliberately omitted. This graph is an exact encoding of unordered positive words, except the diagonal words.

**Lemma 2.1 (PROVED, elementary).** F_n is a forest. For v>1 its only possible smaller neighbour is `r_v = (−n mod v)` in {0,…,v−1}. It is an actual neighbour precisely when r_v>0 and `v r_v | n+v+r_v`. If gcd(v,n)=1, the second condition is equivalent to `r_v | n+v`.

*Proof.* Any neighbour u<v satisfies u ≡ −n (mod v), hence u=r_v. A cycle's largest vertex would have two smaller neighbours, impossible. When gcd(v,n)=1, gcd(v,r_v)=1, and v already divides n+v+r_v; the product divisibility is therefore equivalent to r_v dividing n+v. ∎

The vertex bound is complete: if 2≤u≤v, then `n≥uv−u−v`, so `v≤(n+u)/(u−1)≤n+2`; if u=1 then t≥2 and v≤n+1. A diagonal word has u=v dividing n. At prime p>3 the only diagonal word is (t,u,v)=(p+2,1,1), whose sign is positive. Thus no good prime word is lost.

**Lemma 2.2 (PROVED).** Restrict to vertices coprime to odd n and colour v by `χ_n(v)=(v/n)`. On an edge put A=tu−1. Then

`(A/n) = χ_n(u)χ_n(v)`.

Consequently, for n≡1 (4), a bichromatic edge is exactly a five-slice certificate (the five-slice sign theorem is DEDEKIND_ES Thm 4.5). Along any tree path v₀,…,v_h, the product of edge signs is `χ_n(v₀)χ_n(v_h)`.

*Proof.* `Av=n+u`, so A≡uv⁻¹ (mod n); the Jacobi identity follows. The path product telescopes. ∎

**Construction target (not proved).** A non-residue in the component rooted at 1 forces a bichromatic edge without estimating its count. More generally, any independently forced pair of opposite-coloured vertices in one component suffices. This is weaker than demanding expansion, but stronger than mere existence of a good edge somewhere. We will test it before using it as a conjecture.

**Scope / barrier screen.** A forest is not itself an existence argument. T1 holds identically because all unit vertices at odd squares have colour +1. The forest exists for every n and every numerator; only the five-slice interpretation is 4-specific. In particular the same sign criterion must NOT be used for 8/n. Neither B3 nor the fixed-menu involution theorem excludes a growing rooted-component argument, but a component must actually cross colours. There is no nontrivial cycle on which to apply an odd-cycle or holonomy contradiction.
