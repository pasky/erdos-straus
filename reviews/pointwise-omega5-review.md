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

## Item 5 — saturated-hub cost and Cor 4.1 (is HC* enough for Thm 4.2?)

**D3 (minor; loose but harmless).** The quarantine probability is
`h_ℓ ≤ Σ_{v≤e_ℓ}|𝓗_H(ℓ^v)|/φ(ℓ^v) ≤ 3H(1+log H)/(ℓ−1)·Σ_{v≥1}ℓ^{1−v}
= 3H(1+log H)/(ℓ−1)·ℓ/(ℓ−1)`. O5 bounds each term by the v=1 term and
gets a factor `e_ℓ`. The true factor is `1+O(1/y)`, not `e_ℓ`. Also
`e_ℓ≤k`, not `k+1`, since `ℓ^{k+1}>y^{k+1}>T`. So O4's condition
`300H(1+log H)<y` and `S_hub` are unchanged up to `1+O(1/y)`. The
absorption claim is **CONFIRMED** both ways:

* `h_ℓ≤1/100` (O3 Lemma 1.3) holds at `H=y^{1/2+o(1)}`.
* `S_hub` enters only additively, in `log(M_1/μ)` and in
  J ≈ e²S_hub primes per modulus (O3 Cor 1.2). A factor `≤k+1` costs
  `O(log k)` in `log K`, and a factor `1+O(1/y)` costs nothing.
* O3 Thm 1.1 and Lemma 1.3 accept arbitrary forbidden sets
  `H_ℓ⊆(ℤ/ℓ^{e_ℓ})^×`, so replacing the hub set by the saturated hub set
  changes nothing else.

**Cor 4.1(ii): CONFIRMED.** O4 Thm 4.2 invokes HC exactly once, at
`H=⌈(𝓛^Be^{0.011k}/η_k)^{1/a}⌉`, `k=⌊(a𝓛/5.72)^{1/3}⌋≤𝓛^{1/2}`,
for O with `2≤|O|≤k−1` and no (now saturated) hub vertex. Sets
containing a quarantined vertex carry no P′-mass. HC*'s three
restrictions are all met:

* `log H=(log(1/η_k)+O(k+log𝓛))/a ≈ 2.86k²/a`, while
  `log y ≈ 𝓛/k ≈ 5.72k²/a`. So `H=y^{1/2+o(1)}≤y`, and `4^k≤H` since
  `k log 4≪k²`.
* `e^{Ck}` adds `Ck/a` to `log H`, which is `o(k²)`.
* The 2^k pattern factor of D1 does the same.

`0.2·(1/6)^{1/2}=0.0816>0.08` ✔. Cor 4.1(i) holds: Prop 3.2 with
`μ=Ĥ^{1/6}` plus HC_Π, with `Ĥ≥H`. It is PROVED subject to D1.

**D4 (moderate; status wording).** O5 proves literal HC **false**, yet
it keeps writing as if HC were merely open:

* §0 (§4 bullet): "HC itself is still **not** proved".
* AGENT_REPORT item 5: "HC is not proved".
* Remark after Thm 2.3: "What remains for full HC".
* Cor 4.1: "HC_Π does **not** imply literal HC".
* §0 (§3 bullet): "give HC with a=1/6", where HC* is meant.

Also, Hypothesis HC_Π is stated with "no H-hub" in O4's sense, and only
Cor 4.1's parenthetical switches to saturated hubs. It must be stated
with saturated hubs. With O4's hubs it is false by Def 2.0's mechanism.
Take lifts at `ℓ_1,ℓ_2` of the class `−4` (F1, `s=a=1`). The atoms
`(1,1,b)` with `5|4b−1` have `m=5`, survive since `5|4D+1=5`, and give a
constant codegree. The class −1 itself is no example, because there
`u=v=1`, `m|2` and so `m=1`.

Required wording:

* "Literal HC is false (Def 2.0); HC* (saturated hubs) is open."
* "O4 Thm 4.2 as stated is vacuous; it holds with HC* (Cor 4.1(ii))."

