z=int(input())
n=list(map(int,input().split()))
x=0
for i in range(z):
    if sum(n[:i])==sum(n[i+1:]):
        x=x+1
if x>0:
    print("yes")
else:
    print("no")
