def fact(t):
    s=[]
    for i in range(1,t+1):
        if t%i==0:
            s.append(i)
    return(s)
t,m=map(int,input().split())
a=fact(t)
b=fact(m)
x=list(set(a+b))
if len(x)==len(a)+len(b)-1:
    print("yes")
else:
    print("no")
