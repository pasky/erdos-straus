# z29_forced_level_characters — what a forced level d lacks: the character χ₋₄ is never forced (O259; B1_LINE §5)

**Idea.** O258 Lemma 2.2(b): at a level d with (d/p) = −1 the integer N = p + 4d has χ₋₄d(N) = −1, so some divisor lies in the
coset χ₋₄d = −1 of G = (ℤ/4d)^*. The b = 1 event needs the single class −1. Try to force it deterministically from character
data alone.
**Literature.** Subset products in abelian groups (Davenport constant; for elementary 2-groups the subset products of a multiset
are exactly the subgroup it generates). Landau/Serre half-dimensional sets; Linnik, Motohashi 1970, Iwaniec 1972
("Primes of the type φ(x, y) + A"): infinitely many primes p with p + A a sum of two squares.
**Result (PROVED, elementary).**
(a) For G elementary abelian of exponent 2 (4d | 24, i.e. d ∈ {1, 2, 3, 6}), level d holds ⟺ −1 ∈ ⟨prime factors of N⟩ ⊂ G.
    By duality this holds ⟸ ψ(N) = −1 for every odd character ψ of G (ψ(−1) = −1).
(b) But χ₋₄ is an odd character of every (ℤ/4d)^*, and χ₋₄(N) = χ₋₄(p) = +1 for p ≡ 1 (4). **So at no level d do the quadratic
    characters of N force the event.** Any divisor w ≡ −1 (mod 4d) is ≡ 3 (mod 4), so level d needs a prime ℓ ≡ 3 (4) dividing
    p + 4d. That is a Landau event, not a congruence: it fails whenever p + 4d is a sum of two coprime squares.
(c) In the dual coordinates (level c: cp + 1 has a divisor ≡ −1 (mod 4c)) χ₋₄ can be forced, but only on congruence classes
    (c = 1: (p + 1)/2 ≡ 3 (4) ⟺ p ≡ 5 (8), the trivial class of Prop 1.4). That is B1.
**Barrier screen.** B1: character forcing = congruence covering, blind at p ≡ 1 (24) / the T1 point. B2: what remains is the
Landau-type event "p + 4d has a prime ≡ 3 (4)" together with the class condition. For one level, its failure set is
infinite. This is expected from Iwaniec-type half-dimensional sieves, but we did not check that the primitive (coprime-squares)
version is in the literature, so it is an Assessment. For all levels d ≤ D at once the failure set is infinite under Dickson
(Thm 4.2). T1: at p = m² every odd character of every level has ψ(p) = +1, the extreme case of (b).
**Cheap numerics.** None needed beyond the census (the implication w ≡ 3 (4) ⇒ a prime ≡ 3 (4) is trivial).
**Assessment.** PROVED (a)–(c); closes goal (5) negatively. The parity of Lemma 2.2(b) is one of at least two odd
characters needed, and the other one (χ₋₄) is never available. Forcing must use the *multiplicative* structure of one integer
p + 4d (subset products), which is B2.
