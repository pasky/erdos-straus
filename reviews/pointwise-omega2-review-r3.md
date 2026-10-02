# Hostile review r3: POINTWISE_OMEGA2 §§10–11 (checkpoints 3–4)

Subject: branch `side-agent/omega-hub` @ 040df28 — `POINTWISE_OMEGA2.md` §§10–11,
`reviews/agent-reports/AGENT_REPORT_O2.md` (checkpoints 3–4), `scripts/omega2_iterq.py`,
`scripts/omega2_abstract_check.py`, `data/omega2/iterq.txt`.
Context used: POINTWISE_OMEGA.md §§6, 9 (H_MIN, Lemma 9.2, Thms 9.3/9.4, H_PP),
POINTWISE_OMEGA2 §§1–4, Elsholtz–Tao Prop. 1.4 (`sources/elsholtz-tao-1107.1010.pdf`, p. 3).

Severity scale: **major** (a PROVED claim is false or unsupported), **moderate** (a proof step
is missing or a stated claim is wrong but the result survives / an Assessment is misstated),
**minor** (constants, wording, labels, evidence bookkeeping).

## Verdict summary

| item | verdict |
|---|---|
| Lemma 11.1 (uniform mass S*) | SOUND |
| Lemma 11.2 (iterated quarantine) | SOUND |
| **Theorem 11.3** (`log(1/δ*) ≪ (log T)^3(S*+1)`) | **SOUND** (minor defects D1–D4 only) |
| Numerics for Thm 11.3 (independent code, Item 4) | CONFIRMS; subject's `omega2_iterq.py` output reproduced exactly |
| Lemma 10.1 (private covers) | SOUND |
| Lemma 10.2 (hypergraph moment bound) | SOUND (D5: an unstated symmetrisation step) |
| Theorem 10.3 | SOUND (D6, wording) |
| Theorem 10.4 (H_CD ⇒ H_MIN) | SOUND (D4, D7) |
| Prop. 10.6 | SOUND (D8) |
| Prop. 10.5 | SOUND as estimates; label inflated (D9) |
| Prop. 11.4 / §11.4 G_pair | Prop SOUND for fixed D; consequence SOUND-AFTER-REPAIRS (D10, D11) |
| Document consistency (§10.4/10.5/summary vs §11.4; stale table) | DEFECTIVE until edited (D12–D14) |

**Bottom line.** Theorem 11.3 is correct. It is the real content of checkpoint 4: the polylog Haar bound
`log(1/δ*(T)) ≪ (log T)^7/log log T` holds modulo ET Prop. 1.4 (the stated `(log T)^7 log log T` is
slightly weaker than what the proof gives), and `T^{o(1)}` holds unconditionally. It bypasses, rather than
proves, H_PP. The quarantine cost is `log T` per prime, prime powers included, and is correctly
accounted. The LLL graph is right, every surviving atom is covered, and both are confirmed end to end by
Moser–Tardos witnesses at T ≤ 10⁶. No major defect was found. The two moderate defects are D10
(uniformity at `t≍1/L`) and D12 (the note contradicts itself on whether a sharper Lemma 10.2 is the open
step; the reviewer's count sides with §11.4).

---

## Item 1. Lemma 11.1 — SOUND

Checked line by line.

* Survival of Π means `m_Π | 4D+1`; together with `m_Π | M` this gives `m_Π | g=gcd(M,4D+1)`.
  `φ(r) ≥ r/(C log log r)` for `r ≥ 3` (r is odd and `>1`, so `r ≥ 3`). Hence
  `1/φ(r_Π) ≤ C log log T·g/M`, uniformly in Π. Correct.
* The weight `max_Π 1[survives]/φ(r_Π)` depends on `(M,D)` only through M and the set of
  `ℓ^{v_ℓ(M)} ‖ M` that divide `4D+1`. That set is invariant under `D ↦ A²/D` (as `4A≡1 (M)`).
  So the reduction to `D ≤ A` at a factor 2 is legitimate.
* `D=sr'²` with s squarefree, `sr' | A` (since `v_p(sr') = ⌈v_p(D)/2⌉ ≤ v_p(A)`), `A=sr'k`, `k ≥ r'`.
  `g | (4sr'k−1)+(4sr'²+1) = 4sr'(k+r')`, and `gcd(g,4sr')=1` because `g | 4sr'k−1`. So `g | k+r'` and
  `g | 4sr'²+1`. Grouping k by the value of `g(k)` gives `Σ_k g(k)/k ≤ Σ_{m|4sr'²+1} m Σ_{k≡−r' (m)} 1/k`,
  which is exactly Lemma 4.1's sum. Correct.
* The ET form: Prop. 1.4 needs `A,B>1`. Dyadic blocks with `s` or `r'` in `[1,2)` are handled by
  enlarging the block to `[1,2]`, at no cost. Correct (inherited from PO Lemma 9.2, already reviewed).

## Item 2. Lemma 11.2 — SOUND

* The termination of the procedure is trivial: Π only grows inside a finite set.
* `w_ℓ(Π)` is **not** monotone in Π. Adding a prime ℓ' to Π kills some atoms, but it raises the
  weight `1/φ(r)` of the others from `1/φ(r)` to `1/φ(r/ℓ'^v)`. So the iteration is genuinely needed,
  and the bound must be uniform in Π. The proof handles this correctly: at the stage where ℓ is added,
  `c_0 < w_ℓ(Π_i) ≤ Σ_{atoms surviving Π_i, ℓ | r_{Π_i}} 1/φ(r_{Π_i}) ≤ Σ_{atoms, ℓ|M} wt*(M,D)`. Here
  `wt*` is the atom's S*-weight, and distinct events are at most atoms (an event's mass is
  `#classes/φ(r) ≤ #atoms/φ(r)`).
