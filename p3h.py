t=int(input())
x=0
n=str(t)
z=[]
for i in range(0,len(n)):
    x=x+int(n[i])
    z.append(x)
print(sum(z))
