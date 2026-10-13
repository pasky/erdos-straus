# Review R201 of GROWING_MUTE.md (O201, checkpoint 1) — hostile review

Reviewer: R201 (side agent). Document reviewed at merge of `side-agent/growing-mute`.
From-scratch scripts: `scripts/review_gm_*.py` (no reuse of `scripts/gm_*`).

(in progress)

## Claim-by-claim

### Def 1.0 + Prop 1.1 (cap hierarchy, (A, B) form, T1) — SOUND-AFTER-REPAIRS (M1, m1)

Re-derivation. Def 1.0 agrees with EXPONENT_CAP Def 1.1 at e = 1 (v_ℓ(q) ≤ 1 and rad q | y ⇔ q squarefree, q | y);
the hierarchy q = 1 ⇒ (q | y, q sqfree) ⇒ q | y ⇒ rad q | y is trivial and holds for all solutions.
(a) With c = v_ℓ(Q), s = v_ℓ(K): "c ≤ s + 1 and s ≥ 1 for all ℓ | Q" ⇔ Q | K·rad K — correct.
(b) v(Q₀) = min(c, s), v(Q₁) = max(0, c − s); Q₁ | Q₀ ⇔ c ≤ 2s ⇔ Q | K² — correct; gcd(Q₁, k) = 1 since ℓ | Q₁ ⇒ c > s
⇒ v_ℓ(Q₀) = s ⇒ ℓ ∤ k — correct. Moreover in the shot family ES^{(y,1)} ⇔ (Q₁ squarefree and Q₁ | Q₀) (c > s forces
c = s + 1 with s ≥ 1) — this is the "B squarefree" claim of (c); correct.
(c) Forward: A = 2k, B = Q₁, g·D = nA² + B² (EXPONENT_CAP Prop 1.3(b)), g + 1 = 2AQ₀ with B | Q₀ — correct.
Converse: D ≡ −B² (mod 2A) is forced (A even ⇒ 2A | A²), so Prop 1.3's converse applies; correct, but the
written proof is garbled ("with Q₁ ≡ …") — m1.
T1: (mA)² + B² with gcd(mA, B) = 1, odd ⇒ all divisors ≡ 1 (mod 4), while 4 | 2AB ⇒ g ≡ 3 (mod 4). Correct.

From-scratch check (`scripts/review_gm_dict.py 201 301 60`, exact rationals, solutions classified DIRECTLY from
(x, y, z) per Def 1.0, not via the paper's criteria):
* Part A: all 30 443 shot data (odd n ≤ 201, odd Q ≤ 301, gcd(Q, n) = 1, every g ≡ 3 (4) dividing n + 4Q²):
  den z = Q₁² always; ES ⇔ Q | K; ES^{(y,1)} ⇔ Q | K rad K; ES^{[2]} ⇔ Q | K² ⇔ Q₁ | Q₀; ES^{(y)} ⇔ rad Q | K — no
  exception. 497 have Q | K² (matches the author), all map to valid (A, B, g).
* Part B: all 816 triples (odd n ≤ 201, even A ≤ 60, odd B ≤ 60) (matches the author): every one yields a valid
  solution with den z = B², B | y; B squarefree (782) ⇒ ES^{(y,1)}. Odd squares n ≤ 201: zero triples (T1).
* **But 370 of the 816 triples have λ = (g+1)/(2AB) EVEN, and 35 have gcd(λ, n) > 1.** Since Q₀ = λB and
  Q = λB², these give Q even or gcd(Q, n) > 1 — NOT shot data in the paper's Notation (Q odd, gcd(Q, n) = 1).
  The solutions are nevertheless valid (den z = B², odd, prime to n). See M1.