* Summing over `ℓ∈𝓑`: an atom is charged once per prime of 𝓑 dividing M. Those primes are `>z`, distinct,
  with product `≤M≤T`, so there are at most `⌊log T/log z⌋=k` of them. Prime powers `ℓ^a ‖ M` are charged
  once (per prime, not per exponent). Hence `c_0|𝓑| ≤ kS*`. Correct.

## Item 3. Theorem 11.3 — SOUND (the main claim of checkpoint 4 holds)

**Line-by-line check.**

1. *Quarantine cost.* `Q_Π = lcm(24, ℓ^{e_ℓ} : ℓ∈Π)`, with `ℓ^{e_ℓ} ≤ T`. So
   `log φ(Q_Π) − log 8 ≤ |Π| log T`, with `|Π| = π(z)+|𝓑|`. The cost is `log T` per quarantined prime,
   **prime powers included** (`e_ℓ log ℓ ≤ log T`). Accounted correctly.
2. *Coverage, i.e. (I).* Take an atom (M,D) and n ≡ 1 (mod `ℓ^{e_ℓ}`) for all ℓ∈Π. Then
   `n ≡ −4D (mod M)` requires `m_Π | 4D+1`, since `ℓ^{v_ℓ(M)} | ℓ^{e_ℓ}`.
   * If `r_Π = 1` and `M | 4D+1`, this contradicts Fact 1.1.
   * Otherwise the condition is the event `n ≡ −4D (mod r_Π)`. That event is in the list.
   * `−4D` is a unit mod `r_Π`: `gcd(D,M) | gcd(A²,4A−1) = 1`.

   So "no listed event" implies `W(n) > T`. Every surviving atom is covered. (Independently confirmed
   by Moser–Tardos witnesses; see Item 4.)
3. *Probability space.* The free coordinates `X_ℓ = n mod ℓ^{e_ℓ}` (ℓ∉Π) are independent and uniform on
   units, by CRT. An event `(r,a)` with `v_ℓ(r) ≤ e_ℓ` has probability exactly `1/φ(r)`, and it depends
   only on the coordinates at primes of r. So the dependency graph "share a prime" is a valid LLL graph
   (mutual independence principle).
4. *LLL arithmetic.* Each event has `≤k` free primes. `P(E) ≤ w_ℓ ≤ c_0 = 1/(8k) ≤ 1/8`, so `x_E ≤ 1/4`.
   `Σ_{E'∼E} x_{E'} ≤ Σ_{ℓ|r_E} 2w_ℓ ≤ 2kc_0 = 1/4`, and with `1−x ≥ e^{−2x}` (x ≤ 1/2) this gives
   `∏(1−x) ≥ e^{−1/2} ≥ 1/2`. Then `P(E) = x_E/2 ≤ x_E∏(1−x)`. Next,
   `P(no event) ≥ ∏(1−x_E) ≥ exp(−4S_ev(Π)) ≥ exp(−4S*)`, using `S_ev(Π) ≤ S_tot(Π) ≤ S*`. Correct.
