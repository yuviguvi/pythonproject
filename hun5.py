n=list(map(str,input()))
p=t=0
for i in range(0,len(n)-1):
  q=n[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+n[j]
    if int(q)<27 and int(q)>0: p=p+1
    elif int(q)==0: p=p-1
    else: break
if p!=1: t=p%2
print(p+t+1)
