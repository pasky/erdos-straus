# R242 — hostile review #1 of O237 (CAP_DOWN.md, branch side-agent/cap-down)

Reviewer: R242. Scope: CAP_DOWN.md §§1–7, memos BRAINSTORM/z13_*.md, report AGENT_REPORT_O237.md.
From-scratch scripts: scripts/review_r242_*.py. Labels as in DISCOVERIES.md. ES is not solved here.

## Summary verdicts (in progress)

| Claim | Verdict |
|---|---|
| Lemma 1.1 (general Type II window with cap) | SOUND |
| Thm 1.2 (even windows fire) | SOUND |
| Prop 1.3 (one-prime witness, cap ≤ (q−3)/4) | SOUND |

## Per-claim notes

### Lemma 1.1 — SOUND (re-derived)
* 4/n − 1/K = m/(nK) and 1/(nA) + d/(nKA) = (K+d)/(nKA) = m/(nK): identity holds; A ∈ ℤ_{>0} iff d ≡ −K (mod m).
* For s | K: s ∤ m, else s | 4K − m = n, contradicting (i). So v_s(A) = v_s(K+d), and z = nKA/d has
  v_s(z) = b_s + v_s(K+d) − c_s, which is b_s (c_s < b_s), ≥ b_s (c_s = b_s), or 2b_s − c_s (c_s > b_s). Primes outside S
  do not occur in d, so den z = ∏_{c_s > 2b_s} s^{c_s − 2b_s}. Rad condition: c_s > 2b_s ≥ 2 gives v_s(A) = b_s ≥ 1.
* **The 2-adic question raised by the brief.** EXPONENT_CAP Def 1.1 restricts only the primes ℓ with v_ℓ(z) < 0
  (ℓ ∤ 2n, ℓ | y, even, ≥ −2e). A power of 2 in the *shot* d is not restricted by Def 1.1; what matters is
  v₂(z) = b₂ + v₂(K+d) − c₂ ≥ 0, which (ii) c₂ ≤ 2b₂ guarantees. With c₂ = t = b₂ (Thm 1.2) one even has
  v₂(z) ≥ t ≥ 0. So the 2^t factor of d is compatible with Def 1.1: den z is odd. Confirmed numerically by
  scripts/review_r242_thm12.py (independent exact check of Def 1.1 on the produced (x, y, z)).
* The hypothesis gcd(m, n) = 1 is not used (it follows from (i) when s | gcd(m, n) ⇒ s | 4K, harmless).

### Thm 1.2 — SOUND (re-derived)
* gcd(K, qn) = 1: s | K, s | n ⇒ s | q ⇒ q | n; q | K ⇒ q | n. (K/q) = (4K/q) = (n/q) = (q/n) by Jacobi reciprocity
  (n ≡ 1 (4), n > 0). (K′/q) = (2/q)^t (K/q) = −1 under (E).
* F_q^* cyclic of order 2u, u odd: a subgroup containing a non-residue has even order, hence contains −1; −K′ is a
  residue, hence of odd order o, and h = (−K′)^{(o+1)/2} ∈ H with h² = −K′. d = 2^t∏s^{2a_s} ≡ −K (mod q). Lemma 1.1
  with c₂ = t ≤ 2t, odd exponents even. e = max(a_s − b_s)⁺ ≤ (ord_q s − 1) − 1 ≤ q − 3. ✓
* Mod-8 case split ✓ (v₂(n+q) = t + 2). Wording: "exactly … are excluded" is a statement about the *scope of the
  theorem*, not a claim that the excluded windows never fire (they sometimes do, via −2^j ∈ ⟨K′⟩, |j| ≤ t); see
  defect list for the slightly stronger wording in §7 item 1.

### Prop 1.3 — SOUND (re-derived)
* (K′/q) = −1 = ∏(s/q)^{b_s} ⇒ some odd s | K′ with b_s odd and (s/q) = −1. v₂(ord s) = v₂(q−1) = 1, so o/2 odd and
  s^{o/2} = −1. d = K s^{o/2}: c_s = b + o/2 even; overflow (o/2 − b)/2 ≤ ((q−1)/2 − 1)/2 = (q−3)/4. ✓
* "s ≡ −1 (mod q)" gives o = 2, cap 0 ✓. Sharpness: Prop 4.1(a) (below).