5. *Final arithmetic.* With `z=(log T)²`, `k ≤ log T/(2 log log T)`: the term `π(z)log T ≤ (log T)³`.
   The term `8k²S* log T ≤ 2(log T)³S*/(log log T)²`. The claim `≪ (log T)³(S*+1)` holds, with room to
   spare. Modulo ET, this gives `≪ (log T)^7/log log T`, which is *better* than the stated
   `(log T)^7 log log T` (see D3).

**Does this close PO §9's H_PP problem?** It closes the **purpose** of H_PP, not H_PP itself.
* H_PP(z) is a per-prime bound for the single quarantine `{ℓ≤z}`, and it remains unproved. (PO's own
  Linnik example shows that the naive version fails.)
* Theorem 11.3 bypasses it. Every prime that would violate a per-prime bound is quarantined at cost
  `log T`, and the number of such primes is controlled by the Π-uniform mass S*.
* The polylogarithmic Haar bound that PO Thm 9.4 derived from H_PP is therefore now proved modulo ET
  Prop. 1.4 alone (the same citation PO Lemma 9.2 already used). The `T^{o(1)}` form is unconditional.
* The note's wording ("previously conditional on H_PP") is accurate. Summary item 7 says "the per-prime
  conditions are now free". That is correct for the Haar side, and for (G)/(W) on the prime side; see D4.

**Is the LLL dependency structure right?** Yes; see point 3 above.
* Events sharing two primes are counted once in the true neighbourhood, and at most twice in the per-prime
  bound. That only overcounts.
* Distinct events with the same r and different classes are disjoint. LLL does not care.

**Is every surviving atom covered?** Yes; see point 2 above.

**Defects (Items 1–3).**

* **D1 (minor; §11 summary bullet 7, Thm 11.3 "Remarks", EVIDENCE prose).** Quote: "The iteration stops
  after 2 rounds in every run." The script's `rounds` counter includes the final verification pass. So
  "2 rounds" means **one** round of additions plus one check (confirmed independently, Item 4).
  *Fix:* say "one round of additions; the second pass adds nothing".
* **D2 (minor; Thm 11.3 EVIDENCE).** Quote: "`|𝓑|` grows roughly like `(log T)^{3.8}` here". The data
  (z=20: 99, 171, 345 at T=10⁴, 10⁵, 10⁶) give local exponents 2.45 and 3.85. Moreover k, and hence c_0,
  changes between 10⁵ and 10⁶ (k=3→4). So no growth exponent is supported. *Fix:* drop the exponent, or
  fit at fixed c_0.
* **D3 (minor; Thm 11.3 statement).** The bound `≪(log T)^7 log log T` is weaker than what the proof gives:
  `π(z)log T + 8k²S* log T ≪ (log T)³ + (log T)³S*/(log log T)²`, i.e. `≪(log T)^7/log log T` modulo ET.
  Not an error. *Fix (optional):* state the sharper form, or note the slack.
* **D4 (minor; Thm 11.3 Remarks, 3rd bullet).** Quote: "On the prime side the remaining requirement below
  θ=1/3 is therefore **only** the codegree condition." This is true for the hypotheses of Theorem 10.3
  ((G_k), (W_k) only need fixed constants; Lemma 11.2 at `z=y` gives them with `T^{o(1)}` extra primes).
  But H_CD(θ) as stated in §10.4 still demands `w_ℓ ≤ T^{−ε}`, which is stronger than Theorem 10.3 needs.
  *Fix:* restate H_CD(ii) with `w_ℓ ≤ δ_k/(32k)` (or note that its per-prime part is now automatic by
  Lemma 11.2). Then H_CD reduces literally to "Φ of mass `T^{o(1)}` plus codegrees `≤T^{−ε}`".

## Item 5. Lemma 10.1 (private covers) — SOUND

