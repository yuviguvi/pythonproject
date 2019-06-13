#yv
s,n=map(int,input().split())
p=list(map(int,input().split()))
z=[]
for i in range(0,n):
    f=[]
    f=list(map(int,input().split()))
    m=f[0]
    for j in range(min(f)-1,max(f)):
        if m>p[j]: m=p[j]
    z.append(m)
for i in range(0,len(z)):
    print(z[i])
