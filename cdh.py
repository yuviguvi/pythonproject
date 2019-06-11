t,s=map(str,input().split())
if len(t)>len(s):
    n=len(t)-len(s)
    for i in range(1,n+1):
        s=s+str(i)
else:
    n=len(s)-len(t)
    for i in range(1,n+1):
        t=t+str(i)
x=""
for i in range(0,len(t)):
        x=x+t[i]+s[i]
print(x)
