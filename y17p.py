t,x=map(int,input().split())
a=list(map(int,input().split()))
z=a[:]
c=0
n=0
for i in a:
    z.remove(i)
    for j in z:
        if(n==0):
            if(i+j==x):
                print("yes")
                c=c+1
                n=n+1
    z=a[:]
if(c==0):
    print("no")
