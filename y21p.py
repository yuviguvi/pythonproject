t=int(input())
s=list(map(int,input().split()))
x=y=u=k=0

for i in range(0,t-1):
    if i==0:
        x=(x+s[i])/(i+1)
    else:
        x=0
        for t1 in range(0,i):
            x=x+s[t1]
        x = (x + s[i]) // (i + 1)
    k=0
    for j in range(i+1,t):
        y=y+s[j]
        k=k+1
        if j==t-1:
            y=y//(k)
    if x==y:
        u=1
        print("yes")
if u==0:
    print("no")
