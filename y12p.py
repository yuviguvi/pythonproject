n,q=map(int,input().split())
t=list(map(int,input().split()))
s=[]
for i in range(q):
    s.append(list(map(int,input().split())))
for i in s:
  z=0
  for j in range(i[0]-1,i[1]):
      z=z+t[j]
  print(z)    
