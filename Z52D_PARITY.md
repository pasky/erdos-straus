# Z52D_PARITY — cluster C3 (rank O) = A14/A15 (rank A): parity / involution / group-action forcing

**ES is OPEN; nothing here proves or claims it.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED (computer) / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only (review note at the end).
Scripts: `scripts/z52d_parity_*`. Data: `data/z52d/parity/`.

## 0. Bottom line

* **Task 1 (lemma). INVOLUTION_ES2 Thm 6.1 / Cor 6.2 ((J)2) extend to finite groups acting on the O152 set X(p) in the
  sense of the §2.1 Definition (every group element acts by a fixed finite affine menu).** For two of the rules the
  result is stronger and unconditional. The idea: on generic points (off a fixed proper closed set Z), every element of
  the group acts as id or as the swap ρ (Lemma A). So generic orbits have size ≤ 2, and generic stabilisers have index
  ≤ 2 (Lemma B). Consequences:
  * (Thm C, **PROVED, unconditional: Dirichlet for infinitude, PNT in fixed arithmetic progressions for natural density; no H or Bateman–Horn**) Covered: the fixed-point rule with a
    certificate subgroup K ⊆ Γ^{(2)} := ⟨γ² : γ ∈ Γ⟩, and the Wielandt orbit rule (Z3101) with modulus m ≥ 3, or with any
    m when Γ = Γ^{(2)}. This includes ℤ/3, every odd-order Γ, and A₃ ⊂ S₃. Each such windmill fails on a set of primes
    p ≡ 1 (24) of positive relative density, whatever existence argument it uses.
  * (Thm D, **PROVED reduction**) Covered: the fixed-point rule with K ⊄ Γ^{(2)} and an odd count |Fix K|, and the orbit
    rule with m = 2. These give exactly INVOLUTION_ES Thm 5.1's conclusion E(p) ∩ Z ≠ ∅, so (J)2 Thm 6.1 / Cor 6.2 apply
    verbatim with the same labels: barred CONDITIONAL on Bateman–Horn (BH-order lower bound for the quantitative
    count; see the §2.6 caveat on the parent's 6.1(d) wording), unconditionally when Z has no Siegel-cylinder
    component. ℤ/2, S₃ with a transposition, and S₃ itself land here. Here the result is (J)2 again, nothing stronger.
  * Not covered (§2.8): count congruences that do not come from the action (e.g. |Fix K| ≢ 0 mod 3, K ⊄ Γ^{(2)}, from an
    external formula), subsets of X, other coordinate systems, non-affine maps and infinite menus.
* **Task 2 (falsifier). No 2-power class-group signal detected in certificate parities (EVIDENCE: 719 781 primes
  p ≡ 1 (24) ≤ 10⁸, plus a pre-registered replication on 664 109 primes in (10⁸, 2·10⁸]).** The tested bits are R(p)/2,
  f_II/2 (= unordered Type II count), the number of bichromatic forest edges, |E(p)|, and the number of forest edges, each
  mod 2. None of them is predicted by [8 | h(−4p)], [16 | h(−4p)], or h(−4p)/4 mod 4, after stratifying by p mod 16 or by
  p mod 6160.
  * ≤ 10⁸: max |z| = 2.80 over 30 tests. The Bonferroni threshold is 3.14, or 3.34 if both stratifications are counted.
    None of the five largest deviations replicates on the second range (consistent with fluctuations).
  * Pooled ≤ 2·10⁸ (1 383 890 primes): every class-bit |log OR| ≤ 0.0074, and every nominal (asymptotic, per-test) 95 % interval lies within ±0.017.
  * Non-congruential controls (quartic character of 3, cubic character of 2) and a random bit behave the same way.
  * Stratum-heterogeneous and twisted laws (mod primes 13…47) show nothing either.
  * **CERTIFIED (bounded scope):** no bit is a function of (p mod M, h(−4p) mod 16) for any M | 6160 on primes ≤ 10⁷ (each of the 1 920 classes
    contains both values), and the same holds on (10⁸, 2·10⁸].
* **Verdict: narrowed.**
  * On X with finite affine menus, the Z3101 escape is dead (theorem) for both rules of Thm C: K ⊆ Γ^{(2)}, and orbit
    modulus m ≥ 3.
  * The class-number-parity source (Z3094) shows no detectable signal for the tested bits (EVIDENCE; not a universal
    obstruction).
  * What survives is unchanged from (J)2: ℤ/2 forcing on auxiliary sets other than X, with non-affine maps or infinite
    menus, and the n-dependent SL₂ group; also existence counts that do not come from the action.
  * A14/A15's "no concrete object" remains the real obstruction.

## 1. Statements attacked

* **S1 (Lemma; Ranking O "C3 Lemma", Z3101).** Does (J)2 Thm 6.1 (no finite affine involution menu on X proves ES) extend
  verbatim to ℤ/3, S₃ and general finite groups acting by affine maps? **Answered: §2.** It extends for action-derived rules. For
  K ⊆ Γ^{(2)} and for orbit modulus m ≥ 3 it becomes unconditional (Thm C); the parity case is verbatim (Thm D). Labels
  as stated there.
* **S2 (Falsifier; Ranking O "C3 Falsifier", Z3094, Z0565, Z0881, Z0959).** For p ≡ 1 (24), do [8 | h(−4p)]
  (Barrucand–Cohn: ⟺ p = x² + 32y²) and h(−4p) mod 16 correlate with certificate parities after conditioning on p mod 16?
  A correlation would be the first M5 input seeing more than congruence data. **Answered: §3, no (EVIDENCE).**

Prior repo work, not redone: INVOLUTION_ES (O158), INVOLUTION_ES2 (O162), WINDMILL(_REDUCTION), PARITY_FIXED_P. Z0881 and
`WINDMILL_REDUCTION.md:154` had already reported that h(−4p) mod 16 has no effect on residual *log counts*, and no effect on
≈ 45:55 splits of windmill invariants. The *parity* correlation asked for here was not in the repo (`git grep`).

## 2. Task 1: finite groups acting by finite affine menus on X

### 2.1 Setting (as INVOLUTION_ES §4, INVOLUTION_ES2 §1)

`X(n) = {(t,u,v) ∈ ℤ³_{≥1} : P = tuv − u − v = n}`, `A = tu − 1`, `B = tv − 1`, `E(n) = {x ∈ X(n) : 4 | A}` (ES part),
`ρ(t,u,v) = (t,v,u)`. For a prime p ≡ 1 (4): `x₀ := (p+2,1,1)` is the unique ρ-fixed point of X(p), so |X(p)| is odd
(INVOLUTION_ES Lemma 2.1 / Prop 2.3(iii)), and `x₀ ∉ E(p)` since A = p + 1 ≡ 2 (4).

**Definition (finite-menu group family).** F is a set of primes p ≡ 1 (4). For each p ∈ F, a finite group Γ_p acts on
X(p). There is a fixed finite list 𝓜 = {g₁, …, g_r} of affine maps `g_i(x) = A_i(n)x + β_i(n)`, with coefficients
in ℚ(n), such that for every p, every γ ∈ Γ_p and every x ∈ X(p), `γ·x = g_i(x)` for some i, with the coefficients
evaluated at n = P(x) = p. The pieces (which i is used where) are arbitrary, as in INVOLUTION_ES §4.
*Remark.* Suppose Γ is one fixed finite group generated by finitely many elements, each acting by a finite menu. Then
every element is a word of length < |Γ| in the generators. All points of a word's trajectory stay at level p, so the
element acts by a map from the finite list of all such words. These words are again affine maps with coefficients in
ℚ(n), so the definition holds with 𝓜 = all words of length < |Γ|. Γ_p may also vary with p, as long as 𝓜 is fixed.
The same applies in the `(A,B,t)` coordinates with n-independent menus, since words of n-independent maps are
n-independent.

**Certificate rules.** For all but finitely many p ∈ F, one of the following holds.
* **(R1) fixed-point rule.** For a subgroup 1 ≠ K_p ≤ Γ_p: `Fix(K_p) ⊆ E(p)`, together with some argument that
  Fix(K_p) ≠ ∅. Examples: Zagier/O158 (Γ = K = ℤ/2); Sylow-type, with K an ℓ-group and |X(p)| ≢ 0 (mod ℓ) giving
  |Fix K| ≡ |X| ≢ 0.
* **(R2) Wielandt orbit rule (Z3101).** An integer m_p ≥ 2 such that every Γ_p-orbit of size ≢ 0 (mod m_p) meets E(p),
  together with |X(p)| ≢ 0 (mod m_p). Then some orbit has size ≢ 0 (mod m_p), so E(p) ≠ ∅.

Write `Γ^{(2)} := ⟨γ² : γ ∈ Γ⟩`. It is the intersection of all subgroups of index ≤ 2. It contains every element of odd
order (γ = (γ^{(k+1)/2})² when γ^k = 1 with k odd).

### 2.2 Lemma A (INVOLUTION_ES Lemma 4.1 for bijections; PROVED)

Let `Z₀, Z₁, Z₂` and the finite exceptional level set 𝔈 be as in INVOLUTION_ES Lemma 4.1, built from the menu 𝓜, and put
`Z := Z' ∪ ρ(Z')` with `Z' := Z₀ ∪ Z₁ ∪ Z₂`. This is a proper closed set, ρ-invariant, and depends on 𝓜 only. Then for
every p ∈ F ∖ 𝔈 and every `x ∈ G(p) := X(p) ∖ Z`, every γ ∈ Γ_p satisfies `γx ∈ {x, ρx}`, and G(p) is Γ_p-invariant.

*Proof.* Let γ ∈ Γ_p and let g ∈ 𝓜 be the map used by γ at x. Since P(g(x)) = P(γx) = p = P(x) and x ∉ Z₀, g is a
symmetry of P. Suppose g were degenerate. Then y := γx lies in the image of g at its own level P(y) = p, so y ∈ Z₁. Now
γ⁻¹ ∈ Γ_p also acts by 𝓜. If g' ∈ 𝓜 is used by γ⁻¹ at y, then `x = γ⁻¹y = g'(y) ∈ g'(Z₁) ⊆ Z₂`, contradicting x ∉ Z.
(This is the only change from Lemma 4.1. There, σ⁻¹ = σ; here γ⁻¹ is a different element with the same menu.) So g is an
invertible symmetry. By INVOLUTION_ES Prop 4.2(b), the invertible affine maps with coefficients in ℚ(n) that preserve
`{tuv − u − v = n}` for n ≠ 0 are exactly id and ρ. This classification applies to every element of 𝓜, words included.
So γx ∈ {x, ρx}. Both points lie outside Z because Z is ρ-invariant. ∎

(In the `(A,B,t)` coordinates with n-independent menus, use INVOLUTION_ES Lemma 4.1(ii) with `H = {id, ρ}` and with `Z₃`
the finitely many planes of Lemma 4.3. These are finitely many because 𝓜 contains finitely many scalings.)

### 2.3 Lemma B (structure on generic points; PROVED, elementary)

For p ∈ F ∖ 𝔈 and x ∈ G(p):
(i) the orbit Γ_p x ⊆ {x, ρx}, so `[Γ_p : Stab(x)] ≤ 2` and `Stab(x) ⊇ Γ_p^{(2)}`;
(ii) `Stab(ρx) = Stab(x)`;
(iii) for every subgroup K, `Fix(K) ∩ G(p)` is ρ-invariant;
(iv) if x₀ ∉ G(p), then |Fix(K) ∩ G(p)| is even for every K, and the points of G(p) lying in Γ_p-orbits of odd size
(= size 1) are even in number.

*Proof.* (i) Lemma A. An index-≤ 2 subgroup is normal with quotient of exponent ≤ 2, so it contains all squares. (ii) If
ρx = x there is nothing to prove. Otherwise let γx = x. Then γ(ρx) ∈ {ρx, x} by Lemma A applied to ρx ∈ G(p), and
γ(ρx) = x = γx would contradict injectivity, so γ(ρx) = ρx. The converse follows by symmetry (ρρx = x). (iii) follows from
(ii). (iv) ρ is a fixed-point-free involution of G(p) (its only fixed point on X(p) is x₀). Both sets in question are
ρ-invariant by (ii)/(iii): a size-1 orbit {x} has Stab(x) = Γ_p = Stab(ρx). ∎

### 2.4 Lemma D (generic non-certificate pairs; PROVED, unconditional: Dirichlet / PNT in fixed APs)

Let Z ⊊ 𝔸³ be closed and ρ-invariant. There exist t ≡ 1 (4) and u ≡ 23 (24), t, u ≥ 1, such that the axis line
`ℓ = {(t,u)} × 𝔸¹ ⊄ Z`. For such (t,u), put q := tu − 1, L := lcm(24, 4q), and let 𝒫 be the set of primes p ≡ 1 (24)
with p ≡ −u (mod 4q). Then:
(a) 𝒫 has relative density φ(24)/φ(L) > 0 among the primes ≡ 1 (24);
(b) for p ∈ 𝒫, `x_p := (t, u, (p+u)/q) ∈ X(p)`, and neither x_p nor ρx_p lies in E(p);
(c) x_p ∉ Z, hence ρx_p ∉ Z, for all but finitely many p ∈ 𝒫.

*Proof.* Existence. The set `C := {(t,u) : ℓ_{t,u} ⊆ Z} = ⋂_{v} {(t,u) : (t,u,v) ∈ Z}` is Zariski-closed in 𝔸², and
C ≠ 𝔸² because Z ≠ 𝔸³. The set S = {t ≡ 1 (4)} × {u ≡ 23 (24)} of positive integers is Zariski-dense in 𝔸²: a polynomial
vanishing on S vanishes, for each of infinitely many t, at infinitely many u, so each of its coefficients (as a polynomial
in u) has infinitely many roots t. Hence S ⊄ C.
(a) t ≡ 1 and u ≡ 3 (mod 4) give q ≡ 2 (mod 4), and gcd(u, q) = 1 (as tu − q = 1). So gcd(24, 4q) = 8·gcd(3, q)
divides 24. Since −u ≡ 1 (mod 24), the two congruences are compatible, and the joint class r mod L is reduced: r ≡ 1 (mod 24)
is prime to 2 and 3, and every odd prime ℓ | q has r ≡ −u ≢ 0 (mod ℓ), because gcd(u, q) = 1. Dirichlet gives infinitely many such primes, and the prime number theorem in fixed arithmetic progressions gives the natural density φ(24)/φ(L) relative to p ≡ 1 (24).
(b) 4q | p + u, so v := (p+u)/q is a positive integer ≡ 0 (mod 4), and `tuv − u − v = (q+1)v − u − v = qv − u = p`.
At x_p, A = q ≡ 2 (mod 4), so x_p ∉ E(p). At ρx_p = (t, v, u), A = tv − 1 ≡ −1 (mod 4), so ρx_p ∉ E(p).
(c) ℓ is irreducible and ℓ ⊄ Z, so ℓ ∩ Z is finite. The x_p are distinct points of ℓ, and Z is ρ-invariant. ∎

CERTIFIED sanity check (`uv run --with sympy python scripts/z52d_parity_lemmaD_check.py 3000000`): for (t,u) = (1,23),
(5,23), (1,47), (9,71), (13,95), every p < 3·10⁶ in 𝒫 satisfies (b). The observed relative frequencies are 0.1001,
0.0562, 0.0455, 0.0035, 0.0014, against φ(24)/φ(L) = 0.1000, 0.0556, 0.0455, 0.0036, 0.0016.

### 2.5 Theorem C (the rules K ⊆ Γ^{(2)} and orbit modulus m ≥ 3 are barred unconditionally; PROVED)

Let (Γ_p)_{p∈F} be a finite-menu group family on X, and let Z be its set from Lemma A. Suppose that for all but finitely
many p ∈ F, either
* (R1) holds with `K_p ⊆ Γ_p^{(2)}`, e.g. |K_p| odd: Γ = ℤ/3, ℤ/ℓ (ℓ odd), K = A₃ ⊂ S₃, any Sylow ℓ-subgroup with ℓ odd,
  or any K in a group with no index-2 subgroup; or
* (R2) holds with `m_p ≥ 3`, or with any m_p ≥ 2 when `Γ_p = Γ_p^{(2)}`.

Take (t,u) and 𝒫 from Lemma D for this Z. Then **F contains only finitely many primes of 𝒫**. In particular F omits a set
of primes p ≡ 1 (24) of positive relative density, and no such windmill proves ES for all large p ≡ 1 (24). No hypothesis
is used beyond Dirichlet's theorem and the prime number theorem in fixed arithmetic progressions (for the density), and the existence half of the windmill is never used.

*Proof.* Let p ∈ 𝒫 ∩ F lie outside the finitely many exceptions: 𝔈, the p with x_p ∈ Z (Lemma D(c)), and the p where
(R1)/(R2) fail. Then x_p ∈ G(p).
* Under (R1): Stab(x_p) ⊇ Γ_p^{(2)} ⊇ K_p by Lemma B(i), so x_p ∈ Fix(K_p) ⊆ E(p). This contradicts Lemma D(b).
* Under (R2): the orbit of x_p has size 1 or 2 (Lemma B(i)). If Γ_p = Γ_p^{(2)} it has size 1. In either case the size is
  ≢ 0 (mod m_p), so the orbit, contained in {x_p, ρx_p}, meets E(p). This also contradicts Lemma D(b). ∎

### 2.6 Theorem D (the parity case is exactly (J)2; PROVED reduction, then (J)2's labels)

Same family. Suppose that for all but finitely many p ∈ F, either
* (R1′) `Fix(K_p) ⊆ E(p)` and |Fix(K_p)| is odd, e.g. K_p a 2-group (Sylow congruence |Fix K| ≡ |X(p)| ≡ 1 (mod 2)); or
* (R2′) (R2) with m_p = 2, i.e. every odd-size orbit meets E(p). (Existence is automatic, since |X(p)| is odd.)

Then `E(p) ∩ Z ≠ ∅` for all but finitely many p ∈ F. This is the conclusion of INVOLUTION_ES Thm 5.1, with Z fixed
(depending only on 𝓜; Z₃ = ∅ in the (t,u,v) coordinates, finitely many fixed planes in (A,B,t)). Hence **INVOLUTION_ES2 Thm 6.1 and Cor 6.2 apply verbatim**:
* (PROVED) F omits 100 % of the primes p ≡ 1 (mod α₀) if Z has no Siegel-cylinder component;
* (CONDITIONAL on H) F omits infinitely many p ≡ 1 (24) if every 2-dimensional component of Z is an axis cylinder;
* (CONDITIONAL on a Bateman–Horn-order lower bound `#{admissible y ≤ Y} ≫ Y/(log Y)^{|S|}` for the family of
  INVOLUTION_ES2 Thm 5.3) F omits ≫ N/(log N)^{|S|} primes p ≡ 1 (24) up to N, for every menu. This follows from
  INVOLUTION_ES2 Thm 6.1(a) by subtracting the O(N^{2/3}) exceptional set 𝔈_Z.
  **Caveat (cross-review, inherited from the parent):** INVOLUTION_ES2 Thm 6.1(d) states its hypothesis "precisely" as
  the weaker bound `> C_Z·(24MY)^{2/3}`. That weaker bound gives only infinitely many omitted primes. An assumed bound
  ≫ Y^{2/3+δ} gives a correspondingly weaker count. Neither gives the BH-order count ≫ N/(log N)^{|S|}. The two forms are
  conflated in the source. Here the BH-order form is assumed for the quantitative conclusion; the parent's 6.1(d) wording
  should be repaired (flagged for the FRONTIER/STATUS maintainer, not propagated as a theorem).

*Proof.* (R1′) x₀ is ρ-fixed, so if x₀ ∈ G(p) its orbit is {x₀}. Then x₀ ∈ Fix(Γ_p) ⊆ Fix(K_p) ⊆ E(p), which is false.
So x₀ ∈ Z. By Lemma B(iv), |Fix(K_p) ∩ G(p)| is even. Hence |Fix(K_p) ∩ Z| is odd, and ∅ ≠ Fix(K_p) ∩ Z ⊆ E(p) ∩ Z.
(R2′) Again x₀ ∈ Z: otherwise {x₀} is an odd orbit, so it meets E(p), which is false. Odd-size orbits contribute an odd
total to |X(p)|, since even orbits contribute even amounts and |X(p)| is odd. The odd-orbit points inside G(p) are even in
number (Lemma B(iv)), and G(p) and X(p) ∩ Z are both Γ_p-invariant. So some odd orbit O lies in X(p) ∩ Z, and O meets
E(p). ∎

### 2.7 Answer to S1, case by case

| action / rule | generic behaviour (Lemma B) | status |
|---|---|---|
| ℤ/2, certificates = Fix (Zagier/O158) | pairs {x, ρx} | (J)2 Thm 6.1 as before (CONDITIONAL on BH) |
| **ℤ/3**, ℤ/ℓ (ℓ odd), any odd-order Γ; rules (R1), (R2) any m | acts **trivially** on G(p) | **barred, unconditional** (Thm C) |
| **S₃**, K = A₃ (3-cycles) | A₃ ⊆ Γ^{(2)} fixes G(p) | **barred, unconditional** (Thm C) |
| S₃, K = ⟨(12)⟩ or K = S₃, mod-2 existence | through sign character | verbatim (J)2 (Thm D) |
| general Γ, K ⊆ Γ^{(2)} (e.g. any K in a perfect Γ such as A₅; K = V₄ ⊂ A₄) | K acts trivially on G(p) | **barred, unconditional** (Thm C) |
| general Γ, K ⊄ Γ^{(2)}, mod-2 existence | through Γ → Γ/Γ^{(2)} | verbatim (J)2 (Thm D) |
| general Γ, K ⊄ Γ^{(2)}, existence by an external count mod an odd m | — | **not covered** (§2.8) |
| Wielandt orbit rule, m ≥ 3 (Z3101) | orbits of size ≤ 2 | **barred, unconditional** |
| Wielandt orbit rule, m = 2 | — | verbatim (J)2 |

**Why parity is special (Assessment).** Lemma A says that a finite-menu action only sees the symmetry group of the level
function on generic points. For tuv − u − v that group is {id, ρ} ≅ ℤ/2. Thm C's rules (certificates on points fixed by
squares, or in every orbit of size ≢ 0 mod m ≥ 3) therefore force every generic point, or every generic ρ-pair, to
carry a certificate, and Lemma D refutes that. Only the ℤ/2 case leaves room: that is the parity bookkeeping of Thm 5.1, which localises the
certificate on the fixed surface Z. The general principle: in coordinates whose level function has a finite symmetry
group H, generic orbits lie in H-orbits and have size ≤ |H|. So every orbit rule with modulus m > |H| forces every
generic orbit to meet the certificate set. Whether that is refutable depends on the analogue of Lemma D, which is
checked here only for X.

