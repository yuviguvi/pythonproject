t,s=map(int,input().split())
if(t<=s):
    d=t
else:
    d=s
l=[]
for i in range(0,d):
    l.append(sorted(list(map(int,input().split()))))
l=sorted(l)
for i in range(0,len(l[0])):
    for j in range(0,len(l)-1):
        if(l[j][i]>l[j+1][i]):
            l[j][i],l[j+1][i]=l[j+1][i],l[j][i]
for i in l:
  print(*i)
