# z31 — Integral Hasse principle on affine cubic / log K3 surfaces; sums of three cubes; homogeneous spaces (O261 field memo 6)

Labels as in DISCOVERIES.md. Read by me: CTW abstract (`sources/lit2026g/ctw_cubes.txt`), Heath-Brown's conjecture as stated
by Booker–Sutherland (`hb_cubes.txt`); Harpaz Thm 1.0.1 (research agent B, `harpaz_logk3.txt`); BL Thms 1.1, 1.6 (agent B) and
LITERATURE_2026 (BL Thm 1.8/1.9, Lemma 3.10). Builds on LITERATURE_2026 §(iv), LITERATURE_AUTOMORPHIC, STRONG_APPROX_ES.md.

## (a) Counterparts
* **ES itself (E6):** U_n : 4xyz = n(xy + yz + zx), positive octant. BL: Br U_n/Br ℚ ≅ ℤ/2 (Thm 1.6), no BM obstruction to
  natural-number solutions (Thm 1.1/1.8), BM does not control strong approximation (Thm 1.9). U_n(ℤ) off the lines is finite
  (Lemma 3.10).
* **Sums of three cubes** X_k : x³ + y³ + z³ = k. Colliot-Thélène–Wittenberg (arXiv:0911.3539, Amer. J. Math. 134 (2012)),
  abstract: "If a is not congruent to 4 or 5 modulo 9 then there is no Brauer-Manin obstruction to the existence of integers
  x, y, z such that x³+y³+z³=a" (same for x³ + y³ + 2z³ = a). Heath-Brown 1992 (as stated by Booker–Sutherland,
  arXiv:2007.01209, p. 5): #solutions with max |x_i| ≤ B ~ ρ_sol · log B.
* **Conic log K3 surfaces:** Harpaz (JEMS 21 (2019), arXiv:1511.04876) Thm 1.0.1: S-integral points on a family of conic
  log K3 surfaces under an independence hypothesis on seven square classes, via fibration + 2-descent + Green–Tao–Ziegler.
* **Homogeneous spaces of simply connected semisimple groups** (Colliot-Thélène–Xu, Compositio 2009; agent B: UNVERIFIED
  theorem number): integral points exist iff there is no BM obstruction (strong approximation) — the main *pointwise* integral
  Hasse mechanism in arithmetic geometry. Example: representations by ternary/quaternary forms (z31_quadratic_forms).

## (b) Pointwise status
* Sums of three cubes: **OPEN for every individual k** beyond computation (Booker 33, Booker–Sutherland 42 and 3 —
  agent B; computational). The fingerprint matches ES unusually well: one parameter k (F1), conjecturally only
  ρ log B solutions up to height B (F2: polylog), no local obstruction for k ≢ ±4 (9) (F4), no BM obstruction (CTW) though the
  Brauer group is non-trivial in general. Difference: X_k is expected to have infinitely many points of unbounded height
  (smallest solutions astronomically large, e.g. 42), while U_p has finitely many, all of height O(p²) (BL Lemma 3.10;
  (J)25: ES is a finite search). So ES is "three cubes with a box".
* Homogeneous spaces: PROVED (strong approximation, power-size counts from Siegel mass / Hardy–Littlewood).
* Conic log K3 (Harpaz): CONDITIONAL-type statements for families, via additive-combinatorial inputs (GTZ) on *linear forms with
  bounded coefficients*.
* Markoff-type: almost all k, not all (z31_markoff_chen).

## (c) Transfer to B2
* **Strong approximation for groups: blocked by geometry.** U_n is not a homogeneous space of a simply connected semisimple
  group; its automorphism group is finite; no group acts transitively on integral points (thin_group_orbits §3). Strong
  approximation for the conic-bundle structure fails because BM does not control it (BL Thm 1.9).
* **Harpaz/GTZ: blocked by F1/F3.** GTZ inputs need linear forms whose coefficients are bounded independently of the box;
  at a single p, p is both a coefficient and the box size (LITERATURE_2026 §(iv), Assessment). Fibration methods produce
  points *in some fibre*, i.e. some n, not a prescribed one.
* **Three cubes: no mechanism to transfer** — it is the same open frontier. The precise lesson: "log K3 + no BM obstruction
  + polylog expected count" is the regime where *no* pointwise existence theorem is known for any non-homogeneous family
  (agent B found none; LITERATURE_AUTOMORPHIC likewise). The campaign's B2 is the ES face of this frontier.

## (d) Verdicts
ES ⊂ "integral Hasse principle for log K3 families": **INSTANCE** (E6 is literally such a problem; BL places it there).
Sums of three cubes: **ANALOGUE (closest sister: F1, F2, F4 matched; ES additionally finite)** — open, no mechanism.
Homogeneous spaces/strong approximation: ANALOGUE, blocked (not homogeneous). Harpaz: ANALOGUE, blocked by F1/F3.
Transfer: **NOT SHARP.** Recommendation: describe B2 externally as "the bounded-height integral Hasse principle on the
Erdős–Straus log K3 fibre" — the community's name for the problem class, in which no pointwise mechanism exists.
