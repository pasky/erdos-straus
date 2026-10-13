# AGENT_REPORT_O196 — spark relay Q: is ES firing a Frobenius condition? (FROBENIUS_FIRING.md)

Branch side-agent/frobenius-firing (merged side-agent/ff-mute = O195, CLAIMED). Main file FROBENIUS_FIRING.md;
scripts scripts/ff_frob_selfmute.py, scripts/ff_frob_overflow.py; data data/ff_frob/.
**ES is not solved; no infinite case of ES or ES_q is claimed.**

## SHARP:
1. **Self-mute variant ES^{(y)} is a theorem, and the difference from ES is exactly an exponent cap (§4).**
   ES^{(y)}(n): 4/n = 1/x + 1/y + 1/z where z may have even-power denominators at primes ℓ | y (ℓ ∤ 2n). Thm 4.2:
   holds for every odd n > 1, with Type II shape at every non-square, and is exact-T1 like ES^{(S)}. PROVED relative to
   UNIT_ORBIT Lemma 2.2 (the same sieve as UNIT_ORBIT Thm 2.4: 4 mute primes s_i forced into (r+1)/4 by r ≡ −1 mod s_i;
   reciprocity then makes every s_i a QR, and the sieve gives ⟨S⟩ = squares). Thm 4.4: one mute prime suffices under
   GRH (Lenstra/Hooley; CONDITIONAL, citation-level), also for ES^{(s)} (= O195 spark 1, task (4)).
   Cor 4.3 (PROVED): in the shot family r | n + 4Q², the solution is ES^{(y)} iff rad(Q) | (r+1)/4 and ES iff
   Q | (r+1)/4. So **B2's "the modulus is part of the solution" is harmless when only the radical is constrained
   (fixed Dirichlet modulus 4∏S); the obstruction is the exponent cap** — exponents ≤ log_s r against the
   order ≍ r of ⟨s mod r⟩.
2. **Square-root threshold over F_q[T] (§2, PROVED).** Over F the flip from "P mod f ∈ S" to a condition on f is
   geometric (P mod f = P(α)), valid for characters of every order via Weil, not only reciprocity orders m | q − 1.
   Thm 2.1/Prop 2.2: character-expansion + Weil certifies firing at modulus degree d through a FIXED set S only if
   |S| ≳ n·q^{d/2} (and if |S| ≳ n·q^{d/2}·‖ŝ‖₁); subgroups ‖ŝ‖₁ = 1, fixed-base exponent intervals/boxes logarithmic.
   (Scope: this method; varying bases s(α) are not covered.) The ES
   box has size q^{o(d)} and moving generators (Prop 2.3). This is "how mute must a place be": a fixed algebraic
   sub-structure of size ≥ √|(R/f)^*|·n.
3. EVIDENCE: one mute place S = {3} solves all 78 496 primes < 10⁶ in ES^{(3)} (max shot 9^{18}) and in ES^{(y)}
   (3 | y forced at every j, the stricter statistic; max shot 9^{21}; R196 m1: true ES^{(y)} has j = 0 for 68 655); 0/332 odd squares (T1 control). Overflow scale ES_q^{(s,e)} (z-denominator
   s^{2t}, t ≤ e): 0 unsolved irreducible P over 13 (q, A, n) rows (q = 3, 5, 7; n ≤ 8), max least e = 5, every
   full ES_q failure of data/ffl solved with e ≤ 5 (rerun after the R196 search fix: identical), and the needed e
   does not grow with n (q = 7: max 5, 4, 3, 2 at n = 2..5), while the only known proof (FF_MUTE Thm 3.5) uses overflow n^{2+o(1)}
   (whether less is provable is open).

## Answer to the question (scoped no-go; §1, §3, §6)
* Literal form: Fire(p) is finite (O(p²) moduli), so no finite Galois extension (fixed or p-dependent) gives a
  sufficient Frobenius condition (Prop 1.2, trivial).
* Range-restricted: Thm 1.3 (F_q[T], CONDITIONAL on the cited effective Chebotarev shape; R196 repair m5): genus/degree·ramification ≥ q^{n−k/2}/c₀;
  Thm 1.4 (ℤ, GRH): impossible with [L:ℚ], log d_L ≤ p^{1−ε}. Both are B2/B3 in Chebotarev language (Assessment).
* Constructions F1–F5 (§3): Heegner/ideal dictionary (certificates = degree-1 primes 𝔣 | 1 + 2c√−dp with
  N𝔣 ≡ −1 mod 4cd, PROVED, exact), supersingular-torsion dictionary (every certificate prime is supersingular for
  CM-by-ℚ(√−d) curves, #E(F_f) = f + 1, PROVED, standard), Thue/Minkowski aux-prime template (gives size, not
  divisibility), self-mute (§4), exponent intervals (§5.2). Non-abelian (torsion) fields of moving level give nothing
  over cyclotomic ones: the obstruction is the moving level/small box, not abelianness.

## Self-review (review tool, deep) and repairs, all folded in, marked "R196 #k" in the file
#1 ES_q firing = actual Type II solution (box congruence only necessary over F); #2 Weil main term (q^d − r)/m;
#3 overflow "threshold e ≈ n²" withdrawn (Prop 2.2 needs a fixed base) — replaced by "known proof needs n^{2+o(1)},
smaller open"; #4 overflow search kept only one witness per residue (could miss valid ones) — fixed, grid rerun;
#5 divisor-bound constant; #6 Thm 1.4 constant; #7 CM needs good reduction, lattice count not uniform; #8 Thm 1.3
relabelled CONDITIONAL on the cited Chebotarev shape. The reviewer confirmed Thm 4.2, Cor 4.3, Thm 4.4's disjointness/
Euler product, verify(), and the solution-count bound p^{1+o(1)} (incl. Type I).

## Caveats for the reviewer
* Thm 1.3 cites effective function-field Chebotarev by shape (constants/ramification term not re-checked).
* Thm 4.4 is a citation-level GRH sketch (Lenstra 1977); the density formula's disjointness argument is mine.
* Prop 2.3 compares box size to the threshold; the claim "the method cannot certify" is about the expansion method
  of Prop 2.2 with a FIXED S, not a general impossibility.
* §5.2 e = 0 only sees Type II with modulus degree ≤ D; consistency with data/ffl full-failure lists checked
  (failures ⊆ e = 0-unsolved). FF ES_q has no square-class T1 (FUNCTIONFIELD_ES §4), so squares are not a control
  there; the ℤ T1 control is in §5.1.

## Sparks (not pursued)
1. FF self-mute ES_q^{(Y)}: provable by FF_MUTE Thm 3.5 + the Dirichlet condition f ≡ −1 (mod As)? Reciprocity
   forces s to be an ℓ-th power residue mod f for odd ℓ | q − 1 and (s/f) = ε^{h(d+1)} — so the forced Kummer index
   must be absorbed by matching power-residue conditions on −P/A (FF Lenstra-type entanglement). Worth writing.
2. Exponent-cap interpolation with *growing* cap: allow v_s(Q) ≤ v_s((r+1)/4) + e(r) with e(r) = c·log r — is
   there a sieve (not Weil) that proves this "log-overflow" variant over ℤ? It would sit exactly between ES and
   ES^{(y)}; the Weil threshold says FF needs e ≈ √|f|, but a sieve over r might need far less.
3. Heegner dictionary (F1) with the Gross–Zagier/height viewpoint: 𝔣 | 1 + 2c√−dp is the reduction of the CM
   point attached to (c, d) meeting a specific residue; any equidistribution theorem for reductions of CM points
   *in a fixed residue disc* with level 4cd would be an H-A statement.