* Part 1. Take P ⊆ V(x) with |P| = u. Any inclusion-minimal subfamily of A(x) that covers P is a private
  cover. If a member had no prime of `supp E ∩ P` outside the other members, it could be dropped. So
  `binom(N,u) ≤ G^cov_u(x)`. When `A=∅` we have `G^cov_{L+1}=0`, since u ≥ 1 and C ≠ ∅. The rest is
  Lemma 1.2 verbatim. Correct.
* Part 2. In Lemma 1.3(2), `κ(U,c) ≠ 0` forces every prime of U to be covered by events with support in
  U that occur on c. A minimal such family is a private cover of U. Dropping the constraint
  "support ⊆ U" only enlarges the sum, so the bound by `Σ_{|U|≤L} 2^{|U|} E G^cov_{|U|}` holds. Since
  `G^cov` has +1 coefficients, `M_1 = E`. Correct.
* `|C| ≤ |P|`, because the private primes are distinct elements of P. So every term of `G^cov_{L+1}` lives
  on `≤ k(L+1)` primes. This is used correctly in Thm 10.3.
* Script check (`omega2_abstract_check.py`, new `gcov`). It enumerates P ⊆ V and C ⊆ A by brute force and
  tests the private-prime condition exactly as defined. Restricting P to V loses nothing, since a covered
  P lies in V. This is adequate evidence for part 1. Part 2 is not tested, but it needs no test.

## Item 6. Lemma 10.2 (hypergraph moment bound) — SOUND (one unstated step, minor)

The reduction to private families is correct: C privately covers P ⇒ P ⊆ π(C) and |C| ≤ |P| ≤ U_0. The
following are also correct:

* the singles: there is one single per prime, and a single's only prime must be private, hence disjoint
  from the rest of C;
* the components: components are vertex-connected; two components sharing a prime but not a vertex
  have P = 0;
* privacy is inherited by components;
* the "private vertex is new" argument: v and every old vertex already lie in an attached hyperedge
  ≠ e, so none of them is e's private vertex.

The counting checks:

* `Σ_j binom(n,j)Δ^{(j+1)} ≤ D` for `n ≤ kh ≤ kU_0`;
* `(kh)^{h−1}/(h−1)! = k^{h−1}h^h/h! ≤ k^{h−1}e^h = e(ke)^{h−1}`, using padding to kh slots;
* the geometric sum under `(1+w)^k keD ≤ 1/2`.

* **D5 (minor; proof of Lemma 10.2, "Counting", 2nd bullet).** Quote: "The children sets at the at most n
  processed vertices are unordered: `Σ over sets of c children ≤ D^c/c!`". The weight of a child is the
  product over its *new* vertices. Whether a vertex is new depends on the **earlier siblings** (the proof
  says so: "brought by an earlier sibling"). So the child weights are not a fixed function of the child,
  and `(Σ weight)^c/c!` does not apply as written. The claim is nevertheless true, for this reason:
  * the product of the c sibling weights equals `∏_{u∈(∪ children)∖Disc} p(u)`, which is independent of
    the sibling order;
  * hence Σ over sets = (1/c!)·Σ over ordered tuples of distinct children;
  * for ordered tuples, summing sequentially gives `≤ D^c`. At each step the "old" pool is a set of at most
    `kh` vertices, and the next child has a private, hence new, vertex.

  *Fix:* add this symmetrisation sentence. (Without the 1/c! the lemma still holds with a worse constant,
  e.g. `2^{k+1}` in place of e.)

## Item 7. Theorem 10.3 (hypergraph criterion) — SOUND (minor wording)

All constants were rechecked:

* Hub Markov step: `Σ_{v∈H at ℓ} p(v) ≤ w_ℓ/δ_k`, since each hyperedge at ℓ has exactly one vertex there.
  This gives `g^+ ≤ 1/(16k)` and `S_1^+ ≤ S_1+kS_H/δ_k`.
* LLL: for a single, `≥ 1−2w_ℓ`; for a hyperedge, `(1−1/(8k))^k(1−2kδ_k/(32k)) ≥ 0.874`; `λ = 3(S_1^++S_H)`,
  using `−log(1−x) ≤ 1.07x` for x ≤ 1/8.
