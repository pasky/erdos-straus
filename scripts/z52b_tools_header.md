# z52b lane `tools` — reverse search from recent powerful tools ({{N}} items)

*Wave z52b, lane `tools` (slug `tools`). ES is OPEN. Breadth-first connection generation; only an obvious-nonsense
filter was applied (no barrier screening). Data: `data/z52b/tools.jsonl`; this file is regenerated from it by
`scripts/z52b_tools_build.py` (items live in `scripts/z52b_tools_items_*.py`).*

## Summary

**{{N}} items** from ~200 distinct tools/theorems (≈ 2015–2026 plus older anchors where the recent refinement is
the point), grouped in eight batches: (1) sieve/analytic NT; (2) additive & probabilistic combinatorics, polynomial
method, expansion/thin groups; (3) arithmetic/Diophantine geometry; (4) homogeneous dynamics, automorphic forms,
quadratic forms; (5) computation, AI/ML, formal methods, logic; (6) OAI-dump families (claimed), function fields,
anatomy; (7) group theory, Littlewood–Offord, circle method, misc; (8) second applications of the same tools to I3,
U(n), the pencil S_{n,k}, siblings, T1, pooling. The tag histogram is below the method section. Every arXiv id was
resolved on arxiv.org (two wrong ids, two placeholder ids, one wrong title and one misdescribed result were caught and fixed during the run).

**Ten items I find most exciting** (judgement, not graded):
1. **tools-0108** — U_n's projective closure *is* the Cayley 4-nodal cubic σ₃ = 0 (checked symbolically). The
   triangle at infinity passes through three of the nodes, whereas for Markoff k = 4 the triangle avoids them. This
   pins down the single geometric difference from Markoff. The fact itself was already in `cayley_markoff_cm.md`;
   the boundary-through-nodes framing is the new part.
2. **tools-0262 / 0303** — inverse Littlewood–Offord. Ratios ab⁻¹ with ab | N are signed subset products
   ∏ℓᵢ^{±1,0}, so the e-slice event becomes "a short signed walk in (ℤ/e)^× hits −1". This is a clean language for
   B2, and for I3 the group (ℤ/t)^× is tiny.
3. **tools-0224** — the Type II slices N_e = (p+e)/4 at fixed p are *consecutive integers*, so joint-anatomy
   theorems for consecutive integers are the natural genre (OAI 012 joint Dickman, Tao–Teräväinen sign patterns).
4. **tools-0141 / 0142** — negative Pell (Koymans–Pagano, CKMP) as the closest solved "−1 as a target" problem
   with 2-adic/Rédei obstructions.
5. **tools-0304 / 0062** — target-Davenport constants of small groups (ℤ/4C)^× and (ℤ/t)^×. These give
   finite combinatorial forcing lemmas ("enough prime factors in the right classes ⇒ −1"), cheap to compute.
6. **tools-0166** — class-divisor counts are linear combinations of weight-1 Eisenstein Fourier coefficients, so
   R(p) is a sum of automorphic coefficients along an AP (shifted-convolution and spectral tools apply).
7. **tools-0160 / 0101** — T1 viewed as a spinor-exception square class or as an HKRS-type reciprocity obstruction.
   Both theories have exact algebraic explanations of square-class failures.
8. **tools-0031 / 0032** — an Erdős–Hooley Δ and Ford H(x,y,2y) theory "for residue classes": this is the
   ES-native divisor-concentration function.
9. **tools-0028 / 0317 / 0258** — semi-linear sieve and Selberg–Delange give exact baseline densities for "no
   divisor ≡ −1 (mod m)" (for m = 4: all prime factors ≡ 1 mod 4). They are the cleanest per-slice failure
   probabilities.
10. **tools-0243** — large-q function-field ES via Bank–Bary-Soroker–Rosenzweig Chebotarev. This is a candidate
   *every-n* theorem in a sibling whose failure modes could be studied (check FUNCTIONFIELD_ES* first).

**Coverage notes.**
- Covered every tool named in the lane brief.
- Fargues–Scholze, condensed mathematics, perfectoid tilting and the BSD/modularity claims are recorded as honest
  low-value or null items, not dropped. The brief asks for no pre-judgement, and recording them prevents
  re-proposal.
- About 27 items draw on the local OAI dump; all are tagged `claimed`.
- 111 items carry a `seen:` pointer. Many tools were already touched by `BRAINSTORM/technique_transfer_list.md`,
  `z45_recent_pointwise_tools.md` and the z52 literature lanes.

**Not done.**
- No first steps were executed. Two exceptions: the Cayley-cubic identification was checked symbolically, and the
  I3 divisor identity (tu−1)(tv−1) = tn+1 was checked by hand.
- No barrier screening was done, by design.
- Not mined: the OAI dump's non-NT families beyond titles; Erdős-problems-site AI results individually; and
  physics/probability tools (SLE, spin glasses), which had no evident ES object.

## Method

Listed powerful tools/theorems/techniques of roughly 2015–2026 (plus a few older anchors where a recent refinement
is the point), and for each asked: what does it need, what is the most natural ES-side object it could act on, and
what is a cheap first step. Several items per tool are allowed.

ES-side objects used as targets (shorthand used in items):
* **Type I / Type II divisor events** — f | p² + 4c²d with f ≡ −p (mod 4cd); ff′ − 4c²dp = 1 with f ≡ f′ ≡ −1 (mod 4cd);
  more generally "a p-tied integer such as 4Cp+1 has a divisor ≡ −1 (mod 4C)" (B2: tied modulus).
* **e-slice** — ES(p) ⟺ ∃ e ≡ −p (4) with −1 ∈ Q = {ab⁻¹ mod e : ab | N}, N = (p+e)/4 or (pe+1)/4.
  Note: the Type II slices N_e = (p+e)/4 for e = e₀, e₀+4, … are *consecutive integers*.
* **counts** — f(p), R(p) with main term M_BM(p) ≍ log² p; the open lower tail R(p) ≥ ε·M_BM(p).
* **exceptional set** E(N) (Vaughan; repo N·exp(−c(log N)^{3/4})).
* **T1** — no Type I/II at odd squares (reciprocity obstruction); any mechanism must fail at squares.
* **U_n** — the affine cubic surface 4xyz = n(xy+yz+zx); Br U_n/Br ℚ ≅ ℤ/2, no BM obstruction (Bright–Loughran).
* **ES₅ / SL₂ words / CF length λ(p) ≤ 3**, **I3** (n = tuv − u − v), lattices L_ρ, quaternion orders, theta quotients.
* **siblings** — ES over 𝔽_q[T], ES_Q1 over ℤ[i], pencil S_{n,k}, 8/n, U(n).

Literature claims stated as facts were checked: every arXiv id in `refs` was resolved against arxiv.org
(`scripts/z52b_tools_verify_arxiv.py`, cache `data/z52b/tools_arxiv_titles.tsv`); non-arXiv references are standard
journal citations; uncertain leads are phrased as "check whether …" in `first_step`. OAI-dump items (local
`/home/pasky/projects/math/oai-math`) are tagged `claimed` — unrefereed machine-generated manuscripts.

`seen:<file>` tags come from a cheap `git grep -il <keyword>`; they point to prior discussion, not a dedup verdict.
