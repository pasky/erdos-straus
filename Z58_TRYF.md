# Z58 TRYF — tryhard lane: prove (★) for large Mordell-class primes

Lane TRYF, wave z58. Fresh, unprimed attack (no FRONTIER/Z5* memos read; only `data/z58/screens/`).
Scripts `scripts/z58_tryf_*`, data `data/z58/tryf/`.

**Problem (★).** For every sufficiently large prime p ≡ 1 (mod 24) [ideally every prime p > 10¹⁰ with
p mod 840 ∈ 𝔐 = {1,121,169,289,361,529}] there is d ≡ 3 (mod 4), 3 ≤ d ≤ (4p+1)/3, such that
r := (−p mod d) ∈ [1, d−1] divides (d+1)/4.

**Status line (updated at every commit): NO PROOF. Main idea = character-layer reduction (§3): PROVED
reduction of (★) to a "higher-character equidistribution" hypothesis HCE; HCE is unproved and of the same
depth as (★). NOT a hot lead. Partial theorems: §1 (exact reformulations), §2 (quadratic layer is harmless,
PROVED via Burgess).**

## §0 Mandatory falsifiers — behaviour of the main idea (stated at first commit; re-stated in §7)

Main idea (§3): write R(p) = #{d : hit} and expand, for each prime d ≡ 3 (4), the hit indicator
[p mod d ∈ H_d], H_d := {−k mod d : k | (d+1)/4}, in Dirichlet characters mod d:
  [p mod d ∈ H_d] = (1/(d−1)) Σ_{χ mod d} χ(−p) · Ĥ_d(χ̄),   Ĥ_d(χ) := Σ_{k | (d+1)/4} χ(k).
Layer 0 (χ principal) = τ((d+1)/4)/(d−1): summed over d gives the main term ≍ log²p.
Layer 2 (χ quadratic): Ĥ_d(χ₂) = τ((d+1)/4) exactly (every k | (d+1)/4 is a QR mod d, Lemma 2.1), so the
layer equals −τ((d+1)/4)(p/d)/(d−1) = −τ((d+1)/4)·(d/p)/(d−1) by reciprocity; summed over d it is a
character sum modulo p, bounded by Burgess (§2). Layers of order > 2: cannot be flipped to modulus p; this is
where the attack stops (hypothesis HCE, §3).

* (F1) odd squares n = m²: Layer 2 is where non-squareness is used. For n = m², (n/d) = +1 for all d coprime
  to m, so Layer 2 equals −(Layer 0) term by term and the two cancel exactly (this is precisely the statement
  "H_d consists of non-residues"). For prime p the Burgess step needs χ_p = (·/p) to be a non-principal
  character — the identifiable step. Verdict: the idea FAILS at squares at Layer 2, as it must.
* (F2) C even only: Lemma 2.1 and the Burgess step hold verbatim with k restricted to those with (d+1)/(4k)
  even; the main term halves. So Layers 0+2 alone would "prove" R₈(p) ≥ 1 for large p, which is false at
  12 primes in [10¹⁰, 1.1·10¹⁰]. Hence the higher layers are NOT negligible at p ≈ 10¹⁰ for the half
  family; any proof must control them with an error term ≥ half the main term at that height. The idea
  survives F2 only in the weak sense that it proves nothing without HCE; it does not pass F2 as a proof.
* (F3) 285 non-square composites n ≡ 1 (4) ≤ 8·10⁶: Layer 2 for composite non-square n uses the Jacobi
  character (·/n) (non-principal, conductor = squarefree kernel of n), Burgess still applies; so Layers 0+2
  do not distinguish primes from non-square composites. The asymptotic reduction says nothing at n ≤ 8·10⁶.
  The hypothetical HCE would have to be false for these n (and is, since R(n) = 0 there); consistent, no
  information.
* (F4) 14 primes 409 … 8 813 281 with R(p) = 0: same as F3 — the reduction is asymptotic with an ineffective
  threshold; nothing is claimed below the threshold.

