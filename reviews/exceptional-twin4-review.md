# Hostile review: EXCEPTIONAL_TWIN4.md (task O12), branch side-agent/twin-ternary @ e94ee5e

Scope: `EXCEPTIONAL_TWIN4.md` (TW4), `reviews/agent-reports/AGENT_REPORT_O12.md`,
`scripts/twin4_rough_bt.py`. Context: TW3 (Lemmas 3.1–3.4, 6.1–6.2, Prop 6.3,
§6.3), TW3 review rounds 1–2 (E10–E14), TW2 (Setting 3.0, Lemmas 2.1–2.2,
3.2–3.4, 4.1, 5.4). Defects are numbered F1, F2, … (severity: major / minor / nit).

## Item 1. Lemmas 2.1–2.3 (rough-partner Brun–Titchmarsh) — SOUND

Line-by-line check of the proof of Lemma 2.3.
* Split `R = d·n`, d = the Z-smooth part. `Ω(d) = Ω(R) ≤ s` would give
  `R = d ≤ Z^s = Y^{s/(s+1)} < Y ≤ x`, contradicting `R > x`. So
  `Ω(d) ≤ s−1`, `d ≤ Z^{s−1}`, and `n > 1` has all primes `> Z`. ✓
* `(d,q) = 1` from `(R,q) = 1`, so n lies in one reduced class mod q, in
  `(x/d, 2x/d]`; the k with `n = n₀ + qk` lie in `≤ x/(dq) + 1` consecutive
  integers. For `p ≤ Z`, `p ∤ q`, `p ∤ n` excludes exactly the class
  `k ≡ −n₀q̄ (p)`; `ω(p) = 0` for `p | q`. Then
  `J ≥ Σ_{d≤Z,(d,q)=1} μ²(d)/φ(d)` (`ω/(p−ω) = 1/(p−1)`), and
  van Lint–Richert plus `Σ_{d≤Z}μ²/φ ≥ log Z` (valid for `Z ≥ 1`; here
  `Z ≥ 2` because `Y ≥ 2^{s+1}`). ✓
* Numerator: `Y/d ≥ Y/Z^{s−1} = Z² ≥ 4`, so `Y/d + 1 + Z² ≤ 3Y/d`, giving
  `#{n} ≤ 3x/(dφ(q)log Z)` and `Σ 1/R ≤ 3/(dφ(q)log Z)` per d. ✓
* `Σ_d 1/d ≤ Σ_{i<s}(Σ_{w<p≤Z} 1/(p−1))^i` (ω(d) ≤ Ω(d) ≤ s−1; the
  expansion over-counts). `log Z = log Y/(s+1)`. ✓
* Lemma 2.1 (Montgomery's arithmetic large sieve, `(N+Q²)/J`; MV have
  `N−1+Q²`) and Lemma 2.2 (van Lint–Richert) are correctly quoted.
* Remarks (i), (iii) ✓: `Σ_{w<p≤Z}1/(p−1) ≤ log log Z − log log w + O(1/log w)`,
  and with `log Z ≤ L`, `log w ≥ log L` this is `≤ log L` for L large.

**Independent numerical test** (`reviews/exceptional-twin4-check-lemma23.py 4e6 7`;
own code, different sieve algorithms; ~1 min, < 1 GB). `s = 1…5`,
`w ∈ {2,3,7,50,300,2000}`, 30 moduli q (including 30030, 4620, powers of 2,
primes up to 65537, 12 random q < 10⁵), x at the threshold `x = q·2^{s+1}`,
at `x₀+1`, `1.5x₀` and on a ×4 grid up to 2·10⁶, all units b (or 300
random). **631 686 cases, worst `lhs/bound = 0.126`** (worst at the
threshold 0.096). The author's run replays (1228 cases, 0.128). The
constant is loose by ~8×, as expected from `log Z = log Y/(s+1)` and the
factor 3.

No defect.
