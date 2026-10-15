# s6_ydual_windows — 𝒟_e(M) is the y-window; the pointwise/almost-all boundary is "who owns the mute set" (O238; (iv))

## Idea
CAP_INTERPOLATION Prop 5.1: y = pA with A = (M + 1)/4 FIXED, p ≡ −4D (mod M), D ∈ 𝒟_e(M) (rad D | A). CAP_DOWN Lemma 1.1:
x = K = (p + m)/4 MOVING with p. Both are Lemma 3.1 slices of the same equation, with the roles of x and y exchanged.
**Prop (PROVED).** (a) y-window: for fixed M, ES^{(y,e)} of shot shape y = pA at any cap needs −p/4 ∈ ⟨primes of A⟩ (mod M) (every
D ∈ 𝒟_e(M) has rad D | A; the converse fails in general because odd exponents above 2v_s(A) are excluded at every e); if ⟨primes of A⟩ is a proper subgroup of (ℤ/M)^*, a positive
proportion of residue classes of p fails at EVERY cap. (b) x-window: (K/q) = (p/q) is a character of p, so on the half of
the classes where it is −1 the subgroup contains −1 for every p (forced; R245 repair: under CAP_POINTWISE Thm 1.1 (ii) or CAP_DOWN Thm 1.2 (E)/Addendum).
(Assessment from here to the end of the paragraph — R246 repair.) So the phase boundary between almost-all (sieve) and pointwise (forced) statements is exactly whether the mute set is a
function of p: fixed mute set ⟹ Chebotarev in a fixed field, the large sieve, (e + 3)/(e + 4) exponents (B6);
self-generated mute set ⟹ a reciprocity identity for each p.
Composite multipliers of the 3/4 note at cap e are the y-window menu; nothing in the x-window menu is a fixed class.

## Literature
paper/es-threequarter-note; CAP_INTERPOLATION §5; CAP_POINTWISE Remark 1.4.

## Barrier screen
(a) is B1 (fixed congruence menu); (b) evades B6 but meets B2 at cap 0. A hybrid "both windows moving" is Lemma 3.1 at
general (x, y), i.e. ES itself.

## Cheap numerics
None needed beyond the definitions (e.g. M = 7, A = 2: ⟨2⟩ = {1, 2, 4} has index 2; p with −p/4 ∉ ⟨2⟩, i.e. p ≡ 1, 2, 4
(mod 7), never fire at the y-window M = 7 at any cap).

## Assessment
PROVED dictionary, negative for (iv): composite multipliers at cap e stay on the almost-all side by construction.
