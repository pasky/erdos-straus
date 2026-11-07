# Z62 PARITYF — hunting "the Zagier proof" of Erdős–Straus for primes (NO HOT LEAD; structural results + obstructions)

Lane: tryhard PARITYF, wave z62. Fresh, unprimed attack (no FRONTIER/Z5x/Z6x/BRAINSTORM read). Scripts `scripts/z62_parityf_*.py`, data `data/z62/parityf/`.

**Bottom line.** I did not find a Zagier-type (involution / parity / signed-count) proof. What I did find, all PROVED unless marked:

* a clean *master equation* in bijection with all ES solutions of a prime (§1): ordered solutions of 4/p = 1/x+1/y+1/z ↔ (g,a,b,c,ε), g squarefree, ε ∈ {1,p}³ non-constant, 4gabc = ε_a a + ε_b b + ε_c c;
* the *universal* sets obtained by dropping the 4 — S_n = {gac = n+a+c}, S'_n = {gac = n(a+c)+1} — have **odd cardinality for every prime n ≠ 3** (unique fixed point of the swap), and the ES solutions of the corresponding shapes are exactly their elements with 4 | g (§2). This is the exact analogue of Zagier's S = {x²+4yz = p} with the "trivial" fixed point (1,1,(p−1)/4) ↔ (g,a,c) = (n+2,1,1);
* a Vieta-jump structure linking S_p to two other mutual-divisibility sets (N_p, L_p); but the induced involutions all coincide with the swap (§2.3) — no second involution emerges from jumps;
* Jacobi-symbol constraints: every Type II solution has (4Gac−1 / p) = −1, every Type I solution has (G/p) = −1 (§2.4), which is the exact mechanism killing odd squares (F1) and shows that a Zagier set must "manufacture" a quadratic non-residue;
* a precise statement of what the Zagier template needs and a proof that the natural odd set S_p *cannot* carry it because of F4 (§3), together with numerics showing the natural S₃-symmetric universal sets do not have uniform parity (§4).

Time box ~5h; ES is open; every lemma below was checked numerically before use (scripts listed).

## §0 Mandatory falsifiers (stated first, restated at the end)

Any argument here must survive:

* **(F1) odd squares.** For n = m² odd there is no solution of 4uBC − u − B = n and none of 4abcd = a + b + nc (Type II shapes); n = m² does have other ES solutions. A correct argument for the Type II shapes must use primality.
* **(F2) C-even half.** The C-even half of 4uBC − u − B = p fails for the 12 primes in `data/z58/screens/r8_zeros_1e10.txt` (p ∈ [10¹⁰, 1.1·10¹⁰]); an argument must not "prove" that half.
* **(F3) 285 non-square composites** n ≤ 8·10⁶ (`composite_zeros_le8e6.txt`) have no solution of 4uBC − u − B = n but have other ES solutions.
* **(F4) 14 primes** (`star_prime_zeros.txt`: 409, 577, 5569, …) have no solution of 4uBC − u − B = p; they have Type I solutions and Type II solutions with c > 1 (verified for 409, 577, §4.3).

Status at the end: no claim of the lane proves ES for any new prime, so F1–F4 are not challenged; §3 uses F1/F4 as *obstructions* that any future Zagier set must respect.

## §1 Master equation (PROVED)

Throughout p is an odd prime, ES(p) means 4/p = 1/x + 1/y + 1/z with x,y,z ∈ ℕ.

**Lemma 1.1 (types).** Let p ≥ 5 be prime and (x,y,z) a solution. Then p divides exactly one or exactly two of x,y,z. If p ≡ 1 (mod 4) then x,y,z are pairwise distinct.

*Proof.* 4xyz = p(xy+yz+zx) forces p | xyz. If p | x,y,z, write x=pa etc.: 4 = 1/a+1/b+1/c ≤ 3, impossible. So p divides one or two. If y = z: 4/p − 2/y = 1/x gives x = py/(2(2y−p)); put t = 2y − p (odd), then x = p(p+t)/(4t), so t | p², t ∈ {1,p,p²}; t = p gives x = p/2, and t ∈ {1,p²} give x = p(p+1)/4, (p+1)/4, requiring p ≡ 3 (mod 4). Same for x = y. ∎

Call a solution *Type I* if p divides exactly one denominator and *Type II* if exactly two. For a solution write x = x̃·p^{α}, y = ỹ·p^{β}, z = z̃·p^{γ} with p ∤ x̃ỹz̃, α,β,γ ∈ {0,1}.

**Proposition 1.2 (master equation).** For p ≥ 5 prime, the map
  (g,a,b,c,ε) ↦ (x,y,z) = ( g·bc·p/ε_a , g·ac·p/ε_b , g·ab·p/ε_c )
