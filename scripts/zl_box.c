/* zl_box.c -- O228 (STERILE_LOWER.md Lemma 1.1; R231 m4 / R232 m3 repair: was 'Lemma 2.1'): se_box.c (O219) with the cube-Minkowski factor w^w of (Cop) replaced by the
   l2-ball factor (sqrt(w)*2*Gamma(w/2+1)^{1/w}/sqrt(pi))^w (never larger than w^w). Everything else identical. */
/* se_box.c -- O219 (STERILE_EXPLICIT.md §3). Rigorous (outward-rounded, fail-closed) upper bound for
   D_P(N) = #{P-data (a,b,c,d,e): 4abd = N+e, a+b = ce, a <= b, r ∤ abcd} valid for EVERY odd N in [2^j, 2^{j+1}),
   by the box sum of Table 2 (routes H, A, C, D, E, F, G, tau3, I, J) with Lemma 1.3 / Cor 1.4 class-divisor counts.
   Usage: se_box P|Q j0 j1 q g T [W]  -> for N in [2^{j/q}, 2^{(j+1)/q}) prints "j  F(j)  F(j)/N0^{1/2} (P) or F(j)/N0^{0.7} (Q)  shares"
   Boxes have ratio lam = 2^s, s = 1/g if floor(j/(qT)) < 1, else s = floor(j/(qT)).  W = max lattice dim (default 24).
   Mode Q bounds D_Q(F) = #{N-points of Sigma^I_F with a <= b, r ∤ abcde} (M17 Lemma 2.1), boxes in (c, d, f).
   Error budget: 64-bit-mantissa long double (checked), every derived bound is <= ~30 correctly-rounded-or-few-ulp ops
   (glibc x87 libm assumed accurate to a few ulp), i.e. relative error < 1e-17, dominated by the 1e-15 directed padding
   UP/DN applied to every lower/upper bound before any floor/ceil/comparison; box endpoints are exact powers of 2.
   All quantities are long double; every input to a bound is rounded in the safe direction by a relative 1e-15,
   and the (Cop) inequality is required with a relative safety margin 1e-12.  Integers < 2^63 are exact.      */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <float.h>
typedef long double R;
static int W = 24;
#define UP(x) ((x) * (1.0L + 1e-15L))
#define DN(x) ((x) * (1.0L - 1e-15L))

/* ---- explicit divisor bounds: tau_k(n) <= C_k(eta) n^eta, C_k(eta) = prod_p max_k binom(k+kk-1,kk-1) p^{-eta k} ---- */
#define NETA 21
static R ETA[NETA], LC2[NETA], LC3[NETA];
static int isprime(long p){ if(p<2) return 0; for(long q=2;q*q<=p;q++) if(p%q==0) return 0; return 1; }
static R lC(R eta, int kk){
  R s = 0; long pmax = (long)ceill(powl((R)kk, 1.0L/eta)) + 1;
  for(long p=2;p<=pmax;p++){ if(!isprime(p)) continue;
    R lp = logl((R)p), best = 0, lb = 0; /* lb = log binom(k+kk-1,kk-1) */
    for(int k=1;k<100000;k++){
      lb += logl((R)(k+kk-1)) - logl((R)k);
      R v = lb - eta*k*lp;
      if(v > best) best = v;
      if(v < best - 1 && k > 4) break;  /* function is concave in k: once it drops below the max it keeps dropping */
    }
    s += best;
  }
  return UP(s) + 1e-12L;
}
static R ltau(R ln, R *LC){ R b = 1e300L; for(int i=0;i<NETA;i++){ R v = LC[i] + ETA[i]*ln; if(v<b) b=v; } return b; }

/* max over odd e <= E of 2^{omega(e)} (odd primorial bound) */
static R Omega(R E){ R pr = 1, om = 1; for(long p=3;;p+=2){ if(!isprime(p)) continue; if(pr*p > E) break; pr*=p; om*=2; } return om; }

/* Number of divisors of n (log n <= ln) in a unit class mod s (s >= smin) lying in [D0, D1]: upper bound.
   min of trivial floor((D1-D0)/s)+1, Cor 1.4 J(w-1), and tau(n). */
static R LMK[64];   /* LMK[w] >= log( sqrt(w) * 2 * (Gamma(w/2+1))^{1/w} / sqrt(pi) ), padded up; and <= log w */
static void initLMK(void){ for(int w=1; w<64; w++){ R v = 0.5L*logl((R)w) + logl(2.0L) + lgammal((R)w/2+1)/w - 0.5L*logl(3.14159265358979323846L);
  v = v + 1e-12L*(1+fabsl(v)); if(v > logl((R)w)) v = logl((R)w); LMK[w] = v; } }
