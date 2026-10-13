# AGENT_REPORT_O175 — spark brainstorm B: sign layer, ray classes, SQ, function-field sterile point

Branch `side-agent/spark-signlayer`. **ES is not solved; no case of it is claimed.** Memos `BRAINSTORM/bsB_*.md`
(8, indexed in `BRAINSTORM/README.md`), deep file `SIGNLAYER_DEEP.md`, scripts `scripts/bsB_*`.

## SHARP:
1. **FF sterile point: Case B on the slice "x ≡ 1 off T" is a finite system per level, and only ≈ half the slice
   is covered** (`SIGNLAYER_DEEP.md` Lemma 1.1, §2). For q = 3, A = T², a Case B family valid at x_u is the same
   as monic h₁, h₁' with `h₁ + h₁' = T g' r`, `h₁h₁'L'' = T^K + r` and one T-adic congruence; L'', r are forced
   by (h₁, h₁', K), so each level K is a finite search (PROVED). This **refutes the divergence heuristic** of
   FUNCTIONFIELD_ES2 §0.2 (it summed over unbounded deg L'). Complete enumeration through K = 19 (CERTIFIED by exhaustive
   search, 1036 solutions; cross-validated against FF2's independent searcher): x*_{±1} uncovered; covered Haar
   measure of the slice 0.333 → 0.4906, increments shrinking (≈ 0.001/level); any family covering x* must be
   degree-lopsided (Lemma 3.2, PROVED) — EVIDENCE that ≈ 50 % of the slice is never covered.
   Case A: 0 hits at 4 further slice points (FF2's checker, deg ≤ 3). If this holds, O(3, T²) has positive
   measure on the slice and "no finite linear covering for q = 3, A = T²" holds for a *convergent-lottery*
   reason; x* is special only as a height-1 point (Lemma 3.1: covered set invariant under u ↦ u⁻¹,
   u(T) ↦ u(−T); x*-orbit = {1 ± T, 1/(1 ± T)}). A proof needs one explicit point excluded at all K — the
   suggested tool is the product formula (simultaneous approximation at 0 and ∞, §3). This is the item most
   worth a fresh agent.
2. **Sign-layer dictionaries (all PROVED, elementary; useful as a closed map):**
   the ES sign is (a) the sign of the ℤ/n-half of the transpose of the m × m'' rectangle (Zolotarev),
   (b) the weight-½ theta multiplier of the certificate matrix, (c) the real orthant of one cubic
   (class +1 = negative orthant of cfg − c − f = n), (d) the genus character χ_p on the anti-invariant part
   G[1+σ] of the ray class group. Ray-class/Hecke inputs use only χ∘N (Eisenstein; L(χ)L(χχ_K)), so WR
   Remark 10.4's ray-class "escape" is **pulled back from ℚ**. For prime t ≡ 3 (4), the 2-primary part of the
   class condition is exactly the genus sign: Rédei/governing-field/spin (2-power) information is vacuous;
   the rest is an odd-order (cubic, …) spin condition (H-D residue).

## What was done
| memo | result | label |
|---|---|---|
| bsB_zolotarev_transpose | sign = ℤ/n-half of an even transpose; class +1 generates only even perms | PROVED |
| bsB_theta_multiplier | sign = theta multiplier; **Shimura zero-propagation refuted** (W(105·k²) > 0); W zeros ≤ 2·10⁶ = squares + 26 composites, no prime | PROVED; EVIDENCE |
| bsB_rayclass_norm_pullback | only norm-pulled-back characters; sign = χ_p on G[1+σ] | PROVED |
| bsB_redei_oddpart | 2-primary = genus for prime t; 2-visible slices t = 3·(Fermat products) finite; ES class is the *least* populated non-residue class | PROVED; EVIDENCE |
| bsB_salie_duality | Type II as Γ₀(4) matrices with c = 4p, multiplier constant; Salié inapplicable (not Γ_∞-bi-invariant) | PROVED; Assessment |
| bsB_sterile_pretentious | sterile = maximally pretentious (anti-Siegel); F_q[T] Mordell transfer → degree parity only; corr(log L_y(1,χ_p), W(p)/log²p) = −0.49 | PROVED; EVIDENCE |
| bsB_orthant_sign | sign = real orthant; orthant-crossing maps barred | PROVED |
| bsB_root_number_parity | BSD-parity template fails (rational points free; no fixed module); P(W(p) odd) ∈ [0.47, 0.52] over 32 local classes | Assessment; EVIDENCE |

Barrier verdicts: every sign-layer route is the genus bit at n (B5/T1-consistent) and needs the class layer (B2/H-A).
The brief's three favourites: Zolotarev (dictionary, no route), Waldspurger/half-integral weight (dictionary; the
structural Shimura prediction fails numerically), Rédei/governing fields (provably vacuous beyond genus for prime t).

## Checks / reproducibility
`bsB_sign_dict.py 400` (352 certs, 0 viol.), `bsB_genus_pullback.py 200000` (9859, 0), `bsB_oddpart.py 100000 130000`
(0 viol.), `bsB_typeII_mult.py 400` (472, 0), `bsB_orthant.py 300` (0), `bsB_wcount.c 2000000` (W table; T1 control:
W(k²) = 0 for all odd k), `bsB_pretend.py`, `bsB_parity.py`, `bsB_caseB.c 17` + `bsB_caseB_cover.py` (counts in
`data/bsB_caseB_K17_counts.txt`). K ≤ 19 run done: x* still uncovered, covered measure 0.4906 (`data/bsB_caseB_K19_counts.txt`).
Caveat: Lemma 1.1 relies on FF2 §0.2's Case B reduction ("valid Case B family ⟺ D = EE' with the congruences"),
which FF2/R166 state and use; I re-derived only the step from there.

## Sparks (not pursued)
* Prove sterility of one explicit slice point for all K via the product formula on P¹ (approximation at 0 and ∞;
  Lemma 1.1 makes it a two-place Diophantine approximation statement); or prove Case A empty on the whole slice.
* Is the Case-B-covered measure of the slice exactly 1/2 in the limit (a hidden involution/character)?
* Odd-order spins (bsB_redei_oddpart item 4): cubic-spin equidistribution at fixed p is the cleanest H-D-shaped
  residue of the class condition for t ≡ 1 (mod 3).
* The 26 non-square zeros of the single slice W: all composite with small factors; does every one have
  Type I/II via other slices (SQ check beyond SQ₅'s 105)?