is a bijection from
  𝔐_p := { (g,a,b,c,ε) : g,a,b,c ∈ ℕ, g squarefree, ε ∈ {1,p}³ not constant, 4gabc = ε_a a + ε_b b + ε_c c }
onto the set of ordered solutions of ES(p). Under it, ε_v = 1 iff p divides the corresponding denominator; Type II ↔ exactly one ε_v = p, Type I ↔ exactly two.

*Proof.* (⇐) Multiply 4gabc = Σ ε_v v by 1/(p·gabc): 4/p = Σ_v ε_v/(p·g·Π_{w≠v} w), and each ε_v/(p g Π_{w≠v} w) is the reciprocal of the positive integer g Π_{w≠v} w · (p/ε_v). (⇒) Given a solution, let (x̃,ỹ,z̃) be the p-free parts. From 4xyz = p(xy+yz+zx) one gets, e.g. in Type II (α=0, β=γ=1), ỹz̃ p = x̃(4ỹz̃ − ỹ − z̃), hence x̃ | ỹz̃ (gcd(x̃,p)=1); symmetrically ỹ | x̃z̃, z̃ | x̃ỹ; Type I is identical with p moved. So P_a := ỹz̃/x̃, P_b := x̃z̃/ỹ, P_c := x̃ỹ/z̃ are integers with P_bP_c = x̃², P_aP_c = ỹ², P_aP_b = z̃²; hence the three have a common squarefree part g and P_a = ga², P_b = gb², P_c = gc². Then x̃ = gbc, ỹ = gac, z̃ = gab, and with ε_v := p^{1−(exponent of p in the v-th denominator)} the ES equation becomes 4gabc = Σ ε_v v. Injectivity: g is the squarefree part of P_a, a = √(P_a/g), etc. (Alternative normalisation gcd(a,b,c) = 1 is equivalent via (g,a,b,c) ↦ (g/m², ma, mb, mc).) ∎

Checked by `z62_parityf_master.py` (assert) for all ordered solutions of every prime ≤ 200 and for 409, 577.

**Corollary 1.3 (divisibility form).** ES(p) ⟺ ∃ a,b,c ∈ ℕ and a non-constant ε ∈ {1,p}³ with 4abc | ε_a a + ε_b b + ε_c c. (Then g is the quotient.)

