# z31 — Quadratic forms: ternary/quaternary representation, 290, xy + yz + zx (O261 field memo 3)

Labels as in DISCOVERIES.md. Excerpts: `sources/lit2026g/{borwein_choi, duke_schulzepillot, ono_sound, bhargava_hanke}.txt`
(research agent C; only Borwein–Choi's abstract and Duke 1988's Thm 1 were read verbatim — the others are metadata or
search extracts, so their statements below are marked (memory)). Builds on TWO_FIBRES.md ((J)48), THREE_SQUARES.md,
WINDMILL_REDUCTION Prop 10.3, LITERATURE_2026 §(iii).

## (a) Counterparts
1. **Ternary forms** (Duke–Schulze-Pillot, Invent. Math. 99 (1990); statement (memory)): every sufficiently large n that is
   primitively represented by the genus of a positive ternary Q and is not a spinor exception is represented by Q
   (ineffective). Exceptional sets genuinely exist (spinor exceptions; and anisotropic-prime square classes).
2. **Ramanujan's x² + y² + 10z²** (Ono–Soundararajan, Invent. Math. 130 (1997); (memory)): under GRH it represents every
   eligible odd n except 18 listed values. Unconditionally, finitely many further exceptions cannot be excluded effectively.
3. **290-theorem** (Bhargava–Hanke, Invent. Math. 2012 (preprint read only through a search extract)): a positive-definite
   integral form is universal iff it represents the 29 critical integers ≤ 290.
4. **xy + yz + zx = n in positive integers** (Borwein–Choi, Exp. Math. 9 (2000) 153–158, abstract read): "at most 19
   integers that are not of the form xy+yz+xz with x,y,z ≥ 1. Eighteen of them are small … The remaining possibility must be
   greater than 10^11 and cannot occur if we assume the Generalized Riemann Hypothesis."
5. **Binary forms represented by I₃ = x² + y² + z²** (classical; one-class genus): representability is a purely local
   question.

## (b) Mechanisms and sizes
* (1)–(3): r_Q(n) has an Eisenstein (genus) main term ≍ n^{1/2±ε} (ternary) or ≍ n (quaternary) and a cusp-form error;
  pointwise representation follows once the cusp part is beaten at the individual n: Iwaniec/Duke bounds for half-integral
  weight coefficients (ternary; Siegel ⇒ ineffective) or Deligne (quaternary). **Power main term.**
* (4): n + z² = (x + z)(y + z): solutions ↔ forms of discriminant −4n with a non-degenerate representation; failure means an
  idoneal-type condition on the class group; Siegel's ineffective lower bound for h(−4n) leaves ≤ 1 unknown exception, GRH
  removes it. Count ≍ class number ≍ n^{1/2±ε}. **Power main term, class-number mechanism.**
* (5): one class in the genus ⇒ local ⇒ global (Siegel–Minkowski). No size input at all.

## (c) Relation to B2
* **(5) is an INSTANCE — but of the sign layer only.** (J)48 (TWO_FIBRES, PROVED): ES-five(p) ⟺ some path binary
  [[tv−1, 1], [1, tu−1]] (det tp) attached to X_p is NOT represented by I₃; T1 ⟺ every odd-square path lattice embeds in ℤ³.
  The representation question is solved (one-class genus ⇒ purely local, decided by the 2-adic/p-adic invariants, i.e. the
  quadratic character ψ(A)). What remains is the *supply* of path binaries, which is (E1)/(★): the B2 divisor event.
  This is the cleanest instance of F6: the quadratic-form world solves exactly the part of ES that is already easy.
* **(4) is the closest ANALOGUE in shape** (a symmetric 3-variable equation in positive integers with a parameter, "all
  n except finitely many"): ES's U_n is the cubic 4xyz = n(xy + yz + zx), Borwein–Choi's is the quadric xy + yz + zx = n.
  Its mechanism is the class number h(−4n) ≍ n^{1/2±ε} (F2 fails: power count) and a group-theoretic failure criterion. For
  ES the campaign PROVED that failure is *not* a subgroup condition on Cl(−4p) (LITERATURE_2026 §(iii): at 2521 the principal
  genus is sterile while a non-principal genus is productive; at 193 a class fails while its square succeeds) and
  WINDMILL_REDUCTION Prop 10.3: form-class/Bhargava-cube mechanisms see the ES residue condition only through its genus
  shadow. Blocked by F2 + F6.
* **(1)–(3)**: blocked by F2 (Eisenstein main term is a power; the ES "Eisenstein part" is ≍ (log p)², and STRONG_APPROX_ES
  Thm 9.1 (PROVED): no finite fixed-level Eisenstein-type identity can certify Type I/II counts, by T1) and by the absence of a
  fixed form (F3: the ES lattice L_ρ(g) moves with the slice g; ASTRA_BRIDGE Thm 3.4).
  Note the parallel the brief points to: ternary forms *do* have exceptional sets (spinor exceptions = square classes, local-
  ish), and ES's only exceptional-type set, the odd squares for Type I/II shapes (T1), is likewise a square class. The
  difference is F4: for ES itself the squares are not exceptions (other shapes cover them).

## (d) Verdicts
(5) INSTANCE (sign layer only; already in (J)48); (4) ANALOGUE (shape), mechanism blocked by F2/F6; (1)–(3) ANALOGUE, blocked by
F2/F3. No transfer: **NOT SHARP**.
