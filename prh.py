t=int(input())
s=[]
x=0
for i in range(3,t):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i%10==3:
            x=x+i
print(x)
