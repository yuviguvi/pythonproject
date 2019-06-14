t,s=map(int,input().split())
l=list(map(int,input().split()))
if s==1:
    print(min(l))
elif s==2:
    print(max(l[0],l[t-1]))
else:
    print(max(l))
