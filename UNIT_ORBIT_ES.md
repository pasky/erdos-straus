# UNIT_ORBIT_ES — infinite unit orbits as "infinitely many shots" (task O186, spark relay L)

Status: in progress (O186). **ES is not solved here, nor any infinite case of ES itself.** Labels as in DISCOVERIES.md.
Builds on T1_TEMPLATE.md (O183, CLAIMED, under review R183): its Thm 2.1 (local invariants on integral points) and
Cor 2.2 (T1 for sign-pattern ES) are used below and re-derived where the setting changes. Scripts `scripts/uo_*`,
memos `BRAINSTORM/bsL_*.md`, literature `sources/uo/LITERATURE.md` (research subagent; statements marked
READ/SEC/RECALL there).

## 0. Plan and iteration log

(L1) **Reduction.** In every unit-Type-II mechanism (T1_TEMPLATE Prop 1.2) the case p ≡ 3 (mod 4) is trivial
(g = a_k itself, §3). For p ≡ 1 (mod 8) no Jacobi-symbol/reciprocity argument can produce the required prime,
because the product formula sees p exactly as it sees m² (§3, Prop 3.2). So an analytic input (Chebotarev + an
Artin-type sieve) is unavoidable; the target is an *unconditional* sieve.

(L2) **First screen: number fields (V_φ, ES over r₁ = 1 fields).** The unconditional Artin-type sieves
(Gupta–Murty, Heath-Brown, Harper–Murty) need (a) unit rank ≥ 4 (≥ 3 with level > ½) and (b) a level-½
Bombieri–Vinogradov theorem for *every* Frobenius condition imposed. I show (§4) that every number-field
unit-orbit variant forces a quadratic Kummer condition `(u/𝔮) = prescribed` for a unit u, which is not a
condition on N𝔮; the best known level for such conditions (Murty–Petersen) is 1/([K:ℚ] − 2), and the
arithmetic of the threshold then never closes. Hypothesis of the barrier that the variant satisfied: *the orbit
is a coset ηU² with η not a square* (forced by a mute REAL place, which needs η < 0 there).

(L3) **Modification: make the mute place FINITE.** A finite prime q can be muted by a parity normalisation
(only one denominator may contain q, and only to an even power). Then the orbit is Q², Q ∈ ⟨S⟩ — inside the
squares — and everything happens over ℚ, where all Frobenius conditions are congruences. Result (§1–§2): a
T1-bearing ℤ-equation ES^{(S)} containing ES, solvable at every prime **unconditionally** for |S| ≥ 4.

(L4) Unconditional statements for V_φ itself: almost-all with power saving and an exact-T1 failure set under
GRH (§5).

## 1. The q-mute variant ES^{(S)} over ℤ

Let S be a finite set of odd primes and ⟨S⟩ the multiplicative monoid it generates.

**Definition.** For n ∈ ℤ_{>0} with gcd(n, 2S) = 1:
`ES^{(S)}(n):  4/n = 1/x + 1/y + 1/z,  x, y ∈ ℤ_{>0},  z ∈ ℤ[1/S]_{>0},  v_q(z) ∈ 2ℤ for every q ∈ S with v_q(z) < 0.`
Equivalently `4/n = 1/x + 1/y + Q²/Z` with x, y, Z ∈ ℤ_{>0}, Q ∈ ⟨S⟩, gcd(Z, Q) = 1. For S = ∅ (or Q = 1) this
is ES; every ES solution is an ES^{(S)} solution.

**Lemma 1.1 (q-adic invariant on normalised points; PROVED).** Let q ∈ S, q ∤ n, and u = (x, y, z) a solution as
above, α(u) = (−u₁/u₃, −u₂/u₃) ∈ Br ℚ[2] (T1_TEMPLATE §2; permutation invariant). Then inv_q α(u) = 0.
*Proof.* If v_q(z) ≥ 0 all three are q-integral and T1_TEMPLATE Thm 2.1(b) applies. Let v_q(z) = −w, w > 0 even;
x, y are q-integral and 1/z ≡ 0 (mod q^w). Use x as denominator: α = (a, b), a = −y/x, b = −z/x.
(i) v(x) = v(y) = 0: v(a) = 0, v(b) = −w, tame symbol a^{v(b)}·b^{−v(a)}·(−1)^{v(a)v(b)} = a^{−w}, a square
(w even): inv_q = 0.
(ii) v(x) = V > 0: 1/x has valuation −V while 1/z ≡ 0 and 4/n is a unit, so v(y) = V and v(x + y) ≥ 2V > V,
i.e. a = −y/x ≡ 1 (mod q): the tame symbol a^{−w−V} is trivial.
(iii) v(x) = 0 < v(y): then 1/y is the only term of negative valuation — impossible. ∎
(For w odd case (i) gives inv_q = ((−y/x)/q), which is unconstrained: the parity normalisation is exactly what
mutes q. Without it — plain ES over ℤ[1/q] — the T1 dies; explicit example in §2.)

**Corollary 1.2 (T1 for ES^{(S)}; PROVED).** For every solution of ES^{(S)}(n), Σ_{ℓ | n} inv_ℓ α = ½. Hence for
n = m² (gcd(m, 2S) = 1) no solution has Type I/II shape at every prime of m.
*Proof.* inv_∞ = ½ (x, y, z > 0; Thm 2.1(a)); inv_2 = 0 (z ∈ ℤ_{(2)} as S is odd; Thm 2.1(c)); inv_q = 0 for
q ∈ S (Lemma 1.1); inv_ℓ = 0 for odd ℓ ∉ S, ℓ ∤ n (Thm 2.1(b)). Hilbert reciprocity gives the sum; Thm 2.1(d)
(ℓ ∉ S, so the variables are ℓ-integral) gives 0 at every ℓ | m for Type I/II shapes, contradicting ½. ∎
Anchor = ∞ (positivity), partner = 2 (numerator 4), mute places = S (parity normalisation).
