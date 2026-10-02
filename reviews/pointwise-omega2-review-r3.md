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
| **Theorem 11.3** (`log(1/δ*) ≪ (log T)^3(S*+1)`) | **SOUND** (minor defects only) |
| (filled in item by item below) | |

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
