# Z58 TRYF — tryhard lane: prove (★) for large Mordell-class primes

Lane TRYF, wave z58. Fresh, unprimed attack (no FRONTIER/Z5* memos read; only `data/z58/screens/`).
Scripts `scripts/z58_tryf_*`, data `data/z58/tryf/`.

**Problem (★).** For every sufficiently large prime p ≡ 1 (mod 24) [ideally every prime p > 10¹⁰ with
p mod 840 ∈ 𝔐 = {1,121,169,289,361,529}] there is d ≡ 3 (mod 4), 3 ≤ d ≤ (4p+1)/3, such that
r := (−p mod d) ∈ [1, d−1] divides (d+1)/4.

**Status line (updated at every commit): NO PROOF. Main idea = character-layer decomposition (§3): an exact
identity splitting R̃(p) into reciprocity-flippable layers and an irreducible layer L_n; the hypothesis HCE under which
(★) follows is a trivial reformulation of (★) with a quantitative margin, not a reduction to anything simpler. NOT a hot lead. Partial theorems: §1 (exact reformulations), §2 (quadratic layer is harmless,
PROVED via Burgess).**

## §0 Mandatory falsifiers — behaviour of the main idea (stated at first commit; re-stated in §7)

Main idea (§3): for every d ≡ 3 (4), 3 ≤ d ≤ X_p := (4p+1)/3 (all such d are coprime to p), expand the weighted hit
indicator in Dirichlet characters mod d (Lemma 3.1):
  (φ(d)/d)·[p mod d ∈ H_d] = (1/d) Σ_{χ mod d} χ(−p) · Ĥ_d(χ̄),   H_d := {−k mod d : k | (d+1)/4},  Ĥ_d(χ) := Σ_{k | (d+1)/4} χ(k),
and sum over d: R̃(p) = L₀ + L₂ + L_r + L_n ≤ R(p), R̃ > 0 ⇔ R ≥ 1.
Layer L₀ (χ principal) = Σ_d τ((d+1)/4)/d = M(X_p) = (1/8)log²p + O(log p).
Layer L₂ (Jacobi symbol (·/d)): Ĥ_d((·/d)) = τ((d+1)/4) exactly (Lemma 1.2), so the layer equals
−Σ_d τ((d+1)/4)(p/d)/d = −Σ_d τ((d+1)/4)·(d/p)/d by reciprocity; this is a character sum modulo p and is bounded by
Burgess (Theorem 2.1): |L₂| ≤ (1/64 + o(1))log²p. This is the only layer with an analytic bound in this memo.
Layer L_r (other real characters mod composite d): flips algebraically to the character (χ₋₄χ_p)(e), e | d, with
non-negative weights (§3) — but no analytic bound is proved here. Layer L_n (non-real characters): no bound; this is
where the attack stops (hypothesis HCE, §3).

* (F1) odd squares n = m²: Layer 2 is where non-squareness is used. For n = m², (n/d) = +1 for all d coprime
  to m, so Layer 2 equals −(Layer 0) term by term and the two cancel exactly (this is precisely the statement
  "H_d consists of non-residues"). For prime p the Burgess step needs χ_p = (·/p) to be a non-principal
  character — the identifiable step. Verdict: the idea FAILS at squares at Layer 2, as it must.
* (F2) C even only: Lemma 1.2, Lemma 3.1 and the Burgess argument adapt verbatim with k restricted to those with
  (d+1)/(4k) even (C = 2j; the leading coefficients of the main term and of the region-(I) bound halve — not the values
  at finite X). So Layers 0+2 alone are positive for the half family too, for large p; they therefore cannot imply
  R ≥ 1 for any family, since R₈(p) = 0 at 12 primes in [10¹⁰, 1.1·10¹⁰] (screen data; 6 of them ≡ 1 mod 24) and at
  ≈ 10⁻³ of the Mordell primes in [10⁷, 10⁸] (§4.2). At each such zero the remainder L_r,8 + L_n,8 cancels the
  positive base exactly. Finitely many zeros do not refute an "all sufficiently large p" hypothesis such as a C-even
  analogue of HCE; they do show that any such hypothesis is a strong statement. The idea survives F2 only in the
  weak sense that it proves nothing without HCE; it does not pass F2 as a proof.
