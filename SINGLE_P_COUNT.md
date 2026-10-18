# SINGLE_P_COUNT — counting at one prime: the height-dependent target (task O260, route (a))

Status: O260 working draft. **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md (PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Scripts `scripts/z30_*`, memos `BRAINSTORM/z30_*.md`, tiny logs `logs/z30_*`.

**Prior work this builds on (and does not redo).** CONDITIONAL_ES ((I)2: Prop 2.3 scale constraint, Prop 3.1 "|S₁| < S₀ must
be square-sensitive", Prop 7.3 local-data hypotheses fail at odd squares, Prop 9.1 termwise GRH misses by p^{1−o(1)}, §5 ranked
table of standard hypotheses); POINTWISE_SPECTRAL ((I)3: "a sufficient statement must be Planck-scale, polylog-accurate and
genus-aware"); PARITY_AUDIT ((J)87: R = M + E, |E| ≪ p^{2/5+o(1)}, tied modulus ⟺ height-dependent target); SYNTHESIS_SPARKS8
((J)89) and B1_LINE ((J)90: census, overdispersion D growing 2.2 → 3.6); s7_lvalue_proxy (hardness ≈ QR-richness, EVIDENCE).
What is new here is listed in §0.

## 0. Summary of new content (updated as the work proceeds)

* §1 (PROVED): exact forms of (★): coprime-pair congruence form, divisor form (brief's (★) corrected: no √-cut, R(p) even),
  and an SL₂(ℤ) form with fixed upper-right entry p (γ ∈ −Γ₁(c(γ))).
* §2 (PROVED): **genus split** R(n) = M_gen(n) + X(n) for every odd n, where M_gen ≥ 0 is the exact contribution of all
  characters of order ≤ 2 (an explicit, computable "genus-corrected main term") and X is the order-≥3 part. M_gen(m²) = 0 and
  X(m²) = 0 identically. M_gen(n) > 0 ⟺ (★) is solvable at n·x² for some x (the square-class relaxation).

## 1. Exact forms of the single-p event (★)

For odd n ≥ 3 put R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (Type II with c = 1; PARITY_AUDIT §0, the "c = 1 line" of
SYNTHESIS_SPARKS8, López's Type B).

**Lemma 1.1 (PROVED, elementary).** Let p ≥ 3 be prime. Then
1. (pair form) R(p) = #{(u, B) ∈ ℕ² : gcd(u, B) = 1, p ≡ −(u + B) (mod 4uB)};
2. (divisor form) R(p) = Σ_{C ≥ 1} #{d ≥ 1 : d | 4Cp + 1, d ≡ −1 (mod 4C)}; the cofactor (4Cp+1)/d is then automatically
   ≡ −1 (mod 4C), and R(p) = 2·Σ_C #{d | 4Cp+1 : d ≡ −1 (4C), d < √(4Cp+1)}; in particular R(p) is even;
3. (SL₂ form) R(p) = #{γ = (a p; c d) ∈ SL₂(ℤ) : c ∈ 4ℕ, a, d ≥ 1, a ≡ d ≡ −1 (mod c)}, and every such γ factors as
   γ = Tᵘ·(−1 0; c −1)·Tᴮ with T = (1 1; 0 1), a = uc − 1, d = Bc − 1, c = 4C.

*Proof.* (1) A triple gives 4uB | p + u + B with C = (p+u+B)/(4uB); gcd(u, B) divides p, and gcd = p would force u, B ≥ p and
4uBC − u − B ≥ 4uB − u − B > p. Conversely, if 4uB | p + u + B then C := (p+u+B)/(4uB) is a positive integer (p + u + B > 0).
(2) (4uC − 1)(4BC − 1) = 4C(4uBC − u − B) + 1 = 4Cp + 1, so (u, B, C) ↦ (C, d = 4uC − 1) is a bijection onto pairs
(C, d) with d | 4Cp + 1, d ≡ −1 (mod 4C) (u = (d+1)/(4C), B = ((4Cp+1)/d + 1)/(4C), the latter integral since
d·d′ ≡ 1 and d ≡ −1 force d′ ≡ −1 mod 4C). The swap (u, B) ↔ (B, u) is a fixed-point-free involution (u = B would give
u | p, so u = 1 and 4C − 2 = p, impossible for odd p), and it exchanges d < √(4Cp+1) with d′ > √(4Cp+1).
(3) Tᵘ(−1 0; c −1)Tᴮ = (uc − 1, (uc − 1)B − u; c, cB − 1), whose upper-right entry is ucB − u − B = p for c = 4C.
Conversely, given γ, put u = (a + 1)/c, B = (d + 1)/c; det γ = 1 gives (uc − 1)(Bc − 1) − pc = 1, i.e. ucB − u − B = p. ∎

*Remarks.* (i) The brief's "(★) = Σ_C #{d | 4Cp+1 : d ≡ −1 (4C), d < √(4Cp+1)}" counts unordered solutions = R(p)/2.
(ii) In (3) the condition is −γ ∈ Γ₁(|c|) with c the matrix's own lower-left entry: the SL₂ shadow of the height-dependent
target of PARITY_AUDIT Remark 3.1. Equivalently p is the Hirzebruch–Jung (minus) continuant of the length-3 word (u, 4C, B).
(iii) In (1) the pair set depends on p only through size; the arithmetic of p enters only through the residue p mod 4uB.
