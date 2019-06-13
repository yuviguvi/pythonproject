n=int(input())
t=list(map(int,input().split()))
x=[1]*n
for i in range(n):
    if i==0:
        if t[i]>t[i+1]:
            x[i]=x[i]+x[i+1]
    elif i>0:
        if t[i]>t[i-1]:
            x[i]=x[i]+x[i-1]
print(sum(x))