* Lemma 10.2 at `w=16`: `D ≤ δ_k + δ_k = 2δ_k = [2ek17^k]^{−1}`, once `C_k(Σ+1) ≥ k(L+1)`. This is not
  circular: L is defined from Λ', λ alone, and both are `O_k(Σ+1)`.
* `4^{L+1}EG^cov_{L+1} ≤ 4^{−(L+1)}e^{Λ'}`.
* Twist: the conditional-LLL factor is `1/0.86 ≤ 1.17`, with bracket
  `≤ 1/(16k)+1.17w_{ℓ_0} < 0.073` and `|μ_ψ| ≤ (0.01+0.073/0.927)P(A=∅) < μ/4`.

The prime-power splitting preserves `P, w_ℓ, deg, Δ_O` and "no event"; this was checked, including the
case `ℓ ∉ π(O)`, where the ℓ lifts each carry `1/ℓ` of the weight.

* **D6 (minor; Thm 10.3, Remark (prime powers)).** Quote: "Splitting every class mod ℓ (at primes with
  `e_ℓ=2`) into its ℓ lifts mod ℓ²". For `y=T^θ` with θ < 1/3, the free primes in `(T^θ, T^{1/3}]` have
  `e_ℓ ≥ 3`, and in general `e_ℓ ≤ ⌊1/θ⌋`. Rough parts `ℓ³`, `ℓ²ℓ'`, … occur. The general recipe in the
  Setting ("split into classes mod `∏ℓ^{e_ℓ}`") covers this, but the Remark's "e_ℓ=2", "ℓ lifts mod ℓ²"
  and "rough part ℓ²ℓ'" understate it. *Fix:* "split every class mod `ℓ^a` (a < e_ℓ) into its
  `ℓ^{e_ℓ−a}` lifts mod `ℓ^{e_ℓ}`".

## Item 4. Numerical test of Theorem 11.3's mechanics (independent code) — CONFIRMS

The script `scripts/r3_iterq_mt.py` was written from the statements alone; it imports no subject code.
Data are in `data/review_r3/iterq_mt_*.txt`. It does the following:

* computes `S*` by **brute force over all subsets** of the prime factors of M (the true max over Π, not
  the unitary-divisor shortcut used in `omega2_iterq.py`);
* runs Lemma 11.2. At every stage it checks `w_ℓ(Π_i) ≤ Σ_{atoms, ℓ|M} wt*`, and at the end it checks
  `c_0|𝓑| ≤ Σ_atoms #{ℓ∈𝓑: ℓ|M}·wt* ≤ kS*`;
* checks the asymmetric LLL condition **exactly**: for every event, the product over the union of its
  neighbours;
* computes the certificate `log φ(Q_Π) − log 8 − Σ log(1−x_E)`;
* **end-to-end coverage test.** It runs Moser–Tardos to construct actual coordinates `X_ℓ` with no listed
  event, and puts `n ≡ 1 (ℓ^{e_ℓ})` for ℓ∈Π. Then, for **every** `M ≤ T`, `M≡3 (4)`, and every `D | A²`,
  it checks directly that `n ≢ −4D (mod M)`, i.e. `W(n) > T`.

| T | z | k | c_0 | add. rounds | `|𝓑|` | S* | `c_0|𝓑|` ≤ charge ≤ `kS*` | final max w | S_ev | LLL min ∏(1−x) | certificate | MT: atoms hit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10⁴ | 20 | 3 | .0417 | 1 | 99 | 59.83 | 4.1 ≤ 41.4 ≤ 179.5 | .0414 | 6.73 | 0.922 | 694.6 | 0,0,0 |
| 10⁴ | 85 (=(log T)²) | 2 | .0625 | 1 | 50 | 59.83 | 3.1 ≤ 14.5 ≤ 119.7 | .0621 | 8.37 | 0.886 | 478.6 | 0,0,0 |
| 10⁴ | 5 | 5 | .025 | 1 | 180 | 59.83 | 4.5 ≤ 80.4 ≤ 299.2 | .0249 | 4.31 | 0.952 | 1228.1 | 0,0 |
| 10⁵ | 20 | 3 | .0417 | 1 | 171 | 120.66 | 7.1 ≤ 102.9 ≤ 362.0 | .0401 | 16.94 | 0.924 | 1442.7 | 0,0 |
| 10⁵ | 133 (=(log T)²) | 2 | .0625 | 1 | 77 | 120.66 | 4.8 ≤ 31.0 ≤ 241.3 | .0623 | 20.15 | 0.884 | 966.9 | 0,0 |
| 10⁶ | 20 | 4 | .0312 | 1 | 345 | 217.88 | 10.8 ≤ 222.5 ≤ 871.5 | .0292 | 31.66 | 0.944 | 3499.2 | 0,0 |

