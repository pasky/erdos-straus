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
with gcd(n, e) = 1. The following are in bijection:
(a) divisors r | H² with e | n² + 4r;
(b) rational points (u, v, pH) of p with u = U/n², gcd(U, n) = 1, n²v ∈ ℤ (so twist τ | n);
via U = (n²H + r)/e, v = HU/r, and conversely r = eU − n²H. **ES at level e** (an integral point with x = pH) is the
case n = 1: a divisor r | H² with r ≡ −4⁻¹ (mod e), i.e. the classical Type I criterion "−1 ∈ Σ_e(H)" of the brief.
*Proof.* (a)⇒(b): 4(n²H + r) = n²(pe + 1) + 4r ≡ n² + 4r ≡ 0 (mod e) and gcd(4, e) = 1, so U ∈ ℤ_{>0}. gcd(r, e) = 1
(4H ≡ 1 mod e), and eHU = n²H² + rH ≡ 0 (mod r), so r | HU: v ∈ ℤ, hence n²v ∈ ℤ. n²/U + 1/v = (n²H + r)/(HU) = e/H =
4/p − 1/(pH). gcd(U, n): a prime ℓ | U, n has ℓ | r = eU − n²H, and then ℓ | eU − r … ; use instead gcd(r, n) = 1
(ℓ | r, n ⇒ ℓ | n² + 4r ⇒ … ℓ | e·(n²+4r)/e — and ℓ | n, ℓ | r give ℓ | eU, ℓ ∤ e ⇒ ℓ | U); so gcd(U, n) = gcd(r, n)
[A:STR (29)], and the twist is n/… ≤ n. (R-self: the bijection must therefore be stated on the subset gcd(r, n) = 1 —
see the corrected statement below.)
