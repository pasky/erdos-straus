# Z53_HCHYP — which hypothesis could give HC(p) ≪ (log p)^A? (wave z53, lane HCHYP)

**ES is open. Nothing here proves or disproves ES, conditionally on a standard conjecture or otherwise.**
Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Everything is internally reviewed only.
Scripts `scripts/z53_hchyp_*`, data `data/z53/hchyp/`. Kickoff: `z53_lanes.md` §HCHYP; targets FRONTIER §7.2/§7.4.

*Status: CHECKPOINT 1 (skeleton). Sections marked TODO are filled in later.*

## 1. The statement attacked

**Notation (PROVED equivalences; `LOWERTAIL_ROUND2_FABLE.md` Thm 1, Cor 1.1).** Let p ≡ 1 (mod 8) be prime (for p ≡ 5 (8),
HC(p) = 3 always). Put 𝒞 := {x ≥ 4 : x ≡ 0 (mod 4) or x ≡ 7 (mod 8)}. For x ∈ 𝒞 define the two *lines*
* E_x(p): **p + x has a divisor A ≡ −1 (mod x)** (endpoint line; the word is (t, x, v) with A = tx − 1, v = (p + x)/A);
* L_x(p): **xp + 1 has a divisor d ≡ −1 (mod x)** (level line; the word is (x, u, v) with d = xu − 1).
(The endpoint form here is equivalent to Fable's "uv | n + u + v": given A, put v = (p+x)/A, t = (A+1)/x, then
p + x + v = v(A + 1) = xvt; conversely A := tx − 1 with t = (p + x + v)/(xv).) Then
  **HC(p) = min{x ∈ 𝒞 : E_x(p) or L_x(p)}**, and HC(p) < ∞ ⟺ ES₅(p) ⟹ ES(p).
At an odd square m² every line fails (T1; Fable §1.3; CERTIFIED again here for 5 000 odd squares ≈ 10⁸ and all x ≤ 2048).

**Target S_A (FRONTIER §7.2).** ∃ p₀ ∀ prime p > p₀, p ≡ 1 (8): HC(p) ≤ (log p)^A.

**Lane question.** Find a hypothesis 𝐇, as weak and as natural as possible and *not ES in disguise*, with 𝐇 ⟹ S_A
(or 𝐇 ⟹ R(p) ≥ 1 for large p). For each candidate: (i) the implication, (ii) T1, (iii) numerator 8 (8/131), (iv) numerics at
10⁸–10¹⁶, (v) honest strength. Also: does GRH / GLH / EH / Chowla–Elliott / Hooley R* imply such an 𝐇; if not, the exact
failing step.

## 2. Why this is not already closed

The closed items (brief "Closed", FRONTIER §6) and the existing conditional statements are: H⁻_BM (relative lower tail,
"ES-(★) in disguise", BM_CORRECTED §3.1), Astra's H⁻mom (negative-part moments of the ES count of order L/log L,
LOWERTAIL_DEEP_ASTRA §7), MF₁ (bias of exceptional primes, EXSET_CHAR_FORCING Cor 5.4), Fable's hierarchy (all members
ES₅ plus a size statement; no standard conjecture known to imply any, §4/§6 there), and Conjecture 3.4 (HC ≪ log p). All
of these are *ES-specific* statements. What is not on record, and is the content of this lane:
1. a **calibration** of the target itself: which lines x a hypothesis must control, and at which scale, for S_A to be
   true in the natural probabilistic model (this decides whether Conj 3.4's log p is even the right scale);
2. a **classification of hypothesis shapes** by the regime of lines they act on, with a scoped no-go for the shapes that
   act only on "typical" integers (Erdős–Hall-type statements);
3. the question whether a **general (non-ES-specific) principle** — a statement about all families of divisor-class
   events on affine forms — can imply S_A, and what it must exclude.

## 3. First result (checkpoint): the model scale of HC is (log p)^{2 log 2}, not log p

**Heuristic/model claim (Assessment; a model theorem is proved in §4).** In the Kubilius model (independent prime
factors, residues equidistributed, lines independent), a line x = (log p)^θ succeeds with probability
  P_x = (log p)^{−Q(θ/log 2)+o(1)} for log 2 < θ ≤ 2 log 2,   P_x = (log p)^{1−θ+o(1)} for θ ≥ 2 log 2,
with Q(α) = α log α − α + 1 (Sathe–Selberg). Reason: a line needs 2^{ω(N)} ≳ φ(x) divisor residues to hit the single
class −1 (Erdős–Hall's threshold is exactly φ(x) ≈ (log N)^{log 2}: R. R. Hall, Acta Arith. 29 (1976) 191–196); above
θ = 2 log 2 the success probability is carried by the integers with ω ≈ 2 log log p (the mean of τ), as in
EXSET_CHAR_FORCING §3.2 (the same computation with 3^ω for windows). Summing, the expected number of successful lines
x ≤ (log p)^θ is (log p)^{θ − Q(θ/log 2) + o(1)} < log p for every θ < 2 log 2, and ≍ log p per dyadic block beyond.
Since P(HC(p) > X) ≈ exp(−Σ_{x ≤ X} P_x) in the model, the model predicts
  **max_{p ≤ y} HC(p) = (log y)^{2 log 2 + o(1)} ≈ (log y)^{1.386}**.
Consequences (Assessment, made precise in §4): Conjecture 3.4 (HC ≤ C log p) is false in the model for large p; the
right target is S_A with **A > 2 log 2**; and no hypothesis that only controls lines x ≤ (log p)^{log 2 + ε} (the
"typical", Erdős–Hall regime) can be enough.

**First numerics (EVIDENCE; `scripts/z53_hchyp_lines.c`, `scripts/z53_hchyp_analyze.py`).** Per-line success rates
for 20 000 consecutive primes p ≡ 1 (8) from 10⁸, 10¹² and 10 000 from 4·10¹⁵, all x ∈ 𝒞, x ≤ 2048: the normalised rate
x·P_x/log p rises and then **plateaus** (endpoint lines ≈ 1.1–1.4, level lines ≈ 0.6–0.7), i.e. P_x ≈ c·log p/x in the
mean regime, and the onset of the plateau moves out with p (≈ 128, 256, ≥ 512 at log p = 18.4, 27.6, 35.9). The
independent-lines product underestimates joint failure (ratio 2.7 at X = 7, 10–50 at X = 15–16): line failures are
positively associated — a hypothesis must tolerate this (§5).

## 4. TODO model theorem (precise statement and proof), scoped no-go for typical-regime hypotheses
## 5. TODO hypothesis catalogue (i)–(v); general-principle formulation; standard conjectures and their failing steps
## 6. TODO numerics (full tables, controls: odd squares, near-squares, integers, test primes)
## 7. TODO verdict, four screens, proposed FRONTIER §7 text, bottom line
