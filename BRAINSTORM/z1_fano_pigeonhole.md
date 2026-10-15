# z1_fano_pigeonhole — why the five 4-slices are a character fibre: pigeonhole in ℙ(L/2L) (O224) — SHARP

## Idea
MODEL_SPECIFIC Thm 3.1(a) ("w ∈ S_4 ⟺ χ(w) = −1") was proved by enumerating 320 cells mod 8 (via Dedekind sums, or via
CHI_FLIP's mod-8 lemma). Look for the conceptual reason inside the 2-adic lattice L_w ⊗ ℤ₂, using the five pentagon entries
as the norms (up to the odd factor n in the last two) of five explicit primitive vectors e₁, e₂, e₃, f = n e₁^#, f* = n e₃^#
(norms v, t, u, nA, nA*).

## Literature
CONSTRUCTIVE_ES Lemma 1.1 (mod-4 isotropy test, two classes), CHI_FLIP Thm 1.1 (χ = −ε₂), TRANSPORT_LAW / (J)45 (the unique
even edge of the frieze, Morier-Genoud's mod-2 frieze rigidity), Conway–Coxeter friezes. The Fano argument itself was not
found in the campaign files (`git grep -i fano` before this memo: no hit in a lattice context).

## Result (PROVED; full proof in FOUR_ADIC_INPUT.md §1, Thm 1.3)
q = Q mod 4 is well defined on L/2L; W = {q even} is a 2-plane, so W ∖ 0 is a 3-point line of the Fano plane.
(a) Frieze parity: exactly two pentagon entries are even, giving two distinct points of W ∖ 0 (Lemma 1.1 there).
(b) Isotropic L₂ has exactly two nonzero points with q = 0, both in W ∖ 0 (CONSTRUCTIVE_ES Lemma 1.1).
(c) Two 2-subsets of a 3-set meet, so χ = −1 ⇒ some pentagon entry ≡ 0 (mod 4). The converse is the mod-4 isotropy test.
For prime n = p the two isotropic points are the two endpoints of the Eichler edge (CONSTRUCTIVE_ES Thm 1.2(b)), so a certificate is a
word plus a pentagon vector pointing at an endpoint of its 2-isogeny edge, and the pointer always exists.

## Barrier screen
Not an existence mechanism (it explains the target, not its non-emptiness): B2/B3 untouched; T1-consistent (at squares no
word is isotropic). It sharpens (J)41/(J)46: the 4-specific input of five-slice ES is exactly this pigeonhole. Passing
through it reduces ES-five to SQ₅ ("some path lattice of det p is 2-adically isotropic"), which has no numerator in it and
does not imply 8/n (see z1_depth_bits).

## Cheap numerics
`scripts/z1_fano.py`: all 320 triples with letters 1..8 and n odd: pentagon classes always 5 distinct points; |iso ∩ pentagon| ∈ {1, 2}
when χ = −1; one non-pentagon point always has odd q.

## Assessment
PROVED, elementary, apparently new as an argument (the statement is MODEL_SPECIFIC Thm 3.1(a) / DEDEKIND Thm 4.5). It is the
cleanest available answer to "why 4": 4 is the modulus at which Q's isotropy test lives on L/2L, and 5 + 2 > 7 − 1 forces
the meeting. Promise as a route to ES: 1/5 (explains, does not create words). Value as steering: high.
