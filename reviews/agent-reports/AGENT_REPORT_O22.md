# AGENT REPORT O22 — prime-only majorants for all forced-class mixtures

Branch `side-agent/primelaw`. Deliverable: `EXCEPTIONAL_PRIMELAW.md`, plus
`scripts/primelaw_checks.py` and `data/primelaw/checks.txt`.

## Outcome: positive (cap extends; no obstruction)

* **Thm 3.1 (PROVED; Case A via ElT Prop 1.4).** A *prime majorant* has
  ν(p) ≥ 0 at all primes and ν(p) ≥ 1 at the primes of 𝒜(𝔊), up to
  finitely many exceptions. By Dirichlet this is exactly the LP under the
  unit measure E* on (ℤ/L)^× (Lemma 1.2; no hypothesis on the family).
  For any finite mixture of ℛ(M)-, (a,D)-, Case-A and selector classes
  with arbitrary moduli, a level-λ prime majorant has
  `log(1/E*ν) ≤ Cλ^{3/4}(log λ)^{3/4}`, and `≤ C(B)λ^{3/4}` under bounded B.
* **Why it works.** E* is a product over the unit groups (ℤ/ℓ^e)^×
  (Lemma 1.3). The KARY machinery is arithmetic-free on finite product
  alphabets: EK Thm 2.5/4.1, ETw Thm 2.3′, Prop 4.1, Lemma 4.2/Cor 4.3, and
  the leak. So only three things needed checking:
  * the base: the K2 unit-square base is already made of units, with
    R-term `(π(W)+1)log 2` (Lemma 2.1);
  * the inflation weight: `γ* = (ℓ/(ℓ−1))(1−ℓ^{−1/2})^{−1}` has the four
    properties K2 uses for γ′ (Lemma 2.3);
  * the first and second moments, which follow from those properties
    (Lemmas 2.4–2.5).

  Non-unit forbidden classes (selector classes, and (a,D)-classes with
  `ℓ | gcd(a,D)` or a even) have E*-mass 0, so they come for free.
* **Cor 4.2 (PROVED).** Consider a prime-law method with bound
  `π(N)E*ν + Err`, Err ≥ 0, satisfying either:
  * (H1) all moduli ≤ N^A, which covers SW/BV/BDH/EH/GRH at any
    polynomial level; or
  * (H2) family primes ≤ N^A and Σ|a_i| ≤ N^A.

  Such a method saves at most `C_A(log N)^{3/4}(log log N)^{3/4}`, and
  `C_{A,B}(log N)^{3/4}` under bounded B. Lemma 4.1 is ET Lemma 2.9 under
  E* (projection plus coarsening; it costs a harmless `log λ`).
* **Prop 4.3 (CONDITIONAL on GRH).** Assume moduli ≤ N^A and
  Σ|a_i| ≤ N^{1/2−ε}. Then the *exact* prime sum is
  `≥ (1−o(1))li(N)E*ν`, so signed or exact error handling cannot help.
  Unconditionally the error terms are too weak (NC Rem 3.4).
* **§4.4.** NC Thm 3.3 (sieve-detected primality) holds for all mixtures
  with **no** `(log log N)²` loss, because `𝒜 ∩ {(n,P(z))=1}` is the
  avoider set of the family with selector classes added (K2 Thm 5.1
  directly).

## Exclusions (§6)
* The `(log log N)^{3/4}` factor without B.
* ν ≥ 0 only at primes ≤ N.
* ν ≥ 1 only at the actual exceptional primes (non-CRT).
* Unconditional signed errors.
* Budgets beyond N^{O(1)}.
* Prime-count methods not of the form Σν(p) (Type I/II, Halász).
* The large sieve applied to primes: LARGESIEVE duality under E* was not
  checked.

## Numerics (EVIDENCE, ~21 s)
* The γ* inequalities hold for all primes ≤ 10⁶.
* `φ(Q₀)/|R| = 2^{π(W)+1}` holds.
* All ℛ(M)- and Case-A residues are units, and the (a,D) non-unit primes
  are exactly as predicted (36,000 classes).
