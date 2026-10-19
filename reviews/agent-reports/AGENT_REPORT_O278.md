# AGENT REPORT O278 — consolidation C2: hardening the 3/4 exceptional-set note

Branch `side-agent/paper-threequarter`. Target `paper/es-threequarter-note.tex`.
Internal only; no external release.

## 1. Literature check (goal 1)

Question: is there a published or arXiv result (2015–2026, or earlier)
that improves Vaughan's `E(N) ≪ N exp(−c (log N)^{2/3})` for 4/n, or for
m/n with three unit fractions?

**Answer: none found.** The 3/4 bound is not in the literature we could
locate. The best published bound for `4/n` is still Vaughan's 2/3. This
supports "no known improvement". It does not prove that none exists.

The search was a research subagent plus my own checks of the local PDFs.

| source | exceptional-set statement | how verified |
|---|---|---|
| Vaughan, Mathematika 17 (1970) 193–198, DOI 10.1112/S0025579300002886 | `#{n<N : f(n)=0} ≤ N exp(−c log^{2/3} N)` (as quoted by ET) | No lawful full text (`sources/vaughan-1970-access-log.md`). Statement taken from ET and Bloom–Elsholtz. |
| Elsholtz–Tao, J. Aust. Math. Soc. 94 (2013) 50–105, arXiv:1107.1010 | Intro: "it was shown by Vaughan [82] that the number of n<N for which f(n)=0 is at most N exp(−c log^{2/3} N) … (Compare also [48,84,39,89] for some weaker results)". No improvement of its own. | I read it in the local PDF (`pdftotext`, l. 101–106). |
| Bloom–Elsholtz, "Egyptian fractions", arXiv:2210.04496 (2022 survey) | "Vaughan showed that `E_{4,3}(N) ≤ N exp(−c(log N)^{2/3})`". It gives the general bound `E_{m,k}(N) ≤ N exp(−c_{m,k}(log N)^{1−1/(2^{k−1}−1)})` for `m>k≥3` (Elsholtz). At k=3 this is Vaughan's bound; at k=4 it is 6/7, but that is a different problem (four summands). | Subagent read the arXiv HTML. |
| Pomerance–Weingartner, arXiv:2511.16817 (Ramanujan J. 2026) | Thm 1.3: for `4≤m≤(log N)^2`, `#{n≤N : m/n not a sum of 3 unit fractions} ≤ N/exp(C(log² N/φ(m))^{1/3})`. At fixed m=4 the exponent is again 2/3. The paper says its proof "largely follows the argument in Vaughan". | Subagent read the arXiv HTML. The campaign had already audited this paper. |
| erdosproblems.com/242 | Lists Vaughan's bound and no stronger exceptional-set estimate. | Page visited. The formulas did not render, so only the list of references was used. |
| Elsholtz, Trans. AMS 353 (2001); Elsholtz–Planitzer 2020; Huang–Vaughan 2013 (binary); López 2022/2024; Chamberland 2026 | None improves the 2/3 exponent for three summands. (Elsholtz 2001 is the source of the k-term exponents; Huang–Vaughan treats two summands.) | Subagent; LITERATURE_2026.md. |

**Conclusion for the note.** Say "improves the exponent 2/3 of Vaughan
[V]; we are not aware of an earlier improvement of the exponent". Do not
claim priority beyond that.

Related analogue: for k ≥ 4 summands, Elsholtz already has exponents
above 3/4 (6/7 for k=4). That is consistent with a parameter-count
heuristic and is not a 3-term result.

## 2. Fresh line-by-line audit (goal 2)

I audited the note at commit `ace654cf` (1466 lines), working from the
displayed statements. Two earlier reviews exist; I read them only for
orientation. Every lemma on the load-bearing route was re-derived:
Section 5's unpruned supply → Cor 4.4 → the moment theorem
(conditional-independence proof) → void → Bonferroni assembly → primes →
Rankin. The re-derivations are summarised below, together with the
places where I disagree or tighten.

