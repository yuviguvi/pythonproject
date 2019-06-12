n=int(input())
a=str(n)
c=0
for i in range(len(a)):
    c=c+int(a[i])
j=3
while j>0:
    c=(c*10)+9
    h=str(c)
    s=0
    for i in range(len(h)):
        s=s+int(h[i])
    if s==n:
        print(c)
        break