* **Negative control.** With `DROP=0.3` (30% of events ignored by Moser–Tardos), the direct check finds 2–3
  hit atoms in every seed (`iterq_mt_negctl.txt`). So the coverage check has teeth.
* **Agreement with the subject.** `|𝓑|`, `S*`, `S_tot(Π)` and `max w_ℓ` agree with `data/omega2/iterq.txt`
  to all printed digits, for all common parameters. In particular, the subject's unitary-divisor
  evaluation of S* equals the brute-force max over Π. Its "LLL max Σx" is the cruder per-prime sum; the
  exact product margin is wider still. Its certificate uses `log Q_Π` and `4S_tot`, which is valid but
  slightly weaker than `log φ(Q_Π)` and `−Σlog(1−x)`.
* **Extra stress test** (not in the subject). With `c_0` forced tiny (0.005 at z=20; 0.002 at z=3, k=8),
  the iteration still stops after **one** addition round. All inequalities hold, and the Moser–Tardos
  witnesses are clean.
* **Observation (not a defect).** The explicit bound `(π(z)+kS*/c_0)log T+4S*` exceeds the certificate by a
  factor ≈ 38–110. The slack is in `kS*/c_0` against the actual `|𝓑|`. The charge sum is only 12–28% of
  `kS*`, and `c_0|𝓑|` is only 5–21% of the charge (bad primes carry far more than `c_0` of S*-weight).

Verdict: the mechanics of Lemma 11.2 and Theorem 11.3 are confirmed at T ≤ 10⁶, and coverage (I) is
confirmed end to end. The subject's `omega2_iterq.py` output is reproduced exactly. Defects D1, D2 above
concern the subject's prose about this data, not the data.

## Item 8. Theorem 10.4 (H_CD(θ) ⇒ H_MIN(θ)) — SOUND (minor)

The proof was checked against H_MIN as stated in PO §6 (`840 | Q`, `log Q ≤ T^{θ+ε}`,
`log max d_i ≤ T^{θ+ε}`, `log(M_1/μ) ≤ T^ε`, twist):

* `840 | Q_Π`, since 2, 3, 5, 7 ≤ y;
* `log Q ≤ (π(y)+T^{o(1)})log T ≤ 2y/θ`;
* `log max d_i ≤ k(L+1)log T = T^{o(1)}`;
* (CD_k) follows from `Σ ≤ S_tot(Π)+m(Φ) = T^{o(1)}` together with `Δ ≤ T^{−ε}`, because `C_k` depends on k
  only;
* (I) still holds once Φ is added as singles.

The 1/κ consequence is PO Thm 6.2 (inherited, already reviewed).

* **D7 (minor; §10.4, after Thm 10.4).** Quote: "For `θ>1/3` (so `k=2`), H_CD(θ) holds with Φ = the hub
  vertices (Lemma 4.3)." Lemma 4.3 does not define a Φ. The hubs are removed *inside* Thm 3.1/10.3
  (Step 1), and H_CD needs no codegree condition when k=2. So `Φ=∅` already works, with `w_ℓ ≤ T^{1−3θ+o(1)}`
  from the crude count. *Fix:* "holds with Φ=∅".
* See also D4: H_CD(ii)'s `w_ℓ ≤ T^{−ε}` is stronger than Thm 10.3 needs, and is now automatic at the
  constant level by Lemma 11.2.

## Item 9. Proposition 10.6 (pair codegrees at `(ℓ,−4d²)`) — SOUND (minor)

* The algebra holds: `ℓ_1ℓ_2ℓ_3 ≡ −1 (4d)` ⇒ `M ≡ 3 (4)` and `4d | M+1` ⇒ `d | A`, so `d² | A²`.
  Also `M ≤ T^{2/3}·T^{1/3}`, and m = 1 survives `Π_0`. The class `−4d² mod M` is the hyperedge
  `{v_1,v_2,(ℓ_3,−4d²)}`.
