<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="182173b8a">
A separate reviewer subagent was asked to review the changes in `git log 182173b8a..`. Its request and review follow.

Request: review changes since 182173b8a carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Focused hostile Claude Opus cross-lab review of z81-cap-zero Round 2 §§5–7, notes/z81/CAP_ZERO.md (commit 518e2a6cc). Highest priority Theorem V new unconditional 4/5 cap-one and 3/4 log-gain prime-root exceptional bounds: verify CRT fibre, denominator/gcd, BV double incidence/Shiu, harmonic masses and transfer. Check CTS/HC signs/height and Dickson N. Return concise exact verdict and required fixes. Do NOT write/commit files; parent saves your returned text. If replaying Python use ulimit -v 6000000; timeout 160 uv run --offline --no-project python -B, ≤2 processes. No external priority claim.

Commit log:
commit 518e2a6cc9e8170c17cc767d6b3fac8546055efe
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 16:30:35 2026 +0100

    Prove quartic cap-one supply and single-prime logarithmic gain; test cubic cyclotomic and neighboring windows

 data/z81/cap_zero/round2.txt |  2 ++
 notes/z81/CAP_ZERO.md        | 74 ++++++++++++++++++++++++++++++++++++++++++--
 scripts/z81_cap_quartic.py   | 57 ++++++++++++++++++++++++++++++++++
 3 files changed, 130 insertions(+), 3 deletions(-)

Review:
**Verdict: ACCEPT WITH FIXES.** I found no mathematical error in §§5–7. All required fixes are to form (§0 metadata, labels and the replay script). The one substantive suggestion is optional.

## Theorem V (4/5 at cap one; L^{3/4}(log L)^{1/4} for root 1 or prime) — ACCEPT

- **Packet.** With f = 4arvw − 1 we have nv + S + ar³ = fS + S = 4arvwS. So 1/x + 1/y + 1/z = 4/n exactly. The coprimality conditions (r, nvw) = 1 and (r, S) = 1 (from fS ≡ nv mod l for each prime l | r) give a reduced denominator of z exactly r². Also x, y are integers, r | y, and r is odd. This meets the STATUS cap-1 definition with e = 1.
- **Distinctness and the CRT fibre.**
  - ar³v′ < x^{.126} < ℓ, so two atoms with the same residue mod ℓ satisfy ar³v′ = a′r′³v. Since a and r are squarefree and coprime, this fixes (a, r, v), because the valuations are in {0, 1, 3}.
  - 4arv > K₀ then fixes k.
  - So at each ℓ at most one atom is hit, and Z is a sum of independent per-ℓ Bernoullis.
- **Unit fibres.** A failing n has no prime factor in G (integral solutions scale), and k, r are G-supported. So c is a unit mod every k, r is coprime to k and v, and the WILD_ES §3 unit repair is legitimate. This sidesteps TQ's void lemma and selector, and that substitution is sound.
- **Denominator and gcd.** For a d | r, kℓ ≡ −1 mod q₀d is a reduced class. Since d | q₀, φ(q₀d) = dφ(q₀), so the loss is at most Σ1/l ≤ 1/4.
- **BV double incidence.**
  - W² ≤ τ⁴ΣI² by Cauchy over representations, and BT gives E* ≪ x/φ(q).
  - Expanding I² gives one condition modulo b = [k, k′] ≤ K₀², and a then lies in one reduced class mod b.
  - Shiu's level condition b < A^{1−α} holds amply. Σ_{k,k′} 1/φ([k, k′]) ≪ t³ log t ≤ t⁴.
  - Cauchy against BV at q < x^{.13} then gives the error O(x t^{−A}).
- **Harmonic masses.**
  - Lower bound: k mass ≍ t (positive density via Euler product, then Markov). r mass ≍ t (squarefree row) or ≍ log t (prime row). v mass ≍ t. a mass ≍ t/k (Möbius over h² | a, error √A·τ(2rv) = o(A/k)).
  - Upper bound by BT gives μ_c ≍ t³R_t. Balancing tM ≍ L gives t = L^{1/5} or (L/log L)^{1/4}, matching both stated exponents.
- **Transfer.** (1/2)^Z has an even-degree Taylor majorant. E2^{−Z} ≤ e^{−μ/2}, and the remainder is ≤ 2^{−D−1}μ^{D+1}/(D+1)!. The boundary cost is exp(O(tD)). All of this is correct.

