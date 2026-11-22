<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of lane z81-b2-duality (notes/z81/B2_DUALITY.md). The author is a GPT-6.2 Astra lane. Verify every theorem, Vieta/fibration/ping-pong calculation, falsifier screen (F1–F4), and scope claim. Reject any disguised B2 re-encoding or overclaiming. Cap any computational replay to ≤ 15 minutes.

Commit log:
commit 7d17b3bfd27259beb99973d26f4348fbdc8fa110
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 14:42:00 2026 +0100

    z81: constrain alternating returns, signed Cayley jumps and small-seed Lyness fibres

 data/z81/duality/chords.txt       |  16 ++
 data/z81/duality/cycles.txt       | 212 ++++++++++++++++++++++++++
 data/z81/duality/laws.txt         |  12 ++
 data/z81/duality/lyness.txt       |   2 +
 data/z81/duality/orbits.txt       |  92 ++++++++++++
 data/z81/duality/small_chords.txt | 302 ++++++++++++++++++++++++++++++++++++++
 data/z81/duality/walk.txt         | 136 +++++++++++++++++
 notes/z81/B2_DUALITY.md           |  96 ++++++++++++
 scripts/z81_dual_chords.py        |  64 ++++++++
 scripts/z81_dual_cycles.py        |  36 +++++
 scripts/z81_dual_laws.py          |  44 ++++++
 scripts/z81_dual_lyness.py        |  61 ++++++++
 scripts/z81_dual_orbits.py        |  41 ++++++
 scripts/z81_dual_walk.py          |  54 +++++++
 14 files changed, 1168 insertions(+)

Review:
## Hostile cross-lab review: `notes/z81/B2_DUALITY.md` (commit 7d17b3bfd, the only commit since main)

**Verdict: the note holds up. Accept with minor revisions.** I found no proof gap and no claim about ES. It does not disguise a B2 re-encoding: every section ends with a postmortem that names where the method fails. Its triage class BARRIER-SCOPED with STATUS delta none is right. One item, E, is a small positive theorem and should be routed somewhere (R5 below). The lane touched no master files, as required.

### Theorems: each checked by hand
- **A, the reciprocity two-cycle lemma: correct.** Both symbol chains check out: (q/p)=(−c/q)=(q/c) and (c/p)=(−q⁻¹/c)=(c/q), and their product is −1. The extension to composite levels via Jacobi symbols is valid, because c | pq+1 forces gcd(c,q)=1.
  - I checked it exhaustively over all n≡1 (mod 4) below 3000: 2357 two-cycles of unit levels, 0 with matching characters, 0 at odd squares.
  - At M=8 with n≡1 (mod 8): 143 two-cycles, 0 violations.
- **B, the trap at 183783601: correct.** The least nonresidue is 19 = (2/19), every divisor of 5r is 1 (mod 4), and the divisor classes {1,2,4,5,10} mod 19 are disjoint from their negatives. The Dickson admissibility argument is fine. The claim is honestly scoped: it is a dead first window, and the Y₁₉ start is untested.
- **The 2521 two-cycle census: correct.** I re-derived c(M²ab−p)=p²+Ma, the bound on a, q(M²ab−p)=Mbp+1, and the q-bound for the second method. Note that the 2521 result itself rests only on the first engine; the second engine only cross-checks small n. The note says this.
- **C (1), the squareclass chord law: correct.** It also recovers BRAINSTORM `graph_cayley_moves.md` A.1 on this chart, as a parity statement that now includes tangents. So "strengthens A.1" is justified.
- **C (2), the quaternion chord law: correct.** I checked each step:
  - the w-basis eigenvectors and their diag(V)-orthogonality;
  - the isometry with ⟨h, λⱼdᵢⱼ, λₖdᵢₖ⟩;
  - the even Clifford class (−ac,−bc);
  - the mixed terms collapsing to {Hⱼ,−1};
  - the Steinberg step {d,e}+{−de,f}=0;
  - the final match with C₀⟨H₁,H₂,H₃⟩.
