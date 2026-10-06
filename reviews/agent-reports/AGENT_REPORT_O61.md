# AGENT REPORT O61 (branch side-agent/third-conditional) — checkpoint 1

Deliverable: `POINTWISE_OMEGA16.md` (§§0–7, Replay), scripts `scripts/omega16_{buchstab,esleast,adversary}.py`,
data `data/omega16/`.

## Main results
1. **Hypothesis LS(C)** ("Linnik's theorem for sifted sets"): every unit-class sieve system with moduli
   `≤T` and avoider density `δ>0` contains a prime `p>T` with `log p≤C(log T+log(1/δ))`. Reduces to
   Linnik for one class; log-scale random-set model.
2. **Thm 1.2 (PROVED implication, modulo NT via O13 Thm 3.4):** LS ⇒ `W(p)≥exp(c(log p)^{1/3}(log log p)^{−5/3})`
   for infinitely many Mordell-hard p. Short proof: O13's density bound + LS for one system per T.
3. **Item (i):** EH/GEH/GRH/BV-type inputs (moduli `≤x`) through linear certificates cap at 1/4 (Prop 3.1,
   zero-error planted fake). Main-term forms of "primes in sifted sets" are too strong: AS false in the integer
   analogue (Buchstab), PS/AS heuristically false for primes by a compounding `(e^γω(u))^κ` deficit (Prop 2.1;
   numerics to 1e9 confirm compounding).
4. **Item (ii):** Hardy–Littlewood for CRT-product sets gives exactly `W=(log p)^{2±o(1)}`: every product
   subset of the ES avoider set has `log(1/δ)≍T^{1/2±o(1)}` (Prop 4.1; lower bound modulo
   Barban–Davenport–Halberstam, via the two-prime atoms `(ℓ_1ℓ_2,q)`). Extends POINTWISE_OMEGA Prop 6.1.
5. **Item (iii):** Cramér form CR(A) ⇒ LS ⇒ 1/3; the literal "any set of density δ mod Q" form is false.
6. **Consistency:** LS not refuted by fakes (they are reweightings of Haar onto the complement), provably
   not reachable by linear certificates; robust to Siegel zeros and Jacobsthal effects; matches SIZE.

## EVIDENCE
* N1: Buchstab compounding for primes (κ=1,2,3, x≤1e9).
* N2: least hard prime with W>T: LS ratio 0.64–1.29 for T≤2047; no hard p<1e11 has W>4095 (expected
  ~2–3.6; ratio >0.94). Scan of [1e11,1e12) was started in the background (may be cut by its 4 h timeout;
  output `data/omega16/esleast_1e11_1e12.*`, not committed if incomplete).
* N3: greedy adversarial κ-dimensional systems (z≤1000, κ≤8): LS ratio ≤1.15, adversary gains only
  ≈z^{0.9} over the random model, independent of κ.

## Points for the reviewer
* Prop 4.1(b): the BDH application (π-form on `(x/2,x]`, moduli `4q`), and the CRT-product avoidance criterion.
* Prop 3.1: scope = O15 Def 2.1 linear certificates; the fake matches all level-`≤x` statistics exactly.
* Prop 2.1(b) is an Assessment (HL heuristic), not a theorem.
* Novelty: none claimed for LS as a heuristic principle; the ES-specific content is Thm 1.2, Prop 3.1,
  Prop 4.1.
