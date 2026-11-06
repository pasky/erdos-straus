# Z60_DYNAMICS — R(p) as a single-long-orbit hitting problem: target measure N^{−1+o(1)} vs rate N^{−1/2}; narrowed, no lead

**ES is OPEN; nothing here proves or disproves it.** Internal, unrefereed. Lane DYNAMICS of wave z60 (brief
`z52bbriefs/z60_lanes.md` §DYNAMICS; rules `z58_lanes.md`, `z53_depth.md`). Scripts `scripts/z60_dynamics_*`, data
`data/z60/dynamics/`. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.

**Verdict: narrowed (no HOT LEAD).** (★) has an exact encoding as the number of points of one p-dependent orbit (the
Kloosterman set = split-torus orbit = Farey/Hecke points of level p) lying in an explicit target. The target has measure
μ ≍ (log p)²/p = N^{−1+o(1)} for an orbit of N = p − 1 points; the best equidistribution rates are N^{−1/2} (Weil,
provably optimal for that norm) and N^{−1/2+7/64+ε} (Hecke points on SL₂(ℤ)\ℍ). Scoped no-gos (§5): Weil-type
completion needs a target of ≥ 2p^{3/2}(1 − o(1)) grid points, while T_p has ≤ p(1 + log p)² (missing exponent exactly
1/2, Prop 3 + Lemma 3); for *any* rate ε_N, a certificate's margin over the rate is at most R(p)/N ≤ p^{−2/3+o(1)}
(Prop 4). T1 is located exactly: all hits lie on the QNR half-orbit, which is empty at odd squares and on which the main
term vanishes (Lemma 2, Prop 6). Every escape hatch examined (§6) closes or reduces to B2 / the TRACE lane.

Notation. R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (FRONTIER §2.1). For odd n,
O_n := {(x, x̄) : x ∈ (ℤ/n)^×}, representatives x, x̄ ∈ [1, n − 1] (the *Kloosterman set*; it is the orbit of (1, 1) under
the split torus t·(x, y) = (tx, t⁻¹y) on ((ℤ/n)^×)²), c(x) := (x x̄ − 1)/n ∈ ℤ_{≥0}, χ_n := (·/n) (Jacobi).
**Target** (defined on the grid, without reference to the orbit):
T_n := {(x, y) ∈ [1, n−1]² : c := ⌊(xy − 1)/n⌋ ∈ 4ℕ, c ≥ 4, c | x + 1}. R°(n) := #(O_n ∩ T_n).

## 0. Mandatory falsifier table (final)

| Screen | Behaviour |
|---|---|
| F1 odd squares | Encoding exact for every odd n (Lemma 1). For n ≡ 1 (4) every hit x has χ_n(x) = −1 (Lemma 2): hits lie on the **QNR half-orbit** O_n⁻, a coset of the index-2 subtorus; **O_n⁻ = ∅ iff n is a square — the orbit degenerates exactly there.** The *full* orbit and the target do not degenerate: N·μ(T_n) = 8.03 at n = 101² vs 7.95 at p = 10007 (`orbit_check.txt`). So any argument through the full orbit whose inputs (rates, measures) are equally valid at squares cannot certify a hit; the T1-sensitive half (the χ_n-twisted sum) has **zero main term** (Prop 6). Primality/non-squareness enters only through χ_n ≠ 1. |
| F2 R₈ (C even) | The C-even target T_n⁽⁸⁾ = {8 \| c} has the same orbit, ≈ half the measure, the same QNR location (Lemma 2 holds verbatim for C even) and the same rates. Nothing in the dynamics distinguishes C odd from C even. **Fails** (any rate argument for T_n would apply to T_n⁽⁸⁾, whose zeros at 10¹⁰ are certified). |
| F3 composites | Encoding, Lemma 2 and the measure count hold for composite n; Weil-quality bounds hold for Kloosterman sums mod squarefree n up to n^ε. Uses only χ_n ≠ 1 (non-squareness), not primality. **Fails** (285 composite zeros; also 105, 4545). |
| F4 known zeros | 409, 577, …, 8 813 281 have R = 0 with N·μ(T_p) ≈ 2.9–15 (409: 2.87; 23929: 9.85). No mechanism proposed; the no-gos are consistent with them (they are below every threshold). |

