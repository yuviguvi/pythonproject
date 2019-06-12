t=int(input())
s=list(map(int,input().split()))
x=s
c=[]
while(len(x)!=1):
    for i in range(len(x)):
        if i%2!=0:
            c.append(x[i])
    x=c
    c=[]
print(s.index(x[0]))