* The weight beyond O is checked with lifts: there are `ℓ_3^{e−1}` lifts, each of mass `1/φ(ℓ_3^e)`, for a
  total of `1/(ℓ_3−1) ≥ 1/ℓ_3`.
* Mertens in a fixed progression gives `(1/φ(4d))log(log T^{1/3}/log y) = c_θ/φ(4d)`. Correct.
* The proposition is about the `Π_0`-system. After the additional `T^{o(1)}` bad-prime quarantine
  (Lemma 11.2), the lost ℓ_3 change the sum by at most `T^{o(1)}/y`, so the bound persists. Only Φ could
  destroy it, and that is exactly the point of the subsequent discussion.
* **D8 (minor; Prop. 10.6 statement).** The statement does not say in which system Δ is computed (Π_0
  only, or after bad-prime quarantine). Since it is used against H_CD (which is post-quarantine), add one
  sentence: "the same bound holds after quarantining any `T^{o(1)}` further primes".

## Item 10. Proposition 10.5 — SOUND as estimates; label inflated (minor)

* Part 1 was rederived. A hyperedge `e⊋O` has `r = r_O m` with `m > y`, at most `τ*²T/r` atoms, and weight
  beyond O `≤ 1/φ(m)`. Summing gives `Cτ*²T log log T/(q'_O y)`, using `Σ_m m^{−2} ≤ 2/y` and
  `Σ_{r_O} 1/r_O ≪ 1/q'_O`. Correct as an upper bound.
* **D9 (minor; title of Prop. 10.5).** Quote: "the available estimates certify nothing below θ=1/3;
  PROVED". What is proved are the upper bounds in parts 1–2. The claim that "the available estimates"
  certify nothing, and part 2's "For codegrees it gives only `T^{η/(1+η)+o(1)}`, whatever the residue
  pattern", are statements about a method, not theorems. *Fix:* title "crude and Type-I upper bounds for
  `w_ℓ`, `Δ_O` (PROVED); they do not certify (W_k)/(CD_k) below 1/3 (Assessment)".

## Item 11. Proposition 11.4 and §11.4 (G_pair) — Prop. SOUND for fixed D; the consequence needs uniformity (moderate); §§10.4/10.5 vs 11.4 contradict each other (moderate)

* Prop. 11.4 itself is correct, for fixed D. With `D* = ∏p^{⌈v_p(D)/2⌉}` we have `D | A² ⟺ D* | A`, and
  the proof of Prop. 10.6 runs with `4D* | M+1`. The multiplicity count is also correct: each D* has
  exactly `2^{ω(D*)}` D's (`v_p(D) ∈ {2a−1, 2a}`), `φ(4n) ≤ 2n`, and `Σ_{n≤X}2^{ω(n)} ≍ X log X`. For
  **fixed** t, `μ(t) ≥ (c_θ²/2−o(1))·#{D : φ(4D*) < c_θ/t}` follows. Distinct D give distinct vertex
  classes, because `D ≪ 1/t ≪ y`.
* **D10 (moderate; §11.4, "So `μ(1/L) ≫ c_θ³ L log L`").** The previous bullet is stated "for fixed t". It
  is then applied at `t = 1/L → 0`. That requires the lower bound
  `Σ_{ℓ∈R, ℓ≡a (q)} 1/ℓ ≥ (c_θ−o(1))/φ(q)` **uniformly** for moduli `q = 4D*` up to `≍ L log log L`, where
  `L ≍ Σ+1`.
  * Modulo ET, Σ is polylogarithmic. Then Siegel–Walfisz gives the uniformity (ineffectively).
  * Unconditionally, Σ may be as large as `exp(O(log T/log log T))`. Then only an averaged statement over
    D (Bombieri–Vinogradov/Barban–Davenport–Halberstam) is available, and that suffices because μ(t) is
    a sum over D.

  Either way, a sentence is missing. Since the conclusion is labelled Assessment, this is not a false
  PROVED claim. But the label "Assessment, *with a proved lower bound*" overstates what is proved at
  `t ≍ 1/L`. *Fix:* state Prop. 11.4 uniformly for `D* ≤ (log T)^A` (Siegel–Walfisz), and note the
  restriction.