Parent action: annotate O4 §4.2/Thm 4.2 and DISCOVERIES (H)14 accordingly.

## Item 6 — §3 Lemma 3.1, Prop 3.2, Lemma 3.3, and the §4 anatomy

* Lemma 3.1: CONFIRMED. `m|gcd(M,4D+1)|t(u+v)` and `gcd(m,t)|gcd(M,M+1)`.
  (2) and (3) are direct algebra. The m-system reduction and the bounds
  `h_3(qm,κ_m)≥m−1`, `h_1,h_2≥((m−1)/4)^{1/2}` hold.
* Prop 3.2: CONFIRMED (`2/n′=2m/n≤2μ/n`, `n≥y`), subject to D1.
* Lemma 3.3: CONFIRMED.
  * (i) `M<2qY(u+v)` gives `≤Y(u+v)/(2h)+1` values of M at weight
    `2/Y`.
  * (ii) `gcd(qm,4h)=1` because `gcd(u+v,uv)=1`.
  * (iii) is trivial.

**D5 (moderate; Assessment overstated as "done").** The remark after
Lemma 3.3 says (ii) is HC-shaped "for rays with `τ(u+v)≤y^{2/3}`", and
§4 item 1 says such rays "are done". This is false:

* Bound (ii) is `τ(u+v)(2/y+𝓛/(2h))`. Its second term needs
  `τ(u+v)≤hH^{−a}`, not `τ≤y^{2/3}`.
