# Reproduce exact I3 census for n<=100000, 3<=t<=20.
covered=set()
for t in range(3,21):
 c=0; st=set()
 for u in range(3,100003//(3*t-1)+1):
  a=t*u-1
  for v in range(3,(100000+u)//a+1):
   n=a*v-u
   if 2<=n<=100000:c+=1; st.add(n)
 covered.update(st)
 print(t,c,len(st))
print('union',len(covered),'uncovered',99999-len(covered))
