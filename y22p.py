t=int(input())
s=list(map(int,input().split()))
b=[]
n=[]
for i in range(len(s)):
    if(i%2==0):
        b.append(s[i])
    else:
        n.append(s[i])
for j in b:
    d=sum(b)
for k in n:
    f=sum(n)
if(d>f):
    print(d)
else:
    print(f)
