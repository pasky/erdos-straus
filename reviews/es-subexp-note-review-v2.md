# Referee report R33b — paper/es-subexp-note.tex, Draft v2 (branch side-agent/omega-paper-v4)

Referee: hostile side agent (R33b). Scope: everything changed/added in v2.
Status: COMPLETE (round 1).

## Recommendation: MINOR REVISION
The v2 upgrade (exponent 1/14 → 1/7, constant 1/(2log2) → 1/log2) is
correct. I re-derived every step of the linear transfer theorem. I also
checked the quoted Gallagher statement verbatim against the archived MV III
draft, including its proof, and re-checked the parameter chains. No FATAL
defect. One MAJOR defect (M1): the cited exceptional-zero statement, Thm 3.1,
is false as literally written because it has no height restriction. It has a
one-line repair and no downstream effect. There are six MINOR points.
All new numerical constants were re-checked from scratch in
scripts/review_r33b_numerics.py.

| Claim | Verdict |
|---|---|
| Thm 3.1 (exceptional zero, Page bound) | GAP (statement; M1), repair trivial |
| Thm 3.2 (Gallagher, quoted from MV III 28.19) | SOUND as a quotation; caveat paragraph m1 |
| Thm 4.1 (linear transfer), full proof | SOUND-AFTER-REPAIRS (M1, m1, m2) |
| Lemma 5.4 (cells), Lemma 5.5 (ℓ¹-tightness) | SOUND |
| A ≤ 1+2/99 < 1.03 | SOUND |
| Thm 7.1 (assembly) | SOUND (m5, m6 wording) |
| Thm 1.1 (exponent 1/7) | SOUND modulo cited inputs |
| Thm 1.2 (constant 1/log 2) | SOUND modulo cited inputs |
| Novelty paragraph | adequately hedged; add comparators (m4) |
| Bibliography (Gallagher, MV III) | data plausible; Gallagher unseen (m3) |
| Consistency with unchanged parts | no stale TZ/M_1/K references found |

## Verdicts per claim (filled in as checked)

### Thm 4.1 (linear transfer), proof as written — line-by-line
- Character expansion c(χ)=E_D[B χ̄_D]/φ(Q): re-derived (sum over n≡1 mod Q
  units of QD, χ̄_Q(1)=1, CRT gives φ(D)/φ(QD)=1/φ(Q)). CORRECT.
- (a) conductor support: χ_D trivial on ker((Z/D)^×→(Z/d_i)^×) ⇔ χ_D factors
  mod d_i ⇔ cond(χ_D) | d_i. cond(χ) = cond(χ_Q)cond(χ_D) ≤ Q d_i ≤ Z. CORRECT.
- (b) |c(χ)| ≤ E_D|B|/φ(Q), c(χ_0)=μ/φ(Q). CORRECT.
- (c) twisted coefficient = μ_ψ/φ(Q) (cells with f∤d_i vanish by (a)). CORRECT.
- ≤ Z² characters: χ↦χ* injective at fixed modulus QD, #primitive mod q ≤ φ(q),
  Σ_{q≤Z}φ(q) ≤ Z². CORRECT.
- log(QD) ≤ 2Z: log Q ≤ Q, log D ≤ ψ(max d_i) < 1.04 max d_i (Rosser–Schoenfeld;
  citation not given — MINOR), sum ≤ 2Q·max d_i. CORRECT.
- |R_1| ≤ 2AZ³μ/φ(Q). CORRECT.
- Case 0 numerics: C_G A e^{-L} ≤ A/(400(A+1)) < 1/400; second term ≤ 1e-4. CORRECT.
- Exceptional case: u<L, u ≤ min(u,1)L (L≥2), Le^{-3L}≤e^{-L}. CORRECT.
- Case A: λ ≥ (1-e^{-1}-2/16)min(u,1) = 0.507 min(u,1). CORRECT (checked numerically,
  scripts/review_r33b_numerics.py). 1/λ ≤ 2+2/u ≤ 2+c_2 Z^{1/2}(log Z)²/8 uses
  q_1 | Q ≤ Z and Page bound. CORRECT given Thm 3.1.
