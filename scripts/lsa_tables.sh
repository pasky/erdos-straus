#!/bin/sh
# O135 §3 tables from data/lsa (run scripts/lsa_run.sh first). Writes logs/lsa_tables.txt
gcc -O2 -o /tmp/lsa_census scripts/lsa_census.c
{
echo "== per-p summaries (cols: see scripts/lsa_census.c header)"
for f in data/lsa/cen_mh_le1e6_E2000.txt data/lsa/cen_sample_1e*_E5000.txt data/lsa/cen_hard_E20000.txt; do
awk -v f=$(basename $f) '{n++; sl+=$2+$3; P+=$6; TP+=$7; P20+=$15; TP20+=$16; if($15==0)z20++; if(minP20==""||$15<minP20){minP20=$15;am=$1}; mp+=$13; if(minmp==""||$13<minmp){minmp=$13;amp=$1}; om+=$9; if($13==$14)eq++}
 END{printf "%s n=%d sol-slices=%.1f P=%.2f TP=%.2f P20=%.2f TP20=%.2f #(P20=0)=%d minP20=%d@%s maxPphi:mean=%.0f,min=%d@%s [maxPphi attained transparently: %d/%d] mean max omega=%.2f\n",f,n,sl/n,P/n,TP/n,P20/n,TP20/n,z20,minP20,am,mp/n,minmp,amp,eq,n,om/n}' $f; done
echo "== by e-bin, first 100 primes of each sample, E=5000: per p  sol-slices / P / TP  (P = full coset -K_e covered)"
for k in 4 5 6 7 8; do head -100 data/lsa/mh_sample_1e$k.txt | /tmp/lsa_census 5000 1 | awk -v k=$k '$1=="S" {e=$3; b=(e<20)?"a:e<20":(e<100)?"b:e<100":(e<500)?"c:e<500":(e<2000)?"d:e<2000":"e:e<5000"; if($5>0)s[b]++; if($6==1)P[b]++; if($7==1)T[b]++} END{printf "1e%d:",k; n=asorti(s,ix); for(i=1;i<=n;i++){x=ix[i]; printf "  %s %.2f/%.2f/%.2f",substr(x,3),s[x]/100,P[x]/100,T[x]/100}; print ""}'; done
} > logs/lsa_tables.txt
cat logs/lsa_tables.txt
