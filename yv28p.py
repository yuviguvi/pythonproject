t=int(input())
n=list(map(int,input().split()))
n.sort()
s=0
c=0
for i in range(len(n)):
    if n[i]>=s:
        c=c+1
    s=s+n[i]
print(c
