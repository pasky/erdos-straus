# z52b lane `tools` — reverse search from recent powerful tools ({{N}} items)

*Wave z52b, lane `tools` (slug `tools`). ES is OPEN. Breadth-first connection generation; only an obvious-nonsense
filter was applied (no barrier screening). Data: `data/z52b/tools.jsonl`; this file is regenerated from it by
`scripts/z52b_tools_build.py` (items live in `scripts/z52b_tools_items_*.py`).*

(Summary will be written at the end.)

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
