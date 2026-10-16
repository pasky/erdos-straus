# LATTICE_MEETING — moving the slice in Cl(−4p): the meeting point, composition moves, and what a descent can see (O251)

Status: in progress (O251). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on ASTRA_BRIDGE Thm 3.4 (branch side-agent/astra-bridge): for a slice g ≡ 3 (4), gcd(g, p) = 1, h = (g+1)/4,
ρ² ≡ −p (mod g), L_ρ(g) = {(M, Y) : Y ≡ ρM (mod g)}; Claude points (2k, Y), k | h; Astra points (m, 1); ES = (2k, 1).
Throughout p ≡ 1 (mod 4) is prime. Scripts `scripts/z23_*`.

## 0. Iteration log
(I1) First target: a cap descent Y → Y′ < Y by composition 𝔤 → 𝔤𝔩 in Cl(−4p) ending at Y = 1. Before building moves,
asked where they could end. Answer (§1): the end set (Y = 1 points over *all* slices of Cl(−4p)) is a finite,
explicitly enumerable set, and it is **empty** for 99 primes p ≤ 10⁶ (13, 37, 97, 181, 193, …). So no walk inside
Cl(−4p) can terminate for those p, whatever its moves. Hypothesis of the obstruction: the walk stays in ℤ[√−p]
(ET parameter d = 1 / square). Modification: let the walk change the order/field — ES Type II with ET parameter d
is the meeting set of the forms pM² + dY² (disc −4dp), §1.3.

## 1. The meeting locus is finite, explicit, and sometimes empty

**Proposition 1.1 (d = 1 meeting locus; PROVED, elementary).** For p ≡ 1 (4) prime the following sets are in
explicit bijection:
(i) ES points of Thm 3.4(c): (g, ρ, k) with (2k, 1) ∈ L_ρ(g), k | h, over all slices g ≡ 3 (4);
(ii) triples (a, b, k) ∈ ℤ³_{>0} with **a + b = k(4ab − p)**, via g = 4ka − 1, D := (4k²p + 1)/g = 4kb − 1;
(iii) pairs (a, g) with **g | p + 4a²**, g ≡ −1 (mod 4a), via m := (p + 4a²)/g = 4ab − p, k = (g+1)/(4a).
The ES solution is the symmetric triple **4/p = 1/(ab) + 1/(pka) + 1/(pkb)**: window m = 4x − p, x = ab, and the
two slices g = 4y/p − 1, D = 4z/p − 1 (ET Type II with ET's d = 1, c = k). The set 𝓜(p) is finite:
(4a − 1)(4b − 1) ≤ 4p + 1, so min(a, b) ≤ (1 + √(4p+1))/4, max(a, b) ≤ (p+1)/3, k ≤ a + b.
*Proof.* (i)⇔(ii): (2k, 1) ∈ L_ρ(g) with k | h ⟺ g | 4k²p + 1 and 4k | g + 1 (ρ ≡ (2k)⁻¹ is then a root). Put
g = 4ka − 1; gD ≡ 1 and g ≡ −1 (mod 4k) give D = 4kb − 1. Expanding (4ka − 1)(4kb − 1) = 4k²p + 1 gives
4kab − a − b = kp. Conversely such (a, b, k) gives the factorisation. The identity: (kp + a + b)/(pkab) =
k(p + 4ab − p)/(pkab) = 4/p. (ii)⇔(iii): with m = 4ab − p, gm = 16ka²b − 4kap − 4ab + p = 4a(4kab − kp − b) + p =
4a² + p. Conversely, g ≡ −1 (mod 4a) and gm = p + 4a² give m ≡ −p (mod 4a), so b := (p + m)/(4a) ∈ ℤ_{>0}, and
4a(a + b) = 4a² + p + m = m(g + 1) = 4a·km. Finiteness: m ≥ 1 and m | a + b give 4ab − p ≤ a + b. ∎

**Corollary 1.2 (T1 and the classical covering; PROVED).** (a) For n = c², c odd, the analogue of 𝓜 is empty:
g ≡ 3 (4) has a prime factor ℓ ≡ 3 (4) with odd exponent... more simply, ℓ | c² + (2a)², ℓ ≡ 3 (4) forces ℓ | c and
ℓ | a, contradicting g ≡ −1 (mod 4a). (b) If p ≡ 2 (3) then (a, g) = (1, 3) ∈ 𝓜(p). So 𝓜(p) = ∅ forces p ≡ 1 (12).

**Certified computation (CERTIFIED; `scripts/z23_meet.py`, exhaustive by Prop 1.1's bound, every point
checked as an exact ES identity).** Among the 39 175 primes p ≡ 1 (4), p ≤ 10⁶, **𝓜(p) = ∅ for exactly 99**:
13, 37, 97, 181, 193, 541, 673, 757, 1033, 1093, 1297, 1621, 1777, 2293, 2473, 3361, 3877, 6481, … (22 below 10⁴,
23 in (10⁴, 10⁵], 54 in (10⁵, 10⁶]); all ≡ 1 (12). Mean |𝓜(p)| over p ≤ 10⁵: 13.4. Odd squares ≤ 10⁶: all empty.

**Consequence for the O251 descent (PROVED from Prop 1.1 + certified list).** For each of the 99 primes, no sequence of
moves inside the slice lattices of ℤ[√−p] (composition, reduction, translation, Vieta partner) can end at a point
(2k, 1) with k | h: there is none. Claude points (2k, Y), Y > 1, k | h, exist at every slice (any k | h, Y ≡ 2kρ).
So "Y = 1 reachable for every p" is **false** in Cl(−4p); it is a lottery among finitely many candidates (B1/B2:
Prop 1.1(iii) is "p + 4a² has a divisor ≡ −1 (mod 4a)", a = 1, …, √p/2).

### 1.3 Leaving Cl(−4p): ET's d and the forms pM² + dY²
(next step)