### 2.8 Where the extension does not reach (unchanged residue of INVOLUTION_ES §6)

* **Other auxiliary sets.** Lemma B(iv) and Lemma D use the full X(p) and its swap. Lemma A still holds on a Γ-stable
  *subset* Y(p) ⊂ X(p): generic points of Y(p) move only to themselves or their swap. But Y(p) ∖ Z need not be
  ρ-invariant. Thm C then applies only if Y(p) contains Lemma D's point x_p for a positive-density set of p. Under
  (R2), if ρx_p ∉ Y(p) the orbit of x_p is {x_p}, which must meet E(p), which is again false. Thm D's parity count fails. For arbitrary Y(p), nothing follows.
* **ES coordinates.** H = S₃ there (Prop 4.2(a)), and ℤ/3 can act freely on solutions with distinct coordinates (Z2033:
  for p ≡ 1 (4) the S₃ action on solutions is free). But there the set *is* the certificate set, so no windmill content
  arises.
* **Type II coordinates (a,b,c,k)** with n-dependent menus, the n-dependent SL₂ group of AB − nt = 1, non-affine maps,
  infinite or p-growing menus: not touched (as in (J)2).
* **Count congruences not produced by the action.** Example: |Fix K| ≢ 0 (mod 3) for K ⊄ Γ^{(2)}, known from an external
  formula. Then the certificates may be genuine generic ρ-pairs, and nothing above applies. This is not a group-action
  argument but the bare M5 problem ("a certificate count ≢ 0 mod m by a formula"), and T1 applies to it as before.

