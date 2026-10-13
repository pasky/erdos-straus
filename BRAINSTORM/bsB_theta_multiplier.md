# bsB_theta_multiplier — the ES sign is the weight-½ theta multiplier of the certificate matrix; Waldspurger screen (O175)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
GI Prop 2.1 found the ES sign only in *odd weight*; SQ says the sign sum vanishes identically exactly on the square
class of 1. Half-integral weight is where square classes live (Shimura lift, Waldspurger, Kohnen–Zagier). Make
the link exact, then test the strongest structural prediction (Shimura-type propagation of zeros along square
classes).

## Dictionary (PROVED, elementary)
Type I a = 1 certificate (c, g, f): γ := S_c S_g S_f = [[n, −m''],[m, −g]] (GI Lemma 1.1; m = gf − 1, m'' = cg − 1,
4 | m). So γ⁻¹ = [[−g, m''],[−m, n]] ∈ Γ₀(4), with lower row (c, d) = (−m, n), d = n ≡ 1 (mod 4), ε_d = 1.
Shimura's theta multiplier is `j(γ⁻¹, z) = ε_d⁻¹ (c/d) (cz + d)^{1/2}`, so
**ν_θ(γ⁻¹) = (−m/n) = (m/n) = (m''/n) = the GI class sign.** Hence:
* ES (Type I, a = 1) at n ⟺ the weight-½ theta multiplier is non-trivial on the explicit finite set
  C(n) = {γ⁻¹ : γ an HJ/continuant certificate word with (1,1)-entry n} ⊂ Γ₀(4).
* T1 = "ν_θ is trivial on every γ ∈ Γ₀(4) whose d-entry is a square" (standard).
* ν_θ² = χ_{−4}(d) = 1 here: the **integral-weight** multiplier (θ², weight 1, and all θ^{2k}) is blind to the
  sign. This is the exact form of "sign-odd part only in odd weight" of GI §2 in the θ-normalisation: the sign
  is seen only by odd powers of θ, i.e. half-odd-integral weight k/2, k odd.
* Waldspurger-type reading (Assessment, analogy only): Σ_{D*(n)} (1 − χ_n(m''))/2 is the "χ_n-twisted minus
  untwisted" mass of a sign-blind measure, with χ_n = (·/n) the character of the square class of n; in Waldspurger
  the square class of n enters through the same χ_n (L(f ⊗ χ_n, ½)).

## Literature
Shimura, "On modular forms of half integral weight", Ann. Math. 97 (1973); Waldspurger, J. Math. Pures Appl. 60
(1981); Kohnen–Zagier, Invent. Math. 64 (1981); Iwaniec, *Topics in classical automorphic forms*, Ch. 2 (theta
multiplier), Ch. 4.

## Barrier screen
* The dictionary moves the sign into a multiplier, i.e. it is the sign layer (SYNTHESIS §0); class layer = which
  words exist (B2). Prop 4.1's reciprocity *is* the multiplier's reciprocity, nothing new.
* **Strongest testable structural consequence (Shimura propagation).** If W(n) behaved like a coefficient of a
  half-integral weight Hecke eigenform, zeros would propagate along square classes (c(t) = 0 ⇒ c(tk²) = 0 for
  eigenforms, by the Shimura relation, for **squarefree t**; R175 repair, D13: in general c(tp²) also
  involves c(t/p²); 17 of the 26 zeros below, 105 included, are squarefree, so the test stands), with the square
  class of 1 as the visible instance. *Test:*
  `scripts/bsB_wcount.c 2000000` (exact W(n) for n ≤ 2·10⁶): W vanishes at all odd squares and at **26
  non-squares**, all ≡ 1 (mod 4), all composite (105, 465, 585, 801, 2641, …, 1618521); but W(105·k²) = 2, 4, 7,
  2, 5 for k = 3, 5, 7, 11, 13, and every other non-square zero r has W(rk²) > 0 for all tested k. **Zeros do not
  propagate: W is not Shimura-like** (also W grows like log²n on average, incompatible with fixed Hecke
  eigenvalues). The square class of 1 is special for multiplier reasons, not because of a vanishing "base
  coefficient".
* By-product (EVIDENCE): W(p) ≥ 1 for **every prime p ≡ 1 (mod 4) up to 2·10⁶** — the single slice a = 1 has no
  prime failure in range; its non-square zeros are composites with small factors (many ≡ 9 mod 24). Consistent
  with DK §9 (five slices vanish only at 105 up to 10⁶).
* B6: any Poincaré/Kloosterman expansion with the multiplier sums over the residue d mod c at fixed c; our set
  has d = n fixed and c = m varying, i.e. a single n — see `bsB_salie_duality.md` for the version with p in the
  c-slot (Type II).

## Assessment
Dictionary PROVED (elementary). (R175 repair, D13: the test refutes only "W is an eigenform coefficient", a
strawman-strength target; it does not touch mechanisms in which W is a sum over forms or periods.) The
Waldspurger/Shimura structural hope is **refuted numerically** (EVIDENCE: zero
propagation fails at r = 105 and all 25 other non-square zeros). Promise 1/5; the useful residue is the Type II
version with p as the Kloosterman modulus (Salié sums), pursued separately.
