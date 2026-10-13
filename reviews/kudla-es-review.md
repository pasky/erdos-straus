# R172 — hostile review of O172 `KUDLA_ES.md` (Kudla program / incoherent Eisenstein series vs ES)

Reviewer branch `side-agent/review-kudla` (merged `side-agent/kudla-incoherent` at the start). From-scratch scripts:
`scripts/review_kud_tuples.py` (own Type I / II enumeration, own Hilbert symbol validated against brute-force ℚ_p
solvability, Diff computed from the **Gram matrix** of T via the Hasse invariant of `U ⊕ ⟨det U⟩`, i.e. *not* via the
author's algebra identification `(−d, −dne)`), `scripts/review_kud_genus.py` (§2). Kudla 1997 / KRY 2006 / Gross–Keating
are **not** in `sources/`; statements about them below are from the reviewer's knowledge and are flagged as such.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (2 ∉ Diff, Type I) | SOUND |
| Thm 1.2 (Type I Diff formula, T1 for Type I, Diff = {p} at n = p) | SOUND (wording repairs: D3, D4, D5) |
| Identification Diff(T, 𝒞) = Ram_fin(B_T), 𝒞 = (M₂(ℚ_ℓ)⁰, det)_ℓ ∪ (pos. def.)_∞ | SOUND (convention correct; citation scope D2) |
| Thm 1.4 (Type II Diff formula, T1 for Type II) | SOUND |
| Remark: e·T' vs T' | SOUND (count reproduced exactly; reading D6) |
| "certificates at n = p are supersingular points mod p of Z(T)" | SOUND-AFTER-REPAIRS (D5) |
| Novelty statement (Hilbert reciprocity / ET Prop 1.6 restated) | SOUND — nothing stronger is claimed in the theorems; one summary overclaim (D4) |
| (sections 2, 3: see below) | |

## Independent numerics (§1)

`PYTHONPATH=scripts uv run --with sympy python scripts/review_kud_tuples.py 20000` (≈1 min; also run at 1000):
* own Hilbert symbol vs brute-force primitive-solution search mod p^K (p ∈ {2,3,5}, squarefree |a|,|b| ≤ 12): 0 mismatches;
* Type I, all odd n ∈ [3, 20000], a ≤ b: **882749** tuples (= author's count); Diff(T(d,ab)) from the Gram route equals
  `{ℓ | n : v_ℓ(n) odd, ℓ ∤ e, (−d/ℓ) = −1}` in all cases; 2 never in Diff; |Diff| always odd; 254619 tuples at prime n,
  Diff = {n} in all, n | e never; 0 tuples at odd squares; odd non-squares with no tuple: **105, 2961, 3705** (author: "3");
* Type II: **336357** tuples (= author); Diff(T') equals `{ℓ | n : v_ℓ(n) odd, (−f/ℓ) = −1}` in all cases; 2 never in
  Diff; |Diff| odd; 0 at odd squares; odd non-square with no tuple: **4545** (author: "1");
* e·T' remark: Diff(e·T') = Ram_fin((−d, −n)) in all 336357 cases (so the Gram e·T' is indeed that of a pair in (−d,−n)),
  and Diff(e·T') = Diff(T') in 170966/336357 = 50.8% ("~half" confirmed).
(A first version of my Type I enumerator had a wrong a-cutoff and found 704737; diffing against an enumeration of the
same parametrisation located my bug, not the author's — recorded for honesty.)

## Re-derivation of §1 (reviewer)

*Binary → ternary → quaternion.* For trace-zero u, v with Gram T (form nrd), `U = ℤu + ℤv`; since `B⁰ ≅ ⟨−α, −β, αβ⟩` has
square determinant, Witt cancellation gives `V ≅ U ⊕ ⟨det U⟩` for any ternary V of square determinant containing U. Hence
U ⊂ 𝒞_ℓ = M₂(ℚ_ℓ)⁰ ⟺ `U ⊕ ⟨det U⟩` isotropic ⟺ B_U split at ℓ, and 𝒞_∞ (positive definite, det 1) contains every positive
definite U. Diagonalising, `T(d,m) ~ ⟨d, d(4dm−1)⟩`, `T' ~ ⟨f, f(ff'−1)⟩`, giving `B = (−d, −d(4dm−1))`, `(−f, −f(ff'−1))`
as stated. Incoherence: Hasse invariant of ⟨1,−1,−1⟩ is −1, of ⟨1,1,1⟩ is +1, so switching ∞ makes ∏ε_v = −1. The
convention (Q(x) = nrd(x) = −x² on trace-zero elements, signature (1,2) globally, positive definite at ∞ in 𝒞) is the one
of Kudla 1997 / KRY for Shimura curves, specialised to B = M₂(ℚ) (reviewer's knowledge; sources not in repo). ✔

*Thm 1.2 local computation.* Re-done place by place; all cases correct. Notes: ℓ | d ⇒ ℓ ∤ ne (since ne = 4abd − 1), so the
set in the theorem automatically avoids ℓ | d; ℓ | e is cleared because `e | 4a²d + 1` (from `4ad(a+b) = (4a²d+1) + ne`),
which gives `(−d/ℓ) = 1` and kills the symbol regardless of v_ℓ(ne); Lemma 1.1 (reduced discriminant 4dm − 1 odd ⇒ Λ ⊗ ℤ₂
maximal with unit discriminant ⇒ split) is correct and holds for **every** T(d, m), independent of ES. ✔

*Thm 1.4 local computation.* Re-done; correct. gcd(f, n) = 1 (from ff' − 4c²dn = 1); ℓ | d ⇒ −f ≡ 1 (mod ℓ); at 2:
f ≡ −1 (mod 4), and 2 | d ⇒ 8 | 4cd ⇒ −f ≡ 1 (mod 8), a 2-adic square. ✔

## Defects

(numbered; severity FATAL / MAJOR / MINOR; written incrementally)

**D1 (MINOR) — §1 Thm 1.2 *Check* / Thm 1.4 *Check*, "3 odd non-squares … have no tuple", "1 odd non-square … has none".**
The counts are right but the numbers should be named (105, 2961, 3705 for Type I; 4545 for Type II — all composite, and
none of them lacks both types), since "odd n with no Type I tuple" is a recurring campaign datum. *Repair:* list them.

**D2 (MINOR) — header paragraph and §1 setting: citation scope.** Kudla, Ann. Math. 146 (1997) is (to the reviewer's
knowledge) stated for an indefinite *division* quaternion algebra (D(B) > 1, compact Shimura curve); the modular-curve case
B = M₂(ℚ) needs the non-proper model and is not literally covered there; KRY's book is also set up for Shimura curves.
For positive definite T the special cycle avoids the cusps and the local identity at ℓ ∈ Diff(T) is the same
Gross–Keating computation, so the *geometric reading* is right, but the citation should say so. Since these identities
are "cited, not used" this affects no PROVED statement. *Repair:* add "(for B = M₂(ℚ) and positive definite T the
relevant identity is the local one at the unique ℓ ∈ Diff(T); Kudla 1997 is stated for D(B) > 1)". Sources not accessible
in the repo — state that explicitly.

**D3 (MINOR) — §1 setting, last sentence ("a point of the special cycle Z(T) is a supersingular E/𝔽̄_ℓ (ℓ ∈ Diff(T))").**
For positive definite T, Z(T) is non-empty iff |Diff(T)| = 1 (it is then supported in characteristic ℓ, Diff(T) = {ℓ});
if |Diff(T)| ≥ 3 the algebra B_T is ramified at ≥ 3 finite places, no End(E)⊗ℚ contains it, and Z(T) = ∅. Thm 1.2/1.4 are
stated for all odd n, and for composite n the certificate indices typically have |Diff| ≥ 3 (they are then *not* in the
support of E'(τ,0,Φ)_T; that coefficient is 0 when |Diff| ≥ 3). *Repair:* "Z(T) ≠ ∅ iff Diff(T) = {ℓ}, and then Z(T) is
supported at supersingular points in characteristic ℓ; for |Diff(T)| ≥ 3 both Z(T) and the T-th coefficient of
E'(τ,0,Φ_𝒞) vanish."

**D4 (MINOR) — §1 "Reading", §1 Summary, report SHARP bullet: "the ES congruence conditions … are *exactly* what clears
every place except the primes of n".** Overclaim on two counts. (i) Not all clearing is done by the congruence: for Type I,
2 is cleared for *every* T(d, m) (Lemma 1.1, det(2T) odd), odd ℓ | d by the defining equation 4abd = ne + 1 (not by
e | a + b), and ∞ is never in Diff because 𝒞_∞ is positive definite; only the places ℓ | e use e | a + b. (ii) "Exactly"
suggests necessity; what is necessary and sufficient for Diff ⊆ Odd(n) is the genus condition ((−d/ℓ) = 1 for ℓ with
v_ℓ(e) odd, resp. Prop 2.2(c) for Type II), which is far weaker than e | a + b / f ≡ −1 (4cd) — as §2 itself says.
*Repair:* "the ES congruences are *sufficient* to clear every place ℓ ∤ n (for Type I, with 2 and ℓ | d cleared already by
the shape of T and the equation); only their genus shadow is needed."

**D5 (MINOR, wording) — Thm 1.2(b), §1 Summary, Prop 2.1, report: "certificates *are* supersingular points mod p of
Z(T)".** A certificate determines an *index* T; points of Z(T) are triples (E, x, y). For Type I this is fine: Λ_{d,ab} =
ℤ⟨u,v⟩ is an order of B_{p,∞}, every order lies in a maximal order, every maximal order is End(E) (Deuring), so the
certificate yields points (one per embedding class). For Type II, T' is *not* the Gram matrix of any pair of elements
attached to the certificate: the certificate's own pair (2ai+j, 2bi−j) has Gram e·T' and lives in (−d, −p), and my check
(`scripts/review_kud_eT.py 5000`, Type II tuples at prime n ≤ 5000) gives Diff(e·T') = {p} in only 10976/17435 cases;
in 5555 cases p ∉ Diff(e·T') (the natural pair is a special-cycle point in some *other* characteristic), in 904 cases
|Diff(e·T')| ≥ 3 (Z(e·T') = ∅). So for Type II the statement is: "the certificate determines an index T' with Diff(T') = {p},
hence Z(T')(𝔽̄_p) ≠ ∅". Moreover *every* positive definite T with Diff(T) = {p} has this property (Prop 2.3 shows how
cheap this is), so "lies in the support" is a property of the index's genus, not a certificate property. *Repair:* reword
as indicated; keep the e·T' Remark and add the 63/32/5 % split at prime n.

**D6 (MINOR) — Remark after Thm 1.4: "The T1-relevant Kudla index is T', not eT'."** Correct as a computation, but T' is
a *choice* (the Heegner form [f, 2, f']), selected because its Diff is controlled; nothing in the Kudla formalism singles it
out over e·T' (the Gram of the pair that actually appears in QUATERNION_ES Lemma 3.1). *Repair:* say "a T1-relevant
index is T' (chosen); the natural Gram e·T' is not T1-relevant in ≈ 37% of prime cases".

**Novelty (checked).** Thm 1.2(a)/1.4(a) are ET Prop 1.6 (odd squares have no Type I/II tuples); the Type I refinement
`∏_{ℓ|n, ℓ∤e}(−d/ℓ)^{v_ℓ(n)} = −1` and Diff = {p} at n = p are QUATERNION_ES Prop 1.3 (R130-repaired) extended to composite n.
The author's own caveat ("Hilbert reciprocity … a new dictionary, not new arithmetic") is accurate, and no theorem claims
more. Only the "⟺" in "T1 ⟺ incoherence parity" (§1 Summary) is rhetorical: one direction (oddness ⇒ no tuple at squares)
is the theorem; the converse has no content. Acceptable as Assessment.