## 3. Task 2: 2-power class-group data vs certificate parities

### 3.1 The bits, and the parities that are trivial (PROVED)

All for primes p ≡ 1 (24). F_p is the word forest of FOREST_H4 (vertices 1…p+2, edge {u,v} iff u ≠ v and uv | p+u+v,
colour χ_p(v) = (v/p)).
* `NE` = #edges. **|X(p)| = 2·NE + 1** (x₀ is the only diagonal word).
* `BICH` = #bichromatic edges. For p ≡ 1 (4), bichromatic ⟺ 4 divides a slot in {t,u,v,tu−1,tv−1} (repo, PROVED;
  re-checked here on every edge of every prime ≤ 2·10⁸, 0 mismatches).
* `R2` = R(p)/2 = #edges with 4 | t. **R(p) is always even**: u ↔ B is an involution of {4uBC − u − B = p}, and a fixed
  point u = B would give u | p with u(4uC − 2) = p, impossible for u ∈ {1, p}.
* `EA` = |E(p)| = #ordered words with 4 | tu − 1.
* `UII` = f_II/2, where f_II = #{(a,b,c,d) : 4abcd = a + b + pc, gcd(a,c) = 1} (ordered (a,b); the repo convention,
  STATUS f_II(5101441) = 78, reproduced). **f_II is always even for p ≡ 1 (4)**: (a,b) ↔ (b,a) preserves the set, since
  c | a + b gives gcd(b,c) = gcd(a,c) = 1. A fixed point a = b forces a | p. Then a = 1 gives c(4d − p) = 2, impossible for
  p ≡ 1 (4), and a = p gives c(4pd − 1) = 2, also impossible. So UII is the number of unordered Type II solutions
  (checked against direct enumeration, below). Counting all six orderings of (x,y,z), this is f_II^{(6)}/6, which is the
  "f_II/6" of Ranking O; there are no diagonal solutions (Z2033).