- Case B: |c x^β/β| ≤ (μ/4φ(Q))·2x. CORRECT.

### Thm 3.2 (Gallagher) vs source — SOUND (statement), caveat paragraph needs repair
Checked against sources/omega9/montgomery-mnt3.pdf, Thm 28.19 (pp. 229–232 of the
draft incl. proof). The quoted statement matches verbatim: hypotheses κ≥κ_0,
1<Q^{6c}≤x (NO upper bound on x — so the choice Q_G=x^{1/(κL)} with L unbounded
is legitimate), main RHS, exceptional replacement θ(x;χ_1)+x^{β_1}/β_1 (sign
correct w.r.t. the explicit formula), replaced RHS. The implied constant may
depend on κ (proof ends with exp(c/κ')), so "≪_κ" is right.
The proof's case split is at 1-β<1/(κ_0 log T)=1/(3κ_0 log Q) (Case 1) vs
1-β_1<1/(κ' log T)=1/(κ log Q) (Case 2). Re-derived: Case 2 as printed works for
ANY real zero with 1-β_1<1/(κ_0 log T) (its last step needs only
log(κ_0/c_0)≥3c, guaranteed by (28.91)); and for κ≥3κ_0, if such a zero has
1-β_1 ≥ 1/(κ log Q), the Case-2 bound plus x^{β_1}/β_1 ≤ 2x e^{-log x/(κ log Q)}
and (1-β_1)log x·e^{-log x/log Q} ≤ (log x/log Q)e^{-log x/log Q} ≪ e^{-log x/(2 log Q)}
yields the non-exceptional bound. So the theorem holds for every κ≥3κ_0.

### Thm 3.1 (exceptional zero statement) — GAP in the statement (easy repair)
Checked: MV III (28.61)–(28.62) (draft p. 216–217) say "F(s,T)=∏_{q≤T}∏*L(s,χ) has
at most one zero s with Re s>1-c_1/log T", with NO height restriction and no
stated range of T. The paper copies this ("for every Y≥3"). As literally stated
(no bound on Im s) this is NOT a known theorem: it would give a zero-free
region σ>1-c_1/log Y for each fixed L(s,χ) uniformly in |t|, far beyond
Vinogradov–Korobov. MV's own source, Cor. 11.10 of vol. I (not accessed by me;
MV III p. 193 paraphrases it as "at most one zero ρ=β+iγ to be counted
[i.e. |γ|≤T] with β≥1-c/log 2QT"), has the region σ ≥ 1-c/log(Q(|t|+2)) or a
height cutoff. The paper only uses real zeros (uniqueness of the real
Gallagher zero, reality/quadraticity of χ_1, Page bound), so nothing
downstream breaks. See defect M1.
The Page bound δ_1 ≥ c_2^{-1}q_1^{-1/2}(log q_1)^{-2} is the standard effective
bound for any real zero of a real primitive L(s,χ) (Davenport ch. 14), valid
for every q_1≥3 independently of Y — correct.

### Thm 4.1 parameters paragraph — SOUND
log Q_G = log x/(κL) ≥ (C_2/(κC_3)) log Z; Q_G ≥ 10^4C_G(A+1)(κL)^2 uses
A ≤ Z^{1/4} (so RHS ≪ Z^{1/4}(log Z)^2); κL ≥ 3·2c=6c gives Q_G^{6c} ≤ x;
x ≥ C_4AZ^4 since log A ≤ (1/4)log Z. No circularity (C_G fixed by κ first,
then L, then Q_G). All constants effective (c_2 Page constant effective).
Overall verdict Thm 4.1: SOUND-AFTER-REPAIRS (only M1 on Thm 3.1 and minor
citation points).

### Lemma 5.4 (cells), Cells paragraph, Lemma 5.5 (ℓ¹-tightness) — SOUND
B^- ≤ F-B because F ≥ 0 and B ≤ F; E|B| = EB+2EB^-. Haar mean = E_D because
D=lcm d_i is a product of full prime powers ℓ^{e_ℓ} of free primes, and the
reduction map (Z/D)^× → ∏ G_ℓ is a bijection. gcd(d_i,Q_Π)=1 since 2,3 ∈ Π
(z ≥ 7). Hypothesis "B(n) ≤ 1[W(n)>T] for n≡1 (Q), gcd(n,d_i)=1" follows from
Lemma 5.4's integer identity + Lemma 5.3 (B≤F on ∏G_ℓ) + Lemma 2.7(iv).

### Thm 7.1 (assembly), A ≤ 1.03, parameter chain to 1/7 — SOUND
- E[F-B] ≤ δ/100 ≤ μ/99 (μ ≥ 0.99δ) ⇒ A ≤ 1+2/99 ≈ 1.0202 < 1.03 ≤ Z^{1/4}
  (Z ≥ 1.126 suffices). CORRECT.
- log Z ≤ log Q_Π + log 2 + 2(3k+2t)𝓛 (log ℓ_aux ≤ log 2 + max(𝓛, log max d_i));
  |𝓑| ≤ kS*/c_0 = 64k²S*; log 24 + log 2 < 4. CORRECT.
- ℓ_aux > max d_i ⇒ gcd(d_i,Q)=1; p ≡ 1 (ℓ_aux) ⇒ p > T; 840 | Q_Π ⇒ hard. CORRECT.
- z=𝓛²: k ≤ 𝓛/(2log𝓛), k_0 ≪ S*+k𝓛 ≪ 𝓛⁴log𝓛, t ≪ k·𝓛·k_0 ≪ 𝓛⁶,
  k²S*𝓛 ≪ 𝓛⁷/log𝓛, t𝓛 ≪ 𝓛⁷ ⇒ log p ≪ 𝓛⁷ ⇒ W(p) > T ≥ exp(c(log p)^{1/7}). CORRECT.

### Thm 1.2 (constant 1/log 2) — SOUND
log S* ≤ (log2+o(1))𝓛/log𝓛 (Lemma 2.4(a)); every other factor is 𝓛^{O(1)}, so
log log p ≤ (log2+o(1))𝓛/log𝓛. L/log L ≥ Y ⇒ L ≥ Y (log L ≥ 1) ⇒ L ≥ Y log Y,
and log Y = log₃p + O(1). The v1 constant 1/(2 log 2) came from TZ's
K·max(log Z,K) ≍ (S*)²; with the linear transfer log p ≪ log Z ≍ S*·poly(𝓛),
so 1/log 2 is the right constant. CORRECT.

### Compilation
pdflatex (2 passes, out-of-tree build): 18 pages, no warnings, no overfull
boxes, no undefined references.

## Numbered defects

**M1 (MAJOR, easy repair) — Thm 3.1 as stated is not a theorem.** Location: §3,
Thm 3.1 ("for every Y ≥ 3, ∏_{q≤Y}∏*L(s,χ) has at most one zero with
Re s > 1-c_1/log Y"). Without a height restriction this asserts a zero-free
region of width ≍1/log Y uniformly in |Im s| for every L(s,χ), q ≤ Y — unknown
(stronger than Vinogradov–Korobov). MV III's "Exceptional Zero Statement"
(28.61) has the same omission; its cited source (MV I Cor. 11.10, which I could
not access; MV III p. 193 paraphrases it with |γ| ≤ T and β ≥ 1-c/log 2QT)
has a height cutoff. This answers the author's flagged point: the issue is
not the range of Y (any Y ≥ 3 is fine) but the missing |Im s| bound.
Repair: state "at most one zero in the region σ > 1-c_1/log Y, |t| ≤ Y" (or
σ > 1-c_1/log(Y(|t|+2))), cite MV I Cor. 11.10 / Davenport Ch. 14 for it, and
add one sentence: "We use only real zeros." Nothing downstream changes (the
proof of Thm 4.1 uses only: uniqueness of a real zero with 1-β<1/(κ log Q_G),
reality/quadraticity of χ_1, and the Page bound).

**m1 (MINOR) — source-caveat paragraph is self-inconsistent.** Location: §3,
"We fix κ := max(3κ_0,1/c_1)" and "Source caveat ... its two cases match as
written only for κ=3κ_0. That is why we fix κ ≥ 3κ_0." If the printed proof
only works for κ=3κ_0, then κ=max(3κ_0,1/c_1) > 3κ_0 (possible when 1/c_1 > 3κ_0)
is not covered by that sentence. Two repairs, either suffices: (i) note that
(28.91) only imposes lower bounds on κ_0, so one may enlarge κ_0 to
max(κ_0, 1/(3c_1)) (MV's "c_1" in (28.91) is presumably a slip for 1/c_1) and
then take κ = 3κ_0 exactly; or (ii) add the monotonicity argument (verified by
me): MV's Case 2 works for any real zero with 1-β_1 < 1/(3κ_0 log Q), and if
such a zero has 1-β_1 ≥ 1/(κ log Q) with κ ≥ 3κ_0, then x^{β_1}/β_1 ≤
2x e^{-log x/(κ log Q)} and (1-β_1)(log x)x e^{-log x/log Q} ≪ x e^{-log x/(2log Q)},
so the non-exceptional bound holds; hence the theorem holds for all κ ≥ 3κ_0.

**m2 (MINOR) — uncited explicit Chebyshev bound.** Location: proof of Thm 4.1,
"log D ≤ 1.04 max d_i". Cite Rosser–Schoenfeld (ψ(y) < 1.03883y), or use the
elementary log D ≤ ψ(y) < 2y log 2 (Chebyshev/Erdős: ∏_{p≤y}p < 4^y, plus
prime powers via log D ≤ π(y)log y) — any bound log(QD) ≤ CZ suffices, at the
cost of the constant in x ≥ C_4AZ⁴.

**m3 (MINOR) — Gallagher's original not seen; "Thm 7" number unverified.**
Location: Thm 3.2 header, bibliography [Gallagher]. The bibliographic data
(Invent. Math. 11 (1970) 329–339, "A large sieve density estimate near σ=1")
match my recollection. From memory (UNVERIFIED), Gallagher's Thm 7 may carry a
range of the form exp(√log x) ≤ T ≤ x^b. The use here is robust to that:
log x/log Q_G = κL ≪ 1+log A, and log x ≥ (κL)² follows from the hypothesis of
Thm 4.1, so Q_G ≥ exp(√log x); in the application κL is O(1). Suggest one
sentence saying so, so that the result does not hinge on the draft's range.

**m4 (MINOR) — novelty paragraph: closest comparators missing.** Location:
§1 "Relation to the literature", sentence "Here it serves as a transfer device
for an arbitrary signed combination of progressions". The nearest classical
analogue is the least prime in a union of residue classes / in a Chebotarev
class of an abelian extension (Lagarias–Montgomery–Odlyzko 1979;
Thorner–Zaman, Linnik-type Chebotarev bounds), which also bound the least prime
by a power of the conductor via a log-free zero-density/Deuring–Heilbronn
argument. Those are for nonnegative indicators. What is new here (as far as I
can tell) is a signed minorant whose cost is A = E|B|/E B. Suggest citing
LMO/TZ-Chebotarev as comparators and keeping the hedge.

**m5 (MINOR) — compressed step in Thm 7.1.** Location: proof of Thm 7.1, "Since
m² ≤ T^{2k+4} and S ≤ S*, Lemma 6.2 gives the bound of Corollary 6.3 at this
k_0". Corollary 6.3 is stated with its own k_0 (in terms of m, S), which differs
from the assembly k_0 (in terms of T^{2k+4}, S*). The step is right (the proof of
Cor. 6.3 goes through verbatim: 4·2^{-k_0} ≤ e^{-3S*}/(100T^{2k+4}(S*+1)) ≤
e^{-3S}/(100m²(S+1))), but the sentence should say so. Alternatively, restate
Cor. 6.3 for any k_0 ≥ its value. (v1 had an explicit monotonicity sentence.)

**m6 (MINOR) — case m=0.** Location: proof of Thm 7.1, "If m=0 put B=1". The
following sentences (Lemma 6.2, Lemma 5.6) are then vacuous/irrelevant; say
"(then A=1, D=1, and the twist condition is vacuous)".
