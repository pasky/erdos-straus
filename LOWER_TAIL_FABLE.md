# LOWER_TAIL_FABLE — sustained open attack on the single-integer lower tail (O274, model FABLE)

Status labels as in DISCOVERIES.md (PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment).
ES is not solved here. Scripts: `scripts/z43_fable_*`. Memos: `BRAINSTORM/z43_fable_*.md`.

## 0. Posture

Construction first. Every attempt below is recorded with (i) the mechanism tried, (ii) the exact
barrier hypothesis it meets, (iii) the modification that would violate that hypothesis, if any.

## 1. A canonical two-line form of ES at a prime (PROVED, elementary; re-derived from scratch)

Let p ≡ 1 (mod 4) be prime. Write ES(p) for "4/p = 1/x + 1/y + 1/z has a solution in positive integers".
Every solution has exactly one (Type I) or exactly two (Type II) denominators divisible by p
(standard; the brute-force check in `z43_fable_forms.py` confirms the dichotomy to 400).

**Theorem 1.1 (canonical form).** For a prime p ≡ 1 (mod 4),

> ES(p) ⟺ there exist m, u ≥ 1 such that the integer N = m·p + u has a divisor d with
>   d ≡ −1 (mod 4mu)  [Type II]   or   d ≡ −p (mod 4mu)  [Type I].

Explicit reconstruction (checked symbolically in `z43_fable_canon.py` for every prime < 400, both types,
against brute force — 0 mismatches):

* Type II: d = 4muw − 1, v = N/d, e = (u+v)/m ∈ ℤ, p + e = 4uvw, and
  4/p = 1/(uvw) + 1/(mpvw) + 1/(mpuw).
* Type I: d = 4muw − p, h = N/d, and 4/p = 1/(muw) + 1/(hpmw) + 1/(huw).

*Proof sketch.* 4/p − 1/x = (4x−p)/(px); a reduced fraction a/b is a sum of two unit fractions iff b has
coprime divisors U, V with a | U + V. With a = 4x − p, b = px: Type I is p | U, Type II is p ∤ UV.
Writing x = m·u·w (Type I: U = pm, V = u) resp. x = u·v·w (Type II: U = u, V = v) and reducing modulo
e = 4x − p gives e | pm + u (Type I) resp. e | u + v (Type II); re-indexing gives the statement. ∎

Equivalent symmetric forms (all PROVED, same computation):

* (1.2) ES(p) ⟺ ∃ u, v, w ≥ 1 with 4uvw > p such that (4uvw − p) divides u + v [II] or pu + v [I].
* (1.3) Type I ⟺ ∃ u, w: 4u²w + 1 has a divisor ≡ −p (mod 4uw) (the ET form f | p² + 4c²d, f ≡ −p (4cd)).
* (1.4) Type II ⟺ ∃ d ≡ 3 (mod 4) and m, δ with mδ | (d+1)/4 and p ≡ −δ/m (mod d).
* (1.5) Both types as p-independent covering systems: Type I covers p iff p ≡ −d (mod 4uw) for some
  d | 4u²w + 1; Type II covers p iff p ≡ −δ m⁻¹ (mod d) for some mδ | (d+1)/4.

Remarks.
* The two types differ only in the target class, −1 versus −p, modulo 4mu. The (★) line of
  SINGLE_P_COUNT is the sub-line m = 1 of Type II; the b = 1 (López Type A) line is the sub-line d = N
  of Type II (i.e. 4mu | mp + u + 1).
* T1 in this language: for p = n² an odd square, mn² + u never has a divisor ≡ −1 or ≡ −n² (mod 4mu)
  (reciprocity; see §2).
* Every certificate (m, u, d) forces (p/d) = −1 and hence a prime factor q of d with (p/q) = −1,
  so d (and therefore 4mu·w ± …) carries a prime ≥ ℓ(p), the least quadratic non-residue of p.

(§2 onward: mechanisms.)

## 2. Equivalent symmetric forms and what they expose (PROVED, elementary)

