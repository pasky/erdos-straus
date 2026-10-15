# z9_depth_walks — a pentagon vector of 2-depth k is a non-backtracking walk of k − 1 half-steps in G_p; 8/p is an X₀(4) problem (O233, goal 2)

## Idea
O224 (Assessment) guessed that depth-k pentagon vectors "point at vertices at distance k − 2 beyond the Eichler edge".
Make this exact, globally in G_p and not only on the 2-adic tree, then read the 8/p bit correlation from it.

**Lemma 1 (PROVED, elementary; the walk is *conic-marked*, review repair).** Let L be a positive classical ternary lattice of odd determinant with L ⊗ ℤ₂ isotropic
(an edge of the 2-isogeny graph). Let x ∈ L be primitive with v₂(Q(x)) = k ≥ 2. Define alternately:
* L₁ = L;
* F_j = L_j + ℤ·x/2^j (a vertex lattice: Q-integral, half-integral bilinear form);
* L_{j+1} = the unique classical index-2 sublattice of F_j that contains x/2^j.

Continue while defined: F_j needs Q(x/2^{j−1}) ≡ 0 (mod 4), and L_{j+1} needs Q(x/2^j) even (the *conic marking*: x/2^j is a
point of the conic of F_j). Without the marking a unique classical continuation through x/2^j exists whenever x/2^j 
mod 2F_j is not the radical r. Example (reviewer): p = 5, w = (1, 3, 4), x = e_1:
Q(x) = 4 and Q(x/2) = 1 is odd, yet F_1 has a classical sublattice through x/2 other than L_1. So the step count below is a property of the marked walk, not of
the existence of a continuation. Then:
(a) every step is well defined and x/2^{j−1} is primitive in L_j and in F_{j−1};
(b) the walk L₁, F₁, L₂, F₂, … is non-backtracking (L_{j+1} ≠ L_j, F_{j+1} ≠ F_j);
(c) it has exactly k − 1 steps after L₁ (a step is edge → vertex or vertex → edge). For even k it ends at the vertex
F_{k/2}, reached after k/2 − 1 further edges along the walk (walk length, not graph distance in G_p: the quotient
has cycles). For odd k it ends with the edge L_{(k+1)/2}.

Since all lattices are global and the edges are classes of 𝔊⁻_p (CONSTRUCTIVE_ES Thm 2.1), this is a walk in G_p itself. In
quaternion terms (Assessment, not proved here) the walk should be the chain of Eichler and maximal orders along which the
pentagon element ε_x ∈ E⁰ (nrd ε_x = p·Q(x)) stays divisible by 2^j.
*Proof.* Edge → vertex: x/2^{j−1} =: z ∈ L_j is primitive with Q(z) ≡ 0 (4). So L_j + ℤz/2 is one of the two maximal
overlattices (CONSTRUCTIVE_ES Thm 1.2(b)), i.e. an endpoint of the edge. Vertex → edge: in F = F_j, with z′ = z/2 and Q(z′) even,
z̄′ ∈ F/2F is a nonzero point of the conic {q = 0}. It is nonzero because z/4 ∉ F_j: F_j = L_j + ℤz/2, and z/4 = l + mz/2
would give (1 − 2m)z/4 ∈ L_j, against primitivity. It is not the radical r, because q(r) = 1. The classical index-2
sublattices are the 3 hyperplanes through r (the polar form b = 2B mod 2 has rank 2 with radical r, and B is integral on a
hyperplane H iff b|H = 0 iff r ∈ H). Exactly one of them contains z̄′. Non-backtracking: z′ ∉ L_j (z primitive in L_j),
so L_{j+1} ≠ L_j; and z′/2 ∉ F_j (as above), so F_{j+1} = L_{j+1} + ℤz′/2 ≠ F_j. Primitivity of z′ in L_{j+1}: z′/2 ∉ F_j ⊃ L_{j+1}.
Counting: Q(x/2^j) = 2^{k−2j}·odd. The edge → vertex step from L_j needs k − 2(j − 1) ≥ 2. The vertex → edge step from F_j
needs k − 2j ≥ 1. Both stop exactly after k − 1 steps in total. ∎
CERTIFIED in coordinates (`scripts/z9_depth_walk.py 200`): all 1190 pentagon pointers (4 | entry) of all χ = −1 words of all
odd primes 5 ≤ p ≤ 200 (R234 repair: not only p ≡ 1 (4); R234 re-certified with independent code). (R234 remark: for primitive x
with 4 | Q(x), x/2 ≡ r would force B(x, L) ⊂ 2ℤ, i.e. x ∈ 2L at 2; so without the marking every pointer has a unique continuation,
checked on all 720 depth-2 pointers p ≤ 200 — the marking is the whole content of the step count.) The walk built explicitly by HNF over 2^{−12}ℤ has exactly k − 1 steps, never backtracks, and x/2^j stays primitive; 0
mismatches.

