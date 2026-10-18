# HARD_PAIR — why 193 and 2521 are hardest in both worlds (task O264, cheap check)

Status: in progress (unreviewed). **ES is not solved here; nothing below proves any case of ES.** Labels as in
DISCOVERIES.md. Memos `BRAINSTORM/z34_*.md`; scripts `scripts/z34_*`; logs `logs/z34_*` (tiny).
Throughout p ≡ 1 (mod 4) is prime. Type A = López's b = 1 line (B1_LINE): cp + a + 1 = 4acd, the solution
4/p = 1/(ad) + 1/(acdp) + 1/(cdp). Astra source (q, m, s): q ≡ 3 (4), qs = pm² + 1, h = (q+1)/4, rational point
4/p = m²/(sh) + 1/(psh) + 1/(ph) (ASTRA_BRIDGE Lemma 1.3); genuine ⟺ gcd(m, h) = 1.

## 0. Iteration log
(I1) Read B1_LINE, ASTRA_BRIDGE §1–4, LATTICE_MEETING §1. Observation: Astra's source equation pm² + 1 = qs is
López's dual-coordinate Type A equation cp + 1 = Qa (B1_LINE §5(c)) with c = m², minus the congruence Q ≡ −1 (mod 4c).

## 1. Goal 1: Type A in Astra's coordinates (PROVED, elementary)

**Definition 1.1.** A *generalized source* of p is a triple (q, c, s) of positive integers with q ≡ 3 (mod 4) and
qs = pc + 1. Put h := (q + 1)/4 and P(q, c, s) := (sh/c, psh, ph). For a slice q with gcd(q, p) = 1 let
c_q ∈ [1, q − 1] be the least positive residue of −p⁻¹ (mod q).

**Theorem 1.2 (one equation, three side conditions; PROVED).** Let p ≡ 1 (4) be prime.
(a) For every generalized source, 4/p = c/(sh) + 1/(psh) + 1/(ph), and gcd(c, s) = 1.
(b) Astra's sources are exactly the generalized sources with c = m² a perfect square (Astra's twist m).
(c) P(q, c, s) is integral ⟺ c | h. The generalized sources with c | h are in bijection with the Type A solutions
    (a, c, d) via (q, c, s) = (4cd − 1, c, a), d = h/c, and then P(q, c, s) = (ad, acdp, cdp).
(d) At a fixed slice q, c runs through the class −p⁻¹ (mod q). Hence Type A has a solution with López divisor
    w = q ⟺ c_q | h, and N₁(p) = #{q ≡ 3 (4) : gcd(q, p) = 1, c_q | (q + 1)/4} (each such q gives one solution).
(e) Slice q carries an Astra source ⟺ c_q is a square unit mod q; it then carries genuine sources (gcd(m, h) = 1).
    An Astra source is integral on arrival (Astra's x = sh/m² ∈ ℤ, i.e. "scalar removal") ⟺ m² | h ⟺ c_q = m².
*Proof.* (a) c/(sh) + 1/(psh) + 1/(ph) = (pc + 1 + s)/(psh) = s(q + 1)/(psh) = 4/p; qs − pc = 1 gives the gcd.
(b) Definition (ASTRA_BRIDGE Lemma 1.3). (c) gcd(c, s) = 1, so c | sh ⟺ c | h. If c | h put a = s, d = h/c: then
q = 4cd − 1 and qa = cp + 1 is cp + a + 1 = 4acd, and sh/c = ad, psh = acdp, ph = cdp. Conversely a Type A solution
has (4cd − 1)a = cp + 1, a generalized source with c | cd = h. (d) qs = pc + 1 ⟺ c ≡ −p⁻¹ (mod q) (then s ∈ ℤ_{>0});
c | h and h < q force c = c_q. Two Type A solutions with the same q have the same c = c_q, d = h/c_q, a = (c_q p + 1)/q.
(e) The source condition q | pm² + 1 is m² ≡ c_q (mod q). Genuine lifts: gcd(q, h) = 1 (4h ≡ 1 mod q), so CRT picks
m in the root class with m ≡ 1 mod every prime of h. Integrality: by (c) with c = m², m² | h; then m² ≡ c_q and
m² ≤ h < q give m² = c_q. ∎

**Corollary 1.3 (what Type A failure means for Astra; PROVED).** If Type A fails at p then
(i) no Astra source, genuine or not, on any slice is integral on arrival (m² ∤ h always);
(ii) in particular (m = 1, c_q = 1 ⟺ q | p + 1) every odd prime factor of p + 1 is ≡ 1 (mod 4):
    194 = 2·97, 2522 = 2·13·97, 66530 = 2·5·6653;
(iii) at every split slice q, reducing Astra's twist square modulo the slice, m² ↦ c_q (a move that leaves the
    slice and y = ph fixed but in general leaves the square class of integers), never lands on a divisor of h;
(iv) every ES solution of p (in particular every exit of an Astra route) is Type I, or Type II with both ET
    parameters a, b ≥ 2 (ET form (abd, acdp, bcdp)); none has López's shape (du, dv, duv).
The converse of (i) is false, and so is "Type A fails ⟺ no genuine source on any slice" (genuine sources exist on
every split slice, and every p has split slices: any prime q ≡ 3 (4) with (q/p) = −1).
*Proof.* (i)–(iii) are Thm 1.2(c)–(e). (iv): Type A is ET Type II with b = 1 (or a = 1 by symmetry). ∎

**Reading.** In the slice residue c_q all four notions are one-residue conditions:
| condition on c_q = −p⁻¹ mod q | object | barrier |
|---|---|---|
| c_q ∈ (ℤ/q)^{×2} | Astra source on slice q | B1 (local) |
| c_q ≡ (2k)² (mod q) for some k ∣ h | Claude ES shot (2k, 1) ∈ L_ρ(q) (d = 1 locus) | B2 |
| c_q ∣ h (as an integer) | Type A (b = 1) with López divisor q | B2 |
| c_q = m², m² ∣ h | Astra source integral on arrival | B2 ∩ square |
So Type A is Astra's source equation with the square condition on the twist dropped and an integrality condition
imposed. Astra needs the class of c_q to be a square; Type A needs its least representative to divide h. These are
different (one local, one archimedean/divisor) conditions on the same residue, and neither implies the other.
*Check* (`scripts/z34_dict.py 100000 100000`, 64 s, `logs/z34_dict_full_1e5.txt`): all 4 783 primes p ≡ 1 (4) ≤ 10⁵.
Type A by the pair form (B1_LINE Lemma 1.1): 75 658 solutions, each checked as an exact identity with c = c_q and c | h.
Independently, the slice scan of all q ≡ 3 (4), q ≤ 2p (≥ the bound 4cd − 1 ≤ p + 4d ≤ (3p + 3)/2) gives exactly the same
slice set for every p (Thm 1.2(d)). An independent scan of Astra sources (m ≤ √((p+7)/12), all q | pm² + 1,
q ≡ −1 (mod 4m²)) gives exactly the c-square subset (Thm 1.2(e)). Failures: 193, 2521, 66529 only. 53 716 Type A
solutions sit on split slices (inside some L_ρ(q)) and 21 942 (29 %) on non-split slices (no Astra source there).
22 627 are integral Astra sources (c square). **314 primes ≤ 10⁵ have Type A but no integral Astra source** (73, 313,
337, 409, 577, …, 3361, …): the one-way implication of Cor 1.3(i) is strict.
