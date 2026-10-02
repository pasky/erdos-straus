# Hostile review: EXCEPTIONAL_TWIN.md §§0–5 (branch side-agent/twin-windows @ b708bd1)

Reviewer: side agent (worktree-0003). Scope: `EXCEPTIONAL_TWIN.md` §§0–5,
`reviews/agent-reports/AGENT_REPORT_O1.md`, `scripts/twin_*.py`,
`data/twin/`, as of commit b708bd1 (copied into this worktree). Context
read: ET Prop 2.4, Thm 2.5, Thm 2.7, Lemma 2.8, Lemma 2.9, Lemma 3.1,
Cor 3.6; EB §§1–2, Lemma 4.1–4.2.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects are numbered
T1, T2, … with severity (FATAL / HIGH / MEDIUM / LOW / COSMETIC).

## Summary table

(filled in at the end)

## Item reviews

### 1. Lemma 1.1 (forced classes are Jacobi non-residues) — SOUND

Re-derived. `gcd(A,4A−1)=1`; `D = sr² | A²` ⟺ `sr | A` (v_p check:
`1+2v_p(r) ≤ 2a_p` ⟺ `v_p(r) ≤ a_p−1` for p | s), so `M ≡ −1 (mod 4s)`.
`(−4D|M) = (−1|M)(s|M) = −(s|M)` (r coprime to M). For odd s:
`(s|M) = (M|s)(−1)^{(s−1)/2·(M−1)/2} = (−1|s)·(−1)^{(s−1)/2} = 1`. For
`s = 2s'`: `8 | M+1` so `(2|M)=1`. Correct, and classical (the Mordell /
Schinzel "squares are never covered" obstruction). Replay:
`twin_jacobi_check.py 20000` → `159390 classes checked, 0 with Jacobi != -1`
(matches the quoted count; script exits 1 on a counterexample).

### 2. Cor 1.2, Lemma 1.3 (QR base) — SOUND

Cor 1.2: `(n|M) = Π(n|p)^e = 1`. Lemma 1.3: (1) every W-smooth M divides
Q₀ and is odd, `c ∈ R_W` is a nonzero QR at each of its primes ⇒ Cor 1.2.
(2) the CRT factor at odd `p^e ∥ Q₀` has `p^{e−1}(p−1)/2` elements;
`Σ_{3≤p≤W} log(2p/(p−1)) = (π(W)−1)log 2 + log log W + O(1)`. (3) for
`1 ≤ e' ≤ e`, a class `a mod p^{e'}` has probability `p^{e−e'}/(p^{e−1}(p−1)/2)
= γ(p)/p^{e'}` or 0. Product structure ⇒ independence. Fine.

