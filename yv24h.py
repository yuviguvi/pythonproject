t,k=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in range(0,t):
    for j in range(i+1,t):
        s=l[i]+l[j]
        if s==k:
            c+=1
if c>=1:
    print("YES")
else:
    print("NO")