* For h just above H, with `H=y^{1/2+o(1)}` (Thm 4.2's regime) and
  `τ≈y^{2/3}`, the second term is `≈y^{1/6}≫1`.
* The correct per-ray statement is `τ(u+v)≤min(y,h)·H^{−1/3}` (⇐
  `τ(u+v)≤H^{2/3}`). The open set of unbalanced rays therefore also
  includes `H^{2/3}<τ(u+v)≤y^{2/3}`, so (DIV) is mis-delimited.
* The lower bound "these force `u+v≥y^{c log log y}`" becomes
  `H^{c log log H}`.

More fundamentally, Lemma 3.3 bounds single rays. HC_Π is a sum over all
rays and off-ray points of all m-systems, and no ray-count is given for
m>1: Lemma 2.2's `2F′+1` rays per box is for one system `(Q,K)`, and
there are many m. So no class of rays is "done" for HC_Π. The text
should read "per-ray bounds; the number of rays per m-system is not
controlled". This is Assessment-level, so no PROVED claim is affected.

## Item 7 — §1 Remark and §5 literature

**D6 (minor; wording).** The §1 Remark calls O4's over-counted problem
"genuinely beyond Weil". §5's own verdict shows that the lifting alone
gets within a factor `min(T^{O(1/log𝓛)},√Y)` of the target. Weil is
trivial in that range, but the problem is not shown to be hard. Say
"beyond the Weil range; within a divisor factor by lifting".

Literature, checked against the archived text (`sources/lit2026/*.txt`;
the BG statement was also checked against the PDF):

* **Cilleruelo–Garaev, arXiv:1007.1526, Thm 1.** The text gives
  `I_2(M;K,L)<M^{4/3+o(1)}p^{−1/3}+M^{o(1)}`, for prime p, uniformly
  in K and L, with boxes `[K+1,K+M]×[L+1,L+M]` and products `xy≡λ`.
  The proof is "based on an idea of Heath-Brown". ✔ Matches O5.
* **Bourgain–Garaev, arXiv:1309.1124, Thm 1.** The text gives
  `J_{2k}<(2k)^{90k³}(log N)^{4k²}(N^{2k−1}/m+1)N^k` for the energy of
  reciprocals mod any m, with `I=[1,N]`. ✔ Exact.
* **Shparlinski survey, arXiv:1103.2879, Thm 13.** Main term
  `φ(m)XY/m²`, error `O(m^{1/2+o(1)})`. The survey says that making it
  nontrivial for `XY<m^α`, `α<3/2`, "is out of reach". O5's "trivial for
  `XY<m^{3/2}`" is the correct reading. ✔
* Korolev/Karatsuba: not archived. O5 flags this. Fine.

The negative verdict ("no known theorem gives IS pointwise") is an
Assessment, and O5 makes it moot for HC anyway.

## Item 8 — EVIDENCE

* Replay `omega5_codeg.py 1e9 331 337 347 1024`: the output is
  byte-identical to `data/omega5/codeg_1e9_pair.txt`. It runs in about
  2 s, not "~1 min".
* All table entries match the data files. The m>1 decay exponents
  (16→512) are `ln(.01713/.00670)/ln32=0.27` and
  `ln(.04126/.00348)/ln32=0.71`. ✔
* The script weights are `1/φ(r/q)` on distinct events with `q‖M`, the
  hub levels are capped at HCAP, and `Π=Π_0`. The data are labelled
  EVIDENCE.

**D7 (minor).** The wide pair's m>1 column is identically 0 for a
structural reason, not "essentially":

* `T/q≈989` and `n′>y=331`.
* m is odd and `>1`, so `m≥3`, hence `mn′>993>T/q`.

The column is vacuous and should be described as such. The replay
timings are also overstated.

## Defect list

| # | Severity | Where | Defect | Fix |
|---|---|---|---|---|
| D1 | moderate | Thm 2.3 "Hence", Prop 3.2, Cor 4.1 | PROVED labels cover only events with `ℓ‖M` at every ℓ∈O; the prime-power weights are only Assessment | Sum over `≤2^k` exponent patterns, Thm 2.3 at `Q=q′` (sketch in Item 4) |
| D2 | minor | Def 2.0 vs §6 | Height transfer to `q′` is asserted in one place and called "not checked" in the other | The transfer is immediate; drop the caveat |
| D3 | minor | Def 2.0 Cost | The factor `e_ℓ(≤k+1)` is really `ℓ/(ℓ−1)`; and `e_ℓ≤k` | Restate; the absorption is then trivial |
| D4 | moderate | §0, Thm 2.3 remark, Cor 4.1, report item 5, HC_Π | Literal HC is false but is called "not proved"; HC_Π is stated with O4 hubs, under which it is false (class −4, m=5) | "Literal HC false; HC* open"; O4 Thm 4.2 is vacuous as stated; state HC_Π with saturated hubs |
| D5 | moderate (Assessment) | Lemma 3.3 remark, §4 item 1, (DIV) | `τ≤y^{2/3}` does not make (ii) HC-shaped (`τ/h` can be `y^{1/6}`); per-ray bounds are not "done" without a ray count | Threshold `τ≤H^{2/3}`; re-delimit (DIV); drop "done" |
| D6 | minor | §1 Remark | "genuinely beyond Weil" overstates | Reword |
| D7 | minor | §4 EVIDENCE, Replay | The wide-pair m>1 column is structurally 0; timings overstated | Reword |

**Bottom line.** Lemma 1.1, Lemmas 2.1–2.2, Theorem 2.3 (Δ¹ bound),
Lemma 3.1, Lemma 3.3 and the Def 2.0 counterexample are **PROVED and
verified**. Thm 2.3 "Hence", Prop 3.2 and Cor 4.1 are PROVED for
`ℓ‖M` events, and become fully PROVED once D1's short paragraph is
added. HC* is enough for O4 Thm 4.2, and the saturated-hub cost is
negligible. HC_Π remains open, so the proved rate stays O4 Cor 3.1.

Parent actions:

1. Apply D1–D7 in O5.
2. Annotate O4 §4.2/Thm 4.2 (literal HC false; read with saturated
   hubs) and O4 §7.3/§7.5 (the "sharp obstruction" is dissolved for
   m=1 by O5 §1–2).
3. Update DISCOVERIES (H)14.

---

# Round 2 (subject: `side-agent/omega-inverse-squares` at 8825ea7)

## R2.1 Round-1 defects D1–D7: all FIXED

| # | Status | Where |
|---|---|---|
| D1 | **Fixed.** Lemma 2.0′ added (patterns `≤binom(k,|O|)≤2^k`, `Q=q′`, weight `1/φ(M/(q′m))`); `2^k` carried into the Thm 2.3 "Hence" and Prop 3.2. I checked it: `Σv_ℓ≤k` because `y^{Σv}<T`, and patterns = compositions. | §2 |
| D2 | **Fixed.** The §6 caveat is dropped. The "reduces to one mod each ℓ^{v_ℓ}" sentence now appears twice in Def 2.0 (cosmetic). | Def 2.0, §6 |
| D3 | **Fixed.** Cost is `ℓ/(ℓ−1)`; `e_ℓ≤k`. | Def 2.0 |
| D4 | **Fixed.** The §0, Thm 2.3 remark and Cor 4.1 wording now says "literal HC false; Thm 4.2 vacuous as stated; HC* open". HC_Π is stated with saturated hubs. The −4/m=5 example is recorded. One residue: §0 line 25 still says "O4 Thm 4.2 survives with saturated hubs". That is acceptable as worded, but "holds under HC*" is cleaner. | §0, §2, §4 |
| D5 | **Fixed.** Threshold `τ≤min(y,h)H^{−1/3}` (⇐`τ≤H^{2/3}`); "per ray only, no class done"; (DIV) re-delimited. | §3, §4 |
| D6 | **Fixed.** | §1 |
| D7 | **Fixed.** The wide-pair column is described as vacuous, and the timings are corrected. | §4, Replay |

## R2.2 The O4 erratum/update boxes: CONFIRMED, with one wording nit

* §4.2 erratum (before HC): correct and sufficient. It says literal HC is
  false, gives the saturated-hub reading, the cost `1+O(1/y)`, "Thm 4.2
  vacuous as stated, holds under HC*", and "HC* open".
* §7.3 update: correct, with one nit (R2-D4 below): "the m=1 part of
  every non-hub codegree" should read "every vertex set without
  *saturated* H-hubs, `4^k≤H≤y`".
* §7.5 update: correct.
* DISCOVERIES (H)14 is still the parent's to fix.

## R2.3 New §7: verdicts

**Lemma 7.0: CONFIRMED.**

* `m|a+b` and `m|M` give `gcd(m,ab)=1`, so `qm|4sab−1` fixes s mod qm.
* `M=qmn′≡−1 (4ab)`, and admissible s step `n′` by exactly `4ab`.
* The bound is `2/ν+(1/2ab)·log` (upper bound; s squarefree is dropped).
* Atoms whose true Π-part is a proper multiple of m are charged to their
  own fibre, so there is no double use.
* The split `Δ_O^{>μ}≤P_0+(𝓛/2)P_1` is ✔. P_1 over-counts by including
  all `m|a+b`, which only loosens the bound.

**Prop 7.1 (period part, a=1/4): CONFIRMED, PROVED.** Rechecked:

* `N_R≤AB/q+min(A,B)`, and per box
  `τ*(4X)/q+τ*(4X)/X`.
* `X>h_3^{1/2}/2` because `X²≥AB>h_3/4`, so `4X^{−1/2}<4√2·h_3^{−1/4}≤6h_3^{−1/4}`. ✔
* `X>3q²`, divisor switching:
  * `#{n≡c (q), d|n}` over a stretch of length B is `≤Bg/(qd)+1`, where
    `g=gcd(d,q)`.
  * `Σ_{d≤2√B}g/d≤τ(q)(1+½log4B)`.
  * `4√B<4B/(√3q)<2.4B/q`. ✔
* Nicolas–Robin's constant (1.5379·log2) is right.

Minor defects R2-D2 and R2-D3 are below. Neither affects the conclusion.

**P_0 reductions: CONFIRMED.**

* For fixed `(a,b)`, the classes `−(qm)^{−1} mod 4ab` are distinct, since
  `m≤a+b<4ab`.
* Bound one (`2τ(a+b)/y`) is trivial; the "(1+o(1))" is unnecessary.
* Bound two is the lifting count at fixed `(a,b)`: M determines `(s,m)`,
  and `n′∈[Y,2Y)` forces `M<2qY(a+b)`.
* The first atom has `s<qm(1+y/(4ab))+1`. ✔

**R2-D1 (moderate; status mislabelled and superseded).** The middle band
`H^{1/6}<m≤H^{1/3−ε}` is listed as an *Assessment* (per-m thin-box
sketch, HC-shaped for `μ_0≤H^{1/3−2a}`). But Prop 3.2 is stated and
proved for **every** μ: atoms with `m≤μ` contribute
`≤2μΔ¹(q,κ)≤2^{k+1}Cμ𝓛⁴4^{k/3}H^{−1/3}`. With `μ=H^{1/3−a}` this is
`≪2^k4^{k/3}𝓛⁴H^{−a}`. So:

* `m≤H^{1/3−a}` gives exponent a. This is **PROVED**, by an existing
  proposition, over a *larger* range than the sketch (`H^{1/3−a}` vs
  `H^{1/3−2a}`). It covers all of the atom's mass, not only the first
  terms.
* The sketch is therefore superseded and should be deleted, or marked
  "superseded by Prop 3.2 with general μ".

The correct frontier is: for a target exponent `a∈(0,1/3)`, everything
is PROVED except the **first terms P_0 with `m>H^{1/3−a}`**. The period
part is PROVED (a=1/4) for all m.

Consequences:

* HC_Π should be restated with threshold `m>H^{1/3−a′}` instead of
  `Ĥ^{1/6}`.
* Cor 4.1 then gives HC* with `a=min(a′,1/4)` instead of
  `min(a′,1/6)`, and `log W ≥ 0.2·min(a′,1/4)^{1/2}(log₂p)^{3/2}`.
* The status line "m in (H^{1/6},H^{1/3−ε}] Assessment; m>H^{1/3} open"
  should read "m≤H^{1/3−a} PROVED (Prop 3.2); first terms with
  `m>H^{1/3−a}` open".

**R2-D2 (minor).** Prop 7.1 says "Since `q>y²≥H⁴`". But HC* allows
`H≤y`, and Thm 4.2 uses `H=y^{1/2+o(1)}`, so `y≥H²` (and hence `y²≥H⁴`)
is not guaranteed. The conclusion is unaffected:
`q^{−1+o(1)}<y^{−2+o(1)}≤H^{−2+o(1)}≤H^{−1/4}`. Write `q>y²≥H²`. The
same unjustified "`y≥H²`" appears in the (superseded) middle-band
sketch.

**R2-D3 (minor).** Under Lemma 2.0′, Prop 7.1 runs with `Q=q′`, which
is not squarefree. Its divisor switching uses `Σ_{g|q}1=τ(q)`, which
equals `2^{ω}` only for squarefree q. For `q′`, `τ(q′)≤2^{Σv}≤2^k`.
This is harmless, but the factor should read `τ(q′)`.

**R2-D4 (trivial).** Fix the O4 §7.3 box wording (R2.2) and the §0
"survives" line (R2.1).

**Assessments in §7.** "No longer a divisor-sum problem" and "a pure
core-counting problem averaged over m" are fair descriptions of P_0.
Nothing in them is labelled PROVED.

## Round 2 bottom line

* D1–D7 are fixed, and the O4 boxes are correct.
* §7's PROVED claims (Lemma 7.0, Prop 7.1, the P_0 reductions) are
  verified.
* The only substantive finding is R2-D1. The middle band is already
  PROVED by Prop 3.2, so the open residual is exactly the first terms
  P_0 with `m>H^{1/3−a}`. HC* would then follow with
  `a=min(a′,1/4)`.
* HC* remains open, and the proved rate stays O4 Cor 3.1.
