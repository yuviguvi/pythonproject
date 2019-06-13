v,r=map(int,input().split())
o=list(map(int,input().split()))
t=[]
for i in range(0,r):
    f=[]
    f=list(map(int,input().split()))
    q=f[0]
    for j in range(min(f)-1,max(f)):
        if q>o[j]: q=o[j]
    t.append(q)
for i in range(0,len(t)):
    print(t[i])
