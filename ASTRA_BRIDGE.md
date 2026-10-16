# ASTRA_BRIDGE — Astra square removal ↔ Claude window / exponent cap (task O249)

Status: in progress (O249). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Astra files (../erdos-straus-astra, READ-ONLY, read at d7300f8) are cited as [A:FILE §]. Claude files: EXPONENT_CAP
((J)34), CAP_POINTWISE ((J)64), CAP_DOWN ((J)66), CAP_INTERPOLATION ((J)63). Scripts `scripts/z21_*`.
Throughout p ≡ 1 (mod 4) is prime.

## 0. Iteration log

(B1) Orchestrator's observation: Astra's source congruence q | pm² + 1 and Claude's window congruence q | p + 4Q²
are the same condition mod q with m ≡ ±(2Q)⁻¹. TRUE as a congruence (m²(p + 4Q²) = pm² + (2Qm)²), and both need
exactly q ≡ 3 (4), (q/p) = −1. But the two *solutions* built from it put q in different slots: in Claude's window
shot q is the p-free x-window (x = (p+q)/4) and the ≡ 3 (4) divisor in y is the huge shot modulus g; in Astra's
source q is the divisor in y = p(q+1)/4, i.e. Astra's q plays Claude's g, and Astra's cofactor s plays the window.
So "one problem in two normalisations" is right only after a slot-by-slot dictionary (§1–§3), not literally.
(B2) First dictionary attempt: Astra twist m ↔ Claude cap e. Wrong granularity: Astra's twist is the full
denominator root (an integer), Claude's cap is its max exponent and Claude additionally demands self-muteness
rad(root) | y, which Astra's genuine sources *violate* by design (gcd(m, h) = 1). Correct reading: both are
sub-relaxations of the same ES^□-type space, sitting in different coordinate slots (§1).

## 1. One state space, three slots

**Definition 1.1.** A *rational point* of p is (x, y, z) ∈ ℚ_{>0}³ with 4/p = 1/x + 1/y + 1/z. Its *(Astra) twist*
τ(x, y, z) := min{m ≥ 1 : m²x, m²y, m²z ∈ ℤ}. So the integral points W(pm²) of [A:SQUARE_REMOVAL_STRUCTURAL §1, §11]
("states at twist m") are exactly m²·(rational points with τ | m), and *full square removal* = a point with τ = 1 =
an ES solution.

**Lemma 1.2 (Claude's capped solutions are Astra states; window shots have p-divisible anchor; PROVED, trivial).** Let (x, y, z) be
an ES^{(y,e)}(p) solution (EXPONENT_CAP Def 1.1: x, y ∈ ℤ, den z = r², r odd, gcd(r, p) = 1, rad r | y, v_ℓ(r) ≤ e).
Then τ = r and cap = max_ℓ v_ℓ(r); hence **cap 0 ⟺ τ = 1 ⟺ ES**, and cap ≤ e ⟹ τ is e-th-power-free-ish
(v_ℓ(τ) ≤ e) but τ itself is unbounded. In Astra's normalisation (r²x, r²y, r²z) ∈ W(pr²) has distinguished anchor
Z := r²z (the unique coordinate prime to r), and for a Claude *window shot* (Q, g) (CAP_POINTWISE Thm 1.1) the
anchor is divisible by p: Z = pK(g+1)/(4Q₀²). This is literally [A:POSITIVE_SOURCE_FORCED_FOLD (5)–(6)], which
already identifies its shot with EXPONENT_CAP Prop 1.3 (Q₀ = c, Q₁ = n, k = K/c).
*Proof.* den x = den y = 1, den z = r², so lcm = r², τ = r. Anchor: the coordinates r²x, r²y are ≡ 0 (mod r²).
Shot formula of EXPONENT_CAP §1 with den z = Q₁² (Prop 1.2). ∎

**Lemma 1.3 (Astra's *sources* have p-free anchor; PROVED).** (R-O249 repair M1: an earlier version claimed this for all
reachable states; false — Astra's reachable states include p-divisible anchors, e.g. (450, 19300, 34740) at 193·3² with
anchor 19300 = 100·193 [A:STR §4], and the fold states of [A:FORCED_FOLD].) Astra's source (q ≡ 3 (4),
qs = pm² + 1, h = (q+1)/4, A = sh) is 4/p = 1/(A/m²) + 1/(psh) + 1/(ph): the twisted coordinate is the **p-free**
one, x = A/m². More generally an Astra state (A, B₁, B₂) ∈ W(pm²) with gcd(A, m) = 1 and m² | B₁, B₂ (the
"reachable subclass" [A:STR §11.4]) is a rational point x = A/m² (den exactly m²), y, z ∈ ℤ, and Astra's **defect**
C = 4A − pm² equals m²·w where w := 4x − p is the (rational) Type II window of the point; equivalently the state is
an ES solution of the *input* N = pm² at the integral window C (x_N = A = (N + C)/4) whose other two coordinates
are ≡ 0 (mod m²). For the source, C = s + 1 and the window of the rational point is w = (s+1)/m².
*Proof.* 1/(sh) + 1/(Nsh) = (N+1)/(Nsh) = q/(Nh) and q/(Nh) + 1/(Nh) = 4h/(Nh) = 4/N; multiply by m². Defect of the
source: 4sh − pm² = s(q+1) − (qs − 1) = s + 1. ∎
*Remark (why scalar removal is impossible at a genuine source).* m² | sh with gcd(m, h) = 1 forces m² | s, but
4sh = pm² + 1 + s ≡ 1 + s (mod m²), so m² | s + 1 as well: m = 1. Hence every Astra square removal is a *move*,
never a scalar division of the source itself.