* (F3) 285 non-square composites n ≡ 1 (4) ≤ 8·10⁶: everything in this memo is stated for primes. For composite n
  the layer sums must be restricted to gcd(d, n) = 1 (e.g. n = 57, d = 3: all character values vanish, whereas the
  unrestricted M wrongly counts 1/3), the Jacobi character (·/n) is imprimitive when n has square factors (primitive
  part (·/core(n))), and the shifted-interval factorisation in Theorem 2.1 needs invertible slopes; the transfer of
  Theorem 2.1 to composite n is NOT claimed. HCE is stated only for primes, so these n do not falsify it.
* (F4) 14 primes 409 … 8 813 281 with R(p) = 0 (9 in 𝔐): Theorem 2.1 is asymptotic (effective constants in
  principle, not evaluated here) and HCE is unproved; nothing is claimed for any specific p. At these 14 primes the
  decomposition gives L_r + L_n = −(L₀ + L₂) (§4.3). The 38 𝔊*-zeros of `gstar_zeros.txt` concern a restricted
  subfamily not studied here; they are not all full-family zeros (e.g. 564 661 441 has R = 2, R_𝔊* = 0, per the
  cross-model review), and no restricted-family claim is made in this memo.

Conclusion of §0: the idea is NOT a hot lead. It separates the layers that flip algebraically to characters modulo
4p (principal, Jacobi, all other real characters mod d) from the non-real layer, and bounds analytically only the
Jacobi layer. (Non-real characters of order m | gcd(d−1, p−1) also have m-th power reciprocity laws in ℤ[ζ_m]; no
usable rational-conductor flip for them is established here, and no classification of "unflippable" characters is
claimed.)
Note also that the numerical §4.4 shows a non-zero mean of the "irreducible" layer L_n (≈ −3 at p ≈ 10⁶): the
small-conductor non-real characters (p mod 5, 7, 9, … beyond quadratic information) are local factors, trivially known
in a fixed residue class; the genuinely non-local remainder is what fluctuates.

## §1 Exact reformulations (PROVED, elementary)

Throughout p is a prime ≡ 1 (mod 4), d ≡ 3 (mod 4), r_d := (−p mod d) ∈ [1, d−1] (d ∤ p since d ≥ 3 and d ≠ p, as d ≡ 3, p ≡ 1 mod 4), and
H_d := {−k mod d : k | (d+1)/4}. A **hit** at d means p mod d ∈ H_d, i.e. r_d | (d+1)/4. R(p) := #{d ≡ 3 (4), 3 ≤ d ≤ (4p+1)/3 : hit}.

**Lemma 1.1.** The following are equivalent for a prime p ≡ 1 (4) (the proof uses neither primality nor the residue
class: it holds for every integer n ≥ 1 in place of p, with the convention that d | n is not a hit):
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
hits" for a random residue. Conditioning on the necessary quadratic information of Lemma 1.2 (only d with χ_p(d) = −1
can hit, and for those the conditional proportion is 2|H_d|/d) gives the conditioned expectation 2Q_p = M − S_p; in §3
this is exactly L₀ + L₂. For n = m² and d coprime to m the term (n/d) = +1 kills the conditioned expectation term by
term (consistent with R(n) = 0); d with gcd(d, m) > 1 are excluded from hits by Lemma 1.2 anyway.

**Theorem 2.1.** For every ε ∈ (0, 1/8) there is p₀(ε) such that for all primes p ≥ p₀ and all 3 ≤ X ≤ 2p:
  |S_p(X)| ≤ (1+4ε)²·(log p)²/64 + O_ε(log p).
Consequently Q_p(X_p) ≥ (7/128 − ε)(log p)² for p ≥ p₁(ε); i.e. the conditioned expectation M − S_p = 2Q_p is at least
(7/8 − o(1))·M: the quadratic constraint of Lemma 1.2 removes at most a fraction 1/8 + o(1) of the expected hits.

*Proof.* χ_p is a non-principal character modulo the prime p (p is not a square — this is the step that fails for F1).
Burgess' bound: for every r ≥ 1, η > 0, uniformly in the integer N₀ and L ≥ 1,
  |Σ_{N₀ < n ≤ N₀ + L} χ_p(n)| ≤ C(r, η) L^{1−1/r} p^{(r+1)/(4r²) + η}.                      (B)
