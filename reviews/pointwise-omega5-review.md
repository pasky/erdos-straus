# Hostile review of POINTWISE_OMEGA5.md (task O13)

Subject: `side-agent/omega-inverse-squares` at d1a0b93 (adds
`AGENT_REPORT_O13.md`). Files reviewed: `POINTWISE_OMEGA5.md` (O5),
`scripts/omega5_codeg.py`, `data/omega5/*`, `O13_LITERATURE_NOTES.md`,
against O4 §4.2/Thm 4.2/§7, O3 §1–2, O2 §10.3, and the O4 review.

## Verdict table

| # | Claim | Verdict |
|---|---|---|
| 1 | §1 Lemma 1.1, Cor 1.2 (IS obstruction is an artefact) | **CONFIRMED** (trivial and correct). Wording defect D6 |
| 2 | Lemma 2.1, Lemma 2.2, Theorem 2.3 (bound on Δ¹(Q,K)) | **CONFIRMED**. Every case and constant was rechecked by hand |
| 3 | Thm 2.3 "Hence" for every O (the m=1 part of Δ_O) | **PROVED only for events with ℓ‖M at every ℓ∈O**. The prime-power case is easy to close (D1) |
| 4 | Def 2.0 counterexample (literal HC false) | **CONFIRMED** |
| 5 | Saturated-hub cost absorbed by O4 Thm 4.2 | **CONFIRMED**. The stated cost factor `e_ℓ` is a large overestimate: the true factor is `ℓ/(ℓ−1)` (D3) |
| 6 | Lemma 3.1, Prop 3.2, Lemma 3.3 | **CONFIRMED** (Prop 3.2 is subject to D1). The remark after Lemma 3.3 and §4 item 1 are **wrong** (D5) |
| 7 | Cor 4.1 (HC_Π ⇒ HC* ⇒ `log W ≥ 0.08(log₂p)^{3/2}`) | **CONFIRMED as an implication**: HC* is enough for Thm 4.2. "PROVED" needs D1 |
| 8 | §5 literature | **CONFIRMED** for CG Thm 1, BG 1309.1124 Thm 1 and Shparlinski survey Thm 13 (checked against the archived text) |
| 9 | EVIDENCE table | **CONFIRMED**: the T=10⁹ replay is identical and the table matches the data. Minor D7 |

Overall: the core of O13 is sound and is a real advance. The "sharp
obstruction" of O4 §7.3/§7.5 is not an obstruction to HC's m=1 part.
Literal HC is false, and saturated hubs repair it at no real cost. The
open residual is HC_Π. Defects D1–D7 are below. None of them breaks a
PROVED theorem. D1 is a scope gap with an easy fix, and D5 overstates an
Assessment.

## Item 1 — §1 squarefree lifting. CONFIRMED

* Lemma 1.1: `n=st²` with s squarefree is unique, so the pairs inject
  into `{n≤X : n≡w (q)}`. ✔
* Cor 1.2: atoms on the ray `t(u,v)` are exactly the M with
  `M≡−1 (4h)` and `q|M`. Given such an M, `M+1=4h·N` and
  `N=st²` with s squarefree is unique, and `tu≡κtv (q)` holds because
  `u≡κv`. So **every** such M is an atom of the ray containing O, and the
  ray sum is just `Σ_{n≡n_0 (4h)}1/n`. This is the (F3) count of O3
  Prop 2.2 read as an upper bound. O4 §7.3 instead counted
  `t ↦ s_t` (least residue, any s) and counted each n once for every
  `t²|n`. The O5 diagnosis is correct.
* Atoms ↔ squarefree s: O3 Lemma 2.1 (D=sa² fixes s and a). ✔

## Item 2 — Lemmas 2.1–2.2, Theorem 2.3. CONFIRMED

Checked line by line:

* h_1, h_2, h_3 are the three hub families (`a²≡K·ab` gives (C1),
  `bK≡a` gives (C2)). Reduction to squarefree s via `s′·fa≤sa`. If some
  vertex of O is not a hub mod ℓ, then all heights are `>H` mod q. ✔
* Box facts: `1/n≤Q/(2SAB)`, `SAB>Qy/32`, `AB>h_3/4`, `SA>h_1/4`,
  `SB>h_2/4`; at most `8𝓛³` boxes. ✔
* (a) `≤2^{ω+2}/Q`. ✔ (b) (C1) with injectivity of `(s,a)↦sa²` gives
  `32A/Q+4/h_1`, (C3) gives `2^{ω+1}/A`, and the min is
  `≤4/h_1+2^{ω/2+3}Q^{−1/2}`. ✔ (c) is symmetric (B<Q gives
  `≤2^ω` values of b, a in one class, `≤2A/Q`). ✔
* (d) with `AB≥F′Q`: `≤2^ω` points per s, contribution `≤2^ωQ/(AB)≤1/F`. ✔
  With `AB<F′Q`: s lies in one class mod Q, E gives
  `|E|(2/h_3+16/y)`, and the rays give their whole ray sums (Lemma 2.1,
  with `(u,v)∈Λ*` because t is a unit). ✔
