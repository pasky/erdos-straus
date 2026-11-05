# Z59_MSPF — tryhard lane MSPF (wave z59): the pointwise statement for 4uBC − u − B = n

Status line (updated at every commit): **IN PROGRESS** — no hot lead yet.

Problem (verbatim target). For every sufficiently large non-square n with n mod 840 ∈ 𝔐 = {1, 121, 169, 289, 361, 529}
(n ≡ 1 (24), n a nonzero square mod 5 and mod 7), the equation 4uBC − u − B = n has a solution in positive integers.
Equivalently: some d ≡ 3 (mod 4), d ≥ 3, has k := (−n mod d) dividing (d+1)/4.

## §0 Mandatory falsifiers (stated up front; re-stated in §9 at the end)

Any argument for the target must be run through all four of the following. Where this memo proves something, the
relevant falsifier is answered explicitly next to the proof; where it does not, the memo says so.

* **(F1) Odd squares.** R(m²) = 0 for every odd m (CERTIFIED in data/z58/screens/README.md; re-proved below as Lemma 1.3:
  for every admissible pair (d, k), −k is a Jacobi non-residue mod d). Consequence (Lemma 1.4): *no* argument that uses
  only congruence information about n (n mod M for any fixed M, or any finite set of residue conditions) can prove the
  target, because odd squares occupy every residue class in 𝔐 that the target concerns. A correct proof must use a
  global property of n that distinguishes it from m² — the only such property available in the problem is that the
  Jacobi character χ_n(·) = (·/n) is non-principal (it is principal iff n is a square). Every step of any proof
  below must point to where this is used; the step that fails at n = m² must be identified.
* **(F2) C even alone.** The C-even part of the family (4uBC − u − B = n with C even ⇔ 8u′BC′ … see §1) fails at 4
  primes in 𝔐 ∩ [10¹⁰, 1.1·10¹⁰] (data/z58/screens/r8_zeros_1e10.txt, those with p mod 840 ∈ 𝔐). So any argument that
  only ever produces even C (e.g. only uses moduli 8k | n + k + B) is wrong; the memo must say which parity of C the
  construction produces and why odd C is reachable.
* **(F3) Non-square zeros.** Inside 𝔐 non-square zeros exist up to 17 401 609 and nowhere in (17 401 609, 10¹¹];
  outside 𝔐 non-square zeros continue indefinitely (mostly 3 | n, 5 | n or 7 | n). Any proof must (a) produce an explicit
  threshold n₀ (or explain why it cannot), with n₀ > 17 401 609, and (b) fail for n ∉ 𝔐 — the step that uses
  n ≡ 1 (24), (n/5) = (n/7) = 1 must be identified. (For n with 3 | n, 5 | n or 7 | n the moduli d divisible by 3, 5, 7
  are dead, which is the explanation of most outside-𝔐 zeros; the memo must not rely on those d.)
* **(F4) The nine prime zeros** 5569, 9601, 83449, 102001, 712321, 1724209, 1726201, 5212561, 8813281 (all in 𝔐).
  Any construction (choice of d, k as functions of n) must be evaluated at these nine; it must fail there, and the memo
  must say which hypothesis (size, a "sufficiently large" threshold, or a structural hypothesis) excludes them.

Surviving all four honestly = hot lead, to be flagged in the title and committed at once.

## §1 Reformulations (PROVED)

(Filled in next commit.)
