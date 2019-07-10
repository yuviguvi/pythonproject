y=int(input())
u=3
v=3
i=1
for i in range(y-1):
    if(u==1):
        u=v*2
        v=u
    else:
        u=u-1
print(u)   
