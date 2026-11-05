# Z58_DISPROOF — what a counterexample to (MS) would look like; a sibling-calibrated targeted search

Status: wave z58 lane DISPROOF (brief `z52bbriefs/z58_lanes.md` §DISPROOF, common rules `z52bbriefs/z53_depth.md` with
z53 → z58). Internal, internally reviewed only. **ES is OPEN; nothing here proves or disproves ES or (MS).** Labels:
PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_disproof_*`, data
`data/z58/disproof/`.

*(Checkpoint 1: §§0–2 skeleton, falsifier table, statements, engine validation. Results sections are filled in as runs
finish.)*

## 0. MANDATORY FALSIFIER TABLE

The "idea" of this lane is not a proof mechanism but a *counterexample generator*: structured families of primes
(residue designs, square-mimicking, near-squares) that push R(p) down, plus a calibrated zero law that converts the
measured depression into a model zero tail. The table states how the generator and the model behave on each screen.

| screen | how the counterexample generator / zero model behaves |
|---|---|
| **F1 odd squares** | Squares are the *template* the designs imitate. Lemma 2.2 (PROVED): if n is a square modulo M, every (★) solution at n has all three of its moduli 4uB, 4uC−1, 4BC−1 coprime-to-nothing-but *not dividing* M. At n = m² this holds for every M, so R = 0. A prime can be a square mod M only for M ≤ p (in practice M ≲ p^{1/2} to leave a supply of primes), so the design kills exactly the solutions with a modulus dividing M. **Primality enters the model only through the supply: a prime cannot be a square modulo all M; the "unbounded M" limit is the square itself.** The zero law is fitted on primes; it is not applied to squares (it would predict R(m²) > 0 with high probability, i.e. the model is wrong at squares exactly because squares are the M = ∞ design). |
| **F2 C-even sub-line** | Used as the *calibration sibling*: R₈ has CERTIFIED zeros at 10¹⁰ (12 in [10¹⁰, 1.1·10¹⁰]). The same designs are run on R₈ and R; the design boost of the R₈ zero rate (measurable) is compared with the boost predicted from the mean depression. What distinguishes the halves for the model: only the size of the mean (R₈ ≈ 0.075 L², R ≈ 0.15 L²) — so the model says nothing structural about C odd vs even, and a design that zeroes R₈ above 10¹⁰ is *expected*, not news. |
| **F3 composites** | Composites are not in the search domain. Profile (§3) checks whether the 285 composite zeros are "square-like" (square mod many small moduli / small square part) — they serve as a second calibration of "local square-likeness ⇒ zero". The generator never claims positivity at composites. |
| **F4 known zeros** | The zero law is *fitted on* the 14 + 38 zeros (and the R₈ zeros); it predicts them by construction and must not be read as positivity there. Profile (§3): local data of the zeros (class mod 840, n_p, square depth) vs controls. |

## 1. Statements attacked (precise)

* **(MS)** (`Z57_SYNTH.md` §1.1): every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 has R(p) ≥ 1. Internal variant: threshold 10¹⁰.
* **(D1) Counterexample search.** Find a prime p ∈ 𝔐, 10¹⁰ < p ≤ 10¹⁴, with R(p) = 0 (or R_𝔊*(p) = 0), searching only
  in designed progressions. A find would refute (MS) at threshold 10¹⁰ (not at 10¹⁷; not ES — López/other lines must
  then be checked).
* **(D2) Model question.** Is there a structured family 𝔉 of primes (residue design, square-mimicking, near-square, …)
  whose *model* zero tail E_𝔉(> x) := Σ_{p ∈ 𝔉, p > x} P(R(p) = 0) stays ≥ 1 past x = 10¹⁷? Quantified through the
  design depression ρ_𝔉 := E[R | 𝔉] / E[R | control] at matched size and a zero law fitted on data.

## 2. Elementary structure (PROVED)

**Lemma 2.1 (pair-congruence form; PROVED).** For every n ≥ 1, R(n) = #{(u, B) ∈ ℕ² : 4uB | n + u + B} (C := (n + u +
B)/(4uB) ≥ 1 is automatic from n ≥ 1 since n + u + B > 0 — and C ≥ 1 iff n + u + B ≥ 4uB, which holds as soon as
4uB | n + u + B with n + u + B > 0). Each solution (u, B, C) carries three moduli
m₁ = 4uB, m₂ = 4uC − 1, m₃ = 4BC − 1, and it is equivalent to each of
n ≡ −u − B (mod m₁) [given u, B], n ≡ −u (mod m₂) [given u, C; B = (n + u)/m₂], n ≡ −B (mod m₃) [given B, C].
*Proof.* 4uBC − u − B = n ⟺ n + u + B = 4uB·C; and ⟺ n + u = B(4uC − 1); and ⟺ n + B = u(4BC − 1). Positivity of
the third variable is the size condition, automatic for n ≥ 1. ∎

**Lemma 2.2 (square-class shadow; PROVED; the T1 mechanism made modular — essentially known, cf. `Z53_UPPER.md` C3.2,
`RESIDUE_HARDNESS.md` §3).** Let M ≥ 1 and suppose n ≡ s² (mod M) for some integer s. Then no (★) solution (u, B, C) at
n has m₁ | M, m₂ | M or m₃ | M.
*Proof.* Suppose m_i | M. The solution condition for that (pair of) variable(s) is the congruence of Lemma 2.1 modulo
m_i (the size condition is automatic). Since n ≡ s² (mod m_i), the integer N := (s + t m_i)² for t large satisfies the
same congruence, hence (★) has a solution at the square N, contradicting R(N) = 0 (Lemma A.1(b) of `Z57_SYNTH.md`:
every hit class mod d ≡ 3 (4) is a Jacobi non-residue; for m₁ apply that lemma to m₂ of the same solution at N). ∎
*Remarks.* (i) 𝔐 is exactly the set of squares of units mod 840 (units mod 840 squared: 1 mod 8, 1 mod 3, {1,4} mod 5,
{1,2,4} mod 7 — six classes). So (MS)'s domain is the "M = 840 square design" (Mordell's identities cover the rest).
(ii) "p ≡ 1 (mod M)" (class of one) is a special square class.

**Engine (CERTIFIED validation).** `scripts/z58_disproof_eng.c`: per prime, complete levels C ≤ K (S_K), early-exit
decisions of R, R₈, R_odd, R_H3 ≥ 1 by level scans, exact full enumeration (three loops of FAMDESIGN's audited engine)
whenever any is undecided or EXACT=1; the least raw (MS) witness d_min. Validation: reproduces R = 0 at all 14 (★)-zeros,
R_𝔊* = 0 (with R = 2) at the 𝔊*-zeros 11 814 001, 20 445 289, 85 664 329, 564 661 441, and R₈ = 0 with R = 56, 52, 30,
42 at the first four R₈ zeros above 10¹⁰ (exact match with `r8_zeros_1e10.txt`). Speed: 4 ms/prime at 10¹², 12 ms at
10¹³ (decision mode); 12 ms/prime exact at 10¹⁰.

## 3. Profile of the zeros (pending)

## 4. Designs and depression ρ (pending)

## 5. Targeted search above 10¹⁰ (pending)

## 6. Zero model and tails (pending)

## 7. Verdict, screens, proposed FRONTIER text, bottom line (pending)
