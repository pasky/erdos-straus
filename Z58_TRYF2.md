# Z58_TRYF2 — tryhard lane F2: "some p+u has a divisor ≡ −1 (mod 4u)"

Lane: TRYF2 (wave z58). Fresh, unprimed attack per `z52bbriefs/z55_tryhard.md` (z55→z58). Only external data used:
`data/z58/screens/`. Scripts: `scripts/z58_tryf2_*`; data: `data/z58/tryf2/`.

**Status line (updated at every commit):** NO PROOF. Everything below is labelled PROVED / CERTIFIED / EVIDENCE /
CONDITIONAL. No HOT LEAD yet.

Notation. For n ≡ 1 (mod 4) put R(n) := #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n} = #{(u,d) : u ≥ 1, d | n+u, d ≡ −1 (mod 4u)}
(matches `scripts/z58_screens_rstar.c`). The target is R(p) ≥ 1 for all large primes p ≡ 1 (24).

## §0 Falsifier behaviour of the line of attack (first commit; re-stated in §9)

The line of attack (§1–§4) is: (i) rewrite R(p) in three equivalent ways that expose where primality enters,
(ii) prove that *no* argument using only finitely many congruence conditions on p can work, (iii) isolate the
exact "non-local" statement that must be proved, (iv) try to prove it by exploiting the Jacobi identity
(d/p) = (−C/d) for d | 4pC+1 and a square-corrected main term.

* (F1) odd squares n = m². The Jacobi identity (§1, Lemma 1.3) gives (d/n) = (−C/d) for every divisor d of
  4nC+1 coprime to n; for n = m² the left side is +1 while d ≡ −1 (mod 4C) forces (−C/d) = −1, so R(m²) = 0.
  The square-corrected main term of §4 is Σ_C [τ(4nC+1) − r_{χ_n}(4nC+1)]/φ(4C), which vanishes *termwise* at
  n = m² (χ_n trivial ⇒ r_{χ_n} = τ). So the step that must use non-squareness is: "χ_n is a non-principal character,
  hence Σ_C r_{χ_n}(4nC+1)/φ(4C) = o(Σ_C τ(4nC+1)/φ(4C))". Identifiable, and it genuinely fails at squares.
* (F2) C even only. Nothing in §1–§3 distinguishes C even from C odd; the main term of §4 restricted to C even is
  exactly half the full one. So the line is only *compatible* with F2 if the final inequality is quantitative with
  a constant that does not survive halving the main term — i.e. an argument of the form "main − |error| > 0" where
  |error| is not o(main). Any claimed proof in this lane that does not have such a quantitative step is wrong by F2.
  (As of this commit there is no such step; see status line.)
* (F3) 285 composite non-squares n ≤ 8·10⁶ with R(n) = 0. The line uses nothing about primality beyond
  non-squareness, so it can at best prove the statement for all large non-square n ≡ 1 (4); F3 is then consistent
  only because "large" must exceed 8·10⁶ — i.e. any argument must be explicitly asymptotic with an effective threshold.
* (F4) 14 prime zeros 409 … 8 813 281. Same remark: the threshold must exceed 8.8·10⁶; a "for all p > 10¹⁰" claim
  would need an explicit error term.

Conclusion of §0: the line can only succeed as a quantitative asymptotic argument with an error term that is
provably < main term for every individual large non-square n. §2–§3 show precisely which range of (u,d) that
error term must control.
