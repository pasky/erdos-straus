# PARITY_AUDIT — hatch H-B: parity-breaking literature audit and single-prime feasibility (task O255)

Status: in progress (O255). **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md
(PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Literature excerpts in
`sources/lit2026f/`. "Cited" = external theorem whose statement we read in the source (or an archived
abstract/excerpt); proof not re-checked.

Builds on: PARITY_FIXED_P ((J)6), SYNTHESIS_SPARKS5 ((J)58), CAP_POINTWISE ((J)64), POINTWISE_WINDOW (item 15),
POINTWISE_SIZE §8, LITERATURE_2026 (checked to 2026-09-28).

## 0. The two single-prime events (exact formulations used throughout)

Fix a prime p ≡ 1 (mod 4) (the hard case; in practice p ≡ 1 (mod 24)). ψ(r) := (r/p).

**Event (a) — side-number event ((J)58 = SYNTHESIS_SPARKS5 §1; (J)9).** Words are w = (t, u, v) ∈ ℕ³ with
tuv − u − v = p; A := tu − 1, B := tv − 1, so N_u := p + u = A·v, N_v := p + v = B·u, N_t := tp + 1 = A·B, and the
ES sign is χ(w) = (−A/p) = ψ(A). ES-five(p) ⟺ ∃ w with χ(w) = −1 ((J)9 Thm 4.5; (J)58). Read on the u-side:

  E_a(p; U) :  ∃ u ≤ U, ∃ A | p + u with A ≡ −1 (mod u) and ψ(A) = −1.

(Any such A gives the word t = (A + 1)/u, v = (p + u)/A.) Two layers: the **class/size layer** "A | p + u,
A ≡ −1 (mod u)" (B2: a divisor of a shifted prime in a class modulo a modulus tied to the shift) and the **sign
layer** ψ(A) = −1 ((J)6: needs only upper bounds; no parity barrier).

*Lemma 0.1 (range; PROVED, elementary).* Every word has min(u, v) ≤ √(p+1) + 1. Hence E_a(p; √p + 2) ⟺ ES-five(p);
for U = p^θ with θ < 1/2 (in particular U = (log p)^C) E_a is a genuine restriction.
*Proof.* (tu − 1)(tv − 1) = tp + 1, so t·min(u,v) − 1 ≤ √(tp + 1), i.e. min(u,v) ≤ (√(tp+1) + 1)/t ≤ √(p+1) + 1
for t ≥ 1. Since χ(w) = ψ(A) = ψ(B) (Lemma S of (J)58), u and v play symmetric roles. ∎

*Swap form.* A ≡ −1 (mod u), A | p + u ⟺ (t, u, v) with p = tuv − u − v ⟺ "tp + 1 has a divisor ≡ −1 (mod t)"
((J)6 (★): R(p) = #{(j,f) : f | p + j, f ≡ −1 (mod 4j)} is the same count in Type II normalisation). At fixed p
the expected number of words is ≍ (log p)² per slice family (Elsholtz–Tao), i.e. **polylog many events in a family
of ≍ p parameter values**.

**Event (b) — window event ((J)64 = CAP_POINTWISE §1; POINTWISE_SIZE §8, Thm 8.1).** For a prime q ≡ 3 (mod 4),
q ≡ 4 − p (mod 8), (q/p) = −1, put K_q := (p + q)/4 (odd, gcd(K_q, pq) = 1). ES holds at window q (cap 0) iff
Rat_q(K_q) ∩ {−1, −p} ≠ ∅, Rat_q(K) = {u/v mod q : uv | K, gcd(u,v) = 1}. Its simplest (v = 1, target −1)
sub-event, the "B2 class" of the brief:

  E_b(p; Q) :  ∃ prime q ≤ Q as above, ∃ d | K_q with d ≡ −1 (mod q).

At such windows the *group* condition −1 ∈ ⟨primes of K_q⟩ mod q is **forced** by reciprocity ((J)64 Thm 1.1):
the sign layer is free; only the exponent budget (= class/size layer) is missing, and relaxing it gives the
PROVED cap e*(n) < q.

**What "known theorem reaches it" would mean.** A statement, for every large p (or a thin infinite set of p, or
under GRH), giving E_a(p; p^θ) with θ < 1/2, or E_b(p; p^θ) with θ < 1, or any positive lower bound for the
counts behind them. Note E_b with Q ≈ 3p is ES itself restricted to windows (POINTWISE_SIZE Thm 8.1).
