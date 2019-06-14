n,m=map(int,input().split())
b=list(map(int,input().split()))
v=list(map(int,input().split()))
s=[]
c=0
for i in range(n):
    x=v[i]/b[i]
    s.append(x)
while m>=0 and len(s)>0:
    mindex=s.index(max(s))
    if m>=b[mindex]:
        c=c+v[mindex]
        m=m-b[mindex]
    b.pop(mindex)
    v.pop(mindex)
    s.pop(mindex)
print(c)
