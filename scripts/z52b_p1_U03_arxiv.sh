#!/bin/bash
# z52b Pass-1 U03: arXiv API lookups (title/author) for literature items. Prints id | date | title.
q() { for try in 1 2 3; do c=$(curl -s -w "%{http_code}" -o /tmp/ax.xml "https://export.arxiv.org/api/query?search_query=$1&max_results=2"); if [ "$c" = "200" ]; then break; fi; sleep 20; done; python3 -c "
import sys,re
x=open("/tmp/ax.xml").read()
for e in re.findall(r'<entry>(.*?)</entry>',x,re.S)[:2]:
    t=re.search(r'<title>(.*?)</title>',e,re.S).group(1).strip().replace('\n',' ')
    i=re.search(r'<id>(.*?)</id>',e).group(1); d=re.search(r'<published>(.*?)T',e).group(1)
    print(i.split('/abs/')[-1],d,t[:110])
"; sleep 10; }
while IFS='|' read -r key s; do echo "== $key"; q "$s"; done <<'LIST'
Z2081|ti:%22Goldbach-Linnik%22+AND+ti:powers+of+two
Z2082|ti:%22two+primes+and+powers+of+two%22
Z1278|ti:%22continued+fraction%22+AND+ti:%22Erdos-Straus%22
Z2421|ti:%22Landau-Siegel%22+AND+au:Zhang
Z2412|au:Ustinov+AND+ti:continued+fraction
Z2413|au:Petrow+AND+ti:Weyl+bound
Z2416|au:Pierce+AND+au:Wood+AND+ti:Chebotarev
Z2423|au:Drappeau+AND+au:Radziwill+AND+ti:one-level
Z2512|au:Holowinsky+AND+au:Soundararajan
Z2519|au:Stromberg+AND+au:Venkatesh+AND+ti:congruence
Z2522|au:Katz+AND+ti:Kloosterman
Z2525|au:Rudnick+AND+au:Soundararajan+AND+ti:moments
Z2578|au:Sawin+AND+ti:square-root+cancellation
Z2408|au:Harel+AND+au:Samotij
Z2411|au:Koukoulopoulos+AND+au:Maynard+AND+au:Yang
Z2402|au:Granville+AND+au:Koukoulopoulos+AND+au:Matomaki
Z2403|au:Ford+AND+au:Maynard+AND+ti:sieve
Z2387|au:Matomaki+AND+au:Radziwill+AND+au:Tao+AND+ti:uniformity
Z2382|au:Guth+AND+au:Maynard+AND+ti:Dirichlet
Z2380|au:Lichtman+AND+ti:Goldbach
Z2381|au:Fouvry+AND+au:Radziwill+AND+ti:distribution
Z2395|au:Bretheche+AND+au:Drappeau
Z2397|au:Dunn+AND+au:Kerr+AND+au:Shparlinski
Z2399|au:Fouvry+AND+au:Kowalski+AND+au:Michel+AND+ti:trace
Z2446|au:Peluse+AND+au:Prendiville
Z2462|au:Wooley+AND+ti:congruencing
Z2599|au:Munshi+AND+ti:delta
Z2603|au:Tao+AND+au:Teravainen+AND+ti:Chowla
Z2603b|au:Klurman+AND+au:Mangerel+AND+au:Teravainen
Z3054|au:Goldfeld+AND+ti:effective
Z2098|ti:Tatuzawa
Z2077|au:Bach+AND+au:Sorenson+AND+ti:explicit
Z2418|au:Platt+AND+au:Trudgian+AND+ti:zero-free
Z2078|au:Gupta+AND+au:Murty+AND+ti:primitive+root
Z2080|ti:Linnik+AND+ti:squares
Z2094|au:Hooley+AND+ti:x2+y2+z3
Z2096|au:Ford+AND+ti:divisors+in+short+intervals
Z2097|au:Hall+AND+au:Tenenbaum+AND+ti:divisors
Z2401|au:Irving+AND+ti:divisor
Z2401b|au:Liu+AND+au:Shparlinski+AND+au:Zhang+AND+ti:divisor
Z2404|au:Lichtman+AND+ti:primitive
Z2459|au:Solymosi+AND+ti:sum-product
Z2431|au:Bourgain+AND+ti:sum-product+composite
Z2320|au:Harman+AND+ti:representation
Z2356|au:Friedlander+AND+au:Iwaniec+AND+ti:parity
Z2564|au:Ford+AND+au:Green+AND+au:Konyagin+AND+au:Maynard+AND+au:Tao
Z2164|au:Burgess+AND+ti:character+sums
Z2303|ti:exceptional+set+circle+method
Z2189|ti:exceptional+set+Erdos
Z2298|au:Sawhney+AND+ti:prime
Z2611|au:Vaughan+AND+ti:exceptional
LIST
