# AGENT REPORT O13 — inverse-square problem behind HC(a,B)

Branch `side-agent/omega-inverse-squares`. Deliverable `POINTWISE_OMEGA5.md`,
`scripts/omega5_codeg.py`, `data/omega5/`, literature notes and PDFs in
`sources/lit2026/` (`O13_LITERATURE_NOTES.md`). One self-review (deep
reviewer) was run; its defects D1–D9 were applied in commit aa45856 and
later.

## Results

1. **The core obstruction of O4 §7.3/§7.5 is an artefact (PROVED, §1).**
   HC sums over *atoms*. Atoms have squarefree s (O3 Lemma 2.1 bijection),
   and `(s,t)↦st²` is injective, so
   `#{s≤Y squarefree, t≤t_0 : st²≡w (q)} ≤ Yt_0²/q+1` for every w.
   O4's problem IS counted non-squarefree `s_t`. That over-counts each atom
   and is genuinely beyond Weil, but HC never needed it.
2. **Theorem 2.3 (PROVED).** The m=1 part (trivial Π-part) of every non-hub
   codegree is `≤C𝓛⁴4^{k/3}H^{−1/3}`, using only elementary tools:
   lifting on the planes (C1)/(C2) and on rays, square-root counts, and a
   thin-box lattice lemma. The reviewer checked every case and constant.
3. **HC as literally stated in O4 is false (PROVED counterexample, Def 2.0;
   found by the reviewer).** A non-hub lift mod `ℓ²` of the hub class −1
   inherits codegree `≫1` (O2 §10.3 lifting). Repair: *saturated hubs*
   (a vertex is a hub if some reduction mod `ℓ^v` is). The quarantine cost
   grows by a factor `e_ℓ≤k+1`, which O4 Thm 4.2 absorbs. **The parent
   should log this against O4 §4.2.**
4. **The Π-part m (O4 gap (iii)).** Proved: `m|u+v`, `m|4sa²+1`, and the
   m-system reduction (Lemma 3.1); `m≤H^{1/6}` gives HC* with a=1/6
   (Prop 3.2); ray sums with m for balanced rays (Lemma 3.3). **Open:**
   the large-m part HC_Π. It is a divisor-function problem in short
   progressions: (DIV) for unbalanced rays, and averages of
   `τ_Π(4sa²+1)` over (s,a) with `4sa²≡κ (q)`. Pointwise divisor bounds
   (`T^{O(1/log𝓛)}`) are fatal against `H^{−a}=e^{−c𝓛^{2/3}}`.
5. **Cor 4.1 (PROVED implication).** HC_Π implies HC*, a restricted form of
   HC: saturated hubs, `4^k≤H≤y`, an extra factor `e^{Ck}`. HC* suffices for
   O4 Thm 4.2. So HC_Π implies `log W(p)≥0.08(log₂p)^{3/2}` i.o., modulo
   Thorner–Zaman and Elsholtz–Tao. **HC is not proved; the proved rate
   stays O4 Cor 3.1.**
6. **Literature (§5).** I checked Cilleruelo–Garaev, Bourgain–Garaev ×2,
   Shparlinski's survey and Shparlinski's arXiv:1004.0715 against the PDFs.
   None gives IS pointwise in O4's range. Prime-modulus translated-box
   results are the best available, and Fourier asymptotics are trivial for
   `XY<q^{3/2}`. The squarefree lifting makes IS unnecessary.
7. **EVIDENCE.** Exact pair codegrees (T=10⁹, 10¹¹ near-y pairs; 10¹⁰
   wide pair). The m>1 part is comparable to the m=1 part and decays in
   the hub level (exponents ≈0.27 and ≈0.71 over X=16…512). This is
   consistent with HC_Π and proves nothing.

## Not done / caveats

* HC_Π itself is open. A Shiu/Henriot route for long ranges was sketched,
  but the dependence of its constants on α was not checked; the short ranges
  have no tool.
* Prime powers: the weights `1/φ(n′)` for `ℓ²|M` are Assessment.
* Korolev/Karatsuba papers were not archived, and their statements were not checked.

## Requests to parent

* Hostile review of §1–§2 (Theorem 2.3), Def 2.0 and Cor 4.1.
* Decide whether to correct O4 §4.2 (saturated hubs) and DISCOVERIES (H)14.