Required fixes:
1. **Label.** Add the internal z79 `WILD_ES.md` §3 unit repair to V's dependency list. The "TQ transfer" dependency is only the generic CRT/Bonferroni count, and V restates it, so the TQ dependency can be dropped or narrowed.
2. **Squarefree-row removal bound.** The "+1/√Z … Markov in the last case" term is wrong. The Markov term is ≤ 4Σ_{l>B}1/l², already inside Σ_{j>B}1/j². There is no 1/√Z term.
3. **Independence wording.** State the independence precisely, as in TQ Lemma 2.2: independent per-ℓ indicators, each with mass (number of active atoms at ℓ)/ℓ. It is not literally independence over atoms.

## §6: cyclotomic ternary spread (CTS), the horizontal hypothesis (HC) and the h = 3 height cutoff — ACCEPT (labels correct)

- **Signs.**
  - Since s ≡ 1 mod 4 and h is odd, η_s(t) = (−1/t) for every odd t | s^h + 1. I checked this, and the script also asserts it.
  - u = (s+1)/2 ≡ 3 mod 4 and η(u) = (2/s) = −1 when s ≡ 5 mod 8.
  - η(−p) = (p/s) = −1, so −p/u is a quadratic residue.
  - The Φ₆ toggle in exponent 3h is a separate cyclotomic block because 3 ∤ h. p ∤ s^{3h} + 1 because v₂(ord_p s) ≥ 3.
- **h = 3 cutoff.** m·(p²f + 2p + m) = (p+m)² + p²s³, so the quantity c is an integer. In the second case m | p³ + k³; in the first, f | j³ + 1. All three cases check, giving s ≪ p⁶.
- **HC.**
  - The characters 1 and η both contribute the main term 2/(s−1), since both ab and −p lie in the nonresidue coset.
  - The bound m ≤ (s+1)p^{.03}/2 < s² − p gives s ∥ K, so the root is exactly s.
  - Under GRH the coefficient ℓ¹ norm is O(1), the main term S/(φ(d)b log S) beats √S because db ≤ p^{.06}, and M ≫ log p.
  - The scaling to e*(n) = O(1) via the largest prime factor (s > p, so s ∤ n) is correct.
- **Optional substantive suggestion.** Since a ≡ (2d)^{−1} mod s, a hit is equivalent to s | b + 2dp. That means js = b + 2dp with j ≲ d, and b | (2dp)² − 2dp·j + j². So HC is really a prime count over triples (d, j, b) of Bateman–Horn/divisor-correlation type. Stating it this way makes it directly computable (for a numerical calibration) and shows how hard it is. It is clearer than the bilinear-character phrasing.

## §7 Theorem N (conditional on Dickson) — ACCEPT, replayed

- I checked the algebra: bm = 9p + 4, 4x = p + m, m ≡ 11 mod 12, and 9(x+3j) ≡ −(1+3bj) mod m_j.
- Clearing denominators is valid, since only the direction "m_j divides the cleared numerator" is used.
- All three sign cases hold: j < 0 gives a positive product; j > 0 forces δ_p + δ_T = 0 at l_j; for j = 0, v₃ has size 2 or 3 against at most 1 from w₀.
- Admissibility holds: at primes l | b, p ≡ −1/B mod l, which is nonzero.
- I ran an independent replay (/tmp, not committed) at J = 1. It found 3 instances, e.g. b = 3365891, p = 3189177846574333650961, x = 797296593515992469436 at t = 5170. Each has the root-3 S packet at x, and an exhaustive search over divisors of (p(x+3j))² finds no integral completion at x − 3, x, x + 3. At J = 2 there were no simultaneous prime instances within the search range, which is expected.

## Form fixes (required)
- **§0 Scope line:** add V (all n ≤ N, an exceptional count, ineffective), N (conditional on Dickson) and HC/CTS (conditional).
- **§0 Review line:** mark §§5–7 as "cross-review owed" until this review is filed.
- **STATUS delta:** add "cross-review owed / priority unverified" for V.
- **CAP_INTERPOLATION table:** upgrading the e = 1 entry in its multiplier row from Assessment to PROVED belongs to the wave export, not this lane.
- **Replay script:** in `round2.txt` the second field is 0, meaning no composite r was tested inside the collision-safe box. The "multisupport example" output label suggests otherwise; reword it. The script also does not test N; consider adding a Dickson-instance replay like the one above.

My Python replays used `ulimit -v 6000000`, timeout 160 s, with at most 2 processes. No external priority claim is made.
</code-review>
