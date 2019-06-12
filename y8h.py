t,s,n=map(int,input().split())
x=0
for i in range(t,s+1):
    z=str(i)
    if z.find(str(n))==-1:
        pass
    else:
        x=x+1
print(x)
