t,k=map(int,input().split())
s=[]
x=[]
for i in range(t):
    l=[int(s) for s in input().split()]
    s.append(l)
    if 0 in l:
        m=l.index(0)
        x.append(m)
for i in range(len(s)):
    if 0 in s[i]:
        for j in range(k):
            s[i][j]=0
for i in x:
    for j in range(t):
        s[j][i]=0
for i in s:
    print(*i)
