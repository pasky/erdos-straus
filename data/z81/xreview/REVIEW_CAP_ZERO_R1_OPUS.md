<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of lane z81-cap-zero (notes/z81/CAP_ZERO.md). The author is a GPT-6.2 Astra lane. Verify every theorem, reduction, exponent, hypothesis, falsifier screen (F1–F4), and scope claim. Check closely for hidden circularity, unproved assumptions, overflow accounting errors, or disguised B2 re-encoding. Cap any computational replay to ≤ 15 minutes.

Commit log:
commit 173a7363407eab7444e29f847225916f5f6f2d5d
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 14:49:09 2026 +0100

    Build single-prime inverse packets at the QR cap and bound high-power planting on thin profiles

 data/z81/cap_zero/probe.txt |   6 +++
 notes/z81/CAP_ZERO.md       |  82 +++++++++++++++++++++++++++++++++++
 scripts/z81_cap_probe.py    | 103 ++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 191 insertions(+)

Review:
I reviewed lane z81-cap-zero, commit `173a73634` (`notes/z81/CAP_ZERO.md`, its probe script and data). **Verdict: the mathematics holds; eight presentation fixes (F1–F8) are needed before export.** I found no mathematical error, no circular argument, no overflow accounting mistake and no disguised B2 re-encoding. I worked through every proof step and checked the key arithmetic by computer, within the time cap.

**What I checked**
- **Lemma I (the single-prime packet):** the conditions on the window, the lift fix that multiplies by F=s²−s+1, p∤F, and coprimality all hold. The denominator of z is exactly s^(h−1), and s divides y. No other prime can appear in the denominator.
- **Theorem I (same rates as z80 QR, root on one prime):**
  - Switching the supply primes to t≡3 mod 4 still gives main coefficient 1/(2φ(d)).
  - Since (t−1)/2 divides h with odd quotient, each retained t divides s^h+1.
  - The large-sieve count of discarded carriers has exponent about .994, which leaves surviving carriers.
  - The random-subset Fourier coefficient at the quadratic character η is exactly 0; the others are at most e^(−.08P). This forces an odd-size product hitting −p.
  - The supply set T depends only on U, not on p, so there is no hidden adaptivity.
  - The finitely many small radicals are covered by the z75 free carrier, which also uses one prime.
  - The rate matches QR (14), and the GRH and Montgomery branches match z80 §12.
- **Lemma H:** correct. A brute-force run over 914,161 cases found no violation.
- **Jacobi remark:** this is a correct reading of `CAP_BOUNDED.md` Lemma 1.1 at δ_p=0.
- **Theorem T:** the guaranteed exponent max(1, j−2C) follows exactly from `CAP_DOWN.md` Lemma 3.1. The size step G ≤ 20W³, the single-class Brun–Titchmarsh test and the candidate sum are all correct.
- **Prop S, the p=2521 obstruction and the Dickson family:** correct. I checked 2521 by hand: the residues {2,3,2} with exponents in {−1,0,1} reach {1,…,9} mod 11 and miss 10. The Dickson forms are admissible.
- **Falsifier screens F1–F4:** every entry in the table matches the probe output, and the odd-square argument (9a²+4 is a sum of coprime squares) is right.
- **Replay:** the lane's probe reproduces `probe.txt` byte-for-byte in 0.2 s. My independent script builds 567 Lemma I packets from real factorisations of s^h+1, up to h=45 and including the lift, and all satisfy the relaxation exactly.

**Points the note should address**
1. **Limit of its own method is unstated.** The z80 §12 divisor barrier applies unchanged here. Covering the residues mod s needs about U synchronised primes, which forces log L ≫ log U·log₂U. So this route cannot reach a polylog cap.
2. **Lemma H should be applied to Theorem I's own carriers.** On the unconditional branch s ≥ p^(D/2), so Lemma H gives h ≤ 4E+1. Planting more of s into K could improve the cap by at most a factor of 2 in this pattern.
3. **Theorem T does not reach Theorem I's unconditional carriers.** T only covers support primes up to (log p)^D, while the unconditional carriers are around R^D. On the GRH branch T applies, but the cap there is (h−1)/2 and unbounded, so there is no conflict. The Assessment after T should say this.
4. **Credit is missing.** Theorem I is a markedly simpler proof of QR's rates: no pivot prime, no binary basis, no bad-conductor sieve.
5. **The file name oversells.** "CAP_ZERO" fits only §2; nothing reaches cap zero.

**Form fixes owed (F1–F8)**
- **F1:** §0 triages only Theorem I as RECORD. It needs a BARRIER-SCOPED entry for H/T, merged with the z80 ST line in FRONTIER §6, and a METHOD-CX entry for the fixed-x obstruction, with proposed §6 text.
- **F2:** The Label should mark the z75/z80 inputs as internal and unrefereed, and say "ineffective". The proof uses Thorner–Zaman Thm 1.4 plus Stark, not "effective Linnik".
- **F3:** The Theorem I statement should say s is prime, s∤n, r=s^e and e=(h−1)/2.
- **F4:** The STATUS delta needs a pointer to the note and "cross-review owed" until a second review. The §1B item is already at its 6-line cap, so something must be compressed.
- **F5:** Theorem T's modulus M must explicitly include 2^H, or A|M fails at l=2.
- **F6:** The letter y is used both for the Maynard scale and for the ES denominator.
- **F7:** Two sentences are unclear and should be clarified or deleted: "This is why simply treating the adaptively selected t's as independent samples would be wrong" and "Here is the deterministic size step that a mere union bound on m would miss".
- **F8:** The note's Review line should point to the review file below.

I committed the review and my replay script in `3d0af7c2b`:
- `data/z81/xreview/REVIEW_CAP_ZERO_OPUS.md`
- `scripts/z81_xrev_cap_zero_opus.py` (runs in about 6 s)
</code-review>
