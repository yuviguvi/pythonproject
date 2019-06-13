n,q=map(int,input().split())
m=list(map(int,input().split()))
s=[]
for i in range(q):
    s.append(list(map(int,input().split())))
for i in s:
  s1=0
  for j in range(i[0]-1,i[1]):
      s1=s1+m[j]
  print(s1)    
