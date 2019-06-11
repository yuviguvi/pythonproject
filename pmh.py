t,s=map(int,input().split())
z=0
for i in range(t,s):
    n=str(i)
    x=0
    for h in range(len(n)):
        x=x+int(n[h])
    c=0
    for i in range(1,s):
        if x%i==0:
            c=c+1
    if c==1:
        z=z+1 
print(z)