* Lemma 2.2: sub-box `A′B<Q/2`, so `|det|<Q` forces collinearity. The
  three line types: for `δ=(u′,v′)`, `v′a−u′b≡0` on Λ and `J≠0` gives
  `max>Q/2`; for `δ=(u′,−v′)`, `v′a+u′b∈(0,4max)` gives `max>Q/4`;
  axis directions force `Q|δ`. ✔ A brute-force test (5k random and
  adversarial `(Q,K,A,B)` with `K=±r/s` small, Q<4000) found no
  violation. The test is weak: E was almost always empty.
* Final sum: with `F=(Ĥ/4^ω)^{1/3}`, `1/F=F′²/Ĥ=4^{ω/3}Ĥ^{−1/3}`, and the
  other terms are smaller (they use `Q^{−1/2}<1/y≤1/Ĥ` and
  `2^{ω/2}≤y`). ✔
* "Hence": `Ĥ≥min(H+1,y)≥H≥4^k`, `ω≤k`, `P(e∖O)=1/φ(n)≤2/n`. ✔ This
  holds only for events with `ℓ‖M` at every ℓ∈O. See D1.

## Item 3 — Def 2.0: the counterexample and the saturated-hub repair

**Counterexample: CONFIRMED.** O2 §10.3 (remark) states that splitting a
class mod `ℓ^a` into its lifts leaves `Δ_O` unchanged for O containing
a lifted vertex. Take k=3 and `ℓ_1,ℓ_2` just above `y=2T^{1/4}`, so
`e_ℓ=3`. Take `x_i` a lift of −1 that is not in `𝓗_H(ℓ_i^3)`. This
exists because `3H(1+log H)<ℓ_i²` for `H≤y`. For primes
`r∈[T^{.28},T^{.32}]` with `ℓ_1ℓ_2r≡3 (4)` we have `M=ℓ_1ℓ_2r≤T`,
`m=1`, and the class is −1 (non-injective form of O3 Lemma 2.1). Also
`e_r≥3`, so all lifts at r except `O(H log H)` of them are non-hubs and
survive deletion. Hence `Δ_O ≥ (1−o(1))·½Σ_r 1/r ≈ 0.067`, while HC
demands `𝓛^BH^{−a}→0`. The lifting is essential: with `e_ℓ=1`, `x_i=−1`
is itself a hub. A consequence of this item: O4 Thm 4.2 *as written* is
a true but **vacuous** implication. The usable statement is Thm 4.2 with
saturated hubs. O5's phrase "O4 Thm 4.2 survives" should say this
(see D4).

**Cost: CONFIRMED, with a sharper bound (D3).** See Item 5.

## Item 4 — the prime-power gap (D1)

**D1 (moderate; scope of PROVED labels).** Theorem 2.3's "Hence",
Prop 3.2 and Cor 4.1 are labelled PROVED "for every vertex set O".
But `Δ_O` includes events with `ℓ^v‖M`, `v≥2`, for some ℓ∈O, and for
these O5 itself says "for ℓ²|M it is Assessment" (Def 2.0, last
sentence; §6). For such an event, `P(e∖O)=1/φ(M/(q′m))` with
`q′=∏_{ℓ∈O}ℓ^{v_ℓ(M)}`, which is up to `q′/q` times larger than
`2/n`, `n=M/q`. So `2Δ¹(q,κ)` does **not** bound those terms. The
labels overclaim as written.

*Fix (reviewer-checked sketch; the author should write it out).*

1. Group the events by the exponent pattern `(v_ℓ)_{ℓ∈O}`. Since
   `ℓ>y=2T^{1/(k+1)}` and `∏ℓ^{v_ℓ}≤T`, we have `Σv_ℓ≤k`. So there are
   at most `binom(k,|O|)≤2^k` patterns.
2. For a fixed pattern, the event contains the lifted vertex
   `(ℓ,x_ℓ)` iff its class mod `ℓ^{v_ℓ}` is `x_ℓ mod ℓ^{v_ℓ}`. Exactly
   one lift qualifies, and `v_ℓ≤e_ℓ`. So the events lie in the system
   `(q′,κ′)` with κ′ fixed by O.
3. Their weight is `1/φ(n′)≤2/n′` with `n′=M/(q′m)≥y`, because e strictly
   contains O and so has a free prime outside O.
4. Theorem 2.3 needs only Q odd and `Q>y²`. It applies with `Q=q′`, and
   saturation gives heights `>H` mod `q′` (D2).

Hence the m=1 part and the `m≤μ` part are bounded by `2^k` times the
stated bounds. The factor is absorbed in HC*'s `e^{Ck}`, and in
Thm 4.2 it adds `O(k/a)` to `log H`. With this paragraph added, Thm 2.3
"Hence", Prop 3.2 and Cor 4.1(i) are PROVED as stated. Without it they
are PROVED only for O whose events satisfy `ℓ‖M` at every ℓ∈O.

**D2 (minor; inconsistency).** Def 2.0 asserts that heights transfer to
`q′`, while §6 says "the transfer to `q′` was not checked". The transfer
is immediate. `v_ℓ(M)≤e_ℓ`, and a hub congruence mod `q′` (κ′ a unit)
reduces to a hub congruence mod every `ℓ^{v_ℓ}`, which saturation
forbids. Delete the §6 caveat, or restate it as D1's weight
bookkeeping, which D1 closes.
