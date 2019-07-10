t,s=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
if set(y).issubset(set(x)):
    print("YES")
else:
    print("NO")
