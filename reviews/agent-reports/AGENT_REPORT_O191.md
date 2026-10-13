# AGENT_REPORT_O191 — infinitely many fixed-modulus shots for ES itself (spark relay N)

Main file: FIXED_MODULUS_SHOTS.md. Scripts: scripts/fms_{cube,affine,three,typeI,box}.py. Memo: BRAINSTORM/bsN_divisor_box.md.
Branch side-agent/fixed-modulus-shots (main merged in, incl. O186).

**Verdict: a scoped NO-GO (PROVED for fixed-coefficient affine shots, Type II, one divisor) plus exact size
statements for every Type I/II certificate.** Within that scope ES has no infinite family of shots with a common
fixed-modulus (or Chebotarev) firing condition. Outside it (p-dependent coefficients, degree ≥ 2 shots, Type I affine
shots, multi-prime conditions) nothing is proved; the per-modulus box size h^{o(1)} and the finiteness h = O(p²) are
size facts, not impossibility theorems.
Self-review (deep reviewer, R-O191) found and I repaired: a false bound in Lemma 1.1 (cd ≤ p/4 + 1/2 → 3cd ≤ p + 1;
Prop 6.1 re-proved, h ≤ (p+1)(p+5)/4), an overstated "ES = ES^{(S)} with bounded discrete logs" (the box and the parity
coset are incomparable — itself false, see R191: as residue sets Box(k) ⊆ 4⟨S⟩²), "boxes are never groups" (false: Box(8) = ⟨2⟩ mod 31), a wrong density figure, and the
overbroad scope of Thm 6.2 (now narrowed).

SHARP:
1. **Certificate cube (Lemma 1.1, §4).** Type II solutions of ES(p) ⟷ (c, d, j) with h = 4cdj − 1 dividing
   pj + c ⟺ p + 4c²d ⟺ 4dj²p + 1; explicit x = (p+e)/4, y = pcdj, z = pxj/c. Type I: same with g = 4vwf − p | pv + f.
   Its three coordinate lines are the shot families, modulus = 4 × (product of fixed pair). Verified = brute force
   for all p ≤ 10⁴ (Type II) and ≤ 4000 (Type I).
2. **Unified box criterion (Thms 3.1, 4.2) and the exponent-coordinate comparison with ES^{(S)} (Cor 3.2).**
   ES(p) ⟺ ∃h: −p ∈ Box((h+1)/4) (Type II) or −p ∈ Box((h+p)/4) (Type I) mod h, Box(k) = {c/j : cj | k}. For S-smooth
   k = (r+1)/4 (p ∉ S) ES certifies via the bounded box |e_q| ≤ v_q(k) (all parities), ES^{(S)} via the unbounded parity
   coset e ≡ κ (mod 2); as residue sets Box(k) ⊆ 4⟨S⟩² (R191 repair of "incomparable"), and per certificate their overlap is O186 Prop 6.1.
3. **Exactly three modulus-4 shots (Cor 2.3): p + 1, p + 4, 4p + 1** — refutes "Mordell's p + 4 is the unique
   bounded-modulus shot" (O188). E.g. p = 13 is fired by p + 1 = 14 only. They fail jointly at 942 primes < 10⁶.

Main results (PROVED; elementary except the Dirichlet/Chebotarev density inputs of Cors 2.3–2.4):
* Thm 2.1: for an affine shot αp + β, a divisor h (coprime to 2αβ) certifies iff h ≡ −1 (mod 4M), M ∈ 𝓜(α,β), apart
  from sporadic h < 4μ⁵; every M ≥ √height/2 (Cor 2.2; O186 Prop 6.1 recovered and completed). Cor 2.4: for any fixed
  Chebotarev firing set only finitely many shots. Checked on 979 pairs × h ≤ 6·10⁴.
* Remark 2.5: (p/h) = −1 for every certificate divisor (cube form of T1).
* Prop 6.1: certifying moduli are O(p²) (Type II h ≤ (p+1)(p+5)/4, Type I g < 3p²) — vs ES^{(S)}, where the sieve pushes r → ∞.
* Thm 6.2 summarises with exact scope; NOT covered: p-dependent coefficients, degree ≥ 2 shots, Type I affine shots, multi-prime certificates (B4).
* §5 logs 7 construction attempts (cyclotomic/Lucas forcing, p-dependent D, S-smooth boxes, S-unit cofactors,
  Type I, polynomial shots, orchestrator's discrete-log sharpening) with Assessment-level outcomes; C2 and C6 remain open.

Caveats for the reviewer: Lemma 1.1/4.1 are reparametrisations of known ET forms (novelty is the symmetric packaging,
not the content); Thm 2.1's exceptional bound 4μ⁵ is crude (observed ≤ 8.5μ²).

Sparks: see BRAINSTORM/bsN_divisor_box.md (covering by boxes vs the (A)19 large-sieve cap; Type I self-referential box;
joint-failure density of the three modulus-4 shots).
