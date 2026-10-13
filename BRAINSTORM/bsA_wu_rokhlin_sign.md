# bsA_wu_rokhlin_sign — the ES sign is the Wu-square (Rokhlin invariant) of the plumbing (O174)

## Idea
DK Thm 4.5 says the sign (A/n) of a length-3 word is a mod-4 function of the letters, positive on five cells. DK 5.2
calls this "van der Blij–Milgram–type" without making it precise. Make it precise: compute the characteristic (Wu)
vector w of the plumbing lattice and compare.

Let G be the Gram matrix of a positive-definite integral lattice Λ of rank r and odd determinant n. Let w ∈ Λ be
characteristic (w·x ≡ x·x mod 2 for all x). Then w is unique mod 2Λ, and w·w mod 8 is well defined.

**Theorem W (PROVED for linear plumbings of length r ≤ 5; EVIDENCE for general lattices).** For every HJ word
n/A = [[b₁,…,b_r]] with n odd, with G the tridiagonal plumbing matrix (diagonal b_i, off-diagonal −1):
**(A/n) = +1 ⟺ w·w ≡ n + r − 1 (mod 8)**, and (A/n) = −1 ⟺ w·w ≡ n + r + 3 (mod 8).
*Proof for r ≤ 5.* The mod-2 vector ε of w depends only on the letters mod 2. Then w·w = Σε_i b_i − 2Σε_iε_{i+1} mod 8,
and n mod 8 are polynomials in the letters mod 8. For fixed r, (A/n) is also a function of the letters mod 8 (DK Cor 4.1,
PROVED). So a check over letters 2..9, which covers all residues mod 8, proves the identity. `scripts/bsA_wu2.py` does
this: 24 692 words with r ≤ 5 and 0 failures. (`bsA_wu.py` shows the r = 3 table: n ≡ 1 (8): w·w ≡ 3 ↦ +1, 7 ↦ −1;
n ≡ 5 (8): 3 ↦ −1, 7 ↦ +1; etc.)
*General lattices (EVIDENCE).* For 3000 random positive-definite rank-3 lattices of prime determinant p, the
discriminant-form square class satisfies the same rule (0 failures). This is the classical van der Blij/Milgram
characteristic Gauss-sum formula, quoted from memory (the research subagent could not verify the odd-lattice form).

**Corollary W1 (ES in Wu language).** For p ≡ 1 (4): five-slice interior ES(p) ⟺ **some linear ternary plumbing of
determinant p has w·w ≡ p + 6 (mod 8)** (i.e. ≡ 7 if p ≡ 1 (8), ≡ 3 if p ≡ 5 (8)). DK's five mod-4 conditions are this one
congruence. In the ternary-lattice picture (bsA_selling_sandpile), the genus G⁻(p) is exactly {Λ : w·w ≡ p + 6 (8)}.
**Corollary W2 (T1 in Wu language; PROVED for r ≤ 5).** If n = m² is an odd square, every linear plumbing of
determinant n has w·w ≡ r (mod 8). So at squares the Wu-square is rigid, and no length-3 plumbing reaches the class p + 6.
**Rokhlin reading (convention from memory).** For Y = ∂X with its unique spin structure (n odd), Kaplan's formula
gives μ(Y) ≡ σ(X) − w·w (mod 16). Here σ = r, so **(A/n) = +1 ⟺ μ(L(n,A)) ≡ 1 − n (mod 8)**, independently of the
plumbing chosen. The ES sign is the mod-8 Rokhlin invariant of the lens space, and five-slice ES(p) ⟺ a lens space of order p with
μ ≡ 5 − p (mod 8) has a ≤ 3-sphere linear plumbing.

## Literature
van der Blij, *An invariant of quadratic forms mod 8* (Indag. Math. 1959; from memory). Milgram (1973; from memory).
Kaplan, Trans. AMS 1979 (Rokhlin invariant from plumbings; from memory). Deloup–Turaev reciprocity for Gauss sums (not
verified). Kirby–Melvin, *Dedekind sums, μ-invariants and the signature cocycle* (Math. Ann. 1994; from memory). This
paper ties μ of lens spaces to Dedekind sums, consistent with DK (D2) + (R).

## Barrier screen
* Purely a sign-layer statement (B1, Prop S, Prop 10.3). It is the genus character again, now as a Rokhlin/Brown-type
  invariant. It is T1-correct (W2).
* It changes nothing in the class layer. Shortness (r = 3) is the B2 divisor event.
* Value: it removes the "five cells" bookkeeping. Any future mechanism needs only to produce a short plumbing with
  the *wrong Wu-square*, and the Wu vector is a mod-2 object attached to a lattice (Smith/Wu-type parity structures).

## Cheap numerics
`scripts/bsA_wu.py` (r = 3 table, letters ≤ 33), `scripts/bsA_wu2.py` (r ≤ 5 and random lattices).

## Assessment
PROVED clean reformulation (r ≤ 5 by finite check relative to DK Cor 4.1; general r and general lattices EVIDENCE plus
classical). It is novel only as packaging. It is the most compact form of the ES sign I know: **sign = w·w − n − r + 1 mod 8**.
Promise 1/5 as a route. As a dictionary item it is SHARP.