### 2.1 Analytic inputs as actually stated in the sources

* **Shiu, Theorem 1** (I checked the scanned pp. 162–163 myself). The
  class M is defined by (i) `f(p^l) ≤ A_1^l` and (ii) `f(n) ≤ A_2(ε)n^ε`.
  The bound is (2.1) `Σ_{x−y<n≤x, n≡a(k)} f(n) ≪ y/(φ(k) log x) ·
  exp(Σ_{p≤x, p∤k} f(p)/p)` "as x→∞, uniformly in a, k and y", provided
  `k<y^{1−α}` and `x^β<y≤x`, with (1.1) `0<a<k`, `(a,k)=1`. The implied
  constants depend on α, β and f only. The note's (3.3) matches this,
  including the separate handling of `q=1`. The phrase "as x→∞" is
  absorbed into the thresholds; for bounded x the bound is trivial after
  enlarging the constant.
  * The three functions used are `(3/2)^ω` (pruned route only), `n/φ(n)`
    (profile lemma, not load-bearing) and `2^ω(n) n/φ(n)` (Lemma 5.1,
    load-bearing). All three are in M with fixed `A_1, A_2`.
  * In every application the modulus is `≤ K^2` and the box is
    `(U, 21U/20]` with `U ≥ K^{10}`.
* **Brun–Titchmarsh** in the Montgomery–Vaughan form,
  `π(x+y;q,a)−π(x;q,a) ≤ 2y/(φ(q)log(y/q))` for `y>q`. The note's (3.1)
  is the special case `x=0`. It is applied with `q ≤ 4x^{1/3}`, where
  `log(x/q) ≥ (2/3−o(1))log x`. Correct.
* **Bombieri–Vinogradov.** Davenport Ch. 28 states it for ψ with
  `max_{y≤x}`. The note's form, with π, li and two fixed endpoints, is
  the standard partial-summation corollary. The factor 2 is correct. The
  constants are ineffective (Siegel), and the note says so. *Edit:* the
  rewrite now states the deduction explicitly.

### 2.2 Re-derivation of the load-bearing lemmas (all confirmed)

* **Identity (L2.1).** Numerators: `nv+u+s = s(kℓ+1) = 4suvw`. This is a
  form of the classical Type II criterion (ET Prop 2.7, bullet 4, credited
  there to Vaughan [82]). *Edit:* the attribution is added.
* **Distinctness / CRT (L2.2).**
  * `|uv'−u'v| < z_j² < x_j < ℓ` gives `(u,v)` equal.
  * `kℓ ≡ k'ℓ ≡ −1 (4uv)` and `4uv > 4H² > K` give `k=k'`.
  * `ℓ > X^{1/2} > K ≥ y` gives independence on `Z/𝓜Z`.
  * The relevant properties are distinctness across *all* multipliers and
    fibres, and that at most one atom per ℓ can be hit.
* **Lattice (L3.1).**
  * Lower bound: the main coefficient is `Π_{p∤k}(1−p^{−2}) ≥ 6/π²`. The
    relative error is `≪ τ(k)k²/(φ(k)H) ≤ kτ(k)²/H ≤ 4K²/H`, using
    `k/φ(k) ≤ 2^{ω(k)} ≤ τ(k)`.
  * Upper bound: from the `1/φ` divisor expansion. A divisor `d` of `u`
    with `u ≡ a (k)` reduced forces `(d,k)=1`. The `d>H` tail is
    `≪ (log z)H^{−1/2}`.
  * The constant 1/4 is safe for `K ≥ K_0`.
* **h-lemma (L3.2).** `Σ_{d odd} μ(d)/d² = 8/π²`, so the main term is
  `(1/4)·(8/π²)log K = (2/π²)log K`. The removal bound is immediate.
