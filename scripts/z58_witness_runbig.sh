#!/bin/sh
# chunk i of 12 over (1e9, 1e10]
i=$1; lo=$((1000000001 + i*750000000)); hi=$((1000000000 + (i+1)*750000000))
ulimit -v 6000000
DCAP=0 QCAP=0 timeout 1700 /tmp/z58scan $lo $hi | awk '!/^#/ {s=($8<$10)?$8:$10; L=log($1); if($8<0||$10<0) {print "NOS",$0; fflush(); next} r=s/(L*L); if(r>m){m=r; print "REC",r,$0; fflush()} if(s>=30) {print "BIG",s,$0; fflush()} n++} END{print "DONE",n,m}' > big_$i.txt 2> big_$i.err
