n,y=map(int,input().split())
e=[]
for i in range(y):
  e.append(list(map(int,input().split())))
z=10000000
f=0
for i in range(y):
  if e[i][0]==1:
    s=e[i][1]
    c=e[i][2]
    for j in range(i+1,y):
      if e[j][0]==s:
        s=e[j][1]
        c+=e[j][2]
    if c<z and s==n:
      z=c
      f+=1
if f==0:
  print(-1)
else:
  print(z)
