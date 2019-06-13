t,s=map(int,input().split())
a=list(map(int,input().split()))
n=0
for i in range(0,s):
    u,v=map(int,input().split())
    s=a[u-1:v]
    for j in s:
        n=n^j
    print(n)
    n=0
