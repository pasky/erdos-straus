# z27_small_exponent_windows — composite windows whose unit group has tiny exponent (O256 iteration)

**Idea (violate the hypothesis "the window group is cyclic of order ≍ window").** Take m = ∏ q_j with every (q_j − 1)/2 | E.
Then U_m has exponent | E, so ANY box with sides ≥ E − 1 covers ⟨g_s⟩: covering is automatic at cap ≈ E once the s² generate
(rank ≤ k), with no Diophantine (large-order character) problem at all — the obstruction of z27_pretentious_dual disappears.
**Obstruction found (PROVED for the construction, Assessment for the route).** The prime factors must come from the finite set
Q(E) = {q : (q−1)/2 | E}, |Q(E)| ≤ τ(E). Forcing at q_j | m is a χ_p condition; by Dirichlet/Linnik there are p ≡ 1 (mod 4∏Q(E))
with χ_p ≡ 1 on Q(E), log p ≪ Σ_{q∈Q(E)} log q ≤ τ(E) log(2E+1): for them no window built from Q(E) is forced (parity not
free). (R-O256 repair 8: the fixed-menu statement does not by itself bound an adaptively chosen E.) For all E ≤ T at once: every
Q(E) lies in the primes ≤ 2T + 1; Linnik/primorial progressions give infinitely many p with χ_p(q) = 1 for all q ≤ 2T + 1 and
log p = Θ(T). For these p the menu strategy needs E > T ≍ log p: cap ≳ log p i.o., worse than GRH's exp(O(√(log₂p log₃p))). Also the class condition m ≡ −p (mod P) becomes a subset-product covering problem in
(ℤ/P)^* — the same covering problem in the dual group (products of small cyclic groups), circular.
**Literature.** Davenport constant / Olson (zero-sum and subset-sum covering in groups of small exponent); Linnik.
**Barrier screen.** B1 (finite menus Q(E)) — exactly POINTWISE_SIZE-type: a fixed finite prime menu fails i.o.
**Cheap numerics.** none needed (counting).
**Assessment.** PROVED-level obstruction (Linnik adversary): cap ≳ log p i.o. for this menu strategy; dead at polylog-log caps.