static R cop(R ln, R smin, R D0, R D1){
  if(D0 < 1) D0 = 1;
  if(D1 < D0) return 0;
  D0 = DN(D0); D1 = UP(D1); ln = UP(ln); smin = DN(smin); if(smin < 1) smin = 1;
  R Delta = D1 - D0;
  R best = floorl(UP(Delta/smin)) + 1;
  R lt = ltau(ln, LC2); if(lt < logl(best)) best = floorl(expl(lt)) + 0; /* tau bound (floor of an upper bound is an upper bound) */
  if(best <= 1) return best;
  R lD0 = logl(D0);
  for(int w=2; w<=W; w++){
    if(best <= (R)(w-1)) break;           /* J>=1 so J(w-1) >= w-1 */
    for(int m=1; m<=w; m++){
      R lhs0 = w*LMK[w] + (R)m*(m+1)/2*ln;   /* + w(w-1)/2 * ln X  <  m w lD0;  LMK[w] = log of the l2-Minkowski factor (Lemma 1.1 of STERILE_LOWER) */
      R rhs = (R)m*w*lD0;
      R lXmax = (rhs - lhs0)/((R)w*(w-1)/2);
      lXmax -= 1e-12L*(fabsl(rhs)+fabsl(lhs0)+1)/((R)w*(w-1)/2);   /* safety margin */
      R Xmax = expl(lXmax) * (1.0L - 1e-15L);
      if(Xmax <= 0.5L) continue;
      R J = ceill(UP(Delta/(2*smin*(Xmax-0.5L))));
      if(J < 1) J = 1;
      /* re-verify (Cop) with this J (fail closed) */
      R X = UP(Delta/(2*smin*J)) + 0.5L;
      R lhs = lhs0 + (R)w*(w-1)/2*logl(X);
      if(!(lhs < rhs - 1e-12L*(fabsl(rhs)+fabsl(lhs0)+1))) continue;
      R v = J*(w-1);
      if(v < best) best = v;
    }
  }
  return best;
}


static const char *RN[] = {"H","A","C","D","E","F","G","tau3","I","J"};
static const char *RQ[] = {"AD","fa","AC","CD","Ea","Ed","tau3","fac","fca","fda"};
#define NR 10
#define NQ 10
static R boxP(R N0, R N1, R A, R C, R D, R lam, int *who){
  R nA = floorl(lam*A) - ceill(A) + 1, nC = floorl(lam*C) - ceill(C) + 1, nD = floorl(lam*D) - ceill(D) + 1;
  if(lam*A == floorl(lam*A)) nA -= 1; if(lam*C == floorl(lam*C)) nC -= 1; if(lam*D == floorl(lam*D)) nD -= 1; /* half-open */
  if(nA<=0||nC<=0||nD<=0) { *who=-1; return 0; }
  if(2*A*A*D > N1 || A*C*D > N1) { *who=-1; return 0; }
  R LA = UP(1.0L/A + logl(lam)), LD = UP(1.0L/D + logl(lam)), l3 = lam*lam*lam;
  R E0 = DN(N0/(4*l3*A*C*D)), E1 = UP(N1/(A*C*D));
  R b0 = DN(N0/(4*lam*lam*A*D)), b1 = UP(N1/(2*A*D));
  R f0 = 4*A*C*D-1, f1 = 4*l3*A*C*D;
  R se = floorl(E0)+1;
  R pe = UP((E1-E0)/4);
  R pairF = UP(pe*LA) + nA, pairG = UP(pe*LD) + nD;
  R Om = Omega(E1);
  R v[NR];
  v[0] = nA*nC*nD;
  v[1] = UP(pe*LA*LD) + nA*nD;
  v[2] = nA*nD*cop(logl(3*N1), 4*A*D, f0, f1);
  v[3] = nC*nD*cop(logl(4*l3*C*C*D*N1+1), 4*C*D, f0, f1);
  v[4] = nA*nC*cop(logl(lam*C*N1 + lam*A), 4*A*C, f0, f1);
  { R lm = logl((N1+E1)/(4*A)); R c1 = cop(lm, se, b0, b1), c2 = cop(lm, se, D, lam*D); v[5] = UP(pairF*(c1<c2?c1:c2)); }
  { R lm = logl((N1+E1)/(4*D)); R c1 = cop(lm, se, A, lam*A), c2 = cop(lm, se, b0, b1); v[6] = UP(pairG*Om*(c1<c2?c1:c2)); }
  v[7] = UP((pe+1)*expl(ltau(logl((N1+E1)/4), LC3)));
  v[8] = UP(nC*pairF); v[9] = UP(2*nC*pairG*Om);
  int k = 0; for(int q=1;q<NR;q++) if(v[q] < v[k]) k = q;
  *who = k; return v[k];
}
/* Q: N-points of Sigma^I_F: 4abcd = F(a+b)+c, e=(a+b)/c, f=4acd-F, ef=4a^2d+1, 4abd=eF+1, fb=aF+c, f(4bcd-F)=F^2+4c^2d.
   box: c in [C,lam C), d in [D,lam D), f in [P,lam P) (P = Phi); then a = (f+F)/(4cd). */
