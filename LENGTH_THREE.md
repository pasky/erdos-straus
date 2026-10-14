# LENGTH_THREE — one object behind every "length 3" (task O206, wave Y-c)

Status: in progress (O206). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on DEDEKIND_ES (DK, (J)9), HJ_DEEP ((J)15), MARKOFF_ES ((J)37), COMPOSITION_ES ((J)38), FIXED_MODULUS_SHOTS
((J)25), CHI_FLIP. Scripts `scripts/l3_*`.

Notation. A *word* is (c, m, s) ∈ ℤ³_{≥1}; K(c, m, s) = mcs − c − s (negative continuant); h := cm − 1,
h′ := ms − 1. For letters ≥ 2, N/h′ = [[c, m, s]] is an HJ fraction of length 3 (DK Lemma 1.1, with DK's
(v, t, u) = (c, m, s), A = h′, A* = h). Type II cube point (c, d, j) (FMS Lemma 1.1): h = 4cdj − 1 | pj + c,
s := (pj + c)/h.

## 0. Iteration log

(Y1) Searched for a common geometric carrier. First guess: the closed geodesic (Zagier cycle) of the cyclic word
(c, m, s). Killed: its trace is N − m, unrelated to the discriminant 4(μ² − n) of (J)37. Second guess: act with the
word matrix γ = M(c)M(m)M(s) on the (J)37 form [n, −2μ, 1]: no simplification (sympy). Third: the word is a
**Farey pentagon**, and its five continuants are the λ-lengths of the pentagon, i.e. the five cluster variables of
an A₂ cluster algebra with one frozen value N (§1). The other "length 3" statements are readings of this pentagon
at a CM point (Machin, §2) and along the orthogonal pencil of one geodesic (CF depth, §3).

## 1. The object: a Ford-decorated Farey pentagon = an A₂ frieze with one frozen value N (PROVED, elementary)

**Proposition 1.1.** Let c, m, s ≥ 1 and N = K(c, m, s). The vectors
`V₁ = (0, −1), V₂ = (1, 0), V₃ = (c, 1), V₄ = (h, m), V₅ = (N, h′)`
(cusps 0, ∞, c, c − 1/m, N/h′) satisfy |det(V_i, V_k)| =: λ_{ik} with
* sides λ₁₂ = λ₂₃ = λ₃₄ = λ₄₅ = 1, closing side λ₅₁ = N;
* diagonals λ₁₃ = c, λ₂₄ = m, λ₃₅ = s (the three letters), λ₁₄ = h, λ₂₅ = h′.
For letters ≥ 2 the four unit sides form the HJ path ∞ → c → h/m → N/h′ (DK §5.1). With Ford horocycles,
λ_{ik} are Penner λ-lengths, and the five Ptolemy relations of the pentagon are
`  cm = h + 1,   ms = h′ + 1,   hh′ = mN + 1,   hs = N + c,   ch′ = N + s.`   (P)
Conversely every positive integer solution (c, m, s, h, h′) of (P) is a word with N = K(c, m, s).
*Proof.* V_{i+1} = b_i V_i − V_{i−1} with (b) = (c, m, s), so consecutive determinants are 1 and
det(V_{i−1}, V_{i+1}) = b_i; the rest is expansion (e.g. det(V₃, V₅) = ch′ − N = s). Ptolemy = Plücker. The
converse: the first two relations define h, h′, and the third is then hh′ − mN − 1 = m(mcs − c − s − N), so N = K. ∎

(P) is the exchange pattern of the cluster algebra of type A₂ with frozen variables on the five sides of a pentagon
(cluster cycle c → h → m → h′ → s → c, exchange x_{k−1}x_{k+1} = x_k·(side) + (side)). So:
**a length-3 HJ word at N = a positive integral point of the A₂ cluster variety with frozen values (1, 1, 1, 1, N)
= a positive integral frieze of the pentagon with one non-unit boundary entry N.** The dihedral reflection fixing the
N-side is reversal (c ↔ s, h ↔ h′, m fixed).

**Corollary 1.2 (the five ES slices are the five cluster variables; PROVED, = DK Thm 4.5 restated).** For N ≡ 1 (4):
`  (h′/N) = −1  ⟺  one of the five cluster variables c, m, s, h, h′ is ≡ 0 (mod 4).`
DK Thm 4.5's five conditions 4 | tu−1, tv−1, t, u, v are exactly 4 | h′, h, m, s, c. Each gives an ES solution (DK
Cor 1.2, Thm 4.5). The symmetric formulation is new as a statement (content is DK's).
CERTIFIED (`scripts/l3_dict.py 20000`): all 610 533 words with N ≤ 2·10⁴: pentagon determinants, (P), and Cor 1.2
(139 915 "some variable ≡ 0 mod 4" words with N ≡ 1 mod 4), 0 failures; no such word at odd squares.

**Corollary 1.3 (the certificate cube is the pentagon with m = 4dj, N = pj; PROVED).** A Type II cube point (c, d, j)
is the word (c, 4dj, s) at N = pj (HJ_DEEP Prop 2.1 / FMS Lemma 1.1 rewritten), and FMS's three equivalent
divisibilities are Ptolemy relations of its pentagon: h | pj + c is hs = N + c; h | 4dj²p + 1 is hh′ = mN + 1; and
h | p + 4c²d with cofactor e = (c + s)/j follows from 4cd·(hs) = p(h + 1) + 4c²d. So the cube is the pentagon with
the middle diagonal ≡ 0 (mod 4) and the moving divisibility j | gcd(N/p, m/4) attached.
CERTIFIED (`l3_dict.py … 1000`): all 4 638 cube points of primes 5 ≤ p ≤ 1000, 0 failures.

Reading. The "3" of HJ length is the three short diagonals (c, m, s) of the pentagon; the cube's three coordinates are
(c, m/4j·…, N/p), i.e. two of the short diagonals plus the closing side.