So the relaxations differ in the *slot* and side condition of the square denominator. (R-O249 repair M1: this is a
comparison of Astra's **sources** with Claude's **window shots**, not a disjointness of the two programmes: an Astra
certified state can be a Claude capped point, e.g. 4/193 = 25/1218 + 1/6090 + 1/27985 from (1218, 152250, 699625) at
193·5² [A:STR §11.3] is ES^{(y,1)} with y = 6090 ≡ 0 (mod 5), and Astra's next cross step takes it to cap 0.)
| slot of den = τ² | extra condition | name | provable? |
|---|---|---|---|
| p-free coordinate x | none (gcd(A, m) = 1 "genuine") | Astra source / state | yes, one Dirichlet prime ((J)28 ES^□) |
| p-divisible coordinate z (window shot) | rad τ ∣ y, v(τ) ≤ e, τ odd, gcd(τ, p) = 1 | Claude ES^{(y,e)} | cap ≤ (q−3)/4 forced at windows ((J)64, (J)66) |
| — | τ = 1 | ES | open |
For a source with gcd(m, p) = 1, Astra's *genuineness* gcd(m, h) = 1 makes rad m divide neither integral coordinate
(psh, ph): the opposite of Claude's *self-muteness* rad τ ∣ y. (Without gcd(m, p) = 1 this fails: p = 5, q = 3, m = 5 is
genuine with 5 ∣ 210, 5 — but then τ is not prime to p, as ES^{(y,e)} requires.)

## 2. Astra's certified states = twisted Type I windows (the level/certificate dictionary)

Astra's *level* e and *certificate* (e, H, r) [A:STR §3.1, §11; A:SQUARE_CERTIFICATE_SATURATION §2]: e ≡ 3 (4),
H = (pe+1)/4, a state at twist n with outputs U = (n²H + r)/e, V = n²HU/r, Z = pn²H, r | H², e | n² + 4r.
In Claude's language H = (pe+1)/4 is the **Type I e-slice** integer (brief: N = (pe+1)/4; CAP_POINTWISE Prop 4.1 with
k′ = e, a = H), and Z/n² = pH is the Type I coordinate x = pa.

