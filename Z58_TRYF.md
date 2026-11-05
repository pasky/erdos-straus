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

(to be written)

## §2 Layer 2: the quadratic obstruction is harmless for primes (PROVED)

(to be written)

## §3 Character-layer reduction and the hypothesis HCE

(to be written)

## §4 Numerical evidence (data/z58/tryf/)

(to be written)

## §7 Falsifiers re-stated; hostile review; verdict

(to be written)