Conclusion of §0: the idea is NOT a hot lead. It isolates exactly which part of the problem is "reciprocity-
flippable" (Layer 2 and, for p ≡ 1 (24), the layers of order dividing 24 via cubic/higher reciprocity in
ℤ[ζ_m]) and which is not (all other characters mod d, i.e. (d−1)−O(1) of them).

## §1 Exact reformulations (PROVED, elementary)

Throughout p is an odd prime, d ≡ 3 (mod 4), r_d := (−p mod d) ∈ [1, d−1] (d ∤ p since d ≠ p), and
H_d := {−k mod d : k | (d+1)/4}. A **hit** at d means p mod d ∈ H_d, i.e. r_d | (d+1)/4. R(p) := #{d ≡ 3 (4), 3 ≤ d ≤ (4p+1)/3 : hit}.

**Lemma 1.1.** The following are equivalent for an odd prime p:
(a) R(p) ≥ 1;  (b) ∃ u, B, C ≥ 1 with p = 4uBC − u − B;  (c) ∃ u ≥ 1 such that p + u has a divisor ≡ −1 (mod 4u);
(d) ∃ C ≥ 1 such that 4Cp + 1 has a divisor ≡ −1 (mod 4C).
Moreover the bound d ≤ (4p+1)/3 in (★) is automatic: every d ≡ 3 (4) with r_d | (d+1)/4 satisfies d ≤ (4p+1)/3.

*Proof.* (a)⇒(b): put u = r_d, C = (d+1)/(4u), B = (p+u)/d (integers by hypothesis); then 4uC = d+1 and Bd = p+u give
p = B(4uC−1) − u. (b)⇒(a): d := 4uC − 1 ≡ 3 (4) divides p + u, and 1 ≤ u ≤ (d+1)/4 < d, so r_d = u | (d+1)/4 = uC.
Automatic bound: with these u, B, C: if B ≥ 2 then d ≤ (p+u)/2 ≤ (p + (d+1)/4)/2, so d ≤ (4p+1)/7 < (4p+1)/3; if B = 1 then
d = p + u with u = (d+1)/(4C) ≤ (d+1)/4, so 3d ≤ 4p + 1. (b)⇔(c): d = 4uC−1 | p+u. (b)⇔(d): multiply p = 4uBC − u − B
by 4C: (4uC − 1)(4BC − 1) = 4Cp + 1; conversely a divisor x ≡ −1 (4C) of 4Cp+1 has cofactor y with xy ≡ 1 (4C), hence
y ≡ −1 (4C), and x = 4uC − 1, y = 4BC − 1 gives (b). ∎

(The "C even" half of F2 is (d) with 8 | 4C, i.e. in (c): 8u | d + 1.) Numerical facts recorded in §4 confirm that
neither (c) with u bounded nor (d) with C bounded suffices.

**Lemma 1.2 (quadratic constraint).** For d ≡ 3 (4) and every k | (d+1)/4: gcd(k, d) = 1 and the Jacobi symbol (k/d) = 1.
Consequently (−k/d) = −1 for all k | (d+1)/4, so a hit at d forces (p/d) = −1, i.e. (by Jacobi reciprocity, p ≡ 1 (4))
χ_p(d) := (d/p) = −1. In particular R(n) = 0 for every odd square n = m² (F1).