**Theorem 2.1 (certified state ⟺ twisted Type I window; PROVED, elementary).** Fix e ≡ 3 (4), H = (pe+1)/4 and n ≥ 1
with gcd(n, e) = 1. The maps U = (n²H + r)/e, v = HU/r and r = eU − n²H are inverse bijections between
(a) divisors r | H² with e | n² + 4r and gcd(r, n) = 1 (Astra's closure gate [A:STR (30)]);
(b) rational points (U/n², v, pH) of p with U, v ∈ ℤ_{>0}, gcd(U, n) = 1 (so τ = n exactly).
**ES at level e** (an integral point with x = pH) is n = 1: a divisor r | H² with r ≡ −4⁻¹ (mod e), the classical
Type I criterion (brief: −1 ∈ Σ_e(N), N = (pe+1)/4). So Astra's twist at a fixed level is a square root of the class
−4r, i.e. **twisting = replacing the target class −4⁻¹ by its square class −4⁻¹·(ℤ/e)^{*2}**.
*Proof.* (a)⇒(b): 4(n²H + r) = n²(pe+1) + 4r ≡ n² + 4r ≡ 0 (mod e), gcd(4, e) = 1, so U ∈ ℤ_{>0}. gcd(r, e) = 1
(as 4H ≡ 1 mod e), and eHU = n²H² + rH ≡ 0 (mod r) because r | H²; so r | HU and v ∈ ℤ. n²/U + 1/v =
(n²H + r)/(HU) = e/H = 4/p − 1/(pH). For a prime ℓ | n: ℓ | U ⇒ ℓ | eU − n²H = r, and ℓ | r ⇒ ℓ | eU ⇒ ℓ | U (ℓ ∤ e);
so gcd(U, n) = gcd(r, n) = 1. (b)⇒(a): r := eU − n²H; 1/v = e/H − n²/U = r/(HU) gives r > 0 and r | HU. r ≡ −n²H, so
4r ≡ −n² (mod e). gcd(r, n) = gcd(U, n) = 1 as above. Finally r | HU ⇒ r | eHU = n²H² + rH ⇒ r | n²H² ⇒ r | H². ∎

**Corollary 2.2 (which levels carry a twisted state; PROVED).** Let e ≡ 3 (4) be prime. Some n ≥ 1 admits a twisted
state at level e ⟺ H = (pe+1)/4 has a prime factor s with (s/e) = −1 ⟺ H has a prime factor s with (s/p) = −1
(Kronecker symbol at s = 2). Then the least such twist is < e. Since (H/p) = +1 always (4H ≡ 1 mod p), H has an even
number of p-non-residue prime factors (with multiplicity); the condition is "at least two".
*Proof.* ⇒: −r ≡ (n/2)² is a nonzero square mod e and (−1/e) = −1, so (r/e) = −1; some prime s | r | H² has (s/e) = −1.
⇐: put r := s; (−4s/e) = (−1/e)(s/e) = 1, so n² ≡ −4s (mod e) has a root n₀ ∈ [1, e−1]; s ≠ e (gcd(H, e) = 1), so one of
n₀, e − n₀ is prime to s. Symbol: for odd s | H, pe ≡ −1 (mod s) gives (e/s) = (−1/s)(p/s) and reciprocity with
e ≡ 3 (4) gives (s/e) = (−1/s)(e/s) = (p/s) = (s/p) (CAP_POINTWISE Prop 4.1(a)). For s = 2: 2 | H ⟺ pe ≡ 7 (8) ⟺
e ≡ 7p (8); then (2/e) = −1 ⟺ e ≡ 3 (8) ⟺ p ≡ 5 (8) ⟺ (2/p) = −1. ∎
**Reading.** The levels that carry *no* Astra state at any twist are exactly the levels killed at *every* Claude cap by
CAP_POINTWISE Prop 4.1(b) (its side condition "a odd or k′ ≡ 7 (8)" is the s = 2 case of Cor 2.2). Since Prop 4.1(b) is
only a *sufficient* dead test, this gives **Claude-alive ⊆ Astra-alive**, strictly (R-O249 repair M2: an earlier
version claimed equality. Counterexample p = 5, e = 7, H = 9: Astra state n = 4, r = 3, 4/5 = 16/21 + 1/63 + 1/45, but
no ES^{(y,E)} point retains the coordinate 45 for any E — the reviewer's proof: 7/9 = 1/y + 1/z forces 7y − 9 = 3^c,
c ≡ 5 (6), den z = 3^{c−4}, never a square; reviews/astra-bridge-9bcb149a-hostile.md M2). Astra's *inherited certificate* [A:SATURATION §2] is
precisely what supplies the non-residue factor (r₀ ∈ −K) that Claude's Prop 4.1 showed is never forced by
H ≡ 4⁻¹ alone; Astra's saturation theorem [A:SATURATION §3] is a sufficient whole-subgroup covering condition,
analogous to the box-covering discussion of EXPONENT_CAP §3 / CAP_POINTWISE §2 (not the same criterion as the exact
Lemma 2.1), applied at a Type I level: cover the class −H/c of K = (ℤ/e)^{*2} by the exponent box of the
source primes of H with caps J_q = ⌊(2h_q − v_q(c))/w_q⌋. That is a B2 event (divisor of H² in one class mod e).

## 3. Astra sources = points of Claude's overflow/modulus surface with the congruence switched off

A Type II rational point 4/p = 1/x + 1/(py′) + 1/(pz′) carries two "levels": its **window** w := 4x − p (Claude's
q or m: CAP_POINTWISE, CAP_DOWN) and its **slice** g := 4y′ − 1 (Claude's shot modulus g, y = p(g+1)/4,
EXPONENT_CAP §1). In ES both are integers. The two relaxations twist different ones:
* Astra source (q, m): slice g = q integral (y = ph, h = (q+1)/4), window w = (s+1)/m² **twisted** (Lemma 1.3);
* Claude shot (Q, g): window m_c = (p + 4Q²)/g and slice g integral, third coordinate z twisted (den Q₁²).
So the orchestrator's identification "Astra q = Claude window q" is a coincidence of congruences; slot-wise
**Astra's q is Claude's slice g**, and Astra's cofactor s is Claude's D of EXPONENT_CAP Prop 1.3(b).

**Theorem 3.1 (the surface D·g = pM² + Y²; PROVED).** Let g ≡ 3 (4) (prime or composite) and consider integer points
(M, Y, D) with D·g = pM² + Y², gcd(Y, M) = 1. For a root ρ of ρ² ≡ −p (mod g) put L_ρ := {(M, Y) : Y ≡ ρM (mod g)}.
(a) Y = 1, M = m: an Astra source (q, m, s) = (g, m, D) [A:CAMPAIGN source identity], lying in L_ρ with ρ ≡ m⁻¹.
(b) M = 1, Y = 2Q: a Claude shot datum (Q, g), window D = m_c; in L_ρ with ρ ≡ 2Q. The EXPONENT_CAP Prop 1.3 point
(M, Y) = (2k, Q₁), Q = Q₀Q₁, 4Q₀k = g + 1, lies in the **same** lattice L_ρ (Q₁ ≡ 4Q₀k·Q₁ = 2Q·2k mod g): Prop 1.3 is a
change of lattice point inside L_ρ, and its shot congruence is D ≡ −Q₁² (mod 4k).
(c) **(ES-ready sources.)** For an Astra source with m even: s ≡ −1 (mod 2m) ⟺ q ≡ −1 (mod 2m) ⟺ m | (q+1)/2 = 2h.
In that case (Q₁ = 1, k = m/2, D = s) satisfies Prop 1.3's converse hypotheses, and (if gcd(Q₀, p) = 1, Q₀ := h/k) the
resulting shot is an **honest ES solution sharing Astra's coordinate y = ph**. Conversely every ES shot (Q₁ = 1,
EXPONENT_CAP Prop 1.2 with e = 0) is the source (q, m, s) = (g, 2k, D) with m | 2h.
(d) **(Genuineness excludes exactly this line.)** If gcd(m, h) = 1 and m is even, (c) applies only for m = 2.
*Proof.* (a) Lemma 1.3; pm² ≡ −1 gives ρ := m⁻¹ with ρ² ≡ −p. (b) gm_c = p + 4Q²; Q₁(1 − 4Q₀k) = −gQ₁ ≡ 0. (c) For m
even, 2m | m², so qs = pm² + 1 ≡ 1 (mod 2m) and gcd(q, 2m) = 1; hence s ≡ −1 ⟺ q ≡ −1 (mod 2m). With k = m/2:
D·g = 4k²p + 1 and D ≡ −1 (mod 4k), gcd(1, k) = 1: EXPONENT_CAP Prop 1.3 converse gives Q₀ = (4kp + j)/(4D) ∈ ℤ,
j = (D+1)/k, g = 4Q₀k − 1, g | p + 4Q₀², overflow 1, so (Prop 1.2, e = 0) an ES solution with y = p(g+1)/4 = ph, and
Q₀k = h. Conversely Prop 1.3(b) with Q₁ = 1 reads Dg = 4k²p + 1 and 4Q₀k = g + 1, so k | h. (d) m | 2h and
gcd(m, h) = 1 force m | 2. ∎
*Check* (`scripts/z21_dict.py 100000 100 600`, 11 s): all primes p ≡ 1 (4) ≤ 10⁵, all admissible prime q ≤ 100, all
lifts m ≤ 600 of both root classes: 2 345 942 Astra identities exact; of 1 173 678 even-m sources, 9415 are ES-ready,
the equivalence s ≡ −1 (2m) ⟺ m | 2h held in all, all 9415 Prop 1.3 solutions are exact ES solutions with y = ph,
and none is genuine with m > 2.
**Reading (Assessment).** Astra's genuineness condition gcd(m, h) = 1 is chosen so that the source is *not* already
an ES point; the classical Type II line "4k²p + 1 has a divisor ≡ −1 (mod 4k)" (FIXED_MODULUS_SHOTS Lemma 1.1) is,
in Astra coordinates, the set of maximally non-genuine sources m | 2h. Square removal from a genuine source is
therefore the task of moving into the line k | h by moves that change (m, s, q) — a B2 event in disguise
((c): the condition is a divisibility q ≡ −1 (mod 2m) with a solution-dependent modulus).