Class bits: `b8 = [8 | h(−4p)]`, `b16 = [16 | h(−4p)]`, `hq = h(−4p)/4 mod 4`. (4 | h(−4p) always, since p ≡ 1 (8).)
Non-congruential controls: `q3` = [3 is a quartic residue], `c2` = [2 is a cubic residue] (p = x² + 27y²); `rnd` = a
seeded random bit.

**Caution found during the run.** For p ≡ 1 (8), `[8 | h(−4p)] = [2 is a quartic residue] XOR [p ≡ 9 (16)]`.
* PROVED, given Barrucand–Cohn's two criteria (§3.2): 8 | h(−4p) ⟺ (−4)^{(p−1)/8} ≡ 1 (mod p). Now
  (−4)^{(p−1)/8} = (−1)^{(p−1)/8}·2^{(p−1)/4}, and 2^{(p−1)/4} = ±1 because 2 is a square mod p.
* CERTIFIED on all 1 383 890 primes ≤ 2·10⁸.

So the quartic character of 2 is **not** an independent control once p mod 16 is fixed. It is the same test as b8, and
was replaced by q3.

### 3.2 Literature (Koymans read in full; Barrucand–Cohn original verified by the cross-reviewer)

* 8 | h(−4p) ⟺ p = x² + 32y² ⟺ (−4)^{(p−1)/8} ≡ 1 (mod p) (p ≡ 1 (8)): Barrucand–Cohn, J. reine angew. Math. 238 (1969)
  67–70. I could not open it. The cross-reviewer read the original from the Göttingen scans linked by EuDML
  (https://eudml.org/doc/183503): p. 67 eqs. (1)–(4) and p. 68 Main Theorem (6b), (6d), (6e). The hypotheses there are
  exactly p ≡ 1 (8), and the theorem states x² + 32y² ⟺ −4 an eighth-power residue ⟺ 8 | h(Q(√−p)), whose discriminant
  is −4p. No congruence hypothesis is missing. Earlier secondary sources (search snippets only) agree:
  * Cohn–Lagarias, Math. Comp. (1983) (JSTOR 2007707), eq. (1.3);
  * the note "The forms x² + 32y² and x² + 64y²" (scispace).
* Koymans, ANT 14 (2020) 37–65
  (arXiv:1809.07167, read): Q(ζ₈, √(1+i)) is a governing field for the 8-rank, and p splits completely there iff 8 | h(−p);
  Hasse's criterion is quoted. **CERTIFIED here:** [8 | h(−4p)] = [p = x² + 32y²] on all 82 887 primes p ≡ 1 (24) ≤ 10⁷
  and on every 10th one up to 10⁸ (146 577 checks, 0 mismatches).
* 16-rank: Koymans (loc. cit., Thm 1.1, read) proves unconditionally that 16 | h(−p) has density 1/16 among all primes.
  Among p ≡ 1 (24) the *expected* share is 1/4. That is not stated in Koymans for progressions mod 3; it is observed here
  (0.2499 / 0.2502 on the two ranges). Koymans also states (as of that paper; not a survey of later work) that **no** value of d is known for which a governing
  field for the 16-rank exists or fails to exist. Cohn–Lagarias conjectured that they always exist. **Correction to Ranking
  O's C3 note** ("the 16-rank has no governing field"): the correct statement is "no governing field is *known*". The
  16-rank is still a non-congruential (non-abelian Chebotarev, if a governing field exists) parity source.

### 3.3 Computation (exact commands)

```
gcc -O2 -o /tmp/z52d_parity_counts scripts/z52d_parity_counts.c -lm
/tmp/z52d_parity_counts 10000000 > c_1e7.txt                                         # 55 s, ~100 MB
# 1e7..2e8: 38 chunks [X0, X0+5e6], 9-12 in parallel, ~10 min per range:  /tmp/z52d_parity_counts X0+5e6 X0
#   concatenated -> data/z52d/parity/counts_1e8.txt.gz (p <= 1e8), counts_2e8.txt.gz (1e8 < p <= 2e8)
zcat data/z52d/parity/counts_1e8.txt.gz > /tmp/c1e8.txt
python3 scripts/z52d_parity_brute.py /tmp/c1e8.txt 6000                                  # independent brute force
uv run --with numpy --with scipy python scripts/z52d_parity_corr.py /tmp/c1e8.txt [PMAX] > data/z52d/parity/corr_{1e5,1e7,1e8}.txt
# same on counts_2e8 (-> corr_2e8.txt) and on the concatenation (-> corr_pooled_2e8.txt)
```
* `z52d_parity_counts.c` enumerates each edge once, from its smaller endpoint u ≤ 1 + √(p+1) and the divisors v of p + u.
  The f_II sieve is identical to `scripts/bs_prob_fII.c`. h(−4p) is computed from the reduced forms (a, 2b′, c),
  ac − b′² = p, with the usual boundary convention; all such forms are primitive for p prime.
* **Checks (CERTIFIED).** An independent Python brute force agrees on all six quantities (NE, BICH, R2, EA, f_II/2 versus
  direct enumeration of unordered Type II solutions, and h) for all 89 primes p ≡ 1 (24) ≤ 6000. The (★)-zeros R(p) = 0 up
  to 10⁸ are exactly the known 14 primes (409, …, 8 813 281), and there is none in (10⁸, 2·10⁸]. BICH ≥ 1 at every prime.
  The chunked run reproduces the single run on [5·10⁶, 10⁷] byte for byte.
* **Tests.** 2×2 Cochran–Mantel–Haenszel z-scores with strata p mod 16 and p mod 6160 = 16·5·7·11. A generalised CMH
  (df 3) for hq. b16 is also tested *given* b8, with strata (p mod 16, b8), to isolate the 16-rank from the 8-rank.
  Separately, each Y is tested against p mod M (is the bit congruential at all?). Two checks address CMH's blind spot,
  which is associations whose sign varies between strata:
  * [F] the sum over the 6160-strata (n ≥ 20) of the per-stratum 2×2 χ²;
  * [G] twisted laws: Y ⊕ Z (Z = b8, b16) against p mod ℓ, ℓ = 13…47 prime.

  Mantel–Haenszel log odds ratios carry Robins–Breslow–Greenland 95 % intervals. χ² survival probabilities are evaluated
  numerically (scipy), but the χ² null approximations and the 95 % intervals are asymptotic/nominal: they are not exact
  finite-sample guarantees and not simultaneous over tests.

### 3.4 Results (EVIDENCE; N = 719 781 primes p ≡ 1 (24), p ≤ 10⁸; `data/z52d/parity/corr_1e8.txt`)

Frequencies of all five bits: 0.4996–0.5003. b8: 0.4999, b16: 0.2499, hq uniform (0.2499–0.2503).

| Y \ Z (CMH z, strata p mod 16; MH odds ratio for p mod 6160) | b8 | b16 | b16 \| b8 | q3 (ctrl) | c2 (ctrl) | rnd | hq (χ², df 3) |
|---|---|---|---|---|---|---|---|
| R2 = R/2 mod 2 | −1.46 (0.993) | −0.49 (0.997) | +0.42 | −2.55 (0.988) | +1.14 | −0.49 | 2.34 |
| UII = f_II/2 mod 2 | −2.10 (0.990) | −0.63 (0.997) | +0.71 | −0.60 | +1.02 | −1.23 | 5.56 |
| BICH mod 2 | −0.12 (0.999) | −0.82 (0.996) | −0.92 | −1.62 | +0.51 | −0.54 | 0.98 |
| EA = \|E(p)\| mod 2 | +0.12 (1.001) | −0.28 (0.999) | −0.43 | +0.27 | +0.53 | +1.30 | 4.54 |
| NE mod 2 | +1.05 (1.005) | −1.68 (0.991) | −2.80 (0.981) | +0.25 | −1.89 | −1.74 | 10.02 |

* Stratifying by p mod 6160 instead of p mod 16 changes no z by more than 0.08.
* Largest |z| = 2.80 (NE vs b16 | b8; −2.82 with 6160-strata) among the 30 tests per range (20 [B] z-tests on b8, b16, q3,
  c2; 5 [B2]; 5 hq χ², converted to z). The Bonferroni 5 % threshold is |z| ≈ 3.14 for 30 tests, or 3.34 if both
  stratifications are counted (60). The controls q3 and rnd reach |z| = 2.55 and 1.74, i.e. the same scale. The extremes
  did not replicate (§3.5).
* Effect size: the widest class-bit 95 % interval on ≤ 10⁸ reaches |log OR| = 0.032 (NE vs b16 | b8, where only the b8 = 1
  strata carry information). On the pooled data (§3.5) all class-bit intervals lie within ±0.017. An M5 input would need a
  *forced* parity: a deterministic law, not a percent-level bias.
* Heterogeneity [F]: per-stratum χ² sums against b8, b16 and rnd have z between −1.5 and +2.0 on ≤ 10⁸, and between −2.0
  and +2.3 pooled. The random control reaches +3.2 on (10⁸, 2·10⁸], so this statistic is noisy, and no class bit stands
  out. Twisted laws [G]: 100 tests per range, largest |z| 2.6 (≤ 10⁸), 2.9 ((10⁸, 2·10⁸]) and 2.3 (pooled), each below
  the Bonferroni level 3.48 and not recurring.
* **No deterministic law (CERTIFIED):** for each of the five bits, all 1 920 classes (p mod 6160, h(−4p) mod 16) already
  contain primes with both values among p ≤ 10⁷, and again among (10⁸, 2·10⁸]. First pairs: R2 (937, 19417),
  UII/BICH/EA (433, 18913), NE (1009, 19489). This excludes every law Y = f(p mod M, h(−4p) mod 16) with M | 6160. Laws
  twisted by other moduli are excluded only statistically, by [F] and [G].
* Are the bits congruential? Against p mod 16, 5, 7, 11, 13, 560 and 6160, the χ² tests show no structure. The smallest
  p-value is BICH vs p mod 5 (p ≈ 0.003, 35 tests; replication below).
* At p ≤ 10⁵ (1 181 primes, the range in the brief) all tests are null as well (`corr_1e5.txt`). Max |z| is 2.38 (NE vs
  the control q3); among the class bits it is 2.29 (BICH vs b8), which fell to +0.08 at 10⁷ (`corr_1e7.txt`) and −0.12 at
  10⁸.

### 3.5 Replication on (10⁸, 2·10⁸] (pre-registered in `data/z52d/parity/prereg_replication.txt`, committed before the run finished)

Range: 664 109 primes p ≡ 1 (24) in (10⁸, 2·10⁸] (`data/z52d/parity/corr_2e8.txt`). Criterion: same sign and p < 0.01.

| pre-registered effect | ≤ 10⁸ | (10⁸, 2·10⁸] | replicated? |
|---|---|---|---|
| (i) NE vs b16 \| (p mod 16, b8) | z = −2.80 | z = +0.94 | no (sign flips) |
| (ii) R2 vs q3 (control) | z = −2.55 | z = +0.73 | no |
| (iii) UII vs b8 | z = −2.10 | z = +0.04 | no |
| (iv) BICH vs p mod 5 | χ² = 14, p ≈ 0.003 | χ² ≈ 0, p ≈ 0.92 | no |
| (v) NE vs hq | χ² = 10.0, p ≈ 0.018 | χ² = 1.0, p ≈ 0.80 | no |

On the new range alone, the largest |z| among the 25 class/control z-tests is 1.43. All ORs lie in [0.990, 1.010], and the
2×4 hq tests have p ≥ 0.19. One new small p-value appears: UII vs p mod 16, p = 0.0033 (not pre-registered; p = 0.80 on
≤ 10⁸). The no-deterministic-law check again finds all 1 920 classes non-constant. **Pooled** (N = 1 383 890, p ≤ 2·10⁸,
`corr_pooled_2e8.txt`): max |z| = 1.87 (BICH vs rnd), and among the class bits max |z| = 1.51 (UII vs b16 | b8). All
Mantel–Haenszel ORs for class bits lie in [0.993, 1.007], and every class-bit 95 % interval for log OR lies within ±0.017.
**Nothing replicates; the ≤ 10⁸ extremes did not replicate and are consistent with multiple-testing
fluctuations.**

### 3.6 Interpretation (Assessment)

The certificate counts are sums, over levels t, of divisor-pair counts of tp + 1 in residue classes (METAPLECTIC_ES Thm K).
The 8-rank of Cl(−4p) is Frobenius data in a known governing field, Q(ζ₈, √(1+i)). For the 16-rank a governing
field is only conjectural (Cohn–Lagarias), so it is not known to be Frobenius data in any fixed field. The data detect no
association with the tested parities (tested common-OR estimates within |log OR| ≲ 0.02, nominal intervals). This matches (J)96 ("non-abelian Frobenius inert on finite witness sets") and Z0881 (no effect on log counts).
Z3094's idea was to find a set whose size is a class number up to known even terms. Then the parity of that set's size
would be governed by h(−4p). None of the five natural ES cardinalities is such a set, even statistically. For Rédei-type
forcing it would have to be one exactly.

## 4. Verdict for C3 / A14 / A15: **narrowed**

* **Killed (theorem; "dead" only in this scope).** Finite-group forcing on the O152 set X, with every group element acting by a fixed finite affine
  menu (§2.1), under either of two rules (Thm C, unconditional: Dirichlet / PNT in fixed arithmetic progressions):
  * the fixed-point rule with certificate subgroup K ⊆ Γ^{(2)};
  * the Wielandt orbit rule with m ≥ 3 (any m if Γ = Γ^{(2)}).

  Z3101's escape "m > 2 is not covered by (J)2" is closed on X for these rules.
* **Unchanged (theorem).** The parity rules (K ⊄ Γ^{(2)} with an odd |Fix K|; orbit rule with m = 2) are (J)2 verbatim
  (Thm D): barred CONDITIONAL on Bateman–Horn (BH-order lower bound; §2.6 caveat), CONDITIONAL on H for cylinder
  exceptional sets, and unconditionally for menus without Siegel-cylinder exceptional sets.
* **Not covered.** K ⊄ Γ^{(2)} with an existence count that does not come from the action (e.g. mod 3) — this is the bare
  M5 problem. Also not covered: subsets of X, other coordinate systems, non-affine maps, infinite menus (§2.8).
* **No detectable signal (EVIDENCE; CERTIFIED non-determinism for laws of modulus dividing 6160).** The 8-rank and 16-rank
  of Cl(−4p) show no detectable association with the parity of R(p)/2, f_II/2, BICH, |E(p)| or (|X(p)|−1)/2: the tested
  common-OR estimates and their nominal 95 % intervals are within |log OR| ≈ 0.02 (pooled ±0.017). This does not exclude
  untested interactions, other class-group bits, or other auxiliary sets. The "first M5 input beyond congruence data" did not materialise.
* **Survives (Assessment, as A14/A15 say):** ℤ/2 forcing on auxiliary sets other than X, or with non-affine or growing
  menus; Smith-theory / discrete-Morse complexes (A15; no K_p is specified anywhere, and none is constructed here).
  Plausibility stays at 1 at best, with no concrete object.

## 5. Proposed FRONTIER changes (do not edit FRONTIER here)

* **§6 "Algebraic / forcing", replace the windmill bullet with:**
  "Windmills / involutions / finite-group actions on X in which every group element acts by a fixed finite affine menu:
  * the parity rules (fixed points of K ⊄ Γ^{(2)} with an odd count; Wielandt modulus m = 2) are barred CONDITIONAL on
    a BH-order lower bound ((J)2 Thm 6.1; note that 6.1(d)'s 'precise' Y^{2/3} hypothesis does not yield the stated
    N/(log N)^{|S|} count and needs rewording);
  * the fixed-point rule with K ⊆ Γ^{(2)} (ℤ/3, any odd-order K, A₃ ⊂ S₃) and the Wielandt orbit rule with m ≥ 3 are
    barred unconditionally (on the full X with a fixed common finite affine menu) on a positive-density set of
    p ≡ 1 (24), because generic orbits have size ≤ 2;
  * existence counts not coming from the action are not covered.

  → `Z52D_PARITY.md` Thms C, D."
* **§3 M5 row, append:** "; 2-power class-group data ([8 | h(−4p)], [16 | h(−4p)], h mod 16) show no detectable
  association with the parity of R/2, f_II/2, bichromatic edges, |E(p)| or (|X(p)|−1)/2 (EVIDENCE, p ≤ 2·10⁸, |log OR|
  ≲ 0.02; `Z52D_PARITY.md` §3)."
* **§7:** no entry is added or removed. C3 never had one, and nothing here creates a well-posed tractable sub-problem.
  Optional wording fix wherever the 16-rank is mentioned: "no governing field is *known*" (Koymans 2020), not "none
  exists".

## 6. Bottom line

The closing lemma holds, in a stronger form than asked for two of the rules. When every group element acts on the O152
set by a fixed finite affine menu, the action on generic points can only go through the swap u ↔ v. The following
therefore fail unconditionally on a positive proportion of primes ≡ 1 (24):
* ℤ/3-windmills;
* S₃-windmills certified through its 3-cycles;
* windmills certified at points fixed by squares;
* Wielandt-type orbit rules with modulus m ≥ 3.

The parity rules are exactly the (J)2 case (barred under a BH-order lower bound; the parent's weaker
"precise" 6.1(d) hypothesis does not give that count, §2.6). Existence counts from outside the action stay
open.

The falsifier is clean. It covered 719 781 primes p ≡ 1 (24) up to 10⁸, plus a pre-registered replication on 664 109
primes in (10⁸, 2·10⁸]. Once p mod 16 (or p mod 6160) is fixed, none of [8 | h(−4p)] (Barrucand–Cohn), [16 | h(−4p)] or
h(−4p) mod 16 detectably predicts the parity of any of the five natural certificate counts. The tested common-odds-ratio
estimates are within 2 % of 1 (nominal 95 % intervals), the non-abelian controls behave identically, and no law
Y = f(p mod M, h(−4p) mod 16) with M | 6160 holds (CERTIFIED). This does not rule out untested interactions, other
class-group invariants, laws with other moduli, or an auxiliary set built differently.

Cluster C3 is narrowed. Its group-theoretic generalisation is dead only for Thm C's rules, on the full X with a fixed common finite
affine menu. The parity case keeps its conditional residue, and the class-number experiment is negative evidence, not a
universal obstruction. What remains is the A14/A15 residue: an unconstructed auxiliary set or complex. ES remains open.

## 7. Review

* **Hostile review 1** (subagent, 2026-11-01): no FATAL. The §2 proofs (Lemmas A, B, D; Thms C, D) were checked step by
  step against INVOLUTION_ES / INVOLUTION_ES2, and found correct, including Cor 6.2 applicability. The reviewer
  independently recomputed:
  * both prime counts (719 781, 664 109);
  * NE, BICH, R2, EA, f_II/2 and h(−4p) for 46 primes ≤ 3000 (h from the analytic class-number formula);
  * the 14 (★)-zeros;
  * the Barrucand–Cohn equivalence and the quartic-2 identity on 18 507 primes ≤ 2·10⁶;
  * the Lemma D densities;
  * every table number.

  There was **1 MAJOR** finding: the scope was overclaimed ("every group and rule except parity"). It is fixed in
  §§0, 4, 5, 6, which now list exactly the rules covered, and §2.7 adds the "not covered" row. There were **17 MINOR**
  findings, all applied:
  * "square-generated" was replaced by K ⊆ Γ^{(2)};
  * Thm C's (R2) now allows any m when Γ = Γ^{(2)};
  * the Z₃ wording was fixed in Thm D;
  * the Dirichlet wording was fixed;
  * the subset remark was corrected;
  * the residue-class wording in Lemma D(a) was fixed;
  * 0.07 → 0.08;
  * the Bonferroni counts for both stratifications are now computed in the script;
  * Robins–Breslow–Greenland confidence intervals replace "≲ 0.02 (2σ)";
  * exact χ² tails replace Wilson–Hilferty;
  * the heterogeneity [F] and twisted-law [G] checks were added, and the CERTIFIED non-determinism claim was narrowed
    to moduli dividing 6160;
  * the quartic-2 identity is relabelled PROVED given Barrucand–Cohn, and the dangling citation was fixed;
  * the literature section's title now says what was and was not opened;
  * the 1/4 share among p ≡ 1 (24) is relabelled as expected/observed;
  * "independent" was softened to "no detectable association";
  * this note was added.

  All corr_*.txt files were regenerated with the revised script, and the numbers in §3 come from them.

* **Cross-model hostile review** (GPT/Astra, `data/z52d/xreview/REVIEW_PARITY.md`, verdict ACCEPT-WITH-FIXES).
  The core finite-group obstruction (Lemmas A, B, D; Thm C) and the parity reduction (Thm D) were judged correct.
  All decisive computations were reproduced independently: prime completeness to 2·10⁸, CMH/RBG statistics, the
  1 920-class law exclusion, and byte-identical reruns of `corr_1e8.txt` / `corr_2e8.txt`. Changes made:
  1. (MAJOR) Thm D's quantitative consequence now assumes a Bateman–Horn-order lower bound ≫ Y/(log Y)^{|S|}. A caveat
     flags that INVOLUTION_ES2 6.1(d)'s "precise" Y^{2/3} hypothesis does not give the stated count; this is inherited
     from the parent and is not propagated. The change is applied in §0, §2.6, §4, §5 and §6.
  2. (MAJOR) Statistical and scope wording:
     * "no fixed-modulus law exists" became "no law f(p mod M, h mod 16) with M | 6160";
     * "any association is below …" became "the tested common-OR estimates and nominal intervals are …";
     * "were multiple-testing fluctuations" became "did not replicate; consistent with fluctuations";
     * explicit non-exclusions were added: untested interactions, other class-group bits, other auxiliary sets;
     * "dead" is restricted to Thm C's rules on the full X with a fixed common finite affine menu (§0, §4, §5, §6).
  3. (MINOR) The density attribution is now "Dirichlet for infinitude, PNT in fixed APs for natural density" (Lemma D,
     Thm C, §0, §4). The §2.5 title no longer says "everything except parity".
  4. (MINOR) χ² null approximations and 95 % intervals are labelled asymptotic/nominal and not simultaneous. §3.6 now
     says the 8-rank has a known governing field and the 16-rank only a conjectural one. The pooled bound is rounded up
     to 0.0074. §3.2 now cites the original Barrucand–Cohn pages, as verified by the cross-reviewer.
