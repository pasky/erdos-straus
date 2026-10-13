# GROWING_IDENTITIES — exact identities with growing level (task O170, SPARK, hatch H-E)

Status: internal research note. **ES is not solved here, nor any infinite case of it.** Labels as in
DISCOVERIES.md. Scripts `scripts/gi_*`. Inputs read: STRONG_APPROX_ES.md (O167, branch side-agent/strong-approx;
§7, Thm 9.1, Cor 9.3), EXACT_FORMULA.md (O131; Prop 4.1 = signed decomposition with KH-type boundary),
CONDITIONAL_ES.md Lemma 1.1, PARITY_FIXED_P.md (O165, branch side-agent/parity-fixed-p; Lemmas 1.1–1.3).

Goal (brief): an exact identity (weighted ES count at n) = Σ_{g ≤ G(n)} (explicit expression in n, g) whose right
side has a provable sign at primes n ≡ 1 (24) and vanishes at odd squares. Thm 9.1 (finite Eisenstein
combinations are T1-dead) does not apply when the level grows with n.

## 0. Notation

For integers g ≥ 1, r and N ≥ 1 put `τ_{r,g}(N) := #{m ≥ 1 : m | N, m ≡ r (mod g)}`.
* `R(n) := #{(c,f,g) ∈ ℕ³ : cfg − c − f = n}` — all points of the Type I a = 1 cubic (no mod-4 condition).
* `W(n) := #{(c,f,g) ∈ ℕ³ : cfg − c − f = n, fg ≡ 1 (mod 4)}` — Type I, slice a = 1 (CONDITIONAL_ES Lemma 1.1:
  W(n) > 0 ⇒ ES(n)). By Lemma 1.1 (1⇔2), `W(n) = Σ_{t ≥ 1} #{m | tn+1 : m ≡ −1 (t), 4 | m}`.
* `T2(n) := #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = a + b + nc}` (Type II, ordered; O131 uses a ≤ b).

Computation: `scripts/gi_counts.py N` (exact enumeration of the cubics; n ≤ 2000 in a few seconds).
Control: W(m²) = T2(m²) = 0 for all odd m ≤ 44 (T1), W(n) = 0 for even n (fg odd ⇒ n odd).

## 1. Exact rearrangements with growing level (PROVED, elementary)

**Lemma 1.1 (continuant form).** Put `S_x := [[x, −1],[1, 0]] ∈ SL₂(ℤ)` and let `K⁻(x₁,…,x_r)` be the (1,1)
entry of `S_{x₁}⋯S_{x_r}` (negative continuant; `K⁻(x) = x`, `K⁻(x,y) = xy − 1`, `K⁻(x,y,z) = xyz − x − z`).
Then
* `R(n) = #{(c,g,f) ∈ ℕ³ : K⁻(c,g,f) = n}`, `W(n)` = same with `gf ≡ 1 (4)`;
* `T2(n) = #{(a,b,c,d) : K⁻(a, 4cd, b) = cn}` (since `K⁻(a,4cd,b) = 4abcd − a − b`);
* `S_c S_g S_f = [[n, −(cg−1)],[gf−1, −g]]`, so a Type I (a = 1) certificate is an SL₂(ℤ) word of length 3 with
  (1,1) entry n; for c,g,f ≥ 2 the word is the Hirzebruch–Jung expansion `n/m = [[c,g,f]] = c − 1/(g − 1/f)`
  with `m = gf − 1`. Hence (entries ≥ 2): **W-certificates ↔ residues m ∈ [1,n), 4 | m, (m,n) = 1, such that
  n/m has Hirzebruch–Jung length exactly 3.** Words containing a 1 reduce by `S_a S_1 S_b = S_{a−1}S_{b−1}`.
*Proof.* Direct multiplication; uniqueness of HJ expansions with entries ≥ 2. ∎

**Lemma 1.2 (fibration swap).** Fibring the cubic `cfg − c − f = n` by g, resp. by c, gives
`R(n) = Σ_{g ≥ 1} τ_{−1,g}(gn + 1) = Σ_{c ≥ 1} τ_{−1,c}(n + c)`,
and with the mod-4 condition `W(n) = Σ_{t} #{m | tn+1 : m ≡ −1 (t), 4 | m} = Σ_{c} #{e | n+c : e ≡ −1 (c),
(n+c)/e · (e+1)/c ≡ 1 (4)}`. The two growing-level sums are **not** termwise equal (g = 2: τ(2n+1) vs
τ_odd(n+2)). *Proof.* For fixed c: `f(cg−1) = n + c`, e := cg − 1. For fixed g: Lemma 1.1 of CONDITIONAL_ES. ∎
This is the exact form of the brief's "swap the order of summation": summing over m first (the divisor) gives
`#{t : t | m+1, tn ≡ −1 (m)} ∈ {0,1,2}`, i.e. `W(n) = #{m ≡ 0 (4) : (−n⁻¹ mod m) | m + 1} (+ boundary)`; the
modulus of the inner congruence is the summation variable, so nothing telescopes — every exact re-summation of
the cubic is again a divisor-in-class count (B2), now with the level as the summation variable.

**Lemma 1.3 (the T1-respecting rewrite: a character at the place n).** Let n ≡ 1 (mod 4). For every
Type I (a = 1) certificate, `tn + 1 = m·m''` with `4 | m`, `m'' ≡ −1 (t)`, one has t ≡ 3 (4) and the Jacobi
symbol `(m''/n) = −1`. Consequently
`W(n) = Σ_t Σ_{m'' | tn+1, m'' ≡ −1 (t), 4 | (tn+1)/m''} (1 − (m''/n))/2`,
and at n = k² every summand vanishes, `(m''/k²) = 1`.
*Proof.* tn ≡ −1 (4) forces t ≡ 3 (4). Write m'' = 2^j u, u odd, ε(x) := (x−1)/2. For a prime ℓ | u,
−t ≡ n⁻¹ (mod ℓ), so (−t/ℓ) = (n/ℓ); hence (n/u) = (−t/u), and (u/n) = (n/u) (reciprocity, n ≡ 1 (4)).
From m'' ≡ −1 (t): u ≡ −2^{−j} (t), so (u/t) = (−1/t)(2/t)^j = −(2/t)^j, and
(−t/u) = (−1)^{ε(u)}(u/t)(−1)^{ε(t)ε(u)} = −(2/t)^j. So (m''/n) = (2/n)^j (u/n) = −(2/(tn))^j. If j ≥ 1 then
2^{j+2} | tn + 1, so tn ≡ 7 (8) and (2/(tn)) = 1. Hence (m''/n) = −1. ∎ (Checked: all 4901 certificates of
n ≡ 1 (4), n ≤ 3000, `scripts/gi_spin_check.py`, 0 violations.)
*Reading.* This is PARITY_FIXED_P Lemma 1.3 in slice a = 1. The only T1-respecting factor available is a
genus character **at the place n** (the "main term with genus data at the place p" asked for in O167 §11);
but here it is identically −1 on certificates, i.e. it carries no information beyond the class condition.