Put K₀ := ⌈p^{1/4+ε}⌉ and split the pairs (k, C) with 4kC ≤ X+1 into four regions.
(I) k ≤ K₀, C ≤ K₀: since 1/(4kC−1) = 1/(4kC) + 1/(4kC(4kC−1)),
  Σ_(I) 1/(4kC − 1) ≤ (1/4)(Σ_{k ≤ K₀} 1/k)² + Σ_{m ≥ 1} τ(m)/(4m(4m−1)) ≤ (1/4)(log K₀ + 1)² + O(1)
  = (1+4ε)²(log p)²/64 + O_ε(log p).
(II) k ≤ K₀ < C: fix k. For a dyadic block C ∈ (T, 2T] ∩ (K₀, (X+1)/(4k)], T ≥ K₀, Abel summation with the monotone
weight 1/(4kC−1) ≤ 1/(4kT) gives |Σ_{block} χ_p(4kC−1)/(4kC−1)| ≤ (2/(4kT))·sup_{T<t≤2T} |Σ_{T<C≤t} χ_p(4kC−1)|.
As 4k ≤ 4K₀ < p, χ_p(4kC − 1) = χ_p(4k)·χ_p(C − a_k) with a_k ≡ (4k)^{-1} (mod p), so the inner sum is a character sum over
an interval of length ≤ T and (B) gives ≤ C(r,η) T^{1−1/r} p^{(r+1)/(4r²)+η}. Summing over the dyadic T = 2^j K₀:
  |Σ_(II), fixed k| ≤ (C/k)·Σ_j (2^j K₀)^{−1/r} p^{(r+1)/(4r²)+η} ≪ (1/k)·p^{−(1/4+ε)/r + (r+1)/(4r²) + η} = (1/k)·p^{1/(4r²) − ε/r + η}.
  Choose r := ⌈1/ε⌉ + 1 (so 1/(4r²) < ε/(2r)) and η := ε/(4r); the exponent is ≤ −ε/(4r) =: −δ. Summing over k ≤ K₀:
  Σ_(II) ≪ p^{−δ} log p.
(III) C ≤ K₀ < k: identical with the roles of k and C exchanged (χ_p(4kC−1) = χ_p(4C)χ_p(k − a_C)).
(IV) k > K₀ and C > K₀: fix k; here k ≤ (X+1)/(4K₀) < p (this is where X ≤ 2p is used), so p ∤ 4k and the
factorisation of (II) is available; sum over C ∈ (K₀, (X+1)/(4k)] in dyadic blocks exactly as in (II) (Burgess' bound
(B) is monotone in L, so a block truncated by the upper limit is bounded by the full dyadic block); the bound
(1/k)p^{−δ} holds for each k, and summing over K₀ < k ≤ (X+1)/(4K₀) gives Σ_(IV) ≪ p^{−δ} log X ≪ p^{−δ} log p.
Adding (I)–(IV) proves the bound on S_p(X).
For the consequence: M(X_p) ≥ (1/4) Σ_{m ≤ Y} τ(m)/m with Y = ⌊(X_p+1)/4⌋ ≥ (p−1)/3, so M(X_p) ≥ (1/8)(log p)² − O(log p) (Σ_{m ≤ Y} τ(m)/m =
(1/2)log²Y + 2γ log Y + O(1)), hence Q_p(X_p) = (M − S_p)/2 ≥ ((1/8 − (1+4ε)²/64)/2)(log p)² − O_ε(log p)
= ((7 − 8ε − 16ε²)/128)(log p)² − O_ε(log p). ∎