No idea survives all four; nothing is claimed as a lead.

## 1. Precise statements attacked

**(D-hit)** For every prime p ≡ 1 (4), p > p₀: O_p ∩ T_p ≠ ∅. By Lemma 1, (D-hit)(p) ⟹ R(p) ≥ 1 ⟹ ES(p). It is
strictly stronger than R(p) ≥ 1 only by the boundary solutions u = 1 or B = 1 (fixed-u events, B1).

**(D-eq)** Question: is there an equidistribution statement for O_p — or for another p-dependent orbit (Hecke points of
level p, closed horocycles of length ≍ p, Farey points x/p) — at a *single* p, strong enough to force (D-hit)?
*Why not already closed:* FRONTIER B3 (scale constraint) and BRAINSTORM `bsA_hecke_cusp_excursions.md` record the
heuristic "rate p^{−1/2} misses measure p^{−1}"; STRONG_APPROX_ES §10 phrases the needed horocycle statement. None
had an exact orbit encoding, a proof that the missing exponent is intrinsic (not technological), a margin theorem for
arbitrary rates, or the T1 location in orbit terms. This memo supplies those and tests the escape hatches.

## 2. Exact encodings (PROVED; CERTIFIED checks)

**Lemma 1 (Kloosterman-orbit encoding; PROVED).** For every odd n ≥ 5,
R(n) = R°(n) + #{(u, B, C) : u = 1 or B = 1}, and (x, x̄) ↦ ((x+1)/c, (x̄+1)/c, c/4), c = c(x), is a bijection from
O_n ∩ T_n onto the solutions with u, B ≥ 2.
*Proof.* If (x, x̄) ∈ T_n then c = c(x) (x x̄ = cn + 1 exactly, so ⌊(x x̄ − 1)/n⌋ = c), c ∈ 4ℕ, x ≡ −1 (mod c) and
x x̄ ≡ 1 (mod c), hence x̄ ≡ −1 (mod c). Put u = (x+1)/c, B = (x̄+1)/c, C = c/4. Then
c(cuB − u − B) = (x+1)(x̄+1) − (x+1) − (x̄+1) = x x̄ − 1 = cn, i.e. 4uBC − u − B = n. If u = 1 then x = c − 1 and
x̄ = (cn+1)/(c−1) > n, impossible; likewise B ≥ 2. Conversely, for a solution with u, B ≥ 2 put d = 4uC − 1,
a = 4BC − 1; then ad = 4C(4uBC − u − B) + 1 = 4Cn + 1, so gcd(d, n) = 1 and a ≡ d⁻¹ (mod n); and
n − d = 4uC(B−1) − u − B + 1 ≥ (B−1)(4u−1) − u ≥ 3u − 1 > 0, likewise n − a > 0. So (x, x̄) = (d, a) ∈ O_n, c(x) = 4C,
c | x + 1. The maps are mutually inverse. ∎ CERTIFIED check: 19 values of n (primes, zeros, squares, composites),
`data/z60/dynamics/orbit_check.txt`.

**Lemma 1′ (the orbit dissolves into divisors; PROVED, elementary).** For each c ≥ 1 the c-th hyperbolic shell of the
orbit is O_n ∩ {c(x) = c} = {(d, (cn+1)/d) : d | cn + 1, d ≤ n − 1, (cn+1)/d ≤ n − 1}. (x x̄ = cn + 1 with both factors in
[1, n−1] is a factorisation, and every such factorisation has x̄ ≡ x⁻¹ (mod n).) So the hit condition on the c-th shell is
"cn + 1 has a divisor ≡ −1 (mod c)": **the target's congruence modulus equals the orbit's own shell index** — the
tied-modulus event B2, now as a statement about where one orbit sits relative to its own fibration. Weil-equidistribution
of O_n is equidistribution of the divisors of the progression {cn + 1}_{c<n} jointly; it cannot see the diagonal tie.