static R boxQ(R F0, R F1, R C, R D, R P, R lam, int *who){
  R nC = floorl(lam*C) - ceill(C) + 1, nD = floorl(lam*D) - ceill(D) + 1, nP = floorl(lam*P) - ceill(P) + 1;
  if(lam*C == floorl(lam*C)) nC -= 1; if(lam*D == floorl(lam*D)) nD -= 1; if(lam*P == floorl(lam*P)) nP -= 1;
  if(nC<=0||nD<=0||nP<=0) { *who=-1; return 0; }
  if(P > F1 + 2) { *who=-1; return 0; }                    /* f <= F+2 */
  R a0 = DN((P + F0)/(4*lam*lam*C*D)), a1 = UP((lam*P + F1)/(4*C*D));
  if(a0 < 1) a0 = 1;
  R nA = floorl(a1) - ceill(a0) + 1; if(nA <= 0) { *who=-1; return 0; }
  R E0 = DN(4*a0*a0*D/(lam*P)), E1 = UP((4*a1*a1*lam*D+1)/P);
  R bmax = UP((E1*F1+1)/(4*a0*D)); if(bmax < a0) { *who=-1; return 0; } /* b >= a */
  R b0 = DN((E0*F0)/(4*a1*lam*D)); if(b0 < a0) b0 = a0;
  R LA = UP(1.0L/a0 + logl(a1/a0 + 1e-300L) + 1.0L/a0), LD = UP(1.0L/D + logl(lam));
  R se = floorl(E0); if(se < 1) se = 1;
  R pe = UP((E1-E0)/4);
  R v[NQ];
  v[0] = 2*nA*nD;
  v[1] = nA*nP*(floorl(UP((lam-1)*D/P)) + 1);
  v[2] = nA*nC*cop(logl(a1*F1 + lam*C), 4*a0*C, P, lam*P);
  v[3] = nC*nD*cop(logl(F1*F1 + 4*lam*lam*lam*C*C*D), 4*C*D, P, lam*P);
  { R lm = logl((E1*F1+1)/(4*a0)); R x1 = cop(lm, se, b0, bmax), x2 = cop(lm, se, D, lam*D); v[4] = UP((UP(pe*LA)+nA)*(x1<x2?x1:x2)); }
  { R lm = logl((E1*F1+1)/(4*D)); R x1 = cop(lm, se, a0, a1), x2 = cop(lm, se, b0, bmax); v[5] = UP((UP(pe*LD)+nD)*Omega(E1)*(x1<x2?x1:x2)); }
  v[6] = UP((pe+1)*expl(ltau(logl((E1*F1+1)/4), LC3)));
  { /* f-routes: 4acd = f+F and f | 4a^2d+1 give c == -aF, d == -1/(4a^2), a == -c/F (mod f); f odd-free classes */
    R pf = UP((lam-1)*P/4);                       /* f in window with f == -F (mod 4x): <= pf/x + 1 per x */
    R LAa = 1.0L/a0 + logl(a1/a0) + 1e-18L, LC = 1.0L/C + logl(lam);
    R pa = UP(pf*LAa) + nA, pc = UP(pf*LC) + nC, pd = UP(pf*LD) + nD;
    R cc = floorl(UP((lam-1)*C/P)) + 1, dd = floorl(UP((lam-1)*D/P)) + 1, aa = floorl(UP((a1-a0)/P)) + 1;
    v[7] = UP(pa*(cc<dd?cc:dd));
    v[8] = UP(pc*aa);
    v[9] = UP(pd*Omega(lam*P)*aa);
  }
  int k = 0; for(int q=1;q<NQ;q++) if(v[q] < v[k]) k = q;
  *who = k; return v[k];
}
int main(int argc, char **argv){
  if(argc < 7){ fprintf(stderr,"usage: se_box P|Q j0 j1 q g T [W]\n"); return 2; }
  char mode = argv[1][0];
  int j0 = atoi(argv[2]), j1 = atoi(argv[3]), qq = atoi(argv[4]), g = atoi(argv[5]), T = atoi(argv[6]); if(argc>7) W = atoi(argv[7]);
  initLMK();
  for(int i=0;i<NETA;i++){ ETA[i] = 0.10L + 0.02L*i; LC2[i] = lC(ETA[i],2); LC3[i] = lC(ETA[i],3); }
  printf("# zl_box %c j0=%d j1=%d q=%d g=%d T=%d W=%d LDBL_MANT_DIG=%d\n", mode, j0, j1, qq, g, T, W, LDBL_MANT_DIG);
  if(LDBL_MANT_DIG < 64){ fprintf(stderr,"needs 64-bit long double mantissa\n"); return 2; }
  for(int j=j0;j<=j1;j++){
    if(g != 1){ fprintf(stderr,"only g=1 (integral dyadic boxes) is certified\n"); return 2; }
    int t = j/(qq*T); R s = (t < 1) ? 1.0L : (R)t;   /* boxes [2^{s i}, 2^{s(i+1)}): exact powers of 2 */
    R lam = ldexpl(1.0L, (int)s);
    R N0 = DN(powl(2.0L, (R)j/qq)), N1 = UP(powl(2.0L, (R)(j+1)/qq));   /* enclosure of the N-range */
    if(getenv("SE_EXACT")){ N0 = strtold(getenv("SE_EXACT"),0); N1 = N0*(1.0L+1e-15L); }   /* validation mode */
    int dump = getenv("SE_DUMP") != 0;
    R tot = 0, share[NR]; memset(share,0,sizeof share);
    int imax = (int)ceill((log2l(N1) + 2)/s) + 1;
    for(int i1=0; i1<=imax; i1++){ R X1 = ldexpl(1.0L, (int)s*i1);       /* P: A ; Q: C */
      for(int i2=0; i2<=imax; i2++){ R X2 = ldexpl(1.0L, (int)s*i2);     /* P: D ; Q: D */
        if(mode=='P' && 2*X1*X1*X2 > N1) break;
        if(mode=='Q' && X1*X2 > N1) break;
        R inner = 0, ish[NR]; memset(ish,0,sizeof ish); int any = 0;
        for(int i3=0; i3<=imax; i3++){ R X3 = ldexpl(1.0L, (int)s*i3); int who;   /* P: C ; Q: Phi */
          R v = (mode=='P') ? boxP(N0, N1, X1, X3, X2, lam, &who) : boxQ(N0, N1, X1, X2, X3, lam, &who);
          if(who < 0){ if(mode=='P' && X1*X2*X3 > N1) break; if(mode=='Q' && X3 > N1+2) break; continue; }
          inner += v; ish[who] += v; any = 1;
          if(dump) printf("B %.0Lf %.0Lf %.0Lf %.6Le\n", X1, X2, X3, v);
        }
        if(!any) continue;
        /* aggregated pair routes (all values of the third variable at once) */
        R n1 = floorl(lam*X1) - ceill(X1) + 1, n2 = floorl(lam*X2) - ceill(X2) + 1;
        if(lam*X1 == floorl(lam*X1)) n1 -= 1; if(lam*X2 == floorl(lam*X2)) n2 -= 1;
        R agg;
        if(mode=='P') agg = n1*n2*floorl(expl(ltau(logl(3*N1), LC2)));          /* (a,d): f | N+4a^2d */
        else          agg = n1*n2*floorl(expl(ltau(logl(N1*N1 + 4*lam*lam*lam*X1*X1*X2), LC2))); /* (c,d): f | F^2+4c^2d */
        if(dump) printf("R %.0Lf %.0Lf %.6Le\n", X1, X2, agg < inner ? agg : inner);
        if(agg < inner){ tot += agg; share[mode=='P'?2:3] += agg; }
        else { tot += inner; for(int q=0;q<NR;q++) share[q] += ish[q]; }
      }
    }
    if(!isfinite(tot) || tot < 0){ fprintf(stderr,"non-finite total at j=%d\n", j); return 3; }
    tot = UP(tot)*(1.0L+1e-9L);
    printf("%d %.10Le %.6Le", j, tot, tot/powl(N0, mode=='P'?0.5L:0.7L));
    for(int q=0;q<NR;q++) if(share[q] > 0.01L*tot) printf(" %s:%.2Lf", mode=='P'?RN[q]:RQ[q], share[q]/tot);
    printf("\n"); fflush(stdout);
  }
  return 0;
}