*Proof.* d ≡ −1 (mod 4k) gives gcd(k,d) = 1. Write k = 2^a k' with k' odd. If a ≥ 1 then d ≡ −1 (mod 8), so (2/d) = 1.
For k' > 1: d ≡ −1 (mod k') gives (d/k') = (−1/k') = (−1)^{(k'−1)/2}; Jacobi reciprocity (d, k' odd, coprime) gives
(k'/d) = (d/k')·(−1)^{((k'−1)/2)((d−1)/2)} = (−1)^{(k'−1)/2}·(−1)^{(k'−1)/2} = 1, using (d−1)/2 odd. Hence (k/d) = 1 and
(−k/d) = (−1/d) = −1. For n = m² coprime to d, (n/d) = (m/d)² = 1 ≠ −1; if gcd(m, d) > 1 then −n mod d is not coprime
to d while every element of H_d is. ∎

## §2 Layer 2: the quadratic obstruction is harmless for primes (PROVED)

Let X_p := (4p+1)/3 and, for X ≥ 3,
  M(X) := Σ_{d ≡ 3 (4), 3 ≤ d ≤ X} τ((d+1)/4)/d = Σ_{k,C ≥ 1, 4kC ≤ X+1} 1/(4kC − 1),
  S_p(X) := Σ_{d ≡ 3 (4), 3 ≤ d ≤ X} τ((d+1)/4) χ_p(d)/d = Σ_{4kC ≤ X+1} χ_p(4kC − 1)/(4kC − 1),
  Q_p(X) := Σ_{d ≡ 3 (4), 3 ≤ d ≤ X, χ_p(d) = −1} τ((d+1)/4)/d = (M(X) − S_p(X))/2.
Interpretation: |H_d|/d = τ((d+1)/4)/d is the proportion of residues mod d that are hits; M is the "expected number of
hits" for a random residue, and Q_p is the same after discarding the d excluded by Lemma 1.2. For n = m² one has
S_n(X) = M(X) − O(Σ_{d: gcd(d,m)>1} τ/d) and Q_n is the tiny remainder (consistent with R(n) = 0).

**Theorem 2.1.** For every ε ∈ (0, 1/8) there is δ = δ(ε) > 0 and p₀(ε) such that for all primes p ≥ p₀ and all X ≥ 3:
  |S_p(X)| ≤ (1+4ε)²·(log p)²/64 + O_ε(log p).
Consequently Q_p(X_p) ≥ (7/128 − ε)(log p)² for p ≥ p₁(ε); in particular the quadratic constraint of Lemma 1.2 removes
at most a fraction 1/8 + o(1) of the "expected hits".

*Proof.* χ_p is a non-principal character modulo the prime p (p is not a square — this is the step that fails for F1).
Burgess' bound: for every r ≥ 1, η > 0, uniformly in the integer N₀ and L ≥ 1,
  |Σ_{N₀ < n ≤ N₀ + L} χ_p(n)| ≤ C(r, η) L^{1−1/r} p^{(r+1)/(4r²) + η}.                      (B)
Put K₀ := ⌈p^{1/4+ε}⌉ and split the pairs (k, C) with 4kC ≤ X+1 into four regions.
(I) k ≤ K₀, C ≤ K₀: since 1/(4kC−1) = 1/(4kC) + 1/(4kC(4kC−1)),
  Σ_(I) 1/(4kC − 1) ≤ (1/4)(Σ_{k ≤ K₀} 1/k)² + Σ_{m ≥ 1} τ(m)/(4m(4m−1)) ≤ (1/4)(log K₀ + 1)² + O(1)
  = (1+4ε)²(log p)²/64 + O_ε(log p).
(II) k ≤ K₀ < C: fix k. For a dyadic block C ∈ (T, 2T] ∩ (K₀, (X+1)/(4k)], T ≥ K₀, Abel summation with the monotone
weight 1/(4kC−1) ≤ 1/(4kT) gives |Σ_{block} χ_p(4kC−1)/(4kC−1)| ≤ (2/(4kT))·sup_{T<t≤2T} |Σ_{T<C≤t} χ_p(4kC−1)|.
As 4k < p, χ_p(4kC − 1) = χ_p(4k)·χ_p(C − a_k) with a_k ≡ (4k)^{-1} (mod p), so the inner sum is a character sum over
an interval of length ≤ T and (B) gives ≤ C(r,η) T^{1−1/r} p^{(r+1)/(4r²)+η}. Summing over the dyadic T = 2^j K₀:
  |Σ_(II), fixed k| ≤ (C/k)·Σ_j (2^j K₀)^{−1/r} p^{(r+1)/(4r²)+η} ≪ (1/k)·p^{−(1/4+ε)/r + (r+1)/(4r²) + η} = (1/k)·p^{1/(4r²) − ε/r + η}.
  Choose r := ⌈1/ε⌉ + 1 (so 1/(4r²) < ε/(2r)) and η := ε/(4r); the exponent is ≤ −ε/(4r) =: −δ. Summing over k ≤ K₀:
  Σ_(II) ≪ p^{−δ} log p.
(III) C ≤ K₀ < k: identical with the roles of k and C exchanged (χ_p(4kC−1) = χ_p(4C)χ_p(k − a_C)).
(IV) k > K₀ and C > K₀: fix k and sum over C ∈ (K₀, (X+1)/(4k)] in dyadic blocks exactly as in (II) (Burgess' bound
(B) is monotone in L, so a block truncated by the upper limit is bounded by the full dyadic block); the bound
(1/k)p^{−δ} holds for each k, and summing over k ≤ X+1 gives ≪ p^{−δ} log X. If X > p² this is still ≪ p^{−δ/2}
after using the trivial bound for d > p^{2}... (we only need X ≤ X_p < 2p, so Σ_(IV) ≪ p^{−δ} log p.)
Adding (I)–(IV) proves the bound on S_p(X) for X ≤ 2p (the only range used below).
For the consequence: M(X_p) ≥ (1/4) Σ_{m ≤ (p+1)/3 − 1} τ(m)/m = (1/8)(log p)² − O(log p) (Σ_{m ≤ Y} τ(m)/m =
(1/2)log²Y + 2γ log Y + O(1)), hence Q_p(X_p) = (M − S_p)/2 ≥ ((1/8 − (1+4ε)²/64)/2)(log p)² − O_ε(log p)
= ((7 − 8ε − 16ε²)/128)(log p)² − O_ε(log p). ∎

*Remarks.* (i) The constant 1/64 is the untouched region k, C ≤ p^{1/4+ε}; with Burgess' range replaced by the
GRH range (character sums over intervals of length (log p)^{2+ε}) it would become o(1). (ii) F2 check: restricted to
C even, M halves and the region-(I) bound halves; Q₈ ≥ (7/256−ε)log²p > 0 — no contradiction, because Q > 0 does not
imply R ≥ 1 (§3). (iii) F3/F4: the statement is asymptotic (ineffective p₀ from Burgess' constants are effective, but
the threshold is astronomically beyond 10¹⁰ for ε small); nothing is claimed about the 14 primes or the composites.

## §3 Character-layer decomposition; what is flippable and what is not

**Lemma 3.1 (exact layer identity).** For d ≡ 3 (4) coprime to p,
  (φ(d)/d)·[p mod d ∈ H_d] = (1/d) Σ_{χ mod d} χ(−p) Ĥ_d(χ̄),   Ĥ_d(χ) := Σ_{k | (d+1)/4} χ(k).
*Proof.* Each k | (d+1)/4 is coprime to d (Lemma 1.2) and the classes −k mod d are distinct for distinct k (k < d).
By orthogonality, [p ≡ −k (d)] = (1/φ(d)) Σ_χ χ(p)χ̄(−k) = (1/φ(d)) Σ_χ χ(−p)χ̄(k) (χ̄(−1) = χ(−1)); sum over k. ∎

Define R̃(p) := Σ_{d ≡ 3 (4), 3 ≤ d ≤ X_p} (φ(d)/d)[p mod d ∈ H_d]. Then 0 ≤ R̃(p) ≤ R(p) and R(p) ≥ 1 ⇔ R̃(p) > 0.
Summing Lemma 3.1, R̃(p) = L₀ + L₂ + L_r + L_n, where (all sums over d ≡ 3 (4), 3 ≤ d ≤ X_p):
* L₀ := Σ_d τ((d+1)/4)/d = M(X_p)   (principal character);
* L₂ := Σ_d (−p/d) Ĥ_d((·/d))/d = −S_p(X_p)   (the Jacobi symbol (·/d); by Lemma 1.2 Ĥ_d((·/d)) = τ((d+1)/4), and
  (−p/d) = −(p/d) = −χ_p(d); d ≡ 3 (4) is not a square, so (·/d) is non-principal and ≠ χ₀);
* L_r := Σ_d (1/d) Σ_{χ real, χ ∉ {χ₀, (·/d)}} χ(−p)Ĥ_d(χ̄)   (other real characters; empty for d prime);
* L_n := Σ_d (1/d) Σ_{χ non-real} χ(−p)Ĥ_d(χ̄).
The real characters mod odd d are n ↦ (n/e) (restricted to gcd(n,d)=1) for squarefree e | d; (·/d) is e = core(d)
(product of primes with odd exponent in d). For a real character (·/e) with d = e·i squarefree, (k/e)(k/i) = (k/d) = 1
gives Ĥ_d((·/e)) = Σ_{k | (d+1)/4} (k/i) = τ_{(·/i)}((d+1)/4) ≥ 0, so
  L_r (squarefree d) = Σ_{ei = d, e,i > 1} (−1/e)·χ_p(e)·τ_{(·/i)}((d+1)/4)/d.
Thus **every real layer is flippable**: it is a sum of χ_p(e) = (e/p) over e with non-negative arithmetic weights.
Terms with small e are the classical local factors (e = 3, p ≡ 1 (3): (−p/3) = −1 and the e = 3 layer is
−Σ_{3|d} τ_{(·/3)}((d+1)/4)/d ≈ −(2L(1,χ₋₃)/12)·log p·(1+o(1)) < 0 — this is the "Mordell penalty": for p ≡ 1 (3) only
k ≡ 2 (3) can hit when 3 | d). Heuristically L_r ≈ Σ_e (−1/e)χ_p(e)·c·log(X_p/e)/e, i.e. of the order of
L(1, (−p/·))·log p = O(log p · log log p) under GRH, but only O(log² p) unconditionally (the e ≤ p^{1/4} range is
not reachable by Burgess). I did not complete a rigorous bound for L_r (EVIDENCE only: §4 table).

**The non-real layer L_n is where the attack stops.** For d prime the characters of order m | gcd(d−1, p−1) can be
flipped by m-th power reciprocity in ℤ[ζ_m] (p ≡ 1 (24) allows m | 24, i.e. at most 24 characters per d out of d−1);
all other characters have no reciprocity law and χ(−p) carries genuinely "mod d" information about p. The quantity
  Σ_{χ non-real mod d} χ(−p)Ĥ_d(χ̄) = φ(d)[hit at d] − Σ_{χ real} χ(−p)Ĥ_d(χ̄)
is the hit indicator minus its real-character approximation; bounding it for a single p is equivalent to the problem.

**Hypothesis HCE(δ).** For all sufficiently large primes p ≡ 1 (24): L_n(p) + L_r(p) ≥ −(1−δ)·(M(X_p) − S_p(X_p)).

**Theorem 3.2 (CONDITIONAL on HCE(δ) for some δ > 0).** (★) holds for all sufficiently large primes p ≡ 1 (24).
*Proof.* R̃(p) = (M − S_p) + L_r + L_n ≥ δ(M − S_p) = 2δ Q_p(X_p) ≥ 2δ(7/128 − ε)log²p > 0 by Theorem 2.1. ∎

Honest assessment: HCE is a restatement of the problem plus a quantitative margin; it is not a standard conjecture
and no known tool (Burgess, Kloosterman/Weil, spectral shifted-convolution bounds, Bombieri–Vinogradov) addresses it
for a single p, because every reformulation (Lemma 1.1(c),(d)) asks about divisors of *specific* integers p + u (or
4Cp+1) in residue classes whose modulus 4u is as large as the interval of u's considered. The one genuinely
individual-p tool, exponential sums Σ_d e(hp/d) (van der Corput/exponent pairs, giving equidistribution of p mod d at
resolution d/H for H ≤ p^{1/6} when d ≈ √p), resolves residues only up to scale p^{1/3}, far from the exact
divisibility r_d | (d+1)/4 required. F2 is the quantitative reminder: HCE(δ) restricted to C even is false at p ≈ 10¹⁰.
## §4 Numerical evidence (data/z58/tryf/)

(to be written)

## §7 Falsifiers re-stated; hostile review; verdict

(to be written)