- **The chord corollary: correct.** The Bright–Loughran citations are right: in the PDF, Lemma 3.1 is the real place, 3.5 covers ℓ∤2n, and 3.8 covers ℓ=2. I checked the evaluation claim empirically: at 409, 577, 2521 and 3361, every signed point has trivial α everywhere, and every positive point ramifies exactly at {p,∞}.
- **D, transverse weighted involutions: correct, but nearly tautological.** The generated group is just the projective torus action of S-units plus inversion and permutations. The `tag` canonicalisation is a valid test for that, and the census is really a check that the S-free parts of the coordinates match.
- **E, the torsion criterion: correct and the most valuable item.** I checked:
  - smoothness for N∉{0,1,9};
  - the 3-cycle as a fixed-point-free translation, and inversion as a 2-torsion translation;
  - H ≅ ℤ/6 being exactly the six boundary points;
  - the swap of y and z being negation;
  - Mazur giving index at most 2, so P is torsion iff 2P∈H iff P is fixed by some map Q↦T−Q;
  - the exclusion of geometric progressions and repeated entries.

  This upgrades the P3 item in BRAINSTORM `elliptic_fibration_es.md` from EVIDENCE to PROVED.
- **F, the sterile positive-rank fibre: the algebra is correct.** Sympy confirms both closed forms for s−B(3) and s−B(2p). A brute-force check at p=13, 17, 29, 37, 41 confirms that the largest positive solution sum is below s.
- **G, Lyness rigidity: correct.** I re-derived t·D=W(u+v−E−B) and D(At−W)=R=WL(u−E)(u−B), the cases u=E (seed or neighbour) and A=0, and the expansion giving ≪H⁸. The sharp example (A=1, D=1, n≍H⁹) checks out symbolically.

### Replay (about 12 minutes of compute, within the cap)
- **Reproduced byte-identically:** `cycles.txt`, `lyness.txt`, `laws.txt`, `chords.txt` (including 4545) and `orbits.txt`.
- **Spot-checked:** `small_chords.txt` for primes 1800–2000.
- **Independently checked:**
  - A separate brute-force point enumerator agrees on the point counts at 4/13, 4/17, 4/25, 4/49, 8/11 and 8/17.
  - The 4545 triple is collinear and on the surface, and its direction is all-positive, as the ∞ argument predicts.
  - The two-cycles listed in `walk.txt` at 6955940568721 and 8/1590284203561 satisfy both divisibilities and have opposite characters, consistent with A.
- **Not replayed:** the full `walk.txt` run (large factorisations).

### Required revisions
1. **F overclaims in two places.**
   - "even rational multiples of this generator … cannot cross to that oval" is false for division points: 2Q always lies in the identity component E⁰(ℝ), so a half of P could sit on the positive oval. The statement should be restricted to ⟨P⟩+H.
   - P is never shown to be a generator; it is only shown to have infinite order. Replace "generator" throughout.
2. **F's postmortem overreaches.** Sterility here is a pure size fact: s ≈ p⁴/16 exceeds the largest possible positive sum, which is below about p⁴/48. It shows that the fibre through this one signed point is the wrong fibre. It does not show that "rank is not the lift". Say so.
3. **E needs a priority caveat.** The torsion structure of (Σx)(Σ1/x)=N is very likely in Bremner–Guy–Nowakowski (1993). Cite it as probable prior work and mark a priority check as owed.
4. **D should be labelled for what it is.** State that it is tautological (diagonal S-unit action) and that its census is DATA, not a barrier.
5. **§0 block and routing.**
   - The Label line says PROVED only. It should also list the CERTIFIED parts (the 2521 cycles, the chord census, the orbits) and the CONDITIONAL infinitude in B.
   - Propose the FRONTIER §6 lines the orchestrator should add (A/B, C, D, G), merged by root cause.
   - Propose an erratum to `BRAINSTORM/elliptic_fibration_es.md` P3 recording the PROVED upgrade from E.
6. **Form.** The prose is too compressed, with opaque phrases such as "two-sector supply", "signed reflection at preserved level" and "group-to-divisor-box inference". The F1–F4 table cells cite data without file pointers. G should give an explicit constant (the script effectively uses u ≤ 8(H+1)) and state the u ≤ v convention.

### Falsifier screens (F1–F4)
The table is accurate wherever I could check it:
- **F1:** square-unit levels have no two-cycles; walks at 25, 49 and 121 find no hits; at 25 and 49 dyadic orbits link signed and positive points.
- **F2:** 8/11, 8/17, 8/131 and 8/241 have signed points only (2, 12, 22, 116); numerator-8 ratio windows hit at both large primes.
- **F3:** the 4545 chord exists.
- **F4:** all 15 inputs appear in `walk.txt`, and the prefixes quoted for 409, 2521 and 102001 match.

None of the screens is passed vacuously in a way that hides a claim.
</code-review>