*Remarks.* (i) The constant 1/64 is the untouched region k, C ≤ p^{1/4+ε}. Under a hypothesis of cancellation in
χ_p-sums over *arbitrarily shifted* intervals of length ≥ p^{ε'} (which is what the proof needs; I do not claim this
follows from GRH), region (I) would shrink to k, C ≤ p^{ε'} and the constant to ε'²/4. (ii) F2 check: restricted to
C = 2j, the leading coefficients of M and of the region-(I) bound halve; Q₈ ≥ (7/256−ε)log²p > 0 for large p — no
contradiction, because Q > 0 does not imply R ≥ 1 (§3). (iii) F3/F4: the statement is asymptotic; p₀(ε) is effective
in principle (Burgess' constants are) but has not been evaluated; nothing is claimed about the 14 primes or the
composites. (iv) "Conditioned expectation" is meant for the weighted count R̃: the unweighted hit probability given
(p/d) = −1 is 2τ((d+1)/4)/φ(d) at composite d, and 2Q_p = L₀ + L₂ is the φ(d)/d-weighted version.

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
* L_r := Σ_d (1/d) Σ_{χ real, χ ∉ {χ₀, (·/d)}} χ(−p)Ĥ_d(χ̄)   (other real characters, i.e. (·/e) with e squarefree,
  e | d, e ∉ {1, core(d)}; empty for d prime and for d a prime power, e.g. d = 27);
* L_n := Σ_d (1/d) Σ_{χ non-real} χ(−p)Ĥ_d(χ̄).
The real characters mod odd d are n ↦ (n/e) (restricted to gcd(n,d)=1) for squarefree e | d; (·/d) is e = core(d)
(product of primes with odd exponent in d). For a real character (·/e) with d = e·i squarefree, (k/e)(k/i) = (k/d) = 1
gives Ĥ_d((·/e)) = Σ_{k | (d+1)/4} (k/i) = τ_{(·/i)}((d+1)/4) ≥ 0, so
  L_r (squarefree d) = Σ_{ei = d, e,i > 1} (−1/e)·χ_p(e)·τ_{(·/i)}((d+1)/4)/d.
Thus **every real layer is flippable**: it is a sum of the character (−1/e)χ_p(e) = (χ₋₄χ_p)(e) (a character mod 4p)
over e with non-negative arithmetic weights. (The identity (k/e)(k/i) = (k/d) is Jacobi-multiplicative, so the formula
holds for all d = ei with e squarefree, not only squarefree d.)
Terms with small e are the classical local factors (e = 3, p ≡ 1 (3): (−p/3) = −1 and the e = 3 layer is
−Σ_{3|d} τ_{(·/3)}((d+1)/4)/d ≈ −(2L(1,χ₋₃)/12)·log p·(1+o(1)) < 0 — this is the "Mordell penalty": for p ≡ 1 (3) only
k ≡ 2 (3) can hit when 3 | d). Heuristically L_r ≈ Σ_e (−1/e)χ_p(e)·c·log(X_p/e)/e, i.e. of the order of
L(1, (−p/·))·log p = O(log p · log log p) under GRH, but only O(log² p) unconditionally (the e ≤ p^{1/4} range is
not reachable by Burgess). I did not complete a rigorous bound for L_r (EVIDENCE only: §4 table).

**The non-real layer L_n is where the attack stops.** Non-real characters of order m | gcd(d−1, p−1) do have
m-th power reciprocity laws in ℤ[ζ_m] (and gcd(d−1, p−1) can be large, e.g. p = 241, d = 11: orders 5, 10), but no
rational-conductor-p flip usable for a Burgess-type bound is established here, and no bound is proved for any part
of L_n (nor for L_r). The quantity
  Σ_{χ non-real mod d} χ(−p)Ĥ_d(χ̄) = φ(d)[hit at d] − Σ_{χ real} χ(−p)Ĥ_d(χ̄)
is the hit indicator minus its real-character approximation; bounding it for a single p is equivalent to the problem.

**Hypothesis HCE(δ).** For all sufficiently large primes p ≡ 1 (24): L_n(p) + L_r(p) ≥ −(1−δ)·(M(X_p) − S_p(X_p)).
Equivalently R̃(p) ≥ δ(M − S_p) ≫ log²p: a uniform weighted lower bound of the order of the main term, which is
STRONGER than (★) (eventual positivity of R̃), not a weaker or equivalent target.

**Theorem 3.2 (CONDITIONAL on HCE(δ) for some δ > 0).** (★) holds for all sufficiently large primes p ≡ 1 (24).
*Proof.* R̃(p) = (M − S_p) + L_r + L_n ≥ δ(M − S_p) = 2δ Q_p(X_p) ≥ 2δ(7/128 − ε)log²p > 0 by Theorem 2.1. ∎

Honest assessment: HCE is (★) plus a quantitative margin; it is not a standard conjecture and no tool I know
(assessment, not a theorem) (Burgess, Kloosterman/Weil, spectral shifted-convolution bounds, Bombieri–Vinogradov) addresses it
for a single p, because every reformulation (Lemma 1.1(c),(d)) asks about divisors of *specific* integers p + u (or
4Cp+1) in residue classes whose modulus 4u is as large as the interval of u's considered. The one genuinely
individual-p tool, exponential sums Σ_{d≈√p} e(hp/d) (a standard van der Corput second-derivative computation, not
written out here, gives ≪ h^{1/2}p^{1/4}, i.e. equidistribution of p mod d at resolution d/H for H ≤ p^{1/6}), resolves
residues only up to scale p^{1/3}, far from the exact divisibility r_d | (d+1)/4 required. F2 is the quantitative
reminder: the pointwise inequality of a C-even analogue of HCE fails at 12 primes near 10¹⁰ and at ≈ 10⁻³ of the
Mordell primes in [10⁷, 10⁸] (finitely many failures, which do not refute an eventual statement but show its strength).
## §4 Numerical evidence (data/z58/tryf/; all EVIDENCE/CERTIFIED-by-computation, not used in proofs)

**4.1 Engine.** `scripts/z58_tryf_stats.c N` sieves all triples (u,B,C) with n = 4uBC − u − B ≤ N and, for n ≡ 1 (24),
records R(n), R₈(n) (C even), minC, minUB := min over hits of min(u,B), Rpd := hits with d = 4uC−1 prime, min d.
Run to N = 2·10⁸ (≈ 1 min): `data/z58/tryf/stats_2e8.txt` (Mordell-class primes and all R = 0 lines).
Cross-check with the screens: the primes with R = 0 are exactly the 14 of `star_prime_zeros.txt` (all ≡ 1 mod 24; 9 of them in 𝔐),
none in (8 813 281, 2·10⁸]; non-square composites n ≡ 1 (24) with R(n) = 0: 84 up to 2·10⁸ (last: 162 267 625), the
ones ≤ 8·10⁶ agree with `composite_zeros_le8e6.txt`.

**4.2 Mordell-class primes by decade** (p ∈ [10^k, 10^{k+1}); decade 8 is [10⁸, 2·10⁸]):

| k | #primes | R=0 | mean R | min R | R₈=0 | Rpd=0 | max minC | #minC>20 (R>0) | max minUB | #minUB>100 (R>0) |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 27 | 2 | 6.96 | 0 | 7 | 5 | ∞ | 0 | ∞ | 0 |
| 4 | 246 | 1 | 11.83 | 0 | 25 | 16 | ∞ | 3 | ∞ | 0 |
| 5 | 2097 | 2 | 19.04 | 0 | 64 | 37 | ∞ | 31 | ∞ | 1 |
| 6 | 18143 | 4 | 28.18 | 0 | 99 | 87 | ∞ | 123 | ∞ | 3 |
| 7 | 158955 | 0 | 38.92 | 2 | 136 | 245 | 41027 | 658 | 469 | 4 |
| 8 | 166140 | 0 | 44.90 | 4 | 35 | 123 | 324 | 511 | 156 | 2 |

Readings. (i) mean R ≈ (log p)²/8 (e.g. 44.9 vs 0.125·(log 1.4·10⁸)² ≈ 44), i.e. the local factors of the Mordell
classes are close to 1 on average (the Mordell penalty L_r is O(1), see 4.3). (ii) The C-even half fails for ≈ 10⁻³ of
the primes in decade 7 (F2 at 10¹⁰ is the same phenomenon), and the prime-d subfamily fails for a similar proportion.
(iii) Neither small C nor small min(u,B) suffices uniformly: in decade 7 one prime needs C ≥ 41 027 for every hit
(while having a hit with min(u,B) ≤ 469), and some need min(u,B) > 100. Scoped observation: up to 2·10⁸, no fixed
bound on C or on min(u,B) suffices; this does not exclude that some fixed bound suffices eventually.

**4.3 Character layers** (`scripts/z58_tryf_layers.c`; exact decomposition of §3, X = X_p; also re-verifies
Lemma 1.2 at every d ≤ X_p — no failure for any of the 23 primes below). Files `layers_exceptional.txt`, `layers_sample.txt`.

| p | R | R̃ | L₀ = M | L₂ = −S_p | L_r | L_n | Q_p |
|---|---|---|---|---|---|---|---|
| 409 (∉𝔐) | 0 | 0 | 4.76 | +0.64 | −0.07 | −5.32 | 2.70 |
| 5569 | 0 | 0 | 9.57 | −0.89 | −1.24 | −7.45 | 4.34 |
| 102001 | 0 | 0 | 16.94 | −0.80 | −0.90 | −15.24 | 8.07 |
| 1134241 (∉𝔐) | 0 | 0 | 24.64 | −0.86 | −0.66 | −23.12 | 11.89 |
| 8813281 | 0 | 0 | 32.34 | −1.64 | −2.09 | −28.61 | 15.35 |
| 1021441 | 2 | 1.97 | 24.28 | −1.26 | −1.26 | −19.78 | 11.51 |
| 1065409 | 10 | 9.01 | 24.42 | −1.40 | −2.23 | −11.78 | 11.51 |
| 1062601 | 20 | 16.90 | 24.41 | −2.18 | −2.65 | −2.69 | 11.12 |
| 1032721 | 50 | 42.10 | 24.31 | −0.24 | −1.47 | +19.49 | 12.04 |
| 10087009 | 4 | 3.45 | 32.89 | −1.64 | −1.47 | −26.32 | 15.62 |
| 10024009 | 24 | 19.77 | 32.86 | −1.06 | −2.70 | −9.34 | 15.90 |
| 10003729 | 68 | 56.10 | 32.85 | −0.40 | −1.53 | +25.18 | 16.22 |
| 1000033 (∉𝔐) | 32 | 24.71 | 24.20 | −0.26 | −0.59 | +1.36 | 11.97 |
| 1000081 (∉𝔐) | 14 | 12.48 | 24.20 | −0.39 | −0.52 | −10.82 | 11.91 |

Readings. (i) L₀ = M(X_p) ≈ (log p)²/8 as in §2. (ii) The flippable layers L₂, L_r are O(1) in this range — far
below the Burgess worst case (log p)²/64 ≈ 3–4 of Theorem 2.1 — and L_r < 0 for every Mordell-class prime in the table (local
penalty from p being a QR mod 3, 7). (iii) L_n (computed as R̃ − L₀ − L₂ − L_r, so the identity is not a check) fluctuates on the scale of the main
term itself (−28.6 … +25.2 at p ≈ 10⁷); the event R(p) = 0 is "L_n = −(L₀+L₂+L_r)". Empirical spread: see 4.4. Any
proof of (★) via this identity must show L_n > −(L₀+L₂+L_r) for every large p. (The identity forces this
inequality, not any particular technique for proving it.)
**4.4 Empirical distribution of the layers** (`layers_mordell_1e6.txt`: all 329 Mordell-class primes in
[10⁶, 1.15·10⁶], X = X_p). Means (sd): R = 22.5 (9.1), min R = 2; L₀ = 24.44; L₂ = −1.10 (0.47), positive for 4/329;
L_r = −1.55 (0.52), positive for 1/329; L_n = −3.18 (7.26), range [−19.8, +21.9].
Readings. (i) The flippable layers are tightly concentrated and small: L₂ + L_r ≈ −2.65 ± 0.7, i.e. the quadratic
information (Lemma 1.2 + real characters) costs ≈ 11% of L₀ for Mordell-class primes at this height. (ii) L_n has a
non-zero mean ≈ −3.2. A plausible (unverified) attribution is residual local-factor information carried by
small-conductor non-real characters (e.g. p ≡ 1 (5): for 5 | d only k ≡ 4 (5) can hit, of which the real character
(·/5) captures only half); the data do not identify which characters cause the mean. If that attribution is right, a
refined main term would be ≈ 0.76·L₀ here.
(iii) R̃ = 0 requires L_n = −(L₀+L₂+L_r) ≈ −21.8, i.e. (−21.8 + 3.2)/7.3 ≈ 2.6 empirical standard deviations below
the mean at p ≈ 10⁶ (the sd grows roughly like the mean, so this z-score grows only slowly with p, consistent with
exceptional primes thinning out but existing up to 8.8·10⁶).

## §7 Falsifiers re-stated; verdict

What is PROVED here: Lemma 1.1 (equivalences, automatic bound), Lemma 1.2 (quadratic constraint; F1), Lemma 3.1
(exact layer identity), Theorem 2.1 (Burgess: the quadratic layer removes at most 1/8 + o(1) of the expected hits).
What is CONDITIONAL: Theorem 3.2 ((★) for large p under HCE(δ)); HCE is a quantitative restatement of the problem.
What is EVIDENCE: §4 (stats to 2·10⁸; layer tables for 23 primes). Nothing here proves (★) or ES for any new prime.

* (F1) squares: Lemma 1.2 shows R(m²) = 0; for n = m² and d coprime to m the Jacobi-symbol layer cancels the principal layer exactly, so for d coprime to m the
  conditioned expectation vanishes term by term. Theorem 2.1 uses that χ_p is non-principal — the identifiable
  primality/non-squareness step. ✓ (the argument fails at squares where it must).
* (F2) C even: every proved statement (Lemmas 1.1–1.2, 3.1, Theorem 2.1) holds verbatim for the C-even half with M
  halved in leading coefficient; so these statements cannot imply R₈(p) ≥ 1, and indeed they do not imply R ≥ 1
  either — only Theorem 3.2 does, under HCE. The pointwise inequality of a C-even analogue of HCE fails at 12 primes
  near 10¹⁰ (6 of them ≡ 1 mod 24) and at ≈ 10⁻³ of Mordell primes in [10⁷, 10⁸] (§4.2) — finitely many failures,
  which do not disprove an eventual statement but show that the only route to (★) in this memo passes through an
  unproved hypothesis of the same strength as the problem. The memo claims nothing for p > 10¹⁰. Not a hot lead.
* (F3) 285 composites: nothing in the memo applies to composite n (layer sums would need gcd(d,n) = 1, the Jacobi
  character is imprimitive, Theorem 2.1 is not transferred). (F4) 14 primes (and the 38 𝔊*-zeros of a restricted
  subfamily, not studied here): in the decomposition R = 0 means L_r + L_n = −(L₀ + L₂) (§4.3, a tautology, not a
  check); for the primes near 10⁶ this is a deviation of L_n of ≈ 2.6 empirical standard deviations of a 329-prime
  sample at that height (§4.4) — a reading of that sample only. The asymptotic statements are consistent.

Verdict: NO PROOF; no hot lead. What is banked: the simple full-d estimate |S_p(X)| ≤ (1/64 + o(1))log²p uniformly
for X ≤ 2p with its consequence M − S_p ≥ (7/8 − o(1))M (Theorem 2.1), the exact φ(d)/d-weighted layer identity
(Lemma 3.1), and the reproducible census/layer dataset (§4). Not banked: any bound on L_r or L_n; HCE is a target
stronger than (★). Scoped observations for other lanes: (a) a rigorous bound for L_r (Shiu + Pólya–Vinogradov) looks
feasible and would pin the quadratic part of the local factor; (b) up to 2·10⁸, subfamilies with bounded C or
bounded min(u,B) each have zeros in every decade (§4.2) — a finite observation, not a no-go.

## Prior work (credited after the cross-model review; this lane was run unprimed)

Lemmas 1.1–1.2 are rediscoveries of Z56_FAMTRY §1 Lemmas 1.1–1.4 (hit/divisor/C-factorisations, automatic d-bound,
Jacobi argument, square obstruction, τ((d+1)/4)/d and the (1/8)log² heuristic) and of Z57_SYNTH Lemma A.1 (H_d,
bijection, unit/Jacobi statement; its §2.1 is the source of the C-even screen). Z53_GENUSX §1 (Lemmas 1–2, H⁻_𝔉)
already contains a real/non-real splitting with the reciprocity-flipped quadratic component, square cancellation, a
"remainder ≥ −(1−ε)·main" hypothesis on a different subfamily, and prime-conductor Burgess with shifted-interval
factorisation for density layers. The full-d weighted presentation and the specific uniform bound of Theorem 2.1
are, per the review, not duplicated in the repo (no literature-novelty claim).

## Cross-model review (data/z58/xreview/REVIEW_TRYF.md) — what was fixed

Verdict ACCEPT-WITH-FIXES. Applied: (1) removed the false "≤ 6 flippable characters / no reciprocity law"
classification (counterexample p = 241, d = 11) and replaced the prime-d overview in §0 by the all-d weighted identity,
separating algebraic flips from analytic control (only L₂ is bounded); (2) F2/F3/F4 quantifiers repaired (finite zeros
do not refute eventual hypotheses; 6/12 R₈-zeros are ≡ 1 mod 24; C-even halves leading coefficients only; composite
transfer not claimed, coprimality restriction noted; 38 𝔊*-zeros entry added); (3) HCE stated explicitly as a
weighted Ω(log²p) target stronger than (★); GRH remark replaced by the shifted-interval hypothesis actually needed;
"astronomical threshold" assertion removed; weighted-expectation clarification (Remark (iv)); non-squarefree
real-character exclusion e ∉ {1, core(d)} made explicit; (4) prior work credited; bounded-parameter / full-spectrum /
local-factor statements downgraded to scoped observations; "(8 813 281, 2·10⁸]" corrected. Scripts/data unchanged
(the review reproduced all outputs byte-for-byte).
