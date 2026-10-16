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

**Lemma 1.2 (Claude's capped solutions are Astra states with p-divisible anchor; PROVED, trivial).** Let (x, y, z) be
an ES^{(y,e)}(p) solution (EXPONENT_CAP Def 1.1: x, y ∈ ℤ, den z = r², r odd, gcd(r, p) = 1, rad r | y, v_ℓ(r) ≤ e).
Then τ = r and cap = max_ℓ v_ℓ(r); hence **cap 0 ⟺ τ = 1 ⟺ ES**, and cap ≤ e ⟹ τ is e-th-power-free-ish
(v_ℓ(τ) ≤ e) but τ itself is unbounded. In Astra's normalisation (r²x, r²y, r²z) ∈ W(pr²) has distinguished anchor
Z := r²z (the unique coordinate prime to r), and for a Claude *window shot* (Q, g) (CAP_POINTWISE Thm 1.1) the
anchor is divisible by p: Z = pK(g+1)/(4Q₀²). This is literally [A:POSITIVE_SOURCE_FORCED_FOLD (5)–(6)], which
already identifies its shot with EXPONENT_CAP Prop 1.3 (Q₀ = c, Q₁ = n, k = K/c).
*Proof.* den x = den y = 1, den z = r², so lcm = r², τ = r. Anchor: the coordinates r²x, r²y are ≡ 0 (mod r²).
Shot formula of EXPONENT_CAP §1 with den z = Q₁² (Prop 1.2). ∎

**Lemma 1.3 (Astra's sources and reachable states have p-free anchor; PROVED).** Astra's source (q ≡ 3 (4),
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

So the three relaxations of ES that occur are the *slot* of the square denominator in a rational point:
| slot of den = τ² | extra condition | name | provable? |
|---|---|---|---|
| p-free coordinate x | none (gcd(A, m) = 1 "genuine") | Astra source / state | yes, one Dirichlet prime ((J)28 ES^□) |
| p-divisible coordinate z | rad τ | y, v(τ) ≤ e | Claude ES^{(y,e)} | e ≥ q−3 forced at every window (J)64 |
| — | τ = 1 | ES | open |
Astra's *genuineness* gcd(m, h) = 1 is the exact opposite of Claude's *self-muteness* rad τ | y.

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
CAP_POINTWISE Prop 4.1(b) (its side condition "a odd or k′ ≡ 7 (8)" is the s = 2 case of Cor 2.2). So the Astra and
Claude relaxations agree on which Type I levels are alive. Astra's *inherited certificate* [A:SATURATION §2] is
precisely what supplies the non-residue factor (r₀ ∈ −K) that Claude's Prop 4.1 showed is never forced by
H ≡ 4⁻¹ alone; Astra's saturation theorem [A:SATURATION §3] is CAP_POINTWISE Lemma 2.1's box-covering criterion
(mixed-radix version) applied at a Type I level: cover the class −H/c of K = (ℤ/e)^{*2} by the exponent box of the
source primes of H with caps J_q = ⌊(2h_q − v_q(c))/w_q⌋. That is a B2 event (divisor of H² in one class mod e).