**Proposition 3.2 (ES at Astra's retained slice; PROVED, classical).** An ES solution with y = ph (h = (q+1)/4)
exists ⟺ some d | (ph)² satisfies d ≡ −ph (mod q); and for every source root, −ph ≡ (2m)⁻² ≡ Q² (mod q) where Q is
Claude's window root (p + 4Q² ≡ 0). So "keeping Astra's level y = ph" = "a divisor of (ph)² in the square class of the
Claude root Q²", and the Claude ES shot is the sub-case d = Q₀², Q₀ | h, Q₀² ≡ Q² (mod q) (R-O249 repair M3: not Q₀ ≡ ±Q for composite q —
p = 17, q = 39: Q = 8, Q₀ = 5).
*Proof.* q/(ph) = 1/x + 1/z ⟺ x = (ph + d)/q, z = ph·x/d with d | (ph)² (standard). −ph ≡ −p/4 and pm² ≡ −1. ∎
(Checked by brute force on all 31 360 (p, q) pairs of the run above: 14 883 slices carry ES.)

**Proposition 3.3 (T1 for Astra's state space; PROVED).** Let n = a² (a odd > 1) replace p.
(a) No Astra source exists at n: q | a²m² + 1 with q ≡ 3 (4) is impossible (every divisor of X² + 1 is a product of
primes ≡ 1 (4) and possibly 2). On the surface of Thm 3.1, g | (aM)² + Y² with gcd(aM, Y) = 1 forces g ≡ 1 (4): the
Astra source, the Claude shot and the ES Type II point die simultaneously (EXPONENT_CAP Prop 1.3 "T1 in these
coordinates").
(b) No twisted Type I state exists at any level e ≡ 3 (4) prime to a: for an odd prime s | H = (a²e+1)/4,
a²e ≡ −1 (mod s) gives (e/s) = (−1/s), so (s/e) = (−1/s)(e/s) = 1; and 2 | H forces e ≡ 7 (8), (2/e) = 1. So every prime factor of H has
Jacobi symbol +1 mod e, hence so does every r | H², whereas e | n² + 4r (gcd(n, e) = 1) forces (r/e) = (−1/e) = −1
(Jacobi; valid for composite e). So no r works for any n.
*Check* (`scripts/z21_typeI.py 100000 100 1000000`, 6 s; data/z21_typeI_1e5.txt): all 62 179 pairs (p ≤ 10⁵ prime
≡ 1 (4), prime level e ≡ 3 (4), e ≤ 100): Cor 2.2's prediction (prime factor s | H with (s/p) = −1) agreed with brute
force (some r | H² with −4r a nonzero square mod e) in every case; 45 491 levels alive; at each alive level the
least-twist state was built and checked exactly (4/p identity, τ = n); ES at the level (n = 1) in 24 575; least twist
≤ 32. T1: all 6083 (odd square a² ≤ 10⁶) × level pairs dead, as proved.

**Theorem 3.4 (lattice picture: Astra = horizontal line, Claude = vertical lines, ES = intersection; PROVED).**
Fix g ≡ 3 (4) (prime or composite) with gcd(g, p) = 1, h = (g+1)/4, a root ρ of ρ² ≡ −p (mod g) (a fixed root branch), and L_ρ(g) = {(M, Y) ∈ ℤ² : Y ≡ ρM (mod g)}
(index g; (pM² + Y²)/g is on it a binary form of discriminant −4p).
(a) Astra sources with slice g ⟷ points (m, 1) ∈ L_ρ(g) (the class m ≡ ρ⁻¹); genuine ⟺ gcd(m, h) = 1.
(b) Claude shot data with modulus g, **odd overflow** and root branch ρ (2Q ≡ ρ) ⟷ points (2k, Y) ∈ L_ρ(g) with **k | h**, Y > 0, gcd(Y, 2k) = 1, gcd(hY/k, p) = 1,
via Q = (h/k)·Y (so Q₀ = h/k, Q₁ = Y, Prop 1.3's D = (4k²p + Y²)/g). The solution has y = ph and **den z = Y²**: overflow
= Y; it is ES^{(y,e)} ⟺ rad Y | h and max v_ℓ(Y) ≤ e.
(c) ES shots with modulus g ⟷ (a) ∩ (b) = points (2k, 1) with k | h, i.e. 2kρ ≡ 1, i.e. g | 4k²p + 1 with 4k | g + 1.
*Proof.* (b) ⇒: Prop 1.3 point (2k, Q₁) ∈ L_ρ with ρ = 2Q (Thm 3.1(b)), 4Q₀k = g + 1. ⇐: D·g = 4k²p + Y² ≡ Y² (mod 4k)
and g ≡ −1 (mod 4k) (4k | 4h) give D ≡ −Y² (mod 4k); Prop 1.3's converse (gcd(Y, k) = 1) gives the shot with
Q₀ = (g+1)/(4k) = h/k and overflow Y; den z = Y² by the valuation normalisation of [A:FORCED_FOLD §2] (valid also at ℓ = 2: for ℓ | Q,
a = v_ℓ(Q), b = v_ℓ(h), the identity g·x = ph + Q² with ℓ ∤ pg gives den exponent 2(a − b)⁺; here gcd(Q, h) = h/k, so
the reduced root is Q/(h/k) = Y), and the ES^{(y,e)} conditions are Prop 1.2(i)–(ii) for ℓ | Y
(gcd(Y, k) = 1 and ℓ | h/k allowed: v_ℓ(Q) = v_ℓ(h/k) + v_ℓ(Y) ≤ v_ℓ(4h) + e ⟺ v_ℓ(Y) ≤ v_ℓ(k) + e = e). (a) Thm 3.1(a).
(c) Y = 1. ∎
*Scope (R-O249 repair M3).* Even-overflow shots are outside (b): p = 5, Q = 2, g = 3 gives (3, 5, 15/4), normalised
point (2, 2), not primitive. They are Astra twist-2 states (the 15241 fold, 193 COFACTOR_SUPPLY) but never ES^{(y,e)}
points (odd root required). The forward map (2k, Y) ↦ shot remains valid for non-primitive points; the converse
direction of Prop 1.3 used here assumes Q₁ odd. Sources/shots are matched within one root branch ρ.
*Check* (`scripts/z21_lattice.py 3000 400 400`, data/z21_lattice.txt): all primes p ≡ 1 (4) ≤ 3000, all g ≡ 3 (4) ≤ 400
with a root (composite g included), all k | h, all Y ≤ 400 in the class: 168 858 shots built, den z = Y² exactly in
every case (1193 ES); 125 604 Astra sources exact.
**Reading (Assessment).** In one rank-2 lattice per slice, Astra fixes Y = 1 and moves M along a residue class
(prohibited from the divisors of 2h by genuineness), Claude fixes M among the divisors 2k of 2h and lets Y float
(self-muteness: rad Y | h). ES is the meeting point (2k, ±1). Both "moves" are within L_ρ(g) for a *fixed* slice g;
changing g changes the lattice — this is the solution-dependent modulus of B2. Reduction theory of L_ρ(g) (the
reduced form of discriminant −4p in the class of the ideal above g) controls the *sizes* of (M, Y) but not the
divisibility k | h — the B2 condition lives in the arithmetic of h = (g+1)/4, not in the lattice geometry.

## 4. Astra's fixtures in Claude language

`scripts/z21_fixtures.py` (data/z21_fixtures_translated.txt) re-checks every numeric triple of the verbatim
extraction data/z21_astra_fixtures.txt (141 records from 13 Astra files; four extraction slips repaired and marked
in the data: a W(4p) state mislabelled W(49p), a 5209 record labelled 193, and two rows with N = ? restored from the
Astra text (233689·8², 4·193)) with exact rationals, now **asserting** exactness and the Type II divisor conditions:
**all 51 distinct numeric triples are exact ES points of their input pm²** (two symbolic/non-integral rows are
reported as skipped). (R-O249 repair M5: the earlier version ignored the prime 2 in the self-muteness flag, silently
skipped two rows and printed rather than asserted failures.) Only one twisted fixture is a Claude ES^{(y,e)} point
(193, twist 5, (1218, 152250, 699625)); the twist-2 fixtures are not (even τ). Translation (τ = twist; "level e / r" = Type I certificate of Thm 2.1 with
n = 1; "window w / d" = Type II window divisor d | K², d ≡ −K (mod w), K = x):
| p | Astra route | Claude reading of the exit |
|---|---|---|
| 97 | sources q = 19, m = 3; q = 1171, m = 13 | Type I levels e = 7 (H = 170, r = 5), e = 15 (H = 364, r = 26 or 56); one Type II window w = 15, d = 392 |
| 193 | source q = 79, m = 3 (window 23/9); floors m = 2 (window 2), m = 7 (C = 3: window 3/49); 24→3→1, 7→45360→3→1 | Type I e = 3 (H = 145, r = 5 or 29), e = 7 (H = 338, r = 26), e = 143 (H = 6900, r = 250); Type II w = 15 (d = 8), w = 7 (d = 20) |
| 3361 | sources q = 11 (m = 3, 19), q = 67 (m = 26), q = 271 (m = 457) | Type I e = 7 (r = 68), e = 39 (r = 29), e = 119 (r = 17820); Type II w = 39 (d = 125) |
| 5209 | composite-q seed q = 157915, m = 24 → floor m = 7, C = 3 → borrowing b = 50 | Type I e = 31 (H = 40370, r = 550 = 11·50: borrowed content), e = 119 (r = 2112), e = 95 (r = 261) |
| 233689 | grid / offset repairs, m = 8 | Type I e = 7 (H = 408956, r = 19), e = 119 (r = 446) |
| 2521 | q = 2123 | Type I e = 35 (r = 13851) |
| 15241 | composite q = 17·27179, m = 24 → 7 → fold → 2 → 1 | the fold state is **Claude's window shot at window R = 11 with the even root Q = 2** (twist 2, p-divisible anchor, Lemma 1.2); exit Type I e = 15 (H = 57154, r = 41) |
| 313 | Type II moments, q = 7, m = 19 | Type II window w = 7, d = 25 = 5²: a **cap-0 square shot** (Q = 5) of CAP_POINTWISE Lemma 3.1 |
| 1129 | birational, m = 5 | Type I e = 3 (H = 847, r = 539) |
**Reading (Assessment).** Every Astra exit is a *classical* small-modulus ET certificate: 25 of the 30 twist-1 points
are Type I at levels e ∈ {3, 7, 15, 31, 35, 39, 95, 119, 143}, 5 are Type II at windows w ∈ {7, 15, 39}. The
genealogy (source → floors → borrowing/fold) is a *route to* the level/window, and by Thm 2.1 the exit at level e
depends on the route only through one divisor r | H² (Astra's own remark [A:STR §11.4]: "inherited first
integrality is not inherited exit forcing"). In particular the fold of [A:FORCED_FOLD §2] is a Claude window shot
with the *least* root instead of a subgroup element: it trades Claude's self-muteness (rad τ | y) for size
(τ ≤ (R−1)/2).

## 5. Transfers

### 5.1 Window versus slice: the same prime is forced in one slot and unforced in the other

**Proposition 5.1 (PROVED).** Let q ≡ 3 (4) be prime with (q/p) = −1 (Astra-admissible = Claude window symbol).
(a) *As a Claude window* (x = K = (p+q)/4): (K/q) = −1, so −1 ∈ ⟨primes of K⟩ mod q and −K is the square of an
element of that subgroup (CAP_POINTWISE Thm 1.1; CAP_DOWN Thm 1.2 for the 2-adic side condition) — forced.
(b) *As Astra's slice* (y = ph, h = (q+1)/4): ES at the slice needs d | (ph)², d ≡ −ph (mod q) (Prop 3.2). Here
(h/q) = (4⁻¹/q) = +1, so the primes of h contain an *even* number (possibly zero) of non-residues: nothing forces
−1 ∈ ⟨primes of h⟩. The prime p itself is a non-residue ((p/q) = −1) but may enter d only with exponent ≤ 2.
So the slice is a "+1-parity" object like a Type I level (CAP_POINTWISE Prop 4.1 dichotomy), the window a
"−1-parity" object.
*Proof.* (a) is CAP_POINTWISE Thm 1.1's group step. (b) 4h ≡ 1 (mod q). ∎
**Transfer (Claude → Astra).** Every Astra-admissible prime with q ≡ 4 − p (8) (or q ≡ 7 (8), or v₂(p+q) even, CAP_DOWN
Thm 1.2) *also* carries a forced self-mute state when used as a window: a point with x = K, y = p(g+1)/4, den z = Q₁²,
rad Q₁ | y, cap ≤ (q−3)/4 (CAP_DOWN Prop 1.3). [A:FORCED_FOLD] already uses admissible primes as windows (its R),
but with the *least* root Q < R/2 instead of the forced subgroup element; this is the size/self-muteness trade-off.

### 5.2 Phase diagram of the relaxations (what is free, what is forced, what is open)

**Proposition 5.2 (PROVED, elementary).** For every prime p ≡ 1 (4):
(a) *(non-self-mute, prime twist — free.)* For any Astra-admissible q and any prime m in a root class of pm² ≡ −1
(mod q) with m ∤ ph (infinitely many, Dirichlet), the source is a rational point with y, z ∈ ℤ and den x = m², m prime
(twist m, "cap 1" without self-muteness).
(b) *(non-self-mute, small twist — free.)* For any Astra-admissible q, the least-root window shot (Q the even
representative of a root of −p mod q, halved [A:FORCED_FOLD (3)]; assume gcd(Q, p) = 1, automatic when q < 2p — (O249 self-check: at p = 5, q = 103, Q = 30
the denominator is 20, not a square) is a point with x, y ∈ ℤ and den z = Q₁²,
Q₁ ≤ (q−1)/2; so the minimal twist is < q₀(p)/2 whenever q₀(p) < 2p, q₀(p) := least prime ≡ 3 (4) with (q/p) = −1 (≪_ε p^{1/4+ε}
ineffectively by Pollack IJNT 2014 Thm 1.4 applied to (1 − χ₋₄)(1 − χ_p); ≪ (log p)² under GRH).
(c) *(self-mute, cap < q — forced.)* CAP_POINTWISE Thm 1.1 (cap ≤ q − 3 at windows with q ≡ 4 − p (8)), CAP_DOWN
(cap ≤ (q−3)/4; e*(p) ≤ (p − 5)/8 for p ≡ 1 (8)).
(d) *(self-mute, bounded cap — open; twist 1 = cap 0 = ES — open.)*
*Proof.* (a) Lemma 1.3 and gcd(m, sh) = 1 (gcd(m, h) = 1 as m ∤ h; gcd(m, s) = 1 as qs ≡ 1 mod m). (b) FORCED_FOLD
(3)–(5) (their hypothesis Q < p): Q ≤ (q−1)/2, Q₁ = Q/gcd(Q, K) ≤ Q. ∎
*Check* (`scripts/z21_phase.py 100000 200`, data/z21_phase_1e5.txt): all 4783 primes p ≡ 1 (4) ≤ 10⁵: q₀ ≤ 71, the
least-root shot at q₀ is exact with twist ≤ 22; the prime-twist source at q₀ is exact (den x = m², m prime). Over
admissible q ≤ 200 the least-root twist is 1 (an ES square shot) for 4508 primes, ≤ 9 for all.
**Reading.** Without self-muteness every *size* question about the twist is trivial (prime twist, twist < q₀/2), so
Astra's "strict twist decrease" is progress only through its final step (twist 1). With self-muteness the size
of the twist is free but its *exponents* are forced only up to the order of the subgroup. The two relaxations meet
only at ES; neither contains a bounded-cap/bounded-twist statement that is both nontrivial and provable.

### 5.3 Astra's macros in Claude language (Astra → Claude)

By Thm 2.1, at a fixed level (e, H) a certified state is a divisor r | H² in the coset −4⁻¹(ℤ/e)^{*2}, and the exit is
the element −4⁻¹ itself. Each Astra operation acts on this datum as follows (all PROVED by unwinding the cited formulas):
| Astra operation | action at fixed level | Claude reading |
|---|---|---|
| closure / re-rooting [A:STR §11.2] | change n within ±√(−4r) mod e | choice of lift; no information |
| pure borrowing [A:STR §19.1] | r → r·b with b ∣ H²/r, ℓ²b ≡ 1 (mod e) | move inside D_e(H) = {r ∣ H² mod e}; B2 at modulus e |
| saturation [A:SATURATION §3] | mixed-radix cover of −H/c by source-prime box | sufficient whole-subgroup covering (analogous to EXPONENT_CAP §3) |
| CRT forced factor [A:FORCED_FACTOR, FINITE_CHAIN] | forces t ∣ m and t² ∣ J = (p+q)/4 (gcd(t, p(p−1)) = 1); the subsequent level and its closure gates are not re-derived here | new lottery at the new level |
| fold [A:FORCED_FOLD §2] | Type I state → window shot at a prime R ∣ r | least root (size), not ⟨S⟩ (self-mute) |
| first pivot [A:STR §11.1] | R ∣ m²A², e = (4R + m²)/C | divisor of m²A² in a class mod the defect C (B2) |
(R-O249 repair M1: an earlier sentence "none of them changes the cap of a Claude state" was false — the Astra cross
step from (1218, 152250, 699625), a cap-1 Claude point, reaches cap 0.) What is true: by Thm 2.1 a cross step at level e
uses the input only through one divisor r ∣ H², and its twist-1 output exists iff the classical Type I certificate at e
exists. So these operations can *reach* cap 0 from a capped point, but each such success is a B2 hit at the new level,
not a forced descent. **No forced cap-descent move e → e′ < e is obtained** (Assessment; scope: the operations in the
table. Not analysed: the height-floor gateway with g = s > 1 and no inherited certificate [A:GATEWAY_COMPATIBILITY §1],
to which Thm 2.1 does not apply, and the composite-R cofactor-supply rule [A:COFACTOR_SUPPLY].)

### 5.4 Heights (Astra's compression problem) — what Claude's results do and do not say
*Bound (PROVED, elementary).* The least-root window shot of Prop 5.2(b), scaled to an integral point at pτ²
(τ = Q/c, c = gcd(Q, K)), is (τ²U, τ²pK, pUK/c²), so its height is ≤ τ²·pUK ≤ τ²·p(p+q)(p+q²+q)/(16q): height
O_{p,q}(τ²) with τ < q/2. *Reading (Assessment).* Astra's height problem lives in the opposite regime: twists r → ∞ at
fixed p, where [A:TWIST_HEIGHT_COMPRESSION Thm 1] forces height ≥ r²B(p, r) ≍ r^{5/2}/2 for non-scalable witnesses
and every scaled ES solution has height ≤ F_p r² [A:TWIST_FIXED_DEFECT §1]; the O_{p,s}(r^{32/11}) compression is a
statement about that regime. Claude's window/cap results produce *small* twists directly (τ < q₀/2, or self-mute with
cap < q) and say nothing about compressing a given large twist. Claude's overflow rigidity (EXPONENT_CAP Thm 2.1,
g ≤ 2nQ₁²(n + Q₁²)) is the shot-family analogue of Astra's height wall (both archimedean); no quantitative transfer
between them was attempted.

## 6. The bet (bounded cap for every p via forced membership + forced factors): gate-by-gate, and where it stops

### 6.1 Each Astra gate is one B2 event
B2 (redteam-automorphic-2 Thm 2.2): a fixed-p encoding reduces to "an integer N_θ(p) has a divisor in a residue class
whose modulus is part of the solution". Unwinding Thm 2.1/3.1 and §5.3:
| Astra gate (their name) | N_θ(p) | class / modulus |
|---|---|---|
| endpoint / retained-level exit [A:STR §21.2] | H² = ((pe+1)/4)² | −4⁻¹ mod e (Type I e-slice) |
| ES at the source slice (Prop 3.2) | (ph)², h = (q+1)/4 | Q² ≡ −ph mod q |
| ES-ready source (Thm 3.1(c)) | 4k²p + 1 | q ≡ −1 mod 4k (classical Type II line) |
| first pivot [A:STR (27)] | m²A² | R ≡ −m²/4 mod C (C = defect) |
| borrowing [A:STR (67)] | H²/r₀ | m⁻² mod e |
| fold supply [A:FORCED_FOLD (1)] | r (inherited) | prime R ∣ r, R ≡ 3 (4), (C/R) = 1, R < 2 min(m, p) |
| universal favourable source | (choice of e or q) + one of the above | — |
So the Astra and Claude programmes hit the *same* wall from two sides: Claude relaxes the box (exponents b_s + e)
and keeps the class; Astra relaxes the class (coset −4⁻¹K) and keeps the box (Thm 2.1). Their common refinement is
ES, and their union is still a B2 lottery at a solution-dependent modulus.

### 6.2 Two precise scope statements

**Proposition 6.1 (saturation fires only at levels e = p^{o(1)}; PROVED).** If Astra's saturation hypothesis
[A:SATURATION (2)] holds at level e (odd, e ≡ 3 (4)), then φ(e) ≤ 2^{ω(e)}·τ(H²), H = (pe+1)/4. Hence
e ≤ exp(O(log(pe)/log log(pe))), i.e. e ≤ p^{O(1/log log p)}.
*Proof.* K = (ℤ/e)^{*2} has order φ(e)/2^{ω(e)} (e odd). Hypothesis (2) gives |K| = ∏ d_i with d_i ≤ J_{q_i} + 1 ≤
2h_{q_i} + 1, and ∏ (2h_q + 1) = τ(H²). The divisor bound τ(N) ≤ N^{O(1/log log N)} and φ(e) ≫ e/log log e give the rest. ∎
So the only fully forced Astra exit applies at levels so small that H's factorisation is that of a *given*
integer (pe + 1)/4 — the classical Type I search; CRT-prescribed content t | H forces e ≡ −p⁻¹ (mod t), and the least
such level is a residue of size ≍ t for generic p, while t contributes at most τ(t²) = t^{o(1)} to the box.

**Proposition 6.2 (Type I aliveness and subgroup membership can be forced; PROVED).** Let ℓ be a prime
with (ℓ/p) = −1 (Kronecker) and let e ≡ 3 (4) be a prime with pe ≡ −1 (mod 4ℓ) (infinitely many, Dirichlet;
ℓ = 2 needs p ≡ 5 (8) and then pe ≡ −1 (mod 8)). Then ℓ | H, the level e carries an Astra twisted state of twist
< e (Cor 2.2), and −4⁻¹ ∈ ⟨primes of H⟩ mod e (the Type I analogue of CAP_POINTWISE Thm 1.1's group step).
*Proof.* ℓ | H by construction; (ℓ/e) = (ℓ/p) = −1 by Cor 2.2's symbol computation; ℓ has even order in the cyclic group
(ℤ/e)^* of order 2·odd, so −1 ∈ ⟨ℓ⟩, and H ∈ ⟨primes of H⟩, so −H ≡ −4⁻¹ is in it. ∎
*Why it does not give a bounded cap (Assessment; R-O249 repair M4: not a proof that the exit cannot be forced).* Writing
−H ≡ ℓ·Y² (mod e) with Y ∈ ⟨primes of H⟩ (possible: −H/ℓ is a square lying in a
cyclic subgroup of even order), the point (U, HU/r, pH), r = ℓY² (Thm 2.1's formulas with n = 1, r not dividing H²)
has den(HU/r) = ∏_s s^{(c_s − 2b_s)⁺}, c_s = v_s(r), b_s = v_s(H) (computation as in CAP_DOWN Lemma 1.1), and the
ℓ-exponent c_ℓ = 1 + 2a_ℓ is odd: the denominator is a square (a Claude-type ES^{(y,·)} point with y := U) only if
2a_ℓ + 1 ≤ 2b_ℓ, which needs ℓ-content b_ℓ comparable to the discrete-log exponent a_ℓ < ord_e(ℓ) | e − 1.
Prescribing ℓ^B | H costs e ≡ −p⁻¹ (mod ℓ^B), so e ≳ ℓ^B/p ≫ B for generic p. Forced content and forced
membership pull in opposite directions: **membership is forced at the level of the group (size ≍ e), content only at
the level of the box (size ≤ τ(H²) = e^{o(1)} for e ≥ p)**. This is analogous to B3 at a single level (B3 itself is about
bounded-multiplicity main-term certificates; no such certificate is in play here). It obstructs *covering* arguments,
not the possibility that the one target lies in a small box (short relations / small orders are not excluded).

### 6.3 Verdict on the bet (Assessment: no bounded-cap proof obtained by this attempt)
This attempt obtained no bounded cap e*(p) ≤ C and no new positive-density cap-0 set (cap 0 on positive density is
already classical: Mordell's identities cover all p outside six classes mod 840) from combining Claude's forced
subgroup membership with Astra's forced-factor source preparation. What is PROVED is narrower: whole-subgroup
covering (saturation) is impossible above levels p^{O(1/log log p)} (Prop 6.1); aliveness and membership can be
forced (Prop 6.2) but this attempt found no way to force the *representative*; and a cross step at a fixed level
sees its input only through one divisor r (Thm 2.1). These do **not** exclude a single target lying in a small box
(short multiplicative relations, small orders), nor genealogies that force the arithmetic data of the final level. What would break it: a mechanism forcing the *discrete logarithm* of the
target (not just its membership) into a box of size level^{o(1)} — e.g. equidistribution of short multiplicative
relations among primes of K mod the window (CAP_POINTWISE §2's missing input), or an algebraic identity making the
level divide a value of a factorable polynomial ((J)74's Sophie-Germain mechanism, which works on thin families only).

## 7. Verdict (O249 checkpoint 1)

1. **Slot dictionary (PROVED, §1; scope repaired R-O249 M1).** Both programmes live in one space: rational points of
   4/p with square denominators (Astra: integral points of W(pm²)). Astra's *sources* twist the **p-free** coordinate
   (genuine: gcd(m, h) = 1); Claude's *window shots* twist a **p-divisible** coordinate with self-muteness rad τ ∣ y.
   The programmes are not disjoint: Astra's reachable states include p-divisible anchors and at least one Claude
   capped point (193, twist 5, ES^{(y,1)}). Astra twist = Claude overflow Q₁; Claude cap = max exponent of Q₁.
   "Twist 1 ⟺ cap 0 ⟺ ES" holds trivially; intermediate measures do **not** correspond.
2. **The orchestrator's congruence identification is true but slot-crossed (Thm 3.1).** Astra's q is Claude's
   *slice* g (the ≡ 3 (4) divisor in y = p(g+1)/4), Astra's s is Prop 1.3's D, Astra's twist is Prop 1.3's 2k.
   Astra sources are the points of Claude's overflow/modulus surface Dg = pM² + Y² with Y = 1 and the shot
   congruence switched off; **the ES-ready sources are exactly m | (q+1)/2 (the classical Type II line), and
   genuineness excludes them apart from the trivial m = 2 case** (Thm 3.1(c),(d); 9415/9415 checked; e.g. p = 5,
   q = 3, m = 2 is genuine and ES-ready).
3. **Certified states = twisted Type I windows (Thm 2.1).** Twist at level e = square root of −4r; ES = class −4⁻¹.
   Levels carrying any Astra state = levels where H = (pe+1)/4 has a p-non-residue prime factor (Cor 2.2; 62 179
   pairs checked) ⊇ Claude-alive levels, strictly (R-O249 M2: p = 5, e = 7). T1: Astra sources and certified Type I
   states are empty at odd squares (Prop 3.3; not a claim about arbitrary W(a²m²)).
4. **Fixtures (§4).** All 51 distinct numeric Astra triples re-verified exactly (script now asserts); every Astra exit is
   a classical small-modulus certificate (25 Type I at e ≤ 143, 5 Type II at w ≤ 39); the 15241 fold and the 193
   COFACTOR_SUPPLY state are window shots at R = 11 with Q = 2 (twist 2: an Astra state, not an ES^{(y,e)} point,
   which needs odd τ); the 313 Type II exit is a cap-0 square shot.
5. **Transfers (§5).** The same admissible prime is *forced as a window* and *unforced as a slice* (Prop 5.1).
   Without self-muteness, small/prime twists are free (Prop 5.2), so Astra's twist decrease carries no information
   until twist 1. No *forced* cap-descent move was found among the analysed macros (§5.3, Assessment, scoped).
6. **The bet (§6): no bounded-cap proof obtained (Assessment).** Each Astra gate is a B2 event (table 6.1);
   saturation can fire only at levels p^{O(1/log log p)} (Prop 6.1, PROVED); Type I aliveness and subgroup
   membership can be forced by CRT (Prop 6.2, PROVED); forcing the representative was not achieved, and nothing
   here excludes it.
ES untouched; no infinite case of ES claimed.
