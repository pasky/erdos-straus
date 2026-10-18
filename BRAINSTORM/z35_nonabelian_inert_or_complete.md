# z35_nonabelian_inert_or_complete — the non-abelian part of Frob_p: inert at bounded level, complete at unbounded level (O265)

## Idea
R272 D2 corrected O263: Frobenius data of p = congruence data + an independent NON-ABELIAN part (power-residue / Kummer data).
Does that part act on certificates? (MODP_RECIPROCITY §2.) Prop 2.1: for any finite certificate menu with bounded witnesses,
the event depends on p mod M only, so by Chebotarev the non-abelian part is inert (the abelian part can force, e.g. p ≡ −4 (7)).
Prop 2.2: the order-4 characters χ_π at the primes q ≡ 3 (4) determine π (Dirichlet: a character mod 4pp′ trivial on all
primes ≡ 3 (4) is trivial), so at unbounded level the non-abelian data ARE p — no independence barrier there; any mechanism
must use (a, b) as numbers.

## Literature
Chebotarev; Dirichlet; CLASS_FORCING Thm 2.1(b) (fibre product); R272 review of O263 (D1, D2).

## Barrier screen
B1 at bounded level (the abelian part is a congruence covering, with the usual p ≡ 1 (M) hole); at unbounded level the
question becomes B2 in Gaussian coordinates (z35_anti_windows).

## Cheap numerics
`scripts/z35_quartic_independence.py 2000000 40`: 240 stratified tests (levels d ≤ 40, quartic symbols of 2, 3, 5, 7, 11, 13):
max |z| = 2.46, none > 3.

## Assessment
PROVED (both propositions are short) + EVIDENCE. Clarifies the R272 framing: "independent non-abelian part" is independent
only at bounded level.
