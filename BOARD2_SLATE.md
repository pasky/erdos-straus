# BOARD2_SLATE — O273: the board #2 compatible slate

Source: board memo `/home/pasky/.pi/boards/20261018-es-lowertail/memo.md` (finalists 1–4) and the items/rounds/rulings it
cites. None of these items is single-prime lower-tail progress (the board's unanimous bottom line); this file records the
cheap, compatible results with honest labels. ES is not solved.

## (1) Finalist 4 — ABH attribution for λ(p) (DONE; KNOWN)

* Read ABH arXiv:2210.14095v2 myself: Thm 1 (concentration of S(a/N) at (12/π²) log N log log N, window t log N,
  proportion ≪ 1/t, single fixed N), Thm 6 (|D(a/N)| ≥ t log N with proportion ≪ 1/t), identity (5)
  D = −S_alt/12 + O(1) (Barkan/Hickerson). Conventions: a/N = [0; a₁, …, a_r], a_r > 1 — same as ZAREMBA_TRANSFER's c_i.
* Transfer re-derived: Σ_{j even} c_j = (S + S_alt)/2 ≤ (6/π²) L log L + O(L) off a set of proportion < 1/2, which
  therefore contains a QNR; with r(p/A) ≤ 1 + Σ_{j even} c_j(A/p) this gives **λ(p) ≤ (6/π²) log p log log p + O(log p)**.
  Status: **KNOWN (corollary of ABH 2022)**; the campaign's Theorem A (constant 10) is a weaker special case.
* Numerics (EVIDENCE, `scripts/z42_abh_check.py`): the HJ formula holds as r = 1 + Σ_even − δ, δ ∈ {0, 1};
  |S_alt + 12D| ≤ 3; median r over QNR tracks (6/π²)L log L + O(L).
* Argon's "convergent Legendre invariant" (a/p) = ((−1)^i q_iρ_i/p): a one-line consequence of the standard convergent
  congruence; same genus-character fact as DEDEKIND_ES Thm 4.5. Recorded, **not new**.
* Written into `ZAREMBA_TRANSFER.md` §2 directly after Theorem A (existing text kept).

## (2) Finalist 1 — moving-window cap-0 witness corollary (DONE; FORCED_WINDOW §8)

* **Theorem 8.5 (PROVED modulo Henriot 2014 erratum New Thm 5 + Siegel–Walfisz + Mertens; ineffective).** For 0 < α < 1/6,
  all but O(X/L^{4/3−2α−ε}) primes p ≡ 1 (8) in (X, 2X] have Σ_{χ≠1}|A_χ(K_q)| < 1, hence an honest Type II solution
  with window q, at **every** prime q ≡ 3 (8) in [L^α, 2L^α] (forcedness is not needed — the certificate is target-free).
* Henriot's statement was checked from the source: the 2014 erratum (now `sources/henriot-erratum-2014.pdf`) is read, and
  New Theorem 5 is applied with Q₁ = t, Q₂ = 4t − q, F = f(n₁)·1[P⁻(n₂) > √x] ∈ M₂(1, 1, ε); local factors computed exactly.
* Value: dominated (fixed q = 3 alone gives ≪ X/L^{3/2} exceptions; Vaughan; 3/4 chain). New only in shape. Priority:
  nothing found in a limited search (Elsholtz–Tao Thm 1.8 is the fixed-window analogue).
* EVIDENCE: `scripts/z42_window_cert.py`, 990 windows at p ≈ 10⁶: certificate ⇒ explicit solution, 0 violations.
