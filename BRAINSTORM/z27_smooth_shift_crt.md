# z27_smooth_shift_crt — GRH + smooth shifted primes would make every ℓ-part visible; the joint (CRT) law is still invisible (O256)

**Idea (violate "q − 1 has a large prime factor", the hypothesis of the indistinguishability Prop 2.2).** Restrict to windows
with (q−1)/2 M-powersmooth, M ≤ x^{1/(2k+2)}: every component Λ_q + ℓ^aℤ^S is a Frobenius class in ℚ(ζ_{ℓ^a}, S^{1/ℓ^a}) of degree
≤ M^{k+1}, so each component is GRH-equidistributed. Density cost ρ(2k) ≈ k^{−2k} = P^{−2+o(1)} — affordable (x = P^{O(1)}).
**Why it fails.** (1) (R-O256 repair 5: visibility vs distribution.) For a *given* q the components do determine the whole
vector (CRT reconstructs a(q) up to a global unit), so balance is determined; what is missing is *distribution*: balance is
decided by a character of composite order m = ∏ℓ^a (BALANCED_LATTICE §6), its pretentiousness is not a product of conditions
on the ℓ-components (the components of a short dual vector c/m are c·(m/ℓ^a)^{−1}/ℓ^a, not short), and the marginal Chebotarev
statements for each ℓ^a say nothing about the joint law; the joint law lives in the compositum, degree ≈ N^{k+1}. (2) Lower bounds
for smooth shifted primes with u → ∞ in progressions mod P ≈ x^{1/2} are not known, even under GRH (Baker–Harman 1998,
Lichtman 2022: fixed u ≈ 3.5, fixed shift).
**Barrier screen.** B6/visibility: the joint law across primes ℓ | N is the invisible object.
**Cheap numerics.** n/a.
**Assessment.** Dead (two independent gaps); recorded so the smooth-window idea is not re-run.
