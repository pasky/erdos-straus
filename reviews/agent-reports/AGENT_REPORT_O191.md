# AGENT_REPORT_O191 — infinitely many fixed-modulus shots for ES itself (spark relay N)

Main file: FIXED_MODULUS_SHOTS.md. Scripts: scripts/fms_{cube,affine,three,typeI,box}.py. Memo: BRAINSTORM/bsN_divisor_box.md.
Branch side-agent/fixed-modulus-shots (main merged in, incl. O186).

**Verdict: NO-GO (PROVED, exact scope), plus two clean dictionaries.** ES has no infinite family of fixed-modulus
shots in any single-divisor encoding; the obstruction is exact at the level of one modulus (box vs. group) and one p
(finiteness).

SHARP:
1. **Certificate cube (Lemma 1.1, §4).** Type II solutions of ES(p) ⟷ (c, d, j) with h = 4cdj − 1 dividing
   pj + c ⟺ p + 4c²d ⟺ 4dj²p + 1; explicit x = (p+e)/4, y = pcdj, z = pxj/c. Type I: same with g = 4vwf − p | pv + f.
   Its three coordinate lines are the shot families, modulus = 4 × (product of fixed pair). Verified = brute force
   for all p ≤ 10⁴ (Type II) and ≤ 4000 (Type I).
2. **Unified box criterion (Thms 3.1, 4.2) and "ES = ES^{(S)} with bounded discrete logs" (Cor 3.2).**
   ES(p) ⟺ ∃h: −p ∈ Box((h+1)/4) (Type II) or −p ∈ Box((h+p)/4) (Type I) mod h, Box(k) = {c/j : cj | k}. For S-smooth
   (r+1)/4 the ES box is exactly O186's coset ∏q^{κ_q}⟨S⟩² with each exponent bounded by κ_q = v_q((r+1)/4).
3. **Exactly three modulus-4 shots (Cor 2.3): p + 1, p + 4, 4p + 1** — refutes "Mordell's p + 4 is the unique
   bounded-modulus shot" (O188). E.g. p = 13 is fired by p + 1 = 14 only. They fail jointly at 942 primes < 10⁶.

Main results (all PROVED, elementary):
* Thm 2.1: for an affine shot αp + β, a divisor h (coprime to 2αβ) certifies iff h ≡ −1 (mod 4M), M ∈ 𝓜(α,β), apart
  from sporadic h < 4μ⁵; every M ≥ √height/2 (Cor 2.2; O186 Prop 6.1 recovered and completed). Cor 2.4: for any fixed
  Chebotarev firing set only finitely many shots. Checked on 979 pairs × h ≤ 6·10⁴.
* Remark 2.5: (p/h) = −1 for every certificate divisor (cube form of T1).
* Prop 6.1: certifying moduli are ≤ O(p²) (ES(p) finite) — vs ES^{(S)}, where the sieve pushes r → ∞.
* Thm 6.2 summarises with exact scope; NOT covered: joint multi-prime certificates (B4), non-uniform polynomial shots.
* §5 logs 7 construction attempts (cyclotomic/Lucas forcing, p-dependent D, S-smooth boxes, S-unit cofactors,
  Type I, polynomial shots, orchestrator's discrete-log sharpening) and why each fails.

Caveats for the reviewer: Lemma 1.1/4.1 are reparametrisations of known ET forms (novelty is the symmetric packaging,
not the content); Thm 2.1's exceptional bound 4μ⁵ is crude (observed ≤ 8.5μ²); C6 (non-affine shots) is Assessment only.

Sparks: see BRAINSTORM/bsN_divisor_box.md (covering by boxes vs the (A)19 large-sieve cap; Type I self-referential box;
joint-failure density of the three modulus-4 shots).
