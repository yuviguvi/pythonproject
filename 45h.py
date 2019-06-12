t=int(input())
n=list(map(int,input().split()))
s=0
for i in range(0,t+1):
    if t*i in n:
        s=s+1
print(s)
