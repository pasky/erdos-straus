Result: Hostile review of `notes/z76/PROOF_LIFT.md` (commit eb1dc7988): no FATAL or MAJOR issue. Thm §4 (sterile points for every prime r ≥ 177505) and Thm §5 (dense norm cores) are SOUND as stated.            Label: Assessment
Scope: This review covers §§1–6 of PROOF_LIFT, `scripts/z76_lift.py`, `scripts/z76_sterile.py` and `data/z76/*`. It does not re-certify inherited SE/ZL tables, se_box, zl_sweep or the tail term lists. They are taken as reviewed in SE (R222/R223) and ZL (R231/R232).
Review: Claude (Anthropic; exact model version not exposed), the **same lab** as the author. This does **not** meet the cross-lab gate for a RECORD, so an Astra review is still owed.
Triage: DATA (review)
STATUS delta: none (the gate for PROOF_LIFT remains open: "cross-review owed")

> **Lane provenance clarification (after review):** The mathematical verdict and replays below are the reviewer's unchanged report. The wrapper identifies the reviewer as `anthropic/claude-opus-5-5`, mode `smart`; the authoring lane is OpenAI. The reviewer's inference of common authorship from repository context, including the process comments above and in m3, is incorrect. This is an independent cross-lab review; the threshold improves the repository record, not a claimed externally published record.

## 1. Replays (all byte-identical)
* `z76_sterile.py 558 685` gives `data/z76/sterile.txt` (32 s). With `--explore 544 557`, cell 557 fails at 0.5151 and 553 passes in isolation. 558 is therefore exactly where this certificate stops.
* `zl_sweep.c` (unchanged since O228), `ZL_SHORT=4 X 2X 2X+1 0 32` for octaves 17–20 gives `data/z76/l1_{17..20}.txt` (3/6/16/55 s). A=2X+1 > (X₁+1)/2+1 makes B_A=0, and Y=0 makes the ad≤Y term 0. Octave 21 is reused from ZL (`sweep_21.txt`, Y=300, all rows). Its ADY=3534 agrees with the ZL log `r1_21_l2.txt`.
* `zl_tail.py P 32 800` and `Q 16 100` with SE_W=40 give `data/z76/tail_{P,Q}.txt`.
* New check `scripts/z76_review_lift_check.py`: 0 failures. It has two modes:
  * **No arguments.** It runs exact P-data enumeration for 3⁹, 5⁷, 7⁷, 11⁵, 13⁵, 3¹³, 17⁵, 101³ and 19⁵ (D_P(17⁵)=121 as in M17). For each datum it checks:
    * the centre −f ≡ −h/M mod W with h=a²d, and h|M², h≡−M mod e;
    * per e, #boxes ≤ #h ≤ both compression bounds, with both wheels;
    * the per-band moment bound;
    * s ≤ B−j−1, the per-dyadic-box bound, and the per-pair divcap bound;
    * the total boxes(B).

    It also runs random tests. These cover the compression lemma for every g|M with g≤e (and g²≤e), the short-interval bound (1) against exact τ sums for all k and both wheels, and divcap against adversarial V=lcm(uz_i−1).
  * **Argument `band`.** It compares exact compressed h-counts with the band bounds at N=r³≈2⁶⁰ for i≤9. The bounds are loose by a factor of 10⁵ to 10⁷, and there are 0 violations.

## 2. Mathematics checked line by line
* **§1.** Centre: bf=Nc+a gives f≡a/b mod N. h=Ma/b=a²d divides M². a≡−b mod e gives h≡−M. Both orientations are divisors in the same class. Splitting h=h₀h₁ via h₀=gcd(h,g²) is valid primewise. For fixed h₁ the class of h₀ is a unit class because gcd(M,e)=1. Each of the [1,e] and [1,g] uniqueness arguments is correct. Wheel condition: g≤G≤2^{⌊i/2⌋} gives g²≤2^i≤e, and G≤2^i≤e for cost 2.
* **§2.** H=⌈2^i/4⌉ consecutive M, and M≤m. v_ℓ(M/g)=max(0,v_ℓ(M)−α_ℓ). The successive ratio ((2t+3)/(2t+1))·ℓ^{−1/k} decreases in t, so the loop `while (2t+3)^k > p(2t+1)^k` captures the running maximum. For ℓ≥3^k we have 2t+1≤3^t, so F≡1 there.
* **Rounding.** V=max(F, ⌈(U^k(2t+1)^k/p^j)^{1/k}⌉) (rootup verified to return the exact ceiling of the k-th root). The increments are differences of the *rounded* F, so ΣΔ telescopes exactly to the rounded F(ℓ^∞), and Δ≥0. mass, A and B are all ceil-rounded. Σ_{M∈I}F ≤ Σ_dΔ(d)(H/d+1) is valid.
* **§3.** From e≤2b/c and 4abd=N+e we get 2acde≤N+e. This gives both acd≤(N/e+1)/2 and e≤N/(2acd−1). Then 2^{s+1} ≤ 2^{B−j}+1 forces s≤B−j−1.
  * Route A: ⌊X/q⌋+1 with q=4·2^{x+y}≤4ad is safe.
  * Pair routes: V≤3N<2^{B+2}, Nc+a<2^{B+z_c+2} and 4c²dN+1≤2^{B+2z_c+y_d+6} are correct. uz−1≥2^{b+l−1} holds.
  * Determinant: f_i|V₁ (gcd(f_i,u)=1) and f_i|z_i−v. Row i is divisible by f_i^h. det = V₁^{h(h+1)/2}·Vandermonde, and differences are ≤2^t−1, so the strict inequality is safe. This is a sound, Minkowski-free variant of SE Lemma 1.3.
  * `divcap`: l=⌊(R−1)/v⌋ is exactly the largest t with vt<R.