**Corollary 1.4 (two shapes).** Every Type II solution is, up to order, 4Gabc = a + b + pc (equivalently c(4Gab − p) = a + b, i.e. the brief's 4abcd = a + b + pc with d = G); the shape 4uBC − u − B = p ("(★)") is exactly the sub-case c = 1. Every Type I solution is 4Gabc = pa + pb + c, equivalently c(4Gab − 1) = p(a + b); for primes p ∤ c, so 4Gab − 1 = pk with k | a + b.

*Proof.* Pattern with one ε = p (say ε_c): 4Gabc = a + b + pc. With c = 1: 4Gab − a − b = p is (★) with (u,B,C) = (a,b,G). Pattern with two: 4Gabc = pa + pb + c ⟹ c(4Gab − 1) = p(a+b); if p | c then c'(4Gab − 1) = a + b with c = pc', impossible since 4Gab − 1 ≥ 4ab − 1 > a + b for all a,b ≥ 1 (4ab − a − b − 1 ≥ 2ab − 1 > 0). ∎

**Proposition 1.5 ((m,k)-form).** For p ≡ 1 (mod 4) prime:
 Type II ⟺ ∃ k ≡ 3 (4), m = (p + k)/4 has a factorisation m = g·a·b with k | a + b;
 Type I ⟺ ∃ k ≡ 3 (4), m = (pk + 1)/4 has a factorisation m = g·a·b with k | a + b.

*Proof.* Type II: c(4Gab − p) = a + b; put k := 4Gab − p ≡ 3 (4) (since p ≡ 1 (4)), m := Gab = (p + k)/4, c = (a+b)/k. Conversely such (k,g,a,b) give c and the master equation. Type I: k := (4Gab − 1)/p ∈ ℕ (Cor. 1.4), m := Gab = (pk+1)/4, k | a+b, c := (a+b)/k. ∎

Equivalently (dividing the identity 4/p = 4k/(pk+ε) + 4ε/(p(pk+ε))): ES(p) ⟺ ∃ k ≡ 3 (4), ε ∈ {1,p} with 4k/(pk+ε) a sum of two unit fractions. (The two cases merge: 4k/(pk+1) = 4K/(p(K+1)) with K = pk, so this is just "∃ j: 4/p − 1/(pj) is a sum of two unit fractions", i.e. a solution with a denominator pj — trivially necessary by Lemma 1.1. I record it because it exhibits the ε = 1 / ε = p duality cleanly.)

**Remark 1.6 (the p ↔ 1 duality).** In the (x, t = 4x − p) coordinates, with δ a divisor of x²: Type II ⟺ (4x−p) | 4δ + p, Type I ⟺ (4x−p) | 4δ + 1 (or 4δ + p², the complementary divisor). So both types are "4δ + p^i ≡ 0 (mod 4x − p), δ | x²", i ∈ {0,1,2}; the swap y ↔ z is (δ,i) ↦ (x²/δ, 2−i). (Proof: with t = 4x − p, d = ty − px, d' = tz − px one has dd' = p²x² and gcd(t,px) = 1; write d = p^iδ with δ | x². The condition t | d + px, using p ≡ 4x (mod t), reads p^iδ ≡ −4x², i.e. δ ≡ −4^{1−i}x^{2−i}; the three classes −4x², −x, −1/4 (i = 0,1,2) equal −p²/4, −p/4, −1/4 mod t, i.e. 4δ + p^{2−i} ≡ 0. Type II is i = 1 (p ∥ d), Type I is i ∈ {0,2}.) Checked numerically inside `z62_parityf_enum.py` runs.

## §2 Odd universal sets (PROVED) — the exact analogue of Zagier's S

### 2.1 Type II, c = 1: the set S_n

**Definition.** For n ∈ ℕ, S_n := {(g,a,c) ∈ ℕ³ : gac = n + a + c} ≅ {(a,c) ∈ ℕ² : ac | n + a + c} (g is the quotient).

**Theorem 2.1.** (i) The swap τ(g,a,c) = (g,c,a) is an involution of S_n whose fixed points are the (g,a,a) with a | n and a | n/a + 2 (g = (n/a + 2)/a). For n = p prime ≥ 5 the only fixed point is (p+2,1,1); hence |S_p| is odd. (For composite n there can be more: n = 225 has (227,1,1) and (3,9,9), so |S_225| is even; most odd squares ≤ 1225 have only (n+2,1,1) and |S_{m²}| odd — the parity of |S_n| does not separate primes from squares.)
(ii) For every n, the elements of S_n with 4 | g are in bijection with the solutions (u,B,C) of 4uBC − u − B = n via (g,a,c) = (4C,u,B). Hence (★)(n) ⟺ S_n has an element with 4 | g.
(iii) For p prime ≥ 5 every (a,c) ∈ S_p has gcd(a,c) = 1, so S_p = {(a,c) : a | p + c, c | p + a}.
(iv) The slices S_p^{(g)} := {g fixed} satisfy |S_p^{(g)}| = #{d | gp + 1 : d ≡ −1 (mod g)}; |S_p^{(g)}| is even for every g ≠ p + 2 and odd for g = p + 2. In particular Σ_{4|g} |S_p^{(g)}| = R(p) is even and Σ_{g ≡ 3 (4)} |S_p^{(g)}| is odd.

*Proof.* (i) g a² = n + 2a ⟺ a(ga − 2) = n, so a | n and n/a + 2 = ga, i.e. a | n/a + 2. For n = p: a = 1 gives g = p + 2; a = p gives p | 3. (ii) Put g = 4C. (iii) If d = gcd(a,c) > 1 then d² | ac | p + a + c and d | a + c force d | p, so d = p; writing a = pa', c = pc' gives p a'c' | 1 + a' + c', impossible for p ≥ 5. Then ac | p + a + c ⟺ a | p + c and c | p + a. (iv) (ga − 1)(gc − 1) = g(gac − a − c) + 1 = gp + 1 and d := ga − 1 ≡ −1 (g) determines (a,c); conversely a divisor d ≡ −1 (g) of gp + 1 has complementary divisor ≡ −1 (g) because gp + 1 ≡ 1 (g). The involution d ↦ (gp+1)/d on this slice is τ; it is free unless gp + 1 = d² with d ≡ −1 (g), which by (i) happens only for g = p + 2 (d = p + 1). ∎

Numerically (`data/z62/parityf/c1_counts.txt`, n ≤ 700): |S_n| odd for all primes; the g (mod 4) slice counts are [even, even, even, odd]; ES2 := #{4 | g} is even, and zero exactly for n ∈ {odd squares} ∪ {409, 577} in range.

**Remark (the Zagier dictionary).** Zagier: S = {x² + 4yz = p}, τ = (y ↔ z) with Fix(τ) = representations p = x² + 4y², and σ the "windmill" involution with the single fixed point (1,1,(p−1)/4). Here: S_p = {gac − a − c = p}, τ = swap with the single fixed point (p+2,1,1), and the *target* elements (4 | g) are not fixed points of τ (τ is free on them) — the target is a *congruence* condition, not a symmetry condition. This is the first structural difference from Zagier, and it is forced: by Lemma 1.1 every set consisting of ES solutions of p ≡ 1 (4) carries a free involution.

### 2.2 Type I, c = 1: the set S'_n

**Theorem 2.2.** S'_n := {(g,a,c) : gac = n(a + c) + 1} ≅ {(a,c) : ac | n(a+c) + 1} = {(a,c) : a | nc + 1, c | na + 1}. The swap has the unique fixed point (2n+1,1,1) for every n (g a² = 2na + 1 forces a | 1), so |S'_n| is odd for every n. Elements with 4 | g are exactly the Type I solutions with unmarked variable c = 1 (4Gab = pa + pb + 1).

Numerically (same file) |S'_n| is odd throughout, ES1 := #{4|g} is even, ES1 > 0 for every prime ≤ 700 including 409, 577, and ES1 = 0 for every odd square ≤ 700 (consistent with the Jacobi constraint, §2.4).

### 2.3 Vieta jumps: three coordinate systems, one involution

Define N_p := {(a,D) : a | D + 1, D | p + a} and L_p := {(g,D) : g | D + 1, D | pg + 1}.

**Theorem 2.3.** For p ≥ 5 prime:
(i) K: (a,c) ↦ (a, (p+a)/c) is a bijection S_p → N_p (inverse: the same formula);
(ii) J: (a,D) ↦ ((D+1)/a, D) is a bijection N_p → L_p (inverse: (g,D) ↦ ((D+1)/g, D));
(iii) ι: (g,D) ↦ (g, (pg+1)/D) is an involution of L_p preserving g, with the unique fixed point (p+2, p+1);
(iv) ι = J K τ K⁻¹ J⁻¹ — i.e. in S_p-coordinates ι is the swap τ. So |S_p| = |N_p| = |L_p| is odd and the three "jumps" produce no new involution.

*Proof.* (i) For (a,c) ∈ S_p (so gcd(a,c) = 1, a | p + c, c | p + a) put D = (p+a)/c; D | p + a and a | D + 1 ⟺ ac | p + a + c ✓. Conversely for (a,D) ∈ N_p put c = (p+a)/D; then c | p + a and a | p + c ⟺ aD | pD + p + a ⟺ a | p(D+1) ⟺ a | D + 1 (gcd(a,p) = 1: if p | a then D | p + a forces p | D, and a | D + 1 gives p | 1). (ii) g := (D+1)/a; D | pg + 1 ⟺ aD | p(D+1) + a ⟺ D | p + a ✓ (and a | D+1 ⟺ g | D+1). (iii) (pg+1)/D ≡ −1 (mod g) because pg + 1 ≡ 1 and D ≡ −1 (mod g); fixed points: D² = pg + 1 with g | D + 1 ⟹ (D−1)(D+1) = pg, and g | D + 1 gives (D − 1) | p, so D ∈ {2, p+1}; D = 2 needs g = 3/p. (iv) Direct computation: in the coordinates (a,D,b) with D = ga − 1, b = (pg+1)/D = gc − 1, one has ι(a,D,b) = (c, b, D) i.e. a ↔ c. ∎ (Verified by `z62_parityf_jumps.py` for all primes ≡ 1 (4) below 60.)

The analogous chain for S'_p is S'_p ↔ M_p := {a | p + c, c | pa + 1} ↔ T_p := {a | p + c, c | p² + a}, the last carrying a self-jump with unique fixed point (2p+1, p+1).

### 2.4 Jacobi constraints (PROVED) — why odd squares die, and what a Zagier set must manufacture

**Proposition 2.4.** Let p ≡ 1 (mod 4) be prime.
(i) If 4Gabc = a + b + pc (Type II, any c), then d₁ := 4Gac − 1 and d₂ := 4Gbc − 1 satisfy (d_i/p) = −1.
(ii) If 4Gabc = pa + pb + c (Type I), then (G/p) = −1 (and hence (ab/p) = −1).
(iii) Consequently neither shape has solutions for n = m² in place of p *when the argument is read with n prime-like*; concretely for Type II: d₁ | 4Gc²n + 1 and d₁ ≡ −1 (mod 4Gc) give the Jacobi symbol (n/d₁) = −1, impossible for n = m². (This is F1.)

*Proof.* (i) d₁d₂ = 16G²abc² − 4Gc(a+b) + 1 = 4Gc(4Gabc − a − b) + 1 = 4Gpc² + 1. So −4Gpc² ≡ 1 (mod d₁), i.e. −Gp is a square mod d₁ (as (2c)⁻¹ exists). Thus (−1/d₁)(G/d₁)(p/d₁) = 1. Since d₁ ≡ −1 (mod 4Gc) we have d₁ ≡ 3 (mod 4), so (−1/d₁) = −1, and (G/d₁) = 1: for G = 2^s G' with G' odd, (2/d₁) = 1 because d₁ ≡ −1 (mod 8) when s ≥ 1, and (G'/d₁) = (d₁/G')(−1)^{(G'−1)/2·(d₁−1)/2} = (−1/G')(−1)^{(G'−1)/2} = 1 because d₁ ≡ −1 (mod G') and d₁ ≡ 3 (mod 4). Hence (p/d₁) = −1 and, by reciprocity (p ≡ 1 (4)), (d₁/p) = −1. Symmetric for d₂. (ii) By Cor. 1.4, 4Gab − 1 = pk with k | a + b; put w := (a+b)/k, so b = kw − a and 4Ga(kw − a) − 1 = pk, i.e. k(4Gaw − p) = 4Ga² + 1. Hence D := 4Gaw − p is a positive divisor of 4Ga² + 1 with D ≡ −p (mod 4Ga). From 4Ga² ≡ −1 (mod D): (−G/D) = 1. Since D ≡ −p ≡ 3 (mod 4), (−1/D) = −1, so (G/D) = −1. Write G = 2^sG' with G' odd. If s ≥ 1 then 8 | 4Ga so D ≡ −p (mod 8), whence (2/D) = (2/p) (both are +1 if p ≡ 1 (8), both −1 if p ≡ 5 (8)). For the odd part, D ≡ 3 (4) gives (G'/D) = (D/G')(−1)^{(G'−1)/2} = (−p/G')(−1)^{(G'−1)/2} = (−1/G')(−1)^{(G'−1)/2}(p/G') = (p/G') = (G'/p) (p ≡ 1 (4)). So (G/D) = (2/p)^s(G'/p) = (G/p), i.e. (G/p) = −1. Finally 4Gab ≡ 1 (mod p) gives (Gab/p) = 1, so (ab/p) = −1. (iii) is (i) with n in place of p: the derivation of (n/d₁) = −1 never used primality of n; but (m²/d₁) = 1. ∎

Verified (`z62_parityf_jumps.py`, `data/z62/parityf/g_legendre.txt`): for all primes ≡ 1 (4) below 60 every 4 | g element of U_II has (gac−1 / p) = (gbc−1 / p) = −1 and every 4 | g element of U_I has (g/4 / p) = −1; and in the master listing for primes ≤ 200, Type I always has g a non-residue while Type II has g of either character.

**Consequence for the Zagier programme.** A parity/involution argument that proves existence of a Type I or Type II solution for every prime p ≡ 1 (24) must, as a by-product, exhibit a specific quadratic non-residue mod p (d₁ resp. G) that divides a specific integer (4Gc²p + 1 resp. 4Ga² + 1). In Zagier's proof the analogous "by-product" (−1/p) = 1 is an *input* (p ≡ 1 (4) is what makes (1,1,(p−1)/4) exist). No congruence condition on p (p ≡ 1 (24), or any fixed modulus) supplies a non-residue witness, because by Dirichlet there are primes ≡ 1 (24) that are squares modulo any prescribed finite set of odd moduli — so the Zagier set cannot have its unique σ-fixed point be a congruence-defined element of the kind (n+2,1,1); the fixed point must itself encode divisibility of a p-dependent integer. This does not rule out such a set, but it says the set must be of a different nature from {x² + 4yz = p} (where σ's fixed point is p-independent in shape).

### 2.5 S_p is a forest (PROVED)

Let Γ_p be the graph on ℕ with an edge {a,c} (a ≠ c) iff gcd(a,c) = 1, a | p + c and c | p + a. By Thm 2.1(iii), S_p = {ordered edges of Γ_p} ∪ {(1,1)}, so |S_p| = 2|E(Γ_p)| + 1.

**Theorem 2.5.** (i) If {a,c} is an edge with a < c, then a = (−p mod c), the least positive residue. Hence every vertex has at most one smaller neighbour and Γ_p is a forest; |V(Γ_p)| − |E(Γ_p)| = #roots, where the roots are 1 and those c > 1 which have a neighbour but for which (−p mod c) ∤ p + c.
(ii) The neighbours of 1 are exactly the divisors c > 1 of p + 1. The children of a vertex a (neighbours c > a) are the c = (p+a)/D for divisors D of p + a with D ≡ −1 (mod a), D < (p+a)/a and gcd(a,c)=1; such a child gives an ES solution ((★) with (u,B,C) = (a,c,(D+1)/(4a))) iff D ≡ −1 (mod 4a).
(iii) ES-edges are never fixed by anything natural: the edge-involution (a,c) ↦ (c,a) of S_p is free on them.

*Proof.* (i) c | p + a and 1 ≤ a < c give a ≡ −p (mod c) with a the least positive residue (a ≠ 0 since c ∤ p for 1 < c; c = p is impossible because then p | a). A cycle would contain a vertex with two smaller neighbours. (ii) is the (u,d)-form: p + a = D·c, D ≡ −1 (mod a) ⟺ c ≡ −p (mod a) ⟺ a | p + c; and 4 | g = (D+1)/a ⟺ D ≡ −1 (mod 4a). ∎

Data (`data/z62/parityf/forest.txt`): Γ_p is a tree for p ∈ {5,13,17,29,37,41,53,97,1009}, has roots {1,4} for 73, 241, {1,7} for 193, {1,4,11} for 409, {1,4,6,8} for 577, {1,7,8,11,24,40} for 5569; the F4 primes 409, 577, 5569 have no ES-edge, as they must. All ES-edges observed have small parent (a ≤ 5).

Remark. The parent map c ↦ (−p mod c) is a "parallel Euclid" descent; the forest is the ES analogue of the continued-fraction / reduction structure behind Zagier's windmill. But a forest has only sibling-permuting automorphisms, so no Lefschetz-type involution with prescribed fixed edges exists on Γ_p itself (a tree automorphism of order 2 fixes a vertex or inverts an edge, and nothing forces the inverted edge to be an ES-edge).

## §3 The Zagier template and what it must look like for ES (PROVED obstructions)

**Template.** A finite set 𝒳_p with two involutions σ, τ; |Fix σ| = 1 by an argument using primality; Fix τ ≠ ∅ ⟹ ES(p). Then |𝒳_p| ≡ 1 ≡ |Fix τ| (mod 2).

**Lemma 3.1 (ES solutions can only be fixed points, never the set).** Let p ≡ 1 (4) be prime and let 𝒴 be any set of ES solutions of p closed under one of the swaps y ↔ z (in any of the coordinate systems of §1–§2: (u,B,C) ↦ (B,u,C), (g,a,b,c,ε) ↦ (g,b,a,c,ε'), (k,δ) ↦ (k, x²/δ), …). Then |𝒴| is even. In particular R(p), the Type I count, the Type II count and |𝔐_p| are all even, and the Zagier set 𝒳_p cannot consist of ES solutions: the ES solutions must be (a subset of) Fix τ for an involution τ of a strictly larger set.

*Proof.* Lemma 1.1: x,y,z distinct, so the swap is free. ∎

**Lemma 3.2 (the natural larger set).** Dropping the "4" is exactly the Zagier enlargement: S_n = {gac = n + a + c} ⊃ {4 | g} = (★)-solutions, and the swap τ on S_n has the single fixed point (n+2,1,1) for n prime ≠ 3 (Thm 2.1). So S_p satisfies the "|Fix σ| = 1 by primality" half of the template with σ = τ = swap — but the target is {4 | g}, a congruence class on which τ is free, and |{4|g}| is even. A second involution σ' with Fix σ' ⊂ {4 | g} would have an odd number of fixed points inside an even set — not contradictory, but σ' must then pair some element of {4 ∤ g} (odd cardinality |S_p| − R(p)) with an element of {4 | g}.

**Theorem 3.3 (S_p alone is dead; what the Zagier set must contain).** For p ∈ {409, 577, 5569, …} (F4) one has {4 | g} = ∅ in S_p, so no involution of S_p has all its fixed points in {4 | g}. Hence any Zagier set for all primes ≡ 1 (24) must contain elements producing Type II solutions with c > 1 (shape 4Gabc = a + b + pc, c ≥ 2) and/or Type I solutions (4Gabc = pa + pb + c). For the 12 primes of F2 it must contain elements with C odd (g ≡ 4 (mod 8) in S_p) or of the other shapes.

*Proof.* F4 data + Thm 2.1(ii); for 409, 577 the actual solutions were enumerated (`data/z62/parityf/types_409_577.txt`): 409 has Type II solutions with marked c ∈ {2,3,4,15} and Type I; 577 similarly (c ∈ {2,5,10,21}). ∎

**Theorem 3.4 (odd squares do not obstruct a universal argument; they obstruct a Type-II-only one).** Let U_II(n) := {(g,a,b,c) : gabc = a + b + nc}, U_I(n) := {(g,a,b,c) : gabc = na + nb + c}. For every n (prime or not), an element of U_II(n) ∪ U_I(n) with 4 | g yields an ES solution of n. For odd squares n = m², U_II(n) has no element with 4 | g (Prop. 2.4(iii)), while U_I(n) does (e.g. n = 9: (4,4,1,3) ↦ 4/9 = 1/3 + 1/12 + 1/36). Therefore: (a) a Zagier argument on U_II alone must use primality (F1), and (b) a Zagier argument on U_I ∪ U_II that worked for all n ≡ 1 (24) would be a proof of ES for all such n, consistent with F1–F4 (no falsifier bites), but by Lemma 3.1 it cannot be a parity count of ES solutions; it would have to be a parity count of a set like U_I ∪ U_II in which the ES solutions are the 4 | g elements — and those sets do not have uniform parity (§4.2), because the swap's fixed points are 2 + #{(a ≥ 2, δ | 2a) : a² | n + δ} on U_II and 2 + s(n+1) + s(2n+1) on U_I, s(N) := #{a : a² | N} (both computed in §4.2 and verified).

*Proof of the fixed-point counts.* U_II, a = b: c(ga² − n) = 2a, so ga² − n = δ with δ | 2a, c = 2a/δ, and a² | n + δ; a = 1 gives (n+2,1,1,1), (n+1,1,1,2). U_I, a = b: c(ga² − 1) = 2na forces a | c (gcd(a, ga² − 1) = 1), c = ac', c'(ga² − 1) = 2n; for n = p prime, ga² − 1 ∈ {1,2,p,2p}: (2,1,1,2p), (3,1,1,p), and (g,a,a,2a) for each a² | p + 1, (g,a,a,a) for each a² | 2p + 1. ∎

**Proposition 3.5 (what a σ with one fixed point can and cannot encode).** Suppose 𝒳_n is defined uniformly for all n ≡ 1 (24) by polynomial equations/congruences in the coordinates (as S_n, U_I(n), U_II(n) are), σ is an involution of 𝒳_n defined piecewise by maps that are polynomial in the coordinates and in n, and the fixed points of σ are described by equations whose solution count for n prime is 1 "because a divisor of n must be 1 or n" (as in Zagier). Then the proof shows |𝒳_p| ≡ 1 for all primes p ≡ 1 (24) and hence — if the ES elements are the fixed points of a second involution τ — produces for each such p a Type I/II solution, hence (Prop. 2.4) a quadratic non-residue G or d₁ mod p dividing 4Ga² + 1 resp. 4Gc²p + 1. There is no contradiction in this, but it means the argument would be strictly stronger than anything a congruence condition on p can give: no such set can be a union of "residue-class families" like Zagier's (where the fixed point (1,1,(p−1)/4) only needs p ≡ 1 (4)). CONDITIONAL on the heuristic that Zagier-type constructions are "congruence-defined": this is why the many natural candidates tried here (S_n, S'_n, N_n, L_n, U_I, U_II, the (K,y,z)-set {4/p = 1/y + 1/z + 2/(pM)}, Zagier-type sets {x² + 4yz = 4Cp + 1}) either have the wrong parity or have fixed points unrelated to ES. EVIDENCE, not a theorem.

**Scorecard of candidate sets (all computed; §4):**

| set | |·| mod 2 for primes | swap fixed points | ES elements | verdict |
|---|---|---|---|---|
| S_n = {gac = n+a+c} | 1 (n ≠ 3) | (n+2,1,1) | 4 | g (Type II, c=1) | odd, but F4 kills it alone |
| S'_n = {gac = n(a+c)+1} | 1 (all n) | (2n+1,1,1) | 4 | g (Type I, c=1) | odd; squares have none |
| U_II(n) (all Type II) | varies | 2 + sporadic | 4 | g | no uniform parity |
| U_I(n) (all Type I) | varies | 2 + s(n+1) + s(2n+1) | 4 | g | no uniform parity |
| {(M,y,z): 4/p = 1/y+1/z+2/(pM)} | 0 | (1,p,p), ((p+1)/2,(p+1)/2,(p+1)/2) | M even | even |
| {x²+4yz = 4Cp+1} (fixed C) | ≡ r₂'(4Cp+1) | Zagier's | none natural | irrelevant to d ≡ −1 (4C) |
| 𝔐_p (master, ordered) | 0 | none | all | even (Lemma 3.1) |

## §4 Numerics

### 4.1 c = 1 universal sets (`scripts/z62_parityf_c1.py`, `data/z62/parityf/c1_counts.txt`, n ≤ 700)
For every prime p ≡ 1 (4) ≤ 700: |S_p| odd, |S'_p| odd; the g mod 4 slice counts of S_p are [even, even, even, odd] and of S'_p likewise; ES2 = #{4|g in S_p} = 0 exactly for p ∈ {409, 577} (and all odd squares); ES1 = #{4|g in S'_p} > 0 for every prime in range and = 0 for every odd square in range. (So within this range "Type I with c = 1 or Type II with c = 1" covers every prime — EVIDENCE only; the brief's 14 primes show c = 1 Type II fails, and I have not checked whether Type I with c = 1 ever fails.)

### 4.2 Full universal sets (`scripts/z62_parityf_universal.py`, `data/z62/parityf/universal_counts.txt`)
|U_II(p)| = 26, 40, 53, 74, 58, 82, 99, 79, 79, 141, 106 and |U_I(p)| = 48, 87, 109, 152, 133, 172, 211, 172, 183, 297, 229 for p = 5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97; swap-fixed counts 2,2,3,2,2,2,3,3,3,3,4 resp. 4,5,5,4,5,4,5,4,5,5,5, matching the formulas of Thm 3.4 (e.g. p = 13: s(14) + s(27) = 1 + 2). ES1, ES2 even throughout for primes; U_I(9) has 3 elements with 4 | g (a = b allowed for composite n).

### 4.3 Solutions of the F4 primes (`scripts/z62_parityf_types.py`, `data/z62/parityf/types_409_577.txt`)
409: 84 ordered solutions; Type II with marked c ∈ {2,3,4,15} (none with c = 1), Type I with unmarked c ∈ {1,2,3,4,5,7,11}. 577: Type II with c ∈ {2,5,10,21}, Type I with c ∈ {1,2,3,5,10,29,31}. So F4 primes have c = 1 Type I solutions (4Gab = p(a+b) + 1 solvable).

### 4.4 Jacobi (`scripts/z62_parityf_gleg.py`, `scripts/z62_parityf_jumps.py`)
For primes ≤ 200: every Type I solution has (g/p) = −1; Type II has both signs. For primes < 60: (gac − 1 / p) = (gbc − 1 / p) = −1 on all 4 | g elements of U_II, (g/4 / p) = −1 on all 4 | g elements of U_I.

### 4.5 The (K,y,z) set (`scripts/z62_parityf_kset.py`)
𝒮_p = {(K,y,z) : K odd, 4K/(p(K+1)) = 1/y + 1/z}: |𝒮_p/swap| = 7, 11, 14, 18 for p = 5, 13, 17, 29 with exactly 2 swap-fixed elements; ES elements are K ≡ 3 (4) and they are just "solutions with a distinguished denominator pj".

## §5 Status and verdict

* PROVED: Prop. 1.2 (master bijection), Cor. 1.3–1.4, Prop. 1.5, Thm 2.1, Thm 2.2, Thm 2.3, Prop. 2.4, Thm 2.5, Lemma 3.1, Thm 3.3 (given the certified F4 data), Thm 3.4 fixed-point formulas.
* EVIDENCE: §4.1 coverage by c = 1 shapes up to 700; §4.2 non-uniform parities.
* NOT FOUND: a second involution. The structural reasons collected here — (a) every set of ES solutions carries a free involution, so ES solutions must be fixed points of τ on a larger set; (b) the natural larger set S_n has the right "one fixed point for primes" property but the target is a congruence class on which the only available involution is free; (c) the Vieta jumps of S_p all reduce to the swap; (d) F4 forces Type I / c > 1 elements in, and the natural sets containing them have no uniform parity; (e) any successful argument must manufacture a quadratic non-residue witness (Prop. 2.4), which no congruence-defined fixed point supplies — make me believe that "the Zagier proof" of ES, if it exists, is not a parity argument on a set defined by the ES equation itself in any of the coordinate systems above. It would need a genuinely different finite set (e.g. one built from the forest Γ_p or from a sum over C of representation numbers of 4Cp + 1 by forms of discriminant −4C, where real characters mod 4C enter the count #{d | 4Cp+1 : d ≡ −1 (4C)} = φ(4C)⁻¹ Σ_χ χ(−1) Σ_{d|4Cp+1} χ(d)) — I did not find one.

## §0′ Falsifiers restated
No claim above proves ES for any prime; the lane's results are reformulations, parity facts about auxiliary sets, and obstructions. F1: the only "proofs of existence" here (Thm 2.1(i), 2.2) assert |S_p|, |S'_p| odd — true also for many odd squares (|S_9| = 11 via the fixed point (11,1,1)), and they do not assert existence of 4 | g elements; the Jacobi constraint Prop. 2.4(iii) is exactly what fails at squares. F2: nothing here distinguishes C even/odd. F3, F4: Thm 3.3 uses them as constraints; nothing contradicts them.

### 4.6 Square-decorated counts (`scripts/z62_parityf_decor.py`, `data/z62/parityf/decorations.txt`)
Since Fix τ in a Zagier set is a *decorated* solution set with Σ m(sol) odd, and the natural decorations "split a variable into a product" give parity #{sol : variable is a square}, I tabulated, for all primes ≡ 1 (4) ≤ 600 and odd squares ≤ 600, the parities of #{unordered solutions with Q a perfect square} for Q ∈ {g, Π marked, Π unmarked, g·Π marked, g·Π unmarked, abc, gabc, min denominator, max denominator, x̃ỹz̃, a+b+c, …} and the indicator counts T₁, T₂. None is odd for all primes (best: none; "max denominator square" is even for all 51 primes, "Type I with g = 1" is identically 0 for primes — the numerical shadow of Prop. 2.4(ii)). So no "one-variable-split" Zagier set exists in these coordinates. EVIDENCE.
