t,s=map(int,input().split())
n=list(map(int,input().split()))
c=0
for i in range(0,t):
    for j in range(0,t):
        if n[i]-n[j]==s:
            c=c+1 
print(c)