* Toy exact LP over all four types with modulus | 120120, arity ≤ 2: the
  integer-vs-unit gap is ≤ log(L/φ(L)), as it must be. The k = 3 run did
  not finish in 40 min (not needed).

## Suggested ledger wording (parent's call)
DISCOVERIES (D)18 "Does not cover" / K2 §6 item 3: drop "majorants ≥ 1 …
on exceptional primes" and replace it with a pointer to the new entry:

> EXCEPTIONAL_PRIMELAW Thm 3.1, Cor 4.2: prime-only majorants
> (Dirichlet/unit measure) over any K2 mixture are capped at
> `C(log N)^{3/4}(log log N)^{3/4}` for any equidistribution level `N^{O(1)}`.
> PROVED (internal, unreviewed). Under GRH even signed error accounting
> cannot help (Prop 4.3, CONDITIONAL).

## Review hot spots
* Prop 2.2's three checks (g_j ≥ 0 on units, λ-locality, g_{J+1} = ν).
* The claim that K2 uses γ′ only through the four listed facts (the
  remark after Lemma 2.3).
* Lemma 4.1's projection coefficient `κ_i = φ(L_𝔊)/φ(lcm) ≤ 1`.
* Prop 4.3's error bookkeeping for q > x.

I did not edit DISCOVERIES/STATUS. Stopping for parent review.

## Round 2: review repairs applied (checkpoint 2)

The review is `reviews/exceptional-primelaw-review.md` (branch
`side-agent/review-primelaw`). It found every item SOUND. Repairs:
* **D1.** I had called the unit R-term smaller than NC Thm 3.2's. That
  was false, and it is corrected in §2.1 and Remark 3.2. The exact
  relation is: unit R-term = K2 R-term − log(Q₀/φ(Q₀)). This is larger
  than NC's 0 for selector bases.
* **D2.** The headline, the bold line in §4.2 and the §0 summary now state
  both qualifiers: ν ≥ 0 at *all* primes (Def 1.1), and error terms
  bounded in absolute value (Err ≥ 0).
* **D3.** Cor 4.2 now says that, for validity, Err must contain the
  correction `Σ_{p|L, p≤N}(1+|ν(p)|)`. After Lemma 1.2 I added the
  observation that the exceptions in Def 1.1 automatically lie in {p | L}.
* **D4.** The level is now defined with Theorem 3.1's W. A change of W
  shifts the level by at most θ(W) ≤ 2W.
* **D5.**
  * Prop 2.2 now lists step costs Φ consistently, with the factor 2
    applied once.
  * §4.4 is qualified: nothing beyond K2's own cap. NC's bounded-B
    families lose nothing at all. The reading needs z ≤ N^A.
* **D6.** §6 item 2 now has a Linnik–Xylouris / Bach–Sorenson remark. The
  finite-range relaxations close for L ≤ cN^{1/5}, or L ≲ √N/log N under
  GRH. So that gap lives at L > N^c.

The Replay section now also cites the reviewer's script, which lives on
their branch.

**Corrected ledger wording** (it replaces the suggestion above):

> EXCEPTIONAL_PRIMELAW Thm 3.1, Cor 4.2: prime majorants in the sense of
> Def 1.1 (≥ 0 at all primes, ≥ 1 at all primes of 𝒜(𝔊); Dirichlet/unit
> measure) over any K2 mixture, with error terms bounded in absolute value
> (Err ≥ 0), save at most `C(log N)^{3/4}(log log N)^{3/4}` at any level
> `N^{O(1)}` (`C_B(log N)^{3/4}` under bounded B). **PROVED** (internal;
> review `reviews/exceptional-primelaw-review.md`, SOUND). Under GRH,
> signed error accounting cannot help either (Prop 4.3, CONDITIONAL).
> Open: ν ≥ 0 only at primes ≤ N with L > N^c; unconditional signed
> errors; the prime large sieve.