**Corollary 2 (8/p as a level-4 problem; PROVED from Lemma 1 + MODEL_SPECIFIC Lemma 3.0 / Thm 3.1).** A word is in S₈ iff it
has a pentagon vector whose *conic-marked* walk has ≥ 2 steps, i.e. x/2 is a conic point of the pointed endpoint F₁
(Q(x/2) even). Then the marked continuation L₂ ≠ L₁ is the edge at F₁ belonging to that conic point, and L₁ ∪ L₂ is a cyclic
4-isogeny (a point of X₀(4)). So **an 8/p five-slice certificate = a path-shaped 2-edge + a pointer whose half-vector is a
conic point at the pointed endpoint**. The marking is essential: the bare existence of a continuation edge through x/2 is
not enough (example above, a word not in S₈). 2^k/p asks for a marked walk of k − 1 half-steps. This makes
O224's Assessment precise. The distance "k − 2" is measured in half-steps beyond F₁.

**Proposition 3 (where the bits are correlated; PROVED, elementary).** Use the parity patterns of O224 Lemma 1.1.
(i) t even: the two even entries are t and u (or v). The depth of e₂ is v₂(t), a function of the letter alone, shared by
all words with the same t.
(ii) t, u, v odd: the even entries are A and A*, with v₂(A) + v₂(A*) = v₂(tp + 1) =: s and both ≥ 1. If both are
≥ 2, the two pointers point at **opposite** endpoints (two distinct isotropic classes, Lemma 1.1). Their walks then run in
opposite directions, with total length s − 2 half-steps beyond the edge. In particular **max(v₂A,
v₂A*) ≥ 3 ⟹ s ≥ 4**, and for s = 4 only the lopsided split (1, 3) or (3, 1) works.
(iii) t odd, u even: the even entries are u and A* (v₂(u) is a letter, v₂(A*) = v₂(tv − 1)).
So the bit of a word is *constrained* by v₂ of a letter or by s = v₂(tp + 1), which depends only on (t, p) mod 2^s. It is not
determined by them (review repair). At p = 293, t = 3 (s = 4) the all-odd words (3, 37, 3) and (3, 7, 15) have splits
(1, 3) ∈ S₈ and (2, 2) ∉ S₈. At p = 97, t = 2, (2, 7, 8) ∈ S₈ while (2, 20, 3) ∉ S₈, because the other even letter decides. At p = 131
(≡ 3 mod 8) the odd t = 1, 3, 5, 7, 9, 11, 13 give s = 2, 1, 4, 1, 2, 1, 3. Among them only t = 5 has s ≥ 4, and its
all-odd word (5, 1, 33) has the split (2, 2) (O224 §1.3). The necessary condition (s ≥ 4 in the all-odd pattern) is shared by all words with the same t. This is a qualitative
source of the correlation behind O224's 12-vs-0.82 excess of S₈-empty primes. A quantitative explanation is not claimed.

## Literature
Serre, *Trees* (Bruhat–Tits tree of SL₂(ℚ₂), stable lattices of an element); Eichler orders of level 2^k ⟷ non-backtracking
paths of length k; Kohel (1996); for the global reading, CONSTRUCTIVE_ES Thm 1.2, 2.1.

## Barrier screen
This is a structural explanation of a negative phenomenon (8/p fails at 131, 241, …). It does not attack SQ₅. B2: the
extra 2-adic bit is a congruence on t, i.e. a fixed residue slice on the modulus that is part of the solution. T1: unchanged
(at m² there is no edge to start a walk).

## Cheap numerics
`scripts/z9_depth_walk.py 200` (CERTIFIED check of Lemma 1, above).

## Assessment
PROVED: Lemma 1, Cor 2, Prop 3. They turn O224's tree-depth Assessment into a theorem: a depth is the length of a conic-marked walk in G_p, and
8/p is the X₀(4) refinement of the edge problem. They also show that v₂ of a letter and v₂(tp + 1) constrain (but do not determine) the bit. No existence
mechanism. Promise 1/5 (explanatory value for 8/p; it would be useful if anyone attacks 8/p separately).