* **Weighted second moment (L5.1).** Verified in full.
  * `F = 2^ω·id/φ` has `F(p^a) = 2p/(p−1)` for all `a≥1`, so `h(p^a)=0`
    for `a≥2` and `h(p)=(p+1)/(p−1)`. Both `Σ_{n≤V}F ≪ V log V` and the
    outer `(log z)²` follow.
  * In Shiu, `Σ_p F(p)/p = 2 log log V + O(1)`. The local factor
    `exp(−Σ_{p|d}2/(p−1)) ≍ (φ(d)/d)²` gives a box sum of
    `≪ log U · φ(d)/d²`.
  * Summing over pairs uses `φ([k,k'])/[k,k']² ≤ (k,k')/(kk')`, giving
    `(1+log K)³`.
  * Total: `(log z)^4 (1+log K)^3`.
* **Unpruned supply (T5.2).** The main term is
  `≥ x/log 2x · (1/16)Λ² h(J)`, with `Λ ≥ (1/12)log x`. For the error,
  `W(q)² ≤ 2^{ω(q/4)} Σ r²` (at most `2^{ω(q/4)}` ordered coprime
  splittings), and Cauchy–Schwarz gives
  `(x t^6)^{1/2}(C_{26} x t^{−26})^{1/2} = O(x t^{−10})`. Each triple at
  modulus q has a reduced residue, and distinct k give distinct residues.
  Each is bounded by `E*(q)`, a max over residues, so data-dependent
  families (`J=J_c`) are covered. Confirmed.
* **Fibre masses (C4.4 / C5.3).** An active atom has a unit residue mod
  k, so `f_c = f^{all}_{c;J_c}` *exactly*, with `1∈J_c` and
  `(c,L_{J_c})=1`. Upper bound `μ_c ≤ A_h t² h(K(K)) ≤ C_u t³` for every
  c.
* **Moments (T6.3, conditional-independence proof).** In a fibre,
  `H_X = Σ_ℓ I_ℓ` is a sum of independent Bernoulli variables. Then
  `E(H)_m = Σ_{distinct ℓ_i} Π p_{ℓ_i} ≤ μ_c^m`. The base is independent
  of m. Confirmed.
* **Void (L7.1).**
  * The selector forces `p∤c` for supported `p≤y`.
  * For `p>y`, the events `p|c` are independent with probability `1/p`.
  * `E e^{yZ} ≤ exp((e−1)yΣ_{p>y}p^{−2}) = O(1)`.
  * `h(J_c) ≥ (a_0−2Z)log K`.
  * On the good event, `P(H=0|c) = Π(1−f_c/ℓ) ≤ e^{−μ_c}`.
  * Order of constants: η, then a_v, then B. Confirmed.
* **Bonferroni and ledger (L8.1, T8.2).**
  * `Q_r(h) = C(h−1,r)` for `h≥1`.
  * `T_abs ≤ 2^{π(y)}(r+1)|A|^r` with `|A| ≤ KX^{4/3}`.
  * Exact counts `N/q+θ`, `|θ|≤1`, for every q.
  * `Σν ≤ N e^{−c_a t³} + e^{C_L t^4}`. Confirmed.
* **Primes and Rankin (§9).** Here `δu ≤ η_0 u^{3/4}` for `u ≤ L`, and
  the integral `∫ e^{−(c_0−η_0)u^{3/4}}du` converges. Confirmed.

### 2.3 Findings of this audit (none load-bearing)

