t=int(input())
s=list(map(int,input().split()))
n=g=[]
for i in range(0,t):
    n=list(bin(s[i]))
    n=n[2:]
    g.append(n)
g=sorted(g)
g=g[::-1]
for i in range(0,t):
    y=1
    z=0
    for j in range(len(g[i])-1,-1,-1):
        z=z+(int(g[i][j])*y)
        y=y*2
    print(z)