* **D11 (minor; §11.4, 3rd bullet).** Quote: "The circularity therefore closes **iff** `μ(t) ≤ ε/t` …".
  Only "if" is argued. The cost bookkeeping shows sufficiency. Necessity would need a lower bound on the
  cost of *every* way of killing the heavy pairs, not just of pair-by-pair removal. (G_pair(ii) itself
  concedes that cheaper joint treatments are conceivable.) *Fix:* "closes if"; and "the pair-by-pair
  removal fails because …".
* **D12 (moderate; summary item 6, §10.4 last bullets, §10.5 summary vs §11.4 last paragraph).** These
  passages contradict each other:
  * §10.4: "**The open step is therefore a sharper Lemma 10.2** that pays once per shared vertex … not a
    new arithmetic input", supported by the heuristic "`(c²e²/d)^h`. That is harmless for `d≫1`";
  * §10.5: "The more promising route is a sharper Lemma 10.2.";
  * summary item 6: "The open step is a sharper Lemma 10.2.";
  * §11.4: "A sharper shared-vertex Lemma 10.2 does **not** help: a dense cluster with more members than
    shared vertices genuinely carries `(s·c/d)^{h−s}` private families."

  The reviewer's own count supports §11.4 and refutes §10.4's heuristic. Take a fixed d and a family C
  made of s shared vertices `(ℓ_i,−4d²)` and h = L+1 hyperedges `{v_i,v_j,(ℓ_3^{(t)},−4d²)}`, with distinct
  private ℓ_3^{(t)}. C privately covers its h private primes, so it contributes to `G^cov_{L+1}`. Its total
  weight is `≳ (c^s/s!)·(s²c/(2φ(4d)))^h/h!`; the factor 1/2 needed for every shared vertex to be used is
  absorbed once `h ≥ s log s`. At `s ≍ L/log L` the logarithm is
  `L log L − 2L log log L − O_d(L)`. So `E G^cov_{L+1}` itself is **super-exponential** in L, far above the
  `16^{−L}e^{O(Σ)}` that any minorant of the form `B_L − 4^{L+1}G^cov_{L+1}` needs, unless these clusters
  are quarantined. No sharpening of Lemma 10.2's *proof* can avoid this, since the bound would have to
  exceed the true moment. So §11.4 is right and §10.4's `(c²e²/d)^h` (which keeps s comparable to h)
  misses the dense regime `s ≪ h`. (Reviewer's sketch; constants not optimised.)

  *Fix:* withdraw the §10.4 "open step" bullets, the §10.5 summary line and summary item 6 (or mark them
  superseded by §11.4). Give the `(s·c/d)^{h−s}` count a derivation; currently it is asserted without one.
  As it stands, a reader of the summary is told the opposite of the latest finding.

## Item 12. Stale or overstated summary statements — minor

* **D13 (minor; summary item 6).** Quote: "Prop. 10.6 (PROVED): the classes `−4d²` give pair codegrees
  `≍1/φ(4d)`". Only the lower bound `≥(c_θ−o(1))/φ(4d)` is proved; the matching upper bound is not.
  The same applies to §10.5 item 3, "the true maximal pair codegrees are `≍1/φ(4d)`" (also, "maximal"
  is unproved). *Fix:* "≫".
* **D14 (minor; §10.5 "Summary of (a)+(b)" table).** The Haar column still lists the unconditional entry
  as `T^{1/3+o(1)}` (PO Thm 9.3), and the H_CD row as `T^{κ+o(1)}`. Both are superseded by Thm 11.3
  (`T^{o(1)}` unconditionally; polylog modulo ET). *Fix:* update the table, or mark it "as of
  checkpoint 3".

## Replay (reviewer scripts)

```
cd scripts
for a in "10000 20" "10000 85" "10000 5 - 2" "100000 20 - 2" "100000 133 - 2"; do uv run python r3_iterq_mt.py $a; done   # ~1 min
DROP=0.3 uv run python r3_iterq_mt.py 10000 20 - 4                    # negative control (hits must appear)
(ulimit -v 8000000; uv run python r3_iterq_mt.py 1000000 20 - 2)      # ~7 min, ~4.6 GB
```