**Lemma 1″ (Farey / Hecke-point dictionary; PROVED via LENGTH_THREE Prop 1.1).** R°(n) = #{A ∈ [1, n−1] : n/A has
Hirzebruch–Jung (minus) continued fraction of length exactly 3, [[c, m, s]], with 4 | m} (word (c, m, s) = (u, 4C, B),
A = 4BC − 1 = x̄; letters ≥ 2 automatically). So R° counts Farey points A/n (equivalently Hecke points (A + i)/n of level n,
or primitive rational points on the closed horocycle of length n, Burrin's ℛ_n^{pr}(0, 1/n)) whose geodesic ∞ → A/n has
the 3-excursion structure of BRAINSTORM bsA H3. CERTIFIED: identical counts for 11 values of n incl. squares and 105, 4545
(`hj_check.txt`). *Remark (PROVED, from the pentagon (P) of LENGTH_THREE):* for a hit, det((h, m), (n, A)) = 1 with
h = d = 4uC − 1, so the Hecke point (A + i)/n is Γ-equivalent to a point of height n/(1 + d²), and also to one of height
n/(u² + B²); its Γ\ℍ position is governed by the solution's sizes, not by any fixed region — the hit condition is exact
(length *exactly* 3), a measure-zero event in the geodesic/cylinder space, not an open target.

**Lemma 2 (T1 location; PROVED).** If n ≡ 1 (4) and (x, x̄) ∈ O_n ∩ T_n then χ_n(x) = −1. Hence O_n ∩ T_n ⊂
O_n⁻ := {(x, x̄) : χ_n(x) = −1}, a coset of the index-2 subtorus {t²}, and O_n⁻ = ∅ iff n is a square.
*Proof.* x = d = 4uC − 1 divides 4Cn + 1 with d ≡ −1 (mod 4C); the classical lemma (PARITY_AUDIT Lemma 3.2; Z57_SYNTH
Lemma A.1(b)) gives (n/d) = −1, and Jacobi reciprocity with n ≡ 1 (4) gives (d/n) = (n/d). χ_n is a non-trivial character
of (ℤ/n)^× iff n is not a square. ∎ (CERTIFIED: all hits have χ_n = −1 for n ≡ 1 (4) tested; for p = 10007 ≡ 3 (4) the
sign is +1, as reciprocity predicts.)

## 3. Target measure vs orbit size

**Lemma 3a (PROVED, crude).** |T_n| ≤ n(1 + log n)² for n ≥ 5. *Proof.* For c = 4C and x = ck − 1 (k ≥ 1, so
x ≥ 3ck/4), the y with cn + 1 ≤ xy ≤ (c+1)n form an interval of length < n/x, so number ≤ n/x + 1 ≤ 4n/(3ck) + 1. Summing
k ≤ n/c: ≤ (4n/3c)(1 + log n) + n/c. Summing c = 4C ≤ n, with Σ_{C ≤ n/4} 1/C ≤ 1 + log n:
≤ (n/3)(1 + log n)² + (n/4)(1 + log n) ≤ n(1 + log n)². ∎

**Size (EVIDENCE + heuristic).** The shell count Σ_C n log(n/4C)/(4C) gives |T_n| ∼ n(log n)²/8; measured
(n−1)|T_n|/n² ≈ 0.64–0.80·(log n)²/8 for primes n ∈ [409, 1.002·10⁵] (lower-order terms), and the same ratios at
squares and composites ≥ 225 (`orbit_check.txt`).
So **N = n − 1 orbit points, target measure μ(T_n) = |T_n|/n² ≍ (log n)²/n = N^{−1+o(1)}**, expected hits ≍ (log n)².
The *true* discrepancy on this specific target is small (EVIDENCE, `disc_stats.txt`): over 209 primes p ≡ 1 (4) in
[10⁴, 1.4·10⁴], D := R°(p) − (p−1)μ(T_p) has mean +1.1, standard deviation 4.6, max |D| = 17.8 (N·μ ≈ 8.4, √p ≈ 118);
over 171 primes in [10⁵, 1.04·10⁵]: mean +1.9, sd 6.3, max 20.7 (N·μ ≈ 13.3, √p ≈ 322). The orbit behaves like a
Poisson sample on T_p (sd ≈ √(2Nμ) because hits come in (u, B) ↔ (B, u) pairs); provable rates are ≍ √p.

## 4. The rates available (verified from source where stated)

| Orbit | Rate | Source (checked) |
|---|---|---|
| Kloosterman set O_p ⊂ (ℤ/p)² | |Σ_x f(x, x̄) − (p−1)f̂(0)| ≤ 2√p Σ_{ξ≠0}|f̂(ξ)| | Weil bound |K(h,k;p)| ≤ 2√p (p ∤ hk); K(h,0) = K(0,k) = −1. Standard. |
| χ_p-twisted half (Salié) | Σ_x χ_p(x) e((hx + kx̄)/p) = ε_p √p (k/p) Σ_{v² ≡ 4hk} e(v/p), ε_p = 1 (p ≡ 1 (4)), i (p ≡ 3 (4)); value 0 at h = k = 0 | Iwaniec–Kowalski Lemma 12.4 (cited via secondary sources; formula CERTIFIED numerically here for p ∈ {11, 13, 17, 19, 23, 29}, all h, k ≠ 0) |
| Primitive rational points ℛ_n^{pr}(x, y) = {Γ((j + x)/n + iy) : (j, n) = 1} on SL₂(ℤ)\ℍ (y = 1/n: Hecke/Farey points of level n) | |δ^{pr}_{n,x,y}(Ψ) − μ(Ψ)| ≪_ε S_{2,2}(Ψ)(y^{1/2} + n^{−1+ε}y^{−(1/2+θ+ε)}), θ = 7/64; at y = 1/n: ≪ S_{2,2}(Ψ) n^{−1/2+θ+2ε} | **Burrin, Math. Ann. (2022), Thm 1.1** (read from the PMC full text); θ = 7/64 is Kim–Sarnak (JAMS 16 (2003), App. 2; not re-read). COU (Invent. 144 (2001)) gives Hecke-operator norm bounds in general (cited by Burrin as [3, Thm 1.1]; not re-read). |
| Closed horocycle of length 1/y on SL₂(ℤ)\ℍ | O(S(Ψ) y^{1/2}) (Sarnak 1981); O(y^{3/4−ε}) for all smooth Ψ ⟺ RH (Zagier) | as quoted in Burrin §1 (primary papers not re-read) |
| Segments of a closed horocycle of length ℓ | equidistribute if segment length > ℓ^{1/2+ε} | Strömbergsson, Duke 123 (2004), abstract (theorem text not re-read) |
| Covering exponent (Sarnak letter, Feb 2015) | K(S) := limsup log|V(t_ε)| / log(1/μ(B(ε))) ≥ 1; for LPS-type gates 4/3 ≤ K ≤ 2: "2" = square-root cancellation (Ramanujan/Deligne), "4/3" = **big holes** near projections of integer points; almost every point is approximated optimally | Sarnak's letter (read: statements (a), (b) and the discussion after them) |

*Sharpness of the exponent 1/2 (PROVED, Lemma 3).* For every prime p, Σ_{h ∈ 𝔽_p} |K(h, 1; p)|² = p(p − 1) and
K(0, 1; p) = −1, so max_{h≠0} |K(h, 1; p)| ≥ √(p − 1/(p − 1)). Hence no inequality
|Σ_x f(x, x̄) − (p−1)f̂(0)| ≤ B Σ_{ξ≠0}|f̂(ξ)| valid for all f can have B < √(p − 1/(p−1)) (test f = Re/Im e((hx + y)/p)).
*Proof.* Σ_h |Σ_x e((hx + x̄)/p)|² = Σ_{x,x′} e((x̄ − x̄′)/p) Σ_h e(h(x − x′)/p) = p(p − 1). ∎ (Measured:
max_{h≠0}|K(h,1)|/√p = 1.98–1.99 at p = 409…4001, `weil_check.txt`.) For Hecke points the analogous floor is the Eisenstein
continuous spectrum: the normalised T_p has eigenvalue (p^{it} + p^{−it})/(p^{1/2} + p^{−1/2}) → 2/(√p + 1/√p) at t → 0, so
the L²-operator norm of the normalised Hecke operator on L²₀ is ≥ 2/(√p + 1/√p) (standard: Eisenstein wave packets
concentrated near t = 0; not written out here).

## 5. Scoped no-go theorems

**Prop 3 (Weil-completion certificates need ≥ 2p^{3/2} target points; PROVED).** Let p be prime, T ⊂ 𝔽_p² any set and
f: 𝔽_p² → ℝ with f ≤ 0 off T. If (p − 1)f̂(0) − 2√p Σ_{ξ≠0}|f̂(ξ)| > 0 (the condition under which Weil + f certifies
Σ_x f(x, x̄) > 0, hence a point of O_p ∩ T), then |T| > 2p^{5/2}/(p − 1 + 2√p).
*Proof.* Put A = Σ_{ξ≠0}|f̂(ξ)|. The hypothesis gives f̂(0) > 0 and A < (p−1)f̂(0)/(2√p). For every z, f(z) ≤ f̂(0) + A <
f̂(0)(1 + (p−1)/(2√p)) =: f̂(0)·κ. Since f ≤ 0 off T, p² f̂(0) = Σ_z f(z) ≤ |T|·max f < |T| f̂(0) κ. Divide by f̂(0) > 0. ∎

**Cor 3 (PROVED).** For every prime p ≥ 10⁴, no f with f ≤ 0 off T_p yields a Weil-completion certificate for
O_p ∩ T_p ≠ ∅: by Lemma 3a, |T_p| ≤ p(1 + log p)² < 2p^{5/2}/(p − 1 + 2√p) for p ≥ 10⁴ (at p = 10⁴: 1.04·10⁶ < 1.96·10⁶,
and the ratio decreases). (CERTIFIED for the four primes 409, 1009, 2017, 4001: actual |T_p| = 0.078, 0.068, 0.059, 0.051 ×
the threshold.) The *direct* choice f = 1_{T_p} is far worse: Weil bound / main term = 334, 645, 1085, 1845 at those p.
**Missing exponent: exactly 1/2.** A certificate needs expected hits (p − 1)μ ≳ 2√p; the target supplies (log p)²/8.
By Lemma 3 the exponent 1/2 of the rate is optimal for this norm — the gap is intrinsic to the torus orbit, not a
deficiency of current technology. Enlarging T to fat sets does not help unless the extra part avoids the orbit
(f ≤ 0 at non-hit orbit points), which is Prop 4's "hole" condition.

**Prop 4 (margin theorem for any single-orbit rate; PROVED, abstract).** Let z₁, …, z_N be points of a probability space
(X, μ), H ⊂ {1, …, N} the hit indices, and suppose |N⁻¹ Σ_i f(z_i) − ∫f dμ| ≤ ε·S(f) for all f in a class 𝓕. If f ∈ 𝓕
satisfies f(z_i) ≤ 0 for i ∉ H and f ≤ 1 on hits, then ∫f − ε S(f) ≤ |H|/N. If moreover S(f) ≥ c‖f‖_∞ then
μ(supp f⁺) ≥ ∫f/‖f‖_∞ > cε whenever f certifies (∫f > εS(f)).
*Proof.* N(∫f − εS(f)) ≤ Σ_i f(z_i) ≤ |H|. And ∫f ≤ ‖f‖_∞ μ(supp f⁺). ∎
*Application (PROVED relative to Burrin Thm 1.1 and the elementary bound R(n) ≪ n^{1/3+o(1)}, Z52D_HYPERBOLA Thm 1).* For
Hecke/Farey points of level p (N = p − 1, ε ≍ p^{−1/2+θ+ε}, S = S_{2,2}, which dominates c_K‖·‖_∞ on functions supported
in a fixed compact K by Sobolev embedding in dimension 2 — the second conclusion is used only for such f), any certifying
test function satisfies 0 < ∫f − εS(f) ≤ p^{−2/3+o(1)}, i.e. it beats the rate by a *relative* margin ≤ p^{−1/6−θ+o(1)}/S(f),
while its positive support has measure > cε ≍ p^{−1/2+θ} and contains at most R(p) ≤ p^{1/3+o(1)} orbit points (all hits).
So a certificate must (i) use the rate with its explicit constant, saturated to relative precision p^{−1/6}, and
(ii) find a region of measure ≫ p^{−1/2+θ} that the orbit under-visits by a factor ≥ p^{1/6+θ−o(1)} except at hits — an
orbit **big hole** in Sarnak's sense, located next to the hits. Identifying such a hole is knowing where the hits are.
(Assessment: not a usable route. With the true R ≍ log²p the margin is ≤ p^{−1+o(1)}.)

**Prop 5 (the covering scale; Assessment on a definition).** In covering-exponent language, the hit set of (D-hit) has
relative measure (#hits)/N, and every (★)-hit certificate through an encoding with fibres ≤ p^{o(1)} must cover a target of
relative measure N^{−1}(log N)^{2+o(1)} — the *polylog* scale, below even the optimal exponent K = 1 (which allows targets of
measure N^{−1+δ}, δ > 0 fixed). The "almost every target" results (Sarnak's letter (b); Ghosh–Gorodnik–Nevo, almost-every
orbit κ = 1 per Nevo's ICTS slides, not re-read) are second-moment statements over a family of targets; a single target
needs an every-target statement, and the known every-target exponent is 2 (square-root), with big holes forcing > 1 in the
arithmetic examples. FRONTIER B4 already shows that raising fibre multiplicity in group-orbit recipes cancels in the
relative measure. The research subagent found no theorem or conjecture asserting polylog-scale covering of a *single*
arithmetic orbit (searched: single Hecke orbit covering, closed horocycle shrinking targets, Kloosterman set covering).

## 6. Escape hatches (each with a verdict)

* **(E1) Thickened target that still forces a hit.** A thickening T′ ⊃ T works for Weil only if |T′| ≳ 2p^{3/2} (Prop 3)
  and for any rate only if T′ ∩ orbit ⊂ hits (Prop 4) — so T′ must be an orbit hole. Pigeonhole thickening (two orbit
  points close ⟹ combine) yields signed solutions only (FRONTIER B4, LONGSHOT_PIGEONHOLE). Torus-multiplicativity of O_p
  ((x, x̄)(y, ȳ) = (xy, x̄ȳ)) does not preserve the shells (c(xy) is not a function of c(x), c(y)). **Closed.**
* **(E2) A different orbit with high multiplicity.** The positive points of the ES surface are finite for each n and the
  (★) surface 4uBC − u − B = n is linear in each variable (no Vieta involutions), so no infinite arithmetic group acts on
  solutions; every orbit is auxiliary and the hit set is a fibre-weighted image of ≤ R(n) solutions. Double-coset
  thickening (Γ_∞γΓ_∞ inside {γ₂₁ = p}) multiplies hits and candidates by the same factor (B4's cancellation, checked:
  the (★) condition is not double-coset invariant, so a solution occupies one element per coset). Hecke trees at fixed p
  (level p^k) encode ES(p^k), not ES(p) (ES(p) ⟹ ES(pm), not conversely). **Closed (scoped: encodings whose candidates
  are parametrised with p^{o(1)} multiplicity).**
* **(E3) The QNR half-orbit (the only place T1 is visible).** **Prop 6 (PROVED).** For n ≡ 1 (4):
  Σ_x χ_n(x) 1_{T_n}(x, x̄) = −R°(n); hence R°(n) = ½Σ_x (1 − χ_n(x)) 1_{T_n}(x, x̄) and, for n = p prime,
  −R°(p) = Σ_ξ \hat{1_{T_p}}(ξ)·Sal(ξ) with Sal(0, 0) = Σ_x χ_p(x) = 0. *Proof.* Lemma 2 (every T-point of the orbit has
  χ_n = −1), then Fourier expansion. ∎ So the half of the problem that sees T1 is a sum with **no main term**: an argument
  through it must prove a *sign* for a pure oscillatory (Salié-weighted) sum, which no rate provides; at n = m², χ_n ≡ 1
  and the identity forces R° = 0 (T1 recovered). The Salié sums are explicit (supported on hk ∈ squares), but explicitness
  does not create positivity: |Sal| = 2√p or 0, and Prop 3's argument applies verbatim with 2√p. This is the orbit form
  of FRONTIER §2.2's BM class (inv_p α = χ_{−4uB}(p)). **Closed (as an equidistribution route).**
* **(E4) Symmetry averaging.** Second-moment ("almost all targets") arguments need a family of targets whose hit counts
  are tied to the one we want. (i) The torus t·(x, y) = (tx, t⁻¹y) preserves O_p, so O_p ∩ tT_p = t(O_p ∩ T_p) and every
  torus translate has exactly R°(p) hits (PROVED, one line). But then Σ_t #(O_p ∩ tT_p)² = (p−1)R°(p)² identically —
  the second moment over the stabiliser is a tautology and carries no information unless computed independently (which
  is the Weil/spectral bound again). (ii) The full group ((𝔽_p)^×)² acts, and #(O_p ∩ (a, b)T_p) depends only on λ = ab:
  it equals #({xy ≡ λ⁻¹ (mod p)} ∩ T_p), the count for a *different* hyperbola; a variance bound over λ gives "most
  λ" (a parameter attached to p — B6), never λ = 1. Averaging over p is B6. **Closed.**
* **(E5) Cancellation over the spectrum.** The error term for Hecke points is Σ_φ ⟨1_Ω, φ⟩ λ_φ(p)(p^{1/2} + p^{−1/2})⁻¹φ(z₀);
  beating termwise bounds requires cancellation of λ_φ(p) over φ against the target's spectral coefficients, which by
  Kuznetsov becomes sums of S(·, p; c) over moduli c — a single-p statement averaged over the modulus. This is the trace-
  formula hatch (lane TRACE), not a dynamics statement; this lane records the pointer and does not pursue it.
  **Open, owned elsewhere.**
* **(E6) Linear orbits.** The only single orbits with polylog-scale discrepancy are linear ones (Kronecker/Korobov
  lattices with bounded partial quotients: discrepancy (log N)/N). The Farey points A/n *are* a perfect linear orbit, but by
  Lemma 1″ the target is a countable measure-zero set (exact HJ length 3), and by Lemma 1′ the natural structure of the hit
  condition is multiplicative (divisors of cn + 1). Encoding a tied divisor event through a linear orbit with a
  bounded-complexity target would by itself be a new idea at B2. **No candidate found.**

## 7. Bottom line, verdict, screens, proposed FRONTIER text

**Verdict: narrowed.** What is new (all internal):
1. Exact single-orbit encodings of (★): Kloosterman torus orbit (Lemma 1), shell = divisor set of cn + 1 (Lemma 1′), Farey/
   Hecke points via HJ length 3 with 4 | middle letter (Lemma 1″). CERTIFIED checks.
2. T1 in orbit terms: hits lie on the QNR half-orbit, empty exactly at squares; on it the main term vanishes (Lemma 2,
   Prop 6).
3. The missing exponent is exactly 1/2 and intrinsic for the torus orbit (Prop 3 + Lemma 3 + Cor 3, PROVED, with
   explicit constants); for any rate, certificates have margin ≤ R(p)/N and need an orbit big hole (Prop 4).
4. Literature: Burrin (Math. Ann. 2022) Thm 1.1 is the sharpest verified single-n rate for Farey/Hecke points of level n:
   n^{−1/2+7/64+ε}.

**Screens.** T1: passes as a *location* (QNR half-orbit) but no route through it (zero main term). 8/131 (F2): fails —
dynamics does not distinguish C parity. Tied modulus: the encoding makes the tie explicit (Lemma 1′) and inherits it.
Fixed p: all statements are at fixed p; the rate-based ones fail by p^{1/2}.

**Proposed FRONTIER text (for §6 dead ends; do not edit FRONTIER here):**
> *Single-orbit equidistribution (z60 DYNAMICS, `Z60_DYNAMICS.md`).* R(p) = #(O_p ∩ T_p) + boundary exactly, O_p the
> Kloosterman set (split-torus orbit, Farey/Hecke points of level p), T_p an explicit target of ≤ p(1 + log p)² grid
> points (measure N^{−1+o(1)}). Weil-completion certificates need ≥ 2p^{3/2}(1 − o(1)) target points (PROVED; the √p is
> optimal by Parseval), so the missing exponent is exactly 1/2; for any single-orbit rate a certificate's margin is
> ≤ R(p)/N and requires an orbit big hole (PROVED, abstract). Hits lie on the QNR half-orbit {χ_p(x) = −1}, empty at odd
> squares, where the main term vanishes (Salié). Best verified rate for Hecke/Farey points: n^{−1/2+7/64+ε} (Burrin 2022,
> Thm 1.1). Does NOT rule out: spectral cancellation over φ at fixed p (Kuznetsov / TRACE), or a non-equidistribution
> mechanism that locates orbit holes.

**Bottom line.** Casting R(p) as a single long orbit is exact and clean but adds no force: the orbit (Kloosterman set,
Hecke points, Farey points — all the same object) has N ≍ p points and its hits form a target of relative measure
≍ (log p)²/p, while the best possible rate for this orbit in the natural Fourier norm is p^{−1/2} (provably), and the best
verified rate in Γ\ℍ is p^{−1/2+7/64+ε}. Even the optimal covering exponent would leave a p^{δ} gap; the needed statement is
polylog-scale covering of one arithmetic target, which no theorem or standard conjecture provides. The T1 obstruction sits
on the QNR half-orbit, where there is no main term at all. Any future dynamics attempt must bring either spectral
cancellation at fixed p (trace-formula side) or a structural description of orbit holes — both of which are, in
disguise, the tied-modulus event B2.

## 8. Reproduction
* `python3 scripts/z60_dynamics_orbit.py 409 577 … 4545` → `data/z60/dynamics/orbit_check.txt` (Lemmas 1, 2; |T_n|).
* `python3 scripts/z60_dynamics_rates.py hj …` → `hj_check.txt` (Lemma 1″).
* `uv run --with numpy python scripts/z60_dynamics_rates.py weil 409 1009 2017 4001` → `weil_check.txt` (Cor 3, Lemma 3).
* `python3 scripts/z60_dynamics_rates.py disc 10000 14000` and `disc 100000 104000` → `disc_stats.txt` (§3 EVIDENCE).
All with `ulimit -v 4000000`, `timeout ≤ 1500`, single process.

## 9. Review log
(pending hostile internal review)