* **§4.** The union-measure criterion is weaker than SE (S) and is valid. The note says so correctly.
  * Cell mapping: i·q//32 for q∈{1,4}, b=i//32+1 ≥ (i+1)/32, and the least r in each weight.
  * The l1 assertion checks endpoints and saturation. Tables are padded by 10⁻⁹ (tables have 11 significant digits).
  * Tails: G_P=0.013618≤0.014 and G_Q=9.02·10⁻⁶≤10⁻⁵. e≤0.4797<0.48 and e≤0.7500<0.76.
  * The log power p≤2 holds by inspection of `zl_tail.py`: only route A has LA·LA, with p=2. It is **not printed or asserted** by the script (see m2).
  * Log ratios: −0.0328·ln r < ln 0.8 for r≥900, and −0.42·ln r < ln 0.5. Hence the tails are ≤ 2·5·G_P/√r ≤ 0.137/√r and ≤ 4G_Q ≤ 3.61·10⁻⁵. The charged 0.16/⌊√r⌋ + 4·10⁻⁵ covers both.
  * Starting the tail at each r's actual first tail level is consistent with the truncated finite loop.
* **§5.** The following steps all check out:
  * Cox Thm 9.4: q∤2D, q=x²+Dy² ⇔ q splits completely in the ring class field.
  * L∩ℚ(ζ_u)=ℚ, because u is unramified in L and totally ramified in every subfield of ℚ(ζ_u).
  * The density is 1/([L:ℚ](u−1)).
  * The witness identity is (q+1)v−u−v=qv−u=p.
  * Signs: (q/p)=(p/q)=(−u/q)=(q/u)=(−1/u)=−1, using p≡1 mod 4 and u≡3 mod 4. The (−1/q) factors cancel, so q need not be 1 mod 4.
  * Moduli: mq and mqq′ are at most mX^{2/5}, which is inside the BV range. Each pair modulus is counted at most twice.
  * Var ≤ B+o(1), since the first-moment error O(log^{1−A}X) times B≪log log X is o(1). Chebyshev then applies, followed by dyadic assembly.
  * The result is consistent with, and not contradictory to, z75 PROOF_WILD2 §2, which explicitly excludes α=1 norm catalogues.

## 3. Must-fix
None in the mathematics or the code.

## 4. Should-fix (form, scope)
* **m1. Inherited caveats are not restated.** Thm §4 also inherits two caveats that the note does not repeat:
  * ZL R232 m7: the `P_q1_hi` rows 600–799 (coarse boxes) were never independently re-checked.
  * se_box's x87-libm accuracy assumption.

  Both affect only negligible terms here, but they belong in the Scope line or §4 next to "Dependencies … as in ZL".
* **m2. "Log powers are ≤2 (`zl_tail.py`)" is an inspection fact, not script output.** Either say "by construction (route A, LA·LA)" or add an assertion. The ratio argument for the tails depends on it.
* **m3. Triage and STATUS framing.**
  * §5 is not a RECORD. It is a complement to the z75 thin-core barrier, i.e. a METHOD-CX or FRONTIER-scope line at FRONTIER ll. 124–125.
  * It should say explicitly that density-one statements for ES are classically far stronger (Vaughan-type almost-all results), so it carries no information about the ES exceptional set.
  * The RECORD part needs an Astra review before STATUS l. 98 ("r ≥ 2.84·10⁶") is replaced by 177505.
* **m4. Obscure sentences.**
  * §5: "At an odd square no coprime q can give Jacobi −1 in the denominator-square symbol" is unclear. Rewrite it or drop it.
  * §4: "the coupon saved in §1" is jargon.
* **m5. `z76_sterile.py` bounds.** The hard cap `j1≤685` and `j0≥384` is undocumented. It reflects the available l1 files (17–21) plus ZL for j≥686; say so in the docstring.

## 5. Debate and challenges (not defects)
* **Where the gain comes from.** Near N≈2⁶³ the new uniform P bound is ≈62√(2⁶⁴), against SE's 2·P_q4 ≈ 2.98·10¹², a factor of about 11. That is enough to move the K=3 term from binding (ZL: S=0.65 at j=672) to 0.06.

  The gain comes mainly from compression: one divisor h of M² per box, instead of τ₃-type and route-F envelopes. The bound is still about 10⁵ times above the truth per small-e band (§1 `band` test). It is dominated by the end-effect product ∏F(ℓ^∞) and M^{1/k}. The certificate is honest, but it remains far from the true counts.
* **Cheap further gain.** `boxes(b)` is uniform for N≤2^b with b=⌊i/32⌋+1. Every K=3 cell just above an integer b therefore pays up to √2 (visible as jumps at j=554, 565, 576, …). A non-power-of-two n (s-layer bound from ⌊log₂((n/2^j+1)/2)⌋) would plausibly lower the threshold a few cells more. Q at level 1 and P at K=3 then become the binding terms.
* **r=17 stays out of reach.** The note says this correctly. The uniform bound is ≥25√N everywhere it is used, while M17D needs about 2.5·17^{0.4K}.