All of the following are re-indexings of Theorem 1.1 (each checked against the same brute force in
`z43_fable_canon.py` / `z43_fable_forms.py`; the campaign's window form "Rat_q(K) ∩ {−1, −p} ≠ ∅,
K = (p+q)/4" of B2_ACROSS_FIELDS is (2.1) with e = q prime).

* (2.1) ES(p) ⟺ ∃ u, v, w ≥ 1: e := 4uvw − p > 0 divides u + v [II] or pu + v [I].
* (2.2) ES(p) ⟺ ∃ u, c ≥ 1: the least positive residue of −p (II) or of −p⁻¹ (I) modulo 4uc divides u + c.
* (2.3) Type II ⟺ ∃ u, k, e: 4ku | p + e and e | p + 4ku².  Type I ⟺ ∃ u, k, e: 4ku | pe + 1 and e | 4ku² + 1.
  (reciprocal divisibility; with K = 4ku: II is "K | p + e, e | p + uK", I is "K | pe + 1, e | uK + 1").
* (2.4) Both in one line: ES(p) ⟺ ∃ u, K, e with 4u | K and K·e | uK + αe + β, (α, β) ∈ {(1, p), (p, 1)}.
* (2.5) Type II ⟺ p = e²k² − y² − e for some e ≡ 3 (4), k ≥ 1, y ≥ 0 (i.e. p + e + y² ∈ e²·□), after
  absorbing the third factor; equivalently p ∈ W − □ with W = {X² − e : e | X}.
* (2.6) Type II at a prime slice e ⟺ some divisor M of (p+e)/4 has a divisor u with u² ≡ −M (mod e)
  ("a divisor congruent to a square root of minus the cofactor").

What the forms expose.
* The 4-adic input is the single fact d ≡ 3 (mod 4) for every certificate divisor d (both targets −1 and −p
  are ≡ 3 mod 4). Hence **every certificate integer mp + u (equivalently every slice integer (p+e)/4 or
  (pe+1)/4) is divisible by a prime ≡ 3 (mod 4)**; in particular no primitive sum of two squares can carry a
  certificate. This kills at the root every "p = a² + b² / CM group order" construction: #E(𝔽_p) for curves
  with CM by ℤ[i] and all their quartic twists are sums of two coprime squares.
* The modulus is a product of the two coordinates of the integer: N = mp + u, M = 4mu. Every attempt to
  "untie" the modulus (fix M = 4U, allow all mu | U) gives only a sufficient condition with
  #tries ≈ τ₃(U)·log p ≪ |(ℤ/4U)^×| ≈ 2U; see §3.2.

**Lemma 2.7 (where the sign sits; PROVED, checked on all 9 959 certificates with m, u < 25, p < 3000).**
Let p ∤ mu and d | mp + u.
(II) If d ≡ −1 (mod 4mu) then (p/d) = −1 (Jacobi); so d has a prime factor q with (q/p) = −1 and d ≥ ℓ(p).
(I) If d ≡ −p (mod 4mu) and w := (d + p)/(4mu), then (p/w) = −1 (Kronecker); so the *level* w carries the
non-residue, while d itself need not: p = 13, (m, u, d) = (2, 1, 3) has (13/3) = +1.
*Proof.* (II): d = 4muw − 1 and d | mp + u give p ≡ −u/m ≡ −4u²w (mod d), so (p/d) = (−1/d)(w/d) = −(w/d),
and d ≡ −1 (mod 4w) forces (w/d) = +1 (reciprocity for odd w; for w = 2^a w′ use d ≡ 7 (mod 8)). (I):
d | p² + 4u²w (ET), so −w is a square mod d and (w/d) = (−1/d) = −1; and d ≡ −p (mod 4w) gives (w/d) = (p/w)
for odd w by reciprocity, with the 2-part handled by d ≡ −p (mod 8) when w is even. ∎
(This is the campaign's genus/T1 sign in canonical coordinates; it is recorded here only because it is the
one place where "4" enters.)

### 2.8 The Legendre form (PROVED relative to DEDEKIND_ES Thm 4.5/Cor 4.6; odd branches re-proved here)

> ES(p) ⟺ ∃ r ≥ 1 and a divisor A ≥ 2 of p + r with A ≡ −1 (mod r) and (A/p) = −1.

Equivalently (HJ clothing): ∃ A with (A/p) = −1 such that the least positive residue of −p mod A divides
A + 1 (then p/A = [[a, b, c]] with c = −p mod A, b = (A+1)/c, a = (p+c)/A). The "4" of ES has disappeared
into the Legendre symbol. For odd A, r the sign is a 2-adic statement, (A/p) = −1 ⟺ A ≡ 3 (4) or r ≡ 3 (4)
(reciprocity; checked on every odd pair with r ≤ 400, p < 3000, `z43_fable_hj.py`), which gives the
four-branch decomposition by r mod 4:

| r mod 4 | extra condition on A | explicit solution | campaign name |
|---|---|---|---|
| 3 | none | x = (p+r)/4, y = pAv(A+1)/(4r), z = pv(A+1)/(4r), v = (p+r)/A | e-slice with (u,c) = (A,1) |
| 1 | A ≡ 3 (4), i.e. A ≡ −1 (mod 4r) | (★): Type II at (m,u) = (1,r), d = A | (★) |
| 0 | none (sign automatic) | b = 1 line, r = 4d | López Type A |
| 2 | (−r/A) = −1 | Type I branch | — |

T1 control: for n = m² the symbol (A/m²) is never −1, so the form has no certificates, as it must.
Assessment: this is the cleanest *covering-system* statement of ES at a prime — p must lie in a class
−c (mod A) with c | A + 1 and a parity condition on (A, c) — and it shows that the whole content of ES is
"the infinite system {(A, −c) : c | A+1} covers the primes", i.e. exactly the problem Mordell/ET posed, with
no finite sub-system sufficing (B1). It was useful to me only as a lens; it is not a mechanism.

### 2.9 The mutual-shift graph (PROVED dictionary; census EVIDENCE)

Symmetrising 2.8 by a = t: ES(p) ⟺ ∃ coprime t, e ≥ 1 with te | p + t + e and (te/p) = −1.
Define the graph G_p: vertices e ≥ 1, edge t—e iff gcd(t,e) = 1 and te | p + t + e (equivalently t | p + e
and e | p + t), colour (e/p). Then **ES(p) ⟺ G_p has a bichromatic edge.** The vertex condition
"p + e has a divisor ≡ −p (mod e) coprime to e" is sign-free (no 4, no parity): T1 lives entirely in the
colouring. Vertex 1 is adjacent to every divisor of p + 1; vertex 2 to every odd divisor of p + 2; the
neighbours of e are the divisors of p + e in the class −p (mod e).
Census (`z43_fable_graph.py`, primes p ≡ 1 (4) < 3000, 211 primes): G_p is connected for 28 of them; the
component of 1 has ≍ log² p vertices and contains a QNR vertex for 209 of 211 primes; the other components
are sporadic 2- or 3-cliques ({4,7,11} at 73, {9,14} at 229, …); every prime has a bichromatic edge, no odd
square has one (21 squares checked).
Assessment: "some component is bichromatic" is a global, sign-free reformulation, and a colouring argument
would need the walk 1 → (divisors of p+1) → (divisors of p+e in class −p mod e) → … to be forced to reach a
non-residue. Nothing forces it: the walk is a divisor-structure walk (B2 at every step). Recorded as a lens.

## 3. Mechanism audit (construction attempts, each with the barrier hypothesis it meets)

Every item was first pushed as far as it goes constructively; the barrier is named only where the construction
stops. "Lottery" below always means: a single fixed integer must have a divisor in a single class of a modulus
tied to that integer (B2), with expected count polylog and no control of the fluctuation (B3).

### 3.1 Thue / lattice (Fermat-style size argument)
For a fixed d ≡ 3 (4) the certificate condition is a lattice statement: (u, m) ∈ L_d := {pu + m ≡ 0 (mod d)}
with um | (d+1)/4 (Type II; Type I has um | (d+p)/4). L_d has covolume d and its Klein-polygon vertices
(convergents of p/d) satisfy u_i m_i < d, so Minkowski/Dirichlet always supplies ≍ log d points with
u m < d — the *size* half of a Fermat-type argument is free. What is not free: (i) the *sign* (every other
convergent has pu ≡ +m), which is T1 (Zolotarev/HJ, DEDEKIND_ES §4); (ii) the *divisibility* um | (d+1)/4
instead of um < d, a lottery of probability ≈ τ₃((d+1)/4)/d. Modification that would evade (ii): make
(d+1)/4 have ≍ d divisor pairs — impossible (τ₃(A) ≤ A^{o(1)}). Verdict: the hyperbola condition is not a
lattice condition; Thue gives the box, never the divisor. (B2, "tied modulus"; B5 for the sign.)

### 3.2 Pooling at a fixed modulus; the index calibration
Fix U and consider all cells mu | U with the *sufficient* condition d ≡ −1 (mod 4U). Tries:
Σ_{mu | U} τ(mp + u) ≈ τ₃(U) log p; group: |(ℤ/4U)^×| ≈ 2U. Since τ₃(U) ≤ U^{o(1)}, tries ≪ group for
every U (equality region only U | 24, the campaign's zero-sum levels). Pigeonhole then yields *collisions*
d₁ ≡ d₂ between divisors of different integers, never a hit, and collisions are not certificates.
**Calibration (new framing, Assessment).** The same count against a *coset target* −H, H ≤ (ℤ/4U)^×,
is tries ≈ τ₃(U) log p versus [G : H]. For H = squares, [G : H] = 2^{ω(U)+O(1)} ≪ τ₃(U): counts beat the
group, and that relaxation (ES^□ of (J)28) is indeed a theorem — there the argument is even simpler (one
Dirichlet prime), but the calibration explains *why* it had to be provable. For ES the target is the
2-element set {−1, −p}, H trivial, [G : H] = |G| ≫ tries. Intermediate relaxations (target −H with H = k-th
powers, k ≥ 3) have [G : H] ≈ k^{π(y)/φ(k)} < 3^{π(y)} ≈ τ₃(U): the counting *allows* a hit, but a hit still
needs a covering argument (tries must *cover* G/H, not merely exceed |G/H|), which needs the divisors of the
pooled integers to equidistribute in G/H — unavailable for ~τ₃(U) specific integers near p. So the only
provable member of the ladder is k = 2, where a single prime does the job. (B4; H-A hypothesis "fixed
modulus" is exactly what makes tries ≪ group.)

### 3.3 p's canonical data
* p = a² + b² (Gaussian): every integer built as a primitive norm from ℤ[i] (including #E(𝔽_p) for CM by ℤ[i]
  and its twists, and (a+b)² = p + 2ab) has no prime factor ≡ 3 (mod 4), hence carries no certificate (§2).
  Norms from ℤ[√−2], ℤ[ω], real quadratic rings can be ≡ 3 (4), but the divisor class mod 4mu of a norm
  N(α) is as uncontrolled as any (ideal divisors of (α) ↔ divisors of N(α), classes untouched). Dead by §2 / B2.
* Pell / convergents of √p: x² − py² = u_i gives the cell (m, u) = (y², u_i) with N = x² a square; the divisors
  of x² are d₁²·d₂ for d₁d₂ | x, no obstruction (75 ≡ 3 mod 4 divides 15²) and no forcing: lottery on the
  factorisation of the convergent numerator x. The fundamental unit lives far outside the O(p²) search box.
* ord_p(2) etc.: p | 2^t − 1 produces cells (m, u) = ((2^t − 1)/p, 1) with N = 2^t, whose only odd divisor is 1;
  dead. More generally Fermat/Euler divisibilities put p into the *integer*, whereas certificates need p
  *outside* the integer (gcd(mp + u, p) = 1).
* #E(𝔽_p) for non-CM E: every N in the Hasse interval occurs for some E (Deuring), so "group orders" carry
  no information beyond "integers near p"; the group structure E(𝔽_p) ≅ ℤ/n₁ × ℤ/n₂ constrains n₁ | p − 1,
  not residue classes of divisors mod 4(1 − a_p). Dead (B2).

### 3.4 Non-abelian Frobenius
A prime certificate q at cell (m, u) is the pair of Frobenius conditions
Frob_q|ℚ(ζ_{4mu}) = complex conjugation and Frob_p|ℚ(ζ_q) = −u/m. The second is the *exact* residue of p
mod q, i.e. the statement that q divides the fixed integer mp + u — a factorisation, not a Chebotarev class
of q in any field independent of p. Higher reciprocity relates only the quadratic layer of the two
(TWO_POWER_LADDER Thm 3.2: S determines D modulo μ_m^{gcd(2,m)}). Nothing new beyond (J)93/(J)96/(J)104.

### 3.5 Involutions / parity
In canonical coordinates the only visible involution on Type II certificates is u ↔ v (the two p-divisible
denominators), which is free for p ≡ 1 (4) (a fixed point would force e | p). So f_II(p) is even and the
useful parity is f_II/2, which is 50/50 (board byproduct). A Zagier-type argument needs a superset S_p
with an involution having an odd number of fixed points *because p is prime*, and a second involution whose
fixed points are exactly certificates. Since certificates are divisor events of unforced parity, S_p would
have to contain compensating non-certificate fixed points of controlled parity; no natural S_p was found,
and INVOLUTION_ES already bars affine finite menus. Not pursued further.

### 3.6 Descent / Vieta
The certificate equation 4muwc = mp + u + c (Type II) and 4muwc = p(m + c) + u (Type I) is multilinear:
each variable appears to degree 1, so there is no second root and no Vieta involution; for fixed (m, w) it is
the hyperbola (4mwu − 1)(4mwc − 1) = 4m²wp + 1, whose integer points are exactly the divisor pairs. The only
"quadratic" structure is the norm form p² + 4u²w = N(p + 2u√−w) (Type I), where descent = Gauss composition,
already shown not to create points (COMPOSITION_ES). Dead.

### 3.7 Algebraic identities in p and auxiliary data
Any family (m, u, d) = polynomials in (p, params) with d ≡ −1 (mod 4mu) identically is a congruence covering
(B1); with p = a² + b² or p = Q(x, y) it is the two-variable Mordell–Schinzel situation (POINTWISE_BINARYFORM
Thm 3.2). The only identities that escaped B1 in the campaign (3·2^s + 1 etc.) use the *shape* of n to force
an exponent budget, which has no analogue for a general prime.

### 3.8 Summary of the audit
Every construction ends at one of two places: (a) a single integer near p (or in a fixed AP mod p) must have a
divisor in a single class of a modulus tied to it; or (b) a pooled family at a fixed modulus whose number of
divisor-tries is τ₃(U) log p ≪ U. There is no third place. The provable relaxations are exactly those whose
target is a coset of index ≤ 2^{O(ω)} (square multipliers) or whose shot family is infinite at a fixed
modulus (mute primes); ES has neither.

## 4. Assessment at this checkpoint

* No new mechanism. Every construction in §3 either produces the tied-modulus divisor event at one integer
  (B2/B3) or pools at a fixed modulus where the number of divisor-tries τ₃(U)·log p is below the group size
  (B4). The one quantitative framing I consider worth keeping is the index calibration of §3.2: a target
  coset −H ⊂ (ℤ/4U)^× is reachable by counting only if [G : H] ≲ τ₃(U); squares (ES^□) sit below that
  line, ES (H = 1) sits far above it, and no intermediate relaxation is both below the line and known.
* The forms of §1–2 are re-indexings of the ET/window/HJ forms already in the ledger; their value is that
  (i) Type I and II are the same statement with target −1 versus −p for the same integer mp + u and the
  same modulus 4mu; (ii) the sign of a certificate sits on the divisor for Type II and on the level for
  Type I (Lemma 2.7); (iii) the whole 4-adic content of ES is "the certificate divisor is ≡ 3 (mod 4)",
  which is what excludes norms from ℤ[i]; (iv) the Legendre/graph forms put T1 entirely into a colouring.
* Labels: Thm 1.1, (2.1)–(2.6), Lemma 2.7, 2.8 (odd branches), 2.9 (dictionary): PROVED. 2.8 even
  branches: PROVED relative to DEDEKIND_ES Thm 4.5. §2.9 census, §3 calibration: EVIDENCE / Assessment.
  ES is not solved; no case of it is claimed here.

## 5. Sparks (not pursued)

1. Index-calibrated relaxations: for H = k-th powers (k ≥ 3) the count allows a hit but a hit needs the
   divisors of ~τ₃(U) integers near p to *cover* G/H. Is ES_{Q³} (4/p = 1/x + 1/y + Q³/z, Q free) provable
   by a one-prime argument like ES^□, or is it already a lottery? Either answer calibrates the ladder.
2. The component of 1 in G_p: can |comp(1)| ≫ log² p be proved unconditionally (it is a sign-free count of
   divisors of p + 1, p + e, …)? A proved lower bound would isolate the colouring as the only obstruction.
3. In the Legendre form the map A ↦ (−p mod A) is linear on each Farey interval (p/(k+1), p/k]; the
   condition (−p mod A) | A + 1 then reads (k+1) | p + e, e | p + k + 1 — a 2-parameter symmetric system.
   Is there a Stern–Brocot / mediant move that preserves the system (an "edge-to-edge" map in G_p)? The
   candidate (t, e) ↦ ((p+e)/t, e) is an edge iff e | t + 1 — conditional, but maybe composable.
4. Lemma 2.7 says Type I's non-residue sits on the level w. A Type I search organised by w = ℓ(p) (the least
   QNR) has expected count ≍ (log p)²/ℓ(p); under GRH that is Θ(1) at the extreme. Is there a prime with
   NO certificate at any level w ≤ ℓ(p)·(log p)^{O(1)}? A census of "minimal level" versus ℓ(p) to 10⁸ would
   say whether the level structure adds anything beyond the window census of (J)85.