| # | severity | location (old file) | finding | action |
|---|---|---|---|---|
| F1 | expository | throughout | The proof of record is §5 + §§6–9, but the text interleaves it with the superseded pruned route (§4, L3.3, L4.1, (4.2) H_kBV, Thm 4.2), the residue-profile lemma (L6.1) and the ordered-atom replay. A reader cannot see the 8-page proof. | Rewrite: the main text contains only the load-bearing route. The superseded material is moved out (it stays in git history at `ace654cf`), and a remark records that it exists. |
| F2 | expository | abstract, Thm 1.1, §10 | Internal process (notes §§, review files, "checkpoints") sits inside the theorem statement and the bibliography. Not submission style. | Moved to a single "Status" paragraph. The checkpoint section is dropped; its content is covered by the proofs. |
| F3 | attribution | L2.1 | The identity is attributed only to the internal LL note. | Attributed to the classical Type II criterion (ET Prop 2.7; Vaughan). |
| F4 | precision | (3.2) | The deduction of the BV form (π, li, fixed endpoints) from the ψ-form is not spelled out. | One sentence added. |
| F5 | cosmetic | T8.2 | "every exceptional prime `n>max(K,y)`": only `n>y` is needed (blind audit B4). | Uses `n>y`, so the final count has `+y` instead of `+K+y`. |
| F6 | precision | §9 primes proof | "Increasing the outer constant covers bounded N ≥ 3": fine. The absolute constants become absolute only after fixing κ. | κ = 1/480 is fixed in the statement of the parameter order. |
| F7 | honesty | §10 remark | The remark says the ceiling "is a theorem for this architecture" and cites internal documents (KA2, KA3, SL) as if published. | Kept as a clearly labelled remark that cites internal, unrefereed work. The heuristic balance is separated from the internal cap theorem. |
| F8 | precision | Thm 1.1 | The statement is not explicit about effectivity. | "The constants are ineffective" added to the theorem. |
| F9 | minor | L3.1 proof | The `Λ²/H` term in the lower-bound display covers the `d>H` tail. Correct but loose (blind audit B3). | Kept. |

I found **no gap**. Label recommendation: keep "internally proved; not
externally refereed".

### 2.4 From-scratch numerical sanity checks

`scripts/c2_threequarter_check.py` (log in `reviews/agent-reports/O278_c2_check.log`).
I wrote it independently of `reviews/es-threequarter-note-check.py` and
`scripts/es34_blind_audit_checks.py`. It runs under a 2 GB RLIMIT_AS and
finishes in about 2 minutes. **ALL PASS (19 checks).**

| label | what is checked | result |
|---|---|---|
| A | the identity, exactly with Fractions | 400 random atoms |
| B | same-ℓ distinctness across all multipliers (K=13, H=2, z=⌊√x⌋) | 0 collisions among 6032 atoms |
| B′ | negative control: dropping `4H²>K` | collisions appear, as expected |
| C | exact enumeration of `Z/𝓜Z`, 𝓜 = 3.4·10⁷ (K=9, selector y=3, three primes) | per fibre, `P(H=0|c,S) = Π(1−f_c/ℓ)` (dev 1e−16) and `E(H)_m = m! e_m ≤ μ_c^m` for m ≤ 4 |
| D | even Bonferroni identities | r ≤ 30, h < 120 |
| E | exact transfer: direct `Σ_{n≤N} S_y Q_r(H)` equals the term-by-term class count, and `|Σ − N·Eν| ≤ T_abs` | N = 10⁴ and 123457 |
| F | lattice sums at toy H=30, z=2500 | lower ratio 0.61–0.72 ≥ 1/4; upper ratio ≤ 1.51 |
| G | `h(K) − (2/π²)log K` | → 0.7548 |
| G | removal bound | holds |
| G | pair-lcm sum `/(1+log K)³` | 0.14 → 0.11 |
| K | `exp(−Σ2/(p−1))/(φ(d)/d)²` for d ≤ 3·10⁴ | in [0.41, 1] |
| L | `φ(4uv) ≥ 2φ(u)φ(v)` | holds |
| M | identity classes mod M equal `{−4D : D|A²}`, and `(τ−1)/2 ≤ F ≤ τ` | M < 1600 |
| N | weighted second moment `/(log z)^4(1+log K)^3` (toy) | small and decreasing |

These checks cover algebra and finite probability only. They are not
asymptotic evidence.
